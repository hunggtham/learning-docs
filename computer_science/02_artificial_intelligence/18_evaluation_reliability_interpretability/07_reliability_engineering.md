# Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Kiến thức tiên quyết** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Độ tin cậy (reliability / 신뢰성) khác Accuracy** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Kỹ thuật độ tin cậy (reliability engineering / 신뢰성 공학)** là quá trình thiết kế hệ thống để nó cung cấp hành vi đúng hợp đồng trong thời gian dài, chịu được lỗi, suy giảm có kiểm soát và phục hồi được. Với AI, độ tin cậy không chỉ là dịch vụ (service / 서비스) còn chạy; nó còn bao gồm chất lượng quyết định, tính nhất quán của trạng thái (state / 상태), mức an toàn của side tác động (effect / 효과) và khả năng phát hiện lỗi âm thầm.

Một mô hình có accuracy cao vẫn có thể tạo hệ thống không đáng tin nếu retrieval lỗi, trạng thái (state / 상태) stale, công cụ (tool / 도구) thử lại (retry / 재시도) trùng lặp hoặc fallback thay đổi ngữ nghĩa (semantics / 의미론) mà không ai biết.

## Kiến thức tiên quyết

Nên đọc trước [AI System Design](../15_ai_engineering/10_ai_system_design.md), [Monitoring và Observability](../16_mlops_and_llmops/06_monitoring_and_observability.md), [Incident Response](../16_mlops_and_llmops/09_incident_response_and_lifecycle.md), [Agent Evaluation](../10_agents_and_ai_systems/09_agent_evaluation.md) và [Nền tảng Evaluation](./00_evaluation_foundations.md).

> **Chuyển mạch:** Trong **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Độ tin cậy (reliability / 신뢰성) khác Accuracy** tiếp nhận điểm tựa từ **Kiến thức tiên quyết** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình xác suất của thành công đầu-cuối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ tin cậy (reliability / 신뢰성) khác Accuracy

Accuracy là một chỉ số (metric / 지표) thống kê trên một tập dữ liệu. độ tin cậy (reliability / 신뢰성) bao phủ toàn bộ chuỗi:

```text
availability
correctness
latency stability
state consistency
failure containment
recoverability
observability
safe degradation
```

Nếu 1% lỗi có thể tạo giao dịch trùng hoặc xóa dữ liệu, “99% đúng” không phải mô tả đầy đủ mức độ tin cậy.

