# CROSS-TOOL AGENT CONTRACT — Codex, Daintree, Antigravity and ChatGPT Web

Các công cụ khác nhau có thể cùng tham gia một task, nhưng không được tạo các nguồn sự thật độc lập.

## Durable source of truth

- Git revision và repository artifacts là trạng thái bền vững.
- Daintree dashboard là trạng thái vận hành/live.
- Antigravity artifact là bằng chứng UI/browser/runtime.
- ChatGPT Web response là research/review artifact khi đã lưu vào file và ghi source/revision.

## Quyền theo surface

| Surface | Có thể đọc | Có thể sửa | Bằng chứng bắt buộc |
|---|---|---|---|
| Codex | repository, task manifest | canonical files trong allowed paths | test, diff, handoff |
| Daintree | worktree/agent state | dispatch, terminal, Git action theo quyền | task/worktree id |
| Antigravity | workspace, browser, dev server | assigned worktree và runtime artifacts | screenshot/recording/report |
| ChatGPT Web | source, GitHub revision, uploaded context | research/review artifacts khi được giao | source ledger, revision, limitations |

## Quy tắc chuyển giao

Mỗi handoff phải ghi task id, surface, worktree, base/current revision, changed paths, artifacts, validation, status và next action. Không dùng nội dung chat hoặc màu trạng thái của app làm bằng chứng thay thế.

Không để hai supervisor cùng mutate một worktree. Không broadcast một implementation prompt vào các task có shared paths. Dừng nếu source, permission hoặc revision không đủ rõ.
