# Môn 4 — 프로그래밍 언어 활용 (Programming Language Application) (Ứng dụng ngôn ngữ lập trình)

## 학습 목표 (Mục tiêu học tập)

- 시험에서 사용하는 한국어 용어를 영어와 베트남어 뜻까지 함께 인식한다.
- 각 개념을 정의 → 구성요소/절차 → 비교 포인트 → 예시 순서로 설명할 수 있다.
- 앞에서 배운 개념과 뒤의 심화 개념을 연결하여 문제의 조건을 빠르게 해석한다.

## 권장 학습 순서 (Lộ trình đề xuất)

1. 먼저 이 문서의 각 `##` 단원을 순서대로 읽는다.
2. 단원마다 **핵심 키워드**를 소리 내어 읽고, 한국어 원문과 베트남어 설명을 함께 확인한다.
3. 마지막에 `복습 체크리스트`를 점검한 뒤, 세부 lesson 파일에서 헷갈리는 부분을 다시 본다.

> **Nguồn:** tổng hợp từ các Markdown đã generate trong `raw_md/final`, được đối chiếu với các nguồn `raw` và `raw_md` cùng môn. Nội dung gốc được giữ lại; chỉ chuẩn hoá cấu trúc bài học.

> **Quy ước đọc:** thuật ngữ được ưu tiên theo mẫu `한국어 (English) (Tiếng Việt)`. Mỗi ý tiếng Hàn có phần giải thích Việt ngữ liền kề hoặc ngay sau đó; khi gặp từ kỹ thuật trong ngoặc, hãy xem đó là nghĩa cần nhớ khi làm đề.

> **Cách học:** học theo thứ tự các mục; với mỗi mục, xác định khái niệm → cơ chế/quy tắc → ví dụ → mẹo nhớ. Các mục lặp lại ở phần “심화” (nâng cao) dùng để nối kiến thức trước đó với dạng câu hỏi sâu hơn.

---

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

---

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

---

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

---

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

---

## 239 - 243. 연산자 (Operators)
- **산술 연산자**: 사칙연산, `%`(나머지), `++`/`--`(증감).
  - 전치(`++a`): 먼저 증가시키고 연산. 후치(`a++`): 연산 후 증가시킴.
- **관계 연산자**: `==`(같다), `!=`(다르다), `>`, `<`. C언어에서는 0 이외의 값을 참(True)으로 간주.
- **비트 연산자**: 비트 단위 연산. `&`(AND), `|`(OR), `^`(XOR: 서로 다를 때만 1), `~`(NOT). `<<`, `>>`(비트 이동).
- **논리 연산자**: `&&`(AND), `||`(OR), `!`(NOT).
- **대입 연산자**: `=`, `+=`, `-=` 등. `a += 1`은 `a = a + 1`과 동일.

---

---

## 244. 조건(삼항) 연산자 (Ternary Operator)
- 조건의 참/거짓에 따라 서로 다른 값을 반환.
- 형식: `조건 ? 참일때_값 : 거짓일때_값;`
- (예: `int max = (a > b) ? a : b;`)

**Giải thích (Vietnamese):**
Toán tử 3 ngôi giúp viết tắt câu lệnh if-else trên 1 dòng. Trả về giá trị 1 nếu điều kiện đúng, giá trị 2 nếu sai.

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

## 258 - 261. 배열과 문자열 (Arrays & Strings)
- **배열 (Array)**: **동일한 자료형**의 변수들을 연속된 메모리에 모아둔 것. `인덱스(첨자)`는 0부터 시작. 배열 이름 자체가 **첫 번째 요소의 시작 주소**를 의미.
- **2차원 배열**: 행과 열의 평면 구조 (예: `a[3][4]`는 3행 4열로 총 12개).
- **배열 초기화**: 선언과 동시에 값을 넣는 것. 크기를 생략해도 값의 개수만큼 자동 결정됨. 초기화되지 않은 빈칸은 자동으로 `0`으로 채워짐.
- **배열 형태의 문자열 (C언어)**: C언어는 문자열 자료형이 없어 `char` 배열을 사용. 문자열 끝에는 반드시 **널 문자(`\0`)**가 포함되어야 함 (글자수 + 1바이트 크기 필요).

**Giải thích (Vietnamese):**
Trong C, chuỗi "love" sẽ chiếm 5 ô nhớ (l, o, v, e, `\0`). Ký tự `\0` (Null) báo hiệu cho máy tính biết "đây là kết thúc của chuỗi".

