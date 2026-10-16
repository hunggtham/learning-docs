<!-- lecture-contract: v2 -->
# DML và toán tử

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **DML và toán tử**. Route đi từ business mutation → INSERT/UPDATE/DELETE/MERGE → predicates/operators → affected-row validation → transaction/rollback, để lệnh sửa dữ liệu nối với điều kiện an toàn.
>
> **Mục tiêu:** Hiểu sâu bản chất các thao tác thêm, sửa, xóa, nạp dữ liệu đa bảng (`INSERT ALL`/`FIRST`), cập nhật tương quan (Correlated Update), đồng bộ đối chiếu (`MERGE`), các toán tử số học/chuỗi, và bẫy logic 3 giá trị của `NULL` trong toán tử `IN` / `NOT IN`.
>
> **Phạm vi tham khảo:** PDF *2024 개정판 SQLD 개념정리*, Mục II Quản lý thao tác dữ liệu (trang 85–86).

---

## Bắt đầu từ câu hỏi nghiệp vụ

Ở các bài trước, ta chủ yếu dùng `SELECT` để đọc dữ liệu đã có. Nhưng một hệ thống vận hành thực tế không chỉ đọc: người dùng đăng ký tài khoản mới, điều chỉnh địa chỉ giao hàng, hủy đơn hàng quá hạn, và dữ liệu từ hệ thống đối tác bên ngoài cần được đồng bộ định kỳ vào kho dữ liệu. Vì vậy, bài học này trả lời câu hỏi nghiệp vụ cốt lõi: **khi dữ liệu cần biến đổi, ta lựa chọn câu lệnh DML nào, phạm vi ảnh hưởng được kiểm soát chặt chẽ ra sao, và kết quả đó tồn tại ở đâu trước khi được chốt vĩnh viễn?**

Ta sẽ đi từ bản chất DML trong kiến trúc bộ nhớ đệm (Buffer Cache), lần lượt qua `INSERT` (kèm kỹ thuật nạp đa bảng `INSERT ALL`/`FIRST`), `UPDATE` (đơn bảng và tương quan nhiều cột), `DELETE`, `MERGE` (Upsert đồng bộ), rồi mở rộng sang các toán tử số học/chuỗi và bẫy tử thần `NOT IN` với giá trị `NULL`.

---

## 1. DML: Nhóm lệnh thao tác dữ liệu (Data Manipulation Language)

DML (데이터 조작어) là nhóm câu lệnh trực tiếp thay đổi nội dung các hàng bản ghi trong các bảng đã tồn tại sẵn trong cơ sở dữ liệu.

```
+---------------------------------------------------------------------------------+
|                       VÒNG ĐỜI DỮ LIỆU CỦA LỆNH DML                             |
|                                                                                 |
|  [Câu lệnh DML] ---> [Database Buffer Cache] ---> [Undo Segment / Redo Buffer]  |
|  (INSERT/UPDATE/        (Dữ liệu thay đổi tạm         (Lưu ảnh cũ để ROLLBACK   |
|   DELETE/MERGE)          thời trong bộ nhớ)            và ghi nhật ký khôi phục)|
|                                |                                                |
|                                v                                                |
|                        +---------------+                                        |
|                        | Quyết định?   |                                        |
|                        +---------------+                                        |
|                         /             \                                         |
|                 [COMMIT]               [ROLLBACK]                               |
|                    v                       v                                    |
|          Ghi bền vững vào Đĩa     Hủy bỏ toàn bộ thay đổi,                      |
|          Giải phóng Locks         Khôi phục dữ liệu từ Undo                     |
+---------------------------------------------------------------------------------+
```

> **Bản chất kỹ thuật:** Trong Oracle Database, các thay đổi do DML tạo ra **chỉ mới tồn tại trong bộ nhớ đệm (Database Buffer Cache)** và các khối Undo/Redo. Chúng chưa hề được ghi vĩnh viễn xuống đĩa và hoàn toàn có thể hoàn tác bằng `ROLLBACK`. Để kết thúc một giao dịch DML thành công, người dùng bắt buộc phải phát lệnh `COMMIT`.

---

### 1.1. INSERT: Thêm hàng mới và Kỹ thuật nạp đa bảng

Khi một đối tượng mới phát sinh trong nghiệp vụ, câu lệnh `INSERT` tạo thêm một hoặc nhiều hàng mới vào bảng đích.

