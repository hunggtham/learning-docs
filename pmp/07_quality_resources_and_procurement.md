# 07 — Quality, resources và procurement

## Quality là fitness for purpose

Chất lượng (quality / 품질) không đồng nghĩa “nhiều feature” hoặc “đắt tiền”. Quality là mức deliverable đáp ứng requirement và phù hợp mục đích sử dụng. Grade có thể thấp nhưng quality cao nếu đúng specification; một sản phẩm nhiều feature nhưng lỗi critical vẫn quality thấp.

Quản lý quality cần ba lớp reasoning: requirement chất lượng là gì, process nào tạo khả năng đạt chúng, và evidence nào xác nhận deliverable thực sự đạt.

Quality không phải activity của QA team ở cuối pipeline. Nó là property emergent từ requirement, design, process, capability, supplier và feedback loop xuyên lifecycle.

## Quality và grade khác nhau

Grade nói category hoặc feature level. Quality nói mức conformance/fitness trong grade đã chọn.

Một economy product có ít feature nhưng đạt mọi specification có thể quality cao. Một premium product nhiều feature nhưng unreliable có quality thấp. Distinction này giúp tránh gold plating: thêm capability không tự làm quality tốt hơn.

## Quality requirement phải operationalizable

“High quality”, “secure”, “easy to use” không đủ để control. Requirement cần evidence criterion phù hợp context.

Ví dụ availability 99.95%, defect severity-1 bằng 0 trước go-live, task completion usability test trên 90%, hoặc material tolerance ±0.2 mm. Không phải mọi quality attribute cần numeric, nhưng phải đủ rõ để reviewer biết pass/fail hoặc mức acceptable.

Một criterion còn phải gắn đúng context đo. “Response dưới 300 ms” vô nghĩa nếu workload, percentile, environment và transaction type không rõ. Quality metric càng xa usage thực tế càng dễ tạo false confidence.

## Quality planning, assurance và control

Quality planning xác định standard, metric, acceptance và process. Quality assurance tập trung vào process có khả năng tạo output đúng không. Quality control inspect/measure deliverable hoặc process result.

Ba lớp không thay thế nhau. Test nhiều không cứu requirement sai. Process audit tốt không chứng minh từng deliverable pass. Quality plan tốt không có giá trị nếu execution không follow và evidence không được thu.

Một cách nhìn sâu hơn là quality management cố tạo một process có capability đủ cao để output đúng trở thành trạng thái bình thường, thay vì dựa vào heroic inspection ở cuối.

## Process capability và quality at source

Nếu process thường xuyên tạo defect rồi QA lọc ở cuối, organization có detection capability nhưng chưa chắc có production capability tốt. Quality at source nghĩa người/process tạo work cũng có mechanism phát hiện lỗi sớm tại nơi lỗi sinh ra: peer review, automated validation, poka-yoke/error-proofing, checklist critical step hoặc built-in control phù hợp domain.

Mục tiêu không phải chuyển trách nhiệm sang cá nhân, mà rút feedback loop. Defect được phát hiện một giờ sau khi tạo thường rẻ và dễ hiểu hơn defect được phát hiện ba tháng sau khi context đã mất.

Process capability không đồng nghĩa zero variation. Nó nghĩa variation đủ ổn định và nằm trong tolerance phù hợp để downstream có thể tin vào output mà không cần kiểm tra lại mọi thứ.

## Prevention tốt hơn inspection khi failure cost cao

Inspection cuối pipeline chỉ phát hiện defect sau khi cost đã xảy ra. Prevention đưa quality vào requirement, design, working method và automated control sớm hơn.

Cost of Quality thường được nhìn thành prevention + appraisal + failure cost. Internal failure được phát hiện trước customer; external failure xảy ra sau release/delivery và thường đắt hơn vì incident, recall, penalty hoặc trust loss.

Tuy nhiên “test nhiều vô hạn” cũng không tối ưu. Control phải proportional với risk. Safety-critical component cần evidence mạnh hơn low-impact internal tool.

