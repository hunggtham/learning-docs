# Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)

> **Mạch đọc:** [README](./README.md) là owner của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**; đặt lab sau architecture invariants và trước Compose/runtime. Từ **1. Coroutine không phải luồng thực thi (thread / 스레드)** nối structured concurrency/ownership, cancellation, dispatcher, Flow cold/hot, backpressure, races và failure propagation, rồi kiểm chứng bằng deterministic tests.

Coroutine giúp mã (code / 코드) bất đồng bộ dễ đọc hơn, nhưng việc mã (code / 코드) trông giống synchronous mã (code / 코드) không có nghĩa tính đồng thời (concurrency / 동시성) trở nên đơn giản. cấp cao (senior / 시니어) Android nhà phát triển (developer / 개발자) cần hiểu **thời gian tồn tại (lifetime / 수명), cancellation, structured tính đồng thời (concurrency / 동시성), ngữ cảnh (context / 맥락), race điều kiện (condition / 조건), backpressure và thất bại (failure / 실패) propagation** đủ sâu để giải thích được hành vi (behavior / 동작) thay vì chỉ thuộc `launch`, `async`, `flowOn` hay `stateIn`.

Độ sâu (depth / 깊이) Lab này tập trung vào ngữ nghĩa (semantic / 의미적) phía sau API.

---

## 1. Coroutine không phải luồng thực thi (thread / 스레드)

Coroutine là một computation có thể suspend và resume. luồng thực thi (thread / 스레드) là thực thi (execution / 실행) tài nguyên (resource / 자원) của thời gian chạy (runtime / 런타임)/OS.

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

Nếu caller gọi hàm này trên Main và `heavyParser.parse()` CPU-bound, UI vẫn bị khối (block / 블록).

Main-safe đặc tả hợp đồng (contract / 계약) cần tường minh (explicit / 명시적):

```kotlin
suspend fun parseJson(input: String): Model =
    withContext(defaultDispatcher) {
        heavyParser.parse(input)
    }
```

---

> **Nối mạch:** Trong **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, sau nội dung của **1. Coroutine không phải luồng thực thi (thread / 스레드)**, **2. Structured tính đồng thời (concurrency / 동시성) là quyền sở hữu (ownership / 소유권) mô hình (model / 모델)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **3. Job cây (tree / 트리) là thất bại (failure / 실패) cây (tree / 트리)** mở rộng hệ quả hoặc giới hạn liên quan.

## 2. Structured tính đồng thời (concurrency / 동시성) là quyền sở hữu (ownership / 소유권) mô hình (model / 모델)

Một coroutine không nên “trôi tự do”. Nó cần đơn vị sở hữu (owner / 오너).

```text
viewModelScope -> screen/application state work
lifecycleScope -> lifecycle-bound UI work
coroutineScope {} -> child work owned by current operation
supervisorScope {} -> child failures isolated theo policy
WorkManager -> durable scheduled work
```

Nếu mã (code / 코드) dùng:

```kotlin
GlobalScope.launch { ... }
```

câu hỏi lập tức là:

```text
ai chịu trách nhiệm cancel?
ai quan sát failure?
operation có còn hợp lệ khi screen/app state thay đổi không?
```

GlobalScope thường phá quyền sở hữu (ownership / 소유권) chuỗi (chain / 사슬).

---

> **Nối mạch:** Structured concurrency gắn child job với owner; Job tree vì vậy lan failure theo cấu trúc, còn `coroutineScope`/`supervisorScope` chọn hai semantics khác nhau.

## 3. Job cây (tree / 트리) là thất bại (failure / 실패) cây (tree / 트리)

Ví dụ:

```kotlin
viewModelScope.launch {
    launch { loadProfile() }
    launch { loadFeed() }
}
```

Nếu parent dùng regular `Job`, child thất bại (failure / 실패) có thể cancel sibling và parent tùy phạm vi (scope / 범위) hierarchy.

Hãy hình dung:

```text
Parent Job
├── Child A
└── Child B
```

Thất bại (failure / 실패) propagation không phải detail nhỏ; nó chính là chính sách (policy / 정책) “các tác vụ (task / 작업) này sống/chết cùng nhau hay độc lập?”.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **4. coroutineScope và supervisorScope encode hai nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론) khác nhau** nối từ **3. Job cây (tree / 트리) là thất bại (failure / 실패) cây (tree / 트리)** sang **5. Cancellation là điều khiển (control / 제어) luồng (flow / 흐름), không phải lỗi (error / 오류) bình thường**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. `coroutineScope` và `supervisorScope` encode hai nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론) khác nhau

### `coroutineScope`

Dùng khi các child cùng tạo thành **một thao tác (operation / 연산) nguyên khối**.

Ví dụ generate report cần cả người dùng (user / 사용자) + transactions:

```kotlin
suspend fun buildReport(): Report = coroutineScope {
    val user = async { loadUser() }
    val tx = async { loadTransactions() }
    Report(user.await(), tx.await())
}
```

Nếu một phần thất bại (fail / 실패), report không hoàn chỉnh; cancel sibling là hợp lý.

### `supervisorScope`

Dùng khi child độc lập và thất bại (failure / 실패) một child không nên hủy child khác.

Ví dụ home dashboard có weather card + recommendation + promo:

```kotlin
supervisorScope {
    launch { loadWeatherSafely() }
    launch { loadRecommendationsSafely() }
    launch { loadPromoSafely() }
}
```

Chọn phạm vi (scope / 범위) phải xuất phát từ nghiệp vụ (business / 비즈니스) relationship, không phải “cái nào ít crash hơn”.

---

> **Nối mạch:** Trong **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **4. coroutineScope và supervisorScope encode hai nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론) khác nhau** đặt đầu vào cho **5. Cancellation là điều khiển (control / 제어) luồng (flow / 흐름), không phải lỗi (error / 오류) bình thường**, rồi **6. Cleanup khi cancellation cần phân biệt suspend và non-suspend** mở rộng hệ quả hoặc giới hạn liên quan.

## 5. Cancellation là điều khiển (control / 제어) luồng (flow / 흐름), không phải lỗi (error / 오류) bình thường

Coroutine cancellation thường được biểu diễn bởi `CancellationException`.

Mã (code / 코드) nguy hiểm:

```kotlin
try {
    repository.load()
} catch (t: Throwable) {
    logger.error(t)
    emit(UiState.Error)
}
```

`Throwable` bắt luôn cancellation. Coroutine có thể tiếp tục chạy lô-gic (logic / 논리) không mong muốn.

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

Hoặc bắt kiểu (type / 타입) lỗi (error / 오류) hẹp hơn.

Mental quy tắc (rule / 규칙):

> cancellation không phải “yêu cầu (request / 요청) failed”; cancellation nghĩa thao tác (operation / 연산) không còn được yêu cầu tiếp tục.

---

> **Nối mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **5. Cancellation là điều khiển (control / 제어) luồng (flow / 흐름), không phải lỗi (error / 오류) bình thường** đặt đầu vào cho **6. Cleanup khi cancellation cần phân biệt suspend và non-suspend**, rồi **7. async không phải cách chung để “chạy background”** mở rộng hệ quả hoặc giới hạn liên quan.

## 6. Cleanup khi cancellation cần phân biệt suspend và non-suspend

`finally` vẫn chạy khi coroutine bị cancel:

```kotlin
try {
    useResource()
} finally {
    resource.close()
}
```

Nếu cleanup cần gọi suspend hàm (function / 함수):

```kotlin
finally {
    withContext(NonCancellable) {
        releaseRemoteLease()
    }
}
```

Nhưng `NonCancellable` phải dùng hẹp. Nếu bọc một mạng (network / 네트워크) thao tác (operation / 연산) dài, cancellation mất ý nghĩa và app có thể giữ công việc (work / 작업) sống quá lâu.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **7. async không phải cách chung để “chạy background”** nối từ **6. Cleanup khi cancellation cần phân biệt suspend và non-suspend** sang **8. tính đồng thời (concurrency / 동시성) không tự động tăng hiệu năng (performance / 성능)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. `async` không phải cách chung để “chạy background”

`async` tạo `Deferred<T>` và dành cho concurrent computation có kết quả (result / 결과).

Bad smell:

```kotlin
viewModelScope.async {
    repository.refresh()
}
```

nếu không bao giờ `await`, thất bại (failure / 실패) có thể bị xử lý khó đoán và intent mã (code / 코드) không rõ.

Nếu chỉ fire child thao tác (operation / 연산) dưới phạm vi (scope / 범위):

```kotlin
viewModelScope.launch {
    repository.refresh()
}
```

Nếu cần hai kết quả (result / 결과) concurrent:

```kotlin
coroutineScope {
    val a = async { loadA() }
    val b = async { loadB() }
    combine(a.await(), b.await())
}
```

---

