# 11. DRM (디지털 저작권 관리, Digital Rights Management)

## 학습 목표 (Mục tiêu)
- Định nghĩa Quản lý bản quyền kỹ thuật số (DRM - Digital Rights Management) và mục đích bảo vệ quyền tác giả, ngăn chặn hành vi sao chép lậu và quản trị giấy phép sử dụng nội dung số.
- Nằm lòng 6 thành phần kiến trúc cốt lõi của hệ thống DRM: 클리어링 하우스 (Clearing House), 콘텐츠 제공자 (Contents Provider), 패키저 (Packager), 콘텐츠 분배자 (Distributor), DRM 컨트롤러 (Controller) và 보안 컨테이너 (Security Container).
- Phân biệt các công nghệ nền tảng cấu thành giải pháp DRM: Mã hóa, Quản lý khóa, Hệ thống định danh (DOI, URI), Ngôn ngữ biểu diễn quyền (XrML) và Công nghệ chống bẻ khóa (Tamper Resistance).

## 핵심 키워드 (Từ khóa)
- 디지털 저작권 관리 (Digital Rights Management - DRM)
- 클리어링 하우스 (Clearing House / 권한·결제 관리)
- 패키저 (Packager / 암호화 및 서명)
- 콘텐츠 분배자 (Distributor)
- DRM 컨트롤러 (DRM Controller / 이용 권한 통제)
- 보안 컨테이너 (Security Container)
- 식별체계 (DOI, URI) & 저작권 표현 (XrML)
- 크랙 방지 (Tamper Resistance)

## 선행·연결 개념 (Kiến thức liên kết)
- [41-bai-hoc.md](41-bai-hoc.md): Đóng gói phần mềm và tích hợp bảo mật bản quyền.
- [43-bai-hoc.md](43-bai-hoc.md): Chi tiết quy trình đóng gói nội dung số DRM.
- [51-bai-hoc.md](51-bai-hoc.md): Phân tích chuyên sâu về Luật bản quyền và các kỹ thuật DRM nâng cao.

## 읽는 방법 (Cách đọc)
- Nhớ vai trò 2 nhân vật then chốt trong các câu hỏi thi trắc nghiệm:
  - **Packager (패키저):** Người "khóa cửa" $\rightarrow$ Thực hiện **Mã hóa nội dung (암호화)** và nhúng chữ ký số.
  - **Clearing House (클리어링 하우스):** Người "giữ chìa khóa và thu tiền" $\rightarrow$ Quản lý thanh toán và **Cấp phát giấy phép (라이선스 발급)** để mở khóa.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bản chất của DRM (Digital Rights Management):**
  - Là giải pháp công nghệ toàn diện nhằm bảo vệ quyền tác giả đối với các tài sản số (Phần mềm, Video, Âm nhạc, Sách điện tử), kiểm soát việc truy cập, ngăn chặn sao chép trái phép và quản lý việc thanh toán phí bản quyền trong suốt vòng đời phân phối.
- **Bảng 6 thành phần cấu trúc cốt lõi của hệ thống DRM:**

| Thành phần DRM | Tên tiếng Hàn & Anh | Vai trò và nhiệm vụ kỹ thuật chi tiết |
| :--- | :--- | :--- |
| **Trung tâm thanh toán bản quyền** | **클리어링 하우스 (Clearing House)** | Quản lý bản quyền, xác thực thanh toán tiền bản quyền, **cấp phát giấy phép sử dụng (라이선스 발급)** và quản lý chính sách thanh toán theo thời gian/lưu lượng (종량제) |
| **Nhà cung cấp nội dung** | **콘텐츠 제공자 (Contents Provider)** | Tác giả hoặc chủ sở hữu bản quyền hợp pháp tạo ra nội dung số ban đầu |
| **Bộ phận đóng gói** | **패키저 (Packager)** | **Thực hiện mã hóa nội dung**, nhúng siêu dữ liệu và chữ ký điện tử của tác giả, sau đó đóng gói vào thùng chứa an toàn |
| **Nhà phân phối** | **콘텐츠 분배자 (Distributor)** | Kênh bán lẻ trực tuyến, sàn thương mại điện tử hoặc cổng thông tin hiển thị nội dung và cung cấp tệp đã đóng gói cho người dùng tải về |
| **Bộ điều khiển DRM** | **DRM 컨트롤러 (DRM Controller)** | Phần mềm cài đặt trên thiết bị của người dùng cuối, có nhiệm vụ liên hệ với Clearing House để lấy License, giải mã nội dung và kiểm soát quyền xem/in/nghe |
| **Thùng chứa bảo mật** | **보안 컨테이너 (Security Container)** | Vỏ bọc an toàn được mã hóa bao bọc lấy nội dung số để bảo vệ dữ liệu nguyên vẹn trong quá trình phân phối trên Internet |

- **Bảng các công nghệ cấu thành DRM:**
  - **암호화 및 키 관리 (Encryption & Key Management):** Dùng mã hóa đối xứng (như AES) để khóa nội dung và mã hóa bất đối xứng (như RSA) để truyền khóa giải mã an toàn.
  - **식별체계 (Identification):** Gán mã định danh duy nhất toàn cầu như **DOI (Digital Object Identifier)** hoặc **URI**.
  - **저작권 표현 (Right Expression):** Sử dụng các ngôn ngữ chuẩn hóa như **XrML (eXtensible rights Markup Language)** hoặc ODRL để định nghĩa các quy tắc bản quyền (ví dụ: chỉ cho xem 3 lần, không được in ra giấy).
  - **크랙 방지 (Tamper Resistance / Anti-tampering):** Kỹ thuật xáo trộn mã (Obfuscation), phát hiện Debugger để chống lại việc bẻ khóa phần mềm.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mô hình hoạt động thực tế (Ví dụ Netflix / Spotify):**
  - Khi xem phim trên Netflix:
    1. Phim đã được **Packager** mã hóa và lưu trên máy chủ CDN.
    2. Ứng dụng Netflix trên TV đóng vai trò là **DRM Controller**.
    3. Khi bấm Play, DRM Controller gửi thông tin tài khoản đến máy chủ **Clearing House**.
    4. Nếu đã đóng tiền thuê bao tháng, Clearing House trả về License giải mã tạm thời trong RAM. Phim chạy mượt mà nhưng người dùng không thể bấm quay lại màn hình hay sao chép tệp phim ra ngoài.

### 복습 체크리스트
- [ ] Phân biệt rõ nhiệm vụ của Packager (Mã hóa) và Clearing House (Cấp License).
- [ ] Kể đủ 6 thành phần của hệ thống DRM.
- [ ] Nhớ tên ngôn ngữ biểu diễn quyền bản quyền chuẩn hóa là XrML.
- [ ] Hiểu vai trò của công nghệ chống bẻ khóa Tamper Resistance.
