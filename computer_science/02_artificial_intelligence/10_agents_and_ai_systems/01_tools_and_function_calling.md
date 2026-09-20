# Tools và Function Calling

LLM sinh token; tool tạo side effect. **Function calling / tool calling (도구 호출)** là protocol biến intent của model thành structured request mà runtime có thể validate rồi thực thi.

Mental model:

```text
Natural-language goal
→ model chooses tool + arguments
→ runtime validates
→ tool executes
→ structured result
→ model continues reasoning
```

Model không trực tiếp “gọi API” theo nghĩa networking. Nó thường sinh object conform schema; orchestration layer mới thực thi.

## Vì sao structured tools cần tồn tại?

Nếu yêu cầu model trả prose như `hãy gọi weather API với Seoul`, application phải parse text brittle. Structured schema làm boundary rõ:

```json
{
  "name": "get_weather",
  "arguments": {"city": "Seoul"}
}
```

Runtime có thể kiểm type, permission và required fields trước execution.

## Tool schema là một API contract

Một tool tốt cần:

- tên phản ánh action;
- description nói rõ semantics;
- arguments typed;
- required/optional rõ;
- enum khi domain hữu hạn;
- result structure ổn định;
- error taxonomy rõ.

Schema mơ hồ gây model error dù model mạnh.

Ví dụ `update_user(data)` quá rộng. Tốt hơn có các action hẹp:

```text
update_shipping_address(user_id, address)
set_notification_preference(user_id, channel, enabled)
```

Action hẹp dễ authorize, test và audit hơn.

## Read tools và Write tools

Tách read-only và side-effecting tools.

```text
READ: search, fetch, inspect, query
WRITE: create, update, delete, send, deploy
```

Write tools cần stricter approval, idempotency và audit.

## Validation trước execution

Không tin arguments chỉ vì chúng parse được.

Validation layers:

```text
schema validation
→ semantic validation
→ authorization
→ policy/risk check
→ rate/budget check
→ execution
```

`amount: -1000` có thể đúng type number nhưng sai business semantics.

## Idempotency

Agent retry là bình thường. Với side effects, retry có thể tạo duplicate email/payment/job.

Tool write nên hỗ trợ idempotency key khi khả thi:

```text
create_payment(request_id="task-123-step-4", ...)
```

Nếu same request lặp lại, service trả same result thay vì tạo action mới.

## Tool Result nên machine-readable

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

Agent cần concrete observation để update state.

## Error taxonomy

Tool error không nên là một string chung.

Phân biệt:

```text
INVALID_ARGUMENT
NOT_FOUND
PERMISSION_DENIED
CONFLICT
RATE_LIMITED
TRANSIENT_FAILURE
TIMEOUT
```

Mỗi loại dẫn tới recovery khác nhau. `TRANSIENT_FAILURE` có thể retry; `PERMISSION_DENIED` không nên loop retry.

## Timeout và cancellation

Tool lâu cần timeout rõ. Agent runtime cũng cần khả năng cancel để không để action orphaned.

Tool result có thể ở trạng thái:

```text
PENDING → SUCCEEDED / FAILED / CANCELLED
```

Long-running tools nên trả operation ID rồi poll/event-driven update.

## Least Privilege

Agent chỉ nên thấy tool cần cho task. Tool credential cũng phải scope tối thiểu.

Một agent chỉ cần đọc invoice không nên có `delete_invoice`.

Security boundary nên nằm ngoài prompt. “Đừng xóa dữ liệu” trong system prompt không mạnh bằng không expose delete permission.

## Tool selection

Model phải quyết định không chỉ arguments mà cả **có cần tool không**.

Failure modes:

- hallucinate tool không tồn tại;
- dùng tool không cần thiết;
- chọn tool gần nghĩa nhưng sai semantics;
- gọi nhiều tool redundant;
- không gọi tool khi factual grounding cần thiết.

Tool descriptions và examples ảnh hưởng routing behavior.

## Parallel tool calls

Independent read operations có thể chạy song song:

```text
search CRM ─┐
search docs ├─→ combine
search logs ─┘
```

Nhưng write actions có dependency cần serialize.

Parallelism giảm latency nhưng tăng complexity về ordering, errors và context aggregation.

## Tool output là untrusted input

Web page, email hoặc document tool có thể chứa malicious instruction. Đây là **indirect prompt injection**.

Runtime không nên coi tool content là authority ngang system policy.

Mental separation:

```text
instructions from trusted policy
≠
data returned by tool
```

## Transactions

Multi-step write task có consistency problem:

```text
reserve inventory
charge payment
create shipment
```

Nếu bước 2 fail sau bước 1, cần rollback/compensating action. Agent reasoning không thay thế transactional design.

## Tool abstraction level

Too low-level:

```text
http_request(method,url,body)
```

linh hoạt nhưng khó secure.

Too high-level:

```text
run_company()
```

mơ hồ, khó inspect.

Tốt nhất tool phản ánh meaningful business operation với contract rõ.

## Example: database assistant

Không nên cho model raw production SQL write toàn quyền. Có thể expose:

```text
find_customer(customer_id)
list_open_cases(customer_id)
create_case_note(case_id, text)
```

với authorization ở service layer.

## Observability

Mỗi tool call nên log:

```text
trace_id
agent/task id
tool name
sanitized args
result/error
latency
cost
approval event
side-effect resource/version
```

Không log secret/PII tùy tiện.

## Mental Model

> **Tool calling là typed boundary giữa probabilistic decision và deterministic capability.**

LLM đề xuất; runtime kiểm soát; tool thực thi; result trở thành observation.

## Common Misconceptions

### “JSON đúng schema nghĩa là action đúng”

Schema chỉ kiểm shape. Semantic correctness và authorization vẫn phải validate.

### “Prompt đủ để bảo vệ dangerous tools”

Không. Security cần permission boundary, sandbox, approval và server-side policy.

### “Tool càng generic càng tốt”

Generic tool tăng flexibility nhưng giảm verifiability và safety.

## Knowledge Connection

Tool calling nối [AI System Architecture](../00_foundations/04_ai_system_architecture.md) với agent runtime. Chapter tiếp theo mô tả loop điều phối nhiều tool calls qua time.

Xem tiếp: [Agent Loop](./02_agent_loop.md).