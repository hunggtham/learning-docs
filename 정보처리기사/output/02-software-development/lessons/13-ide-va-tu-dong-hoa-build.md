# 통합 개발 환경(IDE)과 빌드 자동화 도구 (IDE và tự động hóa Build)

## 학습 목표
- Nắm vững định nghĩa Môi trường phát triển tích hợp (`통합 개발 환경 / IDE - Integrated Development Environment`) và 4 chức năng cốt lõi: Soạn thảo mã (`코딩 / Coding`), Biên dịch (`컴파일 / Compile`), Gỡ lỗi (`디버깅 / Debugging`), và Đóng gói triển khai (`배포 / Deployment`).
- Nhận diện các IDE tiêu biểu trong đề thi: Eclipse, IntelliJ IDEA, Visual Studio, Xcode, Android Studio.
- So sánh đối đầu 3 thế hệ công cụ tự động hóa Build trong hệ sinh thái Java/JVM: `Apache Ant` (thủ tục, XML, không quản lý phụ thuộc), `Apache Maven` (vòng đời chuẩn, pom.xml, tải tự động từ Central Repo), và `Gradle` (Groovy/Kotlin DSL, Task DAG, Incremental Build, Build Cache).
- Nắm vững khái niệm Tích hợp liên tục (`CI / Continuous Integration`) và công cụ tự động hóa máy chủ tích hợp `Jenkins`.

## 핵심 키워드
- 통합 개발 환경 (IDE / Integrated Development Environment)
- IDE 4대 기능 (코딩 Coding, 컴파일 Compile, 디버깅 Debugging, 배포 Deployment)
- 빌드 자동화 도구 (Build Tools / 컴파일, 라이브러리 링크, 패키징 자동화)
- Ant vs Maven vs Gradle (3 thế hệ công cụ Build trong Java)
- Maven (pom.xml, 의존성 관리 Dependency Management, 생명주기 Lifecycle)
- Gradle (Groovy/Kotlin DSL, 안드로이드 공식 빌드 도구, 점진적 빌드 Incremental Build)
- Jenkins (젠킨스 / CI/CD 지속적 통합 서버)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [12-quan-ly-cau-hinh-scm-va-git.md](12-quan-ly-cau-hinh-scm-va-git.md), chúng ta đã khảo sát quy trình quản lý phiên bản mã nguồn bằng Git.
- **Đang giải quyết gì (Current Problem):** Việc biên dịch, liên kết hàng trăm thư viện và triển khai thủ công tốn thời gian và dễ gây lỗi. Bài học này giải quyết việc tự động hóa toàn bộ chu trình từ viết mã, biên dịch, kiểm thử đến đóng gói thành phẩm qua các IDE và công cụ Build (Maven, Gradle, Jenkins).
- **Dùng đi đâu (Forward Handoff):** Sau khi phần mềm được build hoàn chỉnh, bài học tiếp theo [14-nguyen-ly-va-phan-loai-kiem-thu.md](14-nguyen-ly-va-phan-loai-kiem-thu.md) sẽ mở màn cho Chương 4 để khảo sát 7 nguyên lý kiểm thử phần mềm nền tảng.

## 읽는 방법
- Đọc TẦNG A để thuộc lòng 4 chức năng IDE, bảng so sánh Ant vs Maven vs Gradle và các bẫy trắc nghiệm.
- Đọc TẦNG B để hiểu sâu cơ chế vòng đời chuẩn của Maven, Task DAG trong Gradle và máy chủ tích hợp Jenkins.

---

## 통합 개발 환경(IDE)과 빌드 자동화 도구

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bốn chức năng cốt lõi của IDE (IDE 4대 기능)
```
[1. 코딩 (Coding)] ──► [2. 컴파일 (Compile)] ──► [3. 디버깅 (Debugging)] ──► [4. 배포 (Deployment)]
```

| Chức năng cốt lõi | Tên tiếng Hàn (English) | Chi tiết tiện ích kỹ thuật |
| :--- | :--- | :--- |
| **Soạn thảo mã** | **코딩 (Coding)** | Tô sáng cú pháp (Syntax Highlighting), tự động thụt lề, gợi ý mã (Auto-completion) |
| **Biên dịch** | **컴파일 (Compile)** | Tích hợp trình biên dịch chuyển mã nguồn thành bytecode hoặc mã máy; tự động liên kết thư viện |
| **Gỡ lỗi** | **디버깅 (Debugging)** | Điểm dừng (**중단점 - Breakpoint**), chạy từng dòng, theo dõi biến (**변수 감시 - Watch**), Call Stack |
| **Đóng gói triển khai** | **배포 (Deployment)** | Tự động đóng gói thành `.jar`, `.war`, `.apk`, `.exe`, tích hợp triển khai lên server |

#### 2. Bảng so sánh 3 thế hệ công cụ Build: Ant vs Maven vs Gradle
```
[Thế hệ 1: Apache Ant]          [Thế hệ 2: Apache Maven]          [Thế hệ 3: Gradle]
- Cấu hình XML (build.xml)      - Cấu hình XML (pom.xml)          - Ngôn ngữ Groovy/Kotlin DSL
- Build theo thủ tục            - Quy chuẩn vòng đời dự án         - Đồ thị tác vụ (Task DAG)
- KHÔNG quản lý phụ thuộc       - Tự động tải từ Central Repo     - Build Cache & Tăng tốc vượt trội
                                                                  - Chuẩn build Android
```

