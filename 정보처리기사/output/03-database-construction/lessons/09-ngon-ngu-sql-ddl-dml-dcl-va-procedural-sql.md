# SQL 언어 체계와 절차형 SQL (Hệ Thống Ngôn Ngữ SQL và SQL Thủ Tục)

## 학습 목표 (Mục tiêu)
- Nắm vững vai trò, đối tượng thao tác và cú pháp chuẩn của 4 phân nhóm SQL: DDL (`데이터 정의어`), DML (`데이터 조작어`), DCL (`데이터 제어어`), và TCL (`트랜잭션 제어어`).
- Sử dụng thành thạo `CREATE`, `ALTER`, `DROP` (kèm tùy chọn `CASCADE` vs `RESTRICT`), phân biệt triệt để `DROP TABLE` vs `TRUNCATE TABLE` vs `DELETE FROM TABLE`.
- Nắm vững thứ tự thực thi câu lệnh `SELECT`, các hàm xếp hạng (`RANK`, `DENSE_RANK`, `ROW_NUMBER`), hàm mở rộng nhóm (`ROLLUP`, `CUBE`), toán tử tập hợp, và phép `JOIN` (kèm ký hiệu `(+)` của Oracle).
- Phân tích câu lệnh quản trị phân quyền `GRANT`, `REVOKE` (với `WITH GRANT OPTION`) và quản trị giao dịch `COMMIT`, `ROLLBACK`, `SAVEPOINT`.
- Phân biệt sâu sắc bản chất, cú pháp, biến giả `:OLD`/`:NEW` và điểm bẫy thi cử của 3 đối tượng SQL thủ tục: **저장 프로시저 (Stored Procedure)**, **트리거 (Trigger)**, và **사용자 정의 함수 (User-Defined Function)**.

## 핵심 키워드 (Từ khóa)
- SQL (Structured Query Language / 관계형 데이터베이스 표준 언어)
- DDL (CREATE, ALTER, DROP, TRUNCATE / Auto-commit)
- DML (SELECT, INSERT, UPDATE, DELETE / Rollback 가능)
- DCL & TCL (GRANT, REVOKE, COMMIT, ROLLBACK, SAVEPOINT)
- SELECT 실행 순서 (FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY)
- 순위 함수 (RANK, DENSE_RANK, ROW_NUMBER)
- 절차형 SQL (저장 프로시저 Stored Procedure, 트리거 Trigger, 사용자 정의 함수 User-Defined Function)
- 트리거 가상 변수 (:OLD, :NEW / TCL 사용 불가 함정)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [08-giao-dich-trang-thai-acid-va-dieu-khien-dong-thoi.md](08-giao-dich-trang-thai-acid-va-dieu-khien-dong-thoi.md), chúng ta đã nắm vững nền tảng lý thuyết về giao dịch ACID và các cơ chế kiểm soát đồng thời để bảo vệ tính nhất quán dữ liệu.
- **Đang giải quyết gì (Current Problem):** Bài học này giải quyết việc hiện thực hóa các lược đồ thiết kế vào hệ RDBMS thực tế, cung cấp toàn bộ cú pháp chuẩn mực của **Hệ thống ngôn ngữ SQL** (DDL, DML, DCL, TCL) và đóng gói logic xử lý hàng loạt bằng **SQL thủ tục (Procedural SQL)**.
- **Dùng đi đâu (Forward Handoff):** Các câu lệnh DDL và DML được xây dựng ở đây sẽ là công cụ trực tiếp để tạo Khung nhìn (View), xây dựng Chỉ mục (Index) và phân tích Từ điển dữ liệu hệ thống (System Catalog) ở bài học tiếp theo [10-view-index-system-catalog-va-ma-tran-crud.md](10-view-index-system-catalog-va-ma-tran-crud.md).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nắm trọn vẹn các bẫy đề thi kinh điển: thứ tự SELECT, đối chiếu 3 lệnh xóa bảng, bảng phân biệt 3 hàm RANK, câu thần chú DCL/TCL và đặc tính cấm TCL trong Trigger.
- Đọc TẦNG B để nắm chi tiết cú pháp DDL/DML nâng cao, các hàm tổng hợp ROLLUP/CUBE, mệnh đề WITH GRANT OPTION trong DCL và khối cấu trúc Procedural SQL kèm biến giả `:OLD`/`:NEW`.

