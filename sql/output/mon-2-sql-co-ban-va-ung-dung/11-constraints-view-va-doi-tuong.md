<!-- lecture-contract: v2 -->
# Constraints, View và các đối tượng hỗ trợ

> **Mục tiêu:** Nắm vững 5 loại ràng buộc toàn vẹn dữ liệu (`PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, `CHECK`), cơ chế hoạt động của `VIEW`, bộ sinh số tự động `SEQUENCE` và bí danh đối tượng `SYNONYM`.
>
> **Phạm vi tham khảo:** PDF *2024 개정판 SQLD 개념정리*, trang 95–100.
>
> **Mạch kiến thức:** Bài trước đã hướng dẫn khởi tạo bảng (DDL). Bài này giải quyết câu hỏi: *Làm thế nào để bảo vệ tính toàn vẹn nghiệp vụ của dữ liệu và tối ưu hóa việc truy cập an toàn qua các đối tượng hỗ trợ?*

---

### 1. 제약 조건 (Constraints) — Cơ chế bảo vệ tính toàn vẹn dữ liệu

> **KR:** 제약 조건은 데이터의 무결성을 유지하기 위해 특정 컬럼에 설정하는 제약이며, 테이블에 부적절한 데이터가 입력되는 것을 방지하는 안전장치이다.

Ràng buộc (Constraints) là các quy tắc logic được áp đặt trực tiếp lên các cột trong bảng nhằm đảm bảo **tính toàn vẹn dữ liệu (Data Integrity)**:
- Có thể khai báo ngay lúc `CREATE TABLE` (cấp cột hoặc cấp bảng) hoặc bổ sung sau bằng `ALTER TABLE ... ADD CONSTRAINT`.
- Việc đặt tên tường minh cho ràng buộc (ví dụ: `CONSTRAINT pk_emp PRIMARY KEY`) giúp định vị chính xác lỗi khi bị vi phạm và thuận tiện cho việc bảo trì.

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
| **`PRIMARY KEY`** (Khóa chính) | Định danh duy nhất từng hàng trong bảng. Bắt buộc thỏa mãn đồng thời: **Không trùng lặp (Unique) và Không được rỗng (Not Null)**. | Mỗi bảng **chỉ có duy nhất 1 khóa chính**, nhưng khóa chính đó có thể gồm nhiều cột ghép lại (Composite Key). Khi tạo PK, hệ thống tự động sinh ra một `Unique Index`. |
| **`UNIQUE`** (Duy nhất) | Đảm bảo giá trị cột không bị trùng lặp giữa các hàng. | **Cho phép chứa giá trị `NULL`** (và có thể chứa nhiều giá trị `NULL` vì trong SQL, `NULL` không bằng `NULL`). Cũng tự động sinh `Unique Index`. |
| **`NOT NULL`** (Không rỗng) | Không cho phép cột mang giá trị `NULL`. | Đây là ràng buộc duy nhất được kế thừa khi nhân bản bảng bằng lệnh `CTAS`. |
| **`CHECK`** (Kiểm tra miền giá trị) | Giới hạn miền giá trị được phép nhập vào cột theo biểu thức logic (ví dụ: `sal >= 1000` hoặc `gender IN ('M', 'F')`). | Biểu thức `CHECK` không được chứa hàm trả về giá trị biến thiên theo thời gian (như `SYSDATE`) hoặc truy vấn con (Subquery). |
| **`FOREIGN KEY`** (Khóa ngoại) | Liên kết cột của bảng con với cột khóa chính (`PK`) hoặc `UNIQUE` của bảng cha để duy trì tính toàn vẹn tham chiếu. | Giá trị khóa ngoại phải **tồn tại ở bảng cha hoặc mang giá trị `NULL`**. |

---

### 3. Khóa ngoại và hành vi tham chiếu (Referential Actions)

> **KR:** FOREIGN KEY는 자식 테이블에 생성하며, 부모 테이블의 참조 컬럼은 반드시 PK 또는 UNIQUE KEY여야 한다. 자식 테이블에 데이터가 남아있는 경우 부모 데이터의 무단 삭제는 차단된다.

Khi dữ liệu ở bảng cha bị xóa hoặc cập nhật, khóa ngoại sẽ kích hoạt một trong các hành vi tham chiếu sau:

| Tùy chọn tham chiếu | Cú pháp ANSI / Oracle | Hành vi khi bản ghi cha bị xóa (`DELETE`) |
| --- | --- | --- |
| **Xóa dây chuyền** | `ON DELETE CASCADE` | Tự động **xóa toàn bộ các bản ghi con** đang trỏ tới bản ghi cha vừa bị xóa. |
| **Gán giá trị NULL** | `ON DELETE SET NULL` | Cập nhật cột khóa ngoại ở các bản ghi con thành `NULL` (cột con bắt buộc phải cho phép NULL). |
| **Chặn đứng thao tác** | `RESTRICT` / `NO ACTION` | **Ngăn chặn việc xóa bản ghi cha** nếu vẫn còn bất kỳ bản ghi con nào đang tham chiếu tới (mặc định nếu không khai báo). |

---

### 4. VIEW (Khung nhìn / Bảng ảo)

> **KR:** VIEW는 별도의 물리적 저장공간을 가지지 않고 SELECT 쿼리 정의만을 저장하는 가상 테이블(Virtual Table)이다.

```sql
CREATE [OR REPLACE] VIEW v_emp_dept AS
SELECT e.empno, e.ename, e.deptno, d.dname
FROM emp e
JOIN dept d ON e.deptno = d.deptno;
```

- **Ưu điểm của VIEW:**
  1. **Tính độc lập (Independence):** Ứng dụng độc lập với sự thay đổi của cấu trúc bảng nền tảng.
  2. **Tính tiện lợi (Convenience):** Tái sử dụng các câu lệnh truy vấn phức tạp nhiều bảng.
  3. **Tính bảo mật (Security):** Che giấu các cột nhạy cảm (như lương nhân viên, mật khẩu) đối với một số nhóm người dùng.
- **Hạn chế trong đề thi:**
  - View không có vùng nhớ lưu dữ liệu riêng biệt (dữ liệu nằm ở bảng gốc).
  - Không thể tạo Index trực tiếp trên View thông thường (trừ Materialized View / Indexed View).
  - Thao tác DML (`INSERT`, `UPDATE`, `DELETE`) trên View bị hạn chế nghiêm ngặt, đặc biệt đối với Complex View có chứa `JOIN`, `GROUP BY`, `DISTINCT` hoặc các hàm tổng hợp.

---

### 5. SEQUENCE (Bộ sinh số tự động)

> **KR:** SEQUENCE는 고유한 일련번호를 자동으로 생성하는 객체이며 주로 기본키(PK) 인조 식별자 생성에 사용된다.

```sql
CREATE SEQUENCE emp_seq
    START WITH 1001       -- Giá trị bắt đầu
    INCREMENT BY 1        -- Bước nhảy mỗi lần gọi
    MAXVALUE 999999       -- Giá trị tối đa
    NOCYCLE               -- Không quay vòng lặp lại
    CACHE 20;             -- Cấp phát trước 20 số vào RAM để tối ưu tốc độ
```

- **Sử dụng trong câu lệnh SQL:**
  - `emp_seq.NEXTVAL`: Cấp phát và trả về giá trị số tiếp theo.
  - `emp_seq.CURRVAL`: Trả về giá trị hiện tại vừa được cấp phát trong phiên làm việc (`Session`). Bắt buộc phải gọi `NEXTVAL` ít nhất một lần trước khi có thể gọi `CURRVAL`.

---

### 6. SYNONYM (Bí danh đối tượng)

> **KR:** SYNONYM은 특정 데이터베이스 객체에 대해 별칭을 부여하는 객체로, 객체의 실제 소유자(Owner)와 물리적 위치를 숨겨 보안성을 높이고 SQL 작성을 단순화한다.

```sql
-- Tạo bí danh riêng (Private Synonym)
CREATE SYNONYM emp FOR hr.employees;

-- Tạo bí danh công khai dùng cho toàn hệ thống (Cần quyền DBA)
CREATE PUBLIC SYNONYM all_emp FOR hr.employees;
```

- **Lợi ích:** Người dùng chỉ cần viết `SELECT * FROM emp` thay vì phải chỉ định tường minh tên chủ sở hữu `SELECT * FROM hr.employees`. Khi cấu trúc phân vùng hoặc tài khoản quản trị thay đổi, chỉ cần cập nhật lại định nghĩa của Synonym mà không cần sửa mã nguồn ứng dụng.

---

## 7. Nối mạch sang Bài tiếp theo: DCL, quyền và Role

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 11 đã phân tích trọn vẹn cách thiết lập các ràng buộc bảo vệ dữ liệu và hệ thống đối tượng hỗ trợ (`VIEW`, `SEQUENCE`, `SYNONYM`).
> - **Đang giải quyết gì:** Trong một môi trường doanh nghiệp có hàng trăm lập trình viên và nhân viên phân tích, ai được phép truy cập, ai được chỉnh sửa các bảng và đối tượng này? Làm thế nào để kiểm soát an ninh dữ liệu tập trung?
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 12 — DCL, quyền và Role](./12-dcl-quyen-va-role.md) để nắm vững cơ chế cấp quyền (`GRANT`), thu hồi quyền (`REVOKE`), quản trị nhóm quyền (`ROLE`) và các bẫy đề thi về `WITH GRANT OPTION` vs `WITH ADMIN OPTION`.
