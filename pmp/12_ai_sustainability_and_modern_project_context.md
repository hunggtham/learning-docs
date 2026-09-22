# 12 — AI, sustainability và bối cảnh dự án hiện đại

## Vì sao PMP 2026 nhấn mạnh context mới

Kỳ thi PMP cập nhật tháng 7/2026 đưa AI, sustainability và stakeholder engagement vào scenario rõ hơn, đồng thời tăng đáng kể trọng số Business Environment. Điều này phản ánh một thay đổi về mental model: project manager không chỉ điều phối plan nội bộ mà phải reasoning về technology, external impact và business outcome.

Chapter này không biến PMP thành khóa AI hay ESG. Mục tiêu là biết các yếu tố mới thay đổi risk, governance, stakeholder và value model như thế nào.

PMI hiện cũng mở rộng guidance chính thức về AI và sustainability ở cấp project work. Điều cần học không phải tên thêm nhiều standard, mà là một principle chung: technology và externality phải được đưa vào cùng hệ thống decision, governance, evidence và accountability như cost, schedule hay quality.

## AI như capability và như risk source

Trí tuệ nhân tạo (artificial intelligence / 인공지능) có thể được dùng bên trong project management để hỗ trợ summarization, forecasting, risk discovery, document analysis hoặc automation. Nhưng output của AI là evidence cần validation, không phải authority.

Nếu dùng model để tóm tắt meeting, project vẫn cần process xác nhận decision/action. Nếu model dự đoán delay, PM cần hiểu data quality, model limitation và action threshold. Automation tăng tốc cả correct process lẫn bad assumption.

Khi AI là một phần deliverable, risk rộng hơn: data privacy, bias, hallucination, model drift, explainability, IP, security, human oversight và regulatory change. Success criteria phải đo behavior thực tế, không chỉ “model đã tích hợp”.

## AI system là socio-technical system

Model chỉ là một component. Outcome còn phụ thuộc user behavior, interface, policy, workflow, incentive, monitoring và fallback. Cùng một model có thể an toàn trong use case draft internal nhưng nguy hiểm trong automatic approval.

Vì vậy quality/risk không thể đánh giá chỉ bằng benchmark model. Project phải đánh giá end-to-end system: ai nhập gì, model nhìn thấy gì, output hiển thị thế nào, user hiểu ra sao, action nào được phép và error được phát hiện/correct ở đâu.

Human factor là part of architecture, không phải control thêm sau cùng.

## Tách use case, model và operating system

Một lỗi phổ biến là nói “project AI” như thể AI tự là objective. Mental model tốt hơn là tách ba lớp. Use case xác định problem và expected outcome. Model hoặc AI capability chỉ là một component giải problem. Operating system xung quanh gồm data pipeline, human process, monitoring, policy, escalation và fallback.

Một model chính xác cao nhưng không có process xử lý low-confidence case vẫn có thể tạo outcome tệ. Vì vậy project manager phải quản lý toàn hệ thống delivery chứ không chỉ milestone “model ready”.

## Intended use và performance envelope

AI governance cần nói rõ intended use: model được dùng cho task nào, population nào, data nào, environment nào và consequence nào. Performance evidence chỉ có meaning bên trong envelope đó.

Một model evaluated trên English customer support không tự động được coi valid cho Korean legal advice. Một classifier chạy tốt ở volume 1.000 case/ngày chưa chứng minh latency/cost ở 1 triệu case.

Khi project mở rộng use case vượt envelope, đó là change cần re-evaluation—not simply “reuse model existing”.

## Bốn boundary cần quản trị: data, model, use và action

AI governance trở nên rõ hơn nếu tách bốn boundary.

Data boundary hỏi dữ liệu nào được phép dùng, nguồn/provenance là gì, retention và privacy ra sao. Model boundary hỏi model/version nào được approved, limitation và evaluation evidence nào tồn tại. Use boundary hỏi ai được phép dùng AI cho task nào. Action boundary hỏi output có thể chỉ gợi ý, tự động tạo draft hay được phép trigger action thật.