---

## SQL 언어 체계와 절차형 SQL

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng phân loại 4 nhóm ngôn ngữ SQL

| Nhóm | Tên tiếng Hàn & Anh | Lệnh tiêu biểu | Đối tượng & Đặc tính then chốt |
| :--- | :--- | :--- | :--- |
| **DDL** | **데이터 정의어 (Data Definition Language)** | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` | Quản lý cấu trúc, bảng, lược đồ. **Tự động Commit (Auto-commit)**, không thể Rollback. |
| **DML** | **데이터 조작어 (Data Manipulation Language)** | `SELECT`, `INSERT`, `UPDATE`, `DELETE` | Thao tác trên từng bản ghi dữ liệu. **Có thể Rollback** trước khi Commit. |
| **DCL** | **데이터 제어어 (Data Control Language)** | `GRANT`, `REVOKE` | Phân quyền bảo mật, cấp và thu hồi quyền truy cập đối tượng. Khẩu quyết: **GR**. |
| **TCL** | **트랜잭션 제어어 (Transaction Control)** | `COMMIT`, `ROLLBACK`, `SAVEPOINT` | Quản lý kết quả giao dịch và thiết lập mốc hoàn tác. Khẩu quyết: **CRS**. |

#### 2. So sánh đối đầu 3 lệnh xóa: DROP vs TRUNCATE vs DELETE

| Tiêu chí | `DROP TABLE` | `TRUNCATE TABLE` | `DELETE FROM` |
| :--- | :---: | :---: | :---: |
| **Phân nhóm SQL** | **DDL** | **DDL** | **DML** |
| **Đối tượng xóa** | Bảng + Toàn bộ dữ liệu | Toàn bộ dữ liệu (giữ lại khung bảng) | Dòng được chỉ định hoặc toàn bộ dòng |
| **Khả năng Rollback** | **Không (Auto-commit)** | **Không (Auto-commit)** | **Có thể Rollback** |
| **Tốc độ thực thi** | Nhanh nhất | Cực nhanh (ghi log tối thiểu) | Chậm (ghi log từng dòng) |
| **Giải phóng ổ đĩa** | Trả lại vùng nhớ ngay lập tức | Trả lại vùng nhớ ngay lập tức | Giữ nguyên vùng nhớ đã cấp phát |

#### 3. Bảng đối chiếu 3 đối tượng SQL thủ tục (Procedural SQL)

| Tiêu chí so sánh | 저장 프로시저 (Stored Procedure) | 사용자 정의 함수 (User Function) | 트리거 (Trigger) |
| :--- | :--- | :--- | :--- |
| **Mục đích chính** | Đóng gói một chuỗi tác vụ nghiệp vụ phức tạp trên máy chủ. | Tính toán và trả về một giá trị duy nhất (hoặc bảng). | Tự động phản ứng ngầm theo sự kiện thay đổi dữ liệu DML. |
| **Cách kích hoạt** | Gọi tường minh bằng lệnh `EXECUTE` hoặc `CALL`. | Gọi lồng bên trong câu lệnh SQL (`SELECT func(col)...`). | **DBMS tự động kích hoạt** ngầm khi có INSERT/UPDATE/DELETE. |
| **Tham số** | Có thể có tham số `IN`, `OUT`, `INOUT`. | Chỉ nhận tham số đầu vào (`IN`). | **KHÔNG CÓ tham số đầu vào**. |
| **Giá trị trả về** | Không bắt buộc trả về, có thể trả qua tham số `OUT`. | **BẮT BUỘC phải có lệnh `RETURN`** trả về giá trị. | **TUYỆT ĐỐI KHÔNG có lệnh `RETURN`**. |
| **Sử dụng lệnh TCL** | Được phép dùng `COMMIT`, `ROLLBACK` (tùy cấu hình). | **CẤM** dùng `COMMIT`, `ROLLBACK`. | **TUYỆT ĐỐI CẤM dùng `COMMIT`, `ROLLBACK`**. |

#### 4. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)

- **Bẫy 1: Thứ tự thực thi của câu lệnh SELECT:**
  - Viết: `SELECT` $\rightarrow$ `FROM` $\rightarrow$ `WHERE` $\rightarrow$ `GROUP BY` $\rightarrow$ `HAVING` $\rightarrow$ `ORDER BY`.
  - Thực thi: **`FROM` $\rightarrow$ `WHERE` $\rightarrow$ `GROUP BY` $\rightarrow$ `HAVING` $\rightarrow$ `SELECT` $\rightarrow$ `ORDER BY`**.
  - Vì `WHERE` chạy trước `GROUP BY`, không được dùng hàm gộp nhóm (như `SUM`, `COUNT`) trong `WHERE` mà phải đặt trong `HAVING`.
- **Bẫy 2: Ký hiệu Oracle `(+)` trong phép JOIN:**
  - `WHERE A.id = B.id(+)`: Dấu `(+)` đặt ở bảng `B` thiếu dữ liệu $\rightarrow$ Bảng `A` là bảng chính $\rightarrow$ **LEFT OUTER JOIN**.
  - `WHERE A.id(+) = B.id`: Dấu `(+)` đặt ở bảng `A` thiếu dữ liệu $\rightarrow$ Bảng `B` là bảng chính $\rightarrow$ **RIGHT OUTER JOIN**.
- **Bẫy 3: Bẫy câu lệnh TCL trong Trigger:**
  - *Câu hỏi:* "Trong khối mã lệnh của Trigger, câu lệnh nào sau đây KHÔNG ĐƯỢC PHÉP sử dụng?"
  - *Đáp án đúng:* **`COMMIT` hoặc `ROLLBACK`**. Trigger chạy ngầm trong bối cảnh giao dịch của câu lệnh DML kích hoạt nó; nếu dùng TCL sẽ phá vỡ tính nguyên tử của giao dịch gốc.
- **Bẫy 4: Thứ tự ưu tiên toán tử trong SQL:**
  - Thần chú: **"산 - 관 - 논"** (Toán - Quan - Logic).
  - Ưu tiên: Toán học (`*, /, +, -`) $\rightarrow$ Quan hệ/So sánh (`=, <>, >, <`) $\rightarrow$ Logic (`NOT` trước, rồi `AND`, cuối cùng là `OR`).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Cú pháp DDL nâng cao

- **CREATE TABLE với ràng buộc toàn vẹn:**
  ```sql
  CREATE TABLE NHAN_VIEN (
      MaNV VARCHAR2(10) PRIMARY KEY,
      HoTen VARCHAR2(50) NOT NULL,
      Tuoi NUMBER(3) CHECK (Tuoi >= 18),
      MaPhong VARCHAR2(10),
      CONSTRAINT fk_phong FOREIGN KEY (MaPhong) REFERENCES PHONG_BAN(MaPhong)
      ON DELETE CASCADE
  );
  ```
- **ALTER TABLE:**
  - Thêm cột: `ALTER TABLE NHAN_VIEN ADD (Email VARCHAR2(100));`
  - Sửa kiểu cột: `ALTER TABLE NHAN_VIEN MODIFY (Email VARCHAR2(150) NOT NULL);`
  - Xóa cột: `ALTER TABLE NHAN_VIEN DROP COLUMN Email;`
- **CASCADE vs RESTRICT trong lệnh DROP:**
  - `CASCADE`: Xóa đối tượng cha đồng thời tự động xóa liên đới toàn bộ các đối tượng con đang tham chiếu tới nó.
  - `RESTRICT`: Nếu có bất kỳ đối tượng nào đang tham chiếu tới thì lập tức từ chối thao tác xóa và báo lỗi.

#### 2. Các hàm xếp hạng và nhóm mở rộng trong DML

- **Bảng phân biệt 3 hàm xếp hạng (순위 함수):**
  | Hàm | Quy tắc xử lý đồng hạng | Điểm [100, 90, 90, 80] |
  | :--- | :--- | :---: |
  | **`RANK()`** | Đồng hạng nhận cùng thứ nguyên, thứ hạng kế tiếp bị **nhảy cóc (Skip)** | **1, 2, 2, 4** |
  | **`DENSE_RANK()`** | Đồng hạng nhận cùng thứ nguyên, thứ hạng kế tiếp **không nhảy cóc** | **1, 2, 2, 3** |
  | **`ROW_NUMBER()`** | Bỏ qua đồng hạng, đánh số thứ tự dòng liên tục duy nhất | **1, 2, 3, 4** |

- **Hàm nhóm mở rộng (ROLLUP vs CUBE):**
  - `ROLLUP(A, B)`: Tạo tổng phụ theo cấp bậc từ phải sang trái: nhóm `(A, B)` $\rightarrow$ nhóm `(A)` $\rightarrow$ `Tổng toàn bộ`.
  - `CUBE(A, B)`: Tạo tổng phụ cho toàn bộ mọi tổ hợp ($2^n$): `(A, B)`, `(A)`, `(B)`, và `Tổng toàn bộ`.

#### 3. Quản trị phân quyền (DCL) và giao dịch (TCL)

- **DCL với WITH GRANT OPTION:**
  - `GRANT SELECT ON BANG TO USER_A WITH GRANT OPTION;`: Cấp quyền cho USER_A kèm quyền ủy quyền tiếp cho người khác.
  - `REVOKE SELECT ON BANG FROM USER_A CASCADE;`: Thu hồi quyền từ USER_A đồng thời thu hồi dây chuyền toàn bộ quyền mà USER_A đã cấp cho người khác.
- **TCL với SAVEPOINT:**
  - Cho phép đặt các mốc kiểm soát cục bộ bên trong một giao dịch dài: `SAVEPOINT sp1;`.
  - Có thể hoàn tác về mốc trung gian bằng lệnh `ROLLBACK TO sp1;` mà không làm hủy bỏ toàn bộ tiến trình.

#### 4. Đối tượng SQL thủ tục và Biến giả trong Trigger

- **Cấu trúc khối PL/SQL chuẩn:**
  ```sql
  DECLARE     -- 선언부: Khai báo biến, hằng, con trỏ (Cursor)
  BEGIN       -- 실행부: Khối lệnh thực thi, rẽ nhánh IF, vòng lặp LOOP
  EXCEPTION   -- 예외처리부: Xử lý ngoại lệ lỗi
  END;        -- 종료: Kết thúc khối
  ```
- **Biến giả trong Trigger (`:OLD` và `:NEW`):**
  - Trong trigger mức dòng (`FOR EACH ROW`), hệ thống cung cấp 2 biến giả đặc biệt:
    + `:OLD`: Đại diện cho bản ghi cũ trước khi bị thay đổi hoặc xóa.
    + `:NEW`: Đại diện cho bản ghi mới vừa được chèn vào hoặc sau khi cập nhật.
  - **Quy tắc xuất hiện trong các câu lệnh DML:**
    | Câu lệnh DML | Biến `:OLD` | Biến `:NEW` | Giải thích nghiệp vụ |
    | :--- | :---: | :---: | :--- |
    | **`INSERT`** | `NULL` | **Có giá trị** | Dòng mới được tạo, chưa từng có dữ liệu cũ. |
    | **`UPDATE`** | **Có giá trị** | **Có giá trị** | `:OLD` là giá trị trước sửa, `:NEW` là giá trị sau sửa. |
    | **`DELETE`** | **Có giá trị** | `NULL` | Dòng bị xóa khỏi bảng, không còn giá trị mới. |

---

### 복습 체크리스트
- [ ] Phân biệt rõ tính chất Commit/Rollback của 4 nhóm DDL, DML, DCL, TCL.
- [ ] Thuộc thần chú DCL: **GR** (Grant, Revoke) và TCL: **CRS** (Commit, Rollback, Savepoint).
- [ ] So sánh triệt để DROP TABLE (DDL), TRUNCATE TABLE (DDL), DELETE FROM TABLE (DML).
- [ ] Thuộc lòng thứ tự thực thi của câu lệnh SELECT: `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY`.
- [ ] Nhớ bảng đối chiếu 3 hàm xếp hạng: RANK (nhảy cóc), DENSE_RANK (liên tục), ROW_NUMBER (đánh số dòng liên tục).
- [ ] Phân biệt sự khác nhau giữa Stored Procedure, Stored Function và Trigger (cách gọi, tham số, câu lệnh RETURN, cấm lệnh TCL trong Trigger).
- [ ] Nắm vững quy tắc sử dụng biến giả `:OLD` và `:NEW` trong Trigger đối với INSERT, UPDATE, DELETE.
