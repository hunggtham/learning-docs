<!-- lecture-contract: v2 -->
# TCL và Transaction (Giao dịch)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **TCL và Transaction**. Route đi từ DML mutations → ACID properties → COMMIT/ROLLBACK mechanism → Nested SAVEPOINT trace → DDL implicit auto-commit, đảm bảo tính toàn vẹn và khả năng kiểm soát dữ liệu.
>
> **Mục tiêu:** Nắm vững bản chất giao dịch, 4 thuộc tính ACID, cơ chế hoạt động của `COMMIT`, `ROLLBACK`, kịch bản `SAVEPOINT` lồng nhau kèm bảng trace trạng thái dữ liệu, và bẫy Auto-commit ngầm định của lệnh DDL trong Oracle Database.
>
> **Phạm vi tham khảo:** PDF *2024 개정판 SQLD 개념정리*, Mục II Kiểm soát giao dịch (trang 87–89).

---

### 1. 트랜잭션 (Transaction) — Đơn vị công việc logic

> **KR:** 트랜잭션은 데이터베이스의 논리적 연산단위이며, 더 이상 분할할 수 없는 최소의 수행 단위이다.

Giao dịch (Transaction) là một chuỗi các thao tác SQL hợp thành một đơn vị công việc logic hoàn chỉnh. Bản chất cốt lõi của giao dịch được đúc kết qua nguyên lý **Tất cả hoặc Không có gì (All or Nothing)**: mọi thao tác bên trong một transaction hoặc phải cùng thành công trọn vẹn và được lưu lại vĩnh viễn, hoặc phải cùng bị hủy bỏ hoàn toàn để đưa cơ sở dữ liệu về trạng thái hợp lệ ban đầu.

#### Tình huống nghiệp vụ kinh điển: Chuyển khoản ngân hàng (계좌이체)
Giả sử khách hàng A muốn chuyển 500,000 VND sang tài khoản khách hàng B. Tiến trình này bao gồm 2 thao tác DML bắt buộc:
1. Trừ 500,000 VND từ tài khoản A: `UPDATE account SET balance = balance - 500000 WHERE id = 'A';`
2. Cộng 500,000 VND vào tài khoản B: `UPDATE account SET balance = balance + 500000 WHERE id = 'B';`

Nếu bước 1 thành công nhưng bước 2 thất bại do đường truyền mạng hoặc sự cố phần cứng, hệ thống không thể để tài khoản A mất tiền mà tài khoản B chưa nhận được. Khi đó, toàn bộ thay đổi ở bước 1 phải được khôi phục ngay lập tức (`ROLLBACK`). Chỉ khi cả hai bước cùng hoàn tất không có lỗi, giao dịch mới được chốt vĩnh viễn (`COMMIT`).

---

### 2. 트랜잭션의 4대 특성 (ACID) — 4 thuộc tính cốt lõi của giao dịch

Để đảm bảo độ tin cậy và tính nhất quán của dữ liệu trong môi trường nhiều người dùng đồng thời truy cập, mỗi giao dịch bắt buộc phải tuân thủ nghiêm ngặt 4 nguyên tắc ACID:

| Thuộc tính (Korean / English) | Định nghĩa kỹ thuật | Cơ chế bảo đảm trong DBMS | Tình huống đề thi nhận diện |
| --- | --- | --- | --- |
| **원자성 (Atomicity - Tính nguyên tử)** | Toàn bộ các thao tác trong giao dịch phải hoàn tất 100% hoặc hoàn toàn không được thực hiện gì cả. | Sử dụng **Undo Segment** để ghi lại nhật ký hoàn tác nếu xảy ra lỗi. | Nguyên lý `All or Nothing`. Gặp lỗi giữa chừng thì tự động hoặc thủ công gọi `ROLLBACK`. |
| **일관성 (Consistency - Tính nhất quán)** | Giao dịch đưa CSDL từ trạng thái hợp lệ này sang trạng thái hợp lệ khác, không vi phạm bất kỳ ràng buộc nào. | Kiểm tra các ràng buộc toàn vẹn (`PK`, `FK`, `CHECK`, `NOT NULL`) trước khi kết thúc giao dịch. | Tài khoản không được âm tiền nếu có `CHECK (balance >= 0)`. Tổng số dư toàn hệ thống trước và sau chuyển khoản phải bằng nhau. |
| **고립성 (Isolation - Tính cô lập)** | Các giao dịch đang diễn ra đồng thời không được can thiệp hoặc nhìn thấy dữ liệu trung gian chưa hoàn tất của nhau. | Cơ chế khóa tài nguyên (**Locks**) và các mức độ cô lập (Isolation Levels). | Giao dịch B không được đọc thấy dữ liệu đang sửa đổi của giao dịch A khi A chưa `COMMIT` (tránh Dirty Read). |
| **지속성 (Durability - Tính bền vững)** | Sau khi giao dịch đã `COMMIT` thành công, các thay đổi dữ liệu sẽ được lưu vĩnh viễn vào hệ thống. | Sử dụng **Redo Log Buffer** và ghi nhật ký xuống tệp Redo Log trên đĩa cứng trước khi trả về xác nhận. | Máy chủ bị mất điện đột ngột hoặc sập hệ điều hành ngay sau khi `COMMIT`, khi khởi động lại dữ liệu vẫn được bảo toàn nguyên vẹn. |

