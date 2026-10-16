<!-- lecture-contract: v2 -->
# DDL và định nghĩa bảng (Data Definition Language)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **DDL và định nghĩa bảng**. Route đi từ data types → naming rules → `CREATE TABLE` / `CTAS` → `ALTER TABLE` operations → Deep comparison: `TRUNCATE` vs `DROP` vs `DELETE` on High Water Mark (HWM) and Tablespace.

> **Mục tiêu:** Nắm vững các kiểu dữ liệu cốt lõi, quy tắc đặt tên đối tượng, cú pháp `CREATE TABLE`, kỹ thuật nhân bản `CTAS` (thuộc tính kế thừa và không kế thừa), các thao tác hiệu chỉnh `ALTER TABLE`, và phân biệt bản chất giải phóng High Water Mark (HWM) cùng Tablespace giữa `TRUNCATE`, `DROP`, `DELETE`.

> **Phạm vi tham khảo:** PDF *2024 개정판 SQLD 개념정리*, trang 90–94.

---

### 1. DDL (Data Definition Language) — Ngôn ngữ định nghĩa dữ liệu

> **KR:** DDL은 데이터의 구조를 정의하는 언어로 객체 생성, 삭제, 변경에 사용하며 AUTO COMMIT이라 ROLLBACK이 불가하다.

DDL chịu trách nhiệm định nghĩa cấu trúc lưu trữ và các đối tượng CSDL (bảng, khung nhìn, chỉ mục, schema...).
- **Đặc tính sống còn trong đề thi:** Trong Oracle, các câu lệnh DDL mang cơ chế **AUTO-COMMIT** ngầm định. Khi lệnh DDL thực thi, hệ thống tự động phát lệnh `COMMIT` trước và sau thao tác. Mọi thay đổi được ghi nhận vĩnh viễn vào từ điển dữ liệu (Data Dictionary) và **hoàn toàn không thể ROLLBACK**.
- **Các lệnh chính:** `CREATE` (tạo mới đối tượng), `ALTER` (sửa đổi cấu trúc), `DROP` (xóa bỏ đối tượng), `TRUNCATE` (xóa trắng dữ liệu, giải phóng bộ nhớ, giữ lại khung bảng).

---

### 2. 데이터 유형 (Data Types) — Các kiểu dữ liệu cơ bản

| Kiểu dữ liệu (Korean / English) | Đặc tính kỹ thuật | Điểm thi trọng tâm |
| --- | --- | --- |
| **`CHAR(n)`** (Độ dài cố định) | Chiếm trọn vẹn đúng $n$ byte. Nếu chuỗi ngắn hơn, hệ thống tự động đệm khoảng trắng (`Blank Padded`) vào cuối. | Khi so sánh hai chuỗi `CHAR`, khoảng trắng ở đuôi được bỏ qua (`'A' = 'A '` là TRUE). |
| **`VARCHAR2(n)`** (Độ dài biến đổi) | Chỉ chiếm dung lượng thực tế của chuỗi ký tự được nạp, tối đa $n$ byte. Tiết kiệm bộ nhớ. | Khi so sánh `VARCHAR2`, ký tự khoảng trắng được tính là một ký tự hợp lệ (`'A' = 'A '` là FALSE). |
| **`NUMBER(p, s)`** (Kiểu số) | $p$ (Precision): Tổng số chữ số; $s$ (Scale): Số chữ số sau dấu phẩy thập phân. | `NUMBER(6, 2)` chứa tối đa 4 chữ số nguyên và 2 chữ số thập phân (ví dụ: `1234.56`). |
| **`DATE` / `DATETIME`** (Ngày giờ) | Lưu trữ cả thông tin ngày, tháng, năm và giờ, phút, giây. | Không cần khai báo kích thước độ dài khi định nghĩa cột. |

---

### 3. CREATE TABLE과 명명 규칙 — Tạo bảng và quy tắc đặt tên

> **KR:** 테이블명은 적절한 단수형 이름을 사용하고, 테이블과 컬럼명은 반드시 문자로 시작하며 A-Z, a-z, 0-9, _, $, #만 허용된다.

```sql
CREATE TABLE [schema.]table_name (
    column_name data_type [DEFAULT default_value] [constraints],
    ...
);
```

#### Quy tắc đặt tên đối tượng trong đề thi SQLD
- Tên bảng và tên cột bắt buộc phải **bắt đầu bằng một chữ cái** (không bắt đầu bằng chữ số hoặc ký tự đặc biệt).
- Chỉ được chứa các ký tự: chữ cái (`A-Z`, `a-z`), chữ số (`0-9`), và 3 ký tự đặc biệt: gạch dưới `_`, dấu đô la `$`, dấu thăng `#`.
- Không được trùng lặp với **Từ khóa dành riêng (Reserved Words)** của hệ thống (như `SELECT`, `FROM`, `ORDER`...).
- Trong cùng một bảng, không được phép có hai cột trùng tên nhau.

---

### 4. CTAS (Create Table As Select) — Tạo bảng từ kết quả truy vấn

