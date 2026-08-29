# TOP-N và Pagination

> **Mục tiêu:** ROWNUM, ROW_NUMBER/RANK/DENSE_RANK, FETCH/OFFSET, TOP và WITH TIES.

## Từ khóa cần nhớ (Keyword)

Các thuật ngữ SQLD được giữ nguyên tiếng Hàn/English trong phần nguồn. Khi ghi chú, dùng mẫu `용어 (English) (Tiếng Việt)` để nối tên gọi trong đề với ý nghĩa thực tế.

## Mạch tư duy (Logic học)

Hãy xác định **đối tượng dữ liệu** trước, sau đó đọc **điều kiện**, **phạm vi dòng**, **thứ tự xử lý** và cuối cùng kiểm tra **kết quả mong đợi**. Với SQL, luôn phân biệt điều kiện lọc trước nhóm (`WHERE`) với điều kiện lọc sau nhóm (`HAVING`).

> **Cách học:** Đọc phần khái niệm → tự chạy lại các ví dụ SQL → chốt lại các mục `Keyword`, bảng so sánh và phần ghi nhớ cuối bài.

---

## 1. TOP-N Query là gì?

**KR:** TOP-N 쿼리는 전체 결과에서 상위 N개의 행을 추출하는 쿼리이다.
**VI:** TOP-N Query dùng để lấy **N dòng đứng đầu** từ toàn bộ tập kết quả.

Ví dụ:

```text
Top 3 người có lương cao nhất
Top 5 sản phẩm bán chạy nhất
Top 10 sinh viên có điểm cao nhất
```

Nó cũng thường được dùng để xử lý **paging / pagination**.

Ví dụ:

```text
Page 1 → row 1~10
Page 2 → row 11~20
Page 3 → row 21~30
```

---

## 2. Các cách làm TOP-N trong phần này

Trong ảnh có 4 cách chính:

```text
1. ROWNUM       → Oracle kiểu cũ
2. RANK()       → Window Function
3. FETCH/OFFSET → Oracle 12c+ / chuẩn hiện đại
4. TOP N        → SQL Server
```

Trước hết phải hiểu `ROWNUM`, vì đây là phần dễ nhầm nhất.

## 3. ROWNUM là gì? ⭐⭐⭐

**KR:** ROWNUM은 출력되는 행에 순차적으로 부여되는 가상의 행 번호이다.
**VI:** `ROWNUM` là **số thứ tự giả** được Oracle gán cho các row khi chúng được lấy ra.

Ví dụ:

```sql
SELECT ROWNUM,
       EMPNO,
       ENAME,
       SAL
FROM EMP
WHERE SAL >= 1500;
```

Có thể ra:

```text
ROWNUM  ENAME   SAL
1       ALLEN   1600
2       JONES   2975
3       BLAKE   2850
4       CLARK   2450
...
```

Điểm quan trọng:

> `ROWNUM` không phải một column thật được lưu trong bảng.

Nó là:

```text
가상 컬럼 / pseudocolumn
```

hay:

```text
pseudo column
```

---

## 4. ROWNUM không phải số thứ tự cố định

**KR:** ROWNUM은 절대적인 행 번호가 아니다.
**VI:** `ROWNUM` **không phải ID cố định của row**.

Ví dụ cùng một row `KING` có thể hôm nay nhận:

```text
ROWNUM = 5
```

nhưng query khác lại nhận:

```text
ROWNUM = 1
```

vì `ROWNUM` phụ thuộc vào **thứ tự row được query xử lý**.

Nó khác với:

```text
EMPNO
ID
PK
```

vốn là giá trị dữ liệu thật.

## 5. Bẫy lớn nhất: ROWNUM + ORDER BY ⭐⭐⭐

Giả sử bạn muốn:

> Top 3 người có SAL cao nhất.

Một người mới học thường viết:

```sql
SELECT ENAME, SAL
FROM EMP
WHERE ROWNUM <= 3
ORDER BY SAL DESC;
```

