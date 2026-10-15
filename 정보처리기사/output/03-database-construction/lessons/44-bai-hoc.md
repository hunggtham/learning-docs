# 186. 시스템 카탈로그 (System Catalog)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa của Hệ thống ca-ta-lô (`시스템 카탈로그 / System Catalog`) hay Từ điển dữ liệu (`데이터 사전 / Data Dictionary`): Cơ sở dữ liệu hệ thống chuyên biệt lưu trữ Siêu dữ liệu (`메타데이터 / Metadata`) mô tả toàn bộ các đối tượng dữ liệu trong DBMS.
- Phân tích chi tiết 4 đặc trưng vận hành bắt buộc trong đề thi Kỹ sư xử lý thông tin Hàn Quốc: Bản thân ca-ta-lô cấu tạo từ các bảng hệ thống, DBMS tự động quản lý và cập nhật, Người dùng được phép tra cứu bằng `SELECT`, và Tuyệt đối cấm thao tác DML trực tiếp.
- Hiểu rõ sự khác biệt giữa Từ điển dữ liệu tĩnh và Bảng hiệu năng động (Dynamic Performance Views).

## 핵심 키워드 (Từ khóa)
- 시스템 카탈로그 (Hệ thống ca-ta-lô / System Catalog)
- 데이터 사전 (Từ điển dữ liệu / Data Dictionary)
- 메타데이터 (Siêu dữ liệu / Metadata: 데이터에 관한 데이터)
- 시스템 테이블 (Bảng hệ thống / System Tables)
- SELECT 조회 가능 (Cho phép tra cứu bằng SELECT)
- 갱신 불가 (Nghiêm cấm INSERT, UPDATE, DELETE trực tiếp)
- DBMS 자동 유지 (DBMS tự động duy trì)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([13-bai-hoc.md](13-bai-hoc.md), [25-bai-hoc.md](25-bai-hoc.md), [26-bai-hoc.md](26-bai-hoc.md)):** Bất kỳ khi nào người dùng chạy một câu lệnh DDL (`CREATE`, `ALTER`, `DROP`), DBMS sẽ tự động biên dịch và ghi lại định nghĩa cấu trúc mới vào Hệ thống ca-ta-lô.
- **Tiếp nối sang bài sau ([45-bai-hoc.md](45-bai-hoc.md)):** Để thực hiện phân tích ma trận CRUD (`CRUD 분석`), người kỹ sư trích xuất siêu dữ liệu về bảng và cột trực tiếp từ Hệ thống ca-ta-lô.

## 읽는 방법 (Cách đọc)
- Khắc sâu 3 đặc trưng cốt lõi thi trắc nghiệm ở TẦNG A:
  - Thông tin lưu trong Ca-ta-lô gọi là **메타데이터 (Metadata - Dữ liệu về dữ liệu)**.
  - Người dùng có được xem không? $\rightarrow$ **ĐƯỢC (tra cứu bằng lệnh SQL SELECT)**.
  - Người dùng có được sửa không? $\rightarrow$ **CẤM TUYỆT ĐỐI (không được INSERT/UPDATE/DELETE thủ công, do DBMS tự động cập nhật)**.

---

## 186. 시스템 카탈로그 (System Catalog)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Định nghĩa và Bản chất của Hệ thống ca-ta-lô (시스템 카탈로그의 개념):**
  - Là **cơ sở dữ liệu hệ thống (`시스템 데이터베이스`)** chứa toàn bộ các thông tin định nghĩa, đặc tả, quyền hạn và cấu trúc liên quan đến các đối tượng trong CSDL do DBMS hỗ trợ (như Table, View, Index, User, Schema, Constraint).
  - Thuật ngữ đồng nghĩa: Trong nghĩa hẹp, ca-ta-lô hệ thống còn được gọi là **Từ điển dữ liệu (`데이터 사전 / Data Dictionary`)**.
  - **Siêu dữ liệu (`메타데이터 / Metadata`):** Là thuật ngữ dùng để chỉ toàn bộ các dữ liệu mô tả cấu trúc được lưu trữ bên trong ca-ta-lô ("Dữ liệu mô tả về dữ liệu").
