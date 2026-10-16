# 탐색 알고리즘과 해싱 (Thuật toán tìm kiếm và cấu trúc bảng băm)

## 학습 목표
- So sánh đối đầu giữa Tìm kiếm tuần tự (`순차 검색 / Linear Search` - $O(n)$, không cần sắp xếp) và Tìm kiếm nhị phân (`이분 검색 / Binary Search` - $O(\log n)$, bắt buộc mảng phải sắp xếp).
- Áp dụng thành thạo công thức tính số lần so sánh tối đa của Tìm kiếm nhị phân trong trường hợp xấu nhất: $\lfloor \log_2 n \rfloor + 1$.
- Nắm vững cấu trúc giải phẫu của Bảng băm (`해시 테이블 / Hash Table`): Xô (`버킷 / Bucket`), Khe cắm (`슬롯 / Slot`), Địa chỉ gốc (`홈 주소 / Home Address`), và mối quan hệ giữa Đồng nghĩa (`동의어 / Synonym`) $\rightarrow$ Xung đột (`충돌 / Collision`) $\rightarrow$ Tràn xô (`오버플로 / Overflow`).
- Nắm vững nguyên lý toán học của 5 hàm băm kinh điển: Phép chia lấy dư (`제산법 / Division`), Bình phương giữa (`제곱법 / Mid-square`), Gấp nếp (`폴딩법 / Folding`), Chuyển cơ số (`기수 변환법 / Radix`), và Phân tích chữ số (`숫자 분석법 / Digit Analysis`).
- Phân biệt 2 chiến lược giải quyết xung đột: Định địa chỉ mở (`개방 주소법 / Open Addressing` - Dò tuyến tính, Dò bậc hai, Băm kép) và Nối kết danh sách (`체이닝 / Chaining` - dùng con trỏ danh sách liên kết).

## 핵심 키워드
- 이분 검색 (Tìm kiếm nhị phân / Binary Search / $O(\log n)$ / $\lfloor \log_2 n \rfloor + 1$)
- 해싱 & 해시 함수 (Hashing & Hash Function / $O(1)$)
- 버킷 & 슬롯 (Bucket & Slot / Hash Table Cấu trúc)
- 동의어 & 충돌 & 오버플로 (Synonym, Collision, Overflow)
- 5대 해시 함수 (제산법 Division, 제곱법 Mid-square, 폴딩법 Folding, 기수 변환법 Radix, 숫자 분석법)
- 충돌 해결 기법 (개방 주소법 Open Addressing - 선형 조사, 이차 조사 vs 체이닝 Chaining)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [05-thuat-toan-sap-xep-va-do-phuc-tap.md](05-thuat-toan-sap-xep-va-do-phuc-tap.md), dữ liệu đã được sắp xếp trật tự, tạo tiền đề để áp dụng các thuật toán tìm kiếm tốc độ cao.
- **Đang giải quyết gì (Current Problem):** Tìm kiếm tuần tự quá chậm trên tập dữ liệu lớn ($O(n)$). Bài học này giải quyết việc tăng tốc độ tra cứu lên $O(\log n)$ bằng Tìm kiếm nhị phân và tiệm cận $O(1)$ tức thời bằng Cấu trúc Bảng băm.
- **Dùng đi đâu (Forward Handoff):** Sau khi hoàn thành toàn bộ các cấu trúc dữ liệu và giải thuật trong RAM, bài học tiếp theo [07-co-so-du-lieu-va-toi-uu-truy-van.md](07-co-so-du-lieu-va-toi-uu-truy-van.md) sẽ đưa người học sang không gian lưu trữ CSDL bền vững.

## 읽는 방법
- Đọc TẦNG A để thuộc lòng công thức tính số bước so sánh nhị phân, bảng 5 hàm băm, bảng đối chiếu Open Addressing vs Chaining và các bẫy trắc nghiệm.
- Đọc TẦNG B để xem sơ đồ ASCII giải phẫu Bucket/Slot, cơ chế nhân quả Synonym $\rightarrow$ Collision $\rightarrow$ Overflow và chi tiết từng phương pháp dò địa chỉ mở.

---

## 탐색 알고리즘과 해싱

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Đối chiếu Linear Search vs Binary Search
| Tiêu chí | 순차 검색 (Linear Search) | 이분 검색 (Binary Search) |
| :--- | :--- | :--- |
| **Yêu cầu dữ liệu** | **Không cần sắp xếp trước** | **Bắt buộc phải được sắp xếp trước** |
| **Độ phức tạp thời gian** | $O(n)$ (Số lần so sánh trung bình: $\frac{n+1}{2}$) | $\mathbf{O(\log n)}$ |
| **Công thức so sánh tối đa** | $n$ lần | $\mathbf{\lfloor \log_2 n \rfloor + 1}$ |
| **Ví dụ: $n = 15$ phần tử** | Tối đa 15 lần | Tối đa: $\lfloor \log_2 15 \rfloor + 1 = 3 + 1 = \mathbf{4}$ lần |
| **Ví dụ: $n = 1.000.000$ bản ghi** | Tối đa 1.000.000 lần | Tối đa: $\lfloor \log_2 1.000.000 \rfloor + 1 = \mathbf{20}$ lần |

