<!-- lecture-contract: v2 -->
# DDL và định nghĩa bảng

> **Mục tiêu:** Kiểu dữ liệu, CREATE/CTAS/ALTER/DROP/TRUNCATE.

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **DDL và định nghĩa bảng**. Route đi từ data types → CREATE/CTAS → ALTER/DROP/TRUNCATE → dependency/metadata → migration safety, để thay đổi schema nối với vòng đời dữ liệu.

Để học **DDL và định nghĩa bảng** như một mạch suy luận, trước hết hãy giữ câu hỏi: **cấu trúc hoặc ràng buộc nào đang bảo vệ dữ liệu, và thay đổi đó ảnh hưởng đến các câu lệnh sau ra sao?** Mục đích của bài là biến kiểu dữ liệu, create/ctas/alter/drop/truncate. thành cách đọc có thể áp dụng.

> **Mục tiêu:** Kiểu dữ liệu, CREATE/CTAS/ALTER/DROP/TRUNCATE.

Để học **DDL và định nghĩa bảng** như một mạch suy luận, trước hết hãy giữ câu hỏi: dữ liệu hoặc truy vấn đang giải quyết vấn đề gì, điều kiện nào làm thay đổi kết quả, và phần này nối với bài SQLD nào? Mục đích của bài là biến phần nguồn dưới đây thành cách đọc có thể áp dụng, không chỉ là danh sách cú pháp.

> **Nguồn bám sát:** PDF *2024 개정판 SQLD 개념정리*, trang 90–94.
>
> **Liên kết bài trước:** DML thay đổi các hàng; DDL định nghĩa hoặc thay đổi cấu trúc chứa các hàng đó. Vì thế DDL được xử lý auto-commit và không quay lui (rollback / 롤백) như DML chưa lần ghi nhận (commit / 커밋).

Ta bắt đầu với **1. DDL (Data Definition Language) (ngôn ngữ định nghĩa dữ liệu)**. Hãy xác định mục đích của khái niệm này trước, rồi mới đọc định nghĩa, ví dụ SQL hoặc bảng so sánh bên dưới.

Ta bắt đầu **1. DDL (Data Definition Language) (ngôn ngữ định nghĩa dữ liệu)** bằng câu hỏi: **cấu trúc hoặc ràng buộc nào đang bảo vệ dữ liệu, và thay đổi đó ảnh hưởng đến các câu lệnh sau ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 1. DDL (Data Definition Language) (ngôn ngữ định nghĩa dữ liệu)

Nội dung dưới **1. DDL (Data Definition Language) (ngôn ngữ định nghĩa dữ liệu)** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** DDL은 데이터의 구조를 정의하는 언어로 객체 생성, 삭제, 변경에 사용하며 AUTO lần ghi nhận (commit / 커밋)이라 quay lui (rollback / 롤백)이 불가하다.

DDL định nghĩa cấu trúc dữ liệu và các đối tượng (object / 객체) (Object) (đối tượng CSDL) như lược đồ (schema / 스키마) (Schema) (lược đồ), lĩnh vực (domain / 도메인) (Domain) (miền giá trị), bảng (table / 테이블) (Table) (bảng), view (View) (khung nhìn) và chỉ mục (index / 인덱스) (Index) (chỉ mục). Các lệnh chính là `CREATE` (Create) (tạo), `ALTER` (Alter) (thay đổi), `TRUNCATE` (Truncate) (xóa toàn bộ hàng, giữ cấu trúc) và `DROP` (Drop) (xóa đối tượng). Tuy `TRUNCATE` xóa dữ liệu, nó là DDL vì auto-commit.

Vừa rồi ta đã khép **1. DDL (Data Definition Language) (ngôn ngữ định nghĩa dữ liệu)** bằng đối tượng, điều kiện và kết quả cần theo dõi. Từ đó, ta chuyển sang **2. 데이터 유형 (Data type) (kiểu dữ liệu)** để xem phần mới dùng lại, mở rộng hay đối chiếu quy tắc nào.

