# Môn 1 · Bài 01 — Vòng đời và phương pháp phát triển phần mềm

> **Phạm vi nguồn:** các mục 001–009 trong `raw/notion/정보처리기사(1과목)/1과목(0~72) … .md`. Bài này không rút gọn ý gốc thành từ khóa rời; mỗi phát biểu Hàn ngữ được giải thích bằng tiếng Việt ngay sau đó.

> **Mạch kiến thức:** trước khi học yêu cầu (요구사항, requirement) và thiết kế (설계, design), cần biết dự án được tổ chức theo vòng đời nào. Vòng đời là “khung toàn bộ”; mô hình phát triển là “cách đi trong khung”; Agile, Scrum và XP là các cách tổ chức công việc khi cần phản hồi nhanh.

---

## 1. 소프트웨어 생명 주기 — Software Development Life Cycle — vòng đời phát triển phần mềm

**소프트웨어 생명 주기는 소프트웨어를 개발하기 위하여 정의, 운용, 유지보수 등의 과정을 단계별로 나눈 것이다.**

Vòng đời phần mềm (Software Development Life Cycle, SDLC, vòng đời phát triển phần mềm) là cách chia toàn bộ công việc làm phần mềm thành những giai đoạn có mục đích rõ ràng: xác định cần làm gì, thiết kế cách làm, xây dựng, kiểm thử, vận hành và bảo trì. Cụm “단계별로 나눈다” (chia theo từng giai đoạn) không có nghĩa mọi dự án luôn đi một chiều; nó nói rằng mỗi công việc phải có vị trí, đầu vào và đầu ra để đội dự án quản lý được.

### Keyword cần nhớ

- **정의 (definition, xác định/định nghĩa):** làm rõ vấn đề và yêu cầu mà hệ thống phải giải quyết.
- **운용 (operation, vận hành):** đưa phần mềm vào môi trường sử dụng thực tế và theo dõi nó hoạt động.
- **유지보수 (maintenance, bảo trì):** sửa lỗi, thích nghi với thay đổi và cải tiến sau khi triển khai.
- **산출물 (deliverable, sản phẩm bàn giao):** tài liệu hoặc kết quả hữu hình của một giai đoạn, ví dụ đặc tả yêu cầu hay mã nguồn đã kiểm thử.

### Hiểu đúng bản chất

SDLC là khung quản lý, không phải tên của một phương pháp cụ thể. Nó giúp trả lời ba câu hỏi: ở giai đoạn này đội đang quyết định điều gì, phải giao ra kết quả gì, và ai kiểm tra kết quả đó. Vì vậy SDLC liên quan trực tiếp đến lịch, chi phí, nhân lực và chất lượng: yêu cầu sai ở đầu vòng đời sẽ kéo theo thiết kế, mã nguồn và kiểm thử sai ở sau. Khi học bài yêu cầu kế tiếp, hãy xem yêu cầu là đầu vào của thiết kế; khi học kiểm thử, hãy xem kiểm thử xác nhận sản phẩm có thực hiện đúng yêu cầu ban đầu hay không.

Ví dụ: ứng dụng đặt hàng bắt đầu bằng yêu cầu “khách được đặt nhiều món”. Sau đó thiết kế tạo đơn hàng và chi tiết đơn hàng, lập trình hiện thực các chức năng, kiểm thử luồng đặt hàng, rồi vận hành thực tế. Nếu sau vận hành phát hiện cần hỗ trợ hoàn tiền, đó là bảo trì/thích nghi; thay đổi này có thể quay lại yêu cầu và thiết kế.

### Điểm dễ nhầm trong đề

- **생명 주기 = 개발 방법론** (vòng đời = phương pháp phát triển) là sai. SDLC là khung các giai đoạn; Waterfall, Spiral, Agile là các mô hình/phương pháp tổ chức hoặc thực hiện các giai đoạn đó.
- **생명 주기 = chỉ coding** là sai. Coding (구현, implementation) chỉ là một phần; yêu cầu, kiểm thử và bảo trì cũng thuộc vòng đời.

## 2. 폭포수 모형 — Waterfall Model — mô hình thác nước

**폭포수 모형은 한 단계가 완전히 끝나야만 다음 단계로 넘어갈 수 있는 선형 순차적 개발 모형이다.**

Mô hình thác nước (Waterfall Model, mô hình phát triển tuần tự tuyến tính) tổ chức công việc theo chuỗi: tính khả thi và kế hoạch → phân tích yêu cầu → thiết kế → hiện thực → kiểm thử → bảo trì. Về nguyên tắc, đầu ra đã được xem xét/duyệt của giai đoạn trước trở thành đầu vào cho giai đoạn sau. Vì vậy tài liệu và mốc phê duyệt có vai trò rất quan trọng.

**각 단계의 결과물이 명확하게 산출되어야 다음 단계를 진행할 수 있다.**

