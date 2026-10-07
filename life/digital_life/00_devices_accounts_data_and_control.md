# Thiết bị, tài khoản và dữ liệu: bản đồ đời sống số

> **Mạch đọc:** [Digital Life README](README.md) đặt chapter này làm nền cho việc dùng thiết bị và dịch vụ số. Ta đi từ thiết bị/giao diện → tài khoản và quyền → dữ liệu, mạng và bên thứ ba → riêng tư, bảo mật, sao lưu và khả năng rời dịch vụ.

## 1. Một hành động số đi qua nhiều lớp

Khi bấm một nút, giao diện gửi yêu cầu; hệ thống xác định tài khoản, kiểm tra quyền, đọc hoặc ghi dữ liệu, gọi dịch vụ mạng rồi trả kết quả. Nếu chỉ nhìn màn hình, người dùng dễ không biết lỗi nằm ở thiết bị, kết nối, danh tính hay máy chủ.

```text
thiết bị/giao diện
→ identity/account
→ authorization
→ data + network
→ service/algorithm
→ result + log
```

> **Chuyển mạch:** Sơ đồ luồng giải thích một hành động cần đi qua đâu; để quản lý rủi ro, cần phân biệt dữ liệu nào được thu thập và quyền nào cho phép ai dùng nó.

## 2. Định danh, xác thực và phân quyền không phải một việc

Định danh trả lời “đây là tài khoản nào”; xác thực kiểm tra “người đang dùng có kiểm soát bằng chứng đăng nhập không”; phân quyền quyết định “tài khoản được làm gì”. Mật khẩu mạnh không bù được việc cấp quyền quá rộng, và xác thực tốt không làm dữ liệu thu thập trở nên vô hại.

Khi đánh giá một dịch vụ, ghi rõ tài khoản owner, phương thức khôi phục, thiết bị tin cậy, quyền của ứng dụng và đường thu hồi quyền. Đây là invariant quan trọng hơn việc nhớ tên một setting.

> **Chuyển mạch:** Sau khi biết ai có quyền, phải theo dữ liệu qua nơi lưu, nơi chia sẻ và nơi sao lưu; đó là ranh giới giữa tiện ích, riêng tư và khả năng phục hồi.

## 3. Dữ liệu có vòng đời

Hãy đọc dữ liệu như một dòng đời thay vì một vật thể nằm yên: mỗi mũi tên dưới đây là một nơi có thể phát sinh quyền truy cập, rò rỉ hoặc mất khả năng khôi phục.

```text
create → collect → process → share → retain → delete/export
```

Mỗi bước có rủi ro khác nhau. Dữ liệu vị trí, danh bạ, ảnh, lịch sử tìm kiếm và thông tin thanh toán không có cùng mức nhạy cảm; ứng dụng cần quyền đọc chưa chắc cần quyền ghi hoặc theo dõi liên tục.

Đọc chính sách quyền riêng tư theo câu hỏi cụ thể: dữ liệu nào, mục đích nào, lưu bao lâu, chia sẻ cho ai, và người dùng có thể xem/xóa/xuất dữ liệu không. Nếu câu trả lời không rõ, đó là bất định cần ghi lại chứ không nên tự suy đoán.

> **Chuyển mạch:** Dữ liệu có vòng đời và chủ thể xử lý; sao lưu và khôi phục kiểm tra điều gì xảy ra khi thiết bị mất, tài khoản bị khóa hoặc dịch vụ ngừng hoạt động.

## 4. Bảo mật thực dụng và khả năng rời dịch vụ

Ưu tiên các tài sản quan trọng: tài khoản email chính, định danh, tiền, ảnh và dữ liệu công việc. Dùng xác thực nhiều yếu tố khi có thể, cập nhật thiết bị, giới hạn quyền, tách tài khoản quan trọng và thử khôi phục trước khi sự cố xảy ra.

Đây là các biện pháp nền, không phải bảo đảm tuyệt đối. [CISA Secure Our World](https://www.cisa.gov/secure-our-world) dùng password manager, MFA, phishing awareness và software updates làm các bước phổ thông; setting recovery, quyền dữ liệu và mức bảo vệ cụ thể vẫn phải kiểm tra ở chính dịch vụ.

Một bản sao lưu chỉ có giá trị nếu khôi phục được. Hãy kiểm tra bản sao có tồn tại, có mã hóa phù hợp, có ở ngoài thiết bị gốc và có thể đọc bằng một tài khoản khác hay không. Khả năng xuất dữ liệu và đổi dịch vụ là một phần của chất lượng hệ thống, không phải việc phụ.

> **Bàn giao:** Giữ mental model `giao diện → identity → quyền → dữ liệu → dịch vụ → khôi phục`; [03. Messaging, smart home and service comparison](03_messaging_smart_home_and_service_comparison.md) áp dụng nó vào nhắn tin và nhà thông minh, còn [04. Service case lab](04_service_case_lab.md) kiểm tra một workflow cụ thể.
