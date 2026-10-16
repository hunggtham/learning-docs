<!-- lecture-contract: v2 -->
# TCL và Transaction (Giao dịch)

> **Mục tiêu:** Nắm vững bản chất giao dịch, 4 thuộc tính ACID, cơ chế hoạt động của `COMMIT`, `ROLLBACK`, `SAVEPOINT` và sự khác biệt giữa Oracle và SQL Server trong đề thi SQLD.
>
> **Phạm vi tham khảo:** PDF *2024 개정판 SQLD 개념정리*, trang 87–89.
>
> **Mạch kiến thức:** Bài trước đã phân tích các thao tác biến đổi dữ liệu (DML). Bài này giải quyết câu hỏi: *Làm thế nào để các thay đổi đó được xác nhận vĩnh viễn hoặc khôi phục an toàn khi có sự cố?*

---

### 1. 트랜잭션 (Transaction) — Đơn vị công việc logic

> **KR:** 트랜잭션은 데이터베이스의 논리적 연산단위이며 분할할 수 없는 최소의 단위이다.

Giao dịch (Transaction) là một đơn vị công việc logic không thể phân chia (`All or Nothing`). Mọi thao tác bên trong một transaction hoặc phải cùng thành công trọn vẹn, hoặc phải cùng bị hủy bỏ hoàn toàn để đưa cơ sở dữ liệu về trạng thái ban đầu.
- **Tình huống nghiệp vụ kinh điển:** Chuyển tiền giữa hai tài khoản ngân hàng:
  1. Trừ tiền ở Tài khoản A (`UPDATE account SET balance = balance - 100 WHERE id = 'A'`).
  2. Cộng tiền ở Tài khoản B (`UPDATE account SET balance = balance + 100 WHERE id = 'B'`).
  Nếu bước 1 thành công nhưng bước 2 bị lỗi hệ thống, toàn bộ tiến trình bắt buộc phải được khôi phục lại trạng thái cũ (`ROLLBACK`).

---

### 2. 트랜잭션의 4대 특성 (ACID) — 4 thuộc tính cốt lõi của giao dịch

Để đảm bảo tính toàn vẹn và độ tin cậy của dữ liệu khi có nhiều người dùng đồng thời truy cập, mỗi giao dịch phải thỏa mãn 4 tiêu chí ACID:

| Thuộc tính (Korean / English) | Bản chất kỹ thuật & Tiêu chí nhận diện đề thi |
| --- | --- |
| **원자성 (Atomicity - Tính nguyên tử)** | Mọi thao tác trong giao dịch phải hoàn tất 100% hoặc không có thao tác nào được ghi nhận (`All or Nothing`). |
| **일관성 (Consistency - Tính nhất quán)** | Giao dịch phải đưa cơ sở dữ liệu từ trạng thái hợp lệ này sang trạng thái hợp lệ khác, không vi phạm bất kỳ ràng buộc (PK, FK, CHECK) nào. |
| **고립성 (Isolation - Tính cô lập)** | Các giao dịch chạy đồng thời không được can thiệp lẫn nhau. Trạng thái trung gian chưa commit của một giao dịch không được làm sai lệch kết quả giao dịch khác. |
| **지속성 (Durability - Tính bền vững)** | Một khi giao dịch đã `COMMIT` thành công, các thay đổi dữ liệu sẽ được lưu trữ vĩnh viễn trong CSDL ngay cả khi hệ thống gặp sự cố mất điện hay sập máy chủ. |

---

### 3. TCL (Transaction Control Language) — Ngôn ngữ điều khiển giao dịch

> **KR:** TCL은 COMMIT, ROLLBACK, SAVEPOINT를 포함하며 DML에 의해 조작된 결과를 작업단위(트랜잭션)별로 제어한다.

TCL không trực tiếp thay đổi nội dung bảng mà chịu trách nhiệm xác nhận hoặc hoàn tác các thay đổi do DML tạo ra:
- **`COMMIT` (Xác nhận lưu):** Đóng gói và ghi vĩnh viễn các thay đổi DML vào đĩa từ.
- **`ROLLBACK` (Hoàn tác):** Hủy bỏ các thao tác DML chưa commit, đưa dữ liệu về trạng thái commit gần nhất hoặc điểm lưu tạm.
- **`SAVEPOINT` (Điểm lưu tạm):** Đánh dấu các mốc trung gian bên trong giao dịch để có thể rollback cục bộ từng phần mà không hủy toàn bộ giao dịch.

---

### 4. COMMIT과 ROLLBACK의 동작 메커니즘 — Cơ chế thực thi

> **KR:** COMMIT 이전에는 메모리(버퍼)에만 임시 반영된 상태이며, ROLLBACK을 통해 언제든 취소할 수 있다. 하지만 COMMIT 이후에는 영구 저장되어 이전 상태로 되돌릴 수 없다.

