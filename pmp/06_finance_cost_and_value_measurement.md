# 06 — Finance, cost, reserves và value measurement

## Cost management bắt đầu từ decision, không từ spreadsheet

Quản lý chi phí (cost management / 비용 관리) trả lời project cần bao nhiêu resource tài chính, khi nào cần, confidence ra sao, và deviation có ý nghĩa gì đối với value/business case. Budget không chỉ là trần chi tiêu; nó là một constraint gắn với scope, schedule, quality và risk.

Một project under budget vẫn có thể thất bại nếu không tạo outcome. Một project over initial estimate vẫn có thể hợp lý nếu expected value tăng nhiều hơn và governance chấp nhận trade-off. Vì vậy cost phải luôn được đọc trong hệ thống value–risk–scope chứ không riêng lẻ.

Finance ở project level không nhằm biến PM thành accountant. Mục tiêu là hiểu economic state đủ tốt để phân biệt “đã chi”, “đã cam kết sẽ chi”, “sắp cần cash”, “forecast sẽ vượt”, và “investment còn đáng tiếp tục hay không”. Những trạng thái này khác nhau nhưng thường bị trộn trên dashboard.

## Estimate, budget và funding

Cost estimate dự đoán chi phí work. Cost baseline là time-phased authorized budget dùng để đo performance, thường không gồm management reserve. Project budget rộng hơn có thể gồm management reserve. Funding requirement còn quan tâm thời điểm dòng tiền cần được cấp.

Nếu PM chỉ biết “tổng budget 1 tỷ” nhưng không biết khi nào contract milestone phải thanh toán, project vẫn có liquidity/timing problem.

Time-phasing quan trọng vì hai project cùng total cost có cash-flow profile khác nhau. Procurement deposit lớn ở đầu, construction payment theo milestone và cloud spend tăng dần theo scale cần funding strategy khác nhau.

## Estimate, commitment, accrual, actual và cash là năm state khác nhau

Estimate là kỳ vọng future cost. Commitment là obligation đã được tạo, ví dụ purchase order hoặc signed contract, dù cash chưa trả. Accrual/expense recognition phản ánh cost đã phát sinh theo accounting rule dù invoice/cash có thể chưa đi qua. Actual cost trong project-control system cần semantic definition rõ. Cash flow nói tiền thực sự vào/ra khi nào.

Ví dụ vendor hoàn thành milestone cuối tháng 9 nhưng invoice trả tháng 10. Operationally project đã incur cost tháng 9; cash ra tháng 10. Nếu dashboard chỉ nhìn bank payment, September có thể trông under budget giả.

Ngược lại project có thể trả deposit lớn trước delivery; cash đã ra nhưng earned progress chưa tương ứng. PM phải biết metric mình đang nhìn thuộc economic state nào.

## Committed cost là early-warning signal

Actual cost chỉ nhìn quá khứ. Committed cost cho thấy một phần future cost đã khó đảo ngược. Nếu project đã ký contract 80% budget dù mới chi 30%, “còn 70% budget chưa dùng” là statement gây hiểu lầm.

Forecast tốt nên reconcile actual + committed + uncommitted estimate. Khi scope change, cần biết phần nào còn flexible và phần nào đã lock bởi contract/cancellation clause.

## Direct, indirect, fixed và variable cost

Direct cost có thể gắn trực tiếp với project như vendor fee hoặc project labor. Indirect cost được chia sẻ như office, shared platform hoặc corporate overhead. Fixed cost không đổi đáng kể theo volume trong range nhất định; variable cost thay theo usage hoặc output.

Classification giúp estimate và business case nhưng không nên học máy móc. Cloud subscription có phần fixed và variable; internal employee cost có thể là sunk payroll ở organization nhưng vẫn có opportunity cost vì họ không làm việc khác.

Một cost cũng có thể behave khác theo decision horizon. Annual license đã trả có thể là sunk trong short-term continuation decision nhưng trở thành avoidable cost ở renewal decision.

## Opportunity cost

Opportunity cost là value của alternative tốt nhất bị bỏ khi chọn một option. Nếu một team senior làm project A, họ không thể đồng thời làm project B.

