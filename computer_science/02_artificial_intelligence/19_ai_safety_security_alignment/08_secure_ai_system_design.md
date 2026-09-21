# Thiết kế hệ thống AI an toàn

**Thiết kế hệ thống AI an toàn (secure AI system design / 안전한 AI 시스템 설계)** đặt thành phần học máy hoặc LLM bên trong một kiến trúc bảo mật có authentication, authorization, isolation, validation, auditing và recovery rõ ràng. Nguyên tắc nền tảng là:

> **Mô hình không phải security boundary.**

LLM có thể đề xuất hành động, diễn giải ngữ nghĩa hoặc chọn tool, nhưng backend mới quyết định identity, permission, resource scope, budget và side effect nào thực sự được phép xảy ra.

## Kiến thức tiên quyết

Nên đọc trước [Prompt Injection](./03_prompt_injection_and_jailbreaks.md), [Reliable Agent Design](../10_agents_and_ai_systems/10_reliable_agent_design.md), [Reliability Engineering](../18_evaluation_reliability_interpretability/07_reliability_engineering.md), [Tool Calling](../10_agents_and_ai_systems/01_tools_and_function_calling.md), [Data Governance](../14_data_for_ai/08_data_governance.md) và [AI System Design](../15_ai_engineering/10_ai_system_design.md).

## Bắt đầu bằng threat model

Trước khi chọn control, cần lập **mô hình đe dọa (threat model)**:

```text
assets          → dữ liệu, credential, money, code, model, reputation
actors          → user, attacker, insider, compromised service
entry points    → prompt, file upload, API, RAG corpus, tool output
trust boundaries→ user/app, app/model, model/tool, tenant/tenant
privileges      → read, write, execute, deploy, transfer
attack paths    → injection, exfiltration, poisoning, privilege escalation
controls        → authz, sandbox, validation, approval, audit
```

Threat model phải mô tả luồng data và control thực tế, không chỉ sơ đồ model.

## Ranh giới tin cậy ngoài mô hình

Backend phải tự quyết định:

```text
user là ai?
được đọc resource nào?
được gọi tool nào?
được ghi dữ liệu nào?
được chi tiêu bao nhiêu?
action nào cần approval?
```

Natural-language instruction không thay IAM, ACL, RBAC/ABAC hoặc policy engine.

## Authentication và Authorization

**Xác thực (authentication)** trả lời “ai đang gọi?”.

**Phân quyền (authorization)** trả lời “identity đó được làm gì trên resource nào?”.

Một Agent biết `user_id` không có nghĩa nó được quyền thực hiện mọi action thay user. Authorization phải được kiểm ở mỗi boundary có side effect hoặc data access nhạy cảm.

## Principle of Least Privilege

Mỗi model session, service account và tool chỉ nên có quyền tối thiểu cần thiết.

Ví dụ:

```text
support assistant
→ read_ticket
→ read_order_status
→ draft_reply

không mặc định có:
→ raw_sql
→ delete_account
→ production_shell
```

Giảm quyền làm giảm **blast radius** nếu model bị prompt injection hoặc mắc lỗi.

## Capability-based tooling

Thay tool toàn quyền bằng capability hẹp và typed:

```text
get_order_status(order_id)
request_refund(order_id, amount, reason)
create_case_note(case_id, text)
```

so với:

```text
http_request(...)
execute_sql(...)
shell(...)
```

Tool hẹp dễ authorize, test, audit và áp business rule hơn.

## Model đề xuất, backend quyết định

Một control flow production tốt:

```text
LLM đề xuất action
→ schema validation
→ semantic validation
→ authorization
→ policy/risk check
→ approval nếu cần
→ scoped executor
→ verify side effect
→ audit
```

Điều này tách **reasoning xác suất** khỏi **authority xác định**.

## Schema validation không đủ

JSON đúng type không đồng nghĩa action đúng.

```json
{"amount":1000000000,"currency":"KRW"}
```

có thể hoàn toàn đúng schema nhưng vượt transaction limit hoặc không thuộc account user.

Do đó cần semantic/business validation sau schema validation.

## Policy engine

Policy engine nên kiểm các rule có thể xác định bằng code:

```text
resource ownership
role / permission
transaction limit
region restriction
approval requirement
allowed destination
working hours nếu domain yêu cầu
```

Policy càng quan trọng thì càng không nên chỉ tồn tại dưới dạng câu văn trong prompt.

## Human approval đúng cách

Với action high-impact hoặc irreversible:

```text
model proposal
→ backend chuẩn hóa structured action
→ hiển thị exact parameters
→ human confirm
→ backend re-authorize
→ execute
```

