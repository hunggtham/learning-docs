# Subquery

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Subquery**. Route đi từ correlated/un correlated scope → scalar/EXISTS/IN semantics → NULL and duplicate behavior → rewrite to joins/CTEs → optimizer consequences, để truy vấn lồng được hiểu qua quan hệ và kế hoạch.

> **Mục tiêu:** Single/multi-row, correlated, scalar, inline view, EXISTS và các bẫy thường gặp.

## Từ khóa cần nhớ (Keyword)

Phần giải thích dùng tiếng Việt trước. Ở mọi lần xuất hiện, thuật ngữ SQLD dùng dạng `nghĩa Việt (English / 한국어)` để vừa giữ mạch đọc vừa đối chiếu được từ khóa trong đề.

> **Chuyển mạch:** Trong **Subquery**, **Mạch tư duy (Logic học)** tiếp nhận điểm tựa từ **Từ khóa cần nhớ (Keyword)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mạch nối của bài học** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mạch tư duy (Logic học)

Hãy xác định **đối tượng dữ liệu** trước, sau đó đọc **điều kiện**, **phạm vi dòng**, **thứ tự xử lý** và cuối cùng kiểm tra **kết quả mong đợi**. Với SQL, luôn phân biệt điều kiện lọc trước nhóm (`WHERE`) với điều kiện lọc sau nhóm (`HAVING`); đây là cầu nối để hiểu vì sao cùng một truy vấn có thể cho kết quả khác nhau.

> **Chuyển mạch:** Ở chặng này của **Subquery**, **Mạch nối của bài học** tiếp nhận điểm tựa từ **Mạch tư duy (Logic học)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mạch nối của bài học

Bài này không đứng riêng: hãy nối **Subquery** với bài trước bằng đối tượng dữ liệu/điều kiện mà nó tái sử dụng, rồi dùng kết quả ở phần cuối để chọn bài kế tiếp trong cùng môn. Khi gặp một truy vấn mới, nói rõ nó đang mở rộng mô hình dữ liệu, thứ tự xử lý hay cách kiểm tra kết quả nào trước khi nhớ cú pháp.

> **Cách học:** Đọc phần khái niệm → tự chạy lại các ví dụ SQL → chốt lại mục **từ khóa (Keyword)**, bảng so sánh và phần ghi nhớ cuối bài.

---

Để học **Subquery** như một mạch suy luận, trước hết hãy giữ câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Mục đích của bài là biến **Single/multi-row, correlated, scalar, inline view, EXISTS và các bẫy thường gặp** thành cách đọc có thể áp dụng.

→ NULL 제외

AVG(col)
= SUM(col) / COUNT(col)

전체 행을 기준으로 나누려면
= SUM(col) / COUNT(*)
```

```
[IDENTIFIER]

본질식별자
= 업무에서 자연스럽게 존재
= Natural / Business Identifier

인조식별자
= 시스템에서 인위적으로 생성
= Surrogate Identifier
= Sequence / Auto-generated ID 등
```

Và **một câu để nhớ toàn bộ phần 인조식별자**:

> **인조식별자는 PK를 단순하게 만들어 개발은 편리하지만, 업무적으로 유일해야 하는 값의 중복까지 자동으로 막아주는 것은 아니다.**
Surrogate key làm PK đơn giản và giúp phát triển thuận tiện, nhưng **không tự động bảo vệ tính duy nhất của business key**.
>

Ví dụ điển hình:

```
PK = ORDER_DETAIL_ID

nhưng business rule:
(ORDER_ID, PRODUCT_ID) phải unique

→ cần UNIQUE(ORDER_ID, PRODUCT_ID)
  nếu nghiệp vụ thực sự yêu cầu không trùng.
