# Case xuyên tầng: yêu cầu → lưu trữ → hàng đợi → thất bại → khôi phục

> **Mạch đọc:** Case này đứng sau [Production troubleshooting: từ triệu chứng tới bằng chứng xuyên tầng](./00_production_troubleshooting_and_change_failure_patterns.md). Chapter trước dạy cách thu hẹp giả thuyết; chapter này áp dụng phương pháp đó lên một luồng có yêu cầu đồng bộ, giao dịch cơ sở dữ liệu, hàng đợi bất đồng bộ và tác động bên ngoài. Mục tiêu không phải học một message broker cụ thể mà hiểu **ngữ nghĩa thất bại (failure semantics / 실패 의미론)** khi một thao tác đi qua nhiều ranh giới.

Prerequisite gần nhất là [đường đi của yêu cầu: DNS/TCP/TLS/proxy](../01_runtime_foundations/01_network_dns_tls_and_request_path.md), [timeout/retry/idempotency của Backend](../../10_backend/backend_core/06_timeout_retry_idempotency.md), [observability dựa trên bằng chứng](../07_observability_sre/00_observability_telemetry_and_evidence_driven_debugging.md) và [incident/resilience/recovery](../07_observability_sre/02_incidents_resilience_backup_and_disaster_recovery.md).

Câu hỏi trung tâm: **khi người dùng thấy một request thất bại, điều gì thực sự đã thất bại?** Request có thể timeout trong khi database đã commit; database có thể commit nhưng event chưa được publish; queue có thể giao message hai lần; worker có thể hoàn thành side effect rồi crash trước ACK. Vì vậy HTTP 500, timeout hoặc queue lag chỉ là triệu chứng, không phải trạng thái nghiệp vụ cuối cùng.

## 1. Hệ thống mẫu và các bất biến

Ta dùng luồng tạo đơn hàng:

```text
Client
  ↓ HTTP request
API service
  ↓ database transaction
Database
  ↓ outbox / event handoff
Message broker / queue
  ↓ delivery
Worker / consumer
  ↓ side effect
External provider
```

Các **bất biến (invariant / 불변식)** cần giữ:

```text
mỗi order_id đại diện một ý định nghiệp vụ
retry cùng ý định không tạo đơn hàng độc lập thứ hai
state cần xử lý cuối cùng phải có đường tới queue hoặc reconciliation
xử lý lặp message không được nhân đôi side effect ngoài ý muốn
recovery phải hội tụ về state đúng, không chỉ làm metric xanh lại
```

Nếu chưa định nghĩa invariant, troubleshooting dễ biến thành “service đỏ thì restart”. Restart chỉ đổi trạng thái process; nó không nói dữ liệu đã commit hay side effect đã xảy ra chưa.

## 2. Một request thành công có nhiều điểm cam kết độc lập

Timeline đơn giản:

```text
T0  client gửi POST /orders với idempotency key
T1  API nhận request
T2  API lấy database connection
T3  transaction ghi order
T4  database COMMIT
T5  outbox/event state trở nên durable
T6  API trả response
T7  publisher đưa event lên queue
T8  broker lưu/giao message
T9  consumer nhận message
T10 consumer gọi external provider
T11 consumer ghi kết quả
T12 consumer ACK message
```

`T4`, `T6`, `T8`, `T11`, `T12` không phải một atomic boundary.

Cần giữ ba phân biệt:

```text
kết quả vận chuyển ≠ kết quả nghiệp vụ
kết quả process ≠ trạng thái bền
ACK của queue ≠ kết quả side effect
```

## 3. Failure A — timeout trước khi có database connection

Traffic tăng, connection pool đầy, request chờ rồi timeout trước khi transaction bắt đầu.

Bằng chứng có thể là:

```text
HTTP latency tăng
DB query latency vẫn bình thường
connection-pool wait tăng
in-flight request tăng
timeout tăng
```

Nếu chỉ nhìn query latency, team có thể kết luận database khỏe nhưng bỏ qua bottleneck ở pool.

Nếu gateway/client retry ngay, tải mới lại tăng. **Khuếch đại do thử lại (retry amplification / 재시도 증폭)** biến thiếu sức chứa thành incident lớn hơn.

## 4. Failure B — database đã commit nhưng client không nhận response

Timeline:

```text
DB COMMIT thành công
→ response bị mất / connection đóng / timeout
→ client không biết outcome
```

Đây là **kết quả không xác định với caller (unknown outcome / 호출자 관점 결과 불명)**.

Nếu client retry và API không có **khóa lũy đẳng (idempotency key / 멱등성 키)**, cùng ý định có thể tạo hai order.

