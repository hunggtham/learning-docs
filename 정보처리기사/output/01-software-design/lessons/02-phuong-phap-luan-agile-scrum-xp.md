# 애자일 방법론, 스크럼 및 XP (Phương pháp luận Agile, Khung Scrum và Kỹ thuật XP)

## 학습 목표 (Mục tiêu)
- Nắm vững triết lý, bối cảnh ra đời và 4 giá trị cốt lõi cùng 12 nguyên tắc chỉ đạo của Tuyên ngôn Agile (`애자일 선언 4대 핵심 가치 및 12대 원칙`).
- Phân tích sâu sắc cơ cấu tổ chức và quy trình vận hành hoàn chỉnh của Khung phát triển `Scrum`: 3 vai trò (PO, SM, Dev Team), 4 sự kiện, 3 tạo phẩm, và cơ chế theo dõi tiến độ bằng Biểu đồ tiêu hao (`소멸 차트 - Burn-down Chart`).
- Thuộc nằm lòng 5 giá trị cốt lõi và 12 kỹ thuật thực hành kinh điển của phương pháp `XP (eXtreme Programming)`: Lập trình cặp (`짝 프로그래밍`), Phát triển hướng kiểm thử (`TDD`), Tái cấu trúc mã nguồn (`리팩토링`), Tích hợp liên tục (`CI`), và Quyền sở hữu mã nguồn chung (`공동 코드 소유`).
- Làm chủ các kỹ thuật ước lượng và quản trị yêu cầu Agile: Đặc tả User Story theo nguyên tắc `INVEST`, tính điểm độ phức tạp `Story Point` theo dãy số Fibonacci, và kỹ thuật ước lượng đồng thuận `Planning Poker`.

## 핵심 키워드 (Từ khóa)
- 애자일 방법론 (Phương pháp luận Agile / Agile Methodology / 민첩함·반복·점증)
- 애자일 선언 4대 가치 (4 giá trị cốt lõi Tuyên ngôn Agile / Four Core Agile Values)
- 스크럼 (Scrum: PO - 제품 책임자, SM - 스크럼 마스터, 개발팀 - Development Team)
- 스프린트 (Sprint / 1~4주 반복 주기 / Sprint Planning, Daily Scrum, Review, Retrospective)
- 소멸 차트 (Biểu đồ tiêu hao / Burn-down Chart / 이상선 vs 실제선)
- XP 5대 핵심 가치 (5 giá trị XP: 의사소통, 단순성, 용기, 존중, 피드백)
- XP 12대 실천 항목 (12 thực hành XP: 짝 프로그래밍, TDD, 리팩토링, 계속적 통합, 공동 소유)
- INVEST 원칙 (Nguyên tắc viết User Story: Independent, Negotiable, Valuable, Estimable, Small, Testable)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Tiếp nối từ [01-sdlc-va-cac-mo-hinh-vong-doi.md](01-sdlc-va-cac-mo-hinh-vong-doi.md), các mô hình truyền thống (Thác nước, V-Model) đặt trọng tâm vào tài liệu đặc tả đồ sộ và đóng băng kế hoạch dài hạn. Khi áp dụng vào các sản phẩm dịch vụ số (Web, App di động, E-commerce), việc hạn chế thay đổi khiến sản phẩm bàn giao ra thị trường thường bị lỗi thời so với thị hiếu người dùng.
- **Đang giải quyết gì (Current Problem):** Bài học này giải quyết triệt để bài toán làm sao để thích ứng nhanh và đón nhận thay đổi: chuyển từ "quản lý theo tài liệu và hợp đồng cứng" sang "hợp tác trực tiếp và chuyển giao phần mềm chạy được định kỳ", đồng thời cụ thể hóa triết lý này bằng hai khung hành động thực tế là Scrum (quản lý tiến độ nhóm) và XP (kỹ thuật lập trình chất lượng cao).
- **Dùng đi đâu (Forward Handoff):** Dù dự án vận hành theo chu kỳ nước rút của Scrum hay theo các pha lớn của Waterfall, bước triển khai thực chất đầu tiên luôn là làm rõ các bên liên quan cần gì ở hệ thống. Kiến thức bài này bàn giao sang [03-ky-nghe-va-dac-ta-yeu-cau.md](03-ky-nghe-va-dac-ta-yeu-cau.md) để học sâu về quy trình Kỹ nghệ yêu cầu, phân loại chức năng/phi chức năng và kỹ thuật phân tích có cấu trúc.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc 4 mệnh đề đối chiếu "A hơn B" của Tuyên ngôn Agile, 3 vai trò Scrum (PO quyết định thứ tự Backlog; SM loại bỏ trở ngại, không phải sếp chỉ đạo), và 5 từ khóa giá trị của XP.
- Đọc TẦNG B để phân biệt rạch ròi hai buổi họp cuối Sprint (Sprint Review trình diễn sản phẩm cho khách hàng vs Sprint Retrospective rút kinh nghiệm nội bộ quy trình), cơ chế đọc đồ thị Burn-down, và thuật toán ước lượng Planning Poker.

