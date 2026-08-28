# 4과목: 프로그래밍 언어 활용 (Subject 4: Programming Language Application)

## 데이터베이스 기초 (Database Basics)
### 157. 집합 연산자의 종류 (Set Operators / Các toán tử tập hợp)
- **UNION**: 두 조회 결과를 통합하여 모두 출력하되, 중복된 행은 한 번만 출력함. (Hợp hai kết quả, loại bỏ trùng lặp).
- **UNION ALL**: 두 조회 결과를 통합하여 모두 출력하되, 중복된 행도 그대로 출력함. (Hợp hai kết quả, giữ nguyên trùng lặp).
- **INTERSECT**: 두 조회 결과 중 공통된 행만 출력함. (Giao hai kết quả, chỉ lấy phần chung).
- **EXCEPT**: 첫 번째 조회 결과에서 두 번째 조회 결과를 제외한 행을 출력함. (Trừ kết quả thứ hai khỏi kết quả thứ nhất).
  - *Example / Ví dụ*: `SELECT * FROM A UNION SELECT * FROM B`
  - 💡 *Mẹo ghi nhớ*: UNION (hợp), INTERSECT (giao), EXCEPT (trừ). ALL nghĩa là lấy tất cả (kể cả trùng lặp).

### 158. 트리거 (Trigger / Trình kích hoạt)
- 데이터의 삽입(Insert), 갱신(Update), 삭제(Delete) 등의 이벤트(Event)가 발생할 때마다 관련 작업이 자동으로 수행되는 절차형 SQL이다. (Là SQL thủ tục tự động thực thi khi có sự kiện chèn, cập nhật hoặc xóa dữ liệu).
  - *Example / Ví dụ*: `CREATE TRIGGER my_trigger AFTER INSERT ON my_table...`
  - 💡 *Mẹo ghi nhớ*: Trigger giống như "cò súng", khi có sự kiện (bóp cò) thì sẽ tự động bắn (thực thi).

### 160. 그룹 함수 (Group Functions / Hàm nhóm)
- GROUP BY절에 지정된 그룹별로 속성의 값을 집계할 때 사용된다. (Được sử dụng để tính toán các giá trị thuộc tính theo từng nhóm được chỉ định trong mệnh đề GROUP BY).
- COUNT/SUM/AVG/MAX/MIN: 그룹별 튜플 수/합계/평균/최대값/최소값을 구하는 함수 (Các hàm tính số lượng, tổng, trung bình, giá trị lớn nhất, nhỏ nhất theo nhóm).
  - *Example / Ví dụ*: `SELECT COUNT(id) FROM users GROUP BY age;`
  - 💡 *Mẹo ghi nhớ*: SAM MC (Sum, Avg, Max, Min, Count).

## 프로그래밍 언어 기초 (Programming Language Basics)
### 159. C/JAVA의 자료형 (Data Types / Kiểu dữ liệu)
- **문자 (Character / Ký tự)**: `char` (1Byte) trong C và JAVA.
- **정수 (Integer / Số nguyên)**: `int` (4Byte) trong C và JAVA; `long` (8Byte).
- **논리 (Boolean / Logic)**: `boolean` (1Byte) chỉ có trong JAVA (C dùng 0/1).
  - *Example / Ví dụ*: `int age = 25; boolean isStudent = true;`
  - 💡 *Mẹo ghi nhớ*: 1 Byte = char/boolean, 4 Bytes = int, 8 Bytes = long.

### 162. 변수명 작성 규칙 (Variable Naming Rules / Quy tắc đặt tên biến)
- 영문자, 숫자, _(under bar)를 사용할 수 있다. (Có thể sử dụng chữ cái tiếng Anh, số và dấu gạch dưới).
- 첫 글자는 숫자는 올 수 없다. (Chữ cái đầu tiên không được là số).
- 공백이나 *, +, -, / 등의 특수문자를 사용할 수 없다. (Không được sử dụng khoảng trắng hoặc ký tự đặc biệt).
- 대소문자를 구분한다. (Phân biệt chữ hoa và chữ thường).
- 예약어를 변수명으로 사용할 수 없다. (Không được sử dụng từ khóa dự phòng làm tên biến).
  - *Example / Ví dụ*: Hợp lệ: `my_var_1`, Không hợp lệ: `1_my_var` (bắt đầu bằng số), `my var` (có khoảng trắng).
  - 💡 *Mẹo ghi nhớ*: Chỉ dùng `A-Z, a-z, 0-9, _`. Số không đi đầu. Không dùng từ khóa.

### 163. 가비지 콜렉터 (Garbage Collector / Trình thu gom rác)
- 선언만 하고 사용하지 않는 변수들이 점유한 메모리 공간을 강제로 해제하여 다른 프로그램들이 사용할 수 있도록 하는 것이다. (Tự động giải phóng không gian bộ nhớ do các biến được khai báo nhưng không sử dụng để các chương trình khác có thể sử dụng).
  - *Example / Ví dụ*: Trong Java, Garbage Collector (GC) tự động dọn dẹp các đối tượng không còn được tham chiếu.
  - 💡 *Mẹo ghi nhớ*: "Garbage" (rác) -> Dọn dẹp bộ nhớ không dùng đến.

## 연산자 (Operators)
### 164. 산술 연산자 (Arithmetic Operators / Toán tử số học)
- `%`: 나머지 (Phần dư). 정수만 연산 가능 (Chỉ dùng cho số nguyên).
- `++`: 증가 (Tăng 1).
  - 전치 (Prefix): `++a` (Tăng rồi mới dùng).
  - 후치 (Postfix): `a++` (Dùng rồi mới tăng).
- `--`: 감소 (Giảm 1). `--a` hoặc `a--`.
  - *Example / Ví dụ*: `int a = 5; b = ++a;` -> a=6, b=6.
  - 💡 *Mẹo ghi nhớ*: Prefix (++a) = Làm trước. Postfix (a++) = Làm sau.

### 165. 비트 연산자 (Bitwise Operators / Toán tử bit)
- `&` (and): 모든 비트가 1일 때만 1. (Chỉ bằng 1 khi tất cả các bit đều là 1).
- `^` (xor): 다르면 1, 같으면 0. (Khác nhau là 1, giống nhau là 0).
- `|` (or): 한 비트라도 1이면 1. (Chỉ cần một bit là 1 thì bằng 1).
- `~` (not): 각 비트의 부정. (Phủ định từng bit).
- `<<` / `>>`: 왼쪽/오른쪽 시프트. (Dịch trái/phải bit).
  - *Example / Ví dụ*: `5 & 3` (0101 & 0011) = `1` (0001).
  - 💡 *Mẹo ghi nhớ*: AND (&) khắt khe (đều phải 1). OR (|) dễ dãi (1 cái là đủ). XOR (^) thích sự khác biệt.

### 166. 논리 연산자 (Logical Operators / Toán tử logic)
- `!` (not): 부정 (Phủ định).
- `&&` (and): 모두 참이면 참 (Cả hai đúng thì đúng).
- `||` (or): 하나라도 참이면 참 (Một trong hai đúng thì đúng).
  - *Example / Ví dụ*: `(a > 0) && (b > 0)`
  - 💡 *Mẹo ghi nhớ*: Tương tự như toán tử bit nhưng áp dụng cho giá trị đúng/sai (true/false).

### 167. 조건 연산자 (Conditional Operator / Toán tử điều kiện)
- 조건에 따라 서로 다른 수식을 수행한다. (Thực hiện các biểu thức khác nhau tùy thuộc vào điều kiện).
- `조건 ? 참일 때 : 거짓일 때`
  - *Example / Ví dụ*: `mx = a < b ? b : a;` (Nếu a < b thì mx = b, ngược lại mx = a).
  - 💡 *Mẹo ghi nhớ*: Dấu `?` là hỏi xem điều kiện đúng không, nếu đúng lấy cái trước `:`, sai lấy cái sau `:`.

### 168. 연산자 우선순위 (Operator Precedence / Thứ tự ưu tiên toán tử)
- 단항 (Unary) > 산술 (Arithmetic) > 시프트 (Shift) > 관계 (Relational) > 비트 (Bitwise) > 논리 (Logical) > 조건 (Conditional) > 대입 (Assignment) > 순서 (Comma).
- 산술 연산자 중에서는 `*, /, %` ưu tiên cao hơn `+, -`.
  - *Example / Ví dụ*: `a + b * c` thì phép nhân `*` được thực hiện trước `+`.
  - 💡 *Mẹo ghi nhớ*: Dấu ngoặc () luôn cao nhất. Đơn, Số, Dịch, Quan, Bit, Logic, Điều, Gán.

## 입출력 (Input/Output)
### 169. 주요 서식 문자열 (Format String / Chuỗi định dạng)
- `%d`: 정수형 10진수 (Số nguyên hệ thập phân).
- `%c`: 문자 (Ký tự).
- `%s`: 문자열 (Chuỗi ký tự).
  - *Example / Ví dụ*: `printf("Tuổi: %d", 20);`
  - 💡 *Mẹo ghi nhớ*: d = decimal (số thập phân), c = character (ký tự), s = string (chuỗi).

### 170. printf() 함수 (printf() Function / Hàm in C)
- 인수로 주어진 값을 화면에 출력하는 함수이다. (Hàm in giá trị ra màn hình theo định dạng).
  - *Example / Ví dụ*: `printf("%d, %c", a, b);`
  - 💡 *Mẹo ghi nhớ*: 'f' trong printf là 'format' (định dạng).

### 171. JAVA의 출력 함수 (Output Functions in JAVA / Hàm in Java)
- `printf()`: Định dạng đầu ra. `System.out.printf("%d", r);`
- `print()`: In không xuống dòng. `System.out.print(r + s);`
- `println()`: In và xuống dòng. `System.out.println(r + "은 소수");`
  - 💡 *Mẹo ghi nhớ*: 'ln' trong println là 'line new' (xuống dòng mới).

## 제어문 (Control Statements)
### 172. 단순 if문 (Simple if statement / Câu lệnh if đơn giản)
- 조건이 한 개일 때 사용하는 제어문이다. (Câu lệnh điều khiển khi chỉ có một điều kiện).
  - *Example / Ví dụ*: `if (a > b) printf("참"); else printf("거짓");`
  - 💡 *Mẹo ghi nhớ*: Nếu (if) đúng thì làm, nếu không (else) thì làm cái khác.

### 173. switch문 (switch statement / Câu lệnh switch)
- 조건에 따라 분기할 곳이 여러 곳인 경우 간단하게 처리할 수 있다. (Sử dụng khi có nhiều nhánh rẽ).
- break문이 생략되면 모든 문장이 실행된다. (Nếu thiếu `break`, các câu lệnh bên dưới cũng sẽ được chạy theo hiệu ứng rơi xuyên).
  - *Example / Ví dụ*: `switch(a) { case 1: printf("A"); break; }`
  - 💡 *Mẹo ghi nhớ*: Đừng quên `break`, nếu không nó sẽ trôi xuống tận dưới cùng.

### 174. for문 (for loop / Vòng lặp for)
- 초기값, 최종값, 증가값을 지정하여 정해진 횟수를 반복하는 제어문이다. (Vòng lặp với số lần xác định, bao gồm giá trị khởi tạo, điều kiện kết thúc và bước nhảy).
  - *Example / Ví dụ*: `for (i = 1; i <= 10 ; i++) sum = sum + i;`
  - 💡 *Mẹo ghi nhớ*: Dùng khi biết trước số lần lặp.

### 175. while문 (while loop / Vòng lặp while)
- 조건이 참인 동안 실행할 문장을 반복 수행한다. (Lặp lại chừng nào điều kiện còn đúng).
  - *Example / Ví dụ*: `while (i <= 10) { i++; }`
  - 💡 *Mẹo ghi nhớ*: Kiểm tra điều kiện trước, làm sau. Có thể không chạy lần nào nếu điều kiện sai ngay từ đầu.

### 176. do~while문 (do~while loop / Vòng lặp do~while)
- 무조건 한 번 실행한 다음 조건을 판단하여 탈출 여부를 결정한다. (Thực hiện ít nhất một lần, sau đó mới kiểm tra điều kiện).
  - *Example / Ví dụ*: `do { i++; } while (i <= 10);`
  - 💡 *Mẹo ghi nhớ*: Làm (do) trước, hỏi (while) sau. Chắc chắn chạy ít nhất 1 lần.

## 구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)
### C언어의 구조체 (Struct in C / Cấu trúc trong C)
- 자료의 종류가 다른 변수의 모임이다. (Tập hợp các biến có kiểu dữ liệu khác nhau).
- 예약어 `struct`를 이용해 정의한다. (Định nghĩa bằng từ khóa `struct`).
  - *Example / Ví dụ*: `struct Person { char name[20]; int age; };`
  - 💡 *Mẹo ghi nhớ*: Mảng (Array) lưu các giá trị cùng kiểu, Cấu trúc (Struct) lưu các giá trị khác kiểu.

### 177. 1차원 배열 (1D Array / Mảng 1 chiều)
- 변수들을 일직선상의 개념으로 조합한 배열이다. (Tập hợp các biến trên một đường thẳng).
  - *Example / Ví dụ*: `char a[3] = {'A', 'B', 'C'};`
  - 💡 *Mẹo ghi nhớ*: Chỉ số mảng luôn bắt đầu từ 0.

### 178. 2차원 배열 (2D Array / Mảng 2 chiều)
- 변수들을 평면, 즉 행과 열로 조합한 배열이다. (Tập hợp các biến theo dạng bảng gồm hàng và cột).
  - *Example / Ví dụ*: `int b[2][3] = {{11, 22, 33}, {44, 55, 66}};`
  - 💡 *Mẹo ghi nhớ*: `[hàng][cột]` (Row x Column).

### 179. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng)
- C언어에서는 큰따옴표("")로 묶인 글자는 문자열로 처리된다. (Trong C, chữ nằm trong ngoặc kép được xem là chuỗi).
- 배열에 문자열을 저장하면 널 문자('\0')가 문자열 끝에 자동으로 삽입된다. (Khi lưu chuỗi vào mảng, ký tự null `\0` tự động được thêm vào cuối).
  - *Example / Ví dụ*: `char a[5] = "love";` (Bao gồm l, o, v, e, \0).
  - 💡 *Mẹo ghi nhớ*: Độ dài mảng phải lớn hơn số ký tự của chuỗi ít nhất 1 (để chứa `\0`).

### 180. 포인터와 포인터 변수 (Pointers / Con trỏ)
- 포인터 변수를 선언할 때는 자료형 뒤에 `*`를 붙인다. (Khai báo biến con trỏ bằng dấu `*`).
- 변수의 주소를 알아낼 때는 `&`를 붙인다. (Lấy địa chỉ của biến bằng dấu `&`).
- 실행문에서 포인터 변수에 `*`를 붙이면 해당 변수가 가리키는 곳의 값을 의미한다. (Dùng `*` trước con trỏ để lấy giá trị tại địa chỉ đó).
  - *Example / Ví dụ*: `int a = 50; int *b = &a; printf("%d", *b);` (In ra 50).
  - 💡 *Mẹo ghi nhớ*: `&` là địa chỉ (Address), `*` là giá trị (Value).

### 181. 포인터와 배열 (Pointer and Array / Con trỏ và mảng)
- 배열을 포인터 변수에 저장한 후 포인터를 이용해 배열의 요소에 접근할 수 있다. (Có thể dùng con trỏ để truy cập các phần tử mảng).
- 배열의 대표명은 배열의 첫 번째 요소의 주소와 같다. (Tên mảng chính là địa chỉ của phần tử đầu tiên).
  - *Example / Ví dụ*: `int a[5]; int *b = a;` tương đương với `b = &a[0];`.
  - 💡 *Mẹo ghi nhớ*: `a[i]` hoàn toàn tương đương với `*(a + i)`.

## Python 기초 (Python Basics)
### 161. Python의 시퀀스 자료형 (Python Sequence Types / Kiểu chuỗi trong Python)
- **리스트 (List)**: 요소의 추가, 삭제, 변경 가능 (Có thể thêm, xóa, sửa phần tử).
- **튜플 (Tuple)**: 요소의 추가, 삭제, 변경 불가능함 (Không thể thay đổi phần tử).
- **range**: 연속된 숫자를 생성함 (Tạo dãy số liên tiếp).
  - *Example / Ví dụ*: List `[1, 2]`, Tuple `(1, 2)`.
  - 💡 *Mẹo ghi nhớ*: List dùng `[]` và linh hoạt. Tuple dùng `()` và cố định (bất biến).

### 185. Python의 리스트 (Python List / Danh sách trong Python)
- 크기를 지정하지 않는다. 하나의 리스트에 다양한 자료형을 섞어 저장할 수 저장할 수 있다. (Không cần chỉ định kích thước. Có thể chứa nhiều kiểu dữ liệu khác nhau).
- 위치는 0부터 시작한다. (Chỉ số bắt đầu từ 0).
  - *Example / Ví dụ*: `a = [10, 'mike', 23.45]`
  - 💡 *Mẹo ghi nhớ*: Python List giống như một cái túi thần kỳ, có thể bỏ bất cứ thứ gì vào.

### 186. Python의 딕셔너리 (Dictionary / Từ điển)
- 연관된 값을 묶어서 저장하는 용도. (Dùng để lưu trữ dữ liệu theo cặp Khóa - Giá trị).
- 위치값 대신 사용자가 원하는 키를 직접 지정하여 사용한다. (Dùng Khóa tự định nghĩa thay vì chỉ số số học).
  - *Example / Ví dụ*: `d = {'name': 'John', 'age': 25}`
  - 💡 *Mẹo ghi nhớ*: Key-Value (Khóa-Giá trị). Dùng `{}` giống như một từ điển thực sự (tra từ -> ra nghĩa).

### 187. Python의 Range (Python Range / Dãy số)
- 연속된 숫자를 생성하는 것. (Tạo dãy số liên tiếp).
  - `range(5)` -> 0, 1, 2, 3, 4
  - `range(4, 9)` -> 4, 5, 6, 7, 8
  - `range(1, 15, 3)` -> 1, 4, 7, 10, 13
  - 💡 *Mẹo ghi nhớ*: `range(start, stop, step)`. Bao gồm `start`, nhưng **không** bao gồm `stop`.

### 188. Python의 슬라이스 (Python Slice / Cắt chuỗi/mảng)
- 객체에서 일부를 잘라 반환하는 기능. (Trích xuất một phần của chuỗi hoặc mảng).
- `a[1:3]`: Lấy từ index 1 đến 2.
- `a[0:5:2]`: Lấy từ 0 đến 4, bước nhảy 2.
- `a[3:]`: Lấy từ index 3 đến cuối.
- `a[:3]`: Lấy từ đầu đến index 2.
- `a[::-1]`: Đảo ngược mảng.
  - 💡 *Mẹo ghi nhớ*: `[start : stop : step]`. Giống range, không bao gồm `stop`.

### 182. Python의 input() 함수 (Python input() Function / Hàm nhập)
- 키보드로 입력받아 변수에 저장하는 함수이다. (Nhập từ bàn phím và lưu vào biến).
- 입력되는 값은 기본적으로 문자열로 취급된다. (Giá trị mặc định luôn là chuỗi).
  - *Example / Ví dụ*: `a = input('Nhập tên:')`

### 183. Python의 print() 함수 (Python print() Function / Hàm in)
- 인수로 주어진 값을 출력한다. (In giá trị ra màn hình).
  - *Example / Ví dụ*: `print(82, 24, sep='-', end=',')` -> `82-24,`
  - 💡 *Mẹo ghi nhớ*: `sep` = phân cách giữa các đối số, `end` = ký tự kết thúc (mặc định là xuống dòng `\n`).

### 184. 입력 값의 형변환 (Input Type Casting / Ép kiểu dữ liệu đầu vào)
- `input()` 함수는 무조건 문자열로 저장하므로, 숫자로 사용하려면 형 변환이 필요하다. (Vì `input()` trả về chuỗi, cần ép kiểu nếu muốn dùng số).
- 변환할 데이터가 1개: `a = int(input())`
- 변환할 데이터가 2개 이상: `a, b = map(int, input().split())`
  - 💡 *Mẹo ghi nhớ*: `split()` để cắt khoảng trắng, `map()` để ép tất cả sang kiểu nguyên `int`.



### 189. Python의 for문 (Python for loop)
- **range를 이용하는 방식 (Dùng range)**: `for i in range(1, 11): sum = sum + i`
- **리스트를 이용하는 방식 (Dùng list)**: `for i in a:` (với `a` là list).
  - 💡 *Mẹo ghi nhớ*: `for item in tập_hợp`. Lặp qua từng phần tử.

### 191. Python의 클래스 및 메소드 (Python Classes & Methods / Lớp và phương thức)
- 클래스 없이 메소드만 단독으로 사용할 수 있다. (Có thể sử dụng phương thức độc lập mà không cần lớp).
- 클래스를 사용하려면 속성과 메소드를 정의한 후 객체를 선언한다. (Để dùng lớp, định nghĩa thuộc tính và phương thức, sau đó khởi tạo đối tượng).
  - *Example / Ví dụ*: `def calc(x, y): return x * y` (Hàm độc lập). `class Cls: x = 10` (Lớp).
  - 💡 *Mẹo ghi nhớ*: Python hỗ trợ cả lập trình thủ tục (như C) và hướng đối tượng (OOP). Tham số đầu tiên của hàm trong lớp luôn là `self`.

## 스크립트 및 운영체제 (Script Languages & Operating Systems)
### 193. 스크립트 언어의 종류 (Types of Scripting Languages / Các loại ngôn ngữ kịch bản)
- **자바스크립트 (JavaScript)**: 클라이언트용 웹 동작 제어 (Phía client, điều khiển hành vi web).
- **PHP**: 서버용 스크립트 언어 (Phía server, dùng trên Linux, Unix, Windows).
- **파이썬 (Python)**: 대화형 인터프리터 언어 (Ngôn ngữ thông dịch tương tác).
- **쉘 스크립트 (Shell Script)**: 명령어들의 조합 (Tập hợp các lệnh shell).
- **Basic**: 절차지향 대화형 인터프리터 (Thông dịch tương tác, hướng thủ tục).
  - 💡 *Mẹo ghi nhớ*: JS = Client Web, PHP = Server, Python = Thông dịch, Shell = Lệnh HĐH.

### 194. 쉘 스크립트 제어문 (Shell Script Control Statements)
- **선택형 (Điều kiện)**: `if`, `case`
- **반복형 (Vòng lặp)**: `for`, `while`, `until`

### 195. 라이브러리 (Libraries / Thư viện)
- **표준 (Standard)**: 기본적으로 포함된 모듈 (Tích hợp sẵn trong ngôn ngữ).
- **외부 (External)**: 다운받아 설치한 후 사용 (Phải tải và cài đặt từ bên ngoài).
  - 💡 *Mẹo ghi nhớ*: Built-in = Không cần cài, External = Cần pip/npm/v.v.

