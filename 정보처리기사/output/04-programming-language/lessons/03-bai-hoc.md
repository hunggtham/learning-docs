# 072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

데이터, 타입, 변수, 연산자

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)**에서 만든 기준을 이어받아 **072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)

Từ **프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)**, ta đã có điểm tựa để bước vào **072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 3/77 trước khi đi vào chi tiết.

Để đọc **072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô. Trong khối này, **데이터 타입 (Data Types)**, **변수 작성 규칙 (Variable Naming Rules)**, **연산자 (Operators)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

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

Điểm chốt của **072 - 073. 데이터 타입, 변수 및 연산자 (Data Types, Variables & Operators)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.