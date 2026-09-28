# Kotlin + Android Master ghi chú (note / 노트) — Intermediate

> **Mạch đọc:** Đặt **Kotlin + Android Master ghi chú (note / 노트) — Intermediate** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Mục lục** sang **8.1 phạm vi (scope / 범위) là đơn vị sở hữu (owner / 오너) của thời gian tồn tại (lifetime / 수명)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


> Mục tiêu: chuyển từ “viết được app” sang “xây app có cấu trúc đúng”, hiểu coroutine/luồng (flow / 흐름), ViewModel, nguồn chuẩn (source of truth / 정본), Room/networking, vòng đời (lifecycle / 생명주기), testing, DI, di chuyển (migration / 마이그레이션) và các dạng thất bại (failure mode / 실패 모드) cơ bản trước khi sang cấp cao (senior / 시니어). Ở mức (level / 수준) này, mỗi API phải được đặt vào đúng **đơn vị sở hữu (owner / 오너), thời gian tồn tại (lifetime / 수명) và luồng dữ liệu (data flow / 데이터 흐름)**.

## Mục lục

1. Kotlin idioms quan trọng
2. phạm vi (scope / 범위) functions
3. Extension hàm (function / 함수)/thuộc tính (property / 속성)
4. Generics và variance
5. đối tượng (object / 객체), companion đối tượng (object / 객체), singleton
6. Delegation và delegated properties
7. Sequences
8. Coroutine nền tảng
9. Structured tính đồng thời (concurrency / 동시성)
10. luồng (flow / 흐름), StateFlow, SharedFlow
11. Android app kiến trúc (architecture / 아키텍처)
12. ViewModel và UI trạng thái (state / 상태)
13. Repository, dữ liệu (data / 데이터) nguồn (source / 소스) và nguồn chuẩn (source of truth / 정본)
14. Room
15. Networking
16. phụ thuộc (dependency / 의존성) Injection
17. điều hướng (navigation / 내비게이션) nâng cao
18. Compose trạng thái (state / 상태)/tác động (effect / 효과)
19. XML interoperability
20. Lifecycle-aware collection
21. WorkManager
22. DataStore
23. Testing
24. lỗi (error / 오류) handling và thử lại (retry / 재시도)
25. bảo mật (security / 보안)/cấu hình (configuration / 구성) căn bản
26. hiện đại (modern / 현대적) vs legacy di chuyển (migration / 마이그레이션) notes
27. dự án (project / 프로젝트) kiến trúc (architecture / 아키텍처) mẫu
28. Serialization và DTO ranh giới (boundary / 경계)
29. Parcelable, Bundle và thành phần (component / 컴포넌트) ranh giới (boundary / 경계)
30. Files, MediaStore và scoped lưu trữ (storage / 저장소)
31. Notification và foreground công việc (work / 작업)
32. Deep link và App Link
33. bản dựng (build / 빌드) variants, bản phát hành (release / 릴리스)/gỡ lỗi (debug / 디버그) và BuildConfig
34. Coroutine/luồng (flow / 흐름) testing có kiểm soát thời gian
35. tiến trình (process / 프로세스) death như trường hợp kiểm thử (test case / 테스트 케이스) thiết kế
36. Intermediate tích hợp (integration / 통합) dự án (project / 프로젝트)
37. trạng thái (state / 상태) thời gian tồn tại (lifetime / 수명) ma trận (matrix / 행렬)
38. Stale-result race và thứ tự (ordering / 순서)
39. Repository hiện thực (implementation / 구현) end-to-end
40. thử lại (retry / 재시도), idempotency và ambiguous kết quả (outcome / 결과)
41. gỡ lỗi (debug / 디버그) vs bản phát hành (release / 릴리스): cách điều tra khác biệt sản phẩm tạo ra (artifact / 산출물)
42. di chuyển (migration / 마이그레이션) scenario: legacy → hiện đại (modern / 현대적) theo từng seam
43. Debugging playbook theo tầng (layer / 계층)
44. Intermediate completion checklist

---

# 1. Kotlin idioms quan trọng

Kotlin không chỉ là Java viết ngắn hơn. Idiomatic Kotlin ưu tiên immutable giá trị (value / 값), expression, extension, sealed hierarchy và higher-order hàm (function / 함수) khi chúng làm intent rõ hơn.

```kotlin
user?.let(::send)
```

Không chuỗi (chain / 사슬) phạm vi (scope / 범위) hàm (function / 함수) chỉ để giảm số dòng. mã (code / 코드) rõ ràng bằng `if` hoặc cục bộ (local / 로컬) variable thường tốt hơn một chuỗi (chain / 사슬) khó đọc.

# 2. phạm vi (scope / 범위) functions: `let`, `run`, `with`, `apply`, `also`

| hàm (function / 함수) | Receiver | Trả về | Dùng tốt khi |
|---|---|---|---|
| `let` | `it` | lambda kết quả (result / 결과) | null-chain, transform |
| `run` | `this` | lambda kết quả (result / 결과) | configure + compute |
| `with(x)` | `this` | lambda kết quả (result / 결과) | nhóm nhiều lời gọi (call / 호출) |
| `apply` | `this` | receiver | configure đối tượng (object / 객체) |
| `also` | `it` | receiver | log/side tác động (effect / 효과) nhỏ |

Ví dụ `apply` để cấu hình đối tượng (object / 객체):

```kotlin
val request = Request.Builder().apply {
    url(baseUrl)
    header("Accept", "application/json")
}.build()
```

Ví dụ `let` để transform nullable giá trị (value / 값):

```kotlin
val userId: Long? = rawId?.toLongOrNull()
val profile = userId?.let(repository::findProfile)
```

Nested `let/apply/run` dễ làm mất ngữ nghĩa `this`/`it`; hãy đặt tên lambda parameter hoặc tách khối (block / 블록).

# 3. Extension hàm (function / 함수) và thuộc tính (property / 속성)

Extension được resolve statically theo declared kiểu (type / 타입), không phải virtual dispatch. Nó phù hợp thêm convenience/API adapter, không thay polymorphism thời gian chạy (runtime / 런타임).

```kotlin
fun String.toUserIdOrNull(): UserId? =
    toLongOrNull()?.let(::UserId)
```

Extension hữu ích để đặt ánh xạ (mapping / 매핑) gần ranh giới (boundary / 경계), nhưng đừng tạo “utility không gian tên (namespace / 네임스페이스) vô hình” với hàng trăm extension không discoverable.

# 4. Generics và variance

`out T` cho producer, `in T` cho bên tiêu thụ (consumer / 소비자). Star projection `Foo<*>` hữu ích khi chưa biết kiểu (type / 타입) argument nhưng vẫn muốn thao tác trong giới hạn an toàn.

```kotlin
interface Producer<out T> {
    fun produce(): T
}

interface Consumer<in T> {
    fun consume(value: T)
}
```

Variance giúp API linh hoạt nhưng cần giữ kiểu (type / 타입) đặc tả hợp đồng (contract / 계약) dễ hiểu; nếu signature đầy projection phức tạp, lớp trừu tượng (abstraction / 추상화) có thể đang quá generic.

# 5. `object`, `companion object` và singleton

`object` tạo singleton theo class-loading ngữ nghĩa (semantics / 의미론).

```kotlin
object AppClock {
    fun now(): Instant = Instant.now()
}
```

Không biến mọi dịch vụ (service / 서비스) thành toàn cục (global / 전역) singleton; stateful singleton làm testing/thời gian tồn tại (lifetime / 수명) khó hơn. DI thường quản lý vòng đời (lifecycle / 생명주기) rõ hơn. `companion object` phù hợp factory/constant gắn lớp (class / 클래스) nhưng không phải Java `static` hoàn toàn tương đương ở bytecode/API shape.

# 6. Delegation và delegated properties

Lớp (class / 클래스) delegation và thuộc tính (property / 속성) delegate giảm boilerplate khi ngữ nghĩa (semantics / 의미론) đúng. `lazy`, Compose trạng thái (state / 상태) delegation và custom ViewBinding delegate là ví dụ phổ biến.

```kotlin
val parser by lazy { ExpensiveParser() }
```

