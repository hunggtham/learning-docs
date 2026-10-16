# Set Operators (집합 연산자 — Toán tử tập hợp)

Trong SQL, các toán tử tập hợp (**Set Operators — 집합 연산자**) cho phép kết hợp kết quả của hai hoặc nhiều câu lệnh `SELECT` độc lập thành một tập kết quả duy nhất.

> **Khác biệt cốt tử giữa JOIN và Set Operator:**
> - **JOIN (조인):** Ghép nối các bảng theo **chiều ngang (Horizontal Combine)** dựa trên điều kiện quan hệ cột (Column Relationship). Kết quả trả về sẽ mở rộng thêm số lượng cột.
> - **Set Operator (집합 연산자):** Ghép nối các tập kết quả theo **chiều dọc (Vertical Combine)**. Kết quả trả về tăng thêm số dòng, trong khi số lượng cột giữ nguyên theo cấu trúc của câu lệnh `SELECT` đầu tiên.

```text
       JOIN (Ghép ngang)                 Set Operator (Ghép dọc)
 ┌─────────┬─────────┐              ┌─────────────────────────┐
 │ Bảng A  │ Bảng B  │              │    SELECT Kết quả A     │
 │ (Cột 1) │ (Cột 2) │              ├─────────────────────────┤
 └─────────┴─────────┘              │  UNION / INTERSECT ...  │
                                    ├─────────────────────────┤
                                    │    SELECT Kết quả B     │
                                    └─────────────────────────┘
```

---

## 1. Bốn toán tử tập hợp cốt lõi (4대 집합 연산자)

Trong chuẩn ANSI SQL và kỳ thi SQLD, có 4 toán tử tập hợp quan trọng:

```text
1. UNION      : Hợp tập hợp (Khử trùng lặp, có phát sinh sắp xếp)
2. UNION ALL  : Hợp tập hợp (Giữ nguyên trùng lặp, KHÔNG sắp xếp, tốc độ cao)
3. INTERSECT  : Giao tập hợp (Chỉ lấy phần tử chung, khử trùng lặp)
4. MINUS      : Hiệu tập hợp (Oracle: lấy tập A trừ tập B, khử trùng lặp)
   (EXCEPT)   : Hiệu tập hợp (SQL Server / PostgreSQL tương đương với MINUS)
```

Giả sử ta có hai tập dữ liệu đơn giản:
- Tập hợp $A = \{1, 2, 3\}$
- Tập hợp $B = \{2, 3, 4\}$

```text
A UNION B       → {1, 2, 3, 4}       (Gộp chung, phần tử 2 và 3 bị loại bớt 1 bản sao)
A UNION ALL B   → {1, 2, 3, 2, 3, 4} (Ghép nối trực tiếp, giữ nguyên 2 và 3 lặp lại)
A INTERSECT B   → {2, 3}             (Chỉ giữ lại các phần tử cùng xuất hiện ở cả hai)
A MINUS B       → {1}                (Lấy các phần tử có trong A nhưng KHÔNG có trong B)
B MINUS A       → {4}                (Lấy các phần tử có trong B nhưng KHÔNG có trong A)
```

---

## 2. Chi tiết từng toán tử tập hợp

### 2.1 UNION (합집합 — Hợp tập hợp khử trùng lặp)

**KR:** UNION은 여러 개의 SELECT 문의 결과를 결합하여 중복된 행을 제거하고 단일 결과 집합으로 반환한다.
**VI:** `UNION` hợp nhất kết quả của các câu lệnh `SELECT`, tự động **loại bỏ các dòng trùng lặp (Deduplication)** và ngầm thực hiện thao tác **sắp xếp (Sort)** các dòng dữ liệu.

Ví dụ hai bảng diễn viên trong phim Sweet Home:

```sql
SELECT ACTOR_NAME, REAL_NAME
FROM SWEET_HOME_SEASON1

UNION

SELECT ACTOR_NAME, REAL_NAME
FROM SWEET_HOME_SEASON2;
```

