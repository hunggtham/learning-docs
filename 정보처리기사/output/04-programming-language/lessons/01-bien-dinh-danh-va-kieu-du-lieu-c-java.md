# 변수, 식별자 명명 규칙 및 C/Java 데이터 타입 (Biến, Định danh & Kiểu dữ liệu C/Java)

## 학습 목표 (Mục tiêu)
- Nắm vững hệ thống quy tắc định danh và đặt tên biến (변수명 작성 규칙 - Variable Naming Rules) trong các ngôn ngữ lập trình C, Java, Python; nhận diện chính xác các tên biến hợp lệ và không hợp lệ trong đề thi.
- Ghi nhớ chính xác độ lớn kích thước bộ nhớ (Bytes) và miền giá trị của các kiểu dữ liệu cơ bản trong ngôn ngữ C/C++ và Java.
- Phân biệt điểm khác biệt bản chất giữa kiểu `char` trong C (1 Byte ASCII) và `char` trong Java (2 Byte Unicode UTF-16), cũng như kiểu chân trị logic giữa C (số nguyên `0`/`1`) và Java (`boolean: true/false`).

## 핵심 키워드 (Từ khóa)
- 식별자 명명 규칙 (Identifier Naming Rules) — Quy tắc đặt tên định danh và biến số.
- 첫 글자 숫자 제한 (First Character Restriction) — Ký tự đầu tiên không được là chữ số.
- 예약어 사용 금지 (Reserved Words Prohibited) — Cấm đặt tên biến trùng từ khóa của ngôn ngữ.
- C/C++ 자료형 크기 (C/C++ Data Type Sizes) — `char` 1B, `short` 2B, `int` 4B, `long long` 8B, `double` 8B.
- Java 자료형 크기 (Java Data Type Sizes) — `boolean` 1B, `byte` 1B, `char` 2B (Unicode), `int` 4B, `long` 8B.
- 표기법 (Naming Conventions) — Camel Case, Pascal Case, Snake Case, Kebab Case.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Bài mở đầu của Môn 4, kế thừa kiến thức tổng quan về lập trình và cú pháp mã nguồn sạch từ Môn 2 (Software Development).
- **Đang giải quyết gì (Current Problem):** Giải quyết câu hỏi nền tảng nhất của mọi ngôn ngữ lập trình: Máy tính cấp phát và biểu diễn dữ liệu trong bộ nhớ như thế nào, và lập trình viên phải đặt tên định danh ra sao để trình biên dịch không báo lỗi cú pháp.
- **Dùng đi đâu (Forward Handoff):** Các kiểu dữ liệu nguyên thủy này sẽ là toán hạng trực tiếp tham gia vào các phép toán số học, quan hệ và thao tác bit trong bài học kế tiếp `02-toan-tu-va-thu-tu-uu-tien-operators.md`.

## 읽는 방법 (Cách đọc)
- **Quy tắc đặt tên biến:** Ghi nhớ 4 cấm: Cấm bắt đầu bằng số (`1a` là sai); Cấm chứa khoảng trắng (`my var` là sai); Cấm chứa dấu gạch ngang và toán tử (`my-var`, `total#` là sai); Cấm trùng từ khóa (`int`, `while` là sai). Cho phép duy nhất dấu gạch dưới `_` (Java cho phép thêm `$`).
- **Kích thước kiểu dữ liệu:** Đề thi cực kỳ hay bẫy ở cặp `char`: C `char` chiếm **1 Byte**, nhưng Java `char` chiếm **2 Byte** (để chứa bảng mã Unicode).

---

## 변수, 식별자 명명 규칙 및 C/Java 데이터 타입

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `변수명은 영문자, 숫자, 밑줄(_)만 사용 가능하며, 첫 글자는 반드시 영문자 또는 밑줄(_)이어야 하고 숫자로 시작할 수 없다.`
  - [Tiếng Việt]: Tên biến chỉ được dùng chữ cái tiếng Anh, chữ số và dấu gạch dưới (`_`). Ký tự đầu tiên bắt buộc phải là chữ cái hoặc dấu gạch dưới, tuyệt đối không được bắt đầu bằng chữ số.

- **1. Bảng đối chiếu quy tắc đặt tên biến (변수명 유효성 검증):**

