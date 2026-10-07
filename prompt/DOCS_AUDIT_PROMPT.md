# DOCS AUDIT PROMPT — Research, verify, rewrite by hand

Áp dụng prompt này sau [`COMMON_PROMPT.md`](./COMMON_PROMPT.md) khi audit một file/chapter đã viết. Mục tiêu là quyết định tài liệu có đủ căn cứ để giữ lại hay không. Nếu không pass, người viết phải nghiên cứu lại nguồn và viết lại thủ công các đoạn lỗi; không dùng script, regex, template hàng loạt, model worker hay thao tác thay tên heading để “đạt pass”.

## 1. Phạm vi đầu vào

Trước khi đọc prose, xác định:

- file đang audit và README/canonical owner của nó;
- đối tượng người học, prerequisite và câu hỏi trung tâm;
- các section có nội dung giảng dạy, kể cả `###`/`####`;
- các claim có thể thay đổi theo thời gian, claim pháp lý, số liệu, phiên bản, tiêu chuẩn hoặc tên tổ chức;
- test/link/report hiện có và thay đổi chưa commit trong working tree.

Không coi một file có heading, link hoặc nhiều thuật ngữ là đã đạt. Không xoá thay đổi không liên quan và không tự ý chuẩn hoá cả thư mục khi chỉ được giao một file.

## 2. Nghiên cứu nguồn chính thức trước khi kết luận

Với mỗi claim quan trọng, mở nguồn chính thức phù hợp và ghi URL, tiêu đề, ngày truy cập/phiên bản và claim mà nguồn chứng minh. Ưu tiên theo thứ tự:

1. văn bản pháp luật, cơ quan nhà nước, tiêu chuẩn hoặc tài liệu phát hành bởi owner của sản phẩm;
2. đặc tả chuẩn và bản phát hành ổn định của tổ chức tiêu chuẩn;
3. tài liệu chính thức của ngôn ngữ, runtime, framework hoặc thư viện;
4. bài nghiên cứu gốc, cơ quan thống kê hoặc tổ chức chuyên môn có phương pháp rõ;
5. nguồn thứ cấp chỉ dùng để định hướng, không dùng làm bằng chứng duy nhất cho claim nhạy cảm.

Ví dụ nguồn chuẩn: [W3C Standards](https://www.w3.org/standards/) và trạng thái tài liệu [W3C](https://www.w3.org/standards/types/) cho Web; [MDN Web APIs](https://developer.mozilla.org/en-US/docs/Web/API) cho cách dùng Web thực tế; [Python Documentation](https://docs.python.org/3/) cho Python; [Korean Law Information Center](https://www.law.go.kr/eng/engMain.do) cho luật Hàn Quốc. Bản dịch tiếng Anh của luật chỉ hỗ trợ đọc hiểu; khi có khác biệt, văn bản tiếng Hàn và cơ quan ban hành là nguồn quyết định.

Không trộn bản draft, editor's draft, blog cá nhân và bản đã ban hành như cùng một mức bằng chứng. Với tiêu chuẩn có nhiều URI, ghi rõ đang dùng bản cố định hay bản mới nhất. Với fact hiện hành, ghi mốc thời gian và không biến snapshot thành quy luật bất biến.

## 3. Checklist audit bắt buộc

### A. Ownership và cấu trúc

- README/canonical map có chỉ đúng owner, vị trí và đường quay lại không?
- internal links, anchor, tên file và numbering có tồn tại không?
- nội dung có bị duplicate hoặc lấn owner của file khác không?
- raw/imported/generated có bị coi nhầm là canonical prose không?

### B. Mạch giảng

Với từng section, ghi bằng chứng cho bốn điểm:

1. mở đầu định vị prerequisite và câu hỏi;
2. prose giải thích object/goal → mechanism/constraint → consequence;
3. câu nối giữa các khối (list/table/formula/code/example/link) nói quan hệ thật;
4. kết luận chốt mental model/boundary và bàn giao sang nhu cầu/section/owner kế tiếp.

Đánh `high` nếu có boilerplate, section nhảy cóc, raw block đứng một mình, claim không có nguồn, fact sai, câu đơn ngữ hoàn chỉnh hoặc quiz. Đánh `medium` nếu quan hệ đúng nhưng diễn đạt cứng, thiếu tổng hợp hoặc thiếu mốc nguồn. Đánh `low` cho lỗi wording không làm đổi mental model.

### C. Ngôn ngữ và tính tự nhiên

- prose giải thích chủ yếu bằng tiếng Việt tự nhiên;
- English/Korean chỉ giữ khi là thuật ngữ tra cứu, tên riêng, API, code, tiêu chuẩn hoặc trích dẫn cần thiết;
- không để nguyên một câu tiếng Anh/Hàn trong prose;
- không ghép gloss Việt–Anh–Hàn sau mọi từ khiến câu mất ngữ pháp;
- không có quiz, mock exam, active-recall bank, lựa chọn đáp án hoặc đáp án mẫu.

## 4. Quyết định và cách sửa

Trả về báo cáo gồm `PASS` hoặc `FAIL`, bảng issue với severity, vị trí, claim/evidence liên quan và hành động sửa. Nếu `FAIL`, không chỉ đưa danh sách lỗi: viết lại thủ công toàn bộ section bị ảnh hưởng, giữ nội dung đúng và link hợp lệ, thêm nguồn chính thức cần thiết, rồi audit lại chính đoạn vừa sửa. Không sửa bằng câu wrapper chung.

Một file chỉ được `PASS` khi mọi issue `high` đã đóng, issue `medium` còn lại có lý do chấp nhận được, nguồn truy được, prose tự nhiên, không quiz và người học có thể đi từ câu hỏi đến kết luận mà không cần đoán.

## 5. Đầu ra

Trả theo thứ tự:

1. phạm vi và owner đã kiểm tra;
2. nguồn chính thức đã dùng và claim được đối chiếu;
3. bảng audit `PASS/FAIL`;
4. bản Markdown hoàn chỉnh sau khi viết lại thủ công nếu cần;
5. các giới hạn chưa thể xác minh và việc cần người dùng quyết định.

Không trả “đã pass” chỉ vì đã chạy một lệnh. Lệnh chỉ là bằng chứng cấu trúc; chất lượng nội dung phải được chứng minh bằng đoạn văn, nguồn và reasoning cụ thể.

## Điều phối và đầu ra mới

Trước audit, đọc prompt/00_ORCHESTRATOR_PROMPT.md, task manifest, source manifest và semantic map nếu corpus có các artifact đó. Ghi task id, owner, base/current revision, allowed paths và acceptance criteria.

Khi FAIL, sửa section nhỏ nhất đủ khôi phục mental model; không mặc định rewrite toàn file. Trả changed sections và lý do sửa, trừ khi caller yêu cầu Markdown hoàn chỉnh để thay thế trực tiếp.

Kết quả phải tách content status, evidence status, Git status và publication status theo prompt/ACCEPTANCE_CONTRACT.md. Repo audit, link check hoặc build pass chỉ chứng minh phạm vi kỹ thuật tương ứng, không tự chứng minh prose hoặc learner usability.
