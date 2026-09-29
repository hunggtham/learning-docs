# Kotlin + Android Intermediate — Completion Deep Dive

> **Mạch đọc:** Đọc **Kotlin + Android Intermediate — Completion Deep Dive** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Hãy xác định đối tượng và câu hỏi trung tâm trước, rồi dùng phần này để đối chiếu với mục liên quan sau khi đã nắm mô hình tư duy (mental model / 사고 모델) chính.


> tệp (file / 파일) này bổ sung cho [`../02_kotlin_intermediate.md`](../02_kotlin_intermediate.md). Mục tiêu là làm rõ những phần thường bị tutorial rút gọn: CoroutineContext/Job hierarchy, luồng (flow / 흐름) ngữ cảnh (context / 맥락) và hot/cold conversion, tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명), mạng (network / 네트워크) lỗi (error / 오류) mô hình (model / 모델), Room như nguồn chuẩn (source of truth / 정본), Compose trạng thái (state / 상태)/tác động (effect / 효과), coroutine testing, DI phạm vi (scope / 범위) và điều hướng (navigation / 내비게이션) đặc tả hợp đồng (contract / 계약).

# 1. Coroutine ngữ cảnh (context / 맥락), dispatcher và Job hierarchy

Một coroutine không chỉ có đoạn mã (code / 코드) `suspend`; nó chạy trong **CoroutineContext** gồm các element như `Job`, `CoroutineDispatcher`, `CoroutineName` và đôi khi exception handler. `Job` tạo cây quyền sở hữu (ownership / 소유권); dispatcher quyết định nơi continuation được schedule. Đây là lý do structured tính đồng thời (concurrency / 동시성) quan trọng: child coroutine thuộc vòng đời (lifecycle / 생명주기) của phạm vi (scope / 범위) thay vì trở thành công việc vô chủ.

```kotlin
viewModelScope.launch {
    val user = withContext(ioDispatcher) {
        repository.loadUser()
    }
    _uiState.value = UiState.Content(user)
}
```

`Dispatchers.Main` dùng cho UI; `Dispatchers.IO` tối ưu cho blocking I/O; `Dispatchers.Default` dành cho CPU-bound công việc (work / 작업). Tuy nhiên thư viện suspend tốt thường tự quản ngữ cảnh (context / 맥락) phù hợp. Không cần bọc mọi Retrofit suspend lời gọi (call / 호출) bằng `withContext(Dispatchers.IO)` theo thói quen nếu máy khách (client / 클라이언트) đã non-blocking.

`coroutineScope` tạo phạm vi (scope / 범위) con và thất bại (fail / 실패) cùng child; `supervisorScope` ngăn thất bại (failure / 실패) của một child tự động cancel sibling. `SupervisorJob` có ngữ nghĩa (semantics / 의미론) tương tự ở Job hierarchy. Chọn supervision dựa trên quan hệ lỗi thực tế: hai yêu cầu (request / 요청) bắt buộc cùng thành công nên thất bại (fail / 실패) together; hai widget độc lập có thể supervise riêng.

Cancellation cooperative. `delay`, luồng (flow / 흐름) và nhiều suspend API kiểm tra cancellation; CPU vòng lặp (loop / 루프) dài phải tự kiểm tra `ensureActive()` hoặc `yield()` nếu cần responsive cancellation. Không nuốt `CancellationException` trong `catch (Exception)` rồi tiếp tục như bình thường.

# 2. `launch`, `async`, `withContext` và parallelism có chủ đích

`launch` trả `Job` và phù hợp công việc không cần return giá trị (value / 값) trực tiếp. `async` trả `Deferred<T>` và chỉ có giá trị khi thực sự cần concurrent computation rồi `await`. Dùng `async` cho mọi suspend lời gọi (call / 호출) chỉ làm vòng đời (lifecycle / 생명주기)/lỗi (error / 오류) phức tạp hơn.

```kotlin
suspend fun loadDashboard(): Dashboard = coroutineScope {
    val user = async { userRepository.load() }
    val alerts = async { alertRepository.load() }
    Dashboard(user.await(), alerts.await())
}
```

Ví dụ trên chỉ có lợi khi hai thao tác (operation / 연산) độc lập và có thể chạy song song. Nếu `alerts` cần người dùng (user / 사용자) ID từ yêu cầu (request / 요청) đầu, chạy parallel là sai phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프).

# 3. luồng (flow / 흐름) cold/hot và ngữ cảnh (context / 맥락) preservation

