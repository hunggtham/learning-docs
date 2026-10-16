# JOIN

Để JOIN **thực sự dễ nhớ**, đừng bắt đầu bằng cú pháp. Hãy nhớ một ý duy nhất:

> **JOIN = ghép các dòng của nhiều bảng dựa trên một điều kiện liên quan.**

Trong SQLD/Oracle, phần dễ nhầm nhất là: **INNER JOIN, LEFT/RIGHT/FULL OUTER JOIN, CROSS JOIN, SELF JOIN, NATURAL JOIN**, và **EQUI/NON-EQUI JOIN**. Mình sẽ đi từ bản chất → ví dụ → kết quả → cách phân biệt.

---

## 1. Tại sao cần JOIN?

Giả sử database có 2 bảng.

#### EMPLOYEES
Phần này nối mạch SQL với “EMPLOYEES”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

| EMP_ID | NAME  | DEPT_ID |
| -----: | ----- | ------: |
|      1 | An    |      10 |
|      2 | Bình  |      20 |
|      3 | Cường |      30 |
|      4 | Dũng  |    NULL |

#### DEPARTMENTS
Phần này nối mạch SQL với “DEPARTMENTS”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

| DEPT_ID | DEPT_NAME |
| ------: | --------- |
|      10 | IT        |
|      20 | HR        |
|      40 | SALES     |

Ta thấy:

* An → phòng 10 → IT
* Bình → phòng 20 → HR
* Cường → phòng 30, nhưng **DEPARTMENTS không có 30**
* Dũng → chưa thuộc phòng nào
* SALES → phòng 40, nhưng **không có employee nào**

Nếu muốn:

> "Cho tôi tên nhân viên + tên phòng ban"

thì một bảng không đủ.

Ta phải nối:

```text
EMPLOYEES.DEPT_ID
        ↓
        ↓ JOIN
        ↓
DEPARTMENTS.DEPT_ID
```

Điều kiện thường là:

```sql
e.dept_id = d.dept_id
```

Nhưng vấn đề quan trọng là:

> Nếu không tìm được đối tượng tương ứng thì có giữ dòng đó lại không?

**Câu hỏi này chính là thứ tạo ra INNER / LEFT / RIGHT / FULL JOIN.**

---

## 2. INNER JOIN — chỉ lấy những dòng "match"

### 핵심

**INNER JOIN = 양쪽 테이블에서 조인 조건을 만족하는 행만 반환한다.**

**INNER JOIN = Chỉ lấy những dòng tìm được cặp tương ứng ở cả hai bảng.**

Ví dụ:

```sql
SELECT e.emp_id,
       e.name,
       d.dept_name
FROM employees e
INNER JOIN departments d
    ON e.dept_id = d.dept_id;
```

SQL sẽ kiểm tra:

```text
An      dept 10 → có 10 → IT       ✓
Bình    dept 20 → có 20 → HR       ✓
Cường   dept 30 → không có         ✗
Dũng    NULL    → không match      ✗
```

Kết quả:

| EMP_ID | NAME | DEPT_NAME |
| -----: | ---- | --------- |
|      1 | An   | IT        |
|      2 | Bình | HR        |

Phòng SALES cũng không xuất hiện vì không có employee tương ứng.

#### Hình dung
Phần này nối mạch SQL với “Hình dung”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
EMPLOYEES              DEPARTMENTS

An     10  ─────────── 10 IT
Bình   20  ─────────── 20 HR
Cường  30              40 SALES
Dũng   NULL
```

Chỉ hai đường nối thành công được giữ.

#### Cách nhớ

> **INNER = MATCH ONLY**

hay:

```text
A ∩ B
```

---

## 3. JOIN và INNER JOIN có khác nhau không?

Thông thường:

```sql
SELECT *
FROM employees e
JOIN departments d
    ON e.dept_id = d.dept_id;
```

tương đương:

```sql
SELECT *
FROM employees e
INNER JOIN departments d
    ON e.dept_id = d.dept_id;
```

Vì khi chỉ viết:

```sql
JOIN
```

thì mặc định là:

```sql
INNER JOIN
```

---

## 4. LEFT OUTER JOIN — giữ toàn bộ bảng bên trái

Đây là JOIN cực kỳ quan trọng.

### 핵심

**LEFT OUTER JOIN은 왼쪽 테이블의 모든 행을 유지한다.**

**LEFT JOIN giữ toàn bộ dòng của bảng bên trái, kể cả khi không tìm được dữ liệu tương ứng bên phải.**

```sql
SELECT e.emp_id,
       e.name,
       d.dept_name
FROM employees e
LEFT JOIN departments d
    ON e.dept_id = d.dept_id;
```

Quan trọng là nhìn `FROM`:

```sql
FROM employees e        ← LEFT
LEFT JOIN departments d ← RIGHT
```

Vì vậy:

> **EMPLOYEES phải được giữ lại toàn bộ.**

SQL xử lý:

```text
An      10 → IT       ✓
Bình    20 → HR       ✓
Cường   30 → ???      không có → NULL
Dũng   NULL → ???     không có → NULL
```

Kết quả:

| EMP_ID | NAME  | DEPT_NAME |
| -----: | ----- | --------- |
|      1 | An    | IT        |
|      2 | Bình  | HR        |
|      3 | Cường | NULL      |
|      4 | Dũng  | NULL      |

Chú ý:

```text
Cường vẫn tồn tại
Dũng vẫn tồn tại
```

Đây chính là khác biệt lớn với INNER JOIN.

#### Cách nhớ
Phần này nối mạch SQL với “Cách nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
LEFT JOIN
    ↓
KEEP LEFT
```

Hay:

> **LEFT JOIN = bên trái là VIP → không được phép mất dòng.**

---

## 5. RIGHT OUTER JOIN — giữ toàn bộ bảng bên phải

Ngược lại:

```sql
SELECT e.name,
       d.dept_id,
       d.dept_name
FROM employees e
RIGHT JOIN departments d
    ON e.dept_id = d.dept_id;
```

Ở đây:

```text
employees   = LEFT
departments = RIGHT
```

RIGHT JOIN nghĩa là:

> Giữ toàn bộ `departments`.

Kết quả:

| NAME | DEPT_ID | DEPT_NAME |
| ---- | ------: | --------- |
| An   |      10 | IT        |
| Bình |      20 | HR        |
| NULL |      40 | SALES     |

Tại sao SALES xuất hiện?

Vì:

```text
DEPARTMENTS

10 IT      → An
20 HR      → Bình
40 SALES   → không có employee
             ↓
             vẫn phải giữ vì RIGHT JOIN
```

