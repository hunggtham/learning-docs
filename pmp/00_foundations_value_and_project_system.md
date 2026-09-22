# 00 — Project, outcome, value và hệ thống tạo giá trị

## Vì sao cần một mental model trước khi học process

Nếu coi quản lý dự án (project management / 프로젝트 관리) là việc “làm schedule và theo dõi task”, ta sẽ dễ tối ưu hoạt động nhưng bỏ quên lý do dự án tồn tại. Dự án (project / 프로젝트) là một nỗ lực tạm thời nhằm tạo ra một sản phẩm, dịch vụ, khả năng hoặc kết quả mang tính riêng biệt. Tính tạm thời nói rằng dự án có boundary và sẽ kết thúc; tính riêng biệt nói rằng luôn có một mức bất định mà operation lặp lại không có cùng kiểu.

Vận hành (operations / 운영) tối ưu một hệ thống đang tồn tại để tạo kết quả ổn định và lặp lại. Project thay đổi hệ thống đó hoặc tạo ra một hệ thống mới. Một ngân hàng xử lý giao dịch mỗi ngày là operations; thay core banking hoặc triển khai eKYC mới là project. Sau khi eKYC đi production, phần giám sát và xử lý giao dịch hằng ngày lại chuyển dần sang operations.

Boundary này quan trọng vì tiêu chí thành công khác nhau. Operations ưu tiên ổn định, throughput và reliability. Project phải đồng thời quản lý learning, change, temporary coordination và transition sang trạng thái bền vững.

## Project tồn tại vì trạng thái hiện tại chưa đủ

Một project luôn bắt đầu từ một gap giữa current state và desired future state. Gap có thể là problem cần sửa, opportunity muốn khai thác, regulation bắt buộc đáp ứng hoặc strategic capability cần xây.

Mental model này quan trọng vì project không nên bắt đầu từ solution. “Triển khai AI chatbot” không phải problem statement. Problem có thể là support cost tăng, response time quá chậm hoặc nhân viên thiếu knowledge. Nếu solution được chọn trước khi hiểu gap, team dễ tối ưu technology thay vì outcome.

Một project tốt bắt đầu bằng câu hỏi: điều gì trong current system không đáp ứng objective, và evidence nào cho thấy future state tốt hơn?

## Problem framing phải phân biệt symptom, mechanism và constraint

Một symptom là điều ta quan sát được, ví dụ “customer complaint tăng”. Mechanism là chuỗi nguyên nhân khiến symptom xuất hiện, ví dụ routing sai làm request tới queue không phù hợp, thời gian xử lý tăng và khách phải gọi lại. Constraint là boundary không được vi phạm, ví dụ regulation, budget cap hoặc service-level obligation.

Nếu project định nghĩa problem bằng symptom rồi nhảy thẳng sang solution, ta có thể chữa sai tầng. “Complaint tăng nên cần chatbot” có thể vô nghĩa nếu root mechanism là billing data sai. Ngược lại, dành nhiều tháng phân tích root cause cũng không hợp lý nếu harm đang xảy ra và cần containment trước.

Problem framing tốt vì vậy có hai output: một causal hypothesis đủ để chọn intervention và một danh sách assumption cần được kiểm chứng. Project không cần biết toàn bộ truth trước khi bắt đầu, nhưng phải biết mình đang giả định điều gì.

## Option space và premature commitment

Mỗi khi organization commit vào một solution, contract, architecture hoặc supplier, một phần option space biến mất. Commitment không xấu; project không thể tiến nếu mọi option luôn mở. Vấn đề là commit quá sớm khi information còn yếu.

Discovery, prototype, proof of concept hoặc pilot có thể được hiểu như cơ chế mua information trước khi đóng option. Nếu một test hai tuần có thể loại bỏ một architecture trị giá sáu tháng implementation, learning đó có economic value.

Mental model hữu ích là: giữ option mở khi uncertainty còn material và cost giữ option tương đối thấp; commit khi additional information không còn đủ giá trị để biện minh cho delay. Đây là cầu nối giữa foundations, lifecycle/tailoring và risk/decision ở các chapter sau.

## Output không phải outcome, outcome không tự động tạo value

Đầu ra (output / 산출물) là thứ nhóm dự án tạo ra: hệ thống, báo cáo, nhà máy, khóa đào tạo. Kết quả (outcome / 결과) là thay đổi xảy ra khi output được sử dụng. Giá trị (value / 가치) là mức lợi ích mà stakeholder hoặc tổ chức thực sự nhận được so với effort, cost và risk.

