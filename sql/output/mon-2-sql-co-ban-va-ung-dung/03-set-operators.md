# Set Operators

B
D
```

Nó rất hữu ích cho bài toán:

> "Tìm những đối tượng **không có** quan hệ/dữ liệu tương ứng."

---

## 29. Một lỗi dễ ra thi: Composite Key trong correlated subquery

Ảnh cho bảng:

```sql
CREATE TABLE order_items (
    order_id   INT,
    product_id INT,
    quantity   INT,
    price      DECIMAL(10,2),
    PRIMARY KEY(order_id, product_id)
);
```

Primary Key gồm:

```text
(order_id, product_id)
```

Nếu correlated subquery muốn xác định đúng một `order_item`, phải liên kết đủ:

```sql
WHERE b.order_id = a.order_id
AND   b.product_id = a.product_id
```

Nếu chỉ:

```sql
WHERE b.order_id = a.order_id
```

thì một order có thể có nhiều product.

→ Không xác định đúng row.

#### 📌 Quy tắc
Phần này nối mạch SQL với “📌 Quy tắc”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
Khóa ghép gồm N cột
→ khi cần xác định chính xác row, thường phải xét đủ các cột cần thiết của khóa/quan hệ.
```

---

## 제2절 집합 연산자 — Set Operators

Bây giờ sang phần thứ hai trong ảnh.

Set Operator kết hợp **kết quả của các SELECT**, không phải JOIN column theo chiều ngang.

Có 4 loại chính:

```text
UNION
UNION ALL
INTERSECT
MINUS / EXCEPT
```

---

## 30. JOIN và Set Operator khác nhau như thế nào?

Đây là cách hiểu cực nhanh.

JOIN:

```text
Table A       Table B

A columns  +  B columns
      → ghép ngang →
```

Set Operator:

```text
SELECT result A
      ↓
SELECT result B
      ↓
ghép dọc
```

Ví dụ:

```text
R1

1
2
3

R2

3
4
5
```

Set operator xử lý hai tập này.

---

## 31. UNION

**UNION은 두 SELECT 결과를 합치고 중복을 제거한다.**
→ UNION hợp hai tập kết quả và **loại duplicate**.

```text
R1 = {1,2,3}
R2 = {3,4,5}
```

```sql
R1
UNION
R2
```

kết quả:

```text
1
2
3
4
5
```

`3` chỉ xuất hiện một lần.

Ví dụ ảnh:

```sql
SELECT 배우명, 본명
FROM sweethome1

UNION

SELECT 배우명, 본명
FROM sweethome2;
```

→ lấy diễn viên của season 1 và season 2, nhưng người trùng chỉ xuất hiện một lần.

---

## 32. UNION ALL

**UNION ALL은 중복을 제거하지 않고 모든 행을 반환한다.**
→ UNION ALL giữ nguyên duplicate.

```text
R1 = {1,2,3}
R2 = {3,4,5}
```

kết quả:

```text
1
2
3
3
4
5
```

#### UNION vs UNION ALL
Phần này nối mạch SQL với “UNION vs UNION ALL”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
UNION
→ duplicate 제거
→ cần xử lý loại trùng

UNION ALL
→ duplicate 유지
→ không cần loại trùng
```

Vì vậy khi **biết chắc không cần loại duplicate**, `UNION ALL` thường tránh được công việc deduplication không cần thiết.

---

## 33. INTERSECT — Giao tập hợp

**INTERSECT는 두 결과에 공통으로 존재하는 행만 반환한다.**
→ INTERSECT chỉ trả các row tồn tại trong **cả hai tập**.

```text
A = {1,2,3}
B = {2,3,4}
```

```text
A INTERSECT B

= {2,3}
```

Có thể nhớ:

```text
INTERSECT
= AND
= phần giao
```

Trong ảnh:

```sql
SELECT 배우명, 본명
FROM sweethome1

INTERSECT

SELECT 배우명, 본명
FROM sweethome2;
```

→ diễn viên xuất hiện ở **cả season 1 và season 2**.

---

## 34. MINUS / EXCEPT — Hiệu tập hợp

Trong Oracle:

```sql
MINUS
```

Trong một số DBMS khác:

```sql
EXCEPT
```

**차집합은 첫 번째 결과에는 존재하지만 두 번째 결과에는 존재하지 않는 행을 반환한다.**
→ Hiệu tập hợp trả row có trong tập đầu nhưng không có trong tập sau.

Ví dụ:

```text
A = {1,2,3}
B = {2,3,4}
```

thì:

```text
A MINUS B
= {1}
```

Nhưng:

```text
B MINUS A
= {4}
```

Do đó:

```text
A - B ≠ B - A
```

Đây là điểm rất hay thi.

#### Mẹo nhớ
Phần này nối mạch SQL với “Mẹo nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
MINUS
= lấy bên TRÊN
  trừ bên DƯỚI
```

---

## 35. Điều kiện sử dụng Set Operator

Ảnh yêu cầu nhớ:

**두 SELECT 문의 컬럼 수가 같아야 한다.**
→ Hai SELECT phải có **cùng số lượng column**.

Ví dụ hợp lệ:

```sql
SELECT id, name
FROM A

UNION

SELECT code, title
FROM B;
```

2 column ↔ 2 column.

---

