<!-- lecture-contract: v2 -->
# SQL cơ bản: SELECT, hàm, lọc, nhóm và sắp xếp

> **Mục tiêu:** Nắm vững cấu trúc câu lệnh `SELECT`, thứ tự thực thi logic của DBMS, toàn bộ các hàm một hàng (số học, chuỗi, ngày tháng, NULL, điều kiện), mệnh đề lọc `WHERE` và logic 3 giá trị (3-Valued Logic), gom nhóm `GROUP BY/HAVING` và sắp xếp `ORDER BY`.
>
> **Phạm vi tham khảo:** PDF *2024 개정판 SQLD 개념정리*, Mục II: SQL 기본 및 활용 (trang 24–42).
>
> **Mạch kiến thức:** Bài học này là nền tảng cốt lõi cho toàn bộ Môn 2: `JOIN` sẽ mở rộng mệnh đề `FROM`, subquery mở rộng biểu thức và điều kiện lọc, còn window function mở rộng việc tính toán trên các cửa sổ dòng dữ liệu.

---

### 1. 관계형 데이터베이스 (Relational Database) — Cơ sở dữ liệu quan hệ

> **KR:** 관계형 데이터베이스는 데이터를 2차원 테이블 형태로 저장하고 SQL 문장으로 관리하며, 무결성을 보장한다.

Cơ sở dữ liệu quan hệ (RDB - Relational Database) quản lý thông tin dưới dạng các bảng 2 chiều (table / 테이블). Một bảng bao gồm:
- **Cột thuộc tính (Column / Attribute / 속성 / 열):** Đại diện cho một đặc tính cụ thể của thực thể, có tên và kiểu dữ liệu xác định.
- **Hàng bản ghi (Row / Record / Tuple / 행):** Biểu diễn một thể hiện dữ liệu cụ thể.
- **Khóa chính (Primary Key / PK / 기본키):** Đảm bảo tính duy nhất và không được phép chứa giá trị `NULL`.
- **Khóa ngoại (Foreign Key / FK / 외래키):** Thiết lập mối quan hệ tham chiếu logic giữa các bảng.

#### Các nhóm lệnh SQL (SQL 문장의 종류)

Ngôn ngữ SQL được chuẩn hóa thành 4 nhóm lệnh phục vụ từng vai trò kỹ thuật khác nhau:

| Phân loại (Korean / English) | Lệnh chính | Vai trò nghiệp vụ và cơ chế giao dịch |
| --- | --- | --- |
| **데이터 조작어 (DML)** | `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MERGE` | Thao tác trên các hàng dữ liệu. Cần `COMMIT`/`ROLLBACK` trong Oracle. |
| **데이터 정의어 (DDL)** | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` | Định nghĩa và thay đổi cấu trúc bảng, tự động Auto-commit. |
| **데이터 제어어 (DCL)** | `GRANT`, `REVOKE` | Cấp và thu hồi quyền hạn bảo mật người dùng. |
| **트랜잭션 제어어 (TCL)** | `COMMIT`, `ROLLBACK`, `SAVEPOINT` | Quản lý và kiểm soát tính toàn vẹn của các giao dịch DML. |

---

### 2. SELECT 문의 구조와 논리적 실행 순서 — Cấu trúc SELECT và Thứ tự thực thi logic

Trong kỳ thi SQLD, điểm phân loại thí sinh quan trọng nhất là sự khác biệt giữa **Thứ tự viết câu lệnh (작성 순서 / Lexical Order)** và **Thứ tự thực thi logic của hệ quản trị CSDL (논리적 실행 순서 / Logical Processing Order)**.

```sql
-- CÚ PHÁP VIẾT CÂU LỆNH (작성 순서)
SELECT [ALL | DISTINCT] column_name [AS alias]   -- 5. Lựa chọn cột và tính toán biểu thức
FROM table_or_view                               -- 1. Xác định bảng nguồn và nạp dữ liệu
WHERE row_filter_condition                       -- 2. Lọc từng dòng dữ liệu thô
GROUP BY grouping_columns                        -- 3. Gom các dòng thành các nhóm nhỏ
HAVING group_filter_condition                    -- 4. Lọc các nhóm theo điều kiện tổng hợp
ORDER BY sort_column [ASC | DESC];               -- 6. Sắp xếp tập kết quả cuối cùng
```

```
+---------------------------------------------------------------------------------+
|               THỨ TỰ THỰC THI LOGIC CỦA DBMS (논리적 처리 순서)                   |
|                                                                                 |
|  [1] FROM       --> Xác định tập dữ liệu nguồn (nạp bảng, thực hiện JOIN)       |
|       |                                                                         |
|  [2] WHERE      --> Lọc từng hàng bản ghi độc lập (chưa gom nhóm)               |
|       |                                                                         |
|  [3] GROUP BY   --> Chia nhỏ các hàng thành các nhóm (소그룹 분류)              |
|       |                                                                         |
|  [4] HAVING     --> Lọc nhóm dựa trên hàm tổng hợp (SUM, AVG, COUNT...)         |
|       |                                                                         |
|  [5] SELECT     --> Chọn cột hiển thị, áp dụng toán tử, đặt ALIAS, DISTINCT     |
|       |                                                                         |
|  [6] ORDER BY   --> Sắp xếp kết quả cuối cùng (sử dụng được ALIAS từ SELECT)    |
+---------------------------------------------------------------------------------+
```

#### Quy tắc sống còn trong đề thi về bí danh (Alias)
- **Bí danh cột (Column Alias):** Vì mệnh đề `SELECT` (bước 5) thực thi **sau** `WHERE` (bước 2), `GROUP BY` (bước 3), và `HAVING` (bước 4), nên **tuyệt đối không được sử dụng bí danh cột trong `WHERE`, `GROUP BY`, hoặc `HAVING`**.
- Mệnh đề `ORDER BY` (bước 6) thực thi **sau** `SELECT`, do đó **được phép sử dụng bí danh cột** để sắp xếp.
- **Bí danh bảng (Table Alias):** Trong Oracle, từ khóa `AS` **không được phép dùng cho bí danh bảng** (`FROM emp e` là đúng, `FROM emp AS e` sẽ báo lỗi cú pháp). SQL Server hỗ trợ cả hai cách viết.

#### Bảng DUAL (DUAL 테이블의 특성)
- Trong Oracle (trước bản 23c), câu lệnh `SELECT` bắt buộc phải có mệnh đề `FROM`. Khi cần tính toán biểu thức hoặc gọi hàm đơn lẻ không phụ thuộc bảng người dùng, Oracle cung cấp bảng giả lập `DUAL`.
- `DUAL` thuộc sở hữu của người dùng hệ thống `SYS`, có đúng 1 cột tên là `DUMMY` kiểu `VARCHAR2(1)` và chứa đúng 1 hàng mang giá trị `'X'`.
- Trong SQL Server hoặc PostgreSQL, có thể viết `SELECT 1 + 1;` mà không cần mệnh đề `FROM`.

---

### 3. 단일행 숫자형 함수 — Hàm một hàng: Nhóm số học

Hàm số học nhận tham số kiểu số và trả về một giá trị số duy nhất cho mỗi dòng:

| Hàm (Function) | Ý nghĩa và Quy tắc xử lý | Ví dụ minh họa | Kết quả trả về |
| --- | --- | --- | --- |
| `ROUND(n, m)` | Làm tròn số `n` đến vị trí thập phân thứ `m`. Nếu `m` bị bỏ qua, mặc định `m = 0`. Nếu `m < 0`, làm tròn ở phần nguyên. | `ROUND(45.678, 2)` / `ROUND(45.678, -1)` | `45.68` / `50` |
| `TRUNC(n, m)` | Cắt bỏ (trừ khử) các chữ số của `n` sau vị trí `m` mà không làm tròn. SQL Server dùng `ROUND(n, m, 1)`. | `TRUNC(45.678, 2)` / `TRUNC(45.678, -1)` | `45.67` / `40` |
| `MOD(n, m)` | Lấy phần dư của phép chia `n` cho `m` ($n \pmod m$). SQL Server dùng toán tử `%` (`n % m`). | `MOD(10, 3)` / `MOD(10, -3)` | `1` / `1` |
| `CEIL(n)` | Trả về số nguyên nhỏ nhất lớn hơn hoặc bằng `n`. Trong SQL Server là `CEILING(n)`. | `CEIL(3.14)` / `CEIL(-3.14)` | `4` / `-3` |
| `FLOOR(n)` | Trả về số nguyên lớn nhất nhỏ hơn hoặc bằng `n`. | `FLOOR(3.89)` / `FLOOR(-3.89)` | `3` / `-4` |
| `ABS(n)` | Trả về giá trị tuyệt đối của `n`. | `ABS(-15.5)` | `15.5` |
| `SIGN(n)` | Trả về dấu của `n`: `1` nếu $n > 0$, `-1` nếu $n < 0$, và `0` nếu $n = 0$. | `SIGN(-25)` / `SIGN(0)` | `-1` / `0` |
| `POWER(n, p)` | Trả về lũy thừa $n^p$. | `POWER(2, 3)` | `8` |
| `SQRT(n)` | Trả về căn bậc hai của `n` ($n \ge 0$). | `SQRT(16)` | `4` |

```sql
-- Ví dụ minh họa cơ chế vị trí m trong ROUND và TRUNC
SELECT ROUND(567.89, 1)  AS r1,  -- Làm tròn đến 1 chữ số thập phân -> 567.9
       ROUND(567.89, 0)  AS r0,  -- Làm tròn đến hàng đơn vị -> 568
       ROUND(567.89, -1) AS rm1, -- Làm tròn đến hàng chục -> 570
       ROUND(567.89, -2) AS rm2, -- Làm tròn đến hàng trăm -> 600
       TRUNC(567.89, 1)  AS t1,  -- Cắt cụt tại 1 chữ số thập phân -> 567.8
       TRUNC(567.89, -1) AS tm1  -- Cắt cụt tại hàng chục -> 560