Ví dụ dự án giao đúng ngày một ứng dụng đặt lịch. “Ứng dụng đã deploy” là output. “Khách hàng đặt lịch online thay vì gọi điện” là outcome. “Giảm 30% thời gian nhân viên trực điện thoại và tăng tỷ lệ đặt lịch hoàn tất” mới gần với value. Vì vậy giao đủ scope chưa chứng minh dự án thành công nếu output không tạo outcome cần thiết.

Mental model hữu ích là:

```text
resources → work → outputs → adoption/use → outcomes → benefits/value
```

Project manager không kiểm soát hoàn toàn toàn bộ chuỗi, nhưng phải đảm bảo giả định giữa các mắt xích được nhìn thấy. Nếu value phụ thuộc vào adoption mà không ai quản lý đào tạo hoặc thay đổi quy trình, project có thể “xanh” trên dashboard nhưng thất bại ở business level.

## Benefits map và assumption chain

Chuỗi output → outcome → value chứa nhiều assumption. Nếu xây portal self-service, ta đang giả định user biết portal tồn tại, có thể đăng nhập, thấy đủ tiện lợi để đổi behavior và process nội bộ xử lý request đúng thời gian.

Benefits map làm các assumption này explicit. Điều này giúp risk management rộng hơn technical delivery. Một project có code hoàn hảo vẫn thất bại nếu adoption assumption sai.

Một assumption quan trọng cần owner, evidence và trigger review, không nên nằm ẩn trong business case.

## Benefit attribution và counterfactual

Một outcome tốt xảy ra sau project không tự động chứng minh project gây ra outcome đó. Revenue có thể tăng vì seasonality, regulation hoặc marketing campaign khác. Complaint có thể giảm do policy thay đổi đồng thời với system mới.

Counterfactual reasoning hỏi: nếu project không xảy ra thì điều gì có khả năng xảy ra? Không phải project nào cũng cần randomized experiment, nhưng benefit owner phải hiểu baseline, external driver và độ tin cậy của attribution.

Điều này quan trọng vì organization dễ “claim” benefit cho project thành công và đổ failure cho external environment. Benefit measurement có giá trị khi cùng một logic causal được dùng cho cả upside lẫn downside.

## Value không phân bố đều giữa stakeholder

Một project có thể tạo net value cho organization nhưng chuyển cost hoặc risk sang một stakeholder khác. Automation có thể giảm processing cost nhưng tăng workload kiểm tra cho operations. Một feature bảo mật có thể giảm fraud nhưng tăng friction cho customer. Outsourcing có thể giảm cost nội bộ nhưng tạo vendor concentration risk.

Vì vậy value không chỉ là một scalar duy nhất. Cần hỏi ai nhận benefit, ai chịu cost, ai gánh risk và ai có authority quyết trade-off. Đây là nơi stakeholder management, ethics và sustainability nối trực tiếp với business case.

Nếu total benefit cao nhưng harm tập trung vào một nhóm không có tiếng nói, “net positive” không tự động biến decision thành hợp lý. Mandatory legal, safety hoặc fairness boundary có thể giới hạn cách organization đánh đổi benefit.

## Success criteria cần nhiều tầng

Project success không phải một binary flag. Có ít nhất ba tầng thường cần phân biệt.

Delivery success hỏi project có giao agreed output trong constraint chấp nhận được hay không. Product/service success hỏi output có hoạt động và được sử dụng đúng như intended không. Business success hỏi outcome có tạo benefit/strategic value không.

Một project có thể giao trễ nhưng tạo value rất lớn; hoặc giao đúng scope/time/cost nhưng output không được dùng. Điều này không có nghĩa constraint không quan trọng, mà nghĩa success model phải rộng hơn iron triangle.

Success criteria còn cần time horizon. Một migration có thể thành công ngày cutover nhưng thất bại ba tháng sau nếu support cost tăng mạnh. Một AI pilot có metric đẹp trong 1.000 case nhưng drift ở production. Vì vậy “success at handover” và “benefit realized sustainably” là hai câu hỏi khác nhau.

## Constraint không phải mục tiêu

