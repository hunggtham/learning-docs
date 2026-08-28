# SQL cơ bản: SELECT, hàm, lọc, nhóm và sắp xếp

> **Nguồn bám sát:** PDF *2024 개정판 SQLD 개념정리*, trang 24–42.
>
> **Cách học:** Đây là nền cho mọi bài tiếp theo: `JOIN` mở rộng `FROM`, subquery mở rộng biểu thức/điều kiện, còn Window Function mở rộng việc tính trên các hàng đã chọn.

## 1. 관계형 데이터베이스 (Relational Database) (cơ sở dữ liệu quan hệ)

> **KR:** 관계형 데이터베이스는 데이터를 테이블로 저장하고 SQL 문장으로 관리한다.

RDB (Relational Database) (cơ sở dữ liệu quan hệ) lưu dữ liệu thành table (Table) (bảng). Một table có column/attribute (Column/Attribute) (cột/thuộc tính) và row/tuple/record (Row/Tuple/Record) (hàng/bản ghi); `PRIMARY KEY` (Primary Key) (khóa chính) nhận diện hàng, còn `FOREIGN KEY` (Foreign Key) (khóa ngoại) liên kết bảng. DBMS (Database Management System) (hệ quản trị CSDL) quản lý dữ liệu, phục hồi hỏng hóc và thực thi SQL.

## 2. SQL 문장의 종류 (DML/DDL/DCL/TCL) (các nhóm câu lệnh SQL)

| 한국어 (English) (Tiếng Việt) | Lệnh chính | Vai trò |
| --- | --- | --- |
| 데이터 조작어 (DML) (thao tác dữ liệu) | `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MERGE` | Đọc/thay đổi hàng. |
| 데이터 정의어 (DDL) (định nghĩa dữ liệu) | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` | Tạo/thay đổi cấu trúc; auto-commit theo PDF. |
| 데이터 제어어 (DCL) (điều khiển dữ liệu) | `GRANT`, `REVOKE` | Cấp/thu hồi quyền. |
| 트랜잭션 제어어 (TCL) (điều khiển giao dịch) | `COMMIT`, `ROLLBACK`, `SAVEPOINT` | Kiểm soát kết quả DML. |

## 3. SELECT 문의 구조 (SELECT statement structure) (cấu trúc câu SELECT)

```sql
SELECT [ALL | DISTINCT] select_expression [AS alias]
FROM table_or_view
WHERE row_condition
GROUP BY grouping_column
HAVING group_condition
ORDER BY sort_expression [ASC | DESC];
```

> **KR:** 작성 순서와 논리적 실행 순서는 다르며, 논리적 순서는 FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY이다.

Ta viết `SELECT` trước nhưng DB logic xử lý từ `FROM` (tạo tập hàng) → `WHERE` (lọc hàng) → `GROUP BY` (nhóm) → `HAVING` (lọc nhóm) → `SELECT` (chọn/biểu diễn cột) → `ORDER BY` (sắp xếp kết quả). Thứ tự này giải thích vì sao alias (Alias) (bí danh) thường dùng được trong `ORDER BY` nhưng không dùng được trong `WHERE`/`HAVING`.

`ALL` (All) (giữ mọi dòng) là mặc định; `DISTINCT` (Distinct) (loại dòng trùng theo danh sách chọn) chỉ để khử trùng kết quả, không thay thế cho thiết kế dữ liệu đúng. Oracle không dùng `AS` cho table alias (bí danh bảng), còn column alias có thể cần dấu `"` nếu chứa khoảng trắng/ký tự đặc biệt.

## 4. WHERE 절 (WHERE clause) (mệnh đề lọc hàng)

> **KR:** WHERE 절은 테이블의 데이터 중 원하는 조건에 맞는 데이터만 조회하기 위해 사용한다.

`WHERE` lọc từng row trước khi tạo nhóm; vì vậy không đặt aggregate function (hàm tổng hợp) trực tiếp ở đây. Dùng `HAVING` cho điều kiện trên kết quả nhóm. Các toán tử quan trọng là `=`, `>`, `>=`, `<`, `<=`, `BETWEEN A AND B`, `IN`, `LIKE`, `IS NULL`, `AND`, `OR`, `NOT`.

```sql
WHERE price BETWEEN 15000 AND 20000       -- gồm cả hai đầu mút
WHERE deptno IN (10, 20, 30)              -- thuộc danh sách
WHERE name LIKE 'S%'                      -- bắt đầu bằng S
WHERE position IS NULL                    -- NULL không so sánh bằng =
```

`LIKE` (Like) (khớp mẫu) dùng `%` cho 0 hoặc nhiều ký tự và `_` cho đúng 1 ký tự. `NULL` (Null) (giá trị chưa biết/không có) với phép so sánh cho kết quả unknown (không xác định), nên không qua được `WHERE`; phải dùng `IS NULL`/`IS NOT NULL`. Ưu tiên toán tử là `()` → `NOT` → so sánh/SQL operator → `AND` → `OR`; dùng ngoặc để ý định không mơ hồ.

