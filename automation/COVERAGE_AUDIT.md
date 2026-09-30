# Automation — kiểm toán phạm vi và độ tin cậy

> **Mạch đọc:** Đọc audit này cạnh [README](./README.md). `automation/` sở hữu workflow và tooling phục vụ repository; nó không sở hữu kiến thức của 정보처리기사, AI, DevOps hay GitHub. Câu hỏi trung tâm là: **một automation có đầu vào/đầu ra rõ, giữ được bất biến nào, thất bại ở đâu, để lại bằng chứng gì và khôi phục thế nào?**

**Ngày rà soát:** 2026-09-29. `main` là nguồn chuẩn (source of truth / 정본); feature branch chỉ là nơi chuẩn bị thay đổi trước merge.

## 1. Phạm vi hiện tại

`automation/` hiện có bốn nhóm chức năng: worker sinh giáo trình 정보처리기사; Repository QA cho `CATALOG.md` và internal Markdown links; utility chuyển đổi hàng loạt như bilingualization/learning-connection retrofit; và cấu hình vận hành như environment variables, cost/run limit, push toggle và deployment assumptions.

Một script tồn tại không đồng nghĩa workflow đã đáng tin cậy ở production. Audit phải nhìn vào **hợp đồng (contract / 계약)**, **tính lũy đẳng (idempotency / 멱등성)**, **ranh giới thay đổi trạng thái (mutation boundary / 변경 경계)**, **bằng chứng chạy (run evidence / 실행 증거)** và **ngữ nghĩa thất bại (failure semantics / 실패 의미론)**.

## 2. Phần hiện đã mạnh

Repository auditor đã có kiểm tra catalog structure, canonical path/entrypoint/date/scope và local Markdown links; unit tests cũng bao phủ parsing, fenced-code exclusion, missing links và reference links. Textbook pipeline đã có input SHA-256, manifest, giới hạn API/cost, QA/revision path và khả năng tắt push.

Các cơ chế này tạo nền tốt, nhưng cần hiểu giới hạn của chúng. Ví dụ SHA-256 input giúp tránh xử lý lại cùng input trong một pipeline cụ thể, nhưng không tự giải quyết concurrent run giữa hai process; `PUSH_CHANGES=false` giúp chặn mutation nhưng không thay thế review/branch protection; process exit code không chứng minh content đúng.

## 3. Các bất biến cần giữ

### Nguồn chuẩn và provenance

Automation phải giữ chuỗi:

```text
source/provenance
→ transform
→ validation
→ reviewable output
→ commit/push boundary
→ canonical merge
```

`job success` không đồng nghĩa `content correct`, và `push success` không đồng nghĩa `canonical approved`.

### Khả năng tái tạo (reproducibility / 재현성)

Một run có ý nghĩa cần truy được ít nhất input revision/hash, code revision, prompt/config quan trọng, model/tool configuration nếu có external service, output identity và validation result. Nếu không dựng lại được `output ← inputs + transform + config`, artifact rất khó audit.

### Tính lũy đẳng (idempotency / 멱등성)

Retry hoặc schedule lặp lại không được tạo duplicate logical work. Mỗi workflow phải xác định idempotency key hoặc state transition tương đương, thay vì mặc định “chạy lại chắc không sao”.

### Ranh giới mutation

Automation có quyền ghi repository phải tách rõ:

```text
read/plan
→ generate
→ validate
→ preview/diff
→ mutate
```

Mặc định an toàn là chưa mutate khi validation chưa pass.

### Secret boundary

Token/API key không được đi vào committed config, generated Markdown, log hoặc command argument dễ bị lưu lại. `.env.example` chỉ giữ placeholder và tên biến.

### Failure atomicity

Nếu API, Git operation, parser hoặc validation chết giữa run, output trung gian phải phân biệt rõ với output đã review. Workflow nhiều file không nên coi “đã ghi được vài file” là success.

## 4. Failure mode phải nghĩ trước khi mở rộng

Cần xem xét input đổi giữa run; retry sau timeout khi side effect lần đầu đã thành công; process chết sau partial output; QA response đúng schema nhưng sai nghĩa; cost/rate limit dừng giữa batch; branch tiến lên khi worker đang dùng snapshot cũ; hai worker ở hai process/container; prompt/model/config drift dù input hash không đổi; hoặc external service đổi behavior.

Các tình huống này quan trọng vì chúng tạo lỗi **không nhìn thấy bằng happy-path test**.

## 5. Khoảng trống ưu tiên

### P1 — Run manifest dùng chung

Cần một contract thống nhất:

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

Nhờ đó có thể phân biệt input drift, code drift và config drift.

### P1 — Publish giống transaction

Generated files nên đi vào staging/worktree, validate toàn bộ rồi mới promote thành commit. Với multi-file workflow, publish nên là một logical unit thay vì chuỗi ghi file độc lập.

### P1 — Concurrency xuyên process

`asyncio.Lock()` chỉ bảo vệ một FastAPI process. Nếu có nhiều replica/scheduler, cần lease/fencing hoặc Git compare-and-swap trước mutation để ngăn hai run cùng publish từ snapshot cũ.

### P2 — Observability contract

Run summary nên có stage, input revision, duration, API calls/usage, validation findings, output commit và failure class. Không cần monitoring stack phức tạp trước; cần semantics ổn định trước.

### P2 — Automation registry

Khi workflow tăng, thêm registry ngắn: owner, trigger, inputs, outputs, mutation permission, secrets, idempotency strategy và rollback path. Mục tiêu là biết “workflow này chịu trách nhiệm gì”, không phải tạo danh sách script.

### P2 — Test theo failure semantics

Ưu tiên test stale branch, partial failure, duplicate run, invalid QA payload, cost-stop giữa run và publish failure. Đây là những test có giá trị hơn việc chỉ tăng happy-path coverage.

## 6. Ranh giới canonical

Nội dung 정보처리기사 thuộc [`../정보처리기사/`](../정보처리기사/README.md). Git/GitHub, CI/CD, container runtime và platform mechanisms thuộc [`../devops_platform_engineering/`](../devops_platform_engineering/README.md). Software design, concurrency, parsing và network/API fundamentals thuộc [`../computer_science/`](../computer_science/README.md) hoặc Backend khi phù hợp.

Automation chỉ sở hữu **quá trình biến đổi và kiểm soát**, không được giành ownership của kiến thức domain chỉ vì nó sinh ra file của domain đó.

## 7. Quy trình review và bàn giao

Khi thêm automation, xác định input/output và source of truth; ghi invariant, side effect và mutation boundary; xác định idempotency/retry semantics; kiểm secret; thêm ít nhất một failure-mode test có giá trị; chạy unit tests + Repository audit; review diff trước merge nếu ghi canonical files.

Khi cần reasoning sâu về delivery/recovery/observability, bàn giao sang [DevOps / Platform Engineering](../devops_platform_engineering/README.md). Khi cần nội dung chứng chỉ, quay về [정보처리기사](../정보처리기사/README.md).