Một tổ chức có thể chấp nhận model viết meeting summary nhưng không cho cùng model tự gửi contract amendment. Cùng một technology nhưng action boundary khác làm risk profile khác hoàn toàn.

Project requirement và control nên gắn với boundary này thay vì một policy chung chung “AI phải được dùng có trách nhiệm”.

## Automation level là một design variable

Automation không binary manual/automatic. System có thể suggest, draft, rank, pre-fill, require approval, auto-act dưới threshold hoặc auto-act hoàn toàn.

Mức automation càng cao, human reaction time càng ít và error propagation càng nhanh. Nhưng quá nhiều approval cũng làm control thành bottleneck hoặc rubber-stamp.

Project nên chọn automation level theo consequence, reversibility, confidence, volume và human capacity. Đây là tailoring giống governance ở các domain khác.

## Risk tiering: control phải tỷ lệ với consequence

Không phải mọi AI use case cần cùng mức governance. Internal brainstorming không dùng confidential data có consequence thấp hơn model từ chối insurance claim hoặc scoring customer credit.

Một risk-tiering approach có thể xem xét decision consequence, data sensitivity, reversibility, automation level, affected population và ability to detect/correct error. Risk càng cao thì evidence, approval, monitoring, human oversight và auditability càng cần mạnh.

Over-control mọi use case làm experimentation chậm và thúc đẩy shadow AI. Under-control high-impact use case lại tạo legal, ethical và reputational exposure. Tailoring ở đây là proportional governance.

## Human-in-the-loop và accountability

Một nguyên tắc governance hữu ích là decision consequence càng cao thì human review/authority càng rõ. AI có thể đề xuất vendor ranking nhưng procurement owner chịu accountability; AI có thể draft risk list nhưng team chịu trách nhiệm validate context.

“AI đã đề xuất” không phải explanation đủ cho một decision có impact lớn.

Human-in-the-loop cũng không nên chỉ tồn tại trên giấy. Nếu reviewer có 3 giây để duyệt 500 recommendation mỗi giờ, control đó có thể không thực sự effective. Cần thiết kế workload, threshold và escalation sao cho human review có khả năng thay outcome.

## Human oversight có failure mode riêng

Human reviewer có thể over-trust automation, fatigue, skip review hoặc chỉ confirm recommendation mặc định. Đây là automation complacency.

Một review control tốt cần meaningful choice, evidence context và enough time. Random sampled audit hoặc disagreement review có thể kiểm tra reviewer behavior thay vì giả định “có người trong loop = safe”.

Nếu human override rate gần zero trong system vốn có uncertainty material, đó có thể là dấu hiệu model hoàn hảo—hoặc control theater. Cần investigate.

## Confidence, uncertainty và abstention

AI system nên có cách biểu diễn uncertainty hoặc ít nhất boundary nơi output không đủ đáng tin để tự động action. Trong nhiều use case, khả năng “không biết” hoặc chuyển case sang human là control quan trọng hơn việc cố trả lời mọi request.

Project requirement có thể bao gồm confidence threshold, fallback path và manual override. Đây là ví dụ quality requirement được hình thành từ risk analysis.

Abstention cũng cần capacity planning. Nếu 30% case bị route manual nhưng operations chỉ đủ xử lý 5%, fallback không thực sự viable.

## Data quality là project dependency

AI output phụ thuộc data. Nếu training/evaluation data không representative, label không consistent hoặc production data distribution thay đổi, model performance có thể khác hẳn pilot.

Project manager không cần trở thành data scientist nhưng phải nhìn data như dependency có owner, provenance, privacy rule, quality criterion và monitoring. “Model team chịu trách nhiệm” không đủ nếu business process cung cấp data sai.

## Data provenance, rights và lineage

Data không chỉ cần “sạch”; cần biết đến từ đâu, quyền sử dụng là gì, biến đổi thế nào và version nào được dùng trong evaluation/training/retrieval.

Nếu incident xảy ra mà team không biết model/retrieval đã dùng dataset nào, root-cause analysis yếu. Nếu license cho phép internal analysis nhưng không cho model training, technical feasibility không đồng nghĩa legal permission.

