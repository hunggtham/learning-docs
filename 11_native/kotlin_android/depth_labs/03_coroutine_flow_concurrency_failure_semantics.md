# Depth Lab 03 — Coroutine, Flow, Concurrency và Failure Semantics

Coroutine giúp code bất đồng bộ dễ đọc hơn, nhưng việc code trông giống synchronous code không có nghĩa concurrency trở nên đơn giản. Senior Android developer cần hiểu **lifetime, cancellation, structured concurrency, context, race condition, backpressure và failure propagation** đủ sâu để giải thích được behavior thay vì chỉ thuộc `launch`, `async`, `flowOn` hay `stateIn`.

Depth Lab này tập trung vào semantic phía sau API.

---

## 1. Coroutine không phải thread

Coroutine là một computation có thể suspend và resume. Thread là execution resource của runtime/OS.

Một coroutine có thể:

```text
start trên Main
suspend
resume trên Main
withContext(IO)
chạy blocking work trên IO thread
suspend
quay lại Main
```

` suspend ` không tự động đồng nghĩa “chạy background”.

Ví dụ:

```kotlin
suspend fun parseJson(input: String): Model {
    return heavyParser.parse(input)
}
```

Nếu caller gọi hàm này trên Main và `heavyParser.parse()` CPU-bound, UI vẫn bị block.

Main-safe contract cần explicit:

```kotlin
suspend fun parseJson(input: String): Model =
    withContext(defaultDispatcher) {
        heavyParser.parse(input)
    }
```

---

## 2. Structured concurrency là ownership model

Một coroutine không nên “trôi tự do”. Nó cần owner.

```text
viewModelScope -> screen/application state work
lifecycleScope -> lifecycle-bound UI work
coroutineScope {} -> child work owned by current operation
supervisorScope {} -> child failures isolated theo policy
WorkManager -> durable scheduled work
```

Nếu code dùng:

```kotlin
GlobalScope.launch { ... }
```

câu hỏi lập tức là:

```text
ai chịu trách nhiệm cancel?
ai quan sát failure?
operation có còn hợp lệ khi screen/app state thay đổi không?
```

GlobalScope thường phá ownership chain.

---

## 3. Job tree là failure tree

Ví dụ:

```kotlin
viewModelScope.launch {
    launch { loadProfile() }
    launch { loadFeed() }
}
```

Nếu parent dùng regular `Job`, child failure có thể cancel sibling và parent tùy scope hierarchy.

Hãy hình dung:

```text
Parent Job
├── Child A
└── Child B
```

Failure propagation không phải detail nhỏ; nó chính là policy “các task này sống/chết cùng nhau hay độc lập?”.

---

## 4. `coroutineScope` và `supervisorScope` encode hai business semantics khác nhau

### `coroutineScope`

Dùng khi các child cùng tạo thành **một operation nguyên khối**.

Ví dụ generate report cần cả user + transactions:

```kotlin
suspend fun buildReport(): Report = coroutineScope {
    val user = async { loadUser() }
    val tx = async { loadTransactions() }
    Report(user.await(), tx.await())
}
```

Nếu một phần fail, report không hoàn chỉnh; cancel sibling là hợp lý.

### `supervisorScope`

Dùng khi child độc lập và failure một child không nên hủy child khác.

Ví dụ home dashboard có weather card + recommendation + promo:

```kotlin
supervisorScope {
    launch { loadWeatherSafely() }
    launch { loadRecommendationsSafely() }
    launch { loadPromoSafely() }
}
```

Chọn scope phải xuất phát từ business relationship, không phải “cái nào ít crash hơn”.

---

## 5. Cancellation là control flow, không phải error bình thường

Coroutine cancellation thường được biểu diễn bởi `CancellationException`.

Code nguy hiểm:

```kotlin
try {
    repository.load()
} catch (t: Throwable) {
    logger.error(t)
    emit(UiState.Error)
}
```

`Throwable` bắt luôn cancellation. Coroutine có thể tiếp tục chạy logic không mong muốn.

