# 21 — Integration Topology, MSA, Real-Time & Resilience

WebSquare page cuối cùng luôn sống trong một topology lớn hơn chính nó. Một Submission có thể đi thẳng vào monolith, qua reverse proxy, API Gateway, BFF, nhiều microservice, hoặc một adapter legacy. Một screen có thể đồng thời nhận HTTP response, polling update, server push và native callback.

Nếu developer chỉ nhìn `sbmSearch.action`, nhiều failure mode production sẽ bị quy thành “API lỗi” hoặc “WebSquare lỗi” dù nguyên nhân nằm ở topology, ownership hoặc ordering.

> Mental model chính: **frontend không gọi “backend”; frontend gửi intent qua một integration topology có nhiều hop, contract và failure domain**.

## 1. Vẽ topology trước khi debug

Một flow đơn giản:

```text
WebSquare Page
→ Submission
→ Web Server / Reverse Proxy
→ Application Server
→ Service
→ Database
```

Một flow enterprise:

```text
WebSquare Shell
→ Submission
→ API Gateway
→ BFF
├─ Customer Service
├─ Order Service
├─ Code Service
└─ Legacy Adapter
   → Mainframe / External API
```

Latency, timeout, auth, retry và error mapping có thể phát sinh ở từng hop.

## 2. Frontend boundary không nên mirror microservice topology

Anti-pattern là mỗi page biết tên và URL của mọi microservice.

Khi service topology thay đổi, hàng trăm XML/Submission phải sửa. Frontend cũng phải tự aggregate data và xử lý partial failure phức tạp.

BFF hoặc stable API boundary có thể giảm coupling:

```text
Screen intent
→ stable frontend contract
→ backend orchestration
→ internal services
```

Không phải mọi hệ thống cần BFF, nhưng **frontend contract nên phản ánh user/business capability hơn deployment topology**.

## 3. WebSquare SP5 và MSA support

Các SP5 build hiện đại có configuration/API liên quan MSA như `msaCommon`, `msaServerName`, `msaName` cho một số resource/component/API. Đây là feature build-dependent và phải đối chiếu release note/API reference đúng engine.

Mental model cần giữ:

```text
logical resource/service name
→ configuration resolves target server/path
→ WebSquare loads/submits resource
```

Không hard-code assumption rằng mọi build SP5 đều có cùng property hoặc default.

## 4. `msaCommon` không biến frontend thành service registry

MSA resource configuration giúp load common module/component từ server logical tương ứng. Nó không có nghĩa business page nên tự discovery service instance, health-check pod hoặc implement load balancer.

Service discovery, routing, circuit breaker và instance health thường thuộc infrastructure/gateway/service layer.

Frontend chỉ nên biết contract cần thiết.

## 5. Resource topology và business API topology khác nhau

Có hai graph dễ bị trộn:

```text
Resource graph
XML / JS / UDC / language pack / W-Pack artifact

Business request graph
Submission / API / transaction / service
```

Một page có thể load JS từ MSA resource server nhưng gửi business Submission sang gateway khác.

Khi lỗi “screen không mở”, kiểm tra resource graph. Khi screen mở nhưng Search fail, kiểm tra request graph.

## 6. Contract-first integration

Một Submission contract tốt mô tả:

```text
intent
request schema
response schema
error taxonomy
idempotency
version/concurrency field
pagination/order semantics
security requirement
observability identity
```

Không chỉ mô tả URL.

URL là routing detail; contract mới là semantic dependency.

## 7. API Gateway không sửa contract xấu

Gateway có thể routing, TLS termination, rate limiting, authentication integration hoặc policy. Nó không tự giải quyết:

```text
field semantics mơ hồ
null vs missing
partial success không định nghĩa
retry unsafe
version conflict không biểu diễn
business error trả HTTP 200 nhưng không có code chuẩn
```

Frontend vẫn cần contract rõ như chapter 15.

## 8. BFF khi nào có giá trị

BFF hữu ích khi một screen cần aggregate nhiều nguồn hoặc cần shape riêng cho UI.

Ví dụ Employee Detail cần:

```text
employee
organization
permissions
code labels
recent activity
```

Nếu page gửi năm request và tự coordinate, nó sở hữu nhiều failure domain. BFF có thể aggregate và trả view-oriented contract.

