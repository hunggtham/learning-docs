# Thiết kế hệ thống AI an toàn

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Secure AI system design**. Route đi từ threat model → trust boundaries → least privilege/data isolation → validation and monitoring → safe failure and response, để security controls bám vào kiến trúc chứ không thêm sau cùng.

**Thiết kế hệ thống AI an toàn (secure AI system design / 안전한 AI 시스템 설계)** đặt thành phần học máy hoặc LLM bên trong một kiến trúc bảo mật có authentication, authorization, isolation, kiểm tra hợp lệ (validation / 검증), auditing và khôi phục (recovery / 복구) rõ ràng. Nguyên tắc nền tảng là:

> **Mô hình không phải ranh giới bảo mật (security boundary / 보안 경계).**

LLM có thể đề xuất hành động, diễn giải ngữ nghĩa hoặc chọn công cụ (tool / 도구), nhưng backend mới quyết định định danh (identity / 식별자), permission, tài nguyên (resource / 자원) phạm vi (scope / 범위), ngân sách (budget / 예산) và side tác động (effect / 효과) nào thực sự được phép xảy ra.

## Kiến thức tiên quyết

Nên đọc trước [Prompt Injection](./03_prompt_injection_and_jailbreaks.md), [Reliable Agent Design](../10_agents_and_ai_systems/10_reliable_agent_design.md), [Reliability Engineering](../18_evaluation_reliability_interpretability/07_reliability_engineering.md), [Tool Calling](../10_agents_and_ai_systems/01_tools_and_function_calling.md), [Data Governance](../14_data_for_ai/08_data_governance.md) và [AI System Design](../15_ai_engineering/10_ai_system_design.md).

> **Chuyển mạch:** Trong **Thiết kế hệ thống AI an toàn**, **Bắt đầu bằng threat mô hình (model / 모델)** tiếp nhận điểm tựa từ **Kiến thức tiên quyết** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ranh giới tin cậy ngoài mô hình** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bắt đầu bằng threat mô hình (model / 모델)

Trước khi chọn điều khiển (control / 제어), cần lập **mô hình đe dọa (threat model)**:

```text
assets          → dữ liệu, credential, money, code, model, reputation
actors          → user, attacker, insider, compromised service
entry points    → prompt, file upload, API, RAG corpus, tool output
trust boundaries→ user/app, app/model, model/tool, tenant/tenant
privileges      → read, write, execute, deploy, transfer
attack paths    → injection, exfiltration, poisoning, privilege escalation
controls        → authz, sandbox, validation, approval, audit
```

Threat mô hình (model / 모델) phải mô tả luồng dữ liệu (data / 데이터) và điều khiển (control / 제어) thực tế, không chỉ sơ đồ mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **Thiết kế hệ thống AI an toàn**, **Ranh giới tin cậy ngoài mô hình** tiếp nhận điểm tựa từ **Bắt đầu bằng threat mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Authentication và Authorization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Natural-language instruction không thay IAM, ACL, RBAC/ABAC hoặc chính sách (policy / 정책) engine.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thiết kế hệ thống AI an toàn**, **Authentication và Authorization** tiếp nhận điểm tựa từ **Ranh giới tin cậy ngoài mô hình** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Principle of Least Privilege** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Authentication và Authorization

**Xác thực (authentication)** trả lời “ai đang gọi?”.

**Phân quyền (authorization)** trả lời “định danh (identity / 식별자) đó được làm gì trên tài nguyên (resource / 자원) nào?”.

Một tác nhân (agent / 에이전트) biết `user_id` không có nghĩa nó được quyền thực hiện mọi hành động (action / 동작) thay người dùng (user / 사용자). Authorization phải được kiểm ở mỗi ranh giới (boundary / 경계) có side tác động (effect / 효과) hoặc dữ liệu (data / 데이터) truy cập (access / 접근) nhạy cảm.

> **Chuyển mạch:** Trong **Thiết kế hệ thống AI an toàn**, **Principle of Least Privilege** tiếp nhận điểm tựa từ **Authentication và Authorization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Capability-based tooling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Principle of Least Privilege

Mỗi mô hình (model / 모델) session, dịch vụ (service / 서비스) account và công cụ (tool / 도구) chỉ nên có quyền tối thiểu cần thiết.

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

Giảm quyền làm giảm **blast radius** nếu mô hình (model / 모델) bị prompt injection hoặc mắc lỗi.

