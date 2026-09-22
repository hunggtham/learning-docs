# 05 — Schedule, estimation, dependency và flow

## Schedule là model của dependency và uncertainty

Lịch trình (schedule / 일정) không phải lời hứa rằng tương lai sẽ diễn ra đúng một tập ngày. Nó là model cho sequence, dependency, resource, constraint và estimate hiện tại. Giá trị của schedule nằm ở việc cho thấy điều gì quyết định finish date và signal nào làm forecast thay đổi.

Nếu một Gantt chart có rất nhiều ngày nhưng không phản ánh dependency hoặc uncertainty, nó tạo false precision.

Schedule tốt phải đủ detailed để coordination nhưng không detailed đến mức maintenance cost lớn hơn information value. Planning horizon càng xa thì detail thường càng coarse vì uncertainty lớn hơn.

Một schedule trưởng thành cần trả lời được ba lớp câu hỏi: logic nào buộc work phải đi theo sequence này, resource/calendar nào giới hạn execution, và uncertainty nào làm finish distribution thay đổi. Chỉ có ngày bắt đầu/kết thúc mà thiếu ba lớp đó thì schedule chưa phải decision model.

## Milestone, activity và deliverable

Deliverable là output có ý nghĩa. Activity là work để tạo output. Milestone là điểm sự kiện quan trọng thường có zero duration trong schedule model.

Nhầm ba lớp làm status méo. “Development 80%” là activity progress; “API contract accepted” là milestone; “integrated service” là deliverable. Milestone thường hữu ích hơn percent-complete khi cần decision hoặc handoff.

Milestone tốt đại diện một state transition có evidence, không chỉ một date đẹp. “Security approval obtained” mạnh hơn “Security review milestone” nếu người đọc biết condition nào làm milestone complete.

## Từ scope tới activity

Sau khi scope được decompose, team xác định activity cần thực hiện, relationship giữa chúng và resource/effort. Dependency có thể bắt buộc về logic, đến từ contract/regulation, hoặc chỉ do cách tổ chức chọn.

Finish-to-start là kiểu phổ biến: B chỉ bắt đầu sau A. Nhưng thực tế còn start-to-start, finish-to-finish và lag/lead. Điều quan trọng không phải nhớ tên mà hiểu constraint thật: “cái gì phải xảy ra trước khi cái khác có thể tiến?”.

Một dependency nên bị challenge nếu chỉ tồn tại vì habit. Nếu testing có thể bắt sớm hơn bằng partial increment, dependency “dev hoàn tất toàn bộ rồi mới test” là organizational choice chứ không phải law tự nhiên.

## Lead và lag: dùng để mô hình reality, không để che thiếu activity

Lag biểu diễn waiting time giữa hai state; lead cho phép overlap. Ví dụ concrete curing cần 3 ngày chờ trước activity sau; đó là lag có physical meaning. Nhưng nếu “đợi phê duyệt 5 ngày” thực chất là một process có owner và work, biến nó thành lag có thể che accountability.

Một schedule khỏe ưu tiên model explicit activity khi có work/control cần quản lý; lag phù hợp hơn với waiting time thật sự. Lead cũng không nên dùng để giả vờ parallelism khi downstream chưa có stable information để bắt đầu.

## Mandatory, discretionary và external dependency

Mandatory dependency đến từ physical/technical logic. Discretionary dependency đến từ preferred sequence hoặc best practice. External dependency nằm ngoài direct control, như regulator approval hoặc vendor shipment.

Classification quan trọng vì recovery option khác nhau. Mandatory dependency khó loại bỏ; discretionary có thể redesign; external cần lead time, monitoring và escalation interface.

External dependency còn cần confidence và response window. “Regulator phản hồi trong tháng 11” khác “regulator có SLA 10 business days”. Schedule cần phân biệt fact, assumption và target.

## Network diagram như causal graph

Schedule network không chỉ là hình để tính CPM. Nó là causal graph của finish-date logic. Khi một activity delay, graph cho biết impact truyền qua đâu.

Nếu team chỉ giữ list task và due date mà không có dependency model, họ khó biết task nào thực sự critical và task nào có slack.

Graph còn giúp phát hiện path convergence: nhiều path độc lập cùng đổ vào một milestone. Dù từng path có xác suất hoàn thành đúng hạn cao, milestone tổng có thể rủi ro hơn vì chỉ cần một path muộn là integration muộn.

## Critical path

Critical Path Method (CPM / 주공정법) tìm chuỗi activity có total duration dài nhất qua network và quyết định thời gian project tối thiểu theo model hiện tại. Activity trên critical path có zero hoặc rất ít total float; delay ở đó có khả năng đẩy finish date nếu không có recovery elsewhere.

