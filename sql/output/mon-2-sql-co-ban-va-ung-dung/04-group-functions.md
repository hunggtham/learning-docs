# Group Functions

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Group functions**. Route đi từ row-level values → GROUP BY grain → aggregate semantics → HAVING/filter order → NULL and precision behavior, để tổng hợp giữ đúng cấp độ dữ liệu.

> **Mục tiêu:** Aggregate, GROUP BY, ROLLUP, CUBE, GROUPING và GROUPING SETS.

## Từ khóa cần nhớ (Keyword)

Phần giải thích dùng tiếng Việt trước. Ở mọi lần xuất hiện, thuật ngữ SQLD dùng dạng `nghĩa Việt (English / 한국어)` để vừa giữ mạch đọc vừa đối chiếu được từ khóa trong đề.

> **Chuyển mạch:** Trong **Group Functions**, **Mạch tư duy (Logic học)** tiếp nhận điểm tựa từ **Từ khóa cần nhớ (Keyword)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mạch nối của bài học** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mạch tư duy (Logic học)

Hãy xác định **đối tượng dữ liệu** trước, sau đó đọc **điều kiện**, **phạm vi dòng**, **thứ tự xử lý** và cuối cùng kiểm tra **kết quả mong đợi**. Với SQL, luôn phân biệt điều kiện lọc trước nhóm (`WHERE`) với điều kiện lọc sau nhóm (`HAVING`); đây là cầu nối để hiểu vì sao cùng một truy vấn có thể cho kết quả khác nhau.

> **Chuyển mạch:** Ở chặng này của **Group Functions**, **Mạch nối của bài học** tiếp nhận điểm tựa từ **Mạch tư duy (Logic học)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **제3절 그룹 함수 — Group Function** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mạch nối của bài học

Bài này không đứng riêng: hãy nối **Group Functions** với bài trước bằng đối tượng dữ liệu/điều kiện mà nó tái sử dụng, rồi dùng kết quả ở phần cuối để chọn bài kế tiếp trong cùng môn. Khi gặp một truy vấn mới, nói rõ nó đang mở rộng mô hình dữ liệu, thứ tự xử lý hay cách kiểm tra kết quả nào trước khi nhớ cú pháp.

> **Cách học:** Đọc phần khái niệm → tự chạy lại các ví dụ SQL → chốt lại mục **từ khóa (Keyword)**, bảng so sánh và phần ghi nhớ cuối bài.

---

Để học **Group Functions** như một mạch suy luận, trước hết hãy giữ câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Mục đích của bài là biến **Aggregate, GROUP BY, ROLLUP, CUBE, GROUPING và GROUPING SETS** thành cách đọc có thể áp dụng.

```text
상관/연관 서브쿼리
Correlated Subquery
```

Ta bắt đầu **⭐ Inline View** bằng câu hỏi: **cấu trúc hoặc ràng buộc nào đang bảo vệ dữ liệu, và thay đổi đó ảnh hưởng đến các câu lệnh sau ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⭐ Inline View

Phần này nối mạch SQL với “⭐ Inline View”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
FROM (
    SELECT ...
)
```

→ hãy tưởng tượng subquery **tạo ra một table tạm logic**.

Khi gom phần **⭐ Inline View** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⭐ Inline View**. Bây giờ chuyển sang **⭐ EXISTS**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⭐ EXISTS** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⭐ EXISTS

Phần này nối mạch SQL với “⭐ EXISTS”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
EXISTS
→ Có ít nhất 1 row?

NOT EXISTS
→ Không có row nào?
```

Khi gom phần **⭐ EXISTS** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⭐ EXISTS**. Bây giờ chuyển sang **⭐ Set Operators**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⭐ Set Operators** bằng câu hỏi: **ta đang hợp, giao hay trừ các tập kết quả, và điều kiện để hai tập có thể kết hợp là gì?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **⭐ Set Operators** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⭐ Set Operators**. Bây giờ chuyển sang **⭐ Cạm bẫy cực hay thi**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⭐ Cạm bẫy cực hay thi** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **⭐ Cạm bẫy cực hay thi** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⭐ Cạm bẫy cực hay thi**. Bây giờ chuyển sang **제3절 그룹 함수 — Group Function**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **제3절 그룹 함수 — Group Function** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Group Functions**, **제3절 그룹 함수 — Group Function** tiếp nhận điểm tựa từ **Mạch nối của bài học** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **2. 집계 함수 — Aggregate Function** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 제3절 그룹 함수 — Group Function

