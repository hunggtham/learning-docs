# 연산자 (Operators)

## 학습 목표 (Mục tiêu)
- Nắm vững toàn bộ các nhóm toán tử trong ngôn ngữ lập trình C và Java: Toán tử số học, Toán tử bitwise, Toán tử logic, Toán tử điều kiện ba ngôi và Toán tử gán.
- Hiểu rõ cơ chế thao tác trên từng bit nhị phân của các toán tử bit: AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), Dịch trái (`<<`) và Dịch phải (`>>`).
- Nắm vững chuỗi thứ tự ưu tiên của các toán tử (연산자 우선순위 - Operator Precedence) để giải chính xác các câu hỏi tính toán biểu thức phức tạp trong đề thi.

## 핵심 키워드 (Từ khóa)
- 연산자 우선순위 (Operator Precedence)
- 산술 연산자 (Arithmetic Operators / `%`, `++`, `--`)
- 비트 연산자 (Bitwise Operators / `&`, `|`, `^`, `~`, `<<`, `>>`)
- 배타적 논리합 (XOR / 다르면 1, 같으면 0)
- 논리 연산자 (Logical Operators / `&&`, `||`, `!`)
- 단항 연산자 (Unary Operators / 최우선 순위)
- 결합 규칙 (Associativity / 좌측 결합 vs 우측 결합)

## 선행·연결 개념 (Kiến thức liên kết)
- [07-bai-hoc.md](07-bai-hoc.md): Quy tắc đặt tên biến và các phong cách định danh.
- [09-bai-hoc.md](09-bai-hoc.md): Toán tử nâng cao - Quan hệ và gán phức hợp.
- [03-bai-hoc.md](03-bai-hoc.md): Cơ bản về các kiểu dữ liệu và toán tử.

## 읽는 방법 (Cách đọc)
- Ghi nhớ câu thần chú thứ tự ưu tiên toán tử từ cao xuống thấp:
  $$\text{Đơn} \rightarrow \text{Số} \rightarrow \text{Dịch} \rightarrow \text{Quan} \rightarrow \text{Bit} \rightarrow \text{Logic} \rightarrow \text{Điều} \rightarrow \text{Gán} \rightarrow \text{Phẩy}$$
  - **Đơn (단항):** `!`, `~`, `++`, `--`, `sizeof` (Ưu tiên cao nhất).
  - **Số (산술):** Nhân, chia, phần dư (`*`, `/`, `%`) rồi đến cộng, trừ (`+`, `-`).
  - **Dịch (시프트):** Dịch bit trái/phải (`<<`, `>>`).
  - **Quan (관계):** So sánh lớn bé (`<`, `<=`, `>`, `>=`) rồi đến bằng, khác (`==`, `!=`).
  - **Bit (비트):** Theo thứ tự `&` (AND) $\rightarrow$ `^` (XOR) $\rightarrow$ `|` (OR).
  - **Logic (논리):** `&&` (AND) trước, `||` (OR) sau.
  - **Điều (조건):** Toán tử ba ngôi `? :`.
  - **Gán (대입):** `=`, `+=`, `-=`... (Tính từ phải sang trái).
  - **Phẩy (콤마):** `,` (Thấp nhất).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng thao tác của các toán tử Bitwise (Toán tử mức bit):**

| Toán tử bit | Tên gọi | Quy tắc tính trên từng cặp bit | Ví dụ minh họa nhị phân |
| :--- | :--- | :--- | :--- |
| **`&`** | **Bitwise AND** | Chỉ bằng **1 khi cả hai bit đều là 1**; còn lại bằng 0 | $5 \ \& \ 3 \ (0101_2 \ \& \ 0011_2) = 0001_2 = 1$ |
| **`\|`** | **Bitwise OR** | Chỉ cần **một trong hai bit bằng 1 là bằng 1** | $5 \ \| \ 3 \ (0101_2 \ \| \ 0011_2) = 0111_2 = 7$ |
| **`^`** | **Bitwise XOR** | **Khác nhau thì bằng 1, giống nhau thì bằng 0** | $5 \ \hat{} \ 3 \ (0101_2 \ \hat{} \ 0011_2) = 0110_2 = 6$ |
| **`~`** | **Bitwise NOT** | Đảo ngược từng bit: 0 thành 1, 1 thành 0 (Đơn vị) | $\sim 5 = -6$ (Hệ bù 2) |
| **`<<`** | **Left Shift** | Dịch các bit sang trái $k$ vị trí (Tương đương nhân với $2^k$) | $5 \ll 2 = 5 \times 2^2 = 20$ |
| **`>>`** | **Right Shift** | Dịch các bit sang phải $k$ vị trí (Tương đương chia cho $2^k$) | $20 \gg 2 = 20 / 2^2 = 5$ |

