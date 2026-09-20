# Kotlin + Android Master Note — Intermediate

> Mục tiêu: chuyển từ “viết được app” sang “xây app có cấu trúc đúng”, nắm Kotlin idioms, coroutine/Flow, ViewModel, Room, networking, navigation, lifecycle, testing và dependency injection.

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
13. Repository và data source
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
24. Error handling
25. Security và configuration căn bản
26. Migration/legacy notes
27. Project architecture mẫu

---

# 1. Kotlin idioms quan trọng

Kotlin không chỉ là Java viết ngắn hơn. Nếu mang nguyên tư duy Java sang Kotlin, code thường nhiều mutable state, nullable handling vụng và class ceremony không cần thiết. Kotlin idiomatic code tận dụng immutable value, expression, extension function, sealed hierarchy, higher-order function và standard library.

Ví dụ thay vì kiểm tra null thủ công:

```kotlin
if (user != null) {
    send(user)
}
```

có thể viết:

```kotlin
user?.let(::send)
```

Nhưng “ngắn hơn” không tự động là “tốt hơn”. Nếu chain scope function dài khiến khó đọc, code rõ ràng bằng `if` vẫn tốt hơn. Idiom là pattern làm intent rõ, không phải cuộc thi rút số dòng.

# 2. Scope functions: `let`, `run`, `with`, `apply`, `also`

Năm scope function đều tạo một scope tạm, nhưng khác nhau ở cách tham chiếu receiver và giá trị trả về.

| Function | Receiver bên trong | Trả về | Dùng tốt khi |
|---|---|---|---|
| `let` | `it` | lambda result | null-chain, transform |
| `run` | `this` | lambda result | configure + compute |
| `with(x)` | `this` | lambda result | nhóm nhiều call trên object đã có |
| `apply` | `this` | chính receiver | cấu hình object |
| `also` | `it` | chính receiver | side effect như log/debug |

```kotlin
val user = User().apply {
    name = "Lan"
    age = 25
}
```

```kotlin
val length = text?.let { value ->
    value.trim().length
} ?: 0
```

Lỗi thường gặp là nested `let/apply/run` làm mất ngữ nghĩa `this`/`it`. Senior code thường giới hạn nesting hoặc đặt tên lambda parameter rõ ràng.

# 3. Extension function và property

Extension tạo API có vẻ như method của type mà không sửa class gốc.

```kotlin
fun String.isEmailLike(): Boolean = contains("@") && contains(".")
```

Extension được resolve statically theo declared type, không phải virtual dispatch như member function.

```kotlin
open class Animal
class Dog : Animal()

fun Animal.name() = "animal"
fun Dog.name() = "dog"

val x: Animal = Dog()
println(x.name()) // animal
```

Do đó extension không phải cách override behavior runtime.

# 4. Generics và variance

Generics cho phép type-safe abstraction.

```kotlin
class Box<T>(val value: T)
```

Kotlin có declaration-site variance `out` và `in`.

```kotlin
interface Producer<out T> {
    fun produce(): T
}

interface Consumer<in T> {
    fun consume(value: T)
}
```

`out T` nghĩa type chủ yếu được produce; `in T` nghĩa type chủ yếu được consume. Quy tắc nhớ PECS của Java vẫn hữu ích về trực giác: Producer Extends, Consumer Super, nhưng Kotlin biểu diễn trực tiếp bằng variance modifier.

Use-site projection cũng tồn tại:

```kotlin
fun copy(from: Array<out Any>, to: Array<Any>) { ... }
```

Star projection `Foo<*>` dùng khi không biết type argument nhưng vẫn muốn thao tác an toàn trong giới hạn compiler cho phép.

# 5. `object`, `companion object` và singleton

`object` declaration tạo singleton lazy theo semantics của JVM/class initialization.

```kotlin
object AppLogger {
    fun log(message: String) { ... }
}
```

Không nên biến mọi service thành global singleton vì testability và dependency boundary sẽ kém. Dependency Injection thường quản lý singleton lifetime tốt hơn.

`companion object` là object gắn với class:

```kotlin
class User private constructor(val id: Long) {
    companion object {
        fun create(id: Long) = User(id)
    }
}
```

# 6. Delegation và delegated properties

Class delegation:

```kotlin
class LoggingList<T>(
    private val delegate: MutableList<T>
) : MutableList<T> by delegate
```

