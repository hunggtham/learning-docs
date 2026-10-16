<!-- lecture-contract: v2 -->
# SQL Style Guide và SQL dễ đọc cho pipeline AI

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **SQL Style Guide**. Route đi từ naming conventions → query formatting & "river" → Enterprise alias standards → WHERE clause indentation & logic grouping → Index-friendly SARGable queries vs Anti-patterns → AI pipeline guidelines.

> **Mục tiêu:** Nắm vững các quy chuẩn viết SQL chuyên nghiệp trong môi trường doanh nghiệp lớn (Enterprise) và pipeline tích hợp AI: quy tắc đặt alias có nghĩa, thụt lề mệnh đề `WHERE`, tránh các Anti-patterns làm vô hiệu hóa Index (`WHERE YEAR(order_date) = 2026`), và bảo đảm tính mở rộng, ổn định hiệu năng của hệ thống.

---

### SQL Style Guide là gì?

Một câu SQL có thể chạy đúng kết quả nhưng vẫn có thể khó đọc, khó review và gây suy giảm hiệu năng nghiêm trọng trong môi trường production. Trong pipeline dữ liệu doanh nghiệp và hệ thống lớn, query thường trở thành một model được chạy lại hàng triệu lần, được kết nối với nhiều hệ thống hạ tầng và được nhiều kỹ sư tiếp quản sau nhiều năm. Vì vậy, style không chỉ là chuyện trình bày thẩm mỹ: nó là một phần cốt lõi của khả năng kiểm thử, bảo trì và hiệu năng thực thi của cơ sở dữ liệu.

Tài liệu này kế thừa các nguyên lý từ SQL Style Guide của Simon Holywell và *SQL Programming Style* của Joe Celko, đồng thời mở rộng các quy chuẩn đặc thù cho môi trường Enterprise và các pipeline dữ liệu được AI hỗ trợ.

---

### 1. Quy chuẩn đặt tên đối tượng (Naming Conventions)

Tên tốt giúp người đọc và công cụ phân tích tự động đoán đúng vai trò của đối tượng mà không cần phải tra cứu schema:
- **Nguyên tắc chung:** Sử dụng tên mô tả, duy nhất, bắt đầu bằng chữ cái, chỉ dùng chữ cái, chữ số và gạch dưới (`_`). Sử dụng kiểu `snake_case`, tránh tiền tố kiểu Hungarian như `tbl_` hoặc `sp_`.
- **Bảng (Tables):** Ưu tiên danh từ tập hợp tự nhiên (`staff`, `inventory`) hoặc danh từ số nhiều (`employees`, `orders`).
- **Cột (Columns):** Dùng danh từ số ít. Tránh đặt tên cột trần trụi là `id` hoặc `name`; nên dùng `customer_id`, `employee_name` để tránh xung đột khi `JOIN`.
- **Hậu tố ngữ nghĩa thống nhất:**

| Hậu tố | Ý nghĩa quy ước | Ví dụ minh họa |
| --- | --- | --- |
| `_id` | Định danh duy nhất hoặc khóa tham chiếu | `customer_id`, `order_id` |
| `_status` | Cờ hoặc mã trạng thái quy trình | `payment_status`, `order_status` |
| `_total` | Tổng số tiền hoặc giá trị tổng | `line_total`, `order_total` |
| `_cnt` / `_num` | Số lượng đếm được hoặc giá trị số | `item_cnt`, `retry_num` |
| `_date` | Ngày diễn ra sự kiện (kiểu `DATE`) | `order_date`, `birth_date` |
| `_at` | Dấu thời gian chính xác (kiểu `TIMESTAMP`) | `created_at`, `updated_at` |

---

### 2. Quy chuẩn đặt Alias chuyên nghiệp trong môi trường Enterprise

Alias là điểm nối giữa bảng vật lý và tư duy nghiệp vụ của truy vấn. Đặt alias tùy tiện là nguyên nhân hàng đầu gây nhầm lẫn khi debug các câu truy vấn phức tạp:

