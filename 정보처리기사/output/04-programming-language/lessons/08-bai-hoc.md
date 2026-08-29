# 연산자 (Operators)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **연산자 (Operators)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

연산자

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

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
