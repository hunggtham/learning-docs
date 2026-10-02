<!-- lecture-contract: v2 -->
# PIVOT, UNPIVOT và Regular Expression

> **Mục tiêu:** Chuyển đổi cấu trúc dữ liệu và regex Oracle.

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **PIVOT, UNPIVOT và regular expression**. Route đi từ row/column shape → PIVOT/UNPIVOT transformation → pattern matching → NULL/aggregation behavior → portable query limits, để biến đổi vẫn giữ nghĩa dữ liệu.

Để học **PIVOT, UNPIVOT và Regular Expression** như một mạch suy luận, trước hết hãy giữ câu hỏi: **dữ liệu được biến đổi hình dạng hoặc nhận diện theo mẫu nào, và kết quả mới còn giữ quan hệ gì với dữ liệu đầu vào?** Mục đích của bài là biến chuyển đổi cấu trúc dữ liệu và regex oracle. thành cách đọc có thể áp dụng.

> **Mục tiêu:** Chuyển đổi cấu trúc dữ liệu và regex Oracle.

Để học **PIVOT, UNPIVOT và Regular Expression** như một mạch suy luận, trước hết hãy giữ câu hỏi: dữ liệu hoặc truy vấn đang giải quyết vấn đề gì, điều kiện nào làm thay đổi kết quả, và phần này nối với bài SQLD nào? Mục đích của bài là biến phần nguồn dưới đây thành cách đọc có thể áp dụng, không chỉ là danh sách cú pháp.

> **Nguồn bám sát:** PDF *2024 개정판 SQLD 개념정리*, trang 81–84.
>
> **Liên kết bài trước:** Đây là bước biến đổi hình dạng kết quả sau khi đã biết `SELECT`, `GROUP BY` và `JOIN`; nó không thay thế mô hình dữ liệu chuẩn hóa.

Ta bắt đầu với **1. Long Data và Wide Data**. Hãy xác định mục đích của khái niệm này trước, rồi mới đọc định nghĩa, ví dụ SQL hoặc bảng so sánh bên dưới.

Ta bắt đầu **1. Long Data và Wide Data** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 1. Long Data và Wide Data

Nội dung dưới **1. Long Data và Wide Data** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** Long dữ liệu (data / 데이터)는 하나의 속성값이 여러 행으로 쌓이는 구조이고, Wide dữ liệu (data / 데이터)는 하나의 속성값이 여러 컬럼으로 분리되어 표현되는 구조이다.

Long dữ liệu (data / 데이터)/Tidy dữ liệu (data / 데이터) lưu mỗi quan sát thành một hàng, dễ phép nối (join / 조인) và phù hợp thiết kế RDBMS. Wide dữ liệu (data / 데이터)/Cross bảng (table / 테이블) dàn giá trị của một thuộc tính thành nhiều cột, tiện cho báo cáo nhưng khó mở rộng khi số cột tăng. `PIVOT` chuyển long → wide; `UNPIVOT` chuyển wide → long.

Vừa rồi ta đã khép **1. Long Data và Wide Data** bằng đối tượng, điều kiện và kết quả cần theo dõi. Từ đó, ta chuyển sang **2. PIVOT (Pivot) (xoay hàng thành cột)** để xem phần mới dùng lại, mở rộng hay đối chiếu quy tắc nào.

Khi gom phần **1. Long Data và Wide Data** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1. Long Data và Wide Data**. Bây giờ chuyển sang **2. PIVOT (Pivot) (xoay hàng thành cột)**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2. PIVOT (Pivot) (xoay hàng thành cột)** bằng câu hỏi: **dữ liệu được biến đổi hình dạng hoặc nhận diện theo mẫu nào, và kết quả mới còn giữ quan hệ gì với dữ liệu đầu vào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 2. PIVOT (Pivot) (xoay hàng thành cột)

Nội dung dưới **2. PIVOT (Pivot) (xoay hàng thành cột)** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** PIVOT은 Long dữ liệu (data / 데이터)를 Wide dữ liệu (data / 데이터)로 바꾸어 행 데이터를 열 데이터로 변환한다.

`PIVOT` tổng hợp theo một phép aggregate và đưa các giá trị chỉ định thành tên cột. Hãy chuẩn bị nguồn dữ liệu đúng mức chi tiết bằng subquery/phép nối (join / 조인) trước, vì các cột không nằm trong `FOR ... IN` trở thành khóa nhóm ngầm.

```sql
SELECT *
FROM (
  SELECT e.job, d.dname
  FROM emp e JOIN dept d ON e.deptno = d.deptno
)
PIVOT (
  COUNT(*) FOR dname IN (
    'ACCOUNTING' AS accounting,
    'RESEARCH' AS research,
    'SALES' AS sales
  )
);
```

Vừa rồi ta đã khép **2. PIVOT (Pivot) (xoay hàng thành cột)** bằng đối tượng, điều kiện và kết quả cần theo dõi. Từ đó, ta chuyển sang **3. UNPIVOT (Unpivot) (xoay cột thành hàng)** để xem phần mới dùng lại, mở rộng hay đối chiếu quy tắc nào.

Khi gom phần **2. PIVOT (Pivot) (xoay hàng thành cột)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2. PIVOT (Pivot) (xoay hàng thành cột)**. Bây giờ chuyển sang **3. UNPIVOT (Unpivot) (xoay cột thành hàng)**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3. UNPIVOT (Unpivot) (xoay cột thành hàng)** bằng câu hỏi: **dữ liệu được biến đổi hình dạng hoặc nhận diện theo mẫu nào, và kết quả mới còn giữ quan hệ gì với dữ liệu đầu vào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 3. UNPIVOT (Unpivot) (xoay cột thành hàng)