Mỗi giai đoạn phải có sản phẩm bàn giao rõ ràng trước khi sang giai đoạn tiếp theo. Chẳng hạn tài liệu yêu cầu được chốt trước khi đội thiết kế; điều này giúp kiểm soát phạm vi và trách nhiệm, nhưng khiến việc thay đổi muộn tốn kém vì phải sửa các sản phẩm đã hoàn thành phía sau.

### Keyword cần nhớ

- **선형 순차적 (linear sequential, tuyến tính tuần tự):** đi theo thứ tự giai đoạn đã định.
- **고전적 생명 주기 (classic life cycle, vòng đời cổ điển):** tên gọi thường gặp của Waterfall.
- **검토·승인 (review and approval, rà soát và phê duyệt):** kiểm tra đầu ra trước khi chuyển giai đoạn.

### Khi nào phù hợp và vì sao

Waterfall phù hợp khi yêu cầu ổn định, phạm vi có thể mô tả đầy đủ từ đầu và việc thay đổi bị kiểm soát nghiêm ngặt, ví dụ một dự án có quy định/hợp đồng chặt chẽ. Đừng hiểu “không thể quay lại” theo nghĩa vật lý tuyệt đối: thực tế vẫn có thể quay lại, nhưng mô hình giả định việc quay lại là đắt và cần quy trình phê duyệt, nên đề thi thường đối lập nó với tính linh hoạt của Agile.

## 3. 나선형 모형 — Spiral Model — mô hình xoắn ốc

**나선형 모형은 폭포수와 프로토타입 모형의 장점에 위험 분석 기능을 추가하여 점진적으로 개발하는 모형이다.**

Mô hình xoắn ốc (Spiral Model, mô hình phát triển lặp có trọng tâm rủi ro) phát triển hệ thống qua nhiều vòng. Mỗi vòng không chỉ làm thêm chức năng mà còn nhận diện, phân tích và giảm rủi ro trước khi đầu tư sâu hơn. “점진적” (incremental, tăng dần) nghĩa là sản phẩm được hoàn thiện qua các lần lặp, không phải chờ đến cuối mới có toàn bộ kết quả.

**주요 단계는 계획 수립 → 위험 분석 → 개발 및 검증 → 고객 평가의 반복이다.**

Mỗi vòng gồm: lập kế hoạch (계획 수립, planning), phân tích rủi ro (위험 분석, risk analysis), phát triển và xác minh (개발 및 검증, development and verification), rồi để khách hàng đánh giá (고객 평가, customer evaluation). Phản hồi ở bước cuối quyết định nội dung vòng tiếp theo. Vì thế Spiral phù hợp với dự án lớn, phức tạp hoặc có rủi ro kỹ thuật/chi phí cao.

### Keyword cần nhớ

- **보헴 (Boehm):** Barry Boehm, người đề xuất mô hình Spiral.
- **위험 분석 (risk analysis, phân tích rủi ro):** nhận diện điều chưa chắc chắn, ước lượng tác động và chọn cách giảm rủi ro.
- **프로토타입 (prototype, bản mẫu):** sản phẩm thử để kiểm chứng ý tưởng/yêu cầu; có thể được dùng để giảm rủi ro trong một vòng xoắn.

### Phân biệt nhanh

Waterfall ưu tiên trình tự và sự ổn định của tài liệu; Spiral ưu tiên quản lý rủi ro qua các vòng lặp. Agile cũng lặp, nhưng trọng tâm nổi bật của Agile là phản hồi nhanh với thay đổi yêu cầu, còn đặc điểm nhận diện của Spiral trong đề là **위험 분석 (risk analysis, phân tích rủi ro)**.

## 4. 애자일 모형 — Agile Model — mô hình/phương pháp Agile

**애자일 모형은 고객의 요구사항 변화에 유연하게 대응할 수 있도록 일정한 주기를 반복하며 진행하는 개발 방법론을 통칭한다.**

Agile (Agile Model/Agile methods, nhóm phương pháp phát triển linh hoạt) là tên chung cho các phương pháp làm việc theo chu kỳ ngắn, lấy phản hồi và sự hợp tác với khách hàng làm trung tâm. Nó không phải một kỹ thuật duy nhất; Scrum, XP, Kanban và Lean là các cách triển khai thuộc tư duy Agile.

**애자일은 계획보다 변화에 대한 반응을 중시한다.**

Agile không phủ nhận kế hoạch. Ý này có nghĩa khi thực tế thay đổi, đội không bám cứng vào kế hoạch cũ mà dùng phản hồi để điều chỉnh ưu tiên. Mỗi lần lặp (iteration, 반복) tạo ra một phần kết quả có thể kiểm tra; nhờ đó sai lệch được thấy sớm hơn so với việc chỉ kiểm tra ở cuối dự án.

### Bốn giá trị cốt lõi của Agile Manifesto

