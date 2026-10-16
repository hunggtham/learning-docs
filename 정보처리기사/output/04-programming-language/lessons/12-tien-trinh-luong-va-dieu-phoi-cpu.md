# 프로세스, 스레드 및 CPU 스케줄링 알고리즘 (Tiến trình, Luồng & Điều phối CPU)

## 학습 목표 (Mục tiêu)
- Nắm vững sự khác nhau giữa Tiến trình (Process - không gian độc lập) và Tiểu trình (Thread - chia sẻ Code, Data, Heap), cùng các thành phần lưu trữ bên trong Khối điều khiển tiến trình (PCB - Process Control Block).
- Thấu hiểu cơ chế và chi phí chuyển ngữ cảnh (Context Switching) khi CPU chuyển giao quyền thực thi giữa các tiến trình.
- Thuộc lòng sơ đồ chuyển trạng thái tiến trình đầy đủ (생성 New, 준비 Ready, 실행 Running, 대기 Blocked, 종료 Terminated, và trạng thái tạm dừng Suspended Ready / Suspended Blocked).
- Phân biệt hai mô hình đa luồng: Luồng mức người dùng (User-level thread) và Luồng mức hạt nhân (Kernel-level thread).
- Phân biệt triệt để hai nhóm giải thuật điều phối CPU: Phi trưng dụng (비선점형: FCFS, SJF, HRN) và Trưng dụng (선점형: Round Robin, SRT, MLQ, MFQ); áp dụng thành thạo công thức ưu tiên HRN $\frac{W+S}{S}$ và tính toán thời gian chờ trung bình.

## 핵심 키워드 (Từ khóa)
- 프로세스 vs 스레드 (Process vs Thread) — Đơn vị cấp phát tài nguyên độc lập vs Đơn vị thực thi nhẹ chia sẻ bộ nhớ.
- 프로세스 제어 블록 (PCB - Process Control Block) — Khối dữ liệu kernel lưu PID, trạng thái, PC, thanh ghi, thông tin lập lịch.
- 문맥 교환 (Context Switching) — Quá trình lưu trạng thái tiến trình cũ vào PCB và nạp trạng thái tiến trình mới.
- 상태 전이 (State Transitions) — New, Ready, Running, Blocked, Terminated, Suspended Ready, Suspended Blocked.
- 사용자 수준 vs 커널 수준 스레드 (User-Level vs Kernel-Level Threads) — Thư viện luồng user space vs Hạt nhân quản lý luồng trực tiếp.
- 비선점형 스케줄링 (Non-preemptive) — FCFS, SJF (nguy cơ bỏ đói Starvation), HRN (công thức chống đói).
- 선점형 스케줄링 (Preemptive) — Round Robin (lát cắt thời gian Time Slice), SRT, MLQ, MFQ.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa từ `11-tong-quan-he-dieu-hanh-unix-linux-va-shell-script.md` khi tệp thực thi được nạp vào bộ nhớ bằng lời gọi `fork()` và `exec()`.
- **Đang giải quyết gì (Current Problem):** Giải quyết câu hỏi: Trong môi trường đa nhiệm (Multi-tasking), làm sao để CPU phân chia thời gian hợp lý cho hàng trăm tiến trình cùng lúc, tối ưu hóa năng suất và không để bất kỳ tiến trình nào bị "bỏ đói" vô hạn định (Starvation).
- **Dùng đi đâu (Forward Handoff):** Khi nhiều tiến trình cùng chạy đồng thời và cạnh tranh tài nguyên hữu hạn của hệ thống, nguy cơ xảy ra khóa chết (Deadlock) là rất cao; chuyên đề xử lý Deadlock sẽ được giải quyết ở bài `13-khoa-chet-deadlock-va-dong-bo-hoa-tien-trinh.md`.

## 읽는 방법 (Cách đọc)
- **Công thức HRN (Highest Response Ratio Next):** Bắt buộc phải thuộc lòng:
  $$\text{Độ ưu tiên} = \frac{\text{Thời gian chờ } W + \text{Thời gian thực thi } S}{S} = \frac{W + S}{S}$$
  Giá trị tính ra **càng lớn thì độ ưu tiên càng cao**, được chọn chạy trước. Công thức này giúp tiến trình dù dài đến mấy nhưng chờ lâu ($W$ lớn) vẫn sẽ được chạy, khắc phục triệt để lỗi bỏ đói của SJF.
- **Chuyển trạng thái Wakeup:** Khi thiết bị I/O xong, tiến trình từ trạng thái Chờ (**Wait/Block**) chuyển về trạng thái Sẵn sàng (**Ready**), **tuyệt đối không nhảy thẳng sang Running**.
- **User vs Kernel Thread:**
  - User-level: Không cần chuyển sang Kernel mode, tạo/chuyển siêu nhanh, nhưng nếu 1 thread gọi hàm I/O chặn (blocking I/O) thì cả tiến trình bị đình trệ.
  - Kernel-level: Hệ điều hành quản lý từng thread, tận dụng được đa lõi CPU thực sự, nhưng tốn chi phí context switch qua kernel mode.