`lazy` cũng có thời gian tồn tại (lifetime / 수명) của đối tượng (object / 객체) đơn vị sở hữu (owner / 오너); nếu đơn vị sở hữu (owner / 오너) là singleton thì lazy giá trị (value / 값) cũng gần như process-lifetime. Đừng dùng `lazy` để che phụ thuộc (dependency / 의존성)/toàn cục (global / 전역) trạng thái (state / 상태).

# 7. Sequences

`Sequence` lazy và có thể giảm intermediate collection với chuỗi xử lý (pipeline / 파이프라인) dài/short-circuit.

```kotlin
val result = source
    .asSequence()
    .map(::normalize)
    .filter(::isValid)
    .take(20)
    .toList()
```

Collection nhỏ/chuỗi (chain / 사슬) ngắn không mặc định nhanh hơn; hiệu năng (performance / 성능) cần đo.

# 8. Coroutine nền tảng

<!-- merge: preserve both chuẩn gốc (canonical / 정본) variants -->
Coroutine không đồng nghĩa luồng thực thi (thread / 스레드). `suspend` chỉ nói hàm (function / 함수) có thể suspend; nó không đảm bảo hàm (function / 함수) chạy background.

```kotlin
suspend fun loadUser(): User = api.loadUser()
```

Builder chính:

```kotlin
scope.launch { ... }       // Job
scope.async { ... }        // Deferred<T>
withContext(dispatcher) { ... }
```

`launch` cho công việc (work / 작업) không trả giá trị (value / 값) trực tiếp; `async` cho concurrent computation cần `await`. Suspend API của dữ liệu (data / 데이터) tầng (layer / 계층) nên **main-safe**: nếu hiện thực (implementation / 구현) dùng blocking I/O, chính tầng (layer / 계층) đó chịu trách nhiệm đổi dispatcher.

```kotlin
suspend fun parseLargeFile(file: File): Model = withContext(ioDispatcher) {
    parser.parse(file)
}
```

# 9. Structured tính đồng thời (concurrency / 동시성)

Coroutine con sống trong phạm vi (scope / 범위) cha. Điều này tạo quyền sở hữu (ownership / 소유권) và cancellation có cấu trúc.
<!-- merge: preserve both chuẩn gốc (canonical / 정본) variants -->
Coroutine là một computation có **thời gian tồn tại (lifetime / 수명), cancellation và thực thi (execution / 실행) ngữ cảnh (context / 맥락)**, không phải “luồng thực thi (thread / 스레드) nhẹ” theo nghĩa mỗi coroutine tương ứng một luồng thực thi (thread / 스레드) riêng. Coroutine có thể suspend mà không khối (block / 블록) luồng thực thi (thread / 스레드), rồi resume sau đó theo dispatcher/ngữ cảnh (context / 맥락). Nhưng `suspend` **không tự động biến blocking mã (code / 코드) thành non-blocking**: nếu gọi JDBC/tệp (file / 파일)/mạng (network / 네트워크) API blocking bên trong suspend hàm (function / 함수) trên Main, main luồng thực thi (thread / 스레드) vẫn bị khối (block / 블록).

```kotlin
suspend fun loadUser(): User {
    delay(100) // suspend, không giữ thread trong lúc chờ
    return User(...)
}
```

## 8.1 phạm vi (scope / 범위) là đơn vị sở hữu (owner / 오너) của thời gian tồn tại (lifetime / 수명)

Mỗi coroutine phải trả lời được “ai chịu trách nhiệm cancel nó?”. Android có vài phạm vi (scope / 범위) phổ biến:

```text
viewModelScope
= work sống cùng ViewModel

lifecycleScope
= work sống cùng LifecycleOwner

LaunchedEffect scope
= work sống cùng vị trí/key trong Composition

WorkManager worker scope
= work sống cùng execution của Worker

application/external scope
= chỉ dùng khi operation thật sự phải sống lâu hơn screen và có owner toàn app rõ ràng
```

Nếu tạo `CoroutineScope(SupervisorJob() + Dispatchers.IO)` tùy ý trong repository mà không có đơn vị sở hữu (owner / 오너)/shutdown chính sách (policy / 정책), ta đã tạo thời gian tồn tại (lifetime / 수명) ẩn.

## 8.2 `launch`, `async`, `withContext` khác nhau về đặc tả hợp đồng (contract / 계약)

```kotlin
scope.launch { ... }       // Job, side-effect/lifecycle work
scope.async { ... }        // Deferred<T>, concurrent result
withContext(dispatcher) { ... } // chuyển context và chờ kết quả
```

`async` chỉ hữu ích khi có **tính đồng thời (concurrency / 동시성) có chủ đích**. Viết:

```kotlin
val value = async { repository.load() }.await()
```

mà không chạy song song với gì thường chỉ thêm `Deferred` không cần thiết.

`withContext` không tạo “background job độc lập”; caller chờ khối (block / 블록) đó hoàn tất và cancellation vẫn nằm trong structured phạm vi (scope / 범위).

## 8.3 Main-safety là đặc tả hợp đồng (contract / 계약) của lower tầng (layer / 계층)

Suspend hàm (function / 함수) ở repository/use trường hợp (case / 사례) nên đủ main-safe để caller không phải nhớ dispatcher hiện thực (implementation / 구현) detail.

```kotlin
class FileRepository(
    private val ioDispatcher: CoroutineDispatcher
) {
    suspend fun readLargeFile(): Data = withContext(ioDispatcher) {
        blockingParser.read()
    }
}
```

Nếu mỗi ViewModel phải nhớ phương thức (method / 메서드) nào cần `Dispatchers.IO`, threading chính sách (policy / 정책) đã leak lên UI tầng (layer / 계층).

## 8.4 Cancellation là cooperative

Cancellation không “giết luồng thực thi (thread / 스레드)”. Coroutine dừng tại suspension điểm (point / 지점) hoặc khi mã (code / 코드) chủ động kiểm tra cancellation.

CPU vòng lặp (loop / 루프) dài nên có checkpoint khi phù hợp:

```kotlin
while (hasMoreWork()) {
    ensureActive()
    processChunk()
}
```

Cleanup thường đặt trong `finally`. Không dùng `NonCancellable` cho toàn thao tác (operation / 연산); chỉ cân nhắc vùng cleanup ngắn thật sự phải hoàn thành.

```kotlin
try {
    repository.sync()
} finally {
    releaseResource()
}
```

Không swallow `CancellationException` thành lĩnh vực (domain / 도메인) lỗi (error / 오류) thông thường. Cancellation thường là điều khiển (control / 제어) tín hiệu (signal / 신호) cho thời gian tồn tại (lifetime / 수명), không phải “mạng (network / 네트워크) failed”.

# 9. Structured tính đồng thời (concurrency / 동시성)

Structured tính đồng thời (concurrency / 동시성) nghĩa coroutine tạo ra một **Job cây (tree / 트리)** có parent-child relationship rõ ràng. Parent không được xem là hoàn tất trong khi child còn chạy; cancellation và thất bại (failure / 실패) đi theo quy tắc (rule / 규칙) của cây (tree / 트리) thay vì coroutine “bay tự do”.
<!-- end merged variant -->

```kotlin
suspend fun loadPage(): Page = coroutineScope {
    val user = async { userRepo.load() }
    val posts = async { postRepo.load() }
    Page(user.await(), posts.await())
}
```

<!-- merge: preserve both chuẩn gốc (canonical / 정본) variants -->
Chỉ parallel khi hai thao tác (operation / 연산) độc lập. `supervisorScope` phù hợp khi sibling thất bại (failure / 실패) độc lập; nó không tự xử lý lỗi (error / 오류).

Tránh `GlobalScope`. Hỏi: **ai sở hữu coroutine và khi đơn vị sở hữu (owner / 오너) chết thì công việc (work / 작업) có nên tiếp tục không?**

# 10. luồng (flow / 흐름), StateFlow và SharedFlow

`Flow<T>` thường cold: upstream chạy khi collect. `StateFlow` là hot trạng thái (state / 상태) holder có hiện tại (current / 현재) giá trị (value / 값). `SharedFlow` là hot broadcast stream với replay/buffer cấu hình được.
<!-- merge: preserve both chuẩn gốc (canonical / 정본) variants -->
Ở đây `user` và `posts` thực sự chạy concurrent. Nếu một child thất bại (fail / 실패) trong `coroutineScope`, sibling còn lại thường bị cancel vì kết quả `Page` không còn tạo được đầy đủ.

