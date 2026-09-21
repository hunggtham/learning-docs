# LLMOps: vận hành ứng dụng mô hình ngôn ngữ lớn

**LLMOps** mở rộng MLOps sang các hệ thống dựa trên mô hình ngôn ngữ lớn (Large Language Model — LLM). Điểm khác quan trọng là hành vi của ứng dụng thường không nằm trong một artifact mô hình duy nhất. Nó là kết quả của model, prompt, retrieval, tool, memory, policy, orchestration và evaluator cùng hoạt động.

Vì vậy đơn vị cần version hóa trong LLMOps không phải chỉ là “model”, mà là **gói hành vi (behavior bundle)** của toàn application.

## Kiến thức tiên quyết

Nên đọc trước [RAG](../09_retrieval_and_rag/README.md), [Agent Systems](../10_agents_and_ai_systems/README.md), [AI System Design](../15_ai_engineering/10_ai_system_design.md), [Evaluation](../18_evaluation_reliability_interpretability/00_evaluation_foundations.md) và [Secure AI System Design](../19_ai_safety_security_alignment/08_secure_ai_system_design.md).

## Behavior Bundle

Một version ứng dụng LLM nên xác định đầy đủ:

```text
base model / provider + version
system prompt
prompt templates
sampling parameters
embedding model
chunking / parser / index version
retriever / reranker config
context packing policy
tool schemas
agent/workflow graph
memory policy
security/safety policy
evaluation suite
```

Chỉ cần một thành phần đổi, hành vi đầu-cuối có thể đổi dù model weights giữ nguyên.

## Lineage của một request

Mỗi request production nên truy được về:

```text
request_id
application release
model version
prompt version
retrieval/index version
tool schema version
policy version
memory/context version khi cần
evaluator/verifier version
```

Lineage này giúp trả lời “tại sao hôm nay cùng câu hỏi lại ra kết quả khác tuần trước?”.

## Prompt Versioning

Prompt nên được xem như code/config có lifecycle:

```text
draft
→ review
→ offline eval
→ canary/shadow
→ production
→ rollback/archive
```

Không nên sửa production prompt trực tiếp trong UI mà không có audit trail. Prompt diff phải đi cùng kết quả evaluation để biết thay đổi nào tạo regression.

## Provider Drift

Hosted model có thể được provider cập nhật hoặc alias `latest` có thể thay đổi behavior.

Khi có thể, nên pin version. Nếu không thể pin, cần:

- lưu provider/model metadata;
- giữ golden/regression set;
- chạy canary định kỳ;
- theo dõi tool/schema adherence;
- có fallback hoặc rollback strategy.

Provider abstraction không loại bỏ drift; nó chỉ đổi nơi drift xuất hiện.

## Release dựa trên Evaluation

Generative output không hoàn toàn deterministic nên exact-string unit test thường quá giòn. Release gate nên kết hợp:

```text
semantic correctness
groundedness
citation support
schema validity
tool selection
security cases
latency
cost
```

Nên dùng deterministic validator cho property kiểm trực tiếp được, human/reference set cho quality cần judgment và model-based evaluator khi đã hiểu bias của evaluator.

## Golden Set, Hidden Set và Production Set

**Golden set** phù hợp cho regression thường xuyên.

**Hidden/holdout set** giảm nguy cơ overfit vào bộ test quen thuộc.

**Production-derived set** phản ánh workload mới xuất hiện.

Một hệ thống trưởng thành cần cả ba thay vì chỉ giữ một benchmark tĩnh.

## Eval Tiering

Để cân bằng chi phí:

```text
Tier 1: nhanh/rẻ, chạy mỗi commit
Tier 2: behavioral + RAG/tool, chạy trước release
Tier 3: safety/red-team + human eval, chạy định kỳ hoặc trước thay đổi lớn
Tier 4: shadow/canary online
```

Không cần chạy bộ đánh giá đắt nhất cho mọi thay đổi nhỏ.

## RAGOps

RAG có lifecycle riêng:

```text
source ingestion
→ parser
→ chunking
→ embedding
→ index build
→ metadata / ACL
→ retrieval
→ reranking
→ context packing
```

Mọi stage có thể tạo regression. Ví dụ model không đổi nhưng parser mới làm mất heading, khiến chunking và retrieval giảm chất lượng.

## Index Lineage và Freshness

Cần biết:

```text
index được build từ source snapshot nào?
parser/chunker version nào?
embedding version nào?
ACL metadata version nào?
index build hoàn tất khi nào?
```

Index stale là failure production ngay cả khi model endpoint hoàn toàn khỏe.

## Retrieval Regression

Generation quality giảm có thể bắt nguồn từ retrieval.

Nên đo riêng:

- Recall@k;
- MRR / nDCG;
- tỷ lệ retrieval rỗng;
- tỷ lệ relevant context;
- citation support;
- ACL-filter correctness;
- index freshness.

Xem [RAG Evaluation](../09_retrieval_and_rag/09_rag_evaluation.md).

## AgentOps

Agent thêm trajectory động:

```text
planner decisions
tool calls
state transitions
retry / loop
human approvals
side effects
verification
```

Version Agent phải bao gồm workflow graph, tool schema, state policy và budget, không chỉ prompt.

## Durable Trace cho Agent

Trace nên đủ để reconstruct:

```text
state trước step
action được đề xuất
policy decision
tool result
state sau step
verification
cost / latency
```

Raw chain-of-thought không phải requirement vận hành; structured event và decision metadata mới là phần cần cho debugging/audit.

## Tool Schema Evolution

Nếu API/tool đổi field hoặc semantics, LLM có thể vẫn sinh argument theo contract cũ.

Cần:

```text
schema version
compatibility test
migration window
fallback behavior
deprecation policy
```

Tool contract nên được quản lý giống normal API contract.

## Memory Lifecycle

Persistent memory là một data store và cần:

- write policy;
- retrieval policy;
- provenance;
- TTL/retention;
- correction/delete semantics;
- tenant/user scope;
- privacy controls.

Memory write từ model không nên được coi là truth mặc định. Xem [Agent Memory](../10_agents_and_ai_systems/04_agent_memory.md).

## Cache và Version Awareness

Prompt cache, exact cache, semantic cache và retrieval cache đều có invalidation problem.

Cache key có thể cần chứa:

```text
model version
prompt version
index version
policy version
tenant/user scope
```

Nếu không, release mới có thể tiếp tục trả output được tạo bởi behavior bundle cũ.

## Model Routing và Release

Nếu app route request sang nhiều model, release không chỉ là “một model mới”. Cần version router policy và đánh giá distribution request theo từng route.

Một thay đổi nhỏ trong router có thể làm cost hoặc failure rate tăng mạnh dù từng model không đổi.

## Token, Cost và Budget

Nên theo dõi theo request/task:

```text
input tokens
output tokens
model calls
retrieval calls
tool calls
cache hits
agent steps
human escalation
cost / task
```

Với Agent, `cost per successful task` có ý nghĩa hơn cost mỗi model call.

## Latency Decomposition

Không chỉ đo tổng latency. Trace nên tách:

```text
retrieval
reranking
prefill
decode
tool wait
verification
queue time
```

Nếu p99 tăng, decomposition giúp biết cần tối ưu model, index, tool hay capacity.

## Security trong LLMOps

LLMOps phải theo dõi và kiểm thử:

- prompt injection;
- malicious retrieved content;
- tool abuse;
- cross-tenant retrieval;
- secret leakage;
- memory poisoning;
- policy bypass.

Document được retrieve là dữ liệu không đáng tin mặc định. System prompt không phải security boundary. Xem [Prompt Injection](../19_ai_safety_security_alignment/03_prompt_injection_and_jailbreaks.md).

## Security Regression Suite

Mỗi security incident hoặc bypass quan trọng nên thành regression scenario:

```text
attack case
→ expected security invariant
→ automated evaluation
→ release gate
```

Ví dụ invariant: “tool write không chạy nếu không có approval”, bất kể model output nói gì.

## Monitoring và Observability