```

Đây chính là mối liên hệ quan trọng nhất giữa **PK – 본질식별자 – 인조식별자 – UNIQUE – 데이터 무결성** mà đề SQLD có thể biến thành câu hỏi đánh lừa.

Mình sẽ tiếp tục đúng format học SQLD đã thống nhất: **bám sát nội dung ảnh → 1 ý tiếng Hàn + 1 ý tiếng Việt → giải thích keyword ngay tại chỗ → sau đó mở rộng phần dễ nhầm/dễ ra thi → cuối bài có `📌 NOTE 시험` để ôn nhanh.**

Ta bắt đầu **제1절 서브쿼리 — Subquery** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 제1절 서브쿼리 — Subquery

Khi gom phần **제1절 서브쿼리 — Subquery** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **제1절 서브쿼리 — Subquery**. Bây giờ chuyển sang **1. 서브쿼리란 무엇인가? — Subquery là gì?**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1. 서브쿼리란 무엇인가? — Subquery là gì?** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **1. 서브쿼리란 무엇인가? — Subquery là gì?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1. 서브쿼리란 무엇인가? — Subquery là gì?**. Bây giờ chuyển sang **2. 서브쿼리 사용 시 주의사항 — Quy tắc khi dùng Subquery**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2. 서브쿼리 사용 시 주의사항 — Quy tắc khi dùng Subquery** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 2. 서브쿼리 사용 시 주의사항 — Quy tắc khi dùng Subquery

Khi gom phần **2. 서브쿼리 사용 시 주의사항 — Quy tắc khi dùng Subquery** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2. 서브쿼리 사용 시 주의사항 — Quy tắc khi dùng Subquery**. Bây giờ chuyển sang **2.1 괄호로 감싸서 사용한다**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2.1 괄호로 감싸서 사용한다** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **2.1 괄호로 감싸서 사용한다** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2.1 괄호로 감싸서 사용한다**. Bây giờ chuyển sang **2.2 단일행 연산자와 다중행 연산자를 구분한다**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2.2 단일행 연산자와 다중행 연산자를 구분한다** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **2.2 단일행 연산자와 다중행 연산자를 구분한다** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2.2 단일행 연산자와 다중행 연산자를 구분한다**. Bây giờ chuyển sang **3. 서브쿼리가 위치할 수 있는 곳 — Subquery có thể nằm ở đâu?**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3. 서브쿼리가 위치할 수 있는 곳 — Subquery có thể nằm ở đâu?** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **3. 서브쿼리가 위치할 수 있는 곳 — Subquery có thể nằm ở đâu?** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3. 서브쿼리가 위치할 수 있는 곳 — Subquery có thể nằm ở đâu?**. Bây giờ chuyển sang **4. 연관 서브쿼리 vs 비연관 서브쿼리**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4. 연관 서브쿼리 vs 비연관 서브쿼리** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 4. 연관 서브쿼리 vs 비연관 서브쿼리

Đây là một cách phân loại **theo quan hệ với main query**.

Khi gom phần **4. 연관 서브쿼리 vs 비연관 서브쿼리** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4. 연관 서브쿼리 vs 비연관 서브쿼리**. Bây giờ chuyển sang **4.1 연관 서브쿼리 — Correlated Subquery**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4.1 연관 서브쿼리 — Correlated Subquery** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **4.1 연관 서브쿼리 — Correlated Subquery** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4.1 연관 서브쿼리 — Correlated Subquery**. Bây giờ chuyển sang **4.2 비연관 서브쿼리 — Uncorrelated Subquery**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4.2 비연관 서브쿼리 — Uncorrelated Subquery** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **4.2 비연관 서브쿼리 — Uncorrelated Subquery** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4.2 비연관 서브쿼리 — Uncorrelated Subquery**. Bây giờ chuyển sang **📌 Điểm nhớ**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **📌 Điểm nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 📌 Điểm nhớ

Phần này nối mạch SQL với “📌 Điểm nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
Correlated
→ cần giá trị từ Main Query

Uncorrelated
→ tự chạy độc lập được
```

---

