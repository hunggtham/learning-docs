# COMMON PROMPT — Learning Docs

Áp dụng file này làm contract tối thiểu cho tài liệu học và mọi thay đổi nội dung trong repository. Đây không phải template văn phong: người viết tự chọn độ dài, cấu trúc, thứ tự giải thích và mức độ chi tiết phù hợp với topic.

## Nguyên tắc nền

- Đọc README/canonical map, owner và các link liên quan trước khi sửa hoặc viết.
- Research claim quan trọng từ nguồn chính thức phù hợp; phân biệt canonical docs, raw/imported material và draft.
- Viết cho người học bằng tiếng Việt tự nhiên. Giữ English/Korean khi đó là thuật ngữ tra cứu, tên riêng, API, code, tiêu chuẩn hoặc trích dẫn cần thiết; không để nguyên câu prose đơn ngữ nếu có thể diễn đạt rõ bằng tiếng Việt.
- Giữ nội dung đúng, đủ ngữ cảnh và không mâu thuẫn với owner hoặc section liên quan. Độ sâu do người viết quyết định theo mục tiêu học, không thêm chi tiết chỉ để làm tài liệu dài hơn.
- Có thể dùng đoạn văn, bullet, bảng, công thức, code hoặc ví dụ theo cách phù hợp với nội dung. Không bắt buộc mọi section phải có cùng một nhịp, cùng số đoạn hay cùng nhãn.
- Câu mở, câu chốt và câu chuyển tiếp chỉ cần khi chúng giúp người đọc hiểu quan hệ hoặc định hướng. Viết chúng theo topic thật; không chèn wrapper chung, không thay tên section trong một khuôn cố định.
- Có thể viết ngắn nếu file là glossary/index/checklist/reference; có thể viết sâu nếu topic cần reasoning. Không bịa thêm bài giảng để làm đầy heading.
- Nội dung phải được viết và sửa thủ công. Không dùng worker, script, regex, template hoặc automation để dịch hàng loạt, chèn câu nối, thay thuật ngữ hay rewrite prose.

## Tự do tổ chức nội dung

Người viết tự quyết định:

- có cần mở đầu, kết luận, bảng hay ví dụ hay không;
- nên đi từ định nghĩa, tình huống, cơ chế, đối chiếu hay câu hỏi thực tế;
- section nào cần gộp, tách hoặc bỏ;
- thuật ngữ nào cần giữ nguyên để tra cứu và thuật ngữ nào chỉ cần nghĩa tiếng Việt;
- mức độ chi tiết phù hợp với prerequisite và mục tiêu của người học.

Không dùng các mục “Mục tiêu”, “Giải thích”, “Kết luận”, `Mạch đọc`, `Nối mạch`
hoặc `Chuyển mạch` chỉ vì prompt yêu cầu. Chỉ dùng khi chúng thực sự làm tài liệu
dễ đọc hơn. `Chuyển mạch` là nhãn legacy; nếu cần một nhãn cho câu nối hiện tại,
dùng `Nối mạch`.

## Mạch đọc và câu chuyển tiếp

Nếu dùng `Mạch đọc`, hãy lấy owner/vị trí từ README hoặc canonical map và mô tả
đúng đường đọc của file đó. Nếu dùng `Nối mạch`, phải gọi tên topic thật của phần
trước và phần sau, đồng thời nói rõ quan hệ giữa chúng: kế thừa, mở rộng, đối
chiếu, áp dụng, nguyên nhân–hệ quả hoặc một nhu cầu học tập cụ thể. Không tạo
`Nối mạch` chỉ để lặp lại thứ tự heading; có thể bỏ qua câu chuyển tiếp khi hai
phần đã tự nhiên nối nhau. Không thêm lại nhãn legacy `Chuyển mạch`.

Không dùng các câu rỗng như “xem tiếp”, “phần này trình bày…” hoặc “ta sang mục sau” nếu không nói rõ người học được gì từ việc chuyển sang đó. Không sao chép ví dụ trong prompt cho topic khác.

## Không tạo quiz

Learning docs không thêm quiz, mock exam, active-recall bank, lựa chọn đáp án, đáp án mẫu hoặc section câu hỏi kiểm tra. Khi review gặp một khối như vậy trong canonical docs, xóa khối đó; không xóa chữ `quiz` trong code, trích dẫn hoặc raw material ngoài phạm vi.

## Mức đạt tối thiểu

Một thay đổi đạt khi:

- owner, phạm vi và link chính có thể truy ra;
- claim quan trọng có nguồn hoặc được đánh dấu là chưa xác minh;
- prose tự nhiên, không có câu máy móc hoặc câu đơn ngữ không cần thiết;
- ví dụ/bảng/code, nếu có, phục vụ trực tiếp cho nội dung;
- không tạo duplicate hoặc làm mất nghĩa của tài liệu hiện có;
- không có quiz và không dùng automation để che lỗi.

Nếu chưa đủ bằng chứng, nói rõ giới hạn thay vì bịa hoặc ép nội dung vào một format.

## Quy trình an toàn

Giữ cấu trúc, naming và canonical ownership của repository. Kiểm tra diff, link và test phù hợp với phạm vi thay đổi; không tự ý chuẩn hóa cả thư mục hoặc xóa thay đổi không liên quan. `repo_audit.py` chỉ là công cụ QA cấu trúc, không thay thế việc đọc và biên tập nội dung bằng tay.

Mọi prompt chuyên môn kế thừa contract này nhưng có thể chọn cách trình bày riêng cho domain. Prompt chuyên môn không được biến các nguyên tắc trên thành một template bắt buộc nếu nội dung không cần.

## Điều phối task và bằng chứng

Trước khi viết, sửa hoặc audit, đọc prompt/00_ORCHESTRATOR_PROMPT.md và task manifest hiện tại. Task phải có task_id, canonical owner, allowed_paths, base revision, audience, learning outcome, acceptance test và stop condition.

Chọn đúng mode: INGEST để đăng ký nguồn; PLAN để lập semantic map; PILOT để kiểm tra hướng viết; AUTHOR để viết output; SELF_REVIEW để tự kiểm tra; LEARNER_REVIEW để xử lý feedback bằng delta nhỏ; ACCEPTANCE hoặc INTEGRATE để chốt evidence và revision.

Không để raw/original/ bị rewrite. Source research, reference mới và unresolved claims đặt trong research/; derived extraction/OCR phải ghi provenance. Nội dung canonical trong output/ phải truy nguyên được về source unit.

Ghi riêng content_status, evidence_status, git_status và publication_status. Không gọi tài liệu là hoàn thành chỉ vì checker xanh, agent đã dừng hoặc worktree đã tạo.
