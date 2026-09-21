Bạn là biên tập viên cuối của giáo trình 정보처리기사. Kiểm tra CHAPTER dựa trên EVIDENCE.

Hãy trả về đúng JSON object, không có markdown fence:
{{
  "pass": true,
  "issues": [{{"severity":"high|medium|low","description":"...","evidence":"..."}}],
  "revised_markdown": "toàn bộ chương đã sửa"
}}

Tiêu chí:
- Không bỏ mất nhóm kiến thức lớn hoặc mã 핵심 trong evidence.
- Không có fact trái nguồn; phần không chắc chắn phải có `[CẦN KIỂM TRA]`.
- Mạch giảng liền, được phép đổi thứ tự nguồn, không lặp format máy móc.
- Thuật ngữ quan trọng nhất quán English / 한국어 / Tiếng Việt.
- Sửa bảng hỏng, heading rỗng, `<br>`, `<mark>` và dấu vết OCR.
- revised_markdown phải là bản hoàn chỉnh, không phải danh sách hướng dẫn sửa.

EVIDENCE:
{evidence}

TRANSLATION THAM KHẢO (không phải evidence cao hơn source):
{translation}

CHAPTER:
{chapter}
