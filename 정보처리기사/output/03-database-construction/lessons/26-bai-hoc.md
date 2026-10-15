# 143-145. SQL 분류 (SQL Categories)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và vai trò của Ngôn ngữ truy vấn có cấu trúc (`SQL / Structured Query Language`): Tiêu chuẩn quốc tế để giao tiếp và thao tác với cơ sở dữ liệu quan hệ.
- Phân biệt chính xác 4 phân nhóm lệnh SQL chính theo chuẩn đề thi Kỹ sư xử lý thông tin Hàn Quốc: **DDL (`데이터 정의어`)**, **DML (`데이터 조작어`)**, **DCL (`데이터 제어어`)**, và **TCL (`트랜잭션 제어어`)**.
- Nhớ rõ đối tượng sử dụng chính của từng nhóm lệnh: Quản trị viên CSDL (DBA), Người dùng/Lập trình viên ứng dụng (User/Developer).

## 핵심 키워드 (Từ khóa)
- SQL 분류 (Phân loại SQL / SQL Categories)
- DDL (데이터 정의어 / Data Definition Language)
- DML (데이터 조작어 / Data Manipulation Language)
- DCL (데이터 제어어 / Data Control Language)
- TCL (트랜잭션 제어어 / Transaction Control Language)
- CREATE / ALTER / DROP
- SELECT / INSERT / UPDATE / DELETE
- GRANT / REVOKE
- COMMIT / ROLLBACK / SAVEPOINT

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([13-bai-hoc.md](13-bai-hoc.md), [15-bai-hoc.md](15-bai-hoc.md), [25-bai-hoc.md](25-bai-hoc.md)):** Để hiện thực hóa các tầng Schema, ràng buộc toàn vẹn và cơ chế kiểm soát đồng thời trên máy tính, người kỹ sư bắt buộc phải dùng các câu lệnh SQL tương ứng.
- **Tiếp nối sang các bài sau ([27-bai-hoc.md](27-bai-hoc.md), [28-bai-hoc.md](28-bai-hoc.md), [30-bai-hoc.md](30-bai-hoc.md)):** Khung phân loại 4 nhóm này là tiền đề trực tiếp để học cú pháp chi tiết của DDL (CREATE TABLE), DML (SELECT, UPDATE) và các cấu trúc SQL thủ tục (Trigger, Procedure).

## 읽는 방법 (Cách đọc)
- Học thuộc bảng ma trận 4 nhóm lệnh ở TẦNG A:
  - **DDL:** Định nghĩa cấu trúc khung xương $\rightarrow$ `CREATE`, `ALTER`, `DROP`, `TRUNCATE`.
  - **DML:** Thao tác ruột dữ liệu $\rightarrow$ `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
  - **DCL:** Bảo mật và quyền hạn $\rightarrow$ `GRANT`, `REVOKE`.
  - **TCL:** Quản lý giao dịch $\rightarrow$ `COMMIT`, `ROLLBACK`, `SAVEPOINT`.

---

## 143-145. SQL 분류 (SQL Categories)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Tổng quan về SQL (SQL의 개요):**
  - Là ngôn ngữ chuẩn tương tác với hệ quản trị CSDL quan hệ (RDBMS), kết hợp các tính chất của cả Đại số quan hệ (Relational Algebra) và Giải tích quan hệ (Relational Calculus).
  - Có tính phi thủ tục cao trong các truy vấn dữ liệu nhưng có thể mở rộng thành ngôn ngữ thủ tục (Procedural SQL) trong các khối lệnh nâng cao.
- **2. Bảng phân loại 4 nhóm lệnh SQL chuẩn thi cử:**
  | Nhóm ngôn ngữ | Tên tiếng Hàn & Anh | Các lệnh chính | Đối tượng thao tác & Mục đích |
  |---|---|---|---|
  | **DDL** | `데이터 정의어` (Data Definition Language) | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` | Thao tác trên **Cấu trúc / Khung xương** của CSDL (Schema, Domain, Table, View, Index). Do DBA hoặc kiến trúc sư CSDL sử dụng. |
  | **DML** | `데이터 조작어` (Data Manipulation Language) | `SELECT`, `INSERT`, `UPDATE`, `DELETE` | Thao tác trên **Bản ghi / Dữ liệu thực tế** bên trong các bảng. Do người dùng cuối hoặc lập trình viên ứng dụng sử dụng. |
  | **DCL** | `데이터 제어어` (Data Control Language) | `GRANT`, `REVOKE` | Thao tác trên **Bảo mật và Quyền hạn** (Cấp quyền, thu hồi quyền truy cập đối tượng dữ liệu). Do DBA quản trị. |
  | **TCL** | `트랜잭션 제어어` (Transaction Control Language) | `COMMIT`, `ROLLBACK`, `SAVEPOINT` | Thao tác trên **Giao dịch** (Xác nhận ghi vĩnh viễn, hoàn tác trạng thái, thiết lập điểm cứu lưu tạm). |

