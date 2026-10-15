# 298. PCB (Process Control Block)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, vòng đời khởi tạo/hủy bỏ và vai trò hạt nhân của Khối điều khiển tiến trình (**PCB - Process Control Block / 프로세스 제어 블록**) trong hệ điều hành.
- Thuộc lòng danh sách các thông tin quản trị cốt lõi được lưu trữ bên trong một PCB: Định danh tiến trình (PID), Trạng thái tiến trình (State), Con trỏ lệnh (Program Counter), Con trỏ thanh ghi CPU, Thông tin lập lịch, và Thông tin quản lý bộ nhớ.
- Thấu hiểu cơ chế chuyển đổi ngữ cảnh (**문맥 교환 - Context Switching**) và cách thức hệ điều hành sử dụng PCB để lưu lại trạng thái và khôi phục việc thực thi tiến trình không bị gián đoạn.

## 핵심 키워드 (Từ khóa)
- PCB (Process Control Block - 프로세스 제어 블록)
- 프로세스 식별자 (PID - Process ID)
- 프로세스 상태 (State: 생성, 준비, 실행, 대기, 종료)
- 프로그램 카운터 (PC - Program Counter / 다음에 실행할 명령어 주소)
- CPU 레지스터 정보 (CPU Registers Context)
- 문맥 교환 (Context Switching)
- 프로세스 생성 시 생성 및 종료 시 폐기 (Lifecycle Synchronization)

## 선행·연결 개념 (Kiến thức liên kết)
- [90-bai-hoc.md](90-bai-hoc.md): Thuật toán thay thế trang nhớ trong bộ nhớ ảo.
- [89-bai-hoc.md](89-bai-hoc.md): Cấu trúc hệ thống UNIX và vai trò của Kernel.
- [39-bai-hoc.md](39-bai-hoc.md): Vòng đời trạng thái tiến trình và chuyển đổi trạng thái.

## 읽는 방법 (Cách đọc)
- Trong bài thi kỹ sư CNTT:
  - Khái niệm: PCB là **cấu trúc dữ liệu do hệ điều hành tạo ra để lưu trữ toàn bộ thông tin cần thiết nhằm quản lý và điều phối một tiến trình**.
  - Vòng đời: PCB **được tạo ra ngay khi tiến trình sinh ra (Process Creation)** và **bị xóa bỏ hoàn toàn khi tiến trình kết thúc (Process Termination)**.
  - Context Switching: Khi CPU chuyển từ tiến trình $A$ sang tiến trình $B$, toàn bộ ngữ cảnh thanh ghi và địa chỉ lệnh kế tiếp ($PC$) của $A$ được lưu vào $\text{PCB}_A$, sau đó ngữ cảnh của $B$ được khôi phục từ $\text{PCB}_B$ vào CPU.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng liệt kê các thông tin lưu trữ bên trong PCB:**

| Mục thông tin | Tên tiếng Hàn & Anh | Ý nghĩa kỹ thuật chi tiết |
| :--- | :--- | :--- |
| **Định danh tiến trình** | **PID (Process ID)** | Mã số nguyên duy nhất do hệ điều hành cấp phát để phân biệt tiến trình này với các tiến trình khác trong hệ thống. |
| **Trạng thái tiến trình** | **프로세스 상태 (State)** | Trạng thái hiện tại của tiến trình: Chuẩn bị (**Ready**), Đang chạy (**Running**), Chờ sự kiện (**Waiting / Blocked**), v.v. |
| **Con trỏ lệnh** | **프로그램 카운터 (PC)** | Lưu **địa chỉ của câu lệnh kế tiếp** mà tiến trình sẽ thực thi khi được hệ điều hành cấp phát lại CPU. |
| **Thanh ghi CPU** | **CPU 레지스터 정보** | Bản sao lưu giá trị của các thanh ghi tích lũy (Accumulator), thanh ghi chỉ số (Index), và con trỏ ngăn xếp (Stack Pointer) tại thời điểm bị ngắt. |
| **Thông tin lập lịch** | **스케줄링 정보 (Scheduling)** | Mức độ ưu tiên của tiến trình (Priority), con trỏ trỏ tới các hàng đợi lập lịch (Ready Queue). |
| **Thông tin quản lý bộ nhớ** | **메모리 관리 정보** | Thông tin về bảng trang (Page Table), bảng phân đoạn (Segment Table), hoặc thanh ghi cơ sở và thanh ghi giới hạn (Base/Limit Registers). |
| **Thông tin tài khoản** | **계정 정보 (Accounting)** | Thời gian CPU đã sử dụng, thời gian giới hạn tối đa, số hiệu tài khoản người dùng sở hữu. |
| **Trạng thái vào/ra** | **입출력 상태 정보 (I/O Status)** | Danh sách các thiết bị I/O được cấp phát cho tiến trình, danh sách các tệp tin đang mở (Open File Descriptors). |

- **2. Quy trình Chuyển đổi ngữ cảnh (Context Switching) với PCB:**
  1. Tiến trình $P_1$ đang chạy trên CPU thì xảy ra tín hiệu ngắt (Interrupt / Timeout).
  2. Hệ điều hành lưu toàn bộ trạng thái hiện tại của CPU ($PC$, thanh ghi, cờ trạng thái) vào $\text{PCB}_1$.
  3. Trạng thái của $P_1$ chuyển từ `Running` sang `Ready` (hoặc `Waiting`).
  4. Bộ điều phối (Scheduler) chọn tiến trình kế tiếp $P_2$ từ hàng đợi `Ready`.
  5. Hệ điều hành nạp lại trạng thái đã lưu từ $\text{PCB}_2$ vào các thanh ghi của CPU.
  6. $P_2$ tiếp tục thực thi từ địa chỉ ghi trong con trỏ lệnh $PC$ của nó.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Chi phí Overhead của Context Switching:**
  - Context Switching hoàn toàn là chi phí quản lý phụ trội (Overhead) thuần túy vì trong suốt thời gian CPU thực hiện lưu/khôi phục PCB, hệ thống không thực thi bất kỳ phép tính nghiệp vụ hữu ích nào của người dùng.
  - Do đó việc sử dụng Luồng (Thread) chia sẻ chung không gian địa chỉ bộ nhớ và bảng tệp tin được ưu tiên vì Context Switching giữa các Thread trong cùng một tiến trình nhẹ hơn rất nhiều so với giữa hai Process độc lập.

### 복습 체크리스트
- [ ] Ghi nhớ PCB được tạo ra khi tiến trình bắt đầu và bị xóa bỏ khi tiến trình kết thúc.
- [ ] Nhớ Program Counter (PC) trong PCB lưu địa chỉ câu lệnh kế tiếp sẽ chạy.
- [ ] Kể tên các thông tin cốt lõi trong PCB: PID, State, PC, Registers, Memory info, I/O info.
- [ ] Hiểu rõ cơ chế Context Switching: Lưu trạng thái vào PCB cũ, nạp trạng thái từ PCB mới.
