# 02 — People: leadership, team, conflict và empowerment

## Project system là socio-technical system

Kế hoạch tốt không tự thực thi. Project tồn tại qua con người có mục tiêu, incentive, expertise và giới hạn khác nhau. Vì vậy domain People không phải “soft skill phụ trợ” cho process; nó là cơ chế để coordination xảy ra.

Lãnh đạo (leadership / 리더십) khác authority. Authority đến từ vị trí hoặc governance; leadership là khả năng tạo direction, alignment và điều kiện để nhóm tự thực hiện công việc tốt. Một project manager có formal authority nhưng không có trust vẫn có thể bị stakeholder trì hoãn hoặc team chỉ “comply” tối thiểu.

Project team nên được nhìn như một network của decision, information và dependency. Người nào biết gì, ai có quyền quyết, ai chịu hậu quả và signal mất bao lâu để tới đúng người quyết định thường quan trọng hơn sơ đồ tổ chức chính thức.

## Leadership là thiết kế môi trường ra quyết định

Một leader không tạo value bằng cách tự quyết mọi thứ. Leader tạo context để những người gần problem nhất có thể quyết đúng trong boundary phù hợp.

Điều này gồm làm rõ outcome, non-negotiable constraint, decision right, escalation threshold, source of truth và cách disagreement được xử lý. Nếu thiếu các yếu tố này, “trao quyền” dễ biến thành ambiguity.

Leadership tốt giảm số decision phải đi qua leader mà không làm giảm coherence. Đây là khác biệt giữa **decentralization có thiết kế** và “mọi người tự làm theo cách mình muốn”.

## Shared vision giảm coordination cost

Shared vision không phải khẩu hiệu. Nó là một model chung về outcome, priority và success. Khi vision đủ rõ, nhiều quyết định nhỏ có thể được decentralize. Nếu mọi quyết định đều phải hỏi project manager, bottleneck thường không chỉ do team thiếu năng lực mà do context hoặc decision boundary không rõ.

Ví dụ: “phát hành đúng ngày” có thể xung đột với “không được có defect severity-1”. Nếu priority chưa rõ, developer, QA và sponsor có thể tối ưu khác nhau ngay trước release. Shared vision cần đi kèm trade-off rule.

Direction tốt thường gồm outcome, non-negotiable constraint, priority rule và success evidence. Khi bốn thứ này rõ, team có thể tự xử lý nhiều local decision mà không cần chờ approval.

## Shared mental model quan trọng hơn shared slogan

Hai người đều nói “customer first” nhưng một người hiểu là release nhanh, người khác hiểu là không chấp nhận bất kỳ defect nào. Slogan giống nhau không đảm bảo mental model giống nhau.

Shared mental model cần đủ cụ thể để dự đoán decision của nhau. Nếu developer biết QA sẽ reject build nào, product owner biết constraint nào không thương lượng và operations biết khi nào cần escalation, coordination cost giảm mạnh.

Working agreement, acceptance criteria, decision rule và architecture boundary đều là cách externalize shared mental model.

## Empowerment và accountability

Trao quyền (empowerment / 권한 부여) nghĩa là đưa decision gần nơi có information nhất, trong boundary phù hợp. Nó không đồng nghĩa bỏ kiểm soát. Một team empowered vẫn cần objective, constraint, escalation threshold và transparency.

Accountability (trách nhiệm giải trình / 책임성) là counterpart của empowerment. Người được trao quyền phải có information và chịu trách nhiệm giải thích decision/outcome. Micromanagement làm giảm ownership; empowerment không boundary lại tạo decision inconsistency.

Một nguyên tắc hữu ích là quyền quyết định nên đi cùng ba thứ: information, competence và consequence visibility. Nếu người ra quyết định không thấy hậu quả tới system khác, local optimization rất dễ xảy ra.

## Delegation failure có hai cực

Undelegation xảy ra khi leader giữ mọi decision dù team đủ capability. Kết quả là queue approval, decision latency và learned helplessness.