Nhìn có vẻ đúng.

Nhưng logic thực tế là:

```text
1. lấy 3 row trước
2. sau đó mới ORDER BY SAL DESC
```

Tức là:

```text
không phải Top 3 SAL cao nhất
```

mà là:

```text
3 row được lấy trước
→ rồi mới sort 3 row đó theo SAL
```

---

## 6. Vì sao?

Theo logic liên quan đến query này:

```text
FROM
↓
WHERE
↓
ROWNUM được áp dụng trong quá trình row vượt qua WHERE
↓
SELECT
↓
ORDER BY
```

Cho nên:

```sql
WHERE ROWNUM <= 3
```

đã giới hạn row **trước khi final ORDER BY thực hiện**.

Ảnh nhấn mạnh:

**KR:** WHERE 절이 ORDER BY 절보다 먼저 수행된다.
**VI:** `WHERE` được xử lý trước `ORDER BY`.

---

## 7. Cách đúng: sort trước bằng Inline View ⭐⭐⭐

Muốn lấy Top 3 SAL:

```sql
SELECT ENAME, SAL
FROM (
    SELECT ENAME, SAL
    FROM EMP
    ORDER BY SAL DESC
)
WHERE ROWNUM <= 3;
```

Cách suy luận:

```text
INNER QUERY
↓
ORDER BY SAL DESC

KING   5000
SCOTT  3000
FORD   3000
JONES  2975
...

OUTER QUERY
↓
ROWNUM <= 3

KING
SCOTT
FORD
```

Điểm phải nhớ:

> **먼저 정렬 → 그 다음 ROWNUM**

> **Sort trước → sau đó mới gán/lọc ROWNUM.**

---

## 8. Inline View là gì?

```sql
FROM (
    SELECT ...
)
```

Subquery nằm trong `FROM` gọi là:

```text
Inline View
```

Ở đây Inline View đóng vai trò như một bảng tạm logic:

```sql
SELECT ENAME, SAL
FROM EMP
ORDER BY SAL DESC
```

Sau khi dữ liệu đã được sắp xếp, outer query mới lấy:

```sql
ROWNUM <= 3
```

---

## 9. Tại sao `ROWNUM <= N` được nhưng `ROWNUM > N` có vấn đề? ⭐⭐⭐

Đây là bẫy SQLD cực hay hỏi.

Ví dụ:

```sql
SELECT *
FROM EMP
WHERE ROWNUM <= 3;
```

✅ Chạy bình thường.

Nhưng:

```sql
SELECT *
FROM EMP
WHERE ROWNUM > 3;
```

❌ Không trả kết quả như bạn tưởng.

Tại sao?

---

## 10. Cơ chế gán ROWNUM

Oracle lấy row đầu tiên.

Nó thử gán:

```text
ROWNUM = 1
```

Sau đó check:

```sql
ROWNUM > 3
```

false.

Row đó bị loại.

Tiếp theo Oracle lấy row khác.

Nhưng vì chưa row nào được accept nên row mới lại được xét như:

```text
ROWNUM = 1
```

lại false.

Cứ thế:

```text
1 > 3 ❌
1 > 3 ❌
1 > 3 ❌
...
```

Không bao giờ tới:

```text
ROWNUM = 4
```

---

## 11. Quy tắc nhớ cực quan trọng

Các điều kiện dạng:

```sql
ROWNUM = 1
ROWNUM <= 5
ROWNUM < 10
```

có thể dùng.

Nhưng dạng khởi đầu yêu cầu:

```sql
ROWNUM > 1
ROWNUM >= 2
ROWNUM BETWEEN 4 AND 6
```

không hoạt động theo cách bạn kỳ vọng nếu áp dụng trực tiếp.

---

## 12. Ví dụ sai: lấy rank 4~6

```sql
SELECT ENAME, SAL
FROM (
    SELECT *
    FROM EMP
    ORDER BY SAL DESC
)
WHERE ROWNUM BETWEEN 4 AND 6;
```

Bạn muốn:

```text
4
5
6
```

nhưng Oracle bắt đầu:

```text
ROWNUM = 1
```

check:

```text
1 BETWEEN 4 AND 6
```

false.

Và lại mắc vào vấn đề như trên.

---

## 13. Cách đúng để lấy row 4~6 bằng ROWNUM

Phải tạo một tầng trung gian và **biến ROWNUM thành column thật của inline view**:

```sql
SELECT ENAME, SAL
FROM (
    SELECT ROWNUM AS RN,
           A.*
    FROM (
        SELECT ENAME, SAL
        FROM EMP
        ORDER BY SAL DESC
    ) A
    WHERE ROWNUM <= 6
)
WHERE RN >= 4;
```

Đây là pattern cổ điển Oracle paging.

Logic:

```text
Bước 1:
ORDER BY SAL DESC

Bước 2:
gán ROWNUM
1
2
3
4
5
6

Bước 3:
lưu ROWNUM thành RN

Bước 4:
outer query:
RN >= 4
```

→ lấy:

```text
4,5,6
```

---

## 14. Tại sao alias RN giải quyết được?

Trong:

```sql
SELECT ROWNUM AS RN, A.*
```

`RN` trở thành output column của inline view.

Outer query nhìn nó như một giá trị dữ liệu bình thường:

```sql
WHERE RN BETWEEN 4 AND 6
```

Lúc này không còn đang filter trực tiếp pseudocolumn `ROWNUM` trong cùng level nữa.

Đây là điểm bản chất.

## 15. ROWNUM và ROW_NUMBER() khác nhau ⭐⭐⭐

Rất dễ nhầm tên.

### ROWNUM

Oracle pseudocolumn:

```sql
ROWNUM
```

* không cần `OVER`
* được gán trong quá trình query
* phụ thuộc query execution
* thường dùng legacy TOP-N/paging

### ROW_NUMBER()

Window Function:

```sql
ROW_NUMBER() OVER(ORDER BY SAL DESC)
```

* là analytic/window function
* có `ORDER BY` rõ ràng
* tạo số thứ tự theo ranking criteria

Ví dụ:

```sql
SELECT ENAME,
       SAL,
       ROW_NUMBER() OVER(ORDER BY SAL DESC) AS RN
FROM EMP;
```

→

```text
KING   5000   1
SCOTT  3000   2
FORD   3000   3
JONES  2975   4
...
```

Đừng bao giờ coi hai cái giống nhau.

## 16. RANK() ⭐⭐⭐

Ảnh tiếp theo dùng:

```sql
RANK() OVER(ORDER BY SAL DESC)
```

**KR:** 동일한 값에는 동일한 순위를 부여하고 다음 순위는 건너뛴다.
**VI:** `RANK()` cho **cùng hạng nếu giá trị bằng nhau**, và thứ hạng tiếp theo sẽ bị nhảy.

Ví dụ:

```text
SAL
5000
3000
3000
2975
```

`RANK()`:

```text
5000 → 1
3000 → 2
3000 → 2
2975 → 4
```

Không có rank 3.

---

## 17. Dùng RANK để lấy thứ hạng

```sql
SELECT ENAME, SAL
FROM (
    SELECT ENAME,
           SAL,
           RANK() OVER(ORDER BY SAL DESC) AS RN
    FROM EMP
)
WHERE RN BETWEEN 4 AND 6;
```

Điểm hay hơn `ROWNUM`:

`RN` ở đây là ranking logic theo `SAL`, không phải vị trí row tùy thời điểm.

---

## 18. Nhưng RANK có thể trả nhiều hơn N row

Giả sử:

```text
KING   5000
SCOTT  3000
FORD   3000
```

Rank:

```text
KING   → 1
SCOTT  → 2
FORD   → 2
```

Nếu nói:

```sql
WHERE RN <= 2
```

thì kết quả có:

```text
3 rows
```

vì rank 2 có hai người.

Đây là khác biệt rất quan trọng:

> **Top N rows** ≠ **Top N ranks**

---

## 19. RANK vs ROW_NUMBER vs DENSE_RANK

Mặc dù ảnh chỉ nhắc `RANK`, nên mở rộng chỗ này vì SQLD thường hỏi chung.

Dữ liệu:

```text
SAL
5000
3000
3000
2975
```

#### ROW_NUMBER

```text
1
2
3
4
```

Không quan tâm tie, mỗi row một số.

#### RANK

```text
1
2
2
4
```

Có tie → nhảy hạng.

#### DENSE_RANK

```text
1
2
2
3
```

Có tie → **không nhảy hạng**.

Công thức nhớ:

```text
ROW_NUMBER → mỗi row 1 số khác nhau

RANK       → cùng giá trị cùng hạng + có gap

DENSE_RANK → cùng giá trị cùng hạng + không gap
```

## 20. FETCH — cách hiện đại hơn ⭐⭐⭐

Từ Oracle 12c trở lên có thể dùng Row Limiting Clause:

```sql
SELECT EMPNO, ENAME, JOB, SAL
FROM EMP
ORDER BY SAL DESC
FETCH FIRST 5 ROWS ONLY;
```

Nghĩa là:

> sort SAL DESC rồi lấy 5 row đầu tiên.

Rất dễ đọc.

---

## 21. Cấu trúc FETCH/OFFSET

Dạng tổng quát:

```sql
SELECT ...
FROM ...
WHERE ...
GROUP BY ...
HAVING ...
ORDER BY ...
OFFSET N ROWS
FETCH FIRST M ROWS ONLY;
```

Hoặc:

```sql
FETCH NEXT M ROWS ONLY
```

Điểm cần nhớ:

```text
ORDER BY
↓
OFFSET
↓
FETCH
```

---

## 22. OFFSET

```sql
OFFSET 3 ROWS
```

nghĩa là:

> bỏ qua 3 row đầu tiên.

Ví dụ đã sort:

```text
1 KING
2 SCOTT
3 FORD
4 JONES
5 BLAKE
6 CLARK
```

```sql
OFFSET 3 ROWS
```

bỏ:

```text
1
2
3
```

bắt đầu từ:

```text
4
```

---

## 23. OFFSET + FETCH

Ảnh có:

```sql
SELECT EMPNO, ENAME, JOB, SAL
FROM EMP
ORDER BY SAL DESC
OFFSET 3 ROWS
FETCH FIRST 3 ROWS ONLY;
```

Logic:

```text
ORDER BY SAL DESC
↓
skip 3 rows
↓
take next 3 rows
```

Kết quả:

```text
rank position 4
rank position 5
rank position 6
```

Lưu ý ở đây nói vị trí row sau sort, chưa chắc là `RANK()` 4,5,6 nếu có tie.

---

## 24. FIRST và NEXT trong FETCH

Có thể gặp:

```sql
FETCH FIRST 5 ROWS ONLY
```

hoặc:

```sql
FETCH NEXT 5 ROWS ONLY
```

Trong ngữ cảnh row limiting:

* `FIRST` thường dùng khi lấy từ đầu
* `NEXT` thường dùng sau `OFFSET`

Ví dụ:

```sql
OFFSET 10 ROWS
FETCH NEXT 10 ROWS ONLY
```

rất tự nhiên cho pagination.

---

## 25. ROW và ROWS

Có thể gặp:

```sql
OFFSET 1 ROW
```

hoặc:

```sql
OFFSET 5 ROWS
```

Tương tự:

```sql
FETCH FIRST 1 ROW ONLY
FETCH FIRST 5 ROWS ONLY
```

Về ý nghĩa, `ROW/ROWS` chỉ khác số ít/số nhiều về cách viết.

---

## 26. Pagination bằng OFFSET/FETCH

Ví dụ page size = 10.

### Page 1

```sql
OFFSET 0 ROWS
FETCH NEXT 10 ROWS ONLY
```

→ row 1~10.

### Page 2