Project selection vì vậy không chỉ hỏi “A có positive ROI không?” mà còn “A có tốt hơn cách dùng resource khác không?”. Portfolio layer quản lý trade-off này rõ hơn project layer, nhưng PM cần hiểu khi resource scarcity ảnh hưởng priority.

Opportunity cost thường vô hình trong accounting report nhưng rất thật trong portfolio. Shared architect 3 tháng dành cho low-value project có thể làm high-value initiative chậm dù payroll total không đổi.

## Avoidable, unavoidable và incremental cost

Khi đánh giá option, useful question là cost nào thực sự thay đổi nếu decision thay đổi. Một sunk or unavoidable corporate overhead không nên được dùng như incremental penalty nếu nó vẫn tồn tại ở mọi option.

Incremental cost là phần thêm do option/change tạo ra. Change request “chỉ tốn 20 triệu vendor fee” có thể còn incremental test, training, support và schedule cost-of-delay. Impact analysis cần total incremental economics, không chỉ invoice trực tiếp.

## Contingency reserve và management reserve

Contingency reserve dùng cho known-unknowns: risk đã được nhận diện nhưng outcome chưa chắc. Nó thường nằm trong cost baseline tùy governance. Management reserve dùng cho unknown-unknowns hoặc work ngoài planning basis trong boundary được quản trị, và thường do management control.

Sự phân biệt quan trọng vì reserve không phải “tiền dư”. Nó biểu diễn uncertainty được chủ động price vào plan.

Reserve cần rule sử dụng. Nếu team coi contingency là budget có thể spend tự do, uncertainty buffer bị consume bởi optional scope. Nếu reserve quá khó access, nó không giúp response khi risk materialize.

## Reserve consumption phải nối với risk retirement

Dùng reserve không tự động là bad performance. Nếu identified risk materialize và contingency được dùng đúng purpose, reserve đang làm công việc của nó.

Câu hỏi quản trị là exposure còn lại so với reserve còn lại. Nếu 70% reserve đã dùng nhưng 80% major uncertainty đã retired, state có thể hợp lý. Nếu 70% reserve đã dùng khi project mới đi qua 20% uncertain work, forecast cần attention.

Reserve analysis nên theo trend của risk exposure, không chỉ balance tài khoản.

## Cost estimate cũng là distribution

Một point estimate như 500 triệu che uncertainty. Range 450–650 triệu với assumptions rõ cung cấp information tốt hơn.

Estimate confidence phụ thuộc maturity của scope, market price, exchange rate, technical uncertainty và vendor quote. Progressive elaboration thường làm range hẹp dần khi evidence tăng.

Management nên tránh ép estimate sớm thành fixed commitment mà không price risk, vì uncertainty không biến mất chỉ vì contract hoặc slide có một con số.

## Estimate range phải phản ánh source of uncertainty

Range rộng không phải luôn do team estimate kém. Early concept project có thể legitimately có range lớn vì scope và market chưa ổn định. Ngược lại range rất hẹp khi data còn yếu có thể là false precision.

Estimate nên kèm basis: quantity, rate, vendor quote, historical reference, inflation/FX assumption, productivity, exclusions và validity period. Một con số không có basis rất khó update khi world thay đổi.

## Cost aggregation và baseline

Work-package estimates được aggregate thành control-account/project budget. Nhưng aggregation không tự loại uncertainty. Correlated risk có thể làm total variance lớn.

Baseline là reference được approve để đo performance. Nếu scope change được approve, baseline có thể cần change theo governance. Baseline không phải original estimate bất biến cũng không phải rolling forecast.

Aggregation cũng cần tránh double count. Shared environment cost được allocate ở infrastructure package rồi lại cộng vào từng workstream sẽ inflate budget; common resource bị bỏ khỏi mọi package lại làm underestimate.

## Funding-limit reconciliation

Một plan có thể economically hợp lý nhưng funding cadence không match. Organization có thể chỉ cấp tối đa 300 triệu/quý trong khi procurement cần deposit 500 triệu tháng đầu.

Funding-limit reconciliation điều chỉnh timing, contract term, phasing hoặc financing plan để cash need phù hợp funding availability. Đây là connection giữa schedule và finance: dời procurement milestone có thể giải cash constraint nhưng làm critical path trễ.

PM cần surface conflict này sớm thay vì tới ngày invoice mới phát hiện “budget có nhưng cash chưa được release”.

