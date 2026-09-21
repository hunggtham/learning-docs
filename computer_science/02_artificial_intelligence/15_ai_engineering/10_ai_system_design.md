# Thiết kế hệ thống AI: từ mô hình tới sản phẩm đáng tin cậy

**Thiết kế hệ thống AI (AI system design / AI 시스템 설계)** là quá trình tổ chức mô hình, dữ liệu, truy xuất, công cụ, state, storage, runtime, quan sát hệ thống và policy thành một sản phẩm có thể vận hành lâu dài. Một kiến trúc tốt không cố nhét toàn bộ “trí thông minh” vào một model duy nhất; nó phân tách trách nhiệm để mỗi thành phần có contract rõ, có thể kiểm thử và có thể thay thế độc lập.

## Kiến thức tiên quyết

Nên đọc trước [RAG](../09_retrieval_and_rag/README.md), [Agents](../10_agents_and_ai_systems/README.md), [Model Serving](./03_model_serving.md), [Latency/Throughput/Cost](./09_latency_throughput_and_cost.md), [LLMOps](../16_mlops_and_llmops/08_llmops.md) và [Reliability Engineering](../18_evaluation_reliability_interpretability/07_reliability_engineering.md).

## Bắt đầu từ Task Contract

Trước khi chọn model, cần định nghĩa:

```text
input là gì?
output contract là gì?
độ trễ mục tiêu là bao nhiêu?
quality target là gì?
error nào chấp nhận được?
error nào buộc phải fail closed?
privacy/security constraint nào phải giữ?
request volume và burst là bao nhiêu?
chi phí tối đa trên mỗi task là bao nhiêu?
```

Nếu output phải là JSON đúng schema, đó là system contract. Nếu câu trả lời phải trích dẫn nguồn, grounding là requirement. Nếu action tạo side effect, authorization, idempotency và verification là requirement.

## Phân tách capability và control

Một kiến trúc production thường có:

```text
User / Upstream
      ↓
API / Gateway
      ↓
Orchestrator
  ├─ Retrieval
  ├─ Model
  ├─ Tools
  ├─ Policy / Security
  ├─ State / Memory
  └─ Verifier
      ↓
Response / Action
      ↓
Logs / Metrics / Evaluation
```

Model cung cấp capability xác suất. Runtime sở hữu control flow, permission, timeout, retry, budget, state và audit.

## Deterministic Shell, Probabilistic Core

Một pattern bền vững:

```text
validation xác định
→ mô hình xác suất
→ verification / policy xác định
```

LLM có thể đề xuất query, SQL hoặc action, nhưng parser, schema checker, permission system và executor mới quyết định action có được thực thi hay không.

Prompt không phải security boundary.

## RAG, Fine-Tuning và Tooling giải quyết bài toán khác nhau

```text
RAG       → kiến thức ngoài model hoặc cần cập nhật
Fine-tune → điều chỉnh behavior, style hoặc task distribution
Tooling   → truy cập action, computation hoặc live system
```

Nếu requirement là “đọc dữ liệu database hôm nay”, fine-tuning không phải abstraction phù hợp. Nếu requirement là output style ổn định, RAG một mình cũng chưa đủ.

## Mô hình triển khai đồng bộ và bất đồng bộ

Không phải mọi task nên nằm trong một request/response đồng bộ.

```text
chat ngắn / classification
→ synchronous path

tài liệu lớn / video / agent dài
→ create task
→ queue
→ worker
→ persisted state
→ poll / event / callback
```

Task dài cần durable state và cancellation. Giữ một HTTP connection quá lâu làm retry, timeout và recovery khó kiểm soát.

## Request Envelope

Một request production nên mang metadata đủ để trace và enforce policy:

```text
request_id
user / tenant identity
task type
deadline
model/policy version
budget
idempotency key nếu có write
```

Nhờ đó timeout, cost, authorization và audit không phụ thuộc vào text prompt.

## Stateless và Stateful Service

State cần được biểu diễn tường minh:

- session/conversation state;
- workflow state;
- durable memory;
- user preference;
- transaction state;
- approval state.

Không nên dựa vào việc model “nhớ” trong context nếu workflow cần resume, retry hoặc chạy trên worker khác.

## Side Effect và Idempotency

