# Subquery (서브쿼리 — Truy vấn con)

Trong kiến trúc truy vấn SQL và kỳ thi chứng chỉ SQLD, **Subquery (서브쿼리)** là một trong những chủ đề xuất hiện với tần suất dày đặc nhất và có nhiều dạng câu hỏi bẫy tư duy nhất.

> **Subquery = Một câu lệnh SQL nằm lồng bên trong một câu lệnh SQL khác.**

Để làm chủ Subquery trong bài thi SQLD, bạn cần nắm vững 3 trục phân loại:
1. **Theo vị trí xuất hiện:** Mệnh đề `SELECT` (Scalar Subquery), mệnh đề `FROM` (Inline View), mệnh đề `WHERE` / `HAVING` (Nested Subquery).
2. **Theo mối quan hệ với Main Query:** Non-correlated Subquery (비연관 서브쿼리 - Độc lập) vs Correlated Subquery (연관 서브쿼리 - Tương quan).
3. **Theo cấu trúc kết quả trả về:** Single-row (단일행), Multi-row (다중행), Multi-column (다중컬럼).

---

## 제1절 서브쿼리 개요 — Tổng quan về Subquery

### 1. 서브쿼리란 무엇인가? — Subquery là gì?

**서브쿼리(Subquery)는 하나의 SQL 문 안에 포함되어 있는 또 다른 SQL 문이다.**
→ **Subquery là một câu SQL nằm bên trong một câu SQL khác.**

Câu SQL bên ngoài gọi là:

* **메인쿼리 (Main Query)** = truy vấn chính.
* **서브쿼리 (Subquery)** = truy vấn con.

Ví dụ đúng như trong ảnh:

```sql
SELECT p.id,
       p.name,
       p.price,
       (SELECT a.name
          FROM artists a
         WHERE a.id = p.artist_id) AS artist_name
FROM paintings p;
```

Ta có cấu trúc:

```text
Main Query
│
├─ đọc từng dòng paintings p
│
└─ Subquery
      SELECT a.name
      FROM artists a
      WHERE a.id = p.artist_id
```

Ở đây:

```sql
p.artist_id
```

đến từ **main query**, còn:

```sql
a.id
```

đến từ **subquery**.

Đây là điểm cực kỳ quan trọng vì lát nữa nó dẫn đến khái niệm **상관 서브쿼리 (Correlated Subquery)**.

---

## 2. 서브쿼리 사용 시 주의사항 — Quy tắc khi dùng Subquery

### 2.1 괄호로 감싸서 사용한다

**서브쿼리는 반드시 괄호 `( )` 안에 작성한다.**
→ Subquery phải được đặt trong ngoặc.

```sql
SELECT *
FROM EMP
WHERE SAL > (
    SELECT AVG(SAL)
    FROM EMP
);
```

Không viết:

```sql
WHERE SAL > SELECT AVG(SAL) FROM EMP
```

---

### 2.2 단일행 연산자와 다중행 연산자를 구분한다

**단일행 서브쿼리에는 단일행 비교 연산자를 사용한다.**
→ Nếu subquery trả về tối đa **1 row**, có thể dùng toán tử so sánh thông thường.

```text
=
<>
>
>=
<
<=
```

Ví dụ:

```sql
WHERE SAL > (SELECT AVG(SAL) FROM EMP)
```

`AVG()` trả về một giá trị → OK.

Ngược lại:

**다중행 서브쿼리에는 다중행 비교 연산자를 사용해야 한다.**
→ Nếu subquery có thể trả về **nhiều row**, thường phải dùng:

```text
IN
ANY
ALL
EXISTS
```

Đây là lỗi SQLD rất hay kiểm tra.

---

## 3. 서브쿼리가 위치할 수 있는 곳 — Subquery có thể nằm ở đâu?

Theo ảnh:

**서브쿼리는 SELECT, FROM, WHERE, HAVING, ORDER BY 절 등에 위치할 수 있다.**
→ Subquery có thể xuất hiện trong `SELECT`, `FROM`, `WHERE`, `HAVING`, `ORDER BY`...

Ngoài ra còn có thể xuất hiện trong DML:

```sql
INSERT ... VALUES (...)
UPDATE ... SET ...
```

Nhưng trong SQLD, ba loại quan trọng nhất cần nhớ:

| Vị trí         | Tên thường gọi | Ý nghĩa         |
| -------------- | -------------- | --------------- |
| `SELECT`       | 스칼라 서브쿼리       | Scalar Subquery |
| `FROM`         | 인라인 뷰          | Inline View     |
| `WHERE/HAVING` | 중첩 서브쿼리        | Nested Subquery |

Hãy nhớ bằng một dòng:

```text
SELECT → Scalar
FROM   → Inline View
WHERE  → Nested
```

---

## 4. 연관 서브쿼리 vs 비연관 서브쿼리

Đây là một cách phân loại **theo quan hệ với main query**.

### 4.1 연관 서브쿼리 — Correlated Subquery

**연관 서브쿼리는 서브쿼리가 메인쿼리의 컬럼을 참조하는 서브쿼리이다.**
→ Correlated Subquery là subquery **tham chiếu cột của main query**.

Ví dụ:

```sql
SELECT p.id,
       p.name,
       (
         SELECT a.name
         FROM artists a
         WHERE a.id = p.artist_id
       ) AS artist_name
FROM paintings p;
```

Điểm quyết định nằm ở:

```sql
p.artist_id
```

Subquery đang sử dụng dữ liệu từ `p`, mà `p` được khai báo ở main query:

```sql
FROM paintings p
```

Do đó subquery **phụ thuộc main query**.

Ta có thể tư duy:

```text
Main query lấy painting 101
        ↓
p.artist_id = 1
        ↓
Subquery tìm artist_id = 1
        ↓
trả artist_name

Main query lấy painting 102
        ↓
p.artist_id = 1
        ↓
Subquery tìm artist_id = 1
        ↓
trả artist_name
...
```

