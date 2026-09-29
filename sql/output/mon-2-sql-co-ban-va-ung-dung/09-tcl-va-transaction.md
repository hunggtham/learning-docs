<!-- lecture-contract: v2 -->
# TCL và Transaction

> **Mục tiêu:** ACID, COMMIT, ROLLBACK, SAVEPOINT và khác biệt Oracle/SQL Server.

Để học **TCL và Transaction** như một mạch suy luận, trước hết hãy giữ câu hỏi: **thay đổi nào tác động lên hàng dữ liệu, phạm vi nào bị ảnh hưởng và khi nào thay đổi được xác nhận?** Mục đích của bài là biến acid, commit, rollback, savepoint và khác biệt oracle/sql server. thành cách đọc có thể áp dụng.

> **Mục tiêu:** ACID, COMMIT, ROLLBACK, SAVEPOINT và khác biệt Oracle/SQL Server.

Để học **TCL và Transaction** như một mạch suy luận, trước hết hãy giữ câu hỏi: dữ liệu hoặc truy vấn đang giải quyết vấn đề gì, điều kiện nào làm thay đổi kết quả, và phần này nối với bài SQLD nào? Mục đích của bài là biến phần nguồn dưới đây thành cách đọc có thể áp dụng, không chỉ là danh sách cú pháp.

> **Nguồn bám sát:** PDF *2024 개정판 SQLD 개념정리*, trang 87–89.
>
> **Liên kết bài trước:** DML thay đổi dữ liệu; TCL quyết định khi nào các thay đổi đó trở thành dữ liệu chính thức hoặc bị hủy.

Ta bắt đầu với **1. TCL (Transaction Control Language) (ngôn ngữ điều khiển giao dịch)**. Hãy xác định mục đích của khái niệm này trước, rồi mới đọc định nghĩa, ví dụ SQL hoặc bảng so sánh bên dưới.

Ta bắt đầu **1. TCL (Transaction Control Language) (ngôn ngữ điều khiển giao dịch)** bằng câu hỏi: **thay đổi nào tác động lên hàng dữ liệu, phạm vi nào bị ảnh hưởng và khi nào thay đổi được xác nhận?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 1. TCL (Transaction Control Language) (ngôn ngữ điều khiển giao dịch)

Nội dung dưới **1. TCL (Transaction Control Language) (ngôn ngữ điều khiển giao dịch)** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** TCL은 COMMIT, ROLLBACK, SAVEPOINT를 포함하며 DML에 의해 조작된 결과를 작업단위(트랜잭션)별로 제어한다.

TCL gồm `COMMIT` (Commit) (xác nhận lưu), `ROLLBACK` (Rollback) (hoàn tác) và `SAVEPOINT` (Savepoint) (điểm lưu tạm). Nó không trực tiếp thêm/sửa/xóa hàng, mà kiểm soát các thay đổi do DML tạo ra theo đơn vị transaction (Transaction) (giao dịch).

Vừa rồi ta đã khép **1. TCL (Transaction Control Language) (ngôn ngữ điều khiển giao dịch)** bằng đối tượng, điều kiện và kết quả cần theo dõi. Từ đó, ta chuyển sang **2. 트랜잭션 (Transaction) (giao dịch)** để xem phần mới dùng lại, mở rộng hay đối chiếu quy tắc nào.

Khi gom phần **1. TCL (Transaction Control Language) (ngôn ngữ điều khiển giao dịch)** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1. TCL (Transaction Control Language) (ngôn ngữ điều khiển giao dịch)**. Bây giờ chuyển sang **2. 트랜잭션 (Transaction) (giao dịch)**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2. 트랜잭션 (Transaction) (giao dịch)** bằng câu hỏi: **thay đổi nào tác động lên hàng dữ liệu, phạm vi nào bị ảnh hưởng và khi nào thay đổi được xác nhận?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 2. 트랜잭션 (Transaction) (giao dịch)

Nội dung dưới **2. 트랜잭션 (Transaction) (giao dịch)** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** 트랜잭션은 데이터베이스의 논리적 연산단위이며 분할할 수 없는 최소의 단위이다.

Transaction là một đơn vị công việc logic, không thể tách nhỏ khi xét tính đúng đắn. Ví dụ chuyển tiền cần cả việc trừ ở tài khoản A lẫn cộng ở tài khoản B thành công; nếu một bước thất bại, cả hai phải trở về trạng thái cũ. Đây là nguyên tắc `ALL OR NOTHING` (all-or-nothing) (tất cả hoặc không gì cả).