Trong software, xem thêm [Testing, quality và verification strategy](../computer_science/09_software_engineering/02_testing_quality_and_verification_strategy.md) để hiểu sâu test architecture và evidence kỹ thuật.

## Cost of quality là economic trade-off

Prevention có cost, appraisal có cost và failure có cost. Mục tiêu không phải zero spending on failure bằng mọi giá, mà minimize total expected cost trong constraint và risk appetite.

Một defect cosmetic hiếm có thể rẻ hơn để accept; một privacy defect low-probability có impact lớn nên prevention mạnh hơn. Economic reasoning giúp quality control không trở thành checklist đồng đều.

Cost of poor quality còn gồm những khoản khó thấy: rework làm chậm feature khác, support load, customer churn, warranty, opportunity cost và management attention. Một defect sửa mất hai giờ có thể gây system cost lớn hơn nhiều nếu nó làm release bị delay hoặc kéo specialist khỏi critical work.

## Quality debt và escaped defect

Khi team chấp nhận known defect, bỏ kiểm thử, nới acceptance hoặc defer corrective action để giữ deadline, họ có thể đang tạo quality debt. Debt có thể hợp lý nếu visible, owner rõ, impact hiểu được và repayment plan có thật. Nó nguy hiểm khi được gọi là “temporary exception” nhưng không bao giờ retire.

Escaped defect là defect vượt qua control hiện tại và được phát hiện ở downstream hoặc production. Trend escaped defect hữu ích vì nó kiểm tra effectiveness của control system, không chỉ số lượng bug nội bộ.

Nếu internal defect count giảm nhưng escaped defect tăng, kết luận “quality tốt hơn” có thể sai. Metric cần được đọc như một system, không tách rời.

## Root cause và contributing factors

Complex failure hiếm khi có một root cause duy nhất. Five Whys hoặc fishbone giúp mở investigation nhưng có thể oversimplify nếu team ép một linear chain.

Một incident production có thể đồng thời do requirement ambiguity, missing automated test, deadline pressure và access control yếu. Corrective action nên target leverage point, không chỉ người cuối cùng chạm system.

Root cause analysis tốt còn phân biệt cause có thể kiểm soát và condition làm failure dễ xảy ra. “Engineer nhập sai” có thể là immediate cause, nhưng interface cho phép thao tác nguy hiểm không confirmation hoặc workload quá cao có thể là contributing system condition.

## Corrective, preventive và defect repair

Defect repair sửa output cụ thể. Corrective action xử lý cause của nonconformity đã xảy ra. Preventive action giảm khả năng future problem dựa trên identified risk hoặc weakness.

Nếu team fix cùng loại bug mỗi release nhưng không đổi process, họ chỉ repair symptom. Nếu thêm lint/test rule để ngăn class bug đó, system capability tăng.

## Statistical thinking ở mức cần thiết

Variation luôn tồn tại. Control chart hoặc trend analysis giúp phân biệt process variation bình thường với special signal. React mạnh với từng data point random có thể làm process bất ổn hơn.

PMP learner không cần trở thành statistician, nhưng cần hiểu quality decision dựa trên pattern và threshold, không anecdote đơn lẻ.

Một điểm quan trọng là specification limit và process behavior khác nhau. Deliverable có thể vẫn pass specification nhưng process đang drift dần về boundary; nếu chỉ nhìn pass/fail cuối cùng, early signal bị bỏ lỡ.

## Continuous improvement

Các vòng như Plan-Do-Check-Act (PDCA) hay retrospective đều dựa trên feedback. Improvement tốt cần phân biệt symptom và root cause. Nếu defect tăng vì requirement ambiguity, tăng số tester có thể chỉ xử lý symptom.

Improvement cần hypothesis và measure. “Thêm code review checklist có giảm escaped defect loại X mà không tăng lead time quá mức không?” rõ hơn “hãy review kỹ hơn”.