> **Nối mạch:** Trong **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **8. tính đồng thời (concurrency / 동시성) không tự động tăng hiệu năng (performance / 성능)** nối từ **7. async không phải cách chung để “chạy background”** sang **9. Dispatcher injection là testability + chính sách (policy / 정책) ranh giới (boundary / 경계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. tính đồng thời (concurrency / 동시성) không tự động tăng hiệu năng (performance / 성능)

Hai tác vụ (task / 작업) CPU-bound chạy concurrent trên limited cores có thể cạnh tranh bộ nhớ đệm (cache / 캐시)/CPU.

Hai cơ sở dữ liệu (database / 데이터베이스) writes concurrent có thể serialize ở cơ sở dữ liệu (database / 데이터베이스) khóa (lock / 잠금).

Hai HTTP requests concurrent có thể tốt, nhưng nếu máy chủ (server / 서버) rate-limit hoặc radio wake-up chi phí (cost / 비용) cao thì không phải lúc nào càng nhiều càng nhanh.

Tính đồng thời (concurrency / 동시성) là công cụ (tool / 도구) để overlap công việc (work / 작업) có thể overlap, không phải tối ưu hóa (optimization / 최적화) mặc định.

---

> **Nối mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **8. tính đồng thời (concurrency / 동시성) không tự động tăng hiệu năng (performance / 성능)** đặt tiêu chí; **9. Dispatcher injection là testability + chính sách (policy / 정책) ranh giới (boundary / 경계)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **10. Dispatchers.IO không phải “luồng thực thi (thread / 스레드) pool vô hạn”** mở rộng hệ quả.

## 9. Dispatcher injection là testability + chính sách (policy / 정책) ranh giới (boundary / 경계)

Đừng hard-code:

```kotlin
withContext(Dispatchers.IO) { ... }
```

khắp mã (code / 코드) nếu cần deterministic kiểm thử (test / 테스트).

Có thể inject:

```kotlin
class ArticleRepository(
    private val ioDispatcher: CoroutineDispatcher
)
```

Kiểm thử (test / 테스트) dùng `StandardTestDispatcher` hoặc dispatcher phù hợp.

Dispatcher injection cũng làm thực thi (execution / 실행) chính sách (policy / 정책) tường minh (explicit / 명시적).

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **9. Dispatcher injection là testability + chính sách (policy / 정책) ranh giới (boundary / 경계)** đặt tiêu chí; **10. Dispatchers.IO không phải “luồng thực thi (thread / 스레드) pool vô hạn”** dùng tiêu chí đó để kiểm tra ranh giới, rồi **11. Mutex bảo vệ trọng yếu (critical / 중요) section trong coroutine world** mở rộng hệ quả.

## 10. `Dispatchers.IO` không phải “luồng thực thi (thread / 스레드) pool vô hạn”

IO dispatcher được tối ưu cho blocking I/O, nhưng app vẫn nên tránh tạo unbounded blocking công việc (work / 작업).

Nếu import 50.000 tệp (file / 파일) và mỗi tệp (file / 파일) launch một coroutine blocking:

```kotlin
files.map { file -> async(ioDispatcher) { parse(file) } }
```

có thể gây bộ nhớ (memory / 메모리) pressure, tệp (file / 파일) descriptor pressure và contention.

Bound tính đồng thời (concurrency / 동시성):

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

Tính đồng thời (concurrency / 동시성) limit là sức chứa (capacity / 용량) planning.

---

> **Nối mạch:** Trong **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **11. Mutex bảo vệ trọng yếu (critical / 중요) section trong coroutine world** nối từ **10. Dispatchers.IO không phải “luồng thực thi (thread / 스레드) pool vô hạn”** sang **12. Atomic thao tác (operation / 연산) khác Mutex**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Mutex bảo vệ trọng yếu (critical / 중요) section trong coroutine world

Giả sử đơn vị từ (token / 토큰) refresh:

```text
20 request cùng nhận 401
```

Nếu mỗi yêu cầu (request / 요청) refresh đơn vị từ (token / 토큰) riêng, máy chủ (server / 서버) nhận 20 refresh calls.

Single-flight mẫu (pattern / 패턴):

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

Nhưng trọng yếu (critical / 중요) section phải ngắn và ngữ nghĩa (semantic / 의미적) rõ. Mutex không biến dùng chung (shared / 공유) mutable trạng thái (state / 상태) thành thiết kế (design / 설계) tốt tự động.

---

> **Nối mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **12. Atomic thao tác (operation / 연산) khác Mutex** nối từ **11. Mutex bảo vệ trọng yếu (critical / 중요) section trong coroutine world** sang **13. Actor/Channel giúp serialize command khi thứ tự (ordering / 순서) quan trọng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Atomic thao tác (operation / 연산) khác Mutex

Nếu chỉ cần compare-and-set một thành phần nguyên thủy (primitive / 기본 요소) trạng thái (state / 상태), atomic có thể phù hợp.

Nếu bất biến (invariant / 불변식) liên quan nhiều trường dữ liệu (field / 필드) hoặc suspend thao tác (operation / 연산), Mutex/giao dịch (transaction / 트랜잭션) có thể cần thiết.

Ví dụ bất biến (invariant / 불변식):

```text
currentToken và tokenExpiry phải thay đổi cùng nhau
```

Hai atomic riêng không nhất thiết bảo vệ pair bất biến (invariant / 불변식).

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **13. Actor/Channel giúp serialize command khi thứ tự (ordering / 순서) quan trọng** nối từ **12. Atomic thao tác (operation / 연산) khác Mutex** sang **14. Cold Flow là recipe, không phải running stream**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Actor/Channel giúp serialize command khi thứ tự (ordering / 순서) quan trọng

Một máy trạng thái (state machine / 상태 머신) có thể nhận command:

```text
Connect
Disconnect
Send
Retry
```

Thay vì nhiều coroutine mutate trạng thái dùng chung (shared state / 공유 상태), một vòng lặp sự kiện (event loop / 이벤트 루프) serialize command:

```kotlin
for (command in commands) {
    reduce(command)
}
```

Đây là actor-like mô hình (model / 모델). Nó giảm race vì có single writer.

Sự đánh đổi (trade-off / 트레이드오프) là cần xử lý hàng đợi (queue / 큐)/backpressure/shutdown rõ ràng.

---

> **Nối mạch:** Trong **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **13. Actor/Channel giúp serialize command khi thứ tự (ordering / 순서) quan trọng** đặt đầu vào cho **14. Cold Flow là recipe, không phải running stream**, rồi **15. Hot luồng (flow / 흐름) cần thời gian tồn tại (lifetime / 수명) đơn vị sở hữu (owner / 오너)** mở rộng hệ quả hoặc giới hạn liên quan.

## 14. Cold Flow là recipe, không phải running stream
Phần này nối mạch Android vừa học với “14. Cold Flow là recipe, không phải running stream”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```kotlin
val flow = flow {
    emit(api.load())
}
```

Chưa chạy gì cho tới khi collect.

Mỗi collector có thể chạy upstream riêng.

Nếu 5 collector collect một cold luồng (flow / 흐름) gọi mạng (network / 네트워크), có thể tạo 5 yêu cầu (request / 요청).

Hãy hỏi:

```text
upstream nên chạy per collector hay shared?
```

---

> **Nối mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **14. Cold Flow là recipe, không phải running stream** đặt đầu vào cho **15. Hot luồng (flow / 흐름) cần thời gian tồn tại (lifetime / 수명) đơn vị sở hữu (owner / 오너)**, rồi **16. SharingStarted.WhileSubscribed là tài nguyên (resource / 자원) chính sách (policy / 정책)** mở rộng hệ quả hoặc giới hạn liên quan.

## 15. Hot luồng (flow / 흐름) cần thời gian tồn tại (lifetime / 수명) đơn vị sở hữu (owner / 오너)

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, cơ chế trong **15. Hot luồng (flow / 흐름) cần thời gian tồn tại (lifetime / 수명) đơn vị sở hữu (owner / 오너)** cần được kiểm chứng bằng dấu vết cụ thể; **16. SharingStarted.WhileSubscribed là tài nguyên (resource / 자원) chính sách (policy / 정책)** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **17. flowOn đổi ngữ cảnh (context / 맥락) phía upstream** mở rộng hệ quả hoặc giới hạn liên quan.

## 16. `SharingStarted.WhileSubscribed` là tài nguyên (resource / 자원) chính sách (policy / 정책)

Nếu upstream là Room luồng (flow / 흐름), giữ một khoảng stop hết thời gian chờ (timeout / 타임아웃) có thể tránh stop/start liên tục khi cấu hình (configuration / 구성) thay đổi (change / 변경) ngắn.

Nếu upstream là GPS sensor, giữ thêm 5 giây có thể tốn pin không cần thiết.

Cùng một operator nhưng tài nguyên (resource / 자원) chi phí (cost / 비용) khác.

Started chính sách (policy / 정책) phải dựa vào upstream ngữ nghĩa (semantics / 의미론).

---

> **Nối mạch:** Trong **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **16. SharingStarted.WhileSubscribed là tài nguyên (resource / 자원) chính sách (policy / 정책)** đặt vấn đề; **17. flowOn đổi ngữ cảnh (context / 맥락) phía upstream** đối chiếu bằng chứng, rồi **18. collectLatest encode cancellation chính sách (policy / 정책)** mở rộng hệ quả hoặc giới hạn liên quan.

## 17. `flowOn` đổi ngữ cảnh (context / 맥락) phía upstream

Mô hình tư duy (mental model / 사고 모델):

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

Việc hiểu ngữ cảnh (context / 맥락) preservation giúp tránh đặt heavy ánh xạ (mapping / 매핑) ở sai phía.

---

> **Nối mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **17. flowOn đổi ngữ cảnh (context / 맥락) phía upstream** đặt đầu vào cho **18. collectLatest encode cancellation chính sách (policy / 정책)**, rồi **19. flatMapLatest bảo vệ stale-request race** mở rộng hệ quả hoặc giới hạn liên quan.

## 18. `collectLatest` encode cancellation chính sách (policy / 정책)

Search-as-you-type:

```kotlin
queryFlow.collectLatest { query ->
    render(repository.search(query))
}
```

Khi truy vấn (query / 쿼리) mới tới, khối (block / 블록) cũ bị cancel.

Điều này chỉ đúng nếu kết quả (result / 결과) cũ không còn giá trị.

Không dùng `collectLatest` cho thao tác (operation / 연산) không được phép cancel giữa chừng như lần ghi nhận (commit / 커밋) cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션) phức tạp nếu cancellation an toàn (safety / 안전) chưa rõ.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **19. flatMapLatest bảo vệ stale-request race** nối từ **18. collectLatest encode cancellation chính sách (policy / 정책)** sang **20. buffer thay đổi producer-consumer coupling**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. `flatMapLatest` bảo vệ stale-request race
Phần này nối mạch Android vừa học với “19. `flatMapLatest` bảo vệ stale-request race”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```kotlin
query
    .debounce(300)
    .flatMapLatest { repository.search(it) }
```