Property delegation phổ biến với `lazy`:

```kotlin
val config by lazy { loadConfig() }
```

Android XML/View code từng dùng `by lazy`, custom delegates hoặc Fragment view binding delegate. Với Compose, `by` còn xuất hiện trong state:

```kotlin
var text by remember { mutableStateOf("") }
```

Đây dựa trên `getValue`/`setValue` operator functions.

# 7. Sequences

Collection operation thông thường như `map().filter()` tạo intermediate collection tùy operation. `Sequence` xử lý lazy.

```kotlin
val result = (1..1_000_000)
    .asSequence()
    .map { it * 2 }
    .filter { it % 3 == 0 }
    .take(10)
    .toList()
```

Sequence không phải lúc nào nhanh hơn. Với collection nhỏ hoặc chain ngắn, overhead iterator/lambda có thể không đáng. Dùng khi pipeline dài, dữ liệu lớn hoặc cần short-circuit lazy.

# 8. Coroutine nền tảng

Coroutine là abstraction concurrency nhẹ, không đồng nghĩa với thread. Coroutine có thể suspend mà không block thread, sau đó resume trên thread thích hợp theo dispatcher/context.

`suspend` đánh dấu function có thể suspend và chỉ được gọi từ coroutine hoặc suspend function khác.

```kotlin
suspend fun loadUser(): User {
    delay(100)
    return User(...)
}
```

Coroutine builder thường gặp:

```kotlin
scope.launch { ... }       // trả Job
scope.async { ... }        // trả Deferred<T>
withContext(dispatcher) { ... }
```

`launch` phù hợp công việc không trả value trực tiếp; `async` phù hợp concurrent computation cần `await`. Không dùng `async` chỉ để “chạy coroutine” nếu không cần Deferred.

Dispatcher phổ biến: `Dispatchers.Main`, `IO`, `Default`. `Main` cho UI; `IO` cho blocking I/O; `Default` cho CPU-intensive work. Suspend function tốt nên “main-safe”: nếu bên trong có blocking I/O, chính function đó chuyển sang dispatcher phù hợp thay vì bắt caller nhớ chuyển thread.

# 9. Structured concurrency

Structured concurrency nghĩa lifecycle coroutine con bị ràng buộc với scope cha. Nó giúp cancellation, error propagation và resource cleanup có cấu trúc.

```kotlin
suspend fun loadPage(): Page = coroutineScope {
    val user = async { userRepo.load() }
    val posts = async { postRepo.load() }
    Page(user.await(), posts.await())
}
```

Nếu một child fail trong `coroutineScope`, các sibling thường bị cancel. `supervisorScope` dùng khi muốn child failure không tự cancel sibling.

Tránh `GlobalScope` trong application code. Scope nên có owner rõ ràng. Android chính thức cũng khuyến nghị inject dispatcher, tránh expose mutable type, để ViewModel tạo coroutine cho business actions, và dùng data/business layer expose suspend function hoặc Flow.

# 10. Flow, StateFlow và SharedFlow

`Flow<T>` là cold asynchronous stream: block upstream thường chỉ chạy khi có collector.

```kotlin
fun observeUsers(): Flow<List<User>> = dao.observeUsers()
```

Operator quan trọng:

```kotlin
flow
    .map { ... }
    .filter { ... }
    .distinctUntilChanged()
    .debounce(300)
    .catch { ... }
    .combine(other) { a, b -> ... }
```

`StateFlow` là hot state holder, luôn có current value. Rất phù hợp expose UI state từ ViewModel.

```kotlin
private val _uiState = MutableStateFlow(UiState())
val uiState: StateFlow<UiState> = _uiState.asStateFlow()
```

`SharedFlow` là hot broadcast stream cấu hình replay/buffer, phù hợp event stream hoặc shared upstream trong một số trường hợp. Tuy nhiên one-off UI event là chủ đề dễ thiết kế sai; không nên mặc định mọi event đều là `SharedFlow` nếu state-based modeling đơn giản hơn.

# 11. Android app architecture

Kiến trúc Android hiện đại thường chia tối thiểu UI layer và data layer; domain layer là optional khi business logic đủ phức tạp hoặc cần reuse rõ ràng.

UI layer nhận state và phát event. ViewModel điều phối UI state. Repository abstract nguồn dữ liệu và cung cấp API cho ViewModel/use case. Data source làm việc với network/database/platform API.

