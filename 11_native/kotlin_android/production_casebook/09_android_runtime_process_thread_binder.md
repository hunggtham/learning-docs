# Case 09 — Android Runtime: Process, Thread, Looper, Binder, ART và Memory

Ở các chapter trước, ta nhìn Android từ phía application architecture: UI, ViewModel, repository, database, network và release. Nhưng đến một mức độ nhất định, nhiều bug không thể giải thích chỉ bằng kiến trúc tầng cao. Vì sao một callback chạy trên main thread? Vì sao một app có thể ANR dù không crash? Vì sao truyền một object lớn qua `Bundle` đôi khi làm app chết ở nơi rất khó đoán? Vì sao process có thể biến mất nhưng task/back stack vẫn được hệ thống phục hồi? Vì sao một `suspend` function không đồng nghĩa với background thread? Vì sao một singleton không phải “sống suốt đời app”? Những câu hỏi này nằm ở tầng **Android runtime**.

Chapter này xây mental model từ dưới lên: Linux process → Android process lifecycle → main thread → `Looper` / `MessageQueue` / `Handler` → Binder IPC → ART/runtime/memory → process death. Mục tiêu không phải biến Android developer thành OS engineer, mà giúp bạn debug đúng khi abstraction phía trên bị rò rỉ.

## 1. Một Android app không phải là một process sống vĩnh viễn

Khi người dùng cài app, Android không tạo một process thường trực cho app. Process chỉ được tạo khi hệ thống cần chạy một component của app, chẳng hạn khi user mở Activity, một BroadcastReceiver được kích hoạt, một Service cần chạy hoặc ContentProvider được truy cập. Sau đó, Android có thể giữ process trong memory để tái sử dụng, nhưng không có lời hứa rằng process sẽ tồn tại cho tới khi user “đóng app”.

Điều này dẫn tới một nguyên tắc rất quan trọng: **process lifetime không phải application lifetime theo góc nhìn business**. User có thể nghĩ rằng họ “đang ở màn hình chi tiết sản phẩm”, nhưng process chứa ViewModel, singleton và object heap của bạn có thể đã bị kill khi app ở background. Khi user quay lại, Android có thể tạo process mới rồi reconstruct Activity/task state dựa trên thông tin hệ thống lưu được.

Vì vậy một singleton Kotlin như:

```kotlin
object SessionCache {
    var accessToken: String? = null
}
```

chỉ singleton **trong một process cụ thể**. Nó không phải persistence. Nếu process chết, object chết. Nếu app dùng nhiều process, mỗi process thậm chí có singleton riêng.

## 2. Linux process và Android sandbox

Mỗi Android app thông thường chạy dưới một Linux UID riêng. UID này là nền tảng của application sandbox: file private của app, process permission và nhiều security boundary được kernel thực thi dựa trên identity này. Android framework bổ sung thêm permission model, SELinux policy, Binder identity và package-level policy bên trên.

Một process app thường chứa Android Runtime (ART), heap managed cho Kotlin/Java object, native heap cho C/C++ hoặc native allocation, thread stack, mapped libraries, graphics resource và các vùng memory khác. Khi nói “app dùng 300 MB RAM”, đừng tự động nghĩ toàn bộ là Kotlin object trong heap. Bitmap, graphics buffer, native codec, database page cache và memory-mapped file có thể chiếm phần đáng kể.

## 3. `Application` không phải nơi đảm bảo dữ liệu sống lâu

`Application.onCreate()` chạy khi process được tạo, trước phần lớn component app. Vì thế nó phù hợp để thiết lập dependency graph, logging infrastructure hoặc library cần process-wide initialization. Nhưng `Application` object chỉ tồn tại cùng process.

Một anti-pattern phổ biến là dùng `Application` như database tạm:

```kotlin
class MyApp : Application() {
    var selectedOrder: Order? = null
}
```

Nếu process chết rồi screen được restore, `selectedOrder` trở lại `null`. Nếu dữ liệu cần khôi phục, hãy lưu identifier nhỏ trong saved state và reconstruct từ Room/backend, hoặc persist dữ liệu thực sự vào storage phù hợp.

## 4. Main thread là event loop, không phải “thread dành riêng cho UI code” theo nghĩa đơn giản

Khi Android tạo process application thông thường, framework thiết lập một main thread. Thread này chạy event loop xử lý input, lifecycle callback, message framework, rendering coordination và phần lớn callback UI.

Mental model quan trọng là:

```text
Message / Runnable / framework event
              ↓
         MessageQueue
              ↓
            Looper
              ↓
         main thread
              ↓
    xử lý callback từng lượt
```

