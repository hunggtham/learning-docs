# Bằng chứng, thử nghiệm và bất định

> **Mạch đọc:** [01. Energy, materials and feedback](01_energy_materials_feedback_and_tradeoffs.md) cho thấy các cơ chế xuyên domain. Chapter này đặt ranh giới cho việc kết luận: khi nào quan sát đủ, khi nào cần thử nghiệm, và khi nào vẫn phải giữ bất định.

## 1. Observation chưa phải causal proof

Quan sát ghi lại điều cùng xảy ra; nó chưa chỉ ra biến nào gây biến nào. Để tăng sức mạnh giải thích, ghi điều kiện, biến thay đổi, đối chứng khả dĩ và cơ chế dự kiến.

Một mô hình tốt dự đoán được ít nhất một điều mới và có thể bị phản bác. Nếu mọi kết quả đều được giải thích sau khi xảy ra, đó là story linh hoạt chứ chưa phải test.

> **Chuyển mạch:** Câu hỏi nhân quả cần prediction; thiết kế thử nghiệm phải cân bằng thông tin thu được với rủi ro, chi phí và khả năng đo.

## 2. Thử nghiệm nhỏ và an toàn

Thay đổi một biến khi có thể, giữ các biến khác ổn định, ghi baseline và thời gian. Với Home, Digital Life hoặc Cars, không thử nếu có nguy cơ điện, cháy, chấn thương, mất dữ liệu hoặc vi phạm điều khoản; dùng mô phỏng, tài liệu owner hoặc chuyên gia thay thế.

Ghi cả kết quả âm tính và lý do test không kết luận được. Không mở rộng một kết quả từ một thiết bị, người dùng hoặc thời điểm thành quy luật phổ quát.

> **Chuyển mạch:** Test tạo dữ liệu trong một vùng điều kiện; bất định còn lại phải được đưa vào quyết định thay vì bị che bằng một con số chắc chắn.

## 3. Quyết định dưới bất định

Tách `điều đã biết`, `ước lượng`, `giả định`, `failure mode` và `trigger xem lại`. Chọn hành động reversible khi giá trị thông tin cao hoặc hậu quả sai lớn; chọn barrier an toàn khi không thể thử.

> **Bàn giao:** Dùng chapter này để review claim trong mọi nhánh Life; khi claim thuộc domain chuyên môn, quay về [SOURCES](../SOURCES.md) và owner chapter trước khi công bố như docs chính thức.
