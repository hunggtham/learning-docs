# 086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm Bế tắc hệ thống (교착상태 - Deadlock): trạng thái hai hay nhiều tiến trình cùng chờ đợi tài nguyên do tiến trình khác nắm giữ vô thời hạn, khiến toàn bộ tiến trình bị đóng băng.
- Ghi nhớ sâu sắc 4 điều kiện tiên quyết bắt buộc phải xảy ra đồng thời để hình thành Deadlock: Loại trừ lẫn nhau (상호 배제 - Mutual Exclusion), Chiếm giữ và chờ đợi (점유와 대기 - Hold & Wait), Không tước đoạt (비선점 - Non-preemption), và Chờ đợi vòng tròn (환형 대기 - Circular Wait).
- Phân biệt rõ ràng 4 chiến lược giải quyết Deadlock kinh điển: Phòng ngừa (예방 - Prevention), Tránh né (회피 - Avoidance / Thuật toán Ngân hàng Banker's Algorithm), Phát hiện (탐지 - Detection), và Khôi phục (회복 - Recovery).

## 핵심 키워드 (Từ khóa)
- 교착상태 (Deadlock)
- 교착상태 4가지 발생 조건 (상호 배제, 점유와 대기, 비선점, 환형 대기)
- 상점비환 (Mnemonic: Mutual Exclusion, Hold & Wait, Non-preemption, Circular Wait)
- 교착상태 해결 방법 (예방, 회피, 탐지, 회복)
- 은행원 알고리즘 (Banker's Algorithm / Dijkstra / 안전 상태 Safe State)
- 자원 할당 그래프 (Resource Allocation Graph / RAG)

## 선행·연결 개념 (Kiến thức liên kết)
- [40-bai-hoc.md](40-bai-hoc.md): Lập lịch tiến trình và thuật toán HRN.
- [42-bai-hoc.md](42-bai-hoc.md): Luồng (Thread) và tổng hợp điều phối CPU.
- [39-bai-hoc.md](39-bai-hoc.md): Tiến trình, luồng và các trạng thái chuyển đổi.

## 읽는 방법 (Cách đọc)
- Học theo thần chú 4 điều kiện phát sinh Deadlock: **상·점·비·환**
  - **상 (Tương - 상호 배제 / Mutual Exclusion):** Tài nguyên chỉ cho phép duy nhất 1 tiến trình dùng tại 1 thời điểm.
  - **점 (Chiếm - 점유와 대기 / Hold & Wait):** Tiến trình đang nắm giữ ít nhất 1 tài nguyên và tiếp tục yêu cầu thêm tài nguyên mới đang bị tiến trình khác giữ.
  - **비 (Phi - 비선점 / Non-preemption):** Tài nguyên đã cấp cho tiến trình thì không ai được quyền giật lại giữa chừng.
  - **환 (Hoàn - 환형 대기 / Circular Wait):** Tồn tại một chuỗi vòng tròn khép kín các tiến trình $P_0 \rightarrow P_1 \rightarrow ... \rightarrow P_n \rightarrow P_0$ chờ nhau.
- Phân biệt 4 giải pháp xử lý Deadlock:
  - **예방 (Phòng ngừa):** Phá vỡ ít nhất 1 trong 4 điều kiện trên (hạn chế tài nguyên nghiêm ngặt, hiệu suất thấp).
  - **회피 (Tránh né):** Động lực kiểm tra trạng thái an toàn (**Safe State**) trước khi cấp phát (Thuật toán Ngân hàng Banker's Algorithm của Dijkstra).
  - **탐지 (Phát hiện):** Để mặc cho Deadlock xảy ra, định kỳ vẽ Đồ thị cấp phát tài nguyên (RAG) để tìm chu trình.
  - **회복 (Khôi phục):** Tiêu diệt tiến trình (Kill Process) hoặc tước đoạt tài nguyên để cứu hệ thống.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng 4 điều kiện tiên quyết phát sinh Deadlock (상점비환):**

| Điều kiện Deadlock | Tên tiếng Hàn & Anh | Bản chất kỹ thuật chuẩn đề thi |
| :--- | :--- | :--- |
| **1. 상호 배제** | **Mutual Exclusion (Loại trừ lẫn nhau)** | Tại một thời điểm, chỉ có **duy nhất một tiến trình** được phép sử dụng tài nguyên độc quyền (như máy in, tệp mở ghi) |
| **2. 점유와 대기** | **Hold and Wait (Chiếm giữ và chờ đợi)** | Tiến trình đã nắm giữ một số tài nguyên nhưng vẫn **tiếp tục yêu cầu thêm tài nguyên khác** và kiên quyết không nhả tài nguyên cũ ra |
| **3. 비선점** | **Non-preemption (Không tước đoạt)** | Tài nguyên đã cấp cho một tiến trình thì hệ điều hành **không được quyền cưỡng chế thu hồi**; chỉ giải phóng khi tiến trình tự nguyện |
| **4. 환형 대기** | **Circular Wait (Chờ đợi vòng tròn)** | Chuỗi tiến trình tạo thành vòng lặp: Tiến trình $A$ chờ tài nguyên của $B$, $B$ chờ $C$, và $C$ lại quay lại chờ tài nguyên của $A$ |

- **Bảng 4 phương pháp giải quyết Deadlock (교착상태 4대 해결책):**

| Phương pháp | Tên tiếng Hàn & Anh | Cơ chế hoạt động cốt lõi | Kỹ thuật / Thuật toán đại diện |
| :--- | :--- | :--- | :--- |
| **Phòng ngừa** | **예방 (Prevention)** | Can thiệp triệt để làm cho **ít nhất 1 trong 4 điều kiện (상점비환) không thể xảy ra** | Đánh số thứ tự tài nguyên, bắt buộc yêu cầu toàn bộ tài nguyên ngay từ đầu |
| **Tránh né** | **회피 (Avoidance)** | Khi có yêu cầu tài nguyên, kiểm tra xem hệ thống có giữ được **trạng thái an toàn (Safe State)** không; chỉ cấp phát khi an toàn | **은행원 알고리즘 (Banker's Algorithm)** của Dijkstra |
| **Phát hiện** | **탐지 (Detection)** | Cho phép Deadlock xảy ra tự do; định kỳ dùng thuật toán rà soát tìm chu trình bế tắc | **자원 할당 그래프 (Resource Allocation Graph - RAG)** |
| **Khôi phục** | **회복 (Recovery)** | Khi đã phát hiện Deadlock, tiến hành giải phóng ách tắc | **Tiêu diệt tiến trình (Process Termination)** hoặc Tước đoạt tài nguyên (Resource Preemption) |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Nguyên lý Thuật toán Ngân hàng (Banker's Algorithm):**
  - Giống như một ngân hàng cho khách vay tiền: Ngân hàng chỉ cho một khách vay thêm tiền nếu lượng tiền mặt dự trữ còn lại trong két sắt (Available) đủ để thỏa mãn nhu cầu tối đa của ít nhất một khách hàng khác (đảm bảo thu hồi được vốn).
  - Thuật toán duy trì các ma trận: Cần tối đa (Max), Đã cấp phát (Allocation), và Còn thiếu (Need = Max - Allocation).

### 복습 체크리스트
- [ ] Học thuộc lòng 4 điều kiện Deadlock: 상점비환 (상호 배제, 점유와 대기, 비선점, 환형 대기).
- [ ] Nhớ Deadlock chỉ xảy ra khi CẢ 4 ĐIỀU KIỆN đồng thời xuất hiện.
- [ ] Phân biệt được 4 cách giải quyết: 예방 (Prevention), 회피 (Avoidance), 탐지 (Detection), 회복 (Recovery).
- [ ] Nhớ 은행원 알고리즘 (Banker's Algorithm) thuộc về phương pháp 회피 (Avoidance).
