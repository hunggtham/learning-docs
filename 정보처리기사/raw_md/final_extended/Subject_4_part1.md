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

