# 16 — End-to-end case studies: predictive, adaptive và hybrid

Các case dưới đây cố ý đi xuyên nhiều domain để tránh thói quen học từng knowledge area độc lập. Mỗi case bắt đầu bằng context, sau đó theo chuỗi decision, trade-off, evidence và failure mode. Mục tiêu không phải tìm một “đáp án chuẩn” duy nhất mà luyện cách đổi decision khi context đổi.

Khi đọc, đừng chỉ hỏi “PM nên làm gì?”. Hãy giữ một state model gồm objective, delivery mode, constraint, authority, assumption, current evidence và next irreversible decision. Khi một signal mới xuất hiện, quan sát nó lan sang domain nào thay vì gắn nhãn ngay là “risk question”, “schedule question” hay “stakeholder question”.

## Case A — Predictive: mở trung tâm dữ liệu dự phòng

### Context

Một công ty tài chính phải mở disaster-recovery site trước deadline regulatory. Location và capacity đã được phê duyệt, construction/equipment có lead time dài, acceptance cần test failover. Requirement phần cứng tương đối ổn định; change muộn rất đắt.

### Chọn approach

Predictive là logic chính vì physical dependency, procurement lead time và compliance gate tạo strong sequencing. Điều này không cấm iteration ở subcomponent, nhưng overall milestones và baseline có giá trị coordination cao.

### Từ value tới scope

Outcome không phải “xây xong site” mà là business service có khả năng failover trong RTO/RPO yêu cầu. Vì thế scope phải gồm network, data replication, runbook, test, training và regulatory evidence; nếu chỉ WBS construction thì output không đạt outcome.

### Integrated planning

Charter nên làm rõ regulatory objective, sponsor, deadline, authority và success criteria. WBS tách facility, power, network, replication, security, test và operational readiness, nhưng integrated schedule phải giữ dependency giữa chúng.

Nếu generator tới đúng hạn nhưng network circuit chưa được carrier provision, facility completion không tạo usable outcome. Đây là integration problem chứ không chỉ schedule problem.

### Schedule và procurement

Long-lead generator và network equipment có thể nằm trên critical path. Procurement strategy cần contract acceptance, delivery milestone và supplier risk. Nếu vendor delay, PM kiểm tra critical-path impact, contract right, alternative supplier và contingency thay vì chỉ yêu cầu overtime.

Suppose generator có 8 tuần lead time và float gần zero, còn office furniture có 4 tuần float. Procurement team không nên ưu tiên hai package theo cùng urgency chỉ vì cả hai “đang trễ”.

### Risk và reserve

Risk register có thể gồm permit delay, supply-chain disruption, failover defect, power-load issue và regulator scheduling. Contingency reserve nên gắn với identified uncertainty thay vì padding ngầm trong từng package.

Nếu supply-chain disruption có probability thấp nhưng impact regulatory rất lớn, threat response có thể là second supplier hoặc early order dù expected cost tăng.

### Quality/compliance

Quality evidence là failover test và service criteria, không chỉ visual inspection facility. Compliance gate phải được đưa vào plan sớm; regulator approval không thể “test cuối rồi sửa”.

Requirement traceability nối regulation → design control → test case → evidence package. Nếu control evidence không traceable, project có thể technically ready nhưng chưa governance-ready.

### Change scenario

Business muốn thêm extra analytics environment trong site vì “đang xây rồi thì làm luôn”. Technical work có vẻ nhỏ nhưng có thể tăng power, network, security scope và delay approval.

Đây là scope change cần impact analysis. Nếu analytics không liên quan regulatory outcome và threaten deadline, decision có thể defer sang project khác thay vì gold plating.

### Closure

Closure chỉ xảy ra khi operations có ownership, runbook/access/monitoring, DR drill được chấp nhận, contract/financials đóng và evidence archived. Benefit—resilience/compliance—sống trong operations sau project.

### Failure mode nếu quản lý theo task

Mọi construction task có thể “green” nhưng failover rehearsal thất bại vì application dependency chưa được map. Đây là ví dụ local completion không bằng system readiness.

## Case B — Adaptive: xây sản phẩm mobile mới trong thị trường chưa chắc chắn

### Context

Startup biết customer problem nhưng chưa biết feature set nào tạo retention. Technical platform đủ linh hoạt để ship increment hàng tuần. Deadline không regulatory; runway là constraint chính.

