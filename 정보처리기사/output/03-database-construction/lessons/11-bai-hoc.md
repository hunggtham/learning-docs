# 110-114. 키 (Keys)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **110-114. 키 (Keys)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

110-114. 키 (Keys)

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 110-114. 키 (Keys)
- **후보키 (Candidate Key):** 튜플을 유일하게 식별하는 속성. 유일성과 최소성 만족.
- **기본키 (Primary Key):** 후보키 중 선정된 주키. 중복과 NULL 불가.
- **대체키 (Alternate Key):** 후보키 중 기본키를 제외한 나머지 (보조키).
- **슈퍼키 (Super Key):** 유일성은 만족하지만 최소성은 만족하지 못하는 속성 집합.
- **외래키 (Foreign Key):** 다른 릴레이션의 기본키를 참조하는 속성.
- **VI (Vietnamese) (Tiếng Việt):** Các loại khóa (Keys).
  - Candidate Key (Khóa ứng viên): Định danh duy nhất, thỏa mãn tính duy nhất và tính tối thiểu.
  - Primary Key (Khóa chính): Chọn từ khóa ứng viên, không trùng lặp, không NULL.
  - Alternate Key (Khóa thay thế): Các khóa ứng viên còn lại.
  - Super Key (Siêu khóa): Thỏa mãn tính duy nhất nhưng không tối thiểu.
  - Foreign Key (Khóa ngoại): Thuộc tính tham chiếu đến khóa chính của bảng khác.
