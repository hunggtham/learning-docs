# Kotlin + Android Master Note — Intermediate

> Mục tiêu: chuyển từ “viết được app” sang “xây app có cấu trúc đúng”, hiểu coroutine/Flow, ViewModel, source of truth, Room/networking, lifecycle, testing, DI, migration và các failure mode cơ bản trước khi sang Senior. Ở level này, mỗi API phải được đặt vào đúng **owner, lifetime và data flow**.

## Mục lục

1. Kotlin idioms quan trọng
2. Scope functions
3. Extension function/property
4. Generics và variance
5. Object, companion object, singleton
6. Delegation và delegated properties
7. Sequences
8. Coroutine nền tảng
9. Structured concurrency
10. Flow, StateFlow, SharedFlow
11. Android app architecture
12. ViewModel và UI State
13. Repository, data source và source of truth
14. Room
15. Networking
16. Dependency Injection
17. Navigation nâng cao
18. Compose state/effect
19. XML interoperability
20. Lifecycle-aware collection
21. WorkManager
22. DataStore
23. Testing
24. Error handling và retry
25. Security/configuration căn bản
26. Modern vs legacy migration notes
27. Project architecture mẫu
28. Serialization và DTO boundary
29. Parcelable, Bundle và component boundary
30. Files, MediaStore và scoped storage
31. Notification và foreground work
32. Deep link và App Link
33. Build variants, release/debug và BuildConfig
34. Coroutine/Flow testing có kiểm soát thời gian
35. Process death như test case thiết kế
36. Intermediate integration project
37. State lifetime matrix
38. Stale-result race và ordering
39. Repository implementation end-to-end
40. Retry, idempotency và ambiguous outcome
41. Debug vs release: cách điều tra khác biệt artifact
42. Migration scenario: legacy → modern theo từng seam
43. Debugging playbook theo layer
44. Intermediate completion checklist

---

# 1. Kotlin idioms quan trọng

Kotlin không chỉ là Java viết ngắn hơn. Idiomatic Kotlin ưu tiên immutable value, expression, extension, sealed hierarchy và higher-order function khi chúng làm intent rõ hơn.

```kotlin
user?.let(::send)
```

Không chain scope function chỉ để giảm số dòng. Code rõ ràng bằng `if` hoặc local variable thường tốt hơn một chain khó đọc.

# 2. Scope functions: `let`, `run`, `with`, `apply`, `also`

| Function | Receiver | Trả về | Dùng tốt khi |
|---|---|---|---|
| `let` | `it` | lambda result | null-chain, transform |
| `run` | `this` | lambda result | configure + compute |
| `with(x)` | `this` | lambda result | nhóm nhiều call |
| `apply` | `this` | receiver | configure object |
| `also` | `it` | receiver | log/side effect nhỏ |

Ví dụ `apply` để cấu hình object:

```kotlin
val request = Request.Builder().apply {
    url(baseUrl)
    header("Accept", "application/json")
}.build()
```

Ví dụ `let` để transform nullable value:

```kotlin
val userId: Long? = rawId?.toLongOrNull()
val profile = userId?.let(repository::findProfile)
```

Nested `let/apply/run` dễ làm mất ngữ nghĩa `this`/`it`; hãy đặt tên lambda parameter hoặc tách block.

# 3. Extension function và property

Extension được resolve statically theo declared type, không phải virtual dispatch. Nó phù hợp thêm convenience/API adapter, không thay polymorphism runtime.

```kotlin
fun String.toUserIdOrNull(): UserId? =
    toLongOrNull()?.let(::UserId)
```

Extension hữu ích để đặt mapping gần boundary, nhưng đừng tạo “utility namespace vô hình” với hàng trăm extension không discoverable.

# 4. Generics và variance

`out T` cho producer, `in T` cho consumer. Star projection `Foo<*>` hữu ích khi chưa biết type argument nhưng vẫn muốn thao tác trong giới hạn an toàn.

```kotlin
interface Producer<out T> {
    fun produce(): T
}

interface Consumer<in T> {
    fun consume(value: T)
}
```

Variance giúp API linh hoạt nhưng cần giữ type contract dễ hiểu; nếu signature đầy projection phức tạp, abstraction có thể đang quá generic.

# 5. `object`, `companion object` và singleton

`object` tạo singleton theo class-loading semantics.

```kotlin
object AppClock {
    fun now(): Instant = Instant.now()
}
```

Không biến mọi service thành global singleton; stateful singleton làm testing/lifetime khó hơn. DI thường quản lý lifecycle rõ hơn. `companion object` phù hợp factory/constant gắn class nhưng không phải Java `static` hoàn toàn tương đương ở bytecode/API shape.