Khi gom phần **📌 Điểm nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **📌 Điểm nhớ**. Bây giờ chuyển sang **5. 반환 데이터에 따른 분류 — Phân loại theo dữ liệu trả về**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5. 반환 데이터에 따른 분류 — Phân loại theo dữ liệu trả về** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 5. 반환 데이터에 따른 분류 — Phân loại theo dữ liệu trả về

Ảnh chia thành ba loại rất quan trọng:

```text
Subquery
├─ 단일행 서브쿼리
├─ 다중행 서브쿼리
└─ 다중컬럼 서브쿼리
```

---

Khi gom phần **5. 반환 데이터에 따른 분류 — Phân loại theo dữ liệu trả về** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5. 반환 데이터에 따른 분류 — Phân loại theo dữ liệu trả về**. Bây giờ chuyển sang **6. 단일행 서브쿼리 — Single-row Subquery**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6. 단일행 서브쿼리 — Single-row Subquery** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **6. 단일행 서브쿼리 — Single-row Subquery** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6. 단일행 서브쿼리 — Single-row Subquery**. Bây giờ chuyển sang **7. 다중행 서브쿼리 — Multi-row Subquery**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7. 다중행 서브쿼리 — Multi-row Subquery** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **7. 다중행 서브쿼리 — Multi-row Subquery** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7. 다중행 서브쿼리 — Multi-row Subquery**. Bây giờ chuyển sang **8. IN — Có nằm trong tập kết quả không?**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **8. IN — Có nằm trong tập kết quả không?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **8. IN — Có nằm trong tập kết quả không?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **8. IN — Có nằm trong tập kết quả không?**. Bây giờ chuyển sang **9. ANY — Chỉ cần đúng với ít nhất một giá trị**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **9. ANY — Chỉ cần đúng với ít nhất một giá trị** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **9. ANY — Chỉ cần đúng với ít nhất một giá trị** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **9. ANY — Chỉ cần đúng với ít nhất một giá trị**. Bây giờ chuyển sang **Mẹo nhớ**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Mẹo nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Mẹo nhớ

