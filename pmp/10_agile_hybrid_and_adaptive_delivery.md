# 10 — Agile, adaptive và hybrid delivery

## Agile là feedback economics, không phải ceremony

Agile (애자일) có giá trị khi uncertainty cao và feedback sớm có thể thay đổi decision. Bản chất không nằm ở daily meeting hay board, mà ở việc giảm batch size của learning, giao increment có thể kiểm chứng, đưa customer/stakeholder feedback vào planning và cho team quyền thích ứng trong guardrail.

Nếu tổ chức chạy sprint nhưng mọi scope đã khóa một năm, feedback không thể thay priority và release vẫn big-bang, ceremony agile không tạo adaptive capability.

Một mental model hữu ích là economics của feedback: feedback càng đến sớm, cost sửa assumption càng thấp. Nhưng feedback cũng có chi phí. Vì vậy cadence nên đủ nhanh để giảm risk đáng kể nhưng không nhanh đến mức ceremony lớn hơn learning value.

## Adaptive loop: hypothesis → evidence → decision

Adaptive delivery chỉ thật sự adaptive khi work nối vào hypothesis. Team đang tin điều gì về user, solution, architecture hoặc process? Increment/experiment nào tạo evidence? Evidence nào đủ mạnh để giữ, đổi hoặc bỏ hypothesis?

Nếu sprint chỉ biến backlog item thành code nhưng không có câu hỏi học tập, team có thể giao nhanh mà learning chậm. Ngược lại, discovery tạo nhiều insight nhưng không thay backlog cũng chỉ là research theater.

Một vòng adaptive hoàn chỉnh có dạng:

```text
hypothesis → smallest useful test/increment → evidence → interpretation → decision → next hypothesis
```

Điểm quan trọng là decision. Feedback không có quyền thay direction thì chỉ là information collection.

## Empiricism: transparency, inspection, adaptation

Adaptive delivery dựa trên empiricism: làm cho state đủ minh bạch để inspect, sau đó adaptation dựa trên evidence. Nếu work status không đáng tin, backlog không phản ánh priority thật hoặc increment không thực sự usable, inspection trở nên giả và adaptation cũng sai.

Transparency không có nghĩa báo cáo thật nhiều. Nó nghĩa những information quan trọng cho decision được nhìn thấy đúng lúc: quality state, blocked dependency, unfinished work, forecast và stakeholder feedback.

Empiricism còn phụ thuộc quality của evidence. Một demo cho 5 user thân thiện không chứng minh product-market fit. Một metric aggregate có thể che segment failure. Inspection tốt phải hiểu sample, measurement boundary và bias.

## Product goal tạo stable direction cho adaptive scope

Adaptive scope có thể thay nhưng system vẫn cần direction đủ ổn định. Product goal/outcome tạo constraint cho local adaptation: backlog có thể đổi, nhưng mọi đổi phải giải thích vì sao giúp objective tốt hơn.

Nếu backlog thay liên tục theo stakeholder mới nhất mà không có stable outcome, organization đang phản ứng với noise chứ không learning. Adaptive không đồng nghĩa direction instability.

Một goal tốt cũng có stop criterion. Nếu evidence liên tục cho thấy hypothesis không tạo value, team phải có permission dừng/pivot thay vì tiếp tục vì roadmap đã công bố.

## Product backlog như một option set

Backlog không phải một contract rằng mọi item sẽ được xây. Nó là ordered set của possibilities theo value, risk, learning và dependency. Item gần delivery được refine chi tiết hơn; item xa giữ coarse-grained để tránh overplanning.

Product Owner chịu trách nhiệm tối ưu value và ordering trong Scrum context. Project manager trong environment PMP có thể phối hợp governance, dependency, stakeholder, risk và organizational boundary mà không giành micro-control của self-managing team.

Backlog item nên đủ nhỏ để tạo learning trong thời gian hợp lý. Một item quá lớn che nhiều assumption; một item quá nhỏ lại tạo administrative overhead. Decomposition tốt theo vertical slice thường tạo evidence tốt hơn chia theo technical layer thuần túy.

## Backlog aging và option decay

Option trong backlog không giữ value mãi. Requirement có thể hết relevance, dependency đổi, market window đóng hoặc assumption ban đầu không còn đúng.

Backlog quá lớn có carrying cost: refinement, duplicate item, search cost và cognitive load. Item không có owner/rationale hoặc không được review nhiều tháng có thể trở thành inventory stale.

