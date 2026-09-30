# Set Operators

> **Mục tiêu:** UNION, UNION ALL, INTERSECT, MINUS/EXCEPT và các quy tắc kết hợp tập kết quả.

## Từ khóa cần nhớ (Keyword)

Các thuật ngữ SQLD được giữ nguyên tiếng Hàn/English trong phần nguồn. Khi ghi chú, dùng mẫu `용어 (English) (Tiếng Việt)` để nối tên gọi trong đề với ý nghĩa thực tế.

## Mạch tư duy (Logic học)

Hãy xác định **đối tượng dữ liệu** trước, sau đó đọc **điều kiện**, **phạm vi dòng**, **thứ tự xử lý** và cuối cùng kiểm tra **kết quả mong đợi**. Với SQL, luôn phân biệt điều kiện lọc trước nhóm (`WHERE`) với điều kiện lọc sau nhóm (`HAVING`).

## Mạch nối của bài học

Bài này không đứng riêng: hãy nối **Set Operators** với bài trước bằng đối tượng (object / 객체)/điều kiện mà nó tái sử dụng, rồi dùng kết quả ở phần cuối để chọn bài kế tiếp trong cùng môn. Khi gặp một truy vấn mới, nói rõ nó đang mở rộng mô hình dữ liệu, thứ tự xử lý hay cách kiểm tra kết quả nào trước khi nhớ cú pháp.

> **Cách học:** Đọc phần khái niệm → tự chạy lại các ví dụ SQL → chốt lại các mục `Keyword`, bảng so sánh và phần ghi nhớ cuối bài.

---

Để học **Set Operators** như một mạch suy luận, trước hết hãy giữ câu hỏi: **ta đang hợp, giao hay trừ các tập kết quả, và điều kiện để hai tập có thể kết hợp là gì?** Mục đích của bài là biến **UNION, UNION ALL, INTERSECT, MINUS/EXCEPT và các quy tắc kết hợp tập kết quả** thành cách đọc có thể áp dụng.

B
D
```

Nó rất hữu ích cho bài toán:

> "Tìm những đối tượng **không có** quan hệ/dữ liệu tương ứng."

---

Ta bắt đầu **29. Một lỗi dễ ra thi: Composite Key trong correlated subquery** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **29. Một lỗi dễ ra thi: Composite Key trong correlated subquery** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **29. Một lỗi dễ ra thi: Composite Key trong correlated subquery**. Bây giờ chuyển sang **📌 Quy tắc**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **📌 Quy tắc** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 📌 Quy tắc

Phần này nối mạch SQL với “📌 Quy tắc”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
Khóa ghép gồm N cột
→ khi cần xác định chính xác row, thường phải xét đủ các cột cần thiết của khóa/quan hệ.
```

---

Khi gom phần **📌 Quy tắc** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **📌 Quy tắc**. Bây giờ chuyển sang **제2절 집합 연산자 — Set Operators**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **제2절 집합 연산자 — Set Operators** bằng câu hỏi: **ta đang hợp, giao hay trừ các tập kết quả, và điều kiện để hai tập có thể kết hợp là gì?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 제2절 집합 연산자 — Set Operators

Bây giờ sang phần thứ hai trong ảnh.

Set Operator kết hợp **kết quả của các SELECT**, không phải phép nối (join / 조인) column theo chiều ngang.

Có 4 loại chính:

```text
UNION
UNION ALL
INTERSECT
MINUS / EXCEPT
```

---

Khi gom phần **제2절 집합 연산자 — Set Operators** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **제2절 집합 연산자 — Set Operators**. Bây giờ chuyển sang **30. JOIN và Set Operator khác nhau như thế nào?**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **30. JOIN và Set Operator khác nhau như thế nào?** bằng câu hỏi: **ta đang kết hợp những tập hàng nào, cột nào làm cầu nối và điều kiện nối làm thay đổi kết quả ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 30. JOIN và Set Operator khác nhau như thế nào?

Đây là cách hiểu cực nhanh.

Phép nối (join / 조인):

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

Khi gom phần **30. JOIN và Set Operator khác nhau như thế nào?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **30. JOIN và Set Operator khác nhau như thế nào?**. Bây giờ chuyển sang **31. UNION**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **31. UNION** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **31. UNION** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **31. UNION**. Bây giờ chuyển sang **32. UNION ALL**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **32. UNION ALL** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **32. UNION ALL** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **32. UNION ALL**. Bây giờ chuyển sang **UNION vs UNION ALL**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **UNION vs UNION ALL** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **UNION vs UNION ALL** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **UNION vs UNION ALL**. Bây giờ chuyển sang **33. INTERSECT — Giao tập hợp**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **33. INTERSECT — Giao tập hợp** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **33. INTERSECT — Giao tập hợp** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **33. INTERSECT — Giao tập hợp**. Bây giờ chuyển sang **34. MINUS / EXCEPT — Hiệu tập hợp**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **34. MINUS / EXCEPT — Hiệu tập hợp** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **34. MINUS / EXCEPT — Hiệu tập hợp** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **34. MINUS / EXCEPT — Hiệu tập hợp**. Bây giờ chuyển sang **Mẹo nhớ**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Mẹo nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Mẹo nhớ

Phần này nối mạch SQL với “Mẹo nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
MINUS
= lấy bên TRÊN
  trừ bên DƯỚI
