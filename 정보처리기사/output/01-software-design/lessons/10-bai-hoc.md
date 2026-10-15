# 12. 요구사항 (Requirements)

## 학습 목표 (Mục tiêu)
- Nắm vững quy trình phân tích yêu cầu 5 bước tiêu chuẩn trong kỹ nghệ phần mềm: Sàng lọc -> Chuẩn bị tài liệu -> Phân loại -> Phân tích và hiệu chỉnh -> Chuyển giao.
- Khắc sâu vai trò của việc thiết lập Đường cơ sở (`베이스라인 - Baseline`) trước khi bước vào giai đoạn thiết kế và lập trình.
- Thuộc nằm lòng 7 tiêu chí chất lượng của tài liệu đặc tả yêu cầu (`요구사항 품질 기준 7개`): Tính đầy đủ, Tính nhất quán, Tính rõ ràng, Tính chức năng, Khả năng kiểm chứng, Khả năng truy xuất, và Tính dễ sửa đổi.

## 핵심 키워드 (Từ khóa)
- 요구사항 분석 절차 (Quy trình phân tích yêu cầu 5 bước)
- 베이스라인 (Đường cơ sở / Baseline)
- 요구사항 품질 기준 (7 tiêu chí chất lượng đặc tả yêu cầu)
- 완전성 (Tính đầy đủ / Completeness)
- 일관성 (Tính nhất quán / Consistency)
- 명확성 (Tính rõ ràng, không mơ hồ / Unambiguity)
- 검증 가능성 (Khả năng kiểm chứng / Verifiability)
- 추적 가능성 (Khả năng truy vết / Traceability)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([1. 요구사항 개발 기법](09-bai-hoc.md)):** Sau khi thu thập yêu cầu từ các buổi phỏng vấn, khảo sát và Brainstorming, bài này tiến hành chuẩn hóa việc phân tích và đánh giá chất lượng các yêu cầu đó theo bộ tiêu chí khắt khe.
- **Tiếp nối sang bài sau ([A+ Deep Dive: 개발 모형 선택과 요구사항 검증](11-bai-hoc.md)):** Tổng hợp toàn bộ các mô hình phát triển phần mềm và xây dựng ma trận so sánh các bẫy đề thi nâng cao về thẩm định và truy vết yêu cầu.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để ghi nhớ chắc chắn 7 tiêu chí chất lượng đặc tả yêu cầu - đề thi thường đưa ra một phát biểu mơ hồ rồi hỏi vi phạm tiêu chí nào (ví dụ câu chữ định tính vi phạm Tính kiểm chứng được).
- Đọc TẦNG B để hiểu cơ chế thiết lập Ma trận truy vết yêu cầu (RTM - Requirements Traceability Matrix) từ yêu cầu đến các ca kiểm thử.

---

## 12. 요구사항 (Requirements)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **요구사항 분석 5단계 절차 (Quy trình 5 bước phân tích yêu cầu):**
  1. `선별 (Sàng lọc / Lập danh sách)`: Liệt kê toàn bộ các yêu cầu thu thập được từ người dùng.
  2. `자료 준비 (Chuẩn bị tài liệu)`: Thu thập các biểu mẫu nghiệp vụ, tài liệu hệ thống cũ và quy chuẩn liên quan.
  3. `분류 (Phân loại)`: Nhóm các yêu cầu thành Nhóm chức năng (Functional) và Nhóm phi chức năng (Non-functional).
  4. `분석 및 수정 (Phân tích và hiệu chỉnh)`: Làm rõ các điểm mâu thuẫn, loại bỏ các yêu cầu phi thực tế hoặc trùng lặp.
  5. `전달 (Chuyển giao)`: Bàn giao tài liệu yêu cầu hoàn chỉnh cho nhóm thiết kế và các bên liên quan.
- **요구사항 검증 및 베이스라인 (Thẩm định và chốt Baseline):**
  - Trước khi bắt đầu thiết kế (`설계`) và lập trình (`구현`), tài liệu yêu cầu phải được kiểm chứng toàn diện và chính thức phê duyệt làm **Đường cơ sở (베이스라인 - Baseline)**.
  - Sau khi chốt Baseline, mọi yêu cầu thay đổi (`변경 관리`) đều phải qua quy trình kiểm soát thay đổi chính thức để tránh phá vỡ phạm vi dự án.