## Payment terms và working-capital effect

Hai vendor có cùng total price nhưng payment term khác nhau: 50% upfront so với payment after acceptance. Điều này thay cash exposure, leverage và risk.

Milestone payment có thể align incentive với verified progress. Upfront payment có thể cần khi equipment custom nhưng tăng buyer exposure nếu vendor fail. Commercial decision vì vậy không chỉ so headline price.

## Inflation, escalation và FX

Long project chịu price escalation. Material, labor rate hoặc cloud/vendor price có thể tăng theo thời gian. Multi-currency contract còn có FX risk.

Một vendor quote 1 triệu USD không phải fixed cost bằng nội tệ nếu exchange rate chưa hedge/fix. PM không cần trade FX, nhưng phải biết assumption rate, exposure owner và trigger update forecast.

Delay cũng có finance effect: cùng scope nhưng mua một năm sau có thể đắt hơn vì inflation/escalation. Schedule variance vì vậy có thể biến thành cost variance ngay cả khi productivity không đổi.

## Tax, duty và regulatory cost boundary

Project estimate cần rõ giá đã gồm tax, import duty, license, insurance hay chưa. Một quote “100” từ vendor có thể không phải landed/project cost 100.

Điểm quan trọng không phải học luật thuế mà là xác định cost boundary. Missing non-work cost thường xuất hiện ở procurement-heavy project khi team chỉ estimate technical price.

## Earned Value Management như một model tích hợp

Earned Value Management (EVM / 획득가치관리) kết nối scope, schedule và cost trong predictive control. Ba quantity cơ bản là Planned Value (PV), Earned Value (EV) và Actual Cost (AC).

Nếu tới hôm nay ta dự kiến hoàn thành work trị giá 100 (PV=100), thực tế hoàn thành lượng work tương đương 80 theo baseline (EV=80), và đã chi 90 (AC=90), thì:

```text
Schedule Variance: SV = EV - PV = 80 - 100 = -20
Cost Variance:     CV = EV - AC = 80 - 90  = -10
Schedule Index:    SPI = EV / PV = 0.80
Cost Index:        CPI = EV / AC ≈ 0.89
```

Negative SV nói ta hoàn thành ít planned work hơn mức dự kiến tại thời điểm đo. CPI dưới 1 nói mỗi đơn vị chi phí tạo ít earned value hơn plan. Nhưng EVM không tự giải thích root cause và không đo customer value; nó đo performance so với baseline.

## EV không phải revenue hay business value

Tên “earned value” dễ gây hiểu nhầm. EV là budgeted value của work đã hoàn thành theo baseline, không phải revenue, profit hoặc customer benefit.

Một feature không ai dùng vẫn có EV nếu scope đã hoàn thành. Vì vậy EVM mạnh về execution control nhưng cần benefit metric để đánh giá outcome.

## EV measurement technique quyết định signal quality

EV chỉ đáng tin khi rule đo completion phù hợp. 0/100, 50/50, weighted milestone hoặc percent complete tạo behavior khác nhau.

Nếu một work package trị giá lớn được cho 90% EV dựa trên subjective progress nhưng phần acceptance khó nhất chưa xong, CPI/SPI sẽ đẹp giả. Discrete deliverable nên ưu tiên objective completion evidence khi feasible.

## BAC, ETC, EAC và VAC

Budget at Completion (BAC) là authorized baseline budget cho scope. Estimate to Complete (ETC) là forecast cost còn lại. Estimate at Completion (EAC) là total forecast cost. Variance at Completion (VAC) là difference giữa BAC và EAC.

Identity cơ bản:

```text
EAC = AC + ETC
VAC = BAC - EAC
```

Các formula khác nhau chủ yếu là cách estimate ETC dưới assumption khác nhau.

## Forecast với EAC

Nếu current cost efficiency dự kiến tiếp tục, có thể dùng:

```text
EAC = BAC / CPI
```

Nếu variance hiện tại được xem là one-off và phần còn lại theo plan, có thể dùng:

```text
EAC = AC + (BAC - EV)
```

Nếu cả cost và schedule efficiency được giả định ảnh hưởng phần còn lại, một model thường gặp dùng:

```text
EAC = AC + (BAC - EV) / (CPI × SPI)
```

Không nên học formula mà quên assumption. Chọn formula trước khi hiểu nguyên nhân variance là biến arithmetic thành ritual.

Worked examples chi tiết hơn nằm ở [Quantitative Reasoning](./15_quantitative_reasoning_worked_examples.md).

## Bottom-up ETC khi structure đã thay đổi

Formula extrapolation hữu ích khi future work giống performance pattern hiện tại. Nhưng nếu scope, vendor, team hoặc approach đã thay đổi, bottom-up ETC có thể tốt hơn.

Ví dụ CPI thấp do one-time failed migration và remaining work là routine rollout. `BAC/CPI` có thể quá pessimistic. Ngược lại nếu root cause là structural productivity problem, “remaining work theo plan” quá optimistic.

Forecast quality phụ thuộc causal model của remaining work.

## TCPI như câu hỏi về feasibility

To-Complete Performance Index (TCPI) hỏi efficiency cần đạt trên work còn lại để chạm một target budget.

Nếu performance lịch sử CPI khoảng 0.8 nhưng TCPI cần 1.25 để đạt BAC, target có thể không realistic nếu không có major change. TCPI giúp chuyển conversation từ “hãy cố lên” sang “required improvement có feasible không?”.

TCPI cao không phải mệnh lệnh làm việc nhanh hơn. Nó là signal để reassess target, scope, process hoặc forecast.

## SPI và SV có giới hạn gần cuối project

Khi project gần completion, EV và PV đều tiến về BAC nên SPI có xu hướng quay về 1 và SV về 0, kể cả project đã finish muộn. Đây là giới hạn của schedule interpretation bằng EVM monetary dimension.

Vì vậy actual/forecast finish date, milestone logic và critical path vẫn cần được quản lý bằng schedule model. EVM không thay network scheduling.

## EVM failure modes

EVM chỉ tốt khi scope/baseline và completion measurement đáng tin. Nếu team declare work 90% complete quá dễ, EV bị inflated. Nếu baseline đã outdated nhưng không rebaseline sau approved major change, variance mất meaning.

EVM cũng ít phù hợp khi scope adaptive liên tục và value không map ổn định vào baseline work package. Có thể vẫn dùng financial control khác mà không ép framework không phù hợp.

Một failure khác là “variance hunting”: management hỏi vì sao CPI 0.97 thay vì tập trung material driver. Threshold nên phản ánh decision significance, không biến mọi decimal thành incident.

## Variance attribution: price, quantity, productivity, mix và timing

Cost variance tổng không đủ để action. Cần biết driver. Vendor rate tăng là price effect; rework tăng hours là quantity/productivity effect; senior/junior ratio khác plan là mix effect; invoice timing lệch là timing effect.

Hai project đều over 10% nhưng response khác nhau. Price escalation cần commercial/forecast action; productivity issue cần process/technical action; timing effect có thể không thay EAC.

Variance analysis tốt phân biệt symptom tài chính với causal mechanism.

## Fixed budget không có nghĩa fixed scope

Nhiều project có budget cap nhưng scope có thể prioritize. Adaptive product delivery thường giữ team/cost tương đối stable và optimize scope theo value.

Ngược lại fixed scope + fixed budget + fixed date trong high uncertainty environment thường đẩy risk sang quality, hidden overtime hoặc contract dispute. Triple constraint không thể bị “ra lệnh” để uncertainty biến mất.

## Burn rate và runway

Burn rate là tốc độ tiêu cash/budget trong period. Runway ước lượng thời gian còn lại nếu burn hiện tại tiếp tục.

Startup/product context dùng khái niệm này rõ, nhưng project cũng có thể dùng để phát hiện funding timing risk. Burn rate cao không nhất thiết xấu nếu project đang ở phase procurement lớn; cần so với plan và output.

Runway dựa trên burn hiện tại chỉ meaningful nếu cost profile tương đối stable. Construction/procurement project có lumpy payment nên linear extrapolation dễ sai.

## Sunk cost và continuation decision

Sunk cost là chi phí đã xảy ra và không thể thu hồi. Quyết định tiếp tục project nên dựa trên future cost, future benefit, risk và alternatives, không dựa trên “đã đầu tư quá nhiều để dừng”.