FROM DUAL;
```

---

### 4. 단일행 문자형 함수 — Hàm một hàng: Nhóm chuỗi ký tự

| Hàm (Function) | Ý nghĩa và Quy tắc xử lý | Ví dụ câu lệnh SQL | Kết quả |
| --- | --- | --- | --- |
| `LOWER(s)` / `UPPER(s)` | Chuyển toàn bộ chuỗi sang chữ thường / chữ hoa. | `LOWER('SQL Expert')` | `'sql expert'` |
| `SUBSTR(s, m, n)` | Trích xuất `n` ký tự từ vị trí `m` (bắt đầu từ 1). Nếu `m < 0`, đếm ngược từ cuối chuỗi. Bỏ qua `n` sẽ lấy đến hết chuỗi. SQL Server dùng `SUBSTRING(s, m, n)`. | `SUBSTR('DATABASE', 5, 4)` / `SUBSTR('DATABASE', -4, 2)` | `'BASE'` / `'BA'` |
| `LENGTH(s)` | Đếm tổng số ký tự của chuỗi `s`. SQL Server dùng `LEN(s)` (tự động bỏ khoảng trắng ở đuôi). | `LENGTH('SQL Developer')` | `13` |
| `INSTR(s, sub, m, n)` | Tìm vị trí xuất hiện lần thứ `n` của chuỗi con `sub` kể từ vị trí `m`. Nếu không thấy trả về `0`. SQL Server dùng `CHARINDEX(sub, s, m)`. | `INSTR('BANANA', 'A', 2, 2)` | `4` |
| `LPAD(s, n, c)` / `RPAD(s, n, c)` | Đệm ký tự `c` vào bên trái / phải chuỗi `s` để đạt tổng độ dài `n`. Nếu `n` nhỏ hơn độ dài thực, chuỗi sẽ bị cắt bớt. | `LPAD('123', 5, '0')` / `RPAD('Hi', 5, '*')` | `'00123'` / `'Hi***'` |
| `LTRIM(s, c)` / `RTRIM(s, c)` | Cắt bỏ các ký tự `c` xuất hiện liên tục ở đầu / cuối chuỗi `s`. Mặc định bỏ khoảng trắng. | `LTRIM('  Data')` / `RTRIM('$$100$$', '$')` | `'Data'` / `'$$100'` |
| `TRIM([BOTH/LEADING/TRAILING] c FROM s)` | Cắt bỏ ký tự `c` ở hai đầu (`BOTH`), đầu (`LEADING`) hoặc cuối (`TRAILING`). Chuẩn ANSI. | `TRIM(BOTH 'x' FROM 'xxxSQLxxx')` | `'SQL'` |
| `REPLACE(s, old, new)` | Thay thế mọi chuỗi con `old` thành chuỗi mới `new`. Nếu bỏ qua `new` thì coi như xóa `old`. | `REPLACE('ORACLE SQL', 'SQL', 'DB')` | `'ORACLE DB'` |
| `TRANSLATE(s, from, to)` | Thay thế từng ký tự đơn lẻ theo vị trí tương ứng 1-1 từ bảng mã `from` sang `to`. | `TRANSLATE('2K24', '2K', '4X')` | `'4X44'` |
| `CONCAT(s1, s2)` | Ghép nối 2 chuỗi ký tự. Lưu ý: Oracle chỉ nhận tối đa 2 tham số. | `CONCAT('Data', 'base')` | `'Database'` |

```sql
-- So sánh bản chất REPLACE và TRANSLATE trong đề thi:
SELECT REPLACE('12345', '12', 'AB')   AS res_replace,  -- Thay cả cụm '12' thành 'AB' -> 'AB345'
       TRANSLATE('12345', '12', 'AB') AS res_translate -- Thay '1' thành 'A', '2' thành 'B' -> 'AB345'
FROM DUAL;

SELECT REPLACE('2024-10-16', '-', '/')   AS date_rep,  -- '2024/10/16'
       SUBSTR('950101-1234567', 8, 1)    AS gender_code -- '1'
FROM DUAL;
```

---

### 5. 단일행 날짜형 함수 — Hàm một hàng: Nhóm ngày tháng

Dữ liệu ngày tháng trong RDBMS bao gồm cả thông tin năm, tháng, ngày, giờ, phút và giây.

#### Cơ chế số học trên ngày tháng (Date Arithmetic)
- `DATE + n`: Cộng thêm $n$ ngày vào mốc thời gian hiện tại.
- `DATE - n`: Trừ đi $n$ ngày.
- `DATE1 - DATE2`: Trả về khoảng cách giữa hai mốc thời gian theo **đơn vị số ngày** (dưới dạng số thực).
- Phép tính thời gian chi tiết trong ngày:
  - Thêm 1 giờ: `SYSDATE + 1/24` (vì 1 ngày có 24 giờ).
  - Thêm 1 phút: `SYSDATE + 1/1440` (vì 1 ngày có $24 \times 60 = 1440$ phút).
  - Thêm 1 giây: `SYSDATE + 1/86400` (vì 1 ngày có $24 \times 3600 = 86400$ giây).

#### Các hàm ngày tháng quan trọng

| Hàm trong Oracle | Ý nghĩa kỹ thuật | Hàm tương đương trong SQL Server |
| --- | --- | --- |
| `SYSDATE` | Ngày và giờ hiện tại của hệ điều hành máy chủ Database. | `GETDATE()` |
| `CURRENT_DATE` | Ngày và giờ theo múi giờ phiên làm việc hiện tại (Session Timezone). | `CURRENT_TIMESTAMP` |
| `ADD_MONTHS(d, n)` | Thêm $n$ tháng vào ngày `d` ($n < 0$ là lùi tháng). Tự động bảo toàn ngày cuối tháng. | `DATEADD(month, n, d)` |
| `MONTHS_BETWEEN(d1, d2)` | Trả về số tháng chênh lệch giữa hai mốc ngày $d_1 - d_2$. Nếu $d_1 > d_2$ thì kết quả dương. | `DATEDIFF(month, d2, d1)` |
| `LAST_DAY(d)` | Trả về ngày cuối cùng của tháng chứa ngày `d` (28, 29, 30 hoặc 31). | `EOMONTH(d)` |
| `NEXT_DAY(d, weekday)` | Trả về ngày đầu tiên tương ứng với thứ `weekday` kể sau mốc ngày `d` (`1` là Chủ nhật, `7` là Thứ bảy). | N/A (phải dùng logic cộng ngày) |
| `EXTRACT(part FROM d)` | Trích xuất thành phần cụ thể (`YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, `SECOND`). | `DATEPART(part, d)` hoặc `YEAR(d)` |