---

## 애자일 방법론, 스크럼 및 XP

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Triết lý Agile và 4 Giá trị cốt lõi của Tuyên ngôn Agile
- **Bản chất của Agile:** Không phải là một phương pháp luận cụ thể duy nhất, mà là một **triết lý / chiếc ô bao trùm** các phương pháp luận phát triển mang tính linh hoạt (`민첩함`), lặp đi lặp lại (`반복적 - Iterative`) và tăng trưởng dần (`점증적 - Incremental`).
- **핵심 원리 (Nguyên tắc cốt lõi — 4대 핵심 가치):**
  1. **개인과 상호작용 > 프로세스와 도구**
     - [Hàn/Anh]: `공정과 도구보다 개인과 상호작용을 가치 있게 여긴다.`
     - [Tiếng Việt]: Coi trọng con người và sự tương tác giữa các thành viên hơn là quy trình máy móc và công cụ hỗ trợ.
  2. **작동하는 소프트웨어 > 포괄적인 문서**
     - [Hàn/Anh]: `포괄적인 문서보다 작동하는 소프트웨어를 가치 있게 여긴다.`
     - [Tiếng Việt]: Coi trọng phần mềm thực tế chạy được và tạo ra giá trị hơn là các bộ tài liệu đặc tả đồ sộ, cồng kềnh.
  3. **고객과의 협업 > 계약 협상**
     - [Hàn/Anh]: `계약 협상보다 고객과의 협업을 가치 있게 여긴다.`
     - [Tiếng Việt]: Coi trọng việc liên tục lắng nghe và hợp tác chặt chẽ với khách hàng hơn là các điều khoản đàm phán hợp đồng cứng nhắc.
  4. **변화에 대응하기 > 계획을 따르기**
     - [Hàn/Anh]: `계획을 따르기보다 변화에 대응하는 것을 가치 있게 여긴다.`
     - [Tiếng Việt]: Coi trọng việc linh hoạt thích ứng và phản hồi nhanh trước sự thay đổi yêu cầu hơn là bám chặt lấy một kế hoạch đã lập từ trước.

- **Bảng đối chiếu toàn diện Waterfall vs Agile:**

| Tiêu chí so sánh | 폭포수 모형 (Waterfall) | 애자일 방법론 (Agile) |
|:---|:---|:---|
| **Trọng tâm quản lý** | Kế hoạch và tài liệu (`계획 및 문서 중심`) | Con người và sản phẩm chạy được (`사람과 소프트웨어 중심`) |
| **Quy trình triển khai** | Tuyến tính tuần tự dứt điểm (`선형 순차적`) | Lặp lại chu kỳ ngắn và tăng trưởng (`반복·점증적`) |
| **Thái độ với thay đổi** | Hạn chế thay đổi, chi phí sửa rất đắt | Đón nhận và thích ứng linh hoạt với thay đổi |
| **Sự tham gia của khách hàng** | Chủ yếu ở đầu (yêu cầu) và cuối (nghiệm thu) | Tham gia liên tục, làm việc cùng nhau mỗi ngày |
| **Thước đo tiến độ** | Số lượng tài liệu sản phẩm bàn giao (`산출물`) | Phần mềm thực tế chạy được (`작동하는 소프트웨어`) |