> **Chuyển mạch:** Ở chặng này của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Mô hình xác suất của thành công đầu-cuối** tiếp nhận điểm tựa từ **Độ tin cậy (reliability / 신뢰성) khác Accuracy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân loại dạng thất bại (failure mode / 실패 모드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình xác suất của thành công đầu-cuối

Một intuition đơn giản cho chuỗi `n` bước quan trọng độc lập, mỗi bước có xác suất thành công `p_i`:

\[
P(success)\approx\prod_{i=1}^{n}p_i
\]

Nếu 20 bước đều có độ tin cậy (reliability / 신뢰성) 0.99, xác suất tất cả cùng thành công chỉ khoảng:

\[
0.99^{20}\approx0.818
\]

Thực tế lỗi không độc lập hoàn toàn, nhưng công thức cho thấy vì sao tác nhân (agent / 에이전트) dài hạn cần checkpoint, xác minh (verification / 확인) và khôi phục (recovery / 복구) thay vì chỉ “mô hình (model / 모델) tốt hơn”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Phân loại dạng thất bại (failure mode / 실패 모드)** tiếp nhận điểm tựa từ **Mô hình xác suất của thành công đầu-cuối** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phụ thuộc (dependency / 의존성) và thất bại (failure / 실패) ngân sách (budget / 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân loại dạng thất bại (failure mode / 실패 모드)

Nên phân lỗi theo nhiều trục:

```text
transient / persistent
detectable / silent
recoverable / irreversible
local / cascading
model / data / infra / tool / policy / state
```

Mỗi loại cần phản ứng khác nhau. `TIMEOUT` có thể thử lại (retry / 재시도); `PERMISSION_DENIED` thường phải dừng; mutation sai có thể cần compensating hành động (action / 동작).

> **Chuyển mạch:** Trong **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Phụ thuộc (dependency / 의존성) và thất bại (failure / 실패) ngân sách (budget / 예산)** tiếp nhận điểm tựa từ **Phân loại dạng thất bại (failure mode / 실패 모드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Queueing và tail độ trễ (latency / 지연 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phụ thuộc (dependency / 의존성) và thất bại (failure / 실패) ngân sách (budget / 예산)

Một yêu cầu (request / 요청) thường phụ thuộc nhiều thành phần:

```text
API
→ retrieval
→ model
→ tool
→ database
→ verifier
```

SLO đầu-cuối không thể tốt hơn phụ thuộc (dependency / 의존성) yếu nhất nếu không có redundancy hoặc fallback. Vì vậy cần phân bổ **ngân sách lỗi (failure budget)** và **ngân sách độ trễ (latency budget)** cho từng thành phần.

Ví dụ yêu cầu (request / 요청) có deadline 2 giây nhưng retrieval hết thời gian chờ (timeout / 타임아웃) 2 giây thì mô hình (model / 모델) và verifier không còn thời gian chạy. Deadline phải được truyền xuống phụ thuộc (dependency / 의존성) thay vì mỗi dịch vụ (service / 서비스) tự đặt hết thời gian chờ (timeout / 타임아웃) tùy ý.

> **Chuyển mạch:** Ở chặng này của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Queueing và tail độ trễ (latency / 지연 시간)** tiếp nhận điểm tựa từ **Phụ thuộc (dependency / 의존성) và thất bại (failure / 실패) ngân sách (budget / 예산)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Graceful degradation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Queueing và tail độ trễ (latency / 지연 시간)

Khi utilization tiến gần 100%, hàng đợi (queue / 큐) thường tăng nhanh và p95/p99 độ trễ (latency / 지연 시간) có thể bùng nổ dù thông lượng (throughput / 처리량) trung bình nhìn vẫn ổn.

Trực giác quan trọng:

```text
capacity gần bão hòa
→ request chờ lâu hơn
→ client timeout / retry
→ tải tăng thêm
→ cascading failure
```

Do đó môi trường vận hành (production / 운영 환경) AI không nên tối ưu GPU utilization tới mức không còn headroom cho burst, thử lại (retry / 재시도) hoặc failover.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Graceful degradation** tiếp nhận điểm tựa từ **Queueing và tail độ trễ (latency / 지연 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fallback phải có ngữ nghĩa (semantics / 의미론) rõ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Graceful degradation

Khi đường chính không khả dụng, hệ thống có thể giảm năng lực (capability / 역량) theo thứ tự có chủ đích:

```text
mô hình chính
→ mô hình dự phòng
→ retrieval-only / deterministic path
→ cache đã xác minh
→ human review
→ thông báo không thể xử lý
```

Fallback phải bảo toàn mức an toàn. Với quyết định rủi ro cao, tường minh (explicit / 명시적) thất bại (failure / 실패) thường tốt hơn fallback âm thầm sang mô hình (model / 모델) yếu hơn.

> **Chuyển mạch:** Trong **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Fallback phải có ngữ nghĩa (semantics / 의미론) rõ** tiếp nhận điểm tựa từ **Graceful degradation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Redundancy và tính độc lập của lỗi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fallback phải có ngữ nghĩa (semantics / 의미론) rõ

Một anti-pattern là:

```text
primary model lỗi
→ gọi model bất kỳ còn sống
```

Nếu mô hình (model / 모델) dự phòng có lược đồ (schema / 스키마), an toàn (safety / 안전) hành vi (behavior / 동작) hoặc năng lực (capability / 역량) khác, hệ thống có thể “available” nhưng không còn đúng đặc tả hợp đồng (contract / 계약).

Fallback nên được phiên bản (version / 버전) hóa, evaluation riêng và có chỉ số (metric / 지표) `fallback_rate` để tránh tình trạng degraded chế độ (mode / 모드) kéo dài mà không ai nhận ra.

> **Chuyển mạch:** Ở chặng này của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Redundancy và tính độc lập của lỗi** tiếp nhận điểm tựa từ **Fallback phải có ngữ nghĩa (semantics / 의미론) rõ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Circuit breaker** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Redundancy và tính độc lập của lỗi

Replication tăng availability khi các replica không cùng lỗi một nguyên nhân. Hai endpoint dùng chung provider, region hoặc credential có thể cùng chết.

Các dạng redundancy:

- nhiều replica;
- nhiều availability zone;
- nhiều provider;
- chỉ mục (index / 인덱스)/trạng thái (state / 상태) store replicated;
- read-only degraded đường dẫn (path / 경로).

Giá trị của redundancy phụ thuộc mức độc lập của miền lỗi (failure domain / 장애 도메인).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Circuit breaker** tiếp nhận điểm tựa từ **Redundancy và tính độc lập của lỗi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thử lại (retry / 재시도) có ngân sách** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Circuit breaker

Nếu downstream liên tục lỗi, **cầu dao (circuit breaker)** tạm ngừng gửi yêu cầu (request / 요청) để tránh thử lại (retry / 재시도) cascade.

```text
CLOSED    → hoạt động bình thường
OPEN      → fail fast
HALF-OPEN → gửi probe kiểm tra recovery
```

Circuit breaker đặc biệt hữu ích với mô hình (model / 모델) API, công cụ (tool / 도구) API hoặc retrieval dịch vụ (service / 서비스) có thất bại (failure / 실패) burst.

> **Chuyển mạch:** Trong **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Thử lại (retry / 재시도) có ngân sách** tiếp nhận điểm tựa từ **Circuit breaker** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Idempotency cho side tác động (effect / 효과)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thử lại (retry / 재시도) có ngân sách

Thử lại (retry / 재시도) chỉ phù hợp lỗi tạm thời và phải bị giới hạn bởi:

```text
max attempts
deadline
exponential backoff
jitter
retry budget
idempotency
```

Không nên cho từng tầng (layer / 계층) tự thử lại (retry / 재시도) ba lần độc lập; ba tầng (layer / 계층) lồng nhau có thể nhân số yêu cầu (request / 요청) lên rất nhanh.

> **Chuyển mạch:** Ở chặng này của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Idempotency cho side tác động (effect / 효과)** tiếp nhận điểm tựa từ **Thử lại (retry / 재시도) có ngân sách** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Xác minh (verification / 확인) trước và sau hành động (action / 동작)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Idempotency cho side tác động (effect / 효과)

Công cụ (tool / 도구) ghi dữ liệu như payment, email, thứ tự (order / 순서) hoặc deploy phải chống thực thi trùng.

Một **idempotency key** gắn với logical hành động (action / 동작) giúp yêu cầu (request / 요청) lặp lại trả cùng kết quả thay vì tạo side tác động (effect / 효과) mới.

Đây là yêu cầu thời gian chạy (runtime / 런타임), không thể thay bằng prompt “đừng làm hai lần”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Xác minh (verification / 확인) trước và sau hành động (action / 동작)** tiếp nhận điểm tựa từ **Idempotency cho side tác động (effect / 효과)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thất bại (fail / 실패) closed và thất bại (fail / 실패) open** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xác minh (verification / 확인) trước và sau hành động (action / 동작)

Mẫu (pattern / 패턴) đáng tin:

```text
model đề xuất
→ schema/policy validation
→ executor thực thi
→ đọc lại state thật
→ verifier kiểm acceptance criterion
```

Các verifier có thể là parser, kiểu (type / 타입) checker, đơn vị (unit / 단위) kiểm thử (test / 테스트), SQL validator, citation checker, chính sách (policy / 정책) engine hoặc phép tính xác định.

Đối với tác nhân (agent / 에이전트), “mô hình (model / 모델) nói done” không phải bằng chứng tác vụ (task / 작업) đã hoàn thành.

> **Chuyển mạch:** Trong **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Thất bại (fail / 실패) closed và thất bại (fail / 실패) open** tiếp nhận điểm tựa từ **Xác minh (verification / 확인) trước và sau hành động (action / 동작)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Durable trạng thái (state / 상태), checkpoint và resume** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thất bại (fail / 실패) closed và thất bại (fail / 실패) open

**thất bại (fail / 실패) closed**: khi không chắc chắn thì không cho hành động (action / 동작) tiếp tục. Phù hợp với bảo mật (security / 보안), payment, destructive ghi (write / 쓰기) hoặc high-risk thao tác (operation / 연산).

**thất bại (fail / 실패) open**: khi phụ thuộc (dependency / 의존성) lỗi vẫn tiếp tục với degraded hành vi (behavior / 동작). Phù hợp hơn với tính năng (feature / 기능) ít rủi ro, ví dụ recommendation phụ.

Lựa chọn phải dựa trên impact của lỗi, không dựa trên mục tiêu availability chung chung.

> **Chuyển mạch:** Ở chặng này của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Durable trạng thái (state / 상태), checkpoint và resume** tiếp nhận điểm tựa từ **Thất bại (fail / 실패) closed và thất bại (fail / 실패) open** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Compensation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Durable trạng thái (state / 상태), checkpoint và resume

Workflow dài cần lưu trạng thái (state / 상태) có cấu trúc:

```text
completed steps
external resource IDs
pending action
approval state
artifacts
verification result
```

Sau crash, thời gian chạy (runtime / 런타임) tải checkpoint rồi xác định bước tiếp theo an toàn. Không nên replay mù toàn bộ transcript vì các side tác động (effect / 효과) cũ có thể chạy lại.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Compensation** tiếp nhận điểm tựa từ **Durable trạng thái (state / 상태), checkpoint và resume** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bulkhead và cô lập phạm vi ảnh hưởng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Compensation

Không phải phân tán (distributed / 분산) workflow nào cũng quay lui (rollback / 롤백) nguyên tử. Một số tác vụ (task / 작업) cần **hành động bù trừ (compensating action)**:

```text
reserve inventory → cancel reservation
charge payment    → refund
create resource   → revoke / delete nếu policy cho phép
```

Tác nhân (agent / 에이전트) không nên tự phát minh compensation; workflow phải định nghĩa tập hành động hợp lệ và điều kiện dùng chúng.

> **Chuyển mạch:** Trong **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Bulkhead và cô lập phạm vi ảnh hưởng** tiếp nhận điểm tựa từ **Compensation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tải (load / 로드) shedding và admission điều khiển (control / 제어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bulkhead và cô lập phạm vi ảnh hưởng

**Bulkhead** tách tài nguyên (resource / 자원) pool để một tenant hoặc tải công việc (workload / 워크로드) không làm cạn toàn hệ thống.

Ví dụ:

```text
interactive queue riêng
batch queue riêng
high-risk tools riêng
per-tenant concurrency limit
```

Cô lập giúp giảm **phạm vi ảnh hưởng (blast radius)** khi có lỗi.

> **Chuyển mạch:** Ở chặng này của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Tải (load / 로드) shedding và admission điều khiển (control / 제어)** tiếp nhận điểm tựa từ **Bulkhead và cô lập phạm vi ảnh hưởng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SLO và lỗi (error / 오류) ngân sách (budget / 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tải (load / 로드) shedding và admission điều khiển (control / 제어)

Khi overload, từ chối hoặc trì hoãn yêu cầu (request / 요청) ít quan trọng thường tốt hơn để tất cả yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃).

Admission điều khiển (control / 제어) có thể dựa trên priority, SLA, đơn vị từ (token / 토큰) ngân sách (budget / 예산), hàng đợi (queue / 큐) độ sâu (depth / 깊이) hoặc sức chứa (capacity / 용량) còn lại.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **SLO và lỗi (error / 오류) ngân sách (budget / 예산)** tiếp nhận điểm tựa từ **Tải (load / 로드) shedding và admission điều khiển (control / 제어)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ tin cậy (reliability / 신뢰성) cho RAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SLO và lỗi (error / 오류) ngân sách (budget / 예산)

SLO cho AI có thể bao gồm:

```text
availability
p99 latency
verified task success
maximum unsafe-action rate
retrieval freshness
cost per successful task
```

**lỗi (error / 오류) ngân sách (budget / 예산)** định lượng mức sai lệch còn chấp nhận được. Khi ngân sách (budget / 예산) bị dùng hết, nhóm (team / 팀) nên ưu tiên độ tin cậy (reliability / 신뢰성) thay vì tiếp tục rollout tính năng (feature / 기능) mới.

> **Chuyển mạch:** Trong **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Độ tin cậy (reliability / 신뢰성) cho RAG** tiếp nhận điểm tựa từ **SLO và lỗi (error / 오류) ngân sách (budget / 예산)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ tin cậy (reliability / 신뢰성) cho LLM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ tin cậy (reliability / 신뢰성) cho RAG

RAG có nhiều thất bại (failure / 실패) điểm (point / 지점):

```text
parser lỗi
index stale
metadata filter sai
retrieval miss
reranker sai
context bị cắt
citation không support claim
```

Một môi trường vận hành (production / 운영 환경) mẫu (pattern / 패턴) tốt là đo riêng retrieval health, chỉ mục (index / 인덱스) freshness và grounded answer chất lượng (quality / 품질). Xem [RAG Evaluation](../09_retrieval_and_rag/09_rag_evaluation.md).

> **Chuyển mạch:** Ở chặng này của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Độ tin cậy (reliability / 신뢰성) cho LLM** tiếp nhận điểm tựa từ **Độ tin cậy (reliability / 신뢰성) cho RAG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ tin cậy (reliability / 신뢰성) cho tác nhân (agent / 에이전트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ tin cậy (reliability / 신뢰성) cho LLM

Các điều khiển (control / 제어) thường dùng:

- structured generation;
- grounding bằng retrieval;
- đầu ra (output / 출력) validator;
- phiên bản (version / 버전) pinning;
- hết thời gian chờ (timeout / 타임아웃) và fallback;
- ngữ cảnh (context / 맥락) ngân sách (budget / 예산);
- regression evaluation.

Không có điều khiển (control / 제어) nào tự biến mô hình (model / 모델) thành nguồn sự thật. độ tin cậy (reliability / 신뢰성) phải gắn với task-specific bằng chứng (evidence / 증거).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Độ tin cậy (reliability / 신뢰성) cho tác nhân (agent / 에이전트)** tiếp nhận điểm tựa từ **Độ tin cậy (reliability / 신뢰성) cho LLM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chaos kỹ thuật (engineering / 엔지니어링) và game day** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ tin cậy (reliability / 신뢰성) cho tác nhân (agent / 에이전트)

Tác nhân (agent / 에이전트) cần thêm:

- step ngân sách (budget / 예산);
- durable trạng thái (state / 상태);
- permission phạm vi (scope / 범위);
- công cụ (tool / 도구) kiểm tra hợp lệ (validation / 검증);
- idempotency;
- xác minh (verification / 확인);
- approval ranh giới (boundary / 경계);
- vòng lặp (loop / 루프) detection;
- khôi phục (recovery / 복구) đường dẫn (path / 경로).

Mỗi bước tự trị bổ sung là một điểm thất bại (failure / 실패) mới. Vì vậy nên dùng deterministic workflow cho những phần đã biết rõ và dành autonomy cho bước thật sự mơ hồ.

> **Chuyển mạch:** Trong **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Chaos kỹ thuật (engineering / 엔지니어링) và game day** tiếp nhận điểm tựa từ **Độ tin cậy (reliability / 신뢰성) cho tác nhân (agent / 에이전트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **RTO và RPO** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chaos kỹ thuật (engineering / 엔지니어링) và game day

Có thể chủ động tiêm lỗi:

- mô hình (model / 모델) endpoint mất kết nối;
- retrieval chậm;
- chỉ mục (index / 인덱스) stale;
- công cụ (tool / 도구) trả 500;
- worker crash;
- cơ sở dữ liệu (database / 데이터베이스) xung đột (conflict / 충돌);
- quota cạn.

Mục tiêu không phải làm hệ thống hỏng, mà xác nhận fallback, alert và khôi phục (recovery / 복구) thực sự hoạt động trước sự cố (incident / 인시던트) thật.

> **Chuyển mạch:** Ở chặng này của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **RTO và RPO** tiếp nhận điểm tựa từ **Chaos kỹ thuật (engineering / 엔지니어링) và game day** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình triển khai môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RTO và RPO

**khôi phục (recovery / 복구) thời gian (time / 시간) mục tiêu (objective / 목표) (RTO)** là thời gian chấp nhận được để phục hồi.

**khôi phục (recovery / 복구) điểm (point / 지점) mục tiêu (objective / 목표) (RPO)** là lượng trạng thái (state / 상태)/dữ liệu (data / 데이터) có thể mất.

Tác nhân (agent / 에이전트) có trạng thái (state / 상태) hoặc workflow dài cần quan tâm cả hai giống hệ thống cơ sở dữ liệu (database / 데이터베이스) truyền thống.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Mô hình triển khai môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **RTO và RPO** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình triển khai môi trường vận hành (production / 운영 환경)

Một kiến trúc đáng tin thường có dạng:

```text
request
→ admission control
→ orchestrator có deadline
→ model / retrieval / tool
→ policy validation
→ side-effect executor
→ state persistence
→ verifier
→ response / escalation

song song:
metrics + trace + audit log + alert
```

Mô hình (model / 모델) nằm bên trong điều khiển (control / 제어) cấu trúc (structure / 구조); nó không tự sở hữu permission, thử lại (retry / 재시도), giao dịch (transaction / 트랜잭션) hay stop chính sách (policy / 정책).

> **Chuyển mạch:** Trong **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Sự đánh đổi (trade-off / 트레이드오프)** tiếp nhận điểm tựa từ **Mô hình triển khai môi trường vận hành (production / 운영 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dạng thất bại (failure mode / 실패 모드) của chính cơ chế độ tin cậy (reliability / 신뢰성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sự đánh đổi (trade-off / 트레이드오프)

Độ tin cậy (reliability / 신뢰성) không miễn phí. Redundancy tăng chi phí; verifier tăng độ trễ (latency / 지연 시간); human approval giảm thông lượng (throughput / 처리량); hết thời gian chờ (timeout / 타임아웃) ngắn có thể tăng false thất bại (failure / 실패); fallback làm kiến trúc phức tạp hơn.

Mục tiêu là dùng điều khiển (control / 제어) mạnh nhất ở nơi `P(failure) × Impact(failure)` lớn nhất, không phải thêm mọi điều khiển (control / 제어) vào mọi yêu cầu (request / 요청).

> **Chuyển mạch:** Ở chặng này của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Sự đánh đổi (trade-off / 트레이드오프)** xác định đầu vào; **Dạng thất bại (failure mode / 실패 모드) của chính cơ chế độ tin cậy (reliability / 신뢰성)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dạng thất bại (failure mode / 실패 모드) của chính cơ chế độ tin cậy (reliability / 신뢰성)

Các điều khiển (control / 제어) cũng có thể gây lỗi:

- thử lại (retry / 재시도) storm;
- fallback lỗi thời;
- circuit breaker mở quá lâu;
- verifier false positive;
- approval hàng đợi (queue / 큐) bị nghẽn;
- checkpoint không nhất quán;
- monitoring không thấy silent chất lượng (quality / 품질) regression.

Vì vậy độ tin cậy (reliability / 신뢰성) cơ chế (mechanism / 메커니즘) cũng phải được kiểm thử (test / 테스트) và quan sát.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Mô hình tư duy** gom các mảnh từ **Dạng thất bại (failure mode / 실패 모드) của chính cơ chế độ tin cậy (reliability / 신뢰성)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> **AI đáng tin cậy = năng lực đủ tốt được đặt bên trong một hệ thống có thể giới hạn, phát hiện và phục hồi lỗi.**

Không cần giả định mô hình (model / 모델) hoàn hảo nếu kiến trúc (architecture / 아키텍처) có thể ngăn lỗi lan rộng và xác minh các hành động quan trọng.

> **Chuyển mạch:** Trong **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “Reliable AI = hallucination thấp”

Hallucination chỉ là một dạng thất bại (failure mode / 실패 모드) ở cấp mô hình (model / 모델).

### “thử lại (retry / 재시도) càng nhiều càng ổn định”

Không. thử lại (retry / 재시도) không giới hạn có thể nhân tải và side tác động (effect / 효과).

### “Fallback luôn tốt hơn trả lỗi”

Không. Fallback chất lượng thấp cho high-risk hành động (action / 동작) có thể nguy hiểm hơn tường minh (explicit / 명시적) thất bại (failure / 실패).

### “Multi-provider tự động giải quyết outage”

Không nếu các provider dùng chung phụ thuộc (dependency / 의존성), credential hoặc lỗi lô-gic (logic / 논리) ở ứng dụng (application / 애플리케이션) tầng (layer / 계층).

> **Chuyển mạch:** Ở chặng này của **Độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) cho hệ thống AI**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Độ tin cậy (reliability / 신뢰성) nối [AI Engineering](../15_ai_engineering/README.md), [LLMOps](../16_mlops_and_llmops/08_llmops.md), [Agent Design](../10_agents_and_ai_systems/10_reliable_agent_design.md), [RAG Evaluation](../09_retrieval_and_rag/09_rag_evaluation.md) và [Safety/Security](../19_ai_safety_security_alignment/README.md).

Chapter này là cầu trực tiếp từ evaluation sang bảo mật (security / 보안): độ tin cậy (reliability / 신뢰성) xử lý lỗi ngẫu nhiên và vận hành; bảo mật (security / 보안) bổ sung mô hình đối thủ chủ động khai thác hệ thống.

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
