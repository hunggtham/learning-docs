<!-- lecture-contract: v2 -->
# DDL và định nghĩa bảng (Data Definition Language)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **DDL và định nghĩa bảng**. Route đi từ data types → naming rules → `CREATE TABLE` / `CTAS` → `ALTER TABLE` operations → Deep comparison: `TRUNCATE` vs `DROP` vs `DELETE` on High Water Mark (HWM) and Tablespace.
>
> **Mục tiêu:** Nắm vững các kiểu dữ liệu cốt lõi, quy tắc đặt tên đối tượng, cú pháp `CREATE TABLE`, kỹ thuật nhân bản `CTAS` (thuộc tính kế thừa và không kế thừa), các thao tác hiệu chỉnh cấu trúc `ALTER TABLE`, và phân biệt bản chất giải phóng High Water Mark (HWM) cùng Tablespace giữa `TRUNCATE`, `DROP`, `DELETE`.
>
> **Phạm vi tham khảo:** PDF *2024 개정판 SQLD 개념정리*, Mục II Định nghĩa dữ liệu (trang 90–94).

---

### 1. DDL (Data Definition Language) — Ngôn ngữ định nghĩa dữ liệu

> **KR:** DDL은 데이터의 구조를 정의하는 언어로 테이블, 뷰, 인덱스 등의 데이터베이스 객체를 생성, 변경, 삭제할 때 사용하며 AUTO COMMIT 특성으로 인해 ROLLBACK이 불가능하다.

DDL là nhóm lệnh dùng để kiến tạo và quản lý cấu trúc của các đối tượng trong cơ sở dữ liệu quan hệ:
- **`CREATE`:** Khởi tạo đối tượng mới (bảng, khung nhìn, chỉ mục, v.v.).
- **`ALTER`:** Sửa đổi cấu trúc của đối tượng đã tồn tại (thêm cột, đổi kiểu dữ liệu, đổi tên cột, v.v.).
- **`DROP`:** Xóa bỏ hoàn toàn đối tượng cùng toàn bộ dữ liệu khỏi từ điển dữ liệu (Data Dictionary).
- **`TRUNCATE`:** Xóa sạch toàn bộ dữ liệu của bảng, giải phóng bộ nhớ và đưa con trỏ High Water Mark (HWM) về ban đầu nhưng vẫn bảo tồn khung cấu trúc bảng.

> **Đặc tính kỹ thuật sống còn trong đề thi:** Trong Oracle Database, các câu lệnh DDL mang cơ chế **AUTO-COMMIT ngầm định**. Khi một câu lệnh DDL được phát đi, hệ thống tự động chốt vĩnh viễn các thay đổi trước đó và chính nó. Mọi thao tác DDL **hoàn toàn không thể hoàn tác bằng `ROLLBACK`**.

---

### 2. 데이터 유형 (Data Types) — Các kiểu dữ liệu cốt lõi

RDBMS cung cấp nhiều kiểu dữ liệu để định hình miền giá trị của từng cột thuộc tính:

| Kiểu dữ liệu (Oracle / SQL Server) | Đặc tính kỹ thuật | So sánh chuỗi ký tự (Blank-Padded vs Non-Padded) | Điểm thi trọng tâm |
| --- | --- | --- | --- |
| **`CHAR(n)`** | Chuỗi ký tự độ dài cố định, tối đa $n$ byte. Nếu dữ liệu nạp vào ngắn hơn $n$, hệ thống tự động đệm các ký tự khoảng trắng vào cuối cho đủ $n$ byte. | So sánh kiểu **Blank-Padded**: Khoảng trắng ở đuôi được bỏ qua khi so khớp. Biểu thức `'AA' = 'AA '` trả về **`TRUE`**. | Tốn dung lượng lưu trữ nếu chiều dài dữ liệu biến động nhiều; thích hợp cho mã định danh cố định (Mã quốc gia `CHAR(2)`, Mã giới tính `CHAR(1)`). |
| **`VARCHAR2(n)`** / `VARCHAR(n)` | Chuỗi ký tự độ dài biến đổi, tối đa $n$ byte. Chỉ chiếm dụng đúng dung lượng thực tế của chuỗi được lưu trữ. Tiết kiệm bộ nhớ. | So sánh kiểu **Non-Padded**: Khoảng trắng ở đuôi được tính là một ký tự hợp lệ. Biểu thức `'AA' = 'AA '` trả về **`FALSE`**. | Trong Oracle, nếu gán chuỗi rỗng `''` vào cột `VARCHAR2`, hệ thống tự động đối xử tương đương giá trị `NULL`. |
| **`NUMBER(p, s)`** / `NUMERIC(p, s)` | Kiểu số thực và số nguyên. $p$ (Precision): Tổng số chữ số (từ 1 đến 38); $s$ (Scale): Số chữ số sau dấu phẩy thập phân. | Hệ thống tự động làm tròn phần thập phân nếu vượt quá $s$, nhưng sẽ báo lỗi nếu phần nguyên vượt quá $p - s$. | `NUMBER(6, 2)` chứa tối đa 4 chữ số nguyên và 2 chữ số thập phân (ví dụ: `1234.56` hợp lệ, nhưng `12345.67` sẽ báo lỗi tràn số). |
| **`DATE`** / `DATETIME` | Lưu trữ mốc thời gian gồm cả thế kỷ, năm, tháng, ngày, giờ, phút, giây. | Không cần và không được phép chỉ định độ dài kích thước khi khai báo cột (`col DATE` là đúng, `col DATE(10)` là lỗi). | Trong Oracle, `SYSDATE` trả về kiểu `DATE`. Để trích xuất phần phân số của giây phải dùng kiểu `TIMESTAMP`. |

---

### 3. CREATE TABLE과 명명 규칙 — Tạo bảng và Quy tắc đặt tên

```sql
CREATE TABLE [schema.]table_name (
    column_name data_type [DEFAULT default_value] [constraints],
    column_name data_type [DEFAULT default_value] [constraints],
    ...
    [table_level_constraints]
);
```

#### Quy tắc đặt tên đối tượng (Naming Rules) bắt buộc trong đề thi SQLD

1. **Ký tự bắt đầu:** Tên bảng và tên cột **bắt buộc phải bắt đầu bằng một chữ cái** (`A-Z`, `a-z`). Tuyệt đối không được bắt đầu bằng chữ số (`0-9`) hoặc các ký tự đặc biệt.
2. **Ký tự cho phép:** Chỉ được phép sử dụng các chữ cái (`A-Z`, `a-z`), chữ số (`0-9`), và **3 ký tự đặc biệt duy nhất:**
   - Dấu gạch dưới `_`
   - Dấu đô la `$`
   - Dấu thăng `#`
3. **Từ khóa dành riêng (Reserved Words):** Tuyệt đối không được trùng với các từ khóa dành riêng của hệ thống (như `SELECT`, `FROM`, `WHERE`, `ORDER`, `TABLE`, v.v.).
4. **Tính duy nhất:**
   - Trong cùng một Schema (người dùng), không được phép có hai bảng trùng tên nhau.
   - Trong cùng một bảng, **không được phép có hai cột trùng tên nhau**.
5. **Quy chuẩn thiết kế:** Tên bảng nên đặt ở dạng danh từ số ít (Singular Form), phản ánh đúng thực thể nghiệp vụ đại diện (ví dụ: `emp`, `player`, `product`).

---

### 4. CTAS (Create Table As Select) — Tạo bảng nhanh từ truy vấn

> **KR:** CTAS는 기존 테이블의 데이터를 활용하여 새 테이블을 생성하는 방식으로, 구조뿐 아니라 데이터도 함께 복제된다. 단, 제약조건 중에서는 NOT NULL만 복제되며 PK, FK, UNIQUE, CHECK 등은 복제되지 않는다.

Kỹ thuật CTAS cho phép sao chép nhanh chóng cấu trúc và dữ liệu từ một bảng có sẵn dựa trên tập kết quả của câu lệnh `SELECT`.

```sql
-- 1. Sao chép toàn bộ cấu trúc và dữ liệu từ bảng nguồn:
CREATE TABLE emp_backup AS
SELECT * FROM emp;

-- 2. Sao chép kèm đặt tên cột mới và tính toán biểu thức:
CREATE TABLE dept_salary_stat (department_id, total_salary, avg_salary) AS
SELECT deptno, SUM(sal), ROUND(AVG(sal), 2)
FROM emp
GROUP BY deptno;

-- 3. Kỹ thuật sao chép khung bảng rỗng (Empty Table Skeleton):
-- Sử dụng mệnh đề WHERE luôn SAI (ví dụ 1 = 2) để chỉ sao chép định nghĩa cột, không lấy bất kỳ bản ghi nào.
CREATE TABLE emp_empty_template AS
SELECT * FROM emp
WHERE 1 = 2;
```

