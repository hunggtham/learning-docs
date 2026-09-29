# TOP-N và Pagination

> **Mục tiêu:** ROWNUM, ROW_NUMBER/RANK/DENSE_RANK, FETCH/OFFSET, TOP và WITH TIES.

## Từ khóa cần nhớ (Keyword)

Các thuật ngữ SQLD được giữ nguyên tiếng Hàn/English trong phần nguồn. Khi ghi chú, dùng mẫu `용어 (English) (Tiếng Việt)` để nối tên gọi trong đề với ý nghĩa thực tế.

## Mạch tư duy (Logic học)

Hãy xác định **đối tượng dữ liệu** trước, sau đó đọc **điều kiện**, **phạm vi dòng**, **thứ tự xử lý** và cuối cùng kiểm tra **kết quả mong đợi**. Với SQL, luôn phân biệt điều kiện lọc trước nhóm (`WHERE`) với điều kiện lọc sau nhóm (`HAVING`).

> **Cách học:** Đọc phần khái niệm → tự chạy lại các ví dụ SQL → chốt lại các mục `Keyword`, bảng so sánh và phần ghi nhớ cuối bài.

---

Để học **TOP-N và Pagination** như một mạch suy luận, trước hết hãy giữ câu hỏi: **ta chọn đúng đoạn kết quả nào, theo thứ tự nào, và làm sao không nhầm giữa giới hạn hàng với thứ tự xử lý?** Mục đích của bài là biến **ROWNUM, ROW_NUMBER/RANK/DENSE_RANK, FETCH/OFFSET, TOP và WITH TIES** thành cách đọc có thể áp dụng.

```

Range:

```text
0 < x ≤ 1
```

Row cuối → `1`.

Ta bắt đầu **⑫ RATIO_TO_REPORT** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⑫ RATIO_TO_REPORT

Phần này nối mạch SQL với “⑫ RATIO_TO_REPORT”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
current value
-------------
partition SUM
```

Tổng ratio ≈ `1`.

---

Khi gom phần **⑫ RATIO_TO_REPORT** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑫ RATIO_TO_REPORT**. Bây giờ chuyển sang **🧠 Một dòng để nhớ toàn bộ chương**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **🧠 Một dòng để nhớ toàn bộ chương** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 🧠 Một dòng để nhớ toàn bộ chương

