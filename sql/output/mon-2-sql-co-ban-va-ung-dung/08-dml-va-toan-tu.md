<!-- lecture-contract: v2 -->
# DML và toán tử

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **DML và toán tử**. Route đi từ business mutation → INSERT/UPDATE/DELETE/MERGE → predicates/operators → affected-row validation → transaction/rollback, để lệnh sửa dữ liệu nối với điều kiện an toàn.

> **Mục tiêu:** Hiểu sâu bản chất các thao tác thêm, sửa, xóa, nạp dữ liệu đa bảng (`INSERT ALL`/`FIRST`), đồng bộ đối chiếu (`MERGE`), các toán tử số học/chuỗi, và bẫy logic 3 giá trị của `NULL` trong toán tử `IN` / `NOT IN`.

## Bắt đầu từ câu hỏi nghiệp vụ

Ở các bài trước, ta chủ yếu dùng `SELECT` để đọc dữ liệu đã có. Nhưng một hệ thống thật không chỉ đọc: người dùng đăng ký, thay đổi thông tin, hủy đơn hàng, và dữ liệu từ hệ thống khác cũng phải được đồng bộ. Vì vậy, bài này trả lời câu hỏi: **khi dữ liệu cần thay đổi, ta chọn lệnh nào, phạm vi thay đổi được xác định ra sao, và kết quả đó còn có thể hoàn tác hay không?**

Ta sẽ đi từ nhóm lệnh DML, lần lượt qua `INSERT` (bao gồm nạp đa bảng `INSERT ALL`/`FIRST`), `UPDATE`, `DELETE`, `MERGE`, rồi sang `SELECT`, các toán tử cơ bản và bẫy logic `NULL` với `IN`/`NOT IN`. Trình tự này có chủ ý: trước hết hiểu cách tác động lên hàng dữ liệu, sau đó học cách kiểm tra và tạo biểu thức từ chính dữ liệu đó. Phần kiểm soát việc lưu hay hoàn tác sẽ được bàn giao cho bài **TCL và Transaction**.

> **Phạm vi tham khảo:** PDF *2024 개정판 SQLD 개념정리*, trang 85–86.

> **Nối mạch:** Trong **DML và toán tử**, **Bắt đầu từ câu hỏi nghiệp vụ** nêu nhu cầu biến đổi dữ liệu; **1. DML: nhóm lệnh tác động lên dữ liệu** giải thích cơ chế từng câu lệnh; sau đó **2. SELECT và toán tử: đọc, tính và biểu diễn kết quả** đi sâu vào toán tử và bẫy logic 3 giá trị `NULL`.

## 1. DML: nhóm lệnh tác động lên dữ liệu

DML (Data Manipulation Language, 데이터 조작어) là lớp lệnh làm việc với **các hàng trong bảng đã tồn tại**. Đây là điểm xuất phát cần nắm trước khi học từng câu lệnh: DML không tạo cấu trúc bảng như DDL, cũng không quyết định thời điểm chốt giao dịch như TCL; nó tạo ra thay đổi dữ liệu trong bộ nhớ đệm (Buffer Cache) để transaction quản lý.

DML gồm `INSERT` để thêm hàng, `UPDATE` để sửa hàng, `DELETE` để xóa hàng và `SELECT` để truy vấn. `MERGE` mở rộng nhóm này bằng cách kết hợp cập nhật và chèn theo điều kiện đối chiếu. Trong Oracle, các thay đổi DML chưa trở thành kết quả bền vững cho đến khi `COMMIT`; trước thời điểm đó, `ROLLBACK` vẫn có thể hoàn tác. Do đó, đọc cú pháp DML luôn phải đi cùng hai câu hỏi: **hàng nào bị tác động** và **khi nào thay đổi được xác nhận**.

### 1.1. INSERT: thêm hàng có chủ đích và nạp đa bảng

