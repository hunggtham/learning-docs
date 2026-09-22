# 08 — Risk, uncertainty, issue và decision making

## Risk là uncertainty có effect lên objective

Rủi ro (risk / 위험) là một sự kiện hoặc điều kiện chưa chắc chắn có thể ảnh hưởng tích cực hoặc tiêu cực tới objective. Issue (vấn đề đang xảy ra / 이슈) là condition đã xảy ra hoặc đang tồn tại và cần xử lý. Nhầm risk với issue làm response sai timing: risk cần preparation; issue cần action.

“Vendor có thể giao trễ” là risk. “Vendor vừa xác nhận trễ hai tuần” là issue. Khi trigger xuất hiện, item chuyển từ monitoring/response readiness sang execution/escalation.

Risk không tồn tại độc lập với objective. Cùng một event có thể là threat với một objective nhưng gần như irrelevant với objective khác. Vì vậy risk statement nên luôn gắn với impact thực tế lên value, scope, schedule, cost, quality, compliance hoặc reputation.

## Uncertainty không chỉ là event risk

Không phải mọi uncertainty đều dễ viết thành một event. Ambiguity xuất hiện khi ta chưa hiểu problem hoặc requirement. Variability xuất hiện khi duration, demand hoặc defect rate dao động tự nhiên. Complexity xuất hiện khi nhiều dependency tương tác khiến behavior khó dự đoán. Unknown unknown là vùng mà team chưa biết mình thiếu knowledge gì.

Event risk có thể đưa vào register. Variability thường cần range, reserve hoặc probabilistic model. Ambiguity cần discovery, prototype hoặc expert input. Complexity cần decomposition, interface management và feedback nhanh. Unknown unknown cần resilience, contingency capacity và khả năng phát hiện anomaly sớm.

Gọi tất cả là “risk” nhưng dùng cùng một response làm mất chất lượng reasoning.

Một cách phân biệt sâu hơn là epistemic uncertainty — uncertainty vì thiếu knowledge và có thể giảm bằng learning — với aleatory variability — variation vốn có không biến mất chỉ vì nghiên cứu thêm. Prototype có thể giảm epistemic uncertainty về API compatibility; nó không loại bỏ natural variability của transaction volume. Hai loại uncertainty cần intervention khác nhau.

## Risk management là làm uncertainty có thể hành động

Risk identification tốt không phải tạo một danh sách dài “có thể xảy ra”. Mỗi risk nên đủ causal để action: cause → uncertain event → effect. Ví dụ “do API regulator chưa ổn định, interface có thể thay trong UAT, dẫn tới rework và delay go-live”. Cấu trúc này gợi response tốt hơn từ “integration risk”.

Risk register là working model gồm owner, probability/impact, response, trigger và status. Nó mất giá trị nếu chỉ được cập nhật trước governance meeting.

Risk owner là người chịu trách nhiệm theo dõi và bảo đảm risk được quản lý; action owner có thể là người thực hiện một response cụ thể. Hai vai trò có thể là một hoặc khác nhau. Nếu register chỉ có “owner” nhưng không ai hiểu trách nhiệm là gì, item dễ bị treo.

## Risk model quality quan trọng hơn số lượng risk

Một risk register 200 dòng có thể kém hơn 30 risk có causal logic rõ. Chất lượng model phụ thuộc vào boundary, dependency, assumptions và ability to update khi evidence đổi.

Duplicate risk làm exposure bị double-count. Risk quá broad làm owner không biết response. Risk quá granular tạo noise. Một risk tốt phải đủ cụ thể để có control nhưng đủ rộng để giữ causal consequence quan trọng.

Register cũng phải phân biệt source risk và symptom risk. “UAT có thể trễ” có thể chỉ là consequence của environment instability, vendor response latency và requirement churn. Nếu chỉ mitigate symptom bằng overtime, underlying exposure còn nguyên.

## Risk identification cần nhìn theo nhiều lớp

Một workshop chỉ hỏi “có risk gì?” thường tạo list nông. Có thể scan theo nguồn: technical, people, vendor, schedule, financial, compliance, security, market, organization, external dependency và transition. Có thể scan theo lifecycle: discovery, build, integration, test, release, adoption và operations handover.

Pre-mortem cũng hữu ích: giả sử sáu tháng sau project thất bại, điều gì có thể đã xảy ra? Cách này giúp team nói ra concern khó nêu khi mọi người đang quá committed với plan.