Quy trình xử lý của CSDL:
1. Thực thi câu lệnh `SELECT` thứ nhất.
2. Thực thi câu lệnh `SELECT` thứ hai.
3. Ghép hai tập dữ liệu lại với nhau.
4. Thực hiện thuật toán sắp xếp (`Sort Unique` hoặc `Hash Unique`) để tìm và loại bỏ tất cả các dòng trùng lặp hoàn toàn trên mọi cột.

---

### 2.2 UNION ALL (합집합 — Hợp tập hợp giữ nguyên trùng lặp)

**KR:** UNION ALL은 중복된 행을 제거하지 않고, 정렬 작업 없이 모든 결과를 단순히 합쳐서 반환한다.
**VI:** `UNION ALL` kết hợp toàn bộ kết quả của các câu `SELECT`, **giữ nguyên toàn bộ các dòng trùng lặp** và **HOÀN TOÀN KHÔNG thực hiện thao tác sắp xếp**.

```sql
SELECT ACTOR_NAME, REAL_NAME
FROM SWEET_HOME_SEASON1

UNION ALL

SELECT ACTOR_NAME, REAL_NAME
FROM SWEET_HOME_SEASON2;
```

Nếu diễn viên Song Kang đóng ở cả mùa 1 và mùa 2, tên của anh ấy sẽ xuất hiện **2 lần** trong kết quả cuối cùng.

#### ⚡ Phân tích hiệu năng chuyên sâu: UNION vs UNION ALL

| Tiêu chí | UNION | UNION ALL |
| :--- | :--- | :--- |
| **Loại bỏ trùng lặp** | CÓ (Deduplicated) | KHÔNG (Keeps Duplicates) |
| **Thao tác ngầm (Internal Operation)** | Phát sinh `SORT UNIQUE` hoặc `HASH UNIQUE` | Không có (Chỉ đơn giản là `APPEND`) |
| **Tài nguyên tiêu tốn** | Tốn CPU và bộ nhớ tạm (PGA / Temp Tablespace) | Tiết kiệm tối đa CPU và bộ nhớ |
| **Tốc độ thực thi** | Chậm hơn đối với tập dữ liệu lớn | Cực nhanh (High Performance) |
| **Khuyên dùng trong thực tế** | Chỉ dùng khi bắt buộc phải loại bỏ trùng lặp | Ưu tiên dùng khi tập dữ liệu không giao nhau hoặc cần giữ vết |

---

### 2.3 INTERSECT (교집합 — Giao tập hợp)

**KR:** INTERSECT는 여러 SELECT 문의 결과에서 공통으로 존재하는 행만 중복을 제거하여 반환한다.
**VI:** `INTERSECT` trả về các dòng **đồng thời xuất hiện trong tất cả các tập kết quả**, tự động loại bỏ trùng lặp và sắp xếp.

```sql
SELECT ACTOR_NAME, REAL_NAME
FROM SWEET_HOME_SEASON1

INTERSECT

SELECT ACTOR_NAME, REAL_NAME
FROM SWEET_HOME_SEASON2;
```

Kết quả: Chỉ những diễn viên tham gia đóng ở **cả mùa 1 VÀ mùa 2** mới được hiển thị.

---

### 2.4 MINUS / EXCEPT (차집합 — Hiệu tập hợp)

**KR:** MINUS(Oracle) 또는 EXCEPT(SQL Server)는 첫 번째 SELECT 문의 결과에서 두 번째 SELECT 문의 결과에 포함된 행을 제외한 결과를 반환한다.
**VI:** `MINUS` (trong Oracle) hoặc `EXCEPT` (trong SQL Server) trả về các dòng **chỉ có trong kết quả thứ nhất mà không tồn tại trong kết quả thứ hai**, tự động loại bỏ trùng lặp.

