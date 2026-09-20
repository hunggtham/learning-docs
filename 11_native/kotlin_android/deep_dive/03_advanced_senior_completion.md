# Kotlin + Android Advanced / Senior — Completion Deep Dive

> File này bổ sung cho [`../03_kotlin_advanced_senior.md`](../03_kotlin_advanced_senior.md). Trọng tâm là những failure mode và trade-off mà developer senior phải reasoning được: type system sâu, cancellation safety, Flow backpressure, Compose Snapshot/identity, background execution, networking/TLS, storage/backup, nhiều tầng testing và quality gate.

# 1. Kotlin type system sâu hơn

Ở senior level, generic không còn chỉ là `List<T>`. Cần hiểu variance theo vị trí producer/consumer, use-site projection, star projection và type erasure. `List<out T>` có thể đọc T an toàn nhưng không thể tùy ý ghi; consumer direction được diễn đạt bằng `in` khi phù hợp.

Trên JVM, generic phần lớn bị **type erasure**, vì vậy runtime thường không biết `List<String>` khác `List<Int>`. `reified` type parameter trong inline function có thể giữ đủ type token cho một số operation như `is T` hoặc lấy `T::class`, nhưng nó không xóa mọi giới hạn erasure của nested generic.

Kotlin cũng có syntax definitely non-null type `T & Any` trong một số generic/interoperability API để nói rằng T tại boundary này chắc chắn non-null. Đây thường gặp hơn khi thiết kế API generic/Java interop hơn là app code hàng ngày.

# 2. Cancellation safety và cleanup

Cancellation là exception-based và cooperative. Code senior phải đảm bảo resource cleanup vẫn chạy. `finally` được thực thi khi coroutine cancel; nếu cleanup cần gọi suspend function, đôi khi cần `withContext(NonCancellable)` rất hẹp.

```kotlin
try {
    repository.sync()
} finally {
    withContext(NonCancellable) {
        auditStore.flushPendingMetadata()
    }
}
```

Không dùng `NonCancellable` để “chống cancel” cả workflow vì sẽ phá structured concurrency và UX. Nếu operation có side effect không thể bỏ dở, thiết kế idempotency/transaction hoặc chuyển nó sang owner phù hợp như WorkManager thường đúng hơn cố giữ UI coroutine sống mãi.

Một lỗi tinh vi khác là catch `Exception` để map lỗi rồi vô tình nuốt `CancellationException`. Khi viết wrapper chung, hãy rethrow cancellation hoặc dùng API/operator giữ semantics cancellation đúng.

# 3. Flow backpressure, buffering và conflation

Flow mặc định tạo backpressure: producer suspend nếu collector xử lý chậm. `buffer()` cho producer/consumer chạy tách nhịp; `conflate()` bỏ intermediate value khi collector chỉ cần trạng thái mới nhất; `collectLatest` cancel phần xử lý emission trước khi value mới tới.

Lựa chọn này phải theo semantics. Search result UI có thể dùng latest-wins; event thanh toán không được `conflate` mất giao dịch. Một operator performance tưởng đơn giản có thể đổi tính đúng đắn của hệ thống.

`SharedFlow` cần thiết kế `replay`, buffer và overflow strategy cẩn thận. Dùng `SharedFlow` cho one-off UI event phải cân nhắc collector lifecycle; nhiều trường hợp state model tốt hơn event channel vì state có thể phục hồi sau recreation.

# 4. Compose Snapshot system

Compose Snapshot State là một hệ thống quản lý state/version chứ không chỉ callback “set value rồi redraw”. Khi composable đọc `State`, runtime ghi nhận dependency; khi state đổi, scope liên quan có thể invalidate và recomposition. Điều này giải thích vì sao đọc state ở scope quá cao làm vùng recomposition lớn hơn cần thiết.

Snapshot cũng tạo một mental model tương tự transaction/versioned state. State mutation phải tuân convention/runtime expectation; shared mutable object không observable có thể thay đổi mà Compose không biết.

# 5. `CompositionLocal`: ambient dependency có kiểm soát

`CompositionLocal` truyền dependency/value theo composition tree mà không phải đưa parameter qua mọi layer. Nó phù hợp cho concern mang tính tree-local như theme, density, localization hoặc một capability UI-scoped.

```kotlin
val LocalAnalytics = staticCompositionLocalOf<Analytics> {
    error("Analytics not provided")
}
```