Không nên dùng câu tóm tắt tự do do LLM viết làm giao diện approval duy nhất.

## Retrieval Authorization

Với RAG đa tenant, authorization phải xảy ra **trước khi chunk vào context**.

```text
user identity
→ ACL filter
→ candidate documents
→ retrieval/ranking
→ context
```

Không nên:

```text
retrieve mọi document
→ đưa vào LLM
→ prompt “đừng tiết lộ phần user không được xem”
```

Cross-tenant vector search và cache key thiếu tenant ID là lỗi rất nguy hiểm.

## Tenant Isolation

Boundary tenant phải tồn tại xuyên suốt:

```text
relational query
vector metadata filter
cache key
memory namespace
object storage path
logs
artifact store
```

Một lớp đúng không bù được lớp khác sai. Ví dụ database ACL đúng nhưng semantic cache dùng key chỉ theo query text vẫn có thể rò dữ liệu chéo tenant.

## Secret Management

Credential nằm trong secret manager hoặc executor backend. Model chỉ nhận opaque capability.

Không đưa API key, password hoặc long-lived token vào system prompt, context hoặc tool description.

Nếu tool cần credential:

```text
model chọn tool
→ executor kiểm permission
→ executor inject credential server-side
→ credential không đi qua model context
```

## Sandboxing

Code/browser/file tool nên chạy trong sandbox có:

- filesystem scope nhỏ;
- network allowlist;
- CPU/memory/time quota;
- process restriction;
- credential tối thiểu;
- môi trường tạm thời khi phù hợp.

Sandbox giảm rủi ro nhưng không phải guarantee tuyệt đối. Cấu hình sandbox, kernel/container boundary và network egress vẫn cần hardening.

## Network Segmentation

Agent tool runner không nên mặc định truy cập toàn bộ internal network.

Allowlist service cần thiết và chặn private/internal destination không thuộc task giúp giảm nguy cơ model bị biến thành pivot kiểu SSRF.

## File Upload và Parser Security

PDF, image, archive hoặc office document đều là input không đáng tin.

Cần:

```text
MIME/type validation
file-size limit
decompression limit
parser isolation
malware scanning khi phù hợp
resource/time limit
```

AI feature thường làm ứng dụng phải xử lý nhiều loại file hơn, từ đó mở rộng attack surface truyền thống.

## Model Output cũng là input không đáng tin

Không trực tiếp đưa model text vào:

- shell;
- SQL;
- HTML;
- URL fetcher;
- code executor;
- policy expression.

Pattern phù hợp:

```text
text generation
→ parse thành structured representation
→ validate/allowlist
→ deterministic executor
```

Đối với SQL, ưu tiên query template hoặc parameterized API thay vì raw SQL tự do nếu use case cho phép.

## Rate Limit, Quota và Cost Security

Abuse không nhất thiết đánh cắp dữ liệu; attacker có thể làm tăng chi phí.

Cần quota theo:

```text
request / minute
token / day
concurrent jobs
agent steps
tool calls
file size
external API spend
```

Cost runaway là một dạng availability/economic attack.

## Idempotency và transaction safety

Retry hoặc Agent loop có thể gọi write tool nhiều lần. Side-effect operation cần idempotency key, transaction ID hoặc resource version.

Ví dụ:

```text
create_payment(request_id="task-42-step-7", ...)
```

Lặp lại cùng logical request không được tạo payment mới.

## Optimistic concurrency

Mutable resource nên có version:

```text
đọc version 10
→ model đề xuất update
→ chỉ ghi nếu resource vẫn version 10
```

Nếu resource thành version 11, runtime trả conflict để Agent refetch và replan. Điều này ngăn action dựa trên state stale.

## Supply-chain security

AI system phụ thuộc nhiều artifact:

```text
model weights
container image
Python/package dependencies
CUDA/runtime
embedding model
parser
prompt template
RAG corpus
tool integration
```

Cần provenance, hash/signature khi phù hợp, dependency scanning, artifact registry và kiểm soát nguồn tải model. Xem [Model and Supply Chain Security](./07_model_and_supply_chain_security.md).

## Model artifact là code-like asset

Model file hoặc tokenizer không nên được tải từ nguồn không kiểm soát rồi đưa thẳng vào production runtime. Một số serialization format hoặc loader có thể có behavior nguy hiểm nếu thực thi object tùy ý.

Nguyên tắc là dùng format/load path an toàn, artifact provenance rõ và sandbox quá trình xử lý artifact lạ.

## Logging và Audit

Audit log cần đủ để reconstruct:

```text
ai yêu cầu
resource nào
model/tool version nào
action nào được đề xuất
policy nào cho phép/chặn
approval nào xảy ra
executor đã làm gì
result/resource version sau cùng
```