```sql
-- Tìm các diễn viên chỉ đóng ở Season 1 mà không tiếp tục đóng ở Season 2
-- Cú pháp Oracle:
SELECT ACTOR_NAME, REAL_NAME
FROM SWEET_HOME_SEASON1
MINUS
SELECT ACTOR_NAME, REAL_NAME
FROM SWEET_HOME_SEASON2;

-- Cú pháp Microsoft SQL Server tương đương:
SELECT ACTOR_NAME, REAL_NAME
FROM SWEET_HOME_SEASON1
EXCEPT
SELECT ACTOR_NAME, REAL_NAME
FROM SWEET_HOME_SEASON2;
```

#### 🚨 Cạm bẫy tính bất đối xứng của phép Hiệu tập hợp:
Phép cộng tập hợp có tính giao hoán ($A \cup B = B \cup A$), nhưng phép trừ tập hợp **KHÔNG CÓ TÍNH GIAO HOÁN**:
$$A - B \ne B - A$$
- `A MINUS B`: Lấy những gì thuộc riêng về A.
- `B MINUS A`: Lấy những gì thuộc riêng về B.

---

## 3. Xử lý giá trị NULL trong Toán tử tập hợp

Đây là một điểm kiến thức rất đặc biệt trong chuẩn SQL mà đề thi SQLD thường dùng để thử thách thí sinh:

> **Quy tắc xử lý NULL trong Set Operators:**
> Trong các phép so sánh thông thường (`=`, `<>`, `IN`), `NULL` so sánh với `NULL` sẽ cho kết quả là `UNKNOWN`.
> **TUY NHIÊN, trong các toán tử tập hợp (`UNION`, `INTERSECT`, `MINUS`), hệ quản trị CSDL coi các giá trị NULL là HOÀN TOÀN BẰNG NHAU (`NULL = NULL`)!**

Ví dụ:
- Bảng A có dòng: `(10, NULL)`
- Bảng B có dòng: `(10, NULL)`

Khi thực thi:
1. `SELECT * FROM A UNION SELECT * FROM B;`
   → Hai dòng `(10, NULL)` được xem là **trùng lặp hoàn toàn**, kết quả chỉ trả về **1 dòng** `(10, NULL)`.
2. `SELECT * FROM A INTERSECT SELECT * FROM B;`
   → Dòng `(10, NULL)` xuất hiện ở cả hai bảng nên được coi là phần tử chung, kết quả trả về **1 dòng** `(10, NULL)`.
3. `SELECT * FROM A MINUS SELECT * FROM B;`
   → Dòng `(10, NULL)` ở bảng A bị dòng `(10, NULL)` ở bảng B triệt tiêu hoàn toàn, kết quả trả về **0 dòng**.

---

## 4. Bốn quy tắc vàng bắt buộc khi sử dụng Set Operators

Để câu lệnh sử dụng toán tử tập hợp có thể biên dịch và thực thi thành công, bắt buộc phải tuân thủ nghiêm ngặt 4 quy tắc sau:

### Quy tắc 1: Số lượng cột phải bằng nhau tuyệt đối
Mọi câu lệnh `SELECT` tham gia vào phép toán tập hợp phải trả về **cùng một số lượng cột**. Nếu một câu `SELECT` có 2 cột mà câu kia có 3 cột, hệ thống sẽ phát sinh lỗi biên dịch ngay lập tức:
- Trong Oracle: `ORA-01789: query block has incorrect number of result columns`.

```sql
-- ❌ LỖI ORA-01789 (Câu trên có 2 cột, câu dưới có 3 cột)
SELECT EMPNO, ENAME FROM EMP
UNION
SELECT DEPTNO, DNAME, LOC FROM DEPT;

-- ✅ ĐÚNG (Cùng có 2 cột)
SELECT EMPNO, ENAME FROM EMP
UNION
SELECT DEPTNO, DNAME FROM DEPT;
```

---