Khi gom phần **제3절 그룹 함수 — Group Function** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **제3절 그룹 함수 — Group Function**. Bây giờ chuyển sang **1. Ba nhóm hàm phân tích dữ liệu trong SQL**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1. Ba nhóm hàm phân tích dữ liệu trong SQL** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **1. Ba nhóm hàm phân tích dữ liệu trong SQL** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1. Ba nhóm hàm phân tích dữ liệu trong SQL**. Bây giờ chuyển sang **2. 집계 함수 — Aggregate Function**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2. 집계 함수 — Aggregate Function** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Group Functions**, **2. 집계 함수 — Aggregate Function** tiếp nhận điểm tựa từ **제3절 그룹 함수 — Group Function** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. SUM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. 집계 함수 — Aggregate Function

Điểm quan trọng nhất của phần này:

> **집계 함수는 일반적으로 NULL을 제외한다.**
> Các Aggregate Function **thường bỏ qua NULL**.

Đây là kiến thức rất dễ xuất hiện trong SQLD.

---

Khi gom phần **2. 집계 함수 — Aggregate Function** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2. 집계 함수 — Aggregate Function**. Bây giờ chuyển sang **2.1 COUNT**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2.1 COUNT** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### 2.1 COUNT

**KR:** `COUNT`는 행의 수를 계산하는 함수이다.
**VI:** `COUNT` là hàm dùng để **đếm số dòng/số giá trị**.

Nhưng phải phân biệt:

```sql
COUNT(*)
COUNT(SAL)
COUNT(EMPNO)
```

Khi gom phần **2.1 COUNT** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2.1 COUNT**. Bây giờ chuyển sang **`COUNT(*)`**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **`COUNT(*)`** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **`COUNT(*)`** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **`COUNT(*)`**. Bây giờ chuyển sang **`COUNT(SAL)`**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **`COUNT(SAL)`** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### `COUNT(SAL)`

**KR:** `COUNT(컬럼)`은 해당 컬럼에서 NULL이 아닌 값만 계산한다.
**VI:** `COUNT(column)` chỉ đếm những row mà column đó **không phải NULL**.

```sql
COUNT(SAL)
```

→ `2`

Do SAL của nhân viên 2 là NULL.

Khi gom phần **`COUNT(SAL)`** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **`COUNT(SAL)`**. Bây giờ chuyển sang **Mẹo SQLD**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Mẹo SQLD** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Mẹo SQLD** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Mẹo SQLD**. Bây giờ chuyển sang **3. SUM**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3. SUM** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Group Functions**, **3. SUM** tiếp nhận điểm tựa từ **2. 집계 함수 — Aggregate Function** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. AVG — phần rất dễ ra đề** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **3. SUM** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3. SUM**. Bây giờ chuyển sang **4. AVG — phần rất dễ ra đề**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4. AVG — phần rất dễ ra đề** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Group Functions**, **4. AVG — phần rất dễ ra đề** tiếp nhận điểm tựa từ **3. SUM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. MIN / MAX** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **4. AVG — phần rất dễ ra đề** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4. AVG — phần rất dễ ra đề**. Bây giờ chuyển sang **AVG(SAL) khác AVG(NVL(SAL,0))**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **AVG(SAL) khác AVG(NVL(SAL,0))** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **AVG(SAL) khác AVG(NVL(SAL,0))** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **AVG(SAL) khác AVG(NVL(SAL,0))**. Bây giờ chuyển sang **Một quan hệ rất đáng nhớ**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Một quan hệ rất đáng nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Một quan hệ rất đáng nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Một quan hệ rất đáng nhớ**. Bây giờ chuyển sang **5. MIN / MAX**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5. MIN / MAX** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Group Functions**, **5. MIN / MAX** tiếp nhận điểm tựa từ **4. AVG — phần rất dễ ra đề** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. VARIANCE / STDDEV** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **5. MIN / MAX** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5. MIN / MAX**. Bây giờ chuyển sang **6. VARIANCE / STDDEV**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6. VARIANCE / STDDEV** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Group Functions**, **6. VARIANCE / STDDEV** tiếp nhận điểm tựa từ **5. MIN / MAX** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. GROUP BY cơ bản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. VARIANCE / STDDEV

