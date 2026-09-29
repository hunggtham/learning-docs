# Vật lý — điểm vào kiểm toán phạm vi

**Ngày rà soát:** 2026-09-29  
**Root chuẩn gốc:** `physics/`

Bản kiểm toán chi tiết về phạm vi, độ sâu và chất lượng đã nằm tại:

- [`13_connections/02_coverage_audit.md`](./13_connections/02_coverage_audit.md)

Tệp root này chỉ đóng vai trò **điểm vào governance ổn định** để tooling cấp repository luôn tìm được `COVERAGE_AUDIT.md`; không lặp lại toàn bộ audit chi tiết ở đây.

## Hợp đồng cấp root

Physics được tổ chức theo phụ thuộc khái niệm và cần giữ chuỗi bền vững:

```text
hiện tượng
→ đại lượng đo được
→ mô hình
→ toán học/suy dẫn
→ giả định
→ miền áp dụng
→ trường hợp giới hạn/thất bại
→ bằng chứng/thực nghiệm
→ liên kết kiến thức
```

Domain này sở hữu định luật vật lý, mô hình, đo lường và các cầu nối nâng cao có chọn lọc. Khi câu hỏi chuyển từ “tự nhiên hoạt động thế nào?” sang “thiết kế topology, timing, power, control hay hardware–software interface ra sao?”, bàn giao sang domain kỹ thuật phù hợp, đặc biệt [Electrical Engineering](../electrical_engineering/README.md).

## Quy tắc review và bàn giao

Khi coverage hoặc depth thực sự thay đổi, cập nhật [`13_connections/02_coverage_audit.md`](./13_connections/02_coverage_audit.md). Chỉ sửa tệp root này khi owner hoặc vị trí audit chi tiết thay đổi.