### 196. C언어의 stdlib.h (Standard Library in C)
- 자료형 변환, 난수 발생, 메모리 할당 기능을 제공한다. (Cung cấp chức năng ép kiểu, tạo số ngẫu nhiên, cấp phát bộ nhớ).
- 주요 함수 (Các hàm chính): `atoi`, `atof`, `srand`, `rand`, `malloc`, `free`.

### 197. UNIX의 특징 (Features of UNIX / Đặc điểm của UNIX)
- 대부분 C 언어로 작성 (Viết chủ yếu bằng C -> tính di động cao).
- 다중 사용자 (Multi User), 다중 작업 (Multi Tasking) 지원 (Hỗ trợ đa người dùng, đa nhiệm).
- 트리 구조의 파일 시스템 (Hệ thống tập tin cấu trúc cây).
  - 💡 *Mẹo ghi nhớ*: UNIX = C + Cây (Tree) + Đa nhiệm/Đa người dùng.

### 198. UNIX - 커널(Kernel)의 기능 (Functions of Kernel / Chức năng hạt nhân)
- 프로세스, 기억장치, 파일 시스템, 입출력 관리 (Quản lý tiến trình, bộ nhớ, hệ thống tập tin, I/O).
  - 💡 *Mẹo ghi nhớ*: Kernel là "Trái tim" làm mọi công việc cốt lõi phần cứng.

### 199. UNIX - 쉘(Shell)
- 명령어 해석기, 시스템과 사용자 간의 인터페이스 담당. (Trình biên dịch dòng lệnh, giao diện giữa người dùng và HĐH).
  - 💡 *Mẹo ghi nhớ*: Shell là "Vỏ bọc" giao tiếp với Kernel.

### 206. UNIX의 주요 명령어 (UNIX Commands / Lệnh UNIX)
- `fork`: 새로운 프로세스 생성 (Tạo tiến trình mới).
- `uname`: 시스템 정보 표시 (Hiển thị thông tin hệ thống).
- `wait`: 자식 프로세스 종료 대기 (Chờ tiến trình con kết thúc).
- `chmod`: 파일 보호 모드 설정 (Đổi quyền truy cập file).
- `ls`: 파일 목록 확인 (Liệt kê file).
- `cat`: 파일 내용 표시 (Xem nội dung file).
- `chown`: 소유자 변경 (Đổi chủ sở hữu file).
  - 💡 *Mẹo ghi nhớ*: fork (nhân bản, nĩa), chmod (change mode), chown (change owner).

## 운영체제 - 메모리 및 프로세스 관리 (OS - Memory & Process Management)
### 200. 기억장치의 배치 전략 (Memory Placement Strategies / Chiến lược cấp phát bộ nhớ)
- **최초 적합 (First Fit)**: 첫 번째 분할 영역에 배치 (Vị trí trống đầu tiên đủ lớn).
- **최적 적합 (Best Fit)**: 단편화가 가장 작은 영역 (Vị trí trống vừa vặn nhất, để lại ít rác nhất).
- **최악 적합 (Worst Fit)**: 단편화가 가장 큰 영역 (Vị trí trống lớn nhất).
  - 💡 *Mẹo ghi nhớ*: First = Nhanh nhất. Best = Tiết kiệm nhất. Worst = Còn lại khoảng trống lớn nhất.

### 201. 페이지 교체 알고리즘 - FIFO (Page Replacement - FIFO / Thuật toán thay thế trang)
- 가장 먼저 들어와서 가장 오래 있었던 페이지를 교체 (Thay thế trang vào bộ nhớ sớm nhất - First In First Out).

### 202. 스래싱 (Thrashing)
- 프로세스 처리 시간보다 페이지 교체 시간이 더 많아지는 현상 (Hiện tượng mất nhiều thời gian cho việc tráo đổi trang bộ nhớ hơn là thực thi tiến trình).
  - 💡 *Mẹo ghi nhớ*: Thrashing = Kẹt xe bộ nhớ (quá tải).

### 203. 프로세스 상태 (Process States / Trạng thái tiến trình)
- 제출(Submit) → 접수(Hold) → 준비(Ready) → 실행(Run) → 대기(Wait/Block) → 종료(Exit).
  - 💡 *Mẹo ghi nhớ*: Nộp -> Nhận -> Chờ chạy -> Chạy -> (Tạm dừng nếu cần) -> Xong.

### 204. 스케줄링 - SJF (Shortest Job First / Việc ngắn làm trước)
- 실행 시간이 가장 짧은 프로세스에게 먼저 CPU 할당 (Ưu tiên tiến trình có thời gian thực thi ngắn nhất).

### 205. 스케줄링 - HRN (Highest Response-ratio Next)
- 우선순위 = `(대기 시간 + 서비스 시간) / 서비스 시간`
- (Priority = (Wait time + Service time) / Service time).
  - *Example / Ví dụ*: Đợi 10, Chạy 5 => `(10+5)/5 = 3`.
  - 💡 *Mẹo ghi nhớ*: Công thức = `(Đợi + Chạy) / Chạy`. Số càng lớn càng ưu tiên. Giải quyết nhược điểm của SJF (tiến trình dài bị bỏ đói).

## 네트워크 통신 (Network Communication)
### 207. 인터넷 주소 체계 - IPv4 (IPv4 Addressing)
- 8비트씩 4부분, 총 32비트 (4 phần, mỗi phần 8 bit -> 32 bit). A~E 클래스.

### 208. 인터넷 주소 체계 - IPv6 (IPv6 Addressing)
- 16비트씩 8부분, 총 128비트 (8 phần, mỗi phần 16 bit -> 128 bit, dùng hệ Hex).
- 유니캐스트(Unicast), 멀티캐스트(Multicast), 애니캐스트(Anycast).
  - 💡 *Mẹo ghi nhớ*: IPv4 = 32 bit (dấu `.`). IPv6 = 128 bit (dấu `:`).

### OSI 7계층 (OSI 7 Layers)
- **209. 데이터 링크 계층 (Data Link)**: 인접 시스템 간 신뢰성 있는 전송. 흐름/오류 제어 (HDLC, PPP). (Truyền tải tin cậy giữa các nút lân cận).
- **210. 네트워크 계층 (Network)**: 경로 설정, 패킷 라우팅. (Định tuyến, chuyển mạch gói).
- **211. 전송 계층 (Transport)**: 종단 간 투명한 데이터 전송. (Truyền tải End-to-End, TCP/UDP).
- **212. 세션 계층 (Session)**: 대화 제어, 동기화 (Quản lý phiên, đồng bộ hóa hội thoại).
  - 💡 *Mẹo ghi nhớ*: Data Link = Frame/MAC. Network = IP/Routing. Transport = TCP/UDP/Port. Session = Dialog/Token.

### 213. 네트워크 관련 주요 장비 (Network Devices / Thiết bị mạng)
- **리피터 (Repeater)**: 신호 재생 (Khuếch đại tín hiệu).
- **브리지 (Bridge)**: LAN 연결 (Kết nối mạng LAN cùng loại).
- **라우터 (Router)**: 최적 경로 선택 (Chọn đường đi tối ưu).
- **스위치 (Switch)**: 여러 랜선 연결 (Chuyển mạch mạng LAN).
- **브라우터 (Brouter)**: Bridge + Router.

### TCP/IP 프로토콜 (TCP/IP Protocols)
- **214. MQTT**: IoT에서 사용하는 발행-구독 메시징 (Giao thức Publish/Subscribe cho IoT).
- **215. TCP**: 신뢰성 있는 양방향 연결형 서비스 (Kết nối hai chiều, đáng tin cậy).
- **216. UDP**: 비연결형, 빠른 속도, 실시간 전송 유리 (Không kết nối, truyền nhanh, hợp với Real-time).
  - 💡 *Mẹo ghi nhớ*: TCP = Cẩn thận, chậm mà chắc. UDP = Nhanh, mất gói cũng không sao (Video call, Game).

## 소프트웨어 공학 및 실무 (Software Engineering & Practice)
### 231. 오류 데이터 상태 (Error Data States / Trạng thái dữ liệu lỗi)
- **Open**: 보고만 됨 (Mới báo cáo).
- **Assigned**: 개발자에게 전달 (Đã giao cho dev).
- **Fixed**: 수정됨 (Đã sửa).
- **Closed**: 테스트 후 문제 없음 (Đóng lại sau khi test OK).
- **Deferred**: 수정 연기 (Hoãn lại).
- **Classified**: 오류 아님 (Xác nhận không phải lỗi).

### 232. 배치 프로그램 필수 요소 (Batch Program Elements / Yếu tố của Batch)
- 대용량 데이터, 자동화, 견고성, 안정성/신뢰성, 성능. (Khối lượng lớn, Tự động hóa, Độ bền bỉ, Tính Ổn định, Hiệu suất).
  - 💡 *Mẹo ghi nhớ*: Batch là tự động chạy ngầm khối lượng lớn, nên không được chết giữa chừng.

### 233. C/C++ 데이터 타입 크기 추가 (C/C++ Data Type Sizes / Kích thước kiểu dữ liệu C++)
- C++에서는 `long long` (8Byte)와 `double` (8Byte), `long double` (8Byte) 등 확장된 크기를 가짐. (Lưu ý các kiểu dữ liệu mở rộng trong C/C++).


## 프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)
### 236. Python의 시퀀스 자료형 (Python Sequence Type / Kiểu chuỗi trong Python - Nhắc lại)
- **리스트 (List)**: Khác kiểu dữ liệu, thêm xóa được.
- **튜플 (Tuple)**: Không thể thay đổi (immutable).
- **range**: Sinh dãy số liên tiếp.

### 구조체 정의 예 (Struct Definition Example / Ví dụ định nghĩa Struct)
- C언어: `struct sawon { char name[10]; int pay; };`

### 235. JAVA의 데이터 타입 크기 (JAVA Data Type Sizes / Kích thước kiểu dữ liệu JAVA)
- **문자 (Char)**: `char` (2Byte - Khác với C là 1Byte).
- **정수 (Integer)**: `byte` (1Byte), `short` (2Byte), `int` (4Byte), `long` (8Byte).
- **실수 (Float)**: `float` (4Byte), `double` (8Byte).
- **논리 (Boolean)**: `boolean` (1Byte).
  - 💡 *Mẹo ghi nhớ*: Java dùng Unicode nên `char` là 2 Bytes. Có thêm kiểu `byte` (1 Byte).

### 237. 변수의 개요 및 헝가리안 표기법 (Variables & Hungarian Notation / Biến và Ký pháp Hungary)
- **헝가리안 표기법 (Hungarian Notation)**: 변수 선언 시 변수명에 데이터 타입을 명시하는 것. (Gắn tiền tố kiểu dữ liệu vào tên biến, vd: `strName`, `nAge`).
- Mọi câu lệnh khai báo biến trong C/Java đều phải kết thúc bằng dấu chấm phẩy `;`.

### 238. 가비지 콜렉터 (Garbage Collector / Trình thu gom rác - Nhắc lại)
- 메모리 공간을 강제로 해제 (Giải phóng không gian bộ nhớ không còn sử dụng).

## 연산자 심화 (Operators - Advanced)
### 240. 관계 연산자 (Relational Operators / Toán tử quan hệ)
- 두 수의 관계를 비교하여 참(1) 또는 거짓(0)을 결과로 얻는다. (So sánh hai số trả về 1 (Đúng) hoặc 0 (Sai)).
- `==` (Bằng), `!=` (Khác), `>`, `>=`, `<`, `<=`.
  - 💡 *Mẹo ghi nhớ*: Trong C, 0 là Sai, mọi số khác 0 đều được coi là Đúng (Thường dùng 1).

### 243. 대입 연산자 (Assignment Operators / Toán tử gán)
- 연산 후 결과를 대입한다. (Thực hiện phép tính xong rồi gán kết quả lại cho biến).
- `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`.
  - *Example / Ví dụ*: `a += 1` tương đương `a = a + 1`.

*(Lưu ý: Các toán tử 산술 (Số học), 비트 (Bit), 논리 (Logic), 조건 (Điều kiện), ưu tiên 연산자 우선순위 đã được trình bày ở phần trước).*

## 입출력 심화 (Input/Output - Advanced)
### 246. scanf() 함수 (scanf() Function / Hàm nhập trong C)
- C언어의 표준 입력 함수로, 키보드로 입력받아 변수에 저장한다. (Hàm nhập chuẩn của C, lấy dữ liệu từ bàn phím lưu vào biến).
- 형식: `scanf(서식 문자열, &변수)` (Định dạng, &Tên_biến).
- 변수에 주소연산자 `&`를 붙여야 한다. (Bắt buộc phải có toán tử địa chỉ `&` trước tên biến, trừ chuỗi).
  - *Example / Ví dụ*: `scanf("%3d", &a);` (Nhập số nguyên tối đa 3 chữ số vào địa chỉ biến a).
  - 💡 *Mẹo ghi nhớ*: "Scan" là quét (đọc vào), luôn nhớ phải có dấu `&` để chỉ đường cho dữ liệu đi vào bộ nhớ.

### 247. 서식 문자열 (Format String / Chuỗi định dạng - Bổ sung)
- `%u`: 부호없는 정수 10진수 (Số nguyên hệ 10 không dấu).
- `%o`: 정수 8진수 (Hệ bát phân - Octal).
- `%x`: 정수 16진수 (Hệ thập lục phân - Hexadecimal).
- `%e`: 지수형 실수 (Số thực dạng số mũ - Exponential).
- `%p`: 주소를 16진수로 (Địa chỉ con trỏ hệ 16).
  - 💡 *Mẹo ghi nhớ*: o = octal, x = hex, u = unsigned, p = pointer.

### 249. 주요 제어문자 (Major Control Characters / Ký tự điều khiển)
- `\n`: new line (Xuống dòng).
- `\b`: backspace (Lùi lại 1 ký tự).
- `\t`: tab (Lùi khoảng cách tab).
- `\r`: carriage return (Về đầu dòng hiện tại).
- `\0`: null (Ký tự rỗng).
- `\'`: in dấu nháy đơn.
- `\"`: in dấu nháy kép.
- `\\`: in dấu xuyệt ngược.

### 250. JAVA에서의 표준 출력 (JAVA Standard Output / Đầu ra chuẩn trong JAVA)
- **출력 포맷**: `System.out.printf("%-8.2f", 200.2);`
  - `-`: Căn trái (왼쪽 정렬).
  - `8`: Tổng 8 ký tự (8자리).
  - `.2`: 2 chữ số thập phân (소수점 이하 2자리).
  - Kết quả: `200.20   ` (Thêm khoảng trắng phía sau).
- **문자열 연결**: `System.out.print("abc" + "def");` (Dùng dấu `+` để nối chuỗi).

### 251. 단순 if문 (Simple if statement / Câu lệnh if đơn giản - Nhắc lại)
- Nếu có nhiều hơn 1 câu lệnh thực thi, phải bọc trong `{ }` (Ngoặc nhọn).
  - *Example / Ví dụ*: `if(a > 10) { b = a - 10; printf("%d", b); }`


## 제어문 심화 (Control Statements - Advanced)
### 252. 다중 if문 (Multi if statement / Câu lệnh if nhiều nhánh)
- 조건이 여러 개일 때 사용하는 제어문이다. (Sử dụng khi có nhiều điều kiện khác nhau).
- `if (조건1) ... else if (조건2) ... else ...`
  - *Example / Ví dụ*: `if(jum >= 90) printf("A"); else if(jum >= 80) printf("B"); else printf("F");`
  - 💡 *Mẹo ghi nhớ*: Xếp hạng hoặc các điều kiện loại trừ lẫn nhau thì dùng `else if`.

### 253. switch문 (switch statement / Câu lệnh switch - Bổ sung)
- `case`문의 레이블에는 상수만 지정할 수 있으며 변수는 지정할 수 없다. (Nhãn `case` chỉ chấp nhận hằng số, không dùng biến).
- `int`, `char`, `enum`형의 상수만 가능하다. (Chỉ dùng được số nguyên, ký tự, hoặc kiểu enum).
  - *Example / Ví dụ*: `switch (jum / 10) { case 10: case 9: printf("A"); break; ... }` (Chia cho 10 để tính điểm thập phân thành số nguyên).
  - 💡 *Mẹo ghi nhớ*: `switch` thích sự chính xác tuyệt đối (giá trị cụ thể), không thích sự so sánh lớn/nhỏ.

### 254. for문 (for loop / Vòng lặp for - Bổ sung)
- 처음부터 조건식을 만족하지 못하면 한 번도 수행하지 않는다. (Nếu điều kiện sai ngay từ đầu, vòng lặp không chạy lần nào).
- `for(초기값; 최종값조건; 증가값) { 실행문; }`

### 255. while문 (while loop / Vòng lặp while - Bổ sung)
- `while(조건) { 실행문; }`
- Điều kiện được kiểm tra trước, nếu sai từ đầu sẽ bỏ qua.
  - *Example / Ví dụ*: `while(a < 5) { a++; hap += a; }`

### 256. do~while문 (do~while loop / Vòng lặp do~while - Bổ sung)
- 실행할 문장을 무조건 한 번 실행한 다음 조건을 판단. (Thực hiện ít nhất 1 lần rồi mới kiểm tra điều kiện ở cuối).
- `do { 실행문; } while(조건);` (Nhớ có dấu chấm phẩy ở cuối `while`).

### 257. break, continue (Keywords / Từ khóa điều khiển vòng lặp)
- **break**: switch문이나 반복문 안에서 나오면 블록을 벗어난다. (Thoát ngay lập tức khỏi vòng lặp hoặc switch).
- **continue**: 이후의 문장을 실행하지 않고 반복문의 처음으로 옮긴다. (Bỏ qua các lệnh bên dưới và quay lại đầu vòng lặp để tiếp tục vòng lặp mới).
  - *Example / Ví dụ*: `if(a % 2 == 0) continue; hap += a;` (Bỏ qua số chẵn, chỉ cộng số lẻ).
  - 💡 *Mẹo ghi nhớ*: `break` = Phá vỡ (thoát ra). `continue` = Tiếp tục (bước tiếp).

## 배열 심화 (Arrays - Advanced)
### 258. 배열과 1차원 배열 (Array & 1D Array / Mảng 1 chiều - Bổ sung)
- 배열은 행 우선으로 데이터가 할당된다. (Mảng được cấp phát theo thứ tự ưu tiên hàng).
- 첨자 없이 배열 이름을 사용하면 첫 번째 요소의 주소를 지정하는 것과 같다. (Tên mảng không có chỉ số chính là địa chỉ phần tử đầu tiên).
  - *Example / Ví dụ*: Khởi tạo mảng bằng `for` loop: `for(i=0; i<5; i++) a[i] = i+10;`
  - 💡 *Mẹo ghi nhớ*: Mảng trong C/Java đếm từ 0.

### 259. 2차원 배열 (2D Array / Mảng 2 chiều - Bổ sung)
- 변수들을 평면, 즉 행과 열로 조합한 배열. (Mảng kết hợp hàng và cột).
- 형식: `자료형 변수명[행개수][열개수]`
  - *Example / Ví dụ*: `int b[3][3];` (Mảng 3 hàng, 3 cột. Chỉ số hàng 0-2, cột 0-2).
  - Sử dụng vòng lặp lồng nhau (Nested loops) để gán giá trị: `for(i=0; i<3; i++) { for(j=0; j<4; j++) { a[i][j] = ++k; } }`
  - 💡 *Mẹo ghi nhớ*: Array 2D giống như ma trận Toán học. `i` là hàng (bên ngoài), `j` là cột (bên trong).


## 배열과 포인터 심화 (Arrays & Pointers - Advanced)
### 260. 배열의 초기화 (Array Initialization / Khởi tạo mảng)
- 배열 선언 시 초기값을 지정할 수 있다. (Có thể gán giá trị khởi tạo ngay khi khai báo mảng).
- 배열의 크기를 생략하려면 반드시 초기값을 지정해야 한다. (Nếu bỏ trống kích thước mảng trong ngoặc `[]`, bắt buộc phải có giá trị khởi tạo để máy tự đếm).
- 적은 수로 초기화하면 나머지 요소는 0이 입력된다. (Nếu khởi tạo ít phần tử hơn kích thước mảng, các phần tử còn lại tự động bằng 0).
  - *Example / Ví dụ*: `int a[5] = {3};` -> `[3, 0, 0, 0, 0]`.
  - 💡 *Mẹo ghi nhớ*: C/Java không tự làm sạch bộ nhớ trừ khi bạn khởi tạo ít nhất 1 phần tử.

### 261. 배열 형태의 문자열 변수 (String as Array / Chuỗi dưới dạng mảng - Bổ sung)
- 배열에 문자열을 저장할 때는 초기값으로 지정해야 하며, 이미 선언된 배열에는 대입 연산자로 문자열을 통째로 저장할 수 없다. (Chỉ được gán chuỗi trực tiếp lúc khởi tạo. Không được gán chuỗi vào mảng đã khai báo bằng dấu `=`).
- `%s`를 이용해 문자열을 출력할 때는 배열 이름이나 포인터 변수만 적어주면 된다. (Khi in chuỗi bằng `%s`, chỉ cần truyền tên mảng hoặc con trỏ, không cần dấu `&`).

### 262. 포인터와 포인터 변수 (Pointer & Pointer Variable / Con trỏ - Bổ sung)
- 포인터 변수는 동적으로 할당되는 메모리 영역인 **힙(Heap) 영역**에 접근하는 동적 변수이다. (Con trỏ là biến động truy cập vào vùng nhớ Heap được cấp phát động).
- `*` 연산자: 간접 연산자 (Lấy giá trị).
- `&` 연산자: 번지 연산자 (Lấy địa chỉ).
  - 💡 *Mẹo ghi nhớ*: Con trỏ giống như tấm bản đồ (chỉ chứa địa chỉ), dùng `*` để đi đến đích và lấy kho báu (giá trị).

### 263. 포인터와 배열 (Pointer & Array / Con trỏ và mảng - Bổ sung)
- `p + 1`은 메모리 주소가 1 증가하는 것이 아니라 해당 자료형의 크기(int는 4Byte)만큼 증가한다. (`p + 1` không cộng thêm 1 vào địa chỉ, mà cộng thêm kích thước của kiểu dữ liệu, ví dụ int thì cộng thêm 4 Bytes).
  - *Example / Ví dụ*: `p` là `1000` -> `p + 1` là `1004` (với int).