### Quy tắc 2: Kiểu dữ liệu tại vị trí tương ứng phải tương thích
Kiểu dữ liệu của các cột tại cùng một vị trí thứ tự từ trái sang phải phải tương thích với nhau (Data Type Compatibility).
- Cột 1 của SELECT 1 phải tương thích với Cột 1 của SELECT 2.
- Cột 2 của SELECT 1 phải tương thích với Cột 2 của SELECT 2.
- **Không yêu cầu tên cột phải giống nhau**, nhưng kiểu dữ liệu không được xung đột (ví dụ không thể ghép kiểu `NUMBER` với kiểu `DATE`).

```sql
-- ❌ LỖI ORA-01790: expression must have same datatype as corresponding expression
SELECT ENAME, HIREDATE FROM EMP   -- Cột 2 là DATE
UNION
SELECT DNAME, DEPTNO FROM DEPT;   -- Cột 2 là NUMBER
```

---

### Quy tắc 3: Tên cột hiển thị luôn lấy theo câu SELECT đầu tiên
Tiêu đề cột (Column Header / Alias) của toàn bộ tập kết quả cuối cùng **luôn luôn được quyết định bởi câu lệnh SELECT đầu tiên**. Mọi bí danh (Alias) được đặt ở câu lệnh `SELECT` thứ hai trở đi đều bị bỏ qua (Ignored).

```sql
SELECT EMPNO AS NHAN_VIEN_ID, ENAME AS HO_TEN
FROM EMP
UNION
SELECT DEPTNO AS PHONG_BAN_ID, DNAME AS TEN_PHONG
FROM DEPT;
```

Bảng kết quả trả về sẽ có 2 cột hiển thị là: `NHAN_VIEN_ID` và `HO_TEN` (không phải `PHONG_BAN_ID` hay `TEN_PHONG`).

---

### Quy tắc 4: Mệnh đề ORDER BY chỉ được đặt duy nhất ở CUỐI CÙNG
- **CẤM:** Không được phép đặt mệnh đề `ORDER BY` ở từng câu lệnh `SELECT` thành phần.
- **ĐÚNG:** Mệnh đề `ORDER BY` chỉ được phép xuất hiện **đúng 1 lần ở cuối cùng** của toàn bộ câu lệnh hợp kết quả.
- **Tên cột trong ORDER BY:** Chỉ được phép sử dụng **tên cột hoặc alias của câu SELECT đầu tiên**, hoặc sử dụng **chỉ số thứ tự cột (Column Position Index: 1, 2, ...)**. Nếu dùng alias của câu SELECT thứ hai sẽ báo lỗi.

```sql
-- ❌ SAI (Đặt ORDER BY ở giữa các SELECT gây lỗi cú pháp ORA-00933)
SELECT EMPNO, ENAME FROM EMP ORDER BY ENAME
UNION
SELECT DEPTNO, DNAME FROM DEPT;

-- ❌ SAI (Dùng tên cột chỉ có ở SELECT thứ 2 trong ORDER BY)
SELECT EMPNO AS ID, ENAME FROM EMP
UNION
SELECT DEPTNO, DNAME FROM DEPT
ORDER BY DNAME;

-- ✅ ĐÚNG (Dùng alias của SELECT đầu tiên)
SELECT EMPNO AS ID, ENAME FROM EMP
UNION
SELECT DEPTNO, DNAME FROM DEPT
ORDER BY ID;

-- ✅ ĐÚNG (Dùng vị trí cột 1, 2)
SELECT EMPNO, ENAME FROM EMP
UNION
SELECT DEPTNO, DNAME FROM DEPT
ORDER BY 1, 2;
```

> **Lưu ý về GROUP BY:**
> Trái ngược với `ORDER BY`, mệnh đề `GROUP BY` là logic xử lý nội bộ của từng câu truy vấn, do đó mỗi câu `SELECT` thành phần **hoàn toàn có quyền tự sử dụng GROUP BY riêng** của mình trước khi đưa kết quả vào phép toán tập hợp!

---

## 5. Bảng ma trận so sánh toàn diện các Toán tử tập hợp

