# 143-145. SQL 분류 (SQL Categories)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **143-145. SQL 분류 (SQL Categories)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

SQL, 분류

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **204-219. SQL 명령어 심화 (SQL Commands Detail)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **143-145. SQL 분류 (SQL Categories)** và nối nó với **204-219. SQL 명령어 심화 (SQL Commands Detail)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 143-145. SQL 분류 (SQL Categories)
- **DDL (데이터 정의어):** CREATE, ALTER, DROP (스키마, 테이블 등 정의/변경/삭제).
- **DML (데이터 조작어):** SELECT, INSERT, DELETE, cập nhật (update / 업데이트).
- **DCL (데이터 제어어):** GRANT, REVOKE (권한 제어).
- **TCL (트랜잭션 제어어):** lần ghi nhận (commit / 커밋), quay lui (rollback / 롤백), SAVEPOINT (트랜잭션 제어).
- **VI (Vietnamese) (Tiếng Việt):** Phân loại SQL.
  - DDL (Định nghĩa dữ liệu): CREATE, ALTER, DROP.
  - DML (Thao tác dữ liệu): SELECT, INSERT, DELETE, cập nhật (update / 업데이트).
  - DCL (Điều khiển dữ liệu): GRANT, REVOKE (điều khiển quyền).
  - TCL (Điều khiển giao dịch): lần ghi nhận (commit / 커밋), quay lui (rollback / 롤백), SAVEPOINT (điều khiển giao dịch).
