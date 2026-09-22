# 09 — Governance, compliance và business environment

## Governance là hệ thống quyền quyết định

Quản trị (governance / 거버넌스) xác định decision rights, accountability, policy, reporting, control và escalation. Nó trả lời: ai có quyền phê duyệt điều gì, threshold nào cần escalate, evidence nào phải có, và ai chịu trách nhiệm cho outcome.

Management vận hành bên trong boundary đó. Governance yếu làm project hoặc tê liệt vì mọi thứ phải xin phép, hoặc nguy hiểm vì không ai rõ authority.

Governance tốt không cố quyết mọi việc ở cấp cao nhất. Nó phân loại decision theo impact, reversibility và risk, rồi đặt quyền quyết định ở level thấp nhất vẫn bảo vệ được organization.

## Governance là decision architecture, không chỉ committee

Một governance operating model cần ít nhất decision type, decision owner, input/evidence, threshold, cadence, escalation path và record. Committee chỉ là một implementation option.

Nếu decision owner rõ nhưng evidence tới quá chậm, governance vẫn fail. Nếu meeting xảy ra đúng lịch nhưng không ai có authority commit, governance chỉ tạo ceremony. Nếu team có authority nhưng threshold không rõ, decision dễ bị escalated quá mức hoặc giữ quá lâu.

Một design tốt cố tối thiểu hóa tổng cost gồm risk của decision sai và latency/overhead của decision process. Governance quá nhẹ tăng uncontrolled risk; governance quá nặng tạo queue, workaround và shadow decision.

## Governance khác bureaucracy

Một control chỉ có ý nghĩa khi nó giảm risk hoặc tạo information cần cho decision. Stage gate có thể phù hợp trước khi bỏ vốn lớn hoặc go-live regulated system. Nhưng nếu mỗi change nhỏ đều cần board meeting hai tuần một lần, governance tạo queue và làm response chậm.

Tailoring governance nghĩa giữ control objective nhưng điều chỉnh mechanism. Có thể tự động hóa evidence, đặt threshold theo risk hoặc delegate approval cho reversible decision.

Một cách audit governance đơn giản là hỏi mỗi control đang bảo vệ failure mode nào. Nếu không ai trả lời được, control có thể đã biến thành ritual. Ngược lại, bỏ một control mà không hiểu failure mode phía sau có thể tạo risk lớn hơn overhead đã tiết kiệm.

## Governance debt

Governance debt xuất hiện khi temporary shortcut trong authority, approval hoặc evidence không được retire. Ví dụ emergency cho phép team deploy bằng verbal approval; nếu exception đó tiếp tục thành habit, organization mất traceability và boundary chính thức.

Debt cũng xuất hiện khi policy/threshold không được update dù operating context đổi. Team khi đó phải workaround rule outdated, làm shadow process lớn dần.

Giống technical debt, governance debt có thể hợp lý trong emergency nếu visible, owner rõ và repayment date có thật. Hidden permanent exception mới nguy hiểm.

## Decision queue và governance latency

Mọi governance body có capacity hữu hạn. Nếu quá nhiều item phải chờ cùng một sponsor, architect hoặc committee, queue tạo latency. Latency có thể lớn hơn thời gian thực hiện work sau approval.

Một system tốt theo dõi không chỉ số decision mà còn age của pending decision, materiality và cost of delay. Delegation, standing guardrail hoặc asynchronous approval có thể giảm queue mà không bỏ control objective.

Nếu team liên tục bắt đầu work “at risk” vì approval đến quá chậm, vấn đề không chỉ là discipline của team; governance design có thể đang không đáp ứng cadence của delivery system.

## Sponsor, project manager và governance body

Sponsor thường sở hữu business justification, bảo trợ project ở cấp tổ chức và hỗ trợ decision vượt authority của project manager. Project manager điều phối delivery trong boundary được trao. Governance body như steering committee hoặc change control board xử lý decision theo threshold đã định.