- **Bảng tổng hợp thứ tự ưu tiên toán tử (Cao $\rightarrow$ Thấp):**

| Cấp ưu tiên | Nhóm toán tử | Danh sách toán tử cụ thể | Hướng kết hợp (Associativity) |
| :--- | :--- | :--- | :--- |
| **1 (Cao nhất)** | **단항 (Unary)** | `!`, `~`, `++`, `--`, `+` (dương), `-` (âm), `(type)`, `sizeof` | Phải sang trái ($\leftarrow$) |
| **2** | **산술 (Nhân chia)** | `*`, `/`, `%` | Trái sang phải ($\rightarrow$) |
| **3** | **산술 (Cộng trừ)** | `+`, `-` | Trái sang phải ($\rightarrow$) |
| **4** | **시프트 (Shift)** | `<<`, `>>` | Trái sang phải ($\rightarrow$) |
| **5** | **관계 (So sánh)** | `<`, `<=`, `>`, `>=` | Trái sang phải ($\rightarrow$) |
| **6** | **관계 (Đẳng thức)** | `==`, `!=` | Trái sang phải ($\rightarrow$) |
| **7** | **비트 AND** | `&` | Trái sang phải ($\rightarrow$) |
| **8** | **비트 XOR** | `^` | Trái sang phải ($\rightarrow$) |
| **9** | **비트 OR** | `\|` | Trái sang phải ($\rightarrow$) |
| **10** | **논리 AND** | `&&` | Trái sang phải ($\rightarrow$) |
| **11** | **논리 OR** | `\|\|` | Trái sang phải ($\rightarrow$) |
| **12** | **조건 (Ba ngôi)** | `? :` | Phải sang trái ($\leftarrow$) |
| **13** | **대입 (Gán)** | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=` | Phải sang trái ($\leftarrow$) |
| **14 (Thấp nhất)**| **순서 (Phẩy)** | `,` | Trái sang phải ($\rightarrow$) |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Hiện tượng đoản mạch trong logic (Short-Circuit Evaluation):**
  - Trong biểu thức `A && B`: Nếu $A$ đã sai (false), ngôn ngữ lập trình sẽ **bỏ qua hoàn toàn vế $B$ không thèm tính** (vì chắc chắn cả biểu thức là false).
  - Trong biểu thức `A || B`: Nếu $A$ đã đúng (true), hệ thống sẽ **bỏ qua không tính vế $B$** (vì chắc chắn cả biểu thức là true).
  - Nếu trong vế $B$ có chứa toán tử tăng giảm (ví dụ: `(a > 0) || (++b > 0)`), biến $b$ có thể sẽ không được tăng nếu $a > 0$ là true. Đây là bẫy tính điểm số cực kỳ nổi tiếng trong đề thi.

### 복습 체크리스트
- [ ] Nhớ thứ tự ưu tiên: Đơn $\rightarrow$ Số $\rightarrow$ Dịch $\rightarrow$ Quan $\rightarrow$ Bit $\rightarrow$ Logic $\rightarrow$ Điều $\rightarrow$ Gán.
- [ ] Tính thành thạo phép XOR (`^`): Hai bit khác nhau ra 1, giống nhau ra 0.
- [ ] Nhớ phép dịch bit: `a << n` bằng $a \times 2^n$, `a >> n` bằng $a / 2^n$.
- [ ] Nắm được bẫy Short-Circuit Evaluation trong phép toán `&&` và `||`.