```sql
OFFSET 10 ROWS
FETCH NEXT 10 ROWS ONLY
```

→ row 11~20.

### Page 3

```sql
OFFSET 20 ROWS
FETCH NEXT 10 ROWS ONLY
```

→ row 21~30.

Công thức:

```text
OFFSET = (page - 1) × page_size
```

Ví dụ page 4, size 20:

```text
OFFSET
= (4 - 1) × 20
= 60
```

sau đó:

```sql
FETCH NEXT 20 ROWS ONLY
```

## 27. FETCH vẫn nên có ORDER BY

Nếu bạn viết:

```sql
SELECT *
FROM EMP
FETCH FIRST 5 ROWS ONLY;
```

DB có thể trả 5 row đầu theo cách execution hiện tại.

Nhưng nếu yêu cầu:

> top 5 lương cao nhất

thì bắt buộc logic:

```sql
ORDER BY SAL DESC
FETCH FIRST 5 ROWS ONLY
```

Không `ORDER BY` thì khái niệm "top" không có tiêu chí xác định.

## 28. SQL Server TOP N

Trong SQL Server:

```sql
SELECT TOP 2
       ENAME,
       SAL
FROM EMP
ORDER BY SAL DESC;
```

→ lấy 2 row đầu tiên sau sort.

Ví dụ:

```text
KING   5000
SCOTT  3000
```

---

## 29. TOP đặt ở đâu?

SQL Server syntax:

```sql
SELECT TOP N column1, column2
FROM table
ORDER BY ...
```

Khác `FETCH`:

```sql
SELECT ...
FROM ...
ORDER BY ...
FETCH ...
```

Vì vậy nhớ vị trí:

```text
TOP   → gần SELECT

FETCH → sau ORDER BY
```

---

## 30. TOP N WITH TIES ⭐⭐⭐

Ảnh có:

```sql
SELECT TOP 2 WITH TIES
       ENAME,
       SAL
FROM EMP
ORDER BY SAL DESC;
```

Dữ liệu:

```text
KING   5000
SCOTT  3000
FORD   3000
JONES  2975
```

Nếu chỉ:

```sql
TOP 2
```

→ có thể:

```text
KING
SCOTT
```

Nhưng:

```sql
TOP 2 WITH TIES
```

thì row thứ 2 có:

```text
SAL = 3000
```

FORD cũng `3000`.

Do đó kết quả:

```text
KING   5000
SCOTT  3000
FORD   3000
```

Tức:

> **WITH TIES giữ thêm các row đồng hạng với boundary row.**

---

## 31. WITH TIES giống tư duy RANK

Ví dụ:

```text
KING   5000 → rank 1
SCOTT  3000 → rank 2
FORD   3000 → rank 2
```

`TOP 2 WITH TIES` gần với ý nghĩa:

```text
lấy tất cả row có rank nằm trong top boundary
```

nên trả 3 row.

---

## 32. Một bẫy: TOP N không đảm bảo N row nếu WITH TIES

```sql
TOP 2
```

→ tối đa 2 row theo limit.

Nhưng:

```sql
TOP 2 WITH TIES
```

có thể:

```text
2 rows
3 rows
4 rows
...
```

tùy tie tại vị trí thứ N.

## 33. So sánh 4 phương pháp

| Phương pháp    | DB/đặc điểm                     |                Tie |            Paging |
| -------------- | ------------------------------- | -----------------: | ----------------: |
| `ROWNUM`       | Oracle legacy                   |     không tự xử lý | có nhưng phức tạp |
| `RANK()`       | Window Function                 |      giữ cùng rank |            có thể |
| `FETCH/OFFSET` | Oracle 12c+, SQL chuẩn hiện đại |  mặc định theo row |          rất tiện |
| `TOP N`        | SQL Server                      | `WITH TIES` hỗ trợ |       chủ yếu top |

---

## 34. TOP 3 rows vs TOP 3 ranks

Giả sử:

```text
SAL
5000
3000
3000
2975
2975
2850
```

