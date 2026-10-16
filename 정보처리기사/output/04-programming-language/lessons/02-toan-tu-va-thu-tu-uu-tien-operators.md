# 연산자 및 연산자 우선순위 (Toán tử & Thứ tự ưu tiên)

## 학습 목표 (Mục tiêu)
- Nắm vững toàn bộ hệ thống toán tử trong C, Java, Python: toán tử số học, toán tử tăng/giảm tiền tố - hậu tố, toán tử quan hệ, toán tử logic, toán tử thao tác bit và toán tử điều kiện tam phân.
- Thuộc lòng thứ tự ưu tiên của các toán tử theo khẩu quyết chuẩn khảo thí **단산관논대** (Đơn hạng > Số học > Quan hệ > Logic > Gán).
- Hiểu rõ cơ chế lượng giá ngắn mạch (Short-Circuit Evaluation) và sự khác biệt giữa toán tử `==` (so sánh địa chỉ ô nhớ) và phương thức `.equals()` (so sánh nội dung chuỗi) trong Java.

## 핵심 키워드 (Từ khóa)
- 연산자 우선순위 (Operator Precedence) — Thứ tự ưu tiên lượng giá toán tử (단산관논대).
- 증감 연산자 (Increment/Decrement Operators) — Tiền tố `++x` (tăng trước) vs Hậu tố `x++` (dùng trước tăng sau).
- 단락 평가 (Short-Circuit Evaluation) — Ngừng lượng giá nhánh sau khi nhánh trước của `&&` hoặc `||` đã xác định được chân trị.
- 비트 연산자 (Bitwise Operators) — Phép toán bit: AND `&`, OR `|`, XOR `^`, NOT `~`, dịch trái `<<`, dịch phải `>>`.
- 삼항 조건 연산자 (Ternary Operator) — Cú pháp `조건식 ? 참 : 거짓`.
- 문자열 비교 (String Comparison in Java) — `==` so sánh tham chiếu Heap vs `equals()` so sánh nội dung.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa từ `01-bien-dinh-danh-va-kieu-du-lieu-c-java.md`, sử dụng các kiểu dữ liệu nguyên thủy (`int`, `char`, `float`, `boolean`) làm toán hạng tính toán.
- **Đang giải quyết gì (Current Problem):** Giải quyết bài toán lượng giá biểu thức phức hợp trong đề thi: Khi một biểu thức chứa đồng thời nhiều loại phép toán, máy tính thực thi phép toán nào trước, quy tắc ép kiểu ngầm định ra sao và bẫy tăng/giảm tiền tố - hậu tố nằm ở đâu.
- **Dùng đi đâu (Forward Handoff):** Các biểu thức điều kiện và phép so sánh logic này là điều kiện cốt lõi để điều khiển các nhánh rẽ và vòng lặp trong bài `04-cau-truc-dieu-khien-re-nhanh-va-vong-lap.md`.

## 읽는 방법 (Cách đọc)
- **Khẩu quyết thứ tự ưu tiên:** Nhớ ngay 5 chữ cái tiếng Hàn: **단·산·관·논·대** (Đơn hạng $\rightarrow$ Số học $\rightarrow$ Quan hệ $\rightarrow$ Logic $\rightarrow$ Gán). Ngoặc đơn `( )` luôn có quyền ưu tiên cao nhất.
- **Toán tử bit XOR `^`:** Hai bit **khác nhau thì bằng 1**, giống nhau thì bằng 0 ($1 \oplus 0 = 1$, $1 \oplus 1 = 0$, $0 \oplus 0 = 0$).
- **Tiền tố vs Hậu tố:** `y = ++x` (tăng `x` lên rồi mới gán cho `y`); `y = x++` (gán giá trị cũ của `x` cho `y` xong mới tăng `x`).

---

## 연산자 및 연산자 우선순위

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `복합 식에서 연산자 우선순위는 괄호()가 가장 높고, 단항 > 산술 > 관계 > 논리 > 대입 연산자 순서로 평가된다. 논리곱(&&)은 앞이 거짓이면 뒤를 평가하지 않고, 논리합(||)은 앞이 참이면 뒤를 평가하지 않는다.`
  - [Tiếng Việt]: Trong biểu thức phức hợp, cặp ngoặc đơn `()` có ưu tiên cao nhất, tiếp theo là Đơn hạng > Số học > Quan hệ > Logic > Gán. Phép `&&` dừng tính nếu vế trái False; phép `||` dừng tính nếu vế trái True.