`supervisorScope` dùng khi thất bại (failure / 실패) của một child không nên tự động cancel sibling:

```kotlin
supervisorScope {
    launch { refreshAvatar() }
    launch { refreshRecommendations() }
}
```

Nhưng supervision không có nghĩa “bỏ qua exception”. Mỗi thất bại (failure / 실패) vẫn cần đơn vị sở hữu (owner / 오너) và lỗi (error / 오류) chính sách (policy / 정책).

## 9.1 tính đồng thời (concurrency / 동시성) không đồng nghĩa parallelism

Hai coroutine có thể concurrent nhưng chạy trên cùng luồng thực thi (thread / 스레드) theo thời gian xen kẽ. Parallelism chỉ xảy ra khi thời gian chạy (runtime / 런타임)/dispatcher cho phép chạy thật sự đồng thời trên nhiều luồng thực thi (thread / 스레드)/cốt lõi (core / 핵심).

Điều cần thiết kế là:

```text
operation nào có thể overlap?
operation nào phải serialize?
operation cũ có được overwrite result mới không?
bao nhiêu request cùng lúc là hợp lý?
```

## 9.2 Duplicate hành động (action / 동작) và stale kết quả (result / 결과) là bug tính đồng thời (concurrency / 동시성) rất phổ biến

Ví dụ người dùng (user / 사용자) đổi tìm kiếm (search / 검색) truy vấn (query / 쿼리) nhanh:

```text
request A(query="ko") bắt đầu
request B(query="kotlin") bắt đầu sau
B trả về trước → UI đúng
A trả về sau → nếu update state vô điều kiện, UI bị quay về result cũ
```

Giải pháp có thể là `flatMapLatest`, cancel job cũ, generation/phiên bản (version / 버전) đơn vị từ (token / 토큰) hoặc repository đặc tả hợp đồng (contract / 계약) khác. Mutex không tự giải quyết stale-result ngữ nghĩa (semantic / 의미적).

Tránh `GlobalScope` trong ứng dụng (application / 애플리케이션) mã (code / 코드). phạm vi (scope / 범위) phải có đơn vị sở hữu (owner / 오너). Nếu thao tác (operation / 연산) cần sống qua screen điều hướng (navigation / 내비게이션) hoặc tiến trình (process / 프로세스) scheduling, hãy chọn đơn vị sở hữu (owner / 오너)/thành phần nguyên thủy (primitive / 기본 요소) đúng thay vì cố kéo dài một coroutine UI.

# 10. luồng (flow / 흐름), StateFlow và SharedFlow

`Flow<T>` biểu diễn chuỗi giá trị theo thời gian. Cold luồng (flow / 흐름) thường chỉ chạy upstream khi có collector.

```kotlin
fun observeUsers(): Flow<List<User>> = dao.observeUsers()
```

Một cold luồng (flow / 흐름) không phải “background tác vụ (task / 작업) tự chạy”. Nếu không collect, phần lớn upstream cold luồng (flow / 흐름) không thực thi.

## 10.1 Operator là ngữ nghĩa (semantic / 의미적), không chỉ cú pháp (syntax / 문법) chuỗi (chain / 사슬)

```kotlin
flow
    .map { ... }
    .filter { ... }
    .distinctUntilChanged()
    .debounce(300)
    .catch { ... }
    .combine(other) { a, b -> ... }
```

`combine` giữ latest giá trị (value / 값) từ nhiều stream; `zip` ghép theo cặp emission; `debounce` đợi khoảng yên; `distinctUntilChanged` bỏ emission lặp theo equality. Chọn operator sai có thể tạo bug thứ tự (ordering / 순서) chứ không chỉ khác hiệu năng (performance / 성능).

`flatMapLatest` rất hữu ích cho tìm kiếm (search / 검색)/truy vấn (query / 쿼리) mà yêu cầu (request / 요청) mới phải làm kết quả (result / 결과) cũ hết hiệu lực:

```kotlin
query
    .debounce(300)
    .flatMapLatest(repository::search)
```

## 10.2 luồng (flow / 흐름) ngữ cảnh (context / 맥락) và `flowOn`

Luồng (flow / 흐름) giữ ngữ cảnh (context / 맥락) preservation. `flowOn(dispatcher)` thay ngữ cảnh (context / 맥락) của **upstream trước nó**, không đơn giản là “mọi thứ sau đây chạy IO”. Collector vẫn chạy trong ngữ cảnh (context / 맥락) nơi collect trừ khi ranh giới (boundary / 경계) khác thay đổi.

```kotlin
flow {
    emit(loadBlocking())
}
    .flowOn(ioDispatcher)
    .map(::toUiModel)
```

Hiểu upstream/downstream quan trọng khi gỡ lỗi (debug / 디버그) luồng thực thi (thread / 스레드), cancellation và hiệu năng (performance / 성능).

## 10.3 Backpressure: producer nhanh hơn bên tiêu thụ (consumer / 소비자)

Không phải mọi emission đều cần kết xuất (render / 렌더링). Các công cụ (tool / 도구) có ngữ nghĩa (semantic / 의미적) khác nhau:

```text
buffer
= cho producer và consumer overlap với buffer

conflate
= bỏ intermediate value khi consumer chậm, giữ latest direction

collectLatest
= cancel xử lý value cũ khi value mới tới
```

Không dùng `conflate` cho sự kiện (event / 이벤트) mà từng item đều phải xử lý, ví dụ giao dịch (transaction / 트랜잭션) mutation hàng đợi (queue / 큐).

## 10.4 `StateFlow` là trạng thái (state / 상태) holder

`StateFlow` là hot, có hiện tại (current / 현재) giá trị (value / 값) và phù hợp trạng thái (state / 상태) có thể đọc ở bất kỳ thời điểm nào.
<!-- end merged variant -->

```kotlin
private val _uiState = MutableStateFlow(UiState())
val uiState: StateFlow<UiState> = _uiState.asStateFlow()
```

<!-- merge: preserve both chuẩn gốc (canonical / 정본) variants -->
Không chọn SharedFlow chỉ vì “sự kiện (event / 이벤트)”. Trước hết hỏi sự kiện (event / 이벤트) có cần survive collector inactive/recreation không. Nếu câu trả lời có, có thể đó là durable trạng thái (state / 상태) chứ không phải one-off sự kiện (event / 이벤트).

Các operator như `debounce`, `combine`, `distinctUntilChanged`, `flatMapLatest` cần dùng theo ngữ nghĩa (semantics / 의미론). `flatMapLatest` hợp tìm kiếm (search / 검색) latest-wins nhưng không hợp kiểm tra (audit / 감사) stream nơi mọi item phải xử lý.
<!-- merge: preserve both chuẩn gốc (canonical / 정본) variants -->
UI trạng thái (state / 상태) nên immutable từ bên ngoài; ViewModel là đơn vị sở hữu (owner / 오너) mutation.

`StateFlow` conflates theo equality/giá trị (value / 값) cập nhật (update / 업데이트) ngữ nghĩa (semantics / 의미론); collector chậm không có nghĩa được nhận mọi intermediate snapshot. Đây thường đúng với trạng thái (state / 상태) vì UI quan tâm latest truth.

## 10.5 `SharedFlow` là dùng chung (shared / 공유) stream, không mặc định là “sự kiện (event / 이벤트) solution”

`SharedFlow` có thể cấu hình replay/buffer và share emission cho nhiều collector. Nó hữu ích cho dùng chung (shared / 공유) upstream hoặc sự kiện (event / 이벤트) stream thực sự.

Nhưng các sự kiện (event / 이벤트) có nghiệp vụ (business / 비즈니스) meaning lâu dài nên thường mô hình (model / 모델) thành trạng thái (state / 상태)/durable dữ liệu (data / 데이터) thay vì phát một tín hiệu có thể mất khi UI không collect. Ví dụ “payment completed” là lĩnh vực (domain / 도메인) trạng thái (state / 상태); snackbar “Copied” có thể transient.