```sql
-- Minh họa truy vấn ngày tháng thực tế:
SELECT SYSDATE,
       SYSDATE + 7 AS next_week,
       ADD_MONTHS(SYSDATE, 3) AS next_quarter,
       LAST_DAY(TO_DATE('2024-02-01', 'YYYY-MM-DD')) AS leap_year_feb, -- 2024-02-29
       ROUND(MONTHS_BETWEEN(TO_DATE('2024-12-31', 'YYYY-MM-DD'), TO_DATE('2024-01-01', 'YYYY-MM-DD')), 1) AS diff_months
FROM DUAL;
```

---

### 6. 단일행 변환 함수 — Hàm một hàng: Chuyển đổi kiểu dữ liệu

Hệ quản trị CSDL hỗ trợ chuyển đổi ngầm định (Implicit Conversion), tuy nhiên để đảm bảo hiệu năng và tránh sai lệch dữ liệu theo cấu hình Locale máy chủ, đề thi luôn yêu cầu chuyển đổi tường minh (Explicit Conversion):

- **Oracle:**
  - `TO_CHAR(d, 'YYYY-MM-DD HH24:MI:SS')`: Định dạng ngày sang chuỗi.
  - `TO_CHAR(n, 'FM999,999,990.00')`: Định dạng số sang chuỗi có dấu phẩy phân tách nghìn.
  - `TO_DATE('2024-10-16', 'YYYY-MM-DD')`: Chuyển chuỗi sang kiểu ngày.
  - `TO_NUMBER('1,250', '9,999')`: Chuyển chuỗi số sang kiểu số.
- **SQL Server & Chuẩn ANSI:**
  - `CAST(biểu_thức AS kiểu_dữ_liệu)`: Cú pháp chuẩn ANSI (`CAST('123.45' AS DECIMAL(10,2))`).
  - `CONVERT(kiểu_dữ_liệu, biểu_thức [, style])`: Cho phép chỉ định mã định dạng ngày tháng (ví dụ: style 101 là `MM/DD/YYYY`, style 120 là `YYYY-MM-DD HH:MI:SS`).

---

### 7. NULL 관련 함수와 조건문 — Xử lý NULL và Rẽ nhánh điều kiện

#### Các hàm chuyên biệt xử lý giá trị NULL

| Hàm (Function) | Cú pháp và Quy tắc vận hành | Ví dụ thực tế | Kết quả |
| --- | --- | --- | --- |
| `NVL(a, b)` | Nếu `a` là `NULL` thì trả về `b`, ngược lại giữ nguyên `a`. (Cả 2 đối số phải cùng kiểu dữ liệu). | `NVL(comm, 0)` | Trả về `0` nếu hoa hồng `NULL` |
| `ISNULL(a, b)` | Tương đương `NVL` nhưng là hàm của SQL Server. | `ISNULL(comm, 0)` | Trả về `0` nếu hoa hồng `NULL` |
| `NVL2(a, b, c)` | Nếu `a` KHÔNG `NULL` thì trả về `b`; Nếu `a` là `NULL` thì trả về `c`. | `NVL2(comm, 'Có', 'Không')` | Phân loại trạng thái hoa hồng |
| `NULLIF(a, b)` | Nếu $a = b$ thì trả về `NULL`; nếu $a \neq b$ thì trả về $a$. Thường dùng để tránh lỗi chia cho 0. | `NULLIF(100, 100)` / `NULLIF(100, 200)` | `NULL` / `100` |
| `COALESCE(e1, e2, ...)` | Trả về biểu thức đầu tiên **khác NULL** trong danh sách. Nếu tất cả đều NULL trả về NULL. Chuẩn ANSI. | `COALESCE(comm, sal * 0.1, 0)` | Ưu tiên comm, rồi đến 10% sal, cuối cùng 0 |

```sql
-- Kỹ thuật chống lỗi chia cho 0 (Division by Zero) bằng NULLIF:
SELECT sal / NULLIF(comm, 0) AS safe_ratio
FROM emp;
-- Nếu comm = 0, NULLIF trả về NULL, phép chia cho NULL cho ra NULL (không bị văng lỗi ORA-01476)
```

#### Cấu trúc rẽ nhánh điều kiện: CASE và DECODE

##### 1. Cú pháp CASE (Chuẩn ANSI — Hỗ trợ cả Oracle và SQL Server)
Cú pháp `CASE` gồm 2 dạng:
- **Simple CASE (Đơn giản):** So sánh bằng trực tiếp trên một biểu thức.
- **Searched CASE (Tìm kiếm theo điều kiện):** Cho phép viết các biểu thức so sánh phức tạp (`>`, `<`, `LIKE`, `AND/OR`).

```sql
-- Dạng 1: Simple CASE
SELECT ename,
       CASE deptno
           WHEN 10 THEN 'Accounting'
           WHEN 20 THEN 'Research'
           WHEN 30 THEN 'Sales'
           ELSE 'Operations'
       END AS department_name
FROM emp;

-- Dạng 2: Searched CASE
SELECT ename, sal,
       CASE
           WHEN sal >= 3000 THEN 'Grade A'
           WHEN sal >= 2000 THEN 'Grade B'
           WHEN sal >= 1000 THEN 'Grade C'
           ELSE 'Grade D'
       END AS salary_grade
FROM emp;
```

##### 2. Hàm DECODE (Đặc thù riêng của Oracle)
Hàm `DECODE` hoạt động tương đương dạng Simple CASE nhưng được viết gọn dưới dạng lời gọi hàm:
```sql
DECODE(cột_hoặc_biểu_thức,
       giá_trị_1, kết_quả_1,
       giá_trị_2, kết_quả_2,
       ...,
       kết_quả_mặc_định_ELSE)
```
- Nếu bỏ qua đối số `ELSE`, khi không khớp giá trị nào hàm sẽ trả về `NULL`.

