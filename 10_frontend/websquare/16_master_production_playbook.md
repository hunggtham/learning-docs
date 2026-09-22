# 16 — Master Production Playbook & End-to-End Case Studies

Đạt mức Master với WebSquare không có nghĩa nhớ nhiều property hơn. Nó nghĩa là khi gặp một screen lạ hoặc incident production, bạn có thể dựng lại **state model, lifecycle, identity, contract và evidence chain** mà không bị abstraction của framework làm mất phương hướng.

Chapter này không thêm một nhóm API mới. Nó hợp nhất toàn library thành phương pháp reasoning có thể dùng khi design, code review, debug, performance tuning, migration và incident response.

## 1. Mental model Master: năm graph chạy đồng thời

Một WebSquare application lớn có thể được hiểu bằng năm graph.

**Page graph** mô tả shell, WFrame, tab, popup, parent/child Scope.

**Data graph** mô tả DataMap, DataList, binding, derived view và owner của business state.

**Event graph** mô tả user event, component event, DataList event, callback và async continuation.

**Request graph** mô tả Submission, dependency, server command, transaction và response.

**Lifetime graph** mô tả object nào tạo object nào, reference nào giữ object sống, khi nào cleanup.

Một bug khó thường là giao điểm của ít nhất hai graph.

```text
Popup đóng nhưng request cũ ghi đè Grid
= page/lifetime graph + request graph

Sort xong error map sai row
= data identity graph + event/request graph

Tab mở lại thấy state tab khác
= page instance graph + global data graph
```

Master debugging là tìm graph nào bị trộn boundary.

## 2. Sáu identity phải luôn được đặt tên

Trong project lớn, từ “ID” quá mơ hồ. Hãy phân biệt:

```text
component logical ID
runtime frame/scope ID
screen definition ID
screen instance/navigation key
business entity key
request/transaction correlation ID
```

Nếu log chỉ ghi `id=123`, incident investigation sẽ rất chậm. Nếu code truyền một `index`/`id` qua nhiều layer mà không biết loại identity, design dễ sai.

## 3. Bốn readiness state thay cho từ “loaded”

Không nói “page load xong” nếu chưa chỉ rõ:

```text
source-ready
object/scope-ready
render-ready
business-data-ready
```

Một WFrame có thể object-ready nhưng initial Submission chưa xong. Một tab preload có `scwin` nhưng UI chưa render. Một Grid render xong nhưng code list chưa load nên display label chưa đúng.

Mỗi cross-page contract phải yêu cầu readiness đúng mức.

## 4. Ba trust boundary

WebSquare developer cần nhìn rõ:

```text
browser/client state = untrusted
server application = policy/business enforcement
persistent data/external systems = transaction/integration boundary
```

DataList, hidden field, disabled button, row status và menu permission đều nằm phía client. Chúng giúp UX/orchestration nhưng không thay server validation/authorization.

## 5. Ba loại state ownership

Một state nên có một owner chính.

**Presentation state**: focus, expanded group, current tab, spinner.

**Client business working state**: DataMap/DataList đang edit, dirty status, search snapshot.

**Canonical business state**: server/database hoặc authoritative backend service.

Bug xuất hiện khi presentation state được dùng làm business truth, hoặc client working state được coi là canonical sau khi server đã normalize/change.

## 6. Design một screen từ invariant trước component

Trước khi kéo Grid/Input trong Studio, viết invariant:

```text
Order ID immutable sau create.
Amount > 0.
Chỉ APPROVED request mới được export.
Hai user không được silently overwrite nhau.
Save không được duplicate khi retry.
```

Sau đó map owner:

```text
UI filter/feedback → WebSquare
working edit state → DataList
cross-field validation → page/domain function
concurrency/idempotency/authorization → server
```

Component/API được chọn sau khi owner rõ.

## 7. Design page contract như service contract

Mỗi reusable screen/UDC/popup nên có:

```text
input
public commands
observable output/events
owned state
side effects
lifecycle/cleanup
```

Ví dụ Order Detail:

```text
Input: { orderId, mode }
Command: reload(), canClose()
Output: ORDER_CHANGED / close result
Owned state: dmOrder, validation state, pending save
Side effect: sbmLoad, sbmSave
Cleanup: timer/listener/pending result guard
```

Nếu consumer cần biết `inputOrderId` hoặc `grdLine`, contract chưa đủ tốt.

## 8. Design Submission từ failure trước success

Happy path dễ viết. Production design nên bắt đầu bằng câu hỏi:

```text
Nếu timeout sau server commit thì sao?
Nếu response cũ về sau response mới thì sao?
Nếu user double-click thì sao?
Nếu session expire thì sao?
Nếu partial batch fail thì sao?
Nếu page đóng khi request pending thì sao?
```

Sau khi trả lời được, success path thường tự rõ.

## 9. Debugging playbook: từ symptom đến boundary

Khi incident xảy ra, không đọc toàn codebase. Đi theo evidence chain.

```text
1. Reproduce và ghi user intent.
2. Xác định screen instance/scope.
3. Snapshot client model trước action.
4. Trace event/call path đến Submission.
5. Inspect request payload thực tế.
6. Inspect HTTP status/body/timing.
7. Correlate server trace nếu có.
8. Inspect target/model sau response.
9. Inspect rendering/selection/focus.
10. Kiểm tra callback stale hoặc cleanup/lifetime.
```

Nếu bước 4 chưa có request, đừng debug SQL. Nếu response đúng và DataList đúng, đừng blame API.

## 10. Performance playbook: chia latency thành budget

Một search screen:

```text
T_total
= T_event
+ T_validation
+ T_request_queue
+ T_network_server
+ T_download_parse
+ T_mapping
+ T_render
+ T_post_render
```

Đo từng phần. “Grid chậm” có thể thật ra là 8 MB response hoặc formatter O(n²).

Performance fix phải giảm dominant term, không giảm term dễ sửa nhất.

## 11. Memory playbook: reachability thay vì “đã close”

Garbage collector chỉ giải phóng object không còn reachable.

Một closed page vẫn sống nếu:

```text
global registry → scope
document listener → closure → scope
setInterval → callback → DataList
pending promise/callback → page object
third-party widget → DOM/component
```

Test bằng repeated lifecycle:

```text
open → interact → close × 30
```

Sau mỗi vòng quan sát heap, listener/request count. Một heap snapshot đơn lẻ không đủ chứng minh leak.

## 12. Security playbook: giả định client bị sửa

Khi review Save flow, tưởng tượng user đã:

```text
unhide hidden field
enable disabled button
change DataList directly
forge row status
modify request payload
replay request
change entity ID
```

Nếu server vẫn giữ invariant, architecture đúng. Nếu chỉ UI ngăn được, đó là security gap.

## 13. Migration playbook: preserve invariant, replace mechanism

Khi migrate legacy `$w`, IFrame, global variable, jQuery DOM hack hoặc synchronous Submission, đừng rewrite chỉ vì syntax cũ.

Quy trình:

```text
identify current behavior/invariant
→ capture regression evidence
→ identify hidden dependency
→ choose modern boundary
→ migrate one boundary
→ compare behavior/performance
→ remove compatibility layer khi evidence đủ
```

Ví dụ `window.parent.grdA...` không nên đổi máy móc thành `$p.parent().grdA...`. Mục tiêu là thay direct internal access bằng page contract nếu có thể.

## 14. Release playbook: source không phải artifact

Một release phải trace được:

```text
Git commit
→ W-Pack/build tool + config
→ artifact hash/version
→ deployed environment
→ cache/CDN/browser response
→ runtime engine/config identity
```

Nếu user thấy UI cũ, “commit đã merge” không phải evidence đủ. Network response/artifact version mới là evidence browser đang chạy gì.

## 15. Case study A — Search result thỉnh thoảng quay về dữ liệu cũ