Điểm quan trọng không phải title mà là decision right. Nếu sponsor chịu accountability về business outcome nhưng không có thời gian hoặc authority để giải quyết escalated issue, project đang có governance gap.

Một escalation tốt nên nêu decision cần đưa ra, option, impact, recommendation và deadline. Chỉ gửi “có vấn đề” làm governance body phải tự tái tạo toàn bộ analysis.

## Sponsor attention là resource khan hiếm

Sponsor không thể tham gia mọi detail. Project manager cần bảo vệ sponsor attention bằng cách escalate material decision, không phải mọi status issue.

Escalation packet tốt giảm cognitive load: current state, why it matters, options, recommendation, deadline và consequence nếu không quyết. Nếu sponsor phải đọc 40 trang để hiểu câu hỏi, latency dễ tăng.

Ngược lại, PM che bad news để “không làm phiền sponsor” có thể làm sponsor chỉ biết problem khi option đã biến mất. Attention management không phải information suppression.

## PMO và organizational governance

Project Management Office (PMO / 프로젝트 관리 조직) có thể cung cấp standard, assurance, portfolio alignment, reporting hoặc trực tiếp quản lý project tùy organization. PMO không mặc định là bureaucracy; giá trị của nó nằm ở việc giảm duplicate learning, chuẩn hóa control cần thiết và tạo visibility xuyên project.

PMO yếu có thể tập trung vào template compliance hơn outcome. PMO mạnh giúp organization phân biệt variance bình thường với systemic risk, dùng historical data tốt hơn và hỗ trợ project manager khi issue vượt boundary một project.

## PMO operating model: support, control hay delivery

Không có một PMO duy nhất cho mọi organization. Supportive PMO tập trung coaching, template, community of practice và data. Controlling PMO đặt standard, assurance, gate và compliance. Directive PMO có thể trực tiếp sở hữu hoặc điều hành project/program.

Ba mode này không phải maturity ladder. Một regulated bank có thể cần control mạnh; một product organization nhỏ có thể cần enablement nhiều hơn. Vấn đề xuất hiện khi authority thực tế và expectation không khớp: PMO bị yêu cầu chịu accountability nhưng không có decision right, hoặc có quyền gate nhưng không chịu consequence của decision latency.

PMO nên đo value của mình bằng organizational outcomes như decision speed, forecast quality, delivery predictability, reuse of learning và systemic risk visibility hơn là số template được điền đúng hạn.

## Assurance cần đủ độc lập để challenge

Project team có incentive tự nhiên muốn chứng minh mình on track. Vì vậy một số decision high-consequence cần independent challenge hoặc assurance: security review, audit, architecture review, commercial review hoặc health check.

Independence không có nghĩa reviewer không hiểu context. Reviewer quá xa reality dễ tạo checkbox control; reviewer quá embedded có thể mất objectivity. Governance phải cân challenge quality với delivery context.

Assurance tốt hỏi evidence và assumption, không chỉ “đã điền template chưa?”.

## Project, program và portfolio nối nhau qua dependency và capital allocation

Project tạo một change cụ thể. Program phối hợp nhiều project/operation liên quan để tạo benefit mà từng project riêng lẻ khó tối ưu. Portfolio chọn và cân investment để phù hợp strategy, capacity và risk appetite.

Boundary này quan trọng vì một project có thể “xanh” nhưng program thất bại. Ví dụ app mobile hoàn thành đúng plan nhưng identity platform trong project khác chưa sẵn sàng, nên benefit toàn program chưa xuất hiện. Local optimization ở từng project không đảm bảo system outcome.

Portfolio cũng có thể dừng một project khỏe nếu capital cần chuyển sang opportunity có strategic value cao hơn. Với project manager, điều này có thể khó chấp nhận nếu chỉ nhìn delivery metrics. Governance cấp portfolio hỏi một câu khác: đây còn là nơi tốt nhất để đầu tư nguồn lực khan hiếm không?