Improvement cũng cần guardrail. Giảm defect bằng cách làm review chậm gấp ba có thể không tối ưu nếu business cần fast feedback. Quality improvement là multi-objective optimization, không phải tối đa một metric.

## Resource management là capability + availability

Tài nguyên (resources / 자원) gồm people, equipment, facilities, material và service capacity. Với knowledge work, một người “rảnh 50%” không tương đương mọi người khác “rảnh 50%”; capability, context switching và domain knowledge matters.

Resource planning cần nhìn role, skill, capacity, timing và dependency. Resource histogram hoặc capacity view chỉ hữu ích nếu phản ánh constraint thật.

## Capacity không bằng calendar availability

Một engineer có 8 giờ calendar không có 8 giờ productive capacity cho project nếu có support duty, meeting và context switching.

Planning dựa trên nominal availability thường gây overcommit. Sustainable capacity cần reserve cho variability và unplanned work, nhất là operational environment.

Capacity nên được nhìn theo effective throughput, không chỉ giờ phân bổ. Hai người mỗi người 50% trên hai project có thể tạo ít output hơn một người full-time trên một project vì switching cost, meeting duplication và memory reload.

## Utilization paradox và queue

Đẩy specialist lên gần 100% utilization thường làm queue tăng mạnh. Khi mọi minute đã được booked, một request bất ngờ không có slack để hấp thụ và chờ đợi lan sang nhiều team.

Vì vậy resource “nhàn một chút” ở bottleneck có thể là capacity bảo hiểm cho variability, không phải waste. Đây là cùng logic flow đã được giải thích ở [Schedule & Flow](./05_schedule_estimation_and_flow.md): local utilization cao không đảm bảo system throughput cao.

## Skill matrix và single point of failure

Resource risk không chỉ thiếu headcount. Có thể đủ 10 người nhưng chỉ một người biết legacy database hoặc contract negotiation.

Skill matrix giúp nhìn capability concentration. Cross-training, pairing và documentation giảm bus factor. Critical knowledge transfer nên được plan trước khi người đó rời project, không chờ notice period.

Skill substitution cũng không tuyến tính. Hai junior không tự động thay một specialist ở decision critical. Resource model phải hiểu minimum capability threshold và learning curve, không coi mọi FTE là fungible unit.

## Learning curve và onboarding cost

Resource mới không tạo full capacity ngay ngày đầu. Họ cần domain context, environment access, working agreement và knowledge transfer; đồng thời người cũ phải dành thời gian onboarding.

Vì vậy “thêm người” vào project trễ có thể tạm thời giảm net throughput. Càng nhiều coordination dependency, ramp-up cost càng lớn. Resource decision phải nhìn time-to-effective-capacity, không chỉ headcount.

## Resource leveling và smoothing

Khi demand vượt availability, resource leveling thay schedule để phù hợp constraint và có thể đổi critical path/finish date. Resource smoothing dùng available float để cân allocation nhưng cố giữ finish date.

Điểm cốt lõi là schedule phải phản ánh capacity thật. Một plan giả định cùng người làm ba activity song song không trở nên khả thi chỉ vì Gantt đẹp.

## Shared resource và portfolio contention

Project có thể plan đúng nội bộ nhưng vẫn fail khi nhiều project cùng tranh một shared specialist, environment hoặc approval body. Đây là resource risk ở portfolio/system level.

Nếu tất cả project đều được plan như thể shared resource luôn available, tổng portfolio plan là impossible dù từng plan riêng trông feasible. PM cần surface contention và đưa priority decision tới level có authority phân bổ capacity.

## Team acquisition và release

Project cần resource đúng thời điểm. Onboarding quá muộn có learning curve; giữ specialist quá lâu tăng cost/opportunity cost.

Resource release cũng cần transition knowledge. Một chuyên gia rời project ngay sau build nhưng trước UAT có thể tạo risk lớn dù planned task của họ đã complete.

Release decision nên nhìn remaining uncertainty và knowledge dependency, không chỉ số task còn lại. Specialist có thể không còn nhiều work nhưng vẫn là critical fallback trong integration window.