Nội dung dưới **3. UNPIVOT (Unpivot) (xoay cột thành hàng)** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** UNPIVOT은 Wide dữ liệu (data / 데이터)를 Long dữ liệu (data / 데이터)로 바꾸어 열 데이터를 행 데이터로 변환한다.

`UNPIVOT` đưa nhiều cột báo cáo trở lại hai cột: một cột nhãn và một cột giá trị. Đây là cách đưa bảng chéo về dạng dễ filter/phép nối (join / 조인)/aggregate hơn.

```sql
SELECT job, department, emp_count
FROM pivot_table
UNPIVOT (
  emp_count FOR department IN (
    accounting AS 'ACCOUNTING',
    research AS 'RESEARCH',
    sales AS 'SALES'
  )
);
```

Vừa rồi ta đã khép **3. UNPIVOT (Unpivot) (xoay cột thành hàng)** bằng đối tượng, điều kiện và kết quả cần theo dõi. Từ đó, ta chuyển sang **4. 정규 표현식 (Regular Expression) (biểu thức chính quy)** để xem phần mới dùng lại, mở rộng hay đối chiếu quy tắc nào.

Khi gom phần **3. UNPIVOT (Unpivot) (xoay cột thành hàng)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3. UNPIVOT (Unpivot) (xoay cột thành hàng)**. Bây giờ chuyển sang **4. 정규 표현식 (Regular Expression) (biểu thức chính quy)**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4. 정규 표현식 (Regular Expression) (biểu thức chính quy)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 4. 정규 표현식 (Regular Expression) (biểu thức chính quy)

Nội dung dưới **4. 정규 표현식 (Regular Expression) (biểu thức chính quy)** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** 정규 표현식은 문자열의 공통된 규칙을 일반화하여 특정 패턴을 검색, 매칭 또는 수정하는 강력한 도구이다.

Regex mô tả mẫu văn bản: `.` là một ký tự (trừ newline), `|` là hoặc, `\` escape (thoát nghĩa đặc biệt); `^` là đầu chuỗi, `$` là cuối chuỗi. Quantifier (bộ định lượng) gồm `?` (0/1), `*` (0+), `+` (1+), `{m}` (đúng m), `{m,}` (ít nhất m), `{,m}` (tối đa m), `{m,n}` (m đến n). Character lớp (class / 클래스) gồm `[char...]`, `[^char...]`, `[[:digit:]]`, `[[:lower:]]`, `[[:upper:]]`, `[[:alpha:]]`, `[[:alnum:]]`, `[[:space:]]`; dạng rút gọn có `\d`, `\w`, `\s` và dạng phủ định `\D`, `\W`, `\S`.

Vừa rồi ta đã khép **4. 정규 표현식 (Regular Expression) (biểu thức chính quy)** bằng đối tượng, điều kiện và kết quả cần theo dõi. Từ đó, ta chuyển sang **5. Oracle REGEXP functions** để xem phần mới dùng lại, mở rộng hay đối chiếu quy tắc nào.

Khi gom phần **4. 정규 표현식 (Regular Expression) (biểu thức chính quy)** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4. 정규 표현식 (Regular Expression) (biểu thức chính quy)**. Bây giờ chuyển sang **5. Oracle REGEXP functions**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5. Oracle REGEXP functions** bằng câu hỏi: **dữ liệu được biến đổi hình dạng hoặc nhận diện theo mẫu nào, và kết quả mới còn giữ quan hệ gì với dữ liệu đầu vào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 5. Oracle REGEXP functions

Nội dung dưới **5. Oracle REGEXP functions** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** REGEXP_LIKE는 패턴 일치 여부를 반환하고, REGEXP_REPLACE는 일치한 패턴을 바꾸며, REGEXP_SUBSTR은 일치한 문자열을 반환한다.

`REGEXP_LIKE(source_char, pattern [, match_param])` lọc/kiểm tra khớp; `REGEXP_REPLACE` thay phần khớp; `REGEXP_SUBSTR` lấy phần khớp; `REGEXP_INSTR` trả vị trí; `REGEXP_COUNT` đếm số lần khớp. Các tham số chung: `source_char` (chuỗi nguồn), `pattern` (mẫu), `position` (vị trí bắt đầu, mặc định 1), `occurrence` (lần khớp, mặc định 1), `match_param` (tùy chọn khớp), `subexpr` (nhóm con). `match_param` PDF nêu `i` bỏ phân biệt hoa/thường, `c` phân biệt, `n` cho `.` khớp newline, `m` ảnh hưởng anchor đa dòng, `x` bỏ qua khoảng trắng trong mẫu (pattern / 패턴).

```sql
-- Chỉ nhận mã gồm đúng 3 chữ số
WHERE REGEXP_LIKE(code, '^[[:digit:]]{3}$')

-- Thay mọi dãy khoảng trắng bằng một khoảng trắng
SELECT REGEXP_REPLACE(name, '[[:space:]]+', ' ') FROM person;
```

Như vậy, **5. Oracle REGEXP functions** cần được nhớ bằng quan hệ giữa dữ liệu đầu vào, quy tắc xử lý và kết quả đầu ra. Khi ôn lại, hãy tự diễn đạt quan hệ đó rồi dùng nó làm điểm tựa cho section kế tiếp.

Khi gom phần **5. Oracle REGEXP functions** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Như vậy, **5. Oracle REGEXP functions** đã được đặt trong quan hệ giữa đầu vào, quy tắc xử lý và kết quả. Khi ôn lại, hãy tự diễn đạt ranh giới của nó rồi dùng ranh giới đó làm điểm nối sang bài tiếp theo.