Khi một đối tượng mới xuất hiện, ta cần ánh xạ các giá trị của đối tượng đó vào các cột của bảng. `INSERT` giải quyết việc này bằng cách tạo thêm hàng; câu lệnh an toàn hay không phụ thuộc trước hết vào cách ta xác định cột.

```sql
-- 1. Chỉ định tường minh danh sách cột
INSERT INTO table_name (column1, column2, column5)
VALUES (value1, value2, value5);

-- 2. Không chỉ định cột (phụ thuộc 100% vào thứ tự vật lý trong DDL)
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
```

Cú pháp đầu tiên ghi rõ cột nhận giá trị, vì vậy không phụ thuộc vào thứ tự vật lý của bảng và giúp người đọc biết từng giá trị có ý nghĩa gì. Cú pháp thứ hai dựa hoàn toàn vào thứ tự cột đã định nghĩa; chỉ nên dùng khi ta chắc chắn thứ tự đó và cung cấp đủ giá trị. Cột bị bỏ qua chỉ có thể nhận `NULL` hoặc `DEFAULT` nếu định nghĩa cột cho phép. Nếu cột là `NOT NULL` mà không có giá trị mặc định hợp lệ, lệnh sẽ báo lỗi.

Theo nội dung ôn thi SQLD:
- Trong Oracle, mỗi câu lệnh `INSERT ... VALUES (...)` truyền thống chỉ chèn một hàng cho mỗi mệnh đề `VALUES`. Trong SQL Server, có thể chèn nhiều nhóm giá trị cùng lúc bằng cách ngăn cách bởi dấu phẩy: `VALUES (1, 'A'), (2, 'B')`.
- Riêng Oracle, chuỗi rỗng `''` được đối xử tương đương `NULL`. Do đó khi cần kiểm tra dữ liệu thiếu, bắt buộc phải dùng toán tử `IS NULL`, không dùng `= ''`.

#### 다중 테이블 INSERT (Multi-table INSERT: INSERT ALL và INSERT FIRST)

Trong môi trường Enterprise và các quy trình ETL/Data Warehouse, một truy vấn nguồn thường cần phân phối dữ liệu vào nhiều bảng đích khác nhau. Thay vì chạy nhiều lệnh `INSERT INTO ... SELECT`, Oracle cung cấp cú pháp nạp đa bảng:

```sql
-- 1. 무조건 INSERT ALL (Unconditional INSERT ALL):
-- Nạp đồng thời vào tất cả các bảng mà không xét điều kiện
INSERT ALL
    INTO emp_sal (empno, sal) VALUES (empno, sal)
    INTO emp_mgr (empno, mgr) VALUES (empno, mgr)
SELECT empno, sal, mgr
FROM emp;

-- 2. 조건부 INSERT ALL (Conditional INSERT ALL):
-- Mỗi hàng nguồn được đánh giá độc lập qua tất cả các nhánh WHEN.
-- Nếu thỏa mãn nhiều nhánh, hàng đó sẽ được chèn vào TẤT CẢ các bảng tương ứng.
INSERT ALL
    WHEN sal >= 3000 THEN
        INTO emp_high_sal VALUES (empno, ename, sal)
    WHEN deptno = 10 THEN
        INTO emp_dept10 VALUES (empno, ename, deptno)
    ELSE
        INTO emp_others VALUES (empno, ename, sal, deptno)
SELECT empno, ename, sal, deptno
FROM emp;

-- 3. 조건부 INSERT FIRST (Conditional INSERT FIRST):
-- Kiểm tra tuần tự từ trên xuống dưới.
-- Khi một hàng nguồn thỏa mãn điều kiện đầu tiên, nó chỉ được chèn vào bảng đó
-- và dừng lại, BỎ QUA toàn bộ các nhánh điều kiện phía sau.
INSERT FIRST
    WHEN sal >= 3000 THEN
        INTO emp_tier1 VALUES (empno, ename, sal)
    WHEN sal >= 2000 THEN
        INTO emp_tier2 VALUES (empno, ename, sal)
    ELSE
        INTO emp_tier3 VALUES (empno, ename, sal)
SELECT empno, ename, sal
FROM emp;
```

