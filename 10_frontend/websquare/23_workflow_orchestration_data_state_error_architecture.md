# 23 — Workflow Orchestration, Advanced Data State & Enterprise Error Architecture

Chapter 03 đã giải thích DataCollection và Submission như hai primitive cốt lõi của WebSquare. Chapter này đi thêm một tầng: khi một user action không còn tương ứng với một request đơn lẻ mà trở thành **một workflow có nhiều bước, nhiều state transition và nhiều failure mode**, ta phải reasoning thế nào để screen vẫn đúng khi timing thay đổi.

Mục tiêu không phải học thuộc `$p.workflow`. Mục tiêu là nhìn một flow như `validate → load prerequisite → save → refresh → notify` và biết bước nào thực sự phụ thuộc bước nào, state nào được snapshot, lỗi nào có thể retry, và WebSquare Workflow chỉ orchestration phía client chứ không biến nhiều HTTP request thành một database transaction.

---

## 1. Từ Submission đơn lẻ đến orchestration graph

Một Submission đơn lẻ có mental model tương đối thẳng:

```text
user intent
→ prepare request state
→ execute Submission
→ server
→ response
→ target DataCollection
→ UI reaction
```

Khi nghiệp vụ lớn hơn, developer thường viết chuỗi callback:

```text
loadCode
→ loadMaster
→ loadDetail
→ saveHeader
→ saveLines
→ refresh
```

Vấn đề là danh sách tuần tự này có thể đang che giấu dependency thật. `loadCode` và `loadMaster` có thể độc lập. `saveLines` có thể phụ thuộc `saveHeader` vì cần generated ID. `refresh` chỉ có ý nghĩa nếu save thành công. Nếu chỉ nối callback theo thứ tự code được viết, ta đang encode **temporal order** thay vì **business dependency**.

Mental model tốt hơn là dependency graph:

```text
loadCode ─────┐
              ├─→ screen-ready
loadMaster ───┘

validate
→ saveHeader
→ obtain orderId/version
→ saveLines
→ refresh
```

Serial hay parallel phải là kết quả của dependency graph, không phải preference coding style.

---

## 2. WebSquare Workflow giải quyết vấn đề gì?

SP5 cung cấp Workflow để định nghĩa thứ tự thực thi nhiều Submission. Official guide mô tả cả serial step, parallel step, result handling và việc quyết định bước sau dựa trên kết quả trước. `$p.workflow` có các capability như thực thi workflow đã khai báo, chạy serial/parallel trực tiếp, kiểm tra workflow đang chạy và reject workflow; exact signature cần đối chiếu engine build.

Điểm quan trọng là Workflow giải quyết **client orchestration**:

```text
Submission A
Submission B
Submission C
        ↓
ordering / parallelism / result coordination
```

Nó không tự tạo distributed transaction:

```text
A commit server
B commit server
C fail
```

Workflow biết C fail nhưng không thể tự rollback database commit của A và B nếu backend không cung cấp transaction/compensation contract.

Vì vậy:

```text
workflow atomicity ≠ database atomicity
```

Đây là invariant quan trọng nhất của chapter.

---

## 3. Serial không có nghĩa là đúng

Serial execution phù hợp khi step sau cần output hoặc side effect của step trước.

Ví dụ tạo order:

```text
createOrder
→ response { orderId, version }
→ createOrderLines(orderId)
```

Nếu chạy parallel, line request chưa có `orderId`. Serial là dependency thật.

Nhưng flow sau không cần serial:

```text
loadDepartmentCodes
loadRoleCodes
loadCountryCodes
```

Nếu ba request độc lập, serial tạo latency:

```text
T_total ≈ T_department + T_role + T_country
```

Parallel lý tưởng gần hơn với:

```text
T_total ≈ max(T_department, T_role, T_country)
```

Tất nhiên server capacity, connection limit và downstream load vẫn phải được tính. Parallel không phải “càng nhiều càng nhanh”.

---

## 4. Parallel cũng không có nghĩa là độc lập về state