#### Cú pháp cơ bản và quy tắc xác định cột

```sql
-- Dạng 1: Chỉ định tường minh danh sách cột (Khuyến nghị dùng trong dự án)
INSERT INTO emp (empno, ename, job, deptno)
VALUES (7950, 'ALICE', 'ANALYST', 20);

-- Dạng 2: Không chỉ định danh sách cột (Ngầm định theo thứ tự vật lý trong DDL)
INSERT INTO emp
VALUES (7951, 'BOB', 'CLERK', 7902, SYSDATE, 1500, NULL, 20);
```

- **Quy tắc an toàn:** Ở dạng 1, thứ tự các giá trị trong `VALUES` khớp với danh sách cột được liệt kê. Cột nào bị bỏ qua sẽ tự động nhận giá trị `DEFAULT` (nếu có) hoặc `NULL`. Nếu cột bị bỏ qua có ràng buộc `NOT NULL` mà không có giá trị mặc định, hệ thống sẽ chặn đứng và báo lỗi vi phạm ràng buộc.
- **Xử lý chuỗi rỗng `''`:**
  - Trong **Oracle Database**, chuỗi rỗng `''` được hệ thống quy về giá trị **`NULL`**. Do đó, nếu chèn `VALUES (7952, '', ...)` vào cột `NOT NULL`, câu lệnh sẽ báo lỗi `ORA-01400: cannot insert NULL`.
  - Trong **SQL Server**, chuỗi rỗng `''` là một chuỗi có độ dài bằng 0, hoàn toàn khác `NULL` và chèn thành công vào cột `NOT NULL`.

---

#### Kỹ thuật nạp đa bảng trong Oracle (Multi-Table INSERT)

Trong các hệ thống phân tích dữ liệu (ETL / Data Warehouse), từ một tập dữ liệu nguồn truy vấn qua `SELECT`, ta thường phải phân tách và chèn đồng thời vào nhiều bảng đích khác nhau. Oracle cung cấp 3 biến thể mạnh mẽ:

##### 1. 무조건 INSERT ALL (Unconditional INSERT ALL - Nạp không điều kiện)
Mỗi dòng dữ liệu trả về từ câu truy vấn nguồn sẽ được chèn vô điều kiện vào tất cả các bảng đích được khai báo:

```sql
INSERT ALL
    INTO emp_salary_history (empno, sal, change_date) VALUES (empno, sal, SYSDATE)
    INTO emp_dept_log (empno, deptno, log_date) VALUES (empno, deptno, SYSDATE)
SELECT empno, sal, deptno
FROM emp;
```

##### 2. 조건부 INSERT ALL (Conditional INSERT ALL - Nạp có điều kiện kiểm tra toàn bộ)
Từng dòng dữ liệu nguồn được mang đi kiểm tra độc lập qua **tất cả** các mệnh đề `WHEN`. Nếu thỏa mãn nhiều điều kiện, dòng đó sẽ được nhân bản và chèn vào **tất cả** các bảng thỏa mãn:

```sql
INSERT ALL
    WHEN sal >= 3000 THEN
        INTO emp_high_sal (empno, ename, sal) VALUES (empno, ename, sal)
    WHEN deptno = 10 THEN
        INTO emp_dept10 (empno, ename, deptno) VALUES (empno, ename, deptno)
    ELSE
        INTO emp_others (empno, ename, sal, deptno) VALUES (empno, ename, sal, deptno)
SELECT empno, ename, sal, deptno
FROM emp;
```

> **Điểm mấu chốt trong đề thi:** Nếu một nhân viên có `sal = 5000` và `deptno = 10`, nhân viên này thỏa mãn cả 2 nhánh `WHEN` đầu tiên. Do đó, bản ghi của nhân viên này sẽ **xuất hiện đồng thời ở cả 2 bảng** `emp_high_sal` và `emp_dept10`!

##### 3. 조건부 INSERT FIRST (Conditional INSERT FIRST - Nạp theo cơ chế Short-Circuit)
Hệ thống đánh giá các nhánh `WHEN` theo thứ tự từ trên xuống dưới. Khi một hàng dữ liệu thỏa mãn điều kiện đầu tiên, nó sẽ lập tức được chèn vào bảng tương ứng và **dừng lại ngay, bỏ qua toàn bộ các nhánh `WHEN` hoặc `ELSE` phía sau**:

```sql
INSERT FIRST
    WHEN sal >= 3000 THEN
        INTO emp_tier1 (empno, ename, sal) VALUES (empno, ename, sal)
    WHEN sal >= 2000 THEN
        INTO emp_tier2 (empno, ename, sal) VALUES (empno, ename, sal)
    ELSE
        INTO emp_tier3 (empno, ename, sal) VALUES (empno, ename, sal)
SELECT empno, ename, sal
FROM emp;
```

```
+---------------------------------------------------------------------------------+
|               SO SÁNH CƠ CHẾ INSERT ALL VÀ INSERT FIRST                         |
|                                                                                 |
|  Dữ liệu đầu vào: Nhân viên KING có [sal = 5000, deptno = 10]                   |
|                                                                                 |
|  * Với INSERT ALL:                                                              |
|    - Kiểm tra nhánh 1 (sal >= 3000): THỎA MÃN  ==> Chèn vào emp_high_sal        |
|    - Kiểm tra nhánh 2 (deptno = 10): THỎA MÃN  ==> Chèn vào emp_dept10          |
|    ==> Kết quả: KING được nạp vào CẢ 2 BẢNG.                                    |
|                                                                                 |
|  * Với INSERT FIRST:                                                            |
|    - Kiểm tra nhánh 1 (sal >= 3000): THỎA MÃN  ==> Chèn vào emp_tier1           |
|    - DỪNG XỬ LÝ (Short-circuit)! Bỏ qua nhánh 2 và nhánh ELSE.                  |
|    ==> Kết quả: KING CHỈ được nạp vào DUY NHẤT emp_tier1.                       |
+---------------------------------------------------------------------------------+
```

---

### 1.2. UPDATE: Sửa đổi dữ liệu và Cập nhật tương quan (Correlated Update)

Câu lệnh `UPDATE` cập nhật giá trị của một hoặc nhiều cột trên các hàng bản ghi đã tồn tại trong bảng.

```sql
UPDATE table_name
SET column1 = value1,
    column2 = value2
WHERE filter_condition;
```

- **Mệnh đề WHERE:** Nếu bỏ quên mệnh đề `WHERE`, câu lệnh `UPDATE` sẽ **thay đổi toàn bộ các dòng** trong bảng dữ liệu.

#### Cập nhật nhiều cột từ Subquery (다중 컬럼 서브쿼리 활용)
Trong Oracle, ta có thể cập nhật cùng lúc nhiều cột bằng kết quả trả về từ một subquery duy nhất:

```sql
UPDATE emp
SET (sal, comm) = (
    SELECT ROUND(AVG(sal), 0), ROUND(AVG(NVL(comm, 0)), 0)
    FROM emp
    WHERE deptno = 30
)
WHERE empno = 7900;
```

#### Cập nhật tương quan (Correlated UPDATE)
Trong các nghiệp vụ phức tạp, giá trị mới cần cập nhật phụ thuộc trực tiếp vào chính từng dòng của bảng đang được update:

```sql
-- Cập nhật lương của từng nhân viên bằng mức lương trung bình của chính phòng ban mà người đó trực thuộc:
UPDATE emp e
SET e.sal = (
    SELECT ROUND(AVG(m.sal), 0)
    FROM emp m
    WHERE m.deptno = e.deptno
)
WHERE e.deptno IN (10, 20);
```

> **Lưu ý kiểm tra an toàn:** Subquery trong mệnh đề `SET` bắt buộc phải là **Scalar Subquery** (truy vấn con vô hướng, chỉ trả về đúng 1 giá trị duy nhất cho mỗi dòng được duyệt). Nếu subquery trả về nhiều hơn 1 dòng, Oracle sẽ báo lỗi `ORA-01427: single-row subquery returns more than one row`.

---

### 1.3. DELETE: Xóa dữ liệu có kiểm soát

Câu lệnh `DELETE` xóa bỏ các hàng dữ liệu ra khỏi bảng mà vẫn giữ nguyên vẹn định nghĩa cấu trúc bảng, các ràng buộc và chỉ mục.

```sql
DELETE FROM table_name
WHERE filter_condition;
```

