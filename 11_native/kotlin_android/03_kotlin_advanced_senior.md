# Kotlin + Android Master Note — Advanced / Senior

> Mục tiêu: hiểu sâu semantics của Kotlin, concurrency, Compose runtime, performance, architecture, testing, modularization, interoperability và các quyết định production mà một Senior Android Engineer phải kiểm soát.

## Mục lục

1. Kotlin type system nâng cao
2. Inline, noinline, crossinline và reified
3. Operator overloading và DSL
4. Contracts và compiler reasoning
5. Reflection, annotations và code generation
6. Coroutines internals và cancellation
7. Exception propagation trong coroutine
8. Flow internals, backpressure và sharing
9. State machine và unidirectional data flow
10. Compose runtime và recomposition
11. Stability, snapshot state và performance
12. Side effects đúng cách
13. Android lifecycle/process death
14. SavedStateHandle
15. Multi-module architecture
16. Build system và Gradle performance
17. Dependency Injection ở quy mô lớn
18. Offline-first, cache và sync
19. Pagination và Paging 3
20. Background execution policy
21. Security production
22. Performance, memory và battery
23. Networking nâng cao
24. Database nâng cao
25. Testing strategy
26. Java interoperability
27. API design bằng Kotlin
28. Common design patterns và Kotlin idioms
29. Legacy migration
30. Senior review checklist

---

# 1. Kotlin type system nâng cao

Kotlin type system có nullable types, bottom type `Nothing`, top types `Any`/`Any?`, generic variance, intersection-like smart cast và platform types từ Java. Senior developer cần hiểu platform type vì đây là nơi null-safety có thể bị xuyên thủng.

Khi Java method trả `String` không có nullability annotation, Kotlin có thể coi nó như platform type `String!`. Compiler cho phép dùng linh hoạt hơn nhưng trách nhiệm runtime thuộc về bạn. Do đó Java boundary nên được normalize sớm:

```kotlin
val safeName: String = javaApi.name ?: "Unknown"
```

Không nên để platform type chảy sâu vào domain model.

`Nothing?` về lý thuyết có thể chứa `null`; `Nothing` không có instance bình thường. Hiểu bottom type giúp đọc type inference trong `throw`, `return`, `error()` và generic expression.

# 2. `inline`, `noinline`, `crossinline`, `reified`

Higher-order function tạo lambda object/call overhead trong một số trường hợp. `inline` cho phép compiler inline body tại call site, đồng thời mở khả năng non-local return từ lambda inline.

```kotlin
inline fun <T> measure(block: () -> T): T {
    val start = System.nanoTime()
    return block()
}
```

`noinline` giữ một lambda parameter không inline khi cần lưu/pass như object. `crossinline` cấm non-local return khi lambda sẽ được gọi trong context khác.

`reified` chỉ dùng cho type parameter của inline function và cho phép truy cập type ở runtime-like call site mà không phải truyền `Class<T>` thủ công.

```kotlin
inline fun <reified T> Json.decode(text: String): T = ...
```

Không dùng `inline` khắp nơi vì code size có thể tăng. Nó phù hợp API nhỏ, higher-order hot path hoặc cần `reified`/non-local return.

# 3. Operator overloading và DSL

Kotlin map syntax operator sang function có tên quy ước như `plus`, `get`, `set`, `contains`, `invoke`, `compareTo`.

```kotlin
operator fun Money.plus(other: Money): Money = ...
```

Operator overloading chỉ nên dùng khi semantics thực sự trực quan. `a + b` mà thực chất gọi network hoặc mutate database là API gây bất ngờ.

Type-safe DSL dựa nhiều vào lambda with receiver, extension và builder pattern.

```kotlin
html {
    body {
        text("Hello")
    }
}
```

Compose bản chất cũng tận dụng khả năng DSL-like của Kotlin, nhưng runtime/compiler semantics phức tạp hơn builder DSL thông thường.

# 4. Contracts

Kotlin contracts giúp compiler hiểu quan hệ giữa call và program state trong một số API. Đây là tính năng nâng cao; không nên tạo custom contract nếu chưa hiểu effect system và giới hạn compiler.

Một số standard functions như `requireNotNull` có semantics giúp smart cast/flow analysis.

# 5. Reflection, annotations và code generation

Reflection Kotlin/JVM cho phép inspect class/property/function runtime, nhưng có overhead và dependency `kotlin-reflect` nếu dùng full reflection. Android production thường ưu tiên code generation/KSP khi có thể vì startup, size và obfuscation predictability.

KSP là API xử lý symbol dành cho Kotlin tooling, được nhiều library dùng để generate code. KAPT dựa trên Java annotation processing và từng là lựa chọn phổ biến; codebase mới thường ưu tiên KSP nếu library hỗ trợ.

# 6. Coroutine internals và cancellation

`suspend` không tự tạo thread. Compiler biến suspend function thành state machine với continuation. Tại suspension point, state được lưu; coroutine có thể resume sau mà không giữ thread blocked.

