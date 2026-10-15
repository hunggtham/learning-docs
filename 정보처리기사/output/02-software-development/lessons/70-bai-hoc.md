# 26. 인터페이스 구현 검증 도구 (Interface Verification Tools)

## 학습 목표 (Mục tiêu)
- Nắm vững danh sách và đặc điểm vận hành của các công cụ kiểm thử tự động dùng để kiểm chứng việc triển khai giao diện phần mềm (인터페이스 구현 검증 도구).
- Phân biệt chính xác mục đích sử dụng và môi trường ứng dụng của 5 công cụ xuất hiện thường xuyên trong kỳ thi: xUnit, STAF, FitNesse, NTAF, và watir.
- Hiểu cách thức tích hợp các công cụ này vào quy trình CI/CD nhằm giám sát liên tục trạng thái hoạt động của các API/Interface.

## 핵심 키워드 (Từ khóa)
- 인터페이스 검증 도구 (Interface Verification Tools)
- xUnit (단위 테스트 프레임워크 / JUnit, CppUnit, NUnit)
- STAF (Software Testing Automation Framework / 분산 환경 / 컴포넌트 재사용)
- FitNesse (웹 기반 협업 테스트 도구 / 위키 기반)
- NTAF (Naver Test Automation Framework / FitNesse + STAF 통합)
- watir (Ruby 기반 웹 애플리케이션 테스트)

## 선행·연결 개념 (Kiến thức liên kết)
- [69-bai-hoc.md](69-bai-hoc.md): Bảo mật giao diện tầng mạng.
- [71-bai-hoc.md](71-bai-hoc.md): Kiến trúc ba tầng lược đồ trong cơ sở dữ liệu.
- [50-bai-hoc.md](50-bai-hoc.md): Quy trình tích hợp liên tục và công cụ CI/CD Jenkins.

## 읽는 방법 (Cách đọc)
- Học theo từ khóa nhận diện đặc trưng (Mnemonic Matching):
  - **xUnit:** Khung kiểm thử đơn vị đa ngôn ngữ (JUnit cho Java, CppUnit cho C++, NUnit cho .NET).
  - **STAF:** Kiểm thử dịch vụ và thành phần trong **môi trường phân tán (분산 환경)**.
  - **FitNesse:** Kiểm thử dựa trên nền tảng **Web và Wiki (웹 기반 테스트)**, dễ viết bảng kiểm tra cho cả khách hàng.
  - **NTAF:** Sản phẩm kết hợp của **Naver (NHN)** tích hợp ưu điểm của cả FitNesse và STAF.
  - **watir:** Khung kiểm thử ứng dụng Web bằng ngôn ngữ **Ruby**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp 5 công cụ kiểm chứng giao diện phần mềm:**

| Tên công cụ | Nền tảng / Ngôn ngữ | Đặc trưng kỹ thuật trọng tâm | Từ khóa bẫy đề thi |
| :--- | :--- | :--- | :--- |
| **xUnit** | Đa ngôn ngữ (Java, C++, C#...) | Khung kiểm thử đơn vị phổ biến nhất; hỗ trợ tự động chạy test và báo cáo kết quả | **단위 테스트 프레임워크**, JUnit, CppUnit |
| **STAF** | Đa nền tảng (C/S, Daemon) | Khung tự động hóa kiểm thử hướng dịch vụ, hỗ trợ gọi dịch vụ và tái sử dụng thành phần trong môi trường phân tán | **서비스 호출**, **컴포넌트 재사용**, **분산 환경** |
| **FitNesse** | Web / Wiki | Công cụ kiểm thử chấp nhận hiển thị dưới dạng bảng trên giao diện web, giúp lập trình viên và khách hàng dễ dàng cùng thiết kế test case | **웹 기반**, **Wiki 기반**, 케이스 설계 및 실행 |
| **NTAF** | Do NHN (Naver) phát triển | Tích hợp giao diện quản lý kiểm thử thân thiện của FitNesse với khả năng kiểm thử phân tán mạnh mẽ của STAF | **FitNesse + STAF 결합**, **NHN(네이버)** |
| **watir** | Ruby | Khung kiểm thử tự động hóa tương tác trình duyệt web dựa trên ngôn ngữ lập trình Ruby | **Ruby 기반**, 웹 애플리케이션 테스트 |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Quy trình giám sát giao diện APM kết hợp Test Tool:**
  - Trong kiến trúc hướng dịch vụ (SOA) hoặc Microservices, việc kiểm tra giao diện không chỉ dừng lại ở chức năng gửi nhận dữ liệu mà còn kiểm tra tính sẵn sàng thông qua APM (Application Performance Monitoring).
  - Các công cụ như STAF thường được cài đặt dưới dạng tiến trình nền (Daemon) trên các máy chủ thử nghiệm để điều phối việc kích hoạt test case đồng loạt trên nhiều môi trường hệ điều hành khác nhau.

### 복습 체크리스트
- [ ] Nhớ tên và ngôn ngữ của xUnit (JUnit, CppUnit), watir (Ruby).
- [ ] Nhớ đặc trưng phân tán của STAF.
- [ ] Nhớ công cụ kết hợp NTAF = FitNesse + STAF của NHN.
- [ ] Nhớ tính năng hiển thị web/wiki của FitNesse.
