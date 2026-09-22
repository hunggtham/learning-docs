# 01 — Vòng đời, delivery approach và tailoring

## Không có một process đúng cho mọi dự án

Một nhà máy, một migration database và một ứng dụng thử nghiệm thị trường đều là project, nhưng cost of change và mức bất định khác nhau. Vì vậy việc áp cùng một quy trình cho mọi dự án là lỗi thiết kế. Tailoring (điều chỉnh phương pháp / 테일러링) là quá trình chọn và điều chỉnh approach, practice, artifact, governance và cadence theo context thực tế.

Câu hỏi đầu tiên không nên là “Waterfall hay Agile?”. Câu hỏi tốt hơn là: ta biết rõ problem và solution đến mức nào, feedback có thể nhận sớm đến đâu, cost of change tăng ra sao theo thời gian, regulatory evidence cần mức nào, dependency vật lý/kỹ thuật chặt đến đâu, và stakeholder chấp nhận incremental delivery đến mức nào.

Một delivery approach thực chất là cách project phân phối ba thứ theo thời gian: **commitment**, **feedback** và **control**. Predictive đặt nhiều commitment sớm hơn để tăng coordination; adaptive trì hoãn một số commitment để giữ option và học; hybrid đặt commitment ở boundary cần ổn định nhưng giữ feedback nhanh ở vùng còn bất định.

## Project lifecycle và development lifecycle

Vòng đời dự án (project life cycle / 프로젝트 생애주기) mô tả project từ khởi đầu đến kết thúc. Development lifecycle mô tả cách sản phẩm hoặc deliverable được tạo ra. Hai thứ có thể khác nhau. Một project có initiation, planning, delivery, transition, closure; bên trong delivery có thể dùng iterative software development.

Nhầm hai khái niệm dẫn đến tranh luận vô ích, ví dụ “Agile không cần planning”. Agile vẫn có planning, nhưng planning được phân phối qua nhiều horizon và cập nhật theo feedback thay vì cố định chi tiết xa trong tương lai.

Một cách nhìn tốt hơn là xem lifecycle như chuỗi thay đổi trạng thái của investment. Lúc đầu tổ chức mới có một hypothesis rằng đầu tư này đáng làm. Sau đó project dần tạo evidence, commit nguồn lực, tạo deliverable, chuyển capability sang operation và cuối cùng đóng temporary organization. Mỗi phase tồn tại vì loại decision cần đưa ra thay đổi theo thời gian.

Lifecycle tốt không chỉ hỏi “đã làm xong phase chưa?” mà hỏi “evidence hiện tại có đủ để chuyển sang mức commitment tiếp theo không?”. Nếu gate chỉ kiểm tra đủ template mà không thay đổi decision quyền đầu tư, nó trở thành ceremony.

## Lifecycle như một chuỗi commitment tăng dần

Mỗi decision lớn làm giảm option. Ký hợp đồng dài hạn, chốt kiến trúc, đặt thiết bị, migrate production data hoặc public launch đều là những commitment ngày càng khó đảo ngược.

Vì vậy lifecycle nên đồng bộ **evidence strength** với **commitment irreversibility**. Decision càng khó đảo ngược thì càng cần evidence mạnh, risk review rõ và authority phù hợp.

Một project yếu thường làm ngược: commitment lớn được đưa ra khi evidence còn yếu, rồi sau đó governance chỉ cố bảo vệ decision cũ. Khi đó lifecycle không còn là learning system mà trở thành cơ chế rationalize sunk cost.

Mental model:

```text
uncertainty cao + commitment dễ đảo ngược
                ↓ learning
uncertainty giảm + evidence tăng
                ↓
commitment lớn hơn / khó đảo ngược hơn
```

## Năm chiều uncertainty cần tách riêng

