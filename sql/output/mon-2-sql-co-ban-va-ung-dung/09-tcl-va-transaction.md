# TCL và Transaction

> **Nguồn bám sát:** PDF *2024 개정판 SQLD 개념정리*, trang 87–89.
>
> **Liên kết bài trước:** DML thay đổi dữ liệu; TCL quyết định khi nào các thay đổi đó trở thành dữ liệu chính thức hoặc bị hủy.

## 1. TCL (Transaction Control Language) (ngôn ngữ điều khiển giao dịch)

> **KR:** TCL은 COMMIT, ROLLBACK, SAVEPOINT를 포함하며 DML에 의해 조작된 결과를 작업단위(트랜잭션)별로 제어한다.

TCL gồm `COMMIT` (Commit) (xác nhận lưu), `ROLLBACK` (Rollback) (hoàn tác) và `SAVEPOINT` (Savepoint) (điểm lưu tạm). Nó không trực tiếp thêm/sửa/xóa hàng, mà kiểm soát các thay đổi do DML tạo ra theo đơn vị transaction (Transaction) (giao dịch).

## 2. 트랜잭션 (Transaction) (giao dịch)

> **KR:** 트랜잭션은 데이터베이스의 논리적 연산단위이며 분할할 수 없는 최소의 단위이다.

Transaction là một đơn vị công việc logic, không thể tách nhỏ khi xét tính đúng đắn. Ví dụ chuyển tiền cần cả việc trừ ở tài khoản A lẫn cộng ở tài khoản B thành công; nếu một bước thất bại, cả hai phải trở về trạng thái cũ. Đây là nguyên tắc `ALL OR NOTHING` (all-or-nothing) (tất cả hoặc không gì cả).

## 3. 트랜잭션의 특징 (ACID) (đặc tính giao dịch)

| 한국어 (English) (Tiếng Việt) | Giải thích |
| --- | --- |
| 원자성 (Atomicity) (tính nguyên tử) | Toàn bộ thao tác trong transaction đều thành công hoặc không thao tác nào được áp dụng. |
| 일관성 (Consistency) (tính nhất quán) | Nếu DB hợp lệ trước transaction thì sau transaction cũng phải hợp lệ; không được phá vỡ ràng buộc và quy tắc dữ liệu. |
| 고립성 (Isolation) (tính cô lập) | Transaction đang chạy không được chịu ảnh hưởng làm tạo ra kết quả sai do transaction khác. |
| 지속성 (Durability) (tính bền vững) | Khi transaction đã thành công, dữ liệu đã cập nhật được lưu bền vững. |

## 4. COMMIT (Commit) (xác nhận lưu)

> **KR:** COMMIT은 올바르게 반영된 데이터를 데이터베이스에 반영시키는 명령어이며, COMMIT 이전에 수행된 DML은 모두 저장되어 되돌릴 수 없다.

`COMMIT` kết thúc transaction hiện tại và làm các DML trước đó trở thành bền vững. Sau `COMMIT`, không thể dùng `ROLLBACK` để quay lại những thay đổi đó. Vì vậy, trước khi commit một `UPDATE` hoặc `DELETE` diện rộng, cần kiểm tra điều kiện `WHERE` và số hàng chịu ảnh hưởng.

## 5. Oracle và SQL Server: transaction/auto-commit

> **KR:** ORACLE은 DML 시 사용자가 COMMIT 또는 ROLLBACK을 수행해야 하며, SQL Server는 기본적으로 AUTO COMMIT 모드이다.

Theo nội dung PDF, Oracle cần người dùng `COMMIT`/`ROLLBACK` để kết thúc transaction DML. SQL Server mặc định auto-commit (tự xác nhận từng lệnh); nếu muốn kiểm soát nhiều lệnh thành một transaction, phải mở transaction rõ ràng. PDF cũng lưu ý DDL của Oracle auto-commit (từ Oracle 23c có thể cấu hình khác) và SQL Server có thể cấu hình auto-commit.

## 6. ROLLBACK (Rollback) (hoàn tác)

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

## 7. SAVEPOINT (Savepoint) (điểm lưu tạm)

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
