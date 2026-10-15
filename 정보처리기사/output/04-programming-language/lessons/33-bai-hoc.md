# 운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)

## 학습 목표 (Mục tiêu)
- Nắm vững 3 chiến lược nạp bộ nhớ chính (기억장치 배치 전략): Nạp vị trí đầu tiên đủ lớn (First Fit - 최초 적합), Nạp vị trí vừa khít nhất (Best Fit - 최적 적합), và Nạp vị trí rộng nhất (Worst Fit - 최악 적합).
- Hiểu rõ hiện tượng quá tải hoán đổi bộ nhớ (스래싱 - Thrashing): nguyên nhân phát sinh khi thời gian hoán đổi trang lớn hơn thời gian thực thi của CPU và các giải pháp khắc phục.
- Nắm vững chu trình 5 trạng thái cơ bản của tiến trình: Sẵn sàng (준비 - Ready) $\rightarrow$ Đang chạy (실행 - Running) $\rightarrow$ Chờ đợi (대기 - Wait/Block).
- Nắm chắc thuật toán lập lịch SJF (Shortest Job First) và công thức tính độ ưu tiên của thuật toán HRN (Highest Response-ratio Next).

## 핵심 키워드 (Từ khóa)
- 기억장치 배치 전략 (First Fit, Best Fit, Worst Fit)
- 단편화 (Fragmentation / 내부 vs 외부 단편화)
- 스래싱 (Thrashing / 페이지 부재 빈발 / CPU 이용률 급감)
- 프로세스 상태 전이 (Process State Transitions / Ready, Run, Wait)
- SJF 스케줄링 (Shortest Job First / 기아 상태 발생 가능)
- HRN 스케줄링 (Highest Response-ratio Next / 우선순위 공식)

## 선행·연결 개념 (Kiến thức liên kết)
- [32-bai-hoc.md](32-bai-hoc.md): Đặc trưng hệ điều hành UNIX và lệnh `fork`.
- [34-bai-hoc.md](34-bai-hoc.md): Chức năng hệ điều hành và cấu trúc Shell / Kernel.
- [37-bai-hoc.md](37-bai-hoc.md): Chi tiết các bài toán tính toán chiến lược nạp bộ nhớ.

## 읽는 방법 (Cách đọc)
- Ghi nhớ công thức tính độ ưu tiên của giải thuật HRN (Thường xuyên có câu hỏi tính toán trong đề thi):
  $$\mathbf{\text{우선순위 (Priority)}} = \frac{\text{대기 시간 (Thời gian chờ)} + \text{서비스 시간 (Thời gian chạy)}}{\text{서비스 시간 (Thời gian chạy)}} = \frac{W + S}{S} = 1 + \frac{W}{S}$$
  - **Ý nghĩa:** Tiến trình nào có thời gian chờ đợi $W$ càng lâu thì giá trị độ ưu tiên càng lớn và sẽ được CPU phục vụ trước.
  - **Mục đích:** Khắc phục nhược điểm "Chết đói" (Starvation / 기아 현상) của giải thuật SJF (trong SJF, các tiến trình dài cứ phải nhường đường mãi cho các tiến trình ngắn mới đến).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng 3 chiến lược nạp khối nhớ (Memory Placement Strategies):**

| Chiến lược | Tên tiếng Hàn & Anh | Cơ chế tìm kiếm vùng nhớ trống | Ưu điểm & Nhược điểm |
| :--- | :--- | :--- | :--- |
| **First Fit** | **최초 적합** | Duyệt từ đầu bộ nhớ, nạp ngay vào **vùng trống đầu tiên** có kích thước đủ lớn | **Tốc độ tìm kiếm nhanh nhất**; có thể gây lãng phí ở phần đuôi |
| **Best Fit** | **최적 적합** | Quét toàn bộ bộ nhớ, chọn vùng trống có kích thước **vừa khít nhất** (chênh lệch nhỏ nhất) | Giảm thiểu phân mảnh ngoại vi; **tốn thời gian duyệt toàn bộ** danh sách ô trống |
| **Worst Fit** | **최악 적합** | Quét toàn bộ bộ nhớ, nạp vào **vùng trống có kích thước LỚN NHẤT** | Chừa lại khoảng trống còn lại tương đối lớn để tiến trình khác dùng tiếp |

- **Bảng so sánh hai giải thuật lập lịch bất khả xâm phạm (Non-preemptive):**

| Giải thuật | Cơ sở lựa chọn CPU | Ưu điểm cốt lõi | Nhược điểm (Bẫy đề thi) |
| :--- | :--- | :--- | :--- |
| **SJF (Shortest Job First)** | Ưu tiên tiến trình có **thời gian thực thi ngắn nhất (Burst time nhỏ nhất)** | Giảm thời gian chờ trung bình (Average Waiting Time) xuống mức tối thiểu | **Hiện tượng đói tài nguyên (기아 현상 - Starvation)** đối với các tiến trình có thời gian chạy dài |
| **HRN (Highest Response-ratio Next)** | Tính toán chỉ số ưu tiên $\frac{W + S}{S}$; **chỉ số lớn nhất được chạy trước** | **Ngăn ngừa hiện tượng Starvation**; vừa ưu tiên việc ngắn vừa đền bù cho việc chờ lâu | Tốn chi phí CPU tính toán lại tỷ lệ đáp ứng trước mỗi lượt điều phối |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bài toán thi mẫu tính độ ưu tiên HRN:**
  - *Đề bài:* Có 3 tiến trình A, B, C với thời gian chờ ($W$) và thời gian dịch vụ ($S$) như sau:
    - Tiến trình A: $W = 10, S = 20 \rightarrow \text{Priority} = \frac{10 + 20}{20} = 1.5$.
    - Tiến trình B: $W = 20, S = 10 \rightarrow \text{Priority} = \frac{20 + 10}{10} = 3.0$.
    - Tiến trình C: $W = 15, S = 5 \rightarrow \text{Priority} = \frac{15 + 5}{5} = 4.0$.
  - *Thứ tự thực thi:* Do $4.0 > 3.0 > 1.5$, thứ tự cấp phát CPU là: **C $\rightarrow$ B $\rightarrow$ A**.

### 복습 체크리스트
- [ ] Phân biệt được First Fit (nhanh nhất), Best Fit (vừa khít nhất), Worst Fit (rộng nhất).
- [ ] Nhớ công thức HRN: $(W + S) / S$ (Chỉ số càng cao càng được ưu tiên chạy trước).
- [ ] Nhớ HRN ra đời để khắc phục nhược điểm 기아 현상 (Starvation) của SJF.
- [ ] Nhớ định nghĩa Thrashing: Thời gian hoán đổi trang (Page Swapping) lớn hơn thời gian chạy thực tế của CPU.