---

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

---

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

---

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

---

## 236. Python의 시퀀스 자료형 (Sequence Data Types in Python)
- 여러 값이 연속적으로 이어진 데이터 구조.
- **리스트(List)**: `[]` 사용. 데이터의 추가/삭제/변경이 자유로움 (Mutable).
- **튜플(Tuple)**: `()` 사용. 한 번 생성하면 데이터의 변경(수정/삭제)이 **불가능함** (Immutable). 읽기 전용에 적합.
- **range**: 반복문에서 연속된 숫자를 생성할 때 사용.

**Giải thích (Vietnamese):**
List và Tuple đều dùng để lưu danh sách. Nhưng List có thể sửa được, còn Tuple thì "Bất di bất dịch" (không thể thêm/xoá/sửa sau khi tạo).

---

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

---

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

---

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

---

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

---

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

---

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

---

## 282. 운영체제의 정의 및 목적 (Definition & Purpose of OS)
- **운영체제(OS)**: 컴퓨터 자원(CPU, 메모리 등)을 효율적으로 관리하고 사용자에게 편리한 환경을 제공하는 소프트웨어 (Windows, Linux 등).
- 목적: 자원 관리, 편리한 인터페이스 제공, 가용성 극대화, 신뢰도 향상.

---

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

---

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

---

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

---

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

---

---

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

---

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

---

## 252. 다중 if문 (Multiple if Statement)
- 처리할 조건이 여러 개일 때 `else if`를 사용해 순차적으로 판단.
- 위에서 조건이 참이면 해당 블록을 실행하고 빠져나옴 (아래 조건은 검사하지 않음).
- 모든 조건이 거짓일 때 마지막 `else`가 실행됨.

---

---

## 305 - 308. IP 주소 체계 (IPv4 vs IPv6)
- **IPv4**: 32비트 (8비트씩 4부분). 클래스 A~E로 나뉨.
- **IPv6**: 128비트 (16비트씩 8부분). 콜론(`:`)으로 구분, 16진수 사용. 
- **IPv6의 특징**: 무한대에 가까운 주소, 보안 강화, 패킷 크기 확장, PnP(자동 설정).
- **IPv6 전송 방식**: 유니캐스트(1:1), 멀티캐스트(1:N), 애니캐스트(가장 가까운 1:1).

**💡 Mẹo ghi nhớ (Mnemonics):**
IPv6 전송 방식 3총사: **유멀애** (Unicast, Multicast, Anycast). *Broadcast는 IPv4에만 있음!*

---

---

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

---

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

---

## 070. 서버개발 프레임워크 (Server Development Framework)
- **모듈화 (Modularity)**: 캡슐화로 영향 최소화, 유지보수 용이.
- **재사용성 (Reusability)**: 반복 모듈 제공으로 생산성/품질 향상.
- **확장성 (Extensibility)**: 다형성 통한 인터페이스 확장.
- **제어 반전 (Inversion of Control, IoC)**: 프레임워크가 흐름을 제어하고 사용자(외부) 코드를 호출.

**Giải thích (Vietnamese):**
Framework (như Spring, Django) là một bộ khung có sẵn. Tính năng đặc biệt nhất của Framework là IoC (Đảo ngược quyền điều khiển): Thay vì bạn tự gọi thư viện (Library), thì Framework sẽ là người gọi code của bạn!

---

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

---

## 교착상태 필요충분조건 1 - 상호배제 (Deadlock Conditions - Mutual Exclusion)
- **교착상태(Deadlock)**: 두 프로세스가 서로의 자원을 기다리며 멈춰버린 현상.
- **상호배제 알고리즘 (Mutual Exclusion)**: 한 번에 하나의 프로세스만 자원을 쓰게 함.
  - Dekker: 두 프로세스 간 Flag와 Turn 변수 사용.
  - Peterson: 두 프로세스 간 상대방에게 양보.
  - Lamport: 고유 번호(티켓) 부여, 번호순 진입.
  - Semaphore: 정수 변수(P연산, V연산)를 이용해 접근 통제.

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

---

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

---

## 234. C언어의 구조체 (struct in C)
- 서로 다른 데이터 유형을 가진 변수들을 하나로 묶어 관리하는 사용자 정의 자료형.
- 배열(Array)은 **동일한 자료형**만 모으지만, 구조체(Struct)는 **상이한 자료형**을 모을 수 있음.