#### 1. Table Alias (Bí danh bảng)
- **Cấm tuyệt đối alias 1 ký tự mơ hồ:** Tránh đặt `a`, `b`, `c`, `t1`, `t2` trong các query thực tế. Khi câu truy vấn có 5 bảng JOIN với nhau, người đọc không thể nhớ `b.status` thuộc về bảng nào.
- **Dùng viết tắt ngắn gọn nhưng nhận diện được ngay:**
  - `orders` $\rightarrow$ `ord`
  - `order_items` $\rightarrow$ `oi`
  - `customers` $\rightarrow$ `cust`
  - `employees` $\rightarrow$ `emp`
  - `departments` $\rightarrow$ `dept`
- **Tự liên kết (Self-Join) và đa vai trò:** Khi cùng một bảng xuất hiện nhiều lần với các vai trò nghiệp vụ khác nhau, alias bắt buộc phải phản ánh chính xác vai trò đó:
  ```sql
  -- Tốt: Phân biệt rõ ai là nhân viên và ai là quản lý
  SELECT emp.employee_id,
         emp.full_name AS employee_name,
         mgr.full_name AS manager_name
  FROM employees emp
  LEFT JOIN employees mgr
    ON emp.manager_id = mgr.employee_id;
  ```
- **Lưu ý về từ khóa `AS` giữa các dialect:** ANSI SQL cho phép `FROM table AS alias`, nhưng Oracle Database truyền thống **không chấp nhận từ khóa `AS` cho table alias** (`FROM orders AS o` sẽ báo lỗi cú pháp; phải viết `FROM orders o`).

#### 2. Column Alias (Bí danh cột)
- Cột tính toán từ hàm hoặc biểu thức bắt buộc phải có alias định danh rõ nghĩa theo `snake_case`:
  - ❌ `SELECT SUM(sal), AVG(comm) FROM emp;`
  - ✅ `SELECT SUM(sal) AS total_sal, ROUND(AVG(comm), 2) AS avg_commission FROM emp;`

---

### 3. Quy chuẩn thụt lề và nhóm điều kiện mệnh đề WHERE

Mệnh đề `WHERE` là trái tim logic của câu truy vấn. Việc trình bày rõ ràng giúp loại trừ các lỗi logic tai hại liên quan đến độ ưu tiên toán tử:

#### 1. Căn lề thẳng hàng (Vertical Alignment)
Căn lề từ khóa chính và đưa các toán tử `AND` / `OR` xuống đầu dòng để tạo thành một "dòng sông" quét mắt tự nhiên:

```sql
SELECT ord.order_id,
       ord.customer_id,
       SUM(oi.line_total) AS order_total
FROM orders ord
JOIN order_items oi
  ON ord.order_id = oi.order_id
WHERE ord.order_date >= DATE '2026-01-01'
  AND ord.order_date <  DATE '2027-01-01'
  AND ord.order_status = 'COMPLETED'
GROUP BY ord.order_id,
         ord.customer_id;
```

#### 2. Quy tắc bắt buộc dùng ngoặc đơn khi kết hợp AND và OR
Trong SQL, toán tử `AND` luôn có **độ ưu tiên cao hơn** toán tử `OR` (`AND` binds tighter than `OR`):

$$\text{condA} \lor \text{condB} \land \text{condC} \iff \text{condA} \lor (\text{condB} \land \text{condC})$$

Nếu không dùng ngoặc đơn, câu truy vấn sẽ trả về kết quả sai lệch hoàn toàn so với nghiệp vụ:

```sql
-- SAI NGHIỆP VỤ: Do AND ưu tiên hơn, hệ thống chỉ lọc dept_id = 10 cho nhánh ADMIN!
-- Nhân viên có status = 'ACTIVE' ở các phòng ban khác vẫn bị lọt vào kết quả!
WHERE status = 'ACTIVE' OR role = 'ADMIN' AND dept_id = 10;

-- ĐÚNG CHUẨN ENTERPRISE: Luôn đóng ngoặc đơn tường minh cho từng khối điều kiện
WHERE (status = 'ACTIVE' OR role = 'ADMIN')
  AND dept_id = 10;
```

