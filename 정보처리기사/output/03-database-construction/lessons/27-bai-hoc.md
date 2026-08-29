# 204-219. SQL 명령어 심화 (SQL Commands Detail)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **204-219. SQL 명령어 심화 (SQL Commands Detail)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

SQL, 명령어, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 204-219. SQL 명령어 심화 (SQL Commands Detail)
- **DDL (204, 207-209):** , , .
  -  옵션:  (참조하는 모든 개체 연쇄 제거),  (참조 중이면 제거 취소).
- **DML (205, 214-218):** , , , .
  - : 중복 튜플 제거.
  - : 정렬 (오름차순/내림차순).
- **DCL (206, 210-213):** , , , .
  - : 권한 부여. (옵션: 남에게 권한 부여 가능).
  - : 권한 회수.
  - : 변경 내용을 DB에 영구 반영.
  - : 변경 취소, 이전 상태로 복구.
- **VI (Vietnamese) (Tiếng Việt):** Chi tiết các lệnh SQL.
  - : Xóa dây chuyền các phần phụ thuộc. : Không cho xóa nếu đang bị phụ thuộc.
  - : Cấp quyền và cho phép người đó cấp quyền tiếp cho người khác.
  - : Xác nhận lưu thay đổi. : Hoàn tác.