Phần này nối mạch SQL với “🧠 Một dòng để nhớ toàn bộ chương”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
PARTITION BY = chia nhóm nhưng giữ row
ORDER BY     = xác định thứ tự tính
ROWS         = tính theo từng row
RANGE        = tính theo giá trị/peer
LAG          = trước
LEAD         = sau
FIRST_VALUE  = đầu frame
LAST_VALUE   = cuối frame
NTILE        = chia N nhóm
RATIO        = giá trị / tổng
PERCENT_RANK = vị trí xếp hạng %
CUME_DIST    = tỷ lệ tích lũy
```

**Đặc biệt nếu đề SQLD cho `SUM(...) OVER(ORDER BY ...)` có giá trị ORDER BY trùng nhau, hoặc cho `LAST_VALUE(...)`, đừng tính ngay. Việc đầu tiên phải làm là xác định `ROWS/RANGE` và window frame trước.** Đây là hai bẫy lớn nhất trong nhóm kiến thức ở các trang này.
Tiếp tục **제5절 TOP N 쿼리 — TOP-N Query**. Phần này nhìn có vẻ đơn giản nhưng SQLD rất thích hỏi bẫy về **`ROWNUM` + `ORDER BY`**, **vì sao `ROWNUM > 1` không chạy**, và sự khác nhau giữa **ROWNUM / RANK / FETCH / TOP**.

Khi gom phần **🧠 Một dòng để nhớ toàn bộ chương** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **🧠 Một dòng để nhớ toàn bộ chương**. Bây giờ chuyển sang **1. TOP-N Query là gì?**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1. TOP-N Query là gì?** bằng câu hỏi: **ta chọn đúng đoạn kết quả nào, theo thứ tự nào, và làm sao không nhầm giữa giới hạn hàng với thứ tự xử lý?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **1. TOP-N Query là gì?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1. TOP-N Query là gì?**. Bây giờ chuyển sang **2. Các cách làm TOP-N trong phần này**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2. Các cách làm TOP-N trong phần này** bằng câu hỏi: **ta chọn đúng đoạn kết quả nào, theo thứ tự nào, và làm sao không nhầm giữa giới hạn hàng với thứ tự xử lý?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 2. Các cách làm TOP-N trong phần này

Trong ảnh có 4 cách chính:

```text
1. ROWNUM       → Oracle kiểu cũ
2. RANK()       → Window Function
3. FETCH/OFFSET → Oracle 12c+ / chuẩn hiện đại
4. TOP N        → SQL Server
```

Trước hết phải hiểu `ROWNUM`, vì đây là phần dễ nhầm nhất.

Khi gom phần **2. Các cách làm TOP-N trong phần này** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2. Các cách làm TOP-N trong phần này**. Bây giờ chuyển sang **3. ROWNUM là gì? ⭐⭐⭐**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3. ROWNUM là gì? ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **3. ROWNUM là gì? ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3. ROWNUM là gì? ⭐⭐⭐**. Bây giờ chuyển sang **4. ROWNUM không phải số thứ tự cố định**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4. ROWNUM không phải số thứ tự cố định** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **4. ROWNUM không phải số thứ tự cố định** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4. ROWNUM không phải số thứ tự cố định**. Bây giờ chuyển sang **5. Bẫy lớn nhất: ROWNUM + ORDER BY ⭐⭐⭐**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5. Bẫy lớn nhất: ROWNUM + ORDER BY ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **5. Bẫy lớn nhất: ROWNUM + ORDER BY ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5. Bẫy lớn nhất: ROWNUM + ORDER BY ⭐⭐⭐**. Bây giờ chuyển sang **6. Vì sao?**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6. Vì sao?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **6. Vì sao?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6. Vì sao?**. Bây giờ chuyển sang **7. Cách đúng: sort trước bằng Inline View ⭐⭐⭐**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7. Cách đúng: sort trước bằng Inline View ⭐⭐⭐** bằng câu hỏi: **cấu trúc hoặc ràng buộc nào đang bảo vệ dữ liệu, và thay đổi đó ảnh hưởng đến các câu lệnh sau ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **7. Cách đúng: sort trước bằng Inline View ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7. Cách đúng: sort trước bằng Inline View ⭐⭐⭐**. Bây giờ chuyển sang **8. Inline View là gì?**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **8. Inline View là gì?** bằng câu hỏi: **cấu trúc hoặc ràng buộc nào đang bảo vệ dữ liệu, và thay đổi đó ảnh hưởng đến các câu lệnh sau ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 8. Inline View là gì?

Phần này nối mạch SQL với “8. Inline View là gì?”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

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

Khi gom phần **8. Inline View là gì?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **8. Inline View là gì?**. Bây giờ chuyển sang **9. Tại sao `ROWNUM <= N` được nhưng `ROWNUM > N` có vấn đề? ⭐⭐⭐**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **9. Tại sao `ROWNUM <= N` được nhưng `ROWNUM > N` có vấn đề? ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **9. Tại sao `ROWNUM <= N` được nhưng `ROWNUM > N` có vấn đề? ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **9. Tại sao `ROWNUM <= N` được nhưng `ROWNUM > N` có vấn đề? ⭐⭐⭐**. Bây giờ chuyển sang **10. Cơ chế gán ROWNUM**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **10. Cơ chế gán ROWNUM** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **10. Cơ chế gán ROWNUM** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **10. Cơ chế gán ROWNUM**. Bây giờ chuyển sang **11. Quy tắc nhớ cực quan trọng**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11. Quy tắc nhớ cực quan trọng** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **11. Quy tắc nhớ cực quan trọng** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11. Quy tắc nhớ cực quan trọng**. Bây giờ chuyển sang **12. Ví dụ sai: lấy rank 4~6**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **12. Ví dụ sai: lấy rank 4~6** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 12. Ví dụ sai: lấy rank 4~6

Phần này nối mạch SQL với “12. Ví dụ sai: lấy rank 4~6”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

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

Khi gom phần **12. Ví dụ sai: lấy rank 4~6** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **12. Ví dụ sai: lấy rank 4~6**. Bây giờ chuyển sang **13. Cách đúng để lấy row 4~6 bằng ROWNUM**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **13. Cách đúng để lấy row 4~6 bằng ROWNUM** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **13. Cách đúng để lấy row 4~6 bằng ROWNUM** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **13. Cách đúng để lấy row 4~6 bằng ROWNUM**. Bây giờ chuyển sang **14. Tại sao alias RN giải quyết được?**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14. Tại sao alias RN giải quyết được?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **14. Tại sao alias RN giải quyết được?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14. Tại sao alias RN giải quyết được?**. Bây giờ chuyển sang **15. ROWNUM và ROW_NUMBER() khác nhau ⭐⭐⭐**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **15. ROWNUM và ROW_NUMBER() khác nhau ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 15. ROWNUM và ROW_NUMBER() khác nhau ⭐⭐⭐

Rất dễ nhầm tên.

Khi gom phần **15. ROWNUM và ROW_NUMBER() khác nhau ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **15. ROWNUM và ROW_NUMBER() khác nhau ⭐⭐⭐**. Bây giờ chuyển sang **ROWNUM**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**ROWNUM** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

### ROWNUM

Oracle pseudocolumn:

```sql
ROWNUM
```

* không cần `OVER`
* được gán trong quá trình query
* phụ thuộc query execution
* thường dùng legacy TOP-N/paging

Khi gom phần **ROWNUM** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **ROWNUM**. Bây giờ chuyển sang **ROW_NUMBER()**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **ROW_NUMBER()** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **ROW_NUMBER()** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **ROW_NUMBER()**. Bây giờ chuyển sang **16. RANK() ⭐⭐⭐**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **16. RANK() ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **16. RANK() ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **16. RANK() ⭐⭐⭐**. Bây giờ chuyển sang **17. Dùng RANK để lấy thứ hạng**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **17. Dùng RANK để lấy thứ hạng** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 17. Dùng RANK để lấy thứ hạng

Phần này nối mạch SQL với “17. Dùng RANK để lấy thứ hạng”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

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

Khi gom phần **17. Dùng RANK để lấy thứ hạng** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **17. Dùng RANK để lấy thứ hạng**. Bây giờ chuyển sang **18. Nhưng RANK có thể trả nhiều hơn N row**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **18. Nhưng RANK có thể trả nhiều hơn N row** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **18. Nhưng RANK có thể trả nhiều hơn N row** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **18. Nhưng RANK có thể trả nhiều hơn N row**. Bây giờ chuyển sang **19. RANK vs ROW_NUMBER vs DENSE_RANK**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **19. RANK vs ROW_NUMBER vs DENSE_RANK** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **19. RANK vs ROW_NUMBER vs DENSE_RANK** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **19. RANK vs ROW_NUMBER vs DENSE_RANK**. Bây giờ chuyển sang **ROW_NUMBER**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**ROW_NUMBER** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

#### ROW_NUMBER

Phần này nối mạch SQL với “ROW_NUMBER”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
1
2
3
4
```

