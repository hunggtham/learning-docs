# Kotlin + Android Intermediate — Completion Deep Dive

> File này bổ sung cho [`../02_kotlin_intermediate.md`](../02_kotlin_intermediate.md). Mục tiêu là làm rõ những phần thường bị tutorial rút gọn: CoroutineContext/Job hierarchy, Flow context và hot/cold conversion, resource lifetime, network error model, Room như source of truth, Compose state/effect, coroutine testing, DI scope và navigation contract.

# 1. Coroutine context, dispatcher và Job hierarchy

Một coroutine không chỉ có đoạn code `suspend`; nó chạy trong **CoroutineContext** gồm các element như `Job`, `CoroutineDispatcher`, `CoroutineName` và đôi khi exception handler. `Job` tạo cây ownership; dispatcher quyết định nơi continuation được schedule. Đây là lý do structured concurrency quan trọng: child coroutine thuộc lifecycle của scope thay vì trở thành công việc vô chủ.

```kotlin
viewModelScope.launch {
    val user = withContext(ioDispatcher) {
        repository.loadUser()
    }
    _uiState.value = UiState.Content(user)
}
```

`Dispatchers.Main` dùng cho UI; `Dispatchers.IO` tối ưu cho blocking I/O; `Dispatchers.Default` dành cho CPU-bound work. Tuy nhiên thư viện suspend tốt thường tự quản context phù hợp. Không cần bọc mọi Retrofit suspend call bằng `withContext(Dispatchers.IO)` theo thói quen nếu client đã non-blocking.

`coroutineScope` tạo scope con và fail cùng child; `supervisorScope` ngăn failure của một child tự động cancel sibling. `SupervisorJob` có semantics tương tự ở Job hierarchy. Chọn supervision dựa trên quan hệ lỗi thực tế: hai request bắt buộc cùng thành công nên fail together; hai widget độc lập có thể supervise riêng.

Cancellation cooperative. `delay`, Flow và nhiều suspend API kiểm tra cancellation; CPU loop dài phải tự kiểm tra `ensureActive()` hoặc `yield()` nếu cần responsive cancellation. Không nuốt `CancellationException` trong `catch (Exception)` rồi tiếp tục như bình thường.

# 2. `launch`, `async`, `withContext` và parallelism có chủ đích

`launch` trả `Job` và phù hợp công việc không cần return value trực tiếp. `async` trả `Deferred<T>` và chỉ có giá trị khi thực sự cần concurrent computation rồi `await`. Dùng `async` cho mọi suspend call chỉ làm lifecycle/error phức tạp hơn.

```kotlin
suspend fun loadDashboard(): Dashboard = coroutineScope {
    val user = async { userRepository.load() }
    val alerts = async { alertRepository.load() }
    Dashboard(user.await(), alerts.await())
}
```

Ví dụ trên chỉ có lợi khi hai operation độc lập và có thể chạy song song. Nếu `alerts` cần user ID từ request đầu, chạy parallel là sai dependency graph.

# 3. Flow cold/hot và context preservation

Một Flow tạo bằng `flow {}` thường là **cold**: mỗi collector chạy lại producer. `StateFlow` và `SharedFlow` là hot: chúng tồn tại theo lifetime của owner và collector chỉ subscribe vào stream đang tồn tại.

```kotlin
val uiState: StateFlow<UiState> = repository.observeNotes()
    .map { notes -> UiState.Content(notes) }
    .stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(5_000),
        initialValue = UiState.Loading
    )
```

Các operator cần hiểu theo semantics. `map` transform; `filter` loại emission; `combine` tính value từ emission mới nhất của nhiều upstream; `zip` ghép theo cặp emission; `debounce` chờ input ổn định; `distinctUntilChanged` bỏ value liên tiếp tương đương; `flatMapLatest` hủy flow cũ khi key mới đến, phù hợp search query.

Flow có **context preservation**. `flowOn(dispatcher)` đổi context của upstream trước operator đó; collector vẫn chạy context của collector. Không `withContext` tùy tiện quanh `emit` trong `flow {}` vì có thể vi phạm Flow invariant.

# 4. `stateIn`, `shareIn` và `SharingStarted`

`stateIn` chuyển Flow thành `StateFlow` và luôn có current value. `shareIn` tạo `SharedFlow` dùng chung upstream. Hai API này tránh việc mỗi collector khởi động lại network/database pipeline đắt tiền, nhưng scope và start policy phải đúng.