### Top 3 rows

Ví dụ với:

```sql
FETCH FIRST 3 ROWS ONLY
```

→

```text
5000
3000
3000
```

chính xác 3 row.

---

### Top 3 ranks

`RANK()`:

```text
5000 → 1
3000 → 2
3000 → 2
2975 → 4
2975 → 4
2850 → 6
```

Không có rank 3.

Nếu:

```sql
WHERE RANK <= 3
```

→ chỉ:

```text
5000
3000
3000
```

Trong khi dùng `DENSE_RANK`:

```text
5000 → 1
3000 → 2
3000 → 2
2975 → 3
2975 → 3
2850 → 4
```

`DENSE_RANK <= 3`:

```text
5000
3000
3000
2975
2975
```

Vì vậy trước khi chọn hàm, phải hỏi:

> muốn **N row** hay **N mức giá trị/rank**?

## 35. Bẫy tie khi ORDER BY không deterministic

Giả sử:

```text
SCOTT  3000
FORD   3000
```

và:

```sql
ORDER BY SAL DESC
```

DB biết cả hai cùng lương nhưng không nhất thiết có tiêu chí xác định ai đứng trước.

Nếu bạn muốn thứ tự duy nhất:

```sql
ORDER BY SAL DESC, EMPNO ASC
```

Lúc này:

```text
SAL
↓
nếu bằng nhau → EMPNO
```

Điều này đặc biệt quan trọng khi dùng pagination.

---

## 36. Vì sao pagination cần ORDER BY ổn định?

Giả sử page 1:

```text
row 1~10
```

page 2:

```text
row 11~20
```

Nếu `ORDER BY SAL` nhưng hàng loạt row SAL bằng nhau, thứ tự peer có thể không ổn định.

Có nguy cơ một row:

```text
lần query 1 → page 1
lần query 2 → page 2
```

Vì vậy thực tế nên:

```sql
ORDER BY SAL DESC, EMPNO
```

để tạo total ordering.

## 37. Cách đọc đề SQLD nhanh

Nếu gặp:

```sql
SELECT ...
FROM EMP
WHERE ROWNUM <= 3
ORDER BY SAL DESC;
```

hãy nghĩ ngay:

```text
❌ limit trước
✅ sort sau
```

→ không đảm bảo Top 3 SAL toàn bảng.

---

Nếu gặp:

```sql
SELECT ...
FROM (
    SELECT ...
    FROM EMP
    ORDER BY SAL DESC
)
WHERE ROWNUM <= 3;
```

hãy nghĩ:

```text
✅ sort trước
✅ limit sau
```

→ đúng Top 3.

---

Nếu gặp:

```sql
WHERE ROWNUM BETWEEN 4 AND 6
```

hãy cảnh giác ngay:

```text
❌ ROWNUM không thể nhảy qua 1 để bắt đầu ở 4 như vậy
```

---

Nếu gặp:

```sql
RANK() OVER(ORDER BY SAL DESC)
```

hãy kiểm tra tie.

---

Nếu gặp:

```sql
OFFSET 3 ROWS
FETCH NEXT 3 ROWS ONLY
```

hãy đọc:

```text
skip 3
take 3
→ position 4~6
```

## 38. So sánh các ví dụ tương đương

### Oracle cổ điển

Top 3:

```sql
SELECT *
FROM (
    SELECT ENAME, SAL
    FROM EMP
    ORDER BY SAL DESC
)
WHERE ROWNUM <= 3;
```

---

### Oracle hiện đại

```sql
SELECT ENAME, SAL
FROM EMP
ORDER BY SAL DESC
FETCH FIRST 3 ROWS ONLY;
```

Dễ đọc hơn rất nhiều.

---

### SQL Server

```sql
SELECT TOP 3
       ENAME,
       SAL
FROM EMP
ORDER BY SAL DESC;
```

---

### Window Function

