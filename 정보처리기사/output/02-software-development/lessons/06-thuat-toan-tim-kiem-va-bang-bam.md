# 탐색 알고리즘과 해싱 (Thuật toán tìm kiếm và cấu trúc bảng băm)

## 학습 목표
- Nắm vững nguyên lý và điều kiện tiên quyết của Tìm kiếm nhị phân (`이분 검색 / Binary Search` - mảng bắt buộc phải được sắp xếp trước) và công thức số lần so sánh tối đa: $\lfloor \log_2 n \rfloor + 1$.
- Định nghĩa chuẩn xác cấu trúc Bảng băm (`해시 테이블 / Hash Table`) và mối quan hệ nhân quả giữa bộ ba thuật ngữ: Từ đồng nghĩa (`동의어 / Synonym`), Đụng độ (`충돌 / Collision`), và Tràn thùng (`오버플로 / Overflow`).
- Phân tích cơ chế và nhận diện qua đề thi 5 hàm băm kinh điển: Phép chia lấy dư (`제산법 / Division`), Bình phương lấy giữa (`제곱법 / Mid-Square`), Gấp nếp (`폴딩법 / Folding`), Phân tích chữ số (`숫자 분석법`), và Chuyển đổi cơ số (`기수 변환법`).
- So sánh hai chiến lược giải quyết xung đột và tràn thùng: Địa chỉ mở (`개방 주소법 / Open Addressing`: Thử tuyến tính, Thử bậc hai, Băm kép) và Đóng địa chỉ (`체이닝 / Chaining` - dùng danh sách liên kết).
- Nhận diện hiện tượng kết cụm (`군집화 / Clustering`) trong Thử tuyến tính và cách khắc phục bằng Băm kép hoặc Chaining.

## 핵심 키워드
- 이분 검색 (Tìm kiếm nhị phân / Binary Search / O(log n) / 정렬 필수 / ⌊log₂ n⌋ + 1)
- 해싱 (Bảng băm / Hashing / O(1) / 홈 주소 Home Address)
- 해시 테이블 용어 (버킷 Bucket, 슬롯 Slot, 동의어 Synonym, 충돌 Collision, 오버플로 Overflow)
- 해시 함수 (제산법 Division M prime, 제곱법 Mid-square, 폴딩법 Folding, 숫자 분석법)
- 충돌 해결 (개방 주소법 Open Addressing - 선형 조사법 군집화, 체이닝 Chaining)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [05-thuat-toan-sap-xep-va-do-phuc-tap.md](05-thuat-toan-sap-xep-va-do-phuc-tap.md), chúng ta đã sắp xếp dữ liệu có thứ tự tăng dần/giảm dần bằng các thuật toán tối ưu $O(n \log n)$.
- **Đang giải quyết gì (Current Problem):** Bài học này giải quyết việc tăng tốc tra cứu dữ liệu từ quét tuần tự chậm chạp $O(n)$ lên $O(\log n)$ bằng Tìm kiếm nhị phân, và đạt tới tốc độ truy xuất tức thì $O(1)$ bằng Cấu trúc Bảng băm (Hashing) cùng các giải thuật xử lý đụng độ.
- **Dùng đi đâu (Forward Handoff):** Từ các thuật toán tìm kiếm và bảng băm trên RAM, khi mở rộng quy mô lên các tệp dữ liệu đĩa cứng bền vững của doanh nghiệp, kiến thức này kết nối trực tiếp với [07-co-so-du-lieu-va-toi-uu-truy-van.md](07-co-so-du-lieu-va-toi-uu-truy-van.md) để khảo sát hệ thống cơ sở dữ liệu và tối ưu hóa truy vấn.

## 읽는 방법
- Đọc TẦNG A để nắm chắc công thức tính số bước so sánh của Binary Search ($\lfloor \log_2 n \rfloor + 1$), bảng đối chiếu 5 hàm băm và quan hệ nhân quả: nếu 1 Bucket có 1 Slot thì Collision lập tức gây ra Overflow.
- Đọc TẦNG B để hiểu sâu hiện tượng Clustering trong Linear Probing và phân biệt hai biến thể Shift Folding vs Boundary Folding.

