# Window Functions

## 1. 윈도우 함수 — Window Function ⭐⭐⭐

**KR:** 집계 함수는 여러 행을 하나의 결과 행으로 집계하기 때문에 원본 데이터의 개별 행 정보가 사라질 수 있다.
**VI:** Aggregate Function gom nhiều row thành một kết quả nên thông tin của từng row ban đầu có thể biến mất.

Ví dụ:

```sql
SELECT DEPTNO, SUM(SAL)
FROM EMP
GROUP BY DEPTNO;
```

Nếu phòng 10 có 3 nhân viên:

```text
KING    5000
CLARK   2450
MILLER  1300
```

thì kết quả chỉ còn:

```text
DEPTNO   SUM(SAL)
10       8750
```

Ba row → một row.

---

**KR:** 윈도우 함수는 원본 행을 유지하면서 여러 행을 대상으로 연산할 수 있다.
**VI:** Window Function thì **giữ nguyên từng row**, nhưng vẫn có thể tính toán dựa trên nhiều row khác.

```sql
SELECT ENAME,
       DEPTNO,
       SAL,
       SUM(SAL) OVER(PARTITION BY DEPTNO) AS TOTAL
FROM EMP;
```

Kết quả:

```text
ENAME    DEPTNO  SAL    TOTAL
KING       10    5000    8750
CLARK      10    2450    8750
MILLER     10    1300    8750
```

Đây chính là bản chất quan trọng nhất:

> **GROUP BY → 행을 합친다.**
> Gom các row.

> **Window Function → 행을 유지한다.**
> Giữ nguyên các row.

---

## 2. Tại sao cần Window Function?

Ảnh đưa ví dụ:

```sql
SELECT EMPNO, ENAME, SAL, SUM(SAL) AS TOTAL
FROM EMP;
```

Câu này sai trong Oracle vì:

```text
EMPNO, ENAME, SAL → dữ liệu từng row
SUM(SAL)          → aggregate của nhiều row
```

Không thể đặt trực tiếp chúng cạnh nhau nếu không có cách grouping phù hợp.

---

### Cách 1 — Subquery
Phần này nối mạch SQL với “Cách 1 — Subquery”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
SELECT EMPNO,
       ENAME,
       SAL,
       (SELECT SUM(SAL) FROM EMP) AS TOTAL
FROM EMP;
```

Có thể làm được.

Nhưng Window Function đơn giản hơn:

```sql
SELECT EMPNO,
       ENAME,
       SAL,
       SUM(SAL) OVER() AS TOTAL
FROM EMP;
```

`OVER()` nghĩa là:

> áp dụng Window Function lên một window.

Không có `PARTITION BY` → toàn bộ tập row là một partition.

---

## 3. Cấu trúc Window Function ⭐⭐⭐

Dạng tổng quát:

```sql
WINDOW_FUNCTION(...) OVER (
    PARTITION BY ...
    ORDER BY ...
    ROWS | RANGE BETWEEN ... AND ...
)
```

Phải nhớ thứ tự:

```text
OVER (
    PARTITION BY
    ORDER BY
    ROWS / RANGE
)
```

Không được viết đảo:

```sql
OVER(
    ORDER BY SAL
    PARTITION BY DEPTNO
)
```

❌ Sai.

---

## 4. PARTITION BY

**KR:** `PARTITION BY`는 윈도우 연산을 수행할 그룹을 나눈다.
**VI:** `PARTITION BY` chia dữ liệu thành các nhóm độc lập để Window Function tính toán.

Có thể hình dung:

```text
PARTITION BY ≈ GROUP BY
```

nhưng khác biệt cực quan trọng:

> `GROUP BY` gom row.
> `PARTITION BY` **không gom row**.

Ví dụ:

```sql
SUM(SAL) OVER(PARTITION BY DEPTNO)
```

Nếu:

```text
DEPT 10
KING    5000
CLARK   2450
MILLER  1300

DEPT 20
SCOTT   3000
ADAMS   1100
```

thì:

```text
KING    10  5000 → 8750
CLARK   10  2450 → 8750
MILLER  10  1300 → 8750

SCOTT   20  3000 → 4100
ADAMS   20  1100 → 4100
```

Mỗi department là một **window partition** riêng.

---

## 5. ORDER BY bên trong OVER()

Đây không phải `ORDER BY` cuối query.

Ví dụ:

```sql
SUM(SAL) OVER(
    PARTITION BY DEPTNO
    ORDER BY SAL
)
```

`ORDER BY SAL` ở đây xác định:

> **thứ tự tính toán bên trong window.**

Trong khi:

```sql
SELECT ...
FROM EMP
ORDER BY SAL;
```

xác định:

> **thứ tự hiển thị kết quả cuối cùng.**

Hai thứ hoàn toàn khác nhau.

---

## 6. Aggregate Function dùng như Window Function

Các hàm:

```text
SUM
AVG
COUNT
MAX
MIN
```

có thể dùng với `OVER()`.

Ví dụ trong ảnh:

```sql
SELECT book_name,
       writer,
       publisher,
       price,
       SUM(price) OVER(
           PARTITION BY publisher
           ORDER BY price
       ) AS total
FROM BOOKSHELF;
```

Điểm quan trọng nằm ở `ORDER BY`.

---

## 7. SUM() + ORDER BY = cumulative sum

**KR:** 집계 윈도우 함수에서 ORDER BY를 사용하면 누적 연산이 발생할 수 있다.
**VI:** Khi Aggregate Window Function có `ORDER BY`, nó có thể trở thành phép tính **lũy kế**.

Ví dụ publisher `문학동네`:

```text
PRICE
13000
16000
```

kết quả:

```text
13000 → 13000
16000 → 29000
```

vì:

```text
row 1: 13000
row 2: 13000 + 16000
```

---

Nếu bỏ:

```sql
ORDER BY price
```

và chỉ:

```sql
SUM(price) OVER(PARTITION BY publisher)
```

thì cả hai row đều nhận:

```text
29000
29000
```

#### Nhớ
Phần này nối mạch SQL với “Nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
SUM(...) OVER(PARTITION BY A)
→ tổng toàn partition

SUM(...) OVER(PARTITION BY A ORDER BY B)
→ thường là cumulative sum theo B
```

---

## 8. AVG cũng tương tự

Ví dụ:

```text
PRICE
12000
13500
15200
```

với:

```sql
AVG(price) OVER(
    PARTITION BY publisher
    ORDER BY price
)
```

ta có:

```text
12000
→ 12000

13500
→ (12000 + 13500) / 2
→ 12750

15200
→ (12000 + 13500 + 15200) / 3
→ 13566.67
```

Đó là **cumulative average**.

---

## 9. Window Frame — ROWS / RANGE ⭐⭐⭐

Đây là phần cực dễ nhầm.

Cấu trúc:

```sql
ROWS BETWEEN A AND B
```

hoặc:

```sql
RANGE BETWEEN A AND B
```

Nó trả lời câu hỏi:

> **Từ row/value nào đến row/value nào được đưa vào phép tính hiện tại?**

Các keyword cần biết:

```text
UNBOUNDED PRECEDING
CURRENT ROW
n PRECEDING
n FOLLOWING
UNBOUNDED FOLLOWING
```

---

### Ý nghĩa

#### `UNBOUNDED PRECEDING`

**KR:** 파티션의 첫 행부터.
**VI:** Từ row đầu tiên của partition.

#### `CURRENT ROW`

**KR:** 현재 행까지.
**VI:** Đến row hiện tại.

#### `1 PRECEDING`

Row ngay trước.

#### `1 FOLLOWING`

Row ngay sau.

#### `UNBOUNDED FOLLOWING`

Row cuối cùng của partition.

---

## 10. ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
Phần này nối mạch SQL với “10. ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
SUM(SAL) OVER(
    ORDER BY SAL
    ROWS BETWEEN UNBOUNDED PRECEDING
             AND CURRENT ROW
)
```

Đọc:

> Tính tổng từ row đầu tiên → row hiện tại.

Giả sử:

```text
800
950
1100
1250
1250
1300
```

Kết quả:

```text
800   → 800
950   → 1750
1100  → 2850
1250  → 4100
1250  → 5350
1300  → 6650
```

Đặc biệt hai row `1250` được xử lý **từng row riêng biệt**.

Đây là đặc điểm của `ROWS`.

---

## 11. RANGE khác ROWS như thế nào? ⭐⭐⭐

Đây là phần cần hiểu thật chắc.

**KR:** ROWS는 물리적인 행을 기준으로 범위를 결정한다.
**VI:** `ROWS` xác định window dựa trên **từng row vật lý**.

**KR:** RANGE는 ORDER BY 값의 범위를 기준으로 계산하며 같은 값을 가진 행을 같은 범위로 취급할 수 있다.
**VI:** `RANGE` dựa trên **giá trị ORDER BY**, nên các row có cùng giá trị được coi như cùng một nhóm peer.

Ví dụ:

```text
SAL
800
950
1100
1250 ← WARD
1250 ← MARTIN
1300
```

---

### ROWS
Phần này nối mạch SQL với “ROWS”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
SUM(SAL) OVER(
    ORDER BY SAL
    ROWS BETWEEN UNBOUNDED PRECEDING
             AND CURRENT ROW
)
```

Kết quả:

```text
800   → 800
950   → 1750
1100  → 2850
1250  → 4100
1250  → 5350
1300  → 6650
```

Hai `1250` khác nhau.

---

### RANGE
Phần này nối mạch SQL với “RANGE”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
SUM(SAL) OVER(
    ORDER BY SAL
    RANGE BETWEEN UNBOUNDED PRECEDING
              AND CURRENT ROW
)
```

Hai row:

```text
1250
1250
```

được xem là cùng một peer group.

Do đó cả hai cùng:

```text
800 + 950 + 1100 + 1250 + 1250
= 5350
```

Kết quả:

```text
1250 → 5350
1250 → 5350
```

#### Câu nhớ

> **ROWS = 행을 본다 — nhìn ROW.**

> **RANGE = 값을 본다 — nhìn VALUE.**

Đây là cách nhớ rất hiệu quả cho SQLD.

---

## 12. Default frame rất quan trọng

Ảnh nhấn mạnh:

> 디폴트 범위가 RANGE라 같은 값을 가진 행은 같이 연산한다.

Khi có window `ORDER BY`, đối với nhiều aggregate analytic cases, frame mặc định về logic là:

```sql
RANGE BETWEEN UNBOUNDED PRECEDING
          AND CURRENT ROW
```

Vì vậy:

```sql
SUM(SAL) OVER(ORDER BY SAL)
```

với SAL trùng nhau có thể cho:

```text
1250 → 5350
1250 → 5350
```

chứ không phải:

```text
1250 → 4100
1250 → 5350
```

Muốn xử lý từng row:

```sql
ROWS BETWEEN UNBOUNDED PRECEDING
         AND CURRENT ROW
```

---

## 13. Toàn partition
Phần này nối mạch SQL với “13. Toàn partition”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
ROWS BETWEEN UNBOUNDED PRECEDING
         AND UNBOUNDED FOLLOWING
```

nghĩa là:

```text
row đầu tiên
      ↓
toàn bộ partition
      ↓
row cuối cùng
```

Ví dụ:

```sql
SUM(SAL) OVER(
    ORDER BY SAL
    ROWS BETWEEN UNBOUNDED PRECEDING
             AND UNBOUNDED FOLLOWING
)
```

Nếu tổng là `6650`, tất cả row:

```text
800  → 6650
950  → 6650
1100 → 6650
...
1300 → 6650
```

---

## 14. FOLLOWING

Ví dụ ảnh:

```sql
SUM(SAL) OVER(
    ORDER BY SAL
    ROWS BETWEEN UNBOUNDED PRECEDING
             AND 1 FOLLOWING
)
```

Tại row `950`:

```text
800   ← trước
950   ← current
1100  ← 1 following
```

nên:

```text
800 + 950 + 1100
= 2850
```

Cách đọc:

> từ row đầu tiên → thêm tới **1 row phía sau current row**.

---

## 15. LAG / LEAD ⭐⭐⭐

Hai hàm này dùng để lấy giá trị của row trước/sau mà không cần self join.

### LAG

**KR:** `LAG`는 현재 행보다 앞에 있는 행의 값을 가져온다.
**VI:** `LAG` lấy giá trị của **row trước**.

```sql
LAG(SAL) OVER(ORDER BY HIREDATE)
```

Hình dung:

```text
← LAG | CURRENT | LEAD →
```

---

### LEAD

**KR:** `LEAD`는 현재 행보다 뒤에 있는 행의 값을 가져온다.
**VI:** `LEAD` lấy giá trị của **row sau**.

```sql
LEAD(SAL) OVER(ORDER BY HIREDATE)
```

Ví dụ:

```text
HIREDATE       SAL    LEAD(SAL)

1981-02-20    1600      1250
1981-02-22    1250      1500
1981-09-08    1500      1350
1981-09-28    1350      NULL
```

Row cuối không còn row sau → `NULL`.

---

## 16. Cú pháp LAG/LEAD

Dạng quan trọng:

```sql
LAG(column, offset, default)
```

Ví dụ:

```sql
LAG(SAL, 2, 0)
```

nghĩa là:

> lấy SAL của **2 row phía trước**; nếu không tồn tại thì trả `0`.

Ví dụ:

```text
SAL

1000
2000
3000
4000
```

`LAG(SAL,2,0)`:

```text
1000 → 0
2000 → 0
3000 → 1000
4000 → 2000
```

#### Default

Nếu không viết offset:

```sql
LAG(SAL)
```

thì mặc định:

```text
offset = 1
```

---

## 17. Một bẫy trong ảnh: ORDER BY DEPTNO không có nghĩa partition

Ví dụ:

```sql
LAG(SAL) OVER(
    ORDER BY DEPTNO, SAL
)
```

Không có:

```sql
PARTITION BY DEPTNO
```

Vì vậy khi chuyển:

```text
DEPT 10
↓
DEPT 20
```

row đầu tiên của DEPT 20 vẫn có thể lấy SAL của row cuối DEPT 10.

Nếu muốn reset mỗi department:

```sql
LAG(SAL) OVER(
    PARTITION BY DEPTNO
    ORDER BY SAL
)
```

#### Nhớ

> `ORDER BY DEPTNO` ≠ `PARTITION BY DEPTNO`

`ORDER BY` chỉ sắp thứ tự.

`PARTITION BY` mới **chia nhóm/reset window**.

---

## 18. FIRST_VALUE ⭐⭐⭐

**KR:** 정해진 윈도우 범위에서 정렬 순서상 첫 번째 값을 반환한다.
**VI:** `FIRST_VALUE` trả về **giá trị đầu tiên theo thứ tự sắp xếp trong window**.

Ví dụ:

```sql
FIRST_VALUE(SAL)
OVER(
    PARTITION BY DEPTNO
    ORDER BY SAL
)
```

Nếu DEPT 10:

```text
1300
2450
5000
```

thì:

```text
1300 → 1300
2450 → 1300
5000 → 1300
```

Vì first value theo `SAL ASC` luôn là `1300`.

---

### Có thể lấy MAX bằng FIRST_VALUE
Phần này nối mạch SQL với “Có thể lấy MAX bằng FIRST_VALUE”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
FIRST_VALUE(SAL)
OVER(
    PARTITION BY DEPTNO
    ORDER BY SAL DESC
)
```

DESC:

```text
5000
2450
1300
```

First value = `5000`.

Vì vậy:

```text
FIRST_VALUE + ASC  → minimum
FIRST_VALUE + DESC → maximum
```

trong ngữ cảnh lấy SAL.

---

## 19. FIRST_VALUE không phải MIN

Đây là điểm cần hiểu.

```sql
MIN(SAL)
```

tìm **giá trị số nhỏ nhất**.

Trong khi:

```sql
FIRST_VALUE(ENAME)
OVER(ORDER BY SAL)
```

lấy **ENAME của row đứng đầu theo SAL**.

Ví dụ:

```text
ENAME   SAL
KING    5000
CLARK   2450
MILLER  1300
```

```sql
FIRST_VALUE(ENAME) OVER(ORDER BY SAL DESC)
```

→ `KING`.

Đây là thứ `MIN()` không thể biểu diễn trực tiếp theo cùng ý nghĩa.

---

## 20. LAST_VALUE — bẫy rất lớn ⭐⭐⭐

**KR:** `LAST_VALUE`는 현재 윈도우 범위에서 마지막 값을 반환한다.
**VI:** `LAST_VALUE` trả về **giá trị cuối cùng trong window hiện tại**.

Nhiều người nhìn:

```sql
LAST_VALUE(SAL) OVER(
    PARTITION BY DEPTNO
    ORDER BY SAL
)
```

và nghĩ:

> "Nó sẽ trả SAL lớn nhất."

Không nhất thiết.

---

### Vì sao?

Window frame mặc định với ORDER BY thường kết thúc tại:

```text
CURRENT ROW
```

Ví dụ:

```text
SAL
1300
2450
5000
```

Window của row 1300:

```text
[1300]
```

Last = `1300`.

Row 2450:

```text
[1300,2450]
```

Last = `2450`.

Row 5000:

```text
[1300,2450,5000]
```

Last = `5000`.

Nên:

```text
V1
1300
2450
5000
```

Trông gần như column SAL ban đầu.

---

## 21. Muốn LAST_VALUE thật sự lấy cuối partition

Phải mở window đến cuối:

```sql
LAST_VALUE(SAL) OVER(
    PARTITION BY DEPTNO
    ORDER BY SAL
    RANGE BETWEEN UNBOUNDED PRECEDING
              AND UNBOUNDED FOLLOWING
)
```

Bây giờ:

```text
SAL     LAST_VALUE

1300       5000
2450       5000
5000       5000
```

#### Câu cực quan trọng

> **LAST_VALUE + ORDER BY → luôn kiểm tra window frame.**

Đây là một trong những bẫy Window Function đáng nhớ nhất.

---

## 22. NTILE(N) ⭐⭐⭐

**KR:** `NTILE(N)`은 정렬된 행들을 N개의 그룹으로 나눈다.
**VI:** `NTILE(N)` chia các row đã được sắp xếp thành **N nhóm gần bằng nhau**.

```sql
NTILE(2) OVER(ORDER BY SAL)
```

→ chia thành 2 nhóm.

---

### Nếu không chia đều?

Ảnh đưa ví dụ:

```text
14 rows
NTILE(3)
```

14 / 3:

```text
4 dư 2
```

Hai nhóm đầu nhận thêm một row:

```text
Group 1 → 5
Group 2 → 5
Group 3 → 4
```

#### Quy tắc

> **Nhóm phía trước lớn hơn nếu có phần dư.**

Ví dụ:

```text
10 rows / 3 groups