Vì vậy backlog refinement không chỉ thêm detail; nó còn xóa option không còn đáng giữ. “Không làm” là một output hợp lệ của learning.

## Prioritization không chỉ là business value

Priority nên phản ánh value, risk, learning, dependency và cost of delay. Một technical spike có direct business value thấp nhưng có thể rất cao về information value. Một compliance item có customer-visible value thấp nhưng mandatory. Một dependency item có thể cần làm sớm để unblock nhiều work sau.

Vì vậy “làm feature có value cao nhất trước” là quá đơn giản. Adaptive planning cần nhìn toàn bộ system objective.

Priority còn phụ thuộc expiry. Một small feature có value vừa nhưng market window một tuần có thể nên đi trước feature value lớn hơn nhưng không time-sensitive.

## Cost of delay và sequencing

Cost of delay biến “trễ” thành economic consequence. Nhưng nó không nhất thiết tuyến tính. Seasonal launch có cliff; regulatory deadline có penalty step; learning item có value giảm nếu đến sau architecture commitment.

Adaptive sequencing nên nhìn value over time, không chỉ static priority. Điều này nối backlog decision với finance/schedule reasoning ở chapter `05–06`.

## Increment, Definition of Done và quality boundary

Increment có ý nghĩa khi đủ integrated và usable để tạo evidence. Definition of Done tạo shared quality boundary cho “done”. Nếu mỗi sprint có nhiều item “90% xong” nhưng test/integration dồn cuối release, project vẫn tích batch lớn và hidden inventory.

Acceptance criteria áp cho item cụ thể; Definition of Done là quality bar chung. Hai thứ bổ sung nhau.

Nếu Definition of Done bỏ integration, security scan hoặc documentation bắt buộc, team có thể tối ưu sprint completion nhưng tạo release debt. “Done” phải phản ánh trạng thái đủ thật để management không bị false progress.

## Done, deployed, released và value realized khác nhau

Một increment có thể Done nhưng chưa deploy. Code có thể deploy nhưng feature flag chưa release cho user. Feature có thể release nhưng chưa được adopt. Adoption có thể xảy ra nhưng benefit chưa materialize.

Phân biệt các state này ngăn false progress. “Chúng ta release mỗi sprint” không đồng nghĩa business nhận value mỗi sprint nếu user chưa dùng hoặc operational dependency chưa sẵn sàng.

Adaptive reporting nên nói rõ state nào đang được đo.

## MVP, prototype, experiment và increment không phải một thứ

Prototype dùng để học về feasibility, interaction hoặc solution shape; nó có thể hoàn toàn không production-ready. Experiment dùng để kiểm tra một hypothesis. Minimum Viable Product (MVP) là phiên bản đủ nhỏ để kiểm tra value proposition với user thật hoặc market thật. Increment là phần product tích hợp đáp ứng quality boundary đã định.

Nhầm bốn khái niệm này tạo governance sai. Một prototype có thể chấp nhận security control nhẹ vì chạy trong sandbox; một increment customer-facing thì không. Một MVP không có nghĩa “sản phẩm chất lượng thấp”; nó giảm scope giả thuyết nhưng vẫn phải đủ an toàn và usable trong context được phép.

Project manager cần hỏi artifact này được tạo để học điều gì, ai sẽ dùng, exposure là bao nhiêu và exit criterion là gì. “Chúng ta đang làm MVP” không phải lý do để bỏ qua compliance hoặc operational readiness.

## Experiment phải có decision rule

Experiment không chỉ có metric; nó cần rule: result nào làm continue, pivot, stop hoặc collect thêm data.

Nếu team nhìn result sau rồi mới chọn threshold thuận lợi, confirmation bias dễ xảy ra. Pre-defined hypothesis, sample/segment, metric và decision boundary làm learning đáng tin hơn.

Experiment cũng có ethical/governance boundary. Không phải mọi hypothesis được phép test trực tiếp trên customer nếu exposure, consent hoặc safety consequence quá lớn.

## Batch size và queueing

Batch nhỏ làm giảm thời gian từ work start tới feedback. Nhưng nếu team bắt quá nhiều work song song, mỗi item vẫn chờ lâu trong queue. Đây là lý do WIP quan trọng: utilization cao không đồng nghĩa flow tốt.

Một system luôn giữ mọi người 100% bận có thể làm cycle time tăng mạnh vì không còn slack để xử lý variation, review hoặc urgent defect. Adaptive delivery tối ưu flow của value hơn utilization của từng cá nhân.

