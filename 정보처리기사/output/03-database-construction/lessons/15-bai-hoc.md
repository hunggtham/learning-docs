# 115. 무결성 (Integrity)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **115. 무결성 (Integrity)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

무결성

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 115. 무결성 (Integrity)
- **개체 무결성 (Entity Integrity):** 기본키는 NULL값이나 중복값을 가질 수 없다.
- **참조 무결성 (Referential Integrity):** 외래키 값은 NULL이거나 참조 릴레이션의 기본키 값과 동일해야 한다.
- **VI (Vietnamese) (Tiếng Việt):** Tính toàn vẹn.
  - Toàn vẹn thực thể: Khóa chính không NULL và không trùng.
  - Toàn vẹn tham chiếu: Khóa ngoại phải là NULL hoặc khớp với khóa chính được tham chiếu.