> Đây là mô hình logic để hiểu correlated subquery; optimizer của DBMS có thể biến đổi cách thực thi thực tế.

---

### 4.2 비연관 서브쿼리 — Uncorrelated Subquery

**비연관 서브쿼리는 메인쿼리의 컬럼을 참조하지 않는다.**
→ Uncorrelated Subquery không phụ thuộc cột của main query.

Ví dụ:

```sql
SELECT *
FROM EMP
WHERE SAL > (
    SELECT AVG(SAL)
    FROM EMP
);
```

Subquery:

```sql
SELECT AVG(SAL)
FROM EMP
```

có thể tự chạy độc lập.

Ví dụ:

```text
AVG(SAL) = 3500
```

Sau đó về logic main query trở thành:

```sql
SELECT *
FROM EMP
WHERE SAL > 3500;
```

#### 📌 Điểm nhớ
Phần này nối mạch SQL với “📌 Điểm nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
Correlated
→ cần giá trị từ Main Query

Uncorrelated
→ tự chạy độc lập được
```

---

## 5. 반환 데이터에 따른 분류 — Phân loại theo dữ liệu trả về

Ảnh chia thành ba loại rất quan trọng:

```text
Subquery
├─ 단일행 서브쿼리
├─ 다중행 서브쿼리
└─ 다중컬럼 서브쿼리
```

---

## 6. 단일행 서브쿼리 — Single-row Subquery

**서브쿼리의 실행 결과가 1건 이하인 서브쿼리이다.**
→ Subquery trả về **tối đa một row**.

Ví dụ:

```sql
SELECT EMPNO, ENAME, SAL
FROM EMP
WHERE SAL > (
    SELECT AVG(SAL)
    FROM EMP
);
```

Giả sử:

```sql
SELECT AVG(SAL)
FROM EMP;
```

trả:

```text
3000
```

thì main query tương đương:

```sql
WHERE SAL > 3000
```

Có thể dùng:

```text
=
<>
>
>=
<
<=
```

---

## 7. 다중행 서브쿼리 — Multi-row Subquery

**서브쿼리의 실행 결과가 여러 행인 서브쿼리이다.**
→ Subquery trả về nhiều row.

Ví dụ:

```sql
SELECT TEAM_ID
FROM PLAYER;
```

có thể trả:

```text
K01
K02
K03
K04
```

Bạn không thể thông thường viết:

```sql
WHERE TEAM_ID = (
    SELECT TEAM_ID
    FROM PLAYER
)
```

vì bên phải `=` có nhiều row.

Thay vào đó dùng:

```text
IN
ANY
ALL
EXISTS
```

---

## 8. IN — Có nằm trong tập kết quả không?

**IN은 서브쿼리 결과 중 일치하는 값이 있는지 확인한다.**
→ `IN` kiểm tra giá trị có thuộc tập kết quả của subquery hay không.

```sql
WHERE TEAM_ID IN (
    SELECT TEAM_ID
    FROM ...
)
```

Nếu subquery trả:

```text
10
20
30
```

thì:

```sql
WHERE DEPTNO IN (10,20,30)
```

Hiểu đơn giản:

```text
10? → YES
20? → YES
30? → YES
40? → NO
```

---

## 9. ANY — Chỉ cần đúng với ít nhất một giá trị

**ANY는 서브쿼리 결과 중 하나라도 조건을 만족하면 TRUE이다.**
→ `ANY` chỉ cần so sánh đúng với **ít nhất một giá trị**.

Ví dụ:

```sql
WHERE SAL > ANY (1000, 2000, 3000)
```

Chỉ cần lớn hơn **một trong số chúng**.

Muốn thỏa mãn dễ nhất thì chỉ cần:

```text
SAL > 1000
```

Vì vậy:

```text
> ANY
→ > MIN
```

Tương tự:

```text
< ANY
→ < MAX
```

#### Mẹo nhớ
Phần này nối mạch SQL với “Mẹo nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
ANY = ít nhất MỘT đứa
```

---

## 10. ALL — Phải đúng với tất cả

**ALL은 서브쿼리의 모든 값에 대해 조건을 만족해야 한다.**
→ `ALL` yêu cầu điều kiện đúng với **mọi giá trị**.

Ví dụ:

```sql
SAL > ALL (1000, 2000, 3000)
```

Muốn lớn hơn tất cả thì phải:

```text
SAL > 3000
```

Do đó:

```text
> ALL
→ > MAX
```

Ngược lại:

```text
< ALL
→ < MIN
```

#### Bảng phải thuộc lòng
Phần này nối mạch SQL với “Bảng phải thuộc lòng”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

| Điều kiện | Tương đương trực giác |
| --------- | --------------------- |
| `> ANY`   | `> MIN`               |
| `< ANY`   | `< MAX`               |
| `> ALL`   | `> MAX`               |
| `< ALL`   | `< MIN`               |

Ví dụ ảnh:

```sql
SELECT EMPNO, ENAME, SAL
FROM EMP
WHERE SAL > ANY (
    SELECT SAL
    FROM EMP
    WHERE DEPTNO = 10
);
```

Nếu phòng 10 có:

```text
1000
2000
4000
```

thì:

```sql
> ANY
```

chỉ cần:

```text
> 1000
```

---

## 11. 다중컬럼 서브쿼리 — Multi-column Subquery

**KR:** 다중컬럼 서브쿼리는 서브쿼리가 비교하는 컬럼이 둘 이상인 서브쿼리이다.
**VI:** Multi-column subquery trả về **tổ hợp nhiều cột cùng lúc** để so sánh đồng thời với các cột ở Main query.

Ví dụ kinh điển:

```sql
SELECT EMPNO, ENAME, SAL, DEPTNO
FROM EMP
WHERE (DEPTNO, SAL) IN (
    SELECT DEPTNO, MAX(SAL)
    FROM EMP
    GROUP BY DEPTNO
);
```

Subquery trả về danh sách các cặp `(DEPTNO, MAX(SAL))`:

```text
DEPTNO | MAX(SAL)
-------+---------
10     | 5000
20     | 4000
30     | 3500
```

Main query kiểm tra theo **từng bộ giá trị (tuple matching)**:
- Nhân viên phòng 10 có lương 5000 → Khớp điều kiện → Giữ lại.
- Nhân viên phòng 10 có lương 3000 → Không khớp → Bỏ qua.
- Nhân viên phòng 20 có lương 4000 → Khớp điều kiện → Giữ lại.

Mục tiêu nghiệp vụ:
> "Tìm những nhân viên có mức lương cao nhất trong từng phòng ban của họ."

### ⚠️ Điểm khác biệt quan trọng giữa Oracle và SQL Server
- **Oracle Database:** Hỗ trợ đầy đủ cú pháp đa cột dạng tuple: `WHERE (col1, col2) IN (SELECT col1, col2 FROM ...)`.
- **Microsoft SQL Server:** **KHÔNG HỖ TRỢ** cú pháp đa cột `(col1, col2) IN (...)`. Trong SQL Server, nếu viết như vậy sẽ báo lỗi cú pháp. Để đạt được kết quả tương đương, trên SQL Server bắt buộc phải chuyển sang dùng `INNER JOIN` với Inline View hoặc dùng `EXISTS` với Correlated Subquery:
  ```sql
  -- Cú pháp thay thế trên SQL Server:
  SELECT e.EMPNO, e.ENAME, e.SAL, e.DEPTNO
  FROM EMP e
  INNER JOIN (
      SELECT DEPTNO, MAX(SAL) AS MAX_SAL
      FROM EMP
      GROUP BY DEPTNO
  ) m ON e.DEPTNO = m.DEPTNO AND e.SAL = m.MAX_SAL;
  ```

---

## 12. 스칼라 서브쿼리 — Scalar Subquery

**KR:** 스칼라 서브쿼리는 SELECT 절에 위치하여 마치 하나의 컬럼이나 표현식처럼 단일 값을 반환하는 서브쿼리이다.
**VI:** Scalar Subquery nằm trong mệnh đề `SELECT`, đóng vai trò như **một cột hoặc một giá trị đơn (scalar value)**.

Ví dụ:

```sql
SELECT p.id,
       p.name,
       p.price,
       (
           SELECT a.name
           FROM artists a
           WHERE a.id = p.artist_id
       ) AS artist_name
FROM paintings p;
```

---

## 13. Tại sao Scalar Subquery chỉ được trả về 1 giá trị? (Bẫy ORA-01427)

**KR:** 스칼라 서브쿼리는 하나의 행, 하나의 컬럼(1 Row 1 Column)만 반환해야 한다.
**VI:** Scalar Subquery chiếm vị trí của **đúng một ô (cell)** trên một dòng kết quả, do đó nó **bắt buộc phải trả về tối đa 1 dòng và đúng 1 cột**.

```text
id   | name       | price     | artist_name (1 CELL DUY NHẤT)
-----+------------+-----------+------------------------------
101  | 숲과 나    | 1100000   | [Giá trị đơn từ Subquery]
```

### 🚨 Hai kịch bản thực thi sống còn trong đề thi SQLD

1. **Trường hợp Subquery trả về 0 dòng (Không tìm thấy dòng nào thỏa mãn):**
   - **Hành vi:** Hệ thống **KHÔNG BÁO LỖI**, mà tự động điền giá trị `NULL` vào ô đó.
   - Hành vi này hoàn toàn tương đồng với cơ chế của `LEFT OUTER JOIN`.
2. **Trường hợp Subquery trả về từ 2 dòng trở lên:**
   - **Hành vi:** Hệ thống **LẬP TỨC PHÁT SINH LỖI THỜI GIAN CHẠY (Runtime Error)**!
   - Trong Oracle, lỗi này có mã hiệu kinh điển: `ORA-01427: single-row subquery returns more than one row`.
   - Trong SQL Server, lỗi tương đương: `Subquery returned more than 1 value. This is not permitted when the subquery follows =, !=, <, <=, >, >= or when the subquery is used as an expression.`

> **Quy tắc vàng thi cử:**
> Nếu đề thi cho một câu truy vấn có Scalar Subquery mà không có điều kiện lọc khóa chính/duy nhất (hoặc không dùng hàm gom nhóm như `MAX`, `MIN`), dẫn đến khả năng bảng con trả về nhiều hơn 1 dòng cho một bản ghi của bảng chính → **Kết quả là phát sinh Lỗi (Error), chứ không phải trả về dữ liệu!**

---

## 14. Scalar Subquery và LEFT OUTER JOIN

Ảnh chỉ ra một liên hệ rất đáng nhớ.

Scalar subquery:

```sql
SELECT p.id,
       p.name,
       p.price,
       (
         SELECT a.name
         FROM artists a
         WHERE a.id = p.artist_id
       ) AS artist_name
FROM paintings p;
```

có thể cho kết quả tương tự:

```sql
SELECT p.id,
       p.name,
       p.price,
       a.name
FROM paintings p
LEFT JOIN artists a
       ON p.artist_id = a.id;
```

Tại sao là `LEFT JOIN`?

Giả sử:

```text
paintings

id  artist_id
101 1
...
108 10
```

nhưng `artists` không có:

```text
id = 10
```

Scalar subquery:

```sql
SELECT a.name
FROM artists a
WHERE a.id = 10
```

không tìm thấy row.

Trong scalar context, kết quả biểu diễn thành:

```text
NULL
```

Do đó painting `108` vẫn tồn tại:

```text
108 | 여행 | 150000 | NULL
```

Điều này giống:

```sql
LEFT JOIN
```

vì LEFT JOIN vẫn giữ row bên trái.

⚠️ Nhưng không nên học thành quy tắc "`Scalar Subquery = LEFT JOIN` trong mọi trường hợp". Hai cách chỉ tương đương khi điều kiện và tính duy nhất của kết quả phù hợp.

---

## 15. Một ví dụ Scalar Subquery rất quan trọng

