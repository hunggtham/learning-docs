# 03 — Stakeholder, communication và knowledge transfer

## Stakeholder management không phải danh sách người nhận email

Bên liên quan (stakeholder / 이해관계자) là cá nhân, nhóm hoặc tổ chức có thể ảnh hưởng, bị ảnh hưởng, hoặc nhận thấy mình bị ảnh hưởng bởi project. Điều khó không nằm ở việc ghi tên họ, mà ở việc hiểu interest, influence, expectation, information need và mức độ thay đổi theo thời gian.

Một regulator, sponsor, end user, operations team và vendor đều có “success” khác nhau. Project manager phải biến các success model riêng đó thành expectation đủ tương thích với objective chung.

Stakeholder engagement vì vậy là một control loop của project. Project gửi signal về direction và current state; stakeholder gửi feedback, constraint, objection hoặc approval; project cập nhật decision. Nếu loop này chậm hoặc méo, requirement và governance sẽ trễ hơn reality.

## Stakeholder system là network, không phải danh sách độc lập

Stakeholder ảnh hưởng lẫn nhau. Sponsor có thể bị board pressure; operations có thể liên kết với security; vendor có thể dựa vào subcontractor; regulator có thể thay expectation sau public incident trong ngành.

Vì vậy phân tích từng người riêng lẻ đôi khi bỏ lỡ coalition, dependency và influence path. Một stakeholder có formal power thấp nhưng có thể ảnh hưởng mạnh nếu họ cung cấp evidence cho người có quyền quyết định.

Mental model tốt hơn là network:

```text
stakeholder → interest / power / dependency / information
            ↘ ảnh hưởng stakeholder khác
```

Project manager cần hiểu không chỉ “ai có power” mà còn **power đi qua đường nào**.

## Identification là continuous sensing

Stakeholder register không phải artifact tạo một lần. Stakeholder mới xuất hiện khi scope, organization hoặc external environment thay đổi. Một team vận hành có thể chưa quan tâm ở đầu dự án nhưng trở thành stakeholder critical trước handover. Nếu identification chỉ diễn ra lúc initiation, transition thường gặp surprise.

Một trigger tốt để rà lại stakeholder là khi có scope change lớn, organization restructure, vendor mới, compliance change, release tới user group mới hoặc benefit owner thay đổi. Stakeholder map phải sống cùng project system.

## Stakeholder lifecycle khác project lifecycle

Cùng một stakeholder có thể đổi vai trò theo thời gian. Security team có thể chỉ consult trong discovery nhưng trở thành approver trước go-live. Operations từ low-interest trở thành primary owner ở transition. Customer support có thể gần như vắng ở build nhưng critical sau rollout.

Engagement strategy nên thay theo **decision need hiện tại**, không theo classification lúc kickoff.

## Stakeholder không chỉ có power và interest

Các matrix như power-interest hữu ích để nghĩ về engagement, nhưng không nên biến con người thành một ô cố định. Một stakeholder “low interest” có thể đột ngột có high power khi incident xảy ra. Salience còn phụ thuộc legitimacy và urgency.

Ngoài power và interest, nên hiểu stance, dependency và information asymmetry. Một stakeholder có power thấp nhưng giữ knowledge độc quyền vẫn có leverage cao. Một end user có formal power thấp nhưng adoption của họ quyết định benefit realization.

Điều quan trọng là strategy: ai cần co-create, ai cần approve, ai cần consult, ai chỉ cần informed; và bằng chứng nào cho thấy strategy cần đổi.

## Salience là dynamic property

Power, legitimacy và urgency thay đổi theo event. Một legal team bình thường ít tham gia nhưng trở thành critical khi data breach xuất hiện. Một user group nhỏ có thể trở nên urgent nếu defect ảnh hưởng safety.

Stakeholder prioritization vì vậy phải event-sensitive. Nếu project chỉ dùng stakeholder matrix static, signal mới có thể không đổi engagement dù risk profile đã đổi hoàn toàn.

## Stakeholder dependency quan trọng ngang stakeholder power

Power hỏi “họ có thể ảnh hưởng project tới đâu?”. Dependency hỏi “project phụ thuộc họ tới đâu?”.

