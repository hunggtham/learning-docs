# Window Functions

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Window functions**. Route đi từ partition/order → frame semantics → rank/lag/lead → running aggregates → pagination and analytics, để tính theo cửa sổ không làm mất từng dòng gốc.

> **Mục tiêu:** OVER, PARTITION BY, window frame, ranking và các hàm phân tích.

## Từ khóa cần nhớ (Keyword)

Phần giải thích dùng tiếng Việt trước. Ở mọi lần xuất hiện, thuật ngữ SQLD dùng dạng `nghĩa Việt (English / 한국어)` để vừa giữ mạch đọc vừa đối chiếu được từ khóa trong đề.

Keyword chỉ giúp nhận diện thuật ngữ; mạch tư duy cần giải thích vì sao window function giữ từng row nhưng vẫn nhìn được tập liên quan. Từ đó bài học nối khái niệm với cú pháp và semantics.

## Mạch tư duy (Logic học)

Hãy xác định **đối tượng dữ liệu** trước, sau đó đọc **điều kiện**, **phạm vi dòng**, **thứ tự xử lý** và cuối cùng kiểm tra **kết quả mong đợi**. Với SQL, luôn phân biệt điều kiện lọc trước nhóm (`WHERE`) với điều kiện lọc sau nhóm (`HAVING`); đây là cầu nối để hiểu vì sao cùng một truy vấn có thể cho kết quả khác nhau.

Mạch tư duy đặt câu hỏi về phạm vi và thứ tự tính toán, còn mạch nối biến câu hỏi ấy thành lộ trình đọc. Điểm vào đầu tiên là window function và sự khác aggregate query truyền thống.

## Mạch nối của bài học

Bài này không đứng riêng: hãy nối **Window Functions** với bài trước bằng đối tượng dữ liệu/điều kiện mà nó tái sử dụng, rồi dùng kết quả ở phần cuối để chọn bài kế tiếp trong cùng môn. Khi gặp một truy vấn mới, nói rõ nó đang mở rộng mô hình dữ liệu, thứ tự xử lý hay cách kiểm tra kết quả nào trước khi nhớ cú pháp.

> **Cách học:** Đọc phần khái niệm → tự chạy lại các ví dụ SQL → chốt lại mục **từ khóa (Keyword)**, bảng so sánh và phần ghi nhớ cuối bài.

---

Để học **Window Functions** như một mạch suy luận, trước hết hãy giữ câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Mục đích của bài là biến **OVER, PARTITION BY, window frame, ranking và các hàm phân tích** thành cách đọc có thể áp dụng.

Ta bắt đầu **1. 윈도우 함수 — Window Function ⭐⭐⭐** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Window function tính trên một window nhưng không làm mất row detail. Hiểu đặc điểm này trước giúp thấy vì sao nó giải quyết các bài toán mà `GROUP BY` đơn thuần không thể giữ đủ ngữ cảnh.

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

Khi gom phần **1. 윈도우 함수 — Window Function ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1. 윈도우 함수 — Window Function ⭐⭐⭐**. Bây giờ chuyển sang **2. Tại sao cần Window Function?**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2. Tại sao cần Window Function?** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Window function trả thêm giá trị theo từng dòng, nhưng lợi ích chỉ rõ khi so với nhu cầu thực tế như running total, ranking và so sánh trong nhóm. Cấu trúc `OVER()` là giao diện mô tả phạm vi đó.

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

Khi gom phần **2. Tại sao cần Window Function?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2. Tại sao cần Window Function?**. Bây giờ chuyển sang **Cách 1 — Subquery**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Cách 1 — Subquery** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Cách 1 — Subquery** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Cách 1 — Subquery**. Bây giờ chuyển sang **3. Cấu trúc Window Function ⭐⭐⭐**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3. Cấu trúc Window Function ⭐⭐⭐** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

