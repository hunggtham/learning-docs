# 11 — Measurement, status, closure và continuous improvement

## Measurement phục vụ decision

Metric có giá trị khi giúp phát hiện state, trend hoặc risk để ai đó ra decision. Số liệu được thu chỉ vì “dashboard phải có” tạo reporting load nhưng không tăng control.

Một metric tốt cần definition, data source, cadence, owner, threshold và action interpretation. Nếu hai team hiểu “completed” khác nhau, tổng percent complete không có meaning.

Điểm quan trọng là measurement không phải objective. Metric là proxy cho một phần reality. Khi proxy trở thành target tuyệt đối, behavior có thể bị méo để tối ưu số thay vì outcome.

## Measurement architecture: metric cũng là một information system

Khi project phụ thuộc nhiều dashboard, metric không nên được xem như con số xuất hiện tự nhiên. Nó có một pipeline:

```text
real event → capture → transform → aggregate → display → interpretation → decision
```

Lỗi ở bất kỳ bước nào đều có thể tạo false confidence. Ticket được đóng nhưng reopen sau đó, timestamp dùng timezone khác, duplicate record hoặc denominator thay đổi đều có thể làm dashboard đúng về query nhưng sai về meaning.

Vì vậy metric quan trọng cần semantic contract: chính xác đang đo event nào, inclusion/exclusion rule, source of truth, latency và cách xử lý missing data. Đây là data governance ở mức project, không chỉ chuyện BI team.

## Measurement error và model error

Hai loại sai khác nhau cần tách. Measurement error xảy ra khi data capture/query không phản ánh event thật. Model error xảy ra khi data đúng nhưng metric được dùng như proxy sai cho objective.

Ví dụ velocity được tính hoàn toàn chính xác nhưng dùng để kết luận productivity giữa hai team là model error. UAT pass rate đúng nhưng test case không đại diện customer journey cũng là model weakness.

Fix dashboard query không sửa metric model; thêm metric mới không sửa source data sai. Diagnosis phải đúng tầng.

## Từ objective tới metric

Một chuỗi reasoning tốt là:

```text
objective → observable outcome → indicator → threshold → decision/action
```

Nếu objective là giảm thời gian onboarding, metric phù hợp có thể là median time-to-complete hoặc abandonment rate. Số story point hoàn thành không trực tiếp chứng minh objective này.

Metric nên được chọn từ câu hỏi quản trị. “Ta cần biết điều gì để quyết định?” tốt hơn “dashboard thường có chỉ số nào?”.

## Proxy distance

Metric càng xa objective, càng dễ bị misinterpreted. Ticket closed là proxy xa customer outcome hơn resolution accepted; training attendance xa adoption hơn actual process usage.

Proxy xa vẫn hữu ích nếu leading và cheap, nhưng cần biết causal link nào đang được giả định. Khi link yếu, metric phải được kết hợp với evidence khác.

Một dashboard tốt không chỉ chứa nhiều number; nó giữ chain từ operational signal tới outcome đủ rõ để reader không nhầm activity với value.

## Leading và lagging indicators

Lagging indicator phản ánh outcome đã xảy ra, như defect escaped production hoặc budget variance. Leading indicator báo trước risk, như test queue tăng, critical dependency chưa resolved hoặc requirement churn cao.

Không có leading metric hoàn hảo. Mục tiêu là tạo early signal đủ tốt để kiểm tra thêm trước khi lagging failure xảy ra.

Một metric có thể leading cho objective này nhưng lagging cho objective khác. Cycle time tăng là lagging signal của workflow congestion đã xảy ra, nhưng có thể là leading signal cho missed release date.

## False positive và false negative

Leading indicator tạo trade-off. Threshold quá nhạy tạo nhiều false alarm, làm team mệt và mất trust. Threshold quá rộng bỏ lỡ problem cho tới khi lagging outcome xấu xuất hiện.

Measurement design phải cân cost của false positive và false negative. Privacy/security control có thể chấp nhận nhiều alert dư hơn low-impact internal workflow vì cost bỏ sót cao hơn.