# 6. Delegation và delegated properties

Class delegation và property delegate giảm boilerplate khi semantics đúng. `lazy`, Compose state delegation và custom ViewBinding delegate là ví dụ phổ biến.

```kotlin
val parser by lazy { ExpensiveParser() }
```

`lazy` cũng có lifetime của object owner; nếu owner là singleton thì lazy value cũng gần như process-lifetime. Đừng dùng `lazy` để che dependency/global state.

# 7. Sequences

`Sequence` lazy và có thể giảm intermediate collection với pipeline dài/short-circuit.

```kotlin
val result = source
    .asSequence()
    .map(::normalize)
    .filter(::isValid)
    .take(20)
    .toList()
```

Collection nhỏ/chain ngắn không mặc định nhanh hơn; performance cần đo.

# 8. Coroutine nền tảng

<!-- merge: preserve both canonical variants -->
Coroutine không đồng nghĩa thread. `suspend` chỉ nói function có thể suspend; nó không đảm bảo function chạy background.

```kotlin
suspend fun loadUser(): User = api.loadUser()
```

Builder chính:

```kotlin
scope.launch { ... }       // Job
scope.async { ... }        // Deferred<T>
withContext(dispatcher) { ... }
```

`launch` cho work không trả value trực tiếp; `async` cho concurrent computation cần `await`. Suspend API của data layer nên **main-safe**: nếu implementation dùng blocking I/O, chính layer đó chịu trách nhiệm đổi dispatcher.

```kotlin
suspend fun parseLargeFile(file: File): Model = withContext(ioDispatcher) {
    parser.parse(file)
}
```

# 9. Structured concurrency

Coroutine con sống trong scope cha. Điều này tạo ownership và cancellation có cấu trúc.
<!-- merge: preserve both canonical variants -->
Coroutine là một computation có **lifetime, cancellation và execution context**, không phải “thread nhẹ” theo nghĩa mỗi coroutine tương ứng một thread riêng. Coroutine có thể suspend mà không block thread, rồi resume sau đó theo dispatcher/context. Nhưng `suspend` **không tự động biến blocking code thành non-blocking**: nếu gọi JDBC/file/network API blocking bên trong suspend function trên Main, main thread vẫn bị block.

```kotlin
suspend fun loadUser(): User {
    delay(100) // suspend, không giữ thread trong lúc chờ
    return User(...)
}
```

## 8.1 Scope là owner của lifetime

Mỗi coroutine phải trả lời được “ai chịu trách nhiệm cancel nó?”. Android có vài scope phổ biến:

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

Nếu tạo `CoroutineScope(SupervisorJob() + Dispatchers.IO)` tùy ý trong repository mà không có owner/shutdown policy, ta đã tạo lifetime ẩn.

## 8.2 `launch`, `async`, `withContext` khác nhau về contract

```kotlin
scope.launch { ... }       // Job, side-effect/lifecycle work
scope.async { ... }        // Deferred<T>, concurrent result
withContext(dispatcher) { ... } // chuyển context và chờ kết quả
```

`async` chỉ hữu ích khi có **concurrency có chủ đích**. Viết:

```kotlin
val value = async { repository.load() }.await()
```

mà không chạy song song với gì thường chỉ thêm `Deferred` không cần thiết.

`withContext` không tạo “background job độc lập”; caller chờ block đó hoàn tất và cancellation vẫn nằm trong structured scope.

## 8.3 Main-safety là contract của lower layer

Suspend function ở repository/use case nên đủ main-safe để caller không phải nhớ dispatcher implementation detail.

```kotlin
class FileRepository(
    private val ioDispatcher: CoroutineDispatcher
) {
    suspend fun readLargeFile(): Data = withContext(ioDispatcher) {
        blockingParser.read()
    }
}
```

Nếu mỗi ViewModel phải nhớ method nào cần `Dispatchers.IO`, threading policy đã leak lên UI layer.

## 8.4 Cancellation là cooperative

Cancellation không “giết thread”. Coroutine dừng tại suspension point hoặc khi code chủ động kiểm tra cancellation.

CPU loop dài nên có checkpoint khi phù hợp:

```kotlin
while (hasMoreWork()) {
    ensureActive()
    processChunk()
}
```

Cleanup thường đặt trong `finally`. Không dùng `NonCancellable` cho toàn operation; chỉ cân nhắc vùng cleanup ngắn thật sự phải hoàn thành.

```kotlin
try {
    repository.sync()
} finally {
    releaseResource()
}
```

Không swallow `CancellationException` thành domain error thông thường. Cancellation thường là control signal cho lifetime, không phải “network failed”.

# 9. Structured concurrency

