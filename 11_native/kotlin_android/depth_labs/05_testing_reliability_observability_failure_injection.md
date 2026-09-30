# Độ sâu (depth / 깊이) Lab 05 — Testing, độ tin cậy (reliability / 신뢰성), khả năng quan sát (observability / 관측 가능성) và thất bại (failure / 실패) Injection

> **Mạch đọc:** Đặt **độ sâu (depth / 깊이) Lab 05 — Testing, độ tin cậy (reliability / 신뢰성), khả năng quan sát (observability / 관측 가능성) và thất bại (failure / 실패) Injection** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. kiểm thử (test / 테스트) phải chứng minh một đặc tả hợp đồng (contract / 계약), không chỉ chứng minh phương thức (method / 메서드) được gọi** sang **2. kiểm thử (test / 테스트) pyramid không phải tỷ lệ cứng**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một bộ kiểm thử (test suite / 테스트 스위트) lớn không đồng nghĩa hệ thống đáng tin cậy. Nhiều codebase có hàng nghìn kiểm thử (test / 테스트) nhưng vẫn gặp môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트) vì kiểm thử (test / 테스트) chỉ chứng minh happy đường dẫn (path / 경로) hoặc hiện thực (implementation / 구현) detail. độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) trên mobile cần đi xa hơn: xác định bất biến (invariant / 불변식), chọn đúng tầng kiểm thử (test / 테스트), inject thất bại (failure / 실패), đo hiệu năng (performance / 성능), quan sát hành vi (behavior / 동작) sau bản phát hành (release / 릴리스) và thiết kế quay lui (rollback / 롤백)/khôi phục (recovery / 복구).

Độ sâu (depth / 깊이) Lab này nối testing với môi trường vận hành (production / 운영 환경) độ tin cậy (reliability / 신뢰성) thay vì xem testing như bước cuối của development.

---

## 1. kiểm thử (test / 테스트) phải chứng minh một đặc tả hợp đồng (contract / 계약), không chỉ chứng minh phương thức (method / 메서드) được gọi

Kiểm thử (test / 테스트) yếu:

```kotlin
verify { repository.refresh() }
```

Kiểm thử (test / 테스트) này chỉ chứng minh tương tác (interaction / 상호작용).

Kiểm thử (test / 테스트) mạnh hơn:

```text
Given cache có dữ liệu cũ
When refresh remote thành công
Then local source of truth được replace transactionally
And observer nhận snapshot mới
And local-only bookmark flag không bị mất
```

Kiểm thử (test / 테스트) nên nhắm vào bất biến (invariant / 불변식)/user-visible hành vi (behavior / 동작).

---

## 2. kiểm thử (test / 테스트) pyramid không phải tỷ lệ cứng

Một app thường có nhiều cục bộ (local / 로컬) đơn vị (unit / 단위) kiểm thử (test / 테스트) hơn instrumented end-to-end kiểm thử (test / 테스트) vì cục bộ (local / 로컬) kiểm thử (test / 테스트) nhanh và deterministic hơn.

Nhưng không có tỷ lệ 70/20/10 thần kỳ.

Hãy phân theo rủi ro (risk / 위험):

```text
pure calculation -> unit test
repository + Room transaction -> integration test
serialization contract -> contract test
Compose semantics -> UI test
process death/deep link -> instrumented/system test
startup/jank -> macrobenchmark
real backend compatibility -> staging/contract environment
```

Tầng kiểm thử (test / 테스트) nên tương ứng ranh giới (boundary / 경계) cần chứng minh.

---

## 3. Fake thường tốt hơn mock cho stateful collaborator

Repository fake:

```kotlin
class FakeArticleRepository : ArticleRepository {
    private val items = MutableStateFlow<List<Article>>(emptyList())

    override fun observeArticles(): Flow<List<Article>> = items

    suspend fun emit(value: List<Article>) {
        items.value = value
    }
}
```

Fake giúp kiểm thử (test / 테스트) trạng thái (state / 상태) evolution tự nhiên.

Mock chuỗi (chain / 사슬) dài:

```text
when dao.observe -> flow
verify mapper
verify dao called once
verify api called once
```

