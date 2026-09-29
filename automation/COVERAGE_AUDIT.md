# Automation — Coverage Audit

> **Mạch đọc:** Đặt audit này cạnh [README](./README.md). `automation/` là domain sở hữu các workflow và tooling phục vụ repository; nó không phải canonical owner của kiến thức Information Processing Engineer, AI, DevOps hay GitHub. Audit tập trung vào câu hỏi: workflow có đầu vào/đầu ra rõ, có invariant, có failure boundary, có evidence và có đường rollback hay không?

Cập nhật: 2026-09-29. `main` vẫn là nguồn chuẩn (source of truth / 정본); feature branch chỉ là nơi triển khai thay đổi trước merge.

## Phạm vi hiện tại

`automation/` hiện có bốn nhóm chức năng chính:

1. **Textbook generation worker** — `app.py`, `pipeline.py`, `Dockerfile`, `.env.example`, `prompts/` và workflow n8n cho pipeline 정보처리기사.
2. **Repository QA** — `repo_audit.py`, `test_repo_audit.py` và GitHub Actions tương ứng để kiểm `CATALOG.md` cùng Markdown links.
3. **Content transformation utilities** — các script như `bilingualize_learning_docs.mjs` và `retrofit_learning_connections.mjs` để sửa hàng loạt tài liệu theo contract của repository.
4. **Operational configuration** — environment variables, cost/run limits, push toggle và deployment assumptions.

Sự tồn tại của script không tự động có nghĩa workflow đã production-ready. Coverage được đánh giá theo contract và failure semantics, không theo số lượng file.

## Trạng thái coverage

| Boundary | Evidence hiện có | Trạng thái |
|---|---|---|
| Repository structural audit | catalog parsing, canonical path/entrypoint/date/scope validation, local Markdown link audit | Strong |
| Repository-audit unit tests | catalog parsing, fenced-code exclusion, local/external link behavior, missing-link failure, reference links | Strong |
| Textbook transformation core | five-subject split, OCR cleanup, core-ID alignment, output extraction | Moderate–Strong |
| Idempotency / duplicate-run prevention | input SHA-256 + manifest short-circuit | Moderate |
| Cost/run guardrails | API-call ceiling, per-run estimated cost ceiling, chunk/part limits | Moderate |
| Secret handling | secret values expected through environment; Git auth header kept out of remote URL | Moderate |
| Concurrency | worker-level in-process lock rejects simultaneous `/run` | Narrow |
| Output QA | draft → QA/revision path + quality report | Moderate |
| Recovery / rollback | reset to remote branch before run; push can be disabled | Moderate |
| Observability | `/health`, HTTP status, manifest/quality report and basic usage accounting | Basic |
| Multi-workflow orchestration | one n8n textbook workflow is present | Narrow |
| Generic automation platform | no stable generic workflow contract/registry yet | Gap |

## Bất biến cần giữ

### 1. Source-of-truth invariant

Automation không được tự biến generated output thành sự thật chỉ vì job chạy thành công.

```text
source/provenance
→ transform
→ validation
→ reviewable output
→ commit/push boundary
→ canonical merge
```

`process exit = success` không đồng nghĩa `content = correct`, và `push = success` không đồng nghĩa `canonical = approved`.

### 2. Reproducibility invariant

Một run có ý nghĩa phải xác định được tối thiểu:

- input identity/hash;
- code/version hoặc commit chạy transformation;
- prompt/config quan trọng;
- model/tool configuration khi workflow phụ thuộc external service;
- output identity;
- validation result.

Nếu không truy ngược được `output ← inputs + transform + config`, output chỉ là artifact khó kiểm chứng.

### 3. Idempotency invariant

Retry hoặc schedule lặp lại không được âm thầm tạo duplicate logical work. Manifest hash hiện giải quyết một trường hợp cụ thể cho textbook pipeline, nhưng các workflow mới phải tự định nghĩa idempotency key hoặc equivalent state transition.

### 4. Mutation boundary

Mọi automation có khả năng ghi repository phải tách rõ:

```text
read/plan
→ generate
→ validate
→ preview/diff
→ mutate
```

Default an toàn nên là không ghi khi chưa vượt validation gate. `PUSH_CHANGES=false` là một guardrail hữu ích nhưng không thay thế branch protection/review workflow.

### 5. Secret boundary

