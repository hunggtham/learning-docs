# 13 — PMP scenario reasoning và chiến lược làm bài

## PMP kiểm tra application nhiều hơn recall

Exam Content Outline 2026 nói rõ câu hỏi đặt candidate vào on-the-job situations và yêu cầu áp dụng project management concepts/experience. Vì vậy học bằng cách nhớ một câu “luôn escalate” hoặc “luôn nói chuyện với team trước” dễ thất bại khi context thay đổi.

Cách bền hơn là đọc scenario như một state machine: hiện tại đang ở state nào, signal nào mới xuất hiện, objective/constraint nào bị đe dọa, authority ở đâu, và action nào là next best step với information hiện có.

PMP scenario thường không hỏi “tool nào tồn tại?” mà hỏi “trong state này, tool/process nào hợp lý tiếp theo?”. Vì vậy thứ tự action và context quan trọng ngang knowledge.

## Đọc scenario theo state, không theo keyword

Keyword matching dễ sai. Thấy “conflict” không có nghĩa answer luôn “collaborate”; thấy “change” không có nghĩa luôn “submit change request”; thấy “risk” không có nghĩa luôn “update risk register”.

Cần xác định state. Risk đã xảy ra thì nó đã thành issue. Change trong adaptive backlog có mechanism khác change đụng predictive baseline. Conflict safety/ethics khác disagreement thông thường.

Keyword chỉ giúp locate concept. State mới quyết định action.

Một cách đọc tốt là tách **surface** khỏi **reasoning core**. Surface có thể là vendor, sprint, construction, AI, stakeholder hoặc dashboard. Reasoning core thường vẫn quay về một trong vài vấn đề: information thiếu, authority chưa đúng, threshold bị vượt, assumption bị phá, response chưa theo đúng sequence, hoặc local optimization đang đe dọa objective lớn hơn.

## Khung reasoning tám bước

### 1. Xác định delivery context

Project đang predictive, adaptive hay hybrid? Điều này thay đổi location của scope decision, cadence, artifact và change mechanism. “Requirement thay đổi” trong predictive baseline khác “backlog item đổi priority” trong adaptive project.

Đừng suy diễn methodology nếu scenario không cho evidence. Chỉ dùng context được nêu hoặc behavior đủ rõ.

### 2. Xác định thời điểm trong lifecycle

Problem xuất hiện ở initiation, planning, delivery, transition hay closure? Cùng một concern có action khác theo timing.

Operations chưa được train ở đầu project là planning dependency; một ngày trước go-live nó là readiness issue. Vendor chưa ký contract khác vendor đang breach contract.

### 3. Xác định loại signal

Đây là risk chưa xảy ra, issue đã xảy ra, change request, conflict, defect, compliance breach, stakeholder expectation gap hay information gap? Gọi đúng loại problem giúp chọn process đúng.

Một câu hỏi exam thường đặt hai option đều “tốt” nhưng một option xử lý sai loại signal. Ví dụ thêm risk vào register khi event đã xảy ra là quá muộn nếu action issue cần bắt đầu ngay.

### 4. Tìm objective và constraint bị tác động

Đừng dừng ở symptom. Delay một task có thể không quan trọng nếu có float; một defect nhỏ có thể critical nếu liên quan privacy. Hỏi effect lên value, scope, schedule, finance, quality, risk và business environment.

Nếu scenario nêu mandatory regulation, safety hoặc contractual boundary, constraint đó thường thay decision space đáng kể.

### 5. Kiểm tra authority và governance

PM có authority xử lý hay cần sponsor/CCB/product owner/compliance body? Escalation không phải default cho mọi problem; nó phù hợp khi issue vượt authority/tolerance hoặc cần decision ở governance level.

Câu trả lời tốt thường tôn trọng decision right. PM không tự thay approved baseline nếu cần authority khác; PM cũng không escalate một local team issue mà team đủ quyền giải quyết.

### 6. Xác định information gap

Ta đã có đủ evidence để action chưa? Nếu root cause chưa rõ hoặc impact chưa được phân tích, action irreversible thường premature.