có thể khóa kiểm thử (test / 테스트) vào hiện thực (implementation / 구현) thay vì đặc tả hợp đồng (contract / 계약).

Mock vẫn hữu ích để verify ranh giới (boundary / 경계) side tác động (effect / 효과) cụ thể, nhưng không nên là default cho mọi phụ thuộc (dependency / 의존성).

---

## 4. kiểm thử (test / 테스트) double phải có fidelity phù hợp

Một fake DB bằng mutable map không mô phỏng:

- SQL giao dịch (transaction / 트랜잭션),
- unique ràng buộc (constraint / 제약조건),
- cascade,
- truy vấn (query / 쿼리) thứ tự (ordering / 순서),
- di chuyển (migration / 마이그레이션).

Nếu rủi ro (risk / 위험) nằm ở SQL hành vi (behavior / 동작), dùng Room in-memory/instrumented kiểm thử (test / 테스트) thay vì fake collection.

Tương tự fake mạng (network / 네트워크) không chứng minh JSON adapter, headers hoặc HTTP status handling.

Chọn kiểm thử (test / 테스트) double theo dạng thất bại (failure mode / 실패 모드) muốn bắt.

---

## 5. đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) bảo vệ ranh giới (boundary / 경계) giữa app và backend

Nếu DTO thay đổi trường dữ liệu (field / 필드) optional -> required, compile vẫn pass vì app mã (code / 코드) không biết máy chủ (server / 서버) triển khai (deployment / 배포).

Đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) có thể validate:

```text
request shape
response fixture
unknown enum behavior
nullability
error payload
pagination cursor
idempotency header
```

Một đặc tả hợp đồng (contract / 계약) fixture nên lấy từ API lược đồ (schema / 스키마) hoặc captured representative payload được version-control.

---

## 6. Serialization kiểm thử (test / 테스트) là regression kiểm thử (test / 테스트) rẻ nhưng giá trị cao

Ví dụ:

```kotlin
@Test
fun unknownCategory_doesNotCrashWholeFeed() {
    val json = """
        {"id":"1","category":"FUTURE_CATEGORY"}
    """.trimIndent()

    val dto = adapter.fromJson(json)

    assertEquals(CategoryDto.Unknown, dto.category)
}
```

Backend evolution thường phá app ở serialization ranh giới (boundary / 경계) trước khi phá lô-gic nghiệp vụ (business logic / 비즈니스 로직).

---

## 7. di chuyển (migration / 마이그레이션) kiểm thử (test / 테스트) phải dùng lược đồ (schema / 스키마) thật của phiên bản (version / 버전) cũ

Kiểm thử (test / 테스트) chỉ create cơ sở dữ liệu (database / 데이터베이스) mới ở lược đồ (schema / 스키마) latest không chứng minh upgrade.

Di chuyển (migration / 마이그레이션) kiểm thử (test / 테스트) cần:

```text
create schema version N
insert representative legacy data
run migration N -> N+1 -> ... -> latest
assert data + index + constraint
```

Nếu app có nhiều phiên bản (version / 버전) ngoài thị trường, cần kiểm thử (test / 테스트) các supported upgrade paths thực tế.

---

## 8. di chuyển (migration / 마이그레이션) tính đúng đắn (correctness / 정확성) khác quay lui (rollback / 롤백) tính tương thích (compatibility / 호환성)

Upgrade di chuyển (migration / 마이그레이션) có thể pass nhưng quay lui (rollback / 롤백) bản phát hành (release / 릴리스) vẫn thất bại (fail / 실패).

Ví dụ phiên bản (version / 버전) 12 thêm column và rewrite enum format. Nếu quay lui (rollback / 롤백) về v11, app cũ không đọc được dữ liệu (data / 데이터) mới.

Release-critical di chuyển (migration / 마이그레이션) cần hỏi:

```text
forward compatible?
backward readable?
rollback cần destructive reset không?
server schema có support mixed client version không?
```

Testing bản phát hành (release / 릴리스) không dừng ở “latest app mở được DB”.

---

## 9. Property-based testing hữu ích cho bất biến (invariant / 불변식) lớn

