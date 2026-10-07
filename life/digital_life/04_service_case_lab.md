# Case lab: chọn một dịch vụ số cho workflow quan trọng

> **Mạch đọc:** [03. Messaging, smart home and service comparison](03_messaging_smart_home_and_service_comparison.md) đã nêu lifecycle và lock-in. Lab này biến chúng thành hồ sơ đánh giá một dịch vụ cụ thể.

## Câu hỏi và tài sản

Ghi workflow, dữ liệu, account owner, downtime chấp nhận được, người dùng khác, chi phí và cách rời dịch vụ. Phân loại dữ liệu theo nhạy cảm, khả năng thay thế và hậu quả mất.

Danh sách này xác định asset và failure mode trước khi đọc điều khoản; nếu chưa biết cái gì cần bảo vệ, không thể đánh giá permission hay exit plan một cách có nghĩa.

## Kiểm tra lifecycle

Hãy đi qua lifecycle theo thứ tự dưới đây và ghi lại điểm kiểm soát ở từng bước:

```text
sign-up → permissions → daily use → export/backup → recovery → cancellation
```

Ở mỗi bước ghi owner, failure mode, bằng chứng và hành động phục hồi. Thử export/restore bằng dữ liệu mẫu, không thử trên dữ liệu duy nhất.

Kết quả của lifecycle check là một đường phục hồi có thể diễn tập, không phải lời hứa rằng dịch vụ sẽ luôn sẵn sàng. Version, policy và ngày kiểm tra phải đi cùng kết luận để lần rà soát sau biết điều gì cần chạy lại.

> **Bàn giao:** Case chỉ kết luận trong version/ngày đã kiểm tra; khi policy hoặc giá đổi, chạy lại những bước nhạy nhất.