- Nếu không có mệnh đề `WHERE`, toàn bộ các hàng trong bảng sẽ bị xóa sạch.
- **Bản chất DML của DELETE:** Mỗi hàng bị xóa đều được ghi nhận chi tiết vào Undo Segment để sẵn sàng hoàn tác nếu người dùng phát lệnh `ROLLBACK`. Do đó, khi xóa bảng lớn hàng triệu dòng, `DELETE` sẽ tiêu tốn dung lượng bộ nhớ đệm và thời gian thực thi rất lâu so với `TRUNCATE`.
- Lệnh `DELETE` **không làm hạ chỉ số High Water Mark (HWM)** của bảng.

---

### 1.4. MERGE (Upsert): Đồng bộ dữ liệu đa năng

`MERGE` (병합) cho phép gộp các thao tác `INSERT`, `UPDATE` và `DELETE` vào trong một câu lệnh duy nhất, rất tối ưu khi đồng bộ dữ liệu giữa bảng tạm (Staging/Source) và bảng nghiệp vụ đích (Target).

```sql
MERGE INTO target_table t
USING source_table s
ON (t.target_id = s.source_id)
WHEN MATCHED THEN
    UPDATE SET
        t.target_name = s.source_name,
        t.target_sal  = s.source_sal,
        t.updated_at  = SYSDATE
    WHERE s.source_sal > 0
    DELETE WHERE t.target_sal >= 5000
WHEN NOT MATCHED THEN
    INSERT (target_id, target_name, target_sal, status, created_at)
    VALUES (s.source_id, s.source_name, s.source_sal, 'ACTIVE', SYSDATE)
    WHERE s.source_sal >= 1000;
```

#### 4 quy tắc vàng bất di bất dịch về MERGE trong đề thi SQLD

1. **Cột tham gia điều kiện `ON (...)` tuyệt đối không được UPDATE:**
   - Các cột nằm trong ngoặc `ON (t.target_id = s.source_id)` được xem là khóa liên kết đối chiếu danh tính.
   - Nếu bạn cố tình viết `UPDATE SET t.target_id = s.source_id`, Oracle sẽ dừng thực thi và ném ra lỗi kinh điển:
     `ORA-38104: Columns referenced in the ON Clause cannot be updated`.
2. **Cơ chế phụ thuộc của mệnh đề `DELETE WHERE`:**
   - Mệnh đề `DELETE` trong `MERGE` **không thể đứng độc lập** mà bắt buộc phải đi kèm sau mệnh đề `UPDATE`.
   - Lệnh `DELETE` chỉ xóa những dòng dữ liệu ở bảng đích **đã được xử lý bởi lệnh `UPDATE` ngay trước đó** và đồng thời thỏa mãn thêm điều kiện trong mệnh đề `WHERE` của `DELETE`. Những dòng không bị UPDATE sẽ không bao giờ bị DELETE bởi MERGE.
3. **Tính tùy chọn của các nhánh (Flexibility):**
   - Không bắt buộc phải có đầy đủ cả `WHEN MATCHED` và `WHEN NOT MATCHED`. Bạn có thể chỉ viết nhánh `WHEN MATCHED` (chỉ cập nhật/xóa) hoặc chỉ viết nhánh `WHEN NOT MATCHED` (chỉ chèn mới).
4. **Bí danh bảng:** Không lặp lại tên bảng đích trong các mệnh đề con `UPDATE` hoặc `INSERT`.

---

## 2. SELECT và các toán tử: Biểu diễn và kiểm tra kết quả

Sau khi các thao tác DML biến đổi dữ liệu, ta dùng `SELECT` và các toán tử để kiểm tra, tính toán giá trị biểu thức.

### 2.1. Toán tử số học và nối chuỗi

- **Toán tử số học (`+`, `-`, `*`, `/`):**
  - Thực hiện trên kiểu `NUMBER` và `DATE`.
  - Phép tính với `NULL`: Bất kỳ số nào cộng, trừ, nhân, chia với `NULL` đều cho kết quả là `NULL` ($100 + \text{NULL} = \text{NULL}$; $0 \times \text{NULL} = \text{NULL}$).
- **Toán tử nối chuỗi:**
  - Trong **Oracle**: Dùng cặp dấu gạch đứng `||` (ví dụ: `'NV: ' || ename`).
  - Trong **SQL Server**: Dùng dấu cộng `+` (ví dụ: `'NV: ' + ename`). Chú ý: Nếu toán tử `+` kết hợp giữa một chuỗi và một số, SQL Server sẽ cố ép kiểu chuỗi thành số, nếu thất bại sẽ báo lỗi chuyển đổi kiểu.
  - Chuẩn ANSI: Dùng hàm `CONCAT(str1, str2)`.

