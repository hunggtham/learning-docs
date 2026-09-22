# 19 — Observability, Logging & Incident Response

## 1. Debugging và observability không giống nhau

Debugging (gỡ lỗi / 디버깅) là quá trình điều tra một vấn đề cụ thể. Observability (khả năng quan sát / 관측 가능성) là khả năng suy ra trạng thái bên trong của hệ thống từ evidence mà hệ thống tạo ra.

Một developer có thể debug tốt trên máy local nhưng production vẫn khó support nếu không có correlation ID, build identity, timing và structured error.

Mental model:

```text
incident
  ↓
evidence
  ↓
hypothesis
  ↓
experiment / comparison
  ↓
root cause
  ↓
fix + regression guard
```

Không bắt đầu bằng sửa code. Bắt đầu bằng evidence.

## 2. WebSquare application có nhiều lớp evidence

Một screen lỗi có thể liên quan:

```text
browser/WebView
WebSquare engine
page scope/scwin
component/GridView
DataCollection
Submission
network
WebSquare server module/config
application backend
DB/external service
build/cache/CDN
native shell nếu hybrid
```

Nếu chỉ nhìn console JavaScript, bạn mới thấy một phần hệ thống.

## 3. Correlation ID là xương sống của tracing

Một user action như Save nên có identity xuyên layer:

```text
click Save
→ client requestId
→ HTTP header/payload
→ gateway/backend log
→ DB/service call log
→ response
→ client completion log
```

Không cần full distributed tracing platform mới áp dụng được nguyên tắc này. Một request ID nhất quán đã giảm đáng kể thời gian điều tra.

## 4. Log event, không log câu chuyện mơ hồ

Log kiểu:

```text
save error
```

ít giá trị.

Log tốt hơn có structure:

```text
event=USER_SAVE_FAILED
requestId=REQ-123
screen=USER_DETAIL
submission=sbmSave
stage=BUSINESS_RESPONSE
code=OPTIMISTIC_LOCK_CONFLICT
elapsedMs=842
```

Message cho người đọc, field cho search/aggregation.

## 5. Không log toàn bộ DataList theo thói quen

DataList có thể chứa PII, account data hoặc hàng nghìn row. Dump toàn bộ object vừa chậm vừa nguy hiểm.

Log summary:

```text
rowCount
changedRowCount
selected business key đã mask
status distribution C/U/D
schema/version
```

Chỉ bật payload detail có kiểm soát trong môi trường phù hợp.

## 6. `$p.log()` và WebSquare log

WebSquare cung cấp logging/debug facility; tài liệu performance/debug mô tả log do `$p.log()` tạo với timestamp, elapsed time giữa log và elapsed time từ log đầu tiên.

Điều này hữu ích để đọc startup/render sequence:

```text
STEP1 engine load
STEP2 engine complete
STEP3 resources loaded
STEP4 object creation
...
```

Đừng chỉ đọc message; elapsed time giữa step giúp xác định bottleneck nằm ở engine/resource/object creation hay business request.

## 7. Client debug configuration

Trong các build tương ứng, `client.config.xml` có các setting như `debug`, `console`, `errorConsole`, `remoteConsole`, `debugKey`, `debugMenu`.

`remoteConsole` có thể cho phép `WebSquare.logger.sendRemoteLog` ghi log về WAS theo cấu hình tương ứng.

Nhưng debug setting là operational policy. Không bật mức verbose production vô hạn chỉ vì cần điều tra một bug.

## 8. Debug context menu là evidence tool

WebSquare hỗ trợ context debug menu trong các setup phù hợp, cho phép xem log và DataCollection hiện tại. Đây là cách tốt để kiểm tra model state mà không sửa source thêm `alert()`.

Khi dùng production-like environment, đảm bảo debug menu không làm lộ dữ liệu cho user không phù hợp.

## 9. Scope-aware debugging

Trong WFrame/Scope app, nhìn thấy DOM element chưa đủ để biết object thuộc page nào.

Debug utility như:

```javascript
$p.debug.getScope($0)
$p.debug.getFrame($0)
```

ở các build hỗ trợ giúp map DOM đang inspect về WebSquare scope/frame.

Workflow:

```text
Inspect broken element
→ identify frame/scope
→ inspect scwin/DataCollection/component trong đúng scope
→ trace Submission/event
```

Điều này tốt hơn thử `$p.top()` cho tới khi tìm thấy object.

## 10. Server-side WebSquare log