Audit log cũng là dữ liệu nhạy cảm và cần access control, retention và tamper resistance phù hợp.

## Security Observability

Các signal cần theo dõi:

```text
permission denied rate
blocked high-risk action
unusual tool sequence
cross-tenant query attempt
prompt-injection detection signal
secret-redaction event
sandbox violation
cost spike
model/tool supply-chain change
```

Security monitoring nên nối với trace của Agent/RAG để biết attack path đi qua component nào.

## Kill Switch

Nên có khả năng disable nhanh:

```text
một tool cụ thể
một provider
một workflow
một model version
một tenant integration
```

Fine-grained kill switch giúp containment mà không cần tắt toàn bộ sản phẩm.

## Secure-by-default và fail-safe defaults

Khi authorization hoặc resource scope không rõ, privileged action nên bị từ chối.

```text
unknown permission
→ deny / request approval
```

Đây là **fail-safe default**. Hệ thống không nên “đoán quyền” để tối ưu convenience.

## Defense in Depth: ví dụ Agent gửi email

```text
User request
→ authenticate
→ LLM draft recipient/body
→ schema validation
→ recipient allowlist / organization policy
→ content DLP check nếu cần
→ user approval
→ scoped email API
→ rate limit
→ log message ID
→ verify send result
```

Nếu LLM bị prompt injection, các lớp sau vẫn giới hạn impact.

## Defense in Depth: ví dụ RAG doanh nghiệp

```text
User
→ authenticate
→ tenant + ACL filter
→ retrieve
→ provenance/trust metadata
→ LLM
→ citation verifier
→ output redaction/policy
→ audit
```

Security không nằm ở một prompt mà nằm trong toàn bộ data path.

## Trade-off

Security control có chi phí:

- approval tăng latency;
- sandbox giảm flexibility;
- tool hẹp tăng số API phải thiết kế;
- ACL filter có thể giảm recall nếu metadata sai;
- logging/redaction tăng engineering complexity;
- fail closed có thể giảm availability.

Mục tiêu không phải “khóa mọi thứ”, mà đặt control tương xứng với impact của failure.

## Failure mode của security architecture

- authorization chỉ kiểm ở UI;
- model được truyền credential raw;
- vector search không có tenant filter;
- cache không namespace theo user/tenant;
- approval dùng summary do model tự viết;
- sandbox vẫn có network/secret quá rộng;
- tool generic hơn nhu cầu thực;
- policy không re-check ngay trước execution;
- log chứa PII/secret quá mức;
- fallback path bỏ qua security gate của primary path.

Fallback và emergency mode phải giữ security invariants giống đường chính.

## Production release checklist

Trước khi mở capability mới, nên kiểm:

```text
threat model đã cập nhật?
permission boundary nằm ở backend?
RAG ACL chạy trước model context?
tool có least privilege?
write action có idempotency?
state có versioning?
high-risk action có approval phù hợp?
secret có nằm ngoài prompt?
sandbox/network đã giới hạn?
security eval có regression suite?
kill switch đã test?
audit trace có đủ để điều tra?
```

## Mô hình tư duy

> **Dùng mô hình cho nhận định và sinh nội dung; dùng control xác định cho quyền hạn, containment và side effect.**

Security tốt không giả định model luôn nghe lời. Nó giả định model có thể bị nhầm, bị thao túng hoặc trả output bất ngờ, rồi thiết kế sao cho lỗi đó không tự động biến thành quyền truy cập hoặc hành động nguy hiểm.

## Những nhầm lẫn thường gặp

### “Model refusal là access control”

Không. Authorization phải được backend cưỡng chế.

### “RAG nội bộ nên được tin cậy tuyệt đối”

Không. Nội dung có thể malicious, stale hoặc thuộc quyền của tenant khác.

### “Có sandbox thì chạy gì cũng được”

Không. Sandbox vẫn cần phạm vi quyền, network, resource limit và hardening.

### “Security chỉ cần kiểm trước model”

Không. Output model, tool call, retrieval result và side effect đều là trust boundary riêng.

## Liên kết kiến thức

Đọc cùng [Prompt Injection](./03_prompt_injection_and_jailbreaks.md), [Privacy Attacks](./06_privacy_attacks_and_data_protection.md), [Supply Chain Security](./07_model_and_supply_chain_security.md), [Reliable Agent Design](../10_agents_and_ai_systems/10_reliable_agent_design.md), [Reliability Engineering](../18_evaluation_reliability_interpretability/07_reliability_engineering.md), [AI System Design](../15_ai_engineering/10_ai_system_design.md) và [LLMOps](../16_mlops_and_llmops/08_llmops.md).