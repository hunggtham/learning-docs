<!-- lecture-contract: v2 -->
# SQL cơ bản: SELECT, hàm, lọc, nhóm và sắp xếp

> **Mục tiêu:** Nắm vững cấu trúc câu lệnh `SELECT`, mệnh đề lọc `WHERE`, hàm một hàng, gom nhóm `GROUP BY/HAVING` và sắp xếp `ORDER BY`.
>
> **Phạm vi tham khảo:** PDF *2024 개정판 SQLD 개념정리*, trang 24–42.
>
> **Mạch kiến thức:** Bài học này là nền tảng cho toàn bộ Môn 2: `JOIN` sẽ mở rộng mệnh đề `FROM`, subquery mở rộng biểu thức và điều kiện lọc, còn window function mở rộng việc tính toán trên các cửa sổ dòng dữ liệu.

---

### 1. 관계형 데이터베이스 (Relational Database) — Cơ sở dữ liệu quan hệ

> **KR:** 관계형 데이터베이스는 데이터를 테이블로 저장하고 SQL 문장으로 관리한다.

Cơ sở dữ liệu quan hệ (RDB) lưu trữ dữ liệu dưới dạng bảng (table / 테이블). Một bảng bao gồm các cột thuộc tính (column / attribute) và các hàng bản ghi (row / record / tuple). Trong đó:
- `PRIMARY KEY` (Khóa chính): Đảm bảo tính duy nhất để nhận diện từng hàng trong bảng.
- `FOREIGN KEY` (Khóa ngoại): Liên kết giữa các bảng và đảm bảo tính toàn vẹn tham chiếu.
- Hệ quản trị CSDL (DBMS): Chịu trách nhiệm lưu trữ, phục hồi khi có sự cố và thực thi các câu lệnh SQL tối ưu.

---

### 2. SQL 문장의 종류 — Các nhóm câu lệnh SQL (DML, DDL, DCL, TCL)

Từ cấu trúc bảng và ràng buộc của RDB, để tương tác với dữ liệu ta sử dụng ngôn ngữ SQL được chuẩn hóa thành 4 nhóm lệnh chuyên biệt theo vai trò:

| Phân loại (Korean / English) | Lệnh chính | Vai trò nghiệp vụ |
| --- | --- | --- |
| **데이터 조작어 (DML)** | `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MERGE` | Đọc và thao tác thay đổi dữ liệu hàng. |
| **데이터 정의어 (DDL)** | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` | Định nghĩa hoặc thay đổi cấu trúc đối tượng (auto-commit). |
| **데이터 제어어 (DCL)** | `GRANT`, `REVOKE` | Quản lý và phân quyền truy cập cho người dùng. |
| **트랜잭션 제어어 (TCL)** | `COMMIT`, `ROLLBACK`, `SAVEPOINT` | Kiểm soát kết quả DML (xác nhận hoặc hoàn tác giao dịch). |

---

### 3. SELECT 문의 구조 — Cấu trúc câu lệnh SELECT và thứ tự thực thi

Trong 4 nhóm lệnh, `SELECT` (DML) là trọng tâm hàng đầu của đề thi SQLD. Cú pháp viết và thứ tự thực thi logic thực tế có sự khác biệt rõ rệt mà người học cần phân biệt:

```sql
SELECT [ALL | DISTINCT] select_expression [AS alias]
FROM table_or_view
WHERE row_condition
GROUP BY grouping_column
HAVING group_condition
ORDER BY sort_expression [ASC | DESC];
```

> **KR:** 작성 순서와 논리적 실행 순서는 다르며, 논리적 순서는 FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY이다.

- **Thứ tự thực thi logic của DBMS:**
  1. `FROM`: Xác định bảng nguồn và nạp tập dữ liệu.
  2. `WHERE`: Lọc từng hàng theo điều kiện trước khi gom nhóm.
  3. `GROUP BY`: Gom các hàng thỏa mãn thành các nhóm con.
  4. `HAVING`: Lọc các nhóm dựa trên điều kiện của hàm tổng hợp.
  5. `SELECT`: Chọn các cột cần hiển thị và tính toán biểu thức.
  6. `ORDER BY`: Sắp xếp tập kết quả cuối cùng.

> **Điểm thi then chốt:** Vì `SELECT` thực thi sau `WHERE` và `GROUP BY`, bí danh cột (column alias) được đặt trong mệnh đề `SELECT` **không thể** được sử dụng trong `WHERE` hay `HAVING`, nhưng **có thể** dùng được trong `ORDER BY`.

Về tùy chọn: `ALL` là giá trị mặc định (giữ mọi dòng); `DISTINCT` loại bỏ dòng trùng lặp trong danh sách chọn. Trong Oracle, không sử dụng từ khóa `AS` cho bí danh bảng (table alias); còn bí danh cột có thể dùng `"` nếu chứa khoảng trắng hoặc ký tự đặc biệt.

