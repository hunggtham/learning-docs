# Editorial QA tools

Thư mục này không còn chứa worker sinh hoặc viết lại learning docs bằng mô hình, script hàng loạt hay workflow tự động. Nội dung học phải được research, viết và sửa thủ công theo:

- [`../prompt/COMMON_PROMPT.md`](../prompt/COMMON_PROMPT.md) — contract nền;
- [`../prompt/DOCS_AUDIT_PROMPT.md`](../prompt/DOCS_AUDIT_PROMPT.md) — audit trước khi chấp nhận;
- [`../prompt/DOCS_REVIEW_PROMPT.md`](../prompt/DOCS_REVIEW_PROMPT.md) — review/fix sau khi người dùng test không đạt.

## Provenance và runtime boundary

[Source Ledger](./SOURCES.md) ghi version/runtime/config boundary cho Git, Python, Node và CI tools. Green CI hoặc script exit 0 chỉ chứng minh job/context đã chạy; không tự chứng minh live provider hay publication state.

## QA cấu trúc không sinh nội dung

`repo_audit.py` chỉ kiểm tra catalog, đường dẫn và Markdown links; nó không sửa file và không tạo prose.

## Worker dependencies

The optional `app.py` worker and `pipeline.py` require the pinned packages in
[`requirements.txt`](./requirements.txt). Recreate the worker environment with:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r automation/requirements.txt
python -m unittest discover -s automation -p 'test_*.py'
```

The repository auditor itself remains standard-library only, so CI can run its
structural checks without installing the worker dependencies.

```bash
python -m unittest automation/test_repo_audit.py
python automation/repo_audit.py --root .
python automation/repo_audit.py --root . --strict-links
```

Các cảnh báo từ `raw/`, `raw_md/`, `workflow-output/` hoặc site generate phải được phân biệt với lỗi của canonical learning docs. Mọi thay đổi nội dung vẫn cần người viết xem diff, đối chiếu nguồn chính thức và sửa bằng tay.
