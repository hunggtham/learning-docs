# Workflow và Agent khác nhau như thế nào?

Hai từ này thường bị dùng như synonym nhưng chúng đại diện hai cách phân bổ quyền quyết định khác nhau.

**Workflow (워크플로 / quy trình)** có control flow chủ yếu được developer định nghĩa trước. **Agent** cho model quyết định nhiều hơn về next step dựa trên state/observation hiện tại.

```text
Workflow:
step A → if X then B else C → D

Agent:
observe state → choose among allowed actions → observe result → repeat
```

## Determinism vs Flexibility

Workflow mạnh khi process ổn định, auditability cao và branching logic biết trước.

Agent mạnh khi:

- input không có schema cố định;
- task có nhiều đường giải;
- cần interpret natural language;
- environment không predictable;
- action sequence khó encode hết bằng rules.

Không nên dùng agent chỉ vì “AI mới hơn”.

## Hybrid Architecture

Thiết kế production thường tốt nhất:

```text
Deterministic workflow shell
      ↓
Agentic decision at ambiguous node
      ↓
Deterministic validation / execution
```

Ví dụ claims processing:

```text
receive claim
→ validate required fields [deterministic]
→ classify unusual narrative [LLM]
→ retrieve policy [deterministic/RAG]
→ decide whether human review needed [policy + model]
→ payment execution [deterministic + approval]
```

## Why Workflow is Easier to Test

Vì transitions known trước, unit/integration tests có thể cover branches rõ hơn.

Agent behavior stochastic hơn; evaluation cần scenario suites và trajectory analysis.

## Reliability Composition

Workflow có fewer model decisions nên giảm compounded uncertainty. Nếu deterministic step có correctness gần 1 và chỉ 2 agentic decisions thay vì 10, end-to-end reliability thường tốt hơn.

## Cost

Agent loop gọi model nhiều lần. Workflow có thể gọi model đúng nơi cần semantic intelligence.

Optimization principle:

> **Dùng deterministic code cho phần deterministic; dùng model cho phần uncertainty/semantics.**

## Explainability và Audit

Workflow branch rõ giúp explain “vì sao action xảy ra”. Agent cần log state, tool calls, selected evidence và verification results để reconstruct trajectory.

## Failure Isolation

Hybrid system có thể isolate AI failure:

```text
model output invalid
→ fallback deterministic/manual route
```

Nếu toàn bộ application là one giant agent loop, blast radius lớn hơn.

## When to Prefer Workflow

- compliance-heavy process;
- exact financial calculation;
- fixed approval chain;
- repeated ETL/data pipeline;
- known API orchestration;
- state transitions defined by business rules.

## When Agent Adds Value

- open-ended research;
- debugging unknown codebase;
- heterogeneous tool discovery;
- document-heavy case analysis;
- planning under changing observations.

## Agent-in-Workflow Pattern

Một node `AnalyzeCase` có thể internally chạy agent, nhưng outer workflow owns:

```text
timeout
retry
approval
state
SLA
next deterministic step
```

## Workflow-in-Agent Pattern

Agent có thể invoke a known workflow as one high-level tool:

```text
agent decides “run onboarding workflow”
→ workflow engine executes 12 deterministic steps
→ returns result
```

Đây thường tốt hơn để agent gọi 12 low-level APIs riêng.

## State Ownership

Workflow engine nên own durable process state. Agent context chỉ nhận relevant view.

## Mental Model

> **Workflow quyết định đường đi trước; Agent quyết định đường đi trong lúc chạy. Hybrid system chọn đúng mức autonomy cho từng đoạn.**

## Common Misconceptions

### “Agent thay thế workflow engine”

Không. Scheduling, persistence, retry và transactional orchestration vẫn là systems problems.

### “Workflow không phải AI”

Workflow có thể chứa ML/LLM nodes. AI vs workflow là khác axis.

### “More agentic = more capable”

More autonomy cũng nghĩa more variance, cost và risk.

## Knowledge Connection

Phân biệt này là nền cho system design ở các chapter orchestration và reliability.

Xem tiếp: [Multi-Agent Systems](./07_multi_agent_systems.md).