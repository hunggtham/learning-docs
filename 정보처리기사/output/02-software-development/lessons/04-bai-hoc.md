# 29. 큐 (Queue)

## 학습 목표 (Mục tiêu)
- Định nghĩa chính xác cấu trúc dữ liệu Hàng đợi (큐 - Queue) và cơ chế vận hành theo nguyên lý Vào trước ra trước (FIFO - First-In, First-Out / 선입선출).
- Nắm vững vai trò và sự biến đổi của hai con trỏ `Front` (trỏ đầu để lấy/xóa dữ liệu) và `Rear` (trỏ cuối để đưa/chèn dữ liệu).
- Hiểu rõ nhược điểm tràn ảo của Queue tuyến tính và nguyên lý giải quyết bằng Hàng đợi vòng (원형 큐 - Circular Queue), cùng các ứng dụng thực tế trong hệ điều hành (Spooling, Scheduling, Buffer).

## 핵심 키워드 (Từ khóa)
- 큐 (Queue)
- FIFO (First-In, First-Out / 선입선출)
- 프런트 포인터 (Front Pointer - 삭제)
- 리어 포인터 (Rear Pointer - 삽입)
- 선형 큐 (Linear Queue)
- 원형 큐 (Circular Queue)
- 스풀링 (Spooling)
- 작업 스케줄링 (Job Scheduling / FCFS / Round Robin)
- 너비 우선 탐색 (BFS)

## 선행·연결 개념 (Kiến thức liên kết)
- [02-bai-hoc.md](02-bai-hoc.md): 스택 (Stack - LIFO) đối trọng với Queue (FIFO).
- [03-bai-hoc.md](03-bai-hoc.md): Tổng quan Stack, Queue và các biến thể Deque (Scroll/Shelf).
- [05-bai-hoc.md](05-bai-hoc.md): Cấu trúc cây (Tree) và duyệt cây theo tầng sử dụng Queue.

## 읽는 방법 (Cách đọc)
- Nhớ hình ảnh dòng người xếp hàng mua vé: Người đến trước được phục vụ trước (FIFO).
- Ghi nhớ rõ chiều con trỏ:
  - Thêm dữ liệu vào cuối hàng $\rightarrow$ **Rear** dịch chuyển tăng lên.
  - Lấy dữ liệu ra khỏi đầu hàng $\rightarrow$ **Front** dịch chuyển tăng lên.
  - Khi `Front == Rear` $\rightarrow$ Hàng đợi đang rỗng (Empty).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bản chất của Hàng đợi (Queue):**
  - Là cấu trúc dữ liệu tuyến tính có 2 đầu riêng biệt: một đầu chuyên dùng để chèn thêm phần tử (`Rear`), một đầu chuyên dùng để xóa/lấy phần tử ra (`Front`).
  - Cơ chế hoạt động: **FIFO (First-In, First-Out / 선입선출)** - Phần tử nào vào trước sẽ được xử lý và rời khỏi hàng đợi trước.
- **Quy tắc điều khiển con trỏ trong Queue:**
  - `Front`: Con trỏ trỏ vào vị trí trước phần tử đầu tiên (hoặc phần tử đầu tiên được lấy ra).
    - Thao tác xóa / lấy dữ liệu (`Delete / Dequeue`): $\text{Front} = \text{Front} + 1$.
  - `Rear`: Con trỏ trỏ vào phần tử cuối cùng hiện tại của hàng.
    - Thao tác thêm / chèn dữ liệu (`Insert / Enqueue`): $\text{Rear} = \text{Rear} + 1$.
  - Trạng thái rỗng (Empty): Khi $\text{Front} = \text{Rear}$.

- **Hàng đợi tuyến tính vs Hàng đợi vòng (Linear Queue vs Circular Queue):**

| Loại Hàng đợi | Đặc điểm vận hành | Hạn chế và Giải pháp |
| :--- | :--- | :--- |
| **선형 큐 (Linear Queue)** | Mảng 1 chiều cố định, con trỏ Front và Rear luôn tịnh tiến dần về phía cuối mảng | **Hiện tượng tràn ảo (Tràn giả):** Khi `Rear` chạm đáy mảng thì báo đầy (Overflow), dù các ô nhớ phía trước đã bị xóa (`Front` đã dịch lên). Rất lãng phí bộ nhớ |
| **원형 큐 (Circular Queue)** | Nối đầu cuối của mảng lại thành một vòng tròn khép kín bằng phép toán chia lấy dư Modulo | **Giải quyết triệt để tràn ảo.** Công thức tịnh tiến: $\text{Rear} = (\text{Rear} + 1) \pmod n$, $\text{Front} = (\text{Front} + 1) \pmod n$ |

- **Các ứng dụng kinh điển của Queue trong thực tế:**
  1. **스풀링 (Spooling / Print Queue):** Hàng đợi chứa các tài liệu chờ máy in vật lý in lần lượt.
  2. **작업 스케줄링 (Job Scheduling):** Lập lịch cấp phát CPU cho các tiến trình sẵn sàng (Ready Queue trong thuật toán FCFS, Round Robin).
  3. **Bộ đệm dữ liệu (Buffer):** Lưu tạm các gói tin truyền qua mạng hoặc dữ liệu đa phương tiện (Video/Audio streaming).
  4. **너비 우선 탐색 (BFS - Breadth-First Search):** Thuật toán duyệt đồ thị theo từng tầng chiều rộng.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Điều kiện nhận biết Rỗng và Đầy trong Circular Queue:**
  - Với mảng có kích thước $n$:
    - **Rỗng (Empty):** Khi $\text{Front} == \text{Rear}$.
    - **Đầy (Full):** Để phân biệt trạng thái đầy với rỗng, người ta luôn bớt lại 1 ô trống. Do đó điều kiện đầy là:
      $$(\text{Rear} + 1) \pmod n == \text{Front}$$

### 복습 체크리스트
- [ ] Định nghĩa chính xác nguyên lý FIFO (선입선출) của Queue.
- [ ] Chỉ rõ vai trò con trỏ: Front lấy ra, Rear thêm vào; trạng thái rỗng khi Front == Rear.
- [ ] Giải thích nguyên nhân hiện tượng tràn ảo ở Linear Queue và cách khắc phục bằng Circular Queue.
- [ ] Nhớ các ứng dụng tiêu biểu: Hàng đợi in Spooling, Lập lịch CPU, Thuật toán BFS.