Cancellation trong coroutine là cooperative. Code CPU loop dài không gọi suspend function cần tự kiểm tra:

```kotlin
while (...) {
    ensureActive()
    computeChunk()
}
```

Không được swallow `CancellationException`:

```kotlin
try {
    work()
} catch (e: CancellationException) {
    throw e
} catch (e: IOException) {
    ...
}
```

Android guidance nhấn mạnh việc làm coroutine cancellable và tránh generic catch phá cancellation.

# 7. Exception propagation

Với `launch`, uncaught exception có thể được xử lý như uncaught exception của coroutine hierarchy và có thể crash tùy scope/handler. Với `async`, exception được giữ trong `Deferred` và rethrow khi `await`, nhưng parent hierarchy vẫn có propagation semantics.

`SupervisorJob`/`supervisorScope` cho phép sibling độc lập về failure, nhưng không phải “tắt exception”. Bạn vẫn cần quyết định ai log, ai retry, ai chuyển thành state.

`CoroutineExceptionHandler` chỉ là last-resort handler cho uncaught exception ở phù hợp coroutine context; không thay thế `try/catch` cho business error.

# 8. Flow internals, buffering và sharing

Flow mặc định sequential: emitter và downstream operator phối hợp theo suspension. Khi collector chậm, upstream cũng bị chậm trừ khi buffer/concurrency operator thay đổi pipeline.

`buffer()` tách producer/consumer bằng buffer. `conflate()` bỏ qua intermediate value và giữ value mới khi consumer chậm. `collectLatest` cancel block xử lý value trước khi value mới đến. `flatMapLatest` cancel upstream sub-flow cũ khi key mới đến; phù hợp search query.

```kotlin
queryFlow
    .debounce(300)
    .distinctUntilChanged()
    .flatMapLatest(repository::search)
```

`stateIn` và `shareIn` chuyển cold flow thành hot shared flow trong một scope. `SharingStarted.WhileSubscribed(...)` thường hợp UI nhưng timeout/replay phải được hiểu, không copy template máy móc.

# 9. State machine, UDF và architecture invariant

UDF không phải tên khác của MVI framework. Nó là một constraint giúp reasoning:

```text
authoritative state
    ↓
UI render
    ↓
user/system event
    ↓
owner xử lý side effect / transition
    ↓
source of truth thay đổi
    ↓
state mới
```

Điểm Senior cần giữ không phải “mọi app phải có reducer”, mà là **mỗi fact quan trọng có owner và source of truth rõ**. Nếu cùng một bookmark tồn tại thành mutable state riêng ở database, repository cache, ViewModel và `remember`, hệ thống có bốn nơi có thể bất đồng.

## 9.1 Bắt đầu architecture bằng invariant

Trước khi chọn MVVM/MVI/Clean Architecture, hãy viết invariant:

```text
User A không bao giờ nhìn thấy cache của User B.
Sau khi payment được server confirm, retry không tạo transaction thứ hai.
UI chỉ render article snapshot từ local source of truth.
Process recreation có thể reconstruct screen từ stable ID.
```

Architecture có giá trị khi boundary làm invariant dễ giữ và dễ test.

## 9.2 State machine tránh impossible state

Nhiều flags độc lập dễ tạo tổ hợp vô nghĩa:

```text
loading=true
fatalError=true
contentEmpty=false
paymentSucceeded=true
```

Có hai kiểu model phổ biến:

```text
mutually exclusive phase
→ sealed state / explicit state machine

content có thể coexist với refresh/error metadata
→ immutable data class với invariant được document
```

Không ép mọi screen thành sealed state nếu UX cần cached content + refresh + warning cùng lúc. Model phải theo business invariant, không theo template.

## 9.3 Command, state và event phải phân biệt

```text
Command
= yêu cầu làm việc: Refresh, Submit, Retry

State
= fact hiện tại có thể đọc lại: PaymentCompleted, UserLoggedOut

Transient UI effect
= Snackbar "Copied", haptic, focus request
```

Nếu một fact quan trọng bị model thành event một lần và collector vắng mặt thì mất, design có thể sai. Durable fact nên có durable/source-of-truth representation.

## 9.4 Stale snapshot là architecture bug, không chỉ concurrency bug

Ví dụ ViewModel giữ object `Article` được truyền từ list screen sang detail. Trong lúc detail mở, DB sync article mới. Detail vẫn hiển thị object cũ vì navigation argument trở thành source of truth thứ hai.

Tốt hơn:

```text
navigation truyền articleId
→ destination observe repository/DB theo ID
→ UI luôn thấy authoritative snapshot
```

Architecture phải giải thích data freshness và reconstruction, không chỉ dependency direction.

# 10. Compose runtime và recomposition

Compose không phải “framework gọi lại toàn bộ screen mỗi khi state đổi”. Compiler Compose biến `@Composable` function thành code có thêm metadata/runtime protocol; runtime duy trì **Composition** để nhớ cấu trúc UI, identity của các call site và những state read nào xảy ra ở đâu. Khi observable state đổi, Compose invalidates đúng restart scope liên quan và cố làm lượng công việc tối thiểu cần thiết.