#### Bảng ma trận kế thừa thuộc tính trong kỹ thuật CTAS (Trọng tâm thi cử)

| Thuộc tính của bảng nguồn | Kế thừa sang bảng mới? | Giải thích kỹ thuật chuyên sâu |
| --- | --- | --- |
| **Tên cột và Kiểu dữ liệu** | **CÓ** | Bảng mới nhận đúng tên cột và kiểu dữ liệu (`VARCHAR2`, `NUMBER`, `DATE`). |
| **Dữ liệu các bản ghi** | **CÓ** | Sao chép toàn bộ các hàng dữ liệu thỏa mãn điều kiện `WHERE` của câu `SELECT`. |
| **Ràng buộc `NOT NULL`** | **CÓ** | **ĐÂY LÀ RÀNG BUỘC DUY NHẤT ĐƯỢC TỰ ĐỘNG KẾ THỪA!** |
| **Khóa chính `PRIMARY KEY`** | **KHÔNG** | Bảng mới hoàn toàn không có PK. Phải khai báo bổ sung bằng `ALTER TABLE`. |
| **Khóa ngoại `FOREIGN KEY`** | **KHÔNG** | Mối quan hệ tham chiếu bị ngắt bỏ hoàn toàn để tránh xung đột dữ liệu. |
| **Ràng buộc `UNIQUE` và `CHECK`** | **KHÔNG** | Toàn bộ các quy tắc duy nhất và điều kiện kiểm tra miền giá trị bị loại bỏ. |
| **Giá trị mặc định `DEFAULT`** | **KHÔNG** | Thuộc tính `DEFAULT` của cột không được chuyển giao sang bảng mới. |
| **Chỉ mục (`INDEX`)** | **KHÔNG** | Bảng mới không kế thừa bất kỳ Index nào từ bảng nguồn. |

> **Cú pháp tương đương trong SQL Server:** Microsoft SQL Server không dùng từ khóa `CREATE TABLE ... AS SELECT` mà sử dụng mệnh đề `SELECT ... INTO`:
> ```sql
> SELECT * INTO emp_backup FROM emp;
> ```

---

### 5. ALTER TABLE — Hiệu chỉnh cấu trúc bảng đã tồn tại

Sau khi bảng đã được tạo, ta sử dụng lệnh `ALTER TABLE` để biến đổi cấu trúc lưu trữ:

```
+---------------------------------------------------------------------------------+
|                         CÁC THAO TÁC CỦA ALTER TABLE                            |
|                                                                                 |
|  [ADD]             --> Thêm cột mới hoặc thêm ràng buộc mới                     |
|  [MODIFY/ALTER]    --> Đổi kiểu dữ liệu, kích thước, DEFAULT, NOT NULL của cột  |
|  [RENAME COLUMN]   --> Đổi tên một cột trong bảng                               |
|  [DROP COLUMN]     --> Xóa vĩnh viễn một cột khỏi bảng                          |
|  [RENAME TO]       --> Đổi tên của chính bảng đó                                |
|  [DROP CONSTRAINT] --> Xóa một ràng buộc toàn vẹn đang áp dụng                  |
+---------------------------------------------------------------------------------+
```

#### 1. Thêm cột mới (ADD COLUMN)
```sql
ALTER TABLE emp ADD (hobby VARCHAR2(50), joining_bonus NUMBER DEFAULT 0 NOT NULL);
```
- **Vị trí cột mới:** Cột mới được thêm vào **luôn luôn nằm ở vị trí cuối cùng** của bảng. Người dùng hoàn toàn không thể chỉ định vị trí đứng (như chèn vào giữa hai cột đã có).
- **Quy tắc `NOT NULL`:** Nếu bảng **đã có sẵn dữ liệu**, bạn **không thể** thêm một cột mới có ràng buộc `NOT NULL` mà không có giá trị `DEFAULT` đi kèm, vì các bản ghi cũ sẽ nhận giá trị `NULL` và vi phạm ngay lập tức. Thêm kèm `DEFAULT` thì thao tác sẽ thành công.

