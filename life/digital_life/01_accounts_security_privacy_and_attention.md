# Tài khoản, bảo mật, riêng tư và chú ý

> **Mạch đọc:** [00. Devices, accounts and data](00_devices_accounts_data_and_control.md) đã mô tả dòng dữ liệu. Chapter này tách năm tài sản thường bị trộn: quyền truy cập, bí mật dữ liệu, toàn vẹn, quyền riêng tư và sự chú ý của người dùng.

## 1. Năm tài sản, năm failure mode

Năm lớp dưới đây không phải danh sách thuật ngữ rời; mỗi lớp có failure mode và biện pháp kiểm soát khác nhau, nên hãy đọc chúng như một bảng phân rã rủi ro.

- **Quyền truy cập:** ai có thể đăng nhập hoặc hành động thay mình.
- **Bí mật:** ai không được đọc dữ liệu.
- **Toàn vẹn:** dữ liệu hoặc giao dịch có bị sửa trái phép không.
- **Quyền riêng tư:** dữ liệu nào được thu thập, dùng và chia sẻ trong phạm vi nào.
- **Sự chú ý:** thời gian và quyết định có bị hệ thống kéo lệch không.

Một ứng dụng có thể bảo mật tài khoản nhưng vẫn dùng thông báo để tối đa hóa thời gian sử dụng; một dịch vụ có thể riêng tư hơn nhưng khôi phục kém. Phân loại đúng giúp chọn biện pháp đúng.

> **Chuyển mạch:** Khi tài sản đã tách, thiết kế phòng vệ phải đi theo failure mode: xác thực và recovery cho quyền, mã hóa và phân quyền cho bí mật, audit cho toàn vẹn, giảm thu thập và giới hạn lưu trữ cho riêng tư, còn setting và thói quen cho sự chú ý.

## 2. Account recovery là một phần của bảo mật

Mật khẩu mạnh không đủ nếu email khôi phục, số điện thoại hoặc thiết bị tin cậy bị chiếm. Hãy lập bản đồ đường khôi phục và hỏi: nếu mất thiết bị chính, còn kênh nào; nếu mất email, ai có thể đổi mật khẩu; nếu tài khoản bị khóa, dữ liệu có bản sao ngoài dịch vụ không?

Xác thực nhiều yếu tố giảm một số rủi ro nhưng không loại bỏ phishing, lộ session hoặc cấp quyền cho ứng dụng độc hại. Biện pháp phải đặt tại điểm failure tương ứng.

> **Chuyển mạch:** Quyền truy cập cần recovery; riêng tư cần data minimization, giới hạn retention và kiểm tra bên thứ ba nhận dữ liệu.

## 3. Quản lý chú ý cũng là quản lý hệ thống

Thông báo, feed, autoplay và badge tạo vòng phản hồi giữa hành vi và thiết kế. Không cần gán động cơ cho người dùng để phân tích; chỉ cần đo trigger, thời điểm, phần thưởng và chi phí chú ý.

Giảm nhiễu bằng cách tắt thông báo không cần, gom thời điểm kiểm tra, tách tài khoản công việc/cá nhân và giữ đường thoát khỏi feed. Đây là can thiệp reversible, có thể thử và đánh giá bằng thời gian tập trung hoặc số lần gián đoạn.

> **Bàn giao:** Dùng năm tài sản làm checklist khi đọc một dịch vụ mới; nếu issue liên quan luồng dữ liệu, quay về chapter nền tảng, còn nếu liên quan quyết định tiêu dùng thì nối sang [Consumer Knowledge](../consumer_knowledge/README.md).