#### 2. Khung làm việc Scrum (Scrum Framework)
Scrum là khung quản lý dự án theo chu kỳ lặp lại ngắn gọi là **스프린트 (Sprint)**, thường kéo dài từ 1 đến 4 tuần.

##### A. 3 Vai trò cốt lõi trong Scrum (Scrum 3 Roles)
- **제품 책임자 (Product Owner - PO):**
  - Đại diện cho tiếng nói và lợi ích của khách hàng cùng các bên liên quan.
  - Chịu trách nhiệm tạo lập, quản lý và **quyết định thứ tự ưu tiên của các hạng mục trong Product Backlog**.
  - Là người duy nhất có quyền nghiệm thu phần mềm hoàn thành sau mỗi Sprint.
- **스크럼 마스터 (Scrum Master - SM):**
  - Đóng vai trò là người điều phối, người thầy hướng dẫn (Facilitator / Servant Leader).
  - Đảm bảo các nguyên tắc và sự kiện của Scrum được tuân thủ nghiêm túc.
  - Chịu trách nhiệm **loại bỏ các trở ngại và vướng mắc kỹ thuật cản trở tiến độ của nhóm phát triển**.
  - **Bẫy đề thi:** SM **không phải là Project Manager hay cấp trên chỉ đạo**, không có quyền phân công công việc hay ép buộc nhóm.
- **개발팀 (Development Team - Nhóm phát triển):**
  - Nhóm tự tổ chức (Self-organizing) và đa chức năng (Cross-functional), quy mô tối ưu từ 5 đến 9 thành viên.
  - Tự chủ phân chia và chịu trách nhiệm tập thể về việc biến các yêu cầu trong Sprint Backlog thành sản phẩm chạy được.

##### B. 4 Sự kiện chính trong Scrum (Scrum 4 Events)
1. `스프린트 계획 회의 (Sprint Planning Meeting)`: Diễn ra đầu Sprint để xác định mục tiêu và chọn các mục từ Product Backlog đưa vào Sprint Backlog.
2. `일일 스크럼 회의 (Daily Scrum Meeting)`: **Họp đứng mỗi sáng tối đa 15 phút**, mỗi thành viên trả lời ngắn gọn 3 câu:
   - Hôm qua tôi đã làm gì để giúp nhóm đạt mục tiêu?
   - Hôm nay tôi sẽ làm gì?
   - Tôi đang gặp trở ngại hay khó khăn gì không?
3. `스프린트 검토 (Sprint Review)`: Diễn ra cuối Sprint, nhóm **trình diễn trực tiếp sản phẩm (Live Demo)** cho khách hàng và các bên liên quan xem để thu nhận phản hồi.
4. `스프린트 회고 (Sprint Retrospective)`: Diễn ra sau Sprint Review, **chỉ nội bộ nhóm Scrum họp kín** để đánh giá quy trình làm việc, văn hóa phối hợp và tìm ra các điểm cải tiến cho Sprint kế tiếp.

##### C. 3 Tạo phẩm trong Scrum (Scrum 3 Artifacts)
- `제품 백로그 (Product Backlog)`: Danh sách tổng thể toàn bộ tính năng mong muốn của sản phẩm, do PO quản lý và liên tục cập nhật.
- `스프린트 백로그 (Sprint Backlog)`: Tập hợp các công việc cụ thể được nhóm phát triển cam kết hoàn thành trong Sprint hiện tại.
- `완료 증분 (Increment)`: Phần mềm chạy được đã hoàn thành trong Sprint, phải đáp ứng chuẩn Định nghĩa hoàn thành (`DoD - Definition of Done`).