Một external API team không có quyền formal với project nhưng nếu không giao interface, project không thể proceed. Đây là high dependency stakeholder dù organizational power thấp.

Ngược lại một executive power cao nhưng không nằm trên critical decision path có thể cần exception-level reporting thay vì daily engagement.

## Representation risk: người lên tiếng không luôn đại diện người chịu tác động

Project thường nghe rõ nhất từ stakeholder có thời gian, authority hoặc kỹ năng diễn đạt tốt. Nhưng nhóm bị ảnh hưởng lớn nhất có thể ít xuất hiện trong workshop: frontline employee bận vận hành, customer bỏ sản phẩm thay vì gửi feedback, user có accessibility need ít được mời, hoặc subcontractor chịu constraint nhưng communication đi qua vendor chính.

Đây là **representation risk**. Nếu project đồng nhất “feedback thu được” với “nhu cầu của population”, requirement và benefit model có thể bị lệch ngay cả khi workshop diễn ra rất chuyên nghiệp.

Cần hỏi ai đang vắng mặt, ai đang được proxy bởi người khác và proxy đó có incentive/knowledge đủ để đại diện không. Product owner, manager hoặc customer representative có thể là interface cần thiết, nhưng high-consequence assumption vẫn nên được kiểm chứng với evidence gần affected population hơn khi khả thi.

Một dấu hiệu nguy hiểm là stakeholder map rất đầy đủ theo org chart nhưng không có người đại diện cho nhóm chịu operational burden sau rollout. Đây là điểm nối stakeholder analysis với distribution of value/harm ở chapter Foundations.

## Engagement state khác communication frequency

Gửi nhiều thông tin không đồng nghĩa stakeholder được engage tốt. Một stakeholder có thể nhận daily report nhưng vẫn phản đối project vì success criteria của họ chưa được hiểu.

Engagement có thể nhìn như movement giữa unaware, resistant, neutral, supportive và leading, nhưng classification chỉ hữu ích nếu gắn với action. Nếu một stakeholder critical vẫn resistant, PM cần hiểu reason: loss of control, workload tăng, compliance concern, trust thấp hay incentive mismatch.

Mục tiêu không phải biến mọi người thành “supportive”. Một regulator đúng vai trò có thể liên tục challenge project; engagement tốt ở đây nghĩa concern được surface sớm và evidence được trao đổi đúng cách.

## Resistance không phải luôn là problem cần “loại bỏ”

Resistance có thể chứa information mà project chưa thấy. Operations phản đối có thể vì support capacity không đủ. Compliance phản đối có thể vì control evidence yếu. User phản đối có thể vì workflow làm tăng workload.

Nếu project coi mọi resistance là “change-management issue”, nó có thể cố thuyết phục thay vì sửa design.

Câu hỏi đầu tiên nên là: resistance đến từ misinformation, incentive conflict, legitimate risk, capability gap hay loss of status/control? Response khác nhau theo cause.

## Feedback sampling bias

Feedback loop chỉ tốt khi sample đủ đại diện cho decision cần đưa ra. Nếu pilot chỉ gồm power user nhiệt tình, adoption signal có thể quá optimistic. Nếu survey chỉ nhận response từ người rất hài lòng hoặc rất bất mãn, average không phản ánh silent majority. Nếu UAT chủ yếu do project team chạy, operational friction có thể bị bỏ qua.

Vì vậy PM cần phân biệt **feedback volume** với **feedback validity**. Câu hỏi nên là: ai được quan sát, trong context nào, ai không xuất hiện và evidence này có đủ gần production reality không?

Sampling bias đặc biệt nguy hiểm vì dashboard có thể rất nhiều data nhưng vẫn sai model. Cách giảm không phải luôn “thu thập nhiều hơn”, mà là chọn segment, scenario và observation window phù hợp với uncertainty đang cần giảm.

## Expectation alignment trước expectation management

Không thể “manage expectation” tốt nếu expectation chưa được surface. Nhiều project conflict đến từ hidden assumptions: sponsor nghĩ MVP gồm reporting, team nghĩ không; vendor nghĩ response SLA là business hours, customer nghĩ 24/7.

