<!-- lecture-contract: v2 -->
# TCL và Transaction (Giao dịch)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **TCL và Transaction**. Route đi từ DML mutations → ACID properties → COMMIT/ROLLBACK mechanism → Nested SAVEPOINT trace → DDL implicit auto-commit, đảm bảo tính toàn vẹn và khả năng kiểm soát dữ liệu.

> **Mục tiêu:** Nắm vững bản chất giao dịch, 4 thuộc tính ACID, cơ chế hoạt động của `COMMIT`, `ROLLBACK`, kịch bản `SAVEPOINT` lồng nhau kèm bảng trace trạng thái dữ liệu, và bẫy Auto-commit ngầm định của lệnh DDL trong Oracle.

> **Phạm vi tham khảo:** PDF *2024 개정판 SQLD 개념정리*, trang 87–89.

---

### 1. 트랜잭션 (Transaction) — Đơn vị công việc logic

> **KR:** 트랜잭션은 데이터베이스의 논리적 연산단위이며 분할할 수 없는 최소의 단위이다.

Giao dịch (Transaction) là một đơn vị công việc logic không thể phân chia (`All or Nothing`). Mọi thao tác bên trong một transaction hoặc phải cùng thành công trọn vẹn, hoặc phải cùng bị hủy bỏ hoàn toàn để đưa cơ sở dữ liệu về trạng thái hợp lệ ban đầu.
- **Tình huống nghiệp vụ kinh điển:** Chuyển tiền giữa hai tài khoản ngân hàng:
  1. Trừ tiền ở Tài khoản A (`UPDATE account SET balance = balance - 100 WHERE id = 'A'`).
  2. Cộng tiền ở Tài khoản B (`UPDATE account SET balance = balance + 100 WHERE id = 'B'`).
  Nếu bước 1 thành công nhưng bước 2 bị lỗi hệ thống, toàn bộ tiến trình bắt buộc phải được khôi phục lại trạng thái cũ (`ROLLBACK`).

---

### 2. 트랜잭션의 4대 특성 (ACID) — 4 thuộc tính cốt lõi của giao dịch

Để đảm bảo tính toàn vẹn và độ tin cậy của dữ liệu khi có nhiều người dùng đồng thời truy cập, mỗi giao dịch phải thỏa mãn 4 tiêu chí ACID:

| Thuộc tính (Korean / English) | Bản chất kỹ thuật | Tiêu chí nhận diện đề thi |
| --- | --- | --- |
| **원자성 (Atomicity - Tính nguyên tử)** | Toàn bộ thao tác hoàn tất 100% hoặc không có thao tác nào được lưu. | Nguyên lý `All or Nothing`. Hủy bỏ bằng `ROLLBACK`. |
| **일관성 (Consistency - Tính nhất quán)** | Đưa CSDL từ trạng thái hợp lệ này sang trạng thái hợp lệ khác. | Không vi phạm ràng buộc toàn vẹn (PK, FK, CHECK). |
| **고립성 (Isolation - Tính cô lập)** | Các giao dịch đồng thời không can thiệp lẫn nhau. | Dữ liệu chưa commit của giao dịch này ẩn với giao dịch khác. |
| **지속성 (Durability - Tính bền vững)** | Giao dịch đã `COMMIT` sẽ được lưu vĩnh viễn trên đĩa từ. | Dữ liệu không mất ngay cả khi mất điện hay sập máy chủ. |

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

#### Trạng thái trước khi `COMMIT`
- Dữ liệu thay đổi chỉ mới nằm trong bộ nhớ đệm (Database Buffer Cache) và ghi nhật ký Redo Log Buffer.
- Người thực hiện truy vấn (`Current Session`) có thể nhìn thấy dữ liệu mới; các người dùng khác (`Other Sessions`) vẫn chỉ nhìn thấy dữ liệu cũ trước khi sửa (nhờ cơ chế Read Consistency thông qua Undo Segment).
- Các hàng dữ liệu đang bị khóa (`Row-Level Lock`) để ngăn phiên làm việc khác sửa đổi đồng thời.

