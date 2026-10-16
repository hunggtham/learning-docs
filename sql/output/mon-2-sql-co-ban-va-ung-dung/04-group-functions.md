# Group Functions

```text
상관/연관 서브쿼리
Correlated Subquery
```

#### ⭐ Inline View
Phần này nối mạch SQL với “⭐ Inline View”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
FROM (
    SELECT ...
)
```

→ hãy tưởng tượng subquery **tạo ra một table tạm logic**.

#### ⭐ EXISTS
Phần này nối mạch SQL với “⭐ EXISTS”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
EXISTS
→ Có ít nhất 1 row?

NOT EXISTS
→ Không có row nào?
```

#### ⭐ Set Operators
Phần này nối mạch SQL với “⭐ Set Operators”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
UNION
= A + B
= remove duplicates

UNION ALL
= A + B
= keep duplicates

INTERSECT
= A ∩ B

MINUS
= A - B
```

#### ⭐ Cạm bẫy cực hay thi
Phần này nối mạch SQL với “⭐ Cạm bẫy cực hay thi”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
UNION     ≠ UNION ALL
ANY       ≠ ALL
IN        ≠ EXISTS về cơ chế/ý nghĩa
A MINUS B ≠ B MINUS A

Scalar Subquery ≠ Inline View
Correlated ≠ Uncorrelated
```

Và đặc biệt:

```text
Scalar / Inline / Nested
```

là cách nhìn chủ yếu theo **vị trí/cách sử dụng**;

trong khi:

```text
Correlated / Uncorrelated
```

là cách nhìn theo **mức độ phụ thuộc vào main query**.

Hai khái niệm này có thể **chồng lên nhau**, không phải hai nhóm đối lập.

Tiếp tục theo đúng format học SQLD trước đó: **bám sát nội dung trong ảnh → mỗi ý tiếng Hàn đi kèm giải thích tiếng Việt → giải thích keyword → sau đó mở rộng phần dễ nhầm và trọng tâm thi.**

## 제3절 그룹 함수 — Group Function

### 1. Ba nhóm hàm phân tích dữ liệu trong SQL

**KR:** ANSI/ISO SQL 표준에서는 데이터 분석을 위한 함수를 크게 `Aggregate Function`, `Group Function`, `Window Function`으로 구분한다.
**VI:** Trong chuẩn ANSI/ISO SQL, các hàm dùng để phân tích dữ liệu có thể chia thành 3 nhóm lớn: **hàm tổng hợp, hàm nhóm nâng cao và hàm cửa sổ**.

| Loại               | Korean | Ý nghĩa                                                               |
| ------------------ | ------ | --------------------------------------------------------------------- |
| Aggregate Function | 집계 함수  | Tổng hợp nhiều row thành một giá trị: `COUNT`, `SUM`, `AVG`, `MAX`... |
| Group Function     | 그룹 함수  | Tạo nhiều cấp độ nhóm/tổng phụ: `ROLLUP`, `CUBE`, `GROUPING SETS`     |
| Window Function    | 윈도우 함수 | Tính toán trên một "cửa sổ" row nhưng **không gom mất row**           |

Ví dụ quan trọng:

```sql
SELECT DEPTNO, SUM(SAL)
FROM EMP
GROUP BY DEPTNO;
```

10 nhân viên có thể bị gom thành chỉ 3 dòng phòng ban.

Trong khi Window Function:

```sql
SELECT EMPNO,
       DEPTNO,
       SAL,
       SUM(SAL) OVER (PARTITION BY DEPTNO)
FROM EMP;
```

vẫn giữ từng nhân viên.

---

## 2. 집계 함수 — Aggregate Function

Điểm quan trọng nhất của phần này:

> **집계 함수는 일반적으로 NULL을 제외한다.**
> Các Aggregate Function **thường bỏ qua NULL**.

Đây là kiến thức rất dễ xuất hiện trong SQLD.

---

### 2.1 COUNT

**KR:** `COUNT`는 행의 수를 계산하는 함수이다.
**VI:** `COUNT` là hàm dùng để **đếm số dòng/số giá trị**.

Nhưng phải phân biệt:

```sql
COUNT(*)
COUNT(SAL)
COUNT(EMPNO)
```

#### `COUNT(*)`

**KR:** `COUNT(*)`는 NULL 여부와 관계없이 행 자체의 개수를 센다.
**VI:** `COUNT(*)` đếm **row**, không quan tâm các column bên trong có NULL hay không.

Ví dụ:

| EMPNO |  SAL |
| ----: | ---: |
|     1 | 1000 |
|     2 | NULL |
|     3 | 2000 |

```sql
COUNT(*)
```

→ `3`

---

#### `COUNT(SAL)`

**KR:** `COUNT(컬럼)`은 해당 컬럼에서 NULL이 아닌 값만 계산한다.
**VI:** `COUNT(column)` chỉ đếm những row mà column đó **không phải NULL**.

```sql
COUNT(SAL)
```

→ `2`

Do SAL của nhân viên 2 là NULL.

#### Mẹo SQLD

Nếu muốn đếm chắc chắn toàn bộ row:

```sql
COUNT(*)
```

hoặc có thể dùng column chắc chắn `NOT NULL`, ví dụ PK:

```sql
COUNT(EMPNO)
```

vì PK không thể NULL.

---

## 3. SUM

**KR:** `SUM`은 숫자 데이터의 합계를 계산한다.
**VI:** `SUM` tính **tổng** các giá trị số.

```sql
SUM(SAL)
```

Ví dụ:

```text
1000
2000
3000
NULL
```

thì:

```sql
SUM(SAL)
```

→ `6000`

NULL bị bỏ qua.

`SUM` về cơ bản dùng cho dữ liệu numeric.

---

## 4. AVG — phần rất dễ ra đề

**KR:** `AVG`는 NULL을 제외한 값들의 평균을 계산한다.
**VI:** `AVG` tính trung bình **chỉ trên những giá trị khác NULL**.

Giả sử:

```text
SAL
----
100
200
NULL
NULL
```

thì:

```sql
AVG(SAL)
```

không phải:

```text
(100 + 200 + 0 + 0) / 4
```

mà là:

```text
(100 + 200) / 2
= 150
```

---

### AVG(SAL) khác AVG(NVL(SAL,0))

Đây là điểm trong ảnh cần nhớ cực chắc.

```sql
AVG(SAL)
```

→ bỏ NULL.

Trong khi:

```sql
AVG(NVL(SAL, 0))
```

`NVL` biến NULL thành `0` trước.