Structured concurrency nghĩa coroutine tạo ra một **Job tree** có parent-child relationship rõ ràng. Parent không được xem là hoàn tất trong khi child còn chạy; cancellation và failure đi theo rule của tree thay vì coroutine “bay tự do”.
<!-- end merged variant -->

```kotlin
suspend fun loadPage(): Page = coroutineScope {
    val user = async { userRepo.load() }
    val posts = async { postRepo.load() }
    Page(user.await(), posts.await())
}
```

<!-- merge: preserve both canonical variants -->
Chỉ parallel khi hai operation độc lập. `supervisorScope` phù hợp khi sibling failure độc lập; nó không tự xử lý error.

Tránh `GlobalScope`. Hỏi: **ai sở hữu coroutine và khi owner chết thì work có nên tiếp tục không?**

# 10. Flow, StateFlow và SharedFlow

`Flow<T>` thường cold: upstream chạy khi collect. `StateFlow` là hot state holder có current value. `SharedFlow` là hot broadcast stream với replay/buffer cấu hình được.
<!-- merge: preserve both canonical variants -->
Ở đây `user` và `posts` thực sự chạy concurrent. Nếu một child fail trong `coroutineScope`, sibling còn lại thường bị cancel vì kết quả `Page` không còn tạo được đầy đủ.

`supervisorScope` dùng khi failure của một child không nên tự động cancel sibling:

```kotlin
supervisorScope {
    launch { refreshAvatar() }
    launch { refreshRecommendations() }
}
```

Nhưng supervision không có nghĩa “bỏ qua exception”. Mỗi failure vẫn cần owner và error policy.

## 9.1 Concurrency không đồng nghĩa parallelism

Hai coroutine có thể concurrent nhưng chạy trên cùng thread theo thời gian xen kẽ. Parallelism chỉ xảy ra khi runtime/dispatcher cho phép chạy thật sự đồng thời trên nhiều thread/core.

Điều cần thiết kế là:

```text
operation nào có thể overlap?
operation nào phải serialize?
operation cũ có được overwrite result mới không?
bao nhiêu request cùng lúc là hợp lý?
```

## 9.2 Duplicate action và stale result là bug concurrency rất phổ biến

Ví dụ user đổi search query nhanh:

```text
request A(query="ko") bắt đầu
request B(query="kotlin") bắt đầu sau
B trả về trước → UI đúng
A trả về sau → nếu update state vô điều kiện, UI bị quay về result cũ
```

Giải pháp có thể là `flatMapLatest`, cancel job cũ, generation/version token hoặc repository contract khác. Mutex không tự giải quyết stale-result semantic.

Tránh `GlobalScope` trong application code. Scope phải có owner. Nếu operation cần sống qua screen navigation hoặc process scheduling, hãy chọn owner/primitive đúng thay vì cố kéo dài một coroutine UI.

# 10. Flow, StateFlow và SharedFlow

`Flow<T>` biểu diễn chuỗi giá trị theo thời gian. Cold Flow thường chỉ chạy upstream khi có collector.

```kotlin
fun observeUsers(): Flow<List<User>> = dao.observeUsers()
```

Một cold Flow không phải “background task tự chạy”. Nếu không collect, phần lớn upstream cold flow không thực thi.

## 10.1 Operator là semantic, không chỉ syntax chain

```kotlin
flow
    .map { ... }
    .filter { ... }
    .distinctUntilChanged()
    .debounce(300)
    .catch { ... }
    .combine(other) { a, b -> ... }
```

`combine` giữ latest value từ nhiều stream; `zip` ghép theo cặp emission; `debounce` đợi khoảng yên; `distinctUntilChanged` bỏ emission lặp theo equality. Chọn operator sai có thể tạo bug ordering chứ không chỉ khác performance.

`flatMapLatest` rất hữu ích cho search/query mà request mới phải làm result cũ hết hiệu lực:

```kotlin
query
    .debounce(300)
    .flatMapLatest(repository::search)
```

## 10.2 Flow context và `flowOn`

Flow giữ context preservation. `flowOn(dispatcher)` thay context của **upstream trước nó**, không đơn giản là “mọi thứ sau đây chạy IO”. Collector vẫn chạy trong context nơi collect trừ khi boundary khác thay đổi.

```kotlin
flow {
    emit(loadBlocking())
}
    .flowOn(ioDispatcher)
    .map(::toUiModel)
```

Hiểu upstream/downstream quan trọng khi debug thread, cancellation và performance.

## 10.3 Backpressure: producer nhanh hơn consumer

Không phải mọi emission đều cần render. Các tool có semantic khác nhau:

```text
buffer
= cho producer và consumer overlap với buffer

conflate
= bỏ intermediate value khi consumer chậm, giữ latest direction

collectLatest
= cancel xử lý value cũ khi value mới tới
```

Không dùng `conflate` cho event mà từng item đều phải xử lý, ví dụ transaction mutation queue.

## 10.4 `StateFlow` là state holder

`StateFlow` là hot, có current value và phù hợp state có thể đọc ở bất kỳ thời điểm nào.
<!-- end merged variant -->

```kotlin
private val _uiState = MutableStateFlow(UiState())
val uiState: StateFlow<UiState> = _uiState.asStateFlow()
```

<!-- merge: preserve both canonical variants -->
Không chọn SharedFlow chỉ vì “event”. Trước hết hỏi event có cần survive collector inactive/recreation không. Nếu câu trả lời có, có thể đó là durable state chứ không phải one-off event.

Các operator như `debounce`, `combine`, `distinctUntilChanged`, `flatMapLatest` cần dùng theo semantics. `flatMapLatest` hợp search latest-wins nhưng không hợp audit stream nơi mọi item phải xử lý.
<!-- merge: preserve both canonical variants -->
UI state nên immutable từ bên ngoài; ViewModel là owner mutation.

`StateFlow` conflates theo equality/value update semantics; collector chậm không có nghĩa được nhận mọi intermediate snapshot. Đây thường đúng với state vì UI quan tâm latest truth.

## 10.5 `SharedFlow` là shared stream, không mặc định là “event solution”

`SharedFlow` có thể cấu hình replay/buffer và share emission cho nhiều collector. Nó hữu ích cho shared upstream hoặc event stream thực sự.

Nhưng các event có business meaning lâu dài nên thường model thành state/durable data thay vì phát một tín hiệu có thể mất khi UI không collect. Ví dụ “payment completed” là domain state; snackbar “Copied” có thể transient.

## 10.6 `stateIn` và `shareIn`

Cold Flow có thể được convert thành hot shared stream trong scope rõ ràng:

```kotlin
val uiState = repository.observeUsers()
    .map(::toUiState)
    .stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(5_000),
        initialValue = UiState.Loading
    )
```

`SharingStarted` quyết định upstream sống khi nào. Đây là **lifetime decision**, không chỉ optimization. `Eagerly`, `Lazily`, `WhileSubscribed` có trade-off khác nhau về freshness, resource và restart.
<!-- end merged variant -->

# 11. Android app architecture

Architecture hiện đại tối thiểu có UI layer và data layer; domain layer optional.

```text
UI
→ ViewModel / state holder
→ UseCase (optional)
→ Repository
→ local/remote/platform data source
```

Điểm quan trọng không phải số layer mà là **dependency direction** và **ownership**.

UI không gọi Retrofit/Room trực tiếp vì UI không nên biết policy cache/retry/sync. Repository không biết Button/NavController vì data layer không nên phụ thuộc presentation.

## 11.1 Architecture bắt đầu từ state

Trước khi tạo class, phân loại state:

```text
UI ephemeral state
screen state
business/application data
persisted data
server truth
```

Ví dụ search text nhỏ có thể ở ViewModel/SavedStateHandle; danh sách article không nên bị nhét vào saved state nếu có thể reload từ Room.

## 11.2 Domain layer là optional

Use case có giá trị khi operation chứa policy/business rule/reuse. Nếu `GetUserUseCase` chỉ gọi một dòng `repository.getUser()`, thêm layer có thể chỉ tăng navigation cost.

# 12. ViewModel và UI State

<!-- merge: preserve both canonical variants -->
ViewModel là screen-level state holder/orchestrator, không phải nơi chứa toàn bộ networking, SQL và service locator.
<!-- merge: preserve both canonical variants -->
ViewModel là state holder ở screen/navigation scope, không phải nơi “mọi logic Android” phải chuyển vào. Nó thường nhận event, gọi domain/data operation và expose state cho UI.
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

Phân biệt initial load và refresh giúp UI giữ cached content thay vì thay toàn màn hình bằng spinner.
<!-- merge: preserve both canonical variants -->

class UserViewModel(
    private val repository: UserRepository
) : ViewModel() {
    private val _uiState = MutableStateFlow(UserUiState())
    val uiState = _uiState.asStateFlow()

    fun refresh() {
        viewModelScope.launch {
            _uiState.update { it.copy(loading = true, errorMessage = null) }
            try {
                repository.refresh()
            } catch (e: CancellationException) {
                throw e
            } catch (e: Throwable) {
                _uiState.update { it.copy(errorMessage = e.message) }
            } finally {
                _uiState.update { it.copy(loading = false) }
            }
        }
    }
}
```

## 12.1 State ownership trước API choice

Trước khi chọn `remember`, `StateFlow` hay SavedStateHandle, hỏi state phải sống bao lâu.

```text
chỉ trong một recomposition tree
→ remember

