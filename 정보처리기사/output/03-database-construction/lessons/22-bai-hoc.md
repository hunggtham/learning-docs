# 130-132. 트랜잭션 (Transaction)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa nền tảng của Giao dịch (`트랜잭션 / Transaction`): Đơn vị thao tác logic cơ bản (`논리적 작업의 단위`) dùng để biến đổi trạng thái của cơ sở dữ liệu.
- Hiểu sâu và giải thích thành thạo 4 đặc tính sống còn **ACID**: **Tính nguyên tử (Atomicity - `원자성`)**, **Tính nhất quán (Consistency - `일관성`)**, **Tính cô lập (Isolation - `독립성 / 격리성`)**, và **Tính bền vững (Durability - `영속성`)**.
- Nhận thức rõ vai trò của giao dịch trong việc kiểm soát truy cập đồng thời (`병행 제어`) và phục hồi sau sự cố (`회복 작업`).

## 핵심 키워드 (Từ khóa)
- 트랜잭션 (Giao dịch / Transaction)
- 논리적 작업 단위 (Đơn vị thao tác logic / Logical Unit of Work)
- ACID 특성 (Bộ 4 đặc tính ACID)
- Atomicity (Tính nguyên tử / 원자성 / All or Nothing)
- Consistency (Tính nhất quán / 일관성)
- Isolation (Tính cô lập, độc lập / 격리성 / 독립성)
- Durability (Tính bền vững / 영속성)
- Commit (Xác nhận hoàn tất) / Rollback (Hủy bỏ và hoàn tác)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([15-bai-hoc.md](15-bai-hoc.md), [21-bai-hoc.md](21-bai-hoc.md)):** Để bảo vệ tính toàn vẹn dữ liệu khi hệ thống xử lý đồng thời hàng nghìn câu truy vấn, DBMS bắt buộc phải đóng gói các câu lệnh thành các Giao dịch độc lập.
- **Tiếp nối sang các bài sau ([23-bai-hoc.md](23-bai-hoc.md), [24-bai-hoc.md](24-bai-hoc.md), [25-bai-hoc.md](25-bai-hoc.md)):** Để thực thi trọn vẹn đặc tính ACID, hệ thống phải quản trị vòng đời trạng thái của giao dịch (Active, Failed, Committed) và áp dụng các kỹ thuật khóa (`Locking`) kiểm soát đồng thời.

## 읽는 방법 (Cách đọc)
- Học thuộc 4 chữ cái vàng **ACID** tương ứng với 4 khái niệm tiếng Hàn:
  - **A $\rightarrow$ 원자성 (All or Nothing: hoặc xong hết `Commit`, hoặc không làm gì `Rollback`).**
  - **C $\rightarrow$ 일관성 (Trạng thái trước và sau giao dịch luôn hợp lệ và nhất quán).**
  - **I $\rightarrow$ 독립성 / 격리성 (Các giao dịch chạy song song không được can thiệp vào nhau).**
  - **D $\rightarrow$ 영속성 (Đã Commit thành công thì mất điện hay hỏng hóc dữ liệu vẫn tồn tại vĩnh viễn).**

---

## 130-132. 트랜잭션 (Transaction)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Định nghĩa và Vai trò của Giao dịch (트랜잭션의 정의):**
  - Là **đơn vị thao tác logic (`논리적 작업의 단위`)** bao gồm một chuỗi các câu lệnh SQL nhằm thực hiện một nghiệp vụ hoàn chỉnh làm biến đổi trạng thái của CSDL.
  - Là đơn vị cơ sở để hệ quản trị CSDL thực thi hai chức năng trọng yếu: **Kiểm soát đồng thời (`병행 제어`)** và **Phục hồi dữ liệu (`회복 작업`)**.