---

## 탐색 알고리즘과 해싱

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng đối chiếu các thuật toán tìm kiếm
| Thuật toán tìm kiếm | Tên tiếng Hàn & Anh | Điều kiện tiên quyết | Độ phức tạp thời gian | Số lần so sánh tối đa |
| :--- | :--- | :--- | :---: | :---: |
| **Tìm kiếm tuần tự** | **순차 검색 (Linear)** | Dữ liệu ngẫu nhiên, không cần sắp xếp | $O(n)$ | $n$ lần |
| **Tìm kiếm nhị phân**| **이분 검색 (Binary)** | **Dữ liệu bắt buộc phải được sắp xếp trước** | $\mathbf{O(\log n)}$ | $\mathbf{\lfloor \log_2 n \rfloor + 1}$ |
| **Bảng băm** | **해싱 (Hashing)** | Sử dụng hàm băm $h(K)$ tính địa chỉ ô nhớ | $\mathbf{O(1)}$ (lý tưởng) | 1 lần (nếu không đụng độ) |

#### 2. Hệ thống thuật ngữ Bảng băm (해시 테이블)
| Thuật ngữ | Tên Hàn & Anh | Định nghĩa kỹ thuật chuẩn thi cử |
| :--- | :--- | :--- |
| **Hàm băm** | **해시 함수 (Hash Function)** | Hàm toán học biến đổi khóa $K$ thành địa chỉ ô nhớ $h(K)$ |
| **Địa chỉ gốc** | **홈 주소 (Home Address)** | Giá trị địa chỉ trả về trực tiếp từ hàm băm |
| **Thùng chứa** | **버킷 (Bucket)** | Khối lưu trữ tương ứng 1 địa chỉ băm, gồm một hoặc nhiều Slot |
| **Khe cắm** | **슬롯 (Slot)** | Ô nhớ lưu trữ đúng 1 bản ghi dữ liệu bên trong Bucket |
| **Từ đồng nghĩa** | **동의어 (Synonym)** | **Tập hợp các khóa khác nhau nhưng có cùng địa chỉ băm**: $h(K_1) = h(K_2)$ |
| **Đụng độ** | **충돌 (Collision)** | **Hiện tượng hai khóa khác nhau được ánh xạ vào cùng một Bucket** |
| **Tràn thùng** | **오버플로 (Overflow)** | Hiện tượng xảy ra khi một Bucket **không còn Slot trống nào** để chứa thêm |

#### 3. Bảng 5 hàm băm kinh điển (해싱 함수)
| Hàm băm | Tên Hàn & Anh | Cơ chế tạo địa chỉ | Điểm lưu ý thi cử |
| :--- | :--- | :--- | :--- |
| **Phép chia lấy dư** | **제산법 (Division)** | $\mathbf{h(K) = K \pmod M}$ | **$M$ bắt buộc phải là số nguyên tố (Prime Number)** |
| **Bình phương giữa** | **제곱법 (Mid-Square)** | Tính $K^2$ rồi trích chữ số ở giữa | Phá vỡ sự trùng lặp ở hai đầu của khóa |
| **Phương pháp gấp nếp**| **폴딩법 (Folding)** | Chia khóa thành từng đoạn rồi cộng lại | Gồm **Shift Folding** và **Boundary Folding** (lật đối xứng) |
| **Phân tích chữ số** | **숫자 분석법 (Digit Analysis)**| Chọn các vị trí chữ số có tần suất phân bố đều | Áp dụng cho tập khóa biết trước (như số CMND/CCCD) |
| **Chuyển đổi cơ số** | **기수 변환법 (Radix)** | Đổi khóa sang hệ cơ số khác rồi lấy địa chỉ | Phá vỡ quy luật phân bố ban đầu |

