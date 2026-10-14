# 6. SQL과 객체, 시스템 개념 (SQL, View, Catalog & Transaction)

## 6. SQL과 객체, 시스템 개념 (SQL, View, Catalog & Transaction)

### SQL의 3가지 분류 (Phân loại câu lệnh SQL)
Phần “SQL의 3가지 분류 (Phân loại câu lệnh SQL)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **DDL (데이터 정의어):** `CREATE`, `ALTER`, `DROP`.
- **DML (데이터 조작어):** `SELECT`, `INSERT`, `DELETE`, `UPDATE`.
- **DCL (데이터 제어어):** `COMMIT` (Lưu vĩnh viễn), `ROLLBACK` (Hoàn tác), `GRANT` (Cấp quyền), `REVOKE` (Thu hồi quyền).

### SELECT 명령어 구조 (Cấu trúc lệnh SELECT)
Phần “SELECT 명령어 구조 (Cấu trúc lệnh SELECT)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `SELECT` [DISTINCT] 속성명 `FROM` 테이블명 `WHERE` 조건 `GROUP BY` 속성 `HAVING` 그룹조건 `ORDER BY` 속성 [ASC|DESC]
- 그룹 함수: COUNT (Số lượng), MAX (Lớn nhất), MIN (Nhỏ nhất), SUM (Tổng), AVG (Trung bình).

### 삽입 / 삭제 / 갱신 문법 (Cú pháp Thêm, Xóa, Sửa)
Phần “삽입 / 삭제 / 갱신 문법 (Cú pháp Thêm, Xóa, Sửa)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **INSERT:** `INSERT INTO` 테이블명(속성) `VALUES` (데이터);
- **DELETE:** `DELETE FROM` 테이블명 `WHERE` 조건; (Lưu ý: DROP là xóa bảng, DELETE là xóa dòng).
- **UPDATE:** `UPDATE` 테이블명 `SET` 속성=데이터 `WHERE` 조건;

### 뷰 (View)의 특징 (Đặc điểm của View)
Phần “뷰 (View)의 특징 (Đặc điểm của View)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 기본 테이블에서 유도된 가상 테이블 (Bảng ảo). 물리적으로 존재하지 않음.
- 필요한 데이터만 보여줘서 자동 보안 제공.
- 뷰의 정의를 `ALTER`로 변경할 수 없으며 (삭제 후 다시 생성해야 함), 인덱스를 가질 수 없음. (Không thể sửa định nghĩa, không có index).
- 생성: `CREATE VIEW`, 삭제: `DROP VIEW 뷰이름 CASCADE` (xóa tất cả liên quan) / `RESTRICT` (nếu đang bị dùng thì cấm xóa).

### 내장 SQL과 시스템 카탈로그 (Embedded SQL & System Catalog)
Phần “내장 SQL과 시스템 카탈로그 (Embedded SQL & System Catalog)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **내장 SQL (Embedded SQL):** 응용 프로그램 코드 내에 삽입된 SQL. 수행 결과로 단 하나의 튜플만 반환됨. (SQL nhúng trong code như Java/C, chỉ trả về 1 dòng 1 lúc).
- **시스템 카탈로그 (System Catalog = Data Dictionary):** 스키마, 권한 등 메타 데이터(Meta-Data)를 저장하는 시스템 DB. (Từ điển dữ liệu chứa thông tin cấu trúc DB).
- 시스템이 자동으로 갱신하며, 사용자는 SELECT로 검색할 수 있지만 갱신(UPDATE/INSERT)은 불가. (Chỉ được xem, không được tự ý sửa).

### 트랜잭션(Transaction)의 정의와 4가지 특성 (Định nghĩa & 4 Đặc tính ACID)
Phần “트랜잭션(Transaction)의 정의와 4가지 특성 (Định nghĩa & 4 Đặc tính ACID)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 데이터베이스 상태를 변환시키는 하나의 논리적 단위 (복구 및 병행 수행의 단위). (Đơn vị công việc logic, ví dụ: 1 giao dịch chuyển tiền).
- **Atomicity (원자성):** 모두 반영되거나 아예 반영되지 않아야 함 (All or Nothing). (Thành công toàn bộ hoặc không có gì).
- **Consistency (일관성):** 트랜잭션 성공 완료 후 항상 일관성 있는 상태 유지. (Kết thúc giao dịch dữ liệu phải đúng đắn, không vi phạm ràng buộc).
- **Isolation (독립성, 격리성):** 실행 중에 다른 트랜잭션이 끼어들 수 없음. (Giao dịch đang chạy thì giao dịch khác không được can thiệp vào giữa chừng).
- **Durability (영속성, 지속성):** 완료된 결과는 영구적으로 반영되어야 함. (Giao dịch xong thì kết quả phải lưu vĩnh viễn dù cúp điện).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **ACID** (Atomicity, Consistency, Isolation, Durability) hoặc **NNĐT** (Nguyên - Nhất - Độc - Trì): **Người Ngoan Đáng Thương**.

# 정보처리기사 - Subject 1 Part 2
