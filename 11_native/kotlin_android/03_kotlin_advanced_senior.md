# Kotlin + Android Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)

> **Mạch đọc:** Đặt **Kotlin + Android Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Mục lục** sang **6.1 Suspension không đồng nghĩa background**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


> Mục tiêu: hiểu sâu ngữ nghĩa (semantics / 의미론) của Kotlin, vòng đời (lifecycle / 생명주기)/trạng thái (state / 상태)/tính đồng thời (concurrency / 동시성) của Android, coroutine/luồng (flow / 흐름), Compose thời gian chạy (runtime / 런타임), kiến trúc (architecture / 아키텍처), thất bại (failure / 실패) modes, hiệu năng (performance / 성능), bảo mật (security / 보안), bản dựng (build / 빌드)/bản phát hành (release / 릴리스) và di chuyển (migration / 마이그레이션). Ở mức (level / 수준) này, không chỉ biết API nào tồn tại mà phải giải thích được **đơn vị sở hữu (owner / 오너) là ai, thời gian tồn tại (lifetime / 수명) bao lâu, điều gì xảy ra khi interleave/tiến trình (process / 프로세스) death/thử lại (retry / 재시도) và API cũ nên giữ hay migrate vì lý do gì**.

## Mục lục

1. Kotlin hệ kiểu (type system / 타입 시스템) nâng cao
2. Inline, noinline, crossinline và reified
3. Operator overloading và DSL
4. Contracts và trình biên dịch (compiler / 컴파일러) lập luận (reasoning / 추론)
5. Reflection, annotations và mã (code / 코드) generation
6. Coroutine internals và cancellation
7. Structured tính đồng thời (concurrency / 동시성), exception và supervision
8. luồng (flow / 흐름) internals, hot/cold, backpressure và sharing
9. máy trạng thái (state machine / 상태 머신), UDF và sự kiện (event / 이벤트) ngữ nghĩa (semantics / 의미론)
10. Compose thời gian chạy (runtime / 런타임), định danh (identity / 식별자) và recomposition
11. Snapshot trạng thái (state / 상태), stability và phase hiệu năng (performance / 성능)
12. Side effects và thời gian tồn tại (lifetime / 수명)
13. Android vòng đời (lifecycle / 생명주기), cấu hình (configuration / 구성) thay đổi (change / 변경) và tiến trình (process / 프로세스) death
14. SavedStateHandle và trạng thái (state / 상태) reconstruction
15. Multi-module kiến trúc (architecture / 아키텍처)
16. hệ thống dựng (build system / 빌드 시스템) và Gradle hiệu năng (performance / 성능)
17. phụ thuộc (dependency / 의존성) Injection ở quy mô lớn
18. Offline-first, bộ nhớ đệm (cache / 캐시) và sync
19. Pagination và Paging 3
20. Background thực thi (execution / 실행) chính sách (policy / 정책)
21. bảo mật (security / 보안) môi trường vận hành (production / 운영 환경)
22. hiệu năng (performance / 성능), bộ nhớ (memory / 메모리) và battery
23. Networking nâng cao
24. cơ sở dữ liệu (database / 데이터베이스) nâng cao
25. Testing chiến lược (strategy / 전략)
26. Java interoperability
27. API thiết kế (design / 설계) bằng Kotlin
28. dùng chung (common / 공통) thiết kế (design / 설계) patterns và Kotlin idioms
29. hiện đại (modern / 현대적) vs legacy API và di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략)
30. cấp cao (senior / 시니어) rà soát (review / 검토) checklist
31. Channel, Mutex, atomic và dùng chung (shared / 공유) mutable trạng thái (state / 상태)
32. Coroutine scheduler, dispatcher injection và starvation
33. Compose hiệu năng (performance / 성능): đo recomposition đúng cách
34. Main luồng thực thi (thread / 스레드), ANR, StrictMode và leak
35. R8, shrinking và keep rules
36. Signing, APK/AAB và bản phát hành (release / 릴리스) reproducibility
37. API-level tính tương thích (compatibility / 호환성), hành vi (behavior / 동작) thay đổi (change / 변경) và tính năng (feature / 기능) gating
38. WebView như một ranh giới bảo mật (security boundary / 보안 경계)
39. cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) và lược đồ (schema / 스키마) evolution
40. cấp cao (senior / 시니어) quyết định (decision / 결정) khung phần mềm (framework / 프레임워크)

---

# 1. Kotlin hệ kiểu (type system / 타입 시스템) nâng cao

Kotlin hệ kiểu (type system / 타입 시스템) có nullable types, bottom kiểu (type / 타입) `Nothing`, top types `Any`/`Any?`, variance, smart cast và nền tảng (platform / 플랫폼) types từ Java. cấp cao (senior / 시니어) nhà phát triển (developer / 개발자) phải xem nền tảng (platform / 플랫폼) kiểu (type / 타입) như một **ranh giới (boundary / 경계) chưa được normalize**, không phải convenience kiểu (type / 타입) bình thường.

Nếu Java trả `String!`, normalize nullability càng sớm càng tốt:

```kotlin
val safeName: String = javaApi.name ?: "Unknown"
```

Đừng để `String!` chảy sâu vào lĩnh vực (domain / 도메인) vì trình biên dịch (compiler / 컴파일러) không còn bảo vệ được bất biến (invariant / 불변식) null-safety.

# 2. `inline`, `noinline`, `crossinline`, `reified`

`inline` có thể loại lời gọi (call / 호출)/lambda allocation và cho phép non-local return; `noinline` giữ lambda như đối tượng (object / 객체); `crossinline` cấm non-local return khi callback chạy ở ngữ cảnh (context / 맥락) khác; `reified` cho kiểu (type / 타입) parameter của inline hàm (function / 함수) được dùng tại lời gọi (call / 호출) site.

```kotlin
inline fun <reified T> Json.decode(text: String): T = ...
```

Đừng inline mọi higher-order hàm (function / 함수). công khai (public / 공개) inline API còn có tính tương thích (compatibility / 호환성) implication vì body có thể được bản sao (copy / 복사) vào bytecode bên tiêu thụ (consumer / 소비자).

# 3. Operator overloading và DSL

Operator nên phản ánh ngữ nghĩa (semantics / 의미론) tự nhiên. `moneyA + moneyB` hợp lý; `user + server` mà âm thầm gọi mạng (network / 네트워크) là API gây bất ngờ. Kotlin DSL dựa vào lambda with receiver/extension/builder; Compose sử dụng cú pháp (syntax / 문법) DSL-like nhưng thời gian chạy (runtime / 런타임) không phải builder thuần.

# 4. Contracts

Contracts giúp trình biên dịch (compiler / 컴파일러) hiểu một số quan hệ control-flow/trạng thái (state / 상태). Chỉ tạo custom đặc tả hợp đồng (contract / 계약) khi hiểu tác động (effect / 효과) và limitation; đặc tả hợp đồng (contract / 계약) sai có thể làm trình biên dịch (compiler / 컴파일러) suy luận mạnh hơn hành vi (behavior / 동작) thực tế.

# 5. Reflection, annotations và mã (code / 코드) generation

Reflection hữu ích nhưng có chi phí (cost / 비용) startup/kích thước (size / 크기)/obfuscation. Android ecosystem hiện đại thường ưu tiên mã (code / 코드) generation khi phù hợp. KSP hiểu Kotlin symbol trực tiếp; kapt dựa Java annotation processing/stub. **hiện đại (modern / 현대적) không đồng nghĩa bắt buộc KSP**: migrate theo processor hỗ trợ (support / 지원)/maturity, không đổi chỉ vì tên API mới hơn.

Generated mã (code / 코드) là một phần bản dựng (build / 빌드) kiến trúc (architecture / 아키텍처). Khi upgrade Kotlin/AGP mà lỗi nằm trong Room/Hilt/serialization/Compose generated đường dẫn (path / 경로), kiểm tra plugin/processor tính tương thích (compatibility / 호환성) trước khi sửa nghiệp vụ (business / 비즈니스) mã (code / 코드).

# 6. Coroutine internals và cancellation

`suspend` không tạo luồng thực thi (thread / 스레드). trình biên dịch (compiler / 컴파일러) biến suspend hàm (function / 함수) thành máy trạng thái (state machine / 상태 머신) với continuation. Coroutine có thể suspend mà không giữ luồng thực thi (thread / 스레드) và resume trên luồng thực thi (thread / 스레드) khác theo dispatcher/ngữ cảnh (context / 맥락).

## 6.1 Suspension không đồng nghĩa background

```kotlin
suspend fun parseHugeJson(text: String): Model {
    return parser.parse(text) // vẫn CPU/blocking trên thread hiện tại nếu parser sync
}
```