| Tiêu chí | Apache Ant | Apache Maven | Gradle |
| :--- | :--- | :--- | :--- |
| **Tệp cấu hình** | `build.xml` | `pom.xml` | `build.gradle` (hoặc `build.gradle.kts`) |
| **Ngôn ngữ định nghĩa** | XML tĩnh | XML tĩnh (khai báo mô hình) | **Groovy DSL** hoặc **Kotlin DSL** |
| **Quản lý phụ thuộc** | **Không hỗ trợ** (phải tự tải `.jar` thủ công) | **Tự động hóa hoàn toàn** qua **Maven Central Repository** | Kế thừa kho Maven, hỗ trợ giải quyết xung đột thông minh |
| **Cơ chế thực thi** | Thủ tục tuần tự | Vòng đời tiêu chuẩn: Compile $\rightarrow$ Test $\rightarrow$ Package | Đồ thị tác vụ (Task DAG), **점진적 빌드 (Incremental Build)** |
| **Hiệu năng & Tốc độ** | Trung bình | Khá chậm (build lại toàn bộ nếu có đổi) | **Rất nhanh** nhờ **빌드 캐시 (Build Cache)** |
| **Vị thế thực tế** | Di sản (Legacy) | Tiêu chuẩn Enterprise Java (Spring Boot) | **Tiêu chuẩn chính thức cho Android** và Microservices |

#### 3. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Tệp cấu hình của Maven và Gradle:**
  - Maven sử dụng: **`pom.xml`** (Project Object Model).
  - Gradle sử dụng: **`build.gradle`** viết bằng Groovy DSL hoặc Kotlin DSL.
- **Bẫy 2: Nhận diện Gradle:** Khi câu hỏi đề cập đến *"Công cụ Build tự động sử dụng ngôn ngữ kịch bản Groovy DSL, thực thi dựa trên đồ thị tác vụ có hướng (DAG), hỗ trợ Incremental Build và là công cụ chính thức cho Android?"* $\rightarrow$ Đáp án chắc chắn là **Gradle**.
- **Bẫy 3: Máy chủ CI/CD Jenkins:** Công cụ mã nguồn mở viết bằng Java chuyên dùng làm máy chủ điều phối tự động hóa quá trình tích hợp liên tục (CI) và phát hành liên tục (CD) là **젠킨스 (Jenkins)**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Danh sách các IDE tiêu biểu trong đề thi
| Tên IDE | Đơn vị phát triển / Xuất xứ | Ngôn ngữ / Nền tảng hỗ trợ chính |
| :--- | :--- | :--- |
| **Eclipse (이클립스)** | IBM khởi xướng / Quỹ Eclipse | Hỗ trợ chính cho **Java**, kiến trúc mở rộng mạnh mẽ qua hệ thống Plugin |
| **IntelliJ IDEA (인텔리제이)** | JetBrains | Hỗ trợ vượt trội cho **Java**, **Kotlin**, phân tích mã thông minh |
| **Visual Studio (비주얼 스튜디오)** | Microsoft | Phát triển trên Windows, hỗ trợ **C#**, **.NET**, C++, F# |
| **Xcode (엑스코드)** | Apple | Môi trường phát triển độc quyền cho macOS/iOS, dùng **Swift** và Objective-C |
| **Android Studio (안드로이드 스튜디오)** | Google (dựa trên nền IntelliJ) | Môi trường phát triển chính thức cho hệ điều hành **Android**, dùng Kotlin/Java |

#### 2. Vòng đời tiêu chuẩn của Apache Maven (Maven Lifecycle)
- `validate`: Kiểm tra tính hợp lệ của dự án và các tệp cấu hình.
- `compile`: Biên dịch toàn bộ mã nguồn của dự án.
- `test`: Tự động chạy các bài kiểm thử đơn vị (Unit Tests qua JUnit).
- `package`: Đóng gói mã nhị phân thành tệp nén phân phối (`.jar` hoặc `.war`).
- `verify`: Chạy các bài kiểm tra tích hợp để xác minh chất lượng gói.
- `install`: Cài đặt gói vào kho lưu trữ cục bộ (Local Repository) của máy phát triển.
- `deploy`: Sao chép gói thành phẩm lên kho lưu trữ từ xa (Remote Repository) để chia sẻ.

---

### 복습 체크리스트
- [ ] Thuộc lòng 4 chức năng cốt lõi của IDE: 코딩, 컴파일, 디버깅, 배포.
- [ ] Nhận diện các IDE tiêu biểu: Eclipse, IntelliJ, Visual Studio, Xcode, Android Studio.
- [ ] So sánh 3 thế hệ công cụ Build: Ant (`build.xml`), Maven (`pom.xml`), Gradle (`build.gradle`).
- [ ] Nhớ Gradle dùng Groovy/Kotlin DSL, hỗ trợ Incremental Build và là chuẩn của Android.
- [ ] Định nghĩa Jenkins là máy chủ CI/CD tự động hóa quá trình build và tích hợp liên tục.
