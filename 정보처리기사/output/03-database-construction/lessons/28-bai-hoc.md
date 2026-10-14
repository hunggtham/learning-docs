# 4. SQL 문법의 종류 (Các loại cú pháp SQL)

## 4. SQL 문법의 종류 (Các loại cú pháp SQL)
Phần “4. SQL 문법의 종류 (Các loại cú pháp SQL)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 종류 (Loại) | 명령어 (Lệnh) | 설명 & 역할 (Mô tả & Vai trò) | Giải thích (VN) |
|---|---|---|---|
| **DDL** (Data Definition Language) | CREATE, ALTER, DROP, TRUNCATE | 데이터베이스를 **정의**하는 언어, 구조 결정. (Ngôn ngữ định nghĩa dữ liệu - Cấu trúc). | Dùng để Tạo (CREATE), Sửa (ALTER), Xóa hoàn toàn (DROP), hoặc Xóa trắng (TRUNCATE) bảng. Giống như việc xây/đập một ngôi nhà. |
| **DML** (Data Manipulation Language) | SELECT, INSERT, UPDATE, DELETE | 저장된 자료를 조회, 삽입, 수정, 삭제. (Ngôn ngữ thao tác dữ liệu - Nội dung). | Dùng để Thêm, Sửa, Xóa, Lấy dữ liệu bên trong bảng. Giống như việc sắp xếp đồ đạc trong nhà. |
| **DCL** (Data Control Language) | GRANT, REVOKE | 데이터 보안과 권한 제어. (Ngôn ngữ điều khiển dữ liệu - Quyền). | Dùng để cấp quyền hoặc thu hồi quyền. |
| **TCL** (Transaction Control Language) | COMMIT, ROLLBACK, SAVEPOINT | 트랜잭션의 확정, 취소, 부분 복귀. (Ngôn ngữ điều khiển giao dịch). | Dùng để xác nhận, hoàn tác hoặc đặt điểm khôi phục giao dịch. |

> 💡 **Mẹo ghi nhớ:**
> DDL: **CADT** (Create, Alter, Drop, Truncate - "Cắt" cấu trúc).
> DML: **SUDI** (Select, Update, Delete, Insert - "Sửa đi" dữ liệu).
> DCL: **GR** (Grant, Revoke - "Gác quyền"). TCL: **CRS** (Commit, Rollback, Savepoint - "Chốt/Rút/Save").

---
