# Reliability Engineering cho hệ thống AI

**Kỹ thuật độ tin cậy (reliability engineering / 신뢰성 공학)** là quá trình thiết kế hệ thống để nó cung cấp hành vi đúng hợp đồng trong thời gian dài, chịu được lỗi, suy giảm có kiểm soát và phục hồi được. Với AI, độ tin cậy không chỉ là service còn chạy; nó còn bao gồm chất lượng quyết định, tính nhất quán của state, mức an toàn của side effect và khả năng phát hiện lỗi âm thầm.

Một mô hình có accuracy cao vẫn có thể tạo hệ thống không đáng tin nếu retrieval lỗi, state stale, tool retry trùng lặp hoặc fallback thay đổi semantics mà không ai biết.

## Kiến thức tiên quyết

Nên đọc trước [AI System Design](../15_ai_engineering/10_ai_system_design.md), [Monitoring và Observability](../16_mlops_and_llmops/06_monitoring_and_observability.md), [Incident Response](../16_mlops_and_llmops/09_incident_response_and_lifecycle.md), [Agent Evaluation](../10_agents_and_ai_systems/09_agent_evaluation.md) và [Nền tảng Evaluation](./00_evaluation_foundations.md).

## Reliability khác Accuracy

Accuracy là một metric thống kê trên một tập dữ liệu. Reliability bao phủ toàn bộ chuỗi:

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

## Mô hình xác suất của thành công đầu-cuối

Một intuition đơn giản cho chuỗi `n` bước quan trọng độc lập, mỗi bước có xác suất thành công `p_i`:

\[
P(success)\approx\prod_{i=1}^{n}p_i
\]

Nếu 20 bước đều có reliability 0.99, xác suất tất cả cùng thành công chỉ khoảng:

\[
0.99^{20}\approx0.818
\]

Thực tế lỗi không độc lập hoàn toàn, nhưng công thức cho thấy vì sao Agent dài hạn cần checkpoint, verification và recovery thay vì chỉ “model tốt hơn”.

## Phân loại failure mode

Nên phân lỗi theo nhiều trục:

```text
transient / persistent
detectable / silent
recoverable / irreversible
local / cascading
model / data / infra / tool / policy / state
```

Mỗi loại cần phản ứng khác nhau. `TIMEOUT` có thể retry; `PERMISSION_DENIED` thường phải dừng; mutation sai có thể cần compensating action.

## Dependency và failure budget

Một request thường phụ thuộc nhiều thành phần:

```text
API
→ retrieval
→ model
→ tool
→ database
→ verifier
```

SLO đầu-cuối không thể tốt hơn dependency yếu nhất nếu không có redundancy hoặc fallback. Vì vậy cần phân bổ **ngân sách lỗi (failure budget)** và **ngân sách độ trễ (latency budget)** cho từng thành phần.

Ví dụ request có deadline 2 giây nhưng retrieval timeout 2 giây thì model và verifier không còn thời gian chạy. Deadline phải được truyền xuống dependency thay vì mỗi service tự đặt timeout tùy ý.

## Queueing và tail latency

Khi utilization tiến gần 100%, queue thường tăng nhanh và p95/p99 latency có thể bùng nổ dù throughput trung bình nhìn vẫn ổn.

Trực giác quan trọng:

```text
capacity gần bão hòa
→ request chờ lâu hơn
→ client timeout / retry
→ tải tăng thêm
→ cascading failure
```

Do đó production AI không nên tối ưu GPU utilization tới mức không còn headroom cho burst, retry hoặc failover.

## Graceful degradation

Khi đường chính không khả dụng, hệ thống có thể giảm capability theo thứ tự có chủ đích:

```text
mô hình chính
→ mô hình dự phòng
→ retrieval-only / deterministic path
→ cache đã xác minh
→ human review
→ thông báo không thể xử lý
```

Fallback phải bảo toàn mức an toàn. Với quyết định rủi ro cao, explicit failure thường tốt hơn fallback âm thầm sang model yếu hơn.

## Fallback phải có semantics rõ

Một anti-pattern là:

```text
primary model lỗi
→ gọi model bất kỳ còn sống
```

Nếu model dự phòng có schema, safety behavior hoặc capability khác, hệ thống có thể “available” nhưng không còn đúng contract.