#### 2. Hiệu chỉnh thuộc tính cột (MODIFY COLUMN)
- Cú pháp trong Oracle: `ALTER TABLE table_name MODIFY (col_name new_data_type ...);`
- Cú pháp trong SQL Server: `ALTER TABLE table_name ALTER COLUMN col_name new_data_type;`

##### Các quy tắc kiểm tra nghiêm ngặt khi MODIFY trong đề thi:
1. **Thay đổi kích thước cột (Column Size):**
   - **Tăng kích thước** (ví dụ từ `VARCHAR2(20)` lên `VARCHAR2(50)`): Luôn luôn thành công trong mọi trường hợp, dù bảng có dữ liệu hay rỗng.
   - **Giảm kích thước** (ví dụ từ `VARCHAR2(50)` xuống `VARCHAR2(30)`): Chỉ thành công khi bảng hoàn toàn rỗng HOẶC chiều dài thực tế của dữ liệu lớn nhất hiện có trong cột nhỏ hơn hoặc bằng kích thước mới (`MAX(LENGTH(col)) <= new_size`).
2. **Thay đổi kiểu dữ liệu (Data Type):**
   - Chỉ được phép thay đổi kiểu dữ liệu khi cột đó **hoàn toàn không chứa dữ liệu** (cột rỗng hoặc tất cả các dòng đều mang giá trị `NULL`).
   - Ngoại lệ: Chuyển đổi qua lại giữa `CHAR` và `VARCHAR2` được phép thực hiện khi kích thước mới đủ chứa toàn bộ dữ liệu hiện tại.
3. **Thay đổi giá trị mặc định (DEFAULT):**
   - Việc sửa đổi `DEFAULT` chỉ có hiệu lực đối với các bản ghi được **chèn mới sau thời điểm chạy lệnh**. Các bản ghi đã tồn tại trước đó không bị thay đổi hồi tố.
   - Để xóa bỏ giá trị mặc định, khai báo: `DEFAULT NULL`.
4. **Thêm ràng buộc `NOT NULL`:**
   - Chỉ thực hiện được khi cột đó hiện **không chứa bất kỳ giá trị `NULL` nào**. Nếu có dù chỉ 1 dòng mang `NULL`, câu lệnh sẽ bị từ chối.

#### 3. Đổi tên cột và Đổi tên bảng (RENAME)
```sql
-- Đổi tên cột trong Oracle:
ALTER TABLE emp RENAME COLUMN ename TO employee_name;

-- Đổi tên bảng trong Oracle:
RENAME emp TO employees;

-- Trong SQL Server: Sử dụng thủ tục hệ thống sp_rename:
EXEC sp_rename 'dbo.emp.ename', 'employee_name', 'COLUMN';
EXEC sp_rename 'dbo.emp', 'employees';
```

#### 4. Xóa cột (DROP COLUMN)
```sql
ALTER TABLE emp DROP COLUMN hobby;
```
- **Quy tắc an toàn:**
  - Mỗi câu lệnh `ALTER TABLE ... DROP COLUMN` chỉ xóa được duy nhất 1 cột (muốn xóa nhiều cột phải thực hiện nhiều lệnh).
  - Không được phép xóa hết toàn bộ các cột: Bảng bắt buộc phải giữ lại **ít nhất 1 cột**.
  - Cột đã bị DROP sẽ bị xóa vĩnh viễn khỏi đĩa từ, giải phóng không gian và **hoàn toàn không thể ROLLBACK**.

---

### 6. DROP TABLE — Xóa bỏ đối tượng bảng

```sql
DROP TABLE emp [CASCADE CONSTRAINTS];
```