Không quan tâm tie, mỗi row một số.

Khi gom phần **ROW_NUMBER** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **ROW_NUMBER**. Bây giờ chuyển sang **RANK**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**RANK** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

#### RANK

Phần này nối mạch SQL với “RANK”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
1
2
2
4
```

Có tie → nhảy hạng.

Khi gom phần **RANK** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **RANK**. Bây giờ chuyển sang **DENSE_RANK**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**DENSE_RANK** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

#### DENSE_RANK

Phần này nối mạch SQL với “DENSE_RANK”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

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

Khi gom phần **DENSE_RANK** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **DENSE_RANK**. Bây giờ chuyển sang **20. FETCH — cách hiện đại hơn ⭐⭐⭐**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **20. FETCH — cách hiện đại hơn ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **20. FETCH — cách hiện đại hơn ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **20. FETCH — cách hiện đại hơn ⭐⭐⭐**. Bây giờ chuyển sang **21. Cấu trúc FETCH/OFFSET**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **21. Cấu trúc FETCH/OFFSET** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **21. Cấu trúc FETCH/OFFSET** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **21. Cấu trúc FETCH/OFFSET**. Bây giờ chuyển sang **22. OFFSET**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **22. OFFSET** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 22. OFFSET

Phần này nối mạch SQL với “22. OFFSET”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

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

Khi gom phần **22. OFFSET** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **22. OFFSET**. Bây giờ chuyển sang **23. OFFSET + FETCH**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **23. OFFSET + FETCH** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **23. OFFSET + FETCH** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **23. OFFSET + FETCH**. Bây giờ chuyển sang **24. FIRST và NEXT trong FETCH**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **24. FIRST và NEXT trong FETCH** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **24. FIRST và NEXT trong FETCH** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **24. FIRST và NEXT trong FETCH**. Bây giờ chuyển sang **25. ROW và ROWS**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **25. ROW và ROWS** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **25. ROW và ROWS** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **25. ROW và ROWS**. Bây giờ chuyển sang **26. Pagination bằng OFFSET/FETCH**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **26. Pagination bằng OFFSET/FETCH** bằng câu hỏi: **ta chọn đúng đoạn kết quả nào, theo thứ tự nào, và làm sao không nhầm giữa giới hạn hàng với thứ tự xử lý?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 26. Pagination bằng OFFSET/FETCH

Ví dụ page size = 10.

Khi gom phần **26. Pagination bằng OFFSET/FETCH** lại, ta không cần nhớ các dòng như những mảnh rời: ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **26. Pagination bằng OFFSET/FETCH**. Bây giờ chuyển sang **Page 1**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Page 1** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### Page 1

Phần này nối mạch SQL với “Page 1”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
OFFSET 0 ROWS
FETCH NEXT 10 ROWS ONLY
```

