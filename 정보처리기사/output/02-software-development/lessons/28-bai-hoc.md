# 8. 주요 해싱 함수 (Hashing Functions)

## 학습 목표 (Mục tiêu)
- Định nghĩa hàm băm (해싱 함수 - Hashing Function) và vai trò biến đổi khóa tìm kiếm (Key) thành địa chỉ ô nhớ vật lý trong bảng băm (Hash Table).
- Nắm vững nguyên lý hoạt động của 4 hàm băm kinh điển nhất: Phép chia lấy dư (제산법 - Division), Bình phương lấy giữa (제곱법 - Mid-Square), Phương pháp gấp nếp (폴딩법 - Folding) và Phân tích chữ số (숫자 분석법 - Digit Analysis).
- Phân biệt hai biến thể của phương pháp gấp nếp: Gấp dịch chuyển (이동 폴딩 - Shift Folding) và Gấp đường biên (경계 폴딩 - Boundary Folding).

## 핵심 키워드 (Từ khóa)
- 해싱 함수 (Hashing Function)
- 제산법 (Division Method / 소수 Prime Modulo)
- 제곱법 (Mid-Square Method / 중간 비트 추출)
- 폴딩법 (Folding Method: 이동 폴딩 & 경계 폴딩)
- 숫자 분석법 (Digit Analysis Method / 균등 분포)
- 홈 주소 (Home Address)

## 선행·연결 개념 (Kiến thức liên kết)
- [26-bai-hoc.md](26-bai-hoc.md): Khái niệm Bảng băm, Đụng độ (Collision) và Tràn thùng chứa (Overflow).
- [29-bai-hoc.md](29-bai-hoc.md): Các hàm băm bổ sung (Radix Conversion, Algebraic Coding, Random).
- [30-bai-hoc.md](30-bai-hoc.md): Tổng hợp Hashing và kiến trúc lưu trữ dữ liệu (Data Storage).

## 읽는 방법 (Cách đọc)
- Nhận diện câu hỏi trắc nghiệm qua từ khóa đặc trưng:
  - Cứ thấy **"키 값을 소수(Prime)로 나눈 나머지"** $\rightarrow$ **제산법 (Division)**.
  - Cứ thấy **"키 값을 제곱한 후 중간 부분 추출"** $\rightarrow$ **제곱법 (Mid-Square)**.
  - Cứ thấy **"키를 여러 부분으로 나누어 더하거나 XOR"** $\rightarrow$ **폴딩법 (Folding)**.
  - Cứ thấy **"숫자의 분포를 분석하여 편중되지 않은 자리수 선택"** $\rightarrow$ **숫자 분석법 (Digit Analysis)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp 4 hàm băm kinh điển:**

| Phương pháp băm | Tên tiếng Hàn & Anh | Cơ chế tạo địa chỉ (Từ khóa nhận diện) | Ví dụ minh họa |
| :--- | :--- | :--- | :--- |
| **Phép chia lấy dư** | **제산법 (Division Method)** | Lấy giá trị khóa $K$ chia cho kích thước bảng băm $M$ (thường chọn $M$ là **số nguyên tố - Prime Number**) và lấy phần dư làm địa chỉ: $h(K) = K \pmod M$ | Khóa $K = 45$, chọn số nguyên tố $M = 7 \rightarrow 45 \pmod 7 = 3 \rightarrow$ Địa chỉ là 3 |
| **Bình phương lấy giữa** | **제곱법 (Mid-Square Method)** | Lấy giá trị khóa nhân với chính nó ($K^2$), sau đó trích xuất các chữ số ở **phần chính giữa** để làm địa chỉ băm | Khóa $K = 512 \rightarrow 512^2 = 262144 \rightarrow$ Lấy 2 chữ số ở giữa là `21` làm địa chỉ |
| **Phương pháp gấp nếp** | **폴딩법 (Folding Method)** | Chia khóa thành nhiều đoạn có độ dài bằng độ dài địa chỉ, sau đó **cộng (hoặc làm phép XOR) các đoạn lại với nhau** để thu được địa chỉ | Khóa `12345678` chia thành `123`, `456`, `78` rồi đem cộng lại: $123 + 456 + 78 = 657$ |
| **Phân tích chữ số** | **숫자 분석법 (Digit Analysis)** | Phân tích toàn bộ tập hợp khóa để tìm ra các vị trí chữ số có **sự phân bố đồng đều nhất (ít bị trùng lặp)** và ghép lại làm địa chỉ | Mã số sinh viên gồm năm nhập học, khoa, số thứ tự $\rightarrow$ Bỏ năm và khoa (dễ trùng), chỉ lấy các số thứ tự để làm địa chỉ |

- **Hai dạng của phương pháp 폴딩법 (Folding Method):**
  - **이동 폴딩 (Shift Folding):** Giữ nguyên thứ tự các đoạn và đem cộng trực tiếp lại với nhau.
  - **경계 폴딩 (Boundary Folding):** Giữ nguyên đoạn ở giữa, lật ngược (đảo chiều đối xứng) các đoạn nằm ở biên giới hai bên trước khi thực hiện phép cộng.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tại sao 제산법 (Division) bắt buộc phải chọn số chia là Số nguyên tố (Prime)?**
  - Nếu chọn số chia $M$ là số chẵn hoặc bội số của 10 (ví dụ $M = 100$): Địa chỉ băm sẽ chỉ phụ thuộc vào 2 chữ số cuối cùng của khóa. Nếu các khóa trong thực tế có xu hướng kết thúc bằng đuôi giống nhau (như các mã phòng ban chẵn chục), hiện tượng đụng độ (Collision) sẽ tăng đột biến.
  - Việc chọn $M$ là **số nguyên tố** giúp phân tán dư lượng đều khắp mọi vùng địa chỉ trong bảng băm.

### 복습 체크리스트
- [ ] Nhớ công thức 제산법: $h(K) = K \pmod M$ với $M$ là số nguyên tố.
- [ ] Nhận diện 제곱법 qua hành động tính $K^2$ rồi trích chữ số ở giữa.
- [ ] Phân biệt rõ hai loại 폴딩법: 이동 폴딩 (Shift) và 경계 폴딩 (Boundary).
- [ ] Nhớ cơ chế 숫자 분석법: Phân tích tần suất phân bố đồng đều của các chữ số.
