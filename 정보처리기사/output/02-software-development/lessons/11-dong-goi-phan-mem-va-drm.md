# 소프트웨어 패키징 및 저작권 관리 (Đóng gói phần mềm và DRM)

## 학습 목표
- Nắm vững định nghĩa Đóng gói phần mềm (`소프트웨어 패키징 / Software Packaging`) và 4 nguyên tắc vàng: Lấy người dùng làm trung tâm (`사용자 중심`), Mô-đun hóa (`모듈화`), Bảo mật và Quản lý bản quyền (`보안 및 저작권 관리`), và Tính thích ứng môi trường (`환경 적합성`).
- Thuộc lòng quy trình đóng gói phần mềm chuẩn 7 bước: Nhận diện tính năng $\rightarrow$ Mô-đun hóa $\rightarrow$ Thực hiện Build $\rightarrow$ Phân tích môi trường người dùng $\rightarrow$ Đóng gói & Thử nghiệm $\rightarrow$ Cải tiến thay đổi $\rightarrow$ Phát hành.
- Phân tích kiến trúc hệ thống quản trị bản quyền số (`DRM / Digital Rights Management`) gồm 6 thành phần kỹ thuật: Clearing House (`클리어링 하우스`), Contents Creator (`콘텐츠 제공자`), Contents Distributor (`콘텐츠 분배자`), Packager (`패키저`), Security Container (`보안 컨테이너`), và DRM Controller (`DRM 컨트롤러`).
- Nắm vững 5 công nghệ kỹ thuật cốt lõi trong DRM: Mã hóa (`암호화`), Thủy vân số (`워터마킹 / Watermarking`), Chống giả mạo can thiệp (`크랙 방지 / Tamper-proofing`), Quản lý khóa mật mã (`키 관리`), và Quản lý chính sách bản quyền (`정책 관리`).
- Nắm vững các thành phần cấu thành tài liệu Ghi chú phát hành (`릴리즈 노트 / Release Notes`) và Hướng dẫn sử dụng (`매뉴얼 / Manual`).

## 핵심 키워드
- 소프트웨어 패키징 (Đóng gói phần mềm / Software Packaging)
- 패키징 7단계 (Feature ID, Modularization, Build, User Environment, Testing, Improvement, Deployment)
- DRM (Digital Rights Management / 디지털 저작권 관리)
- DRM 6대 구성 요소 (Clearing House, Creator, Distributor, Packager, Security Container, DRM Controller)
- 워터마킹 & 핑거프린팅 (Watermarking bản quyền vs Fingerprinting truy vết người mua)
- 크랙 방지 (Tamper-proofing / 역공학 방지)
- 릴리즈 노트 (Release Notes / 버전 정보, 수정 내역)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [10-bao-mat-giao-dien-va-kiem-chung.md](10-bao-mat-giao-dien-va-kiem-chung.md), chúng ta đã bảo vệ an toàn các kênh giao diện truyền thông và kiểm thử tự động.
- **Đang giải quyết gì (Current Problem):** Bài học này chuyển giao sản phẩm từ môi trường phát triển sang môi trường người dùng, giải quyết bài toán tích hợp các thành phần thành bộ cài đặt hoàn chỉnh và bảo vệ tài sản trí tuệ thông qua công nghệ bản quyền số DRM.
- **Dùng đi đâu (Forward Handoff):** Sau khi phần mềm được đóng gói và phát hành, các phiên bản sẽ liên tục thay đổi. Bài học tiếp theo [12-quan-ly-cau-hinh-scm-va-git.md](12-quan-ly-cau-hinh-scm-va-git.md) sẽ khảo sát quy trình quản lý cấu hình SCM và công cụ Git/SVN.

## 읽는 방법
- Đọc TẦNG A để thuộc lòng bảng 7 bước đóng gói phần mềm, bảng 6 thành phần DRM, bảng phân biệt Watermarking vs Fingerprinting và các bẫy trắc nghiệm.
- Đọc TẦNG B để theo dõi sơ đồ ASCII luồng vận hành DRM giữa Clearing House và các bên liên quan, các lưu ý khi thiết kế bộ cài đặt gỡ bỏ Uninstall.

---

## 소프트웨어 패키징 및 저작권 관리

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng quy trình đóng gói phần mềm chuẩn 7 bước
```
[1. 기능 식별] ──► [2. 모듈화] ──► [3. 빌드 진행] ──► [4. 사용자 환경 분석]
                                                              │
[7. 배포]     ◄── [6. 패키징 변경 개선] ◄── [5. 패키징 및 적용 시험] ◄┘
```