Near miss và weak signal cũng là nguồn identification. Một environment outage chỉ kéo dài 10 phút và chưa ảnh hưởng milestone có thể là signal của systemic reliability risk. Nếu organization chỉ học từ loss thật, learning cost sẽ cao hơn cần thiết.

## Risk dimensions ngoài probability × impact

Probability và impact là hai dimension phổ biến nhưng không phải toàn bộ. Risk velocity nói effect xảy ra nhanh tới mức nào sau trigger. Proximity nói risk có thể materialize gần hay xa. Detectability nói team có khả năng thấy signal sớm hay không. Controllability nói team có influence thực sự lên cause/impact không.

Một risk probability trung bình nhưng velocity cực nhanh và detectability thấp có thể cần stronger prevention hơn risk probability cao nhưng consequence phát triển chậm và dễ contain.

Không nhất thiết phải biến mọi dimension thành score. Mục tiêu là tránh flatten mọi risk thành một ô màu.

## Qualitative và quantitative analysis

Qualitative analysis dùng relative scales để prioritize. Probability-impact matrix hữu ích để tập trung attention nhưng dễ tạo false precision nếu scale không calibrated.

Expected Monetary Value (EMV) cho decision đơn giản:

```text
EMV = Probability × Impact
```

Nếu 20% khả năng outage gây tổn thất 100 triệu, EMV kỳ vọng là 20 triệu. Nhưng two risks cùng EMV có tail profile rất khác; catastrophic low-probability risk có thể cần response mạnh hơn risk nhỏ lặp lại.

Decision tree giúp so option có branch probability/cost. Monte Carlo simulation có thể mô hình distribution của schedule/cost khi nhiều uncertainty kết hợp. Tool không thay risk judgment; nó làm assumption explicit và aggregation tốt hơn.

Correlation là điểm dễ bị bỏ qua. Nếu ba risk đều cùng phụ thuộc một vendor hoặc cùng xảy ra khi market biến động, cộng EMV như các event độc lập có thể đánh giá thấp tail risk.

## Risk-adjusted value thay vì expected value đơn thuần

Hai option có cùng expected value nhưng distribution khác nhau có thể không tương đương với organization. Option A có upside vừa phải và downside bounded; option B có upside lớn nhưng tail có thể gây compliance breach hoặc mất khả năng thanh toán. Risk appetite/capacity làm preference khác nhau.

Vì vậy EMV là input, không phải quyết định. Risk-adjusted reasoning phải nhìn downside severity, reversibility, liquidity/capacity, mandatory boundary và concentration exposure.

Một organization không có capacity hấp thụ một loss 1 tỷ không nên hành xử như thể 1% × 1 tỷ chỉ đơn giản là 10 triệu expected cost.

## Scenario analysis: không ép uncertainty thành một số duy nhất

Khi probability chưa đủ tốt để mô hình chi tiết, scenario analysis có thể hữu ích hơn việc tạo một con số giả chính xác. Team xây một vài future state có logic nội tại, chẳng hạn base case, downside case và severe-but-plausible case, rồi hỏi project có còn viable trong mỗi state không.

Scenario không phải ba con số tùy ý quanh estimate trung bình. Mỗi scenario nên thay đổi một nhóm driver có causal relation: regulation chậm phê duyệt, vendor capacity giảm, adoption thấp hoặc FX biến động. Mục tiêu là kiểm tra robustness của plan và tìm assumption nào làm decision đảo chiều.

Một project chỉ “tốt” trong best case nhưng mất viability ngay khi adoption thấp hơn 10% đang có fragility mà một single-point forecast che mất.

## Stress test và break point

Scenario analysis có thể đi thêm một bước: thay vì hỏi outcome ở vài scenario cố định, hỏi parameter nào làm decision đổi. Adoption thấp tới mức nào thì NPV không còn dương? Vendor delay bao lâu thì legal deadline không thể recover? Defect rate nào làm manual fallback vượt capacity?

Break point biến discussion từ “risk cao hay thấp” thành “system chịu được tới đâu”. Đây là bridge giữa risk, finance, schedule và operations readiness.

## Monte Carlo: từ một finish date sang distribution

Monte Carlo simulation không “dự đoán ngày hoàn thành chính xác”. Nó chạy nhiều iteration bằng cách sample duration/cost từ distribution đã định cho các activity/risk, rồi tạo distribution của outcome tổng.

Ví dụ thay vì nói project sẽ hoàn thành ngày 30/11, simulation có thể cho:

```text
P50 finish: 30/11
P80 finish: 12/12
P90 finish: 20/12
```