---

### 2.2. Bẫy tử thần của giá trị NULL trong toán tử IN và NOT IN (3-Valued Logic)

Đây là chủ đề bẫy xuất hiện nhiều nhất trong các câu hỏi phân loại điểm cao của kỳ thi SQLD.

#### Cơ chế Logic 3 giá trị của toán tử IN
Toán tử `IN` tương đương với chuỗi phép so sánh bằng (`=`) nối với nhau qua toán tử logic `OR`:

$$\text{x} \in (A, B, \text{NULL}) \iff (x = A) \lor (x = B) \lor (x = \text{NULL})$$

- Xét kiểm tra: `deptno IN (10, 20, NULL)`:
  - Nếu `deptno = 10`: `(10 = 10) OR (10 = 20) OR (10 = NULL)` $\Rightarrow$ `TRUE OR FALSE OR UNKNOWN` $\Rightarrow$ **`TRUE`**. Dòng này được chọn!
  - Nếu `deptno = 30`: `(30 = 10) OR (30 = 20) OR (30 = NULL)` $\Rightarrow$ `FALSE OR FALSE OR UNKNOWN` $\Rightarrow$ **`UNKNOWN`**. Dòng này bị loại.

#### Cạm bẫy phá hủy truy vấn của toán tử NOT IN
Theo luật De Morgan, toán tử `NOT IN` tương đương với chuỗi phép so sánh khác (`<>`) nối với nhau qua toán tử logic `AND`:

$$\text{x} \notin (A, B, \text{NULL}) \iff (x \neq A) \land (x \neq B) \land (x \neq \text{NULL})$$

- Xét kiểm tra: `deptno NOT IN (10, 20, NULL)`:
  - Biểu thức được tách thành: `(deptno <> 10) AND (deptno <> 20) AND (deptno <> NULL)`.
  - Vì mọi phép so sánh với `NULL` đều trả về `UNKNOWN`, vế `deptno <> NULL` **luôn luôn ra `UNKNOWN`** đối với mọi dòng dữ liệu!
  - Cho dù `deptno = 30` thỏa mãn cả 2 vế đầu (`TRUE AND TRUE`), thì:
    $$\text{TRUE} \land \text{TRUE} \land \text{UNKNOWN} \implies \textbf{UNKNOWN}$$
  - Vì mệnh đề `WHERE` chỉ chấp nhận kết quả `TRUE`, biểu thức ra `UNKNOWN` sẽ khiến **toàn bộ dữ liệu bị loại bỏ** $\Rightarrow$ **CÂU TRUY VẤN TRẢ VỀ 0 HÀNG (TẬP RỖNG)!**

```sql
-- TRƯỜNG HỢP GẶP THƯỜNG XUYÊN TRONG ĐỀ THI:
-- Tìm tên các nhân viên không phải là Quản lý (Manager):
SELECT ename
FROM emp
WHERE empno NOT IN (
    SELECT mgr
    FROM emp
);

-- KẾT QUẢ: 0 HÀNG (RỖNG)!
-- NGUYÊN NHÂN: Trong bảng emp, Chủ tịch (KING) không có cấp trên nên MGR IS NULL.
-- Subquery trả về danh sách có chứa NULL: (7839, 7782, 7698, ..., NULL).
-- Khiến toán tử NOT IN luôn trả về UNKNOWN!

-- HAI GIẢI PHÁP CHUẨN XÁC ĐỂ KHẮC PHỤC:
-- Cách 1: Loại bỏ giá trị NULL ngay trong Subquery
SELECT ename
FROM emp
WHERE empno NOT IN (
    SELECT mgr
    FROM emp
    WHERE mgr IS NOT NULL
);

-- Cách 2: Sử dụng NOT EXISTS (An toàn tuyệt đối trước giá trị NULL)
SELECT e.ename
FROM emp e
WHERE NOT EXISTS (
    SELECT 1
    FROM emp m
    WHERE m.mgr = e.empno
);
```

---

## 3. Bảng ma trận so sánh DML giữa Oracle và SQL Server