Symptom: user search `Kim`, đổi nhanh thành `Lee`; đôi lúc Grid cuối cùng lại hiển thị `Kim`.

Page graph không có vấn đề. Data graph có một target `dlUser`. Request graph có A và B chạy async.

```text
A(Kim) sent
B(Lee) sent
B response → dlUser = Lee
A response → dlUser = Kim
```

Root cause là latest-intent invariant thiếu. Fix boundary có thể là cancel request cũ nếu API/build hỗ trợ hoặc request generation token để stale callback không apply result.

Regression test phải cố tình làm A chậm hơn B. Debounce chỉ giảm tần suất, không chứng minh ordering.

## 16. Case study B — Save đôi lúc gửi giá trị cũ của cell cuối

Symptom: user gõ `100`, click Save ngay; server nhận `90`.

Đừng thêm delay. Trace editing lifecycle:

```text
editor value = 100
DataList value = 90
Save handler executes
Submission serializes DataList
```

Root cause nằm ở edit commit boundary. Fix bằng public lifecycle/API/convention để current edit commit trước serialization, sau đó test trực tiếp “edit rồi click Save không blur trước”.

Đây là ví dụ editor state khác canonical client model.

## 17. Case study C — Popup save xong refresh nhầm tab

Có hai Order List tab với filter khác nhau. Detail popup dùng `$p.top()` tìm `grdOrder` và update row index 4.

Bug có ba identity bị trộn:

```text
screen instance identity
business order identity
row index
```

Fix architecture: popup trả `{orderId, changed:true}` về owner/caller. Caller quyết định re-query hoặc patch bằng business key. Không traverse top để tìm Grid.

## 18. Case study D — Grid 50.000 row load nhanh network nhưng UI freeze

Network 150 ms, response 6 MB, parse + DataList + render 3.5 s. Performance trace cho thấy formatter và summary chạy nhiều.

Possible strategy:

```text
server paging/filter để giảm row
simplify formatter hot path
reduce derived recalculation
use appropriate Grid rendering strategy
avoid eager hidden tabs
```

Đừng chỉ bật virtual scroll rồi kết luận xong; parse/model memory vẫn còn nếu full payload giữ nguyên.

## 19. Case study E — Mở/đóng tab nhiều lần request tăng gấp đôi

Lần đầu một polling request/30s. Sau 10 lần mở/đóng, Network thấy 10 request/30s.

Hypothesis mạnh: timer/listener lifecycle leak.

Trace lifetime graph cho thấy `setInterval` giữ closure `scwin.refresh`. Tab close không clear timer. Fix ở cleanup boundary, không ở backend rate limit.

Regression test lặp open/close và assert active timer/request count không tăng.

## 20. Case study F — Production lỗi nhưng UAT đúng

Source commit giống nhau. Đừng dừng ở Git.

So sánh:

```text
engine build
W-Pack artifact hash
client/server config
context root
proxy/cache header
browser artifact response
backend API version
```

Nếu PROD còn artifact cũ, fix deployment/cache. Nếu engine build khác, kiểm tra release note/regression. Nếu config khác, tìm config drift.

## 21. Case study G — Batch Save 100 row, 3 row lỗi

Nếu backend all-or-nothing, client phải giữ 100 row chưa commit và show 3 nguyên nhân. Nếu backend partial, 97 row cần normalize/reset, 3 row giữ dirty/error.

Không thể thiết kế UI đúng nếu transaction contract chưa rõ. Đây là ví dụ “frontend bug” thực ra là contract ambiguity.

## 22. Case study H — User không có menu nhưng vẫn gọi được Save API

Ẩn menu chỉ là navigation UX. Nếu endpoint không check authorization, attacker có thể forge request.

Fix server authorization. Frontend vẫn có thể ẩn/disable để UX phù hợp, nhưng security test phải gọi request không qua UI và kỳ vọng server reject.

