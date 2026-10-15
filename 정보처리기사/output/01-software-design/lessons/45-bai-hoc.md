# 2. Commit & Rollback 연산

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và tác động kỹ thuật của các câu lệnh điều khiển giao dịch (`TCL - Transaction Control Language`): `COMMIT`, `ROLLBACK`, và `SAVEPOINT`.
- Hiểu rõ ranh giới bất biến của thao tác `COMMIT`: một khi đã hoàn tất thì dữ liệu trở thành vĩnh viễn và không thể đảo ngược bằng thao tác `ROLLBACK`.
- Nắm vững cú pháp và cơ chế phục hồi từng phần linh hoạt của `SAVEPOINT` trong các giao dịch phức tạp nhiều bước.

## 핵심 키워드 (Từ khóa)
- TCL (Transaction Control Language / 트랜잭션 제어어)
- COMMIT (Xác nhận hoàn tất giao dịch / 영구 반영)
- ROLLBACK (Hủy bỏ giao dịch / 원상 복구)
- SAVEPOINT (Điểm lưu tạm / 부분 롤백)
- 트랜잭션 경계 (Ranh giới giao dịch / Transaction Boundary)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([1. 회복 (Recovery)](44-bai-hoc.md)):** Sau khi xem xét cơ chế phục hồi REDO/UNDO của hệ thống, bài này tìm hiểu hai câu lệnh cụ thể mà người lập trình viên trực tiếp sử dụng để ra lệnh Commit hoặc Rollback.
- **Tiếp nối sang bài sau ([3. 트랜잭션의 상태 (Transaction States)](46-bai-hoc.md)):** Khảo sát 5 trạng thái vòng đời của một giao dịch từ khi kích hoạt đến khi hoàn tất hoặc bị hủy.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nhớ tính chất một chiều của Commit: Commit rồi là đóng giao dịch vĩnh viễn, không thể Rollback; Savepoint cho phép chia nhỏ giao dịch để cứu vãn các bước làm đúng.
- Đọc TẦNG B để theo dõi đoạn code mẫu SQL minh họa cú pháp Rollback từng phần về Savepoint.

---

## 2. Commit & Rollback 연산

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. COMMIT 연산 (Thao tác Xác nhận hoàn tất):**
  - **Khái niệm:** Báo hiệu rằng một giao dịch đã thực thi thành công toàn bộ các câu lệnh một cách trọn vẹn và không phát sinh bất kỳ lỗi nào (`트랜잭션이 성공적으로 종료`).
  - **Tác động:** Tất cả các thao tác sửa đổi, thêm, xóa dữ liệu trong bộ đệm (Buffer) được chính thức ghi nhận và lưu vĩnh viễn xuống cơ sở dữ liệu trên đĩa cứng (`데이터베이스에 영구적으로 반영`).
  - **Tính chất sống còn:** **Một khi lệnh COMMIT đã được thực thi thành công, giao dịch đó kết thúc hoàn toàn và TUYỆT ĐỐI KHÔNG THỂ DÙNG LỆNH ROLLBACK ĐỂ HỦY BỎ ĐƯỢC NỮA**.
- **2. ROLLBACK 연산 (Thao tác Hủy bỏ và Quay lui):**
  - **Khái niệm:** Báo hiệu rằng một giao dịch đã gặp sự cố hoặc bị hủy bỏ giữa chừng không thể hoàn thành trọn vẹn (`트랜잭션이 비정상적으로 종료`).
  - **Tác động:** Hủy bỏ toàn bộ các thay đổi dữ liệu mà giao dịch đó vừa thực hiện, khôi phục trạng thái cơ sở dữ liệu quay trở về chính xác thời điểm trước khi giao dịch bắt đầu chạy (`트랜잭션 시작 이전의 정상 상태로 복구`).
- **3. SAVEPOINT 연산 (Điểm lưu tạm trung gian):**
  - **Khái niệm:** Cho phép lập trình viên tạo ra các mốc đánh dấu lưu tạm (`저장점`) bên trong một giao dịch dài gồm nhiều bước.
  - **Cơ chế phục hồi từng phần:** Khi xảy ra lỗi ở các bước sau, lập trình viên có thể ra lệnh `ROLLBACK TO <tên_savepoint>` để chỉ hủy bỏ các câu lệnh từ sau mốc Savepoint đó, **giữ nguyên toàn bộ kết quả của các bước xử lý hợp lệ đã làm trước mốc Savepoint**.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Sau khi thực hiện câu lệnh COMMIT, lập trình viên có thể dùng lệnh ROLLBACK để đưa CSDL về trạng thái trước khi COMMIT?"* -> **Sai hoàn toàn**. Commit rồi thì không thể Rollback được nữa.
  - **Bẫy 2:** *"Lệnh nào cho phép hủy bỏ một phần giao dịch thay vì hủy bỏ toàn bộ?"* -> **SAVEPOINT (ROLLBACK TO SAVEPOINT)**.
  - **Bẫy 3:** *"Các câu lệnh DDL như CREATE, DROP, ALTER có thể dùng ROLLBACK để hủy bỏ được không?"* -> **Không thể (trong hầu hết DBMS như Oracle)** vì các lệnh DDL có cơ chế Auto-Commit tự động.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Commit là xác nhận lưu vĩnh viễn cấm quay đầu; Rollback là hủy sạch về xuất phát điểm; Savepoint lưu mốc để quay lui từng phần".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa mã nguồn SQL sử dụng Savepoint:**
  ```sql
  BEGIN TRANSACTION;
  INSERT INTO Customers VALUES ('C01', 'Alice');
  SAVEPOINT sp1; -- Đặt mốc lưu tạm sp1

  INSERT INTO Customers VALUES ('C02', 'Bob');
  SAVEPOINT sp2; -- Đặt mốc lưu tạm sp2

  INSERT INTO Customers VALUES ('C03', 'Charlie'); -- Dòng này bị lỗi nghiệp vụ!

  ROLLBACK TO sp1; -- Quay lui về mốc sp1: hủy bỏ Bob và Charlie, GIỮ LẠI Alice!

  COMMIT; -- Chính thức lưu lại Alice vào CSDL
  ```

### 복습 체크리스트
- [ ] Định nghĩa được tác động của câu lệnh COMMIT (lưu vĩnh viễn, kết thúc giao dịch).
- [ ] Khẳng định được sau khi COMMIT thì không thể dùng ROLLBACK để hủy.
- [ ] Giải thích được vai trò của SAVEPOINT trong việc phục hồi từng phần của giao dịch.
- [ ] Nhớ lệnh DDL tự động commit nên không thể rollback thông thường.
