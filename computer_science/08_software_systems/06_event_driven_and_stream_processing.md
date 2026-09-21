# Event-driven systems và stream processing

Request/response phù hợp khi caller cần kết quả ngay. Nhưng nhiều workflows cần decouple producers và consumers, xử lý dữ liệu liên tục, fan-out hoặc chịu spikes. Event-driven architecture dùng events/messages làm boundary, nhưng đổi call-stack trực tiếp lấy delivery/order/state complexity.

## Event, command và message

Message là envelope transport. Command thường biểu đạt yêu cầu “hãy làm X” với intended handler. Event biểu đạt “X đã xảy ra” và có thể có nhiều subscribers.

Terminology không tuyệt đối giữa frameworks, nhưng distinction intent vs fact hữu ích cho coupling.

## Queue và log

Traditional work queue phân phối messages để worker xử lý, thường mỗi message bởi một consumer trong group.

Append-only distributed log như Kafka giữ ordered records theo partition và consumers track offsets. Multiple consumer groups có thể replay cùng history độc lập.

Queue nhấn mạnh work distribution; log nhấn mạnh durable ordered history/replay.

## At-most-once, at-least-once, effectively-once

At-most-once có thể mất message nhưng không redeliver. At-least-once retry nên có duplicates. Exactly-once end-to-end rất khó vì broker acknowledgment và external side effect không atomic mặc định.

Thực tế thường dùng idempotent consumers, deduplication keys hoặc transactional integration để đạt effectively-once business outcome.

## Ordering chỉ có scope

Global total ordering đắt và hiếm cần. Systems thường guarantee order per partition/key.

Nếu account updates phải ordered, partition theo account ID giúp cùng account vào một ordered stream, trong khi accounts khác xử lý parallel.

Ordering requirement vì vậy ảnh hưởng partitioning và throughput.

## Event time và processing time

Processing time là lúc system xử lý record. Event time là lúc event thực sự xảy ra theo source timestamp.

Late/out-of-order events làm window aggregation khó. Watermark là estimate rằng system đã thấy phần lớn events trước một event-time frontier.

Streaming correctness phải nói rõ lateness policy, window type và update/retraction semantics.

## Backpressure

Producer nhanh hơn consumer vô hạn thời gian thì queue grow vô hạn. Backpressure cần giới hạn/buffering/rate control hoặc drop/degrade policy.

Queue chỉ hấp thụ burst tạm thời; nó không tạo processing capacity.

## Dead-letter queue

Messages retry mãi do malformed data có thể block throughput hoặc waste resources. DLQ tách poison messages để investigate.

Nhưng DLQ không nên là nơi data biến mất vô thời hạn; cần ownership, alerting và replay process.

## Event sourcing

Event sourcing lưu state changes như sequence events và derive current state bằng replay/projection. Nó tạo audit/history mạnh nhưng schema evolution, event immutability và replay cost phức tạp.

Không phải mọi event-driven system đều event-sourced.

## Common Misconceptions

**“Message broker làm system reliable tự động.”** Reliability phụ thuộc producer ack, retention, consumer idempotency, retry và downstream side effects.

**“Exactly-once là checkbox của broker.”** End-to-end effect vượt broker boundary cần additional protocol/state.

**“Queue giải overload.”** Nó trì hoãn overload; sustained arrival rate > service rate vẫn không ổn định.

## Mental Model

> Event-driven design biến temporal coupling thành state in queues/logs. Đổi lại bạn phải explicit delivery, ordering, replay, idempotency và backpressure.

## Kết nối

Đọc [queues/backpressure](./03_state_queues_backpressure_and_boundaries.md), [time/idempotency](./04_time_serialization_and_idempotency.md), [distributed failure](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md) và [reliability](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md).