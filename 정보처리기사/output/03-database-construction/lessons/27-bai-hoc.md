# 3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm của SQL thủ tục (`절차형 SQL / Procedural SQL`): Sự kết hợp giữa các câu lệnh SQL tiêu chuẩn với cấu trúc điều khiển logic (rẽ nhánh IF-ELSE, vòng lặp LOOP) tương tự các ngôn ngữ lập trình C/Java.
- Phân biệt chi tiết 3 đối tượng SQL thủ tục quan trọng: **Trigger (`트리거`)**, **Thủ tục lưu trữ (`프로시저 / Stored Procedure`)**, và **Hàm do người dùng định nghĩa (`사용자 정의 함수 / User-Defined Function`)**.
- Nhớ rõ sự khác nhau cốt lõi về cơ chế kích hoạt và giá trị trả về: Trigger chạy tự động theo sự kiện, Procedure gọi thực thi bằng lệnh CALL và trả về nhiều tham số OUT, Function bắt buộc trả về một giá trị duy nhất qua RETURN.

## 핵심 키워드 (Từ khóa)
- 절차형 SQL (SQL thủ tục / Procedural SQL)
- 트리거 (Trigger / Tự động kích hoạt)
- 프로시저 (Stored Procedure / Thủ tục lưu trữ)
- 사용자 정의 함수 (Hàm người dùng định nghĩa / User-Defined Function)
- 이벤트 (Sự kiện: INSERT, UPDATE, DELETE)
- RETURN 단일 값 (Trả về một giá trị đơn nhất)
- 매개변수 (Tham số: IN, OUT, INOUT)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([15-bai-hoc.md](15-bai-hoc.md), [26-bai-hoc.md](26-bai-hoc.md)):** Khi các ràng buộc toàn vẹn cơ bản (như CHECK, FOREIGN KEY) không đủ để biểu diễn các quy tắc nghiệp vụ phức tạp, người ta dùng Trigger và Procedure để cưỡng chế logic dữ liệu.
- **Tiếp nối sang các bài sau ([28-bai-hoc.md](28-bai-hoc.md), [29-bai-hoc.md](29-bai-hoc.md)):** Để xây dựng logic trong Procedure và Function, lập trình viên phối hợp nhuần nhuyễn các khối lệnh DML và cú pháp điều kiện lọc dữ liệu.

## 읽는 방법 (Cách đọc)
- Học thuộc bảng phân biệt 3 đối tượng ở TẦNG A:
  - **Trigger:** Tự động chạy khi có sự kiện (Insert/Update/Delete), không gọi thủ công.
  - **Procedure:** Chạy khi được gọi bằng lệnh `EXEC` / `CALL`, thực hiện chuỗi tác vụ lớn, có thể trả về nhiều kết quả qua biến `OUT`.
  - **User-Defined Function:** Luôn có lệnh `RETURN` trả về **1 giá trị đơn nhất**, được gọi trực tiếp trong câu lệnh `SELECT`.

---

## 3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Tổng quan SQL thủ tục (절차형 SQL 개요):**
  - Mở rộng SQL thông thường bằng các khối cấu trúc tuần tự, phân nhánh (`IF`, `CASE`) và lặp (`LOOP`, `WHILE`).
  - Được biên dịch và lưu trữ trực tiếp trên máy chủ cơ sở dữ liệu DBMS, giúp giảm lưu lượng truyền tải trên mạng giữa ứng dụng và máy chủ.
- **2. Bảng so sánh 3 đối tượng SQL thủ tục kinh điển:**
  | Tiêu chí | 트리거 (Trigger) | 프로시저 (Stored Procedure) | 사용자 정의 함수 (User-Defined Function) |
  |---|---|---|---|
  | **Cơ chế kích hoạt** | **Tự động thực thi** ngay khi phát sinh sự kiện (`INSERT`, `UPDATE`, `DELETE`) trên bảng | Được gọi tường minh bởi người dùng hoặc ứng dụng qua lệnh `CALL` hoặc `EXECUTE` | Được gọi lồng trực tiếp bên trong biểu thức của câu lệnh SQL (như `SELECT`, `WHERE`) |
  | **Giá trị trả về** | **Không có giá trị trả về** (Không có lệnh RETURN) | Trả về thông qua **nhiều tham số đầu ra (`OUT`, `INOUT`)**, hoặc không trả về | **Bắt buộc phải trả về DUY NHẤT 1 giá trị** thông qua mệnh đề `RETURN` |
  | **Lệnh giao dịch TCL** | **Không cho phép** dùng `COMMIT`, `ROLLBACK` bên trong (thuộc cùng transaction với sự kiện) | **Được phép** sử dụng các lệnh điều khiển giao dịch `COMMIT`, `ROLLBACK` | **Tuyệt đối cấm** lệnh làm biến đổi dữ liệu (DML) hoặc lệnh giao dịch (`COMMIT`, `ROLLBACK`) |
  | **Mục đích chính** | Ghi nhật ký kiểm toán (Audit Log), đồng bộ dữ liệu tự động, kiểm tra toàn vẹn nghiệp vụ | Đóng gói chuỗi quy trình nghiệp vụ phức tạp (ví dụ: Chốt sổ tính lương, Kết toán cuối tháng) | Tính toán công thức và trả về giá trị tái sử dụng (ví dụ: Tính tuổi từ ngày sinh, Quy đổi tiền tệ) |

- **3. Cấu trúc một khối SQL thủ tục (PL/SQL Block Structure):**
  - **DECLARE (Phần khai báo):** Khai báo tên biến, hằng số, kiểu dữ liệu và con trỏ (Cursor).
  - **BEGIN (Phần thân thực thi):** Bắt buộc phải có, chứa các câu lệnh logic và truy vấn SQL chính.
  - **EXCEPTION (Phần xử lý ngoại lệ):** Bắt và xử lý các lỗi phát sinh trong quá trình chạy.
  - **END (Phần kết thúc):** Đánh dấu kết thúc khối lệnh.
- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Đối tượng nào tự động chạy khi có sự kiện Insert, Update, Delete?"* $\rightarrow$ Đáp án: **트리거 (Trigger)**.
  - Đề hỏi: *"Khác biệt cốt lõi giữa Stored Procedure và User-Defined Function là gì?"* $\rightarrow$ **Function bắt buộc có RETURN trả về một giá trị duy nhất (단일 값 반환)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa ứng dụng thực tế của Trigger:**
  - Khi có sự kiện `DELETE` một tài khoản khách hàng khỏi bảng `KHACH_HANG`, Trigger `trg_LuuNhatKy` tự động ghi một dòng thông tin gồm `(MaKH, NgayXoa, NguoiThucHien)` vào bảng `NHAT_KY_XOA` nhằm phục vụ việc kiểm toán bảo mật.
- **Minh họa sự khác nhau khi gọi trong mã SQL:**
  - Gọi Procedure:
    ```sql
    CALL TinhThuongCuoiNam(2025, :TongThuong);
    ```
  - Gọi User-Defined Function:
    ```sql
    SELECT HoTen, TinhTuoi(NgaySinh) AS Tuoi FROM NHAN_VIEN;
    ```

### 복습 체크리스트
- [ ] Phân biệt rõ cách thức kích hoạt của Trigger (tự động) và Procedure (gọi lệnh).
- [ ] Khẳng định được đặc điểm của Function: bắt buộc RETURN 단일 값.
- [ ] Nhớ rõ 4 phần cấu trúc của khối SQL thủ tục: DECLARE, BEGIN, EXCEPTION, END.
- [ ] Nắm được lý do cấm COMMIT/ROLLBACK bên trong Trigger và Function.
