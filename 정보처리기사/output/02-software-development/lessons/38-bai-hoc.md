# 핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)

## 학습 목표 (Mục tiêu)
- Nắm vững quy trình 4 giai đoạn chuẩn của Quản lý cấu hình phần mềm (SCM): Nhận dạng cấu hình (형상 식별) $\rightarrow$ Kiểm soát cấu hình (형상 통제) $\rightarrow$ Kiểm toán cấu hình (형상 감사) $\rightarrow$ Báo cáo/Ghi chép cấu hình (형상 기록).
- Định nghĩa vai trò của Hội đồng kiểm soát thay đổi (CCB - Configuration Control Board) trong giai đoạn 형상 통제.
- Định nghĩa Môi trường phát triển tích hợp (IDE - Integrated Development Environment) và 4 chức năng cốt lõi: Viết mã (Coding), Biên dịch (Compile), Gỡ lỗi (Debugging) và Triển khai (Deployment).

## 핵심 키워드 (Từ khóa)
- 형상 관리 4단계 절차 (SCM 4 Stages)
- 형상 식별 (Configuration Identification)
- 형상 통제 (Configuration Control / CCB 변경 통제 위원회)
- 형상 감사 (Configuration Audit)
- 형상 기록 / 보고 (Configuration Status Accounting)
- 통합 개발 환경 (IDE - Integrated Development Environment)
- 코딩, 컴파일, 디버깅, 배포 (Coding, Compile, Debugging, Deployment)

## 선행·연결 개념 (Kiến thức liên kết)
- [36-bai-hoc.md](36-bai-hoc.md): Khái niệm tổng quan về SCM và các thao tác kho chứa.
- [37-bai-hoc.md](37-bai-hoc.md): 3 mô hình phiên bản (Shared Folder, C/S, Distributed).
- [47-bai-hoc.md](47-bai-hoc.md): Mở rộng về các công cụ IDE và Build tools trong quy trình DevOps.

## 읽는 방법 (Cách đọc)
- Học thuộc thần chú 4 bước SCM: **"Nhận - Kiểm - Toán - Ghi"** (식별 $\rightarrow$ 통제 $\rightarrow$ 감사 $\rightarrow$ 기록).
- Cứ thấy nhắc đến việc phê duyệt yêu cầu thay đổi (CR - Change Request) $\rightarrow$ Chọn ngay **형상 통제 (Configuration Control)** gắn liền với **CCB**.
- Ghi nhớ bộ tứ của IDE: **Coding - Compile - Debugging - Deployment**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Quy trình 4 giai đoạn chuẩn mực của Quản lý cấu hình (SCM):**
  $$\mathbf{형상\ 식별 (Nhận\ dạng)} \longrightarrow \mathbf{형상\ 통제 (Kiểm\ soát)} \longrightarrow \mathbf{형상\ 감사 (Kiểm\ toán)} \longrightarrow \mathbf{형상\ 기록 (Báo\ cáo)}$$

| Giai đoạn SCM | Tên tiếng Hàn & Anh | Nội dung công việc trọng tâm |
| :--- | :--- | :--- |
| **1. Nhận dạng cấu hình** | **형상 식별 (Identification)** | Xác định các sản phẩm cần quản lý (Source code, Thiết kế, Kế hoạch), gán mã định danh, thiết lập cây cấu trúc và xác lập đường cơ sở (**기준선 - Baseline**) |
| **2. Kiểm soát cấu hình** | **형상 통제 (Control)** | Tiếp nhận yêu cầu thay đổi (Change Request), giao cho **Hội đồng kiểm soát thay đổi (CCB)** thẩm định tính khả thi, đánh giá tác động và ra quyết định phê duyệt hoặc từ chối |
| **3. Kiểm toán cấu hình** | **형상 감사 (Audit)** | Tiến hành kiểm tra và xác minh độc lập xem các thay đổi được thực hiện có đúng theo bản vẽ kỹ thuật đã duyệt và có bảo đảm tính toàn vẹn của hệ thống không |
| **4. Báo cáo cấu hình** | **형상 기록 / 보고 (Status Accounting)** | Ghi chép chi tiết nhật ký lịch sử thay đổi, phiên bản hiện tại, trạng thái xử lý của các yêu cầu thay đổi và xuất báo cáo cho các bên liên quan |

- **Môi trường phát triển tích hợp (IDE - Integrated Development Environment):**
  - **Khái niệm:** Là ứng dụng phần mềm toàn diện cung cấp đầy đủ các tiện ích cần thiết cho lập trình viên làm việc trên một giao diện duy nhất, thay vì phải chạy rời rạc nhiều phần mềm riêng biệt.
  - **4 chức năng cốt lõi của IDE:**
    1. **코딩 (Coding):** Soạn thảo mã nguồn với các tính năng tự động hoàn thành từ (IntelliSense), tô màu cú pháp (Syntax Highlighting).
    2. **컴파일 (Compile / Build):** Tích hợp trình biên dịch/thông dịch để chuyển đổi mã nguồn sang mã máy hoặc mã byte.
    3. **디버깅 (Debugging):** Đặt điểm dừng (Breakpoints), theo dõi giá trị biến (Variable Watch), chạy từng dòng lệnh (Step Over/Into) để dò tìm lỗi logic.
    4. **배포 (Deployment):** Đóng gói sản phẩm thành các tệp thực thi (JAR, WAR, APK, EXE) và triển khai tự động lên máy chủ thử nghiệm.
  - **Các phần mềm IDE tiêu biểu:** Eclipse, IntelliJ IDEA (Java), Visual Studio (C#, C++), Xcode (Swift/iOS), Android Studio (Android).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cấu tạo và Quyền hạn của CCB (Configuration Control Board):**
  - CCB là nhóm chuyên trách gồm đại diện của tất cả các bên liên quan: Quản lý dự án (PM), Kiến trúc sư trưởng (Architect), Trưởng nhóm phát triển (Dev Lead), Trưởng nhóm kiểm thử (QA Lead) và Đại diện khách hàng.
  - Không một nhà phát triển nào được phép tự ý sửa đổi mã nguồn đã nằm trong Baseline nếu chưa có chữ ký chấp thuận chính thức từ CCB.

### 복습 체크리스트
- [ ] Đọc đúng thứ tự 4 bước SCM: 형상 식별 $\rightarrow$ 형상 통제 $\rightarrow$ 형상 감사 $\rightarrow$ 형상 기록.
- [ ] Nhớ vai trò của CCB trong giai đoạn 형상 통제 (Kiểm soát thay đổi).
- [ ] Nhớ giai đoạn 형상 식별 gắn liền với việc thiết lập Baseline (기준선).
- [ ] Liệt kê đủ 4 chức năng cốt lõi của IDE: 코딩, 컴파일, 디버깅, 배포.