## Portfolio WIP và capacity

Portfolio có thể overcommit giống team. Nếu organization khởi động 30 initiative nhưng chỉ có capacity thực cho 15, mỗi project nhận resource không ổn định, decision body quá tải và change saturation tăng.

Portfolio WIP cao làm cycle time của strategic change dài hơn. Giảm số initiative active có thể tăng throughput hoàn thành dù nhìn bề ngoài organization “làm ít thứ hơn”. Đây là same flow logic ở [Schedule & Flow](./05_schedule_estimation_and_flow.md), nhưng áp dụng ở cấp investment.

Portfolio governance vì vậy không chỉ chọn project tốt; nó quyết định bao nhiêu work có thể được active đồng thời mà system vẫn giữ focus và absorption capacity.

## Incremental funding và progressive commitment

Một initiative uncertainty cao không nhất thiết cần full funding ngay từ đầu. Governance có thể cấp discovery tranche, sau đó tăng commitment khi evidence tốt hơn.

Incremental funding tạo option stop/pivot trước irreversible spend lớn. Nhưng nếu mỗi tranche approval quá nhỏ và chậm, transaction cost có thể phá flow. Progressive commitment cần threshold phù hợp với size/risk, không micro-approve mọi expense.

Đây là portfolio equivalent của stage-gate/real-options thinking ở chapter Lifecycle và Risk.

## Cross-project dependency và shared constraint

Program/portfolio governance cần thấy dependency xuyên project: shared vendor, environment, data migration, regulatory approval, specialist hoặc business owner. Nếu mỗi project forecast độc lập, cùng một resource có thể bị allocate 200% trên giấy.

Dependency cần owner, required-by date, supplying project, consuming project và escalation path. Một dependency “được biết” nhưng không có decision mechanism vẫn là unmanaged risk.

Shared constraint cũng làm risk correlated. Năm project dùng cùng vendor không phải năm exposure độc lập. Đây là điểm nối với [Risk, uncertainty và decision](./08_risk_uncertainty_issues_and_decisions.md).

## Portfolio governance và kill/pause/pivot decision

Governance trưởng thành không chỉ approve start; nó cũng có khả năng pause, pivot hoặc terminate khi evidence thay đổi. Nếu mọi project chỉ được phép “continue”, portfolio review trở thành reporting ritual.

Decision nên xem sunk cost là history, không phải lý do tiếp tục. Các câu hỏi quan trọng hơn là remaining investment, expected future value, strategic alignment, opportunity cost, risk và reversibility.

Một project bị terminate không nhất thiết là failure của PM. Có thể đó là evidence rằng governance học sớm trước khi đốt thêm capital.

## Strategic alignment drift

Project có thể vẫn đúng charter ban đầu nhưng strategy đã đổi. Merger, regulation, market shock hoặc new platform có thể làm initiative ít value hơn mà delivery metrics không phản ánh.

Alignment vì vậy cần được reassess ở material trigger, không chỉ annual planning. Nếu project purpose không còn nối strategy, “on scope/on budget” không phải lý do đủ để tiếp tục.

Strategic drift cũng có thể theo hướng ngược: một project từng optional trở thành critical vì regulation hoặc competitor event. Governance cần có ability reprioritize, không khóa toàn portfolio theo ranking cũ.

## Compliance là constraint không thể “trade-off tùy ý”

Tuân thủ (compliance / 컴플라이언스) đến từ law, regulation, industry standard, contract, policy hoặc internal control. Project phải xác định requirement, owner, evidence, timing và consequence của noncompliance.

Security, privacy, health & safety và sustainability có thể tạo requirement xuyên suốt lifecycle. Nếu compliance review chỉ được gọi ở cuối, rework thường rất đắt. “Shift left” trong project context nghĩa đưa constraint vào requirement/design/planning đủ sớm.

Compliance requirement cần được chuyển thành testable evidence. “Đảm bảo privacy” quá mơ hồ; “PII được mã hóa at rest, retention theo policy X và access được log” tạo boundary có thể verify. Đây là điểm nối giữa governance và quality.