`OVER()` tách partition, order và frame thành các lớp semantics khác nhau. Sau khi thấy cấu trúc tổng quát, cần cô lập `PARTITION BY` để hiểu ranh giới nhóm trước khi xét thứ tự.

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

Khi gom phần **3. Cấu trúc Window Function ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3. Cấu trúc Window Function ⭐⭐⭐**. Bây giờ chuyển sang **4. PARTITION BY**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4. PARTITION BY** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

`PARTITION BY` chia các row thành những cửa sổ độc lập nhưng không tự sắp xếp bên trong. `ORDER BY` tiếp theo quyết định vị trí tương đối và hướng tính các hàm tuần tự.

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

Khi gom phần **4. PARTITION BY** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4. PARTITION BY**. Bây giờ chuyển sang **5. ORDER BY bên trong OVER()**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5. ORDER BY bên trong OVER()** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

`ORDER BY` trong `OVER()` khác order của result set: nó định nghĩa logic cửa sổ chứ không nhất thiết đổi thứ tự output. Khi có thứ tự, aggregate cũng có thể trở thành running hoặc cumulative calculation.

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

Khi gom phần **5. ORDER BY bên trong OVER()** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5. ORDER BY bên trong OVER()**. Bây giờ chuyển sang **6. Aggregate Function dùng như Window Function**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6. Aggregate Function dùng như Window Function** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Aggregate dùng như window giữ từng row và tính trên frame tương ứng. Với `SUM()`, thêm `ORDER BY` thường biến tổng của cả partition thành cumulative sum, nhưng frame mặc định và ties vẫn phải được kiểm tra.

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

Khi gom phần **6. Aggregate Function dùng như Window Function** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6. Aggregate Function dùng như Window Function**. Bây giờ chuyển sang **7. SUM() + ORDER BY = cumulative sum**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7. SUM() + ORDER BY = cumulative sum** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Với `SUM()`, thêm `ORDER BY` thường tạo cumulative sum: frame mở rộng từ đầu partition đến row hiện tại. Kết quả còn phụ thuộc peer rows và frame mặc định, nên phải kiểm tra trước khi suy ra semantics.

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

Khi gom phần **7. SUM() + ORDER BY = cumulative sum** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7. SUM() + ORDER BY = cumulative sum**. Bây giờ chuyển sang **Nhớ**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Nhớ

Phần này nối mạch SQL với “Nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
SUM(...) OVER(PARTITION BY A)
→ tổng toàn partition