Với dữ liệu trên:

```sql
AVG(NVL(SAL,0))
```

→

```text
(100 + 200 + 0 + 0) / 4
= 75
```

Vì vậy:

```sql
AVG(SAL)          = 150
AVG(NVL(SAL, 0))  = 75
```

**KR:** NULL을 0으로 처리할 것인지 제외할 것인지에 따라 평균 결과가 달라진다.
**VI:** Kết quả trung bình thay đổi hoàn toàn tùy việc ta **bỏ NULL** hay **coi NULL là 0**.

---

### Một quan hệ rất đáng nhớ

Nếu `EMPNO` là PK:

```sql
SUM(SAL) / COUNT(EMPNO)
```

không nhất thiết bằng:

```sql
AVG(SAL)
```

Bởi vì:

```sql
COUNT(EMPNO)
```

đếm toàn bộ nhân viên.

Nhưng:

```sql
AVG(SAL)
```

chỉ tính nhân viên có `SAL IS NOT NULL`.

Muốn coi nhân viên SAL NULL là 0:

```sql
AVG(NVL(SAL,0))
```

---

## 5. MIN / MAX

**KR:** `MIN`, `MAX`는 각각 최솟값과 최댓값을 반환한다.
**VI:** `MIN` trả về giá trị nhỏ nhất, `MAX` trả về giá trị lớn nhất.

Không chỉ number:

```sql
MIN(SAL)
MAX(SAL)
```

mà còn có thể dùng với date/string tùy DB và datatype:

```sql
MIN(HIREDATE)
MAX(HIREDATE)
```

Ví dụ:

```sql
MIN(HIREDATE)
```

→ người có ngày tuyển dụng sớm nhất.

---

## 6. VARIANCE / STDDEV

**KR:** `VARIANCE`는 분산을, `STDDEV`는 표준편차를 계산한다.
**VI:** `VARIANCE` tính **phương sai**, còn `STDDEV` tính **độ lệch chuẩn**.

Quan hệ:

```text
STDDEV ≈ √VARIANCE
```

SQLD chủ yếu yêu cầu hiểu ý nghĩa, thường không cần tự tính toán thống kê phức tạp.

---

## 7. GROUP BY cơ bản

Ví dụ trong ảnh:

```sql
SELECT DNAME,
       JOB,
       COUNT(*) "Total Empl",
       SUM(SAL) "Total Sal"
FROM EMP, DEPT
WHERE DEPT.DEPTNO = EMP.DEPTNO
GROUP BY DNAME, JOB;
```

**KR:** `DNAME, JOB`의 조합별로 하나의 그룹을 만든다.
**VI:** SQL tạo một group cho **mỗi tổ hợp DNAME + JOB**.

Ví dụ:

```text
SALES + MANAGER
SALES + CLERK
SALES + SALESMAN
RESEARCH + MANAGER
...
```

Nghĩa là:

```sql
GROUP BY DNAME, JOB
```

hãy đọc là:

> "Nhóm theo từng tổ hợp `(DNAME, JOB)`."

Không phải:

> "group DNAME rồi group JOB riêng biệt."

Đây là khác biệt cực kỳ quan trọng trước khi học `ROLLUP/CUBE`.

---

## 8. GROUP BY không tự ORDER BY

**KR:** GROUP BY를 사용한다고 해서 결과가 자동으로 정렬되는 것은 아니다.
**VI:** Dùng `GROUP BY` **không đảm bảo kết quả được sắp xếp**.

Muốn chắc chắn:

```sql
ORDER BY DNAME, JOB
```

Phải nhớ:

> **GROUP BY = grouping**
> **ORDER BY = sorting**

Không được coi chúng là một.

---

## 9. ROLLUP ⭐⭐⭐

Đây là phần quan trọng nhất của nhóm ảnh này.

Câu cơ bản:

```sql
GROUP BY ROLLUP(DNAME, JOB)
```

Hãy hiểu nó tương đương với:

```sql
GROUPING SETS (
    (DNAME, JOB),
    (DNAME),
    ()
)
```

Đây là công thức cực quan trọng.

---

### 9.1 ROLLUP(A,B)

**KR:** `ROLLUP(A,B)`는 계층 구조에 따라 단계적으로 소계를 생성한다.
**VI:** `ROLLUP(A,B)` tạo subtotal theo **cấu trúc phân cấp từ trái sang phải**.

Nó sinh:

```text
(A, B)
(A)
()
```

Trong đó:

```text
(A,B) = chi tiết theo A+B
(A)   = subtotal theo A
()    = grand total
```

Ví dụ:

```sql
GROUP BY ROLLUP(DNAME, JOB)
```

sinh:

```text
DNAME + JOB
DNAME
전체
```

Ví dụ SALES:

```text
SALES  CLERK      950
SALES  MANAGER   2850
SALES  SALESMAN  5600
SALES  NULL      9400   ← subtotal SALES
```

cuối cùng:

```text
NULL   NULL      29025  ← Grand Total
```

---

## 10. Tại sao ROLLUP(A,B) có N+1 level?

**KR:** ROLLUP에서 그룹핑 컬럼의 수가 N개이면 N+1개의 집계 Level이 생성된다.
**VI:** Nếu `ROLLUP` có N column thì sẽ tạo **N+1 cấp aggregation**.

Ví dụ:

```sql
ROLLUP(A)
```

→

```text
(A)
()
```

2 level.

```sql
ROLLUP(A,B)
```

→

```text
(A,B)
(A)
()
```

3 level.

```sql
ROLLUP(A,B,C)
```

→

```text
(A,B,C)
(A,B)
(A)
()
```

4 level.

#### Công thức nhớ

> **ROLLUP = xóa dần từ bên phải.**

Ví dụ:

```text
A B C
↓
A B
↓
A
↓
()
```

Cách này dễ nhớ hơn học thuộc định nghĩa.

---

## 11. Thứ tự ROLLUP cực kỳ quan trọng ⭐⭐⭐

Ảnh dùng ví dụ:

```sql
ROLLUP(species, breed)
```

Nó sinh:

```text
(species, breed)
(species)
()
```

→ subtotal theo `species`.

Ví dụ:

```text
강아지 + 말티즈
강아지 + 비숑프리제
...
강아지 + 합계
```

---

Nếu đổi thành:

```sql
ROLLUP(breed, species)
```

thì:

```text
(breed, species)
(breed)
()
```

Bây giờ subtotal theo **breed**, không phải species.

Do đó:

**KR:** ROLLUP은 인수의 순서가 바뀌면 결과도 바뀐다.
**VI:** Với `ROLLUP`, **đổi thứ tự tham số sẽ làm thay đổi cấu trúc subtotal**.

Đây là đặc điểm phân biệt quan trọng với `CUBE`.

---

## 12. ROLLUP với composite column

Ảnh có:

```sql
GROUP BY ROLLUP(DNAME, (JOB, MGR))
```

Cặp:

```sql
(JOB, MGR)
```

được coi là **một đơn vị grouping duy nhất**.

Do đó hãy tưởng tượng:

```text
A = DNAME
B = (JOB,MGR)
```

thành:

```sql
ROLLUP(A,B)
```

nên tạo:

```text
(DNAME, JOB, MGR)
(DNAME)
()
```

Chứ **không tạo**:

```text
(DNAME, JOB)
```

hay:

```text
(DNAME, MGR)
```

---

### So sánh rất quan trọng

#### Không có ngoặc
Phần này nối mạch SQL với “Không có ngoặc”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
ROLLUP(DNAME, JOB, MGR)
```

→

```text
(DNAME, JOB, MGR)
(DNAME, JOB)
(DNAME)
()
```

#### Có composite column dạng ROLLUP(A, (B, C))
Phần này nối mạch SQL với “Có composite column dạng ROLLUP(A, (B, C))”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
ROLLUP(DNAME, (JOB, MGR))
```

Coi `(JOB, MGR)` là một khối thống nhất $Y$. Số đối số thực tế là $N = 2$ (gồm `DNAME` và `(JOB, MGR)`), do đó tạo ra $N + 1 = 3$ cấp aggregation:

```text
1. (DNAME, JOB, MGR) -- Chi tiết theo DNAME và cặp (JOB, MGR)
2. (DNAME)           -- Tổng phụ theo DNAME (JOB và MGR hiển thị NULL)
3. ()                -- Tổng toàn thể Grand Total (Tất cả hiển thị NULL)
```

`JOB + MGR` được coi như **một package**, tuyệt đối **không có** cấp `(DNAME, JOB)`.

#### Có composite column dạng ROLLUP((A, B), C)
Phần này nối mạch SQL với “Có composite column dạng ROLLUP((A, B), C)”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
ROLLUP((DNAME, JOB), MGR)
```

Coi `(DNAME, JOB)` là một khối thống nhất $X$. Số đối số là $N = 2$ (gồm `(DNAME, JOB)` và `MGR`), do đó cũng tạo ra $N + 1 = 3$ cấp aggregation:

```text
1. (DNAME, JOB, MGR) -- Chi tiết từng phòng ban, công việc và người quản lý
2. (DNAME, JOB)      -- Tổng phụ theo cặp (DNAME, JOB) (MGR hiển thị NULL)
3. ()                -- Tổng toàn thể Grand Total (Tất cả hiển thị NULL)
```

> **Điểm thi trọng tâm:**
> - Trong `ROLLUP((A, B), C)`, hoàn toàn **KHÔNG CÓ** dòng tổng phụ chỉ gom theo `(A)` riêng biệt! Cặp `(A, B)` luôn đi liền với nhau hoặc cùng biến mất ở mức tổng toàn thể `()`.
> - Tương đương cú pháp: `GROUPING SETS ( ((A, B), C), ((A, B)), () )`.

---

## 13. GROUPING() ⭐⭐⭐

Một vấn đề xuất hiện khi dùng `ROLLUP`.

Ví dụ subtotal:

```text
SALES  NULL  9400
```

NULL này có thể có 2 nghĩa:

1. JOB thật sự là NULL.
2. NULL do ROLLUP tạo ra để biểu diễn subtotal.

Làm sao phân biệt?

→ `GROUPING()`.

---

### Quy tắc

**KR:** ROLLUP/CUBE에 의해 생성된 NULL이면 `GROUPING(column)`은 1을 반환한다.
**VI:** Nếu NULL được sinh ra bởi ROLLUP/CUBE để biểu diễn subtotal/total thì `GROUPING(column)` trả `1`.

Ngược lại:

```text
GROUPING(column) = 0
```

→ column đang tham gia grouping ở level đó; một NULL dữ liệu thật cũng không bị đánh dấu là subtotal.

Tóm lại để đi thi:

```text
GROUPING(column) = 1
→ NULL do GROUP FUNCTION sinh ra

GROUPING(column) = 0
→ không phải NULL tổng hợp của level đó
```

---

## 14. Dùng GROUPING thay NVL

Trong ảnh:

```sql
CASE
    WHEN GROUPING(DNAME) = 1
    THEN 'All Departments'
    ELSE DNAME
END
```

và:

```sql
CASE
    WHEN GROUPING(JOB) = 1
    THEN 'All Jobs'
    ELSE JOB
END
```

Tại sao tốt hơn:

```sql
NVL(JOB, 'All Jobs')
```

?

Vì `NVL` không biết NULL đó là:

```text
NULL thật trong data
```

hay:

```text
NULL do ROLLUP sinh ra.
```

Nhưng `GROUPING()` biết.

Vì vậy:

> **ROLLUP/CUBE에서 생성된 NULL 판별 → GROUPING()**

---

## 15. CASE và DECODE đều dùng được

Ảnh cho hai cách.

#### CASE
Phần này nối mạch SQL với “CASE”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
CASE
    WHEN GROUPING(DNAME) = 1
    THEN 'All Departments'
    ELSE DNAME
END
```

