# 프로세스와 스레드 (Tiến trình & Luồng trong Hệ điều hành)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa tiến trình (Process) và các trường thông tin lưu trữ bên trong Khối điều khiển tiến trình PCB (Process Control Block).
- Làm chủ sơ đồ chuyển đổi trạng thái của tiến trình (Ready, Run, Wait, Exit) cùng các hành vi chuyển mạch: Dispatch, Timeout, Block, Wake Up.
- Hiểu rõ bản chất của kỹ thuật đệm Spooling trong việc cân bằng tốc độ CPU và thiết bị I/O.
- Phân biệt kiến trúc chia sẻ tài nguyên giữa Tiến trình (Process) và Luồng (Thread / Light Weight Process).

## 핵심 키워드 (Từ khóa)
- **프로세스 (Process)**: Chương trình đang thực thi trong bộ nhớ, đơn vị cấp phát tài nguyên của OS.
- **PCB (Process Control Block)**: Bảng thông tin định danh PID, trạng thái, thanh ghi, con trỏ bộ nhớ và tài nguyên I/O.
- **상태 전이 (State Transitions)**: Dispatch (Ready $\rightarrow$ Run), Timeout (Run $\rightarrow$ Ready), Block (Run $\rightarrow$ Wait), Wake Up (Wait $\rightarrow$ Ready).
- **스풀링 (Spooling)**: Tận dụng ổ đĩa làm đệm trung gian cho thiết bị I/O chậm (như in ấn).
- **스레드 (Thread)**: Đơn vị thực thi nhỏ nhất (LWP), chia sẻ chung Code/Data/Heap, sở hữu riêng PC/Stack.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [61-bai-hoc.md](61-bai-hoc.md) (Đặc tính hoạt động và Locality của tiến trình).
- Liên kết với [63-bai-hoc.md](63-bai-hoc.md) (Các thuật toán lập lịch CPU).
- Liên kết với [04-programming-language/74-bai-hoc.md](../../04-programming-language/lessons/74-bai-hoc.md) (Deadlock và đồng bộ hóa tiến trình).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh các thao tác chuyển trạng thái:
  - "Chuyển từ Ready sang Run (cấp phát CPU)" $\rightarrow$ **Dispatch (디스패치)**.
  - "Hoàn thành I/O, chuyển từ Wait sang Ready" $\rightarrow$ **Wake Up (웨이크 업)**.
  - "Hết thời gian CPU được cấp, quay về hàng đợi Ready" $\rightarrow$ **Timeout / Timer Run-out**.
  - Các Thread trong cùng một Process chia sẻ những gì? Chia sẻ **Code, Data, Heap**; KHÔNG chia sẻ **Stack và Register**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Tiến trình và Khối điều khiển tiến trình (PCB)
- **Định nghĩa**: Một chương trình đang được nạp vào bộ nhớ và được CPU cấp phát tài nguyên để thực thi (còn gọi là Job hoặc Task).
- **PCB (Process Control Block)**:
  - Cấu trúc dữ liệu do hệ điều hành tạo ra ngay khi tiến trình được sinh ra và giải phóng khi tiến trình kết thúc.
  - *Các trường thông tin quan trọng trong PCB*:
    - Định danh tiến trình (PID - Process ID) và PID của tiến trình cha.
    - Trạng thái hiện tại của tiến trình (Ready, Running, Waiting...).
    - Bộ đếm chương trình (Program Counter - PC): Địa chỉ của lệnh tiếp theo cần thực thi.
    - Tập thanh ghi CPU (CPU Registers): Lưu trạng thái khi bị ngắt.
    - Thông tin lập lịch CPU (Scheduling Priority, độ ưu tiên).
    - Thông tin quản lý bộ nhớ (Base/Limit registers hoặc Page Table pointer).
    - Thông tin thống kê tài khoản (Thời gian CPU đã dùng, giới hạn thời gian).
    - Trạng thái các thiết bị I/O và danh sách tệp tin đang mở.