Data lineage vì vậy là governance/evidence requirement, không chỉ data-engineering concern.

## Evaluation phải gắn với harm và use case

Một aggregate accuracy score hiếm khi đủ. Error type khác nhau có cost khác nhau. Trong eKYC, false accept có thể là security/compliance risk lớn hơn false reject; trong support chatbot, wrong refund policy có impact khác typo nhỏ.

Evaluation nên segment theo user, scenario và severity. Threshold phải nối với business risk appetite chứ không chỉ benchmark kỹ thuật.

## Evaluation matrix: capability × harm × operating condition

Evaluation sâu hơn khi phân biệt model có khả năng làm gì, error gây harm nào và trong condition nào performance đổi. Peak load, long context, rare language, adversarial input hoặc stale retrieval có thể khác benchmark normal.

Không cần test infinite scenario; cần prioritize theo exposure, severity và plausibility.

Edge case hiếm nhưng catastrophic có thể đáng test hơn common case low-impact.

## Benchmark leakage và evaluation theater

Một model có thể đạt score cao nếu evaluation set quá giống training data, test case bị biết trước hoặc metric không phản ánh production behavior. Khi team tối ưu liên tục trên một benchmark cố định, benchmark có thể dần trở thành target thay vì independent evidence.

Evaluation tốt cần holdout hoặc fresh test set khi phù hợp, representative scenario, adversarial/edge case và human review cho harm khó nén thành một số. Với generative AI, citation correctness, refusal quality hoặc factual severity có thể quan trọng hơn average helpfulness score.

“95% accuracy” không có meaning nếu không biết denominator, distribution và 5% sai còn lại gây hậu quả gì.

## Red-team, misuse và abuse case

AI system có thể fail không chỉ vì accidental error mà vì user cố tình exploit. Prompt injection, data exfiltration, policy bypass hoặc adversarial usage là examples ở technical level; ở project level cần mental model rộng hơn: ai có incentive misuse system và consequence là gì?

Threat modeling nên gồm intended user, careless user và malicious user khi exposure đáng kể.

Control có thể là permission boundary, input/output filtering, tool restriction, audit log, rate limit hoặc human escalation. PMP không cần implement kỹ thuật, nhưng phải ensure ownership/evidence tồn tại.

## Model drift và post-launch governance

AI behavior có thể thay đổi khi data, user behavior, model version hoặc external environment đổi. Vì vậy go-live không kết thúc quality governance.

Cần có monitoring, incident classification, rollback/fallback, model/version traceability và owner cho re-evaluation. Nếu vendor silently update model, project/operation phải biết change control nào áp dụng.

## Drift không chỉ một loại

Data drift là input distribution đổi. Concept drift là relationship giữa input và desired outcome đổi. Configuration drift là prompt/retrieval/threshold/tool thay. Vendor/model drift là provider update behavior.

Các loại drift cần evidence khác nhau. Chỉ theo dõi latency/uptime không phát hiện semantic degradation.

Project nên định nghĩa signal nào trigger re-evaluation, không chờ complaint tích lũy lớn.

## Model/version change cũng là configuration management

AI system thường có nhiều moving parts: prompt, retrieval source, model version, threshold, safety rule, tool permission và data pipeline. Nếu chỉ version code nhưng không version những component này, root-cause analysis sau incident sẽ khó.

Một production decision nên có enough traceability để biết request được xử lý bởi configuration nào. Điều này nối AI governance trực tiếp với [Artifacts, information flow và traceability](./14_artifacts_information_and_traceability.md).

Change có thể cần regression evaluation trước rollout, canary/pilot, rollback criterion và approval theo risk tier. “Vendor model tốt hơn” không tự động có nghĩa safe để auto-upgrade.

## AI observability phải nhìn semantic outcome

Traditional monitoring xem uptime, latency, error code. AI cần thêm semantic signal: harmful response rate, override, abstention, groundedness, complaint, segment performance hoặc policy violation tùy use case.

Observability không cần monitor mọi câu trả lời thủ công. Có thể sample, automated check, human audit và incident feedback.