Threshold vì vậy là risk decision, không chỉ statistical tuning.

## Baseline, actual và forecast

Baseline là reference đã được phê duyệt. Actual cho biết điều đã xảy ra. Forecast ước lượng điều có khả năng xảy ra tiếp theo dựa trên current evidence.

Ba lớp này không nên trộn. Nếu forecast xấu, không được sửa baseline chỉ để dashboard đẹp. Nếu scope hoặc strategy đã formally đổi, giữ baseline cũ mãi cũng mất ý nghĩa. Rebaseline phải là governance decision có rationale, không phải cosmetic action.

## Forecast calibration: dự báo tốt không chỉ là “gần đúng một lần”

Một forecast có thể nhìn chính xác do may mắn. Calibration hỏi prediction có đáng tin qua nhiều lần hay không. Nếu team thường nói “80% confidence” nhưng chỉ đúng khoảng một nửa số lần, confidence language đang overconfident.

Không cần hệ thống thống kê phức tạp để bắt đầu. Có thể lưu forecast theo status date, range/confidence, actual outcome và reason variance. Sau vài milestone, team sẽ thấy estimate nào thường bias, dependency nào gây tail và context nào làm historical model mất hiệu lực.

Forecast nên được versioned thay vì overwrite. Nếu mỗi tuần chỉ giữ con số forecast mới nhất, organization mất evidence về forecast quality và không học được từ bias.

## Forecast stability và forecast responsiveness

Forecast quá ổn định có thể là dấu hiệu không absorb evidence; forecast thay mỗi ngày có thể là noise chasing. Một model tốt đủ responsive với material signal nhưng không react quá mạnh với random fluctuation.

Đây là trade-off giống control system: update quá chậm tạo lag; update quá nhanh với noise tạo oscillation. Cadence nên match tốc độ system thay đổi và cost của decision.

## Status không phải màu

Red/amber/green có thể hữu ích nhưng dễ che uncertainty. Một status report mạnh thường nối objective/milestone với current evidence, trend, forecast, key risk/issue, decision needed và confidence.

Project “green” nhưng không có evidence cho adoption hoặc integration readiness có thể chỉ đang đo task completion. Status phải phản ánh success model, không chỉ activity.

Một report hữu ích thường trả lời bốn câu: ta đang ở đâu so với objective, điều gì thay đổi từ lần trước, nếu không làm gì thì forecast là gì, và decision nào cần ai đưa ra khi nào.

## Status narrative phải giải thích causal story

Hai project cùng `amber` có thể cần decision hoàn toàn khác. Một project amber vì known vendor delay có contingency; project khác amber vì requirement ambiguity chưa có owner.

Status nên giải thích driver, not just label. Trend và causal story giúp governance biết liệu cần thêm resource, decision, risk acceptance hay chỉ tiếp tục monitor.

Color without story dễ biến governance thành reaction to formatting.

## Confidence và uncertainty trong reporting

Một ngày forecast duy nhất dễ tạo false precision. Khi uncertainty cao, range hoặc confidence statement trung thực hơn. Ví dụ “P80 hoàn thành trước 30/11” chứa information khác hoàn toàn “deadline 30/11”.

PM không cần biến mọi report thành thống kê nâng cao, nhưng nên tránh trình bày estimate như fact. Confidence phải thay đổi khi evidence thay đổi.

Nếu uncertainty tăng nhưng report vẫn giữ cùng một màu xanh chỉ vì target date chưa chính thức trượt, status system đang phản ứng quá muộn.

## Percent complete đặc biệt dễ gây ảo giác

Một task “90% complete” không nói rõ 10% còn lại là documentation dễ làm hay integration unknown có thể kéo dài ba tuần. Percent complete càng chủ quan khi work chưa có objective completion criterion.

Deliverable-based evidence thường tốt hơn subjective completion percentage: requirement accepted, environment ready, interface integrated, test passed, regulatory evidence approved. Với adaptive work, usable increment hoặc flow state có thể informative hơn phần trăm.