Ảnh có:

```sql
SELECT EMPNO,
       ENAME,
       DEPTNO,
       (
         SELECT DNAME
         FROM DEPT D
         WHERE D.DEPTNO = E.DEPTNO
       ) AS DNAME
FROM EMP E
WHERE DEPTNO = 10;
```

Ta đọc từng phần:

```sql
FROM EMP E
```

→ lấy nhân viên.

```sql
WHERE DEPTNO = 10
```

→ chỉ lấy nhân viên phòng 10.

Với từng nhân viên:

```sql
SELECT DNAME
FROM DEPT D
WHERE D.DEPTNO = E.DEPTNO
```

→ tìm tên department tương ứng.

Kết quả:

```text
EMPNO | ENAME | DEPTNO | DNAME
```

---

## 16. Scalar Subquery với SUM()

Ảnh có ví dụ:

```sql
SELECT EMPNO,
       ENAME,
       DEPTNO,
       SAL,
       (
          SELECT SUM(SAL)
          FROM EMP
       ) AS TOTAL_SAL
FROM EMP;
```

Giả sử:

```sql
SELECT SUM(SAL)
FROM EMP;
```

trả:

```text
50000
```

thì:

```text
EMPNO ENAME DEPTNO SAL  TOTAL_SAL
7369  SMITH 20     800   50000
7499  ALLEN 30     1600  50000
7521  WARD  30     1250  50000
...
```

`TOTAL_SAL` được lặp trên từng row.

Đây chính là lý do aggregate function rất hay được dùng với scalar subquery:

```text
SUM()
AVG()
MAX()
MIN()
COUNT()
```

vì chúng thường gom kết quả thành **một giá trị**.

---

## 17. 인라인 뷰 — Inline View

**인라인 뷰는 FROM 절에 작성하는 서브쿼리이다.**
→ Inline View là subquery nằm trong `FROM`.

Ví dụ:

```sql
SELECT ...
FROM (
    SELECT ...
    FROM ...
) p2;
```

Hãy tưởng tượng:

```text
Subquery
   ↓
tạo ra một bảng tạm logic
   ↓
Main Query sử dụng bảng đó
```

Ví dụ trong ảnh:

```sql
SELECT p.artist_id,
       p.name,
       p.price,
       p2.avg_price
FROM paintings p,
     (
       SELECT artist_id,
              AVG(price) AS avg_price
       FROM paintings
       GROUP BY artist_id
     ) p2
WHERE p.artist_id = p2.artist_id
  AND p.price > p2.avg_price;
```

Subquery:

```sql
SELECT artist_id,
       AVG(price) AS avg_price
FROM paintings
GROUP BY artist_id;
```

trước tiên tạo logic:

```text
artist_id | avg_price
----------+----------
1         | 1,225,000
2         | ...
3         | ...
5         | 650,000
```

Ta có thể tưởng tượng đây là bảng:

```text
p2
```

Sau đó:

```sql
p.artist_id = p2.artist_id
```

→ nối painting với average của artist đó.

Rồi:

```sql
p.price > p2.avg_price
```

→ chỉ lấy painting đắt hơn average của artist.

---

## 18. Tại sao Inline View được gọi là Dynamic View?

**인라인 뷰는 동적 뷰(Dynamic View)라고도 한다.**
→ Inline View còn được gọi là Dynamic View.

Vì kết quả:

```sql
(
 SELECT ...
)
```

được tạo ra trong lúc query chạy.

Nó **không phải table vật lý được lưu cố định trong database**.

Có thể hình dung:

```text
Physical table
     ↓
Subquery chạy
     ↓
Temporary logical result
     ↓
Main Query sử dụng
     ↓
kết thúc query
```

---

## 19. Inline View và JOIN — phần rất dễ nhầm

Ảnh viết phiên bản:

```sql
FROM paintings p,
     (
       SELECT ...
     ) p2
WHERE p.artist_id = p2.artist_id
```

Đây là kiểu join cũ.

Có thể viết rõ hơn bằng ANSI JOIN:

```sql
SELECT p.artist_id,
       p.name,
       p.price,
       p2.avg_price
FROM paintings p
INNER JOIN (
    SELECT artist_id,
           AVG(price) AS avg_price
    FROM paintings
    GROUP BY artist_id
) p2
ON p.artist_id = p2.artist_id
WHERE p.price > p2.avg_price;
```

Hai phần cần phân biệt:

```sql
ON p.artist_id = p2.artist_id
```

→ điều kiện JOIN.

```sql
WHERE p.price > p2.avg_price
```

→ điều kiện lọc.

Đây cũng là cách viết dễ đọc hơn.

---

## 20. Cartesian Product khi quên JOIN condition

Ảnh nhấn mạnh:

**두 테이블 사이에 명확한 JOIN 조건이 없으면 Cartesian Product가 발생할 수 있다.**
→ Nếu kết hợp hai bảng mà không có điều kiện nối thích hợp, có thể sinh Cartesian Product.

Ví dụ:

```text
paintings = 7 rows
p2        = 5 rows
```

Nếu ghép mọi row với mọi row:

```text
7 × 5 = 35 rows
```

Đó chính là:

```text
Cartesian Product
= Cross Join
```

---

## 21. Scalar Subquery vs Inline View

Đây là phần ảnh so sánh trực tiếp.

#### Scalar
Phần này nối mạch SQL với “Scalar”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
SELECT p.id,
       p.name,
       p.price,
       (
         SELECT a.name
         FROM artists a
         WHERE a.id = p.artist_id
       ) artist_name
FROM paintings p;
```

Subquery trả:

```text
1 value
```

và trở thành:

```text
1 column/cell
```

#### Inline View
Phần này nối mạch SQL với “Inline View”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
SELECT p.artist_id,
       p.name,
       p.price,
       p2.avg_price
FROM paintings p,
     (
       SELECT artist_id,
              AVG(price) avg_price
       FROM paintings
       GROUP BY artist_id
     ) p2
WHERE ...
```

