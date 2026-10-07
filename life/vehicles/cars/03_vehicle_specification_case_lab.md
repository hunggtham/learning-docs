# Case lab: đọc specification của một chiếc xe

> **Mạch đọc:** [02. Transmission, tires, safety and ownership](02_transmission_tires_safety_and_ownership.md) đã nối kiến trúc với safety/TCO. Lab này biến một spec sheet thành quyết định theo scenario.

## 1. Chuẩn hóa đầu vào

Ghi phiên bản, thị trường, model year, powertrain, curb weight, công suất/mô-men, battery/tank, transmission, tire, safety equipment và warranty. Không so hai con số nếu đơn vị, điều kiện đo hoặc cấu hình khác.

## 2. Chọn scenario

Ví dụ: đi phố ngắn, cao tốc dài, chở tải, đường dốc, khí hậu nóng/lạnh hoặc giữ xe mười năm. Mỗi scenario ưu tiên biến khác: range/useful fuel, nhiệt, traction, cabin, service network hoặc depreciation.

## 3. Viết kết luận có điều kiện

Kết luận nên giữ nguyên điều kiện áp dụng thay vì ép thành một thứ hạng chung:

```text
xe A phù hợp khi [scenario + điều kiện]
xe B phù hợp khi [scenario + điều kiện]
chưa kết luận vì [thiếu dữ liệu/khác cấu hình]
```

> **Bàn giao:** Lab này không tạo bảng xếp hạng vĩnh viễn; cập nhật lại khi model year, giá, hạ tầng, warranty hoặc scenario thay đổi.