Alignment là quá trình làm assumption explicit, tìm gap, thương lượng priority và ghi nhận decision. Sau đó expectation management mới là việc liên tục so sánh current reality với agreed expectation và cập nhật khi context thay đổi.

Expectation càng quan trọng càng cần evidence cụ thể. “Nhanh”, “ổn định”, “dễ dùng” hoặc “xong trước cuối quý” đều có thể được hiểu khác nhau nếu không chuyển thành acceptance criterion, milestone hoặc measurable outcome.

## Expectation debt

Nếu project biết expectation đang khác reality nhưng trì hoãn conversation vì sợ conflict, gap đó tích lại thành **expectation debt**.

Ví dụ sponsor vẫn tin go-live tháng 10 dù team đã biết từ tháng 8 rằng critical vendor dependency có khả năng đẩy sang tháng 12. Mỗi tuần không cập nhật làm correction sau này khó hơn vì decision khác đã dựa trên expectation cũ.

Expectation debt giống technical debt ở chỗ short-term silence giảm discomfort nhưng tăng future correction cost.

## Promise, forecast và aspiration phải tách nhau

Stakeholder thường nghe một date nhưng không biết đó là commitment, forecast hay target. Communication tốt phải làm rõ semantic level.

“Chúng tôi target 30/10 với confidence hiện tại 60%” khác hoàn toàn “30/10 là contractual commitment”. Nếu ba loại date bị trộn, trust bị phá dù team technically “đã nói trước”.

## Communication là transfer of meaning

Gửi message không đồng nghĩa communication thành công. Communication có sender, encoding, channel, noise, receiver, interpretation và feedback. Vì vậy “đã gửi email” không chứng minh stakeholder hiểu decision.

Channel nên match với purpose. Một conflict phức tạp thường cần synchronous conversation; một decision cần traceability nên được documented; urgent incident cần fast broadcast và acknowledgement; knowledge bền vững cần repository có ownership.

Communication plan hữu ích khi nó trả lời ai cần thông tin gì, tại sao, khi nào, qua channel nào, format nào, ai chịu trách nhiệm và feedback loop nào xác nhận understanding.

## Closed-loop communication

Với information critical, communication nên có acknowledgement và confirmation of meaning. Sender truyền message, receiver xác nhận nhận/hiểu, action hoặc next state được ghi rõ.

Trong incident, “đã post Slack” không đủ nếu owner chưa acknowledge. Trong handover, “đã gửi tài liệu” không đủ nếu operations chưa chứng minh capability.

Closed-loop communication đặc biệt quan trọng khi consequence của misunderstanding cao.

## Communication reliability có thể thiết kế như service

Một project lớn có thể coi communication path như service với expectation rõ: incident severity-1 acknowledgement trong 10 phút, dependency request phản hồi trong hai ngày, change decision trong năm ngày.

Đây không phải để biến con người thành SLA máy móc, mà để làm latency visible. Nếu project phụ thuộc decision nhưng không có response expectation, queue có thể bị coi là “communication problem” thay vì governance bottleneck.

## Information có half-life

Một message có thể hoàn toàn đúng lúc gửi nhưng nhanh chóng stale. Forecast, stakeholder stance, vendor ETA, risk exposure và operating procedure đều có **information half-life** khác nhau. Vì vậy traceability không chỉ hỏi “nguồn ở đâu?” mà còn “nguồn này còn fresh không?”.

Information high-volatility cần timestamp, owner và refresh trigger rõ hơn information ổn định. Một contact list có thể review hàng quý; incident status có thể stale sau 15 phút. Dùng cùng một cadence cho mọi information tạo hoặc overhead hoặc stale decision input.

Decision dựa trên stale information có thể hợp lý tại thời điểm cũ nhưng sai ở hiện tại. Vì vậy artifact quan trọng nên cho người đọc biết effective time, confidence và condition làm nó hết hiệu lực. Đây là connection trực tiếp với freshness SLO và lineage ở chapter Artifacts.

## Push, pull và interactive communication