## 10.6 `stateIn` và `shareIn`

Cold luồng (flow / 흐름) có thể được convert thành hot dùng chung (shared / 공유) stream trong phạm vi (scope / 범위) rõ ràng:

```kotlin
val uiState = repository.observeUsers()
    .map(::toUiState)
    .stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(5_000),
        initialValue = UiState.Loading
    )
```

`SharingStarted` quyết định upstream sống khi nào. Đây là **thời gian tồn tại (lifetime / 수명) quyết định (decision / 결정)**, không chỉ tối ưu hóa (optimization / 최적화). `Eagerly`, `Lazily`, `WhileSubscribed` có sự đánh đổi (trade-off / 트레이드오프) khác nhau về freshness, tài nguyên (resource / 자원) và restart.
<!-- end merged variant -->

# 11. Android app kiến trúc (architecture / 아키텍처)

Kiến trúc (architecture / 아키텍처) hiện đại tối thiểu có UI tầng (layer / 계층) và dữ liệu (data / 데이터) tầng (layer / 계층); lĩnh vực (domain / 도메인) tầng (layer / 계층) optional.

```text
UI
→ ViewModel / state holder
→ UseCase (optional)
→ Repository
→ local/remote/platform data source
```

Điểm quan trọng không phải số tầng (layer / 계층) mà là **phụ thuộc (dependency / 의존성) direction** và **quyền sở hữu (ownership / 소유권)**.

UI không gọi Retrofit/Room trực tiếp vì UI không nên biết chính sách (policy / 정책) bộ nhớ đệm (cache / 캐시)/thử lại (retry / 재시도)/sync. Repository không biết Button/NavController vì dữ liệu (data / 데이터) tầng (layer / 계층) không nên phụ thuộc presentation.

## 11.1 kiến trúc (architecture / 아키텍처) bắt đầu từ trạng thái (state / 상태)

Trước khi tạo lớp (class / 클래스), phân loại trạng thái (state / 상태):

```text
UI ephemeral state
screen state
business/application data
persisted data
server truth
```

Ví dụ tìm kiếm (search / 검색) văn bản (text / 텍스트) nhỏ có thể ở ViewModel/SavedStateHandle; danh sách article không nên bị nhét vào saved trạng thái (state / 상태) nếu có thể reload từ Room.

## 11.2 lĩnh vực (domain / 도메인) tầng (layer / 계층) là optional

Use trường hợp (case / 사례) có giá trị khi thao tác (operation / 연산) chứa chính sách (policy / 정책)/nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙)/reuse. Nếu `GetUserUseCase` chỉ gọi một dòng `repository.getUser()`, thêm tầng (layer / 계층) có thể chỉ tăng điều hướng (navigation / 내비게이션) chi phí (cost / 비용).

# 12. ViewModel và UI trạng thái (state / 상태)

<!-- merge: preserve both chuẩn gốc (canonical / 정본) variants -->
ViewModel là screen-level trạng thái (state / 상태) holder/orchestrator, không phải nơi chứa toàn bộ networking, SQL và dịch vụ (service / 서비스) locator.
<!-- merge: preserve both chuẩn gốc (canonical / 정본) variants -->
ViewModel là trạng thái (state / 상태) holder ở screen/điều hướng (navigation / 내비게이션) phạm vi (scope / 범위), không phải nơi “mọi lô-gic (logic / 논리) Android” phải chuyển vào. Nó thường nhận sự kiện (event / 이벤트), gọi lĩnh vực (domain / 도메인)/dữ liệu (data / 데이터) thao tác (operation / 연산) và expose trạng thái (state / 상태) cho UI.
<!-- end merged variant -->

```kotlin
data class UserUiState(
    val users: List<UserUi> = emptyList(),
    val isInitialLoading: Boolean = false,
    val isRefreshing: Boolean = false,
    val error: UiError? = null
)
<!-- merge: preserve both canonical variants -->
```

Phân biệt initial tải (load / 로드) và refresh giúp UI giữ cached content thay vì thay toàn màn hình bằng spinner.
<!-- merge: preserve both chuẩn gốc (canonical / 정본) variants -->

Lớp (class / 클래스) UserViewModel(
    private val repository: UserRepository
) : ViewModel() {
    private val _uiState = MutableStateFlow(UserUiState())
    val uiState = _uiState.asStateFlow()

    fun refresh() {
        viewModelScope.launch {
            _uiState.cập nhật (update / 업데이트) { it.bản sao (copy / 복사)(loading = true, errorMessage = null) }
            try {
                repository.refresh()
            } catch (e: CancellationException) {
                throw e
            } catch (e: Throwable) {
                _uiState.cập nhật (update / 업데이트) { it.bản sao (copy / 복사)(errorMessage = e.message) }
            } finally {
                _uiState.cập nhật (update / 업데이트) { it.bản sao (copy / 복사)(loading = false) }
            }
        }
    }
}
```

## 12.1 State ownership trước API choice

Trước khi chọn `remember`, `StateFlow` hay SavedStateHandle, hỏi state phải sống bao lâu.

```văn bản (text / 텍스트)
chỉ trong một recomposition cây (tree / 트리)
→ remember

qua cấu hình (configuration / 구성) recreation cho UI giá trị (value / 값) nhỏ
→ rememberSaveable hoặc SavedStateHandle tùy đơn vị sở hữu (owner / 오너)

screen trạng thái (state / 상태)/nghiệp vụ (business / 비즈니스) tương tác (interaction / 상호작용) trong cùng tiến trình (process / 프로세스)
→ ViewModel + StateFlow thường phù hợp

qua tiến trình (process / 프로세스) death
→ reconstruct từ SavedStateHandle nhỏ + repository/cơ sở dữ liệu (database / 데이터베이스)/máy chủ (server / 서버)

durable nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터)
→ cơ sở dữ liệu (database / 데이터베이스)/DataStore/máy chủ (server / 서버), không dựa vào ViewModel
```

ViewModel sống qua configuration change nhưng **không sống qua process death**.

## 12.2 Authoritative state và derived state

Không lưu cùng một fact thành nhiều mutable source nếu có thể derive.

Sai hướng:

```văn bản (text / 텍스트)
repository có users
ViewModel bản sao (copy / 복사) users vào mutable danh sách (list / 목록) riêng
Composable lại bản sao (copy / 복사) vào remember danh sách (list / 목록) khác
```

Ba source có thể lệch nhau.

Tốt hơn là xác định source of truth, sau đó derive filter/sort/presentation state từ nó.

## 12.3 Impossible state và state machine

Nhiều boolean độc lập dễ tạo tổ hợp vô nghĩa:

```văn bản (text / 텍스트)
loading=true
contentVisible=true
fatalError=true
```

Có thể dùng sealed state cho mutually exclusive screen state hoặc giữ content + refresh/error metadata nếu UX cho phép content và refresh đồng thời. Không có một data class duy nhất đúng; state model phải phản ánh invariant UI.

## 12.4 Concurrency trong ViewModel

Hai `refresh()` cùng chạy có thể tạo duplicate request; request cũ trả sau có thể overwrite state mới; logout/account switch có thể để response từ session cũ quay lại UI.

Giải pháp tùy semantic:

```văn bản (text / 텍스트)
cancel previous job
single-flight
Mutex/serialization
flatMapLatest cho query-driven công việc (work / 작업)
generation/session đơn vị từ (token / 토큰) để bỏ stale kết quả (result / 결과)
repository làm nguồn chuẩn (source of truth / 정본) để UI không apply raw phản hồi (response / 응답) trực tiếp
```

Không giải quyết race bằng cách thêm `loading` boolean nếu ordering vẫn không được định nghĩa.
<!-- end merged variant -->

ViewModel nhận action, gọi repository/use case, rồi expose state. Nó không giữ Activity/View context và không tạo Retrofit/Room trực tiếp.

# 13. Repository, data source và source of truth

Repository không chỉ là wrapper DAO/API. Nó trả lời:

```văn bản (text / 텍스트)
nguồn (source / 소스) nào authoritative?
khi nào refresh?
cục bộ (local / 로컬) và remote merge ra sao?
lỗi (error / 오류) nào propagate?
mutation có thử lại (retry / 재시도) được không?
```

```kotlin
giao diện (interface / 인터페이스) UserRepository {
    fun observeUsers(): luồng (flow / 흐름)<danh sách (list / 목록)<người dùng (user / 사용자)>>
    suspend fun refresh()
}
```

Offline/read-cache pattern phổ biến:

```văn bản (text / 텍스트)
Room emits cached dữ liệu (data / 데이터)
→ UI kết xuất (render / 렌더링) ngay
→ refresh mạng (network / 네트워크)
→ validate/map DTO
→ giao dịch (transaction / 트랜잭션) cập nhật (update / 업데이트) Room
→ Room emits trạng thái (state / 상태) mới
```

UI không cần biết data mới tới từ network hay DB.

# 14. Room

Room bọc SQLite bằng schema/DAO/compile-time validation.

```kotlin
@thực thể (entity / 엔터티)(tableName = "users")
dữ liệu (data / 데이터) lớp (class / 클래스) UserEntity(
    @PrimaryKey val id: Long,
    val name: String
)
```

```kotlin
@Dao
giao diện (interface / 인터페이스) UserDao {
    @truy vấn (query / 쿼리)("SELECT * FROM users ORDER BY name")
    fun observeAll(): luồng (flow / 흐름)<danh sách (list / 목록)<UserEntity>>

    @Upsert
    suspend fun upsertAll(items: List<UserEntity>)
}
```

Transaction bảo vệ invariant DB. Migration phải được test với schema/data cũ thật đại diện. `fallbackToDestructiveMigration` chỉ hợp dữ liệu disposable/cache nếu product chấp nhận mất data.

# 15. Networking

Retrofit/OkHttp hoặc Ktor client đều là implementation detail của transport layer.

DTO nên tách domain model:

```kotlin
dữ liệu (data / 데이터) lớp (class / 클래스) UserDto(val id: Long, val name: String?)