Dùng nó như service locator toàn cục cho repository/business dependency sẽ làm data flow khó theo dõi. Nếu dependency là logic/domain dependency bình thường, constructor/ViewModel injection thường rõ hơn.

# 6. Recomposition, layout và draw là các phase khác nhau

Không nên đồng nhất “recomposition” với “vẽ lại toàn màn hình”. Compose pipeline có composition, layout/measurement và draw. Một thay đổi chỉ ảnh hưởng draw có thể không cần recomposition; một thay đổi layout có thể không cần rebuild toàn subtree.

Optimization senior bắt đầu bằng trace/metrics chứ không thêm `remember` vô điều kiện. Function rẻ recomposition nhiều lần có thể hoàn toàn ổn; một allocation/layout đắt ở hot path mới đáng tối ưu.

Stable/immutable model giúp runtime skip tốt hơn trong một số trường hợp, nhưng đừng annotation tùy tiện để “ép stable” khi contract mutation không đúng. Sai stability contract có thể biến bug state thành thứ khó phát hiện hơn.

# 7. Identity và `key`

Compose nhớ state dựa trên identity/position trong composition. Khi một nhóm composable có thể đổi vị trí, `key` giúp runtime hiểu logical identity.

```kotlin
for (item in items) {
    key(item.id) {
        ItemRow(item)
    }
}
```

Trong `LazyColumn`, dùng `items(..., key = { it.id })` thường là cách phù hợp hơn. Key phải stable và unique trong phạm vi list.

# 8. Chọn background API theo semantics

Android có nhiều cơ chế background vì mỗi loại công việc có requirement khác nhau. **WorkManager** phù hợp deferred, durable work có constraint và có thể chạy lại sau process death. **Foreground Service** dùng cho tác vụ user-visible đang diễn ra và phải tuân notification/FGS type/restriction. **AlarmManager** dành cho alarm theo thời điểm; exact alarm chỉ khi use case thực sự cần và có policy/permission tương ứng.

Coroutine trong ViewModel chỉ phù hợp công việc gắn lifetime ViewModel, không thay thế durable background scheduling.

Một quyết định tốt bắt đầu bằng câu hỏi: công việc có phải hoàn tất nếu app/process chết không, có cần thời điểm chính xác không, user có nhận biết đang chạy không, có constraint mạng/charging không, và OS có quyền trì hoãn không. Sau đó mới chọn API.

# 9. Foreground service và notification restriction

Foreground service không phải “service chạy mãi”. Android ngày càng giới hạn việc start FGS từ background và yêu cầu khai báo service type/permission phù hợp use case. Vì policy thay đổi theo API level, production code phải đọc behavior change của target SDK hiện tại.

Notification channel trên Android 8+ có behavior do user kiểm soát. App không nên giả định importance luôn như lúc tạo channel ban đầu. Android mới cũng có notification runtime permission; UX cần hoạt động hợp lý khi user từ chối.

# 10. Retry, idempotency và exponential backoff

Retry chỉ an toàn khi operation idempotent hoặc backend có idempotency key. GET thường retry dễ hơn POST tạo giao dịch. Nếu request “create order” timeout sau khi server đã commit nhưng client chưa nhận response, retry mù có thể tạo order thứ hai.

Exponential backoff giúp giảm tải khi backend/mạng có vấn đề; jitter tránh nhiều client retry cùng thời điểm. Retry policy phải phân loại lỗi: 400 validation thường không retry, 401 có thể trigger auth refresh, 429/503 có thể retry theo policy và `Retry-After` nếu server cung cấp.

# 11. HTTP cache và app cache

HTTP cache có thể giảm latency/data nhưng phải tôn trọng freshness/validation semantics. ETag/If-None-Match cho phép revalidation. App-layer cache như Room giải quyết source-of-truth/offline UX khác với HTTP cache ở transport layer.

Khi nói “cache”, luôn trả lời cache cái gì, key là gì, stale sau bao lâu, invalidate bằng gì, và khi cache/network khác nhau thì nguồn nào thắng.

# 12. TLS và certificate pinning

TLS mặc định của platform/OkHttp thường an toàn hơn tự viết trust manager. Không bao giờ “fix SSL error” bằng trust-all certificate verifier trong production.

