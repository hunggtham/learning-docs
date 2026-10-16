# 11. Đóng gói phần mềm, DRM và tài liệu phát hành (소프트웨어 패키징 및 저작권 관리)

## 1. Tổng quan về Đóng gói phần mềm (소프트웨어 패키징 개요)

Sau khi hoàn thành các giai đoạn thiết kế, lập trình và kiểm thử, sản phẩm phần mềm phải được đóng gói thành một bộ cài đặt hoàn chỉnh để chuyển giao đến tay người dùng cuối. 

**소프트웨어 패키징 (Software Packaging - Đóng gói phần mềm)** là quá trình tích hợp mã nguồn đã biên dịch (Binary/Executable), tệp tài nguyên (Resource), thư viện liên kết và tệp cấu hình môi trường thành một gói cài đặt độc lập, có thể vận hành ổn định trên thiết bị của người dùng.

### 1.1. 4 nguyên tắc vàng trong đóng gói phần mềm

1. **Lấy người dùng làm trung tâm (사용자 중심):** Giao diện trình cài đặt trực quan, thao tác đơn giản, thông báo rõ ràng về các bước thiết lập và tiến trình sao chép tệp.
2. **Mô-đun hóa (모듈화):** Tách biệt các thành phần cốt lõi và các tiện ích mở rộng (Plugin/Add-on) để tạo điều kiện thuận lợi cho việc vá lỗi, nâng cấp một phần mà không cần cài lại toàn bộ hệ thống.
3. **Bảo mật và Quản lý bản quyền (보안 및 저작권 관리):** Tích hợp công nghệ bảo vệ bản quyền số (**DRM**), mã hóa các tệp cấu hình và mã nguồn nhạy cảm để ngăn chặn hành vi dịch ngược (Reverse Engineering) và sao chép lậu.
4. **Tính thích ứng môi trường (환경 적합성):** Đảm bảo gói cài đặt tương thích tối ưu với các nền tảng hệ điều hành mục tiêu, tự động kiểm tra cấu hình phần cứng tối thiểu (CPU, RAM, ổ đĩa) trước khi thực thi.

---

## 2. Quy trình đóng gói phần mềm chuẩn 7 bước (패키징 순서)

Đề thi Kỹ sư xử lý thông tin thường xuyên yêu cầu sắp xếp thứ tự hoặc nhận diện công việc cốt lõi của từng bước trong chuỗi 7 giai đoạn đóng gói:

```
[1. 기능 식별] ──► [2. 모듈화] ──► [3. 빌드 진행] ──► [4. 사용자 환경 분석]
                                                              │
[7. 배포]     ◄── [6. 패키징 변경 개선] ◄── [5. 패키징 및 적용 시험] ◄┘
```

| Bước | Tên tiếng Hàn (English) | Nội dung công việc trọng tâm |
| :--- | :--- | :--- |
| **1** | **기능 식별 (Feature Identification)** | Rà soát và xác định danh sách các tính năng, module đã hoàn thiện kiểm thử và được phê duyệt đưa vào phiên bản phát hành |
| **2** | **모듈화 (Modularization)** | Tổ chức cấu trúc mã nguồn và tài nguyên thành các module độc lập theo chức năng nhằm tối ưu hóa việc quản lý và cập nhật |
| **3** | **빌드 진행 (Build Execution)** | Sử dụng công cụ tự động hóa build (Ant, Maven, Gradle) biên dịch mã nguồn, kiểm tra phụ thuộc và tạo file thực thi/nén (`.jar`, `.war`, `.exe`) |
| **4** | **사용자 환경 분석 (User Environment Analysis)** | Xác định cấu hình phần cứng tối thiểu, phiên bản hệ điều hành đích, môi trường thực thi (JRE, .NET Runtime) và các thư viện hệ thống cần thiết |
| **5** | **패키징 및 적용 시험 (Packaging & Testing)** | Tạo bộ cài đặt (Installer), thiết lập quy trình giải nén và kiểm thử thử nghiệm cài đặt trực tiếp trên môi trường ảo hóa mô phỏng người dùng |
| **6** | **패키징 변경 개선 (Packaging Modification & Improvement)** | Ghi nhận các lỗi phát sinh trong quá trình thử nghiệm cài đặt (xung đột file, thiếu quyền Admin, lỗi Registry) để tinh chỉnh bộ cài |
| **7** | **배포 (Deployment & Distribution)** | Phát hành gói cài đặt chính thức kèm tài liệu hướng dẫn và mã cấp phép (License Key) qua các kênh phân phối |