Trade-off là BFF thêm một service cần vận hành và version.

## 9. Client fan-out và partial failure

Nếu vẫn cần nhiều Submission song song:

```text
A = employee
B = code list
C = permission
```

Không được coi “Promise.all-like success” là lựa chọn duy nhất.

Hỏi:

```text
A fail thì screen có usable không?
B fail có thể show raw code không?
C fail có được default allow không? — thường là không.
request nào critical, request nào optional?
```

Thiết kế degraded mode phải theo business semantics.

## 10. Timeout budget theo hop

Nếu frontend timeout 5 giây nhưng gateway timeout 30 giây và downstream 60 giây, request có thể tiếp tục chạy sau khi UI đã báo fail.

Mental model:

```text
T_frontend
T_gateway
T_BFF
T_service
T_external
```

Timeout phải được thiết kế theo budget, không đặt độc lập.

Mutating operation càng cần idempotency/reconciliation vì client timeout không chứng minh server chưa commit.

## 11. Retry ownership

Một request có thể bị retry ở:

```text
browser/page
common Submission layer
gateway
service client
message broker consumer
```

Nếu mọi layer đều retry 3 lần, một failure có thể khuếch đại thành nhiều request.

Retry policy phải có owner rõ và phân biệt read vs write.

## 12. Circuit breaker thuộc đâu?

Circuit breaker thường có giá trị ở service/gateway layer nơi có visibility về downstream health. Frontend có thể có UX backoff hoặc stop spam request, nhưng không nên tự giả lập infrastructure circuit breaker bằng global boolean tùy tiện.

Frontend concern là:

```text
fail fast UX
backoff polling
prevent duplicate action
show degraded state
resume/reload safely
```

## 13. Bulkhead và screen isolation

Một service chậm không nên freeze toàn shell.

Nếu Code service fail, có thể chỉ một selector bị degraded thay vì block toàn app. Nếu auth service fail, protected command có thể phải block rộng hơn.

Đây là **failure-domain design**.

## 14. Real-time không đồng nghĩa WebSocket

Có nhiều transport pattern:

```text
manual refresh
polling
long polling
Server-Sent Events (SSE)
WebSocket
native push → app event
```

Chọn theo requirement, không theo độ “modern”.

Nếu update mỗi 5 phút, polling đơn giản có thể tốt hơn WebSocket.

## 15. WebSquare boundary cho real-time

WebSquare-specific concern không phải tự invent socket API. Concern là **event từ transport cập nhật Scope/DataCollection/Grid như thế nào và lifecycle ai sở hữu subscription**.

Một adapter tốt:

```text
transport adapter
→ normalized domain event
→ screen/application event bus
→ owner checks identity/version
→ update/requery DataCollection
→ Grid renders from model
```

Không để raw socket callback đi thẳng sửa DOM.

## 16. Polling lifecycle

Polling thường bị coi nhẹ nhưng gây leak phổ biến.

```text
page open
→ start timer
→ tab hidden
→ page close
```

Phải quyết định:

```text
hidden có poll tiếp không?
interval bao lâu?
request trước chưa xong thì có gửi request mới không?
close cleanup ở đâu?
resume có immediate refresh không?
```

Chapter 10 về lifetime áp dụng trực tiếp.

## 17. Overlapping polling

Anti-pattern:

```javascript
setInterval(function () {
    search();
}, 5000);
```

Nếu Search mất 8 giây, request chồng nhau.

Pattern tốt hơn về mental model:

```text
request complete
→ wait/backoff
→ next request
```

hoặc guard `inFlight` nếu semantics cho phép.

## 18. SSE mental model

SSE phù hợp server → client stream một chiều qua HTTP. Frontend cần xử lý:

```text
connection state
last event identity
reconnect
duplicate event
out-of-order event
screen ownership
logout cleanup
```

Không assume reconnect đồng nghĩa không mất event; contract phải định nghĩa replay/resume nếu cần.

## 19. WebSocket mental model

WebSocket là long-lived bidirectional channel. Nó tạo thêm lifecycle:

```text
DISCONNECTED
→ CONNECTING
→ CONNECTED
→ DEGRADED
→ RECONNECTING
→ CLOSED
```

