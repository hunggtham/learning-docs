# Depth Lab 05 — Testing, Reliability, Observability và Failure Injection

Một test suite lớn không đồng nghĩa hệ thống đáng tin cậy. Nhiều codebase có hàng nghìn test nhưng vẫn gặp production incident vì test chỉ chứng minh happy path hoặc implementation detail. Reliability engineering trên mobile cần đi xa hơn: xác định invariant, chọn đúng tầng test, inject failure, đo performance, quan sát behavior sau release và thiết kế rollback/recovery.

Depth Lab này nối testing với production reliability thay vì xem testing như bước cuối của development.

---

## 1. Test phải chứng minh một contract, không chỉ chứng minh method được gọi

Test yếu:

```kotlin
verify { repository.refresh() }
```

Test này chỉ chứng minh interaction.

Test mạnh hơn:

```text
Given cache có dữ liệu cũ
When refresh remote thành công
Then local source of truth được replace transactionally
And observer nhận snapshot mới
And local-only bookmark flag không bị mất
```

Test nên nhắm vào invariant/user-visible behavior.

---

## 2. Test pyramid không phải tỷ lệ cứng

Một app thường có nhiều local unit test hơn instrumented end-to-end test vì local test nhanh và deterministic hơn.

Nhưng không có tỷ lệ 70/20/10 thần kỳ.

Hãy phân theo risk:

```text
pure calculation -> unit test
repository + Room transaction -> integration test
serialization contract -> contract test
Compose semantics -> UI test
process death/deep link -> instrumented/system test
startup/jank -> macrobenchmark
real backend compatibility -> staging/contract environment
```

Tầng test nên tương ứng boundary cần chứng minh.

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

Fake giúp test state evolution tự nhiên.

Mock chain dài:

```text
when dao.observe -> flow
verify mapper
verify dao called once
verify api called once
```

có thể khóa test vào implementation thay vì contract.

Mock vẫn hữu ích để verify boundary side effect cụ thể, nhưng không nên là default cho mọi dependency.

---

## 4. Test double phải có fidelity phù hợp

Một fake DB bằng mutable map không mô phỏng:

- SQL transaction,
- unique constraint,
- cascade,
- query ordering,
- migration.

Nếu risk nằm ở SQL behavior, dùng Room in-memory/instrumented test thay vì fake collection.

Tương tự fake network không chứng minh JSON adapter, headers hoặc HTTP status handling.

Chọn test double theo failure mode muốn bắt.

---

## 5. Contract test bảo vệ boundary giữa app và backend

Nếu DTO thay đổi field optional -> required, compile vẫn pass vì app code không biết server deployment.

Contract test có thể validate:

```text
request shape
response fixture
unknown enum behavior
nullability
error payload
pagination cursor
idempotency header
```

Một contract fixture nên lấy từ API schema hoặc captured representative payload được version-control.

---

## 6. Serialization test là regression test rẻ nhưng giá trị cao

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

Backend evolution thường phá app ở serialization boundary trước khi phá business logic.

---

## 7. Migration test phải dùng schema thật của version cũ

Test chỉ create database mới ở schema latest không chứng minh upgrade.

Migration test cần:

```text
create schema version N
insert representative legacy data
run migration N -> N+1 -> ... -> latest
assert data + index + constraint
```

Nếu app có nhiều version ngoài thị trường, cần test các supported upgrade paths thực tế.

---

## 8. Migration correctness khác rollback compatibility

Upgrade migration có thể pass nhưng rollback release vẫn fail.

Ví dụ version 12 thêm column và rewrite enum format. Nếu rollback về v11, app cũ không đọc được data mới.

Release-critical migration cần hỏi:

```text
forward compatible?
backward readable?
rollback cần destructive reset không?
server schema có support mixed client version không?
```

Testing release không dừng ở “latest app mở được DB”.

---

## 9. Property-based testing hữu ích cho invariant lớn

Thay vì viết vài case cụ thể, generate nhiều input/event order.

Ví dụ state reducer:

```text
random sequence:
Load
Success
Refresh
Error
Retry
Logout
```

Invariant:

```text
không bao giờ vừa FatalError vừa giữ stale loading spinner
logout luôn clear account-scoped state
```

Property-based test bắt combination mà developer không nghĩ tới.

---

## 10. State machine test nên kiểm tra transition hợp lệ

Nếu sync mutation state:

```text
Pending -> InFlight -> Synced
Pending -> InFlight -> RetryAt -> InFlight
InFlight -> PermanentFailure
```

Test phải chặn transition vô nghĩa:

```text
Synced -> RetryAt
PermanentFailure -> InFlight nếu không explicit retry
```

Type/state machine rõ giúp test exhaustively hơn boolean flags.

---

## 11. Coroutine test phải deterministic theo virtual time

Không dùng:

```kotlin
Thread.sleep(1_000)
```