- **1. Bảng thứ tự ưu tiên toán tử (연산자 우선순위 - 단산관논대):**

| Cấp ưu tiên | Nhóm toán tử | Ký hiệu phép toán | Hướng kết hợp |
| :---: | :--- | :--- | :---: |
| **1 (Cao nhất)** | Ngoặc & Truy xuất | `()`, `[]`, `.`, `->` | Trái $\rightarrow$ Phải |
| **2 (Đơn hạng - 단)**| Unary / Đơn vị | `++`, `--`, `+`, `-`, `!`, `~`, `sizeof`, `(type)` | **Phải $\rightarrow$ Trái** |
| **3 (Số học - 산)** | Nhân, chia, lấy dư | `*`, `/`, `%` | Trái $\rightarrow$ Phải |
| **4 (Số học - 산)** | Cộng, trừ | `+`, `-` | Trái $\rightarrow$ Phải |
| **5 (Dịch bit)** | Shift bit | `<<`, `>>` | Trái $\rightarrow$ Phải |
| **6 (Quan hệ - 관)**| So sánh lớn nhỏ | `<`, `<=`, `>`, `>=` | Trái $\rightarrow$ Phải |
| **7 (Quan hệ - 관)**| So sánh bằng nhau | `==`, `!=` | Trái $\rightarrow$ Phải |
| **8 (Bitwise)** | Thao tác bit | `&` $\rightarrow$ `^` $\rightarrow$ `\|` (theo thứ tự này) | Trái $\rightarrow$ Phải |
| **9 (Logic - 논)** | Logic AND & OR | `&&` rồi đến `\|\|` | Trái $\rightarrow$ Phải |
| **10 (Tam phân)** | Điều kiện 3 ngôi | `? :` | **Phải $\rightarrow$ Trái** |
| **11 (Gán - 대)** | Gán & Gán phức | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, `&=`, `^=`, `\|=` | **Phải $\rightarrow$ Trái** |
| **12 (Thấp nhất)**| Dấu phẩy | `,` | Trái $\rightarrow$ Phải |

- **2. Bảng quy tắc toán tử thao tác bit (비트 연산자):**

| Toán tử bit | Tên gọi | Bản chất xử lý bit | Ví dụ minh họa |
| :---: | :--- | :--- | :--- |
| `&` | Bitwise AND | Cả 2 bit đều bằng 1 thì kết quả là 1; ngược lại bằng 0. | `5 & 3` (`101 & 011` $\rightarrow$ `001` = **1**) |
| `\|` | Bitwise OR | Chỉ cần 1 trong 2 bit bằng 1 thì kết quả là 1. | `5 \| 3` (`101 \| 011` $\rightarrow$ `111` = **7**) |
| `^` | Bitwise XOR | **Hai bit khác nhau thì bằng 1**, giống nhau thì bằng 0. | `5 ^ 3` (`101 ^ 011` $\rightarrow$ `110` = **6**) |
| `~` | Bitwise NOT | Đảo bit (bù 1): biến 0 thành 1 và biến 1 thành 0. | `~5` (trong hệ bù 2 thành **-6**) |
| `<<` | Left Shift | Dịch bit sang trái $k$ vị trí, tương đương nhân với $2^k$. | `3 << 2` ($3 \times 2^2$ = **12**) |
| `>>` | Right Shift | Dịch bit sang phải $k$ vị trí, tương đương chia nguyên cho $2^k$. | `12 >> 2` ($12 \div 2^2$ = **3**) |

- **3. Đối chiếu so sánh chuỗi trong Java (`==` vs `.equals()`):**

| Cú pháp kiểm tra | Kết quả trả về | Cơ chế kỹ thuật |
| :--- | :---: | :--- |
| `new String("A") == new String("A")` | **`false`** | Toán tử `==` so sánh **địa chỉ ô nhớ Heap**; 2 lệnh `new` tạo ra 2 ô nhớ khác nhau. |
| `str1.equals(str2)` | **`true`** | Phương thức `.equals()` so sánh **từng ký tự nội dung bên trong**. |
| `"A" == "A"` | **`true`** | Java tự động tối ưu hóa hằng số chuỗi vào **String Constant Pool**. |