**각 위치의 데이터 타입은 서로 호환 가능해야 한다.**
→ Data type của các column ở cùng vị trí phải tương thích.

Tức là:

```text
SELECT
   col1, col2
     ↕     ↕
   col1, col2
SELECT
```

Không phải so sánh theo tên.

Mà là:

```text
column 1 ↔ column 1
column 2 ↔ column 2
```

---

## 36. Tên column kết quả lấy từ SELECT đầu tiên

Ảnh nhấn mạnh:

**전체 집합의 컬럼명과 데이터 타입은 첫 번째 집합에 의해 결정된다.**
→ Tên cột hiển thị của kết quả set operation chủ yếu dựa vào SELECT đầu tiên; kiểu dữ liệu phải tương thích giữa các nhánh.

Ví dụ:

```sql
SELECT empno AS id,
       ename AS name
FROM emp

UNION

SELECT deptno,
       dname
FROM dept;
```

Tên output:

```text
ID
NAME
```

không phải:

```text
DEPTNO
DNAME
```

---

## 37. ORDER BY với Set Operator

Ảnh có câu rất quan trọng:

**개별 SELECT 문에는 ORDER BY를 사용할 수 없고 전체 집합 결과의 마지막에 사용한다.**
→ Trong dạng set query thông thường, `ORDER BY` được đặt ở **cuối toàn bộ phép tập hợp**, không đặt trực tiếp sau từng SELECT thành phần.

Sai dạng cơ bản:

```sql
SELECT ...
FROM A
ORDER BY ...

UNION

SELECT ...
FROM B
ORDER BY ...;
```

Đúng:

```sql
SELECT ...
FROM A

UNION

SELECT ...
FROM B

ORDER BY ...;
```

Tức là:

```text
SELECT A
   │
 UNION
   │
SELECT B
   │
ORDER BY
   ↓
sort FINAL RESULT
```

---

## 38. GROUP BY thì sao?

Ảnh ghi:

```text
ORDER BY ❌
GROUP BY ⭕
```

Ý nghĩa:

Mỗi SELECT thành phần vẫn có thể tự `GROUP BY`:

```sql
SELECT DEPTNO, COUNT(*)
FROM EMP
GROUP BY DEPTNO

UNION

SELECT DEPTNO, COUNT(*)
FROM OLD_EMP
GROUP BY DEPTNO;
```

Vì `GROUP BY` là logic nội bộ của từng SELECT.

Còn `ORDER BY` thường dùng để sắp xếp **kết quả cuối cùng**.

---

## 39. Tổng hợp toàn bộ Subquery bằng một sơ đồ
Phần này nối mạch SQL với “39. Tổng hợp toàn bộ Subquery bằng một sơ đồ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
                    SUBQUERY
                       │
        ┌──────────────┴──────────────┐
        │                             │
   Theo vị trí                    Theo kết quả
        │                             │
 ┌──────┼──────┐              ┌──────┼─────────┐
 │      │      │              │      │         │
SELECT FROM   WHERE         1 row  N rows   N columns
 │      │      │
Scalar Inline Nested
       View
```

Một cách phân loại khác:

```text
Theo phụ thuộc Main Query

Subquery
├── 비연관 / Uncorrelated
│      └── không dùng column main query
│
└── 연관 / Correlated
       └── dùng column main query
```

Hai hệ phân loại này **không loại trừ nhau**.

Ví dụ:

```sql
SELECT ...,
       (
          SELECT ...
          WHERE x.id = main.id
       )
FROM ...
```

có thể đồng thời là:

```text
Scalar Subquery
+
Correlated Subquery
```

Vì:

* `Scalar` mô tả **hình dạng/vị trí kết quả**.
* `Correlated` mô tả **quan hệ phụ thuộc với main query**.

Đây là chỗ rất nhiều người học nhầm.

---

## 40. 📌 NOTE 시험 — phần phải nhớ trước khi thi

#### ⭐ Subquery
Phần này nối mạch SQL với “⭐ Subquery”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
서브쿼리
= SQL 안의 SQL
= query nằm trong query
```

#### ⭐ Theo vị trí
Phần này nối mạch SQL với “⭐ Theo vị trí”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
SELECT → Scalar Subquery
FROM   → Inline View
WHERE/HAVING → Nested Subquery
```

#### ⭐ Scalar
Phần này nối mạch SQL với “⭐ Scalar”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
Scalar = ONE VALUE
```

Nếu không match:

```text
→ NULL
```

Nếu trả quá nhiều row khi ngữ cảnh yêu cầu một giá trị:

```text
→ ERROR
```

#### ⭐ Single-row
Phần này nối mạch SQL với “⭐ Single-row”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
=, <>, >, >=, <, <=
```

#### ⭐ Multi-row
Phần này nối mạch SQL với “⭐ Multi-row”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
IN
ANY
ALL
EXISTS
```

#### ⭐ ANY / ALL
Phần này nối mạch SQL với “⭐ ANY / ALL”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
> ANY → > MIN
< ANY → < MAX

> ALL → > MAX
< ALL → < MIN
```

#### ⭐ Correlated

Nhìn thấy kiểu:

```sql
Subquery:
WHERE E1.DEPTNO = E2.DEPTNO
```

trong đó `E1` thuộc outer/main query →
