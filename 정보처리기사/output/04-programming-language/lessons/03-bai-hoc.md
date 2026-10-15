# 072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)

## 학습 목표 (Mục tiêu)
- Nắm vững các kiểu dữ liệu cơ bản (Data Types), quy tắc khai báo biến và các nhóm toán tử cốt lõi trong ngôn ngữ lập trình C và Java.
- Phân biệt sự khác biệt then chốt giữa toán tử tăng giảm tiền tố (전치 증감 연산자: `++A`, `--A`) và toán tử tăng giảm hậu tố (후치 증감 연산자: `A++`, `A--`).
- Nắm vững cách tính toán và thứ tự ưu tiên của toán tử số học, toán tử quan hệ, toán tử logic và toán tử điều kiện ba ngôi (삼항 조건 연산자).

## 핵심 키워드 (Từ khóa)
- 데이터 타입 (Data Types / int, float, char, boolean)
- 산술 연산자 (Arithmetic Operators / `+`, `-`, `*`, `/`, `%`)
- 전치 연산자 vs 후치 연산자 (Prefix `++A` vs Postfix `A++`)
- 관계 연산자 (Relational Operators / `==`, `!=`, `>`, `<`, `>=`, `<=`)
- 논리 연산자 (Logical Operators / `&&`, `||`, `!`)
- 삼항 조건 연산자 (Ternary Operator / `? :`)

## 선행·연결 개념 (Kiến thức liên kết)
- [02-bai-hoc.md](02-bai-hoc.md): Kiểu chuỗi dữ liệu trong Python và kiểu dữ liệu Java.
- [04-bai-hoc.md](04-bai-hoc.md): Kích thước chi tiết các kiểu dữ liệu trong C/C++.
- [08-bai-hoc.md](08-bai-hoc.md): Tổng hợp chi tiết các nhóm toán tử và thứ tự ưu tiên.

## 읽는 방법 (Cách đọc)
- Phân biệt rõ hai cơ chế tăng giảm (Bẫy thi cực phổ biến trong đề thi Code C/Java):
  - **전치 (Prefix: `++a`):** Tăng giá trị lên 1 TRƯỚC, rồi mới lấy giá trị mới đó đi tính toán trong biểu thức.
  - **후치 (Postfix: `a++`):** Lấy giá trị HIỆN TẠI đi tính toán biểu thức trước, tính xong toàn bộ câu lệnh mới tăng giá trị lên 1.
  - Ví dụ:
    ```c
    int a = 5, b, c;
    b = ++a; // a tăng lên 6 trước -> b = 6
    c = a++; // c nhận giá trị a hiện tại là 6 -> sau đó a tăng lên 7
    ```

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp các nhóm toán tử cốt lõi:**

| Nhóm toán tử | Ký hiệu | Ý nghĩa thao tác | Ví dụ cú pháp và kết quả |
| :--- | :--- | :--- | :--- |
| **산술 (Số học)** | `+`, `-`, `*` | Cộng, trừ, nhân thông thường | `5 * 2 = 10` |
|  | `/` | Phép chia lấy phần nguyên (với số nguyên) | `7 / 2 = 3` (bỏ phần thập phân) |
|  | `%` | **Phép chia lấy phần dư** (Chỉ dùng cho số nguyên) | `7 % 3 = 1` |
| **증감 (Tăng giảm)** | `++A`, `--A` | **Tiền tố:** Tăng/giảm trước khi định giá biểu thức | `x = 5; y = ++x;` $\rightarrow$ $x=6, y=6$ |
|  | `A++`, `A--` | **Hậu tố:** Định giá biểu thức xong mới tăng/giảm | `x = 5; y = x++;` $\rightarrow$ $x=6, y=5$ |
| **관계 (Quan hệ)** | `==`, `!=` | So sánh bằng, so sánh khác | `5 == 5` trả về Đúng (1/true) |
|  | `>`, `<`, `>=`, `<=` | So sánh lớn hơn, nhỏ hơn | `3 < 5` trả về Đúng (1/true) |
| **논리 (Logic)** | `&&` | Phép VÀ (AND): Cả hai vế đều đúng mới đúng | `(3 < 5) && (2 > 1)` $\rightarrow$ true |
|  | `\|\|` | Phép HOẶC (OR): Chỉ cần một vế đúng là đúng | `(3 > 5) \|\| (2 > 1)` $\rightarrow$ true |
|  | `!` | Phép PHỦ ĐỊNH (NOT): Đổi đúng thành sai, sai thành đúng | `!(3 > 5)` $\rightarrow$ true |
| **삼항 조건 (Ba ngôi)** | `조건 ? 참 : 거짓` | Nếu điều kiện đúng chọn vế trước `:`, sai chọn vế sau `:` | `max = (a > b) ? a : b;` |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Quy tắc ép kiểu tự động (Type Promotion):**
  - Khi thực hiện phép toán giữa các kiểu dữ liệu khác nhau, kiểu nhỏ hơn sẽ tự động được ép lên kiểu lớn hơn trước khi tính toán: `int + double` sẽ cho kết quả là `double`.
  - Phép chia hai số nguyên trong C/Java `5 / 2` luôn trả về số nguyên `2`. Muốn lấy kết quả thực `2.5`, phải ép kiểu ít nhất một toán hạng: `(double)5 / 2` hoặc `5.0 / 2`.

### 복습 체크리스트
- [ ] Phân biệt được Prefix (`++a`: tăng trước) và Postfix (`a++`: tăng sau).
- [ ] Nhớ toán tử `%` chỉ áp dụng cho số nguyên và trả về phần dư.
- [ ] Nhớ phép chia số nguyên `7 / 2` trong C/Java bằng 3 (cắt phần thập phân).
- [ ] Viết thành thạo cấu trúc toán tử ba ngôi `(điều kiện) ? (nếu đúng) : (nếu sai)`.