Over-delegation xảy ra khi leader chuyển decision nhưng không chuyển context, authority hoặc resource. Team “được trao quyền” nhưng vẫn không thể đổi priority, access budget hoặc yêu cầu stakeholder phản hồi.

Delegation tốt cần answer: decision nào được giao, boundary nào không được vượt, information nào cần nhìn, khi nào phải escalate và outcome nào người nhận accountable.

## Decision rights nên phân theo reversibility và consequence

Một reversible decision ít hậu quả có thể nằm gần team. Một irreversible decision có legal, safety hoặc financial exposure cần governance mạnh hơn.

Mental model:

```text
reversible + low consequence → decentralize nhiều hơn
irreversible + high consequence → evidence + review + authority cao hơn
```

Điều này tránh hai lỗi: micro-manage mọi chi tiết và trao quyền vô điều kiện cho decision vượt risk tolerance.

## Authority gradient và escalation friction

Không chỉ cần biết “ai có quyền quyết”; cần biết **độ dốc authority** giữa nơi phát hiện problem và nơi có quyền xử lý nó. Nếu một engineer phát hiện issue trong vài phút nhưng phải đi qua bốn tầng management để xin một thay đổi nhỏ, project có authority gradient quá dốc so với tốc độ của work.

Escalation luôn có friction: chuẩn bị context, chờ lịch, giải thích lại problem và mất information qua mỗi handoff. Vì vậy escalation không miễn phí. Nhưng loại bỏ escalation hoàn toàn cũng nguy hiểm khi decision vượt competence hoặc consequence boundary. Thiết kế tốt đặt authority đủ gần nơi có information, đồng thời giữ một đường escalation ngắn cho exception có impact lớn.

Một dấu hiệu architecture kém là **shadow authority**: trên giấy team được quyền quyết, nhưng thực tế mọi người vẫn chờ một senior leader “gật đầu” vì sợ hậu quả chính trị. Khi đó RACI hay delegation matrix đúng trên tài liệu nhưng behavior không đổi. PM phải quan sát decision thực tế đi qua đâu, không chỉ đọc governance chart.

## Power, influence và authority không giống nhau

Stakeholder power có thể đến từ formal role, expertise, resource control, network hoặc khả năng làm chậm decision. Project manager cần hiểu influence map thay vì giả định org chart phản ánh toàn bộ quyền lực thực tế.

Một architect không có chức danh quản lý có thể ảnh hưởng lớn vì mọi technical decision phụ thuộc expertise của họ. Một compliance officer có thể không tham gia daily project nhưng có quyền chặn go-live. Một senior executive có quyền formal cao nhưng interest thấp nên không cần tham gia mọi detail.

Đây là lý do stakeholder engagement và team leadership phải nối với governance thay vì chỉ dựa vào communication skill.

## Power asymmetry thay đổi cách conflict biểu hiện

Conflict không phải lúc nào xuất hiện dưới dạng tranh luận trực tiếp. Khi power asymmetry lớn, người ít quyền có thể im lặng, trì hoãn, comply hình thức hoặc dùng side-channel thay vì phản đối công khai.

Vì vậy absence of disagreement không chứng minh alignment. Một meeting nơi mọi người đều “yes” có thể vẫn chứa unresolved risk nếu psychological safety thấp hoặc hierarchy mạnh.

Leader cần tạo mechanism để dissent có thể xuất hiện: pre-mortem, anonymous input, round-robin, independent review hoặc one-on-one channel tùy context.

## Team formation và psychological safety

Nhóm hiệu quả cần role clarity, trust, working agreement và khả năng đưa bad news lên sớm. Psychological safety (an toàn tâm lý / 심리적 안전감) không có nghĩa mọi người luôn thoải mái hoặc không bị challenge. Nó nghĩa thành viên có thể nêu vấn đề, hỏi, thừa nhận sai và disagree mà không bị trừng phạt cá nhân.

Đây là control quan trọng đối với risk. Nếu engineer phát hiện security concern nhưng sợ báo, dashboard có thể vẫn xanh cho đến khi failure xảy ra. Vì vậy culture ảnh hưởng trực tiếp tới information quality.