### Chọn approach

Adaptive delivery tối ưu learning. Roadmap nên định nghĩa outcome/hypothesis, còn backlog giữ option. Việc lập một WBS chi tiết 12 tháng sẽ tạo false precision.

### Business hypothesis

Giả thuyết ban đầu là user bỏ service vì onboarding quá khó. Outcome target không phải “ship 20 feature” mà là tăng activation và retention với runway hữu hạn.

Điều này ảnh hưởng priority: analytics instrumentation có thể được làm sớm dù customer không thấy vì nó tạo evidence cho hypothesis.

### Value-based delivery

Team bắt đầu với onboarding + core action nhỏ nhất để đo activation. Mỗi increment có Definition of Done và telemetry. Feature request được ưu tiên theo customer evidence, strategic fit, risk, dependency và learning value chứ không theo người nói to nhất.

### Discovery failure

Customer interview nói họ muốn social feature, nhưng prototype cho thấy feature gần như không ảnh hưởng retention. Team không nên tiếp tục chỉ vì đã đưa social feature vào roadmap slide.

Adaptive governance cho phép bỏ option khi evidence thay đổi. Sunk effort trong discovery không phải lý do build full feature.

### Metric trap

Nếu team chỉ tối ưu velocity, story point có thể tăng nhưng retention không đổi. Project/product leadership phải nối delivery metric với outcome metric. Flow metric giúp delivery; product metric giúp business learning.

Nếu activation tăng nhưng support ticket và refund cũng tăng, team cần mở boundary measurement thay vì tuyên bố success từ một metric.

### Schedule và forecasting

Release forecast có thể dựa trên throughput/cycle-time distribution thay vì detailed long-range task estimate. Khi WIP tăng, cycle time tăng dù velocity gần như giữ nguyên, team cần inspect flow trước khi thêm người.

### Risk

Risk lớn nhất có thể là market risk chứ không technical risk. Response tốt là experiment sớm, không phải thêm buffer schedule. Một prototype có thể “thất bại” về feature nhưng thành công vì loại bỏ assumption sai.

Technical risk vẫn tồn tại. Nếu payment integration chưa được thử với production-like load, spike sớm có information value cao hơn polish UI.

### Governance

Adaptive không nghĩa không governance. Runway/budget threshold, privacy/security và brand risk vẫn có guardrail. Decision reversible được team tự chủ; high-impact policy decision escalate.

### Closure hoặc transition

Nếu initiative chứng minh product-market signal, temporary project mode có thể chuyển sang long-lived product team. Nếu hypothesis fail, closure có thể là stop investment và preserve learning thay vì “ship cho xong vì đã làm nhiều”.

### Failure mode nếu hiểu Agile như ceremony

Team chạy sprint, daily và retrospective nhưng founder khóa roadmap sáu tháng và mọi request đều “must-have”. Feedback không thay decision; system chỉ có ceremony, không có adaptation.

## Case C — Hybrid: ngân hàng triển khai eKYC với external vendor

### Context

Ngân hàng có deadline business, privacy/security policy, vendor OCR/face matching, integration với backend cũ và UX cần được test với user. Một số external interface và UAT gate cố định; UX/flow còn uncertainty.

### Decompose theo uncertainty

Compliance requirement, data retention, vendor contract và production cutover cần control mạnh. UX và error-flow có thể iterative. Hybrid được thiết kế từ boundary này thay vì trộn ceremony tùy ý.

### Stakeholder map

Sponsor quan tâm deadline/adoption; compliance quan tâm lawful processing; security quan tâm attack/data exposure; operations quan tâm supportability; vendor quan tâm contract boundary; user quan tâm friction/privacy. Communication phải tailor theo decision need.

### Early risk reduction

Thay vì chờ full integration rồi UAT, team prototype API, test representative ID-card images, đo accuracy theo segment và xác nhận failure fallback. Đây là mua information sớm để giảm rework.

### Procurement interface

Vendor contract fixed một số SLA/API obligation, nhưng UX backlog adaptive. Nếu UX change làm API volume tăng gấp ba, product decision có thể chạm commercial term dù “chỉ đổi flow”. Hybrid interface phải nối backlog change với vendor impact analysis.

### Schedule interface