## 5. 단일행 함수 (Single-Row Function) (hàm một hàng)

> **KR:** 단일행 함수는 하나의 행 값에 대해 하나의 결과를 반환한다.

Hàm một hàng biến đổi từng hàng độc lập, nên có thể dùng ở `SELECT`, `WHERE`, `ORDER BY` và lồng hàm. Nhóm số học: `ABS`, `SIGN`, `CEIL`, `FLOOR`, `MOD`, `ROUND`, `TRUNCATE`, `POWER`, `SQRT`; nhóm chuỗi Oracle: `LOWER`, `UPPER`, `SUBSTR`, `INSTR`, `LENGTH`, `TRIM`, `LPAD`, `RPAD`, `REPLACE`, `TRANSLATE`; nhóm ngày: `SYSDATE`, `CURRENT_DATE`, `EXTRACT`, `ADD_MONTHS`, `MONTHS_BETWEEN`, `LAST_DAY`, `NEXT_DAY`; nhóm chuyển đổi: `TO_NUMBER`, `TO_CHAR`, `TO_DATE`, `CAST`, `CONVERT`.

> **KR:** DBMS마다 함수명과 날짜 출력 형식은 다를 수 있다.

Ví dụ PDF: SQL Server dùng `GETDATE()` tương ứng `SYSDATE`, `DATEPART` tương ứng `EXTRACT`, `DATEDIFF` tương ứng `MONTHS_BETWEEN` theo đơn vị phù hợp; `SUBSTR`/`LENGTH`/`INSTR` có tên thường gặp là `SUBSTRING`/`LEN`/`CHARINDEX`. Khi đề không chỉ rõ DBMS, hãy chú ý cú pháp đang dùng thay vì áp tên hàm của DBMS khác.

## 6. 집계 함수와 NULL (Aggregate Function and NULL) (hàm tổng hợp và NULL)

> **KR:** 집계 함수는 여러 행을 하나의 결과값으로 반환하며, NULL 값은 0으로 계산되는 것이 아니라 무시된다.

`COUNT(*)` đếm mọi hàng; `COUNT(column)` chỉ đếm hàng có giá trị khác `NULL`; `SUM`, `AVG`, `MIN`, `MAX`, `STDDEV`, `VARIANCE` tổng hợp giá trị không NULL. `AVG(sal)` không phải trung bình của toàn bộ hàng nếu `sal` có NULL; nếu muốn coi NULL là 0, dùng `AVG(NVL(sal, 0))` theo mục tiêu đề bài.

`NVL(a,b)` (Oracle), `ISNULL(a,b)` (SQL Server) thay NULL; `NVL2`, `NULLIF`, `COALESCE` xử lý biến thể; `CASE`/`DECODE` tạo nhánh điều kiện. `CASE` đơn giản so một expression với các value, còn searched `CASE` kiểm tra từng condition.

## 7. GROUP BY và HAVING

> **KR:** GROUP BY는 데이터를 소그룹으로 분류하여 통계 정보를 얻고, HAVING은 그룹화된 결과에 조건을 적용한다.

Sau `GROUP BY`, chỉ được chọn cột nhóm hoặc biểu thức aggregate, vì mỗi nhóm trả về đúng một hàng. `WHERE` giảm số hàng trước nhóm để hiệu năng tốt hơn; `HAVING` giữ/bỏ cả nhóm sau khi aggregate. `GROUP BY` không tự sắp xếp; muốn thứ tự ổn định dùng `ORDER BY`.

```sql
SELECT deptno, COUNT(*) AS employee_count, AVG(sal) AS avg_sal
FROM emp
WHERE deptno IN (10, 20, 30)
GROUP BY deptno
HAVING AVG(sal) > 2500
ORDER BY avg_sal DESC;
```

## 8. ORDER BY (Order By) (sắp xếp)

> **KR:** ORDER BY는 결과 집합의 정렬 기준을 명시하며 기본값은 ASC이다.

`ASC` (Ascending) (tăng dần) là mặc định, `DESC` (Descending) (giảm dần) đảo thứ tự. Khi nhiều cột, cột bên trái là tiêu chí ưu tiên cao hơn; cột sau chỉ phân xử các hàng hòa ở cột trước. Theo PDF, Oracle mặc định xếp `NULL` cuối ở ASC và SQL Server xếp NULL đầu; Oracle cho `NULLS FIRST`/`NULLS LAST` để chỉ định rõ. Sau `GROUP BY`, chỉ dùng trong `ORDER BY` các cột hiện có trong kết quả `SELECT`.