4
3
3
```

Không phải:

```text
3
3
4
```

---

## 23. NTILE bắt buộc ORDER BY

Vì phải biết:

> row nào thuộc nhóm đầu, row nào thuộc nhóm sau.

```sql
NTILE(4) OVER(ORDER BY SAL DESC)
```

Có thể hiểu như chia:

```text
Top 25%
25~50%
50~75%
Bottom 25%
```

Nhưng đây là **chia số row**, không phải trực tiếp tính percentile thống kê.

---

## 24. RATIO_TO_REPORT ⭐⭐

**KR:** `RATIO_TO_REPORT`는 각 값이 파티션 전체 합계에서 차지하는 비율을 계산한다.
**VI:** `RATIO_TO_REPORT` tính tỷ lệ của giá trị hiện tại so với **tổng của partition**.

Công thức:

```text
current value
-----------------
SUM(partition)
```

Ví dụ:

```text
ALLEN    1600
WARD     1250
TURNER   1250
MARTIN   1500
```

Tổng:

```text
5600
```

Lưu ý: hình minh họa ghi mũi tên `1600 / 5000`, nhưng với chính bốn giá trị đang hiển thị thì tổng là `5600`; vì vậy nếu tính đúng theo các row đó, tỷ lệ của ALLEN là khoảng `0.2857`, làm tròn thành `0.29`.

```sql
RATIO_TO_REPORT(SAL) OVER()
```

→

```text
ALLEN:
1600 / 5600
≈ 0.29
```

Tổng tất cả ratio:

```text
≈ 1
= 100%
```

---

### PARTITION BY
Phần này nối mạch SQL với “PARTITION BY”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
RATIO_TO_REPORT(SAL)
OVER(PARTITION BY DEPTNO)
```

→ tỷ lệ SAL trong **department đó**.

Không có partition:

```sql
OVER()
```

→ tỷ lệ trên toàn bộ tập dữ liệu sau các bước lọc liên quan.

#### Điểm cần nhớ

Theo nội dung SQLD trong ảnh:

```text
RATIO_TO_REPORT
→ PARTITION BY được
→ ORDER BY không dùng
```

---

## 25. PERCENT_RANK ⭐⭐⭐

**KR:** `PERCENT_RANK`는 파티션 내에서 현재 행의 상대적인 순위 위치를 0~1 사이의 값으로 반환한다.
**VI:** `PERCENT_RANK` biểu diễn **vị trí xếp hạng tương đối** của row trong partition từ `0` đến `1`.

Công thức:

```text
RANK - 1
----------------
Total Rows - 1
```

hay:

```text
(rank - 1) / (n - 1)
```

---

Ví dụ 3 row:

```text
KING    5000
CLARK   2400
MILLER  1300
```

với:

```sql
PERCENT_RANK()
OVER(
    PARTITION BY DEPTNO
    ORDER BY SAL DESC
)
```

KING:

```text
(1-1)/(3-1)
= 0
```

CLARK:

```text
(2-1)/(3-1)
= 0.5
```

MILLER:

```text
(3-1)/(3-1)
= 1
```

---

## 26. PERCENT_RANK xử lý tie

Ví dụ:

```text
SAL
3000
3000
2975
1100
800
```

Rank:

```text
3000 → 1
3000 → 1
2975 → 3
1100 → 4
800  → 5
```

Do `RANK()` bỏ qua rank 2.

PERCENT_RANK:

```text
3000 → (1-1)/4 = 0
3000 → (1-1)/4 = 0
2975 → (3-1)/4 = 0.5
1100 → (4-1)/4 = 0.75
800  → (5-1)/4 = 1
```

Vậy tie có cùng `PERCENT_RANK`.

---

## 27. CUME_DIST ⭐⭐⭐

**KR:** `CUME_DIST`는 현재 행까지 포함된 행의 누적 비율을 반환한다.
**VI:** `CUME_DIST` trả về **tỷ lệ tích lũy của các row đến vị trí hiện tại theo ORDER BY**.

Có thể hiểu:

```text
số row đã đi qua tính cả peer/tie
--------------------------------
tổng số row trong partition
```

Kết quả:

```text
0 < CUME_DIST <= 1
```

Khác `PERCENT_RANK`:

```text
0 <= PERCENT_RANK <= 1
```

---

## 28. Ví dụ CUME_DIST

Có 3 row:

```text
5000
2400
1300
```

với:

```sql
ORDER BY SAL DESC
```

thì:

```text
5000 → 1/3 = 0.3333
2400 → 2/3 = 0.6667
1300 → 3/3 = 1
```

Đây chính là kết quả trong ảnh.

---

## 29. CUME_DIST và tie ⭐⭐⭐

Ví dụ:

```text
3000
3000
2975
1100
800
```

Có 5 row.

Hai `3000` bằng nhau.

Do đó cả hai được tính đến **cuối peer group**:

```text
3000 → 2/5 = 0.4
3000 → 2/5 = 0.4
```

Sau đó:

```text
2975 → 3/5 = 0.6
1100 → 4/5 = 0.8
800  → 5/5 = 1
```

Đây là điểm rất quan trọng.

---

## 30. PERCENT_RANK vs CUME_DIST ⭐⭐⭐

Lấy:

```text
3000
3000
2975
1100
800
```

#### PERCENT_RANK

Dựa trên:

```text
(RANK - 1) / (N - 1)
```

→

```text
3000 → 0
3000 → 0
2975 → 0.5
1100 → 0.75
800  → 1
```

#### CUME_DIST

Dựa trên tỷ lệ row tích lũy:

```text
3000 → 0.4
3000 → 0.4
2975 → 0.6
1100 → 0.8
800  → 1
```

#### Cách nhớ

> **PERCENT_RANK = 내 순위가 어디인가?**
> Rank của tôi nằm ở đâu?

> **CUME_DIST = 여기까지 몇 % 왔는가?**
> Đến vị trí này đã bao phủ bao nhiêu % row?

---

## 31. Đừng nhầm RANGE và CUME_DIST

Ảnh cuối nhắc lại:

> `RANGE` coi các row có cùng ORDER BY value là peer và tính cùng phạm vi.

Ví dụ:

```text
1250
1250
```

với cumulative `SUM` + RANGE có thể nhận cùng kết quả.

Nếu muốn tách từng row:

```sql
ROWS ...
```

hoặc có thể làm `ORDER BY` deterministic hơn:

```sql
ORDER BY SAL, EMPNO
```

khi phù hợp với mục đích nghiệp vụ.

---

## 32. Sơ đồ tổng hợp Window Function

Hãy hình dung câu:

```sql
SUM(SAL) OVER(
    PARTITION BY DEPTNO
    ORDER BY HIREDATE
    ROWS BETWEEN UNBOUNDED PRECEDING
             AND CURRENT ROW
)
```

theo 3 bước.