qua configuration recreation cho UI value nhỏ
→ rememberSaveable hoặc SavedStateHandle tùy owner

screen state/business interaction trong cùng process
→ ViewModel + StateFlow thường phù hợp

qua process death
→ reconstruct từ SavedStateHandle nhỏ + repository/database/server

durable business data
→ database/DataStore/server, không dựa vào ViewModel
```

ViewModel sống qua configuration change nhưng **không sống qua process death**.

## 12.2 Authoritative state và derived state

Không lưu cùng một fact thành nhiều mutable source nếu có thể derive.

Sai hướng:

```text
repository có users
ViewModel copy users vào mutable list riêng
Composable lại copy vào remember list khác
```

Ba source có thể lệch nhau.

Tốt hơn là xác định source of truth, sau đó derive filter/sort/presentation state từ nó.

## 12.3 Impossible state và state machine

Nhiều boolean độc lập dễ tạo tổ hợp vô nghĩa:

```text
loading=true
contentVisible=true
fatalError=true
```

Có thể dùng sealed state cho mutually exclusive screen state hoặc giữ content + refresh/error metadata nếu UX cho phép content và refresh đồng thời. Không có một data class duy nhất đúng; state model phải phản ánh invariant UI.

## 12.4 Concurrency trong ViewModel

Hai `refresh()` cùng chạy có thể tạo duplicate request; request cũ trả sau có thể overwrite state mới; logout/account switch có thể để response từ session cũ quay lại UI.

Giải pháp tùy semantic:

```text
cancel previous job
single-flight
Mutex/serialization
flatMapLatest cho query-driven work
generation/session token để bỏ stale result
repository làm source of truth để UI không apply raw response trực tiếp
```

Không giải quyết race bằng cách thêm `loading` boolean nếu ordering vẫn không được định nghĩa.
<!-- end merged variant -->

ViewModel nhận action, gọi repository/use case, rồi expose state. Nó không giữ Activity/View context và không tạo Retrofit/Room trực tiếp.

# 13. Repository, data source và source of truth

Repository không chỉ là wrapper DAO/API. Nó trả lời:

```text
source nào authoritative?
khi nào refresh?
local và remote merge ra sao?
error nào propagate?
mutation có retry được không?
```

```kotlin
interface UserRepository {
    fun observeUsers(): Flow<List<User>>
    suspend fun refresh()
}
```

Offline/read-cache pattern phổ biến:

```text
Room emits cached data
→ UI render ngay
→ refresh network
→ validate/map DTO
→ transaction update Room
→ Room emits state mới
```

UI không cần biết data mới tới từ network hay DB.

# 14. Room

Room bọc SQLite bằng schema/DAO/compile-time validation.

```kotlin
@Entity(tableName = "users")
data class UserEntity(
    @PrimaryKey val id: Long,
    val name: String
)
```

```kotlin
@Dao
interface UserDao {
    @Query("SELECT * FROM users ORDER BY name")
    fun observeAll(): Flow<List<UserEntity>>

    @Upsert
    suspend fun upsertAll(items: List<UserEntity>)
}
```

Transaction bảo vệ invariant DB. Migration phải được test với schema/data cũ thật đại diện. `fallbackToDestructiveMigration` chỉ hợp dữ liệu disposable/cache nếu product chấp nhận mất data.

# 15. Networking

Retrofit/OkHttp hoặc Ktor client đều là implementation detail của transport layer.

DTO nên tách domain model:

```kotlin
data class UserDto(val id: Long, val name: String?)

fun UserDto.toDomain() = User(
    id = id,
    name = name.orEmpty()
)
```

Phân biệt ít nhất:

```text
transport error: offline, DNS, timeout
protocol error: HTTP status
serialization/schema error
auth/session error
domain/business error
```

Không để `HttpException`/Retrofit type chảy tới Composable nếu UI chỉ cần domain action/message.

# 16. Dependency Injection

DI là quản lý graph/lifetime. Manual DI, Hilt hay Koin đều chỉ là công cụ.

```kotlin
class UserRepositoryImpl(
    private val api: UserApi,
    private val dao: UserDao
) : UserRepository
```

Scope sai gây leak/state-sharing. `@Singleton` không phải default tốt cho mọi class; chỉ dùng khi lifetime thực sự app-wide.

# 17. Navigation nâng cao

Navigation gồm back stack, route identity, deep link, argument và ViewModel scope. Truyền stable ID thay object lớn/stale:

<!-- merge: preserve both canonical variants -->
```text
navigate(articleId)
→ destination reconstruct data từ repository
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
    viewModel.load(userId)
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
val state by viewModel.uiState.collectAsStateWithLifecycle()
```

Trong View system:
<!-- end merged variant -->

```kotlin
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
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