#### 3. Phương pháp lập trình eXtreme Programming (XP)
XP là phương pháp phát triển linh hoạt tập trung sâu vào **kỹ thuật lập trình và năng suất của lập trình viên**.

##### A. 5 Giá trị cốt lõi của XP (XP 5 Core Values)
- [Hàn/Anh]: `XP의 5대 핵심 가치는 의사소통(Communication), 단순성(Simplicity), 용기(Courage), 존중(Respect), 피드백(Feedback)이다.`
- **Ý nghĩa kỹ thuật:**
  1. `의사소통 (Communication)`: Thảo luận cởi mở, trực tiếp mặt đối mặt giữa các lập trình viên và với khách hàng.
  2. `단순성 (Simplicity)`: Thiết kế và viết mã nguồn vừa đủ đơn giản để giải quyết yêu cầu hiện tại, kiên quyết chống over-engineering.
  3. `용기 (Courage)`: Dũng cảm tái cấu trúc mã nguồn cũ (Refactoring) và đón nhận các yêu cầu thay đổi khó khăn.
  4. `존중 (Respect)`: Tôn trọng công sức, quyền tự chủ và đóng góp kỹ thuật của đồng đội.
  5. `피드백 (Feedback)`: Liên tục nhận phản hồi tức thì thông qua bộ kiểm thử tự động, tích hợp liên tục và ý kiến người dùng.

##### B. 12 Kỹ thuật thực hành kinh điển của XP (XP 12 Practices)
1. **짝 프로그래밍 (Pair Programming):** Hai lập trình viên cùng làm việc trên 1 máy tính (1 Driver gõ code, 1 Navigator rà soát logic và kiến trúc).
2. **테스트 주도 개발 (TDD - Test-Driven Development):** Viết mã kiểm thử tự động (Test Case) trước khi viết mã nguồn thực tế; chu trình Red $\rightarrow$ Green $\rightarrow$ Refactor.
3. **리팩토링 (Refactoring):** Cải tiến cấu trúc mã nguồn bên trong để nâng cao tính dễ đọc và bảo trì mà **không làm thay đổi hành vi bên ngoài của phần mềm**.
4. **계속적인 통합 (CI - Continuous Integration):** Tích hợp mã nguồn của toàn đội vào nhánh chính nhiều lần mỗi ngày và tự động chạy test kiểm thử toàn diện.
5. **공동 코드 소유 (Collective Ownership):** Mọi dòng mã đều là tài sản chung của toàn đội, bất kỳ ai cũng có quyền và trách nhiệm sửa đổi khi thấy cần thiết.
6. **소규모 릴리즈 (Small Releases):** Phát hành các phiên bản cập nhật nhỏ thường xuyên để nhận phản hồi sớm từ người dùng.
7. **계획 게임 (Planning Game):** Khách hàng quyết định phạm vi kinh doanh dựa trên ước tính kỹ thuật của lập trình viên.
8. **간단한 디자인 (Simple Design):** Thiết kế tối giản nhất vừa đủ vượt qua các bài kiểm thử hiện có.
9. **메타포어 (Metaphor):** Sử dụng các phép ẩn dụ đời thường để mọi người cùng chung một cách hiểu về hệ thống.
10. **주 40시간 노동 (40-Hour Work Week):** Duy trì nhịp độ làm việc bền vững, không làm việc kiệt sức quá 40 giờ/tuần để tránh sinh lỗi do mệt mỏi.
11. **고객 상주 (On-site Customer):** Đại diện khách hàng ngồi làm việc trực tiếp tại văn phòng của nhóm phát triển để giải đáp thắc mắc ngay lập tức.
12. **코딩 표준 (Coding Standards):** Tuân thủ quy tắc định dạng và đặt tên code thống nhất trong toàn nhóm.

