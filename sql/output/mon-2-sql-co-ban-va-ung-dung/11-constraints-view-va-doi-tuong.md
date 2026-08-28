# Constraints, View và các đối tượng hỗ trợ

> **Nguồn bám sát:** PDF *2024 개정판 SQLD 개념정리*, trang 95–100.
>
> **Liên kết bài trước:** DDL tạo cấu trúc; constraint bảo đảm dữ liệu đi vào cấu trúc đó vẫn đúng quy tắc nghiệp vụ. Điều này hiện thực hóa consistency (Consistency) (tính nhất quán) trong ACID đã học.

## 1. 제약 조건 (Constraint) (ràng buộc)

> **KR:** 제약 조건은 데이터의 무결성을 유지하기 위해 특정 컬럼에 설정하는 제약이며 테이블에 데이터가 올바르게 들어오도록 거는 장치이다.

Constraint bảo vệ integrity (Integrity) (tính toàn vẹn): ví dụ mã sinh viên không được `NULL` và không được trùng. Có thể khai báo khi `CREATE TABLE`, khi thêm cột, hoặc thêm constraint cho cột sẵn có. Đặt tên constraint giúp xem lỗi, sửa/xóa constraint và đọc DDL dễ hơn.

```sql
CREATE TABLE table_name (
  column1 data_type [DEFAULT value]
    [CONSTRAINT constraint_name] constraint_type,
  ...
);

ALTER TABLE table_name
ADD CONSTRAINT constraint_name constraint_type (column_name);

ALTER TABLE table_name
DROP CONSTRAINT constraint_name;
```

## 2. PRIMARY KEY (Primary Key) (khóa chính)

> **KR:** PRIMARY KEY는 행 데이터를 고유하게 구분하는 식별자이고 중복과 NULL을 허용하지 않는다.

`PRIMARY KEY` (Primary Key) (khóa chính) nhận diện duy nhất một hàng, tương đương `UNIQUE` + `NOT NULL`. DBMS tự tạo unique index (Unique Index) (chỉ mục duy nhất) khi tạo PK. Mỗi bảng chỉ có một PK, nhưng PK đó có thể là composite key (Composite Key) (khóa ghép) gồm nhiều cột. PK không có default; đừng nhầm CTAS sao chép `NOT NULL` với việc sao chép PK — CTAS không sao chép PK.

```sql
CONSTRAINT pk_name PRIMARY KEY (column1, column2)
```

## 3. UNIQUE, NOT NULL và CHECK

> **KR:** UNIQUE는 중복을 허용하지 않고 NULL은 허용하며, NOT NULL은 NULL 값을 허용하지 않는다.

`UNIQUE` (Unique) (duy nhất) ngăn giá trị trùng nhưng cho phép `NULL` theo nội dung PDF; nó cũng tạo unique index. `NOT NULL` (Not Null) (không rỗng) là thuộc tính cột và là constraint duy nhất được CTAS kế thừa. `CHECK` (Check) (kiểm tra miền giá trị) giới hạn trực tiếp giá trị hợp lệ theo điều kiện, chẳng hạn lương phải dương.

```sql
CREATE TABLE test (
  id NUMBER,
  name VARCHAR2(10) UNIQUE
);

ALTER TABLE emp1
ADD CONSTRAINT emp_sal_ck CHECK (sal > 0);
```

## 4. FOREIGN KEY (Foreign Key) (khóa ngoại)

> **KR:** FOREIGN KEY는 자식 테이블에 생성하며 부모 테이블의 참조 컬럼은 PK 또는 UNIQUE KEY를 가져야 한다.

FK được tạo ở child table (Child Table) (bảng con) và tham chiếu reference key (Reference Key) (cột được tham chiếu) của parent table (Parent Table) (bảng cha). Cột đích phải là PK hoặc UNIQUE. FK có thể `NULL` và một bảng có thể có nhiều FK. Điều này liên hệ với bài mô hình dữ liệu: quan hệ giữa entity cha/con được cưỡng chế ở tầng dữ liệu, không chỉ tồn tại trên ERD.

```sql
CREATE TABLE emp1 (
  empno NUMBER PRIMARY KEY,
  deptno NUMBER,
  CONSTRAINT emp_fk FOREIGN KEY (deptno)
    REFERENCES dept1(deptno)
);
```

> **KR:** 자식 테이블에는 부모가 가진 값만 INSERT와 UPDATE할 수 있고, 자식이 있는 부모는 삭제와 값 변경이 불가능하다.

