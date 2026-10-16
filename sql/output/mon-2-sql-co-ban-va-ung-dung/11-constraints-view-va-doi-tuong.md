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
| --- | --- | --- |
| **`PRIMARY KEY`** (Khóa chính) | Định danh duy nhất từng hàng. Thỏa mãn đồng thời: **Không trùng lặp (Unique) và Không rỗng (Not Null)**. | Mỗi bảng **chỉ có duy nhất 1 khóa chính** (có thể ghép từ nhiều cột). Hệ thống tự động sinh `Unique Index`. |
| **`UNIQUE`** (Duy nhất) | Đảm bảo giá trị cột không bị trùng lặp giữa các hàng. | **Cho phép chứa nhiều giá trị `NULL`** (vì trong SQL, `NULL` không bằng `NULL`). Cũng tự động sinh `Unique Index`. |
| **`NOT NULL`** (Không rỗng) | Không cho phép cột mang giá trị `NULL`. | Đây là ràng buộc duy nhất được kế thừa khi nhân bản bảng bằng lệnh `CTAS`. |
| **`CHECK`** (Kiểm tra miền giá trị) | Giới hạn miền giá trị theo biểu thức logic (ví dụ: `sal >= 1000` hoặc `gender IN ('M', 'F')`). | Biểu thức `CHECK` không được chứa hàm biến thiên theo thời gian (`SYSDATE`) hoặc truy vấn con (Subquery). |
| **`FOREIGN KEY`** (Khóa ngoại) | Liên kết cột bảng con với cột `PK` hoặc `UNIQUE` của bảng cha để duy trì toàn vẹn tham chiếu. | Giá trị khóa ngoại phải **tồn tại ở bảng cha hoặc mang giá trị `NULL`**. |

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

- `emp_seq.NEXTVAL`: Cấp phát và trả về giá trị số tiếp theo.
- `emp_seq.CURRVAL`: Trả về giá trị hiện tại vừa được cấp phát trong phiên (`Session`). Bắt buộc phải gọi `NEXTVAL` ít nhất một lần trước khi có thể gọi `CURRVAL`.

#### SYNONYM (Bí danh đối tượng)
> **KR:** SYNONYM은 특정 데이터베이스 객체에 대해 별칭을 부여하는 객체로, 객체의 실제 소유자(Owner)와 물리적 위치를 숨겨 보안성을 높이고 SQL 작성을 단순화한다.

```sql
-- Tạo bí danh riêng (Private Synonym)
CREATE SYNONYM emp FOR hr.employees;

-- Tạo bí danh công khai dùng cho toàn hệ thống (Cần quyền DBA)
CREATE PUBLIC SYNONYM all_emp FOR hr.employees;
```

---

## 7. Nối mạch sang Bài tiếp theo: DCL, quyền và Role

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 11 đã phân tích trọn vẹn cách thiết lập các ràng buộc bảo vệ dữ liệu (`PK`, `FK`, `DEFERRABLE`), các góc nhìn bảo mật qua `VIEW` (`WITH CHECK OPTION`, `WITH READ ONLY`) và các đối tượng `SEQUENCE`, `SYNONYM`.
> - **Đang giải quyết gì:** Trong một môi trường doanh nghiệp có nhiều phòng ban, ai được cấp quyền kết nối hệ thống (`CREATE SESSION`), ai được thao tác trên bảng (`SELECT`, `UPDATE`), và làm thế nào để quản trị an ninh tập trung qua `ROLE`?
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 12 — DCL, quyền và Role](./12-dcl-quyen-va-role.md) để phân biệt rạch ròi giữa Quyền hệ thống và Quyền đối tượng, cùng cơ chế thu hồi dây chuyền của `WITH GRANT OPTION` vs `WITH ADMIN OPTION`.
