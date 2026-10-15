# 2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)

## 학습 목표 (Mục tiêu)
- Nắm vững các quy tắc và nguyên tắc vàng khi tổ chức Đánh giá kỹ thuật chính thức (`FTR - Formal Technical Review`) cho tài liệu giao diện hệ thống.
- Hệ thống hóa 4 phương pháp rà soát kiểm tra giao diện: Đánh giá đồng cấp (`동료검토`), Rà soát từng bước (`워크스루`), Thanh tra chuyên gia (`인스펙션`), và Tạo mẫu thử (`프로토타이핑`).
- Nắm vững các kỹ thuật liên kết hệ thống thông dụng: `DB Link`, `API / Open API`, `EAI`, `ESB`, và `Socket`.

## 핵심 키워드 (Từ khóa)
- FTR (Formal Technical Review / 정형 기술 검토)
- 검토 원칙 (Nguyên tắc FTR: 제품 중심, 결함 발견 집중, 시간 제한)
- 인스펙션 (Inspection / 공식 검토 / 체크리스트)
- 시스템 연계 기술 (Kỹ thuật liên kết hệ thống)
- DB Link / API / Socket
- EAI (Enterprise Application Integration)
- ESB (Enterprise Service Bus)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([11. 디자인 패턴](37-bai-hoc.md)):** Sau khi hoàn thành thiết kế các mẫu GoF, bài này chuyển sang kỹ thuật kiểm soát chất lượng giao diện và liên kết các phân hệ trong môi trường doanh nghiệp.
- **Tiếp nối sang bài sau ([13. 시스템 연계 및 인터페이스](39-bai-hoc.md)):** Khảo sát chi tiết 4 mô hình kiến trúc của EAI (Point-to-Point, Hub & Spoke, Message Bus, Hybrid) và so sánh chuyên sâu với ESB.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc các nguyên tắc vàng của FTR: chỉ tập trung vào sản phẩm (không công kích cá nhân tác giả), chỉ vạch lỗi (không tranh cãi cách sửa ngay trong buổi họp), và giới hạn thời gian (dưới 2 giờ).
- Đọc TẦNG B để hiểu rõ tại sao việc phát hiện lỗi giao diện (Interface Bug) trước khi lập trình lại có ý nghĩa sống còn trong các dự án tích hợp nhiều ngân hàng và đối tác.

---

## 2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Formal Technical Review (FTR - 정형 기술 검토):**
  - **Khái niệm:** Là quy trình kiểm tra, rà soát có cấu trúc và chính thức đối với các sản phẩm tài liệu kỹ thuật, đặc tả giao diện và thiết kế bởi một nhóm kỹ sư nhằm phát hiện các khiếm khuyết sớm.
  - **5 nguyên tắc vàng khi tổ chức FTR (Bắt buộc phải thuộc):**
    1. **Tập trung vào sản phẩm, không công kích người viết (`제품의 검토에 집중 / 작성자 비판 금지`)**: Rà soát tài liệu thiết kế chứ không đánh giá năng lực cá nhân của lập trình viên.
    2. **Chỉ tập trung vào việc tìm kiếm lỗi, không tranh luận tìm giải pháp sửa chữa (`결함의 발견에 집중 / 해결책 논쟁 배제`)**: Buổi FTR chỉ ghi nhận danh sách lỗi; việc sửa lỗi như thế nào do tác giả nghiên cứu sau buổi họp.
    3. **Chuẩn bị tài liệu trước và giới hạn thời gian họp (`사전 준비 필수 / 시간 엄수`)**: Các thành viên phải đọc tài liệu trước khi họp; thời lượng họp tiêu chuẩn **từ 1 đến 2 giờ**, số người tham gia từ 3 đến 5 người.
    4. **Duy trì biên bản cuộc họp và danh mục checklist rõ ràng (`의제와 체크리스트 준수`)**: Ghi chép chính xác danh mục lỗi để theo dõi tiến độ khắc phục.
    5. **Tất cả các thành viên phải được đào tạo bài bản về quy trình rà soát.**