Review plan, contract, risk response, acceptance criterion hoặc speak with relevant stakeholder có thể là bước đúng khi chúng làm information gap nhỏ hơn. Nhưng “analyze more” không phải excuse khi safety/compliance incident đã rõ và cần containment ngay.

### 7. Xem tính reversible của action

Reversible action chi phí thấp có thể làm sớm để tạo evidence. Irreversible action như terminate vendor, fire team member, rebaseline hoặc major scope commitment cần evidence và authority mạnh hơn.

Câu hỏi này giúp phân biệt giữa option “investigate/facilitate/pilot” và option quá mạnh khi context còn uncertain.

### 8. Chọn next action, không chọn entire plan

Nhiều câu hỏi hỏi “what should the project manager do first/next?”. Một answer có thể đúng về tổng thể nhưng sai thứ tự. Ví dụ trước khi submit change cho approval có thể cần impact analysis; trước khi blame vendor cần review contract và facts.

Nếu stem hỏi “should have done”, reasoning quay lại preventive action trước failure. Nếu hỏi “do next”, không chọn retrospective preventive action trước khi current issue được contain.

## Bộ lọc năm cổng khi hai đáp án đều có vẻ đúng

Khi còn hai option hợp lý, đừng chọn theo câu chữ “nghe PMP hơn”. Hãy đưa chúng qua năm cổng.

Cổng thứ nhất là **state fit**: option có xử lý đúng loại state hiện tại không, hay đang dùng process của risk cho issue, của planning cho incident, hoặc của predictive cho backlog adaptive?

Cổng thứ hai là **authority fit**: người thực hiện có quyền làm việc đó chưa? Một action đúng về kỹ thuật nhưng vượt authority vẫn là action sai trong governance context.

Cổng thứ ba là **information fit**: decision có đang đòi bằng chứng mà scenario chưa có không? Nếu một option irreversible nhưng facts còn mơ hồ, option tạo thêm evidence thường mạnh hơn.

Cổng thứ tư là **sequence fit**: action đúng nhưng có đúng lúc không? Containment thường đi trước root-cause analysis khi harm đang xảy ra; impact analysis đi trước approval; approval đi trước implementation khi baseline cần governance.

Cổng thứ năm là **system fit**: option có giải objective/root cause hay chỉ làm một local metric đẹp hơn? Thêm overtime có thể tăng activity nhưng không sửa approval bottleneck; gửi nhiều report hơn không sửa expectation gap.

Nếu một option qua đủ năm cổng còn option kia fail một cổng quan trọng, decision thường rõ hơn nhiều.

## Phân biệt assess, act và escalate

Ba loại option thường cạnh tranh trong câu hỏi.

Assess phù hợp khi information thiếu và không có immediate harm. Act phù hợp khi response đã planned, authority rõ hoặc failure cần containment. Escalate phù hợp khi threshold/authority bị vượt hoặc cross-organizational decision cần cấp cao hơn.

Mẹo “luôn assess trước” sai trong emergency. Mẹo “luôn act proactively” sai khi chưa hiểu impact. Mẹo “không bao giờ escalate” sai khi governance boundary rõ.

Mental model là proportional response.

## Proactive không đồng nghĩa tự ý

PMP thường đánh giá cao proactive behavior, nhưng proactive phải nằm trong governance. PM có thể gather information, facilitate, remove impediment và execute approved contingency mà không chờ. Nhưng thay legal requirement hoặc approve budget ngoài authority không phải proactive; đó là governance violation.

Tư duy tốt là “chủ động trong boundary, escalate khi vượt boundary”.

## Team conflict

Khi team conflict thông thường, ưu tiên hiểu source/context và facilitate resolution gần những người liên quan trước khi dùng authority nặng. Tách interest khỏi position và khuyến khích direct problem solving.

Nếu conflict liên quan harassment, safety, discrimination, ethics hoặc policy violation, ordinary conflict-resolution sequence có thể không đủ; cần formal process/escalation phù hợp.

Nếu root cause là resource conflict do organization, coaching hai cá nhân có thể không giải system constraint.

## Stakeholder dissatisfaction

