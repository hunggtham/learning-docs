# 프로그래밍 언어 기초 (Programming Language Basics)

## 프로그래밍 언어 기초 (Programming Language Basics)
### 159. C/JAVA의 자료형 (Data Types / Kiểu dữ liệu)
Phần “159. C/JAVA의 자료형 (Data Types / Kiểu dữ liệu)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **C (exam assumption / giả định đề thi phổ biến):** `char` 1 byte, `int` 4 bytes; `long` phụ thuộc ABI/compiler và không nên ghi là 8 bytes tuyệt đối.
- **Java:** `byte` 1 byte, `short` 2 bytes, `int` 4 bytes, `long` 8 bytes, `char` 2 bytes (Unicode), `float` 4 bytes, `double` 8 bytes. `boolean` là kiểu logic; Java không quy định một kích thước lưu trữ cố định.
  - *Example / Ví dụ*: `int age = 25; boolean isStudent = true;`
  - 💡 *Mẹo ghi nhớ*: Java `char` = 2 bytes; C `char` = 1 byte; không suy ra kích thước storage của `boolean` từ ví dụ JVM.

### 162. 변수명 작성 규칙 (Variable Naming Rules / Quy tắc đặt tên biến)
Phần “162. 변수명 작성 규칙 (Variable Naming Rules / Quy tắc đặt tên biến)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 영문자, 숫자, _(under bar)를 사용할 수 있다. (Có thể sử dụng chữ cái tiếng Anh, số và dấu gạch dưới).
- 첫 글자는 숫자는 올 수 없다. (Chữ cái đầu tiên không được là số).
- 공백이나 *, +, -, / 등의 특수문자를 사용할 수 없다. (Không được sử dụng khoảng trắng hoặc ký tự đặc biệt).
- 대소문자를 구분한다. (Phân biệt chữ hoa và chữ thường).
- 예약어를 변수명으로 사용할 수 없다. (Không được sử dụng từ khóa dự phòng làm tên biến).
  - *Example / Ví dụ*: Hợp lệ: `my_var_1`, Không hợp lệ: `1_my_var` (bắt đầu bằng số), `my var` (có khoảng trắng).
  - 💡 *Mẹo ghi nhớ*: Chỉ dùng `A-Z, a-z, 0-9, _`. Số không đi đầu. Không dùng từ khóa.

### 163. 가비지 콜렉터 (Garbage Collector / Trình thu gom rác)
Phần “163. 가비지 콜렉터 (Garbage Collector / Trình thu gom rác)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 선언만 하고 사용하지 않는 변수들이 점유한 메모리 공간을 강제로 해제하여 다른 프로그램들이 사용할 수 있도록 하는 것이다. (Tự động giải phóng không gian bộ nhớ do các biến được khai báo nhưng không sử dụng để các chương trình khác có thể sử dụng).
  - *Example / Ví dụ*: Trong Java, Garbage Collector (GC) tự động dọn dẹp các đối tượng không còn được tham chiếu.
  - 💡 *Mẹo ghi nhớ*: "Garbage" (rác) -> Dọn dẹp bộ nhớ không dùng đến.
