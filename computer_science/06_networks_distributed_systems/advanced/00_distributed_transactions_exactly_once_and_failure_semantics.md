# Distributed transactions, exactly-once và failure semantics

Trong một process, function có thể return success/failure tương đối rõ. Trong distributed system, timeout tạo trạng thái khó hơn: **operation đã thất bại, hay chỉ response thất lạc?** Đây là nguồn gốc của retry ambiguity, duplicate side effects và nhiều protocol patterns như idempotency key, outbox, 2PC và consensus-backed state machine.

## Timeout không phải evidence của failure

Client gửi request, server commit DB rồi response bị mất. Client thấy timeout nhưng operation đã thành công. Nếu retry một `chargeCard()` không idempotent, khách có thể bị charge hai lần.

Vì vậy distributed API cần phân biệt ít nhất:

```text
known success
known failure
unknown outcome
```

Unknown outcome là trạng thái thật, không nên ép thành boolean chỉ vì application API muốn đơn giản.

## At-most-once, at-least-once và exactly-once

**At-most-once** ưu tiên không duplicate nhưng có thể mất operation. **At-least-once** retry tới khi có ack, chấp nhận duplicate delivery/execution. **Exactly-once** thường chỉ đạt được trong một boundary cụ thể bằng coordination + durable deduplication/state transition; không phải phép màu loại bỏ failure.

Một message broker nói “exactly-once” thường định nghĩa guarantee trong phạm vi producer/broker/consumer state được phối hợp. Khi side effect đi ra hệ thống khác như email, payment gateway hay external API, boundary guarantee thay đổi.

## Idempotency biến retry thành operation an toàn hơn

Operation idempotent nghĩa apply nhiều lần cho cùng logical request cho final state tương đương apply một lần. `SET balance = 100` gần idempotent về state; `balance += 100` không.

API có thể dùng idempotency key. Server lưu key → result/transaction identity trong durable store. Retry với cùng key trả lại prior result hoặc tiếp tục state machine thay vì tạo side effect mới.

Nhưng deduplication cần retention policy. Nếu key bị expire quá sớm, retry muộn có thể trở thành duplicate thật.

## Two-Phase Commit giải atomicity giữa participants

2PC có coordinator và participants. Phase prepare hỏi mỗi participant có thể commit không; nếu tất cả prepared, coordinator quyết định commit, nếu không abort.

Prepared participant thường đã giữ locks/resources và ghi durable intent. Nếu coordinator chết sau prepare, participant có thể bị **in-doubt**: nó không được tự đoán commit hay abort nếu điều đó phá atomicity.

2PC vì vậy cung cấp atomic decision nhưng có blocking/failure-management cost. Consensus có thể dùng để replicate coordinator/decision state, nhưng 2PC và consensus giải câu hỏi khác nhau: atomic commit giữa resource managers vs agreement trong replicated state machine.

## Saga đổi atomicity mạnh lấy compensating workflow

Trong microservices, giữ distributed lock/transaction lâu thường không phù hợp. Saga chia workflow thành local transactions và compensating actions.

Ví dụ booking: reserve flight → reserve hotel → charge payment. Nếu hotel fail, compensation có thể release flight. Nhưng compensation không phải time travel. Email đã gửi không “unsend”, giá thị trường có thể đổi, external side effect có thể không reversible.

Do đó saga correctness cần business semantics, không chỉ technical retry.

## Transactional outbox giải dual-write cục bộ

Một service cần update DB rồi publish event. Nếu làm hai operations độc lập, crash giữa chúng tạo inconsistency.

Outbox pattern ghi business state + outbox row trong cùng local DB transaction. Worker/CDC sau đó publish outbox event, có thể retry. Consumer phải xử lý duplicate bằng idempotency/deduplication.

Outbox không tạo exactly-once toàn cầu; nó biến “DB update và intent-to-publish” thành atomic trong một local boundary.

## Fencing chống stale actor

Lease-holder cũ có thể bị pause, lease expire, actor mới nhận quyền, rồi actor cũ thức dậy và tiếp tục write. Chỉ “có lock token” chưa đủ nếu stale token vẫn được resource chấp nhận.

Fencing token tăng đơn điệu; storage/resource từ chối request có token nhỏ hơn token mới nhất đã thấy. Đây là pattern quan trọng khi correctness phụ thuộc ownership qua network/GC pause/process freeze.

## Mental Model

> Distributed correctness bắt đầu từ **uncertain outcome**. Retry tạo duplicate risk; idempotency/dedup thuần hóa retry; 2PC phối hợp atomic decision; saga phối hợp business compensation; outbox nối local transaction với messaging; fencing ngăn owner cũ quay lại phá state.

## Kết nối

Foundation: [time/failure/consistency](../../basic/06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md), [replication/consensus](../../basic/06_networks_distributed_systems/05_replication_partitioning_and_consensus.md), [idempotency](../../basic/08_software_systems/04_time_serialization_and_idempotency.md) và [event-driven systems](../../basic/08_software_systems/06_event_driven_and_stream_processing.md).