## Policy hierarchy và conflict

Project có thể chịu nhiều rule: law, regulation, contract, corporate policy, architecture standard, project working agreement. Chúng không có cùng authority.

Khi hai requirement conflict, team không nên tự chọn rule dễ hơn. Cần biết hierarchy, interpretation owner và exception mechanism. Internal policy có thể có exception; law thường không thể được override bằng sponsor approval.

Làm rõ source/authority của constraint giúp scenario reasoning tránh lỗi “manager đã approve nên được phép”.

## Compliance by design thay vì compliance at gate

Nếu mandatory control chỉ được kiểm tra ở cuối, project đang biến compliance thành inspection. Compliance by design đưa requirement, evidence capture và review vào lifecycle sớm.

Ví dụ data retention requirement ảnh hưởng architecture, database lifecycle, vendor contract và test evidence. Nếu chỉ hỏi privacy team hai ngày trước go-live, cost-of-change rất cao.

Gate cuối vẫn cần, nhưng role của nó nên xác nhận accumulated evidence chứ không khám phá lần đầu requirement critical.

## Evidence chain và auditability

Một control chỉ đáng tin khi có evidence chain. Requirement nào áp dụng? Ai phê duyệt interpretation? Control nào được implement? Test nào chứng minh control hoạt động? Exception nào đã được chấp nhận và bởi ai?

Traceability không nhất thiết phải là spreadsheet lớn. Trong software project, chain có thể đi từ regulatory requirement → backlog/control → code/configuration → test evidence → release approval. Mục tiêu là reconstruct reasoning khi audit hoặc incident xảy ra.

## Materiality và proportional control

Không phải mọi deviation có cùng materiality. Một typo trong internal note khác với privacy control missing. Governance cần threshold dựa trên consequence, exposure và reversibility.

Nếu mọi deviation được xử lý bằng cùng escalation, system quá tải. Nếu materiality bị hiểu là “issue nhỏ nên bỏ qua” mà không có rule, hidden risk tích tụ. Proportionality cần explicit boundary.

## Exception management

Thực tế có lúc project không thể đáp ứng một internal standard đúng thời điểm. Khi đó exception không nên được “nói miệng cho qua”. Cần document scope, rationale, compensating control, owner, expiry date và authority chấp nhận residual risk.

Nếu exception không có expiry hoặc review, temporary deviation dễ trở thành permanent hidden debt.

Exception register cũng nên theo dõi concentration. Mười exception nhỏ trên cùng control area có thể tạo systemic weakness dù từng exception riêng nằm dưới threshold.

## Organizational Process Assets và Enterprise Environmental Factors

Organizational Process Assets (OPA) gồm template, policy, historical data, lessons learned và process nội bộ mà project có thể dùng. Enterprise Environmental Factors (EEF) là environment project phải hoạt động trong đó: culture, structure, market, regulation, technology, resource availability.

Không cần học thuộc category nếu mental model rõ: OPA phần lớn là knowledge/process asset có thể tận dụng; EEF là context tạo constraint/opportunity và thường không do project tự kiểm soát.

OPA chỉ có giá trị nếu được cập nhật từ learning thực tế. Template cũ không phản ánh incident hoặc technology mới có thể gây false confidence. Project manager nên reuse knowledge nhưng vẫn kiểm tra relevance.

## Organizational structure và authority

Functional organization giữ authority chủ yếu ở functional managers. Projectized organization trao authority mạnh hơn cho project manager. Matrix nằm giữa và có weak/balanced/strong variants.

Cấu trúc ảnh hưởng tốc độ resource allocation, escalation và conflict. Một PM trong weak matrix không thể hành xử như có full authority; influence và sponsor support trở nên quan trọng hơn.