Thay vì viết vài trường hợp (case / 사례) cụ thể, generate nhiều đầu vào (input / 입력)/sự kiện (event / 이벤트) thứ tự (order / 순서).

Ví dụ trạng thái (state / 상태) reducer:

```text
random sequence:
Load
Success
Refresh
Error
Retry
Logout
```

Bất biến (invariant / 불변식):

```text
không bao giờ vừa FatalError vừa giữ stale loading spinner
logout luôn clear account-scoped state
```

Property-based kiểm thử (test / 테스트) bắt combination mà nhà phát triển (developer / 개발자) không nghĩ tới.

---

## 10. máy trạng thái (state machine / 상태 머신) kiểm thử (test / 테스트) nên kiểm tra chuyển tiếp (transition / 전이) hợp lệ

Nếu sync mutation trạng thái (state / 상태):

```text
Pending -> InFlight -> Synced
Pending -> InFlight -> RetryAt -> InFlight
InFlight -> PermanentFailure
```

Kiểm thử (test / 테스트) phải chặn chuyển tiếp (transition / 전이) vô nghĩa:

```text
Synced -> RetryAt
PermanentFailure -> InFlight nếu không explicit retry
```

Kiểu (type / 타입)/máy trạng thái (state machine / 상태 머신) rõ giúp kiểm thử (test / 테스트) exhaustively hơn boolean flags.

---

## 11. Coroutine kiểm thử (test / 테스트) phải deterministic theo virtual thời gian (time / 시간)

Không dùng:

```kotlin
Thread.sleep(1_000)
```

để kiểm thử (test / 테스트) debounce/thử lại (retry / 재시도).

Dùng kiểm thử (test / 테스트) scheduler:

```kotlin
runTest {
    viewModel.onQuery("kot")
    advanceTimeBy(300)
    runCurrent()
    assertEquals("kot", repo.lastQuery)
}
```

Virtual thời gian (time / 시간) làm kiểm thử (test / 테스트) nhanh và ít flaky.

---

## 12. kiểm thử (test / 테스트) cancellation đường dẫn (path / 경로)

Một coroutine có thể success đúng nhưng cancel sai.

Ví dụ callbackFlow:

```text
collector subscribe -> listener register
collector cancel -> listener unregister
```

Kiểm thử (test / 테스트):

```kotlin
val job = launch { repository.locations().collect() }
assertTrue(provider.registered)

job.cancelAndJoin()
assertFalse(provider.registered)
```

Cleanup đường dẫn (path / 경로) là part của Đặc tả API (API contract / API 계약).

---

## 13. Race kiểm thử (test / 테스트) phải điều khiển thứ tự (ordering / 순서)

Bug khó thường chỉ xảy ra khi thực thi (execution / 실행) thứ tự (order / 순서) cụ thể.

Thiết kế fake có gate:

```kotlin
val requestAStarted = CompletableDeferred<Unit>()
val allowAComplete = CompletableDeferred<Unit>()
```

Kiểm thử (test / 테스트) chuỗi (sequence / 시퀀스):

```text
start A
wait A started
start B
complete B
then complete A
assert state vẫn là result B
```

Đây là cách kiểm thử (test / 테스트) stale phản hồi (response / 응답) protection deterministic thay vì hy vọng race tự xảy ra.

---

## 14. thất bại (failure / 실패) injection tốt hơn random chaos không kiểm soát

Inject thất bại (failure / 실패) tại ranh giới (boundary / 경계) cụ thể:

```text
DB transaction fail sau write thứ nhất
network timeout sau server commit
HTTP 429 có Retry-After
process death sau outbox insert
disk full
permission revoke
Bluetooth disconnect giữa operation
```

Mỗi thất bại (failure / 실패) nên map tới một expected khôi phục (recovery / 복구) hành vi (behavior / 동작).

---

## 15. tiến trình (process / 프로세스) death kiểm thử (test / 테스트) nên là acceptance kiểm thử (test / 테스트) cho trạng thái (state / 상태) reconstruction

Scenario:

```text
open detail id=42
scroll
background
kill process
restore
```

Assert:

```text
route identity vẫn đúng
content reload từ source of truth
transient in-memory cache không được assumption
saved UI state nhỏ được restore nếu design yêu cầu
```

Tiến trình (process / 프로세스) death kiểm thử (test / 테스트) phát hiện hidden singleton phụ thuộc (dependency / 의존성) rất tốt.

---

## 16. Permission revoke là thời gian chạy (runtime / 런타임) kiểm thử (test / 테스트) quan trọng

Permission có thể bị người dùng (user / 사용자) revoke sau khi tính năng (feature / 기능) từng hoạt động.

Kiểm thử (test / 테스트):

```text
grant camera
open scanner
leave screen
revoke permission
return
```

App phải degrade/re-request hợp lý, không crash vì assume permission permanent.

---

## 17. mạng (network / 네트워크) flapping kiểm thử (test / 테스트)

Scenario:

```text
online -> request start
network lost
retry scheduled
network briefly online
network lost again
```

Assert:

```text
không spawn retry storm
queue vẫn durable
backoff đúng
UI không flip error/loading quá mức
```

Mobile mạng (network / 네트워크) thực tế không nhị phân (binary / 이진) ổn định như emulator lab.

---

## 18. Snapshot/screenshot kiểm thử (test / 테스트) không thay ngữ nghĩa (semantics / 의미론) kiểm thử (test / 테스트)

Screenshot bắt visual regression.

Ngữ nghĩa (semantics / 의미론) kiểm thử (test / 테스트) bắt khả năng tiếp cận (accessibility / 접근성)/meaning.

Một button có thể giống hệt điểm ảnh (pixel / 픽셀) nhưng content description bị mất. Screenshot pass, khả năng tiếp cận (accessibility / 접근성) thất bại (fail / 실패).

Dùng hai loại kiểm thử (test / 테스트) cho hai đặc tả hợp đồng (contract / 계약) khác nhau.

---

## 19. Compose UI kiểm thử (test / 테스트) nên assert hành vi (behavior / 동작) qua ngữ nghĩa (semantics / 의미론)

Ví dụ:

```kotlin
composeRule
    .onNodeWithText("Bookmark")
    .performClick()

composeRule
    .onNodeWithContentDescription("Bookmarked")
    .assertExists()
```

Kiểm thử (test / 테스트) ngữ nghĩa (semantic / 의미적) intent bền hơn kiểm thử (test / 테스트) nội bộ (internal / 내부) composable cây (tree / 트리) nếu hiện thực (implementation / 구현) đổi.

---

## 20. khả năng tiếp cận (accessibility / 접근성) kiểm thử (test / 테스트) cần manual + automated

Automated kiểm thử (test / 테스트) không mô phỏng hoàn toàn trải nghiệm TalkBack.

Checklist manual:

```text
focus order
meaningful labels
state announcement
touch target
font scaling
RTL
keyboard navigation
contrast
```

Khả năng tiếp cận (accessibility / 접근성) là tương tác (interaction / 상호작용) tính đúng đắn (correctness / 정확성), không chỉ lint warning.

---

## 21. hiệu năng (performance / 성능) kiểm thử (test / 테스트) phải có chỉ số (metric / 지표) trước khi có threshold

Không viết:

```text
startup phải nhanh
```

Hãy chọn:

```text
TTID p50/p90
TTFD p50/p90
frame time/jank
scroll benchmark
memory peak
APK/AAB size
```

Threshold phải gắn với baseline/sản phẩm (product / 제품) SLO.

---

## 22. Macrobenchmark đo người dùng (user / 사용자) journey, không chỉ hàm (function / 함수)

Microbenchmark đo mã (code / 코드) nhỏ.

Macrobenchmark đo app-level journey như:

```text
cold startup
scroll feed
open detail
navigate tab
```

Điều này phù hợp khi bottleneck qua nhiều tầng (layer / 계층): tiến trình (process / 프로세스) startup, nạp lớp (class loading / 클래스 로딩), Compose, cơ sở dữ liệu (database / 데이터베이스), ảnh (image / 이미지), rendering.

---

## 23. Baseline Profile phải được đo tác động (effect / 효과)