**Giải thích (Vietnamese):**
Struct (Cấu trúc) dùng để gom nhóm nhiều biến khác kiểu lại với nhau. Ví dụ tạo kiểu `SinhVien` gồm tên (chuỗi) và tuổi (số). Trong khi Mảng (Array) chỉ được lưu cùng một kiểu (hoặc toàn chuỗi, hoặc toàn số).

---

---

## 238. 가비지 콜렉터 (Garbage Collector)
- 더 이상 사용되지 않고 메모리를 점유하고 있는 변수/객체를 시스템이 **자동으로 해제**하여 자원을 회수하는 모듈.
- 메모리 누수(Memory Leak)를 방지. JAVA 등에서 사용됨.

**Giải thích (Vietnamese):**
"Người dọn rác" tự động. Bạn cứ việc tạo biến dùng, khi không dùng nữa, hệ thống sẽ tự động xoá nó khỏi RAM để giải phóng bộ nhớ. Trong C/C++ bạn phải tự dọn dẹp, nhưng Java/Python có tính năng này.

---

---

## 250. JAVA에서의 표준 출력 (Standard Output in JAVA)
- `System.out.print()`: 형식 없이 그대로 출력 (줄바꿈 없음).
- `System.out.println()`: 출력 후 자동으로 줄바꿈(Enter) 수행.
- `System.out.printf()`: C언어처럼 서식 문자열(`%d` 등)을 사용하여 출력.
- 문자열과 변수를 섞어 쓸 때 `+` 연산자로 연결 가능.

---

---

## 251. 단순 if문 (Simple if Statement)
- 조건의 참/거짓에 따라 실행할 문장 결정.
- 문장이 두 개 이상이면 반드시 중괄호 `{ }`로 묶어야 함.
- C언어에서는 조건식 결과가 0이면 거짓(False), **0 이외의 모든 값은 참(True)**으로 간주.

---

---

## 253. switch문 (switch Statement)
- 변수의 값에 따라 일치하는 `case` 문장을 실행하는 다분기 제어문.

---

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

---

## 275 - 278. 프로그래밍 언어의 종류 (Types of Programming Languages)
- **절차적 언어**: 실행 순서 중시. 
  - `COBOL` (사무용), `FORTRAN` (과학 기술 계산용), `C` (시스템 프로그래밍), `ALGOL`.
- **객체지향 언어**: 데이터+기능 캡슐화. 재사용성 높음.
  - `JAVA` (플랫폼 독립성, JVM), `C++` (C의 객체지향 확장), `Smalltalk` (최초 GUI, 순수 객체지향).
- **선언형 언어**: '무엇(What)'을 할지 기술 (함수형/논리형).
  - `LISP` (연결리스트, AI용), `PROLOG` (논리 추론, AI용), `Haskell` (순수 함수형), `XML` (구조화 문서).

---

---

## 281. 매시업과 SOA (SW Related Terms: Mashup & SOA)
- **매시업 (Mashup)**: 웹 서비스나 콘텐츠를 조합하여 **새로운 서비스를 만드는 기술** (예: 구글 지도 + 부동산 정보).
- **SOA (Service Oriented Architecture, 서비스 지향 아키텍처)**: 시스템을 **공유/재사용 가능한 서비스 단위**로 구축하는 구조. (계층: 표현, 업무 프로세스, 서비스 중간, 애플리케이션, 데이터 저장).

**Giải thích (Vietnamese):**
- Mashup: Lấy dữ liệu bản đồ của Google kết hợp với dữ liệu danh sách quán ăn để tạo ra app "Tìm quán ăn gần đây". (Trộn lẫn dữ liệu có sẵn để làm ra cái mới).

---

---

## 226 - 227. 데이터베이스 접속 기술 (Database Connectivity)
- **JDBC (Java DataBase Connectivity)**: **자바(Java)** 프로그램 내에서 데이터베이스(DBMS)에 접속하여 SQL 문을 실행하기 위한 표준 API. 운영체제에 독립적.
- **ODBC (Open DataBase Connectivity)**: 프로그래밍 **언어에 관계없이** (C, C++, VB 등) 다양한 DBMS에 접근할 수 있게 마이크로소프트가 만든 개방형 표준 API.

**Giải thích (Vietnamese):**
- JDBC: Dành riêng cho ngôn ngữ Java.
- ODBC: Mở (Open) cho mọi ngôn ngữ khác, dùng chung thông qua một "người quản lý tài xế" (Driver Manager) để dịch lệnh SQL gửi xuống Database.

---

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

---

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

---

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

---

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

---

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

---

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