Tốt hơn:

```kotlin
try {
    repository.load()
} catch (ce: CancellationException) {
    throw ce
} catch (t: Throwable) {
    logger.error(t)
}
```

Hoặc bắt type error hẹp hơn.

Mental rule:

> cancellation không phải “request failed”; cancellation nghĩa operation không còn được yêu cầu tiếp tục.

---

## 6. Cleanup khi cancellation cần phân biệt suspend và non-suspend

`finally` vẫn chạy khi coroutine bị cancel:

```kotlin
try {
    useResource()
} finally {
    resource.close()
}
```

Nếu cleanup cần gọi suspend function:

```kotlin
finally {
    withContext(NonCancellable) {
        releaseRemoteLease()
    }
}
```

Nhưng `NonCancellable` phải dùng hẹp. Nếu bọc một network operation dài, cancellation mất ý nghĩa và app có thể giữ work sống quá lâu.

---

## 7. `async` không phải cách chung để “chạy background”

`async` tạo `Deferred<T>` và dành cho concurrent computation có result.

Bad smell:

```kotlin
viewModelScope.async {
    repository.refresh()
}
```

nếu không bao giờ `await`, failure có thể bị xử lý khó đoán và intent code không rõ.

Nếu chỉ fire child operation dưới scope:

```kotlin
viewModelScope.launch {
    repository.refresh()
}
```

Nếu cần hai result concurrent:

```kotlin
coroutineScope {
    val a = async { loadA() }
    val b = async { loadB() }
    combine(a.await(), b.await())
}
```

---

## 8. Concurrency không tự động tăng performance

Hai task CPU-bound chạy concurrent trên limited cores có thể cạnh tranh cache/CPU.

Hai database writes concurrent có thể serialize ở database lock.

Hai HTTP requests concurrent có thể tốt, nhưng nếu server rate-limit hoặc radio wake-up cost cao thì không phải lúc nào càng nhiều càng nhanh.

Concurrency là tool để overlap work có thể overlap, không phải optimization mặc định.

---

## 9. Dispatcher injection là testability + policy boundary

Đừng hard-code:

```kotlin
withContext(Dispatchers.IO) { ... }
```

khắp code nếu cần deterministic test.

Có thể inject:

```kotlin
class ArticleRepository(
    private val ioDispatcher: CoroutineDispatcher
)
```

Test dùng `StandardTestDispatcher` hoặc dispatcher phù hợp.

Dispatcher injection cũng làm execution policy explicit.

---

## 10. `Dispatchers.IO` không phải “thread pool vô hạn”

IO dispatcher được tối ưu cho blocking I/O, nhưng app vẫn nên tránh tạo unbounded blocking work.

Nếu import 50.000 file và mỗi file launch một coroutine blocking:

```kotlin
files.map { file -> async(ioDispatcher) { parse(file) } }
```

có thể gây memory pressure, file descriptor pressure và contention.

Bound concurrency:

```kotlin
val semaphore = Semaphore(8)

files.map { file ->
    async {
        semaphore.withPermit {
            parse(file)
        }
    }
}.awaitAll()
```

Concurrency limit là capacity planning.

---

## 11. Mutex bảo vệ critical section trong coroutine world

Giả sử token refresh:

```text
20 request cùng nhận 401
```

Nếu mỗi request refresh token riêng, server nhận 20 refresh calls.

Single-flight pattern:

```kotlin
private val refreshMutex = Mutex()

suspend fun getValidToken(): Token = refreshMutex.withLock {
    val current = tokenStore.read()
    if (current.isStillValid()) return current

    val refreshed = api.refresh(current.refreshToken)
    tokenStore.write(refreshed)
    refreshed
}
```

Nhưng critical section phải ngắn và semantic rõ. Mutex không biến shared mutable state thành design tốt tự động.

---

## 12. Atomic operation khác Mutex

Nếu chỉ cần compare-and-set một primitive state, atomic có thể phù hợp.

