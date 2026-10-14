# 075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)

## 075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)

### 스택 (Stack)
Phần “스택 (Stack)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **LIFO (Last-In-First-Out / 후입선출):** Vào sau ra trước.
- **Con trỏ:** `Top` (Điểm vào/ra), `Bottom` (Đáy).
- **Lỗi:** Overflow (Đầy mà cố nhét), Underflow (Rỗng mà cố lấy).
- **Ứng dụng:** 재귀 호출 (Đệ quy), 후위 표기법 (Postfix).

### 큐 (Queue)
Phần “큐 (Queue)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **FIFO (First-In-First-Out / 선입선출):** Vào trước ra trước.
- **Con trỏ:** `Rear` (Chỗ đưa vào), `Front` (Chỗ lấy ra).
- **Ứng dụng:** 작업 스케줄링 (Lập lịch OS - Xếp hàng chờ xử lý).

### 데크 (Deque - Double Ended Queue)
Phần “데크 (Deque - Double Ended Queue)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 양쪽 끝에서 모두 입출력 가능. (Vào/Ra ở cả 2 đầu).
- **Scroll (스크롤):** 입력 제한 (Hạn chế Đầu vào - Vào 1 bên, Ra 2 bên).
- **Shelf (셸프):** 출력 제한 (Hạn chế Đầu ra - Vào 2 bên, Ra 1 bên).

- 💡 **Mẹo ghi nhớ (Mnemonics):**
  - Stack = LIFO = Đệ quy.
  - Queue = FIFO = Lập lịch.
  - Scroll (Cuộn) = Chỉ cuộn vào 1 hướng (Hạn chế Input).
  - Shelf (Cái giá đỡ) = Đẩy đồ vào từ 2 bên nhưng chỉ lấy ra được 1 mặt (Hạn chế Output).

---