P80 nghĩa trong model có khoảng 80% iteration hoàn thành không muộn hơn mốc đó. Nó không phải guarantee 80% ngoài đời; chất lượng phụ thuộc network, distribution, correlation và assumptions đầu vào.

Một lỗi phổ biến là sample mỗi activity độc lập dù nhiều activity cùng phụ thuộc một resource hoặc vendor. Khi correlation bị bỏ qua, tail thường trông đẹp hơn reality. Một lỗi khác là dùng distribution quá hẹp chỉ vì team không muốn forecast xấu.

Monte Carlo hữu ích nhất khi decision cần probability language: cần contingency bao nhiêu để đạt confidence target, milestone nào có tail lớn, hoặc risk response nào làm distribution thu hẹp đáng kể.

## Sensitivity và tornado thinking

Simulation tạo nhiều output, nhưng management vẫn cần biết driver nào quan trọng nhất. Sensitivity analysis đo outcome thay đổi mạnh ra sao khi input thay đổi. Tornado chart thường sắp các driver theo mức ảnh hưởng để attention đi vào leverage point thay vì risk có tên đáng sợ nhất.

Nếu finish date nhạy nhất với regulatory approval và integration test duration, thêm buffer vào low-impact documentation task không giải quyết uncertainty chính. Nếu cost forecast nhạy với FX nhưng team chỉ thảo luận overtime, risk conversation đang lệch driver.

Sensitivity không chứng minh causation tuyệt đối, nhưng giúp ưu tiên nơi nên mua thêm information hoặc response.

## Probability không phải frequency đơn giản

Trong project, probability thường là judgment dựa trên evidence không đầy đủ. Vì vậy numeric score cần calibration. Nếu team gọi gần như mọi risk là “medium”, matrix không tạo priority. Nếu probability 30% chỉ là cảm giác nhưng dashboard hiển thị 0.30 như số đo khoa học, organization đang tạo false precision.

Điều quan trọng là consistency của scale và quality của evidence, không phải số chữ số thập phân.

Calibration có thể học theo thời gian. Nếu một team liên tục gắn “20%” cho risk nhưng gần một nửa risk đó xảy ra, scale hoặc judgment đang miscalibrated. Decision log và historical outcomes giúp cải thiện forecasting skill.

## Threat response và opportunity response

Threat có thể avoid, mitigate, transfer, accept hoặc escalate. Opportunity có thể exploit, enhance, share, accept hoặc escalate. Chọn response dựa trên expected value, controllability, cost và risk appetite.

Mitigation làm probability hoặc impact giảm trước khi event xảy ra. Contingency plan được kích hoạt khi trigger xảy ra. Workaround thường là response cho issue không có planned response phù hợp.

Transfer không làm risk biến mất khỏi project outcome. Bảo hiểm hoặc contract có thể chuyển financial consequence, nhưng schedule hoặc reputation effect vẫn có thể ở lại. Đây là lý do transfer phải được hiểu theo loại exposure cụ thể.

## Control taxonomy: preventive, detective, corrective

Preventive control cố giảm khả năng event xảy ra. Detective control làm signal xuất hiện nhanh hơn. Corrective control giảm consequence sau khi event xảy ra.

Một project mature không chỉ hỏi “có response không?” mà hỏi control nằm ở đâu trên causal chain. Ví dụ duplicate data validation có thể prevent bad input, monitoring phát hiện anomaly và rollback giảm impact.

Bow-tie reasoning hữu ích vì nó đặt event ở giữa: bên trái là cause/preventive barrier; bên phải là consequence/mitigating barrier. Nó giúp thấy project đang dựa quá nhiều vào một control duy nhất hay không.

## Control effectiveness phải được kiểm chứng

Có control trên giấy không có nghĩa control hoạt động. Backup là control chỉ khi restore đã được test. Vendor fallback là control chỉ khi alternate supplier thực sự có capacity. Escalation path là control chỉ khi người nhận có authority và response time phù hợp.

Risk review nên hỏi evidence về control effectiveness, không chỉ status “implemented”. Control có thể degrade theo thời gian, đặc biệt khi configuration, people hoặc vendor version thay đổi.

## Residual và secondary risk

Response có thể không loại bỏ risk hoàn toàn; phần còn lại là residual risk. Response cũng có thể tạo secondary risk. Ví dụ duplicate vendor để giảm supply risk làm tăng integration/coordination risk. Risk management trưởng thành luôn hỏi “response này tạo failure mode mới nào?”.