Scope, schedule và cost thường được gọi chung là các constraint kinh điển. Chúng giới hạn solution space nhưng không nên bị nhầm với purpose. Nếu một thay đổi nhỏ về scope tạo gấp đôi business value với chi phí chấp nhận được, tư duy máy móc “không được thay baseline” có thể làm hỏng dự án. Ngược lại, thay scope tùy tiện mà không hiểu impact cũng làm mất khả năng kiểm soát.

Điều cần bảo vệ là sự nhất quán giữa objective, constraint, risk appetite và value. Baseline tồn tại để tạo một reference point cho reasoning, không phải để ngăn learning.

Constraint cũng không có cùng độ cứng. Legal deadline khác target date; safety requirement khác optional feature; budget cap khác cost forecast. Project manager phải hiểu source và negotiability của mỗi constraint.

## Trade-off là bản chất, không phải dấu hiệu quản lý kém

Project luôn có resource hữu hạn và objective cạnh tranh. Tăng quality có thể cần thời gian/cost; giảm schedule có thể tăng risk; thêm scope có thể giảm focus.

Quản lý dự án không loại bỏ trade-off. Nó làm trade-off visible để đúng authority quyết định. Một project “không có trade-off” thường chỉ đang giấu chúng dưới overtime, technical debt hoặc risk chưa được report.

Trade-off cũng có second-order effect. Cắt testing để giữ deadline có thể không chỉ tăng defect risk; nó còn làm operations thiếu confidence, kéo dài hypercare và khiến vendor dispute về acceptance. Một local saving có thể tạo system cost lớn hơn ở downstream.

## Project như một hệ thống quyết định tạm thời

Một dự án gồm nhiều vòng feedback: stakeholder cung cấp nhu cầu, team tạo increment/deliverable, evidence được thu thập, risk và assumption được cập nhật, rồi kế hoạch thay đổi. Vì thế project management có thể được nhìn như một hệ thống ra quyết định dưới bất định.

Một hệ thống tốt cần ít nhất bốn thứ. Thứ nhất là shared direction để biết “tại sao”. Thứ hai là decision rights để biết “ai có quyền quyết”. Thứ ba là feedback loop để phát hiện deviation và learning. Thứ tư là escalation path để xử lý tình huống vượt authority hoặc tolerance.

Nếu thiếu direction, team bận rộn nhưng local optimization. Nếu thiếu decision rights, việc nhỏ cũng bị chờ. Nếu thiếu feedback, sai lệch chỉ lộ ra cuối dự án. Nếu thiếu escalation, blocker sống quá lâu và biến thành crisis.

## Project như control system

Có thể nhìn project theo control-system analogy:

```text
target state → plan/action → actual state → measurement → comparison → adjustment
```

Nếu target không rõ, control vô nghĩa. Nếu measurement chậm, response trễ. Nếu authority không cho adjustment, feedback loop tồn tại nhưng không có adaptation.

Predictive và adaptive delivery khác nhau chủ yếu ở cadence, placement của feedback và mức commitment, nhưng cả hai đều cần control loop.

## Sensor, actuator và latency

Control-system analogy sâu hơn khi tách ba phần. Sensor là mechanism tạo evidence: test, metric, stakeholder feedback, audit, forecast. Actuator là khả năng thay đổi system: reprioritize backlog, reallocate resource, change vendor, update baseline hoặc escalate. Latency là thời gian từ khi state xấu xuất hiện tới khi evidence tới người có quyền và action xảy ra.

Một project có dashboard tốt nhưng không có authority điều chỉnh chỉ có sensor mà thiếu actuator. Một project có sponsor mạnh nhưng report trễ ba tuần có actuator nhưng sensor latency quá cao. Reliability của control loop phụ thuộc cả ba, không chỉ số lượng report.

## Decision rights và escalation

Một system tốt không đưa mọi decision lên sponsor. Reversible, low-impact decision nên được đưa gần nơi có information. High-impact, irreversible hoặc tolerance-breaking decision cần governance mạnh hơn.

Escalation không phải failure của PM. Nó là mechanism khi decision vượt authority hoặc cross-boundary. Failure là escalate quá sớm mọi việc hoặc giữ issue quá lâu chỉ để chứng minh mình “tự xử lý được”.

## Project manager không phải người làm mọi decision

Project manager thiết kế coordination và integration, nhưng authority phân tán. Product owner quyết priority trong product context; architect có technical authority; compliance có control boundary; sponsor quyết strategic trade-off; functional manager có resource authority.

PMP mindset trưởng thành là biết ai nên quyết, information nào họ cần và khi nào decision phải xảy ra.