## Python 기본 문법 (Python Basic Syntax)
### 264. Python의 기본 문법 (Python Basic Syntax / Cú pháp cơ bản của Python)
- **자료형 선언 없음**: 변수 선언 시 타입을 명시하지 않는다. (Không cần khai báo kiểu dữ liệu).
- **세미콜론 생략**: 문장 끝에 `;`이 필요 없다. (Không cần dấu chấm phẩy ở cuối câu).
- **연속 할당**: `x, y, z = 10, 20, 30` (Có thể gán liên tiếp nhiều biến).
- **코드 블록**: 콜론(`:`)과 여백(Indentation)으로 구분한다. (Dùng dấu hai chấm và thụt lề để xác định khối lệnh, thay vì dùng `{ }`).
  - 💡 *Mẹo ghi nhớ*: Python yêu cầu thụt lề (thường là 4 spaces) vô cùng khắt khe. Sai thụt lề = Lỗi (IndentationError).

### 265 ~ 269. Python 입출력, 리스트, 딕셔너리, 슬라이스 (Python I/O, List, Dict, Slice - Ôn tập)
*(Các khái niệm này đã được đề cập kỹ ở phần trước, dưới đây là tóm tắt nhanh các điểm chú ý)*:
- **`input()`**: Luôn trả về chuỗi. Dùng `int(input())` để ép kiểu. Đa trị: `map(int, input().split())`.
- **`print()`**: Có thể dùng `sep` (ký tự phân tách) và `end` (ký tự kết thúc).
- **리스트 (List)**: Khai báo bằng `[]` hoặc `list()`. Hỗ trợ chứa nhiều kiểu dữ liệu hỗn hợp.
- **딕셔너리 (Dictionary)**: Khai báo bằng `{}` hoặc `dict()`. Cấu trúc Key:Value.
- **슬라이스 (Slice)**: Cắt `[start:stop:step]`. Nếu bỏ trống `start` thì lấy từ đầu, bỏ trống `stop` thì lấy đến cuối.


## 프로그래밍 언어 종류 및 특징 (Programming Languages Types & Features)
### 275. 절차적 프로그래밍 언어의 종류 (Procedural Programming Languages / Ngôn ngữ lập trình hướng thủ tục)
- **C**: 1972년 데니스 리치 개발, UNIX 일부 구현, 포인터 제공. 고급+저급 특징 모두 가짐. (Phát triển bởi Dennis Ritchie năm 1972, có con trỏ, kết hợp đặc điểm của ngôn ngữ bậc cao và bậc thấp).
- **ALGOL**: 과학 기술 계산용. PASCAL과 C의 모체. (Ngôn ngữ tính toán khoa học, là tiền thân của Pascal và C).
- **COBOL**: 사무 처리용. 영어 문장 형식, 4개의 DIVISION. (Ngôn ngữ xử lý nghiệp vụ, cú pháp giống tiếng Anh, chia làm 4 phần - DIVISION).
- **FORTRAN**: 과학 기술 계산용. 수학 공식 형태. (Ngôn ngữ tính toán khoa học kỹ thuật, cú pháp như công thức toán).
  - 💡 *Mẹo ghi nhớ*: C = Pointer, ALGOL = Algorithm, COBOL = Business, FORTRAN = Formula Translation.

### 276. 객체지향 프로그래밍 언어의 종류 (Object-Oriented Languages / Ngôn ngữ lập trình hướng đối tượng)
- **JAVA**: 분산 네트워크, 멀티스레드, 운영체제에 독립적(이식성 강함). (Hỗ trợ mạng phân tán, đa luồng, chạy độc lập không phụ thuộc hệ điều hành nhờ JVM).
- **C++**: C언어에 객체지향 개념 적용. (Bổ sung tính năng OOP vào ngôn ngữ C).
- **Smalltalk**: 1세대, 순수한 객체지향, 최초의 GUI 제공. (Ngôn ngữ OOP thuần túy thế hệ 1, ngôn ngữ đầu tiên cung cấp giao diện đồ họa).
  - 💡 *Mẹo ghi nhớ*: Java = Đa luồng/Độc lập HĐH, Smalltalk = Thuần OOP/GUI đầu tiên.

### 278. 선언형 프로그래밍 언어의 종류 (Declarative Programming Languages / Ngôn ngữ lập trình khai báo)
- **HTML**: 하이퍼텍스트 문서. 단순 텍스트. (Ngôn ngữ đánh dấu văn bản siêu liên kết).
- **XML**: 웹에서 구조화된 문서 상호 교환, 사용자 정의 태그. (Ngôn ngữ đánh dấu mở rộng, cho phép tự định nghĩa thẻ Tag, dùng để trao đổi dữ liệu).
- **LISP**: 인공지능(AI), 연결 리스트, 재귀 호출. (Dùng trong AI, dùng danh sách liên kết, đệ quy nhiều).
- **PROLOG**: 인공지능, 논리적 추론. (Dùng trong AI, suy luận logic).
- **Haskell**: 함수형 언어, 부작용(Side Effect) 없음. (Ngôn ngữ hàm, không có hiệu ứng phụ).
  - 💡 *Mẹo ghi nhớ*: AI = LISP & PROLOG. XML = Tag tự định nghĩa. Haskell = Hàm thuần túy.

## 라이브러리 및 예외 처리 (Libraries & Exception Handling)
### 280. C언어의 표준 라이브러리 (C Standard Libraries / Thư viện chuẩn C)
- **stdio.h**: 입출력 (`printf`, `scanf`, `fopen`).
- **math.h**: 수학 함수 (`sqrt`, `pow`, `abs`).
- **string.h**: 문자열 처리 (`strlen`, `strcpy`, `strcmp`).
- **stdlib.h**: 자료형 변환, 메모리 할당, 난수 (`atoi`, `rand`, `malloc`, `free`).
- **time.h**: 시간 처리 (`time`, `clock`).
  - 💡 *Mẹo ghi nhớ*: io = Input/Output, lib = Library (chung chung như cấp phát bộ nhớ), str = String.

### 281. 예외 처리 (Exception Handling / Xử lý ngoại lệ)
- 프로그램의 정상적인 실행을 방해하는 조건을 예외라고 한다. (Điều kiện làm gián đoạn chương trình gọi là ngoại lệ).
- 예외 발생 시 대처하는 루틴을 작성하는 것 (Viết mã để xử lý các sự cố này mà không làm sập chương trình).
- C++, Java, JS는 내장 기능 제공. (Các ngôn ngữ hiện đại có tích hợp sẵn như `try-catch`).
  - 💡 *Mẹo ghi nhớ*: Exception = Bắt lỗi chủ động.

## 운영체제 (Operating Systems)
### 282. 운영체제의 정의 및 평가 기준 (OS Definition & Evaluation Criteria / Định nghĩa và tiêu chí đánh giá HĐH)
- 자원을 효율적으로 관리하고 사용자 환경을 제공하는 시스템 소프트웨어. (Phần mềm hệ thống quản lý tài nguyên và cung cấp môi trường làm việc cho người dùng).
- **평가 기준 (Tiêu chí đánh giá)**:
  1. **처리 능력 (Throughput)**: 양 (Số lượng công việc xử lý trong 1 đơn vị thời gian - Càng cao càng tốt).
  2. **반환 시간 (Turn Around Time)**: 걸린 시간 (Thời gian từ lúc gửi yêu cầu đến lúc hoàn thành - Càng thấp càng tốt).
  3. **사용 가능도 (Availability)**: 즉시 사용 가능 정도 (Độ sẵn sàng, sử dụng được ngay khi cần - Càng cao càng tốt).
  4. **신뢰도 (Reliability)**: 정확하게 해결하는 정도 (Mức độ tin cậy, tính toán chính xác - Càng cao càng tốt).

### 283. 운영체제의 구성 (OS Components / Cấu trúc HĐH)
- **제어 프로그램 (Control Program - Chương trình điều khiển)**:
  1. **감시 (Supervisor)**: 핵심, 자원 할당 감시 (Giám sát cốt lõi, cấp phát tài nguyên).
  2. **작업 관리 (Job Management)**: 작업 순서와 방법 관리 (Quản lý thứ tự và phương pháp chạy job).
  3. **데이터 관리 (Data Management)**: 파일/데이터 처리 및 전송 (Quản lý file và dữ liệu).
- **처리 프로그램 (Processing Program - Chương trình xử lý)**:
  1. **언어 번역 (Language Translator)**: 컴파일러, 어셈블러 (Trình biên dịch, hợp ngữ).
  2. **서비스 (Service)**: 정렬/병합, 유틸리티 (Các tiện ích, sắp xếp, gộp).
  - 💡 *Mẹo ghi nhớ*: Điều khiển gồm Giám sát, Công việc, Dữ liệu (GCD - Giám đốc Công ty Dữ liệu). Xử lý gồm Dịch ngôn ngữ, Tiện ích (DT - Dịch Thuật).

### 284. 운영체제의 기능 (OS Functions / Chức năng HĐH)
- 프로세서, 기억장치, 입출력 장치, 파일 등의 자원 관리. (Quản lý CPU, Bộ nhớ, I/O, File).
- **선점형 멀티태스킹 (Preemptive Multi-Tasking)**: 응용 프로그램 강제 종료 및 자원 반환 가능. (Đa nhiệm ưu tiên, OS có quyền thu hồi CPU từ tiến trình bị treo).
- **PnP (Plug and Play)**: 환경 자동 구성. (Cắm là chạy, tự động nhận cấu hình phần cứng).


### 285. Windows 특징 (Windows OS Features)
- **GUI (Graphic User Interface)**: 마우스로 아이콘 선택 (Giao diện đồ họa người dùng).
- **선점형 멀티태스킹 (Preemptive Multi-Tasking)**: 응용 프로그램 강제 종료 가능.
- **PnP (Plug and Play)**: 하드웨어 설치 시 환경 자동 구성 (Cắm là chạy).
- **OLE (Object Linking and Embedding)**: 개체를 다른 문서에 연결/삽입 (Chèn hoặc liên kết đối tượng giữa các ứng dụng).
- **255자의 긴 파일명**: 최대 255자 (VFAT), 한글 127자. (Tên file tối dài tối đa 255 ký tự).

### 286. UNIX의 특징 (UNIX Overview / Đặc điểm UNIX - Bổ sung)
- **시분할 시스템 (Time Sharing System)**: 시간을 분할하여 대화식으로 운영.
- **개방형 시스템 (Open System)**: 소스 공개. (Hệ thống mở, mã nguồn mở).
- **네트워킹 (Networking)**: 통신망 관리용으로 적합.

### 287. UNIX 시스템의 구성 (UNIX System Structure / Cấu trúc hệ thống UNIX)
- **커널 (Kernel)**: 핵심, 메모리 상주, 하드웨어 보호 및 자원 관리. (Lõi HĐH, thường trú trong RAM).
- **쉘 (Shell)**: 명령어 해석기, 인터페이스, 주기억장치에 상주하지 않음. (Trình thông dịch lệnh, giao diện người dùng, không thường trú trong RAM).
- **유틸리티 (Utility)**: 에디터, 컴파일러 등. (Các chương trình tiện ích).

### 288. 파일 디스크립터 (File Descriptor / FCB - Khối điều khiển tập tin)
- 파일을 관리하기 위한 시스템 제어 블록 (Khối dữ liệu chứa thông tin quản lý tập tin).
- 사용자가 직접 참조할 수 없다. (Người dùng không thể truy cập trực tiếp).

## 가상기억장치 및 페이지 교체 (Virtual Memory & Page Replacement)
### 290. 페이징 기법 (Paging / Phân trang)
- 프로그램을 **동일한 크기**로 나눔 (Chia chương trình thành các phần có kích thước BẰNG NHAU).
- 프로그램 단위 = 페이지 (Page), 기억장치 단위 = 페이지 프레임 (Page Frame).
- **내부 단편화 (Internal Fragmentation)** 발생 가능. (Có thể xảy ra phân mảnh trong).

### 291. 세그먼테이션 기법 (Segmentation / Phân đoạn)
- 프로그램을 배열이나 함수 같은 **다양한 크기의 논리적인 단위**로 나눔. (Chia theo khối logic kích thước KHÁC NHAU).
- **외부 단편화 (External Fragmentation)** 발생 가능. (Có thể xảy ra phân mảnh ngoài).
  - 💡 *Mẹo ghi nhớ*: Page = Kích thước cố định (Sinh ra rác bên trong). Segment = Kích thước logic (Sinh ra rác bên ngoài).

### 292. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang)
- **OPT (Optimal)**: 앞으로 가장 오랫동안 사용하지 않을 페이지 교체. (Thay thế trang sẽ lâu được dùng nhất trong tương lai - Tốt nhất nhưng khó thực hiện).
- **FIFO (First In First Out)**: 가장 먼저 들어온 페이지 교체. (Vào trước ra trước).
- **LRU (Least Recently Used)**: 최근에 가장 오랫동안 사용하지 않은 페이지 교체. (Thay thế trang lâu nhất chưa được truy cập).
- **LFU (Least Frequently Used)**: 사용 빈도가 가장 적은 페이지 교체. (Thay thế trang có số lần truy cập ít nhất).
- **NUR (Not Used Recently)**: 참조 비트와 변형 비트 사용. (Tương tự LRU nhưng dùng 2 bit để theo dõi).

### 293. 페이지 크기 (Page Size / Kích thước trang)
- **작을 경우 (Kích thước nhỏ)**: 단편화 감소, 매핑 늦어짐, 디스크 접근 많아짐. (Phân mảnh ít, nhưng bảng ánh xạ lớn, truy cập ổ đĩa nhiều hơn).
- **클 경우 (Kích thước lớn)**: 단편화 증가, 매핑 빨라짐, 불필요한 내용까지 적재될 수 있음. (Phân mảnh nhiều, ánh xạ nhanh, có thể load cả những phần thừa).

### 294. Locality (국부성 / Tính địa phương)
- 프로세스가 실행되는 동안 주기억장치의 일부 페이지만 집중적으로 참조하는 성질. (Tiến trình có xu hướng chỉ tập trung truy cập một số trang cụ thể).
- **시간 구역성 (Temporal Locality)**: Loop, 스택, 변수 (Vòng lặp, stack, biến - Truy cập cùng 1 chỗ nhiều lần).
- **공간 구역성 (Spatial Locality)**: 배열 순회, 순차적 코드 (Mảng, mã tuần tự - Truy cập các ô nhớ cạnh nhau).

### 295. 워킹 셋 (Working Set / Tập làm việc)
- 프로세스가 자주 참조하는 페이지들의 집합. (Tập hợp các trang được truy cập thường xuyên nhất).
- 주기억장치에 상주시킴으로써 페이지 부재(Page Fault)를 줄인다. (Giữ trong RAM để giảm thiểu lỗi trang).

### 296. 스래싱 (Thrashing / Hiện tượng tráo đổi quá mức)
- 페이지 교체 시간이 처리 시간보다 많아지는 현상. (Mất thời gian hoán đổi trang nhiều hơn thời gian xử lý thực tế).
- 방지: 다중 프로그래밍 정도 조절, 워킹 셋 유지. (Kiểm soát đa nhiệm, dùng Working Set).

## 프로세스 관리 (Process Management)
### 297. 프로세스 (Process / Tiến trình)
- 실행 중인 프로그램, PCB를 가진 프로그램. (Chương trình đang chạy, có chứa khối PCB).

### 298. PCB (Process Control Block / Khối điều khiển tiến trình)
- 프로세스의 상태, 포인터, 식별자(PID), CPU 레지스터 정보 등 저장. (Lưu trạng thái, PID, bộ nhớ, thanh ghi CPU của tiến trình).

### 299 & 300. 프로세스 상태 전이 및 용어 (Process States & Terms)
- **Dispatch (디스패치)**: 준비(Ready) -> 실행(Run). (Cấp phát CPU cho tiến trình).
- **Wake Up (깨움)**: 대기(Wait) -> 준비(Ready). (Hoàn tất I/O, sẵn sàng chạy lại).
- **Spooling (스풀링)**: 입출력 데이터를 디스크에 한꺼번에 저장. (Lưu đệm vào đĩa để xử lý I/O mượt mà).

### 301. 스레드 (Thread / Luồng)
- 프로세스 내에서의 작업 단위. (Đơn vị thực thi nhỏ nhất bên trong một tiến trình).


### 스레드 및 스케줄링 심화 (Threads & Scheduling - Advanced)
- **스레드의 분류 (Thread Types)**:
  - **사용자 수준 (User-level)**: 라이브러리 사용, 빠르지만 구현 어려움. (Dùng thư viện, nhanh nhưng khó code).
  - **커널 수준 (Kernel-level)**: OS 커널이 관리, 구현 쉽지만 속도 느림. (OS quản lý, dễ code nhưng chậm).
- **스레드 장점**: 병행성 증진, 응답 시간 단축, 기억장소 낭비 감소. (Tăng đồng thời, phản hồi nhanh, tiết kiệm RAM).
- **FCFS (First Come First Service = FIFO)**: 도착한 순서대로 처리, 공평하지만 짧은 작업이 오래 대기할 수 있음. (Đến trước phục vụ trước, công bằng nhưng dễ gây kẹt xe).

### 303. UNIX / LINUX 주요 환경 변수 (Environment Variables / Biến môi trường)
- 명령어에서 사용 시 앞에 `$`를 붙인다. (Thêm `$` phía trước để gọi biến).
- **`$HOME`**: 홈 디렉터리 (Thư mục gốc).
- **`$PATH`**: 실행 파일 경로 (Đường dẫn tìm file thực thi).
- **`$PWD`**: 현재 작업 디렉터리 (Thư mục hiện tại).
- **`$LANG`**: 기본 언어 (Ngôn ngữ mặc định).

### 304. UNIX / LINUX 기본 명령어 (Basic Commands - Bổ sung)
- **`fsck`**: 파일 시스템 검사 및 보수 (Kiểm tra và sửa lỗi File System).
- **`getpid`**: 자신의 프로세스 ID (Lấy PID của bản thân).
- **`getppid`**: 부모 프로세스 ID (Lấy PID của tiến trình cha).

## 네트워크 프로토콜 및 장비 심화 (Network Protocols & Devices - Advanced)
### 서브네팅 및 IP 클래스 (Subnetting & IP Classes)
- **A Class**: 0~127. 대형 통신망 (Mạng rất lớn).
- **B Class**: 128~191. 중대형 통신망 (Mạng trung-lớn).
- **C Class**: 192~223. 소규모 통신망 (Mạng nhỏ).
- **D Class**: 224~239. 멀티캐스트 (Multicast).
- **서브네팅 (Subnetting)**: 서브넷 마스크를 이용해 네트워크 주소를 분할. (Dùng Subnet Mask để chia nhỏ mạng).

### 계층별 주요 프로토콜 (Major Protocols by Layer / Giao thức theo tầng)
- **응용 계층 (Application)**: FTP (파일 전송), SMTP (메일), TELNET (원격 접속), SNMP (네트워크 관리), DNS (도메인-IP 변환), HTTP (웹 문서).
- **전송 계층 (Transport)**: TCP (신뢰성), UDP (빠른 속도), RTCP (실시간 제어).
- **네트워크/인터넷 계층 (Network/Internet)**: IP (주소 지정, 비연결형), ICMP (오류 제어 메시지), IGMP (멀티캐스트 그룹 관리), ARP (IP -> MAC), RARP (MAC -> IP).
- **데이터 링크 계층 (Data Link)**: Ethernet, HDLC, X.25.
  - 💡 *Mẹo ghi nhớ*: ARP = "A"ddress Resolution (Tìm MAC từ IP). RARP = "R"everse (Ngược lại).

### 네트워크 장비 (Network Devices - Bổ sung)
- **게이트웨이 (Gateway)**: 다른 네트워크로부터 데이터를 주고받는 출입구 역할, 프로토콜 구조가 다른 네트워크 연결. (Cổng ra vào giữa các mạng có giao thức hoàn toàn khác nhau).
- **NIC (Network Interface Card)**: 랜카드, 컴퓨터를 네트워크에 연결. (Card mạng).

## 소프트웨어 공학 (Software Engineering)
### 167. 소프트웨어와 시스템 / 위기 (Software & System / Khủng hoảng phần mềm)
- **소프트웨어의 특징 (Đặc điểm phần mềm)**:
  - **비마모성 (No wear)**: 마모되거나 소멸되지 않음 (Không bị hao mòn vật lý).
  - **비가시성 (Invisibility)**: 코드 속에 숨어 있음 (Vô hình).
  - **복잡성, 비제조성, 비과학성** (Phức tạp, Không sản xuất công nghiệp, Phụ thuộc con người).
- **소프트웨어 위기 (Software Crisis)**: 하드웨어 발전 속도를 소프트웨어가 따라가지 못해 비용 증가, 유지보수 어려움 발생. (Khủng hoảng do nhu cầu phần mềm quá lớn nhưng chất lượng kém, chi phí bảo trì cao).

### 168. 소프트웨어 공학의 개념 (Concept of Software Engineering / Khái niệm kỹ nghệ phần mềm)
- **목적**: 소프트웨어의 위기 극복, 품질과 생산성 향상. (Khắc phục khủng hoảng, tăng chất lượng và năng suất).
- 가장 경제적인 방법으로 양질의 제품을 생산하는 것. (Sản xuất phần mềm tốt với chi phí tiết kiệm nhất).
  - 💡 *Mẹo ghi nhớ*: Kỹ nghệ phần mềm = Khoa học + Quản lý + Tiết kiệm tiền & thời gian.



# 과목 4. 소프트웨어 공학 (Phần 2)

## 169. 일반적인 소프트웨어 생명 주기 (General Software Life Cycle / Vòng đời phát triển phần mềm chung)
- **정의 단계 (Definition Phase / Giai đoạn định nghĩa)**: ‘무엇(What)’을 처리하는 소프트웨어를 개발할 것인지 정의하는 단계. 관리자와 사용자가 가장 많이 참여함.
  - **타당성 검토 단계 (Feasibility Study)**: 법적, 경제적, 기술적으로 실현 가능성이 있는지 조사.
  - **개발 계획 단계 (Development Planning)**: 자원과 비용을 측정.
  - **요구사항 분석 단계 (Requirements Analysis)**: 사용자 요구 문제를 상세하고 정확히 분석.
- **개발 단계 (Development Phase / Giai đoạn phát triển)**: ‘어떻게(How)’에 초점을 두고 실제적으로 소프트웨어를 개발하는 단계.
  - **설계 단계 (Design)**: 구조, 알고리즘, 자료구조 등을 작성 (에러가 가장 많이 발생).
  - **구현 단계 (Implementation)**: 설계된 문서를 기초로 코딩.
  - **테스트 단계 (Testing)**: 오류를 찾는 단계.
- **유지보수 단계 (Maintenance Phase / Giai đoạn bảo trì)**: ‘변경(Change)’에 초점을 두고 환경 변화에 적응 및 유지시키는 단계 (시간과 비용이 가장 많이 투입됨).

**Giải thích (Vietnamese):**
Vòng đời phần mềm (SDLC) gồm 3 giai đoạn chính: Định nghĩa (tìm hiểu xem cần làm "cái gì"), Phát triển (tiến hành xây dựng "như thế nào"), và Bảo trì (cập nhật, sửa lỗi sau khi bàn giao - "thay đổi"). Giai đoạn bảo trì luôn tốn nhiều thời gian và chi phí nhất.

