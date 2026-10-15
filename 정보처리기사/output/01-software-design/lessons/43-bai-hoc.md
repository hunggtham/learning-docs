# 6. SQL과 객체, 시스템 개념 (SQL, View, Catalog & Transaction)

## 학습 목표 (Mục tiêu)
- Phân loại chuẩn xác 3 nhóm câu lệnh SQL: Nhóm định nghĩa dữ liệu (`DDL`), Nhóm thao tác dữ liệu (`DML`), và Nhóm điều khiển dữ liệu (`DCL/TCL`).
- Nắm vững bản chất, ưu điểm và các hạn chế kỹ thuật của đối tượng Bảng ảo (`뷰 - View`) trong cơ sở dữ liệu quan hệ.
- Hiểu vai trò của Danh mục hệ thống (`시스템 카탈로그 - System Catalog`) và thuộc nằm lòng 4 đặc tính `ACID` của Giao dịch (`트랜잭션`).

## 핵심 키워드 (Từ khóa)
- DDL (CREATE, ALTER, DROP, TRUNCATE)
- DML (SELECT, INSERT, UPDATE, DELETE)
- DCL / TCL (GRANT, REVOKE, COMMIT, ROLLBACK)
- 뷰 (Bảng ảo / Virtual Table / 보안성, 독립성)
- 시스템 카탈로그 (System Catalog / 데이터 사전 / 메타데이터)
- 트랜잭션 4대 특성 (ACID: 원자성, 일관성, 고립성, 지속성)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([5. 관계 데이터 연산 및 정규화](42-bai-hoc.md)):** Sau khi xem xét đại số quan hệ và các mức chuẩn hóa, bài này hệ thống hóa các công cụ thao tác dữ liệu thực tế bằng SQL và cơ chế an toàn giao dịch.
- **Tiếp nối sang bài sau ([1. 회복 (Recovery)](44-bai-hoc.md)):** Khởi đầu cụm bài học chuyên sâu về cơ chế Phục hồi CSDL sau sự cố (Redo/Undo, Checkpoint).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nhớ bảng phân loại lệnh SQL (DDL, DML, DCL) và 4 thuộc tính ACID (Nguyên tử, Nhất quán, Cô lập, Bền vững) - đây là những điểm thi trọng tâm của cả Môn 1 và Môn 3.
- Đọc TẦNG B để hiểu rõ tại sao người dùng thông thường chỉ được phép đọc System Catalog bằng câu lệnh SELECT mà tuyệt đối không thể can thiệp bằng UPDATE/DELETE.

---

## 6. SQL과 객체, 시스템 개념 (SQL, View, Catalog & Transaction)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Phân loại 3 nhóm câu lệnh SQL chuẩn:**
  - **DDL (Data Definition Language - Ngôn ngữ định nghĩa dữ liệu):**
    - Thao tác trực tiếp trên cấu trúc của cơ sở dữ liệu và các đối tượng (Table, View, Index).
    - Các lệnh: `CREATE` (Tạo mới), `ALTER` (Sửa đổi cấu trúc), `DROP` (Xóa bỏ hoàn toàn đối tượng), `TRUNCATE` (Xóa sạch toàn bộ dữ liệu trong bảng nhưng giữ lại cấu trúc).
  - **DML (Data Manipulation Language - Ngôn ngữ thao tác dữ liệu):**
    - Thao tác trên các hàng dữ liệu (Tuples) chứa bên trong bảng.
    - Các lệnh: `SELECT` (Truy vấn dữ liệu), `INSERT` (Thêm hàng mới), `UPDATE` (Chỉnh sửa dữ liệu), `DELETE` (Xóa hàng).
  - **DCL (Data Control Language - Ngôn ngữ điều khiển dữ liệu / Bao gồm TCL):**
    - Quản lý quyền hạn truy cập bảo mật và điều khiển giao dịch.
    - Các lệnh: `GRANT` (Cấp quyền), `REVOKE` (Thu hồi quyền), `COMMIT` (Xác nhận lưu vĩnh viễn giao dịch), `ROLLBACK` (Hủy bỏ và khôi phục trạng thái ban đầu), `SAVEPOINT` (Điểm lưu trung gian).
