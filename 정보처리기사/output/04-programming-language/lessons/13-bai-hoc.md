# 입출력 (Input/Output)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **입출력 (Input/Output)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

입출력

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

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
