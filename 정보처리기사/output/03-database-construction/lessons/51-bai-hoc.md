# 7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)

## 학습 목표 (Mục tiêu)
- Nắm vững 4 toán tử tập hợp trong ngôn ngữ SQL: **`UNION` (Hợp khử trùng)**, **`UNION ALL` (Hợp giữ nguyên trùng)**, **`INTERSECT` (Giao)**, và **`MINUS` / `EXCEPT` (Hiệu)** cùng điều kiện tương thích tập hợp.
- Phân biệt chi tiết các loại kết nối bảng (JOIN): **INNER JOIN**, **LEFT OUTER JOIN**, **RIGHT OUTER JOIN**, **FULL OUTER JOIN**, **SELF JOIN**, và **CROSS JOIN**.
- Nắm chắc ký hiệu cổ điển của Oracle trong phép Outer Join: **Dấu `(+)` đặt ở bảng bị thiếu dữ liệu** (ví dụ: `A.id = B.id(+)` chính là LEFT OUTER JOIN).

## 핵심 키워드 (Từ khóa)
- 집합 연산자 (Toán tử tập hợp / Set Operators)
- UNION / UNION ALL
- INTERSECT (Phép giao)
- MINUS / EXCEPT (Phép hiệu)
- 조인 (Phép kết nối / JOIN)
- INNER JOIN (Kết nối trong)
- OUTER JOIN (Kết nối ngoài: LEFT, RIGHT, FULL)
- SELF JOIN (Tự kết nối)
- CROSS JOIN (Tích Đề-các / Cartesian Product)
- 오라클 (+) 기호 (Ký hiệu (+) của Oracle)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([12-bai-hoc.md](12-bai-hoc.md), [16-bai-hoc.md](16-bai-hoc.md), [50-bai-hoc.md](50-bai-hoc.md)):** Các toán tử tập hợp và JOIN trong SQL là sự hiện thực hóa trực tiếp các toán tử đại số quan hệ thuần túy ($\bowtie, \times$) và toán tử tập hợp thông thường ($\cup, \cap, -$) trên máy tính.
- **Tiếp nối sang bài sau ([52-bai-hoc.md](52-bai-hoc.md)):** Bài tiếp theo sẽ tổng hợp toàn diện ngôn ngữ dữ liệu quan hệ, đối chiếu giữa đại số quan hệ và giải tích quan hệ.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh sự khác nhau giữa `UNION` và `UNION ALL`:
  - **UNION:** Khử trùng lặp $\rightarrow$ Hệ thống phải tốn chi phí sắp xếp (Sort).
  - **UNION ALL:** Giữ nguyên trùng lặp $\rightarrow$ Không cần sắp xếp, tốc độ chạy nhanh hơn.
- Nhớ quy tắc dấu `(+)` trong Oracle: **Dấu `(+)` nằm ở bên nào thì bên kia là BẢNG CHÍNH (Được ưu tiên lấy hết)**. Ví dụ: `WHERE A.id = B.id(+)` $\rightarrow$ Bảng A là chính $\rightarrow$ **LEFT OUTER JOIN**.

---

## 7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng 4 toán tử tập hợp trong SQL (집합 연산자):**
  | Toán tử | Chức năng kỹ thuật | Xử lý trùng lặp & Chi phí | Tương đương trong toán học |
  |---|---|---|:---:|
  | **`UNION`** | Hợp hai tập kết quả truy vấn lại thành một | **Tự động loại bỏ các dòng trùng lặp**; tốn chi phí sắp xếp (Sort) dữ liệu | $R \cup S$ |
  | **`UNION ALL`** | Gộp hai tập kết quả truy vấn lại thành một | **Giữ nguyên toàn bộ các dòng trùng lặp**; không sắp xếp $\rightarrow$ tốc độ nhanh nhất | $R \cup S$ (có lặp) |
  | **`INTERSECT`** | Trích xuất các dòng xuất hiện đồng thời ở cả hai tập kết quả | Tự động loại bỏ trùng lặp | $R \cap S$ |
  | **`MINUS` / `EXCEPT`** | Lấy các dòng có trong tập kết quả thứ nhất nhưng không có trong tập kết quả thứ hai | Tự động loại bỏ trùng lặp (`MINUS` trong Oracle; `EXCEPT` trong SQL Server, PostgreSQL) | $R - S$ |
  - **Điều kiện tương thích tập hợp (Union-compatible):** Hai câu lệnh SELECT được gộp phải có **cùng số lượng cột** và các cột tương ứng theo thứ tự phải có **kiểu dữ liệu tương thích**.