`SharingStarted.WhileSubscribed(...)` thường hợp UI vì upstream hoạt động khi có subscriber và có thể giữ một khoảng timeout để tránh stop/start liên tục khi configuration change. `Eagerly` khởi ngay khi scope tạo; `Lazily` đợi subscriber đầu tiên. Không copy `WhileSubscribed(5_000)` như magic number nếu product/lifecycle requirement khác.

# 5. `callbackFlow` và bridge callback API

`callbackFlow` adapter một callback API thành Flow. Điều quan trọng nhất là cleanup callback bằng `awaitClose`; nếu quên unregister listener, leak có thể xuất hiện.

```kotlin
fun LocationClient.locations(): Flow<Location> = callbackFlow {
    val listener = LocationListener { location ->
        trySend(location)
    }

    register(listener)
    awaitClose { unregister(listener) }
}
```

Nếu callback có thể emit nhanh hơn collector, cần quyết định buffer/overflow semantics thay vì mặc định giả định mọi event đều được xử lý kịp.

# 6. Resource management và `use`

Một số resource như stream, cursor, file descriptor phải được đóng dù success hay exception. Kotlin cung cấp `use`, tương tự try-with-resources.

```kotlin
contentResolver.openInputStream(uri)?.use { input ->
    val bytes = input.readBytes()
}
```

Không đóng resource là bug lifecycle/resource leak, khác với garbage collection. GC có thể thu object nhưng không đảm bảo release tài nguyên hệ điều hành đúng thời điểm.

# 7. Network layer: transport, protocol và domain error

Retrofit mô tả HTTP API; OkHttp thực hiện transport phổ biến trong Android stack. Một network layer production cần timeout, authentication, logging an toàn, cancellation và error mapping rõ ràng.

Cần tách ít nhất ba loại failure. **Transport failure** như timeout/offline thường xuất hiện qua `IOException`. **Protocol failure** như HTTP 401/404/500 vẫn là HTTP response hợp lệ nhưng không success. **Domain failure** có thể nằm trong JSON body dù status là 200 hoặc 4xx tùy backend contract.

Repository nên map các chi tiết này thành model mà caller hiểu thay vì để UI biết `SocketTimeoutException`, Retrofit response code và JSON error schema cùng lúc.

```kotlin
sealed interface LoadUserResult {
    data class Success(val user: User) : LoadUserResult
    data object Offline : LoadUserResult
    data object Unauthorized : LoadUserResult
    data class Failed(val cause: Throwable) : LoadUserResult
}
```

Không log access token, cookie, password hoặc payload PII trong production. Logging interceptor nên có policy theo build type và redaction.

# 8. Room: transaction, relation và source of truth

Room không chỉ là annotation quanh SQLite. Database là persistent source có constraint, transaction và migration. `@Transaction` đảm bảo nhóm operation cần atomicity được thực hiện như một unit. Với relationship, Room có `@Embedded`, `@Relation` và junction patterns, nhưng cần hiểu query cost thay vì tạo object graph rất lớn mỗi lần render.

Type converter phù hợp value nhỏ có mapping ổn định; đừng serialize cả domain object phức tạp vào một text column chỉ để tránh thiết kế schema. Làm vậy mất khả năng query/index và migration rõ ràng.

Repository offline-first thường để Room là local source of truth: network sync cập nhật DB, UI observe DB bằng Flow. Pattern này tránh hai nguồn state cạnh tranh giữa “network result đang nằm trong memory” và “database state”.

# 9. Compose state hoisting

**State hoisting** chuyển state lên owner phù hợp và composable con nhận `value` + event callback. Composable stateless dễ preview, reuse và test hơn.

```kotlin
@Composable
fun SearchBox(
    query: String,
    onQueryChange: (String) -> Unit
) {
    TextField(
        value = query,
        onValueChange = onQueryChange
    )
}
```

Không phải state nào cũng phải đưa vào ViewModel. State thuần visual, ngắn hạn và không ảnh hưởng business logic có thể ở local composition. State cần tồn tại qua screen recreation, chia sẻ giữa nhiều composable hoặc điều khiển data operation thường thuộc owner cao hơn.

# 10. Compose identity và key

Trong lazy list, key ổn định giúp Compose giữ đúng identity khi list reorder.

```kotlin
LazyColumn {
    items(items, key = { it.id }) { item ->
        ItemRow(item)
    }
}
```

Nếu dùng index làm identity trong list có insert/remove/reorder, remembered state có thể “đi theo vị trí” thay vì đúng item. Key nên ổn định và unique trong phạm vi cần thiết.

