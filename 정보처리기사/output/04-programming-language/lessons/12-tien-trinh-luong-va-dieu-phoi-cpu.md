# 프로세스, 스레드 및 CPU 스케줄링 알고리즘 (Tiến trình, Luồng & Điều phối CPU)

## 학습 목표 (Mục tiêu)
- Nắm vững sự khác nhau giữa Tiến trình (Process - không gian độc lập) và Tiểu trình (Thread - chia sẻ Code, Data, Heap), cùng các thành phần lưu trữ bên trong Khối điều khiển tiến trình (PCB - Process Control Block).
- Thấu hiểu sơ đồ 5 trạng thái vòng đời tiến trình (생성 $\rightarrow$ 준비 $\leftrightarrow$ 실행 $\rightarrow$ 대기 $\rightarrow$ 종료) và bản chất của 4 sự kiện chuyển trạng thái: Dispatch, Timeout, Block, Wakeup.
- Phân biệt triệt để hai nhóm giải thuật điều phối CPU: Phi trưng dụng (비선점형: FCFS, SJF, HRN) và Trưng dụng (선점형: Round Robin, SRT, MLQ, MFQ); áp dụng thành thạo công thức ưu tiên HRN $\frac{W+S}{S}$ và tính toán thời gian chờ trung bình.

## 핵심 키워드 (Từ khóa)
- 프로세스 vs 스레드 (Process vs Thread) — Đơn vị tài nguyên độc lập vs Đơn vị thực thi nhẹ chia sẻ bộ nhớ.
- 프로세스 제어 블록 (PCB - Process Control Block) — PID, 상태, PC, 레지스터, 스케줄링 정보 저장.
- 상태 전이 (State Transitions) — Dispatch, Timeout, Block (I/O 요청), Wakeup (I/O 완료).
- 비선점형 스케줄링 (Non-preemptive) — FCFS, SJF (최단 작업 우선, 기아 발생 가능), HRN (기아 방지 공식).
- 선점형 스케줄링 (Preemptive) — Round Robin (Time Slice), SRT (최소 잔여 시간), MLQ, MFQ.
- 문맥 교환 (Context Switching) — Chi phí lưu và phục hồi PCB khi CPU chuyển đổi tiến trình.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa từ `11-tong-quan-he-dieu-hanh-unix-linux-va-shell-script.md` khi một tệp thực thi mã máy được nạp vào bộ nhớ để vận hành.
- **Đang giải quyết gì (Current Problem):** Giải quyết câu hỏi: Trong môi trường đa nhiệm (Multi-tasking), làm sao để CPU phân chia thời gian hợp lý cho hàng trăm tiến trình cùng lúc, tối ưu hóa năng suất và không để bất kỳ tiến trình nào bị "bỏ đói" vô hạn định (Starvation).
- **Dùng đi đâu (Forward Handoff):** Khi nhiều tiến trình cùng chạy đồng thời và cạnh tranh tài nguyên hữu hạn của hệ thống, nguy cơ xảy ra khóa chết (Deadlock) là rất cao; chuyên đề xử lý Deadlock sẽ được giải quyết ở bài `13-khoa-chet-deadlock-va-dong-bo-hoa-tien-trinh.md`.

## 읽는 방법 (Cách đọc)
- **Công thức HRN (Highest Response Ratio Next):** Bắt buộc phải thuộc lòng:
  $$\text{Độ ưu tiên} = \frac{\text{Thời gian chờ } W + \text{Thời gian thực thi } S}{S} = \frac{W + S}{S}$$
  Giá trị tính ra **càng lớn thì độ ưu tiên càng cao**, được chọn chạy trước. Công thức này giúp tiến trình dù dài đến mấy nhưng chờ lâu ($W$ lớn) vẫn sẽ được chạy, khắc phục triệt để lỗi bỏ đói của SJF.
- **Chuyển trạng thái Wakeup:** Khi thiết bị I/O xong, tiến trình từ trạng thái Chờ (**Wait/Block**) chuyển về trạng thái Sẵn sàng (**Ready**), **tuyệt đối không nhảy thẳng sang Running**.
- **Time Slice của Round Robin:** Time slice quá lớn biến thành FCFS; Time slice quá nhỏ làm nghẽn hệ thống do Context Switching liên tục.

---

## 프로세스, 스레드 및 CPU 스케줄링 알고리즘

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `스레드는 프로세스 내에서 Code, Data, Heap 영역을 공유하고 Stack과 PC만 독립적으로 갖는다. I/O 완료 시 프로세스는 대기(Wait)에서 준비(Ready) 상태로 전이된다. HRN 스케줄링의 우선순위 계산식은 (대기시간+서비스시간)/서비스시간이며 값이 클수록 우선순위가 높다.`
  - [Tiếng Việt]: Thread chia sẻ vùng Code, Data, Heap trong tiến trình và chỉ sở hữu riêng Stack cùng Program Counter. Khi hoàn tất I/O, tiến trình chuyển từ trạng thái Chờ (Wait) sang Sẵn sàng (Ready). Công thức tính độ ưu tiên HRN là (Chờ + Dịch vụ) / Dịch vụ, giá trị càng lớn thì độ ưu tiên càng cao.