Một response chỉ hợp lý khi tổng exposure sau response, gồm residual và secondary risk, tốt hơn trạng thái trước đó so với cost bỏ ra.

## Risk capacity, appetite, threshold và tolerance

Risk capacity là mức loss/exposure tối đa system thực tế có thể chịu trước khi viability bị đe dọa. Risk appetite nói mức risk organization sẵn sàng nhận để theo đuổi objective. Threshold/tolerance chuyển preference thành boundary hành động cụ thể.

Capacity và appetite không giống nhau. Organization có thể có capacity chịu delay một tháng nhưng appetite chỉ chấp nhận một tuần vì strategic timing. Ngược lại, leadership có thể muốn nhận risk lớn hơn capacity thực tế; governance tốt phải surface inconsistency đó.

Ví dụ organization có thể chấp nhận schedule variance vài ngày nhưng zero tolerance với privacy breach. Hai risk cùng probability không thể được xử lý bằng cùng priority rule.

## Reserve và buffer: bảo vệ plan khỏi uncertainty

Contingency reserve thường dành cho known-unknowns đã được nhận diện; management reserve bao quát unknown-unknowns hoặc uncertainty ở mức cao hơn tùy governance của tổ chức. Schedule buffer cũng có vai trò tương tự: nó hấp thụ variability thay vì giả định mọi estimate xảy ra đúng giá trị trung bình.

Reserve không phải “padding bí mật”. Nếu buffer bị giấu trong từng estimate, team khó biết true forecast và risk exposure. Reserve nên có purpose, owner và rule sử dụng rõ.

Reserve cũng không nên được tính bằng cách cộng mechanical mọi EMV rồi coi tổng đó là đủ. Correlation, tail risk, non-monetary impact và confidence target có thể làm required reserve khác đáng kể expected value trung bình.

Reserve consumption cần liên hệ risk retirement. Nếu contingency đã tiêu nhưng exposure chưa giảm, project đang mất protection. Nếu risk đã retire mà reserve vẫn bị giữ không cần thiết, forecast có thể quá conservative.

## Risk exposure trend và risk burndown

Một snapshot risk register không cho biết system đang khỏe lên hay xấu đi. Có thể theo dõi exposure trend theo thời gian: tổng weighted exposure, số risk vượt threshold, expected loss hoặc distribution percentile tùy context.

Risk burndown không có nghĩa số risk phải luôn giảm. Trong discovery tốt, số risk có thể tăng vì team nhìn thấy reality rõ hơn. Signal tích cực là uncertainty quan trọng được retire, response effectiveness tăng và residual exposure phù hợp appetite.

Nếu team “đóng risk” để dashboard đẹp trong khi assumption chưa được kiểm chứng, metric trở thành gaming.

## Risk interaction và risk cascade

Risk có thể gây risk khác. Vendor delay có thể ép compression schedule; compression lại tăng defect risk; defect tăng khả năng failed UAT; failed UAT ảnh hưởng regulatory deadline. Nếu register tách từng risk nhưng không thấy causal chain, response dễ local.

Một dependency map hoặc bow-tie reasoning giúp nhìn root cause, preventive control, event và consequence. Mục tiêu là chọn control ở nơi có leverage lớn nhất.

## Systemic risk và common-cause failure

Một portfolio dự án có thể tưởng đang diversified vì dùng nhiều team khác nhau nhưng thực tế cùng phụ thuộc một cloud region, một vendor identity provider, một key architect hoặc một regulatory approval queue. Đây là common-cause risk.

Ở project level cũng vậy: nhiều workstream có thể trông độc lập nhưng cùng tranh một environment hoặc specialist. Nếu shared dependency fail, nhiều path cùng fail. Register theo workstream riêng có thể che systemic exposure.

Cách xử lý là map shared dependency và failure domain, không chỉ tăng số item trong risk register.

Concentration risk còn có thể nằm ở assumption. Nhiều benefit case có vẻ khác nhau nhưng cùng phụ thuộc adoption growth. Nếu adoption assumption sai, nhiều benefit cùng collapse.

## Robustness, resilience và recoverability

Prediction không thể loại bỏ surprise. Robustness là khả năng system vẫn hoạt động khi input thay đổi trong một range. Resilience là khả năng hấp thụ shock và phục hồi. Recoverability là tốc độ/capability quay về trạng thái acceptable sau failure.

