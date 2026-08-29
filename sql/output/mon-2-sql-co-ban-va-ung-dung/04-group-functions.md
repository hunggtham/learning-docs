# Group Functions

> **Mục tiêu:** Aggregate, GROUP BY, ROLLUP, CUBE, GROUPING và GROUPING SETS.

> **Cách học:** Đọc phần khái niệm → tự chạy lại các ví dụ SQL → chốt lại các mục `Keyword`, bảng so sánh và phần ghi nhớ cuối bài.

---

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

#### Có composite column

```sql
ROLLUP(DNAME, (JOB,MGR))
```

→

```text
(DNAME, JOB, MGR)
(DNAME)
()
```

`JOB + MGR` được coi như **một package**.

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

```sql
CASE
    WHEN GROUPING(DNAME) = 1
    THEN 'All Departments'
    ELSE DNAME
END
```

#### Oracle DECODE

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

```text
ROLLUP → hierarchy → ORDER MATTERS
CUBE   → combinations → ORDER DOESN'T MATTER
```

Lưu ý: "order doesn't matter" ở đây nói về **các grouping set được sinh ra**, không có nghĩa SQL đảm bảo thứ tự hiển thị row. Muốn sort vẫn phải dùng `ORDER BY`.

---

## 19. Tại sao CUBE nặng hơn ROLLUP?

Với N column:

#### ROLLUP

```text
N + 1 grouping levels
```

#### CUBE

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

```text
GROUP BY A,B

A+B
```

#### ROLLUP

```text
ROLLUP(A,B)

A+B
 ↓
 A
 ↓
TOTAL
```

#### CUBE

```text
CUBE(A,B)

      A+B
     /   \
    A     B
     \   /
     TOTAL
```

#### GROUPING SETS

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
