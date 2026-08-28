# DML và toán tử

> **Nguồn bám sát:** PDF *2024 개정판 SQLD 개념정리*, trang 85–86.
>
> **Liên kết bài trước:** Sau khi đã học `SELECT`, `JOIN`, subquery và các hàm nhóm, bài này giải thích cách thay đổi dữ liệu thật sự trong bảng. Vì vậy, mọi lệnh thay đổi cần được hiểu cùng với `COMMIT` và `ROLLBACK` ở bài kế tiếp.

## 1. DML (Data Manipulation Language) (Ngôn ngữ thao tác dữ liệu)

> **KR:** DML은 만들어진 테이블에 관리하고자 하는 자료를 입력, 수정, 삭제, 조회하는 명령어이다.

DML là nhóm lệnh dùng để nhập, sửa, xóa và truy vấn dữ liệu trong bảng đã được tạo. Các lệnh cốt lõi là `INSERT` (nhập dữ liệu), `UPDATE` (cập nhật dữ liệu), `DELETE` (xóa dữ liệu) và `SELECT` (truy vấn dữ liệu); `MERGE` (hợp nhất dữ liệu) là lệnh bổ sung. Khác với DDL, kết quả của DML gắn với transaction (giao dịch), nên trong Oracle cần chủ động `COMMIT` (xác nhận lưu) hoặc `ROLLBACK` (hoàn tác) khi cần.

## 2. INSERT (Insert) (chèn dữ liệu)

> **KR:** INSERT는 테이블에 행 데이터를 삽입하는 명령어이다.

`INSERT` thêm một hàng mới vào bảng. Khi chỉ chỉ định một số cột, giá trị phải đi đúng thứ tự các cột đã liệt kê; các cột không liệt kê nhận `NULL` hoặc `DEFAULT` (giá trị mặc định) nếu đã được khai báo. Vì vậy, việc ghi tên cột là cách an toàn hơn: nó tránh phụ thuộc vào thứ tự cột vật lý và làm rõ ý nghĩa từng giá trị.

```sql
-- Chèn vào các cột được chọn
INSERT INTO table_name (column1, column2, column5)
VALUES (value1, value2, value5);

-- Chèn vào toàn bộ cột theo đúng thứ tự định nghĩa bảng
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
```

> **KR:** ORACLE은 한 번에 한 행만 입력 가능하고, SQL Server는 여러 행 동시 삽입이 가능하다.

Trong cú pháp được PDF nhấn mạnh, Oracle chèn một hàng cho mỗi mệnh đề `VALUES`; SQL Server có thể viết nhiều nhóm giá trị trong một câu lệnh. Dù dùng hệ quản trị nào, mỗi giá trị phải phù hợp kiểu dữ liệu và kích thước của cột. Nếu bỏ qua một cột có `NOT NULL` (Not Null) (không cho phép rỗng) mà không có giá trị mặc định hợp lệ, câu lệnh lỗi. Trong Oracle, chuỗi rỗng `''` được xử lý như `NULL`; vì thế khi truy vấn cần kiểm tra bằng `IS NULL`, không phải `= ''`.

## 3. UPDATE (Update) (cập nhật dữ liệu)

> **KR:** UPDATE는 데이터를 수정하며 컬럼 단위로 수행하고 다중 컬럼 수정이 가능하다.

`UPDATE` thay đổi giá trị của một hay nhiều cột ở các hàng thỏa điều kiện. `SET` (Set) (gán giá trị mới) xác định cột và giá trị cần sửa; `WHERE` (Where) (điều kiện lọc hàng) xác định phạm vi bị ảnh hưởng. Nếu không có `WHERE`, toàn bộ hàng trong bảng bị cập nhật — đây là bẫy SQLD rất quan trọng.

```sql
UPDATE table_name
SET column1 = value1,
    column2 = value2
WHERE condition;
```

`UPDATE` có thể nhận kết quả subquery (truy vấn con). Khi gán nhiều cột bằng một subquery, số cột bên trái phải khớp số giá trị mà subquery trả về cho từng hàng đích; nếu không, không thể xác định phép gán một-một.

```sql
UPDATE emp
SET (sal, comm) = (
  SELECT AVG(sal), AVG(comm)
  FROM emp
)
WHERE ename = 'John';
```

