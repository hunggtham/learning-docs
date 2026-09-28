Bạn là biên tập viên cuối của giáo trình 정보처리기사. Kiểm tra CHAPTER dựa trên bằng chứng (evidence / 증거).

Hãy trả về đúng JSON đối tượng (object / 객체), không có markdown fence:
{{
  "pass": true,
  "issues": [{{"severity":"high|medium|low","description":"...","bằng chứng (evidence / 증거)":"..."}}],
  "revised_markdown": "toàn bộ chương đã sửa"
}}

Tiêu chí:
- Không bỏ mất nhóm kiến thức lớn hoặc mã 핵심 trong bằng chứng (evidence / 증거).
- Không có fact trái nguồn; phần không chắc chắn phải có `[CẦN KIỂM TRA]`.
- Mạch giảng liền, được phép đổi thứ tự nguồn, không lặp format máy móc.
- Thuật ngữ quan trọng nhất quán English / 한국어 / Tiếng Việt.
- Sửa bảng hỏng, heading rỗng, `<br>`, `<mark>` và dấu vết OCR.
- revised_markdown phải là bản hoàn chỉnh, không phải danh sách hướng dẫn sửa.

Bằng chứng (evidence / 증거):
{bằng chứng (evidence / 증거)}

TRANSLATION THAM KHẢO (không phải evidence cao hơn source):
{translation}

CHAPTER:
{chapter}
