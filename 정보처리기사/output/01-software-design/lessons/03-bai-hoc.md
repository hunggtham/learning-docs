# 1. 소프트웨어 공학 및 개발 방법론 (Kỹ nghệ phần mềm và Phương pháp luận phát triển)

## 학습 목표 (Mục tiêu)
- Nắm vững 3 nguyên tắc cơ bản của kỹ nghệ phần mềm (`소프트웨어 공학의 기본 원칙`) nhằm duy trì chất lượng và hồ sơ dự án.
- Thuộc nằm lòng 4 giá trị cốt lõi của Tuyên ngôn Agile (`애자일 선언 4대 핵심 가치`) và phân biệt rõ triết lý Agile với mô hình Thác nước truyền thống.
- Ghi nhớ 5 giá trị cốt lõi của phương pháp XP (`eXtreme Programming 5대 가치`): Giao tiếp, Đơn giản, Dũng cảm, Tôn trọng, Phản hồi.

## 핵심 키워드 (Từ khóa)
- 소프트웨어 공학 (Kỹ nghệ phần mềm / Software Engineering)
- 애자일 방법론 (Phương pháp luận Agile / Agile Methodology)
- 4대 핵심 가치 (4 giá trị cốt lõi Agile / Four Core Agile Values)
- XP (eXtreme Programming)
- 5대 가치 (5 giá trị XP: 의사소통, 단순성, 용기, 존중, 피드백)
- 스크럼 (Scrum)
- 칸반 / 린 (Kanban / Lean)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([1. 소프트웨어 생명 주기](02-bai-hoc.md)):** Sau khi xem xét các mô hình nặng về quy trình và kế hoạch dài hạn (Waterfall, Spiral), bài này chuyển sang cách tiếp cận linh hoạt, thích ứng với thay đổi trong môi trường kinh doanh hiện đại.
- **Tiếp nối sang bài sau ([2. 요구사항 개발](04-bai-hoc.md)):** Dù phát triển theo Waterfall hay Agile, bước thực chất đầu tiên của việc xây dựng hệ thống là thu thập, phân tích và đặc tả các yêu cầu (Requirements) của người dùng.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc 4 mệnh đề so sánh cốt lõi của Agile (A hơn B) và 5 từ khóa giá trị của XP - đây là dạng câu hỏi xuất hiện liên tục trong đề thi 정보처리기사.
- Đọc TẦNG B để hiểu tại sao Agile không phủ nhận tài liệu hay quy trình mà chỉ ưu tiên giá trị tương tác và phần mềm thực tế chạy được.

---

## 1. 소프트웨어 공학 및 개발 방법론 (Kỹ nghệ phần mềm và Phương pháp luận phát triển)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **소프트웨어 공학의 기본 원칙 (3 nguyên tắc cơ bản của SE):**
  1. Liên tục áp dụng kỹ thuật lập trình hiện đại (`현대적인 프로그래밍 기술을 계속적으로 적용`).
  2. Xác minh liên tục để duy trì chất lượng phần mềm (`품질이 유지되도록 지속적으로 검증`).
  3. Duy trì hồ sơ ghi chép rõ ràng về quy trình và kết quả phát triển (`명확한 기록을 유지`).
- **애자일 (Agile) 4대 핵심 가치 (4 giá trị cốt lõi tuyên ngôn Agile):**
  1. **개인과 상호작용** > 프로세스와 도구 (Coi trọng cá nhân và sự tương tác hơn quy trình và công cụ).
  2. **실행되는 SW (작동하는 소프트웨어)** > 방대한 문서 (Coi trọng phần mềm chạy được hơn tài liệu đồ sộ).
  3. **고객과의 협업** > 계약 협상 (Coi trọng cộng tác với khách hàng hơn đàm phán hợp đồng).
  4. **변화에 대응 (반응)** > 계획을 따르는 것 (Coi trọng thích ứng với thay đổi hơn bám sát kế hoạch).