Main thread không “chạy UI liên tục”. Nó nhận công việc từ queue rồi xử lý tuần tự. Nếu một callback chiếm thread quá lâu, các input/render/lifecycle message phía sau không được xử lý đúng thời điểm. Đây là nền tảng của jank và ANR.

## 5. `Looper`, `MessageQueue`, `Handler`

`Looper` là abstraction chạy vòng lặp lấy message từ `MessageQueue` và dispatch chúng. Main thread có main `Looper`. `Handler` là API truyền thống để post `Runnable` hoặc message vào queue gắn với một Looper.

Ví dụ:

```kotlin
val mainHandler = Handler(Looper.getMainLooper())

mainHandler.post {
    // chạy trên main thread ở một lượt event loop tương lai
}
```

Code hiện đại thường không dùng `Handler` trực tiếp cho application concurrency vì coroutine cung cấp abstraction tốt hơn, nhưng hiểu Handler/Looper vẫn quan trọng vì nhiều Android API, View system và library cũ dựa trên cơ chế này.

Android 17 thay đổi implementation của `MessageQueue` cho app target API 37+, theo hướng lock-free. Application bình thường không nên phụ thuộc private field của `MessageQueue`; thay đổi này là ví dụ điển hình cho lý do không reflection vào implementation detail của framework.

## 6. Coroutine không thay thế event loop; nó chạy bên trên scheduler/thread

Một `suspend` function không tự động chạy background:

```kotlin
suspend fun loadUser() {
    val user = repository.getUser()
}
```

Nếu `repository.getUser()` thực hiện CPU-heavy work trực tiếp và coroutine đang ở `Dispatchers.Main`, CPU work vẫn chiếm main thread. `suspend` chỉ có nghĩa function có thể **suspend và resume** mà không giữ nguyên call stack kiểu blocking truyền thống.

Khi dùng:

```kotlin
withContext(Dispatchers.IO) {
    blockingDatabaseCall()
}
```

coroutine được chuyển sang dispatcher khác cho block đó. Khi dùng API suspend-native như Room suspend DAO hoặc Retrofit coroutine adapter, library thường đã quản lý thread phù hợp theo contract của nó; đừng thêm `withContext(IO)` theo thói quen nếu không cần.

Senior rule là hỏi: **operation này blocking hay non-blocking, CPU-bound hay IO-bound, và API contract nói gì về execution context?** chứ không phải “mọi suspend đều background”.

## 7. Main-safety

Một function được gọi từ main thread nên “main-safe”: nó không làm blocking IO hoặc CPU work đủ lớn để gây lag. Một design tốt thường để layer sở hữu operation tự đảm bảo main-safety.

Ví dụ:

```kotlin
class ImageHasher(
    private val defaultDispatcher: CoroutineDispatcher
) {
    suspend fun hash(bytes: ByteArray): String =
        withContext(defaultDispatcher) {
            expensiveHash(bytes)
        }
}
```

Caller không cần biết implementation dùng CPU nhiều. Điều này giảm việc dispatcher logic bị rải khắp UI/ViewModel.

## 8. Frame budget và jank

UI 60 Hz có khoảng 16.67 ms cho mỗi frame; màn hình refresh cao hơn có budget nhỏ hơn. Không phải toàn bộ budget thuộc application code, vì rendering pipeline còn có measure/layout/draw, GPU work và system overhead.

Nếu main thread bị block 50 ms, user có thể thấy dropped frames. Nếu bị block lâu hơn nhiều trong những context nhất định, hệ thống có thể coi app không phản hồi và tạo ANR.

Performance work vì vậy bắt đầu bằng đo trace/frame/jank, không bằng nhìn code rồi đoán rằng một function “có vẻ chậm”.

## 9. ANR khác crash

Crash xảy ra khi process gặp exception/fatal signal không được xử lý và kết thúc. ANR xảy ra khi app vẫn tồn tại nhưng không đáp ứng đúng thời hạn mà framework yêu cầu cho một operation quan trọng, phổ biến nhất là main thread không xử lý event đủ nhanh.

Nguồn ANR thường gồm blocking IO trên main, lock contention/deadlock, synchronous Binder call quá lâu, BroadcastReceiver làm việc quá nhiều, startup quá nặng hoặc thread pool starvation gián tiếp làm main chờ.

Một bug có thể không xuất hiện trong local testing vì network/dev machine nhanh, nhưng xuất hiện production trên device chậm. Vì vậy StrictMode, tracing và representative hardware quan trọng.

## 10. `StrictMode` như development guardrail