Psychological safety không thay performance standard. Team có thể vừa an toàn để nói thật vừa có accountability cao. Môi trường tốt không phải nơi “ai cũng được chấp nhận mọi hành vi”, mà là nơi problem được đưa ra sớm và xử lý công bằng.

## Psychological safety là chất lượng của sensor

Project cần sensor để phát hiện deviation. Con người là sensor quan trọng nhất với signal như “estimate không realistic”, “vendor đang che issue”, “requirement mâu thuẫn” hoặc “deployment có risk”.

Nếu culture khiến sensor tự kiểm duyệt, governance nhận data trễ hoặc sai. Vì vậy psychological safety không chỉ là employee-wellbeing concept; nó là **information reliability mechanism**.

Một leader phản ứng bằng blame mỗi khi có bad news sẽ dần làm dashboard đẹp hơn nhưng reality xấu hơn.

## Trust không đồng nghĩa kiểm soát thấp

Trust làm giảm verification transaction cost nhưng không loại bỏ control ở high-consequence work. Ta có thể trust engineer nhưng vẫn yêu cầu peer review cho production security change.

Control tốt bảo vệ system chứ không mặc định nghi ngờ cá nhân. Khi control được giải thích bằng risk/consequence thay vì “vì tôi không tin bạn”, trust và assurance có thể cùng tồn tại.

## Team development không phải một đường thẳng

Các team thường trải qua giai đoạn hình thành, va chạm, thiết lập chuẩn và tăng hiệu suất, nhưng thực tế không tuyến tính. Khi thành viên mới vào, deadline đổi hoặc conflict lớn xuất hiện, team có thể quay lại trạng thái cần tái thiết lập trust và working agreement.

Vì vậy project manager không nên nhìn team health như trạng thái đạt một lần rồi xong. Team là dynamic system; thay đổi cấu trúc hoặc pressure làm behavior thay đổi.

## Team topology ảnh hưởng coordination cost

Cách chia team tạo dependency. Nếu một feature cần đi qua năm team chuyên môn mới hoàn tất, handoff và queue có thể lớn dù mỗi team riêng lẻ hiệu suất cao.

Project manager không luôn có authority đổi organization, nhưng cần thấy coordination cost là property của structure. Tối ưu utilization từng specialist có thể làm end-to-end flow tệ hơn.

Cross-functional ownership, stable team hoặc clear service interface có thể giảm coordination dependency hơn việc thêm meeting.

## Coordination load tăng phi tuyến theo dependency

Thêm một người không chỉ thêm capacity; đôi khi nó thêm communication path, handoff và ambiguity về ownership. Trong work có coupling cao, team lớn hơn có thể chậm hơn nếu architecture và decision boundary không thay đổi.

Điều cần quan sát không phải số người tuyệt đối mà là **coordination surface**: bao nhiêu interface cần đồng bộ để một outcome hoàn thành. Một feature cần năm specialist từ năm department có coordination surface lớn hơn feature do một cross-functional team sở hữu, dù tổng headcount giống nhau.

Vì vậy “thêm người để cứu deadline” chỉ hiệu quả khi work có thể partition, onboarding cost chấp nhận được và bottleneck thực sự là capacity. Nếu bottleneck là decision, environment, requirement ambiguity hoặc shared reviewer, thêm người có thể tăng queue thay vì giảm duration.

## Decision load và attention budget

Con người có giới hạn về số context và decision có thể xử lý tốt trong một khoảng thời gian. Khi một PM, architect hoặc product owner trở thành node phải approve hàng chục quyết định nhỏ, vấn đề không chỉ là calendar bận; **decision quality** có thể giảm vì context switching và cognitive overload.

Decision load nên được quản lý như capacity. Có thể giảm bằng cách chuẩn hóa decision lặp lại, delegate decision reversible, dùng guardrail rõ, batch những decision có cùng context và bảo vệ attention cho exception high-consequence. Nếu mọi issue đều được escalate “cho chắc”, leader trở thành queue và team mất khả năng tự điều chỉnh.

Một signal quan trọng là decision aging: request đã chờ bao lâu, bao nhiêu work bị block và decision nào thường xuyên quay lại vì rationale không rõ. Đây là điểm nối People với flow và governance.