---

### 3. TCL (Transaction Control Language) — Ngôn ngữ điều khiển giao dịch

TCL là nhóm lệnh dùng để quản lý trạng thái của các thay đổi do lệnh DML tạo ra:

```
+---------------------------------------------------------------------------------+
|                          CƠ CHẾ LƯU TRỮ VÀ KHÓA CỦA DML                         |
|                                                                                 |
|  [Session 1 (Người sửa)]                       [Session 2 (Người khác)]          |
|  - Chạy UPDATE emp SET sal = 5000              - Chạy SELECT sal FROM emp       |
|  - Dữ liệu đổi trong Buffer Cache              - Nhìn thấy dữ liệu cũ trong     |
|  - Hàng bị khóa (Row-Level Lock)                 Undo Segment (Read Consistency)|
|  - Thấy sal = 5000                             - Thấy sal cũ (chưa sửa)         |
|         |                                                                       |
|         v                                                                       |
|    Phát lệnh COMMIT;                                                            |
|         |                                                                       |
|         +---> 1. Dữ liệu ghi bền vững xuống tệp Datafile qua DBWn/LGWR.         |
|         +---> 2. Giải phóng toàn bộ Row Lock.                                   |
|         +---> 3. Session 2 lập tức nhìn thấy sal mới = 5000.                    |
+---------------------------------------------------------------------------------+
```

#### Các lệnh điều khiển chính
- **`COMMIT` (Xác nhận giao dịch):**
  - Chốt vĩnh viễn các thao tác DML đã thực hiện kể từ lệnh `COMMIT` trước đó.
  - Giải phóng toàn bộ các khóa tài nguyên trên hàng/bảng để các phiên khác có thể tiếp tục thao tác.
  - Dữ liệu mới trở nên hiển thị công khai với toàn bộ các phiên làm việc trong hệ thống.
  - **Một khi đã `COMMIT`, hoàn toàn không thể dùng `ROLLBACK` để quay lại.**
- **`ROLLBACK` (Hoàn tác giao dịch):**
  - Hủy bỏ toàn bộ các thay đổi DML chưa được commit trong giao dịch hiện tại.
  - Khôi phục lại trạng thái dữ liệu tại thời điểm `COMMIT` gần nhất (hoặc tại một điểm `SAVEPOINT` xác định).
  - Giải phóng mọi khóa tài nguyên đang bị chiếm giữ.
- **`SAVEPOINT` (Điểm lưu tạm thời):**
  - Đánh dấu các mốc trung gian bên trong một giao dịch lớn.
  - Cho phép người dùng rollback một phần công việc (Partial Rollback) về mốc đã chọn mà không làm mất công sức của các bước thành công trước đó.

---

### 4. So sánh chế độ giao dịch giữa Oracle và SQL Server

Đề thi SQLD thường xuyên đặt câu hỏi so sánh trực tiếp cơ chế quản lý giao dịch giữa hai hệ quản trị CSDL phổ biến nhất:

