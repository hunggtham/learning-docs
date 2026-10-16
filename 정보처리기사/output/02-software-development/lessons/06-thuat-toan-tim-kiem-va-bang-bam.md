# Môn 2 · Bài 06 — Thuật toán tìm kiếm và cấu trúc bảng băm

> **Mạch đọc:** [README](../README.md) là bản đồ chủ đề của **Môn 2 — 소프트웨어 개발 (Software Development)**. Sau khi dữ liệu đã được sắp xếp trật tự ở [Bài 05](05-thuat-toan-sap-xep-va-do-phuc-tap.md), thao tác truy xuất dữ liệu có thể chuyển dịch từ quét tuần tự chậm chạp sang các thuật toán tốc độ cao. Bài học này kết nối chặt chẽ thuật toán **Tìm kiếm nhị phân (Binary Search — $O(\log n)$)** với đỉnh cao của kỹ thuật tra cứu dữ liệu không cần so sánh: **Cấu trúc Bảng băm (Hashing — $O(1)$)**, cùng các phương pháp toán học giải quyết xung đột khóa.

> **Phạm vi nguồn:** Hợp nhất và chuẩn hóa nội dung từ 6 bài học cũ: `25, 26, 27, 28, 29, 30-bai-hoc.md` (tương ứng với các mục 7, 8, 32, 029 & 030, 087, 088 & 088-1 trong tài liệu chuẩn gốc). Toàn bộ công thức tính số lần so sánh tối đa và hệ thống thuật ngữ Bucket/Slot/Collision/Overflow được đối chiếu chuẩn xác theo giáo trình khảo thí HRDK.

> **Mạch kiến thức:** Bài học giải quyết ba bài toán cốt lõi trong truy xuất dữ liệu: (1) Tại sao Tìm kiếm nhị phân đòi hỏi mảng phải được sắp xếp trước và công thức tính số bước so sánh tối đa $\lfloor \log_2 n \rfloor + 1$ vận hành ra sao? (2) Bảng băm biến đổi khóa thành địa chỉ vật lý như thế nào và bộ ba thuật ngữ Synonym, Collision, Overflow có quan hệ nhân quả ra sao? (3) Năm hàm băm kinh điển (Division, Mid-square, Folding, Digit Analysis, Radix) và hai kỹ thuật giải quyết xung đột (Open Addressing vs Chaining) được áp dụng trong tình huống nào?

---

## 1. 검색 알고리즘 — Các thuật toán tìm kiếm so sánh khóa

Tìm kiếm (Searching / Retrieval) là quá trình xác định vị trí của một bản ghi chứa khóa tìm kiếm ($K$) trong một tập hợp dữ liệu.

### 1.1. 순차 검색 (Sequential / Linear Search — Tìm kiếm tuần tự)
- **Cơ chế:** Bắt đầu từ phần tử đầu tiên của danh sách, so sánh lần lượt từng phần tử một cho đến khi tìm thấy khóa cần tìm hoặc duyệt hết danh sách.
- **Đặc điểm:** Không yêu cầu dữ liệu phải được sắp xếp trước.
- **Độ phức tạp:** Thời gian trung bình và xấu nhất là **$O(n)$**. Số lần so sánh trung bình là $\frac{n + 1}{2}$. Rất chậm khi kích thước mảng $n$ lớn.

---

### 1.2. 이분 검색 (Binary Search — Tìm kiếm nhị phân)

**이분 검색은 반드시 자료가 미리 정렬(Sorted)되어 있어야만 적용할 수 있는 고속 탐색 알고리즘이다.**

- **Điều kiện tiên quyết bắt buộc:** Toàn bộ tập dữ liệu $A[1 \dots n]$ bắt buộc phải được **sắp xếp có thứ tự từ trước** (tăng dần hoặc giảm dần).
- **Cơ chế Chia để trị (Halving search space):**
  - Duy trì hai con trỏ biên: Đầu $\text{First } (F)$ và Cuối $\text{Last } (L)$.
  - Tại mỗi bước, tính chỉ số phần tử nằm ở chính giữa mảng:
    $$\mathbf{M = \left\lfloor \frac{F + L}{2} \right\rfloor}$$
  - So sánh khóa cần tìm ($K$) với giá trị $A[M]$:
    - Nếu $K == A[M]$: Tìm thấy thành công, trả về vị trí $M$.
    - Nếu $K < A[M]$: Thu hẹp phạm vi sang nửa bên trái: $\mathbf{L = M - 1}$.
    - Nếu $K > A[M]$: Thu hẹp phạm vi sang nửa bên phải: $\mathbf{F = M + 1}$.
  - Nếu $F > L$: Dừng tìm kiếm (Không tồn tại khóa trong mảng).