## Strategy, portfolio và project

Strategy định hướng organization muốn đi đâu. Portfolio lựa chọn investment nào đáng làm để thực thi strategy. Program phối hợp nhiều initiative liên quan. Project tạo một change cụ thể.

Nếu project không còn align strategy, “hoàn thành plan” có thể không còn giá trị. Đây là lý do business environment và business case phải được reassess khi context thay đổi.

## Project, program, portfolio và product

Chương trình (program / 프로그램) phối hợp nhiều project và hoạt động liên quan để đạt benefit không thể đạt tối ưu nếu quản lý từng project riêng lẻ. Danh mục (portfolio / 포트폴리오) là tập hợp investment được quản lý để phù hợp strategy; các thành phần không nhất thiết phụ thuộc kỹ thuật vào nhau. Sản phẩm (product / 제품) có vòng đời dài hơn một project và có thể được phát triển qua nhiều project hoặc continuous product delivery.

Sự khác biệt cốt lõi nằm ở câu hỏi quản trị. Project hỏi “làm thay đổi cụ thể này thế nào?”. Program hỏi “phối hợp các thay đổi liên quan ra sao để đạt benefit?”. Portfolio hỏi “tổ chức nên đầu tư vào đâu?”. Product hỏi “làm thế nào tạo và duy trì value liên tục cho customer/user?”.

Một product có thể sống qua nhiều project; một project có thể tạo capability cho nhiều product. Boundary không phải lúc nào cũng clean, vì vậy governance cần nói rõ temporary project kết thúc ở đâu và long-lived ownership bắt đầu ở đâu.

## Business case, charter và authorization

Business case giải thích vì sao investment có lý: problem/opportunity, expected benefit, cost, risk và alternatives. Project charter (hiến chương dự án / 프로젝트 헌장) chính thức hóa project và trao authority cho project manager trong boundary đã thống nhất. Hai artifact này liên quan nhưng không thay thế nhau: business case biện minh investment; charter thiết lập quyền hạn và direction ở cấp project.

Một charter tốt không cần dài. Nó phải đủ để tránh một dự án “đã bắt đầu làm” nhưng chưa ai đồng ý rõ objective, sponsor, success criteria hoặc authority.

Business case nên sống đủ lâu để bị challenge. Nếu market, regulation hoặc technology làm assumption thay đổi lớn, governance cần hỏi investment còn đáng tiếp tục không.

## Continue, pivot hay stop là decision bình thường

Một business case sống không chỉ hỗ trợ decision “tiếp tục”. Nó phải cho phép pivot, pause hoặc stop khi future value không còn biện minh future cost/risk.

Stop criteria đặc biệt quan trọng với project có sunk cost lớn. Nếu organization chỉ định nghĩa success path mà không định nghĩa evidence nào làm investment không còn đáng tiếp tục, sunk-cost bias dễ biến project thành zombie initiative.

Stop không nhất thiết nghĩa project management thất bại. Một discovery project có thể thành công nếu chứng minh sớm rằng hypothesis không viable và tránh hàng năm investment sai. Value của learning đôi khi nằm ở việc biết điều gì không nên làm.

## Temporary organization và transaction cost

Project tạo ra một temporary social system: người từ nhiều function được ghép lại để tạo change. Temporary structure cho phép focus nhưng cũng tạo transaction cost: onboarding, meeting, reporting, cross-functional negotiation, tool access và handoff.

Khi project kéo dài quá lâu hoặc số workstream quá nhiều, coordination cost có thể tăng nhanh hơn delivery capacity. Thêm người không chỉ tăng resource; nó tăng communication path và integration need.

Đây là lý do team topology, interface rõ và artifact tốt có economic value: chúng giảm transaction cost của temporary organization.

## Transition debt

Khi project kết thúc, temporary system giải tán nhưng capability phải sống ở đâu đó. Nếu operations chỉ được kéo vào cuối, support model, monitoring, ownership và tacit knowledge chưa sẵn sàng, project tích transition debt.

Transition debt giống technical debt ở chỗ output có thể “xong” nhưng future cost bị đẩy sang operations. Nó xuất hiện dưới dạng incident kéo dài, phụ thuộc developer cũ, manual workaround hoặc benefit chưa đo được.

Transition cần owner bên operations, product hoặc business. Closure vì vậy phải được nghĩ từ đầu, không phải cuối project mới hỏi “ai vận hành?”.

