# 20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)

## 학습 목표 (Mục tiêu)
- Nắm vững quy trình tối ưu hóa hiệu năng truy vấn SQL (`쿼리 성능 최적화`) và vai trò của công cụ giám sát hiệu năng APM (`Application Performance Management`).
- Phân biệt chi tiết cơ chế hoạt động của hai loại bộ tối ưu hóa truy vấn trong DBMS: **Bộ tối ưu dựa trên quy tắc (RBO - `규칙 기반 옵티마이저`)** và **Bộ tối ưu dựa trên chi phí (CBO - `비용 기반 옵티마이저`)**.
- Kết hợp kỹ thuật Phi chuẩn hóa (`반정규화`) có kiểm soát để giảm thiểu gánh nặng phép kết nối (`Join`) trong các truy vấn thường xuyên.

## 핵심 키워드 (Từ khóa)
- 쿼리 성능 최적화 (Tối ưu hóa hiệu năng truy vấn / Query Optimization)
- 옵티마이저 (Bộ tối ưu hóa truy vấn / Optimizer)
- RBO (규칙 기반 옵티마이저 / Rule-Based Optimizer)
- CBO (비용 기반 옵티마이저 / Cost-Based Optimizer)
- 실행 계획 (Kế hoạch thực thi truy vấn / Execution Plan)
- APM (Application Performance Management)
- 반정규화 (Phi chuẩn hóa / Denormalization)
- 인덱스 재구성 (Tái cấu trúc chỉ mục / Index Rebuild)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([18-bai-hoc.md](18-bai-hoc.md), [19-bai-hoc.md](19-bai-hoc.md), [20-bai-hoc.md](20-bai-hoc.md)):** Sau khi chuẩn hóa để bảo vệ tính toàn vẹn, trong môi trường sản xuất thực tế người kỹ sư phải theo dõi hiệu năng hệ thống qua APM và tái cân bằng bằng tối ưu truy vấn hoặc phi chuẩn hóa.
- **Tiếp nối sang các bài sau ([22-bai-hoc.md](22-bai-hoc.md), [24-bai-hoc.md](24-bai-hoc.md)):** Để các câu truy vấn chạy nhanh mà không xung đột tài nguyên, hệ thống cần phối hợp tối ưu hóa truy vấn với cấu trúc Chỉ mục (`인덱스`) và quản trị Giao dịch (`트랜잭션`).

## 읽는 방법 (Cách đọc)
- Học thuộc bảng so sánh **RBO vs CBO** ở TẦNG A:
  - RBO: Chạy theo **thứ tự ưu tiên quy tắc cố định (규칙 우선순위)**, phụ thuộc vào tay nghề viết SQL của lập trình viên.
  - CBO: Chạy theo **ước tính chi phí tài nguyên (액세스 비용)**, sử dụng số liệu thống kê (Statistics) từ DBMS.
- Nhớ quy trình tối ưu hóa: Đo đạc bằng APM $\rightarrow$ Kiểm tra Execution Plan $\rightarrow$ Viết lại SQL / Tạo thêm Index.

---

## 20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Quy trình tối ưu hóa hiệu năng truy vấn (쿼리 성능 최적화 개요):**
  - **Mục tiêu:** Nâng cao tốc độ xử lý I/O và giảm thời gian phản hồi của các ứng dụng nhập/xuất dữ liệu thông qua tối ưu hóa mã SQL và kiến trúc vật lý.
  - **Bước 1 (Chọn đối tượng):** Dùng công cụ đo lường hiệu năng ứng dụng **APM** để giám sát và phát hiện các câu lệnh SQL chạy chậm (Slow Query / 병목 쿼리).
  - **Bước 2 (Phân tích):** Đánh giá **Kế hoạch thực thi (`실행 계획 / Execution Plan`)** do bộ tối ưu hóa (Optimizer) thiết lập.
  - **Bước 3 (Thực thi):** Tái cấu trúc mã lệnh SQL, tạo/sắp xếp lại chỉ mục (Index) hoặc áp dụng kỹ thuật phi chuẩn hóa (Denormalization).