```

---

Khi gom phần **Mẹo nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Mẹo nhớ**. Bây giờ chuyển sang **35. Điều kiện sử dụng Set Operator**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **35. Điều kiện sử dụng Set Operator** bằng câu hỏi: **ta đang hợp, giao hay trừ các tập kết quả, và điều kiện để hai tập có thể kết hợp là gì?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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
→ dữ liệu (data / 데이터) kiểu (type / 타입) của các column ở cùng vị trí phải tương thích.

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

Khi gom phần **35. Điều kiện sử dụng Set Operator** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **35. Điều kiện sử dụng Set Operator**. Bây giờ chuyển sang **36. Tên column kết quả lấy từ SELECT đầu tiên**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **36. Tên column kết quả lấy từ SELECT đầu tiên** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 36. Tên column kết quả lấy từ SELECT đầu tiên

Ảnh nhấn mạnh:

**전체 집합의 컬럼명과 데이터 타입은 첫 번째 집합에 의해 결정된다.**
→ Tên cột hiển thị của kết quả set thao tác (operation / 연산) chủ yếu dựa vào SELECT đầu tiên; kiểu dữ liệu phải tương thích giữa các nhánh.

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

Tên đầu ra (output / 출력):

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

Khi gom phần **36. Tên column kết quả lấy từ SELECT đầu tiên** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **36. Tên column kết quả lấy từ SELECT đầu tiên**. Bây giờ chuyển sang **37. ORDER BY với Set Operator**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **37. ORDER BY với Set Operator** bằng câu hỏi: **ta đang hợp, giao hay trừ các tập kết quả, và điều kiện để hai tập có thể kết hợp là gì?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 37. ORDER BY với Set Operator

Ảnh có câu rất quan trọng:

**개별 SELECT 문에는 thứ tự (order / 순서) BY를 사용할 수 없고 전체 집합 결과의 마지막에 사용한다.**
→ Trong dạng set truy vấn (query / 쿼리) thông thường, `ORDER BY` được đặt ở **cuối toàn bộ phép tập hợp**, không đặt trực tiếp sau từng SELECT thành phần.

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

Khi gom phần **37. ORDER BY với Set Operator** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **37. ORDER BY với Set Operator**. Bây giờ chuyển sang **38. GROUP BY thì sao?**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **38. GROUP BY thì sao?** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Vì `GROUP BY` là lô-gic (logic / 논리) nội bộ của từng SELECT.

Còn `ORDER BY` thường dùng để sắp xếp **kết quả cuối cùng**.

---

Khi gom phần **38. GROUP BY thì sao?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **38. GROUP BY thì sao?**. Bây giờ chuyển sang **39. Tổng hợp toàn bộ Subquery bằng một sơ đồ**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **39. Tổng hợp toàn bộ Subquery bằng một sơ đồ** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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
* `Correlated` mô tả **quan hệ phụ thuộc với main truy vấn (query / 쿼리)**.

Đây là chỗ rất nhiều người học nhầm.

---

Khi gom phần **39. Tổng hợp toàn bộ Subquery bằng một sơ đồ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **39. Tổng hợp toàn bộ Subquery bằng một sơ đồ**. Bây giờ chuyển sang **40. 📌 NOTE 시험 — phần phải nhớ trước khi thi**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **40. 📌 NOTE 시험 — phần phải nhớ trước khi thi** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 40. 📌 NOTE 시험 — phần phải nhớ trước khi thi

Khi gom phần **40. 📌 NOTE 시험 — phần phải nhớ trước khi thi** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **40. 📌 NOTE 시험 — phần phải nhớ trước khi thi**. Bây giờ chuyển sang **⭐ Subquery**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⭐ Subquery** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⭐ Subquery

Phần này nối mạch SQL với “⭐ Subquery”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
서브쿼리
= SQL 안의 SQL
= query nằm trong query
```

Khi gom phần **⭐ Subquery** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⭐ Subquery**. Bây giờ chuyển sang **⭐ Theo vị trí**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⭐ Theo vị trí** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⭐ Theo vị trí

Phần này nối mạch SQL với “⭐ Theo vị trí”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
SELECT → Scalar Subquery
FROM   → Inline View
WHERE/HAVING → Nested Subquery
```

Khi gom phần **⭐ Theo vị trí** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⭐ Theo vị trí**. Bây giờ chuyển sang **⭐ Scalar**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⭐ Scalar** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **⭐ Scalar** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⭐ Scalar**. Bây giờ chuyển sang **⭐ Single-row**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⭐ Single-row** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⭐ Single-row

Phần này nối mạch SQL với “⭐ Single-row”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
=, <>, >, >=, <, <=
```

Khi gom phần **⭐ Single-row** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⭐ Single-row**. Bây giờ chuyển sang **⭐ Multi-row**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⭐ Multi-row** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⭐ Multi-row

Phần này nối mạch SQL với “⭐ Multi-row”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
IN
ANY
ALL
EXISTS
```

Khi gom phần **⭐ Multi-row** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⭐ Multi-row**. Bây giờ chuyển sang **⭐ ANY / ALL**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⭐ ANY / ALL** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⭐ ANY / ALL

Phần này nối mạch SQL với “⭐ ANY / ALL”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
> ANY → > MIN
< ANY → < MAX

> ALL → > MAX
< ALL → < MIN
```

Khi gom phần **⭐ ANY / ALL** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⭐ ANY / ALL**. Bây giờ chuyển sang **⭐ Correlated**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⭐ Correlated** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⭐ Correlated

Nhìn thấy kiểu:

```sql
Subquery:
WHERE E1.DEPTNO = E2.DEPTNO
```

trong đó `E1` thuộc outer/main truy vấn (query / 쿼리) →

Khi gom phần **⭐ Correlated** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Như vậy, **⭐ Correlated** đã được đặt trong quan hệ giữa đầu vào, quy tắc xử lý và kết quả. Khi ôn lại, hãy tự diễn đạt ranh giới của nó rồi dùng ranh giới đó làm điểm nối sang bài tiếp theo.