Phần này nối mạch SQL với “Mẹo nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
ANY = ít nhất MỘT đứa
```

---

Khi gom phần **Mẹo nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Mẹo nhớ**. Bây giờ chuyển sang **10. ALL — Phải đúng với tất cả**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **10. ALL — Phải đúng với tất cả** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **10. ALL — Phải đúng với tất cả** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **10. ALL — Phải đúng với tất cả**. Bây giờ chuyển sang **Bảng phải thuộc lòng**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Bảng phải thuộc lòng** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Bảng phải thuộc lòng** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Bảng phải thuộc lòng**. Bây giờ chuyển sang **11. 다중컬럼 서브쿼리 — Multi-column Subquery**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11. 다중컬럼 서브쿼리 — Multi-column Subquery** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 11. 다중컬럼 서브쿼리 — Multi-column Subquery

**다중컬럼 서브쿼리는 여러 컬럼을 동시에 반환한다.**
→ Multi-column subquery trả về nhiều cột cùng lúc.

Ví dụ trong ảnh:

```sql
SELECT EMPNO, ENAME, SAL, DEPTNO
FROM EMP
WHERE (DEPTNO, SAL) IN (
    SELECT DEPTNO, MAX(SAL)
    FROM EMP
    GROUP BY DEPTNO
);
```

Subquery có thể tạo:

```text
DEPTNO | MAX(SAL)
-------+---------
10     | 5000
20     | 4000
30     | 3500
```

Main query kiểm tra theo **cặp giá trị**:

```text
(DEPTNO, SAL)
```

Ví dụ:

```text
(10,5000) → match
(10,3000) → không
(20,4000) → match
```

Mục tiêu của câu SQL:

> Tìm nhân viên có mức lương cao nhất của từng department.

---

Khi gom phần **11. 다중컬럼 서브쿼리 — Multi-column Subquery** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11. 다중컬럼 서브쿼리 — Multi-column Subquery**. Bây giờ chuyển sang **12. 스칼라 서브쿼리 — Scalar Subquery**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **12. 스칼라 서브쿼리 — Scalar Subquery** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 12. 스칼라 서브쿼리 — Scalar Subquery

Đây là phần trọng tâm của ảnh.

**스칼라 서브쿼리는 SELECT 절에서 하나의 값처럼 사용되는 서브쿼리이다.**
→ Scalar Subquery là subquery được sử dụng giống như **một giá trị đơn**.

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

Hãy nhìn nó như một column:

```text
p.id
p.name
p.price
[SUBQUERY] → artist_name
```

Kết quả:

```text
id   name       price      artist_name
101  숲과 나    1100000    이지현
102  밤의 도시   1350000    이지현
103  파도        470000     황현석
...
```

---

Khi gom phần **12. 스칼라 서브쿼리 — Scalar Subquery** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **12. 스칼라 서브쿼리 — Scalar Subquery**. Bây giờ chuyển sang **13. Tại sao Scalar Subquery phải trả về 1 giá trị?**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **13. Tại sao Scalar Subquery phải trả về 1 giá trị?** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 13. Tại sao Scalar Subquery phải trả về 1 giá trị?

**스칼라 서브쿼리는 하나의 컬럼 위치에서 사용되므로 단일 값을 반환해야 한다.**
→ Vì scalar subquery chiếm vị trí của **một ô**, nên nó phải trả về một giá trị scalar.

Ví dụ một row của kết quả:

```text
101 | 숲과 나 | 1,100,000 | ???
```

Vị trí `???` chỉ là **một cell**.

Do đó subquery không thể trả:

```text
이지현
황현석
박성진
```

vào cùng một cell.

---

Khi gom phần **13. Tại sao Scalar Subquery phải trả về 1 giá trị?** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **13. Tại sao Scalar Subquery phải trả về 1 giá trị?**. Bây giờ chuyển sang **14. Scalar Subquery và LEFT OUTER JOIN**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14. Scalar Subquery và LEFT OUTER JOIN** bằng câu hỏi: **ta đang kết hợp những tập hàng nào, cột nào làm cầu nối và điều kiện nối làm thay đổi kết quả ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **14. Scalar Subquery và LEFT OUTER JOIN** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14. Scalar Subquery và LEFT OUTER JOIN**. Bây giờ chuyển sang **15. Một ví dụ Scalar Subquery rất quan trọng**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **15. Một ví dụ Scalar Subquery rất quan trọng** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **15. Một ví dụ Scalar Subquery rất quan trọng** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **15. Một ví dụ Scalar Subquery rất quan trọng**. Bây giờ chuyển sang **16. Scalar Subquery với SUM()**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **16. Scalar Subquery với SUM()** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **16. Scalar Subquery với SUM()** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **16. Scalar Subquery với SUM()**. Bây giờ chuyển sang **17. 인라인 뷰 — Inline View**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **17. 인라인 뷰 — Inline View** bằng câu hỏi: **cấu trúc hoặc ràng buộc nào đang bảo vệ dữ liệu, và thay đổi đó ảnh hưởng đến các câu lệnh sau ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **17. 인라인 뷰 — Inline View** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **17. 인라인 뷰 — Inline View**. Bây giờ chuyển sang **18. Tại sao Inline View được gọi là Dynamic View?**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **18. Tại sao Inline View được gọi là Dynamic View?** bằng câu hỏi: **cấu trúc hoặc ràng buộc nào đang bảo vệ dữ liệu, và thay đổi đó ảnh hưởng đến các câu lệnh sau ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **18. Tại sao Inline View được gọi là Dynamic View?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **18. Tại sao Inline View được gọi là Dynamic View?**. Bây giờ chuyển sang **19. Inline View và JOIN — phần rất dễ nhầm**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **19. Inline View và JOIN — phần rất dễ nhầm** bằng câu hỏi: **ta đang kết hợp những tập hàng nào, cột nào làm cầu nối và điều kiện nối làm thay đổi kết quả ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **19. Inline View và JOIN — phần rất dễ nhầm** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **19. Inline View và JOIN — phần rất dễ nhầm**. Bây giờ chuyển sang **20. Cartesian Product khi quên JOIN condition**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **20. Cartesian Product khi quên JOIN condition** bằng câu hỏi: **ta đang kết hợp những tập hàng nào, cột nào làm cầu nối và điều kiện nối làm thay đổi kết quả ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **20. Cartesian Product khi quên JOIN condition** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **20. Cartesian Product khi quên JOIN condition**. Bây giờ chuyển sang **21. Scalar Subquery vs Inline View**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **21. Scalar Subquery vs Inline View** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

## 21. Scalar Subquery vs Inline View

Đây là phần ảnh so sánh trực tiếp.

Khi gom phần **21. Scalar Subquery vs Inline View** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **21. Scalar Subquery vs Inline View**. Bây giờ chuyển sang **Scalar**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Scalar** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Scalar** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Scalar**. Bây giờ chuyển sang **Inline View**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Inline View** bằng câu hỏi: **cấu trúc hoặc ràng buộc nào đang bảo vệ dữ liệu, và thay đổi đó ảnh hưởng đến các câu lệnh sau ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Inline View** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Inline View**. Bây giờ chuyển sang **Cách nhớ**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Đoạn **Cách nhớ** đổi quy tắc thành hình ảnh hoặc câu nhớ. Hãy trả lời: **hình ảnh hoặc câu nhớ này đang nén quan hệ nào để ta có thể tự dựng lại kết quả mà không học thuộc cú pháp?** Sau đó quay lại điều kiện SQL để chắc rằng cách nhớ không làm mất trường hợp biên.

#### Cách nhớ

Phần này nối mạch SQL với “Cách nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
Scalar Subquery
→ tạo VALUE

Inline View
→ tạo TABLE
```