> **Chuyển mạch:** Ở chặng này của **Thiết kế hệ thống AI an toàn**, **Capability-based tooling** tiếp nhận điểm tựa từ **Principle of Least Privilege** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình (model / 모델) đề xuất, backend quyết định** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Capability-based tooling

Thay công cụ (tool / 도구) toàn quyền bằng năng lực (capability / 역량) hẹp và typed:

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

Công cụ (tool / 도구) hẹp dễ authorize, kiểm thử (test / 테스트), kiểm tra (audit / 감사) và áp nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thiết kế hệ thống AI an toàn**, **Mô hình (model / 모델) đề xuất, backend quyết định** tiếp nhận điểm tựa từ **Capability-based tooling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증) không đủ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình (model / 모델) đề xuất, backend quyết định

Một điều khiển (control / 제어) luồng (flow / 흐름) môi trường vận hành (production / 운영 환경) tốt:

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

Điều này tách **lập luận (reasoning / 추론) xác suất** khỏi **authority xác định**.

> **Chuyển mạch:** Trong **Thiết kế hệ thống AI an toàn**, **Lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증) không đủ** tiếp nhận điểm tựa từ **Mô hình (model / 모델) đề xuất, backend quyết định** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chính sách (policy / 정책) engine** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증) không đủ

JSON đúng kiểu (type / 타입) không đồng nghĩa hành động (action / 동작) đúng.

```json
{"amount":1000000000,"currency":"KRW"}
```

có thể hoàn toàn đúng lược đồ (schema / 스키마) nhưng vượt giao dịch (transaction / 트랜잭션) limit hoặc không thuộc account người dùng (user / 사용자).

Do đó cần ngữ nghĩa (semantic / 의미적)/nghiệp vụ (business / 비즈니스) kiểm tra hợp lệ (validation / 검증) sau lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증).

> **Chuyển mạch:** Ở chặng này của **Thiết kế hệ thống AI an toàn**, **Chính sách (policy / 정책) engine** tiếp nhận điểm tựa từ **Lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증) không đủ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Human approval đúng cách** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chính sách (policy / 정책) engine

Chính sách (policy / 정책) engine nên kiểm các quy tắc (rule / 규칙) có thể xác định bằng mã (code / 코드):

```text
resource ownership
role / permission
transaction limit
region restriction
approval requirement
allowed destination
working hours nếu domain yêu cầu
```

Chính sách (policy / 정책) càng quan trọng thì càng không nên chỉ tồn tại dưới dạng câu văn trong prompt.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thiết kế hệ thống AI an toàn**, **Human approval đúng cách** tiếp nhận điểm tựa từ **Chính sách (policy / 정책) engine** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Retrieval Authorization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Human approval đúng cách

Với hành động (action / 동작) high-impact hoặc irreversible:

```text
model proposal
→ backend chuẩn hóa structured action
→ hiển thị exact parameters
→ human confirm
→ backend re-authorize
→ execute
```

Không nên dùng câu tóm tắt tự do do LLM viết làm giao diện approval duy nhất.

> **Chuyển mạch:** Trong **Thiết kế hệ thống AI an toàn**, **Retrieval Authorization** tiếp nhận điểm tựa từ **Human approval đúng cách** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tenant Isolation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Retrieval Authorization

Với RAG đa tenant, authorization phải xảy ra **trước khi chunk vào ngữ cảnh (context / 맥락)**.

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

Cross-tenant véc-tơ (vector / 벡터) tìm kiếm (search / 검색) và bộ nhớ đệm (cache / 캐시) key thiếu tenant ID là lỗi rất nguy hiểm.

> **Chuyển mạch:** Ở chặng này của **Thiết kế hệ thống AI an toàn**, **Tenant Isolation** tiếp nhận điểm tựa từ **Retrieval Authorization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Secret Management** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tenant Isolation

Ranh giới (boundary / 경계) tenant phải tồn tại xuyên suốt:

```text
relational query
vector metadata filter
cache key
memory namespace
object storage path
logs
artifact store
```

Một lớp đúng không bù được lớp khác sai. Ví dụ cơ sở dữ liệu (database / 데이터베이스) ACL đúng nhưng ngữ nghĩa (semantic / 의미적) bộ nhớ đệm (cache / 캐시) dùng key chỉ theo truy vấn (query / 쿼리) văn bản (text / 텍스트) vẫn có thể rò dữ liệu chéo tenant.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thiết kế hệ thống AI an toàn**, **Secret Management** tiếp nhận điểm tựa từ **Tenant Isolation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sandboxing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Secret Management

