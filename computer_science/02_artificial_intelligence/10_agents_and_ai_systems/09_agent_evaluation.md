# Đánh giá Agent

Đánh giá **tác nhân AI (AI agent)** khó hơn đánh giá một phản hồi đơn lẻ vì agent tạo ra **quỹ đạo thực thi (trajectory)** gồm nhiều quyết định, lời gọi công cụ, thay đổi trạng thái và side effect. Một final answer đúng vẫn có thể đến từ trajectory nguy hiểm; ngược lại một task thất bại có thể do tool outage, stale state hoặc permission chứ không phải do reasoning của model.

Vì vậy evaluation cần đồng thời nhìn:

```text
step-level
trajectory-level
end-to-end task-level
system-level
```

## Kiến thức cần có trước

Nên đọc [Tool Calling](./01_tools_and_function_calling.md), [Agent Loop](./02_agent_loop.md), [Planning](./03_planning_and_task_decomposition.md), [Agent State](./05_agent_state_and_context.md), [RAG Evaluation](../09_retrieval_and_rag/09_rag_evaluation.md) và [LLM Evaluation](../08_large_language_models/14_llm_evaluation.md).

## Hợp đồng đánh giá Agent

Trước khi chạy benchmark, cần xác định:

```text
goal là gì?
acceptance criterion là gì?
agent được phép dùng tool nào?
state ban đầu là gì?
side effect nào được phép?
stop condition là gì?
maximum budget về step/token/cost/time là bao nhiêu?
property nào là hard invariant?
```

Nếu không cố định những yếu tố này, hai run không thực sự đang giải cùng một task.

## Thành công End-to-End

Metric quan trọng nhất là task có thực sự đạt acceptance criterion hay không.

Ví dụ với coding task:

```text
required tests pass
không có regression
requested behavior đã được implement
scope constraint được giữ đúng
```

Không dùng self-report kiểu “đã xong” của mô hình làm ground truth.

## Step-level Evaluation

Mỗi quyết định có thể được kiểm tra:

- có chọn đúng tool không?
- argument có đúng schema và semantics không?
- có gọi tool không cần thiết không?
- observation có được diễn giải đúng không?
- retry có phù hợp error class không?
- dangerous action có bị runtime chặn đúng không?

Step metric giúp xác định failure đầu tiên thay vì chỉ thấy task cuối cùng thất bại.

## Trajectory Evaluation

Hai agent đều có thể hoàn thành task nhưng trajectory khác nhau:

```text
Agent A: 5 step, 1 retry, có verification
Agent B: 27 step, search lặp lại, ghi nhầm rồi rollback
```

Final success không phản ánh đầy đủ efficiency và risk.

Các metric có thể gồm:

```text
step count
tool-call count
repeated-action rate
cost
latency
rollback count
approval count
unnecessary mutation count
```

## Trực giác toán học về xác suất thành công theo horizon

Nếu mỗi critical step có xác suất thành công xấp xỉ `p` và coi đơn giản các bước độc lập, một task dài `H` bước có xác suất hoàn tất gần:

\[
P(success)\approx p^H
\]

Đây không phải mô hình chính xác cho mọi agent, nhưng cho trực giác quan trọng: **sai số nhỏ ở mỗi bước có thể khuếch đại mạnh khi horizon dài**.

Ví dụ nếu `p=0.98`:

\[
0.98^{20}\approx0.67
\]

Nghĩa là reliability của long-horizon task không thể suy ra trực tiếp từ accuracy một bước. Đây là lý do cần decomposition, checkpoint, verifier và recovery.

## Hiệu quả và Economics

Có thể định nghĩa utility có điều chỉnh resource:

\[
E=\frac{utility}{cost+\lambda\,latency+\mu\,steps}
\]

Không có công thức universal. Mục tiêu là làm rõ trade-off giữa outcome và resource.

Production nên theo dõi **cost per verified successful task**, không chỉ cost/request.

## Độ chính xác khi dùng Tool

Nên tạo test case mà tool đúng và argument đúng đã biết trước. Đo:

```text
tool selection accuracy
argument validity
semantic correctness
permission compliance
unnecessary tool-call rate
recovery correctness
```

Một JSON hợp schema nhưng gọi nhầm account hoặc operation vẫn là lỗi nghiêm trọng.

## Đánh giá Planning

Plan nên được kiểm tra theo:

```text
coverage của subtask bắt buộc
dependency correctness
executability
risk ordering
verification coverage
khả năng thích nghi sau failure
```

Một plan viết đẹp nhưng chứa tool không tồn tại hoặc step không thể thực thi vẫn là plan thất bại.

## Đánh giá Retrieval trong Agent

Research agent cần đo cả:

```text
source recall
citation correctness
source authority
claim–evidence alignment
unsupported claim rate
freshness
ACL compliance
```

Nếu agent dùng RAG như một subroutine, failure taxonomy nên giữ được stage retrieval riêng thay vì gộp chung thành “reasoning error”.

## Đánh giá Memory và State

Có thể đo:

- recall khi retrieve memory liên quan;
- stale fact usage;
- contradiction rate;
- unauthorized memory access;
- memory write precision;
- harmful persistence;
- token cost do memory gây ra.

State evaluation còn cần kiểm:

```text
resume có đúng sau crash không?
retry có lặp side effect không?
concurrent update có gây lost update không?
version/state transition có hợp lệ không?
```

## Safety và Security Evaluation

Scenario suite nên có:

```text
direct prompt injection
indirect injection qua document/web/tool output
privilege escalation
destructive action request
data exfiltration
ambiguous approval
conflicting instruction
compromised tool output
cross-tenant access attempt
```

Safety test phải verify runtime boundary và permission behavior, không chỉ xem mô hình có viết câu từ chối hay không.

## Môi trường kiểm thử có thể replay

Agent eval nên chạy trên simulator hoặc sandbox có trạng thái kiểm soát được:

```text
fake email server
test database
mock filesystem
sandbox API
versioned document corpus
```

Mỗi case cần một **environment snapshot** xác định:

```text
initial state
available tools
tool versions
credentials / permissions
network conditions
expected invariants
```

Nhờ vậy failure có thể replay thay vì biến mất vì production state đã đổi.

## State Snapshot và Event Log

Một run nên lưu:

```text
agent/model/prompt version
initial state snapshot
mỗi tool proposal
validation/authorization result
tool response
state transition
approval event
final state
final answer
```

Natural-language transcript không đủ để tái tạo workflow có side effect.

## Scenario-based Evaluation

Agent task có nhiều biến thể nên xây scenario dataset:

```text
normal success
missing information
transient tool failure
permission denied
conflicting records
stale state
user đổi goal giữa task
malicious retrieved content
partial side effect
service timeout
```

Mỗi scenario nên có expected invariant và acceptance criterion rõ.

## Invariant-based Scoring

Không phải lúc nào cũng cần exact trajectory. Agent có thể tìm đường đi khác nhau miễn giữ invariant:

```text
không write trước approval
không vượt budget
không truy cập ngoài tenant
phải verify sau mutation
không lặp payment khi retry
factual claim cần citation nếu policy yêu cầu
```

Invariant đặc biệt hữu ích khi đánh giá agent tự chủ vì trajectory hợp lệ có thể không duy nhất.

## Đánh giá tính ngẫu nhiên của trajectory

Sampling, tool latency hoặc search result có thể làm cùng một task sinh trajectory khác nhau. Vì vậy với critical case nên chạy nhiều lần.

Nếu `S_i` là 1 khi run thứ `i` hoàn tất task an toàn và 0 nếu không:

\[
\hat p=\frac{1}{n}\sum_i S_i
\]

`\hat p` ước lượng **verified success probability**. Nên theo dõi thêm variance của cost, step count và latency, vì một agent “thường nhanh nhưng thỉnh thoảng loop 100 bước” là production risk thật.

## Fault Injection

Để đánh giá recovery, simulator có thể chủ động tạo lỗi:

```text
TIMEOUT
RATE_LIMITED
TRANSIENT_FAILURE
CONFLICT
STALE_VERSION
PARTIAL_RESULT
```

Agent phải phân biệt retryable và non-retryable error. Retry mù mọi lỗi thường làm reliability kém hơn.

## LLM-as-a-Judge

LLM judge hữu ích cho relevance, style hoặc completeness, nhưng không nên là evaluator duy nhất cho factual, tool hoặc state correctness.

Deterministic check nên giữ vai trò anchor cho:

```text
file tồn tại?
transaction có đúng state?
schema hợp lệ?
permission có đúng?
test có pass?
```

## Human Evaluation