SUM(...) OVER(PARTITION BY A ORDER BY B)
→ thường là cumulative sum theo B
```

---

Khi gom phần **Nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Nhớ**. Bây giờ chuyển sang **8. AVG cũng tương tự**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **8. AVG cũng tương tự** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Cumulative sum cho thấy frame tiến dần theo order; `AVG()` dùng cùng cơ chế nhưng denominator thay đổi theo frame. Vì vậy bước kế tiếp phải làm rõ `ROWS` và `RANGE`, thay vì giả định mọi frame theo thứ tự đều giống nhau.

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

Khi gom phần **8. AVG cũng tương tự** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **8. AVG cũng tương tự**. Bây giờ chuyển sang **9. Window Frame — ROWS / RANGE ⭐⭐⭐**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **9. Window Frame — ROWS / RANGE ⭐⭐⭐** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

ROWS/RANGE xác định tập row thực sự đi vào mỗi phép tính. Đây là ranh giới quan trọng giữa vị trí vật lý và giá trị order, đặc biệt khi có peer rows hoặc duplicate sort keys.

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

Khi gom phần **9. Window Frame — ROWS / RANGE ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **9. Window Frame — ROWS / RANGE ⭐⭐⭐**. Bây giờ chuyển sang **Ý nghĩa**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Ý nghĩa** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### Ý nghĩa

Khi gom phần **Ý nghĩa** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Ý nghĩa**. Bây giờ chuyển sang **`UNBOUNDED PRECEDING`**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **`UNBOUNDED PRECEDING`** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### `UNBOUNDED PRECEDING`

**KR:** 파티션의 첫 행부터.
**VI:** Từ row đầu tiên của partition.

Khi gom phần **`UNBOUNDED PRECEDING`** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **`UNBOUNDED PRECEDING`**. Bây giờ chuyển sang **`CURRENT ROW`**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **`CURRENT ROW`** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### `CURRENT ROW`

**KR:** 현재 행까지.
**VI:** Đến row hiện tại.

Khi gom phần **`CURRENT ROW`** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **`CURRENT ROW`**. Bây giờ chuyển sang **`1 PRECEDING`**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **`1 PRECEDING`** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### `1 PRECEDING`

Row ngay trước.

Khi gom phần **`1 PRECEDING`** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **`1 PRECEDING`**. Bây giờ chuyển sang **`1 FOLLOWING`**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **`1 FOLLOWING`** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### `1 FOLLOWING`

Row ngay sau.

Khi gom phần **`1 FOLLOWING`** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **`1 FOLLOWING`**. Bây giờ chuyển sang **`UNBOUNDED FOLLOWING`**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **`UNBOUNDED FOLLOWING`** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### `UNBOUNDED FOLLOWING`

Row cuối cùng của partition.

---

Khi gom phần **`UNBOUNDED FOLLOWING`** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **`UNBOUNDED FOLLOWING`**. Bây giờ chuyển sang **10. ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **10. ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

`ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` lấy từ đầu partition đến vị trí hiện tại theo row position. Khi muốn semantics theo giá trị và peer group, cần so sánh trực tiếp với `RANGE`.

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

Khi gom phần **10. ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **10. ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW**. Bây giờ chuyển sang **11. RANGE khác ROWS như thế nào? ⭐⭐⭐**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11. RANGE khác ROWS như thế nào? ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

RANGE nhóm các peer có cùng giá trị order, còn ROWS đếm vị trí vật lý; vì vậy cùng cú pháp aggregate có thể cho kết quả khác. Mặc định frame của dialect phải được kiểm tra trước khi đọc output.

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

Khi gom phần **11. RANGE khác ROWS như thế nào? ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11. RANGE khác ROWS như thế nào? ⭐⭐⭐**. Bây giờ chuyển sang **ROWS**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**ROWS** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

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

Khi gom phần **ROWS** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **ROWS**. Bây giờ chuyển sang **RANGE**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**RANGE** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

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

Khi gom phần **RANGE** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **RANGE**. Bây giờ chuyển sang **Câu nhớ**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Câu nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Câu nhớ

> **ROWS = 행을 본다 — nhìn ROW.**

> **RANGE = 값을 본다 — nhìn VALUE.**

Đây là cách nhớ rất hiệu quả cho SQLD.

---

Khi gom phần **Câu nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Câu nhớ**. Bây giờ chuyển sang **12. Default frame rất quan trọng**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **12. Default frame rất quan trọng** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Default frame thường thay đổi khi có hoặc không có `ORDER BY`, và peer rows có thể cùng nhận một giá trị. Hiểu mặc định giúp giải thích vì sao `RANGE` xuất hiện dù query không ghi rõ frame.

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

Khi gom phần **12. Default frame rất quan trọng** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **12. Default frame rất quan trọng**. Bây giờ chuyển sang **13. Toàn partition**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **13. Toàn partition** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Một frame có thể bao phủ toàn partition nếu bỏ order hoặc chọn boundary phù hợp, khi đó mỗi row nhận cùng aggregate. Từ toàn partition, `FOLLOWING` mở cửa sổ về phía các row tương lai.

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

Khi gom phần **13. Toàn partition** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **13. Toàn partition**. Bây giờ chuyển sang **14. FOLLOWING**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14. FOLLOWING** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

`FOLLOWING` cho phép nhìn trước trong partition nhưng làm frame nhạy với biên cuối và NULL/tie ordering. Các hàm offset như `LAG` và `LEAD` giải quyết một dạng nhìn trước/nhìn sau khác, theo vị trí row.

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

Khi gom phần **14. FOLLOWING** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14. FOLLOWING**. Bây giờ chuyển sang **15. LAG / LEAD ⭐⭐⭐**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **15. LAG / LEAD ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

`LAG` và `LEAD` lấy giá trị ở offset tương đối, không phải aggregate trên frame. Cú pháp offset, default value và order key cần được đọc cùng nhau để biết hành vi ở biên partition.

## 15. LAG / LEAD ⭐⭐⭐

Hai hàm này dùng để lấy giá trị của row trước/sau mà không cần self join.

Khi gom phần **15. LAG / LEAD ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **15. LAG / LEAD ⭐⭐⭐**. Bây giờ chuyển sang **LAG**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**LAG** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

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

Khi gom phần **LAG** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **LAG**. Bây giờ chuyển sang **LEAD**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**LEAD** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

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

Khi gom phần **LEAD** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **LEAD**. Bây giờ chuyển sang **16. Cú pháp LAG/LEAD**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **16. Cú pháp LAG/LEAD** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Cú pháp `LAG/LEAD` quy định offset và giá trị thay thế khi không có row, nhưng semantics vẫn phụ thuộc order ổn định. Một `ORDER BY` đặt sai cột có thể tạo kết quả hợp lệ về cú pháp nhưng sai ý định.

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

Khi gom phần **16. Cú pháp LAG/LEAD** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **16. Cú pháp LAG/LEAD**. Bây giờ chuyển sang **Default**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Default** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Default** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Default**. Bây giờ chuyển sang **17. Một bẫy trong ảnh: ORDER BY DEPTNO không có nghĩa partition**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **17. Một bẫy trong ảnh: ORDER BY DEPTNO không có nghĩa partition** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

ORDER BY `DEPTNO` chỉ sắp xếp trong window; nó không tạo partition theo department. Khi cần so sánh trong từng nhóm, `PARTITION BY` phải được viết riêng trước khi chọn value đầu hoặc cuối.

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

Khi gom phần **17. Một bẫy trong ảnh: ORDER BY DEPTNO không có nghĩa partition** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **17. Một bẫy trong ảnh: ORDER BY DEPTNO không có nghĩa partition**. Bây giờ chuyển sang **Nhớ**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Nhớ

> `ORDER BY DEPTNO` ≠ `PARTITION BY DEPTNO`

`ORDER BY` chỉ sắp thứ tự.

`PARTITION BY` mới **chia nhóm/reset window**.

---

Khi gom phần **Nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Nhớ**. Bây giờ chuyển sang **18. FIRST_VALUE ⭐⭐⭐**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **18. FIRST_VALUE ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

`FIRST_VALUE` trả value của row đầu theo frame/order, không phải giá trị nhỏ nhất. Phân biệt vị trí đầu với phép cực trị giúp tránh nhầm nó với `MIN()` khi dữ liệu có ties hoặc frame thay đổi.

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

Khi gom phần **18. FIRST_VALUE ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **18. FIRST_VALUE ⭐⭐⭐**. Bây giờ chuyển sang **Có thể lấy MAX bằng FIRST_VALUE**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Có thể lấy MAX bằng FIRST_VALUE** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Có thể lấy MAX bằng FIRST_VALUE** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Có thể lấy MAX bằng FIRST_VALUE**. Bây giờ chuyển sang **19. FIRST_VALUE không phải MIN**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **19. FIRST_VALUE không phải MIN** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

`FIRST_VALUE` phụ thuộc frame và thứ tự, còn `MIN()` chỉ xét giá trị trong tập. Đối xứng với bẫy này là `LAST_VALUE`, vì frame mặc định thường kết thúc ở current row chứ chưa tới cuối partition.

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

Khi gom phần **19. FIRST_VALUE không phải MIN** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **19. FIRST_VALUE không phải MIN**. Bây giờ chuyển sang **20. LAST_VALUE — bẫy rất lớn ⭐⭐⭐**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **20. LAST_VALUE — bẫy rất lớn ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

`LAST_VALUE` theo frame mặc định thường trả chính row hiện tại, nên dễ bị tưởng là giá trị cuối nhóm. Muốn lấy last thật sự, phải mở frame tới `UNBOUNDED FOLLOWING` và kiểm tra order/ties.

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

Khi gom phần **20. LAST_VALUE — bẫy rất lớn ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **20. LAST_VALUE — bẫy rất lớn ⭐⭐⭐**. Bây giờ chuyển sang **Vì sao?**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Vì sao?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Vì sao?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Vì sao?**. Bây giờ chuyển sang **21. Muốn LAST_VALUE thật sự lấy cuối partition**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **21. Muốn LAST_VALUE thật sự lấy cuối partition** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Để `LAST_VALUE` thật sự nhìn tới cuối partition, frame phải bao phủ phần còn lại chứ không dừng ở current row. Sau các frame theo vị trí, `NTILE(N)` chuyển sang chia các row đã order thành các bucket.

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

Khi gom phần **21. Muốn LAST_VALUE thật sự lấy cuối partition** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **21. Muốn LAST_VALUE thật sự lấy cuối partition**. Bây giờ chuyển sang **Câu cực quan trọng**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Câu cực quan trọng** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Câu cực quan trọng

> **LAST_VALUE + ORDER BY → luôn kiểm tra window frame.**

Đây là một trong những bẫy Window Function đáng nhớ nhất.

---

Khi gom phần **Câu cực quan trọng** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Câu cực quan trọng**. Bây giờ chuyển sang **22. NTILE(N) ⭐⭐⭐**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **22. NTILE(N) ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

NTILE chia thứ tự trong partition thành N nhóm gần đều, nên bucket boundary phụ thuộc số row, ties và order ổn định. Vì cần một thứ tự để chia, `NTILE` bắt buộc có `ORDER BY`.

## 22. NTILE(N) ⭐⭐⭐

**KR:** `NTILE(N)`은 정렬된 행들을 N개의 그룹으로 나눈다.
**VI:** `NTILE(N)` chia các row đã được sắp xếp thành **N nhóm gần bằng nhau**.

```sql
NTILE(2) OVER(ORDER BY SAL)
```

→ chia thành 2 nhóm.

---

Khi gom phần **22. NTILE(N) ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **22. NTILE(N) ⭐⭐⭐**. Bây giờ chuyển sang **Nếu không chia đều?**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Nếu không chia đều?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Nếu không chia đều?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Nếu không chia đều?**. Bây giờ chuyển sang **Quy tắc**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Quy tắc** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Quy tắc** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Quy tắc**. Bây giờ chuyển sang **23. NTILE bắt buộc ORDER BY**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **23. NTILE bắt buộc ORDER BY** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

NTILE chia bucket dựa trên thứ tự, nên phần tiếp theo cần nêu rõ vì sao thiếu `ORDER BY` làm semantics không xác định. Đây là boundary khác với các hàm chỉ aggregate theo partition.

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

Khi gom phần **23. NTILE bắt buộc ORDER BY** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **23. NTILE bắt buộc ORDER BY**. Bây giờ chuyển sang **24. RATIO_TO_REPORT ⭐⭐**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **24. RATIO_TO_REPORT ⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

NTILE bắt buộc order để bucket có nghĩa; sau khi phân nhóm theo vị trí, `RATIO_TO_REPORT` chuyển câu hỏi sang tỷ trọng của mỗi row trong tổng partition.

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

Khi gom phần **24. RATIO_TO_REPORT ⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **24. RATIO_TO_REPORT ⭐⭐**. Bây giờ chuyển sang **PARTITION BY**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**PARTITION BY** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

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

Khi gom phần **PARTITION BY** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **PARTITION BY**. Bây giờ chuyển sang **Điểm cần nhớ**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Điểm cần nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Điểm cần nhớ

Theo nội dung SQLD trong ảnh:

```text
RATIO_TO_REPORT
→ PARTITION BY được
→ ORDER BY không dùng
```

---

Khi gom phần **Điểm cần nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Điểm cần nhớ**. Bây giờ chuyển sang **25. PERCENT_RANK ⭐⭐⭐**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **25. PERCENT_RANK ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

`RATIO_TO_REPORT` trả phần đóng góp tương đối của row hoặc expression trong partition, không cần frame tuần tự như running sum. Để xếp hạng theo vị trí tương đối, dùng `PERCENT_RANK`.

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

Khi gom phần **25. PERCENT_RANK ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **25. PERCENT_RANK ⭐⭐⭐**. Bây giờ chuyển sang **26. PERCENT_RANK xử lý tie**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **26. PERCENT_RANK xử lý tie** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

`PERCENT_RANK` chuẩn hóa rank từ 0 đến 1 dựa trên số row và vị trí rank. Khi nhiều row đồng hạng, cần xem tie được gán rank chung và khoảng trống ra sao.

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

Khi gom phần **26. PERCENT_RANK xử lý tie** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **26. PERCENT_RANK xử lý tie**. Bây giờ chuyển sang **27. CUME_DIST ⭐⭐⭐**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **27. CUME_DIST ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Ties làm `PERCENT_RANK` giữ cùng rank cho peer rows, còn `CUME_DIST` đo tỷ lệ row có giá trị nhỏ hơn hoặc bằng current value. Vì vậy CUME_DIST cần được minh họa bằng dữ liệu có lặp.

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

Khi gom phần **27. CUME_DIST ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **27. CUME_DIST ⭐⭐⭐**. Bây giờ chuyển sang **28. Ví dụ CUME_DIST**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **28. Ví dụ CUME_DIST** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

`CUME_DIST` tăng theo cumulative population đến peer group hiện tại; ví dụ cụ thể giúp tách nó khỏi rank của một row đơn lẻ. Khi có tie, cả nhóm nhảy cùng một mốc phân phối.

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

Khi gom phần **28. Ví dụ CUME_DIST** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **28. Ví dụ CUME_DIST**. Bây giờ chuyển sang **29. CUME_DIST và tie ⭐⭐⭐**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **29. CUME_DIST và tie ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Ví dụ CUME_DIST cho thấy peer rows cùng chia sẻ cumulative boundary. Từ đó có thể so sánh trực tiếp cách `PERCENT_RANK` và `CUME_DIST` phản ánh vị trí trong một partition.

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

Khi gom phần **29. CUME_DIST và tie ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **29. CUME_DIST và tie ⭐⭐⭐**. Bây giờ chuyển sang **30. PERCENT_RANK vs CUME_DIST ⭐⭐⭐**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **30. PERCENT_RANK vs CUME_DIST ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

`PERCENT_RANK` dựa trên rank và mẫu số `n-1`, còn `CUME_DIST` dựa trên số row không vượt quá giá trị hiện tại và mẫu số `n`. Hai hàm cùng chuẩn hóa nhưng không cùng semantics.

## 30. PERCENT_RANK vs CUME_DIST ⭐⭐⭐

Lấy:

```text
3000
3000
2975
1100
800
```

Khi gom phần **30. PERCENT_RANK vs CUME_DIST ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **30. PERCENT_RANK vs CUME_DIST ⭐⭐⭐**. Bây giờ chuyển sang **PERCENT_RANK**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**PERCENT_RANK** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

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

Khi gom phần **PERCENT_RANK** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **PERCENT_RANK**. Bây giờ chuyển sang **CUME_DIST**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**CUME_DIST** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

#### CUME_DIST

Dựa trên tỷ lệ row tích lũy:

```text
3000 → 0.4
3000 → 0.4
2975 → 0.6
1100 → 0.8
800  → 1
```

Khi gom phần **CUME_DIST** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **CUME_DIST**. Bây giờ chuyển sang **Cách nhớ**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Đoạn **Cách nhớ** đổi quy tắc thành hình ảnh hoặc câu nhớ. Hãy trả lời: **hình ảnh hoặc câu nhớ này đang nén quan hệ nào để ta có thể tự dựng lại kết quả mà không học thuộc cú pháp?** Sau đó quay lại điều kiện SQL để chắc rằng cách nhớ không làm mất trường hợp biên.

#### Cách nhớ

> **PERCENT_RANK = 내 순위가 어디인가?**
> Rank của tôi nằm ở đâu?

> **CUME_DIST = 여기까지 몇 % 왔는가?**
> Đến vị trí này đã bao phủ bao nhiêu % row?

---

Khi gom phần **Cách nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Cách nhớ**. Bây giờ chuyển sang **31. Đừng nhầm RANGE và CUME_DIST**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **31. Đừng nhầm RANGE và CUME_DIST** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

So sánh hai hàm ranking không nên lẫn với semantics của frame. `RANGE` xác định row đưa vào aggregate theo order value, còn `CUME_DIST` là một ranking distribution function.

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

Khi gom phần **31. Đừng nhầm RANGE và CUME_DIST** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **31. Đừng nhầm RANGE và CUME_DIST**. Bây giờ chuyển sang **32. Sơ đồ tổng hợp Window Function**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **32. Sơ đồ tổng hợp Window Function** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

`RANGE` và `CUME_DIST` đều nhạy với peer values nhưng giải quyết hai câu hỏi khác nhau: frame cho phép tính trên tập nào, còn CUME_DIST cho biết bao nhiêu row đã đạt tới value đó.

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

Khi gom phần **32. Sơ đồ tổng hợp Window Function** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **32. Sơ đồ tổng hợp Window Function**. Bây giờ chuyển sang **Bước 1 — PARTITION BY**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Bước 1 — PARTITION BY** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Bước 1 — PARTITION BY

Phần này nối mạch SQL với “Bước 1 — PARTITION BY”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
DEPT 10 | DEPT 20 | DEPT 30
```