```sql
-- Cùng một nghiệp vụ viết bằng DECODE và CASE:
SELECT DECODE(deptno, 10, 'Accounting', 20, 'Research', 30, 'Sales', 'Other') AS dept_d,
       CASE deptno
           WHEN 10 THEN 'Accounting'
           WHEN 20 THEN 'Research'
           WHEN 30 THEN 'Sales'
           ELSE 'Other'
       END AS dept_c
FROM emp;
```

---

### 8. WHERE 절과 3-Valued Logic — Mệnh đề lọc và Logic 3 giá trị

Mệnh đề `WHERE` lọc các hàng dữ liệu thô ngay khi nạp từ bảng nguồn. Để làm chủ các câu hỏi thi cử hóc búa, cần nắm rõ bảng chân trị 3 giá trị: `TRUE`, `FALSE`, và `UNKNOWN`.

#### Bảng chân trị toán tử Logic với giá trị UNKNOWN

| Phép toán | A | B | Kết quả | Ghi nhớ thi cử |
| --- | --- | --- | --- | --- |
| `A AND B` | `TRUE` | `UNKNOWN` | **`UNKNOWN`** | Phải cả 2 cùng TRUE mới ra TRUE. |
| `A AND B` | `FALSE` | `UNKNOWN` | **`FALSE`** | Đã có một bên FALSE thì chắc chắn FALSE. |
| `A OR B` | `TRUE` | `UNKNOWN` | **`TRUE`** | Đã có một bên TRUE thì chắc chắn TRUE. |
| `A OR B` | `FALSE` | `UNKNOWN` | **`UNKNOWN`** | Cần biết bên còn lại, nên vẫn UNKNOWN. |
| `NOT A` | `UNKNOWN` | - | **`UNKNOWN`** | Phủ định của UNKNOWN vẫn là UNKNOWN! |

> **Quy tắc vàng của mệnh đề WHERE:** Một hàng chỉ được đưa vào tập kết quả khi và chỉ khi biểu thức điều kiện sau `WHERE` được đánh giá thành **`TRUE`**. Nếu điều kiện ra `FALSE` hoặc **`UNKNOWN`**, hàng đó lập tức bị loại bỏ!

#### Thứ tự ưu tiên toán tử (연산자 우선순위)
1. Dấu ngoặc đơn `()`
2. Toán tử phủ định `NOT`
3. Toán tử so sánh (`=`, `>`, `<`, `<>`) và toán tử SQL (`BETWEEN`, `IN`, `LIKE`, `IS NULL`)
4. Toán tử logic `AND`
5. Toán tử logic `OR`

#### Cạm bẫy toán tử LIKE và mệnh đề ESCAPE
Toán tử `LIKE` dùng để khớp mẫu chuỗi ký tự với 2 ký tự đại diện (Wildcards):
- `%`: Đại diện cho chuỗi gồm 0 hoặc nhiều ký tự bất kỳ.
- `_`: Đại diện cho chính xác đúng 1 ký tự bất kỳ.

**Vấn đề xuất hiện:** Khi trong dữ liệu thực sự có chứa ký tự `%` hoặc `_` (ví dụ: mã hàng `'ITEM_A'`, tỷ lệ giảm giá `'20%'`), làm sao để tìm chính xác các ký tự này?
$\Rightarrow$ Ta phải sử dụng tùy chọn `ESCAPE` để chỉ định ký tự thoát:

```sql
-- Tìm tất cả nhân viên có chức danh chứa ký tự gạch dưới '_'
SELECT ename, job
FROM emp
WHERE job LIKE '%#_%' ESCAPE '#';
-- Ký tự '#' được khai báo là ký tự thoát, khiến '_' phía sau được hiểu là ký tự gạch dưới thực tế, không phải wildcard.
```

---

### 9. GROUP BY와 HAVING 절 — Gom nhóm và lọc điều kiện trên nhóm

`GROUP BY` gom các hàng có cùng giá trị trên các cột được chỉ định thành một nhóm thống kê. Sau khi gom nhóm, dữ liệu chi tiết của từng hàng bị gộp lại và chỉ còn giá trị đại diện của nhóm.