Khi stakeholder unhappy, xác định expectation gap và evidence trước. “Gửi thêm report” hiếm khi giải concern nếu success criterion khác nhau.

Nếu stakeholder mới xuất hiện hoặc influence đổi, update engagement strategy. Nếu request mới ảnh hưởng scope, chuyển sang change/prioritization mechanism phù hợp thay vì hứa ngay để làm họ hài lòng.

## Risk và issue

Risk chưa xảy ra cần owner, response và trigger. Khi trigger xảy ra, execute response/contingency và quản lý impact như issue.

Nếu risk mới được identify, analyze trước khi random response. Nếu known risk materialize và contingency đã approved, không cần quay lại từ đầu chỉ để “update register” trước action cần thiết.

## Change request

Predictive baseline change thường cần impact analysis trước approval và implementation sau approval. Adaptive product change có thể đi qua backlog prioritization nếu nằm trong guardrail.

Silent implementation gần như luôn problematic vì effect lên commitment không visible. Nhưng không phải mọi backlog reorder cần CCB.

## Defect và quality problem

Defect cần phân biệt severity, customer/compliance impact và root cause. Immediate containment có thể đi trước root-cause analysis khi harm đang xảy ra.

Sau containment, process improvement quan trọng hơn chỉ sửa từng symptom. Nếu cùng defect class lặp lại, exam answer chỉ “fix defect” có thể quá hẹp.

## Vendor problem

Khi vendor delay hoặc quality kém, review contract/SOW, facts và dependency trước khi punitive action. Collaborate recovery trong boundary contract, nhưng enforce/escalate nếu material breach vượt tolerance.

“Thêm người” không phải universal solution. Bottleneck có thể là third-party dependency hoặc approval.

Nếu option nhắc terminate vendor, claim hoặc penalty, hãy kiểm tra ba lớp trước: entitlement/contract right, causation/facts và impact/authority. Punitive action trước evidence thường là distractor mạnh vì nghe decisive nhưng phá governance.

## Agile/adaptive scenario

Self-managing team nên được trao quyền trong product/delivery boundary. PM/leader remove impediment, facilitate stakeholder và protect team khỏi micro-management.

Product Owner quản lý product backlog/value trong Scrum context. PM không nên tự reorder backlog để “cứu schedule” nếu decision right không thuộc mình.

Velocity không phải KPI để ép team. Retrospective nhằm improve system, không blame cá nhân.

Trong adaptive context, “change control” vẫn tồn tại nhưng control object khác. Product priority có thể thay thường xuyên trong guardrail; budget cap, privacy policy, contractual obligation hoặc release gate vẫn cần governance rõ. Vì vậy option “agile nên chấp nhận change ngay” cũng máy móc như “mọi change phải qua CCB”.

## Hybrid scenario

Hybrid question thường xoay quanh interface: adaptive team gặp fixed contract, regulatory gate hoặc predictive dependency.

Không chọn answer “chuyển toàn bộ sang agile” chỉ vì một phần uncertainty cao. Hỏi constraint nào thực sự cố định và feedback loop nào có thể adaptive.

Đặc biệt chú ý state naming. `Done` trong sprint có thể chưa đồng nghĩa vendor accepted, regulator approved hoặc production ready. Nếu scenario cho nhiều gate, hãy xác định chính xác state của deliverable trước khi chọn action.

## Business environment và strategy change

Khi market, regulation hoặc strategy thay đổi, reassess business case/value/risk. Bám baseline cũ chỉ vì đã approve là sunk-cost behavior.

PM thường cần surface evidence và recommendation; governance/sponsor quyết continuation nếu vượt authority.

Nếu external change làm project không còn tạo value, câu hỏi không còn đơn thuần là “làm sao giao đúng plan”. Có thể phải compare continue, pivot, phase, pause hoặc terminate theo future value và transition impact.

## Compliance và safety

Mandatory compliance/safety boundary có priority đặc biệt. Không de-scope requirement bắt buộc để giữ deadline nếu không có authorized/legal exception mechanism.

Nếu violation đang gây exposure, containment và proper escalation có thể phải xảy ra trước full analysis. Business pressure không tự override regulation.

## Ethics và transparency