- **1. Bảng đối chiếu Tiến trình (Process) vs Tiểu trình (Thread):**

| Tiêu chuẩn so sánh | Tiến trình (프로세스 - Process) | Tiểu trình (스레드 - Thread) |
| :--- | :--- | :--- |
| **Định nghĩa cốt lõi** | Chương trình đang được thực thi trên RAM; là **đơn vị cấp phát tài nguyên độc lập**. | Đơn vị thực thi luồng lệnh nhỏ nhất bên trong một tiến trình (Lightweight Process). |
| **Vùng nhớ chia sẻ** | Độc lập hoàn toàn; tiến trình này không truy cập được bộ nhớ của tiến trình khác. | **Chia sẻ chung không gian Code, Data, Heap** của tiến trình cha. |
| **Vùng nhớ độc lập** | Sở hữu toàn bộ không gian địa chỉ riêng. | **Chỉ sở hữu riêng biệt: Ngăn xếp (Stack) và Con trỏ lệnh (PC)**. |
| **Chi phí tạo & Chuyển đổi**| Tốn nhiều tài nguyên; chuyển ngữ cảnh (Context Switch) chậm. | **Rất nhẹ**, tạo nhanh và chuyển ngữ cảnh nhanh gấp nhiều lần. |

- **2. Bảng 4 sự kiện chuyển đổi trạng thái tiến trình (상태 전이 이벤트):**

| Sự kiện chuyển đổi | Trạng thái nguồn $\rightarrow$ đích | Nguyên nhân kích hoạt trong hệ thống |
| :--- | :---: | :--- |
| **Dispatch (Phân phối)**| **준비 (Ready) $\rightarrow$ 실행 (Running)** | Bộ lập lịch CPU (Scheduler) chọn tiến trình đầu hàng đợi để trao quyền CPU. |
| **Timeout (Hết lượt)** | **실행 (Running) $\rightarrow$ 준비 (Ready)** | Tiến trình đã dùng hết khoảng thời gian định mức (Time Quantum / Slice). |
| **Block (Chờ I/O)** | **실행 (Running) $\rightarrow$ 대기 (Wait)** | Tiến trình phát sinh yêu cầu đọc/ghi đĩa, mạng hoặc đợi tài nguyên chưa sẵn sàng. |
| **Wakeup (Đánh thức)** | **대기 (Wait) $\rightarrow$ 준비 (Ready)** | **Sự kiện I/O đã hoàn tất**; tiến trình quay lại hàng đợi sẵn sàng để chờ cấp CPU. |

- **3. Bảng phân loại các giải thuật điều phối CPU (CPU 스케줄링):**

| Nhóm giải thuật | Tên thuật toán | Cơ chế vận hành & Đặc điểm khảo thí |
| :--- | :--- | :--- |
| **Phi trưng dụng**<br>(비선점형 - Non-preemptive:<br>Không bị cướp CPU) | **FCFS** | Đến trước chạy trước (First-Come First-Served); đơn giản nhưng dễ nghẽn (Convoy Effect). |
| | **SJF** | Việc ngắn nhất chạy trước; tối ưu thời gian chờ nhưng dễ gây **bỏ đói (기아 - Starvation)** việc dài. |
| | **HRN** | Khắc phục SJF; tính ưu tiên: **$\text{Priority} = \frac{W + S}{S}$** (Chờ càng lâu ưu tiên càng cao). |
| | **우선순위 (Priority)** | Chạy theo cấp độ ưu tiên định sẵn; có thể áp dụng kỹ thuật Aging để chống đói CPU. |
| **Trưng dụng**<br>(선점형 - Preemptive:<br>HĐH có quyền cưỡng chế thu hồi CPU) | **Round Robin (RR)** | Chia đều CPU theo lát cắt thời gian (**Time Slice**); giải thuật tiêu biểu cho hệ thống tương tác. |
| | **SRT** | Phiên bản trưng dụng của SJF; tiến trình mới có thời gian còn lại ngắn hơn sẽ cướp CPU. |
| | **MLQ (다단계 큐)** | Đa hàng đợi sẵn sàng cố định; mỗi hàng đợi có mức ưu tiên và giải thuật riêng. |
| | **MFQ (다단계 피드백 큐)**| Hàng đợi phản hồi động; tiến trình dùng hết time slice bị hạ cấp xuống hàng đợi dưới. |