Một luồng (flow / 흐름) tạo bằng `flow {}` thường là **cold**: mỗi collector chạy lại producer. `StateFlow` và `SharedFlow` là hot: chúng tồn tại theo thời gian tồn tại (lifetime / 수명) của đơn vị sở hữu (owner / 오너) và collector chỉ subscribe vào stream đang tồn tại.

```kotlin
val uiState: StateFlow<UiState> = repository.observeNotes()
    .map { notes -> UiState.Content(notes) }
    .stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(5_000),
        initialValue = UiState.Loading
    )
```

Các operator cần hiểu theo ngữ nghĩa (semantics / 의미론). `map` transform; `filter` loại emission; `combine` tính giá trị (value / 값) từ emission mới nhất của nhiều upstream; `zip` ghép theo cặp emission; `debounce` chờ đầu vào (input / 입력) ổn định; `distinctUntilChanged` bỏ giá trị (value / 값) liên tiếp tương đương; `flatMapLatest` hủy luồng (flow / 흐름) cũ khi key mới đến, phù hợp tìm kiếm (search / 검색) truy vấn (query / 쿼리).

Luồng (flow / 흐름) có **ngữ cảnh (context / 맥락) preservation**. `flowOn(dispatcher)` đổi ngữ cảnh (context / 맥락) của upstream trước operator đó; collector vẫn chạy ngữ cảnh (context / 맥락) của collector. Không `withContext` tùy tiện quanh `emit` trong `flow {}` vì có thể vi phạm luồng (flow / 흐름) bất biến (invariant / 불변식).

# 4. `stateIn`, `shareIn` và `SharingStarted`

`stateIn` chuyển luồng (flow / 흐름) thành `StateFlow` và luôn có hiện tại (current / 현재) giá trị (value / 값). `shareIn` tạo `SharedFlow` dùng chung upstream. Hai API này tránh việc mỗi collector khởi động lại mạng (network / 네트워크)/cơ sở dữ liệu (database / 데이터베이스) chuỗi xử lý (pipeline / 파이프라인) đắt tiền, nhưng phạm vi (scope / 범위) và start chính sách (policy / 정책) phải đúng.

`SharingStarted.WhileSubscribed(...)` thường hợp UI vì upstream hoạt động khi có subscriber và có thể giữ một khoảng hết thời gian chờ (timeout / 타임아웃) để tránh stop/start liên tục khi cấu hình (configuration / 구성) thay đổi (change / 변경). `Eagerly` khởi ngay khi phạm vi (scope / 범위) tạo; `Lazily` đợi subscriber đầu tiên. Không bản sao (copy / 복사) `WhileSubscribed(5_000)` như magic number nếu sản phẩm (product / 제품)/vòng đời (lifecycle / 생명주기) yêu cầu (requirement / 요구사항) khác.

# 5. `callbackFlow` và cầu nối (bridge / 브리지) callback API

`callbackFlow` adapter một callback API thành luồng (flow / 흐름). Điều quan trọng nhất là cleanup callback bằng `awaitClose`; nếu quên unregister listener, leak có thể xuất hiện.

```kotlin
fun LocationClient.locations(): Flow<Location> = callbackFlow {
    val listener = LocationListener { location ->
        trySend(location)
    }

    register(listener)
    awaitClose { unregister(listener) }
}
```

Nếu callback có thể emit nhanh hơn collector, cần quyết định buffer/overflow ngữ nghĩa (semantics / 의미론) thay vì mặc định giả định mọi sự kiện (event / 이벤트) đều được xử lý kịp.

# 6. tài nguyên (resource / 자원) management và `use`

Một số tài nguyên (resource / 자원) như stream, cursor, tệp (file / 파일) descriptor phải được đóng dù success hay exception. Kotlin cung cấp `use`, tương tự try-with-resources.

```kotlin
contentResolver.openInputStream(uri)?.use { input ->
    val bytes = input.readBytes()
}
```

Không đóng tài nguyên (resource / 자원) là bug vòng đời (lifecycle / 생명주기)/tài nguyên (resource / 자원) leak, khác với garbage collection. GC có thể thu đối tượng (object / 객체) nhưng không đảm bảo bản phát hành (release / 릴리스) tài nguyên hệ điều hành đúng thời điểm.

# 7. mạng (network / 네트워크) tầng (layer / 계층): vận chuyển (transport / 전송), giao thức (protocol / 프로토콜) và lĩnh vực (domain / 도메인) lỗi (error / 오류)

