# Agent Orchestration

**Orchestration (오케스트레이션 / điều phối)** là layer quản lý execution của agent/workflow: scheduling, state, queues, retries, budgets, concurrency, approvals, tracing và recovery. Model reasoning không thay thế orchestration.

```text
User / Event
    ↓
Orchestrator
├─ state store
├─ task queue
├─ policy engine
├─ model runtime
├─ tool executors
├─ approval service
└─ observability
```

## Orchestrator owns lifecycle

Một task production có lifecycle:

```text
CREATED
→ RUNNING
→ WAITING_TOOL / WAITING_APPROVAL
→ RUNNING
→ COMPLETED / FAILED / CANCELLED
```

Persist lifecycle giúp restart/resume.

## Queue-Based Execution

Long-running task nên tách request/response HTTP khỏi execution worker.

```text
API creates task
→ queue
→ worker executes
→ events/state persisted
→ client polls/subscribes
```

Điều này hỗ trợ retries, backpressure và horizontal scaling.

## Concurrency Control

Need limits theo:

- tenant;
- user;
- tool/provider;
- model capacity;
- external API rate limits.

Unlimited parallel agents dễ tạo cost explosion hoặc hammer downstream systems.

## Scheduling

Subtasks có dependency DAG. Scheduler chỉ run nodes có prerequisites satisfied.

Priority có thể dựa trên SLA, deadline, critical path hoặc user tier.

## Backpressure

Nếu tool/provider chậm, queue length tăng. System cần backpressure thay vì tiếp tục spawn workers.

Signals:

```text
queue depth
oldest task age
worker utilization
provider error rate
```

## Retry Ownership

Retry policy nên nằm orchestration layer, không chỉ trong prompt.

Model có thể propose semantic retry, nhưng transport/transient retries là runtime concern.

## Approval as First-Class State

Human approval nên persisted event/state:

```text
WAITING_APPROVAL
approval_scope
requested_action
expires_at
approved_by
```

Sau restart vẫn biết task đang chờ gì.

## Cancellation

User cần cancel long task. Runtime phải propagate cancellation tới queued/running tool operations khi có thể.

## Model Routing

Không phải step nào cũng cần strongest model.

Routing có thể chọn:

```text
small model → classification/extraction
large model → ambiguous planning
embedding model → retrieval
specialized model → vision/code
```

Routing là cost-quality optimization problem.

## Tool Routing

Multiple providers cho same capability có thể route theo:

```text
availability
latency
cost
region
compliance
quality
```

Fallback phải preserve semantics; hai APIs cùng tên capability có thể khác contract.

## Artifact Store

Large outputs nên persist artifact, không pass qua every prompt.

```text
artifact id
content hash
metadata
producer step
version
```

Context chỉ carry references/excerpts.

## Event Bus

Events decouple components:

```text
ToolSucceeded
ApprovalGranted
TaskTimedOut
ArtifactCreated
```

Consumers có thể update UI, metrics, audit hoặc trigger next step.

## Exactly-Once là khó

Distributed systems thường không guarantee exactly-once execution đơn giản. Practical design dùng at-least-once delivery + idempotent handlers.

Agent tools vì vậy cần idempotency.

## Checkpoint và Resume

Persist state sau meaningful transition. Khi worker crash:

```text
load checkpoint
inspect last committed side effect
resume from next safe step
```

Không blindly replay whole trajectory.

## Observability

Trace hierarchy:

```text
Task trace
├─ model span
├─ retrieval span
├─ tool span
├─ approval span
└─ verification span
```

Metrics:

- task success;
- latency distribution;
- tokens/cost;
- tool error rate;
- retry count;
- step count;
- human escalation rate.

## Orchestration vs Framework

Framework có thể provide abstractions, nhưng concepts bền vững là state machine, queue, event log, retry, permission và tracing. Library này ưu tiên concepts thay vì phụ thuộc một agent framework cụ thể.

## Example: Enterprise document agent

```text
upload event
→ parse worker
→ retrieval/index worker
→ agent analysis
→ policy validation
→ human approval if sensitive
→ export artifact
→ notify user
```

Đây là distributed workflow có agentic node, không phải single Python loop.

## Mental Model

> **Agent reasoning quyết định “nên làm gì”; orchestration đảm bảo “việc đó được chạy, theo dõi, retry, giới hạn và phục hồi như thế nào”.**

## Common Misconceptions

### “Agent framework đã lo production orchestration”

Nhiều framework chủ yếu lo prompt/tool graph; durability, multi-tenant security và ops vẫn cần architecture riêng.

### “Serverless function loop là đủ”

Task dài có timeout, retries và external side effects cần durable state/workflow semantics.

### “Queue chỉ để scale”

Queue còn là isolation, buffering và retry boundary.

## Knowledge Connection

Orchestration nối agents với distributed systems, backend architecture, queues, event sourcing và observability.

Xem tiếp: [Agent Evaluation](./09_agent_evaluation.md).