Push communication đưa information trực tiếp tới audience, ví dụ email hoặc notification. Pull communication để stakeholder tự truy cập repository, dashboard hoặc portal khi cần. Interactive communication cho phép trao đổi hai chiều như workshop, call hoặc negotiation.

Chọn mode theo uncertainty. Information ổn định và self-service phù hợp pull. Announcement rõ có thể push. Ambiguous requirement hoặc conflict cần interactive vì meaning phải được đồng tạo, không chỉ truyền đi.

## Communication mode nên dựa trên cost of misunderstanding

Một routine metric có thể pull qua dashboard. Một material risk cần push tới owner. Một ambiguous contractual interpretation cần interactive discussion rồi formal record.

Càng khó sửa misunderstanding, càng cần richer channel và confirmation mạnh hơn.

## Richness của communication channel

Channel có độ giàu thông tin khác nhau. Text ngắn tốt cho fact đơn giản nhưng kém cho conflict nhiều cảm xúc. Video/call hoặc face-to-face cung cấp feedback tức thời và nhiều contextual cue hơn, nhưng khó trace nếu không document decision sau đó.

Một pattern tốt là discuss rich, record lean: dùng synchronous channel để giải ambiguity rồi ghi decision/action trong artifact bền vững.

## Synchronous và asynchronous communication là trade-off

Synchronous communication giảm feedback latency nhưng tốn calendar alignment và dễ mất traceability. Asynchronous communication scale tốt hơn và tạo record nhưng cần context rõ, có thể làm clarification chậm.

Project distributed nên thiết kế loại decision nào cần sync, loại nào async và timeout bao lâu trước escalation.

## Transparency không phải information overload

Transparency nghĩa information cần thiết cho decision được nhìn thấy đúng thời điểm. Dump mọi log/report cho sponsor không tăng transparency nếu họ không nhận ra signal quan trọng. Reporting tốt phải tailor theo decision level.

Team có thể cần blocker, WIP, defect và dependency detail. Sponsor cần outcome, trend, forecast, major risk, decision request và tolerance breach. Governance body cần compliance/evidence và escalation.

Information overload cũng là risk vì signal quan trọng bị chìm. PM phải thiết kế information architecture, không chỉ tăng volume.

## Executive reporting là compression có chủ đích

Một executive dashboard luôn mất detail. Vì vậy người thiết kế phải bảo vệ các signal không được phép bị average hóa: safety breach, legal exposure, critical dependency, major forecast shift.

Green overall status không được phép che một red non-negotiable constraint. Aggregation rule phải phản ánh consequence chứ không chỉ arithmetic average.

## Communication noise và distortion

Noise có thể là technical jargon, language barrier, timezone, organizational politics, data inconsistency hoặc quá nhiều intermediary. Mỗi handoff có khả năng làm message mất fidelity.

Một project nhiều layer reporting có thể thấy “red risk” biến thành “amber concern” rồi cuối cùng thành “on track” ở executive deck. Đây là distortion do incentive và compression, không chỉ lỗi wording.

Control tốt gồm source-of-truth, direct escalation path cho material risk và traceable decision request.

## Incentive tạo distortion

Nếu messenger bị phạt khi mang bad news, signal sẽ bị soften. Nếu department KPI phụ thuộc status xanh, report có bias cấu trúc.

Project manager phải hiểu communication reliability không chỉ là kỹ năng viết; nó phụ thuộc incentive và psychological safety. Đây là điểm nối trực tiếp với chapter People.

## Active listening và diagnostic question

Stakeholder conversation tốt không chỉ là thuyết phục. Active listening dùng paraphrase, clarification và evidence check để xác nhận meaning.

Khi stakeholder nói “project chậm”, PM nên tìm statement cụ thể: milestone nào, expectation nào, data nào? Khi user nói “khó dùng”, cần scenario và friction cụ thể. Diagnostic question biến emotion hoặc general statement thành actionable information mà không dismiss concern.

## Listening phải phân biệt position, interest và constraint

Position là điều stakeholder nói họ muốn. Interest là lý do họ muốn. Constraint là boundary họ không thể thay.