→ row 1~10.

Khi gom phần **Page 1** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Page 1**. Bây giờ chuyển sang **Page 2**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Page 2** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### Page 2

Phần này nối mạch SQL với “Page 2”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
OFFSET 10 ROWS
FETCH NEXT 10 ROWS ONLY
```

→ row 11~20.

Khi gom phần **Page 2** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Page 2**. Bây giờ chuyển sang **Page 3**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Page 3** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### Page 3

Phần này nối mạch SQL với “Page 3”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

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

Khi gom phần **Page 3** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Page 3**. Bây giờ chuyển sang **27. FETCH vẫn nên có ORDER BY**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **27. FETCH vẫn nên có ORDER BY** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **27. FETCH vẫn nên có ORDER BY** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **27. FETCH vẫn nên có ORDER BY**. Bây giờ chuyển sang **28. SQL Server TOP N**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **28. SQL Server TOP N** bằng câu hỏi: **ta chọn đúng đoạn kết quả nào, theo thứ tự nào, và làm sao không nhầm giữa giới hạn hàng với thứ tự xử lý?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **28. SQL Server TOP N** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **28. SQL Server TOP N**. Bây giờ chuyển sang **29. TOP đặt ở đâu?**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **29. TOP đặt ở đâu?** bằng câu hỏi: **ta chọn đúng đoạn kết quả nào, theo thứ tự nào, và làm sao không nhầm giữa giới hạn hàng với thứ tự xử lý?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **29. TOP đặt ở đâu?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **29. TOP đặt ở đâu?**. Bây giờ chuyển sang **30. TOP N WITH TIES ⭐⭐⭐**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **30. TOP N WITH TIES ⭐⭐⭐** bằng câu hỏi: **ta chọn đúng đoạn kết quả nào, theo thứ tự nào, và làm sao không nhầm giữa giới hạn hàng với thứ tự xử lý?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **30. TOP N WITH TIES ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **30. TOP N WITH TIES ⭐⭐⭐**. Bây giờ chuyển sang **31. WITH TIES giống tư duy RANK**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **31. WITH TIES giống tư duy RANK** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **31. WITH TIES giống tư duy RANK** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **31. WITH TIES giống tư duy RANK**. Bây giờ chuyển sang **32. Một bẫy: TOP N không đảm bảo N row nếu WITH TIES**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **32. Một bẫy: TOP N không đảm bảo N row nếu WITH TIES** bằng câu hỏi: **ta chọn đúng đoạn kết quả nào, theo thứ tự nào, và làm sao không nhầm giữa giới hạn hàng với thứ tự xử lý?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 32. Một bẫy: TOP N không đảm bảo N row nếu WITH TIES

Phần này nối mạch SQL với “32. Một bẫy: TOP N không đảm bảo N row nếu WITH TIES”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

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

Khi gom phần **32. Một bẫy: TOP N không đảm bảo N row nếu WITH TIES** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **32. Một bẫy: TOP N không đảm bảo N row nếu WITH TIES**. Bây giờ chuyển sang **33. So sánh 4 phương pháp**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **33. So sánh 4 phương pháp** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 33. So sánh 4 phương pháp

Phần này nối mạch SQL với “33. So sánh 4 phương pháp”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

| Phương pháp    | DB/đặc điểm                     |                Tie |            Paging |
| -------------- | ------------------------------- | -----------------: | ----------------: |
| `ROWNUM`       | Oracle legacy                   |     không tự xử lý | có nhưng phức tạp |
| `RANK()`       | Window Function                 |      giữ cùng rank |            có thể |
| `FETCH/OFFSET` | Oracle 12c+, SQL chuẩn hiện đại |  mặc định theo row |          rất tiện |
| `TOP N`        | SQL Server                      | `WITH TIES` hỗ trợ |       chủ yếu top |

---

Khi gom phần **33. So sánh 4 phương pháp** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **33. So sánh 4 phương pháp**. Bây giờ chuyển sang **34. TOP 3 rows vs TOP 3 ranks**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **34. TOP 3 rows vs TOP 3 ranks** bằng câu hỏi: **ta chọn đúng đoạn kết quả nào, theo thứ tự nào, và làm sao không nhầm giữa giới hạn hàng với thứ tự xử lý?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **34. TOP 3 rows vs TOP 3 ranks** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **34. TOP 3 rows vs TOP 3 ranks**. Bây giờ chuyển sang **Top 3 rows**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Top 3 rows** bằng câu hỏi: **ta chọn đúng đoạn kết quả nào, theo thứ tự nào, và làm sao không nhầm giữa giới hạn hàng với thứ tự xử lý?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Top 3 rows** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Top 3 rows**. Bây giờ chuyển sang **Top 3 ranks**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Top 3 ranks** bằng câu hỏi: **ta chọn đúng đoạn kết quả nào, theo thứ tự nào, và làm sao không nhầm giữa giới hạn hàng với thứ tự xử lý?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Top 3 ranks** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Top 3 ranks**. Bây giờ chuyển sang **35. Bẫy tie khi ORDER BY không deterministic**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **35. Bẫy tie khi ORDER BY không deterministic** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **35. Bẫy tie khi ORDER BY không deterministic** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **35. Bẫy tie khi ORDER BY không deterministic**. Bây giờ chuyển sang **36. Vì sao pagination cần ORDER BY ổn định?**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **36. Vì sao pagination cần ORDER BY ổn định?** bằng câu hỏi: **ta chọn đúng đoạn kết quả nào, theo thứ tự nào, và làm sao không nhầm giữa giới hạn hàng với thứ tự xử lý?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **36. Vì sao pagination cần ORDER BY ổn định?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **36. Vì sao pagination cần ORDER BY ổn định?**. Bây giờ chuyển sang **37. Cách đọc đề SQLD nhanh**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **37. Cách đọc đề SQLD nhanh** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **37. Cách đọc đề SQLD nhanh** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **37. Cách đọc đề SQLD nhanh**. Bây giờ chuyển sang **38. So sánh các ví dụ tương đương**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **38. So sánh các ví dụ tương đương** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 38. So sánh các ví dụ tương đương

Khi gom phần **38. So sánh các ví dụ tương đương** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **38. So sánh các ví dụ tương đương**. Bây giờ chuyển sang **Oracle cổ điển**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Oracle cổ điển** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Oracle cổ điển** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Oracle cổ điển**. Bây giờ chuyển sang **Oracle hiện đại**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Oracle hiện đại** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### Oracle hiện đại

Phần này nối mạch SQL với “Oracle hiện đại”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
SELECT ENAME, SAL
FROM EMP
ORDER BY SAL DESC
FETCH FIRST 3 ROWS ONLY;
```

