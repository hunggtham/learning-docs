# Case xuyên tầng: yêu cầu → lưu trữ → hàng đợi → thất bại → khôi phục

> **Mạch đọc:** Case này đứng sau [Production troubleshooting: từ symptom đến evidence xuyên tầng](./00_production_troubleshooting_and_change_failure_patterns.md). Chapter trước cung cấp phương pháp thu hẹp giả thuyết; chapter này áp dụng phương pháp đó lên một luồng có cả yêu cầu đồng bộ (synchronous request / 동기 요청), giao dịch cơ sở dữ liệu (database transaction / 데이터베이스 트랜잭션), hàng đợi bất đồng bộ (asynchronous queue / 비동기 큐) và bên tiêu thụ (consumer / 소비자). Mục tiêu không phải học một message broker cụ thể mà hiểu failure semantics khi một thao tác đi qua nhiều boundary.

Prerequisite gần nhất là [đường đi của yêu cầu: DNS/TCP/TLS/proxy](../01_runtime_foundations/01_network_dns_tls_and_request_path.md), [timeout/retry/idempotency của Backend](../../10_backend/backend_core/06_timeout_retry_idempotency.md), [observability dựa trên bằng chứng](../07_observability_sre/00_observability_telemetry_and_evidence_driven_debugging.md) và [incident/resilience/recovery](../07_observability_sre/02_incidents_resilience_backup_and_disaster_recovery.md).

Câu hỏi trung tâm: **khi người dùng thấy một request thất bại, điều gì thực sự đã thất bại?** Request có thể timeout trong khi database đã commit; database có thể commit nhưng event chưa được publish; broker có thể giao message hai lần; consumer có thể hoàn thành side effect rồi crash trước khi acknowledge; recovery có thể làm backlog tạo một đợt tải còn lớn hơn incident ban đầu. Vì vậy `HTTP 500`, `timeout` hay `queue lag` chỉ là symptom, không phải trạng thái nghiệp vụ cuối cùng.

## 1. Hệ thống mẫu và bất biến cần giữ

Ta dùng một flow đặt hàng tối giản:

```text
Client
  ↓ HTTP request
API service
  ↓ transaction
Database
  ↓ event handoff
Message broker / queue
  ↓ delivery
Worker / consumer
  ↓ side effect
External provider
```

Ví dụ nghiệp vụ: client gửi yêu cầu tạo đơn hàng. API xác thực dữ liệu, tạo bản ghi `order`, sau đó một worker xử lý tác vụ tiếp theo như gửi email, cập nhật kho hoặc gọi nhà cung cấp.

Trước khi debug failure, cần định nghĩa **bất biến (invariant / 불변식)**. Với flow này, một tập bất biến hợp lý có thể là:

- mỗi `order_id` đại diện đúng một ý định nghiệp vụ;
- retry của cùng ý định không tạo hai đơn hàng độc lập;
- nếu trạng thái database nói một tác vụ cần được xử lý, tác vụ đó cuối cùng phải có đường tới hàng đợi hoặc cơ chế reconciliation;
- consumer xử lý lặp cùng message không được nhân đôi side effect không mong muốn;
- recovery phải hội tụ về trạng thái nhất quán thay vì chỉ làm metric chuyển sang xanh.

Nếu chưa viết được bất biến, troubleshooting dễ rơi vào “service nào đỏ thì restart service đó”. Nhưng restart chỉ tác động tiến trình; nó không trả lời dữ liệu đã commit hay side effect đã xảy ra chưa.

> **Chuyển mạch:** Sau khi biết trạng thái đúng cần giữ, ta có thể đi theo timeline và đánh dấu nơi nào hệ thống mất khả năng biết chắc kết quả.

## 2. Một request thành công bình thường đi qua nhiều điểm commit khác nhau

Một flow thành công có thể trông như sau:

```text
T0  client gửi POST /orders với idempotency key
T1  API nhận request
T2  API acquire database connection
T3  transaction ghi order
T4  database COMMIT
T5  event/outbox state trở nên durable
T6  API trả HTTP response
T7  publisher đưa event lên queue
T8  broker lưu / giao message
T9  consumer nhận message
T10 consumer gọi external provider
T11 consumer ghi trạng thái kết quả
T12 consumer ACK message
```

Điểm khó là `T4`, `T6`, `T8`, `T11` và `T12` không phải một atomic boundary duy nhất. Mỗi điểm có thể thành công trong khi điểm kế tiếp thất bại. Vì vậy “request thất bại” không đủ để suy ra “operation chưa xảy ra”.