## Batch size có optimum kinh tế, không phải càng nhỏ càng tốt

Batch nhỏ giảm risk và feedback latency nhưng tăng transaction cost: planning, setup, deployment, review, coordination. Nếu mỗi thay đổi cực nhỏ cần manual compliance gate hai giờ, batch quá nhỏ có thể tạo overhead lớn hơn learning value.

Automation thường làm optimum batch nhỏ hơn bằng cách giảm transaction cost. Đây là lý do CI/CD hoặc automated evidence có impact quản lý chứ không chỉ kỹ thuật.

Câu hỏi đúng là batch nào tối thiểu hóa tổng cost của waiting, rework và transaction—not “sprint càng ngắn càng agile”.

## Iteration, flow và Kanban

Iteration-based approach timebox work; flow-based approach giới hạn WIP và kéo work theo capacity. Kanban chú trọng visualize workflow, WIP limit, manage flow và improve system. Scrum tạo role/event/artifact framework rõ hơn. Không cần biến đây thành tranh luận brand; chọn mechanism theo problem.

WIP limit giúp expose bottleneck. Nếu team cứ bắt đầu task mới khi testing queue đầy, total utilization nhìn cao nhưng cycle time và feedback latency tăng.

Kanban board chỉ có giá trị nếu column phản ánh real workflow state. Một board đẹp nhưng work thực vẫn chạy ngoài hệ thống không tạo observability.

## Class of service và expedite risk

Không phải mọi work có cùng urgency. Một production incident, fixed-date regulatory item và normal feature có thể cần service policy khác.

Nhưng expedite lane không miễn phí. Nếu quá nhiều item được gọi urgent, normal flow bị phá và priority system mất meaning. Team nên định nghĩa tiêu chí expedite và theo dõi cost mà urgent work gây cho queue khác.

## Scrum events như control loops

Sprint Planning tạo near-term commitment dựa trên objective và capacity. Daily Scrum giúp team inspect progress toward Sprint Goal và điều chỉnh coordination. Sprint Review lấy stakeholder feedback trên increment. Retrospective inspect cách làm việc và chọn improvement.

Nếu biến Daily Scrum thành status report cho manager, hoặc Sprint Review thành demo ceremonial không ảnh hưởng backlog, event mất control-loop function. Khi học framework, nên luôn hỏi event này làm giảm loại uncertainty nào.

## Estimation và forecasting trong adaptive context

Velocity là empirical planning signal của một team, không phải performance KPI. Throughput và cycle-time distribution có thể tạo probabilistic forecast, ví dụ “85% item tương tự hoàn thành trong 8 ngày”. Forecast nên dùng historical evidence và được update khi system thay đổi.

So sánh velocity giữa hai team dễ gây gaming vì story point không có unit chuẩn xuyên team. Khi metric trở thành target, behavior thường thay đổi để tối ưu metric thay vì outcome.

Forecast tốt nên nói bằng range và confidence thay vì một ngày duy nhất khi uncertainty cao.

## Story point là relative model, không phải giờ được mã hóa

Story point thường được dùng để biểu diễn tương đối size/complexity/uncertainty trong một team. Nếu organization quy định “1 point = 8 giờ”, point mất vai trò relative signal và trở thành time estimate vòng vo.

Story point cũng không phải measure productivity. Team có thể đổi scale mà capability không đổi. Nếu management thưởng team tăng velocity, incentive tự nhiên là point inflation.

Khi work tương đối đồng nhất và historical data đủ tốt, throughput/cycle time có thể forecast mà không cần point. Khi item size thay đổi lớn, decomposition hoặc class-of-service có thể quan trọng hơn cố tìm một conversion factor thần kỳ.

## Probabilistic forecast và evidence từ flow

Một release gồm 40 item còn lại không nên được forecast chỉ bằng `40 / average velocity` nếu throughput biến động mạnh. Historical throughput distribution có thể được sample nhiều lần để tạo range finish hoặc xác suất hoàn thành trước target date. Đây là cùng mental model probabilistic reasoning đã dùng ở [Risk & Uncertainty](./08_risk_uncertainty_issues_and_decisions.md) và [Quantitative Reasoning](./15_quantitative_reasoning_worked_examples.md).

Forecast chỉ đáng tin khi work system đủ tương đồng với historical window. Nếu team vừa thay architecture, thêm ba người mới hoặc đổi Definition of Done, dữ liệu cũ cần được discount hoặc phân đoạn.

