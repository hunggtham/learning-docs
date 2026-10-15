# 34. 단위 모듈과 IPC (Unit Module & Inter-Process Communication)

## 학습 목표 (Mục tiêu)
- Định nghĩa chính xác Mô-đun đơn vị (단위 모듈 - Unit Module) với tư cách là khối phần mềm độc lập tối thiểu có khả năng biên dịch riêng biệt.
- Hiểu rõ khái niệm và sự cần thiết của Giao tiếp liên tiến trình (IPC - Inter-Process Communication) khi các tiến trình chạy trong không gian địa chỉ bộ nhớ cô lập của hệ điều hành.
- Nằm lòng 5 phương thức IPC kinh điển: Bộ nhớ chia sẻ (Shared Memory), Ổ cắm mạng (Socket), Cờ hiệu đồng bộ (Semaphores), Đường ống (Pipes) và Hàng đợi thông điệp (Message Queue).

## 핵심 키워드 (Từ khóa)
- 단위 모듈 (Unit Module)
- 독립 컴파일 (Independent Compilation)
- IPC (Inter-Process Communication)
- 공유 메모리 (Shared Memory / Tốc độ nhanh nhất)
- 소켓 (Socket / Mạng TCP/IP)
- 세마포어 (Semaphores / Đồng bộ hóa tài nguyên)
- 파이프 (Pipes & Named Pipes / FIFO)
- 메시지 큐 (Message Queue / Bất đồng bộ)

## 선행·연결 개념 (Kiến thức liên kết)
- [30-bai-hoc.md](30-bai-hoc.md): Hashing và mô hình lưu trữ dữ liệu.
- [32-bai-hoc.md](32-bai-hoc.md): Quy trình triển khai mô-đun (Module Implementation).
- [34-bai-hoc.md](34-bai-hoc.md): Chi tiết các phương thức IPC và kiến trúc thuật toán theo phân loại mô-đun.

## 읽는 방법 (Cách đọc)
- Học thuộc danh sách 5 phương thức IPC qua mẹo ghi nhớ chữ cái đầu: **S-S-S-P-M** (*Shared Memory, Socket, Semaphore, Pipe, Message Queue*).
- Nắm vững đặc trưng đề thi hay hỏi:
  - Phương thức IPC có tốc độ truy xuất nhanh nhất $\rightarrow$ **공유 메모리 (Shared Memory)**.
  - Phương thức IPC dùng để đồng bộ hóa và khóa tài nguyên chia sẻ $\rightarrow$ **세마포어 (Semaphores)**.
  - Phương thức giao tiếp giữa các tiến trình qua mạng máy tính $\rightarrow$ **소켓 (Socket)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Khái niệm Mô-đun đơn vị (단위 모듈 - Unit Module):**
  - Là đơn vị cấu trúc phần mềm độc lập nhỏ nhất, thực hiện duy nhất một chức năng nghiệp vụ đơn lẻ và có khả năng **biên dịch độc lập (독립적으로 컴파일 가능)**.
  - Các đơn vị mô-đun liên kết lại với nhau tạo thành các phân hệ và toàn bộ hệ thống phần mềm hoàn chỉnh.
- **Khái niệm IPC (Inter-Process Communication):**
  - Trong các hệ điều hành hiện đại, mỗi tiến trình (Process) đều được cấp phát một không gian địa chỉ ảo hoàn toàn tách biệt để bảo đảm tính an toàn.
  - IPC là tập hợp các cơ chế do hệ điều hành cung cấp để cho phép **các tiến trình khác nhau có thể trao đổi dữ liệu và đồng bộ hóa hoạt động** với nhau.

- **Bảng tổng hợp 5 phương pháp IPC trọng điểm trong đề thi:**

| Phương thức IPC | Tên tiếng Hàn & Anh | Cơ chế hoạt động chi tiết | Đặc điểm nổi bật |
| :--- | :--- | :--- | :--- |
| **Bộ nhớ chia sẻ** | **Shared Memory (공유 메모리)** | Hệ điều hành ánh xạ một vùng nhớ vật lý chung vào không gian địa chỉ của nhiều tiến trình để cùng đọc/ghi trực tiếp | **Tốc độ nhanh nhất** vì không qua sao chép Kernel; cần cơ chế khóa đồng bộ |
| **Ổ cắm mạng** | **Socket (소켓)** | Tạo điểm cuối kết nối mạng logic (IP Address + Port Number) theo giao thức TCP/UDP | Cho phép tiến trình giao tiếp **qua môi trường mạng** giữa các máy tính khác nhau |
| **Cờ hiệu** | **Semaphores (세마포어)** | Biến đếm nguyên thủy do Dijkstra đề xuất, dùng thao tác nguyên tử $P$ (Wait) và $V$ (Signal) để kiểm soát quyền truy cập | Chuyên dùng để **đồng bộ hóa và kiểm soát tương tranh**, ngăn ngừa xung đột tài nguyên |
| **Đường ống** | **Pipes (파이프 / FIFO)** | Kênh đệm một chiều (Unidirectional) hoạt động theo nguyên lý FIFO: Một tiến trình ghi vào đầu ống, tiến trình kia đọc ra ở đầu kia | Chia thành: Pipe vô danh (cha-con) và Named Pipe (giữa các tiến trình bất kỳ) |
| **Hàng đợi thông điệp** | **Message Queue (메시지 큐)** | Các thông điệp dữ liệu được đóng gói thành gói tin và đưa vào hàng đợi do hệ điều hành quản lý | Hỗ trợ truyền thông **bất đồng bộ (Asynchronous)** giữa các tiến trình |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Vấn đề tranh chấp trong Shared Memory và vai trò của Semaphore:**
  - Vì nhiều tiến trình có thể cùng ghi đồng thời vào vùng **Shared Memory**, nếu không có kiểm soát sẽ gây ra hiện tượng xung đột dữ liệu (Race Condition).
  - Do đó trong lập trình hệ thống thực tế, các kỹ sư thường kết hợp **Shared Memory (để truyền tải dữ liệu dung lượng lớn cực nhanh)** với **Semaphore hoặc Mutex (để làm ổ khóa điều phối ai được vào đọc/ghi)**.

### 복습 체크리스트
- [ ] Định nghĩa đơn vị mô-đun: Khối độc lập nhỏ nhất có thể biên dịch riêng biệt.
- [ ] Giải thích tại sao cần IPC: Do các tiến trình bị cô lập không gian bộ nhớ.
- [ ] Kể tên đầy đủ 5 phương thức IPC: Shared Memory, Socket, Semaphore, Pipe, Message Queue.
- [ ] Nhớ Shared Memory có tốc độ nhanh nhất và Semaphore chuyên dùng để đồng bộ khóa.