## RACI và giới hạn

RACI làm rõ Responsible, Accountable, Consulted, Informed. Nhưng matrix không sửa được governance mơ hồ nếu authority thực tế khác trên giấy.

Một work item nên có accountability rõ. Nếu ba người đều “A”, thường decision ownership chưa rõ. Nếu người “A” không có authority/resource để quyết, RACI chỉ là documentation theater.

RACI cũng không mô tả dependency timing, decision threshold hoặc escalation. Nó là role map, không phải operating model hoàn chỉnh.

## Procurement là chuyển một phần delivery qua boundary tổ chức

Thu mua (procurement / 조달) tạo một interface giữa buyer và seller. Contract phân phối scope, price, schedule và risk giữa hai bên. Vì incentive hai bên không hoàn toàn giống nhau, contract design ảnh hưởng behavior.

Procurement không chỉ là purchasing. Nó gồm make-or-buy, solicitation, selection, contracting, performance control, change/claim và closure.

## Principal–agent problem và information asymmetry

Buyer thường không quan sát trực tiếp toàn bộ effort, quality hay internal constraint của seller; seller cũng không hiểu đầy đủ business consequence phía buyer. Đây là information asymmetry.

Contract và governance cố align behavior bằng acceptance, milestone, reporting, audit right, incentive và liability. Nhưng không contract nào mô tả hết mọi future state. Vì vậy procurement luôn là combination của formal agreement và relationship/governance mechanism.

Nếu buyer chỉ dựa vào trust, material issue có thể bị che. Nếu buyer cố contract hóa mọi micro-action, transaction cost và adversarial behavior tăng. Design tốt cân evidence, autonomy và consequence.

## Make-or-buy và total cost

Make-or-buy không chỉ so hourly rate. Outsourcing có transaction cost: vendor selection, contract, integration, knowledge transfer, security, oversight và exit cost. Internal development có opportunity cost và capacity constraint.

Một vendor rẻ hơn 20% nhưng lock-in cao, SLA yếu và knowledge transfer kém có thể đắt hơn trong lifecycle.

Decision cũng cần strategic capability. Outsource một commodity khác outsource core knowledge tạo competitive advantage.

Make-or-buy còn thay đổi future option. Nếu internal capability bị mất sau nhiều năm outsource, switching back không miễn phí. Total cost phải nhìn cả capability erosion và dependency concentration.

## Risk allocation: giao risk cho bên có khả năng quản lý

Contract không nên chỉ “đẩy càng nhiều risk sang seller càng tốt”. Seller sẽ price risk họ không kiểm soát được hoặc phản ứng bằng exclusion/change claim. Risk allocation hiệu quả giao exposure cho party có capability kiểm soát cause tốt nhất và có incentive phù hợp.

Ví dụ buyer kiểm soát requirement approval thì delay do buyer approval khó hợp lý nếu hoàn toàn chuyển sang seller. Seller kiểm soát staffing thì capacity failure nên nằm nhiều hơn ở seller. Shared risk cần interface, trigger và decision rule rõ.

Poor risk allocation tạo risk premium, dispute và defensive behavior; nó không làm uncertainty biến mất.

## Contract type là incentive architecture

Fixed-price chuyển nhiều cost risk sang seller khi scope rõ, nhưng seller sẽ price uncertainty hoặc resist change. Cost-reimbursable phù hợp khi scope uncertain hơn nhưng buyer giữ nhiều cost risk và cần oversight. Time-and-materials linh hoạt nhưng cần cap/control để tránh spend không kiểm soát.

Không có contract type “tốt nhất” độc lập context. Cần hỏi ai kiểm soát risk tốt hơn và measurement nào có thể enforce.

Risk không thật sự biến mất khi “transfer” qua contract. Seller có thể chịu financial penalty nhưng buyer vẫn chịu business delay, reputation hoặc integration consequence.

## Fixed-price trong high uncertainty