#### Trạng thái sau khi `COMMIT`
- Dữ liệu được ghi bền vững vào cơ sở dữ liệu qua tiến trình nền (LGWR/DBWn).
- Tất cả người dùng khác đều nhìn thấy kết quả mới nhất.
- Các khóa tài nguyên (`Locks`) được giải phóng hoàn toàn, phiên khác có thể truy cập cập nhật.

---

### 5. DBMS 엔진별 트랜잭션 모드 và Bẫy DDL ngầm định Auto-commit

Đề thi SQLD thường xuyên kiểm tra sự khác biệt về chế độ giao dịch mặc định giữa Oracle và SQL Server:

| Tiêu chí đối chiếu | Oracle | SQL Server |
| --- | --- | --- |
| **Chế độ mặc định DML** | **Không auto-commit** (phải phát lệnh `COMMIT` hoặc `ROLLBACK` rõ ràng). | **Mặc định AUTO-COMMIT** (mỗi câu lệnh DML tự động commit ngay). |
| **Mở giao dịch nhiều lệnh** | Tự động mở khi gặp câu lệnh DML đầu tiên. | Bắt buộc khai báo tường minh: `BEGIN TRANSACTION;`. |
| **Lệnh DDL (`CREATE`, `ALTER`, `DROP`)** | **Tự động kích hoạt ngầm định Auto-Commit**. | **Không auto-commit** (có thể rollback nếu nằm trong transaction). |

#### Bẫy đề thi: Chạy DDL giữa giao dịch DML trong Oracle

Trong Oracle Database, cơ chế thực thi của một câu lệnh DDL diễn ra theo 3 nhịp:
1. Phát sinh một lệnh `COMMIT` ngầm định (Implicit Commit) trước khi DDL chạy.
2. Thực thi câu lệnh DDL và cập nhật Từ điển dữ liệu (Data Dictionary).
3. Phát sinh thêm một lệnh `COMMIT` ngầm định sau khi DDL chạy xong.

> **Hệ quả sống còn:** Nếu bạn đang thực hiện một chuỗi thao tác DML (`INSERT`, `UPDATE`, `DELETE`) chưa commit, rồi bất ngờ chạy một câu lệnh DDL (như `CREATE TABLE temp_tbl ...`, `ALTER TABLE ...`, hoặc `TRUNCATE TABLE ...`), thì:
> - Toàn bộ các thao tác DML trước đó **sẽ tự động bị COMMIT vĩnh viễn** vào cơ sở dữ liệu!
> - Tất cả các điểm lưu tạm `SAVEPOINT` đã khai báo trước đó **sẽ bị hủy bỏ hoàn toàn**!
> - Thao tác `ROLLBACK` sau đó hoàn toàn vô hiệu, không thể cứu lại trạng thái dữ liệu cũ!

---

### 6. SAVEPOINT와 부분 롤백 (Partial Rollback) & Kịch bản lồng nhau

> **KR:** SAVEPOINT는 트랜잭션의 특정 지점에 이름을 지정하여, 해당 지점까지만 부분적으로 롤백할 수 있도록 지원한다. 복수의 SAVEPOINT를 지정할 수 있으며 동일 이름 사용 시 나중에 생성된 지점이 유효하다.

Khi giao dịch gồm nhiều nghiệp vụ con tuần tự, `SAVEPOINT` cho phép quay lui cục bộ về một mốc xác định mà không làm mất công sức của các bước trước đó.

#### Hai quy tắc cốt lõi của SAVEPOINT trong đề thi
1. **Trùng tên Savepoint (Name Overwriting):** Nếu khai báo 2 `SAVEPOINT` có cùng tên trong cùng một transaction, điểm lưu tạm tạo sau sẽ **ghi đè và thay thế** hoàn toàn điểm lưu tạm tạo trước.
2. **Hủy điểm lưu tạm phía sau khi Rollback (Savepoint Invalidation):** Khi thực hiện `ROLLBACK TO SAVEPOINT A`, toàn bộ các thay đổi sau mốc A bị hủy bỏ, đồng thời **mọi Savepoint được tạo sau mốc A (ví dụ B, C) cũng tự động bị xóa sổ**. Nếu sau đó cố tình gọi `ROLLBACK TO SAVEPOINT B`, hệ thống sẽ báo lỗi do điểm lưu đó không còn tồn tại.

