# Phân tán (distributed / 분산) transactions, exactly-once và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Phân tán (distributed / 분산) transactions, exactly-once và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Hết thời gian chờ (timeout / 타임아웃) không phải bằng chứng (evidence / 증거) của thất bại (failure / 실패)** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **At-most-once, at-least-once và exactly-once** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối distributed transactions với exactly-once và failure semantics, để retry, duplicate và recovery được phân biệt bằng hệ quả.

Trong một tiến trình (process / 프로세스), hàm (function / 함수) có thể return success/thất bại (failure / 실패) tương đối rõ. Trong hệ thống phân tán (distributed system / 분산 시스템), hết thời gian chờ (timeout / 타임아웃) tạo trạng thái khó hơn: **thao tác (operation / 연산) đã thất bại, hay chỉ phản hồi (response / 응답) thất lạc?** Đây là nguồn gốc của thử lại (retry / 재시도) ambiguity, duplicate side effects và nhiều giao thức (protocol / 프로토콜) patterns như idempotency key, outbox, 2PC và consensus-backed máy trạng thái (state machine / 상태 머신).

## Hết thời gian chờ (timeout / 타임아웃) không phải bằng chứng (evidence / 증거) của thất bại (failure / 실패)

Máy khách (client / 클라이언트) gửi yêu cầu (request / 요청), máy chủ (server / 서버) lần ghi nhận (commit / 커밋) DB rồi phản hồi (response / 응답) bị mất. máy khách (client / 클라이언트) thấy hết thời gian chờ (timeout / 타임아웃) nhưng thao tác (operation / 연산) đã thành công. Nếu thử lại (retry / 재시도) một `chargeCard()` không idempotent, khách có thể bị charge hai lần.

Vì vậy phân tán (distributed / 분산) API cần phân biệt ít nhất:

```text
known success
known failure
unknown outcome
```

Unknown kết quả (outcome / 결과) là trạng thái thật, không nên ép thành boolean chỉ vì ứng dụng (application / 애플리케이션) API muốn đơn giản.

> **Nối mạch:** **Hết thời gian chờ (timeout / 타임아웃) không phải bằng chứng (evidence / 증거) của thất bại (failure / 실패)** đặt vấn đề; **At-most-once, at-least-once và exactly-once** kiểm tra bằng chứng, rồi **Idempotency biến thử lại (retry / 재시도) thành thao tác (operation / 연산) an toàn hơn** mở rộng hệ quả.

## At-most-once, at-least-once và exactly-once

**At-most-once** ưu tiên không duplicate nhưng có thể mất thao tác (operation / 연산). **At-least-once** thử lại (retry / 재시도) tới khi có ack, chấp nhận duplicate delivery/thực thi (execution / 실행). **Exactly-once** thường chỉ đạt được trong một ranh giới (boundary / 경계) cụ thể bằng coordination + durable deduplication/chuyển tiếp trạng thái (state transition / 상태 전이); không phải phép màu loại bỏ thất bại (failure / 실패).

Một message broker nói “exactly-once” thường định nghĩa guarantee trong phạm vi producer/broker/bên tiêu thụ (consumer / 소비자) trạng thái (state / 상태) được phối hợp. Khi side tác động (effect / 효과) đi ra hệ thống khác như email, payment gateway hay bên ngoài (external / 외부) API, ranh giới (boundary / 경계) guarantee thay đổi.

> **Nối mạch:** **Idempotency biến thử lại (retry / 재시도) thành thao tác (operation / 연산) an toàn hơn** nối từ **At-most-once, at-least-once và exactly-once** sang **Two-Phase lần ghi nhận (commit / 커밋) giải atomicity giữa participants**, vì cơ chế trước tạo đầu vào cho bước sau.

## Idempotency biến thử lại (retry / 재시도) thành thao tác (operation / 연산) an toàn hơn

Thao tác (operation / 연산) idempotent nghĩa apply nhiều lần cho cùng logical yêu cầu (request / 요청) cho final trạng thái (state / 상태) tương đương apply một lần. `SET balance = 100` gần idempotent về trạng thái (state / 상태); `balance += 100` không.

API có thể dùng idempotency key. máy chủ (server / 서버) lưu key → kết quả (result / 결과)/giao dịch (transaction / 트랜잭션) định danh (identity / 식별자) trong durable store. thử lại (retry / 재시도) với cùng key trả lại prior kết quả (result / 결과) hoặc tiếp tục máy trạng thái (state machine / 상태 머신) thay vì tạo side tác động (effect / 효과) mới.

Nhưng deduplication cần retention chính sách (policy / 정책). Nếu key bị expire quá sớm, thử lại (retry / 재시도) muộn có thể trở thành duplicate thật.

> **Nối mạch:** **Two-Phase lần ghi nhận (commit / 커밋) giải atomicity giữa participants** nối từ **Idempotency biến thử lại (retry / 재시도) thành thao tác (operation / 연산) an toàn hơn** sang **Saga đổi atomicity mạnh lấy compensating workflow**, vì cơ chế trước tạo đầu vào cho bước sau.

## Two-Phase lần ghi nhận (commit / 커밋) giải atomicity giữa participants

2PC có coordinator và participants. Phase prepare hỏi mỗi participant có thể lần ghi nhận (commit / 커밋) không; nếu tất cả prepared, coordinator quyết định lần ghi nhận (commit / 커밋), nếu không abort.