Trong matrix, conflict resource thường không giải được chỉ bằng “ưu tiên project”. Functional manager tối ưu capability dài hạn, project manager tối ưu temporary delivery. Governance phải cung cấp mechanism để giải trade-off thay vì để hai phía tranh quyền không chính thức.

## Business environment là moving target

External environment gồm regulation, market, technology, competition, geopolitics, supply chain và social expectation. PMP 2026 tăng trọng số Business Environment vì project manager ngày càng phải nối delivery với business context chứ không chỉ internal process.

Environmental scanning không có nghĩa PM dự đoán mọi trend. Nó nghĩa có mechanism để phát hiện change có thể làm business case, scope/backlog hoặc risk profile thay đổi.

Trigger có thể là regulation draft mới, competitor release, FX movement, vendor acquisition hoặc strategic priority change. Một project khỏe phải có khả năng hỏi lại “business case còn đúng không?” thay vì coi charter ban đầu là chân lý bất biến.

## Environmental signal, trigger và response horizon

Không phải mọi external signal cần change ngay. Team cần phân biệt weak signal, confirmed trigger và material effect.

Một regulation draft có thể cần scenario analysis; regulation finalized có thể trigger requirement change; enforcement date quyết response horizon. Phản ứng quá sớm với noise tạo churn, phản ứng quá muộn với signal rõ tạo surprise.

Environmental scanning tốt nối signal → possible impact → owner → decision trigger. “Theo dõi thị trường” mà không có threshold không tạo actionability.

## Business case cần sống trong suốt project

Business case không chỉ dùng để xin budget. Khi cost tăng mạnh, market thay đổi hoặc expected benefit giảm, project cần reassess viability. Continuing chỉ vì đã đầu tư nhiều là sunk-cost trap.

Project manager có thể không có authority hủy project, nhưng phải surface evidence khi expected value thay đổi đáng kể. Governance body cần quyết định continue, pivot, pause hoặc terminate.

## Benefits ownership

Project tạo capability nhưng benefit thường xuất hiện sau delivery. Vì vậy cần business owner chịu trách nhiệm cho adoption và benefit realization. Nếu không có owner sau closure, organization có thể hoàn thành output nhưng không ai theo dõi outcome.

Một benefit map nối output → capability → behavior change → measurable outcome giúp xác định assumption nào nằm ngoài control trực tiếp của project nhưng vẫn phải được quản lý như dependency.

## Benefit dependency network

Benefit hiếm khi đến từ một output duy nhất. Revenue uplift có thể cần system capability, sales training, pricing change, marketing và operations capacity. Nếu một dependency không thuộc project nhưng không có owner, benefit model có hidden gap.

Benefit network nên cho thấy dependency, owner và assumption. Điều này giúp governance phân biệt “project delivered” với “investment value realized”.

Nếu multiple projects cùng claim một benefit, portfolio cần tránh double-count. Attribution logic phải consistent với business case.

## Benefits realization không kết thúc ở project closure

Closure chỉ xác nhận project work đã hoàn thành và transition đã xảy ra. Benefit có thể cần nhiều tháng hoặc năm mới materialize. Vì vậy benefits realization plan cần owner, metric, baseline, target, measurement cadence và trigger review sau project.

Nếu benefit phụ thuộc adoption, process redesign hoặc sales behavior, các activity đó phải được nối vào operating model sau handover. Một project đóng đúng quy trình nhưng không có post-project measurement đang bỏ mất feedback loop cuối cùng của investment.

Governance cũng cần phân biệt benefit không xuất hiện vì project output kém với benefit không xuất hiện vì assumption business sai. Hai nguyên nhân dẫn tới learning khác nhau.

## Organizational change

Project tạo output, nhưng organization cần hấp thụ thay đổi. Change management quan tâm readiness, sponsor coalition, communication, training, resistance và reinforcement. Một system mới không tạo outcome nếu user tiếp tục dùng workaround cũ.

Project manager không nhất thiết sở hữu toàn bộ organizational change management, nhưng phải tích hợp dependency đó vào success model và transition.