Một trace production có thể là:

```text
request
→ prompt assembly
→ retrieval
→ model call
→ tool call
→ model call
→ verifier
→ output
```

Mỗi span nên có latency, cost, error và version metadata.

Không nên log raw prompt/tool result nhạy cảm mặc định; cần redaction, sampling và retention policy.

## Online Quality Signals

Ground truth thường đến trễ. Có thể dùng:

- verified completion;
- user correction;
- human escalation;
- citation verification;
- tool failure;
- business outcome;
- delayed labels.

Proxy signal phải được hiểu là proxy, không phải ground truth tuyệt đối.

## Evaluation Drift

Workload thay đổi theo thời gian. Eval suite cũ có thể không còn đại diện.

Production failure cluster nên quay lại thành test mới:

```text
production issue
→ classify failure
→ create reproducible case
→ add eval
→ fix
→ prevent regression
```

## Incident và Rollback

Rollback phải khôi phục **behavior bundle** tương thích:

```text
model
prompt
retrieval/index config
tool schema
policy
```

Chỉ rollback model có thể không đủ nếu incident đến từ index hoặc tool schema mới.

Xem [Incident Response](./09_incident_response_and_lifecycle.md).

## Canary và Shadow

Shadow cho candidate nhận production-like request nhưng không tác động user.

Canary cho một phần traffic thật sử dụng candidate.

Guardrail cần gồm quality, latency, cost và security signal; không chỉ HTTP error rate.

## Trade-off

LLMOps sâu làm tăng số artifact, version và evaluation cần quản lý. Quá nhiều gate có thể làm release chậm; quá ít gate làm regression khó phát hiện.

Mục tiêu là tăng mức kiểm soát theo risk và complexity của application, không xây platform nặng nề hơn nhu cầu.

## Failure Modes phổ biến

- prompt thay đổi nhưng không version;
- model provider update âm thầm;
- index mới build từ corpus thiếu dữ liệu;
- embedding đổi nhưng index chưa rebuild;
- tool schema thay đổi không có compatibility test;
- semantic cache trả result cũ;
- eval set overfit;
- trace thiếu version metadata;
- Agent loop cost runaway;
- rollback chỉ đổi model nhưng không đổi prompt/index.

## Mô hình triển khai LLMOps

```text
Git / config registry
→ build behavior bundle
→ offline eval
→ artifact/index registry
→ shadow/canary
→ production
→ trace/monitor
→ feedback + incidents
→ eval dataset update
→ next release
```

Đây là một feedback loop vận hành, không phải pipeline một chiều.

## Mô hình tư duy

> **LLMOps là quản lý vòng đời của toàn bộ graph tạo hành vi, không chỉ riêng mô hình ngôn ngữ.**

Nếu không truy vết được model + prompt + retrieval + tool + policy đã tạo một output, hệ thống chưa thật sự reproducible ở cấp application.

## Những nhầm lẫn thường gặp

### “Prompt tốt thì chỉ cần lưu text prompt”

Không. Behavior còn phụ thuộc model, context, retrieval, tool và decoding config.

### “RAG không train model nên không cần MLOps”

Không. Index, data và config vẫn cần versioning, evaluation và monitoring.

### “Agent trace chỉ để debug”

Không. Trace còn cần cho evaluation, security audit, cost attribution và incident response.

### “Dùng hosted API thì provider lo hết operations”

Không. Provider chỉ vận hành model endpoint; application lifecycle vẫn thuộc trách nhiệm của bạn.

## Liên kết kiến thức

LLMOps nối [RAG Evaluation](../09_retrieval_and_rag/09_rag_evaluation.md), [Agent Evaluation](../10_agents_and_ai_systems/09_agent_evaluation.md), [AI System Design](../15_ai_engineering/10_ai_system_design.md), [Evaluation Foundations](../18_evaluation_reliability_interpretability/00_evaluation_foundations.md), [Reliability](../18_evaluation_reliability_interpretability/07_reliability_engineering.md) và [Security](../19_ai_safety_security_alignment/08_secure_ai_system_design.md).