> **KR:** CTAS는 이미 만들어진 테이블을 활용해서 테이블을 재생성하며, 구조뿐 아니라 데이터도 복제할 수 있다. 단, NOT NULL을 제외한 PK, FK, UNIQUE 등 제약조건은 복제되지 않는다.

Kỹ thuật CTAS cho phép tạo nhanh bảng mới dựa trên tập kết quả của một câu lệnh `SELECT`. Cú pháp hỗ trợ gán lại danh sách tên cột mới và tính toán biểu thức:

```sql
-- 1. Cú pháp chuẩn tạo bảng kèm đặt tên cột mới và tính toán
CREATE TABLE dept_sal_summary (deptno, total_sal, avg_sal)
AS
SELECT deptno, SUM(sal), ROUND(AVG(sal), 2)
FROM emp
GROUP BY deptno;

-- 2. Sao chép toàn bộ cấu trúc và dữ liệu từ bảng gốc
CREATE TABLE emp_copy AS
SELECT * FROM emp;

-- 3. Kỹ thuật tạo khung bảng rỗng (Empty Table Skeleton)
CREATE TABLE emp_skeleton AS
SELECT * FROM emp
WHERE 1 = 2; -- Mệnh đề luôn False để không lấy bất kỳ bản ghi nào
```

#### Bảng phân tích thuộc tính kế thừa và không kế thừa trong CTAS

| Thuộc tính schema | Kế thừa vào bảng mới? | Giải thích kỹ thuật & Cách khắc phục |
| --- | --- | --- |
| **Tên và Kiểu dữ liệu cột** | **CÓ** | Tự động ánh xạ kiểu dữ liệu (`VARCHAR2`, `NUMBER`, `DATE`...). |
| **Dữ liệu các bản ghi** | **CÓ** | Sao chép toàn bộ hàng thỏa mãn mệnh đề `WHERE` của truy vấn con. |
| **Ràng buộc `NOT NULL`** | **CÓ** | Đây là **ràng buộc duy nhất** được tự động kế thừa từ bảng nguồn. |
| **Khóa chính `PRIMARY KEY`** | **KHÔNG** | Phải dùng `ALTER TABLE ... ADD CONSTRAINT` để tạo lại sau đó. |
| **Khóa ngoại `FOREIGN KEY`** | **KHÔNG** | Mối quan hệ tham chiếu bị cắt đứt; phải khai báo thủ công. |
| **Ràng buộc `UNIQUE` & `CHECK`** | **KHÔNG** | Toàn bộ quy tắc miền giá trị và tính duy nhất không được sao chép. |
| **Chỉ mục (`INDEX`)** | **KHÔNG** | Bảng mới hoàn toàn không có Index, phải tạo mới bằng `CREATE INDEX`. |

---

### 5. ALTER TABLE — Hiệu chỉnh cấu trúc bảng

Sau khi bảng đã được tạo, ta sử dụng `ALTER TABLE` để thêm, sửa hoặc xóa cột và ràng buộc:

> **KR:** ALTER는 테이블의 구조 변경에 사용하며, 컬럼 추가 시 새로운 컬럼은 테이블의 맨 마지막에 위치하고 순서 변경은 불가능하다.

```sql
-- 1. Thêm cột mới (Luôn nằm ở vị trí cuối cùng của bảng)
ALTER TABLE emp ADD (dept_name VARCHAR2(50), hire_reason VARCHAR2(100));

-- 2. Hiệu chỉnh cột (Đổi kiểu dữ liệu hoặc tăng/giảm kích thước)
ALTER TABLE emp MODIFY (dept_name VARCHAR2(100) DEFAULT 'IT' NOT NULL);

-- 3. Đổi tên cột và đổi tên bảng
ALTER TABLE emp RENAME COLUMN hire_reason TO reason;
RENAME emp TO employees;

-- 4. Xóa cột khỏi bảng
ALTER TABLE employees DROP COLUMN reason;
```

#### Các quy tắc kiểm tra ràng buộc khi `ALTER` trong đề thi
- **Tăng kích thước cột:** Luôn luôn thực hiện được dù bảng đã có dữ liệu hay chưa.
- **Giảm kích thước cột:** Chỉ thực hiện được nếu kích thước mới vẫn lớn hơn hoặc bằng chiều dài tối đa của dữ liệu hiện có trong cột (hoặc cột hoàn toàn rỗng).
- **Đổi kiểu dữ liệu:** Chỉ an toàn và được phép khi cột hoàn toàn không có dữ liệu (hoặc toàn bộ giá trị là `NULL`). Ngoại lệ: `CHAR` và `VARCHAR2` có thể chuyển đổi tương hỗ nếu kích thước chứa đủ dữ liệu.
- **Thêm ràng buộc `NOT NULL`:** Chỉ thành công nếu cột đó hiện không chứa bất kỳ giá trị `NULL` nào.

---

### 6. So sánh chi tiết DROP vs TRUNCATE vs DELETE trên High Water Mark và Tablespace

Để hiểu sâu bản chất vận hành của cơ sở dữ liệu, cần đối chiếu 3 câu lệnh này qua lăng kính quản lý vùng nhớ và chỉ số **High Water Mark (HWM - 고수위 마크)**.