Mental model một frame:

```text
State/data
   ↓
Composition — UI nào tồn tại?
   ↓
Layout — đo và đặt ở đâu?
   ↓
Draw — vẽ như thế nào?
```

Recomposition chỉ nói về việc chạy lại phần **composition** cần thiết. Sau đó layout hoặc draw có thể chạy hoặc được bỏ qua tùy kết quả. Vì vậy “recomposition count cao” tự nó chưa chứng minh UI chậm.

## 10.1 Identity đến từ vị trí call site và key

Compose cần biết instance logic nào ở lần composition hiện tại tương ứng với instance nào trước đó để giữ `remember`, effect và state đúng chỗ.

```kotlin
LazyColumn {
    items(
        items = users,
        key = { it.id },
        contentType = { "user" }
    ) { user ->
        UserRow(user)
    }
}
```

Key phải biểu diễn identity bền vững, không phải index nếu index thay đổi khi insert/delete/reorder.

## 10.2 `remember` thuộc Composition, không thuộc business object

```kotlin
val state = remember(key) { expensiveInitialization(key) }
```

Giá trị được giữ khi call site còn identity và key không đổi. `remember` không sống qua process death; không tự sống qua việc composable rời Composition; và không phải nơi giữ dữ liệu business lâu dài chỉ vì “muốn khỏi load lại”.

Phân lớp owner:

```text
UI ephemeral state trong call site
→ remember

UI state nhỏ cần save qua recreation
→ rememberSaveable

screen state/business interaction
→ ViewModel / state holder

durable data
→ repository + database/DataStore/server
```

## 10.3 State read quyết định phase nào bị invalidated

Compose theo dõi nơi đọc state, không chỉ nơi state được tạo. Read trong composition có thể trigger recomposition; read trong placement có thể chỉ restart layout; read trong draw có thể chỉ restart draw.

Senior optimization không phải chuyển mọi read xuống phase thấp nhất bằng mẹo khó đọc; nó là hiểu hot path để tránh work không cần thiết khi profiler chứng minh vấn đề.

## 10.4 Composable body phải gần pure

Composable có thể chạy lại, bị skip hoặc một composition attempt có thể không được apply. Vì vậy body không phải nơi gọi side effect tùy ý:

```kotlin
@Composable
fun Bad(userId: String) {
    repository.load(userId) // sai: side effect trong composition
}
```

UI body nên chủ yếu mô tả output từ input/state. Business side effect thuộc event handler/ViewModel/data layer; effect gắn lifecycle UI dùng Effect API phù hợp.

# 11. Snapshot State, stability và performance

Compose Snapshot system cung cấp observable state model cho runtime. Ordinary Kotlin mutation không tự trở thành observable. Immutable snapshot hoặc Snapshot-aware collection làm mutation contract rõ hơn.

**Immutable** và **Stable** không phải cùng khái niệm. Không annotate `@Stable`/`@Immutable` chỉ để giảm metric; annotation sai có thể khiến runtime bỏ work cần thiết và tạo correctness bug.

`derivedStateOf` hữu ích khi input đổi thường xuyên nhưng output semantic đổi ít hơn. `remember` cache theo identity/key chứ không phải global cache. Lazy list cần stable key; key sai không chỉ ảnh hưởng performance mà còn có thể gắn state/effect nhầm entity.

Performance phải đo theo frame: composition, measure/layout, draw, allocation/GC, main-thread block và lazy reuse. Correctness đứng trước skip optimization.

# 12. Side effects đúng cách

Compose effect API tồn tại vì composable body nên side-effect free. Chọn effect theo lifetime và cleanup contract.

`LaunchedEffect(key)` launch coroutine khi vào Composition, cancel khi rời Composition, và cancel/restart khi key đổi. Constant key như `Unit` chỉ có nghĩa “không restart vì key trong lifetime call site này”, không phải “một lần toàn app”.

`rememberUpdatedState` cho phép effect giữ lifetime hiện tại nhưng đọc callback/value mới nhất. `DisposableEffect` dùng khi có acquire/release listener/resource. `SideEffect` publish Compose state sang non-Compose object sau successful composition. `snapshotFlow` chuyển Snapshot reads thành Flow; `rememberCoroutineScope` hữu ích cho coroutine được kích hoạt từ UI event như snackbar.

Senior review phải hỏi:

```text
identity của effect là gì?
key nào restart?
value nào chỉ cần latest?
cleanup ở đâu?
leaving Composition có nên cancel operation không?
đây là UI effect hay business command?
```

# 13. Lifecycle, configuration change và process death

Configuration change thường recreate Activity nhưng ViewModel có thể sống qua recreation. Process death khác hoàn toàn: OS kill process, toàn bộ in-memory state mất. Nếu state phải restore, cần persistence/SavedStateHandle/rememberSaveable tùy loại dữ liệu.

