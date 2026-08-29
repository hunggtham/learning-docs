# JOIN

> **Mục tiêu:** INNER/OUTER/CROSS/SELF JOIN, NATURAL/USING, ANSI join và các bẫy điều kiện.

## Từ khóa cần nhớ (Keyword)

Các thuật ngữ SQLD được giữ nguyên tiếng Hàn/English trong phần nguồn. Khi ghi chú, dùng mẫu `용어 (English) (Tiếng Việt)` để nối tên gọi trong đề với ý nghĩa thực tế.

## Mạch tư duy (Logic học)

Hãy xác định **đối tượng dữ liệu** trước, sau đó đọc **điều kiện**, **phạm vi dòng**, **thứ tự xử lý** và cuối cùng kiểm tra **kết quả mong đợi**. Với SQL, luôn phân biệt điều kiện lọc trước nhóm (`WHERE`) với điều kiện lọc sau nhóm (`HAVING`).

> **Cách học:** Đọc phần khái niệm → tự chạy lại các ví dụ SQL → chốt lại các mục `Keyword`, bảng so sánh và phần ghi nhớ cuối bài.

---

Để JOIN **thực sự dễ nhớ**, đừng bắt đầu bằng cú pháp. Hãy nhớ một ý duy nhất:

> **JOIN = ghép các dòng của nhiều bảng dựa trên một điều kiện liên quan.**

Trong SQLD/Oracle, phần dễ nhầm nhất là: **INNER JOIN, LEFT/RIGHT/FULL OUTER JOIN, CROSS JOIN, SELF JOIN, NATURAL JOIN**, và **EQUI/NON-EQUI JOIN**. Mình sẽ đi từ bản chất → ví dụ → kết quả → cách phân biệt.

---

## 1. Tại sao cần JOIN?

Giả sử database có 2 bảng.

#### EMPLOYEES

| EMP_ID | NAME  | DEPT_ID |
| -----: | ----- | ------: |
|      1 | An    |      10 |
|      2 | Bình  |      20 |
|      3 | Cường |      30 |
|      4 | Dũng  |    NULL |

#### DEPARTMENTS

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

```text
EQUI JOIN
    ↓
=

NON-EQUI JOIN
    ↓
>, <, >=, <=, BETWEEN...
```

---

## 15. NATURAL JOIN

NATURAL JOIN là loại rất dễ xuất hiện trong lý thuyết SQLD.

Ví dụ:

```text
EMPLOYEES
----------------
EMP_ID
NAME
DEPT_ID

DEPARTMENTS
----------------
DEPT_ID
DEPT_NAME
```

Hai bảng có column cùng tên:

```text
DEPT_ID
```

Nếu viết:

```sql
SELECT *
FROM employees
NATURAL JOIN departments;
```

SQL tự tìm các column có:

```text
cùng tên
```

và dùng chúng để JOIN.

Trong trường hợp này tương đương gần như:

```sql
SELECT *
FROM employees e
JOIN departments d
    ON e.dept_id = d.dept_id;
```

---

## 16. Tại sao NATURAL JOIN nguy hiểm?

Giả sử ban đầu:

```text
EMPLOYEES
EMP_ID
NAME
DEPT_ID

DEPARTMENTS
DEPT_ID
DEPT_NAME
```

NATURAL JOIN dựa trên:

```text
DEPT_ID
```

Sau này developer thêm column:

```text
EMPLOYEES
----------------
EMP_ID
NAME
DEPT_ID
LOCATION_ID

DEPARTMENTS
----------------
DEPT_ID
DEPT_NAME
LOCATION_ID
```

Bây giờ NATURAL JOIN có thể tự JOIN dựa trên **cả các cột cùng tên thích hợp**, khiến ý nghĩa query thay đổi ngoài dự kiến.

Vì thế trong code production, thường nên viết điều kiện JOIN rõ ràng hơn.

---

## 17. USING — khi hai bảng JOIN bằng column cùng tên

Nếu:

```text
employees.department_id

departments.department_id
```

cùng tên `department_id`, có thể viết:

```sql
SELECT *
FROM employees
JOIN departments
USING (department_id);
```

thay vì:

```sql
SELECT *
FROM employees e
JOIN departments d
ON e.department_id = d.department_id;
```

Khác biệt về tư duy:

```text
NATURAL JOIN
→ SQL tự quyết định column cùng tên

USING(department_id)
→ Tôi chỉ rõ column muốn dùng

ON e.department_id = d.department_id
→ Tôi viết điều kiện cụ thể
```

Mức độ kiểm soát:

```text
NATURAL JOIN
     ↓ ít explicit

USING
     ↓

ON
     ↓ rõ ràng nhất
```

---

## 18. ANSI JOIN và Oracle Old-Style JOIN

Đây là phần rất quan trọng khi học Oracle/SQLD.

### ANSI JOIN

Ví dụ:

```sql
SELECT e.employee_name,
       d.department_name
FROM employees e
JOIN departments d
    ON e.department_id = d.department_id;
```

Đây là cú pháp ANSI/ISO SQL.

---

### Oracle old-style

Oracle truyền thống có thể viết:

```sql
SELECT e.employee_name,
       d.department_name
FROM employees e,
     departments d
WHERE e.department_id = d.department_id;
```

Hai câu trên về logic là INNER JOIN tương đương.

```text
ANSI

FROM A
JOIN B
ON A.id = B.id
```

vs.

```text
Oracle old style

FROM A, B
WHERE A.id = B.id
```

---

## 19. Oracle `(+)` Outer Join

Trong cú pháp Oracle cũ, outer join dùng:

```sql
(+)
```

Ví dụ ANSI:

```sql
SELECT *
FROM employees e
LEFT JOIN departments d
    ON e.department_id = d.department_id;
```

Oracle old syntax:

```sql
SELECT *
FROM employees e,
     departments d
WHERE e.department_id = d.department_id(+);
```

Chỗ `(+)` rất dễ gây nhầm.

Hãy hiểu:

```sql
e.department_id = d.department_id(+)
```

`departments` là phía có thể **thiếu dữ liệu**.

Tức là:

```text
employees phải giữ
departments có thể không có
```

→ LEFT JOIN.

#### Mẹo nhớ `(+)`

Đừng nghĩ:

> `(+)` = bên được giữ.

Mà nghĩ:

> **`(+)` = bên được phép thiếu / cần NULL bổ sung.**

Ví dụ:

```sql
A.id = B.id(+)
```

→ B được phép không tồn tại

→ giữ A

→

```sql
A LEFT JOIN B
```

Ngược lại:

```sql
A.id(+) = B.id
```

→ A được phép thiếu

→ giữ B

→

```sql
A RIGHT JOIN B
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

```sql
SELECT *
FROM employees e
LEFT JOIN departments d
    ON e.dept_id = d.dept_id
   AND d.dept_name = 'IT';
```

với:

#### Query B

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

```text
SELF JOIN
→ table JOIN chính nó
```

#### Không dùng điều kiện match

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

```sql
FULL OUTER JOIN
```

#### "Tạo tất cả tổ hợp employee × department"

```sql
CROSS JOIN
```

#### "Tìm manager của employee trong cùng bảng"

```sql
SELF JOIN
```

---

## 25. Bảng tổng kết cuối bài

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