---

## 프로세스, 스레드 및 CPU 스케줄링 알고리즘

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `스레드는 Code, Data, Heap을 공유하고 Stack과 PC만 독립적으로 갖는다. PCB는 프로세스 식별자(PID), 상태, PC, 레지스터 등을 저장하는 운영체제 제어 블록이다. I/O 완료 시 프로세스는 대기(Blocked)에서 준비(Ready) 상태로 전이된다. HRN 우선순위 공식은 (W+S)/S이며 값이 클수록 먼저 실행된다.`
  - [Tiếng Việt]: Thread chia sẻ vùng Code, Data, Heap trong tiến trình và chỉ sở hữu riêng Stack cùng Program Counter. PCB là khối cấu trúc dữ liệu của kernel lưu PID, trạng thái, PC, các thanh ghi. Khi hoàn tất I/O, tiến trình chuyển từ trạng thái Chờ (Blocked) sang Sẵn sàng (Ready). Công thức tính độ ưu tiên HRN là (Chờ + Dịch vụ) / Dịch vụ, giá trị càng lớn thì ưu tiên càng cao.

- **1. Bảng đối chiếu Tiến trình (Process) vs Tiểu trình (Thread):**

| Tiêu chuẩn so sánh | Tiến trình (프로세스 - Process) | Tiểu trình (스레드 - Thread) |
| :--- | :--- | :--- |
| **Định nghĩa cốt lõi** | Chương trình đang được thực thi trên RAM; là **đơn vị cấp phát tài nguyên độc lập**. | Đơn vị thực thi luồng lệnh nhỏ nhất bên trong một tiến trình (Lightweight Process). |
| **Vùng nhớ chia sẻ** | Độc lập hoàn toàn; tiến trình này không truy cập được bộ nhớ của tiến trình khác. | **Chia sẻ chung không gian Code, Data, Heap** của tiến trình cha. |
| **Vùng nhớ độc lập** | Sở hữu toàn bộ không gian địa chỉ riêng. | **Chỉ sở hữu riêng biệt: Ngăn xếp (Stack) và Con trỏ lệnh (PC)**. |
| **Chi phí tạo & Chuyển đổi**| Tốn nhiều tài nguyên; chuyển ngữ cảnh (Context Switch) chậm. | **Rất nhẹ**, tạo nhanh và chuyển ngữ cảnh nhanh gấp nhiều lần. |

- **2. Bảng các thành phần cấu thành Khối điều khiển tiến trình (PCB - Process Control Block):**

| Thành phần thông tin trong PCB | Ý nghĩa kỹ thuật phục vụ HĐH |
| :--- | :--- |
| **Mã định danh tiến trình (PID)** | Số nguyên duy nhất nhận diện tiến trình trong toàn hệ thống. |
| **Trạng thái tiến trình (State)** | Cho biết tiến trình đang ở trạng thái nào: New, Ready, Running, Blocked, Terminated. |
| **Bộ đếm chương trình (PC)** | Địa chỉ câu lệnh máy tiếp theo sẽ được CPU thực thi khi tiến trình được cấp quyền. |
| **Thanh ghi CPU (Registers)** | Giá trị của các thanh ghi tích lũy (Accumulator), con trỏ ngăn xếp (SP), thanh ghi chỉ số. |
| **Thông tin lập lịch (Scheduling Info)** | Mức độ ưu tiên của tiến trình, con trỏ đến các hàng đợi điều phối CPU. |
| **Thông tin quản lý bộ nhớ** | Bảng phân trang (Page Table) hoặc bảng phân đoạn xác định phạm vi bộ nhớ của tiến trình. |
| **Thông tin trạng thái vào/ra (I/O Status)**| Danh sách các tệp tin đang mở, thiết bị ngoại vi đang được gán cho tiến trình. |

- **3. Bảng phân loại các sự kiện chuyển trạng thái tiến trình (상태 전이):**