---

### 4. WHERE 절 — Mệnh đề lọc hàng

Sau khi `FROM` xác định bảng nguồn, mệnh đề `WHERE` lập tức lọc các hàng dữ liệu thô trước khi đưa vào tính toán tổng hợp:

> **KR:** WHERE 절은 테이블의 데이터 중 원하는 조건에 맞는 데이터만 조회하기 위해 사용한다.

- `WHERE` lọc từng hàng (row-level) độc lập; do đó **tuyệt đối không được đặt trực tiếp hàm tổng hợp (aggregate function)** vào mệnh đề `WHERE` (phải dùng `HAVING`).
- Các toán tử thông dụng: `=`, `>`, `>=`, `<`, `<=`, `BETWEEN A AND B`, `IN`, `LIKE`, `IS NULL`, `AND`, `OR`, `NOT`.

```sql
WHERE price BETWEEN 15000 AND 20000       -- Bao gồm cả 2 giá trị đầu mút (15000 và 20000)
WHERE deptno IN (10, 20, 30)              -- Thuộc một trong các giá trị của danh sách
WHERE name LIKE 'S%'                      -- Bắt đầu bằng chữ 'S' (% đại diện cho 0 hoặc nhiều ký tự)
WHERE position IS NULL                    -- Giá trị NULL bắt buộc so sánh bằng IS NULL, không dùng dấu =
```

> **Lưu ý về NULL và thứ tự ưu tiên toán tử:**
> Phép so sánh với `NULL` luôn trả về trạng thái `UNKNOWN`, khiến điều kiện không thỏa mãn `WHERE`. Thứ tự ưu tiên khi đánh giá điều kiện logic: `()` → `NOT` → Phép so sánh/toán tử SQL → `AND` → `OR`. Nên luôn dùng dấu ngoặc đơn để bảo đảm logic rõ ràng.

---

### 5. 단일행 함수 — Hàm một hàng (Single-Row Function)

Trong quá trình lọc ở `WHERE` hoặc định dạng ở `SELECT`, SQL cung cấp các hàm một hàng xử lý độc lập trên từng bản ghi:

> **KR:** 단일행 함수는 하나의 행 값에 대해 하나의 결과를 반환한다.

Hàm một hàng trả về đúng 1 kết quả cho mỗi hàng đầu vào, do đó có thể đặt linh hoạt ở `SELECT`, `WHERE`, `ORDER BY` và lồng nhau nhiều cấp:
- **Nhóm số học:** `ABS`, `SIGN`, `CEIL`, `FLOOR`, `MOD`, `ROUND`, `TRUNC`, `POWER`, `SQRT`.
- **Nhóm chuỗi ký tự (Oracle):** `LOWER`, `UPPER`, `SUBSTR`, `INSTR`, `LENGTH`, `TRIM`, `LPAD`, `RPAD`, `REPLACE`, `TRANSLATE`.
- **Nhóm ngày tháng:** `SYSDATE`, `CURRENT_DATE`, `EXTRACT`, `ADD_MONTHS`, `MONTHS_BETWEEN`, `LAST_DAY`, `NEXT_DAY`.
- **Nhóm chuyển đổi kiểu:** `TO_NUMBER`, `TO_CHAR`, `TO_DATE`, `CAST`, `CONVERT`.

> **KR:** DBMS마다 함수명과 날짜 출력 형식은 다를 수 있다.
> Cần lưu ý sự khác biệt giữa các hệ quản trị: SQL Server dùng `GETDATE()` thay cho `SYSDATE`, `DATEPART` thay cho `EXTRACT`, `DATEDIFF` thay cho `MONTHS_BETWEEN`, và `SUBSTRING`/`LEN`/`CHARINDEX` tương ứng với `SUBSTR`/`LENGTH`/`INSTR` của Oracle.

---

### 6. 집계 함수와 NULL — Hàm tổng hợp và cơ chế xử lý NULL

Khác với hàm một hàng, hàm tổng hợp (hàm nhiều hàng) nhận vào một tập hợp nhiều hàng để trả về một giá trị tóm tắt duy nhất:

> **KR:** 집계 함수는 여러 행을 하나의 결과값으로 반환하며, NULL 값은 0으로 계산되는 것이 아니라 무시된다.