## Conflict là signal, không mặc định là failure

Xung đột (conflict / 갈등) có thể xuất phát từ resource scarcity, goal khác nhau, ambiguity, personality, schedule pressure hoặc technical disagreement. Mục tiêu không phải loại bỏ mọi conflict mà là xử lý nó ở level phù hợp trước khi biến thành relationship damage hoặc decision paralysis.

Một cách reasoning là tách position khỏi interest. “QA không đồng ý release” là position. Interest có thể là bảo vệ customer, tránh incident hoặc đáp ứng policy. “Business muốn release” có thể vì campaign deadline. Khi hiểu interest, ta có thể tìm option như limited rollout, feature flag hoặc explicit risk acceptance thay vì tranh luận thắng-thua.

Trong tình huống cần quyết định nhanh, forcing/directing có thể hợp lý, ví dụ incident an toàn. Khi issue quan trọng và relationship cần duy trì, collaborating/problem solving thường tạo outcome tốt hơn. Compromising có thể hữu dụng khi time box chặt. Avoiding hoặc smoothing chỉ phù hợp khi issue thấp hoặc cần cooling-off; dùng chúng với conflict cốt lõi sẽ làm debt tích tụ.

## Task conflict và relationship conflict khác nhau

Task conflict có thể hữu ích khi team tranh luận về option, assumption hoặc evidence. Relationship conflict chuyển focus từ problem sang con người và thường làm information quality giảm.

Leader nên bảo vệ **productive dissent** nhưng ngăn attack cá nhân. Nếu mọi disagreement bị dập để “giữ hòa khí”, team dễ groupthink. Nếu mọi tranh luận trở thành đấu quyền lực, decision latency và trust cùng xấu đi.

## Conflict escalation ladder

Không phải conflict nào cũng nên escalate ngay. Một ladder hợp lý thường bắt đầu bằng direct conversation giữa những người liên quan, sau đó facilitation, rồi manager/sponsor intervention nếu issue vượt authority hoặc relationship đã breakdown. Compliance, harassment, safety hoặc ethics concern là exception vì có thể cần channel chính thức sớm hơn.

Escalation đúng không phải failure của PM. Failure là giữ issue ở level không thể giải quyết chỉ vì muốn “tự xử lý”.

## Conflict debt tích lũy như technical debt

Unresolved disagreement có thể được che bằng quyết định tạm thời, nhưng assumption khác nhau vẫn tồn tại. Sau vài tuần, cùng conflict quay lại dưới dạng rework, passive resistance hoặc blame.

Một conflict được “đóng” khi decision, rationale, owner và follow-up đủ rõ; không phải chỉ khi meeting kết thúc yên bình.

## Negotiation trong team là phân bổ constraint

Khi hai nhóm cùng cần một scarce resource, negotiation không chỉ là communication skill. Nó là bài toán phân bổ capacity theo value, urgency, dependency và consequence.

Nếu PM cố “chia đều” resource để mọi bên hài lòng, có thể làm cả hai path chậm. Đôi khi quyết định đúng là ưu tiên một path critical và trì hoãn path khác. Fairness không đồng nghĩa equality; fairness cần rationale transparent.

## Motivation và incentive alignment

Con người phản ứng với system incentive chứ không chỉ instruction. Nếu developer được đánh giá theo số ticket đóng còn QA theo số defect bắt được, hai nhóm có thể vô tình tối ưu ngược nhau. Nếu vendor được trả tiền theo effort thay vì outcome, incentive có thể khuyến khích kéo dài work.

Project manager không phải lúc nào cũng thay compensation system được, nhưng cần nhìn thấy incentive mismatch và thiết kế shared objective, acceptance criterion hoặc governance để giảm local optimization.

Đây là một mental model quan trọng: behavior thường là property của system, không chỉ của cá nhân.

## Metric trở thành incentive ngay cả khi không gắn thưởng

Một metric được executive hỏi hàng tuần có thể trở thành target dù không có bonus. Nếu chỉ hỏi velocity, team sẽ tối ưu velocity. Nếu chỉ hỏi defect count, người ta có thể thay cách classify defect.