`suspend` chỉ nói hàm (function / 함수) có thể suspend; nó không nói công việc (work / 작업) main-safe. Blocking/CPU-heavy công việc (work / 작업) cần thực thi (execution / 실행) chính sách (policy / 정책) rõ ở tầng (layer / 계층) sở hữu hiện thực (implementation / 구현).

## 6.2 Cancellation là cooperative điều khiển (control / 제어) luồng (flow / 흐름)

CPU vòng lặp (loop / 루프) dài phải check cancellation:

```kotlin
while (hasMore()) {
    ensureActive()
    computeChunk()
}
```

Không swallow `CancellationException`:

```kotlin
try {
    work()
} catch (e: CancellationException) {
    throw e
} catch (e: IOException) {
    handle(e)
}
```

Generic `catch (Throwable)` rồi convert thành `UiError` có thể biến screen đã đóng thành thao tác (operation / 연산) tiếp tục chạy và emit trạng thái (state / 상태) muộn.

## 6.3 Cleanup và `NonCancellable`

`finally` vẫn chạy khi cancel. Chỉ dùng `withContext(NonCancellable)` cho cleanup suspend nhỏ thật sự bắt buộc, ví dụ đóng giao dịch (transaction / 트랜잭션)/giao thức (protocol / 프로토콜) trạng thái (state / 상태). Bọc toàn thao tác (operation / 연산) trong `NonCancellable` phá structured cancellation.

# 7. Structured tính đồng thời (concurrency / 동시성), exception và supervision

Structured tính đồng thời (concurrency / 동시성) tạo cây (tree / 트리) thời gian tồn tại (lifetime / 수명)/thất bại (failure / 실패):

```text
parent scope
├─ child A
└─ child B
```

Với `coroutineScope`, child thất bại (failure / 실패) thường cancel siblings/parent phạm vi (scope / 범위). `supervisorScope` tách thất bại (failure / 실패) của siblings nhưng không “nuốt lỗi”. Bạn vẫn cần xử lý từng child thất bại (failure / 실패).

`launch` và `async` khác mục đích: `launch` cho fire-and-join side tác động (effect / 효과) trong phạm vi (scope / 범위); `async` tạo giá trị (value / 값) cần `await`. Dùng `async` mà không `await` thường là smell.

## 7.1 Concurrent start không phải always faster

```kotlin
coroutineScope {
    val a = async { loadA() }
    val b = async { loadB() }
    combine(a.await(), b.await())
}
```

Chỉ parallel nếu A/B độc lập và backend/thiết bị (device / 장치) ngân sách (budget / 예산) cho phép. Parallel hóa quá mức có thể tăng contention, rate-limit và battery chi phí (cost / 비용).

## 7.2 Stale kết quả (result / 결과) race

Người dùng (user / 사용자) tìm kiếm (search / 검색) `a`, rồi `ab`; yêu cầu (request / 요청) `a` có thể finish sau `ab` và overwrite UI. Giải pháp không chỉ “dùng coroutine”: cần latest-wins cancellation (`flatMapLatest`/cancel previous), yêu cầu (request / 요청) generation ID hoặc trạng thái (state / 상태) đơn vị sở hữu (owner / 오너) reject stale kết quả (result / 결과).

# 8. luồng (flow / 흐름) internals, hot/cold, backpressure và sharing

Cold luồng (flow / 흐름) chạy producer theo mỗi collector. Hot luồng (flow / 흐름) tồn tại độc lập collector tùy phạm vi (scope / 범위)/thời gian tồn tại (lifetime / 수명).

```text
cold Flow
collector mới → upstream mới

StateFlow/SharedFlow
upstream/state có lifetime riêng
```

## 8.1 Backpressure operator mang nghĩa nghiệp vụ

`buffer()` cho producer đi trước trong giới hạn buffer. `conflate()` bỏ intermediate values. `collectLatest` cancel xử lý giá trị (value / 값) cũ. `flatMapLatest` cancel sub-flow cũ khi key mới đến.

```kotlin
queryFlow
    .debounce(300)
    .distinctUntilChanged()
    .flatMapLatest(repository::search)
```

Tìm kiếm (search / 검색) phù hợp latest-wins. kiểm tra (audit / 감사)/payment sự kiện (event / 이벤트) thì không được conflate vì mỗi sự kiện (event / 이벤트) có nghĩa.

<!-- merge: preserve both chuẩn gốc (canonical / 정본) variants -->
## 8.2 `stateIn`/`shareIn` thay đổi thời gian tồn tại (lifetime / 수명)

Chúng không chỉ tối ưu subscription; chúng biến cold upstream thành dùng chung (shared / 공유) hot stream trong một phạm vi (scope / 범위). Nếu phạm vi (scope / 범위) application-level, DB/mạng (network / 네트워크) subscription có thể sống lâu hơn screen. `SharingStarted.WhileSubscribed(timeout)` phải chọn theo reconnect chi phí (cost / 비용)/staleness ngữ nghĩa (semantics / 의미론).

## 8.3 `StateFlow` vs sự kiện (event / 이벤트)

`StateFlow` luôn có trạng thái hiện tại (current state / 현재 상태). Collector mới nhận trạng thái hiện tại. One-shot tác động (effect / 효과) như “toast copied” có thể không cần survive tiến trình (process / 프로세스)/recreation; payment success lại thường là lĩnh vực (domain / 도메인) trạng thái (state / 상태) phải reconstruct. Trước khi chọn Channel/SharedFlow, hỏi sự kiện (event / 이벤트) có được phép mất không và replay có nguy hiểm không.

# 9. máy trạng thái (state machine / 상태 머신), UDF và sự kiện (event / 이벤트) ngữ nghĩa (semantics / 의미론)

Nhiều boolean dễ tạo impossible trạng thái (state / 상태):

```text
loading=true
success=true
error=true
```

Mô hình (model / 모델) phase rõ hơn:
<!-- merge: preserve both chuẩn gốc (canonical / 정본) variants -->
# 9. máy trạng thái (state machine / 상태 머신), UDF và kiến trúc (architecture / 아키텍처) bất biến (invariant / 불변식)

UDF không phải tên khác của MVI khung phần mềm (framework / 프레임워크). Nó là một ràng buộc (constraint / 제약조건) giúp lập luận (reasoning / 추론):

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

Điểm cấp cao (senior / 시니어) cần giữ không phải “mọi app phải có reducer”, mà là **mỗi fact quan trọng có đơn vị sở hữu (owner / 오너) và nguồn chuẩn (source of truth / 정본) rõ**. Nếu cùng một bookmark tồn tại thành mutable trạng thái (state / 상태) riêng ở cơ sở dữ liệu (database / 데이터베이스), repository bộ nhớ đệm (cache / 캐시), ViewModel và `remember`, hệ thống có bốn nơi có thể bất đồng.

## 9.1 Bắt đầu kiến trúc (architecture / 아키텍처) bằng bất biến (invariant / 불변식)

Trước khi chọn MVVM/MVI/Clean kiến trúc (architecture / 아키텍처), hãy viết bất biến (invariant / 불변식):

```text
User A không bao giờ nhìn thấy cache của User B.
Sau khi payment được server confirm, retry không tạo transaction thứ hai.
UI chỉ render article snapshot từ local source of truth.
Process recreation có thể reconstruct screen từ stable ID.
```

Kiến trúc (architecture / 아키텍처) có giá trị khi ranh giới (boundary / 경계) làm bất biến (invariant / 불변식) dễ giữ và dễ kiểm thử (test / 테스트).

## 9.2 máy trạng thái (state machine / 상태 머신) tránh impossible trạng thái (state / 상태)

Nhiều flags độc lập dễ tạo tổ hợp vô nghĩa:

```text
loading=true
fatalError=true
contentEmpty=false
paymentSucceeded=true
```

Có hai kiểu mô hình (model / 모델) phổ biến:

```text
mutually exclusive phase
→ sealed state / explicit state machine

content có thể coexist với refresh/error metadata
→ immutable data class với invariant được document
```

Không ép mọi screen thành sealed trạng thái (state / 상태) nếu UX cần cached content + refresh + warning cùng lúc. mô hình (model / 모델) phải theo nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식), không theo template.

## 9.3 Command, trạng thái (state / 상태) và sự kiện (event / 이벤트) phải phân biệt

```text
Command
= yêu cầu làm việc: Refresh, Submit, Retry

State
= fact hiện tại có thể đọc lại: PaymentCompleted, UserLoggedOut

Transient UI effect
= Snackbar "Copied", haptic, focus request
```