fun UserDto.toDomain() = người dùng (user / 사용자)(
    id = id,
    name = name.orEmpty()
)
```

Phân biệt ít nhất:

```văn bản (text / 텍스트)
vận chuyển (transport / 전송) lỗi (error / 오류): offline, DNS, hết thời gian chờ (timeout / 타임아웃)
giao thức (protocol / 프로토콜) lỗi (error / 오류): HTTP status
serialization/lược đồ (schema / 스키마) lỗi (error / 오류)
auth/session lỗi (error / 오류)
lĩnh vực (domain / 도메인)/nghiệp vụ (business / 비즈니스) lỗi (error / 오류)
```

Không để `HttpException`/Retrofit type chảy tới Composable nếu UI chỉ cần domain action/message.

# 16. Dependency Injection

DI là quản lý graph/lifetime. Manual DI, Hilt hay Koin đều chỉ là công cụ.

```kotlin
lớp (class / 클래스) UserRepositoryImpl(
    private val api: UserApi,
    private val dao: UserDao
) : UserRepository
```

Scope sai gây leak/state-sharing. `@Singleton` không phải default tốt cho mọi class; chỉ dùng khi lifetime thực sự app-wide.

# 17. Navigation nâng cao

Navigation gồm back stack, route identity, deep link, argument và ViewModel scope. Truyền stable ID thay object lớn/stale:

<!-- merge: preserve both canonical variants -->
```văn bản (text / 텍스트)
navigate(articleId)
→ destination reconstruct dữ liệu (data / 데이터) từ repository
```

Deep link là external input, phải validate và authorization lại ở destination/domain layer.

# 18. Compose state/effect

`remember` sống qua recomposition trong cùng composition. `rememberSaveable` có thể save qua recreation cho value phù hợp. `LaunchedEffect(key)` chạy coroutine theo composition lifetime; `DisposableEffect` cleanup resource; `rememberUpdatedState` cập nhật latest callback mà không restart effect.

Không gọi network trực tiếp trong Composable body. Business operation nên do owner phù hợp quản lý.
<!-- merge: preserve both canonical variants -->
Không nên truyền object lớn qua navigation argument. Truyền stable identifier rồi load dữ liệu tại destination thường tốt hơn, tránh vượt Binder transaction limit và tránh stale object.

# 18. Compose state và effect

Compose có nhiều API state/effect với mục đích khác nhau. Chúng không thay ViewModel/repository; chúng quản lý state/effect **gắn với composition**.

`remember` giữ value qua recomposition. `rememberSaveable` thêm khả năng save qua recreation khi value saveable. `derivedStateOf` tạo derived state và hữu ích khi derived result cần tránh invalidation không cần thiết. `LaunchedEffect` chạy coroutine gắn với composition lifecycle theo key. `DisposableEffect` có cleanup. `SideEffect` publish state ra non-Compose object sau successful composition. `rememberUpdatedState` giữ latest value trong long-lived effect mà không restart effect.

```kotlin
LaunchedEffect(userId) {
    viewModel.tải (load / 로드)(userId)
}
```

Key là lifetime contract. Nếu `userId` đổi, effect cũ bị cancel và effect mới chạy. `LaunchedEffect(Unit)`/`LaunchedEffect(true)` có nghĩa “sống cùng vị trí composition này”, không phải “chạy đúng một lần toàn app”.

Business operation quan trọng thường nên có owner ngoài Composable nếu nó phải tiếp tục khi composition rời màn hình hoặc phải survive UI recreation. Không gọi network trực tiếp trong Composable body vì recomposition có thể gọi body nhiều lần.
<!-- end merged variant -->

# 19. XML interoperability

Compose và View system có thể coexist. `ComposeView` cho View/Fragment host Compose; `AndroidView` cho Compose host View.

XML/Fragment/RecyclerView/View Binding không “sai” chỉ vì Compose tồn tại. Migration incremental giảm regression risk.

# 20. Lifecycle-aware collection

<!-- merge: preserve both canonical variants -->
Compose thường dùng `collectAsStateWithLifecycle()`. View system dùng `repeatOnLifecycle`.
<!-- merge: preserve both canonical variants -->
Lifecycle của **producer** và **collector** là hai chuyện khác nhau.

Ví dụ ViewModel `StateFlow` có thể sống khi screen tạm STOPPED, nhưng UI collector nên dừng khi UI không visible để tránh render/effect không cần thiết.

Trong Compose, thường dùng:

```kotlin
val trạng thái (state / 상태) by viewModel.uiState.collectAsStateWithLifecycle()
```

Trong View system:
<!-- end merged variant -->

```kotlin
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.state.STARTED) {
        viewModel.uiState.collect(::render)
    }
}
```

<!-- merge: preserve both canonical variants -->
Collector lifecycle phải phản ánh việc UI có cần nhận update khi invisible không.
<!-- merge: preserve both canonical variants -->
`repeatOnLifecycle` cancel child collection khi lifecycle xuống dưới state yêu cầu và launch lại khi quay lên. Vì vậy upstream cold Flow có thể restart nếu không được share ở layer phù hợp. Đây là lý do `stateIn/shareIn` và sharing policy có liên hệ trực tiếp với lifecycle.

Không nên `lifecycleScope.launch { flow.collect { ... } }` vô hạn cho UI stream mà không hiểu behavior khi Activity/Fragment STOPPED.

## 20.1 Lifetime matrix cần thuộc bằng reasoning

```văn bản (text / 텍스트)
Recomposition
< Composition entry
< Fragment view vòng đời (lifecycle / 생명주기)
< Activity/Fragment vòng đời (lifecycle / 생명주기)
< ViewModel
< tiến trình (process / 프로세스)
< Persisted lưu trữ (storage / 저장소) / máy chủ (server / 서버)
```

State phải được đặt ở owner ngắn nhất nhưng đủ sống qua requirement. Đặt quá ngắn gây mất state; đặt quá dài gây leak, stale data hoặc shared state ngoài ý muốn.

## 20.2 Fragment có hai lifecycle đáng chú ý

Fragment object lifecycle và Fragment **view lifecycle** không giống nhau. Binding/collector chạm View phải gắn với `viewLifecycleOwner`, vì Fragment có thể còn tồn tại sau khi View đã destroy.

Đây là nguồn leak/crash phổ biến ở XML/View codebase và là một lý do Compose route/state ownership cần được hiểu qua lifetime thay vì chỉ syntax.
<!-- end merged variant -->

# 21. WorkManager

WorkManager cho **deferrable durable work** cần eventually run và có constraints/retry.

```kotlin
lớp (class / 클래스) SyncWorker(...) : CoroutineWorker(...) {
    override suspend fun doWork(): kết quả (result / 결과) = try {
        sync()
        kết quả (result / 결과).success()
    } catch (e: IOException) {
        kết quả (result / 결과).thử lại (retry / 재시도)()
    }
}
```

Không retry mọi exception. Validation/4xx nghiệp vụ thường cần failure, không phải retry vô hạn.

# 22. DataStore

Preferences DataStore phù hợp key-value; Proto DataStore phù hợp schema rõ. Không dùng DataStore như relational database.

Migration SharedPreferences → DataStore nên giữ key/semantic behavior, không chỉ copy giá trị.

# 23. Testing

Ba tầng cơ bản:

```văn bản (text / 텍스트)
JVM đơn vị (unit / 단위) kiểm thử (test / 테스트)
kiểm thử tích hợp (integration test / 통합 테스트) ranh giới (boundary / 경계)
instrumented/UI kiểm thử (test / 테스트)
```

Business logic nên test nhanh ngoài Android framework nếu có thể. Fake tốt cho collaborator stateful; mock tốt cho interaction hẹp.

Một test có giá trị chứng minh behavior/invariant, không khóa implementation detail.

# 24. Error handling và retry

Không `catch(Exception)` mọi nơi rồi trả string chung.

```kotlin
sealed giao diện (interface / 인터페이스) DataError {
    dữ liệu (data / 데이터) đối tượng (object / 객체) Offline : DataError
    dữ liệu (data / 데이터) đối tượng (object / 객체) hết thời gian chờ (timeout / 타임아웃) : DataError
    dữ liệu (data / 데이터) đối tượng (object / 객체) Unauthorized : DataError
    dữ liệu (data / 데이터) lớp (class / 클래스) Http(val code: Int) : DataError
    dữ liệu (data / 데이터) lớp (class / 클래스) Unknown(val cause: Throwable) : DataError
}
```

<!-- merge: preserve both canonical variants -->
UI map error sang behavior phù hợp: offline có thể vẫn render cache; unauthorized có thể trigger session recovery; validation focus field.
<!-- merge: preserve both canonical variants -->
Race test tốt phải kiểm soát ordering, không dựa vào `delay(100)` và hy vọng scheduler chạy theo ý mình. Test stale-result nên chủ động giữ request A, hoàn tất B trước rồi hoàn tất A để chứng minh state mới không bị overwrite.

# 24. Error handling
<!-- end merged variant -->

GET read thường dễ retry hơn mutation. Với POST tạo side effect, timeout có thể xảy ra sau khi server đã commit. Muốn retry an toàn cần backend idempotency contract/key.

Coroutine bị cancel do screen đóng không nên hiện snackbar error. Đừng swallow `CancellationException`.

# 25. Security/configuration căn bản

Không hardcode server secret trong APK. BuildConfig/local.properties chỉ thay cách inject value vào artifact, không làm value đóng gói trở thành secret.

Dùng HTTPS, Network Security Config khi cần, Keystore cho key material, tránh log PII/token và validate Intent/deep-link/URI input từ bên ngoài.

# 26. Modern vs legacy migration notes

Phân loại legacy trước khi rewrite:

<!-- merge: preserve both canonical variants -->
```văn bản (text / 텍스트)
Deprecated/unsafe
Supported nhưng có replacement
Still-valid cho use trường hợp (case / 사례) cụ thể
Historical-only
```

| Older API/stack | Modern direction | Lý do |
|---|---|---|
| `AsyncTask` | coroutine / WorkManager theo lifetime | AsyncTask deprecated |
| `startActivityForResult` | Activity Result API | lifecycle-aware |
| Kotlin synthetic view | View Binding / Compose | workflow cũ |
| LiveData-centric | Flow/StateFlow trong Kotlin stack | LiveData vẫn supported |
| RxJava-heavy | coroutine/Flow khi đáng migrate | không rewrite mù |
| SharedPreferences | DataStore cho structured settings | migrate theo contract |
| XML-only | Compose/hybrid | XML vẫn supported |
| kapt | KSP khi processor hỗ trợ | migrate per dependency |

Modern stack không tự động tạo architecture tốt. Migration cần test/telemetry và benefit cụ thể.
<!-- merge: preserve both canonical variants -->
`LiveData` vẫn hợp lệ và phổ biến trong app cũ; app Kotlin/Compose mới thường dùng Flow/StateFlow. `AsyncTask` deprecated và nên thay bằng coroutine/WorkManager **theo lifetime**, không phải replacement một-một. `startActivityForResult`/`onActivityResult` nên thay bằng Activity Result API. `SharedPreferences` không bị “cấm”, nhưng DataStore thường là lựa chọn mới tốt hơn. XML/View system không deprecated; Compose chỉ là hướng UI hiện đại được ưu tiên.
<!-- end merged variant -->

# 27. Project architecture mẫu

```văn bản (text / 텍스트)
app/
├─ ui/
│  ├─ home/
│  │  ├─ HomeRoute.kt
│  │  ├─ HomeScreen.kt
│  │  ├─ HomeViewModel.kt
│  │  └─ HomeUiState.kt
│  └─ điều hướng (navigation / 내비게이션)/
├─ lĩnh vực (domain / 도메인)/              # optional
│  ├─ mô hình (model / 모델)/
│  └─ usecase/
├─ dữ liệu (data / 데이터)/
│  ├─ repository/
│  ├─ remote/
│  └─ cục bộ (local / 로컬)/
└─ di/
```

Folder structure không phải architecture. Dependency direction/source of truth/state ownership mới là architecture.

# 28. Serialization và DTO boundary

<!-- merge: preserve both canonical variants -->
Transport DTO phản ánh wire schema; domain model phản ánh nghiệp vụ.
<!-- merge: preserve both canonical variants -->
## Intermediate Senior Notes

Một Android developer ở mức intermediate nên nhìn app như một hệ thống **state + side effect + lifetime + ordering** chứ không phải collection các callback.

Với mỗi state/operation, hãy trả lời:

```văn bản (text / 텍스트)
đơn vị sở hữu (owner / 오너) là ai?
sống qua recomposition không?
sống qua cấu hình (configuration / 구성) thay đổi (change / 변경) không?
sống qua tiến trình (process / 프로세스) death không?
thao tác (operation / 연산) có thể overlap không?
kết quả (result / 결과) cũ có thể tới sau kết quả (result / 결과) mới không?
cancellation có nghĩa gì?
collector dừng thì producer có tiếp tục không?
trạng thái (state / 상태) authoritative nằm ở đâu?
```

Coroutine phải có scope owner; Flow phải có sharing/lifecycle semantics; repository phải có source-of-truth policy; UI không được trực tiếp biết chi tiết storage/network nếu không có lý do rõ ràng. Khi các câu này rõ, framework choice thường trở nên đơn giản hơn.

---

# 28. Serialization, DTO và boundary giữa network/domain

Network payload thường là JSON, nhưng object nhận từ server không nên mặc định trở thành domain model dùng khắp ứng dụng. DTO (**Data Transfer Object**) phản ánh contract transport; domain model phản ánh ý nghĩa nghiệp vụ. Tách hai loại này cho phép backend thay field, nullable hoặc naming mà không làm domain layer bị phụ thuộc trực tiếp.
<!-- end merged variant -->

```kotlin
@Serializable
dữ liệu (data / 데이터) lớp (class / 클래스) UserDto(
    val id: Long,
    val display_name: String? = null
)
```

Unknown field, missing field, new enum value và null bất ngờ là tình huống bình thường khi client/server release độc lập. Parser/model cần forward-compatible ở nơi phù hợp.

# 29. Parcelable, Bundle và component boundary

Bundle/Intent chỉ nên mang dữ liệu nhỏ. `@Parcelize` giúp generate Parcelable nhưng không phải lý do truyền object graph lớn.

```kotlin
@Parcelize
dữ liệu (data / 데이터) lớp (class / 클래스) UserArgs(val userId: Long) : Parcelable
```

Stable ID + repository reconstruction bền hơn object snapshot stale.

# 30. Files, MediaStore và scoped storage

Android storage có internal/cache/shared-media/document-provider với lifetime/permission khác nhau. Với `content://`, dùng `ContentResolver`; đừng cố ép mọi URI thành filesystem path.

