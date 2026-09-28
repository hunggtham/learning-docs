# Trạng thái (state / 상태), queues, backpressure và hệ thống (system / 시스템) boundaries

> **Mạch đọc:** Đặt **trạng thái (state / 상태), queues, backpressure và hệ thống (system / 시스템) boundaries** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Why queues exist** sang **Bounded vs unbounded hàng đợi (queue / 큐)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Many môi trường vận hành (production / 운영 환경) các hệ thống (systems / 시스템들) can be understood as producers, queues/buffers and consumers moving trạng thái (state / 상태)/events across boundaries. hàng đợi (queue / 큐) smooths bursts and decouples rates, but it does not create sức chứa (capacity / 용량). Without backpressure or tải (load / 로드) shedding, overload only moves into bộ nhớ (memory / 메모리)/độ trễ (latency / 지연 시간).

## Why queues exist

Producer may create công việc (work / 작업) faster temporarily than bên tiêu thụ (consumer / 소비자) processes. hàng đợi (queue / 큐) stores temporal difference. It also decouples availability: producer can enqueue while downstream temporarily unavailable if broker durable enough.

But for sustained arrival `λ > μ` dịch vụ (service / 서비스) tỷ lệ (rate / 비율), hàng đợi (queue / 큐) grows without bound. Stable hệ thống (system / 시스템) requires long-term dịch vụ (service / 서비스) sức chứa (capacity / 용량) exceed admitted tải (load / 로드) or rejection/degradation.


> **Chuyển mạch:** Từ **Why queues exist**, ta sang **Bounded vs unbounded hàng đợi (queue / 큐)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bounded vs unbounded hàng đợi (queue / 큐)

Unbounded hàng đợi (queue / 큐) converts overload into ever-growing độ trễ (latency / 지연 시간) and eventually bộ nhớ (memory / 메모리)/disk exhaustion. Bounded hàng đợi (queue / 큐) forces tường minh (explicit / 명시적) chính sách (policy / 정책): khối (block / 블록) producer, reject new, drop oldest/newest, prioritize or spill elsewhere.

Choice is nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론): dropping metrics may be acceptable; dropping payment command not.


> **Chuyển mạch:** Từ **Bounded vs unbounded hàng đợi (queue / 큐)**, ta sang **Backpressure** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Backpressure

Backpressure propagates tín hiệu (signal / 신호) upstream that bên tiêu thụ (consumer / 소비자) cannot keep up. TCP receive/congestion windows, Reactive Streams demand, bounded channels and thread-pool queues are forms.

If upstream ignores tín hiệu (signal / 신호) and buffers locally, hệ thống (system / 시스템) has not solved overload. Backpressure must extend through chuỗi (chain / 사슬) or termination chính sách (policy / 정책) apply.


> **Chuyển mạch:** Từ **Backpressure**, ta sang **Messaging ngữ nghĩa (semantics / 의미론)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Messaging ngữ nghĩa (semantics / 의미론)

At-most-once may lose but no thử lại (retry / 재시도) duplicates; at-least-once retries but duplicates possible; exactly-once effects require stronger coordination/deduplication and phạm vi (scope / 범위) definition.

Message broker delivery acknowledgement is not same as nghiệp vụ (business / 비즈니스) giao dịch (transaction / 트랜잭션) completion. bên tiêu thụ (consumer / 소비자) may lần ghi nhận (commit / 커밋) DB then crash before ack → redelivery; idempotent handler/outbox/inbox patterns handle.


> **Chuyển mạch:** Từ **Messaging ngữ nghĩa (semantics / 의미론)**, ta sang **thứ tự (ordering / 순서)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Thứ tự (ordering / 순서)

Toàn cục (global / 전역) total thứ tự (order / 순서) expensive and often unnecessary. Partitioned logs provide thứ tự (order / 순서) within partition/key. If nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) requires per-account thứ tự (order / 순서), partition by account may suffice.

Tính đồng thời (concurrency / 동시성) can reorder completion even if dequeue thứ tự (order / 순서) fixed. thứ tự (ordering / 순서) đặc tả hợp đồng (contract / 계약) must specify enqueue, delivery, processing or lần ghi nhận (commit / 커밋) thứ tự (order / 순서).


> **Chuyển mạch:** Từ **thứ tự (ordering / 순서)**, ta sang **trạng thái (state / 상태) placement** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Trạng thái (state / 상태) placement