---

### 4. Tối ưu hóa Index: Tránh các Anti-patterns làm vô hiệu hóa Index (SARGability)

Một vị từ tìm kiếm được gọi là **SARGable** (Search Argumentable) khi nó cho phép Optimizer tận dụng cấu trúc cây B-Tree Index để thực hiện `INDEX RANGE SCAN` thay vì phải quét toàn bộ bảng (`FULL TABLE SCAN`).

Dưới đây là 4 Anti-patterns kinh điển làm tê liệt Index trong môi trường production:

#### Anti-pattern 1: Dùng hàm trên cột Index (Function on Indexed Column)
- **Sai:**
  ```sql
  -- Vô hiệu hóa Index trên cột order_date hoặc hiredate!
  WHERE YEAR(order_date) = 2026;
  WHERE TO_CHAR(hiredate, 'YYYY') = '2026';
  ```
- **Bản chất kỹ thuật:** Index lưu trữ giá trị ngày tháng nguyên thủy. Khi bọc hàm `YEAR()` hoặc `TO_CHAR()`, DBMS không thể định vị điểm bắt đầu và kết thúc trên cây B-Tree, buộc phải tính hàm trên từng dòng của hàng triệu bản ghi qua Full Table Scan.
- **Viết lại chuẩn SARGable:**
  ```sql
  -- Tận dụng Index Range Scan cực nhanh
  WHERE order_date >= DATE '2026-01-01'
    AND order_date <  DATE '2027-01-01';
  ```

#### Anti-pattern 2: Phép tính số học trên cột Index (Arithmetic on Indexed Column)
- **Sai:**
  ```sql
  -- Phép nhân trên cột làm vô hiệu hóa B-Tree Index
  WHERE sal * 12 > 60000;
  WHERE balance + 1000 < 5000;
  ```
- **Viết lại chuẩn SARGable:** Di chuyển toàn bộ phép tính toán học sang vế hằng số:
  ```sql
  WHERE sal > 60000 / 12;
  WHERE balance < 5000 - 1000;
  ```

#### Anti-pattern 3: Ép kiểu dữ liệu ngầm định (Implicit Type Conversion)
- **Sai:**
  ```sql
  -- Cột phone_number có kiểu VARCHAR2, nhưng so sánh với hằng số NUMBER!
  WHERE phone_number = 01012345678;
  ```
- **Bản chất kỹ thuật:** Theo quy tắc chuyển đổi kiểu của Oracle, khi so sánh giữa chuỗi và số, hệ thống sẽ ngầm ép kiểu chuỗi thành số: `WHERE TO_NUMBER(phone_number) = 01012345678`. Việc ngầm bọc hàm `TO_NUMBER()` này biến cột Index thành Non-SARGable và gây lỗi nếu cột chứa ký tự không phải số.
- **Viết lại chuẩn SARGable:** Luôn giữ đúng kiểu dữ liệu với dấu nháy đơn cho chuỗi:
  ```sql
  WHERE phone_number = '01012345678';
  ```

#### Anti-pattern 4: Tìm kiếm chuỗi với ký tự đại diện ở đầu (Leading Wildcard)
- **Sai:**
  ```sql
  -- Dấu '%' ở đầu vô hiệu hóa hoàn toàn B-Tree Index
  WHERE ename LIKE '%SMITH';
  WHERE ename LIKE '%SON%';
  ```
- **Bản chất kỹ thuật:** B-Tree sắp xếp các ký tự từ trái sang phải. Dấu `%` ở đầu khiến hệ thống không biết bắt đầu từ chữ cái nào trên cây Index.
- **Viết lại chuẩn SARGable:** Chỉ đặt ký tự đại diện ở cuối chuỗi (`Trailing Wildcard`):
  ```sql
  WHERE ename LIKE 'SMITH%'; -- Sử dụng tốt Index Range Scan
  ```
  *(Nếu bắt buộc phải tìm kiếm chuỗi con toàn diện, hãy sử dụng giải pháp Full-Text Search, Oracle Text, hoặc Reverse Key Index).*