Điểm quan trọng không phải dùng tool Monte Carlo cho mọi sprint; điểm quan trọng là tránh biến average thành certainty.

## Forecast calibration

Adaptive forecast nên được đánh giá bằng calibration theo thời gian. Nếu team nói “85% confidence” nhưng chỉ đạt target khoảng 50% số lần, model hoặc input chưa calibrated.

Calibration tốt hơn việc ép team cho một date “chắc chắn”. Nó khuyến khích range honest và learning từ forecast miss.

Forecast miss cũng cần phân loại: scope inflow, blocked dependency, throughput shift hay model assumption sai. Chỉ cập nhật average mà không hiểu cause dễ lặp lại error.

## Adaptive planning across horizons

Vision/roadmap định hướng outcome dài hơn. Release planning nối outcome với increment/milestone. Iteration planning chọn work gần. Daily coordination xử lý flow. Retrospective cải thiện system. Mỗi horizon có mức detail khác nhau.

Đây là rolling-wave planning dưới dạng adaptive: commitment gần mạnh hơn; option xa linh hoạt hơn.

Roadmap không nên bị biến thành fixed scope schedule dài hạn nếu môi trường còn nhiều uncertainty. Nó có thể giữ outcome, strategic sequence và major constraint trong khi detail thay đổi theo evidence.

## Decision horizon khác delivery horizon

Team có thể chỉ plan task chi tiết hai tuần nhưng vẫn phải quyết architecture, vendor hoặc regulatory path nhiều tháng trước. Không phải mọi decision có thể postpone tới sprint gần nhất.

Adaptive planning cần identify decision có long lead time hoặc high irreversibility và tạo evidence sớm. “Không plan xa” là hiểu sai agility; đúng hơn là không commit detail xa hơn information quality cho phép, trong khi vẫn quản lý future constraint.

## Change trong adaptive environment không có nghĩa “không cần control”

Backlog reprioritization trong authority của Product Owner có thể không cần formal change request cho từng item. Nhưng thay budget, regulatory commitment, contract scope, architecture boundary hoặc milestone đã được governance phê duyệt có thể vẫn cần change mechanism chính thức.

Vì vậy câu “Agile không có change control” là sai. Adaptive delivery chuyển một phần change decision vào frequent planning loop, nhưng governance boundary vẫn tồn tại. Tailoring tốt định nghĩa rõ change nào là normal backlog management và change nào vượt authority/tolerance.

Điều này đặc biệt quan trọng trong hybrid project: team có thể đổi sequence hàng ngày nhưng không thể tự thay contractual acceptance hoặc regulatory evidence requirement.

## Adaptive change control là continuous reprioritization có guardrail

Traditional change control thường tạo explicit request/approval vì baseline scope ổn định hơn. Adaptive control dùng backlog ordering, WIP policy, product goal và review cadence để absorb small change liên tục.

Nhưng change vẫn có cost. Nếu stakeholder thêm work nhanh hơn throughput, backlog inflow tăng và lead time dài. Adaptive system cần capacity rule: new item vào có thể đẩy item khác ra hoặc làm forecast thay đổi; không có free scope.

## Discovery và delivery không nên tách tuyệt đối

Discovery tìm hiểu problem, user và solution hypothesis; delivery biến hypothesis đủ tốt thành working increment. Nếu discovery đi trước delivery nhiều tháng, team dễ quay lại big-batch specification. Nếu không có discovery nào, team có thể build rất nhanh thứ không có value.

Dual-track hoặc continuous discovery chỉ có ý nghĩa khi learning được nối vào backlog decision. Discovery artifact không phải mục tiêu; decision quality mới là mục tiêu.

## Technical practice ảnh hưởng trực tiếp khả năng adaptive

Agile về management không đủ nếu technical system làm change rất đắt. Automated test, continuous integration, modular architecture, feature flag và deployment automation thường giảm cost of change và feedback latency.

PMP không cần đi sâu implementation, nhưng project manager phải hiểu một dependency quan trọng: technical debt có thể làm organization “muốn agile” nhưng không thể thay đổi nhanh. Nội dung kỹ thuật sâu hơn nằm ở [Delivery, configuration và operations](../computer_science/09_software_engineering/03_delivery_configuration_and_operations.md) và [Maintenance, evolution và technical debt](../computer_science/09_software_engineering/04_maintenance_evolution_and_technical_debt.md).

