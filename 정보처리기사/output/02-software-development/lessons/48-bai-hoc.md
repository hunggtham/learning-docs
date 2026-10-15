# 41. 빌드 자동화 도구 심화: Jenkins vs Gradle

## 학습 목표 (Mục tiêu)
- Phân tích chuyên sâu và so sánh đối đầu hai công cụ tự động hóa hàng đầu trong quy trình phát triển hiện đại: Jenkins (Máy chủ CI/CD) và Gradle (Công cụ Build cấp dự án).
- Nắm vững kiến trúc Phân tán Master - Agent và giao diện Web GUI của Jenkins.
- Hiểu rõ cơ chế thực thi theo tác vụ (Task DAG), công nghệ bộ nhớ đệm Build Cache và ngôn ngữ kịch bản Groovy DSL của Gradle.

## 핵심 키워드 (Từ khóa)
- Jenkins (Java 기반 / CI·CD 서버 / Web GUI)
- 마스터 - 에이전트 구조 (Master-Agent Distributed Build)
- Gradle (Groovy DSL / Task 단위 실행)
- 빌드 캐시 (Build Cache / 속도 최적화)
- 점진적 빌드 (Incremental Build)
- 안드로이드 빌드 표준 (Android Build Standard)

## 선행·연결 개념 (Kiến thức liên kết)
- [46-bai-hoc.md](46-bai-hoc.md): Tổng quan 4 công cụ tự động hóa build (Ant, Maven, Jenkins, Gradle).
- [47-bai-hoc.md](47-bai-hoc.md): Môi trường phát triển tích hợp (IDE) và công cụ Build.
- [49-bai-hoc.md](49-bai-hoc.md): Ứng dụng quy trình CI/CD trong phát triển phần mềm doanh nghiệp.

## 읽는 방법 (Cách đọc)
- Phân biệt phạm vi hoạt động:
  - **Gradle:** Đứng ở cấp độ **Tệp mã nguồn và Dự án** (tải thư viện jar, compile file `.java` thành `.class`, đóng gói `.apk`).
  - **Jenkins:** Đứng ở cấp độ **Hệ thống và Máy chủ CI/CD** (lắng nghe Git push, ra lệnh cho Gradle chạy trên nhiều máy Agent, gửi email báo cáo kết quả kiểm thử).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh chi tiết đối đầu giữa Jenkins và Gradle:**

| Tiêu chí so sánh | Jenkins (젠킨스) | Gradle (그레이들) |
| :--- | :--- | :--- |
| **Bản chất công cụ** | **Máy chủ tự động hóa tích hợp liên tục (CI/CD Server)** | **Hệ thống tự động hóa Build dự án (Build Automation Tool)** |
| **Ngôn ngữ nền tảng** | **Java** (Giao diện Web GUI trực quan) | **Java** (Viết kịch bản bằng **Groovy / Kotlin DSL**) |
| **Cơ chế kiến trúc** | **마스터 - 에이전트 (Master-Agent)**: Master điều phối công việc, nhiều máy Agent chạy phân tán song song | **Đồ thị có hướng không chu trình (DAG)** của các Task độc lập |
| **Điểm mạnh vượt trội** | Kho Plugin khổng lồ (>1800 plugins); hỗ trợ kiểm thử phân tán; giao diện web dễ cấu hình | Công nghệ **빌드 캐시 (Build Cache)** và biên dịch gia tăng giúp tốc độ build nhanh gấp 2~10 lần Maven |
| **Phạm vi ứng dụng** | Quản lý toàn bộ chuỗi Pipeline: Tải code từ Git $\rightarrow$ Build $\rightarrow$ Test $\rightarrow$ Deploy | Công cụ build chính thức và tiêu chuẩn cho hệ sinh thái **Android**, ứng dụng Java/Kotlin |

- **Các tính năng kỹ thuật cốt lõi trong đề thi:**
  - **Jenkins:**
    - Khả năng kích hoạt tự động (Triggers): Khi lập trình viên push code lên Git (Webhook), hoặc theo lịch định kỳ (Cron Trigger), hoặc khi có dự án khác build xong.
    - **분산 빌드 (Distributed Build):** Giảm tải cho máy chủ chính bằng cách phân bổ các tác vụ kiểm thử nặng sang các máy Agent phụ.
  - **Gradle:**
    - **태스크 (Task) 단위 실행:** Mỗi công đoạn (như compileJava, processResources, test, jar) là một Task riêng lẻ có thể tái sử dụng.
    - **빌드 캐시 (Build Cache):** Nếu mã nguồn và tham số đầu vào của một Task không hề thay đổi so với lần build trước, Gradle sẽ bỏ qua việc tính toán lại và lấy thẳng kết quả từ Cache ra sử dụng.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mô hình phối hợp thực tế trong quy trình CI/CD:**
  - Trong các công ty công nghệ lớn, Jenkins và Gradle không bao giờ triệt tiêu nhau mà phối hợp nhịp nhàng:
    ```
    [Lập trình viên] --git push--> [Git Repository]
                                         |
                                (Kích hoạt Webhook)
                                         v
                                  [Jenkins Server]
                                         |
                            (Gọi lệnh "gradle build")
                                         v
                                  [Gradle Engine]
                                (Biên dịch, Test, Cache)
                                         |
    [Máy chủ Production] <--Deploy-- [Tệp đóng gói APK/JAR]
    ```

### 복습 체크리스트
- [ ] Phân biệt rõ bản chất: Jenkins là CI/CD Server, Gradle là Build Tool.
- [ ] Nhớ kiến trúc Master-Agent của Jenkins hỗ trợ phân tán kiểm thử.
- [ ] Nhớ Gradle dùng ngôn ngữ Groovy DSL và là chuẩn mực cho ứng dụng Android.
- [ ] Nêu được cơ chế tăng tốc của Gradle: Build Cache và Incremental Build.