Photo Picker/SAF giúp giảm broad storage permission khi user chủ động chọn tài liệu/media.

# 31. Notification và foreground work

Notification channel, runtime notification permission và foreground-service policy thay đổi theo Android generation. Foreground Service không phải cách lách background restriction.

Chọn primitive theo lifetime/guarantee, không theo thói quen.

# 32. Deep link và App Link

Custom scheme dễ conflict. App Links dùng HTTPS + verification. External route phải validate input và authorization; deep link không phải quyền truy cập.

# 33. Build variants, release/debug và BuildConfig

Build type (`debug`/`release`) và product flavor tạo variants. Quá nhiều dimensions làm CI/test matrix nổ theo tích tổ hợp.

**Debug chạy không chứng minh release chạy.** Release có thể khác vì:

```văn bản (text / 텍스트)
R8/obfuscation/tài nguyên (resource / 자원) shrinking
manifest merge
BuildConfig/env
signing
môi trường vận hành (production / 운영 환경) endpoint
tính năng (feature / 기능) flags
```

CI nên build ít nhất release/minified variant quan trọng. Secret không trở nên an toàn vì nằm trong BuildConfig.

# 34. Coroutine/Flow testing có kiểm soát thời gian

Dùng `runTest`/TestDispatcher thay `Thread.sleep()`.

