# Tác nhân (agent / 에이전트) Orchestration

> **Mạch đọc:** Đặt **tác nhân (agent / 에이전트) Orchestration** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Orchestrator owns vòng đời (lifecycle / 생명주기)** sang **Queue-Based thực thi (execution / 실행)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**Orchestration (오케스트레이션 / điều phối)** là tầng (layer / 계층) quản lý thực thi (execution / 실행) của tác nhân (agent / 에이전트)/workflow: scheduling, trạng thái (state / 상태), queues, retries, budgets, tính đồng thời (concurrency / 동시성), approvals, tracing và khôi phục (recovery / 복구). mô hình (model / 모델) lập luận (reasoning / 추론) không thay thế orchestration.

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

## Orchestrator owns vòng đời (lifecycle / 생명주기)

Một tác vụ (task / 작업) môi trường vận hành (production / 운영 환경) có vòng đời (lifecycle / 생명주기):

```text
CREATED
→ RUNNING
→ WAITING_TOOL / WAITING_APPROVAL
→ RUNNING
→ COMPLETED / FAILED / CANCELLED
```

Persist vòng đời (lifecycle / 생명주기) giúp restart/resume.

## Queue-Based thực thi (execution / 실행)

Long-running tác vụ (task / 작업) nên tách yêu cầu (request / 요청)/phản hồi (response / 응답) HTTP khỏi thực thi (execution / 실행) worker.

```text
API creates task
→ queue
→ worker executes
→ events/state persisted
→ client polls/subscribes
```

Điều này hỗ trợ retries, backpressure và horizontal scaling.

## Tính đồng thời (concurrency / 동시성) điều khiển (control / 제어)

Need limits theo:

- tenant;
- người dùng (user / 사용자);
- công cụ (tool / 도구)/provider;
- mô hình (model / 모델) sức chứa (capacity / 용량);
- bên ngoài (external / 외부) API tỷ lệ (rate / 비율) limits.

Unlimited parallel agents dễ tạo chi phí (cost / 비용) explosion hoặc hammer downstream các hệ thống (systems / 시스템들).

## Scheduling

Subtasks có phụ thuộc (dependency / 의존성) DAG. Scheduler chỉ run nodes có prerequisites satisfied.

Priority có thể dựa trên SLA, deadline, đường găng (critical path / 임계 경로) hoặc người dùng (user / 사용자) tier.

## Backpressure

Nếu công cụ (tool / 도구)/provider chậm, hàng đợi (queue / 큐) length tăng. hệ thống (system / 시스템) cần backpressure thay vì tiếp tục spawn workers.

Signals:

```text
queue depth
oldest task age
worker utilization
provider error rate
```

## Thử lại (retry / 재시도) quyền sở hữu (ownership / 소유권)

Thử lại (retry / 재시도) chính sách (policy / 정책) nên nằm orchestration tầng (layer / 계층), không chỉ trong prompt.

Mô hình (model / 모델) có thể propose ngữ nghĩa (semantic / 의미적) thử lại (retry / 재시도), nhưng vận chuyển (transport / 전송)/transient retries là thời gian chạy (runtime / 런타임) concern.

## Approval as First-Class trạng thái (state / 상태)

Human approval nên persisted sự kiện (event / 이벤트)/trạng thái (state / 상태):

```text
WAITING_APPROVAL
approval_scope
requested_action
expires_at
approved_by
```

Sau restart vẫn biết tác vụ (task / 작업) đang chờ gì.

## Cancellation

Người dùng (user / 사용자) cần cancel long tác vụ (task / 작업). thời gian chạy (runtime / 런타임) phải propagate cancellation tới queued/running công cụ (tool / 도구) operations khi có thể.

## Mô hình (model / 모델) Routing

Không phải step nào cũng cần strongest mô hình (model / 모델).

Routing có thể chọn:

```text
small model → classification/extraction
large model → ambiguous planning
embedding model → retrieval
specialized model → vision/code
```

Routing là cost-quality tối ưu hóa (optimization / 최적화) bài toán (problem / 문제).

## Công cụ (tool / 도구) Routing

Multiple providers cho same năng lực (capability / 역량) có thể tuyến (route / 경로) theo:

```text
availability
latency
cost
region
compliance
quality
```

Fallback phải preserve ngữ nghĩa (semantics / 의미론); hai APIs cùng tên năng lực (capability / 역량) có thể khác đặc tả hợp đồng (contract / 계약).