Không nên gộp mọi bất định thành một từ “uncertain”. Requirement uncertainty là mức chưa rõ về nhu cầu. Solution uncertainty là mức chưa rõ về cách xây. Execution uncertainty là khả năng kế hoạch bị lệch do dependency, năng suất hoặc resource. External uncertainty đến từ regulation, market, vendor hay technology. Adoption uncertainty là mức chưa rõ liệu output có thực sự được sử dụng để tạo outcome hay không.

Một dự án có thể requirement ổn định nhưng solution uncertainty cao, ví dụ migration một hệ thống legacy có scope rõ nhưng chưa biết dữ liệu bẩn đến mức nào. Dự án khác có solution technology quen thuộc nhưng requirement uncertainty cao vì customer chưa biết họ muốn gì. Hai trường hợp này cần feedback loop khác nhau.

Đây là lý do chỉ hỏi “scope có rõ không?” là chưa đủ để chọn approach.

## Uncertainty profile phải nối với loại feedback

Không phải feedback nào cũng giảm cùng loại uncertainty. User interview có thể giảm requirement uncertainty nhưng không chứng minh performance ở production load. Technical spike có thể giảm solution uncertainty nhưng không chứng minh adoption. Contract clarification giảm external/commercial uncertainty nhưng không giúp customer usability.

Tailoring tốt vì vậy cần hỏi **ta đang cố học điều gì**, rồi chọn feedback mechanism tương ứng. Demo không phải feedback đủ cho mọi risk. Prototype, pilot, simulation, regulatory review, load test, vendor proof-of-concept hay operational rehearsal đều là các feedback loop khác nhau.

Một project có nhiều feedback event nhưng vẫn học rất ít nếu feedback không chạm assumption critical.

## Cost of change không phải một đường cong cố định

Người học thường nghe “change càng muộn càng đắt”. Điều này đúng trong nhiều context nhưng không phải luật tuyệt đối. Cost of change phụ thuộc artifact đã commit, dependency đã phát sinh, contract đã khóa, data đã migrate, training đã rollout và expectation đã được public đến đâu.

Trong software có automated test, modular architecture và feature flag, một số change muộn có thể vẫn rẻ. Trong construction, hardware fabrication hoặc regulated submission, change muộn có thể rất đắt.

Delivery approach nên được chọn dựa trên **actual change economics**, không dựa vào slogan theo methodology.

## Predictive: khi việc dự đoán có giá trị cao

Predictive approach (phương pháp dự đoán / 예측형 접근) phù hợp khi scope có thể xác định tương đối sớm, dependency rõ, thay đổi muộn đắt, hoặc contract/regulation yêu cầu baseline mạnh. Công trình xây dựng là ví dụ trực quan: không thể liên tục đổi vị trí cột chịu lực sau khi đã thi công.

Predictive không có nghĩa “không thay đổi”. Nó làm change explicit bằng baseline, impact analysis và change control. Strength của nó là coordination và predictability khi knowledge đủ ổn định; weakness là feedback có thể đến muộn nếu ta giả định quá nhiều điều chưa biết.

Điểm sâu hơn là predictive đặt commitment tương đối sớm. Vì vậy nó hiệu quả nhất khi information lúc commitment đủ tốt. Nếu commitment được đưa ra sớm hơn khả năng hiểu problem, baseline có thể tạo cảm giác chắc chắn giả. Khi đó project không thực sự “có kế hoạch tốt”; nó chỉ có một forecast được trình bày như commitment.

## Predictive failure không phải lúc nào do “Waterfall”

Một predictive project có thể thất bại vì requirement discovery kém, dependency model sai, governance latency hoặc incentive khiến bad news bị giấu. Chuyển sang sprint không tự sửa những nguyên nhân này.

Cần phân biệt **approach failure** với **execution-system failure**. Nếu uncertainty thật sự thấp nhưng team vẫn trễ vì resource contention, vấn đề không phải predictive. Nếu uncertainty cao nhưng organization bắt baseline chi tiết quá sớm, lúc đó delivery approach mới là nguyên nhân cấu trúc.

## Adaptive/agile: khi learning có giá trị cao

