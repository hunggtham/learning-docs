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