---

### 5. Bảng tổng hợp Anti-patterns và giải pháp chuẩn SARGable

| Anti-pattern làm hỏng Index | Câu truy vấn Non-SARGable (Tránh) | Câu truy vấn SARGable chuẩn (Khuyên dùng) |
| --- | --- | --- |
| **Hàm trên cột ngày** | `WHERE EXTRACT(YEAR FROM dt) = 2026` | `WHERE dt >= DATE '2026-01-01' AND dt < DATE '2027-01-01'` |
| **Hàm trên cột chuỗi** | `WHERE UPPER(status) = 'ACTIVE'` | Dùng Function-based Index hoặc lưu dữ liệu chuẩn hoa |
| **Phép tính số học** | `WHERE amount * 1.1 > 1000` | `WHERE amount > 1000 / 1.1` |
| **Ép kiểu ngầm định** | `WHERE code_str = 100` | `WHERE code_str = '100'` |
| **Wildcard ở đầu chuỗi** | `WHERE name LIKE '%TECH'` | `WHERE name LIKE 'TECH%'` |

---

### 6. Quy ước bổ sung cho SQL trong pipeline AI

Với pipeline có các model SQL do AI sinh, review hoặc refactor tự động:
- **Xác định rõ Grain của truy vấn:** Mỗi khối truy vấn cần nêu rõ 1 dòng kết quả đại diện cho thực thể gì (ví dụ: 1 dòng = 1 đơn hàng, hay 1 dòng = 1 mặt hàng chi tiết).
- **Tuyệt đối tránh `SELECT *` trong model sản xuất:** Liệt kê tường minh danh sách cột để schema drift (thay đổi cấu trúc bảng nguồn) không làm sai lệch hợp đồng dữ liệu của pipeline.
- **Tách bước bằng CTE (Common Table Expression):** Dùng `WITH cte AS (...)` để chia tách các bước xử lý dữ liệu phức tạp thay vì lồng nhiều tầng subquery khó đọc.
- **Kiểm soát tính tất định (Deterministic):** Luôn có `ORDER BY` rõ ràng khi kết hợp phân trang hoặc lấy Top-N, bảo đảm AI và hệ thống kiểm thử tự động trả về cùng một kết quả nhất quán.

---

### 7. Checklist kiểm duyệt SQL trước khi Merge vào Production

Trước khi tạo pull request hoặc phê duyệt một query SQL vào kho mã nguồn:
1. [ ] **Tên đối tượng:** Nhất quán theo `snake_case`, không trùng từ khóa dành riêng của DBMS.
2. [ ] **Alias:** Phản ánh đúng ngữ nghĩa thực thể (`cust`, `ord`, `emp`), không dùng alias 1 ký tự (`a`, `b`).
3. [ ] **Căn lề & Mệnh đề WHERE:** Các điều kiện `AND`/`OR` được căn thẳng dòng; dùng ngoặc đơn `( )` rõ ràng khi kết hợp `AND` với `OR`.
4. [ ] **Kiểm tra SARGable:** Không bọc hàm hoặc tính toán trên cột đã đánh Index trong mệnh đề `WHERE` (`YEAR(date)`, `sal * 12`).
5. [ ] **Ép kiểu:** So sánh dữ liệu đúng kiểu (chuỗi có nháy đơn, số không nháy).
6. [ ] **NULL & Xử lý biên:** Mệnh đề `NOT IN` không chứa `NULL` từ subquery; các phép toán số học có xử lý `COALESCE` / `NVL` khi cần.

---

## 8. Bảng ma trận so sánh Oracle vs SQL Server về Style Guide và Tối ưu hóa truy vấn