Vừa rồi ta đã khép **2. 트랜잭션 (Transaction) (giao dịch)** bằng đối tượng, điều kiện và kết quả cần theo dõi. Từ đó, ta chuyển sang **3. 트랜잭션의 특징 (ACID) (đặc tính giao dịch)** để xem phần mới dùng lại, mở rộng hay đối chiếu quy tắc nào.

Khi gom phần **2. 트랜잭션 (Transaction) (giao dịch)** lại, ta không cần nhớ các dòng như những mảnh rời: ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2. 트랜잭션 (Transaction) (giao dịch)**. Bây giờ chuyển sang **3. 트랜잭션의 특징 (ACID) (đặc tính giao dịch)**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3. 트랜잭션의 특징 (ACID) (đặc tính giao dịch)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 3. 트랜잭션의 특징 (ACID) (đặc tính giao dịch)

Nội dung dưới **3. 트랜잭션의 특징 (ACID) (đặc tính giao dịch)** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

| 한국어 (English) (Tiếng Việt) | Giải thích |
| --- | --- |
| 원자성 (Atomicity) (tính nguyên tử) | Toàn bộ thao tác trong transaction đều thành công hoặc không thao tác nào được áp dụng. |
| 일관성 (Consistency) (tính nhất quán) | Nếu DB hợp lệ trước transaction thì sau transaction cũng phải hợp lệ; không được phá vỡ ràng buộc và quy tắc dữ liệu. |
| 고립성 (Isolation) (tính cô lập) | Transaction đang chạy không được chịu ảnh hưởng làm tạo ra kết quả sai do transaction khác. |
| 지속성 (Durability) (tính bền vững) | Khi transaction đã thành công, dữ liệu đã cập nhật được lưu bền vững. |

Vừa rồi ta đã khép **3. 트랜잭션의 특징 (ACID) (đặc tính giao dịch)** bằng đối tượng, điều kiện và kết quả cần theo dõi. Từ đó, ta chuyển sang **4. COMMIT (Commit) (xác nhận lưu)** để xem phần mới dùng lại, mở rộng hay đối chiếu quy tắc nào.

Khi gom phần **3. 트랜잭션의 특징 (ACID) (đặc tính giao dịch)** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3. 트랜잭션의 특징 (ACID) (đặc tính giao dịch)**. Bây giờ chuyển sang **4. COMMIT (Commit) (xác nhận lưu)**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4. COMMIT (Commit) (xác nhận lưu)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 4. COMMIT (Commit) (xác nhận lưu)

Nội dung dưới **4. COMMIT (Commit) (xác nhận lưu)** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** COMMIT은 올바르게 반영된 데이터를 데이터베이스에 반영시키는 명령어이며, COMMIT 이전에 수행된 DML은 모두 저장되어 되돌릴 수 없다.

`COMMIT` kết thúc transaction hiện tại và làm các DML trước đó trở thành bền vững. Sau `COMMIT`, không thể dùng `ROLLBACK` để quay lại những thay đổi đó. Vì vậy, trước khi commit một `UPDATE` hoặc `DELETE` diện rộng, cần kiểm tra điều kiện `WHERE` và số hàng chịu ảnh hưởng.

Vừa rồi ta đã khép **4. COMMIT (Commit) (xác nhận lưu)** bằng đối tượng, điều kiện và kết quả cần theo dõi. Từ đó, ta chuyển sang **5. Oracle và SQL Server: transaction/auto-commit** để xem phần mới dùng lại, mở rộng hay đối chiếu quy tắc nào.

Khi gom phần **4. COMMIT (Commit) (xác nhận lưu)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4. COMMIT (Commit) (xác nhận lưu)**. Bây giờ chuyển sang **5. Oracle và SQL Server: transaction/auto-commit**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5. Oracle và SQL Server: transaction/auto-commit** bằng câu hỏi: **thay đổi nào tác động lên hàng dữ liệu, phạm vi nào bị ảnh hưởng và khi nào thay đổi được xác nhận?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 5. Oracle và SQL Server: transaction/auto-commit

Nội dung dưới **5. Oracle và SQL Server: transaction/auto-commit** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** ORACLE은 DML 시 사용자가 COMMIT 또는 ROLLBACK을 수행해야 하며, SQL Server는 기본적으로 AUTO COMMIT 모드이다.

Theo nội dung PDF, Oracle cần người dùng `COMMIT`/`ROLLBACK` để kết thúc transaction DML. SQL Server mặc định auto-commit (tự xác nhận từng lệnh); nếu muốn kiểm soát nhiều lệnh thành một transaction, phải mở transaction rõ ràng. PDF cũng lưu ý DDL của Oracle auto-commit (từ Oracle 23c có thể cấu hình khác) và SQL Server có thể cấu hình auto-commit.

