# Editorial QA tools

Thư mục này không còn chứa worker sinh hoặc viết lại learning docs bằng mô hình, script hàng loạt hay workflow tự động. Nội dung học phải được research, viết và sửa thủ công theo:

- [`../prompt/COMMON_PROMPT.md`](../prompt/COMMON_PROMPT.md) — contract nền;
- [`../prompt/DOCS_AUDIT_PROMPT.md`](../prompt/DOCS_AUDIT_PROMPT.md) — audit trước khi chấp nhận;
- [`../prompt/DOCS_REVIEW_PROMPT.md`](../prompt/DOCS_REVIEW_PROMPT.md) — review/fix sau khi người dùng test không đạt.

## QA cấu trúc không sinh nội dung

`repo_audit.py` chỉ kiểm tra catalog, đường dẫn và Markdown links; nó không sửa file và không tạo prose.

```bash
python -m unittest automation/test_repo_audit.py
python automation/repo_audit.py --root .
python automation/repo_audit.py --root . --strict-links
```

Các cảnh báo từ `raw/`, `raw_md/`, `workflow-output/` hoặc site generate phải được phân biệt với lỗi của canonical learning docs. Mọi thay đổi nội dung vẫn cần người viết xem diff, đối chiếu nguồn chính thức và sửa bằng tay.
