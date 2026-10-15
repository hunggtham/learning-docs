# 10. 요구사항 심화 (Yêu cầu chuyên sâu)

## 학습 목표 (Mục tiêu)
- Phân biệt chi tiết giữa Kỹ thuật đặc tả hình thức (`정형 명세 기법`) và Kỹ thuật đặc tả phi hình thức (`비정형 명세 기법`), nắm rõ ưu nhược điểm và ví dụ tiêu biểu của từng loại.
- Ghi nhớ các công cụ CASE tự động hóa phân tích yêu cầu kinh điển trong đề thi: SADT, SREM (RSL/REVS), PSL/PSA và TAGS.
- Nắm vững các kỹ thuật thu thập yêu cầu người dùng (`요구사항 도출 기법`) phổ biến trong thực tế.

## 핵심 키워드 (Từ khóa)
- 정형 명세 기법 (Kỹ thuật đặc tả hình thức / Formal Specification: 수학적 기호, Z, VDM, Petri-net)
- 비정형 명세 기법 (Kỹ thuật đặc tả phi hình thức / Informal Specification: 자연어, FSM, State Chart)
- CASE 도구 (Công cụ kỹ nghệ phần mềm máy tính hỗ trợ / Computer-Aided Software Engineering)
- SADT (Structured Analysis and Design Technique / SoftTech)
- SREM (Software Requirements Engineering Methodology / TRW / RSL·REVS)
- PSL/PSA (Problem Statement Language / Analyzer)
- TAGS (Technology for Automated Generation of Systems)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([9. 요구사항 및 시스템 파악](05-bai-hoc.md)):** Sau khi xem xét quy trình rà soát và hiện trạng hệ thống, bài này đi sâu vào cách thức biểu diễn các yêu cầu một cách chặt chẽ bằng toán học hoặc ngôn ngữ tự nhiên.
- **Tiếp nối sang bài sau ([2. 요구사항 정의](07-bai-hoc.md)):** Tổng hợp định nghĩa yêu cầu và bảng so sánh toàn diện chức năng và phi chức năng nhằm định hình tài liệu chuẩn trước khi bước sang pha thiết kế kiến trúc.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc nằm lòng phân loại: Z, VDM, Petri-net thuộc `정형` (Toán học); FSM, Decision Table thuộc `비정형` (Ngôn ngữ tự nhiên / Đồ thị).
- Đọc TẦNG B để hiểu tại sao trong các hệ thống đòi hỏi độ an toàn tuyệt đối (hàng không, y tế), các kỹ sư bắt buộc phải áp dụng đặc tả hình thức bằng toán học.

---

## 10. 요구사항 심화 (Yêu cầu chuyên sâu)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **So sánh 2 kỹ thuật đặc tả yêu cầu (명세 기법):**
  - **1. 정형 명세 기법 (Formal Specification - Kỹ thuật đặc tả hình thức):**
    - **Cơ sở biểu diễn:** Dựa trên **Ký hiệu toán học (`수학적 기호`)**, lý thuyết tập hợp, logic vị từ.
    - **Ưu điểm:** Tính chính xác (`정확성`), ngắn gọn, súc tích, hoàn toàn nhất quán (`일관성`), không bị hiểu đa nghĩa, có thể chứng minh tính đúng đắn bằng toán.
    - **Nhược điểm:** Cú pháp khó, người dùng (`사용자`) và khách hàng không có nền tảng toán học sẽ không hiểu được, tốn nhiều công sức đào tạo.
    - **Các công cụ/ngôn ngữ tiêu biểu:** **VDM, Z, Petri-net, CSP**.
  - **2. 비정형 명세 기법 (Informal Specification - Kỹ thuật đặc tả phi hình thức):**
    - **Cơ sở biểu diễn:** Dựa trên **Ngôn ngữ tự nhiên (`자연어`)** và các loại biểu đồ, hình vẽ (`다이어그램`).
    - **Ưu điểm:** Dễ hiểu, người dùng và các bên liên quan dễ dàng trao đổi, giao tiếp thuận tiện (`의사소통이 용이`).
    - **Nhược điểm:** Dễ phát sinh tính mơ hồ (`모호성`), đa nghĩa, phụ thuộc vào văn phong người viết, khó tự động hóa việc kiểm tra tính nhất quán.
    - **Các công cụ tiêu biểu:** **FSM (Finite State Machine), Decision Table (Bảng quyết định), ERD, State Chart**.