**Ví dụ (Example):**
Xây dựng ứng dụng đặt đồ ăn:
- Định nghĩa: Xác định app cần chức năng gì, ngân sách bao nhiêu (What).
- Phát triển: Code app, thiết kế database, test tính năng (How).
- Bảo trì: Cập nhật app khi có iOS mới hoặc đổi thuật toán (Change).

**💡 Mẹo ghi nhớ (Mnemonics):**
**정개유** (Định - Phát - Bảo): **정**의 (Định nghĩa), **개**발 (Phát triển), **유**지보수 (Bảo trì). Nhớ câu "Định hướng - Phát triển - Bảo vệ".

---

## 170. 소프트웨어 생명 주기 모형 - 폭포수 모형 (Waterfall Model / Mô hình thác nước)
- 소프트웨어 공학에서 가장 오래되고 폭넓게 사용된 전통적/고전적 생명 주기 모형.
- 각 단계를 확실히 매듭짓고, 철저한 검토 및 승인 후 다음 단계로 진행하는 **선형 순차적 모형(Linear Sequential Model)**.
- 이전 단계로 되돌아갈 수 없음.
- 개발 순서: 타당성 검토 → 계획 → 요구 분석 → 설계 → 구현(코딩) → 시험(검사) → 유지보수
- **장점**: 성공 사례가 많음. 단계별 산출물이 명확하여 공정 기준점이 뚜렷함.
- **단점**: 새로운 요구사항 반영이 어려움. 초기에 모든 요구사항을 명확히 해야 함. 현실적으로 오류 없이 다음 단계로 넘어가기 힘듦.

**Giải thích (Vietnamese):**
Mô hình thác nước là mô hình lâu đời nhất. Giống như nước chảy từ trên cao xuống, không thể chảy ngược, bạn phải hoàn thành xong một giai đoạn mới được sang giai đoạn tiếp theo. Rất khó để quay lại sửa đổi yêu cầu.

**Ví dụ (Example):**
Giống như việc xây một ngôi nhà truyền thống. Bạn phải hoàn thành xong bản vẽ (thiết kế) rồi mới xây móng (code). Khi đã xây xong móng, nếu muốn đổi bản vẽ để thêm tầng hầm thì cực kỳ khó và tốn kém.

**💡 Mẹo ghi nhớ (Mnemonics):**
**폭포수는 거꾸로 흐르지 않는다** (Thác nước không chảy ngược): Yêu cầu phải chuẩn ngay từ đầu, khó thay đổi về sau (고전적, 선형 순차적 - Cổ điển, tuần tự tuyến tính).

---

## 171. 소프트웨어 생명 주기 모형 - 프로토타입 모형 (Prototype Model / Mô hình nguyên mẫu)
- 사용자 요구사항을 정확히 파악하기 위해 실제 개발될 소프트웨어의 **견본(시제품, Prototype)**을 만들어 최종 결과물을 예측하는 모형.
- 시제품은 사용자와 시스템 사이의 **인터페이스에 중점**을 둠.
- 개발 단계 안에서 유지보수가 이루어지며 별도의 유지보수 단계가 없어짐.
- 개발 순서: 요구 수집 → 빠른 설계 → 프로토타입 구축 → 고객 평가 → 프로토타입 조정 → 구현
- **장점**: 요구사항을 충실히 반영, 변경 용이. 미리 모형을 볼 수 있어 공동 참조 모델 제공.
- **단점**: 단기간 제작으로 비효율적 알고리즘 사용 가능성. 시제품을 완제품으로 오해하여 혼란 발생 가능.

**Giải thích (Vietnamese):**
Thay vì làm một mạch từ đầu đến cuối, mô hình nguyên mẫu tạo ra một bản "nháp" (prototype) nhanh chóng để khách hàng dùng thử và góp ý. Chủ yếu tập trung vào giao diện (UI/UX) để khách hàng hình dung được sản phẩm.

**Ví dụ (Example):**
Trước khi may một bộ vest thật (bằng vải đắt tiền), thợ may làm một bộ bằng vải nháp (prototype) cho khách mặc thử để xem form dáng đã chuẩn chưa, khách ưng ý rồi mới may vải thật.

**💡 Mẹo ghi nhớ (Mnemonics):**
**프**로토타입은 **미리보기(견본)**: Prototype = Bản dùng thử. Khách hàng xem trước rồi mới làm thật.

---

## 172. 소프트웨어 생명 주기 모형 - 나선형 모형 (Spiral Model / Mô hình xoắn ốc)
- 보헴(Boehm) 제안. 폭포수 모형과 프로토타입 모형의 장점에 **위험 분석(Risk Analysis)** 기능을 추가.
- 나선을 따라 돌 듯 점진적으로 완벽한 소프트웨어를 개발 (**점진적 모형**).
- 목적: 소프트웨어 개발 중 발생할 수 있는 **위험을 관리하고 최소화**.
- 개발 순서: 계획 및 정의(Planning) → **위험 분석(Risk Analysis)** → 공학적 개발(Engineering) → 고객 평가(Customer Evaluation)
- **장점**: 대규모 시스템에 적합 (현실적). 요구사항 추가/수정 용이. 유지보수 과정 불필요.
- **단점**: 위험성 평가에 크게 의존하여, 위험을 발견하지 못하면 문제 발생.

**Giải thích (Vietnamese):**
Mô hình xoắn ốc lặp đi lặp lại nhiều chu kỳ. Đặc trưng lớn nhất của nó là "Phân tích rủi ro" (Risk Analysis). Rất phù hợp cho các dự án quy mô lớn, phức tạp, ngân sách khổng lồ cần giảm thiểu rủi ro.

**Ví dụ (Example):**
Phát triển phần mềm cho tên lửa vũ trụ. Qua mỗi vòng xoắn ốc, team sẽ thêm tính năng và lập tức phân tích xem "có nguy cơ nổ tên lửa hay rò rỉ dữ liệu không?". Đảm bảo rủi ro ở mức 0 rồi mới xoắn tiếp.

**💡 Mẹo ghi nhớ (Mnemonics):**
**나위대** (나선형 - 위험분석 - 대규모): **나**선형 모형(Xoắn ốc) = **위**험 분석(Phân tích rủi ro) = **대**규모 프로젝트(Dự án lớn).
4 vòng lặp: **계위공고** (계획 - 위험 - 공학 - 고객).

---

## 173. 프로젝트 관리 (Project Management / Quản lý dự án)
- 주어진 기간 내 최소 비용으로 사용자를 만족시키는 시스템을 개발하기 위한 전반적인 활동.
- **효과적인 프로젝트 관리를 위한 3P (3대 요소)**:
  1. **사람 (People)**: 가장 기본이 되는 인적 자원.
  2. **문제 (Problem)**: 사용자 입장에서 문제를 분석하여 인식.
  3. **프로세스 (Process)**: 개발에 필요한 전체적인 작업 계획 및 구조 (Framework).
- **프로젝트 관리 대상**:
  - 계획 관리: 프로젝트 계획, 비용 산정, 일정 계획.
  - 품질 관리: 품질 통제, 품질 보증.
  - 위험 관리: 위험 식별, 위험 분석/평가.

**Giải thích (Vietnamese):**
Quản lý dự án là làm sao để làm ra phần mềm đúng hạn, rẻ nhất mà khách hàng vẫn hài lòng. Có 3 yếu tố cốt lõi (3P): Con người (ai làm?), Vấn đề (giải quyết cái gì?), và Quy trình (làm như thế nào?).

**Ví dụ (Example):**
Dự án game: People (lập trình viên, hoạ sĩ thiết kế), Problem (game bị giật lag, cần tối ưu), Process (Dùng Agile Scrum để chia sprint làm việc).

**💡 Mẹo ghi nhớ (Mnemonics):**
**3P**: **P**eople (Người) - **P**roblem (Vấn đề) - **P**rocess (Quy trình). Thiếu chữ P nào dự án cũng "Phá sản" (Phá).

---

## 174. 프로젝트 계획 수립 & 비용 결정 요소 (Project Planning & Cost Factors / Lập kế hoạch dự án & Các yếu tố chi phí)
- **소프트웨어 개발 영역 결정**: 프로젝트 계획 수립의 첫 번째 업무. 처리될 데이터, 기능, 성능, 제약조건, 인터페이스 등을 결정.
- **프로젝트 비용 결정 요소**:
  - **프로젝트 요소**: 제품의 복잡도, 시스템 크기, 요구 신뢰도.
  - **자원 요소**: 인적 자원, 하드웨어/소프트웨어 자원.
  - **생산성 요소**: 개발자 능력, 경험, 개발 기간.

**Giải thích (Vietnamese):**
Việc đầu tiên khi lập kế hoạch là xác định phạm vi (scope). Chi phí làm app đắt hay rẻ phụ thuộc vào 3 nhóm yếu tố: Bản thân dự án có phức tạp không? Tài nguyên cần thiết là gì? Lập trình viên có xịn không (năng suất)?

**💡 Mẹo ghi nhớ (Mnemonics):**
Chi phí phụ thuộc = **프자생** (프로젝트, 자원, 생산성).

---

## 175. 비용 산정 기법 - LOC 기법 (Lines Of Code / Kỹ thuật dòng mã lệnh)
- 소프트웨어 각 기능의 원시 코드 라인 수(LOC)의 비관치, 낙관치, 기대치를 측정하여 예측치를 구함.
- 측정이 용이하고 이해가 쉬워 가장 많이 사용됨.
- **산정 공식 (Dự đoán số dòng code)**: 
  예측치 = (낙관치 + 4 × 기대치 + 비관치) / 6
- **노력(인월, Person-Month)** = LOC / 1인당 월평균 생산 코드 라인 수 = 개발기간 × 투입인원.

**Giải thích (Vietnamese):**
Dự đoán chi phí dựa trên tổng số dòng code. Kỹ thuật này tính toán xem 1 người viết được bao nhiêu dòng code/tháng, từ đó suy ra cần bao nhiêu người và làm trong bao lâu (Person-Month). Công thức tính số dòng code kỳ vọng giống với ước lượng PERT.

**Ví dụ (Example):**
Làm web cần 6000 dòng code. Một Dev viết được 1000 dòng/tháng. Suy ra tốn 6 Người-Tháng (Person-Month). Nếu thuê 2 Dev thì tốn 3 tháng.

**💡 Mẹo ghi nhớ (Mnemonics):**
**LOC**: L = Line, O = Of, C = Code. **1 4 1 / 6**: 1 Lạc quan + 4 Kỳ vọng + 1 Bi quan chia 6.

---

## 176 - 177. 비용 산정 기법 - COCOMO 모형 (COnstructive COst MOdel / Kỹ thuật COCOMO)
- 보헴(Boehm)이 제안. 원시 프로그램 규모(LOC)에 의한 비용 산정 기법.
- 소프트웨어 개발 유형:
  - **조직형 (Organic Mode)**: 기관 내부 중·소규모, 5만 라인(50KDSI) 이하 (예: 사무/업무용).
  - **반분리형 (Semi-Detached Mode)**: 30만 라인(300KDSI) 이하 (예: 유틸리티, 트랜잭션 처리 시스템).
  - **내장형 (Embedded Mode)**: 초대형 규모, 30만 라인 이상 (예: 미사일 유도, 운영체제, 실시간 제어).
- **COCOMO 종류**:
  - **기본(Basic)**: 크기와 개발 유형만 이용.
  - **중간(Intermediate)**: 기본 + 제품/컴퓨터/개발자/프로젝트 특성 4가지 추가 반영.
  - **발전(Detailed)**: 개발 공정별로 노력을 산출하여 더 정확함.

**Giải thích (Vietnamese):**
COCOMO là mô hình tính phí dựa vào số dòng code nhưng phân loại theo quy mô dự án.
1. Organic: Nhỏ, nội bộ (<50k dòng).
2. Semi-detached: Vừa (<300k dòng).
3. Embedded: Rất lớn, nhúng vào phần cứng phức tạp như tên lửa (>300k dòng).

**Ví dụ (Example):**
- Organic: Viết tool điểm danh nhân sự cho cty.
- Embedded: Lập trình hệ thống điều khiển phanh ABS cho ô tô (cần cực kỳ phức tạp và chính xác).

**💡 Mẹo ghi nhớ (Mnemonics):**
**조반내** (Tổ - Bán - Nội): **조**직형(5만) - **반**분리형(30만) - **내**장형(30만 이상).

---

## 178. 프로젝트 일정 계획 (Project Scheduling / Lập lịch dự án)
- **브룩스(Brooks)의 법칙**: 프로젝트 진행 중에 새로운 인력을 투입할 경우 적응 기간과 부작용으로 일정이 더욱 지연됨. (Thêm người vào dự án đang trễ sẽ làm nó trễ hơn).
- **PERT (Program Evaluation and Review Technique)**:
  - 낙관치, 기대치, 비관치 3가지로 각 단계별 종료 시기를 결정.
  - 노드(작업)와 간선(예상시간)으로 구성.
- **CPM (Critical Path Method)**:
  - 노드(작업), 간선(전후 의존 관계).
  - 임계 경로(Critical Path)를 제공하여 프로젝트 최소 개발 기간을 결정함. 최장 경로가 임계 경로가 됨.

**Giải thích (Vietnamese):**
Khi lên lịch dự án, có quy luật Brooks nổi tiếng: "Thêm người vào dự án đang chậm tiến độ chỉ làm nó chậm hơn" (vì mất thời gian đào tạo người mới).
PERT và CPM là 2 biểu đồ mạng lưới giúp tìm ra đường găng (Critical Path) - chuỗi công việc dài nhất quyết định tổng thời gian dự án.

**💡 Mẹo ghi nhớ (Mnemonics):**
**Brooks**: "Chín người phụ nữ không thể sinh một đứa bé trong một tháng". Thêm người không có nghĩa là nhanh hơn!

---

## 179. 간트 차트 (Gantt Chart / Biểu đồ Gantt)
- 작업 일정을 **막대 도표(Bar Chart)**를 이용하여 표시하는 프로젝트 일정표. **시간선(Time-Line) 차트**라고도 함.
- 수평 막대 길이는 작업 기간을 나타냄.
- 중간 목표 미달성 이유와 예산 초과 등도 관리 가능. (단, 작업 간 의존성 파악은 CPM보다 약함).

**Giải thích (Vietnamese):**
Biểu đồ Gantt thể hiện các công việc bằng các thanh ngang (bar) chạy theo dòng thời gian. Rất trực quan để xem ai đang làm gì vào ngày nào, tiến độ ra sao.

---

## 180. 프로젝트 팀 구성 (Team Organization / Cấu trúc nhóm dự án)
- **분산형 팀 (민주주의식 팀 / Democratic Team)**:
  - 팀원 모두 의사 결정 참여. 장기 프로젝트에 적합. 이직률이 낮음.
  - 단점: 의사 결정 시간이 늦어지고 책임감이 분산될 수 있음. 의사소통 경로 수 = n(n-1)/2.
- **중앙 집중형 팀 (책임 프로그래머 팀 / Chief Programmer Team)**:
  - 한 관리자(책임 프로그래머)가 모든 의사 결정 권한과 책임을 가짐.
  - 의사 결정이 빠르고 소규모 문제에 적합.
  - 구성: 책임 프로그래머, 프로그래머, 프로그램 사서, 보조 프로그래머.
- **계층적 팀 (Hierarchical Team)**:
  - 분산형 + 중앙 집중형의 혼합. 초급 프로그래머들을 고급 프로그래머가 관리.

**Giải thích (Vietnamese):**
- Phân tán (Dân chủ): Mọi người cùng bàn bạc. Tốt cho dự án dài hạn nhưng họp hành mất thời gian.
- Tập trung (Chuyên tài): Một "siêu trình dịch" (Chief) quyết định hết, những người khác phụ việc. Nhanh nhưng phụ thuộc vào Chief.

---

## 181. 품질 표준 (Quality Standards / Tiêu chuẩn chất lượng phần mềm)
ISO/IEC 9126 등에서 말하는 소프트웨어 품질 특성:
1. **정확성 (Correctness)**: 사용자 요구 기능 충족.
2. **신뢰성 (Reliability)**: 오류 없이 정확/일관된 결과 수행.
3. **효율성 (Efficiency)**: 필요한 자원 소요 정도 (성능).
4. **무결성 (Integrity)**: 허용되지 않은 사용/변경 제어 (보안).
5. **사용용이성 (Usability)**: 배우고 사용하기 쉬운 정도.
6. **유지보수성 (Maintainability)**: 변경/오류 교정의 용이성.
7. **이식성 (Portability)**: 다양한 환경(하드웨어/OS)에서 운용 가능 정도.
8. **재사용성 (Reusability)**: 다른 목적으로 재사용 가능 여부.
9. **상호운용성 (Interoperability)**: 다른 소프트웨어와 정보 교환 능력.

**Giải thích (Vietnamese):**
Đây là các tiêu chí đánh giá phần mềm tốt. Ví dụ, phần mềm chạy nhanh là "Hiệu quả" (Efficiency), bảo mật chống hack là "Tính toàn vẹn" (Integrity), dễ cài trên cả Mac và Windows là "Tính di động/chuyển đổi" (Portability).

**💡 Mẹo ghi nhớ (Mnemonics):**
Chất lượng = **정신효무 사유이재상** (Đúng-Tin-Hiệu-Toàn Dùng-Bảo-Chuyển-Tái-Tương).

---

## 182. 품질 보증 / 정형 기술 검토 / 검토 회의 / 검열 (Quality Assurance & Reviews / Đảm bảo chất lượng & Đánh giá)
- **품질 보증 (QA)**: 소프트웨어가 요구사항과 일치하는지 확인하는 체계적인 작업.
- **정형 기술 검토 (FTR, Formal Technical Review)**: 소프트웨어 기술자들에 의해 수행되는 품질 보증 활동.
  - 지침: 제품 검토에만 집중, 의제 제한, 논쟁/반박 제한, 해결책(개선책) 논하지 않음, 참가자 수 제한 및 사전 준비.
- **검토 회의 (Walkthrough / Walkthrough)**:
  - 제품 개발자가 주최. 오류 조기 검출 목적 (해결책은 회의 후에). 사전 자료 배포.
- **검열 (Inspections / Inspection)**:
  - 검토 회의보다 더 공식적이고 발전된 형태. 다른 전문가가 코드/산출물을 꼼꼼히 심사하여 품질을 평가하고 개선.

**Giải thích (Vietnamese):**
- FTR (Đánh giá kỹ thuật chính thức): Là những cuộc họp để tìm lỗi phần mềm. **Lưu ý quan trọng**: Trong cuộc họp này CHỈ tìm lỗi, KHÔNG tranh cãi, KHÔNG bàn cách sửa lỗi (cách sửa sẽ bàn sau).
- Walkthrough: Tác giả tự trình bày code của mình cho team xem để tìm lỗi.
- Inspection: Người khác (thanh tra viên) sẽ soi xét code của bạn một cách rất nghiêm ngặt.

**💡 Mẹo ghi nhớ (Mnemonics):**
**FTR 원칙**: "문제만 찾고 해결책은 나중에!" (Chỉ tìm vấn đề, giải pháp tính sau!).

---

## 183. 위험 관리 (Risk Management / Quản lý rủi ro)
- 프로젝트 추진 과정에서 예상되는 돌발 상황을 미리 예상하고 대책을 수립하는 활동.
## 183. 위험 관리 절차 (Risk Management Procedure / Quy trình quản lý rủi ro) - Tiếp theo
- Yếu tố rủi ro tiêu biểu nhất là **사용자 요구 변경** (Sự thay đổi yêu cầu từ người dùng).
- **절차 (Quy trình)**:
  1. **위험 식별 (Nhận diện rủi ro)**: Nắm bắt các rủi ro có thể đoán trước.
  2. **위험 분석 및 평가 (Phân tích & Đánh giá)**: Lập bảng rủi ro (Risk Table) để phân tích xác suất xảy ra và sức ảnh hưởng (Risk Estimation).
  3. **위험 관리 계획 (Lập kế hoạch)**: Chuẩn bị đối sách phòng ngừa và tài liệu hóa.
     - *위험 회피 (Risk Avoidance)*: Chiến lược tốt nhất (Dự đoán và né tránh).
  4. **위험 감시 및 조치 (Giám sát & Xử lý)**:
     - *위험 감시 (Risk Monitoring)*: Liên tục theo dõi các dấu hiệu.
     - *비상 계획 (Contingency Plan)*: Kế hoạch dự phòng khi chiến lược né tránh thất bại.

**Giải thích (Vietnamese):**
Khách hàng liên tục thay đổi yêu cầu là rủi ro lớn nhất khi làm phần mềm. Để quản lý, trước tiên ta phải nhận diện được nó, rồi lập bảng đánh giá xem nếu xảy ra thì hậu quả là gì. Cách tốt nhất là "Né tránh" (Ví dụ: Chốt hợp đồng rõ ràng từ đầu để khách không đổi yêu cầu). Nếu vẫn xảy ra thì phải có kế hoạch dự phòng (Contingency Plan).

**💡 Mẹo ghi nhớ (Mnemonics):**
**식분계감** (Thức - Phân - Kế - Giám): 식별(Nhận diện) -> 분석(Phân tích) -> 계획(Lập kế hoạch) -> 감시(Giám sát).

---

## 184. 형상 관리 (SCM - Software Configuration Management / Quản lý cấu hình phần mềm)
- 소프트웨어 개발 과정에서 생산물을 확인하고 통제, **변경 상태를 기록하고 보관**하는 일련의 작업.
- 변경의 원인을 제어하고 적절히 변경되고 있는지 담당자에게 통보.
- 소프트웨어 생명 주기 **전 단계에 적용**되며 (유지보수 단계 포함), 방해 요인을 최소화하는 것이 목적.
- 형상 항목: 개발 문서, 소스 코드, 자료 구조, 유지보수 변경 사항 등.

**Giải thích (Vietnamese):**
SCM (Quản lý cấu hình) là việc theo dõi và kiểm soát mọi sự thay đổi của phần mềm (như dùng Git/GitHub). Ai đã sửa dòng code này? Sửa khi nào? Sửa tài liệu nào? Nó được áp dụng trong suốt vòng đời dự án để tránh xung đột và dễ dàng khôi phục khi có lỗi.

**Ví dụ (Example):**
Khi dùng Git để quản lý source code. Bạn commit một tính năng mới (theo dõi sự thay đổi), nếu code bị lỗi, bạn có thể dễ dàng revert (quay lại) phiên bản cũ. SCM chính là hệ thống quản lý các phiên bản này.

**💡 Mẹo ghi nhớ (Mnemonics):**
**형상관리 = 변경 통제 (Git)**: Nhắc đến 형상관리 là nhớ ngay đến việc theo dõi sự thay đổi (Change Control) trong suốt vòng đời.

---

