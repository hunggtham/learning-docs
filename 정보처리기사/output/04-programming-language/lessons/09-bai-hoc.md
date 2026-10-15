# 연산자 심화 (Operators - Advanced)

## 학습 목표 (Mục tiêu)
- Nắm vững bản chất xử lý của các toán tử quan hệ (관계 연산자) trong ngôn ngữ C: quy ước số 0 là Sai (False) và mọi số khác 0 đều được coi là Đúng (True, mặc định trả về 1 khi so sánh đúng).
- Hiểu rõ cơ chế và cú pháp của các toán tử gán phức hợp (복합 대입 연산자 - Compound Assignment Operators): `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`.
- Phân tích chính xác thứ tự thực thi biểu thức phức tạp có chứa hiệu ứng phụ (Side Effects) và quy tắc kết hợp từ phải sang trái của toán tử gán.

## 핵심 키워드 (Từ khóa)
- 관계 연산자 (Relational Operators / `==`, `!=`, `>`, `<`, `>=`, `<=`)
- 참과 거짓 (True & False / C언어의 0과 1)
- 복합 대입 연산자 (Compound Assignment / `+=`, `-=`, `*=`, `%=`)
- 비트 복합 대입 (Bitwise Compound / `<<=`, `>>=`, `&=`, `^=`, `|=`)
- 부수 효과 (Side Effect / 변수 값의 변경)
- 우측 결합 (Right-to-Left Associativity)

## 선행·연결 개념 (Kiến thức liên kết)
- [08-bai-hoc.md](08-bai-hoc.md): Các nhóm toán tử cơ bản và thứ tự ưu tiên.
- [10-bai-hoc.md](10-bai-hoc.md): Tổng hợp toàn diện toán tử và bài tập vận dụng.
- [03-bai-hoc.md](03-bai-hoc.md): Kiểu dữ liệu, biến và toán tử.

## 읽는 방법 (Cách đọc)
- Phân biệt hai mảng trọng tâm:
  - **Quy ước Chân trị trong ngôn ngữ C:**
    - Không giống Java có kiểu `boolean` độc lập, ngôn ngữ C biểu diễn chân lý bằng số: **Số `0` là Sai (False)**; **Bất kỳ số nào khác `0` (dù là số âm như `-1` hay số dương như `100`) đều được coi là Đúng (True)**.
    - Kết quả của các phép so sánh quan hệ trong C luôn trả về giá trị số nguyên: đúng trả về `1`, sai trả về `0`.
  - **Toán tử gán phức hợp:**
    - Biểu thức `A op= B` tương đương với `A = A op (B)`. Chú ý vế $B$ luôn được tính toán hoàn chỉnh trước khi áp dụng phép toán gán `op`.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng toán tử gán phức hợp (Compound Assignment Operators):**

| Toán tử | Cú pháp viết tắt | Biểu thức tương đương đầy đủ | Ví dụ tính toán với $a = 10$ |
| :--- | :--- | :--- | :--- |
| **`+=`** | `a += b` | `a = a + b` | `a += 5` $\rightarrow$ $a = 10 + 5 = 15$ |
| **`-=`** | `a -= b` | `a = a - b` | `a -= 3` $\rightarrow$ $a = 10 - 3 = 7$ |
| **`*=`** | `a *= b` | `a = a * b` | `a *= 2` $\rightarrow$ $a = 10 \times 2 = 20$ |
| **`/=`** | `a /= b` | `a = a / b` | `a /= 4` $\rightarrow$ $a = 10 / 4 = 2$ (chia nguyên) |
| **`%=`** | `a %= b` | `a = a % b` | `a %= 4` $\rightarrow$ $a = 10 \pmod 4 = 2$ |
| **`<<=`** | `a <<= b` | `a = a << b` | `a <<= 1` $\rightarrow$ $a = 10 \times 2^1 = 20$ |
| **`>>=`** | `a >>= b` | `a = a >> b` | `a >>= 1` $\rightarrow$ $a = 10 / 2^1 = 5$ |
| **`&=`** | `a &= b` | `a = a & b` | `a &= 3` $\rightarrow$ $1010_2 \ \& \ 0011_2 = 0010_2 = 2$ |
| **`^=`** | `a ^= b` | `a = a ^ b` | `a ^= 3` $\rightarrow$ $1010_2 \ \hat{} \ 0011_2 = 1001_2 = 9$ |
| **`\|=`** | `a \|= b` | `a = a \| b` | `a \|= 3` $\rightarrow$ $1010_2 \ \| \ 0011_2 = 1011_2 = 11$ |

- **Bẫy thứ tự ưu tiên trong toán tử gán phức hợp:**
  - *Ví dụ:* `a *= b + 3` với $a = 5, b = 2$.
  - Cách tính đúng: Phép cộng `b + 3` được tính trước vì toán tử số học có độ ưu tiên cao hơn toán tử gán $\rightarrow$ `b + 3 = 5`.
  - Sau đó mới tính: `a = a * 5 = 5 * 5 = 25`.
  - *(Sai lầm phổ biến là hiểu nhầm thành `a = a * b + 3 = 5 * 2 + 3 = 13` - SAI).*

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Chuỗi gán liên tiếp (Chained Assignment):**
  - Trong biểu thức `x = y = z = 10;`, hướng kết hợp của toán tử gán là **từ phải sang trái ($\leftarrow$)**.
  - Bước 1: $z = 10$.
  - Bước 2: $y = z$ (nhận 10).
  - Bước 3: $x = y$ (nhận 10).
  - Tất cả các biến đều nhận giá trị 10.

### 복습 체크리스트
- [ ] Nhớ trong C: Số 0 là Sai, mọi số khác 0 (kể cả số âm) đều là Đúng.
- [ ] Tính đúng phép toán gán phức hợp: `a *= b + c` tương đương `a = a * (b + c)`.
- [ ] Nhớ toán tử gán có hướng kết hợp từ phải sang trái.
- [ ] Phân biệt được phép so sánh bằng `==` và phép gán `=`.
