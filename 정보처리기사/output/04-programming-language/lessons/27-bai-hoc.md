# 264 - 274. 파이썬 문법 (Python Syntax & Basics)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **264 - 274. 파이썬 문법 (Python Syntax & Basics)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

파이썬, 문법

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

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