Team có sprint hai tuần nhưng bank UAT window chỉ mở hàng tháng. Internal Definition of Done không đồng nghĩa external acceptance. Plan cần state rõ: code complete, integrated, UAT accepted và production ready là các trạng thái khác nhau.

### Change scenario

Giữa UAT, regulator yêu cầu thêm consent wording và retention evidence. Đây không chỉ là “UI text change”. PM đánh giá requirement/compliance impact, vendor/data lifecycle, test evidence, schedule và approval. Mandatory compliance scope được ưu tiên; optional feature có thể bị đẩy sau go-live để bảo vệ deadline.

### Incident trước go-live

Load test phát hiện face-matching timeout ở peak. PM không nên chỉ yêu cầu “optimize code”. Team cần xác định bottleneck phía vendor/network/application, business impact, SLA, capacity option, degradation/fallback và go-live threshold. Nếu failure vượt risk tolerance, governance quyết định go/no-go dựa evidence.

### AI/model-quality scenario

OCR accuracy trung bình 98% nhưng giấy tờ cũ của một nhóm customer chỉ 85%. Average metric che segment risk. Team cần phân loại impact, manual fallback, business volume và fairness/customer friction trước khi quyết rollout.

Nếu nhóm đó chỉ 1% volume và manual fallback xử lý được, response khác trường hợp nhóm đó chiếm 30% user hoặc regulation yêu cầu equal treatment.

### Transition

Operations cần dashboard, alert, vendor escalation, manual fallback, privacy incident procedure và knowledge transfer. Project closure không thể chỉ dựa vào UAT sign-off nếu support model chưa sẵn sàng.

### Failure mode nếu hybrid chỉ là tên

Nếu team vừa giữ full upfront specification, vừa có sprint ceremony, vừa phải submit mọi backlog reorder cho CCB, overhead tăng mà feedback không nhanh hơn. Hybrid tốt chọn mechanism theo constraint; hybrid xấu cộng tất cả ceremony.

## Case D — Troubled project recovery: ERP rollout đang đỏ

### Context

Một ERP transformation 18 tháng đã dùng 70% budget. Integration test trễ hai tháng, business unit liên tục thêm requirement, vendor blame internal data quality, sponsor vẫn yêu cầu original go-live vì đã công bố với board.

### Bước đầu không phải lập recovery plan ngay

PM mới vào không nên lập tức yêu cầu overtime hoặc rebaseline. Trước hết cần reconstruct state: approved scope, actual completion evidence, open defect, data migration readiness, contract obligation, critical dependency, cost forecast và decision authority.

Nếu status lịch sử dùng percent complete chủ quan, dashboard cũ không đủ làm evidence.

### Sunk cost

70% spend đã xảy ra không chứng minh project nên tiếp tục original plan. Governance cần future-cost/future-value analysis.

Nếu remaining investment vẫn tạo strategic capability nhưng original go-live không realistic, recovery có thể hợp lý. Nếu business case đã mất value, stop/pivot cũng là option hợp lệ.

### Scope stabilization

Requirement churn cần phân loại mandatory, committed, optional và future enhancement. Freeze toàn bộ scope có thể sai nếu compliance need mới xuất hiện; tiếp tục nhận mọi request cũng sai.

Change governance cần được reset với explicit threshold và product/business owner.

### Vendor conflict

Không bắt đầu bằng blame. Review contract, acceptance criterion, responsibility matrix và evidence về data quality. Có thể root cause shared: buyer data cleansing trễ và vendor tooling yếu.

Recovery plan cần action owner hai bên, milestone evidence và escalation path. Claim/legal handling tách khỏi technical recovery khi cần.

### Forecast và rebaseline

Chỉ rebaseline sau khi planning basis mới đủ credible và authority approve. Rebaseline không xóa history; original variance và rationale phải được giữ để learning/governance.

### Team health

Nếu team đã overtime nhiều tháng, thêm pressure có thể tăng defect. Recovery cần capacity realism và psychological safety để bad news được nói ra.

### Decision

Một recovery proposal tốt có option: phased rollout, reduced scope, delayed full rollout hoặc terminate module. Mỗi option cần value, cost, risk và transition impact.

### Failure mode