Ví dụ có hai đường: A(3 ngày) → B(5) → D(2) = 10 ngày, và A(3) → C(2) → D(2) = 7 ngày. Đường A-B-D critical. C có khoảng slack 3 ngày so với network đơn giản này. Việc tăng tốc C không làm project kết thúc sớm hơn; muốn giảm duration cần tác động critical path.

Critical path có thể thay đổi khi estimate hoặc dependency đổi. Vì vậy nó là dynamic property của schedule model.

## Near-critical path và criticality switching

Path có float rất nhỏ có thể trở thành critical sau một delay nhỏ. Trong project nhiều uncertainty, chỉ theo dõi một critical path duy nhất tạo false security.

Near-critical path cần attention theo mức float và uncertainty. Một path có 2 ngày float nhưng estimate rất volatile có thể đáng quan tâm hơn critical path ổn định. Khi simulation được dùng, criticality index có thể cho intuition activity/path xuất hiện trên critical path trong bao nhiêu iteration; mục tiêu không phải học thêm metric mà là hiểu criticality có thể thay đổi theo uncertainty.

## Float và việc hiểu đúng “không critical”

Total float là lượng delay một activity có thể chịu trước khi project finish bị ảnh hưởng theo current network. Free float là lượng delay trước khi successor sớm nhất bị ảnh hưởng.

Activity không critical không có nghĩa không quan trọng. Float có thể bị consume dần và path gần critical có thể trở thành critical sau vài change. PM nên theo dõi near-critical path ở project có uncertainty cao.

Float cũng không phải “budget của activity owner”. Nếu nhiều upstream activity cùng tiêu cùng downstream slack, local team không thể giả định toàn bộ float thuộc riêng mình.

## Negative float

Negative float xuất hiện khi imposed date sớm hơn finish date mà network hiện tại có thể đạt. Nó không phải phép thuật để schedule “ép” nhanh hơn; nó là signal rằng constraint và logic đang conflict.

Nếu network forecast 30/11 nhưng contractual milestone là 20/11, negative float 10 ngày cho biết cần thay scope, sequence, resource, constraint hoặc commitment. Chỉ đổi ngày trên Gantt không giải inconsistency.

Negative float nên trigger management conversation về feasibility chứ không trở thành lý do tự động ép overtime.

## Forward pass và backward pass

Forward pass tính earliest start/finish từ đầu network. Backward pass tính latest start/finish từ deadline hoặc finish date. Difference giữa latest và earliest tạo float.

Cơ chế quan trọng hơn arithmetic: forward pass hỏi “sớm nhất có thể xong khi dependency giữ nguyên là khi nào?”, backward pass hỏi “muộn nhất có thể làm mà chưa đẩy finish là khi nào?”. Worked example đầy đủ nằm ở [Quantitative Reasoning](./15_quantitative_reasoning_worked_examples.md).

## Hard constraint và soft constraint

Không phải mọi constraint date đều ngang nhau. “Must finish on” do regulation có thể là hard boundary; “prefer finish before” để align internal campaign là soft target.

Hard constraint nên được dùng cẩn thận trong schedule tool vì nó có thể che logic nếu planner ép date mà không giải dependency. Soft constraint nên giữ visibility của forecast để management nhìn gap giữa target và khả năng hiện tại.

Constraint source luôn cần traceable: contract, law, sponsor target, market window hay internal preference.

## Calendar là một phần của logic

Duration phụ thuộc calendar. 5 working days không đồng nghĩa 5 calendar days. Holiday, shift, regional calendar, vendor working hours và specialist availability đều làm earliest finish thay đổi.

Một global project có thể mất một ngày ở mỗi handoff vì timezone/cutoff dù effort gần như không đổi. Nếu schedule tool dùng default calendar cho mọi activity, forecast có thể optimistic giả.

Resource calendar đặc biệt quan trọng với reviewer hoặc expert hiếm. Activity duration 2 giờ nhưng reviewer chỉ available thứ Sáu có thể tạo lead time gần một tuần.

## Estimate là distribution, không phải số thật tuyệt đối

Estimate luôn dựa trên information chưa hoàn chỉnh. Một estimate “10 ngày” nên được hiểu như một forecast với confidence, assumptions và range. Three-point estimation dùng optimistic, most likely và pessimistic để buộc ta nghĩ về uncertainty.

PERT thường dùng expected duration:

```text
E = (O + 4M + P) / 6
```

Nếu O=4, M=7, P=16 thì E=(4+28+16)/6=8 ngày. Formula không biến uncertainty thành certainty; nó chỉ tạo một summary có trọng số. Nếu input là guess không có reasoning, output vẫn là guess có thêm decimal.