## 23. Case study I — Excel export lộ cột nhạy cảm

Grid ẩn `PERSONAL_ID`, nhưng DataList vẫn có field và export config lấy source data rộng hơn visible view.

Root cause: hidden presentation bị nhầm với data authorization/export contract.

Fix bằng explicit export schema/whitelist và server policy nếu export được tạo server-side. Regression test file output, không chỉ screenshot Grid.

## 24. Case study J — Engine upgrade làm event order thay đổi

Một screen phụ thuộc `onviewchange` chạy trước/after edit theo assumption cũ. Engine/build mới có property/default khác.

Migration flow:

```text
capture old event trace
read release note/API reference
set explicit config nếu cần
update regression test
remove reliance on ambiguous order nếu có thể
```

Đây là lý do library ưu tiên mechanism và evidence hơn học thuộc default.

## 25. Code review ở mức Master

Một review tốt không chỉ tìm syntax lỗi. Nó hỏi:

```text
State owner là ai?
Identity nào đang được truyền?
Index có sống lâu hơn event không?
Async result có stale guard không?
Page contract có xuyên internals không?
Dirty state có thể mất khi navigation không?
Server contract có concurrency/idempotency không?
Failure path có terminal cleanup không?
Bulk operation có event/render storm không?
Generated/private API có bị phụ thuộc không?
Test nào chứng minh invariant này?
Production evidence nào giúp debug nếu nó fail?
```

Nếu PR không trả lời được các câu liên quan, review chưa kết thúc ở mức architecture.

## 26. Master checklist cho một screen mới

### Trước khi code

Xác định screen purpose, input/output contract, DataCollection owner, server contract, identity và transaction semantics.

### Khi code

Giữ handler mỏng, domain function có tên, model là source of truth, Scope dependency explicit, async lifecycle có guard và cleanup.

### Trước khi merge

Test success/error/timeout/double-click/stale response/unsaved navigation; kiểm tra keyboard/accessibility; đo dataset/performance hợp lý; không log secret/PII.

### Trước khi deploy

Biết artifact/build/config identity, regression trên engine tương ứng, cache strategy và rollback path.

### Khi production lỗi

Lấy evidence trước khi sửa. Xác định boundary rồi mới thay code.

## 27. Capstone Master — xây một mini enterprise application

Capstone nên có:

```text
App shell
├─ menu
├─ multi-tab navigation
├─ Employee Search
├─ Employee Detail
└─ reusable EmployeePicker UDC
```

Employee Search dùng `dmSearch → sbmSearch → dlEmployee → GridView`, server paging và query snapshot. Detail mở bằng navigation key theo employee ID, có optimistic locking và unsaved-change guard. EmployeePicker expose property/method/event, không biết parent internals.

Thêm fault injection:

```text
search A response về sau B
Save double-click
timeout sau commit
version conflict
session expiration
partial batch failure
Excel import invalid row
tab close khi request pending
30 lần open/close để test leak
stale W-Pack cache ở environment giả lập
```

Nếu bạn có thể giải thích owner, identity, lifecycle, evidence và fix boundary của từng case, bạn đã đi qua library theo đúng mục tiêu.

## 28. Cách tiếp tục sau library này

Sau mức Master, giá trị cao nhất không đến từ thêm 500 property GridView vào note. Nó đến từ đọc API/release note đúng build khi cần, quan sát codebase thực, và bổ sung case study khi gặp một failure mode mới có tính khái quát.

Một topic chỉ nên được thêm vào canonical library nếu nó tạo mental model hoặc reasoning reusable. Project-specific ID, endpoint và workaround nên ở project docs/runbook, không làm loãng canonical WebSquare knowledge.

## 29. Bản đồ quay lại chapter gốc

Khi thiếu runtime/page mental model, quay lại [01](01_platform_runtime_page_model.md) và [02](02_components_events_binding.md).

Khi lỗi data/request, quay lại [03](03_data_collection_submission.md) và [15](15_backend_contract_transaction_concurrency.md).