| Tiêu chí | UNION | UNION ALL | INTERSECT | MINUS / EXCEPT |
| :--- | :--- | :--- | :--- | :--- |
| **Ý nghĩa toán học** | $A \cup B$ | $A \cup B$ | $A \cap B$ | $A - B$ |
| **Khử trùng lặp (Deduplication)** | **CÓ** | **KHÔNG** | **CÓ** | **CÓ** |
| **Phát sinh Sắp xếp ngầm (Sort)** | **CÓ** | **KHÔNG** | **CÓ** | **CÓ** |
| **Tốc độ / Hiệu năng** | Trung bình | **Rất cao (Nhanh nhất)** | Trung bình | Trung bình |
| **Tính giao hoán ($A \text{ op } B = B \text{ op } A$)** | CÓ | CÓ | CÓ | **KHÔNG** |
| **Cú pháp Oracle** | `UNION` | `UNION ALL` | `INTERSECT` | `MINUS` |
| **Cú pháp SQL Server** | `UNION` | `UNION ALL` | `INTERSECT` | `EXCEPT` |
| **Xử lý giá trị NULL** | Coi NULL = NULL | Giữ mọi dòng NULL | Coi NULL = NULL | Coi NULL = NULL |

---

## 6. Cạm bẫy thi cử trọng điểm (출제 함정 & 오답 노트)

1. **Bẫy vị trí mệnh đề ORDER BY:**
   - Đề thi thường lừa đặt `ORDER BY` ngay sau câu `SELECT` đầu tiên → Đây là lỗi cú pháp! `ORDER BY` chỉ được đặt ở cuối cùng.
2. **Bẫy tên cột trong mệnh đề ORDER BY:**
   - Cố tình dùng alias của câu SELECT thứ hai để sort kết quả cuối cùng → Lỗi không tìm thấy cột. Bắt buộc phải dùng tên cột của SELECT thứ nhất hoặc vị trí 1, 2, ...
3. **Bẫy số lượng cột và kiểu dữ liệu:**
   - Các nhánh SELECT phải có số cột bằng nhau tuyệt đối.
   - Các cột đối ứng phải cùng họ kiểu dữ liệu (Numeric với Numeric, Character với Character).
4. **Bẫy khác biệt giữa MINUS và EXCEPT:**
   - Trong đề thi kiểm tra cú pháp Oracle: từ khóa là `MINUS`.
   - Trong đề thi kiểm tra cú pháp SQL Server: từ khóa là `EXCEPT`. Nếu dùng `MINUS` trên SQL Server sẽ bị báo lỗi không nhận diện từ khóa.
5. **Bẫy UNION vs UNION ALL khi tính tổng số dòng:**
   - Cho bảng A có 5 dòng (chứa giá trị: 1, 2, 2, 3, 4).
   - Bảng B có 4 dòng (chứa giá trị: 2, 3, 4, 5).
   - Hỏi số dòng trả về của `UNION`: Tập duy nhất là $\{1, 2, 3, 4, 5\} \rightarrow$ **5 dòng**.
   - Hỏi số dòng trả về của `UNION ALL`: Tổng số dòng là $5 + 4 =$ **9 dòng**.

---

## 7. Câu hỏi trắc nghiệm thi thử mô phỏng (실전 기출 변형 문제 & 정답 해설)

### Câu 1 (Độ khó: Dễ — Quy tắc tên cột và ORDER BY)
Xét đoạn mã SQL sau thực thi trên hệ quản trị cơ sở dữ liệu Oracle:

```sql
SELECT EMPNO AS CODE, ENAME AS FULL_NAME, SAL
FROM EMP
WHERE DEPTNO = 10

UNION

SELECT DEPTNO AS D_CODE, DNAME AS DEPT_NAME, NULL
FROM DEPT
WHERE DEPTNO = 20

ORDER BY DEPT_NAME;
```

Kết quả của câu lệnh trên là gì?

