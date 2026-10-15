# 282. 운영체제의 정의 및 목적 (Definition & Purpose of OS)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa của hệ điều hành (운영체제 - Operating System): phần mềm hệ thống trung gian quản lý tài nguyên phần cứng máy tính và cung cấp giao diện thuận tiện cho người dùng và các chương trình ứng dụng.
- Ghi nhớ 4 mục tiêu đánh giá hiệu năng của hệ điều hành: Tối đa hóa năng lực xử lý (처리 능력 - Throughput), Tối thiểu hóa thời gian quay vòng (반환 시간 - Turnaround Time), Tối đa hóa độ tin cậy (신뢰도 - Reliability), và Tối đa hóa tính khả dụng (사용 가능도 / 가용성 - Availability).
- Phân biệt các chức năng quản trị tài nguyên cốt lõi của hệ điều hành: Quản lý bộ vi xử lý (CPU), Quản lý bộ nhớ (Memory), Quản lý thiết bị I/O, và Quản lý hệ thống tệp tin (File System).

## 핵심 키워드 (Từ khóa)
- 운영체제의 정의 (Definition of Operating System)
- 운영체제의 목적 (Purposes of OS / 4대 평가 기준)
- 처리 능력 (Throughput / 일정 시간 내 작업 처리량 증대)
- 반환 시간 (Turnaround Time / 작업 제출부터 결과 완료까지 단축)
- 신뢰도 (Reliability / 정확한 결과 보장)
- 사용 가능도 (Availability / 즉시 사용 가능한 정도)
- 자원 관리 (Resource Management)

## 선행·연결 개념 (Kiến thức liên kết)
- [34-bai-hoc.md](34-bai-hoc.md): Cấu trúc chương trình điều khiển và xử lý của hệ điều hành.
- [36-bai-hoc.md](36-bai-hoc.md): Hệ thống UNIX và mô tả tệp tin (File Descriptor).
- [정보처리기사/output/01-software-design/lessons/01-bai-hoc.md](../../01-software-design/lessons/01-bai-hoc.md): Khái niệm phần mềm và kiến trúc hệ thống thông tin.

## 읽는 방법 (Cách đọc)
- Phân biệt rõ chiều hướng của 4 tiêu chí đánh giá hiệu năng hệ điều hành:
  - **TĂNG CÀNG CAO CÀNG TỐT (Maximize):**
    - **처리 능력 (Throughput):** Số lượng công việc máy tính giải quyết xong trong 1 đơn vị thời gian (giờ/ngày) $\rightarrow$ Càng nhiều càng tốt ($\uparrow$).
    - **신뢰도 (Reliability):** Tỷ lệ máy tính tính toán đúng, không bị lỗi $\rightarrow$ Càng cao càng tốt ($\uparrow$).
    - **사용 가능도 (Availability):** Khi người dùng cần máy tính, hệ thống sẵn sàng phục vụ ngay lập tức mà không bị đơ/sập $\rightarrow$ Càng cao càng tốt ($\uparrow$).
  - **GIẢM CÀNG THẤP CÀNG TỐT (Minimize):**
    - **반환 시간 (Turnaround Time):** Tổng thời gian tính từ lúc người dùng bấm nút gửi lệnh cho đến khi máy tính trả kết quả hoàn chỉnh $\rightarrow$ **CÀNG NGẮN CÀNG TỐT ($\downarrow$)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng 4 mục tiêu hiệu năng của hệ điều hành (운영체제의 4대 목적):**

| Tiêu chuẩn mục tiêu | Tên tiếng Hàn & Anh | Định nghĩa kỹ thuật chuẩn đề thi | Chiều hướng tối ưu |
| :--- | :--- | :--- | :--- |
| **1. Năng lực xử lý** | **처리 능력 (Throughput)** | Số lượng công việc (Job/Task) mà hệ thống có thể xử lý hoàn tất trong một đơn vị thời gian định trước | **Tối đa hóa (증대 / $\uparrow$)** |
| **2. Thời gian quay vòng** | **반환 시간 (Turnaround Time)** | Tổng thời gian trôi qua từ thời điểm nộp công việc (**제출**) đến khi nhận được kết quả cuối cùng (**완료**) | **Tối thiểu hóa (단축 / $\downarrow$)** |
| **3. Độ tin cậy** | **신뢰도 (Reliability)** | Khả năng hệ thống thực thi chính xác nhiệm vụ mà không xảy ra sai sót, lỗi logic hay đổ vỡ dữ liệu | **Tối đa hóa (향상 / $\uparrow$)** |
| **4. Tính khả dụng** | **사용 가능도 (Availability)** | Mức độ sẵn sàng phục vụ của hệ thống ngay tức thì khi người dùng hoặc ứng dụng có nhu cầu sử dụng tài nguyên | **Tối đa hóa (증대 / $\uparrow$)** |

- **Bốn lĩnh vực quản lý tài nguyên của hệ điều hành:**
  1. **프로세스 관리 (Quản lý tiến trình):** Lập lịch CPU, tạo/hủy tiến trình, đồng bộ hóa và chống bế tắc (Deadlock).
  2. **기억장치 관리 (Quản lý bộ nhớ):** Phân bổ vùng nhớ, quản lý bộ nhớ ảo (Paging/Segmentation), dọn dẹp phân mảnh.
  3. **주변장치 관리 (Quản lý ngoại vi):** Điều phối các thiết bị nhập xuất (I/O), xử lý ngắt và cơ chế Spooling.
  4. **파일 관리 (Quản lý tệp tin):** Tạo, đọc, ghi, xóa và phân quyền bảo mật cây thư mục trên ổ đĩa.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Các thành phần cấu thành Thời gian quay vòng (Turnaround Time):**
  - $\text{Turnaround Time} = \text{Thời gian chờ trong hàng đợi (Waiting Time)} + \text{Thời gian thực thi CPU (Execution Time)} + \text{Thời gian chờ I/O} + \text{Thời gian xuất kết quả}$.
  - Mục tiêu hàng đầu của các thuật toán lập lịch hiện đại là cắt giảm thời gian chờ đợi lãng phí trong hàng đợi (Waiting Time) để ép thời gian phản hồi (Response Time) xuống mức nhỏ nhất.

### 복습 체크리스트
- [ ] Kể tên đủ 4 mục tiêu của hệ điều hành: 처리 능력, 반환 시간, 신뢰도, 사용 가능도.
- [ ] Nhớ trong 4 mục tiêu, CHỈ CÓ 반환 시간 (Turnaround Time) là cần 단축 (giảm tối thiểu).
- [ ] Ba mục tiêu còn lại (Throughput, Reliability, Availability) đều cần 증대 (tăng tối đa).
- [ ] Nắm được 4 mảng quản trị tài nguyên: Tiến trình, Bộ nhớ, Ngoại vi, Tệp tin.
