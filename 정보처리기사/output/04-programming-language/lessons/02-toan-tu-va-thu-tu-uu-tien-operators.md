# 연산자 및 연산자 우선순위 (Toán tử & Thứ tự ưu tiên)

## 학습 목표 (Mục tiêu)
- Nắm vững toàn bộ hệ thống toán tử trong C, Java, Python: toán tử số học, toán tử tăng/giảm tiền tố - hậu tố, toán tử quan hệ, toán tử logic, toán tử thao tác bit và toán tử điều kiện tam phân.
- Thuộc lòng thứ tự ưu tiên của các toán tử theo khẩu quyết chuẩn khảo thí **단산관논대** (Đơn hạng > Số học > Quan hệ > Logic > Gán), kèm hướng kết hợp (Associativity: Trái sang Phải hay Phải sang Trái).
- Hiểu rõ cơ chế lượng giá ngắn mạch (단락 평가 - Short-Circuit Evaluation) trong các biểu thức điều kiện chứa `&&` và `||`.
- Thành thạo các phép toán thao tác bit (`&`, `|`, `^`, `~`, `<<`, `>>`, `>>>`), giải thuật bù 2 và công thức đảo bit `~x = -(x + 1)`.
- Phân biệt sự khác nhau giữa toán tử `==` (so sánh địa chỉ ô nhớ) và phương thức `.equals()` (so sánh nội dung chuỗi) trong Java.

## 핵심 키워드 (Từ khóa)
- 연산자 우선순위 (Operator Precedence) — Thứ tự ưu tiên lượng giá toán tử (단산관논대).
- 결합 방향 (Associativity) — Hướng kết hợp Trái sang Phải (L->R) hoặc Phải sang Trái (R->L).
- 증감 연산자 (Increment/Decrement Operators) — Tiền tố `++x` (tăng trước) vs Hậu tố `x++` (dùng trước tăng sau).
- 단락 평가 (Short-Circuit Evaluation) — Ngừng lượng giá nhánh sau khi nhánh trước của `&&` hoặc `||` đã xác định được chân trị.
- 비트 연산자 (Bitwise Operators) — Phép toán bit: AND `&`, OR `|`, XOR `^`, NOT `~`, dịch trái `<<`, dịch phải số học `>>`, dịch phải logic `>>>`.
- 삼항 조건 연산자 (Ternary Operator) — Cú pháp `조건식 ? 참 : 거짓` (hướng kết hợp Phải -> Trái).
- 문자열 비교 (String Comparison in Java) — `==` so sánh tham chiếu Heap vs `equals()` so sánh nội dung.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa từ `01-bien-dinh-danh-va-kieu-du-lieu-c-java.md`, sử dụng các kiểu dữ liệu nguyên thủy (`int`, `char`, `float`, `boolean`) làm toán hạng tính toán.
- **Đang giải quyết gì (Current Problem):** Giải quyết bài toán lượng giá biểu thức phức hợp trong đề thi: Khi một biểu thức chứa đồng thời nhiều loại phép toán, máy tính thực thi phép toán nào trước, quy tắc ép kiểu ngầm định ra sao và bẫy tăng/giảm tiền tố - hậu tố nằm ở đâu.
- **Dùng đi đâu (Forward Handoff):** Các biểu thức điều kiện và phép so sánh logic này là điều kiện cốt lõi để điều khiển các nhánh rẽ và vòng lặp trong bài `04-cau-truc-dieu-khien-re-nhanh-va-vong-lap.md`.

## 읽는 방법 (Cách đọc)
- **Khẩu quyết thứ tự ưu tiên:** Nhớ ngay 5 chữ cái tiếng Hàn: **단·산·관·논·대** (Đơn hạng -> Số học -> Quan hệ -> Logic -> Gán). Ngoặc đơn `( )` luôn có quyền ưu tiên cao nhất.
- **Hướng kết hợp Phải sang Trái (R->L):** Chỉ có 3 nhóm: Toán tử đơn hạng (Unary: `++`, `--`, `!`, `~`), Toán tử ba ngôi (`? :`), và Toán tử gán (`=`, `+=`, `-=`). Mọi toán tử còn lại đều từ Trái sang Phải.
- **Toán tử bit XOR `^`:** Hai bit **khác nhau thì bằng 1**, giống nhau thì bằng 0 ($1 \oplus 0 = 1$, $1 \oplus 1 = 0$, $0 \oplus 0 = 0$).
- **Toán tử đảo bit `~`:** Trong hệ bù 2, giá trị đảo bit của số nguyên `x` luôn bằng `-(x + 1)` (ví dụ: `~5 = -6`, `~(-10) = 9`).
- **Tiền tố vs Hậu tố:** `y = ++x` (tăng `x` lên rồi mới gán cho `y`); `y = x++` (gán giá trị cũ của `x` cho `y` xong mới tăng `x`).

---