Ở bảng con, INSERT/UPDATE FK chỉ dùng giá trị đang tồn tại ở bảng cha (hoặc NULL nếu cột cho phép). Xóa hàng con không bị FK cản; nhưng không thể xóa hoặc đổi khóa ở hàng cha khi vẫn có hàng con tham chiếu, trừ khi dùng referential action (Referential Action) (hành động tham chiếu) phù hợp.

| 한국어 (English) (Tiếng Việt) | Khi xóa cha |
| --- | --- |
| 연쇄 (ON DELETE CASCADE) (xóa dây chuyền) | Xóa luôn hàng con. |
| 널 설정 (ON DELETE SET NULL) (đặt NULL) | Đặt FK của hàng con thành NULL; cột con phải cho phép NULL. |
| 제한 (RESTRICT) (hạn chế) | Chỉ cho xóa cha khi không còn con tham chiếu. |
| 동작 없음 (NO ACTION) (không hành động) | Không thực hiện thao tác vi phạm toàn vẹn tham chiếu. |

PDF còn nêu insert action (Insert Action) (hành động khi chèn): `Automatic` (tự động tạo cha rồi chèn con), `Set Null` (đặt FK con NULL), `Set Default` (đặt default), `Dependent` (chỉ chèn con khi cha đã có), `No Action` (không chấp nhận thao tác vi phạm). Khi làm bài SQLD, trước hết đọc xem đề nói đến xóa/sửa cha hay chèn/sửa con, vì hướng tác động khác nhau.

## 5. VIEW (View) (khung nhìn)

> **KR:** VIEW는 저장공간을 가지지 않지만 테이블처럼 조회 및 수정 가능한 객체이며 가상 테이블이라고도 한다.

View là virtual table (Virtual Table) (bảng ảo): nó lưu định nghĩa truy vấn chứ thông thường không giữ dữ liệu vật lý. Simple view (Simple View) (view đơn giản) lấy từ một bảng, còn complex view (Complex View) (view phức hợp) được tạo bằng JOIN từ hai bảng trở lên. Khi truy vấn view, DB thực thi lại truy vấn định nghĩa nên dữ liệu gốc thay đổi sẽ phản ánh trong kết quả view.

```sql
CREATE [OR REPLACE] VIEW view_name AS
SELECT ...;

DROP VIEW view_name;
```

> **KR:** 뷰는 독립성, 편리성, 보안성의 장점이 있고 정의 변경, 삽입·삭제·갱신 연산, 인덱스 구성에는 제약이 있다.

View giúp độc lập chương trình với thay đổi cấu trúc, tái sử dụng truy vấn phức tạp và che cột nhạy cảm như lương. View có thể được dùng làm nền để định nghĩa view khác; xóa bảng gốc làm view dựa trên nó không còn dùng được. PDF nhấn mạnh hạn chế về thay đổi định nghĩa, DML và index; hãy xem view như một lớp trình bày/bảo vệ truy vấn chứ không phải bản sao dữ liệu mặc định.

```sql
CREATE VIEW v_emp_dept AS
SELECT e.empno, e.ename, e.deptno, d.dname
FROM emp e, dept d
WHERE e.deptno = d.deptno;
```

## 6. SEQUENCE (Sequence) (bộ sinh số tuần tự)

> **KR:** SEQUENCE는 자동으로 연속적인 숫자를 부여해주는 객체이다.

Sequence tạo số liên tiếp, thường dùng làm giá trị khóa nhân tạo. `INCREMENT BY` là bước tăng, `START WITH` là giá trị đầu, `MAXVALUE`/`MINVALUE` là giới hạn, `CYCLE`/`NOCYCLE` quyết định có quay vòng không và `CACHE N` là số giá trị đệm trước trong bộ nhớ (mặc định PDF nêu 20). Sequence tạo số, không tự bảo đảm uniqueness trong mọi tình huống; PK mới là ràng buộc bảo đảm không trùng.

```sql
CREATE SEQUENCE seq_name
  INCREMENT BY 1
  START WITH 1
  MAXVALUE 9999
  NOCYCLE
  CACHE 20;
```

## 7. SYNONYM (Synonym) (từ đồng nghĩa/bí danh đối tượng)

> **KR:** SYNONYM은 테이블 별칭을 생성하는 객체이다.

Synonym là bí danh cho object, giúp không phải ghi lặp `owner.table_name`, ví dụ dùng `EMP` thay cho `SCOTT.EMP` khi đã có quyền. `PUBLIC` (Public) (công khai) cho mọi người dùng; private synonym (bí danh riêng) chỉ người tạo sử dụng. `OR REPLACE` thay thế synonym trùng tên; synonym public phải được xóa theo cách public.

```sql
CREATE [OR REPLACE] [PUBLIC] SYNONYM emp
FOR scott.emp;
```
