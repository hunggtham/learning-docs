# Thời gian (time / 시간), thất bại (failure / 실패) và consistency trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Thời gian (time / 시간), thất bại (failure / 실패) và consistency trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Partial thất bại (failure / 실패)** biến nhận định thành tiêu chí kiểm tra hoặc cách gỡ lỗi; sau đó sang **Không có toàn cục (global / 전역) thời gian (time / 시간) đơn giản** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Hệ thống phân tán (distributed system / 분산 시스템) gồm components trên nhiều machines/processes giao tiếp qua mạng (network / 네트워크). Điều làm nó khó không chỉ “nhiều máy” mà là **không có dùng chung (shared / 공유) bộ nhớ (memory / 메모리) hoàn hảo, không có toàn cục (global / 전역) clock hoàn hảo, message delay không bounded chắc chắn, và thất bại (failure / 실패) có thể partial**.

## Partial thất bại (failure / 실패)

Single tiến trình (process / 프로세스) crash thường dễ nhận: nó dừng. hệ thống phân tán (distributed system / 분산 시스템) có thể thấy nút (node / 노드) A nói B hết thời gian chờ (timeout / 타임아웃) nhưng C vẫn nói chuyện được với B. mạng (network / 네트워크) partition, asymmetric routing, GC pause, overload và packet mất mát (loss / 손실) có thể giống thất bại (failure / 실패).

Hết thời gian chờ (timeout / 타임아웃) chỉ nói “chưa nhận phản hồi (response / 응답) trong thời gian chờ”, không chứng minh remote thao tác (operation / 연산) chưa chạy. Đây là nguồn duplicate side effects khi thử lại (retry / 재시도).

> **Chuyển mạch:** Partial failure làm observation lệch giữa nodes; không có global clock đơn giản, nên causality tiếp theo phải được biểu diễn bằng event ordering hoặc logical clocks.

## Không có toàn cục (global / 전역) thời gian (time / 시간) đơn giản

Vật lý (physical / 물리적) clocks drift. NTP/PTP synchronize tương đối nhưng bất định (uncertainty / 불확실성) vẫn tồn tại. Timestamp từ machine A 10:00:00.100 và B 10:00:00.090 không chứng minh sự kiện (event / 이벤트) B xảy ra trước theo nhân quả (causal / 인과적) thứ tự (order / 순서).

Lamport clocks capture happens-before partial thứ tự (order / 순서): cục bộ (local / 로컬) events increment counter; send includes clock; receive advances max+1. véc-tơ (vector / 벡터) clocks có thể detect tính đồng thời (concurrency / 동시성) nhưng siêu dữ liệu (metadata / 메타데이터) grows with participants.

Logical clocks không đo wall thời gian (time / 시간); chúng encode thứ tự (ordering / 순서) thông tin (information / 정보).

> **Chuyển mạch:** Ở chặng này của **Thời gian (time / 시간), thất bại (failure / 실패) và consistency trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들)**, **Causality** tiếp nhận điểm tựa từ **Không có toàn cục (global / 전역) thời gian (time / 시간) đơn giản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Consistency các mô hình (models / 모델들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Causality

Sự kiện (event / 이벤트) A causally precedes B nếu B có thể be influenced by A via program/message chuỗi (chain / 사슬). Concurrent events không có nhân quả (causal / 인과적) quan hệ (relation / 관계). Many consistency các mô hình (models / 모델들) preserve nhân quả (causal / 인과적) thứ tự (order / 순서) even if total thứ tự (order / 순서) unnecessary.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thời gian (time / 시간), thất bại (failure / 실패) và consistency trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들)**, **Consistency các mô hình (models / 모델들)** tiếp nhận điểm tựa từ **Causality** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CAP theorem đúng ngữ cảnh (context / 맥락)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Consistency các mô hình (models / 모델들)

Strong consistency là family, không một term duy nhất. Linearizability makes operations appear atomic in real-time-consistent thứ tự (order / 순서). Sequential consistency preserves per-process thứ tự (order / 순서) but not real-time ràng buộc (constraint / 제약조건). nhân quả (causal / 인과적) consistency preserves causality. Eventual consistency promises replicas converge if updates stop and propagation continues, but giải quyết xung đột (conflict resolution / 충돌 해결) ngữ nghĩa (semantics / 의미론) matter.

Máy khách (client / 클라이언트)/session guarantees như read-your-writes và monotonic reads có thể làm weakly consistent các hệ thống (systems / 시스템들) dễ dùng hơn.

