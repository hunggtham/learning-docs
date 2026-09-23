# 075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

배열, 조건문, 반복문

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

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
