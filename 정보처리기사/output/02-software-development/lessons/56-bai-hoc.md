# 35. 테스트 케이스 (Test Case)

## 학습 목표 (Mục tiêu)
- Định nghĩa Bản mô tả ca kiểm thử (테스트 케이스 - Test Case) theo tiêu chuẩn quốc tế ISO/IEC/IEEE 29119-3.
- Nằm lòng các thành phần cấu tạo bắt buộc của một Test Case chuyên nghiệp: Mã định danh (ID), Hạng mục kiểm tra, Điều kiện tiên quyết (Pre-conditions), Dữ liệu đầu vào (Input), Kết quả kỳ vọng (Expected Output) và Quan hệ phụ thuộc.
- Phân biệt rõ sự khác nhau giữa Ca kiểm thử đơn lẻ (Test Case) và Kịch bản kiểm thử tích hợp (테스트 시나리오 - Test Scenario).

## 핵심 키워드 (Từ khóa)
- 테스트 케이스 (Test Case)
- ISO/IEC/IEEE 29119-3 (소프트웨어 테스트 국제 표준)
- 테스트 식별자 (Test Case ID)
- 입력 명세 (Input Specification)
- 출력 명세 / 기대 결과 (Output Specification / Expected Result)
- 환경 설정 / 전제 조건 (Pre-conditions)
- 테스트 시나리오 (Test Scenario)

## 선행·연결 개념 (Kiến thức liên kết)
- [35-bai-hoc.md](35-bai-hoc.md): Nguyên tắc soạn thảo Test Case trước khi code trong kiểm thử đơn vị.
- [52-bai-hoc.md](52-bai-hoc.md): Các kỹ thuật thiết kế Test Case hộp trắng và hộp đen.
- [57-bai-hoc.md](57-bai-hoc.md): Các nguyên lý kiểm thử ứng dụng và hiện tượng 살충제 패러독스.

## 읽는 방법 (Cách đọc)
- Nhớ cấu trúc chuẩn quốc tế của Test Case: ID $\rightarrow$ Mục tiêu $\rightarrow$ Môi trường tiên quyết $\rightarrow$ Dữ liệu nhập $\rightarrow$ Kết quả kỳ vọng.
- Phân biệt Test Case vs Test Scenario:
  - **Test Case:** Đơn lẻ, cụ thể cho 1 chức năng (Ví dụ: Nhập mật khẩu sai báo lỗi gì).
  - **Test Scenario:** Kịch bản xuyên suốt chuỗi thao tác thực tế của người dùng (Ví dụ: Đăng nhập $\rightarrow$ Tìm hàng $\rightarrow$ Thêm vào giỏ $\rightarrow$ Thanh toán).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Định nghĩa Test Case theo chuẩn ISO/IEC/IEEE 29119-3:**
  - Là tài liệu kỹ thuật quy định một tập hợp các giá trị đầu vào, các điều kiện thực thi phần mềm và các kết quả mong đợi được phát triển cho một mục tiêu kiểm tra cụ thể, nhằm xác minh sự tuân thủ đối với một yêu cầu xác định.
- **Bảng các thành phần cấu tạo tiêu chuẩn của Test Case:**

| Thành phần cấu tạo | Tên tiếng Hàn & Anh | Mục đích và nội dung chi tiết |
| :--- | :--- | :--- |
| **Mã định danh** | **테스트 식별자 (Test ID)** | Chuỗi ký tự định danh duy nhất (ví dụ: `TC_LOGIN_001`) để quản lý và truy vết |
| **Hạng mục kiểm tra** | **테스트 항목 (Test Item)** | Tên chức năng hoặc mô-đun được kiểm thử (ví dụ: Kiểm tra tính năng Đăng nhập) |
| **Điều kiện tiên quyết** | **환경 설정 / 전제 조건 (Pre-conditions)** | Trạng thái hệ thống trước khi test (ví dụ: Người dùng đã đăng ký tài khoản thành công) |
| **Dữ liệu đầu vào** | **입력 명세 (Input Specification)** | Giá trị tham số cụ thể truyền vào hệ thống (ví dụ: `ID = "user@test.com"`, `PW = "Abc@123"`) |
| **Kết quả kỳ vọng** | **출력 명세 / 기대 결과 (Expected Output)** | Hành vi hoặc giá trị mà hệ thống phải trả về nếu hoạt động đúng (ví dụ: Chuyển hướng sang trang Dashboard) |
| **Thủ tục thực hiện** | **특수 절차 요구 (Special Procedures)** | Các thao tác đặc biệt cần thiết (ví dụ: Phải ngắt kết nối Internet giữa chừng) |
| **Quan hệ phụ thuộc** | **의존성 기술 (Inter-case Dependencies)** | Chỉ rõ Test Case này có cần phải chạy sau một Test Case nào khác không |

- **So sánh Test Case vs Test Scenario:**

| Tiêu chí | 테스트 케이스 (Test Case) | 테스트 시나리오 (Test Scenario) |
| :--- | :--- | :--- |
| **Phạm vi** | Từng phép thử đơn lẻ cho một trường hợp cụ thể | **Một chuỗi liên hoàn nhiều hành vi của người dùng** |
| **Chi tiết dữ liệu** | Ghi rõ từng giá trị dữ liệu nhập và kết quả số cụ thể | Mô tả luồng công việc nghiệp vụ ở mức tổng quan |
| **Mối quan hệ** | **Nhiều Test Case kết hợp lại tạo thành một Test Scenario** | Là khung sườn định hướng để thiết kế các Test Case |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ma trận truy xuất nguồn gốc kiểm thử (RTM - Requirements Traceability Matrix):**
  - Trong quản lý chất lượng phần mềm chuyên nghiệp, mỗi Test Case bắt buộc phải được ánh xạ 1-1 hoặc 1-N với một Yêu cầu người dùng (User Requirement) trong tài liệu SRS.
  - Ma trận RTM giúp bảo đảm **100% yêu cầu của khách hàng đều có ít nhất một Test Case bao phủ**, không bỏ sót bất kỳ tính năng nào.

### 복습 체크리스트
- [ ] Kể tên tiêu chuẩn quốc tế về tài liệu kiểm thử: ISO/IEC/IEEE 29119-3.
- [ ] Liệt kê đủ các thành phần chính: ID, Hạng mục, Pre-condition, Input, Expected Output.
- [ ] Phân biệt được Test Case (phép thử cụ thể) và Test Scenario (kịch bản chuỗi hành vi).
- [ ] Hiểu vai trò của Ma trận RTM trong việc bảo đảm độ bao phủ yêu cầu.