Subquery trả về:

```text
table-like result
```

gồm nhiều:

```text
rows × columns
```

#### Cách nhớ
Phần này nối mạch SQL với “Cách nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
Scalar Subquery
→ tạo VALUE

Inline View
→ tạo TABLE
```

---

## 22. 중첩 서브쿼리 — Nested Subquery

**중첩 서브쿼리는 WHERE 또는 HAVING 같은 조건절에서 사용되는 서브쿼리이다.**
→ Nested Subquery là subquery thường nằm trong điều kiện như `WHERE`, `HAVING`.

Ví dụ:

```sql
SELECT EMPNO, ENAME, SAL
FROM EMP
WHERE SAL > (
    SELECT AVG(SAL)
    FROM EMP
);
```

Subquery:

```sql
SELECT AVG(SAL)
FROM EMP
```

trả một giá trị.

Main query:

```sql
SAL > giá_trị_đó
```

---

## 23. 상호연관 서브쿼리 — Correlated Subquery sâu hơn

Ảnh có ví dụ tìm:

> Nhân viên nhận lương cao hơn mức lương trung bình của **chính department của mình**.

```sql
SELECT EMPNO,
       ENAME,
       SAL,
       DEPTNO
FROM EMP E1
WHERE SAL > (
    SELECT AVG(SAL)
    FROM EMP E2
    WHERE E1.DEPTNO = E2.DEPTNO
);
```

Đây là ví dụ cực kỳ quan trọng.

Giả sử đang xét:

```text
KING
DEPTNO = 10
SAL = 5000
```

Subquery trở thành về mặt logic:

```sql
SELECT AVG(SAL)
FROM EMP E2
WHERE 10 = E2.DEPTNO;
```

→ tính average phòng 10.

Sau đó:

```text
5000 > AVG(phòng 10)?
```

Nếu đúng → KING được chọn.

Tiếp theo main query xét nhân viên phòng 20.

Subquery lúc đó tính:

```text
AVG(phòng 20)
```

Vì thế correlated subquery phụ thuộc **row hiện tại của main query**.

---

## 24. 상호 연관 서브쿼리의 논리적 순서

Ảnh mô tả logic:

```text
① Main Query table READ
        ↓
② Main Query WHERE 확인
        ↓
③ Subquery table READ
        ↓
④ Subquery WHERE 확인
        ↓
⑤ So sánh column Main ↔ Subquery
        ↓
⑥ tính AVG(...)
        ↓
⑦ trả kết quả về Main Query
```

Ví dụ:

```sql
WHERE E1.DEPTNO = E2.DEPTNO
```

`E1.DEPTNO` được truyền từ row đang xét của main query.

---

## 25. HAVING절에서 서브쿼리

**HAVING 절에서도 서브쿼리를 사용할 수 있다.**
→ Có thể sử dụng subquery trong `HAVING`.

Nhớ lại:

```text
WHERE
→ lọc ROW trước GROUP BY

HAVING
→ lọc GROUP sau GROUP BY
```

Do đó nếu điều kiện liên quan kết quả aggregate:

```sql
GROUP BY ...
HAVING AVG(SAL) > (...)
```

thì subquery có thể xuất hiện ở `HAVING`.

---

## 26. UPDATE SET에서 서브쿼리

Ảnh nhắc một lỗi quan trọng.

Ví dụ:

```sql
UPDATE EMP
SET DEPTNO = (
    SELECT DEPTNO
    FROM ...
    WHERE ...
);
```

Nếu subquery không tìm được row thì scalar result có thể trở thành:

```text
NULL
```

Khi đó:

```text
DEPTNO = NULL
```

có thể xảy ra.

Do đó phải đặc biệt cẩn thận khi dùng subquery trong:

```sql
UPDATE ... SET
```

---

## 27. EXISTS

**EXISTS는 서브쿼리 결과가 존재하는지를 확인한다.**
→ `EXISTS` chỉ kiểm tra **có row tồn tại hay không**.

```sql
WHERE EXISTS (
    SELECT 1
    FROM ...
    WHERE ...
)
```

Ta không quan tâm subquery trả giá trị gì.

Chỉ quan tâm:

```text
Có ít nhất 1 row?
```

Nếu:

```text
YES → TRUE
NO  → FALSE
```

Vì vậy thường thấy:

```sql
SELECT 1
```

trong EXISTS.

Không phải vì số `1` có ý nghĩa đặc biệt; ý nghĩa là:

> Tôi chỉ quan tâm row có tồn tại hay không.

---

## 28. NOT EXISTS

**NOT EXISTS는 서브쿼리에 해당하는 행이 존재하지 않을 때 TRUE이다.**
→ `NOT EXISTS` trả TRUE nếu không tồn tại row phù hợp.

Ví dụ tư duy:

```text
Main table
A
B
C
D
```

Subquery match:

```text
A
C
```

thì:

```sql
EXISTS
```

giữ:

```text
A
C
```

còn:

```sql
NOT EXISTS
```

giữ:

```text
B
D
```

Toán tử `NOT EXISTS` cực kỳ hữu ích cho bài toán nghiệp vụ kinh điển:
> "Tìm những thực thể ở bảng A **hoàn toàn không có** bất kỳ dữ liệu phát sinh nào ở bảng B" (ví dụ: Tìm khách hàng chưa từng phát sinh đơn hàng, tìm sinh viên chưa đăng ký môn học nào).

---

## 29. Khóa ngoại ghép (Composite Key) trong Correlated Subquery

Khi một bảng sử dụng khóa chính gồm nhiều cột (Composite Primary Key), correlated subquery bắt buộc phải liên kết **đầy đủ tất cả các cột thành phần của khóa**.

Ví dụ bảng chi tiết đơn hàng:

```sql
CREATE TABLE order_items (
    order_id   INT,
    product_id INT,
    quantity   INT,
    price      DECIMAL(10,2),
    PRIMARY KEY(order_id, product_id)
);
```

Khóa chính là cặp `(order_id, product_id)`. Nếu correlated subquery muốn kiểm tra trạng thái của đúng một dòng chi tiết đơn hàng:

```sql
-- ✅ ĐÚNG: Liên kết đủ cả 2 cột khóa
WHERE b.order_id = a.order_id
  AND b.product_id = a.product_id