Truy vấn (query / 쿼리) mới cancel upstream tìm kiếm (search / 검색) cũ.

Bất biến (invariant / 불변식) được bảo vệ:

```text
result của query cũ không được trở thành state hiện tại sau query mới
```

Operator là hiện thực (implementation / 구현) của bất biến (invariant / 불변식).

---

> **Nối mạch:** Trong **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **20. buffer thay đổi producer-consumer coupling** nối từ **19. flatMapLatest bảo vệ stale-request race** sang **21. conflate bỏ intermediate giá trị (value / 값)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. `buffer` thay đổi producer-consumer coupling

Không buffer:

```text
producer emit -> chờ consumer xử lý -> emit tiếp
```

Có buffer:

```text
producer có thể chạy trước consumer một khoảng
```

Điều này tăng thông lượng (throughput / 처리량) khi producer và bên tiêu thụ (consumer / 소비자) có thể overlap, nhưng cũng tăng bộ nhớ (memory / 메모리) và stale công việc (work / 작업).

Đừng thêm `buffer()` chỉ vì “hiệu năng (performance / 성능)”. Hãy biết hàng đợi (queue / 큐) kích thước (size / 크기) và drop ngữ nghĩa (semantics / 의미론).

---

> **Nối mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **21. conflate bỏ intermediate giá trị (value / 값)** nối từ **20. buffer thay đổi producer-consumer coupling** sang **22. SharedFlow không tự động là sự kiện (event / 이벤트) bus tốt**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. `conflate` bỏ intermediate giá trị (value / 값)

