# 프로그래밍 언어 기초 (Programming Language Basics)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **프로그래밍 언어 기초 (Programming Language Basics)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

프로그래밍, 언어, 기초

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

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