- **Các công cụ CASE tự động hóa phân tích yêu cầu:**
  - `SADT (Structured Analysis and Design Technique)`: Do SoftTech phát triển, công cụ phân tích và thiết kế theo cấu trúc phân rã chức năng.
  - `SREM (Software Requirements Engineering Methodology)`: Do hãng TRW phát triển cho các hệ thống xử lý thời gian thực (`실시간 처리 시스템`), sử dụng ngôn ngữ RSL (Requirements Statement Language) và bộ phân tích REVS.
  - `PSL/PSA (Problem Statement Language / Problem Statement Analyzer)`: Phát triển bởi Đại học Michigan, dùng ngôn ngữ mô tả bài toán và bộ phân tích tự động.
  - `TAGS (Technology for Automated Generation of Systems)`: Công cụ tự động hóa tích hợp cho toàn bộ vòng đời phát triển hệ thống (`개발 주기 전 과정`).
- **Các kỹ thuật thu thập yêu cầu (요구사항 도출 기법):**
  - Phỏng vấn (`인터뷰`), Bảng câu hỏi khảo sát (`설문조사`), Công não (`브레인스토밍`), Hội thảo chuyên đề (`워크숍`), Tạo nguyên mẫu thử nghiệm (`프로토타이핑`), Ca sử dụng (`유스케이스`).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Ngôn ngữ Z và VDM thuộc kỹ thuật đặc tả nào?"* -> **정형 명세 기법 (Đặc tả hình thức - Toán học)**.
  - **Bẫy 2:** *"Đặc tả phi hình thức (비정형) có ưu điểm là hoàn toàn không bị mơ hồ?"* -> **Sai**. Ngôn ngữ tự nhiên rất dễ bị hiểu lầm và mơ hồ (모호성 발생 가능).
  - **Bẫy 3:** *"Công cụ CASE nào chuyên dùng để mô tả yêu cầu hệ thống thời gian thực (실시간 처리)?"* -> **SREM (RSL/REVS)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Chính thức (정형) dùng toán (Z, VDM), Phi chính thức (비정형) dùng lời (tự nhiên); SREM thời gian thực, SADT cấu trúc".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ứng dụng thực tế của đặc tả hình thức (Z-Schema):**
  - Trong kỹ nghệ an toàn cao (ví dụ: hệ thống điều khiển tàu cao tốc KTX hoặc chip vi xử lý), một lỗi ngữ nghĩa trong tài liệu yêu cầu có thể gây tử vong hoặc thiệt hại hàng tỷ USD. Khi đó, các điều kiện tiền đề (Pre-condition) và hậu đề (Post-condition) được viết bằng ký hiệu tập hợp và toán logic (Z notation) để máy tính có thể tự động chạy bộ giải (Theorem Prover) chứng minh không bao giờ xảy ra lỗi deadlock hay tràn số.
- **Vai trò của công cụ CASE trong quản lý yêu cầu:**
  - CASE không chỉ đơn thuần là phần mềm vẽ biểu đồ mà còn giúp duy trì ma trận truy vết (Traceability Matrix), kiểm tra xem một thực thể dữ liệu có bị mồ côi (không ai đọc/ghi) hay một luồng dữ liệu vào mà không có đầu ra (Black Hole / Miracle trong DFD) hay không.

### 복습 체크리스트
- [ ] Phân biệt rõ 정형 명세 (Toán học, VDM, Z, Petri-net) và 비정형 명세 (Ngôn ngữ tự nhiên, FSM).
- [ ] Kể tên 4 công cụ CASE phân tích yêu cầu: SADT, SREM, PSL/PSA, TAGS.
- [ ] Nhớ SREM gắn liền với hệ thống thời gian thực (실시간 처리) của hãng TRW.
- [ ] Nắm được ưu điểm của 정형 명세 là chính xác, không mơ hồ nhưng khó hiểu với người dùng.