- **3. Mẹo ghi nhớ nhận diện nhanh lệnh thi trắc nghiệm:**
  - DDL: **CADT** (Create - Alter - Drop - Truncate: Xây, sửa, đập, dọn nhà).
  - DML: **SUDI** (Select - Update - Delete - Insert: Tìm, sửa, xóa, thêm đồ đạc).
  - DCL: **GR** (Grant - Revoke: Ban phát quyền - Thu hồi quyền).
  - TCL: **CRS** (Commit - Rollback - Savepoint: Chốt hạ - Hoàn tác - Lưu chốt điểm).
- **주의/함정 (Bẫy đề thi hay gặp):**
  - Đề hỏi: *"Lệnh DROP thuộc nhóm ngôn ngữ nào?"* $\rightarrow$ Đáp án: **DDL (데이터 정의어)**.
  - Đề hỏi: *"Lệnh GRANT và REVOKE thuộc nhóm nào?"* $\rightarrow$ Đáp án: **DCL (데이터 제어어)**.
  - Đề hỏi: *"Lệnh nào dùng để xác nhận kết thúc giao dịch thành công và lưu vĩnh viễn xuống đĩa?"* $\rightarrow$ Đáp án: **COMMIT (thuộc TCL/DCL)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Sự khác biệt căn bản giữa DDL và DML:**
  - Lệnh DDL (`CREATE`, `DROP`, `ALTER`, `TRUNCATE`) một khi đã thực thi thì hệ thống sẽ **tự động COMMIT ngay lập tức (Auto-commit)**, không thể dùng lệnh `ROLLBACK` để hủy bỏ.
  - Lệnh DML (`INSERT`, `UPDATE`, `DELETE`) sau khi chạy thì dữ liệu chỉ mới được biến đổi trong phiên làm việc hiện tại (Transaction buffer); người dùng vẫn có thể dùng `ROLLBACK` để khôi phục lại dữ liệu ban đầu trước khi gõ `COMMIT`.
- **Phân biệt DROP TABLE vs TRUNCATE TABLE vs DELETE FROM TABLE:**
  - `DROP TABLE`: Xóa sạch cả dữ liệu và định nghĩa cấu trúc bảng khỏi Schema (DDL).
  - `TRUNCATE TABLE`: Xóa toàn bộ dữ liệu cực nhanh, giải phóng bộ nhớ, giữ lại cấu trúc bảng rỗng (DDL - Không thể Rollback).
  - `DELETE FROM TABLE`: Xóa dữ liệu từng dòng một có ghi log, giữ lại cấu trúc bảng (DML - Có thể Rollback).

### 복습 체크리스트
- [ ] Phân loại chính xác 4 nhóm: DDL, DML, DCL, TCL.
- [ ] Kể tên đúng các lệnh thuộc DDL (CREATE, ALTER, DROP, TRUNCATE).
- [ ] Kể tên đúng các lệnh thuộc DML (SELECT, INSERT, UPDATE, DELETE).
- [ ] Nêu được điểm khác nhau về tính năng Rollback giữa DDL và DML.