**KR:** `VARIANCE`는 분산을, `STDDEV`는 표준편차를 계산한다.
**VI:** `VARIANCE` tính **phương sai**, còn `STDDEV` tính **độ lệch chuẩn**.

Quan hệ:

```text
STDDEV ≈ √VARIANCE
```

SQLD chủ yếu yêu cầu hiểu ý nghĩa, thường không cần tự tính toán thống kê phức tạp.

---

Khi gom phần **6. VARIANCE / STDDEV** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6. VARIANCE / STDDEV**. Bây giờ chuyển sang **7. GROUP BY cơ bản**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7. GROUP BY cơ bản** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Group Functions**, **7. GROUP BY cơ bản** tiếp nhận điểm tựa từ **6. VARIANCE / STDDEV** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. GROUP BY không tự ORDER BY** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **7. GROUP BY cơ bản** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7. GROUP BY cơ bản**. Bây giờ chuyển sang **8. GROUP BY không tự ORDER BY**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **8. GROUP BY không tự ORDER BY** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Group Functions**, **8. GROUP BY không tự ORDER BY** tiếp nhận điểm tựa từ **7. GROUP BY cơ bản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. ROLLUP ⭐⭐⭐** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **8. GROUP BY không tự ORDER BY** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **8. GROUP BY không tự ORDER BY**. Bây giờ chuyển sang **9. ROLLUP ⭐⭐⭐**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **9. ROLLUP ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Group Functions**, **9. ROLLUP ⭐⭐⭐** tiếp nhận điểm tựa từ **8. GROUP BY không tự ORDER BY** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Tại sao ROLLUP(A,B) có N+1 level?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **9. ROLLUP ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **9. ROLLUP ⭐⭐⭐**. Bây giờ chuyển sang **9.1 ROLLUP(A,B)**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **9.1 ROLLUP(A,B)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **9.1 ROLLUP(A,B)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **9.1 ROLLUP(A,B)**. Bây giờ chuyển sang **10. Tại sao ROLLUP(A,B) có N+1 level?**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **10. Tại sao ROLLUP(A,B) có N+1 level?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Group Functions**, **10. Tại sao ROLLUP(A,B) có N+1 level?** tiếp nhận điểm tựa từ **9. ROLLUP ⭐⭐⭐** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Thứ tự ROLLUP cực kỳ quan trọng ⭐⭐⭐** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **10. Tại sao ROLLUP(A,B) có N+1 level?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **10. Tại sao ROLLUP(A,B) có N+1 level?**. Bây giờ chuyển sang **Công thức nhớ**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Công thức nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Công thức nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Công thức nhớ**. Bây giờ chuyển sang **11. Thứ tự ROLLUP cực kỳ quan trọng ⭐⭐⭐**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11. Thứ tự ROLLUP cực kỳ quan trọng ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Group Functions**, **11. Thứ tự ROLLUP cực kỳ quan trọng ⭐⭐⭐** tiếp nhận điểm tựa từ **10. Tại sao ROLLUP(A,B) có N+1 level?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. ROLLUP với composite column** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **11. Thứ tự ROLLUP cực kỳ quan trọng ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11. Thứ tự ROLLUP cực kỳ quan trọng ⭐⭐⭐**. Bây giờ chuyển sang **12. ROLLUP với composite column**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **12. ROLLUP với composite column** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Group Functions**, **12. ROLLUP với composite column** tiếp nhận điểm tựa từ **11. Thứ tự ROLLUP cực kỳ quan trọng ⭐⭐⭐** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. GROUPING() ⭐⭐⭐** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **12. ROLLUP với composite column** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **12. ROLLUP với composite column**. Bây giờ chuyển sang **So sánh rất quan trọng**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **So sánh rất quan trọng** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### So sánh rất quan trọng

Khi gom phần **So sánh rất quan trọng** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **So sánh rất quan trọng**. Bây giờ chuyển sang **Không có ngoặc**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Không có ngoặc** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Không có ngoặc** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Không có ngoặc**. Bây giờ chuyển sang **Có composite column**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Có composite column** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Có composite column

Phần này nối mạch SQL với “Có composite column”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

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