## 4. DELETE (Delete) (xóa hàng dữ liệu)

> **KR:** DELETE는 데이터 삭제를 수행하며 행 단위로 실행된다.

`DELETE` xóa các hàng dữ liệu, nhưng không xóa cấu trúc bảng. `FROM` là tùy chọn trong cú pháp PDF. Không có `WHERE` nghĩa là xóa tất cả hàng; tuy nhiên, vì đây là DML, dữ liệu vẫn có thể được `ROLLBACK` trước khi `COMMIT`.

```sql
DELETE FROM table_name
WHERE condition;
```

## 5. MERGE (Merge) (hợp nhất/đồng bộ dữ liệu)

> **KR:** MERGE는 참조 테이블의 데이터를 기준으로 다른 테이블을 수정하고, UPDATE와 DELETE, INSERT를 한 번의 작업으로 수행할 수 있다.

`MERGE` đồng bộ bảng đích với bảng nguồn theo điều kiện nối `ON`. Hàng đã khớp (`WHEN MATCHED`) được cập nhật hoặc có thể xóa theo điều kiện; hàng chưa khớp (`WHEN NOT MATCHED`) được chèn. Bản chất của nó là “nếu có thì sửa, nếu chưa có thì thêm”, nên phù hợp dữ liệu staging (bảng trung gian) hoặc đồng bộ dữ liệu thành viên.

```sql
MERGE INTO team t
USING member m
ON (t.member_id = m.member_id)
WHEN MATCHED THEN
  UPDATE SET t.name = m.name, t.email = m.email
WHEN NOT MATCHED THEN
  INSERT (team_id, name, email)
  VALUES (m.member_id, m.name, m.email);
```

## 6. SELECT (Select) (truy vấn dữ liệu)

> **KR:** SELECT는 테이블에서 필요한 컬럼을 조회하는 명령어이다.

```sql
SELECT [ALL | DISTINCT] column_name
FROM table_name;
```

`ALL` (All) (giữ mọi dòng) là mặc định; `DISTINCT` (Distinct) (loại dòng trùng theo toàn bộ danh sách chọn) chỉ giữ kết quả khác nhau. Phần JOIN, GROUP BY, subquery, Window Function và Hierarchical Query trong các bài trước đều là những cách mở rộng của câu `SELECT` này.

## 7. 산술 연산자 (Arithmetic operator) (toán tử số học)

> **KR:** 산술 연산자는 NUMBER와 DATE 자료형에 적용되고, 수학에서와 같이 괄호, 곱셈, 나눗셈, 덧셈, 뺄셈의 우선순위를 가진다.

Toán tử số học áp dụng cho `NUMBER` (Number) (kiểu số) và `DATE` (Date) (kiểu ngày). Thứ tự ưu tiên là `()` → `*`, `/` → `+`, `-`; hãy dùng ngoặc khi ý định tính toán cần rõ ràng. Với ngày tháng, phép cộng/trừ thường biểu thị cộng/trừ số ngày theo cách xử lý của DBMS.

## 8. 합성 연산자 (Concatenation operator) (toán tử nối chuỗi)

> **KR:** 합성 연산자는 컬럼과 문자 또는 다른 컬럼을 연결시켜 문자 표현식의 결과로 새 컬럼을 생성한다.

Toán tử nối tạo một biểu thức văn bản mới từ cột và chuỗi, hoặc từ nhiều cột. Oracle dùng `||`, SQL Server thường dùng `+`, còn `CONCAT` là hàm nối chuỗi. Không nhầm `+` của SQL Server với phép cộng số: kiểu dữ liệu của biểu thức quyết định ý nghĩa.

```sql
-- Oracle
SELECT first_name || ' ' || last_name AS full_name
FROM employees;

-- SQL Server
SELECT first_name + ' ' + last_name AS full_name
FROM employees;

-- Hàm nối chuỗi
SELECT CONCAT('Hello, ', 'World!') AS greeting;
```

Ví dụ `PLAYER_NAME + '선수, ' + HEIGHT + 'cm, ' + WEIGHT + 'kg'` tạo câu mô tả một cầu thủ. Đây là một biểu thức trong `SELECT`, nên không làm thay đổi dữ liệu gốc; muốn lưu kết quả vào bảng phải dùng DML như `INSERT` hoặc `UPDATE` một cách có chủ đích.