Retrofit mô tả HTTP API; OkHttp thực hiện vận chuyển (transport / 전송) phổ biến trong Android ngăn xếp (stack / 스택). Một mạng (network / 네트워크) tầng (layer / 계층) môi trường vận hành (production / 운영 환경) cần hết thời gian chờ (timeout / 타임아웃), authentication, logging an toàn, cancellation và lỗi (error / 오류) ánh xạ (mapping / 매핑) rõ ràng.

Cần tách ít nhất ba loại thất bại (failure / 실패). **vận chuyển (transport / 전송) thất bại (failure / 실패)** như hết thời gian chờ (timeout / 타임아웃)/offline thường xuất hiện qua `IOException`. **giao thức (protocol / 프로토콜) thất bại (failure / 실패)** như HTTP 401/404/500 vẫn là HTTP phản hồi (response / 응답) hợp lệ nhưng không success. **lĩnh vực (domain / 도메인) thất bại (failure / 실패)** có thể nằm trong JSON body dù status là 200 hoặc 4xx tùy backend đặc tả hợp đồng (contract / 계약).

Repository nên map các chi tiết này thành mô hình (model / 모델) mà caller hiểu thay vì để UI biết `SocketTimeoutException`, Retrofit phản hồi (response / 응답) mã (code / 코드) và JSON lỗi (error / 오류) lược đồ (schema / 스키마) cùng lúc.

```kotlin
sealed interface LoadUserResult {
    data class Success(val user: User) : LoadUserResult
    data object Offline : LoadUserResult
    data object Unauthorized : LoadUserResult
    data class Failed(val cause: Throwable) : LoadUserResult
}
```

Không log truy cập (access / 접근) đơn vị từ (token / 토큰), cookie, password hoặc payload PII trong môi trường vận hành (production / 운영 환경). Logging interceptor nên có chính sách (policy / 정책) theo bản dựng (build / 빌드) kiểu (type / 타입) và redaction.

# 8. Room: giao dịch (transaction / 트랜잭션), quan hệ (relation / 관계) và nguồn chuẩn (source of truth / 정본)

Room không chỉ là annotation quanh SQLite. cơ sở dữ liệu (database / 데이터베이스) là persistent nguồn (source / 소스) có ràng buộc (constraint / 제약조건), giao dịch (transaction / 트랜잭션) và di chuyển (migration / 마이그레이션). `@Transaction` đảm bảo nhóm thao tác (operation / 연산) cần atomicity được thực hiện như một đơn vị (unit / 단위). Với relationship, Room có `@Embedded`, `@Relation` và junction patterns, nhưng cần hiểu truy vấn (query / 쿼리) chi phí (cost / 비용) thay vì tạo đối tượng (object / 객체) đồ thị (graph / 그래프) rất lớn mỗi lần kết xuất (render / 렌더링).

Kiểu (type / 타입) converter phù hợp giá trị (value / 값) nhỏ có ánh xạ (mapping / 매핑) ổn định; đừng serialize cả lĩnh vực (domain / 도메인) đối tượng (object / 객체) phức tạp vào một văn bản (text / 텍스트) column chỉ để tránh thiết kế lược đồ (schema / 스키마). Làm vậy mất khả năng truy vấn (query / 쿼리)/chỉ mục (index / 인덱스) và di chuyển (migration / 마이그레이션) rõ ràng.

Repository offline-first thường để Room là cục bộ (local / 로컬) nguồn chuẩn (source of truth / 정본): mạng (network / 네트워크) sync cập nhật DB, UI observe DB bằng luồng (flow / 흐름). mẫu (pattern / 패턴) này tránh hai nguồn trạng thái (state / 상태) cạnh tranh giữa “mạng (network / 네트워크) kết quả (result / 결과) đang nằm trong bộ nhớ (memory / 메모리)” và “cơ sở dữ liệu (database / 데이터베이스) trạng thái (state / 상태)”.

# 9. Compose trạng thái (state / 상태) hoisting

**trạng thái (state / 상태) hoisting** chuyển trạng thái (state / 상태) lên đơn vị sở hữu (owner / 오너) phù hợp và composable con nhận `value` + sự kiện (event / 이벤트) callback. Composable stateless dễ preview, reuse và kiểm thử (test / 테스트) hơn.

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

