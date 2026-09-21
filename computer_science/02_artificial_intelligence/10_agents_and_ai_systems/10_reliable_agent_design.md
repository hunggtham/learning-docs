# Thiết kế Agent đáng tin cậy

Một agent đáng tin cậy không xuất hiện chỉ nhờ prompt kiểu “hãy cẩn thận”. **Độ tin cậy (reliability)** đến từ kiến trúc có khả năng giới hạn uncertainty, kiểm soát side effect, verify progress và phục hồi sau failure.

Một mô hình production có thể nhìn như sau:

```text
Mục tiêu của user
→ plan được giới hạn phạm vi
→ action space có ranh giới
→ execution được validate
→ observation của kết quả
→ verification
→ state được persist
→ tiếp tục / escalate / dừng
```

## Nguyên tắc 1: Chỉ dùng Autonomy khi nó tạo giá trị

Nếu logic đã biết trước, code hoặc workflow deterministic thường đáng tin hơn. Chỉ nên giao cho model những quyết định thật sự cần semantic flexibility.

```text
branch đã biết      → code trực tiếp
semantic choice mơ hồ → model có thể quyết định
write rủi ro cao    → policy + approval
```

Autonomy là một trade-off, không phải mục tiêu tự thân.

## Nguyên tắc 2: Thu hẹp Action Space

Một số tool nhỏ nhưng có semantics rõ thường tốt hơn raw shell hoặc API toàn quyền. Typed action tạo boundary rõ cho authorization, validation và audit.

Ví dụ `delete_customer_account(customer_id)` có thể dễ kiểm soát hơn một generic `execute_sql(sql)` rất nhiều.

## Nguyên tắc 3: Tách Proposal khỏi Execution

LLM đề xuất action. Runtime kiểm tra:

```text
schema
business constraint
permission
risk
budget
approval
```

sau đó mới thực thi.

Probabilistic reasoning và deterministic execution không nên bị trộn thành một bước không kiểm soát.

## Nguyên tắc 4: Least Privilege

Credential và tool chỉ nên có quyền tối thiểu cần thiết.

```text
read-only mặc định
write permission tách riêng
destructive operation có gate mạnh hơn
```

Agent không nên có quyền rộng chỉ vì “có thể sẽ cần”.

## Nguyên tắc 5: Thiết kế Write có tính Idempotent

Retry là chuyện bình thường trong distributed system. Write operation nên chống duplicate side effect bằng:

```text
idempotency key
resource version
transaction id
request id
```

Nếu cùng một step bị chạy lại, hệ thống cần biết đó là retry chứ không phải một yêu cầu mới.

## Nguyên tắc 6: Verify Effect, không Verify Intent

Sau mutation:

```text
write → đọc lại / test / inspect external state
```

Không chấp nhận assertion của model kiểu “đã hoàn thành” nếu hệ thống có thể kiểm tra trạng thái thật.

## Nguyên tắc 7: Persist State có cấu trúc

Conversation transcript không đủ làm durable state. Nên persist ít nhất:

```text
task status
resource id
plan
completed step
approval
verification result
budget
```

Structured state giúp resume, audit và concurrency control đáng tin hơn.

## Nguyên tắc 8: Thiết kế để Restart được

Worker, model và API đều có thể fail. Cần checkpoint sau committed side effect và resume từ known state thay vì replay toàn bộ trajectory một cách mù quáng.

## Nguyên tắc 9: Phân loại Error

Các error khác nhau cần cách recovery khác nhau:

```text
transient error   → retry/backoff
invalid argument  → sửa input
permission error  → stop/escalate
conflict          → refetch state
business rejection→ replan hoặc hỏi user
```

Blind retry là một anti-pattern.

## Nguyên tắc 10: Giới hạn Loop

Đặt các giới hạn như:

```text
max steps
max tokens
max tool calls
max cost
wall-clock deadline
repetition threshold
```

Agent cần biết khi nào phải dừng, abstain hoặc escalate thay vì tiếp tục vô hạn.

## Nguyên tắc 11: Context phải được Curate

Chỉ đưa vào context state và evidence liên quan. Tách trusted instruction khỏi untrusted content và giữ provenance.

Context càng dài không đồng nghĩa quyết định càng tốt.

## Nguyên tắc 12: Xem Tool Output và Retrieved Content là Untrusted

Document, email, website hoặc API response có thể chứa prompt injection hoặc dữ liệu sai.

External data không được tự nâng cấp thành instruction authority chỉ vì nó nằm trong model context.

## Nguyên tắc 13: Human Approval dựa trên Risk Class

Approval policy nên rõ ràng:

| Action | Mặc định |
|---|---|
| Search / read | tự động |
| Draft artifact | tự động |
| Sửa state có thể hoàn tác trong sandbox | tự động có kiểm soát |
| Gửi communication ra ngoài | thường cần approval |
| Production deploy | approval hoặc policy riêng |
| Xóa / chuyển tài sản nhạy cảm | approval nghiêm ngặt |

Policy cụ thể phụ thuộc domain và impact của failure.

## Nguyên tắc 14: Dùng Sandbox cho Exploration

Coding agent, browser agent hoặc data agent nên thử trong sandbox hoặc staging khi có thể. Failure trong isolated environment rẻ hơn nhiều so với production incident.

## Nguyên tắc 15: Ưu tiên Action có thể hoàn tác

Thứ tự an toàn thường là:

```text
observe → simulate → stage → verify → commit
```

Trì hoãn irreversible action tạo thêm cơ hội kiểm tra và recovery.

## Nguyên tắc 16: Tách Planner, Executor và Verifier

Không nhất thiết phải dùng ba model khác nhau, nhưng ba vai trò logic nên tách:

```text
planner  → đề xuất
executor → thực hiện operation được phép
verifier → kiểm acceptance criterion
```

Independent verifier giảm self-confirmation bias.

## Nguyên tắc 17: Giữ Provenance

Fact và decision nên truy được về evidence.

Với RAG hoặc research agent, citation cần map tới source chunk hoặc document. Với tool action, log phải giữ request, result và resource id liên quan.

## Nguyên tắc 18: Version Mutable State

Dùng optimistic concurrency khi phù hợp:

```text
đọc version 10
→ đề xuất update
→ chỉ commit nếu vẫn là version 10
```

Nếu state đã đổi, agent phải refetch rồi replan.

## Nguyên tắc 19: Theo dõi Economics

Một agent đáng tin nhưng chi phí không kiểm soát vẫn chưa production-ready.

Theo dõi:

```text
success per dollar
success per second
steps per task
retries per task
cost by tool/model
```

Optimization phải cân bằng quality, reliability, latency và cost.

## Nguyên tắc 20: Evaluation theo hướng Adversarial

Happy-path test chưa đủ. Cần chủ động đưa vào:

- dữ liệu stale;
- timeout;
- document độc hại;
- permission thiếu;
- partial success;
- state xung đột;
- goal thay đổi giữa chừng;
- tool result bất thường.

Hệ thống đáng tin cần fail an toàn khi assumption bị phá vỡ.

## Ví dụ kiến trúc Reliability

```mermaid
flowchart TD
    U[User Goal] --> O[Orchestrator]
    O --> P[Planner / LLM]
    P --> V[Policy & Schema Validation]
    V -->|safe read| T[Tool]
    V -->|risky write| H[Human Approval]
    H --> T
    T --> S[Persist Result / State]
    S --> Q[Verifier]
    Q -->|pass| O
    Q -->|fail / replan| P
    O -->|done| R[Final Result]
```

Điểm chính là model nằm bên trong một control structure có permission, validation, state và verification rõ ràng.

## Reliability Budget

Không phải mọi failure có impact giống nhau. Có thể ưu tiên engineering effort theo:

\[
Expected\ Loss = P(failure)\times Impact(failure)
\]

Một lỗi tóm tắt ít rủi ro có thể chấp nhận variance lớn hơn. Payment, deletion hoặc production deployment cần control nghiêm ngặt hơn nhiều.

## Graceful Degradation

Khi model hoặc tool unavailable, hệ thống có thể:

- chuyển sang fallback model;
- chuyển sang read-only mode;
- giảm scope;
- queue task để xử lý lại;
- handoff cho human.

Với high-risk write, nên **fail closed** thay vì improvisation không an toàn.

## Safe Default

Action mơ hồ nên mặc định về phương án không phá hủy.

Ví dụ nếu “remove” có thể nghĩa là hide hoặc delete vĩnh viễn, policy nên chọn operation có thể hoàn tác hoặc yêu cầu clarification trước destructive action.

## Auditability

Hệ thống cần lưu đủ để reconstruct:

```text
ai yêu cầu
state nào đã được quan sát
action nào được đề xuất
policy nào cho phép
approval nào đã xảy ra
tool thật sự đã làm gì
verifier đã thấy gì
```

Audit log cần mức chống tampering phù hợp với risk của domain.

## Data Privacy

Context minimization cũng là privacy control. Không gửi toàn bộ customer database cho model nếu task chỉ cần một record. Secret và PII nên được redact hoặc không đưa vào context nếu không cần thiết.

## Model Update là System Change

Đổi model version có thể làm tool selection, formatting và refusal behavior thay đổi. Hãy xử lý model upgrade giống dependency upgrade:

```text
offline eval
→ canary
→ monitor
→ rollback nếu cần
```

## Version Prompt, Tool Schema và Policy

Prompt template, tool schema và policy cần versioning để khi regression xảy ra có thể xác định chính xác configuration nào đã tạo hành vi đó.

## Incident Response

Khi agent gây incident, quy trình có thể gồm:

1. dừng hoặc cancel task bị ảnh hưởng;
2. thu hồi credential nguy hiểm nếu cần;
3. xác định side effect đã xảy ra;
4. rollback hoặc compensating action;
5. bảo toàn trace và log;
6. phân loại root cause;
7. thêm regression scenario vào eval suite.

## Mô hình tư duy

> **Reliable agent = probabilistic reasoning được giới hạn bên trong deterministic safety và systems boundary.**

Model không cần hoàn hảo nếu hệ thống có khả năng phát hiện, giới hạn và phục hồi failure tốt. Nhưng high-risk action không nên phụ thuộc vào khả năng “tự kiềm chế” của model.

## Những nhầm lẫn thường gặp

### “Model mạnh hơn sẽ giải quyết reliability”

Không. Model quality giúp giảm một số lỗi nhưng không thay transaction, authorization, state consistency hoặc observability.

### “Guardrail prompt là security boundary”

Không. Prompt chỉ là behavioral signal, không phải access-control mechanism.

### “Human-in-the-loop tự động làm hệ thống an toàn”

Không. Approval quá nhiều có thể dẫn tới rubber-stamping. Chỉ nên escalate risk thật sự và cung cấp context đủ rõ cho human reviewer.

### “Agent có thể tự verify mọi thứ”

Không. Verification đáng tin hơn khi dựa vào deterministic test, independent source hoặc external state có thể kiểm tra trực tiếp.

## Liên kết kiến thức

Thiết kế agent đáng tin cậy kết hợp Software Engineering, Security, Distributed Systems, Databases, HCI, AI Evaluation và classical control loop. Đây là điểm kết thúc layer Agent trước khi chuyển sang Reinforcement Learning, nơi policy được học trực tiếp từ reward và interaction.