| Khía cạnh kỹ thuật | Oracle Database | Microsoft SQL Server | Điểm khác biệt thi cử SQLD |
| :--- | :--- | :--- | :--- |
| **Bí danh bảng (`AS`)** | **CẤM từ khóa `AS`** trong mệnh đề `FROM` (`FROM emp e`) | Cho phép tùy chọn từ khóa `AS` (`FROM emp AS e`) | Lỗi cú pháp rất phổ biến khi chuyển từ SQL Server sang Oracle. |
| **Lưu giá trị NULL trong B-Tree** | Cột đơn lẻ: **Không lưu NULL** trong Index | **Lưu trữ cả giá trị NULL** trong Index | Trong Oracle, `WHERE col IS NULL` thường không dùng được B-Tree Index đơn cột. |
| **Đánh chỉ mục dựa trên hàm** | Hỗ trợ trực tiếp **Function-based Index** (`CREATE INDEX idx ON t (UPPER(col))`) | Dùng **Computed Column** kèm từ khóa `PERSISTED` rồi đánh index | Oracle cho phép tối ưu trực tiếp biểu thức hàm bằng FBI. |
| **Ép kiểu chuỗi vs số** | Chuỗi so với Số: Cột chuỗi bị ép thành số (`TO_NUMBER(str_col)`) | Cột chuỗi bị ép kiểu sang số (ưu tiên kiểu số cao hơn) | Làm mất Index trên cột chuỗi và có nguy cơ lỗi runtime nếu chứa chữ cái. |
| **Gợi ý tối ưu hóa (Optimizer Hints)** | Cú pháp comment đặc biệt: `/*+ INDEX(t idx_name) */` | Dùng mệnh đề `WITH (INDEX(idx_name))` hoặc `OPTION (...)` | Oracle đưa hint vào ngay sau từ khóa `SELECT /*+ ... */`. |
| **Phân biệt chữ hoa / chữ thường** | Mặc định **phân biệt hoa thường** (Case-sensitive) | Mặc định **không phân biệt** (CI - Case Insensitive Collation) | Trong Oracle, tìm chuỗi hoa thường cần chuẩn hóa hoặc dùng FBI. |

---

## 9. Cạm bẫy thi cử trọng điểm (출제 함정 & 오답 노트)

> [!WARNING]
> Dưới đây là 5 cạm bẫy kinh điển làm mất hiệu năng truy vấn và sai lệch logic trong đề thi SQLD:

### Cạm bẫy 1: Bẫy ép kiểu ngầm định làm mất Index (Implicit Type Conversion Trap)
- **Tình huống thi:** Bảng `CUSTOMER` có cột `PHONE` kiểu dữ liệu `VARCHAR2(20)` đã được đánh B-Tree Index.
  ```sql
  -- LỖI HIỆU NĂNG:
  SELECT * FROM CUSTOMER WHERE PHONE = 01012345678;
  ```
- **Bản chất thực thi:** Theo quy tắc chuyển đổi kiểu của Oracle, kiểu dữ liệu `NUMBER` có độ ưu tiên cao hơn kiểu `VARCHAR2`. Do đó, hệ thống sẽ ngầm bọc hàm `TO_NUMBER()` lên cột của bảng:
  `WHERE TO_NUMBER(PHONE) = 1012345678`
- **Hậu quả:** Cột `PHONE` bị bọc hàm nên B-Tree Index bị **vô hiệu hóa hoàn toàn**, Optimizer bắt buộc phải quét toàn bộ bảng (`TABLE ACCESS FULL`)! Hơn nữa, nếu có bản ghi chứa ký tự gạch nối (ví dụ `'010-1234-5678'`), truy vấn sẽ ném lỗi runtime `ORA-01722: invalid number`!
- **Ngược lại:** Nếu cột `SAL` là kiểu `NUMBER` và viết `WHERE SAL = '3000'`, Oracle sẽ ngầm ép hằng số thành số: `WHERE SAL = TO_NUMBER('3000')`. Khi đó hàm bọc ngoài hằng số chứ không bọc vào cột, nên **Index trên cột SAL vẫn được sử dụng bình thường**!

