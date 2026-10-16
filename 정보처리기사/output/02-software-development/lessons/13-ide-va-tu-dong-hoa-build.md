# 통합 개발 환경과 빌드 자동화 (IDE và tự động hóa Build)

## 학습 목표
- Nắm vững 4 chức năng cốt lõi cấu thành Môi trường phát triển tích hợp (IDE): Soạn thảo mã (`코딩 / Coding`), Biên dịch (`컴파일 / Compile`), Gỡ lỗi (`디버깅 / Debugging`), và Đóng gói triển khai (`배포 / Deployment`).
- Nhận diện các công cụ IDE tiêu biểu: Eclipse, IntelliJ IDEA, Visual Studio, Xcode, và Android Studio.
- So sánh đối đầu 3 thế hệ công cụ tự động hóa build trong hệ sinh thái Java: Apache Ant (`build.xml`), Apache Maven (`pom.xml` - quản lý phụ thuộc trung tâm), và Gradle (`build.gradle` - Groovy/Kotlin DSL, Build Cache, chuẩn Android).
- Phân biệt khái niệm Tích hợp liên tục (`지속적 통합 / CI`) và Triển khai liên tục (`지속적 배포 / CD`), cùng kiến trúc phân tán Master - Agent của máy chủ Jenkins.
- Nắm vững vai trò của các công cụ hỗ trợ cộng tác phát triển phần mềm: Jira (quản lý dự án Agile), Slack (truyền thông nội bộ), Zeplin (bàn giao thiết kế UI/UX), và Swagger (tài liệu hóa API).

## 핵심 키워드
- 통합 개발 환경 (IDE / Integrated Development Environment / 코딩, 컴파일, 디버깅, 배포)
- 빌드 자동화 도구 (Build Tools / Ant build.xml, Maven pom.xml, Gradle build.gradle Groovy DSL)
- CI/CD (지속적 통합 Continuous Integration, 지속적 배포 Continuous Delivery/Deployment)
- 젠킨스 (Jenkins / Java 기반 / Master-Agent 분산 빌드 / Web GUI)
- 협업 도구 (Jira 프로젝트 관리, Slack 커뮤니케이션, Zeplin 디자인 핸드오프, Swagger API 문서화)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [12-quan-ly-cau-hinh-scm-va-git.md](12-quan-ly-cau-hinh-scm-va-git.md), chúng ta đã làm chủ quy trình quản lý cấu hình và kho lưu trữ mã nguồn Git.
- **Đang giải quyết gì (Current Problem):** Bài học này giải quyết việc nâng cao năng suất lập trình viên thông qua bộ tứ tiện ích IDE và tự động hóa toàn bộ đường ống tải phụ thuộc, biên dịch, chạy test và đóng gói sản phẩm qua các công cụ Build (Maven, Gradle) và máy chủ CI/CD (Jenkins).
- **Dùng đi đâu (Forward Handoff):** Khi đường ống Build tự động được kích hoạt, các bài test kiểm thử phần mềm sẽ tự động chạy để sàng lọc lỗi, mở đầu cho Chương 4 về Kiểm thử phần mềm tại [14-nguyen-ly-va-phan-loai-kiem-thu.md](14-nguyen-ly-va-phan-loai-kiem-thu.md).

## 읽는 방법
- Đọc TẦNG A để nắm chắc bộ tứ chức năng của IDE, bảng đối chiếu 3 thế hệ công cụ Build (Ant vs Maven vs Gradle), kiến trúc Master-Agent của Jenkins và bảng nhận diện 4 công cụ cộng tác.
- Đọc TẦNG B để hiểu sâu cơ chế Build Cache và Incremental Build của Gradle so với Maven.

---

## 통합 개발 환경과 빌드 자동화

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bộ tứ chức năng cốt lõi của IDE (IDE 4대 기능)
```
[1. 코딩 (Coding)] ──► [2. 컴파일 (Compile)] ──► [3. 디버깅 (Debugging)] ──► [4. 배포 (Deployment)]
```
- **코딩 (Coding):** Tô sáng cú pháp, tự động thụt lề, gợi ý IntelliSense, phát hiện lỗi cú pháp tức thì.
- **컴파일 (Compile):** Biên dịch mã nguồn thành bytecode/mã máy, tự động liên kết thư viện.
- **디버깅 (Debugging):** Đặt điểm dừng (**Breakpoint**), chạy từng bước (Step), theo dõi biến (**Watch**), Call Stack.
- **배포 (Deployment):** Đóng gói thành `.jar`, `.war`, `.apk`, `.exe` và đẩy lên môi trường chạy thử.

