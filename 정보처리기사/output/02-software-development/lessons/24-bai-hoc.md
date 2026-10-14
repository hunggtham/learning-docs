# 086-1: 기수 정렬 (Radix Sort / Bucket Sort)

## 086-1: 기수 정렬 (Radix Sort / Bucket Sort)
Phần “086-1: 기수 정렬 (Radix Sort / Bucket Sort)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 데이터를 비교하지 않음! **큐(Queue)**를 이용하여 데이터의 **자릿수(Digit)**별로 나누어 담았다가 꺼냄. (Không dùng dấu < hay > để so sánh. Nhìn vào chữ số hàng Đơn vị, phân vào 10 cái Queue (0-9). Xong ráp lại, làm tiếp hàng Chục, Trăm...).
- **시간 복잡도:** **O(d*n)** (Trong đó d là số chữ số dài nhất). Cực kỳ nhanh, vượt qua giới hạn n log n của các thuật toán so sánh thông thường.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Radix (Cơ số) = Chữ số (Hàng đơn vị, chục...) (Chữ số), Queue/Bucket. Siêu tốc O(dn).

---