Khi gom phần **Có composite column** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Có composite column**. Bây giờ chuyển sang **13. GROUPING() ⭐⭐⭐**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **13. GROUPING() ⭐⭐⭐** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Group Functions**, **13. GROUPING() ⭐⭐⭐** tiếp nhận điểm tựa từ **12. ROLLUP với composite column** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Dùng GROUPING thay NVL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **13. GROUPING() ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **13. GROUPING() ⭐⭐⭐**. Bây giờ chuyển sang **Quy tắc**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Quy tắc** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Quy tắc** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Quy tắc**. Bây giờ chuyển sang **14. Dùng GROUPING thay NVL**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14. Dùng GROUPING thay NVL** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Group Functions**, **14. Dùng GROUPING thay NVL** tiếp nhận điểm tựa từ **13. GROUPING() ⭐⭐⭐** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. CASE và DECODE đều dùng được** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **14. Dùng GROUPING thay NVL** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14. Dùng GROUPING thay NVL**. Bây giờ chuyển sang **15. CASE và DECODE đều dùng được**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **15. CASE và DECODE đều dùng được** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Group Functions**, **14. Dùng GROUPING thay NVL** cho ta quy tắc; **15. CASE và DECODE đều dùng được** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **16. CUBE ⭐⭐⭐** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. CASE và DECODE đều dùng được

Ảnh cho hai cách.

Khi gom phần **15. CASE và DECODE đều dùng được** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **15. CASE và DECODE đều dùng được**. Bây giờ chuyển sang **CASE**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**CASE** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

#### CASE

Phần này nối mạch SQL với “CASE”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
CASE
    WHEN GROUPING(DNAME) = 1
    THEN 'All Departments'
    ELSE DNAME
END
```

Khi gom phần **CASE** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **CASE**. Bây giờ chuyển sang **Oracle DECODE**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Oracle DECODE** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Oracle DECODE** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Oracle DECODE**. Bây giờ chuyển sang **16. CUBE ⭐⭐⭐**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **16. CUBE ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Group Functions**, **15. CASE và DECODE đều dùng được** cho ta quy tắc; **16. CUBE ⭐⭐⭐** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **17. ROLLUP vs CUBE** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **16. CUBE ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **16. CUBE ⭐⭐⭐**. Bây giờ chuyển sang **17. ROLLUP vs CUBE**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **17. ROLLUP vs CUBE** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Group Functions**, **17. ROLLUP vs CUBE** tiếp nhận điểm tựa từ **16. CUBE ⭐⭐⭐** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Thứ tự CUBE khác ROLLUP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. ROLLUP vs CUBE

Khi gom phần **17. ROLLUP vs CUBE** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **17. ROLLUP vs CUBE**. Bây giờ chuyển sang **ROLLUP**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**ROLLUP** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

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

Khi gom phần **ROLLUP** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **ROLLUP**. Bây giờ chuyển sang **CUBE**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**CUBE** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

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

Khi gom phần **CUBE** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **CUBE**. Bây giờ chuyển sang **Ví dụ từ ảnh**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Ví dụ từ ảnh** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Ví dụ từ ảnh** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Ví dụ từ ảnh**. Bây giờ chuyển sang **18. Thứ tự CUBE khác ROLLUP**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **18. Thứ tự CUBE khác ROLLUP** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Group Functions**, **18. Thứ tự CUBE khác ROLLUP** tiếp nhận điểm tựa từ **17. ROLLUP vs CUBE** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Tại sao CUBE nặng hơn ROLLUP?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **18. Thứ tự CUBE khác ROLLUP** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **18. Thứ tự CUBE khác ROLLUP**. Bây giờ chuyển sang **Nhớ**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Nhớ

Phần này nối mạch SQL với “Nhớ”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
ROLLUP → hierarchy → ORDER MATTERS
CUBE   → combinations → ORDER DOESN'T MATTER
```

Lưu ý: "order doesn't matter" ở đây nói về **các grouping set được sinh ra**, không có nghĩa SQL đảm bảo thứ tự hiển thị row. Muốn sort vẫn phải dùng `ORDER BY`.

---

Khi gom phần **Nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Nhớ**. Bây giờ chuyển sang **19. Tại sao CUBE nặng hơn ROLLUP?**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **19. Tại sao CUBE nặng hơn ROLLUP?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Group Functions**, **19. Tại sao CUBE nặng hơn ROLLUP?** tiếp nhận điểm tựa từ **18. Thứ tự CUBE khác ROLLUP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. GROUPING SETS ⭐⭐⭐** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Tại sao CUBE nặng hơn ROLLUP?