Leader phải quan sát **behavioral side effect của measurement**. Đây là liên kết trực tiếp với Goodhart's Law ở chapter measurement: khi metric thành target cứng, nó có thể mất giá trị làm signal.

## Extrinsic và intrinsic motivation

Tiền thưởng, deadline hoặc recognition là extrinsic motivator. Mastery, autonomy, purpose, professional identity và peer trust là intrinsic motivator.

Knowledge work dài hạn thường cần cả hai nhưng không nên giả định “thêm bonus” luôn cải thiện performance. Incentive cá nhân mạnh có thể phá collaboration nếu outcome cần teamwork.

Project manager nên thiết kế environment nơi người giỏi thấy work meaningful, có autonomy phù hợp và được feedback về impact, đồng thời objective/constraint vẫn rõ.

## Servant leadership và adaptive teams

Lãnh đạo phục vụ (servant leadership / 서번트 리더십) tập trung vào việc loại impediment, phát triển khả năng của team và bảo vệ autonomy thay vì ra lệnh chi tiết. Nó đặc biệt phù hợp với knowledge work nơi người thực hiện có expertise sâu hơn manager.

Nhưng servant leadership không phải passive leadership. Khi team thiếu direction, vi phạm policy hoặc risk vượt tolerance, leader vẫn phải thiết lập boundary, escalate hoặc quyết định.

Servant leader tốt chuyển focus từ “ai đang chậm?” sang “system nào đang làm flow chậm?”. Nếu testing luôn nghẽn vì shared environment, thúc tester làm nhanh hơn không giải quyết constraint.

## Leadership mode nên đổi theo context

Không có một style đúng mọi lúc. Emergency cần direction rõ và tốc độ. Discovery cần curiosity và psychological safety. Team mới cần context/role clarity nhiều hơn. Team mature cần autonomy cao hơn.

Maturity của leader là khả năng thay mode mà không tạo confusion về principle. Direction có thể thay, nhưng fairness, transparency và respect không nên biến mất khi pressure tăng.

## Leadership dưới pressure bộc lộ governance thật

Khi deadline bình thường, nhiều organization trông rất collaborative. Khi crisis xảy ra, quyền lực và incentive thật mới lộ ra.

Nếu leader bỏ quality gate ngay khi executive gây áp lực, team học rằng policy chỉ là optional. Nếu leader che forecast xấu để tránh conflict, team học rằng transparency bị phạt.

Culture được định hình nhiều bởi behavior lúc pressure hơn bởi policy document.

## Coaching, mentoring và training

Training truyền knowledge/skill có cấu trúc. Mentoring dựa trên kinh nghiệm để định hướng phát triển. Coaching dùng câu hỏi và feedback để người khác tự nâng khả năng giải quyết vấn đề. Chọn sai intervention làm lãng phí thời gian: người mới thiếu skill cần training, không chỉ “hãy tự tìm cách”; chuyên gia cần autonomy/coaching, không nên bị hướng dẫn vi mô.

Một fourth mode là directing, cần khi risk cao và capability thấp hoặc khi emergency cần action nhanh. Maturity không nằm ở việc luôn coaching, mà ở việc chọn intervention theo capability và context.

## Capability matrix phải nhìn cả depth lẫn redundancy

Một team có một chuyên gia cực giỏi nhưng không có backup vẫn có capability risk. Skill matrix nên nhìn mức proficiency, criticality và redundancy.

Pairing, review rotation, shadowing và ownership sharing không chỉ phát triển người; chúng giảm single point of knowledge failure. Nhưng rotation quá nhiều cũng phá focus. Cần balance learning với flow.

## Team resilience không chỉ là có người backup

Backup chỉ giải một failure mode: một cá nhân unavailable. Team resilience còn phụ thuộc khả năng giữ decision quality khi workload tăng, khi một dependency biến mất, khi leader không online hoặc khi project chuyển phase.