Nếu một fact quan trọng bị mô hình (model / 모델) thành sự kiện (event / 이벤트) một lần và collector vắng mặt thì mất, thiết kế (design / 설계) có thể sai. Durable fact nên có durable/source-of-truth biểu diễn (representation / 표현).

## 9.4 Stale snapshot là kiến trúc (architecture / 아키텍처) bug, không chỉ tính đồng thời (concurrency / 동시성) bug

Ví dụ ViewModel giữ đối tượng (object / 객체) `Article` được truyền từ danh sách (list / 목록) screen sang detail. Trong lúc detail mở, DB sync article mới. Detail vẫn hiển thị đối tượng (object / 객체) cũ vì điều hướng (navigation / 내비게이션) argument trở thành nguồn chuẩn (source of truth / 정본) thứ hai.

Tốt hơn:

```text
navigation truyền articleId
→ destination observe repository/DB theo ID
→ UI luôn thấy authoritative snapshot
```

Kiến trúc (architecture / 아키텍처) phải giải thích dữ liệu (data / 데이터) freshness và reconstruction, không chỉ phụ thuộc (dependency / 의존성) direction.
<!-- end merged variant -->

```kotlin
sealed interface LoadState {
    data object Idle : LoadState
    data object Loading : LoadState
    data class Content(val items: List<Item>, val refreshing: Boolean) : LoadState
    data class Failed(val previous: List<Item>?) : LoadState
}
```

<!-- merge: preserve both chuẩn gốc (canonical / 정본) variants -->
UDF nghĩa trạng thái (state / 상태) đi xuống, sự kiện (event / 이벤트)/hành động (action / 동작) đi lên đơn vị sở hữu (owner / 오너); không bắt buộc dùng MVI khung phần mềm (framework / 프레임워크) hay giant reducer.

Trạng thái (state / 상태) đơn vị sở hữu (owner / 오너) phải là nơi duy nhất quyết định authoritative chuyển tiếp (transition / 전이). UI cục bộ (local / 로컬) `remember` không nên cạnh tranh với cơ sở dữ liệu (database / 데이터베이스)/ViewModel cho cùng nghiệp vụ (business / 비즈니스) trạng thái (state / 상태).

# 10. Compose thời gian chạy (runtime / 런타임), định danh (identity / 식별자) và recomposition

Compose trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) tạo composition cây (tree / 트리), theo dõi trạng thái (state / 상태) reads và invalidate phạm vi (scope / 범위) liên quan. Recomposition không đồng nghĩa redraw toàn screen.

Composable body phải gần như pure kết xuất (render / 렌더링) description. Side tác động (effect / 효과) trực tiếp trong body sai vì body có thể chạy nhiều lần:
<!-- merge: preserve both chuẩn gốc (canonical / 정본) variants -->
Compose không phải “khung phần mềm (framework / 프레임워크) gọi lại toàn bộ screen mỗi khi trạng thái (state / 상태) đổi”. trình biên dịch (compiler / 컴파일러) Compose biến `@Composable` hàm (function / 함수) thành mã (code / 코드) có thêm siêu dữ liệu (metadata / 메타데이터)/thời gian chạy (runtime / 런타임) giao thức (protocol / 프로토콜); thời gian chạy (runtime / 런타임) duy trì **Composition** để nhớ cấu trúc UI, định danh (identity / 식별자) của các lời gọi (call / 호출) site và những trạng thái (state / 상태) read nào xảy ra ở đâu. Khi observable trạng thái (state / 상태) đổi, Compose invalidates đúng restart phạm vi (scope / 범위) liên quan và cố làm lượng công việc tối thiểu cần thiết.

Mô hình tư duy (mental model / 사고 모델) một frame:

```text
State/data
   ↓
Composition — UI nào tồn tại?
   ↓
Layout — đo và đặt ở đâu?
   ↓
Draw — vẽ như thế nào?
```

Recomposition chỉ nói về việc chạy lại phần **composition** cần thiết. Sau đó bố cục (layout / 레이아웃) hoặc draw có thể chạy hoặc được bỏ qua tùy kết quả. Vì vậy “recomposition count cao” tự nó chưa chứng minh UI chậm.

## 10.1 định danh (identity / 식별자) đến từ vị trí lời gọi (call / 호출) site và key

Compose cần biết instance lô-gic (logic / 논리) nào ở lần composition hiện tại tương ứng với instance nào trước đó để giữ `remember`, tác động (effect / 효과) và trạng thái (state / 상태) đúng chỗ.

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

Key phải biểu diễn định danh (identity / 식별자) bền vững, không phải chỉ mục (index / 인덱스) nếu chỉ mục (index / 인덱스) thay đổi khi insert/delete/reorder.

## 10.2 `remember` thuộc Composition, không thuộc nghiệp vụ (business / 비즈니스) đối tượng (object / 객체)

```kotlin
val state = remember(key) { expensiveInitialization(key) }
```

Giá trị được giữ khi lời gọi (call / 호출) site còn định danh (identity / 식별자) và key không đổi. `remember` không sống qua tiến trình (process / 프로세스) death; không tự sống qua việc composable rời Composition; và không phải nơi giữ dữ liệu nghiệp vụ (business / 비즈니스) lâu dài chỉ vì “muốn khỏi tải (load / 로드) lại”.

Phân lớp đơn vị sở hữu (owner / 오너):

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

## 10.3 trạng thái (state / 상태) read quyết định phase nào bị invalidated

Compose theo dõi nơi đọc trạng thái (state / 상태), không chỉ nơi trạng thái (state / 상태) được tạo. Read trong composition có thể trigger recomposition; read trong placement có thể chỉ restart bố cục (layout / 레이아웃); read trong draw có thể chỉ restart draw.

Cấp cao (senior / 시니어) tối ưu hóa (optimization / 최적화) không phải chuyển mọi read xuống phase thấp nhất bằng mẹo khó đọc; nó là hiểu đường xử lý nóng (hot path / 핫 패스) để tránh công việc (work / 작업) không cần thiết khi profiler chứng minh vấn đề.

## 10.4 Composable body phải gần pure

Composable có thể chạy lại, bị skip hoặc một composition attempt có thể không được apply. Vì vậy body không phải nơi gọi side tác động (effect / 효과) tùy ý:
<!-- end merged variant -->

```kotlin
@Composable
fun Bad(userId: String) {
    repository.load(userId) // sai owner/lifetime
}
```

<!-- merge: preserve both chuẩn gốc (canonical / 정본) variants -->
## 10.1 định danh (identity / 식별자) quan trọng như trạng thái (state / 상태)

Composition trạng thái (state / 상태) gắn với vị trí/định danh (identity / 식별자). Với danh sách (list / 목록) động, stable key giúp trạng thái (state / 상태) đi theo thực thể (entity / 엔터티):

```kotlin
LazyColumn {
    items(items, key = { it.id }) { item ->
        ItemRow(item)
    }
}
```
<!-- merge: preserve both chuẩn gốc (canonical / 정본) variants -->
UI body nên chủ yếu mô tả đầu ra (output / 출력) từ đầu vào (input / 입력)/trạng thái (state / 상태). nghiệp vụ (business / 비즈니스) side tác động (effect / 효과) thuộc sự kiện (event / 이벤트) handler/ViewModel/dữ liệu (data / 데이터) tầng (layer / 계층); tác động (effect / 효과) gắn vòng đời (lifecycle / 생명주기) UI dùng tác động (effect / 효과) API phù hợp.

# 11. Snapshot trạng thái (state / 상태), stability và hiệu năng (performance / 성능)

Compose Snapshot hệ thống (system / 시스템) cung cấp observable trạng thái (state / 상태) mô hình (model / 모델) cho thời gian chạy (runtime / 런타임). Ordinary Kotlin mutation không tự trở thành observable. Immutable snapshot hoặc Snapshot-aware collection làm mutation đặc tả hợp đồng (contract / 계약) rõ hơn.

**Immutable** và **Stable** không phải cùng khái niệm. Không annotate `@Stable`/`@Immutable` chỉ để giảm chỉ số (metric / 지표); annotation sai có thể khiến thời gian chạy (runtime / 런타임) bỏ công việc (work / 작업) cần thiết và tạo tính đúng đắn (correctness / 정확성) bug.

`derivedStateOf` hữu ích khi đầu vào (input / 입력) đổi thường xuyên nhưng đầu ra (output / 출력) ngữ nghĩa (semantic / 의미적) đổi ít hơn. `remember` bộ nhớ đệm (cache / 캐시) theo định danh (identity / 식별자)/key chứ không phải toàn cục (global / 전역) bộ nhớ đệm (cache / 캐시). Lazy danh sách (list / 목록) cần stable key; key sai không chỉ ảnh hưởng hiệu năng (performance / 성능) mà còn có thể gắn trạng thái (state / 상태)/tác động (effect / 효과) nhầm thực thể (entity / 엔터티).