- **주의/함정 (Bẫy đề thi):**
  - **Wakeup không nhảy thẳng sang Running:** Đề thi khẳng định *"Khi hoàn tất I/O, tiến trình chuyển thẳng từ 대기 (Wait) sang 실행 (Running)"* $\rightarrow$ **SAI**. Tiến trình bắt buộc phải về hàng đợi **준비 (Ready)** để xếp hàng chờ cấp CPU.
  - **Khối PCB không chứa dữ liệu người dùng:** PCB chỉ lưu thông tin điều khiển quản trị (PID, trạng thái, PC, thanh ghi); không lưu trữ nội dung dữ liệu ứng dụng.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"Thread chung Code Data Heap riêng Stack PC; I/O xong về Ready đợi CPU; HRN lấy Chờ cộng Thực thi chia Thực thi."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán trắc nghiệm tính độ ưu tiên HRN chuẩn đề thi:
- **Đề bài:** Cho 3 tiến trình $A, B, C$ đang cùng nằm trong hàng đợi sẵn sàng với các thông số thời gian như sau:
  - Tiến trình $A$: Thời gian chờ ($W$) = 10, Thời gian dịch vụ ($S$) = 20.
  - Tiến trình $B$: Thời gian chờ ($W$) = 20, Thời gian dịch vụ ($S$) = 10.
  - Tiến trình $C$: Thời gian chờ ($W$) = 30, Thời gian dịch vụ ($S$) = 15.
  Hỏi theo giải thuật điều phối HRN, tiến trình nào sẽ được ưu tiên cấp CPU chạy trước tiên?

- **Phân tích thay công thức $\frac{W+S}{S}$:**
  - $\text{Priority}_A = \frac{10 + 20}{20} = \frac{30}{20} = \mathbf{1.5}$
  - $\text{Priority}_B = \frac{20 + 10}{10} = \frac{30}{10} = \mathbf{3.0}$
  - $\text{Priority}_C = \frac{30 + 15}{15} = \frac{45}{15} = \mathbf{3.0}$
- Nếu $B$ và $C$ cùng có độ ưu tiên bằng 3.0, tiến trình nào đến trước (hoặc thời gian dịch vụ ngắn hơn tùy đề bài quy định) sẽ được chạy. Trong trường hợp so sánh $A$ và $B$, tiến trình **$B$ (3.0)** có độ ưu tiên vượt trội so với **$A$ (1.5)**.

#### 2. Bài toán tính Thời gian chờ trung bình (FCFS vs SJF):
Giả sử có 3 tiến trình đến cùng thời điểm 0 với thời gian thực thi: $P_1 = 24$, $P_2 = 3$, $P_3 = 3$.

- **Thực thi theo FCFS (Thứ tự $P_1 \rightarrow P_2 \rightarrow P_3$):**
  - Thời gian chờ của $P_1 = 0$
  - Thời gian chờ của $P_2 = 24$
  - Thời gian chờ của $P_3 = 24 + 3 = 27$
  - $\text{Thời gian chờ trung bình (FCFS)} = \frac{0 + 24 + 27}{3} = \frac{51}{3} = \mathbf{17}$.

- **Thực thi theo SJF (Thứ tự ngắn nhất trước $P_2 \rightarrow P_3 \rightarrow P_1$):**
  - Thời gian chờ của $P_2 = 0$
  - Thời gian chờ của $P_3 = 3$
  - Thời gian chờ của $P_1 = 3 + 3 = 6$
  - $\text{Thời gian chờ trung bình (SJF)} = \frac{0 + 3 + 6}{3} = \frac{9}{3} = \mathbf{3}$.
  $\rightarrow$ SJF giảm thời gian chờ trung bình từ 17 xuống còn 3!

---

### 복습 체크리스트
- [ ] Phân biệt được: Thread chia sẻ Code, Data, Heap; chỉ sở hữu riêng Stack và Program Counter.
- [ ] Ghi nhớ 5 trạng thái tiến trình: 생성 $\rightarrow$ 준비 $\leftrightarrow$ 실행 $\rightarrow$ 대기 $\rightarrow$ 종료.
- [ ] Nhớ sự kiện Wakeup đưa tiến trình từ Chờ (Wait) về Sẵn sàng (Ready), không nhảy sang Running.
- [ ] Thuộc lòng công thức độ ưu tiên HRN: $\frac{W + S}{S}$.
- [ ] Phân biệt rõ: Phi trưng dụng (FCFS, SJF, HRN) vs Trưng dụng (Round Robin, SRT, MLQ, MFQ).
- [ ] Hiểu ảnh hưởng của Time Slice trong Round Robin: Quá dài thành FCFS, quá ngắn tốn phí Context Switch.