#### Hai quy tắc bất di bất dịch của GROUP BY
1. **Ràng buộc cột trong `SELECT`:** Mọi cột xuất hiện trong mệnh đề `SELECT` **bắt buộc phải nằm trong danh sách các cột của `GROUP BY`** hoặc **phải được bọc bên trong một hàm tổng hợp** (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`). Cố tình chọn một cột đơn lẻ không nằm trong `GROUP BY` sẽ gây lỗi cú pháp (`ORA-00979: not a GROUP BY expression`).
2. **Cấm dùng ALIAS trong `GROUP BY` và `HAVING`:** Vì `GROUP BY` và `HAVING` thực thi trước `SELECT`, hệ thống chưa hề biết đến bí danh cột được đặt trong `SELECT`.

#### Phân biệt rạch ròi WHERE và HAVING

| Tiêu chí đối chiếu | Mệnh đề `WHERE` | Mệnh đề `HAVING` |
| --- | --- | --- |
| **Đối tượng tác động** | Từng dòng dữ liệu độc lập (Row-level) | Từng nhóm sau khi gộp (Group-level) |
| **Vị trí thực thi logic** | Trước `GROUP BY` | Sau `GROUP BY` |
| **Sử dụng hàm tổng hợp** | **TUYỆT ĐỐI CẤM** (`WHERE AVG(sal) > 1000` là LỖI) | **ĐƯỢC PHÉP** (`HAVING AVG(sal) > 1000`) |
| **Mục đích tối ưu** | Loại bỏ dữ liệu thừa sớm để giảm tải tính toán | Lọc bỏ các nhóm không thỏa mãn tiêu chí tổng hợp |

```sql
-- Ví dụ chuẩn về câu lệnh kết hợp đầy đủ:
SELECT deptno,
       COUNT(*)          AS emp_count,
       ROUND(AVG(sal), 2) AS avg_sal
FROM emp
WHERE sal >= 1000                 -- 1. Lọc các nhân viên có lương >= 1000 trước khi gom nhóm
GROUP BY deptno                   -- 2. Gom nhóm theo phòng ban
HAVING COUNT(*) >= 3              -- 3. Chỉ giữ lại các phòng ban có từ 3 nhân viên trở lên
ORDER BY avg_sal DESC;            -- 4. Sắp xếp theo lương trung bình giảm dần
```

> **Ghi chú mở rộng:** Mệnh đề `HAVING` có thể đứng độc lập mà không cần mệnh đề `GROUP BY` tường minh. Khi đó, toàn bộ bảng được coi là một nhóm duy nhất (ví dụ: `SELECT AVG(sal) FROM emp HAVING AVG(sal) > 2000;`).

---

### 10. ORDER BY 절 — Sắp xếp tập kết quả cuối cùng

`ORDER BY` là mệnh đề được thực thi cuối cùng trong câu lệnh SQL, dùng để xác định thứ tự trả về của các dòng bản ghi.

#### Các cách chỉ định cột sắp xếp
1. **Theo tên cột:** `ORDER BY sal DESC, ename ASC`
2. **Theo bí danh cột (Column Alias):** `SELECT sal * 12 AS annual_sal FROM emp ORDER BY annual_sal DESC;` (Hoàn toàn hợp lệ vì `ORDER BY` chạy sau `SELECT`).
3. **Theo vị trí cột (Column Position):** `ORDER BY 1 DESC, 2 ASC` (Số `1` đại diện cho cột thứ nhất trong danh sách `SELECT`). Lưu ý: Dù tiện viết nhanh nhưng không khuyến khích trong hệ thống thật vì dễ lỗi khi thứ tự cột thay đổi.
4. **Theo biểu thức:** `ORDER BY sal + NVL(comm, 0) DESC`

#### Quy tắc xử lý NULL khi sắp xếp giữa Oracle và SQL Server
Đây là một trong những câu hỏi xuất hiện liên tục trong mọi kỳ thi SQLD:

| Hệ quản trị CSDL | Chiều tăng dần (`ASC`) | Chiều giảm dần (`DESC`) | Tùy chọn mở rộng |
| --- | --- | --- | --- |
| **Oracle Database** | `NULL` được coi là **giá trị LỚN NHẤT** $\Rightarrow$ Nằm ở **CUỐI CÙNG** | `NULL` được coi là **giá trị LỚN NHẤT** $\Rightarrow$ Nằm ở **ĐẦU TIÊN** | Cho phép can thiệp bằng `NULLS FIRST` hoặc `NULLS LAST` |
| **SQL Server** | `NULL` được coi là **giá trị NHỎ NHẤT** $\Rightarrow$ Nằm ở **ĐẦU TIÊN** | `NULL` được coi là **giá trị NHỎ NHẤT** $\Rightarrow$ Nằm ở **CUỐI CÙNG** | Không hỗ trợ `NULLS FIRST/LAST` (phải dùng `CASE`) |

```sql
-- Ví dụ trong Oracle: Ép giá trị NULL lên đầu dù đang sắp xếp tăng dần:
SELECT empno, ename, comm
FROM emp
ORDER BY comm ASC NULLS FIRST;
```

---

### 11. Bảng ma trận so sánh toàn diện Oracle vs SQL Server

| Hạng mục chức năng | Oracle Database | Microsoft SQL Server |
| --- | --- | --- |
| **Lấy ngày giờ hiện tại** | `SYSDATE` | `GETDATE()` |
| **Cắt chuỗi con** | `SUBSTR(str, pos, len)` | `SUBSTRING(str, pos, len)` |
| **Đo độ dài chuỗi** | `LENGTH(str)` | `LEN(str)` (bỏ qua khoảng trắng đuôi) |
| **Tìm vị trí ký tự** | `INSTR(str, sub, pos, occ)` | `CHARINDEX(sub, str, start)` |
| **Toán tử chia lấy dư** | `MOD(n, m)` | Toán tử `%` (`n % m`) |
| **Toán tử ghép chuỗi** | Toán tử `||` hoặc `CONCAT(a, b)` | Toán tử `+` hoặc `CONCAT(a, b, ...)` |
| **Xử lý NULL đơn giản** | `NVL(col, default)` | `ISNULL(col, default)` |
| **Rẽ nhánh nhanh** | `DECODE(col, val1, res1, ...)` | Phải dùng cấu trúc `CASE WHEN ...` |
| **Thứ tự NULL mặc định (ASC)** | `NULLS LAST` (NULL xem là lớn nhất) | `NULLS FIRST` (NULL xem là nhỏ nhất) |
| **Từ khóa AS cho Table Alias** | **LỖI CÚ PHÁP** nếu dùng `FROM emp AS e` | Hỗ trợ cả `FROM emp AS e` và `FROM emp e` |
| **Mệnh đề FROM bắt buộc** | Bắt buộc (phải dùng bảng `DUAL` nếu không có bảng) | Không bắt buộc (`SELECT 100 * 2;`) |

---

### 12. Cạm bẫy thi cử trọng điểm (출제 함정 & 오답 노트)

1. **Bẫy bí danh cột trong WHERE và GROUP BY:**
   - *Đề thi hay bẫy:* `SELECT sal * 12 AS total_sal FROM emp WHERE total_sal > 50000;` $\Rightarrow$ **LỖI NGAY TỨC KHẮC!** Vì `WHERE` thực thi trước `SELECT`, bí danh `total_sal` chưa hề được tạo ra.
2. **Bẫy hàm tổng hợp trong WHERE:**
   - *Đề thi hay bẫy:* `SELECT deptno, AVG(sal) FROM emp WHERE AVG(sal) > 2000 GROUP BY deptno;` $\Rightarrow$ **LỖI BIÊN DỊCH!** Hàm tổng hợp chỉ được dùng trong `HAVING` hoặc `SELECT`, không bao giờ được xuất hiện trực tiếp trong `WHERE`.
3. **Bẫy NOT IN chứa giá trị NULL (3-Valued Logic):**
   - *Đề thi hay bẫy:* `WHERE empno NOT IN (10, 20, NULL)` sẽ luôn luôn được đánh giá thành `UNKNOWN` cho mọi dòng dữ liệu, khiến câu truy vấn trả về **0 dòng kết quả (tập rỗng)**.
4. **Bẫy hàm COUNT(column) và giá trị NULL:**
   - `COUNT(*)` đếm tất cả các hàng kể cả hàng chứa toàn `NULL`.
   - `COUNT(comm)` chỉ đếm các hàng có cột `comm` khác `NULL`.
   - `AVG(comm)` chia tổng cho số người có hoa hồng, trong khi `AVG(NVL(comm, 0))` chia tổng cho toàn bộ nhân viên công ty.
5. **Bẫy dấu âm trong SUBSTR:**
   - Trong Oracle, `SUBSTR('ABCDEFG', -3, 2)`: đếm lùi 3 ký tự từ cuối là chữ `'E'`, sau đó trích xuất 2 ký tự xuôi theo chiều đọc bình thường $\Rightarrow$ kết quả là `'EF'`.

---

### 13. Câu hỏi trắc nghiệm thi thử mô phỏng (실전 기출 변형 문제 & 정답 해설)

#### Câu 1: Thứ tự thực thi logic và bí danh cột
Cho câu lệnh SQL sau:
```sql
SELECT deptno AS department_id,
       AVG(sal) AS average_salary
FROM emp
WHERE sal > 1000
GROUP BY department_id
HAVING AVG(sal) >= 2000
ORDER BY average_salary DESC;
```
Phát biểu nào sau đây giải thích chính xác nhất về tính đúng đắn khi thực thi câu lệnh trên trong Oracle Database?
- A. Câu lệnh thực thi thành công vì mọi mệnh đề đều đúng cú pháp chuẩn SQL.
- B. Câu lệnh báo lỗi tại mệnh đề `HAVING` vì không được phép dùng hàm tổng hợp `AVG(sal)`.
- C. Câu lệnh báo lỗi tại mệnh đề `GROUP BY` vì sử dụng bí danh cột `department_id`.
- D. Câu lệnh báo lỗi tại mệnh đề `ORDER BY` vì không được dùng bí danh `average_salary`.

> **Đáp án chính xác:** **C**
>
> **Giải thích chi tiết từng phương án:**
> - **A sai:** Câu lệnh sẽ bị chặn và báo lỗi cú pháp trước khi chạy.
> - **B sai:** Mệnh đề `HAVING` được phép sử dụng hàm tổng hợp để lọc điều kiện nhóm, do đó `HAVING AVG(sal) >= 2000` là cú pháp hoàn toàn hợp lệ.
> - **C đúng:** Theo thứ tự thực thi logic của DBMS, mệnh đề `GROUP BY` (bước 3) thực thi trước mệnh đề `SELECT` (bước 5). Tại thời điểm gom nhóm, bí danh cột `department_id` chưa tồn tại trong bộ nhớ, bắt buộc phải viết `GROUP BY deptno`.
> - **D sai:** Mệnh đề `ORDER BY` (bước 6) thực thi sau cùng, sau khi `SELECT` đã định hình danh sách bí danh, nên việc sử dụng `ORDER BY average_salary DESC` là hoàn toàn hợp lệ.

---

#### Câu 2: Giá trị tính toán của hàm số học và chuỗi
Xét câu lệnh SQL sau được thực thi trên Oracle Database:
```sql
SELECT ROUND(TRUNC(15.789, 1), 0) + MOD(14, 4) + LENGTH(SUBSTR('SQL_DEVELOPER', -9, 3)) AS result
FROM DUAL;
```
Giá quả của cột `result` trả về là bao nhiêu?
- A. 19
- B. 20
- C. 21
- D. 22

> **Đáp án chính xác:** **B**
>
> **Giải thích chi tiết từng thành phần:**
> 1. Thành phần 1: `TRUNC(15.789, 1)` cắt cụt sau chữ số thập phân thứ nhất $\Rightarrow$ được `15.7`. Tiếp tục `ROUND(15.7, 0)` làm tròn đến hàng đơn vị $\Rightarrow$ được **`16`**.
> 2. Thành phần 2: `MOD(14, 4)` lấy số dư của phép chia 14 cho 4 ($14 = 3 \times 4 + 2$) $\Rightarrow$ được **`2`**.
> 3. Thành phần 3: Xét chuỗi `'SQL_DEVELOPER'` có 13 ký tự. Vị trí `-9` đếm lùi từ cuối chuỗi: ký tự cuối cùng là R (-1), E (-2), P (-3), O (-4), L (-5), E (-6), V (-7), E (-8), D (-9). Bắt đầu từ `'D'`, lấy 3 ký tự xuôi về trước $\Rightarrow$ được chuỗi `'DEV'`. Hàm `LENGTH('DEV')` trả về độ dài là **`3`** (hoặc nhận biết ngay tham số thứ 3 của `SUBSTR` là 3 nên độ dài là 3).
> 4. Tổng biểu thức: $16 + 2 + 3 = \mathbf{21}$? Khoan, hãy kiểm tra kỹ lại vị trí âm của `'SQL_DEVELOPER'`:
>    - Chuỗi: `S(1) Q(2) L(3) _(4) D(5) E(6) V(7) E(8) L(9) O(10) P(11) E(12) R(13)`
>    - Chiều lùi: `R(-1), E(-2), P(-3), O(-4), L(-5), E(-6), V(-7), E(-8), D(-9)`. Đúng vị trí là chữ `D`.
>    - Lấy 3 ký tự: `'DEV'`, độ dài là 3.
>    - Phép cộng: $15.7$ làm tròn thành $16$. $16 + 2 + 3 = 21$.
>    - Hãy điều chỉnh đáp án: Phương án C là 21!
>
> **Đáp án chính xác:** **C** (21)

---

#### Câu 3: Logic 3 giá trị (3-Valued Logic) và mệnh đề WHERE
Bảng `EMPLOYEE` có 10 nhân viên, trong đó cột `COMMISSION` có 3 hàng mang giá trị 300, 2 hàng mang giá trị 0, và 5 hàng mang giá trị `NULL`.
Xét câu lệnh truy vấn sau:
```sql
SELECT COUNT(*)
FROM EMPLOYEE
WHERE COMMISSION <> 300;
```
Kết quả trả về của câu lệnh là bao nhiêu?
- A. 7
- B. 5
- C. 2
- D. 0

> **Đáp án chính xác:** **C**
>
> **Giải thích chi tiết:**
> - Phép so sánh `<>` (khác) hoạt động theo Logic 3 giá trị:
>   - Đối với 3 hàng có `COMMISSION = 300`: Biểu thức `300 <> 300` trả về `FALSE` $\Rightarrow$ bị loại.
>   - Đối với 2 hàng có `COMMISSION = 0`: Biểu thức `0 <> 300` trả về `TRUE` $\Rightarrow$ được chọn (**2 hàng**).
>   - Đối với 5 hàng có `COMMISSION IS NULL`: Biểu thức `NULL <> 300` trả về **`UNKNOWN`**! Trong mệnh đề `WHERE`, điều kiện ra `UNKNOWN` sẽ không được thỏa mãn $\Rightarrow$ cả 5 hàng này đều bị loại!
> - Như vậy, chỉ có đúng **2 hàng** thỏa mãn điều kiện `TRUE`. Kết quả `COUNT(*)` là **2**.
> - *Lưu ý:* Nếu muốn lấy cả các hàng NULL, lập trình viên phải viết tường minh: `WHERE COMMISSION <> 300 OR COMMISSION IS NULL;`.

---

#### Câu 4: Phân biệt sắp xếp ORDER BY và cơ chế xử lý NULL
Cho bảng dữ liệu `SCORE_TBL` gồm các bản ghi điểm số như sau:
`SCORE`: `(100, NULL, 85, 90, NULL)`.
Thực thi câu truy vấn sau trên hệ quản trị Oracle Database:
```sql
SELECT SCORE
FROM SCORE_TBL
ORDER BY SCORE DESC;
```
Thứ tự các giá trị điểm số được hiển thị từ trên xuống dưới là:
- A. `NULL`, `NULL`, `100`, `90`, `85`
- B. `100`, `90`, `85`, `NULL`, `NULL`
- C. `NULL`, `100`, `90`, `85`, `NULL`
- D. `85`, `90`, `100`, `NULL`, `NULL`

> **Đáp án chính xác:** **A**
>
> **Giải thích chi tiết:**
> - Trong Oracle Database, giá trị `NULL` mặc định được xem là **giá trị vô cùng lớn (lớn nhất)**.
> - Khi sắp xếp giảm dần (`DESC`), các giá trị lớn nhất sẽ được xếp lên đầu tiên. Do đó, các hàng chứa `NULL` sẽ đứng ở vị trí đầu tiên của tập kết quả.
> - Tiếp theo là các giá trị số sắp xếp giảm dần: `100`, `90`, `85`.
> - Do đó, kết quả chính xác là: `NULL`, `NULL`, `100`, `90`, `85`.
> - *(Ghi chú so sánh: Nếu thực thi câu truy vấn tương tự trên Microsoft SQL Server, do SQL Server coi NULL là giá trị nhỏ nhất, nên khi `DESC` các hàng `NULL` sẽ nằm ở cuối cùng - tương ứng đáp án B)*.

---

## 14. Nối mạch sang Bài tiếp theo: JOIN và liên kết bảng

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 00 đã trang bị đầy đủ cú pháp, thứ tự thực thi logic, hệ thống hàm một hàng phong phú, cơ chế 3-Valued Logic của `WHERE`, kỹ thuật gom nhóm `GROUP BY/HAVING` và các quy tắc sắp xếp `ORDER BY`.
> - **Đang giải quyết gì:** Mọi câu lệnh trong bài này mới chỉ thao tác trên một bảng dữ liệu đơn lẻ. Trong thực tế các hệ thống chuẩn hóa, dữ liệu nghiệp vụ luôn bị phân tán trên nhiều bảng khác nhau. Làm thế nào để ghép nối các hàng từ nhiều bảng lại với nhau một cách chính xác theo tiêu chuẩn quốc tế?
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 01 — JOIN](./01-join.md) để khảo sát chuyên sâu các phép kết nối bảng chuẩn ANSI (`INNER JOIN`, `LEFT/RIGHT/FULL OUTER JOIN`, `CROSS JOIN`, `NATURAL JOIN` và cú pháp `ON` vs `USING`).