| Tên biến kiểm tra | Hợp lệ / Không | Giải thích chuẩn đề thi HRDK |
| :--- | :---: | :--- |
| `user_name` | **Hợp lệ (O)** | Chỉ gồm chữ thường và dấu gạch dưới `_`. |
| `_count` | **Hợp lệ (O)** | Bắt đầu bằng dấu gạch dưới `_` hoàn toàn hợp lệ. |
| `data2026` | **Hợp lệ (O)** | Bắt đầu bằng chữ cái, chữ số nằm ở phía sau. |
| `$salary` | **Hợp lệ (O in Java)** | Ngôn ngữ Java đặc cách cho phép ký tự `$`. |
| `2nd_score` | **Bất hợp lệ (X)** | **Lỗi ký tự đầu:** Bắt đầu bằng chữ số `2`. |
| `user name` | **Bất hợp lệ (X)** | **Lỗi khoảng trắng:** Chứa dấu cách ở giữa 2 từ. |
| `user-id` | **Bất hợp lệ (X)** | **Lỗi ký tự đặc biệt:** Trình biên dịch nhầm `-` với phép trừ. |
| `while` / `int` | **Bất hợp lệ (X)** | **Lỗi từ khóa (예약어):** Trùng từ khóa có sẵn của ngôn ngữ. |

- **2. Bảng phân loại quy ước đặt tên (표기법 - Naming Conventions):**

| Phong cách | Quy tắc viết hoa | Ngữ cảnh sử dụng điển hình |
| :--- | :--- | :--- |
| **Camel Case (낙타 표기법)** | Từ đầu viết thường, các từ sau viết hoa chữ cái đầu: `studentCount` | Tên biến và tên hàm/phương thức trong Java, JS. |
| **Pascal Case (파스칼 표기법)** | Mọi từ đều viết hoa chữ cái đầu: `StudentManager` | Tên Lớp (Class) và Giao diện (Interface) trong Java, C#. |
| **Snake Case (스네이크 표기법)** | Tất cả viết thường, cách nhau bằng dấu `_`: `student_score` | Tên biến và tên hàm trong C, Python; tên cột CSDL. |
| **Kebab Case (케밥 표기법)** | Viết thường, cách nhau bằng dấu `-`: `student-card` | Tên class CSS, slug URL web (Không dùng làm tên biến). |

- **3. Bảng đối chiếu kích thước kiểu dữ liệu C vs Java (자료형 크기 비교):**

