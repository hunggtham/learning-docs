# PIVOT, UNPIVOT và Regular Expression

> **Nguồn bám sát:** PDF *2024 개정판 SQLD 개념정리*, trang 81–84.
>
> **Liên kết bài trước:** Đây là bước biến đổi hình dạng kết quả sau khi đã biết `SELECT`, `GROUP BY` và `JOIN`; nó không thay thế mô hình dữ liệu chuẩn hóa.

## 1. Long Data và Wide Data

> **KR:** Long Data는 하나의 속성값이 여러 행으로 쌓이는 구조이고, Wide Data는 하나의 속성값이 여러 컬럼으로 분리되어 표현되는 구조이다.

Long Data/Tidy Data (dữ liệu dài/gọn) lưu mỗi quan sát thành một hàng, dễ JOIN và phù hợp thiết kế RDBMS. Wide Data/Cross Table (dữ liệu rộng/bảng chéo) dàn giá trị của một thuộc tính thành nhiều cột, tiện cho báo cáo nhưng khó mở rộng khi số cột tăng. `PIVOT` chuyển long → wide; `UNPIVOT` chuyển wide → long.

## 2. PIVOT (Pivot) (xoay hàng thành cột)

> **KR:** PIVOT은 Long Data를 Wide Data로 바꾸어 행 데이터를 열 데이터로 변환한다.

`PIVOT` tổng hợp theo một phép aggregate và đưa các giá trị chỉ định thành tên cột. Hãy chuẩn bị nguồn dữ liệu đúng mức chi tiết bằng subquery/JOIN trước, vì các cột không nằm trong `FOR ... IN` trở thành khóa nhóm ngầm.

```sql
SELECT *
FROM (
  SELECT e.job, d.dname
  FROM emp e JOIN dept d ON e.deptno = d.deptno
)
PIVOT (
  COUNT(*) FOR dname IN (
    'ACCOUNTING' AS accounting,
    'RESEARCH' AS research,
    'SALES' AS sales
  )
);
```

## 3. UNPIVOT (Unpivot) (xoay cột thành hàng)

> **KR:** UNPIVOT은 Wide Data를 Long Data로 바꾸어 열 데이터를 행 데이터로 변환한다.

`UNPIVOT` đưa nhiều cột báo cáo trở lại hai cột: một cột nhãn và một cột giá trị. Đây là cách đưa bảng chéo về dạng dễ filter/JOIN/aggregate hơn.

```sql
SELECT job, department, emp_count
FROM pivot_table
UNPIVOT (
  emp_count FOR department IN (
    accounting AS 'ACCOUNTING',
    research AS 'RESEARCH',
    sales AS 'SALES'
  )
);
```

## 4. 정규 표현식 (Regular Expression) (biểu thức chính quy)

> **KR:** 정규 표현식은 문자열의 공통된 규칙을 일반화하여 특정 패턴을 검색, 매칭 또는 수정하는 강력한 도구이다.

Regex mô tả mẫu văn bản: `.` là một ký tự (trừ newline), `|` là hoặc, `\` escape (thoát nghĩa đặc biệt); `^` là đầu chuỗi, `$` là cuối chuỗi. Quantifier (bộ định lượng) gồm `?` (0/1), `*` (0+), `+` (1+), `{m}` (đúng m), `{m,}` (ít nhất m), `{,m}` (tối đa m), `{m,n}` (m đến n). Character class (lớp ký tự) gồm `[char...]`, `[^char...]`, `[[:digit:]]`, `[[:lower:]]`, `[[:upper:]]`, `[[:alpha:]]`, `[[:alnum:]]`, `[[:space:]]`; dạng rút gọn có `\d`, `\w`, `\s` và dạng phủ định `\D`, `\W`, `\S`.

## 5. Oracle REGEXP functions

> **KR:** REGEXP_LIKE는 패턴 일치 여부를 반환하고, REGEXP_REPLACE는 일치한 패턴을 바꾸며, REGEXP_SUBSTR은 일치한 문자열을 반환한다.

`REGEXP_LIKE(source_char, pattern [, match_param])` lọc/kiểm tra khớp; `REGEXP_REPLACE` thay phần khớp; `REGEXP_SUBSTR` lấy phần khớp; `REGEXP_INSTR` trả vị trí; `REGEXP_COUNT` đếm số lần khớp. Các tham số chung: `source_char` (chuỗi nguồn), `pattern` (mẫu), `position` (vị trí bắt đầu, mặc định 1), `occurrence` (lần khớp, mặc định 1), `match_param` (tùy chọn khớp), `subexpr` (nhóm con). `match_param` PDF nêu `i` bỏ phân biệt hoa/thường, `c` phân biệt, `n` cho `.` khớp newline, `m` ảnh hưởng anchor đa dòng, `x` bỏ qua khoảng trắng trong pattern.

```sql
-- Chỉ nhận mã gồm đúng 3 chữ số
WHERE REGEXP_LIKE(code, '^[[:digit:]]{3}$')

-- Thay mọi dãy khoảng trắng bằng một khoảng trắng
SELECT REGEXP_REPLACE(name, '[[:space:]]+', ' ') FROM person;
```
