# 소프트웨어 패키징 및 저작권 관리 (Đóng gói phần mềm, DRM và tài liệu phát hành)

## 학습 목표
- Nắm vững định nghĩa và 4 nguyên tắc vàng trong đóng gói phần mềm: Lấy người dùng làm trung tâm (`사용자 중심`), Mô-đun hóa (`모듈화`), Bảo mật và quản lý bản quyền (`보안 및 저작권 관리`), và Tính thích ứng môi trường (`환경 적합성`).
- Thuộc nằm lòng quy trình 7 bước đóng gói phần mềm chuẩn: 기능 식별 $\rightarrow$ 모듈화 $\rightarrow$ 빌드 진행 $\rightarrow$ 사용자 환경 분석 $\rightarrow$ 패키징 및 적용 시험 $\rightarrow$ 패키징 변경 개선 $\rightarrow$ 배포.
- Phân tích vai trò của 6 thành phần kiến trúc DRM: Clearing House (`클리어링 하우스` - cấp License và tính cước theo mức sử dụng), Contents Provider, Packager, Distributor, DRM Controller, và Security Container.
- Phân biệt các công nghệ bảo vệ nội dung số: Digital Watermarking (`디지털 워터마킹` - khẳng định quyền sở hữu), Steganography (`스테가노그래피` - giấu tin mật), XrML, và mã định danh DOI.
- Nắm vững nguyên tắc soạn thảo Ghi chú phát hành (`릴리즈 노트 / Release Note` - do Dev viết bằng thì hiện tại) và phân biệt 6 loại phần mềm theo quyền tác giả (상용, 주문형, 셰어웨어, 프리웨어, 공개, 공용).

## 핵심 키워드
- 소프트웨어 패키징 (Đóng gói phần mềm / Software Packaging / 빌드 진행, 배포)
- DRM 구성 요소 (Clearing House 클리어링 하우스 종량제 청구, Packager, DRM Controller, Security Container)
- 저작권 보안 기술 (디지털 워터마킹 Watermarking, 스테가노그래피 Steganography, XrML, DOI)
- 릴리즈 노트 (Release Note / 개발팀 작성 / 현재 시제 사용)
- 소프트웨어 분류 (상용 COTS, 주문형 Custom, 셰어웨어 Shareware, 프리웨어 Freeware, 공개 OSS, 공용 Public Domain)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [10-bao-mat-giao-dien-va-kiem-chung.md](10-bao-mat-giao-dien-va-kiem-chung.md), chúng ta đã hoàn tất việc bảo vệ các giao diện API và kiểm chứng độ chính xác trước khi đưa vào sản xuất.
- **Đang giải quyết gì (Current Problem):** Bài học này giải quyết việc đóng gói toàn bộ mã nguồn nhị phân, tài nguyên và cấu hình thành một bộ cài đặt hoàn chỉnh chuyển giao cho người dùng cuối, đồng thời thiết lập lá chắn bảo vệ bản quyền số DRM và chuẩn bị tài liệu kỹ thuật phát hành.
- **Dùng đi đâu (Forward Handoff):** Khi phần mềm được phát hành qua nhiều phiên bản liên tục, việc kiểm soát mã nguồn và tài liệu đóng gói đòi hỏi quy trình Quản lý cấu hình phần mềm tại [12-quan-ly-cau-hinh-scm-va-git.md](12-quan-ly-cau-hinh-scm-va-git.md).

## 읽는 방법
- Đọc TẦNG A để thuộc lòng vai trò của Clearing House (종량제 청구), phân biệt Watermarking vs Steganography, thứ tự 7 bước đóng gói và quy tắc viết Release Note bằng thì hiện tại do dev viết.
- Đọc TẦNG B để hiểu sâu sơ đồ kiến trúc 6 thực thể DRM và sự khác biệt giữa Installation Manual với User Manual.

---

## 소프트웨어 패키징 및 저작권 관리

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Quy trình đóng gói phần mềm chuẩn 7 bước
```
[1. 기능 식별] ──> [2. 모듈화] ──> [3. 빌드 진행] ──> [4. 사용자 환경 분석]
                                                               │
[7. 배포]     <── [6. 패키징 변경 개선] <── [5. 패키징 및 적용 시험] <──┘
```