#### 4. Kỹ thuật quản trị và ước lượng Agile nâng cao

##### A. User Story và Nguyên tắc INVEST
- Cấu trúc chuẩn của một câu chuyện người dùng: *"Là một [vai trò người dùng], tôi muốn [hành động/tính năng], để [đạt được lợi ích gì]."*
- **6 tiêu chí vàng INVEST:**
  - `I - Independent` (Độc lập, không phụ thuộc chặt vào Story khác).
  - `N - Negotiable` (Có thể thương lượng, không phải hợp đồng đóng băng).
  - `V - Valuable` (Mang lại giá trị cụ thể cho người dùng cuối).
  - `E - Estimable` (Có thể ước lượng được độ phức tạp và khối lượng công việc).
  - `S - Small` (Quy mô vừa đủ nhỏ để hoàn thành trong 1 Sprint).
  - `T - Testable` (Có thể kiểm thử được thông qua các tiêu chí nghiệm thu rõ ràng).

##### B. Story Point và Planning Poker
- **스토리 포인트 (Story Point):** Đơn vị đo lường tương đối về độ phức tạp, rủi ro và nỗ lực cần thiết của một User Story; thường sử dụng các con số theo dãy **피보나치 수열 (Fibonacci: 1, 2, 3, 5, 8, 13, 21...)** để phản ánh mức độ bất định tăng dần theo độ lớn của công việc.
- **플래닝 포커 (Planning Poker):** Kỹ thuật ước lượng tập thể bằng các lá bài in số Fibonacci. Mỗi thành viên bí mật chọn lá bài tương ứng với độ khó, cùng lật bài đồng thời. Hai người chọn điểm cao nhất và thấp nhất sẽ trình bày lý do, sau đó cả nhóm thảo luận để thống nhất điểm số chung, triệt tiêu sự áp đặt của người có tiếng nói lớn nhất.

#### 5. Bẫy đề thi trắc nghiệm thường gặp (주의/함정)
- **Bẫy 1 (Hiểu sai về tài liệu trong Agile):** Đề thi khẳng định *"Agile hoàn toàn không cần tài liệu và không cần kế hoạch"* $\rightarrow$ **SAI**. Agile vẫn có tài liệu và kế hoạch, nhưng coi trọng phần mềm hoạt động và sự thích ứng với thay đổi hơn là tài liệu quá chi tiết.
- **Bẫy 2 (Nhầm lẫn vai trò Scrum):** Đề hỏi *"Ai là người phân công công việc cụ thể cho từng thành viên trong nhóm phát triển?"* $\rightarrow$ **Chính các thành viên trong nhóm phát triển tự nhận việc**, Scrum Master và Product Owner tuyệt đối không phân công áp đặt.
- **Bẫy 3 (Phân biệt Review vs Retrospective):**
  - Họp demo tính năng cho khách hàng và các bên liên quan xem $\rightarrow$ **스프린트 검토 (Sprint Review)**.
  - Họp kín nội bộ team để cải tiến quy trình và văn hóa làm việc $\rightarrow$ **스프린트 회고 (Sprint Retrospective)**.
- **Bẫy 4 (Bộ 5 giá trị XP):** Đề hay chèn các từ gây nhiễu như `정확성 (Chính xác)`, `효율성 (Hiệu quả)`, `복잡성 (Phức tạp)` và hỏi có thuộc 5 giá trị của XP không $\rightarrow$ **KHÔNG**. 5 giá trị chuẩn chỉ gồm: **의사소통, 단순성, 용기, 존중, 피드백**.