Mental model quan trọng:

```text
transport outcome ≠ business outcome
process outcome   ≠ durable-state outcome
queue ACK outcome ≠ side-effect outcome
```

Từ đây, mỗi failure mode phải trả lời hai câu: **trạng thái durable cuối cùng là gì** và **caller/consumer biết được bao nhiêu về trạng thái đó**.

## 3. Failure mode A — timeout trước khi lấy được database connection

Giả sử traffic tăng mạnh. Pool có 100 connection, mọi connection đều bận; request mới chờ ở connection pool. Sau 2 giây, request timeout trước khi transaction bắt đầu.

Symptom có thể là:

```text
HTTP latency ↑
DB query latency ≈ bình thường
connection-pool wait ↑
in-flight requests ↑
timeout ↑
```

Nếu chỉ nhìn database query latency, team có thể kết luận sai rằng database khỏe. Thực tế bottleneck nằm **trước query execution**, ở chờ liên kết (connection-pool wait / 커넥션 풀 대기).

Nếu client hoặc gateway retry ngay, lượng request mới tăng trong khi tài nguyên không tăng. Retry biến một vấn đề sức chứa thành **khuếch đại tải (load amplification / 부하 증폭)**. Đây là lý do timeout, retry và concurrency budget phải được xem như một hệ thống.

Bằng chứng cần thu gồm pool utilization, pool wait histogram, request concurrency, database active sessions và tỷ lệ retry. Recovery hợp lý có thể là giảm intake, shed tải ít quan trọng hoặc sửa query/transaction giữ connection quá lâu; tăng pool mù quáng có thể chuyển bottleneck sang database max connections.

> **Bàn giao:** Failure A tương đối dễ vì transaction chưa bắt đầu. Failure tiếp theo khó hơn: database đã commit nhưng client không nhận được câu trả lời.

## 4. Failure mode B — database commit thành công nhưng HTTP response bị mất

Timeline:

```text
T3 transaction ghi order
T4 COMMIT thành công
T5 process chuẩn bị response
T6 network connection reset / gateway timeout
```

Client thấy timeout và không biết request đã thành công hay chưa. Đây là **kết quả không xác định đối với caller (unknown outcome / 호출자 관점 결과 불명)**, không phải chắc chắn thất bại.

Nếu client gửi lại một `POST /orders` hoàn toàn mới mà không có idempotency, hệ thống có thể tạo order thứ hai. Nếu thao tác có khóa idempotency (idempotency key / 멱등성 키) gắn với cùng principal/tenant và cùng payload fingerprint, server có thể trả lại kết quả của operation cũ thay vì tạo side effect mới.

Điểm quan trọng là timeout không hủy ngược một database commit đã xảy ra. **Hủy (cancellation / 취소)** và **quay lui giao dịch (transaction rollback / 트랜잭션 롤백)** chỉ có hiệu lực nếu chúng tới đúng boundary trước commit. Sau commit, caller phải chuyển sang query status/reconciliation, không giả định rollback.

Evidence tốt gồm request ID, idempotency key, transaction/order ID, commit timestamp và status query. Log “response failed” mà không có durable operation ID sẽ làm incident investigation khó hơn rất nhiều.

## 5. Failure mode C — database commit nhưng event publish thất bại

Một anti-pattern phổ biến:

```text
BEGIN TRANSACTION
  INSERT order
COMMIT
publish OrderCreated
```

Nếu process crash giữa `COMMIT` và `publish`, database nói order tồn tại nhưng queue không có event. Nếu đảo thứ tự — publish trước rồi commit — consumer có thể nhận event cho dữ liệu cuối cùng rollback. Đây là **bài toán dual-write (dual-write problem / 이중 쓰기 문제)**: hai hệ thống durable không chia sẻ một transaction atomic đơn giản.

Một cách xử lý phổ biến là **transactional outbox (트랜잭셔널 아웃박스)**:

```text
BEGIN TRANSACTION
  INSERT order
  INSERT outbox_event
COMMIT

separate publisher:
  read unsent outbox rows
  publish to broker
  mark / advance delivery state
```

Order và intent-to-publish cùng commit trong database. Publisher có thể retry việc publish. Cơ chế này không biến broker và database thành exactly-once toàn cục; nó biến trạng thái “cần publish” thành durable và có thể reconciliation.

Bất biến trở thành:

