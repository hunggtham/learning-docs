# 115. 무결성 (Integrity)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và tầm quan trọng của Tính toàn vẹn dữ liệu (`무결성 / Integrity`): Đảm bảo dữ liệu trong CSDL luôn chính xác, nhất quán và hợp lệ.
- Phân biệt chi tiết 6 loại ràng buộc toàn vẹn: Toàn vẹn thực thể (`개체 무결성`), Toàn vẹn tham chiếu (`참조 무결성`), Toàn vẹn miền giá trị (`도메인 무결성`), Toàn vẹn khóa (`키 무결성`), Toàn vẹn quan hệ (`관계 무결성`), và Toàn vẹn người dùng định nghĩa (`사용자 정의 무결성`).
- Nắm chắc các quy tắc xử lý khi vi phạm toàn vẹn tham chiếu trong thao tác Xóa/Cập nhật (`CASCADE`, `RESTRICT / NO ACTION`, `SET NULL`, `SET DEFAULT`).

## 핵심 키워드 (Từ khóa)
- 무결성 (Tính toàn vẹn / Integrity)
- 개체 무결성 (Toàn vẹn thực thể / Entity Integrity)
- 참조 무결성 (Toàn vẹn tham chiếu / Referential Integrity)
- 도메인 무결성 (Toàn vẹn miền giá trị / Domain Integrity)
- 키 무결성 (Toàn vẹn khóa / Key Integrity)
- 관계 무결성 (Toàn vẹn quan hệ / Relational Integrity)
- CASCADE (Xóa / Sửa lan truyền)
- RESTRICT (Chặn thao tác khi còn tham chiếu)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([11-bai-hoc.md](11-bai-hoc.md), [12-bai-hoc.md](12-bai-hoc.md), [14-bai-hoc.md](14-bai-hoc.md)):** Tính toàn vẹn không thể tách rời khỏi hệ thống Khóa (Khóa chính $\leftrightarrow$ Toàn vẹn thực thể; Khóa ngoại $\leftrightarrow$ Toàn vẹn tham chiếu).
- **Tiếp nối sang các bài sau ([16-bai-hoc.md](16-bai-hoc.md), [17-bai-hoc.md](17-bai-hoc.md)):** Để dữ liệu duy trì tính toàn vẹn ngay cả khi thực hiện thao tác đại số quan hệ và tránh dị thường (Anomaly), lược đồ cần phải trải qua quá trình Chuẩn hóa dữ liệu (`정규화`).

## 읽는 방법 (Cách đọc)
- Khắc ghi 2 quy tắc bất biến thường xuyên xuất hiện nhất trong đề thi:
  1. **개체 무결성:** Khóa chính cấm tuyệt đối `NULL` và cấm `trùng lặp`.
  2. **참조 무결성:** Khóa ngoại chỉ được phép là `NULL` hoặc bằng một khóa chính đang tồn tại.
- Học thuộc 3 phương thức xử lý khóa ngoại khi bảng cha bị xóa (`CASCADE`, `RESTRICT`, `SET NULL`).

---

## 115. 무결성 (Integrity)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bản chất của Tính toàn vẹn (무결성의 개념):**
  - Là sự chính xác, nhất quán và không mâu thuẫn của dữ liệu được lưu trữ trong cơ sở dữ liệu (`데이터의 정확성, 일관성, 유효성 유지`).
  - Hệ quản trị CSDL (DBMS) có trách nhiệm tự động kiểm tra và cưỡng chế các quy tắc này mỗi khi có lệnh Insert, Update, hoặc Delete.