Adaptive approach (phương pháp thích ứng / 적응형 접근) phù hợp khi requirement hoặc solution uncertainty cao và có thể nhận feedback qua increment nhỏ. Thay vì tối ưu khả năng dự đoán toàn bộ scope, nó tối ưu tốc độ học và khả năng đổi hướng.

Batch nhỏ làm giảm cost of wrong assumption. Nếu một feature mất hai tuần để thử và bị bác bỏ, tổn thất nhỏ hơn việc dành sáu tháng xây toàn bộ system rồi mới cho user xem. Nhưng adaptive không loại bỏ governance, architecture, compliance hay long-term thinking. Nó chỉ thay cách và thời điểm ra quyết định.

Adaptive chỉ có giá trị khi feedback có thể thay decision. Nếu team demo mỗi hai tuần nhưng scope, priority, budget và release plan đều không được phép thay, vòng lặp chỉ tạo ceremony chứ không tạo adaptation.

## Feedback latency quyết định learning speed

Adaptive delivery không chỉ nói về iteration length. Điều quan trọng hơn là từ lúc một assumption được đưa vào work đến lúc project nhận evidence đủ để giữ hoặc thay decision mất bao lâu.

Một team có sprint hai tuần nhưng production feedback ba tháng một lần vẫn có learning latency dài. Ngược lại, một predictive project có prototype sớm và customer validation mạnh có thể giảm một số uncertainty rất nhanh.

Ta có thể nghĩ đơn giản:

```text
learning speed ≈ quality of feedback / feedback latency
```

Đây không phải công thức toán học, mà là mental model: feedback nhanh nhưng noise cao không giúp nhiều; feedback chất lượng nhưng đến quá muộn cũng làm rework lớn.

## Batch size và risk exposure

Batch càng lớn, càng nhiều assumption được đóng gói trước khi nhận feedback. Khi batch sai, rework blast radius lớn hơn.

Nhưng batch quá nhỏ cũng có overhead: deployment, approval, setup hoặc validation cost có thể cao. Tailoring phải tìm economic batch size hợp lý thay vì mặc định “nhỏ nhất luôn tốt nhất”.

Trong regulated project, có thể development batch nhỏ nhưng evidence package/release gate lớn hơn vì compliance transaction cost. Hybrid thường xuất hiện chính ở đây.

## Hybrid không phải “lấy một nửa mỗi bên”

Hybrid approach (phương pháp lai / 하이브리드 접근) có ý nghĩa khi các phần của system có uncertainty/cost profile khác nhau. Ví dụ core integration với regulator có interface cố định và milestone cứng, trong khi UX có thể được phát triển iteratively. Ta có thể baseline external milestones nhưng dùng backlog và sprint cho interaction design.

Hybrid tệ là giữ toàn bộ bureaucracy của predictive và toàn bộ ceremony của agile cùng lúc. Hybrid tốt chọn mechanism theo problem: phần nào cần predictability, phần nào cần feedback, và interface giữa hai phần được quản lý thế nào.

Điểm khó nhất của hybrid thường không nằm trong từng phần mà ở interface. Một vendor predictive có thể yêu cầu specification freeze trong khi product team adaptive vẫn thay backlog. Nếu không định nghĩa rõ change window, versioning, acceptance và dependency, mỗi bên đều có thể “làm đúng process” nhưng toàn hệ thống vẫn trễ.

## Hybrid interface cần contract rõ hơn methodology label

Mỗi boundary giữa hai delivery mode nên làm rõ ít nhất: artifact nào là authoritative, version nào được dùng, cadence handoff, acceptance rule, change window, dependency owner và escalation threshold.

Ví dụ adaptive UX team release mỗi sprint nhưng vendor chỉ nhận API change mỗi tháng. Nếu interface cadence không explicit, backlog priority nội bộ có thể tạo work không deploy được. Vấn đề ở đây là **coordination architecture**, không phải team nào “less agile”.

## Tailoring như một bài toán control system

