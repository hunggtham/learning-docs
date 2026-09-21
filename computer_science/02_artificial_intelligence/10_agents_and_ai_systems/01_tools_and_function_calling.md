# Công cụ và Function Calling

LLM sinh token; công cụ tạo **năng lực thực thi (capability)** và đôi khi tạo side effect. **Function calling / tool calling (도구 호출 / gọi công cụ)** là giao thức biến ý định xác suất của mô hình thành một yêu cầu có cấu trúc để runtime có thể kiểm tra, phân quyền, thực thi và ghi vết.

Mô hình tư duy:

```text
mục tiêu bằng ngôn ngữ tự nhiên
→ model đề xuất tool + arguments
→ runtime kiểm schema/semantics/quyền
→ tool thực thi
→ kết quả có cấu trúc
→ model tiếp tục reasoning
```

Mô hình thường không trực tiếp “gọi API” theo nghĩa networking. Nó sinh một object phù hợp schema; orchestration/runtime mới thực sự thực thi.

## Kiến thức cần có trước

Nên đọc [LLM và Context Engineering](../08_large_language_models/11_prompting_and_context_engineering.md), [RAG](../09_retrieval_and_rag/README.md), [AI System Architecture](../00_foundations/04_ai_system_architecture.md), [Secure AI System Design](../19_ai_safety_security_alignment/08_secure_ai_system_design.md) và [Reliability Engineering](../18_evaluation_reliability_interpretability/07_reliability_engineering.md).

## Tool Calling giải quyết bài toán gì?

LLM giỏi ánh xạ ngôn ngữ sang cấu trúc có ý nghĩa nhưng không nên tự sở hữu quyền truy cập hệ thống. Tool calling tách hai phần:

```text
model  → đề xuất hành động
runtime → quyết định hành động có hợp lệ và được phép hay không
```

Đây là ranh giới quan trọng giữa **suy luận xác suất** và **quyền thực thi xác định**.

## Vì sao cần công cụ có cấu trúc?

Nếu model chỉ trả prose kiểu `hãy gọi weather API với Seoul`, application phải parse text dễ vỡ. Schema có cấu trúc tạo boundary rõ:

```json
{
  "name": "get_weather",
  "arguments": {"city": "Seoul"}
}
```

Runtime có thể kiểm type, permission và field bắt buộc trước execution.

## Tool Schema là hợp đồng API

Một tool tốt cần:

- tên phản ánh đúng hành động;
- mô tả rõ semantics;
- argument có type;
- required/optional rõ;
- enum khi domain hữu hạn;
- result schema ổn định;
- taxonomy lỗi rõ;
- version rõ nếu contract có thể tiến hóa.

`update_user(data)` quá rộng. Tốt hơn:

```text
update_shipping_address(user_id, address)
set_notification_preference(user_id, channel, enabled)
```

Action hẹp dễ authorize, test và audit hơn.

## Mô hình thực thi Tool Call

Một tool call production nên đi qua pipeline:

```text
MODEL_PROPOSAL
→ PARSE
→ SCHEMA_VALIDATE
→ SEMANTIC_VALIDATE
→ AUTHORIZE
→ POLICY_CHECK
→ BUDGET_CHECK
→ EXECUTE
→ VERIFY_RESULT
→ PERSIST_EVENT
→ RETURN_OBSERVATION
```

Không nên bỏ qua bước vì model “có vẻ hiểu đúng”.

## Schema Validation khác Semantic Validation

`amount = -1000` có thể đúng type `number` nhưng vô nghĩa với API thanh toán.

Do đó cần hai tầng:

```text
schema validation   → shape/type đúng?
semantic validation → giá trị có hợp domain/business rule không?
```

Sau đó mới tới authorization và policy.

## Tool đọc và Tool ghi

Nên tách:

```text
READ  → search, fetch, inspect, query
WRITE → create, update, delete, send, deploy
```

Write tool cần approval, idempotency, concurrency control và audit chặt hơn.

## Authorization phải xảy ra tại thời điểm thực thi

Không nên chỉ kiểm quyền khi agent bắt đầu task rồi tin rằng quyền vẫn còn nguyên. User có thể bị revoke permission giữa workflow dài.

Pattern tốt:

```text
model proposes action
→ runtime resolve current identity/context
→ authorize action trên resource cụ thể
→ execute
```

Đây là cách giảm lỗi **time-of-check to time-of-use (TOCTOU)** giữa bước lập kế hoạch và bước thực thi.

## Quyền tối thiểu

Agent chỉ nên thấy tool cần cho task; credential cũng phải được scope tối thiểu.

Agent chỉ cần đọc invoice không nên có `delete_invoice`. Nếu workflow chỉ cần tạo draft email thì không nên cấp quyền gửi thật.

Prompt “đừng xóa dữ liệu” không thay thế việc **không cấp capability xóa**.

## Idempotency và ảo tưởng Exactly-Once