Employee không tồn tại nên:

```text
NAME = NULL
```

---

## 6. LEFT JOIN và RIGHT JOIN thực chất có thể đổi cho nhau

Ví dụ:

```sql
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.dept_id
```

có thể viết thành:

```sql
FROM departments d
RIGHT JOIN employees e
ON e.dept_id = d.dept_id
```

Ý nghĩa tương đương.

Vì vậy trong code thực tế, nhiều developer chủ yếu dùng:

```sql
INNER JOIN
LEFT JOIN
```

và ít dùng RIGHT JOIN, vì có thể đảo thứ tự bảng để đọc dễ hơn.

---

## 7. FULL OUTER JOIN — không bỏ ai cả

### 핵심

**FULL OUTER JOIN은 양쪽 테이블의 모든 행을 유지한다.**

**FULL OUTER JOIN giữ tất cả dòng của cả hai bảng.**

```sql
SELECT e.name,
       e.dept_id AS emp_dept,
       d.dept_id,
       d.dept_name
FROM employees e
FULL OUTER JOIN departments d
    ON e.dept_id = d.dept_id;
```

Ta có:

```text
An      10 → IT       match
Bình    20 → HR       match

Cường   30 → ???      không match nhưng vẫn giữ
Dũng   NULL → ???     không match nhưng vẫn giữ

???        → 40 SALES không match nhưng vẫn giữ
```

Kết quả đại khái:

| NAME  | EMP_DEPT | DEPT_ID | DEPT_NAME |
| ----- | -------: | ------: | --------- |
| An    |       10 |      10 | IT        |
| Bình  |       20 |      20 | HR        |
| Cường |       30 |    NULL | NULL      |
| Dũng  |     NULL |    NULL | NULL      |
| NULL  |     NULL |      40 | SALES     |

#### Cách nhớ
Phần này nối mạch SQL với “Cách nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
INNER = chỉ MATCH
LEFT  = MATCH + LEFT dư
RIGHT = MATCH + RIGHT dư
FULL  = MATCH + LEFT dư + RIGHT dư
```

Đây là công thức nên nhớ nhất.

---

## 8. So sánh 4 loại JOIN quan trọng nhất

Với:

```text
A = bảng bên trái
B = bảng bên phải
```

| JOIN            | Dòng match | A không match | B không match |
| --------------- | :--------: | :-----------: | :-----------: |
| INNER JOIN      |      ✅     |       ❌       |       ❌       |
| LEFT JOIN       |      ✅     |       ✅       |       ❌       |
| RIGHT JOIN      |      ✅     |       ❌       |       ✅       |
| FULL OUTER JOIN |      ✅     |       ✅       |       ✅       |

Chỉ cần nhớ bảng này là xử lý được phần lớn câu hỏi JOIN.

---

## 9. CROSS JOIN — tất cả kết hợp với tất cả

CROSS JOIN hoàn toàn khác.

```sql
SELECT *
FROM employees
CROSS JOIN departments;
```

Không có:

```sql
ON ...
```

vì SQL không tìm "cặp phù hợp".

Nó làm:

> **Mỗi dòng A kết hợp với tất cả dòng B.**

Giả sử:

```text
EMPLOYEES

An
Bình
Cường
```

và:

```text
DEPARTMENTS

IT
HR
```

CROSS JOIN:

```text
An     IT
An     HR

Bình   IT
Bình   HR

Cường  IT
Cường  HR
```

Nếu:

```text
A = 3 rows
B = 2 rows
```

thì:

```text
3 × 2 = 6 rows
```

Nếu:

```text
A = 1000 rows
B = 500 rows
```

thì:

```text
1000 × 500
= 500,000 rows
```

Đây gọi là:

**카티션 곱 (Cartesian Product) — tích Descartes.**

#### Cách nhớ

> **CROSS JOIN = A × B**

---

## 10. CROSS JOIN rất quan trọng để hiểu lỗi JOIN

Ví dụ vô tình viết:

```sql
SELECT *
FROM employees e, departments d;
```

mà không có:

```sql
WHERE e.dept_id = d.dept_id
```

thì sẽ tạo Cartesian Product.

Ví dụ:

```text
EMPLOYEE 100 rows
DEPARTMENT 20 rows

→ 2,000 rows
```

Đây là một lỗi SQL phổ biến.

---

## 11. SELF JOIN — bảng JOIN với chính nó

SELF JOIN không phải một thuật toán JOIN hoàn toàn mới.

Nó có nghĩa:

> **Một bảng đóng hai vai trò khác nhau rồi JOIN với chính nó.**

Ví dụ bảng:

#### EMPLOYEES
Phần này nối mạch SQL với “EMPLOYEES”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

| EMP_ID | NAME | MANAGER_ID |
| -----: | ---- | ---------: |
|      1 | Kim  |       NULL |
|      2 | Lee  |          1 |
|      3 | Park |          1 |
|      4 | Choi |          2 |

Ý nghĩa:

```text
Lee.manager_id = 1
→ manager của Lee là employee 1
→ Kim
```

Ta muốn:

```text
Employee | Manager
```

thì cần đọc `EMPLOYEES` hai lần:

```sql
SELECT e.name AS employee,
       m.name AS manager
FROM employees e
LEFT JOIN employees m
    ON e.manager_id = m.emp_id;
```

Ở đây:

```text
employees e
```

đóng vai:

```text
nhân viên
```

còn:

```text
employees m
```

đóng vai:

```text
manager
```

Tưởng tượng như tạo hai bản sao logic:

```text
EMPLOYEES e                 EMPLOYEES m

Lee   manager=1 ─────────→ Kim emp_id=1
Park  manager=1 ─────────→ Kim emp_id=1
Choi  manager=2 ─────────→ Lee emp_id=2
```

Kết quả:

| EMPLOYEE | MANAGER |
| -------- | ------- |
| Kim      | NULL    |
| Lee      | Kim     |
| Park     | Kim     |
| Choi     | Lee     |

#### Keyword

**셀프 조인 (Self Join)**
= 동일한 테이블을 자기 자신과 조인하는 방식.

**Self Join**
= JOIN một bảng với chính nó.

---

## 12. SELF JOIN vẫn có thể là INNER/LEFT JOIN

Đây là điểm dễ hiểu sai.

`SELF JOIN` mô tả:

> **JOIN bảng nào?**

Còn `INNER/LEFT/RIGHT` mô tả:

> **Giữ những dòng nào?**

Cho nên có thể có:

```sql
FROM employees e
INNER JOIN employees m
    ON ...