```sql
SELECT ENAME, SAL
FROM (
    SELECT ENAME,
           SAL,
           ROW_NUMBER() OVER(ORDER BY SAL DESC) AS RN
    FROM EMP
)
WHERE RN <= 3;
```

Cả 4 đều nhằm mục đích lấy 3 row theo thứ tự, nhưng mechanism khác nhau.

## 🔥 SQLD NOTE — 반드시 암기

### ① TOP-N

**KR:** 전체 결과에서 상위 N개의 행을 추출한다.
**VI:** Lấy N row đầu theo một tiêu chí sắp xếp.

---

### ② ROWNUM

```text
Oracle pseudocolumn
```

* không phải ID thật
* không cố định
* được gán trong quá trình row được lấy

---

### ③ Bẫy lớn nhất

```sql
WHERE ROWNUM <= 3
ORDER BY SAL DESC
```

≠ Top 3 SAL.

Vì:

```text
ROWNUM filter trước
ORDER BY sau
```

---

### ④ Cách đúng

```sql
SELECT *
FROM (
    SELECT *
    FROM EMP
    ORDER BY SAL DESC
)
WHERE ROWNUM <= 3;
```

Câu nhớ:

> **정렬 먼저, ROWNUM 나중.**
> Sort trước, ROWNUM sau.

---

### ⑤ `ROWNUM > 1` trực tiếp không hoạt động

```text
row đầu tiên luôn thử ROWNUM=1
↓
không pass
↓
row tiếp theo lại là candidate ROWNUM=1
```

nên không lên được 2.

---

### ⑥ Paging với ROWNUM

Phải dùng nested query:

```text
ORDER BY
↓
ROWNUM AS RN
↓
WHERE RN BETWEEN ...
```

---

### ⑦ RANK

```text
5000 → 1
3000 → 2
3000 → 2
2975 → 4
```

Tie cùng hạng, rank sau bị skip.

---

### ⑧ FETCH

```sql
ORDER BY ...
OFFSET N ROWS
FETCH NEXT M ROWS ONLY
```

nhớ:

```text
OFFSET = bỏ N row
FETCH = lấy M row
```

---

### ⑨ Ví dụ 4~6

```sql
OFFSET 3 ROWS
FETCH NEXT 3 ROWS ONLY
```

→ row vị trí:

```text
4, 5, 6
```

---

### ⑩ SQL Server TOP

```sql
SELECT TOP 2 ...
ORDER BY ...
```

---

### ⑪ WITH TIES

```sql
TOP 2 WITH TIES
```

Nếu vị trí thứ 2 bị đồng hạng:

```text
2 rows có thể biến thành 3+ rows
```

---

## 🧠 Công thức nhớ 10 giây

```text
ROWNUM
= Oracle số row giả
= limit trước ORDER BY nếu cùng query level

Top N đúng với ROWNUM
= ORDER BY trong subquery
→ ROWNUM ở ngoài

RANK
= tie cùng hạng + skip rank

OFFSET N
= bỏ N row

FETCH M
= lấy M row

TOP N
= SQL Server

WITH TIES
= lấy thêm những row bằng boundary value
```

Và câu quan trọng nhất của cả chương:

> **TOP-N 문제에서 먼저 판단할 것: "N개의 행"을 원하는가, 아니면 "N개의 순위"를 원하는가?**
> Khi gặp bài TOP-N, trước tiên phải xác định: **muốn N row hay muốn N thứ hạng**.

Hai yêu cầu này nhìn giống nhau nhưng khi có **동점/tie**, kết quả có thể hoàn toàn khác.
Tiếp tục **제6절 계층형 질의와 셀프 조인 — Hierarchical Query & Self Join**. Phần ảnh này tập trung gần như toàn bộ vào **Hierarchical Query của Oracle**, đặc biệt là `START WITH`, `CONNECT BY PRIOR`, `LEVEL`, `NOCYCLE`, `CONNECT_BY_ROOT`, `SYS_CONNECT_BY_PATH`, `CONNECT_BY_ISLEAF`, `CONNECT_BY_ISCYCLE`.