Chia dữ liệu.

Khi gom phần **Bước 1 — PARTITION BY** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Bước 1 — PARTITION BY**. Bây giờ chuyển sang **Bước 2 — ORDER BY**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Bước 2 — ORDER BY** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Bước 2 — ORDER BY** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Bước 2 — ORDER BY**. Bây giờ chuyển sang **Bước 3 — ROWS**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Bước 3 — ROWS** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Bước 3 — ROWS** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Bước 3 — ROWS**. Bây giờ chuyển sang **33. Bảng phân loại các hàm trong ảnh**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **33. Bảng phân loại các hàm trong ảnh** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Sơ đồ tổng hợp nên đặt partition, order, frame và function family trên cùng các trục để đọc query boundary. Bảng phân loại sau đó giúp chọn hàm theo mục tiêu thay vì nhớ rời từng ví dụ.

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

Khi gom phần **33. Bảng phân loại các hàm trong ảnh** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **33. Bảng phân loại các hàm trong ảnh**. Bây giờ chuyển sang **🔥 SQLD NOTE — Phần phải thuộc**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **🔥 SQLD NOTE — Phần phải thuộc** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

Bảng phân loại gom aggregate, offset, ranking và distribution functions theo semantics. SQLD note cuối bài chốt các bẫy phải kiểm tra: NULL, ties, default frame, order và dialect.