`StrictMode` có thể phát hiện một số hành vi không mong muốn như disk/network access trên main thread trong development. Nó không thay profiling, nhưng rất hữu ích để biến “performance smell” thành tín hiệu sớm.

Ví dụ conceptual:

```kotlin
if (BuildConfig.DEBUG) {
    StrictMode.setThreadPolicy(
        StrictMode.ThreadPolicy.Builder()
            .detectAll()
            .penaltyLog()
            .build()
    )
}
```

Không nên bật penalty phá app một cách mù quáng trong production. Mục tiêu là dùng StrictMode để phát hiện boundary violation trong dev/test.

# Binder — xương sống IPC của Android

## 11. Tại sao Android cần IPC

Nhiều thứ application gọi thực tế sống ở process khác: ActivityManager, PackageManager service, system service, media service và các component hệ thống khác. Android dùng **Binder** làm cơ chế IPC chủ đạo để process gọi qua boundary an toàn hơn so với chia sẻ memory tùy ý.

Khi bạn gọi một method trông như local Java/Kotlin call, object phía sau có thể là Binder proxy gửi transaction sang process khác.

Mental model:

```text
App process
  proxy
    │ Binder transaction
    ▼
Kernel Binder driver
    │
    ▼
System/server process
  Binder stub
```

## 12. IPC không miễn phí

Binder call có serialization/marshalling, context switching, scheduling và giới hạn transaction. Vì vậy tránh thiết kế chatty IPC ở hot path.

Ví dụ, gọi system service hàng nghìn lần trong loop có thể tốn hơn việc batch/caching hợp lý. Nhưng cũng không nên cache dữ liệu hệ thống vô hạn nếu contract yêu cầu freshness.

## 13. `Bundle`, `Intent` và transaction size

`Bundle`, Intent extras và saved state thường đi qua Binder hoặc infrastructure có giới hạn kích thước. Truyền object graph lớn là lỗi thiết kế.

Đừng làm:

```kotlin
intent.putExtra("whole_result_list", hugeParcelableList)
```

Nên truyền ID nhỏ:

```kotlin
intent.putExtra("order_id", orderId)
```

rồi reconstruct data từ repository/source of truth ở destination.

Điều này không chỉ tránh `TransactionTooLargeException`, mà còn làm state restoration ổn định hơn.

## 14. Parcelable không phải persistence format

`Parcelable` tối ưu cho IPC/in-process Android boundary, không phải schema lưu trữ dài hạn. Không lưu raw Parcel vào database/file rồi kỳ vọng version sau đọc ổn định.

Cho persistence, dùng schema rõ ràng: Room, Proto/DataStore, JSON/CBOR/protobuf tùy use case.

## 15. Binder thread pool và callback threading

Không phải Binder callback nào cũng chạy main thread. Một Binder service có thread pool xử lý incoming transaction. Nếu bạn tự viết Service/AIDL hoặc tương tác low-level IPC, phải đọc contract threading rõ ràng.

Nếu callback từ background/Binder thread cần mutate UI state, chuyển sang lifecycle-aware/main-safe path phù hợp. Ngược lại, đừng ép mọi callback sang main nếu processing nặng không cần UI.

## 16. Binder identity và security boundary

Khi system/service xử lý Binder call, caller identity có ý nghĩa security. Custom exported component/service phải validate caller/permission nếu nhận dữ liệu nhạy cảm. Không nên nghĩ rằng “đây là app nội bộ nên Intent/Binder input chắc chắn hợp lệ”.

Mọi external input nên được xem là untrusted boundary.

# ART, bytecode và runtime

## 17. Kotlin không chạy trực tiếp như source code

Kotlin/JVM source được compile thành JVM bytecode/class representation, Android build pipeline tiếp tục chuyển đổi thành DEX để ART thực thi. D8 xử lý dexing/desugaring; R8 có thể shrink, optimize và obfuscate.

Pipeline giản lược:

```text
Kotlin source
→ Kotlin compiler / K2 frontend + backend
→ JVM bytecode
→ D8 / R8
→ DEX
→ ART
```

Điều này giải thích vì sao Java interoperability, generic erasure, synthetic method, bridge method, boxing và reflection đều có thể ảnh hưởng Android app dù code viết bằng Kotlin.

## 18. AOT, JIT và profile-guided optimization

ART có thể dùng nhiều cơ chế compile/runtime optimization tùy Android version và trạng thái app. Developer không nên cố “điều khiển JIT” như JVM server app. Thứ có thể kiểm soát tốt hơn ở app layer là startup path, code size, class loading, Baseline Profile và hot path design.