Không che forecast xấu, defect hoặc conflict of interest để bảo vệ hình ảnh project. Decision maker cần material information.

Confidentiality không đồng nghĩa concealment. Share đúng người, đúng channel, đủ evidence.

## Formula questions: nhớ assumption trước công thức

Nếu gặp EVM, CPM, PERT hoặc EMV, hãy viết mental meaning trước arithmetic. CPI dưới 1 nghĩa cost efficiency kém hơn baseline; critical path là đường quyết định minimum modeled duration; PERT là estimate summary dựa trên three points; EMV là probability-weighted impact. Formula không tự ra decision nếu context/assumption chưa rõ.

Khi có nhiều EAC formula, clue quan trọng là assumption: current variance tiếp tục, one-time, hay cả CPI/SPI ảnh hưởng phần còn lại. Arithmetic đứng sau causal story.

Một câu formula có thể được giấu trong scenario. Ví dụ dashboard cho `CPI = 0.82`, `SPI = 1.03` và management hỏi có nên báo “project healthy” hay không. Arithmetic chỉ cho biết cost efficiency kém baseline còn earned schedule đang hơi ahead theo EVM; decision vẫn cần scope, quality, forecast và cause.

## Đọc dashboard, artifact và data-based question

Exam 2026 có thể đưa candidate vào tình huống dùng tools, data, project artifact hoặc case study thay vì chỉ paragraph text. Khi gặp một dashboard hoặc artifact, đừng đọc mọi field như nhau. Hãy xác định trước decision question rồi mới tìm signal liên quan.

Một dashboard tốt nên được đọc theo chuỗi:

```text
objective/decision cần đưa ra
→ metric/artifact nào thực sự liên quan
→ baseline/threshold là gì
→ actual/trend/forecast đang nói gì
→ data có limitation nào
→ authority/action tiếp theo là gì
```

Ví dụ dashboard có `SPI = 0.92`, `CPI = 1.04`, defect severity-1 tăng và go-live còn hai tuần. Không nên kết luận “cost tốt nên project ổn”. Quality signal có thể dominate release decision. Ngược lại một red cost variance nhỏ có thể không cần escalation ngay nếu nằm trong tolerance và forecast vẫn recoverable.

Artifact cũng cần đọc theo purpose. Risk register trả lời uncertainty/response; issue log trả lời condition đã xảy ra; change log trả lời governance state; RTM trả lời traceability; decision log trả lời rationale/assumption. Nếu câu hỏi đưa artifact nhưng option yêu cầu update một artifact khác, hãy hỏi update đó có làm decision tốt hơn ngay lúc này không hay chỉ là administrative action.

## Case-study/practicum reasoning: giữ một state model xuyên nhiều câu

Case-study item khác independent question ở chỗ nhiều câu có thể dùng chung context, data hoặc artifact. Sai lầm lớn là reset mental model ở mỗi câu và quên các fact đã establish trước đó.

Hãy tạo một state model ngắn trong đầu: objective, delivery mode, key constraint, current issue/risk, decision rights, relevant thresholds và unresolved assumptions. Khi case đưa thêm evidence, update state model chứ không xây lại từ đầu.

Nếu artifact mới mâu thuẫn narrative cũ, ưu tiên evidence cụ thể và xem đó như signal cần reconcile. Ví dụ status slide nói green nhưng defect dashboard cho thấy release blocker; đây không phải hai fact độc lập mà là information-quality problem.

Case study cũng thường kiểm tra propagation. Một vendor delay có thể làm schedule slip, kích hoạt contract right, tăng cost, đẩy UAT vào regulatory window khác và thay stakeholder expectation. Đừng cố giữ câu hỏi trong một knowledge area duy nhất.

## Loại distractor thường gặp

Một distractor có thể đúng nhưng quá muộn, như update lesson learned trước khi contain incident. Một distractor đúng nhưng vượt authority, như PM tự approve major budget change. Một distractor xử lý symptom, như tăng overtime khi root cause là dependency. Một distractor quá punitive khi chưa có facts, như terminate vendor ngay. Một distractor quá passive, như “monitor” risk đã materialize.

