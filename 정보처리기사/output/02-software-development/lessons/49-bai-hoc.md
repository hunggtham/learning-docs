# 118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm và chu trình Tích hợp liên tục / Phân phối liên tục (CI/CD: 지속적 통합 / 지속적 배포) trong phát triển phần mềm hiện đại.
- Tổng kết toàn diện các đặc tính kỹ thuật cốt lõi của Jenkins (Java, Web GUI, Master-Agent) và Gradle (Groovy, DSL, Build Cache, Android).
- Đánh giá các lợi ích chiến lược của việc tự động hóa quá trình Build: Phát hiện lỗi sớm, loại bỏ sai sót của con người và rút ngắn chu kỳ đưa sản phẩm ra thị trường.

## 핵심 키워드 (Từ khóa)
- 빌드 자동화 도구 (Build Automation Tools)
- CI (Continuous Integration / 지속적 통합)
- CD (Continuous Deployment / 지속적 배포)
- Jenkins (Java 기반 / Web GUI / 분산 빌드)
- Gradle (Groovy DSL / 빌드 캐시 / 안드로이드 빌드)
- 자동화 파이프라인 (Automated Pipeline)

## 선행·연결 개념 (Kiến thức liên kết)
- [46-bai-hoc.md](46-bai-hoc.md): Tổng quan về 4 công cụ tự động hóa build.
- [48-bai-hoc.md](48-bai-hoc.md): So sánh chuyên sâu Jenkins vs Gradle.
- [50-bai-hoc.md](50-bai-hoc.md): Quản lý bản quyền số DRM và bảo mật sau giai đoạn đóng gói.

## 읽는 방법 (Cách đọc)
- Ôn tập bảng tóm tắt 2 dòng định mệnh thường ra đề:
  - Jenkins = **Java + Web GUI + Phân tán (분산)**.
  - Gradle = **Groovy + DSL + Build Cache + Android**.
- Hiểu khái niệm CI: Lập trình viên liên tục gộp code vào kho chung nhiều lần trong ngày, máy chủ tự động build và chạy test ngay lập tức để phát hiện xung đột sớm.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Chu trình CI/CD trong phát triển phần mềm:**
  - **지속적 통합 (CI - Continuous Integration):**
    - Các thành viên trong nhóm tích hợp mã nguồn vào kho lưu trữ chung hàng ngày.
    - Mỗi lần commit đều tự động kích hoạt tiến trình Build và kiểm thử tự động (Automated Testing) để đảm bảo mã mới không làm vỡ các tính năng cũ.
  - **지속적 배포 / 전달 (CD - Continuous Deployment / Delivery):**
    - Tự động đóng gói phần mềm đã qua kiểm thử thành công và triển khai tự động lên các môi trường thử nghiệm (Staging) hoặc phát hành trực tiếp cho khách hàng (Production).
- **Bảng ghi nhớ nhanh đặc tính cốt lõi của hai công cụ:**

| Công cụ | Nền tảng ngôn ngữ | Giao diện / Cách viết | Tính năng ăn điểm trắc nghiệm |
| :--- | :--- | :--- | :--- |
| **Jenkins** | **Java** | **Giao diện Web GUI** thân thiện | Hỗ trợ mô hình Master-Agent cho phép **kiểm thử và build phân tán (분산 빌드)** trên nhiều máy trạm song song |
| **Gradle** | **Groovy** | **Ngôn ngữ kịch bản DSL** linh hoạt | Trang bị tính năng **빌드 캐시 (Build Cache)** giúp tăng tốc độ build vượt trội; là công cụ chuẩn mực của ứng dụng di động **Android** |

- **Lợi ích kinh tế và kỹ thuật của Tự động hóa Build:**
  - Loại bỏ hoàn toàn sự chậm trễ và sai sót thủ công khi gõ lệnh biên dịch.
  - Tăng độ tin cậy của mã nguồn nhờ cơ chế chạy toàn bộ bộ ca kiểm thử tự động (Automated Regression Testing) sau mỗi lần cập nhật.
  - Rút ngắn thời gian nhận phản hồi (Feedback loop) cho lập trình viên từ vài ngày xuống còn vài phút.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tệp Jenkinsfile và khái niệm Pipeline as Code:**
  - Trong các hệ thống DevOps tiên tiến, toàn bộ các bước kiểm thử, build, quét lỗ hổng bảo mật SonarQube và triển khai Docker/Kubernetes được lập trình thành một tệp văn bản duy nhất có tên là **`Jenkinsfile`**.
  - Tệp này được lưu trữ và quản lý phiên bản cùng với mã nguồn dự án trên Git (Pipeline-as-Code), giúp toàn bộ hạ tầng triển khai có thể tái tạo dễ dàng ở bất kỳ đâu.

### 복습 체크리스트
- [ ] Định nghĩa CI là tích hợp kiểm thử liên tục, CD là triển khai phát hành liên tục.
- [ ] Ghi nhớ chắc chắn: Jenkins dựa trên Java với Web GUI; Gradle dựa trên Groovy DSL.
- [ ] Nhớ tính năng ăn điểm của Gradle là Build Cache tối ưu hóa thời gian.
- [ ] Nhớ tính năng ăn điểm của Jenkins là khả năng phân tán công việc trên nhiều Agent.
