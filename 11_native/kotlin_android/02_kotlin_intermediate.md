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

Nested `let/apply/run` dễ làm mất ngữ nghĩa `this`/`it`; hãy đặt tên lambda parameter hoặc tách block.

# 3. Extension function và property

Extension được resolve statically theo declared type, không phải virtual dispatch. Nó phù hợp thêm convenience/API adapter, không thay polymorphism runtime.

# 4. Generics và variance

`out T` cho producer, `in T` cho consumer. Star projection `Foo<*>` hữu ích khi chưa biết type argument nhưng vẫn muốn thao tác trong giới hạn an toàn.

# 5. `object`, `companion object` và singleton

`object` tạo singleton theo class-loading semantics. Không biến mọi service thành global singleton; stateful singleton làm testing/lifetime khó hơn. DI thường quản lý lifecycle rõ hơn.

# 6. Delegation và delegated properties

Class delegation và property delegate giảm boilerplate khi semantics đúng. `lazy`, Compose state delegation và custom ViewBinding delegate là ví dụ phổ biến.

# 7. Sequences

`Sequence` lazy và có thể giảm intermediate collection với pipeline dài/short-circuit. Collection nhỏ/chain ngắn không mặc định nhanh hơn; performance cần đo.

# 8. Coroutine nền tảng

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

# 9. Structured concurrency

Coroutine con sống trong scope cha. Điều này tạo ownership và cancellation có cấu trúc.

```kotlin
suspend fun loadPage(): Page = coroutineScope {
    val user = async { userRepo.load() }
    val posts = async { postRepo.load() }
    Page(user.await(), posts.await())
}
```

Chỉ parallel khi hai operation độc lập. `supervisorScope` phù hợp khi sibling failure độc lập; nó không tự xử lý error.

Tránh `GlobalScope`. Hỏi: **ai sở hữu coroutine và khi owner chết thì work có nên tiếp tục không?**

# 10. Flow, StateFlow và SharedFlow

`Flow<T>` thường cold: upstream chạy khi collect. `StateFlow` là hot state holder có current value. `SharedFlow` là hot broadcast stream với replay/buffer cấu hình được.

```kotlin
private val _uiState = MutableStateFlow(UiState())
val uiState: StateFlow<UiState> = _uiState.asStateFlow()
```

Không chọn SharedFlow chỉ vì “event”. Trước hết hỏi event có cần survive collector inactive/recreation không. Nếu câu trả lời có, có thể đó là durable state chứ không phải one-off event.

Các operator như `debounce`, `combine`, `distinctUntilChanged`, `flatMapLatest` cần dùng theo semantics. `flatMapLatest` hợp search latest-wins nhưng không hợp audit stream nơi mọi item phải xử lý.

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

ViewModel là screen-level state holder/orchestrator, không phải nơi chứa toàn bộ networking, SQL và service locator.

Ví dụ state:

```kotlin
data class UserUiState(
    val users: List<UserUi> = emptyList(),
    val isInitialLoading: Boolean = false,
    val isRefreshing: Boolean = false,
    val error: UiError? = null
)
```

Phân biệt initial load và refresh giúp UI giữ cached content thay vì thay toàn màn hình bằng spinner.

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

```text
navigate(articleId)
→ destination reconstruct data từ repository
```

Deep link là external input, phải validate và authorization lại ở destination/domain layer.

# 18. Compose state/effect

`remember` sống qua recomposition trong cùng composition. `rememberSaveable` có thể save qua recreation cho value phù hợp. `LaunchedEffect(key)` chạy coroutine theo composition lifetime; `DisposableEffect` cleanup resource; `rememberUpdatedState` cập nhật latest callback mà không restart effect.

Không gọi network trực tiếp trong Composable body. Business operation nên do owner phù hợp quản lý.

# 19. XML interoperability

Compose và View system có thể coexist. `ComposeView` cho View/Fragment host Compose; `AndroidView` cho Compose host View.

XML/Fragment/RecyclerView/View Binding không “sai” chỉ vì Compose tồn tại. Migration incremental giảm regression risk.

# 20. Lifecycle-aware collection

Compose thường dùng `collectAsStateWithLifecycle()`. View system dùng `repeatOnLifecycle`.

```kotlin
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.uiState.collect(::render)
    }
}
```

Collector lifecycle phải phản ánh việc UI có cần nhận update khi invisible không.

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

Preferences DataStore phù hợp key-value typed wrapper; Proto DataStore phù hợp schema rõ. Không dùng DataStore như relational database.

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

Một error model đơn giản:

```kotlin
sealed interface DataError {
    data object Offline : DataError
    data object Timeout : DataError
    data object Unauthorized : DataError
    data class Http(val code: Int) : DataError
    data class Unknown(val cause: Throwable) : DataError
}
```

UI map error sang behavior phù hợp: offline có thể vẫn render cache; unauthorized có thể trigger session recovery; validation focus field.

## 24.1 Retry không phải mặc định

GET read thường dễ retry hơn mutation. Với POST tạo side effect, timeout có thể xảy ra sau khi server đã commit. Muốn retry an toàn cần backend idempotency contract/key.

## 24.2 Cancellation không phải error UI

Coroutine bị cancel do screen đóng không nên hiện snackbar “Something went wrong”. Đừng swallow `CancellationException`.

# 25. Security/configuration căn bản

Không hardcode server secret trong APK. BuildConfig/local.properties chỉ thay cách inject value vào artifact, không làm value đóng gói trở thành secret.

Dùng HTTPS, Network Security Config khi cần, Keystore cho key material, tránh log PII/token và validate Intent/deep-link/URI input từ bên ngoài.

# 26. Modern vs legacy migration notes

Phân loại legacy trước khi rewrite:

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

Transport DTO phản ánh wire schema; domain model phản ánh nghiệp vụ.

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

Quan trọng hơn: **debug chạy không chứng minh release chạy**. Release có thể khác vì:

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

# 35. Process death như test case thiết kế

ViewModel sống qua configuration change nhưng không sống qua process death. Phân loại state:

```text
reloadable data → repository/source of truth
small reconstruct key → SavedStateHandle/rememberSaveable
durable business data → DB/DataStore/server
```

Nếu screen chỉ restore được bằng cách save toàn object graph vào Bundle, architecture có thể đang thiếu stable identity/source of truth.

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

Ngoài happy path phải có ít nhất:

```text
offline với cache
refresh failure
process recreation bằng stable ID
validation/auth error
retry policy rõ
release variant build
DB/serialization integration test
```

Mục tiêu không phải nhồi framework, mà là thấy rõ **dependency direction + lifetime + failure behavior** trước khi bước sang Advanced/Senior.