-- ❌ SAI: Chỉ liên kết 1 cột khóa
WHERE b.order_id = a.order_id
```

Nếu chỉ nối theo `order_id`, một đơn hàng có thể chứa nhiều sản phẩm khác nhau, subquery sẽ trả về nhiều dòng ngoài dự kiến và gây sai lệch toàn bộ logic tính toán.

> **Quy tắc thi cử:**
> Khi kiểm tra liên kết bảng có khóa ghép N cột, điều kiện tương quan trong Subquery bắt buộc phải xuất hiện đủ N cột liên kết.

---

## 30. Cạm bẫy kinh điển số 1 của Subquery: NOT IN chứa NULL vs NOT EXISTS

Đây là **câu hỏi phân loại học sinh giỏi** có tần suất xuất hiện cực cao trong kỳ thi SQLD.

### Bản chất toán học của NOT IN

Xét hai bảng:
- Bảng `EMP` có các nhân viên thuộc phòng ban `DEPTNO = 10, 20, 30`.
- Bảng `DEPT` có danh sách `DEPTNO` gồm: `10, 20, NULL`.

Nếu thực hiện truy vấn:

```sql
SELECT EMPNO, ENAME, DEPTNO
FROM EMP
WHERE DEPTNO NOT IN (
    SELECT DEPTNO
    FROM DEPT
);
```

#### Quá trình biên dịch logic 3 giá trị (Three-Valued Logic):
Biểu thức `DEPTNO NOT IN (10, 20, NULL)` được hệ quản trị CSDL mở rộng thành phép toán logic `AND` liên tiếp:

```sql
WHERE (DEPTNO <> 10) AND (DEPTNO <> 20) AND (DEPTNO <> NULL)
```

Theo quy tắc toán tử so sánh với `NULL` trong SQL:
- Bất kỳ phép so sánh nào với `NULL` (`= NULL`, `<> NULL`, `> NULL`) đều **luôn trả về giá trị logic UNKNOWN**.
- Bảng chân trị phép `AND` với `UNKNOWN`:
  - `TRUE AND UNKNOWN` → `UNKNOWN`
  - `FALSE AND UNKNOWN` → `FALSE`
- Thử kiểm tra từng giá trị `DEPTNO`:
  - Với nhân viên có `DEPTNO = 10`: `(10 <> 10) AND ...` = `FALSE AND ...` → **FALSE**.
  - Với nhân viên có `DEPTNO = 30`: `(30 <> 10) AND (30 <> 20) AND (30 <> NULL)` = `TRUE AND TRUE AND UNKNOWN` → **UNKNOWN**.

Mệnh đề `WHERE` chỉ chấp nhận và trả về những dòng có kết quả đánh giá là **TRUE**. Kết quả `UNKNOWN` không thỏa mãn!

> 🚨 **HỆ QUẢ KINH HOÀNG:**
> Khi danh sách kết quả của Subquery bên trong toán tử `NOT IN` **chứa dù chỉ một giá trị NULL**, toàn bộ câu truy vấn chính sẽ **KHÔNG TRẢ VỀ BẤT KỲ DÒNG NÀO (0 rows)**!

### Tại sao NOT EXISTS lại an toàn tuyệt đối trước giá trị NULL?

Xét câu truy vấn tương đương sử dụng `NOT EXISTS`:

```sql
SELECT E.EMPNO, E.ENAME, E.DEPTNO
FROM EMP E
WHERE NOT EXISTS (
    SELECT 1
    FROM DEPT D
    WHERE D.DEPTNO = E.DEPTNO
);
```

Cơ chế hoạt động của `EXISTS / NOT EXISTS`:
1. `EXISTS` chỉ kiểm tra **sự tồn tại của dòng (Row Count > 0)**, nó không quan tâm giá trị cột trả về là gì.
2. Khi xét nhân viên có `DEPTNO = 30`:
   - So sánh `D.DEPTNO = 30` trên bảng `DEPT`:
     - Dòng có `DEPTNO = 10` → `FALSE`.
     - Dòng có `DEPTNO = 20` → `FALSE`.
     - Dòng có `DEPTNO = NULL` → `NULL = 30` → `UNKNOWN`.
   - Vì không có dòng nào đánh giá là `TRUE`, subquery trả về **0 dòng**.
3. Vì subquery trả về 0 dòng, điều kiện `NOT EXISTS` đánh giá thành **TRUE**!
4. Nhân viên có `DEPTNO = 30` được đưa vào kết quả một cách chính xác!

| Tiêu chí | `NOT IN` | `NOT EXISTS` |
| :--- | :--- | :--- |
| **Gặp NULL trong tập Subquery** | Toàn bộ câu truy vấn trả về **RỖNG (0 dòng)** | **Hoạt động chính xác**, bỏ qua NULL |
| **Bản chất kiểm tra** | So sánh từng giá trị (`<> ALL`) | Kiểm tra số lượng dòng tồn tại |
| **Khuyên dùng trong dự án & đề thi** | Nguy hiểm nếu cột có thể chứa NULL | An toàn, tối ưu hiệu năng tốt |

---

## 31. Sơ đồ tổng hợp toàn bộ cấu trúc Subquery

```text
                                SUBQUERY (서브쿼리)
                                        │
        ┌───────────────────────────────┼───────────────────────────────┐
        │                               │                               │
  Theo Vị trí                      Theo Kết quả                    Theo Tương quan
  (구문 위치)                       (반환 데이터 형태)               (상관 관계)
        │                               │                               │
  ┌─────┼─────┐                   ┌─────┼─────┐                   ┌─────┴─────┐
  │     │     │                   │     │     │                   │           │