## 185. 요구사항 분석 (Requirements Analysis / Phân tích yêu cầu)
- 소프트웨어 개발의 실질적인 첫 단계. 사용자의 요구를 이해하고 **문서화(명세화)**함.
- 분석 결과는 '설계 단계'의 기본 자료가 됨.
- **작업 과정**: 문제 인식 (면담, 설문조사) → 평가와 종합 (해결책 종합) → 모델 제작 (도식화, 이해하기 쉽게) → 문서화와 검토 (명세서 작성).
- **요구사항 분석가의 자질**: 소프트웨어 개발 경험, 사용자 환경 이해, 하드웨어/소프트웨어 기술 지식, **고객 관점(상대의 관점)**에서 문제 파악 능력.

**Giải thích (Vietnamese):**
Phân tích yêu cầu là bước đầu tiên để biết khách hàng thực sự muốn gì. Nhà phân tích phải có kinh nghiệm lập trình, hiểu biết hệ thống và đặc biệt là phải có "góc nhìn của khách hàng" để giải quyết đúng nỗi đau của họ.

---

## 186. 자료 흐름도 (DFD - Data Flow Diagram / Biểu đồ luồng dữ liệu)
- 자료의 흐름과 변환 과정을 도형 중심으로 기술. **버블(Bubble) 차트**라고도 함.
- 시스템의 범위를 표현하는 단계를 **배경도 (Level 0)**라고 함.
- **기호 (Ký hiệu)**:
  - **프로세스 (Process)**: `원(O)` - 자료를 변환시키는 처리 기능 (버블).
  - **자료 흐름 (Flow)**: `화살표(→)` - 자료의 이동.
  - **자료 저장소 (Data Store)**: `평행선(=)` - 파일, 데이터베이스.
  - **단말 (Terminator)**: `사각형(□)` - 정보의 생산자와 소비자 (외부 개체).

**Giải thích (Vietnamese):**
DFD vẽ ra cách dữ liệu chạy trong hệ thống. Ví dụ khi bạn mua hàng: Khách hàng (Hình vuông) -> Gửi yêu cầu mua (Mũi tên) -> Xử lý thanh toán (Hình tròn) -> Lưu vào Database (Đường song song). DFD còn gọi là Bubble Chart vì các Process được vẽ bằng hình tròn giống như bong bóng.

**💡 Mẹo ghi nhớ (Mnemonics):**
**프흐저단** (Process, Flow, Store, Terminator) / **원화평사** (Tròn, Mũi tên, Bình hành/Song song, Vuông).

---

## 187. 자료 사전 (DD - Data Dictionary / Từ điển dữ liệu)
- DFD에 있는 자료를 더 자세히 정의. 데이터를 설명하는 데이터이므로 **메타 데이터(Meta Data)**라고도 함.
- **표기 기호**:
  - `=` : 정의 (~로 구성되어 있다 / is composed of)
  + `+` : 연결 (그리고 / and)
  - `()` : 생략 가능 (Optional)
  - `[ | ]` : 선택 (또는 / or)
  - `{}` : 반복 (Iteration of)
  - `**` : 주석 (Comment)

**Giải thích (Vietnamese):**
Từ điển dữ liệu giải thích chi tiết các thành phần trong DFD. Ví dụ: `Hồ sơ = Tên + [ Nam | Nữ ] + ( Số điện thoại )`. Nghĩa là Hồ sơ gồm Tên, VÀ Giới tính (chọn Nam HOẶC Nữ), Số điện thoại (có ngoặc đơn nghĩa là có thể điền hoặc không).

**💡 Mẹo ghi nhớ (Mnemonics):**
- `()` Giống hình cái miệng ngậm lại -> Có thể không nói (Optional).
- `[ | ]` Dấu vách ngăn -> Phải chọn một trong hai.
- `{}` Dấu ngoặc nhọn móc nối tiếp -> Lặp đi lặp lại.

---

## 188. HIPO (Hierarchy plus Input-Process-Output)
- 입력, 처리, 출력의 기능을 나타내는 하향식 소프트웨어 개발 문서화 도구.
- **종류**:
  - **가시적 도표 (Visual Table of Contents)**: 전체적인 기능과 흐름을 보여주는 계층(Tree) 구조도.
  - **총체적 도표 (Overview Diagram)**: 입력, 처리, 출력에 대한 전반적 정보 제공.
  - **세부적 도표 (Detail Diagram)**: 기능을 상세히 기술.

**Giải thích (Vietnamese):**
HIPO là tài liệu thiết kế chia hệ thống theo cấu trúc từ trên xuống (Top-down). Gồm 3 loại biểu đồ: Tổng quan phân cấp (Tree), Biểu đồ chung (vẽ Input-Process-Output cơ bản), và Biểu đồ chi tiết.

**💡 Mẹo ghi nhớ (Mnemonics):**
**가총세** (Gia - Tổng - Tế): 가시적 (Trực quan/Phân cấp), 총체적 (Tổng quát), 세부적 (Chi tiết).

---

## 189. 구조적 설계의 주요 기본 원리 (Principles of Structured Design / Nguyên lý thiết kế có cấu trúc)
- **모듈화 (Modularity)**: 시스템을 모듈 단위로 나눔.
- **추상화 (Abstraction)**: 포괄적 개념 먼저 설계 후 세분화 (기능, 제어, 자료 추상화).
- **정보 은닉 (Information Hiding)**: 모듈 내부의 세부 정보를 감추어 다른 모듈이 변경하지 못하게 함 (유지보수 용이).
- **프로그램 구조 (Program Structure)**: 제어 계층 구조 (트리 형태).
  - 공유도(Fan-In): 나를 호출하는 상위 모듈 수.
  - 제어도(Fan-Out): 내가 호출하는 하위 모듈 수.

**Giải thích (Vietnamese):**
Khi thiết kế phần mềm, ta chia nhỏ thành các hàm/chức năng (Modularity). Dùng "Che giấu thông tin" (Information Hiding) như tính đóng gói (Encapsulation) trong OOP để các hàm không can thiệp sai vào dữ liệu của nhau.
- Fan-In (Đi vào): Có bao nhiêu hàm gọi đến mình. Fan-In cao là tốt vì tính tái sử dụng cao.
- Fan-Out (Đi ra): Mình gọi bao nhiêu hàm khác. Fan-Out cao nghĩa là hàm này quá phức tạp.

**💡 Mẹo ghi nhớ (Mnemonics):**
**모추정** (Mô - Trừu - Thông): **모**듈화(Modularity), **추**상화(Abstraction), **정**보 은닉(Information Hiding).

---

## 190. 바람직한 설계의 특징 (Good Design Characteristics / Đặc điểm của thiết kế tốt)
- 적당한 모듈 크기를 유지.
- **결합도(Coupling)는 약하게, 응집도(Cohesion)는 강하게 설계한다**.

**Giải thích (Vietnamese):**
Một thiết kế phần mềm chuẩn mực phải đảm bảo: "Mối liên kết giữa các module càng lỏng lẻo càng tốt (Low Coupling), nhưng sự gắn kết nhiệm vụ bên trong một module phải càng chặt chẽ càng tốt (High Cohesion)".

---

## 191. 결합도 (Coupling / Mức độ phụ thuộc)
- 모듈 간에 상호 의존하는 정도. 약할수록 독립성이 높고 품질이 좋음.
- **결합도가 약한 것부터 강한 순서 (Tốt -> Xấu)**:
  1. **자료 (Data)**: 파라미터로 단순 데이터(값)만 전달 (가장 좋음).
  2. **스탬프 (Stamp)**: 배열이나 레코드 등 자료 구조를 전달.
  3. **제어 (Control)**: 제어 신호(Flag)를 전달하여 상대 모듈의 흐름을 제어.
  4. **외부 (External)**: 외부에서 선언된 데이터를 참조.
  5. **공통 (Common)**: 전역 변수(공통 데이터 영역)를 여러 모듈이 사용.
  6. **내용 (Content)**: 다른 모듈의 내부 기능이나 변수를 직접 참조/수정 (가장 나쁨).

**Giải thích (Vietnamese):**
Coupling đánh giá mức độ "dính líu" giữa 2 module. Càng dính líu nhiều, khi sửa module này sẽ làm hỏng module kia.
Tốt nhất là Data (chỉ truyền tham trị như `int a`). Tệ nhất là Content (module A nhảy thẳng vào code của module B để sửa biến).

**💡 Mẹo ghi nhớ (Mnemonics):**
**자스제 외공내** (Tự - Tem - Chế - Ngoại - Công - Nội): 자료 (Data) -> 스탬프 (Stamp) -> 제어 (Control) -> 외부 (External) -> 공통 (Common) -> 내용 (Content). Từ Tốt đến Xấu.

---

## 192. 응집도 (Cohesion / Mức độ gắn kết)
- 모듈 안의 요소들이 서로 관련되어 있는 정도. 강할수록 독립성이 높고 품질이 좋음.
- **응집도가 약한 것부터 강한 순서 (Xấu -> Tốt)**:
  1. **우연적 (Coincidental)**: 아무 관련 없는 요소들이 우연히 모임 (가장 나쁨).
  2. **논리적 (Logical)**: 논리적으로 유사한 성격의 작업들을 모음.
  3. **시간적 (Temporal)**: 특정 시간에 같이 처리되는 기능들을 모음 (예: 초기화).
  4. **절차적 (Procedural)**: 기능들이 순차적으로 수행됨.
  5. **교환/통신적 (Communication)**: 동일한 입력/출력 데이터를 사용.
  6. **순차적 (Sequential)**: 앞 활동의 출력 데이터를 다음 활동의 입력 데이터로 사용.
  7. **기능적 (Functional)**: 내부 모든 요소가 단일 목적(기능)만을 위해 존재 (가장 좋음).

**Giải thích (Vietnamese):**
Cohesion đo lường sự tập trung của một module. Nếu một hàm vừa làm toán cộng, vừa in hóa đơn, vừa gửi email -> Quá nhiều việc không liên quan (Xấu). Hàm chỉ làm đúng một việc là "Tính tổng" -> Tuyệt vời (Functional).

**💡 Mẹo ghi nhớ (Mnemonics):**
**우논시절 교순기** (U - Luận - Thời - Tiết - Giao - Tuần - Kỹ): 우연 (Coincidental) -> 논리 (Logical) -> 시간 (Temporal) -> 절차 (Procedural) -> 교환 (Communication) -> 순차 (Sequential) -> 기능 (Functional). Từ Xấu đến Tốt.

---

## 193 - 194. 효과적인 모듈화 설계 방안 & N-S 차트 (Effective Modular Design & Nassi-Schneiderman Chart)
- **모듈화 방안**: 결합도를 줄이고 응집도를 높임 (Low Coupling, High Cohesion). 모듈 크기는 이해하기 쉽게 분해. 하나의 입구와 하나의 출구를 가짐.
- **N-S 차트**: 논리 기술에 중점을 둔 도형 (박스 다이어그램).
  - 순차, 선택, 반복 구조를 시각적으로 표현.
  - **GOTO나 화살표를 사용하지 않음**.
  - 읽기는 쉽지만 작성하기 어려움.

**Giải thích (Vietnamese):**
Biểu đồ N-S (Nassi-Schneiderman) là loại biểu đồ khối chữ nhật, không dùng mũi tên, không dùng GOTO. Cấu trúc lồng nhau rất dễ đọc logic nhưng vẽ ra thì khó.

---

## 195 - 197. 구현 및 구조적 프로그래밍, 제어 흐름도 (Implementation & Structured Programming)
- **구현(코딩)**: 설계 명세서를 컴퓨터가 알 수 있는 코드로 변환.
- **구조적 프로그래밍**: 순차(Sequence), 선택(Selection), 반복(Iteration)의 3가지 제어 구조만 사용하여 코딩 (Dijkstra 제안). 신뢰성 향상.
- **순환 복잡도 (Cyclomatic Complexity)**: 프로그램의 논리적 복잡도 척도.
  - V(G) = E - N + 2 (E: 화살표 수, N: 노드 수). 또는 닫힌 영역의 수 + 1.

**Giải thích (Vietnamese):**
Lập trình có cấu trúc chỉ dùng 3 luồng: Chạy tuần tự từ trên xuống (Sequence), Lệnh rẽ nhánh If/Else (Selection), và Vòng lặp For/While (Iteration). Độ phức tạp McCabe tính xem hàm có bao nhiêu đường đi (nhánh) độc lập.

**Ví dụ (Example):**
Nếu biểu đồ luồng có 5 Node (N=5) và 6 Cạnh/Mũi tên (E=6).
Độ phức tạp Cyclomatic V(G) = 6 - 5 + 2 = 3. Số 3 nghĩa là hàm này cần ít nhất 3 test case để phủ toàn bộ các đường đi.

---

## 196. 화이트 박스 테스트 (White Box Test / Kiểm thử Hộp trắng)
- 모듈의 **원시 코드(Source Code)를 오픈시킨 상태**에서 논리적인 모든 경로를 검사.
- 내부 구조, 제어 흐름, 논리 흐름(루프)을 직접 관찰하며 테스트.
- 조건의 참/거짓 경로를 적어도 한 번 이상 실행.
- 테스트 과정 **초기**에 적용됨.
- 종류: 기초 경로 검사 (Basic Path Testing), 조건 검사, 루프 검사, 데이터 흐름 검사.

**Giải thích (Vietnamese):**
Kiểm thử hộp trắng là bạn (thường là Dev) nhìn thấy toàn bộ source code và viết test case để đảm bảo mọi dòng code (if, else, vòng lặp) đều được chạy qua ít nhất 1 lần.

**💡 Mẹo ghi nhớ (Mnemonics):**
Hộp trắng trong suốt -> Nhìn thấu được code bên trong. Trọng tâm là "Logic đường đi" (경로).

---

## 198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)
- **기능 검사**라고도 함. 내부 코드를 보지 않고, 소프트웨어의 인터페이스(입·출력)에서 기능이 완전히 작동하는지 입증.
- 테스트 과정 **후반부**에 적용됨.
- 종류:
  - **동치 분할 검사 (Equivalence Partitioning)**: 타당한 입력과 타당하지 않은 입력 자료의 갯수를 균등하게 나눠 테스트. (Ví dụ: Yêu cầu nhập từ 1-100. Test case: 50 (hợp lệ), 150 (không hợp lệ)).
  - **경계값 분석 (Boundary Value Analysis)**: 경계값에서 오류가 발생할 확률이 높음을 이용. (Ví dụ: Test case: 0, 1, 100, 101).
  - **원인-효과 그래프 (Cause-Effect Graphing)**: 입력(원인)과 출력(효과)의 관계 분석.
## 199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)
- **단위 검사 (Unit Testing)**: 코딩 후 최소 단위인 '모듈' 초점 검사 (화이트 박스 기법).
- **하향식 통합 검사 (Top-Down Integration)**: 상위 모듈 -> 하위 모듈 방향. 임시 시험용 모듈인 **스터브(Stub)** 필요.
- **상향식 통합 검사 (Bottom-Up Integration)**: 하위 모듈 -> 상위 모듈 방향. 제어 모듈과 종속 모듈 그룹인 **클러스터(Cluster)**와 드라이버(Driver) 필요. (Stub 불필요).
- **검증(확인) 검사 (Validation Testing)**: 요구사항 충족 여부 확인 (블랙 박스 기법).
  - **알파 검사 (Alpha Test)**: **개발자 환경(장소)**에서 사용자가 테스트 (통제된 환경).
  - **베타 검사 (Beta Test)**: **실제 사용자 환경**에서 여러 사용자가 테스트 (개발자 통제 없음).
- **시스템 검사 (System Test)**: 전체 시스템(하드웨어 포함)에서 완벽히 수행되는지 검사. (복구/보안/강도/성능 검사).

**Giải thích (Vietnamese):**
- Kiểm thử tích hợp từ trên xuống (Top-down) cần làm các module giả (Stub) để thay thế cho module con chưa code xong. Từ dưới lên (Bottom-up) cần nhóm (Cluster/Driver) để gọi module con.
- Alpha Test: Bạn mời khách hàng đến công ty bạn ngồi test app trước mặt bạn.
- Beta Test: Bạn tung app lên store cho người dùng tải về dùng thử và báo lỗi (bạn không ngồi cạnh họ).

**💡 Mẹo ghi nhớ (Mnemonics):**
**하스 상드** (Hạ - Stub, Thượng - Driver): **하**향식 = **스**터브(Stub). **상**향식 = 드라이버(Driver)/클러스터(Cluster).

---

## 200. 유지보수 (Maintenance / Bảo trì phần mềm)
- 개발 중 가장 많은 노력과 비용이 투입됨.
- **유형 (Phân loại)**:
  1. **수정(Corrective) 보수 (하자 보수)**: 검사 단계에서 못 찾은 '오류(버그) 수정'.
  2. **적응(Adaptive) 보수 (환경 적응)**: OS 변경, 하드웨어 변경 등 '환경 변화에 적응'하기 위한 수정.
  3. **완전화(Perfective) 보수 (기능 개선)**: 새로운 기능 추가, 성능 개선 (유지보수 중 가장 큰 비용 차지).
  4. **예방(Preventive) 보수**: 장래의 오류 발생에 대비하여 미리 예방.

**Giải thích (Vietnamese):**
- Corrective (Sửa lỗi): App bị crash, bạn phải vá lỗi.
- Adaptive (Thích ứng): Apple ra iOS mới, bạn update app để không bị lỗi màn hình tai thỏ.
- Perfective (Hoàn thiện): Thêm tính năng "Chat" vào app, cải tiến tốc độ tải (Chiếm nhiều ngân sách nhất).
- Preventive (Phòng ngừa): Refactor code để sau này dễ nâng cấp.

**💡 Mẹo ghi nhớ (Mnemonics):**
**수적완예** (Tu - Thích - Hoàn - Dự): **수**정, **적**응, **완**전, **예**방.

---

## 201. 외계인 코드 (Alien Code / Mã ngoài hành tinh)
- 아주 오래 전에 개발되어(보통 15년 전) 문서화가 제대로 되어 있지 않아 유지보수가 매우 어려운 프로그램.
- 해결책: 문서화(Documentation)를 철저히 해야 함.

**Giải thích (Vietnamese):**
Đó là những đoạn code từ "đời tống", người viết code đã nghỉ việc, code không có comment hay tài liệu giải thích. Người mới đọc vào không hiểu gì như ngôn ngữ ngoài hành tinh, không dám sửa vì sợ sập hệ thống.

---

## 202 - 203. 객체지향 기법 & 주요 원칙 (Object-Oriented Techniques & Principles / OOP)
- **개념**: 현실 세계의 개체(Entity)를 기계 부품(Object)처럼 만들어 조립식으로 소프트웨어 개발. 재사용/확장 용이.
- **구성 요소**:
  - **데이터 (Data/Attribute)**: 객체가 가진 정보 (속성, 상태).
  - **연산/메소드 (Method/Operation)**: 데이터를 처리하는 알고리즘/함수.
  - **클래스 (Class)**: 공통 속성/연산을 갖는 객체들의 집합 (틀, Type). 객체를 '인스턴스(Instance)'라고 함.
  - **메시지 (Message)**: 객체 간 상호작용 수단 (명령).
- **주요 기본 원칙**:
  1. **캡슐화 (Encapsulation)**: 데이터와 함수를 하나로 묶음. 재사용 용이, 결합도 낮아짐.
  2. **정보 은닉 (Information Hiding)**: 내부 정보를 숨기고 연산만을 통해 접근 허용 (Side Effect 최소화).
  3. **상속성 (Inheritance)**: 상위 클래스의 속성/연산을 하위 클래스가 물려받음. (다중 상속도 있음).
  4. **추상화 (Abstraction)**: 불필요한 부분 생략, 중요한 부분만 모델화.
  5. **다형성 (Polymorphism)**: 동일한 메시지(메소드명)에 대해 객체마다 다른 응답(기능)을 함.

**Giải thích (Vietnamese):**
OOP (Lập trình hướng đối tượng) giống như trò chơi xếp hình Lego.
- Class: Bản vẽ thiết kế chiếc xe.
- Object (Instance): Chiếc xe thật được lắp ráp.
- Tính đóng gói (Encapsulation): Gói gọn các bộ phận động cơ vào trong vỏ xe.
- Tính đa hình (Polymorphism): Cùng là lệnh "Kêu", con chó kêu "Gâu", con mèo kêu "Meo".

**💡 Mẹo ghi nhớ (Mnemonics):**
**캡정상추다** (Đóng - Ẩn - Kế - Trừu - Đa): 캡슐화, 정보 은닉, 상속성, 추상화, 다형성.

---

## 204 - 205. 객체지향 분석 및 럼바우 기법 (OO Analysis & Rumbaugh Method)
- **객체지향 분석**: 사용자의 요구사항을 분석하여 클래스(객체), 속성, 연산, 관계 등을 정의하는 작업.
- **분석 방법론**:
  - **Booch**: 미시적/거시적 개발 프로세스 모두 사용.
  - **Jacobson**: Use Case 강조.
  - **Coad/Yourdon**: E-R 다이어그램 사용.
  - **Wirfs-Brock**: 분석과 설계 간 구분 없음.
- **🌟 럼바우(Rumbaugh)의 분석 기법 (객체 모델링 기법, OMT)**:
  - 분석 순서: **객동기** (객체 -> 동적 -> 기능).
  1. **객체 모델링 (Object Modeling)**: 객체 식별, 구조 및 관계 규정 (객체 다이어그램 / 정보 모델링).
  2. **동적 모델링 (Dynamic Modeling)**: 시간 흐름에 따른 상태 변화, 제어 흐름 표현 (상태도).
  3. **기능 모델링 (Functional Modeling)**: 데이터 흐름을 중심으로 처리 과정 표현 (자료 흐름도, DFD).

**Giải thích (Vietnamese):**
Phương pháp phân tích của Rumbaugh là kinh điển nhất trong thi. Gồm 3 bước:
1. Object (Khách hàng, Tài khoản).
2. Dynamic (Tài khoản từ Đang mở -> Bị khóa khi nhập sai pass 3 lần).
3. Functional (Dữ liệu tiền chạy từ hệ thống ra ATM như thế nào).

**💡 Mẹo ghi nhớ (Mnemonics):**
**객동기** (Khách - Động - Cơ): **객**체(Object) -> **동**적(Dynamic) -> **기**능(Functional).

---

## 206 - 207. 객체지향 설계 및 프로그래밍 (OO Design & Programming)
- **설계 (OOD)**: 분석 모델을 설계 모델로 변환 (추상화, 정보 은닉, 상속 등 활용). 가장 중요한 것은 **모듈화**. 설계 명세서를 작성.
- **프로그래밍 (OOP)**: 현실 세계에 가까운 방식으로 프로그래밍. 유지보수/재사용성 향상.
  - 객체지향성 언어: Simula (최초), Smalltalk, C++, Java 등.

---

