# 핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)

## 핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)

### RAM/ROM의 용량 계산 (Tính dung lượng RAM/ROM)
Phần “RAM/ROM의 용량 계산 (Tính dung lượng RAM/ROM)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 주소선 (Address Bus) số lượng quyết định số Word: Nếu có n đường thì có 2^n Word. (Liên quan đến MAR và PC).
- 데이터 버스 (Data Bus) số lượng quyết định kích thước mỗi Word. (Liên quan đến MBR và IR).
- `Dung lượng = Số Word × Kích thước Word`. Ví dụ: 7 Address lines, 8 Data lines => 2^7 × 8 Bit = 128 × 8 Bit.

### 자기 코어 (Magnetic Core - Lõi từ)
Phần “자기 코어 (Magnetic Core - Lõi từ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 부피에 비해 용량이 작고 가격이 비싸 현재는 거의 사용하지 않는다. (Dung lượng nhỏ, giá đắt, ít dùng hiện nay.)
- 데이터를 읽으면 읽은 내용이 지워지는 파괴 메모리(DRO Memory)이므로, 재저장(Restoration Time) 시간이 필요하다. (Đọc xong là mất dữ liệu (Phá hủy), nên cần thời gian ghi lại.)
- Cấu tạo: 구동선(X, Y) 2개 (2 dây chọn địa chỉ), 센스 선 1개 (1 dây cảm biến trạng thái), 금지선 1개 (1 dây cấm).

- **Vietnamese Explanation:** Kích thước bộ nhớ phụ thuộc vào Address Bus (chiều dài) và Data Bus (chiều rộng). Lõi từ là công nghệ cổ, đọc xong bị mất dữ liệu nên phải tốn thời gian khôi phục, hiện không còn dùng.
- 💡 **Mẹo ghi nhớ (Mnemonics):** 자기 코어 (Magnetic Core) = Đọc là Mất (DRO), Cần ghi lại. 4 dây = 2 X/Y + 1 Sense + 1 Inhibit.

---
