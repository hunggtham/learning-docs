# A+ Deep Dive: 개발 모형 선택과 요구사항 검증

## 학습 목표 (Mục tiêu)
- Nắm vững bảng ma trận đối chiếu tổng hợp các tiêu chí lựa chọn mô hình phát triển phần mềm (Thác nước, Nguyên mẫu, Xoắn ốc, Agile) dựa trên mức độ bất định và rủi ro.
- Phân biệt bản chất giữa Xác minh (`검증 - Verification`) và Xác nhận (`확인 - Validation`) trong kiểm chứng yêu cầu.
- Giải mã các bẫy đề thi nâng cao thường gặp nhất trong Môn 1 về phân biệt hạng mục quản lý cấu hình (`형상 관리`), tích hợp EAI và biểu đồ N-S.

## 핵심 키워드 (Từ khóa)
- 개발 모형 선택 (Lựa chọn mô hình phát triển / Development Model Selection)
- 위험 관리 (Quản lý rủi ro / Risk Management)
- 검증 vs 확인 (Xác minh vs Xác nhận / Verification vs Validation)
- 형상 관리 항목 (Hạng mục quản lý cấu hình / Configuration Items: 산출물, 코드, 문서)
- EAI Hybrid (Mô hình tích hợp ứng dụng doanh nghiệp lai / Hub-and-Spoke + Bus)
- N-S 차트 (Nassi-Schneiderman Chart / 구조적 제어 흐름)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([01-bai-hoc.md](01-bai-hoc.md) đến [10-bai-hoc.md](10-bai-hoc.md)):** Đây là bài học tổng hợp nâng cao (Deep Dive), xâu chuỗi toàn bộ kiến thức của Cụm 1 về SDLC, phương pháp luận phát triển và kỹ nghệ yêu cầu.
- **Tiếp nối sang cụm sau ([1. 현행 시스템 분석](12-bai-hoc.md)):** Khởi đầu Cụm 2 về khảo sát kiến trúc hệ thống hiện trạng, hạ tầng phần cứng, mạng và mô hình hóa UML.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nắm ma trận đối chiếu 4 mô hình SDLC và 4 tiêu chuẩn vàng phân biệt bẫy đề thi hay gặp.
- Đọc TẦNG B để theo dõi luồng tư duy giải quyết câu hỏi tình huống phức tạp trong đề thi trắc nghiệm và thực hành tự luận.

---

## A+ Deep Dive: 개발 모형 선택과 요구사항 검증

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng ma trận đối chiếu lựa chọn mô hình SDLC:**
  - **폭포수 모형 (Waterfall):**
    - `Tín hiệu nhận diện mạnh nhất:` Yêu cầu đã ổn định, rõ ràng ngay từ đầu, các sản phẩm bàn giao từng bước minh bạch.
    - `Khả năng ứng phó thay đổi:` Thấp (`낮음`).
    - `Bẫy đề thi:` "Tuần tự" không có nghĩa là không kiểm thử; kiểm thử được thực hiện quy củ ở cuối chu trình.
  - **프로토타입 모형 (Prototype):**
    - `Tín hiệu nhận diện mạnh nhất:` Khách hàng chưa hình dung rõ giao diện và tính năng cần thiết, khó diễn đạt bằng lời.
    - `Khả năng ứng phó thay đổi:` Cao trong khâu làm rõ yêu cầu.
    - `Bẫy đề thi:` Bản mẫu thử nghiệm (시제품) không được dùng làm sản phẩm vận hành chính thức vì thiếu cấu trúc bảo mật và chịu tải.
  - **나선형 모형 (Spiral):**
    - `Tín hiệu nhận diện mạnh nhất:` Dự án quy mô lớn, tính phức tạp cao, tiềm ẩn nhiều rủi ro công nghệ mới chưa kiểm chứng.
    - `Khả năng ứng phó thay đổi:` Rất cao qua từng vòng lặp nhờ bước **Phân tích rủi ro (`위험 분석`)**.
    - `Bẫy đề thi:` Nhà khoa học Boehm là tác giả của mô hình Xoắn ốc (나선형).
  - **애자일 (Agile):**
    - `Tín hiệu nhận diện mạnh nhất:` Chu kỳ phát triển ngắn (2-4 tuần), đòi hỏi phản hồi liên tục và chuyển giao phần mềm chạy được nhanh chóng.
    - `Khả năng ứng phó thay đổi:` Rất cao (`매우 높음`).
    - `Bẫy đề thi:` Agile không phải là một phương pháp đơn lẻ mà là một triết lý gồm nhiều phương pháp luận (Scrum, XP, Kanban).