```text
committed business state
→ durable event intent exists
→ publisher retries until handed off or explicitly quarantined
```

Observability cần đo outbox age/backlog, không chỉ broker queue depth. Nếu broker hoàn toàn trống vì publisher chết, queue depth có thể trông “healthy” trong khi event đang kẹt ở database.

## 6. Failure mode D — broker giao message nhiều hơn một lần

Nhiều hệ thống queue thực tế cung cấp ngữ nghĩa **ít nhất một lần (at-least-once / 최소 한 번)**: message có thể được giao lại nếu consumer xử lý xong nhưng ACK bị mất, consumer crash trước ACK hoặc broker không chắc delivery trước đã hoàn thành.

Timeline điển hình:

```text
consumer receives message M
→ calls external provider successfully
→ process crashes
→ ACK never reaches broker
→ broker redelivers M
```

Nếu consumer gọi provider lần nữa, side effect bị nhân đôi. Vì vậy idempotency phải đi **end-to-end**, không chỉ ở HTTP endpoint.

Các chiến lược tùy boundary gồm:

- dùng operation key ổn định khi gọi provider nếu provider hỗ trợ idempotency;
- lưu processed-message/business-operation state với unique constraint;
- thiết kế state transition như `pending → completed` để lặp lại không tạo outcome thứ hai;
- khi không thể làm side effect idempotent, dùng reconciliation/compensation có chủ đích thay vì giả định queue exactly-once.

“Exactly once” ở một thành phần không tự đảm bảo exactly-once của toàn workflow. Một broker có thể deduplicate delivery nhưng external API bên ngoài broker vẫn có failure boundary riêng.

## 7. Failure mode E — poison message và retry vô hạn

Một message có payload hợp lệ về schema nhưng kích hoạt bug deterministic ở consumer. Nếu mọi failure đều retry với backoff vô hạn, message đó có thể giữ tài nguyên, làm queue lag tăng và che khuất traffic khỏe.

Cần phân biệt:

- **lỗi tạm thời (transient failure / 일시적 실패):** dependency timeout, rate limit, temporary unavailable;
- **lỗi vĩnh viễn hoặc deterministic (permanent/deterministic failure / 영구적·결정적 실패):** invalid business state, unsupported version, bug luôn tái hiện với cùng input.

Retry policy phải có classification, attempt budget và đường sang **hàng đợi thư chết (dead-letter queue / 데드 레터 큐)** hoặc quarantine. Nhưng DLQ không phải bãi rác cuối cùng. Nó cần owner, alert, inspect tooling, replay policy và khả năng đảm bảo replay vẫn idempotent.

Một queue có depth ổn định nhưng DLQ tăng đều vẫn là system failure. Vì vậy operational contract phải bao phủ cả main path và exception path.

## 8. Failure mode F — recovery tạo recovery storm

Giả sử broker hoặc downstream provider down 40 phút. Trong thời gian đó producer vẫn ghi outbox và backlog tích tụ. Khi dependency phục hồi, hàng nghìn worker cùng bắt đầu drain backlog nhanh nhất có thể.

Nếu steady-state arrival rate là 1.000 jobs/phút nhưng recovery chạy 8.000 jobs/phút, database/provider có thể bị quá tải, latency tăng, timeout xuất hiện, retry tăng và dependency lại sập. Hệ thống rơi vào **bão khôi phục (recovery storm / 복구 폭주)**.

Recovery không phải “mở toàn bộ van”. Cần điều khiển tốc độ drain:

```text
new traffic budget
+ backlog recovery budget
< safe downstream capacity
```

Có thể dùng concurrency limit, token bucket/rate limit, tenant priority hoặc staged replay. Theo dõi **tuổi message (message age / 메시지 지연 시간)** cùng queue depth: depth giảm nhưng oldest message vẫn già có thể nghĩa fairness/order policy đang khiến một subset bị starve.

Exit criterion của recovery nên là trạng thái hội tụ: backlog về mức bình thường, error rate ổn định, downstream không còn saturation, reconciliation không còn discrepancy và business outcome được kiểm tra. Dashboard xanh ngay sau restart chưa đủ.

## 9. Một failure graph giúp tránh debug theo tên service

Thay vì vẽ kiến trúc như danh sách box, hãy vẽ **đồ thị thất bại (failure graph / 실패 그래프)** với boundary và observable evidence:

```text
client
  │ timeout / retry
  ▼
gateway
  │ request ID, deadline
  ▼
API process
  │ pool wait / concurrency
  ▼
database
  │ commit / rollback / lock / durable state
  ├──────────────┐
  ▼              │
outbox            │ business query
  │ age/backlog  │
  ▼              │
publisher         │
  │ publish ack  │
  ▼              │
broker            │
  │ delivery attempt / lag
  ▼              │
consumer          │
  │ operation key
  ▼              │
external provider
  │ side-effect status
  └──────────────┘ reconciliation
```

Khi incident xảy ra, tìm boundary đầu tiên nơi expected state khác actual state. Không cần mở mọi dashboard cùng lúc.

## 10. Evidence contract: cần correlation xuyên tầng

Một trace ID duy nhất hữu ích nhưng chưa đủ nếu operation sống lâu hơn request ban đầu. Nên phân biệt một số định danh:

```text
request_id       = một transport attempt
operation_id     = một ý định nghiệp vụ
idempotency_key  = khóa nhận diện retry cùng intent
message_id       = một envelope/delivery identity
trace_id         = một causal trace context
```

Một retry HTTP có `request_id` mới nhưng có thể giữ cùng `operation_id` và `idempotency_key`. Một message redelivery có thể giữ cùng business operation nhưng attempt number tăng. Nếu ép tất cả vào một ID, investigation dễ nhầm transport attempt với business intent.

Telemetry nên trả lời được:

- request nào tạo operation nào;
- operation durable state hiện ở đâu;
- outbox event tương ứng đã publish chưa;
- message đã được delivery bao nhiêu lần;
- consumer side effect có operation key nào;
- recovery/replay nào đã tác động lên record.

Mục tiêu không phải log thật nhiều mà là có đủ bằng chứng để dựng lại state transition.

## 11. Runbook reasoning: symptom → hypothesis → evidence → action

Giả sử người dùng báo “đặt hàng bị timeout nhưng sau đó nhận hai email”. Một runbook reasoning tốt không bắt đầu bằng restart.

### Bước 1 — xác định business outcome

Tìm `operation_id`/idempotency key và số order durable. Nếu có một order nhưng hai email, duplication xảy ra sau business commit. Nếu có hai order, duplication có thể bắt đầu từ HTTP retry/idempotency boundary.

### Bước 2 — dựng timeline

So sánh commit timestamp, response failure, outbox publish, message delivery attempts và provider calls. Tìm điểm đầu tiên tạo hai branch hành vi.

### Bước 3 — xác minh retry ownership

Client, gateway, service, publisher và consumer có thể đều retry. Vẽ retry topology để xem amplification. Một operation không nên bị retry mù ở mọi layer.

### Bước 4 — chọn mitigation có expected effect

Nếu lỗi là consumer duplicate, pause/reduce consumer hoặc bật idempotency guard có thể phù hợp hơn rollback deployment toàn API. Nếu lỗi là pool saturation, restart consumer không giải quyết queueing ở API.

### Bước 5 — preserve evidence trước mutation khi có thể

Chụp relevant logs, queue offsets/delivery metadata, outbox records và database state trước mass replay/delete/restart. Hành động recovery có thể xóa dấu vết của failure ban đầu.

## 12. Recovery correctness quan trọng hơn recovery speed đơn thuần

Một hệ thống “phục hồi” về latency nhưng để lại missing event, duplicate side effect hoặc orphan record vẫn chưa thực sự phục hồi.

Recovery cần ba lớp:

**Khôi phục dịch vụ (service recovery / 서비스 복구).** Request mới hoạt động và dependency reachable.

**Khôi phục dữ liệu (data recovery / 데이터 복구).** Durable state giữa database, outbox, broker và consumer converges; discrepancy được reconcile.

**Khôi phục nghiệp vụ (business recovery / 비즈니스 복구).** User-visible outcome đúng: không mất order, không charge hai lần, không bỏ sót notification quan trọng.

Thứ tự có thể khác tùy incident nhưng cả ba phải có owner. Đây là lý do incident commander cần tách “mitigation done” khỏi “recovery complete”.

## 13. Khi nào dùng replay, khi nào dùng reconciliation, khi nào dùng compensation

**Replay (재처리)** phù hợp khi cùng operation có thể được xử lý lại an toàn và input/event vẫn đáng tin. Điều kiện tiên quyết là idempotency hoặc state transition bảo vệ side effect.