Dùng khi chỉ trạng thái (state / 상태) mới nhất quan trọng.

Ví dụ progress 1%, 2%, 3%, ... 90% mà UI kết xuất (render / 렌더링) chậm, có thể không cần kết xuất (render / 렌더링) mọi bước.

Nhưng không dùng cho sự kiện (event / 이벤트) stream mà mỗi item đều quan trọng như giao dịch (transaction / 트랜잭션) sự kiện (event / 이벤트).

Trạng thái (state / 상태) stream và sự kiện (event / 이벤트) stream có mất mát (loss / 손실) tolerance khác nhau.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **21. conflate bỏ intermediate giá trị (value / 값)** đặt đầu vào cho **22. SharedFlow không tự động là sự kiện (event / 이벤트) bus tốt**, rồi **23. Channel có hàng đợi (queue / 큐) ngữ nghĩa (semantics / 의미론) rõ hơn cho point-to-point sự kiện (event / 이벤트)** mở rộng hệ quả hoặc giới hạn liên quan.

## 22. `SharedFlow` không tự động là sự kiện (event / 이벤트) bus tốt

Một toàn cục (global / 전역) dùng chung (shared / 공유) luồng (flow / 흐름) cho mọi one-off sự kiện (event / 이벤트) dễ tạo hidden phụ thuộc (dependency / 의존성).

Các câu hỏi cần trả lời:

```text
replay bao nhiêu?
buffer capacity?
onBufferOverflow?
collector inactive thì event mất được không?
multiple collector có cùng nhận không?
```

Nếu sự kiện (event / 이벤트) không được phép mất, có thể nó nên là durable trạng thái (state / 상태) hoặc hàng đợi (queue / 큐) chứ không phải ephemeral SharedFlow.

---

> **Nối mạch:** Trong **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **22. SharedFlow không tự động là sự kiện (event / 이벤트) bus tốt** đặt đầu vào cho **23. Channel có hàng đợi (queue / 큐) ngữ nghĩa (semantics / 의미론) rõ hơn cho point-to-point sự kiện (event / 이벤트)**, rồi **24. Callback -> callbackFlow cần cleanup chính xác** mở rộng hệ quả hoặc giới hạn liên quan.

## 23. `Channel` có hàng đợi (queue / 큐) ngữ nghĩa (semantics / 의미론) rõ hơn cho point-to-point sự kiện (event / 이벤트)