Khi gom phần **1. DDL (Data Definition Language) (ngôn ngữ định nghĩa dữ liệu)** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1. DDL (Data Definition Language) (ngôn ngữ định nghĩa dữ liệu)**. Bây giờ chuyển sang **2. 데이터 유형 (Data type) (kiểu dữ liệu)**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2. 데이터 유형 (Data type) (kiểu dữ liệu)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 2. 데이터 유형 (Data type) (kiểu dữ liệu)

Nội dung dưới **2. 데이터 유형 (Data type) (kiểu dữ liệu)** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** CHAR은 고정 길이 문자형이고, VARCHAR2/VARCHAR는 가변 길이 문자형이다.

`CHAR(n)` (Character) (chuỗi độ dài cố định) chiếm đủ `n` ký tự; nếu giá trị ngắn hơn, phần còn thiếu được đệm khoảng trắng. `VARCHAR2(n)`/`VARCHAR(n)` (Variable Character) (chuỗi độ dài biến đổi) chỉ dùng dung lượng cần thiết, tối đa `n`. Điều này giải thích vì sao so sánh chuỗi của `CHAR` và `VARCHAR` có thể khác do khoảng trắng đệm.

> **KR:** NUMBER(p, s), NUMERIC(p, s)는 정수와 실수 등의 숫자 정보이고 DATE, DATETIME은 날짜와 시각 정보이다.

`NUMBER(p, s)`/`NUMERIC(p, s)` (Number/Numeric) (kiểu số) có `p` là tổng số chữ số và `s` là số chữ số phần thập phân: `NUMBER(6,2)` cho phép `1234.56` nhưng không `12345.67`. `DATE`/`DATETIME` (Date/Datetime) (ngày/giờ) lưu thông tin thời gian. Chọn kiểu dữ liệu đúng là nền tảng để ràng buộc (constraint / 제약조건) (Constraint) (ràng buộc) và so sánh/nhóm trong các bài SQL hoạt động đúng.

Vừa rồi ta đã khép **2. 데이터 유형 (Data type) (kiểu dữ liệu)** bằng đối tượng, điều kiện và kết quả cần theo dõi. Từ đó, ta chuyển sang **3. CREATE TABLE (Create Table) (tạo bảng)** để xem phần mới dùng lại, mở rộng hay đối chiếu quy tắc nào.

Khi gom phần **2. 데이터 유형 (Data type) (kiểu dữ liệu)** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2. 데이터 유형 (Data type) (kiểu dữ liệu)**. Bây giờ chuyển sang **3. CREATE TABLE (Create Table) (tạo bảng)**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3. CREATE TABLE (Create Table) (tạo bảng)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 3. CREATE TABLE (Create Table) (tạo bảng)

Nội dung dưới **3. CREATE TABLE (Create Table) (tạo bảng)** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

```sql
CREATE TABLE [owner.]table_name (
  column1 data_type [DEFAULT default_value] [constraint],
  column2 data_type [DEFAULT default_value] [constraint]
);
```

> **KR:** CREATE는 테이블, 인덱스 등의 객체를 생성하는 명령어이며 숫자 컬럼만 사이즈 생략이 가능하다.

`CREATE TABLE` tạo bảng với tên bảng, cột, kiểu dữ liệu, giá trị `DEFAULT` (Default) (mặc định) và ràng buộc (constraint / 제약조건) tùy chọn. Theo PDF, tên đơn vị sở hữu (owner / 오너) có thể bỏ qua khi tạo trong lược đồ (schema / 스키마) của tài khoản hiện tại; kiểu số có thể bỏ kích thước còn kiểu ngày không khai báo kích thước. Tên bảng/tên cột không phân biệt hoa thường nếu không dùng quy tắc đặc biệt; mặc định DB biểu diễn tên không trích dẫn bằng chữ hoa.

Vừa rồi ta đã khép **3. CREATE TABLE (Create Table) (tạo bảng)** bằng đối tượng, điều kiện và kết quả cần theo dõi. Từ đó, ta chuyển sang **Quy tắc đặt tên cần nhớ** để xem phần mới dùng lại, mở rộng hay đối chiếu quy tắc nào.