Nếu system uptime 100% nhưng recommendation quality drift, technical dashboard xanh vẫn không phản ánh service health.

## AI incident response

AI incident có thể khác software crash thông thường. System vẫn uptime nhưng tạo harmful output, data leakage, discriminatory pattern hoặc wrong recommendation. Incident classification vì vậy cần nhìn impact chứ không chỉ availability.

Response có thể gồm contain use case, disable automation, switch fallback, preserve evidence, identify affected decisions/users, notify stakeholder/compliance và re-evaluate model/configuration. Với high-impact system, incident drill trước production có thể đáng giá như disaster-recovery drill.

## AI incident có thể cần decision remediation

Nếu model hỗ trợ quyết định đã ảnh hưởng customer, containment system chưa đủ; organization có thể cần identify affected decisions và review/remediate outcome.

Traceability từ decision tới model/configuration/input trở thành critical. Nếu không biết ai bị ảnh hưởng, remediation scope không thể xác định đáng tin.

## AI supply-chain và vendor risk

Dùng third-party model tạo dependency về availability, pricing, data handling, intellectual property, security và roadmap. Vendor có thể đổi API, policy hoặc model quality.

Contract và architecture cần xem xét exit strategy, data portability, version pinning nếu có, service level, breach notification và ownership của generated content. Đây là nơi procurement, risk và technical architecture nối nhau.

## AI concentration risk

Nhiều use case nội bộ có thể phụ thuộc cùng model/provider. Mỗi project nhìn risk nhỏ nhưng organization có common-cause exposure nếu provider outage, price change hoặc policy restriction.

Portfolio/architecture governance nên map concentration và fallback. “Có nhiều AI project” không nghĩa diversified nếu tất cả cùng dependency.

## Automation bias và over-trust

Người dùng có xu hướng tin recommendation của system tự động dù output sai, đặc biệt khi interface tạo cảm giác chắc chắn. Đây là automation bias.

Project không nên chỉ train user “hãy cẩn thận”. Control tốt hơn có thể gồm confidence display, citation/evidence, constrained action, sampled review và clear escalation path. Behavior design là một phần risk mitigation.

## Hidden human labor và shifted cost

AI automation thường vẫn cần labeling, prompt maintenance, exception review, quality audit và incident handling. Nếu business case chỉ tính model/API cost mà bỏ human fallback, expected saving bị overstate.

Automation có thể chuyển work từ frontline sang specialist. Total labor không giảm nhiều nhưng skill mix/capacity constraint thay đổi.

Benefit model cần đo end-to-end process, không chỉ step được automate.

## AI trong chính công việc project management

Generative AI có thể hỗ trợ draft charter, summarize workshop, identify possible risk, transform meeting note hoặc search knowledge. Nhưng confidential data, hallucinated fact và loss of context là risk.

Một working agreement nên xác định loại dữ liệu nào được đưa vào tool, output nào cần human verification, ai chịu trách nhiệm final artifact và cách record source. Với decision quan trọng, AI nên tăng information processing chứ không thay decision accountability.

## Shadow AI

Khi official process quá chậm hoặc tool không đáp ứng need, employee có thể dùng public AI ngoài governance. Shadow AI tạo data leakage, inconsistent output và untraceable decision.

Response không chỉ là cấm. Organization cần hiểu demand, cung cấp safe alternative, proportional guardrail và education. Over-control low-risk use case có thể tăng incentive đi vòng control.

Shadow usage là signal governance-design mismatch giống shadow process ở project governance.

## Sustainability là lifecycle constraint và value dimension

Bền vững (sustainability / 지속가능성) có thể gồm environmental, social và economic effects. Trong project, nó đi vào requirement, procurement, design trade-off, compliance, risk và benefit.

Ví dụ data center project có energy/water footprint; construction có material/waste/safety; software có compute cost và hardware lifecycle. Sustainability không nên bị thêm như checklist cuối dự án nếu design decision sớm đã khóa phần lớn impact.

## Planet, People và Prosperity như ba lens thực hành