> **Bẫy đề thi SQLD:**
> - Trong `INSERT ALL`, nếu nhân viên có `sal = 3500` và thuộc `deptno = 10`, bản ghi đó sẽ xuất hiện ở **cả hai bảng** `emp_high_sal` và `emp_dept10`.
> - Trong `INSERT FIRST`, nhân viên này chỉ được nạp vào `emp_tier1`, nhánh tiếp theo sẽ bị bỏ qua hoàn toàn.

### 1.2. UPDATE: thay đổi đúng phạm vi

`UPDATE` dùng khi hàng đã tồn tại nhưng một hoặc nhiều thuộc tính của nó cần đổi. Mục tiêu của câu lệnh không chỉ là gán giá trị mới; quan trọng hơn là giới hạn đúng tập hàng bằng `WHERE`, bởi `SET` nói **sửa gì** còn `WHERE` nói **sửa ở đâu**.

```sql
UPDATE table_name
SET column1 = value1,
    column2 = value2
WHERE condition;
```

Nếu bỏ `WHERE`, mọi hàng trong bảng đều thỏa điều kiện ngầm định và sẽ bị cập nhật toàn bộ. `UPDATE` cũng có thể nhận kết quả từ subquery (truy vấn con); khi gán nhiều cột, số cột bên trái phải khớp chính xác với số giá trị mà subquery trả về:

```sql
UPDATE emp
SET (sal, comm) = (
    SELECT AVG(sal), AVG(comm)
    FROM emp
)
WHERE ename = 'John';
```

### 1.3. DELETE: xóa hàng, không xóa bảng

`DELETE` giải quyết nhu cầu loại bỏ dữ liệu khỏi bảng nhưng vẫn giữ nguyên cấu trúc bảng, cột và các ràng buộc. Vì nó tác động theo hàng, điều kiện `WHERE` tiếp tục là ranh giới an toàn: có `WHERE` thì xóa tập hàng được chọn, không có `WHERE` thì xóa toàn bộ hàng.

```sql
DELETE FROM table_name
WHERE condition;
```

Khác với `DROP TABLE` và `TRUNCATE TABLE`, `DELETE` là lệnh DML. Trong Oracle, các hàng vừa xóa ghi nhận đầy đủ Undo Log và có thể khôi phục bằng `ROLLBACK` nếu chưa `COMMIT`.

### 1.4. MERGE (Upsert): đồng bộ hai nguồn dữ liệu

`MERGE` (병합) là câu lệnh tối ưu cho bài toán đồng bộ dữ liệu: đối chiếu bảng nguồn (`USING`) với bảng đích (`INTO`) thông qua điều kiện liên kết (`ON`). Nếu bản ghi đã tồn tại thì tiến hành cập nhật (`UPDATE`) hoặc xóa (`DELETE`), nếu chưa tồn tại thì tiến hành chèn mới (`INSERT`).

```sql
MERGE INTO target_table t
USING source_table s
ON (t.target_id = s.source_id)
WHEN MATCHED THEN
    UPDATE SET
        t.name = s.name,
        t.sal = s.sal,
        t.updated_at = SYSDATE
    WHERE s.sal > 0
    DELETE WHERE t.status = 'INACTIVE'
WHEN NOT MATCHED THEN
    INSERT (target_id, name, sal, status, created_at)
    VALUES (s.source_id, s.name, s.sal, 'ACTIVE', SYSDATE)
    WHERE s.sal >= 1000;
```