### Độ phức tạp thời gian và Công thức tính số lần so sánh tối đa
- **Thời gian trung bình và xấu nhất:** $\mathbf{O(\log n)}$.
- **Công thức tính số lần so sánh tối đa trong trường hợp xấu nhất:**
  $$\mathbf{\text{Max Comparisons} = \lfloor \log_2 n \rfloor + 1}$$
- **Ví dụ tính toán đề thi:**
  - Với tập dữ liệu $n = 15$ phần tử: $\lfloor \log_2 15 \rfloor + 1 = 3 + 1 = \mathbf{4}$ lần so sánh tối đa.
  - Với tập dữ liệu $n = 1.000.000$ bản ghi: Tối đa chỉ cần $\lfloor \log_2 1.000.000 \rfloor + 1 = 19 + 1 = \mathbf{20}$ lần so sánh!

---

## 2. 해싱(Hashing)의 개념 및 해시 테이블 구조 — Cấu trúc Bảng băm

**해싱은 키(Key) 값을 해시 함수(Hash Function)에 대입하여 계산된 값을 메모리의 주소(Home Address)로 직접 사용하는 검색 방법으로, 이상적인 경우 $O(1)$의 시간 복잡도를 갖는다.**

Thay vì tốn thời gian so sánh khóa qua nhiều bước, Hashing tính toán trực tiếp địa chỉ ô nhớ từ giá trị khóa thông qua một hàm toán học.

### Cấu trúc giải phẫu Bảng băm (Hash Table Terminology)

```
+--------------------------------------------------------+
| HASH TABLE                                             |
|                                                        |
| Bucket 0: [ Slot 1: Data A ] [ Slot 2: Empty  ]        |
| Bucket 1: [ Slot 1: Data B ] [ Slot 2: Data C ] (FULL) | <-- Overflow nếu có khóa mới vào đây!
| Bucket 2: [ Slot 1: Empty  ] [ Slot 2: Empty  ]        |
+--------------------------------------------------------+
```

### Bảng hệ thống thuật ngữ Hashing chuẩn đề thi

| Thuật ngữ | Tên Hàn & Anh | Định nghĩa kỹ thuật chuẩn mực |
| :--- | :--- | :--- |
| **Hàm băm** | **해시 함수 (Hash Function)** | Hàm toán học biến đổi khóa tìm kiếm $K$ thành địa chỉ bộ nhớ $h(K)$ |
| **Địa chỉ gốc** | **홈 주소 (Home Address)** | Giá trị địa chỉ trả về trực tiếp từ hàm băm $h(K)$ |
| **Thùng chứa** | **버킷 (Bucket)** | Một khối lưu trữ tương ứng với một địa chỉ băm, gồm một hoặc nhiều Slot |
| **Khe cắm** | **슬롯 (Slot)** | Một ô nhớ lưu trữ đúng một bản ghi dữ liệu bên trong Bucket |
| **Từ đồng nghĩa** | **동의어 (Synonym)** | **Tập hợp các khóa khác nhau nhưng có cùng địa chỉ băm**: $h(K_1) = h(K_2)$ |
| **Đụng độ** | **충돌 (Collision)** | **Hiện tượng hai khóa khác nhau được hàm băm ánh xạ vào cùng một Bucket** |
| **Tràn thùng** | **오버플로 (Overflow)** | Hiện tượng xảy ra khi một Bucket **không còn Slot trống nào** để chứa thêm bản ghi |