```kotlin
@kiểm thử (test / 테스트)
fun loadUser_updatesState() = runTest {
    val vm = UserViewModel(fakeRepo)
    vm.tải (load / 로드)()
    advanceUntilIdle()
    assertEquals("An", vm.uiState.value.name)
}
```

Với race/latest-wins, fake repository có thể cho phép test điều khiển thứ tự completion thay vì dựa timing ngẫu nhiên.

<!-- merge: preserve both canonical variants -->
# 35. Process death như test case thiết kế

ViewModel sống qua configuration change nhưng không sống qua process death. Phân loại state:

```văn bản (text / 텍스트)
reloadable dữ liệu (data / 데이터) → repository/nguồn chuẩn (source of truth / 정본)
small reconstruct key → SavedStateHandle/rememberSaveable
durable nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터) → DB/DataStore/máy chủ (server / 서버)
```
<!-- merge: preserve both canonical variants -->
Đối với `stateIn(WhileSubscribed(...))`, test cần có collector nếu muốn upstream chạy. Đây là lỗi test phổ biến: assert StateFlow nhưng không tạo subscription, trong khi sharing policy cố ý chưa start upstream.

# 35. Process death như một test case thiết kế

Configuration change và process death không giống nhau. ViewModel giúp sống qua recreation trong cùng process nhưng không tồn tại sau khi process bị kill.

Hãy phân loại state theo lifetime:

```văn bản (text / 텍스트)
Derived/reloadable dữ liệu (data / 데이터)
→ reconstruct từ repository/nguồn chuẩn (source of truth / 정본)

Small điều hướng (navigation / 내비게이션)/form trạng thái (state / 상태)
→ SavedStateHandle hoặc rememberSaveable nếu phù hợp

Durable nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터)
→ cơ sở dữ liệu (database / 데이터베이스)/DataStore/máy chủ (server / 서버)

Transient animation/scroll detail
→ chỉ save nếu UX thực sự yêu cầu
```

`SavedStateHandle` không phải database. Nhét object graph lớn vào saved state tạo serialization/Binder cost và khiến state cũ trở thành source of truth ngoài ý muốn.

Một screen production nên có reconstruction recipe:

```văn bản (text / 텍스트)
stable tuyến (route / 경로) ID
+ small saved người dùng (user / 사용자) đầu vào (input / 입력)
+ repository persisted dữ liệu (data / 데이터)
→ rebuild UiState
```

Test process death nên kiểm tra recipe này thay vì chỉ rotate screen. Configuration change có thể giữ ViewModel; process recreation thì không.
<!-- end merged variant -->

Nếu screen chỉ restore được bằng cách save toàn object graph vào Bundle, architecture có thể đang thiếu stable identity/source of truth.

<!-- merge: preserve both canonical variants -->
# 36. Intermediate integration project

Một project kết thúc Intermediate nên chứng minh được flow:

```văn bản (text / 텍스트)
UI hành động (action / 동작)
→ ViewModel
→ repository
→ mạng (network / 네트워크)/Room
→ source-of-truth cập nhật (update / 업데이트)
→ luồng (flow / 흐름)/StateFlow
→ lifecycle-aware UI kết xuất (render / 렌더링)
```

Ngoài happy path phải có offline với cache, refresh failure, process recreation bằng stable ID, validation/auth error, retry policy rõ, release variant build và DB/serialization integration test.

# 37. State lifetime matrix

Một trong những kỹ năng quan trọng nhất trước khi sang Senior là đặt state vào đúng owner.

| State | Lifetime mong muốn | Nơi phù hợp |
|---|---|---|
| animation/local toggle tạm | composition | `remember` |
| input nhỏ cần survive recreation | saved-state | `rememberSaveable` / `SavedStateHandle` |
| screen UI state | ViewModel | `StateFlow`/state holder |
| entity/cache lớn | process-independent | Room/file |
| user preference | durable | DataStore |
| authoritative business data | tùy domain | DB/server/source of truth |

Sai lầm phổ biến là nghĩ “ViewModel giữ được state” nên đặt mọi thứ trong ViewModel. ViewModel chỉ kéo dài qua configuration change; process death vẫn xóa toàn bộ memory.

Một câu hỏi thực tế:

```văn bản (text / 텍스트)
Nếu Android kill tiến trình (process / 프로세스) ngay bây giờ,
trạng thái (state / 상태) nào phải tự khôi phục và trạng thái (state / 상태) nào được phép mất?
```

Nếu không trả lời được, state model chưa hoàn chỉnh.

# 38. Stale-result race và ordering

Ví dụ user gõ search nhanh:

```văn bản (text / 텍스트)
truy vấn (query / 쿼리) = "a"  → yêu cầu (request / 요청) A
truy vấn (query / 쿼리) = "ab" → yêu cầu (request / 요청) B
B trả trước
A trả sau
```

Nếu ViewModel set state theo callback completion, A có thể overwrite kết quả mới hơn của B.

Một hướng giải quyết ở Flow:

```kotlin
val results = truy vấn (query / 쿼리)
    .debounce(300)
    .distinctUntilChanged()
    .flatMapLatest { repository.tìm kiếm (search / 검색)(it) }
```

`flatMapLatest` cancel flow cũ khi query mới tới. Nếu API không cancellable hoặc callback boundary không cooperate, vẫn có thể dùng request-generation token để reject stale response.

Điểm cốt lõi: concurrency bug thường là **ordering bug**, không phải “thiếu thread”.

# 39. Repository implementation end-to-end

Một repository offline-readable có thể có structure:

```kotlin
lớp (class / 클래스) OfflineFirstUserRepository(
    private val api: UserApi,
    private val dao: UserDao,
    private val ioDispatcher: CoroutineDispatcher
) : UserRepository {

    override fun observeUsers(): luồng (flow / 흐름)<danh sách (list / 목록)<người dùng (user / 사용자)>> =
        dao.observeAll()
            .map { rows -> rows.map(UserEntity::toDomain) }

    override suspend fun refresh() = withContext(ioDispatcher) {
        val remote = api.getUsers()
        val entities = remote.map(UserDto::toEntity)
        dao.replaceRemoteSnapshot(entities)
    }
}
```

Đây không phải template bắt buộc. Điều cần hiểu là read path và refresh path tách nhau:

```văn bản (text / 텍스트)
read = observe nguồn chuẩn (source of truth / 정본)
refresh = fetch bên ngoài (external / 외부) nguồn (source / 소스) rồi cập nhật (update / 업데이트) nguồn chuẩn (source of truth / 정본)
```

Nếu UI observe network response trực tiếp trong khi Room cũng emit cùng entity, bạn có hai nguồn state cạnh tranh.