Fixed-price/fixed-scope ở environment uncertainty cao có thể tạo adversarial behavior. Seller phải price risk hoặc kiếm margin qua change request; buyer cố chứng minh item nằm trong scope.

Nếu requirement chưa ổn định, contract theo increment, capacity hoặc outcome có thể align collaboration tốt hơn tùy procurement rules. Nhưng flexibility cần governance để không biến thành uncontrolled spend.

Một contract “fixed” vẫn cần change mechanism vì reality thay đổi. Không có mechanism không làm change biến mất; nó chỉ đẩy negotiation sang informal channel hoặc dispute.

## Statement of Work và acceptance boundary

Statement of Work (SOW / 작업명세서) hoặc procurement specification cần đủ rõ về deliverable, boundary, acceptance, schedule, responsibility và constraint.

Ambiguity bị trì hoãn không biến mất; nó thường quay lại thành claim. Acceptance criterion càng objective càng giảm dispute.

SOW nên nói rõ interface và buyer-provided dependency. Nếu seller deliver đúng phần mình nhưng buyer không cung cấp environment/data đúng hạn, project vẫn fail dù contract scope phía seller có vẻ clear.

## Seller selection không chỉ nhìn price

Selection có thể cân capability, technical approach, financial stability, security, delivery record, support model, total cost và strategic fit.

Weighted scoring giúp structure decision nhưng weight vẫn là judgment. Một matrix đẹp không cứu input bias hoặc vendor reference không được verify.

Selection còn phải hỏi failure mode: supplier này yếu nhất ở đâu, concentration risk nào tồn tại, exit có khả thi không và evidence nào chứng minh claim marketing của vendor.

## SLA, KPI và outcome

Service Level Agreement định nghĩa service expectation như availability, response time hoặc recovery. KPI theo dõi performance. Nhưng metric cần liên hệ business impact.

Vendor đáp SLA 99.9% nhưng outage luôn rơi đúng peak payment window có thể vẫn gây business pain lớn. Contract metric không thay operational reasoning.

SLA cũng có thể bị local optimization. Seller đạt response-time KPI bằng cách acknowledgement nhanh nhưng resolution chậm; buyer cần metric semantic rõ và counter-metric cho behavior không mong muốn.

## Vendor performance và relationship

Vendor management cần objective metrics, acceptance criteria, review cadence và escalation path. Payment milestone nên liên kết với deliverable/evidence có nghĩa, không chỉ “đã làm x% effort”.

Relationship tốt không có nghĩa bỏ contract. Contract cung cấp boundary; collaboration giúp solve problem bên trong boundary. Dùng penalty quá sớm có thể phá cooperation; không enforce khi material breach lại làm control vô nghĩa.

Review cadence nên khác nhau theo phase và risk. Weekly deep review trong stabilization có thể hợp lý nhưng thành overhead trong steady phase. Procurement governance cũng cần tailoring.

## Supplier financial/capacity health

Technical delivery tốt hôm nay không bảo đảm supplier còn capacity hoặc financial health sáu tháng sau. Critical procurement nên theo dõi signal như key-person turnover, subcontractor dependency, cash-flow stress, backlog overload hoặc repeated missed commitment.

Mục tiêu không phải quản trị nội bộ vendor thay họ, mà phát hiện early warning trước khi failure thành delivery issue.

## Procurement change và claim

Contract change cần formal mechanism. Verbal request có thể tạo disputed scope. Claim xuất hiện khi party bất đồng về compensation, time hoặc obligation.

PM nên giữ records, correspondence, approved change và acceptance evidence đủ tốt để dispute không phụ thuộc memory. Legal/procurement specialist cần được involve khi issue vượt authority.

## Claim anatomy: entitlement, causation và quantum

Một claim có chất lượng thường phải trả lời ba câu hỏi tách biệt. Entitlement hỏi contract có cho bên yêu cầu quyền được thêm tiền/thời gian hoặc relief hay không. Causation hỏi event được nêu có thật sự gây ra delay/cost đó không. Quantum hỏi nếu có entitlement và causation thì mức compensation/time extension hợp lý là bao nhiêu.

