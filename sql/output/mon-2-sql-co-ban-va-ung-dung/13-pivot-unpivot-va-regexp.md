<!-- lecture-contract: v2 -->
# PIVOT, UNPIVOT và Regular Expression

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **PIVOT, UNPIVOT và Regular Expression**. Route đi từ Long data vs Wide data → Multi-column / Multi-aggregate `PIVOT` → `UNPIVOT` with NULL handling (`INCLUDE NULLS` vs `EXCLUDE NULLS`) → Deep dive into Oracle Regular Expression functions (`REGEXP_LIKE`, `REGEXP_SUBSTR`, `REGEXP_REPLACE`, `REGEXP_INSTR`, `REGEXP_COUNT`).

> **Mục tiêu:** Nắm vững cơ chế xoay trục dữ liệu giữa dạng dọc (Long data) và ma trận ngang (Wide data), kỹ thuật `PIVOT` nhiều cột và nhiều hàm tổng hợp, cơ chế giữ hoặc loại bỏ `NULL` trong `UNPIVOT`, cùng bộ hàm biểu thức chính quy mạnh mẽ của Oracle SQL trong đề thi SQLD.

> **Phạm vi tham khảo:** PDF *2024 개정판 SQLD 개념정리*, trang 81–84.

---

### 1. Long Data vs Wide Data — Hai dạng cấu trúc dữ liệu

> **KR:** Long 데이터는 하나의 속성값이 여러 행으로 누적되는 구조(Tidy Data)이고, Wide 데이터는 속성값이 여러 컬럼으로 전개되어 표현되는 교차표(Cross Table) 구조이다.

| Đặc tính cấu trúc | Long Data (Dữ liệu dạng dọc) | Wide Data (Dữ liệu ma trận ngang) |
| --- | --- | --- |
| **Bản chất tổ chức** | Mỗi quan sát tương ứng một hàng. Cột ít, hàng nhiều. | Các giá trị của một thuộc tính dàn thành các cột. Cột nhiều, hàng ít. |
| **Tính tương thích RDBMS** | Cực kỳ tối ưu cho `JOIN`, `GROUP BY`, đánh chỉ mục và mở rộng. | Thân thiện cho người dùng xem báo cáo trực quan hoặc trích xuất Excel. |
| **Lệnh chuyển đổi** | Chuyển sang Wide Data bằng mệnh đề **`PIVOT`**. | Chuyển sang Long Data bằng mệnh đề **`UNPIVOT`**. |

---

### 2. PIVOT — Xoay hàng thành cột

> **KR:** PIVOT은 집계 함수와 함께 사용되어 행 데이터를 열 데이터로 회전시키는 연산자이다.

#### 1. Cú pháp PIVOT cơ bản

```sql
SELECT *
FROM (
    SELECT deptno, job, sal
    FROM emp
)
PIVOT (
    SUM(sal)                           -- 1. Hàm tổng hợp bắt buộc
    FOR deptno IN (10 AS dept_10,      -- 2. Cột giá trị xoay thành tên cột mới
                   20 AS dept_20,
                   30 AS dept_30)
);
```

#### Quy tắc thi trắc nghiệm sống còn về PIVOT
1. **Hàm tổng hợp bắt buộc:** `PIVOT` bắt buộc phải chứa ít nhất một hàm tổng hợp (`SUM`, `COUNT`, `AVG`, `MAX`, `MIN`).
2. **Cơ chế gom nhóm ngầm định (Implicit GROUP BY):** Mọi cột trong bảng hoặc Inline View nguồn **không nằm trong hàm tổng hợp** và **không nằm trong mệnh đề `FOR`** sẽ tự động trở thành các cột gom nhóm (`GROUP BY`). Do đó, luôn dùng Subquery / Inline View để lọc chính xác các cột cần thiết trước khi đưa vào `PIVOT`.

#### 2. Cú pháp PIVOT nâng cao

#### Kịch bản A: PIVOT nhiều cột gom nhóm trong mệnh đề `FOR`
Khi cần xoay đồng thời nhiều thuộc tính thành cột mới (ví dụ vừa phân theo phòng ban, vừa phân theo năm tuyển dụng):

```sql
SELECT *
FROM (
    SELECT job, deptno, EXTRACT(YEAR FROM hiredate) AS hire_year, sal
    FROM emp
)
PIVOT (
    SUM(sal)
    FOR (deptno, hire_year) IN (
        (10, 2025) AS d10_y2025,
        (10, 2026) AS d10_y2026,
        (20, 2025) AS d20_y2025,
        (20, 2026) AS d20_y2026
    )
);
```

#### Kịch bản B: PIVOT nhiều hàm tổng hợp (Multi-aggregate PIVOT)
Khi muốn xem đồng thời cả tổng lương (`SUM`) và số lượng nhân viên (`COUNT`) cho mỗi phòng ban:

```sql
SELECT *
FROM (
    SELECT job, deptno, sal
    FROM emp
)
PIVOT (
    SUM(sal) AS sum_sal,
    COUNT(*) AS emp_cnt
    FOR deptno IN (
        10 AS d10,
        20 AS d20,
        30 AS d30
    )
);
```

- **Quy tắc sinh tên cột kết quả của Oracle:** Tên cột mới được ghép theo mẫu `<alias_giá_trị>_<alias_hàm>`.
- Câu lệnh trên sẽ tự động sinh ra 6 cột mới: `D10_SUM_SAL`, `D10_EMP_CNT`, `D20_SUM_SAL`, `D20_EMP_CNT`, `D30_SUM_SAL`, `D30_EMP_CNT`.

---

### 3. UNPIVOT — Xoay cột thành hàng & Cơ chế xử lý NULL

> **KR:** UNPIVOT은 가로로 전개된 여러 컬럼을 세로 형태의 행 데이터로 환원시키는 연산자이다. 기본적으로 NULL 값을 제외(EXCLUDE NULLS)하지만 명시적으로 포함(INCLUDE NULLS)할 수 있다.

```sql
SELECT job, deptno, total_sal
FROM sales_summary_wide
UNPIVOT [INCLUDE NULLS | EXCLUDE NULLS] (
    total_sal                          -- Tên cột mới chứa GIÁ TRỊ đo lường
    FOR deptno IN (dept_10 AS 10,      -- Tên cột mới chứa TÊN THUỘC TÍNH
                   dept_20 AS 20,
                   dept_30 AS 30)
);
```

#### So sánh cơ chế INCLUDE NULLS vs EXCLUDE NULLS trong đề thi

| Tùy chọn xử lý NULL | Hành vi thực thi | Ứng dụng thực tế |
| --- | --- | --- |
| **`EXCLUDE NULLS`** (Mặc định) | Tự động **loại bỏ các hàng** mà cột giá trị đo lường mang giá trị `NULL`. | Giảm kích thước tập dữ liệu, loại bỏ dữ liệu trống không có phát sinh giao dịch. |
| **`INCLUDE NULLS`** | **Giữ lại nguyên vẹn** các hàng có giá trị đo lường là `NULL`. | Bảo toàn đầy đủ ma trận dữ liệu phân tích, giúp nhận biết những ô không có dữ liệu. |

> **Bẫy đề thi:** Nếu một hàng trong bảng ngang có giá trị `dept_30` là `NULL`:
> - Dưới chế độ mặc định (`EXCLUDE NULLS`), hàng đó sẽ chỉ sinh ra 2 dòng ở kết quả đầu ra (chỉ chứa `dept_10` và `dept_20`).
> - Dưới chế độ `INCLUDE NULLS`, kết quả sẽ sinh ra đủ 3 dòng, trong đó dòng cho phòng 30 có cột `total_sal` mang giá trị `NULL`.

---

### 4. 정규 표현식 (Regular Expression) — Các ký tự siêu mẫu

> **KR:** 정규 표현식은 문자열의 공통된 규칙을 패턴화하여 복잡한 문자열 검색, 유효성 검증, 치환을 수행하는 강력한 도구이다.

- **Ký tự định vị & ranh giới (Anchors):**
  - `^`: Bắt đầu chuỗi.
  - `$`: Kết thúc chuỗi.
  - `.`: Đại diện cho đúng 1 ký tự bất kỳ (ngoại trừ ký tự ngắt dòng).
- **Bộ định lượng (Quantifiers):**
  - `?`: Xuất hiện 0 hoặc 1 lần.
  - `*`: Xuất hiện 0 hoặc nhiều lần.
  - `+`: Xuất hiện 1 hoặc nhiều lần.
  - `{m, n}`: Xuất hiện tối thiểu $m$ lần, tối đa $n$ lần.
- **Lớp ký tự chuẩn (POSIX Character Classes):**
  - `[[:digit:]]` hoặc `\d`: Chữ số (`0-9`).
  - `[[:alpha:]]`: Chữ cái (`a-z`, `A-Z`).
  - `[[:alnum:]]`: Chữ cái hoặc chữ số.
  - `[[:space:]]` hoặc `\s`: Ký tự khoảng trắng (space, tab, enter).

---

### 5. Bộ 5 hàm Regular Expression trong Oracle SQL

Oracle cung cấp 5 hàm biểu thức chính quy mạnh mẽ phục vụ mọi tác vụ chuỗi:

#### 1. `REGEXP_LIKE(source_char, pattern [, match_param])`
Kiểm tra chuỗi có khớp mẫu hay không, trả về giá trị Boolean dùng trực tiếp trong mệnh đề `WHERE`:

```sql
-- Tìm nhân viên có số điện thoại đúng chuẩn Hàn Quốc (ví dụ: 010-1234-5678)
SELECT ename, phone_number
FROM emp
WHERE REGEXP_LIKE(phone_number, '^010-[0-9]{4}-[0-9]{4}$');
```

