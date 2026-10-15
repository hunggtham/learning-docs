# 주요 스케줄링 알고리즘 (Các Thuật toán Lập lịch CPU Cốt lõi)

## 학습 목표 (Mục tiêu)
- Phân biệt rõ hai trường phái lập lịch CPU trong hệ điều hành: Lập lịch không chiếm đoạt (비선점형 - Non-Preemptive) và Lập lịch chiếm đoạt (선점형 - Preemptive).
- Nắm vững nguyên lý và bài toán tính toán thời gian chờ trung bình của các thuật toán: FCFS, SJF, Round Robin.
- Làm chủ công thức tính độ ưu tiên trong thuật toán HRN (Highest Response-ratio Next) và cơ chế khắc phục tình trạng đói tài nguyên (Starvation).
- Phân tích tác động của độ dài lượng tử thời gian (Time Quantum) trong thuật toán Round Robin.

## 핵심 키워드 (Từ khóa)
- **비선점형 스케줄링 (Non-Preemptive)**: FCFS (FIFO, Convoy Effect), SJF (tối ưu thời gian chờ, nguy cơ đói tài nguyên), HRN (công thức tỷ lệ phản hồi).
- **선점형 스케줄링 (Preemptive)**: Round Robin (lát thời gian Time Quantum), SRT (Shortest Remaining Time), MLFQ (Multi-Level Feedback Queue).
- **HRN 우선순위 계산식**: $\frac{\text{대기 시간} + \text{서비스 시간}}{\text{서비스 시간}}$ (Càng lớn càng ưu tiên).
- **Starvation (기아 현상)**: Tiến trình dài chờ đợi vô hạn định; giải quyết bằng kỹ thuật Aging (lão hóa).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [62-bai-hoc.md](62-bai-hoc.md) (Trạng thái tiến trình và Dispatch).
- Liên kết với [56-bai-hoc.md](56-bai-hoc.md) (Chỉ số Turnaround Time của hệ điều hành).
- Liên kết với [04-programming-language/84-bai-hoc.md](../../04-programming-language/lessons/84-bai-hoc.md) (Chi tiết các thuật toán điều độ).

## 읽는 방법 (Cách đọc)
- Đi thi chú ý công thức tính toán HRN:
  - Công thức: $\text{Ưu tiên} = \frac{\text{Thời gian chờ} + \text{Thời gian chạy}}{\text{Thời gian chạy}} = 1 + \frac{\text{Thời gian chờ}}{\text{Thời gian chạy}}$.
  - Tính ra số nào **lớn nhất** thì tiến trình đó được **chọn chạy trước tiên**!
  - Trong Round Robin: Time Quantum quá lớn $\rightarrow$ suy biến thành FCFS; Time Quantum quá nhỏ $\rightarrow$ tiêu tốn thời gian cho Context Switch.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng phân loại Lập lịch Chiếm đoạt vs Không chiếm đoạt
| Phân loại | Khái niệm bản chất | Ưu điểm & Nhược điểm | Các thuật toán tiêu biểu |
| :--- | :--- | :--- | :--- |
| **비선점형 / (Non-Preemptive)** | Khi CPU đã được cấp cho một tiến trình, hệ điều hành **không thể cưỡng chế thu hồi** cho đến khi tiến trình tự hoàn thành hoặc tự nhả CPU | Chi phí chuyển ngữ cảnh thấp, dễ dự đoán; Tiến trình ngắn đến sau phải đợi tiến trình dài phía trước | **FCFS**, **SJF**, **HRN**, Lập lịch ưu tiên tĩnh (Priority) |
| **선점형 / (Preemptive)** | Hệ điều hành **có quyền ngắt lời và thu hồi CPU** từ tiến trình đang chạy để chuyển giao cho tiến trình ưu tiên hơn | Thời gian đáp ứng nhanh, phù hợp hệ thống tương tác và thời gian thực; Chi phí Context Switch cao | **Round Robin (RR)**, **SRT**, Hàng đợi đa cấp (MLQ), Hàng đợi phản hồi đa cấp (MLFQ) |

#### 2. Chi tiết 4 thuật toán thường gặp trong đề thi
- **FCFS (First Come First Service)**:
  - Nguyên lý: Tiến trình nào đến hàng đợi sẵn sàng (Ready Queue) trước sẽ được cấp CPU chạy trước.
  - Nhược điểm: Hiệu ứng đoàn tàu (**Convoy Effect**) - một tiến trình dài chạy trước sẽ làm tất cả các tiến trình ngắn chạy sau bị kéo dài thời gian chờ đợi.