Analogous estimation nhanh khi có historical comparable. Parametric estimation dùng rate như “giờ mỗi migration record”. Bottom-up estimate chi tiết hơn nhưng tốn effort và vẫn bị aggregation error.

## Estimate effort và duration khác nhau

Effort là lượng work, ví dụ 40 person-hours. Duration là calendar time để hoàn tất, có thể dài hơn hoặc ngắn hơn tùy resource, parallelism, calendar và dependency.

40 giờ effort không tự động là 5 ngày duration. Nếu chuyên gia chỉ available 50%, hoặc work phải chờ review, duration tăng. Đây là lỗi phổ biến khi convert estimate cơ học.

Parallelism cũng có giới hạn. Hai người không luôn giảm duration một nửa vì communication, indivisible work hoặc shared environment.

## Estimate uncertainty có nhiều nguồn

Uncertainty không chỉ đến từ “không biết effort”. Nó có thể đến từ requirement ambiguity, technical novelty, external approval, resource availability, queue time, defect/rework và event risk.

Hai activity cùng point estimate 5 ngày nhưng uncertainty profile khác nhau. Một activity routine có range 4–6; một integration mới có range 2–15. Schedule nên attention vào variance/tail, không chỉ mean.

## Historical data và reference class forecasting

Estimate nội bộ dễ bị optimism bias. Reference class forecasting nhìn các project/work item tương tự trong lịch sử để tạo base rate.

Nếu 20 migration tương tự có median 8 ngày và P80 13 ngày, forecast nên bắt đầu từ evidence đó rồi adjust theo difference, thay vì hỏi owner “bạn nghĩ mấy ngày?”. Historical data không hoàn hảo nhưng giúp anchor vào reality.

Reference class cần đủ tương đồng. Dùng history của feature nhỏ để forecast regulatory migration lớn có thể tạo precision giả. Base rate là starting point, không phải replacement cho context.

## Confidence và probabilistic forecast

Một deterministic date dễ bị hiểu thành guarantee. Khi uncertainty material, forecast có thể dùng confidence như P50 hoặc P80.

P80 date nghĩa theo model và assumption hiện tại có khoảng 80% simulated outcome hoàn tất trước hoặc tại date đó, không phải “80% project đã xong”. Confidence phải đi kèm model caveat.

Monte Carlo schedule simulation có thể aggregate duration distribution và dependency để nhìn finish-date distribution. PMP learner không cần code simulation để hiểu mental model: output nên là range/probability, không phải một ngày thần kỳ.

## Path convergence và merge bias

Khi nhiều parallel path hội tụ, milestone chỉ hoàn thành khi tất cả input sẵn sàng. Nếu mỗi path “thường đúng hạn”, integration milestone vẫn có tail risk cao hơn từng path riêng.

Đây là merge bias intuition: uncertainty không average đơn giản ở điểm hội tụ; late tail của bất kỳ path nào có thể kéo milestone. Vì vậy integration/test milestone thường cần attention đặc biệt, nhất là khi nhiều vendor/workstream hội tụ gần deadline.

Một schedule quá optimistic thường xuất hiện khi planner cộng average duration nhưng bỏ correlation và convergence.

## Correlation trong schedule risk

Activity không luôn độc lập. Nhiều task cùng phụ thuộc một vendor, một environment hoặc một expert. Nếu shared dependency chậm, nhiều duration cùng tăng.

Simulation giả độc lập có thể đánh giá thấp tail. Mapping common-cause dependency giúp forecast thực tế hơn và cũng gợi ý response: thêm buffer vào từng task không bằng giảm shared failure domain.

## Resource constraint và critical chain intuition

Network logic không phải constraint duy nhất. Hai activity có thể độc lập nhưng dùng cùng một chuyên gia. Nếu resource chỉ làm được một việc tại một thời điểm, schedule phải phản ánh resource leveling/smoothing. Đây là lý do critical path trên logic graph có thể chưa đủ để dự đoán thực tế.

Resource leveling có thể đổi critical path và finish date. Resource smoothing cố dùng float để cân resource mà không đổi critical path/finish nếu có thể.

Critical chain intuition nhấn mạnh resource constraint và buffer. Điểm đáng hiểu là bảo vệ flow ở system level thay vì nhét safety margin bí mật vào từng task.

## Resource contention và multitasking cost

Một specialist chạy ba project song song không tạo 300% capacity. Context switching, queue và priority conflict làm elapsed duration tăng.

