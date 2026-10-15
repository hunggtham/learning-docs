# 080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)

## 학습 목표 (Mục tiêu)
- Nắm vững danh sách các tệp tiêu đề thư viện chuẩn (표준 라이브러리 헤더 파일) trong ngôn ngữ C: `<stdio.h>`, `<stdlib.h>`, `<string.h>`, và `<math.h>` cùng các hàm thông dụng tương ứng.
- Hiểu sâu cơ chế xử lý ngoại lệ (예외 처리 - Exception Handling) trong Java (`try - catch - finally`) và Python (`try - except - finally`).
- Nắm vững vai trò đặc biệt của khối `finally`: luôn luôn được thực thi vô điều kiện dù ngoại lệ có xảy ra hay không.
- Nhận diện các lớp ngoại lệ runtime phổ biến trong đề thi: `NullPointerException`, `ArithmeticException` (hoặc `ZeroDivisionError`), và `ArrayIndexOutOfBoundsException`.

## 핵심 키워드 (Từ khóa)
- C 표준 라이브러리 (stdio.h, stdlib.h, string.h, math.h)
- atoi() (문자열 $\rightarrow$ 정수 변환)
- 예외 처리 (Exception Handling / try-catch-finally)
- finally 블록 (무조건 실행 / 자원 해제)
- NullPointerException (객체 참조 부재)
- ArithmeticException / ZeroDivisionError (0으로 나누기)
- ArrayIndexOutOfBoundsException / IndexError (인덱스 초과)

## 선행·연결 개념 (Kiến thức liên kết)
- [29-bai-hoc.md](29-bai-hoc.md): So sánh toán tử quan hệ Java và luồng điều khiển Python.
- [31-bai-hoc.md](31-bai-hoc.md): Lập trình hướng đối tượng (OOP) và tính kế thừa.
- [23-bai-hoc.md](23-bai-hoc.md): Thư viện xử lý chuỗi `<string.h>`.

## 읽는 방법 (Cách đọc)
- Phân biệt hai mảng kiến thức:
  - **C Standard Libraries:**
    - `<stdio.h>`: Input/Output (`printf`, `scanf`, `getchar`, `puts`).
    - `<stdlib.h>`: Quản lý bộ nhớ và chuyển đổi (`malloc`, `free`, `atoi` đổi chuỗi thành int, `rand`).
    - `<string.h>`: Xử lý chuỗi (`strlen`, `strcpy`, `strcat`, `strcmp`).
    - `<math.h>`: Toán học (`sqrt` căn bậc hai, `pow` lũy thừa, `abs` giá trị tuyệt đối).
  - **Cơ chế Khối `finally`:**
    - Khối `try`: Chứa đoạn mã có nguy cơ phát sinh sự cố.
    - Khối `catch` / `except`: Chứa đoạn mã xử lý khi sự cố xảy ra.
    - Khối `finally`: **Luôn luôn chạy 100% trong mọi trường hợp**, kể cả khi trong khối `try` có lệnh `return`. Thường dùng để đóng kết nối cơ sở dữ liệu hoặc đóng file mở.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng 4 thư viện chuẩn ngôn ngữ C thường gặp:**

| Tệp tiêu đề (Header File) | Lĩnh vực phụ trách | Các hàm tiêu biểu chuẩn đề thi |
| :--- | :--- | :--- |
| **`<stdio.h>`** | Standard I/O (Nhập xuất chuẩn) | `printf()`, `scanf()`, `getchar()`, `putchar()`, `gets()`, `puts()` |
| **`<stdlib.h>`** | Standard Utilities (Tiện ích chuẩn) | `atoi()` (chuyển chuỗi sang số nguyên), `malloc()`, `free()`, `rand()`, `exit()` |
| **`<string.h>`** | String Manipulation (Thao tác chuỗi) | `strlen()` (độ dài), `strcpy()` (sao chép), `strcat()` (nối), `strcmp()` (so sánh) |
| **`<math.h>`** | Math Functions (Toán học giải tích) | `sqrt()` (căn bậc 2), `pow(x, y)` ($x^y$), `abs()` / `fabs()` (trị tuyệt đối) |

- **Bảng đối chiếu cơ chế xử lý ngoại lệ: Java vs Python:**

| Thành phần xử lý | Cú pháp trong Java | Cú pháp trong Python | Ý nghĩa hành vi thực thi |
| :--- | :--- | :--- | :--- |
| **Khối thử nghiệm rủi ro** | `try { ... }` | `try:` | Chứa các câu lệnh có khả năng ném ra ngoại lệ khi chạy |
| **Khối bắt lỗi ngoại lệ** | `catch (ExceptionType e) { ... }` | `except ExceptionType:` | Bắt lấy đối tượng lỗi và thực thi biện pháp khắc phục sự cố |
| **Khối dọn dẹp bắt buộc** | `finally { ... }` | `finally:` | **Bắt buộc thực thi vô điều kiện**, dùng để giải phóng tài nguyên |

- **Bảng các loại ngoại lệ thường gặp trong đề thi:**

| Ngoại lệ trong Java | Ngoại lệ tương đương trong Python | Nguyên nhân phát sinh lỗi |
| :--- | :--- | :--- |
| **`NullPointerException`** | `AttributeError` | Thao tác trên một biến đối tượng chưa được khởi tạo (`null`) |
| **`ArithmeticException`** | **`ZeroDivisionError`** | Thực hiện phép chia một số nguyên cho số 0 |
| **`ArrayIndexOutOfBoundsException`** | **`IndexError`** | Truy xuất phần tử ngoài giới hạn độ dài của mảng (ví dụ: mảng có 5 phần tử nhưng gọi `a[10]`) |
| **`NumberFormatException`** | `ValueError` | Ép một chuỗi ký tự chữ cái sang số nguyên (ví dụ: `Integer.parseInt("abc")`) |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bẫy thi hành khối `finally` khi gặp `return`:**
  - *Đoạn mã Java:*
    ```java
    public static int test() {
        try {
            return 10;
        } finally {
            System.out.print("Finally ");
        }
    }
    ```
  - Dù lệnh `return 10;` nằm trong khối `try`, Java vẫn **tạm ngưng return để thực thi toàn bộ khối `finally` trước**, sau đó mới thực sự trả về giá trị 10 cho hàm gọi. Màn hình in ra chữ `Finally ` trước.

### 복습 체크리스트
- [ ] Nhớ hàm `atoi` nằm trong `<stdlib.h>` dùng để đổi chuỗi sang số nguyên.
- [ ] Nhớ các hàm chuỗi `strlen`, `strcpy` nằm trong `<string.h>`.
- [ ] Nhớ khối `finally` luôn được thực thi trong mọi trường hợp (kể cả có lỗi hay không, có `return` hay không).
- [ ] Phân biệt được các lỗi runtime: `NullPointerException` (null), `ArithmeticException` (chia 0), và `ArrayIndexOutOfBoundsException` (vượt biên mảng).