#### 2. `REGEXP_SUBSTR(source_char, pattern [, position [, occurrence [, match_param [, subexpr]]]])`
Trích xuất chuỗi con thỏa mãn mẫu:
- `position`: Vị trí bắt đầu tìm kiếm (mặc định 1).
- `occurrence`: Thứ tự lần xuất hiện khớp mẫu cần lấy (mặc định 1).
- `subexpr`: Số thứ tự của nhóm ngoặc đơn `( )` cần trích xuất (0 là toàn bộ mẫu, 1 là nhóm thứ nhất).

```sql
-- Trích xuất tên miền từ địa chỉ email
SELECT REGEXP_SUBSTR('contact@oracle.com', '@([[:alnum:]]+)\.', 1, 1, 'i', 1) AS domain_name
FROM dual;
-- Kết quả: 'oracle'
```

#### 3. `REGEXP_REPLACE(source_char, pattern [, replace_string [, position [, occurrence [, match_param]]]])`
Tìm kiếm đoạn chuỗi khớp mẫu và thay thế bằng chuỗi mới:

```sql
-- Chuẩn hóa nhiều khoảng trắng liên tiếp thành đúng 1 khoảng trắng
SELECT REGEXP_REPLACE('SQLD    Exam   2026', '\s+', ' ') AS clean_text
FROM dual;
-- Kết quả: 'SQLD Exam 2026'

-- Che 4 số cuối của số điện thoại bằng dấu '*'
SELECT REGEXP_REPLACE('010-1234-5678', '(\d{4})$', '****') AS masked_phone
FROM dual;
-- Kết quả: '010-1234-****'
```

#### 4. `REGEXP_INSTR(source_char, pattern [, position [, occurrence [, return_opt [, match_param [, subexpr]]]]])`
Trả về vị trí (1-based index) của mẫu xuất hiện trong chuỗi:
- `return_opt`: `0` (trả về vị trí ký tự đầu tiên của mẫu - mặc định); `1` (trả về vị trí ký tự ngay sau vị trí kết thúc của mẫu).

```sql
-- Tìm vị trí bắt đầu của chuỗi số trong mã sản phẩm
SELECT REGEXP_INSTR('ITEM_2026_PROD', '\d+') AS num_start_pos
FROM dual;
-- Kết quả: 6 (chữ số '2' bắt đầu ở vị trí thứ 6)
```

#### 5. `REGEXP_COUNT(source_char, pattern [, position [, match_param]])`
Đếm tổng số lần mẫu xuất hiện trong chuỗi nguồn:

```sql
SELECT REGEXP_COUNT('abc@test.com, xyz@oracle.com, dev@sql.org', '@') AS email_count
FROM dual;
-- Kết quả: 3
```

#### Bảng tham số tùy chọn so khớp (`match_param`)

| Ký tự tùy chọn | Ý nghĩa kỹ thuật | Điểm thi trọng tâm |
| --- | --- | --- |
| **`'c'`** | Phân biệt chữ hoa / chữ thường (Case-sensitive). | Đây là giá trị **mặc định** của Oracle. |
| **`'i'`** | **Không phân biệt** chữ hoa / chữ thường (Case-insensitive). | Tìm kiếm linh hoạt chữ hoa lẫn chữ thường. |
| **`'m'`** | Chế độ nhiều dòng (Multi-line mode). | Khiến `^` và `$` khớp ở đầu và cuối của **mỗi dòng**. |
| **`'n'`** | Cho phép dấu chấm `.` khớp ký tự xuống dòng (Newline). | Mặc định dấu `.` không khớp với ký tự newline. |
| **`'x'`** | Bỏ qua khoảng trắng bên trong biểu thức chính quy. | Giúp định dạng mẫu regex phức tạp dễ đọc hơn. |

---

## 6. Nối mạch sang Bài tiếp theo: SQL Style Guide và viết truy vấn sạch

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 13 đã hoàn tất toàn bộ các kỹ thuật biến đổi trục dữ liệu nâng cao (`PIVOT`/`UNPIVOT`) và bộ hàm biểu thức chính quy `REGEXP_*`.
> - **Đang giải quyết gì:** Trong môi trường dự án doanh nghiệp lớn (Enterprise) và pipeline tích hợp AI, làm thế nào để quy chuẩn hóa mã SQL, đặt tên alias chuẩn mực, thụt lề mệnh đề `WHERE` rõ ràng và đặc biệt là phòng tránh các bẫy Anti-patterns làm vô hiệu hóa Index?
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 14 — SQL Style Guide và SQL dễ đọc cho pipeline AI](./14-sql-style-guide.md) để đúc kết toàn diện các quy chuẩn viết SQL chuyên nghiệp chuẩn Enterprise.
