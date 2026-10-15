# 2. 스크럼 및 XP 추가 개념 (Advanced Scrum & XP)

## 학습 목표 (Mục tiêu)
- Nắm vững cấu trúc viết Câu chuyện người dùng (`사용자 스토리 - User Story`) và bộ tiêu chuẩn đánh giá chất lượng `INVEST`.
- Hiểu phương pháp ước lượng độ phức tạp tương đối bằng `Story Point` và kỹ thuật chơi bài `Planning Poker`.
- Nắm vững khái niệm Vận tốc hoàn thành (`Velocity`), Nhiệm vụ thử nghiệm kỹ thuật (`Spike`), và Định nghĩa hoàn thành (`DoD - Definition of Done`).

## 핵심 키워드 (Từ khóa)
- 사용자 스토리 (User Story / As a... I want... So that...)
- INVEST 원칙 (Independent, Negotiable, Valuable, Estimable, Small, Testable)
- 스토리 포인트 (Story Point / 피보나치 수열)
- 플래닝 포커 (Planning Poker / 상대적 규모 추정)
- 속도 / 개발 속도 (Velocity / Sprint 처리량)
- 스파이크 (Spike / 기술 탐색용 태스크)
- 완료의 정의 (DoD - Definition of Done / Acceptance Criteria)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([7. 스크럼(Scrum) 및 XP(eXtreme Programming)](59-bai-hoc.md)):** Sau khi nắm vững cấu trúc cơ bản của Scrum và XP, bài này bổ sung các công cụ đo lường và kỹ thuật ước lượng nâng cao được áp dụng trong thực tế dự án.
- **Tiếp nối sang bài sau ([4. 운영 환경 구축 고려사항](61-bai-hoc.md)):** Chuyển từ quy trình phát triển sang các cân nhắc kỹ thuật khi xây dựng môi trường vận hành hạ tầng máy chủ và lưu trữ.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc 6 chữ cái tiêu chuẩn INVEST và cách tính Velocity (tổng điểm Story Point hoàn thành trong 1 Sprint).
- Đọc TẦNG B để hiểu tại sao Planning Poker lại dùng dãy số Fibonacci (1, 2, 3, 5, 8...) để phản ánh độ bất định tăng dần theo quy mô.

---

## 2. 스크럼 및 XP 추가 개념 (Advanced Scrum & XP)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. 사용자 스토리 (User Story - Câu chuyện người dùng):**
  - **Khái niệm:** Là phương thức mô tả yêu cầu tính năng ngắn gọn, tự nhiên từ góc độ của người dùng cuối.
  - **Cú pháp chuẩn:**
    $$\text{“Là [Ai - Vai trò người dùng], tôi muốn [Làm gì - Tính năng], để [Đạt được lợi ích gì - Giá trị nghiệp vụ]”}$$
  - **Bộ tiêu chuẩn chất lượng INVEST (Bắt buộc phải thuộc):**
    - `I - Independent (독립적)`: Các story không nên phụ thuộc chặt chẽ vào nhau để dễ dàng sắp xếp thứ tự ưu tiên.
    - `N - Negotiable (협상 가능)`: Nội dung story không phải hợp đồng cứng nhắc mà có thể trao đổi, điều chỉnh chi tiết giữa PO và Dev Team.
    - `V - Valuable (가치 있는)`: Story phải mang lại giá trị thực tế rõ ràng cho khách hàng hoặc người dùng cuối.
    - `E - Estimable (추정 가능)`: Độ lớn và độ phức tạp của story có thể ước lượng được.
    - `S - Small (작은 단위)`: Kích thước story vừa phải, có thể hoàn thành trọn vẹn trong vòng 1 Sprint.
    - `T - Testable (테스트 가능)`: Phải có tiêu chí nghiệm thu rõ ràng để kiểm thử viên có thể viết test case xác nhận.
- **2. Kỹ thuật ước lượng: Story Point & Planning Poker:**
  - `스토리 포인트 (Story Point)`: Đơn vị đo lường tương đối về **quy mô, độ phức tạp và rủi ro** của một User Story (không đồng nhất với số giờ làm việc thực tế). Thường sử dụng các số trong dãy **Fibonacci (1, 2, 3, 5, 8, 13, 21)**.
  - `플래닝 포커 (Planning Poker)`: Kỹ thuật ước lượng tập thể bằng các lá bài in số Fibonacci; tất cả các thành viên trong nhóm cùng lật bài đồng thời để thảo luận và đưa ra con số thống nhất, tránh hiện tượng bị thiên lệch bởi ý kiến của người có uy tín nhất.
- **3. Các khái niệm bổ trợ then chốt:**
  - `개발 속도 / 속도 (Velocity)`: **Tổng số Story Point mà nhóm hoàn thành trọn vẹn trong một Sprint**. Chỉ số này được dùng làm căn cứ thực tế để dự báo số lượng công việc mà nhóm có thể cam kết thực hiện trong các Sprint tiếp theo.
  - `스파이크 (Spike)`: Một nhiệm vụ nghiên cứu, khảo sát hoặc viết mã thử nghiệm ngắn (thường kéo dài 1-2 ngày) nhằm tìm hiểu một công nghệ mới hoặc làm sáng tỏ các rủi ro kiến trúc trước khi bắt tay làm story thật.
  - `완료의 정의 (DoD - Definition of Done)`: Bản danh sách các tiêu chuẩn chất lượng chung được toàn đội thống nhất (ví dụ: Code đã review, Unit test pass 100%, Tài liệu đã cập nhật, Đã deploy lên môi trường Staging). Chỉ khi thỏa mãn toàn bộ DoD, User Story mới được xem là hoàn thành.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Bộ tiêu chuẩn đánh giá User Story viết tắt là gì?"* -> **INVEST**.
  - **Bẫy 2:** *"Story Point có tương đương trực tiếp với số giờ (Hours) làm việc của lập trình viên không?"* -> **Không tương đương**. Story Point đo lường độ phức tạp và nỗ lực tương đối, không phải thời gian tuyệt đối.
  - **Bẫy 3:** *"Nhiệm vụ nghiên cứu kỹ thuật ngắn để giảm rủi ro công nghệ trong Agile gọi là gì?"* -> **스파이크 (Spike)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "User Story chuẩn INVEST; Ước lượng Story Point bằng Planning Poker Fibonacci; Velocity đo năng suất Sprint, Spike giải quyết bài toán kỹ thuật mới".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ví dụ tính toán lập kế hoạch dựa trên Velocity:**
  - Trong 3 Sprint gần nhất, nhóm đạt Velocity lần lượt là 20, 22, 24 Story Points $\rightarrow$ Vận tốc trung bình của nhóm là $\frac{20 + 22 + 24}{3} = 22$ điểm / Sprint.
  - Khi lập kế hoạch cho Sprint 4, nhóm chỉ nên bốc các User Story từ Product Backlog có tổng Story Point xấp xỉ 22 điểm, tránh việc nhận quá nhiều việc dẫn đến trễ hạn cam kết.

### 복습 체크리스트
- [ ] Nêu cú pháp chuẩn của một User Story (Là ai, Muốn gì, Để làm gì).
- [ ] Giải thích ý nghĩa của 6 chữ cái trong tiêu chuẩn INVEST.
- [ ] Định nghĩa Story Point và cách áp dụng Planning Poker.
- [ ] Phân biệt được Velocity (tốc độ hoàn thành) và Spike (nhiệm vụ nghiên cứu kỹ thuật).