A. Câu lệnh thực thi thành công và sắp xếp kết quả theo tên phòng ban `DEPT_NAME`.
B. Phát sinh lỗi thực thi vì cột `DEPT_NAME` không phải là tên cột của câu lệnh SELECT đầu tiên.
C. Phát sinh lỗi vì kiểu dữ liệu của `SAL` (kiểu số) và `NULL` không tương thích với nhau.
D. Câu lệnh tự động đổi tên cột kết quả thành `D_CODE` và `DEPT_NAME`.

**Đáp án đúng:** **B**
**Giải thích chi tiết:**
- Theo quy tắc của Set Operators, tiêu đề cột của tập kết quả cuối cùng được xác định bởi câu lệnh `SELECT` đầu tiên (`CODE`, `FULL_NAME`, `SAL`).
- Tên bí danh `DEPT_NAME` chỉ xuất hiện ở câu `SELECT` thứ hai, do đó hệ thống không nhận diện được định danh `DEPT_NAME` khi thực hiện `ORDER BY` ở cấp độ toàn cục. Muốn sắp xếp theo cột thứ hai, phải viết là `ORDER BY FULL_NAME` hoặc `ORDER BY 2`.
- `NULL` có thể tương thích với mọi kiểu dữ liệu nên đáp án C không chính xác.

---

### Câu 2 (Độ khó: Trung bình — Tính toán số dòng giữa UNION và UNION ALL)
Cho bảng `TAB_A` và `TAB_B` có cấu trúc và dữ liệu như sau:
- `TAB_A` (Cột `VAL` kiểu số): có 5 dòng với các giá trị: `10, 20, 20, 30, NULL`.
- `TAB_B` (Cột `VAL` kiểu số): có 4 dòng với các giá trị: `20, 30, 40, NULL`.

Xét hai câu truy vấn:
- Truy vấn 1: `SELECT VAL FROM TAB_A UNION SELECT VAL FROM TAB_B;`
- Truy vấn 2: `SELECT VAL FROM TAB_A UNION ALL SELECT VAL FROM TAB_B;`

Số lượng dòng kết quả trả về của Truy vấn 1 và Truy vấn 2 lần lượt là bao nhiêu?

A. Truy vấn 1: 5 dòng; Truy vấn 2: 9 dòng
B. Truy vấn 1: 4 dòng; Truy vấn 2: 7 dòng
C. Truy vấn 1: 5 dòng; Truy vấn 2: 7 dòng
D. Truy vấn 1: 6 dòng; Truy vấn 2: 9 dòng

**Đáp án đúng:** **A**
**Giải thích chi tiết:**
- **Với Truy vấn 1 (UNION):**
  - Gộp tất cả các giá trị lại: `10, 20, 20, 30, NULL` và `20, 30, 40, NULL`.
  - Tiến hành khử trùng lặp:
    - Giá trị `10` xuất hiện 1 lần.
    - Giá trị `20` xuất hiện ở cả hai bảng → chỉ lấy 1 lần.
    - Giá trị `30` xuất hiện ở cả hai bảng → chỉ lấy 1 lần.
    - Giá trị `40` xuất hiện 1 lần.
    - Giá trị `NULL` xuất hiện ở cả hai bảng → Set Operators coi các giá trị NULL bằng nhau và chỉ giữ lại **1 lần duy nhất**!
  - Tập kết quả duy nhất gồm: `{10, 20, 30, 40, NULL}` $\rightarrow$ **Đúng 5 dòng**.
- **Với Truy vấn 2 (UNION ALL):**
  - Không khử trùng lặp, chỉ việc nối thêm tất cả các dòng: $5 + 4 = $ **9 dòng**.

---

### Câu 3 (Độ khó: Khá — Cạm bẫy bất đối xứng của phép trừ MINUS / EXCEPT)
Cho hai tập dữ liệu kết quả:
- Tập hợp $X = \{1, 2, 2, 3\}$
- Tập hợp $Y = \{2, 3, 3, 4\}$