Resistance không phải lúc nào cũng “người dùng chống thay đổi”. Nó có thể là signal rằng process mới tăng workload, incentive không phù hợp hoặc stakeholder không tin data. Treat resistance như information giúp design intervention tốt hơn.

## Change readiness: ability, willingness và environment

Readiness không chỉ là “đã training”. Người dùng có thể biết cách dùng hệ thống nhưng không muốn dùng vì incentive cũ vẫn thưởng behavior cũ. Hoặc họ muốn dùng nhưng process, permission hay manager expectation không cho phép.

Có thể reasoning readiness qua ba lớp: ability—người dùng có skill/capability không; willingness—họ hiểu purpose, tin change và thấy incentive hợp lý không; environment—tool, policy, workload và management reinforcement có hỗ trợ behavior mới không.

Nếu một trong ba lớp fail, communication campaign mạnh hơn chưa chắc sửa được adoption.

## Reinforcement và regression về behavior cũ

Ngay sau go-live, novelty và project-team support có thể làm adoption cao tạm thời. Khi hypercare kết thúc, user có thể quay lại workaround cũ nếu incentive, manager behavior hoặc process không reinforce change.

Vì vậy adoption cần theo dõi sau transition, không chỉ launch week. Sustainable change cần local manager reinforcement, removal of old path khi phù hợp và feedback loop để friction được sửa.

Không phải lúc nào cũng nên tắt old process ngay; nếu new system chưa stable, parallel run có thể là risk control. Nhưng old path không có retirement plan sẽ làm dual process thành permanent complexity.

## Change saturation và portfolio effect

Một team có thể chịu nhiều initiative cùng lúc: ERP mới, org restructure, compliance training và office relocation. Mỗi project riêng lẻ nhìn change impact “vừa phải”, nhưng tổng tải thay đổi lên cùng population có thể vượt absorption capacity.

Đây là change saturation. Portfolio governance cần nhìn shared stakeholder load, training calendar, blackout period và operational peak. Nếu không, project manager có thể đổ lỗi cho “resistance” trong khi organization đơn giản là không còn bandwidth để hấp thụ thêm change.

Change saturation là ví dụ điển hình cho system effect không nhìn thấy khi quản lý từng project riêng lẻ.

## Adoption metric phải đo behavior, không chỉ activity

Training attendance, email open rate hoặc số guide được gửi là activity metric. Adoption cần measure behavior hoặc outcome: tỷ lệ transaction đi qua process mới, active users, workaround rate, error rate, cycle time hoặc benefit indicator.

Một rollout có 100% training completion nhưng 40% user quay lại spreadsheet cũ chưa thể coi là successful adoption.

Measurement nên segment theo role, location hoặc cohort để tìm nơi intervention cần khác nhau.

## Transition và operating model

Handover tốt không chỉ chuyển document. Operation cần role, support model, incident path, access, monitoring, budget, vendor contact, SLA, ownership và improvement backlog.

Nếu project team rời đi nhưng không ai có authority/capacity vận hành capability mới, project chỉ chuyển risk sang operations.

Transition readiness vì vậy là acceptance criterion của system vận hành, không phải administrative checklist cuối project.

## Ethics và professional responsibility

Ethics không phải chỉ tránh hành vi trái luật. Project manager thường đứng giữa pressure giao hàng và obligation về safety, truthfulness, fairness hoặc confidentiality. Reporting một forecast xấu trung thực có thể khó về chính trị nhưng che giấu dữ liệu làm governance mất chức năng.

Khi conflict of interest hoặc pressure vượt authority, escalate qua channel phù hợp và giữ evidence. “Sponsor muốn vậy” không tự động biến hành động thành acceptable.

Professional judgment cũng yêu cầu phân biệt confidentiality với concealment. Không chia sẻ sensitive data bừa bãi là đúng; giấu risk material khỏi người có quyền quyết định là governance failure.

## Speaking truth to power là control mechanism