#### 2. Bảng 5 hàm băm (Hash Functions) kinh điển trong đề thi
| Tên hàm băm | Tên tiếng Hàn | Nguyên lý hoạt động toán học | Trường hợp áp dụng |
| :--- | :--- | :--- | :--- |
| **Phép chia lấy dư** | **제산법 (Division)** | Lấy khóa chia cho số nguyên tố $p$ (sát kích thước bảng), lấy phần dư làm địa chỉ: $h(K) = K \bmod p$ | Phổ biến nhất, dễ cài đặt |
| **Bình phương giữa** | **제곱법 (Mid-Square)** | Bình phương giá trị khóa ($K^2$), sau đó trích xuất các chữ số ở chính giữa làm địa chỉ | Khóa có nhiều chữ số |
| **Gấp nếp** | **폴딩법 (Folding)** | Chia khóa thành nhiều đoạn có độ dài bằng địa chỉ, rồi cộng (hoặc XOR) các đoạn lại (Shift fold / Boundary fold) | Khóa có độ dài rất lớn |
| **Chuyển đổi cơ số** | **기수 변환법 (Radix)** | Coi khóa như một số ở hệ cơ số khác rồi đổi sang hệ cơ số của bảng băm | Khóa chứa ký tự đặc biệt |
| **Phân tích chữ số** | **숫자 분석법 (Digit Analysis)** | Phân tích phân bố các chữ số của khóa, loại bỏ các vị trí hay trùng lặp, chọn các vị trí có độ ngẫu nhiên cao | Biết trước phân bố tập khóa |

#### 3. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Điều kiện tiên quyết của Binary Search:** Bắt buộc dữ liệu phải được **sắp xếp có thứ tự từ trước (정렬)**. Nếu dữ liệu xáo trộn, Binary Search không thể hoạt động.
- **Bẫy 2: Quan hệ nhân quả Synonym - Collision - Overflow:**
  - Hai khóa khác nhau cho ra cùng Home Address $\rightarrow$ Gọi là **동의어 (Synonym)**.
  - Hiện tượng hai khóa tranh chấp cùng 1 Bucket $\rightarrow$ Gọi là **충돌 (Collision)**.
  - Khi Collision xảy ra mà Bucket đã **hết sạch Slot trống** $\rightarrow$ Dẫn đến **오버플로 (Overflow)**.
- **Bẫy 3: Đánh giá Chaining vs Open Addressing:** Chaining dùng con trỏ liên kết nên **không bị giới hạn dung lượng bảng và không gây tràn bảng ảo**, nhưng tốn thêm vùng nhớ lưu con trỏ.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ giải phẫu cấu trúc Bảng băm (Hash Table Structure)
```
+--------------------------------------------------------+
| HASH TABLE                                             |
|                                                        |
| Bucket 0: [ Slot 1: Data A ] [ Slot 2: Empty  ]        |
| Bucket 1: [ Slot 1: Data B ] [ Slot 2: Data C ] (FULL) | <-- Tràn nếu có khóa mới băm vào đây!
| Bucket 2: [ Slot 1: Empty  ] [ Slot 2: Empty  ]        |
+--------------------------------------------------------+
```
- **버킷 (Bucket):** Một khối ô nhớ có cùng một địa chỉ băm (Home Address). Một bảng băm gồm nhiều Bucket.
- **슬롯 (Slot):** Vị trí chứa từng bản ghi dữ liệu bên trong một Bucket. Nếu 1 Bucket có $k$ Slot thì nó chứa tối đa được $k$ bản ghi đồng nghĩa mà chưa bị Overflow.

#### 2. Hai phương pháp giải quyết xung đột (충돌 해결 기법)
Khi xảy ra hiện tượng Overflow (xô đã đầy), có 2 chiến lược hóa giải:
- **개방 주소법 (Open Addressing):** Tìm một ô nhớ trống khác còn lại ngay bên trong bảng băm:
  - *선형 조사법 (Linear Probing):* Khi ô bị chiếm, tuần tự kiểm tra ô tiếp theo ($+1, +2, +3 \dots$). Dễ gây hiện tượng dồn cục cụm (Clustering).
  - *이차 조사법 (Quadratic Probing):* Nhảy theo bình phương khoảng cách ($+1^2, +2^2, +3^2 \dots$) để giảm bớt dồn cục.
  - *이중 해싱 (Double Hashing):* Dùng một hàm băm thứ hai để tính khoảng cách nhảy mỗi bước.
- **체이닝 (Chaining):** Mỗi Bucket được liên kết với một Danh sách liên kết (Linked List). Khi có phần tử mới cùng băm vào Bucket đã đầy, chỉ cần tạo Node mới và móc vào cuối danh sách liên kết mà không làm ảnh hưởng đến các Bucket khác.

---

### 복습 체크리스트
- [ ] Tính thành thạo số lần so sánh tối đa của Binary Search: $\lfloor \log_2 n \rfloor + 1$.
- [ ] Nắm rõ điều kiện tiên quyết bắt buộc của Binary Search là mảng đã sắp xếp.
- [ ] Phân biệt rõ chuỗi khái niệm: 동의어 (Synonym) $\rightarrow$ 충돌 (Collision) $\rightarrow$ 오버플로 (Overflow).
- [ ] Kể tên và nêu nguyên lý 5 hàm băm: 제산법 (chia dư), 제곱법 (bình phương giữa), 폴딩법 (gấp nếp), 기수 변환법, 숫자 분석법.
- [ ] Phân biệt hai chiến lược giải quyết xung đột: 개방 주소법 (Open Addressing) và 체이닝 (Chaining).
