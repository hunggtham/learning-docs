# Case labs xuyên domain: một khung, nhiều cơ chế

> **Mạch đọc:** [02. Evidence, experiment and uncertainty](02_evidence_experiment_and_uncertainty.md) đã đặt tiêu chuẩn bằng chứng. Chapter này áp dụng khung vào ba case để chỉ ra phần tương đồng thật và ranh giới của phép so sánh.

## 1. Xe và nhà: năng lượng, nhiệt và feedback

Xe và nhà đều có nguồn năng lượng, tải, tổn hao và feedback điều khiển, nhưng actuator, thời gian đáp ứng và failure mode khác. Không dùng thermostat để giải thích trực tiếp drivetrain; chỉ mượn invariant về luồng năng lượng và điều khiển.

Phép so sánh này chỉ có giá trị ở invariant đã nêu: năng lượng đi qua hệ, được đo và điều khiển với độ trễ. Khi object và failure mode đổi, cần kiểm tra xem invariant còn dự đoán được gì trước khi mở rộng sang lifecycle.

## 2. Dịch vụ số và sản phẩm vật lý: lifecycle và exit

App và xe đều có mua, vận hành, bảo trì, update và kết thúc vòng đời. App có thể đổi policy từ xa; xe có ràng buộc vật lý và service network khác. TCO và exit là cầu nối, nhưng evidence phải theo owner domain.

Lifecycle vì thế là cầu nối để đặt câu hỏi chung, không phải lý do gộp hai owner. Case tiếp theo dùng cùng nguyên tắc giới hạn để đối chiếu triage trong sơ cứu với troubleshooting.

## 3. Sơ cứu và troubleshooting: ưu tiên rủi ro

Trong sơ cứu, ưu tiên nguy cơ tức thời và gọi trợ giúp; trong troubleshooting, ưu tiên cô lập failure và bảo toàn dữ liệu/tài sản. Cả hai dùng triage, nhưng hậu quả và năng lực người thực hiện không thể đánh đồng.

> **Bàn giao:** Case lab chỉ được giữ khi nêu rõ invariant, phần khác nhau và evidence; nếu phép so sánh không giúp dự đoán hoặc quyết định, trả nó về owner chuyên môn.
