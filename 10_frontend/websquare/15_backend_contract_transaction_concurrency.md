# 15 — Backend Contract, Transaction & Concurrency Integration

WebSquare là frontend platform, nhưng phần khó nhất của màn hình enterprise thường nằm ở **ranh giới client–server**. DataList có row status, Submission có reference/target và Grid có validation, nhưng database transaction, authorization, locking và business invariant thật sự vẫn thuộc backend.

Chapter này không dạy lại Java/Spring hay database. Nó tập trung vào câu hỏi WebSquare developer phải reasoning được: **client gửi contract gì, server trả contract gì, row state được dịch thành command thế nào, retry có an toàn không, conflict được biểu diễn ra sao, và UI làm gì khi kết quả transaction không đơn giản là success/fail**.

## 1. Submission là transport contract, không phải transaction

Mental model:

```text
WebSquare page
→ DataCollection
→ Submission serialization
→ HTTP
→ server controller/service
→ transaction/database
→ response
→ Submission target
→ UI state
```

`executeSubmission()` không mở database transaction trong browser. Một Workflow chạy ba Submission liên tiếp cũng không tự làm ba HTTP call thành một ACID transaction.

Nếu ba operation phải commit hoặc rollback cùng nhau, backend cần một transaction boundary hoặc một business command phù hợp.

## 2. CRUD row status cần mapping contract rõ

Client có thể giữ row `C/U/D`. Server phải biết semantics này bằng một contract được thống nhất.

Có hai style phổ biến:

```text
style A: payload chứa row status + row data
style B: payload tách created/updated/deleted collections
```

Không có style luôn tốt hơn. Điều quan trọng là server không “đoán” operation từ field rỗng hoặc vị trí row.

Ví dụ conceptual:

```json
{
  "created": [{"clientKey":"tmp-1","name":"A"}],
  "updated": [{"id":"U1001","version":7,"name":"B"}],
  "deleted": [{"id":"U1002","version":3}]
}
```

Contract tách operation rõ và dễ validate.

## 3. Client row status không phải authorization proof

User có thể sửa payload trong DevTools:

```text
U → D
ROLE=USER → ROLE=ADMIN
PRICE=100 → PRICE=0
```

Server phải quyết định caller có quyền create/update/delete field/entity đó không. Row status chỉ là **client intent**, không phải evidence rằng operation hợp lệ.

## 4. Writable-field whitelist quan trọng hơn hidden/readOnly

Một screen có thể nhận object gồm 30 field nhưng user chỉ được sửa 4 field. Nếu client gửi lại toàn object, server không nên mass-assign tất cả field.

Contract nên phân biệt:

```text
identity fields
writable fields
server-owned fields
calculated fields
audit fields
```

Ví dụ `createdBy`, `approvedAt`, `role`, `version` có thể là server-owned tùy domain. UI hidden/readOnly chỉ giúp UX.

## 5. Canonical value phải được thống nhất ở API boundary

UI có thể hiển thị:

```text
₩1,234,567
2026.09.22
서울
```

Payload nên dùng representation ổn định:

```text
1234567
2026-09-22 hoặc contract date đã thống nhất
SEOUL hoặc code tương ứng
```

Đừng để backend parse string display phụ thuộc locale nếu model đã có canonical value.

WebSquare binding/formatter nên giữ presentation và domain value tách nhau.

## 6. Empty, null, absent là ba semantic khác nhau

Update API cần đặc biệt rõ:

```text
field absent → không thay đổi?
field: null → xóa giá trị?
field: "" → chuỗi rỗng hợp lệ hay normalize null?
```

Nếu client serializer tự chuyển đổi theo DataList/DataMap config, test contract phải kiểm tra payload thực tế trong Network. Không chỉ nhìn JavaScript object trước submit.

## 7. Business error nên có machine-readable code

Response chỉ trả message Korean như:

```text
"이미 처리된 데이터입니다."
```

khó cho client mapping behavior và i18n.

Tốt hơn:

```json
{
  "success": false,
  "code": "ALREADY_PROCESSED",
  "message": "이미 처리된 데이터입니다.",
  "details": {}
}
```

Client dùng `code` để quyết định behavior; `message` dùng hiển thị/log tùy policy. Nếu frontend đa ngôn ngữ, có thể map code sang locale key thay vì phụ thuộc raw server sentence.

## 8. Transport success, application success và transaction success

Một response HTTP 200 có thể chứa business failure. Một HTTP 500 có thể xảy ra sau khi transaction đã commit nhưng response serialization/network bị lỗi ở boundary khác.

Do đó client cần phân biệt:

```text
request reached server?
server understood request?
business command accepted?
transaction committed?
response reached client?
```

Trong timeout/network loss, client đôi lúc **không biết** transaction đã commit hay chưa. Đây là lý do mutation retry cần idempotency.

## 9. Idempotency cho Save quan trọng khi network không chắc chắn

Scenario:

```text
client gửi Create Payment
server commit thành công
response bị mất
client timeout
user bấm Save lại
```

Nếu server tạo transaction mới mỗi lần, duplicate có thể xảy ra.