Channel phù hợp khi sự kiện (event / 이벤트) cần được consume bởi một bên tiêu thụ (consumer / 소비자) theo hàng đợi (queue / 큐) ngữ nghĩa (semantics / 의미론).

Nhưng channel nằm in-memory; tiến trình (process / 프로세스) death vẫn làm sự kiện (event / 이벤트) mất.

Vì vậy notification “payment succeeded” quan trọng có thể nên reconstruct từ persisted giao dịch (transaction / 트랜잭션) trạng thái (state / 상태) thay vì chờ một Channel sự kiện (event / 이벤트).

---

> **Nối mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **23. Channel có hàng đợi (queue / 큐) ngữ nghĩa (semantics / 의미론) rõ hơn cho point-to-point sự kiện (event / 이벤트)** đặt đầu vào cho **24. Callback -> callbackFlow cần cleanup chính xác**, rồi **25. Backpressure ở callbackFlow cần chính sách (policy / 정책)** mở rộng hệ quả hoặc giới hạn liên quan.

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

Callback thời gian tồn tại (lifetime / 수명) phải map đúng vào luồng (flow / 흐름) collection thời gian tồn tại (lifetime / 수명).

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **24. Callback -> callbackFlow cần cleanup chính xác** đặt đầu vào cho **25. Backpressure ở callbackFlow cần chính sách (policy / 정책)**, rồi **26. repeatOnLifecycle bảo vệ collection thời gian tồn tại (lifetime / 수명)** mở rộng hệ quả hoặc giới hạn liên quan.

## 25. Backpressure ở callbackFlow cần chính sách (policy / 정책)

Sensor có thể emit 100Hz nhưng bên tiêu thụ (consumer / 소비자) xử lý 10Hz.

Cần quyết định:

```text
buffer bao nhiêu?
drop oldest?
drop latest?
conflate?
```

Nếu telemetry cho UI, latest có thể đủ. Nếu dữ liệu scientific capture, drop có thể không chấp nhận.

---

> **Nối mạch:** Trong **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **25. Backpressure ở callbackFlow cần chính sách (policy / 정책)** đặt đầu vào cho **26. repeatOnLifecycle bảo vệ collection thời gian tồn tại (lifetime / 수명)**, rồi **27. Race giữa refresh và cục bộ (local / 로컬) mutation** mở rộng hệ quả hoặc giới hạn liên quan.

## 26. `repeatOnLifecycle` bảo vệ collection thời gian tồn tại (lifetime / 수명)

UI không nên collect luồng (flow / 흐름) vô điều kiện khi vòng đời (lifecycle / 생명주기) không active.

Compose thường dùng:

```kotlin
collectAsStateWithLifecycle()
```

View hệ thống (system / 시스템) có thể dùng `repeatOnLifecycle`.

Mục tiêu không phải thuộc API mà là tránh:

```text
UI không visible nhưng vẫn xử lý/render stream
```

và tránh manual start/stop dễ leak.

---

> **Nối mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **26. repeatOnLifecycle bảo vệ collection thời gian tồn tại (lifetime / 수명)** đặt đầu vào cho **27. Race giữa refresh và cục bộ (local / 로컬) mutation**, rồi **28. Race giữa logout và in-flight request** mở rộng hệ quả hoặc giới hạn liên quan.

## 27. Race giữa refresh và cục bộ (local / 로컬) mutation

Timeline:

```text
T0 refresh request bắt đầu
T1 user bookmark locally
T2 server response của refresh chứa bookmark=false từ snapshot cũ
T3 refresh ghi toàn row -> bookmark local bị mất
```

Đây không phải coroutine bug; đây là merge ngữ nghĩa (semantics / 의미론) bug.

Fix có thể là:

- remote refresh không overwrite local-only trường dữ liệu (field / 필드),
- trường dữ liệu (field / 필드) versioning,
- separate bảng (table / 테이블),
- pending mutation overlay.

Tính đồng thời (concurrency / 동시성) operator không thay thế dữ liệu (data / 데이터) merge chính sách (policy / 정책).

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **28. Race giữa logout và in-flight request** nối từ **27. Race giữa refresh và cục bộ (local / 로컬) mutation** sang **29. Race giữa tiến trình (process / 프로세스) vòng đời (lifecycle / 생명주기) và callback**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. Race giữa logout và in-flight request
Phần này nối mạch Android vừa học với “28. Race giữa logout và in-flight request”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```text
T0 account A request start
T1 logout A
T2 login B
T3 response A về
T4 repository ghi DB dùng current account B
```

Cần session/account định danh (identity / 식별자) capture và verify trước lần ghi nhận (commit / 커밋).

Cancellation yêu cầu (request / 요청) cũ giúp nhưng không đủ vì remote phản hồi (response / 응답) có thể vẫn race. nghiệp vụ (business / 비즈니스) guard phải tồn tại.

---