Hai request có endpoint khác nhau vẫn có thể tranh chấp cùng client state.

Ví dụ:

```text
sbmLoadCustomer → target dlResult
sbmLoadOrders   → target dlResult
```

Chúng chạy parallel nhưng cùng target. Request về sau ghi đè request về trước. Đây không phải network bug; design đã cho hai operation cùng ownership.

Parallel an toàn hơn khi:

```text
request identity độc lập
+ target state độc lập
+ side effect độc lập
+ completion aggregation rõ
```

Nếu hai step cùng sửa một DataMap hoặc cùng bật/tắt spinner global, vẫn có race dù endpoint độc lập.

---

## 5. Snapshot request state trước khi orchestration

Một lỗi enterprise phổ biến là Workflow đọc DataMap mutable ở từng step thay vì chụp user intent ban đầu.

User bấm Search với:

```text
customerId = A
```

Workflow bắt đầu. Trong lúc request đầu đang chạy, user đổi input thành B. Step sau serialize lại `dmSearch` và gửi B.

Một business action đã bị chia thành hai intent.

Khi consistency cần thiết, hãy snapshot:

```javascript
scwin.search = function () {
    var criteria = {
        customerId: dmSearch.get("customerId"),
        fromDate: dmSearch.get("fromDate"),
        toDate: dmSearch.get("toDate")
    };

    scwin.executeSearchFlow(criteria);
};
```

Exact API lấy DataMap có thể khác theo project convention; mental model là **workflow input phải có identity và snapshot rõ**.

---

## 6. Workflow instance cũng cần identity

Nếu user chạy cùng workflow hai lần:

```text
Search A → workflow W1
Search B → workflow W2
```

thì tên workflow `wfSearch` không đủ phân biệt hai intent.

Cần reasoning với:

```text
workflowDefinitionId = wfSearch
workflowRunId        = R101 / R102
userIntentVersion    = 7 / 8
screenInstanceKey    = employeeSearch#3
```

Khi callback về, câu hỏi không chỉ là “workflow nào?” mà là “run này còn thuộc intent hiện tại của screen instance này không?”.

Đây là cùng một stale-result problem đã gặp ở Submission, popup và native bridge, nhưng ở orchestration level.

---

## 7. Cancel transport và cancel business intent là hai việc khác nhau

SP5 Submission có cơ chế abort ở các build tương ứng, và Workflow có reject/cancel semantics. Nhưng abort client request không chứng minh server chưa commit.

Timeline:

```text
client gửi Save
server commit
client bấm Cancel
browser abort connection
```

UI có thể nghĩ “đã hủy”, trong khi dữ liệu đã lưu.

Vì vậy cần tách:

```text
transport cancellation
business cancellation
```

Transport cancellation chỉ dừng chờ/nhận response ở client khi còn có thể. Business cancellation phải là domain command có contract server riêng nếu nghiệp vụ hỗ trợ.

---

## 8. Workflow result không nên bị giảm thành boolean

Một orchestration lớn cần result model có cấu trúc.

Thay vì:

```javascript
success = true;
```

hãy reasoning theo:

```text
workflowRunId
stepId
requestId
status
httpStatus
businessCode
retryable
committed
correlationId
payload/result reference
```

`success=false` không nói được step nào fail, có side effect trước đó không, hay retry toàn flow có duplicate dữ liệu không.

---

## 9. Error taxonomy cho WebSquare enterprise screen

Không nên gom mọi lỗi vào một `alert("오류")`.

Một taxonomy thực dụng:

```text
Client validation error
Transport error
Protocol/HTTP error
Authentication/session error
Authorization error
Business rule error
Concurrency/conflict error
Partial batch error
Integration/downstream error
Unexpected client/runtime error
```

Mỗi loại có owner và UX khác nhau.

Client validation thường map về field/row. Authentication có thể yêu cầu re-auth hoặc redirect. Authorization không nên retry. Conflict cần reload/compare. Transport timeout có thể retry chỉ khi operation idempotent hoặc có idempotency key. Business rule phải hiển thị message đủ context nhưng không leak server internals.

