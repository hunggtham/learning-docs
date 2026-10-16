<!-- lecture-contract: v2 -->
# Constraints, View và các đối tượng hỗ trợ

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Constraints, View và các đối tượng hỗ trợ**. Route đi từ 5 core constraints → Deferred constraints (`DEFERRABLE`) → `VIEW` options (`WITH CHECK OPTION`, `WITH READ ONLY`) → `SEQUENCE` and `SYNONYM`, thiết lập tầng bảo vệ toàn vẹn và bảo mật dữ liệu.

> **Mục tiêu:** Nắm vững 5 loại ràng buộc toàn vẹn dữ liệu, cơ chế hoãn kiểm tra ràng buộc (`DEFERRABLE INITIALLY DEFERRED` vs `IMMEDIATE`), kiểm soát DML qua View với `WITH CHECK OPTION` và `WITH READ ONLY`, bộ sinh số tự động `SEQUENCE` và bí danh `SYNONYM`.

> **Phạm vi tham khảo:** PDF *2024 개정판 SQLD 개념정리*, trang 95–100.

---

### 1. 제약 조건 (Constraints) — Cơ chế bảo vệ tính toàn vẹn dữ liệu

> **KR:** 제약 조건은 데이터의 무결성을 유지하기 위해 특정 컬럼에 설정하는 제약이며, 테이블에 부적절한 데이터가 입력되는 것을 방지하는 안전장치이다.

Ràng buộc (Constraints) là các quy tắc logic được áp đặt trực tiếp lên các cột trong bảng nhằm bảo vệ **tính toàn vẹn dữ liệu (Data Integrity)**:
- Có thể khai báo ngay lúc `CREATE TABLE` (cấp cột hoặc cấp bảng) hoặc bổ sung sau bằng `ALTER TABLE ... ADD CONSTRAINT`.
- Việc đặt tên tường minh cho ràng buộc (ví dụ: `CONSTRAINT pk_emp PRIMARY KEY`) giúp định vị chính xác lỗi khi bị vi phạm và thuận tiện cho việc bảo trì schema.

```sql
-- Khai báo khi tạo bảng
CREATE TABLE emp (
    empno NUMBER CONSTRAINT pk_emp PRIMARY KEY,
    ename VARCHAR2(20) NOT NULL,
    sal NUMBER CONSTRAINT ck_sal CHECK (sal > 0)
);

-- Thêm ràng buộc sau khi bảng đã tồn tại
ALTER TABLE emp ADD CONSTRAINT fk_emp_dept FOREIGN KEY (deptno) REFERENCES dept(deptno);

-- Xóa ràng buộc
ALTER TABLE emp DROP CONSTRAINT ck_sal;
```

---

### 2. Các loại ràng buộc cốt lõi trong đề thi SQLD

| Ràng buộc (Korean / English) | Định nghĩa & Tính chất kỹ thuật | Bẫy đề thi then chốt |
| :--- | :--- | :--- |
| **`PRIMARY KEY`** (Khóa chính) | Định danh duy nhất từng hàng. Thỏa mãn đồng thời: **Không trùng lặp (Unique) và Không rỗng (Not Null)**. | Mỗi bảng **chỉ có duy nhất 1 khóa chính** (có thể ghép từ nhiều cột). Hệ thống tự động sinh `Unique Index`. |
| **`UNIQUE`** (Duy nhất) | Đảm bảo giá trị cột không bị trùng lặp giữa các hàng. | **Cho phép chứa nhiều giá trị `NULL`** (vì trong SQL, `NULL` không bằng `NULL`). Cũng tự động sinh `Unique Index`. |
| **`NOT NULL`** (Không rỗng) | Không cho phép cột mang giá trị `NULL`. | Đây là ràng buộc duy nhất được kế thừa khi nhân bản bảng bằng lệnh `CTAS`. |
| **`CHECK`** (Kiểm tra miền giá trị) | Giới hạn miền giá trị theo biểu thức logic (ví dụ: `sal >= 1000` hoặc `gender IN ('M', 'F')`). | Biểu thức `CHECK` không được chứa hàm biến thiên theo thời gian (`SYSDATE`) hoặc truy vấn con (Subquery). |
| **`FOREIGN KEY`** (Khóa ngoại) | Liên kết cột bảng con với cột `PK` hoặc `UNIQUE` của bảng cha để duy trì toàn vẹn tham chiếu. | Giá trị khóa ngoại phải **tồn tại ở bảng cha hoặc mang giá trị `NULL`**. |