“Phải go-live ngày 1/11” có thể là position. Interest có thể là marketing campaign; constraint thực có thể chỉ là regulatory reporting trước cuối năm. Nếu không tách ba lớp, project dễ coi mọi request là hard constraint.

## Negotiation là quản lý trade-off

Project thường có nhiều objective không thể tối ưu đồng thời. Negotiation tốt tách interest khỏi position và làm trade-off explicit.

Ví dụ sponsor yêu cầu thêm scope nhưng không đổi deadline. PM không nên chỉ nói “không thể” hoặc âm thầm ép team overtime. Cần đưa option: bỏ scope khác, tăng capacity nếu có leverage, chấp nhận risk, đổi milestone hoặc defer feature. Negotiation làm constraint visible để authority chọn.

## BATNA và ZOPA

BATNA (Best Alternative to a Negotiated Agreement) là alternative tốt nhất nếu không đạt agreement. ZOPA (Zone of Possible Agreement) là vùng hai bên có thể cùng chấp nhận.

Hiểu BATNA giúp negotiation bớt cảm tính. Nếu vendor không giảm giá nhưng buyer có alternative vendor credible, bargaining position khác hoàn toàn trường hợp switching cost rất cao.

ZOPA không phải lúc nào tồn tại. Nếu customer yêu cầu deadline không thể đạt mà không phá legal/safety constraint, “compromise ở giữa” không phải answer hợp lý. Khi đó cần đổi scope/resource hoặc escalate decision.

## Negotiation power đến từ option, information và timing

Formal authority chỉ là một nguồn power. Có alternative tốt, evidence tốt và thời gian chuẩn bị có thể tăng leverage. Bị khóa vào một vendor ngay trước deadline làm BATNA yếu dù contract manager có chức danh cao.

Project strategy nên tạo option sớm thay vì đợi negotiation crisis mới tìm leverage.

## Negotiation tốt đôi khi tạo option mới thay vì chia phần cũ

Nếu hai bên chỉ tranh một biến như price hoặc deadline, negotiation dễ thành zero-sum. Nhưng project thường có nhiều dimension: scope, timing, payment profile, service level, risk allocation, sequence, pilot size hoặc acceptance mechanism. Mở thêm dimension có thể tạo trade mà cả hai bên coi là tốt hơn.

Ví dụ vendor không thể giảm total price nhưng có thể chấp nhận milestone payment muộn hơn; customer không thể đổi regulatory date nhưng có thể tách optional scope sang phase sau. Đây là **option creation**, khác với compromise cơ học “mỗi bên nhường một nửa”.

Tuy nhiên option mới chỉ có giá trị nếu obligation và consequence được làm rõ. Một creative deal mơ hồ có thể chỉ chuyển conflict sang acceptance/claim ở cuối project.

## Trust là tài sản của information system

Influence không chỉ đến từ authority. Credibility, consistency, reciprocity và understanding stakeholder interest đều tạo trust. Khi PM liên tục che bad news để “giữ hình ảnh”, short-term conflict có thể giảm nhưng information reliability bị phá. Khi crisis xảy ra, stakeholder sẽ discount mọi report sau đó.

Trust giúp giảm verification cost. Khi report đáng tin, stakeholder không phải kiểm lại mọi detail. Nhưng trust không thay evidence ở decision có compliance hoặc financial impact cao.

## Trust repair cần evidence, không chỉ apology

Khi trust bị phá bởi missed commitment hoặc hidden issue, nói “sẽ communicate tốt hơn” thường không đủ. Cần thay mechanism: forecast confidence rõ hơn, earlier escalation trigger, transparent source data hoặc checkpoint mới.

Trust được rebuild khi stakeholder thấy prediction/reality dần align và bad news đến sớm hơn.

## Stakeholder risk propagation

Một stakeholder issue có thể lan thành scope, schedule, finance hoặc adoption risk. Operations resistance có thể delay transition; vendor dispute có thể thành schedule/cost risk; regulator concern có thể block go-live.

Stakeholder register không nên đứng tách biệt risk register. Khi engagement problem có probability/impact lên objective, nó đã trở thành project risk cần owner/response.

## Coalition và stakeholder alignment