Dễ đọc hơn rất nhiều.

---

Khi gom phần **Oracle hiện đại** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Oracle hiện đại**. Bây giờ chuyển sang **SQL Server**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **SQL Server** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### SQL Server

Phần này nối mạch SQL với “SQL Server”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
SELECT TOP 3
       ENAME,
       SAL
FROM EMP
ORDER BY SAL DESC;
```

---

Khi gom phần **SQL Server** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **SQL Server**. Bây giờ chuyển sang **Window Function**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Window Function** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### Window Function

Phần này nối mạch SQL với “Window Function”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

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

Khi gom phần **Window Function** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Window Function**. Bây giờ chuyển sang **🔥 SQLD NOTE — 반드시 암기**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **🔥 SQLD NOTE — 반드시 암기** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 🔥 SQLD NOTE — 반드시 암기

Khi gom phần **🔥 SQLD NOTE — 반드시 암기** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **🔥 SQLD NOTE — 반드시 암기**. Bây giờ chuyển sang **① TOP-N**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **① TOP-N** bằng câu hỏi: **ta chọn đúng đoạn kết quả nào, theo thứ tự nào, và làm sao không nhầm giữa giới hạn hàng với thứ tự xử lý?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### ① TOP-N

**KR:** 전체 결과에서 상위 N개의 행을 추출한다.
**VI:** Lấy N row đầu theo một tiêu chí sắp xếp.

---

Khi gom phần **① TOP-N** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **① TOP-N**. Bây giờ chuyển sang **② ROWNUM**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **② ROWNUM** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### ② ROWNUM

Phần này nối mạch SQL với “② ROWNUM”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
Oracle pseudocolumn
```