#### Oracle DECODE
Phần này nối mạch SQL với “Oracle DECODE”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
DECODE(
    GROUPING(DNAME),
    1, 'All Departments',
    DNAME
)
```

Hai cách nhằm mục đích tương tự.

Trong Oracle, `DECODE` rất hay xuất hiện trong đề SQLD.

---

## 15.1. GROUPING_ID() — Mã hóa nhị phân các cấp độ tổng gộp ⭐⭐⭐

**KR:** `GROUPING_ID`는 여러 `GROUPING` 함수의 반환값을 결합하여 2진수 비트열(Bit Vector)로 변환한 뒤 이를 10진수 정수로 반환하는 함수이다.
**VI:** `GROUPING_ID` là hàm gộp kết quả của nhiều hàm `GROUPING` thành một vector bit nhị phân rồi chuyển đổi thành số nguyên thập phân tương ứng.

Khi truy vấn có nhiều cột gom nhóm, việc kiểm tra từng điều kiện `GROUPING(col1) = 1 AND GROUPING(col2) = 1` trong mệnh đề `HAVING` hoặc `ORDER BY` sẽ rất rườm rà. `GROUPING_ID(A, B)` giải quyết triệt để vấn đề này:

$$\text{GROUPING\_ID}(A, B) = \text{GROUPING}(A) \times 2^1 + \text{GROUPING}(B) \times 2^0$$

#### Bảng giá trị chuyển đổi GROUPING_ID(DNAME, JOB)

| Cấp độ tổng hợp | GROUPING(DNAME) | GROUPING(JOB) | Chuỗi bit nhị phân | Kết quả GROUPING_ID(DNAME, JOB) |
| :--- | :--- | :--- | :--- | :--- |
| **Chi tiết (DNAME, JOB)** | 0 | 0 | `00` | **0** |
| **Tổng phụ theo DNAME (DNAME)** | 0 | 1 | `01` | **1** |
| **Tổng phụ theo JOB (JOB)** | 1 | 0 | `10` | **2** |
| **Tổng toàn thể Grand Total ()** | 1 | 1 | `11` | **3** |

#### Ví dụ truy vấn thực chiến:

```sql
SELECT DNAME,
       JOB,
       COUNT(*) AS EMP_CNT,
       SUM(SAL) AS TOTAL_SAL,
       GROUPING(DNAME) AS G_DNAME,
       GROUPING(JOB)   AS G_JOB,
       GROUPING_ID(DNAME, JOB) AS GID
FROM EMP
GROUP BY CUBE(DNAME, JOB)
ORDER BY GID, DNAME;
```

#### Kết quả thực tế (ASCII Table):

```text
+------------+-----------+---------+-----------+---------+-------+-----+
| DNAME      | JOB       | EMP_CNT | TOTAL_SAL | G_DNAME | G_JOB | GID |
+------------+-----------+---------+-----------+---------+-------+-----+
| ACCOUNTING | CLERK     |       1 |      1300 |       0 |     0 |   0 |
| ACCOUNTING | MANAGER   |       1 |      2450 |       0 |     0 |   0 |
| RESEARCH   | ANALYST   |       2 |      6000 |       0 |     0 |   0 |
| ACCOUNTING | NULL      |       2 |      3750 |       0 |     1 |   1 |
| RESEARCH   | NULL      |       2 |      6000 |       0 |     1 |   1 |
| NULL       | CLERK     |       1 |      1300 |       1 |     0 |   2 |
| NULL       | MANAGER   |       1 |      2450 |       1 |     0 |   2 |
| NULL       | NULL      |       4 |      9750 |       1 |     1 |   3 |
+------------+-----------+---------+-----------+---------+-------+-----+
```

> **Mẹo thi SQLD:** Muốn lọc chỉ lấy dòng tổng phụ theo từng phòng ban và tổng toàn thể, ta chỉ cần viết: `HAVING GROUPING_ID(DNAME, JOB) IN (1, 3)`.

---

## 16. CUBE ⭐⭐⭐

Nếu ROLLUP là **phân cấp**, CUBE là **mọi tổ hợp grouping có thể có**.

**KR:** CUBE는 그룹핑 가능한 모든 조합에 대해 집계를 생성한다.
**VI:** `CUBE` tạo aggregation cho **tất cả các tổ hợp grouping có thể**.

Ví dụ:

```sql
GROUP BY CUBE(DNAME, JOB)
```

tương đương:

```sql
GROUPING SETS (
    (DNAME, JOB),
    (DNAME),
    (JOB),
    ()
)
```

Đây là công thức phải thuộc.

---

## 17. ROLLUP vs CUBE

#### ROLLUP
Phần này nối mạch SQL với “ROLLUP”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
ROLLUP(A,B)
```

→

```text
(A,B)
(A)
()
```

#### CUBE
Phần này nối mạch SQL với “CUBE”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
CUBE(A,B)
```

→

```text
(A,B)
(A)
(B)
()
```

Khác biệt chính:

```text
(B)
```

CUBE có.

ROLLUP không có.

---

### Ví dụ từ ảnh
Phần này nối mạch SQL với “Ví dụ từ ảnh”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
CUBE(DNAME, JOB)
```

sinh:

```text
SALES + CLERK
SALES + MANAGER
...
```

subtotal department:

```text
SALES       9400
RESEARCH   10875
ACCOUNTING  8750
```

subtotal JOB:

```text
CLERK       4150
ANALYST     6000
MANAGER     8275
SALESMAN    5600
PRESIDENT   5000
```

và cuối cùng:

```text
GRAND TOTAL = 29025
```

---

## 18. Thứ tự CUBE khác ROLLUP

Đây là câu dễ thi.

```sql
CUBE(A,B)
```

và:

```sql
CUBE(B,A)
```

đều tạo cùng các grouping set:

```text
(A,B)
(A)
(B)
()
```

Do đó về **tập kết quả aggregation**, thứ tự không quan trọng.

Trong khi:

```sql
ROLLUP(A,B)
```

→

```text
(A,B)
(A)
()
```

nhưng:

```sql
ROLLUP(B,A)
```

→

```text
(B,A)
(B)
()
```

subtotal thay đổi.

#### Nhớ
Phần này nối mạch SQL với “Nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
ROLLUP → hierarchy → ORDER MATTERS
CUBE   → combinations → ORDER DOESN'T MATTER
```

Lưu ý: "order doesn't matter" ở đây nói về **các grouping set được sinh ra**, không có nghĩa SQL đảm bảo thứ tự hiển thị row. Muốn sort vẫn phải dùng `ORDER BY`.

---

## 19. Tại sao CUBE nặng hơn ROLLUP?

Với N column:

#### ROLLUP
Phần này nối mạch SQL với “ROLLUP”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
N + 1 grouping levels
```

#### CUBE
Phần này nối mạch SQL với “CUBE”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
2^N grouping combinations
```

Ví dụ 3 column:

```sql
ROLLUP(A,B,C)
```

chỉ:

```text
(A,B,C)
(A,B)
(A)
()
```

= 4 grouping sets.

Nhưng:

```sql
CUBE(A,B,C)
```

sinh:

```text
(A,B,C)
(A,B)
(A,C)
(B,C)
(A)
(B)
(C)
()
```

= **8 grouping sets**.

Vì thế:

**KR:** CUBE는 ROLLUP보다 시스템 부하가 커질 수 있다.
**VI:** CUBE có thể gây tải hệ thống lớn hơn ROLLUP vì số tổ hợp tăng rất nhanh.

---

## 20. GROUPING SETS ⭐⭐⭐

Đây là cách linh hoạt nhất.

```sql
GROUP BY GROUPING SETS(DNAME, JOB)
```

nghĩa là:

```text
(DNAME)
(JOB)
```

Chỉ đúng những grouping mà ta yêu cầu.

Không có:

```text
(DNAME,JOB)
```

và cũng không tự có:

```text
()
```

---

### Đây là chỗ rất dễ nhầm
Phần này nối mạch SQL với “Đây là chỗ rất dễ nhầm”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
GROUP BY DNAME, JOB
```