| Sự kiện chuyển đổi | Trạng thái nguồn -> đích | Nguyên nhân kích hoạt trong hệ thống |
| :--- | :---: | :--- |
| **Admit (Chấp nhận)** | **생성 (New) -> 준비 (Ready)** | Hệ điều hành khởi tạo PCB và nạp tiến trình vào hàng đợi sẵn sàng. |
| **Dispatch (Phân phối)**| **준비 (Ready) -> 실행 (Running)** | Bộ lập lịch CPU (Scheduler) chọn tiến trình đầu hàng đợi để trao quyền CPU. |
| **Timeout (Hết lượt)** | **실행 (Running) -> 준비 (Ready)** | Tiến trình đã dùng hết khoảng thời gian định mức (Time Quantum / Slice). |
| **Block (Chờ I/O)** | **실행 (Running) -> 대기 (Blocked)** | Tiến trình phát sinh yêu cầu đọc/ghi đĩa, mạng hoặc đợi tài nguyên chưa sẵn sàng. |
| **Wakeup (Đánh thức)** | **대기 (Blocked) -> 준비 (Ready)** | **Sự kiện I/O đã hoàn tất**; tiến trình quay lại hàng đợi sẵn sàng để chờ cấp CPU. |
| **Exit (Kết thúc)** | **실행 (Running) -> 종료 (Terminated)** | Tiến trình hoàn thành xong toàn bộ công việc hoặc bị cưỡng chế hủy (`kill`). |
| **Suspend (Tạm dừng)** | **준비/대기 -> 지연 준비/지연 대기** | Bộ nhớ RAM bị cạn kiệt, HĐH hoán đổi (Swap-out) tiến trình ra đĩa cứng. |

- **4. Bảng đối chiếu User-Level Thread vs Kernel-Level Thread:**

| Tiêu chí | Luồng mức người dùng (User-Level Thread) | Luồng mức hạt nhân (Kernel-Level Thread) |
| :--- | :--- | :--- |
| **Quản lý luồng** | Do thư viện người dùng (User Library) quản lý hoàn toàn. | Do chính Hạt nhân Hệ điều hành (Kernel) quản lý trực tiếp. |
| **Tốc độ chuyển đổi** | Rất nhanh vì không cần chuyển sang Kernel Mode (không System Call). | Chậm hơn vì mỗi lần chuyển luồng phải chuyển ngữ cảnh cấp Kernel. |
| **Tính đa xử lý (SMP)** | Không tận dụng được đa nhân CPU (cả tiến trình chỉ là 1 luồng trong mắt OS). | Tận dụng đa nhân tối đa; các thread chạy song song trên nhiều CPU Core. |
| **Tác động khi Block**| **Một thread bị chặn (I/O) làm toàn bộ tiến trình bị đình trệ**. | Một thread bị chặn, các thread khác trong cùng tiến trình vẫn chạy bình thường. |

- **5. Bảng phân loại các giải thuật điều phối CPU (CPU 스케줄링):**

| Nhóm giải thuật | Tên thuật toán | Cơ chế vận hành & Đặc điểm khảo thí |
| :--- | :--- | :--- |
| **Phi trưng dụng (Non-preemptive)** | **FCFS** | Đến trước chạy trước; đơn giản nhưng dễ gây nghẽn đoàn tàu (Convoy Effect). |
| **Phi trưng dụng (Non-preemptive)** | **SJF** | Việc ngắn nhất chạy trước; tối ưu thời gian chờ nhưng dễ gây **bỏ đói (Starvation)** việc dài. |
| **Phi trưng dụng (Non-preemptive)** | **HRN** | Khắc phục SJF; tính ưu tiên: **$\text{Priority} = \frac{W + S}{S}$** (Chờ càng lâu ưu tiên càng cao). |
| **Phi trưng dụng (Non-preemptive)** | **우선순위 (Priority)** | Chạy theo cấp độ ưu tiên; có thể áp dụng kỹ thuật Aging để chống đói CPU. |
| **Trưng dụng (Preemptive)** | **Round Robin (RR)** | Chia đều CPU theo lát cắt thời gian (**Time Slice**); giải thuật chuẩn cho hệ thống tương tác. |
| **Trưng dụng (Preemptive)** | **SRT** | Phiên bản trưng dụng của SJF; tiến trình mới có thời gian còn lại ngắn hơn sẽ cướp CPU. |
| **Trưng dụng (Preemptive)** | **MLQ (다단계 큐)** | Đa hàng đợi sẵn sàng cố định; mỗi hàng đợi có mức ưu tiên và giải thuật riêng. |
| **Trưng dụng (Preemptive)** | **MFQ (다단계 피드백 큐)**| Hàng đợi phản hồi động; tiến trình dùng hết time slice bị hạ cấp xuống hàng đợi dưới. |

- **주의/함정 (Bẫy đề thi):**
  - **Wakeup không nhảy thẳng sang Running:** Đề thi khẳng định *"Khi hoàn tất I/O, tiến trình chuyển thẳng từ 대기 (Wait) sang 실행 (Running)"* -> **SAI**. Tiến trình bắt buộc phải về hàng đợi **준비 (Ready)** để xếp hàng chờ cấp CPU.
  - **Khối PCB không chứa mã người dùng:** PCB chỉ lưu thông tin điều khiển quản trị (PID, trạng thái, PC, thanh ghi); không lưu trữ nội dung code hay biến của người dùng.
  - **Ngữ cảnh chuyển đổi (Context Switch):** Là khoảng thời gian CPU tạm dừng để lưu trạng thái PCB1 và khôi phục trạng thái PCB2; thời gian này là **chi phí phụ thuần túy (Overhead)**, CPU không xử lý được bất kỳ công việc hữu ích nào của người dùng.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"Thread chung Code Data Heap riêng Stack PC; I/O xong về Ready đợi CPU; HRN lấy Chờ cộng Thực thi chia Thực thi; User thread 1 con tắc cả nhà dừng."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ trạng thái tiến trình 7 trạng thái đầy đủ (Extended Process Lifecycle):