1. **프로세스와 도구보다 개인과 상호작용을 중시한다.** — Coi trọng con người và tương tác (individuals and interactions, con người và tương tác) hơn quy trình và công cụ. Công cụ vẫn cần, nhưng không thay thế được việc trao đổi để giải quyết vấn đề.
2. **포괄적인 문서보다 작동하는 소프트웨어를 중시한다.** — Coi trọng phần mềm chạy được (working software, phần mềm hoạt động) hơn tài liệu quá đầy đủ. Không phải “không viết tài liệu”; tài liệu phải đủ để phục vụ sản phẩm và vận hành.
3. **계약 협상보다 고객과의 협업을 중시한다.** — Coi trọng hợp tác với khách hàng (customer collaboration, hợp tác khách hàng) hơn chỉ đàm phán hợp đồng.
4. **계획을 따르기보다 변화에 대응하는 것을 중시한다.** — Coi trọng phản hồi với thay đổi (responding to change, ứng phó thay đổi) hơn bám kế hoạch cứng nhắc.

## 5. 스크럼 — Scrum — khung làm việc Scrum

**스크럼은 팀이 중심이 되어 짧은 주기를 반복하면서 제품을 개발하는 애자일 프레임워크이다.**

Scrum (Scrum framework, khung Scrum) cụ thể hóa tư duy Agile bằng vai trò, danh sách công việc và các sự kiện định kỳ. Mục tiêu là biến yêu cầu còn nhiều thay đổi thành những đợt làm việc ngắn, có kết quả kiểm tra được. Scrum không phải người quản lý ra lệnh làm gì; nó tạo khung để nhóm tự tổ chức và minh bạch tiến độ.

### Vai trò và tạo tác

- **제품 책임자, PO (Product Owner, chủ sở hữu sản phẩm):** quản lý và sắp thứ tự ưu tiên của **제품 백로그 (Product Backlog, danh sách toàn bộ yêu cầu/công việc sản phẩm)** theo giá trị sản phẩm.
- **스크럼 마스터, SM (Scrum Master, người hỗ trợ Scrum):** giúp đội áp dụng Scrum, loại bỏ cản trở; không phải cấp trên giám sát hay giao việc cho lập trình viên.
- **개발 팀 (Development Team, nhóm phát triển):** nhóm liên chức năng tạo phần tăng trưởng sản phẩm có thể sử dụng.
- **스프린트 (Sprint, chu kỳ nước rút):** khoảng thời gian cố định, thường 2–4 tuần theo tài liệu nguồn, để tạo một phần sản phẩm hoàn chỉnh có thể xem xét.

## 6. 스크럼 개발 프로세스 — Scrum process — quy trình vận hành Scrum

**제품 백로그에서 시작하여 스프린트 계획, 실행, 검토, 회고를 거쳐 진행된다.**

Quy trình bắt đầu từ Product Backlog. Trong Sprint Planning (스프린트 계획, lập kế hoạch Sprint), nhóm chọn việc ưu tiên và xác định mục tiêu Sprint. Trong khi thực hiện, Daily Scrum (일일 스크럼, họp Scrum hằng ngày) là cuộc họp ngắn, thường khoảng 15 phút, để đồng bộ công việc và phát hiện trở ngại; nó không phải cuộc họp báo cáo dài với quản lý.

Kết thúc Sprint, Sprint Review (스프린트 검토, xem xét Sprint) trình bày và kiểm tra kết quả với các bên liên quan để lấy phản hồi về sản phẩm. Sau đó Sprint Retrospective (스프린트 회고, hồi tưởng/cải tiến Sprint) nhìn lại cách cả nhóm làm việc và chọn cải tiến cho Sprint sau. Burn-down Chart (소멸 차트, biểu đồ công việc còn lại) cho thấy lượng công việc còn lại theo thời gian, nên hỗ trợ theo dõi xu hướng chứ không thay thế đánh giá chất lượng.

## 7. XP — eXtreme Programming — lập trình cực hạn

**XP는 고객의 참여와 개발 과정의 반복을 극대화하여 생산성을 높이는 애자일 방법론이다.**

XP (eXtreme Programming, lập trình cực hạn) là phương pháp Agile nhấn mạnh thực hành kỹ thuật và phản hồi nhanh. Nó dùng các lần phát hành ngắn (short release, phát hành ngắn), thiết kế đơn giản và sự tham gia liên tục của khách hàng để phát hiện sai lệch sớm. Khi đề hỏi giá trị XP, hãy nhớ năm từ: **의사소통 (communication, giao tiếp), 단순성 (simplicity, đơn giản), 용기 (courage, dũng khí), 존중 (respect, tôn trọng), 피드백 (feedback, phản hồi)**.

### Chốt liên kết để làm đề

SDLC nói toàn bộ dự án đi qua những giai đoạn nào. Waterfall chọn đường đi tuần tự khi yêu cầu ổn định. Spiral quay theo vòng để quản lý rủi ro. Agile lặp ngắn để thích nghi với thay đổi. Scrum là khung Agile tổ chức nhóm bằng backlog và sprint; XP là phương pháp Agile nhấn mạnh các thực hành phát triển và phản hồi. Nhớ được quan hệ “khung → mô hình → phương pháp/khung triển khai” sẽ tránh nhầm các khái niệm này với nhau.