- **2. Bảng 4 phương pháp kiểm tra giao diện:**
  - `동료검토 (Peer Review)`: Tác giả trực tiếp giải thích nội dung cho đồng nghiệp nghe, thảo luận phi chính thức.
  - `워크스루 (Walkthrough)`: Gửi tài liệu trước, họp ngắn rà soát từng kịch bản nghiệp vụ để tìm lỗi, mang tính phi chính thức (`비공식적`).
  - `인스펙션 (Inspection)`: **Chính thức và khắt khe nhất (`공식적인 검토`)**. Tác giả không điều hành; nhóm chuyên gia thẩm định độc lập soi xét tài liệu dựa trên bảng tiêu chí (Checklist).
  - `프로토타이핑 (Prototyping)`: Xây dựng giao diện mẫu chạy thử để người dùng trực tiếp nghiệm thu luồng liên kết.
- **3. Các công nghệ liên kết hệ thống (시스템 연계 기술):**
  - `DB Link`: Sử dụng đối tượng liên kết cơ sở dữ liệu có sẵn của DBMS (như Oracle DB Link) để truy vấn bảng của CSDL từ xa qua câu lệnh SQL (`SELECT * FROM table@remote_db`).
  - `API / Open API`: Cung cấp các hàm giao diện lập trình mở cổng qua giao thức mạng HTTP/HTTPS (RESTful, SOAP) để các hệ thống bên ngoài gọi dịch vụ.
  - `EAI (Enterprise Application Integration)`: Nền tảng phần mềm trung gian giúp tích hợp các ứng dụng không đồng nhất trong nội bộ doanh nghiệp.
  - `ESB (Enterprise Service Bus)`: Trục liên kết dịch vụ theo kiến trúc hướng dịch vụ (SOA), kết nối lỏng lẻo (Loosely coupled) giữa các hệ thống thông qua các chuẩn web service (WSDL, SOAP).
  - `Socket`: Lập trình truyền nhận dữ liệu trực tiếp ở tầng giao vận (TCP/UDP) giữa các cổng mạng máy chủ.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1 (Nguyên tắc FTR):** *"Trong buổi FTR, nhóm kiểm tra cần thảo luận và viết ngay mã nguồn giải pháp sửa chữa lỗi tại chỗ?"* -> **Sai hoàn toàn**. FTR **chỉ tập trung phát hiện lỗi (결함 발견에 집중)**, tuyệt đối không biến buổi họp thành tranh luận giải pháp.
  - **Bẫy 2:** *"Thời lượng họp FTR lý tưởng là bao lâu?"* -> **Từ 1 đến 2 giờ (1~2시간 이내)**, không kéo dài cả ngày gây mệt mỏi và mất tập trung.
  - **Bẫy 3:** *"Phương pháp rà soát nào là chính thức sử dụng bảng checklist?"* -> **인스펙션 (Inspection)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "FTR soi sản phẩm chứ không soi người, chỉ vạch lỗi chứ không tranh cãi giải pháp; Liên kết hệ thống dùng DB Link, API, EAI, ESB và Socket".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tình huống thực tế áp dụng các công nghệ liên kết:**
  - Khi cần kết nối 2 cơ sở dữ liệu Oracle nội bộ nằm trong cùng một mạng LAN tốc độ cao: Dùng **DB Link** cho tiện lợi và nhanh chóng.
  - Khi cần kết nối website thương mại điện tử với Cổng thanh toán VnPay hay ngân hàng: Dùng **Open API (RESTful JSON)** qua HTTPS để đảm bảo bảo mật và độc lập nền tảng.
  - Khi một tập đoàn viễn thông có 50 phân hệ phần mềm cũ mới (ERP, CRM, Billing, Quản lý kho) cần liên kết đồng bộ hóa dữ liệu khách hàng: Sử dụng **EAI hoặc ESB**.

### 복습 체크리스트
- [ ] Nhớ 4 nguyên tắc cốt lõi của FTR (soi sản phẩm không soi người, chỉ vạch lỗi, giới hạn 1-2h, dùng checklist).
- [ ] Phân biệt được sự khác biệt giữa Walkthrough (phi chính thức) và Inspection (chính thức, checklist).
- [ ] Kể tên 5 công nghệ liên kết hệ thống phổ biến: DB Link, API, EAI, ESB, Socket.
- [ ] Nhận diện được các phát biểu sai về FTR trong câu hỏi trắc nghiệm.
