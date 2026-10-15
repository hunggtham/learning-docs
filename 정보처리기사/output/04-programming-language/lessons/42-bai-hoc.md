# 297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)

## 학습 목표 (Mục tiêu)
- Tổng hợp toàn diện kiến thức về Tiến trình (Process), Luồng thực thi (Thread) và các thuật toán lập lịch CPU trong đề thi Kỹ sư xử lý thông tin.
- Rèn luyện kỹ năng giải các bài toán tính toán định lượng: Tính độ ưu tiên HRN, vẽ sơ đồ Gantt và tính thời gian quay vòng trung bình (Average Turnaround Time).
- Phân tích sâu sắc sự đánh đổi giữa hiệu năng song hành (Concurrency) và chi phí chuyển đổi ngữ cảnh (Context Switching Overhead).

## 핵심 키워드 (Từ khóa)
- 프로세스 제어 블록 (PCB / Process Control Block)
- 스레드 동시성 (Thread Concurrency / 경량 프로세스)
- 문맥 교환 오버헤드 (Context Switch Overhead)
- 선점 vs 비선점 스케줄링 (Preemptive vs Non-Preemptive)
- FCFS, SJF, HRN 종합 분석
- 라운드 로빈 (RR / Time Quantum)

## 선행·연결 개념 (Kiến thức liên kết)
- [41-bai-hoc.md](41-bai-hoc.md): Lập lịch tiến trình và bế tắc hệ thống (Deadlock).
- [43-bai-hoc.md](43-bai-hoc.md): Tổng quan mạng truyền thông và giao thức OSI.
- [40-bai-hoc.md](40-bai-hoc.md): Chi tiết các thuật toán lập lịch CPU.

## 읽는 방법 (Cách đọc)
- Ôn tập hệ thống qua 3 mối quan hệ tương hỗ:
  - **Tiến trình & Luồng:** 1 Tiến trình có thể chứa nhiều Luồng. Các Luồng dùng chung tài nguyên Code/Data/Heap $\rightarrow$ Giúp tăng tốc độ giao tiếp và giảm đáng kể chi phí chuyển đổi so với giữa hai Tiến trình riêng biệt.
  - **Lập lịch Non-Preemptive (FCFS, SJF, HRN):** Không tước đoạt CPU giữa chừng. Chú ý tính toán chỉ số HRN:
    $$\text{HRN Priority} = \frac{\text{Wait} + \text{Service}}{\text{Service}}$$
  - **Lập lịch Preemptive (Round Robin, SRT):** Tước đoạt CPU định kỳ. Cần theo dõi lượng tử thời gian Time Slice và hàng đợi vòng lặp.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp đặc tính các thuật toán điều phối CPU:**

| Thuật toán | Phân loại | Tiêu chí cấp phát CPU | Hệ quả / Bẫy đề thi |
| :--- | :--- | :--- | :--- |
| **FCFS** | **비선점형 (Non-Preemptive)** | Tiến trình nào đến hàng đợi trước được chạy trước | Dễ bị hiệu ứng đoàn tàu (**Convoy Effect**), thời gian chờ trung bình cao |
| **SJF** | **비선점형 (Non-Preemptive)** | Tiến trình có thời gian chạy ngắn nhất được chạy trước | **Thời gian chờ trung bình tối ưu nhất**; nguy cơ Starvation cho tiến trình dài |
| **HRN** | **비선점형 (Non-Preemptive)** | Tiến trình có chỉ số $\frac{W+S}{S}$ lớn nhất được chạy trước | **Khắc phục Starvation**; cân bằng giữa tiến trình dài và ngắn |
| **Round Robin (RR)** | **선점형 (Preemptive)** | Cấp phát luân phiên theo lượng tử thời gian $q$ | Nếu $q$ quá lớn biến thành FCFS; nếu $q$ quá nhỏ gây nghẽn Context Switch |
| **SRT** | **선점형 (Preemptive)** | Tiến trình có thời gian còn lại ít nhất được cướp CPU | Thời gian đáp ứng tốt nhưng tốn tài nguyên đo đạc thời gian còn lại |

- **Bài toán thi mẫu tính toán tổng hợp HRN:**
  - *Dữ liệu đề bài:* Xác định thứ tự ưu tiên của 3 tiến trình sau:
    - $P_1$: Thời gian chờ $W = 30$, Thời gian chạy $S = 10 \rightarrow \text{Ưu tiên} = \frac{30 + 10}{10} = \mathbf{4.0}$.
    - $P_2$: Thời gian chờ $W = 20$, Thời gian chạy $S = 20 \rightarrow \text{Ưu tiên} = \frac{20 + 20}{20} = \mathbf{2.0}$.
    - $P_3$: Thời gian chờ $W = 10$, Thời gian chạy $S = 5 \rightarrow \text{Ưu tiên} = \frac{10 + 5}{5} = \mathbf{3.0}$.
  - *Kết luận thứ tự thực thi:* Do $4.0 > 3.0 > 2.0$, thứ tự chạy là: **$P_1 \rightarrow P_3 \rightarrow P_2$**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tác động của Context Switching đối với bộ nhớ Cache:**
  - Khi CPU chuyển từ Tiến trình $A$ sang Tiến trình $B$, các dữ liệu lưu trên bộ nhớ đệm L1/L2/L3 Cache của $A$ trở nên vô dụng đối với $B$ (Cold Cache).
  - Tiến trình $B$ sẽ phải mất thời gian nạp lại dữ liệu từ RAM lên Cache (gây ra hàng loạt Cache Miss). Do đó, tần suất Context Switch quá cao sẽ làm sụt giảm nghiêm trọng hiệu năng của hệ thống đa nhiệm.

### 복습 체크리스트
- [ ] Phân biệt được đặc tính Non-Preemptive (FCFS, SJF, HRN) và Preemptive (RR, SRT).
- [ ] Tính thành thạo chỉ số ưu tiên HRN: $(W + S) / S$.
- [ ] Nhớ hiện tượng Convoy Effect xảy ra trong FCFS khi tiến trình dài đứng đầu.
- [ ] Nhớ hiện tượng Cold Cache và quá tải khi tần suất Context Switch quá cao.