Hiệu năng (performance / 성능) phải đo theo frame: composition, measure/bố cục (layout / 레이아웃), draw, allocation/GC, main-thread khối (block / 블록) và lazy reuse. tính đúng đắn (correctness / 정확성) đứng trước skip tối ưu hóa (optimization / 최적화).
<!-- end merged variant -->

Key sai có thể khiến text-field trạng thái (state / 상태)/animation của item A nhảy sang B khi reorder.

<!-- merge: preserve both chuẩn gốc (canonical / 정본) variants -->
## 10.2 tuyến (route / 경로) vs screen

```kotlin
@Composable
fun HomeRoute(viewModel: HomeViewModel) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()
    HomeScreen(state, viewModel::onAction)
<!-- merge: preserve both canonical variants -->
Compose effect API tồn tại vì composable body nên side-effect free. Chọn effect theo lifetime và cleanup contract.

`LaunchedEffect(key)` launch coroutine khi vào Composition, cancel khi rời Composition, và cancel/restart khi key đổi. Constant key như `Unit` chỉ có nghĩa “không restart vì key trong lifetime call site này”, không phải “một lần toàn app”.

`rememberUpdatedState` cho phép effect giữ lifetime hiện tại nhưng đọc callback/value mới nhất. `DisposableEffect` dùng khi có acquire/release listener/resource. `SideEffect` publish Compose state sang non-Compose object sau successful composition. `snapshotFlow` chuyển Snapshot reads thành Flow; `rememberCoroutineScope` hữu ích cho coroutine được kích hoạt từ UI event như snackbar.

Senior review phải hỏi:

```văn bản (text / 텍스트)
định danh (identity / 식별자) của tác động (effect / 효과) là gì?
key nào restart?
giá trị (value / 값) nào chỉ cần latest?
cleanup ở đâu?
leaving Composition có nên cancel thao tác (operation / 연산) không?
đây là UI tác động (effect / 효과) hay nghiệp vụ (business / 비즈니스) command?
```

# 13. Lifecycle, configuration change và process death

Configuration change thường recreate Activity nhưng ViewModel có thể sống qua recreation. Process death khác hoàn toàn: OS kill process, toàn bộ in-memory state mất. Nếu state phải restore, cần persistence/SavedStateHandle/rememberSaveable tùy loại dữ liệu.

Đừng lưu object lớn hoặc dữ liệu có thể reload vào Bundle. Bundle có giới hạn Binder transaction; stable IDs và persistence tốt hơn.

# 14. SavedStateHandle

`SavedStateHandle` cho ViewModel state cần phục hồi sau process recreation theo capability của saved state. Nó không phải database. Chỉ lưu dữ liệu nhỏ, serializable/savable hoặc identifier cần để reconstruct screen.

# 15. Multi-module architecture: boundary phải mua được giá trị

Module hóa không phải mục tiêu tự thân. Một module nên tồn tại vì ít nhất một force cụ thể: ownership/team boundary, dependency isolation, build parallelism/cache, reusable public contract, optional delivery hoặc giới hạn accidental coupling.

Một graph có thể như:

```văn bản (text / 텍스트)
:app
  ↓
:tính năng (feature / 기능):home:impl ─────→ :tính năng (feature / 기능):home:api
  ↓                           ↑
:cốt lõi (core / 핵심):dữ liệu (data / 데이터) ─────→ :cốt lõi (core / 핵심):mô hình (model / 모델) │
  ↓                           │
:cốt lõi (core / 핵심):cơ sở dữ liệu (database / 데이터베이스) / :cốt lõi (core / 핵심):mạng (network / 네트워크)
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

```văn bản (text / 텍스트)
Settings / dự án (project / 프로젝트) discovery
→ cấu hình (configuration / 구성)
→ variant/tác vụ (task / 작업) đồ thị (graph / 그래프)
→ tác vụ (task / 작업) thực thi (execution / 실행)
→ trình biên dịch (compiler / 컴파일러)/mã (code / 코드) generation
→ tài nguyên (resource / 자원) + manifest processing
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

```văn bản (text / 텍스트)
nguồn (source / 소스) lần ghi nhận (commit / 커밋)
Gradle wrapper
AGP/Kotlin/JDK
resolved phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)
bản dựng (build / 빌드) variant/flavor
R8 rules
signing định danh (identity / 식별자)/tiến trình (process / 프로세스)
tính năng (feature / 기능)/cấu hình (config / 설정) inputs
```

Dynamic version như `1.+` phá reproducibility vì cùng commit có thể resolve dependency khác ở ngày khác.

## 16.3 Debug build pass không chứng minh release pass

Release có thể khác debug ở:

```văn bản (text / 텍스트)
R8 shrinking/tối ưu hóa (optimization / 최적화)/obfuscation
tài nguyên (resource / 자원) shrinking
BuildConfig/manifest giá trị (value / 값)
signing
proguard bên tiêu thụ (consumer / 소비자) rules
cờ tính năng (feature flag / 기능 플래그)/môi trường (environment / 환경)
bản địa (native / 네이티브) symbols
```

Vì vậy CI cần compile/test release-like variant. Lỗi reflection/JNI/serialization chỉ xuất hiện sau minify là failure mode bình thường cần được thiết kế test.

## 16.4 Debugging theo exact variant

Khi bug chỉ xảy ra ở `prodRelease`, đừng reproduce bằng `devDebug` rồi kết luận. Ghi exact tuple:

```văn bản (text / 텍스트)
lần ghi nhận (commit / 커밋) + variant + thiết bị (device / 장치)/API + phụ thuộc (dependency / 의존성) khóa (lock / 잠금) + máy chủ (server / 서버)/cấu hình (config / 설정) phiên bản (version / 버전)
```

Forensics bắt đầu từ artifact thật, không từ source “trông giống”.

# 17. DI ở quy mô lớn: graph và lifetime contract

DI không phải architecture; DI quản lý object graph và creation/lifetime. Scope phải phản ánh owner thật:

```văn bản (text / 텍스트)
ứng dụng (application / 애플리케이션) singleton
session scoped
activity/điều hướng (navigation / 내비게이션) đồ thị (graph / 그래프) scoped
ViewModel scoped
transient
```

Một object stateful vô tình `@Singleton` có thể leak data qua account switch. Một Activity Context bị giữ trong singleton tạo memory leak. Constructor injection làm dependency explicit nhưng không tự bảo đảm scope đúng.

Hilt/Dagger compile-time graph giúp verify dependency. Assisted injection hữu ích khi một số input là runtime identity như `itemId`. Multibinding phù hợp registry/plugin model. Không tạo interface cho mọi class chỉ để DI “đẹp”; seam phải phản ánh volatility/test requirement thật.

# 18. Offline-first, source of truth và sync correctness

Offline-first không chỉ là “cache API response”. Phải định nghĩa consistency contract giữa local và remote.

Một pattern production:

```văn bản (text / 텍스트)
UI observe cục bộ (local / 로컬) DB
mạng (network / 네트워크) refresh/sync
    ↓
giao dịch (transaction / 트랜잭션) cập nhật (update / 업데이트) cục bộ (local / 로컬) DB
    ↓
DB emit authoritative snapshot
    ↓
UI cập nhật (update / 업데이트)
```

## 18.1 Read-offline và write-offline khác độ khó

Read cache chỉ cần freshness/revalidation policy. Write-offline cần durable pending mutation, idempotency, ordering, conflict, retry và account isolation.

Nếu product không cần offline mutation, đừng xây distributed sync engine chỉ vì “offline-first nghe hiện đại”.

## 18.2 Ambiguous outcome

Request timeout không có nghĩa server chưa commit:

```văn bản (text / 텍스트)
máy khách (client / 클라이언트) gửi POST
máy chủ (server / 서버) lần ghi nhận (commit / 커밋)
phản hồi (response / 응답) mất
máy khách (client / 클라이언트) thấy hết thời gian chờ (timeout / 타임아웃)
```

Nếu retry mù, duplicate side effect có thể xuất hiện. Idempotency key/server contract mới giải quyết được nhóm failure này.

## 18.3 Durable outbox invariant

Nếu local optimistic update và pending operation phải luôn cùng tồn tại, ghi chúng trong cùng local transaction:

```văn bản (text / 텍스트)
thực thể (entity / 엔터티) trạng thái (state / 상태) changed
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