Fallback nên được version hóa, evaluation riêng và có metric `fallback_rate` để tránh tình trạng degraded mode kéo dài mà không ai nhận ra.

## Redundancy và tính độc lập của lỗi

Replication tăng availability khi các replica không cùng lỗi một nguyên nhân. Hai endpoint dùng chung provider, region hoặc credential có thể cùng chết.

Các dạng redundancy:

- nhiều replica;
- nhiều availability zone;
- nhiều provider;
- index/state store replicated;
- read-only degraded path.

Giá trị của redundancy phụ thuộc mức độc lập của failure domain.

## Circuit breaker

Nếu downstream liên tục lỗi, **cầu dao (circuit breaker)** tạm ngừng gửi request để tránh retry cascade.

```text
CLOSED    → hoạt động bình thường
OPEN      → fail fast
HALF-OPEN → gửi probe kiểm tra recovery
```

Circuit breaker đặc biệt hữu ích với model API, tool API hoặc retrieval service có failure burst.

## Retry có ngân sách

Retry chỉ phù hợp lỗi tạm thời và phải bị giới hạn bởi:

```text
max attempts
deadline
exponential backoff
jitter
retry budget
idempotency
```

Không nên cho từng layer tự retry ba lần độc lập; ba layer lồng nhau có thể nhân số request lên rất nhanh.

## Idempotency cho side effect

Tool ghi dữ liệu như payment, email, order hoặc deploy phải chống thực thi trùng.

Một **idempotency key** gắn với logical action giúp request lặp lại trả cùng kết quả thay vì tạo side effect mới.

Đây là yêu cầu runtime, không thể thay bằng prompt “đừng làm hai lần”.

## Verification trước và sau action

Pattern đáng tin:

```text
model đề xuất
→ schema/policy validation
→ executor thực thi
→ đọc lại state thật
→ verifier kiểm acceptance criterion
```

Các verifier có thể là parser, type checker, unit test, SQL validator, citation checker, policy engine hoặc phép tính xác định.

Đối với Agent, “model nói done” không phải bằng chứng task đã hoàn thành.

## Fail closed và fail open

**Fail closed**: khi không chắc chắn thì không cho action tiếp tục. Phù hợp với security, payment, destructive write hoặc high-risk operation.

**Fail open**: khi dependency lỗi vẫn tiếp tục với degraded behavior. Phù hợp hơn với feature ít rủi ro, ví dụ recommendation phụ.

Lựa chọn phải dựa trên impact của lỗi, không dựa trên mục tiêu availability chung chung.

## Durable state, checkpoint và resume

Workflow dài cần lưu state có cấu trúc:

```text
completed steps
external resource IDs
pending action
approval state
artifacts
verification result
```

Sau crash, runtime tải checkpoint rồi xác định bước tiếp theo an toàn. Không nên replay mù toàn bộ transcript vì các side effect cũ có thể chạy lại.

## Compensation

Không phải distributed workflow nào cũng rollback nguyên tử. Một số task cần **hành động bù trừ (compensating action)**:

```text
reserve inventory → cancel reservation
charge payment    → refund
create resource   → revoke / delete nếu policy cho phép
```

Agent không nên tự phát minh compensation; workflow phải định nghĩa tập hành động hợp lệ và điều kiện dùng chúng.

## Bulkhead và cô lập phạm vi ảnh hưởng

**Bulkhead** tách resource pool để một tenant hoặc workload không làm cạn toàn hệ thống.

Ví dụ:

```text
interactive queue riêng
batch queue riêng
high-risk tools riêng
per-tenant concurrency limit
```

Cô lập giúp giảm **phạm vi ảnh hưởng (blast radius)** khi có lỗi.

## Load shedding và admission control

Khi overload, từ chối hoặc trì hoãn request ít quan trọng thường tốt hơn để tất cả request timeout.

Admission control có thể dựa trên priority, SLA, token budget, queue depth hoặc capacity còn lại.

## SLO và error budget

SLO cho AI có thể bao gồm:

```text
availability
p99 latency
verified task success
maximum unsafe-action rate
retrieval freshness
cost per successful task
```