#### Các quy tắc kiểm tra sống còn trong đề thi SQLD về MERGE
1. **Cột trong mệnh đề `ON` không được phép UPDATE:** Các cột tham gia vào điều kiện kết nối `ON (t.target_id = s.source_id)` là khóa nhận diện bản ghi. Nếu cố tình viết `UPDATE SET t.target_id = ...`, Oracle sẽ chặn đứng với mã lỗi `ORA-38104: Columns referenced in the ON Clause cannot be updated`.
2. **Mệnh đề `DELETE WHERE` phụ thuộc:** Mệnh đề `DELETE` trong `MERGE` chỉ có thể xuất hiện sau `UPDATE`. Nó chỉ xóa những hàng đích **đã được cập nhật** bởi mệnh đề `UPDATE` trước đó và thỏa mãn thêm điều kiện lọc trong `DELETE WHERE`.
3. **Tính tùy chọn của các nhánh:** Câu lệnh `MERGE` không bắt buộc phải có đầy đủ cả hai nhánh. Bạn có thể chỉ viết `WHEN MATCHED THEN` (chỉ cập nhật) hoặc chỉ viết `WHEN NOT MATCHED THEN` (chỉ chèn mới).

---

## 2. SELECT và toán tử: đọc, tính và biểu diễn kết quả

Sau khi dữ liệu được thay đổi qua DML, `SELECT` là công cụ giúp quan sát và xác minh trạng thái. Tách rõ vai trò giữa **thay đổi đã lưu vào bảng** và **biểu thức tính toán hiển thị** là nguyên tắc cốt lõi để tránh sai lệch logic.

### 2.1. SELECT: kiểm tra dữ liệu sau thay đổi

```sql
SELECT [ALL | DISTINCT] column_name
FROM table_name;
```

- `ALL` là tùy chọn mặc định, giữ nguyên mọi dòng kể cả trùng lặp.
- `DISTINCT` loại bỏ các dòng trùng lặp dựa trên toàn bộ các cột xuất hiện sau mệnh đề `SELECT`.

### 2.2. Toán tử số học và nối chuỗi

- **Toán tử số học (`+`, `-`, `*`, `/`):** Áp dụng cho kiểu `NUMBER` và `DATE`. Phép cộng trừ trên ngày biểu thị số ngày chênh lệch (`SYSDATE + 7` là thời điểm 7 ngày sau). Khi biểu thức có chứa giá trị `NULL`, mọi phép tính số học với `NULL` đều cho kết quả là `NULL` (`100 + NULL = NULL`).
- **Toán tử nối chuỗi:**
  - Trong Oracle: Sử dụng cặp gạch đứng `||` (ví dụ: `ename || ' (' || job || ')'`).
  - Trong SQL Server: Sử dụng dấu cộng `+`. Cần lưu ý nếu hai toán hạng là số thì `+` là cộng số, nếu là chuỗi thì là nối chuỗi.
  - Hàm chuẩn ANSI: `CONCAT(str1, str2)`. Chú ý hàm `CONCAT` trong Oracle chỉ nhận đúng 2 tham số; muốn nối 3 chuỗi bằng hàm phải lồng nhau: `CONCAT(CONCAT(a, b), c)`.

### 2.3. Bẫy NULL trong toán tử IN và NOT IN (3-Valued Logic)

Đề thi SQLD thường xuyên đưa ra các câu hỏi bẫy về biểu thức so sánh chứa giá trị `NULL`. Trong SQL, logic không chỉ có `TRUE` và `FALSE`, mà vận hành theo **Logic 3 giá trị (3-Valued Logic: TRUE, FALSE, UNKNOWN)**.

#### 1. Cơ chế hoạt động của toán tử IN

Toán tử `IN` tương đương với chuỗi phép so sánh bằng nối với nhau bởi toán tử `OR`:

$$\text{val} \in (A, B, C) \iff (\text{val} = A) \lor (\text{val} = B) \lor (\text{val} = C)$$

