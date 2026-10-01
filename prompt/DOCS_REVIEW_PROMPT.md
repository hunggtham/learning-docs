# DOCS REVIEW PROMPT — Review after learner testing

Áp dụng prompt này sau [`COMMON_PROMPT.md`](./COMMON_PROMPT.md) khi người dùng đã đọc/test tài liệu và báo “không được”, sai, khó hiểu, thiếu fact hoặc không dùng được. Đây là vòng review có phản hồi thực tế; không phải pass QA hình thức.

## 1. Đầu vào bắt buộc

Nhận:

- file/chapter và canonical owner;
- bản Markdown hiện tại;
- test case, câu người học không trả lời được, kết quả thực thi, screenshot/log hoặc nhận xét cụ thể;
- nguồn đã dùng trước đó và mốc phiên bản/thời gian nếu có.

Nếu feedback mơ hồ, nêu đúng điểm cần làm rõ; không tự bịa lỗi hoặc tự thay đổi phạm vi file.

## 2. Cách review

1. Đọc README/canonical map và toàn bộ section liên quan trước khi sửa.
2. Chuyển feedback thành một claim hoặc thao tác có thể kiểm chứng: “không hiểu”, “sai kết quả”, “không tìm thấy owner”, “không phân biệt được A/B”, “ví dụ không chạy”, “nguồn đã cũ”.
3. Truy nguyên claim về nguồn chính thức. Ưu tiên văn bản owner, specification/release ổn định, tài liệu official của ngôn ngữ/framework, cơ quan thống kê hoặc nghiên cứu gốc. Dùng [W3C Standards](https://www.w3.org/standards/), [MDN](https://developer.mozilla.org/en-US/docs/Web), [Python Docs](https://docs.python.org/3/) và [Korean Law Information Center](https://www.law.go.kr/eng/engMain.do) đúng phạm vi; không dùng bản dịch luật như authority cuối cùng.
4. Phân loại nguyên nhân: fact sai, nguồn cũ, ví dụ sai, prerequisite thiếu, mạch giải thích đứt, câu nối máy móc, thuật ngữ không nhất quán, link/owner sai, hoặc test không đủ.
5. Viết lại thủ công đoạn nhỏ nhất có thể nhưng đủ để khôi phục mental model. Nếu sửa claim ở đầu làm thay đổi section sau, đọc lại toàn bộ chuỗi và sửa các handoff liên quan.
6. Chạy lại đúng test của người dùng hoặc mô phỏng cùng điều kiện. Ghi rõ cái gì đã pass, cái gì chưa thể chạy và vì sao.

Không dùng automation để dịch hàng loạt, thay thế thuật ngữ, chèn `Mạch đọc`/`Chuyển mạch`, xoá quiz hoặc làm cho checker xanh. Không rewrite phần không liên quan chỉ để làm diff đẹp.

## 3. Tiêu chí chấp nhận sau review

- feedback ban đầu có một câu trả lời cụ thể trong prose hoặc output;
- claim mới có nguồn chính thức và mốc phiên bản/ngày khi cần;
- ví dụ/code/công thức được kiểm tra trong điều kiện đã nêu;
- section có mở đầu, reasoning, câu nối theo topic và kết luận/bàn giao tự nhiên;
- các bảng/list/link có prose giải thích cách đọc và hệ quả;
- tiếng Việt là ngôn ngữ giải thích; English/Korean chỉ còn ở vị trí tra cứu cần thiết;
- không có quiz/mock exam/answer bank;
- các section kế cận không bị mâu thuẫn hoặc mất owner.

Nếu chưa đạt, trạng thái là `FAIL — cần review tiếp`, kèm một danh sách hành động cụ thể. Không dùng “đã sửa” thay cho bằng chứng test.

## 4. Đầu ra bắt buộc

1. **Feedback đã xử lý:** trích feedback và giải thích nguyên nhân.
2. **Nguồn đối chiếu:** URL, tiêu đề, phiên bản/ngày và claim được dùng.
3. **Thay đổi thủ công:** file/section, trước–sau ở mức đủ hiểu, và lý do sư phạm.
4. **Kết quả test:** lệnh/tình huống, output thực tế, trạng thái pass/fail.
5. **Markdown hoàn chỉnh:** trả toàn bộ file đã sửa nếu file là đầu ra cần thay thế; không trả patch rời khiến người dùng phải đoán.
6. **Giới hạn còn lại:** fact chưa xác minh, test chưa chạy hoặc quyết định cần người dùng.

Chỉ trả `PASS` khi feedback đã được tái hiện hoặc kiểm tra bằng chứng tương đương, nội dung đã được đọc lại như một lesson hoàn chỉnh, và không còn issue `high`.