`server.config.xml`/engine configuration có log target, level, file, retention và các option như line/thread tùy build. Tài liệu chính thức lưu ý line number/thread logging có resource cost và không nên bật tùy tiện ở production.

Operational principle:

```text
log level càng chi tiết
→ evidence tăng
→ I/O + storage + CPU + noise tăng
```

Chọn level theo mục tiêu và thời gian điều tra.

## 11. Engine type ảnh hưởng khả năng debug

WebSquare engine có các `engineType` với mức remapping/debug/log khác nhau ở các dòng engine tương ứng. Một số type loại bỏ debug info hoặc logger để giảm size.

Vì vậy “production không có log giống dev” có thể là behavior của artifact/config, không phải logger code bị lỗi.

Incident report phải ghi engine build/type.

## 12. Build identity là telemetry

Một production error chỉ hữu ích khi biết code nào đang chạy.

Record tối thiểu:

```text
application release
Git commit/build ID
WebSquare engine build
W-Pack artifact version
client config version
server config version
native app version nếu hybrid
```

Nếu browser đang cache artifact cũ, Git main mới nhất không phải evidence về code user đang chạy.

## 13. Cache mismatch signature

Một failure sau deploy có pattern:

```text
HTML/shell mới
+ JS/W-Pack cũ
+ config mới
→ API/component mismatch
```

Hoặc ngược lại.

Khi lỗi chỉ xảy ra ở một số user sau deploy, kiểm tra cache/resource version trước khi suy business logic.

## 14. Network waterfall là distributed timeline

Network tab cho biết:

```text
request start
queue/stall
DNS/TLS khi có
request upload
TTFB
response download
status/header/body
```

Nếu click → request start đã mất 2 giây, vấn đề có thể nằm client JS/render. Nếu request start ngay nhưng TTFB 5 giây, focus backend/network.

Đừng gọi mọi thứ là “WebSquare chậm”.

## 15. Submission telemetry

Một wrapper Submission có thể emit lifecycle event:

```text
SUBMISSION_STARTED
SUBMISSION_SUCCEEDED
SUBMISSION_FAILED
SUBMISSION_CANCELLED
SUBMISSION_STALE_IGNORED
```

Fields nên gồm submission ID, request ID, screen ID, elapsed time, result class và payload size summary khi có thể.

Không cần log payload raw.

## 16. Transport success và business failure phải tách metric

Nếu HTTP 200 nhưng business response trả validation/lock conflict, transport dashboard sẽ nhìn “100% success” trong khi user thấy lỗi.

Tách metric:

```text
transport_error_rate
protocol_mapping_error_rate
business_rejection_rate
```

Ba metric trả lời ba loại vấn đề khác nhau.

## 17. Grid performance evidence

Grid lag cần đo:

```text
row count
column count
visible row count
formatter/expression count
render/update duration
browser memory
long task
```

Nếu Grid chỉ 100 row nhưng formatter gọi heavy function hàng chục nghìn lần do redraw, row count không phải root cause.

Performance chapter và Grid internals đã giải thích mechanism; observability chapter yêu cầu biến mechanism thành measurable evidence.

## 18. User timing mark

Với flow quan trọng có thể tạo timing mark ở application layer:

```text
SEARCH_CLICK
REQUEST_SENT
RESPONSE_RECEIVED
MODEL_UPDATED
GRID_READY
```

Sau đó tính:

```text
T_network = RESPONSE_RECEIVED - REQUEST_SENT
T_client  = GRID_READY - RESPONSE_RECEIVED
T_total   = GRID_READY - SEARCH_CLICK
```

Không cần framework APM phức tạp để có decomposition cơ bản.

## 19. Long task và UI freeze

Browser main thread freeze có thể đến từ:

```text
large JSON parse
DataList bulk mutation
Grid redraw
formatter loop
synchronous request
large DOM work
custom JavaScript loop
```

Nếu Network nhanh nhưng click không phản hồi, capture Performance profile thay vì tối ưu SQL.

## 20. Memory incident

SPA/hybrid app chạy lâu có thể leak dần.

Evidence nên so sánh:

```text
open screen 1 lần
close
open/close 20 lần
heap/object/listener count có quay về baseline không?
```

Nếu mỗi vòng tăng cố định, tìm retained reference: global cache, timer, document listener, stale WFrame scope, large DataList closure hoặc native callback registry.

## 21. Error taxonomy

Đừng dùng một error code `SYSTEM_ERROR` cho mọi thứ.

