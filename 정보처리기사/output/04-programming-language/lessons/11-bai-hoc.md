# 244. 조건(삼항) 연산자 (Ternary Operator)

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp, nguyên lý hoạt động và thứ tự định giá của toán tử điều kiện ba ngôi (조건 연산자 / 삼항 연산자 - Ternary Operator): `조건식 ? 참일 때 식 : 거짓일 때 식`.
- Biết cách chuyển đổi qua lại linh hoạt giữa câu lệnh rẽ nhánh `if-else` truyền thống và toán tử điều kiện ba ngôi rút gọn.
- Phân tích và lần vết chính xác các biểu thức toán tử ba ngôi lồng nhau (Nested Ternary Operators) xuất hiện trong đề thi lập trình C/Java.

## 핵심 키워드 (Từ khóa)
- 조건 연산자 (Conditional Operator)
- 삼항 연산자 (Ternary Operator / `? :`)
- 조건식 평가 (Condition Evaluation)
- if-else문 대체 (Alternative to if-else)
- 중첩 삼항 연산자 (Nested Ternary Operator)
- 우측 결합성 (Right-to-Left Associativity)

## 선행·연결 개념 (Kiến thức liên kết)
- [10-bai-hoc.md](10-bai-hoc.md): Tổng hợp toàn diện các toán tử trong lập trình.
- [12-bai-hoc.md](12-bai-hoc.md): Thứ tự ưu tiên chi tiết của các toán tử.
- [17-bai-hoc.md](17-bai-hoc.md): Câu lệnh điều khiển rẽ nhánh `if` và `switch-case`.

## 읽는 방법 (Cách đọc)
- Cấu trúc cơ bản gồm 3 thành phần phân tách bởi dấu hỏi `?` và dấu hai chấm `:`:
  $$\text{Điều kiện} \quad ? \quad \text{Biểu thức khi ĐÚNG} \quad : \quad \text{Biểu thức khi SAI}$$
  - Bước 1: Trình biên dịch tính toán giá trị của `Điều kiện`.
  - Bước 2: Nếu điều kiện là Đúng (khác 0 trong C, hoặc `true` trong Java), biểu thức nằm giữa `?` và `:` được thực thi và lấy làm kết quả.
  - Bước 3: Nếu điều kiện là Sai (bằng 0 hoặc `false`), biểu thức nằm sau dấu `:` được thực thi.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh câu lệnh `if-else` và Toán tử ba ngôi:**

| Tiêu chuẩn so sánh | Câu lệnh `if-else` | Toán tử điều kiện ba ngôi `? :` |
| :--- | :--- | :--- |
| **Bản chất cú pháp** | Là **câu lệnh điều khiển (Statement)**; không trực tiếp trả về giá trị biểu thức | Là **toán tử biểu thức (Expression)**; luôn trả về một giá trị cụ thể |
| **Khả năng gán giá trị** | Phải gán bên trong từng nhánh: `if (a > b) max = a; else max = b;` | Gán trực tiếp trong 1 dòng: `max = (a > b) ? a : b;` |
| **Độ súc tích** | Chiếm nhiều dòng mã, rõ ràng khi xử lý nhiều câu lệnh | Rất ngắn gọn, tối ưu khi chỉ cần lựa chọn giữa hai giá trị đơn giản |
| **Hướng kết hợp** | Khối lệnh tuần tự | **Từ phải sang trái ($\leftarrow$)** khi lồng nhau |

- **Giải bài toán Toán tử ba ngôi lồng nhau chuẩn đề thi:**
  - *Đoạn mã C:*
    ```c
    int score = 85;
    char grade;
    grade = (score >= 90) ? 'A' : (score >= 80) ? 'B' : 'C';
    ```
  - *Quá trình phân tích:*
    1. Do có tính kết hợp từ phải sang trái, biểu thức phía sau được gom nhóm: `(score >= 90) ? 'A' : ((score >= 80) ? 'B' : 'C')`.
    2. Kiểm tra điều kiện đầu: `score >= 90` ($85 \ge 90$) $\rightarrow$ Sai (False).
    3. Nhảy sang vế sau dấu `:`: `(score >= 80) ? 'B' : 'C'`.
    4. Kiểm tra điều kiện con: `score >= 80` ($85 \ge 80$) $\rightarrow$ Đúng (True).
    5. Kết quả trả về ký tự `'B'`. Do đó `grade = 'B'`.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tương thích kiểu dữ liệu trong biểu thức ba ngôi:**
  - Trong Java, cả hai nhánh biểu thức (khi đúng và khi sai) nên có kiểu dữ liệu tương thích với nhau hoặc cùng được ép kiểu ngầm định về một kiểu chung.
  - Ví dụ: `int x = true ? 1 : 2.0;` sẽ báo lỗi biên dịch trong Java vì `2.0` là `double`, khiến cả biểu thức được nâng cấp thành kiểu `double` không thể gán trực tiếp cho biến `int`.

### 복습 체크리스트
- [ ] Viết đúng cấu trúc: `(điều kiện) ? (nếu đúng) : (nếu sai)`.
- [ ] Chuyển đổi thành thạo từ `if-else` sang biểu thức ba ngôi.
- [ ] Phân tích chính xác toán tử ba ngôi lồng nhau theo hướng từ phải sang trái.
- [ ] Nhớ trong C: điều kiện khác 0 là Đúng, bằng 0 là Sai.