- Câu lệnh xóa bỏ hoàn toàn dữ liệu và định nghĩa cấu trúc của bảng khỏi Từ điển dữ liệu (Data Dictionary).
- Sau khi `DROP`, không thể thực hiện truy vấn `SELECT` hay kiểm tra cấu trúc bằng `DESCRIBE`.
- **Tùy chọn `CASCADE CONSTRAINTS` (Oracle):**
  - Nếu bảng đang được tham chiếu bởi khóa ngoại (`FOREIGN KEY`) của một bảng con khác, việc chạy `DROP TABLE` thông thường sẽ báo lỗi vi phạm tham chiếu (`ORA-02449: unique/primary keys in table referenced by foreign keys`).
  - Khi thêm tùy chọn `CASCADE CONSTRAINTS`, Oracle sẽ tự động xóa bỏ toàn bộ các ràng buộc khóa ngoại đang trỏ tới bảng này trước, sau đó xóa bảng bình thường.
  - *Lưu ý:* SQL Server không hỗ trợ từ khóa `CASCADE CONSTRAINTS` trong lệnh `DROP TABLE`. Bạn bắt buộc phải dùng lệnh `ALTER TABLE ... DROP CONSTRAINT` xóa các khóa ngoại ở bảng con trước rồi mới được `DROP TABLE` cha.

---

### 7. Đối đầu sinh tử: DELETE vs TRUNCATE vs DROP

Đây là bảng so sánh kinh điển xuất hiện trong hầu hết các đề thi SQLD nhằm đánh giá sự hiểu biết của thí sinh về tầng kiến trúc vật lý lưu trữ và con trỏ **High Water Mark (HWM - 고수위 마크)**.

#### High Water Mark (HWM) là gì?
- Trong Oracle, mỗi bảng dữ liệu được lưu trữ trong một vùng Segment gồm nhiều khối dữ liệu (Data Blocks).
- **HWM là mốc biên giới hạn khối dữ liệu cao nhất từng được ghi nhận dữ liệu**.
- Khi chạy thao tác quét toàn bộ bảng (**Full Table Scan**), hệ thống bắt buộc phải đọc tuần tự từ khối đầu tiên **cho đến tận đỉnh HWM**, bất kể các khối dữ liệu bên dưới HWM đang có dữ liệu hay đã bị xóa trống.

```
+---------------------------------------------------------------------------------+
|                    HIGH WATER MARK (HWM) TRONG BẢNG DỮ LIỆU                     |
|                                                                                 |
|  [Block 1] [Block 2] [Block 3] [Block 4] [Block 5] | [Block 6] [Block 7] ...   |
|  <---------------- Dữ liệu đã từng ghi ----------->|<--- Chưa dùng bao giờ ---> |
|                                                    ^                            |
|                                                   HWM                           |
|                                                                                 |
|  - Sau khi DELETE toàn bộ:                                                      |
|    Block 1 -> 5 thành các khối TRỐNG RỖNG, nhưng HWM VẪN ĐỨNG NGUYÊN TẠI BLOCK 5!|
|    Full Table Scan vẫn phải đọc qua cả 5 block trống ==> HIỆU NĂNG RẤT CHẬM!    |
|                                                                                 |
|  - Sau khi TRUNCATE TABLE:                                                      |
|    HWM được RESET TỤT VỀ VỊ TRÍ 0 (Đầu bảng)!                                   |
|    Giải phóng các Extent trả lại cho Tablespace ==> TRUY VẤN CỰC NHANH!         |
+---------------------------------------------------------------------------------+
```

#### Bảng ma trận đối đầu toàn diện

| Tiêu chí kỹ thuật | `DELETE` | `TRUNCATE` | `DROP` |
| --- | --- | --- | --- |
| **Phân loại ngôn ngữ** | **DML** (Thao tác dữ liệu) | **DDL** (Định nghĩa dữ liệu) | **DDL** (Định nghĩa dữ liệu) |
| **Phạm vi tác động** | Xóa từng dòng (hỗ trợ lọc `WHERE`) | Xóa toàn bộ dữ liệu bảng (không có `WHERE`) | Xóa toàn bộ cấu trúc và dữ liệu |
| **Khung cấu trúc bảng** | Vẫn tồn tại nguyên vẹn | Vẫn tồn tại nguyên vẹn (dùng `DESC` kiểm tra được) | Bị xóa sạch khỏi CSDL |
| **High Water Mark (HWM)** | **GIỮ NGUYÊN ĐỈNH CŨ** | **RESET HWM VỀ 0** | Toàn bộ Segment bị giải phóng |
| **Giải phóng Tablespace** | **Không giải phóng** Extent về Tablespace | **Giải phóng toàn bộ Extent** (chỉ giữ Initial Extent) | Giải phóng 100% dung lượng về Tablespace |
| **Ghi nhật ký Undo/Redo** | Ghi đầy đủ Undo Log cho từng dòng | Chỉ ghi tối thiểu vào Redo Log (quản lý vùng nhớ) | Chỉ ghi tối thiểu vào Data Dictionary |
| **Tốc độ thực thi** | Rất chậm trên bảng lớn | Cực nhanh (ngay tức thì) | Cực nhanh |
| **Khả năng ROLLBACK** | **CÓ THỂ ROLLBACK** | **KHÔNG THỂ ROLLBACK** (Auto-Commit) | **KHÔNG THỂ ROLLBACK** (Auto-Commit) |
| **Kích hoạt Trigger** | Kích hoạt `DELETE` Trigger | Không kích hoạt bất kỳ Trigger nào | Không kích hoạt Trigger |