Schedule nên phản ánh allocation thực tế thay vì giả mỗi project có full resource. Nếu portfolio không resolve contention, từng PM có thể có schedule “feasible” riêng nhưng toàn organization thì không feasible.

Resource contention là điểm nối trực tiếp giữa project schedule và portfolio governance.

## Student syndrome và Parkinson-like behavior

Khi mỗi task có buffer riêng nhưng deadline được coi như target, work có xu hướng bắt đầu muộn hoặc expand tới available time. Buffer bị tiêu thụ mà không bảo vệ project finish.

System buffer rõ và early-finish handoff có thể tạo visibility tốt hơn hidden padding, dù implementation cụ thể tùy methodology.

## Crashing và fast tracking

Crashing thêm resource hoặc chi phí để giảm duration của critical activities khi có thể. Fast tracking chạy overlap các việc vốn sequence để rút thời gian nhưng tăng coordination/rework risk. Không phải activity nào cũng compress được; chín phụ nữ không thể tạo một em bé trong một tháng là intuition kinh điển cho non-parallelizable work.

Crashing chỉ có value khi activity nằm trên critical path hoặc path có khả năng trở thành critical. Thêm người vào noncritical task không rút project finish.

Fast tracking hiệu quả khi downstream có thể bắt với partial stable information. Nếu upstream uncertainty cao, overlap có thể tạo rework lớn hơn time saved.

## Compression có diminishing return

Khi schedule bị compress dần, option rẻ thường được dùng trước. Sau đó mỗi ngày rút thêm có thể đắt hơn và riskier hơn.

Crashing một activity có thể làm path khác trở thành critical; fast tracking có thể tăng defect/rework. Vì vậy schedule compression cần re-run network/risk reasoning sau mỗi significant change, không giả benefit tuyến tính.

## Deadline, target date và constraint khác nhau

Một date có thể là aspirational target, contractual milestone, regulatory deadline hoặc technical dependency. Chúng không có cùng flexibility.

Nếu team đối xử target nội bộ như legal deadline, họ có thể nhận risk không cần thiết. Ngược lại, coi regulatory deadline như estimate có thể gây compliance failure. Schedule reasoning phải hiểu source của constraint.

## External window và cadence mismatch

Một project có thể internal cadence nhanh nhưng phụ thuộc window hiếm: regulator test mỗi tháng, vendor cutover mỗi quý, data center maintenance mỗi cuối tuần.

Nếu miss một 2-hour window, effective delay có thể là cả tháng. Schedule nên model calendar/window như real constraint, không chỉ activity duration.

Đây là lý do “task chỉ trễ một ngày” đôi khi gây impact rất lớn khi nó bỏ lỡ fixed integration window.

## Schedule reserve và buffer

Uncertainty nên được visible ở system level. Buffer có thể bảo vệ milestone, integration window hoặc release.

Buffer không phải lý do để slack work vô hạn. Nó là risk capacity có trigger và owner. Khi buffer burn nhanh hơn progress, đó là early warning signal.

Buffer consumption nên được đọc cùng uncertainty retired. Dùng 50% buffer nhưng đã retire 90% major risk khác với dùng 50% buffer khi mới hoàn thành 20% uncertain work.

## Adaptive flow: velocity không phải productivity tuyệt đối

Trong adaptive delivery, planning thường dùng backlog, story points, throughput, cycle time và velocity. Story point là relative sizing trong một team/context; không nên dùng để so hiệu suất giữa team hoặc ép “tăng productivity”. Khi biến point thành KPI thưởng/phạt, Goodhart's Law khiến metric bị game.

Flow metrics giúp nhìn system: work in progress cao thường kéo cycle time dài. Little's Law trong steady-state cho intuition:

```text
WIP ≈ Throughput × Cycle Time
```

Nếu trung bình 20 item đang mở và hoàn thành 5 item/tuần, cycle time trung bình xấp xỉ 4 tuần. Giảm WIP có thể cải thiện feedback nhanh hơn mà không cần “làm nhanh hơn” từng người.

## Little's Law assumptions

Little's Law là relationship dài hạn trong stable flow, không phải magic formula cho mọi snapshot. Arrival/completion system cần đủ ổn định trong period đo và unit phải consistent.

Nếu scope inflow tăng đột biến hoặc backlog không bounded, dùng formula từ một tuần dữ liệu có thể gây kết luận sai. Mental model là WIP, throughput và cycle time ràng buộc nhau trong flow system.

## Queueing và utilization

Khi resource utilization tiến gần 100%, queue thường tăng mạnh vì không còn slack hấp thụ variation. Đây là lý do “mọi người phải luôn bận” có thể làm lead time tệ hơn.