SELECT FROM WHERE/HAVING        1 dòng Nhiều Nhiều              Không phụ  Phụ thuộc
  │     │     │                 (단일행) dòng  cột               thuộc Outer Outer row
  │     │     │                   │   (다중행) (다중컬럼)         (비연관)    (연관)
Scalar Inline Nested              │     │       │                 │           │
Sub-   View   Subquery            │     │       │                 Độc lập     Chạy lại
query                             │     │       │                 1 lần duy   theo từng
                                  │     │       └─ (col1,col2)IN  nhất        dòng của
                                  │     │          (Oracle OK,                Main query
                                  │     │          SQL Server NO)
                                  │     │
                                  │     └─ IN, ANY/SOME, ALL, EXISTS
                                  │
                                  └─ =, <>, >, >=, <, <=
```

---

## 32. Bảng ma trận so sánh Subquery giữa Oracle và SQL Server

| Tính năng Subquery | Oracle Database | Microsoft SQL Server |
| :--- | :--- | :--- |
| **Scalar Subquery trong SELECT** | Hỗ trợ đầy đủ; trả > 1 dòng báo lỗi `ORA-01427` | Hỗ trợ đầy đủ; trả > 1 dòng báo lỗi Runtime |
| **Inline View trong FROM** | Bắt buộc hoặc tùy chọn Alias | **BẮT BUỘC** phải đặt Alias cho Inline View |
| **Multi-Column Subquery `(A, B) IN`** | **HỖ TRỢ ĐẦY ĐỦ** cú pháp tuple | **KHÔNG HỖ TRỢ** (phải viết bằng JOIN/EXISTS) |
| **Correlated Subquery trong UPDATE** | Hỗ trợ trong mệnh đề `SET` | Hỗ trợ trong `SET` hoặc cú pháp `UPDATE ... FROM` |
| **NOT IN có chứa NULL** | Đều trả về 0 dòng (Chuẩn ANSI SQL) | Đều trả về 0 dòng (Chuẩn ANSI SQL) |
| **Toán tử EXISTS / NOT EXISTS** | Tối ưu hóa Semi-join / Anti-join tự động | Tối ưu hóa Semi-join / Anti-join tự động |

---

## 33. Cạm bẫy thi cử trọng điểm (출제 함정 & 오답 노트)

1. **Bẫy Scalar Subquery trả về nhiều dòng (`ORA-01427`):**
   - Scalar Subquery chỉ được phép trả về duy nhất 1 ô dữ liệu (1 hàng, 1 cột).
   - Nếu trả về 0 hàng → Trả về `NULL` (không lỗi).
   - Nếu trả về $\ge 2$ hàng → LẬP TỨC BÁO LỖI RUNTIME.
2. **Bẫy `NOT IN` chứa giá trị `NULL`:**
   - Trong Subquery, nếu danh sách con chứa giá trị `NULL`, toán tử `NOT IN` sẽ khiến câu query chính không trả về bất kỳ dòng nào.
   - Giải pháp: dùng `WHERE col IS NOT NULL` trong subquery hoặc thay thế bằng `NOT EXISTS`.
3. **Bẫy dùng toán tử đơn dòng cho Subquery đa dòng:**
   - Nếu subquery có khả năng trả về nhiều hơn 1 dòng mà dùng toán tử so sánh đơn (`=`, `>`, `<`) → Báo lỗi runtime. Bắt buộc phải dùng toán tử đa dòng (`IN`, `ANY`, `ALL`, `EXISTS`).
4. **Bẫy mệnh đề ORDER BY trong Subquery:**
   - Theo chuẩn SQL truyền thống, mệnh đề `ORDER BY` không được phép xuất hiện trong Subquery của mệnh đề `WHERE` hoặc Scalar Subquery (chỉ được dùng trong Inline View khi phục vụ phân trang Top-N hoặc ROWNUM).
5. **Bẫy Alias của Inline View trong SQL Server:**
   - Trong SQL Server, mọi Inline View trong mệnh đề `FROM` bắt buộc phải có Alias (`FROM (SELECT ...) AS T`). Nếu thiếu alias sẽ bị lỗi cú pháp.

---

## 34. Câu hỏi trắc nghiệm thi thử mô phỏng (실전 기출 변형 문제 & 정답 해설)

### Câu 1 (Độ khó: Trung bình — Bẫy giá trị NULL trong NOT IN)
Cho bảng `DEPARTMENT` gồm 3 dòng dữ liệu:
- Dòng 1: `DEPTNO = 10`
- Dòng 2: `DEPTNO = 20`
- Dòng 3: `DEPTNO = NULL`

Và bảng `EMPLOYEE` gồm 5 nhân viên có `DEPTNO` lần lượt là `10, 20, 30, 40, NULL`.
Xét câu lệnh SQL sau:

```sql
SELECT COUNT(*) AS CNT
FROM EMPLOYEE
WHERE DEPTNO NOT IN (
    SELECT DEPTNO
    FROM DEPARTMENT
);
```

Kết quả hiển thị của cột `CNT` là bao nhiêu?

A. 0
B. 2
C. 3
D. Báo lỗi cú pháp do không thể chứa NULL trong tập hợp IN

**Đáp án đúng:** **A**
**Giải thích chi tiết:**
- Tập hợp do Subquery trả về là `{10, 20, NULL}`.
- Mệnh đề lọc trở thành: `WHERE DEPTNO <> 10 AND DEPTNO <> 20 AND DEPTNO <> NULL`.
- Vì phép so sánh bất kỳ với `NULL` (`DEPTNO <> NULL`) luôn trả về giá trị chân lý `UNKNOWN`, và phép toán logic `AND` có chứa `UNKNOWN` không bao giờ cho kết quả `TRUE`.
- Do không có dòng nào trong bảng `EMPLOYEE` thỏa mãn điều kiện `WHERE` để được chọn, số lượng dòng thỏa mãn là 0. Hàm `COUNT(*)` đếm số dòng thỏa mãn sẽ trả về kết quả là `0`.

---

### Câu 2 (Độ khó: Khá — Cạm bẫy Scalar Subquery ORA-01427)
Xét lược đồ dữ liệu gồm bảng `CUSTOMER` (Khách hàng) và `ORDERS` (Đơn hàng). Mỗi khách hàng có thể có 0, 1 hoặc nhiều đơn hàng. Câu lệnh SQL nào dưới đây có nguy cơ **phát sinh lỗi thời gian chạy (Runtime Error: ORA-01427)** cao nhất?

A.
```sql
SELECT C.CUST_ID,
       (SELECT COUNT(*) FROM ORDERS O WHERE O.CUST_ID = C.CUST_ID) AS ORDER_COUNT
