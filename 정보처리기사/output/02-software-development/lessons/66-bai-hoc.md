# 132 ~ 136: 개발 단계에 따른 애플리케이션 테스트 (V-Model Test Levels)

## 학습 목표 (Mục tiêu)
- Nắm vững chuỗi các cấp độ kiểm thử phần mềm theo các giai đoạn phát triển trong mô hình chữ V: Kiểm thử đơn vị (단위 테스트) $\rightarrow$ Kiểm thử tích hợp (통합 테스트) $\rightarrow$ Kiểm thử hệ thống (시스템 테스트) $\rightarrow$ Kiểm thử chấp nhận (인수 테스트).
- Phân biệt sâu sắc hai trường phái kiểm thử tích hợp: Tích hợp phi gia tăng Big Bang (비점진적 / 빅뱅 통합) và Tích hợp gia tăng từng bước (점진적 통합: Top-down, Bottom-up, Sandwich).
- Hiểu rõ sự khác biệt giữa kiểm thử chức năng và kiểm thử phi chức năng trong tầng Kiểm thử hệ thống, cùng hai hình thức nghiệm thu Alpha Test và Beta Test.

## 핵심 키워드 (Từ khóa)
- 개발 단계별 테스트 레벨 (Development Phase Test Levels)
- 단위 테스트 (Unit Test / 구현 단계 / 화이트박스)
- 통합 테스트 (Integration Test / 상세 설계 / 빅뱅 vs 점진적)
- 시스템 테스트 (System Test / 시스템 설계 / 기능 및 비기능)
- 인수 테스트 (Acceptance Test / 요구사항 / 알파 및 베타)
- 빅뱅 테스트 (Big Bang Test / 일괄 통합)
- 점진적 통합 (Incremental: 하향식, 상향식, 샌드위치)

## 선행·연결 개념 (Kiến thức liên kết)
- [53-bai-hoc.md](53-bai-hoc.md): Khái niệm 4 cấp độ kiểm thử phần mềm.
- [55-bai-hoc.md](55-bai-hoc.md): Chi tiết kiểm thử tích hợp Top-down và Test Stub.
- [60-bai-hoc.md](60-bai-hoc.md): Mô hình V-Model và nguyên lý ánh xạ hai nhánh đối xứng.

## 읽는 방법 (Cách đọc)
- Ôn tập so sánh hai phương thức tích hợp mô-đun:
  - **빅뱅 통합 (Big Bang):** Gom tất cả các mô-đun lại ghép thành một khối duy nhất rồi mới bấm chạy $\rightarrow$ Rất khó truy tìm nguyên nhân gây lỗi khi xảy ra sự cố.
  - **점진적 통합 (Incremental):** Tích hợp từng mô-đun một (Top-down hoặc Bottom-up) $\rightarrow$ Lỗi phát sinh ở đâu phát hiện được ngay lập tức tại điểm vừa ghép.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp 4 cấp độ kiểm thử theo giai đoạn phát triển (V-Model):**

| Cấp độ kiểm thử | Giai đoạn phát triển đối ứng | Mục tiêu kiểm tra trọng tâm | Đặc trưng kỹ thuật và phương pháp |
| :--- | :--- | :--- | :--- |
| **1. 단위 테스트 (Unit Test)** | **구현 (Implementation / Coding)** | Kiểm tra thuật toán, logic câu lệnh, điều kiện biên của từng mô-đun, hàm, lớp riêng lẻ | Chủ yếu là **화이트박스 (White-box)**; do lập trình viên thực hiện ngay sau khi code xong |
| **2. 통합 테스트 (Integration Test)** | **상세 설계 (Detailed Design)** | Kiểm tra **lỗi giao tiếp (인터페이스 오류 - Interface Error)**, tính tương thích tham số khi ghép các mô-đun lại với nhau | Gồm 2 phương thức: **빅뱅 (Big Bang)** và **점진적 (Incremental: Top-down, Bottom-up, Sandwich)** |
| **3. 시스템 테스트 (System Test)** | **시스템 설계 (System Design)** | Kiểm tra toàn bộ hệ thống tích hợp hoàn chỉnh trên môi trường thực tế | Kiểm tra cả **Chức năng (Functional)** lẫn **Phi chức năng (Non-functional)**: Hiệu năng, Bảo mật, Tải áp lực, Phục hồi |
| **4. 인수 테스트 (Acceptance Test)** | **요구사항 분석 (Requirements Analysis)** | Khách hàng hoặc người dùng cuối trực tiếp kiểm tra xem phần mềm có đáp ứng đúng nhu cầu nghiệp vụ để ký nghiệm thu | Chia thành **알파 테스트 (Alpha Test - có Dev)** và **베타 테스트 (Beta Test - ngoài thực địa)** |

- **So sánh hai phương thức Kiểm thử tích hợp (통합 테스트):**

| Phương thức tích hợp | Đặc điểm vận hành | Ưu điểm | Nhược điểm cốt lõi (Bẫy thi) |
| :--- | :--- | :--- | :--- |
| **빅뱅 통합 (Big Bang)** | Lắp ghép tất cả các mô-đun lại với nhau **cùng một lúc** rồi tiến hành kiểm thử toàn diện | Phù hợp với các phần mềm quy mô rất nhỏ, tốn ít thời gian chuẩn bị | **Rất khó định vị vị trí và nguyên nhân gây lỗi (원인 식별 곤란)** do lỗi phát sinh từ nhiều chỗ cùng lúc |
| **점진적 통합 (Incremental)** | Tích hợp **từng bước lần lượt từng mô-đun** vào hệ thống (Top-down dùng Stub, Bottom-up dùng Driver) | **Dễ dàng xác định nguyên nhân lỗi** (vì lỗi xảy ra ngay tại mô-đun vừa thêm vào); kiểm tra giao diện triệt để | Tốn công sức và thời gian viết các công cụ giả lập giàn giáo (Stub, Driver) |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Kiểm thử phi chức năng trong Kiểm thử hệ thống (System Testing):**
  - **Kiểm thử hiệu năng (Performance Testing):** Xác định tốc độ xử lý và thời gian đáp ứng của giao dịch (Response time).
  - **Kiểm thử chịu tải (Load Testing):** Đưa số lượng người dùng đồng thời tăng dần đến giới hạn thiết kế để đo độ ổn định.
  - **Kiểm thử áp lực quá tải (Stress Testing):** Đưa tải vượt ngưỡng chịu đựng tối đa để tìm điểm sập (Breaking Point) và cách hệ thống phục hồi.
  - **Kiểm thử bảo mật (Security Testing):** Rà quét các lỗ hổng Injection, XSS, kiểm tra mã hóa dữ liệu nhạy cảm.

### 복습 체크리스트
- [ ] Nhớ 4 tầng kiểm thử V-Model: 단위 (Unit) $\rightarrow$ 통합 (Integration) $\rightarrow$ 시스템 (System) $\rightarrow$ 인수 (Acceptance).
- [ ] Phân biệt được 빅뱅 통합 (ghép 1 cục) và 점진적 통합 (ghép từng bước).
- [ ] Nhớ nhược điểm lớn nhất của Big Bang: Khó tìm ra nguyên nhân và vị trí gây lỗi.
- [ ] Nêu được các nội dung kiểm thử phi chức năng trong Kiểm thử hệ thống.
