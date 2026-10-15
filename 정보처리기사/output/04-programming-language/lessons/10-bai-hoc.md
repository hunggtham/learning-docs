# 239 - 243. 연산자 (Operators)

## 학습 목표 (Mục tiêu)
- Tổng hợp toàn diện kiến thức về 5 nhóm toán tử cơ bản trong lập trình: Toán tử số học, Toán tử quan hệ, Toán tử bitwise, Toán tử logic, và Toán tử gán.
- Rèn luyện kỹ năng phân tích và lần vết từng bước (Trace) các biểu thức phức tạp lồng ghép nhiều loại toán tử khác nhau trong đề thi Kỹ sư xử lý thông tin.
- Nhận diện các bẫy đề thi kinh điển: Tiền tố vs Hậu tố, Phép chia số nguyên, Phép chia lấy phần dư, và Hiện tượng đoản mạch trong biểu thức logic.

## 핵심 키워드 (Từ khóa)
- 연산자 종합 정리 (Operators Synthesis)
- 산술 연산자 (Arithmetic / 사칙연산, `%`, `++`, `--`)
- 관계 연산자 (Relational / `==`, `!=`, `>`, `<`)
- 비트 연산자 (Bitwise / `&`, `|`, `^`, `~`)
- 논리 연산자 (Logical / `&&`, `||`, `!`)
- 대입 연산자 (Assignment / `=`, `+=`, `-=`)
- 식의 평가 순서 (Expression Evaluation Order)

## 선행·연결 개념 (Kiến thức liên kết)
- [08-bai-hoc.md](08-bai-hoc.md): Thứ tự ưu tiên của các nhóm toán tử.
- [09-bai-hoc.md](09-bai-hoc.md): Toán tử nâng cao - Quan hệ và gán phức hợp.
- [11-bai-hoc.md](11-bai-hoc.md): Cấu trúc điều khiển rẽ nhánh (if, switch-case).

## 읽는 방법 (Cách đọc)
- Ôn tập hệ thống 5 nhóm toán tử qua bảng tra cứu nhanh:
  - **Nhóm 1 (Số học):** `+`, `-`, `*`, `/` (chia lấy nguyên), `%` (chia lấy dư), `++`/`--` (tăng giảm).
  - **Nhóm 2 (Quan hệ):** `==` (bằng), `!=` (khác), `>`, `<`, `>=`, `<=`. Trong C, kết quả trả về `1` (đúng) hoặc `0` (sai).
  - **Nhóm 3 (Bit):** Xử lý từng bit nhị phân `&` (cả 2 bằng 1), `|` (1 trong 2 bằng 1), `^` (khác nhau là 1), `~` (đảo bit).
  - **Nhóm 4 (Logic):** `&&` (VÀ), `||` (HOẶC), `!` (PHỦ ĐỊNH).
  - **Nhóm 5 (Gán):** `=`, `+=`, `-=`, `*=`... thực hiện tính toán vế phải rồi gán ngược vào biến vế trái.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp tra cứu nhanh 5 nhóm toán tử:**

| Nhóm toán tử | Toán tử cụ thể | Quy tắc tính toán chuẩn | Bẫy đề thi cần cảnh giác |
| :--- | :--- | :--- | :--- |
| **1. 산술 (Số học)** | `+`, `-`, `*`, `/`, `%`, `++`, `--` | Phép chia hai số nguyên cắt bỏ phần thập phân; `%` chỉ dùng cho số nguyên | Phân biệt tiền tố `++a` (tăng trước) và hậu tố `a++` (tăng sau) |
| **2. 관계 (Quan hệ)** | `==`, `!=`, `>`, `<`, `>=`, `<=` | So sánh hai giá trị; trả về Đúng (1/true) hoặc Sai (0/false) | Nhầm lẫn giữa so sánh bằng `==` và phép gán `=` |
| **3. 비트 (Bitwise)** | `&`, `\|`, `^`, `~`, `<<`, `>>` | Thao tác trên từng bit nhị phân; `^` (XOR) bằng 1 khi hai bit khác nhau | Quên đổi số thập phân sang nhị phân trước khi tính |
| **4. 논리 (Logic)** | `&&`, `\|\|`, `!` | Thao tác trên giá trị chân lý Đúng/Sai | Hiện tượng đoản mạch: `A && B` bỏ qua $B$ nếu $A$ sai |
| **5. 대입 (Gán)** | `=`, `+=`, `-=`, `*=`, `/=`, `%=` | `a op= b` tương đương `a = a op (b)` | Vế phải `(b)` luôn được ưu tiên tính xong trước khi gán |

- **Bài toán lần vết biểu thức tổng hợp chuẩn đề thi:**
  - *Đoạn mã C:*
    ```c
    int a = 5, b = 10, c = 15, res;
    res = ++a + b-- * (c % 4);
    ```
  - *Quá trình lần vết từng bước:*
    1. Ưu tiên trong ngoặc: `c % 4` $= 15 \pmod 4 = 3$.
    2. Toán tử tiền tố `++a`: Biến $a$ tăng ngay từ 5 lên 6; giá trị dùng là 6.
    3. Phép nhân `*`: Toán tử hậu tố `b--` lấy giá trị hiện tại là 10 để nhân với 3 $\rightarrow$ $10 \times 3 = 30$. (Sau đó $b$ giảm xuống 9).
    4. Phép cộng `+`: Lấy 6 cộng với 30 $\rightarrow$ $\text{res} = 36$.
    5. Kết quả cuối cùng: `a = 6`, `b = 9`, `c = 15`, `res = 36`.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Quy tắc chuyển đổi kiểu ngầm định (Implicit Type Conversion):**
  - Thứ tự chuyển đổi ưu tiên: `char`, `short` $\rightarrow$ `int` $\rightarrow$ `unsigned int` $\rightarrow$ `long` $\rightarrow$ `float` $\rightarrow$ `double`.
  - Trong biểu thức có cả số thực và số nguyên, số nguyên sẽ tự động chuyển đổi thành số thực để giữ độ chính xác cao nhất.

### 복습 체크리스트
- [ ] Phân biệt rõ sự khác nhau giữa toán tử logic `&&`, `||` và toán tử bit `&`, `|`.
- [ ] Tính đúng phép tính kết hợp: `++a + b-- * (c % 4)`.
- [ ] Nhớ trong C: `5 / 2 = 2` và `5 % 2 = 1`.
- [ ] Nhớ quy tắc chuyển đổi kiểu dữ liệu từ nhỏ sang lớn khi tính toán.