Một idempotency/business request key giúp server nhận ra retry của cùng logical command. Cách implement thuộc backend/domain, nhưng WebSquare client cần biết khi nào tạo/giữ key.

Rule: retry query thường dễ hơn retry mutation. Không auto-retry Save chỉ vì `submiterror` chạy.

## 10. Optimistic locking là contract giữa UI và database

Client đọc entity version 7. Khi save:

```json
{
  "id": "ORD-1001",
  "version": 7,
  "status": "APPROVED"
}
```

Server update với expectation version 7. Nếu version hiện đã là 8, server trả conflict.

Client không nên silently overwrite. UX có thể:

```text
reload canonical server state
show conflict message
show diff nếu domain cần
cho user re-apply change
```

Row status `U` chỉ nói client đã sửa; nó không nói server row vẫn như lúc client đọc.

## 11. Conflict khác validation failure

Validation failure nghĩa input vi phạm rule. Conflict nghĩa input có thể hợp lệ nhưng state nền đã thay đổi.

```text
INVALID_EMAIL → sửa email
VERSION_CONFLICT → reload/compare state
ALREADY_APPROVED → operation state đã chuyển
PERMISSION_DENIED → authorization
```

Nếu mọi lỗi đều hiện “저장 실패”, user không biết hành động tiếp theo.

Error taxonomy là một phần của API contract.

## 12. All-or-nothing batch transaction

Với 100 row save, backend có thể chọn một transaction:

```text
validate all
→ apply all
→ commit all
```

Một row fail thì rollback tất cả. Client giữ toàn bộ changed rows dirty và highlight lỗi gây rollback.

Ưu điểm là invariant toàn batch dễ giữ. Nhược điểm là một row lỗi chặn 99 row đúng.

UI phải nói rõ “không row nào được lưu” thay vì đánh dấu success từng row trước khi transaction result cuối cùng có.

## 13. Partial success cần protocol mạnh hơn

Nếu backend cho phép row độc lập commit, response phải nói row nào thành công/thất bại bằng stable key.

```json
{
  "results": [
    {"id":"A","status":"SUCCESS","version":8},
    {"id":"B","status":"ERROR","code":"DUPLICATE"}
  ]
}
```

Client chỉ reset dirty state cho row A; row B giữ edit/error. Nếu client reset toàn DataList sau HTTP 200, user mất unsaved correction.

Partial success là distributed state reconciliation problem, không chỉ là “loop alert”.

## 14. Created row cần client correlation key

Row mới chưa có server ID. Nếu batch create 10 row và server sinh sequence, response cần map ID về đúng client row.

Có thể dùng temporary client key:

```json
{"clientKey":"tmp-7","name":"Kim"}
```

Response:

```json
{"clientKey":"tmp-7","id":"USR-10442","status":"SUCCESS"}
```

Không map bằng array index nếu server có thể reorder result hoặc partial failure.

## 15. Delete cần version và ownership như update

Delete không chỉ là `DELETE WHERE ID=?`. Nếu record đã đổi hoặc không còn thuộc quyền user, server phải enforce rule.

Client gửi identity/version cần thiết; server xác thực permission/invariant. Nếu delete conflict, UI không nên đơn giản remove row local rồi coi như xong.

## 16. Search contract phải snapshot điều kiện đã execute

User có thể sửa `dmSearch` sau khi request bắt đầu. Response A tương ứng condition A, trong khi UI input đã là B.

Nên giữ request identity và snapshot:

```javascript
scwin.lastExecutedSearch = {
    requestId: requestId,
    condition: /* clone plain data */
};
```

Khi export/report hoặc debug, biết dataset hiện tại sinh từ query nào. Điều này cũng hỗ trợ stale-response guard.

## 17. Latest-intent guard cần server/client cooperation khi có side effect

Search response cũ có thể bỏ qua ở client. Save response cũ thì phức tạp hơn vì server side effect có thể đã xảy ra.

Do đó:

```text
read request → cancellation/latest-response policy thường đủ
mutation → cần duplicate guard/idempotency/concurrency contract
```

Đừng áp cùng một “ignore stale response” pattern cho mọi operation.

## 18. Workflow phù hợp orchestration đọc hơn transaction mutation phức tạp

WebSquare Workflow có thể mô tả thứ tự nhiều Submission và official guide khuyến nghị dùng cho flow query/select phù hợp. Nhưng nếu Save A rồi Save B phải atomic, hai Submission nối bằng Workflow vẫn không tạo server transaction chung.

Tốt hơn có thể là một backend command duy nhất nếu invariant yêu cầu atomicity.

First principle: **transaction boundary phải nằm nơi có quyền kiểm soát resource cần commit**.

## 19. File/Excel import cần staging mindset

Excel 10.000 row không nên đi thẳng từ upload thành commit nếu domain phức tạp.

Một pipeline an toàn hơn:

```text
parse
→ normalize
→ client preview
→ server validate
→ return row-level errors
→ user correct/confirm
→ commit command
```