Một reviewer có 100% calendar booked tạo queue cho mọi approval. System cần capacity margin ở bottleneck để flow ổn định.

Queue time thường lớn hơn touch time. Một change request có 2 giờ analysis nhưng chờ 8 ngày approval; tối ưu analyst 10% không cải thiện lead time đáng kể.

## Bottleneck và Theory of Constraints intuition

Throughput toàn system bị giới hạn bởi constraint/bottleneck. Tối ưu non-bottleneck có thể chỉ tạo inventory trước bottleneck.

Nếu QA là bottleneck, tăng coding throughput có thể làm WIP và cycle time tăng. Cần exploit/elevate bottleneck hoặc giảm demand trước nó.

Bottleneck có thể di chuyển sau khi được cải thiện. Vì vậy optimization là loop, không phải one-time fix.

## Schedule health: logic trước màu status

Một schedule “green” có thể unhealthy nếu thiếu predecessor/successor, dùng quá nhiều hard constraint, có activity dài hàng tháng không milestone, hoặc không phản ánh resource calendar.

Health audit nên hỏi: work có logic link đủ không, constraint có source rõ không, negative float có được hiểu không, near-critical path nào tồn tại, external window nào quyết định, estimate nào stale, resource nào overallocated và actual progress có evidence không.

Một Gantt chart đẹp không chứng minh schedule model tốt.

## Open ends và dangling activities

Activity không có predecessor hoặc successor ngoài start/finish logic có thể là intentional, nhưng cũng có thể là broken network. Nếu một task có due date nhưng không link tới project finish, delay của nó không propagate trong model.

Schedule audit cần phân biệt genuine independent work với missing dependency. Broken logic tạo false float và false critical path.

## Progress measurement và remaining duration

Percent complete không tự động suy ra remaining duration. Một task “90% done” có thể còn phần integration khó nhất.

Forecast nên update remaining duration dựa trên evidence, không tính cơ học `original duration × (1 - %complete)`. Khi knowledge tăng, remaining estimate có thể tăng dù percent complete cao.

## Schedule variance và forecast

Một deviation không tự nói nguyên nhân. PM cần hỏi: đây là random variation hay systematic problem, task có critical không, downstream dependency nào bị tác động, recovery option nào tồn tại, và uncertainty mới làm forecast đổi bao nhiêu.

Schedule report tốt nên update forecast, không chỉ báo variance quá khứ. Stakeholder cần biết “nếu current trend tiếp tục thì sao?”.

## Progress measurement pitfalls

Percent complete dễ subjective. “90% done” có thể tồn tại nhiều tuần. Deliverable-based milestone hoặc objective acceptance evidence thường đáng tin hơn effort-consumed percentage.

Level of effort work như management/support không nên tạo earned progress giống discrete deliverable nếu không có logic phù hợp.

## Ví dụ reasoning

Một project có task coding trễ 3 ngày nhưng activity có float 7 ngày. PM không nên ngay lập tức crash. Trước hết xem float, near-critical path và downstream resource. Nếu testing path khác đã critical, thêm resource vào coding có thể không thay finish date.

Một adaptive team có throughput ổn 8 item/tuần nhưng cycle time tăng từ 5 lên 12 ngày. Nếu WIP tăng mạnh, issue có thể là quá nhiều work started. Action hợp lý là giảm WIP và inspect queue trước khi kết luận team “làm chậm”.

Một project khác có ba parallel workstream cùng cần security approval trước go-live. Mỗi workstream riêng lẻ có P80 đúng hạn, nhưng tất cả hội tụ vào một approval window duy nhất. PM cần nhìn convergence/common-cause reviewer capacity thay vì cộng confidence từng path như độc lập.

## Failure modes

Date-driven scheduling xảy ra khi planner đặt ngày trước rồi ép logic theo. Constraint masking xảy ra khi hard constraint che infeasible network. Resource fantasy xảy ra khi cùng specialist được booking full-time ở nhiều activity. Merge blindness bỏ qua tail ở convergence point. Open-end network tạo false float. Percent-complete theater báo tiến độ mà không update remaining duration.

Schedule management trưởng thành không cố làm mọi activity “đúng ngày”; nó giữ model causal đủ thật để forecast và trade-off còn đáng tin.

## Mental model

> Schedule là causal model của dependency, resource, calendar, queue và uncertainty. Quản lý schedule tốt là biết path/window/resource nào thật sự quyết định outcome, nhận ra khi constraint làm model infeasible, và cập nhật forecast trước khi variance quá khứ biến thành surprise tương lai.

Tiếp theo: [Finance, cost, reserves và value measurement](./06_finance_cost_and_value_measurement.md).