### Các điểm cần lưu ý khi thiết kế bộ cài đặt (패키징 고려사항)
- **Quy trình gỡ cài đặt (삭제 / Uninstall):** Bắt buộc phải có chức năng gỡ bỏ sạch sẽ, khôi phục lại trạng thái ban đầu của hệ điều hành (xóa tệp tạm, dọn dẹp Registry/Service, không để lại tệp rác).
- **Đồng bộ hóa giao diện (UI 일치):** Tất cả ảnh chụp màn hình trong tài liệu hướng dẫn cài đặt phải khớp 100% với giao diện thực tế của trình cài đặt.
- **Tối ưu hóa dung lượng (용량 최적화):** Nén dữ liệu hợp lý để giảm thời gian tải xuống qua mạng mà không làm giảm hiệu năng giải nén.

---

## 3. Bản quyền phần mềm và Công nghệ DRM (디지털 저작권 관리)

Phần mềm là tài sản trí tuệ được pháp luật bảo hộ theo cơ chế **소프트웨어 저작권 (Software Copyright - Quyền tác giả phần mềm)**: quyền mang tính bài trừ và độc quyền (**배타적 독점적 권리**) của tác giả sáng tạo ra phần mềm. Để hiện thực hóa việc bảo vệ bản quyền trên không gian số, các nhà phát triển sử dụng công nghệ DRM.

### 3.1. 6 thành phần kiến trúc DRM (DRM 구성 요소)

Hệ thống quản lý bản quyền kỹ thuật số (**DRM - Digital Rights Management**) vận hành dựa trên sự phối hợp của 6 thực thể kỹ thuật:

```
                  ┌─────────────────────────────────────────┐
                  │    클리어링 하우스 (Clearing House)       │
                  │   - Quản trị bản quyền / Cấp License     │
                  │   - Tính cước theo mức sử dụng (종량제)   │
                  └──────────▲───────────────────▲──────────┘
                             │                   │ Xác thực & Cấp khóa
        Đăng ký chính sách   │                   │ (License Issue)
                             │                   ▼
┌──────────────────┐    ┌─────────────┐    ┌─────────────────┐    ┌────────────────┐
│ 콘텐츠 제공자     ├───►│  패키저      ├───►│  콘텐츠 분배자   ├───►│ DRM 컨트롤러   │
│(Contents Provider)│    │ (Packager)  │    │  (Distributor)  │    │  (Controller)  │
└──────────────────┘    └──────┬──────┘    └─────────────────┘    └───────┬────────┘
                               │                                          │
                               ▼                                          ▼
                      ┌────────────────────────────────────────────────────────┐
                      │              보안 컨테이너 (Security Container)          │
                      │         (Vỏ bọc mã hóa an toàn chứa nội dung số)       │
                      └────────────────────────────────────────────────────────┘
```

| Thành phần DRM | Tên tiếng Anh | Vai trò kỹ thuật cốt lõi trong đề thi |
| :--- | :--- | :--- |
| **클리어링 하우스** | **Clearing House** | Trung tâm quản trị bản quyền, cấp phát chứng nhận số và License; thực hiện tính cước theo mức tiêu thụ (**종량제 청구**) |
| **콘텐츠 제공자** | **Contents Provider** | Tác giả hoặc đơn vị nắm giữ nội dung gốc tạo ra tài nguyên số |
| **패키저** | **Packager** | Công cụ mã hóa nội dung bằng khóa mật mã và gắn kèm siêu dữ liệu (Metadata) chứa điều kiện bản quyền |
| **콘텐츠 분배자** | **Distributor** | Kênh phân phối trực tuyến (App Store, Web Portal) cung cấp gói nội dung đã đóng gói đến người dùng |
| **DRM 컨트롤러** | **DRM Controller** | Ứng dụng/tiến trình bảo mật chạy trên máy người dùng, liên lạc với Clearing House để xác thực quyền hạn và giải mã |
| **보안 컨테이너** | **Security Container** | Vỏ bọc an toàn (vùng nhớ hoặc tệp mã hóa) ngăn chặn nội dung bị trích xuất trái phép trong quá trình phát/chạy |

### 3.2. Hai chiến lược đóng gói DRM

- **실시간 패키징 (Real-time Packaging - Đóng gói thời gian thực):** Áp dụng cho các tệp có dung lượng nhỏ (tài liệu, bản tin số). Việc mã hóa và cấp khóa được thực hiện tức thì ngay tại thời điểm người dùng gửi yêu cầu tải xuống.
- **사전 패키징 (Pre-packaging - Đóng gói trước):** Áp dụng cho các tệp có dung lượng lớn (video chất lượng cao, bộ cài game, phần mềm lớn). Toàn bộ nội dung được mã hóa sẵn từ trước và lưu trong kho phân phối; khi người dùng mua, hệ thống chỉ cấp khóa giải mã tương ứng.

### 3.3. Các công nghệ bảo mật nội dung liên quan