P5 sustainability guidance hiện hành của PMI/GPM mở rộng environmental, social và economic impact. Một cách reasoning thực dụng là nhìn ba lens: Planet hỏi resource/emission/waste/ecosystem; People hỏi labor, safety, privacy, equity và community impact; Prosperity hỏi economic resilience, lifecycle cost và long-term value.

Ba lens không độc lập. Chọn cloud region tiết kiệm cost có thể tăng carbon intensity; automation tăng productivity có thể tạo reskilling burden; local sourcing có thể tăng unit price nhưng giảm supply-chain exposure và tạo community value.

Mục tiêu không phải tối đa hóa mọi lens cùng lúc mà làm trade-off visible và có governance.

## Sustainability không chỉ là environmental metric

Environmental impact dễ thấy, nhưng social và economic sustainability cũng quan trọng. Automation có thể tăng productivity nhưng tạo reskilling need. Procurement giá thấp có thể dựa trên supplier labor practice rủi ro. Infrastructure rẻ lúc build có thể maintenance cost cao suốt lifecycle.

Project manager nên mở boundary từ delivery cost sang lifecycle impact khi business case và governance yêu cầu.

## Materiality: không đo mọi thứ như nhau

Sustainability program dễ biến thành checklist rất rộng. Materiality hỏi impact nào đủ lớn hoặc relevant với stakeholder/policy để ảnh hưởng decision.

Một software project nhỏ có thể không cần lifecycle analysis chi tiết cho office paper nhưng cần chú ý privacy, cloud compute và hardware refresh nếu chúng material. Construction project có material/emission/safety profile khác.

Materiality giúp tập trung evidence vào impact có consequence, tránh reporting overhead không tạo decision.

## Lifecycle thinking

Nhiều impact bị quyết định trước khi build. Material choice, architecture, cloud region, hardware, vendor hoặc process design có thể khóa energy, maintenance và disposal profile nhiều năm.

Vì vậy sustainability assessment nên xuất hiện trong option analysis và design trade-off, không chỉ trong closure report.

## Boundary của lifecycle assessment quyết định conclusion

Nếu chỉ đo project delivery phase, option A có thể nhìn tốt hơn. Nếu thêm operation/maintenance/end-of-life, option B có thể thắng.

Ví dụ cloud migration giảm on-premise hardware nhưng tăng continuous compute. Automation giảm headcount task nhưng tăng review/retraining. Measurement boundary phải được explicit để stakeholder hiểu claim đang nói về phần nào của lifecycle.

Không có boundary duy nhất đúng cho mọi decision; boundary phải đủ rộng để không hide material externality.

## Baseline, target và measurable impact

“Sustainable hơn” là statement yếu nếu không có baseline. Cần xác định current state, target, measurement method và owner.

Ví dụ “giảm compute cost 20% per transaction so với baseline release” rõ hơn “tối ưu green IT”. Nhưng metric cũng cần guardrail để tránh chuyển cost sang nơi khác, như giảm compute nhưng tăng latency đến mức user phải retry nhiều hơn.

## Impact threshold và escalation

Không phải sustainability impact nào cũng cần steering committee. Một impact nhỏ có thể xử lý trong team; impact vượt policy, regulatory threshold hoặc stakeholder tolerance cần escalation.

Tư duy threshold làm sustainability trở thành governance mechanism thay vì một score trang trí. Nếu supplier labor issue vượt tolerance, procurement decision có thể phải dừng dù schedule/cost đang favorable.

Điều này giống risk/compliance: cần category, owner, threshold, response và evidence.

## Systems thinking và externality

Project có thể tối ưu local objective nhưng tạo cost nơi khác. Một automation giảm headcount cost nhưng tăng support burden hoặc unfair outcome; một faster shipping option tăng emission; một security control mạnh tăng user friction.

Systems thinking hỏi boundary của measurement có đủ rộng chưa. Externality không có nghĩa mọi impact phải tối ưu tuyệt đối, mà phải được nhìn thấy và trade-off có governance.

Một useful question là “ai nhận benefit và ai chịu cost?”. Nếu hai nhóm khác nhau, stakeholder analysis cần phản ánh distributional effect chứ không chỉ total benefit.

## Burden shifting