“Red project” thường bị cứu bằng kế hoạch đẹp hơn mà không sửa information quality, governance hoặc scope coupling. Khi sensor vẫn sai, recovery plan cũng chỉ là fiction mới.

## Case E — AI-assisted claims processing với sustainability và governance

### Context

Một insurer muốn dùng generative AI để hỗ trợ claim assessor, giảm handling time 30%. Vendor model là cloud service. Data chứa personal/medical information. Management muốn pilot nhanh vì competitor đã công bố AI capability.

### Problem framing

Objective là giảm processing time mà không tăng incorrect claim decision hoặc privacy risk. “Dùng GenAI” là solution hypothesis, không phải objective.

### Delivery approach

Pilot/adaptive learning phù hợp vì model behavior và user workflow uncertainty cao. Nhưng privacy, security, legal approval và data-location constraint cần governance cứng. Đây là hybrid project ngay từ nature của constraint.

### Data và quality

Evaluation không chỉ dùng average accuracy. Team cần segment claim type, severity của error, hallucination/factual inconsistency và human override.

Một 2% error rate có thể acceptable cho draft summarization nhưng unacceptable nếu system auto-deny claim. Same model, different decision consequence, different governance.

### Human-in-the-loop

Assessor phải review recommendation trước final decision. Nhưng control chỉ thật nếu workload cho phép review meaningful. Nếu target productivity ép reviewer approve 100 case/giờ, human-in-the-loop có thể thành theater.

### Vendor/procurement

Contract cần data handling, model/version change notification, incident, availability, IP và exit/export. Cheap API price không phản ánh switching cost hoặc regulatory exposure.

### Sustainability

AI inference tăng compute spend. Project có thể đo cost/energy proxy per claim và total volume. Nếu automation làm claim volume processed tăng mạnh, unit efficiency không đủ để kết luận total footprint giảm.

### Go/no-go

Pilot giảm handling 28%, serious error dưới threshold ở low-risk claim nhưng high-risk medical claim vẫn không ổn. Option hợp lý có thể limited rollout cho low-risk segment với mandatory human review, còn high-risk giữ manual process và tiếp tục evaluation.

Đây là risk segmentation, không binary “AI rollout” hay “AI fail”.

### Benefits realization

Sau rollout cần đo actual handling time, assessor adoption, override rate, complaint, error, vendor spend và incident. Pilot success không chứng minh production benefit nếu behavior thay đổi ở scale.

## Case F — Portfolio/PMO: nhiều initiative cùng tranh một change capacity

### Context

Một ngân hàng đang chạy đồng thời core-banking modernization, CRM replacement, eKYC upgrade, mobile redesign và regulatory reporting. Mỗi project riêng lẻ đều có business case hợp lý. Tuy nhiên ba initiative cùng cần một integration team, hai project cùng yêu cầu branch staff training trong quý IV và nhiều release cùng nhắm một production window.

Đây là problem mà project-level optimization không giải được. Nếu từng PM chỉ bảo vệ milestone của mình, organization có thể tạo resource contention, release collision và change saturation dù từng plan nhìn hợp lý độc lập.

### Portfolio view

Portfolio governance hỏi investment nào tạo strategic value cao hơn trong constraint chung, dependency nào cần sequence và initiative nào nên defer, phase hoặc stop. Decision không dựa vào ai escalate mạnh nhất mà vào strategy, mandatory obligation, expected value, risk, capacity và timing.

Một regulatory reporting project có ROI trực tiếp thấp nhưng deadline pháp lý cứng. Mobile redesign có customer value cao nhưng flexible timing hơn. Portfolio priority vì vậy không đồng nghĩa xếp project theo financial ROI đơn giản.

### PMO như information/control capability

PMO không chỉ thu status slide. Một PMO hữu ích làm cross-project dependency, shared-resource demand, decision latency, common risk và benefit visibility trở nên comparable.

Nếu mỗi project định nghĩa “green”, “complete” và “critical” khác nhau, portfolio dashboard chỉ cộng nhiều semantic không tương thích. PMO cần minimum information contract đủ để leadership nhìn system state mà không ép mọi team dùng cùng delivery method.

### Cross-project dependency

eKYC cần identity platform từ core modernization; mobile redesign cũng cần identity API đó. Nếu identity work slip, hai project cùng bị tác động. Tách risk thành hai register không làm exposure độc lập hơn.