Khi gom phần **3. CREATE TABLE (Create Table) (tạo bảng)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3. CREATE TABLE (Create Table) (tạo bảng)**. Bây giờ chuyển sang **Quy tắc đặt tên cần nhớ**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Quy tắc đặt tên cần nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

##### Quy tắc đặt tên cần nhớ

Nội dung dưới **Quy tắc đặt tên cần nhớ** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** 테이블명은 적절한 단수형 이름을 사용하고, 테이블과 컬럼명은 반드시 문자로 시작하며 A-Z, a-z, 0-9, _, $, #만 허용된다.

Tên bảng nên có ý nghĩa, thường dùng dạng số ít; không trùng tên bảng khác, và tên cột không được trùng trong cùng bảng. Tên phải bắt đầu bằng chữ cái, không dùng reserved word (Reserved word) (từ khóa dành riêng), và chỉ dùng ký tự được PDF liệt kê: `A-Z`, `a-z`, `0-9`, `_`, `$`, `#`. Các cột được ngăn bằng dấu phẩy và câu lệnh kết thúc bằng `;`.

Vừa rồi ta đã khép **Quy tắc đặt tên cần nhớ** bằng đối tượng, điều kiện và kết quả cần theo dõi. Từ đó, ta chuyển sang **4. CTAS (Create Table As Select) (tạo bảng từ kết quả truy vấn)** để xem phần mới dùng lại, mở rộng hay đối chiếu quy tắc nào.

Khi gom phần **Quy tắc đặt tên cần nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Quy tắc đặt tên cần nhớ**. Bây giờ chuyển sang **4. CTAS (Create Table As Select) (tạo bảng từ kết quả truy vấn)**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4. CTAS (Create Table As Select) (tạo bảng từ kết quả truy vấn)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 4. CTAS (Create Table As Select) (tạo bảng từ kết quả truy vấn)

Nội dung dưới **4. CTAS (Create Table As Select) (tạo bảng từ kết quả truy vấn)** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** CTAS는 이미 만들어진 테이블을 활용해서 테이블을 재생성하며, 구조뿐 아니라 데이터도 복제할 수 있다.

```sql
-- Oracle
CREATE TABLE test AS
SELECT * FROM book;

-- SQL Server
SELECT * INTO test
FROM book;
```

CTAS sao chép cột, kiểu dữ liệu, dữ liệu và `NULL` thuộc tính (property / 속성) của kết quả `SELECT`; alias (Alias) (bí danh) trong SELECT trở thành tên cột mới. Có thể đổi tên cột trong `CREATE TABLE`. `WHERE 1 = 2` tạo cấu trúc mà không lấy hàng nào. Tuy nhiên, PDF nhấn mạnh PK, FK, UNIQUE, CHECK và các ràng buộc (constraint / 제약조건) khác không được sao chép; chỉ `NOT NULL` được kế thừa. Đây là lý do một bảng CTAS không tự động có đầy đủ tính toàn vẹn như bảng gốc.

```sql
CREATE TABLE test (book_id, book_name) AS
SELECT id, name
FROM book;

-- Chỉ sao chép cấu trúc
CREATE TABLE test AS
SELECT * FROM book WHERE 1 = 2;
```

Để xem cấu trúc: Oracle dùng `DESCRIBE employees` hoặc `DESC employees`; SQL máy chủ (server / 서버) dùng `exec sp_help 'dbo.employees'`.

Vừa rồi ta đã khép **4. CTAS (Create Table As Select) (tạo bảng từ kết quả truy vấn)** bằng đối tượng, điều kiện và kết quả cần theo dõi. Từ đó, ta chuyển sang **5. ALTER TABLE (Alter Table) (thay đổi cấu trúc bảng)** để xem phần mới dùng lại, mở rộng hay đối chiếu quy tắc nào.