| Tiêu chí so sánh | Oracle Database | Microsoft SQL Server |
| --- | --- | --- |
| **Chế độ giao dịch mặc định** | **Giao dịch ngầm định (Implicit Transaction)**: DML không tự commit. | **Tự động Commit (AUTO-COMMIT Mode)**: Mỗi câu lệnh DML riêng lẻ tự động commit ngay lập tức. |
| **Bắt đầu một giao dịch** | Tự động mở giao dịch mới khi phát sinh câu lệnh DML đầu tiên. | Phải dùng lệnh tường minh: `BEGIN TRANSACTION` (hoặc `BEGIN TRAN`). |
| **Kết thúc giao dịch** | Bắt buộc người dùng phải gõ lệnh `COMMIT` hoặc `ROLLBACK`. | Nếu dùng `BEGIN TRAN`, phải gọi `COMMIT TRAN` hoặc `ROLLBACK TRAN`. |
| **Khả năng cấu hình** | Trước bản 23c không có chế độ tự động commit cho DML. | Hỗ trợ 3 chế độ: 1) Auto-commit (mặc định), 2) Implicit (`SET IMPLICIT_TRANSACTIONS ON`), 3) Explicit. |
| **Ảnh hưởng của lệnh DDL (`CREATE`, `ALTER`, `DROP`)** | **TỰ ĐỘNG COMMIT NGẦM ĐỊNH (Implicit Auto-Commit)** trước và sau khi chạy DDL. | **KHÔNG tự động commit**. Lệnh DDL có thể nằm trong transaction và **CÓ THỂ ROLLBACK** bình thường! |

```sql
-- MINH HỌA SỰ KHÁC BIỆT KHI CHẠY DDL TRONG GIAO DỊCH:

-- 1. Trong Microsoft SQL Server (DDL có thể ROLLBACK được):
BEGIN TRANSACTION;
CREATE TABLE temp_test (id INT);
INSERT INTO temp_test VALUES (1);
ROLLBACK; -- Bảng temp_test bị hủy bỏ hoàn toàn, không hề tồn tại trong CSDL!

-- 2. Trong Oracle Database (DDL kích hoạt Auto-Commit ngầm định):
-- Lệnh CREATE TABLE tự động chốt vĩnh viễn các DML trước đó và chính nó, cấm hoàn tác!
```

---

### 5. Cạm bẫy tử thần: DDL Auto-Commit ngầm định trong Oracle

Đây là một trong những câu hỏi bẫy kinh điển và xuất hiện nhiều nhất trong đề thi chứng chỉ SQLD.