nghĩa là:

```text
(DNAME,JOB)
```

Nhưng:

```sql
GROUP BY GROUPING SETS(DNAME, JOB)
```

nghĩa là:

```text
(DNAME)
(JOB)
```

Hai câu **hoàn toàn khác nhau**.

---

## 21. GROUPING SETS không tự sinh Grand Total

**KR:** GROUPING SETS는 ROLLUP이나 CUBE와 달리 자동으로 총계를 생성하지 않는다.
**VI:** Khác ROLLUP/CUBE, GROUPING SETS **không tự động tạo Grand Total**.

Ví dụ:

```sql
GROUPING SETS(DNAME, JOB)
```

→

```text
DNAME subtotal
JOB subtotal
```

không có total.

Muốn thêm total:

```sql
GROUP BY GROUPING SETS (
    DNAME,
    JOB,
    ()
);
```

`()` chính là:

> **Grand Total grouping set**

---

## 22. GROUPING SETS tương đương UNION ALL

Ví dụ:

```sql
GROUP BY GROUPING SETS(DNAME, JOB)
```

về logic tương đương:

```sql
SELECT DNAME, NULL AS JOB, ...
FROM ...
GROUP BY DNAME

UNION ALL

SELECT NULL AS DNAME, JOB, ...
FROM ...
GROUP BY JOB;
```

Đây là lý do `GROUPING SETS` rất hữu ích: thay vì viết nhiều SELECT + `UNION ALL`, ta khai báo trực tiếp các grouping cần lấy.

---

## 23. GROUPING SETS không phụ thuộc thứ tự
Phần này nối mạch SQL với “23. GROUPING SETS không phụ thuộc thứ tự”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
GROUPING SETS(A,B)
```

và:

```sql
GROUPING SETS(B,A)
```

đều yêu cầu:

```text
(A)
(B)
```

Vì vậy tương tự CUBE, **thứ tự đối số không làm thay đổi tập grouping được yêu cầu**.

---

## 24. Có thể biểu diễn ROLLUP bằng GROUPING SETS

Ảnh cuối có:

```sql
SELECT DEPTNO, JOB, SUM(SAL)
FROM EMP
GROUP BY ROLLUP(DEPTNO, JOB);
```

ROLLUP sinh:

```text
(DEPTNO,JOB)
(DEPTNO)
()
```

Do đó viết bằng GROUPING SETS:

```sql
SELECT DEPTNO, JOB, SUM(SAL)
FROM EMP
GROUP BY GROUPING SETS (
    (DEPTNO, JOB),
    DEPTNO,
    ()
);
```

Hai câu mô tả cùng các grouping set.

---

## 25. Biểu diễn CUBE bằng GROUPING SETS
Phần này nối mạch SQL với “25. Biểu diễn CUBE bằng GROUPING SETS”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
CUBE(DEPTNO, JOB)
```

sinh:

```text
(DEPTNO,JOB)
(DEPTNO)
(JOB)
()
```

nên tương đương:

```sql
GROUP BY GROUPING SETS (
    (DEPTNO, JOB),
    DEPTNO,
    JOB,
    ()
);
```

Đây chính là cách tốt nhất để hiểu cả 3 hàm.

---

## 26. Bảng so sánh phải thuộc trước khi thi
Phần này nối mạch SQL với “26. Bảng so sánh phải thuộc trước khi thi”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

| Expression                  | Grouping sets thực tế |
| --------------------------- | --------------------- |
| `GROUP BY A,B`              | `(A,B)`               |
| `ROLLUP(A,B)`               | `(A,B) → (A) → ()`    |
| `ROLLUP(B,A)`               | `(B,A) → (B) → ()`    |
| `CUBE(A,B)`                 | `(A,B), (A), (B), ()` |
| `GROUPING SETS(A,B)`        | `(A), (B)`            |
| `GROUPING SETS((A,B),A,())` | `(A,B), (A), ()`      |

---

## 27. Cách suy luận nhanh khi gặp đề SQLD

Đừng cố nhớ output bằng hình. Hãy **bung grouping set ra**.

Ví dụ đề hỏi:

```sql
GROUP BY ROLLUP(A,B,C)
```

Viết ngay:

```text
ABC
AB
A
()
```

Nếu hỏi:

```sql
GROUP BY CUBE(A,B)
```

viết:

```text
AB
A
B
()
```

Nếu hỏi:

```sql
GROUP BY GROUPING SETS((A,B), A, C)
```

viết:

```text
AB
A
C
```

Xong. Sau đó nhìn grouping nào cần tính.

---

## 28. Một bẫy đặc biệt: NULL trong kết quả

Giả sử:

```text
DNAME       JOB       SUM
----------- -------- -----
SALES       CLERK      950
SALES       NULL      9400
NULL        NULL     29025
```

Không được kết luận ngay rằng:

```text
JOB NULL = dữ liệu JOB bị NULL
```

Nó có thể là subtotal do `ROLLUP`.

Phải dùng:

```sql
GROUPING(JOB)
```

để xác định.

```text
GROUPING(JOB)=1
→ JOB đã bị loại khỏi grouping ở level hiện tại

GROUPING(JOB)=0
→ JOB vẫn thuộc grouping level
```

Đây là cách hiểu chính xác hơn chỉ học:

> "NULL thì GROUPING = 1."

---

## 29. Sơ đồ tổng hợp cực dễ nhớ

Hãy lấy:

```text
A = Department
B = Job
```

#### GROUP BY
Phần này nối mạch SQL với “GROUP BY”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
GROUP BY A,B

A+B
```

#### ROLLUP
Phần này nối mạch SQL với “ROLLUP”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
ROLLUP(A,B)

A+B
 ↓
 A
 ↓
TOTAL
```

#### CUBE
Phần này nối mạch SQL với “CUBE”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
CUBE(A,B)

      A+B
     /   \
    A     B
     \   /
     TOTAL
