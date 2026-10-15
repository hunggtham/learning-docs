# 085. 프로세스 및 스레드 (Process & Thread)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm tiến trình (프로세스 - Process) như một chương trình đang thực thi trong bộ nhớ và luồng (스레드 - Thread) như một đơn vị thực thi nhẹ bên trong tiến trình.
- Ghi nhớ chu trình 5 trạng thái của tiến trình (준비 - Ready, 실행 - Running, 대기 - Wait/Block) và 4 sự kiện chuyển đổi trạng thái (상태 전이): Dispatch, Timeout, Block, và Wakeup theo thần chú **디·타·블·웨**.
- Hiểu cấu trúc khối điều khiển tiến trình (PCB - Process Control Block) và cơ chế chuyển đổi ngữ cảnh (문맥 교환 - Context Switching).
- Phân biệt sâu sắc giữa Luồng mức người dùng (User-Level Thread) và Luồng mức nhân hệ điều hành (Kernel-Level Thread).

## 핵심 키워드 (Từ khóa)
- 프로세스 vs 스레드 (Process vs Thread)
- 프로세스 상태 전이 (Process State Transitions)
- 디타블웨 (Mnemonic: Dispatch, Timeout, Block, Wakeup)
- PCB (Process Control Block / 프로세스 제어 블록)
- 문맥 교환 (Context Switching / 오버헤드 발생)
- 사용자 수준 스레드 vs 커널 수준 스레드 (User-level vs Kernel-level Thread)
- 자원 공유 (Resource Sharing / Code, Data, Heap 공유)

## 선행·연결 개념 (Kiến thức liên kết)
- [38-bai-hoc.md](38-bai-hoc.md): Quản lý bộ nhớ ảo và hiện tượng Thrashing.
- [40-bai-hoc.md](40-bai-hoc.md): Thuật toán lập lịch điều phối CPU cho tiến trình.
- [33-bai-hoc.md](33-bai-hoc.md): Tổng quan quản lý tiến trình và bộ nhớ.

## 읽는 방법 (Cách đọc)
- Học theo thần chú 4 sự kiện chuyển đổi trạng thái tiến trình: **디·타·블·웨**
  - **디 (Dispatch):** Tiến trình ở trạng thái **Ready $\rightarrow$ Running** (Được bộ lập lịch cấp phát CPU để chạy).
  - **타 (Timeout):** Tiến trình ở trạng thái **Running $\rightarrow$ Ready** (Đang chạy nhưng hết thời lượng lượng tử Time Quantum, bị thu hồi CPU nhường cho tiến trình khác).
  - **블 (Block):** Tiến trình ở trạng thái **Running $\rightarrow$ Wait/Block** (Đang chạy nhưng chủ động phát sinh yêu cầu I/O hoặc tài nguyên chưa sẵn sàng, phải tạm dừng chờ).
  - **웨 (Wakeup):** Tiến trình ở trạng thái **Wait/Block $\rightarrow$ Ready** (Sự kiện I/O đã hoàn tất, chuyển về hàng đợi sẵn sàng để chờ được cấp CPU trở lại).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng 4 chuyển đổi trạng thái tiến trình cốt lõi (디타블웨):**

| Sự kiện chuyển trạng thái | Trạng thái bắt đầu | Trạng thái đích | Nguyên nhân phát sinh sự kiện |
| :--- | :--- | :--- | :--- |
| **1. 디스패치 (Dispatch)** | **준비 (Ready)** | **실행 (Running)** | Bộ điều phối chọn tiến trình đầu tiên trong hàng đợi Ready và giao quyền chiếm dụng CPU |
| **2. 타임아웃 (Timeout)** | **실행 (Running)** | **준비 (Ready)** | Tiến trình chạy hết thời gian chia sẻ cho phép (**Time Slice / Quantum 만료**); bị ngắt đồng hồ hệ thống |
| **3. 블록 (Block)** | **실행 (Running)** | **대기 (Wait/Block)** | Tiến trình tự ngưng chạy để **chờ một tác vụ nhập/xuất (I/O 요청)** hoặc tín hiệu đồng bộ |
| **4. 웨이크업 (Wakeup)** | **대기 (Wait/Block)** | **준비 (Ready)** | Sự kiện **nhập/xuất đã hoàn thành xong (I/O 완료)**; sẵn sàng nhận lại CPU |