Redundancy, slack, modularity, fallback, cross-training và rollback đều có thể là resilience investment. Chúng nhìn giống “inefficiency” nếu chỉ tối ưu utilization/cost bình thường, nhưng tạo option khi uncertainty materialize.

Risk management trưởng thành cân preventive efficiency với recovery capability. Một system không bao giờ fail là mục tiêu không thực tế; một system fail nhưng recover nhanh có thể tạo business outcome tốt hơn.

## Issue management và impediment

Issue log theo dõi owner, priority, due date, impact và resolution. Impediment/blocker là trở ngại làm team không thể hoặc khó tiến. Project manager nên ưu tiên remove system impediment hơn thúc từng người “làm nhanh hơn”.

Một issue recurring thường chỉ ra systemic cause. Nếu mỗi sprint environment lại hỏng, workaround liên tục không đủ; cần đầu tư vào environment reliability.

Khi risk trở thành issue, register không nên chỉ chuyển status sang “occurred” rồi bỏ. Team cần execute response, cập nhật forecast, reassess secondary risk và communicate impact tới người có decision right.

## Triage: contain trước, diagnose sau khi harm đang lan

Khi issue gây active harm, thứ tự có thể khác risk analysis bình thường. Containment giảm blast radius trước khi root-cause analysis hoàn tất. Security incident có thể cần revoke access trước khi biết chính xác attacker path; failed release có thể cần rollback trước post-mortem.

Triage nên dựa trên severity, velocity, reversibility và stakeholder exposure. Không phải mọi issue cần war room; nhưng slow analysis trong fast-moving failure cũng là risk.

Sau containment, team vẫn phải diagnose và sửa system. Nếu chỉ dập lửa rồi quay lại business-as-usual, recurring issue trở thành normalized failure.

## Crisis và decision compression

Trong crisis, information không đầy đủ nhưng decision deadline ngắn. Governance cần pre-defined authority, communication channel và safe default để tránh mọi action chờ escalation chain bình thường.

Crisis không phải lúc thích hợp để invent toàn bộ operating model. Tabletop exercise và pre-agreed threshold giúp organization biết ai chỉ huy, ai communicate và condition nào trigger fallback.

Sau crisis, temporary emergency authority phải được retire; nếu không, exception dễ biến thành permanent shadow governance.

## Decision under uncertainty

Khi thiếu information, câu hỏi không phải “làm sao biết chắc?” mà là “information nào đáng mua thêm?”. Prototype, spike, pilot, expert review hoặc experiment đều có information value. Một test hai ngày có thể đáng làm nếu tránh commitment sáu tháng.

Reversible decision nên được decentralize và thực hiện nhanh hơn. Irreversible/high-impact decision cần evidence và review mạnh hơn. Đây là cách liên kết decision cost với governance.

Value of Information có thể reasoning định tính: nếu một thử nghiệm rẻ có khả năng thay đổi một decision rất đắt, test thường đáng làm. Nếu dù kết quả nào decision cũng không đổi, thu thêm data chỉ trì hoãn action.

## Decision regret và cost of waiting

“Thu thêm information” cũng là một decision có cost. Trong market window ngắn, chờ certainty có thể làm option hết hạn. Trong safety issue, delay để phân tích thêm có thể tăng harm.

Decision reasoning cần cân expected regret hai phía: regret vì commit sai quá sớm và regret vì chờ quá lâu. Reversibility, information value và cost of delay quyết định balance.

Không tồn tại rule “luôn phân tích trước” hoặc “luôn hành động nhanh”. Context quyết định information threshold phù hợp.

## Real options: giữ quyền lựa chọn có thể có giá trị

Trong uncertainty cao, value không chỉ đến từ chọn option “tốt nhất” hôm nay mà còn từ giữ khả năng đổi hướng khi có thêm information. Pilot nhỏ, architecture modular, contract có exit clause hoặc phased investment đều có thể tạo option value.

Một commitment lớn không đảo ngược có thể rẻ hơn nominally nhưng làm mất flexibility. Một approach đắt hơn chút nhưng cho phép stop/pivot sau milestone có thể tốt hơn nếu uncertainty lớn.

Real-options thinking không có nghĩa trì hoãn mọi decision. Option cũng có cost và expiry. Câu hỏi là flexibility có đáng giá hơn cost giữ option không.

## Decision quality khác outcome quality

Một quyết định tốt vẫn có thể cho outcome xấu vì uncertainty; một quyết định tệ đôi khi may mắn cho outcome tốt. Nếu team chỉ đánh giá decision theo kết quả cuối, họ dễ học sai.