Đừng lưu object lớn hoặc dữ liệu có thể reload vào Bundle. Bundle có giới hạn Binder transaction; stable IDs và persistence tốt hơn.

# 14. SavedStateHandle

`SavedStateHandle` cho ViewModel state cần phục hồi sau process recreation theo capability của saved state. Nó không phải database. Chỉ lưu dữ liệu nhỏ, serializable/savable hoặc identifier cần để reconstruct screen.

# 15. Multi-module architecture: boundary phải mua được giá trị

Module hóa không phải mục tiêu tự thân. Một module nên tồn tại vì ít nhất một force cụ thể: ownership/team boundary, dependency isolation, build parallelism/cache, reusable public contract, optional delivery hoặc giới hạn accidental coupling.

Một graph có thể như:

```text
:app
  ↓
:feature:home:impl ─────→ :feature:home:api
  ↓                           ↑
:core:data ─────→ :core:model │
  ↓                           │
:core:database / :core:network
```

Dependency phải có hướng. Nếu `feature:A` import internal implementation của `feature:B`, boundary trên sơ đồ không tồn tại thực tế.

## 15.1 Public surface nhỏ hơn implementation surface

Module public API nên chứa contract cần thiết, không export mọi DTO/entity/helper. `internal` là công cụ compile-time/module visibility hữu ích nhưng không phải security boundary.

Một thay đổi implementation phía sau API nhỏ có blast radius build/source nhỏ hơn một `core:common` expose hàng trăm symbol.

## 15.2 God core module là monolith đội lốt modularization

`core:common` chứa networking, analytics, navigation, model, auth và utility của mọi feature tạo dependency fan-in cực lớn. Mỗi sửa nhỏ có thể invalidated nhiều module và mọi team đều sở hữu “một chút”, cuối cùng không ai thực sự sở hữu.

Tách theo capability ổn định, không theo mong muốn tạo thật nhiều folder.

## 15.3 Module boundary phải đi cùng runtime ownership

Tách `feature:checkout` thành module không tự giải quyết việc checkout session sống bao lâu, repository source of truth ở đâu hay coroutine scope thuộc ai. Build boundary và runtime boundary là hai dimension khác nhau.

# 16. Gradle, build graph và release debugging

Gradle build cần được hiểu theo phase thay vì xem như “Android Studio bấm Run”.

```text
Settings / project discovery
→ configuration
→ variant/task graph
→ task execution
→ compiler/code generation
→ resource + manifest processing
→ D8/R8
→ packaging/signing
→ APK/AAB
```

Một lỗi phải được định vị ở phase nào trước khi sửa.

## 16.1 Configuration cost vs execution cost

Configuration cache giải quyết việc tái sử dụng configuration state khi build logic tương thích; build cache tái sử dụng task output dựa trên input. Hai cache khác nhau.

Không chạy network/file scanning tùy ý trong configuration. Custom task phải khai báo input/output đúng để incremental/cache có thể tin cậy.

## 16.2 Build reproducibility

Production artifact phải truy được:

```text
source commit
Gradle wrapper
AGP/Kotlin/JDK
resolved dependency graph
build variant/flavor
R8 rules
signing identity/process
feature/config inputs
```

Dynamic version như `1.+` phá reproducibility vì cùng commit có thể resolve dependency khác ở ngày khác.

## 16.3 Debug build pass không chứng minh release pass

Release có thể khác debug ở:

```text
R8 shrinking/optimization/obfuscation
resource shrinking
BuildConfig/manifest value
signing
proguard consumer rules
feature flag/environment
native symbols
```

Vì vậy CI cần compile/test release-like variant. Lỗi reflection/JNI/serialization chỉ xuất hiện sau minify là failure mode bình thường cần được thiết kế test.

## 16.4 Debugging theo exact variant

Khi bug chỉ xảy ra ở `prodRelease`, đừng reproduce bằng `devDebug` rồi kết luận. Ghi exact tuple:

```text
commit + variant + device/API + dependency lock + server/config version
```

Forensics bắt đầu từ artifact thật, không từ source “trông giống”.

# 17. DI ở quy mô lớn: graph và lifetime contract

DI không phải architecture; DI quản lý object graph và creation/lifetime. Scope phải phản ánh owner thật:

```text
application singleton
session scoped
activity/navigation graph scoped
ViewModel scoped
transient
```

Một object stateful vô tình `@Singleton` có thể leak data qua account switch. Một Activity Context bị giữ trong singleton tạo memory leak. Constructor injection làm dependency explicit nhưng không tự bảo đảm scope đúng.

Hilt/Dagger compile-time graph giúp verify dependency. Assisted injection hữu ích khi một số input là runtime identity như `itemId`. Multibinding phù hợp registry/plugin model. Không tạo interface cho mọi class chỉ để DI “đẹp”; seam phải phản ánh volatility/test requirement thật.