Với N column:

Khi gom phần **19. Tại sao CUBE nặng hơn ROLLUP?** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **19. Tại sao CUBE nặng hơn ROLLUP?**. Bây giờ chuyển sang **ROLLUP**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**ROLLUP** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

#### ROLLUP

Phần này nối mạch SQL với “ROLLUP”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
N + 1 grouping levels
```

Khi gom phần **ROLLUP** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **ROLLUP**. Bây giờ chuyển sang **CUBE**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**CUBE** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

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

Khi gom phần **CUBE** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **CUBE**. Bây giờ chuyển sang **20. GROUPING SETS ⭐⭐⭐**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **20. GROUPING SETS ⭐⭐⭐** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Group Functions**, **20. GROUPING SETS ⭐⭐⭐** tiếp nhận điểm tựa từ **19. Tại sao CUBE nặng hơn ROLLUP?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. GROUPING SETS không tự sinh Grand Total** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **20. GROUPING SETS ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **20. GROUPING SETS ⭐⭐⭐**. Bây giờ chuyển sang **Đây là chỗ rất dễ nhầm**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Đây là chỗ rất dễ nhầm** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Đây là chỗ rất dễ nhầm** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Đây là chỗ rất dễ nhầm**. Bây giờ chuyển sang **21. GROUPING SETS không tự sinh Grand Total**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **21. GROUPING SETS không tự sinh Grand Total** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Group Functions**, **21. GROUPING SETS không tự sinh Grand Total** tiếp nhận điểm tựa từ **20. GROUPING SETS ⭐⭐⭐** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. GROUPING SETS tương đương UNION ALL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **21. GROUPING SETS không tự sinh Grand Total** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **21. GROUPING SETS không tự sinh Grand Total**. Bây giờ chuyển sang **22. GROUPING SETS tương đương UNION ALL**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **22. GROUPING SETS tương đương UNION ALL** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Group Functions**, **22. GROUPING SETS tương đương UNION ALL** tiếp nhận điểm tựa từ **21. GROUPING SETS không tự sinh Grand Total** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. GROUPING SETS không phụ thuộc thứ tự** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **22. GROUPING SETS tương đương UNION ALL** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **22. GROUPING SETS tương đương UNION ALL**. Bây giờ chuyển sang **23. GROUPING SETS không phụ thuộc thứ tự**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **23. GROUPING SETS không phụ thuộc thứ tự** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Group Functions**, **23. GROUPING SETS không phụ thuộc thứ tự** tiếp nhận điểm tựa từ **22. GROUPING SETS tương đương UNION ALL** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Có thể biểu diễn ROLLUP bằng GROUPING SETS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **23. GROUPING SETS không phụ thuộc thứ tự** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **23. GROUPING SETS không phụ thuộc thứ tự**. Bây giờ chuyển sang **24. Có thể biểu diễn ROLLUP bằng GROUPING SETS**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **24. Có thể biểu diễn ROLLUP bằng GROUPING SETS** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Group Functions**, **24. Có thể biểu diễn ROLLUP bằng GROUPING SETS** tiếp nhận điểm tựa từ **23. GROUPING SETS không phụ thuộc thứ tự** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Biểu diễn CUBE bằng GROUPING SETS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **24. Có thể biểu diễn ROLLUP bằng GROUPING SETS** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **24. Có thể biểu diễn ROLLUP bằng GROUPING SETS**. Bây giờ chuyển sang **25. Biểu diễn CUBE bằng GROUPING SETS**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **25. Biểu diễn CUBE bằng GROUPING SETS** bằng câu hỏi: **ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Group Functions**, **25. Biểu diễn CUBE bằng GROUPING SETS** tiếp nhận điểm tựa từ **24. Có thể biểu diễn ROLLUP bằng GROUPING SETS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Bảng so sánh phải thuộc trước khi thi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **25. Biểu diễn CUBE bằng GROUPING SETS** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **25. Biểu diễn CUBE bằng GROUPING SETS**. Bây giờ chuyển sang **26. Bảng so sánh phải thuộc trước khi thi**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **26. Bảng so sánh phải thuộc trước khi thi** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Group Functions**, **25. Biểu diễn CUBE bằng GROUPING SETS** đã nêu tiêu chí phân biệt, còn **26. Bảng so sánh phải thuộc trước khi thi** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **27. Cách suy luận nhanh khi gặp đề SQLD** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **26. Bảng so sánh phải thuộc trước khi thi** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **26. Bảng so sánh phải thuộc trước khi thi**. Bây giờ chuyển sang **27. Cách suy luận nhanh khi gặp đề SQLD**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **27. Cách suy luận nhanh khi gặp đề SQLD** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Group Functions**, **26. Bảng so sánh phải thuộc trước khi thi** đã nêu tiêu chí phân biệt, còn **27. Cách suy luận nhanh khi gặp đề SQLD** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **28. Một bẫy đặc biệt: NULL trong kết quả** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **27. Cách suy luận nhanh khi gặp đề SQLD** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **27. Cách suy luận nhanh khi gặp đề SQLD**. Bây giờ chuyển sang **28. Một bẫy đặc biệt: NULL trong kết quả**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **28. Một bẫy đặc biệt: NULL trong kết quả** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Group Functions**, **27. Cách suy luận nhanh khi gặp đề SQLD** đã nêu tiêu chí phân biệt, còn **28. Một bẫy đặc biệt: NULL trong kết quả** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **29. Sơ đồ tổng hợp cực dễ nhớ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **28. Một bẫy đặc biệt: NULL trong kết quả** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **28. Một bẫy đặc biệt: NULL trong kết quả**. Bây giờ chuyển sang **29. Sơ đồ tổng hợp cực dễ nhớ**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **29. Sơ đồ tổng hợp cực dễ nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Group Functions**, **28. Một bẫy đặc biệt: NULL trong kết quả** đã nêu tiêu chí phân biệt, còn **29. Sơ đồ tổng hợp cực dễ nhớ** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **🔥 SQLD NOTE — 반드시 암기 / Bắt buộc nhớ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Sơ đồ tổng hợp cực dễ nhớ

Hãy lấy:

```text
A = Department
B = Job
```

Khi gom phần **29. Sơ đồ tổng hợp cực dễ nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **29. Sơ đồ tổng hợp cực dễ nhớ**. Bây giờ chuyển sang **GROUP BY**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**GROUP BY** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

#### GROUP BY

Phần này nối mạch SQL với “GROUP BY”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
GROUP BY A,B

A+B
```

