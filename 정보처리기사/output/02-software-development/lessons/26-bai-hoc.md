# 029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)

## 학습 목표 (Mục tiêu)
- So sánh toàn diện ba phương pháp tìm kiếm dữ liệu kinh điển: Tìm kiếm tuần tự (순차 검색 - $O(n)$), Tìm kiếm nhị phân (이진 검색 - $O(\log n)$) và Băm dữ liệu (해싱 - $O(1)$).
- Định nghĩa khái niệm Đụng độ hàm băm (충돌 - Collision) và Tràn thùng chứa (오버플로 - Overflow) trong bảng băm (Hash Table).
- Nắm vững hai nhóm giải pháp xử lý đụng độ hàm băm: Phương pháp móc xích danh sách liên kết (체이닝 - Chaining) và Phương pháp định địa chỉ mở (개방 주소법 - Open Addressing: Tuyến tính, Bậc hai, Băm kép).

## 핵심 키워드 (Từ khóa)
- 검색 알고리즘 (Search Algorithms)
- 순차 검색 (Sequential Search: $O(n)$)
- 이진 검색 (Binary Search: $O(\log n)$)
- 해싱 (Hashing: $O(1)$ / Home Address)
- 해시 충돌 (Collision) & 오버플로 (Overflow)
- 체이닝 (Chaining / 연결 리스트 Linked List)
- 개방 주소법 (Open Addressing: 선형 탐색, 제곱 탐색, 이중 해시)

## 선행·연결 개념 (Kiến thức liên kết)
- [01-bai-hoc.md](01-bai-hoc.md): Danh sách liên kết (Linked List) hỗ trợ giải thuật Chaining.
- [25-bai-hoc.md](25-bai-hoc.md): Nguyên lý hoạt động của Tìm kiếm nhị phân (Binary Search).
- [28-bai-hoc.md](28-bai-hoc.md): Chi tiết các phương pháp xây dựng hàm băm (Division, Mid-square, Folding).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh cơ chế giải quyết đụng độ:
  - **체이닝 (Chaining):** Đụng độ thì "ở chung một xô", móc nối nhau bằng **연결 리스트 (Linked List)**.
  - **개방 주소법 (Open Addressing):** Đụng độ thì "đi tìm nhà khác" (địa chỉ bị đổi) bằng cách nhảy từng bước:
    - Nhảy liên tiếp $+1, +2 \dots \rightarrow$ **선형 탐색 (Linear Probing)**.
    - Nhảy theo bình phương $+1^2, +2^2, +3^2 \dots \rightarrow$ **제곱 탐색 (Quadratic Probing)**.
    - Dùng thêm 1 hàm băm phụ để tính bước nhảy $\rightarrow$ **이중 해시 (Double Hashing)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh 3 phương pháp tìm kiếm dữ liệu:**

| Phương pháp tìm kiếm | Tên tiếng Hàn & Anh | Yêu cầu sắp xếp dữ liệu | Độ phức tạp thời gian | Đặc trưng vận hành |
| :--- | :--- | :--- | :--- | :--- |
| **Tìm kiếm tuần tự** | **순차 검색 (Sequential Search)** | **Không cần sắp xếp** (Tùy ý) | $\mathbf{O(n)}$ | Duyệt lần lượt từng phần tử từ đầu đến cuối danh sách |
| **Tìm kiếm nhị phân** | **이진 검색 (Binary Search)** | **Bắt buộc phải sắp xếp** | $\mathbf{O(\log n)}$ | So sánh với phần tử ở giữa, mỗi lần loại bỏ 50% phạm vi |
| **Băm dữ liệu** | **해싱 (Hashing)** | Không cần sắp xếp | $\mathbf{O(1)}$ *(Lý tưởng)* | Dùng hàm băm tính trực tiếp địa chỉ vật lý từ giá trị khóa |

- **Các khái niệm cốt lõi trong Bảng băm (Hash Table):**
  - **버킷 (Bucket):** Một ô/ngăn lưu trữ trong bảng băm. Một bucket có thể chứa một hoặc nhiều khe (Slot).
  - **슬롯 (Slot):** Vị trí chứa đúng 1 bản ghi dữ liệu bên trong Bucket.
  - **충돌 (Collision):** Hiện tượng hai hoặc nhiều khóa khác nhau ($K_1 \ne K_2$) khi qua hàm băm lại cho ra **cùng một địa chỉ băm (Home Address)** ($h(K_1) = h(K_2)$).
  - **오버플로 (Overflow):** Hiện tượng xảy ra khi một khóa mới băm vào một Bucket mà **toàn bộ các Slot của Bucket đó đã bị lấp đầy hoàn toàn** (không còn chỗ trống).
  - **동의어 (Synonym):** Tập hợp các khóa tạo ra cùng một địa chỉ băm.

- **Bảng phân loại các kỹ thuật giải quyết đụng độ (Collision Resolution):**

| Nhóm phương pháp | Kỹ thuật cụ thể | Cơ chế hoạt động chi tiết |
| :--- | :--- | :--- |
| **Móc xích (Chaining)** | **체이닝 (Chaining)** | Cấp phát một **Danh sách liên kết (연결 리스트 - Linked List)** cho từng Bucket. Khi xảy ra Collision, bản ghi mới được móc thêm vào đuôi của danh sách liên kết tại chính Bucket đó |
| **Địa chỉ mở (Open Addressing)** | **선형 탐색 (Linear Probing)** | Khi Bucket bị trùng, dò tuần tự các Bucket kế tiếp ($+1, +2, +3 \dots$) cho đến khi gặp Bucket còn trống đầu tiên để lưu |
| **Địa chỉ mở (Open Addressing)** | **제곱 탐색 (Quadratic Probing)** | Dò tìm ô trống theo khoảng cách bình phương ($+1^2, +2^2, +3^2, +4^2 \dots$) để giảm thiểu hiện tượng co cụm dữ liệu (Clustering) |
| **Địa chỉ mở (Open Addressing)** | **이중 해시 (Double Hashing)** | Dùng hàm băm thứ nhất $h_1(K)$ để xác định địa chỉ ban đầu; nếu đụng độ thì dùng hàm băm thứ hai $h_2(K)$ để tính toán khoảng cách bước nhảy |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Hiện tượng Co cụm dữ liệu (Primary Clustering):**
  - Trong phương pháp **Linear Probing**, các khóa bị đụng độ liên tục có xu hướng tụ tập thành từng mảng đặc liền kề nhau trong bảng băm. Khi một chuỗi ô bị lấp đầy càng dài thì xác suất các khóa mới băm vào vùng này tiếp tục bị đụng độ càng cao $\rightarrow$ Làm suy giảm hiệu năng tìm kiếm từ $O(1)$ tụt dần về $O(n)$. Kỹ thuật **Quadratic Probing** và **Double Hashing** ra đời để khắc phục triệt để hiện tượng này.

### 복습 체크리스트
- [ ] So sánh thời gian: Tuần tự $O(n)$, Nhị phân $O(\log n)$, Hashing $O(1)$.
- [ ] Phân biệt Collision (Đụng độ địa chỉ) và Overflow (Hết slot trong bucket).
- [ ] Nhớ kỹ Chaining sử dụng danh sách liên kết (연결 리스트) để giải quyết đụng độ.
- [ ] Phân biệt 3 nhánh của Open Addressing: Linear Probing ($+1$), Quadratic Probing ($+i^2$), Double Hashing (hàm băm phụ).