FROM CUSTOMER C;
```
B.
```sql
SELECT C.CUST_ID,
       (SELECT MAX(O.ORDER_DATE) FROM ORDERS O WHERE O.CUST_ID = C.CUST_ID) AS LAST_ORDER
FROM CUSTOMER C;
```
C.
```sql
SELECT C.CUST_ID,
       (SELECT O.ORDER_ID FROM ORDERS O WHERE O.CUST_ID = C.CUST_ID) AS ORDER_ID
FROM CUSTOMER C;
```
D.
```sql
SELECT C.CUST_ID
FROM CUSTOMER C
WHERE EXISTS (SELECT 1 FROM ORDERS O WHERE O.CUST_ID = C.CUST_ID);
```

**Đáp án đúng:** **C**
**Giải thích chi tiết:**
- **Đáp án C là câu lệnh gây lỗi:** Ở đây `(SELECT O.ORDER_ID FROM ORDERS O WHERE O.CUST_ID = C.CUST_ID)` là một Scalar Subquery trong mệnh đề `SELECT`. Vì một khách hàng có thể có nhiều đơn hàng (`1 : N`), câu lệnh subquery này sẽ trả về $\ge 2$ dòng đối với khách hàng có từ 2 đơn hàng trở lên. Khi đó hệ quản trị CSDL Oracle sẽ ngay lập tức ngắt truy vấn và báo lỗi `ORA-01427: single-row subquery returns more than one row`.
- **Đáp án A an toàn:** `COUNT(*)` là hàm tập hợp luôn trả về đúng 1 giá trị số nguyên (0 hoặc số lượng đơn).
- **Đáp án B an toàn:** `MAX(ORDER_DATE)` là hàm tập hợp luôn trả về đúng 1 giá trị ngày lớn nhất (hoặc NULL nếu khách hàng không có đơn hàng nào).
- **Đáp án D an toàn:** Mệnh đề `EXISTS` trong `WHERE` chấp nhận subquery trả về bao nhiêu dòng cũng được, chỉ kiểm tra sự tồn tại.

---

### Câu 3 (Độ khó: Khá — Phân tích toán tử đa dòng ANY và ALL)
Cho bảng `SALARY_TBL` có các mức lương: `1000, 2000, 3000`. Câu lệnh SQL nào dưới đây sẽ trả về kết quả tương đương với điều kiện `WHERE SAL > 3000`?

A. `WHERE SAL > ANY (SELECT SAL FROM SALARY_TBL)`
B. `WHERE SAL > ALL (SELECT SAL FROM SALARY_TBL)`
C. `WHERE SAL >= ALL (SELECT SAL FROM SALARY_TBL)`
D. `WHERE SAL = ANY (SELECT SAL FROM SALARY_TBL)`

**Đáp án đúng:** **B**
**Giải thích chi tiết:**
- `> ALL (tập hợp)` có nghĩa là phải **lớn hơn tất cả** các giá trị trong tập hợp, tương đương với việc phải **lớn hơn giá trị lớn nhất (MAX)** của tập hợp đó: `> MAX(1000, 2000, 3000) = > 3000`. Do đó đáp án B hoàn toàn chính xác.
- **Đáp án A:** `> ANY (tập hợp)` có nghĩa là chỉ cần lớn hơn ít nhất một giá trị, tương đương `> MIN(1000, 2000, 3000) = > 1000`.
- **Đáp án C:** `>= ALL (tập hợp)` tương đương `>= 3000` (giữ lại cả giá trị 3000).
- **Đáp án D:** `= ANY (tập hợp)` chính là toán tử `IN (1000, 2000, 3000)`.

---

### Câu 4 (Độ khó: Nâng cao — Đa cột Subquery và tính tương thích DBMS)
Phát biểu nào sau đây là **SAI** khi nói về Subquery trong SQL?

A. Subquery trong mệnh đề `HAVING` được sử dụng để so sánh kết quả gom nhóm với một giá trị tính toán từ một tập hợp dữ liệu khác.
B. Trong Oracle, câu lệnh `WHERE (DEPTNO, JOB) IN (SELECT DEPTNO, JOB FROM EMP_BACKUP)` là cú pháp hợp lệ, nhưng cú pháp so sánh đa cột dạng tuple này không được Microsoft SQL Server hỗ trợ trực tiếp.
C. Khi Scalar Subquery không tìm thấy bất kỳ dòng nào thỏa mãn điều kiện, toàn bộ câu truy vấn chính sẽ phát sinh lỗi `ORA-01403: no data found`.
D. Mệnh đề `ORDER BY` trong Inline View (mệnh đề `FROM`) là hoàn toàn hợp lệ và thường xuyên được sử dụng để phục vụ các truy vấn Top-N và phân trang.

**Đáp án đúng:** **C**
**Giải thích chi tiết:**
- **Phát biểu C là SAI:** Khi Scalar Subquery trả về 0 dòng dữ liệu, hệ thống không báo lỗi mà tự động gán giá trị `NULL` cho ô kết quả đó (hoạt động tương tự cơ chế LEFT OUTER JOIN). Lỗi `ORA-01427` chỉ phát sinh khi subquery trả về nhiều hơn 1 dòng dữ liệu.
- Các phát biểu A, B, D đều hoàn toàn chính xác theo chuẩn lý thuyết và thực tiễn của kỳ thi SQLD.