Ngoài ra có distractor **administratively correct but decision-useless**: update một register trước khi làm action cần thiết. Có distractor **locally optimal**: tối ưu schedule nhưng phá safety/quality. Có distractor **framework-pure**: áp Scrum/CCB textbook nhưng bỏ qua hybrid constraint của scenario. Và có distractor **evidence-blind**: chọn action dựa trên average metric dù segmentation cho thấy high-impact tail.

Đọc option theo action ordering, authority, evidence và system effect thường giúp loại chúng mà không cần nhớ phrase template.

## Không thêm fact không có trong scenario

Đừng tự giả định sponsor hostile, team incompetent hay contract fixed-price nếu đề không nói. Hidden assumption có thể làm option sai trở nên hợp lý.

Dùng thông tin được cung cấp và project-management principle đủ để suy luận. Nếu hai answer chỉ khác vì một fact không nêu, xem lại wording như first/next, authority hoặc lifecycle.

## Sáu mini-scenario để luyện reasoning

### Mini 1 — Known risk đã materialize

Vendor shipment có risk đã được nhận diện, contingency plan đã approve và trigger vừa xảy ra. Option A là update risk register; option B là execute contingency rồi cập nhật artifact/status phù hợp.

Nếu không có information mới làm contingency invalid, B mạnh hơn vì state đã chuyển từ risk sang issue/triggered response. Update register có thể cần nhưng không nên đứng trước response đã được authorize.

### Mini 2 — Stakeholder yêu cầu feature mới trong adaptive product

Product Owner nhận request mới từ key customer. Feature có value tiềm năng nhưng chưa có evidence và sprint hiện tại đang hướng tới một compliance goal. PM tự reorder backlog sẽ vượt decision right; đưa mọi request qua CCB lại quá predictive nếu backlog nằm trong product guardrail.

Next step hợp lý là để Product Owner đánh giá value/priority cùng relevant evidence và constraint, giữ compliance commitment nếu mandatory. Reasoning nằm ở authority + objective, không ở slogan “customer first”.

### Mini 3 — Vendor quality issue và contract tension

Vendor giao component có defect lặp lại. Sponsor muốn phạt ngay. Team chưa rõ defect do vendor spec violation hay integration environment của buyer.

Punitive action ngay là irreversible và evidence yếu. Review acceptance criteria, contract/SOW, defect evidence và causation trước; containment technical nếu harm đang tiếp tục. Sau đó mới recovery/claim/escalation theo contract boundary.

### Mini 4 — Privacy incident trước go-live

Log cho thấy production-like test data chứa personal information đã bị gửi sang environment không được approve. Đây không còn là hypothetical risk. “Phân tích thêm trong risk workshop tuần sau” quá chậm.

Contain exposure, activate incident/compliance process, preserve evidence và escalate theo policy trước; root-cause analysis sâu theo sau. Sequence thay đổi vì harm/compliance boundary đã rõ.

### Mini 5 — Dashboard cho signal trái chiều

Project có `CPI = 1.06`, milestone forecast vẫn đúng ngày nhưng severity-1 defect tăng và test queue kéo dài. Nếu option nói “status green vì cost/schedule tốt”, nó local-optimize hai metric và bỏ quality/readiness.

PM cần surface integrated state, investigate quality bottleneck và update forecast/readiness evidence. Healthy project không được định nghĩa chỉ bởi hai index.

### Mini 6 — Project đã close nhưng benefit chưa xuất hiện

System go-live, acceptance hoàn tất, budget đóng nhưng adoption sau ba tháng thấp hơn target. Reopen project chỉ vì benefit thấp có thể sai boundary; tuyên bố success hoàn toàn cũng sai.

Benefits owner/product/operations cần investigate adoption drivers theo benefits plan. Nếu corrective initiative vượt project closure boundary, governance có thể authorize new work. Output acceptance và benefit realization là hai state khác nhau.

## Time management cho exam 2026

Theo ECO July 2026 hiện hành, PMP có 180 câu trong 240 phút; 170 câu được chấm và 10 câu là pretest không tính điểm. Exam có hai break 10 phút. ECO hiện mô tả break đầu sau case-study section và break thứ hai khoảng giữa phần independent questions; sau khi review và bắt đầu break, bạn không quay lại section trước.