Đừng assume “có profile là nhanh”.

Benchmark:

```text
without profile
with profile
```

so sánh startup/frame chỉ số (metric / 지표).

Profile generator cũng cần cover trọng yếu (critical / 중요) người dùng (user / 사용자) journey thật, không chỉ launch empty screen.

---

## 24. hiệu năng (performance / 성능) kiểm thử (test / 테스트) nên chạy release-like bản dựng (build / 빌드)

Gỡ lỗi (debug / 디버그) bản dựng (build / 빌드) có hành vi (behavior / 동작) khác về trình biên dịch (compiler / 컴파일러) tối ưu hóa (optimization / 최적화), R8, tracing overhead và profile.

Benchmark trên gỡ lỗi (debug / 디버그) rồi kết luận môi trường vận hành (production / 운영 환경) hiệu năng (performance / 성능) có thể sai.

---

## 25. Flaky kiểm thử (test / 테스트) là độ tin cậy (reliability / 신뢰성) debt

Một kiểm thử (test / 테스트) flaky 2% nghe nhỏ, nhưng nếu CI có 500 flaky-sensitive kiểm thử (test / 테스트), xác suất bản dựng (build / 빌드) có ít nhất một false thất bại (failure / 실패) rất cao.

Flaky kiểm thử (test / 테스트) gây:

```text
rerun culture
ignore red CI
release delay
mất trust vào test suite
```

Nhánh học (track / 트랙) flake tỷ lệ (rate / 비율) như môi trường vận hành (production / 운영 환경) chỉ số (metric / 지표).

---

## 26. Không sửa flaky bằng thử lại (retry / 재시도) vô hạn

Thử lại (retry / 재시도) có thể giảm noise nhưng che nguyên nhân gốc (root cause / 근본 원인).

Quy trình:

```text
quarantine có visibility
collect evidence
classify timing/shared-state/external dependency
fix determinism
remove quarantine
```

Thử lại (retry / 재시도) chỉ là mitigation tạm thời.

---

## 27. kiểm thử (test / 테스트) isolation cần điều khiển (control / 제어) toàn cục (global / 전역) trạng thái (state / 상태)

Các nguồn leak giữa kiểm thử (test / 테스트):

```text
singleton
shared DB
static cache
Dispatchers.Main không reset
WorkManager state
clock/timezone
locale
```

Một kiểm thử (test / 테스트) pass riêng nhưng thất bại (fail / 실패) khi chạy suite thường là isolation issue.

---

## 28. Clock nên inject khi lô-gic (logic / 논리) phụ thuộc thời gian (time / 시간)

Bad:

```kotlin
Instant.now()
```

khắp lô-gic nghiệp vụ (business logic / 비즈니스 로직).

Better:

```kotlin
class ExpiryPolicy(
    private val clock: Clock
)
```

Kiểm thử (test / 테스트) dùng fixed clock.

Điều này giúp expiry/thử lại (retry / 재시도)/session kiểm thử (test / 테스트) deterministic.

---

## 29. Random nên seed hoặc inject

Nếu thuật toán (algorithm / 알고리즘)/backoff jitter dùng random, kiểm thử (test / 테스트) cần deterministic seed/provider.

Môi trường vận hành (production / 운영 환경) vẫn random; kiểm thử (test / 테스트) kiểm soát đầu vào (input / 입력).

---

## 30. khả năng quan sát (observability / 관측 가능성) bắt đầu từ câu hỏi sự cố (incident / 인시던트)

Đừng log mọi thứ.

Hãy hỏi khi sự cố (incident / 인시던트) xảy ra cần biết gì:

```text
user journey nào fail?
app version/build nào?
device/API/OEM nào?
request/mutation nào?
latency ở layer nào?
retry bao nhiêu lần?
process cold/warm?
feature flag nào bật?
```

Từ đó thiết kế sự kiện (event / 이벤트)/log lược đồ (schema / 스키마).

---

## 31. Correlation ID nối mobile sự kiện (event / 이벤트) xuyên tầng (layer / 계층)

Một luồng (flow / 흐름) có thể có:

```text
UI action
-> repository mutation
-> network request
-> server operation
-> sync acknowledgement
```

Dùng thao tác (operation / 연산)/mutation/correlation id giúp dấu vết (trace / 추적) end-to-end.

Không dùng PII làm correlation key.

---

## 32. Structured log tốt hơn free-text log

Thay vì:

```text
"sync failed badly"
```

log trường dữ liệu (field / 필드):

```text
event=sync_attempt
outcome=retryable_failure
mutationType=bookmark
attempt=3
httpStatus=503
queueAgeMs=42000
```

Structured dữ liệu (data / 데이터) truy vấn (query / 쿼리)/aggregate được.

---

## 33. Crash log không đủ cho ANR/jank

Crash = tiến trình (process / 프로세스) terminated bởi unhandled lỗi (error / 오류).

ANR = UI/main luồng thực thi (thread / 스레드) không responsive.

Jank = frame deadline miss.

Ba dạng thất bại (failure mode / 실패 모드) cần telemetry/công cụ (tool / 도구) khác nhau.

App “crash-free 99.9%” vẫn có thể UX rất tệ vì ANR/jank.

---

## 34. độ tin cậy (reliability / 신뢰성) SLI/SLO cho mobile

Ví dụ SLI:

```text
crash-free sessions
ANR rate
successful login rate
sync success within 5 min
cold-start TTID p90
checkout success
```

SLO biến “app ổn” thành mục tiêu (target / 대상) measurable.

---

## 35. sản phẩm (product / 제품) success chỉ số (metric / 지표) và technical chỉ số (metric / 지표) phải nối nhau

Ví dụ checkout drop tăng.

Technical dữ liệu (data / 데이터) cần giúp phân biệt:

```text
network latency
payment API errors
UI validation errors
ANR
session expiry
```

Nếu telemetry chỉ có CPU/bộ nhớ (memory / 메모리) mà không có journey kết quả (outcome / 결과), sự cố (incident / 인시던트) phân tích (analysis / 분석) thiếu ngữ cảnh (context / 맥락).

---

## 36. cờ tính năng (feature flag / 기능 플래그) là độ tin cậy (reliability / 신뢰성) công cụ (tool / 도구), không chỉ A/B testing

Flag có thể dùng để:

```text
disable risky feature
switch backend route
turn off expensive animation
fall back old implementation
```

Nhưng flag cần vòng đời (lifecycle / 생명주기):

```text
owner
expiry date
default
kill-switch behavior
offline behavior
```

Flag tồn tại mãi tạo branching debt.

---

## 37. Rollout theo cohort giảm blast radius

Bản phát hành (release / 릴리스) 100% ngay khiến bug ảnh hưởng toàn người dùng (user / 사용자) cơ sở (base / 기반).

Staged rollout:

```text
1% -> 5% -> 20% -> 50% -> 100%
```

Mỗi step quan sát trọng yếu (critical / 중요) chỉ số (metric / 지표).

Nếu chỉ số (metric / 지표) regress, stop/quay lui (rollback / 롤백) trước khi blast radius lớn.

---

## 38. quay lui (rollback / 롤백) chỉ an toàn nếu dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약) tương thích

Quay lui (rollback / 롤백) app nhị phân (binary / 이진) không quay lui (rollback / 롤백) automatically:

```text
DB schema
DataStore format
server data mutation
remote config state
uploaded file format
```

Bản phát hành (release / 릴리스) thiết kế (design / 설계) phải xem quay lui (rollback / 롤백) như tính tương thích (compatibility / 호환성) bài toán (problem / 문제).

---

## 39. Canary/nội bộ (internal / 내부) nhánh học (track / 트랙) nên có representative người dùng (user / 사용자) journey

Nội bộ (internal / 내부) testing chỉ mở app rồi đóng không có giá trị lớn.

Checklist smoke:

```text
login
cold start
main feed
critical write
background/restore
deep link
notification tap
upgrade from previous production
```

---

## 40. sự cố (incident / 인시던트) phản hồi (response / 응답) cần runbook mobile-specific

Khi crash spike:

```text
identify version/cohort/device/API
compare previous release
check feature flags
check server deploy correlation
pause rollout
activate kill switch
prepare hotfix/rollback
```

Runbook giảm quyết định (decision / 결정) độ trễ (latency / 지연 시간) khi sự cố (incident / 인시던트) thật xảy ra.

---

## 41. Postmortem phải tìm hệ thống (system / 시스템) cause

Không dừng ở:

```text
developer quên null check
```

Hỏi:

```text
contract test thiếu?
serializer không handle unknown field?
rollout quá nhanh?
observability không phát hiện sớm?
review checklist thiếu boundary này?
```

Mục tiêu là giảm recurrence, không tìm người chịu lỗi.

---

## 42. kiểm thử (test / 테스트) ma trận (matrix / 행렬) nên risk-based

Không thể kiểm thử (test / 테스트) mọi thiết bị (device / 장치) x mọi API x mọi locale x mọi mạng (network / 네트워크).

Chọn ma trận (matrix / 행렬) theo:

```text
user distribution
revenue impact
hardware feature
OEM risk
API behavior changes
form factor
```

Kiểm thử (test / 테스트) độ sâu (depth / 깊이) nên tỷ lệ với blast radius.

---

## 43. “Works on emulator” không đủ cho hardware tính năng (feature / 기능)

BLE, camera, audio focus, background thực thi (execution / 실행), thermal, biometric và OEM permission hành vi (behavior / 동작) cần physical-device coverage phù hợp.

Emulator vẫn rất tốt cho deterministic API-level ma trận (matrix / 행렬) và UI automation.

---

## 44. Chaos kiểm thử (test / 테스트) có giá trị khi bất biến (invariant / 불변식) rõ

Random kill/mạng (network / 네트워크) thất bại (failure / 실패) chỉ hữu ích nếu biết assert gì.

Ví dụ chaos sync:

```text
randomly kill worker
randomly drop response
randomly reorder remote events
```

Bất biến (invariant / 불변식):

```text
no lost durable mutation
no cross-account commit
no duplicate business effect
```

Chaos không thay specification.

---

## 45. Reliability review checklist
Phần này nối mạch Android vừa học với “45. Reliability review checklist”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.


| Câu hỏi | bằng chứng (evidence / 증거) |
|---|---|
| bất biến (invariant / 불변식) được kiểm thử (test / 테스트) ở tầng nào? | đơn vị (unit / 단위)/tích hợp (integration / 통합)/hệ thống (system / 시스템) |
| Race có deterministic kiểm thử (test / 테스트) không? | gates/kiểm thử (test / 테스트) scheduler |
| tiến trình (process / 프로세스) death được cover không? | reconstruction kiểm thử (test / 테스트) |
| di chuyển (migration / 마이그레이션) dùng real old lược đồ (schema / 스키마) chưa? | di chuyển (migration / 마이그레이션) fixture |
| Permission revoke được kiểm thử (test / 테스트) chưa? | thời gian chạy (runtime / 런타임)/hệ thống (system / 시스템) kiểm thử (test / 테스트) |
| hiệu năng (performance / 성능) có baseline không? | macrobenchmark |
| Telemetry trả lời sự cố (incident / 인시던트) question không? | structured events |
| Rollout có guardrail không? | staged rollout/SLO |
| quay lui (rollback / 롤백) compatible không? | old-version read kiểm thử (test / 테스트) |
| Flaky kiểm thử (test / 테스트) được quản lý không? | flake dashboard/quarantine |

---

## 46. Kết luận

Testing ở mức (level / 수준) cấp cao (senior / 시니어)/Master không phải là tăng số lượng kiểm thử (test / 테스트). Đó là quá trình biến bất biến (invariant / 불변식) và thất bại (failure / 실패) mô hình (model / 모델) thành bằng chứng (evidence / 증거) có thể chạy lại.

Mô hình tư duy (mental model / 사고 모델):

```text
invariant
-> risk
-> test layer
-> deterministic failure injection
-> production metric
-> rollout guardrail
-> incident feedback
```

Test suite chứng minh những gì ta biết trước. Observability giúp phát hiện những gì ta chưa biết. Reliability cần cả hai.
