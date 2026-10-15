# 12. 소프트웨어 패키징 및 설치 매뉴얼 (Software Packaging & Manual)

## 학습 목표 (Mục tiêu)
- Định nghĩa Đóng gói phần mềm (소프트웨어 패키징 - Software Packaging) với tư cách là quá trình tích hợp các tệp thực thi, tài nguyên và cấu hình thành bộ cài đặt hoàn chỉnh hướng đến người dùng cuối.
- Nắm vững cấu trúc và các thành phần bắt buộc trong Bản hướng dẫn cài đặt phần mềm (설치 매뉴얼 - Installation Manual).
- Hiểu rõ nguyên tắc lấy người dùng làm trung tâm (사용자 중심) và các yêu cầu bảo mật, mã hóa, tích hợp DRM khi phát hành sản phẩm phần mềm.

## 핵심 키워드 (Từ khóa)
- 소프트웨어 패키징 (Software Packaging)
- 사용자 중심 (User-centric)
- 설치 매뉴얼 (Installation Manual)
- 삭제 / 언인스톨 (Uninstall)
- 환경 설정 (Environment Configuration)
- DRM 연동 (DRM Integration)

## 선행·연결 개념 (Kiến thức liên kết)
- [40-bai-hoc.md](40-bai-hoc.md): Quản lý phiên bản mã nguồn trước khi đóng gói phát hành.
- [42-bai-hoc.md](42-bai-hoc.md): Các yếu tố kỹ thuật cần xem xét khi đóng gói phần mềm.
- [50-bai-hoc.md](50-bai-hoc.md): Quản trị bản quyền số DRM (Digital Rights Management).

## 읽는 방법 (Cách đọc)
- Cứ thấy đề thi hỏi về nguyên tắc tối cao của việc đóng gói phần mềm $\rightarrow$ Khẳng định ngay: **사용자 중심 (Lấy người dùng cuối làm trung tâm)**.
- Khi biên soạn tài liệu hướng dẫn cài đặt: Bắt buộc phải có cả hướng dẫn **설치 (Cài đặt)** lẫn hướng dẫn **삭제 (Gỡ cài đặt / Uninstall)** và thông số cấu hình phần cứng tối thiểu.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bản chất của Đóng gói phần mềm (소프트웨어 패키징):**
  - Là công đoạn gom tất cả các tệp thực thi (`.exe`, `.jar`, `.apk`), thư viện liên kết (`.dll`, `.so`), tệp cấu hình và tài nguyên giao diện lại thành một gói cài đặt duy nhất (Setup / Installer) để người dùng có thể dễ dàng cài đặt và vận hành mà không cần am hiểu kỹ thuật lập trình.
  - **Nguyên tắc cốt lõi:** **사용자 중심 (Lấy người sử dụng làm trung tâm)**:
    - Giao diện cài đặt trực quan, dễ thao tác (thao tác Next $\rightarrow$ Finish).
    - Phải có tính tương thích cao với nhiều hệ điều hành khác nhau.
    - Cần tích hợp cơ chế bảo mật bản quyền (Mã hóa, chữ ký số, DRM).
- **Cấu trúc chuẩn của Bản hướng dẫn cài đặt (설치 매뉴얼):**

| Mục nội dung | Tên tiếng Hàn & Anh | Yêu cầu chi tiết |
| :--- | :--- | :--- |
| **Thông tin cơ bản** | **기본 사항 (General Info)** | Tên sản phẩm, phiên bản phần mềm, ngày phát hành, thông tin nhà phát triển và hỗ trợ kỹ thuật |
| **Tổng quan phần mềm** | **소프트웨어 개요 (Software Overview)** | Mục đích sử dụng, các tính năng chính và cấu hình phần cứng tối thiểu/đề nghị (OS, CPU, RAM, Ổ cứng) |
| **Quy trình cài đặt** | **설치 과정 (Installation Steps)** | Hướng dẫn từng bước kèm ảnh chụp màn hình minh họa (UI Screenshots), cách chọn thư mục và nhập khóa bản quyền (License Key) |
| **Quy trình gỡ bỏ** | **프로그램 삭제 (Uninstallation)** | Hướng dẫn chi tiết cách gỡ bỏ sạch sẽ chương trình khỏi hệ thống mà không để lại tệp rác hay hỏng Registry |
| **Xử lý sự cố** | **이상 발생 시 조치 (Troubleshooting)** | Bảng mã lỗi thường gặp khi cài đặt thất bại và các bước khắc phục sự cố |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tầm quan trọng của tài liệu Uninstallation:**
  - Trong đánh giá chất lượng phần mềm theo chuẩn quốc tế (như ISO/IEC 25010), một phần mềm được coi là kém chất lượng nếu chỉ có hướng dẫn cài đặt mà không cung cấp quy trình gỡ bỏ an toàn.
  - Trình gỡ cài đặt (Uninstaller) phải bảo đảm thu hồi toàn bộ dịch vụ nền (Background Services), giải phóng cổng mạng và xóa bỏ các liên kết hệ thống đã đăng ký lúc cài đặt.

### 복습 체크리스트
- [ ] Nhớ nguyên tắc vàng của đóng gói phần mềm: 사용자 중심 (Lấy người dùng làm trung tâm).
- [ ] Kể tên các thành phần trong sổ tay cài đặt: Tổng quan, Cấu hình tối thiểu, Các bước cài đặt, Quy trình xóa bỏ.
- [ ] Khẳng định sổ tay cài đặt bắt buộc phải có hướng dẫn gỡ cài đặt (Uninstall).
- [ ] Nhớ yêu cầu tích hợp bảo mật bản quyền (DRM và mã hóa) trong quá trình đóng gói.