---

### 8. Bảng so sánh DDL giữa Oracle và SQL Server

| Tính năng DDL | Oracle Database | Microsoft SQL Server |
| --- | --- | --- |
| **Kiểu dữ liệu chuỗi biến đổi** | `VARCHAR2(n)` (hỗ trợ cả `VARCHAR`) | `VARCHAR(n)` |
| **Kiểu số thực/nguyên** | `NUMBER(p, s)` | `NUMERIC(p, s)` hoặc `DECIMAL(p, s)` |
| **Cú pháp sao chép bảng (CTAS)** | `CREATE TABLE new_t AS SELECT ...` | `SELECT ... INTO new_t FROM ...` |
| **Cú pháp sửa cột** | `ALTER TABLE tbl MODIFY (col ...)` | `ALTER TABLE tbl ALTER COLUMN col ...` |
| **Đổi tên cột** | `ALTER TABLE tbl RENAME COLUMN a TO b` | `sp_rename 'tbl.a', 'b', 'COLUMN'` |
| **Đổi tên bảng** | `RENAME old_tbl TO new_tbl` | `sp_rename 'old_tbl', 'new_tbl'` |
| **Xóa bảng có FK tham chiếu** | Hỗ trợ `DROP TABLE tbl CASCADE CONSTRAINTS` | Không có CASCADE, phải xóa FK trước |
| **Khả năng Rollback lệnh DDL** | Không thể (Implicit Auto-Commit) | Có thể nếu nằm trong `BEGIN TRANSACTION` |

---

### 9. Cạm bẫy thi cử trọng điểm (출제 함정 & 오답 노트)

