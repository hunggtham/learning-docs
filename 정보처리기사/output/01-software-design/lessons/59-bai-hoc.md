# 7. 스크럼(Scrum) 및 XP(eXtreme Programming)

## 학습 목표 (Mục tiêu)
- Nắm vững cơ cấu tổ chức và quy trình vận hành hoàn chỉnh của Khung phát triển `Scrum`: 3 vai trò (PO, SM, Dev Team), 4 sự kiện, 3 tạo phẩm, và Biểu đồ Burn-down.
- Thuộc nằm lòng 5 giá trị cốt lõi và 12 kỹ thuật thực hành kinh điển của phương pháp `XP (eXtreme Programming)`.
- Phân biệt rõ sự khác nhau giữa cuộc họp Duyệt sản phẩm (`Sprint Review` - demo tính năng) và cuộc họp Rút kinh nghiệm (`Sprint Retrospective` - cải tiến quy trình).

## 핵심 키워드 (Từ khóa)
- 스크럼 (Scrum: PO, SM, 개발팀 / 스프린트 / 소멸 차트 - Burn-down Chart)
- 제품 백로그 vs 스프린트 백로그 (Product Backlog vs Sprint Backlog)
- 스프린트 검토 vs 회고 (Sprint Review vs Retrospective)
- XP 5대 가치 (의사소통, 단순성, 용기, 존중, 피드백)
- XP 12대 실천 항목 (짝 프로그래밍, TDD, 리팩토링, 계속적 통합, 공동 코드 소유)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([6. 애자일 방법론](58-bai-hoc.md)):** Sau khi hiểu triết lý tổng quát của Agile, bài này đi sâu vào chi tiết kỹ thuật của hai phương pháp luận thực tế được áp dụng rộng rãi nhất: Scrum và XP.
- **Tiếp nối sang bài sau ([2. 스크럼 및 XP 추가 개념](60-bai-hoc.md)):** Khảo sát các kỹ thuật nâng cao như User Story (INVEST), Story Point và Planning Poker.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nhớ 3 vai trò Scrum (PO quản lý Backlog, SM giải quyết khó khăn; SM không phải là Project Manager hay sếp chỉ đạo) và 5 giá trị XP.
- Đọc TẦNG B để phân biệt hai buổi họp cuối Sprint: Review mời khách hàng đến xem demo sản phẩm; Retrospective chỉ nội bộ team họp bàn cải tiến cách làm việc.

---

## 7. 스크럼(Scrum) 및 XP(eXtreme Programming)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Chi tiết Khung làm việc Scrum (Scrum Framework):**
  - **3 vai trò cốt lõi (Scrum 3 Roles):**
    - `PO (Product Owner - Chủ sản phẩm)`: Đại diện cho tiếng nói khách hàng; chịu trách nhiệm tạo lập, quản lý và **quyết định thứ tự ưu tiên của các yêu cầu trong Product Backlog**.
    - `SM (Scrum Master)`: Người hướng dẫn, bảo vệ đội ngũ, **loại bỏ các trở ngại cản trở tiến độ của nhóm** và đảm bảo các nguyên tắc Scrum được tuân thủ; **không phải là sếp quản lý hay người phân công công việc**.
    - `개발팀 (Development Team - Nhóm phát triển)`: Nhóm tự quản (Self-organizing) và đa chức năng (Cross-functional), thường từ 5 đến 9 thành viên, cùng nhau làm ra sản phẩm có thể chuyển giao.
  - **4 sự kiện chính (Scrum 4 Events):**
    1. `스프린트 계획 회의 (Sprint Planning)`: Lập kế hoạch cho Sprint (vòng lặp phát triển kéo dài 1-4 tuần).
    2. `일일 스크럼 회의 (Daily Scrum)`: **Họp đứng mỗi sáng 15 phút**, mỗi thành viên trả lời 3 câu hỏi (Hôm qua làm gì, Hôm nay làm gì, Có gặp khó khăn gì không); theo dõi tiến độ công việc còn lại bằng **소멸 차트 (Burn-down Chart)**.
    3. `스프린트 검토 (Sprint Review)`: Diễn ra cuối Sprint, nhóm **trình diễn trực tiếp sản phẩm (Demo)** cho khách hàng và các bên liên quan xem để nhận phản hồi.
    4. `스프린트 회고 (Sprint Retrospective)`: Diễn ra sau Sprint Review, chỉ nội bộ nhóm họp để **đánh giá và cải tiến quy trình làm việc, văn hóa phối hợp cho các Sprint sau**.
  - **3 tạo phẩm (Scrum 3 Artifacts):**
    - `제품 백로그 (Product Backlog)`: Danh sách tổng thể toàn bộ các tính năng mong muốn của sản phẩm do PO quản lý.
    - `스프린트 백로그 (Sprint Backlog)`: Danh sách các task được chọn từ Product Backlog để làm trong Sprint hiện tại.
    - `완료 증분 (Increment)`: Phần mềm chạy được đã hoàn thành và đạt chuẩn định nghĩa hoàn thành (DoD).