Tool tạo payment, email, order hoặc deploy phải có transaction semantics hoặc idempotency key.

```text
plan
→ validate
→ authorize
→ execute với idempotency
→ verify outcome
→ persist state
```

Retry request không được tạo side effect mới ngoài ý muốn.

## Optimistic Concurrency cho State Mutable

Nếu resource có thể thay đổi song song:

```text
read version 10
→ model đề xuất update
→ commit chỉ khi vẫn là version 10
```

Nếu resource đã là version 11, runtime trả conflict để Agent đọc lại và replan. Điều này ngăn mutation dựa trên state lỗi thời.

## Model Routing

Không phải request nào cũng cần model lớn nhất.

```text
classifier/router
→ task dễ: small model
→ task khó: large model
→ search: embedding + reranker
→ image: vision model
→ deterministic calculation: tool
```

Router có thể dựa trên task type, quality requirement, latency budget, token length hoặc risk class.

Trade-off: routing tiết kiệm cost nhưng thêm một failure point. Router sai có thể làm task khó bị đưa sang model không đủ khả năng.

## Cascade

Một cascade có thể dùng model rẻ trước:

```text
small model
→ nếu đủ confidence / verifier pass: kết thúc
→ nếu không: escalate sang model mạnh hơn
```

Cascade hiệu quả khi có criterion đáng tin để quyết định “đủ tốt”. Nếu criterion yếu, hệ thống có thể tiết kiệm tiền nhưng tăng silent failure.

## Caching

Có nhiều lớp cache:

```text
exact request cache
retrieval cache
embedding cache
prefix / prompt cache
semantic cache
```

Cache key phải bao gồm những version ảnh hưởng semantics: model, prompt, tenant, index, policy hoặc tool state khi cần.

Semantic cache có rủi ro trả kết quả cũ cho query “gần giống nhưng khác ý”, vì vậy nên dùng cho domain ít thay đổi và có invalidation strategy rõ.

## Backpressure và Admission Control

Khi GPU hoặc provider quá tải, queue dài vô hạn thường làm p99 latency tệ hơn và gây retry storm.

Hệ thống cần:

```text
queue limit
priority
per-tenant concurrency
rate limit
load shedding
```

Mục tiêu là giữ hệ thống trong vùng vận hành ổn định thay vì cố nhận mọi request.

## Deadline Propagation

Nếu end-to-end deadline là 2 giây, từng stage cần budget:

```text
retrieval 300 ms
model 1200 ms
verification 200 ms
network + margin 300 ms
```

Downstream call phải nhận deadline còn lại. Timeout 10 giây ở một dependency là vô nghĩa nếu user chỉ chờ 2 giây.

## Fallback và Graceful Degradation

```text
preferred model
→ fallback model
→ cached/verified result
→ deterministic/manual path
→ explicit failure
```

Fallback phải được evaluate và version hóa. Silent fallback sang model yếu hơn có thể nguy hiểm cho high-risk decision.

## Human-in-the-Loop

Human review phù hợp khi:

- action không thể hoàn tác;
- uncertainty cao;
- policy yêu cầu approval;
- impact lỗi lớn.

Approval point phải nằm trước side effect. UI approval nên hiển thị structured parameters, không chỉ prose do model sinh.

## RAG Architecture

Một pipeline RAG production:

```text
User query
→ authentication / tenant filter
→ query transformation
→ sparse + dense retrieval
→ reranking
→ context packing
→ LLM generation
→ citation / grounding verifier
→ policy
→ response
```

Failure có thể đến từ parser, index stale, ACL filter, retrieval miss, context truncation hoặc unsupported claim. Vì vậy cần component evaluation riêng, xem [RAG Evaluation](../09_retrieval_and_rag/09_rag_evaluation.md).

## Agent Architecture

```text
Goal
→ planner
→ candidate action
→ schema + permission + risk validation
→ execute
→ observe
→ verify
→ persist state
→ continue / stop
```

Agent cần step budget, loop detection, durable state và recovery. Không nên để model tự sở hữu stop policy hoặc permission.

## Evaluation Architecture

Evaluation nên tồn tại ở nhiều cấp:

```text
component eval  → retrieval / model / tool
trajectory eval → Agent steps
end-to-end eval → task success
online eval     → production behavior
```