---

Khi gom phần **Cách nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Cách nhớ**. Bây giờ chuyển sang **22. 중첩 서브쿼리 — Nested Subquery**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **22. 중첩 서브쿼리 — Nested Subquery** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **22. 중첩 서브쿼리 — Nested Subquery** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **22. 중첩 서브쿼리 — Nested Subquery**. Bây giờ chuyển sang **23. 상호연관 서브쿼리 — Correlated Subquery sâu hơn**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **23. 상호연관 서브쿼리 — Correlated Subquery sâu hơn** bằng câu hỏi: **truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **23. 상호연관 서브쿼리 — Correlated Subquery sâu hơn** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **23. 상호연관 서브쿼리 — Correlated Subquery sâu hơn**. Bây giờ chuyển sang **24. 상호 연관 서브쿼리의 논리적 순서**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **24. 상호 연관 서브쿼리의 논리적 순서** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **24. 상호 연관 서브쿼리의 논리적 순서** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **24. 상호 연관 서브쿼리의 논리적 순서**. Bây giờ chuyển sang **25. HAVING절에서 서브쿼리**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **25. HAVING절에서 서브쿼리** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **25. HAVING절에서 서브쿼리** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **25. HAVING절에서 서브쿼리**. Bây giờ chuyển sang **26. UPDATE SET에서 서브쿼리**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **26. UPDATE SET에서 서브쿼리** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **26. UPDATE SET에서 서브쿼리** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **26. UPDATE SET에서 서브쿼리**. Bây giờ chuyển sang **27. EXISTS**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **27. EXISTS** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **27. EXISTS** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **27. EXISTS**. Bây giờ chuyển sang **28. NOT EXISTS**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **28. NOT EXISTS** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **28. NOT EXISTS** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Như vậy, **28. NOT EXISTS** đã được đặt trong quan hệ giữa đầu vào, quy tắc xử lý và kết quả. Khi ôn lại, hãy tự diễn đạt ranh giới của nó rồi dùng ranh giới đó làm điểm nối sang bài tiếp theo.

> **Bàn giao:** Sau **Mạch nối của bài học**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