```văn bản (text / 텍스트)
công việc (work / 작업) chỉ có ý nghĩa khi screen còn sống
→ ViewModel/vòng đời (lifecycle / 생명주기) coroutine

Công việc (work / 작업) user-visible đang chạy liên tục
→ foreground dịch vụ (service / 서비스) nếu nền tảng (platform / 플랫폼) chính sách (policy / 정책)/use trường hợp (case / 사례) cho phép

Công việc (work / 작업) có thể trì hoãn nhưng cần eventually execute
→ WorkManager

đúng thời điểm gần tuyệt đối
→ alarm API chỉ khi use trường hợp (case / 사례) đủ điều kiện

server-triggered tín hiệu (signal / 신호)
→ push/FCM, sau đó app quyết định công việc (work / 작업) phù hợp
```

Service không phải thread. WorkManager không phải sync correctness engine; nó schedule execution, còn idempotency/source-of-truth/retry semantic thuộc business/data design.

Production failure cần test Doze, battery saver, process kill, reboot, network mất/đổi, permission revoke và duplicate scheduling nếu relevant.

# 21. Security production: threat model trước API

Mobile client là môi trường người dùng kiểm soát. Attacker có thể decompile APK, hook method, inspect memory, chạy rooted/emulated environment hoặc gửi Intent/deep link trực tiếp.

## 21.1 Trust boundary

```văn bản (text / 텍스트)
client-side role check
= UX tối ưu hóa (optimization / 최적화)

backend authorization
= bảo mật (security / 보안) authority
```

Không nhúng server secret dài hạn rồi trông chờ R8/obfuscation bảo vệ. Keystore bảo vệ key material tốt hơn file plaintext nhưng không biến compromised device thành trusted server.

## 21.2 External input phải coi là untrusted

Các boundary cần validate:

```văn bản (text / 텍스트)
Intent/deep link
exported Activity/dịch vụ (service / 서비스)/Receiver/Provider
PendingIntent
content URI/FileProvider
WebView điều hướng (navigation / 내비게이션)/JS cầu nối (bridge / 브리지)
notification hành động (action / 동작)
Binder/bản địa (native / 네이티브) đầu vào (input / 입력)
```

Kiểm tra scheme/host/path/ID, authorization sau navigation, URI grant tối thiểu và `android:exported` có chủ đích.

## 21.3 Token/session security là lifecycle problem

Token có expiry/refresh/revoke. Concurrent `401` cần single-flight refresh; logout cần vô hiệu session state, cancel/namespace pending work và không để response của account cũ update state account mới.

Không log token/PII. Telemetry schema phải có privacy review vì observability cũng là data export surface.

## 21.4 Certificate pinning có operational cost

Pinning chỉ dùng khi threat model biện minh và có rotation/recovery plan. Certificate/key thay đổi không được chuẩn bị có thể biến security control thành outage toàn app.

# 22. Performance, memory và battery: evidence before optimization

Performance engineering theo vòng:

```văn bản (text / 텍스트)
user-visible chỉ số (metric / 지표)
→ reproduce trên representative thiết bị (device / 장치)
→ dấu vết (trace / 추적)/profile
→ hypothesis
→ one controlled thay đổi (change / 변경)
→ measure lại
→ regression guard
```

Các metric khác nhau cần tool khác nhau:

```văn bản (text / 텍스트)
startup TTID/TTFD
frame thời gian (time / 시간)/jank
CPU đường xử lý nóng (hot path / 핫 패스)
allocation/GC/bộ nhớ (memory / 메모리) peak
DB độ trễ (latency / 지연 시간)/kế hoạch truy vấn (query plan / 쿼리 계획)
mạng (network / 네트워크) độ trễ (latency / 지연 시간)/bytes
battery/background wakeup
APK/download kích thước (size / 크기)
```

Macrobenchmark phù hợp startup/interaction ở package level; Perfetto/System Trace nhìn thread/system timeline; memory profiler tìm retention/allocation; baseline profile cải thiện compiled hot path nhưng không sửa algorithm chậm.

## 22.1 Tail latency quan trọng hơn average đẹp

Average 8 ms không có nghĩa smooth nếu p95/p99 có frame 80–150 ms. Production telemetry nên segment theo device class/OS/network nếu metric nhạy với environment.

## 22.2 Memory leak = lifetime mismatch

Các pattern thường gặp:

```văn bản (text / 텍스트)
singleton giữ Activity/View
listener không unregister
Fragment binding sống sau onDestroyView
coroutine phạm vi (scope / 범위) sống dài hơn đơn vị sở hữu (owner / 오너)
unbounded bộ nhớ đệm (cache / 캐시)
callback/lambda capture đối tượng (object / 객체) đồ thị (graph / 그래프) lớn
```

GC không thể thu object còn reachable. Debug bằng retention path thay vì gọi `System.gc()`.

## 22.3 Battery là scheduling + radio + sensor problem

Polling thường xuyên, location high accuracy liên tục, wakeup quá nhiều và retry storm đều tốn pin. Batch work, chọn constraint hợp lý, debounce/throttle khi đúng semantic và dừng sensor/camera/BLE theo lifecycle/resource ownership.

# 23. Networking nâng cao: failure taxonomy trước retry

Phân biệt:

```văn bản (text / 텍스트)
DNS/connectivity/hết thời gian chờ (timeout / 타임아웃)
TLS thất bại (failure / 실패)
HTTP giao thức (protocol / 프로토콜) status
serialization/lược đồ (schema / 스키마) thất bại (failure / 실패)
auth/session miền lỗi (failure domain / 장애 도메인) kiểm tra hợp lệ (validation / 검증)/xung đột (conflict / 충돌)
ambiguous kết quả (outcome / 결과) sau side tác động (effect / 효과)
```

Không map tất cả thành `NetworkError` rồi retry.

OkHttp interceptor chain có application/network interceptor với semantics khác. Token refresh cần tránh thundering herd khi nhiều request cùng `401`; mutex/single-flight có thể phù hợp nếu lock scope đúng.

Timeout cần phân biệt connect/read/write/call. Retry chỉ an toàn khi operation idempotent hoặc backend có idempotency key. Backoff nên có jitter ở fleet lớn để tránh nhiều client retry cùng lúc.

HTTP cache và application DB cache là hai layer khác nhau. Cache policy phải xác định freshness, validation và source of truth.

# 24. Database nâng cao: transaction là invariant boundary

Room transaction không chỉ để “chạy nhanh hơn”; nó bảo đảm nhóm write quan trọng commit/rollback cùng nhau.

```kotlin
@giao dịch (transaction / 트랜잭션)
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

```văn bản (text / 텍스트)
yêu cầu (request / 요청) A bắt đầu
yêu cầu (request / 요청) B bắt đầu
B success
A success muộn
→ assert A không overwrite B
```

Các failure test có giá trị cao:

```văn bản (text / 텍스트)
tiến trình (process / 프로세스) death giữa luồng (flow / 흐름)
DB di chuyển (migration / 마이그레이션) từ lược đồ (schema / 스키마) thực
mạng (network / 네트워크) hết thời gian chờ (timeout / 타임아웃) sau remote lần ghi nhận (commit / 커밋)
401 đồng thời
permission revoke
disk full / serialization corrupt nếu lĩnh vực (domain / 도메인) quan trọng
R8/minified bản phát hành (release / 릴리스)
quay lui (rollback / 롤백) đọc dữ liệu (data / 데이터) phiên bản (version / 버전) mới
```

Compose UI test nên query semantics phản ánh meaning/accessibility thay vì chỉ testTag nếu có thể.

# 26. Java interoperability

Annotations quan trọng gồm `@JvmStatic`, `@JvmField`, `@JvmOverloads`, `@JvmName`, `@Throws`. Không dùng tự động; chỉ thêm khi Java caller cần API shape tương ứng.

SAM conversion hoạt động tốt với Java functional interface và Kotlin `fun interface`.

```kotlin
fun giao diện (interface / 인터페이스) Listener {
    fun onEvent(value: String)
<!-- end merged variant -->
}
```

`HomeScreen` nên render state + forward action. Route xử lý lifecycle/navigation/DI. Cách này giúp preview/test và giảm coupling.

# 11. Snapshot state, stability và phase performance

Compose frame có các phase chính:

```văn bản (text / 텍스트)
Composition
→ bố cục (layout / 레이아웃)
→ Draw
```

State đọc ở phase nào quyết định phase nào bị invalidated. Đọc scroll offset chỉ để draw alpha không nhất thiết phải trigger recomposition toàn subtree nếu có API phase phù hợp.

`@Stable`/`@Immutable` là **contract**, không phải performance hint vô hại. Annotate sai có thể khiến runtime skip trong khi object mutate không observable.

<!-- merge: preserve both canonical variants -->
`remember` cache theo composition lifetime/key, không phải global memoization. `derivedStateOf` hữu ích khi derived value thay đổi ít hơn source; dùng ở mọi chỗ tạo overhead không cần thiết.
<!-- merge: preserve both canonical variants -->
Public API cần document cả **behavioral contract**: threading, cancellation, ordering, replay, nullability, ownership và failure; type signature một mình chưa đủ.

# 28. Design patterns và Kotlin idioms
<!-- end merged variant -->

# 12. Side effects và lifetime

`LaunchedEffect(key)` restart coroutine khi key thay đổi. `DisposableEffect` cho resource cần register/unregister. `rememberUpdatedState` cập nhật callback/value mà không restart effect. `SideEffect` sync outward sau successful composition.

<!-- merge: preserve both canonical variants -->
Senior review hỏi hai câu:

```văn bản (text / 텍스트)
tác động (effect / 효과) này thuộc vòng đời (lifecycle / 생명주기) nào?
Nếu screen biến mất, công việc (work / 작업) có nên tiếp tục không?
```

Nếu phải tiếp tục sau navigation/process background, owner có thể là ViewModel/repository/WorkManager thay vì composition.

# 13. Android lifecycle, configuration change và process death

Phải phân biệt bốn lớp lifetime:

```văn bản (text / 텍스트)
recomposition
< composable destination
< Activity/Fragment instance
< tiến trình (process / 프로세스)
< persistent lưu trữ (storage / 저장소)/máy chủ (server / 서버)
```

Configuration change recreate Activity/Fragment instance nhưng ViewModel có thể sống qua recreation. Process death giết toàn bộ in-memory state: ViewModel, singleton, coroutine scope, object cache đều biến mất.

## 13.1 State placement theo khả năng phục hồi

```văn bản (text / 텍스트)
render-local ephemeral trạng thái (state / 상태)
→ remember

