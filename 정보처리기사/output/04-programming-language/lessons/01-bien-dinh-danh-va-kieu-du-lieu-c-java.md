# 변수, 식별자 명명 규칙 및 C/Java 데이터 타입 (Biến, Định danh & Kiểu dữ liệu C/Java)

## 학습 목표 (Mục tiêu)
- Nắm vững hệ thống quy tắc định danh và đặt tên biến (변수명 작성 규칙 - Variable Naming Rules) trong các ngôn ngữ lập trình C, Java, Python; nhận diện chính xác các tên biến hợp lệ và không hợp lệ trong đề thi.
- Ghi nhớ chính xác độ lớn kích thước bộ nhớ (Bytes) và miền giá trị của các kiểu dữ liệu cơ bản trong ngôn ngữ C/C++ và Java (`char`, `short`, `int`, `long`, `float`, `double`).
- Phân biệt điểm khác biệt bản chất giữa kiểu `char` trong C (1 Byte ASCII) và `char` trong Java (2 Byte Unicode UTF-16), cũng như kiểu chân trị logic giữa C (số nguyên `0`/`1`) và Java (`boolean: true/false`).
- Hiểu rõ 4 lớp lưu trữ biến trong C (기억 부류 - Storage Classes: `auto`, `static`, `register`, `extern`) về vùng nhớ cư trú, vòng đời và giá trị khởi tạo mặc định.

## 핵심 키워드 (Từ khóa)
- 식별자 명명 규칙 (Identifier Naming Rules) — Quy tắc đặt tên định danh và biến số.
- 첫 글자 숫자 제한 (First Character Restriction) — Ký tự đầu tiên không được là chữ số.
- 예약어 사용 금지 (Reserved Words Prohibited) — Cấm đặt tên biến trùng từ khóa của ngôn ngữ.
- C/C++ 자료형 크기 (C/C++ Data Type Sizes) — `char` 1B, `short` 2B, `int` 4B, `long` 4/8B, `long long` 8B, `float` 4B, `double` 8B.
- Java 자료형 크기 (Java Data Type Sizes) — `boolean` 1B, `byte` 1B, `char` 2B (Unicode), `short` 2B, `int` 4B, `long` 8B, `float` 4B, `double` 8B.
- 기억 부류 (Storage Classes) — auto (자동 변수), static (정적 변수), register (레지스터 변수), extern (외부 변수).
- 표기법 (Naming Conventions) — Camel Case, Pascal Case, Snake Case, Kebab Case.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Bài mở đầu của Môn 4, kế thừa kiến thức tổng quan về lập trình và cú pháp mã nguồn sạch từ Môn 2 (Software Development).
- **Đang giải quyết gì (Current Problem):** Giải quyết câu hỏi nền tảng nhất của mọi ngôn ngữ lập trình: Máy tính cấp phát và biểu diễn dữ liệu trong bộ nhớ như thế nào, lập trình viên đặt tên định danh ra sao để trình biên dịch không báo lỗi cú pháp, và vòng đời của biến được quản lý thế nào qua các lớp lưu trữ.
- **Dùng đi đâu (Forward Handoff):** Các kiểu dữ liệu nguyên thủy này sẽ là toán hạng trực tiếp tham gia vào các phép toán số học, quan hệ và thao tác bit trong bài học kế tiếp `02-toan-tu-va-thu-tu-uu-tien-operators.md`.

## 읽는 방법 (Cách đọc)
- **Quy tắc đặt tên biến:** Ghi nhớ 4 cấm: Cấm bắt đầu bằng số (`1a` là sai); Cấm chứa khoảng trắng (`my var` là sai); Cấm chứa dấu gạch ngang và toán tử (`my-var`, `total#` là sai); Cấm trùng từ khóa (`int`, `while` là sai). Cho phép duy nhất dấu gạch dưới `_` (Java cho phép thêm `$`).
- **Kích thước kiểu dữ liệu:** Đề thi cực kỳ hay bẫy ở cặp `char`: C `char` chiếm **1 Byte**, nhưng Java `char` chiếm **2 Byte** (để chứa bảng mã Unicode).
- **4 Lớp lưu trữ trong C:**
  - `auto`: Mặc định trong hàm, trên Stack, mất khi thoát hàm, giá trị rác.
  - `static`: Trên Data Segment, tồn tại suốt chương trình, giữ nguyên giá trị qua các lần gọi hàm, mặc định bằng 0.
  - `register`: Lưu trong CPU Register, truy xuất cực nhanh, cấm dùng toán tử lấy địa chỉ `&`.
  - `extern`: Khai báo biến toàn cục ở file/module khác để dùng chung.

---