Khi lỗi Scope/navigation, quay lại [04](04_scope_wframe_popup_spa.md) và [14](14_application_shell_navigation_state.md).

Khi lỗi Grid/edit/index, quay lại [05](05_gridview_crud_patterns.md) và [13](13_gridview_editing_identity_internals.md).

Khi lỗi production/performance/security, quay lại [06](06_debugging_performance_security.md), [10](10_rendering_lazy_loading_lifetime.md) và [12](12_build_config_deployment.md).

Khi refactor/migrate/test, quay lại [07](07_legacy_modern_migration.md), [08](08_reusable_architecture_udc_common_modules.md) và [11](11_testing_testability_regression.md).

## 30. Kết luận

Mental model cuối cùng của WebSquare enterprise development là:

```text
Intent
→ Screen instance
→ Event
→ Canonical client state
→ Contract
→ Server transaction
→ Canonical result
→ Reconciliation
→ Render
→ Evidence
```

Bao quanh flow đó là Scope, lifetime, security, performance, testing và deployment identity.

Khi bạn có thể giữ tất cả boundary này rõ trong đầu, WebSquare không còn là một tập API khó nhớ. Nó trở thành một runtime có quy tắc mà bạn có thể reasoning, đo, test và vận hành một cách có hệ thống.

---

## 31. Master extension — thêm ba graph cho file, native và evidence

Khi library mở rộng sang file transfer, hybrid app và observability, năm graph ban đầu vẫn đúng nhưng chưa đủ chi tiết cho production system hiện đại. Hãy bổ sung ba graph chuyên biệt.

**Artifact graph** theo dõi file/upload/export artifact từ browser đến storage, metadata và business owner.

**Native capability graph** theo dõi WebSquare intent → bridge request → native/plugin operation → callback/deep link → WebSquare reconciliation.

**Evidence graph** theo dõi user action → request/correlation ID → client log → network → server/native log → metric/trace.

Một incident có thể giao cả ba:

```text
User export report trong hybrid app
→ server tạo file
→ native download
→ app background
→ callback về page cũ
→ log không có requestId
```

Nếu chỉ nhìn Submission graph, bạn sẽ bỏ lỡ storage/native/lifetime boundary.

## 32. Identity model mở rộng

Master track mới cần phân biệt thêm:

```text
attachment/file ID
physical storage key
upload session/intent ID
export job ID
native operation request ID
app/web build ID
correlation/trace ID
```

`fileName`, `rowIndex`, `URL` hay callback function name không phải identity ổn định cho các operation dài.

Rule tổng quát:

```text
identity phải sống ít nhất lâu bằng operation mà nó đại diện
```

Nếu operation sống qua page reload/background, identity không thể chỉ là local variable trong page.

## 33. Case study K — Upload thành công nhưng Save fail

User upload ba attachment, sau đó Save contract bị optimistic lock conflict. Storage đã có file nhưng contract transaction rollback.

Nếu hệ thống không có staging/cleanup, ba file trở thành orphan.

Reasoning:

```text
file transfer success ≠ business commit success
```

Fix architecture có thể là upload session/staging + promote sau commit hoặc compensating cleanup có expiry. Regression test phải kiểm tra storage/metadata sau failed Save, không chỉ UI message.

## 34. Case study L — Excel import “thành công” nhưng dữ liệu sai cột

User thêm một column ở đầu template. Import code map theo index nên `CUSTOMER_NAME` nhận giá trị của column khác. Parser không throw exception.

Đây là silent semantic corruption, nguy hiểm hơn parse failure.

Fix:

```text
version/header validation
→ explicit column mapping
→ type conversion
→ business validation
→ preview/error report
→ commit
```

Test phải bao gồm reordered/missing/extra header, không chỉ happy template.

## 35. Case study M — Hybrid eKYC callback về sau khi user đóng screen

Page A start camera với `nativeRequestId=R1`. User chuyển screen. Native SDK hoàn tất và callback R1.