```

#### GROUPING SETS
Phần này nối mạch SQL với “GROUPING SETS”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
GROUPING SETS(A,B)

A       B
```

Bạn **chỉ lấy đúng những group mình chỉ định**.

---

## 🔥 SQLD NOTE — 반드시 암기 / Bắt buộc nhớ

1. **집계 함수는 일반적으로 NULL을 제외한다.**
   Aggregate Function thường bỏ qua NULL.

2. `COUNT(*)` → đếm row; `COUNT(column)` → bỏ NULL của column.

3. `AVG(SAL)` khác `AVG(NVL(SAL,0))`.

4. `GROUP BY A,B` nghĩa là group theo **tổ hợp `(A,B)`**.

5. `GROUP BY` **không đảm bảo sorting** → cần `ORDER BY`.

6. `ROLLUP(A,B)`:

   ```text
   AB → A → ()
   ```

7. **ROLLUP phụ thuộc thứ tự tham số.**

8. `CUBE(A,B)`:

   ```text
   AB + A + B + ()
   ```

9. CUBE sinh mọi combination → N column có tối đa `2^N` grouping sets.

10. `GROUPING SETS(A,B)`:

    ```text
    A + B
    ```

    **không phải AB**.

11. GROUPING SETS không tự tạo Grand Total; muốn total thêm `()`.

12. `GROUPING(column)=1` → column bị loại khỏi grouping ở subtotal/total level do group function tạo ra.

13. `ROLLUP(A,(B,C))` coi `(B,C)` là **một composite grouping unit**.

14. Cả `ROLLUP` và `CUBE` đều có thể biểu diễn bằng `GROUPING SETS`.

#### Công thức nhớ 10 giây trước khi vào thi
Phần này nối mạch SQL với “Công thức nhớ 10 giây trước khi vào thi”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
ROLLUP(A,B)
= AB + A + TOTAL

CUBE(A,B)
= AB + A + B + TOTAL