Một process tạo overhead để đổi lấy visibility, coordination hoặc risk reduction. Nếu artifact không thay đổi decision nào, nó có thể chỉ là waste. Ngược lại, bỏ artifact critical chỉ vì “nhẹ” có thể làm tổ chức mất evidence cần cho compliance hoặc audit.

Có thể reasoning theo chuỗi:

```text
context → uncertainty/risk → information need → control/feedback → artifact/cadence
```

Ví dụ project ít người, low risk, co-located có thể không cần status report dài. Nhưng project tài chính có vendor, security review và regulator cần traceability mạnh; cùng một report/control lúc này có purpose rõ.

Tailoring tốt luôn giữ control objective trước rồi mới thay mechanism. Nếu objective là “không release khi privacy evidence chưa đủ”, ta có thể thay manual meeting bằng automated gate, nhưng không được bỏ requirement chỉ vì muốn delivery nhanh hơn.

## Control strength nên tỷ lệ với consequence

Không phải mọi decision cần cùng governance. Reversible low-impact decision có thể được decentralize; irreversible high-impact decision cần evidence, review và authority mạnh hơn.

Một cách nhìn hữu ích là:

```text
control intensity ↑ khi
impact ↑, irreversibility ↑, external obligation ↑, information asymmetry ↑
```

Đây là lý do một CSS change không cần CCB nhưng thay data-retention policy có thể cần legal/compliance approval dù coding effort nhỏ.

## Tailoring economics: control cũng có cost

Control không miễn phí. Mỗi approval, report, meeting, evidence package hoặc handoff tạo transaction cost và decision latency. Thiếu control gây failure risk; quá nhiều control làm flow chậm và khiến team tìm đường vòng.

Tailoring maturity nằm ở việc tối ưu **total cost of governance**, không phải tối thiểu hóa ceremony.

Nếu review thêm một ngày nhưng giảm đáng kể risk của irreversible release, cost hợp lý. Nếu 12 approver cùng ký một low-risk change nhưng không ai thực sự thêm information, control đó chỉ chuyển trách nhiệm mà không tăng decision quality.

## Governance cadence và decision latency

Cadence nên match tốc độ thay đổi của information. Risk review hàng quý có thể vô nghĩa trong một project release hàng tuần. Ngược lại executive steering meeting hàng ngày tạo overhead mà không có new evidence tương xứng.

Decision latency là thời gian từ khi decision need xuất hiện đến khi authority quyết. Tailoring phải xem latency có phù hợp với delivery cadence không. Team sprint hai tuần nhưng procurement approval sáu tuần tạo bottleneck governance, dù development rất nhanh.

Một control system tốt không chỉ biết **ai quyết**, mà còn biết **cần quyết trong bao lâu**.

## Một khung chọn approach thực tế

Có thể đánh giá một dự án bằng sáu câu hỏi. Requirement có ổn định không? Solution có quen thuộc không? Feedback có thể lấy sớm không? Change muộn có đắt không? Compliance/contract có yêu cầu evidence cố định không? Dependency vật lý hoặc external có buộc sequence cứng không?

Nếu requirement và solution đều ổn định, change muộn đắt và external dependency chặt, predictive thường có lợi. Nếu requirement hoặc solution còn nhiều unknown nhưng có thể test bằng increment nhỏ, adaptive mạnh hơn. Nếu các subsystem có profile khác nhau, hybrid thường hợp lý hơn một methodology duy nhất.

Khung này không tạo answer tự động. Nó buộc team giải thích vì sao một practice tồn tại thay vì chọn theo thói quen tổ chức.

## Delivery approach có thể khác theo layer

Không nhất thiết cả project có một approach duy nhất. Governance/funding có thể predictive, product discovery adaptive, procurement milestone-based, infrastructure migration phased và operations transition theo readiness gate.

Điểm quan trọng là các layer phải có interface rõ. “Project này Agile” là mô tả quá thô nếu funding chỉ duyệt theo annual fixed scope và vendor contract không cho change.

