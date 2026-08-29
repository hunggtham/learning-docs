# 254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

반복문과, 제어, 키워드

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

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