Một socket connection không nên mặc định thuộc từng page nếu app có nhiều screen dùng chung. Có thể app shell sở hữu connection và screen subscribe domain event.

## 20. Connection ownership

Hai lựa chọn:

**Page-owned connection** phù hợp capability hoàn toàn local và lifetime ngắn.

**Shell-owned connection** phù hợp notification hoặc shared event stream toàn app.

Sai ownership dẫn đến duplicate connection, leak hoặc event gửi vào page đã disposed.

## 21. Event identity quan trọng hơn arrival order

Real-time event có thể duplicate hoặc out of order.

Một event nên có identity/version phù hợp:

```text
eventId
entityId
entityVersion / sequence
eventType
occurredAt
correlationId
```

Frontend không nên “event đến sau thì mới hơn” nếu transport không đảm bảo ordering toàn cục.

## 22. Requery vs patch

Khi nhận `ORDER_CHANGED`, có hai chiến lược.

**Patch**: update DataList row trực tiếp. Nhanh nhưng cần event payload/version đủ mạnh.

**Requery**: dùng event như invalidation signal rồi Submission lấy canonical state. Chậm hơn nhưng đơn giản và an toàn hơn trong nhiều hệ thống.

Hybrid strategy thường hiệu quả: patch optimistic cho UX, requery khi invariant phức tạp.

## 23. Grid sort/filter và real-time patch

Nếu row đang bị filter hoặc sort, patch một field có thể làm row đổi vị trí hoặc biến mất khỏi view.

Do đó business key phải được dùng để locate model row, rồi để Grid/view layer reconcile. Không giữ view index từ trước event.

Chapter 13 giải thích identity này sâu hơn.

## 24. Backpressure

Nếu server gửi 1.000 event/giây nhưng Grid render mỗi event, UI freeze.

Cần strategy:

```text
buffer
coalesce theo entity
batch apply
throttle render
invalidate + requery
```

Backpressure là mismatch giữa producer rate và consumer capacity.

## 25. Event storm và formatter cost

Ngay cả DataList update rẻ, Grid formatter/summary/expression có thể chạy lại rất nhiều. Real-time architecture phải đo render cost, không chỉ network throughput.

## 26. Offline và reconnect

Khi browser/mobile offline:

```text
transport disconnect
pending mutation uncertain
local state stale
```

Reconnect không nên tự động replay mọi command. Query có thể refresh; mutation cần idempotency/reconciliation.

Hybrid app cần nối thêm native network state nhưng không được tin native “online” là API reachable.

## 27. Schema evolution trong event stream

Long-lived client có thể đang chạy build cũ trong khi server deploy event schema mới.

Event contract cần backward compatibility hoặc explicit versioning.

Không rename field và assume tất cả browser đã reload.

Đây là lý do browser client khác server process: client version rollout kéo dài.

## 28. Frontend version skew

Trong production cùng lúc có thể tồn tại:

```text
browser A → W-Pack v41
browser B → W-Pack v42
server → API v43 compatible mode
```

Contract migration phải chịu được overlap window.

Chapter 22 sẽ đi sâu artifact/cache identity.

## 29. MSA common resource version skew

Nếu shell load common component từ logical MSA resource server, version của common module cũng trở thành dependency.

Cần biết:

```text
shell artifact version
common component version
engine build
config routing
```

“main đã deploy” không đủ chứng minh runtime composition đồng nhất.

## 30. Cross-origin và credential boundary

Nếu resource/API nằm khác origin, browser CORS, cookie policy và security header trở thành một phần topology.

Không workaround CORS bằng disable browser security hoặc JSONP-like hack. Origin policy phải được giải quyết ở architecture/server/gateway.

## 31. File/upload trong MSA topology

Upload có thể đi vào file service khác business API. Khi đó attachment metadata và business transaction càng cần correlation identity.

```text
uploadSessionId
fileId
businessEntityId
requestId
```

Chapter 17 đã giải thích consistency giữa binary và DB state.

## 32. Auth trong multi-service topology

Frontend không nên gửi role tự khai báo để mỗi service tin theo. Credential/security context phải được gateway/service validate theo architecture.

Frontend capability vẫn chỉ phục vụ UX.

Chapter 20 là prerequisite cho phần này.

## 33. Observability xuyên topology

Một request cần correlation xuyên:

```text
screenInstanceKey
→ requestId
→ gateway trace
→ BFF trace
→ service trace
→ database/external call
```

Frontend không cần biết mọi internal span, nhưng support cần đủ identity để nối browser symptom với server evidence.

## 34. Failure taxonomy theo hop

Nên phân biệt:

```text
CLIENT_VALIDATION
CLIENT_LIFECYCLE
DNS_NETWORK
GATEWAY_REJECT
AUTH_FAILURE
UPSTREAM_TIMEOUT
SERVICE_UNAVAILABLE
BUSINESS_REJECT
CONCURRENCY_CONFLICT
SCHEMA_MISMATCH
REALTIME_DISCONNECTED
STALE_EVENT
```

Taxonomy giúp incident triage nhanh hơn generic `SYSTEM_ERROR`.

## 35. Testing topology bằng fault injection

Không chỉ mock success.

Test:

```text
gateway timeout
BFF trả partial data
service A nhanh, B chậm
response cũ về sau mới
polling overlap
socket disconnect/reconnect
duplicate event
out-of-order event
1.000 event burst
schema field mới/thiếu
browser client cũ với server mới
```

## 36. Case study — Code service chậm làm màn hình không mở

Employee data đã về nhưng page chờ code list trước render toàn bộ.

Câu hỏi architecture:

```text
code list có critical không?
có cache hợp lý không?
có thể render raw code rồi hydrate label không?
BFF nên aggregate không?
```

Fix tốt không nhất thiết là tăng timeout.

## 37. Case study — Polling tạo 12 request cùng lúc

Tab background bị throttled rồi resume; timer fire pattern và request overlap tạo burst.

Fix bằng lifecycle-aware scheduler, in-flight guard/backoff và immediate reconciliation sau resume.

## 38. Case study — WebSocket event update sai row

Callback giữ `selectedRowIndex` từ lúc subscribe. User sort Grid, event về sau và patch index cũ.

Root cause là identity boundary. Event phải mang `orderId`; locate DataList bằng business key.

## 39. Case study — Deploy service mới làm browser cũ crash

Server đổi response field từ `employeeId` thành `id`, nhưng nhiều browser vẫn chạy W-Pack cũ do cache.

Root cause là schema migration không hỗ trợ version overlap. Fix bằng backward-compatible contract hoặc coordinated versioning; không chỉ “clear cache user”.

## 40. Master checklist

```text
Topology thực tế có những hop nào?
Frontend phụ thuộc contract hay deployment URL?
Request nào critical/optional?
Timeout budget được phân bổ ra sao?
Retry owner là layer nào?
Mutation có idempotency không?
Resource MSA và business API MSA có bị trộn không?
Real-time connection owner là page hay shell?
Event có identity/version không?
Duplicate/out-of-order xử lý thế nào?
Backpressure có thể freeze Grid không?
Client cũ/server mới coexist thế nào?
Correlation ID đi xuyên topology tới đâu?
```

## 41. Connection map

Submission: [03 — DataCollection & Submission](03_data_collection_submission.md).

Lifecycle: [10 — Rendering, Lazy Loading & Resource Lifetime](10_rendering_lazy_loading_lifetime.md).

Deployment: [12 — Build, Configuration & Deployment](12_build_config_deployment.md).

Grid identity: [13 — GridView Editing, Identity & View Internals](13_gridview_editing_identity_internals.md).

Backend contract: [15 — Backend Contract, Transaction & Concurrency](15_backend_contract_transaction_concurrency.md).

File pipeline: [17 — File, Excel, Upload & Download](17_file_excel_upload_download_pipeline.md).

Authentication/session: [20 — Authentication, Session, SSO & Security Lifecycle](20_authentication_session_sso_security_lifecycle.md).

## 42. Kết luận

Integration Master không nhìn một Submission như “AJAX call”. Họ nhìn nó như một edge trong graph:

```text
User intent
→ Screen owner
→ Submission contract
→ Routing topology
→ Service transaction
→ Response/event
→ Identity/version reconciliation
→ DataCollection
→ Render
→ Evidence
```

Khi có real-time, graph không còn request-response tuyến tính. Vì vậy **ownership, identity, ordering, backpressure, version skew và lifecycle** trở thành những invariant quan trọng hơn việc nhớ transport API.