| Đặc tính DML | Oracle Database | Microsoft SQL Server |
| --- | --- | --- |
| **Cơ chế Commit mặc định** | Không auto-commit. Bắt buộc phải phát lệnh `COMMIT` thủ công. | Mặc định **AUTO-COMMIT**. Mỗi lệnh DML tự commit ngay khi chạy xong. |
| **Chèn chuỗi rỗng `''`** | Tự động coi là giá trị **`NULL`**. | Coi là chuỗi có độ dài 0 (khác `NULL`). |
| **Chèn nhiều dòng `VALUES`** | Trước bản 23c: Không hỗ trợ `VALUES (...), (...)`. Phải dùng `INSERT ALL` hoặc `UNION ALL`. | Hỗ trợ cú pháp chuẩn ANSI: `VALUES (1, 'A'), (2, 'B')`. |
| **Cú pháp nạp đa bảng** | Hỗ trợ mạnh mẽ `INSERT ALL` và `INSERT FIRST`. | Không hỗ trợ cú pháp `INSERT ALL/FIRST`. |
| **Từ khóa FROM trong DELETE** | Có thể có hoặc không (`DELETE FROM tbl` hoặc `DELETE tbl`). | Có thể có hoặc không (`DELETE FROM tbl` hoặc `DELETE tbl`). |
| **Cập nhật đa cột từ Subquery** | Hỗ trợ: `SET (col1, col2) = (SELECT ...)`. | Không hỗ trợ gộp ngoặc đơn; phải gán từng cột riêng. |

---

## 4. Cạm bẫy thi cử trọng điểm (출제 함정 & 오답 노트)

1. **Bẫy cập nhật cột khóa trong ON của MERGE:**
   - *Đề thi:* Cho một câu lệnh `MERGE INTO tbl_a a USING tbl_b b ON (a.id = b.id) WHEN MATCHED THEN UPDATE SET a.id = b.new_id ...`.
   - *Bẫy:* Cố tình sửa cột `a.id` xuất hiện trong mệnh đề `ON`. Lệnh này **báo lỗi biên dịch ngay lập tức (`ORA-38104`)**.
2. **Bẫy số dòng của INSERT ALL vs INSERT FIRST:**
   - Khi các điều kiện `WHEN` có khoảng giá trị chồng lấn nhau (ví dụ: `sal >= 2000` và `sal >= 3000`), với `INSERT ALL`, một dòng lương 4000 sẽ được ghi vào cả hai bảng; còn với `INSERT FIRST`, dòng đó chỉ được ghi vào bảng đầu tiên.
3. **Bẫy NOT IN với Subquery chứa NULL:**
   - Khi nhìn thấy truy vấn dạng `WHERE col NOT IN (SELECT other_col FROM ...)`, điều đầu tiên cần kiểm tra ngay lập tức là: **Cột `other_col` có chứa giá trị `NULL` hay không?** Nếu có chứa dù chỉ 1 giá trị `NULL`, kết quả truy vấn chắc chắn là rỗng.
4. **Bẫy quên điều kiện WHERE trong UPDATE/DELETE:**
   - Không có `WHERE` đồng nghĩa với tác động lên 100% số hàng của bảng dữ liệu.

---

## 5. Câu hỏi trắc nghiệm thi thử mô phỏng (실전 기출 변형 문제 & 정답 해설)

#### Câu 1: Phân biệt cơ chế nạp dữ liệu đa bảng INSERT ALL và INSERT FIRST
Bảng nguồn `SRC_DATA` có 3 hàng dữ liệu với cột điểm số `SCORE` lần lượt là: `85`, `95`, `70`.
Thực thi câu lệnh SQL sau trên Oracle Database:
```sql
INSERT FIRST
    WHEN SCORE >= 90 THEN
        INTO HIGH_GRADE VALUES (SCORE)
    WHEN SCORE >= 80 THEN
        INTO MID_GRADE VALUES (SCORE)
    ELSE
        INTO LOW_GRADE VALUES (SCORE)
SELECT SCORE FROM SRC_DATA;
```
Hỏi tổng số hàng được chèn vào bảng `MID_GRADE` là bao nhiêu?
- A. 0 hàng
- B. 1 hàng
- C. 2 hàng
- D. 3 hàng