Một dependency direction điển hình:

```text
UI -> ViewModel -> UseCase(optional) -> Repository -> DataSource
```

Không nên để Composable gọi Retrofit/Room trực tiếp. Không nên để Repository biết Button hay NavController. Boundary rõ giúp test, thay nguồn dữ liệu và xử lý concurrency tốt hơn.

# 12. ViewModel và UI State

```kotlin
data class UserUiState(
    val loading: Boolean = false,
    val users: List<UserUi> = emptyList(),
    val errorMessage: String? = null
)

class UserViewModel(
    private val repository: UserRepository
) : ViewModel() {
    private val _uiState = MutableStateFlow(UserUiState())
    val uiState = _uiState.asStateFlow()

    fun refresh() {
        viewModelScope.launch {
            _uiState.update { it.copy(loading = true, errorMessage = null) }
            runCatching { repository.refresh() }
                .onFailure { e ->
                    _uiState.update { it.copy(errorMessage = e.message) }
                }
            _uiState.update { it.copy(loading = false) }
        }
    }
}
```

Trong app lớn, nên tránh nhiều boolean độc lập tạo impossible state. Có thể dùng sealed state hoặc state machine tùy domain.

# 13. Repository và data source

Repository không chỉ là wrapper “mỗi method gọi một DAO”. Nó nên đại diện abstraction dữ liệu mà upper layer cần, xử lý source of truth, synchronization, caching và policy.

```kotlin
interface UserRepository {
    fun observeUsers(): Flow<List<User>>
    suspend fun refresh()
}
```

Nếu app offline-first, database thường đóng vai trò source of truth; network refresh ghi DB; UI observe DB. Cách này giảm việc UI phải ghép nhiều source thủ công.

# 14. Room

Room là abstraction database trên SQLite.

Entity:

```kotlin
@Entity(tableName = "users")
data class UserEntity(
    @PrimaryKey val id: Long,
    val name: String
)
```

DAO:

```kotlin
@Dao
interface UserDao {
    @Query("SELECT * FROM users ORDER BY name")
    fun observeAll(): Flow<List<UserEntity>>

    @Upsert
    suspend fun upsertAll(items: List<UserEntity>)
}
```

Database:

```kotlin
@Database(entities = [UserEntity::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
}
```

Migration phải được quản lý nghiêm túc. `fallbackToDestructiveMigration` có thể hữu ích cho prototype nhưng có thể xóa data; không dùng vô thức trong production.

# 15. Networking

Android app thường dùng OkHttp + Retrofit hoặc Ktor client. Retrofit biến HTTP API thành Kotlin interface.

```kotlin
interface UserApi {
    @GET("users")
    suspend fun getUsers(): List<UserDto>

    @POST("users")
    suspend fun createUser(@Body request: CreateUserRequest): UserDto
}
```

Tách DTO khỏi domain model để backend schema không rò trực tiếp vào toàn app.

```kotlin
data class UserDto(val id: Long, val name: String)
fun UserDto.toDomain() = User(id, name)
```

Cần phân biệt transport failure, HTTP error, serialization error và domain error. `200` không luôn đồng nghĩa nghiệp vụ thành công nếu backend trả error code trong body.

# 16. Dependency Injection

DI đưa dependency từ bên ngoài thay vì class tự tạo chúng.

```kotlin
class UserRepositoryImpl(
    private val api: UserApi,
    private val dao: UserDao
) : UserRepository
```

Hilt là lựa chọn phổ biến trong Android Jetpack ecosystem. Koin là runtime DI/service locator style dễ bắt đầu nhưng có trade-off khác. Manual DI vẫn tốt cho app nhỏ và giúp hiểu bản chất.

Điểm quan trọng là lifetime/scope: singleton toàn app, Activity retained, ViewModel scoped, hoặc object transient. Sai scope có thể tạo memory leak hoặc state-sharing ngoài ý muốn.

# 17. Navigation nâng cao

Navigation không chỉ là `navigate("detail")`. Cần nghĩ về back stack, deep link, argument, saved state và ownership của ViewModel.

Không nên truyền object lớn qua navigation argument. Truyền stable identifier rồi load dữ liệu tại destination thường tốt hơn, tránh vượt Binder transaction limit và tránh stale object.

# 18. Compose state và effect

Compose có nhiều API state/effect với mục đích khác nhau.