- `COUNT(*)`: Đếm toàn bộ số hàng (bao gồm cả các hàng có giá trị NULL).
- `COUNT(column)`: Chỉ đếm các hàng có giá trị khác `NULL`.
- `SUM`, `AVG`, `MIN`, `MAX`, `STDDEV`, `VARIANCE`: Tự động bỏ qua (ignore) các giá trị `NULL`.
  *Lưu ý đề thi:* `AVG(sal)` chỉ tính trung bình trên các nhân viên có lương thực tế. Nếu muốn gán nhân viên chưa có lương là 0 để tính trung bình toàn công ty, bắt buộc phải dùng `AVG(NVL(sal, 0))`.

- **Hàm xử lý giá trị NULL và rẽ nhánh điều kiện:**
  - `NVL(a, b)` (Oracle) / `ISNULL(a, b)` (SQL Server): Nếu `a` là NULL thì lấy `b`.
  - `NVL2(a, b, c)`: Nếu `a` không NULL lấy `b`, ngược lại lấy `c`.
  - `NULLIF(a, b)`: Nếu `a = b` thì trả về NULL, khác nhau trả về `a`.
  - `COALESCE(a, b, c, ...)`: Trả về giá trị đầu tiên khác NULL trong danh sách.
  - `CASE` / `DECODE`: Phân nhánh logic có điều kiện.

---

### 7. GROUP BY và HAVING — Gom nhóm và lọc điều kiện trên nhóm

Khi cần thống kê số liệu theo từng phòng ban, danh mục sản phẩm hay khu vực, ta kết hợp hàm tổng hợp với mệnh đề gom nhóm:

> **KR:** GROUP BY는 데이터를 소그룹으로 분류하여 통계 정보를 얻고, HAVING은 그룹화된 결과에 조건을 적용한다.

- Sau khi áp dụng `GROUP BY`, trong mệnh đề `SELECT` **chỉ được phép chứa các cột nằm trong `GROUP BY` hoặc các biểu thức hàm tổng hợp**.
- **Phân biệt `WHERE` và `HAVING`:**
  - `WHERE`: Lọc từng hàng trước khi gom nhóm để tối ưu hiệu năng tính toán.
  - `HAVING`: Lọc tập nhóm sau khi hàm tổng hợp đã hoàn tất tính toán.
  - `GROUP BY` không tự động sắp xếp kết quả; nếu cần thứ tự xác định phải dùng `ORDER BY`.

```sql
SELECT deptno, COUNT(*) AS employee_count, AVG(sal) AS avg_sal
FROM emp
WHERE deptno IN (10, 20, 30)
GROUP BY deptno
HAVING AVG(sal) > 2500
ORDER BY avg_sal DESC;
```

---

### 8. ORDER BY — Sắp xếp tập kết quả cuối cùng

Mệnh đề thực thi sau cùng trong chu trình xử lý truy vấn là `ORDER BY`, định hình thứ tự hiển thị dữ liệu cho người dùng:

> **KR:** ORDER BY는 결과 집합의 정렬 기준을 명시하며 기본값은 ASC이다.

- `ASC` (Tăng dần - mặc định) và `DESC` (Giảm dần).
- Khi sắp xếp theo nhiều cột, thứ tự từ trái qua phải thể hiện mức độ ưu tiên.
- **Xử lý NULL khi sắp xếp trong đề thi:**
  - **Oracle:** Mặc định xem `NULL` là giá trị lớn nhất (ở cuối khi `ASC`, ở đầu khi `DESC`). Cho phép chỉ định tường minh bằng `NULLS FIRST` hoặc `NULLS LAST`.
  - **SQL Server:** Mặc định xem `NULL` là giá trị nhỏ nhất (ở đầu khi `ASC`).
- Nếu truy vấn có `GROUP BY`, mệnh đề `ORDER BY` chỉ được tham chiếu đến các cột có mặt trong `SELECT` hoặc các hàm tổng hợp hợp lệ.

---

## 9. Nối mạch sang Bài tiếp theo: JOIN và liên kết bảng

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 00 đã trang bị toàn bộ cú pháp cơ bản và thứ tự thực thi logic của câu lệnh `SELECT` đơn lẻ trên một bảng dữ liệu.
> - **Đang giải quyết gì:** Trong cơ sở dữ liệu quan hệ thực tế, thông tin nghiệp vụ luôn bị phân tán trên nhiều bảng chuẩn hóa khác nhau. Làm thế nào để kết hợp các bảng này lại một cách chính xác theo khóa chính và khóa ngoại?
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 01 — JOIN](./01-join.md) để mở rộng mệnh đề `FROM` với các kỹ thuật liên kết bảng chuẩn ANSI (`INNER JOIN`, `LEFT/RIGHT OUTER JOIN`, `FULL OUTER JOIN`, `CROSS JOIN`, `NATURAL JOIN`).