> **Đáp án chính xác:** **B**
>
> **Giải thích chi tiết:**
> - Câu lệnh sử dụng `INSERT FIRST` (cơ chế dừng ngay khi thỏa mãn điều kiện đầu tiên):
>   1. Xét dòng `SCORE = 85`:
>      - Nhánh 1: `SCORE >= 90` $\Rightarrow$ `FALSE`.
>      - Nhánh 2: `SCORE >= 80` $\Rightarrow$ `TRUE` $\Rightarrow$ Chèn vào bảng `MID_GRADE` (**1 hàng**). Dừng xử lý.
>   2. Xét dòng `SCORE = 95`:
>      - Nhánh 1: `SCORE >= 90` $\Rightarrow$ `TRUE` $\Rightarrow$ Chèn vào bảng `HIGH_GRADE`. Vì đây là `INSERT FIRST`, hệ thống **dừng lại ngay lập tức** và bỏ qua nhánh 2 (`SCORE >= 80`), dù 95 vẫn lớn hơn 80!
>   3. Xét dòng `SCORE = 70`:
>      - Nhánh 1: `FALSE`, Nhánh 2: `FALSE`, rơi vào nhánh `ELSE` $\Rightarrow$ Chèn vào `LOW_GRADE`.
> - Như vậy, chỉ có duy nhất bản ghi có điểm `85` được chèn vào `MID_GRADE`. Số hàng chèn vào `MID_GRADE` là **1**.
> - *(Lưu ý: Nếu câu lệnh trên sử dụng `INSERT ALL`, thì bản ghi `95` sẽ được chèn vào cả `HIGH_GRADE` và `MID_GRADE`, khi đó số hàng của `MID_GRADE` sẽ là 2)*.

---

#### Câu 2: Ràng buộc kỹ thuật trong câu lệnh MERGE
Xét câu lệnh `MERGE` sau đây trong Oracle Database:
```sql
MERGE INTO EMP_TARGET T
USING EMP_SOURCE S
ON (T.EMPNO = S.EMPNO)
WHEN MATCHED THEN
    UPDATE SET
        T.EMPNO = S.NEW_EMPNO,
        T.ENAME = S.ENAME,
        T.SAL   = S.SAL
    DELETE WHERE T.SAL < 1000
WHEN NOT MATCHED THEN
    INSERT (EMPNO, ENAME, SAL)
    VALUES (S.EMPNO, S.ENAME, S.SAL);
```
Điều gì sẽ xảy ra khi thực thi câu lệnh SQL trên?
- A. Câu lệnh thực thi thành công và đồng bộ dữ liệu vào bảng `EMP_TARGET`.
- B. Báo lỗi vì mệnh đề `DELETE` không được phép đi kèm trong nhánh `WHEN MATCHED`.
- C. Báo lỗi vì cột `T.EMPNO` tham gia trong mệnh đề `ON` không được phép cập nhật trong mệnh đề `SET`.
- D. Báo lỗi vì thiếu mệnh đề `WHERE` trong nhánh `WHEN NOT MATCHED`.

> **Đáp án chính xác:** **C**
>
> **Giải thích chi tiết:**
> - Trong cú pháp chuẩn của câu lệnh `MERGE`, các cột được sử dụng làm điều kiện nối trong mệnh đề `ON` (ở đây là `T.EMPNO`) đóng vai trò là khóa định danh liên kết giữa hai bảng.
> - Oracle quy định nghiêm ngặt rằng **không được phép cập nhật các cột xuất hiện trong mệnh đề ON** (`ORA-38104: Columns referenced in the ON Clause cannot be updated`).
> - Do câu lệnh cố tình gán `T.EMPNO = S.NEW_EMPNO` trong phần `UPDATE SET`, hệ thống sẽ chặn đứng và báo lỗi cú pháp.
> - Các phương án khác: Mệnh đề `DELETE` nằm sau `UPDATE` là hoàn toàn hợp lệ (B sai); nhánh `WHEN NOT MATCHED` không bắt buộc phải có `WHERE` (D sai).

---

#### Câu 3: Logic 3 giá trị với toán tử NOT IN và NULL
Bảng `DEPARTMENT` có dữ liệu các phòng ban với mã `DEPT_ID` gồm: `10`, `20`, `30`.
Bảng `PROJECT` có cột `DEPT_ID` phụ trách dự án gồm: `10`, `20`, và `NULL`.
Thực thi câu lệnh SQL sau:
```sql
SELECT COUNT(*)
FROM DEPARTMENT
WHERE DEPT_ID NOT IN (
    SELECT DEPT_ID
    FROM PROJECT
);
```
Kết quả trả về của câu lệnh là:
- A. 1
- B. 0
- C. 2
- D. 3

