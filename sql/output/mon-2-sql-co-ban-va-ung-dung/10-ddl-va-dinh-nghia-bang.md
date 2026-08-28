# DDL và định nghĩa bảng

> **Nguồn bám sát:** PDF *2024 개정판 SQLD 개념정리*, trang 90–94.
>
> **Liên kết bài trước:** DML thay đổi các hàng; DDL định nghĩa hoặc thay đổi cấu trúc chứa các hàng đó. Vì thế DDL được xử lý auto-commit và không rollback như DML chưa commit.

## 1. DDL (Data Definition Language) (ngôn ngữ định nghĩa dữ liệu)

> **KR:** DDL은 데이터의 구조를 정의하는 언어로 객체 생성, 삭제, 변경에 사용하며 AUTO COMMIT이라 ROLLBACK이 불가하다.

DDL định nghĩa cấu trúc dữ liệu và các object (Object) (đối tượng CSDL) như schema (Schema) (lược đồ), domain (Domain) (miền giá trị), table (Table) (bảng), view (View) (khung nhìn) và index (Index) (chỉ mục). Các lệnh chính là `CREATE` (Create) (tạo), `ALTER` (Alter) (thay đổi), `TRUNCATE` (Truncate) (xóa toàn bộ hàng, giữ cấu trúc) và `DROP` (Drop) (xóa đối tượng). Tuy `TRUNCATE` xóa dữ liệu, nó là DDL vì auto-commit.

## 2. 데이터 유형 (Data type) (kiểu dữ liệu)

> **KR:** CHAR은 고정 길이 문자형이고, VARCHAR2/VARCHAR는 가변 길이 문자형이다.

`CHAR(n)` (Character) (chuỗi độ dài cố định) chiếm đủ `n` ký tự; nếu giá trị ngắn hơn, phần còn thiếu được đệm khoảng trắng. `VARCHAR2(n)`/`VARCHAR(n)` (Variable Character) (chuỗi độ dài biến đổi) chỉ dùng dung lượng cần thiết, tối đa `n`. Điều này giải thích vì sao so sánh chuỗi của `CHAR` và `VARCHAR` có thể khác do khoảng trắng đệm.

> **KR:** NUMBER(p, s), NUMERIC(p, s)는 정수와 실수 등의 숫자 정보이고 DATE, DATETIME은 날짜와 시각 정보이다.

`NUMBER(p, s)`/`NUMERIC(p, s)` (Number/Numeric) (kiểu số) có `p` là tổng số chữ số và `s` là số chữ số phần thập phân: `NUMBER(6,2)` cho phép `1234.56` nhưng không `12345.67`. `DATE`/`DATETIME` (Date/Datetime) (ngày/giờ) lưu thông tin thời gian. Chọn kiểu dữ liệu đúng là nền tảng để constraint (Constraint) (ràng buộc) và so sánh/nhóm trong các bài SQL hoạt động đúng.

## 3. CREATE TABLE (Create Table) (tạo bảng)

```sql
CREATE TABLE [owner.]table_name (
  column1 data_type [DEFAULT default_value] [constraint],
  column2 data_type [DEFAULT default_value] [constraint]
);
```

> **KR:** CREATE는 테이블, 인덱스 등의 객체를 생성하는 명령어이며 숫자 컬럼만 사이즈 생략이 가능하다.

`CREATE TABLE` tạo bảng với tên bảng, cột, kiểu dữ liệu, giá trị `DEFAULT` (Default) (mặc định) và constraint tùy chọn. Theo PDF, tên owner có thể bỏ qua khi tạo trong schema của tài khoản hiện tại; kiểu số có thể bỏ kích thước còn kiểu ngày không khai báo kích thước. Tên bảng/tên cột không phân biệt hoa thường nếu không dùng quy tắc đặc biệt; mặc định DB biểu diễn tên không trích dẫn bằng chữ hoa.

### Quy tắc đặt tên cần nhớ

> **KR:** 테이블명은 적절한 단수형 이름을 사용하고, 테이블과 컬럼명은 반드시 문자로 시작하며 A-Z, a-z, 0-9, _, $, #만 허용된다.

Tên bảng nên có ý nghĩa, thường dùng dạng số ít; không trùng tên bảng khác, và tên cột không được trùng trong cùng bảng. Tên phải bắt đầu bằng chữ cái, không dùng reserved word (Reserved word) (từ khóa dành riêng), và chỉ dùng ký tự được PDF liệt kê: `A-Z`, `a-z`, `0-9`, `_`, `$`, `#`. Các cột được ngăn bằng dấu phẩy và câu lệnh kết thúc bằng `;`.

## 4. CTAS (Create Table As Select) (tạo bảng từ kết quả truy vấn)

> **KR:** CTAS는 이미 만들어진 테이블을 활용해서 테이블을 재생성하며, 구조뿐 아니라 데이터도 복제할 수 있다.

```sql
-- Oracle
CREATE TABLE test AS
SELECT * FROM book;

-- SQL Server
SELECT * INTO test
FROM book;
```