Khi gom phần **GROUP BY** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **GROUP BY**. Bây giờ chuyển sang **ROLLUP**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**ROLLUP** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

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

Khi gom phần **ROLLUP** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **ROLLUP**. Bây giờ chuyển sang **CUBE**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**CUBE** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

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

Khi gom phần **CUBE** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **CUBE**. Bây giờ chuyển sang **GROUPING SETS**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

**GROUPING SETS** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. Hãy đọc các cột và hàng để trả lời: **bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao?**

#### GROUPING SETS

Phần này nối mạch SQL với “GROUPING SETS”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
GROUPING SETS(A,B)

A       B
```

Bạn **chỉ lấy đúng những group mình chỉ định**.

---

Khi gom phần **GROUPING SETS** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **GROUPING SETS**. Bây giờ chuyển sang **🔥 SQLD NOTE — 반드시 암기 / Bắt buộc nhớ**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **🔥 SQLD NOTE — 반드시 암기 / Bắt buộc nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Group Functions**, **🔥 SQLD NOTE — 반드시 암기 / Bắt buộc nhớ** gom các mảnh từ **29. Sơ đồ tổng hợp cực dễ nhớ** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

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

Khi gom phần **🔥 SQLD NOTE — 반드시 암기 / Bắt buộc nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **🔥 SQLD NOTE — 반드시 암기 / Bắt buộc nhớ**. Bây giờ chuyển sang **Công thức nhớ 10 giây trước khi vào thi**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Công thức nhớ 10 giây trước khi vào thi** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Công thức nhớ 10 giây trước khi vào thi** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Như vậy, **Công thức nhớ 10 giây trước khi vào thi** đã được đặt trong quan hệ giữa đầu vào, quy tắc xử lý và kết quả. Khi ôn lại, hãy tự diễn đạt ranh giới của nó rồi dùng ranh giới đó làm điểm nối sang bài tiếp theo.

> **Bàn giao:** Sau **🔥 SQLD NOTE — 반드시 암기 / Bắt buộc nhớ**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