## 연산자 및 연산자 우선순위

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `복합 식에서 연산자 우선순위는 괄호()가 가장 높고, 단항 > 산술 > 시프트 > 관계 > 비트 > 논리 > 삼항 > 대입 연산자(단산관논대) 순서로 평가된다. 단항, 삼항, 대입 연산자는 우측에서 좌측(R->L)으로 결합한다. 논리곱(&&)은 앞이 거짓이면 뒤를 평가하지 않고, 논리합(||)은 앞이 참이면 뒤를 평가하지 않는다.`
  - [Tiếng Việt]: Trong biểu thức phức hợp, cặp ngoặc đơn `()` có ưu tiên cao nhất, tiếp theo là Đơn hạng > Số học > Dịch bit > Quan hệ > Bitwise > Logic > Tam phân > Gán (단산관논대). Các toán tử Đơn hạng, Tam phân và Gán kết hợp từ Phải sang Trái (R->L). Phép `&&` dừng tính nếu vế trái False; phép `||` dừng tính nếu vế trái True.

- **1. Bảng thứ tự ưu tiên toán tử đầy đủ (연산자 우선순위 및 결합 방향):**

| Cấp ưu tiên | Nhóm toán tử | Ký hiệu phép toán | Hướng kết hợp |
| :---: | :--- | :--- | :---: |
| **1 (Cao nhất)** | Ngoặc & Truy xuất | `()`, `[]`, `.`, `->` | Trái -> Phải |
| **2 (Đơn hạng - 단)**| Unary / Đơn vị | `++`, `--`, `+` (dương), `-` (âm), `!`, `~`, `sizeof`, `(type)` | **Phải -> Trái** |
| **3 (Số học - Nhân chia)**| Nhân, chia, lấy dư | `*`, `/`, `%` | Trái -> Phải |
| **4 (Số học - Cộng trừ)**| Cộng, trừ | `+`, `-` | Trái -> Phải |
| **5 (Dịch bit)** | Shift bit | `<<`, `>>`, `>>>` (Java không dấu) | Trái -> Phải |
| **6 (Quan hệ - Thứ tự)**| So sánh lớn nhỏ | `<`, `<=`, `>`, `>=` | Trái -> Phải |
| **7 (Quan hệ - Bằng)** | So sánh bằng nhau | `==`, `!=` | Trái -> Phải |
| **8 (Bitwise AND)** | Thao tác bit AND | `&` | Trái -> Phải |
| **9 (Bitwise XOR)** | Thao tác bit XOR | `^` | Trái -> Phải |
| **10 (Bitwise OR)** | Thao tác bit OR | `\|` | Trái -> Phải |
| **11 (Logic AND)** | Logic AND | `&&` | Trái -> Phải |
| **12 (Logic OR)** | Logic OR | `\|\|` | Trái -> Phải |
| **13 (Tam phân)** | Điều kiện 3 ngôi | `? :` | **Phải -> Trái** |
| **14 (Gán - 대)** | Gán & Gán phức | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, `&=`, `^=`, `\|=` | **Phải -> Trái** |
| **15 (Thấp nhất)**| Dấu phẩy | `,` | Trái -> Phải |

- **2. Bảng quy tắc toán tử thao tác bit (비트 연산자):**

| Toán tử bit | Tên gọi | Bản chất xử lý bit | Ví dụ minh họa |
| :---: | :--- | :--- | :--- |
| `&` | Bitwise AND | Cả 2 bit đều bằng 1 thì kết quả là 1; ngược lại bằng 0. | `5 & 3` (`101 & 011` -> `001` = **1**) |
| `\|` | Bitwise OR | Chỉ cần 1 trong 2 bit bằng 1 thì kết quả là 1. | `5 \| 3` (`101 \| 011` -> `111` = **7**) |
| `^` | Bitwise XOR | **Hai bit khác nhau thì bằng 1**, giống nhau thì bằng 0. | `5 ^ 3` (`101 ^ 011` -> `110` = **6**) |
| `~` | Bitwise NOT | Đảo bit (bù 1): `~x = -(x + 1)`. | `~5` -> **-6**; `~(-10)` -> **9** |
| `<<` | Left Shift | Dịch bit sang trái $k$ bit, tương đương nhân với $2^k$. | `3 << 2` ($3 \times 2^2$ = **12**) |
| `>>` | Right Shift | Dịch bit sang phải $k$ bit có dấu (giữ nguyên bit dấu). | `-16 >> 2` (kết quả = **-4**) |
| `>>>` | Unsigned Right Shift | Dịch phải không dấu (chỉ có trong Java), luôn chèn 0 vào đầu. | `-1 >>> 28` (cho ra số dương lớn) |

- **3. Bảng cơ chế lượng giá đoản mạch (단락 평가 - Short-Circuit Evaluation):**

| Phép toán | Biểu thức tổng quát | Điều kiện kích hoạt đoản mạch | Hành vi của Runtime | Giá trị trả về |
| :---: | :--- | :--- | :--- | :---: |
| **`&&` (AND)** | `A && B` | `A == false` | **Bỏ qua vế `B`**, không thực thi các hàm hay phép `++` trong `B` | `false` |
| **`\|\|` (OR)**| `A \|\| B` | `A == true` | **Bỏ qua vế `B`**, không thực thi các hàm hay phép `++` trong `B` | `true` |