## Rolling-wave planning và planning horizon

Khi thông tin xa tương lai kém tin cậy, ta lập kế hoạch chi tiết cho near term và coarse-grained cho far term. Đây là rolling-wave planning (lập kế hoạch cuốn chiếu / 점진적 상세 계획). Nó không phải thiếu kế hoạch; nó thừa nhận information quality giảm theo time horizon.

Một roadmap 12 tháng có thể xác định outcome/milestone, nhưng task chi tiết chỉ nên chắc trong vài tuần hoặc vài tháng tùy domain. Nếu cố chi tiết hóa quá sớm, ta tạo false precision và tốn chi phí cập nhật.

Ngược lại, rolling-wave không được dùng như lý do để bỏ qua dependency dài hạn. Procurement lead time sáu tháng hoặc regulatory approval ba tháng phải được nhìn thấy sớm dù task implementation chi tiết chưa cần xác định.

## Planning horizon nên gắn với decision horizon

Chi tiết chỉ có giá trị nếu giúp một decision sắp tới. Nếu team chưa cần chọn implementation option trong sáu tháng nữa và evidence còn thay đổi mạnh, plan chi tiết hôm nay dễ trở thành waste.

Nhưng decision có lead time dài phải được kéo về sớm. Đây là khác biệt giữa **work horizon** và **decision horizon**. Một thiết bị chỉ được lắp sáu tháng sau nhưng procurement decision có thể cần xảy ra ngay hôm nay.

## Stage gate và progressive commitment

Stage gate có ý nghĩa khi organization muốn tăng mức commitment theo evidence. Ở đầu project có thể chỉ duyệt discovery budget. Sau prototype và risk review mới duyệt full implementation. Trước production lại có readiness gate.

Mental model ở đây là progressive commitment: càng gần irreversible investment, yêu cầu evidence càng mạnh. Đây cũng là cách giảm sunk-cost trap vì project có cơ hội bị dừng hoặc đổi hướng trước khi chi phí lớn hơn.

## Gate phải có exit option thật

Nếu mọi stage gate luôn approve vì “đã đi đến đây rồi”, gate không còn chức năng. Một gate thực sự cần option continue, conditionally continue, pivot, pause hoặc stop.

Criteria nên được xác định trước khi emotion/sunk cost tăng. Ví dụ pilot chỉ mở rộng nếu adoption > X, error < Y và operational cost < Z. Nếu threshold được đổi sau khi thấy kết quả để tránh stop, governance đã mất integrity.

## Tailoring theo organizational capability

Approach phù hợp trên lý thuyết có thể thất bại nếu organization chưa có capability. Continuous delivery cần automated test, deployment discipline và product decision rights. Decentralized decision cần skill và transparency. Predictive baseline cần estimation/data quality đủ tốt.

Vì vậy tailoring phải xét không chỉ project uncertainty mà cả **capability của system thực thi**. Chọn practice vượt xa capability hiện tại có thể tạo theater; chọn practice quá thấp so với capability lại bỏ phí lợi thế.

## Transition là phần của lifecycle, không phải hậu sự

Project không tạo value chỉ vì deliverable đã “xong”. Cần transition sang operation, product team, customer hoặc business owner. Transition có thể gồm training, support model, runbook, ownership transfer, data migration, warranty, operational acceptance và benefits tracking.

Nếu transition không được thiết kế từ đầu, project có thể đóng hành chính nhưng organization chưa thực sự có capability bền vững. Điều này đặc biệt quan trọng với system software, nơi production ownership và incident responsibility phải rõ trước go-live.

## Transition readiness là evidence, không phải calendar date

Go-live date không tự tạo readiness. Readiness cần evidence như operation owner rõ, support coverage, monitoring, rollback, knowledge transfer, access, data quality và incident path.

Nếu date đến nhưng readiness evidence thiếu, project phải surface trade-off thay vì gọi “schedule success” rồi đẩy risk sang operations.