**Error budget** định lượng mức sai lệch còn chấp nhận được. Khi budget bị dùng hết, team nên ưu tiên reliability thay vì tiếp tục rollout feature mới.

## Reliability cho RAG

RAG có nhiều failure point:

```text
parser lỗi
index stale
metadata filter sai
retrieval miss
reranker sai
context bị cắt
citation không support claim
```

Một production pattern tốt là đo riêng retrieval health, index freshness và grounded answer quality. Xem [RAG Evaluation](../09_retrieval_and_rag/09_rag_evaluation.md).

## Reliability cho LLM

Các control thường dùng:

- structured generation;
- grounding bằng retrieval;
- output validator;
- version pinning;
- timeout và fallback;
- context budget;
- regression evaluation.

Không có control nào tự biến model thành nguồn sự thật. Reliability phải gắn với task-specific evidence.

## Reliability cho Agent

Agent cần thêm:

- step budget;
- durable state;
- permission scope;
- tool validation;
- idempotency;
- verification;
- approval boundary;
- loop detection;
- recovery path.

Mỗi bước tự trị bổ sung là một điểm failure mới. Vì vậy nên dùng deterministic workflow cho những phần đã biết rõ và dành autonomy cho bước thật sự mơ hồ.

## Chaos engineering và game day

Có thể chủ động tiêm lỗi:

- model endpoint mất kết nối;
- retrieval chậm;
- index stale;
- tool trả 500;
- worker crash;
- database conflict;
- quota cạn.

Mục tiêu không phải làm hệ thống hỏng, mà xác nhận fallback, alert và recovery thực sự hoạt động trước incident thật.

## RTO và RPO

**Recovery Time Objective (RTO)** là thời gian chấp nhận được để phục hồi.

**Recovery Point Objective (RPO)** là lượng state/data có thể mất.

Agent có state hoặc workflow dài cần quan tâm cả hai giống hệ thống database truyền thống.

## Mô hình triển khai production

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

Model nằm bên trong control structure; nó không tự sở hữu permission, retry, transaction hay stop policy.

## Trade-off

Reliability không miễn phí. Redundancy tăng chi phí; verifier tăng latency; human approval giảm throughput; timeout ngắn có thể tăng false failure; fallback làm kiến trúc phức tạp hơn.

Mục tiêu là dùng control mạnh nhất ở nơi `P(failure) × Impact(failure)` lớn nhất, không phải thêm mọi control vào mọi request.

## Failure mode của chính cơ chế reliability

Các control cũng có thể gây lỗi:

- retry storm;
- fallback lỗi thời;
- circuit breaker mở quá lâu;
- verifier false positive;
- approval queue bị nghẽn;
- checkpoint không nhất quán;
- monitoring không thấy silent quality regression.

Vì vậy reliability mechanism cũng phải được test và quan sát.

## Mô hình tư duy

> **AI đáng tin cậy = năng lực đủ tốt được đặt bên trong một hệ thống có thể giới hạn, phát hiện và phục hồi lỗi.**

Không cần giả định model hoàn hảo nếu architecture có thể ngăn lỗi lan rộng và xác minh các hành động quan trọng.

## Những nhầm lẫn thường gặp

### “Reliable AI = hallucination thấp”

Hallucination chỉ là một failure mode ở cấp model.

### “Retry càng nhiều càng ổn định”

Không. Retry không giới hạn có thể nhân tải và side effect.

### “Fallback luôn tốt hơn trả lỗi”

Không. Fallback chất lượng thấp cho high-risk action có thể nguy hiểm hơn explicit failure.

### “Multi-provider tự động giải quyết outage”

Không nếu các provider dùng chung dependency, credential hoặc lỗi logic ở application layer.

## Liên kết kiến thức

Reliability nối [AI Engineering](../15_ai_engineering/README.md), [LLMOps](../16_mlops_and_llmops/08_llmops.md), [Agent Design](../10_agents_and_ai_systems/10_reliable_agent_design.md), [RAG Evaluation](../09_retrieval_and_rag/09_rag_evaluation.md) và [Safety/Security](../19_ai_safety_security_alignment/README.md).

Chapter này là cầu trực tiếp từ evaluation sang security: reliability xử lý lỗi ngẫu nhiên và vận hành; security bổ sung mô hình đối thủ chủ động khai thác hệ thống.