- **SJF (Shortest Job First)**:
  - Nguyên lý: Lựa chọn tiến trình có thời gian thực thi (Service/Burst Time) ngắn nhất để chạy trước.
  - Ưu điểm: Đảm bảo **thời gian chờ đợi trung bình (Average Waiting Time) là nhỏ nhất** trong mọi thuật toán không chiếm đoạt.
  - Nhược điểm: Hiện tượng **Đói tài nguyên (Starvation)** - nếu các tiến trình ngắn liên tục xuất hiện, tiến trình có thời gian dài sẽ phải chờ đợi vô hạn định.
- **HRN (Highest Response-ratio Next)**:
  - Nguyên lý: Cải tiến của SJF nhằm khắc phục hiện tượng Starvation bằng cách kết hợp cả thời gian đã chờ đợi vào công thức tính độ ưu tiên:
    $$\text{Độ ưu tiên (Priority)} = \frac{\text{Thời gian chờ (Waiting Time)} + \text{Thời gian dịch vụ (Service Time)}}{\text{Thời gian dịch vụ (Service Time)}}$$
  - Cơ chế Aging (Lão hóa): Càng chờ lâu trong hàng đợi, giá trị tử số càng lớn $\rightarrow$ Độ ưu tiên tự động tăng dần theo thời gian, đảm bảo các tiến trình dài cuối cùng cũng sẽ được chạy.
- **Round Robin (RR)**:
  - Mỗi tiến trình được cấp một khoảng thời gian CPU cố định gọi là lát thời gian lượng tử (**Time Quantum** hoặc Time Slice).
  - Hết thời gian lượng tử, tiến trình bị ngắt cưỡng bức đưa về cuối hàng đợi Ready (Preemptive) để nhường quyền cho tiến trình tiếp theo.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán tính độ ưu tiên HRN trong đề thi Kỹ sư xử lý thông tin
- *Đề bài*: Cho 3 tiến trình A, B, C trong hàng đợi sẵn sàng với các thông số sau. Hãy xác định tiến trình nào được cấp CPU thực thi tiếp theo theo thuật toán HRN?
  - Tiến trình A: Thời gian chờ $= 20$, Thời gian dịch vụ $= 10$
  - Tiến trình B: Thời gian chờ $= 10$, Thời gian dịch vụ $= 5$
  - Tiến trình C: Thời gian chờ $= 30$, Thời gian dịch vụ $= 15$
- *Lời giải chi tiết*:
  - Độ ưu tiên A $= \frac{20 + 10}{10} = \frac{30}{10} = 3.0$
  - Độ ưu tiên B $= \frac{10 + 5}{5} = \frac{15}{5} = 3.0$
  - Độ ưu tiên C $= \frac{30 + 15}{15} = \frac{45}{15} = 3.0$
  - Nếu bằng nhau: Hệ thống áp dụng FCFS theo thứ tự đến trước. Giả sử tiến trình D có: Chờ $= 40$, Dịch vụ $= 10 \rightarrow \frac{40+10}{10} = 5.0 \rightarrow$ D sẽ được ưu tiên cao nhất!

#### 2. Đánh đổi độ dài Time Quantum trong Round Robin
```
[Time Quantum q quá lớn (q ──► ∞)] ──► Trở thành FCFS thuần túy (Mất tính tương tác)
                                          ▲
                                          │ Vùng tối ưu (10ms - 100ms)
                                          ▼
[Time Quantum q quá nhỏ (q ──► 0)] ──► CPU bận rộn chuyển cảnh (Context Switch Overhead)
```

---

### 복습 체크리스트
- [ ] Sự khác biệt cơ bản giữa thuật toán lập lịch 선점형 (Preemptive) và 비선점형 (Non-Preemptive) là gì?
- [ ] Tại sao thuật toán SJF đạt thời gian chờ trung bình ngắn nhất nhưng lại ít được dùng trong thực tế?
- [ ] Viết chính xác công thức tính độ ưu tiên trong thuật toán HRN?
- [ ] Điều gì xảy ra với hệ thống nếu lát thời gian (Time Quantum) trong Round Robin được thiết lập quá nhỏ?