#### 2. Sơ đồ Chuyển đổi Trạng thái Tiến trình
```
                         [Timeout (Hết lượt CPU)]
                       ┌─────────────────────────┐
                       │                         │
                       ▼     Dispatch (Cấp CPU)  │
 [Ready (Sẵn sàng)] ────────────────────────► [Running (Đang chạy)] ──► [Exit (Kết thúc)]
        ▲                                                │
        │ Wake Up (I/O xong)                             │ Block / Wait (Yêu cầu I/O)
        └───────────────── [Waiting / Block (Chờ)] ◄─────┘
```

| Tên chuyển dịch | Trạng thái nguồn $\rightarrow$ đích | Tác nhân kích hoạt |
| :--- | :--- | :--- |
| **Dispatch (디스패치)** | Ready $\rightarrow$ Running | Bộ điều độ (Scheduler) chọn tiến trình đầu hàng đợi cấp quyền chiếm giữ CPU |
| **Timeout (시간 초과)** | Running $\rightarrow$ Ready | Hết lát thời gian lượng tử (Time Quantum) trong đa nhiệm chiếm đoạt |
| **Block / Wait** | Running $\rightarrow$ Waiting | Tiến trình phát sinh yêu cầu đọc/ghi dữ liệu (I/O) hoặc đợi tín hiệu tài nguyên |
| **Wake Up (웨이크 업)** | Waiting $\rightarrow$ Ready | Thao tác I/O ngoại vi hoàn thành hoặc sự kiện chờ đợi xảy ra |

#### 3. Phân biệt Tiến trình (Process) vs Luồng (Thread)
| Tiêu chí so sánh | Tiến trình (Process) | Luồng (Thread / LWP) |
| :--- | :--- | :--- |
| **Khái niệm** | Đơn vị độc lập sở hữu tài nguyên hệ thống do OS cấp phát | Đơn vị thực thi công việc nhỏ nhất bên trong một tiến trình |
| **Không gian địa chỉ** | Mỗi tiến trình có một không gian bộ nhớ ảo hoàn toàn độc lập | Các luồng trong cùng tiến trình **chia sẻ chung Code, Data, Heap** |
| **Thành phần sở hữu riêng** | PCB riêng, bảng trang riêng, tệp mở riêng | Chỉ sở hữu riêng: **Program Counter (PC), Registers, Stack** |
| **Chi phí chuyển cảnh (Context Switch)** | **Rất cao** (phải nạp lại bảng trang, xả cache TLB) | **Rất thấp** (chỉ cần đổi thanh ghi và con trỏ ngăn xếp Stack) |
| **Mức độ ảnh hưởng lỗi** | 1 tiến trình sập không ảnh hưởng tới tiến trình khác | 1 luồng gặp lỗi bộ nhớ (Crash) có thể làm **sập toàn bộ tiến trình** |

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Kỹ thuật Spooling (Simultaneous Peripheral Operation On-Line)
- **Bản chất**: Việc sử dụng bộ nhớ ngoài (ổ đĩa cứng) làm một bộ đệm trung gian lưu trữ hàng đợi công việc trước khi chuyển đến thiết bị I/O tốc độ chậm.
- **Ví dụ kinh điển (Print Spooler)**: Khi một ứng dụng in một tài liệu 500 trang, CPU không phải ngồi đợi máy in in từng trang một. Toàn bộ lệnh in được ghi nhanh xuống đĩa cứng (Spool file), sau đó một tiến trình chạy ngầm sẽ đẩy dần dữ liệu cho máy in, giải phóng CPU ngay lập tức để làm việc khác.

---

### 복습 체크리스트
- [ ] Khối điều khiển tiến trình PCB được tạo ra và hủy bỏ tại những thời điểm nào?
- [ ] Thao tác Dispatch (디스패치) thực hiện việc chuyển đổi trạng thái nào của tiến trình?
- [ ] Các Thread trong cùng một Process chia sẻ chung những vùng nhớ nào và sở hữu riêng những thành phần nào?
- [ ] Kỹ thuật Spooling giải quyết bài toán chênh lệch tốc độ giữa những thành phần phần cứng nào?