Nếu chỉ chứng minh “vendor đã gặp khó” nhưng không nối khó khăn đó với obligation cụ thể và impact đã đo được, claim yếu. Ngược lại, buyer cũng không nên từ chối claim chỉ vì outcome xấu nếu chính buyer đã thay requirement, trì hoãn approval hoặc không cung cấp dependency đúng cam kết.

Mental model này giúp project manager tránh biến claim thành tranh luận cảm tính. Contract language, event chronology, baseline, approved changes, contemporaneous records và impact analysis phải nối được với nhau.

## Delay analysis và concurrent cause

Delay không phải lúc nào cũng có một nguyên nhân. Buyer có thể chậm data access trong khi seller cũng chậm staffing. Nếu hai cause overlap, câu hỏi responsibility phức tạp hơn việc “ai trễ trước”.

Project manager không nên tự đóng vai legal expert, nhưng cần giữ schedule logic và evidence đủ tốt để specialist phân tích. Nếu baseline không đáng tin, actual dates không được ghi, hoặc change được thực hiện trước rồi mới document, dispute resolution trở nên đắt hơn nhiều.

Điểm quản lý quan trọng là preserve evidence khi event xảy ra, không reconstruct memory nhiều tháng sau.

## Negotiation: position khác interest

Position là điều một bên nói muốn, ví dụ “thêm 200 triệu” hoặc “không trả thêm”. Interest là concern phía sau: cash flow, margin protection, deadline, reputation, capacity hoặc future relationship.

Nếu chỉ bargaining trên position, negotiation dễ thành chia đôi con số. Nếu hiểu interest, có thể mở solution space: đổi milestone payment, giảm low-value scope, kéo dài schedule, tăng buyer-provided resource, chia sẻ risk hoặc đổi acceptance sequence.

Một negotiation tốt cần biết BATNA — phương án tốt nhất nếu không đạt agreement. BATNA yếu làm một bên dễ chấp nhận deal tệ; BATNA mạnh nhưng được đánh giá sai có thể dẫn tới bluff nguy hiểm. Project manager nên chuẩn bị objective, authority limit, tradeable variables, evidence và walk-away condition trước meeting.

## Dispute ladder và escalation proportionality

Không phải mọi disagreement cần legal escalation ngay. Một dispute ladder có thể đi từ working-level clarification → project-manager negotiation → commercial/procurement review → executive mediation → formal dispute mechanism theo contract.

Mục tiêu là giải ở level thấp nhất có đủ authority và expertise, nhưng không kéo dài informal discussion tới mức mất contractual notice deadline hoặc evidence. Collaboration và rights preservation phải song song.

Nếu contract yêu cầu notice trong 7 ngày, “giữ quan hệ nên chưa gửi notice” có thể vô tình làm mất quyền. Notice không nhất thiết là hành động thù địch; nó có thể là governance mechanism để hai bên cùng nhìn thấy issue sớm.

## Incentive gaming và metric design

Contract metric tạo behavior. Nếu vendor được thưởng theo số ticket đóng, họ có incentive chia ticket nhỏ hoặc đóng sớm. Nếu payment chỉ theo milestone date, quality debt có thể bị đẩy sang giai đoạn sau.

Metric tốt phải gần outcome, khó game và có counter-metric cho side effect. Ví dụ velocity không nên là commercial KPI nếu nó khuyến khích inflate story point. SLA availability có thể cần đi cùng severity, business-hour impact và recovery quality.

Mọi incentive đều tạo optimization pressure; procurement design cần hỏi “nếu supplier tối ưu đúng metric này, system behavior tệ nhất có thể là gì?”.

## Procurement ethics và conflict of interest

Vendor selection và negotiation dễ phát sinh conflict of interest, gift, confidential information leak hoặc favoritism. Ethics không phải lớp phụ bên ngoài commercial decision; nó bảo vệ tính legitimacy của decision và giảm legal/reputational risk.