Human evaluation cần thiết với task chủ quan hoặc rủi ro cao. Rubric phải đủ rõ để inter-rater agreement có ý nghĩa.

Disagreement giữa evaluator cũng là tín hiệu: task có thể mơ hồ, policy chưa rõ hoặc evidence chưa đủ.

## Regression Testing

Mọi thay đổi model, prompt, tool schema, workflow graph hoặc retrieval pipeline đều có thể làm behavior đổi.

Cần lưu **behavior bundle**:

```text
model + prompt + tools + schemas + workflow + retrieval + policy
```

và chạy cùng regression suite trước khi promote.

## Online Evaluation

Metric production có thể gồm:

```text
verified task completion rate
user correction rate
human escalation
abort / cancel rate
cost per task
p95 / p99 latency
unsafe-action block rate
incident rate
retry/loop rate
```

A/B test cần guardrail metric, không chỉ tối ưu số task completed.

## Failure Taxonomy

Nên tag failure theo layer:

```text
MODEL_REASONING
TOOL_SELECTION
TOOL_ARGUMENT
TOOL_EXECUTION
STATE_STALE
STATE_CONFLICT
RETRIEVAL_MISS
PERMISSION
PLANNING
VERIFICATION_MISS
ORCHESTRATION
USER_AMBIGUITY
BUDGET_EXCEEDED
```

Taxonomy giúp biết cần sửa model, prompt, tool, data hay runtime.

## Credit Assignment

Task thất bại sau 20 step tạo bài toán credit assignment: step nào gây lỗi gốc?

Structured trace, state snapshot và event log giúp xác định causal chain tốt hơn so với đọc transcript bằng mắt.

## Benchmark Leakage

Public agent benchmark có thể xuất hiện trong training data hoặc bị tối ưu quá mức. Internal realistic task thường phản ánh production distribution tốt hơn.

Nên giữ cả benchmark chuẩn để so sánh và private eval để đo generalization.

## Failure mode của hệ thống đánh giá Agent

**Chỉ chấm final answer.** Bỏ qua trajectory nguy hiểm.

**Không snapshot environment.** Run không thể replay.

**Tool mock quá đơn giản.** Agent pass benchmark nhưng fail với lỗi thật như timeout/conflict.

**Judge chấm cả property xác định.** Dùng LLM để “đoán” transaction state thay vì đọc state thật.

**Không test horizon dài.** Agent trông tốt ở task 2 bước nhưng sụp ở workflow 20 bước.

**Không pin tool/workflow version.** Score thay đổi mà không biết vì code hay model.

## Production Release Gate

Một flow hợp lý:

```text
candidate behavior bundle
→ deterministic tool/state tests
→ scenario replay
→ stochastic repeated runs cho critical cases
→ security/invariant suite
→ cost/latency budget
→ shadow/canary
→ online monitoring
→ promote hoặc rollback
```

Mọi incident đáng kể nên quay lại thành scenario regression mới.

## Mô hình tư duy

> **Agent evaluation phải đo outcome, trajectory, invariants, recovery và economics cùng lúc.**

Một demo thành công chỉ chứng minh hệ thống *có thể* hoạt động trong một trường hợp; nó không chứng minh reliability distribution của production workload.

## Những nhầm lẫn thường gặp

### “Model benchmark cao thì agent chắc chắn tốt”

Không. Agent quality còn phụ thuộc tool, state, orchestration, retrieval và environment.

### “Final answer đúng là đủ”

Không. Trajectory có thể vi phạm permission hoặc tạo side effect sai rồi mới rollback.

### “LLM judge thay thế được test”

Không đối với property xác định như file existence, transaction state, schema validity hoặc permission.

### “Một successful run chứng minh agent reliable”

Không. Cần đo phân phối behavior qua nhiều scenario và nhiều run.

## Liên kết kiến thức

Agent evaluation nối [Tool Calling](./01_tools_and_function_calling.md), [Agent State](./05_agent_state_and_context.md), [RAG Evaluation](../09_retrieval_and_rag/09_rag_evaluation.md), [Evaluation Foundations](../18_evaluation_reliability_interpretability/00_evaluation_foundations.md), [Reliability Engineering](../18_evaluation_reliability_interpretability/07_reliability_engineering.md) và [LLMOps](../16_mlops_and_llmops/08_llmops.md).

Xem tiếp: [Thiết kế Agent đáng tin cậy](./10_reliable_agent_design.md).