### ⚠️ Mối liên hệ nhân quả giữa Collision và Overflow
- **Trường hợp 1 (Bucket có 1 Slot — $1 \text{ Bucket} = 1 \text{ Slot}$):** Khi xảy ra **Collision (Đụng độ)** thì **đồng thời lập tức xảy ra Overflow (Tràn)**.
- **Trường hợp 2 (Bucket có nhiều Slot):** Khi xảy ra Collision, bản ghi mới vẫn được cất vào Slot trống tiếp theo trong cùng Bucket đó; chỉ khi toàn bộ các Slot trong Bucket đều đã đầy kín thì mới phát sinh hiện tượng Overflow.

---

## 3. 주요 해싱 함수 (Hashing Functions) — Các hàm băm kinh điển

Mục tiêu tối thượng của hàm băm là: Tính toán nhanh và phân tán các khóa đồng đều khắp các Bucket để giảm thiểu tối đa hiện tượng Collision.

### Bảng 5 hàm băm chuẩn xuất hiện trong đề thi

| Hàm băm | Tên Hàn & Anh | Cơ chế tạo địa chỉ (Từ khóa nhận diện đề thi) | Ví dụ minh họa thực tế |
| :--- | :--- | :--- | :--- |
| **Phép chia lấy dư** | **제산법 (Division Method)** | Lấy khóa $K$ chia cho kích thước bảng băm $M$ (**$M$ bắt buộc phải là số nguyên tố — Prime Number**) và lấy phần dư: $\mathbf{h(K) = K \pmod M}$ | Khóa $K = 45$, chọn số nguyên tố $M = 7$: $45 \pmod 7 = \mathbf{3}$ $\rightarrow$ Địa chỉ là 3 |
| **Bình phương lấy giữa** | **제곱법 (Mid-Square Method)** | Lấy giá trị khóa nhân với chính nó ($K^2$), sau đó **trích xuất các chữ số ở phần chính giữa** để làm địa chỉ băm | Khóa $K = 512 \rightarrow 512^2 = 262144 \rightarrow$ Lấy 2 số giữa là **`21`** làm địa chỉ |
| **Phương pháp gấp nếp** | **폴딩법 (Folding Method)** | Chia khóa thành nhiều đoạn có độ dài bằng độ dài địa chỉ, sau đó **cộng (hoặc làm phép XOR) các đoạn lại với nhau** | Khóa `12345678` chia thành `123, 456, 78` $\rightarrow 123 + 456 + 78 = \mathbf{657}$ |
| **Phân tích chữ số** | **숫자 분석법 (Digit Analysis)** | Phân tích toàn bộ tập khóa để tìm ra các vị trí chữ số có **tần suất phân bố đồng đều nhất (ít bị trùng lặp)** và ghép lại làm địa chỉ | Số CMND/CCCD: Bỏ mã tỉnh và năm sinh (dễ trùng), chỉ trích xuất các chữ số ngẫu nhiên ở cuối |
| **Chuyển đổi cơ số** | **기수 변환법 (Radix Conversion)** | Coi khóa như đang ở một hệ cơ số khác (ví dụ từ cơ số 10 chuyển sang cơ số 13 hoặc 16) rồi trích xuất địa chỉ | Đổi hệ cơ số để phá vỡ quy luật trùng lặp ban đầu |

### Phân biệt hai biến thể của phương pháp Gấp nếp (폴딩법):
- **이동 폴딩 (Shift Folding):** Giữ nguyên thứ tự các đoạn và đem cộng trực tiếp lại với nhau.
- **경계 폴딩 (Boundary Folding):** Giữ nguyên đoạn ở giữa, **lật ngược đối xứng (đảo chiều các chữ số) các đoạn nằm ở biên hai bên** trước khi cộng lại.

---

## 4. 충돌 및 오버플로 해결 기법 — Xử lý đụng độ và tràn thùng

Khi hiện tượng Overflow xảy ra (Bucket đã kín chỗ), bắt buộc phải có cơ chế tìm vị trí mới để lưu bản ghi. Có hai chiến lược giải quyết chính:

### 4.1. 개방 주소법 (Open Addressing — Địa chỉ mở)
Khi Bucket mục tiêu bị tràn, thuật toán sẽ đi tìm một **Bucket trống khác còn lại trong bảng băm** để cất bản ghi vào:
1. **선형 조사법 (Linear Probing — Thử tuyến tính):**
   - Nếu Bucket $h(K)$ bị đầy, thử tuần tự các Bucket kế tiếp: $h(K) + 1, h(K) + 2, h(K) + 3 \dots$
   - **Nhược điểm lớn nhất (Bẫy thi):** Dẫn đến hiện tượng **동기화 / 군집화 (Clustering — Kết cụm dữ liệu)**, các bản ghi dồn cục vào một khu vực làm thời gian tra cứu bị chậm dần.