## 208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)
- 이미 개발된 소프트웨어 전체/일부를 다른 개발에 사용하는 것. 개발 시간/비용 단축, 품질 향상.
- **컴포넌트 (Component)**: 객체들의 모임으로 대규모 재사용 단위.
- 모듈 크기가 작고 일반적일수록 재사용률이 높음.
- 문제점: 표준화 부족, 공통 요소 발견의 어려움, 새 코드에 통합하기 어려움.

**Giải thích (Vietnamese):**
Đừng "phát minh lại cái bánh xe". Lấy những module, function đã chạy tốt ở dự án trước để ghép vào dự án này (ví dụ: dùng lại module đăng nhập bằng Google).

---

## 209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)
- 기존 시스템을 수정 보완하거나 기능을 추가하여 성능을 향상 (예방 유지보수).
- 목적: 유지보수 비용 절감, 품질 향상, 소프트웨어 위기 해결.
- **주요 활동**:
  - **분석 (Analysis)**: 기존 명세서 확인.
  - **재구성/개조 (Restructuring)**: 기능은 그대로 두고 코드 구조만 향상 (Refactoring).
  - **역공학 (Reverse Engineering)**: 기존 코드를 분석하여 설계/명세서(문서)를 다시 뽑아내는 것 (복구). 가장 오래된 형태는 재문서화.
  - **이식 (Migration)**: 다른 OS나 하드웨어 환경으로 변환.

**Giải thích (Vietnamese):**
Reengineering là đập đi xây lại hoặc tu sửa lại nhà cũ cho hiện đại hơn.
- Restructuring: Cấu trúc lại bên trong nhà (mở rộng bếp, đập vách ngăn) nhưng nhìn bề ngoài vẫn là cái nhà đó.
- Reverse Engineering: Có một cái nhà cũ xây từ thời xưa không có bản vẽ. Nhìn vào cái nhà thực tế để vẽ lại bản vẽ kỹ thuật (Dịch ngược code thành tài liệu thiết kế).

**💡 Mẹo ghi nhớ (Mnemonics):**
**분재역이** (Phân - Tái - Nghịch - Di): 분석, 재구성, 역공학, 이식.

---

## 210. CASE (Computer-Aided Software Engineering)
- 소프트웨어 생명주기 전체 또는 일부를 **자동화하는 소프트웨어 도구**.
- 개발 기간 단축, 비용 절감, 품질 및 생산성 향상. 개발 주기의 표준화.
- **CASE 정보 저장소 (Repository)**: 개발 중 모아진 정보 보관 (현재의 Database 역할). 일관성 유지.
- **분류**:
  - 상위 (Upper) CASE: 요구 분석, 설계 단계 지원.
  - 하위 (Lower) CASE: 코드 작성, 테스트 지원.
  - 통합 (Integrated) CASE: 전체 과정 지원.

**Giải thích (Vietnamese):**
CASE là các phần mềm hỗ trợ kỹ sư làm phần mềm. Giống như Excel giúp kế toán tính toán nhanh hơn, CASE (như StarUML, Jira, Eclipse) giúp lập trình viên vẽ biểu đồ, quản lý task, sinh code tự động.

---

# 4과목 프로그래밍 언어 활용 (Phần 4: Ứng dụng ngôn ngữ lập trình)

## 070. 서버개발 프레임워크 (Server Development Framework)
- **모듈화 (Modularity)**: 캡슐화로 영향 최소화, 유지보수 용이.
- **재사용성 (Reusability)**: 반복 모듈 제공으로 생산성/품질 향상.
- **확장성 (Extensibility)**: 다형성 통한 인터페이스 확장.
- **제어 반전 (Inversion of Control, IoC)**: 프레임워크가 흐름을 제어하고 사용자(외부) 코드를 호출.

**Giải thích (Vietnamese):**
Framework (như Spring, Django) là một bộ khung có sẵn. Tính năng đặc biệt nhất của Framework là IoC (Đảo ngược quyền điều khiển): Thay vì bạn tự gọi thư viện (Library), thì Framework sẽ là người gọi code của bạn!

---

## 071. 보안 취약성 식별 (Security Vulnerability Identification / Lỗ hổng bảo mật)
- **버퍼 오버플로 (Buffer Overflow)**: 메모리를 다루는 데 오류 발생시켜 덮어쓰는 공격.
- **허상 포인터 (Dangling Pointer)**: 삭제된 객체를 가리키고 있는 포인터 (메모리 보안 위반).
- **FTP 바운스 공격**: FTP 프로토콜 구조 허점 이용.
- **SQL 삽입 (SQL Injection)**: 웹 입력창에 SQL 문법 삽입해 DB 데이터 유출/조작.
- **디렉토리 접근 공격 (Directory Traversal)**: 웹 루트 외 디렉토리 접근 (`../` 문자 사용).
- **포맷 스트링 버그**: `printf()` 등에서 검사되지 않은 입력 통한 공격.
- **코드 인젝션 (Code Injection)**: 유효하지 않은 실행 코드 주입.

**Giải thích (Vietnamese):**
- SQL Injection: Kẻ gian gõ `1' OR '1'='1` vào ô đăng nhập để lừa hệ thống cho phép truy cập.
- Buffer Overflow: Kẻ gian cố tình nhập 100 ký tự vào ô chỉ cho phép 10 ký tự, làm tràn bộ nhớ và sập chương trình.

---

## 072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)
- **데이터 타입 (Data Types)**:
  - 정수형 (Integer): `int`, `short`, `long` (Ví dụ: 1, -1).
  - 부동 소수형 (Float Point): `float`, `double` (실수, 소수점) (Ví dụ: 3.14).
  - 문자형 (Character): `char` ('A').
  - 문자열 (String): `char` 배열, `string` ("ABC").
  - 논리형 (Boolean): 참/거짓 (True/False).
- **변수 작성 규칙 (Variable Naming Rules)**:
  - 영문자, 숫자, 밑줄(`_`) 사용 가능.
  - **숫자로 시작 불가**, 중간 공백 특수문자 불가, 예약어(`if`, `for` 등) 사용 불가.
- **연산자 (Operators)**:
  - 산술 (Arithmetic): `+`, `-`, `*`, `/` (몫), `%` (나머지).
  - 증감 (Increment/Decrement): `++` (1 증가), `--` (1 감소).
    - 전치 (`++A`): 연산 전 증가.
    - 후치 (`A++`): 연산 후 증가.
  - 관계 (Relational): `>`, `<`, `==` (같다), `!=` (다르다).
  - 논리 (Logical): `&&` (AND), `||` (OR), `!` (NOT).
  - 삼항 (Ternary): `(조건) ? (참) : (거짓);`
## 074. 데이터 입출력 (Data Input/Output)
- **표준 입력 함수 (C언어)**: `scanf("서식 문자열", &변수명);` (변수의 주소 `&`를 붙임).
- **표준 출력 함수 (C언어)**: `printf("서식 문자열", 변수);`
- **서식 문자열 유형 (Format Strings)**:
  - `%d`: 정수형 10진수 (Decimal)
  - `%f`: 실수형 (Float)
  - `%c`: 문자형 1개 (Character)
  - `%s`: 문자열 (String)
- **이스케이프 문자**: `\n` (줄바꿈), `\t` (탭), `\b` (백스페이스).
- **JAVA 입출력**: `System.out.println()` (출력 후 자동 개행), `System.out.print()` (개행 없음).
- **Python 입출력**: `print(문자열, end='')` (끝에 개행 대신 다른 문자 삽입).

**Giải thích (Vietnamese):**
Khi lập trình bằng C, bạn dùng `scanf` để nhận dữ liệu người dùng nhập (nhớ có dấu `&` trước tên biến) và `printf` để in ra màn hình. Dấu `%d` dùng cho số nguyên, `%f` cho số thập phân. Java dùng `System.out.println()`. Python thì ngắn gọn hơn chỉ cần `print()`.

---

## 075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)
- **배열 (Array)**: `자료형 변수명[개수] = {초깃값};` (C/Java). 2차원 배열은 `변수명[행][열]`.
- **조건문 (if/switch)**:
  - C/Java: `if (조건) { ... } else if (조건) { ... } else { ... }`
  - Python: `if 조건:` -> `elif 조건:` -> `else:`
  - switch문 (C/Java): 식의 값에 따라 `case`를 찾아가며, `break;`가 없으면 아래 문장들도 계속 실행됨.
- **반복문 (for/while)**:
  - for문 (C/Java): `for (초기식; 조건식; 증감식) { ... }`
  - for문 (Python): `for 변수 in range(시작, 끝+1):`
  - while문: 조건이 참일 동안 반복.
  - do~while문 (C/Java): 조건과 상관없이 무조건 **최소 1번**은 실행하고 조건을 검사함.

**Giải thích (Vietnamese):**
- Trong Python, cấu trúc điều kiện là `if`, `elif` (viết tắt của else if) và `else`. Không cần ngoặc nhọn `{}` mà dùng thụt lề (indentation).
- `do~while` khác `while` ở chỗ: `do~while` sẽ làm việc trước rồi mới kiểm tra điều kiện sau, nên chắc chắn code bên trong được chạy ít nhất 1 lần.

---

## 078. 사용자 정의 함수와 클래스 (User Defined Functions & Classes)
- **접근 제어자 (JAVA Access Modifiers)**:
  1. `public`: 모든 접근 허용 (Bất cứ đâu cũng gọi được).
  2. `protected`: 같은 패키지 + 상속받은 자식 클래스만 허용.
  3. `default`: 같은 패키지(폴더) 내에서만 허용.
  4. `private`: 오직 해당 객체 내에서만 허용 (Bảo mật cao nhất).
- **클래스와 생성자 (Class & Constructor)**:
  - JAVA: 생성자 이름은 클래스 이름과 동일하며 반환값이 없음. `this` 키워드로 인스턴스 변수(필드)를 가리킴.
  - Python: `class` 키워드 사용. 생성자는 매직 메소드 `__init__(self, ...)`로 정의. `self`는 객체 자신을 참조(JAVA의 `this`와 유사).

---

## 079. 프로그래밍 언어의 종류 (Types of Programming Languages)
- **절차적 언어 (Procedural)**: 코드를 순차적인 함수(Procedure) 단위로 나누어 해결. (C, FORTRAN, ALGOL 등).
- **객체지향 언어 (Object-Oriented)**: 데이터와 메소드를 묶어 '객체'로 만듦 (캡슐화, 상속, 다형성 지원). (C++, JAVA 등). JAVA는 '가비지 컬렉터(Garbage Collector)'가 메모리를 자동 관리함.
- **스크립트 언어 (Scripting)**: 컴파일 없이 인터프리터 방식으로 바로 실행되는 언어. (Python, JavaScript, PHP, Bash 등).
  - PHP: 웹 서버용 스크립트. `@`를 쓰면 에러 무시.
  - JavaScript: 웹 브라우저 제어 (클래스와 프로토타입 기반).

**Giải thích (Vietnamese):**
- Ngôn ngữ thủ tục (như C) chạy từ trên xuống dưới, gọi các hàm.
- Ngôn ngữ OOP (như Java, C++) nhóm code thành các "Thực thể" (Object). Java có Garbage Collector tự động dọn dẹp RAM không dùng đến.
- Ngôn ngữ Script (Python, JS) không cần biên dịch ra file `.exe` mà chạy trực tiếp, rất linh hoạt.

---

## 080 - 081. 라이브러리와 예외처리 (Libraries & Exception Handling)
- **C언어 표준 라이브러리**:
  - `stdio.h`: 입출력 (`printf`, `scanf`).
  - `stdlib.h`: 자료형 변환 (`atoi`: char->int).
  - `string.h`: 문자열 처리 (`strlen`, `strcpy`).
  - `math.h`: 수학 함수 (`sqrt`: 제곱근).
- **예외처리 (Exception Handling)**:
  - JAVA: `try { 실행 } catch (예외객체 e) { 에러처리 } finally { 무조건 실행 }`
  - Python: `try: ... except 예외객체: ... finally: ...`
  - 주요 예외객체: `NullPointerException` (객체가 없을 때), `ZeroDivisionError` (0으로 나눌 때).

---

# Chapter 3. 응용 SW 기초 기술 활용 (Phần 3: Ứng dụng kỹ thuật cơ sở phần mềm)

## 082. 운영체제 기능 및 종류 (Operating System OS)
- **운영체제의 주요 프로그램**:
  - **제어 프로그램 (Control Program)**: 감시(Kernel), 작업 제어, 데이터 관리.
  - **처리 프로그램 (Processing Program)**: 언어 번역(컴파일러), 서비스, 문제 프로그램.
- **쉘(Shell)과 커널(Kernel)**:
  - **쉘 (Shell)**: 사용자의 명령어를 해석하여 커널로 전달 (사용자 인터페이스).
  - **커널 (Kernel)**: 핵심 모듈. 하드웨어/메모리/프로세스를 직접 제어 및 관리.
- **운영체제 종류**:
  - **Windows**: GUI, 선점형 멀티태스킹, PnP(자동 감지) 기능.
  - **Linux / Unix**: 오픈소스 (Linux), 트리 구조 파일 시스템. 시분할 시스템.
  - **Unix 파일 시스템 구조**: 부트 블록 -> 슈퍼 블록 (전체 정보) -> 아이노드(i-node) 블록 (파일 메타데이터) -> 데이터 블록 (실제 파일 내용).

**Giải thích (Vietnamese):**
OS giống như quản gia của máy tính.
- Kernel (Hạt nhân) là bộ não xử lý phần cứng. Shell (Vỏ) là cái dòng lệnh hoặc giao diện để con người nói chuyện với bộ não đó.
- Hệ thống tệp của UNIX chia làm 4 phần: Boot (chứa code khởi động) -> Super (Thông tin tổng quan) -> i-node (Lưu tên file, quyền truy cập...) -> Data (Nội dung file thực tế).

**💡 Mẹo ghi nhớ (Mnemonics):**
**제어 프로그램**: 감작데 (감시, 작업, 데이터). / **처리 프로그램**: 언서문 (언어, 서비스, 문제).

---

## 083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)
- **최초 적합 (First fit)**: 가장 처음 만나는 빈 공간에 할당 (빠름).
- **최적 적합 (Best fit)**: 자원 낭비(단편화)가 가장 적은 핏(딱 맞는) 공간에 할당.
- **최악 적합 (Worst fit)**: 단편화가 가장 큰(넓은) 공간에 할당 (남은 공간을 다시 쓰기 위해).

**Giải thích (Vietnamese):**
Khi một phần mềm cần RAM, OS sẽ nhét nó vào đâu?
- First fit: Thấy chỗ nào trống nhét vào luôn (Nhanh).
- Best fit: Tìm chỗ nào vừa khít nhất để nhét (Tiết kiệm chỗ).
- Worst fit: Cố tình nhét vào chỗ rộng nhất (Để chừa lại không gian rộng cho các app sau).

---

## 084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)
- 메모리가 꽉 찼을 때 어떤 페이지를 내보낼지 결정.
- **FIFO (First In First Out)**: 가장 먼저 들어온 페이지를 교체.
- **OPT (Optimal)**: 앞으로 가장 오랫동안 사용되지 않을 페이지를 교체 (이론상 최적).
- **LRU (Least Recently Used)**: (과거 기준) 가장 오랫동안 사용되지 않은 페이지를 교체.
- **LFU (Least Frequently Used)**: 사용(참조) 횟수가 가장 적은 페이지 교체.
- **NUR (Not Used Recently)**: 최근에 사용하지 않은 페이지 교체 (참조 비트 사용).
- **지역성 (Locality)**: 프로세스가 특정 메모리 영역을 집중적으로 참조하는 현상.
  - 공간 지역성: 근처 메모리 참조 (배열).
  - 시간 지역성: 방금 참조한 곳 다시 참조 (루프, 변수).
- **스레싱 (Thrashing)**: 실제 CPU 연산보다 페이지 교체에 더 많은 시간이 소요되어 시스템 성능이 뚝 떨어지는 현상.

**Giải thích (Vietnamese):**
Khi RAM đầy, máy phải đẩy tạm dữ liệu ra ổ cứng.
- LRU: Đuổi cái nào lâu nhất không ai thèm đụng tới (Thường xuyên dùng nhất).
- LFU: Đuổi cái nào ít được gọi tên nhất.
- Locality: Chương trình có xu hướng dùng lại những dữ liệu gần nhau (Ví dụ chạy vòng lặp `for`).
- Thrashing: Tình trạng máy tính bị đơ, giật lag vì RAM quá đầy, máy mải mê swap dữ liệu ra vào ổ cứng mà không chịu tính toán xử lý.

---

## 085. 프로세스 및 스레드 (Process & Thread)
- **프로세스 상태 (Process States)**: 생성(Create) -> 준비(Ready) -> 실행(Running) -> 대기(Wait/Block) -> 종료(Exit).
- **상태 전이 (State Transitions)**:
  - **Dispatch**: 준비 -> 실행 (CPU 할당받음, 문맥교환 발생).
  - **Timeout (Timer Runout)**: 실행 -> 준비 (할당된 시간 초과).
  - **Block**: 실행 -> 대기 (I/O 작업 요청).
  - **Wake Up**: 대기 -> 준비 (I/O 작업 완료).
- **PCB (Process Control Block)**: OS가 프로세스를 관리하기 위해 유지하는 정보 블록 (상태, 식별자, 스택 정보 등).
- **문맥 교환 (Context Switch)**: CPU가 프로세스를 바꿀 때 현재 상태를 PCB에 저장하고 새 프로세스 상태를 불러오는 작업.
- **스레드 (Thread)**: 커널 수준(느리지만 안정적), 사용자 수준(빠르지만 불안정).

**Giải thích (Vietnamese):**
Process là một chương trình đang chạy.
Khi Process A đang chạy, hết thời gian (Timeout), OS sẽ cất trạng thái của A vào tờ giấy nhớ gọi là "PCB", sau đó gọi Process B lên chạy. Việc chuyển đổi này gọi là "Context Switch" (Chuyển đổi ngữ cảnh). Chuyển đổi càng nhiều máy càng chậm.

**💡 Mẹo ghi nhớ (Mnemonics):**
**디타블웨** (Dispatch, Timeout, Block, WakeUp): Chu trình chuyển trạng thái của Process.

---

## 086. 프로세스 스케줄링 (Process Scheduling)
- **선점형 (Preemptive)**: 운영체제가 CPU를 강제로 뺏을 수 있음. 빠르고 대화식 시스템에 유리하지만 오버헤드 발생. (RR, SRT, MLQ, MLFQ).
- **비선점형 (Non-Preemptive)**: 한 프로세스가 끝나야만 다음 프로세스가 CPU를 씀. 일괄처리에 적합. (FCFS, SJF, HRN).
  - **FCFS**: 먼저 온 놈이 먼저 (First Come First Serve).
  - **SJF**: 짧은 작업 먼저 (Shortest Job First). 긴 작업은 무한 대기(기아 상태) 발생 가능.
  - **HRN**: SJF의 단점(기아 상태) 보완. 우선순위 = (대기시간 + 서비스시간) / 서비스시간. 결과값이 큰 것부터 우선 처리!

**Giải thích (Vietnamese):**
Lập lịch cho CPU:
- Độc quyền (Non-Preemptive): Đang chạy thì không ai được cướp (Giống như đang đi vệ sinh, người khác phải đợi). Ví dụ: FCFS, SJF, HRN.
- Cướp quyền (Preemptive): Đang chạy nhưng có việc khẩn cấp (hoặc hết giờ) thì hệ thống đuổi ra cho người khác vào. Ví dụ: RR, SRT.
- Công thức HRN rất hay thi: `(Thời gian đợi + Thời gian xử lý) / Thời gian xử lý`. Việc đợi càng lâu ưu tiên càng cao.

---

## 교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)
- **교착상태(Deadlock)**: 두 프로세스가 서로의 자원을 기다리며 멈춰버린 현상.
- **상호배제 알고리즘 (Mutual Exclusion)**: 한 번에 하나의 프로세스만 자원을 쓰게 함.
  - Dekker: 두 프로세스 간 Flag와 Turn 변수 사용.
  - Peterson: 두 프로세스 간 상대방에게 양보.
  - Lamport: 고유 번호(티켓) 부여, 번호순 진입.
  - Semaphore: 정수 변수(P연산, V연산)를 이용해 접근 통제.
## 086. 프로세스 스케줄링과 교착상태 (Process Scheduling & Deadlock) - 계속
- **교착상태(Deadlock) 4가지 필요충분조건**:
  1. **상호배제 (Mutual Exclusion)**: 한 번에 한 프로세스만 자원 사용.
  2. **점유와 대기 (Hold and Wait)**: 자원을 가진 채로 다른 자원을 기다림.
  3. **비선점 (Non-Preemption)**: 남의 자원을 강제로 뺏을 수 없음.
  4. **환형 대기 (Circular Wait)**: 꼬리에 꼬리를 물고 서로의 자원을 기다림.
- **교착상태 해결 방법 (Handling Deadlocks)**:
  - **예방 (Prevention)**: 4가지 조건 중 하나를 부정 (자원 낭비 심함).
  - **회피 (Avoidance)**: 발생 가능성을 피해 자원 할당 (예: **은행원 알고리즘**, 자원 할당 그래프).
  - **발견 (Detection)**: 발생을 허용하고 나중에 감시하여 발견.
  - **복구 (Recovery)**: 발견 후 프로세스를 종료하여 자원 회복 (기아 상태 주의).

**Giải thích (Vietnamese):**
Deadlock (Bế tắc) giống như kẹt xe ở ngã tư. Ai cũng tiến lên một chút (Chiếm giữ), không ai chịu lùi (Không thể cướp quyền), và chờ người kia nhường đường (Vòng tròn chờ đợi).
- Phòng ngừa (Prevention): Xây cầu vượt để không bao giờ kẹt xe (Tốn kém).
- Né tránh (Avoidance): Xem Google Maps, thấy đường đỏ (nguy cơ kẹt) thì không đi vào (Thuật toán Banker).
- Phục hồi (Recovery): Kẹt rồi thì gọi công an đến cẩu bớt 1 xe đi để thông đường.

**💡 Mẹo ghi nhớ (Mnemonics):**
Điều kiện: **상점비환** (Tương - Chiếm - Phi - Hoàn)
Giải quyết: **예회발복** (Dự - Tị - Phát - Phục).

---

## 087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)
- **환경변수 명령어**:
  - `printenv`: 단일 변수 반환.
  - `env`: 환경 변수 출력/설정.
  - `set` / `setenv`: 변수 추가/업데이트.
  - `export`: 변수를 전역(Global) 변수로 변경 (export 안하면 현재 쉘에만 국한됨).