## 🔥 SQLD NOTE — Phần phải thuộc

Khi gom phần **🔥 SQLD NOTE — Phần phải thuộc** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **🔥 SQLD NOTE — Phần phải thuộc**. Bây giờ chuyển sang **① Bản chất**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **① Bản chất** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ① Bản chất

Phần này nối mạch SQL với “① Bản chất”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
GROUP BY
→ nhiều row → ít row

WINDOW FUNCTION
→ giữ nguyên row
→ tính toán giữa các row
```

Khi gom phần **① Bản chất** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **① Bản chất**. Bây giờ chuyển sang **② Cấu trúc**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **② Cấu trúc** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **② Cấu trúc** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **② Cấu trúc**. Bây giờ chuyển sang **③ PARTITION BY**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **③ PARTITION BY** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ③ PARTITION BY

Phần này nối mạch SQL với “③ PARTITION BY”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
PARTITION BY ≈ chia group
```

nhưng:

```text
không làm mất row.
```

Khi gom phần **③ PARTITION BY** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **③ PARTITION BY**. Bây giờ chuyển sang **④ Aggregate + ORDER BY**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **④ Aggregate + ORDER BY** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ④ Aggregate + ORDER BY

Phần này nối mạch SQL với “④ Aggregate + ORDER BY”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
SUM(SAL) OVER(ORDER BY ...)
```

→ thường tạo **누적합 / cumulative sum**.

Khi gom phần **④ Aggregate + ORDER BY** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **④ Aggregate + ORDER BY**. Bây giờ chuyển sang **⑤ ROWS vs RANGE**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑤ ROWS vs RANGE** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **⑤ ROWS vs RANGE** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑤ ROWS vs RANGE**. Bây giờ chuyển sang **⑥ Window frame**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑥ Window frame** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **⑥ Window frame** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑥ Window frame**. Bây giờ chuyển sang **⑦ LAG / LEAD**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑦ LAG / LEAD** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⑦ LAG / LEAD

Phần này nối mạch SQL với “⑦ LAG / LEAD”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
LAG  ← CURRENT → LEAD
```