| Bước | Tên tiếng Hàn & Anh | Công việc trọng tâm |
| :---: | :--- | :--- |
| **1** | **기능 식별 (Feature Identification)** | Rà soát danh sách các tính năng và module đã kiểm thử thành công |
| **2** | **모듈화 (Modularization)** | Tổ chức cấu trúc mã nguồn thành các module chức năng độc lập |
| **3** | **빌드 진행 (Build Execution)** | Biên dịch mã nguồn và tạo tệp thực thi qua công cụ tự động (Ant, Maven, Gradle) |
| **4** | **사용자 환경 분석 (Environment Analysis)** | Xác định cấu hình phần cứng tối thiểu, hệ điều hành đích, JRE, runtime |
| **5** | **패키징 및 적용 시험 (Packaging & Testing)** | Tạo bộ cài đặt Installer và kiểm thử cài đặt trên môi trường ảo hóa |
| **6** | **패키징 변경 개선 (Modification)** | Khắc phục xung đột quyền hạn, sửa đổi registry phát hiện trong khi thử nghiệm |
| **7** | **배포 (Deployment)** | Phát hành chính thức gói cài đặt kèm License Key và tài liệu hướng dẫn |

#### 2. Bảng 6 thành phần kiến trúc DRM
| Thành phần | Tên tiếng Anh | Vai trò kỹ thuật cốt lõi trong đề thi |
| :--- | :--- | :--- |
| **클리어링 하우스** | **Clearing House** | Trung tâm quản trị bản quyền, cấp License; **tính cước theo mức tiêu thụ (종량제 청구)** |
| **콘텐츠 제공자** | **Contents Provider** | Tác giả hoặc đơn vị nắm giữ bản quyền tạo ra tài nguyên số gốc |
| **패키저** | **Packager** | Mã hóa nội dung số và gắn kèm Metadata chứa điều kiện bản quyền |
| **콘텐츠 분배자** | **Distributor** | Kênh phân phối trực tuyến (App Store, Web Portal) cung cấp gói cài đặt |
| **DRM 컨트롤러** | **DRM Controller** | Tiến trình bảo mật trên máy người dùng, liên lạc với Clearing House để giải mã |
| **보안 컨테이너** | **Security Container** | Vỏ bọc an toàn ngăn chặn nội dung bị trích xuất trái phép trong khi chạy |

#### 3. Bảng công nghệ bảo mật nội dung số
| Công nghệ | Cơ chế hoạt động | Mục đích sử dụng | Từ khóa nhận diện đề thi |
| :--- | :--- | :--- | :--- |
| **디지털 워터마킹 (Watermarking)** | Nhúng thông tin bản quyền (logo mờ, ID tác giả) không thể xóa vào tệp | Khẳng định chủ quyền, làm bằng chứng khi tranh chấp | **저작권 표시**, **위조 방지**, 소유권 증명 |
| **스테가노그래피 (Steganography)** | Giấu thông điệp bí mật vào trong một bức ảnh hoặc bài hát bình thường | Truyền tin mật mà người ngoài không hề hay biết | **기밀 정보 은닉**, 암호통신 |
| **XrML** | Ngôn ngữ XML mô tả chi tiết quyền sử dụng và cấp phép nội dung số | Tiêu chuẩn hóa điều kiện bản quyền | **디지털 저작권 표현 언어**, XML 기반 |
| **DOI** | Chuỗi mã định danh duy nhất toàn cầu gán cho từng đối tượng số | Quản lý bản quyền tài sản số | **디지털 저작물 고유 식별자** |

#### 4. Phân loại 6 mô hình phần mềm theo bản quyền
| Loại phần mềm | Tên tiếng Hàn & Anh | Đặc điểm cấp phép & mã nguồn | Ví dụ thực tế |
| :--- | :--- | :--- | :--- |
| **Thương mại đóng gói** | **상용 소프트웨어 (COTS)** | Trả tiền mua bản quyền mới được dùng; mã nguồn đóng | Windows, MS Office, Oracle |
| **Theo đơn đặt hàng** | **주문형 소프트웨어 (Custom)** | Phát triển riêng theo hợp đồng; thuộc quyền bên đặt hàng | ERP nội bộ ngân hàng |
| **Dùng thử** | **셰어웨어 (Shareware)** | Dùng thử có thời hạn (Trial 30 ngày) hoặc khóa tính năng; mã nguồn đóng | WinRAR, IDM |
| **Miễn phí** | **프리웨어 (Freeware)** | Miễn phí hoàn toàn cho cá nhân; không mở mã nguồn | Adobe Reader, Chrome |
| **Mã nguồn mở** | **공개 소프트웨어 (OSS)** | Tự do sử dụng, sửa đổi và phân phối lại; mã nguồn mở | Linux, Apache, MySQL |
| **Miền công cộng** | **공용 소프트웨어 (Public Domain)** | Tác giả từ bỏ sở hữu trí tuệ hoặc hết hạn bảo hộ | Thuật toán cổ điển |