```text
Recomposition
< Composition entry
< Fragment view lifecycle
< Activity/Fragment lifecycle
< ViewModel
< Process
< Persisted storage / server
```

State phải được đặt ở owner ngắn nhất nhưng đủ sống qua requirement. Đặt quá ngắn gây mất state; đặt quá dài gây leak, stale data hoặc shared state ngoài ý muốn.

## 20.2 Fragment có hai lifecycle đáng chú ý

Fragment object lifecycle và Fragment **view lifecycle** không giống nhau. Binding/collector chạm View phải gắn với `viewLifecycleOwner`, vì Fragment có thể còn tồn tại sau khi View đã destroy.

Đây là nguồn leak/crash phổ biến ở XML/View codebase và là một lý do Compose route/state ownership cần được hiểu qua lifetime thay vì chỉ syntax.
<!-- end merged variant -->

# 21. WorkManager

WorkManager cho **deferrable durable work** cần eventually run và có constraints/retry.

```kotlin
class SyncWorker(...) : CoroutineWorker(...) {
    override suspend fun doWork(): Result = try {
        sync()
        Result.success()
    } catch (e: IOException) {
        Result.retry()
    }
}
```

Không retry mọi exception. Validation/4xx nghiệp vụ thường cần failure, không phải retry vô hạn.

# 22. DataStore

Preferences DataStore phù hợp key-value; Proto DataStore phù hợp schema rõ. Không dùng DataStore như relational database.

Migration SharedPreferences → DataStore nên giữ key/semantic behavior, không chỉ copy giá trị.

# 23. Testing

Ba tầng cơ bản:

```text
JVM unit test
integration test boundary
instrumented/UI test
```

Business logic nên test nhanh ngoài Android framework nếu có thể. Fake tốt cho collaborator stateful; mock tốt cho interaction hẹp.

Một test có giá trị chứng minh behavior/invariant, không khóa implementation detail.

# 24. Error handling và retry

Không `catch(Exception)` mọi nơi rồi trả string chung.

```kotlin
sealed interface DataError {
    data object Offline : DataError
    data object Timeout : DataError
    data object Unauthorized : DataError
    data class Http(val code: Int) : DataError
    data class Unknown(val cause: Throwable) : DataError
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
```text
Deprecated/unsafe
Supported nhưng có replacement
Still-valid cho use case cụ thể
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

```text
app/
├─ ui/
│  ├─ home/
│  │  ├─ HomeRoute.kt
│  │  ├─ HomeScreen.kt
│  │  ├─ HomeViewModel.kt
│  │  └─ HomeUiState.kt
│  └─ navigation/
├─ domain/              # optional
│  ├─ model/
│  └─ usecase/
├─ data/
│  ├─ repository/
│  ├─ remote/
│  └─ local/
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

```text
owner là ai?
sống qua recomposition không?
sống qua configuration change không?
sống qua process death không?
operation có thể overlap không?
result cũ có thể tới sau result mới không?
cancellation có nghĩa gì?
collector dừng thì producer có tiếp tục không?
state authoritative nằm ở đâu?
```

Coroutine phải có scope owner; Flow phải có sharing/lifecycle semantics; repository phải có source-of-truth policy; UI không được trực tiếp biết chi tiết storage/network nếu không có lý do rõ ràng. Khi các câu này rõ, framework choice thường trở nên đơn giản hơn.

---

# 28. Serialization, DTO và boundary giữa network/domain

Network payload thường là JSON, nhưng object nhận từ server không nên mặc định trở thành domain model dùng khắp ứng dụng. DTO (**Data Transfer Object**) phản ánh contract transport; domain model phản ánh ý nghĩa nghiệp vụ. Tách hai loại này cho phép backend thay field, nullable hoặc naming mà không làm domain layer bị phụ thuộc trực tiếp.
<!-- end merged variant -->

```kotlin
@Serializable
data class UserDto(
    val id: Long,
    val display_name: String? = null
)
```

Unknown field, missing field, new enum value và null bất ngờ là tình huống bình thường khi client/server release độc lập. Parser/model cần forward-compatible ở nơi phù hợp.

# 29. Parcelable, Bundle và component boundary

Bundle/Intent chỉ nên mang dữ liệu nhỏ. `@Parcelize` giúp generate Parcelable nhưng không phải lý do truyền object graph lớn.

```kotlin
@Parcelize
data class UserArgs(val userId: Long) : Parcelable
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