Mỗi release phải truy được về model, prompt, index, tool schema và policy version.

## Observability

Một trace tốt nên nối:

```text
request
→ retrieval span
→ model span
→ tool span
→ verifier span
→ persistence span
```

Theo dõi:

- p50/p95/p99 latency;
- queue time;
- token count;
- cache hit;
- fallback rate;
- tool error;
- verified success;
- cost/task.

Không log raw secret hoặc PII theo mặc định.

## Capacity Design

Cần ước lượng:

```text
peak QPS
input/output token distribution
concurrency
model memory
KV-cache memory
batching efficiency
headroom khi failover
```

Average traffic không đủ để sizing production. Burst và failover thường quyết định capacity thật.

## Cost Model

Tổng cost/task có thể xem gần đúng:

\[
C_{task}=C_{model}+C_{retrieval}+C_{tool}+C_{infra}+C_{human}
\]

Model rẻ hơn trên mỗi token chưa chắc rẻ hơn trên mỗi task nếu cần retry nhiều hoặc tạo nhiều human escalation.

Mục tiêu nên là **cost per successful task**, không phải chỉ cost per request.

## Deployment Strategy

Thay đổi model hoặc application nên đi qua:

```text
offline eval
→ shadow
→ canary
→ monitor
→ expand traffic
→ rollback nếu gate fail
```

Rollback phải khôi phục behavior bundle tương thích: model + prompt + retrieval config + tool schema khi cần.

## Feedback Loop của Data

Production decision ảnh hưởng dữ liệu tương lai. Recommendation thay đổi nội dung user nhìn thấy; fraud model thay đổi transaction nào được review.

Dữ liệu mới vì vậy không trung tính. Trước retraining cần hiểu selection bias và policy feedback.

## Build hay Buy

Hosted API giảm gánh nặng serving nhưng tăng dependency vào provider. Self-host tăng control nhưng cần expertise về GPU, capacity, security, upgrades và incident response.

Nên quyết định theo:

```text
volume
privacy/compliance
latency
customization
operational capability
provider lock-in risk
```

## Failure Modes xuyên suốt hệ thống

```text
retrieval stale
prompt/config mismatch
model timeout
schema invalid
tool permission error
state conflict
cache poisoning / stale cache
queue saturation
fallback regression
cost runaway
```

Thiết kế tốt phải biết mỗi failure được phát hiện ở đâu, ai sở hữu recovery và fallback nào hợp lệ.

## Security Boundary

AI system mở thêm attack surface: prompt injection, malicious document, tool abuse, exfiltration, poisoned corpus và supply-chain risk.

Security phải nằm trong code, permission, network và policy layer. Xem [Secure AI System Design](../19_ai_safety_security_alignment/08_secure_ai_system_design.md).

## Mô hình tư duy

> **Sản phẩm AI = capability xác suất nằm bên trong một operational contract có tính xác định.**

Model chỉ là một thành phần. Production quality đến từ cách toàn bộ graph giới hạn, quan sát, xác minh và phục hồi lỗi.

## Những nhầm lẫn thường gặp

### “Mô hình tốt hơn sẽ sửa architecture tệ”

Không. Permission sai, retrieval cũ, state lỗi hoặc retry không idempotent vẫn gây failure.

### “Agent framework tự giải quyết reliability”

Không. Framework cung cấp abstraction; state durability, security, evaluation và recovery vẫn là trách nhiệm hệ thống.

### “Production AI chỉ là deploy endpoint”

Không. Production còn có routing, state, lifecycle, monitoring, rollback, data feedback và governance.

### “GPU utilization càng cao càng tốt”

Không. Nếu không còn headroom, burst nhỏ cũng có thể làm tail latency tăng mạnh.

## Liên kết kiến thức

Chapter này nối [RAG](../09_retrieval_and_rag/README.md), [Agents](../10_agents_and_ai_systems/README.md), [Data for AI](../14_data_for_ai/README.md), [Model Serving](./03_model_serving.md), [MLOps / LLMOps](../16_mlops_and_llmops/README.md), [Evaluation](../18_evaluation_reliability_interpretability/README.md), [Reliability](../18_evaluation_reliability_interpretability/07_reliability_engineering.md) và [Security](../19_ai_safety_security_alignment/README.md).