1. **Bẫy ràng buộc kế thừa trong CTAS:**
   - *Đề thi hỏi:* "Khi thực hiện `CREATE TABLE new_emp AS SELECT * FROM emp`, những ràng buộc nào sau đây được sao chép sang bảng mới?"
   - *Đáp án chính xác:* **Chỉ duy nhất ràng buộc `NOT NULL`**. Toàn bộ `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `CHECK` đều bị bỏ lại.
2. **Bẫy thêm cột `NOT NULL` vào bảng có dữ liệu:**
   - `ALTER TABLE emp ADD (age NUMBER NOT NULL);` $\Rightarrow$ **Báo lỗi ngay!** Vì các dòng hiện tại không thể nhận giá trị `NULL`. Phải bổ sung `DEFAULT`: `ALTER TABLE emp ADD (age NUMBER DEFAULT 0 NOT NULL);`.
3. **Bẫy giảm kích thước cột khi có dữ liệu:**
   - Cột chứa giá trị chuỗi dài nhất là 15 ký tự, nếu cố tình giảm kích thước cột xuống `VARCHAR2(10)` sẽ bị chặn và báo lỗi.
4. **Bẫy Full Table Scan sau lệnh DELETE:**
   - Sau khi chạy `DELETE FROM large_table;`, câu lệnh `SELECT COUNT(*)` chạy sau đó vẫn rất chậm vì HWM chưa được hạ xuống, buộc engine phải quét qua tất cả các khối rác cũ.

---

### 10. Câu hỏi trắc nghiệm thi thử mô phỏng (실전 기출 변형 문제 & 정답 해설)

#### Câu 1: Ràng buộc toàn vẹn trong kỹ thuật CTAS
Bảng `PRODUCT` được định nghĩa có khóa chính `PROD_ID`, cột `PROD_NAME` có ràng buộc `NOT NULL`, cột `PRICE` có ràng buộc `CHECK (PRICE > 0)`, và một chỉ mục duy nhất `IDX_PROD_CODE`.
Thực thi câu lệnh SQL sau:
```sql
CREATE TABLE PRODUCT_BACKUP AS
SELECT * FROM PRODUCT;
```
Hỏi những ràng buộc/đối tượng nào sau đây được kế thừa nguyên vẹn trên bảng mới `PRODUCT_BACKUP`?
- A. `PRIMARY KEY` và `NOT NULL`
- B. Chỉ duy nhất `NOT NULL`
- C. `PRIMARY KEY`, `NOT NULL`, và `CHECK`
- D. Toàn bộ các ràng buộc và chỉ mục `IDX_PROD_CODE`

> **Đáp án chính xác:** **B**
>
> **Giải thích chi tiết:**
> - Kỹ thuật `CTAS` (Create Table As Select) sao chép tên cột, kiểu dữ liệu và các hàng dữ liệu thỏa mãn truy vấn.
> - Về mặt ràng buộc toàn vẹn, **ràng buộc duy nhất được tự động kế thừa sang bảng mới là `NOT NULL`**.
> - Khóa chính (`PRIMARY KEY`), khóa ngoại (`FOREIGN KEY`), ràng buộc duy nhất (`UNIQUE`), ràng buộc kiểm tra (`CHECK`), giá trị mặc định (`DEFAULT`) và các chỉ mục (`INDEX`) đều **KHÔNG** được kế thừa. Lập trình viên phải tự định nghĩa lại thủ công nếu cần.

---

#### Câu 2: Quy tắc hiệu chỉnh cấu trúc bảng bằng ALTER TABLE
Bảng `CUSTOMERS` hiện đang có 1,000 bản ghi dữ liệu. Thao tác nào sau đây bằng lệnh `ALTER TABLE` sẽ **BÁO LỖI** khi thực thi trên Oracle Database?
- A. `ALTER TABLE CUSTOMERS ADD (VIP_STATUS CHAR(1) DEFAULT 'N' NOT NULL);`
- B. `ALTER TABLE CUSTOMERS MODIFY (PHONE_NO VARCHAR2(50));` (Kích thước cũ của cột `PHONE_NO` là `VARCHAR2(20)`).
- C. `ALTER TABLE CUSTOMERS ADD (JOIN_REASON VARCHAR2(100) NOT NULL);`
- D. `ALTER TABLE CUSTOMERS RENAME COLUMN CUST_NAME TO FULL_NAME;`

> **Đáp án chính xác:** **C**
>
> **Giải thích chi tiết:**
> - **A hợp lệ:** Thêm cột mới có ràng buộc `NOT NULL` nhưng có khai báo giá trị mặc định `DEFAULT 'N'`. Khi thực thi, 1,000 bản ghi hiện có sẽ tự động nhận giá trị `'N'`, thỏa mãn ràng buộc `NOT NULL`.
> - **B hợp lệ:** Thao tác tăng kích thước cột từ 20 lên 50 luôn luôn thành công dù bảng có dữ liệu hay không.
> - **C báo lỗi:** Bảng đang có 1,000 bản ghi. Khi thêm một cột mới có ràng buộc `NOT NULL` mà **không có giá trị `DEFAULT`**, toàn bộ 1,000 bản ghi cũ sẽ nhận giá trị `NULL`, dẫn đến vi phạm ràng buộc `NOT NULL` ngay lập tức. Hệ thống chặn đứng với mã lỗi `ORA-01758: table must be empty to add mandatory (NOT NULL) column`.
> - **D hợp lệ:** Đổi tên cột luôn luôn được phép bất kể bảng có dữ liệu hay rỗng.

---

#### Câu 3: Bản chất High Water Mark (HWM) và cơ chế lưu trữ
Phát biểu nào sau đây giải thích chính xác nhất sự khác biệt giữa hai lệnh `DELETE FROM EMP;` và `TRUNCATE TABLE EMP;`?
- A. Lệnh `DELETE` giải phóng toàn bộ các Extent trả về Tablespace, còn `TRUNCATE` giữ nguyên dung lượng đĩa.
- B. Lệnh `TRUNCATE` đưa chỉ số High Water Mark (HWM) trở về mức ban đầu, trong khi `DELETE` vẫn giữ nguyên đỉnh HWM cũ.
- C. Cả hai lệnh đều ghi nhận đầy đủ thông tin vào Undo Segment và có thể khôi phục trạng thái bằng lệnh `ROLLBACK`.
- D. Lệnh `TRUNCATE` cho phép lọc điều kiện xóa các hàng cụ thể bằng mệnh đề `WHERE`.

> **Đáp án chính xác:** **B**
>
> **Giải thích chi tiết:**
> - **A sai:** Ngược lại, `TRUNCATE` mới là lệnh giải phóng các Extent trả về Tablespace (chỉ giữ lại Initial Extent), còn `DELETE` không giải phóng không gian lưu trữ của bảng.
> - **B đúng:** `TRUNCATE` là lệnh DDL, nó đặt lại (reset) con trỏ High Water Mark (HWM) về vị trí khởi tạo ban đầu, giúp các truy vấn quét bảng Full Table Scan sau này diễn ra rất nhanh. Trong khi đó, `DELETE` chỉ xóa dữ liệu trong các block mà không hạ đỉnh HWM, khiến Full Table Scan vẫn phải đọc hết các block trống cũ.
> - **C sai:** `TRUNCATE` là DDL mang cơ chế Auto-Commit, không ghi nhật ký chi tiết vào Undo Segment nên hoàn toàn không thể `ROLLBACK`.
> - **D sai:** `TRUNCATE` không hỗ trợ mệnh đề `WHERE`; muốn xóa có chọn lọc theo điều kiện bắt buộc phải dùng `DELETE`.

---

#### Câu 4: Quy tắc đặt tên đối tượng trong cơ sở dữ liệu
Trong các tên bảng/cột sau đây, tên nào tuân thủ đúng quy tắc định danh chuẩn trong Oracle Database mà không cần đặt trong dấu ngoặc kép?
- A. `2024_SALES_RECORD`
- B. `EMP#INFO_2`
- C. `SELECT`
- D. `USER-DEPARTMENT`