#### 2.1. Hành vi của giá trị NULL trong ràng buộc UNIQUE
- Trong chuẩn ANSI SQL và Oracle Database, `NULL` được định nghĩa là giá trị "chưa xác định" (unknown). Vì hai giá trị chưa xác định không thể kết luận là bằng nhau (`NULL = NULL` trả về `UNKNOWN`), nên:
  - Cột có ràng buộc `UNIQUE` **cho phép chèn vô số giá trị `NULL`** mà không hề vi phạm tính duy nhất.
  - Ngoại lệ: Trong Microsoft SQL Server (theo thiết lập mặc định truyền thống), ràng buộc `UNIQUE` chỉ cho phép duy nhất **1 giá trị `NULL`**. Muốn cho phép nhiều NULL như Oracle, kỹ sư SQL Server phải tạo một *Unique Filtered Index* (`WHERE col IS NOT NULL`).

#### 2.2. Hành vi của giá trị NULL trong ràng buộc CHECK (Bẫy 3-Valued Logic kinh điển)
- Trong SQL, biểu thức logic tuân theo đại số logic tam trị (Three-Valued Logic): `TRUE`, `FALSE`, hoặc `UNKNOWN`.
- Quy tắc kiểm tra của ràng buộc `CHECK`:
  > Ràng buộc `CHECK` chỉ ngăn chặn (từ chối bản ghi) khi và chỉ khi biểu thức điều kiện trả về kết quả là **`FALSE`**. Nếu biểu thức trả về `TRUE` hoặc `UNKNOWN`, bản ghi **hoàn toàn được chấp nhận**!
- **Ví dụ thực chiến:**
  ```sql
  CREATE TABLE emp_salary (
      empno NUMBER PRIMARY KEY,
      sal   NUMBER CONSTRAINT ck_sal CHECK (sal > 0)
  );

  -- Thao tác chèn bản ghi mang giá trị NULL:
  INSERT INTO emp_salary VALUES (1, NULL);
  ```
- **Hỏi:** Lệnh `INSERT` trên có thành công không?
- **Phân tích:** Khi thay `sal = NULL`, biểu thức `sal > 0` trở thành `NULL > 0`, kết quả trả về là **`UNKNOWN`**. Vì `UNKNOWN` không phải là `FALSE`, Oracle **chấp nhận lệnh chèn dữ liệu và giao dịch thành công rực rỡ**!
- **Bài học xương máu:** Muốn cột vừa thỏa mãn `sal > 0` vừa không được để trống, bắt buộc phải khai báo kết hợp cả hai: `sal NUMBER NOT NULL CHECK (sal > 0)`.

---

### 3. Cơ chế ràng buộc hoãn kiểm tra (Deferred Constraints)

Theo mặc định trong Oracle, tất cả các ràng buộc đều là `NOT DEFERRABLE`: hệ thống kiểm tra tính toàn vẹn ngay lập tức sau mỗi câu lệnh DML (`Immediate Enforcement`). Nếu vi phạm, câu lệnh bị lỗi và rollback tức thì.

Tuy nhiên, trong các tình huống thực tế như nạp dữ liệu hàng loạt (Batch Data Load) hoặc quan hệ tham chiếu vòng (Circular Foreign Keys giữa hai bảng), việc kiểm tra tức thì sẽ gây tắc nghẽn. Cơ chế hoãn kiểm tra (`DEFERRABLE`) cho phép dời thời điểm kiểm tra tính toàn vẹn đến tận khi phát lệnh `COMMIT`:

```sql
-- 1. DEFERRABLE INITIALLY IMMEDIATE:
-- Cho phép hoãn kiểm tra, nhưng mặc định vẫn kiểm tra tức thì sau mỗi câu lệnh DML.
ALTER TABLE emp ADD CONSTRAINT fk_emp_dept
FOREIGN KEY (deptno) REFERENCES dept(deptno)
DEFERRABLE INITIALLY IMMEDIATE;

-- Chuyển trạng thái sang hoãn kiểm tra trong phiên làm việc hiện tại:
SET CONSTRAINT fk_emp_dept DEFERRED;
-- Hoặc chuyển toàn bộ các ràng buộc có thể hoãn:
SET CONSTRAINTS ALL DEFERRED;

-- 2. DEFERRABLE INITIALLY DEFERRED:
-- Tự động hoãn kiểm tra toàn vẹn cho đến tận khi phát lệnh COMMIT.
ALTER TABLE dept ADD CONSTRAINT fk_dept_mgr
FOREIGN KEY (mgr_id) REFERENCES emp(empno)
DEFERRABLE INITIALLY DEFERRED;
```

#### Bảng so sánh các trạng thái kiểm tra ràng buộc

| Chế độ ràng buộc | Thời điểm kiểm tra mặc định | Cho phép chuyển trạng thái bằng `SET CONSTRAINT`? |
| --- | --- | --- |
| **`NOT DEFERRABLE`** | Tức thì sau mỗi câu lệnh DML (Mặc định của Oracle). | **KHÔNG** (báo lỗi ORA-02447 nếu cố hoãn). |
| **`DEFERRABLE INITIALLY IMMEDIATE`** | Tức thì sau mỗi câu lệnh DML. | **CÓ** (có thể chuyển sang `DEFERRED`). |
| **`DEFERRABLE INITIALLY DEFERRED`** | **Cuối giao dịch khi phát lệnh `COMMIT`**. | **CÓ** (có thể chuyển sang `IMMEDIATE`). |

> **Bẫy đề thi:** Với `INITIALLY DEFERRED`, trong suốt quá trình chạy giao dịch, bạn có thể chèn dữ liệu vi phạm khóa ngoại mà hệ thống không báo lỗi. Tuy nhiên, khi bạn gõ lệnh `COMMIT`, nếu dữ liệu vẫn chưa thỏa mãn ràng buộc, Oracle sẽ chặn đứng và tự động phát lệnh `ROLLBACK` toàn bộ giao dịch!

---

### 4. Khóa ngoại và hành vi tham chiếu (Referential Actions)

> **KR:** FOREIGN KEY는 자식 테이블에 생성하며, 부모 테이블의 참조 컬럼은 반드시 PK 또는 UNIQUE KEY여야 한다. 자식 테이블에 데이터가 남아있는 경우 부모 데이터의 무단 삭제는 차단된다.

Khi dữ liệu ở bảng cha bị xóa, khóa ngoại sẽ kích hoạt một trong các hành vi tham chiếu:

| Tùy chọn tham chiếu | Cú pháp ANSI / Oracle | Hành vi khi bản ghi cha bị xóa (`DELETE`) |
| --- | --- | --- |
| **Xóa dây chuyền** | `ON DELETE CASCADE` | Tự động **xóa toàn bộ các bản ghi con** đang trỏ tới bản ghi cha vừa bị xóa. |
| **Gán giá trị NULL** | `ON DELETE SET NULL` | Cập nhật cột khóa ngoại ở các bản ghi con thành `NULL` (cột con bắt buộc cho phép NULL). |
| **Chặn đứng thao tác** | `RESTRICT` / `NO ACTION` | **Ngăn chặn việc xóa bản ghi cha** nếu vẫn còn bất kỳ bản ghi con nào tham chiếu tới (mặc định). |

---

### 5. VIEW (Khung nhìn) và các tùy chọn kiểm soát DML

> **KR:** VIEW는 별도의 물리적 저장공간을 가지지 않고 SELECT 쿼리 정의만을 저장하는 가상 테이블(Virtual Table)이다.

```sql
CREATE [OR REPLACE] VIEW v_emp_dept AS
SELECT e.empno, e.ename, e.sal, e.deptno, d.dname
FROM emp e
JOIN dept d ON e.deptno = d.deptno;
```

#### Hai tùy chọn kiểm soát DML sống còn trong đề thi SQLD

#### 1. Tùy chọn `WITH CHECK OPTION`
Mặc định trên một Simple View, người dùng có thể thực hiện `INSERT` hoặc `UPDATE` các bản ghi làm cho bản ghi đó biến mất khỏi phạm vi hiển thị của View. Tùy chọn `WITH CHECK OPTION` ngăn chặn triệt để điều này:

```sql
CREATE VIEW v_emp_dept10 AS
SELECT empno, ename, sal, deptno
FROM emp
WHERE deptno = 10
WITH CHECK OPTION CONSTRAINT v_emp_dept10_ck;
```

- **Hành vi kiểm tra:** Mọi thao tác `INSERT` hoặc `UPDATE` thông qua `v_emp_dept10` bắt buộc phải thỏa mãn điều kiện `WHERE deptno = 10`.
- **Tình huống vi phạm:**
  ```sql
  -- Lệnh này sẽ bị Oracle chặn đứng ngay lập tức với lỗi ORA-01402!
  UPDATE v_emp_dept10
  SET deptno = 20
  WHERE empno = 7782;
  ```

#### 2. Tùy chọn `WITH READ ONLY`
Khóa cứng View thành đối tượng chỉ đọc tuyệt đối. Toàn bộ các thao tác làm biến đổi dữ liệu (`INSERT`, `UPDATE`, `DELETE`) thông qua View đều bị cấm hoàn toàn:

```sql
CREATE VIEW v_emp_readonly AS
SELECT empno, ename, sal, deptno
FROM emp
WITH READ ONLY;
```

- **Tình huống vi phạm:**
  ```sql
  -- Lệnh này sẽ báo lỗi ORA-42399: cannot perform a DML operation on a read-only view
  DELETE FROM v_emp_readonly WHERE empno = 7782;
  ```

#### 3. Phân biệt Simple View vs Complex View & Các điều kiện CẤM DML
Trong đề thi SQLD, việc nhận biết khi nào một View cho phép hoặc cấm thực hiện thao tác DML (`INSERT`, `UPDATE`, `DELETE`) là nội dung cực kỳ trọng tâm:

| Tiêu chí phân biệt | Simple View (단순 뷰) | Complex View (복합 뷰) |
| :--- | :--- | :--- |
| **Số lượng bảng gốc** | Đúng 1 bảng duy nhất | Từ 2 bảng trở lên (chứa JOIN) |
| **Hàm tổng hợp (`SUM`, `MAX`...)** | Tuyệt đối không có | Thường có chứa |
| **Mệnh đề `GROUP BY` / `HAVING`** | Tuyệt đối không có | Thường có chứa |
| **Từ khóa `DISTINCT`** | Tuyệt đối không có | Có thể có |
| **Thao tác DML (`INSERT`/`UPDATE`/`DELETE`)** | **Được phép** (trừ cột tính toán hoặc vi phạm NOT NULL) | **Bị cấm hoặc giới hạn rất khắt khe** |

#### Quy tắc cấm DML trên View cần ghi nhớ:
1. **Cấm hoàn toàn mọi DML (`INSERT`, `UPDATE`, `DELETE`):** Khi định nghĩa View có chứa bất kỳ yếu tố nào sau đây:
   - Hàm tổng hợp: `SUM()`, `AVG()`, `COUNT()`, `MAX()`, `MIN()`.
   - Mệnh đề gom nhóm: `GROUP BY` hoặc `HAVING`.
   - Loại bỏ trùng lặp: `DISTINCT`.
   - Toán tử tập hợp: `UNION`, `UNION ALL`, `INTERSECT`, `MINUS`.
   - Pseudocolumn hoặc Window Function: `ROWNUM`, `RANK() OVER(...)`.
2. **Quy tắc DML trên Join View (View nhiều bảng):**
   - Chỉ được phép thao tác DML trên bảng bảo toàn khóa (**Key-Preserved Table** - bảng mà khóa chính của nó vẫn duy trì tính duy nhất $1:1$ trong kết quả của View).
   - Tuyệt đối không thể đồng thời sửa đổi dữ liệu của 2 bảng khác nhau trong cùng một câu lệnh DML thông qua View.

---

### 6. SEQUENCE và SYNONYM

#### SEQUENCE (Bộ sinh số tự động)
> **KR:** SEQUENCE는 고유한 일련번호를 자동으로 생성하는 객체이며 주로 기본키(PK) 인조 식별자 생성에 사용된다.

```sql
CREATE SEQUENCE emp_seq
    START WITH 1001       -- Giá trị bắt đầu
    INCREMENT BY 1        -- Bước nhảy mỗi lần gọi
    MAXVALUE 999999       -- Giá trị tối đa
    NOCYCLE               -- Không quay vòng lặp lại
    CACHE 20;             -- Cấp phát trước 20 số vào RAM để tối ưu tốc độ
```