small UI trạng thái (state / 상태) cần survive recreation
→ rememberSaveable / SavedStateHandle

screen/nghiệp vụ (business / 비즈니스) trạng thái (state / 상태)
→ ViewModel + nguồn chuẩn (source of truth / 정본)

large/durable dữ liệu (data / 데이터)
→ cơ sở dữ liệu (database / 데이터베이스)/tệp (file / 파일)/máy chủ (server / 서버)
```

Không nhét object lớn/list vào Bundle. Binder/saved-state có limit và object lớn thường reconstruct được từ stable ID.

## 13.2 Lifecycle-aware collection

Flow UI collection phải gắn lifecycle phù hợp. Compose dùng `collectAsStateWithLifecycle()` cho Android UI thường an toàn hơn collect không lifecycle-aware. Trong View system, `repeatOnLifecycle` giúp start/cancel collector theo state lifecycle.

# 14. SavedStateHandle và state reconstruction

`SavedStateHandle` không phải database. Nó phù hợp query/filter/entity ID/navigation argument hoặc small form state cần reconstruct sau process recreation.

Pattern tốt:

```văn bản (text / 텍스트)
SavedStateHandle giữ articleId
→ ViewModel khởi tạo lại
→ repository/Room tải (load / 로드) Article(articleId)
→ UI trạng thái (state / 상태) được reconstruct
```

Pattern xấu: serialize toàn `Article` graph/list/cache vào saved state rồi coi đó là source of truth.

# 15. Multi-module architecture

Module hóa để enforce direction/ownership/build isolation, không để tăng số folder. Feature public API nên nhỏ. Tránh circular dependency và `core:common` god-module.

# 16. Build system và Gradle performance

Nắm configuration phase, task graph, incremental build, build/configuration cache, source set, variants, KSP/kapt cost và dependency resolution. Tránh dynamic version `1.+` và hidden I/O trong configuration.

# 17. Dependency Injection ở quy mô lớn

DI quản lý dependency graph/lifetime, không phải architecture. Scope phải khớp owner: singleton giữ Activity là leak; stateful session object singleton có thể leak user state giữa logout/login nếu reset contract không rõ.

# 18. Offline-first, cache và sync

Local DB thường là source of truth cho read path. Mutation offline cần durable pending operation, idempotency, ordering/conflict strategy và retry classification. Timeout sau request gửi đi có thể là **ambiguous outcome**: server đã commit nhưng client không nhận response.

Không xây sync engine nếu product chỉ cần read cache. Complexity phải theo requirement.

# 19. Pagination và Paging 3

`Pager`, `PagingSource`, `RemoteMediator` giúp page từ DB/network. Refresh/append/prepend error có semantics riêng; append fail không nên xóa content đang hiển thị.

# 20. Background execution policy

Chọn primitive theo lifetime/durability:

```văn bản (text / 텍스트)
screen-bound công việc (work / 작업) → viewModelScope/coroutine
short vòng đời (lifecycle / 생명주기) UI công việc (work / 작업) → vòng đời (lifecycle / 생명주기)/composition phạm vi (scope / 범위)
persisted deferrable guaranteed công việc (work / 작업) → WorkManager
user-visible ongoing công việc (work / 작업) → foreground dịch vụ (service / 서비스) nếu use trường hợp (case / 사례)/chính sách (policy / 정책) cho phép
chính xác (exact / 정확한) wall-clock need → chính xác (exact / 정확한) alarm khi đủ điều kiện
```

Service không phải thread. WorkManager không phải general async replacement cho mọi request.

# 21. Security production

Threat model xem APK/device là untrusted. Backend phải authorize. Validate exported component/deep link/PendingIntent/URI/WebView input. R8 không phải secret storage.

WebView + JavaScript bridge là high-risk boundary. Chỉ expose capability tối thiểu, validate URL/origin và tránh token trong URL/log.

# 22. Performance, memory và battery

Đo startup, frame/jank, memory, network, DB, battery trên thiết bị đại diện. Leak thường do long-lived owner giữ short-lived Activity/View/listener/callback hoặc coroutine scope sai lifetime.

Performance optimization phải theo:

```văn bản (text / 텍스트)
chỉ số (metric / 지표) → dấu vết (trace / 추적) → hypothesis → thay đổi (change / 변경) → verify
```

# 23. Networking nâng cao

Timeout cần phân biệt call/connect/read/write. Retry chỉ khi operation idempotent hoặc backend có idempotency key. Token refresh cần single-flight để tránh hàng chục 401 cùng refresh.

# 24. Database nâng cao

Room transaction bảo vệ invariant trong DB boundary. Index theo query pattern; quá nhiều index tăng write/storage. Migration test cần schema cũ + data thật đại diện → migrate → assert schema/data.

# 25. Testing strategy

Test theo risk. Pure logic test nhanh, integration test cho serialization/DB/network/DI, instrumented/Compose test cho platform semantics. Test race bằng scheduler/barrier/fake controllable, không `delay()` ngẫu nhiên rồi hy vọng timing.

# 26. Java interoperability

`@JvmStatic`, `@JvmField`, `@JvmOverloads`, `@JvmName`, `@Throws` chỉ dùng khi Java caller cần API shape đó. Public Kotlin API nên review Java ergonomics nếu module có Java consumer.

# 27. API design bằng Kotlin

API tốt làm ownership/failure semantics explicit. Tránh boolean khó đọc và generic `Any`. Prefer type-safe domain model, immutable state và sealed result khi phù hợp.

# 28. Common design patterns và Kotlin idioms

Kotlin làm nhiều GoF pattern nhẹ hơn: Strategy bằng function type, Singleton bằng `object`, Decorator bằng delegation, Observer bằng Flow, State bằng sealed hierarchy. Pattern là giải pháp cho force cụ thể, không phải huy hiệu senior.

# 29. Modern vs legacy API và migration strategy

Đây là điểm thường bị tài liệu Android giải thích quá đơn giản. Không phải API cũ nào cũng phải xóa.

Phân loại trước khi migrate:

```văn bản (text / 텍스트)
A. Deprecated/unsafe
→ lập kế hoạch migrate

B. Supported nhưng replacement mới có benefit rõ
→ migrate incremental khi đáng chi phí

C. Still-valid cho use trường hợp (case / 사례) cụ thể
→ giữ

