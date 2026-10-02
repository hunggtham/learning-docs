# Tác nhân (agent / 에이전트) Orchestration

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Agent orchestration**. Route đi từ lifecycle ownership → queue/scheduler → retries/timeouts → concurrency/idempotency → tracing and human handoff, để orchestration được đọc như reliability infrastructure.

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

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) Orchestration**, **Orchestrator owns vòng đời (lifecycle / 생명주기)** xác định đầu vào; **Queue-Based thực thi (execution / 실행)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Tính đồng thời (concurrency / 동시성) điều khiển (control / 제어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Tác nhân (agent / 에이전트) Orchestration**, **Tính đồng thời (concurrency / 동시성) điều khiển (control / 제어)** tiếp nhận điểm tựa từ **Queue-Based thực thi (execution / 실행)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Scheduling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính đồng thời (concurrency / 동시성) điều khiển (control / 제어)

Need limits theo:

- tenant;
- người dùng (user / 사용자);
- công cụ (tool / 도구)/provider;
- mô hình (model / 모델) sức chứa (capacity / 용량);
- bên ngoài (external / 외부) API tỷ lệ (rate / 비율) limits.

Unlimited parallel agents dễ tạo chi phí (cost / 비용) explosion hoặc hammer downstream các hệ thống (systems / 시스템들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tác nhân (agent / 에이전트) Orchestration**, **Scheduling** tiếp nhận điểm tựa từ **Tính đồng thời (concurrency / 동시성) điều khiển (control / 제어)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Backpressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Scheduling

Subtasks có phụ thuộc (dependency / 의존성) DAG. Scheduler chỉ run nodes có prerequisites satisfied.

Priority có thể dựa trên SLA, deadline, đường găng (critical path / 임계 경로) hoặc người dùng (user / 사용자) tier.

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) Orchestration**, **Backpressure** tiếp nhận điểm tựa từ **Scheduling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thử lại (retry / 재시도) quyền sở hữu (ownership / 소유권)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Backpressure

Nếu công cụ (tool / 도구)/provider chậm, hàng đợi (queue / 큐) length tăng. hệ thống (system / 시스템) cần backpressure thay vì tiếp tục spawn workers.

Signals:

```text
queue depth
oldest task age
worker utilization
provider error rate
```

> **Chuyển mạch:** Ở chặng này của **Tác nhân (agent / 에이전트) Orchestration**, sau nội dung của **Backpressure**, **Thử lại (retry / 재시도) quyền sở hữu (ownership / 소유권)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Approval as First-Class trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thử lại (retry / 재시도) quyền sở hữu (ownership / 소유권)

Thử lại (retry / 재시도) chính sách (policy / 정책) nên nằm orchestration tầng (layer / 계층), không chỉ trong prompt.

Mô hình (model / 모델) có thể propose ngữ nghĩa (semantic / 의미적) thử lại (retry / 재시도), nhưng vận chuyển (transport / 전송)/transient retries là thời gian chạy (runtime / 런타임) concern.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tác nhân (agent / 에이전트) Orchestration**, **Approval as First-Class trạng thái (state / 상태)** tiếp nhận điểm tựa từ **Thử lại (retry / 재시도) quyền sở hữu (ownership / 소유권)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cancellation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) Orchestration**, **Cancellation** tiếp nhận điểm tựa từ **Approval as First-Class trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình (model / 모델) Routing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cancellation

Người dùng (user / 사용자) cần cancel long tác vụ (task / 작업). thời gian chạy (runtime / 런타임) phải propagate cancellation tới queued/running công cụ (tool / 도구) operations khi có thể.

> **Chuyển mạch:** Ở chặng này của **Tác nhân (agent / 에이전트) Orchestration**, **Mô hình (model / 모델) Routing** tiếp nhận điểm tựa từ **Cancellation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Công cụ (tool / 도구) Routing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tác nhân (agent / 에이전트) Orchestration**, **Công cụ (tool / 도구) Routing** tiếp nhận điểm tựa từ **Mô hình (model / 모델) Routing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sản phẩm tạo ra (artifact / 산출물) Store** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) Orchestration**, **Sản phẩm tạo ra (artifact / 산출물) Store** tiếp nhận điểm tựa từ **Công cụ (tool / 도구) Routing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sự kiện (event / 이벤트) Bus** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Tác nhân (agent / 에이전트) Orchestration**, **Sự kiện (event / 이벤트) Bus** tiếp nhận điểm tựa từ **Sản phẩm tạo ra (artifact / 산출물) Store** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Exactly-Once là khó** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sự kiện (event / 이벤트) Bus