- **운영체제별 주요 명령어 (Windows / Unix(Linux))**:
  - 목록 보기: `dir` / `ls`
  - 복사: `copy` / `cp`
  - 삭제: `del` / `rm`
  - 이름 변경/이동: `ren`, `move` / `mv`
  - 폴더 생성: `md` / `mkdir`
  - 기타 Unix 명령어:
    - `chmod`: 권한 변경. / `chown`: 소유자 변경.
    - `cat`: 파일 내용 출력.
    - `grep`: 문자열(패턴) 검색 (Windows의 `find`).
    - `ps`: 프로세스 상태. / `kill`: 프로세스 종료.
    - `tar`: 파일 묶기/풀기. / `crontab`: 스케줄링.

**Giải thích (Vietnamese):**
- Lệnh `export` rất hay dùng trong Linux để set biến môi trường (Ví dụ: `export PATH=...`) để các chương trình khác cũng đọc được biến đó.
- Các lệnh Linux kinh điển: `ls` (list - liệt kê), `cp` (copy), `rm` (remove), `mv` (move), `mkdir` (make directory), `grep` (tìm text).

---

## 088. 인터넷 구성과 네트워크 - OSI 7계층 (OSI 7 Layer)
- **IEEE 802 표준**: 802.3 (Ethernet, 유선랜), 802.11 (무선랜, Wi-Fi).
- **OSI 7계층 (상위 계층부터)**:
  7. **응용 계층 (Application)**: 사용자 인터페이스. (HTTP, FTP, DNS) - 데이터 단위: Data.
  6. **표현 계층 (Presentation)**: 암호화, 압축, 포맷 변환. - 데이터 단위: Data.
  5. **세션 계층 (Session)**: 응용 프로그램 간 논리적 연결 생성/유지. - 데이터 단위: Data.
  4. **전송 계층 (Transport)**: 종단 간(End-to-End) 신뢰성 있는 전송. 포트 번호 사용. (TCP, UDP). 장비: L4 스위치. - 데이터 단위: Segment.
  3. **네트워크 계층 (Network)**: 경로 설정(Routing). IP 주소 사용. (IP, ICMP, ARP). 장비: 라우터, L3 스위치. - 데이터 단위: Packet.
  2. **데이터 링크 계층 (Data Link)**: 인접 노드 간 전송 제어, 오류/흐름 제어. MAC 주소 사용. (HDLC, PPP). 장비: 브리지, L2 스위치. - 데이터 단위: Frame.
  1. **물리 계층 (Physical)**: 전기적 신호 전송. 장비: 허브, 리피터. - 데이터 단위: Bit.

**Giải thích (Vietnamese):**
Mô hình OSI 7 lớp chia nhỏ quá trình gửi dữ liệu qua mạng.
Tầng 1 (Cáp mạng, dây điện), Tầng 2 (Truyền giữa 2 máy tính kề nhau qua địa chỉ MAC), Tầng 3 (Tìm đường đi trên mạng Internet qua IP), Tầng 4 (Đảm bảo gói tin không bị rớt qua TCP/UDP), Tầng 5-7 (Phần mềm xử lý hiển thị lên màn hình).

**💡 Mẹo ghi nhớ (Mnemonics):**
Tên 7 tầng từ dưới lên (1->7): **물데네 전세표응** (Vật - Dữ - Mạng - Truyền - Phiên - Biểu - Ứng).
Đơn vị dữ liệu (1->4): **비프패세** (Bit, Frame, Packet, Segment).

---

## 088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어
- **TCP (Transmission Control Protocol)**: 연결 지향, 신뢰성 높음, 흐름 및 오류 제어 지원. 속도는 느림.
- **UDP (User Datagram Protocol)**: 비연결 지향, 신뢰성 낮음(오류 복구 안함). 실시간 전송(스트리밍)에 유리하여 속도가 빠름.
- **TCP 흐름 제어 (Flow Control)**: 수신측이 처리할 수 있는 만큼만 보냄 (Window 크기 사용).
  - Stop and Wait: 1개 보내고 응답 기다림.
  - Sliding Window: 윈도우 크기만큼 한 번에 여러 개 보냄 (효율적).
- **TCP 오류 제어 (Error Control)**:
  - Go Back n: 오류 발생한 패킷부터 **그 이후의 모든 패킷** 재전송.
  - Selective Repeat: 오류가 발생한 **해당 패킷만** 골라서 재전송.

**Giải thích (Vietnamese):**
- TCP giống như gửi thư bảo đảm, phải có người ký nhận mới yên tâm. Chậm nhưng chắc.
- UDP giống như phát loa phóng thanh, cứ phát ra, ai nghe được thì nghe. Phù hợp gọi Video call (Rớt 1 hình cũng không sao, quan trọng là độ trễ thấp).
- Trượt cửa sổ (Sliding Window): Kỹ thuật gửi liên tục nhiều gói tin mà không cần đợi từng gói báo nhận.
- Go Back N: Bị lỗi gói số 3, hệ thống sẽ gửi lại từ gói 3, 4, 5... Selective Repeat: Lỗi gói 3 thì chỉ gửi lại đúng gói 3.

---

## 089. IP와 서브네팅, IPv4 vs IPv6 (IP & Subnetting)
- **IPv4 헤더 필드**: Version, Header Length, TOS, Total Length, TTL (수명), Source/Destination Address 등.
- **IPv4 클래스**:
  - Class A: `0.~` (거대 망)
  - Class B: `128.~` (중형 망)
  - Class C: `192.~` (소형 망)
- **IPv4 vs IPv6**:
  - 주소 길이: IPv4(32비트) -> **IPv6(128비트)** 확장.
  - IPv6 특징: 호스트 주소 자동 설정, 패킷 크기 제한 없음, 헤더 단순화, **보안(인증/무결성) 강화**, 플로 레이블링(QoS), 이동성 지원.
- **데이터 전송 방법**:
  - **유니캐스트 (Unicast)**: 1:1 통신.
  - **멀티캐스트 (Multicast)**: 1:N (특정 그룹).
  - **브로드캐스트 (Broadcast)**: 1:전체 (IPv4에서만 사용, 과부하 원인).
  - **애니캐스트 (Anycast)**: 1:가장 가까운 1개 노드 (IPv6에서 도입).

**Giải thích (Vietnamese):**
IPv4 sắp hết số (vì chỉ có 32 bit = khoảng 4 tỷ địa chỉ). Nên người ta sinh ra IPv6 (128 bit = số lượng vô hạn). IPv6 bảo mật tốt hơn, không cần cấu hình DHCP phức tạp (tự gán địa chỉ) và loại bỏ Broadcast để tránh nghẽn mạng.

**💡 Mẹo ghi nhớ (Mnemonics):**
Các kiểu truyền:
- Unicast = Nói chuyện riêng.
- Multicast = Nhắn tin vào group chat Zalo.
- Broadcast = Cầm loa hét cho cả trường nghe (Chỉ IPv4).
- Anycast = Gọi tổng đài, ai rảnh thì nhấc máy nghe trước (Chỉ IPv6).

---

## 추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)

### 232. 배치 프로그램 (Batch Program)
- 대량의 데이터를 사용자 개입 없이 정해진 순서에 따라 **일괄적으로 처리**하는 방식.
- 야간 시간대 등 자원 소모가 적은 시간에 실행됨.
- **필수 요소 5가지**: 대용량, 자동화, 견고성, 안정성, 성능.

**Giải thích (Vietnamese):**
Chương trình Batch (xử lý hàng loạt) là loại phần mềm tự động chạy ngầm, thường vào ban đêm. Ví dụ: Cuối ngày ngân hàng tổng hợp lại toàn bộ giao dịch trong ngày, xử lý một lúc hàng triệu giao dịch mà không cần người bấm nút.

### 233 & 235. 데이터 타입 크기 (Data Type Sizes - C/C++ vs JAVA)
- **C/C++**: `char`(1바이트), `short`(2바이트), `int`(4바이트), `float`(4바이트), `double`(8바이트).
- **JAVA**: `byte`(1바이트), **`char`(2바이트, 유니코드 지원)**, `int`(4바이트), `boolean`(1바이트).

**Giải thích (Vietnamese):**
Lưu ý quan trọng: Trong C, `char` (kí tự) chiếm 1 byte. Nhưng trong Java, `char` chiếm 2 byte vì Java dùng bảng mã Unicode để hỗ trợ mọi ngôn ngữ trên thế giới (kể cả tiếng Hàn, tiếng Việt).

### 234. C언어의 구조체 (struct)
- 서로 다른 데이터 타입을 하나로 묶어 관리하는 사용자 정의 자료형. 배열(동일 타입)과의 차이점.
- (Ví dụ: Một `struct SinhVien` có thể chứa Tên(string), Tuổi(int), Điểm(float)).

### 236. Python 시퀀스 자료형
- 리스트(List): `[]` 변경 가능.
- 튜플(Tuple): `()` **변경 불가능(Immutable)**.
- (Ví dụ: Tuple dùng để lưu toạ độ GPS không bao giờ đổi).

### 238. 가비지 콜렉터 (Garbage Collector)
- 사용되지 않는 메모리를 자동으로 해제해주는 기능 (메모리 누수 방지). Java 등 현대 언어의 핵심.

### 239 - 244. 각종 연산자
- 산술(`%`, `++`), 관계(`==`, `!=`), 비트(`&`, `|`, `^`, `<<`), 논리(`&&`, `||`), 대입(`+=`), 조건 삼항연산자.
- `a += 1`은 `a = a + 1`과 같다.
- 비트 XOR(`^`): 두 비트가 다를 때만 1을 반환.
## 232. 배치 프로그램 (Batch Program)
- 대량의 데이터를 사용자 개입 없이 정해진 순서에 따라 **일괄적으로 처리**하는 방식.
- 야간 시간대 등 자원 소모가 적은 시간에 실행됨.
- **필수 요소 5가지**: 대용량, 자동화, 견고성(오류 시에도 중단 없이 기록/지속), 안정성, 성능.

**Giải thích (Vietnamese):**
Chương trình Batch (xử lý hàng loạt) tự động chạy ngầm để xử lý lượng lớn dữ liệu mà không cần con người can thiệp.
- Tính kiên cố (견고성): Lỡ có 1 dòng dữ liệu bị lỗi, chương trình không bị sập mà sẽ ghi log lại và chạy tiếp dòng khác.

**💡 Mẹo ghi nhớ (Mnemonics):**
**대자견안성** (Đại - Tự - Kiên - An - Tính): 대용량, 자동화, 견고성, 안정성, 성능.

---

## 233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)
- `char`: 1바이트 (문자 하나)
- `short`: 2바이트 (짧은 정수)
- `int` / `long`: 4바이트 (기본 정수)
- `long long`: 8바이트 (긴 정수)
- `float`: 4바이트 (실수)
- `double`: 8바이트 (정밀도 높은 실수)

**Giải thích (Vietnamese):**
Kích thước bộ nhớ các biến trong C/C++. Chữ cái (char) chiếm 1 byte. Số nguyên (int) chiếm 4 byte. Số thực (float) 4 byte, double (gấp đôi) là 8 byte.

---

## 234. C언어의 구조체 (struct in C)
- 서로 다른 데이터 유형을 가진 변수들을 하나로 묶어 관리하는 사용자 정의 자료형.
- 배열(Array)은 **동일한 자료형**만 모으지만, 구조체(Struct)는 **상이한 자료형**을 모을 수 있음.

**Giải thích (Vietnamese):**
Struct (Cấu trúc) dùng để gom nhóm nhiều biến khác kiểu lại với nhau. Ví dụ tạo kiểu `SinhVien` gồm tên (chuỗi) và tuổi (số). Trong khi Mảng (Array) chỉ được lưu cùng một kiểu (hoặc toàn chuỗi, hoặc toàn số).

---

## 235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)
- `byte`: 1바이트 (작은 숫자)
- `boolean`: 1바이트 (참/거짓)
- **`char`: 2바이트** (유니코드 지원으로 인해 C언어와 달리 2바이트를 차지함)
- `int`: 4바이트
- `long`: 8바이트 (C언어는 보통 4바이트지만 JAVA는 8바이트)
- `float`: 4바이트 / `double`: 8바이트

**Giải thích (Vietnamese):**
Java có 2 điểm khác biệt lớn với C: `char` chiếm 2 byte (để lưu bảng mã Unicode đa ngôn ngữ), và có kiểu `boolean` (chỉ lưu True/False).

---

## 236. Python의 시퀀스 자료형 (Sequence Data Types in Python)
- 여러 값이 연속적으로 이어진 데이터 구조.
- **리스트(List)**: `[]` 사용. 데이터의 추가/삭제/변경이 자유로움 (Mutable).
- **튜플(Tuple)**: `()` 사용. 한 번 생성하면 데이터의 변경(수정/삭제)이 **불가능함** (Immutable). 읽기 전용에 적합.
- **range**: 반복문에서 연속된 숫자를 생성할 때 사용.

**Giải thích (Vietnamese):**
List và Tuple đều dùng để lưu danh sách. Nhưng List có thể sửa được, còn Tuple thì "Bất di bất dịch" (không thể thêm/xoá/sửa sau khi tạo).

---

## 237. 변수명 작성 규칙 (Variable Naming Rules)
- 영문자, 숫자, 밑줄(`_`)의 조합만 가능.
- **첫 글자는 숫자로 시작할 수 없음** (예: `1a` 안됨).
- 공백이나 특수문자(`+`, `-`, `*`, `/`, `@` 등) 사용 금지.
- 예약어(`if`, `for`, `while` 등) 사용 금지.
- 대소문자 엄격히 구분.

**Giải thích (Vietnamese):**
Quy tắc đặt tên biến: Không được bắt đầu bằng số, không có khoảng trắng, không chứa ký tự đặc biệt (trừ dấu gạch dưới `_`), không dùng từ khoá của ngôn ngữ.

---

## 238. 가비지 콜렉터 (Garbage Collector)
- 더 이상 사용되지 않고 메모리를 점유하고 있는 변수/객체를 시스템이 **자동으로 해제**하여 자원을 회수하는 모듈.
- 메모리 누수(Memory Leak)를 방지. JAVA 등에서 사용됨.

**Giải thích (Vietnamese):**
"Người dọn rác" tự động. Bạn cứ việc tạo biến dùng, khi không dùng nữa, hệ thống sẽ tự động xoá nó khỏi RAM để giải phóng bộ nhớ. Trong C/C++ bạn phải tự dọn dẹp, nhưng Java/Python có tính năng này.

---

## 239 - 243. 연산자 (Operators)
- **산술 연산자**: 사칙연산, `%`(나머지), `++`/`--`(증감).
  - 전치(`++a`): 먼저 증가시키고 연산. 후치(`a++`): 연산 후 증가시킴.
- **관계 연산자**: `==`(같다), `!=`(다르다), `>`, `<`. C언어에서는 0 이외의 값을 참(True)으로 간주.
- **비트 연산자**: 비트 단위 연산. `&`(AND), `|`(OR), `^`(XOR: 서로 다를 때만 1), `~`(NOT). `<<`, `>>`(비트 이동).
- **논리 연산자**: `&&`(AND), `||`(OR), `!`(NOT).
- **대입 연산자**: `=`, `+=`, `-=` 등. `a += 1`은 `a = a + 1`과 동일.

---

## 244. 조건(삼항) 연산자 (Ternary Operator)
- 조건의 참/거짓에 따라 서로 다른 값을 반환.
- 형식: `조건 ? 참일때_값 : 거짓일때_값;`
- (예: `int max = (a > b) ? a : b;`)

**Giải thích (Vietnamese):**
Toán tử 3 ngôi giúp viết tắt câu lệnh if-else trên 1 dòng. Trả về giá trị 1 nếu điều kiện đúng, giá trị 2 nếu sai.

---

## 245. 연산자 우선순위 (Operator Precedence)
- 하나의 수식에 여러 연산자가 있을 때 계산되는 순서.
- 순위: **단항**(`!`, `++`, `~`) > **산술**(`*`, `/` > `+`, `-`) > **관계**(`>`, `==`) > **논리**(`&&` > `||`) > **대입**(`=`, `+=`).
- 괄호 `()`가 가장 우선.

**Giải thích (Vietnamese):**
Thứ tự ưu tiên tính toán: Ngoặc () -> Đơn nguyên (phủ định, tăng giảm) -> Nhân chia cộng trừ -> So sánh -> Logic (AND trước OR sau) -> Gán.

**💡 Mẹo ghi nhớ (Mnemonics):**
**단산관논대** (Đơn - Toán - Quan - Luận - Gán): 단항 -> 산술 -> 관계 -> 논리 -> 대입.

---

## 246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)
- **`scanf("서식문자열", &변수)`**: C언어 표준 입력. 변수명 앞에 주소 연산자 **`&`**를 반드시 붙여야 함.
- **`printf("서식문자열", 변수)`**: C언어 표준 출력. `&`를 붙이지 않음.
- **서식 문자열**:
  - `%d`: 10진수 정수 / `%f`: 실수 (예: `%8.2f`는 총 8자리, 소수점 2자리) / `%c`: 문자 1개 / `%s`: 문자열.
  - `%o`: 8진수 / `%x`: 16진수.
- **제어문자 (Escape Sequence)**:
  - `\n`: 줄바꿈 (New Line) / `\t`: 탭 (Tab) / `\b`: 백스페이스 / `\0`: 널 문자(문자열의 끝 표시).

**Giải thích (Vietnamese):**
Nhớ kĩ `scanf` phải có dấu `&` (địa chỉ) để nhét dữ liệu vào đúng chỗ trong RAM. `printf` thì không cần. Dấu `\0` (Null) cực kỳ quan trọng trong C để đánh dấu kết thúc một chuỗi (string).

---

## 250. JAVA에서의 표준 출력 (Standard Output in JAVA)
- `System.out.print()`: 형식 없이 그대로 출력 (줄바꿈 없음).
- `System.out.println()`: 출력 후 자동으로 줄바꿈(Enter) 수행.
- `System.out.printf()`: C언어처럼 서식 문자열(`%d` 등)을 사용하여 출력.
- 문자열과 변수를 섞어 쓸 때 `+` 연산자로 연결 가능.

---

## 251. 단순 if문 (Simple if Statement)
- 조건의 참/거짓에 따라 실행할 문장 결정.
- 문장이 두 개 이상이면 반드시 중괄호 `{ }`로 묶어야 함.
- C언어에서는 조건식 결과가 0이면 거짓(False), **0 이외의 모든 값은 참(True)**으로 간주.

---

## 252. 다중 if문 (Multiple if Statement)
- 처리할 조건이 여러 개일 때 `else if`를 사용해 순차적으로 판단.
- 위에서 조건이 참이면 해당 블록을 실행하고 빠져나옴 (아래 조건은 검사하지 않음).
- 모든 조건이 거짓일 때 마지막 `else`가 실행됨.

---

## 253. switch문 (switch Statement)
- 변수의 값에 따라 일치하는 `case` 문장을 실행하는 다분기 제어문.
## 254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)
- **for문**: 횟수가 정해진 반복(초기화, 조건검사, 증감식). 배열 순회에 주로 사용.
- **while문**: 조건이 참인 동안 반복(선행 판단). 조건이 항상 참이면 무한 루프 발생.
- **do~while문**: **최소 1번은 무조건 실행**한 후 조건을 검사(후행 판단).
- **break**: 현재 실행 중인 루프(블록)를 즉시 완전히 빠져나감.
- **continue**: 루프를 완전히 빠져나가지 않고, **다음 반복 회차로 건너뜀**.

**Giải thích (Vietnamese):**
- `for`: Biết trước số lần lặp (VD: đếm từ 1 đến 10).
- `while`: Lặp cho đến khi điều kiện sai (VD: lặp tới khi game over).
- `break`: Dừng cuộc chơi ngay lập tức, thoát ra ngoài.
- `continue`: Bỏ qua vòng lặp hiện tại, đi tới vòng lặp tiếp theo (VD: đếm từ 1 đến 10, nếu gặp số 5 thì `continue` -> in ra 1 2 3 4 6 7 8 9 10).

---

## 258 - 261. 배열과 문자열 (Arrays & Strings)
- **배열 (Array)**: **동일한 자료형**의 변수들을 연속된 메모리에 모아둔 것. `인덱스(첨자)`는 0부터 시작. 배열 이름 자체가 **첫 번째 요소의 시작 주소**를 의미.
- **2차원 배열**: 행과 열의 평면 구조 (예: `a[3][4]`는 3행 4열로 총 12개).
- **배열 초기화**: 선언과 동시에 값을 넣는 것. 크기를 생략해도 값의 개수만큼 자동 결정됨. 초기화되지 않은 빈칸은 자동으로 `0`으로 채워짐.
- **배열 형태의 문자열 (C언어)**: C언어는 문자열 자료형이 없어 `char` 배열을 사용. 문자열 끝에는 반드시 **널 문자(`\0`)**가 포함되어야 함 (글자수 + 1바이트 크기 필요).

**Giải thích (Vietnamese):**
Trong C, chuỗi "love" sẽ chiếm 5 ô nhớ (l, o, v, e, `\0`). Ký tự `\0` (Null) báo hiệu cho máy tính biết "đây là kết thúc của chuỗi".

---

## 262 - 263. 포인터 (Pointers)
- **포인터 (Pointer)**: 변수의 실제 **메모리 주소값**을 저장하는 특수 변수.
- `*` (간접 참조 연산자): 포인터가 가리키는 주소의 '값'.
- `&` (주소 연산자): 변수의 '주소'.
- **포인터와 배열**: 배열 이름은 포인터와 같음 (`배열명 == &배열명[0]`). 포인터 연산(`p+i`)으로 배열 요소에 접근 가능.

**Giải thích (Vietnamese):**
Pointer (Con trỏ) không lưu giá trị (như số 5), mà lưu "địa chỉ nhà" (ví dụ: nhà số 100A). 
`&a` là lấy địa chỉ nhà của a. `*p` là mở cửa vào nhà để lấy đồ (lấy giá trị).

---

## 264 - 274. 파이썬 문법 (Python Syntax & Basics)
- **기본 문법**: 자료형 선언 생략, 세미콜론(`;`) 불필요. 코드 블록은 중괄호 `{}` 대신 **콜론(`:`)과 들여쓰기(Indentation)**로 구분.
- **입출력**: `input()` (기본적으로 모두 문자열로 입력받음), `print()`. `sep`(분리 문자), `end`(종료 문자).
- **형변환 (Casting)**: `int()`(정수), `float()`(실수). 여러 개 입력 받을 땐 `map(int, input().split())` 사용.
- **자료형**:
  - **리스트 (List, `[]`)**: 수정/추가/삭제 자유로움 (Mutable). 서로 다른 타입 혼용 가능.
  - **딕셔너리 (Dictionary, `{}`)**: `Key:Value` 쌍으로 저장 (해시 맵). Key로 빠르게 검색.
  - **슬라이스 (Slice)**: `객체[시작:끝:증가값]`. 끝 번호는 제외됨 (n-1까지). 원본은 변경하지 않음.