- **한 문장 설명 (Câu chốt ghi nhớ):** "PO quyết Backlog, SM diệt rào cản, Daily 15 phút, Review xem Demo, Retrospective cải tiến quy trình; XP gồm 5 giá trị và bộ kỹ thuật thực chiến Pair, TDD, CI, Refactor".

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Đồ thị tiêu hao (Burn-down Chart) trong vận hành Scrum
- **Bản chất hình học:** Trục hoành ($X$) biểu thị số ngày làm việc trong Sprint; trục tung ($Y$) biểu thị tổng số giờ công việc còn lại (Remaining Hours) hoặc số Story Points cần hoàn thành.
- **이상선 (Ideal Line - Đường tiến độ lý tưởng):** Đường thẳng chéo nối từ đỉnh góc trên bên trái (tổng công việc ban đầu) xuống điểm 0 ở góc dưới bên phải vào ngày cuối Sprint.
- **실제선 (Actual Line - Đường tiến độ thực tế):**
  - Nếu đường thực tế nằm **phía TRÊN** đường lý tưởng: Dự án đang bị **chậm tiến độ (지연)**. Khối lượng công việc tồn đọng nhiều hơn dự kiến; Scrum Master cần vào cuộc để tháo gỡ khó khăn hoặc PO phải giảm bớt phạm vi của Sprint.
  - Nếu đường thực tế nằm **phía DƯỚI** đường lý tưởng: Dự án đang **vượt tiến độ (조기 완료)**, nhóm giải quyết công việc nhanh hơn dự kiến.

#### 2. Chu trình TDD (Test-Driven Development) trong XP
TDD làm thay đổi hoàn toàn tư duy của lập trình viên thông qua vòng lặp **Red $\rightarrow$ Green $\rightarrow$ Refactor**:
1. **Red (Viết test fail):** Viết một đoạn mã kiểm thử tự động cho chức năng chưa tồn tại. Chạy test và bài test chắc chắn sẽ báo đỏ (Fail).
2. **Green (Viết code vừa đủ pass):** Viết một đoạn mã nguồn tối thiểu, đơn giản nhất có thể (thậm chí hard-code kết quả) miễn sao bài test chuyển sang màu xanh (Pass).
3. **Refactor (Tối ưu hóa mã nguồn):** Cải tiến cấu trúc code, xóa bỏ mã trùng lặp, tối ưu thuật toán nhưng đảm bảo tất cả bài test vẫn tiếp tục màu xanh (Green).
- *Lợi ích sống còn:* TDD tạo ra một "tấm lưới an toàn" (Safety Net). Khi nhóm thực hiện Refactoring hay tích hợp CI hàng ngày, họ có thể tự tin chỉnh sửa mã nguồn mà không sợ làm đổ vỡ các tính năng cũ.

---

### 복습 체크리스트
- [ ] Đọc vanh vách 4 giá trị cốt lõi của Tuyên ngôn Agile (Con người > Công cụ, SW chạy được > Tài liệu, Hợp tác > Đàm phán, Thích ứng > Kế hoạch).
- [ ] Phân biệt được trách nhiệm của 3 vai trò Scrum: PO (ưu tiên Backlog), SM (loại bỏ trở ngại), Dev Team (tự tổ chức nhận việc).
- [ ] Nhớ thời lượng họp Daily Scrum là 15 phút mỗi sáng và 3 câu hỏi đứng báo cáo.
- [ ] Phân biệt rõ sự khác nhau giữa Sprint Review (demo sản phẩm cho khách) và Sprint Retrospective (rút kinh nghiệm quy trình nội bộ).
- [ ] Đọc đúng trạng thái chậm tiến độ của dự án khi nhìn đường thực tế nằm trên đường lý tưởng trong Burn-down Chart.
- [ ] Thuộc lòng 5 giá trị cốt lõi của XP: 의사소통 (Giao tiếp), 단순성 (Đơn giản), 용기 (Dũng cảm), 존중 (Tôn trọng), 피드백 (Phản hồi).
- [ ] Kể tên và giải thích được ít nhất 5 thực hành then chốt của XP: Pair Programming, TDD, Refactoring, CI, Collective Ownership.
- [ ] Nhớ 6 chữ cái của nguyên tắc viết User Story: I-N-V-E-S-T.