# 18. Offline-first, source of truth và sync correctness

Offline-first không chỉ là “cache API response”. Phải định nghĩa consistency contract giữa local và remote.

Một pattern production:

```text
UI observe local DB
network refresh/sync
    ↓
transaction update local DB
    ↓
DB emit authoritative snapshot
    ↓
UI update
```

## 18.1 Read-offline và write-offline khác độ khó

Read cache chỉ cần freshness/revalidation policy. Write-offline cần durable pending mutation, idempotency, ordering, conflict, retry và account isolation.

Nếu product không cần offline mutation, đừng xây distributed sync engine chỉ vì “offline-first nghe hiện đại”.

## 18.2 Ambiguous outcome

Request timeout không có nghĩa server chưa commit:

```text
client gửi POST
server commit
response mất
client thấy timeout
```

Nếu retry mù, duplicate side effect có thể xuất hiện. Idempotency key/server contract mới giải quyết được nhóm failure này.

## 18.3 Durable outbox invariant

Nếu local optimistic update và pending operation phải luôn cùng tồn tại, ghi chúng trong cùng local transaction:

```text
entity state changed
AND
outbox mutation exists
```

Crash giữa hai write riêng biệt sẽ phá invariant.

## 18.4 Conflict và ordering

LWW chỉ đúng nếu business chấp nhận last-write-wins và clock/version đáng tin. Nhiều domain cần server revision/optimistic concurrency/field merge hoặc explicit conflict UI.

Mutation queue cũng cần biết operation có commute không. `setFavorite(true)` có semantics retry khác `toggleFavorite()` vì toggle phụ thuộc state trước đó.

## 18.5 Account/session isolation

Pending work và cache phải namespace theo account/session nếu dữ liệu user-specific. Logout không chỉ xóa token; cần xác định worker đang chạy, DB/cache cũ, in-flight response và notification/deep link state.

# 19. Paging 3

Paging 3 giúp load dữ liệu theo trang từ database/network. `Pager`, `PagingSource`, `RemoteMediator` là các abstraction chính. `RemoteMediator` phù hợp khi network + DB kết hợp và DB là source of truth.

UI cần handle refresh/append/prepend load states độc lập. Sai lầm thường gặp là biến mọi error thành full-screen error dù chỉ append page fail.

# 20. Background execution policy: chọn primitive theo lifetime + guarantee

Không chọn background API theo câu hỏi “cái nào chạy nền?”, mà theo contract:

```text
work chỉ có ý nghĩa khi screen còn sống
→ ViewModel/lifecycle coroutine

work user-visible đang chạy liên tục
→ foreground service nếu platform policy/use case cho phép

work có thể trì hoãn nhưng cần eventually execute
→ WorkManager

đúng thời điểm gần tuyệt đối
→ alarm API chỉ khi use case đủ điều kiện

server-triggered signal
→ push/FCM, sau đó app quyết định work phù hợp
```

Service không phải thread. WorkManager không phải sync correctness engine; nó schedule execution, còn idempotency/source-of-truth/retry semantic thuộc business/data design.

Production failure cần test Doze, battery saver, process kill, reboot, network mất/đổi, permission revoke và duplicate scheduling nếu relevant.

# 21. Security production: threat model trước API

Mobile client là môi trường người dùng kiểm soát. Attacker có thể decompile APK, hook method, inspect memory, chạy rooted/emulated environment hoặc gửi Intent/deep link trực tiếp.

## 21.1 Trust boundary

```text
client-side role check
= UX optimization

backend authorization
= security authority
```

Không nhúng server secret dài hạn rồi trông chờ R8/obfuscation bảo vệ. Keystore bảo vệ key material tốt hơn file plaintext nhưng không biến compromised device thành trusted server.

## 21.2 External input phải coi là untrusted

Các boundary cần validate:

```text
Intent/deep link
exported Activity/Service/Receiver/Provider
PendingIntent
content URI/FileProvider
WebView navigation/JS bridge
notification action
Binder/native input
```

Kiểm tra scheme/host/path/ID, authorization sau navigation, URI grant tối thiểu và `android:exported` có chủ đích.

## 21.3 Token/session security là lifecycle problem

Token có expiry/refresh/revoke. Concurrent `401` cần single-flight refresh; logout cần vô hiệu session state, cancel/namespace pending work và không để response của account cũ update state account mới.

Không log token/PII. Telemetry schema phải có privacy review vì observability cũng là data export surface.

## 21.4 Certificate pinning có operational cost

Pinning chỉ dùng khi threat model biện minh và có rotation/recovery plan. Certificate/key thay đổi không được chuẩn bị có thể biến security control thành outage toàn app.

# 22. Performance, memory và battery: evidence before optimization

Performance engineering theo vòng:

```text
user-visible metric
→ reproduce trên representative device
→ trace/profile
→ hypothesis
→ one controlled change
→ measure lại
→ regression guard
```

Các metric khác nhau cần tool khác nhau:

```text
startup TTID/TTFD
frame time/jank
CPU hot path
allocation/GC/memory peak
DB latency/query plan
network latency/bytes
battery/background wakeup
APK/download size
```

Macrobenchmark phù hợp startup/interaction ở package level; Perfetto/System Trace nhìn thread/system timeline; memory profiler tìm retention/allocation; baseline profile cải thiện compiled hot path nhưng không sửa algorithm chậm.

## 22.1 Tail latency quan trọng hơn average đẹp

Average 8 ms không có nghĩa smooth nếu p95/p99 có frame 80–150 ms. Production telemetry nên segment theo device class/OS/network nếu metric nhạy với environment.

## 22.2 Memory leak = lifetime mismatch

Các pattern thường gặp:

```text
singleton giữ Activity/View
listener không unregister
Fragment binding sống sau onDestroyView
coroutine scope sống dài hơn owner
unbounded cache
callback/lambda capture object graph lớn
```

GC không thể thu object còn reachable. Debug bằng retention path thay vì gọi `System.gc()`.

## 22.3 Battery là scheduling + radio + sensor problem

Polling thường xuyên, location high accuracy liên tục, wakeup quá nhiều và retry storm đều tốn pin. Batch work, chọn constraint hợp lý, debounce/throttle khi đúng semantic và dừng sensor/camera/BLE theo lifecycle/resource ownership.

# 23. Networking nâng cao: failure taxonomy trước retry

Phân biệt:

```text
DNS/connectivity/timeout
TLS failure
HTTP protocol status
serialization/schema failure
auth/session failure
domain validation/conflict
ambiguous outcome sau side effect
```

Không map tất cả thành `NetworkError` rồi retry.

OkHttp interceptor chain có application/network interceptor với semantics khác. Token refresh cần tránh thundering herd khi nhiều request cùng `401`; mutex/single-flight có thể phù hợp nếu lock scope đúng.

Timeout cần phân biệt connect/read/write/call. Retry chỉ an toàn khi operation idempotent hoặc backend có idempotency key. Backoff nên có jitter ở fleet lớn để tránh nhiều client retry cùng lúc.

HTTP cache và application DB cache là hai layer khác nhau. Cache policy phải xác định freshness, validation và source of truth.

# 24. Database nâng cao: transaction là invariant boundary

Room transaction không chỉ để “chạy nhanh hơn”; nó bảo đảm nhóm write quan trọng commit/rollback cùng nhau.

```kotlin
@Transaction
suspend fun replaceData(...) { ... }
```

Nếu business invariant là entity update và outbox mutation phải cùng tồn tại, transaction phải bao quanh cả hai.

Index cần dựa trên query plan. Quá nhiều index tăng write/storage. Migration phải test bằng schema cũ + dữ liệu đại diện; destructive migration chỉ hợp với disposable cache nếu product chấp nhận mất dữ liệu.

Database lock/transaction dài có thể block resource dù API là suspend. Không đặt network call trong DB transaction. Sync cursor + downloaded page có thể cần cùng transaction để crash không tạo “cursor mới nhưng data chưa ghi”.

Rollback release cũng phải đọc được schema/data đã do version mới tạo nếu product muốn binary rollback thực sự khả thi.

# 25. Testing strategy: test invariant và failure order

Test pyramid Android nên tối đa hóa fast deterministic tests ở domain/data boundary, thêm integration test tại serialization/DB/DI/boundary, và UI/end-to-end test cho critical flows.

Fake thường tốt hơn mock cho stateful collaborator vì giữ behavior gần hệ thống thật. Mock phù hợp interaction hẹp.

Senior test không chỉ happy path. Cần chủ động điều khiển order:

```text
request A bắt đầu
request B bắt đầu
B success
A success muộn
→ assert A không overwrite B
```

Các failure test có giá trị cao:

```text
process death giữa flow
DB migration từ schema thực
network timeout sau remote commit
401 đồng thời
permission revoke
disk full / serialization corrupt nếu domain quan trọng
R8/minified release
rollback đọc data version mới
```

Compose UI test nên query semantics phản ánh meaning/accessibility thay vì chỉ testTag nếu có thể.

# 26. Java interoperability

Annotations quan trọng gồm `@JvmStatic`, `@JvmField`, `@JvmOverloads`, `@JvmName`, `@Throws`. Không dùng tự động; chỉ thêm khi Java caller cần API shape tương ứng.

SAM conversion hoạt động tốt với Java functional interface và Kotlin `fun interface`.

```kotlin
fun interface Listener {
    fun onEvent(value: String)
}
```

# 27. API design bằng Kotlin

Public API nên ưu tiên type safety, immutability, explicit ownership và predictable failure semantics. Tránh boolean parameter khó đọc:

```kotlin
send(true, false)
```

Tốt hơn dùng enum/options object hoặc named arguments nếu internal Kotlin-only API.

Builder chỉ cần khi constructor/named defaults không đủ. Kotlin data class + default parameter thường loại bỏ boilerplate builder Java.