#### 5. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Clearing House trong DRM:** Thành phần chịu trách nhiệm quản lý chứng nhận bản quyền và tính cước theo mức sử dụng (`종량제 청구`) là **클리어링 하우스 (Clearing House)**.
- **Bẫy 2: Watermarking vs Steganography:**
  - Nhúng logo mờ để chứng minh quyền sở hữu $\rightarrow$ **디지털 워터마킹 (Digital Watermarking)**.
  - Giấu thông điệp bí mật vào bức ảnh để truyền tin mật $\rightarrow$ **스테가노그래피 (Steganography)**.
- **Bẫy 3: Biên soạn Release Note:** Phải do **개발팀 (Đội ngũ phát triển)** viết bằng **현재 시제 (Thì hiện tại)**.
- **Bẫy 4: Yếu tố bắt buộc trong Installation Manual:** Phải có hướng dẫn **quy trình gỡ bỏ cài đặt sạch sẽ (`삭제 / 언인스톨 - Uninstall`)**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Chiến lược đóng gói DRM
- **실시간 패키징 (Real-time Packaging):** Áp dụng cho tệp nhỏ (tài liệu, bản tin số). Việc mã hóa và cấp khóa diễn ra tức thời ngay khi người dùng bấm tải xuống.
- **사전 패키징 (Pre-packaging):** Áp dụng cho tệp lớn (video chất lượng cao, bộ cài game). Nội dung được mã hóa sẵn từ trước và lưu trong kho; khi mua chỉ cấp thêm khóa giải mã.

#### 2. Cấu trúc bản Ghi chú phát hành (Release Note)
1. `머릿말 (Header)`: Tên tài liệu, tên sản phẩm, phiên bản (Version), ngày phát hành.
2. `개요 (Overview) & 목적 (Purpose)`: Tóm tắt bối cảnh và mục đích chính của bản phát hành.
3. `문제 요약 & 재현 단계`: Mô tả lỗi đã được ghi nhận ở bản trước và các bước tái hiện.
4. `수정 및 개선 내용 (Bug Fixes)`: Chi tiết các lỗi đã sửa và tính năng mới bổ sung.
5. `사용자 영향도 (User Impact)`: Ảnh hưởng của bản cập nhật đến quy trình thao tác và tính tương thích ngược.
6. `면책 조항 (Disclaimer)`: Điều khoản giới hạn trách nhiệm pháp lý.

---

### 복습 체크리스트
- [ ] Thuộc lòng 4 nguyên tắc đóng gói: 사용자 중심, 모듈화, 보안 및 저작권 관리, 환경 적합성.
- [ ] Nắm chắc thứ tự 7 bước đóng gói: 기능 식별 $\rightarrow$ 모듈화 $\rightarrow$ 빌드 $\rightarrow$ 환경 분석 $\rightarrow$ 시험 $\rightarrow$ 개선 $\rightarrow$ 배포.
- [ ] Kể tên 6 thành phần DRM và nhớ Clearing House là đơn vị quản lý bản quyền và tính cước 종량제.
- [ ] Phân biệt được Digital Watermarking (chứng minh sở hữu) và Steganography (giấu tin mật).
- [ ] Nhớ XrML là ngôn ngữ XML mô tả quyền tác giả, DOI là mã định danh số toàn cầu.
- [ ] Ghi nhớ Release Note do Dev viết bằng thì hiện tại; Installation Manual bắt buộc phải có hướng dẫn Uninstall.
- [ ] Phân loại 6 nhóm phần mềm: COTS, Custom, Shareware, Freeware, OSS, Public Domain.