- **Các phương pháp luận thuộc dòng họ Agile:**
  - `스크럼 (Scrum)`: Phát triển theo chu kỳ ngắn Sprint (2-4 tuần), họp đứng hàng ngày.
  - `XP (eXtreme Programming)`: Tập trung vào chất lượng code và kỹ thuật lập trình của developer.
  - `칸반 (Kanban)`: Quản lý luồng công việc trực quan bằng bảng thẻ.
  - `린 (Lean)`: Loại bỏ lãng phí (Muda), tối ưu hóa luồng giá trị.
  - `FDD (Feature-Driven Development)`: Phát triển định hướng tính năng.
- **XP 5대 핵심 가치 (5 giá trị cốt lõi của XP):**
  1. `의사소통 (Communication)`: Giao tiếp cởi mở giữa các thành viên và khách hàng.
  2. `단순성 (Simplicity)`: Thiết kế và viết mã đơn giản nhất vừa đủ cho yêu cầu hiện tại, tránh over-engineering.
  3. `용기 (Courage)`: Dũng cảm refactor mã nguồn cũ, dũng cảm đón nhận thay đổi.
  4. `존중 (Respect)`: Tôn trọng công sức và đóng góp của đồng đội.
  5. `피드백 (Feedback)`: Nhận phản hồi liên tục từ kiểm thử tự động và người dùng thực tế.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** Đề thi khẳng định *"Agile hoàn toàn không cần tài liệu và không cần kế hoạch"* -> **Sai**. Agile vẫn có tài liệu và kế hoạch, nhưng coi trọng phần mềm hoạt động và sự thích ứng với thay đổi hơn.
  - **Bẫy 2 (XP values):** Đề đưa vào các từ như `정확성 (Chính xác)`, `효율성 (Hiệu quả)`, `복잡성 (Phức tạp)` và hỏi có phải giá trị của XP không -> **Không phải**. Bộ 5 giá trị chuẩn chỉ gồm: **의사소통, 단순성, 용기, 존중, 피드백**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Agile tương tác - phần mềm - hợp tác - thích nghi; XP gói gọn trong Giao tiếp - Đơn giản - Dũng cảm - Tôn trọng - Phản hồi".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh đối chiếu Waterfall vs Agile:**
  - **Waterfall (폭포수):** Trọng tâm là Kế hoạch (`계획 중심`), tài liệu đặc tả chặt chẽ từ đầu, kiểm thử ở cuối chu trình, thay đổi là ngoại lệ cần thủ tục xét duyệt nghiêm ngặt. Phù hợp cho các dự án cố định yêu cầu (quốc phòng, lõi ngân hàng).
  - **Agile (애자일):** Trọng tâm là Khách hàng và Giá trị sản phẩm (`고객/가치 중심`), chia nhỏ thành các vòng lặp lặp đi lặp lại (`반복/점증`), liên tục nhận phản hồi và chuyển giao phần mềm dùng được sau mỗi chu kỳ ngắn. Phù hợp sản phẩm thương mại điện tử, ứng dụng di động thay đổi thị hiếu liên tục.
- **Ví dụ thực tế dễ hiểu:**
  - Trong một nhóm XP, lập trình viên không ngần ngại xóa 500 dòng code spaghetti cũ để viết lại thành 50 dòng sạch hơn vì họ có "Dũng cảm (용기)", họ viết code dễ đọc để đạt "Đơn giản (단순성)", và họ có bộ test tự động báo xanh đỏ liên tục để nhận "Phản hồi (피드백)".

### 복습 체크리스트
- [ ] Nhớ 3 nguyên tắc cơ bản của kỹ nghệ phần mềm (kỹ thuật hiện đại, kiểm chứng liên tục, lưu giữ hồ sơ).
- [ ] Đọc vanh vách 4 giá trị cốt lõi của Agile (Cá nhân > Quy trình, SW chạy được > Tài liệu, Hợp tác > Đàm phán, Thích nghi > Kế hoạch).
- [ ] Thuộc lòng 5 giá trị của XP: 의사소통, 단순성, 용기, 존중, 피드백.
- [ ] Kể tên ít nhất 4 phương pháp luận thuộc nhóm Agile (Scrum, XP, Kanban, Lean).