> **Đáp án chính xác:** **B**
>
> **Giải thích chi tiết:**
> - Subquery `SELECT DEPT_ID FROM PROJECT` trả về tập giá trị: `{10, 20, NULL}`.
> - Biểu thức ở mệnh đề lọc trở thành: `DEPT_ID NOT IN (10, 20, NULL)`.
> - Biểu thức này được triển khai theo logic logic 3 giá trị:
>   `(DEPT_ID <> 10) AND (DEPT_ID <> 20) AND (DEPT_ID <> NULL)`.
> - Phép so sánh `DEPT_ID <> NULL` luôn luôn trả về giá trị **`UNKNOWN`** với mọi giá trị của `DEPT_ID`.
> - Khi liên kết các phép toán qua toán tử `AND`: `[Kết quả] AND UNKNOWN` không bao giờ có thể đạt được giá trị `TRUE` (chỉ có thể ra `FALSE` hoặc `UNKNOWN`).
> - Do mệnh đề `WHERE` chỉ chọn các dòng có điều kiện đánh giá là `TRUE`, nên không có bất kỳ dòng nào của bảng `DEPARTMENT` được chọn.
> - Hàm `COUNT(*)` đếm số dòng thỏa mãn, kết quả trả về là **0**.

---

#### Câu 4: Cập nhật tương quan và câu lệnh UPDATE
Cho bảng `EMP` có 14 nhân viên thuộc các phòng ban 10, 20, 30.
Xét câu lệnh sau:
```sql
UPDATE EMP E
SET E.SAL = (
    SELECT MAX(M.SAL)
    FROM EMP M
    WHERE M.DEPTNO = E.DEPTNO
)
WHERE E.DEPTNO = 10;
```
Phát biểu nào sau đây là đúng về kết quả sau khi thực thi câu lệnh trên?
- A. Lương của tất cả 14 nhân viên trong công ty đều được cập nhật bằng mức lương cao nhất của phòng ban họ.
- B. Chỉ những nhân viên thuộc phòng ban 10 mới được cập nhật mức lương bằng lương cao nhất của phòng ban 10.
- C. Câu lệnh báo lỗi `ORA-01427` vì subquery trả về nhiều dòng dữ liệu.
- D. Câu lệnh không cập nhật dòng nào vì mệnh đề WHERE trong subquery không hợp lệ.

> **Đáp án chính xác:** **B**
>
> **Giải thích chi tiết:**
> - Mệnh đề `WHERE E.DEPTNO = 10` ở câu lệnh `UPDATE` ngoài cùng giới hạn phạm vi tác động: chỉ những hàng có `deptno = 10` mới được cập nhật (loại bỏ đáp án A).
> - Subquery `SELECT MAX(M.SAL) FROM EMP M WHERE M.DEPTNO = E.DEPTNO` sử dụng hàm tổng hợp `MAX`, luôn luôn trả về duy nhất đúng 1 giá trị vô hướng (Scalar Value) cho mỗi phòng ban, do đó không bao giờ gây ra lỗi nhiều dòng `ORA-01427` (loại bỏ đáp án C).
> - Do đó, toàn bộ nhân viên thuộc phòng ban 10 sẽ được cập nhật lương bằng đúng mức lương cao nhất hiện tại của phòng ban 10. Các phòng ban khác giữ nguyên trạng thái cũ.

---

## 6. Nối mạch sang Bài tiếp theo: TCL và Transaction

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 08 đã phân tích toàn bộ các công cụ DML biến đổi dữ liệu bản ghi (`INSERT`, `INSERT ALL/FIRST`, `UPDATE`, `DELETE`, `MERGE`) và ranh giới biểu thức tính toán logic `NULL`.
> - **Đang giải quyết gì:** Các lệnh DML này mới chỉ lưu tạm trong bộ nhớ đệm (Database Buffer Cache) và tạo khóa tài nguyên. Làm thế nào để đóng gói các thao tác này thành một đơn vị công việc logic toàn vẹn, xác nhận lưu vĩnh viễn hoặc khôi phục an toàn khi có sự cố?
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 09 — TCL và Transaction](./09-tcl-va-transaction.md) để khảo sát 4 thuộc tính ACID, cơ chế `COMMIT`, `ROLLBACK`, kịch bản chia nhỏ điểm lưu tạm `SAVEPOINT` và bẫy DDL ngầm định Auto-commit.