- **Phân biệt cốt lõi: 검증 (Verification) vs 확인 (Validation):**
  - **검증 (Verification - Xác minh):** "Có làm sản phẩm đúng theo đặc tả thiết kế không?" (`Are we building the product right?`). Đánh giá xem phần mềm có tuân thủ đúng tài liệu kỹ thuật, tiêu chuẩn lập trình và quy chuẩn thiết kế hay không.
  - **확인 (Validation - Xác nhận):** "Có làm đúng sản phẩm người dùng thực sự cần không?" (`Are we building the right product?`). Đánh giá xem phần mềm có giải quyết đúng bài toán nghiệp vụ và đem lại giá trị thực tế cho khách hàng hay không.
- **Điểm phân biệt bẫy đề thi hay gặp trong Môn 1:**
  - `Hạng mục quản lý cấu hình (형상 관리 항목 - Configuration Item):` Bao gồm mã nguồn (`소스 코드`), tài liệu yêu cầu (`요구사항 명세서`), tài liệu thiết kế (`설계서`), tài liệu hướng dẫn cài đặt và vận hành. **Bẫy:** Ngân sách dự án (`예산`) hay Lịch trình cá nhân (`개인 일정`) KHÔNG PHẢI là hạng mục quản lý cấu hình.
  - `EAI Hybrid Architecture:` Là sự kết hợp giữa kiến trúc trung tâm (Hub-and-Spoke) và kiến trúc trục truyền thông điệp (Message Bus). Không được nhầm với Point-to-Point (kết nối trực tiếp điểm-điểm).
  - `N-S 차트 (Nassi-Schneiderman Chart):` Biểu diễn trực quan 3 cấu trúc điều khiển cơ bản (Tuần tự - 순차, Lựa chọn - 선택, Lặp - 반복) không dùng mũi tên goto. Không biểu diễn cấu trúc bộ nhớ hay gói tin mạng.
  - `Độ độc lập của mô-đun (모듈 독립성):` Để hệ thống dễ bảo trì, nguyên tắc vàng là **Giảm độ kết hợp (결합도 낮춤) và Tăng độ gắn kết (응집도 높임)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Verification kiểm tra theo thiết kế, Validation kiểm tra theo nhu cầu khách hàng; Quản lý cấu hình lưu sản phẩm bàn giao, không lưu tiền và lịch cá nhân".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Quy trình thẩm định yêu cầu thu nhỏ (Mini-Trace):**
  - Khi cầm trên tay một tài liệu yêu cầu, kỹ sư tiến hành kiểm tra 4 lát cắt sống còn:
    1. `완전성 (Completeness)`: Đã có đủ xử lý cho cả trường hợp bình thường lẫn ngoại lệ (Error handling) chưa?
    2. `일관성 (Consistency)`: Có xung đột về mặt thuật ngữ và dữ liệu giữa các chương không?
    3. `추적성 (Traceability)`: Mỗi gạch đầu dòng yêu cầu có sinh ra ít nhất một ca kiểm thử tương ứng không?
    4. `검증 가능성 (Verifiability)`: Thay vì viết câu cảm tính như "Ứng dụng phải cực kỳ ổn định", yêu cầu đã được lượng hóa thành "Tỷ lệ thời gian hoạt động đạt 99.95% mỗi tháng" chưa?
- **Phân tích bẫy tình huống đề thi:**
  - *"Một công ty Fintech muốn phát triển hệ thống giao dịch tự động tiền mã hóa mới hoàn toàn với công nghệ blockchain phân tán, đội ngũ kỹ sư chưa từng có kinh nghiệm về blockchain. Mô hình nào phù hợp nhất?"*
    - **Phân tích:** Công nghệ mới, độ bất định cực cao, rủi ro mất an toàn vốn rất lớn. Mô hình tối ưu là **나선형 모형 (Spiral Model)** vì có khâu `위험 분석` lặp lại để thử nghiệm tính khả thi trước khi mở rộng quy mô.

### 복습 체크리스트
- [ ] Phân tích được ma trận lựa chọn mô hình SDLC theo mức độ rủi ro và tính ổn định của yêu cầu.
- [ ] Phân biệt được câu hỏi tiếng Anh kinh điển: Verification (right?) vs Validation (right product?).
- [ ] Nhận diện được hạng mục nào thuộc 형상 관리 항목 (sản phẩm bàn giao) và hạng mục nào không thuộc (tiền bạc, lịch cá nhân).
- [ ] Nắm được nguyên tắc tối ưu hóa mô-đun: 결합도는 낮추고 응집도는 높인다.