Portfolio/PMO nên nhìn shared dependency như một failure domain, xác định owner ở level phù hợp và tránh hai PM cùng “đòi ưu tiên” resource theo cách cục bộ.

### Change saturation

CRM và core project đều lập training plan tốt nếu xét riêng. Nhưng cùng branch employee phải học hai process mới trong ba tuần trước year-end peak. Adoption risk đến từ tổng tải thay đổi, không phải chất lượng một training deck.

Response có thể là sequence rollout, segment population, giảm simultaneous change hoặc thêm transition support. “Mỗi project đã có change plan” không chứng minh organization có capacity hấp thụ tổng change.

### Capacity conflict

Integration team chỉ có 8 người nhưng demand từ năm initiative tương đương 15 người trong cùng tháng. Yêu cầu từng project “làm nhanh hơn” không tạo capacity mới.

Portfolio option gồm resequence, reduce scope, thuê thêm capability nếu onboarding economics hợp lý, hoặc protect mandatory work trước. Decision phải nhìn opportunity cost: ưu tiên project A nghĩa project B bị chậm bao nhiêu value hoặc risk.

### Benefits và continuation

Sau sáu tháng, CRM project vẫn on-budget nhưng adoption thấp; mobile project tạo benefit cao hơn dự kiến. Portfolio review không nên giữ funding chỉ vì annual plan đã approve. Business case là living decision object.

Tuy nhiên stop một initiative cũng có transition cost, contract obligation và dependency effect. “Value thấp hơn plan” là signal để reassess, không tự động là lệnh terminate.

### Failure mode

PMO thất bại khi trở thành reporting bureaucracy mà không cải thiện decision quality. Portfolio thất bại khi chỉ rank project một lần đầu năm rồi bỏ qua dependency/capacity/change trong execution. Project manager thất bại khi local success metric khiến system-level objective xấu đi.

Case này nối [Governance & Business Environment](./09_governance_compliance_and_business_environment.md), [Stakeholders](./03_stakeholders_communication_and_knowledge.md), [Schedule & Flow](./05_schedule_estimation_and_flow.md), [Risk](./08_risk_uncertainty_issues_and_decisions.md) và [Measurement](./11_measurement_status_closure_and_continuous_improvement.md).

## Cross-case synthesis: invariant nào giữ nguyên, variable nào làm decision đổi

Case khác nhau về domain nhưng có một số invariant. Thứ nhất, objective phải được giữ tách khỏi solution. DR site tồn tại để tạo resilience, mobile product để tạo customer/business outcome, AI để giảm handling mà không tăng harm. Khi solution trở thành objective, local optimization bắt đầu.

Thứ hai, evidence phải đi trước irreversible commitment khi information còn yếu. Trong Case A, physical procurement cần evidence/plan đủ trước order lớn. Case B dùng prototype/experiment. Case C test API và representative documents sớm. Case D reconstruct state trước recovery commitment. Cơ chế khác nhau nhưng invariant là information quality phải tương xứng irreversibility.

Thứ ba, authority phải match consequence. Product team có thể reorder backlog nhưng không tự waive regulation. PM có thể facilitate vendor recovery nhưng không tự quyết legal claim ngoài authority. Portfolio conflict không thể được giải bằng từng PM tự tối ưu.

Thứ tư, transition không phải phụ lục. Mọi case đều chỉ tạo value khi ownership sau project tồn tại: DR operations, product team, bank support, ERP business operation, claim assessor workflow hoặc portfolio benefit owner.

Nhưng nhiều variable làm next action đổi mạnh. Constraint source là một variable: legal deadline khác market target. Delivery mode là một variable: predictive baseline change khác backlog reprioritization. Harm velocity là một variable: active privacy incident cần contain sớm hơn normal analysis. Reversibility là một variable: prototype dễ rollback khác long-term contract. Information gap là một variable: vendor breach đã có evidence khác suspicion chưa verified.

Mental model tốt giữ invariant nhưng thay action theo variable. Đây là cách tránh slogan kiểu “luôn assess trước”, “luôn team first” hoặc “luôn follow change control”.

## Cross-case synthesis: bottleneck di chuyển

