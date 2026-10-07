# Workbook so sánh sản phẩm theo category

> **Mạch đọc:** [02. Durability, warranty, repair and TCO](02_durability_warranty_repair_and_tco.md) đã theo dõi sản phẩm qua thời gian. Chapter này gom các nguyên tắc thành workbook để so sánh category mà không biến nó thành bảng xếp hạng cố định.

## 1. Xác định decision boundary

Ghi scenario, ngân sách, thời gian sở hữu, điều kiện môi trường, tiêu chí bắt buộc và failure không chấp nhận. Nếu hai sản phẩm không cùng decision boundary, bảng điểm sẽ tạo ảo giác chính xác.

Decision boundary là điều kiện để biết bảng đang trả lời câu hỏi nào; sau khi cố định nó, ta mới có thể hỏi mỗi tiêu chí được đo bằng bằng chứng nào và bất định nằm ở đâu.

## 2. Ma trận evidence

Ma trận dưới đây buộc mỗi tiêu chí phải gắn với cách đo, nguồn và điều kiện; không có dữ liệu tương thích thì để trống thay vì chấm điểm cảm tính.

```text
criterion → measurement → source → condition → uncertainty → consequence
```

Mỗi hàng phải chỉ ra bằng chứng và điều kiện. Review chỉ ra trải nghiệm; test định lượng; warranty và service network cho biết rủi ro sau mua. Không điền điểm khi dữ liệu không tương thích.

> **Chuyển mạch:** Ma trận giúp so sánh minh bạch; bước cuối là sensitivity: nếu một giả định đổi, quyết định có còn giữ không?

## 3. Quyết định và cập nhật

Viết kết luận theo dạng “chọn A khi…, chọn B khi…, chưa đủ dữ liệu ở…”. Ghi ngày, phiên bản, giá và nguồn. Khi product refresh, policy đổi hoặc nhu cầu đổi, chạy lại những hàng nhạy nhất thay vì sửa một con số trong bảng cũ.

> **Bàn giao:** Workbook là công cụ reasoning của Life, không phải recommendation engine; dùng nó với [COVERAGE](../COVERAGE.md) để thêm category mới mà vẫn giữ owner và bằng chứng.