Nếu invariant liên quan nhiều field hoặc suspend operation, Mutex/transaction có thể cần thiết.

Ví dụ invariant:

```text
currentToken và tokenExpiry phải thay đổi cùng nhau
```

Hai atomic riêng không nhất thiết bảo vệ pair invariant.

---

## 13. Actor/Channel giúp serialize command khi ordering quan trọng

Một state machine có thể nhận command:

```text
Connect
Disconnect
Send
Retry
```

Thay vì nhiều coroutine mutate shared state, một event loop serialize command:

```kotlin
for (command in commands) {
    reduce(command)
}
```

Đây là actor-like model. Nó giảm race vì có single writer.

Trade-off là cần xử lý queue/backpressure/shutdown rõ ràng.

---

## 14. Cold Flow là recipe, không phải running stream

```kotlin
val flow = flow {
    emit(api.load())
}
```

Chưa chạy gì cho tới khi collect.

Mỗi collector có thể chạy upstream riêng.

Nếu 5 collector collect một cold flow gọi network, có thể tạo 5 request.

Hãy hỏi:

```text
upstream nên chạy per collector hay shared?
```

---

## 15. Hot Flow cần lifetime owner

`StateFlow` và `SharedFlow` có thể sống lâu hơn collector.

Khi convert:

```kotlin
repository.observe()
    .stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(5_000),
        initialValue = ...
    )
```

ba quyết định quan trọng là:

```text
scope nào sở hữu upstream?
khi nào upstream start/stop?
initial/replay semantics gì?
```

`stateIn` không chỉ là convenience conversion.

---

## 16. `SharingStarted.WhileSubscribed` là resource policy

Nếu upstream là Room Flow, giữ một khoảng stop timeout có thể tránh stop/start liên tục khi configuration change ngắn.

Nếu upstream là GPS sensor, giữ thêm 5 giây có thể tốn pin không cần thiết.

Cùng một operator nhưng resource cost khác.

Started policy phải dựa vào upstream semantics.

---

## 17. `flowOn` đổi context phía upstream

Mental model:

```kotlin
flow {
    // upstream
}
    .map { ... }
    .flowOn(ioDispatcher)
    .collect {
        // collector context
    }
```

`flowOn` tác động phần upstream trước nó, không ép collector chạy IO.

Việc hiểu context preservation giúp tránh đặt heavy mapping ở sai phía.

---

## 18. `collectLatest` encode cancellation policy

Search-as-you-type:

```kotlin
queryFlow.collectLatest { query ->
    render(repository.search(query))
}
```

Khi query mới tới, block cũ bị cancel.

Điều này chỉ đúng nếu result cũ không còn giá trị.

Không dùng `collectLatest` cho operation không được phép cancel giữa chừng như commit local transaction phức tạp nếu cancellation safety chưa rõ.

---

## 19. `flatMapLatest` bảo vệ stale-request race

```kotlin
query
    .debounce(300)
    .flatMapLatest { repository.search(it) }
```

Query mới cancel upstream search cũ.

Invariant được bảo vệ:

```text
result của query cũ không được trở thành state hiện tại sau query mới
```

Operator là implementation của invariant.

---

## 20. `buffer` thay đổi producer-consumer coupling

Không buffer:

```text
producer emit -> chờ consumer xử lý -> emit tiếp
```

Có buffer:

```text
producer có thể chạy trước consumer một khoảng
```

Điều này tăng throughput khi producer và consumer có thể overlap, nhưng cũng tăng memory và stale work.

Đừng thêm `buffer()` chỉ vì “performance”. Hãy biết queue size và drop semantics.

---

## 21. `conflate` bỏ intermediate value

Dùng khi chỉ state mới nhất quan trọng.

Ví dụ progress 1%, 2%, 3%, ... 90% mà UI render chậm, có thể không cần render mọi bước.

Nhưng không dùng cho event stream mà mỗi item đều quan trọng như transaction event.

State stream và event stream có loss tolerance khác nhau.