- **2. Bốn đặc trưng vận hành cốt lõi (카탈로그의 4대 특징):**
  | Đặc trưng | Nội dung kỹ thuật chính xác | Quy tắc đề thi trắc nghiệm |
  |---|---|---|
  | **Cấu trúc lưu trữ** | Bản thân ca-ta-lô cũng được tổ chức dưới dạng **các bảng hệ thống thông thường (`시스템 테이블`)**. | Giúp hệ thống có thể dùng chính bộ máy SQL nội bộ để quản lý ca-ta-lô. |
  | **Quyền truy cập tra cứu** | Người dùng thông thường và DBA **đều có thể sử dụng câu lệnh SQL `SELECT` để tìm kiếm và xem nội dung** ca-ta-lô. | Người dùng được quyền đọc thông tin cấu trúc (Read-only). |
  | **Quyền cập nhật / chỉnh sửa** | **TUYỆT ĐỐI CẤM** người dùng sử dụng các câu lệnh DML (`INSERT`, `UPDATE`, `DELETE`) để can thiệp hoặc sửa đổi trực tiếp vào các bảng ca-ta-lô. | Nếu người dùng sửa tay sẽ làm hỏng toàn bộ tính toàn vẹn của DBMS. |
  | **Cơ chế duy trì** | Ca-ta-lô được **DBMS tự động tạo lập, cập nhật và duy trì hoàn toàn** mỗi khi có sự kiện DDL phát sinh. | Người dùng chạy lệnh `CREATE TABLE` thì DBMS tự động thêm dòng mới vào ca-ta-lô. |

- **3. Cấu trúc nội dung được lưu trữ trong Ca-ta-lô:**
  - Định nghĩa các bảng, cột, kiểu dữ liệu, độ dài và giá trị mặc định.
  - Định nghĩa các chỉ mục (Index) và phương thức truy xuất vật lý.
  - Các quy tắc ràng buộc toàn vẹn (Khóa chính, Khóa ngoại, CHECK, UNIQUE).
  - Danh mục người dùng, mật khẩu đã băm (hash), và ma trận phân quyền truy cập (Grant/Revoke).
  - Số liệu thống kê phục vụ Bộ tối ưu hóa truy vấn CBO (số dòng, số trang dữ liệu).
- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Người dùng có thể sửa đổi ca-ta-lô hệ thống bằng lệnh INSERT được không?"* $\rightarrow$ Đáp án: **KHÔNG ĐƯỢC PHÉP (갱신은 허용되지 않음)**.
  - Đề hỏi: *"Dữ liệu được lưu trữ trong hệ thống ca-ta-lô được gọi là gì?"* $\rightarrow$ Đáp án: **메타데이터 (Metadata)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa truy vấn Từ điển dữ liệu trong thực tế:**
  - Trong Oracle Database:
    ```sql
    -- Xem danh sách tất cả các bảng thuộc quyền sở hữu của người dùng hiện tại
    SELECT table_name, num_rows FROM USER_TABLES;

    -- Xem chi tiết các cột của bảng SINH_VIEN
    SELECT column_name, data_type, data_length FROM USER_TAB_COLUMNS WHERE table_name = 'SINH_VIEN';
    ```
  - Trong MySQL / PostgreSQL:
    ```sql
    SELECT * FROM information_schema.tables WHERE table_schema = 'public';
    ```
  - Các lệnh `SELECT` trên hoàn toàn hợp lệ, nhưng nếu chạy `DELETE FROM USER_TABLES ...` hệ thống sẽ chặn đứng ngay lập tức với thông báo lỗi bảo mật hệ thống.

### 복습 체크리스트
- [ ] Định nghĩa chính xác 시스템 카탈로그 và 메타데이터.
- [ ] Nắm vững 4 đặc trưng: cấu trúc bảng, xem bằng SELECT, cấm sửa bằng DML, DBMS tự động cập nhật.
- [ ] Phân biệt được sự khác nhau giữa dữ liệu người dùng và siêu dữ liệu trong từ điển.
- [ ] Kể tên các đối tượng được ghi nhận trong ca-ta-lô (Table, View, Index, User, Constraint).