Baseline Profile giúp runtime biết những code path quan trọng nên được tối ưu sớm, giảm cold-start/jank cho path điển hình.

## 19. Class loading và startup

Nếu app có quá nhiều initialization eager ở `Application.onCreate()`, cold startup tăng. Mỗi SDK analytics, DI graph lớn, reflection scan, database open hoặc synchronous disk read đều có thể cộng dồn.

Senior approach là phân loại initialization:

| Nhóm | Cách nghĩ |
|---|---|
| bắt buộc trước first frame | giữ tối thiểu |
| cần sớm nhưng không trước first frame | defer |
| chỉ cần khi feature dùng | lazy/on-demand |
| background durable | cân nhắc WorkManager |

Không tối ưu startup bằng cách chuyển tất cả sang thread nền mà không xét dependency; race condition có thể thay performance bug bằng correctness bug.

# Memory

## 20. Managed heap không phải toàn bộ memory

Kotlin/Java object sống trong managed heap do GC quản lý, nhưng app còn dùng native memory, graphics buffer, bitmap, SQLite/native library memory và mapped file.

Một profiler chỉ nhìn Java heap có thể không thấy toàn bộ vấn đề.

## 21. Garbage Collection không phải leak detector

GC thu object không còn reachable. Nếu object vẫn reachable vì reference chain không mong muốn, GC không thể giải phóng nó.

Ví dụ leak Android kinh điển:

```text
process singleton
→ listener
→ Activity
→ View tree
→ large bitmap/resources
```

Nếu singleton giữ listener của Activity sau destroy, toàn graph còn reachable.

## 22. `Context` leak

`Activity` Context giữ nhiều state gắn với window/UI. Không giữ Activity trong singleton/static object lâu hơn lifecycle.

Nếu dependency chỉ cần process-level context, inject `ApplicationContext`. Nhưng cũng không biến `ApplicationContext` thành giải pháp mặc định cho mọi thứ; một số API cần themed/activity context.

Câu hỏi đúng là **dependency cần lifetime/context capability nào?**

## 23. Listener và coroutine leak

Coroutine có structured concurrency tốt hơn thread/callback tự do, nhưng vẫn leak work nếu scope ownership sai.

Ví dụ `GlobalScope.launch` trong ViewModel khiến work không bị cancel cùng ViewModel. Tương tự, callback/listener đăng ký mà không unregister sẽ giữ owner sống.

Ownership map nên rõ:

```text
Composable effect → Composition
ViewModel coroutine → viewModelScope
Lifecycle collection → lifecycleScope / repeatOnLifecycle
durable background work → WorkManager
process-level work → application-owned scope nếu thật sự cần
```

## 24. Bitmap và image memory

Image decoding có thể dùng memory lớn. Không load ảnh full-resolution chỉ để hiển thị thumbnail. Dùng image loading library có decode/downsample/cache policy đúng. Với app widget/RemoteViews, Android 17 target 37+ còn áp memory limit rõ hơn cho combined Bitmap/Icon trong parcel, cho thấy platform ngày càng siết resource misuse.

## 25. Low-memory và process reclaim

Android có thể reclaim background process để giải phóng memory. Developer không được dựa vào callback kiểu “sẽ luôn được báo trước khi process bị kill”. Hãy thiết kế như process có thể mất mà không có cơ hội cleanup business state.

Nếu dữ liệu quan trọng chỉ tồn tại trong RAM, đó là data-loss bug chờ xảy ra.

# Process death và state restoration

## 26. Configuration change khác process death

Rotation/window resize có thể recreate Activity nhưng process vẫn sống. ViewModel thường survive configuration change.

Process death thì ViewModel, singleton và heap biến mất. Android có thể restore navigation/task/activity state đủ để đưa user về màn hình gần trước đó, nhưng application memory không được phục hồi tự động.

Bởi vậy test rotation thôi chưa đủ; cần test **Don't keep activities** chỉ giúp một phần và không hoàn toàn tương đương process kill thật. Với flow quan trọng, cần test restore từ saved state + persistent source of truth.

## 27. State classification

Một cách phân loại thực dụng:

| State | Ví dụ | Owner/persistence |
|---|---|---|
| ephemeral UI | pressed state, animation progress | `remember` |
| restorable UI | tab/page nhỏ | `rememberSaveable` |
| screen business state | loading/filter/result | ViewModel |
| restore key | query/orderId/draftId | `SavedStateHandle` |
| durable local data | entity, pending sync | Room/DataStore |
| authoritative remote | account/order server state | backend |

Không cố lưu mọi thứ vào `SavedStateHandle`; saved state phải nhỏ và reconstructive.