- **제어문**: `if`, **`elif`** (else if 아님), `else`. `for i in range(시작, 끝)` 또는 `for i in 리스트`. `while`문.
- **클래스 (Class)**: `class` 키워드. 메소드(함수) 정의 시 첫 번째 매개변수로 반드시 **`self`**를 써야 함. 파이썬은 클래스 밖에서도 `def`로 독립된 함수를 만들 수 있음.

**Giải thích (Vietnamese):**
- Python dùng "thụt lề" (indentation) để phân chia các khối code thay vì `{}`.
- `input()` luôn trả về chuỗi (String). Nếu nhập số 5, nó hiểu là chữ "5". Phải bọc lại bằng `int(input())`.
- Dictionary giống như từ điển: tra chữ "Apple" (Key) ra "Quả táo" (Value).
- Cắt lát (Slicing): `a[1:4]` lấy các phần tử ở index 1, 2, 3 (không lấy 4).

---

## 275 - 278. 프로그래밍 언어의 종류 (Types of Programming Languages)
- **절차적 언어**: 실행 순서 중시. 
  - `COBOL` (사무용), `FORTRAN` (과학 기술 계산용), `C` (시스템 프로그래밍), `ALGOL`.
- **객체지향 언어**: 데이터+기능 캡슐화. 재사용성 높음.
  - `JAVA` (플랫폼 독립성, JVM), `C++` (C의 객체지향 확장), `Smalltalk` (최초 GUI, 순수 객체지향).
- **선언형 언어**: '무엇(What)'을 할지 기술 (함수형/논리형).
  - `LISP` (연결리스트, AI용), `PROLOG` (논리 추론, AI용), `Haskell` (순수 함수형), `XML` (구조화 문서).

---

## 279 - 280. 라이브러리 (Library)
- **라이브러리**: 자주 사용되는 함수/데이터를 모아 놓은 집합체 (개발 시간 단축, 코드 재사용).
- **C언어 표준 라이브러리 (Header Files)**:
  - `stdio.h`: 입출력 (`printf`, `scanf`)
  - `math.h`: 수학 연산 (`sqrt`, `pow`, `abs`)
  - `string.h`: 문자열 처리
  - `stdlib.h`: 유틸리티, 자료형 변환, 메모리 할당

**Giải thích (Vietnamese):**
Thư viện (Library) giống như siêu thị bán đồ làm sẵn. Bạn không cần tự viết code để tính căn bậc 2, chỉ cần gọi hàm `sqrt` trong thư viện `math.h` là xong.

---

## 281. 매시업과 SOA (SW Related Terms: Mashup & SOA)
- **매시업 (Mashup)**: 웹 서비스나 콘텐츠를 조합하여 **새로운 서비스를 만드는 기술** (예: 구글 지도 + 부동산 정보).
- **SOA (Service Oriented Architecture, 서비스 지향 아키텍처)**: 시스템을 **공유/재사용 가능한 서비스 단위**로 구축하는 구조. (계층: 표현, 업무 프로세스, 서비스 중간, 애플리케이션, 데이터 저장).

**Giải thích (Vietnamese):**
- Mashup: Lấy dữ liệu bản đồ của Google kết hợp với dữ liệu danh sách quán ăn để tạo ra app "Tìm quán ăn gần đây". (Trộn lẫn dữ liệu có sẵn để làm ra cái mới).

---

## 282. 운영체제의 정의 및 목적 (Definition & Purpose of OS)
- **운영체제(OS)**: 컴퓨터 자원(CPU, 메모리 등)을 효율적으로 관리하고 사용자에게 편리한 환경을 제공하는 소프트웨어 (Windows, Linux 등).
- 목적: 자원 관리, 편리한 인터페이스 제공, 가용성 극대화, 신뢰도 향상.
## 283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)
- **운영체제 구성**:
  - **제어 프로그램**: 감시(Supervisor, 핵심), 작업 제어, 데이터 관리.
  - **처리 프로그램**: 언어 번역(컴파일러), 서비스(유틸리티).
- **UNIX의 특징**: 대화식 운영체제, **C언어로 작성**되어 이식성이 높음. 트리(Tree) 구조의 파일 시스템.
  - **커널(Kernel)**: UNIX의 핵심. 하드웨어/메모리/프로세스 관리.
  - **쉘(Shell)**: 사용자의 명령어를 해석하여 커널에 전달하는 인터페이스.
- **파일 디스크립터 (File Descriptor)**: 시스템이 파일을 관리하기 위해 이름, 위치, 크기 등의 속성을 담아두는 제어 블록 (사용자가 직접 볼 수 없음).
- **UNIX 환경 변수**: `$HOME`(홈 디렉터리), `$PATH`(명령어 검색 경로), `$PWD`(현재 작업 폴더).
- **UNIX 명령어**: `chmod`(권한 변경), `fork`(프로세스 복제).

**Giải thích (Vietnamese):**
- Kernel là não bộ, Shell là lớp vỏ giao tiếp với người dùng.
- Lệnh `fork` trong Unix dùng để nhân bản một Process đang chạy thành một Process con mới.

---

## 289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)
- **배치 전략 (Placement)**: 최초 적합(First Fit, 빠름), 최적 적합(Best Fit, 단편화 최소), 최악 적합(Worst Fit, 큰 공간 남김).
- **페이징(Paging)**: 메모리를 **동일한 고정 크기**로 나눔. **내부 단편화** 발생 (빈 공간이 남아버림).
- **세그먼테이션(Segmentation)**: 논리적 의미(함수 등)에 따라 **가변 크기**로 나눔. **외부 단편화** 발생 (공간이 작아서 못 들어감).
- **페이지 크기**: 페이지가 작으면 내부 단편화는 줄지만, 맵 테이블이 커져 매핑 속도가 느려짐.
- **스래싱 (Thrashing)**: 빈번한 페이지 교체로 인해 시스템 처리량보다 교체 시간이 더 많아져 CPU 이용률이 급감하는 마비 상태.

**Giải thích (Vietnamese):**
- Paging (Phân trang): Cắt bánh thành các miếng bằng nhau. Điểm yếu: Ăn không hết 1 miếng sẽ dư thừa (Nội phân mảnh).
- Segmentation (Phân đoạn): Cắt bánh theo sức ăn của mỗi người (to nhỏ khác nhau). Điểm yếu: Chừa lại các khoảng trống lắt nhắt không ai nhét vừa (Ngoại phân mảnh).
- Thrashing: Máy quá tải, giật lag do mải lấy dữ liệu từ ổ cứng đắp vào RAM.

---

## 297 - 302. 프로세스와 스레드, 스케줄링 (Processes, Threads & Scheduling)
- **프로세스(Process)**: **PCB(Process Control Block)를 가진** 실행 중인 프로그램.
- **상태 전이**:
  - **Dispatch**: 준비(Ready) -> 실행(Run) (CPU 할당 받음).
  - **Timeout**: 실행(Run) -> 준비(Ready) (시간 초과).
  - **Wake Up**: 대기(Wait) -> 준비(Ready) (입출력 완료).
- **스레드(Thread)**: 프로세스 내의 독립적인 실행 흐름 (최소 작업 단위). 프로세스의 자원을 공유하여 병행성 증대 및 문맥 교환 오버헤드 감소.
- **비선점 스케줄링 (Non-Preemptive)**:
  - FCFS: 먼저 온 순서대로.
  - SJF: 실행 시간이 가장 짧은 것 먼저.
  - **HRN**: 대기 시간과 서비스 시간을 고려해 기아(Starvation) 현상 해결. 공식: **(대기시간 + 서비스시간) / 서비스시간** (값이 클수록 우선).

---

## 305 - 308. IP 주소 체계 (IPv4 vs IPv6)
- **IPv4**: 32비트 (8비트씩 4부분). 클래스 A~E로 나뉨.
- **IPv6**: 128비트 (16비트씩 8부분). 콜론(`:`)으로 구분, 16진수 사용. 
- **IPv6의 특징**: 무한대에 가까운 주소, 보안 강화, 패킷 크기 확장, PnP(자동 설정).
- **IPv6 전송 방식**: 유니캐스트(1:1), 멀티캐스트(1:N), 애니캐스트(가장 가까운 1:1).

**💡 Mẹo ghi nhớ (Mnemonics):**
IPv6 전송 방식 3총사: **유멀애** (Unicast, Multicast, Anycast). *Broadcast는 IPv4에만 있음!*

---

## 309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)
- **응용 계층 (Application, 7계층)**: HTTP(웹), FTP(파일), SMTP(메일), DNS(도메인->IP 변환), SNMP(네트워크 관리).
- **전송 계층 (Transport, 4계층)**: 
  - **TCP**: 연결형, 신뢰성 보장, 양방향. 흐름 제어.
  - **UDP**: 비연결형, 신뢰성 낮음. 속도가 빨라 스트리밍에 유리.
- **인터넷/네트워크 계층 (Network, 3계층)**: 라우터 사용.
  - **IP**: 경로 설정.
  - **ICMP**: 오류 보고 및 제어.
  - **ARP**: IP 주소 -> MAC 주소 변환. (**RARP**는 반대).
- **데이터 링크/네트워크 액세스 계층 (Data Link, 2계층)**: Ethernet(CSMA/CD 방식), HDLC.

**Giải thích (Vietnamese):**
- **ARP**: Khi biết địa chỉ IP, dùng ARP để hỏi xem "Máy nào có IP này, cho xin địa chỉ MAC của card mạng (phần cứng)".
- **ICMP**: Lệnh `ping` hay dùng trên máy tính chính là chạy giao thức ICMP để kiểm tra mạng có thông không.

---

## 226 - 227. 데이터베이스 접속 기술 (Database Connectivity)
- **JDBC (Java DataBase Connectivity)**: **자바(Java)** 프로그램 내에서 데이터베이스(DBMS)에 접속하여 SQL 문을 실행하기 위한 표준 API. 운영체제에 독립적.
- **ODBC (Open DataBase Connectivity)**: 프로그래밍 **언어에 관계없이** (C, C++, VB 등) 다양한 DBMS에 접근할 수 있게 마이크로소프트가 만든 개방형 표준 API.

**Giải thích (Vietnamese):**
- JDBC: Dành riêng cho ngôn ngữ Java.
- ODBC: Mở (Open) cho mọi ngôn ngữ khác, dùng chung thông qua một "người quản lý tài xế" (Driver Manager) để dịch lệnh SQL gửi xuống Database.


## 인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)
### TẦNG A – NOTE NÉN (ÔN / ĐI THI)
- **개념 (Khái niệm)**: 소스 코드를 컴파일하지 않고 인터프리터(Interpreter)가 한 줄씩 즉시 해석하여 실행하는 프로그래밍 언어. (Ngôn ngữ lập trình dịch và thực thi từng dòng mã nguồn trực tiếp mà không cần biên dịch toàn bộ.)
- **핵심 키워드 (Từ khóa)**: 자바 스크립트 (JavaScript), PHP, 파이썬 (Python), 쉘 스크립트 (Shell script).
- **시험 포인트 (Điểm thi)**: 클라이언트용(Client-side: JS)과 서버용(Server-side: ASP, JSP, PHP) 스크립트 언어를 구분하는 것이 단골 문제. (Phân biệt ngôn ngữ cho Client và Server là câu hỏi thường gặp.)
- **한 문장 설명 (Tóm tắt)**: 컴파일 과정이 없어 실행 속도가 빠르고 수정이 용이하여 웹 개발 및 시스템 관리에 널리 사용됨. (Tốc độ khởi động nhanh và dễ sửa đổi vì không cần biên dịch, phổ biến trong web và quản trị hệ thống.)

### TẦNG B – NOTE 보충 (HIỂU SÂU)
- **자바 스크립트 (JavaScript)**: 웹 브라우저 내에서 동작하며 입력 사항 확인 등 클라이언트 측 제어에 사용. (Chạy trên trình duyệt, kiểm soát phía client như xác thực đầu vào.)
- **PHP**: 서버용 스크립트로 C, Java와 문법이 유사. (Script cho server, cú pháp giống C/Java.)
- **파이썬 (Python)**: 객체지향 지원, 문법이 간단하여 배우기 쉽고 플랫폼 독립적인 대화형 언어. (Hỗ trợ OOP, cú pháp đơn giản, độc lập nền tảng, có tính tương tác.)
- **쉘 스크립트 (Shell Script)**: 유닉스/리눅스의 쉘 명령어를 조합한 관리용. (Kết hợp lệnh shell Linux/Unix để quản trị.)
- **ASP / JSP**: 서버 측 동적 페이지 생성 언어 (ASP의 마이크로소프트, JSP의 자바 기반). (ASP của MS, JSP của Java.)
- **예시 (Ví dụ)**: 브라우저에서 버튼을 누르면 즉시 알림창이 뜨는 JS 코드는 컴파일 없이 바로 실행됨. (Mã JS hiển thị thông báo khi bấm nút trên trình duyệt chạy ngay mà không cần biên dịch.)
- 💡 **Mẹo ghi nhớ**: JS là Client, còn lại PPP (PHP, JSP, ASP) đa số là Server.

## 284 & 294. 구역성 (Locality / Tính cục bộ)
### TẦNG A – NOTE NÉN (ÔN / ĐI THI)
- **개념 (Khái niệm)**: 프로세스가 실행되는 동안 주기억장치(Main memory)의 특정 영역만을 집중적으로 참조하는 성질. (Tính chất mà quá trình chỉ tham chiếu tập trung vào một số trang nhất định của bộ nhớ chính khi thực thi.)
- **핵심 키워드 (Từ khóa)**: 시간 구역성 (Temporal locality), 공간 구역성 (Spatial locality), 집중 참조 (Concentrated reference).
- **시험 포인트 (Điểm thi)**: 시간 구역성(Loop, Stack)과 공간 구역성(Array)의 구체적인 사례를 구분하는 것. (Phân biệt ví dụ của cục bộ thời gian và cục bộ không gian.)
- **한 문장 설명 (Tóm tắt)**: 스래싱(Thrashing) 방지를 위한 핵심 이론. (Lý thuyết cốt lõi để ngăn chặn hiện tượng Thrashing.)

### TẦNG B – NOTE 보충 (HIỂU SÂU)
- **시간 구역성 (Temporal locality)**: 한 번 참조된 페이지는 가까운 시간 내에 다시 참조될 가능성이 높음. (Trang vừa dùng sẽ có khả năng cao được dùng lại sớm. Ví dụ: Vòng lặp/Loop, Ngăn xếp/Stack, Biến đếm.)
- **공간 구역성 (Spatial locality)**: 특정 페이지가 참조되면 인근 위치의 페이지가 계속 참조될 가능성이 높음. (Trang vừa dùng thì các trang liền kề nó dễ được gọi theo. Ví dụ: Mảng/Array, duyệt tuần tự.)
- **예시 (Ví dụ)**: 배열 `A[0]`부터 `A[100]`까지 순서대로 읽는 것은 공간 구역성이고, `for`문 안에서 변수 `i`를 계속 증가시키며 쓰는 것은 시간 구역성. (Đọc mảng theo thứ tự là cục bộ không gian; dùng biến i nhiều lần trong vòng lặp là cục bộ thời gian.)
- 💡 **Mẹo ghi nhớ**: **T**emporal = **T**ime (Lặp lại nhiều lần/Loop), **S**patial = **S**pace (Gần nhau/Array).

## 285 & 295. 워킹 셋 (Working Set / Tập làm việc)
### TẦNG A – NOTE NÉN (ÔN / ĐI THI)
- **개념 (Khái niệm)**: 프로세스가 원활한 수행을 위해 일정 시간 동안 집중적으로 참조하는 페이지들의 집합. (Tập hợp các trang mà tiến trình tham chiếu tập trung trong một khoảng thời gian để chạy mượt mà.)
- **핵심 키워드 (Từ khóa)**: 데닝 (Denning), Locality 활용 (Ứng dụng Locality), 페이지 부재 감소 (Giảm Page Fault), 동적 변경 (Thay đổi động).
- **시험 포인트 (Điểm thi)**: 자주 참조되는 워킹 셋을 주기억장치에 상주시킴으로써 시스템을 안정화(스래싱 방지)한다는 점. (Giữ Working Set trong bộ nhớ chính giúp hệ thống ổn định và tránh Thrashing.)

### TẦNG B – NOTE 보충 (HIỂU SÂU)
- 데닝(Denning)이 제안한 모델로, 프로그램의 국부성(Locality)을 이용. (Mô hình do Denning đề xuất dựa trên tính cục bộ.)
- 시간에 따라 참조하는 페이지가 달라지므로 지속적으로 (동적으로) 변경됨. (Thay đổi động theo thời gian.)
- **예시 (Ví dụ)**: 당신이 시험 공부를 할 때 지금 당장 책상 위에 꺼내놓은 책과 필기구들이 '워킹 셋'입니다. 과목이 바뀌면 책상 위 물건(워킹 셋)도 바뀝니다. (Những cuốn sách và bút bạn đang để trên bàn học ngay lúc này chính là 'Working Set'. Khi chuyển môn, đồ trên bàn cũng thay đổi.)
- 💡 **Mẹo ghi nhớ**: Working Set = Những món đồ đang "Working" (Đang dùng) phải để sẵn trên bàn (Memory).

## 287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)
### TẦNG A – NOTE NÉN (ÔN / ĐI THI)
- **개념 (Khái niệm)**: 커널(Kernel), 쉘(Shell), 유틸리티(Utility)의 계층적 구조. (Cấu trúc phân tầng gồm Kernel, Shell và Utility.)
- **핵심 키워드 (Từ khóa)**: 커널(Kernel - Hạt nhân), 쉘(Shell - Vỏ), 명령어 해석기 (Trình thông dịch lệnh).
- **시험 포인트 (Điểm thi)**: 커널(핵심 및 상주)과 쉘(명령어 해석기 및 인터페이스)의 역할을 명확히 구분. (Phân biệt vai trò của Kernel và Shell.)

### TẦNG B – NOTE 보충 (HIỂU SÂU)
- **커널 (Kernel)**: 하드웨어를 직접 관리, 프로세스/메모리/파일 관리. 주기억장치에 상주. (Quản lý trực tiếp phần cứng, tiến trình, bộ nhớ. Nằm thường trực trong RAM.)
- **쉘 (Shell)**: 사용자의 명령을 인식하여 수행하는 명령어 해석기 (인터페이스). (Trình biên dịch lệnh, nhận lệnh từ người dùng và gọi chương trình.)
- **유틸리티 (Utility)**: 에디터, 컴파일러 등 응용 프로그램. (Các chương trình ứng dụng như trình soạn thảo, biên dịch.)
- **예시 (Ví dụ)**: 식당에서 사용자가 주문(명령)을 하면 종업원(Shell)이 이를 받아 주방장(Kernel)에게 전달하여 요리(하드웨어 제어)를 하는 구조. (Khách hàng gọi món (Lệnh) -> Phục vụ bàn (Shell) -> Đầu bếp (Kernel) xử lý nấu nướng.)
- 💡 **Mẹo ghi nhớ**: Kernel là **Lõi** (Hardware), Shell là **Vỏ** (Giao tiếp người dùng).

## 292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)
### TẦNG A – NOTE NÉN (ÔN / ĐI THI)
- **개념 (Khái niệm)**: 주기억장치 빈 공간이 없을 때 어떤 페이지를 내보낼지 결정하는 기법. (Kỹ thuật chọn trang để loại bỏ khi bộ nhớ chính đã đầy để nhường chỗ cho trang mới.)
- **핵심 키워드 (Từ khóa)**: OPT, FIFO, LRU, LFU, NUR.
- **시험 포인트 (Điểm thi)**: 각 알고리즘별 교체 대상 선정 기준 묻는 문제. (Tiêu chí chọn trang của từng thuật toán.)

### TẦNG B – NOTE 보충 (HIỂU SÂU)
- **OPT (Optimal)**: 앞으로 가장 오랫동안 안 쓸 페이지 교체 (이론적 최고). (Thay trang sẽ lâu nhất không được dùng trong tương lai - Tốt nhất nhưng chỉ trên lý thuyết.)
- **FIFO (First-In First-Out)**: 들어온 지 가장 오래된 페이지 교체. (Thay trang vào bộ nhớ sớm nhất.)
- **LRU (Least Recently Used)**: 최근에 가장 오랫동안 안 쓴 페이지 교체. (Thay trang lâu nhất chưa được sử dụng tính từ hiện tại.)
- **LFU (Least Frequently Used)**: 참조 횟수가 가장 적은 페이지 교체. (Thay trang có số lần sử dụng ít nhất.)
- **NUR (Not Used Recently)**: 참조 비트와 변형 비트를 사용해 최근 미사용 페이지 교체. (Dùng bit tham chiếu và bit sửa đổi để loại trang không dùng gần đây.)
- **예시 (Ví dụ)**: 스마트폰에서 앱을 여러 개 켜다가 램이 부족해지면, 제일 먼저 켰던 앱(FIFO)을 끄거나 최근에 가장 안 본 앱(LRU)을 종료시킴. (Khi điện thoại đầy RAM, nó sẽ tắt app mở đầu tiên (FIFO) hoặc app lâu rồi chưa đụng tới (LRU).)
- 💡 **Mẹo ghi nhớ**: **R**ecently = Lâu không đụng (Thời gian), **F**requently = Ít dùng (Số lần). 

## 298. PCB (Process Control Block)
### TẦNG A – NOTE NÉN (ÔN / ĐI THI)
- **개념 (Khái niệm)**: 운영체제가 각 프로세스를 관리하기 위해 정보를 저장하는 데이터 구조. (Cấu trúc dữ liệu HĐH dùng để lưu thông tin quản lý từng tiến trình.)
- **핵심 키워드 (Từ khóa)**: 프로세스 상태 (Trạng thái tiến trình), 식별자 (PID), 우선순위 (Priority).
- **시험 포인트 (Điểm thi)**: 프로세스 생성 시 고유하게 생성되며, 종료 시 제거됨. (Được tạo ra duy nhất khi tiến trình bắt đầu và bị xóa khi kết thúc.)

### TẦNG B – NOTE 보충 (HIỂU SÂU)
- 현재 상태(준비/실행/대기), CPU 레지스터 정보, 자원 정보 포함. (Chứa trạng thái hiện tại, thanh ghi CPU, tài nguyên được cấp.)
- 문맥 교환(Context Switching) 시, 현재까지 진행 상황을 PCB에 저장. (Khi chuyển đổi ngữ cảnh, lưu tiến độ vào PCB để sau này chạy tiếp.)
- **예시 (Ví dụ)**: 병원에서 환자(프로세스)마다 차트(PCB)를 만들어 병력과 현재 상태를 기록하는 것과 같음. 퇴원하면 차트를 닫음. (Giống như Bệnh án (PCB) của từng bệnh nhân (Process), ghi lại tình trạng, xuất viện thì đóng hồ sơ.)
- 💡 **Mẹo ghi nhớ**: PCB giống như "Thẻ căn cước + Hồ sơ bệnh án" của một tiến trình.


