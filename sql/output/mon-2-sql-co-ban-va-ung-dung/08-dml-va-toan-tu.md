<!-- lecture-contract: v2 -->
# DML và toán tử

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **DML và toán tử**. Route đi từ business mutation → INSERT/UPDATE/DELETE → predicates/operators → affected-row validation → transaction/rollback, để lệnh sửa dữ liệu nối với điều kiện an toàn.

> **Mục tiêu:** Hiểu cách thêm, sửa, xóa, đồng bộ và truy vấn dữ liệu; đồng thời biết toán tử làm thay đổi biểu thức như thế nào.

## Bắt đầu từ câu hỏi nghiệp vụ

Ở các bài trước, ta chủ yếu dùng `SELECT` để đọc dữ liệu đã có. Nhưng một hệ thống thật không chỉ đọc: người dùng đăng ký, thay đổi thông tin, hủy đơn hàng, và dữ liệu từ hệ thống khác cũng phải được đồng bộ. Vì vậy, bài này trả lời câu hỏi: **khi dữ liệu cần thay đổi, ta chọn lệnh nào, phạm vi thay đổi được xác định ra sao, và kết quả đó còn có thể hoàn tác hay không?**

Ta sẽ đi từ nhóm lệnh DML, lần lượt qua `INSERT`, `UPDATE`, `DELETE`, `MERGE`, rồi quay lại `SELECT` và các toán tử. Trình tự này có chủ ý: trước hết hiểu cách tác động lên hàng dữ liệu, sau đó học cách kiểm tra và tạo biểu thức từ chính dữ liệu đó. Phần kiểm soát việc lưu hay hoàn tác sẽ được bàn giao cho bài **TCL và Transaction**.

> **Nguồn bám sát:** PDF *2024 개정판 SQLD 개념정리*, trang 85–86.

> **Chuyển mạch:** Trong **DML và toán tử**, **Bắt đầu từ câu hỏi nghiệp vụ** nêu điều cần giải thích; **1. DML: nhóm lệnh tác động lên dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **2. SELECT và toán tử: đọc, tính và biểu diễn kết quả** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 1. DML: nhóm lệnh tác động lên dữ liệu

DML (Data Manipulation Language, 데이터 조작어) là lớp lệnh làm việc với **các hàng trong bảng đã tồn tại**. Đây là điểm xuất phát cần nắm trước khi học từng câu lệnh: DML không tạo cấu trúc bảng như DDL, cũng không quyết định thời điểm chốt giao dịch như TCL; nó tạo ra thay đổi dữ liệu để transaction quản lý.

DML gồm `INSERT` để thêm hàng, `UPDATE` để sửa hàng, `DELETE` để xóa hàng và `SELECT` để truy vấn. `MERGE` mở rộng nhóm này bằng cách kết hợp cập nhật và chèn theo điều kiện đối chiếu. Trong Oracle, các thay đổi DML chưa trở thành kết quả bền vững cho đến khi `COMMIT`; trước thời điểm đó, `ROLLBACK` vẫn có thể hoàn tác. Do đó, đọc cú pháp DML luôn phải đi cùng hai câu hỏi: **hàng nào bị tác động** và **khi nào thay đổi được xác nhận**.

Như vậy, DML là cách biến một yêu cầu nghiệp vụ thành thay đổi trên hàng dữ liệu, còn transaction là lớp kiểm soát phía sau. Ta bắt đầu với trường hợp đơn giản nhất: bảng cần nhận thêm một hàng mới.

### 1.1. INSERT: thêm một hàng có chủ đích

Khi một đối tượng mới xuất hiện — chẳng hạn một thành viên mới — ta cần ánh xạ các giá trị của đối tượng đó vào các cột của bảng. `INSERT` giải quyết việc này bằng cách tạo thêm hàng; câu lệnh an toàn hay không phụ thuộc trước hết vào cách ta xác định cột.

```sql
INSERT INTO table_name (column1, column2, column5)
VALUES (value1, value2, value5);

INSERT INTO table_name
VALUES (value1, value2, value3, ...);
```

Cú pháp đầu tiên ghi rõ cột nhận giá trị, vì vậy không phụ thuộc vào thứ tự vật lý của bảng và giúp người đọc biết từng giá trị có ý nghĩa gì. Cú pháp thứ hai dựa hoàn toàn vào thứ tự cột đã định nghĩa; chỉ nên dùng khi ta chắc chắn thứ tự đó và cung cấp đủ giá trị. Cột bị bỏ qua chỉ có thể nhận `NULL` hoặc `DEFAULT` nếu định nghĩa cột cho phép. Nếu cột là `NOT NULL` mà không có giá trị mặc định hợp lệ, lệnh sẽ lỗi.

Theo nội dung ôn thi, Oracle chèn một hàng cho mỗi mệnh đề `VALUES`, còn SQL Server có thể cho nhiều nhóm giá trị trong một câu lệnh. Riêng Oracle, chuỗi rỗng `''` được xử lý như `NULL`; vì vậy khi cần kiểm tra giá trị thiếu, phải dùng `IS NULL`, không dùng `= ''`.