---

## 10. `submitdone` không đồng nghĩa business success

SP5 phân biệt `submitdone` và `submiterror` chủ yếu theo HTTP response status. Vì vậy response HTTP 200 có thể vẫn chứa:

```json
{
  "success": false,
  "code": "ORDER_ALREADY_APPROVED",
  "message": "..."
}
```

Mental model:

```text
transport success
≠ protocol success
≠ business success
≠ state convergence
```

Sau business success, client còn phải kiểm tra canonical state đã hội tụ chưa: version mới, generated key, normalized value, permission snapshot hoặc server-calculated field có được merge đúng không.

---

## 11. Error envelope phải ổn định hơn message text

UI không nên branch theo text:

```javascript
if (message === "이미 승인되었습니다") { ... }
```

Message thay đổi theo locale hoặc wording.

Contract tốt hơn:

```json
{
  "success": false,
  "error": {
    "code": "ORDER_ALREADY_APPROVED",
    "category": "BUSINESS_RULE",
    "messageKey": "order.alreadyApproved",
    "fieldErrors": [],
    "rowErrors": [],
    "correlationId": "..."
  }
}
```

WebSquare page dùng `code/category` để chọn behavior, locale layer chọn message, correlation ID phục vụ incident trace.

---

## 12. Field error, row error và global error là ba coordinate system

Form error có coordinate:

```text
field = amount
```

Grid batch error cần business identity:

```text
entityKey = ORDER_LINE_9281
field = quantity
```

Không nên chỉ trả:

```text
rowIndex = 7
```

vì sort/filter/paging có thể làm index 7 không còn là entity server đã validate.

Global error như “downstream settlement unavailable” không thuộc field hay row cụ thể.

Error mapping đúng phải giữ coordinate system rõ.

---

## 13. DataList dirty state là state machine, không phải boolean

Developer thường hỏi “DataList có thay đổi chưa?”. Câu hỏi chính xác hơn là row nào đang ở transition nào.

Conceptually:

```text
server baseline
→ user insert
→ C

server baseline
→ user edit
→ U

server baseline
→ user delete
→ D
```

Một row mới tạo rồi xóa trước khi save có thể có semantics khác row server đã tồn tại rồi bị xóa. Release notes của SP5 từng sửa behavior quanh modified/deleted serialization, cho thấy exact edge case có thể thay đổi theo build.

Do đó code production không nên tự suy diễn row-state internals bằng array phụ nếu DataList đã là owner.

---

## 14. Row status và cell status có memory cost

Tracking thay đổi cần metadata. Với DataList rất lớn, metadata theo row/cell có thể trở thành memory pressure đáng kể. SP5 release notes 2024–2025 có thay đổi để giảm phần tử rowStatus/cellStatus không cần thiết khi set large data.

Điều này cho một bài học bền hơn API cụ thể:

```text
change tracking is not free
```

Nếu screen chỉ xem 100.000 row mà không edit, đừng mặc định architecture giống editable 100.000-row client table. Server paging, chunk loading hoặc read-only representation có thể phù hợp hơn.

---

## 15. Type conversion là contract, không phải convenience

DataList column có `dataType`, và các SP5 build mới bổ sung behavior như `preserveType`/`keepDataType` để xử lý dữ liệu string đi vào column number/date theo policy tương ứng.

Điều nguy hiểm là code chạy “có vẻ đúng” nhưng equality/sort/serialization dùng type khác kỳ vọng.

Ví dụ:

```text
"10" < "2"   // lexical semantics
10 < 2        // numeric semantics
```

Master rule:

```text
server schema
↔ DataCollection schema
↔ UI display/edit conversion
```

phải được thiết kế nhất quán. Không dùng formatter để che type model sai.

---

## 16. `null`, empty string và missing field là ba trạng thái khác nhau

SP5 mới hơn có `nullYN`/`nullYNType` cho DataList serialization/getter behavior ở các build tương ứng. Điều này tồn tại vì enterprise contract thường cần phân biệt:

