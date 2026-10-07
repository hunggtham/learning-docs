# Nhắn tin, smart home và so sánh dịch vụ số

> **Mạch đọc:** [02. Backup, privacy and platform exit](02_backup_privacy_and_platform_exit.md) đã đặt khả năng khôi phục và rời nền tảng làm tiêu chí. Chapter này áp dụng vào ba hệ thống đời sống số thường gặp.

## 1. Nhắn tin: nội dung, metadata và recovery

Đọc một app nhắn tin theo nội dung được bảo vệ, metadata, thiết bị đăng nhập, backup, tìm kiếm, export và khả năng xác minh người nhận. “Mã hóa” không tự trả lời mọi câu hỏi về metadata, endpoint hoặc bản backup.

Vì vậy, đánh giá nhắn tin phải nối claim bảo mật với nơi dữ liệu còn tồn tại và cách khôi phục tài khoản. Cùng mental model đó có thể áp dụng cho smart home, nơi các lớp thiết bị–cloud–tài khoản tạo coupling khác.

## 2. Smart home: tiện lợi đổi lấy coupling

Thiết bị nhà thông minh nối sensor, cloud, app, tài khoản và nguồn điện. Khi một lớp hỏng, automation có thể dừng hoặc hành xử sai. Chọn thiết bị cần xem local fallback, manual override, update policy, quyền chia sẻ và cách reset khi đổi chủ.

Các thuộc tính này không phải checklist độc lập: local fallback giảm phụ thuộc cloud, manual override giới hạn hậu quả khi automation lỗi, còn reset và update quyết định vòng đời sau khi đổi chủ. Vì vậy [04. Service case lab](04_service_case_lab.md) sẽ so sánh cả lifecycle, không chỉ số tính năng lúc mua.

## 3. So sánh dịch vụ theo lifecycle

Bảng so sánh nên gồm chức năng hiện tại, dữ liệu thu thập, giá tăng theo thời gian, lock-in, export, recovery và shutdown risk. Một app rẻ hơn nhưng không xuất dữ liệu có thể có TCO cao hơn khi workflow đã phụ thuộc.

> **Bàn giao:** Dùng chapter này cùng [Consumer Knowledge](../consumer_knowledge/README.md) để đánh giá sản phẩm số như một hệ thống có lifecycle, không chỉ như giao diện nhiều tính năng.
