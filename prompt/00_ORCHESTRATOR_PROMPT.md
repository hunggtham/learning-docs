# LEARNING-DOC ORCHESTRATOR — task routing and evidence contract

Đây là lớp điều phối cho mọi task tạo, chuyển đổi, audit hoặc sửa learning docs. Nó không thay thế \`COMMON_PROMPT.md\`; nó quyết định task đang ở mode nào, được phép chạm phạm vi nào và bằng chứng nào cần có trước khi chuyển mode.

## 1. Bắt buộc trước khi làm

Đọc task manifest và xác định:

- \`task_id\`, \`agent_surface\`, \`worktree\`, \`base_sha\`;
- canonical owner và \`allowed_paths\`;
- audience, learning outcome, prerequisite và non-goals;
- nguồn đầu vào, source state, currentness risk;
- acceptance test, artifact cần tạo và stop condition.

Nếu thiếu owner, source boundary hoặc allowed paths, dừng ở \`INTAKE_REQUIRED\`; không tự mở rộng phạm vi.

## 2. Các mode

| Mode | Mục tiêu | Đầu ra tối thiểu |
|---|---|---|
| \`INGEST\` | Đăng ký và kiểm tra nguồn | \`SOURCE_MANIFEST.yaml\`, source-quality note |
| \`PLAN\` | Lập semantic map và ownership | \`semantic-map.tsv\`, outline, dependency notes |
| \`PILOT\` | Kiểm tra hướng viết sớm | một section đại diện và pilot review |
| \`AUTHOR\` | Viết output theo map đã chốt | Markdown trong \`output/\` |
| \`SELF_REVIEW\` | Tự kiểm tra trước khi giao người đọc | source, coverage, prose, link report |
| \`LEARNER_REVIEW\` | Xử lý feedback thực tế | feedback triage và delta patch |
| \`ACCEPTANCE\` | Chốt bằng chứng và trạng thái | acceptance report |
| \`INTEGRATE\` | Kiểm tra diff, revision và generated output | integration handoff |

Không chuyển từ \`INGEST\` thẳng sang \`AUTHOR\` nếu chưa có semantic map và pilot, trừ khi task manifest ghi rõ đây là một file reference/index không cần pilot.

Khi task audit bản nháp, dùng thêm \`DOCS_AUDIT_PROMPT.md\`. Khi task có phản hồi learner/user đã cụ thể hóa, dùng \`DOCS_REVIEW_PROMPT.md\` cùng skill learner-feedback-triage; hai prompt này không thay thế task manifest hoặc acceptance contract.

## 3. Ranh giới nguồn

- \`raw/original/\` là bất biến sau khi đăng ký.
- \`raw/extracted/\`, \`raw/ocr/\`, \`raw/derived/\` là output chuyển đổi có provenance, không phải canonical prose.
- AI research, source comparison và reference mới nằm trong \`research/\`, không trộn vào raw.
- \`output/\` là learning prose canonical và phải truy nguyên được về source unit.

## 4. Agent surface

- Codex: canonical implementation, audit, integration.
- Daintree: dispatch, worktree, terminal và review dashboard.
- Antigravity: browser/UI/runtime verification và artifact.
- ChatGPT Web: source research, decision memo và learner/prose review.

Mỗi surface phải ghi \`agent_surface\`, revision/SHA và artifact trong handoff. Không coi trạng thái của một app là bằng chứng thay cho Git hoặc test.

## 5. Trạng thái độc lập

Ghi riêng:

\`\`\`text
content_status: DRAFT | QA_PASS | LEARNER_PASS | USER_APPROVED
git_status: UNCOMMITTED | COMMITTED | MERGE_READY | INTEGRATED
publication_status: NOT_PUBLISHED | DEPLOYED | UNKNOWN
\`\`\`

Chỉ dùng \`COMPLETED\` khi cả task manifest, acceptance report và integration evidence đã tồn tại.

## 6. Điều kiện dừng

Dừng và ghi \`BLOCKED\` nếu:

- source không truy được hoặc OCR không đủ tin cậy;
- ownership hoặc current-state boundary chưa rõ;
- task overlap với một claim đang hoạt động;
- test/acceptance không thể chạy trong môi trường hiện tại.

Không bịa source, không sửa raw để làm audit xanh, không commit hoặc publish ngoài phạm vi được giao.