Timeout không rollback transaction đã commit. Vì vậy handler phải thiết kế cho trường hợp “caller không biết nhưng server đã làm”.

## 5. Idempotency bảo vệ ý định nghiệp vụ

Idempotency không có nghĩa mọi request giống nhau đều trả cùng response mãi mãi. Nó nghĩa nhiều lần thực hiện **cùng một ý định logic** không tạo side effect lặp ngoài mong muốn.

Một thiết kế phổ biến:

```text
idempotency_key + caller/tenant
→ lookup operation
→ nếu chưa có: tạo operation và thực hiện
→ nếu đang xử lý: trả trạng thái phù hợp
→ nếu đã hoàn tất: trả outcome đã lưu
```

Khóa cần có scope rõ; nếu global quá rộng có thể va chạm, nếu scope quá hẹp có thể không chặn duplicate thật.

## 6. Failure C — database commit nhưng event publish thất bại

Nếu application làm:

```text
1. COMMIT order
2. publish event
```

thì publish có thể thất bại sau commit. Đây là **bài toán ghi kép (dual-write problem / 이중 쓰기 문제)**.

Retry toàn request không an toàn nếu bước 1 đã thành công. Chỉ retry publish cũng cần biết event identity.

## 7. Transactional outbox nối commit với việc phát sự kiện

**Mẫu outbox giao dịch (transactional outbox / 트랜잭셔널 아웃박스)** ghi business state và outbox record trong cùng database transaction:

```text
BEGIN
→ insert/update business state
→ insert outbox event
→ COMMIT
```

Sau đó publisher đọc outbox và gửi event.

Outbox không tạo exactly-once end-to-end. Nó chuyển bài toán từ “mất event sau commit” sang “publisher/consumer phải idempotent khi delivery lặp”.

## 8. At-least-once delivery nghĩa là duplicate là trạng thái bình thường

Nhiều broker cung cấp **giao ít nhất một lần (at-least-once delivery / 최소 1회 전달)**: message có thể đến nhiều hơn một lần.

Consumer phải giả định:

```text
message đã xử lý nhưng ACK bị mất
→ broker giao lại
```

Nếu side effect là gửi email, charge payment hoặc gọi provider không idempotent, duplicate delivery có thể tạo hậu quả thật.

## 9. Failure D — side effect thành công nhưng consumer crash trước khi ghi state

Timeline:

```text
consumer gọi provider
provider xử lý thành công
consumer crash
local result chưa ghi
ACK chưa gửi
message được giao lại
```

Lúc này consumer không biết provider đã làm chưa.

Cần một trong các cơ chế:

- provider hỗ trợ idempotency key;
- query/reconciliation được trạng thái provider;
- local operation record có state machine đủ rõ;
- compensation nếu action có thể đảo ngược.

## 10. Retry, replay, reconciliation, compensation, restore và rollback khác nhau

Các từ này không thay thế nhau:

- **thử lại (retry / 재시도):** thực hiện lại một operation vì tin rằng nó chưa thành công hoặc an toàn khi lặp;
- **phát lại (replay / 재생):** chạy lại event/message lịch sử qua processor;
- **đối soát (reconciliation / 대조):** so hai nguồn trạng thái và sửa chênh lệch;
- **bù trừ (compensation / 보상):** thực hiện action mới để đảo/giảm tác động nghiệp vụ trước đó;
- **khôi phục dữ liệu (restore / 복원):** phục hồi từ backup/snapshot;
- **quay lui phiên bản (rollback / 롤백):** đưa code/config về version trước.

Chọn sai từ thường dẫn tới chọn sai cơ chế recovery.

## 11. Poison message cần cô lập, không retry vô hạn

Một **message độc (poison message / 독성 메시지)** có thể luôn fail vì dữ liệu sai schema, bug deterministic hoặc dependency không hỗ trợ input đó.

Retry vô hạn gây:

```text
CPU/network waste
queue lag tăng
log noise
delay cho message hợp lệ
```

Cần giới hạn retry và có **hàng đợi thư chết (dead-letter queue, DLQ / 데드레터 큐)** hoặc cơ chế quarantine tương đương.

DLQ không phải nơi “vứt lỗi”; nó cần owner, reason, replay policy và evidence.

## 12. Queue lag là triệu chứng, phải tách arrival rate và service rate

Backlog tăng khi:

```text
arrival rate > effective service rate
```

Nguyên nhân có thể là traffic tăng, consumer chậm, external provider chậm, retry storm hoặc poison message.

Chỉ tăng số worker có thể làm downstream quá tải hơn nếu bottleneck nằm ở database/provider.

Cần đo:

```text
queue depth
oldest message age
arrival rate
processing rate
retry rate
consumer saturation
downstream latency/error
```

## 13. Recovery storm có thể tạo incident thứ hai

Khi dependency phục hồi, backlog lớn có thể được xử lý đồng loạt:

```text
provider phục hồi
→ worker tăng throughput
→ DB/provider bị dồn tải
→ latency tăng
→ timeout/retry tăng
→ dependency lại suy yếu
```

Đây là **bão phục hồi (recovery storm / 복구 폭주)**.

Recovery plan cần rate limit, staged drain hoặc adaptive concurrency, không chỉ “mở toàn bộ consumer”.

## 14. Correlation ID và operation ID có vai trò khác nhau

**Mã tương quan (correlation ID / 상관 ID)** nối telemetry qua service.

**Mã thao tác (operation ID / 작업 ID)** hoặc idempotency key đại diện ý định nghiệp vụ.

**Message ID** đại diện delivery/event instance.

Nếu dùng một ID cho mọi vai trò, trace có thể đẹp nhưng khó xác định duplicate nghiệp vụ hay duplicate delivery.

## 15. Một runbook tốt bắt đầu bằng câu hỏi trạng thái

Khi user báo “đặt hàng bị lỗi”, đừng bắt đầu bằng restart.

Runbook nên hỏi:

```text
operation ID là gì?
request đã tới API chưa?
transaction có commit không?
outbox có record không?
event đã publish chưa?
queue đã giao chưa?
consumer đã xử lý chưa?
external provider đã làm chưa?
final business state đang là gì?
```

Mỗi câu thu hẹp failure domain.

## 16. Evidence cần gắn với boundary

Ví dụ:

```text
API → request log/trace + operation ID
DB → transaction state / row / commit evidence
outbox → event record + publish status
queue → offset/delivery/age
consumer → processing state + retry count
provider → idempotency/status API
```

Metric tổng như CPU 80% không đủ chứng minh operation cụ thể đã ở trạng thái nào.

## 17. Capacity phải tính cả trạng thái recovery

Hệ thống không chỉ cần chịu traffic bình thường mà còn phải chịu:

```text
normal traffic
+ retry traffic
+ backlog drain
+ reconciliation jobs
+ deployment/recovery overhead
```

Nếu capacity plan chỉ dựa trên steady state, incident nhỏ có thể tạo backlog mà hệ thống mất nhiều giờ để hấp thụ.

## 18. Đối soát là lớp bảo hiểm cho distributed state

Ngay cả khi thiết kế idempotency/outbox tốt, hệ thống vẫn nên có **đối soát (reconciliation / 대조)** cho state quan trọng.

Ví dụ định kỳ so:

```text
order ở trạng thái paid
↔ provider payment status
↔ downstream fulfillment state
```

Reconciliation không thay correctness. Nó là cơ chế phát hiện/sửa divergence còn sót lại do failure bất thường.

## 19. Recovery hoàn tất khi bất biến được khôi phục

Service process chạy lại chưa đủ.

Cần xác minh:

```text
new request hoạt động
backlog đang giảm có kiểm soát
duplicate không tăng
outbox không bị kẹt
provider state đã reconcile
business invariant được giữ
SLO/latency trở về vùng an toàn
```

Đây là khác biệt giữa “hệ thống xanh” và “nghiệp vụ đã phục hồi”.

## 20. Mô hình tổng hợp

```text
ý định nghiệp vụ
→ idempotency boundary
→ transaction + durable state
→ outbox/event handoff
→ at-least-once delivery
→ idempotent/reconcilable consumer
→ external side effect
→ evidence ở từng boundary
→ retry / replay / reconciliation / compensation
→ controlled recovery
```

Điểm quan trọng nhất: **failure xuyên nhiều lớp tạo trạng thái không chắc chắn; recovery tốt phải dựa trên bằng chứng về trạng thái đã bền và side effect đã thực sự xảy ra hay chưa.**

## 21. Bàn giao

Khi cần hiểu sâu application contract, đọc [Backend Core](../../10_backend/backend_core/README.md). Khi cần database transaction/WAL, đọc [Computer Science Databases](../../computer_science/05_data_databases/README.md). Khi cần host/resource evidence, đọc [Linux](../../linux/README.md). Khi cần incident/SLO/DR, quay lại [DevOps Observability & SRE](../07_observability_sre/README.md).

> **Bàn giao:** Sau case này, người đọc nên có thể vẽ timeline của một operation, đánh dấu **durable boundary → unknown outcome → retry/replay path → evidence → recovery action**, thay vì suy ra business outcome chỉ từ HTTP status hoặc trạng thái process.