- **주의/함정 (Bẫy đề thi):**
  - **Bẫy chia nguyên:** Trong C/Java, `5 / 2` cho kết quả là **`2`** (cắt bỏ phần thập phân), chứ không phải `2.5`. Muốn có `2.5` phải viết `5.0 / 2` hoặc `(double)5 / 2`.
  - **Bẫy Short-Circuit:** Trong biểu thức `(a > 0) || (++b > 0)`: Nếu `a > 0` đúng, máy tính **bỏ qua hoàn toàn vế sau**, do đó `b` không hề được tăng lên.
  - **Bẫy `a == b == c`:** Máy tính tính `(a == b)` trước cho ra `true` hoặc `false`, sau đó lấy giá trị boolean đó so sánh tiếp với `c`. Muốn so sánh 3 số bằng nhau, bắt buộc phải viết: `(a == b) && (b == c)`.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"Đơn - 산 - 관 - 논 - 대: Tiền tố đổi trước, hậu tố đổi sau; chia nguyên cắt số, chuỗi Java nhớ gọi equals."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Lần vết chi tiết tiền tố `++x` và hậu tố `x++`:
```c
#include <stdio.h>

int main() {
    int a = 10, b = 10;
    int x, y;

    // Tiền tố (++a): a được tăng lên 11 trước, sau đó mới gán cho x
    x = ++a; 
    printf("x = %d, a = %d\n", x, a); // In ra: x = 11, a = 11

    // Hậu tố (b++): giá trị hiện tại của b (10) được gán cho y trước, sau đó b mới tăng lên 11
    y = b++;
    printf("y = %d, b = %d\n", y, b); // In ra: y = 10, b = 11

    return 0;
}
```

#### 2. Lần vết bẫy lượng giá ngắn mạch (Short-Circuit Evaluation):
```c
#include <stdio.h>

int main() {
    int x = 5, y = 10;

    // Trong phép ||: vế trái (x > 0) là True -> Trình biên dịch không thực thi (++y)
    if (x > 0 || ++y > 10) {
        printf("Dieu kien dung!\n");
    }
    printf("Gia tri y sau bieu thuc: %d\n", y); // Kết quả: y vẫn là 10, không phải 11!

    int m = 0, n = 20;
    // Trong phép &&: vế trái (m != 0) là False -> Trình biên dịch không thực thi (++n)
    if (m != 0 && ++n > 20) {
        printf("Khong bao gio vao day\n");
    }
    printf("Gia tri n sau bieu thuc: %d\n", n); // Kết quả: n vẫn là 20!

    return 0;
}
```

#### 3. Minh họa toán tử tam phân phức hợp (Nested Ternary):
```java
public class TernaryDemo {
    public static void main(String[] args) {
        int score = 85;
        // Toán tử tam phân kết hợp từ phải sang trái:
        // score >= 90 ? "A" : (score >= 80 ? "B" : "C")
        String grade = (score >= 90) ? "A" : (score >= 80) ? "B" : "C";
        System.out.println("Xep loai: " + grade); // In ra: B
    }
}
```

---

### 복습 체크리스트
- [ ] Thuộc lòng thứ tự ưu tiên: **단산관논대** (Đơn vị > Số học > Quan hệ > Logic > Gán).
- [ ] Phân biệt rõ `x = ++a` (tăng rồi gán) và `y = b++` (gán rồi mới tăng).
- [ ] Nắm vững bảng chân trị XOR `^`: Hai bit khác nhau ra 1, giống nhau ra 0.
- [ ] Hiểu rõ cơ chế Short-Circuit: `&&` dừng nếu gặp False, `||` dừng nếu gặp True.
- [ ] Ghi nhớ phép chia 2 số nguyên trong C/Java luôn cắt bỏ phần dư: `7 / 2 = 3`.
- [ ] Phân biệt trong Java: Dùng `.equals()` để so sánh nội dung chuỗi, dùng `==` chỉ so sánh địa chỉ ô nhớ.