```text
field missing
field = null
field = ""
```

Ví dụ PATCH semantics:

```text
missing  → không thay đổi
null     → clear value
""       → business value rỗng hoặc normalize tùy schema
```

Nếu frontend normalize tất cả về `""`, server mất thông tin intent.

Null semantics phải được quyết định ở contract boundary, không để accidental conversion quyết định.

---

## 17. Modified payload cần snapshot trước async save

Giả sử Save lấy changed rows từ DataList. User tiếp tục edit trong lúc request pending.

Nếu callback success rồi reset toàn DataList dirty state, edit mới chưa gửi có thể bị đánh dấu sạch.

Timeline:

```text
T0 snapshot changes A
T1 send A
T2 user edits B
T3 response A success
T4 reset all dirty state   ← B bị mất tracking
```

Cần một strategy như:

```text
snapshot/version changes gửi đi
→ request identity
→ success chỉ acknowledge đúng snapshot
→ preserve changes phát sinh sau snapshot
```

Exact implementation phụ thuộc project/API, nhưng invariant là **acknowledgement không được xóa mutation chưa được acknowledge**.

---

## 18. Derived view không được trở thành canonical identity

LinkedDataList, Grid sort/filter và paging tạo view coordinate. Business save/error mapping phải quay về stable entity identity.

Mental model:

```text
canonical DataList/entity
        ↓
filter/sort/derived view
        ↓
Grid view row
```

Không đi ngược bằng cách giả định `viewRowIndex === modelRowIndex`.

Chapter 13 đi sâu Grid coordinate; chapter này nhấn mạnh orchestration/error mapping phải mang business key qua toàn flow.

---

## 19. Workflow không nên sở hữu business rule

Workflow nên orchestration:

```text
prepare
→ call
→ branch result
→ continue/stop
```

Không nên chứa hàng trăm dòng rule tính giá, quyền hay trạng thái domain. Rule thuần nên nằm ở function/module testable; invariant authoritative nằm server.

Nếu Workflow definition trở thành “business engine phía browser”, testability và security đều giảm.

---

## 20. Compensation khi multi-step flow không atomic

Flow:

```text
create attachment metadata
→ upload binary
→ save business entity
```

Nếu bước cuối fail, có thể còn metadata/file orphan.

Các strategy:

```text
staging + promote
expiry cleanup
explicit compensation command
idempotent upsert
server-side transaction khi cùng boundary
```

Client Workflow chỉ gọi strategy; nó không thay thế strategy.

---

## 21. Retry phải gắn với idempotency

Không retry chỉ vì timeout.

Search/read thường dễ retry hơn command tạo side effect. Save/create cần biết:

```text
requestId / idempotencyKey
server deduplication policy
commit ambiguity
```

Nếu timeout xảy ra sau server commit, retry blind có thể duplicate.

Master question trước retry:

> Tôi có chứng minh được request này chưa commit, hoặc retry cùng identity sẽ không tạo side effect thứ hai không?

Nếu không, phải query status/reconcile thay vì retry mù.

---

## 22. Loading indicator cũng cần ownership

Hai request parallel dùng một spinner global:

```text
A start → spinner on
B start → spinner on
A done  → spinner off
B still running
```

UI báo ready sai.

Dùng operation count hoặc owner token:

```text
pending = 2
A done → 1
B done → 0 → hide
```

Tương tự disable Save button phải gắn với command instance, không phải boolean global dễ bị callback cũ reset.

---

## 23. Workflow observability

Một workflow production nên trace được:

```text
screenInstanceKey
workflowDefinitionId
workflowRunId
userIntentVersion
stepId
submissionId
requestId
correlationId
start/end/elapsed
result category
```

Không cần log toàn payload nhạy cảm. Cần log identity và timing đủ nối graph.

Khi incident “Save treo”, ta phải trả lời được nó treo ở validation, Workflow queue, Submission, gateway, server hay callback mapping.

---