GROUPING SETS(A,B)
= A + B
```

Và câu quyết định:

> **ROLLUP = 계층 / hierarchy**
> **CUBE = 모든 조합 / all combinations**
> **GROUPING SETS = 내가 지정 / exactly what I specify**

---

## 30. Bảng ma trận so sánh Oracle vs SQL Server về hàm nhóm (Group Functions)

| Tiêu chí kỹ thuật | Oracle Database | Microsoft SQL Server | Điểm khác biệt & Bẫy thi SQLD |
| :--- | :--- | :--- | :--- |
| **Cú pháp ANSI ROLLUP** | `GROUP BY ROLLUP(A, B)` | `GROUP BY ROLLUP(A, B)` | Cả hai đều tuân thủ đầy đủ chuẩn ANSI SQL:1999+. |
| **Cú pháp ANSI CUBE** | `GROUP BY CUBE(A, B)` | `GROUP BY CUBE(A, B)` | Cả hai đều hỗ trợ đầy đủ chuẩn ANSI. |
| **Cú pháp ANSI GROUPING SETS** | `GROUP BY GROUPING SETS(...)` | `GROUP BY GROUPING SETS(...)` | Chuẩn ANSI tương thích 100% trên cả hai DBMS. |
| **Cú pháp cũ (Non-ANSI)** | Không hỗ trợ cú pháp `WITH ROLLUP` | Hỗ trợ `GROUP BY A, B WITH ROLLUP` (cú pháp cũ của T-SQL, hiện đã deprecated) | Đề thi SQLD ưu tiên cú pháp chuẩn ANSI `GROUP BY ROLLUP(A, B)`. |
| **Cột kết hợp (Composite)** | `ROLLUP((A, B), C)` | `ROLLUP((A, B), C)` | Cả hai đều hỗ trợ gom nhóm cột bằng cặp ngoặc đơn `()`. |
| **Hàm GROUPING** | `GROUPING(col)` (trả về 0 hoặc 1) | `GROUPING(col)` (trả về 0 hoặc 1) | Hoàn toàn tương đồng: trả về 1 khi là dòng tổng gộp (Subtotal/Total). |
| **Hàm GROUPING_ID** | `GROUPING_ID(col1, col2)` | `GROUPING_ID(col1, col2)` | Cả hai đều tính bitmask nhị phân chuyển đổi thành số nguyên thập phân. |
| **Hàm GROUPING_ID cú pháp cũ** | Không có hàm `GROUPING()` đa tham số | Trước SQL Server 2008 dùng hàm `GROUPING_ID()`, cú pháp `GROUPING(col)` chỉ nhận 1 tham số | Không dùng `GROUPING(A, B)` trực tiếp, phải dùng `GROUPING_ID(A, B)`. |

---

## 31. Cạm bẫy thi cử trọng điểm (출제 함정 & 오답 노트)

> [!WARNING]
> Dưới đây là 5 cạm bẫy kinh điển trong các kỳ thi SQLD liên quan đến Hàm nhóm (Group Functions):

### Cạm bẫy 1: Nhầm lẫn bản chất của hàm `GROUPING(col)` khi dữ liệu gốc có giá trị `NULL`
- **Tình huống:** Bảng dữ liệu gốc có một nhân viên chưa được xếp việc (`JOB` mang giá trị `NULL`). Khi chạy `GROUP BY ROLLUP(JOB)`, dòng hiển thị mức chi tiết của nhân viên này sẽ có `JOB = NULL`.
- **Hỏi:** Tại dòng mức chi tiết này, hàm `GROUPING(JOB)` trả về 0 hay 1?
- **Bẫy sai:** Nghĩ rằng cứ thấy cột có giá trị `NULL` là `GROUPING` sẽ trả về `1`.
- **Đúng chuẩn:** `GROUPING(JOB)` **trả về 0**!
  - `GROUPING(col) = 0`: Cột tham gia vào cấp độ gom nhóm của dòng hiện tại (dù giá trị dữ liệu thật sự trong bảng có là NULL).
  - `GROUPING(col) = 1`: Dòng hiện tại là dòng Subtotal / Grand Total do hệ thống tự sinh ra, cột này bị loại khỏi cấp độ gom nhóm.

### Cạm bẫy 2: Số mức tổng gộp khi có cột kết hợp (Composite Column)
- Với $N$ cột thông thường, `ROLLUP` sinh ra $N + 1$ mức. Nhưng khi có cặp ngoặc đơn `ROLLUP((A, B), C)`, số phần tử gom nhóm thực tế chỉ là $2$ (gồm khối `(A, B)` và cột `C`), do đó chỉ sinh ra $2 + 1 = 3$ mức:
  1. `((A, B), C)`
  2. `((A, B))`
  3. `()`
- **Bẫy thi:** Đề bài lừa rằng có 4 mức hoặc có mức gom riêng theo `(A)`. Nhớ rằng khối `(A, B)` bên trong ngoặc đơn không bao giờ bị tách rời!

### Cạm bẫy 3: `GROUPING SETS` không tự động tạo dòng tổng toàn thể (Grand Total)
- Cả `ROLLUP` và `CUBE` luôn tự động bổ sung dòng Grand Total `()`.
- Nhưng `GROUPING SETS(A, B)` **tuyệt đối không** có Grand Total! Nó chỉ tính riêng rẽ 2 mức: nhóm theo `(A)` và nhóm theo `(B)`.
- Muốn có Grand Total trong `GROUPING SETS`, người viết bắt buộc phải thêm cặp ngoặc rỗng `()`: `GROUPING SETS(A, B, ())`.

### Cạm bẫy 4: Đổi thứ tự tham số trong `ROLLUP` vs `CUBE`
- `ROLLUP(A, B)` tạo ra các nhóm: `(A, B)`, `(A)`, `()`.
- `ROLLUP(B, A)` tạo ra các nhóm: `(B, A)`, `(B)`, `()`.
  $\rightarrow$ **Thứ tự tham số trong ROLLUP làm thay đổi hoàn toàn kết quả tổng phụ (cấu trúc phân cấp)!**
- Ngược lại, `CUBE(A, B)` và `CUBE(B, A)` đều tạo ra 4 nhóm: `(A, B)`, `(A)`, `(B)`, `()`.
  $\rightarrow$ **Thứ tự tham số trong CUBE không làm thay đổi các tập hợp gom nhóm (quan hệ bình đẳng)!**

### Cạm bẫy 5: Rollup từng phần (Partial Rollup)
- Khi viết: `GROUP BY A, ROLLUP(B)`
- Cột `A` nằm độc lập bên ngoài, nên nó luôn luôn hiện diện trong mọi mức tổng hợp!
- Các mức tạo ra:
  - Ghép `A` với `B`: tạo mức `(A, B)`.
  - Ghép `A` với `()`: tạo mức `(A)`.
- **Bẫy thi:** Truy vấn `GROUP BY A, ROLLUP(B)` **KHÔNG HỀ sinh ra Grand Total `()`** vì cột `A` luôn cố định tham gia vào mọi dòng kết quả!

---

## 32. Câu hỏi trắc nghiệm thi thử mô phỏng (실전 기출 변형 문제 & 정답 해설)

### Câu 1: Xác định tập hợp gom nhóm tương đương (Độ khó: Trung bình)
Cho câu lệnh SQL sau thực thi trên hệ quản trị cơ sở dữ liệu Oracle:

```sql
SELECT DEPTNO, JOB, MGR, SUM(SAL) AS TOTAL_SAL
FROM EMP
GROUP BY ROLLUP((DEPTNO, JOB), MGR);
```

Mệnh đề `GROUP BY` nào dưới đây sử dụng `GROUPING SETS` mang lại kết quả gom nhóm hoàn toàn tương đương?

A. `GROUP BY GROUPING SETS ((DEPTNO, JOB, MGR), (DEPTNO, JOB), (DEPTNO), ())`
B. `GROUP BY GROUPING SETS ((DEPTNO, JOB, MGR), (DEPTNO, JOB), ())`
C. `GROUP BY GROUPING SETS ((DEPTNO, JOB, MGR), (JOB, MGR), ())`
D. `GROUP BY GROUPING SETS ((DEPTNO, JOB), (MGR), ())`

> **Đáp án chính xác:** **B**
>
> **Giải thích chi tiết từng lựa chọn:**
> - **Phân tích đề bài:** Mệnh đề `ROLLUP((DEPTNO, JOB), MGR)` chứa cặp cột kết hợp `(DEPTNO, JOB)` đóng vai trò là một phần tử thứ nhất, và `MGR` là phần tử thứ hai. Số đối số thực tế là $N = 2$.
> - Quy tắc ROLLUP cắt tỉa từ phải sang trái:
>   1. Toàn bộ đối số: `((DEPTNO, JOB), MGR)` $\rightarrow$ Tập nhóm `(DEPTNO, JOB, MGR)`.
>   2. Bỏ `MGR`: còn lại `((DEPTNO, JOB))` $\rightarrow$ Tập nhóm `(DEPTNO, JOB)`.
>   3. Bỏ nốt phần tử cuối: còn lại `()` $\rightarrow$ Tổng toàn thể Grand Total.
> - **Lựa chọn B:** Chính xác, gồm đúng 3 tập hợp `((DEPTNO, JOB, MGR), (DEPTNO, JOB), ())`.
> - **Lựa chọn A sai:** Chứa thêm tập `(DEPTNO)`, nhưng `(DEPTNO, JOB)` là khối kết hợp nên không bao giờ bị tách để tính riêng `DEPTNO`.
> - **Lựa chọn C sai:** Chứa tập `(JOB, MGR)` không tồn tại trong cấu trúc phân cấp từ trái sang phải của ROLLUP.
> - **Lựa chọn D sai:** Thiếu tập hợp đầy đủ `(DEPTNO, JOB, MGR)`.

---

### Câu 2: Phân biệt giá trị NULL thật và dòng tổng hợp qua GROUPING (Độ khó: Cao)
Xét bảng `TB_SALES` có cấu trúc và dữ liệu như sau:

```text
+---------+----------+--------+
| PROD_ID | CUST_ID  | AMOUNT |
+---------+----------+--------+
| P1      | C100     |    500 |
| P1      | NULL     |    300 |
| P2      | C200     |    400 |
+---------+----------+--------+
```

Người dùng thực thi câu lệnh SQL sau:

```sql
SELECT PROD_ID,
       CUST_ID,
       SUM(AMOUNT) AS SUM_AMT,
       GROUPING(CUST_ID) AS G_CUST