Public API cần document cả **behavioral contract**: threading, cancellation, ordering, replay, nullability, ownership và failure; type signature một mình chưa đủ.

# 28. Design patterns và Kotlin idioms

Nhiều GoF pattern được Kotlin làm nhẹ hơn. Strategy có thể là function type thay vì hierarchy class. Singleton có `object`. Builder có DSL/named/default args. Decorator có delegation. Observer thường biểu diễn bằng Flow. State pattern có sealed hierarchy/reducer.

Không áp pattern vì tên nghe “senior”. Pattern là giải pháp cho force cụ thể. Nếu language feature làm vấn đề biến mất, đừng dựng class graph chỉ để giống sách.

# 29. Legacy migration: strangler thay big-bang

Migration Java → Kotlin hoặc XML → Compose nên tạo seam và di chuyển incrementally.

Ví dụ:

```text
Rx repository cũ
→ adapter boundary expose Flow cho feature mới
→ migrate caller dần
→ đo/test
→ xóa Rx path khi không còn consumer
```

Hoặc:

```text
Fragment host cũ
→ ComposeView cho leaf screen mới
→ navigation/lifecycle vẫn giữ contract cũ
→ migrate screen theo risk/ownership
```

Mỗi migration phải có:

```text
behavior baseline
entry/exit criteria
coexistence contract
telemetry/test
rollback/fallback
owner
ngày/điều kiện xóa legacy
```

Convert source tự động không đồng nghĩa migration semantic hoàn tất.

# 30. Senior review checklist

Review theo chain thay vì theo framework:

```text
Requirement
→ invariant
→ owner/lifetime
→ source of truth
→ state transition
→ execution context
→ concurrency/ordering
→ external boundary
→ failure/retry/idempotency
→ persistence/reconstruction
→ security/privacy
→ performance budget
→ test evidence
→ build/artifact
→ rollout/rollback
```

Một feature chưa production-ready nếu chỉ trả lời “dùng MVVM + Hilt + Room + Compose” nhưng không giải thích được race, process death, stale data, retry, security boundary hoặc rollback.

---

## Senior Notes tổng kết

Code Android production bền không đến từ việc dùng nhiều library nhất mà từ việc đặt đúng ownership và giữ invariant. State thuộc ai, coroutine thuộc scope nào, database là source of truth hay cache, retry thuộc layer nào, error được map ở boundary nào, event có thực sự là event hay chỉ là state chưa model đúng, dependency sống bao lâu, và behavior nào phải survive process death. Seniority thể hiện ở khả năng trả lời rõ những câu hỏi đó trước khi bug xảy ra.

---

# 31. Channel, Mutex, atomic và shared mutable state

Coroutine giúp viết concurrency dễ đọc hơn nhưng không tự loại bỏ data race. Nếu nhiều coroutine truy cập shared mutable state trên nhiều thread, bạn vẫn cần synchronization. `Mutex` là primitive coroutine-friendly cho critical section có thể suspend; `Channel` mô hình hóa việc truyền message giữa producer/consumer; atomic primitive phù hợp cho operation nhỏ không cần suspension.

```kotlin
private val mutex = Mutex()
private var cached: Token? = null

suspend fun token(): Token = mutex.withLock {
    cached ?: refreshToken().also { cached = it }
}
```

Ví dụ trên còn gợi ý pattern single-flight. Tuy nhiên nếu `refreshToken()` lâu hoặc re-enter dependency khác, phải xem lock scope để tránh contention/deadlock logic. Trước tiên giảm shared mutable state và xác định owner rồi mới chọn primitive.

`Channel` không thay thế Flow. Flow phù hợp stream/declarative transformation; Channel phù hợp queue/message hand-off. Tránh Channel như event bus toàn app vì ownership/backpressure khó kiểm soát.

# 32. Coroutine scheduler, dispatcher injection và starvation

`Dispatchers.IO` và `Dispatchers.Default` có mục đích khác nhau. Blocking I/O nên tách khỏi CPU-bound work. Đưa vòng lặp CPU nặng vào IO không biến nó thành I/O.

Dispatcher injection làm code testable và giúp data layer kiểm soát main-safety. Thread starvation có thể xảy ra khi blocking call trong pool nhỏ, lock quá lâu hoặc quá nhiều CPU work đồng thời. Khi profile, phân biệt coroutine suspend với thread blocked.

# 33. Compose performance: từ invalidation tới frame evidence

Recomposition count tự nó không phải bug. Compose có ba phase chính cho frame: composition → layout → draw, và Snapshot state read ở phase nào quyết định work có thể restart khi state đổi.

Expensive calculation trong composition cần được xem xét:

```kotlin
val sortedItems = remember(items) {
    items.sortedBy { it.title }
}
```

`remember` chỉ đúng nếu key phản ánh mutation semantics. `derivedStateOf` hữu ích khi input đổi thường xuyên nhưng output semantic đổi ít hơn.

