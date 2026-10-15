# 094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)

## 학습 목표 (Mục tiêu)
- Nắm vững kiến trúc giao tiếp liên tiến trình (IPC - Inter-Process Communication) và các cơ chế truyền tin đồng bộ/bất đồng bộ trong hệ điều hành.
- Phân biệt 5 loại mô-đun thuật toán cơ bản khi lập trình hệ thống: Mô-đun trình điều khiển thiết bị (Device Driver), Mô-đun mạng (Network), Mô-đun tệp tin (File), Mô-đun bộ nhớ (Memory) và Mô-đun tiến trình (Process).
- Hiểu rõ vai trò điều phối tài nguyên và bảo vệ hệ thống của từng loại mô-đun trong kiến trúc phần mềm phân tầng.

## 핵심 키워드 (Từ khóa)
- IPC (Inter-Process Communication)
- 공유 메모리 (Shared Memory) & 세마포어 (Semaphores)
- 디바이스 드라이버 모듈 (Device Driver Module)
- 네트워크 모듈 (Network Module)
- 파일 모듈 (File Module)
- 메모리 모듈 (Memory Module)
- 프로세스 모듈 (Process Module)

## 선행·연결 개념 (Kiến thức liên kết)
- [31-bai-hoc.md](31-bai-hoc.md): Khái niệm 단위 모듈 (Unit Module) và 5 phương thức IPC tổng quan.
- [33-bai-hoc.md](33-bai-hoc.md): Nguyên tắc biên soạn đặc tả chức năng và triển khai I/O mô-đun.
- [35-bai-hoc.md](35-bai-hoc.md): Kiểm thử đơn vị mô-đun và xây dựng Test Case.

## 읽는 방법 (Cách đọc)
- Phân biệt 5 loại mô-đun lập trình dựa trên đối tượng quản lý trực tiếp của nó:
  - Điều khiển phần cứng ngoại vi (Máy in, Card đồ họa) $\rightarrow$ **디바이스 드라이버 (Device Driver)**.
  - Quản lý truyền nhận gói tin, giao thức TCP/IP $\rightarrow$ **네트워크 모듈 (Network)**.
  - Quản lý đọc/ghi và cấu trúc thư mục trên ổ đĩa $\rightarrow$ **파일 모듈 (File)**.
  - Quản lý cấp phát và giải phóng RAM, bộ nhớ ảo $\rightarrow$ **메모리 모듈 (Memory)**.
  - Quản lý vòng đời, tạo mới và lập lịch tiến trình $\rightarrow$ **프로세스 모듈 (Process)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **So sánh 5 phương thức IPC cốt lõi:**
  - **Shared Memory (공유 메모리):** Nhanh nhất vì dữ liệu nằm trực tiếp trong RAM dùng chung giữa các process, không qua trung gian sao chép Kernel.
  - **Socket (소켓):** Giao tiếp linh hoạt nhất, hỗ trợ cả giao tiếp nội bộ trong máy lẫn giao tiếp phân tán qua mạng Internet.
  - **Semaphores (세마포어):** Cơ chế điều khiển đồng bộ và khóa tài nguyên, không mang dữ liệu nghiệp vụ.
  - **Pipes (파이프):** Giao tiếp luồng tuần tự một chiều theo cơ chế FIFO giữa 2 tiến trình.
  - **Message Queue (메시지 큐):** Hàng đợi chứa các gói tin nhắn có cấu trúc, cho phép truyền nhận bất đồng bộ.

- **Bảng phân loại 5 mô-đun triển khai thuật toán hệ thống:**

| Loại mô-đun | Tên tiếng Hàn & Anh | Chức năng nhiệm vụ trọng tâm |
| :--- | :--- | :--- |
| **Trình điều khiển thiết bị** | **디바이스 드라이버 모듈 (Device Driver)** | Giao tiếp và điều khiển trực tiếp các thiết bị phần cứng ngoại vi (bàn phím, chuột, máy in, card mạng, màn hình hiển thị) thông qua các thanh ghi phần cứng |
| **Mô-đun mạng** | **네트워크 모듈 (Network Module)** | Đóng gói, định tuyến, truyền nhận và kiểm tra lỗi của các gói tin dữ liệu trên môi trường mạng máy tính (TCP/IP, UDP, HTTP) |
| **Mô-đun tệp tin** | **파일 모듈 (File Module)** | Quản lý các thao tác mở (Open), đọc (Read), ghi (Write), đóng (Close), tìm kiếm (Seek) và khóa tệp tin (File Locking) trên hệ thống lưu trữ |
| **Mô-đun bộ nhớ** | **메모리 모듈 (Memory Module)** | Cấp phát (Allocation) và thu hồi (Deallocation) vùng nhớ RAM, quản lý phân trang (Paging), phân đoạn (Segmentation) trong bộ nhớ ảo |
| **Mô-đun tiến trình** | **프로세스 모듈 (Process Module)** | Tạo mới (Fork/Create), lập lịch thực thi (Scheduling), thay đổi trạng thái và hủy tiến trình (Termination), ngăn chặn Deadlock |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế hoạt động của Device Driver trong Kernel:**
  - Device Driver là phần mềm trung gian giúp hệ điều hành không cần biết cấu tạo vật lý chi tiết của từng loại máy in hay card đồ họa của các hãng khác nhau.
  - Hệ điều hành chỉ cần đưa ra các lệnh chuẩn hóa (như `read()`, `write()`), Device Driver sẽ dịch lệnh đó thành chuỗi tín hiệu điện hoặc lệnh phần cứng cụ thể để thiết bị thực thi.

### 복습 체크리스트
- [ ] So sánh được đặc điểm 5 phương thức IPC: Shared Memory, Socket, Semaphore, Pipe, Message Queue.
- [ ] Phân biệt rõ nhiệm vụ của Device Driver (phần cứng) và File Module (tệp tin đĩa cứng).
- [ ] Nhớ chức năng của Memory Module (cấp phát/thu hồi RAM) và Process Module (tạo/lập lịch tiến trình).
- [ ] Xác định Shared Memory là phương thức IPC có tốc độ cao nhất.