Nếu bắt buộc dùng percent complete, definition và earning rule phải nhất quán; nếu không metric dễ tăng đều cho đến 90% rồi đứng yên rất lâu.

## Metric portfolio thay vì single metric

Một metric duy nhất dễ bị tối ưu cục bộ. Throughput nên đi với cycle time/quality; adoption nên đi với support/error; cost efficiency nên đi với outcome/risk.

Metric portfolio không có nghĩa dashboard 50 KPI. Chỉ cần đủ counter-signal để metric chính không che side effect.

Một pattern tốt là outcome metric + flow/leading metric + risk/quality guardrail. Cấu trúc cụ thể tùy objective.

## Variance → diagnosis → response

Khi variance xuất hiện, trình tự tốt là xác nhận data, tìm cause, đánh giá impact, xem threshold/authority, chọn response, update forecast và communicate. Jump ngay từ “delay” sang “overtime” có thể giải quyết symptom và tăng quality risk.

Variance analysis nên tách common-cause variation khỏi special-cause signal khi phù hợp. Một team có cycle time dao động tự nhiên 3–5 ngày không nên bị escalated vì một item mất 5 ngày. Nhưng queue tăng liên tục ba tuần có thể là system change cần investigation.

## Threshold và action rule phải tồn tại trước crisis

Metric không tạo control nếu không ai biết khi nào phải action. Threshold có thể là hard boundary như regulatory tolerance hoặc soft trigger như “cycle time P85 tăng hơn 20% trong ba tuần”.

Threshold tốt không tự động hóa mọi decision; nó kích hoạt review thích hợp. Nếu threshold bị vượt nhưng response phụ thuộc context, playbook có thể nói ai review, evidence nào cần và authority nào quyết.

Nếu threshold chỉ được định nghĩa sau khi problem xảy ra, organization dễ chọn rule thuận tiện để giải thích outcome thay vì rule giúp kiểm soát trước đó.

## Threshold hysteresis và alert flapping

Nếu metric dao động quanh một threshold, status có thể nhảy green/amber liên tục. Điều này tạo noise và overreaction.

Một số system cần hysteresis: trigger action khi vượt boundary đủ lâu hoặc quay về normal khi evidence phục hồi đủ rõ. Không phải mọi metric cần kỹ thuật này, nhưng mental model hữu ích: control state không nên flip vì một data point random.

## Vanity metric và Goodhart effect

Vanity metric trông tích cực nhưng không hỗ trợ decision, như số meeting, số page tài liệu hoặc số ticket đóng mà không có context. Goodhart effect xuất hiện khi metric trở thành target và người ta tối ưu cách tính metric.

Nếu velocity trở thành KPI cá nhân/team, story point có thể phình ra. Nếu defect count thấp được thưởng, team có incentive redefine defect. Control tốt cần metric portfolio thay vì một số đơn lẻ và cần audit semantic definition.

## Measurement cần denominator và context

“Có 20 defect” ít information nếu không biết release size, severity, detection stage hoặc trend. “Cost tăng 10%” cần biết baseline quality và scope change. Relative measure thường cần denominator để tránh kết luận sai.

Metric cũng cần segmentation. Average có thể che tail. User onboarding trung bình 3 phút nhưng 10% user mất 20 phút có thể là problem lớn nếu nhóm đó là customer chiến lược.

## Aggregation loss

Khi metric được aggregate từ team → program → executive, detail bị mất. Average schedule status có thể che một dependency red quyết định toàn outcome.

Aggregation nên preserve exception material. Executive không cần mọi task, nhưng cần biết tail/threshold breach và uncertainty quan trọng.

Nếu summary luôn làm data “mượt hơn”, governance có compression bias.

## Decision latency như một metric hệ thống

Project có thể delivery chậm không phải vì team làm chậm mà vì decision chậm. Thời gian từ khi issue được nêu đến khi authority ra quyết định là decision latency.

Đo decision latency đặc biệt hữu ích trong matrix/hybrid organization. Nếu mọi blocker chờ steering committee hai tuần, thêm developer không giải quyết throughput.

