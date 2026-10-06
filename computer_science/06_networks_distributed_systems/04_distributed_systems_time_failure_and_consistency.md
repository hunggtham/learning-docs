# Thời gian (time / 시간), thất bại (failure / 실패) và consistency trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Time, failure và consistency trong distributed systems**. Route đi từ partial failure → clock/causality → consistency models → CAP → safety/liveness và failure detectors, để mọi guarantee được đặt trong giới hạn quan sát và thời gian.

Hệ thống phân tán (distributed system / 분산 시스템) gồm components trên nhiều machines/processes giao tiếp qua mạng (network / 네트워크). Điều làm nó khó không chỉ “nhiều máy” mà là **không có dùng chung (shared / 공유) bộ nhớ (memory / 메모리) hoàn hảo, không có toàn cục (global / 전역) clock hoàn hảo, message delay không bounded chắc chắn, và thất bại (failure / 실패) có thể partial**.

## Partial thất bại (failure / 실패)

Single tiến trình (process / 프로세스) crash thường dễ nhận: nó dừng. hệ thống phân tán (distributed system / 분산 시스템) có thể thấy nút (node / 노드) A nói B hết thời gian chờ (timeout / 타임아웃) nhưng C vẫn nói chuyện được với B. mạng (network / 네트워크) partition, asymmetric routing, GC pause, overload và packet mất mát (loss / 손실) có thể giống thất bại (failure / 실패).

Hết thời gian chờ (timeout / 타임아웃) chỉ nói “chưa nhận phản hồi (response / 응답) trong thời gian chờ”, không chứng minh remote thao tác (operation / 연산) chưa chạy. Đây là nguồn duplicate side effects khi thử lại (retry / 재시도).

> **Nối mạch:** Partial failure làm observation lệch giữa nodes; không có global clock đơn giản, nên causality tiếp theo phải được biểu diễn bằng event ordering hoặc logical clocks.

## Không có toàn cục (global / 전역) thời gian (time / 시간) đơn giản

Vật lý (physical / 물리적) clocks drift. NTP/PTP synchronize tương đối nhưng bất định (uncertainty / 불확실성) vẫn tồn tại. Timestamp từ machine A 10:00:00.100 và B 10:00:00.090 không chứng minh sự kiện (event / 이벤트) B xảy ra trước theo nhân quả (causal / 인과적) thứ tự (order / 순서).

Lamport clocks capture happens-before partial thứ tự (order / 순서): cục bộ (local / 로컬) events increment counter; send includes clock; receive advances max+1. véc-tơ (vector / 벡터) clocks có thể detect tính đồng thời (concurrency / 동시성) nhưng siêu dữ liệu (metadata / 메타데이터) grows with participants.

Logical clocks không đo wall thời gian (time / 시간); chúng encode thứ tự (ordering / 순서) thông tin (information / 정보).

> **Nối mạch:** **Causality** nối từ **Không có toàn cục (global / 전역) thời gian (time / 시간) đơn giản** sang **Consistency các mô hình (models / 모델들)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Causality

Sự kiện (event / 이벤트) A causally precedes B nếu B có thể be influenced by A via program/message chuỗi (chain / 사슬). Concurrent events không có nhân quả (causal / 인과적) quan hệ (relation / 관계). Many consistency các mô hình (models / 모델들) preserve nhân quả (causal / 인과적) thứ tự (order / 순서) even if total thứ tự (order / 순서) unnecessary.

> **Nối mạch:** **Consistency các mô hình (models / 모델들)** nối từ **Causality** sang **CAP theorem đúng ngữ cảnh (context / 맥락)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Consistency các mô hình (models / 모델들)

Strong consistency là family, không một term duy nhất. Linearizability makes operations appear atomic in real-time-consistent thứ tự (order / 순서). Sequential consistency preserves per-process thứ tự (order / 순서) but not real-time ràng buộc (constraint / 제약조건). nhân quả (causal / 인과적) consistency preserves causality. Eventual consistency promises replicas converge if updates stop and propagation continues, but giải quyết xung đột (conflict resolution / 충돌 해결) ngữ nghĩa (semantics / 의미론) matter.

Máy khách (client / 클라이언트)/session guarantees như read-your-writes và monotonic reads có thể làm weakly consistent các hệ thống (systems / 시스템들) dễ dùng hơn.

> **Nối mạch:** **CAP theorem đúng ngữ cảnh (context / 맥락)** nối từ **Consistency các mô hình (models / 모델들)** sang **An toàn (safety / 안전) và liveness**, vì cơ chế trước tạo đầu vào cho bước sau.

