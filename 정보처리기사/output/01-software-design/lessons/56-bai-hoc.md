# 13. 검색 및 해싱 (Search & Hashing)

## 학습 목표 (Mục tiêu)
- Nắm vững nguyên lý và điều kiện tiên quyết của Tìm kiếm nhị phân (`이진 검색 - Binary Search`): mảng bắt buộc phải được sắp xếp trước (`정렬 필수`) và đạt độ phức tạp $O(\log_2 N)$.
- Thuộc nằm lòng các khái niệm cốt lõi trong kỹ thuật Bảng băm (`해싱 - Hashing`): `버킷 (Bucket)`, `슬롯 (Slot)`, `충돌 (Collision)`, `동의어 (Synonym)`, và `오버플로 (Overflow)`.
- Nhận diện 5 hàm băm thông dụng (Chia dư, Bình phương giữa, Gấp nếp, Đổi cơ số, Phân tích số) và 2 chiến lược xử lý xung đột: Thăm dò mở (`개방 주소법`) và Chuỗi liên kết (`체이닝`).

## 핵심 키워드 (Từ khóa)
- 이진 검색 (Tìm kiếm nhị phân / Binary Search / 정렬 필수 / $O(\log N)$)
- 순차 검색 (Tìm kiếm tuần tự / Sequential Search / $O(N)$)
- 해싱 (Bảng băm / Hashing / $O(1)$)
- 버킷 / 슬롯 (Bucket / Slot)
- 충돌 vs 오버플로 (Collision vs Overflow)
- 제산법 (Division / Modulo), 제곱법 (Mid-Square), 폴딩법 (Folding)
- 개방 주소법 (Open Addressing / 선형 탐사) vs 체이닝 (Chaining / 연결 리스트)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([12. 외부 정렬 및 정렬 알고리즘](55-bai-hoc.md)):** Sau khi hoàn thành các thuật toán sắp xếp mảng, bài này khai thác mảng đã sắp xếp để tăng tốc tìm kiếm và giới thiệu kỹ thuật truy xuất tức thời $O(1)$ bằng Hashing.
- **Tiếp nối sang bài sau ([14. 파일 편성 방식 (File Organization)](57-bai-hoc.md)):** Ứng dụng kỹ thuật tìm kiếm tuần tự và chỉ mục băm vào các phương thức tổ chức tập tin vật lý trên đĩa cứng (Sequential, ISAM, Direct File).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc định nghĩa phân biệt: Collision là 2 khóa cùng ra 1 địa chỉ; Overflow là đụng độ khi Bucket đã hết slot trống; Chaining dùng danh sách liên kết giải quyết tràn.
- Đọc TẦNG B để theo dõi bài toán mẫu tính số lượt so sánh trong Binary Search và công thức chia dư của 제산법.

---

## 13. 검색 및 해싱 (Search & Hashing)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Các giải thuật tìm kiếm (검색 알고리즘):**
  - **순차 검색 (Sequential Search / Linear Search - Tìm kiếm tuần tự):**
    - Duyệt lần lượt từng phần tử từ đầu đến cuối danh sách cho đến khi tìm thấy khóa hoặc hết mảng.
    - *Điều kiện:* Dữ liệu **KHÔNG CẦN sắp xếp trước**.
    - *Độ phức tạp:* Trung bình $\frac{N+1}{2}$ lần so sánh $\rightarrow \mathbf{O(N)}$.
  - **이진 검색 / 이분 검색 (Binary Search - Tìm kiếm nhị phân):**
    - Chia đôi không gian tìm kiếm, so sánh khóa cần tìm với phần tử nằm chính giữa (`Mid`). Nếu nhỏ hơn thì tìm ở nửa trái, lớn hơn thì tìm ở nửa phải.
    - **Điều kiện tiên quyết sống còn:** **DỮ LIỆU BẮT BUỘC PHẢI ĐƯỢC SẮP XẾP SẴN (`반드시 정렬되어 있어야 함`)**.
    - *Độ phức tạp:* $\mathbf{O(\log_2 N)}$ (cực kỳ nhanh chóng).
- **2. Kỹ thuật Bảng băm (해싱 - Hashing):**
  - **Khái niệm:** Dùng hàm băm $h(K)$ chuyển đổi trực tiếp giá trị khóa $K$ thành địa chỉ ô nhớ trong bảng băm (`해시 테이블 - Hash Table`), cho phép tìm kiếm dữ liệu với **thời gian lý tưởng là $O(1)$**.
  - **Các thuật ngữ Hashing bắt buộc phải thuộc:**
    - `버킷 (Bucket)`: Một địa chỉ ô nhớ trong bảng băm, có thể chứa nhiều bản ghi.
    - `슬롯 (Slot)`: Số lượng vị trí chứa bản ghi có thể lưu trữ bên trong một Bucket duy nhất.
    - `충돌 (Collision - Xung đột)`: Hiện tượng **hai khóa khác nhau $K_1 \neq K_2$ nhưng qua hàm băm lại cho ra cùng một địa chỉ bucket ($h(K_1) = h(K_2)$)**.
    - `동의어 (Synonym)`: Tập hợp các khóa khác nhau nhưng sinh ra cùng một địa chỉ băm (các khóa gây ra xung đột Collision).
    - `오버플로 (Overflow - Hiện tượng tràn)`: Xảy ra khi xảy ra Collision tại một Bucket mà **Bucket đó đã hết sạch Slot trống** để chứa thêm bản ghi mới.