Điểm cần giữ lại là `INSERT` không chỉ là “đưa dữ liệu vào bảng”; nó là phép ghép **cột đích – giá trị – ràng buộc**. Khi đã biết cách tạo hàng, câu hỏi tiếp theo là làm sao thay đổi đúng những hàng đã tồn tại mà không chạm nhầm toàn bộ bảng. Đó là lý do ta chuyển sang `UPDATE`.

### 1.2. UPDATE: thay đổi đúng phạm vi

`UPDATE` dùng khi hàng đã tồn tại nhưng một hoặc nhiều thuộc tính của nó cần đổi. Mục tiêu của câu lệnh không chỉ là gán giá trị mới; quan trọng hơn là giới hạn đúng tập hàng bằng `WHERE`, bởi `SET` nói **sửa gì** còn `WHERE` nói **sửa ở đâu**.

```sql
UPDATE table_name
SET column1 = value1,
    column2 = value2
WHERE condition;
```

Nếu bỏ `WHERE`, mọi hàng trong bảng đều thỏa điều kiện ngầm định và sẽ bị cập nhật. Đây là bẫy SQLD quan trọng vì cú pháp vẫn hợp lệ nhưng hậu quả nghiệp vụ có thể rất lớn. `UPDATE` cũng có thể nhận kết quả từ subquery; khi gán nhiều cột, số cột bên trái phải khớp số giá trị mà subquery trả về cho mỗi hàng đích.

```sql
UPDATE emp
SET (sal, comm) = (
  SELECT AVG(sal), AVG(comm)
  FROM emp
)
WHERE ename = 'John';
```

Ví dụ trên cho thấy một thay đổi có thể được tính từ dữ liệu hiện có, nhưng phạm vi vẫn do `WHERE ename = 'John'` kiểm soát. Vì vậy, trước khi chạy `UPDATE`, hãy đọc theo thứ tự: xác định hàng đích, kiểm tra biểu thức tính giá trị, rồi mới xem xét việc `COMMIT`.

Ta đã thấy cách sửa thuộc tính mà vẫn giữ hàng. Trường hợp tiếp theo giữ lại cấu trúc bảng nhưng loại bỏ chính các hàng không còn cần nữa; đó là `DELETE`.

### 1.3. DELETE: xóa hàng, không xóa bảng

`DELETE` giải quyết nhu cầu loại bỏ dữ liệu khỏi bảng nhưng vẫn giữ nguyên bảng, cột và các ràng buộc. Vì nó tác động theo hàng, điều kiện `WHERE` tiếp tục là ranh giới an toàn: có `WHERE` thì xóa tập hàng được chọn, không có `WHERE` thì xóa toàn bộ hàng.

```sql
DELETE FROM table_name
WHERE condition;
```

Khác với `DROP TABLE`, `DELETE` không phá hủy cấu trúc. Và vì `DELETE` là DML, trong Oracle các hàng vừa xóa vẫn có thể được khôi phục bằng `ROLLBACK` nếu chưa `COMMIT`. Do đó, quy trình an toàn là chạy trước một `SELECT` với cùng điều kiện để xem tập hàng dự kiến, sau đó mới thực hiện `DELETE`.

Insight của phần này là “xóa dữ liệu” và “xóa đối tượng chứa dữ liệu” là hai việc khác nhau. Khi đã biết thêm, sửa và xóa từng loại hàng, ta có thể gặp bài toán thực tế hơn: bảng đích cần vừa cập nhật bản ghi cũ vừa thêm bản ghi mới dựa trên một bảng nguồn. Ta chuyển sang `MERGE`.

### 1.4. MERGE: đồng bộ hai nguồn dữ liệu

`MERGE` dùng khi ta có bảng nguồn và bảng đích, rồi muốn quyết định theo điều kiện `ON` rằng một hàng đã tồn tại hay chưa. Nó gom hai nhánh nghiệp vụ vào một câu lệnh: hàng khớp thì `UPDATE` hoặc `DELETE` theo điều kiện; hàng không khớp thì `INSERT`.

```sql
MERGE INTO team t
USING member m
ON (t.member_id = m.member_id)
WHEN MATCHED THEN
  UPDATE SET t.name = m.name, t.email = m.email
WHEN NOT MATCHED THEN
  INSERT (team_id, name, email)
  VALUES (m.member_id, m.name, m.email);
```

Hãy đọc câu lệnh theo ba bước: `USING` cho biết dữ liệu mới đến từ đâu, `ON` định nghĩa thế nào là cùng một đối tượng, còn hai nhánh `MATCHED` và `NOT MATCHED` mô tả hệ quả của việc đối chiếu. Vì vậy, `MERGE` phù hợp với dữ liệu staging hoặc quy trình đồng bộ thành viên; nó không phải là một phép “gộp tùy ý” mà phụ thuộc vào khóa/điều kiện nhận diện đúng.