Một taxonomy hữu ích:

```text
CLIENT_SCRIPT
CLIENT_VALIDATION
SCOPE_LIFECYCLE
NETWORK
TIMEOUT
AUTHENTICATION
AUTHORIZATION
PROTOCOL_MAPPING
BUSINESS_REJECTION
CONCURRENCY_CONFLICT
SERVER_EXCEPTION
DEPENDENCY_FAILURE
FILE_STORAGE
NATIVE_BRIDGE
CONFIG_ARTIFACT_MISMATCH
```

Taxonomy giúp dashboard và runbook map symptom sang owner.

## 22. Incident severity không đồng nghĩa exception severity

Một console exception trên optional widget có thể low impact. Một silent stale-response bug hiển thị sai account data có thể high impact dù không throw exception.

Severity dựa trên user/business impact:

```text
scope
criticality
data integrity
security
recoverability
```

Không dựa chỉ vào stack trace dài.

## 23. First response: bảo toàn evidence

Khi production incident xảy ra, trước khi restart/clear cache mọi thứ hãy thu evidence đủ:

```text
exact time/timezone
user/session/request ID đã mask
screen/URL
steps
expected vs actual
browser/WebView/app version
release/build ID
network request/response metadata
client/server logs
screenshot/video nếu hữu ích
```

Restart có thể làm symptom biến mất nhưng cũng xóa state giúp tìm root cause.

## 24. Reproduce theo invariant, không theo click sequence duy nhất

Nếu bug xảy ra “sau khi mở tab A rồi B rồi quay lại A”, hãy hỏi invariant nào bị phá:

```text
scope identity?
stale reference?
global mutable state?
late Submission response?
DataList shared nhầm?
```

Sau đó tạo minimal reproduction tập trung invariant đó.

## 25. Differential diagnosis

So sánh môi trường/điều kiện giúp giảm search space:

```text
user A fail / user B pass
Chrome fail / Edge pass
fresh cache pass / warm cache fail
main page pass / WFrame fail
small data pass / large data fail
app 5.4 pass / app 5.2 fail
```

Mỗi contrast là evidence về layer có khả năng liên quan.

## 26. Binary search configuration

Khi nghi config/build, đừng đổi 10 option cùng lúc. Thay một dimension hoặc bisect version.

```text
engine build N pass
engine build N+4 fail
→ test N+2
→ thu hẹp release introducing behavior
```

Đây là version bisection, áp dụng được cho engine, common JS và app build.

## 27. Production hotfix phải có rollback path

Một hotfix không nên chỉ hỏi “fix được chưa?” mà còn:

```text
rollback artifact nào?
cache invalidation thế nào?
config có backward compatible không?
DB migration có reversible không?
native app có thể rollback không?
```

Web resource rollback nhanh hơn native store release, nên hybrid compatibility càng quan trọng.

## 28. Runbook theo symptom

Runbook tốt bắt đầu từ symptom user thấy.

Ví dụ “Grid trống sau Search”:

```text
1. event có chạy?
2. Submission có start?
3. request payload đúng?
4. response có rows?
5. target DataList rowCount?
6. Grid bind đúng DataList?
7. filter/view state?
8. scope đúng instance?
```

Runbook encode knowledge để on-call không cần nhớ mọi API.

## 29. Runbook: Save quay mãi

```text
button/loading state hiện gì?
request có gửi không?
request pending hay completed?
submitdone/submiterror có chạy?
business response parse được không?
callback throw exception trước cleanup không?
stale request guard có drop callback không?
loading reset ở finally-equivalent path không?
```

Nếu Network không có request, đừng điều tra DB.

## 30. Runbook: chỉ lỗi sau deploy

```text
build ID user đang chạy?
W-Pack artifact đúng release?
engine/config version?
cache headers/ETag?
service worker/PWA cache nếu có?
CDN node khác nhau?
API contract deploy order?
```

Deployment incident thường là artifact graph problem, không chỉ source code problem.

## 31. Runbook: hybrid callback không về

```text
JS requestId được tạo?
bridge dispatch thành công?
native log nhận request?
permission/capability state?
operation complete?
native callback emitted?
WebView/page còn alive?
requestId registry còn entry?
deep link/callback route đúng?
web build ↔ native version compatible?
```

Trace theo boundary thay vì restart app nhiều lần.

## 32. Security incident logging

Security log cần đủ để audit nhưng không tự tạo data leak.

Không log:

```text
password
access/refresh token
full resident/identity number
raw biometric/eKYC image
private document body
```

Có thể log masked identifier, hash/token fingerprint hoặc internal request ID tùy policy.

## 33. Metrics nên gắn với user journey

Framework metric hữu ích, nhưng business journey metric còn quan trọng hơn:

```text
search success latency
save completion rate
upload completion rate
export job completion time
eKYC completion/drop-off
```

Nếu engine khỏe nhưng 30% user không hoàn thành Save, hệ thống vẫn có vấn đề.

## 34. SLO và error budget ở mức thực dụng

Không cần bắt đầu bằng hệ thống SRE lớn. Có thể định nghĩa:

```text
99% Search hoàn thành < 2s
99.9% Save không có transport/system failure
99% screen load < 3s
```

Sau đó đo và xem regression theo release.

SLO buộc team định nghĩa “nhanh” và “ổn định” bằng số thay vì cảm giác.

## 35. Alert phải actionable

Alert “error count > 10” có thể noisy. Alert tốt gắn với impact và context:

```text
Save system failure rate > 2% trong 5 phút
AND traffic > minimum threshold
```

Alert nên dẫn tới dashboard/runbook có request IDs và release version.

## 36. Root cause vs trigger

Ví dụ incident xảy ra sau khi user double-click Save.

Trigger là double-click.

Root cause có thể là mutation endpoint không idempotent.

Nếu fix chỉ disable button, automation/retry khác vẫn tạo duplicate. Root cause fix phải bảo vệ invariant ở authoritative layer.

## 37. Five-whys phải dừng ở actionable system cause

Đừng kết thúc RCA bằng “developer quên check null”. Hỏi tại sao null có thể đi tới đây mà không contract/test/guard.

RCA tốt dẫn tới control:

```text
schema validation
contract test
lint/static check
central wrapper
monitoring
release guard
```

Không biến RCA thành blame document.

## 38. Regression guard sau incident

Mỗi serious incident nên để lại ít nhất một guard phù hợp:

```text
automated test
metric/alert
runtime validation
runbook
architecture constraint
migration checklist
```

Nếu hệ thống có thể tái phát y hệt mà không ai phát hiện sớm hơn, incident chưa thực sự được “học”.

## 39. Evidence bundle cho support

Một support bundle có thể gồm:

```text
release/build metadata
engine/config metadata
screen + scope/frame identity
request IDs
selected WebSquare logs
network HAR đã sanitize
console errors
backend log slice
performance trace nếu là latency
```

Bundle chuẩn hóa giúp chuyển issue giữa frontend/backend/platform mà không mất context.

## 40. Master incident mental model

Khi nhận bug production, đi theo thứ tự:

```text
1. Xác định impact và invariant bị phá.
2. Xác định exact instance/build/environment.
3. Dựng timeline từ user action đến outcome.
4. Tách client, transport, server, storage/native boundary.
5. Thu evidence ở boundary nghi ngờ.
6. So sánh case pass/fail.
7. Thu hẹp hypothesis.
8. Fix authoritative cause.
9. Thêm regression guard.
10. Cập nhật runbook/telemetry nếu evidence ban đầu thiếu.
```

Đây là production reasoning quan trọng hơn việc nhớ thêm một API.

## 41. Kết nối

Chapter này tổng hợp evidence từ [06 — Debugging, Performance & Security](06_debugging_performance_security.md), lifecycle từ [10 — Rendering & Lifetime](10_rendering_lazy_loading_lifetime.md), regression từ [11 — Testing](11_testing_testability_regression.md), artifact identity từ [12 — Build/Deployment](12_build_config_deployment.md), backend consistency từ [15](15_backend_contract_transaction_concurrency.md), file pipeline từ [17](17_file_excel_upload_download_pipeline.md) và hybrid boundary từ [18](18_hybrid_webview_native_bridge.md).

Các mental model này được hợp nhất thành quy trình senior/master ở [16 — Master Production Playbook](16_master_production_playbook.md).

## 42. Mastery checkpoint

Bạn đã master observability khi một bug “thỉnh thoảng xảy ra ở production” không còn khiến bạn bắt đầu bằng thêm `alert()` hoặc đoán API. Bạn biết yêu cầu build identity, dựng timeline, phân loại failure domain, dùng correlation ID, đo latency theo stage, bảo toàn evidence và biến mỗi incident nghiêm trọng thành test/metric/runbook để lần sau phát hiện sớm hơn.