---

## 22. `SharedFlow` không tự động là event bus tốt

Một global shared flow cho mọi one-off event dễ tạo hidden dependency.

Các câu hỏi cần trả lời:

```text
replay bao nhiêu?
buffer capacity?
onBufferOverflow?
collector inactive thì event mất được không?
multiple collector có cùng nhận không?
```

Nếu event không được phép mất, có thể nó nên là durable state hoặc queue chứ không phải ephemeral SharedFlow.

---

## 23. `Channel` có queue semantics rõ hơn cho point-to-point event

Channel phù hợp khi event cần được consume bởi một consumer theo queue semantics.

Nhưng channel nằm in-memory; process death vẫn làm event mất.

Vì vậy notification “payment succeeded” quan trọng có thể nên reconstruct từ persisted transaction state thay vì chờ một Channel event.

---

## 24. Callback -> `callbackFlow` cần cleanup chính xác

Ví dụ listener API:

```kotlin
fun observeLocation(): Flow<Location> = callbackFlow {
    val listener = LocationListener { location ->
        trySend(location)
    }

    provider.register(listener)

    awaitClose {
        provider.unregister(listener)
    }
}
```

Nếu quên `awaitClose`, listener leak sau collector cancel.

Callback lifetime phải map đúng vào Flow collection lifetime.

---

## 25. Backpressure ở callbackFlow cần policy

Sensor có thể emit 100Hz nhưng consumer xử lý 10Hz.

Cần quyết định:

```text
buffer bao nhiêu?
drop oldest?
drop latest?
conflate?
```

Nếu telemetry cho UI, latest có thể đủ. Nếu dữ liệu scientific capture, drop có thể không chấp nhận.

---

## 26. `repeatOnLifecycle` bảo vệ collection lifetime

UI không nên collect flow vô điều kiện khi lifecycle không active.

Compose thường dùng:

```kotlin
collectAsStateWithLifecycle()
```

View system có thể dùng `repeatOnLifecycle`.

Mục tiêu không phải thuộc API mà là tránh:

```text
UI không visible nhưng vẫn xử lý/render stream
```

và tránh manual start/stop dễ leak.

---

## 27. Race giữa refresh và local mutation

Timeline:

```text
T0 refresh request bắt đầu
T1 user bookmark locally
T2 server response của refresh chứa bookmark=false từ snapshot cũ
T3 refresh ghi toàn row -> bookmark local bị mất
```

Đây không phải coroutine bug; đây là merge semantics bug.

Fix có thể là:

- remote refresh không overwrite local-only field,
- field versioning,
- separate table,
- pending mutation overlay.

Concurrency operator không thay thế data merge policy.

---

## 28. Race giữa logout và in-flight request

```text
T0 account A request start
T1 logout A
T2 login B
T3 response A về
T4 repository ghi DB dùng current account B
```

Cần session/account identity capture và verify trước commit.

Cancellation request cũ giúp nhưng không đủ vì remote response có thể vẫn race. Business guard phải tồn tại.

---

## 29. Race giữa process lifecycle và callback

Một callback có thể về sau Activity destroyed.

Nếu callback giữ Activity reference hoặc trực tiếp mutate View, leak/crash dễ xảy ra.

State nên đi qua lifecycle-aware owner; callback registration cleanup theo lifecycle/resource owner.

---

## 30. Timeout cần ở boundary đúng

```kotlin
withTimeout(5_000) {
    wholeCheckoutFlow()
}
```

có thể sai nếu checkout gồm nhiều step hợp lệ lâu hơn 5s.

Timeout nên reflect SLA của boundary cụ thể:

```text
DNS/connect timeout
HTTP request timeout
BLE operation timeout
user interaction không nên dùng network timeout
```

Một timeout global dễ cancel operation ở điểm không an toàn.

---

## 31. Retry trong Flow cần phân loại error

```kotlin
flow.retry(3)
```

quá thô nếu mọi error đều retry.

Tốt hơn:

```kotlin
.retryWhen { cause, attempt ->
    cause is IOException && attempt < 3
}
```

HTTP validation error không nên retry như connectivity error.

---

## 32. Flow exception transparency

Flow convention yêu cầu upstream exception không bị nuốt hoặc emit tùy tiện từ nơi không phù hợp.

`catch` chỉ catch upstream trước nó.

Mental model:

```kotlin
source
    .map { ... }
    .catch { ... }   // catch source/map error
    .collect { ... } // collector error không bị catch ở trên
```

Hiểu boundary của operator giúp debug exception propagation.

---

## 33. CPU cancellation cooperative

Một loop CPU dài không suspend có thể không phản ứng cancellation nhanh:

```kotlin
for (item in hugeList) {
    heavyCompute(item)
}
```

Có thể cần:

```kotlin
for (item in hugeList) {
    ensureActive()
    heavyCompute(item)
}
```

hoặc chunk/yield hợp lý.

Cancellation responsiveness là phần của UX/resource correctness.

---

## 34. Blocking library trong coroutine vẫn block thread

Nếu SDK Java cũ có:

```kotlin
legacyClient.blockingCall()
```

bọc trong `suspend fun` không biến nó non-blocking.

Phải chuyển dispatcher hoặc dùng async API nếu có.

Suspending abstraction không thay đổi bản chất underlying I/O.

---

## 35. Test coroutine phải kiểm soát scheduler

Dùng test dispatcher cho phép:

```text
advance time
run queued tasks
assert intermediate state
```

Ví dụ debounce:

```kotlin
runTest {
    viewModel.onQuery("kot")
    advanceTimeBy(299)
    assertEquals(0, repo.searchCount)

    advanceTimeBy(1)
    runCurrent()
    assertEquals(1, repo.searchCount)
}
```

Không dùng `Thread.sleep()` trong deterministic coroutine test.

---

## 36. Test cancellation, không chỉ success

Một repository có thể pass happy path nhưng leak resource khi cancel.

Test:

```text
collector start
callback register
collector cancel
assert callback unregister
```

Hoặc:

```text
request start
screen leaves
job cancel
assert stale result không commit
```

Cancellation path là first-class behavior.

---

## 37. Debug coroutine bằng ownership graph

Khi gặp “coroutine vẫn chạy”, đừng chỉ log thread name.

Hỏi:

```text
Job parent là ai?
Scope sống bao lâu?
Child có được cancel không?
Có NonCancellable không?
Có callback external giữ reference không?
Flow upstream shared ở scope nào?
```

Ownership graph thường giải thích bug nhanh hơn thread dump đơn thuần.

---

## 38. Concurrency design checklist

| Câu hỏi | Ý nghĩa |
|---|---|
| Operation owner là ai? | scope/lifetime |
| Child sống chết cùng nhau không? | coroutineScope/supervision |
| Cancellation có được propagate không? | structured concurrency |
| Shared state có single writer không? | race control |
| Retry có idempotent không? | duplicate effect |
| Upstream cold hay hot? | duplicate work/resource |
| Collector chậm thì sao? | backpressure |
| Event có được phép mất không? | state vs queue |
| External callback cleanup ở đâu? | leak prevention |
| Test scheduler kiểm soát được không? | determinism |

---

## 39. Kết luận

Coroutine và Flow mạnh vì chúng cho phép biểu diễn lifetime và data stream bằng cấu trúc rõ hơn callback truyền thống. Nhưng correctness chỉ có khi developer hiểu semantic phía sau API.

Mental model nên giữ:

```text
owner
-> Job tree
-> execution context
-> cancellation
-> shared-state policy
-> stream temperature
-> backpressure
-> failure/retry semantics
-> cleanup
-> deterministic test
```

Khi những điểm này rõ, việc chọn `launch`, `async`, `stateIn`, `flatMapLatest`, `Mutex` hay `callbackFlow` trở thành quyết định có lý do thay vì pattern copy từ sample.