Ví dụ đã chi 70% budget nhưng evidence mới cho thấy product không có market fit. Nếu remaining 30% không tạo expected value, tiếp tục chỉ để “không phí 70%” làm tổn thất lớn hơn.

Governance cần exit criteria đủ rõ để sunk-cost psychology không khóa organization vào project mất value.

## Cancellation cost và switching cost vẫn là future cost

Tránh sunk-cost fallacy không có nghĩa dừng là miễn phí. Termination fee, data migration, decommission, employee transition hoặc regulatory obligation là future cost và phải được tính vào stop option.

Decision đúng so future states: continue, pause, pivot, phase hoặc terminate. “Đã chi bao nhiêu” không quyết định; “mỗi option từ hôm nay tạo cost/value/risk gì” mới quyết định.

## Marginal analysis

Khi project gần hoàn thành, câu hỏi có thể là thêm 10% cost có tạo enough incremental benefit/risk reduction không. Đây là marginal reasoning.

Không nên dùng average ROI của toàn project để quyết một optional enhancement cuối kỳ. Hãy so incremental cost với incremental value và effect lên deadline/risk.

## ROI, payback và NPV

Return on Investment (ROI) so return với investment theo definition tổ chức. Payback period hỏi mất bao lâu để recover investment. Net Present Value (NPV) discount future cash flow về present value.

Mỗi metric trả lời câu khác. Payback ưu tiên liquidity/tốc độ thu hồi nhưng bỏ qua nhiều benefit sau payback. ROI có thể che timing. NPV phản ánh time value of money nhưng phụ thuộc discount rate và cash-flow assumptions.

Project selection không nên dùng một metric như truth tuyệt đối.

## Benefit-cost ratio và break-even intuition

Benefit-cost ratio so present/expected benefit với cost theo convention tổ chức. Break-even hỏi khi nào cumulative benefit bù cumulative cost hoặc mức volume nào làm economics đổi dấu.

Hai metric này hữu ích để reason nhưng vẫn phụ thuộc assumptions. A project có BCR tốt ở adoption 80% có thể không viable ở adoption 30%.

Sensitivity analysis nên tìm driver làm decision đổi, không chỉ produce one base-case number.

## NPV và time value intuition

Tiền nhận hôm nay thường có giá trị hơn cùng số tiền nhận sau nhiều năm vì opportunity cost và risk. NPV có dạng khái quát:

```text
NPV = Σ CF_t / (1 + r)^t - Initial Investment
```

Trong đó `r` là discount rate và `CF_t` là cash flow theo period.

Thư viện này không biến PMP thành môn corporate finance; mental model cần nhớ là investment decision phải so benefit theo time/risk, không chỉ tổng nominal money.

Delay có thể giảm NPV ngay cả khi total nominal benefit không đổi vì cash inflow đến muộn hơn và cost kéo dài.

## Financial benefit và non-financial benefit

Compliance, safety, capability, reputation hoặc strategic option có thể có benefit khó quy tiền chính xác. Không nên ép mọi value thành dollar nếu model quá giả tạo.

Business case có thể kết hợp financial metric với mandatory constraint và strategic rationale. “NPV thấp” không tự động loại project pháp lý bắt buộc; decision context khác nhau.

Non-financial benefit vẫn cần evidence. “Tăng uy tín” quá mơ hồ; có thể dùng proxy như audit finding giảm, service availability, employee adoption hoặc risk exposure reduction.

## Cost of delay

Cost of delay cố lượng hóa value mất khi delivery trễ. Một feature seasonal hoặc regulatory deadline có cost of delay cao; enhancement nội bộ có thể thấp hơn.

Cost of delay giúp priority khi nhiều item cạnh tranh resource. Nó cũng cho thấy schedule và finance nối nhau: delay là economic effect chứ không chỉ màu đỏ trên Gantt.

Cost of delay có thể nonlinear. Miss Black Friday một ngày có thể mất phần lớn seasonal value; delay một ngày ở internal refactor có thể gần zero. Vì vậy “cost per day” constant chỉ là approximation trong một số context.

## Cost of quality nối quality với finance

Prevention/appraisal cost tăng có thể giảm internal/external failure cost. Cắt testing để “tiết kiệm budget” có thể làm total lifecycle cost tăng nếu defect escape production.