Có thể tách decision latency thành waiting-for-information, waiting-for-authority và rework-after-decision. Ba phần này dẫn đến intervention khác nhau.

## Information latency và action latency

Measurement có thể đúng nhưng đến quá muộn. Information latency là thời gian từ event xảy ra đến evidence available. Action latency là thời gian từ evidence tới intervention.

End-to-end control latency = information latency + decision latency + action latency. Đây là metric mạnh để hiểu vì sao organization “biết vấn đề nhưng vẫn phản ứng chậm”.

Automation có thể giảm capture latency; delegation giảm decision latency; pre-approved playbook giảm action latency.

## Benefit measurement và vấn đề attribution

Sau go-live, outcome cải thiện không tự động chứng minh project gây ra toàn bộ improvement. Market thay đổi, seasonal effect, policy khác hoặc campaign marketing có thể cùng tác động. Đây là vấn đề attribution.

Trong nhiều project không thể làm experiment hoàn hảo, nhưng vẫn có thể reasoning tốt hơn bằng baseline, comparison cohort nếu có, pre/post trend và assumption rõ. Claim “automation giảm cost 30%” mạnh hơn nếu biết volume, staffing policy và demand không đổi đáng kể; nếu tất cả cùng thay, conclusion cần thận trọng hơn.

Benefit owner nên phân biệt measurement với causal claim. Đo được KPI tăng là một chuyện; chứng minh investment tạo phần tăng đó là chuyện khác.

## Benefit decay và unintended consequence

Benefit có thể giảm theo thời gian vì user behavior, competitor response, maintenance cost hoặc process drift. Vì vậy measurement chỉ tại go-live + 1 tháng có thể quá sớm.

Outcome tốt cũng có side effect: automation giảm handling time nhưng complaint tăng; self-service giảm contact center volume nhưng chuyển complex case sang specialist, làm average handling time phần còn lại tăng.

Benefit measurement cần guardrail và time horizon, không chỉ headline KPI.

## Lessons learned như knowledge loop

Lessons learned không nên chỉ viết lúc close. Nếu insight có thể giúp project hiện tại, nên capture và áp dụng ngay. Retrospective, incident review và milestone review đều là learning loop.

Một “lesson” hữu ích không chỉ kể chuyện; nó nêu context, signal, cause/contributing factor, action và điều kiện áp dụng. Organizational Process Assets chỉ có giá trị nếu người sau tìm và dùng được.

“Vendor communication cần tốt hơn” không phải lesson đủ actionable. “API schema change không có versioning làm UAT rework; project sau cần contract yêu cầu notice period và backward compatibility” có context và mechanism rõ hơn.

## Knowledge retention và retrieval

Lesson tồn tại nhưng không được tìm thấy thì organizational learning bằng zero. Learning system cần taxonomy/search, owner hoặc integration vào template/checklist nơi relevant.

Một lesson có expiry/context. Practice tốt cho monolith 2018 có thể không phù hợp cloud-native 2026. Reuse cần relevance check, không copy blind.

Knowledge loop hoàn chỉnh là capture → abstract mechanism → store → retrieve → apply → update.

## Retrospective và post-mortem khác blame session

Mục tiêu của review là tăng system capability, không tìm người để quy trách nhiệm. Accountability vẫn cần, nhưng blame làm information bị che ở lần sau.

Một review trưởng thành tách event timeline, contributing condition, control đã fail, decision context và corrective action. Action nên có owner và verification, nếu không lesson chỉ là narrative.

## Action item closure phải kiểm tra effectiveness

Post-mortem action “thêm checklist” không nên được coi là done chỉ vì checklist đã publish. Cần evidence rằng control mới được dùng và failure pattern giảm.

Otherwise organization tích corrective-action inventory nhưng system capability không thay đổi.

## Closure là chuyển responsibility, không chỉ đóng ticket