| Bước | Tên tiếng Hàn (English) | Nội dung công việc trọng tâm |
| :---: | :--- | :--- |
| **1** | **기능 식별 (Feature ID)** | Xác định danh sách các tính năng đã kiểm thử đạt chuẩn đưa vào bản phát hành |
| **2** | **모듈화 (Modularization)** | Tổ chức cấu trúc mã nguồn thành các module độc lập theo chức năng |
| **3** | **빌드 진행 (Build Execution)** | Dùng công cụ build (Maven, Gradle) biên dịch và đóng gói thành file `.jar`, `.exe` |
| **4** | **사용자 환경 분석 (User Environment)** | Xác định cấu hình phần cứng tối thiểu, hệ điều hành đích, môi trường runtime JRE/.NET |
| **5** | **패키징 및 적용 시험 (Testing)** | Tạo bộ cài đặt Installer, thử nghiệm cài đặt trên môi trường ảo hóa mô phỏng |
| **6** | **패키징 변경 개선 (Improvement)** | Khắc phục các lỗi phát sinh khi cài đặt (xung đột file, quyền Admin, Registry) |
| **7** | **배포 (Deployment)** | Phát hành gói cài đặt chính thức kèm tài liệu hướng dẫn và mã License Key |

#### 2. Bảng 6 thành phần kiến trúc hệ thống DRM
| Thành phần DRM | Tên tiếng Hàn & Anh | Vai trò và chức năng kỹ thuật cốt lõi |
| :--- | :--- | :--- |
| **Clearing House** | **클리어링 하우스** | **Cơ quan cấp phép trung tâm**: Quản trị bản quyền, cấp giấy phép (License), giải mã khóa, tính cước theo mức sử dụng (종량제) |
| **Contents Creator** | **콘텐츠 제공자** | Tác giả hoặc nhà sản xuất sáng tạo ra nội dung số gốc |
| **Contents Distributor** | **콘텐츠 분배자** | Nhà phân phối cung cấp nội dung đã đóng gói đến người dùng qua Internet |
| **Packager** | **패키저** | Công cụ nén và mã hóa nội dung gốc kèm siêu dữ liệu (Metadata) bản quyền |
| **Security Container** | **보안 컨테이너** | Lớp vỏ bọc an toàn bảo vệ tệp nội dung đã mã hóa phân phối trên mạng |
| **DRM Controller** | **DRM 컨트롤러** | Module phía Client kiểm tra License, giải mã và cho phép thực thi nội dung |

#### 3. Phân biệt Thủy vân số (Watermarking) vs Điểm chỉ số (Fingerprinting)
| Tiêu chuẩn so sánh | 워터마킹 (Digital Watermarking) | 핑거프린팅 (Digital Fingerprinting) |
| :--- | :--- | :--- |
| **Dấu ấn nhúng vào** | Nhúng thông tin nhận diện của **Tác giả / Nhà sản xuất (저작권자)** | Nhúng thông tin nhận diện của **Người mua / Người dùng cuối (구매자)** |
| **Mục đích chính** | Khẳng định chủ quyền tác giả hợp pháp của sản phẩm | **Truy vết và phát hiện người đã phát tán tệp tin trái phép ra ngoài** |

#### 4. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Vai trò của Clearing House:** Khi câu hỏi đề cập đến *"Thành phần nào trong mô hình DRM chịu trách nhiệm cấp giấy phép (License), phân phối khóa giải mã và quản lý tính phí bản quyền?"* $\rightarrow$ Đáp án chắc chắn là **클리어링 하우스 (Clearing House)**.
- **Bẫy 2: Phân biệt Watermarking vs Fingerprinting:**
  - Nhúng thông tin tác giả $\rightarrow$ **워터마킹 (Watermarking)**.
  - Nhúng thông tin người mua để chống phát tán lậu $\rightarrow$ **핑거프린팅 (Fingerprinting)**.
- **Bẫy 3: Tamper-proofing (크랙 방지):** Công nghệ ngăn chặn tin tặc dịch ngược mã nguồn (Reverse Engineering) hoặc sửa đổi tệp nhị phân để vượt qua cơ chế kiểm tra License.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ luồng vận hành kiến trúc DRM (Đủ 6 thành phần)
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

#### 2. Các điểm cần lưu ý khi thiết kế bộ cài đặt (패키징 고려사항)
- **Quy trình gỡ cài đặt (삭제 / Uninstall):** Bắt buộc phải có chức năng gỡ bỏ sạch sẽ, khôi phục lại trạng thái ban đầu của hệ điều hành (xóa tệp tạm, dọn dẹp Registry/Service, không để lại tệp rác).
- **Đồng bộ hóa giao diện (UI 일치):** Tất cả ảnh chụp màn hình trong tài liệu hướng dẫn cài đặt phải khớp 100% với giao diện thực tế của trình cài đặt.
- **Tối ưu hóa dung lượng (용량 최적화):** Nén dữ liệu hợp lý để giảm thời gian tải xuống qua mạng mà không làm giảm hiệu năng giải nén.

---

### 복습 체크리스트
- [ ] Thuộc lòng thứ tự 7 bước đóng gói phần mềm từ 기능 식별 đến 배포.
- [ ] Phân biệt rõ vai trò của 6 thành phần DRM, đặc biệt là Clearing House.
- [ ] Phân biệt được Watermarking (nhúng tên tác giả) và Fingerprinting (nhúng tên người mua để truy vết).
- [ ] Nêu vai trò của công nghệ Tamper-proofing (chống dịch ngược và sửa mã).
- [ ] Liệt kê các thành phần chính trong Release Notes và Manual hướng dẫn.