- **요구사항 품질 기준 7개 (7 tiêu chí chất lượng của tài liệu yêu cầu):**
  1. **완전성 (Completeness - Tính đầy đủ):** Tất cả các chức năng, ràng buộc của người dùng và hệ thống đều được phản ánh đầy đủ, không bị bỏ sót bất kỳ luồng xử lý nào.
  2. **일관성 (Consistency - Tính nhất quán):** Không có sự mâu thuẫn hay xung đột logic giữa các yêu cầu trong cùng một tài liệu (ví dụ: một chỗ viết "cho phép xóa user", chỗ khác viết "tuyệt đối không được xóa user").
  3. **명확성 (Unambiguity - Tính rõ ràng):** Mỗi câu phát biểu yêu cầu chỉ có duy nhất một cách hiểu, không dùng từ ngữ mơ hồ, đa nghĩa.
  4. **기능성 (Functionality - Tính chức năng):** Tập trung vào việc mô tả hệ thống **Làm cái gì (`무엇을 - What`)** thay vì can thiệp vào việc lập trình viên phải **Làm như thế nào (`어떻게 - How`)**.
  5. **검증 가능성 (Verifiability - Khả năng kiểm chứng):** Mỗi yêu cầu đều có thể kiểm tra hoặc đo lường được bằng các tiêu chí định lượng cụ thể thông qua kiểm thử.
  6. **추적 가능성 (Traceability - Khả năng truy xuất):** Mỗi yêu cầu đều có mã định danh (ID) duy nhất và có thể truy ngược về nguồn gốc người dùng cũng như truy xuôi đến các mô-đun thiết kế, mã nguồn và ca kiểm thử tương ứng.
  7. **변경 용이성 (Easily Changeable - Tính dễ sửa đổi):** Cấu trúc tài liệu đặc tả có mục lục, chỉ mục rõ ràng để khi có yêu cầu thay đổi có thể chỉnh sửa nhanh chóng mà không làm rối loạn toàn bộ hệ thống.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1 (Verifiability trap):** Phát biểu *"Hệ thống phải có giao diện thân thiện và thời gian phản hồi nhanh"* vi phạm tiêu chí nào? -> **Vi phạm Tính kiểm chứng được (검증 가능성)** và Tính rõ ràng (명확성) vì "thân thiện", "nhanh" là từ ngữ cảm tính, không thể kiểm thử nghiệm thu định lượng được. Phải sửa thành: "Thời gian phản hồi trang dưới 1.5 giây với 1.000 user truy cập".
  - **Bẫy 2 (Functionality trap):** Yêu cầu viết *"Hệ thống phải sử dụng thuật toán QuickSort và mảng động trong C++ để sắp xếp danh sách"* vi phạm tiêu chí nào? -> **Vi phạm Tính chức năng (기능성)** vì tài liệu yêu cầu chỉ nên quy định "hệ thống sắp xếp danh sách theo tên tăng dần", không được can thiệp vào chi tiết kỹ thuật cài đặt bên trong.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Quy trình phân tích 5 bước chốt Baseline; tài liệu yêu cầu chuẩn phải Đầy đủ, Nhất quán, Rõ ràng, Định tính What, Kiểm chứng số đo, Truy vết ID, và Dễ sửa đổi".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ma trận truy xuất yêu cầu (Requirements Traceability Matrix - RTM):**
  - RTM là một bảng ánh xạ hai chiều:
    - Cột 1: Mã yêu cầu (`REQ_001`)
    - Cột 2: Mô tả yêu cầu (Đăng nhập bằng vân tay)
    - Cột 3: Mô-đun thiết kế (`MOD_AUTH`)
    - Cột 4: Tệp mã nguồn (`BiometricAuth.java`)
    - Cột 5: Mã ca kiểm thử (`TC_001_FINGERPRINT`)
  - Khi khách hàng muốn đổi logic của `REQ_001`, kỹ sư nhìn vào RTM có thể biết ngay cần sửa file code nào và chạy lại test case nào, tránh việc sửa một tính năng mà vô tình làm hỏng các tính năng khác.

### 복습 체크리스트
- [ ] Nhớ thứ tự 5 bước của quy trình phân tích yêu cầu (Sàng lọc -> Chuẩn bị -> Phân loại -> Phân tích/Sửa -> Chuyển giao).
- [ ] Định nghĩa được 베이스라인 (Baseline) và mốc thời gian thiết lập nó (trước thiết kế và cài đặt).
- [ ] Thuộc tên 7 tiêu chí chất lượng đặc tả yêu cầu: 완전성, 일관성, 명확성, 기능성, 검증 가능성, 추적 가능성, 변경 용이성.
- [ ] Nhận diện được lỗi viết yêu cầu định tính vi phạm 검증 가능성 (Khả năng kiểm chứng).