| Công nghệ | Cơ chế hoạt động | Mục đích sử dụng | Từ khóa nhận diện đề thi |
| :--- | :--- | :--- | :--- |
| **디지털 워터마킹 (Digital Watermarking)** | Nhúng thông tin bản quyền (logo mờ, ID tác giả) không thể xóa bỏ vào tệp đa phương tiện | Khẳng định chủ quyền, làm bằng chứng khi xảy ra tranh chấp bản quyền | **저작권 표시**, **위조 방지**, 소유권 증명 |
| **스테가노그래피 (Steganography)** | Giấu một thông điệp bí mật bên trong một bức ảnh, bài hát hoặc đoạn phim bình thường | Truyền tin mật quân sự/an ninh mà người ngoài không hề hay biết | **기밀 정보 은닉**, 암호통신 |
| **XrML** | eXtensible rights Markup Language | Ngôn ngữ chuẩn dựa trên XML dùng để mô tả chi tiết quyền sử dụng và điều kiện cấp phép nội dung số | **디지털 저작권 표현 언어**, XML 기반 |
| **DOI** | Digital Object Identifier | Chuỗi mã định danh duy nhất toàn cầu gán cho từng đối tượng số (bài báo khoa học, sách, phần mềm) | **디지털 저작물 고유 식별자** |

---

## 4. Tài liệu phát hành và hướng dẫn phần mềm (소프트웨어 문서화)

Một sản phẩm phần mềm khi đóng gói chuyển giao bắt buộc phải đi kèm với hai nhóm văn bản kỹ thuật: **Ghi chú phát hành (Release Note)** và **Tài liệu hướng dẫn (Manuals)**.

### 4.1. Ghi chú phát hành (릴리즈 노트 - Release Note)

- **Định nghĩa:** Là tài liệu chính thức chia sẻ thông tin cập nhật, cải tiến tính năng và danh sách lỗi đã khắc phục giữa nhóm phát triển và người dùng cuối/khách hàng.
- **Nguyên tắc biên soạn chuẩn thi:**
  - **Ai viết?** Do **개발팀 (Đội ngũ phát triển)** trực tiếp soạn thảo dựa trên lịch sử commit mã nguồn thực tế.
  - **Viết thế nào?** Phải viết bằng **현재 시제 (Thì hiện tại)**, ngôn từ súc tích, khách quan và chính xác.
- **Các thành phần bắt buộc trong Release Note:**
  1. **머릿말 (Header):** Tên tài liệu, tên sản phẩm, phiên bản phát hành (Version), ngày phát hành.
  2. **개요 (Overview) & 목적 (Purpose):** Tóm tắt bối cảnh và mục đích chính của bản phát hành.
  3. **문제 요약 (Issue Summary) & 재현 단계 (Reproduction Steps):** Mô tả lỗi đã được ghi nhận ở bản trước và cách tái hiện.
  4. **수정 및 개선 내용 (Bug Fixes & Enhancements):** Danh sách chi tiết các lỗi đã sửa và chức năng mới bổ sung.
  5. **사용자 영향도 (User Impact):** Ảnh hưởng của bản cập nhật đến quy trình thao tác hoặc tính tương thích ngược.
  6. **면책 조항 (Disclaimer):** Điều khoản giới hạn trách nhiệm pháp lý đối với việc cài đặt và sử dụng sai mục đích.

### 4.2. Tài liệu hướng dẫn phần mềm: 설치 매뉴얼 vs 사용자 매뉴얼

| Tiêu chí | 설치 매뉴얼 (Installation Manual) | 사용자 매뉴얼 (User Manual) |
| :--- | :--- | :--- |
| **Mục đích** | Hướng dẫn đưa phần mềm vào môi trường máy tính hoạt động | Hướng dẫn vận hành các tính năng phục vụ công việc |
| **Đối tượng** | Kỹ sư triển khai hệ thống, Quản trị viên, hoặc người dùng cài đặt | Người dùng cuối vận hành nghiệp vụ hàng ngày |
| **Nội dung bắt buộc** | - Cấu hình hệ thống tối thiểu (HW, OS, JRE)<br>- Trình tự các bước cài đặt kèm ảnh minh họa<br>- **Quy trình gỡ cài đặt sạch (삭제 / 언인스톨)**<br>- **Xử lý sự cố khi cài đặt (예외 상황)** | - Giới thiệu tổng quan giao diện và thanh menu<br>- Kịch bản thực hiện từng nghiệp vụ tuần tự<br>- Danh mục mã lỗi và cách khắc phục lỗi thao tác<br>- Câu hỏi thường gặp (FAQ) và liên hệ hỗ trợ |
| **Nguyên tắc viết** | Lấy người dùng làm trung tâm (**사용자 중심**), chi tiết từng bước, không bỏ sót bước cấu hình ban đầu | Tránh thuật ngữ kỹ thuật phức tạp, minh họa trực quan luồng thao tác thực tế |

---