Một improvement có thể chuyển impact giữa phase, location hoặc stakeholder. Cloud làm local energy footprint giảm nhưng provider footprint tăng. Automation giảm user effort nhưng tăng reviewer burden. Vendor giá rẻ giảm capex nhưng tăng maintenance/support cost.

Burden shifting là failure mode của narrow boundary. Project manager cần biết metric đang optimize có đẩy cost/harm ra ngoài scope đo hay không.

## Rebound effect và unintended consequence

Efficiency improvement đôi khi làm usage tăng đến mức tổng resource consumption không giảm. Đây là rebound effect. Ví dụ AI inference rẻ hơn có thể làm số request tăng mạnh.

Project evaluation nên đo system-level outcome thay vì chỉ unit efficiency khi scale có thể thay đổi behavior.

## AI và sustainability giao nhau trực tiếp

AI project có resource footprint từ training/inference, storage, network và hardware lifecycle. Nhưng không nên kết luận máy móc rằng “AI dùng nhiều compute nên không sustainable”; AI cũng có thể giảm waste, route transport tốt hơn hoặc optimize energy system.

Decision cần nhìn net lifecycle effect. Một model nhỏ hơn giảm compute 40% nhưng accuracy giảm khiến manual rework tăng mạnh có thể không tốt hơn overall. Ngược lại, model lớn hơn chút nhưng giảm error ở high-impact case có thể tạo net value lớn hơn.

Đây là ví dụ vì sao unit metric và system outcome phải được nối với nhau.

## Value chain và supplier evidence

Sustainability impact không dừng ở boundary của project team. Supplier hardware, cloud provider, outsourced labor hoặc logistics có thể tạo phần lớn footprint/risk.

Procurement requirement có thể yêu cầu evidence phù hợp: energy/carbon reporting, labor/safety policy, data-center region, material provenance hoặc end-of-life plan tùy context. Không cần thu mọi dữ liệu có thể; chỉ thu evidence liên quan material impact và decision.

Nếu sustainability score của vendor chỉ là self-declaration không auditability, project nên coi đó là weak evidence chứ không phải fact.

## Evidence quality và green claim

Sustainability claim có strength khác nhau tùy source, method và boundary. Vendor brochure yếu hơn audited data; estimated proxy khác measured value; per-unit improvement khác total footprint.

Governance nên tránh false precision khi evidence weak. “Estimated reduction khoảng 15–25% under current volume” trung thực hơn con số 19.7% nếu input uncertainty lớn.

## Data-driven decision và data quality

PMP 2026 nhấn mạnh collect/analyze data cho decision. Nhưng data-driven không phải “có dashboard”. Cần hỏi data có representative không, definition ổn định không, lag bao lâu, incentive có làm metric bị game không và uncertainty còn lại là gì.

Một metric chính xác về wrong outcome vẫn dẫn decision sai. Ví dụ team tối ưu số story point nhưng customer churn tăng.

Data quality gồm completeness, accuracy, timeliness, consistency và relevance. Không metric nào “objective” nếu collection process bias hoặc definition thay đổi giữa kỳ.

## Technology change như external environment

Technology có thể thay assumption của business case giữa project. Một dependency bị deprecated, regulation AI thay đổi hoặc competitor ra capability mới có thể làm scope/backlog/value thay đổi. Project cần scanning mechanism và change decision, không thể coi initial plan là immutable truth.

Emerging technology còn tạo skill risk. Team có thể estimate sai vì chưa có historical productivity data. Pilot và progressive commitment thường an toàn hơn full-scale commitment ngay từ đầu.

## Obsolescence risk

Technology project dài có thể giao solution đã outdated. Nhưng chạy theo every new release cũng tạo churn.

Project cần trigger cho re-evaluation: vendor end-of-life notice, major regulation, security issue, material cost shift hoặc capability leap. Không phải trend trên social media nào cũng cần architecture change.

Decision phải cân switching cost, maturity và option value.

## Responsible experimentation

Experiment giúp giảm uncertainty nhưng experiment cũng cần boundary. Với low-risk internal prototype, guardrail có thể nhẹ. Với personal data hoặc customer-facing AI, experiment cần consent, privacy, safety và rollback rõ hơn.