Vừa rồi ta đã khép **5. Oracle và SQL Server: transaction/auto-commit** bằng đối tượng, điều kiện và kết quả cần theo dõi. Từ đó, ta chuyển sang **6. ROLLBACK (Rollback) (hoàn tác)** để xem phần mới dùng lại, mở rộng hay đối chiếu quy tắc nào.

Khi gom phần **5. Oracle và SQL Server: transaction/auto-commit** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5. Oracle và SQL Server: transaction/auto-commit**. Bây giờ chuyển sang **6. ROLLBACK (Rollback) (hoàn tác)**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6. ROLLBACK (Rollback) (hoàn tác)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 6. ROLLBACK (Rollback) (hoàn tác)

Nội dung dưới **6. ROLLBACK (Rollback) (hoàn tác)** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** ROLLBACK은 테이블 내 입력, 수정, 삭제 데이터의 변경을 취소하고 최종 COMMIT 지점, 변경 전 또는 특정 SAVEPOINT 지점으로 원복한다.

`ROLLBACK` hủy các thay đổi DML chưa commit. Có thể quay về lần `COMMIT` cuối cùng hoặc về một `SAVEPOINT` được đặt sau lần commit đó. Vì DDL và `TRUNCATE` là auto-commit theo nội dung PDF, chúng không được hoàn tác bằng rollback thông thường.

```sql
-- Oracle
UPDATE player SET price = 2800
WHERE drink = '아메리카노';
ROLLBACK;

-- SQL Server: cần transaction rõ ràng khi không dùng auto-commit
BEGIN TRANSACTION;
UPDATE player SET price = 2800
WHERE drink = '아메리카노';
ROLLBACK;
```

Vừa rồi ta đã khép **6. ROLLBACK (Rollback) (hoàn tác)** bằng đối tượng, điều kiện và kết quả cần theo dõi. Từ đó, ta chuyển sang **7. SAVEPOINT (Savepoint) (điểm lưu tạm)** để xem phần mới dùng lại, mở rộng hay đối chiếu quy tắc nào.

Khi gom phần **6. ROLLBACK (Rollback) (hoàn tác)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6. ROLLBACK (Rollback) (hoàn tác)**. Bây giờ chuyển sang **7. SAVEPOINT (Savepoint) (điểm lưu tạm)**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7. SAVEPOINT (Savepoint) (điểm lưu tạm)** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### 7. SAVEPOINT (Savepoint) (điểm lưu tạm)

Nội dung dưới **7. SAVEPOINT (Savepoint) (điểm lưu tạm)** cung cấp phần giải thích và bằng chứng cho mục đích vừa nêu; khi đọc SQL, hãy theo dõi đối tượng, điều kiện lọc, thứ tự xử lý và kết quả thay đổi như thế nào.

> **KR:** SAVEPOINT는 트랜잭션 전체가 아니라 현 시점에서 SAVEPOINT까지 트랜잭션의 일부만 롤백할 수 있게 한다.

`SAVEPOINT` đánh dấu một vị trí trong transaction để có thể hoàn tác một phần sau đó. Có thể tạo nhiều savepoint; nếu đặt lại cùng tên, savepoint mới nhất mang tên đó có hiệu lực. Không thể rollback vượt qua `COMMIT`.

```sql
-- Oracle
SAVEPOINT a;
ROLLBACK TO a;

-- SQL Server
SAVE TRANSACTION a;
ROLLBACK TRANSACTION a;
```

Với chuỗi `INSERT` → `SAVEPOINT SVPT_A` → `UPDATE` → `SAVEPOINT SVPT_B` → `DELETE`: `ROLLBACK TO SVPT_B` chỉ hủy DELETE; `ROLLBACK TO SVPT_A` hủy UPDATE và DELETE; `ROLLBACK` hủy cả INSERT chưa commit. Cách suy luận này nối trực tiếp với nguyên tắc atomicity (Atomicity) (tính nguyên tử): savepoint chia đường quay lui trong một transaction, không chia nhỏ tính đúng đắn của transaction đã commit.

Như vậy, **7. SAVEPOINT (Savepoint) (điểm lưu tạm)** cần được nhớ bằng quan hệ giữa dữ liệu đầu vào, quy tắc xử lý và kết quả đầu ra. Khi ôn lại, hãy tự diễn đạt quan hệ đó rồi dùng nó làm điểm tựa cho section kế tiếp.

Khi gom phần **7. SAVEPOINT (Savepoint) (điểm lưu tạm)** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Như vậy, **7. SAVEPOINT (Savepoint) (điểm lưu tạm)** đã được đặt trong quan hệ giữa đầu vào, quy tắc xử lý và kết quả. Khi ôn lại, hãy tự diễn đạt ranh giới của nó rồi dùng ranh giới đó làm điểm nối sang bài tiếp theo.