## 24. Testing orchestration bằng permutation, không chỉ happy path

Một test tốt thay đổi ordering:

```text
A nhanh, B chậm
A chậm, B nhanh
A timeout
B business fail
screen close giữa flow
session expire ở step 2
user chạy flow mới trước flow cũ xong
retry sau ambiguous timeout
```

Parallel flow cần test permutation. Serial flow cần test fail ở từng boundary.

Nếu test chỉ chạy network mock với response cố định 100 ms, race bug gần như không được kiểm tra.

---

## 25. Case study — Search workflow trả state lai

Screen cần load customer và permission-dependent action list.

```text
loadCustomer(A)
loadActions(A)
```

User nhanh chóng search B. Response order:

```text
customer B
customer A
actions B
actions A
```

Nếu mỗi callback chỉ set target, cuối cùng UI có thể hiển thị customer A nhưng search box B.

Fix không phải “thêm delay”. Fix là intent identity:

```text
searchRunId
→ attach vào cả request
→ callback chỉ apply nếu runId === currentRunId
```

---

## 26. Case study — Save header thành công, line fail

Header đã commit và trả `orderId=1001`. Line save fail do validation.

UI không được hiển thị “Save failed, nothing changed”. Canonical state đã thay đổi.

Possible contract:

```text
server endpoint atomic save header+lines
```

hoặc nếu boundary buộc tách:

```text
header created
→ line failure
→ show partial state
→ allow resume/repair
→ compensation nếu domain cho phép
```

Error UX phải phản ánh transaction reality.

---

## 27. Case study — Success callback reset edit mới

User bấm Save A rồi tiếp tục sửa B. Save A success callback gọi common function reset toàn row status.

B không còn được gửi ở lần Save sau.

Root cause là acknowledgement không có mutation identity.

Regression test phải thực hiện edit trong lúc Save pending; đây là case rất dễ bị bỏ sót nếu test disable toàn screen trong mọi request.

---

## 28. Production review checklist

Trước khi approve một multi-request flow, hãy trả lời:

```text
Dependency graph thật là gì?
Step nào có thể parallel?
Workflow input có snapshot không?
Mỗi run có identity không?
Target state có bị nhiều request cùng sở hữu không?
Cancel có nghĩa transport hay business cancel?
HTTP success được tách khỏi business success chưa?
Error có category/code/coordinate ổn định không?
Retry có idempotency contract không?
Partial commit được biểu diễn thế nào?
Dirty-state acknowledgement có xóa edit mới không?
Null/type semantics có explicit không?
Loading/disabled state thuộc operation nào?
Log có đủ workflowRunId/requestId/correlationId không?
Test đã đảo response order chưa?
```

---

## 29. Master synthesis

Ở mức Master, DataCollection, Submission và Workflow không còn là ba API riêng lẻ. Chúng tạo một state-transition system:

```text
User intent
→ immutable/snapshotted command input
→ workflow run identity
→ Submission graph
→ server side effects
→ result/error taxonomy
→ acknowledgement
→ client state convergence
→ render
```

Mỗi mũi tên cần ownership và failure semantics.

Nếu chỉ nhớ `$p.executeSubmission()` hay `$p.workflow.executeSerial()`, ta mới biết mechanism. Nếu có thể giải thích **dependency, snapshot, identity, atomicity, compensation, retry safety, dirty-state acknowledgement và evidence**, ta mới reasoning được production workflow.

---

## 30. Nguồn kiểm chứng theo build

Khi cần exact API, đối chiếu WebSquare5 SP5 Development Guide/API Reference/Release Notes đúng engine build, đặc biệt các phần Workflow, Submission, DataCollection và các release note về `executeSerial`/`executeParallel`, `nullYNType`, `preserveType`/`keepDataType`, `getModifiedJSON()`/`getOnlyDeletedJSON()` và row/cell-status memory behavior.

Các API/signature có thể tiến hóa theo build. Canonical invariant của chapter là dependency, identity, transaction boundary và state convergence; không phải một signature cố định.