Token/API key không được xuất hiện trong committed config, generated Markdown, log hoặc command argument có thể bị lưu lại. `.env.example` chỉ được chứa placeholder và contract tên biến.

### 6. Failure atomicity

Nếu external API, Git operation, parser hoặc validation thất bại giữa run, workflow không được để lại trạng thái mà người đọc nhầm là output hoàn chỉnh. Temporary/intermediate state phải phân biệt được với reviewed output.

## Failure modes cần kiểm khi mở rộng

Một workflow mới nên trả lời được các tình huống sau trước khi được coi là ổn định:

- input thay đổi giữa lúc run đang chạy;
- job bị retry sau timeout dù lần đầu đã side-effect thành công;
- process chết sau khi ghi một phần output nhưng trước manifest/commit;
- API trả response hợp lệ về schema nhưng sai về nội dung;
- rate limit hoặc cost guard dừng run giữa nhiều chunk;
- branch đã tiến lên trong lúc worker đang xử lý snapshot cũ;
- hai worker chạy ở hai process/container khác nhau nên in-process lock không còn đủ;
- generated file làm hỏng internal link hoặc canonical metadata;
- prompt/model/config thay đổi nhưng input hash không đổi;
- external service version thay đổi làm behavior drift.

## Gaps ưu tiên

### P1 — Run manifest chung

Tách manifest từ textbook-specific thành contract dùng được cho mọi automation:

```text
run_id
input_revision / input_hashes
code_revision
config fingerprint
started_at / completed_at
outputs
validation status
mutation/commit SHA
```

Điều này giúp phân biệt content drift với code/config drift.

### P1 — Transaction-like publish boundary

Generated files nên được tạo trong staging/worktree riêng, chạy validation toàn bộ, sau đó mới promote thành commit. Với workflow nhiều file, không nên coi việc từng file ghi thành công là một run thành công.

### P1 — Cross-process concurrency/fencing

`asyncio.Lock()` bảo vệ một process FastAPI nhưng không bảo vệ nhiều replica hoặc hai deployment cùng chạy. Nếu worker được scale hoặc có nhiều scheduler, cần lease/fencing hoặc Git-based compare-and-swap trước mutation.

### P2 — Observability contract

Chuẩn hóa run log/summary quanh các field như stage, input revision, duration, API calls, estimated/actual usage, validation findings, output commit và failure class. Không cần monitoring stack lớn; trước hết cần semantics ổn định.

### P2 — Automation registry

Khi số workflow tăng, thêm một index/registry ngắn mô tả owner, trigger, inputs, outputs, mutation quyền, secrets, idempotency strategy và rollback path. Không biến README thành danh sách script rời rạc.

### P2 — Tests theo failure semantics

Unit tests hiện xác nhận nhiều pure transformation/audit behavior. Các test tiếp theo có giá trị cao hơn khi cover partial failure, stale branch, duplicate run, invalid QA payload, cost-stop giữa run và publish gate.

## Ranh giới canonical

- Kiến thức **정보처리기사** thuộc [`../정보처리기사/`](../정보처리기사/README.md); Automation chỉ sở hữu pipeline tạo/chuyển đổi artifact.
- Git/GitHub, CI/CD, container runtime và production platform mechanisms thuộc [`../devops_platform_engineering/`](../devops_platform_engineering/README.md).
- Software design, concurrency, files, parsing, network/API fundamentals thuộc [`../computer_science/`](../computer_science/README.md) hoặc Backend khi phù hợp.
- Prompt/output quality của một domain không được chuyển quyền sở hữu kiến thức domain sang `automation/`.

## Review protocol

Khi thêm hoặc sửa automation:

1. xác định input/output và source of truth;
2. ghi invariant + side effects + mutation boundary;
3. xác định idempotency/retry semantics;
4. bảo đảm secret không đi vào repository/log/output;
5. thêm test cho ít nhất một failure mode quan trọng;
6. chạy unit tests liên quan và `Repository audit`;
7. nếu workflow ghi nhiều canonical files, review diff trước merge;
8. cập nhật audit này chỉ khi xuất hiện capability/failure class mới, không cập nhật chỉ vì thêm một script tương tự.

> **Bàn giao:** Đọc [README](./README.md) để xem workflow hiện tại. Khi cần reasoning sâu về delivery/recovery/observability, chuyển sang [DevOps / Platform Engineering](../devops_platform_engineering/README.md); khi cần nội dung chứng chỉ, quay về [정보처리기사](../정보처리기사/README.md).