## Tailoring anti-patterns

Một anti-pattern phổ biến là cargo-cult methodology: giữ artifact và ceremony vì “framework yêu cầu” dù không ai dùng output để quyết định. Anti-pattern thứ hai là methodology shopping: đổi framework mỗi khi project gặp khó thay vì sửa root cause về authority, capability hay dependency. Anti-pattern thứ ba là gọi mọi exception là “hybrid” nhưng không định nghĩa interface giữa các mode. Anti-pattern cuối cùng là over-tailoring: bỏ quá nhiều control đến mức project mất traceability và shared understanding.

Một anti-pattern tinh vi hơn là **tailoring theo convenience**: control bị bỏ vì team không thích, không phải vì risk đã giảm. Ngược lại **control accumulation** xảy ra khi mỗi incident thêm một approval mới nhưng không bao giờ retire control cũ, khiến governance ngày càng chậm.

Tailoring chỉ tốt khi giảm waste mà không làm mất information cần cho decision.

## Tailoring cần review lại khi context đổi

Tailoring không phải decision một lần lúc kickoff. Khi team size tăng, vendor mới vào, regulation đổi, incident xảy ra hoặc product chuyển từ discovery sang scale, control need thay đổi.

Một lightweight project có thể cần formal configuration control sau khi nhiều team cùng integration. Một regulated pilot có thể giảm một số ceremony khi evidence/automation trưởng thành. Process architecture phải tiến hóa cùng risk profile.

## Mixed uncertainty profile: một project có nhiều logic delivery cùng lúc

Một project hiếm khi có chỉ một loại uncertainty. Ví dụ eKYC có thể có requirement compliance gần như cố định, solution uncertainty ở OCR/face matching, execution uncertainty ở integration với legacy, external uncertainty từ regulator/vendor và adoption uncertainty ở customer behavior. Nếu organization chọn một methodology duy nhất cho toàn bộ project, ít nhất một loại uncertainty thường bị xử lý bằng feedback mechanism không phù hợp.

Cách reasoning tốt hơn là tạo một **uncertainty profile** cho từng boundary quan trọng. Compliance requirement có thể cần baseline và formal evidence. Model quality cần pilot/segmented evaluation. UX cần user feedback ngắn. Legacy integration cần early technical spike. Operations readiness cần rehearsal gần transition. Đây không phải “trộn framework”; đây là ánh xạ uncertainty → evidence mechanism.

Điểm quan trọng hơn là uncertainty profile có thể **di chuyển theo lifecycle**. Lúc đầu requirement uncertainty có thể cao; sau discovery nó giảm nhưng execution uncertainty tăng khi nhiều dependency bắt đầu tương tác. Gần go-live, technical uncertainty có thể giảm trong khi adoption và operational uncertainty trở thành dominant. Tailoring trưởng thành phải theo dõi sự dịch chuyển này thay vì giữ nguyên process vì “đã thống nhất từ đầu”.

## Nhiều feedback loop có cadence khác nhau

Một project có thể có customer feedback mỗi tuần, integration test mỗi hai tuần, vendor contract review mỗi tháng và regulatory gate mỗi quý. Nếu chỉ chọn một cadence chung, hoặc feedback nhanh bị chặn bởi gate chậm, hoặc governance phải họp quá thường xuyên mà không có evidence mới.

Do đó cần phân biệt **local cadence** và **synchronization point**. Team có thể inspect/adapt nhanh bên trong boundary nhưng chỉ synchronize với external authority khi đủ information. Tuy nhiên synchronization quá thưa tạo batch risk: nhiều decision nội bộ tích tụ rồi va vào regulatory/vendor boundary một lần.

Một design tốt giảm khoảng cách giữa các cadence ở những interface có coupling cao. Nếu product backlog thay đổi hàng tuần nhưng vendor interface freeze mỗi ba tháng, project cần compatibility/versioning hoặc change window rõ; nếu không, local agility tạo downstream rework.