- Giả sử xét điều kiện: `deptno IN (10, 20, NULL)`:
  - Nếu `deptno = 10`: Biểu thức thành `TRUE OR FALSE OR UNKNOWN` $\Rightarrow$ **`TRUE`** (dòng dữ liệu được chọn).
  - Nếu `deptno = 30`: Biểu thức thành `FALSE OR FALSE OR UNKNOWN` $\Rightarrow$ **`UNKNOWN`** (không thỏa mãn `WHERE`, dòng bị loại).

#### 2. Bẫy chết người của toán tử NOT IN

Toán tử `NOT IN` tương đương với chuỗi phép so sánh khác nhau nối với nhau bởi toán tử `AND` theo định lý De Morgan:

$$\text{val} \notin (A, B, C) \iff (\text{val} \neq A) \land (\text{val} \neq B) \land (\text{val} \neq C)$$

- Giả sử xét điều kiện: `deptno NOT IN (10, 20, NULL)`:
  - Biểu thức được phân rã thành: `(deptno <> 10) AND (deptno <> 20) AND (deptno <> NULL)`.
  - Trong SQL, mọi phép so sánh với `NULL` đều trả về `UNKNOWN` (`deptno <> NULL` là `UNKNOWN`).
  - Bất kể giá trị của `deptno` là bao nhiêu (ví dụ `deptno = 30` thì hai vế đầu là `TRUE`):
    $$\text{TRUE} \land \text{TRUE} \land \text{UNKNOWN} \implies \textbf{UNKNOWN}$$
  - Vì kết quả của mệnh đề `WHERE` luôn là `UNKNOWN` (không bao giờ đạt được `TRUE`), câu truy vấn sẽ **KHÔNG TRẢ VỀ BẤT KỲ DÒNG NÀO (TẬP KẾT QUẢ RỖNG)!**

```sql
-- TÌNH HUỐNG BẪY ĐỀ THI KINH ĐIỂN:
-- Tìm những nhân viên không phải là người quản lý (Manager):
SELECT ename
FROM emp
WHERE empno NOT IN (SELECT mgr FROM emp);

-- KẾT QUẢ: 0 dòng (Rỗng)!
-- NGUYÊN NHÂN: Trong bảng emp có nhân viên KING là Chủ tịch (MGR IS NULL).
-- Subquery trả về tập giá trị có chứa NULL (ví dụ: 7839, 7782, ..., NULL).
-- Khiến toàn bộ mệnh đề NOT IN luôn bị đánh giá thành UNKNOWN.

-- CÁCH KHẮC PHỤC CHUẨN:
-- Cách 1: Loại bỏ NULL trong Subquery
SELECT ename
FROM emp
WHERE empno NOT IN (SELECT mgr FROM emp WHERE mgr IS NOT NULL);

-- Cách 2: Sử dụng NOT EXISTS (an toàn tuyệt đối với NULL)
SELECT e.ename
FROM emp e
WHERE NOT EXISTS (
    SELECT 1
    FROM emp m
    WHERE m.mgr = e.empno
);
```

---

## 3. Nối mạch sang Bài tiếp theo: TCL và Transaction

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 08 đã phân tích toàn bộ các công cụ DML biến đổi dữ liệu bản ghi (`INSERT`, `INSERT ALL/FIRST`, `UPDATE`, `DELETE`, `MERGE`) và ranh giới biểu thức tính toán logic `NULL`.
> - **Đang giải quyết gì:** Các lệnh DML này mới chỉ lưu tạm trong bộ nhớ đệm (Buffer Cache). Làm thế nào để đóng gói các thao tác này thành một đơn vị công việc logic toàn vẹn, xác nhận lưu vĩnh viễn hoặc khôi phục an toàn khi có sự cố?
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 09 — TCL và Transaction](./09-tcl-va-transaction.md) để khảo sát 4 thuộc tính ACID, cơ chế `COMMIT`, `ROLLBACK`, và kịch bản chia nhỏ điểm lưu tạm `SAVEPOINT`.