D. Historical
→ biết để maintain, không chọn cho mã (code / 코드) mới
```

## 29.1 Bản đồ legacy → modern

| Legacy / older stack | Modern direction | Reasoning |
|---|---|---|
| Java-heavy | Kotlin-first | Java vẫn fully relevant cho interop/legacy |
| Kotlin synthetic view | View Binding / Compose | synthetic không còn modern workflow |
| `findViewById` | View Binding / Compose | vẫn valid trong custom/View code |
| XML + Fragment | Compose hoặc hybrid | XML/Fragment vẫn supported |
| `AsyncTask` | coroutine / WorkManager theo lifetime | replacement phụ thuộc durability |
| callback pyramid | suspend / Flow | callback vẫn đúng ở SDK boundary |
| LiveData-centric | Flow/StateFlow ở modern Kotlin stack | LiveData vẫn dùng được |
| RxJava-heavy | coroutine/Flow thường phổ biến hơn | không rewrite nếu cost/risk không có lợi |
| SharedPreferences | DataStore cho structured settings | migration theo data/behavior contract |
| `startActivityForResult` | Activity Result API | lifecycle-aware registration/result |
| manual Service cho deferred work | WorkManager | Service còn đúng cho ongoing work |
| kapt | KSP khi processor hỗ trợ | migrate từng processor |
| `kotlinOptions {}` | `compilerOptions {}` | modern Kotlin Gradle DSL |
| K1 | K2 | compiler generation mới |

## 29.2 Migration giữ behavior trước, đổi implementation sau

Ví dụ RxJava repository cũ có thể adapter sang Flow ở boundary thay vì rewrite data layer cùng lúc. XML Fragment có thể host `ComposeView`, hoặc Compose có thể host `AndroidView`. Java module có thể được gọi từ Kotlin mà chưa cần convert tất cả.

Characterization test bảo vệ behavior hiện tại trước khi refactor. Strangler migration cho phép feature/screen mới dùng stack modern trong khi path cũ vẫn chạy; khi telemetry/test đủ confidence mới xóa legacy.

## 29.3 Đừng nhầm modern với architecture tốt

Compose + Flow + Hilt + Kotlin 2.x vẫn có thể có duplicated state, leaked scope, race và god ViewModel. Ngược lại XML + Fragment + RxJava có thể có contract/test rất tốt. Migration phải mua được giá trị: safety, maintainability, policy compatibility, performance hoặc developer productivity.

# 30. Senior review checklist

Review theo invariant/lifetime thay vì syntax:

```văn bản (text / 텍스트)
trạng thái (state / 상태) đơn vị sở hữu (owner / 오너)/nguồn chuẩn (source of truth / 정본)?
tiến trình (process / 프로세스) death reconstruct thế nào?
coroutine phạm vi (scope / 범위) đơn vị sở hữu (owner / 오너)?
cancellation propagate không?
race/stale kết quả (result / 결과) có thể xảy ra không?
luồng (flow / 흐름) hot/cold/replay đúng ngữ nghĩa (semantics / 의미론) không?
Compose tác động (effect / 효과) đúng thời gian tồn tại (lifetime / 수명) không?
thao tác (operation / 연산) thử lại (retry / 재시도)/idempotent không?
legacy API thuộc nhóm A/B/C/D nào?
ranh giới bảo mật (security boundary / 보안 경계) nào nhận đầu vào (input / 입력) không tin cậy?
hiệu năng (performance / 성능) chỉ số (metric / 지표) nào quan trọng?
bản phát hành (release / 릴리스)/minified đường dẫn (path / 경로) có kiểm thử (test / 테스트) không?
```
<!-- merge: preserve both canonical variants -->
# 29. Legacy migration: strangler thay big-bang

Migration Java → Kotlin hoặc XML → Compose nên tạo seam và di chuyển incrementally.

Ví dụ:

```văn bản (text / 텍스트)
Rx repository cũ
→ adapter ranh giới (boundary / 경계) expose luồng (flow / 흐름) cho tính năng (feature / 기능) mới
→ migrate caller dần
→ đo/kiểm thử (test / 테스트)
→ xóa Rx đường dẫn (path / 경로) khi không còn bên tiêu thụ (consumer / 소비자)
```

Hoặc:

```văn bản (text / 텍스트)
Fragment host cũ
→ ComposeView cho leaf screen mới
→ điều hướng (navigation / 내비게이션)/vòng đời (lifecycle / 생명주기) vẫn giữ đặc tả hợp đồng (contract / 계약) cũ
→ migrate screen theo rủi ro (risk / 위험)/quyền sở hữu (ownership / 소유권)
```

Mỗi migration phải có:

```văn bản (text / 텍스트)
hành vi (behavior / 동작) baseline
entry/exit criteria
coexistence đặc tả hợp đồng (contract / 계약)
telemetry/kiểm thử (test / 테스트)
quay lui (rollback / 롤백)/fallback
đơn vị sở hữu (owner / 오너)
ngày/điều kiện xóa legacy
```

Convert source tự động không đồng nghĩa migration semantic hoàn tất.

# 30. Senior review checklist

Review theo chain thay vì theo framework:

```văn bản (text / 텍스트)
yêu cầu (requirement / 요구사항)
→ bất biến (invariant / 불변식)
→ đơn vị sở hữu (owner / 오너)/thời gian tồn tại (lifetime / 수명)
→ nguồn chuẩn (source of truth / 정본)
→ chuyển tiếp trạng thái (state transition / 상태 전이)
→ thực thi (execution / 실행) ngữ cảnh (context / 맥락)
→ tính đồng thời (concurrency / 동시성)/thứ tự (ordering / 순서)
→ bên ngoài (external / 외부) ranh giới (boundary / 경계)
→ thất bại (failure / 실패)/thử lại (retry / 재시도)/idempotency
→ persistence/reconstruction
→ bảo mật (security / 보안)/privacy
→ hiệu năng (performance / 성능) ngân sách (budget / 예산)
→ kiểm thử (test / 테스트) bằng chứng (evidence / 증거)
→ bản dựng (build / 빌드)/sản phẩm tạo ra (artifact / 산출물)
→ rollout/quay lui (rollback / 롤백)
```

Một feature chưa production-ready nếu chỉ trả lời “dùng MVVM + Hilt + Room + Compose” nhưng không giải thích được race, process death, stale data, retry, security boundary hoặc rollback.

---

## Senior Notes tổng kết

Code Android production bền không đến từ việc dùng nhiều library nhất mà từ việc đặt đúng ownership và giữ invariant. State thuộc ai, coroutine thuộc scope nào, database là source of truth hay cache, retry thuộc layer nào, error được map ở boundary nào, event có thực sự là event hay chỉ là state chưa model đúng, dependency sống bao lâu, và behavior nào phải survive process death. Seniority thể hiện ở khả năng trả lời rõ những câu hỏi đó trước khi bug xảy ra.

---
<!-- end merged variant -->

# 31. Channel, Mutex, atomic và shared mutable state

Coroutine không loại data race. `Mutex` phù hợp critical section suspend-aware; atomic cho operation nhỏ; Channel cho message hand-off/queue; actor/single-owner cho ordered mutation.

```kotlin
private val mutex = Mutex()
private var cached: đơn vị từ (token / 토큰)? = null