# 11. Effect API: `LaunchedEffect`, `DisposableEffect`, `rememberUpdatedState`, `snapshotFlow`

`LaunchedEffect(key)` khởi coroutine gắn với composition và restart khi key đổi. `DisposableEffect` dành cho resource/listener cần cleanup. `rememberUpdatedState` giữ reference mới nhất cho callback/value bên trong effect lâu sống mà không restart effect. `snapshotFlow` chuyển đọc Snapshot State thành Flow khi cần dùng operator của Flow.

```kotlin
@Composable
fun Timer(onTimeout: () -> Unit) {
    val latestOnTimeout by rememberUpdatedState(onTimeout)

    LaunchedEffect(Unit) {
        delay(5_000)
        latestOnTimeout()
    }
}
```

Sai lầm phổ biến là gọi network trực tiếp trong body composable. Body có thể chạy nhiều lần; side effect phải đi qua effect API hoặc ViewModel/repository owner phù hợp.

# 12. Test double: fake khác mock

Test double gồm fake, stub, spy, mock. Fake thường là implementation nhẹ nhưng hoạt động thật trong memory, rất phù hợp repository/data source vì test ít phụ thuộc interaction detail.

```kotlin
class FakeUserRepository(
    private var user: User? = null
) : UserRepository {
    override suspend fun load(): User = requireNotNull(user)
}
```

Mock useful khi cần verify interaction quan trọng, nhưng mock mọi object khiến test gắn chặt implementation. Test nên ưu tiên contract/observable behavior.

# 13. Coroutine testing bằng virtual time

`kotlinx-coroutines-test` cung cấp test dispatcher/scheduler để điều khiển virtual time. `runTest` giúp test suspend code mà không `Thread.sleep`.

```kotlin
@Test
fun load_success_updates_state() = runTest {
    val repo = FakeUserRepository(User(1))
    val vm = UserViewModel(repo)

    advanceUntilIdle()

    assertEquals(
        UserUiState.Content(User(1)),
        vm.uiState.value
    )
}
```

Với Flow nhiều emission, có thể collect thủ công hoặc dùng library như Turbine nếu project chấp nhận dependency. Điều quan trọng là assertion theo contract emission/order/completion chứ không sleep “đợi một chút”.

# 14. DI scope và lifetime

Dependency Injection không chỉ là “Hilt tạo object giúp”. Scope phải khớp lifetime. Singleton dùng cho object thực sự toàn process như database/client thường hợp lý; object chứa state của một Activity/feature không nên vô tình trở thành singleton.

Constructor injection làm dependency rõ nhất và dễ test. Field injection chỉ nên dùng ở Android framework entry point nơi bạn không kiểm soát constructor. Service locator/global singleton che dependency và khiến test setup khó suy luận.

# 15. Navigation result, deep link và state restoration

Navigation không chỉ là đổi màn hình. Route phải có contract input, ownership state và behavior khi process recreation. Tránh truyền object lớn trong route; truyền stable ID rồi load dữ liệu từ source of truth thường an toàn hơn.

Deep link là external input. Mọi parameter từ URL phải validate như dữ liệu không tin cậy. Không cho rằng link được tạo bởi app của bạn thì luôn hợp lệ.

Khi màn hình B trả result cho A, có thể dùng `SavedStateHandle`, navigation entry hoặc shared state owner tùy architecture. Đừng biến global singleton thành event bus chỉ để tránh thiết kế result contract.

# 16. Process death là một test case thiết kế

Configuration change và process death khác nhau. ViewModel sống qua configuration change nhưng không sống nếu process bị kill. Những thứ cần khôi phục phải đến từ saved state, database/file hoặc backend. Nếu screen chỉ đúng khi process chưa từng bị kill, architecture vẫn còn phụ thuộc memory state quá nhiều.

Một test thực tế là bật **Don't keep activities** để phát hiện một số lỗi lifecycle, nhưng nó không mô phỏng đầy đủ process death. Cần kiểm tra restore path thật của navigation, form state và source of truth.

# 17. Checklist hoàn thiện Intermediate

Ở cuối phần này, bạn nên giải thích được Job hierarchy, supervision, dispatcher/cancellation, Flow cold-hot/context, `stateIn`/`shareIn`, callback adaptation, resource cleanup, network error model, Room transaction/source-of-truth, Compose state hoisting/effect, test double/coroutine test, DI scope và navigation contract. Mục tiêu không phải biết tên thư viện, mà biết lifetime và failure semantics của từng abstraction.
