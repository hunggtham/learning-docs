# 105: 시각에 따른 테스트 (Verification vs Validation)

## 학습 목표 (Mục tiêu)
- Phân biệt sâu sắc và toàn diện giữa hai góc nhìn cốt lõi trong đánh giá chất lượng phần mềm: Kiểm tra xác minh (검증 - Verification) và Kiểm tra xác nhận (확인 - Validation).
- Nằm lòng hai câu hỏi kinh điển của Barry Boehm định vị ranh giới giữa Verification ("Are we building the product right?") và Validation ("Are we building the right product?").
- Nhận biết các hoạt động kiểm thử và tài liệu đối chiếu đặc trưng của từng góc nhìn trong các câu hỏi tình huống thi trắc nghiệm.

## 핵심 키워드 (Từ khóa)
- 검증 (Verification / 개발자 관점 / 명세서 준수)
- 확인 (Validation / 사용자 관점 / 고객 요구 충족)
- Barry Boehm의 정의
- "Are we building the product right?" (검증)
- "Are we building the right product?" (확인)
- 단위·통합 테스트 (검증) vs 시스템·인수 테스트 (확인)

## 선행·연결 개념 (Kiến thức liên kết)
- [53-bai-hoc.md](53-bai-hoc.md): 4 cấp độ kiểm thử phần mềm từ Đơn vị đến Chấp nhận.
- [57-bai-hoc.md](57-bai-hoc.md): 7 nguyên lý kiểm thử phần mềm cơ bản.
- [60-bai-hoc.md](60-bai-hoc.md): Phân bổ Verification và Validation trên hai nhánh của V-Model.

## 읽는 방법 (Cách đọc)
- Nhớ câu mẹo ghi nhớ bằng tiếng Việt:
  - **Kiểm tra xác minh (Verification):** Dev tự hỏi: "Mình code có đúng thiết kế và chuẩn kỹ thuật không?" $\rightarrow$ Nhìn vào **Bản vẽ đặc tả (Spec)**.
  - **Kiểm tra xác nhận (Validation):** Khách hàng hỏi: "Phần mềm này có giải quyết đúng bài toán thực tế của tôi không?" $\rightarrow$ Nhìn vào **Nhu cầu nghiệp vụ thực tế (Requirement)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng đối đầu chi tiết Verification (검증) vs Validation (확인):**

| Tiêu chí so sánh | 검증 (Verification - Kiểm tra xác minh) | 확인 (Validation - Kiểm tra xác nhận) |
| :--- | :--- | :--- |
| **Góc nhìn chủ thể** | Góc nhìn của **Nhà phát triển (Developer / Engineer)** | Góc nhìn của **Người sử dụng / Khách hàng (User / Customer)** |
| **Câu hỏi triết lý (Barry Boehm)** | *"Are we building the product right?"* (Chúng ta có đang xây dựng sản phẩm đúng quy chuẩn kỹ thuật không?) | *"Are we building the right product?"* (Chúng ta có đang xây dựng đúng sản phẩm mà khách hàng cần không?) |
| **Mục đích cốt lõi** | Kiểm tra xem sản phẩm của một giai đoạn phát triển có **thỏa mãn đầy đủ các điều kiện do giai đoạn trước đó đặt ra** hay không | Kiểm tra xem sản phẩm phần mềm hoàn thiện có **đáp ứng đúng mục đích sử dụng thực tế và kỳ vọng nghiệp vụ của người dùng** hay không |
| **Đối tượng căn cứ** | Bản đặc tả kiến trúc, tài liệu thiết kế chi tiết, tiêu chuẩn lập trình | Mục tiêu kinh doanh, nhu cầu thực tế của người dùng cuối |
| **Các hoạt động tiêu biểu** | Rà soát mã (Code Review), Kiểm tra tài liệu (Inspection, Walkthrough), **Kiểm thử đơn vị (Unit Test)**, **Kiểm thử tích hợp (Integration Test)** | **Kiểm thử hệ thống (System Test)**, **Kiểm thử chấp nhận (Acceptance Test)**, Kiểm thử thực địa (Alpha / Beta Test) |

- **Bẫy đề thi trắc nghiệm:**
  - **Bẫy 1:** *"Hoạt động nào sau đây thuộc góc nhìn 검증 (Verification)?"* $\rightarrow$ Tìm các hoạt động kiểm tra code, kiểm tra thiết kế, Unit test, Review.
  - **Bẫy 2:** *"Hoạt động nào sau đây thuộc góc nhìn 확인 (Validation)?"* $\rightarrow$ Tìm các hoạt động nghiệm thu người dùng, Beta test, Acceptance test.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ví dụ phân biệt thực tế kinh điển:**
  - Một nhóm phát triển phần mềm nhận yêu cầu làm tính năng đăng nhập cho khách hàng VIP.
  - Nhóm thiết kế và lập trình tính năng đăng nhập bằng nhận diện khuôn mặt 3D cực kỳ tinh vi, mã nguồn viết chuẩn Clean Code 100%, không một con bug, Unit Test bao phủ 100% $\rightarrow$ **Giai đoạn 검증 (Verification) hoàn hảo tuyệt đối (PASS)**.
  - Nhưng khi bàn giao ra thực tế, khách hàng VIP lại sử dụng máy tính bàn không hề có camera! Khách hàng không thể đăng nhập được và yêu cầu hoàn tiền $\rightarrow$ **Giai đoạn 확인 (Validation) hoàn toàn thất bại (FAIL)**!
  - Bài học: Phần mềm dù Verification đạt điểm tối đa nhưng nếu Validation bị Fail thì vẫn là một dự án thất bại hoàn toàn.

### 복습 체크리스트
- [ ] Nhớ câu hỏi của Verification: "Are we building the product right?" (개발자 관점).
- [ ] Nhớ câu hỏi của Validation: "Are we building the right product?" (사용자 관점).
- [ ] Phân loại đúng Unit Test và Integration Test thuộc Verification.
- [ ] Phân loại đúng Acceptance Test và System Test thuộc Validation.