CTAS sao chép cột, kiểu dữ liệu, dữ liệu và `NULL` property (thuộc tính cho phép rỗng) của kết quả `SELECT`; alias (Alias) (bí danh) trong SELECT trở thành tên cột mới. Có thể đổi tên cột trong `CREATE TABLE`. `WHERE 1 = 2` tạo cấu trúc mà không lấy hàng nào. Tuy nhiên, PDF nhấn mạnh PK, FK, UNIQUE, CHECK và các constraint khác không được sao chép; chỉ `NOT NULL` được kế thừa. Đây là lý do một bảng CTAS không tự động có đầy đủ tính toàn vẹn như bảng gốc.

```sql
CREATE TABLE test (book_id, book_name) AS
SELECT id, name
FROM book;

-- Chỉ sao chép cấu trúc
CREATE TABLE test AS
SELECT * FROM book WHERE 1 = 2;
```

Để xem cấu trúc: Oracle dùng `DESCRIBE employees` hoặc `DESC employees`; SQL Server dùng `exec sp_help 'dbo.employees'`.

## 5. ALTER TABLE (Alter Table) (thay đổi cấu trúc bảng)

> **KR:** ALTER는 테이블의 구조 변경에 사용하며 컬럼 순서 변경은 불가능하다.

`ALTER TABLE` thêm, sửa, đổi tên hoặc xóa cột/ràng buộc. Cột mới luôn được thêm cuối bảng, không chỉ định vị trí. Đây là khác biệt quan trọng giữa thay đổi schema và thay đổi nội dung bảng: `ALTER` đổi definition (định nghĩa), không sửa từng hàng như `UPDATE`.

```sql
ALTER TABLE table_name ADD column_name data_type [DEFAULT value] [constraint];
ALTER TABLE table_name MODIFY column_name data_type;
ALTER TABLE table_name RENAME COLUMN old_name TO new_name;
ALTER TABLE table_name DROP COLUMN column_name;
ALTER TABLE table_name DROP CONSTRAINT constraint_name;
ALTER TABLE table_name ADD CONSTRAINT constraint_name constraint_definition;
```

### Thêm/sửa cột

> **KR:** 여러 컬럼 동시 추가는 가능하지만 반드시 괄호를 사용한다.

Oracle cho phép thêm nhiều cột bằng ngoặc; cột thêm mới có thể có `DEFAULT` và constraint. Nếu bảng đã có dữ liệu, thêm cột `NOT NULL` không có default là không thể vì các hàng cũ sẽ nhận `NULL`; thêm default hợp lệ thì có thể. Oracle có thể `MODIFY` nhiều cột; theo PDF SQL Server sửa một cột cho mỗi lệnh `ALTER COLUMN`.

```sql
ALTER TABLE player ADD (birthday DATE, address VARCHAR2(80));
ALTER TABLE player ADD stadium VARCHAR2(25)
  DEFAULT '전주월드컵경기장' NOT NULL;
```

### Các bẫy khi thay đổi thuộc tính

> **KR:** 컬럼 사이즈 증가는 항상 가능하고, 축소는 데이터 존재 여부에 따라 제한된다.

Tăng kích thước cột luôn được phép; giảm kích thước chỉ được khi dữ liệu hiện có vẫn phù hợp. Đổi kiểu dữ liệu thường chỉ an toàn khi cột rỗng hoặc mọi giá trị là `NULL`; PDF lưu ý `CHAR` và `VARCHAR` có thể đổi qua lại dù đã có dữ liệu. Đổi `DEFAULT` chỉ ảnh hưởng những hàng được chèn sau khi đổi, không sửa dữ liệu đã tồn tại; gán `NULL` là lưu NULL chứ không tự thay bằng default.

### Đổi tên và xóa

> **KR:** 컬럼 이름 변경은 항상 가능하지만 동시에 여러 컬럼 이름 변경은 불가능하다.

Oracle dùng `RENAME COLUMN`, SQL Server dùng `sp_rename`; đổi tên bảng cũng có cú pháp riêng. Xóa cột chỉ xóa một cột một lần, không phụ thuộc dữ liệu có hay không và không khôi phục được; bảng phải còn ít nhất một cột.

```sql
ALTER TABLE emp RENAME COLUMN ename TO first_name;
RENAME season1 TO season2;
ALTER TABLE player DROP COLUMN address;
```

## 6. DROP và TRUNCATE

> **KR:** DROP TABLE은 테이블의 모든 데이터 및 구조를 삭제하고, TRUNCATE는 테이블 구조를 남기고 전체 데이터를 삭제한다.

`DROP TABLE` xóa cả cấu trúc lẫn dữ liệu; nếu có FK tham chiếu thì Oracle có thể cần `CASCADE CONSTRAINT`, còn PDF lưu ý SQL Server phải xóa FK/bảng tham chiếu trước. `TRUNCATE TABLE` xóa toàn bộ hàng, giữ cấu trúc và có thể kiểm tra lại bằng `DESC`; vì là DDL nên không rollback. Ngược lại, `DELETE` là DML, có thể xóa một phần/toàn bộ hàng và rollback trước commit.

| Lệnh | Phân loại | Phạm vi | Rollback |
| --- | --- | --- | --- |
| `DELETE` | DML | Một hoặc toàn bộ hàng | Có trước COMMIT |
| `DROP` | DDL | Dữ liệu và cấu trúc bảng | Không (auto-commit) |
| `TRUNCATE` | DDL | Toàn bộ hàng, giữ cấu trúc | Không (auto-commit) |