Trạng thái (state / 상태) can live máy khách (client / 클라이언트), ứng dụng (application / 애플리케이션) bộ nhớ (memory / 메모리), bộ nhớ đệm (cache / 캐시), cơ sở dữ liệu (database / 데이터베이스), log or bên ngoài (external / 외부) dịch vụ (service / 서비스). Placement affects availability, scaling and khôi phục (recovery / 복구). cục bộ (local / 로컬) in-memory session makes horizontal scaling need sticky routing/replication; bên ngoài (external / 외부) session store adds mạng (network / 네트워크) phụ thuộc (dependency / 의존성).

“Stateless dịch vụ (service / 서비스)” usually means durable/người dùng (user / 사용자) session trạng thái (state / 상태) externalized, not literally no temporary trạng thái (state / 상태).


> **Chuyển mạch:** Từ **trạng thái (state / 상태) placement**, ta sang **sự kiện (event / 이벤트) log and trạng thái (state / 상태)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Sự kiện (event / 이벤트) log and trạng thái (state / 상태)

Event-sourcing stores chuỗi (sequence / 시퀀스) of lĩnh vực (domain / 도메인) events as nguồn (source / 소스); trạng thái hiện tại (current state / 현재 상태) derived by replay/folding. It enables lịch sử (history / 이력)/kiểm tra (audit / 감사) but lược đồ (schema / 스키마) evolution, replay chi phí (cost / 비용), sự kiện (event / 이벤트) tính đúng đắn (correctness / 정확성) and bên ngoài (external / 외부) side effects complex. Not every hệ thống (system / 시스템) needs it.

Thay đổi (change / 변경) dữ liệu (data / 데이터) Capture streams cơ sở dữ liệu (database / 데이터베이스) changes to downstream indexes/analytics; consistency lag must be accepted/monitored.


> **Chuyển mạch:** Từ **sự kiện (event / 이벤트) log and trạng thái (state / 상태)**, ta sang **Backpressure vs tỷ lệ (rate / 비율) limiting** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Backpressure vs tỷ lệ (rate / 비율) limiting

Tỷ lệ (rate / 비율) limiter protects ranh giới (boundary / 경계) by limiting admitted yêu cầu (request / 요청) tỷ lệ (rate / 비율) per định danh (identity / 식별자)/hệ thống (system / 시스템). Backpressure is động (dynamic / 동적) downstream pressure. Both may coexist: limiter prevents abuse/overload; backpressure reacts hiện tại (current / 현재) sức chứa (capacity / 용량).


> **Chuyển mạch:** Từ **Backpressure vs tỷ lệ (rate / 비율) limiting**, ta sang **Queueing and thử lại (retry / 재시도) storms** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Queueing and thử lại (retry / 재시도) storms

If phụ thuộc (dependency / 의존성) slows, queues grow; hết thời gian chờ (timeout / 타임아웃) triggers retries; retries increase arrival tỷ lệ (rate / 비율); overload worsens. Circuit breaker, thử lại (retry / 재시도) ngân sách (budget / 예산), bounded queues and deadlines break vòng phản hồi (feedback loop / 피드백 루프).


> **Chuyển mạch:** Từ **Queueing and thử lại (retry / 재시도) storms**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> hàng đợi (queue / 큐) is **stored waiting thời gian (time / 시간)**. It absorbs burst, not sustained sức chứa (capacity / 용량) deficit. Every hàng đợi (queue / 큐) should have sức chứa (capacity / 용량), admission chính sách (policy / 정책), thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론), thứ tự (ordering / 순서) phạm vi (scope / 범위) and khả năng quan sát (observability / 관측 가능성).


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Async hàng đợi (queue / 큐) makes hệ thống (system / 시스템) faster.”** It changes when caller waits and smooths tải (load / 로드); total công việc (work / 작업)/sức chứa (capacity / 용량) unchanged.

**“Kafka/RabbitMQ guarantees exactly once everywhere.”** Broker guarantees have phạm vi (scope / 범위); bên ngoài (external / 외부) DB/API side effects need coordination/idempotency.

**“Unbounded hàng đợi (queue / 큐) is safer because không reject.”** It often fails later with worse độ trễ (latency / 지연 시간)/tài nguyên (resource / 자원) exhaustion.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

[Linear queues](../01_algorithms_data_structures/03_linear_data_structures.md) are cục bộ (local / 로컬) lớp trừu tượng (abstraction / 추상화); [TCP backpressure](../06_networks_distributed_systems/02_transport_tcp_udp_and_congestion.md) mạng (network / 네트워크) example; [fault tolerance](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md) uses tải (load / 로드) shedding/circuit breakers; next [time/idempotency](./04_time_serialization_and_idempotency.md) handles thử lại (retry / 재시도) effects.

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 abstraction modularity interfaces and apis](./00_abstraction_modularity_interfaces_and_apis.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
