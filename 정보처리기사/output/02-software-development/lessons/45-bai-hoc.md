# 100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)

## 학습 목표 (Mục tiêu)
- Nằm lòng trình tự 7 bước chuẩn mực trong quy trình Đóng gói phần mềm: 기능 식별 (Xác định chức năng) $\rightarrow$ 모듈화 (Mô-đun hóa) $\rightarrow$ 빌드 진행 (Tiến hành Build) $\rightarrow$ 사용자 환경 분석 (Phân tích môi trường người dùng) $\rightarrow$ 패키징 및 적용 시험 (Đóng gói và Kiểm thử) $\rightarrow$ 패키징 변경 개선 (Sửa đổi cải tiến) $\rightarrow$ 배포 (Phát hành/Triển khai).
- Hiểu rõ nội dung công việc và kết quả đầu ra của từng bước trong chuỗi 7 giai đoạn đóng gói.
- Ôn tập các lưu ý sống còn về môi trường tối thiểu, tính đồng nhất giao diện và các giải pháp an ninh bản quyền.

## 핵심 키워드 (Từ khóa)
- 패키징 순서 7단계 (Packaging 7 Steps)
- 기능 식별 (Functional Identification)
- 모듈화 (Modularization)
- 빌드 진행 (Build Execution)
- 사용자 환경 분석 (User Environment Analysis)
- 패키징 및 적용 시험 (Packaging & Verification Test)
- 패키징 변경 개선 (Modification & Improvement)
- 배포 (Deployment)

## 선행·연결 개념 (Kiến thức liên kết)
- [42-bai-hoc.md](42-bai-hoc.md): Các yếu tố kỹ thuật cần xem xét khi đóng gói phần mềm.
- [44-bai-hoc.md](44-bai-hoc.md): Định nghĩa tổng quan và nguyên tắc đóng gói phần mềm.
- [46-bai-hoc.md](46-bai-hoc.md): Các công cụ tự động hóa quá trình Build (Ant, Maven, Gradle, Jenkins).

## 읽는 방법 (Cách đọc)
- Học thuộc thần chú 7 chữ cái đầu của quy trình đóng gói: **"기 - 모 - 빌 - 환 - 패 - 개 - 배"** (*Kì - Mô - Bil - Hoàn - Phe - Cải - Bê*).
- Nhớ thứ tự logic:
  - Phải có tính năng và chia mô-đun trước $\rightarrow$ sau đó mới Build ra file thực thi $\rightarrow$ phân tích môi trường người dùng $\rightarrow$ đóng gói tạo file setup và test thử $\rightarrow$ sửa lỗi nếu có $\rightarrow$ phát hành chính thức.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Quy trình 7 bước đóng gói phần mềm chuẩn mực (소프트웨어 패키징 순서):**
  $$\mathbf{기능\ 식별} \rightarrow \mathbf{모듈화} \rightarrow \mathbf{빌드\ 진행} \rightarrow \mathbf{사용자\ 환경\ 분석} \rightarrow \mathbf{패키징\ 및\ 적용\ 시험} \rightarrow \mathbf{변경\ 개선} \rightarrow \mathbf{배포}$$

| Thứ tự bước | Tên tiếng Hàn & Anh | Nội dung công việc cụ thể |
| :---: | :--- | :--- |
| **Bước 1** | **기능 식별 (Functional Identification)** | Rà soát toàn bộ các chức năng và tính năng nghiệp vụ đã được phát triển hoàn thiện trong phần mềm |
| **Bước 2** | **모듈화 (Modularization)** | Phân chia các chức năng thành các khối mô-đun độc lập để phục vụ việc đóng gói, quản lý và bảo trì sau này |
| **Bước 3** | **빌드 진행 (Build Execution)** | Sử dụng các công cụ Build để biên dịch mã nguồn, liên kết các thư viện phụ thuộc và tạo ra các tệp thực thi nhị phân hoàn chỉnh |
| **Bước 4** | **사용자 환경 분석 (User Environment Analysis)** | Khảo sát và phân tích cấu hình hệ điều hành, vi xử lý, dung lượng RAM và card đồ họa phổ biến của nhóm người dùng mục tiêu |
| **Bước 5** | **패키징 및 적용 시험 (Packaging & Verification Test)** | Tạo tệp cài đặt (Setup/Installer), tiến hành cài đặt thử nghiệm trên các máy tính mẫu mô phỏng môi trường người dùng để kiểm tra tính tương thích |
| **Bước 6** | **패키징 변경 개선 (Modification & Improvement)** | Rà soát các lỗi phát sinh trong quá trình cài đặt thử nghiệm, sửa đổi tệp cấu hình và tối ưu hóa lại bộ cài đặt |
| **Bước 7** | **배포 (Deployment / Delivery)** | Bàn giao chính thức bộ cài đặt phần mềm hoàn thiện cho khách hàng hoặc tải lên các kho ứng dụng phân phối trực tuyến |

- **Bẫy đề thi trắc nghiệm:**
  - **Bẫy 1:** *"Sắp xếp đúng thứ tự các bước trong quy trình đóng gói phần mềm?"* $\rightarrow$ Tra cứu thần chú **기-모-빌-환-패-개-배** để chọn phương án chính xác.
  - **Bẫy 2:** *"Bước '사용자 환경 분석' (Phân tích môi trường người dùng) diễn ra trước hay sau bước '빌드 진행' (Build)?"* $\rightarrow$ Diễn ra **ngay sau bước Build** và **trước bước Packaging**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tầm quan trọng của bước 패키징 및 적용 시험 (Verification Test):**
  - Quá trình thử nghiệm bộ cài đặt (Installer Testing) không chỉ kiểm tra xem phần mềm có chạy được hay không, mà còn phải kiểm tra:
    - Cơ chế kiểm tra dung lượng ổ đĩa trống trước khi giải nén tệp.
    - Cơ chế khôi phục trạng thái ban đầu (Rollback) nếu người dùng bấm Hủy (Cancel) giữa chừng hoặc gặp sự cố mất điện trong lúc đang cài đặt.
    - Khả năng cài đè nâng cấp (In-place Upgrade) từ phiên bản cũ lên phiên bản mới mà không làm mất dữ liệu người dùng.

### 복습 체크리스트
- [ ] Thuộc lòng thứ tự 7 bước đóng gói: 기능 식별 $\rightarrow$ 모듈화 $\rightarrow$ 빌드 $\rightarrow$ 사용자 환경 분석 $\rightarrow$ 패키징 및 시험 $\rightarrow$ 변경 개선 $\rightarrow$ 배포.
- [ ] Nắm vững thần chú ghi nhớ: 기 - 모 - 빌 - 환 - 패 - 개 - 배.
- [ ] Xác định đúng thời điểm kiểm thử cài đặt: diễn ra ở bước 5 sau khi phân tích môi trường.
- [ ] Hiểu rõ cơ chế Rollback an toàn trong kiểm thử trình cài đặt.
