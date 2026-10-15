# 086. 프로세스 스케줄링 (Process Scheduling)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm và mục tiêu của việc lập lịch điều phối CPU (프로세스 스케줄링 - Process Scheduling): tối ưu hóa việc phân chia thời gian chiếm dụng CPU giữa các tiến trình cạnh tranh.
- Phân biệt sâu sắc và toàn diện giữa hai trường phái lập lịch: Lập lịch độc quyền bất khả xâm phạm (비선점형 - Non-Preemptive) và Lập lịch chiếm quyền ưu tiên (선점형 - Preemptive).
- Nắm vững nguyên lý và phương pháp tính toán thời gian chờ đợi trung bình (Average Waiting Time) của các thuật toán: FCFS, SJF, Round Robin (RR), và công thức tính độ ưu tiên của thuật toán HRN.

## 핵심 키워드 (Từ khóa)
- 프로세스 스케줄링 (Process Scheduling)
- 비선점형 스케줄링 (Non-Preemptive / FCFS, SJF, HRN)
- 선점형 스케줄링 (Preemptive / Round Robin, SRT, MLQ, MLFQ)
- FCFS (First-Come First-Served / 도착 순서대로 처리)
- SJF (Shortest Job First / 평균 대기 시간 최소)
- HRN (Highest Response-ratio Next / `(대기+서비스)/서비스`)
- 라운드 로빈 (Round Robin / RR / 시분할 할당량 Time Slice)
- SRT (Shortest Remaining Time / 잔여 시간 최소 우선)

## 선행·연결 개념 (Kiến thức liên kết)
- [39-bai-hoc.md](39-bai-hoc.md): Tiến trình, luồng (Thread) và các trạng thái chuyển đổi.
- [41-bai-hoc.md](41-bai-hoc.md): Thuật toán thay thế trang bộ nhớ (Page Replacement).
- [33-bai-hoc.md](33-bai-hoc.md): Quản lý bộ nhớ và điều phối tiến trình cơ bản.

## 읽는 방법 (Cách đọc)
- Phân loại nhanh hai trường phái lập lịch qua quyền lực của hệ điều hành:
  - **비선점형 (Non-Preemptive - Không chiếm quyền):** Khi một tiến trình đã được giao CPU, nó sẽ **chạy liên tục cho đến khi hoàn thành xong hoặc tự nguyện nhường CPU** (đi vào I/O). Hệ điều hành không thể can thiệp giật lại CPU giữa chừng $\rightarrow$ An toàn, ít chi phí Context Switch nhưng tiến trình ngắn phải đợi lâu (Đại diện: **FCFS, SJF, HRN, Priority, Deadline**).
  - **선점형 (Preemptive - Chiếm quyền ưu tiên):** Hệ điều hành giữ quyền tối cao; nếu có tiến trình có độ ưu tiên cao hơn xuất hiện hoặc tiến trình hiện tại hết thời lượng chia sẻ (Time Quantum), hệ điều hành sẽ **ngay lập tức tước đoạt CPU** để giao cho tiến trình khác $\rightarrow$ Đáp ứng thời gian thực nhanh, phù hợp hệ thống tương tác nhưng tốn nhiều chi phí Context Switch (Đại diện: **Round Robin - RR, SRT, Multi-level Queue - MLQ, Multi-level Feedback Queue - MLFQ**).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng phân loại các thuật toán lập lịch CPU:**

| Phân loại | Tên giải thuật | Nguyên lý chọn tiến trình tiếp theo | Ưu điểm & Hạn chế cốt lõi |
| :--- | :--- | :--- | :--- |
| **비선점형 (Non-Preemptive)** | **FCFS (FIFO)** | Đến trước phục vụ trước theo thứ tự hàng đợi | Đơn giản; dễ bị hiệu ứng đoàn tàu (**Convoy Effect**) khi việc dài đứng đầu |
|  | **SJF** | Chọn tiến trình có **thời gian thực thi ngắn nhất (Burst Time nhỏ nhất)** | **Thời gian chờ trung bình ngắn nhất**; tiến trình dài dễ bị đói tài nguyên (**기아 현상 - Starvation**) |
|  | **HRN** | Tính chỉ số ưu tiên: $\frac{\text{대기시간} + \text{서비스시간}}{\text{서비스시간}}$ | **Khắc phục triệt để nhược điểm Starvation của SJF**; chỉ số lớn nhất chạy trước |
| **선점형 (Preemptive)** | **Round Robin (RR)** | Cấp phát CPU luân phiên theo từng lượng tử thời gian (**Time Slice / Quantum**) | Công bằng tuyệt đối; hệ thống tương tác tốt; Time Slice quá nhỏ gây nghẽn Context Switch |
|  | **SRT** | Phiên bản chiếm quyền của SJF; ưu tiên tiến trình có **thời gian còn lại ngắn nhất (Shortest Remaining Time)** | Hiệu quả cao nhưng tốn chi phí liên tục tính toán thời gian còn lại |
|  | **MLQ / MLFQ** | Hàng đợi đa cấp; MLFQ cho phép tiến trình dịch chuyển giữa các hàng đợi | Hệ thống lập lịch linh hoạt và thông minh nhất của các HĐH hiện đại |

- **Bài toán thi mẫu: Tính thời gian chờ trung bình của giải thuật FCFS:**
  - *Dữ liệu:* 3 tiến trình cùng đến tại thời điểm $t = 0$:
    - $P1$: Thời gian chạy 24 ms.
    - $P2$: Thời gian chạy 3 ms.
    - $P3$: Thời gian chạy 3 ms.
  - *Biểu đồ Gantt:* `| P1 (0 - 24) | P2 (24 - 27) | P3 (27 - 30) |`
  - *Thời gian chờ của từng tiến trình:*
    - $P1$ được chạy ngay tại $0$ $\rightarrow$ Chờ $0\text{ ms}$.
    - $P2$ phải đợi $P1$ xong $\rightarrow$ Chờ $24\text{ ms}$.
    - $P3$ phải đợi $P1$ và $P2$ xong $\rightarrow$ Chờ $27\text{ ms}$.
  - *Thời gian chờ trung bình:* $\frac{0 + 24 + 27}{3} = \frac{51}{3} = \mathbf{17\text{ ms}}$.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tác động của Lượng tử thời gian (Time Slice) trong Round Robin:**
  - Nếu Time Slice được đặt **quá lớn ($\rightarrow \infty$)**: Thuật toán Round Robin sẽ thoái hóa thành giải thuật **FCFS**.
  - Nếu Time Slice được đặt **quá nhỏ ($\rightarrow 0$)**: Tần suất ngắt đồng hồ và chi phí chuyển đổi ngữ cảnh (**문맥 교환 오버헤드 - Context Switch Overhead**) bùng nổ, CPU mất hết thời gian chỉ để lưu và nạp PCB thay vì xử lý dữ liệu.

### 복습 체크리스트
- [ ] Phân loại đúng: 비선점형 (FCFS, SJF, HRN) vs 선점형 (RR, SRT, MLQ, MLFQ).
- [ ] Nhớ công thức HRN: $(W + S) / S$ và ý nghĩa khắc phục Starvation của SJF.
- [ ] Vẽ được biểu đồ Gantt và tính thời gian chờ trung bình cho các tiến trình.
- [ ] Nêu được hệ quả khi Time Slice của Round Robin quá lớn (biến thành FCFS) hoặc quá nhỏ (quá tải Context Switch).