`remember` giữ value qua recomposition. `rememberSaveable` thêm khả năng save qua recreation khi value saveable. `derivedStateOf` tạo state suy ra và hữu ích khi muốn giảm recomposition khi derived result không đổi. `LaunchedEffect` chạy coroutine gắn với composition lifecycle theo key. `DisposableEffect` có cleanup. `SideEffect` publish state ra non-Compose object sau successful composition. `rememberUpdatedState` giữ latest value trong long-lived effect mà không restart effect.

Ví dụ:

```kotlin
LaunchedEffect(userId) {
    viewModel.load(userId)
}
```

Sai lầm hay gặp là dùng `LaunchedEffect(Unit)` để chạy business logic mà không hiểu lifecycle, hoặc gọi network trực tiếp trong Composable body gây call lặp khi recomposition.

# 19. XML interoperability

Compose có thể nhúng View qua `AndroidView`; XML/View app có thể nhúng Compose qua `ComposeView`. Điều này rất hữu ích khi migration từng màn hình.

Legacy View code còn gặp Fragment, RecyclerView, ConstraintLayout, LiveData, Data Binding, View Binding. Không cần rewrite toàn bộ chỉ để “hiện đại”; migration nên dựa vào cost/risk.

# 20. Lifecycle-aware collection

Trong Compose, thường dùng `collectAsStateWithLifecycle` để collect Flow thành Compose State theo lifecycle thích hợp.

Trong View system, dùng `repeatOnLifecycle`:

```kotlin
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.uiState.collect { state ->
            render(state)
        }
    }
}
```

Không nên `launch { flow.collect {} }` vô hạn trong Activity mà không quan tâm lifecycle nếu collector cần dừng khi UI không visible.

# 21. WorkManager

WorkManager dành cho deferrable, guaranteed background work có constraint, ví dụ sync dữ liệu cần eventually execute. Nó không phải replacement chung cho mọi coroutine/background task.

```kotlin
class SyncWorker(
    appContext: Context,
    params: WorkerParameters
) : CoroutineWorker(appContext, params) {
    override suspend fun doWork(): Result {
        return try {
            sync()
            Result.success()
        } catch (e: IOException) {
            Result.retry()
        }
    }
}
```

# 22. DataStore

DataStore phù hợp thay SharedPreferences cho key-value/settings hiện đại. Có Preferences DataStore và Proto DataStore. Preferences đơn giản nhưng không type-safe schema mạnh; Proto có schema rõ hơn và migration tốt hơn.

Không dùng DataStore như database quan hệ. Room phù hợp dữ liệu có query/relationship lớn hơn.

# 23. Testing

Ba tầng test phổ biến: local unit test chạy JVM, instrumentation test chạy device/emulator, UI test (Compose/UI Automator/Espresso tùy stack).

Business logic nên test không cần Android framework nếu có thể.

Coroutine test dùng `runTest` và `TestDispatcher`. Android guidance khuyến nghị inject dispatcher để test deterministic hơn.

```kotlin
@Test
fun load_success_updatesState() = runTest {
    val repo = FakeRepository(...)
    val vm = UserViewModel(repo)
    vm.refresh()
    advanceUntilIdle()
    assertFalse(vm.uiState.value.loading)
}
```

# 24. Error handling

Không catch `Exception` mọi nơi rồi bỏ qua. Đặc biệt trong coroutine, không nên swallow `CancellationException` vì cancellation cooperative cần propagate.

Boundary pattern thường là data layer map low-level exceptions thành domain error khi cần, ViewModel chuyển domain result thành UI state, UI render state và action retry.

# 25. Security và configuration căn bản

Không hardcode API secret trong APK và kỳ vọng nó bí mật; APK có thể reverse engineer. API cần secret thực sự nên đặt logic phía server hoặc dùng cơ chế token thích hợp.

BuildConfig field, resource value và local properties có thể hữu ích quản lý environment nhưng không biến secret client thành an toàn tuyệt đối.

Dùng HTTPS, Network Security Config khi cần policy, Android Keystore cho cryptographic keys, và tránh log dữ liệu nhạy cảm.

# 26. Migration/legacy notes