- `emp_seq.NEXTVAL`: Cấp phát và trả về giá trị số tiếp theo. Mỗi lần gọi sẽ làm bộ đếm tăng lên vĩnh viễn (dù transaction có bị `ROLLBACK`, số đã cấp phát cũng không được hoàn lại, tạo ra khoảng trống - gap).
- `emp_seq.CURRVAL`: Trả về giá trị hiện tại vừa được cấp phát trong cùng phiên làm việc (`Session`). Bắt buộc phải gọi `NEXTVAL` ít nhất một lần trong phiên đó trước khi có thể tham chiếu tới `CURRVAL`.

#### SYNONYM (Bí danh đối tượng)
> **KR:** SYNONYM은 특정 데이터베이스 객체에 대해 별칭을 부여하는 객체로, 객체의 실제 소유자(Owner)와 물리적 위치를 숨겨 보안성을 높이고 SQL 작성을 단순화한다.

```sql
-- Tạo bí danh riêng (Private Synonym - chỉ người tạo hoặc người được cấp quyền dùng)
CREATE SYNONYM emp FOR hr.employees;

-- Tạo bí danh công khai dùng cho toàn hệ thống (Cần đặc quyền DBA)
CREATE PUBLIC SYNONYM all_emp FOR hr.employees;

-- Xóa bí danh
DROP SYNONYM emp;
DROP PUBLIC SYNONYM all_emp;
```

---

## 7. Bảng ma trận so sánh Oracle vs SQL Server về Ràng buộc và Đối tượng

| Khía cạnh kỹ thuật | Oracle Database | Microsoft SQL Server | Điểm khác biệt thi cử SQLD |
| :--- | :--- | :--- | :--- |
| **Giá trị NULL trong UNIQUE** | Cho phép **vô số giá trị NULL** (chuẩn ANSI) | Mặc định chỉ cho phép **1 giá trị NULL duy nhất** | Bẫy lý thuyết so sánh giữa 2 hệ quản trị CSDL. |
| **Ràng buộc hoãn kiểm tra** | Hỗ trợ đầy đủ: `DEFERRABLE INITIALLY DEFERRED / IMMEDIATE` | **Không hỗ trợ** `DEFERRABLE` (luôn luôn kiểm tra tức thì Immediate) | Đề thi SQLD thường hỏi sâu cơ chế hoãn của Oracle. |
| **Tự động sinh số PK** | Dùng đối tượng độc lập **`SEQUENCE`** (hoặc `IDENTITY` từ 12c+) | Dùng thuộc tính cột **`IDENTITY(seed, increment)`** hoặc `SEQUENCE` (từ 2012+) | Oracle truyền thống dùng `seq.NEXTVAL`, SQL Server dùng `IDENTITY`. |
| **Biến đổi View** | `CREATE OR REPLACE VIEW` | `CREATE VIEW` / `ALTER VIEW` | Oracle hỗ trợ mệnh đề gộp `OR REPLACE`. |
| **Chỉ định chỉ đọc cho View** | Mệnh đề `WITH READ ONLY` | Dùng Trigger `INSTEAD OF` hoặc phân quyền chỉ `SELECT` | Tùy chọn `WITH READ ONLY` là đặc trưng nổi bật của Oracle. |
| **Kiểm soát DML trên View** | Mệnh đề `WITH CHECK OPTION` | Mệnh đề `WITH CHECK OPTION` | Cả hai DBMS hoàn toàn tương đồng về cơ chế chặn bản ghi vi phạm WHERE. |
| **Bí danh đối tượng** | Hỗ trợ `SYNONYM` và `PUBLIC SYNONYM` | Hỗ trợ `CREATE SYNONYM` (không có khái niệm Public Synonym riêng) | Oracle phân biệt rạch ròi Private và Public Synonym. |

---

## 8. Cạm bẫy thi cử trọng điểm (출제 함정 & 오답 노트)

> [!WARNING]
> Dưới đây là 5 cạm bẫy thi cử không thể bỏ qua về Ràng buộc và View:

### Cạm bẫy 1: Bẫy logic tam trị (Three-Valued Logic) của ràng buộc CHECK khi gặp NULL
- Ràng buộc `CHECK (sal >= 1000)`:
  - Nếu chèn `sal = 500`: $500 \ge 1000 \rightarrow \text{FALSE} \rightarrow$ **Bị chặn (Báo lỗi vi phạm ràng buộc)**.
  - Nếu chèn `sal = NULL`: $\text{NULL} \ge 1000 \rightarrow \text{UNKNOWN} \rightarrow$ **Được chấp nhận (Không báo lỗi!)**.
- Rất nhiều thí sinh mất điểm vì tưởng rằng dòng có `NULL` sẽ bị từ chối. Ràng buộc `CHECK` **chỉ chặn khi biểu thức lượng giá là FALSE**.

### Cạm bẫy 2: Sao chép bảng bằng `CTAS` làm rơi rụng hầu hết các ràng buộc
- Khi sử dụng cú pháp sao chép bảng:
  ```sql
  CREATE TABLE emp_copy AS SELECT * FROM emp;
  ```
- **Sự thật thi cử:** Chỉ có duy nhất ràng buộc **`NOT NULL`** được sao chép sang bảng mới! Toàn bộ các ràng buộc `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `CHECK` và các chỉ mục `INDEX` đều **bị biến mất hoàn toàn**!

### Cạm bẫy 3: Tham chiếu `CURRVAL` trước khi gọi `NEXTVAL` trong phiên
- Trong một phiên làm việc mới kết nối (New Session):
  ```sql
  -- LỖI NGAY LẬP TỨC: ORA-08002: sequence EMP_SEQ.CURRVAL is not yet defined in this session!
  SELECT emp_seq.CURRVAL FROM dual;
  ```
- `CURRVAL` lưu trữ giá trị số vừa được cấp phát **trong chính phiên hiện tại**. Bắt buộc phải thực hiện ít nhất một lần `emp_seq.NEXTVAL` thì mới có thể sử dụng `CURRVAL`.

### Cạm bẫy 4: Lầm tưởng thao tác DML trên View chỉ ảnh hưởng tới View
- View là một bảng ảo, không hề có vùng nhớ lưu trữ dữ liệu riêng.
- Mọi thao tác `INSERT`, `UPDATE`, `DELETE` thực thi thành công thông qua View đều **tác động trực tiếp và làm thay đổi vĩnh viễn dữ liệu trên bảng vật lý bên dưới (Base Table)**!

### Cạm bẫy 5: Nhầm lẫn giữa xóa View (`DROP VIEW`) và xóa bảng gốc
- Thực hiện lệnh: `DROP VIEW v_emp;`
- Chỉ có định nghĩa của View bị xóa khỏi hệ thống Từ điển dữ liệu (`Data Dictionary`).
- Toàn bộ dữ liệu vật lý và cấu trúc của bảng gốc `emp` **vẫn hoàn toàn nguyên vẹn, không hề bị ảnh hưởng**!

---

## 9. Câu hỏi trắc nghiệm thi thử mô phỏng (실전 기출 변형 문제 & 정답 해설)

### Câu 1: Hành vi kiểm tra giá trị NULL của ràng buộc CHECK (Độ khó: Cao)
Xét định nghĩa bảng sau trong cơ sở dữ liệu Oracle:

```sql
CREATE TABLE TB_EMP (
    EMPNO NUMBER(4) CONSTRAINT PK_TB_EMP PRIMARY KEY,
    ENAME VARCHAR2(20),
    SAL NUMBER(7,2) CONSTRAINT CK_SAL CHECK (SAL BETWEEN 1000 AND 5000),
    COMM NUMBER(7,2) CONSTRAINT CK_COMM CHECK (COMM > 0)
);
```

Người dùng lần lượt thực hiện 4 thao tác `INSERT` độc lập dưới đây. Hỏi thao tác nào sẽ **BỊ HỆ THỐNG TỪ CHỐI (Báo lỗi vi phạm ràng buộc)**?

A. `INSERT INTO TB_EMP VALUES (1001, 'KIM', 2000, 100);`
B. `INSERT INTO TB_EMP VALUES (1002, 'LEE', NULL, 200);`
C. `INSERT INTO TB_EMP VALUES (1003, 'PARK', 3000, NULL);`
D. `INSERT INTO TB_EMP VALUES (1004, 'CHOI', 500, 300);`

> **Đáp án chính xác:** **D**
>
> **Giải thích chi tiết từng lựa chọn:**
> - Ràng buộc `CK_SAL` kiểm tra `SAL BETWEEN 1000 AND 5000`.
> - Ràng buộc `CK_COMM` kiểm tra `COMM > 0`.
> - **Lựa chọn A:** `SAL = 2000` (TRUE), `COMM = 100` (TRUE) $\rightarrow$ Hợp lệ, chèn thành công.
> - **Lựa chọn B:** `SAL = NULL` khiến biểu thức `NULL BETWEEN 1000 AND 5000` trả về **`UNKNOWN`**. Vì kết quả không phải là `FALSE`, ràng buộc CHECK không kích hoạt chặn. Cột không có `NOT NULL` nên chèn thành công!
> - **Lựa chọn C:** `COMM = NULL` khiến `NULL > 0` trả về **`UNKNOWN`** $\rightarrow$ Không phải `FALSE`, chèn thành công!
> - **Lựa chọn D:** `SAL = 500` khiến biểu thức `500 BETWEEN 1000 AND 5000` trả về kết quả rõ ràng là **`FALSE`**! Oracle lập tức chặn đứng thao tác và ném lỗi `ORA-02290: check constraint (CK_SAL) violated`.
> - Do đó thao tác D bị từ chối.

---

### Câu 2: Thao tác DML trên View có tùy chọn WITH CHECK OPTION (Độ khó: Trung bình)
Cho bảng `EMP` và View `V_EMP_D20` được định nghĩa như sau:

```sql
CREATE VIEW V_EMP_D20 AS
SELECT EMPNO, ENAME, SAL, DEPTNO
FROM EMP
WHERE DEPTNO = 20
WITH CHECK OPTION CONSTRAINT CK_V_EMP_D20;
```

Phát biểu nào sau đây là **ĐÚNG** về các thao tác thông qua View `V_EMP_D20`?

A. Thao tác `DELETE FROM V_EMP_D20 WHERE DEPTNO = 20;` sẽ bị hệ thống chặn đứng vì tùy chọn WITH CHECK OPTION cấm xóa dữ liệu.
B. Thao tác `UPDATE V_EMP_D20 SET DEPTNO = 30 WHERE EMPNO = 7788;` sẽ bị hệ thống báo lỗi vi phạm ràng buộc CHECK OPTION.
C. Thao tác `INSERT INTO V_EMP_D20 VALUES (9001, 'JANE', 3000, 10);` vẫn thực hiện thành công và bản ghi mới sẽ thuộc phòng 10.
D. Người dùng không thể thực hiện bất kỳ câu lệnh DML nào vì View mặc định là chỉ đọc.

> **Đáp án chính xác:** **B**
>
> **Giải thích chi tiết từng lựa chọn:**
> - **Bản chất của `WITH CHECK OPTION`:** Ngăn chặn các câu lệnh `INSERT` hoặc `UPDATE` làm cho dòng dữ liệu không còn thỏa mãn điều kiện `WHERE` của View (tức `DEPTNO = 20`).
> - **Lựa chọn B đúng:** Cập nhật `DEPTNO = 30` khiến bản ghi biến mất khỏi phạm vi `DEPTNO = 20`, vi phạm trực tiếp ràng buộc `WITH CHECK OPTION` $\rightarrow$ Báo lỗi `ORA-01402`.
> - **Lựa chọn A sai:** `WITH CHECK OPTION` không cấm lệnh `DELETE`. Việc xóa các bản ghi thuộc phòng 20 hoàn toàn hợp lệ.
> - **Lựa chọn C sai:** Chèn bản ghi với `DEPTNO = 10` vi phạm điều kiện `DEPTNO = 20` của View nên sẽ bị chặn đứng ngay lập tức.
> - **Lựa chọn D sai:** Muốn cấm mọi DML phải dùng tùy chọn `WITH READ ONLY`.

---

### Câu 3: Kế thừa ràng buộc khi nhân bản bảng bằng CTAS (Độ khó: Dễ)
Một lập trình viên tạo bảng mới bằng câu lệnh sau:

```sql
CREATE TABLE EMP_BACKUP AS
SELECT * FROM EMP;
```

Giả sử bảng gốc `EMP` có đầy đủ 5 ràng buộc: `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, và `CHECK`. Hỏi những ràng buộc nào sẽ **ĐƯỢC KẾ THỪA** sang bảng mới `EMP_BACKUP`?