Average thô là 80 giây/câu, nhưng không nên cố giữ từng câu đúng 80 giây. Case-study/artifact item có thể cần nhiều context hơn trong khi một số independent question ngắn hơn. Dùng time budget theo section/block, đánh dấu câu gây tắc và bảo vệ thời gian cho phần còn lại.

Câu dài scenario nên đọc question stem để biết đang tìm “first”, “next”, “best” hay “should have done”, sau đó quay lại evidence trong scenario. Với artifact/data question, đọc decision ask trước rồi mới scan dashboard. Đừng dành quá nhiều phút để chứng minh một câu ambiguous nếu có thể mark và quay lại trong cùng section.

## Cách luyện practice question đúng cách

Sau mỗi câu sai, không chỉ ghi đáp án đúng. Ghi state đã nhận diện sai ở đâu: delivery context, risk vs issue, authority, sequencing, constraint, artifact interpretation hay assumption.

Nếu sai vì không biết term, review glossary. Nếu sai vì chọn action đúng nhưng sai thứ tự, luyện state transition. Nếu sai vì đọc nhầm dashboard, ghi metric nào đã được over-weight và signal nào bị bỏ qua. Nếu sai vì áp mẹo máy móc, tạo counterexample nơi mẹo đó thất bại.

Error log nên phân loại reasoning failure để practice có feedback loop. Mục tiêu là giảm một **class of error**, không chỉ nhớ đáp án của một câu.

## Cách tự tạo scenario

Lấy một case cơ bản rồi đổi một biến. Conflict thông thường → harassment. Deadline target → legal deadline. Risk chưa xảy ra → event đã xảy ra. Predictive → adaptive. PM có authority → vượt tolerance. Average metric tốt → tail segment xấu. Vendor delay → vendor delay kèm contractual entitlement dispute.

Nếu answer của bạn thay đổi hợp lý theo một biến, mental model đang hoạt động. Nếu answer không bao giờ đổi, có thể bạn đang dùng slogan.

Một bài tập mạnh hơn là giữ stem nhưng thay artifact. Ví dụ cùng một project, dashboard A cho schedule slip nhỏ nhưng quality ổn; dashboard B cho schedule đúng nhưng severity-1 defect tăng. Nếu action không đổi, bạn có thể đang bỏ qua evidence.

## Cách học chapter theo exam loop

Đọc chapter để hiểu mechanism. Làm scenario để test transfer. Khi sai, quay về đúng conceptual gap, không đọc lại toàn bộ PMBOK một cách ngẫu nhiên. Sau đó làm lại biến thể khác để kiểm tra generalization.

Exam prep hiệu quả là feedback loop giống project learning:

```text
mental model
→ scenario/artifact
→ decision
→ feedback
→ classify reasoning error
→ revisit đúng concept
→ new variant
```

Khi tỷ lệ đúng tăng nhưng error log vẫn cho thấy cùng một reasoning failure, đừng vội tăng số câu. Hãy sửa mechanism trước. Ngược lại, nếu concept hiểu tốt nhưng tốc độ chậm, practice nên tập trung recognition của state/authority/sequence dưới time pressure.

## Final mental model

> Câu hỏi PMP tốt là một bài kiểm tra decision quality trong context. Hãy xác định state, signal, objective, authority, evidence, reversibility và thứ tự action; với exam 2026, áp cùng framework đó cho text scenario, dashboard, artifact và case study thay vì học từng item format như một kỹ năng riêng.

Sau chapter này, dùng [Artifacts & Traceability](./14_artifacts_information_and_traceability.md) để hiểu information structure, [Quantitative Reasoning](./15_quantitative_reasoning_worked_examples.md) để luyện formula theo assumption, [End-to-end Case Studies](./16_end_to_end_case_studies.md) để luyện interaction giữa nhiều domain, [Coverage Audit](./COVERAGE_AUDIT.md) để tìm vùng cần ôn và [Glossary](./GLOSSARY.md) để chuẩn hóa thuật ngữ.