- **4. Đối chiếu so sánh chuỗi trong Java (`==` vs `.equals()`):**

| Cú pháp kiểm tra | Kết quả trả về | Cơ chế kỹ thuật |
| :--- | :---: | :--- |
| `new String("A") == new String("A")` | **`false`** | Toán tử `==` so sánh **địa chỉ ô nhớ Heap**; 2 lệnh `new` tạo ra 2 ô nhớ khác nhau. |
| `str1.equals(str2)` | **`true`** | Phương thức `.equals()` so sánh **từng ký tự nội dung bên trong**. |
| `"A" == "A"` | **`true`** | Java tự động tối ưu hóa hằng số chuỗi vào **String Constant Pool**. |

- **주의/함정 (Bẫy đề thi):**
  - **Bẫy chia nguyên:** Trong C/Java, `5 / 2` cho kết quả là **`2`** (cắt bỏ phần thập phân), chứ không phải `2.5`. Muốn có `2.5` phải viết `5.0 / 2` hoặc `(double)5 / 2`.
  - **Bẫy Short-Circuit:** Trong biểu thức `(a > 0) || (++b > 0)`: Nếu `a > 0` đúng, máy tính **bỏ qua hoàn toàn vế sau**, do đó `b` không hề được tăng lên.
  - **Toán tử tam phân lồng nhau:** `a ? b : c ? d : e` được kết hợp từ phải sang trái: `a ? b : (c ? d : e)`.
  - **Độ ưu tiên giữa `&` và `==`:** Phép so sánh quan hệ `==` ưu tiên cao hơn phép thao tác bit `&`. Do đó `if (flags & 1 == 0)` sẽ bị hiểu thành `flags & (1 == 0)` -> Luôn phải đóng ngoặc: `(flags & 1) == 0`.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"Đơn - 산 - 관 - 논 - 대: Tiền tố đổi trước, hậu tố đổi sau; đoản mạch bỏ vế sau nếu vế trước đã chốt chân trị."*

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

#### 2. Phân tích bài toán thi kinh điển: Lượng giá biểu thức đoản mạch (Short-Circuit):
```c
#include <stdio.h>

int main() {
    int x = 5, y = 10;

    // Trong phép ||: vế trái (x > 0) là True -> Trình biên dịch không thực thi (++y)
    if (x > 0 || ++y > 10) {
        printf("Dieu kien || dung!\n");
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

**Bảng Trace trạng thái biến:**

| Bước | Biểu thức | Vế trái | Kết quả vế trái | Có thực thi vế phải không? | Giá trị biến sau biểu thức |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `(x > 0) \|\| (++y > 10)` | `5 > 0` | `true` | **KHÔNG** (Đoản mạch OR) | `x = 5, y = 10` |
| 2 | `(m != 0) && (++n > 20)` | `0 != 0` | `false` | **KHÔNG** (Đoản mạch AND) | `m = 0, n = 20` |

#### 3. Minh họa toán tử tam phân và biểu thức thao tác bit phức hợp:
```c
#include <stdio.h>

int main() {
    int a = 12; // Nhị phân: 0000 1100
    int b = 10; // Nhị phân: 0000 1010

    int and_res = a & b; // 0000 1000 = 8
    int or_res  = a | b; // 0000 1110 = 14
    int xor_res = a ^ b; // 0000 0110 = 6
    int not_res = ~a;    // -(12 + 1) = -13

    printf("AND: %d, OR: %d, XOR: %d, NOT: %d\n", and_res, or_res, xor_res, not_res);

    // Toán tử tam phân lồng nhau tính điểm xếp hạng
    int score = 85;
    char grade = (score >= 90) ? 'A' : (score >= 80) ? 'B' : 'C';
    printf("Grade: %c\n", grade); // In ra: B

    return 0;
}
```

---

### 복습 체크리스트
- [ ] Thuộc lòng thứ tự ưu tiên: **단산관논대** (Đơn vị > Số học > Quan hệ > Logic > Gán).
- [ ] Ghi nhớ 3 nhóm kết hợp Phải sang Trái (R->L): Toán tử đơn vị, Toán tử ba ngôi, Toán tử gán.
- [ ] Phân biệt rõ `x = ++a` (tăng rồi gán) và `y = b++` (gán rồi mới tăng).
- [ ] Nắm vững bảng chân trị XOR `^`: Hai bit khác nhau ra 1, giống nhau ra 0.
- [ ] Ghi nhớ công thức đảo bit bù hai: `~x = -(x + 1)`.
- [ ] Hiểu rõ cơ chế Short-Circuit: `&&` dừng nếu gặp False, `||` dừng nếu gặp True.
- [ ] Ghi nhớ phép chia 2 số nguyên trong C/Java luôn cắt bỏ phần dư: `7 / 2 = 3`.
- [ ] Phân biệt trong Java: Dùng `.equals()` để so sánh nội dung chuỗi, dùng `==` chỉ so sánh địa chỉ ô nhớ.