```

hoặc:

```sql
FROM employees e
LEFT JOIN employees m
    ON ...
```

Cả hai đều là SELF JOIN.

Ví dụ Kim không có manager:

```text
Kim.manager_id = NULL
```

Nếu INNER JOIN:

```sql
INNER JOIN employees m
ON e.manager_id = m.emp_id
```

Kim biến mất.

Nếu LEFT JOIN:

```sql
LEFT JOIN employees m
ON e.manager_id = m.emp_id
```

Kim vẫn còn:

```text
Kim | NULL
```

---

## 13. EQUI JOIN — điều kiện JOIN dùng dấu `=`

**등가 조인 (Equi Join)** nghĩa là điều kiện JOIN sử dụng phép bằng:

```sql
=
```

Ví dụ:

```sql
SELECT *
FROM employees e
JOIN departments d
    ON e.dept_id = d.dept_id;
```

Đây là:

```text
e.dept_id = d.dept_id
          ↑
          =
```

→ EQUI JOIN.

Phần lớn JOIN khóa ngoại/khóa chính mà bạn gặp là EQUI JOIN.

Ví dụ:

```text
EMPLOYEES.department_id
        ↓ FK

DEPARTMENTS.department_id
        ↑ PK
```

JOIN:

```sql
ON e.department_id = d.department_id
```

---

## 14. NON-EQUI JOIN — không JOIN bằng `=`

**비등가 조인 (Non-Equi Join)**

là JOIN bằng:

```text
>
<
>=
<=
BETWEEN
...
```

Ví dụ rất kinh điển trong SQLD.

Có bảng nhân viên:

| NAME  | SALARY |
| ----- | -----: |
| An    |   2500 |
| Bình  |   4500 |
| Cường |   7000 |

và bảng mức lương:

#### SALARY_GRADE
Phần này nối mạch SQL với “SALARY_GRADE”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

| GRADE | MIN_SAL | MAX_SAL |
| ----: | ------: | ------: |
|     1 |       0 |    2999 |
|     2 |    3000 |    4999 |
|     3 |    5000 |    7999 |

Không thể JOIN:

```sql
salary = min_sal
```

vì salary 4500 không bằng 3000.

Ta cần:

```sql
SELECT e.name,
       e.salary,
       g.grade
FROM employees e
JOIN salary_grade g
    ON e.salary BETWEEN g.min_sal AND g.max_sal;
```

Ví dụ:

```text
An
salary = 2500

0 <= 2500 <= 2999

→ Grade 1
```

```text
Bình
salary = 4500

3000 <= 4500 <= 4999

→ Grade 2
```

```text
Cường
salary = 7000

5000 <= 7000 <= 7999

→ Grade 3
```

Kết quả:

| NAME  | SALARY | GRADE |
| ----- | -----: | ----: |
| An    |   2500 |     1 |
| Bình  |   4500 |     2 |
| Cường |   7000 |     3 |

#### Nhớ
Phần này nối mạch SQL với “Nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
EQUI JOIN
    ↓
=

NON-EQUI JOIN
    ↓
>, <, >=, <=, BETWEEN...
```

---

## 15. NATURAL JOIN (네추럴 조인)

NATURAL JOIN là loại cú pháp chuẩn ANSI rất hay xuất hiện trong các câu hỏi bẫy cú pháp của SQLD.

**KR:** NATURAL JOIN은 두 테이블에서 이름과 데이터 타입이 같은 모든 컬럼을 기준으로 EQUI JOIN을 자동으로 수행한다.
**VI:** NATURAL JOIN tự động tìm **tất cả các cột có cùng tên và cùng kiểu dữ liệu** giữa hai bảng để thực hiện EQUI JOIN.

Ví dụ hai bảng:

```text
EMPLOYEES (사원 테이블)
-----------------------
EMP_ID   (NUMBER)
NAME     (VARCHAR2)
DEPT_ID  (NUMBER)

DEPARTMENTS (부서 테이블)
-----------------------
DEPT_ID   (NUMBER)
DEPT_NAME (VARCHAR2)
```

Hai bảng có cột chung duy nhất là `DEPT_ID` (cùng tên, cùng kiểu `NUMBER`):

```sql
SELECT *
FROM employees
NATURAL JOIN departments;
```

SQL tự động hiểu và ghép dòng theo điều kiện `employees.DEPT_ID = departments.DEPT_ID`.

### ⚠️ Cạm bẫy thi cử SQLD số 1: TUYỆT ĐỐI KHÔNG DÙNG ALIAS TRƯỚC CỘT JOIN

Đây là bẫy phổ biến nhất trong đề thi:
- Trong `NATURAL JOIN`, các cột dùng làm khóa join trở thành **cột chung sở hữu bởi cả hai bảng**.
- Do đó, trong mệnh đề `SELECT`, `WHERE`, hoặc bất kỳ đâu, **tuyệt đối không được gắn tiền tố tên bảng hoặc alias** vào cột join.

```sql
-- ❌ SAI (Gây lỗi ORA-25155: column used in NATURAL JOIN cannot have qualifier)
SELECT e.emp_id, e.name, e.dept_id, d.dept_name
FROM employees e
NATURAL JOIN departments d;

-- ✅ ĐÚNG (Cột dept_id không được có tiền tố e. hay d.)
SELECT e.emp_id, e.name, dept_id, d.dept_name
FROM employees e
NATURAL JOIN departments d;
```

### ⚠️ Cạm bẫy thi cử SQLD số 2: Thứ tự cột khi dùng SELECT *

Khi thực hiện `SELECT *` với `NATURAL JOIN`:
1. Cột chung (cột tham gia join) luôn **xuất hiện đầu tiên** và chỉ xuất hiện **đúng 1 lần** (không bị lặp lại 2 lần như INNER JOIN thông thường).
2. Tiếp theo là các cột còn lại của bảng thứ nhất (bảng bên trái).
3. Cuối cùng là các cột còn lại của bảng thứ hai (bảng bên phải).

---

## 16. Tại sao NATURAL JOIN nguy hiểm trong thực tế?

Giả sử ban đầu hệ thống chỉ có `DEPT_ID` cùng tên giữa 2 bảng:

```text
EMPLOYEES:   EMP_ID, NAME, DEPT_ID
DEPARTMENTS: DEPT_ID, DEPT_NAME
```

NATURAL JOIN join chính xác theo `DEPT_ID`. Nhưng sau đó, DBA bổ sung cột `UPD_DATE` (ngày cập nhật) hoặc `LOC_ID` vào cả hai bảng:

```text
EMPLOYEES:   EMP_ID, NAME, DEPT_ID, LOC_ID
DEPARTMENTS: DEPT_ID, DEPT_NAME, LOC_ID
```

Lúc này, `NATURAL JOIN` sẽ tự động chuyển thành:

```sql
WHERE employees.DEPT_ID = departments.DEPT_ID
  AND employees.LOC_ID = departments.LOC_ID
```

Hệ quả:
- Ý nghĩa nghiệp vụ bị thay đổi hoàn toàn ngoài dự kiến.
- Số lượng bản ghi trả về có thể đột ngột giảm xuống 0 (vì `LOC_ID` của nhân viên có thể khác `LOC_ID` của phòng ban).
- Nếu hai cột cùng tên nhưng **khác kiểu dữ liệu** (ví dụ một bên `VARCHAR2`, một bên `NUMBER`), Oracle sẽ báo lỗi không thực thi được.

---

## 17. USING — Cú pháp chỉ định chính xác cột JOIN cùng tên

Mệnh đề `USING` ra đời để khắc phục sự nguy hiểm của `NATURAL JOIN`. Khi hai bảng có nhiều cột cùng tên, nhưng ta chỉ muốn join theo một (hoặc một số) cột nhất định:

```sql
SELECT emp_id, name, dept_id, dept_name
FROM employees e
JOIN departments d
USING (dept_id);
```

### ⚠️ Các quy tắc bất di bất dịch của USING trong đề thi SQLD

1. **Bắt buộc phải có dấu ngoặc đơn `( )`**:
   - `USING (dept_id)` → Hợp lệ.
   - `USING dept_id` → LỖI CÚ PHÁP (Syntax Error).
2. **CẤM dùng Alias / Table Prefix trước cột trong USING**:
   - Tương tự NATURAL JOIN, cột trong danh sách `USING` trở thành cột chung.
   - Trong `SELECT`, nếu viết `e.dept_id` hoặc `d.dept_id` sẽ báo lỗi `ORA-25154: column part of USING clause cannot have qualifier`.
   - Phải viết trần: `SELECT dept_id ...`.
3. **CẤM dùng đồng thời `USING` và `ON`**:
   - Trong cùng một mệnh đề JOIN của hai bảng, chỉ được chọn hoặc dùng `ON`, hoặc dùng `USING`. Không được kết hợp cả hai.

### So sánh mức độ kiểm soát giữa ON, USING và NATURAL JOIN

| Tiêu chí | NATURAL JOIN | USING (cột) | ON điều kiện |
| :--- | :--- | :--- | :--- |
| **Cột JOIN** | Tự động quét mọi cột cùng tên & kiểu | Chỉ định cụ thể danh sách cột cùng tên | Tự do chỉ định bất kỳ cột nào |
| **Tên cột 2 bảng** | Bắt buộc phải trùng tên | Bắt buộc phải trùng tên | Có thể trùng hoặc khác tên |
| **Dấu ngoặc đơn** | Không có | Bắt buộc: `(col1, col2)` | Tùy chọn: `ON (e.id = d.id)` |
| **Alias trong SELECT** | **CẤM** dùng alias trên cột join | **CẤM** dùng alias trên cột join | **BẮT BUỘC** hoặc nên dùng alias để tránh nhập nhằng |
| **Mức độ khuyên dùng** | Thấp nhất (rủi ro cao) | Trung bình | Cao nhất (chuẩn mực dự án) |

---

## 18. ANSI JOIN và Oracle Old-Style JOIN

Đề thi SQLD thường xuyên yêu cầu chuyển đổi qua lại giữa cú pháp chuẩn ANSI (ANSI Standard SQL: 1999) và cú pháp truyền thống của Oracle.

### Cú pháp ANSI Standard JOIN
```sql
SELECT e.name, d.dept_name
FROM employees e
INNER JOIN departments d
   ON e.dept_id = d.dept_id;
```

### Cú pháp Oracle Old-Style (Non-ANSI)
```sql
SELECT e.name, d.dept_name
FROM employees e,
     departments d
WHERE e.dept_id = d.dept_id;
```
Ở cú pháp Oracle cũ, các bảng liệt kê ngăn cách bởi dấu phẩy trong `FROM`, và điều kiện kết nối được đặt chung với điều kiện lọc trong `WHERE`.

---

## 19. Oracle `(+)` Outer Join — Bản chất và 4 Cấm kỵ sống còn

Trong cú pháp Oracle cũ, toán tử Outer Join được ký hiệu bằng `(+)`.

### Bản chất của ký hiệu `(+)`

**KR:** `(+)` 기호는 데이터가 부족한(NULL로 보충되어야 하는) 쪽에 붙인다.
**VI:** Dấu `(+)` luôn được đặt ở phía **thiếu dữ liệu** (phía cần được điền thêm các dòng NULL để ghép với bảng đầy đủ).

```sql
-- ANSI: Giữ toàn bộ EMPLOYEES, DEPARTMENTS thiếu thì điền NULL
SELECT e.name, d.dept_name
FROM employees e
LEFT OUTER JOIN departments d
   ON e.dept_id = d.dept_id;

-- Oracle Old-Style tương đương:
SELECT e.name, d.dept_name
FROM employees e, departments d
WHERE e.dept_id = d.dept_id(+);
```

#### Mẹo ghi nhớ vị trí dấu `(+)`
- Phía có `(+)` = Phía yếu thế hơn = Phía bị thiếu dòng = Phía nhận thêm giá trị NULL.
- Phía KHÔNG có `(+)` = Phía chủ đạo = Bảng được giữ lại toàn bộ (Master table).
- `A.id = B.id(+)` → Giữ A (A LEFT JOIN B).
- `A.id(+) = B.id` → Giữ B (A RIGHT JOIN B hoặc B LEFT JOIN A).

### 🚨 4 CẤM KỴ SỐNG CÒN CỦA TOÁN TỬ `(+)` TRONG ĐỀ THI SQLD

1. **CẤM đặt `(+)` ở cả hai vế (Không thể mô phỏng FULL OUTER JOIN):**
   ```sql
   -- ❌ LỖI ORA-01468: a predicate may reference only one outer-joined table
   SELECT *
   FROM employees e, departments d
   WHERE e.dept_id(+) = d.dept_id(+);
   ```
   Để thực hiện FULL OUTER JOIN trong cú pháp Oracle cũ, bắt buộc phải dùng phép hợp `UNION`: lấy `LEFT OUTER JOIN` rồi `UNION` với `RIGHT OUTER JOIN`.