Khi gom phần **4. CTAS (Create Table As Select) (tạo bảng từ kết quả truy vấn)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4. CTAS (Create Table As Select) (tạo bảng từ kết quả truy vấn)**. Bây giờ chuyển sang **5. ALTER TABLE (Alter Table) (thay đổi cấu trúc bảng)**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5. ALTER TABLE (Alter Table) (thay đổi cấu trúc bảng)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 5. ALTER TABLE (Alter Table) (thay đổi cấu trúc bảng)

Nội dung dưới **5. ALTER TABLE (Alter Table) (thay đổi cấu trúc bảng)** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** ALTER는 테이블의 구조 변경에 사용하며 컬럼 순서 변경은 불가능하다.

`ALTER TABLE` thêm, sửa, đổi tên hoặc xóa cột/ràng buộc. Cột mới luôn được thêm cuối bảng, không chỉ định vị trí. Đây là khác biệt quan trọng giữa thay đổi lược đồ (schema / 스키마) và thay đổi nội dung bảng: `ALTER` đổi definition (định nghĩa), không sửa từng hàng như `UPDATE`.

```sql
ALTER TABLE table_name ADD column_name data_type [DEFAULT value] [constraint];
ALTER TABLE table_name MODIFY column_name data_type;
ALTER TABLE table_name RENAME COLUMN old_name TO new_name;
ALTER TABLE table_name DROP COLUMN column_name;
ALTER TABLE table_name DROP CONSTRAINT constraint_name;
ALTER TABLE table_name ADD CONSTRAINT constraint_name constraint_definition;
```

Vừa rồi ta đã khép **5. ALTER TABLE (Alter Table) (thay đổi cấu trúc bảng)** bằng đối tượng, điều kiện và kết quả cần theo dõi. Từ đó, ta chuyển sang **Thêm/sửa cột** để xem phần mới dùng lại, mở rộng hay đối chiếu quy tắc nào.

Khi gom phần **5. ALTER TABLE (Alter Table) (thay đổi cấu trúc bảng)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5. ALTER TABLE (Alter Table) (thay đổi cấu trúc bảng)**. Bây giờ chuyển sang **Thêm/sửa cột**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Thêm/sửa cột** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

##### Thêm/sửa cột

Nội dung dưới **Thêm/sửa cột** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** 여러 컬럼 동시 추가는 가능하지만 반드시 괄호를 사용한다.

Oracle cho phép thêm nhiều cột bằng ngoặc; cột thêm mới có thể có `DEFAULT` và ràng buộc (constraint / 제약조건). Nếu bảng đã có dữ liệu, thêm cột `NOT NULL` không có default là không thể vì các hàng cũ sẽ nhận `NULL`; thêm default hợp lệ thì có thể. Oracle có thể `MODIFY` nhiều cột; theo PDF SQL máy chủ (server / 서버) sửa một cột cho mỗi lệnh `ALTER COLUMN`.

```sql
ALTER TABLE player ADD (birthday DATE, address VARCHAR2(80));
ALTER TABLE player ADD stadium VARCHAR2(25)
  DEFAULT '전주월드컵경기장' NOT NULL;
```

Vừa rồi ta đã khép **Thêm/sửa cột** bằng đối tượng, điều kiện và kết quả cần theo dõi. Từ đó, ta chuyển sang **Các bẫy khi thay đổi thuộc tính** để xem phần mới dùng lại, mở rộng hay đối chiếu quy tắc nào.

Khi gom phần **Thêm/sửa cột** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Thêm/sửa cột**. Bây giờ chuyển sang **Các bẫy khi thay đổi thuộc tính**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Các bẫy khi thay đổi thuộc tính** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

##### Các bẫy khi thay đổi thuộc tính

Nội dung dưới **Các bẫy khi thay đổi thuộc tính** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** 컬럼 사이즈 증가는 항상 가능하고, 축소는 데이터 존재 여부에 따라 제한된다.

Tăng kích thước cột luôn được phép; giảm kích thước chỉ được khi dữ liệu hiện có vẫn phù hợp. Đổi kiểu dữ liệu thường chỉ an toàn khi cột rỗng hoặc mọi giá trị là `NULL`; PDF lưu ý `CHAR` và `VARCHAR` có thể đổi qua lại dù đã có dữ liệu. Đổi `DEFAULT` chỉ ảnh hưởng những hàng được chèn sau khi đổi, không sửa dữ liệu đã tồn tại; gán `NULL` là lưu NULL chứ không tự thay bằng default.