#### High Water Mark (HWM) là gì?
- Trong kiến trúc lưu trữ Oracle, một bảng (`Table Segment`) được cấu thành từ nhiều `Extent`, mỗi Extent gồm nhiều khối dữ liệu (`Data Block`).
- **HWM là con trỏ biên giới hạn khối dữ liệu cao nhất đã từng được nạp dữ liệu** bên trong Segment.
- Khi dữ liệu được thêm vào, HWM di chuyển tịnh tiến lên.
- **Nguyên lý quét bảng toàn bộ (Full Table Scan):** Khi câu lệnh `SELECT * FROM table` thực thi mà không dùng Index, Oracle Engine bắt buộc phải quét tuần tự toàn bộ các khối dữ liệu từ khối đầu tiên **cho đến tận đỉnh High Water Mark**, bất kể các khối bên dưới HWM đang chứa dữ liệu hay đã bị xóa rỗng!

#### Bảng so sánh chuyên sâu giữa DELETE, TRUNCATE và DROP

| Tiêu chí | `DELETE` | `TRUNCATE` | `DROP` |
| --- | --- | --- | --- |
| **Phân loại lệnh** | **DML** (Thao tác dữ liệu) | **DDL** (Định nghĩa dữ liệu) | **DDL** (Định nghĩa dữ liệu) |
| **Phạm vi tác động** | Xóa từng hàng (hỗ trợ `WHERE`) | Xóa toàn bộ dữ liệu bảng (không có `WHERE`) | Xóa toàn bộ cấu trúc và dữ liệu bảng |
| **Khung bảng (Structure)** | Vẫn giữ nguyên vẹn | Vẫn giữ nguyên vẹn (kiểm tra bằng `DESC`) | Bị xóa hoàn toàn khỏi Data Dictionary |
| **Tác động High Water Mark** | **HWM KHÔNG THAY ĐỔI** (Giữ nguyên đỉnh cũ) | **RESET HWM về 0** (Về mức khởi tạo ban đầu) | Hủy bỏ Segment, không còn HWM |
| **Giải phóng Tablespace** | **Không giải phóng** Extent về Tablespace | **Giải phóng toàn bộ Extent** (chỉ giữ Initial Extent) | Giải phóng toàn bộ dung lượng về Tablespace |
| **Hiệu năng quét sau khi xóa** | Chậm (Full Table Scan vẫn quét hết block rác đến HWM) | Cực nhanh (Full Table Scan chỉ quét vài block ban đầu) | Không thể truy vấn (bảng không còn) |
| **Khả năng ROLLBACK** | **Có thể ROLLBACK** (ghi đầy đủ Undo/Redo) | **KHÔNG THỂ ROLLBACK** (Auto-Commit) | **KHÔNG THỂ ROLLBACK** (Auto-Commit) |

> **Bẫy thực tế nghiệp vụ:** Nếu một bảng có 10 triệu bản ghi, bạn chạy lệnh `DELETE FROM table;`:
> 1. Thời gian chạy rất lâu vì phải ghi Undo Log cho từng dòng để hỗ trợ `ROLLBACK`.
> 2. Dung lượng ổ đĩa của Tablespace không giảm một byte nào.
> 3. HWM vẫn nằm ở đỉnh 10 triệu bản ghi. Câu lệnh `SELECT COUNT(*)` sau đó sẽ chạy rất chậm vì hệ thống vẫn phải đọc qua hàng trăm nghìn block trống cho đến đỉnh HWM!
> Trái lại, lệnh `TRUNCATE TABLE table;` xử lý ngay tức thì, giải phóng dung lượng trả lại cho Tablespace và đưa HWM về vị trí ban đầu.

---

## 7. Nối mạch sang Bài tiếp theo: Ràng buộc, Khung nhìn và Đối tượng hỗ trợ

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 10 đã trang bị đầy đủ cú pháp khởi tạo bảng, kiểu dữ liệu, kỹ thuật `CTAS`, cơ chế biến đổi `ALTER` và bản chất quản lý dung lượng HWM của `TRUNCATE`/`DROP`/`DELETE`.
> - **Đang giải quyết gì:** Một bảng trần chỉ với kiểu dữ liệu chưa đủ để bảo vệ độ chính xác nghiệp vụ. Làm thế nào để áp đặt các quy tắc logic ngăn ngừa dữ liệu rác, cơ chế hoãn kiểm tra ràng buộc (`DEFERRABLE`), và tạo ra các góc nhìn bảo mật có kiểm soát (`WITH CHECK OPTION`, `WITH READ ONLY`)?
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 11 — Constraints, View và các đối tượng hỗ trợ](./11-constraints-view-va-doi-tuong.md) để khảo sát 5 loại ràng buộc toàn vẹn dữ liệu (`PK`, `FK`, `NOT NULL`, `UNIQUE`, `CHECK`), cơ chế hoãn kiểm tra và các đối tượng `VIEW`, `SEQUENCE`, `SYNONYM`.
