# 4. SQL 문법의 종류 (Các loại cú pháp SQL)

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp chi tiết và các tùy chọn bắt buộc của các lệnh DDL: `CREATE TABLE`, `ALTER TABLE`, và `DROP TABLE` (phân biệt hai chế độ `CASCADE` và `RESTRICT`).
- Hiểu rõ cú pháp 4 lệnh DML cốt lõi: `SELECT`, `INSERT`, `UPDATE`, và `DELETE`.
- Thành thạo cú pháp cấp quyền và thu hồi quyền trong DCL: `GRANT ... WITH GRANT OPTION` và `REVOKE ... CASCADE`.
- Nắm vững cú pháp điều khiển giao dịch TCL với điểm lưu an toàn: `SAVEPOINT` và `ROLLBACK TO SAVEPOINT`.

## 핵심 키워드 (Từ khóa)
- DDL (CREATE, ALTER, DROP, TRUNCATE)
- CASCADE (Xóa / Thu hồi lan truyền)
- RESTRICT (Chặn thao tác nếu còn tham chiếu)
- WITH GRANT OPTION (Cho phép cấp tiếp quyền cho người khác)
- DML (SELECT, INSERT, UPDATE, DELETE)
- DCL (GRANT, REVOKE)
- TCL (COMMIT, ROLLBACK, SAVEPOINT)
- 제약조건 (Ràng buộc: PRIMARY KEY, UNIQUE, FOREIGN KEY, CHECK, DEFAULT)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([15-bai-hoc.md](15-bai-hoc.md), [26-bai-hoc.md](26-bai-hoc.md)):** Sau khi nắm được sơ đồ phân loại tổng quan ở bài 26, bài học này cung cấp toàn bộ cú pháp thực thi để viết mã chuẩn xác trong các bài thi lý thuyết và thực hành.
- **Tiếp nối sang các bài sau ([29-bai-hoc.md](29-bai-hoc.md), [30-bai-hoc.md](30-bai-hoc.md)):** Thứ tự thực thi logic của các mệnh đề trong câu lệnh `SELECT` (WHERE, GROUP BY, HAVING, ORDER BY) sẽ được phân tích sâu ở cấp độ từng dòng dữ liệu.

## 읽는 방법 (Cách đọc)
- Học thuộc hai cặp từ khóa quan trọng nhất trong đề thi trắc nghiệm:
  - **CASCADE:** Xóa/sửa/thu hồi liên đới toàn bộ các đối tượng liên quan.
  - **RESTRICT:** Chặn lại, từ chối thực hiện nếu có đối tượng khác đang phụ thuộc.
- Nhớ câu lệnh phân quyền: `WITH GRANT OPTION` trao quyền cấp tiếp cho người khác; khi `REVOKE CASCADE`, quyền của những người được A cấp tiếp cũng bị thu hồi sạch.

---

## 4. SQL 문법의 종류 (Các loại cú pháp SQL)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Cú pháp chi tiết DDL (데이터 정의어):**
  - **CREATE TABLE (Tạo bảng):**
    ```sql
    CREATE TABLE HOC_VIEN (
        MaHV VARCHAR(10) PRIMARY KEY,
        HoTen VARCHAR(50) NOT NULL,
        Tuoi INT CHECK (Tuoi >= 18),
        MaLop VARCHAR(10),
        FOREIGN KEY (MaLop) REFERENCES LOP_HOC(MaLop)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
    ```
  - **ALTER TABLE (Sửa cấu trúc bảng):**
    - Thêm cột: `ALTER TABLE HOC_VIEN ADD Email VARCHAR(100);`
    - Sửa kiểu dữ liệu / giá trị mặc định: `ALTER TABLE HOC_VIEN ALTER COLUMN Tuoi SET DEFAULT 20;`
    - Xóa cột: `ALTER TABLE HOC_VIEN DROP COLUMN Email [CASCADE];`
  - **DROP TABLE (Xóa bảng):**
    - `DROP TABLE LOP_HOC CASCADE;` $\rightarrow$ Xóa bảng `LOP_HOC` đồng thời tự động xóa toàn bộ các bảng con, view, chỉ mục đang tham chiếu đến nó.
    - `DROP TABLE LOP_HOC RESTRICT;` $\rightarrow$ Nếu còn bảng con nào đang tham chiếu đến thì lệnh bị hủy bỏ ngay lập tức.