## Technical option value và reversibility

Modularity, feature flags, backward-compatible interface và automated rollback không chỉ là engineering elegance. Chúng giữ option đổi hướng với cost thấp hơn.

Khi system architecture làm mọi change cross-cutting, management adaptation bị giới hạn dù process rất agile. Technical reversibility là một phần của project flexibility.

## Hybrid interface là nơi rủi ro tích tụ

Khi adaptive team phụ thuộc predictive vendor hoặc governance gate, interface cần được explicit. Ví dụ sprint team release feature liên tục nhưng regulator chỉ approve theo quarterly batch. Khi đó “done” nội bộ khác “released to customer”. Schedule và status phải phân biệt hai state để không tạo false progress.

Một hybrid design tốt xác định cadence, contract, acceptance, dependency, change mechanism và integration point giữa các mode.

Nếu internal team dùng backlog linh hoạt nhưng vendor contract fixed scope/fixed date, change economics cần được explicit. Mỗi backlog reorder có thể không cost nhiều bên trong nhưng có contract implication bên ngoài.

## Cadence mismatch và synchronization cost

Hai subsystem có cadence khác nhau tạo waiting. Team A integrate daily, vendor B deliver monthly, regulator test quarterly. Flow toàn system bị giới hạn bởi interface chậm nhất nếu work cần qua gate đó.

Giải pháp không nhất thiết làm mọi cadence giống nhau. Có thể dùng stable interface, mock/sandbox, decouple dependency hoặc create pre-validation để giảm waiting.

Hybrid design tốt tối ưu synchronization cost, không chỉ chọn methodology riêng cho từng team.

## Contract và procurement trong adaptive context

Adaptive delivery phù hợp hơn với contract cho phép collaboration, incremental acceptance hoặc capacity-based arrangement khi requirement còn thay đổi. Fixed-price fixed-scope có thể hợp khi scope đủ ổn định, nhưng nếu uncertainty cao nó thường chuyển uncertainty thành negotiation friction hoặc change-order cost.

Không có contract type “agile” tự động. Câu hỏi là incentive có hỗ trợ shared outcome và adaptation hay không.

## Adaptive governance và funding guardrail

Adaptive team cần autonomy bên trong boundary, nhưng autonomy không đồng nghĩa không có budget, risk appetite hay decision threshold. Organization có thể tài trợ theo product/capability horizon, review outcome theo cadence và giữ stop/pivot decision ở portfolio hoặc sponsor level.

Một governance design tốt tách reversible product decision khỏi irreversible investment decision. Team nên tự quyết UI copy hay sequence của backlog item nếu nằm trong guardrail; nhưng tăng funding 40%, thay regulated data processor hoặc bỏ committed market launch có thể cần authority khác.

Nếu steering committee approve từng user story, feedback loop bị nghẹt. Nếu team tự thay strategic commitment mà không governance, organization mất control. Adaptive governance là đặt decision ở level thấp nhất vẫn giữ được accountability.

## Adaptive funding và option-based investment

Funding toàn năm cho một hypothesis chưa kiểm chứng có thể lock capital quá sớm. Incremental funding theo outcome/learning milestone giữ option stop/pivot.

Nhưng funding review quá dày làm team mất continuity và tạo pitch theater. Cadence cần match material uncertainty và investment size.

Adaptive portfolio logic không có nghĩa “mỗi sprint xin tiền”; nó nghĩa commitment tăng cùng evidence.

## Servant leadership và impediment removal

Adaptive team cần autonomy nhưng organization vẫn có impediment: slow procurement, shared environment, policy, cross-team dependency. Leader tạo value bằng cách remove system constraint, facilitate conflict và bảo vệ feedback loop hơn là phân task từng người.

Nếu cùng một blocker xuất hiện nhiều sprint, xử lý từng lần chỉ là workaround. Retrospective nên chuyển issue thành system improvement có owner.

## Autonomy boundary phải đi cùng visibility

Self-management không có nghĩa local team được tối ưu mà downstream không biết. Autonomy có hiệu quả khi objective, constraint, interface và evidence visible.

Team có thể tự quyết implementation nhưng nếu decision làm API contract đổi, blast radius vượt local boundary. Decision right cần match consequence radius.

## Agile không loại bỏ documentation hoặc governance

Regulated agile project vẫn cần evidence. Difference là documentation được tạo đúng thời điểm và tự động hóa nếu có thể. Traceability có thể nối backlog item → code change → test → release approval. Governance objective được giữ, ceremony có thể khác.