## 39.1 Mapper tồn tại để bảo vệ boundary

```văn bản (text / 텍스트)
DTO
→ vận chuyển (transport / 전송) đặc tả hợp đồng (contract / 계약)

Thực thể (entity / 엔터티)
→ cục bộ (local / 로컬) lược đồ (schema / 스키마)

Lĩnh vực (domain / 도메인)
→ ứng dụng (application / 애플리케이션) meaning

UiModel
→ presentation need
```

Không bắt buộc luôn có bốn class. Tách khi hai representation có lý do thay đổi khác nhau. Over-modeling cũng là cost.

# 40. Retry, idempotency và ambiguous outcome

Giả sử app gửi:

```http
POST /orders
```

Server tạo order thành công nhưng response bị mất vì network timeout. Client nhìn thấy timeout nhưng không biết server đã commit chưa. Nếu retry mù, có thể tạo hai order.

Đây là **ambiguous outcome**.

Một protocol tốt có thể dùng idempotency key:

```văn bản (text / 텍스트)
operationId = UUID
máy khách (client / 클라이언트) gửi operationId cùng yêu cầu (request / 요청)
máy chủ (server / 서버) lưu kết quả theo operationId
thử lại (retry / 재시도) cùng operationId trả lại cùng logical kết quả (result / 결과)
```

Intermediate developer chưa cần xây distributed sync engine, nhưng cần hiểu vì sao `catch IOException -> retry()` không an toàn cho mọi mutation.

Retry classification cơ bản:

```văn bản (text / 텍스트)
DNS/offline/transient 5xx → có thể thử lại (retry / 재시도) tùy chính sách (policy / 정책)
401 → session khôi phục (recovery / 복구), không thử lại (retry / 재시도) vô hạn
kiểm tra hợp lệ (validation / 검증) 4xx → không thử lại (retry / 재시도) tự động
xung đột (conflict / 충돌) → cần nghiệp vụ (business / 비즈니스) resolution
unknown hết thời gian chờ (timeout / 타임아웃) after mutation → cần idempotency/reconciliation
```

# 41. Debug vs release: cách điều tra khác biệt artifact

Nếu debug chạy nhưng release fail, không nên tiếp tục debug source giống nhau rồi kết luận “Android ngẫu nhiên”. Hãy so sánh artifact path.

Checklist:

```văn bản (text / 텍스트)
R8 có strip/rename lớp (class / 클래스) không?
bên tiêu thụ (consumer / 소비자) ProGuard rules có đủ không?
reflection/serialization có phụ thuộc tên lớp (class / 클래스) không?
manifest merge khác không?
tài nguyên (resource / 자원) shrink có xóa tài nguyên (resource / 자원) được lookup động không?
BuildConfig/cơ sở (base / 기반) URL/cờ tính năng (feature flag / 기능 플래그) khác không?
signing/certificate-dependent API có khác không?
prod backend lược đồ (schema / 스키마) có khác staging không?
```

Release bug thường là build/configuration/boundary bug hơn là UI syntax bug.

# 42. Migration scenario: legacy → modern theo từng seam

Giả sử app cũ dùng:

```văn bản (text / 텍스트)
Fragment XML
LiveData
RxJava repository
SharedPreferences
startActivityForResult
```

Không cần rewrite toàn bộ cùng lúc.

Một migration an toàn hơn:

```văn bản (text / 텍스트)
1. thêm characterization tests cho luồng (flow / 흐름) quan trọng
2. đổi Activity kết quả (result / 결과) API độc lập
3. adapter Rx observable → luồng (flow / 흐름) ở ranh giới (boundary / 경계) mới
4. màn hình mới dùng StateFlow/ViewModel
5. migrate settings mới sang DataStore + di chuyển (migration / 마이그레이션) cũ
6. nhúng Compose ở leaf screen nếu có benefit
7. theo dõi crash/hiệu năng (performance / 성능)
8. xóa đường dẫn (path / 경로) cũ sau khi không còn caller
```

Điểm mạnh của seam-based migration là mỗi bước có thể review/rollback riêng.

# 43. Debugging playbook theo layer

Khi app “không hoạt động”, đừng sửa ngẫu nhiên. Xác định layer.

```văn bản (text / 텍스트)
UI không cập nhật (update / 업데이트)
→ trạng thái (state / 상태) có đổi không?
→ collector có active vòng đời (lifecycle / 생명주기) không?
→ Compose có đọc đúng observable trạng thái (state / 상태) không?

Dữ liệu (data / 데이터) không đúng
→ repository nguồn chuẩn (source of truth / 정본) là gì?
→ mapper có mất trường dữ liệu (field / 필드)/null không?
→ DB giao dịch (transaction / 트랜잭션) có lần ghi nhận (commit / 커밋) không?

Yêu cầu (request / 요청) thất bại (fail / 실패)
→ vận chuyển (transport / 전송)/giao thức (protocol / 프로토콜)/auth/lĩnh vực (domain / 도메인) lỗi (error / 오류) loại nào?
→ endpoint/variant/cấu hình (config / 설정) đúng không?

Chỉ bản phát hành (release / 릴리스) thất bại (fail / 실패)
→ R8/signing/manifest/tài nguyên (resource / 자원)/cấu hình (config / 설정)

Sau rotate/tiến trình (process / 프로세스) recreation thất bại (fail / 실패)
→ trạng thái (state / 상태) đơn vị sở hữu (owner / 오너)/saved-state/source-of-truth
```

Debug tốt là thu evidence ở đúng boundary: log có correlation/context, DB inspector, network trace, profiler, stack trace và test tái hiện.

# 44. Intermediate completion checklist

Trước khi sang Advanced/Senior, bạn nên tự giải thích được mà không nhìn tài liệu:

```văn bản (text / 텍스트)
suspend khác luồng thực thi (thread / 스레드) thế nào?
structured tính đồng thời (concurrency / 동시성) bảo vệ thời gian tồn tại (lifetime / 수명) ra sao?
luồng (flow / 흐름) cold khác StateFlow hot thế nào?
SharedFlow/sự kiện (event / 이벤트) có thể mất hoặc replay ra sao?
ViewModel sống qua gì và không sống qua gì?
remember / rememberSaveable / SavedStateHandle / Room khác thời gian tồn tại (lifetime / 수명) nào?
repository có nhiệm vụ gì ngoài gọi API?
nguồn chuẩn (source of truth / 정본) là gì?
DTO/thực thể (entity / 엔터티)/lĩnh vực (domain / 도메인)/UI mô hình (model / 모델) tách khi nào?
thử lại (retry / 재시도) mutation vì sao có thể nguy hiểm?
WorkManager khác coroutine/dịch vụ (service / 서비스) thế nào?
XML/LiveData/RxJava là legacy hay vẫn valid trong trường hợp nào?
gỡ lỗi (debug / 디버그) chạy nhưng bản phát hành (release / 릴리스) thất bại (fail / 실패) thì kiểm tra gì?
```

Nếu các câu trả lời đều dựa trên **owner, lifetime, state, failure và compatibility** thay vì chỉ tên framework, bạn đã sẵn sàng cho level Advanced/Senior.
<!-- merge: preserve both canonical variants -->
Một project kết thúc Intermediate nên có ít nhất một flow từ UI → ViewModel → Repository → local/network data source; UI state expose bằng StateFlow; Room làm local persistence; network layer map DTO sang domain; navigation có typed/validated argument; DI rõ ràng; coroutine có lifecycle owner; loading/error/empty/success state được model; unit test cho ViewModel/repository và ít nhất một integration test cho DB hoặc serialization.

Ngoài happy path, project nên chứng minh được ít nhất các case: rotate/recreate screen không mất state cần thiết; process death có thể reconstruct bằng stable ID/source of truth; search/query mới không bị result cũ overwrite; collector dừng khi UI không active; cancellation không bị convert thành generic error; release behavior không phụ thuộc `GlobalScope` hay ad-hoc thời gian tồn tại (lifetime / 수명).
<!-- end merged variant -->

> **Bàn giao:** Sau **11.2 Lĩnh vực (domain / 도메인) tầng (layer / 계층) là optional**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 kotlin beginner](./01_kotlin_beginner.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
