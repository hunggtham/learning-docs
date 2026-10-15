# 193. 뷰 (View)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa của Khung nhìn (`뷰 / View`): Bảng ảo (`가상 테이블 / Virtual Table`) được định nghĩa dựa trên một hoặc nhiều bảng cơ sở (`기본 테이블`) thông qua câu lệnh truy vấn SELECT.
- Phân tích chi tiết 4 ưu điểm kỹ thuật của View: Cung cấp tính độc lập dữ liệu logic (`논리적 데이터 독립성`), Tự động bảo mật thông qua kiểm soát truy cập, Đơn giản hóa các câu lệnh truy vấn phức tạp, và Cho phép nhiều góc nhìn khác nhau trên cùng một tập dữ liệu.
- Nhớ rõ các hạn chế sống còn của View trong đề thi: Không có không gian lưu trữ vật lý độc lập, **Không thể tạo chỉ mục độc lập (인덱스 생성 불가)**, và Không thể dùng lệnh `ALTER VIEW` để thay đổi định nghĩa cấu trúc (phải DROP rồi CREATE lại).

## 핵심 키워드 (Từ khóa)
- 뷰 (Khung nhìn / View)
- 가상 테이블 (Bảng ảo / Virtual Table)
- 기본 테이블 (Bảng cơ sở / Base Table)
- 논리적 데이터 독립성 (Tính độc lập dữ liệu logic)
- 보안 제공 (Bảo mật dữ liệu)
- 인덱스 구성 불가 (Không thể tạo chỉ mục)
- CREATE VIEW / DROP VIEW

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([13-bai-hoc.md](13-bai-hoc.md), [28-bai-hoc.md](28-bai-hoc.md), [30-bai-hoc.md](30-bai-hoc.md)):** View chính là hình thức triển khai cụ thể nhất của Lược đồ ngoại (`외부 스키마`) trong kiến trúc 3 tầng ANSI/SPARC, được tạo dựng từ câu lệnh DDL `CREATE VIEW ... AS SELECT`.
- **Tiếp nối sang bài sau ([32-bai-hoc.md](32-bai-hoc.md)):** Để hiểu sâu hơn về View, bài học tiếp theo sẽ so sánh View tĩnh trong từ điển dữ liệu với Khung nhìn nội tuyến (`인라인 뷰 / Inline View`) sinh ra từ các câu truy vấn con (Subquery).

## 읽는 방법 (Cách đọc)
- Học thuộc bảng đặc trưng Ưu điểm và Nhược điểm ở TẦNG A:
  - Ưu điểm: Độc lập logic, bảo mật tốt, rút gọn câu lệnh.
  - Nhược điểm: **Không có Index riêng**, không sửa được cấu trúc (phải tạo lại), việc ghi dữ liệu (Insert/Update/Delete) bị hạn chế nghiêm ngặt.
- Ghi nhớ điều kiện để View có thể cập nhật được: **Bắt buộc phải chứa Khóa chính (`기본키`) của bảng cơ sở**.

---

## 193. 뷰 (View)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bản chất kỹ thuật của Khung nhìn (뷰의 개념):**
  - Là một **bảng ảo (`가상 테이블`)** có tên gọi, được hình thành từ kết quả truy vấn của một hay nhiều bảng cơ sở (`기본 테이블`).
  - **Không tồn tại về mặt vật lý trên ổ đĩa** (không chiếm dung lượng lưu trữ bản ghi), chỉ có câu lệnh định nghĩa View (`SELECT ...`) được lưu trong Hệ thống ca-ta-lô / Từ điển dữ liệu (`시스템 카탈로그`).
  - Người dùng thao tác với View bằng các câu lệnh `SELECT`, `INSERT`, `UPDATE`, `DELETE` tương tự như với một bảng thông thường.
- **2. Bảng phân tích Ưu điểm và Nhược điểm của View:**
  | Tiêu chí | Nội dung chi tiết cần nhớ | Ý nghĩa thực tế trong quản trị CSDL |
  |---|---|---|
  | **Ưu điểm** | - **Cung cấp tính độc lập dữ liệu logic (`논리적 데이터 독립성`):** Bảng cơ sở thêm cột mới thì ứng dụng đọc qua View không bị ảnh hưởng. ; - **Tự động bảo mật thông tin:** Giấu đi các cột nhạy cảm (như Lương, Mật khẩu, Số CCCD), chỉ hiển thị phần dữ liệu được phép cho từng nhóm người dùng. ; - **Đơn giản hóa câu lệnh truy vấn:** Đóng gói các phép JOIN nhiều bảng phức tạp thành một bảng ảo duy nhất. ; - Cho phép nhiều nhóm người dùng xem cùng một dữ liệu theo các góc nhìn khác nhau. | Giảm thiểu rủi ro lộ lọt dữ liệu và tăng năng suất lập trình. |
  | **Nhược điểm** | - **Không thể tạo chỉ mục độc lập (`독립적인 인덱스를 가질 수 없음`):** Không thể chạy `CREATE INDEX` trên View thông thường. ; - **Không thể sửa đổi định nghĩa cấu trúc của View:** Không có lệnh `ALTER VIEW` trong chuẩn; muốn sửa phải xóa bằng `DROP VIEW` rồi tạo mới bằng `CREATE VIEW`. ; - **Hạn chế thao tác cập nhật (Insert/Update/Delete):** View chứa phép JOIN, chứa hàm tập hợp (`SUM`, `AVG`), mệnh đề `GROUP BY`, hoặc `DISTINCT` thì **tuyệt đối không được phép INSERT/UPDATE/DELETE**. | View chủ yếu được tối ưu hóa cho mục đích xem và tra cứu dữ liệu (Read-only). |

- **3. Cú pháp quản lý View:**
  - Tạo View: `CREATE VIEW v_NhanVienIT AS SELECT MaNV, HoTen FROM NHAN_VIEN WHERE PhongBan = 'IT';`
  - Xóa View: `DROP VIEW v_NhanVienIT [CASCADE | RESTRICT];`
- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"View có thể tạo chỉ mục riêng (Index) không?"* $\rightarrow$ Đáp án: **KHÔNG THỂ (독립적인 인덱스를 가질 수 없다)**.
  - Đề hỏi: *"Làm thế nào để sửa định nghĩa của một View?"* $\rightarrow$ Đáp án: **Xóa bằng DROP VIEW rồi tạo lại bằng CREATE VIEW**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa tính năng bảo mật của View:**
  - Bảng cơ sở: `NHAN_VIEN (MaNV, HoTen, SoDienThoai, Luong, SoCCCD)`
  - Tạo View cho phòng hành chính:
    ```sql
    CREATE VIEW v_HanhChinh AS
    SELECT MaNV, HoTen, SoDienThoai
    FROM NHAN_VIEN;
    ```
  - Cấp quyền truy cập View này cho nhân viên hành chính: `GRANT SELECT ON v_HanhChinh TO nhanvien_hc;`
  - Kết quả: Nhân viên hành chính tra cứu được danh bạ nhưng hoàn toàn không thể biết được cột `Luong` và `SoCCCD`.

### 복습 체크리스트
- [ ] Định nghĩa chính xác 뷰 là 가상 테이블 (bảng ảo).
- [ ] Nêu 3 ưu điểm lớn của View: 논리적 독립성, 보안성, 쿼리 단순화.
- [ ] Khẳng định được View không thể tạo Index độc lập.
- [ ] Nắm được điều kiện hạn chế khi Insert/Update trên View.