Trong software project, cơ chế delivery kỹ thuật sâu hơn nằm ở [Delivery, configuration và operations](../computer_science/09_software_engineering/03_delivery_configuration_and_operations.md). PMP chapter giữ focus ở coordination/value/governance boundary.

## Scaling không chỉ là thêm ceremony

Khi nhiều team cùng làm một product hoặc program, vấn đề chính là dependency, architecture, integration, decision rights và shared outcome. Thêm nhiều layer meeting có thể làm coordination cost tăng mà không giảm coupling.

Trước khi chọn scaling framework, nên hỏi dependency nào thực sự bắt buộc, dependency nào có thể loại bỏ bằng architecture/team boundary, và decision nào cần synchronize. Organization design và system design thường liên quan chặt.

Integration cadence thường quan trọng hơn reporting cadence. Hai team demo tốt riêng lẻ nhưng chỉ integrate cuối quý vẫn mang batch risk lớn. Shared environment, interface contract, version compatibility và cross-team Definition of Done có thể là control mạnh hơn thêm một coordination meeting.

## Scaling law: dependency tăng nhanh hơn team count

Thêm team có thể tăng capacity nhưng cũng tăng interface. Nếu architecture và ownership không rõ, coordination path tăng nhanh và marginal throughput giảm.

Scaling tốt cố giảm dependency trước khi tăng coordination ceremony. Team boundary nên align với value stream/capability đủ độc lập để local decision không liên tục chờ cross-team agreement.

## Adaptive anti-patterns

Sprint waterfall xảy ra khi analysis, dev và test vẫn chạy tuần tự trong cùng sprint. Fake agility xảy ra khi team có ceremony nhưng priority không thể thay. Velocity pressure biến estimate thành performance target. Backlog hoarding tạo hàng nghìn item không còn relevance. “Self-managing” bị dùng như lý do manager không remove organizational blocker.

Một anti-pattern khác là release every sprint nhưng không đo outcome. Delivery nhanh không tự động tạo value nhanh. Một anti-pattern tinh vi hơn là backlog thay đổi liên tục nhưng không có stable product goal; lúc đó team “adaptive” nhưng chỉ phản ứng với noise.

Experiment theater xảy ra khi mọi work được gọi là experiment nhưng result không bao giờ làm roadmap đổi. Hybrid theater xảy ra khi organization cộng tất cả gate và ceremony của cả hai mode mà không bỏ control trùng lặp.

## Ví dụ scenario

Customer liên tục đổi priority nhưng deadline compliance cố định. Câu trả lời không phải “agile nên chấp nhận mọi change” hoặc “deadline cố định nên khóa toàn bộ scope”. Ta giữ compliance outcome/deadline như constraint, ưu tiên backlog theo value và mandatory scope, giảm optional scope khi cần, validate increment thường xuyên và quản lý dependency/gate rõ.

Giả sử integration với regulator chỉ có test window mỗi tháng. Team vẫn có thể làm adaptive bên trong, nhưng integration window là external cadence phải đưa vào planning. Feature nên được integrated/prototyped sớm trước window thay vì chờ sprint cuối. Hybrid ở đây là thiết kế feedback loop quanh một constraint không adaptive.

Một scenario khác: velocity tăng 25% sau khi management đặt KPI “tăng point mỗi sprint”, nhưng escaped defect và cycle time cũng tăng. Kết luận không nên là team productivity tăng. Metric đã trở thành target và behavior thay đổi. PM nên quay lại outcome/flow/quality evidence, bỏ incentive gây gaming và dùng velocity đúng vai trò local planning signal.

Một scenario experimentation: onboarding experiment tăng activation 8% nhưng churn tháng đầu không đổi. Team không nên tự động rollout full feature chỉ vì primary metric tăng. Cần xem hypothesis ban đầu là activation có dẫn tới retention hay không, guardrail metric có xấu đi không và thêm evidence có khả năng đổi decision không.

## Mental model

> Adaptive delivery tối ưu tốc độ học bằng cách giảm batch, rút feedback latency và giữ option; predictive delivery tối ưu coordination/predictability khi commitment sớm có giá trị; hybrid tối ưu interface giữa các logic khác cadence. Agility thật được đo bằng việc evidence có thể thay decision mà không phá governance boundary.

Tiếp theo: [Measurement, status, closure và continuous improvement](./11_measurement_status_closure_and_continuous_improvement.md).