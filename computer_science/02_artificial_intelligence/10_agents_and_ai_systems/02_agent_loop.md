# Agent Loop

Agent loop là cơ chế biến một goal lớn thành chuỗi observation–decision–action lặp lại. Không có loop, tool calling thường chỉ là một lần gọi hàm; có loop, system phải quản lý state, termination, retries, budgets và verification qua nhiều bước.

Một loop cơ bản:

```text
initialize task state
while not done:
    observe(state)
    decide(next_action)
    validate(action)
    execute(action)
    record(result)
    verify(progress)
```

## Observe

Observation không chỉ là tool output cuối. Nó có thể gồm:

- current structured state;
- latest tool result;
- outstanding subtasks;
- previous failures;
- budget còn lại;
- approval status;
- environment changes.

Nếu observation thiếu hoặc stale, decision sau sai dù reasoning logic tốt.

## Decide

Model có thể chọn:

```text
call tool
ask user
revise plan
retry with changed arguments
verify
finish
```

Decision space nên explicit. Nếu model chỉ được prompt “hãy tiếp tục”, stopping behavior khó kiểm soát.

## Act

Action execution phải qua control plane. Agent không nên tự bypass policy bằng cách encode action trong free-form text.

## Verify

Sau execution, system cần kiểm progress dựa trên evidence.

Ví dụ coding agent không nên dừng vì model nói “đã sửa xong”; phải chạy test, inspect diff hoặc check acceptance criteria.

```text
claim of success ≠ verified success
```

## Termination

Stop conditions có thể gồm:

- success criterion satisfied;
- max steps reached;
- token/cost budget exceeded;
- repeated identical failure;
- unrecoverable error;
- human approval required;
- confidence/evidence insufficient.

Không có stop rule, agent có thể loop indefinitely.

## ReAct mental model

Một common pattern là alternating reasoning/action/observation. Dù implementation không expose chain-of-thought, conceptual cycle vẫn hữu ích:

```text
assess state → choose action → receive observation → reassess
```

Điểm quan trọng không phải format prompt mà là closed-loop control.

## Retry policy

Retry phải phụ thuộc error class.

```text
TIMEOUT → retry with backoff
RATE_LIMIT → wait/backoff
INVALID_ARGUMENT → revise arguments
PERMISSION_DENIED → stop/escalate
CONFLICT → refetch state then decide
```

Blind retry vừa tốn cost vừa có thể tạo side effect duplicate.

## Backoff và jitter

Distributed tools thường cần exponential backoff:

\[
t_k=\min(t_{max},t_0 2^k)+\epsilon
\]

`ε` là jitter để tránh nhiều workers retry đồng thời.

## Loop detection

Agent có thể lặp cùng thought/action sequence.

Detection signals:

- same tool + same args repeated;
- state hash không đổi;
- same error lặp lại;
- no improvement in progress metric.

Runtime có thể force replanning hoặc terminate.

## Checkpointing

Long task cần checkpoint persisted:

```text
completed steps
current artifacts
external resource ids
pending approvals
next intended action
```

Nhờ đó process restart không cần replay toàn bộ conversation.

## Event sourcing

Một robust pattern là append immutable events:

```text
TaskCreated
PlanUpdated
ToolCalled
ToolSucceeded
ApprovalRequested
ApprovalGranted
TaskCompleted
```

Current state có thể derive từ event log. Điều này hỗ trợ audit, replay và debugging.

## Concurrency

Nếu agent chạy nhiều subtasks song song, shared state cần consistency strategy.

Hai workers có thể cùng update same resource. Cần optimistic locking, version check hoặc coordinator.

Agent orchestration không loại bỏ distributed-systems problems.

## Budget như một control variable

Budget có thể gồm:

```text
max model calls
max tokens
max wall-clock time
max tool cost
max external writes
```

Policy có thể thay đổi model hoặc search depth khi budget gần cạn.

## Recovery

Recovery không phải luôn “retry”. Có thể:

- rollback;
- compensate;
- switch tool/provider;
- reduce scope;
- ask user;
- continue from partial success.

## Deterministic shell quanh probabilistic core

Một design mạnh:

```text
Deterministic runtime owns:
state
permissions
budgets
retries
logging
termination

LLM owns:
semantic interpretation
planning suggestion
next-action choice within allowed space
```

Đây là separation of concerns quan trọng.

## Example: research agent

Task: so sánh 3 vendors.

Loop có thể:

```text
1. parse evaluation criteria
2. search vendor A/B/C
3. fetch primary sources
4. detect missing criterion
5. search targeted evidence
6. build structured comparison
7. verify citations
8. finalize
```

Nếu step 4 phát hiện thiếu pricing, agent cần loop retrieval thay vì generate từ memory.

## Example: coding agent

```text
inspect issue
→ search relevant code
→ read tests
→ edit
→ run focused tests
→ inspect failure
→ revise
→ run broader tests
→ inspect diff
→ finish
```

Verification actions là một phần của loop, không phải post-processing tùy chọn.

## Mental Model

> **Agent loop là feedback controller cho một policy không hoàn hảo.**

Open-loop plan giả định world diễn ra đúng dự kiến; closed-loop agent liên tục quan sát và điều chỉnh.

## Common Misconceptions

### “Plan một lần rồi execute hết là agent tốt”

Environment thay đổi và tool có thể fail. Replanning dựa observation mới thường cần thiết.

### “More steps means more intelligence”

Nhiều bước có thể chỉ là dithering. Quality nằm ở progress per step và verification.

### “Conversation history chính là state”

Transcript có thể chứa state, nhưng structured persisted state đáng tin và queryable hơn.

## Knowledge Connection

Agent loop nối control theory intuition, state machines, distributed systems và classical agent architecture. Phần tiếp theo tập trung vào cách phân rã goal thành plan có thể thực thi.

Xem tiếp: [Planning and Task Decomposition](./03_planning_and_task_decomposition.md).