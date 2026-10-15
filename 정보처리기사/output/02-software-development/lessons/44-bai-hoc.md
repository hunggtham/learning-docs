# 099: 소프트웨어 패키징 (Software Packaging)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và mục đích cốt lõi của quá trình Đóng gói phần mềm (소프트웨어 패키징 - Software Packaging).
- Nằm lòng 4 nguyên tắc vàng trong đóng gói phần mềm thương mại: Lấy người dùng làm trung tâm (사용자 중심), Mô-đun hóa (모듈화), Bảo mật và Bản quyền (보안 및 DRM), và Tính tương thích môi trường (환경 적합성).
- Hiểu rõ sự chuyển biến từ sản phẩm phần mềm của lập trình viên sang sản phẩm thương phẩm hoàn chỉnh bàn giao cho khách hàng.

## 핵심 키워드 (Từ khóa)
- 소프트웨어 패키징 (Software Packaging)
- 배포용 설치 파일 (Deployment Installer / Setup)
- 사용자 중심 (User-centric Principle)
- 모듈화 (Modularization / Patch Update)
- 보안 및 암호화 (Security & Encryption)
- 환경 적합성 (Environment Compatibility)

## 선행·연결 개념 (Kiến thức liên kết)
- [41-bai-hoc.md](41-bai-hoc.md): Sổ tay cài đặt và gỡ cài đặt phần mềm.
- [42-bai-hoc.md](42-bai-hoc.md): Các yếu tố kỹ thuật cần xem xét khi đóng gói.
- [45-bai-hoc.md](45-bai-hoc.md): Trình tự 7 bước đóng gói phần mềm chi tiết.

## 읽는 방법 (Cách đọc)
- Cứ thấy đề thi hỏi: **"실행 파일들을 묶어 배포용 설치 파일을 만드는 과정은?"** (Quá trình gom các tệp thực thi lại thành tệp cài đặt để phát hành) $\rightarrow$ Khẳng định ngay **소프트웨어 패키징 (Software Packaging)**.
- Ghi nhớ 2 tiêu chuẩn thiết kế: Dễ dùng cho người không chuyên (사용자 중심) và Dễ sửa từng phần khi có lỗi (모듈화).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Khái niệm Đóng gói phần mềm (소프트웨어 패키징):**
  - Là giai đoạn cuối cùng trong quy trình phát triển sản phẩm, tập hợp toàn bộ các tệp thực thi nhị phân, các thư viện liên kết động, các tệp âm thanh, đồ họa, dữ liệu mẫu và tệp cấu hình môi trường để đóng gói thành một bộ cài đặt duy nhất (như `.msi`, `.exe`, `.dmg`, `.deb`).
- **4 nguyên tắc thiết kế đóng gói sản phẩm phần mềm:**
  1. **사용자 중심 (Lấy người dùng làm trung tâm):**
     - Thiết kế trình cài đặt với giao diện đồ họa thân thiện (Wizard GUI).
     - Tối giản hóa các thao tác lựa chọn phức tạp, cung cấp chế độ cài đặt nhanh (Express / Default Setup) cho người dùng phổ thông.
  2. **모듈화 (Mô-đun hóa cao):**
     - Các chức năng độc lập phải được phân chia thành các tệp thư viện hoặc gói con riêng biệt.
     - Khi nâng cấp phiên bản hoặc sửa lỗi, hệ thống chỉ cần tải về và cập nhật đúng mô-đun bị lỗi (Hotfix / Patch) mà không bắt buộc người dùng phải gỡ ra cài lại toàn bộ chương trình từ đầu.
  3. **보안 및 암호화 연동 (Tích hợp an ninh và bản quyền):**
     - Áp dụng các thuật toán mã hóa đối xứng và bất đối xứng để bảo vệ mã nguồn nhị phân chống dịch ngược (Decompilation).
     - Tích hợp công nghệ bảo vệ bản quyền DRM để ngăn chặn việc sao chép lậu và chia sẻ trái phép.
  4. **다양한 환경 지원 (Hỗ trợ đa môi trường):**
     - Bảo đảm gói cài đặt có thể tự động kiểm tra và thích ứng với nhiều phiên bản hệ điều hành khác nhau, kiến trúc phần cứng khác nhau (x86, x64, ARM).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Công cụ đóng gói phần mềm phổ biến trong ngành:**
  - Trên môi trường Windows: **InstallShield**, **Inno Setup**, **NSIS (Nullsoft Scriptable Install System)**, **WiX Toolset**.
  - Trên môi trường di động: **APK** / **AAB (Android App Bundle)** cho Android, **IPA** cho iOS.
  - Trên môi trường Linux: **RPM**, **DEB**, **Snap**, **Flatpak**.

### 복습 체크리스트
- [ ] Định nghĩa đóng gói phần mềm là tạo bộ cài đặt hoàn chỉnh từ các tệp thực thi.
- [ ] Nhớ nguyên tắc 사용자 중심: Dễ cài đặt cho người dùng cuối không am hiểu công nghệ.
- [ ] Nhớ nguyên tắc 모듈화: Giúp cập nhật bản vá Patch dễ dàng mà không cài lại toàn bộ.
- [ ] Kể tên các yêu cầu an ninh: Mã hóa, chống dịch ngược và tích hợp DRM.