```text
  [ New (생성) ]
        |
        v (Admit)
+-------------------+   (Dispatch)   +-------------------+   (Exit)
|   Ready (준비)     | ------------> |   Running (실행)  | ---------> [ Terminated (종료) ]
|                   | <------------ |                   |
+-------------------+   (Timeout)    +-------------------+
     ^         |                          |
     |         | (Suspend)                | (I/O Request / Block)
     |         v                          v
     |   +-------------------+       +-------------------+
     |   | Suspended Ready   |       | Blocked (대기)    |
     |   | (지연 준비 - Disk)|       +-------------------+
     |   +-------------------+                 |
     |         ^                               | (Suspend)
     |         | (I/O Complete)                v
     |         +---------------------- +-------------------+
     |                                 | Suspended Blocked |
     +-------------------------------- | (지연 대기 - Disk)|
              (Swap-in)                +-------------------+
```

#### 2. Sơ đồ cơ chế Chuyển ngữ cảnh (Context Switching):
```text
Tiến trình P1 (Đang chạy)                    Tiến trình P2 (Đang đợi)
-----------------------                      -----------------------
    |
    | (Phát sinh ngắt / Hết Time Slice)
    v
Lưu trạng thái vào PCB_P1
-------------------------> [ Giai đoạn Overhead: CPU không chạy user code ]
                           Nạp trạng thái từ PCB_P2
                           ------------------------->
                                                        |
                                                        v
                                                 P2 bắt đầu chạy
```

#### 3. Bài toán trắc nghiệm tính độ ưu tiên HRN chuẩn đề thi:
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

#### 4. Bài toán tính Thời gian chờ trung bình (FCFS vs SJF):
Giả sử có 3 tiến trình đến cùng thời điểm 0 với thời gian thực thi: $P_1 = 24$, $P_2 = 3$, $P_3 = 3$.

- **Thực thi theo FCFS (Thứ tự $P_1 -> P_2 -> P_3$):**
  - Thời gian chờ của $P_1 = 0$
  - Thời gian chờ của $P_2 = 24$
  - Thời gian chờ của $P_3 = 24 + 3 = 27$
  - $\text{Thời gian chờ trung bình (FCFS)} = \frac{0 + 24 + 27}{3} = \frac{51}{3} = \mathbf{17}$.

- **Thực thi theo SJF (Thứ tự ngắn nhất trước $P_2 -> P_3 -> P_1$):**
  - Thời gian chờ của $P_2 = 0$
  - Thời gian chờ của $P_3 = 3$
  - Thời gian chờ của $P_1 = 3 + 3 = 6$
  - $\text{Thời gian chờ trung bình (SJF)} = \frac{0 + 3 + 6}{3} = \frac{9}{3} = \mathbf{3}$.
  -> SJF giảm thời gian chờ trung bình từ 17 xuống còn 3!

---

### 복습 체크리스트
- [ ] Phân biệt được: Thread chia sẻ Code, Data, Heap; chỉ sở hữu riêng Stack và Program Counter.
- [ ] Ghi nhớ các thành phần cốt lõi trong PCB: PID, State, PC, Registers, Scheduling Info, Memory Info.
- [ ] Hiểu rõ bản chất Context Switching: Chi phí overhead lưu và phục hồi PCB, không chạy code người dùng.
- [ ] Ghi nhớ sơ đồ chuyển trạng thái đầy đủ kèm trạng thái tạm dừng (Suspended Ready / Suspended Blocked).
- [ ] Nhớ sự kiện Wakeup đưa tiến trình từ Chờ (Wait/Blocked) về Sẵn sàng (Ready), không nhảy sang Running.
- [ ] Phân biệt User-level thread (nhanh nhưng 1 thread block là nghẽn cả process) và Kernel-level thread (đa nhân thực sự).
- [ ] Thuộc lòng công thức độ ưu tiên HRN: $\frac{W + S}{S}$.
- [ ] Phân biệt rõ: Phi trưng dụng (FCFS, SJF, HRN) vs Trưng dụng (Round Robin, SRT, MLQ, MFQ).
- [ ] Hiểu ảnh hưởng của Time Slice trong Round Robin: Quá dài thành FCFS, quá ngắn tốn phí Context Switch.
