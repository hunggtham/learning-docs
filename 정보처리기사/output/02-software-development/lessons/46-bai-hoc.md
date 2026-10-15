# 10. 빌드 자동화 도구 (Build Automation Tools)

## 학습 목표 (Mục tiêu)
- Định nghĩa Công cụ tự động hóa quá trình Build (빌드 자동화 도구 - Build Automation Tools) và vai trò trong việc tự động biên dịch, kiểm thử, tích hợp và đóng gói mã nguồn phần mềm.
- Nắm vững 4 công cụ tự động hóa build kinh điển trong hệ sinh thái phần mềm: Ant, Maven, Gradle và Jenkins.
- Phân biệt sự tiến hóa về ngôn ngữ cấu hình và kiến trúc từ XML tĩnh (Ant, Maven) sang ngôn ngữ DSL linh hoạt (Gradle) và máy chủ tích hợp liên tục CI/CD chuyên dụng (Jenkins).

## 핵심 키워드 (Từ khóa)
- 빌드 자동화 도구 (Build Automation Tools)
- Ant (Apache / XML / 절차적 빌드)
- Maven (Apache / `pom.xml` / 생명주기 및 의존성 관리)
- Gradle (Groovy DSL / 빌드 캐시 / 안드로이드 표준)
- Jenkins (Java 기반 / CI·CD 자동화 서버 / Web GUI / 분산 빌드)

## 선행·연결 개념 (Kiến thức liên kết)
- [45-bai-hoc.md](45-bai-hoc.md): Bước 빌드 진행 (Build Execution) trong quy trình đóng gói phần mềm.
- [47-bai-hoc.md](47-bai-hoc.md): Môi trường phát triển tích hợp (IDE) và công cụ Build.
- [48-bai-hoc.md](48-bai-hoc.md): So sánh chuyên sâu Jenkins vs Gradle trong quy trình CI/CD.

## 읽는 방법 (Cách đọc)
- Học thuộc 4 đại diện qua thần chú chữ cái đầu: **AMJG** (*Ant, Maven, Jenkins, Gradle*).
- Nhớ nhanh từ khóa nhận diện đề thi:
  - Cứ thấy **"Apache, XML, pom.xml, 의존성 관리 (Quản lý phụ thuộc)"** $\rightarrow$ **Maven**.
  - Cứ thấy **"Groovy 기반 DSL, 빌드 캐시 (Build Cache), Android 표준"** $\rightarrow$ **Gradle**.
  - Cứ thấy **"Java 기반 오픈소스, Web GUI, CI/CD 서버, 분산 빌드"** $\rightarrow$ **Jenkins**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bản chất của Tự động hóa quá trình Build:**
  - Build là quá trình chuyển đổi toàn bộ mã nguồn viết tay cùng các tệp cấu hình thành sản phẩm nhị phân có thể thực thi được.
  - Quá trình tự động hóa giải phóng lập trình viên khỏi các công việc thủ công lặp đi lặp lại: Tự động tải thư viện $\rightarrow$ Biên dịch mã $\rightarrow$ Chạy Unit Test $\rightarrow$ Đóng gói thành `.jar` / `.war` / `.apk` $\rightarrow$ Triển khai lên máy chủ.
- **Bảng tổng hợp 4 công cụ tự động hóa Build tiêu biểu:**

| Công cụ | Nền tảng phát triển | Ngôn ngữ cấu hình | Đặc trưng kỹ thuật cốt lõi (Từ khóa đề thi) |
| :--- | :--- | :--- | :--- |
| **Ant** | Java (Apache) | XML (`build.xml`) | Công cụ đời đầu, cấu hình theo hướng **thủ tục mệnh lệnh (Imperative)**; không có cơ chế quản lý phụ thuộc tự động |
| **Maven** | Java (Apache) | XML (`pom.xml`) | Khắc phục Ant bằng nguyên lý **Quy ước hơn Cấu hình (Convention over Configuration)**; tự động tải thư viện từ Kho trung tâm (Maven Central Repository); quản lý vòng đời Build (Lifecycle) rõ ràng |
| **Gradle** | Java (Gradle Inc.) | **Groovy / Kotlin DSL** | Kết hợp ưu điểm của cả Ant và Maven; tốc độ vượt trội nhờ tính năng **빌드 캐시 (Build Cache)** và biên dịch gia tăng (Incremental Build); là công cụ build tiêu chuẩn cho Android |
| **Jenkins** | Java (Open Source) | Web GUI / Pipeline Script | Máy chủ tích hợp liên tục (**CI/CD Server**); cung cấp giao diện trực quan thân thiện; hỗ trợ hàng ngàn plugin và khả năng **phân tán công việc (Distributed Build)** qua các nút Agent |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Vòng đời chuẩn của Maven (Maven Build Lifecycle):**
  - Gồm 3 vòng đời tích hợp sẵn: `default` (xử lý build ứng dụng), `clean` (xóa sạch thư mục build cũ), `site` (tạo tài liệu dự án).
  - Chuỗi pha tuần tự trong vòng đời `default`:
    $$\text{validate} \rightarrow \text{compile} \rightarrow \text{test} \rightarrow \text{package} \rightarrow \text{verify} \rightarrow \text{install} \rightarrow \text{deploy}$$

### 복습 체크리스트
- [ ] Kể tên 4 công cụ Build tự động hóa: Ant, Maven, Jenkins, Gradle.
- [ ] Nhớ Maven sử dụng tệp cấu hình `pom.xml` để tự động quản lý thư viện phụ thuộc.
- [ ] Nhớ Gradle sử dụng ngôn ngữ Groovy DSL và có công nghệ Build Cache siêu tốc.
- [ ] Nhớ Jenkins là máy chủ CI/CD tự động hóa viết bằng Java với giao diện Web GUI.
