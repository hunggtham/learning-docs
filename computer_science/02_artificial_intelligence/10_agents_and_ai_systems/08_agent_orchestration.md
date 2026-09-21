# Điều phối Agent

**Điều phối (orchestration / 오케스트레이션)** là layer quản lý quá trình thực thi của agent hoặc workflow: scheduling, state, queue, retry, budget, concurrency, approval, tracing và recovery. Khả năng reasoning của mô hình không thay thế orchestration.

```text
User / Event
    ↓
Orchestrator
├─ state store
├─ task queue
├─ policy engine
├─ model runtime
├─ tool executor
├─ approval service
└─ observability
```

## Orchestrator sở hữu vòng đời Task

Một task production thường có lifecycle rõ:

```text
CREATED
→ RUNNING
→ WAITING_TOOL / WAITING_APPROVAL
→ RUNNING
→ COMPLETED / FAILED / CANCELLED
```

Persist lifecycle giúp hệ thống restart hoặc resume mà không mất tiến trình.

## Thực thi dựa trên Queue

Task chạy lâu nên tách HTTP request/response khỏi worker thực thi:

```text
API tạo task
→ đưa vào queue
→ worker thực thi
→ event / state được persist
→ client poll hoặc subscribe kết quả
```

Kiến trúc này hỗ trợ retry, backpressure và horizontal scaling tốt hơn một request giữ kết nối lâu.

## Kiểm soát Concurrency

Hệ thống cần giới hạn concurrency theo các chiều như:

- tenant;
- user;
- tool hoặc provider;
- model capacity;
- external API rate limit.

Cho phép agent chạy song song không giới hạn dễ gây bùng nổ chi phí hoặc làm quá tải downstream system.

## Scheduling

Subtask có thể tạo thành dependency graph hoặc DAG. Scheduler chỉ nên chạy node khi prerequisite đã hoàn thành.

Priority có thể dựa trên:

```text
SLA
deadline
critical path
user tier
resource availability
```

Scheduling vì vậy là bài toán systems engineering, không phải nhiệm vụ nên để LLM tự quyết hoàn toàn.

## Backpressure

Nếu tool hoặc provider chậm, queue depth sẽ tăng. Hệ thống cần **backpressure** thay vì tiếp tục spawn worker vô hạn.

Các signal quan trọng gồm:

```text
queue depth
oldest task age
worker utilization
provider error rate
throughput
```

Backpressure có thể dẫn tới giảm admission rate, hạ concurrency, delay task hoặc route sang provider khác.

## Quyền sở hữu Retry

Retry policy nên nằm trong orchestration layer, không chỉ trong prompt.

Mô hình có thể đề xuất một **semantic retry**, ví dụ sửa arguments rồi thử lại. Nhưng transport retry, timeout retry và backoff cho transient error là trách nhiệm của runtime.

## Approval là State hạng nhất

Human approval nên được persist như một event hoặc state rõ ràng:

```text
WAITING_APPROVAL
approval_scope
requested_action
expires_at
approved_by
```

Sau khi service restart, system vẫn biết task đang chờ approval nào và approval đó áp dụng cho action nào.

## Cancellation

User cần khả năng hủy task dài. Runtime phải propagate cancellation tới queued operation và tool đang chạy khi có thể.

Cancellation cũng cần semantics rõ: một external side effect đã commit có thể không thể “hủy” đơn giản mà phải dùng compensating action.

## Model Routing

Không phải step nào cũng cần model mạnh nhất.

Orchestrator có thể route:

```text
small model       → classification / extraction
large model       → planning mơ hồ hoặc synthesis khó
embedding model   → retrieval
specialized model → vision / speech / code
```

Model routing là bài toán tối ưu giữa chất lượng, latency và cost.

## Tool Routing

Nếu nhiều provider cung cấp cùng capability, routing có thể xét:

```text
availability
latency
cost
region
compliance
quality
rate limit
```

Fallback phải bảo toàn semantics. Hai API cùng được gọi là “search” hoặc “send message” có thể có contract và side effect khác nhau.

## Artifact Store

Output lớn nên được persist thành artifact thay vì truyền nguyên nội dung qua mọi prompt:

```text
artifact_id
content_hash
metadata
producer_step
version
```

Context của model chỉ nên mang reference, summary hoặc excerpt cần thiết.

## Event Bus

Event giúp tách rời các component:

```text
ToolSucceeded
ApprovalGranted
TaskTimedOut
ArtifactCreated
```

Consumer khác nhau có thể dùng cùng event để cập nhật UI, metrics, audit log hoặc trigger step tiếp theo.

## Exactly-Once rất khó

Trong distributed systems, bảo đảm **exactly-once execution** thật sự thường khó và đắt. Thiết kế thực tế phổ biến hơn là:

```text
at-least-once delivery
+
idempotent handler
```

Do đó tool có side effect nên hỗ trợ idempotency key hoặc cơ chế deduplication.

## Checkpoint và Resume

State nên được checkpoint sau những transition quan trọng. Khi worker crash:

```text
load checkpoint
→ kiểm tra side effect cuối đã commit chưa
→ xác định step an toàn tiếp theo
→ resume
```

Không nên replay mù toàn bộ trajectory, vì các write action cũ có thể bị thực hiện lại.

## Observability

Một trace có thể tổ chức theo hierarchy:

```text
Task trace
├─ model span
├─ retrieval span
├─ tool span
├─ approval span
└─ verification span
```

Các metric quan trọng gồm:

- task success rate;
- latency distribution;
- token và cost;
- tool error rate;
- retry count;
- step count;
- human escalation rate;
- cancellation rate;
- queue wait time.

## Orchestration và Framework

Agent framework có thể cung cấp abstraction tiện lợi, nhưng các khái niệm bền vững vẫn là:

```text
state machine
queue
event log
retry
permission
budget
tracing
checkpoint
```

Knowledge library nên ưu tiên những concept này thay vì phụ thuộc vào một framework cụ thể có thể thay đổi nhanh.

## Ví dụ: Enterprise Document Agent

Một hệ thống xử lý tài liệu doanh nghiệp có thể chạy:

```text
upload event
→ parse worker
→ indexing worker
→ agent analysis
→ policy validation
→ human approval nếu nhạy cảm
→ export artifact
→ notify user
```

Đây là một distributed workflow có node agentic, không phải một Python loop duy nhất chạy từ đầu đến cuối.

## Mô hình tư duy

> **Agent reasoning quyết định “nên làm gì”; orchestration đảm bảo việc đó được chạy, giới hạn, theo dõi, retry và phục hồi như thế nào.**

## Những nhầm lẫn thường gặp

### “Dùng agent framework là đã có production orchestration”

Không. Nhiều framework chủ yếu hỗ trợ prompt, tool và graph. Durability, multi-tenant security, queue, retry semantics và operations vẫn cần kiến trúc riêng.

### “Một serverless function loop là đủ”

Không phải với task dài, external side effect hoặc workflow cần resume. Timeout và retry của serverless runtime có thể tạo duplicate execution nếu không có durable state.

### “Queue chỉ để scale”

Không. Queue còn tạo isolation, buffering, rate control và retry boundary.

## Liên kết kiến thức

Orchestration nối agent với distributed systems, backend architecture, queue, event sourcing, concurrency control và observability.

Xem tiếp: [Đánh giá Agent](./09_agent_evaluation.md).