```text
R8/obfuscation/resource shrinking
manifest merge
BuildConfig/env
signing
production endpoint
feature flags
```

CI nên build ít nhất release/minified variant quan trọng. Secret không trở nên an toàn vì nằm trong BuildConfig.

# 34. Coroutine/Flow testing có kiểm soát thời gian

Dùng `runTest`/TestDispatcher thay `Thread.sleep()`.

```kotlin
@Test
fun loadUser_updatesState() = runTest {
    val vm = UserViewModel(fakeRepo)
    vm.load()
    advanceUntilIdle()
    assertEquals("An", vm.uiState.value.name)
}
```

Với race/latest-wins, fake repository có thể cho phép test điều khiển thứ tự completion thay vì dựa timing ngẫu nhiên.

<!-- merge: preserve both canonical variants -->
# 35. Process death như test case thiết kế

ViewModel sống qua configuration change nhưng không sống qua process death. Phân loại state:

```text
reloadable data → repository/source of truth
small reconstruct key → SavedStateHandle/rememberSaveable
durable business data → DB/DataStore/server
```
<!-- merge: preserve both canonical variants -->
Đối với `stateIn(WhileSubscribed(...))`, test cần có collector nếu muốn upstream chạy. Đây là lỗi test phổ biến: assert StateFlow nhưng không tạo subscription, trong khi sharing policy cố ý chưa start upstream.

# 35. Process death như một test case thiết kế

Configuration change và process death không giống nhau. ViewModel giúp sống qua recreation trong cùng process nhưng không tồn tại sau khi process bị kill.

Hãy phân loại state theo lifetime:

```text
Derived/reloadable data
→ reconstruct từ repository/source of truth

Small navigation/form state
→ SavedStateHandle hoặc rememberSaveable nếu phù hợp

Durable business data
→ database/DataStore/server

Transient animation/scroll detail
→ chỉ save nếu UX thực sự yêu cầu
```

`SavedStateHandle` không phải database. Nhét object graph lớn vào saved state tạo serialization/Binder cost và khiến state cũ trở thành source of truth ngoài ý muốn.

Một screen production nên có reconstruction recipe:

```text
stable route ID
+ small saved user input
+ repository persisted data
→ rebuild UiState
```

Test process death nên kiểm tra recipe này thay vì chỉ rotate screen. Configuration change có thể giữ ViewModel; process recreation thì không.
<!-- end merged variant -->

Nếu screen chỉ restore được bằng cách save toàn object graph vào Bundle, architecture có thể đang thiếu stable identity/source of truth.

<!-- merge: preserve both canonical variants -->
# 36. Intermediate integration project

Một project kết thúc Intermediate nên chứng minh được flow:

```text
UI action
→ ViewModel
→ repository
→ network/Room
→ source-of-truth update
→ Flow/StateFlow
→ lifecycle-aware UI render
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

```text
Nếu Android kill process ngay bây giờ,
state nào phải tự khôi phục và state nào được phép mất?
```

Nếu không trả lời được, state model chưa hoàn chỉnh.

# 38. Stale-result race và ordering

Ví dụ user gõ search nhanh:

```text
query = "a"  → request A
query = "ab" → request B
B trả trước
A trả sau
```

Nếu ViewModel set state theo callback completion, A có thể overwrite kết quả mới hơn của B.

Một hướng giải quyết ở Flow:

```kotlin
val results = query
    .debounce(300)
    .distinctUntilChanged()
    .flatMapLatest { repository.search(it) }