> **Đáp án chính xác:** **B**
>
> **Giải thích chi tiết:**
> - **A không hợp lệ:** Tên đối tượng bắt đầu bằng chữ số (`2`), vi phạm quy tắc bắt buộc phải bắt đầu bằng một chữ cái (`A-Z`, `a-z`).
> - **B hợp lệ:** Bắt đầu bằng chữ cái `E`, chứa các ký tự chữ cái, chữ số và ký tự đặc biệt `#` (3 ký tự đặc biệt được phép là `_`, `$`, `#`).
> - **C không hợp lệ:** Trùng lặp với từ khóa dành riêng của hệ thống (Reserved Word `SELECT`).
> - **D không hợp lệ:** Chứa dấu gạch ngang `-` (toán tử trừ), không nằm trong danh sách các ký tự đặc biệt được phép.

---

## 11. Nối mạch sang Bài tiếp theo: Ràng buộc, Khung nhìn và Đối tượng hỗ trợ

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 10 đã trang bị đầy đủ cú pháp khởi tạo bảng, kiểu dữ liệu, quy tắc định danh, kỹ thuật `CTAS`, cơ chế biến đổi `ALTER TABLE` và bản chất quản lý dung lượng HWM của `TRUNCATE`/`DROP`/`DELETE`.
> - **Đang giải quyết gì:** Một bảng trần chỉ với kiểu dữ liệu chưa đủ để bảo vệ độ chính xác nghiệp vụ. Làm thế nào để áp đặt các quy tắc logic ngăn ngừa dữ liệu rác, cơ chế hoãn kiểm tra ràng buộc (`DEFERRABLE`), và tạo ra các góc nhìn bảo mật có kiểm soát (`WITH CHECK OPTION`, `WITH READ ONLY`)?
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 11 — Constraints, View và các đối tượng hỗ trợ](./11-constraints-view-va-doi-tuong.md) để khảo sát 5 loại ràng buộc toàn vẹn dữ liệu (`PK`, `FK`, `NOT NULL`, `UNIQUE`, `CHECK`), cơ chế hoãn kiểm tra và các đối tượng hỗ trợ `VIEW`, `SEQUENCE`, `SYNONYM`.