A. Toàn bộ 5 ràng buộc đều được kế thừa nguyên vẹn.
B. Chỉ có `PRIMARY KEY` và `FOREIGN KEY`.
C. Chỉ có duy nhất ràng buộc `NOT NULL`.
D. Không có bất kỳ ràng buộc nào được kế thừa.

> **Đáp án chính xác:** **C**
>
> **Giải thích chi tiết từng lựa chọn:**
> - Trong Oracle SQL, câu lệnh `CREATE TABLE ... AS SELECT` (CTAS) chỉ sao chép cấu trúc cột, kiểu dữ liệu và nội dung dữ liệu.
> - Ràng buộc duy nhất được hệ thống giữ lại là **`NOT NULL`** (vì nó gắn liền với định nghĩa kiểu dữ liệu của cột).
> - Tất cả các ràng buộc khác (`PK`, `FK`, `UNIQUE`, `CHECK`), các giá trị mặc định phức tạp và chỉ mục Index đều không được kế thừa, người quản trị phải tự tạo lại bằng lệnh `ALTER TABLE`.
> - **Lựa chọn C:** Hoàn toàn chính xác.

---

### Câu 4: Nhận diện trường hợp cấm DML trên View (Độ khó: Trung bình)
View nào dưới đây **KHÔNG THỂ** thực hiện bất kỳ thao tác DML (`INSERT`, `UPDATE`, `DELETE`) nào?