Project closure (đóng dự án / 프로젝트 종료) xác nhận acceptance, xử lý obligation, chuyển giao deliverable/knowledge, đóng contract/finance, release resource, archive evidence và ghi learning. Với project bị terminate sớm, closure vẫn cần diễn ra để bảo toàn knowledge, legal/financial obligation và asset.

Transition readiness quan trọng hơn một chữ ký hình thức. Operations phải có monitoring, runbook, access, training, support model, rollback/recovery và ownership phù hợp với type of deliverable.

Closure nên xác định rõ open item nào được chuyển sang operation, product backlog hoặc separate project. “Đóng project” không được biến unfinished responsibility thành orphan work.

## Closure là risk transfer event

Khi project team giải tán, residual risk không biến mất; nó chuyển sang product/operations/business owner. Transfer chỉ thật khi receiving owner hiểu exposure, có authority/capacity và chấp nhận nó.

Một open defect list được gửi email không phải risk transfer nếu operations không biết severity hoặc không có budget xử lý.

Closure package nên làm residual risk, warranty/support window, unresolved claim và dependency visible.

## Operational readiness phải được chứng minh bằng evidence

Một handover meeting không chứng minh operation sẵn sàng. Readiness có thể cần evidence như support ownership đã nhận, access được test, monitoring alert tới đúng người, backup/restore hoặc rollback được diễn tập, unresolved defect được risk-accepted và supplier support channel hoạt động.

Các tiêu chí này nên được định nghĩa trước go-live, không phải sáng tạo vào ngày closure. Khi readiness là gate, cần phân biệt mandatory criterion với desirable criterion để tránh vừa block vô lý vừa waive mọi thứ dưới áp lực deadline.

Nếu operation chỉ ký acceptance vì project team sắp giải tán, administrative closure đã lấn át risk transfer.

## Legacy decommission cũng là một phần của transition

New system go-live nhưng old system sống vô hạn tạo duplicate process, cost, data inconsistency và security exposure.

Decommission cần retention/archive, data reconciliation, user migration, contract/license closure, access revoke và fallback decision. Có thể giữ parallel run có chủ đích trong stabilization, nhưng phải có exit criterion.

Project scope bỏ decommission thường chỉ chuyển hidden cost sang operations.

## Acceptance không đồng nghĩa benefit realization

Customer hoặc sponsor có thể accept deliverable vì nó đáp ứng agreed criteria, nhưng benefit vẫn chưa xuất hiện. Một hệ thống có thể pass UAT nhưng adoption thấp. Vì vậy acceptance chứng minh output đủ chuẩn; benefits tracking chứng minh outcome/value.

Hai khái niệm này cần owner khác nhau trong nhiều organization.

## Benefit realization có thể sống sau project

Một project kết thúc không đồng nghĩa benefit đã xuất hiện. Ví dụ hệ thống tự động hóa go-live tháng 12 nhưng cost saving chỉ đo rõ sau sáu tháng. Benefit owner và measurement plan phải tiếp tục sau closure nếu cần.

Điều này nối project management với product/operations/portfolio governance: project bàn giao capability, organization tiếp tục khai thác value.

Benefit metric nên có baseline trước project nếu có thể. Nếu không biết trạng thái trước, rất khó chứng minh change sau project thực sự đến từ investment.

## Premature closure và endless project

Premature closure xảy ra khi administrative deadline quan trọng hơn readiness, khiến operation nhận system chưa ổn. Ngược lại, project kéo dài vô tận khi mọi enhancement sau go-live đều được giữ trong project thay vì chuyển product/operations ownership.

Closure boundary cần được định nghĩa từ charter/lifecycle: deliverable nào thuộc temporary project, ongoing improvement nào thuộc operation hoặc product lifecycle.

## Continuous improvement

Continuous improvement (cải tiến liên tục / 지속적 개선) dùng feedback để thay process, capability hoặc environment. Cải tiến không nhất thiết là project lớn; nhiều thay đổi nhỏ có compounding effect.