`LAG` = previous.

`LEAD` = next.

Khi gom phần **⑦ LAG / LEAD** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑦ LAG / LEAD**. Bây giờ chuyển sang **⑧ FIRST_VALUE / LAST_VALUE**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑧ FIRST_VALUE / LAST_VALUE** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⑧ FIRST_VALUE / LAST_VALUE

Phần này nối mạch SQL với “⑧ FIRST_VALUE / LAST_VALUE”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
FIRST_VALUE
→ đầu frame

LAST_VALUE
→ cuối frame
```

⚠️ `LAST_VALUE` đặc biệt phải kiểm tra **window frame**.

Khi gom phần **⑧ FIRST_VALUE / LAST_VALUE** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑧ FIRST_VALUE / LAST_VALUE**. Bây giờ chuyển sang **⑨ NTILE**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑨ NTILE** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⑨ NTILE

Phần này nối mạch SQL với “⑨ NTILE”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
NTILE(N)
→ chia N nhóm

14 rows / 3
→ 5 / 5 / 4
```

Phần dư được đưa cho **nhóm phía trước**.

Khi gom phần **⑨ NTILE** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑨ NTILE**. Bây giờ chuyển sang **⑩ PERCENT_RANK**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑩ PERCENT_RANK** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **⑩ PERCENT_RANK** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑩ PERCENT_RANK**. Bây giờ chuyển sang **⑪ CUME_DIST**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑪ CUME_DIST** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⑪ CUME_DIST

Phần này nối mạch SQL với “⑪ CUME_DIST”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
cumulative rows
---------------
total rows

Khi gom phần **⑪ CUME_DIST** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Như vậy, **⑪ CUME_DIST** đã được đặt trong quan hệ giữa đầu vào, quy tắc xử lý và kết quả. Khi ôn lại, hãy tự diễn đạt ranh giới của nó rồi dùng ranh giới đó làm điểm nối sang bài tiếp theo.

> **Bàn giao:** Sau **🔥 SQLD NOTE — Phần phải thuộc**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
