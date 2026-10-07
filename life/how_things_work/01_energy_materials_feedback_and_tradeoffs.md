# Năng lượng, vật liệu, phản hồi và trade-off xuyên đời sống

> **Mạch đọc:** [00. System boundary](00_system_boundary_mechanism_and_failure.md) cung cấp khung phân tích. Chapter này cho thấy cùng một khung xuất hiện trong Cars, Home, Food & Drinks và Digital Life, nhưng không đồng nhất các domain.

## 1. Năng lượng luôn đi cùng đường truyền và tổn hao

Xe biến năng lượng hóa học hoặc điện thành mô-men; nhà chuyển điện/nhiệt thành comfort; bia và whisky dùng năng lượng để biến đổi nguyên liệu; thiết bị số dùng điện để xử lý và truyền dữ liệu. Trong mọi case, hãy hỏi nguồn, biến đổi, nơi lưu trữ và nơi năng lượng thất thoát.

Tổn hao không chỉ là “phần xấu”. Nhiệt thải, ma sát, điện trở, thời gian chờ hoặc công suất dự phòng là hệ quả của constraint; muốn giảm chúng phải trả bằng tiền, khối lượng, độ phức tạp hoặc độ bền.

> **Chuyển mạch:** Năng lượng chỉ là một lớp; vật liệu và cấu tạo quyết định hệ thống chịu tải, truyền nhiệt, giữ áp suất hoặc lưu dữ liệu như thế nào.

## 2. Vật liệu là một gói thuộc tính

Một vật liệu thường trade-off giữa độ cứng, khối lượng, độ bền mỏi, dẫn nhiệt, chống hóa chất, giá và khả năng sửa chữa. Không có “vật liệu tốt nhất” ngoài bối cảnh tải và failure mode.

Đọc vật liệu theo chức năng của bộ phận, môi trường, cách nối và cách xuống cấp. Cùng loại vật liệu nhưng hình học, bề mặt và mối nối khác có thể làm kết quả đảo ngược.

> **Chuyển mạch:** Vật liệu tạo điều kiện cho cơ chế; phản hồi quyết định hệ thống tự ổn định, khuếch đại lỗi hay cần điều khiển bên ngoài.

## 3. Phản hồi tạo ra hành vi hệ thống

Thermostat, kiểm soát traction, giới hạn tốc độ, notification và quy trình bảo trì đều là feedback loop. Vòng phản hồi tốt cần đo đúng trạng thái, có ngưỡng hợp lý và hành động không làm hệ thống dao động.

Khi hệ thống oscillate hoặc runaway, tìm độ trễ, tín hiệu sai, giới hạn actuator và vòng phản hồi bị bỏ qua. Đây là lý do một sửa chữa cục bộ đôi khi làm failure lớn hơn.

> **Bàn giao:** Dùng ba câu hỏi `năng lượng đi đâu? vật liệu chịu gì? feedback giữ trạng thái nào?` để nối các chapter Life; nếu cần claim chi tiết, quay về owner domain thay vì kéo một ẩn dụ quá xa.