2. **CẤM dùng `(+)` với toán tử `IN` hoặc `OR`:**
   ```sql
   -- ❌ LỖI ORA-01719: outer join operator (+) not allowed in operand of OR or IN
   WHERE e.dept_id = d.dept_id(+)
      OR e.salary > 5000;

   WHERE e.dept_id(+) IN (10, 20, 30);
   ```

3. **CẤM dùng `(+)` kết hợp với Subquery trong điều kiện nối:**
   ```sql
   -- ❌ LỖI CÚ PHÁP
   WHERE e.dept_id = (SELECT dept_id FROM departments WHERE ...)(+);
   ```

4. **Quy tắc bảo toàn Outer Join: Mọi điều kiện lọc bảng phụ đều PHẢI có `(+)`:**
   Nếu đã Outer Join với bảng `departments d`, thì bất kỳ điều kiện lọc nào áp lên bảng `d` trong mệnh đề `WHERE` cũng phải kèm `(+)`. Nếu quên `(+)`, câu lệnh sẽ bị suy thoái thành INNER JOIN!
   ```sql
   -- ❌ SUY THOÁI THÀNH INNER JOIN (Mất hết nhân viên chưa có phòng ban vì NULL = 'SEOUL' trả về UNKNOWN)
   SELECT e.name, d.dept_name
   FROM employees e, departments d
   WHERE e.dept_id = d.dept_id(+)
     AND d.loc = 'SEOUL';

   -- ✅ ĐÚNG CHUẨN OUTER JOIN (Vẫn giữ nhân viên không có phòng ban)
   SELECT e.name, d.dept_name
   FROM employees e, departments d
   WHERE e.dept_id = d.dept_id(+)
     AND d.loc(+) = 'SEOUL';
   ```

---

## 20. Một lỗi cực kỳ quan trọng: LEFT JOIN + WHERE

Giả sử:

```sql
SELECT e.name,
       d.dept_name
FROM employees e
LEFT JOIN departments d
    ON e.dept_id = d.dept_id;
```

Cường không có department:

```text
Cường | NULL
```

Nhưng nếu viết:

```sql
SELECT e.name,
       d.dept_name
FROM employees e
LEFT JOIN departments d
    ON e.dept_id = d.dept_id
WHERE d.dept_name = 'IT';
```

Dòng:

```text
Cường | NULL
```

đi vào WHERE:

```sql
NULL = 'IT'
```

không TRUE.

→ bị loại.

Vì vậy `WHERE` có thể khiến kết quả LEFT JOIN trông giống INNER JOIN.

Đây là một trong những bẫy JOIN quan trọng nhất.

---

## 21. `ON` và `WHERE` khác nhau thế nào trong OUTER JOIN?

So sánh:

#### Query A
Phần này nối mạch SQL với “Query A”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
SELECT *
FROM employees e
LEFT JOIN departments d
    ON e.dept_id = d.dept_id
   AND d.dept_name = 'IT';
```

với:

#### Query B
Phần này nối mạch SQL với “Query B”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
SELECT *
FROM employees e
LEFT JOIN departments d
    ON e.dept_id = d.dept_id
WHERE d.dept_name = 'IT';
```

Không giống nhau.

Query A:

```text
JOIN với department IT
nhưng vẫn bảo toàn employees
```

Query B:

```text
JOIN trước
↓
sau đó WHERE lọc kết quả
↓
employee không có IT bị loại
```

Đây là kiến thức nên đặc biệt nhớ khi thi SQLD.

---

## 22. Một khái niệm rất dễ nhầm: loại JOIN có nhiều cách phân loại

Bạn không nên xem danh sách:

```text
INNER
LEFT
RIGHT
FULL
SELF
EQUI
NON-EQUI
```

như 7 thứ hoàn toàn ngang hàng.

Thực ra chúng đang mô tả **các khía cạnh khác nhau**.

#### Phân loại theo "giữ dòng nào?"
Phần này nối mạch SQL với “Phân loại theo "giữ dòng nào?"”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
JOIN
│
├── INNER JOIN
│
└── OUTER JOIN
    ├── LEFT OUTER JOIN
    ├── RIGHT OUTER JOIN
    └── FULL OUTER JOIN
```

#### Phân loại theo "điều kiện JOIN?"
Phần này nối mạch SQL với “Phân loại theo "điều kiện JOIN?"”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
JOIN condition
│
├── EQUI JOIN
│      =
│
└── NON-EQUI JOIN
       < > <= >= BETWEEN ...
```

#### Phân loại theo "JOIN với bảng nào?"
Phần này nối mạch SQL với “Phân loại theo "JOIN với bảng nào?"”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
SELF JOIN
→ table JOIN chính nó
```

#### Không dùng điều kiện match
Phần này nối mạch SQL với “Không dùng điều kiện match”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
CROSS JOIN
→ Cartesian Product
```

Vì vậy một JOIN hoàn toàn có thể đồng thời là:

```text
SELF JOIN
+
LEFT OUTER JOIN
+
EQUI JOIN
```

Ví dụ:

```sql
SELECT e.name,
       m.name
FROM employees e
LEFT JOIN employees m
    ON e.manager_id = m.employee_id;
```

Nó là:

```text
SELF JOIN
    vì employees JOIN employees

LEFT OUTER JOIN
    vì giữ toàn bộ e

EQUI JOIN
    vì điều kiện sử dụng =
```

Đây là cách hiểu chính xác hơn thay vì học thuộc từng JOIN riêng biệt.

---

## 23. Sơ đồ tổng hợp để nhớ khi thi SQLD

Hãy nhớ thế này:

```text
                         JOIN
                          │
             ┌────────────┴────────────┐
             │                         │
          MATCH?                    NO MATCH
             │
      ┌──────┴──────┐
      │             │
    INNER         OUTER
                  │
          ┌───────┼───────┐
          │       │       │
        LEFT    RIGHT    FULL
```

Ý nghĩa:

```text
INNER
→ chỉ lấy MATCH

LEFT
→ MATCH + LEFT không match

RIGHT
→ MATCH + RIGHT không match

FULL
→ MATCH + cả hai bên không match
```

Ngoài nhóm đó:

```text
CROSS
→ mọi A × mọi B

SELF
→ bảng JOIN chính nó

EQUI
→ điều kiện =

NON-EQUI
→ điều kiện khác =

NATURAL
→ tự JOIN column cùng tên
```

