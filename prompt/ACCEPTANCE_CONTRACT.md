# ACCEPTANCE CONTRACT — content, evidence, integration and publication

Acceptance là quyết định dựa trên bằng chứng, không phải xác nhận rằng agent đã chạy xong.

## Các lớp trạng thái

Ghi độc lập:

~~~text
content_status: DRAFT | QA_PASS | LEARNER_PASS | USER_APPROVED
evidence_status: NONE | SOURCE_BACKED | TEST_BACKED | USER_VERIFIED
git_status: UNCOMMITTED | COMMITTED | MERGE_READY | INTEGRATED
publication_status: NOT_PUBLISHED | DEPLOYED | UNKNOWN
~~~

## Điều kiện PASS nội dung

- owner, audience, prerequisite và scope được xác định;
- claim quan trọng có source hoặc được đánh dấu chưa xác minh;
- semantic map không còn MISSING ngoài các mục có lý do được chấp nhận;
- pilot/full prose tạo được mental model, không chỉ có heading, keyword hoặc bảng;
- link, handoff và canonical ownership đúng;
- không có source-wrapper prose, quiz hoặc nội dung sinh hàng loạt làm che lỗi;
- test hoặc learner scenario đã chạy nếu task yêu cầu.

## Điều kiện MERGE_READY

- diff chỉ nằm trong allowed paths;
- base revision và current revision được ghi;
- validation commands/results có artifact;
- không còn conflict với task claim khác;
- generated output được tái sinh từ canonical source nếu có;
- known issues và giới hạn đã được ghi.

## Báo cáo bắt buộc

Trả PASS hoặc FAIL, không dùng DONE chung chung. Báo cáo phải nêu:

1. phạm vi và owner;
2. source/revision;
3. evidence theo từng acceptance criterion;
4. issue còn lại theo severity;
5. content/Git/publication status;
6. next action hoặc lý do dừng.

Một task chỉ được gọi là COMPLETED khi content đã đạt, evidence đủ, thay đổi đã tích hợp và publication status được xác nhận hoặc ghi rõ là chưa publish.