## 5. Phân loại phần mềm theo quyền sở hữu và phân phối (소프트웨어의 분류)

Kỳ thi Kỹ sư xử lý thông tin phân loại phần mềm theo 6 mô hình cấp phép và phát hành bản quyền cốt lõi:

| Loại phần mềm | Tên tiếng Hàn / Anh | Đặc điểm cấp phép và chi phí | Trạng thái mã nguồn | Ví dụ thực tế |
| :--- | :--- | :--- | :--- | :--- |
| **Thương mại đóng gói** | **상용 소프트웨어 (COTS)** | Bắt buộc phải trả tiền mua bản quyền mới được phép cài đặt và sử dụng | Mã nguồn đóng (Closed Source) | Windows, MS Office, Oracle RDBMS |
| **Theo đơn đặt hàng** | **주문형 소프트웨어 (Custom / SI)** | Phát triển riêng biệt theo hợp đồng đặt hàng của doanh nghiệp cụ thể | Thuộc quyền sở hữu của bên đặt hàng theo hợp đồng | Hệ thống ERP nội bộ ngân hàng, cổng dịch vụ công |
| **Dùng thử** | **셰어웨어 (Shareware)** | Miễn phí dùng thử trong thời hạn quy định (Trial 30 ngày) hoặc bị khóa tính năng nâng cao; phải trả phí để dùng tiếp | Mã nguồn đóng | WinRAR, IDM |
| **Miễn phí** | **프리웨어 (Freeware)** | Miễn phí hoàn toàn cho mọi mục đích cá nhân mà không cần trả tiền | Mã nguồn đóng (không mở mã nguồn) | Adobe Acrobat Reader, Google Chrome |
| **Mã nguồn mở** | **공개 소프트웨어 (OSS)** | Tự do sử dụng, chỉnh sửa và phân phối lại theo điều khoản giấy phép (GPL, Apache, MIT) | Mã nguồn mở hoàn toàn (Open Source) | Linux, Apache HTTP Server, MySQL |
| **Miền công cộng** | **공용 소프트웨어 (Public Domain)** | Tác giả từ bỏ hoàn toàn quyền sở hữu trí tuệ hoặc bản quyền đã hết hạn bảo hộ | Tự do không ràng buộc bất kỳ điều kiện bản quyền nào | Thuật toán cổ điển, văn bản luật |

---

## 6. Câu hỏi ôn tập và bẫy đề thi thực tế

1. **Thành phần Clearing House trong DRM:**
   - *Câu hỏi:* Trong kiến trúc DRM, thành phần nào chịu trách nhiệm quản trị bản quyền, cấp phát chứng chỉ bản quyền (License) cho người dùng và thực hiện thanh toán, tính cước theo mức sử dụng (**종량제 청구**)?
   - *Đáp án chuẩn thi:* **클리어링 하우스 (Clearing House)**.
2. **So sánh Watermarking vs Steganography:**
   - *Bẫy đề thi:* "Kỹ thuật giấu một bức thư bảo mật vào các bit dữ liệu thừa của tệp ảnh để truyền tin bí mật được gọi là Digital Watermarking." $\rightarrow$ **SAI**. Việc giấu tin mật vào tệp khác để che mắt việc truyền tin là **스테가노그래피 (Steganography)**. Watermarking là chèn thông tin bản quyền để chứng minh chủ sở hữu.
3. **Nguyên tắc soạn thảo Release Note:**
   - *Câu hỏi:* Tài liệu Release Note do ai trực tiếp viết và sử dụng thì nào trong câu văn?
   - *Đáp án chuẩn thi:* Do **개발팀 (Đội ngũ phát triển)** trực tiếp soạn thảo và viết bằng **현재 시제 (Thì hiện tại)**.
4. **Hạng mục bắt buộc trong Installation Manual:**
   - *Câu hỏi:* Yếu tố nào dưới đây là bắt buộc phải có trong bản Hướng dẫn cài đặt (설치 매뉴얼)?
   - *Đáp án chuẩn thi:* Trình tự cài đặt, xử lý lỗi ngoại lệ, và đặc biệt là **hướng dẫn gỡ bỏ cài đặt hoàn toàn (삭제 / 언인스톨 - Uninstall)**.

---

## 7. Liên kết bài học tiếp theo

Việc quản lý các phiên bản mã nguồn, tài liệu đóng gói và kiểm soát các thay đổi trong toàn bộ vòng đời phát triển đòi hỏi hệ thống Quản lý cấu hình phần mềm chuyên nghiệp. Tiếp tục với **[12-quan-ly-cau-hinh-scm-va-git.md](12-quan-ly-cau-hinh-scm-va-git.md)** để tìm hiểu quy trình SCM, đường cơ sở (Baseline) và các hệ thống kiểm soát phiên bản Git, SVN.