- **2. Bảng phân tích chi tiết 4 đặc tính ACID (ACID 4대 특성):**
  | Đặc tính ACID | Tên tiếng Hàn & Anh | Nội dung kỹ thuật bắt buộc | Cơ chế bảo đảm trong DBMS |
  |---|---|---|---|
  | **Tính nguyên tử** | `원자성` (Atomicity) | **"All or Nothing"** (Tất cả hoặc không có gì). Tất cả các câu lệnh trong giao dịch phải được thực hiện hoàn tất (`Commit`), nếu có bất kỳ lỗi nào xảy ra thì toàn bộ các thay đổi phải bị hủy bỏ hoàn toàn (`Rollback`). | Hệ thống ghi nhật ký (`Log / Journal`) và cơ chế Undo khi Rollback. |
  | **Tính nhất quán** | `일관성` (Consistency) | Khi giao dịch thực thi thành công, cơ sở dữ liệu luôn chuyển từ một trạng thái nhất quán này sang một trạng thái nhất quán khác, không vi phạm bất kỳ ràng buộc toàn vẹn nào. | Bộ kiểm tra ràng buộc toàn vẹn (Integrity Constraints Engine). |
  | **Tính cô lập** | `독립성 / 격리성` (Isolation) | Khi nhiều giao dịch cùng chạy đồng thời, không giao dịch nào được phép can thiệp vào giữa quá trình của giao dịch khác. Kết quả tạm thời của một giao dịch đang chạy không được để giao dịch khác nhìn thấy. | Cơ chế kiểm soát đồng thời (`병행 제어`) và các cấp độ khóa (`Locking / Isolation Levels`). |
  | **Tính bền vững** | `영속성` (Durability) | Một khi giao dịch đã thực hiện thành công (`Commit`), mọi kết quả biến đổi sẽ được lưu trữ vĩnh viễn trong CSDL, ngay cả khi hệ thống gặp sự cố sập nguồn hoặc hư hại phần cứng. | Cơ chế Redo log, Checkpoint và ghi xuống thiết bị lưu trữ thứ cấp phi bốc hơi. |

- **3. Quy tắc cốt lõi thi trắc nghiệm:**
  - Nếu câu hỏi nhắc đến: *"Tất cả phản ánh thành công hoặc không phản ánh gì (All or Nothing)"* $\rightarrow$ Đáp án: **원자성 (Atomicity)**.
  - Nếu câu hỏi nhắc đến: *"Đã hoàn thành thì dù mất điện kết quả vẫn được bảo toàn"* $\rightarrow$ Đáp án: **영속성 (Durability)**.
  - Nếu câu hỏi nhắc đến: *"Các giao dịch đồng thời không được nhìn thấy dữ liệu trung gian của nhau"* $\rightarrow$ Đáp án: **격리성 / 독립성 (Isolation)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ví dụ kinh điển về giao dịch chuyển khoản ngân hàng:**
  - Giao dịch chuyển 100 USD từ tài khoản A sang tài khoản B gồm 2 thao tác:
    1. Trừ 100 USD từ tài khoản A (`UPDATE TAI_KHOAN SET SoDu = SoDu - 100 WHERE ID = 'A'`).
    2. Cộng 100 USD vào tài khoản B (`UPDATE TAI_KHOAN SET SoDu = SoDu + 100 WHERE ID = 'B'`).
  - **Minh họa ACID:**
    - **원자성 (Atomicity):** Nếu bước 1 thành công nhưng bước 2 bị mất kết nối mạng, hệ thống bắt buộc phải `ROLLBACK` bước 1 để tài khoản A không bị mất tiền oan.
    - **일관성 (Consistency):** Tổng số dư của A + B trước và sau khi chuyển khoản luôn phải được bảo toàn không đổi.
    - **격리성 (Isolation):** Trong khi giao dịch chuyển khoản đang thực hiện giữa chừng, giao dịch xem sao kê của tài khoản A hoặc B không thể nhìn thấy số dư nửa vời.
    - **영속성 (Durability):** Ngay sau khi ngân hàng thông báo "Chuyển khoản thành công" (`COMMIT`), máy chủ có bị cháy nguồn thì dữ liệu số dư mới vẫn nguyên vẹn.

### 복습 체크리스트
- [ ] Định nghĩa chuẩn xác 트랜잭션 là 논리적 작업의 단위.
- [ ] Thuộc tên và giải thích 4 đặc tính ACID: 원자성, 일관성, 독립성/격리성, 영속성.
- [ ] Nắm được cơ chế All or Nothing thuộc về 원자성 (Atomicity).
- [ ] Phân biệt được nhiệm vụ của lệnh Commit (xác nhận) và Rollback (hủy bỏ).
