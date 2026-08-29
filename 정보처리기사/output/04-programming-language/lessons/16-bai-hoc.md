# 246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

입출력, 함수와, 포맷

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

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