Một project không có một bottleneck cố định suốt lifecycle. Case A có thể bắt đầu với permit/procurement bottleneck rồi chuyển sang integration/testing. Case B có thể từ learning bottleneck chuyển sang engineering throughput rồi adoption. Case C có thể từ vendor API sang UAT window rồi operational readiness.

Khi team tiếp tục optimize bottleneck cũ, effort mất leverage. Thêm developer khi approval queue là constraint không giúp. Tăng training khi permission chưa mở không giúp. Tăng test khi requirement ambiguity tiếp tục tạo defect chỉ xử lý symptom.

Vì vậy mỗi status cycle nên hỏi: constraint hiện tại của system là gì, evidence nào chứng minh, và nếu constraint được giải thì constraint kế tiếp có khả năng ở đâu?

## Cross-case synthesis: risk chuyển hình khi project tiến triển

Uncertainty ở discovery có thể là ambiguity; sau design nó thành execution variability; gần release nó thành readiness/operational risk. Một risk item không nên sống nguyên wording suốt 12 tháng nếu underlying state đã đổi.

Case E minh họa rõ: ban đầu uncertainty là model quality; pilot xong, risk chuyển sang human capacity, vendor change và production drift. Case D: ban đầu dashboard uncertainty; sau reconstruct state, risk có thể chuyển thành commercial/scope/recovery execution.

Risk management tốt theo state transition, không chỉ giữ register history.

## Cross-case synthesis: local success có thể tạo global failure

Case A: facility complete nhưng failover unusable. Case B: velocity cao nhưng retention không đổi. Case C: sprint complete nhưng UAT chưa accepted. Case D: module on schedule nhưng program business case không viable. Case F: từng project green nhưng shared capacity impossible.

Đây là pattern quan trọng nhất của system thinking: metric/local deliverable chỉ là proxy. Mỗi time bạn thấy một local success, hỏi downstream outcome và shared constraint có còn healthy không.

## Cross-case synthesis: decision quality và outcome quality

Một decision đúng vẫn có thể outcome xấu vì uncertainty. Case B có experiment hợp lý nhưng user vẫn không thích feature. Case A chọn supplier tốt nhưng geopolitical disruption vẫn xảy ra. Case E rollout segment low-risk hợp lý nhưng vendor incident vẫn có thể xảy ra.

Review sau outcome phải hỏi information available lúc decision, assumption, authority, option và threshold—not hindsight “đã thất bại thì decision sai”. Ngược lại, may mắn không chứng minh process tốt.

Case study nên được dùng để luyện quality của reasoning, không đo khả năng đoán kết quả.

## Cách dùng case study để tự luyện

### Pass 1 — Không mở chapter khác

Đọc context rồi tự viết ngắn: objective, delivery mode, strongest constraint, current signal, authority, evidence còn thiếu và next action. Mục tiêu là test mental model đang có, không phải tra cứu.

### Pass 2 — Trace reasoning về canonical chapter

Sau khi trả lời, map mỗi decision về mechanism. Nếu không giải thích được vì sao vendor issue cần contract evidence, quay lại [Quality, Resources & Procurement](./07_quality_resources_and_procurement.md). Nếu không giải thích được vì sao project green nhưng portfolio vẫn unhealthy, quay lại [Governance](./09_governance_compliance_and_business_environment.md).

Không đọc lại toàn bộ library. Chỉ sửa đúng conceptual gap.

### Pass 3 — Counterfactual

Đổi một biến và quan sát decision có đổi không. Với Case C, giả sử vendor interface ổn định nhưng deadline không còn cố định; hoặc accuracy issue chỉ ảnh hưởng 0.01% user; hoặc regulator requirement trở thành recommendation. Với Case D, giả sử project mới chi 10% thay vì 70%; sunk cost không nên thay future-value decision, nhưng option recovery và termination cost có thể khác.

Với Case F, đổi regulatory project thành optional efficiency initiative. Priority có thể đổi vì constraint source đổi. Hoặc tăng integration capacity từ 8 lên 20 người nhưng giữ training saturation; bottleneck chuyển từ technical capacity sang adoption capacity.

### Pass 4 — Artifact/data injection

Tự thêm một artifact: risk register, EVM dashboard, defect trend, contract clause, stakeholder engagement assessment hoặc benefits dashboard. Hỏi evidence mới có làm state model hoặc next action thay đổi không.