Events decouple components:

```text
ToolSucceeded
ApprovalGranted
TaskTimedOut
ArtifactCreated
```

Consumers có thể cập nhật (update / 업데이트) UI, metrics, kiểm tra (audit / 감사) hoặc trigger next step.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tác nhân (agent / 에이전트) Orchestration**, **Exactly-Once là khó** tiếp nhận điểm tựa từ **Sự kiện (event / 이벤트) Bus** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Checkpoint và Resume** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Exactly-Once là khó

Phân tán (distributed / 분산) các hệ thống (systems / 시스템들) thường không guarantee exactly-once thực thi (execution / 실행) đơn giản. Practical thiết kế (design / 설계) dùng at-least-once delivery + idempotent handlers.

Tác nhân (agent / 에이전트) tools vì vậy cần idempotency.

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) Orchestration**, **Checkpoint và Resume** tiếp nhận điểm tựa từ **Exactly-Once là khó** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khả năng quan sát (observability / 관측 가능성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Checkpoint và Resume

Persist trạng thái (state / 상태) sau meaningful chuyển tiếp (transition / 전이). Khi worker crash:

```text
load checkpoint
inspect last committed side effect
resume from next safe step
```

Không blindly replay whole trajectory.

> **Chuyển mạch:** Ở chặng này của **Tác nhân (agent / 에이전트) Orchestration**, **Khả năng quan sát (observability / 관측 가능성)** tiếp nhận điểm tựa từ **Checkpoint và Resume** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Orchestration vs khung phần mềm (framework / 프레임워크)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tác nhân (agent / 에이전트) Orchestration**, **Orchestration vs khung phần mềm (framework / 프레임워크)** tiếp nhận điểm tựa từ **Khả năng quan sát (observability / 관측 가능성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Example: Enterprise document tác nhân (agent / 에이전트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Orchestration vs khung phần mềm (framework / 프레임워크)

Khung phần mềm (framework / 프레임워크) có thể provide abstractions, nhưng concepts bền vững là máy trạng thái (state machine / 상태 머신), hàng đợi (queue / 큐), sự kiện (event / 이벤트) log, thử lại (retry / 재시도), permission và tracing. thư viện (library / 라이브러리) này ưu tiên concepts thay vì phụ thuộc một tác nhân (agent / 에이전트) khung phần mềm (framework / 프레임워크) cụ thể.

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) Orchestration**, **Orchestration vs khung phần mềm (framework / 프레임워크)** cho ta quy tắc; **Example: Enterprise document tác nhân (agent / 에이전트)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Tác nhân (agent / 에이전트) Orchestration**, **Example: Enterprise document tác nhân (agent / 에이전트)** cho ta quy tắc; **Mô hình tư duy (mental model / 사고 모델)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **tác nhân (agent / 에이전트) lập luận (reasoning / 추론) quyết định “nên làm gì”; orchestration đảm bảo “việc đó được chạy, theo dõi, thử lại (retry / 재시도), giới hạn và phục hồi như thế nào”.**

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tác nhân (agent / 에이전트) Orchestration**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “tác nhân (agent / 에이전트) khung phần mềm (framework / 프레임워크) đã lo môi trường vận hành (production / 운영 환경) orchestration”

Nhiều khung phần mềm (framework / 프레임워크) chủ yếu lo prompt/công cụ (tool / 도구) đồ thị (graph / 그래프); durability, multi-tenant bảo mật (security / 보안) và ops vẫn cần kiến trúc (architecture / 아키텍처) riêng.

### “Serverless hàm (function / 함수) vòng lặp (loop / 루프) là đủ”

Tác vụ (task / 작업) dài có hết thời gian chờ (timeout / 타임아웃), retries và bên ngoài (external / 외부) side effects cần durable trạng thái (state / 상태)/workflow ngữ nghĩa (semantics / 의미론).

### “hàng đợi (queue / 큐) chỉ để quy mô (scale / 규모)”

Hàng đợi (queue / 큐) còn là isolation, buffering và thử lại (retry / 재시도) ranh giới (boundary / 경계).

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) Orchestration**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Orchestration nối agents với phân tán (distributed / 분산) các hệ thống (systems / 시스템들), backend kiến trúc (architecture / 아키텍처), queues, sự kiện (event / 이벤트) sourcing và khả năng quan sát (observability / 관측 가능성).

Xem tiếp: [Agent Evaluation](./09_agent_evaluation.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