A. `CREATE VIEW V1 AS SELECT EMPNO, ENAME, SAL FROM EMP WHERE SAL > 2000;`
B. `CREATE VIEW V2 AS SELECT DEPTNO, SUM(SAL) AS TOTAL_SAL FROM EMP GROUP BY DEPTNO;`
C. `CREATE VIEW V3 AS SELECT EMPNO, ENAME, DEPTNO FROM EMP WHERE DEPTNO = 10 WITH CHECK OPTION;`
D. `CREATE VIEW V4 AS SELECT EMPNO, ENAME, COMM FROM EMP WHERE COMM IS NOT NULL;`

> **Đáp án chính xác:** **B**
>
> **Giải thích chi tiết từng lựa chọn:**
> - **Lựa chọn B:** View `V2` chứa hàm tổng hợp `SUM(SAL)` và mệnh đề gom nhóm `GROUP BY DEPTNO`. Đây là một **Complex View** (View tổng hợp). Mỗi dòng trong View đại diện cho cả một nhóm nhiều bản ghi của bảng gốc, do đó hệ thống không thể ánh xạ một thao tác DML ngược về từng dòng vật lý riêng rẽ $\rightarrow$ Cấm tuyệt đối mọi thao tác DML!
> - **Lựa chọn A, C, D:** Đều là các Simple View dựa trên đúng 1 bảng `EMP`, không có hàm nhóm, không có GROUP BY hay DISTINCT nên hoàn toàn cho phép thực hiện DML hợp lệ.

---

## 10. Nối mạch sang Bài tiếp theo: DCL, quyền và Role

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 11 đã phân tích trọn vẹn cách thiết lập các ràng buộc bảo vệ dữ liệu (`PK`, `FK`, `DEFERRABLE`), cơ chế 3-valued logic của `CHECK`, các góc nhìn bảo mật qua `VIEW` (`WITH CHECK OPTION`, `WITH READ ONLY`, giới hạn DML trên Complex View) và các đối tượng `SEQUENCE`, `SYNONYM`.
> - **Đang giải quyết gì:** Trong một môi trường doanh nghiệp có nhiều phòng ban, ai được cấp quyền kết nối hệ thống (`CREATE SESSION`), ai được thao tác trên bảng (`SELECT`, `UPDATE`), và làm thế nào để quản trị an ninh tập trung qua `ROLE`?
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 12 — DCL, quyền và Role](./12-dcl-quyen-va-role.md) để phân biệt rạch ròi giữa Quyền hệ thống và Quyền đối tượng, cùng cơ chế thu hồi dây chuyền của `WITH GRANT OPTION` vs `WITH ADMIN OPTION`.
