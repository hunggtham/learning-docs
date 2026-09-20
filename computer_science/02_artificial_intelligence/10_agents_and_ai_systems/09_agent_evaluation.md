# Agent Evaluation

Đánh giá agent khó hơn đánh giá single model response vì agent tạo **trajectory** gồm nhiều decisions, tool calls và state transitions. Một final answer đúng có thể đến từ trajectory nguy hiểm; một task fail có thể do tool outage chứ không phải model reasoning.

Do đó evaluation cần nhiều level:

```text
step-level
trajectory-level
end-to-end task-level
system-level
```

## End-to-End Task Success

Metric quan trọng nhất là task có đạt acceptance criteria thật không.

Ví dụ coding task:

```text
required tests pass
no regression
requested behavior implemented
scope constraints respected
```

Không dùng self-reported “done” của model làm ground truth.

## Step-Level Evaluation

Mỗi decision có thể score:

- chọn đúng tool?
- arguments đúng?
- có dùng unnecessary tool?
- observation được interpret đúng?
- retry appropriate?
- dangerous action bị chặn?

Step metrics giúp localize failure.

## Trajectory Evaluation

Hai agents đều hoàn thành task nhưng trajectory khác:

```text
A: 5 steps, 1 retry, verified
B: 27 steps, repeated searches, accidental write then rollback
```

Final success alone không capture efficiency/risk.

Trajectory metrics:

```text
step count
tool calls
repeated-action rate
cost
latency
rollback count
approval count
unnecessary mutation count
```

## Efficiency

Có thể define normalized efficiency:

\[
E = \frac{utility}{cost + \lambda latency + \mu steps}
\]

Không có universal formula; mục đích là make trade-off explicit.

## Tool-Use Accuracy

Create test cases mà correct tool/arguments known. Measure:

- tool selection accuracy;
- argument validity;
- semantic correctness;
- permission compliance.

## Retrieval/Research Agents

Ngoài answer quality cần:

- source recall;
- citation correctness;
- source authority;
- claim–evidence alignment;
- unsupported claim rate.

## Agentic Coding

Metrics có thể:

- tests passed;
- patch correctness;
- regression rate;
- files changed beyond scope;
- compile/lint;
- security/static-analysis issues;
- number of failed attempts.

## Planning Evaluation

Plan score theo:

```text
coverage of required subtasks
dependency correctness
executability
risk ordering
verification coverage
adaptability after failure
```

Một plan prose đẹp nhưng chứa non-existent tool là fail.

## Memory Evaluation

Measure:

- relevant memory retrieval recall;
- stale fact usage;
- contradiction;
- unauthorized memory access;
- memory write precision;
- harmful persistence.

## Safety Evaluation

Scenario suites phải test:

- direct prompt injection;
- indirect injection qua documents/web;
- privilege escalation;
- destructive action request;
- exfiltration attempt;
- ambiguous approval;
- conflicting instructions.

Safety test cần verify runtime boundary, không chỉ model refusal text.

## Deterministic Test Environment

Tool/environment nên có simulator/sandbox để repeat trajectories.

Ví dụ fake email server, test database, mock filesystem. Nếu mỗi evaluation run tác động production state, test không reproducible và nguy hiểm.

## Scenario-Based Evaluation

Agent tasks đa dạng nên xây scenario dataset:

```text
normal success
missing information
transient tool failure
permission denied
conflicting records
stale state
user changes goal mid-task
malicious retrieved content
```

Mỗi scenario có expected invariants.

## Invariants

Thay vì yêu cầu exact trajectory, enforce invariants:

```text
must not write before approval
must cite external factual claims
must not exceed budget
must verify after mutation
must preserve user data
```

Agent có thể tìm different valid paths miễn invariants hold.

## LLM-as-Judge

LLM judge hữu ích cho semantic dimensions như relevance/style, nhưng không nên là sole evaluator cho factual/tool correctness.

Risks:

- judge bias;
- self-preference;
- prompt sensitivity;
- poor calibration.

Use deterministic checks và human labels làm anchors.

## Human Evaluation

Cần khi quality subjective hoặc high-stakes. Human rubric phải rõ để inter-rater consistency tốt.

## Regression Testing

Mỗi thay đổi prompt/model/tool schema có thể đổi behavior. Maintain fixed eval suite và compare before/after.

Không chỉ compare average; inspect critical scenario regressions.

## Online Evaluation

Production metrics:

```text
task completion rate
user corrections
human escalation
abort/cancel rate
cost/task
p95 latency
unsafe action blocks
incident rate
```

A/B test cần guardrail metrics, không chỉ user engagement.

## Failure Taxonomy

Tag failures:

```text
MODEL_REASONING
TOOL_SELECTION
TOOL_EXECUTION
STATE_STALE
RETRIEVAL_MISS
PERMISSION
PLANNING
VERIFICATION_MISS
ORCHESTRATION
USER_AMBIGUITY
```

Taxonomy giúp biết nên fix prompt, tool, data hay runtime.

## Credit Assignment

End-to-end failure qua 20 steps tạo challenge: step nào thực sự gây fail? Trace + structured state giúp postmortem.

## Benchmark Leakage

Public agent benchmarks có thể contaminated trong training data. Internal realistic tasks thường cho signal production tốt hơn.

## Reliability Curve theo Horizon

Đo success theo number of required steps. Nếu performance sụt mạnh khi horizon > 5, design cần more decomposition/checkpoints chứ không chỉ average benchmark.

## Cost-aware Evaluation

Model A success 90% với $1/task, model B 92% với $10/task. “Better” phụ thuộc business utility và failure cost.

## Mental Model

> **Agent evaluation phải đo outcome, trajectory, safety và economics cùng lúc.**

Một demo thành công không nói gì về reliability distribution.

## Common Misconceptions

### “Benchmark model cao thì agent sẽ cao”

Agent quality phụ thuộc tools, state, orchestration và environment.

### “Final answer đúng là đủ”

Trajectory có thể vi phạm permission hoặc tạo side effect sai rồi sửa lại.

### “LLM judge thay thế được test”

Không cho deterministic properties như file existence, transaction state hay permission.

## Knowledge Connection

Evaluation nối software testing, observability, statistics và safety engineering. Chapter cuối chuyển các lessons thành design principles cho reliable agents.

Xem tiếp: [Reliable Agent Design](./10_reliable_agent_design.md).