- **Bảng so sánh: Tiến trình (Process) vs Luồng (Thread):**

| Tiêu chuẩn so sánh | 프로세스 (Process) | 스레드 (Thread / Lightweight Process) |
| :--- | :--- | :--- |
| **Định nghĩa** | Một chương trình độc lập đang nạp và chạy trên bộ nhớ | Một đơn vị luồng thực thi lệnh **bên trong** một tiến trình |
| **Không gian địa chỉ** | Mỗi tiến trình sở hữu **không gian bộ nhớ riêng biệt hoàn toàn** | Các luồng trong cùng 1 tiến trình **chia sẻ chung vùng Code, Data, Heap** |
| **Tài nguyên độc lập** | Sở hữu toàn bộ tài nguyên: PCB, bộ nhớ, bảng tệp | Mỗi luồng chỉ có riêng: **Con trỏ lệnh PC, Tập thanh ghi (Registers), và Vùng nhớ Ngăn xếp (Stack)** |
| **Chi phí chuyển đổi (Context Switch)** | **Rất lớn (Nặng nề)**; phải hoán đổi bảng trang và thanh ghi | **Rất nhỏ (Nhẹ nhàng)**; tốc độ chuyển đổi giữa các luồng cực nhanh |
| **Mức độ an toàn** | Một tiến trình sập không ảnh hưởng tới tiến trình khác | Một luồng bị lỗi bộ nhớ có thể **làm sập toàn bộ tiến trình cha** |

- **Bảng so sánh: Luồng mức người dùng vs Luồng mức nhân:**

| Tiêu chí | 사용자 수준 스레드 (User-Level Thread) | 커널 수준 스레드 (Kernel-Level Thread) |
| :--- | :--- | :--- |
| **Quản lý bởi** | Thư viện luồng trong không gian người dùng (Pthreads) | Nhân hệ điều hành (Kernel) trực tiếp điều phối |
| **Tốc độ chuyển đổi** | Rất nhanh; không cần chuyển chế độ sang Kernel Mode | Chậm hơn một chút; phải chuyển ngữ cảnh ở mức hệ điều hành |
| **Khả năng đa xử lý** | Nếu 1 luồng bị khóa I/O, **toàn bộ tiến trình bị khóa theo** | Một luồng bị khóa I/O, **các luồng khác vẫn chạy bình thường trên lõi CPU khác** |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Các thông tin bắt buộc phải có trong PCB (Process Control Block):**
  1. Mã định danh tiến trình (PID - Process ID).
  2. Trạng thái hiện tại của tiến trình (Ready, Running, Waiting...).
  3. Thanh ghi đếm chương trình (Program Counter - PC) lưu địa chỉ lệnh thực thi tiếp theo.
  4. Trạng thái các thanh ghi CPU (Registers Context).
  5. Thông tin quản lý bộ nhớ (Base/Limit Registers, Page Table).
  6. Danh sách các tệp đang mở (Open File Descriptors) và thông tin thiết bị I/O.

### 복습 체크리스트
- [ ] Nhớ thần chú 4 sự kiện chuyển đổi trạng thái: 디타블웨 (Dispatch, Timeout, Block, Wakeup).
- [ ] Nhớ các Thread trong cùng 1 Process chia sẻ chung Code, Data, Heap; chỉ có riêng Stack và Registers.
- [ ] Nhớ Context Switching là việc lưu PCB của tiến trình cũ và nạp PCB của tiến trình mới.
- [ ] Phân biệt được ưu/nhược điểm của User-level thread và Kernel-level thread.