- **2. Chi tiết 6 loại quy tắc toàn vẹn theo chuẩn đề thi:**
  | Loại Toàn vẹn | Thuật ngữ Hàn - Anh | Định nghĩa kỹ thuật | Điểm kiểm tra trắc nghiệm |
  |---|---|---|---|
  | **Toàn vẹn thực thể** | `개체 무결성` (Entity Integrity) | Thuộc tính khóa chính (`기본키`) không được nhận giá trị `NULL` và không được phép trùng lặp dữ liệu. | Đảm bảo mỗi hàng trong quan hệ luôn là một thực thể riêng biệt. |
  | **Toàn vẹn tham chiếu** | `참조 무결성` (Referential Integrity) | Giá trị của khóa ngoại (`외래키`) phải bằng giá trị khóa chính của bảng được tham chiếu, hoặc phải là `NULL`. | Ngăn ngừa việc trỏ đến một bản ghi không hề tồn tại. |
  | **Toàn vẹn miền giá trị** | `도메인 무결성` (Domain Integrity) | Giá trị của một thuộc tính bắt buộc phải nằm trong miền giá trị (`도메인`) đã được định nghĩa hợp lệ. | Kiểm tra kiểu dữ liệu, thang điểm (0-10), định dạng ngày tháng. |
  | **Toàn vẹn khóa** | `키 무결성` (Key Integrity) | Mỗi quan hệ (bảng) phải có ít nhất một khóa để phân biệt các bộ dữ liệu. | Đảm bảo tính duy nhất của quan hệ. |
  | **Toàn vẹn quan hệ** | `관계 무결성` (Relational Integrity) | Quy định tính hợp lệ của mối quan hệ giữa các bộ trong hai hay nhiều quan hệ khác nhau. | Đảm bảo cấu trúc liên kết logic giữa các thực thể. |
  | **Toàn vẹn người dùng** | `사용자 정의 무결성` (User-Defined Integrity) | Dữ liệu phải tuân thủ các điều kiện ràng buộc do người dùng hoặc quy trình nghiệp vụ đặt ra. | Cài đặt thông qua lệnh `CHECK`, `TRIGGER`, hoặc `ASSERTION`. |

- **3. Hành vi xử lý tham chiếu khi xóa / cập nhật ở bảng cha (외래키 참조 옵션):**
  - **CASCADE (Xóa/sửa lan truyền):** Khi một hàng ở bảng cha bị xóa/sửa, toàn bộ các hàng tương ứng ở bảng con đang tham chiếu đến cũng sẽ tự động bị xóa/sửa theo.
  - **RESTRICT / NO ACTION (Chặn thao tác):** Nếu còn bất kỳ hàng con nào đang tham chiếu đến hàng cha, DBMS sẽ lập tức từ chối và báo lỗi, không cho phép xóa/sửa hàng cha.
  - **SET NULL (Gán về rỗng):** Khi hàng cha bị xóa/sửa, giá trị khóa ngoại ở các hàng con sẽ được tự động đổi thành `NULL` (chỉ áp dụng nếu cột khóa ngoại cho phép NULL).
  - **SET DEFAULT (Gán về mặc định):** Khi hàng cha bị xóa/sửa, khóa ngoại ở bảng con được tự động gán về giá trị mặc định được định nghĩa trước.
- **주의/함정 (Bẫy đề thi cần nhớ):**
  - Đề hỏi: *"Nếu xóa bảng cha mà bảng con tự động xóa theo thì đó là hành vi gì?"* $\rightarrow$ Đáp án: **CASCADE**.
  - Đề hỏi: *"Nếu không cho phép xóa hàng cha khi vẫn còn dữ liệu tham chiếu thì đó là gì?"* $\rightarrow$ Đáp án: **RESTRICT**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa mã lệnh SQL thiết lập ràng buộc toàn vẹn:**
  ```sql
  CREATE TABLE DON_HANG (
      MaDH INT PRIMARY KEY,               -- 개체 무결성 (Toàn vẹn thực thể)
      MaKH INT,
      SoLuong INT CHECK (SoLuong > 0),    -- 도메인 / 사용자 정의 무결성
      FOREIGN KEY (MaKH) REFERENCES KHACH_HANG(MaKH)
          ON DELETE CASCADE               -- 참조 무결성 xử lý lan truyền
  );
  ```
- **So sánh Cơ chế kiểm tra Toàn vẹn:**
  - `CHECK`: Kiểm tra ngay trên từng thuộc tính của bảng khi ghi dữ liệu.
  - `TRIGGER`: Tự động kích hoạt khi có sự kiện Insert, Update, Delete để thi hành các logic ràng buộc phức tạp giữa nhiều bảng.
  - `ASSERTION`: Vị từ điều kiện cấp cơ sở dữ liệu kiểm tra tổng thể hệ thống.

### 복습 체크리스트
- [ ] Định nghĩa chuẩn xác 개체 무결성 (기본키 NULL 불가, 중복 불가).
- [ ] Định nghĩa chuẩn xác 참조 무결성 (외래키는 NULL이거나 참조 릴레이션의 기본키 값).
- [ ] Phân biệt rõ tác dụng của CASCADE và RESTRICT khi xóa dữ liệu.
- [ ] Nhớ tên các loại toàn vẹn: 개체, 참조, 도메인, 키, 관계, 사용자 정의 무결성.