- **2. Chi tiết Phương pháp eXtreme Programming (XP):**
  - **5 giá trị cốt lõi (XP 5 Core Values):**
    - `의사소통 (Communication - Giao tiếp)`, `단순성 (Simplicity - Đơn giản)`, `용기 (Courage - Dũng cảm)`, `존중 (Respect - Tôn trọng)`, `피드백 (Feedback - Phản hồi)`.
  - **Các kỹ thuật thực hành quan trọng (XP Practices):**
    - `짝 프로그래밍 (Pair Programming)`: 2 lập trình viên cùng ngồi làm việc trên 1 máy tính (1 Driver gõ code, 1 Navigator rà soát logic).
    - `테스트 주도 개발 (TDD)`: Viết kiểm thử tự động trước, viết mã nguồn hiện thực sau.
    - `리팩토링 (Refactoring)`: Cải tiến cấu trúc mã nguồn bên trong mà không làm thay đổi hành vi bên ngoài.
    - `계속적인 통합 (CI - Continuous Integration)`: Tích hợp mã nguồn của tất cả thành viên liên tục hàng ngày qua bộ kiểm thử tự động.
    - `공동 코드 소유 (Collective Ownership)`: Mã nguồn là tài sản chung của toàn đội, bất kỳ ai cũng có quyền sửa đổi bất kỳ đoạn code nào khi cần.
    - `소규모 릴리즈 (Small Releases)`: Phát hành các bản cập nhật nhỏ thường xuyên.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Ai là người quyết định thứ tự ưu tiên của Product Backlog?"* -> **PO (Product Owner - Chủ sản phẩm)**.
  - **Bẫy 2:** *"Cuộc họp cuối Sprint để đánh giá quy trình làm việc và rút kinh nghiệm nội bộ gọi là gì?"* -> **스프린트 회고 (Sprint Retrospective)**, không phải Sprint Review (trình diễn sản phẩm).
  - **Bẫy 3:** *"Scrum Master là người trực tiếp phân công công việc cụ thể cho từng lập trình viên?"* -> **Sai**. Nhóm Scrum là nhóm tự tổ chức (Self-organizing), các thành viên tự nhận việc từ Sprint Backlog.
- **한 문장 설명 (Câu chốt ghi nhớ):** "PO ưu tiên Backlog, SM diệt trở ngại, Daily Scrum 15 phút Burn-down, Review xem demo, Retrospective cải tiến quy trình; XP gồm 5 giá trị và các kỹ thuật Pair, TDD, CI, Refactor".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế Burn-down Chart trong Daily Scrum:**
  - Trục hoành là ngày làm việc trong Sprint, trục tung là số giờ công việc còn lại (Remaining Hours). Đường chéo từ đỉnh xuống đáy góc phải là đường tiến độ lý tưởng. Nếu đường thực tế nằm phía trên đường lý tưởng, cả nhóm biết ngay dự án đang bị chậm tiến độ và cần sự can thiệp của Scrum Master để gỡ bỏ nút thắt.

### 복습 체크리스트
- [ ] Phân biệt rõ vai trò của PO (Product Owner) và SM (Scrum Master).
- [ ] Nhớ đặc trưng của Daily Scrum (15 phút, đứng họp, Burn-down chart).
- [ ] Phân biệt được mục đích của Sprint Review (demo sản phẩm) và Sprint Retrospective (cải tiến quy trình).
- [ ] Đọc thuộc 5 giá trị của XP: 의사소통, 단순성, 용기, 존중, 피드백.
- [ ] Kể tên ít nhất 5 kỹ thuật thực hành của XP (Pair Programming, TDD, Refactoring, CI, Collective Ownership).