## CAP theorem đúng ngữ cảnh (context / 맥락)

CAP states that in an asynchronous-ish phân tán (distributed / 분산) dữ liệu (data / 데이터) hệ thống (system / 시스템) under mạng (network / 네트워크) partition, one cannot simultaneously guarantee both strong consistency (linearizability-like in common formulation) and availability for every yêu cầu (request / 요청). Partition tolerance is not optional on real mạng (network / 네트워크); when partition occurs, thiết kế (design / 설계) chooses rejecting/delaying some requests vs serving possibly divergent trạng thái (state / 상태).

CAP không nói “chọn 2 trong 3” trong normal thao tác (operation / 연산), và availability trong theorem có technical meaning, not general uptime SLA.

PACELC extends intuition: if Partition, trade Availability vs Consistency; Else, often độ trễ (latency / 지연 시간) vs Consistency.

> **Nối mạch:** **An toàn (safety / 안전) và liveness** nối từ **CAP theorem đúng ngữ cảnh (context / 맥락)** sang **Exactly-once myth**, vì cơ chế trước tạo đầu vào cho bước sau.

## An toàn (safety / 안전) và liveness

An toàn (safety / 안전) thuộc tính (property / 속성): bad thing never happens, e.g. two leaders lần ghi nhận (commit / 커밋) conflicting entries for same log position. Liveness: good thing eventually happens, e.g. yêu cầu (request / 요청) eventually completes when conditions recover.

Consensus algorithms often sacrifice liveness during certain partitions to preserve an toàn (safety / 안전).

> **Nối mạch:** **Exactly-once myth** nối từ **An toàn (safety / 안전) và liveness** sang **Thất bại (failure / 실패) detectors**, vì cơ chế trước tạo đầu vào cho bước sau.

## Exactly-once myth

Mạng (network / 네트워크) can lose yêu cầu (request / 요청) or phản hồi (response / 응답). máy khách (client / 클라이언트) timing out cannot know if máy chủ (server / 서버) executed. End-to-end “exactly once tác động (effect / 효과)” usually requires idempotency keys/deduplication/transactional trạng thái (state / 상태), not vận chuyển (transport / 전송) magic.

Message brokers may advertise exactly-once within scoped ngữ nghĩa (semantics / 의미론), but bên ngoài (external / 외부) side effects still need coordinated giao thức (protocol / 프로토콜).

> **Nối mạch:** **Thất bại (failure / 실패) detectors** nối từ **Exactly-once myth** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Thất bại (failure / 실패) detectors

Perfectly distinguishing slow from failed is impossible in fully asynchronous mô hình (model / 모델). Practical các hệ thống (systems / 시스템들) use heartbeats/timeouts and eventually accurate các giả định (assumptions / 가정들). Tuning thất bại (failure / 실패) detector too aggressive causes false positives; too slow delays failover.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Thất bại (failure / 실패) detectors**; **Dùng chung (common / 공통) Misconceptions** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> phân tán (distributed / 분산) các hệ thống (systems / 시스템들) replace certainty with **messages + bất định (uncertainty / 불확실성)**. Never infer “did not happen” from hết thời gian chờ (timeout / 타임아웃). Separate thứ tự (ordering / 순서), durability, availability and độ trễ (latency / 지연 시간) guarantees explicitly.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Dùng chung (common / 공통) Misconceptions

**“Eventual consistency means random/stale forever.”** It promises convergence under conditions, but xung đột (conflict / 충돌) and session ngữ nghĩa (semantics / 의미론) must be defined.

**“CAP means every phân tán (distributed / 분산) DB chooses exactly CA/CP/AP.”** The theorem focuses partition periods and specific guarantees; real các hệ thống (systems / 시스템들) expose tunable operations/các mô hình (models / 모델들).

**“Timestamp sorts events correctly globally.”** Clock skew and bất định (uncertainty / 불확실성) break nhân quả (causal / 인과적) suy luận (inference / 추론) unless stronger clock giao thức (protocol / 프로토콜)/các giả định (assumptions / 가정들) exist.

> **Nối mạch:** **Kết nối** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

[Concurrency](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md) has shared-memory thứ tự (ordering / 순서); phân tán (distributed / 분산) các hệ thống (systems / 시스템들) remove dùng chung (shared / 공유) clock/bộ nhớ (memory / 메모리) and add partial thất bại (failure / 실패). Next [replication/partitioning/consensus](./05_replication_partitioning_and_consensus.md) builds mechanisms for these các ràng buộc (constraints / 제약조건들).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