Governance chỉ hoạt động nếu bad news có thể đi lên. Nếu incentive trừng phạt người báo variance nhưng thưởng dashboard xanh, information system sẽ tự làm đẹp số liệu.

PM cần trình bày material fact, uncertainty và recommendation rõ ràng, ngay cả khi message không thuận political expectation. Điều này không có nghĩa confrontational; có thể communicate bằng evidence, option và consequence.

Một organization trưởng thành phân biệt messenger khỏi problem. Nếu không, silence trở thành rational behavior của team và governance mất sensor.

## Governance failure modes

Một failure mode là decision latency: authority tồn tại nhưng approval quá chậm nên team tạo workaround. Failure mode khác là shadow governance: decision thật xảy ra trong chat riêng còn meeting chỉ hợp thức hóa. Một dạng khác là metric gaming: report được tối ưu để trông xanh thay vì phản ánh state thật.

Khi governance tạo incentive che bad news, organization mất early warning. Governance tốt phải thưởng transparency đủ để problem được thấy trước khi trở thành crisis.

Ở level portfolio, failure mode còn là zombie project: initiative không còn value rõ nhưng không ai muốn terminate vì political cost. Một dạng khác là resource illusion: cùng specialist được allocate cho nhiều project mà mỗi plan đều giả định 100% availability. PMO/portfolio governance phải surface những conflict này thay vì chỉ consolidate dashboard.

Governance cũng có thể fail vì policy collision, assurance theater, exception accumulation hoặc committee without authority. Những failure này khác nhau nhưng đều phá link giữa evidence và action.

## Ví dụ scenario

Một product sắp go-live nhưng privacy review chưa hoàn tất. Business nói delay sẽ mất campaign. PM không nên tự bỏ control hoặc chỉ “để security quyết”. Cần xác định policy/regulatory requirement, risk/authority, available compensating control, deadline, approver hợp lệ và escalation. Nếu compliance là mandatory gate, business pressure không thay đổi requirement; nó chỉ thay urgency của resolution.

Giả sử review phát hiện một control internal chưa đủ nhưng law vẫn được đáp ứng. Khi đó governance có thể cho phép exception có thời hạn với compensating monitoring nếu authority phù hợp chấp nhận residual risk. Nhưng nếu legal requirement bị vi phạm, cùng cơ chế exception nội bộ không thể hợp pháp hóa release.

Một scenario portfolio: project A và B đều cần cùng specialist database trong tháng 11 và cả hai report “on track”. PMO phát hiện capacity chỉ đủ cho một. Câu hỏi không phải ép specialist overtime để giữ hai dashboard xanh; portfolio governance phải xem strategic priority, dependency, delay cost, alternative resource và sequencing rồi đưa trade-off lên đúng decision level.

Một scenario change: rollout mới đạt 100% training completion nhưng adoption chỉ 55%. Thay vì tổ chức thêm cùng một khóa training cho toàn bộ user, team cần segment data và tìm failure layer. Nếu một nhóm không có permission, đây là environment problem; nếu manager vẫn yêu cầu spreadsheet cũ, đây là reinforcement/incentive problem; nếu user không hiểu workflow, mới là capability/training problem.

Một scenario governance: architecture board họp hai tuần một lần, nhưng sprint cần decision interface trong ba ngày. Team liên tục implement trước rồi xin approve sau. Chỉ nhắc team “tuân thủ quy trình” không sửa root cause. Governance cần threshold/delegation hoặc faster review path để control cadence match delivery cadence.

## Mental model

> Governance là kiến trúc biến evidence thành quyết định có authority; portfolio governance phân bổ capital, capacity và attention; compliance bảo vệ non-negotiable boundary; organizational change biến capability thành behavior bền vững. Governance tốt không tối đa control—nó tối ưu control quality, decision latency và accountability cùng lúc.

Tiếp theo: [Agile, adaptive và hybrid delivery](./10_agile_hybrid_and_adaptive_delivery.md).