Đến đây, ta đã đi qua các lệnh làm thay đổi dữ liệu. Nhưng sau mỗi thay đổi, người học vẫn cần đọc kết quả và kiểm tra biểu thức mà không làm thay đổi bảng. Ta quay lại `SELECT`, nền tảng để quan sát dữ liệu.

> **Chuyển mạch:** Sau khi hiểu DML thay đổi dữ liệu và điều kiện giao dịch, hãy sang **SELECT và toán tử** để đọc, tính và biểu diễn kết quả trên trạng thái vừa thay đổi.

## 2. SELECT và toán tử: đọc, tính và biểu diễn kết quả

Phần này nối DML với kỹ năng truy vấn đã học trước đó. `SELECT` không sửa dữ liệu; nó tạo ra một tập kết quả từ bảng, rồi các toán tử giúp tính toán hoặc ghép các giá trị trong từng dòng. Tách rõ hai vai trò này giúp tránh nhầm giữa **biểu thức hiển thị** và **thay đổi được lưu vào bảng**.

### 2.1. SELECT: kiểm tra dữ liệu sau thay đổi

`SELECT` đọc những cột cần thiết từ bảng. `ALL` là mặc định, nghĩa là giữ mọi dòng; `DISTINCT` loại các dòng trùng theo toàn bộ danh sách cột được chọn.

```sql
SELECT [ALL | DISTINCT] column_name
FROM table_name;
```

Các bài `JOIN`, `GROUP BY`, subquery, Window Function và Hierarchical Query đều mở rộng khung `SELECT` này: chúng thay đổi cách tạo hoặc xử lý tập kết quả, chứ không thay đổi bản chất rằng `SELECT` đang đọc dữ liệu. Vì vậy, sau một `INSERT`, `UPDATE`, `DELETE` hoặc `MERGE`, `SELECT` là công cụ kiểm tra đầu tiên để đối chiếu số hàng và giá trị thực tế.

Ta đã xác định được dữ liệu đầu ra. Bây giờ cần hiểu cách một biểu thức biến các giá trị đầu vào thành kết quả mới; trước hết là phép tính số học.

### 2.2. Toán tử số học: quy tắc tính trên dữ liệu

Toán tử số học áp dụng cho `NUMBER` và `DATE`. Với số, thứ tự ưu tiên là ngoặc `()` trước phép nhân/chia `*`, `/`, rồi đến cộng/trừ `+`, `-`. Với ngày, phép cộng hoặc trừ thường biểu thị số ngày theo cách xử lý của DBMS.

Điều này quan trọng vì SQL không đọc biểu thức theo cảm giác; cùng một dãy toán tử có thể cho kết quả khác nếu không hiểu độ ưu tiên. Hãy dùng ngoặc khi muốn làm rõ quy tắc nghiệp vụ, nhất là khi biểu thức được dùng trong `SELECT` hoặc điều kiện lọc.

Sau phép tính, ta chuyển sang trường hợp kết quả không còn là một con số mà là một chuỗi mô tả người dùng có thể đọc được. Đó là nối chuỗi.

### 2.3. Toán tử nối chuỗi: tạo biểu thức hiển thị

Toán tử nối chuỗi ghép một cột với chuỗi ký tự hoặc ghép nhiều cột để tạo ra một giá trị văn bản mới. Oracle dùng `||`, SQL Server thường dùng `+`, còn `CONCAT` là hàm nối chuỗi.

```sql
-- Oracle
SELECT first_name || ' ' || last_name AS full_name
FROM employees;

-- SQL Server
SELECT first_name + ' ' + last_name AS full_name
FROM employees;

SELECT CONCAT('Hello, ', 'World!') AS greeting;
```

Trong SQL Server, cần phân biệt `+` dùng để cộng số với `+` dùng để nối chuỗi: kiểu dữ liệu của biểu thức quyết định ý nghĩa. Kết quả nối chỉ là một biểu thức trong tập `SELECT`, không tự ghi ngược vào bảng; muốn lưu nó, ta phải chủ động dùng `INSERT` hoặc `UPDATE` và chịu các ràng buộc transaction tương ứng.

Như vậy, toàn bộ bài đi theo một vòng khép kín: `INSERT`/`UPDATE`/`DELETE`/`MERGE` tác động lên dữ liệu, `SELECT` kiểm tra kết quả, còn toán tử biến dữ liệu thành giá trị tính toán hoặc biểu diễn. Ranh giới cuối cùng cần nhớ là **biểu thức hiển thị không đồng nghĩa với thay đổi đã lưu**. Sang bài **TCL và Transaction**, ta sẽ học chính xác khi nào các thay đổi DML được `COMMIT`, khi nào còn có thể `ROLLBACK`, và vì sao thứ tự đó quyết định tính an toàn của giao dịch.

> **Bàn giao:** Sau **2. SELECT và toán tử: đọc, tính và biểu diễn kết quả**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