```

`flatMapLatest` cancel flow cũ khi query mới tới. Nếu API không cancellable hoặc callback boundary không cooperate, vẫn có thể dùng request-generation token để reject stale response.

Điểm cốt lõi: concurrency bug thường là **ordering bug**, không phải “thiếu thread”.

# 39. Repository implementation end-to-end

Một repository offline-readable có thể có structure:

```kotlin
class OfflineFirstUserRepository(
    private val api: UserApi,
    private val dao: UserDao,
    private val ioDispatcher: CoroutineDispatcher
) : UserRepository {

    override fun observeUsers(): Flow<List<User>> =
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

```text
read = observe source of truth
refresh = fetch external source rồi update source of truth
```

Nếu UI observe network response trực tiếp trong khi Room cũng emit cùng entity, bạn có hai nguồn state cạnh tranh.

## 39.1 Mapper tồn tại để bảo vệ boundary

```text
DTO
→ transport contract

Entity
→ local schema

Domain
→ application meaning

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

```text
operationId = UUID
client gửi operationId cùng request
server lưu kết quả theo operationId
retry cùng operationId trả lại cùng logical result
```

Intermediate developer chưa cần xây distributed sync engine, nhưng cần hiểu vì sao `catch IOException -> retry()` không an toàn cho mọi mutation.

Retry classification cơ bản:

```text
DNS/offline/transient 5xx → có thể retry tùy policy
401 → session recovery, không retry vô hạn
validation 4xx → không retry tự động
conflict → cần business resolution
unknown timeout after mutation → cần idempotency/reconciliation
```

# 41. Debug vs release: cách điều tra khác biệt artifact

Nếu debug chạy nhưng release fail, không nên tiếp tục debug source giống nhau rồi kết luận “Android ngẫu nhiên”. Hãy so sánh artifact path.

Checklist:

```text
R8 có strip/rename class không?
consumer ProGuard rules có đủ không?
reflection/serialization có phụ thuộc tên class không?
manifest merge khác không?
resource shrink có xóa resource được lookup động không?
BuildConfig/base URL/feature flag khác không?
signing/certificate-dependent API có khác không?
prod backend schema có khác staging không?
```

Release bug thường là build/configuration/boundary bug hơn là UI syntax bug.

# 42. Migration scenario: legacy → modern theo từng seam

Giả sử app cũ dùng:

```text
Fragment XML
LiveData
RxJava repository
SharedPreferences
startActivityForResult
```

Không cần rewrite toàn bộ cùng lúc.

Một migration an toàn hơn:

```text
1. thêm characterization tests cho flow quan trọng
2. đổi Activity Result API độc lập
3. adapter Rx observable → Flow ở boundary mới
4. màn hình mới dùng StateFlow/ViewModel
5. migrate settings mới sang DataStore + migration cũ
6. nhúng Compose ở leaf screen nếu có benefit
7. theo dõi crash/performance
8. xóa path cũ sau khi không còn caller
```

Điểm mạnh của seam-based migration là mỗi bước có thể review/rollback riêng.

# 43. Debugging playbook theo layer

Khi app “không hoạt động”, đừng sửa ngẫu nhiên. Xác định layer.

```text
UI không update
→ state có đổi không?
→ collector có active lifecycle không?
→ Compose có đọc đúng observable state không?

Data không đúng
→ repository source of truth là gì?
→ mapper có mất field/null không?
→ DB transaction có commit không?

Request fail
→ transport/protocol/auth/domain error loại nào?
→ endpoint/variant/config đúng không?

Chỉ release fail
→ R8/signing/manifest/resource/config

Sau rotate/process recreation fail
→ state owner/saved-state/source-of-truth
```

Debug tốt là thu evidence ở đúng boundary: log có correlation/context, DB inspector, network trace, profiler, stack trace và test tái hiện.

# 44. Intermediate completion checklist

Trước khi sang Advanced/Senior, bạn nên tự giải thích được mà không nhìn tài liệu:

```text
suspend khác thread thế nào?
structured concurrency bảo vệ lifetime ra sao?
Flow cold khác StateFlow hot thế nào?
SharedFlow/event có thể mất hoặc replay ra sao?
ViewModel sống qua gì và không sống qua gì?
remember / rememberSaveable / SavedStateHandle / Room khác lifetime nào?
repository có nhiệm vụ gì ngoài gọi API?
source of truth là gì?
DTO/Entity/Domain/UI model tách khi nào?
retry mutation vì sao có thể nguy hiểm?
WorkManager khác coroutine/Service thế nào?
XML/LiveData/RxJava là legacy hay vẫn valid trong trường hợp nào?
debug chạy nhưng release fail thì kiểm tra gì?
```

Nếu các câu trả lời đều dựa trên **owner, lifetime, state, failure và compatibility** thay vì chỉ tên framework, bạn đã sẵn sàng cho level Advanced/Senior.
<!-- merge: preserve both canonical variants -->
Một project kết thúc Intermediate nên có ít nhất một flow từ UI → ViewModel → Repository → local/network data source; UI state expose bằng StateFlow; Room làm local persistence; network layer map DTO sang domain; navigation có typed/validated argument; DI rõ ràng; coroutine có lifecycle owner; loading/error/empty/success state được model; unit test cho ViewModel/repository và ít nhất một integration test cho DB hoặc serialization.

Ngoài happy path, project nên chứng minh được ít nhất các case: rotate/recreate screen không mất state cần thiết; process death có thể reconstruct bằng stable ID/source of truth; search/query mới không bị result cũ overwrite; collector dừng khi UI không active; cancellation không bị convert thành generic error; release behavior không phụ thuộc `GlobalScope` hay ad-hoc lifetime.
<!-- end merged variant -->
