# Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Fault, lỗi (error / 오류) và thất bại (failure / 실패)** biến nhận định thành tiêu chí kiểm tra hoặc cách gỡ lỗi; sau đó sang **Redundancy** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Reliable hệ thống (system / 시스템) không phải hệ thống (system / 시스템) không bao giờ thất bại (fail / 실패). Components inevitably thất bại (fail / 실패); độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) designs detection, containment, khôi phục (recovery / 복구) and sức chứa (capacity / 용량) so user-visible dịch vụ (service / 서비스) meets defined objectives.

## Fault, lỗi (error / 오류) và thất bại (failure / 실패)

Dependability literature often distinguishes fault = underlying cause, lỗi (error / 오류) = incorrect trạng thái nội bộ (internal state / 내부 상태), thất bại (failure / 실패) = externally visible dịch vụ (service / 서비스) deviation. A bit flip fault may corrupt trạng thái (state / 상태); checksum detects lỗi (error / 오류) before user-visible thất bại (failure / 실패).

Terminology varies, but distinction encourages defense before bên ngoài (external / 외부) impact.

> **Chuyển mạch:** Fault gây error và failure; redundancy giảm blast radius khi failure độc lập, còn retry chỉ an toàn khi operation idempotent và có budget/backoff rõ ràng.

## Redundancy

Replication, extra instances, RAID/erasure coding và multi-zone triển khai (deployment / 배포) add redundancy. Redundancy helps only if failures sufficiently independent. Two replicas on same power rack are not protection from rack outage.

Correlated thất bại (failure / 실패) and dùng chung (shared / 공유) dependencies are dùng chung (common / 공통) hidden single points.

> **Chuyển mạch:** Ở chặng này của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **Thử lại (retry / 재시도)** tiếp nhận điểm tựa từ **Redundancy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hết thời gian chờ (timeout / 타임아웃)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thử lại (retry / 재시도)

Thử lại (retry / 재시도) turns transient thất bại (failure / 실패) into success but adds tải (load / 로드). Exponential backoff + jitter prevents synchronized thử lại (retry / 재시도) storms. thử lại (retry / 재시도) ngân sách (budget / 예산) limits amplification.

Only thử lại (retry / 재시도) operations whose ngữ nghĩa (semantics / 의미론) are safe or made idempotent. hết thời gian chờ (timeout / 타임아웃) + thử lại (retry / 재시도) without idempotency can duplicate payment/thứ tự (order / 순서).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **Hết thời gian chờ (timeout / 타임아웃)** tiếp nhận điểm tựa từ **Thử lại (retry / 재시도)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Circuit breaker** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hết thời gian chờ (timeout / 타임아웃)

Without hết thời gian chờ (timeout / 타임아웃), waiting on remote phụ thuộc (dependency / 의존성) can consume luồng thực thi (thread / 스레드)/liên kết (connection / 연결) forever. hết thời gian chờ (timeout / 타임아웃) too short causes false thất bại (failure / 실패)/thử lại (retry / 재시도); too long delays khôi phục (recovery / 복구) and holds resources. hết thời gian chờ (timeout / 타임아웃) should reflect độ trễ (latency / 지연 시간) SLO and end-to-end deadline, not arbitrary constants copied everywhere.

Deadline propagation gives downstream remaining ngân sách (budget / 예산) rather than each tầng (layer / 계층) resetting full hết thời gian chờ (timeout / 타임아웃).

> **Chuyển mạch:** Trong **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **Circuit breaker** tiếp nhận điểm tựa từ **Hết thời gian chờ (timeout / 타임아웃)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bulkhead** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Circuit breaker

When phụ thuộc (dependency / 의존성) failing, circuit breaker temporarily reject/fallback instead of sending all requests, reducing wasted công việc (work / 작업) and allowing khôi phục (recovery / 복구). But it is stateful and can create synchronized reopen/tải (load / 로드) spikes; half-open probing helps.

Tải (load / 로드) shedding rejects low-priority/excess công việc (work / 작업) before total collapse. hàng đợi (queue / 큐) limits are độ tin cậy (reliability / 신뢰성) tools.