> **Nối mạch:** Trong **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **28. Race giữa logout và in-flight request** đặt đầu vào cho **29. Race giữa tiến trình (process / 프로세스) vòng đời (lifecycle / 생명주기) và callback**, rồi **30. Timeout cần ở boundary đúng** mở rộng hệ quả hoặc giới hạn liên quan.

## 29. Race giữa tiến trình (process / 프로세스) vòng đời (lifecycle / 생명주기) và callback

Một callback có thể về sau Activity destroyed.

Nếu callback giữ Activity tham chiếu (reference / 참조) hoặc trực tiếp mutate View, leak/crash dễ xảy ra.

Trạng thái (state / 상태) nên đi qua lifecycle-aware đơn vị sở hữu (owner / 오너); callback registration cleanup theo vòng đời (lifecycle / 생명주기)/tài nguyên (resource / 자원) đơn vị sở hữu (owner / 오너).

---

> **Nối mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **29. Race giữa tiến trình (process / 프로세스) vòng đời (lifecycle / 생명주기) và callback** đặt tiêu chí; **30. Timeout cần ở boundary đúng** dùng tiêu chí đó để kiểm tra ranh giới, rồi **31. Retry trong Flow cần phân loại error** mở rộng hệ quả.

## 30. Timeout cần ở boundary đúng
Phần này nối mạch Android vừa học với “30. Timeout cần ở boundary đúng”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```kotlin
withTimeout(5_000) {
    wholeCheckoutFlow()
}
```

có thể sai nếu checkout gồm nhiều step hợp lệ lâu hơn 5s.

Hết thời gian chờ (timeout / 타임아웃) nên reflect SLA của ranh giới (boundary / 경계) cụ thể:

```text
DNS/connect timeout
HTTP request timeout
BLE operation timeout
user interaction không nên dùng network timeout
```

Một hết thời gian chờ (timeout / 타임아웃) toàn cục (global / 전역) dễ cancel thao tác (operation / 연산) ở điểm không an toàn.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **30. Timeout cần ở boundary đúng** đặt tiêu chí; **31. Retry trong Flow cần phân loại error** dùng tiêu chí đó để kiểm tra ranh giới, rồi **32. luồng (flow / 흐름) exception transparency** mở rộng hệ quả.

## 31. Retry trong Flow cần phân loại error
Phần này nối mạch Android vừa học với “31. Retry trong Flow cần phân loại error”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```kotlin
flow.retry(3)
```

quá thô nếu mọi lỗi (error / 오류) đều thử lại (retry / 재시도).

Tốt hơn:

```kotlin
.retryWhen { cause, attempt ->
    cause is IOException && attempt < 3
}
```

HTTP kiểm tra hợp lệ (validation / 검증) lỗi (error / 오류) không nên thử lại (retry / 재시도) như connectivity lỗi (error / 오류).

---

> **Nối mạch:** Trong **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **31. Retry trong Flow cần phân loại error** đặt đầu vào cho **32. luồng (flow / 흐름) exception transparency**, rồi **33. CPU cancellation cooperative** mở rộng hệ quả hoặc giới hạn liên quan.

## 32. luồng (flow / 흐름) exception transparency

Luồng (flow / 흐름) convention yêu cầu upstream exception không bị nuốt hoặc emit tùy tiện từ nơi không phù hợp.

`catch` chỉ catch upstream trước nó.

Mô hình tư duy (mental model / 사고 모델):

```kotlin
source
    .map { ... }
    .catch { ... }   // catch source/map error
    .collect { ... } // collector error không bị catch ở trên
```

Hiểu ranh giới (boundary / 경계) của operator giúp gỡ lỗi (debug / 디버그) exception propagation.

---

> **Nối mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **32. luồng (flow / 흐름) exception transparency** đặt đầu vào cho **33. CPU cancellation cooperative**, rồi **34. Blocking thư viện (library / 라이브러리) trong coroutine vẫn khối (block / 블록) luồng thực thi (thread / 스레드)** mở rộng hệ quả hoặc giới hạn liên quan.

## 33. CPU cancellation cooperative

Một vòng lặp (loop / 루프) CPU dài không suspend có thể không phản ứng cancellation nhanh:

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

Cancellation responsiveness là phần của UX/tài nguyên (resource / 자원) tính đúng đắn (correctness / 정확성).

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **34. Blocking thư viện (library / 라이브러리) trong coroutine vẫn khối (block / 블록) luồng thực thi (thread / 스레드)** nối từ **33. CPU cancellation cooperative** sang **35. kiểm thử (test / 테스트) coroutine phải kiểm soát scheduler**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. Blocking thư viện (library / 라이브러리) trong coroutine vẫn khối (block / 블록) luồng thực thi (thread / 스레드)

Nếu SDK Java cũ có:

```kotlin
legacyClient.blockingCall()
```

bọc trong `suspend fun` không biến nó non-blocking.