### Cạm bẫy 2: Phép tính toán học trên cột Index
- Viết: `WHERE SAL * 12 > 60000;` $\rightarrow$ Phép nhân `* 12` tác động trực tiếp lên từng giá trị trên đĩa của cột `SAL`, khiến hệ thống không thể nhảy nhót trên cây B-Tree $\rightarrow$ **Full Table Scan**.
- Viết chuẩn SARGable: `WHERE SAL > 60000 / 12;` $\rightarrow$ Phép chia `60000 / 12 = 5000` được tính trước 1 lần duy nhất thành hằng số, Optimizer dùng **`INDEX RANGE SCAN`** cực nhanh!

### Cạm bẫy 3: Ký tự đại diện đứng đầu trong mệnh đề LIKE
- `WHERE ENAME LIKE '%KING'` hoặc `WHERE ENAME LIKE '%ING%'`:
  Cây B-Tree sắp xếp các khóa theo thứ tự chữ cái từ trái qua phải. Dấu `%` ở đầu chuỗi đồng nghĩa với việc ký tự đầu tiên có thể là bất kỳ chữ cái nào từ A đến Z, hệ thống không thể định vị nhánh cây cần duyệt $\rightarrow$ **Bắt buộc quét toàn bộ bảng**.
- `WHERE ENAME LIKE 'KING%'`: Ký tự bắt đầu cố định là `'K'`, Optimizer định vị ngay nút `'K'` trên cây Index và chỉ duyệt dải giá trị đó qua `INDEX RANGE SCAN`.

### Cạm bẫy 4: Subquery của NOT IN trả về dù chỉ một giá trị NULL
- Cú pháp:
  ```sql
  SELECT ENAME FROM EMP
  WHERE EMPNO NOT IN (SELECT MGR FROM EMP);
  ```
- **Hiện tượng:** Truy vấn không trả về bất kỳ dòng nào (0 dòng), dù trong công ty có rất nhiều nhân viên không phải là quản lý!
- **Nguyên nhân:** Trong bảng `EMP`, sếp tổng `KING` có `MGR IS NULL`. Mệnh đề `NOT IN (7566, 7698, ..., NULL)` được phân rã thành:
  `EMPNO != 7566 AND EMPNO != 7698 AND ... AND EMPNO != NULL`
  Trong logic tam trị của SQL, `EMPNO != NULL` trả về **`UNKNOWN`**. Mệnh đề `AND` gặp `UNKNOWN` sẽ không bao giờ có thể cho ra kết quả `TRUE`!
- **Khắc phục:** Luôn thêm điều kiện `WHERE MGR IS NOT NULL` trong subquery hoặc thay thế bằng `NOT EXISTS`.

### Cạm bẫy 5: Nhầm lẫn độ ưu tiên giữa toán tử AND và OR
- Độ ưu tiên: `NOT` $\rightarrow$ `AND` $\rightarrow$ `OR`.
- Biểu thức: `WHERE DEPTNO = 10 OR DEPTNO = 20 AND SAL > 2000`
  sẽ được hiểu ngầm định là:
  `WHERE DEPTNO = 10 OR (DEPTNO = 20 AND SAL > 2000)`
- Toàn bộ nhân viên phòng 10 (bất kể lương thấp bao nhiêu) đều bị lấy ra! Nếu muốn lọc những người có lương trên 2000 thuộc phòng 10 hoặc 20, bắt buộc phải dùng ngoặc đơn:
  `WHERE (DEPTNO = 10 OR DEPTNO = 20) AND SAL > 2000`

---

## 10. Câu hỏi trắc nghiệm thi thử mô phỏng (실전 기출 변형 문제 & 정답 해설)

### Câu 1: Khả năng sử dụng Index của các vị từ tìm kiếm (SARGability) (Độ khó: Trung bình)
Bảng `TB_ORDERS` có chỉ mục B-Tree Index trên cột ngày đặt hàng `ORDER_DATE` (kiểu `DATE`). Câu lệnh truy vấn nào dưới đây có thể **TẬN DỤNG ĐƯỢC CHỈ MỤC B-TREE (Index Range Scan)** thay vì quét toàn bộ bảng?