Không phải trạng thái (state / 상태) nào cũng phải đưa vào ViewModel. trạng thái (state / 상태) thuần visual, ngắn hạn và không ảnh hưởng lô-gic nghiệp vụ (business logic / 비즈니스 로직) có thể ở cục bộ (local / 로컬) composition. trạng thái (state / 상태) cần tồn tại qua screen recreation, chia sẻ giữa nhiều composable hoặc điều khiển dữ liệu (data / 데이터) thao tác (operation / 연산) thường thuộc đơn vị sở hữu (owner / 오너) cao hơn.

# 10. Compose định danh (identity / 식별자) và key

Trong lazy danh sách (list / 목록), key ổn định giúp Compose giữ đúng định danh (identity / 식별자) khi danh sách (list / 목록) reorder.

```kotlin
LazyColumn {
    items(items, key = { it.id }) { item ->
        ItemRow(item)
    }
}
```

Nếu dùng chỉ mục (index / 인덱스) làm định danh (identity / 식별자) trong danh sách (list / 목록) có insert/remove/reorder, remembered trạng thái (state / 상태) có thể “đi theo vị trí” thay vì đúng item. Key nên ổn định và unique trong phạm vi cần thiết.

# 11. tác động (effect / 효과) API: `LaunchedEffect`, `DisposableEffect`, `rememberUpdatedState`, `snapshotFlow`

`LaunchedEffect(key)` khởi coroutine gắn với composition và restart khi key đổi. `DisposableEffect` dành cho tài nguyên (resource / 자원)/listener cần cleanup. `rememberUpdatedState` giữ tham chiếu (reference / 참조) mới nhất cho callback/giá trị (value / 값) bên trong tác động (effect / 효과) lâu sống mà không restart tác động (effect / 효과). `snapshotFlow` chuyển đọc Snapshot trạng thái (state / 상태) thành luồng (flow / 흐름) khi cần dùng operator của luồng (flow / 흐름).

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

Sai lầm phổ biến là gọi mạng (network / 네트워크) trực tiếp trong body composable. Body có thể chạy nhiều lần; side tác động (effect / 효과) phải đi qua tác động (effect / 효과) API hoặc ViewModel/repository đơn vị sở hữu (owner / 오너) phù hợp.

# 12. kiểm thử (test / 테스트) double: fake khác mock

Kiểm thử (test / 테스트) double gồm fake, stub, spy, mock. Fake thường là hiện thực (implementation / 구현) nhẹ nhưng hoạt động thật trong bộ nhớ (memory / 메모리), rất phù hợp repository/dữ liệu (data / 데이터) nguồn (source / 소스) vì kiểm thử (test / 테스트) ít phụ thuộc tương tác (interaction / 상호작용) detail.

```kotlin
class FakeUserRepository(
    private var user: User? = null
) : UserRepository {
    override suspend fun load(): User = requireNotNull(user)
}
```

Mock useful khi cần verify tương tác (interaction / 상호작용) quan trọng, nhưng mock mọi đối tượng (object / 객체) khiến kiểm thử (test / 테스트) gắn chặt hiện thực (implementation / 구현). kiểm thử (test / 테스트) nên ưu tiên đặc tả hợp đồng (contract / 계약)/observable hành vi (behavior / 동작).

# 13. Coroutine testing bằng virtual thời gian (time / 시간)

`kotlinx-coroutines-test` cung cấp kiểm thử (test / 테스트) dispatcher/scheduler để điều khiển virtual thời gian (time / 시간). `runTest` giúp kiểm thử (test / 테스트) suspend mã (code / 코드) mà không `Thread.sleep`.

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

Với luồng (flow / 흐름) nhiều emission, có thể collect thủ công hoặc dùng thư viện (library / 라이브러리) như Turbine nếu dự án (project / 프로젝트) chấp nhận phụ thuộc (dependency / 의존성). Điều quan trọng là assertion theo đặc tả hợp đồng (contract / 계약) emission/thứ tự (order / 순서)/completion chứ không sleep “đợi một chút”.

# 14. DI phạm vi (scope / 범위) và thời gian tồn tại (lifetime / 수명)

Phụ thuộc (dependency / 의존성) Injection không chỉ là “Hilt tạo đối tượng (object / 객체) giúp”. phạm vi (scope / 범위) phải khớp thời gian tồn tại (lifetime / 수명). Singleton dùng cho đối tượng (object / 객체) thực sự toàn tiến trình (process / 프로세스) như cơ sở dữ liệu (database / 데이터베이스)/máy khách (client / 클라이언트) thường hợp lý; đối tượng (object / 객체) chứa trạng thái (state / 상태) của một Activity/tính năng (feature / 기능) không nên vô tình trở thành singleton.