Certificate pinning tăng một số lớp phòng thủ nhưng tạo operational risk khi certificate rotation. Nếu dùng, phải có backup pin và quy trình rotation rõ ràng. Pinning không thay thế hostname verification, authorization hay secure backend.

# 13. WebSocket, SSE và long-lived connection

WebSocket/SSE là connection lâu sống; cần lifecycle, reconnect, heartbeat, duplicate event và ordering strategy. Đừng gắn connection trực tiếp vào composable lifetime nếu domain session sống rộng hơn màn hình.

Khi reconnect, server/client cần biết từ sequence nào tiếp tục hoặc chấp nhận duplicate rồi deduplicate bằng event ID. Nếu không có protocol strategy, “reconnect tự động” có thể gây mất hoặc lặp dữ liệu.

# 14. Storage, backup và dữ liệu nhạy cảm

DataStore phù hợp setting/preferences nhỏ; Room phù hợp relational structured data; file storage phù hợp blob/document; MediaStore/Storage Access Framework dùng cho media/document theo scoped storage model.

Dữ liệu nhạy cảm cần threat model. Android Keystore bảo vệ key material bằng system/hardware-backed capability khi có, nhưng ciphertext, metadata và backup policy vẫn phải thiết kế. Kiểm tra `android:allowBackup`, data extraction rules và cloud/device-transfer behavior để tránh dữ liệu không nên rời thiết bị bị backup ngoài ý muốn.

# 15. JVM test, Robolectric và instrumented test

Pure Kotlin/domain test chạy JVM nhanh nhất. Robolectric mô phỏng nhiều Android API trên JVM và hữu ích ở middle layer nhưng không thay thế thiết bị thật cho mọi behavior. Instrumented test kiểm tra integration với Android runtime/device.

Không nên đưa toàn bộ test xuống instrumented chỉ vì code chạm Android. Nếu business logic có thể tách khỏi framework boundary, test phần logic ở JVM và chỉ giữ số lượng nhỏ integration test quanh boundary Android.

# 16. Compose UI testing

Compose UI test tương tác với **semantics tree**, không phải pixel tree. Điều này khuyến khích UI có semantics/accessibility tốt.

```kotlin
composeTestRule
    .onNodeWithText("Save")
    .performClick()
```

Test nên assert behavior user-visible thay vì internal composable call. Khi test khó tìm node, đôi khi vấn đề thật nằm ở semantics/accessibility chứ không phải testing API.

# 17. Performance test: Macrobenchmark và Baseline Profile

Macrobenchmark đo journey như startup/scroll/interaction ở app level. Baseline Profile ghi lại code path quan trọng để ART compile tối ưu sớm hơn. Hai thứ liên quan nhưng không đồng nghĩa: profile có thể cải thiện runtime path, benchmark dùng để chứng minh improvement/regression.

Benchmark cần thiết bị/thermal state đủ ổn định. Một lần chạy trên emulator mạnh không phải evidence production.

# 18. Android Lint và static analysis

Android Lint hiểu nhiều Android-specific issue như lifecycle, resource, API level, manifest và Compose. Compiler warning, Lint, formatter/static-analysis tool như ktlint/Detekt nếu team chọn dùng có thể trở thành CI quality gate.

Baseline chỉ nên là chiến lược migration: ghi nhận debt hiện có để chặn debt mới, rồi giảm dần baseline. Không để baseline trở thành “thùng rác warning vĩnh viễn”.

# 19. Senior review framework

Khi review một feature, đừng chỉ đọc happy path. Hãy hỏi: coroutine thuộc scope nào, cancellation có dọn resource không, Flow có backpressure semantics đúng không, state có source of truth nào, process death xảy ra thì sao, retry có duplicate side effect không, local schema upgrade ra sao, background work có đúng API không, dữ liệu nhạy cảm có backup/log không, và metric nào chứng minh performance ổn.

Senior-level code review là kiểm tra **lifetime + ownership + failure + recovery + observability**, không chỉ style hoặc pattern name.

# 20. Checklist hoàn thiện Advanced / Senior

Bạn nên reasoning được về cancellation/failure, backpressure, Compose snapshot/phase/identity, background execution semantics, storage/backup, network retry/TLS, long-lived connection, test-layer trade-off, benchmark và quality gate. Seniority thể hiện ở khả năng dự đoán failure mode và blast radius trước khi chọn library hoặc pattern.