`LiveData` vẫn hợp lệ và phổ biến trong app cũ; app Kotlin/Compose mới thường dùng Flow/StateFlow. `AsyncTask` deprecated và nên thay bằng coroutine/WorkManager tùy use case. `startActivityForResult`/`onActivityResult` nên thay bằng Activity Result API. `SharedPreferences` không bị “cấm”, nhưng DataStore thường là lựa chọn mới tốt hơn. XML/View system không deprecated; Compose chỉ là hướng UI hiện đại được ưu tiên.

# 27. Project architecture mẫu

```text
app/
├─ ui/
│  ├─ home/
│  │  ├─ HomeScreen.kt
│  │  ├─ HomeViewModel.kt
│  │  └─ HomeUiState.kt
│  └─ navigation/
├─ domain/
│  ├─ model/
│  └─ usecase/
├─ data/
│  ├─ repository/
│  ├─ remote/
│  └─ local/
└─ di/
```

Domain layer có thể bỏ nếu app đơn giản. Đừng tạo use case một dòng chỉ vì template bảo phải có. Kiến trúc tốt giảm coupling và làm dependency/business rules rõ hơn; kiến trúc xấu chỉ tăng folder.

---

## Intermediate Senior Notes

Một Android developer ở mức intermediate nên bắt đầu nhìn app như một hệ thống state + side effect + lifecycle chứ không phải collection các callback. Khi state ownership rõ ràng, lifecycle rõ ràng và data flow một chiều, phần lớn bug “màn hình tự dưng sai” giảm mạnh. Coroutine phải có scope owner; Flow phải có lifecycle; repository phải có policy; UI không được trực tiếp biết chi tiết storage/network nếu không có lý do rõ ràng.

---

# 28. Serialization, DTO và boundary giữa network/domain

Network payload thường là JSON, nhưng object nhận từ server không nên mặc định trở thành domain model dùng khắp ứng dụng. DTO (**Data Transfer Object**) phản ánh contract transport; domain model phản ánh ý nghĩa nghiệp vụ. Tách hai loại này cho phép backend thay field, nullable hoặc naming mà không làm domain layer bị phụ thuộc trực tiếp.

```kotlin
@Serializable
data class UserDto(
    val id: Long,
    val display_name: String? = null
)

data class User(
    val id: Long,
    val displayName: String
)

fun UserDto.toDomain() = User(
    id = id,
    displayName = display_name.orEmpty()
)
```

Kotlin Serialization, Moshi và Gson là các lựa chọn phổ biến tùy stack. Khi dùng reflection-based serializer cần hiểu R8/obfuscation và default constructor/annotation requirements. Với Kotlin Serialization, compiler plugin tạo serializer giúp type-safe hơn và tránh một số reflection cost. Dù dùng library nào, unknown field, missing field, enum value mới, null bất ngờ và schema migration đều phải được xem là tình huống bình thường của hệ thống phân tán.

# 29. Parcelable, Bundle và dữ liệu truyền giữa component

`Bundle`/Intent argument phù hợp cho dữ liệu nhỏ. Android có `Parcelable` để serialization hiệu quả hơn trong IPC/component boundary. Kotlin Android Extensions trước đây từng cung cấp `@Parcelize`; hiện `kotlin-parcelize` plugin là cách chuẩn nếu muốn compiler generate implementation.

```kotlin
@Parcelize
data class UserArgs(
    val userId: Long,
    val source: String
) : Parcelable
```

Không truyền object graph lớn qua Intent/Bundle. Cách bền vững hơn là truyền ID nhỏ rồi load dữ liệu từ repository/database. Điều này tránh Binder transaction limit, giảm coupling và giúp process recreation dễ phục hồi hơn.

# 30. Files, MediaStore và scoped storage

Android có nhiều loại storage với lifetime và visibility khác nhau. Internal app storage chỉ app truy cập trực tiếp và thường bị xóa khi uninstall. Cache có thể bị hệ thống dọn. Shared media như ảnh/video nên đi qua MediaStore hoặc system picker theo API hiện hành. Không nên áp dụng tư duy “đường dẫn file tùy ý” từ desktop vào Android hiện đại vì scoped storage và permission model đã thay đổi đáng kể qua nhiều Android version.

Khi cần user chọn tài liệu, Storage Access Framework hoặc Activity Result contract thường tốt hơn tự xin quyền truy cập toàn bộ storage. URI trả về có thể là `content://`, vì vậy code nên làm việc qua `ContentResolver` thay vì cố chuyển mọi URI thành filesystem path.

# 31. Notification và foreground work