A. `SELECT * FROM TB_ORDERS WHERE TO_CHAR(ORDER_DATE, 'YYYYMM') = '202610';`
B. `SELECT * FROM TB_ORDERS WHERE EXTRACT(YEAR FROM ORDER_DATE) = 2026;`
C. `SELECT * FROM TB_ORDERS WHERE ORDER_DATE >= TO_DATE('2026-10-01', 'YYYY-MM-DD') AND ORDER_DATE < TO_DATE('2026-11-01', 'YYYY-MM-DD');`
D. `SELECT * FROM TB_ORDERS WHERE TRUNC(ORDER_DATE) = TO_DATE('2026-10-16', 'YYYY-MM-DD');`

> **Đáp án chính xác:** **C**
>
> **Giải thích chi tiết từng lựa chọn:**
> - **Lựa chọn C đúng:** Cột `ORDER_DATE` đứng độc lập nguyên thủy, không hề bị bọc bởi bất kỳ hàm hay phép toán nào. Phép so sánh dải `>=` và `<` trên hằng số ngày tháng cho phép Optimizer thực hiện **`INDEX RANGE SCAN`** định vị trực tiếp điểm bắt đầu và kết thúc trên cây B-Tree.
> - **Lựa chọn A, B, D sai:** Đều bọc các hàm biến đổi (`TO_CHAR`, `EXTRACT`, `TRUNC`) trực tiếp lên cột `ORDER_DATE`, làm biến dạng giá trị khóa Index và khiến hệ thống bắt buộc phải thực hiện quét toàn bộ bảng (`TABLE ACCESS FULL`).

---

### Câu 2: Ép kiểu ngầm định và ảnh hưởng tới Index (Độ khó: Cao)
Xét bảng `TB_ACCOUNT` có cột `ACCOUNT_NO` có kiểu dữ liệu là `VARCHAR2(20)` và đã được tạo chỉ mục `IX_ACCOUNT_NO`.
Xét hai câu lệnh truy vấn sau:

```sql
-- Query 1:
SELECT * FROM TB_ACCOUNT WHERE ACCOUNT_NO = 1234567890;

-- Query 2:
SELECT * FROM TB_ACCOUNT WHERE ACCOUNT_NO = '1234567890';
```

Phát biểu nào sau đây là **CHÍNH XÁC NHẤT** về kế hoạch thực thi (Execution Plan) của hai câu truy vấn trên trong Oracle?

A. Cả hai câu truy vấn đều sử dụng `INDEX RANGE SCAN` trên chỉ mục `IX_ACCOUNT_NO`.
B. Query 1 bị `TABLE ACCESS FULL` do ép kiểu ngầm định trên cột; Query 2 sử dụng `INDEX RANGE SCAN`.
C. Query 1 sử dụng `INDEX RANGE SCAN`; Query 2 bị `TABLE ACCESS FULL` vì so sánh với chuỗi ký tự.
D. Cả hai câu truy vấn đều bị `TABLE ACCESS FULL` vì Oracle không thể so sánh số tài khoản qua Index.

> **Đáp án chính xác:** **B**
>
> **Giải thích chi tiết từng lựa chọn:**
> - **Phân tích cơ chế ép kiểu:**
>   - Trong Query 1: Cột `ACCOUNT_NO` là `VARCHAR2`, nhưng giá trị so sánh `1234567890` là số (`NUMBER`). Theo luật ưu tiên kiểu dữ liệu của Oracle, hệ thống sẽ ngầm ép cột chuỗi thành số: `TO_NUMBER(ACCOUNT_NO) = 1234567890`. Việc bọc hàm ngầm định này làm tê liệt hoàn toàn B-Tree Index, buộc Optimizer phải quét toàn bộ bảng (`TABLE ACCESS FULL`).
>   - Trong Query 2: Kiểu dữ liệu giữa cột `ACCOUNT_NO` (`VARCHAR2`) và hằng số `'1234567890'` (`VARCHAR2`) hoàn toàn tương thích, không xảy ra ép kiểu ngầm định $\rightarrow$ Tận dụng tối đa chỉ mục qua `INDEX RANGE SCAN` (hoặc Unique Scan nếu là PK).
> - **Lựa chọn B:** Hoàn toàn chính xác.
> - **Lựa chọn A, C, D sai:** Đều không nắm vững quy tắc ưu tiên ép kiểu dữ liệu giữa chuỗi và số của Oracle.