Tuy nhiên thay process liên tục cũng có cost. Một experiment cải tiến nên có hypothesis và signal: “giới hạn WIP từ 10 xuống 6 có giảm cycle time mà không làm throughput giảm đáng kể không?”. Như vậy retrospective trở thành learning system thay vì meeting cảm tính.

Improvement cần ổn định đủ lâu để đo. Nếu team đổi process mỗi tuần, khó phân biệt effect của thay đổi nào.

## Improvement WIP và change fatigue

Team cũng có thể overcommit improvement. Mười action từ retrospective nhưng không ai có capacity chỉ tạo guilt và stale backlog.

Giới hạn số improvement active giúp learning loop hoàn tất. Chọn leverage point cao, verify effect, rồi mới thêm change khác.

Continuous improvement không có nghĩa continuous disturbance.

## Control chart và process stability ở mức mental model

Không cần biến PMP thành khóa statistics, nhưng nên hiểu distinction giữa variation bình thường và signal bất thường. Nếu process stable, phản ứng mạnh với từng fluctuation có thể làm system tệ hơn. Nếu pattern thay đổi rõ, cần investigate special cause.

Mental model này giúp tránh management by anecdote: một incident đơn lẻ không luôn chứng minh process hỏng, nhưng trend và repeated signal cần action.

## Metric cũng cần lifecycle và retirement

Một metric hữu ích ở discovery có thể vô nghĩa ở operations. Risk count quan trọng lúc uncertainty cao nhưng sau stabilization có thể nhường chỗ cho service reliability. Nếu dashboard chỉ thêm metric mà không retire metric cũ, attention bị phân tán và reporting cost tăng.

Mỗi metric quan trọng nên có review point: nó còn giúp decision nào, owner còn dùng không, definition còn phù hợp không và collection cost có xứng đáng không. Measurement system cũng cần continuous improvement.

## Software operations connection

Khi deliverable là software, go-live chỉ bắt đầu một lifecycle mới. Xem [Delivery, configuration và operations](../computer_science/09_software_engineering/03_delivery_configuration_and_operations.md) và [Maintenance, evolution và technical debt](../computer_science/09_software_engineering/04_maintenance_evolution_and_technical_debt.md) để hiểu sâu production transition và long-term evolution.

## Ví dụ reasoning

Một project báo 95% task complete nhưng UAT pass rate chỉ 55% và defect reopen tăng. Nếu chỉ nhìn percent complete, status có vẻ gần xong. Nhưng evidence về usable outcome cho thấy project còn uncertainty lớn. PM nên chuyển focus sang quality/integration bottleneck, update forecast và tránh tuyên bố gần hoàn tất chỉ vì planned tasks đã được bắt đầu hoặc code-complete.

Một project khác hoàn thành đúng budget nhưng adoption sau ba tháng chỉ 20%. Project delivery có thể đã đạt constraint nhưng business outcome chưa đạt. Benefits owner cần investigate training, process fit, incentive hoặc product usability thay vì coi closure administrative là success cuối cùng.

Một forecast release được báo “P80 trước 15/12” suốt bốn lần nhưng actual liên tục muộn hơn P80. Vấn đề không chỉ là lần dự báo hiện tại sai; forecasting model hoặc assumption đang understate uncertainty. Team cần review calibration, shared dependency/correlation và historical window trước khi tiếp tục dùng cùng confidence label.

Một scenario measurement: throughput tăng 20% sau automation nhưng escaped defect cũng tăng 40%. Nếu management chỉ nhìn throughput, improvement có vẻ thành công. Metric portfolio cho thấy system đang đổi quality lấy speed; team cần tìm optimum chứ không tiếp tục tối đa một proxy.

## Mental model

> Measurement là sensor system: nó phải đo đúng reality đủ sớm, giữ semantic ổn định và kích hoạt action phù hợp. Closure là event chuyển ownership và residual risk; continuous improvement chỉ hoàn tất khi action được kiểm chứng thành capability mới, không phải khi retrospective kết thúc.

Tiếp theo: [AI, sustainability và bối cảnh dự án hiện đại](./12_ai_sustainability_and_modern_project_context.md).