Credential nằm trong secret manager hoặc executor backend. mô hình (model / 모델) chỉ nhận opaque năng lực (capability / 역량).

Không đưa API key, password hoặc long-lived đơn vị từ (token / 토큰) vào hệ thống (system / 시스템) prompt, ngữ cảnh (context / 맥락) hoặc công cụ (tool / 도구) description.

Nếu công cụ (tool / 도구) cần credential:

```text
model chọn tool
→ executor kiểm permission
→ executor inject credential server-side
→ credential không đi qua model context
```

> **Chuyển mạch:** Trong **Thiết kế hệ thống AI an toàn**, **Sandboxing** tiếp nhận điểm tựa từ **Secret Management** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mạng (network / 네트워크) Segmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sandboxing

Mã (code / 코드)/trình duyệt (browser / 브라우저)/tệp (file / 파일) công cụ (tool / 도구) nên chạy trong sandbox có:

- filesystem phạm vi (scope / 범위) nhỏ;
- mạng (network / 네트워크) allowlist;
- CPU/bộ nhớ (memory / 메모리)/thời gian (time / 시간) quota;
- tiến trình (process / 프로세스) restriction;
- credential tối thiểu;
- môi trường tạm thời khi phù hợp.

Sandbox giảm rủi ro nhưng không phải guarantee tuyệt đối. Cấu hình sandbox, kernel/bộ chứa (container / 컨테이너) ranh giới (boundary / 경계) và mạng (network / 네트워크) egress vẫn cần hardening.

> **Chuyển mạch:** Ở chặng này của **Thiết kế hệ thống AI an toàn**, **Mạng (network / 네트워크) Segmentation** tiếp nhận điểm tựa từ **Sandboxing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tệp (file / 파일) Upload và Parser bảo mật (security / 보안)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mạng (network / 네트워크) Segmentation

Tác nhân (agent / 에이전트) công cụ (tool / 도구) runner không nên mặc định truy cập toàn bộ nội bộ (internal / 내부) mạng (network / 네트워크).

Allowlist dịch vụ (service / 서비스) cần thiết và chặn private/nội bộ (internal / 내부) destination không thuộc tác vụ (task / 작업) giúp giảm nguy cơ mô hình (model / 모델) bị biến thành pivot kiểu SSRF.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thiết kế hệ thống AI an toàn**, **Tệp (file / 파일) Upload và Parser bảo mật (security / 보안)** tiếp nhận điểm tựa từ **Mạng (network / 네트워크) Segmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình (model / 모델) đầu ra (output / 출력) cũng là đầu vào (input / 입력) không đáng tin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tệp (file / 파일) Upload và Parser bảo mật (security / 보안)

PDF, ảnh (image / 이미지), archive hoặc office document đều là đầu vào (input / 입력) không đáng tin.

Cần:

```text
MIME/type validation
file-size limit
decompression limit
parser isolation
malware scanning khi phù hợp
resource/time limit
```

AI tính năng (feature / 기능) thường làm ứng dụng phải xử lý nhiều loại tệp (file / 파일) hơn, từ đó mở rộng attack surface truyền thống.

> **Chuyển mạch:** Trong **Thiết kế hệ thống AI an toàn**, **Mô hình (model / 모델) đầu ra (output / 출력) cũng là đầu vào (input / 입력) không đáng tin** tiếp nhận điểm tựa từ **Tệp (file / 파일) Upload và Parser bảo mật (security / 보안)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tỷ lệ (rate / 비율) Limit, Quota và chi phí (cost / 비용) bảo mật (security / 보안)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình (model / 모델) đầu ra (output / 출력) cũng là đầu vào (input / 입력) không đáng tin

Không trực tiếp đưa mô hình (model / 모델) văn bản (text / 텍스트) vào:

- shell;
- SQL;
- HTML;
- URL fetcher;
- mã (code / 코드) executor;
- chính sách (policy / 정책) expression.

Mẫu (pattern / 패턴) phù hợp:

```text
text generation
→ parse thành structured representation
→ validate/allowlist
→ deterministic executor
```

Đối với SQL, ưu tiên truy vấn (query / 쿼리) template hoặc parameterized API thay vì raw SQL tự do nếu use trường hợp (case / 사례) cho phép.

