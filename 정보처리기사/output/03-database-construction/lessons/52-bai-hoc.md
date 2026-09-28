# 6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

DDL, DML, DCL, 상세

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞의 **220-230. 하위 질의, 트리거, DBMS 접속 및 데이터 전환**에서 만든 기준을 바탕으로 절차와 비교 기준을 확장한다. 읽은 뒤에는 **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)**에서 같은 기준이 어떻게 심화되거나 다른 형태로 적용되는지 확인한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)** và nối nó với **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)

### 6.1 DDL 문법 (Cú pháp DDL)
- `CREATE TABLE`: Tạo bảng. Các ràng buộc: `PRIMARY KEY` (Khóa chính), `FOREIGN KEY` (Khóa ngoại), `UNIQUE` (Duy nhất), `CONSTRAINT` (Điều kiện), `CHECK` (Kiểm tra), `DEFAULT` (Mặc định), `NOT NULL` (Không được rỗng).
- `ALTER TABLE`:
  - `ADD` (Thêm cột): `ALTER TABLE table_name ADD col_name datatype;`
  - `MODIFY` (Sửa kiểu/ràng buộc cột): `ALTER TABLE table_name MODIFY col_name datatype;`
  - `DROP` (Xóa cột): `ALTER TABLE table_name DROP col_name;`
  - `RENAME COLUMN`: Đổi tên cột.
- `DROP TABLE` [CASCADE | RESTRICT]: Xóa bảng. CASCADE (xóa luôn đối tượng phụ thuộc), RESTRICT (không xóa nếu đang bị tham chiếu).
- `TRUNCATE TABLE`: Xóa nhanh toàn bộ dữ liệu, giữ lại cấu trúc, **không thể quay lui (rollback / 롤백)**.

### 6.2 DCL 문법 (Cú pháp DCL)
- `GRANT 권한 ON 테이블 TO 사용자 [WITH GRANT OPTION];` (Cấp quyền. WITH GRANT OPTION: cho phép người đó cấp quyền tiếp cho người khác).
- `REVOKE 권한 ON 테이블 FROM 사용자 [CASCADE CONSTRAINTS];` (Thu hồi quyền. CASCADE: thu hồi luôn quyền mà người này đã cấp cho người khác).

### 6.3 TCL 문법 (Cú pháp TCL)
- `COMMIT`: Lưu vĩnh viễn giao dịch (transaction / 트랜잭션) thành công.
- `ROLLBACK`: Hủy bỏ giao dịch bị lỗi, quay về trạng thái cũ.
- `SAVEPOINT`: Đặt điểm lưu để quay lui (rollback / 롤백) về điểm đó thay vì toàn bộ.

### 6.3 DML 문법 (Cú pháp DML)
- `SELECT [DISTINCT] 속성명 FROM 테이블 WHERE 조건 GROUP BY 속성명 HAVING 조건 ORDER BY 속성명 [ASC|DESC];`
  - `DISTINCT`: Loại bỏ dòng trùng lặp.
  - `GROUP BY`: Nhóm dữ liệu (ROLLUP, CUBE để tính tổng phụ).
  - `HAVING`: Điều kiện cho nhóm (GROUP BY).
- **집계 함수 (Hàm tập hợp):** `COUNT`, `SUM`, `AVG`, `MAX`, `MIN`, `STDDEV` (độ lệch chuẩn), `VARIANCE` (phương sai).
- **순위 함수 (Hàm xếp hạng):** `RANK` (bỏ qua số hạng: 1, 1, 3), `DENSE_RANK` (không bỏ qua: 1, 1, 2), `ROW_NUMBER` (đánh số thứ tự: 1, 2, 3).
- **WHERE 연산자 (Toán tử điều kiện):** `LIKE '%'` (Nhiều ký tự), `LIKE '_'` (1 ký tự), `BETWEEN A AND B`, `IN()`, `IS NULL`.
- `UPDATE 테이블 SET 속성 = 데이터 WHERE 조건;` (Sửa dữ liệu).
- `DELETE FROM 테이블 WHERE 조건;` (Xóa dữ liệu, có thể ROLLBACK).
- `INSERT INTO 테이블 (속성) VALUES (데이터);` (Thêm dữ liệu).

---