- **2. Cú pháp chi tiết DCL (데이터 제어어):**
  - **GRANT (Cấp quyền):**
    ```sql
    GRANT SELECT, INSERT ON HOC_VIEN TO user1 WITH GRANT OPTION;
    ```
    - `WITH GRANT OPTION`: Cho phép `user1` có quyền cấp tiếp quyền `SELECT, INSERT` cho người dùng khác (`user2`).
  - **REVOKE (Thu hồi quyền):**
    ```sql
    REVOKE SELECT ON HOC_VIEN FROM user1 CASCADE;
    ```
    - Tùy chọn `CASCADE`: Thu hồi quyền của `user1` kéo theo thu hồi luôn quyền của tất cả những người dùng mà `user1` đã từng cấp tiếp.
    - `GRANT OPTION FOR`: Chỉ thu hồi quyền chia sẻ quyền của `user1`, vẫn giữ lại quyền sử dụng của chính `user1`.
- **3. Cú pháp chi tiết TCL (트랜잭션 제어어):**
  - `COMMIT;`: Lưu vĩnh viễn toàn bộ các thay đổi vào CSDL.
  - `SAVEPOINT SP1;`: Đánh dấu điểm khôi phục trung gian `SP1`.
  - `ROLLBACK TO SP1;`: Hoàn tác dữ liệu quay trở lại đúng thời điểm đánh dấu `SP1`, các thao tác trước `SP1` vẫn được bảo toàn.
- **주의/함정 (Bẫy đề thi):**
  - Đề hỏi: *"Tùy chọn nào trong DROP TABLE làm xóa luôn cả các khung nhìn (View) phụ thuộc?"* $\rightarrow$ Đáp án: **CASCADE**.
  - Đề hỏi: *"Khi muốn quay lui một phần của giao dịch về mốc nhất định thì dùng cú pháp nào?"* $\rightarrow$ Đáp án: **ROLLBACK TO <tên_savepoint>**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa quy trình SAVEPOINT trong giao dịch:**
  ```sql
  INSERT INTO DON_HANG VALUES (1, 'SP_A');
  SAVEPOINT diem1;
  INSERT INTO DON_HANG VALUES (2, 'SP_B');
  SAVEPOINT diem2;
  INSERT INTO DON_HANG VALUES (3, 'SP_C');
  ROLLBACK TO diem1; -- Chỉ hủy dòng SP_B và SP_C; dòng SP_A vẫn tồn tại
  COMMIT;            -- Xác nhận dòng SP_A vào CSDL
  ```
- **So sánh quyền hạn quản trị (DBA) và quyền hạn đối tượng:**
  - Quyền hệ thống (System Privileges): `CREATE USER`, `CREATE TABLE`, `DROP ANY TABLE` (thường do DBA nắm giữ).
  - Quyền đối tượng (Object Privileges): `SELECT`, `INSERT`, `UPDATE`, `DELETE` trên một bảng cụ thể.

### 복습 체크리스트
- [ ] Viết đúng cấu trúc lệnh CREATE TABLE với PRIMARY KEY, FOREIGN KEY, CHECK.
- [ ] Phân biệt được sự khác nhau giữa CASCADE và RESTRICT trong lệnh DROP TABLE.
- [ ] Giải thích ý nghĩa của WITH GRANT OPTION trong lệnh GRANT.
- [ ] Nêu cách sử dụng SAVEPOINT và ROLLBACK TO trong điều khiển giao dịch.