#### Bảng Trace kịch bản SAVEPOINT tuần tự (SQLD Classic Case)

Giả sử ban đầu bảng `PLAYER` có **480 bản ghi**, và không có cầu thủ nào nặng 100kg (`SELECT COUNT(*) FROM player WHERE weight = 100` trả về **0**).

```sql
-- Bước 1: Thêm cầu thủ mới (Tổng: 481 cầu thủ)
INSERT INTO player (player_id, team_id, player_name, weight)
VALUES ('135', 'K02', 'Lee', 82);

-- Bước 2: Đánh dấu mốc A
SAVEPOINT svpt_a;

-- Bước 3: Cập nhật cân nặng toàn bộ cầu thủ lên 100kg
UPDATE player
SET weight = 100;

-- Bước 4: Đánh dấu mốc B
SAVEPOINT svpt_b;

-- Bước 5: Xóa sạch toàn bộ cầu thủ trong bảng
DELETE FROM player;
```

Bảng theo dõi trạng thái dữ liệu và các Savepoint hiệu lực qua từng kịch bản Rollback:

| Kịch bản thực thi | Tổng số cầu thủ trong phiên | Số cầu thủ có weight = 100 | Trạng thái các Savepoint còn tồn tại |
| --- | --- | --- | --- |
| **Sau Bước 5** (Vừa DELETE) | 0 hàng (Bảng rỗng) | 0 hàng | `svpt_a`, `svpt_b` đang hoạt động |
| **Case 1:** `ROLLBACK TO svpt_b;` | 481 hàng | 481 hàng | `svpt_a`, `svpt_b` tiếp tục hoạt động |
| **Case 2:** Tiếp tục `ROLLBACK TO svpt_a;` | 481 hàng | 0 hàng (Trở về cân nặng cũ) | Chỉ còn `svpt_a` (`svpt_b` đã bị hủy) |
| **Case 3:** Tiếp tục `ROLLBACK;` | 480 hàng (Hủy cả lệnh INSERT) | 0 hàng | Toàn bộ Savepoint bị xóa sạch |

> **Phân tích kết quả:**
> - Tại **Case 1**, lệnh `DELETE` bị hủy, bảng khôi phục lại 481 người đều có cân nặng 100kg.
> - Tại **Case 2**, tiếp tục lùi về `svpt_a`, lệnh `UPDATE` bị hủy bỏ, cầu thủ 'Lee' vẫn còn nhưng cân nặng của toàn đội quay về nguyên trạng ban đầu. Lúc này, mốc `svpt_b` đã bị hủy bỏ vĩnh viễn khỏi transaction!
> - Tại **Case 3**, lệnh `ROLLBACK` trần đưa toàn bộ CSDL về mốc `COMMIT` gần nhất trước khi transaction bắt đầu (tổng 480 người, cầu thủ 'Lee' bị loại bỏ).

---

## 7. Nối mạch sang Bài tiếp theo: DDL và định nghĩa bảng

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 09 đã giải quyết trọn vẹn cơ chế kiểm soát giao dịch, 4 thuộc tính ACID, kịch bản `SAVEPOINT` và bẫy Auto-commit ngầm định của lệnh DDL.
> - **Đang giải quyết gì:** Để các bản ghi có thể tồn tại và chịu sự chi phối của các quy tắc toàn vẹn, trước tiên cấu trúc bảng, kiểu dữ liệu và dung lượng lưu trữ phải được định hình như thế nào trong cơ sở dữ liệu?
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 10 — DDL và định nghĩa bảng](./10-ddl-va-dinh-nghia-bang.md) để học cách kiến tạo và hiệu chỉnh cấu trúc bảng bằng `CREATE TABLE`, kỹ thuật nhân bản `CTAS`, các thao tác `ALTER TABLE`, và so sánh cơ chế giải phóng High Water Mark (HWM) giữa `TRUNCATE`, `DROP`, `DELETE`.