Ví dụ thêm vào Case D một dashboard có `CPI = 0.78`, `SPI = 0.93` nhưng data migration readiness chỉ 35%. Nếu chỉ focus EVM, bạn có thể bỏ readiness driver lớn hơn. Thêm vào Case F một portfolio heatmap cho thấy ba project cùng phụ thuộc một vendor; systemic risk trở nên visible hơn.

### Pass 5 — Explain the rejected alternative

Đừng chỉ nói option nào tốt hơn. Giải thích vì sao alternative hấp dẫn nhưng sai state, authority, sequence hoặc system effect. Kỹ năng này trực tiếp giúp loại distractor trong exam.

Một answer có chất lượng thường có dạng:

```text
Signal → Impact → Information → Authority → Option → Next action → Evidence cần theo dõi
```

Nếu reasoning tự điều chỉnh theo value/risk/authority thay vì lặp câu thuộc lòng, mental model đã hoạt động.

### Pass 6 — Change the bottleneck

Sau khi chọn next action, giả sử action thành công rồi hỏi bottleneck kế tiếp là gì. Đây là cách tránh giải một vấn đề rồi tiếp tục dùng cùng intervention khi system đã chuyển state.

Ví dụ Case C fix vendor timeout xong nhưng UAT window vẫn là monthly external constraint. Case F tăng integration capacity nhưng branch training vẫn saturated. Decision quality phải theo system state mới.

### Pass 7 — Separate decision quality from outcome

Tự tạo hai ending: một ending tốt sau decision xấu nhờ may mắn và một ending xấu sau decision hợp lý do tail event. Sau đó đánh giá process bằng evidence available tại decision time.

Bài tập này chống hindsight bias và giúp reasoning giống project manager hơn người kể chuyện sau sự kiện.

## Coverage của các case

Case A chủ yếu ép bạn nối predictive planning, procurement, compliance, schedule, quality và closure. Case B nối adaptive learning, product value, flow, metric và governance. Case C tập trung hybrid interface, vendor, privacy, AI quality và operational transition. Case D luyện recovery, sunk cost, rebaseline, information quality và vendor conflict. Case E nối AI governance, human oversight, sustainability và benefit measurement. Case F đưa reasoning lên program/portfolio level với shared dependency, PMO, capacity và change saturation.

Không case nào chỉ thuộc một chapter. Đó chính là mục đích của layer consolidation này.

## Một micro-case về contractual claim

Construction vendor báo delay 20 ngày và yêu cầu extension + compensation vì buyer thay design. Buyer cho rằng vendor vốn đã chậm 10 ngày trước change.

Không nên nhảy thẳng sang “approve claim” hoặc “reject claim”. Tách reasoning thành entitlement: contract/change có trao quyền không; causation: buyer change thực sự gây bao nhiêu delay; concurrent delay: phần nào overlap với delay do vendor; quantum: time/cost relief nào có evidence. Song song đó, project vẫn cần technical recovery và forecast update; dispute process không nên làm recovery đứng yên.

Micro-case này giúp nối contract mechanics trong [07](./07_quality_resources_and_procurement.md) với schedule evidence trong [05](./05_schedule_estimation_and_flow.md) và governance trong [09](./09_governance_compliance_and_business_environment.md).

## Cross-domain connection

Software-specific requirement, test và production mechanics nên đọc tiếp ở [Software Engineering](../computer_science/09_software_engineering/README.md). PMP giữ focus ở system of decisions quanh delivery chứ không duplicate implementation detail.

AI implementation detail không được duplicate trong PMP; chapter [AI, sustainability và bối cảnh dự án hiện đại](./12_ai_sustainability_and_modern_project_context.md) chỉ giữ governance/value/risk boundary cần cho project reasoning.

Finance chuyên sâu như corporate valuation/portfolio theory tiếp tục thuộc [Investing Knowledge Library](../investing/README.md); PMP chỉ lấy phần cần cho project/portfolio decision.

## Mental model

> Một dự án thật không phát sinh “câu hỏi quality” hoặc “câu hỏi stakeholder” riêng rẽ. Một signal thường lan qua nhiều domain; kỹ năng PMP là giữ một state model đủ đúng, nhận ra invariant và context variable, theo dõi bottleneck/risk khi chúng chuyển hình, rồi chọn next action phù hợp mà không tối ưu cục bộ một metric hay một project.