> **Chuyển mạch:** Ở chặng này của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **Bulkhead** tiếp nhận điểm tựa từ **Circuit breaker** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khả năng quan sát (observability / 관측 가능성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bulkhead

Separate pools/quotas isolate miền lỗi (failure domain / 장애 도메인): one slow tenant/phụ thuộc (dependency / 의존성) should not consume all threads/connections. Ship bulkheads inspired name. tài nguyên (resource / 자원) partitioning trades utilization efficiency for fault isolation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **Khả năng quan sát (observability / 관측 가능성)** tiếp nhận điểm tựa từ **Bulkhead** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SLI, SLO, SLA** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khả năng quan sát (observability / 관측 가능성)

Khả năng quan sát (observability / 관측 가능성) asks how well trạng thái nội bộ (internal state / 내부 상태) can be inferred from outputs/telemetry. Logs, metrics and traces are tools, not khả năng quan sát (observability / 관측 가능성) definition.

Golden signals often include độ trễ (latency / 지연 시간), traffic, errors, saturation. RED (rate, Errors, Duration) useful for services; USE (Utilization, Saturation, Errors) for resources.

> **Chuyển mạch:** Trong **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **SLI, SLO, SLA** tiếp nhận điểm tựa từ **Khả năng quan sát (observability / 관측 가능성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Availability math intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SLI, SLO, SLA

SLI is measured indicator (e.g. successful requests under 300 ms). SLO is mục tiêu (target / 대상) (99.9% over window). SLA is bên ngoài (external / 외부)/nghiệp vụ (business / 비즈니스) agreement with consequences, not synonym of SLO.

Lỗi (error / 오류) ngân sách (budget / 예산) = allowed unreliability under SLO, enabling sự đánh đổi (trade-off / 트레이드오프) between tính năng (feature / 기능) velocity and độ tin cậy (reliability / 신뢰성) công việc (work / 작업).

> **Chuyển mạch:** Ở chặng này của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **SLI, SLO, SLA** cho ta quy tắc; **Availability math intuition** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Graceful degradation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Availability math intuition

If independent components are in series and all required, availability multiplies. Two 99.9% required independent services give ~99.8001% combined, not 99.9. Parallel redundant components can improve availability if failover works and failures independent.

Độ tin cậy (reliability / 신뢰성) kiến trúc (architecture / 아키텍처) therefore considers phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), not thành phần (component / 컴포넌트) score alone.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **Availability math intuition** cho ta quy tắc; **Graceful degradation** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Chaos/fault injection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Graceful degradation

Under thất bại (failure / 실패), hệ thống (system / 시스템) may serve stale bộ nhớ đệm (cache / 캐시), disable recommendations, reduce chất lượng (quality / 품질) or read-only chế độ (mode / 모드) rather than total outage. Degradation must preserve trọng yếu (critical / 중요) tính đúng đắn (correctness / 정확성)/bảo mật (security / 보안); serving stale authorization chính sách (policy / 정책) may be unsafe.

> **Chuyển mạch:** Trong **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **Chaos/fault injection** tiếp nhận điểm tựa từ **Graceful degradation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chaos/fault injection

Testing thất bại (failure / 실패) modes deliberately verifies các giả định (assumptions / 가정들) about timeouts, failover and khôi phục (recovery / 복구). Injected faults should have blast-radius controls and hypotheses. Chaos without khả năng quan sát (observability / 관측 가능성) is just causing incidents.

> **Chuyển mạch:** Ở chặng này của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Chaos/fault injection** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> độ tin cậy (reliability / 신뢰성) = **assume thất bại (failure / 실패), bound blast radius, detect quickly, recover predictably, and define acceptable người dùng (user / 사용자) impact quantitatively**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“High availability = never thất bại (fail / 실패).”** Availability is measured fraction/dịch vụ (service / 서비스) mục tiêu (objective / 목표); components can thất bại (fail / 실패) while hệ thống (system / 시스템) remains available.

**“More replicas always safer.”** dùng chung (shared / 공유) thất bại (failure / 실패) domains, bad deploys and replicated corruption can take all copies.

**“Monitoring = khả năng quan sát (observability / 관측 가능성).”** Monitoring watches known signals; khả năng quan sát (observability / 관측 가능성) broader ability to infer unknown/nội bộ (internal / 내부) conditions through telemetry.

> **Chuyển mạch:** Trong **Fault tolerance, khả năng quan sát (observability / 관측 가능성) và độ tin cậy (reliability / 신뢰성)**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[Distributed partial failure](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md) supplies thất bại (failure / 실패) mô hình (model / 모델); [idempotency](../08_software_systems/04_time_serialization_and_idempotency.md) enables safe retries; [performance/capacity](../08_software_systems/02_performance_capacity_and_scalability.md) explains saturation and hàng đợi (queue / 큐) collapse.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