- **2. Bảng phân loại các phép JOIN theo chuẩn đề thi:**
  | Loại JOIN | Cú pháp ANSI SQL | Bản chất kết quả dữ liệu | Ký hiệu Oracle truyền thống |
  |---|---|---|:---:|
  | **INNER JOIN** | `FROM A INNER JOIN B ON A.id = B.id` | Chỉ lấy các dòng có giá trị khóa kết nối **khớp nhau ở cả hai bảng** (Phần giao). | `WHERE A.id = B.id` |
  | **LEFT OUTER JOIN** | `FROM A LEFT OUTER JOIN B ON A.id = B.id` | Lấy **toàn bộ dữ liệu bảng A**; nếu bảng B không có dữ liệu khớp thì các cột của B được điền **`NULL`**. | `WHERE A.id = B.id(+)` |
  | **RIGHT OUTER JOIN** | `FROM A RIGHT OUTER JOIN B ON A.id = B.id` | Lấy **toàn bộ dữ liệu bảng B**; nếu bảng A không có dữ liệu khớp thì các cột của A được điền **`NULL`**. | `WHERE A.id(+) = B.id` |
  | **FULL OUTER JOIN** | `FROM A FULL OUTER JOIN B ON A.id = B.id` | Lấy **toàn bộ dữ liệu của cả hai bảng**; bên nào thiếu dữ liệu tương ứng thì điền **`NULL`**. | Không hỗ trợ trực tiếp bằng (+), phải dùng UNION giữa Left và Right |
  | **SELF JOIN** | `FROM A e1 JOIN A e2 ON e1.mgr = e2.emp_id` | Một bảng **tự kết nối với chính nó**; bắt buộc phải sử dụng bí danh (Alias) khác nhau. | Dùng trong mô hình cây gia phả, nhân viên - người quản lý |
  | **CROSS JOIN** | `FROM A CROSS JOIN B` | Tạo ra tích Đề-các (Cartesian Product), ghép mọi dòng của A với mọi dòng của B; số dòng = $Dòng_A \times Dòng_B$. | `FROM A, B` (không có WHERE) |

- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Toán tử tập hợp nào không khử trùng lặp và có tốc độ nhanh nhất?"* $\rightarrow$ Đáp án: **`UNION ALL`**.
  - Đề đưa biểu thức Oracle: `WHERE A.dept_id = B.dept_id(+)` hỏi đây là phép Join nào $\rightarrow$ Đáp án: **LEFT OUTER JOIN**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa bằng số liệu thực tế:**
  - Bảng A gồm 2 dòng: `{1, 2}`. Bảng B gồm 2 dòng: `{2, 3}`.
    - `A UNION B` $\rightarrow$ `{1, 2, 3}` (3 dòng).
    - `A UNION ALL B` $\rightarrow$ `{1, 2, 2, 3}` (4 dòng).
    - `A INTERSECT B` $\rightarrow$ `{2}` (1 dòng).
    - `A MINUS B` $\rightarrow$ `{1}` (1 dòng).
- **Minh họa SELF JOIN tìm tên người quản lý:**
  ```sql
  SELECT E.HoTen AS NhanVien, M.HoTen AS QuanLy
  FROM NHAN_VIEN E
  LEFT JOIN NHAN_VIEN M ON E.MaQuanLy = M.MaNV;
  ```
  - Dùng LEFT JOIN giúp nhân viên cấp cao nhất (Giám đốc không có người quản lý, `MaQuanLy = NULL`) vẫn được hiển thị trong kết quả với cột `QuanLy = NULL`.

### 복습 체크리스트
- [ ] Phân biệt được sự khác nhau giữa UNION (loại trùng) và UNION ALL (giữ trùng).
- [ ] Nắm được điều kiện để thực hiện phép toán tập hợp (cùng số cột, cùng kiểu dữ liệu).
- [ ] Phân biệt được INNER JOIN, LEFT OUTER JOIN, RIGHT OUTER JOIN, FULL OUTER JOIN.
- [ ] Nhớ cách đọc dấu (+) trong Oracle: (+) ở bên nào thì bên đó là bên thiếu dữ liệu.