- **2. Bảng ảo (뷰 - View):**
  - **Khái niệm:** Là một bảng ảo (`가상 테이블`) được định nghĩa dựa trên kết quả truy vấn của câu lệnh SELECT từ một hoặc nhiều bảng cơ sở (`기본 테이블 - Base Table`). View không thực sự lưu trữ dữ liệu vật lý trên đĩa cứng (ngoại trừ định nghĩa của nó trong System Catalog).
  - **Ưu điểm:**
    - Nâng cao tính bảo mật (`보안성`): Ẩn đi các cột nhạy cảm (như lương, mật khẩu), chỉ cấp quyền xem View cho người dùng.
    - Đơn giản hóa các câu truy vấn phức tạp có nhiều phép JOIN.
    - Đảm bảo tính độc lập dữ liệu logic (`논리적 데이터 독립성`).
  - **Hạn chế kỹ thuật thi trắc nghiệm:**
    - Không thể trực tiếp dùng câu lệnh `ALTER VIEW` để thay đổi định nghĩa các cột (bắt buộc phải `DROP VIEW` rồi `CREATE VIEW` lại).
    - Không thể tạo chỉ mục Index độc lập trên View thông thường.
    - Thao tác INSERT, UPDATE trên View có chứa hàm gộp (SUM, AVG) hay phép GROUP BY bị cấm hoàn toàn.
- **3. Danh mục hệ thống (시스템 카탈로그 - System Catalog / Data Dictionary):**
  - Là cơ sở dữ liệu đặc biệt do DBMS quản lý dùng để lưu trữ toàn bộ thông tin mô tả về cơ sở dữ liệu (**siêu dữ liệu - 메타데이터 / Metadata**).
  - **Quy tắc vận hành:** Người dùng chỉ có thể dùng lệnh `SELECT` để tra cứu thông tin trong Catalog; **tuyệt đối không thể dùng DML (`INSERT`, `UPDATE`, `DELETE`) để sửa đổi trực tiếp Catalog** vì DBMS sẽ tự động đồng bộ hóa nó khi có thay đổi DDL.
- **4. 4 đặc tính sống còn của Giao dịch (트랜잭션 ACID 특성):**
  - `원자성 (Atomicity - Tính nguyên tử)`: Giao dịch phải được thực hiện trọn vẹn hoặc không thực hiện gì cả (**All or Nothing**). Khi có lỗi, hệ thống phải tự động Rollback về trạng thái ban đầu.
  - `일관성 (Consistency - Tính nhất quán)`: Sau khi giao dịch hoàn tất thành công, cơ sở dữ liệu phải luôn ở trạng thái nhất quán, thỏa mãn toàn bộ các ràng buộc toàn vẹn.
  - `고립성 / 독립성 (Isolation - Tính cô lập)`: Các giao dịch chạy đồng thời không được phép can thiệp hoặc nhìn thấy dữ liệu trung gian chưa commit của nhau.
  - `지속성 / 영속성 (Durability - Tính bền vững)`: Dữ liệu của giao dịch một khi đã Commit thành công sẽ được ghi vĩnh viễn xuống đĩa cứng và không bị mất mát kể cả khi hệ thống bị mất điện đột ngột.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Lệnh TRUNCATE thuộc nhóm DML hay DDL?"* -> **DDL (Ngôn ngữ định nghĩa dữ liệu)** vì nó tự động commit và không thể rollback được như DELETE.
  - **Bẫy 2:** *"Có thể dùng lệnh UPDATE để sửa trực tiếp thông tin trong System Catalog không?"* -> **Tuyệt đối KHÔNG**. Chỉ được dùng SELECT để đọc.
  - **Bẫy 3:** *"Đặc tính nào đảm bảo giao dịch thực hiện theo nguyên tắc All or Nothing?"* -> **원자성 (Atomicity - Tính nguyên tử)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "SQL gồm DDL định nghĩa, DML thao tác, DCL phân quyền; View là bảng ảo bảo mật; Catalog lưu Metadata cấm sửa; Giao dịch chuẩn 4 chữ ACID: Nguyên tử, Nhất quán, Cô lập, Bền vững".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tình huống thực tế minh họa tính cô lập (Isolation):**
  - Nếu giao dịch A đang chuyển tiền từ tài khoản X sang Y (đã trừ tiền ở X nhưng chưa cộng vào Y): Giao dịch B của người dùng khác khi truy vấn số dư của X và Y sẽ không bao giờ được nhìn thấy trạng thái "tiền đang bay lơ lửng" này; B chỉ thấy dữ liệu trước khi A chạy, hoặc sau khi A đã Commit xong hoàn toàn. Cơ chế này được đảm bảo thông qua kỹ thuật khóa (Locking) hoặc MVCC.

### 복습 체크리스트
- [ ] Phân loại chính xác các lệnh vào nhóm DDL, DML, DCL/TCL.
- [ ] Định nghĩa View là bảng ảo và nhớ hạn chế không thể sửa định nghĩa cột trực tiếp bằng ALTER.
- [ ] Nắm được vai trò của System Catalog và quy tắc cấm sửa trực tiếp bằng DML.
- [ ] Thuộc nằm lòng 4 đặc tính ACID: 원자성 (Atomicity), 일관성 (Consistency), 고립성 (Isolation), 지속성 (Durability).