> **Chuyển mạch:** Trong **Thời gian (time / 시간), thất bại (failure / 실패) và consistency trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들)**, **CAP theorem đúng ngữ cảnh (context / 맥락)** tiếp nhận điểm tựa từ **Consistency các mô hình (models / 모델들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **An toàn (safety / 안전) và liveness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CAP theorem đúng ngữ cảnh (context / 맥락)

CAP states that in an asynchronous-ish phân tán (distributed / 분산) dữ liệu (data / 데이터) hệ thống (system / 시스템) under mạng (network / 네트워크) partition, one cannot simultaneously guarantee both strong consistency (linearizability-like in common formulation) and availability for every yêu cầu (request / 요청). Partition tolerance is not optional on real mạng (network / 네트워크); when partition occurs, thiết kế (design / 설계) chooses rejecting/delaying some requests vs serving possibly divergent trạng thái (state / 상태).

CAP không nói “chọn 2 trong 3” trong normal thao tác (operation / 연산), và availability trong theorem có technical meaning, not general uptime SLA.

PACELC extends intuition: if Partition, trade Availability vs Consistency; Else, often độ trễ (latency / 지연 시간) vs Consistency.

> **Chuyển mạch:** Ở chặng này của **Thời gian (time / 시간), thất bại (failure / 실패) và consistency trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들)**, **An toàn (safety / 안전) và liveness** tiếp nhận điểm tựa từ **CAP theorem đúng ngữ cảnh (context / 맥락)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Exactly-once myth** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## An toàn (safety / 안전) và liveness

An toàn (safety / 안전) thuộc tính (property / 속성): bad thing never happens, e.g. two leaders lần ghi nhận (commit / 커밋) conflicting entries for same log position. Liveness: good thing eventually happens, e.g. yêu cầu (request / 요청) eventually completes when conditions recover.

Consensus algorithms often sacrifice liveness during certain partitions to preserve an toàn (safety / 안전).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thời gian (time / 시간), thất bại (failure / 실패) và consistency trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들)**, **Exactly-once myth** tiếp nhận điểm tựa từ **An toàn (safety / 안전) và liveness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thất bại (failure / 실패) detectors** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Exactly-once myth

Mạng (network / 네트워크) can lose yêu cầu (request / 요청) or phản hồi (response / 응답). máy khách (client / 클라이언트) timing out cannot know if máy chủ (server / 서버) executed. End-to-end “exactly once tác động (effect / 효과)” usually requires idempotency keys/deduplication/transactional trạng thái (state / 상태), not vận chuyển (transport / 전송) magic.

Message brokers may advertise exactly-once within scoped ngữ nghĩa (semantics / 의미론), but bên ngoài (external / 외부) side effects still need coordinated giao thức (protocol / 프로토콜).

> **Chuyển mạch:** Trong **Thời gian (time / 시간), thất bại (failure / 실패) và consistency trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들)**, **Thất bại (failure / 실패) detectors** tiếp nhận điểm tựa từ **Exactly-once myth** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thất bại (failure / 실패) detectors

Perfectly distinguishing slow from failed is impossible in fully asynchronous mô hình (model / 모델). Practical các hệ thống (systems / 시스템들) use heartbeats/timeouts and eventually accurate các giả định (assumptions / 가정들). Tuning thất bại (failure / 실패) detector too aggressive causes false positives; too slow delays failover.

> **Chuyển mạch:** Ở chặng này của **Thời gian (time / 시간), thất bại (failure / 실패) và consistency trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Thất bại (failure / 실패) detectors** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> phân tán (distributed / 분산) các hệ thống (systems / 시스템들) replace certainty with **messages + bất định (uncertainty / 불확실성)**. Never infer “did not happen” from hết thời gian chờ (timeout / 타임아웃). Separate thứ tự (ordering / 순서), durability, availability and độ trễ (latency / 지연 시간) guarantees explicitly.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thời gian (time / 시간), thất bại (failure / 실패) và consistency trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Eventual consistency means random/stale forever.”** It promises convergence under conditions, but xung đột (conflict / 충돌) and session ngữ nghĩa (semantics / 의미론) must be defined.

**“CAP means every phân tán (distributed / 분산) DB chooses exactly CA/CP/AP.”** The theorem focuses partition periods and specific guarantees; real các hệ thống (systems / 시스템들) expose tunable operations/các mô hình (models / 모델들).

**“Timestamp sorts events correctly globally.”** Clock skew and bất định (uncertainty / 불확실성) break nhân quả (causal / 인과적) suy luận (inference / 추론) unless stronger clock giao thức (protocol / 프로토콜)/các giả định (assumptions / 가정들) exist.

> **Chuyển mạch:** Trong **Thời gian (time / 시간), thất bại (failure / 실패) và consistency trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들)**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[Concurrency](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md) has shared-memory thứ tự (ordering / 순서); phân tán (distributed / 분산) các hệ thống (systems / 시스템들) remove dùng chung (shared / 공유) clock/bộ nhớ (memory / 메모리) and add partial thất bại (failure / 실패). Next [replication/partitioning/consensus](./05_replication_partitioning_and_consensus.md) builds mechanisms for these các ràng buộc (constraints / 제약조건들).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
