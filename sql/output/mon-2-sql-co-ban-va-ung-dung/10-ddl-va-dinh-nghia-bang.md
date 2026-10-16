<!-- lecture-contract: v2 -->
# DDL và định nghĩa bảng (Data Definition Language)

> **Mục tiêu:** Nắm vững các kiểu dữ liệu cốt lõi, quy tắc đặt tên đối tượng, cú pháp `CREATE TABLE`, kỹ thuật sao chép `CTAS`, các thao tác hiệu chỉnh `ALTER TABLE`, và phân biệt chính xác `DROP`, `TRUNCATE`, `DELETE` trong đề thi SQLD.
>
> **Phạm vi tham khảo:** PDF *2024 개정판 SQLD 개념정리*, trang 90–94.
>
> **Mạch kiến thức:** Bài trước đã phân tích cách quản lý giao dịch dữ liệu (TCL). Bài này đi vào tầng kiến trúc nền tảng: *Làm thế nào để định nghĩa và hiệu chỉnh cấu trúc lưu trữ của các bảng trong cơ sở dữ liệu?*

---

### 1. DDL (Data Definition Language) — Ngôn ngữ định nghĩa dữ liệu

> **KR:** DDL은 데이터의 구조를 정의하는 언어로 객체 생성, 삭제, 변경에 사용하며 AUTO COMMIT이라 ROLLBACK이 불가하다.

DDL chịu trách nhiệm định nghĩa cấu trúc lưu trữ và các đối tượng CSDL (bảng, khung nhìn, chỉ mục, schema...).
- **Đặc tính sống còn trong đề thi:** Trong Oracle, các câu lệnh DDL mang cơ chế **AUTO-COMMIT** ngầm định. Khi lệnh DDL thực thi thành công, thay đổi được ghi nhận vĩnh viễn vào từ điển dữ liệu (Data Dictionary) và **hoàn toàn không thể ROLLBACK**.
- **Các lệnh chính:** `CREATE` (tạo mới), `ALTER` (sửa đổi cấu trúc), `DROP` (xóa bỏ đối tượng), `TRUNCATE` (xóa trắng dữ liệu giải phóng bộ nhớ, giữ lại khung bảng).

---

### 2. 데이터 유형 (Data Types) — Các kiểu dữ liệu cơ bản

| Kiểu dữ liệu (Korean / English) | Đặc tính kỹ thuật | Điểm thi trọng tâm |
| --- | --- | --- |
| **`CHAR(n)`** (Độ dài cố định) | Chiếm trọn vẹn đúng $n$ byte. Nếu chuỗi ngắn hơn $n$, hệ thống tự động đệm khoảng trắng (`Blank Padded`) vào cuối. | Khi so sánh hai chuỗi `CHAR`, khoảng trắng ở đuôi được bỏ qua (`'A' = 'A '` là TRUE). |
| **`VARCHAR2(n)`** (Độ dài biến đổi) | Chỉ chiếm dung lượng thực tế của chuỗi ký tự được nạp, tối đa $n$ byte. Tiết kiệm bộ nhớ. | Khi so sánh `VARCHAR2`, ký tự khoảng trắng được tính là một ký tự hợp lệ (`'A' = 'A '` là FALSE). |
| **`NUMBER(p, s)`** (Kiểu số) | $p$ (Precision): Tổng số chữ số tối đa; $s$ (Scale): Số chữ số sau dấu phẩy thập phân. | `NUMBER(6, 2)` chứa tối đa 4 chữ số nguyên và 2 chữ số thập phân (ví dụ: `1234.56`). |
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

- **Quy tắc đặt tên đối tượng trong đề thi:**
  - Tên bảng và tên cột bắt buộc phải **bắt đầu bằng một chữ cái** (không bắt đầu bằng chữ số hoặc ký tự đặc biệt).
  - Chỉ được chứa các ký tự: chữ cái (`A-Z`, `a-z`), chữ số (`0-9`), và 3 ký tự đặc biệt: gạch dưới `_`, dấu đô la `$`, dấu thăng `#`.
  - Không được trùng lặp với **Từ khóa dành riêng (Reserved Words)** của hệ thống (như `SELECT`, `FROM`, `ORDER`...).
  - Trong cùng một bảng, không được phép có hai cột trùng tên nhau.

---

### 4. CTAS (Create Table As Select) — Tạo bảng từ kết quả truy vấn

> **KR:** CTAS는 이미 만들어진 테이블을 활용해서 테이블을 재생성하며, 구조뿐 아니라 데이터도 복제할 수 있다. 단, NOT NULL을 제외한 PK, FK, UNIQUE 등 제약조건은 복제되지 않는다.

Kỹ thuật CTAS cho phép nhân bản nhanh một bảng từ câu lệnh `SELECT`:

```sql
-- Sao chép cả cấu trúc và toàn bộ dữ liệu
CREATE TABLE emp_copy AS
SELECT * FROM emp;

-- Chỉ sao chép cấu trúc khung (không lấy bất kỳ dòng dữ liệu nào)
CREATE TABLE emp_skeleton AS
SELECT * FROM emp
WHERE 1 = 2; -- Mệnh đề luôn False
```

> **Bẫy đề thi then chốt của CTAS:**
> CTAS sao chép kiểu dữ liệu, dữ liệu và thuộc tính **`NOT NULL`**. Ngược lại, **tất cả các ràng buộc khác (Khóa chính `PRIMARY KEY`, Khóa ngoại `FOREIGN KEY`, `UNIQUE`, `CHECK`) và chỉ mục (`INDEX`) đều KHÔNG ĐƯỢC SAO CHÉP**. Muốn có các ràng buộc này, bắt buộc phải dùng `ALTER TABLE` để thêm thủ công.

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

- **Các quy tắc kiểm tra ràng buộc khi `ALTER` trong đề thi:**
  - **Tăng kích thước cột:** Luôn luôn thực hiện được dù bảng đã có dữ liệu hay chưa.
  - **Giảm kích thước cột:** Chỉ thực hiện được nếu kích thước mới vẫn lớn hơn hoặc bằng chiều dài tối đa của dữ liệu hiện có trong cột (hoặc cột hoàn toàn rỗng).
  - **Đổi kiểu dữ liệu:** Chỉ an toàn và được phép khi cột hoàn toàn không có dữ liệu (hoặc toàn bộ giá trị là `NULL`). Ngoại lệ: `CHAR` và `VARCHAR2` có thể chuyển đổi tương hỗ nếu kích thước chứa đủ dữ liệu.
  - **Thêm ràng buộc `NOT NULL`:** Chỉ thành công nếu cột đó hiện không chứa bất kỳ giá trị `NULL` nào.

---

### 6. So sánh DROP, TRUNCATE và DELETE

Đây là một trong những bảng so sánh có tần suất xuất hiện cao nhất trong kỳ thi SQLD:

| Tiêu chí | `DELETE` | `TRUNCATE` | `DROP` |
| --- | --- | --- | --- |
| **Phân loại ngôn ngữ** | **DML** (Thao tác dữ liệu) | **DDL** (Định nghĩa dữ liệu) | **DDL** (Định nghĩa dữ liệu) |
| **Đối tượng tác động** | Xóa từng hàng (hoặc toàn bộ hàng thỏa mãn `WHERE`) | Xóa toàn bộ dữ liệu trong bảng (không hỗ trợ `WHERE`) | Xóa vĩnh viễn toàn bộ bảng (cả cấu trúc lẫn dữ liệu) |
| **Khung bảng (Structure)** | **Vẫn giữ nguyên** | **Vẫn giữ nguyên** (kiểm tra lại bằng `DESC`) | **Bị xóa hoàn toàn khỏi CSDL** |
| **Giải phóng bộ nhớ (Storage)** | Không giải phóng vùng nhớ đã cấp phát | **Giải phóng toàn bộ vùng nhớ (Reset High Water Mark)** | Giải phóng toàn bộ tài nguyên lưu trữ |
| **Khả năng ROLLBACK** | **Có thể ROLLBACK** (trước khi `COMMIT`) | **KHÔNG THỂ ROLLBACK** (Auto-Commit) | **KHÔNG THỂ ROLLBACK** (Auto-Commit) |
| **Tốc độ thực thi** | Chậm (ghi nhận đầy đủ Undo/Redo Log từng hàng) | Cực nhanh (chỉ ghi log việc giải phóng trang dữ liệu) | Cực nhanh |

---

## 7. Nối mạch sang Bài tiếp theo: Ràng buộc, Khung nhìn và Đối tượng hỗ trợ

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 10 đã trang bị đầy đủ cú pháp khởi tạo bảng, kiểu dữ liệu và cách biến đổi schema bằng DDL.
> - **Đang giải quyết gì:** Một bảng trần chỉ với kiểu dữ liệu chưa đủ để bảo vệ độ chính xác nghiệp vụ. Làm thế nào để áp đặt các quy tắc logic ngăn ngừa dữ liệu rác, và tạo ra các góc nhìn bảo mật hoặc sinh khóa tự động?
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 11 — Constraints, View và các đối tượng hỗ trợ](./11-constraints-view-va-doi-tuong.md) để khảo sát 5 loại ràng buộc toàn vẹn dữ liệu (`PK`, `FK`, `NOT NULL`, `UNIQUE`, `CHECK`) và các đối tượng `VIEW`, `SEQUENCE`, `SYNONYM`.