- **3. Các hàm băm (해시 함수) thông dụng:**
  - `제산법 (Division Method - Phương pháp chia dư)`: Lấy khóa chia cho số nguyên tố $M$ rồi lấy phần dư làm địa chỉ: $h(K) = K \pmod M$.
  - `제곱법 (Mid-Square Method - Phương pháp bình phương giữa)`: Bình phương giá trị khóa lên ($K^2$), sau đó trích xuất các chữ số nằm ở phần giữa làm địa chỉ băm.
  - `폴딩법 / 중첩법 (Folding Method - Phương pháp gấp nếp)`: Chia khóa thành nhiều đoạn có độ dài bằng nhau, sau đó cộng dồn hoặc dùng phép XOR các đoạn đó lại để tạo thành địa chỉ (Shift Folding hoặc Boundary Folding).
  - `기수 변환법 (Radix Transformation)`: Chuyển đổi hệ cơ số của khóa (ví dụ từ thập phân sang bát phân) rồi lấy các chữ số phù hợp làm địa chỉ.
  - `숫자 분석법 (Digit Analysis)`: Phân tích sự phân bố của các chữ số trong khóa và loại bỏ các chữ số có tính quy luật hoặc phân bố thiên lệch.
- **4. Phương pháp giải quyết Xung đột / Tràn (Collision / Overflow):**
  - `개방 주소법 (Open Addressing - Thăm dò mở)`: Khi bị tràn, tìm kiếm một ô trống khác còn lại bên trong chính bảng băm:
    - *Dò tuyến tính (Linear Probing):* Lần lượt thử các ô kế tiếp: $+1, +2, +3, \dots$
    - *Dò bậc hai (Quadratic Probing):* Thử các ô theo bước nhảy bậc hai: $+1^2, +2^2, +3^2, \dots$
  - `체이닝 (Chaining - Chuỗi liên kết)`: Sử dụng **Danh sách liên kết (Linked List)** để móc nối tất cả các bản ghi bị xung đột vào cùng một Bucket.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Điều kiện bắt buộc để thực hiện tìm kiếm nhị phân (Binary Search) là gì?"* -> **Mảng dữ liệu bắt buộc phải được sắp xếp trước (정렬되어 있어야 함)**.
  - **Bẫy 2:** *"Hiện tượng 2 khóa khác nhau sinh ra cùng 1 địa chỉ băm gọi là gì?"* -> **충돌 (Collision)**. Còn khi Bucket hết slot trống chứa mới gọi là **오버플로 (Overflow)**.
  - **Bẫy 3:** *"Các khóa sinh ra cùng địa chỉ băm gọi là gì?"* -> **동의어 (Synonym)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Nhị phân bắt buộc mảng đã sắp xếp; Hashing đổi khóa ra địa chỉ $O(1)$; Cùng địa chỉ là Collision, hết slot là Overflow; Tràn thì dùng Chaining liên kết hoặc Dò mở".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bài toán mẫu trắc nghiệm hàm băm chia dư (제산법):**
  - Cho bảng băm có kích thước $M = 11$ (địa chỉ từ $0$ đến $10$).
  - Dùng hàm băm: $h(K) = K \pmod{11}$.
  - Xác định địa chỉ của khóa $K = 27$ và $K = 38$:
    - $h(27) = 27 \pmod{11} = 5$ (địa chỉ 5).
    - $h(38) = 38 \pmod{11} = 5$ (địa chỉ 5).
  - Vì $h(27) = h(38) = 5$, ta kết luận:
    - Đã xảy ra hiện tượng **충돌 (Collision)** tại Bucket 5.
    - $27$ và $38$ được gọi là các **동의어 (Synonym)** của nhau.

### 복습 체크리스트
- [ ] Khẳng định được điều kiện của Binary Search là mảng đã sắp xếp với độ phức tạp $O(\log N)$.
- [ ] Phân biệt được rõ ràng giữa 충돌 (Collision) và 오버플로 (Overflow).
- [ ] Định nghĩa được thuật ngữ 동의어 (Synonym).
- [ ] Kể tên 4 hàm băm phổ biến: 제산법 (chia dư), 제곱법 (bình phương giữa), 폴딩법 (gấp nếp), 숫자 분석법.
- [ ] Phân biệt được 2 cách xử lý tràn: 개방 주소법 (dò ô trống) và 체이닝 (dùng linked list).
