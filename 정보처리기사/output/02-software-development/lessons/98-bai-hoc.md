# 098 & 기타 협업 도구 (Build Tools & Collaboration Tools)

## 학습 목표 (Mục tiêu)
- Nắm vững vai trò của các công cụ xây dựng (빌드 도구 - Build Tools) trong việc tự động hóa quy trình biên dịch, kiểm thử, đóng gói và triển khai sản phẩm phần mềm.
- Phân biệt sâu sắc sự tiến hóa của 3 công cụ build hàng đầu trong hệ sinh thái Java: Apache Ant (cấu hình XML, không quản lý thư viện phụ thuộc), Apache Maven (`pom.xml`, kho lưu trữ trung tâm Repository), và Gradle (Groovy/Kotlin DSL, Build Cache, công cụ chuẩn của Android).
- Nhận diện và phân loại các công cụ hỗ trợ cộng tác phát triển (협업 도구 - Collaboration Tools): Quản lý dự án (Jira, Trello), Trao đổi nội bộ (Slack, Jandi), Chuyển giao thiết kế UI/UX (Zeplin, Sketch), và Tài liệu hóa API (Swagger).

## 핵심 키워드 (Từ khóa)
- 빌드 도구 (Build Tools / 빌드 자동화)
- Ant (XML 기반 / 절차적 빌드 / 라이브러리 관리 부재)
- Maven (pom.xml / 선언적 빌드 / 중앙 저장소 의존성 관리)
- Gradle (Groovy/Kotlin DSL / 태스크 기반 / 증분 빌드)
- 협업 도구 (Collaboration Tools)
- 프로젝트 관리 도구 (Jira, Trello)
- 커뮤니케이션 도구 (Slack, Jandi)
- 디자인 핸드오프 (Zeplin, Figma)
- API 문서 자동화 (Swagger)

## 선행·연결 개념 (Kiến thức liên kết)
- [97-bai-hoc.md](97-bai-hoc.md): Môi trường phát triển tích hợp (IDE).
- [99-bai-hoc.md](99-bai-hoc.md): Tài liệu hướng dẫn sử dụng và cài đặt phần mềm.
- [46-bai-hoc.md](46-bai-hoc.md): Chi tiết các công cụ build tự động Ant, Maven, Gradle.

## 읽는 방법 (Cách đọc)
- Phân biệt sự tiến hóa của 3 thế hệ công cụ Build:
  - **Ant:** Cổ điển nhất, dùng tệp `build.xml`. Phải tự viết từng bước lệnh tuần tự; lập trình viên phải tự tải các file `.jar` ném vào thư mục dự án (không tự động tải thư viện).
  - **Maven:** Bước nhảy vọt với tệp `pom.xml`. Chỉ cần khai báo tọa độ thư viện (Group ID, Artifact ID, Version), Maven tự động tải từ kho trung tâm Maven Central về máy.
  - **Gradle:** Hiện đại nhất, thay XML cồng kềnh bằng kịch bản mã ngắn gọn (Groovy/Kotlin DSL). Hỗ trợ cơ chế Build Cache và biên dịch gia tăng (Incremental Build) cho tốc độ vượt trội gấp 10 lần so với Maven.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh 3 công cụ Build tự động (Ant vs Maven vs Gradle):**

| Tiêu chuẩn so sánh | Apache Ant | Apache Maven | Gradle |
| :--- | :--- | :--- | :--- |
| **Ngôn ngữ kịch bản** | **XML (`build.xml`)** | **XML (`pom.xml`)** | **Groovy / Kotlin DSL (`build.gradle`)** |
| **Quản lý phụ thuộc** | **Không có (없음)**; phải tự copy file JAR thủ công | **Tự động (자동)** qua kho lưu trữ Maven Central Repository | **Tự động (자동)**; tương thích kho Maven và Ivy |
| **Cấu trúc quy trình** | Thủ tục tuần tự (Procedural); tự định nghĩa target | Vòng đời chuẩn hóa cố định (Lifecycle: compile, test, package) | Hướng tác vụ linh hoạt (Task-based DAG), tùy biến cao |
| **Hiệu năng biên dịch** | Chậm khi dự án lớn | Trung bình do biên dịch lại nhiều phần | **Cực nhanh** nhờ **증분 빌드 (Incremental Build)** và **Build Cache** |
| **Ứng dụng chính** | Dự án Java di sản cổ điển | Ứng dụng doanh nghiệp Java Web tiêu chuẩn | Hệ sinh thái **Android**, Spring Boot hiện đại |

- **Bảng phân loại các công cụ cộng tác nhóm (협업 도구):**

| Nhóm công cụ | Tên công cụ tiêu biểu | Vai trò và giá trị cộng tác cốt lõi |
| :--- | :--- | :--- |
| **Quản lý dự án & Lịch trình** | **Jira (지라), Trello** | Quản lý tác vụ theo thẻ Kanban/Scrum, theo dõi tiến độ công việc, phân công nhiệm vụ và ghi nhận lỗi (Issue Tracking) |
| **Truyền thông nội bộ (Chat)** | **Slack, Jandi** | Kênh trò chuyện theo chủ đề (Channels), tích hợp thông báo tự động từ Git commit và CI/CD |
| **Chuyển giao thiết kế UI/UX** | **Zeplin, Sketch, Figma** | Cầu nối giữa Designer và Lập trình viên Front-end; tự động bóc tách mã CSS, tọa độ và trích xuất tài nguyên hình ảnh |
| **Tài liệu hóa giao diện API** | **Swagger** | Tự động sinh tài liệu giao diện RESTful API từ mã nguồn và cung cấp giao diện Web UI để chạy thử nghiệm trực tiếp |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mô hình GitOps và ChatOps:**
  - Ngày nay, các công cụ cộng tác như Slack và Jira được tích hợp sâu với kho lưu trữ mã nguồn (GitHub/GitLab) và hệ thống CI/CD (Jenkins/GitHub Actions).
  - Khi lập trình viên push code hoặc merge pull request, một thông báo tức thời sẽ bắn vào kênh Slack và tự động cập nhật trạng thái thẻ công việc trên bảng Jira.

### 복습 체크리스트
- [ ] So sánh được Ant (XML, không quản lý thư viện), Maven (`pom.xml`, repo tự động), và Gradle (Groovy/Kotlin DSL, Incremental Build).
- [ ] Nhớ Gradle là công cụ build tiêu chuẩn của Android.
- [ ] Phân loại đúng vai trò của Jira (quản lý dự án/ticket), Slack (giao tiếp), Zeplin (thiết kế UI sang code), Swagger (tài liệu API).