---

### Câu 3: Hiện tượng tập kết quả rỗng khi dùng NOT IN với NULL (Độ khó: Trung bình)
Cho bảng `DEPARTMENT` (gồm các mã phòng: 10, 20, 30) và bảng `EMPLOYEE` có cột `DEPTNO` chứa các giá trị: `10, 20, NULL`.
Người dùng chạy câu lệnh SQL sau:

```sql
SELECT DNAME
FROM DEPARTMENT
WHERE DEPTNO NOT IN (SELECT DEPTNO FROM EMPLOYEE);
```

Kết quả của câu truy vấn trên là gì?

A. Trả về tên của phòng ban 30.
B. Không trả về bất kỳ dòng nào (Empty set / 0 dòng).
C. Trả về toàn bộ danh sách phòng ban 10, 20, 30.
D. Hệ thống báo lỗi cú pháp do có giá trị NULL trong mệnh đề NOT IN.

> **Đáp án chính xác:** **B**
>
> **Giải thích chi tiết từng lựa chọn:**
> - Tập kết quả của truy vấn con `(SELECT DEPTNO FROM EMPLOYEE)` trả về tập hợp `{10, 20, NULL}`.
> - Mệnh đề `WHERE DEPTNO NOT IN (10, 20, NULL)` được kiểm tra logic:
>   - Xét với phòng 30: `(30 != 10) AND (30 != 20) AND (30 != NULL)`
>   - Ta có: `TRUE AND TRUE AND UNKNOWN` $\rightarrow$ Kết quả chung cuộc là **`UNKNOWN`**!
> - Theo định lý lọc dữ liệu của SQL, chỉ những dòng có điều kiện WHERE lượng giá là **`TRUE`** mới được trả về. Do điều kiện là `UNKNOWN`, dòng phòng 30 bị loại bỏ.
> - Kết quả: Không có bất kỳ dòng nào được trả về (0 dòng).
> - **Lựa chọn B:** Hoàn toàn chính xác.
> - **Lựa chọn A sai:** Bẫy kinh điển của thí sinh nghĩ rằng phòng 30 sẽ được chọn.

---

### Câu 4: Quy tắc cú pháp viết câu lệnh SQL trong Oracle (Độ khó: Dễ)
Xét các câu lệnh SQL dưới đây, câu lệnh nào sẽ **BỊ LỖI CÚ PHÁP (Syntax Error)** khi chạy trên Oracle Database?

A. `SELECT e.empno, e.ename FROM emp e WHERE e.deptno = 10;`
B. `SELECT e.empno, e.ename AS employee_name FROM emp e;`
C. `SELECT e.empno, e.ename FROM emp AS e WHERE e.deptno = 10;`
D. `SELECT emp.empno, emp.ename FROM emp WHERE emp.deptno = 10;`

> **Đáp án chính xác:** **C**
>
> **Giải thích chi tiết từng lựa chọn:**
> - **Lựa chọn C sai cú pháp:** Trong Oracle SQL, từ khóa `AS` **tuyệt đối không được sử dụng** khi đặt bí danh cho bảng trong mệnh đề `FROM` (viết `FROM emp AS e` sẽ ném lỗi `ORA-00933: SQL command not properly ended`). (Khác với Microsoft SQL Server hoặc PostgreSQL cho phép dùng `AS` cho table alias).
> - **Lựa chọn A, B, D hợp lệ:** Cú pháp bí danh bảng không dùng `AS` (`FROM emp e`) và bí danh cột có `AS` (`e.ename AS employee_name`) hoàn toàn chuẩn mực trong Oracle.