Constructor injection làm phụ thuộc (dependency / 의존성) rõ nhất và dễ kiểm thử (test / 테스트). trường dữ liệu (field / 필드) injection chỉ nên dùng ở Android khung phần mềm (framework / 프레임워크) entry điểm (point / 지점) nơi bạn không kiểm soát constructor. dịch vụ (service / 서비스) locator/toàn cục (global / 전역) singleton che phụ thuộc (dependency / 의존성) và khiến kiểm thử (test / 테스트) setup khó suy luận.

# 15. điều hướng (navigation / 내비게이션) kết quả (result / 결과), deep link và trạng thái (state / 상태) restoration

Điều hướng (navigation / 내비게이션) không chỉ là đổi màn hình. tuyến (route / 경로) phải có đặc tả hợp đồng (contract / 계약) đầu vào (input / 입력), quyền sở hữu (ownership / 소유권) trạng thái (state / 상태) và hành vi (behavior / 동작) khi tiến trình (process / 프로세스) recreation. Tránh truyền đối tượng (object / 객체) lớn trong tuyến (route / 경로); truyền stable ID rồi tải (load / 로드) dữ liệu từ nguồn chuẩn (source of truth / 정본) thường an toàn hơn.

Deep link là bên ngoài (external / 외부) đầu vào (input / 입력). Mọi parameter từ URL phải validate như dữ liệu không tin cậy. Không cho rằng link được tạo bởi app của bạn thì luôn hợp lệ.

Khi màn hình B trả kết quả (result / 결과) cho A, có thể dùng `SavedStateHandle`, điều hướng (navigation / 내비게이션) entry hoặc trạng thái dùng chung (shared state / 공유 상태) đơn vị sở hữu (owner / 오너) tùy kiến trúc (architecture / 아키텍처). Đừng biến toàn cục (global / 전역) singleton thành sự kiện (event / 이벤트) bus chỉ để tránh thiết kế kết quả (result / 결과) đặc tả hợp đồng (contract / 계약).

# 16. tiến trình (process / 프로세스) death là một trường hợp kiểm thử (test case / 테스트 케이스) thiết kế

Cấu hình (configuration / 구성) thay đổi (change / 변경) và tiến trình (process / 프로세스) death khác nhau. ViewModel sống qua cấu hình (configuration / 구성) thay đổi (change / 변경) nhưng không sống nếu tiến trình (process / 프로세스) bị kill. Những thứ cần khôi phục phải đến từ saved trạng thái (state / 상태), cơ sở dữ liệu (database / 데이터베이스)/tệp (file / 파일) hoặc backend. Nếu screen chỉ đúng khi tiến trình (process / 프로세스) chưa từng bị kill, kiến trúc (architecture / 아키텍처) vẫn còn phụ thuộc bộ nhớ (memory / 메모리) trạng thái (state / 상태) quá nhiều.

Một kiểm thử (test / 테스트) thực tế là bật **Don't keep activities** để phát hiện một số lỗi vòng đời (lifecycle / 생명주기), nhưng nó không mô phỏng đầy đủ tiến trình (process / 프로세스) death. Cần kiểm tra restore đường dẫn (path / 경로) thật của điều hướng (navigation / 내비게이션), form trạng thái (state / 상태) và nguồn chuẩn (source of truth / 정본).

# 17. Checklist hoàn thiện Intermediate

Ở cuối phần này, bạn nên giải thích được Job hierarchy, supervision, dispatcher/cancellation, luồng (flow / 흐름) cold-hot/ngữ cảnh (context / 맥락), `stateIn`/`shareIn`, callback adaptation, tài nguyên (resource / 자원) cleanup, mạng (network / 네트워크) lỗi (error / 오류) mô hình (model / 모델), Room giao dịch (transaction / 트랜잭션)/source-of-truth, Compose trạng thái (state / 상태) hoisting/tác động (effect / 효과), kiểm thử (test / 테스트) double/coroutine kiểm thử (test / 테스트), DI phạm vi (scope / 범위) và điều hướng (navigation / 내비게이션) đặc tả hợp đồng (contract / 계약). Mục tiêu không phải biết tên thư viện, mà biết thời gian tồn tại (lifetime / 수명) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) của từng lớp trừu tượng (abstraction / 추상화).

> **Bàn giao:** Sau **Kotlin + Android Intermediate — Completion Deep Dive**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 beginner completion](./01_beginner_completion.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