| Kiểu dữ liệu | Ngôn ngữ C / C++ | Ngôn ngữ JAVA | Ghi chú thi cử then chốt |
| :--- | :---: | :---: | :--- |
| **Ký tự (Character)** | `char`: **1 Byte** | `char`: **2 Byte** | C dùng ASCII (0–127); Java dùng Unicode UTF-16. |
| **Số nguyên 1 Byte** | `char` (dùng như số) | `byte`: **1 Byte** | Java có kiểu `byte` (-128 đến 127). |
| **Số nguyên ngắn** | `short`: **2 Byte** | `short`: **2 Byte** | Miền giá trị: $-32,768 \sim 32,767$. |
| **Số nguyên chuẩn** | `int`: **4 Byte** | `int`: **4 Byte** | Mặc định biểu diễn bù 2 (Two's Complement). |
| **Số nguyên dài** | `long`: 4 Byte (hoặc 8B) | `long`: **8 Byte** | Java luôn cố định 64-bit; C phụ thuộc OS. |
| **Số nguyên cực dài** | `long long`: **8 Byte** | (Không có cú pháp này) | Trong Java dùng `long` 8 Byte. |
| **Số thực độ chính xác đơn** | `float`: **4 Byte** | `float`: **4 Byte** | Chuẩn IEEE 754 (chính xác ~7 chữ số thập phân). |
| **Số thực độ chính xác kép**| `double`: **8 Byte** | `double`: **8 Byte** | Chuẩn IEEE 754 (chính xác ~15 chữ số thập phân). |
| **Kiểu logic chân trị** | `_Bool` (hoặc số 0/1) | `boolean`: **1 Byte** | Java chỉ nhận `true`/`false`, cấm dùng số `0/1`. |

- **주의/함정 (Bẫy đề thi):**
  - Đề thi hỏi: *"Đâu là kích thước của kiểu `char` trong Java?"* $\rightarrow$ Đáp án đúng là **2 Byte**, chọn 1 Byte là sai bẫy C.
  - Tên biến phân biệt hoa thường tuyệt đối (Case-sensitive): `Score` và `score` là hai biến nằm ở hai ô nhớ hoàn toàn khác nhau.
  - Hằng số ký tự dùng nháy đơn `'A'` (1 ký tự), hằng chuỗi dùng nháy kép `"A"` (kèm ký tự kết thúc `\0`).

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"Tên biến cấm số đứng đầu, cấm cách cấm trùng; C char 1 byte ASCII còn Java char 2 byte Unicode."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Tại sao trình phân tích từ vựng (Lexer) cấm số đứng đầu tên biến?
Trình biên dịch xử lý mã nguồn qua bước Phân tích từ vựng (Lexical Analysis):
- Khi con trỏ đọc gặp ký tự đầu tiên là chữ số `[0-9]`, bộ phân tích từ vựng tự động chuyển trạng thái nội bộ sang nhận diện **Hằng số số học (Numeric Literal)**.
- Nếu các ký tự tiếp theo lại là chữ cái (ví dụ: `1st_player`), Lexer sẽ không thể gộp thành số nguyên hợp lệ và sẽ ném ra lỗi cú pháp (Syntax Error / Invalid Token).
- Nếu cho phép số đứng đầu, một biến tên `123` sẽ gây xung đột không thể phân định được giữa "tên biến 123" và "số nguyên 123".

#### 2. Minh họa mã nguồn kiểm tra kiểu dữ liệu trong C:
```c
#include <stdio.h>

int main() {
    // Khai báo các kiểu dữ liệu cơ bản
    char c = 'A';              // 1 Byte ký tự ASCII
    int i = 2026;              // 4 Byte số nguyên
    long long ll = 9000000000; // 8 Byte số nguyên lớn
    float f = 3.14f;           // 4 Byte số thực
    double d = 3.1415926535;   // 8 Byte số thực kép

    // In kích thước bằng toán tử sizeof (trả về size_t - %zu hoặc %lu)
    printf("char: %zu Byte\n", sizeof(c));       // Kết quả: 1
    printf("int: %zu Byte\n", sizeof(i));         // Kết quả: 4
    printf("long long: %zu Byte\n", sizeof(ll)); // Kết quả: 8
    printf("float: %zu Byte\n", sizeof(f));       // Kết quả: 4
    printf("double: %zu Byte\n", sizeof(d));     // Kết quả: 8

    return 0;
}
```

#### 3. Minh họa mã nguồn phân biệt kiểu dữ liệu trong Java:
```java
public class DataTypeDemo {
    public static void main(String[] args) {
        // Java phân biệt rạch ròi kiểu boolean và số nguyên
        boolean isValid = true; // Chỉ nhận true hoặc false
        // int wrongFlag = (int) isValid; // Lỗi biên dịch: Không thể ép kiểu boolean sang int

        // char trong Java lưu ký tự 16-bit Unicode
        char vietChar = 'Á'; // Lưu trữ ký tự tiếng Việt hoặc tiếng Hàn bình thường
        char korChar = '가'; // Không bị tràn bộ nhớ như char 8-bit trong C

        System.out.println("Boolean: " + isValid);
        System.out.println("Vietnamese Char: " + vietChar);
        System.out.println("Korean Char: " + korChar);
        System.out.println("Java char size: " + Character.BYTES + " Bytes"); // In ra: 2 Bytes
    }
}
```

---

### 복습 체크리스트
- [ ] Ghi nhớ quy tắc ký tự đầu: Chỉ được bắt đầu bằng chữ cái hoặc dấu gạch dưới `_`, cấm bắt đầu bằng số.
- [ ] Nhớ tên biến cấm chứa dấu cách, cấm dấu gạch ngang `-`, cấm trùng từ khóa dự phòng (예약어).
- [ ] Phân biệt Camel Case (`myVar`), Pascal Case (`MyClass`), Snake Case (`my_var`).
- [ ] Nắm chắc kích thước: C `char` = 1 Byte, Java `char` = 2 Byte Unicode.
- [ ] Ghi nhớ `int` = 4 Byte, `double` = 8 Byte, `long long` = 8 Byte trong C.
- [ ] Nhớ Java `boolean` chỉ nhận giá trị `true` hoặc `false`, không dùng số `0/1` thay thế được như trong C.