---

## 24. Cách chọn JOIN khi gặp bài thực tế

Đừng hỏi:

> "Câu này dùng JOIN nào?"

Hãy hỏi:

> **"Dòng nào tuyệt đối không được phép mất?"**

Ví dụ:

#### "Chỉ lấy employee có department"
Phần này nối mạch SQL với “"Chỉ lấy employee có department"”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
Không cần giữ employee không có department
Không cần giữ department không có employee

→ INNER JOIN
```

#### "Lấy TẤT CẢ employee và thông tin department nếu có"

Keyword:

```text
TẤT CẢ EMPLOYEE
```

→ employee phải được bảo toàn.

```sql
FROM employees e
LEFT JOIN departments d
```

#### "Lấy TẤT CẢ department, kể cả department chưa có nhân viên"

Department phải được bảo toàn:

```sql
FROM employees e
RIGHT JOIN departments d
```

hoặc dễ đọc hơn:

```sql
FROM departments d
LEFT JOIN employees e
```

#### "Lấy tất cả employee và tất cả department, kể cả hai bên không match"
Phần này nối mạch SQL với “"Lấy tất cả employee và tất cả department, kể cả hai bên không match"”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
FULL OUTER JOIN
```

#### "Tạo tất cả tổ hợp employee × department"
Phần này nối mạch SQL với “"Tạo tất cả tổ hợp employee × department"”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
CROSS JOIN
```

#### "Tìm manager của employee trong cùng bảng"
Phần này nối mạch SQL với “"Tìm manager của employee trong cùng bảng"”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
SELF JOIN
```

---

## 25. Bảng tổng kết cuối bài
Phần này nối mạch SQL với “25. Bảng tổng kết cuối bài”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

| Loại                | Ý nghĩa dễ nhớ                       | Không match           |
| ------------------- | ------------------------------------ | --------------------- |
| **INNER JOIN**      | Chỉ lấy cặp match                    | bỏ                    |
| **LEFT JOIN**       | Giữ toàn bộ LEFT                     | RIGHT → NULL          |
| **RIGHT JOIN**      | Giữ toàn bộ RIGHT                    | LEFT → NULL           |
| **FULL OUTER JOIN** | Giữ cả hai bên                       | bên thiếu → NULL      |
| **CROSS JOIN**      | Mọi tổ hợp A × B                     | không cần match       |
| **SELF JOIN**       | Table JOIN chính nó                  | phụ thuộc INNER/OUTER |
| **EQUI JOIN**       | JOIN bằng `=`                        | phụ thuộc loại JOIN   |
| **NON-EQUI JOIN**   | JOIN bằng `< > BETWEEN...`           | phụ thuộc loại JOIN   |
| **NATURAL JOIN**    | tự JOIN cột cùng tên                 | SQL tự xác định       |
| **USING**           | JOIN bằng cột cùng tên được chỉ định | explicit hơn NATURAL  |

### 🧠 NOTE NHỚ NHANH SQLD

Chỉ cần thuộc cụm này:

```text
INNER = MATCH

LEFT  = MATCH + LEFT
RIGHT = MATCH + RIGHT
FULL  = MATCH + LEFT + RIGHT

CROSS = A × B
SELF  = JOIN chính mình

EQUI     = "="
NON-EQUI = không phải "="

NATURAL = tự tìm cột cùng tên
USING   = chỉ định cột cùng tên
ON      = chỉ định điều kiện
```

Và với Oracle `(+)`:

```text
A.id = B.id(+)
         ↑
       B được phép thiếu

=> giữ A
=> A LEFT JOIN B
```

Điểm quan trọng nhất để giải đề là **đừng học hình Venn một cách máy móc**. Khi gặp JOIN, xác định theo thứ tự:

```text
1. Bảng nào đang JOIN với bảng nào?
2. Điều kiện match là gì?
3. Dòng nào match?
4. Bên nào bắt buộc phải được giữ?
5. Bên không match → bỏ hay điền NULL?
```

Nếu trả lời được 5 câu này thì INNER/OUTER JOIN gần như không còn khó nữa.

---

## 26. Semi-Join (세미 조인) vs Anti-Join (안티 조인)

Trong tối ưu hóa truy vấn và đề thi SQLD, hai dạng join logic này xuất hiện rất nhiều dưới hình thức toán tử `EXISTS` và `IN`.

### 26.1 Semi-Join (세미 조인)

**KR:** 세미 조인은 서브쿼리에 존재하는지만 확인하고, 메인 쿼리의 행을 중복 없이 한 번만 반환하는 조인이다.
**VI:** Semi-Join kiểm tra sự **tồn tại** của dữ liệu ở bảng phụ; nếu có ít nhất 1 dòng tương ứng thì dòng của bảng chính được giữ lại và **không bao giờ bị nhân đôi số dòng**.

Khác biệt cốt tử với INNER JOIN:
- Nếu bảng `DEPARTMENTS` có 1 phòng ban nối với `EMPLOYEES` có 10 nhân viên (quan hệ 1 - N):
  - Khi dùng `INNER JOIN`: Bảng phòng ban sẽ bị lặp lại thành 10 dòng kết quả.
  - Khi dùng `Semi-Join` (`EXISTS` / `IN`): Mỗi phòng ban chỉ xuất hiện **đúng 1 lần** trong kết quả, dù nó có bao nhiêu nhân viên đi chăng nữa.

```sql
-- Semi-Join bằng EXISTS: Tìm các phòng ban có ít nhất 1 nhân viên
SELECT d.dept_id, d.dept_name
FROM departments d
WHERE EXISTS (
    SELECT 1
    FROM employees e
    WHERE e.dept_id = d.dept_id
);
```

### 26.2 Anti-Join (안티 조인)

**KR:** 안티 조인은 서브쿼리의 조건에 만족하지 않는 행만 메인 쿼리에서 추출하는 조인이다.
**VI:** Anti-Join lấy các dòng từ bảng chính mà **không có bất kỳ bản ghi khớp nào** trong bảng phụ.

```sql
-- Anti-Join bằng NOT EXISTS: Tìm các phòng ban chưa có nhân viên nào
SELECT d.dept_id, d.dept_name
FROM departments d
WHERE NOT EXISTS (
    SELECT 1
    FROM employees e
    WHERE e.dept_id = d.dept_id
);
```

---

## 27. Bảng ma trận so sánh ANSI JOIN vs Oracle Old-Style vs SQL Server