Prepared participant thường đã giữ locks/resources và ghi durable intent. Nếu coordinator chết sau prepare, participant có thể bị **in-doubt**: nó không được tự đoán lần ghi nhận (commit / 커밋) hay abort nếu điều đó phá atomicity.

2PC vì vậy cung cấp atomic quyết định (decision / 결정) nhưng có blocking/failure-management chi phí (cost / 비용). Consensus có thể dùng để replicate coordinator/quyết định (decision / 결정) trạng thái (state / 상태), nhưng 2PC và consensus giải câu hỏi khác nhau: atomic lần ghi nhận (commit / 커밋) giữa tài nguyên (resource / 자원) managers vs agreement trong replicated máy trạng thái (state machine / 상태 머신).

> **Nối mạch:** **Two-Phase lần ghi nhận (commit / 커밋) giải atomicity giữa participants** đặt đầu vào cho **Saga đổi atomicity mạnh lấy compensating workflow**, rồi **Transactional outbox giải dual-write cục bộ** mở rộng hệ quả.

## Saga đổi atomicity mạnh lấy compensating workflow

Trong microservices, giữ phân tán (distributed / 분산) khóa (lock / 잠금)/giao dịch (transaction / 트랜잭션) lâu thường không phù hợp. Saga chia workflow thành cục bộ (local / 로컬) transactions và compensating actions.

Ví dụ booking: reserve flight → reserve hotel → charge payment. Nếu hotel thất bại (fail / 실패), compensation có thể bản phát hành (release / 릴리스) flight. Nhưng compensation không phải thời gian (time / 시간) travel. Email đã gửi không “unsend”, giá thị trường có thể đổi, bên ngoài (external / 외부) side tác động (effect / 효과) có thể không reversible.

Do đó saga tính đúng đắn (correctness / 정확성) cần nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론), không chỉ technical thử lại (retry / 재시도).

> **Nối mạch:** **Saga đổi atomicity mạnh lấy compensating workflow** đặt đầu vào cho **Transactional outbox giải dual-write cục bộ**, rồi **Fencing chống stale actor** mở rộng hệ quả.

## Transactional outbox giải dual-write cục bộ

Một dịch vụ (service / 서비스) cần cập nhật (update / 업데이트) DB rồi publish sự kiện (event / 이벤트). Nếu làm hai operations độc lập, crash giữa chúng tạo inconsistency.

Outbox mẫu (pattern / 패턴) ghi nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) + outbox row trong cùng cục bộ (local / 로컬) DB giao dịch (transaction / 트랜잭션). Worker/CDC sau đó publish outbox sự kiện (event / 이벤트), có thể thử lại (retry / 재시도). bên tiêu thụ (consumer / 소비자) phải xử lý duplicate bằng idempotency/deduplication.

Outbox không tạo exactly-once toàn cầu; nó biến “DB cập nhật (update / 업데이트) và intent-to-publish” thành atomic trong một cục bộ (local / 로컬) ranh giới (boundary / 경계).

> **Nối mạch:** **Fencing chống stale actor** nối từ **Transactional outbox giải dual-write cục bộ** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Fencing chống stale actor

Lease-holder cũ có thể bị pause, lease expire, actor mới nhận quyền, rồi actor cũ thức dậy và tiếp tục ghi (write / 쓰기). Chỉ “có khóa (lock / 잠금) đơn vị từ (token / 토큰)” chưa đủ nếu stale đơn vị từ (token / 토큰) vẫn được tài nguyên (resource / 자원) chấp nhận.

Fencing đơn vị từ (token / 토큰) tăng đơn điệu; lưu trữ (storage / 저장소)/tài nguyên (resource / 자원) từ chối yêu cầu (request / 요청) có đơn vị từ (token / 토큰) nhỏ hơn đơn vị từ (token / 토큰) mới nhất đã thấy. Đây là mẫu (pattern / 패턴) quan trọng khi tính đúng đắn (correctness / 정확성) phụ thuộc quyền sở hữu (ownership / 소유권) qua mạng (network / 네트워크)/GC pause/tiến trình (process / 프로세스) freeze.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Fencing chống stale actor**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> phân tán (distributed / 분산) tính đúng đắn (correctness / 정확성) bắt đầu từ **uncertain kết quả (outcome / 결과)**. thử lại (retry / 재시도) tạo duplicate rủi ro (risk / 위험); idempotency/dedup thuần hóa thử lại (retry / 재시도); 2PC phối hợp atomic quyết định (decision / 결정); saga phối hợp nghiệp vụ (business / 비즈니스) compensation; outbox nối cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션) với messaging; fencing ngăn đơn vị sở hữu (owner / 오너) cũ quay lại phá trạng thái (state / 상태).

> **Nối mạch:** **Kết nối** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Foundation: [time/failure/consistency](../../basic/06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md), [replication/consensus](../../basic/06_networks_distributed_systems/05_replication_partitioning_and_consensus.md), [idempotency](../../basic/08_software_systems/04_time_serialization_and_idempotency.md) và [event-driven systems](../../basic/08_software_systems/06_event_driven_and_stream_processing.md).

> **Bàn giao:** Giữ lại distinction giữa uncertain outcome, retry/dedup, atomic commit, compensation và fencing trước khi gọi một workflow là “exactly once”. Sang [Failure detectors và membership](./01_failure_detectors_membership_and_gossip.md) để xử lý suspicion/authority, hoặc [Leases và fencing](./02_leases_fencing_tokens_and_split_brain_prevention.md) khi stale actor có thể quay lại; quay về [README](./README.md) để xác nhận owner.
