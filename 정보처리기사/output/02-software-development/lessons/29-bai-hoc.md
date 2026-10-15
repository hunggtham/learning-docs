# 32. 추가 해싱 함수 (Additional Hashing Functions)

## 학습 목표 (Mục tiêu)
- Nắm vững các hàm băm bổ sung thường xuất hiện trong đề thi nâng cao: Phương pháp chuyển đổi cơ số (기수 변환법 - Radix Conversion), Phương pháp mã hóa đại số (대수적 코딩법 - Algebraic Coding) và Phương pháp ngẫu nhiên (무작위법 - Random Method).
- Phân biệt cơ chế sinh địa chỉ của từng phương pháp: Đổi hệ cơ số, Chia đa thức đại số và Sinh số giả ngẫu nhiên.
- Đánh giá ưu nhược điểm và phạm vi ứng dụng thực tế của từng hàm băm trong cấu trúc dữ liệu và an toàn thông tin.

## 핵심 키워드 (Từ khóa)
- 해싱 함수 (Hashing Functions)
- 기수 변환법 (Radix Conversion Method)
- 대수적 코딩법 (Algebraic Coding Method)
- 다항식의 계수 (Polynomial Coefficients)
- 무작위법 / 난수법 (Random Method)
- 의사 난수 생성기 (Pseudo-random Generator)

## 선행·연결 개념 (Kiến thức liên kết)
- [26-bai-hoc.md](26-bai-hoc.md): Nguyên lý hoạt động của bảng băm và các phương pháp giải quyết đụng độ.
- [28-bai-hoc.md](28-bai-hoc.md): Các hàm băm cơ bản (Division, Mid-square, Folding, Digit analysis).
- [30-bai-hoc.md](30-bai-hoc.md): Tổng hợp toàn diện Hashing và mô hình lưu trữ dữ liệu.

## 읽는 방법 (Cách đọc)
- Nhớ nhanh từ khóa nhận diện của 3 phương pháp bổ sung:
  - Cứ thấy **"진수를 다른 진수로 변환"** (Đổi sang hệ cơ số khác) $\rightarrow$ **기수 변환법 (Radix Conversion)**.
  - Cứ thấy **"다항식의 계수로 간주하여 나눈 나머지"** (Coi chữ số là hệ số đa thức rồi chia) $\rightarrow$ **대수적 코딩법 (Algebraic Coding)**.
  - Cứ thấy **"난수(Random Number)를 발생시켜 주소로 사용"** $\rightarrow$ **무작위법 (Random Method)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp 3 hàm băm mở rộng:**

| Phương pháp băm | Tên tiếng Hàn & Anh | Cơ chế hoạt động chi tiết | Mẹo nhận diện đề thi |
| :--- | :--- | :--- | :--- |
| **Chuyển đổi cơ số** | **기수 변환법 (Radix Conversion)** | Lấy giá trị khóa số vốn ở hệ thập phân (Base 10) đem chuyển đổi sang một hệ cơ số khác (ví dụ Base 13 hoặc Base 16). Sau đó trích xuất các chữ số ở phần đuôi có độ dài vừa khít với kích thước bảng băm để làm địa chỉ | "다른 진법으로 변환", "기수 변환" |
| **Mã hóa đại số** | **대수적 코딩법 (Algebraic Coding)** | Coi các chữ số cấu thành nên khóa $K$ như là **các hệ số của một đa thức đại số** (Polynomial). Đem đa thức này chia cho một đa thức sinh (Generator Polynomial) cố định, và lấy các hệ số của phần dư làm địa chỉ băm | "다항식 (Đa thức)", "계수 (Hệ số)" |
| **Phương pháp ngẫu nhiên** | **무작위법 / 난수법 (Random Method)** | Sử dụng chính giá trị của khóa $K$ làm hạt giống (Seed) đưa vào một hàm sinh số giả ngẫu nhiên (Pseudo-random number generator) để tạo ra một số ngẫu nhiên nằm trong khoảng kích thước bảng băm làm địa chỉ | "난수 발생 (Sinh số ngẫu nhiên)", "Seed 값" |

- **Bẫy đề thi trắc nghiệm:**
  - **Bẫy 1:** *"Phương pháp băm nào xem các ký tự của khóa như là các hệ số của đa thức?"* $\rightarrow$ Đáp án: **대수적 코딩법 (Algebraic Coding)**.
  - **Bẫy 2:** *"Phương pháp nào sử dụng thuật toán sinh số giả ngẫu nhiên để xác định địa chỉ ô nhớ?"* $\rightarrow$ Đáp án: **무작위법 (Random Method)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mối liên hệ giữa Algebraic Coding và mã kiểm tra lỗi CRC:**
  - Bản chất của **Algebraic Coding Method** tương tự như cơ chế tính toán mã kiểm tra dư thừa vòng tuần hoàn **CRC (Cyclic Redundancy Check)** trong truyền thông mạng máy tính:
    - Cả hai đều biểu diễn chuỗi bit thành đa thức $P(x)$, thực hiện phép chia đa thức theo trường hữu hạn modulo 2 (GF(2)) với đa thức sinh $G(x)$, và lấy phần dư $R(x)$.
    - Kỹ thuật này giúp phân tán các bit cực kỳ đồng đều, giảm thiểu tỷ lệ đụng độ ngay cả khi tập khóa có cấu trúc rất giống nhau.

### 복습 체크리스트
- [ ] Nhận biết 기수 변환법 qua từ khóa: Đổi hệ cơ số (진법 변환).
- [ ] Nhận biết 대수적 코딩법 qua từ khóa: Hệ số đa thức đại số (다항식의 계수).
- [ ] Nhận biết 무작위법 qua từ khóa: Sinh số giả ngẫu nhiên (난수 발생).
- [ ] Tổng hợp đủ 7 hàm băm kinh điển: Division, Mid-Square, Folding, Digit Analysis, Radix, Algebraic, Random.