- **Trạng thái trước khi `COMMIT`:**
  - Dữ liệu thay đổi chỉ mới nằm trong bộ nhớ đệm (Buffer Cache).
  - Người thực hiện truy vấn có thể nhìn thấy dữ liệu mới; các người dùng khác (`Session` khác) vẫn chỉ nhìn thấy dữ liệu cũ trước khi sửa.
  - Các hàng dữ liệu đang bị khóa (`Lock`) để ngăn phiên làm việc khác sửa đổi đồng thời.
- **Trạng thái sau khi `COMMIT`:**
  - Dữ liệu được ghi bền vững vào cơ sở dữ liệu.
  - Tất cả người dùng khác đều nhìn thấy kết quả mới nhất.
  - Các khóa tài nguyên (`Lock`) được giải phóng hoàn toàn.

---

### 5. DBMS 엔진별 트랜잭션 모드 차이 (Oracle vs SQL Server)

Đề thi SQLD thường xuyên kiểm tra sự khác biệt về chế độ giao dịch mặc định giữa Oracle và SQL Server:

| Tiêu chí đối chiếu | Oracle | SQL Server |
| --- | --- | --- |
| **Chế độ mặc định DML** | **Không auto-commit** (phải gõ lệnh `COMMIT` hoặc `ROLLBACK` rõ ràng). | **Mặc định AUTO-COMMIT** (mỗi câu lệnh DML tự động commit ngay lập tức). |
| **Mở giao dịch nhiều lệnh** | Tự động mở giao dịch khi gặp câu lệnh DML đầu tiên. | Bắt buộc phải khai báo tường minh: `BEGIN TRANSACTION;`. |
| **Lệnh DDL (`CREATE`, `ALTER`, `DROP`)** | **Tự động Auto-Commit** (ngay trước và sau câu lệnh DDL). | **Không auto-commit** (câu lệnh DDL có thể được rollback nếu nằm trong transaction). |

> **Cảnh báo bẫy đề thi:** Trong Oracle, nếu bạn thực hiện một loạt lệnh `INSERT`, sau đó chạy một lệnh `CREATE TABLE ...`, thì toàn bộ các lệnh `INSERT` trước đó **sẽ tự động bị commit vĩnh viễn** do lệnh DDL tự kích hoạt commit ngầm định!

---

### 6. SAVEPOINT와 부분 롤백 (Partial Rollback)

> **KR:** SAVEPOINT는 트랜잭션의 특정 지점에 이름을 지정하여, 해당 지점까지만 부분적으로 롤백할 수 있도록 지원한다.

Khi một giao dịch dài có nhiều bước phức tạp, `SAVEPOINT` cho phép khôi phục lại một bước cụ thể mà không làm mất công sức của các bước trước đó:

```sql
-- Cú pháp trong Oracle
INSERT INTO emp (empno, ename) VALUES (9001, 'KIM');
SAVEPOINT sp1;

UPDATE emp SET sal = 5000 WHERE empno = 9001;
SAVEPOINT sp2;

DELETE FROM emp WHERE empno = 9001;

-- Quay lui từng phần
ROLLBACK TO sp2;    -- Chỉ hủy lệnh DELETE; lệnh UPDATE và INSERT vẫn tồn tại
ROLLBACK TO sp1;    -- Hủy tiếp lệnh UPDATE; lệnh INSERT vẫn tồn tại
ROLLBACK;           -- Hủy toàn bộ giao dịch, kể cả lệnh INSERT đầu tiên
```

*Lưu ý đề thi:*
- Nếu đặt 2 `SAVEPOINT` trùng tên, điểm lưu tạm tạo sau sẽ ghi đè lên điểm tạo trước.
- Không thể `ROLLBACK TO SAVEPOINT` sau khi đã thực thi lệnh `COMMIT`.

---

## 7. Nối mạch sang Bài tiếp theo: DDL và định nghĩa bảng

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 09 đã hoàn thiện cơ chế kiểm soát giao dịch, tính toàn vẹn dữ liệu (ACID) và vòng đời của dữ liệu bản ghi khi thao tác DML.
> - **Đang giải quyết gì:** Để các bản ghi có thể tồn tại và chịu sự chi phối của các quy tắc toàn vẹn, trước tiên cấu trúc bảng, kiểu dữ liệu và dung lượng lưu trữ phải được định hình như thế nào trong cơ sở dữ liệu?
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 10 — DDL và định nghĩa bảng](./10-ddl-va-dinh-nghia-bang.md) để học cách kiến tạo và hiệu chỉnh cấu trúc bảng bằng các lệnh `CREATE TABLE`, `ALTER TABLE`, `DROP`, `TRUNCATE` và quy tắc tự động commit ngầm định.