Với dataset lớn, server-side staging/import job có thể phù hợp hơn giữ mọi row trong browser. WebSquare Grid là UI cho process, không nhất thiết là nơi xử lý toàn bộ import.

## 20. Long-running operation cần job semantics

Một report/export/import mất 2 phút không nên giả định HTTP request giữ UI blocking là tốt nhất.

Backend có thể dùng async job:

```text
POST create job
→ jobId
→ poll/status/subscription
→ completed/failed
→ download/result
```

Client cần state machine:

```text
IDLE → SUBMITTED → RUNNING → SUCCEEDED/FAILED/CANCELLED
```

Đừng dùng một boolean `isLoading` cho workflow nhiều trạng thái.

## 21. Session expiration là protocol event, không chỉ generic error

Nếu session hết hạn, nhiều Submission có thể đồng thời nhận 401/403 hoặc response convention riêng. Common layer cần policy tránh 10 popup “session expired”.

Application shell có thể coordinate:

```text
first auth-expired signal
→ freeze new protected actions
→ show one re-auth/login flow
→ pending operation policy
```

Nhưng backend status semantics phải rõ. Không map mọi 403 thành session expired vì 403 cũng có thể là permission denial.

## 22. Correlation ID nối frontend incident với backend trace

Client log:

```text
screen=ORDER_DETAIL
operation=SAVE
requestId=abc-123
orderId=ORD-1001
```

Server/gateway log cùng correlation/trace ID giúp tìm transaction. Không log full payload nếu chứa PII.

Production support tốt cần đủ context để trả lời: request nào, screen instance nào, business entity nào, build nào.

## 23. Contract versioning và backward compatibility

Frontend artifact và backend release có thể deploy lệch thời điểm. Nếu API contract thay breaking ngay, rolling deployment/cache cũ có thể lỗi.

Cần policy:

```text
additive field change
optional field/default
versioned endpoint/schema nếu cần
compatibility window
```

WebSquare W-Pack cache làm khả năng client cũ sống lâu hơn đáng kể. Backend nên tính đến stale client trong deployment strategy.

## 24. Client-generated business rule dễ drift

Nếu cùng rule được copy ở 20 screen và backend, sớm muộn sẽ lệch.

Client có thể duplicate một subset để UX nhanh, nhưng server vẫn là owner invariant. Khi rule thay đổi, cần centralize metadata/common function hoặc trả constraint từ server nếu phù hợp.

Không nên đưa toàn business engine xuống browser chỉ để tránh request.

## 25. Contract test quan trọng hơn screenshot test cho integration

Một regression suite nên chứng minh:

```text
C/U/D serialize đúng
null/empty semantics đúng
business error code map đúng
version conflict không reset dirty state
partial success reconcile đúng row
created clientKey map đúng server ID
timeout không auto-duplicate mutation
401/403 đi đúng auth/permission path
```

Screenshot không chứng minh các invariant này.

## 26. Case study: batch approval có conflict

User search 200 request, chọn 20 row và bấm Approve. Client snapshot `REQUEST_ID + VERSION`. Server nhận batch command.

Trong lúc user thao tác, 2 row đã được người khác approve. Server có thể chọn all-or-nothing hoặc partial policy. Nếu all-or-nothing, response trả conflict list và không commit row nào. Client giữ 20 row unchanged/dirty theo workflow và yêu cầu refresh. Nếu partial, 18 row success được normalize/reset; 2 row conflict giữ error state và hiển thị canonical server status.

Điểm quyết định không nằm ở Grid API. Nó nằm ở transaction contract. Grid chỉ phản ánh result.

## 27. Boundary với canonical backend docs

Chi tiết Spring transaction propagation, controller/service architecture, database isolation level, SQL locking, authentication framework và API design tổng quát thuộc canonical `10_backend/` và Computer Science/Database docs của repository.

WebSquare chapter này chỉ giữ phần giao nhau cần cho frontend reasoning. Khi cần hiểu vì sao optimistic locking hoạt động ở SQL/JPA/MyBatis hoặc transaction rollback xảy ra thế nào, hãy đọc backend canonical thay vì duplicate ở đây.

## 28. Master checklist cho client–server contract

Trước khi productionize một Save flow, phải trả lời được:

```text
Operation identity là gì?
Business entity identity là gì?
Writable fields là gì?
Null/empty/absent nghĩa gì?
Concurrency version nằm ở đâu?
Retry có an toàn không?
Transaction all-or-nothing hay partial?
Error code machine-readable là gì?
Created row map server ID bằng gì?
Sau success client lấy canonical state ở đâu?
Timeout thì user biết trạng thái chắc chắn hay không chắc chắn?
Server authorization kiểm tra gì dù UI đã hidden/readOnly?
```

Nếu một câu chưa có answer, đó là contract gap chứ không phải “việc frontend/backend tự xử lý”.

## 29. Kết nối

Ba chapter 13–15 đi từ identity của row → identity của screen instance → identity của transaction/request. Chapter cuối tổng hợp các lớp này thành cách reasoning cấp Master: [16 — Master Production Playbook & End-to-End Case Studies](16_master_production_playbook.md).