Xét biểu thức tập hợp sau trong Oracle Database:
```sql
SELECT VAL FROM TAB_X MINUS SELECT VAL FROM TAB_Y
```
và
```sql
SELECT VAL FROM TAB_Y MINUS SELECT VAL FROM TAB_X
```

Kết quả của hai câu lệnh trên lần lượt là gì?

A. Câu 1 trả về `{1}`; Câu 2 trả về `{4}`
B. Câu 1 trả về `{1, 2}`; Câu 2 trả về `{3, 4}`
C. Cả hai câu đều trả về `{1, 4}`
D. Câu 1 trả về `{1, 2, 2}`; Câu 2 trả về `{3, 3, 4}`

**Đáp án đúng:** **A**
**Giải thích chi tiết:**
- Toán tử `MINUS` (hoặc `EXCEPT`) luôn thực hiện thao tác khử trùng lặp trên cả hai tập hợp trước khi trừ.
- Tập $X$ sau khi khử trùng lặp: $\{1, 2, 3\}$.
- Tập $Y$ sau khi khử trùng lặp: $\{2, 3, 4\}$.
- `X MINUS Y`: Lấy phần tử thuộc $X$ mà không có trong $Y$: $\{1, 2, 3\} \setminus \{2, 3, 4\} = \{1\}$.
- `Y MINUS X`: Lấy phần tử thuộc $Y$ mà không có trong $X$: $\{2, 3, 4\} \setminus \{1, 2, 3\} = \{4\}$.
- Do đó Câu 1 trả về `{1}` và Câu 2 trả về `{4}`. Phép trừ tập hợp không có tính chất giao hoán.

---

### Câu 4 (Độ khó: Nâng cao — Phát biểu chuẩn mực về Set Operators)
Phát biểu nào sau đây là **CHÍNH XÁC NHẤT** khi nói về các toán tử tập hợp trong hệ quản trị CSDL quan hệ?

A. Trong mệnh đề `ORDER BY` ở cuối toàn bộ câu lệnh Set Operator, bắt buộc phải dùng tên cột nguyên bản của bảng dữ liệu, không được phép sử dụng số thứ tự của cột.
B. Toán tử `UNION ALL` thực hiện ghép nối dữ liệu mà không cần thông qua phân đoạn sắp xếp (Sort Operation), do đó luôn tiêu tốn ít tài nguyên bộ nhớ và có tốc độ xử lý nhanh hơn `UNION`.
C. Các câu lệnh `SELECT` thành phần trong phép toán tập hợp tuyệt đối không được chứa mệnh đề `WHERE` hoặc `GROUP BY`.
D. Khi sử dụng `INTERSECT`, nếu dòng dữ liệu chứa giá trị `NULL` ở cả hai bảng thì dòng đó sẽ bị loại bỏ hoàn toàn vì `NULL` không bao giờ bằng `NULL`.

**Đáp án đúng:** **B**
**Giải thích chi tiết:**
- **Đáp án B chính xác:** `UNION ALL` chỉ đơn giản nối tiếp các khối dữ liệu (cơ chế Append) mà không cần thực hiện `Sort Unique` hay `Hash Unique` trong bộ nhớ PGA/Temp, do đó tiết kiệm tài nguyên CPU, I/O và cho tốc độ vượt trội.
- **Đáp án A sai:** Trong `ORDER BY`, hoàn toàn được phép sử dụng số thứ tự cột (ví dụ `ORDER BY 1, 2`).
- **Đáp án C sai:** Từng câu lệnh `SELECT` thành phần hoàn toàn có thể tự do chứa các mệnh đề `WHERE`, `GROUP BY`, `HAVING` nội bộ.
- **Đáp án D sai:** Trong Set Operators, các giá trị `NULL` được đối xử như nhau (`NULL = NULL`), nên dòng có giá trị `NULL` ở cả hai bảng vẫn được giữ lại trong kết quả của `INTERSECT`.
