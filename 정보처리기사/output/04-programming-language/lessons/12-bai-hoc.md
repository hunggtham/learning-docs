# 245. 연산자 우선순위 (Operator Precedence)

## 학습 목표 (Mục tiêu)
- Nắm vững quy tắc và chuỗi thứ tự ưu tiên (연산자 우선순위 - Operator Precedence) khi trong một biểu thức chứa nhiều loại toán tử đan xen nhau.
- Ghi nhớ thần chú thi cử tiếng Hàn **단산관논대** (Đơn $\rightarrow$ Toán $\rightarrow$ Quan $\rightarrow$ Luận $\rightarrow$ Gán) cùng bảng ưu tiên chi tiết.
- Hiểu vai trò tuyệt đối của dấu ngoặc đơn `()` như công cụ cưỡng chế thứ tự thực thi có độ ưu tiên cao nhất trong mọi ngôn ngữ lập trình.

## 핵심 키워드 (Từ khóa)
- 연산자 우선순위 (Operator Precedence)
- 단산관논대 (Mnemonic: 단항 > 산술 > 관계 > 논리 > 대입)
- 괄호 연산자 (Parentheses `()` / 최우선)
- 단항 연산자 (Unary Operators / `!`, `~`, `++`, `--`)
- 결합 방향 (Associativity / 좌 $\rightarrow$ 우 vs 우 $\rightarrow$ 좌)
- 수식 평가 (Expression Evaluation)

## 선행·연결 개념 (Kiến thức liên kết)
- [11-bai-hoc.md](11-bai-hoc.md): Toán tử điều kiện ba ngôi.
- [13-bai-hoc.md](13-bai-hoc.md): Các hàm nhập xuất cơ bản trong C và Java.
- [08-bai-hoc.md](08-bai-hoc.md): Bảng chi tiết toàn bộ các nhóm toán tử.

## 읽는 방법 (Cách đọc)
- Học theo thần chú 5 âm tiết kinh điển của kỳ thi kỹ sư:
  $$\mathbf{단} \rightarrow \mathbf{산} \rightarrow \mathbf{관} \rightarrow \mathbf{논} \rightarrow \mathbf{대}$$
  1. **단 (Đơn - 단항):** `!`, `~`, `++`, `--` (Toán tử 1 ngôi thực hiện trước).
  2. **산 (Toán - 산술):** `*`, `/`, `%` rồi đến `+`, `-` (Nhân chia trước, cộng trừ sau).
  3. **관 (Quan - 관계):** `<`, `<=`, `>`, `>=` rồi đến `==`, `!=` (So sánh lớn bé trước, so sánh bằng khác sau).
  4. **논 (Luận - 논리):** `&&` (VÀ) trước, `||` (HOẶC) sau.
  5. **대 (Gán - 대입):** `=`, `+=`, `-=`... (Tính hết vế phải rồi mới gán sang trái).
  - *Lưu ý:* Dấu ngoặc `()` luôn đứng đầu bảng tuyệt đối, phá vỡ mọi quy tắc ưu tiên thông thường.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng phân cấp thứ tự ưu tiên cốt lõi (단산관논대):**

| Cấp bậc ưu tiên | Nhóm toán tử (Tiếng Hàn) | Ký hiệu toán tử | Hướng thực thi |
| :--- | :--- | :--- | :--- |
| **Ưu tiên tuyệt đối** | **괄호 (Ngoặc đơn)** | `( )` | Từ trong ra ngoài |
| **Cấp 1** | **단항 (Đơn nguyên)** | `!`, `~`, `++`, `--`, `+` (dấu), `-` (dấu), `sizeof` | **Phải sang trái ($\leftarrow$)** |
| **Cấp 2** | **산술 (Số học - Nhân/Chia)** | `*`, `/`, `%` | Trái sang phải ($\rightarrow$) |
| **Cấp 3** | **산술 (Số học - Cộng/Trừ)** | `+`, `-` | Trái sang phải ($\rightarrow$) |
| **Cấp 4** | **시프트 (Dịch bit)** | `<<`, `>>` | Trái sang phải ($\rightarrow$) |
| **Cấp 5** | **관계 (So sánh kích thước)** | `<`, `<=`, `>`, `>=` | Trái sang phải ($\rightarrow$) |
| **Cấp 6** | **관계 (So sánh đẳng thức)** | `==`, `!=` | Trái sang phải ($\rightarrow$) |
| **Cấp 7** | **비트 논리 (Bitwise)** | `&` (AND) $\rightarrow$ `^` (XOR) $\rightarrow$ `\|` (OR) | Trái sang phải ($\rightarrow$) |
| **Cấp 8** | **논리 (Logic)** | `&&` (AND) $\rightarrow$ `\|\|` (OR) | Trái sang phải ($\rightarrow$) |
| **Cấp 9** | **조건 (Ba ngôi)** | `? :` | **Phải sang trái ($\leftarrow$)** |
| **Cấp 10** | **대입 (Phép gán)** | `=`, `+=`, `-=`, `*=`, `/=`, `%=` | **Phải sang trái ($\leftarrow$)** |
| **Cấp 11 (Thấp nhất)** | **콤마 (Dấu phẩy)** | `,` | Trái sang phải ($\rightarrow$) |

- **Bài toán thi mẫu phân tích thứ tự ưu tiên:**
  - *Biểu thức:* `int res = 5 + 3 * 2 > 10 && 4 == 4;`
  - *Thứ tự định giá từng bước:*
    1. Số học nhân: `3 * 2 = 6`. Biểu thức thành: `5 + 6 > 10 && 4 == 4`.
    2. Số học cộng: `5 + 6 = 11`. Biểu thức thành: `11 > 10 && 4 == 4`.
    3. Quan hệ lớn hơn: `11 > 10` $\rightarrow$ `1` (True). Biểu thức thành: `1 && 4 == 4`.
    4. Quan hệ so sánh bằng: `4 == 4` $\rightarrow$ `1` (True). Biểu thức thành: `1 && 1`.
    5. Logic AND: `1 && 1` $\rightarrow$ `1` (True).
    6. Phép gán: `res = 1`.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Hướng kết hợp (Associativity) của toán tử:**
  - Phần lớn các toán tử nhị phân (có 2 toán hạng) thực hiện theo hướng **Trái sang Phải** (Left-to-Right).
  - Có 3 trường hợp đặc biệt thực hiện theo hướng **Phải sang Trái** (Right-to-Left):
    1. Toán tử đơn nguyên (Unary): `++x`, `!y`, `-z`.
    2. Toán tử điều kiện ba ngôi (Conditional): `a ? b : c ? d : e`.
    3. Các toán tử gán (Assignment): `x = y = z = 5`.

### 복습 체크리스트
- [ ] Học thuộc lòng thần chú: 단산관논대 (단항 > 산술 > 관계 > 논리 > 대입).
- [ ] Nhớ trong phép nhân chia cộng trừ: nhân chia trước (`* / %`), cộng trừ sau (`+ -`).
- [ ] Nhớ trong phép quan hệ: so sánh lớn bé (`< >`) trước, so sánh bằng khác (`== !=`) sau.
- [ ] Nhớ trong logic: `&&` thực hiện trước `||`.
