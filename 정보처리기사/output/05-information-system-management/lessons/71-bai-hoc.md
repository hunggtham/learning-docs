# 교착상태 (Deadlock - Hiện tượng Bế tắc Hệ thống)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và bản chất của hiện tượng bế tắc (교착상태 - Deadlock) trong hệ thống đa nhiệm.
- Thuộc lòng 4 điều kiện cần và đủ để phát sinh Deadlock (상점비환: 상호 배제, 점유와 대기, 비선점, 환형 대기).
- Phân biệt 4 chiến lược giải quyết Deadlock trong hệ điều hành: Phòng ngừa (예방), Né tránh (회피), Phát hiện (발견), và Phục hồi (회복).
- Hiểu rõ nguyên lý hoạt động của Thuật toán người chia tiền (은행원 알고리즘 - Banker's Algorithm) trong việc duy trì trạng thái an toàn (Safe State).

## 핵심 키워드 (Từ khóa)
- **교착상태 (Deadlock)**: Các tiến trình cùng chờ đợi tài nguyên của nhau vô hạn định.
- **4대 발생 조건 (Coffman Conditions)**: 상호 배제 (Mutual Exclusion), 점유와 대기 (Hold & Wait), 비선점 (Non-preemption), 환형 대기 (Circular Wait). Mẹo nhớ: **상-점-비-환**.
- **4대 해결 기법**: 예방 (Prevention - loại bỏ 1 trong 4 điều kiện), 회피 (Avoidance - Banker's Algorithm), 발견 (Detection - đồ thị RAG), 회복 (Recovery - hủy tiến trình, thu hồi tài nguyên).
- **안전 상태 (Safe State)**: Tồn tại ít nhất một chuỗi an toàn (Safe Sequence) đảm bảo mọi tiến trình đều có thể hoàn thành.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [62-bai-hoc.md](62-bai-hoc.md) (Tiến trình và các trạng thái Ready, Block).
- Liên kết với [70-bai-hoc.md](70-bai-hoc.md) (Kiểm soát đồng thời và khóa trong cơ sở dữ liệu).
- Liên kết với [04-programming-language/74-bai-hoc.md](../../04-programming-language/lessons/74-bai-hoc.md) (Các thuật toán tương hỗ loại trừ Dekker, Peterson, Semaphore).

## 읽는 방법 (Cách đọc)
- Đi thi chú ý nhận diện nhanh:
  - 4 điều kiện: Nhớ ngay câu thần chú **상 - 점 - 비 - 환** (Mutual Exclusion - Hold & Wait - Non-preemption - Circular Wait).
  - Thuật toán né tránh bế tắc kinh điển: Cứ thấy từ khóa "Banker's Algorithm" hoặc "은행원 알고리즘" $\rightarrow$ Chọn phương pháp **회피 (Avoidance)**.
  - Phương pháp gây lãng phí tài nguyên nhất: **예방 (Prevention)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bốn điều kiện phát sinh Deadlock (Coffman Conditions)
Deadlock chỉ có thể xảy ra khi và chỉ khi **đồng thời cả 4 điều kiện** sau đây cùng được thỏa mãn:
| Điều kiện (KR / EN) | Khái niệm kỹ thuật bản chất | Cách thức phá bỏ điều kiện (Prevention) |
| :--- | :--- | :--- |
| **상호 배제 / (Mutual Exclusion)** | Tài nguyên có tính chất độc quyền, tại một thời điểm chỉ cho phép duy nhất một tiến trình sử dụng | Chia sẻ tài nguyên cho nhiều tiến trình cùng đọc (chỉ áp dụng được với tài nguyên Read-only như file đọc) |
| **점유와 대기 / (Hold and Wait)** | Tiến trình đang nắm giữ ít nhất một tài nguyên và tiếp tục yêu cầu thêm tài nguyên mới đang bị tiến trình khác chiếm giữ | Bắt buộc tiến trình phải xin cấp phát toàn bộ mọi tài nguyên cần thiết cùng một lúc ngay từ đầu |
| **비선점 / (Non-preemption)** | Tài nguyên đã cấp phát cho một tiến trình thì không thể bị hệ điều hành cưỡng chế thu hồi; chỉ được giải phóng khi tiến trình tự nguyện nhả | Nếu tiến trình xin thêm tài nguyên mà bị từ chối, hệ điều hành lập tức thu hồi mọi tài nguyên nó đang nắm giữ |
| **환형 대기 / (Circular Wait)** | Tồn tại một chuỗi các tiến trình chờ đợi lẫn nhau tạo thành một vòng tròn khép kín ($P_0 \rightarrow P_1 \rightarrow \dots \rightarrow P_n \rightarrow P_0$) | Đánh số thứ tự duy nhất cho tất cả các tài nguyên trong hệ thống và bắt buộc tiến trình chỉ được xin cấp phát theo thứ tự tăng dần |

#### 2. Bốn chiến lược giải quyết Deadlock
- **1. 예방 (Prevention - Phòng ngừa)**:
  - Chủ động thiết kế hệ thống sao cho triệt tiêu ít nhất 1 trong 4 điều kiện phát sinh Deadlock.
  - *Đánh giá*: Làm giảm nghiêm trọng hiệu suất sử dụng thiết bị và gây lãng phí tài nguyên lớn nhất trong 4 phương pháp.
- **2. 회피 (Avoidance - Né tránh)**:
  - Hệ thống theo dõi liên tục trạng thái cấp phát tài nguyên động. Khi có yêu cầu cấp phát mới, hệ điều hành chỉ đồng ý cấp phát nếu trạng thái sau đó vẫn là **Trạng thái an toàn (Safe State)**.
  - **Thuật toán người chia tiền (Banker's Algorithm - Dijkstra)**: Thuật toán né tránh kinh điển, mô phỏng hoạt động của một ngân hàng luôn giữ lại đủ lượng tiền mặt dự trữ để đáp ứng nhu cầu tối đa của ít nhất một khách hàng.
- **3. 발견 (Detection - Phát hiện)**:
  - Cho phép Deadlock xảy ra tự nhiên, định kỳ hệ điều hành chạy thuật toán kiểm tra chu trình trên Đồ thị cấp phát tài nguyên (**RAG - Resource Allocation Graph**). Nếu phát hiện chu trình đóng kín (Cycle) thì kết luận có Deadlock.
- **4. 회복 (Recovery - Phục hồi)**:
  - Tiến hành giải tỏa Deadlock sau khi đã phát hiện, bằng một trong hai cách:
    - *Hủy tiến trình (Process Termination)*: Buộc dừng tất cả các tiến trình trong vòng bế tắc, hoặc hủy lần lượt từng tiến trình theo thứ tự ưu tiên cho đến khi hết Deadlock.
    - *Thu hồi tài nguyên (Resource Preemption)*: Cưỡng chế lấy lại tài nguyên từ một tiến trình nạn nhân (Victim) và Rollback tiến trình đó về trạng thái an toàn trước đó.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ minh họa chu trình bế tắc 환형 대기 (Circular Wait)
```
          ┌──────────────────────────────────────┐
          ▼                                      │
     [Tiến trình P1] ──(Đang giữ)──► [Tài nguyên R1]
            │                                    ▲
            │ (Đang chờ)                         │ (Đang giữ)
            ▼                                    │
     [Tài nguyên R2] ◄──(Đang chờ)── [Tiến trình P2]
```
- $P_1$ giữ $R_1$ và đợi $R_2$. Trong khi đó $P_2$ giữ $R_2$ và đợi $R_1$. Cả hai tiến trình đều không thể tiến thêm một bước nào $\rightarrow$ Bế tắc vĩnh viễn!

---

### 복습 체크리스트
- [ ] Kể tên 4 điều kiện cần và đủ để phát sinh Deadlock theo câu thần chú 상-점-비-환?
- [ ] Phá bỏ điều kiện 환형 대기 (Circular Wait) trong chiến lược Phòng ngừa bằng kỹ thuật nào?
- [ ] Thuật toán Banker's Algorithm thuộc chiến lược giải quyết Deadlock nào (Phòng ngừa, Né tránh, Phát hiện hay Phục hồi)?
- [ ] Trạng thái an toàn (Safe State) trong hệ điều hành được định nghĩa như thế nào?