Financial reasoning tốt nhìn total cost of outcome, không chỉ project spend ngắn hạn. Tuy vậy lifecycle cost thuộc boundary rộng hơn project baseline và cần explicit business-case assumption.

## Value measurement vượt ra ngoài budget

Dự án có thể under budget nhưng không tạo business outcome. Vì vậy metric nên nối tới benefit: adoption, revenue uplift, risk reduction, time saved, compliance achieved, customer outcome. Một benefit owner có thể tiếp tục theo dõi sau project closure khi benefit realization xảy ra muộn.

Value nên được nhìn theo numerator lẫn denominator. Tăng revenue 5% nhưng tăng support cost 20% có thể không tạo net benefit mong muốn.

## Benefit attribution và counterfactual

Nếu revenue tăng sau go-live, không tự động chứng minh project tạo toàn bộ increase. Market growth, promotion hoặc seasonality có thể cùng tác động.

Benefit plan nên có baseline và, khi khả thi, counterfactual/comparison. Project management không cần causal-inference textbook, nhưng cần tránh claim benefit chỉ vì metric thay cùng thời điểm.

## Living business case và continuation threshold

Business case là hypothesis về future value dựa trên assumptions. Khi cost, timing, adoption, regulation hoặc strategic priority đổi đủ lớn, hypothesis cần được cập nhật.

Governance nên có threshold để reassess: forecast cost vượt X, benefit giảm Y, deadline miss làm value window mất, hoặc mandatory risk xuất hiện. Không cần reopen business case vì every small variance, nhưng cũng không nên chờ closure mới phát hiện investment đã mất logic.

## Forecast phải được update khi assumption đổi

Financial forecast không nên chỉ update vì actual cost. FX, vendor price, schedule delay, demand, adoption hoặc regulation có thể đổi expected value và future cost.

Business case sống cần phản ánh information mới đủ material. Nếu expected benefit giảm mạnh, PM cần surface tới governance thay vì chỉ cố “giữ budget”.

Forecast change nên preserve history. Original forecast, revised forecast và reason giúp organization học calibration; overwrite số cũ làm mất evidence.

## Ví dụ reasoning

Project có BAC 1 tỷ, CPI 0.8 sau 40% work. Nếu inefficiency có systemic cause chưa sửa, dùng `BAC/CPI` tạo forecast khoảng 1.25 tỷ hợp lý hơn giả định phần còn lại tự quay về plan. Nếu root cause là one-time migration incident đã giải quyết, formula one-off có thể phù hợp hơn.

Một project khác có NPV dương nhưng deadline market bị delay một năm, khiến benefit tới muộn và competitor chiếm share. Business case cần recompute thay vì giữ quyết định dựa trên NPV cũ.

Một vendor contract 600 triệu đã signed nhưng project mới thanh toán 150 triệu. Dashboard “actual spend 150/1000” có thể khiến management nghĩ 850 triệu còn flexible; thực tế committed spend đã 600 và cancellation fee có thể làm phần lớn obligation khó tránh. Decision cần nhìn commitment, không chỉ cash paid.

## Failure modes

Budget tunnel vision xảy ra khi project tối ưu under-budget nhưng mất outcome. Cash/expense confusion xảy ra khi payment timing bị đọc như performance. Commitment blindness bỏ qua obligation chưa invoiced. Reserve raiding dùng contingency cho optional scope. EVM theater xuất hiện khi EV rule chủ quan làm metric đẹp. Sunk-cost lock-in giữ project chỉ vì đã chi nhiều. Forecast overwrite xóa lịch sử calibration. FX/inflation blindness giả định nominal quote bất biến qua thời gian.

Financial maturity là khả năng nối accounting state, project-control state và value hypothesis thành một decision model nhất quán.

## Mental model

> Cost control hỏi resource đã được cam kết, tiêu và forecast như thế nào; funding hỏi cash cần khi nào; value management hỏi từ hôm nay investment còn đáng tiếp tục hay không. Reserve làm uncertainty visible, còn mọi forecast chỉ có ý nghĩa khi basis, commitment và assumption phía sau được nói rõ.

Tiếp theo: [Quality, resources và procurement](./07_quality_resources_and_procurement.md).