* không phải ID thật
* không cố định
* được gán trong quá trình row được lấy

---

Khi gom phần **② ROWNUM** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **② ROWNUM**. Bây giờ chuyển sang **③ Bẫy lớn nhất**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **③ Bẫy lớn nhất** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### ③ Bẫy lớn nhất

Phần này nối mạch SQL với “③ Bẫy lớn nhất”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

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

Khi gom phần **③ Bẫy lớn nhất** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **③ Bẫy lớn nhất**. Bây giờ chuyển sang **④ Cách đúng**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **④ Cách đúng** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### ④ Cách đúng

Phần này nối mạch SQL với “④ Cách đúng”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

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

Khi gom phần **④ Cách đúng** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **④ Cách đúng**. Bây giờ chuyển sang **⑤ `ROWNUM > 1` trực tiếp không hoạt động**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑤ `ROWNUM > 1` trực tiếp không hoạt động** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### ⑤ `ROWNUM > 1` trực tiếp không hoạt động

Phần này nối mạch SQL với “⑤ `ROWNUM > 1` trực tiếp không hoạt động”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
row đầu tiên luôn thử ROWNUM=1
↓
không pass
↓
row tiếp theo lại là candidate ROWNUM=1
```

nên không lên được 2.

---

Khi gom phần **⑤ `ROWNUM > 1` trực tiếp không hoạt động** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑤ `ROWNUM > 1` trực tiếp không hoạt động**. Bây giờ chuyển sang **⑥ Paging với ROWNUM**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑥ Paging với ROWNUM** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **⑥ Paging với ROWNUM** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑥ Paging với ROWNUM**. Bây giờ chuyển sang **⑦ RANK**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑦ RANK** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### ⑦ RANK

Phần này nối mạch SQL với “⑦ RANK”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
5000 → 1
3000 → 2
3000 → 2
2975 → 4
```

Tie cùng hạng, rank sau bị skip.

---

Khi gom phần **⑦ RANK** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑦ RANK**. Bây giờ chuyển sang **⑧ FETCH**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑧ FETCH** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### ⑧ FETCH

Phần này nối mạch SQL với “⑧ FETCH”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

Khi gom phần **⑧ FETCH** lại, ta không cần nhớ các dòng như những mảnh rời: ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Như vậy, **⑧ FETCH** đã được đặt trong quan hệ giữa đầu vào, quy tắc xử lý và kết quả. Khi ôn lại, hãy tự diễn đạt ranh giới của nó rồi dùng ranh giới đó làm điểm nối sang bài tiếp theo.