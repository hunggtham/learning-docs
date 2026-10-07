# Tiến độ review câu nối tài liệu

Cập nhật gần nhất: **2026-10-07 (Asia/Seoul)**

## Tiêu chí Review prompt

- Câu nối phải nói đúng quan hệ giữa các topic đang đứng cạnh nhau, không dùng
  boilerplate kiểu “tiếp nhận điểm tựa” hoặc “đọc liền hai mục”.
- Owner của mỗi tài liệu phải lấy từ README/entrypoint canonical của domain.
- Phần giải thích dùng tiếng Việt; thuật ngữ Hàn/Anh chỉ giữ cạnh nghĩa Việt khi
  cần đối chiếu.
- Không thêm quiz, mock exam, answer bank hoặc lời gọi “tự kiểm tra” vào phần
  giải thích.
- Mỗi batch phải chạy `repo_audit.py --strict-links`, unit tests và
  `git diff --check` trước khi commit.

## Trạng thái hiện tại

Phạm vi **chưa hoàn tất**. Snapshot live của checkout hiện tại:

| Chỉ số | Giá trị |
|---|---:|
| File còn connector cũ `Chuyển mạch` | 991 |
| File còn mẫu câu nối cũ | 914 |
| File có connector malformed `Nối mạch:***` | 0 |
| File bị broad scan đánh dấu từ khóa quiz/self-check | 122 |

Broad scan chỉ là danh sách cần rà lại; không phải mọi kết quả đều là quiz thực
thụ. Các thay đổi dirty/staged ngoài phạm vi review được giữ nguyên và không đưa
vào những commit checkpoint.

### Phạm vi còn lại theo domain (file có connector cũ)

| Domain | Còn lại |
|---|---:|
| `computer_science` | 396 |
| `정보처리기사` | 264 |
| `korea_business_economy_knowledge_library` | 62 |
| `philosophy` | 60 |
| `electrical_engineering` | 31 |
| `10_backend` | 30 |
| `devops_platform_engineering` | 20 |
| `data_engineering` | 20 |
| `economics` | 18 |
| `sql` | 17 |
| `linux` | 16 |
| Các domain nhỏ còn lại | 77 |

## Checkpoint đã commit

Mỗi commit dưới đây đã pass audit/test/diff-check trong phạm vi batch của nó:

- `68bb55bb`, `5745c65a`, `87e129f8`, `d5bc93bb`, `9deaccd5`, `bf858e59`,
  `77c30327`, `fad55689`: các batch `정보처리기사`.
- `53af8e54`, `9ea48b12`, `1a70ba0c`, `33616533`, `91151a62`: các batch
  physics.
- `de9f18be`, `3b25c396`, `05986463`, `2d9466c7`: các batch mathematics.
- `e0ac5af6`, `d1b0b048`, `b8a25136`: các batch psychology.
- `f023d6c3`, `11fd3f0e`, `333acf3d`, `8c80a046`: các batch investing.
- `ce7650b4`, `9af3e1a1`, `01e93033`: KIIP/Korean culture.
- `fed2e2a9`: Vietnam history.
- `7e290cd7`, `2f3b19ae`, `cc7c2aaf`, `4796cb8a`, `ed6a765e`, `3544cd0c`:
  chemistry.
- `2dbb7f9b`, `4c623208`: Linux.
- `75ea7a1d`, `ce846235`: Kotlin/Swift.
- `45f398bf`, `b83dfef8`: frontend/JavaScript.

## Publication checkpoint

- `main` đã đồng bộ với `origin/main` bằng `git merge --ff-only origin/main`;
  kết quả: **Already up to date**.
- `94d4781b` đã được push thành công lên `origin/main`.
- Commit local đi kèm trước đó là `30ccc804`; không có thay đổi unrelated nào
  được stage hoặc commit trong checkpoint này.

## Prompt contract checkpoint

- `94ff05ad` cập nhật `prompt/COMMON_PROMPT.md`: `Nối mạch` là nhãn hiện tại,
  `Chuyển mạch` là legacy; câu nối phải gọi tên topic thật, nói quan hệ thật và
  lấy owner/vị trí từ README hoặc canonical map.
- Prompt vẫn giữ yêu cầu giải thích tiếng Việt, không quiz và audit từng batch;
  các batch sau phải dùng contract này.

## Branch cleanup checkpoint

- Local branch `codex/connection-sentence-updates` đã được xoá sau khi xác nhận
  branch là ancestor của `main`, không có commit riêng và không có remote branch
  tương ứng.
- Worktree detached `/Users/mac/.codex/worktrees/507a/00.my-learning` vẫn được
  giữ vì còn thư mục untracked `life/`; không xoá tự động dữ liệu chưa xác định
  owner. Cần một chỉ dẫn riêng nếu muốn xoá toàn bộ worktree đó.

## Project cleanup snapshot — 2026-10-07

- Local cleanup hiện có **354 ảnh JPG** trong `증권투자기초/raw/sach1/` được xoá;
  source map đã được ghi chú rằng các số trang/ảnh chỉ còn là provenance.
- Có **145 file Markdown/text bị xoá** và **20 file được sửa** trong các nhóm
  module cũ; các source canonical còn được tham chiếu (`automation` và raw
  `sach2/sach3`) đã được khôi phục trước khi commit.
- Có **10 artifact untracked có chủ đích** gồm prompt/skill/template/workflow
  contracts; các thư mục `__pycache__` không được đưa vào commit.
- Full audit sau khi khôi phục source còn **143 lỗi link**: chủ yếu là link
  generated-site trỏ ngược về source tree và link URL OCR trong raw Notion; đây
  là backlog cần xử lý riêng, không che bằng cách bỏ audit.
- Cleanup checkpoint đã commit ở `32cf47e0`; unit tests `automation/test_repo_audit.py`
  vẫn pass `6/6`. Một số trailing spaces trong Markdown là hard-break có chủ ý;
  raw OCR đã được chuẩn hoá newline/whitespace thừa.

### Git cleanup

- `main` đã merge/push tới `0fe25e33` và local/remote đang cùng revision.
- Đã xoá 7 local branch merged/không còn commit riêng: `codex/kiip-main-merge`,
  `codex/remove-selection-translation`, `codex/review-feature-branches`,
  `feat/korean-history`, `feat/learning-docs-bilingual-continuity`,
  `feat/marxism-leninism-learning-module`, `feat/vietnamese-history-depth`.
- Giữ các branch còn unique commit hoặc thuộc task khác; không xoá remote branch
  khi chưa xác định owner. Worktree detached có untracked `life/` vẫn được giữ.

## Cách cập nhật file này

Sau mỗi batch tiếp theo, cập nhật snapshot số lượng, thêm hash commit mới và ghi
domain/batch vừa xử lý. Không sửa hoặc stage các thay đổi unrelated chỉ để làm
đẹp báo cáo tiến độ.

Lệnh kiểm tra chuẩn:

```bash
python3 automation/repo_audit.py --files-from /tmp/batchNNN-review.md --strict-links
python3 -m unittest automation/test_repo_audit.py
git diff --check -- $(cat /tmp/batchNNN-review.md)
```