Phải chuyển dispatcher hoặc dùng async API nếu có.

Suspending lớp trừu tượng (abstraction / 추상화) không thay đổi bản chất underlying I/O.

---

> **Nối mạch:** Trong **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **35. kiểm thử (test / 테스트) coroutine phải kiểm soát scheduler** nối từ **34. Blocking thư viện (library / 라이브러리) trong coroutine vẫn khối (block / 블록) luồng thực thi (thread / 스레드)** sang **36. kiểm thử (test / 테스트) cancellation, không chỉ success**, vì cơ chế trước tạo đầu vào cho bước sau.

## 35. kiểm thử (test / 테스트) coroutine phải kiểm soát scheduler

Dùng kiểm thử (test / 테스트) dispatcher cho phép:

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

Không dùng `Thread.sleep()` trong deterministic coroutine kiểm thử (test / 테스트).

---

> **Nối mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **36. kiểm thử (test / 테스트) cancellation, không chỉ success** nối từ **35. kiểm thử (test / 테스트) coroutine phải kiểm soát scheduler** sang **37. gỡ lỗi (debug / 디버그) coroutine bằng quyền sở hữu (ownership / 소유권) đồ thị (graph / 그래프)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 36. kiểm thử (test / 테스트) cancellation, không chỉ success

Một repository có thể pass happy đường dẫn (path / 경로) nhưng leak tài nguyên (resource / 자원) khi cancel.

Kiểm thử (test / 테스트):

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

Cancellation đường dẫn (path / 경로) là first-class hành vi (behavior / 동작).

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **37. gỡ lỗi (debug / 디버그) coroutine bằng quyền sở hữu (ownership / 소유권) đồ thị (graph / 그래프)** nối từ **36. kiểm thử (test / 테스트) cancellation, không chỉ success** sang **38. Concurrency design checklist**, vì cơ chế trước tạo đầu vào cho bước sau.

## 37. gỡ lỗi (debug / 디버그) coroutine bằng quyền sở hữu (ownership / 소유권) đồ thị (graph / 그래프)

Khi gặp “coroutine vẫn chạy”, đừng chỉ log luồng thực thi (thread / 스레드) name.

Hỏi:

```text
Job parent là ai?
Scope sống bao lâu?
Child có được cancel không?
Có NonCancellable không?
Có callback external giữ reference không?
Flow upstream shared ở scope nào?
```

Quyền sở hữu (ownership / 소유권) đồ thị (graph / 그래프) thường giải thích bug nhanh hơn luồng thực thi (thread / 스레드) dump đơn thuần.

---

> **Nối mạch:** Trong **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **38. Concurrency design checklist** nối từ **37. gỡ lỗi (debug / 디버그) coroutine bằng quyền sở hữu (ownership / 소유권) đồ thị (graph / 그래프)** sang **39. Kết luận**, vì cơ chế trước tạo đầu vào cho bước sau.

## 38. Concurrency design checklist
Phần này nối mạch Android vừa học với “38. Concurrency design checklist”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

| Câu hỏi | Ý nghĩa |
|---|---|
| thao tác (operation / 연산) đơn vị sở hữu (owner / 오너) là ai? | phạm vi (scope / 범위)/thời gian tồn tại (lifetime / 수명) |
| Child sống chết cùng nhau không? | coroutineScope/supervision |
| Cancellation có được propagate không? | structured tính đồng thời (concurrency / 동시성) |
| trạng thái dùng chung (shared state / 공유 상태) có single writer không? | race điều khiển (control / 제어) |
| thử lại (retry / 재시도) có idempotent không? | duplicate tác động (effect / 효과) |
| Upstream cold hay hot? | duplicate công việc (work / 작업)/tài nguyên (resource / 자원) |
| Collector chậm thì sao? | backpressure |
| sự kiện (event / 이벤트) có được phép mất không? | trạng thái (state / 상태) vs hàng đợi (queue / 큐) |
| bên ngoài (external / 외부) callback cleanup ở đâu? | leak prevention |
| kiểm thử (test / 테스트) scheduler kiểm soát được không? | determinism |

---

> **Nối mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 03 — Coroutine, luồng (flow / 흐름), tính đồng thời (concurrency / 동시성) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**, **39. Kết luận** tổng hợp từ **38. Concurrency design checklist** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## 39. Kết luận

Coroutine và luồng (flow / 흐름) mạnh vì chúng cho phép biểu diễn thời gian tồn tại (lifetime / 수명) và dữ liệu (data / 데이터) stream bằng cấu trúc rõ hơn callback truyền thống. Nhưng tính đúng đắn (correctness / 정확성) chỉ có khi nhà phát triển (developer / 개발자) hiểu ngữ nghĩa (semantic / 의미적) phía sau API.

Mô hình tư duy (mental model / 사고 모델) nên giữ:

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

> **Bàn giao:** Sau **39. Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