#### 4. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Điều kiện của Binary Search:** Dữ liệu **bắt buộc phải được sắp xếp trước**; nếu mảng lộn xộn thì không thể áp dụng tìm kiếm nhị phân.
- **Bẫy 2: Collision vs Overflow:**
  - Nếu Bucket có đúng 1 Slot: **Collision luôn luôn đồng thời gây ra Overflow**.
  - Nếu Bucket có nhiều Slot: Xảy ra Collision nhưng chưa chắc đã Overflow (nếu vẫn còn Slot trống).
- **Bẫy 3: Nhược điểm của Linear Probing:** Gây ra hiện tượng **군집화 (Clustering / Kết cụm)**, các bản ghi dồn cục vào các Bucket liền kề làm chậm tốc độ tìm kiếm.
- **Bẫy 4: Công thức số lần so sánh của Binary Search:** $n = 15 \rightarrow \lfloor \log_2 15 \rfloor + 1 = 3 + 1 = \mathbf{4}$ lần; $n = 1.000.000 \rightarrow$ chỉ cần tối đa **20 lần**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Cơ chế tìm kiếm nhị phân (Binary Search)
- Duy trì 2 con trỏ Đầu ($F$) và Cuối ($L$).
- Tính chỉ số giữa: $M = \lfloor (F + L) / 2 \rfloor$.
- So sánh $K$ với $A[M]$:
  - Nếu $K == A[M]$: Tìm thấy.
  - Nếu $K < A[M]$: Thu hẹp sang nửa trái $L = M - 1$.
  - Nếu $K > A[M]$: Thu hẹp sang nửa phải $F = M + 1$.
  - Khi $F > L$: Dừng, không tìm thấy khóa.

#### 2. Kỹ thuật giải quyết đụng độ và tràn thùng
- **개방 주소법 (Open Addressing):** Đi tìm Bucket trống khác trong bảng:
  - `선형 조사법 (Linear Probing)`: Thử tuần tự các ô kế tiếp: $h(K) + 1, h(K) + 2 \dots$ (dễ bị 군집화).
  - `이차 조사법 (Quadratic Probing)`: Thử theo bước nhảy bậc hai: $h(K) + 1^2, h(K) + 2^2 \dots$
  - `이중 해싱법 (Double Hashing)`: Dùng 2 hàm băm độc lập, hàm 1 xác định địa chỉ, hàm 2 xác định bước nhảy.
- **체이닝 (Chaining):** Mỗi Bucket gắn với một Danh sách liên kết (Linked List). Khi tràn, nút mới được móc nối tiếp vào đuôi danh sách của chính Bucket đó; không làm ảnh hưởng các Bucket khác.

---

### 복습 체크리스트
- [ ] Nhớ điều kiện tiên quyết của 이분 검색: Dữ liệu bắt buộc phải được sắp xếp trước.
- [ ] Tính đúng chỉ số giữa: $M = \lfloor (F + L) / 2 \rfloor$.
- [ ] Áp dụng đúng công thức số lần so sánh tối đa của Binary Search: $\lfloor \log_2 n \rfloor + 1$.
- [ ] Định nghĩa và phân biệt rõ bộ ba: 동의어 (Synonym), 충돌 (Collision), 오버플로 (Overflow).
- [ ] Khẳng định: Nếu Bucket chỉ có 1 Slot thì Collision luôn kéo theo Overflow.
- [ ] Nhớ công thức 제산법 (Division Method): $h(K) = K \pmod M$ với $M$ là số nguyên tố.
- [ ] Nhận diện 제곱법 (Mid-Square) qua thao tác tính $K^2$ rồi trích chữ số ở giữa.
- [ ] Phân biệt 이동 폴딩 (Shift) và 경계 폴딩 (Boundary) trong phương pháp 폴딩법.
- [ ] Phân biệt 개방 주소법 (Linear, Quadratic, Double Hashing) và 체이닝 (Chaining dùng Linked List).
- [ ] Nhớ nhược điểm lớn nhất của Linear Probing là hiện tượng 군집화 (Clustering).