Project manager nên disclose conflict, tách người đánh giá khi cần, giữ scoring evidence và không chia sẻ bid information không được phép. Một supplier tốt không nên được chọn bằng process yếu, vì process yếu làm decision khó defend khi audit hoặc dispute.

## Procurement risk và supply chain

Vendor có own vendor, geography, currency, regulation và capacity risk. Buyer không nên dừng analysis ở tier-1 supplier nếu critical component phụ thuộc single source.

Supply-chain mapping, alternate supplier hoặc buffer có thể giảm risk nhưng tạo cost. Procurement strategy là risk strategy.

Cần phân biệt redundancy thật với redundancy giả. Hai supplier khác tên nhưng cùng dùng một subcontractor hoặc cloud region không tạo independent fallback.

## Exit strategy và lock-in

Contract nên nghĩ về kết thúc từ đầu: data export, IP ownership, transition assistance, documentation, source code/escrow nếu relevant, account/access revocation và asset return.

Vendor lock-in không luôn xấu nếu benefit lớn, nhưng phải là decision có visibility. Hidden switching cost làm future organization mất option.

Exit strategy tốt phải được test ở mức phù hợp. “Có quyền export data” không đủ nếu format proprietary và chưa ai thử restore sang system khác.

## Procurement closure

Closure cần verify obligation, final acceptance, payment, claim resolution, asset/IP/data transfer và record retention.

Closed contract không đồng nghĩa vendor knowledge đã chuyển. Transition capability cần acceptance riêng nếu operation phụ thuộc nó.

## Quality và procurement nối nhau tại acceptance

Outsourced deliverable vẫn phải đáp project quality requirement. Contract acceptance criterion là bridge giữa procurement và quality.

Nếu buyer chỉ specify schedule/price mà quality vague, conflict gần như được thiết kế vào contract. Nếu quality requirement unrealistic hoặc không testable, seller cũng không thể price risk đúng.

Acceptance còn phải phân biệt conditional acceptance và final acceptance. Chấp nhận deliverable với open defect có thể hợp lý nếu risk được hiểu và owner rõ, nhưng nếu exception biến thành default thì buyer tích quality debt và mất leverage commercial.

## Ví dụ scenario

Vendor thông báo delay hai tuần vì third-party API. PM không nên lập tức “ép vendor tăng người”. Trước hết cần kiểm tra contract responsibility, dependency, critical path, alternative/workaround, root cause, service credit/claim nếu relevant và collaborative recovery plan. Contract cho quyền; relationship và system reasoning quyết định cách dùng quyền đó.

Nếu vendor cho rằng buyer thay API specification muộn và yêu cầu extension 10 ngày cùng 80 triệu chi phí, PM không nên tranh luận ngay về con số 80. Cần tách entitlement, causation và quantum: change nào được yêu cầu, ai authorize, change nằm ngoài SOW không, nó tác động critical path thế nào, cost evidence là gì, và có concurrent seller delay hay không. Khi evidence rõ, negotiation mới có solution space thực.

Một scenario quality: UAT phát hiện nhiều defect nhưng tất cả tập trung ở requirement thay đổi muộn. Chỉ yêu cầu QA tăng regression test không đủ. Team cần inspect change process, acceptance clarity và integration timing, vì quality failure có upstream cause.

Một scenario resource: ba project cùng lập plan dùng một security architect 50% trong cùng tháng. Mỗi plan riêng đều “đủ resource”, nhưng tổng demand là 150%. Project manager không thể giải bằng motivational talk; organization cần portfolio priority, schedule shift hoặc capability redundancy.

## Mental model

> Quality bảo vệ fitness for purpose bằng process capability và evidence; resource management bảo vệ effective capacity thay vì headcount danh nghĩa; procurement mở rộng project system qua organizational boundary và vì thế phải thiết kế risk allocation, incentive, evidence, negotiation mechanism và exit path rõ ràng.

Tiếp theo: [Risk, uncertainty, issue và decision making](./08_risk_uncertainty_issues_and_decisions.md).