## Decision-flip test: variable nào làm approach phải đổi?

Một cách kiểm tra tailoring có logic hay không là hỏi: **điều gì nếu thay đổi sẽ khiến ta chọn mechanism khác?** Nếu câu trả lời là “không gì cả vì công ty luôn làm Scrum/Waterfall”, approach đang dựa trên identity chứ không dựa trên context.

Ví dụ nếu feedback có thể lấy trong hai ngày thay vì ba tháng, adaptive experimentation trở nên đáng giá hơn. Nếu change trở nên gần như irreversible sau fabrication, commitment cần sớm và control mạnh hơn. Nếu regulation bỏ mandatory gate, governance có thể nhẹ hơn. Nếu automated testing làm regression cost giảm mạnh, batch/release strategy có thể thay đổi. Nếu team chưa đủ skill để decentralized decision, autonomy boundary phải hẹp hơn dù uncertainty vẫn cao.

Decision-flip test buộc team nêu **causal variable** đứng sau methodology. Nó cũng giúp review tailoring khi context đổi: ta không hỏi “có nên Agile hơn không?”, mà hỏi “feedback economics, irreversibility, coupling hoặc control consequence đã thay đổi chưa?”.

## Methodology inertia và tailoring debt

Một process từng hợp lý có thể trở thành overhead khi context đổi. Pilot nhỏ ban đầu có approval nhẹ; khi scale sang nhiều country và personal data, control cũ có thể quá yếu. Ngược lại, emergency controls thêm sau incident có thể vẫn tồn tại nhiều năm dù automation và capability đã làm risk giảm.

Đây có thể xem như **tailoring debt**: khoảng cách giữa process hiện tại và control architecture mà context bây giờ thực sự cần. Tailoring debt tăng khi organization không retire control cũ, không thêm control mới khi exposure tăng, hoặc giữ cadence/authority của giai đoạn trước.

Review lifecycle nên vì thế hỏi không chỉ “process có được follow không?” mà còn “process này còn đúng problem không?”. Compliance với một process lỗi thời không phải maturity.

## Tailoring decision example

Dự án eKYC phải tích hợp vendor, đáp ứng privacy/security, vượt UAT với ngân hàng, nhưng UI và flow onboarding còn cần user feedback. Approach hợp lý có thể là hybrid: compliance/security gates và vendor milestones được quản lý bằng acceptance criteria/baseline rõ; UX được iteratively refined; integration risk được prototype sớm; deployment có cutover plan riêng.

Nếu vendor API còn chưa ổn định, integration spike nên xảy ra sớm hơn việc hoàn thiện toàn bộ UI. Nếu regulator có deadline cứng, mandatory compliance scope phải được phân biệt với optional feature. Nếu user feedback chỉ có thể nhận sau pilot, project cần thiết kế pilot như một learning milestone chứ không chỉ là demo.

Điểm quan trọng không phải tên methodology mà là từng mechanism đang giải quyết uncertainty hoặc constraint nào.

## Counterexample: Agile không phải lúc nào giảm risk

Giả sử hardware cần đặt trước sáu tháng và vendor chỉ chấp nhận một interface version trước fabrication. Nếu team trì hoãn interface decision quá lâu với lý do “giữ option”, họ có thể bỏ lỡ procurement window. Trong context này, early commitment ở boundary hardware lại giảm risk.

Ngược lại, nếu UI preference chưa rõ mà project freeze toàn bộ interaction design cùng lúc với hardware interface, commitment đó không mang thêm coordination value. Tailoring tốt tách hai loại uncertainty thay vì dùng một ideology cho toàn hệ thống.

## Mental model

> Chọn delivery approach là chọn vị trí đặt feedback, commitment và control. Tailoring tốt đồng bộ uncertainty, feedback latency, reversibility, governance cost và organizational capability để mỗi commitment xảy ra khi evidence đủ mạnh.

Tiếp theo: [People, leadership, team và conflict](./02_people_leadership_team_and_conflict.md).