suspend fun đơn vị từ (token / 토큰)(): đơn vị từ (token / 토큰) = mutex.withLock {
    cached ?: refreshToken().also { cached = it }
}
```

<!-- merge: preserve both canonical variants -->
Ví dụ trên single-flight nhưng giữ lock trong network call. Tùy design có thể cần deferred-in-flight state để không giữ lock rộng. Primitive phải theo invariant, không theo template.

# 32. Coroutine scheduler, dispatcher injection và starvation

Blocking I/O, CPU-heavy và main-thread UI có execution need khác nhau. Dispatcher injection giúp test/main-safety nhưng không cần inject năm dispatcher vào mọi class.

Starvation xảy ra khi blocking work giữ pool thread, lock dài hoặc CPU parallelism vượt budget. Phân biệt coroutine `suspended` với thread `blocked` khi đọc profiler/stack trace.
<!-- merge: preserve both canonical variants -->
Ví dụ trên còn gợi ý pattern single-flight. Tuy nhiên nếu `refreshToken()` lâu hoặc re-enter dependency khác, phải xem lock scope để tránh contention/deadlock logic. Trước tiên giảm shared mutable state và xác định owner rồi mới chọn primitive.

`Channel` không thay thế Flow. Flow phù hợp stream/declarative transformation; Channel phù hợp queue/message hand-off. Tránh Channel như event bus toàn app vì ownership/backpressure khó kiểm soát.

# 32. Coroutine scheduler, dispatcher injection và starvation

`Dispatchers.IO` và `Dispatchers.Default` có mục đích khác nhau. Blocking I/O nên tách khỏi CPU-bound work. Đưa vòng lặp CPU nặng vào IO không biến nó thành I/O.

Dispatcher injection làm code testable và giúp data layer kiểm soát main-safety. Thread starvation có thể xảy ra khi blocking call trong pool nhỏ, lock quá lâu hoặc quá nhiều CPU work đồng thời. Khi profile, phân biệt coroutine suspend với thread blocked.

# 33. Compose performance: từ invalidation tới frame evidence
<!-- end merged variant -->

Recomposition count tự nó không phải bug. Compose có ba phase chính cho frame: composition → layout → draw, và Snapshot state read ở phase nào quyết định work có thể restart khi state đổi.

<!-- merge: preserve both canonical variants -->
Recomposition count không tự là bug. Quan tâm frame time, expensive composition/layout/draw, allocation và invalidation scope. `remember`/`derivedStateOf` chỉ dùng khi semantics đúng và measurement chỉ ra benefit.

# 34. Main thread, ANR, StrictMode và leak

UI thread xử lý input/lifecycle/draw orchestration. Disk/network, JSON parse, DB, bitmap decode hoặc lock contention đều có thể gây jank/ANR.

`StrictMode` hữu ích ở debug để phát hiện một số policy violation. Leak investigation cần retention path; `System.gc()` không sửa reachable reference.

# 35. R8, shrinking và keep rules

Reflection/JNI/name-based lookup có thể bị R8 ảnh hưởng. Keep rule phải hẹp. Library tự cần rule thì nên ship consumer rules. Release crash cần mapping đúng artifact để deobfuscate.

# 36. Signing, APK/AAB và release reproducibility

Release artifact phải ký. Quản lý signing/upload key như credential dài hạn. Reproducibility nghĩa trace được source commit, dependency versions, Gradle/JDK/toolchain/config đã tạo artifact.

# 37. API-level compatibility, behavior change và feature gating
<!-- merge: preserve both canonical variants -->
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

```văn bản (text / 텍스트)
gỡ lỗi (debug / 디버그) pass + bản phát hành (release / 릴리스) thất bại (fail / 실패)
→ compare minify/tài nguyên (resource / 자원) shrink/BuildConfig/manifest/signing
→ inspect R8 diagnostics/ánh xạ (mapping / 매핑)/usage
→ reproduce chính xác (exact / 정확한) bản phát hành (release / 릴리스) variant
```

# 36. Signing, APK/AAB và release reproducibility

Android artifact release phải được ký. Release signing key/upload key là credential operational quan trọng.

Build reproducibility nghĩa release truy ra được source commit, dependency graph, wrapper/JDK/toolchain, variant, config, R8 mapping, native symbols và signing process.

AAB là publishing artifact; thiết bị thường nhận split APK phù hợp configuration. Vì vậy verify install/delivery path khi bug liên quan ABI/resource/language split, không chỉ inspect `.aab` upload.
<!-- end merged variant -->

`compileSdk` cho symbol compile-time; `minSdk` cho runtime floor; `targetSdk` opt-in platform behavior contract. Khi nâng target, phải audit behavior changes, không chỉ sửa số Gradle.

<!-- merge: preserve both canonical variants -->
API mới cần runtime guard/compat abstraction nếu minSdk thấp hơn. Platform latest và Play target requirement là hai khái niệm khác nhau.

# 38. WebView như một security boundary

Validate scheme/host/navigation. Cấu hình JavaScript/file access/debugging theo threat model. `addJavascriptInterface` chỉ cho trusted content và API tối thiểu. Token không nên nằm tùy tiện trong URL.

# 39. Database migration và schema evolution

Production migration phải bảo vệ data thật. Test từ nhiều schema version còn tồn tại, không chỉ previous → latest. Với sync app, local schema migration còn phải tương thích rollout backend/client lệch version.
<!-- merge: preserve both canonical variants -->
`minSdk`, `compileSdk`, `targetSdk` là ba contract khác nhau. Code gọi API mới trên OS cũ cần guard hoặc compat abstraction.

Nâng `targetSdk` là behavior migration: test notification, permission, background execution, storage, window/insets, exported component và policy thay đổi. Nên tách target migration khỏi Kotlin/AGP migration khi có thể để forensic rõ.

Tại baseline này Android 17 là API 37, trong khi Play target requirement có thể thấp hơn latest platform. Latest SDK và distribution requirement không phải cùng một khái niệm.

# 38. WebView như một security boundary

WebView kết hợp web security model với native app privilege. Validate external URL scheme/host, quyết định domain nào được ở trong WebView, hạn chế file access/JS/debugging theo threat model và cực kỳ thận trọng với `addJavascriptInterface`.

Authentication token không nên nhét tùy tiện vào URL. Certificate pinning chỉ dùng khi có operational plan cho rotation/recovery.

# 39. Database migration và schema evolution trong production

Room migration phải coi dữ liệu người dùng là tài sản. Test từ schema cũ thực tế, insert dữ liệu đại diện, chạy migration rồi verify schema + data.

Với staged rollout, app version cũ và mới có thể cùng tồn tại. Local data, remote payload và server behavior phải có compatibility window. Nếu migration irreversible, binary rollback có thể không cứu được user đã mở app version mới.
<!-- end merged variant -->

# 40. Production failure model và Senior decision framework

<!-- merge: preserve both canonical variants -->
Khi gặp feature mới, đi theo chuỗi:

```văn bản (text / 텍스트)
yêu cầu (requirement / 요구사항)
→ bất biến (invariant / 불변식)
→ đơn vị sở hữu (owner / 오너)/thời gian tồn tại (lifetime / 수명)
→ trạng thái (state / 상태)/nguồn chuẩn (source of truth / 정본)
→ tính đồng thời (concurrency / 동시성)/thứ tự (order / 순서)
→ cancellation/thất bại (failure / 실패)/thử lại (retry / 재시도)
→ persistence/reconstruction
→ nền tảng (platform / 플랫폼)/phiên bản (version / 버전) tính tương thích (compatibility / 호환성)
→ bảo mật (security / 보안)
→ bằng chứng hiệu năng (performance evidence / 성능 증거)
→ tests
→ bản phát hành (release / 릴리스)/quay lui (rollback / 롤백)
```

Nếu chuỗi này rõ, việc chọn MVVM/MVI, Hilt/Koin, Room/SQLDelight hay Retrofit/Ktor trở thành quyết định có lý do thay vì preference.
<!-- merge: preserve both canonical variants -->
Mobile production không chạy theo happy path. Một feature nên được review với failure matrix:

```văn bản (text / 텍스트)
tiến trình (process / 프로세스)
- cấu hình (configuration / 구성) recreate
- tiến trình (process / 프로세스) kill
- app cập nhật (update / 업데이트)
- thiết bị (device / 장치) reboot

Tính đồng thời (concurrency / 동시성)
- duplicate tap
- yêu cầu (request / 요청) A/B out of thứ tự (order / 순서)
- 401 storm
- worker + foreground UI cùng mutate

Mạng (network / 네트워크)
- offline
- hết thời gian chờ (timeout / 타임아웃) trước lần ghi nhận (commit / 커밋)
- hết thời gian chờ (timeout / 타임아웃) sau remote lần ghi nhận (commit / 커밋)
- partial payload/lược đồ (schema / 스키마) drift

Persistence
- di chuyển (migration / 마이그레이션)
- disk full/corrupt dữ liệu (data / 데이터)
- giao dịch (transaction / 트랜잭션) partiality
- quay lui (rollback / 롤백) nhị phân (binary / 이진) đọc lược đồ (schema / 스키마) mới

Nền tảng (platform / 플랫폼)
- permission revoke
- targetSdk hành vi (behavior / 동작) thay đổi (change / 변경)
- OEM/WebView difference
- background restriction

Bản phát hành (release / 릴리스)
- R8-only thất bại (failure / 실패)
- ABI/split issue
- bad remote cấu hình (config / 설정)
- staged rollout regression
```

Sau đó hỏi theo chuỗi:

```văn bản (text / 텍스트)
trạng thái (state / 상태) thuộc đơn vị sở hữu (owner / 오너) nào?
thời gian tồn tại (lifetime / 수명) bao lâu?
nguồn chuẩn (source of truth / 정본) ở đâu?
thao tác (operation / 연산) blocking hay suspend?
thứ tự (ordering / 순서) được định nghĩa chưa?
thử lại (retry / 재시도) có an toàn/idempotent không?
tiến trình (process / 프로세스) death reconstruct thế nào?
đầu vào (input / 입력) nào untrusted?
hiệu năng (performance / 성능) ngân sách (budget / 예산) nào cần đo?
kiểm thử (test / 테스트) nào chứng minh bất biến (invariant / 불변식)?
telemetry nào phát hiện regression?
quay lui (rollback / 롤백)/fallback có thật sự khả thi không?
```

Nếu những câu hỏi này có đáp án rõ, lựa chọn MVVM/MVI, Hilt/Koin, Room/SQLDelight hoặc Retrofit/Ktor thường trở thành quyết định kỹ thuật dễ lý giải hơn.
<!-- end merged variant -->

> **Bàn giao:** Sau **10.2 Tuyến (route / 경로) vs screen**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 kotlin beginner](./01_kotlin_beginner.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