2. **이차 조사법 (Quadratic Probing — Thử bậc hai):**
   - Thử các vị trí theo bước nhảy bình phương để tránh kết cụm: $h(K) + 1^2, h(K) + 2^2, h(K) + 3^2 \dots$
3. **이중 해싱법 (Double Hashing — Băm kép):**
   - Sử dụng hai hàm băm độc lập: Hàm băm 1 $h_1(K)$ để xác định địa chỉ ban đầu; nếu bị tràn thì dùng Hàm băm 2 $h_2(K)$ để tính bước nhảy. Đây là phương pháp địa chỉ mở tối ưu nhất.

### 4.2. 폐쇄 주소법 / 체이닝 (Chaining — Đóng địa chỉ / Móc xích)
- **Cơ chế:** Không đi tìm Bucket khác. Mỗi Bucket trong bảng băm được gắn với một **Danh sách liên kết (Linked List)**.
- Khi xảy ra Collision và Overflow, bản ghi mới sẽ được tạo thành một Node mới và **móc nối tiếp vào đuôi danh sách liên kết của chính Bucket đó**.
- **Ưu điểm lớn:** Bảng băm không bao giờ bị đầy tuyệt đối, không làm ảnh hưởng đến các Bucket khác, xóa bản ghi cực kỳ dễ dàng.

---

## 5. Nối mạch kiến thức sang bài tiếp theo

Từ các thuật toán tìm kiếm nhị phân và bảng băm trong bộ nhớ RAM, khi dữ liệu phát triển lên quy mô doanh nghiệp và đòi hỏi tính bền vững, toàn vẹn và giao dịch an toàn, toàn bộ cơ chế lưu trữ này được nâng cấp thành **Hệ thống Quản lý Cơ sở Dữ liệu (DBMS)**.

Chúng ta sẽ khép lại Chương 1 với **[Bài 07: Cơ sở dữ liệu và tối ưu hóa truy vấn trong phát triển phần mềm](07-co-so-du-lieu-va-toi-uu-truy-van.md)**, nơi ta sẽ khảo sát kiến trúc 3 tầng Schema, tính độc lập dữ liệu, lập trình SQL thủ tục (Procedural SQL) và kỹ thuật tối ưu hóa truy vấn (Query Optimization) từ góc nhìn của kỹ sư phát triển phần mềm.

---

## 6. 복습 체크리스트 (Checklist ôn tập)

- [ ] Nhớ điều kiện tiên quyết duy nhất của 이분 검색 (Binary Search): Dữ liệu bắt buộc phải được sắp xếp trước.
- [ ] Tính đúng chỉ số giữa: $M = \lfloor (F + L) / 2 \rfloor$.
- [ ] Áp dụng đúng công thức số lần so sánh tối đa của Binary Search: $\lfloor \log_2 n \rfloor + 1$.
- [ ] Định nghĩa và phân biệt rõ bộ ba thuật ngữ: 동의어 (Synonym), 충돌 (Collision), 오버플로 (Overflow).
- [ ] Khẳng định: Nếu Bucket chỉ có 1 Slot thì Collision luôn kéo theo Overflow.
- [ ] Nhớ công thức 제산법 (Division Method): $h(K) = K \pmod M$ với $M$ là số nguyên tố.
- [ ] Nhận diện 제곱법 (Mid-Square) qua thao tác tính $K^2$ rồi trích chữ số ở giữa.
- [ ] Phân biệt 이동 폴딩 (Shift) và 경계 폴딩 (Boundary) trong phương pháp 폴딩법.
- [ ] Phân biệt hai hướng xử lý Overflow: 개방 주소법 (Open Addressing: Linear, Quadratic, Double) và 체이닝 (Chaining dùng Linked List).
- [ ] Nhớ nhược điểm lớn nhất của Linear Probing là hiện tượng 군집화 (Clustering).