## Sản phẩm tạo ra (artifact / 산출물) Store

Large outputs nên persist sản phẩm tạo ra (artifact / 산출물), không pass qua every prompt.

```text
artifact id
content hash
metadata
producer step
version
```

Ngữ cảnh (context / 맥락) chỉ carry references/excerpts.

## Sự kiện (event / 이벤트) Bus

Events decouple components:

```text
ToolSucceeded
ApprovalGranted
TaskTimedOut
ArtifactCreated
```

Consumers có thể cập nhật (update / 업데이트) UI, metrics, kiểm tra (audit / 감사) hoặc trigger next step.

## Exactly-Once là khó

Phân tán (distributed / 분산) các hệ thống (systems / 시스템들) thường không guarantee exactly-once thực thi (execution / 실행) đơn giản. Practical thiết kế (design / 설계) dùng at-least-once delivery + idempotent handlers.

Tác nhân (agent / 에이전트) tools vì vậy cần idempotency.

## Checkpoint và Resume

Persist trạng thái (state / 상태) sau meaningful chuyển tiếp (transition / 전이). Khi worker crash:

```text
load checkpoint
inspect last committed side effect
resume from next safe step
```

Không blindly replay whole trajectory.

## Khả năng quan sát (observability / 관측 가능성)

Dấu vết (trace / 추적) hierarchy:

```text
Task trace
├─ model span
├─ retrieval span
├─ tool span
├─ approval span
└─ verification span
```

Metrics:

- tác vụ (task / 작업) success;
- độ trễ (latency / 지연 시간) phân phối (distribution / 분포);
- tokens/chi phí (cost / 비용);
- công cụ (tool / 도구) lỗi (error / 오류) tỷ lệ (rate / 비율);
- thử lại (retry / 재시도) count;
- step count;
- human escalation tỷ lệ (rate / 비율).

## Orchestration vs khung phần mềm (framework / 프레임워크)

Khung phần mềm (framework / 프레임워크) có thể provide abstractions, nhưng concepts bền vững là máy trạng thái (state machine / 상태 머신), hàng đợi (queue / 큐), sự kiện (event / 이벤트) log, thử lại (retry / 재시도), permission và tracing. thư viện (library / 라이브러리) này ưu tiên concepts thay vì phụ thuộc một tác nhân (agent / 에이전트) khung phần mềm (framework / 프레임워크) cụ thể.

## Example: Enterprise document tác nhân (agent / 에이전트)

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

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

Đây là phân tán (distributed / 분산) workflow có agentic nút (node / 노드), không phải single Python vòng lặp (loop / 루프).

## Mô hình tư duy (mental model / 사고 모델)

> **tác nhân (agent / 에이전트) lập luận (reasoning / 추론) quyết định “nên làm gì”; orchestration đảm bảo “việc đó được chạy, theo dõi, thử lại (retry / 재시도), giới hạn và phục hồi như thế nào”.**

## Dùng chung (common / 공통) Misconceptions

### “tác nhân (agent / 에이전트) khung phần mềm (framework / 프레임워크) đã lo môi trường vận hành (production / 운영 환경) orchestration”

Nhiều khung phần mềm (framework / 프레임워크) chủ yếu lo prompt/công cụ (tool / 도구) đồ thị (graph / 그래프); durability, multi-tenant bảo mật (security / 보안) và ops vẫn cần kiến trúc (architecture / 아키텍처) riêng.

### “Serverless hàm (function / 함수) vòng lặp (loop / 루프) là đủ”

Tác vụ (task / 작업) dài có hết thời gian chờ (timeout / 타임아웃), retries và bên ngoài (external / 외부) side effects cần durable trạng thái (state / 상태)/workflow ngữ nghĩa (semantics / 의미론).

### “hàng đợi (queue / 큐) chỉ để quy mô (scale / 규모)”

Hàng đợi (queue / 큐) còn là isolation, buffering và thử lại (retry / 재시도) ranh giới (boundary / 경계).

## Liên kết kiến thức (knowledge connection / 지식 연결)

Orchestration nối agents với phân tán (distributed / 분산) các hệ thống (systems / 시스템들), backend kiến trúc (architecture / 아키텍처), queues, sự kiện (event / 이벤트) sourcing và khả năng quan sát (observability / 관측 가능성).

Xem tiếp: [Agent Evaluation](./09_agent_evaluation.md).
