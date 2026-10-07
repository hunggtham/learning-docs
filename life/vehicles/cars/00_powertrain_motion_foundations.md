# Nguồn động lực và chuyển động: xe biến năng lượng thành lực như thế nào?

> **Mạch đọc:** [Cars README](README.md) đặt chapter này ngay sau bản đồ hệ thống. Ta đi từ năng lượng → power unit → mô-men và công suất → truyền động → lực tại lốp → gia tốc và giới hạn bám, để các thông số động cơ được nối với trải nghiệm xe thay vì đứng riêng lẻ.

## 1. Xe cần lực, không cần một con số quảng cáo

Để tăng tốc, xe cần lực tổng theo hướng chuyển động. Lực đó đến từ mô-men ở bánh xe, còn mô-men bánh xe phụ thuộc power unit, tỷ số truyền, hiệu suất truyền động và bán kính lốp. Khối lượng, độ dốc, cản không khí và cản lăn quyết định bao nhiêu lực bị tiêu hao.

Một mental model đơn giản:

```text
năng lượng
→ power unit tạo mô-men
→ transmission biến đổi tốc độ/mô-men
→ drivetrain phân phối tới bánh
→ lốp tạo lực với mặt đường
→ xe tăng tốc hoặc giữ tốc độ
```

> **Chuyển mạch:** Chuỗi truyền năng lượng cho biết lực đến bánh từ đâu; [01. ICE, EV, hybrid and thermal](01_ice_ev_hybrid_and_thermal.md) tách các nguồn năng lượng, còn [02. Transmission, tires, safety and ownership](02_transmission_tires_safety_and_ownership.md) kiểm tra vì sao cùng horsepower vẫn cho cảm giác khác.

## 2. Mô-men và công suất trả lời hai câu hỏi khác nhau

Mô-men mô tả xu hướng làm quay; công suất mô tả tốc độ thực hiện công. Trong hệ quay, công suất tăng khi mô-men được tạo ra ở tốc độ quay cao hơn, vì vậy cần nhìn cả đường cong theo vòng tua.

Hộp số cho phép power unit hoạt động trong vùng phù hợp bằng cách đổi quan hệ giữa tốc độ quay và mô-men tại bánh. So sánh horsepower cực đại mà bỏ qua tỷ số truyền, khối lượng và traction sẽ dự đoán sai cảm giác tăng tốc.

> **Chuyển mạch:** Công suất/mô-men của nguồn chưa phải lực thực tế; transmission và drivetrain quyết định lực đó được đưa tới cầu nào và với tổn hao bao nhiêu.

## 3. Lốp là điểm tiếp xúc giới hạn toàn hệ thống

Lốp truyền lực dọc khi tăng/giảm tốc và lực ngang khi đổi hướng. Độ bám phụ thuộc tải lên bánh, hợp chất cao su, nhiệt độ, mặt đường, nước, góc trượt và cách điều khiển. Tăng công suất nhưng không tăng khả năng truyền lực có thể chỉ tạo trượt bánh.

AWD/4WD thay đổi cách phân phối mô-men nhưng không xóa giới hạn ma sát. Chassis, suspension và hệ thống điều khiển giúp giữ lốp trong vùng làm việc, còn brake và steering biến lực thành quỹ đạo mong muốn.

> **Bàn giao:** Giữ chuỗi `năng lượng → mô-men → tỷ số truyền → lực tại lốp → quỹ đạo`; từ đây có thể học riêng ICE, motor điện, turbo, hộp số hoặc tire mà vẫn biết chúng nằm ở đâu trong hệ thống.