Một team resilient có context được externalize đủ để người khác tiếp quản, authority không tập trung vào một người, critical skill có redundancy, working agreement cho incident rõ và recovery capacity sau surge. Ngược lại, một team có nhiều người nhưng mọi quyết định vẫn cần một architect duy nhất vẫn có single point of failure.

Resilience có cost. Pairing, documentation, cross-training và slack capacity có thể làm utilization nhìn thấp hơn trong ngắn hạn nhưng giảm tail risk. Đây là trade-off giống redundancy trong technical system: efficiency cực đại thường làm system mong manh hơn trước disturbance.

## Decision protocol làm giảm conflict không cần thiết

Nhiều conflict xuất hiện không phải vì người ta bất đồng nội dung mà vì không rõ ai quyết. Team nên explicit decision rule: consensus ở đâu, consult ở đâu, ai accountable cuối cùng, và decision nào có thể reversible.

Một decision log ngắn ghi decision, context, owner, date và assumption có thể ngăn project tranh luận lại cùng vấn đề nhiều lần. Nó cũng giúp learning khi assumption thay đổi.

## Consensus không phải default

Consensus có value khi buy-in rộng thực sự cần thiết hoặc knowledge phân tán. Nhưng yêu cầu consensus cho mọi decision có thể tạo veto power và latency.

Một rule tốt có thể là: consult rộng, decision owner rõ. Người không đồng ý vẫn có thể commit sau decision nếu process công bằng và rationale explicit.

## Disagree-and-commit cần điều kiện

“Disagree and commit” chỉ lành mạnh khi dissent đã được nghe, decision owner hợp lệ và decision không vi phạm safety/ethics/legal boundary. Nó không nên được dùng để ép im lặng hoặc tránh escalation cần thiết.

Sau commitment, evidence mới có thể reopen decision nếu assumption thay đổi. Commit không đồng nghĩa decision bất biến.

## Virtual và cross-cultural teams

Distributed team làm mất nhiều context phi ngôn ngữ và tạo timezone/communication latency. Cross-cultural context còn khác ở cách thể hiện disagreement, hierarchy và commitment. Giải pháp không phải stereotype văn hóa mà là làm explicit working agreement: channel nào dùng cho decision, response expectation, language, documentation, handoff và escalation.

Async communication tốt cần artifact đủ context để người khác hiểu mà không cần người viết online. Nhưng không phải mọi conflict nên xử lý async; sensitive disagreement thường cần synchronous conversation để giảm misunderstanding.

## Timezone là constraint hệ thống

Nếu hai team chỉ overlap một giờ mỗi ngày, một clarification đơn giản có thể mất 24 giờ. Đây là communication latency có thể tích lũy thành schedule risk.

Solution có thể là better async artifact, rotating overlap, decision SLA hoặc local decision rights. “Họ phải communicate tốt hơn” là chẩn đoán quá mơ hồ.

## Dấu hiệu team health cần quan sát

Velocity hoặc task completion không đủ để đánh giá team. Các signal khác gồm số issue được nêu sớm hay muộn, dependency wait time, rework, meeting dominated bởi một người, decision latency, turnover intention và mức chủ động cross-help.

Một team vẫn “đạt deadline” trong vài sprint nhưng nếu bad news bị che giấu và overtime tăng liên tục, system đang tích debt. Project manager cần nhìn leading indicator chứ không chỉ output ngắn hạn.

## Burnout là risk hệ thống, không phải weakness cá nhân

Chronic overtime làm giảm attention, tăng defect và giảm willingness to surface problem. Sau một mức nhất định, thêm giờ có thể làm throughput thực giảm vì rework.

Leader cần phân biệt surge ngắn hạn có recovery với operating model dựa trên overtime. Nếu plan chỉ khả thi khi team liên tục vượt sustainable capacity, plan đang che risk bằng sức khỏe con người.

## Recovery debt sau giai đoạn surge

Một team có thể hoàn thành deadline bằng overtime rồi trông như đã “hết risk”, nhưng hệ thống thường mang theo recovery debt: fatigue, deferred learning, documentation thiếu, technical/quality debt và leave bị dồn. Nếu project lập tức bắt đầu phase mới với capacity danh nghĩa 100%, forecast đang giả định con người phục hồi tức thời.