Notification không chỉ là gọi `notify()`. Từ Android 8, notification thường cần channel. Một số phiên bản Android mới còn có runtime notification permission. Notification channel được người dùng kiểm soát; sau khi tạo, một số behavior không thể tùy ý đổi như config nội bộ bình thường.

Foreground Service dành cho công việc ongoing mà người dùng nhận biết và platform cho phép, đồng thời yêu cầu notification thích hợp. Nó không phải cách lách background restriction. Nếu công việc có thể trì hoãn và cần bảo đảm chạy, WorkManager thường đúng hơn. Nếu công việc chỉ tồn tại cùng một màn hình, coroutine trong lifecycle/ViewModel thường đúng hơn. Chọn primitive theo **lifetime và guarantee**, không theo thói quen.

# 32. Deep link và App Link

Deep link đưa user trực tiếp đến destination cụ thể. Custom scheme như `myapp://product/42` dễ thiết lập nhưng có thể bị app khác đăng ký cùng scheme. Android App Links dùng HTTPS domain và domain verification để tạo liên kết đáng tin cậy hơn.

Route từ external input phải được validate. Không giả định query parameter luôn tồn tại hoặc có format đúng. Nếu deep link có thể mở chức năng nhạy cảm, authorization vẫn phải kiểm tra sau khi điều hướng; deep link không phải bằng chứng người dùng được phép truy cập dữ liệu đó.

# 33. Build variants, product flavors và BuildConfig

Build type thường biểu diễn cách build như `debug`/`release`; product flavor thường biểu diễn biến thể sản phẩm như `dev`, `staging`, `prod` hoặc region/brand. Hai chiều này kết hợp thành build variant. Cần tránh tạo quá nhiều dimension vì số variant tăng theo tích Descartes và làm build, test, CI phức tạp hơn.

Thông tin như base URL có thể khác theo variant, nhưng **secret thực sự không trở nên an toàn chỉ vì đặt trong BuildConfig/local.properties**. Bất kỳ giá trị nào đóng gói trong app đều có khả năng bị trích xuất. Secret dài hạn phải được bảo vệ phía server hoặc bằng protocol phù hợp.

# 34. Coroutine/Flow testing có kiểm soát thời gian

Coroutine test nên dùng `kotlinx-coroutines-test` để điều khiển scheduler thay vì `Thread.sleep()`. `runTest` có virtual time và cho phép `advanceUntilIdle()`/`advanceTimeBy()` khi cần. Dispatcher nên inject để production dùng dispatcher thật còn test dùng test dispatcher.

```kotlin
@Test
fun loadUser_updatesState() = runTest {
    val dispatcher = StandardTestDispatcher(testScheduler)
    val vm = UserViewModel(fakeRepo, dispatcher)

    vm.load()
    advanceUntilIdle()

    assertEquals("An", vm.uiState.value.name)
}
```

Với Flow, cần quyết định đang test snapshot state cuối cùng hay chuỗi emission. StateFlow có giá trị hiện tại; cold Flow chỉ chạy khi collect. Một test tốt xác minh behavior công khai, không khóa chặt implementation detail như số coroutine nội bộ nếu điều đó không phải contract.

# 35. Process death như một test case thiết kế

Configuration change và process death không giống nhau. ViewModel giúp sống qua recreation trong cùng process nhưng không tồn tại sau khi process bị kill. Khi thiết kế screen, hãy phân loại state: dữ liệu có thể reload từ repository; input nhỏ cần phục hồi bằng SavedStateHandle/rememberSaveable; dữ liệu nghiệp vụ bền vững cần persist ở database/DataStore/server.

Một dấu hiệu kiến trúc yếu là cần nhét toàn bộ object graph vào saved state để “không mất gì”. Kiến trúc tốt thường có stable identifier và source of truth có thể reconstruct state.

# 36. Intermediate integration project nên có gì

Một project kết thúc Intermediate nên có ít nhất một flow từ UI → ViewModel → Repository → local/network data source; UI state expose bằng StateFlow; Room làm local persistence; network layer map DTO sang domain; navigation có typed/validated argument; DI rõ ràng; coroutine có lifecycle owner; loading/error/empty/success state được model; unit test cho ViewModel/repository và ít nhất một integration test cho DB hoặc serialization. Mục tiêu không phải nhồi framework mà là nhìn thấy dependency direction và lifetime của dữ liệu xuyên suốt một app hoàn chỉnh.