Nếu bridge gateway gọi trực tiếp `scwin.onSuccess`, stale scope có thể không còn hoặc callback update nhầm screen instance mới.

Fix boundary:

```text
native callback
→ gateway
→ resolve request owner/session
→ owner còn valid?
   ├─ yes → deliver result
   └─ no  → persist/ignore theo workflow contract
```

Đây là stale Submission problem mở rộng qua native boundary.

## 36. Case study N — Web deploy mới phá app native cũ

Web build mới gọi plugin API V2 nhưng nhiều user chưa update app và chỉ có V1.

Source web đúng, backend đúng, browser desktop đúng, chỉ hybrid app cũ fail.

Root cause là release graph không chứa compatibility matrix.

Fix architecture:

```text
capability/version handshake
→ compatible adapter path
→ minimum supported app policy
→ telemetry appVersion + webBuildId
```

Web và native release cadence phải được coi là distributed deployment.

## 37. Case study O — Production incident không reproduce được vì thiếu build identity

User báo Save treo. Team kiểm tra source mới nhất và không thấy bug. Sau đó mới phát hiện browser đang dùng W-Pack artifact cũ từ cache node khác.

Root cause không phải chỉ cache; root cause operational là evidence không ghi artifact identity.

Sau incident cần thêm:

```text
build ID visible trong diagnostics
resource version/cache policy
correlation ID
release dashboard
runbook kiểm tra artifact trước source
```

Một fix tốt thay đổi khả năng phát hiện lần sau, không chỉ xóa cache một lần.

## 38. Master design review cho file/hybrid/observability

Khi PR thêm upload/export/native capability, review thêm các câu:

```text
File content, metadata và business row có cùng transaction không?
Orphan cleanup ở đâu?
Filename/path có được tin từ client không?
Large export chạy client hay server và vì sao?
Native callback có request identity không?
Page đóng/background thì operation ra sao?
Web build có compatible với app cũ không?
Bridge expose capability tối thiểu chưa?
Sensitive data có đi qua log/JS global không?
Nếu incident xảy ra, request/build/file/native identity nào giúp trace?
```

Đây là những câu hỏi architecture, không phải framework trivia.

## 39. Master capstone mở rộng

Mở rộng mini enterprise app ở section 27 bằng ba capability.

Thứ nhất, thêm attachment staging cho Employee Detail. Upload trước Save, fail Save bằng version conflict và chứng minh orphan cleanup đúng.

Thứ hai, thêm Excel import cho Employee Search. File phải qua header/schema validation, preview invalid rows và chỉ commit khi user xác nhận.

Thứ ba, giả lập hybrid identity verification. Fake native bridge trả callback chậm, callback sau page close, permission denied và app-version mismatch.

Cuối cùng thêm observability:

```text
screenInstanceKey
requestId
uploadSessionId
nativeRequestId
webBuildId
engineBuild
elapsed stage timings
```

Tạo ba runbook và fault-inject để người khác có thể điều tra mà không đọc source trước.

Nếu capstone chỉ chạy happy path thì chưa phải Master.

## 40. Master definition sau khi mở rộng đến chapter 19

Một WebSquare engineer ở mức Master không được định nghĩa bởi số API nhớ được. Người đó có thể:

```text
mô hình hóa state và owner;
phân biệt identity theo lifetime;
thiết kế page/data/server/file/native contract;
reason async ordering và transaction ambiguity;
đo performance thay vì đoán;
coi browser/native client là untrusted;
thiết kế compatibility giữa engine/web/native/backend;
truy vết incident bằng correlation và artifact identity;
biến incident thành regression guard/runbook;
đọc official API/release note đúng build khi exact behavior cần xác minh.
```

Từ đây, chapter mới chỉ nên được thêm nếu nó mở một boundary hoặc mental model chưa được library giải thích. Danh sách API dài, workaround riêng của một project hoặc copy nguyên reference không làm tăng mastery.