#### Bước 1 — PARTITION BY
Phần này nối mạch SQL với “Bước 1 — PARTITION BY”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
DEPT 10 | DEPT 20 | DEPT 30
```

Chia dữ liệu.

#### Bước 2 — ORDER BY

Trong mỗi department:

```text
old hire
↓
...
↓
new hire
```

Sắp thứ tự.

#### Bước 3 — ROWS

Ở mỗi current row:

```text
FIRST ROW ───────────── CURRENT ROW
        vùng được SUM
```

Sau đó chuyển sang row tiếp theo.

Đây là cách đọc Window Function dễ nhất:

> **PARTITION → ORDER → FRAME → CALCULATE**

---

## 33. Bảng phân loại các hàm trong ảnh
Phần này nối mạch SQL với “33. Bảng phân loại các hàm trong ảnh”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

| Hàm               | Ý nghĩa dễ nhớ                               | ORDER BY               |
| ----------------- | -------------------------------------------- | ---------------------- |
| `SUM/AVG/MAX/MIN` | tính toán trên window                        | tùy mục đích           |
| `LAG`             | nhìn về trước trong danh sách = previous row | cần để xác định thứ tự |
| `LEAD`            | nhìn về sau = next row                       | cần                    |
| `FIRST_VALUE`     | giá trị đầu window                           | thường cần             |
| `LAST_VALUE`      | giá trị cuối **frame hiện tại**              | thường cần             |
| `NTILE(N)`        | chia N nhóm                                  | **bắt buộc**           |
| `RATIO_TO_REPORT` | current / total                              | không ORDER BY         |
| `PERCENT_RANK`    | vị trí rank tương đối                        | **bắt buộc**           |
| `CUME_DIST`       | tỷ lệ row tích lũy                           | **bắt buộc**           |

---

## 🔥 SQLD NOTE — Phần phải thuộc

#### ① Bản chất
Phần này nối mạch SQL với “① Bản chất”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
GROUP BY
→ nhiều row → ít row

WINDOW FUNCTION
→ giữ nguyên row
→ tính toán giữa các row
```

#### ② Cấu trúc
Phần này nối mạch SQL với “② Cấu trúc”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
FUNCTION(...)
OVER(
    PARTITION BY ...
    ORDER BY ...
    ROWS/RANGE ...
)
```

Nhớ thứ tự:

```text
PARTITION
→ ORDER
→ ROWS/RANGE
```

#### ③ PARTITION BY
Phần này nối mạch SQL với “③ PARTITION BY”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
PARTITION BY ≈ chia group
```

nhưng:

```text
không làm mất row.
```

#### ④ Aggregate + ORDER BY
Phần này nối mạch SQL với “④ Aggregate + ORDER BY”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
SUM(SAL) OVER(ORDER BY ...)
```

→ thường tạo **누적합 / cumulative sum**.

#### ⑤ ROWS vs RANGE
Phần này nối mạch SQL với “⑤ ROWS vs RANGE”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
ROWS
→ xét từng ROW

RANGE
→ xét ORDER BY VALUE
→ cùng value → peer → có thể cùng kết quả
```

Đây là trọng tâm thi.

#### ⑥ Window frame
Phần này nối mạch SQL với “⑥ Window frame”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
UNBOUNDED PRECEDING
= từ đầu

CURRENT ROW
= row hiện tại

1 PRECEDING
= 1 row trước

1 FOLLOWING
= 1 row sau

UNBOUNDED FOLLOWING
= đến cuối
```

#### ⑦ LAG / LEAD
Phần này nối mạch SQL với “⑦ LAG / LEAD”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
LAG  ← CURRENT → LEAD
```

`LAG` = previous.

`LEAD` = next.

#### ⑧ FIRST_VALUE / LAST_VALUE
Phần này nối mạch SQL với “⑧ FIRST_VALUE / LAST_VALUE”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
FIRST_VALUE
→ đầu frame

LAST_VALUE
→ cuối frame
```

⚠️ `LAST_VALUE` đặc biệt phải kiểm tra **window frame**.

#### ⑨ NTILE
Phần này nối mạch SQL với “⑨ NTILE”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
NTILE(N)
→ chia N nhóm

14 rows / 3
→ 5 / 5 / 4
```

Phần dư được đưa cho **nhóm phía trước**.

#### ⑩ PERCENT_RANK
Phần này nối mạch SQL với “⑩ PERCENT_RANK”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
(RANK - 1)
------------
(N - 1)
```

Range:

```text
0 ≤ x ≤ 1
```

Row đứng đầu → `0`.

#### ⑪ CUME_DIST
Phần này nối mạch SQL với “⑪ CUME_DIST”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
cumulative rows (số dòng có giá trị <= giá trị hiện tại)
---------------------------------------------------------
total rows (tổng số dòng trong partition)
```

- Giá trị trả về: $0 < \text{CUME\_DIST} \le 1$.
- Dòng đầu tiên **không bao giờ bằng 0**.
- Dòng cuối cùng luôn bằng 1.
- Nếu có nhiều dòng đồng hạng (tie), tất cả các dòng đồng hạng đều nhận giá trị xác suất tích lũy lớn nhất của nhóm đồng hạng đó.