Khi profile Compose, phân biệt composition cost, measure/layout, draw, allocation/GC, main-thread block, image/text cost và lazy list identity/reuse. Production correctness luôn đứng trước skip optimization.

# 34. Main thread, ANR, StrictMode và leak

Android UI thread xử lý input, lifecycle callback, drawing orchestration và nhiều callback framework. Blocking disk/network hoặc CPU work dài trên main có thể gây jank và ANR. JSON parse lớn, bitmap decode, DB transaction hoặc lock contention cũng có thể chặn main.

`StrictMode` trong debug build giúp phát hiện một số disk/network operation hoặc leaked closable object. Khi nghi leak, nhìn retention path bằng memory profiler/tooling; GC không thể thu object còn reachable.

ANR investigation nên kết hợp main-thread stack/thread dump, trace/Perfetto và context về binder/lock/I/O. Không “sửa ANR” bằng cách chuyển toàn bộ code sang IO nếu bottleneck thật là lock contention hoặc algorithm CPU.

# 35. R8, shrinking và keep rules

Release build có thể bật R8 để shrink, optimize và obfuscate. Reflection, JNI, serializer hoặc framework tìm class theo tên có thể bị ảnh hưởng nếu entry point không được model.

Keep rule phải càng hẹp càng tốt. Library Android nên cung cấp consumer rules nếu chính library cần. Sau obfuscation, release pipeline phải lưu/upload mapping đúng artifact để deobfuscate crash.

Failure forensic:

```text
debug pass + release fail
→ compare minify/resource shrink/BuildConfig/manifest/signing
→ inspect R8 diagnostics/mapping/usage
→ reproduce exact release variant
```

# 36. Signing, APK/AAB và release reproducibility

Android artifact release phải được ký. Release signing key/upload key là credential operational quan trọng.

Build reproducibility nghĩa release truy ra được source commit, dependency graph, wrapper/JDK/toolchain, variant, config, R8 mapping, native symbols và signing process.

AAB là publishing artifact; thiết bị thường nhận split APK phù hợp configuration. Vì vậy verify install/delivery path khi bug liên quan ABI/resource/language split, không chỉ inspect `.aab` upload.

# 37. API level compatibility, behavior change và feature gating

`minSdk`, `compileSdk`, `targetSdk` là ba contract khác nhau. Code gọi API mới trên OS cũ cần guard hoặc compat abstraction.

Nâng `targetSdk` là behavior migration: test notification, permission, background execution, storage, window/insets, exported component và policy thay đổi. Nên tách target migration khỏi Kotlin/AGP migration khi có thể để forensic rõ.

Tại baseline này Android 17 là API 37, trong khi Play target requirement có thể thấp hơn latest platform. Latest SDK và distribution requirement không phải cùng một khái niệm.

# 38. WebView như một security boundary

WebView kết hợp web security model với native app privilege. Validate external URL scheme/host, quyết định domain nào được ở trong WebView, hạn chế file access/JS/debugging theo threat model và cực kỳ thận trọng với `addJavascriptInterface`.

Authentication token không nên nhét tùy tiện vào URL. Certificate pinning chỉ dùng khi có operational plan cho rotation/recovery.

# 39. Database migration và schema evolution trong production

Room migration phải coi dữ liệu người dùng là tài sản. Test từ schema cũ thực tế, insert dữ liệu đại diện, chạy migration rồi verify schema + data.

Với staged rollout, app version cũ và mới có thể cùng tồn tại. Local data, remote payload và server behavior phải có compatibility window. Nếu migration irreversible, binary rollback có thể không cứu được user đã mở app version mới.

# 40. Production failure model và Senior decision framework

Mobile production không chạy theo happy path. Một feature nên được review với failure matrix:

```text
Process
- configuration recreate
- process kill
- app update
- device reboot

Concurrency
- duplicate tap
- request A/B out of order
- 401 storm
- worker + foreground UI cùng mutate

Network
- offline
- timeout trước commit
- timeout sau remote commit
- partial payload/schema drift

Persistence
- migration
- disk full/corrupt data
- transaction partiality
- rollback binary đọc schema mới

Platform
- permission revoke
- targetSdk behavior change
- OEM/WebView difference
- background restriction

Release
- R8-only failure
- ABI/split issue
- bad remote config
- staged rollout regression
```

Sau đó hỏi theo chuỗi:

```text
state thuộc owner nào?
lifetime bao lâu?
source of truth ở đâu?
operation blocking hay suspend?
ordering được định nghĩa chưa?
retry có an toàn/idempotent không?
process death reconstruct thế nào?
input nào untrusted?
performance budget nào cần đo?
test nào chứng minh invariant?
telemetry nào phát hiện regression?
rollback/fallback có thật sự khả thi không?
```

Nếu những câu hỏi này có đáp án rõ, lựa chọn MVVM/MVI, Hilt/Koin, Room/SQLDelight hoặc Retrofit/Ktor thường trở thành quyết định kỹ thuật dễ lý giải hơn.