## Complexity không chỉ là project lớn

Project phức tạp có thể do số stakeholder, dependency, technology uncertainty, regulatory coupling hoặc organizational politics, không chỉ budget/headcount.

Complex system tạo emergent behavior: một change nhỏ có thể lan qua nhiều boundary. Điều này làm system thinking quan trọng hơn việc tối ưu từng knowledge area riêng lẻ.

Khi complexity cao, decomposition vẫn cần nhưng phải giữ integration view. Chia project thành 20 workstream không loại bỏ dependency giữa chúng.

## Feedback loop và second-order effect

Trong complex project, action có thể thay chính system đang được quản lý. Thêm approval để giảm risk có thể tăng latency; latency làm team workaround; workaround làm evidence kém; evidence kém lại khiến governance thêm approval. Đây là reinforcing loop có thể làm bureaucracy tăng mà control thực tế giảm.

Ngược lại, một improvement có thể tạo virtuous loop. Automated test làm feedback nhanh hơn, defect giảm, release confidence tăng, batch nhỏ hơn và learning nhanh hơn.

System thinking hỏi không chỉ “action này giải issue hiện tại không?” mà còn “behavior nào nó khuyến khích và feedback loop nào nó tạo?”.

## Uncertainty và learning

Bất định không phải failure của planning. Nó là trạng thái tự nhiên khi làm điều mới.

Good planning nói rõ cái gì đã biết, cái gì estimate, assumption nào quan trọng và feedback nào sẽ giảm uncertainty. Bad planning trình bày uncertainty như certainty để tạo cảm giác kiểm soát.

Project maturity không phải dự đoán đúng mọi thứ từ đầu mà là phát hiện deviation sớm và điều chỉnh có kỷ luật.

## Ethics là nền của information quality

Project manager phụ thuộc vào truthful information. Nếu team che defect, vendor giấu delay hoặc PM làm forecast đẹp để tránh pressure, control system mất sensor.

Ethics vì vậy không phải chapter phụ. Truthfulness, fairness và professional responsibility ảnh hưởng trực tiếp tới decision quality và governance.

Ethics cũng là boundary của value optimization. Một option tạo ROI cao nhưng cần che material risk, vi phạm consent hoặc chuyển harm không hợp lý sang nhóm yếu thế không trở thành lựa chọn tốt chỉ vì financial metric đẹp.

## Ví dụ reasoning

Giả sử công ty muốn “triển khai chatbot AI trong ba tháng”. Nếu nhảy thẳng vào schedule, ta đang chấp nhận hàng loạt assumption chưa kiểm tra. Chatbot giải quyết problem nào? Success là giảm ticket, tăng conversion hay chỉ demo công nghệ? Dữ liệu nào được phép dùng? Ai chịu trách nhiệm nếu model trả lời sai? Adoption được đo ra sao? Ba tháng là deadline business thật hay chỉ target ban đầu?

Quản lý dự án tốt biến câu “làm chatbot” thành một chuỗi giả thuyết có thể kiểm chứng: outcome mong muốn, stakeholder, constraints, risks, measurement và delivery approach. Sau đó mới chọn process phù hợp.

Giả sử pilot cho thấy ticket giảm nhưng customer complaint tăng vì câu trả lời sai. Delivery output vẫn hoạt động, nhưng outcome/value model có conflict. Team cần đánh giá harm, human review, scope và business case thay vì chỉ hỏi “có kịp ba tháng không?”.

Một bước reasoning sâu hơn là hỏi counterfactual: complaint có tăng vì chatbot hay vì campaign tạo volume bất thường? Nếu model chỉ tốt ở nhóm low-risk query, limited rollout có tạo value tốt hơn binary go/no-go không? Nếu human review làm cost quay về gần baseline, business case còn đứng vững không? Project manager không tự quyết mọi câu hỏi này, nhưng phải đưa đúng evidence tới đúng decision owner.

## Mental model

> Project management không phải quản lý danh sách task. Nó là thiết kế và vận hành một hệ thống quyết định tạm thời để biến investment thành outcome có giá trị trong điều kiện bất định, đồng thời giữ đủ option để học, đủ control để bảo vệ constraint và đủ evidence để dừng khi investment không còn hợp lý.

Chương tiếp theo giải thích vì sao mức bất định quyết định vòng đời và cách giao hàng: [Lifecycle, delivery approach và tailoring](./01_lifecycle_delivery_approaches_and_tailoring.md).