#### Nguyên lý vận hành của câu lệnh DDL trong Oracle
Khi bạn phát một câu lệnh DDL (như `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, `TRUNCATE TABLE`, `RENAME`...):
1. Oracle Engine tự động phát một lệnh **`COMMIT` ngầm định** trước khi lệnh DDL bắt đầu thực thi.
2. Hệ thống thực thi thay đổi cấu trúc bảng và cập nhật Từ điển dữ liệu (Data Dictionary).
3. Sau khi hoàn thành, Oracle tiếp tục phát thêm một lệnh **`COMMIT` ngầm định** thứ hai.

```
+---------------------------------------------------------------------------------+
|                     CHUỖI TÁC ĐỘNG CỦA DDL TRONG PHIÊN ORACLE                   |
|                                                                                 |
|  1. UPDATE emp SET sal = 9000 WHERE empno = 7788;  (DML - Đang chờ commit)      |
|  2. SAVEPOINT s1;                                  (Tạo mốc lưu tạm)            |
|  3. INSERT INTO emp (empno) VALUES (9999);         (DML - Đang chờ commit)      |
|                                                                                 |
|  4. CREATE TABLE temp_log (msg VARCHAR2(100));     <=== CHẠY LỆNH DDL TẠI ĐÂY!  |
|     |                                                                           |
|     +--> PHÁT SINH IMPLICIT COMMIT NGAY TỨC THÌ!                                |
|          - Toàn bộ lệnh UPDATE và INSERT ở bước 1 và 3 ĐÃ BỊ CHỐT VĨNH VIỄN!    |
|          - Điểm lưu tạm SAVEPOINT s1 BỊ XÓA BỎ HOÀN TOÀN KHỎI HỆ THỐNG!        |
|                                                                                 |
|  5. ROLLBACK TO s1;  ===> BÁO LỖI ORA-01086: savepoint 'S1' never established!  |
|  6. ROLLBACK;        ===> HOÀN TOÀN VÔ HIỆU! Dữ liệu bước 1 & 3 không thể mất!  |
+---------------------------------------------------------------------------------+
```

> **Ghi nhớ thi cử sống còn:** Bất kỳ thao tác DML nào đứng trước một câu lệnh DDL trong Oracle đều **tự động bị ghi vĩnh viễn** vào cơ sở dữ liệu. Mọi điểm `SAVEPOINT` trước đó đều bị xóa sổ. Lệnh `ROLLBACK` phát sau DDL sẽ hoàn toàn vô tác dụng đối với những thay đổi trước DDL.

---

### 6. SAVEPOINT와 부분 롤백 (Partial Rollback) — Điểm lưu tạm và Kịch bản lồng nhau

Khi thực hiện một chuỗi nhiều nghiệp vụ phức tạp, `SAVEPOINT` cho phép chia nhỏ tiến trình để xử lý lỗi linh hoạt.

#### Cú pháp
- **Oracle:**
  - Khai báo điểm lưu: `SAVEPOINT savepoint_name;`
  - Hoàn tác về điểm lưu: `ROLLBACK TO savepoint_name;` (hoặc `ROLLBACK TO SAVEPOINT savepoint_name;`).
- **SQL Server:**
  - Khai báo: `SAVE TRANSACTION savepoint_name;` (hoặc `SAVE TRAN savepoint_name;`).
  - Hoàn tác: `ROLLBACK TRANSACTION savepoint_name;`.

#### Hai quy tắc cốt lõi của SAVEPOINT trong đề thi SQLD

1. **Quy tắc ghi đè tên (Name Overwriting):**
   - Trong cùng một giao dịch, nếu bạn tạo nhiều `SAVEPOINT` có **cùng một tên**, điểm lưu tạm được tạo sau cùng sẽ **ghi đè và thay thế hoàn toàn** điểm lưu tạm được tạo trước đó. Điểm lưu cũ không còn hiệu lực.
2. **Quy tắc hủy bỏ điểm lưu phía sau khi Rollback (Savepoint Invalidation):**
   - Giả sử thứ tự tạo điểm lưu là: `mốc A` $\rightarrow$ `mốc B` $\rightarrow$ `mốc C`.
   - Nếu bạn thực hiện `ROLLBACK TO SAVEPOINT A;`:
     - Dữ liệu được đưa về trạng thái tại thời điểm mốc A.
     - **Tất cả các điểm lưu tạo sau mốc A (tức là mốc B và mốc C) sẽ bị hệ thống tự động xóa bỏ hoàn toàn!**
     - Nếu sau đó bạn tiếp tục gọi `ROLLBACK TO SAVEPOINT B;`, hệ thống sẽ ném ra lỗi do mốc B không còn tồn tại trong phiên làm việc.

---

#### Bảng Trace kịch bản SAVEPOINT chi tiết (SQLD Classic Trace Case)

Bài toán thi cử điển hình: Ban đầu bảng `PLAYER` có **480 cầu thủ**, và không có cầu thủ nào nặng 100kg (`SELECT COUNT(*) FROM player WHERE weight = 100` trả về **0**).

Hãy theo dõi sự biến đổi dữ liệu qua chuỗi lệnh sau:

```sql
-- [Thao tác 1]: Thêm 1 cầu thủ mới
INSERT INTO player (player_id, team_id, player_name, weight)
VALUES ('999', 'K01', 'Park', 75);

-- [Thao tác 2]: Đánh dấu mốc SP_A
SAVEPOINT sp_a;

-- [Thao tác 3]: Cập nhật cân nặng toàn bộ cầu thủ thành 100kg
UPDATE player
SET weight = 100;

-- [Thao tác 4]: Đánh dấu mốc SP_B
SAVEPOINT sp_b;

-- [Thao tác 5]: Xóa toàn bộ cầu thủ trong bảng
DELETE FROM player;
```

Bảng theo dõi trạng thái dữ liệu ứng với từng kịch bản kết thúc độc lập:

| Kịch bản thực thi tiếp theo | Tổng số cầu thủ trong bảng | Số cầu thủ có weight = 100 | Trạng thái các SAVEPOINT trong phiên | Phân tích bản chất kỹ thuật |
| --- | --- | --- | --- | --- |
| **Tại thời điểm sau Thao tác 5** | **0** hàng (Bảng rỗng) | **0** hàng | `sp_a`, `sp_b` đều đang tồn tại | Toàn bộ dữ liệu vừa bị DELETE trong buffer cache. |
| **Kịch bản 1:** Gọi `ROLLBACK TO sp_b;` | **481** hàng | **481** hàng | `sp_a`, `sp_b` tiếp tục tồn tại | Lệnh DELETE bị hủy bỏ. Khôi phục lại 481 cầu thủ, tất cả đều có cân nặng 100kg. |
| **Kịch bản 2:** Sau KB1, gọi tiếp `ROLLBACK TO sp_a;` | **481** hàng | **0** hàng | Chỉ còn lại `sp_a` (`sp_b` đã bị hủy bỏ) | Lệnh UPDATE bị hủy bỏ. Cầu thủ 'Park' vẫn còn (481 người), nhưng cân nặng trở về như cũ (0 người nặng 100kg). `sp_b` bị xóa sổ. |
| **Kịch bản 3:** Sau KB2, gọi tiếp `ROLLBACK;` trần | **480** hàng | **0** hàng | Tất cả Savepoint bị xóa sạch | Lệnh INSERT đầu tiên bị hủy bỏ. Đưa CSDL về mốc commit trước đó (480 người ban đầu). |

---

### 7. Cạm bẫy thi cử trọng điểm (출제 함정 & 오답 노트)

1. **Bẫy DDL chèn giữa các lệnh DML trong đề thi Oracle:**
   - *Tình huống:* Thực hiện `INSERT` $\rightarrow$ `UPDATE` $\rightarrow$ Chạy `CREATE TABLE` hoặc `TRUNCATE TABLE` $\rightarrow$ Gọi `ROLLBACK`.
   - *Kết quả:* Lệnh `ROLLBACK` không có tác dụng với các lệnh `INSERT` và `UPDATE` trước đó vì lệnh DDL đã phát sinh commit ngầm định.
2. **Bẫy gọi SAVEPOINT đã bị vô hiệu hóa:**
   - Khi đã rollback về một Savepoint phía trước, cố gắng rollback về một Savepoint phía sau sẽ gặp lỗi không tồn tại điểm lưu.
3. **Bẫy phân biệt phạm vi nhìn thấy dữ liệu trước và sau COMMIT:**
   - Trước `COMMIT`: Chỉ có người chạy lệnh (Current Session) nhìn thấy dữ liệu sửa đổi. Các người dùng khác (Other Sessions) nhìn thấy dữ liệu cũ lấy từ Undo Segment.
   - Sau `COMMIT`: Tất cả mọi người dùng trong hệ thống đều nhìn thấy dữ liệu mới.
4. **Bẫy đóng phiên làm việc (Session Termination):**
   - Đóng kết nối bình thường (Normal Exit / Disconnect): Oracle tự động phát lệnh `COMMIT`.
   - Phiên làm việc bị ngắt đột ngột (Abnormal Termination / Crash): Oracle tự động phát lệnh `ROLLBACK`.

---

### 8. Câu hỏi trắc nghiệm thi thử mô phỏng (실전 기출 변형 문제 & 정답 해설)

#### Câu 1: Tác động của DDL ngầm định Auto-commit trong Oracle
Xét kịch bản các thao tác SQL được thực hiện tuần tự trong một phiên làm việc trên Oracle Database:
```sql
UPDATE ACCOUNT SET BALANCE = BALANCE + 1000 WHERE ACC_NO = 101;
SAVEPOINT SP1;
INSERT INTO ACCOUNT_LOG VALUES (101, 'BONUS', SYSDATE);
SAVEPOINT SP2;
UPDATE ACCOUNT SET BALANCE = BALANCE - 200 WHERE ACC_NO = 101;
CREATE TABLE TEMP_AUDIT (AUDIT_ID INT);
ROLLBACK TO SP1;
```
Điều gì sẽ xảy ra khi dòng lệnh cuối cùng `ROLLBACK TO SP1;` được thực thi?
- A. Dữ liệu quay trở về trạng thái tại mốc `SP1`, giao dịch tiếp tục diễn ra bình thường.
- B. Lệnh `ROLLBACK TO SP1;` hoàn tác cả lệnh `CREATE TABLE` và đưa số dư tài khoản về trạng thái ban đầu.
- C. Báo lỗi do điểm lưu tạm `SP1` không còn tồn tại vì lệnh DDL `CREATE TABLE` đã tự động kích hoạt COMMIT trước đó.
- D. Toàn bộ các thao tác trước `SP1` bị hủy bỏ, chỉ giữ lại bảng `TEMP_AUDIT`.

> **Đáp án chính xác:** **C**
>
> **Giải thích chi tiết:**
> - Trong Oracle Database, các câu lệnh DDL (`CREATE`, `ALTER`, `DROP`, `TRUNCATE`...) luôn đi kèm cơ chế **Implicit Auto-Commit** (tự động phát lệnh COMMIT trước và sau khi thực thi DDL).
> - Khi câu lệnh `CREATE TABLE TEMP_AUDIT` được thực thi:
>   1. Toàn bộ các thay đổi DML trước đó (lệnh `UPDATE` đầu tiên, lệnh `INSERT` và lệnh `UPDATE` thứ hai) đều được **chốt vĩnh viễn (COMMIT)** vào CSDL.
>   2. Toàn bộ các điểm lưu tạm trung gian đã tạo (`SP1` và `SP2`) **đều bị hủy bỏ hoàn toàn** khỏi phiên làm việc.
> - Do đó, khi gọi lệnh `ROLLBACK TO SP1;`, Oracle không thể tìm thấy điểm lưu `SP1` và sẽ trả về lỗi: `ORA-01086: savepoint 'SP1' never established in this session or is invalid`.

---

#### Câu 2: Quy tắc Invalidation của SAVEPOINT
Bảng `DEPARTMENT` có 5 phòng ban. Thực hiện chuỗi thao tác sau trong một giao dịch:
```sql
INSERT INTO DEPARTMENT VALUES (60, 'SECURITY');
SAVEPOINT SV_A;
INSERT INTO DEPARTMENT VALUES (70, 'LOGISTICS');
SAVEPOINT SV_B;
INSERT INTO DEPARTMENT VALUES (80, 'LEGAL');
ROLLBACK TO SV_A;
ROLLBACK TO SV_B;
```
Kết quả thực thi dòng lệnh cuối cùng `ROLLBACK TO SV_B;` là gì?
- A. Hoàn tác lệnh chèn phòng ban 80 và giữ lại phòng ban 70.
- B. Hệ thống thông báo lỗi vì điểm lưu tạm `SV_B` đã bị xóa khi thực hiện `ROLLBACK TO SV_A`.
- C. Bảng có tổng cộng 7 phòng ban.
- D. Khôi phục lại trạng thái tại điểm lưu `SV_B`, phòng ban 70 được khôi phục.

> **Đáp án chính xác:** **B**
>
> **Giải thích chi tiết:**
> - Sau khi nạp phòng ban 70 và đánh dấu `SAVEPOINT SV_B`, tiếp tục nạp phòng ban 80.
> - Lệnh `ROLLBACK TO SV_A;` khôi phục CSDL về trạng thái tại mốc `SV_A` (chỉ có phòng ban 60).
> - Theo nguyên tắc kỹ thuật của TCL trong SQL, khi thực hiện quay lui về một điểm lưu phía trước (`SV_A`), **toàn bộ các điểm lưu được tạo sau mốc đó (ở đây là `SV_B`) sẽ tự động bị hủy bỏ vĩnh viễn (Invalidated)**.
> - Khi cố tình gọi tiếp `ROLLBACK TO SV_B;`, hệ thống không còn mốc `SV_B` để tham chiếu nên sẽ ném ra lỗi cú pháp/thực thi.

---

#### Câu 3: Nhận diện 4 thuộc tính ACID
Xét tình huống nghiệp vụ:
Một khách hàng thực hiện thanh toán hóa đơn trực tuyến trị giá 2,000,000 VND. Hệ thống trừ tiền tài khoản thành công và màn hình thông báo: *"Giao dịch đã được ghi nhận thành công"*. Tuy nhiên, chỉ 1 giây sau đó, toàn bộ trung tâm dữ liệu gặp sự cố mất điện đột ngột làm máy chủ Database sập nguồn ngay lập tức. Sau khi hệ thống điện dự phòng khởi động lại máy chủ, dữ liệu kiểm toán cho thấy khoản thanh toán 2,000,000 VND vẫn tồn tại chính xác trong hệ thống.
Thuộc tính nào trong 4 đặc tính ACID bảo đảm sự toàn vẹn của tình huống trên?
- A. Tính nguyên tử (Atomicity)
- B. Tính nhất quán (Consistency)
- C. Tính cô lập (Isolation)
- D. Tính bền vững (Durability)

> **Đáp án chính xác:** **D**
>
> **Giải thích chi tiết:**
> - **A (Tính nguyên tử):** Đảm bảo nguyên lý "tất cả hoặc không", nếu lỗi thì hoàn tác toàn bộ.
> - **B (Tính nhất quán):** Đảm bảo các quy tắc toàn vẹn dữ liệu (không âm tiền, đúng định dạng).
> - **C (Tính cô lập):** Đảm bảo các phiên chạy đồng thời không can thiệp dữ liệu lẫn nhau.
> - **D (Tính bền vững - Durability):** Đảm bảo rằng một khi giao dịch đã được xác nhận hoàn tất thành công (`COMMIT`), các thay đổi đó sẽ được lưu trữ vĩnh viễn trên thiết bị nhớ không khả biến (đĩa cứng, thông qua Redo Log) và không bao giờ bị mất đi, ngay cả khi xảy ra sự cố sập nguồn máy chủ hoặc lỗi hệ điều hành đột ngột.

---

#### Câu 4: Sự khác biệt về giao dịch giữa SQL Server và Oracle
Phát biểu nào sau đây là **ĐÚNG** khi so sánh cơ chế quản lý giao dịch giữa Microsoft SQL Server và Oracle Database?
- A. Cả Oracle và SQL Server đều mặc định tự động commit cho từng câu lệnh DML riêng lẻ.
- B. Trong SQL Server, các câu lệnh DDL như `CREATE TABLE` có thể được rollback nếu được đặt trong một transaction rõ ràng bằng `BEGIN TRANSACTION`.
- C. Trong Oracle Database, người dùng có thể dễ dàng rollback một câu lệnh DDL nếu chưa thực hiện ngắt kết nối.
- D. Trong SQL Server, không hỗ trợ điểm lưu tạm `SAVEPOINT` mà chỉ hỗ trợ hoàn tác toàn bộ giao dịch.

> **Đáp án chính xác:** **B**
>
> **Giải thích chi tiết:**
> - **A sai:** Oracle không mặc định auto-commit cho DML; người dùng phải gõ `COMMIT` tường minh.
> - **B đúng:** SQL Server hỗ trợ giao dịch tường minh (`BEGIN TRANSACTION`), bên trong đó các câu lệnh DDL (`CREATE TABLE`, `DROP TABLE`, v.v.) vẫn tham gia vào transaction và hoàn toàn có thể được khôi phục nguyên trạng bằng lệnh `ROLLBACK TRANSACTION`.
> - **C sai:** Trong Oracle Database, DDL kích hoạt cơ chế tự động commit ngầm định, tuyệt đối không thể rollback được.
> - **D sai:** SQL Server hỗ trợ đầy đủ điểm lưu tạm thông qua cú pháp `SAVE TRANSACTION savepoint_name`.

---

## 9. Nối mạch sang Bài tiếp theo: DDL và định nghĩa bảng

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 09 đã giải quyết trọn vẹn cơ chế kiểm soát giao dịch, 4 thuộc tính ACID, kịch bản `SAVEPOINT` lồng nhau và bẫy Auto-commit ngầm định của lệnh DDL trong Oracle.
> - **Đang giải quyết gì:** Các giao dịch DML và TCL chỉ có ý nghĩa khi có các cấu trúc bảng chứa dữ liệu. Làm thế nào để định nghĩa kiểu dữ liệu, áp đặt quy tắc đặt tên, mở rộng cấu trúc bảng bằng `ALTER TABLE`, và so sánh chuyên sâu cơ chế giải phóng High Water Mark (HWM) giữa `TRUNCATE`, `DROP`, `DELETE`?
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 10 — DDL và định nghĩa bảng](./10-ddl-va-dinh-nghia-bang.md) để học cách kiến tạo và hiệu chỉnh cấu trúc bảng bằng `CREATE TABLE`, kỹ thuật nhân bản `CTAS`, và bản chất quản lý dung lượng ổ đĩa.