# Thread safety

## 28. “Chỉ dùng coroutine” không tự động thread-safe

Nếu nhiều coroutine cùng mutate shared state trên dispatcher đa thread, race condition vẫn tồn tại.

Ví dụ:

```kotlin
var counter = 0

coroutineScope {
    repeat(1000) {
        launch(Dispatchers.Default) {
            counter++
        }
    }
}
```

`counter++` không atomic. Giải pháp có thể là confinement, immutable state reducer, `Mutex`, atomic primitive hoặc database transaction tùy loại state.

## 29. Confinement thường đơn giản hơn lock

UI state thường tốt khi mutation được serialize trong một owner (ViewModel/reducer). Thay vì nhiều layer cùng mutate `MutableStateFlow`, expose immutable state và funnel event qua một mutation path.

```kotlin
private val _uiState = MutableStateFlow(UiState())
val uiState: StateFlow<UiState> = _uiState
```

Không đưa `_uiState` ra ngoài.

## 30. Deadlock và lock inversion

Nếu nhiều lock được acquire theo thứ tự khác nhau, deadlock có thể xảy ra. Trong Android, synchronous Binder call trong khi giữ app lock còn có thể tạo dependency khó thấy giữa process/thread.

Senior guideline: giữ critical section nhỏ, tránh blocking IO/Binder call khi đang giữ lock nếu không thật sự cần, và ưu tiên architecture giảm shared mutable state.

# Debugging runtime

## 31. Khi nào dùng tool nào

Logcat tốt cho sequence/event. Android Studio Profiler tốt cho CPU/memory/network overview. Perfetto/System Trace tốt cho thread scheduling, frame, Binder, lock và end-to-end timing. Heap dump tốt cho retained object. Macrobenchmark đo startup/frame interaction ở gần production. StrictMode bắt một số policy violation dev-time.

Không chọn tool theo thói quen; chọn theo hypothesis.

## 32. Ví dụ suy luận một ANR

Giả sử stack main thread cho thấy:

```text
Main thread
→ onResume
→ repository.refreshBlocking()
→ OkHttp execute()
```

Không cần tối ưu Compose trước. Root cause là synchronous network trên lifecycle callback/main thread.

Nếu trace lại cho thấy main thread đang chờ `CountDownLatch`, trong khi worker cần callback trên main để count down, đây có thể là deadlock/liveness bug chứ không phải network chậm.

## 33. Ví dụ suy luận memory leak

Nếu heap dump cho thấy destroyed Activity retained bởi `SomeManager.listener`, sửa manager/listener lifetime. Không “gọi System.gc()” để chữa leak. GC không thể thu object vẫn reachable.

# Senior Notes

## 34. Runtime knowledge dùng để phá vỡ ảo tưởng abstraction

Ở code bình thường, hãy làm việc ở abstraction cao: coroutine, Flow, Compose, Room, Navigation. Chỉ hạ xuống Handler/Binder/ART khi evidence chỉ tới đó. Senior không phải người luôn viết low-level code; Senior là người biết abstraction nào đang giữ và khi nào nó đã rò rỉ.

## 35. Process death là design input, không phải edge case kỳ lạ

Nếu app mobile chạy đủ lâu ngoài production, process death sẽ xảy ra. Vì vậy persistence/state restoration nên là một phần architecture, không phải patch sau bug report.

## 36. Thread là resource, không phải unit business logic

Business code nên nói “load profile”, “sync pending mutation”, “render state”, không nói “spawn thread 4”. Thread/dispatcher là execution mechanism. Tách hai thứ giúp code testable và portable hơn.

## 37. IPC boundary là serialization + trust boundary

Qua Binder/Intent/URI, hãy nghĩ cùng lúc ba vấn đề: payload có nhỏ không, version/serialization có đúng không, input có đáng tin không.

## 38. Memory optimization phải dựa trên retained graph và allocation pattern

Đừng thấy memory cao rồi xóa cache ngẫu nhiên. Hãy phân biệt cache hợp lệ, retained leak, bitmap/native allocation và working set cần thiết.

# Checklist kết thúc chapter

Sau chapter này, bạn nên tự giải thích được vì sao `suspend` không đồng nghĩa background; vì sao main thread thực chất là event loop; vì sao `Handler` vẫn xuất hiện trong code Android; vì sao Intent/Bundle không nên mang object graph lớn; Binder là gì và vì sao IPC không miễn phí; process death khác configuration change thế nào; singleton/Application không phải persistence; managed heap khác total process memory thế nào; và khi gặp ANR/leak nên dùng trace/heap evidence thay vì đoán.