Retry là bình thường trong distributed system. Với side effect, retry có thể tạo payment/email/job trùng.

Write tool nên nhận **khóa idempotency (idempotency key)**:

```text
create_payment(request_id="task-123-step-4", ...)
```

Nếu cùng logical request lặp lại, service trả cùng logical result thay vì tạo action mới.

Không nên giả định mạng cung cấp “exactly once”. Thực tế thường là:

```text
at-least-once delivery
+ idempotent effect
≈ exactly-once behavior ở mức nghiệp vụ
```

Đây là distinction quan trọng cho agent có side effect.

## Optimistic Concurrency Control

Nếu agent đọc resource version 42 rồi user khác cập nhật thành 43, write dựa trên state cũ không nên âm thầm ghi đè.

Tool có thể yêu cầu:

```text
update_resource(id, expected_version=42, ...)
```

Nếu version đã đổi, trả `CONFLICT` để agent re-read hoặc escalate.

Cơ chế này giảm lost update trong workflow stateful.

## Kết quả Tool nên đọc được bằng máy

Tránh chỉ trả:

```text
Success
```

Tốt hơn:

```json
{
  "status": "updated",
  "resource_id": "A17",
  "version": 42,
  "changed_fields": ["email"]
}
```

Agent cần observation cụ thể để cập nhật state và verify outcome.

## Phân loại lỗi

Tool error không nên chỉ là một string chung.

```text
INVALID_ARGUMENT
NOT_FOUND
PERMISSION_DENIED
CONFLICT
RATE_LIMITED
TRANSIENT_FAILURE
TIMEOUT
DEPENDENCY_FAILURE
```

Recovery phụ thuộc loại lỗi:

```text
TRANSIENT_FAILURE → retry có backoff
RATE_LIMITED      → chờ hoặc giảm tải
CONFLICT          → đọc state mới rồi quyết định lại
PERMISSION_DENIED → không retry mù
INVALID_ARGUMENT  → sửa request hoặc dừng
```

## Timeout, Deadline và Cancellation

Tool cần timeout riêng nhưng phải nằm trong end-to-end deadline.

Ví dụ request có budget 5 giây thì một downstream timeout 30 giây là cấu hình sai.

Runtime nên truyền deadline:

```text
request deadline
→ orchestrator remaining budget
→ tool timeout <= remaining budget
```

Tool chạy dài cần cancellation hoặc operation ID.

## Công cụ bất đồng bộ

Một số operation không thể hoàn tất trong một HTTP call:

```text
start_export(...)
→ {operation_id: "op-123", status: "PENDING"}
```

Sau đó:

```text
get_operation("op-123")
→ RUNNING / SUCCEEDED / FAILED / CANCELLED
```

Agent state phải lưu operation ID; không nên “nhớ” nó chỉ trong prose transcript.

## Chọn Tool

Mô hình phải quyết định cả **có cần dùng tool hay không**.

Failure mode gồm:

- bịa tool không tồn tại;
- dùng tool không cần thiết;
- chọn tool gần nghĩa nhưng sai semantics;
- gọi nhiều tool dư thừa;
- không gọi tool khi cần dữ liệu live;
- dùng retrieval khi cần action hoặc ngược lại.

Mô tả tool, tên field và ví dụ ảnh hưởng mạnh tới routing behavior.

## Tool Selection như bài toán phân loại có điều kiện

Có thể hình dung model đang ước lượng:

\[
P(tool, arguments\mid context)
\]

Runtime không cần biết xác suất nội bộ chính xác, nhưng intuition này giải thích vì sao tool schema chồng lấn làm routing khó hơn.

Nếu hai tool gần như cùng semantics, entropy lựa chọn tăng và error dễ xuất hiện. Thiết kế capability rõ ràng thường tốt hơn thêm prompt dài để phân biệt hai API mơ hồ.

## Gọi Tool song song

Các read operation độc lập có thể chạy song song:

```text
search CRM ─┐
search docs ├─→ combine
search logs ─┘
```

Nhưng write action có dependency thường phải tuần tự hoặc có transaction semantics.

Parallelism giảm latency nhưng tăng complexity về ordering, partial failure và aggregation context.

## Transaction và Compensating Action

Task nhiều bước:

```text
reserve inventory
charge payment
create shipment
```

Nếu bước 3 lỗi, không phải lúc nào rollback database transaction xuyên nhiều service cũng khả thi. Khi đó workflow cần **hành động bù (compensating action)** đã được định nghĩa trước, ví dụ refund hoặc release reservation.

Agent planner không nên tự phát minh compensation cho nghiệp vụ nhạy cảm; workflow/tool contract phải chỉ ra action nào hợp lệ.

## Tool Output là dữ liệu không đáng tin

Web page, email, document hoặc API text có thể chứa malicious instruction. Đây là **indirect prompt injection**.

Runtime phải phân biệt:

```text
trusted policy/instruction
≠
untrusted tool data
```

Delimiter hoặc JSON giúp cấu trúc context nhưng không tạo security boundary.

## Mức trừu tượng của Tool

Quá thấp:

```text
http_request(method,url,body)
```

linh hoạt nhưng khó secure.

Quá cao:

```text
run_company()
```

mơ hồ và khó verify.

Tool tốt nên phản ánh business operation có contract rõ, đủ hẹp để authorize và đủ cao để model không phải điều khiển protocol chi tiết.

## Tool Schema Evolution

Tool contract thay đổi có thể làm model behavior regression dù model không đổi.

Các thay đổi nguy hiểm:

```text
đổi tên field
đổi enum semantics
field optional thành required
đổi đơn vị
đổi error taxonomy
đổi permission requirement
```

Nên version schema và giữ compatibility hoặc migration rõ. LLMOps phải coi tool schema là một phần của **behavior bundle**.

## Tool Discovery và Capability Surface

Không nên đưa hàng trăm tool vào context nếu task chỉ cần vài tool. Tool set lớn:

- tăng token cost;
- tăng nhầm lẫn routing;
- mở rộng attack surface;
- khó đánh giá hơn.

Có thể dùng routing tầng trước để chọn một subset capability phù hợp với task và user permission.

## Ví dụ: trợ lý cơ sở dữ liệu

Không nên cấp raw production SQL write toàn quyền. Có thể expose:

```text
find_customer(customer_id)
list_open_cases(customer_id)
create_case_note(case_id, text, expected_version)
```

Authorization nằm ở service layer, không ở prompt.

## Observability

Mỗi tool call nên ghi:

```text
trace_id
agent/task id
tool name + schema version
arguments đã redaction dữ liệu nhạy cảm
authorization result
approval event
result/error
latency
retry count
resource/version bị thay đổi
idempotency key
```

Không nên log secret hoặc PII tùy tiện.

## Đánh giá Tool Calling

Eval suite nên có:

```text
tool selection
argument schema
argument semantics
permission enforcement
retry behavior
idempotency
conflict handling
async operation recovery
injection qua tool output
unnecessary call rate
```

Cần test cả case “không được gọi tool”. Một model luôn gọi tool có thể tạo cost hoặc side effect không cần thiết.

## Failure mode thường gặp

**Schema đúng nhưng semantics sai.** `customer_id` tồn tại nhưng thuộc người khác.

**Authorization chỉ kiểm đầu workflow.** Quyền bị revoke nhưng action sau vẫn chạy.

**Retry gây duplicate side effect.** Không có idempotency key.

**Concurrent write ghi đè.** Không có version check.

**Tool schema đổi âm thầm.** Prompt/model cũ tiếp tục sinh argument theo contract cũ.

**Async operation bị mất state.** Agent crash rồi không biết job nào đang chạy.

**Tool output chiếm quyền điều khiển.** Indirect prompt injection được coi như instruction đáng tin.

**Tool quá generic.** Model có capability vượt nhu cầu task.

## Production usage pattern

Một execution path an toàn:

```text
LLM proposal
→ parse + schema validation
→ semantic validation
→ current authorization
→ policy/risk gate
→ approval nếu cần
→ execute với idempotency/concurrency control
→ verify result
→ persist event/state
→ return structured observation
```

Đây là pattern nền cho reliable agent.

## Mô hình tư duy

> **Tool calling là ranh giới có kiểu giữa quyết định xác suất và capability xác định. LLM đề xuất; runtime kiểm soát authority; service thực thi; observation quay lại agent.**

## Những hiểu lầm thường gặp

### “JSON đúng schema nghĩa là action đúng”

Không. Schema chỉ kiểm shape; semantic correctness và authorization vẫn cần validation.

### “Prompt đủ để bảo vệ tool nguy hiểm”

Không. Security cần permission boundary, sandbox, approval và server-side policy.

### “Retry đơn giản là gọi lại”

Không với side effect. Retry cần idempotency và hiểu error class.

### “Tool càng generic càng tốt”

Không. Tool quá generic tăng flexibility nhưng giảm verifiability và safety.

### “Tool schema chỉ là tài liệu cho model”

Không. Schema/version là một phần của runtime contract và behavior bundle production.

## Liên kết kiến thức

Tool calling nối [LLM](../08_large_language_models/README.md) và [RAG](../09_retrieval_and_rag/README.md) với [Agent Loop](./02_agent_loop.md), [Agent State](./05_agent_state_and_context.md), [Agent Evaluation](./09_agent_evaluation.md), [Reliability Engineering](../18_evaluation_reliability_interpretability/07_reliability_engineering.md), [LLMOps](../16_mlops_and_llmops/08_llmops.md) và [Secure AI System Design](../19_ai_safety_security_alignment/08_secure_ai_system_design.md).

Xem tiếp: [Agent Loop](./02_agent_loop.md).