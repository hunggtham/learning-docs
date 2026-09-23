# COMMON PROMPT — Learning Docs

Áp dụng file này làm yêu cầu nền cho toàn bộ tài liệu và thay đổi tiếp theo trong repository.

## Nguyên tắc chung

- Luôn kiểm tra cấu trúc hiện tại, README, canonical files và internal links trước khi tạo hoặc sửa nội dung.
- Viết như một tài liệu học hoàn chỉnh để có thể đọc và hiểu trực tiếp, không phải note hoặc bản tóm tắt rời rạc.
- Giải thích theo luồng từ nền tảng đến nâng cao, đủ sâu để hiểu bản chất; không dừng ở giải thích ngắn, nửa chừng hoặc chỉ nêu kết luận.
- Ưu tiên understanding, reasoning, mechanism, first principles và connection giữa các concept hơn ghi nhớ máy móc.
- Nội dung phải liền mạch, tự nhiên, đủ ngữ cảnh; hạn chế bullet/table khi chúng làm đứt luồng đọc.
- Với thuật ngữ quan trọng, giữ hoặc note thuật ngữ tiếng Anh; khi có liên hệ phù hợp với kiến thức/ngữ cảnh Hàn Quốc, note thêm thuật ngữ tiếng Hàn. Giải thích ngay tại chỗ để người đọc không phải tự tra hoặc dịch thêm.
- Ví dụ chỉ thêm khi giúp hiểu rõ hơn, phải đúng bản chất và không làm lệch nội dung chuyên môn.
- Có thể chia nhỏ, gộp hoặc tổ chức lại file/topic nếu giúp việc học và điều hướng tốt hơn, nhưng không làm mất nội dung cần thiết.
- Tôn trọng cấu trúc, naming, liên kết và style chung của repository; tránh duplicate content và file cô lập.
- Không cá nhân hóa nội dung học theo người dùng trừ khi được yêu cầu rõ ràng.

## Branch & Git workflow

- `main` là trạng thái ổn định và canonical.
- Thay đổi lớn hoặc theo từng topic nên thực hiện trên branch riêng; kiểm tra nội dung, links và lỗi trước khi merge.
- Không giữ branch/commit dư thừa; sau khi merge, dọn các branch không còn cần thiết và giữ cấu trúc branch tối giản, rõ mục đích.

## Quy tắc kế thừa

Mọi yêu cầu mới sau này mặc định kế thừa file này.

Yêu cầu mới chỉ bổ sung hoặc override đúng phạm vi được nói rõ; các nguyên tắc còn lại vẫn giữ nguyên.