“Đang thử nghiệm” không loại bỏ accountability nếu experiment có thể gây harm thật.

Experiment tốt có hypothesis, exposure limit, success/failure criterion và stop condition. Nếu pilot cứ kéo dài vì team không định nghĩa decision gate, experiment biến thành shadow production.

## Pilot-to-production gap

Pilot thường có clean data, expert support, limited volume và motivated user. Production có messy input, scale, turnover, abuse và operational constraint.

Go/no-go cần hỏi assumption nào thay đổi khi scale. Human fallback đủ ở 1.000 case nhưng không ở 1 triệu. Manual monitoring trong pilot có thể không scalable.

Pilot success là evidence, không phải proof production-ready.

## Ví dụ scenario

Project dùng generative AI để hỗ trợ nhân viên tư vấn. Pilot cho thấy thời gian xử lý giảm 25% nhưng 2% câu trả lời có factual error nghiêm trọng. Response hợp lý không phải rollout vì productivity gain cũng không phải hủy ngay. Team cần classify harm, thiết kế human review, grounding/evaluation, usage boundary, monitoring, privacy/compliance và threshold trước khi scale. Đây là integration của value, quality, risk, governance và stakeholder impact.

Giả sử error nghiêm trọng tập trung ở một nhóm policy hiếm nhưng high-impact. Team có thể giới hạn AI không xử lý nhóm đó, route sang expert và tiếp tục rollout phần low-risk. Đây là tailoring theo risk segmentation thay vì binary “AI tốt/xấu”.

Một case sustainability khác: migration cloud giảm server on-premise nhưng cloud bill và compute usage tăng mạnh. Nếu chỉ đo hardware local, project có vẻ green hơn; nếu nhìn full lifecycle/usage, kết luận có thể khác. Measurement boundary quyết định quality của decision.

Một case governance khác: vendor thông báo model version mới sẽ auto-deploy tuần sau. Benchmark vendor tốt hơn, nhưng project đang ở regulated workflow. PM không nên coi đây là minor patch mặc định; cần xác định configuration/change authority, regression evidence, fallback và whether approval threshold bị kích hoạt.

Một case shadow AI: analyst copy customer data vào public chatbot để tiết kiệm thời gian vì official tool quá chậm. Chỉ discipline analyst không đủ. Organization phải contain exposure, review data impact, hiểu workflow pressure và cung cấp safe alternative/guardrail để demand không tiếp tục đi vòng governance.

## Failure modes cần nhớ

AI washing xảy ra khi project thêm AI dù use case không cần. Greenwashing xảy ra khi sustainability claim không có baseline/evidence. Dashboard bias xảy ra khi metric dễ đo thay metric quan trọng. Human-in-the-loop theater xảy ra khi reviewer không có capacity hoặc authority thật. Pilot trap xảy ra khi prototype tốt trong controlled data nhưng operating model production chưa sẵn sàng.

Benchmark theater xảy ra khi score đẹp nhưng test set không đại diện production. Auto-upgrade risk xảy ra khi model/vendor thay đổi nhưng organization không có configuration traceability. Sustainability theater xảy ra khi scorecard có nhiều mục nhưng không có threshold, owner hoặc decision consequence.

Shadow AI, burden shifting, hidden human labor và pilot-to-production gap đều là cùng một class failure: system boundary bị định nghĩa quá hẹp so với nơi consequence thực sự xuất hiện.

Các failure mode này đều chung một root cause: artifact hoặc technology được dùng thay cho reasoning về system.

## Mental model

> AI và sustainability không phải các chapter rời khỏi project management; chúng mở rộng system boundary. AI đòi hỏi quản trị data–model–use–action, human behavior và semantic outcome; sustainability đòi hỏi lifecycle/materiality/externality. Cả hai đều phải được quản lý bằng evidence, proportional control, traceability và ownership giống các constraint quan trọng khác.

Tiếp theo: [Scenario reasoning và chiến lược làm PMP](./13_pmp_scenario_reasoning_and_exam_strategy.md).