- **2. Bảng so sánh kinh điển: RBO vs CBO (옵티마이저 비교):**
  | Tiêu chí | RBO (규칙 기반 옵티마이저 / Rule-Based) | CBO (비용 기반 옵티마이저 / Cost-Based) |
  |---|---|---|
  | **Tiêu chí tối ưu** | Dựa trên **thứ tự ưu tiên của các quy tắc định sẵn** (15 bậc quy tắc cố định) | Dựa trên **tổng chi phí tài nguyên ước tính** (CPU, bộ nhớ, số lần I/O đĩa) |
  | **Phụ thuộc hiệu năng** | Phụ thuộc vào **trình độ và độ am hiểu quy tắc của lập trình viên SQL** | Phụ thuộc vào **năng lực dự đoán và độ chính xác thống kê của DBMS** |
  | **Đặc trưng kế hoạch** | **Dễ dự đoán** trước lộ trình thực thi truy vấn | Kế hoạch **phức tạp, tự động điều chỉnh** theo khối lượng dữ liệu thực tế |
  | **Yếu tố then chốt** | Lập trình viên phải nắm rõ quy tắc để viết lệnh đúng thứ tự | Phải định kỳ thu thập và cập nhật **thông tin thống kê (Statistics Info)** |

- **3. Vai trò của Phi chuẩn hóa trong tối ưu hiệu năng:**
  - Khi một câu truy vấn phải thực hiện phép kết nối trên quá nhiều bảng lớn, chi phí CPU và I/O tăng vọt.
  - Kỹ thuật phi chuẩn hóa như **Gộp bảng (`테이블 통합`)** hoặc **Thêm cột trùng lặp (`중복 속성 추가`)** giúp loại bỏ trực tiếp phép Join, cho phép Optimizer truy xuất trực tiếp từ một khối dữ liệu liền mạch.
- **주의/함정 (Bẫy đề thi):**
  - Đề hỏi: *"Bộ tối ưu nào dựa vào thống kê dữ liệu thực tế để đưa ra quyết định?"* $\rightarrow$ Đáp án: **CBO (비용 기반 옵티마이저)**.
  - Đề hỏi: *"Bộ tối ưu nào phụ thuộc trực tiếp vào tay nghề viết SQL của lập trình viên?"* $\rightarrow$ Đáp án: **RBO (규칙 기반 옵티마이저)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa đọc Kế hoạch thực thi (Execution Plan):**
  - Giả sử câu truy vấn: `SELECT TenSV, Diem FROM SINH_VIEN WHERE MaSV = 101;`
  - Nếu cột `MaSV` có Index (Primary Key):
    - Optimizer chọn đường dẫn `INDEX UNIQUE SCAN` $\rightarrow$ Đọc đúng 1 khối dữ liệu trên đĩa (Cost cực thấp).
  - Nếu cột `MaSV` không có Index:
    - Optimizer bắt buộc phải chọn `TABLE ACCESS FULL` $\rightarrow$ Quét toàn bộ hàng triệu dòng trong bảng (Cost rất cao).
- **Công cụ APM trong thực tế:**
  - Các công cụ APM phổ biến (như Jennifer, Scouter, Dynatrace, New Relic) tự động thu thập các metric: thời gian xử lý truy vấn, số phiên kết nối (connection pool), và dung lượng lock contention trên DBMS.

### 복습 체크리스트
- [ ] Phân biệt được điểm khác nhau căn bản giữa RBO (규칙 기반) và CBO (비용 기반).
- [ ] Nhớ rõ CBO sử dụng thông tin thống kê (통계 정보) và ước tính chi phí (비용).
- [ ] Nêu được vai trò của APM trong việc phát hiện truy vấn cần tối ưu.
- [ ] Giải thích được vì sao phi chuẩn hóa giúp Optimizer giảm bớt chi phí Join.