## 변수, 식별자 명명 규칙 및 C/Java 데이터 타입

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `변수명은 영문자, 숫자, 밑줄(_)만 사용 가능하며, 첫 글자는 반드시 영문자 또는 밑줄(_)이어야 하고 숫자로 시작할 수 없다. C의 char는 1바이트(ASCII)이나 Java의 char는 2바이트(Unicode)이다. C 기억 부류에는 auto(스택, 자동소멸), static(데이터영역, 값유지, 초기값 0), register(CPU 레지스터, 주소연산자 & 불가), extern(외부참조)이 있다.`
  - [Tiếng Việt]: Tên biến chỉ được dùng chữ cái tiếng Anh, chữ số và dấu gạch dưới (`_`). Ký tự đầu tiên bắt buộc phải là chữ cái hoặc dấu gạch dưới, tuyệt đối không được bắt đầu bằng chữ số. `char` trong C là 1 Byte (ASCII) nhưng trong Java là 2 Byte (Unicode). Bốn lớp lưu trữ trong C gồm: auto (Stack, tự hủy), static (Data segment, giữ giá trị, khởi tạo 0), register (thanh ghi CPU, cấm toán tử địa chỉ `&`), extern (tham chiếu file ngoài).

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
| **Số nguyên ngắn** | `short`: **2 Byte** | `short`: **2 Byte** | Miền giá trị: -32,768 đến 32,767. |
| **Số nguyên chuẩn** | `int`: **4 Byte** | `int`: **4 Byte** | Miền giá trị: khoảng -2.1 tỷ đến +2.1 tỷ. |
| **Số nguyên dài** | `long`: 4 Byte (hoặc 8B) | `long`: **8 Byte** | Java luôn cố định 64-bit; C phụ thuộc kiến trúc OS. |
| **Số nguyên cực dài** | `long long`: **8 Byte** | (Không có cú pháp này) | Trong Java dùng `long` 8 Byte. |
| **Số thực độ chính xác đơn** | `float`: **4 Byte** | `float`: **4 Byte** | Chuẩn IEEE 754 (chính xác ~7 chữ số thập phân). |
| **Số thực độ chính xác kép**| `double`: **8 Byte** | `double`: **8 Byte** | Chuẩn IEEE 754 (chính xác ~15 chữ số thập phân). |
| **Kiểu logic chân trị** | `_Bool` (hoặc số 0/1) | `boolean`: **1 Byte** | Java chỉ nhận `true`/`false`, cấm dùng số `0/1`. |

- **4. Bảng 4 lớp lưu trữ trong C (C 기억 부류 - Storage Classes):**

| Lớp lưu trữ | Vị trí bộ nhớ | Vòng đời (Lifetime) | Phạm vi (Scope) | Giá trị khởi tạo mặc định | Toán tử `&` (Địa chỉ) |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **`auto` (자동 변수)** | **Stack** | Khi hàm/khối lệnh thực thi; thoát hàm tự hủy | Cục bộ trong khối `{}` | **Giá trị rác (Garbage)** | Hợp lệ |
| **`static` (정적 변수)** | **Data Segment** (BSS/Data) | Suốt thời gian chạy chương trình | Cục bộ hoặc toàn file | **Tự động gán 0** | Hợp lệ |
| **`register` (레지스터 변수)** | **CPU Register** | Tương tự `auto` (khi hàm chạy) | Cục bộ trong khối `{}` | Giá trị rác | **CẤM (Lỗi biên dịch)** |
| **`extern` (외부 변수)** | **Data Segment** | Suốt thời gian chạy chương trình | Toàn bộ dự án đa file | Theo định nghĩa gốc | Hợp lệ |

- **주의/함정 (Bẫy đề thi):**
  - **Kích thước `char` trong Java:** Đề thi hỏi: *"Đâu là kích thước của kiểu `char` trong Java?"* -> Đáp án đúng là **2 Byte**, chọn 1 Byte là sai bẫy C.
  - **Toán tử địa chỉ trên biến register:** Biến `register int x;` được lưu trong thanh ghi CPU, không có địa chỉ trong RAM vật lý -> Biểu thức `&x` sẽ bị **Trình biên dịch báo lỗi ngay lập tức**.
  - **Biến `static` trong hàm:** Dòng khai báo `static int count = 0;` chỉ chạy **duy nhất một lần** khi chương trình nạp. Khi gọi lại hàm lần thứ 2, 3, dòng này bị bỏ qua và biến giữ nguyên giá trị từ lần gọi trước.
  - Tên biến phân biệt hoa thường tuyệt đối (Case-sensitive): `Score` và `score` là hai biến nằm ở hai ô nhớ hoàn toàn khác nhau.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"Tên biến cấm số đứng đầu; Java char 2 byte; static giữ giá trị qua ngàn lần gọi, register trong CPU cấm hỏi địa chỉ &."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ bố trí các phân vùng bộ nhớ của chương trình C (Memory Layout):
Khi chương trình C được nạp vào RAM, hệ điều hành phân chia không gian tiến trình như sau:

```text
+-------------------------------------------------------+ Cao (0xFFFFFFFF)
| Stack Segment: Chứa biến cục bộ auto, tham số hàm     |
|       |                                               |
|       v (Phát triển xuống dưới)                       |
|                                                       |
|       ^ (Phát triển lên trên)                         |
|       |                                               |
| Heap Segment: Cấp phát động (malloc / calloc / new)   |
+-------------------------------------------------------+
| BSS Segment: Biến static và toàn cục CHƯA khởi tạo    | (Mặc định nạp 0)
+-------------------------------------------------------+
| Data Segment: Biến static và toàn cục ĐÃ khởi tạo     |
+-------------------------------------------------------+
| Text/Code Segment: Mã máy nhị phân thực thi           | Thấp (0x00000000)
+-------------------------------------------------------+
```

Biến `static` cư trú tại Data/BSS Segment nên không bị phá hủy khi hàm kết thúc, khác hoàn toàn với biến `auto` trên Stack.

#### 2. Phân tích bài toán thi kinh điển: Biến `auto` vs Biến `static`:
Xem xét hàm C sau và dự đoán giá trị in ra:

```c
#include <stdio.h>

void counter() {
    auto int a = 0;      // Biến auto: Cấp phát mới mỗi lần vào hàm
    static int s = 0;    // Biến static: Chỉ khởi tạo 1 lần duy nhất

    a++;
    s++;
    printf("a = %d, s = %d\n", a, s);
}

int main() {
    counter(); // Lần 1: a tăng lên 1, s tăng lên 1 -> In: a = 1, s = 1
    counter(); // Lần 2: a tạo mới = 0 -> a = 1; s giữ nguyên 1 -> s = 2
    counter(); // Lần 3: a tạo mới = 0 -> a = 1; s giữ nguyên 2 -> s = 3
    return 0;
}
```

**Bảng Trace biến qua 3 lần gọi:**

| Lần gọi hàm | Giá trị `a` ban đầu | `a++` | Giá trị `s` ban đầu | `s++` | Output hiển thị |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **Lần 1** | 0 (khởi tạo) | 1 | 0 (khởi tạo) | 1 | `a = 1, s = 1` |
| **Lần 2** | 0 (tái tạo trên stack) | 1 | 1 (giữ nguyên từ lần 1) | 2 | `a = 1, s = 2` |
| **Lần 3** | 0 (tái tạo trên stack) | 1 | 2 (giữ nguyên từ lần 2) | 3 | `a = 1, s = 3` |

#### 3. Minh họa mã nguồn kiểm tra kiểu dữ liệu trong C & Java:
```c
#include <stdio.h>

int main() {
    // Khai báo các kiểu dữ liệu cơ bản trong C
    char c = 'A';              // 1 Byte ký tự ASCII
    short s = 32000;           // 2 Byte số nguyên ngắn
    int i = 2026;              // 4 Byte số nguyên
    long long ll = 9000000000; // 8 Byte số nguyên lớn
    float f = 3.14f;           // 4 Byte số thực đơn
    double d = 3.1415926535;   // 8 Byte số thực kép

    printf("char: %zu Byte\n", sizeof(c));       // Kết quả: 1
    printf("short: %zu Byte\n", sizeof(s));     // Kết quả: 2
    printf("int: %zu Byte\n", sizeof(i));         // Kết quả: 4
    printf("long long: %zu Byte\n", sizeof(ll)); // Kết quả: 8
    printf("float: %zu Byte\n", sizeof(f));       // Kết quả: 4
    printf("double: %zu Byte\n", sizeof(d));     // Kết quả: 8

    return 0;
}
```

```java
public class DataTypeDemo {
    public static void main(String[] args) {
        // Java phân biệt rạch ròi kiểu boolean và số nguyên
        boolean isValid = true; // Chỉ nhận true hoặc false
        // int wrongFlag = (int) isValid; // Lỗi biên dịch: Không thể ép kiểu boolean sang int

        // char trong Java lưu ký tự 16-bit Unicode (2 Bytes)
        char vietChar = 'Á'; // Lưu trữ ký tự tiếng Việt bình thường
        char korChar = '가'; // Lưu ký tự tiếng Hàn không bị tràn bộ nhớ

        System.out.println("Boolean: " + isValid);
        System.out.println("Vietnamese Char: " + vietChar);
        System.out.println("Korean Char: " + korChar);
        System.out.println("Java char size: " + Character.BYTES + " Bytes"); // In ra: 2 Bytes
        System.out.println("Java int size: " + Integer.BYTES + " Bytes");   // In ra: 4 Bytes
        System.out.println("Java long size: " + Long.BYTES + " Bytes");     // In ra: 8 Bytes
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
- [ ] Phân biệt 4 lớp lưu trữ trong C: `auto` (Stack, giá trị rác), `static` (Data segment, giá trị giữ nguyên, mặc định 0), `register` (CPU register, cấm `&`), `extern` (tham chiếu biến ngoài).
