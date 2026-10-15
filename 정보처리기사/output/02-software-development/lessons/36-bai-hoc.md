# 13. 형상 관리 (SCM - Software Configuration Management)

## 학습 목표 (Mục tiêu)
- Định nghĩa Quản lý cấu hình phần mềm (형상 관리 - SCM: Software Configuration Management) và mục tiêu cốt lõi: Quản lý có hệ thống mọi thay đổi phát sinh trong suốt vòng đời phần mềm, giảm thiểu chi phí và loại bỏ các tác nhân gây gián đoạn.
- Phân biệt các thuật ngữ thao tác kho chứa phiên bản cơ bản: Check-Out, Check-In, Commit và Update.
- Nhận diện các công cụ SCM kinh điển trong lịch sử và hiện đại (CVS, SVN, Git).

## 핵심 키워드 (Từ khóa)
- 형상 관리 (Software Configuration Management - SCM)
- 소프트웨어 생명주기 변경 관리 (Lifecycle Change Management)
- 체크아웃 (Check-Out) & 체크인 (Check-In)
- 커밋 (Commit) & 업데이트 (Update)
- 저장소 (Repository)
- 버전 관리 도구 (Git, SVN, CVS)

## 선행·연결 개념 (Kiến thức liên kết)
- [32-bai-hoc.md](32-bai-hoc.md): Quy trình triển khai mã nguồn mô-đun.
- [37-bai-hoc.md](37-bai-hoc.md): 3 mô hình kiến trúc quản lý phiên bản (Shared Folder, Client/Server, Distributed).
- [39-bai-hoc.md](39-bai-hoc.md): 5 chức năng quản lý cấu hình chuẩn tắc (식별, 통제, 감사, 기록).

## 읽는 방법 (Cách đọc)
- Phân biệt hướng di chuyển của dữ liệu giữa Máy cá nhân (Local) và Kho lưu trữ (Repository):
  - Kéo mã nguồn từ kho về máy để làm việc $\rightarrow$ **Check-Out**.
  - Đẩy mã nguồn đã sửa đổi lên kho phiên bản $\rightarrow$ **Check-In / Commit**.
  - Đồng bộ mã nguồn mới nhất của nhóm về máy $\rightarrow$ **Update**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bản chất của Quản lý cấu hình (SCM - Software Configuration Management):**
  - Là chuỗi các hoạt động có kỷ luật nhằm nhận dạng, kiểm soát, ghi chép và kiểm toán mọi thay đổi đối với toàn bộ các sản phẩm phần mềm (Mã nguồn, Tài liệu thiết kế, Kế hoạch, Bản đặc tả kiểm thử) trong suốt vòng đời phát triển phần mềm (SDLC).
  - **Mục tiêu tối thượng:**
    - Nâng cao tính hiển thị (Visibility) và tính truy xuất nguồn gốc (Traceability) của dự án.
    - Ngăn chặn các sửa đổi tùy tiện, không được phê duyệt (무절제한 변경 방지).
    - Giảm thiểu chi phí phát triển và hạn chế xung đột công việc giữa các lập trình viên.
- **Bảng thuật ngữ thao tác kho chứa phiên bản cơ bản:**

| Thuật ngữ (Hàn / Anh) | Định nghĩa thao tác kỹ thuật | Ý nghĩa thực tế |
| :--- | :--- | :--- |
| **저장소 (Repository)** | Nơi lưu trữ tập trung toàn bộ mã nguồn, tệp tin và lịch sử thay đổi phiên bản | "Kho chứa dữ liệu lịch sử" của dự án |
| **체크아웃 (Check-Out)** | Trích xuất một phiên bản cụ thể từ kho lưu trữ về thư mục làm việc của lập trình viên | Lấy mã nguồn về máy để chuẩn bị sửa đổi |
| **체크인 (Check-In)** | Đưa các tệp tin đã được lập trình viên sửa đổi hoàn tất trở lại kho lưu trữ | Ghi nhận phiên bản cập nhật mới vào kho |
| **커밋 (Commit)** | Thao tác xác nhận ghi vĩnh viễn các thay đổi vào lịch sử kho lưu trữ (kèm thông điệp Commit message) | Đóng dấu phiên bản sửa đổi chính thức |
| **업데이트 (Update)** | Đồng bộ hóa và tải về máy cá nhân những thay đổi mới nhất mà các thành viên khác vừa Commit lên kho | Làm mới mã nguồn cục bộ để tránh xung đột |

- **Bẫy đề thi trắc nghiệm:**
  - **Bẫy 1:** *"Thao tác nào sau đây dùng để lấy mã nguồn từ Repository về thư mục làm việc của lập trình viên?"* $\rightarrow$ Đáp án: **체크아웃 (Check-Out)**.
  - **Bẫy 2:** *"Chi phí phát triển phần mềm (개발 비용) có phải là đối tượng nằm trong danh mục cấu hình (Configuration Item) cần quản lý SCM không?"* $\rightarrow$ Đáp án: **KHÔNG**. Đối tượng SCM chỉ là các sản phẩm kỹ thuật phần mềm (Source code, Thiết kế, Kế hoạch, Test case).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Đường cơ sở (기준선 - Baseline) trong SCM:**
  - Baseline là trạng thái của một hạng mục cấu hình đã được xem xét và phê duyệt chính thức bởi Hội đồng kiểm soát thay đổi (CCB).
  - Khi một tài liệu hoặc phiên bản mã đã trở thành Baseline:
    - Bất kỳ ai muốn sửa đổi đều bắt buộc phải trải qua quy trình yêu cầu thay đổi (CR - Change Request) và được CCB duyệt chính thức, không được tự ý sửa trực tiếp.

### 복습 체크리스트
- [ ] Định nghĩa mục tiêu của SCM: Quản lý có hệ thống mọi thay đổi trong vòng đời phần mềm.
- [ ] Phân biệt rõ Check-Out (lấy về), Check-In / Commit (đẩy lên), Update (đồng bộ).
- [ ] Nhớ đối tượng của SCM là các sản phẩm kỹ thuật, KHÔNG bao gồm chi phí phát triển.
- [ ] Hiểu khái niệm Baseline (기준선) là mốc đã được phê duyệt chính thức.