Sau surge cần nhìn capacity thực, defect/rework tail và knowledge debt trước khi commit tiếp. Recovery time không phải phần thưởng tùy chọn; trong knowledge work nó có thể là input để khôi phục quality của attention và decision.

Điều này nối People với schedule/finance: overtime có thể chuyển cost từ hiện tại sang future rework, turnover hoặc delay. Một plan “đúng hạn” nhưng làm phase sau mất capability chưa chắc tối ưu toàn system.

## Accountability loop cần có feedback

Accountability không phải chỉ “ai chịu trách nhiệm khi sai”. Một loop lành mạnh gồm expectation rõ → autonomy/resource → observation/evidence → feedback → correction/learning.

Nếu organization chỉ có punishment cuối loop nhưng không có clarity/resource/feedback sớm, accountability trở thành blame system.

## People evidence phải nối được với project state

People signal dễ bị coi là subjective nên bị bỏ qua cho đến khi schedule hoặc quality xấu rõ ràng. Cách tốt hơn là nối signal hành vi với evidence vận hành: decision latency tăng, issue được raise muộn hơn, review queue dài, rework tăng, handoff fail hoặc overtime kéo dài.

Mục tiêu không phải biến mọi cảm xúc thành KPI. Mục tiêu là tránh hai cực: chỉ tin dashboard số và bỏ qua weak signal của con người, hoặc chỉ dựa vào impression mà không kiểm tra impact. Khi nhiều loại evidence cùng chỉ một mechanism, confidence của diagnosis tăng.

Ví dụ team nói “quá tải” và đồng thời cycle time, defect escape và decision aging đều tăng. Response hợp lý hơn là điều tra demand/capacity và bottleneck, không mặc định đây chỉ là morale issue. Đây là cách People trở thành một phần của integrated project sensing.

## Ví dụ scenario

Một senior developer thường xuyên bác ý kiến junior trong meeting. Velocity vẫn ổn nhưng junior ngừng phát biểu và defect do edge case tăng. Hành động tốt không phải chỉ “nhắc cả team tôn trọng nhau” hoặc thay developer ngay. PM cần quan sát evidence, nói riêng để hiểu root cause, thiết lập lại ground rules, tạo channel an toàn cho feedback, và theo dõi behavioral outcome. Problem cần được xử lý ở system/team level chứ không chỉ trên task board.

Một case khác: hai team cùng cần một DBA duy nhất và bắt đầu đổ lỗi cho nhau. Nếu root cause là resource contention, workshop hòa giải chỉ xử lý symptom. PM cần làm visible demand/capacity, ưu tiên theo business constraint và escalate resource decision nếu vượt authority.

Một case thứ ba: team nói họ “được empowered”, nhưng mọi production change vẫn phải chờ một director ở timezone khác. Vấn đề không phải thiếu ownership ở team; decision architecture contradicts empowerment. PM cần làm rõ threshold nào có thể delegate, control nào có thể automate và decision nào thật sự cần director.

## Failure modes

Hero culture xảy ra khi project phụ thuộc vài cá nhân cứu deadline liên tục; short-term success che capability fragility. Consensus theater xảy ra khi mọi người phải đồng ý hình thức nhưng dissent không được xử lý. Empowerment theater xảy ra khi team được giao trách nhiệm nhưng không có authority/resource. Blame culture làm bad news đến muộn. Metric pressure làm behavior tối ưu số thay vì outcome. Conflict avoidance tích unresolved decision debt.

Những failure này đều làm information flow hoặc decision quality xấu đi trước khi chúng xuất hiện thành schedule/quality issue.

## Mental model

> Leadership là thiết kế environment nơi information thật có thể đi lên, decision có thể đi xuống đúng level và accountability có thể quay lại bằng feedback. Team health là một phần của risk management vì incentive, trust, power và decision architecture quyết định chất lượng hành vi dưới uncertainty.

Tiếp theo: [Stakeholder, communication và knowledge transfer](./03_stakeholders_communication_and_knowledge.md).