Một project transformation có thể gặp nhiều stakeholder riêng lẻ neutral nhưng khi họ hình thành coalition phản đối, influence tăng mạnh. Ngược lại sponsor có thể tạo coalition hỗ trợ bằng cách align business owners quanh shared outcome.

PM không nên “chính trị hóa” mọi interaction, nhưng phải nhận ra organizational change diễn ra qua network. Engagement strategy chỉ theo từng cá nhân có thể bỏ lỡ group dynamics.

## Knowledge transfer và bus factor

Knowledge transfer (chuyển giao tri thức / 지식 이전) giải quyết rủi ro tri thức nằm trong đầu một vài người. Explicit knowledge có thể document; tacit knowledge thường cần pairing, shadowing, walkthrough, rehearsal và thực hành.

Một handover document 100 trang không đảm bảo operations có thể vận hành system. Readiness tốt hơn được chứng minh bằng việc operations tự chạy scenario, xử lý incident mẫu hoặc thực hiện rollback dưới supervision.

Bus factor thấp nghĩa một vài cá nhân là single point of knowledge failure. PM nên phát hiện sớm qua dependency map, vacation risk, review ownership và handover need.

## Knowledge decay

Knowledge không chỉ có nguy cơ mất khi người rời team; nó còn stale khi system thay đổi. Runbook viết đúng sáu tháng trước có thể sai sau architecture change.

Knowledge artifact cần owner, update trigger và validation. Một rehearsal định kỳ có thể phát hiện document stale tốt hơn việc chỉ review text.

## Knowledge transfer cần acceptance criterion

“Đã training” là activity, không phải evidence của transfer. Có thể dùng teach-back, simulation, runbook execution hoặc support handoff drill để kiểm chứng.

Ví dụ operations team chỉ được coi là ready khi họ tự deploy bản test, restore backup và xử lý ba incident scenario mà không phụ thuộc developer chính. Điều này biến knowledge transfer từ attendance thành capability evidence.

## Knowledge transfer là chuyển khả năng tái tạo reasoning

Một người có thể nhớ procedure nhưng không biết tại sao procedure tồn tại. Khi context thay đổi, họ không biết phần nào được phép adapt. Vì vậy transfer sâu cần cả **what**, **why**, boundary và failure signal.

Ví dụ runbook nói “restart service B trước service A” nhưng không giải dependency. Khi architecture đổi, operator có thể tiếp tục procedure cũ dù invariant đã thay. Một handover tốt phải giúp receiving team tái tạo reasoning đủ để nhận ra khi document không còn đúng.

Teach-back vì thế mạnh hơn attendance: người nhận giải thích lại mental model, thực hiện scenario bình thường và xử lý một exception. Nếu chỉ làm được happy path khi người cũ đứng cạnh, capability chưa thực sự được transfer.

## Knowledge ownership sau transition

Ai giữ knowledge sau project closure phải được xác định. Nếu temporary project team giải tán nhưng không có owner cho runbook, architecture decision hoặc vendor context, knowledge decay gần như chắc chắn.

Transition cần chuyển cả **artifact ownership** và **responsibility to maintain knowledge**, không chỉ copy file sang folder operations.

## Cross-cultural và multilingual communication

Ngôn ngữ chung không đảm bảo shared interpretation. Culture khác nhau về hierarchy, directness, silence, disagreement và meaning của commitment.

PM không nên stereotype theo nationality. Cách thực tế hơn là explicit working norms: “yes” nghĩa acknowledgement hay commitment? Khi chưa đồng ý có được nói trực tiếp trong meeting không? Decision được xác nhận ở đâu? Deadline timezone nào?

Khi translation cần thiết, critical requirement hoặc contract term phải được verify hai chiều, không dựa hoàn toàn vào machine translation hoặc một cá nhân trung gian.

## Translation risk là semantic risk

Một từ legal/technical dịch gần đúng có thể thay obligation. Critical term nên giữ original wording cùng translation, có glossary hoặc back-translation khi cần.

Nếu một bilingual coordinator trở thành single source cho mọi meaning, họ cũng trở thành knowledge bottleneck. Important decision cần artifact song ngữ hoặc verification independent khi consequence cao.