Post-decision review nên hỏi: information lúc đó là gì, assumption nào hợp lý, alternative nào được cân nhắc, risk threshold nào áp dụng và điều gì mới xuất hiện sau decision. Đây là nền tảng của organizational learning.

Decision log giúp chống hindsight bias. Sau khi biết outcome, con người dễ tin rằng result “rõ ràng từ đầu”. Ghi prediction, confidence và rationale tại thời điểm decision tạo evidence để học calibration thật.

## Cognitive bias trong risk decision

Optimism bias làm estimate quá đẹp. Anchoring khiến team bám con số đầu tiên. Availability bias làm event mới xảy ra được đánh giá quá cao. Sunk-cost effect khiến organization tiếp tục investment chỉ vì đã chi nhiều. Confirmation bias khiến team tìm evidence ủng hộ plan đã chọn.

Không thể loại bỏ bias hoàn toàn, nhưng có thể thiết kế countermeasure: independent review, range estimate, pre-mortem, explicit exit criteria và decision log.

Groupthink và authority bias cũng quan trọng. Nếu senior leader nói “vendor này chắc chắn ổn”, team có thể ngừng surface weak signal. Psychological safety ở chapter People vì vậy là một risk-control mechanism thực sự.

## Opportunity management không chỉ là “risk tích cực” trên giấy

Opportunity có thể là supplier sẵn capacity sớm, market demand tăng, reusable platform hoặc regulation mở option mới. Nếu opportunity chỉ được ghi vào register nhưng không có trigger/capacity để exploit, nó không tạo value.

Opportunity response cũng cạnh tranh resource với threat mitigation. Organization cần nhìn expected upside, strategic fit và option expiry. Một opportunity có thể biến thành threat nếu scale quá nhanh làm operations quá tải.

## Ví dụ scenario

Team phát hiện vendor OCR có accuracy thấp với giấy tờ cũ, nhưng chưa biết mức độ. Thay vì ngay lập tức đổi vendor hoặc chấp nhận risk, PM có thể thiết kế sample test đại diện, đo accuracy theo segment, estimate business impact, tìm fallback manual review và xác định threshold go/no-go. Đây là risk reduction bằng information.

Nếu kết quả cho thấy chỉ 2% document bị ảnh hưởng và manual review đủ capacity, mitigation có thể rẻ hơn đổi vendor. Nếu failure tập trung ở một loại giấy tờ bắt buộc và compliance không cho manual exception, risk profile thay đổi hoàn toàn. Cùng một technical symptom nhưng decision phụ thuộc impact model.

Một scenario schedule khác: deterministic plan nói go-live 30/11, nhưng simulation cho P50 là 30/11 và P80 là 12/12. Nếu contract penalty bắt đầu 5/12, quản lý không nên báo “on track 30/11” như một fact duy nhất. Cần surface confidence distribution, driver chính và option giảm tail—ví dụ early integration hoặc giảm shared-resource contention.

Một scenario resilience: payment API phụ thuộc một vendor đạt SLA 99.99%, nhưng không có degraded mode. Expected outage thấp, song mỗi outage chặn toàn bộ sales. Một fallback manual/queued processing có thể tạo nhiều value hơn việc mua thêm 0.005% SLA vì nó giảm consequence thay vì chỉ probability.

## Anti-patterns

Risk register dài nhưng không có owner là documentation theater. Chỉ theo dõi red risk nhưng bỏ correlation là nhìn từng cây mà mất rừng. Chỉ nói “monitor” mà không có trigger là trì hoãn decision. Escalate mọi risk làm governance overload; không escalate risk vượt tolerance lại là governance failure.

Dùng Monte Carlo với input giả chính xác cũng chỉ tạo false precision đẹp hơn. Dùng EMV như luật quyết định duy nhất bỏ qua tail, capacity, appetite và ethics. Control “implemented” nhưng chưa test là paper control. Reserve bị tiêu mà exposure không giảm là protection erosion.

Mục tiêu không phải có nhiều risk item hay nhiều chart mà là tạo preparedness, option, resilience và timely decision.

## Mental model

> Risk management không nhằm dự đoán đúng tương lai; nó xây một causal model đủ tốt để biết uncertainty nào cần học, control nào cần kiểm chứng, exposure nào system có thể chịu, option nào nên giữ và cách phục hồi khi surprise vượt prediction.

Tiếp theo: [Governance, compliance và business environment](./09_governance_compliance_and_business_environment.md).