# A+ Deep Dive: Java 비교 연산과 Python 제어 흐름

## 학습 목표 (Mục tiêu)
- Nắm vững sự khác biệt bản chất giữa toán tử so sánh `==` và phương thức `equals()` trong ngôn ngữ Java khi làm việc với kiểu dữ liệu đối tượng (Reference Types), đặc biệt là lớp chuỗi `String`.
- Hiểu cơ chế thăng cấp số học nhị phân (Binary Numeric Promotion) trong các phép so sánh giữa các kiểu số nguyên thủy khác nhau của Java.
- Rèn luyện kỹ năng lần vết thuật toán phức tạp trên luồng điều khiển vòng lặp của Python (`for`, `while`, `break`, `continue`) và các bẫy điều kiện biên trong đề thi.

## 핵심 키워드 (Từ khóa)
- Java 비교 연산 (`==` vs `equals()`)
- 주소 비교 vs 내용 비교 (Reference Comparison vs Value Comparison)
- 수치 승격 (Binary Numeric Promotion)
- Python 제어 흐름 (Python Control Flow Trace)
- continue vs break (반복문 제어 흐름)
- String Constant Pool (문자열 리터럴 풀)

## 선행·연결 개념 (Kiến thức liên kết)
- [28-bai-hoc.md](28-bai-hoc.md): Tổng hợp toàn diện cú pháp và cấu trúc Python.
- [30-bai-hoc.md](30-bai-hoc.md): Thư viện chuẩn và cơ chế xử lý ngoại lệ.
- [05-bai-hoc.md](05-bai-hoc.md): Kiểu dữ liệu nguyên thủy và kiểu tham chiếu trong Java.

## 읽는 방법 (Cách đọc)
- Phân biệt hai bẫy thi dễ mất điểm nhất trong đề thi kỹ sư:
  - **Bẫy 1 - So sánh trong Java:**
    - Đối với biến nguyên thủy (`int`, `double`): `==` so sánh **giá trị số học**.
    - Đối với biến đối tượng (`String`, `Object`): `==` so sánh **địa chỉ ô nhớ** (xem 2 biến có cùng trỏ tới 1 đối tượng duy nhất trên Heap không). Muốn so sánh **nội dung chuỗi chữ bên trong**, bắt buộc phải dùng phương thức `.equals()`.
  - **Bẫy 2 - Lần vết vòng lặp Python:**
    - Cần theo dõi chính xác thời điểm biến đếm thay đổi: Khi gặp `continue`, phần thân bên dưới bị bỏ qua ngay lập tức để nhảy sang bước lặp tiếp theo.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh: `==` vs `equals()` trong Java:**

| Trường hợp kiểm tra | Cú pháp Java | Kết quả trả về | Lý do kỹ thuật giải thích chuẩn thi |
| :--- | :--- | :--- | :--- |
| **Số nguyên và Số thực** | `int a = 1; double b = 1.0; a == b` | **`true`** | Kiểu `int` tự động thăng cấp thành `double` rồi so sánh giá trị số học |
| **Hai đối tượng chuỗi tạo bằng `new`** | `String x = new String("A");` `String y = new String("A");` `x == y` | **`false`** | Toán tử `==` so sánh **địa chỉ ô nhớ**; hai lệnh `new` tạo ra hai vùng nhớ Heap hoàn toàn độc lập |
| **So sánh nội dung chuỗi** | `x.equals(y)` | **`true`** | Phương thức `equals()` so sánh **từng ký tự bên trong** của hai chuỗi |
| **Chuỗi Literal gán trực tiếp** | `String s1 = "A";` `String s2 = "A";` `s1 == s2` | **`true`** | Java gom hai chuỗi hằng số vào cùng một vùng nhớ **String Constant Pool** |

- **Bẫy biểu thức so sánh chuỗi ba ngôi: `a == b == c`:**
  - Trong lập trình, biểu thức `a == b == c` **KHÔNG MANG NGHĨA** "cả ba giá trị có bằng nhau hay không".
  - Trình biên dịch tính toán từ trái sang phải: `(a == b) == c`. Biểu thức `(a == b)` trả về `true` hoặc `false`, sau đó giá trị boolean này mới đem so sánh với `c` $\rightarrow$ Thường dẫn đến sai logic nghiêm trọng hoặc lỗi biên dịch.
  - Muốn so sánh 3 biến bằng nhau, bắt buộc phải viết: `(a == b) && (b == c)`.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Lần vết bài toán kết hợp Python Control Flow:**
  - *Đoạn mã Python:*
    ```python
    items = [1, 2, 3, 4]
    total = 0
    for value in items:
        if value == 2:
            continue
        if value == 4:
            break
        total += value
    print(total)
    ```
  - *Quá trình lần vết:*
    - `value = 1`: Không rơi vào if nào $\rightarrow$ `total = 0 + 1 = 1`.
    - `value = 2`: Thỏa mãn `value == 2` $\rightarrow$ Gặp `continue`, bỏ qua `total += value`, nhảy sang phần tử tiếp theo.
    - `value = 3`: Không rơi vào if $\rightarrow$ `total = 1 + 3 = 4`.
    - `value = 4`: Thỏa mãn `value == 4` $\rightarrow$ Gặp `break`, kết thúc ngay lập tức vòng lặp.
  - Kết quả in ra: **`4`**.

### 복습 체크리스트
- [ ] Nhớ trong Java: `new String("A") == new String("A")` là FALSE (khác địa chỉ).
- [ ] Nhớ trong Java: So sánh nội dung chuỗi BẮT BUỘC dùng phương thức `equals()`.
- [ ] Hiểu quy tắc Short-Circuit và hướng thực thi của `continue` và `break` trong Python.
- [ ] Không viết gộp `a == b == c`; phải tách thành `(a == b) && (b == c)`.
