# 109 ~ 112: 형상 관리 (SCM - Software Configuration Management)

## 학습 목표 (Mục tiêu)
- Nắm vững 5 chức năng cốt lõi của Quản lý cấu hình phần mềm (SCM): 형상 식별 (Nhận dạng), 버전 제어 (Kiểm soát phiên bản), 형상 통제 (Kiểm soát thay đổi), 형상 감사 (Kiểm toán cấu hình) và 형상 기록/보고 (Báo cáo trạng thái).
- Hiểu rõ mục tiêu của SCM trong việc bảo đảm tính hiển thị (가시성 - Visibility), tính truy xuất nguồn gốc (추적성 - Traceability) và ngăn ngừa các sửa đổi tùy tiện (무절제한 변경 방지).
- Thành thạo các thuật ngữ quản trị vòng đời phiên bản: Kho lưu trữ (Repository), Lấy mã (Check-out), Đẩy mã (Check-in/Commit) và Đồng bộ hóa (Update/Sync).

## 핵심 키워드 (Từ khóa)
- 형상 관리 5대 기능 (SCM 5 Major Functions)
- 형상 식별 (Identification) & 버전 제어 (Version Control)
- 형상 통제 (Control) & 형상 감사 (Audit) & 형상 기록 (Reporting)
- 가시성 (Visibility) & 추적성 (Traceability)
- 무절제한 변경 방지 (Preventing uncontrolled changes)
- 저장소 (Repository) & 체크아웃 (Check-out) & 커밋 (Commit)

## 선행·연결 개념 (Kiến thức liên kết)
- [36-bai-hoc.md](36-bai-hoc.md): Tổng quan về SCM và các thao tác cơ bản.
- [37-bai-hoc.md](37-bai-hoc.md): 3 mô hình kiến trúc phiên bản (Shared, C/S, Distributed).
- [40-bai-hoc.md](40-bai-hoc.md): So sánh chi tiết hai công cụ SVN và Git.

## 읽는 방법 (Cách đọc)
- Phân biệt rõ chức năng thứ 2 (버전 제어) và chức năng thứ 3 (형상 통제):
  - **버전 제어 (Version Control):** Lưu vết lịch sử thay đổi của từng file (phiên bản cũ, mới).
  - **형상 통제 (Configuration Control):** Thẩm định và duyệt xem CÓ ĐƯỢC PHÉP thay đổi Baseline hay không (thông qua CCB).
- Nhớ 2 từ khóa lợi ích của SCM: **가시성 (Hiển thị)** và **추적성 (Truy vết)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Mục tiêu quản lý của SCM (Software Configuration Management):**
  - **가시성 (Tính hiển thị):** Giúp toàn bộ nhóm và ban quản lý thấy rõ ai đang làm việc trên mô-đun nào, tiến độ sửa đổi ra sao.
  - **추적성 (Tính truy xuất):** Khi phát sinh lỗi (Bug/Defect), có thể lần ngược lịch sử để biết chính xác dòng code nào, commit nào, ai đã sửa đổi và vì lý do gì.
  - **무절제한 변경 방지 (Ngăn chặn sửa đổi vô độ):** Đảm bảo mọi thay đổi vào nhánh chính (Baseline) đều phải qua quy trình xét duyệt nghiêm ngặt.
- **5 chức năng cơ bản của Quản lý cấu hình (SCM 5대 기능):**
  1. **형상 식별 (Configuration Identification):**
     - Đặt tên, đánh số phiên bản, phân cấp cây cấu trúc cho từng hạng mục cấu hình (Source code, Thiết kế, Kế hoạch).
     - Xác lập đường cơ sở (**기준선 - Baseline**).
  2. **버전 제어 (Version Control):**
     - Quản lý các phiên bản phát sinh theo thời gian, lưu vết chênh lệch giữa các phiên bản.
  3. **형상 통제 (Configuration Control):**
     - Tiếp nhận phiếu yêu cầu thay đổi (CR - Change Request).
     - Hội đồng kiểm soát thay đổi (CCB) phân tích tác động và ra quyết định chấp thuận hay bác bỏ.
  4. **형상 감사 (Configuration Audit):**
     - Kiểm tra độc lập xem các thay đổi đã thực hiện có tuân thủ đúng yêu cầu kỹ thuật và có làm hỏng các chức năng khác không (gồm Kiểm toán chức năng FCA và Kiểm toán vật lý PCA).
  5. **형상 기록 / 보고 (Configuration Status Accounting / Reporting):**
     - Ghi nhận nhật ký thay đổi, theo dõi tiến độ xử lý yêu cầu và lập báo cáo định kỳ gửi các bên liên quan.

- **Bảng thuật ngữ quản lý kho chứa:**

| Thuật ngữ | Tiếng Hàn | Hành động cụ thể |
| :--- | :--- | :--- |
| **Repository** | **저장소** | Thư mục trung tâm hoặc phân tán chứa toàn bộ lịch sử các phiên bản |
| **Check-out** | **체크아웃** | Lấy một phiên bản từ kho lưu trữ về máy trạm để xem hoặc sửa đổi |
| **Check-in / Commit** | **체크인 / 커밋** | Ghi nhận phiên bản đã chỉnh sửa xong vào kho lưu trữ |
| **Update / Sync** | **업데이트 / 동기화** | Cập nhật những thay đổi mới nhất từ kho lưu trữ vào thư mục làm việc của mình |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Hai hình thức Kiểm toán cấu hình (Configuration Audit):**
  - **기능 형상 감사 (Functional Configuration Audit - FCA):** Kiểm tra xem hạng mục cấu hình có đáp ứng đầy đủ tất cả các tính năng và hiệu năng nghiệp vụ được mô tả trong bản đặc tả ban đầu hay không.
  - **물리 형상 감사 (Physical Configuration Audit - PCA):** Kiểm tra xem mã nguồn, tài liệu hướng dẫn sử dụng, ca kiểm thử đã được đóng gói đầy đủ và đúng quy chuẩn kỹ thuật để bàn giao chưa.

### 복습 체크리스트
- [ ] Kể tên 5 chức năng cơ bản của SCM: 식별, 버전 제어, 통제, 감사, 기록.
- [ ] Nhớ 3 mục tiêu của SCM: 가시성 (Hiển thị), 추적성 (Truy vết), 무절제한 변경 방지 (Ngăn sửa đổi vô độ).
- [ ] Phân biệt rõ nhiệm vụ của Hội đồng CCB trong bước 형상 통제.
- [ ] Phân biệt được 2 loại kiểm toán: FCA (Tính năng) và PCA (Đóng gói vật lý).