#### ⑫ RATIO_TO_REPORT
Phần này nối mạch SQL với “⑫ RATIO_TO_REPORT”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
giá trị của dòng hiện tại
--------------------------
SUM(giá trị) trong partition
```

- Trả về tỷ trọng đóng góp của dòng hiện tại so với tổng của partition (giá trị từ 0 đến 1).
- Lưu ý: Đây là hàm đặc thù rất nổi tiếng trong Oracle SQL.

---

## 34. So sánh bộ ba hàm xếp hạng: RANK vs DENSE_RANK vs ROW_NUMBER

Giả sử có bảng điểm thi của 5 sinh viên với số điểm: `100, 90, 90, 80, 70`.

```text
+--------+-------+---------------+--------------------+--------------------+
| Sinh viên | Điểm | RANK()        | DENSE_RANK()       | ROW_NUMBER()       |
+--------+-------+---------------+--------------------+--------------------+
| A      |   100 | 1             | 1                  | 1                  |
| B      |    90 | 2 (đồng hạng) | 2 (đồng hạng)      | 2 (thứ tự vật lý)  |
| C      |    90 | 2 (đồng hạng) | 2 (đồng hạng)      | 3 (thứ tự vật lý)  |
| D      |    80 | 4 (nhảy bậc!) | 3 (liên tục!)      | 4                  |
| E      |    70 | 5             | 4                  | 5                  |
+--------+-------+---------------+--------------------+--------------------+
```

- **`RANK()`:** Đồng hạng thì nhận cùng thứ hạng, nhưng thứ hạng kế tiếp **bị nhảy cóc** (1 $\rightarrow$ 2 $\rightarrow$ 2 $\rightarrow$ 4).
- **`DENSE_RANK()`:** Đồng hạng nhận cùng thứ hạng, nhưng thứ hạng kế tiếp **liên tục không nhảy cóc** (1 $\rightarrow$ 2 $\rightarrow$ 2 $\rightarrow$ 3).
- **`ROW_NUMBER()`:** Luôn gán số nguyên liên tục duy nhất tăng dần (1 $\rightarrow$ 2 $\rightarrow$ 3 $\rightarrow$ 4 $\rightarrow$ 5), không quan tâm giá trị có bằng nhau hay không.

---

## 35. So sánh khung cửa sổ vật lý ROWS vs logic RANGE khi có giá trị trùng lặp

Xét bảng dữ liệu có 4 nhân viên với mức lương: `1000, 2000, 2000, 3000`.

```sql
SELECT EMPNO, SAL,
       SUM(SAL) OVER(ORDER BY SAL ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS SUM_ROWS,
       SUM(SAL) OVER(ORDER BY SAL RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS SUM_RANGE
FROM EMP;
```

#### Kết quả thực tế (ASCII Table):

```text
+-------+------+----------+-----------+----------------------------------------------+
| EMPNO | SAL  | SUM_ROWS | SUM_RANGE | Giải thích cơ chế                            |
+-------+------+----------+-----------+----------------------------------------------+
|     1 | 1000 |     1000 |      1000 | Dòng đầu tiên                                |
|     2 | 2000 |     3000 |      5000 | ROWS: 1000+2000=3000                         |
|     3 | 2000 |     5000 |      5000 | RANGE: Gộp toàn bộ đồng hạng (1000+2000+2000)|
|     4 | 3000 |     8000 |      8000 | 5000 + 3000 = 8000                           |
+-------+------+----------+-----------+----------------------------------------------+
```

> **Điểm mấu chốt:** Khi có `ORDER BY` mà không khai báo tường minh khung cửa sổ, DBMS mặc định dùng `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`. Do đó, tại dòng thứ 2 (SAL = 2000), kết quả sẽ gộp luôn dòng thứ 3 (cũng có SAL = 2000) tạo thành `5000`!

---

## 36. Bảng ma trận so sánh Oracle vs SQL Server về Window Functions

| Nhóm hàm / Tính năng | Oracle Database | Microsoft SQL Server | Điểm khác biệt & Bẫy thi SQLD |
| :--- | :--- | :--- | :--- |
| **Xếp hạng:** `RANK`, `DENSE_RANK`, `ROW_NUMBER` | Hỗ trợ chuẩn ANSI | Hỗ trợ chuẩn ANSI | Cả hai DBMS hoàn toàn giống nhau về cú pháp và logic trả về. |
| **Chia nhóm:** `NTILE(n)` | Hỗ trợ chuẩn ANSI | Hỗ trợ chuẩn ANSI | Phân chia đều các hàng; phần dư được chia lần lượt từ nhóm 1 trở đi. |
| **Khung cửa sổ:** `ROWS` | Hỗ trợ đầy đủ | Hỗ trợ đầy đủ (từ SQL Server 2012+) | Khung vật lý theo số dòng cố định. |
| **Khung cửa sổ:** `RANGE` | Hỗ trợ đầy đủ | Giới hạn: Chỉ hỗ trợ `UNBOUNDED` và `CURRENT ROW` | Cả hai đều lấy `RANGE UNBOUNDED PRECEDING AND CURRENT ROW` làm mặc định khi có `ORDER BY`. |
| **Điều hướng:** `LAG`, `LEAD` | Hỗ trợ đầy đủ (từ Oracle 8i+) | Hỗ trợ đầy đủ (từ SQL Server 2012+) | Cú pháp: `LAG(col, offset, default_val) OVER(...)`. |
| **Đầu / Cuối:** `FIRST_VALUE`, `LAST_VALUE` | Hỗ trợ chuẩn ANSI | Hỗ trợ (từ SQL Server 2012+) | `LAST_VALUE` đòi hỏi phải mở rộng khung cửa sổ đến `UNBOUNDED FOLLOWING`. |
| **Tỷ trọng:** `RATIO_TO_REPORT` | **Có sẵn (Hàm tích hợp cực mạnh)** | **Không có sẵn** (phải tự tính bằng `val * 1.0 / SUM(val) OVER()`) | Xuất hiện rất nhiều trong đề thi Oracle SQLD. |
| **Phân phối:** `CUME_DIST`, `PERCENT_RANK` | Hỗ trợ chuẩn ANSI | Hỗ trợ (từ SQL Server 2012+) | Cả hai đều trả về kết quả số thực từ 0 đến 1. |

---

## 37. Cạm bẫy thi cử trọng điểm (출제 함정 & 오답 노트)

> [!WARNING]
> Dưới đây là 5 cạm bẫy chết người về Window Functions trong đề thi SQLD:

### Cạm bẫy 1: Cạm bẫy `LAST_VALUE` với khung cửa sổ mặc định
- **Tình huống:** Người dùng muốn tìm mức lương cao nhất trong phòng ban nên viết:
  ```sql
  SELECT ENAME, SAL, LAST_VALUE(SAL) OVER(PARTITION BY DEPTNO ORDER BY SAL) AS MAX_SAL
  FROM EMP;
  ```
- **Bẫy sai:** Nghĩ rằng `LAST_VALUE` sẽ trả về người có mức lương cao nhất trong phòng ban.
- **Thực tế:** Do có `ORDER BY SAL` mà không chỉ định khung cửa sổ, hệ thống tự động áp dụng mặc định: `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`.
- **Hậu quả:** Khung cửa sổ chỉ mở rộng đến đúng **dòng hiện tại**! Do đó, `LAST_VALUE(SAL)` trả về chính mức lương của dòng hiện tại (hoặc giá trị của bạn đồng hạng cuối cùng nếu có trùng điểm), hoàn toàn không lấy được cuối partition!
- **Cách viết đúng chuẩn:**
  ```sql
  LAST_VALUE(SAL) OVER(
      PARTITION BY DEPTNO
      ORDER BY SAL
      ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
  )
  ```

### Cạm bẫy 2: Dùng Window Function trực tiếp trong mệnh đề `WHERE` hoặc `HAVING`
- **Tình huống:** Viết truy vấn lấy Top 3 nhân viên lương cao nhất:
  ```sql
  -- LỖI CÚ PHÁP: ORA-30483: Window functions are not allowed here!
  SELECT ENAME, SAL
  FROM EMP
  WHERE RANK() OVER(ORDER BY SAL DESC) <= 3;
  ```
- **Bản chất kỹ thuật:** Trong thứ tự xử lý logic của câu lệnh SQL:
  `FROM` $\rightarrow$ `WHERE` $\rightarrow$ `GROUP BY` $\rightarrow$ `HAVING` $\rightarrow$ `SELECT (Window Functions)` $\rightarrow$ `ORDER BY`.
  Mệnh đề `WHERE` được lọc **trước** khi Window Function được tính toán trong `SELECT`!
- **Giải pháp:** Bắt buộc phải bọc Window Function vào **Inline View** hoặc **CTE (WITH clause)** rồi mới lọc ở ngoài:
  ```sql
  SELECT ENAME, SAL
  FROM (
      SELECT ENAME, SAL, RANK() OVER(ORDER BY SAL DESC) AS RNK
      FROM EMP
  )
  WHERE RNK <= 3;
  ```

### Cạm bẫy 3: Phân biệt giá trị đầu tiên của `PERCENT_RANK` vs `CUME_DIST`
- Công thức `PERCENT_RANK`: $\frac{\text{RANK} - 1}{N - 1}$. Dòng đầu tiên có $\text{RANK} = 1$, do đó: $\frac{1 - 1}{N - 1} = 0$.
  $\rightarrow$ **`PERCENT_RANK` của dòng đầu tiên luôn luôn bằng 0!**
- Công thức `CUME_DIST`: $\frac{\text{Số dòng có giá trị} \le \text{giá trị hiện tại}}{N}$. Dòng đầu tiên có ít nhất 1 dòng thỏa mãn, do đó giá trị tối thiểu là $\frac{1}{N} > 0$.
  $\rightarrow$ **`CUME_DIST` của dòng đầu tiên tuyệt đối không bao giờ bằng 0!**

### Cạm bẫy 4: Thuật toán chia nhóm của `NTILE(n)` khi không chia hết
- Nếu bảng có $M$ dòng chia thành $N$ nhóm: Mỗi nhóm cơ bản có $\lfloor M / N \rfloor$ dòng. Số dư $R = M \pmod N$ sẽ được phân bổ **mỗi nhóm 1 dòng, bắt đầu từ nhóm 1 trở đi**.
- **Ví dụ:** Có 14 dòng chia `NTILE(4)`:
  - $14 / 4 = 3$ dư $2$.
  - Nhóm 1 nhận thêm 1: $3 + 1 = 4$ dòng.
  - Nhóm 2 nhận thêm 1: $3 + 1 = 4$ dòng.
  - Nhóm 3 nhận $3$ dòng.
  - Nhóm 4 nhận $3$ dòng.
  $\rightarrow$ Kết quả phân bổ: `4, 4, 3, 3` (tuyệt đối không phải `3, 3, 4, 4` hay `4, 3, 4, 3`).

### Cạm bẫy 5: Giá trị mặc định của `LAG` và `LEAD` khi trỏ ra ngoài biên
- `LAG(col)` trên dòng đầu tiên hoặc `LEAD(col)` trên dòng cuối cùng sẽ trả về `NULL` nếu không khai báo tham số thứ 3.
- Cú pháp an toàn: `LAG(SAL, 1, 0) OVER(...)` $\rightarrow$ Nếu vượt biên, tự động trả về giá trị `0` thay vì `NULL`.

---

## 38. Câu hỏi trắc nghiệm thi thử mô phỏng (실전 기출 변형 문제 & 정답 해설)

### Câu 1: Xác định kết quả xếp hạng khi có điểm đồng hạng (Độ khó: Dễ)
Bảng điểm thi `TB_SCORE` có cột điểm số `SCORE` của 6 thí sinh như sau: `100, 95, 95, 90, 85, 85`.
Xét câu lệnh SQL sau:

```sql
SELECT SCORE,
       RANK() OVER(ORDER BY SCORE DESC) AS R1,
       DENSE_RANK() OVER(ORDER BY SCORE DESC) AS R2,
       ROW_NUMBER() OVER(ORDER BY SCORE DESC) AS R3
FROM TB_SCORE;
```

Tại thí sinh có mức điểm `SCORE = 90`, giá trị của `(R1, R2, R3)` lần lượt là bao nhiêu?

A. `(4, 3, 4)`
B. `(3, 3, 4)`
C. `(4, 4, 4)`
D. `(3, 2, 4)`

> **Đáp án chính xác:** **A**
>
> **Giải thích chi tiết từng lựa chọn:**
> - Điểm số sắp xếp giảm dần:
>   - Điểm 100 (1 người): `RANK = 1`, `DENSE_RANK = 1`, `ROW_NUMBER = 1`.
>   - Điểm 95 (2 người): Cả hai đều có `RANK = 2`, `DENSE_RANK = 2`; `ROW_NUMBER` lần lượt là `2` và `3`.
>   - Điểm 90 (1 người tiếp theo):
>     - `RANK()`: Do trước đó có 2 người xếp hạng 2 nên thứ hạng bị nhảy cóc bỏ qua số 3, nhảy thẳng lên **4**.
>     - `DENSE_RANK()`: Thứ hạng không nhảy cóc, tiếp nối liền kề là **3**.
>     - `ROW_NUMBER()`: Tiếp tục đếm dòng thứ **4**.
> - Vì vậy tại `SCORE = 90`, bộ giá trị `(R1, R2, R3)` chính là `(4, 3, 4)`.
> - **Lựa chọn A:** Hoàn toàn chính xác.
> - **Lựa chọn B sai:** Nhầm rằng RANK không nhảy cóc.
> - **Lựa chọn C sai:** Nhầm rằng DENSE_RANK nhảy cóc như RANK.
> - **Lựa chọn D sai:** Nhầm lẫn thứ tự đánh số của DENSE_RANK.

---

### Câu 2: Cạm bẫy khung cửa sổ mặc định của LAST_VALUE (Độ khó: Cao)
Xét bảng nhân viên `EMP` có 3 nhân viên trong phòng ban 10 với mức lương được sắp xếp tăng dần:
`MILLER (1300), CLARK (2450), KING (5000)`.
Người dùng thực thi câu truy vấn sau:

```sql
SELECT ENAME, SAL,
       LAST_VALUE(SAL) OVER(ORDER BY SAL) AS LV_SAL
FROM EMP
WHERE DEPTNO = 10;
```

Giá trị của cột `LV_SAL` hiển thị tại dòng của nhân viên `CLARK` là bao nhiêu?

A. `5000`
B. `2450`
C. `1300`
D. `NULL`

> **Đáp án chính xác:** **B**
>
> **Giải thích chi tiết từng lựa chọn:**
> - **Phân tích bẫy:** Đây là bẫy kinh điển số 1 của hàm `LAST_VALUE`.
> - Khi mệnh đề `OVER()` có `ORDER BY` nhưng không chỉ định mệnh đề `ROWS/RANGE`, Oracle sẽ tự động kích hoạt khung cửa sổ mặc định:
>   `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`.
> - Điều này có nghĩa là tại bất kỳ dòng nào, khung cửa sổ tính toán chỉ kéo dài từ dòng đầu tiên đến **đúng dòng hiện tại** (`CURRENT ROW`).
> - Tại dòng của `CLARK (2450)`:
>   - Khung cửa sổ chỉ bao gồm 2 dòng: `MILLER (1300)` và `CLARK (2450)`.
>   - Do đó, giá trị cuối cùng (`LAST_VALUE`) của khung cửa sổ này chính là **2450**!
> - Nhân viên `KING (5000)` nằm ở phía sau nên chưa lọt vào khung cửa sổ tính toán của dòng `CLARK`.
> - **Lựa chọn B:** Hoàn toàn chính xác (2450).
> - **Lựa chọn A sai:** Bẫy thường gặp của người học tưởng rằng LAST_VALUE tự động quét tới cuối bảng để lấy mức lương cao nhất (5000).

---

### Câu 3: Thuật toán chia nhóm NTILE khi có phần dư (Độ khó: Trung bình)
Bảng `TB_STUDENT` có tổng cộng 11 sinh viên. Người quản trị muốn phân loại sinh viên thành 3 nhóm học lực bằng câu lệnh sau:

```sql
SELECT STUDENT_ID,
       NTILE(3) OVER(ORDER BY SCORE DESC) AS GROUP_NUM
FROM TB_STUDENT;
```

Số lượng sinh viên thuộc các nhóm `1, 2, 3` lần lượt là bao nhiêu?

A. Nhóm 1 có 3 người, Nhóm 2 có 4 người, Nhóm 3 có 4 người.
B. Nhóm 1 có 4 người, Nhóm 2 có 3 người, Nhóm 3 có 4 người.
C. Nhóm 1 có 4 người, Nhóm 2 có 4 người, Nhóm 3 có 3 người.
D. Nhóm 1 có 3 người, Nhóm 2 có 3 người, Nhóm 3 có 5 người.

> **Đáp án chính xác:** **C**
>
> **Giải thích chi tiết từng lựa chọn:**
> - Phép chia: $11 / 3 = 3$ dư $2$.
> - Theo chuẩn thuật toán ANSI SQL của `NTILE`:
>   - Ban đầu mỗi nhóm được chia tối thiểu 3 sinh viên.
>   - Số dư 2 sinh viên sẽ được phân bổ ưu tiên lần lượt cho các nhóm từ đầu tiên:
>     - Nhóm 1 nhận thêm 1 $\rightarrow 3 + 1 = 4$ sinh viên.
>     - Nhóm 2 nhận thêm 1 $\rightarrow 3 + 1 = 4$ sinh viên.
>     - Nhóm 3 không nhận thêm $\rightarrow 3$ sinh viên.
> - Kết quả phân bổ chính xác: `Nhóm 1 = 4, Nhóm 2 = 4, Nhóm 3 = 3`.
> - **Lựa chọn C:** Hoàn toàn chính xác.
> - **Lựa chọn A, B, D sai:** Vi phạm quy tắc phân bổ phần dư từ nhóm đầu tiên.

---

### Câu 4: Tính toán giá trị PERCENT_RANK và CUME_DIST (Độ khó: Trung bình)
Bảng `TB_DATA` gồm 4 dòng dữ liệu có giá trị cột `VAL` lần lượt là: `10, 20, 20, 30`.
Thực thi câu truy vấn sau:

```sql
SELECT VAL,
       PERCENT_RANK() OVER(ORDER BY VAL) AS PR,
       CUME_DIST() OVER(ORDER BY VAL) AS CD
FROM TB_DATA;
```

Tại dòng thứ 2 (dòng đầu tiên có `VAL = 20`), cặp giá trị `(PR, CD)` hiển thị là bao nhiêu?

A. `PR = 0.333, CD = 0.500`
B. `PR = 0.333, CD = 0.750`
C. `PR = 0.250, CD = 0.750`
D. `PR = 0.500, CD = 0.500`

> **Đáp án chính xác:** **B**
>
> **Giải thích chi tiết từng lựa chọn:**
> - Tổng số dòng $N = 4$.
> - Dãy giá trị đã sắp xếp:
>   - Dòng 1: `VAL = 10` $\rightarrow \text{RANK} = 1$.
>   - Dòng 2: `VAL = 20` $\rightarrow \text{RANK} = 2$.
>   - Dòng 3: `VAL = 20` $\rightarrow \text{RANK} = 2$.
>   - Dòng 4: `VAL = 30` $\rightarrow \text{RANK} = 4$.
> - **Tính `PERCENT_RANK` tại dòng `VAL = 20`:**
>   $$\text{PR} = \frac{\text{RANK} - 1}{N - 1} = \frac{2 - 1}{4 - 1} = \frac{1}{3} \approx 0.333$$
> - **Tính `CUME_DIST` tại dòng `VAL = 20`:**
>   - Đếm số dòng có giá trị $\le 20$: có 3 dòng (gồm dòng 10, dòng 20 thứ nhất, dòng 20 thứ hai).
>   $$\text{CD} = \frac{\text{Số dòng} \le 20}{N} = \frac{3}{4} = 0.750$$
> - Cặp giá trị thu được là: `PR = 0.333, CD = 0.750`.
> - **Lựa chọn B:** Hoàn toàn chính xác.
> - **Lựa chọn A sai:** Nhầm tưởng CUME_DIST chỉ đếm đến dòng thứ 2 (bỏ qua dòng đồng hạng thứ 3).
> - **Lựa chọn C, D sai:** Tính sai công thức mẫu số hoặc bậc xếp hạng của PERCENT_RANK.