**Đối soát (reconciliation / 조정)** phù hợp khi hai hệ thống có thể lệch state và ta cần so sánh source of truth với observed state để tạo corrective work. Reconciliation đặc biệt quan trọng sau dual-write partial failure hoặc provider uncertainty.

**Bù trừ (compensation / 보상)** là một operation nghiệp vụ mới nhằm trung hòa hiệu ứng cũ khi không thể rollback vật lý. Refund sau charge là ví dụ điển hình: nó không xóa lịch sử charge mà tạo một state transition mới.

Không nên dùng ba từ này thay nhau. Replay cố thực hiện lại intent cũ; reconciliation phát hiện và sửa divergence; compensation tạo hành động nghiệp vụ đối nghịch/điều chỉnh.

## 14. Capacity phải tính cả đường recovery

Capacity planning chỉ dựa trên steady-state traffic bỏ sót một failure mode lớn. Hệ thống production cần headroom cho retry, failover và backlog drain.

Một mô hình đơn giản:

```text
steady load       = λ
recovery backlog  = B
safe capacity     = C
recovery window   = T

required average drain rate ≈ λ + B/T
```

Nếu `λ + B/T > C`, mục tiêu recovery window không khả thi nếu không tăng capacity, giảm incoming load hoặc kéo dài T. Đây không phải vấn đề “worker chưa đủ nhanh” mà là ràng buộc vật lý của hệ thống.

Case này nối trực tiếp với [SLI/SLO, error budget và capacity](../07_observability_sre/01_sli_slo_error_budget_and_capacity.md): reliability policy phải bao gồm degraded mode và recovery budget, không chỉ peak QPS bình thường.

## 15. Boundary với các canonical owner khác

Chapter này chỉ sở hữu **lập luận xuyên tầng (cross-layer reasoning / 계층 간 추론)**. Cơ chế sâu hơn thuộc các đơn vị khác:

- request lifecycle, transaction boundary, timeout/retry/idempotency: [Backend Core](../../10_backend/backend_core/README.md);
- process, socket, resource pressure và runtime evidence: [Linux](../../linux/README.md);
- database transaction, durability, replication và storage internals: [Computer Science](../../computer_science/README.md);
- pipeline/backfill/replay/data quality ở quy mô dữ liệu: [Data Engineering](../../data_engineering/README.md);
- telemetry, SLO, incident response và DR: [`07_observability_sre`](../07_observability_sre/00_observability_telemetry_and_evidence_driven_debugging.md).

Nếu cần đào sâu một failure, hãy quay về canonical owner thay vì mở rộng case này thành textbook riêng cho database, broker hoặc Linux.

## 16. Checklist reasoning ngắn cho incident tương tự

Khi một request đi qua storage và queue rồi thất bại, hãy lần lượt hỏi:

1. **Ý định nghiệp vụ là gì?** Có stable operation/idempotency identity không?
2. **Điểm durable cuối cùng ở đâu?** Chưa commit, đã commit, đã publish, đã side effect hay đã ACK?
3. **Caller biết gì và durable state thực sự là gì?** Timeout có thể chỉ tạo uncertainty.
4. **Retry nằm ở những layer nào?** Tổng amplification là bao nhiêu?
5. **Có dual-write boundary không?** Nếu có, cơ chế reconcile là gì?
6. **Consumer có chịu duplicate delivery không?** Side effect có idempotent không?
7. **Backlog sẽ phục hồi với tốc độ nào?** Recovery có thể overload downstream không?
8. **Exit criterion là gì?** Metric xanh hay state/business outcome đã hội tụ?

Checklist này là công cụ nén reasoning, không thay thế evidence.

## Kết luận: theo dõi trạng thái nghiệp vụ, không chỉ theo dõi request

Bất biến (invariant / 불변식) quan trọng nhất của case là: **một failure ở transport không xác định business outcome, và một recovery ở process không đảm bảo state đã hội tụ**. Muốn debug đúng, ta phải theo một ý định nghiệp vụ xuyên qua request attempt, database commit, event handoff, message delivery, consumer side effect và reconciliation.

Sau chapter này, quay lại [Production troubleshooting](./00_production_troubleshooting_and_change_failure_patterns.md) với một mental model cụ thể hơn: symptom đầu tiên chỉ là điểm vào. Khi hệ thống có nhiều durable boundary, câu hỏi quyết định luôn là **state nào đã trở thành sự thật, state nào chỉ là quan sát tạm thời, và cơ chế nào sẽ đưa toàn workflow trở lại một trạng thái nhất quán có thể kiểm chứng?**