> **Chuyển mạch:** Ở chặng này của **Thiết kế hệ thống AI an toàn**, **Mô hình (model / 모델) đầu ra (output / 출력) cũng là đầu vào (input / 입력) không đáng tin** đã nêu tiêu chí phân biệt, còn **Tỷ lệ (rate / 비율) Limit, Quota và chi phí (cost / 비용) bảo mật (security / 보안)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Idempotency và giao dịch (transaction / 트랜잭션) an toàn (safety / 안전)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tỷ lệ (rate / 비율) Limit, Quota và chi phí (cost / 비용) bảo mật (security / 보안)

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

Chi phí (cost / 비용) runaway là một dạng availability/economic attack.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thiết kế hệ thống AI an toàn**, **Tỷ lệ (rate / 비율) Limit, Quota và chi phí (cost / 비용) bảo mật (security / 보안)** đã nêu tiêu chí phân biệt, còn **Idempotency và giao dịch (transaction / 트랜잭션) an toàn (safety / 안전)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Optimistic tính đồng thời (concurrency / 동시성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Idempotency và giao dịch (transaction / 트랜잭션) an toàn (safety / 안전)

Thử lại (retry / 재시도) hoặc tác nhân (agent / 에이전트) vòng lặp (loop / 루프) có thể gọi ghi (write / 쓰기) công cụ (tool / 도구) nhiều lần. Side-effect thao tác (operation / 연산) cần idempotency key, giao dịch (transaction / 트랜잭션) ID hoặc tài nguyên (resource / 자원) phiên bản (version / 버전).

Ví dụ:

```text
create_payment(request_id="task-42-step-7", ...)
```

Lặp lại cùng logical yêu cầu (request / 요청) không được tạo payment mới.

> **Chuyển mạch:** Trong **Thiết kế hệ thống AI an toàn**, **Optimistic tính đồng thời (concurrency / 동시성)** tiếp nhận điểm tựa từ **Idempotency và giao dịch (transaction / 트랜잭션) an toàn (safety / 안전)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Supply-chain bảo mật (security / 보안)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Optimistic tính đồng thời (concurrency / 동시성)

Mutable tài nguyên (resource / 자원) nên có phiên bản (version / 버전):

```text
đọc version 10
→ model đề xuất update
→ chỉ ghi nếu resource vẫn version 10
```

Nếu tài nguyên (resource / 자원) thành phiên bản (version / 버전) 11, thời gian chạy (runtime / 런타임) trả xung đột (conflict / 충돌) để tác nhân (agent / 에이전트) refetch và replan. Điều này ngăn hành động (action / 동작) dựa trên trạng thái (state / 상태) stale.

> **Chuyển mạch:** Ở chặng này của **Thiết kế hệ thống AI an toàn**, **Supply-chain bảo mật (security / 보안)** tiếp nhận điểm tựa từ **Optimistic tính đồng thời (concurrency / 동시성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình (model / 모델) sản phẩm tạo ra (artifact / 산출물) là code-like asset** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Supply-chain bảo mật (security / 보안)

AI hệ thống (system / 시스템) phụ thuộc nhiều sản phẩm tạo ra (artifact / 산출물):

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

Cần provenance, băm (hash / 해시)/signature khi phù hợp, phụ thuộc (dependency / 의존성) scanning, sản phẩm tạo ra (artifact / 산출물) registry và kiểm soát nguồn tải mô hình (model / 모델). Xem [Model and Supply Chain Security](./07_model_and_supply_chain_security.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thiết kế hệ thống AI an toàn**, **Mô hình (model / 모델) sản phẩm tạo ra (artifact / 산출물) là code-like asset** tiếp nhận điểm tựa từ **Supply-chain bảo mật (security / 보안)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Logging và kiểm tra (audit / 감사)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình (model / 모델) sản phẩm tạo ra (artifact / 산출물) là code-like asset

Mô hình (model / 모델) tệp (file / 파일) hoặc tokenizer không nên được tải từ nguồn không kiểm soát rồi đưa thẳng vào môi trường vận hành (production / 운영 환경) thời gian chạy (runtime / 런타임). Một số serialization format hoặc loader có thể có hành vi (behavior / 동작) nguy hiểm nếu thực thi đối tượng (object / 객체) tùy ý.

Nguyên tắc là dùng format/tải (load / 로드) đường dẫn (path / 경로) an toàn, sản phẩm tạo ra (artifact / 산출물) provenance rõ và sandbox quá trình xử lý sản phẩm tạo ra (artifact / 산출물) lạ.

> **Chuyển mạch:** Trong **Thiết kế hệ thống AI an toàn**, **Logging và kiểm tra (audit / 감사)** tiếp nhận điểm tựa từ **Mô hình (model / 모델) sản phẩm tạo ra (artifact / 산출물) là code-like asset** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bảo mật (security / 보안) khả năng quan sát (observability / 관측 가능성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Logging và kiểm tra (audit / 감사)

Nhật ký kiểm tra (audit log / 감사 로그) cần đủ để reconstruct:

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

Nhật ký kiểm tra (audit log / 감사 로그) cũng là dữ liệu nhạy cảm và cần kiểm soát truy cập (access control / 접근 제어), retention và tamper resistance phù hợp.

> **Chuyển mạch:** Ở chặng này của **Thiết kế hệ thống AI an toàn**, **Bảo mật (security / 보안) khả năng quan sát (observability / 관측 가능성)** tiếp nhận điểm tựa từ **Logging và kiểm tra (audit / 감사)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kill Switch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bảo mật (security / 보안) khả năng quan sát (observability / 관측 가능성)

Các tín hiệu (signal / 신호) cần theo dõi:

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

Bảo mật (security / 보안) monitoring nên nối với dấu vết (trace / 추적) của tác nhân (agent / 에이전트)/RAG để biết attack đường dẫn (path / 경로) đi qua thành phần (component / 컴포넌트) nào.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thiết kế hệ thống AI an toàn**, **Kill Switch** tiếp nhận điểm tựa từ **Bảo mật (security / 보안) khả năng quan sát (observability / 관측 가능성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Secure-by-default và fail-safe defaults** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Thiết kế hệ thống AI an toàn**, **Secure-by-default và fail-safe defaults** tiếp nhận điểm tựa từ **Kill Switch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Defense in độ sâu (depth / 깊이): ví dụ tác nhân (agent / 에이전트) gửi email** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Secure-by-default và fail-safe defaults

Khi authorization hoặc tài nguyên (resource / 자원) phạm vi (scope / 범위) không rõ, privileged hành động (action / 동작) nên bị từ chối.

```text
unknown permission
→ deny / request approval
```

Đây là **fail-safe default**. Hệ thống không nên “đoán quyền” để tối ưu convenience.

> **Chuyển mạch:** Ở chặng này của **Thiết kế hệ thống AI an toàn**, **Secure-by-default và fail-safe defaults** cho ta quy tắc; **Defense in độ sâu (depth / 깊이): ví dụ tác nhân (agent / 에이전트) gửi email** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Defense in độ sâu (depth / 깊이): ví dụ RAG doanh nghiệp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Defense in độ sâu (depth / 깊이): ví dụ tác nhân (agent / 에이전트) gửi email

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thiết kế hệ thống AI an toàn**, **Defense in độ sâu (depth / 깊이): ví dụ tác nhân (agent / 에이전트) gửi email** cho ta quy tắc; **Defense in độ sâu (depth / 깊이): ví dụ RAG doanh nghiệp** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Defense in độ sâu (depth / 깊이): ví dụ RAG doanh nghiệp

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

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

Bảo mật (security / 보안) không nằm ở một prompt mà nằm trong toàn bộ dữ liệu (data / 데이터) đường dẫn (path / 경로).

> **Chuyển mạch:** Trong **Thiết kế hệ thống AI an toàn**, **Defense in độ sâu (depth / 깊이): ví dụ RAG doanh nghiệp** cho ta quy tắc; **Sự đánh đổi (trade-off / 트레이드오프)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Dạng thất bại (failure mode / 실패 모드) của bảo mật (security / 보안) kiến trúc (architecture / 아키텍처)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sự đánh đổi (trade-off / 트레이드오프)

Bảo mật (security / 보안) điều khiển (control / 제어) có chi phí:

- approval tăng độ trễ (latency / 지연 시간);
- sandbox giảm flexibility;
- công cụ (tool / 도구) hẹp tăng số API phải thiết kế;
- ACL filter có thể giảm recall nếu siêu dữ liệu (metadata / 메타데이터) sai;
- logging/redaction tăng kỹ thuật (engineering / 엔지니어링) độ phức tạp (complexity / 복잡도);
- thất bại (fail / 실패) closed có thể giảm availability.

Mục tiêu không phải “khóa mọi thứ”, mà đặt điều khiển (control / 제어) tương xứng với impact của thất bại (failure / 실패).

> **Chuyển mạch:** Ở chặng này của **Thiết kế hệ thống AI an toàn**, **Dạng thất bại (failure mode / 실패 모드) của bảo mật (security / 보안) kiến trúc (architecture / 아키텍처)** tiếp nhận điểm tựa từ **Sự đánh đổi (trade-off / 트레이드오프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Môi trường vận hành (production / 운영 환경) bản phát hành (release / 릴리스) checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dạng thất bại (failure mode / 실패 모드) của bảo mật (security / 보안) kiến trúc (architecture / 아키텍처)

Phần này kiểm tra ranh giới và failure mode của cơ chế vừa học. Hãy dùng nó để biết khi nào mô hình còn đúng, khi nào cần đổi chiến lược và bằng chứng nào phải thu thập.

- authorization chỉ kiểm ở UI;
- mô hình (model / 모델) được truyền credential raw;
- véc-tơ (vector / 벡터) tìm kiếm (search / 검색) không có tenant filter;
- bộ nhớ đệm (cache / 캐시) không không gian tên (namespace / 네임스페이스) theo người dùng (user / 사용자)/tenant;
- approval dùng summary do mô hình (model / 모델) tự viết;
- sandbox vẫn có mạng (network / 네트워크)/secret quá rộng;
- công cụ (tool / 도구) generic hơn nhu cầu thực;
- chính sách (policy / 정책) không re-check ngay trước thực thi (execution / 실행);
- log chứa PII/secret quá mức;
- fallback đường dẫn (path / 경로) bỏ qua bảo mật (security / 보안) gate của primary đường dẫn (path / 경로).

Fallback và emergency chế độ (mode / 모드) phải giữ bảo mật (security / 보안) invariants giống đường chính.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thiết kế hệ thống AI an toàn**, **Môi trường vận hành (production / 운영 환경) bản phát hành (release / 릴리스) checklist** tiếp nhận điểm tựa từ **Dạng thất bại (failure mode / 실패 모드) của bảo mật (security / 보안) kiến trúc (architecture / 아키텍처)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Môi trường vận hành (production / 운영 환경) bản phát hành (release / 릴리스) checklist

Trước khi mở năng lực (capability / 역량) mới, nên kiểm:

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

> **Chuyển mạch:** Trong **Thiết kế hệ thống AI an toàn**, **Mô hình tư duy** gom các mảnh từ **Môi trường vận hành (production / 운영 환경) bản phát hành (release / 릴리스) checklist** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> **Dùng mô hình cho nhận định và sinh nội dung; dùng điều khiển (control / 제어) xác định cho quyền hạn, containment và side tác động (effect / 효과).**

Bảo mật (security / 보안) tốt không giả định mô hình (model / 모델) luôn nghe lời. Nó giả định mô hình (model / 모델) có thể bị nhầm, bị thao túng hoặc trả đầu ra (output / 출력) bất ngờ, rồi thiết kế sao cho lỗi đó không tự động biến thành quyền truy cập hoặc hành động nguy hiểm.

> **Chuyển mạch:** Ở chặng này của **Thiết kế hệ thống AI an toàn**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “mô hình (model / 모델) refusal là kiểm soát truy cập (access control / 접근 제어)”

Không. Authorization phải được backend cưỡng chế.

### “RAG nội bộ nên được tin cậy tuyệt đối”

Không. Nội dung có thể malicious, stale hoặc thuộc quyền của tenant khác.

### “Có sandbox thì chạy gì cũng được”

Không. Sandbox vẫn cần phạm vi quyền, mạng (network / 네트워크), tài nguyên (resource / 자원) limit và hardening.

### “bảo mật (security / 보안) chỉ cần kiểm trước mô hình (model / 모델)”

Không. đầu ra (output / 출력) mô hình (model / 모델), công cụ (tool / 도구) lời gọi (call / 호출), retrieval kết quả (result / 결과) và side tác động (effect / 효과) đều là trust ranh giới (boundary / 경계) riêng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thiết kế hệ thống AI an toàn**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Đọc cùng [Prompt Injection](./03_prompt_injection_and_jailbreaks.md), [Privacy Attacks](./06_privacy_attacks_and_data_protection.md), [Supply Chain Security](./07_model_and_supply_chain_security.md), [Reliable Agent Design](../10_agents_and_ai_systems/10_reliable_agent_design.md), [Reliability Engineering](../18_evaluation_reliability_interpretability/07_reliability_engineering.md), [AI System Design](../15_ai_engineering/10_ai_system_design.md) và [LLMOps](../16_mlops_and_llmops/08_llmops.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