| Tính năng / Loại JOIN | Chuẩn ANSI SQL (SQL:1999) | Oracle Truyền thống (Old-Style) | Microsoft SQL Server |
| :--- | :--- | :--- | :--- |
| **INNER JOIN** | `A INNER JOIN B ON A.id = B.id` | `FROM A, B WHERE A.id = B.id` | Hỗ trợ chuẩn ANSI và kiểu cũ |
| **LEFT OUTER JOIN** | `A LEFT JOIN B ON A.id = B.id` | `WHERE A.id = B.id(+)` | `A LEFT JOIN B ON A.id = B.id` (Không hỗ trợ `(+)`) |
| **RIGHT OUTER JOIN** | `A RIGHT JOIN B ON A.id = B.id` | `WHERE A.id(+) = B.id` | `A RIGHT JOIN B ON A.id = B.id` |
| **FULL OUTER JOIN** | `A FULL OUTER JOIN B ON A.id = B.id` | **KHÔNG HỖ TRỢ** bằng `(+)` (Phải dùng UNION giữa LEFT và RIGHT) | `A FULL OUTER JOIN B ON A.id = B.id` |
| **CROSS JOIN** | `A CROSS JOIN B` | `FROM A, B` (Không có điều kiện WHERE) | Hỗ trợ cả hai cú pháp |
| **NATURAL JOIN** | `A NATURAL JOIN B` | Hỗ trợ chuẩn ANSI | **KHÔNG HỖ TRỢ** từ khóa `NATURAL JOIN` |
| **Mệnh đề USING** | `JOIN B USING (col_name)` | Hỗ trợ chuẩn ANSI | **KHÔNG HỖ TRỢ** mệnh đề `USING` |
| **Điều kiện Non-EQUI** | `ON (A.val BETWEEN B.low AND B.high)` | `WHERE A.val BETWEEN B.low AND B.high` | Hỗ trợ tương đương ANSI |

---

## 28. Cạm bẫy thi cử trọng điểm (출제 함정 & 오답 노트)

1. **Bẫy tiền tố bảng (Table Qualifier) trong NATURAL JOIN:**
   - Cấm dùng: `SELECT e.dept_id FROM emp e NATURAL JOIN dept d` → Lỗi `ORA-25155`.
   - Phải viết: `SELECT dept_id ...`.
2. **Bẫy tiền tố bảng trong mệnh đề USING:**
   - Cấm dùng: `SELECT e.dept_id FROM emp e JOIN dept d USING (dept_id)` → Lỗi `ORA-25154`.
   - Mệnh đề `USING` bắt buộc phải có dấu ngoặc: `USING (dept_id)`.
3. **Bẫy 4 Cấm của ký hiệu `(+)` trong Oracle:**
   - Cấm đặt `(+)` ở cả 2 vế của phép so sánh (Không tạo được FULL OUTER JOIN).
   - Cấm dùng `(+)` kết hợp với toán tử `OR` hoặc `IN` (`ORA-01719`).
   - Mọi điều kiện lọc cột của bảng outer-joined trong `WHERE` đều bắt buộc phải có `(+)`, nếu không Outer Join sẽ suy thoái thành Inner Join.
4. **Bẫy số dòng của CROSS JOIN (Cartesian Product):**
   - Bảng A có N dòng, bảng B có M dòng. Kết quả CROSS JOIN luôn có đúng `N × M` dòng.
   - Quên điều kiện JOIN trong cú pháp Oracle cũ (`FROM A, B;`) sẽ vô tình tạo ra CROSS JOIN.
5. **Bẫy vị trí điều kiện lọc: ON vs WHERE trong LEFT OUTER JOIN:**
   - Điều kiện đặt trong `ON`: Lọc các dòng của bảng phụ trước khi ghép; dòng bảng chính không match vẫn được giữ lại (bảng phụ điền NULL).
   - Điều kiện đặt trong `WHERE`: Lọc trên tập kết quả sau khi ghép; các dòng bảng chính có giá trị NULL ở bảng phụ sẽ bị loại bỏ hoàn toàn, biến câu lệnh thành INNER JOIN.

---

## 29. Câu hỏi trắc nghiệm thi thử mô phỏng (실전 기출 변형 문제 & 정답 해설)

### Câu 1 (Độ khó: Trung bình — Bẫy cú pháp NATURAL JOIN)
Cho hai bảng `EMP` (chứa các cột: `EMPNO`, `ENAME`, `DEPTNO`) và `DEPT` (chứa các cột: `DEPTNO`, `DNAME`). Câu lệnh SQL nào dưới đây sẽ gây lỗi biên dịch khi thực thi trên Oracle Database?

A.
```sql
SELECT EMPNO, ENAME, DEPTNO, DNAME
FROM EMP NATURAL JOIN DEPT;
```
B.
```sql
SELECT E.EMPNO, E.ENAME, DEPTNO, D.DNAME
FROM EMP E NATURAL JOIN DEPT D;
```
C.
```sql
SELECT E.EMPNO, E.ENAME, E.DEPTNO, D.DNAME
FROM EMP E NATURAL JOIN DEPT D;
```
D.
```sql
SELECT E.EMPNO, E.ENAME, D.DNAME
FROM EMP E JOIN DEPT D USING (DEPTNO);
```

**Đáp án đúng:** **C**
**Giải thích chi tiết:**
- **Đáp án C là câu lệnh gây lỗi:** Trong `NATURAL JOIN`, cột dùng làm điều kiện kết nối (`DEPTNO`) trở thành thuộc tính chung, cấm tuyệt đối không được có tiền tố tên bảng hoặc alias (`E.DEPTNO` hay `D.DEPTNO`). Khi thực thi sẽ phát sinh lỗi `ORA-25155: column used in NATURAL JOIN cannot have qualifier`.
- **Đáp án A hợp lệ:** Không dùng alias cho bất kỳ cột nào, `DEPTNO` đứng độc lập.
- **Đáp án B hợp lệ:** Các cột riêng biệt của từng bảng (`EMPNO`, `ENAME`, `DNAME`) được phép có alias, riêng cột chung `DEPTNO` không có alias.
- **Đáp án D hợp lệ:** Cú pháp `USING (DEPTNO)` chuẩn xác, cột trong `SELECT` không có qualifier trên `DEPTNO`.

---

### Câu 2 (Độ khó: Khá — Cạm bẫy Oracle `(+)` và suy thoái Outer Join)
Cho bảng `TB_CUSTOMER` (10 khách hàng) và `TB_ORDER` (5 đơn hàng, trong đó chỉ có 4 khách hàng có đơn hàng). Xét câu lệnh SQL sau trên Oracle:

```sql
SELECT C.CUST_ID, C.CUST_NAME, O.ORDER_ID, O.AMOUNT
FROM TB_CUSTOMER C, TB_ORDER O
WHERE C.CUST_ID = O.CUST_ID(+)
  AND O.AMOUNT > 100000;
```

Kết quả của câu truy vấn trên sẽ như thế nào?

A. Trả về toàn bộ 10 khách hàng; các khách hàng không có đơn hàng hoặc có đơn hàng `<= 100000` sẽ hiển thị `ORDER_ID` và `AMOUNT` là NULL.
B. Chỉ trả về các khách hàng có đơn hàng với số tiền `AMOUNT > 100000` (các khách hàng chưa từng mua hàng bị loại bỏ hoàn toàn).
C. Trả về lỗi thực thi vì không thể dùng điều kiện so sánh `>` trên bảng có dấu `(+)`.
D. Trả về đúng 10 dòng dữ liệu nhưng cột `AMOUNT` được tính theo hàm gộp.

**Đáp án đúng:** **B**
**Giải thích chi tiết:**
- Mặc dù điều kiện join `C.CUST_ID = O.CUST_ID(+)` là LEFT OUTER JOIN (giữ toàn bộ khách hàng), nhưng điều kiện lọc `AND O.AMOUNT > 100000` lại **thiếu dấu `(+)`** (`O.AMOUNT(+) > 100000`).
- Đối với những khách hàng không có đơn hàng, giá trị `O.AMOUNT` sinh ra từ Outer Join là `NULL`.
- Khi đưa vào mệnh đề `WHERE`, biểu thức `NULL > 100000` trả về giá trị logic `UNKNOWN` (coi như FALSE), khiến tất cả các dòng khách hàng này bị loại bỏ khỏi kết quả cuối cùng.
- Hiện tượng này gọi là **suy thoái Outer Join thành Inner Join (Outer Join Degeneration)**. Do đó chỉ có khách hàng thỏa mãn `AMOUNT > 100000` mới được hiển thị.

---

### Câu 3 (Độ khó: Khá — Phân biệt Semi-Join vs Inner Join)
Phát biểu nào sau đây là **ĐÚNG NHẤT** khi so sánh giữa `INNER JOIN` và `SEMI-JOIN` (sử dụng toán tử `EXISTS`)?

A. `SEMI-JOIN` luôn trả về nhiều dòng hơn hoặc bằng số dòng của `INNER JOIN` đối với cùng một tập dữ liệu.
B. Nếu bảng bên phải có quan hệ 1 - Nhiều (1:N) với bảng bên trái, `INNER JOIN` sẽ làm nhân bản các dòng của bảng bên trái, trong khi `SEMI-JOIN` chỉ trả về mỗi dòng của bảng bên trái tối đa một lần.
C. `SEMI-JOIN` cho phép truy xuất tất cả các cột của bảng phụ trong mệnh đề `SELECT` của câu truy vấn chính.
D. Trong SQL chuẩn ANSI, toán tử `CROSS JOIN` chính là một dạng đặc biệt của `SEMI-JOIN`.

**Đáp án đúng:** **B**
**Giải thích chi tiết:**
- **Đáp án B chính xác tuyệt đối:** Khi bảng phụ (bên phải) có nhiều bản ghi thỏa mãn điều kiện join với 1 bản ghi của bảng chính (bên trái), `INNER JOIN` sẽ ghép cặp tạo thành nhiều dòng kết quả (nhân đôi/nhân ba số dòng). Ngược lại, `SEMI-JOIN` chỉ quan tâm đến việc "có tồn tại ít nhất 1 dòng hay không", ngay khi tìm thấy nó sẽ dừng quét cho bản ghi đó, bảo đảm mỗi dòng bảng chính chỉ xuất hiện duy nhất 1 lần.
- **Đáp án A sai:** Semi-join trả về số dòng ít hơn hoặc bằng Inner Join.
- **Đáp án C sai:** Mệnh đề `SELECT` chính không thể nhìn thấy hoặc truy xuất các cột từ bảng nằm bên trong subquery `EXISTS`.
- **Đáp án D sai:** `CROSS JOIN` là tích Đề-các (Cartesian product), hoàn toàn không liên quan đến cơ chế Semi-join.

---

### Câu 4 (Độ khó: Nâng cao — Các quy tắc hạn chế của toán tử `(+)`)
Trong hệ quản trị cơ sở dữ liệu Oracle, câu lệnh SQL nào dưới đây là **HỢP LỆ** và thực thi thành công không bị báo lỗi?

A.
```sql
SELECT A.ID, B.VAL
FROM TAB_A A, TAB_B B
WHERE A.ID(+) = B.ID(+);
```
B.
```sql
SELECT A.ID, B.VAL
FROM TAB_A A, TAB_B B
WHERE A.ID = B.ID(+)
   OR A.STATUS = 'ACTIVE';
```
C.
```sql
SELECT A.ID, B.VAL
FROM TAB_A A, TAB_B B
WHERE A.ID = B.ID(+)
  AND B.CODE(+) = 'KR';
```
D.
```sql
SELECT A.ID, B.VAL
FROM TAB_A A, TAB_B B
WHERE A.ID = B.ID(+)
  AND B.CODE(+) IN ('KR', 'US', 'JP');
```

**Đáp án đúng:** **C**
**Giải thích chi tiết:**
- **Đáp án C HỢP LỆ:** Cú pháp LEFT OUTER JOIN chuẩn của Oracle cũ, điều kiện lọc bổ sung trên bảng phụ có kèm dấu `(+)` chính xác (`B.CODE(+) = 'KR'`).
- **Đáp án A SAI:** Lỗi `ORA-01468: a predicate may reference only one outer-joined table` vì cấm đặt dấu `(+)` ở cả hai vế (không thể mô phỏng FULL OUTER JOIN theo cách này).
- **Đáp án B SAI:** Lỗi `ORA-01719: outer join operator (+) not allowed in operand of OR or IN` vì Oracle cấm kết hợp điều kiện có dấu `(+)` với toán tử `OR`.
- **Đáp án D SAI:** Lỗi `ORA-01719: outer join operator (+) not allowed in operand of OR or IN` vì Oracle cấm dùng dấu `(+)` đi kèm với toán tử `IN`. Muốn lọc nhiều giá trị trên bảng outer-joined, phải dùng cú pháp ANSI JOIN (`ON A.ID = B.ID AND B.CODE IN ('KR', 'US', 'JP')`).
