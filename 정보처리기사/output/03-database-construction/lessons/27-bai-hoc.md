# 204-219. SQL 명령어 심화 (SQL Commands Detail)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **204-219. SQL 명령어 심화 (SQL Commands Detail)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

SQL, 명령어, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **143-145. SQL 분류 (SQL Categories)**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **204-219. SQL 명령어 심화 (SQL Commands Detail)** và nối nó với **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 204-219. SQL 명령어 심화 (SQL Commands Detail)
- **DDL (204, 207-209):** `CREATE`, `ALTER`, `DROP`, `TRUNCATE`.
  - `CASCADE`: 참조하는 모든 개체를 연쇄 처리; `RESTRICT`: 참조 중이면 처리 취소.
- **DML (205, 214-218):** `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
  - `DISTINCT`: 중복 튜플 제거; `ORDER BY`: 오름차순/내림차순 정렬.
- **DCL (206, 210-213):** `GRANT`, `REVOKE`.
  - `GRANT`: 권한 부여 (`WITH GRANT OPTION`으로 재부여 허용).
  - `REVOKE`: 권한 회수.
- **TCL:** `COMMIT`, `ROLLBACK`, `SAVEPOINT`.
  - `COMMIT`: 변경 내용을 DB에 영구 반영; `ROLLBACK`: 변경 취소; `SAVEPOINT`: 부분 복귀 지점 설정.
- **VI (Vietnamese) (Tiếng Việt):** Chi tiết các lệnh SQL.
  - `CASCADE`: Xử lý dây chuyền các đối tượng phụ thuộc. `RESTRICT`: Không xử lý nếu đang bị tham chiếu.
  - `GRANT`/`REVOKE`: Cấp và thu hồi quyền.
  - `COMMIT`/`ROLLBACK`/`SAVEPOINT`: Xác nhận, hoàn tác hoặc đánh dấu điểm khôi phục giao dịch.