## Stakeholder fatigue

Engagement quá nhiều cũng có cost. Mời stakeholder vào mọi meeting làm họ disengage khi thật sự cần decision.

Engagement cadence nên match decision need. Executive sponsor có thể cần milestone/exception review; product user cần frequent feedback trên increment; compliance cần gate ở những point material. Tailoring communication giúp bảo vệ attention như một resource hữu hạn.

## Attention là scarce resource

Một decision request gửi cùng 30 informational email dễ bị bỏ qua. Communication design nên phân biệt action-needed, approval-needed, risk alert và FYI.

Nếu mọi message đều marked urgent, organization mất ability phân biệt urgency. Đây là information-system failure, không chỉ etiquette.

## Stakeholder decision debt

Khi project liên tục trì hoãn những conversation hoặc approval khó, decision không biến mất; nó tích thành queue. Scope option khác có thể tiếp tục được xây trên assumption chưa được sponsor xác nhận, vendor có thể tiếp tục work trước khi commercial term rõ, hoặc operations có thể chuẩn bị theo support model chưa thống nhất.

Đây là **stakeholder decision debt**: số decision material đã đến lúc cần authority/feedback nhưng vẫn bị giữ ở trạng thái implicit. Debt này làm rework potential tăng theo thời gian vì nhiều downstream action phụ thuộc state chưa được chốt.

Một dashboard tốt không chỉ báo “awaiting sponsor”; nó cho thấy age, blocked value, latest-needed date và consequence nếu không quyết. Điều đó biến engagement từ activity mềm thành decision-flow management.

## Ví dụ scenario

Sponsor yêu cầu báo cáo mỗi ngày vì “không thấy tiến độ”. Thay vì chỉ tăng tần suất report, PM nên tìm information gap thực sự. Có thể sponsor không cần danh sách task mà cần forecast ngày UAT và dependency với vendor. Một dashboard nhỏ có milestone confidence, critical blocker và decision needed có thể giải quyết problem tốt hơn 20 trang status.

Một scenario khác: operations liên tục từ chối nhận handover vì “tài liệu chưa đủ”, trong khi project đã viết nhiều document. Root cause có thể là họ chưa được tham gia design support model và không tin mình có capability xử lý incident. Giải pháp cần joint readiness rehearsal và ownership alignment, không chỉ viết thêm tài liệu.

Một scenario thứ ba: vendor liên tục trả lời “đang xem xét” nhưng không commit resolution date. PM gửi thêm email mỗi ngày nhưng dependency vẫn trễ. Problem không còn là message frequency; communication path thiếu response expectation, escalation threshold và commercial leverage. Cần chuyển từ informal follow-up sang dependency/governance mechanism phù hợp.

## Stakeholder anti-patterns

Broadcast management là giả định gửi nhiều update sẽ tạo alignment. Executive shielding là che bad news khỏi sponsor để “không làm họ lo”. Stakeholder appeasement là hứa scope/date không realistic chỉ để tránh conflict. Engagement theater là workshop nhiều nhưng decision right không đổi. Translation bottleneck là để một người giữ toàn bộ semantic bridge. Handover dump là chuyển hàng trăm file nhưng không chuyển capability.

Các anti-pattern này đều có điểm chung: activity communication có vẻ cao nhưng information/decision quality thấp.

## Kết nối với software requirements

Stakeholder need là đầu vào quan trọng của requirement nhưng không đồng nghĩa requirement cuối cùng. Trong software project, xem thêm [Requirements Engineering](../computer_science/09_software_engineering/00_requirements_specification_and_engineering_process.md) để hiểu cách intent được biến thành acceptance criteria và traceable behavior.

## Mental model

> Stakeholder engagement là thiết kế feedback và influence network giữa project với những người định nghĩa, cung cấp, sử dụng hoặc chịu hệ quả của value. Communication tốt phải bảo toàn meaning, latency và accountability; knowledge transfer tốt phải biến information thành capability có owner sau transition.

Tiếp theo: [Integration, scope, requirements và change](./04_integration_scope_requirements_and_change.md).
