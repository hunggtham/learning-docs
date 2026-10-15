# 237. 변수명 작성 규칙 (Variable Naming Rules)

## 학습 목표 (Mục tiêu)
- Nắm vững hệ thống quy tắc định danh và đặt tên biến (변수명 작성 규칙 - Variable Naming Rules) trong các ngôn ngữ lập trình phổ biến (C, Java, Python).
- Phân biệt chính xác các tên biến hợp lệ và không hợp lệ trong các câu hỏi trắc nghiệm của kỳ thi Kỹ sư xử lý thông tin.
- Hiểu rõ lý do kỹ thuật đằng sau từng quy tắc: tại sao biến không được bắt đầu bằng chữ số, tại sao cấm dùng khoảng trắng, và cơ chế phân biệt chữ hoa chữ thường.

## 핵심 키워드 (Từ khóa)
- 변수명 작성 규칙 (Variable Naming Rules)
- 식별자 (Identifier)
- 첫 글자 제한 (First Character Restriction / 숫자 시작 불가)
- 특수문자 제한 (Special Characters / 밑줄 `_` 및 `$` 예외 허용)
- 예약어 금지 (Reserved Words Prohibited)
- 대소문자 구분 (Case Sensitivity)

## 선행·연결 개념 (Kiến thức liên kết)
- [06-bai-hoc.md](06-bai-hoc.md): Biến môi trường và các lệnh kịch bản Shell.
- [08-bai-hoc.md](08-bai-hoc.md): Các toán tử trong ngôn ngữ lập trình và thứ tự ưu tiên.
- [01-bai-hoc.md](01-bai-hoc.md): Khái niệm cơ bản về biến và Garbage Collector.

## 읽는 방법 (Cách đọc)
- Ghi nhớ 5 quy tắc bất di bất dịch khi đặt tên biến:
  1. **Thành phần cấu tạo:** Chỉ gồm chữ cái (`A-Z`, `a-z`), chữ số (`0-9`), và dấu gạch dưới (`_`) (trong Java cho phép thêm `$`).
  2. **Ký tự đầu tiên:** **BẮT BUỘC là chữ cái hoặc dấu gạch dưới**, tuyệt đối **KHÔNG ĐƯỢC LÀ CHỮ SỐ** (vì trình biên dịch sẽ nhầm với hằng số số học).
  3. **Ký tự đặc biệt & Khoảng trắng:** Tuyệt đối không được chứa dấu cách, không được chứa các toán tử `+`, `-`, `*`, `/`, `@`, `%`, `#`.
  4. **Từ khóa dự phòng (예약어):** Không được đặt trùng tên với các từ khóa dành riêng của ngôn ngữ (`int`, `char`, `if`, `else`, `while`, `return`, `class`...).
  5. **Độ nhạy chữ hoa/thường:** Tên biến phân biệt hoa - thường tuyệt đối (`total`, `Total`, `TOTAL` là 3 biến hoàn toàn khác nhau).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng đối chiếu các trường hợp tên biến Hợp lệ vs Bất hợp lệ:**

| Tên biến kiểm tra | Tính hợp lệ | Lý do kỹ thuật giải thích chuẩn thi |
| :--- | :--- | :--- |
| `student_name` | **Hợp lệ (O)** | Chỉ gồm chữ cái thường và dấu gạch dưới (`_`) |
| `_temp` | **Hợp lệ (O)** | Bắt đầu bằng dấu gạch dưới (`_`) là hoàn toàn hợp lệ |
| `sum100` | **Hợp lệ (O)** | Bắt đầu bằng chữ cái, chữ số nằm ở phía sau |
| `$price` | **Hợp lệ (O in Java)** | Ngôn ngữ Java cho phép ký tự `$` trong tên biến |
| `1st_player` | **Bất hợp lệ (X)** | **Bắt đầu bằng chữ số `1`** (Vi phạm quy tắc ký tự đầu) |
| `user name` | **Bất hợp lệ (X)** | **Chứa khoảng trắng ở giữa** hai từ |
| `my-var` | **Bất hợp lệ (X)** | Chứa dấu gạch nối `-` (Trình biên dịch nhầm với toán tử trừ) |
| `total#` | **Bất hợp lệ (X)** | Chứa ký tự đặc biệt `#` không được phép |
| `while` | **Bất hợp lệ (X)** | **Trùng với từ khóa vòng lặp (예약어)** của ngôn ngữ |
| `int` | **Bất hợp lệ (X)** | **Trùng với từ khóa kiểu dữ liệu** |

- **Bảng so sánh các phong cách đặt tên (Naming Conventions):**

| Phong cách đặt tên | Quy tắc viết hoa | Ngữ cảnh ứng dụng phổ biến |
| :--- | :--- | :--- |
| **Camel Case (낙타 표기법)** | Chữ đầu viết thường, các từ sau viết hoa chữ cái đầu: `studentCount` | Tên biến và tên phương thức/hàm trong Java, JavaScript |
| **Pascal Case (파스칼 표기법)** | Mọi từ đều viết hoa chữ cái đầu: `StudentController` | Tên Lớp (Class) và Giao diện (Interface) trong Java, C# |
| **Snake Case (스네이크 표기법)** | Tất cả viết thường, phân tách bằng dấu gạch dưới: `user_login_count` | Tên biến và tên hàm trong ngôn ngữ C, Python, tên cột CSDL |
| **Kebab Case (케밥 표기법)** | Tất cả viết thường, phân tách bằng dấu gạch ngang: `user-card` | Tên lớp CSS, đường dẫn URL Web (Không dùng làm tên biến) |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tại sao trình biên dịch cấm số đứng đầu tên biến?**
  - Trình phân tích từ vựng (Lexical Analyzer / Lexer) quét mã nguồn từ trái sang phải.
  - Khi bắt gặp ký tự đầu tiên là một chữ số (`0-9`), Lexer lập tức chuyển sang chế độ phân tích hằng số (Numeric Literal). Nếu phía sau lại có chữ cái (ví dụ: `123abc`), Lexer sẽ báo lỗi cú pháp do không thể nhận diện được kiểu số hợp lệ.

### 복습 체크리스트
- [ ] Nhớ tên biến không được bắt đầu bằng chữ số (ví dụ: `1a` là sai).
- [ ] Nhớ tên biến không được chứa khoảng trắng và dấu gạch ngang `-`.
- [ ] Nhớ tên biến không được trùng với từ khóa dự phòng (예약어) như `while`, `class`.
- [ ] Phân biệt được Camel Case (`studentName`), Pascal Case (`StudentClass`), và Snake Case (`student_name`).