FROM TB_SALES
GROUP BY ROLLUP(PROD_ID, CUST_ID)
ORDER BY PROD_ID, CUST_ID;
```

Dòng kết quả tương ứng với `PROD_ID = 'P1'` mà có `CUST_ID` hiển thị giá trị `NULL` sẽ có bao nhiêu dòng và giá trị cột `G_CUST` tương ứng là gì?

A. Chỉ có 1 dòng duy nhất và có `G_CUST = 1`.
B. Chỉ có 1 dòng duy nhất và có `G_CUST = 0`.
C. Có 2 dòng: một dòng có `G_CUST = 0` (dữ liệu thật) và một dòng có `G_CUST = 1` (tổng phụ của P1).
D. Có 2 dòng: cả hai dòng đều có `G_CUST = 1`.

> **Đáp án chính xác:** **C**
>
> **Giải thích chi tiết từng lựa chọn:**
> - **Phân tích cơ chế:**
>   - Bảng nguồn có 1 bản ghi thật sự mang giá trị `CUST_ID IS NULL` với `AMOUNT = 300` thuộc `PROD_ID = 'P1'`. Khi gom nhóm chi tiết theo `(PROD_ID, CUST_ID)`, dòng này được tạo ra và cột `CUST_ID` tham gia vào cấp độ gom nhóm, vì vậy `GROUPING(CUST_ID)` trả về **0**.
>   - Ngoài ra, `ROLLUP(PROD_ID, CUST_ID)` tự động tạo thêm một dòng tổng phụ cho từng sản phẩm `(PROD_ID)`. Tại dòng tổng phụ của sản phẩm `P1`, tổng doanh số là $500 + 300 = 800$, giá trị cột `CUST_ID` được hệ thống hiển thị là `NULL` do bị gộp, và hàm `GROUPING(CUST_ID)` trả về **1**.
> - Do đó, với `PROD_ID = 'P1'`, có đúng 2 dòng xuất hiện `CUST_ID` là `NULL`:
>   - Dòng 1: `PROD_ID = 'P1'`, `CUST_ID = NULL`, `SUM_AMT = 300`, `G_CUST = 0`.
>   - Dòng 2: `PROD_ID = 'P1'`, `CUST_ID = NULL`, `SUM_AMT = 800`, `G_CUST = 1`.
> - **Lựa chọn C:** Khẳng định chính xác bản chất khác biệt giữa NULL dữ liệu thật và NULL do tổng hợp.
> - **Lựa chọn A, B, D sai:** Đều ngộ nhận về số dòng hoặc đánh đồng giá trị trả về của hàm GROUPING.

---

### Câu 3: Tính toán giá trị GROUPING_ID (Độ khó: Trung bình)
Cho câu lệnh SQL sau:

```sql
SELECT DNAME,
       JOB,
       SUM(SAL) AS TOTAL_SAL,
       GROUPING_ID(DNAME, JOB) AS GID
FROM EMP
GROUP BY CUBE(DNAME, JOB)
HAVING GROUPING_ID(DNAME, JOB) = 2;
```

Dòng dữ liệu được trả về bởi mệnh đề `HAVING GROUPING_ID(DNAME, JOB) = 2` đại diện cho mức tổng hợp nào?

A. Mức chi tiết từng phòng ban và từng công việc `(DNAME, JOB)`.
B. Mức tổng phụ theo từng phòng ban `(DNAME)`.
C. Mức tổng phụ theo từng công việc `(JOB)`.
D. Mức tổng toàn thể của toàn bộ công ty `()`.

> **Đáp án chính xác:** **C**
>
> **Giải thích chi tiết từng lựa chọn:**
> - **Phân tích công thức:**
>   $$\text{GROUPING\_ID}(DNAME, JOB) = \text{GROUPING}(DNAME) \times 2 + \text{GROUPING}(JOB) \times 1$$
> - Để giá trị $\text{GID} = 2$, trong hệ nhị phân giá trị này tương ứng với chuỗi bit `10`:
>   - $\text{GROUPING}(DNAME) = 1$ (cột `DNAME` bị loại khỏi nhóm, tức là subtotal không phân theo phòng ban).
>   - $\text{GROUPING}(JOB) = 0$ (cột `JOB` tham gia gom nhóm).
> - Điều này có nghĩa dòng kết quả đang gom nhóm độc lập theo từng chức vụ công việc `(JOB)`.
> - **Lựa chọn C:** Hoàn toàn chính xác.
> - **Lựa chọn A sai:** Mức chi tiết có bit `00` $\rightarrow \text{GID} = 0$.
> - **Lựa chọn B sai:** Mức tổng phụ theo DNAME có bit `01` $\rightarrow \text{GID} = 1$.
> - **Lựa chọn D sai:** Mức tổng toàn thể có bit `11` $\rightarrow \text{GID} = 3$.

---

### Câu 4: Phân biệt Rollup từng phần - Partial Rollup (Độ khó: Dễ)
Nhà phân tích dữ liệu thực thi câu lệnh SQL sau:

```sql
SELECT REGION, CHANNEL, SUM(REVENUE) AS TOTAL_REV
FROM SALES
GROUP BY REGION, ROLLUP(CHANNEL);
```

Giả sử bảng `SALES` có 3 vùng (`REGION`) và 2 kênh bán hàng lẻ (`CHANNEL`). Hỏi câu truy vấn trên sẽ trả về tổng cộng bao nhiêu dòng kết quả (giả sử tất cả các tổ hợp đều có dữ liệu)?

A. 6 dòng
B. 9 dòng
C. 10 dòng
D. 12 dòng

> **Đáp án chính xác:** **B**
>
> **Giải thích chi tiết từng lựa chọn:**
> - **Phân tích cơ chế:** Mệnh đề `GROUP BY REGION, ROLLUP(CHANNEL)` là Rollup từng phần.
> - `ROLLUP(CHANNEL)` với $N = 1$ tạo ra $1 + 1 = 2$ mức: `(CHANNEL)` và `()`.
> - Kết hợp với `REGION` cố định ở ngoài:
>   - Mức 1: `(REGION, CHANNEL)` $\rightarrow$ Có 3 vùng $\times$ 2 kênh = 6 dòng chi tiết.
>   - Mức 2: `(REGION, ())` tức `(REGION)` $\rightarrow$ Tổng phụ theo từng vùng = 3 dòng.
> - Truy vấn này **không tạo ra Grand Total** `()` vì `REGION` luôn tham gia bắt buộc.
> - Tổng số dòng kết quả = $6 + 3 = 9$ dòng.
> - **Lựa chọn B:** Hoàn toàn chính xác ($9$ dòng).
> - **Lựa chọn C sai:** Bẫy cộng thêm 1 dòng Grand Total ($9 + 1 = 10$).
> - **Lựa chọn A sai:** Chỉ tính mức chi tiết mà quên mất các dòng tổng phụ theo vùng.
> - **Lựa chọn D sai:** Nhầm lẫn với CUBE toàn phần ($3 \times 2 + 3 + 2 + 1 = 12$).