Vừa rồi ta đã khép **Các bẫy khi thay đổi thuộc tính** bằng đối tượng, điều kiện và kết quả cần theo dõi. Từ đó, ta chuyển sang **Đổi tên và xóa** để xem phần mới dùng lại, mở rộng hay đối chiếu quy tắc nào.

Khi gom phần **Các bẫy khi thay đổi thuộc tính** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Các bẫy khi thay đổi thuộc tính**. Bây giờ chuyển sang **Đổi tên và xóa**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Đổi tên và xóa** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

##### Đổi tên và xóa

Nội dung dưới **Đổi tên và xóa** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** 컬럼 이름 변경은 항상 가능하지만 동시에 여러 컬럼 이름 변경은 불가능하다.

Oracle dùng `RENAME COLUMN`, SQL máy chủ (server / 서버) dùng `sp_rename`; đổi tên bảng cũng có cú pháp riêng. Xóa cột chỉ xóa một cột một lần, không phụ thuộc dữ liệu có hay không và không khôi phục được; bảng phải còn ít nhất một cột.

```sql
ALTER TABLE emp RENAME COLUMN ename TO first_name;
RENAME season1 TO season2;
ALTER TABLE player DROP COLUMN address;
```

Vừa rồi ta đã khép **Đổi tên và xóa** bằng đối tượng, điều kiện và kết quả cần theo dõi. Từ đó, ta chuyển sang **6. DROP và TRUNCATE** để xem phần mới dùng lại, mở rộng hay đối chiếu quy tắc nào.

Khi gom phần **Đổi tên và xóa** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Đổi tên và xóa**. Bây giờ chuyển sang **6. DROP và TRUNCATE**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6. DROP và TRUNCATE** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 6. DROP và TRUNCATE

Nội dung dưới **6. DROP và TRUNCATE** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** DROP bảng (table / 테이블)은 테이블의 모든 데이터 및 구조를 삭제하고, TRUNCATE는 테이블 구조를 남기고 전체 데이터를 삭제한다.

`DROP TABLE` xóa cả cấu trúc lẫn dữ liệu; nếu có FK tham chiếu thì Oracle có thể cần `CASCADE CONSTRAINT`, còn PDF lưu ý SQL máy chủ (server / 서버) phải xóa FK/bảng tham chiếu trước. `TRUNCATE TABLE` xóa toàn bộ hàng, giữ cấu trúc và có thể kiểm tra lại bằng `DESC`; vì là DDL nên không quay lui (rollback / 롤백). Ngược lại, `DELETE` là DML, có thể xóa một phần/toàn bộ hàng và quay lui (rollback / 롤백) trước lần ghi nhận (commit / 커밋).

| Lệnh | Phân loại | Phạm vi | quay lui (rollback / 롤백) |
| --- | --- | --- | --- |
| `DELETE` | DML | Một hoặc toàn bộ hàng | Có trước lần ghi nhận (commit / 커밋) |
| `DROP` | DDL | Dữ liệu và cấu trúc bảng | Không (auto-commit) |
| `TRUNCATE` | DDL | Toàn bộ hàng, giữ cấu trúc | Không (auto-commit) |

Như vậy, **6. DROP và TRUNCATE** cần được nhớ bằng quan hệ giữa dữ liệu đầu vào, quy tắc xử lý và kết quả đầu ra. Khi ôn lại, hãy tự diễn đạt quan hệ đó rồi dùng nó làm điểm tựa cho section kế tiếp.

Khi gom phần **6. DROP và TRUNCATE** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Như vậy, **6. DROP và TRUNCATE** đã được đặt trong quan hệ giữa đầu vào, quy tắc xử lý và kết quả. Khi ôn lại, hãy tự diễn đạt ranh giới của nó rồi dùng ranh giới đó làm điểm nối sang bài tiếp theo.
