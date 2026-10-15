# 교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm Bế tắc (교착상태 - Deadlock) và 4 điều kiện cần và đủ bắt buộc phải xảy ra đồng thời để tạo nên bế tắc theo khẩu quyết **상점비환**.
- Hiểu sâu sắc điều kiện tiên quyết đầu tiên: Tính tương hỗ loại trừ (상호 배제 - Mutual Exclusion) trong việc bảo vệ miền găng (임계 구역 - Critical Section).
- Phân biệt các giải thuật kinh điển giải quyết tương hỗ loại trừ bằng phần mềm: Dekker, Peterson, Lamport Bakery và cơ chế đồng bộ Semaphore ($P/V$ Operations).

## 핵심 키워드 (Từ khóa)
- 교착상태 (Deadlock)
- 상호 배제 (Mutual Exclusion)
- 점유와 대기 (Hold and Wait)
- 비선점 (Non-preemption)
- 환형 대기 (Circular Wait)
- 임계 구역 (Critical Section)
- 데커 알고리즘 (Dekker's Algorithm)
- 피터슨 알고리즘 (Peterson's Algorithm)
- 램포트 베이커리 (Lamport's Bakery Algorithm)
- 세마포어 (Semaphore: P연산, V연산)
- 암기 공식 (상점비환)

## 선행·연결 개념 (Kiến thức liên kết)
- [73-bai-hoc.md](73-bai-hoc.md): Thuật toán thay thế trang nhớ và hiện tượng Thrashing.
- [75-bai-hoc.md](75-bai-hoc.md): Tổng hợp các kỹ thuật cơ sở phần mềm ứng dụng.
- [41-bai-hoc.md](41-bai-hoc.md): Tổng quan 4 điều kiện bế tắc và các chiến lược xử lý (예방, 회피, 탐지, 회복).

## 읽는 방법 (Cách đọc)
- Trong bài thi kỹ sư CNTT:
  - 4 điều kiện cần của Deadlock bắt buộc phải thuộc: **상·점·비·환** (상호배제, 점유와 대기, 비선점, 환형 대기).
  - Về các giải thuật Mutual Exclusion cho miền găng:
    - **Dekker:** Giải pháp phần mềm đầu tiên giải quyết tương hỗ loại trừ cho 2 tiến trình.
    - **Peterson:** Tối ưu hóa Dekker, dùng cờ và nhường lượt cho tiến trình kia chạy trước.
    - **Lamport Bakery:** Mở rộng cho **$N$ tiến trình** dựa trên mô hình phát số thứ tự như tiệm bánh mì.
    - **Semaphore:** Dùng biến nguyên với thao tác **$P$ (Wait / giảm đếm)** và **$V$ (Signal / tăng đếm)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. 4 điều kiện cần và đủ để phát sinh bế tắc (Deadlock - 상점비환):**

| Điều kiện | Tên tiếng Hàn & Anh | Bản chất kỹ thuật |
| :--- | :--- | :--- |
| **1. Tương hỗ loại trừ** | **상호 배제** (Mutual Exclusion) | Tại một thời điểm, tài nguyên chỉ có thể được sở hữu và sử dụng bởi **duy nhất một tiến trình**; tiến trình khác muốn dùng phải đợi. |
| **2. Chiếm giữ và chờ** | **점유와 대기** (Hold and Wait) | Tiến trình đang nắm giữ ít nhất một tài nguyên nhưng lại yêu cầu cấp phát thêm tài nguyên khác mà tài nguyên đó đang bị tiến trình khác chiếm. |
| **3. Không thể trưng dụng** | **비선점** (Non-preemption) | Tài nguyên đã cấp cho một tiến trình không thể bị hệ điều hành hay tiến trình khác cưỡng chế lấy lại; chỉ được nhả ra khi tiến trình sở hữu tự nguyện giải phóng. |
| **4. Chờ đợi vòng tròn** | **환형 대기** (Circular Wait) | Tồn tại một chuỗi các tiến trình chờ đợi lẫn nhau theo vòng tròn khép kín ($P_0$ chờ $P_1$, $P_1$ chờ $P_2$, ..., $P_n$ chờ lại $P_0$). |

- **2. Bảng phân loại các giải thuật tương hỗ loại trừ (Mutual Exclusion):**

| Tên giải thuật | Số lượng tiến trình | Cơ chế kỹ thuật chủ đạo |
| :--- | :---: | :--- |
| **데커 (Dekker)** | 2 tiến trình | Giải thuật phần mềm đầu tiên; kết hợp cờ trạng thái (`flag`) và biến lượt ưu tiên (`turn`) để tránh xung đột nhưng logic khá phức tạp. |
| **피터슨 (Peterson)** | 2 tiến trình | Đơn giản hóa Dekker; khi muốn vào miền găng, tiến trình bật cờ muốn vào và chủ động **gán lượt cho tiến trình còn lại** (`turn = other`). |
| **램포트 베이커리 (Lamport Bakery)** | **$N$ tiến trình** | Mô phỏng quầy bán bánh mì: Mỗi tiến trình đến cửa miền găng sẽ rút một vé số thứ tự; tiến trình có số vé nhỏ nhất sẽ được quyền vào trước. |
| **세마포어 (Semaphore - Dijkstra)** | Đa tiến trình | Cơ chế đồng bộ hóa hệ thống sử dụng biến nguyên đếm tài nguyên $S$ với hai hàm nguyên tử: **$P(S)$ (Wait):** Nếu $S \le 0$ thì chờ, ngược lại $S = S - 1$; **$V(S)$ (Signal):** $S = S + 1$ và đánh thức tiến trình đang chờ. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **3 yêu cầu bắt buộc đối với một giải pháp Miền găng (Critical Section Requirements):**
  1. **상호 배제 (Mutual Exclusion):** Không thể có từ 2 tiến trình cùng ở trong miền găng tại một thời điểm.
  2. **진행 (Progress):** Nếu không có tiến trình nào trong miền găng, việc quyết định ai được vào kế tiếp không được bị hoãn vô hạn.
  3. **유한 대기 (Bounded Waiting):** Mỗi tiến trình chỉ phải đợi một số lần hữu hạn trước khi được cấp quyền vào miền găng, không bị bỏ đói (Starvation).

### 복습 체크리스트
- [ ] Thuộc lòng 4 điều kiện cần của bế tắc: **상점비환** (상호배제, 점유와 대기, 비선점, 환형 대기).
- [ ] Nhớ Dekker và Peterson áp dụng cho 2 tiến trình, Lamport Bakery áp dụng cho $N$ tiến trình.
- [ ] Nắm vững hai thao tác của Semaphore: $P(S)$ là trừ và đợi, $V(S)$ là cộng và báo hiệu.
- [ ] Kể tên 3 yêu cầu của giải pháp miền găng: Tương hỗ loại trừ, Tiến triển (Progress), và Đợi hữu hạn (Bounded Waiting).