để test debounce/retry.

Dùng test scheduler:

```kotlin
runTest {
    viewModel.onQuery("kot")
    advanceTimeBy(300)
    runCurrent()
    assertEquals("kot", repo.lastQuery)
}
```

Virtual time làm test nhanh và ít flaky.

---

## 12. Test cancellation path

Một coroutine có thể success đúng nhưng cancel sai.

Ví dụ callbackFlow:

```text
collector subscribe -> listener register
collector cancel -> listener unregister
```

Test:

```kotlin
val job = launch { repository.locations().collect() }
assertTrue(provider.registered)

job.cancelAndJoin()
assertFalse(provider.registered)
```

Cleanup path là part của API contract.

---

## 13. Race test phải điều khiển ordering

Bug khó thường chỉ xảy ra khi execution order cụ thể.

Thiết kế fake có gate:

```kotlin
val requestAStarted = CompletableDeferred<Unit>()
val allowAComplete = CompletableDeferred<Unit>()
```

Test sequence:

```text
start A
wait A started
start B
complete B
then complete A
assert state vẫn là result B
```

Đây là cách test stale response protection deterministic thay vì hy vọng race tự xảy ra.

---

## 14. Failure injection tốt hơn random chaos không kiểm soát

Inject failure tại boundary cụ thể:

```text
DB transaction fail sau write thứ nhất
network timeout sau server commit
HTTP 429 có Retry-After
process death sau outbox insert
disk full
permission revoke
Bluetooth disconnect giữa operation
```

Mỗi failure nên map tới một expected recovery behavior.

---

## 15. Process death test nên là acceptance test cho state reconstruction

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

Process death test phát hiện hidden singleton dependency rất tốt.

---

## 16. Permission revoke là runtime test quan trọng

Permission có thể bị user revoke sau khi feature từng hoạt động.

Test:

```text
grant camera
open scanner
leave screen
revoke permission
return
```

App phải degrade/re-request hợp lý, không crash vì assume permission permanent.

---

## 17. Network flapping test

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

Mobile network thực tế không binary ổn định như emulator lab.

---

## 18. Snapshot/screenshot test không thay semantics test

Screenshot bắt visual regression.

Semantics test bắt accessibility/meaning.

Một button có thể giống hệt pixel nhưng content description bị mất. Screenshot pass, accessibility fail.

Dùng hai loại test cho hai contract khác nhau.

---

## 19. Compose UI test nên assert behavior qua semantics

Ví dụ:

```kotlin
composeRule
    .onNodeWithText("Bookmark")
    .performClick()

composeRule
    .onNodeWithContentDescription("Bookmarked")
    .assertExists()
```

Test semantic intent bền hơn test internal composable tree nếu implementation đổi.

---

## 20. Accessibility test cần manual + automated

Automated test không mô phỏng hoàn toàn trải nghiệm TalkBack.

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

Accessibility là interaction correctness, không chỉ lint warning.

---

## 21. Performance test phải có metric trước khi có threshold

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

Threshold phải gắn với baseline/product SLO.

---

## 22. Macrobenchmark đo user journey, không chỉ function

Microbenchmark đo code nhỏ.

Macrobenchmark đo app-level journey như:

```text
cold startup
scroll feed
open detail
navigate tab
```

Điều này phù hợp khi bottleneck qua nhiều layer: process startup, class loading, Compose, database, image, rendering.

---

## 23. Baseline Profile phải được đo effect

Đừng assume “có profile là nhanh”.

Benchmark:

```text
without profile
with profile
```

so sánh startup/frame metric.

Profile generator cũng cần cover critical user journey thật, không chỉ launch empty screen.

---

## 24. Performance test nên chạy release-like build

Debug build có behavior khác về compiler optimization, R8, tracing overhead và profile.

Benchmark trên debug rồi kết luận production performance có thể sai.

---

## 25. Flaky test là reliability debt

Một test flaky 2% nghe nhỏ, nhưng nếu CI có 500 flaky-sensitive test, xác suất build có ít nhất một false failure rất cao.

Flaky test gây:

```text
rerun culture
ignore red CI
release delay
mất trust vào test suite
```

Track flake rate như production metric.

---

## 26. Không sửa flaky bằng retry vô hạn

Retry có thể giảm noise nhưng che root cause.

Quy trình:

```text
quarantine có visibility
collect evidence
classify timing/shared-state/external dependency
fix determinism
remove quarantine
```

Retry chỉ là mitigation tạm thời.

---

## 27. Test isolation cần control global state

Các nguồn leak giữa test:

```text
singleton
shared DB
static cache
Dispatchers.Main không reset
WorkManager state
clock/timezone
locale
```

Một test pass riêng nhưng fail khi chạy suite thường là isolation issue.

---

## 28. Clock nên inject khi logic phụ thuộc time

Bad:

```kotlin
Instant.now()
```

khắp business logic.