#### 2. So sánh 3 thế hệ công cụ Build trong Java
| Tiêu chí | Apache Ant | Apache Maven | Gradle |
| :--- | :--- | :--- | :--- |
| **Tệp cấu hình** | `build.xml` | `pom.xml` (Project Object Model) | `build.gradle` (hoặc `build.gradle.kts`) |
| **Ngôn ngữ định nghĩa** | XML tĩnh | XML tĩnh (khai báo mô hình) | **Groovy DSL** hoặc **Kotlin DSL** |
| **Quản lý phụ thuộc** | **Không hỗ trợ** (phải tự tải file `.jar`) | **Tự động hóa** qua kho trung tâm (**Maven Central**) | Tự động hóa, kế thừa Maven/Ivy, giải quyết xung đột thông minh |
| **Cơ chế thực thi** | Thủ tục tuần tự (Procedural) | Vòng đời chuẩn (Compile $\rightarrow$ Test $\rightarrow$ Package) | Đồ thị tác vụ (Task DAG), **Incremental Build** |
| **Hiệu năng & Tốc độ** | Trung bình | Khá chậm (build lại nếu có đổi nhỏ) | **Rất nhanh** nhờ cơ chế **빌드 캐시 (Build Cache)** |
| **Vị thế thực tế** | Di sản (Legacy) | Tiêu chuẩn Enterprise Java (Spring Boot) | **Tiêu chuẩn chính thức của Google cho Android** |

#### 3. Bảng đối chiếu các công cụ hỗ trợ cộng tác (협업 도구)
| Nhóm công cụ | Tên tiếng Anh | Công cụ đại diện | Mục đích sử dụng |
| :--- | :--- | :--- | :--- |
| **Quản lý dự án** | **Project Management** | **Jira**, Trello, Asana | Theo dõi tiến độ Sprint, Issue/Ticket, Backlog theo Agile/Scrum |
| **Giao tiếp nội bộ** | **Communication** | **Slack**, Jandi, MS Teams | Trao đổi tức thời, tạo kênh theo chủ đề, nhận thông báo Git/Jenkins |
| **Bàn giao thiết kế** | **Design Hand-off** | **Zeplin**, Figma | Xuất kích thước pixel, mã màu CSS, tài nguyên đồ họa sang mã UI |
| **Tài liệu hóa API** | **API Documentation** | **Swagger (OpenAPI)** | Tự động sinh tài liệu API trực quan từ mã nguồn, thử gọi API trên Web |

#### 4. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Bộ tứ chức năng IDE:** 4 chức năng cốt lõi gồm: **코딩 (Coding), 컴파일 (Compile), 디버깅 (Debugging), 배포 (Deployment)**.
- **Bẫy 2: Quản lý thư viện phụ thuộc của Ant:** Khẳng định "Ant tự động tải thư viện từ Maven Central" $\rightarrow$ **SAI**. Ant không có tính năng quản lý phụ thuộc tự động; Maven mới là công cụ đưa tính năng này vào qua `pom.xml`.
- **Bẫy 3: Đặc trưng nhận diện Gradle:** Dùng ngôn ngữ kịch bản **Groovy DSL**, tối ưu tốc độ bằng **Build Cache** và là chuẩn chính thức của **Android** $\rightarrow$ Chọn **Gradle**.
- **Bẫy 4: Kiến trúc phân tán của Jenkins:** Hỗ trợ phân tán khối lượng build song song thông qua cấu trúc **Master - Agent (hoặc Master - Slave)**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Khái niệm CI và CD
- `CI (Continuous Integration - 지속적 통합)`: Lập trình viên liên tục gộp mã mới vào kho chung nhiều lần trong ngày; máy chủ CI tự động build và chạy test ngay lập tức để phát hiện lỗi sớm.
- `CD (Continuous Delivery / Deployment - 지속적 배포)`: Tự động hóa đường ống đưa mã nguồn đã qua kiểm thử thành công lên môi trường Staging hoặc triển khai thẳng vào Production.

#### 2. Phân định ranh giới: Jenkins vs Gradle
- `Gradle`: Là công cụ build ở **cấp độ dự án** (Project-level), chịu trách nhiệm biên dịch tệp `.java`, liên kết thư viện `.jar` và đóng gói tệp cài đặt.
- `Jenkins`: Là máy chủ tự động hóa ở **cấp độ hệ thống** (System-level), giám sát kho Git và tự động ra lệnh kích hoạt Gradle chạy trên máy chủ khi có commit mới.

---

### 복습 체크리스트
- [ ] Kể tên bộ tứ chức năng của IDE: 코딩, 컴파일, 디버깅, 배포.
- [ ] Phân biệt tệp cấu hình của 3 công cụ build: Ant (`build.xml`), Maven (`pom.xml`), Gradle (`build.gradle`).
- [ ] Nhớ rõ Ant không tự quản lý phụ thuộc; Maven dùng XML tĩnh; Gradle dùng Groovy/Kotlin DSL và Build Cache.
- [ ] Định nghĩa CI là tích hợp liên tục phát hiện lỗi sớm, CD là tự động triển khai.
- [ ] Nhớ kiến trúc của Jenkins là Master - Agent trên nền tảng Web GUI bằng Java.
- [ ] Phân biệt 4 công cụ cộng tác: Jira (quản lý dự án), Slack (giao tiếp), Zeplin (bàn giao thiết kế), Swagger (tài liệu API).