Better:

```kotlin
class ExpiryPolicy(
    private val clock: Clock
)
```

Test dùng fixed clock.

Điều này giúp expiry/retry/session test deterministic.

---

## 29. Random nên seed hoặc inject

Nếu algorithm/backoff jitter dùng random, test cần deterministic seed/provider.

Production vẫn random; test kiểm soát input.

---

## 30. Observability bắt đầu từ câu hỏi incident

Đừng log mọi thứ.

Hãy hỏi khi incident xảy ra cần biết gì:

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

Từ đó thiết kế event/log schema.

---

## 31. Correlation ID nối mobile event xuyên layer

Một flow có thể có:

```text
UI action
-> repository mutation
-> network request
-> server operation
-> sync acknowledgement
```

Dùng operation/mutation/correlation id giúp trace end-to-end.

Không dùng PII làm correlation key.

---

## 32. Structured log tốt hơn free-text log

Thay vì:

```text
"sync failed badly"
```

log field:

```text
event=sync_attempt
outcome=retryable_failure
mutationType=bookmark
attempt=3
httpStatus=503
queueAgeMs=42000
```

Structured data query/aggregate được.

---

## 33. Crash log không đủ cho ANR/jank

Crash = process terminated bởi unhandled error.

ANR = UI/main thread không responsive.

Jank = frame deadline miss.

Ba failure mode cần telemetry/tool khác nhau.

App “crash-free 99.9%” vẫn có thể UX rất tệ vì ANR/jank.

---

## 34. Reliability SLI/SLO cho mobile

Ví dụ SLI:

```text
crash-free sessions
ANR rate
successful login rate
sync success within 5 min
cold-start TTID p90
checkout success
```

SLO biến “app ổn” thành target measurable.

---

## 35. Product success metric và technical metric phải nối nhau

Ví dụ checkout drop tăng.

Technical data cần giúp phân biệt:

```text
network latency
payment API errors
UI validation errors
ANR
session expiry
```

Nếu telemetry chỉ có CPU/memory mà không có journey outcome, incident analysis thiếu context.

---

## 36. Feature flag là reliability tool, không chỉ A/B testing

Flag có thể dùng để:

```text
disable risky feature
switch backend route
turn off expensive animation
fall back old implementation
```

Nhưng flag cần lifecycle:

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

Release 100% ngay khiến bug ảnh hưởng toàn user base.

Staged rollout:

```text
1% -> 5% -> 20% -> 50% -> 100%
```

Mỗi step quan sát critical metric.

Nếu metric regress, stop/rollback trước khi blast radius lớn.

---

## 38. Rollback chỉ an toàn nếu data contract tương thích

Rollback app binary không rollback automatically:

```text
DB schema
DataStore format
server data mutation
remote config state
uploaded file format
```

Release design phải xem rollback như compatibility problem.

---

## 39. Canary/internal track nên có representative user journey

Internal testing chỉ mở app rồi đóng không có giá trị lớn.

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

## 40. Incident response cần runbook mobile-specific

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

Runbook giảm decision latency khi incident thật xảy ra.

---

## 41. Postmortem phải tìm system cause

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

## 42. Test matrix nên risk-based

Không thể test mọi device x mọi API x mọi locale x mọi network.

Chọn matrix theo:

```text
user distribution
revenue impact
hardware feature
OEM risk
API behavior changes
form factor
```

Test depth nên tỷ lệ với blast radius.

---

## 43. “Works on emulator” không đủ cho hardware feature

BLE, camera, audio focus, background execution, thermal, biometric và OEM permission behavior cần physical-device coverage phù hợp.

Emulator vẫn rất tốt cho deterministic API-level matrix và UI automation.

---

## 44. Chaos test có giá trị khi invariant rõ

Random kill/network failure chỉ hữu ích nếu biết assert gì.

Ví dụ chaos sync:

```text
randomly kill worker
randomly drop response
randomly reorder remote events
```

Invariant:

```text
no lost durable mutation
no cross-account commit
no duplicate business effect
```

Chaos không thay specification.

---

## 45. Reliability review checklist

| Câu hỏi | Evidence |
|---|---|
| Invariant được test ở tầng nào? | unit/integration/system |
| Race có deterministic test không? | gates/test scheduler |
| Process death được cover không? | reconstruction test |
| Migration dùng real old schema chưa? | migration fixture |
| Permission revoke được test chưa? | runtime/system test |
| Performance có baseline không? | macrobenchmark |
| Telemetry trả lời incident question không? | structured events |
| Rollout có guardrail không? | staged rollout/SLO |
| Rollback compatible không? | old-version read test |
| Flaky test được quản lý không? | flake dashboard/quarantine |

---

## 46. Kết luận

Testing ở level Senior/Master không phải là tăng số lượng test. Đó là quá trình biến invariant và failure model thành evidence có thể chạy lại.

Mental model:

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