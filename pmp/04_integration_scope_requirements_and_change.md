# 04 — Integration, scope, requirements và change

## Integration là quản lý interaction giữa các quyết định

Tích hợp dự án (project integration management / 프로젝트 통합 관리) không đơn giản là gom nhiều plan vào một file. Scope thay đổi có thể làm schedule, cost, procurement, risk và stakeholder expectation thay đổi cùng lúc. Integration là năng lực nhìn project như một system và giữ các decision nhất quán với nhau.

Integrated project management plan vì vậy là một coherent decision model: delivery approach, baselines khi cần, governance, subsidiary plans, thresholds và cách kiểm soát change. Giá trị của nó nằm ở consistency chứ không ở độ dày.

Integration đặc biệt quan trọng ở boundary. Một local decision có thể tối ưu subsystem nhưng làm toàn project tệ hơn. Team technical có thể chọn solution tốt nhất về performance nhưng phá vendor contract; business có thể thêm feature high-value nhưng làm compliance review trễ. Project manager phải nhìn effect lan truyền trước khi decision được commit.

## Integration là operating system của project

Một cách hiểu sâu hơn là xem integration như operating system của project. Mỗi domain tạo local state: scope có requirement và baseline; schedule có dependency và forecast; finance có budget và actual; risk có exposure; procurement có obligation; stakeholder có expectation. Nếu các local state này không được đồng bộ, project có nhiều “sự thật” cùng tồn tại.

Integration tạo protocol để một thay đổi ở một domain được nhận diện, phân tích, quyết định và phản ánh vào các domain liên quan. Nếu vendor delivery date đổi nhưng schedule, risk register, cash forecast và stakeholder commitment vẫn giữ state cũ, project đã mất coherence dù từng artifact riêng lẻ vẫn nhìn hợp lệ.

Vì vậy maturity của integration không nằm ở số meeting coordination mà ở tốc độ và độ chính xác của state propagation.

## Integration là quản lý constraint coupling

Scope, schedule, cost, quality và risk không phải các thanh trượt độc lập. Chúng coupling với nhau. Rút schedule có thể làm cost hoặc risk tăng. Giảm cost có thể giảm redundancy và quality margin. Tăng scope có thể làm resource contention xuất hiện.

Vì vậy câu hỏi đúng không phải “change này ảnh hưởng schedule bao nhiêu?” mà là “change này làm objective và constraint system thay đổi ra sao?”. Impact analysis tốt luôn multidimensional.

Coupling còn có thể phi tuyến. Thêm 5% scope không nhất thiết tăng 5% duration. Nếu phần thêm chạm một regulatory review hoặc vendor interface, nó có thể mở một dependency chain mới và kéo finish date nhiều tuần. Project manager cần tìm discontinuity như gate, shared resource, license threshold hoặc architecture boundary, không chỉ dùng tỷ lệ tuyến tính.

## Project charter và integrated direction

Charter thiết lập project purpose, high-level objective, sponsor, authority và boundary. Nó giúp tránh project bắt đầu execution khi chưa có agreement tối thiểu về vì sao investment tồn tại.

Project management plan phát triển direction đó thành operating model. Charter không cần mô tả cách quản lý mọi domain; plan không nên thay business justification. Hai artifact ở hai abstraction level khác nhau.

Charter cũng tạo anchor khi project bị kéo theo local pressure. Nếu một request mới hấp dẫn nhưng không còn phục vụ objective được authorize, team cần đưa nó trở lại business-case/change reasoning thay vì mặc định hấp thụ.

## Scope: boundary của commitment

Phạm vi (scope / 범위) mô tả những gì project/product cam kết tạo ra và boundary của công việc cần thiết. Product scope nói về feature/capability; project scope nói về work để tạo ra result đó.

Scope cần đủ rõ để stakeholder có thể đồng ý và team có thể decompose. Nhưng “rõ” không nhất thiết nghĩa mọi chi tiết cố định từ đầu. Trong adaptive project, product backlog là một scope model động; trong predictive project, scope baseline thường ổn định hơn và change được formalized.

Scope boundary còn cần nói rõ exclusion. “Không bao gồm migration historical data trước 2020” có thể quan trọng ngang “bao gồm customer profile migration”. Exclusion làm hidden assumption visible.

Một boundary tốt còn nêu interface. Nếu project tạo API nhưng downstream migration do chương trình khác làm, interface acceptance và handoff condition phải rõ; nếu không, mỗi bên có thể hoàn thành “scope của mình” nhưng system outcome vẫn thiếu.

## Requirement không phải solution statement

Requirement mô tả need, condition hoặc capability cần đạt. Solution design mô tả cách đạt nó. Nhầm hai lớp làm solution space bị khóa sớm.

Ví dụ “user phải đăng nhập bằng OTP SMS” nghe như requirement nhưng có thể thực chất need là “xác thực possession factor”. Nếu regulation không bắt SMS, passkey hoặc app-based OTP có thể tốt hơn. Tách need khỏi implementation giúp option analysis.

Một kỹ thuật reasoning hữu ích là hỏi nhiều lần “tại sao cần điều này?”. Nếu answer quay về business need, risk/control objective hoặc stakeholder outcome, requirement đang tiến gần problem layer. Nếu answer chỉ lặp implementation, có thể solution đã bị masquerade thành requirement.

## Requirement conflict không thể giải bằng cách giữ tất cả

Stakeholder có thể đưa requirement mâu thuẫn. Security muốn session timeout ngắn; user experience muốn không bị logout. Finance muốn giảm vendor cost; operations muốn premium support. Ghi cả hai vào backlog không giải conflict.

Project cần explicit priority và trade-off authority. Conflict nên được đưa về objective, risk appetite, compliance và value. Requirement engineering trưởng thành không chỉ capture nhu cầu mà còn resolve inconsistency trước khi nó trở thành design rework.

Nếu conflict được trì hoãn quá lâu, team thường tự quyết ngầm ở implementation. Khi đó một technical decision vô tình trở thành business decision mà không có đúng authority.

## Assumption là dependency vô hình

Nhiều plan nhìn nhất quán chỉ vì một assumption chưa bị kiểm tra: “vendor sẽ hỗ trợ API này”, “regulator chấp nhận control tương đương”, “user có smartphone mới”, “data quality đủ tốt” hoặc “operations có capacity nhận thêm workload”. Assumption chưa được chứng minh nhưng thường được dùng như fact trong schedule, budget và design.

Vì vậy assumption material nên có owner, evidence plan, expiry/validation date và consequence nếu sai. Khi assumption đổi state, integration mechanism phải biết artifact/decision nào phụ thuộc nó. Đây là **assumption dependency graph**.

Một assumption có blast radius lớn đáng được validate sớm ngay cả khi probability sai không cao. Nếu toàn bộ architecture và contract phụ thuộc một interpretation pháp lý, value of information của việc xác minh sớm có thể rất lớn.

Assumption debt xuất hiện khi project tiếp tục build nhiều layer trên assumption chưa kiểm chứng. Mỗi layer mới làm reversal cost tăng. Đây là lý do discovery, spike, pilot hoặc early external review có thể là integration control chứ không chỉ technical activity.

## Requirement và acceptance

Requirement là need/condition/capability cần được đáp ứng. Một requirement chưa testable thường còn ambiguity. Acceptance criteria biến intent thành điều kiện kiểm chứng.

Trong software, một câu “hệ thống phải nhanh” không đủ. “95% API request dưới 300 ms ở workload X” tạo evidence. Chiều kỹ thuật sâu hơn đã có ở canonical [Requirements Engineering](../computer_science/09_software_engineering/00_requirements_specification_and_engineering_process.md); chapter này tập trung vào tác động cấp project.

Acceptance criterion tốt phải đủ cụ thể để hai bên có cùng answer khi kiểm tra. Nếu acceptance phụ thuộc cảm nhận chủ quan nhưng không có user-test protocol, dispute rất dễ xảy ra ở cuối.

Acceptance criteria cũng cần phản ánh operating context. Performance test ở 100 user không chứng minh requirement nếu production expected 10.000 concurrent user. Evidence chỉ mạnh khi test condition tương thích với claim cần chứng minh.

## Verification và validation là hai câu hỏi khác nhau

Verification hỏi deliverable được xây đúng specification chưa. Validation hỏi deliverable có giải đúng need trong context sử dụng không. Một system có thể pass toàn bộ test kỹ thuật nhưng user vẫn không thể hoàn thành business flow.

Ở project level, distinction này ngăn team đồng nhất “test pass” với “value achieved”. Acceptance thường cần evidence về conformance; benefit realization cần evidence về outcome sau khi capability được dùng.

## Functional và non-functional requirement

Functional requirement nói system cần làm gì. Non-functional requirement mô tả quality hoặc constraint như performance, security, availability, usability, portability hoặc compliance.

Project thường under-plan non-functional requirement vì chúng ít visible trong demo nhưng có thể quyết định go-live. Một feature đủ chức năng nhưng không đạt security review vẫn chưa usable trong context thật.

Non-functional requirement thường tạo cross-cutting work. Security hoặc availability không nằm gọn trong một feature; nó ảnh hưởng architecture, test, monitoring, vendor và operations. Vì vậy chúng cần được đưa vào integration reasoning sớm.

## Requirement lifecycle và traceability

Requirement không chỉ được “thu thập” rồi đóng. Nó cần source, owner, priority, rationale, status, acceptance evidence và impact khi thay đổi.

Traceability nối business need → requirement → deliverable/design → verification → outcome. Điều này giúp phát hiện orphan feature và uncovered requirement. Chi tiết hơn xem [Artifacts, information flow và traceability](./14_artifacts_information_and_traceability.md).

Traceability còn giúp đánh giá blast radius khi change. Nếu requirement A đổi, graph cho biết design, test, vendor obligation, training và operational control nào cần review. Traceability vì vậy vừa phục vụ compliance vừa phục vụ change economics.

## Decomposition và WBS

Work Breakdown Structure (WBS / 작업분류체계) decompose project scope thành các phần quản lý được. WBS tốt là product/deliverable-oriented trước khi biến thành activity list. Điều này giúp giữ connection giữa work và output.

Decomposition phải đủ chi tiết để estimate, assign và control, nhưng quá chi tiết tạo maintenance overhead. Work package là level đủ nhỏ để có owner/estimate/control hợp lý trong context.

Trong adaptive delivery, backlog decomposition thực hiện chức năng tương tự nhưng theo rolling horizon: epic/capability được chia dần thành item nhỏ khi gần delivery.

Decomposition cũng expose interface. Nếu hai work package cần cùng một data model hoặc cùng một expert, dependency nên được nhìn thấy trước khi activity scheduling.

## 100% rule và boundary discipline

Một WBS thường dùng mental model 100% rule: parent scope được bao phủ đầy đủ bởi child elements mà không cố ý thêm work ngoài boundary.

Điểm quan trọng không phải thuộc rule để thi mà là tránh hai lỗi: missing work và duplicate work. Nếu testing hoặc migration không nằm trong WBS vì “đó không phải feature”, estimate sẽ thiếu dù implementation scope đúng.

100% rule không yêu cầu mô tả mọi micro-task. Nó yêu cầu không để critical deliverable/work biến mất giữa abstraction level.

## Scope validation và quality control khác nhau

Quality control hỏi deliverable có đáp ứng specification hay không. Validate scope hỏi customer/sponsor có formally accept deliverable phù hợp hay không.

Một component có thể pass internal QA nhưng chưa được customer accept. Ngược lại, stakeholder có thể accept deliverable với agreed exception dù một noncritical defect còn tồn tại. Hai process dùng evidence liên quan nhưng purpose khác.

## Acceptance debt

Acceptance debt xuất hiện khi team hoàn thành technical work nhưng trì hoãn acceptance evidence hoặc stakeholder validation. Dashboard có thể báo nhiều item “done”, trong khi business chưa xác nhận deliverable thực sự usable.

Debt này nguy hiểm vì defect hoặc expectation gap được phát hiện muộn, khi cost of change cao hơn. Early acceptance slice hoặc progressive validation làm giảm batch size của uncertainty.

## Scope creep và gold plating

Scope creep là expansion không được kiểm soát của scope. Gold plating là thêm feature/quality không được yêu cầu chỉ vì team nghĩ nó tốt. Cả hai đều nguy hiểm vì dùng resource và thay risk profile mà không có explicit decision.

Đây không có nghĩa mọi idea mới phải bị từ chối. Idea có value nên đi qua change/prioritization mechanism để trade-off được nhìn thấy.

Gold plating còn tạo support obligation. Một feature không được yêu cầu nhưng đã release có thể trở thành permanent product expectation và tăng maintenance cost.

## Change là normal; uncontrolled change mới là problem

Project tồn tại trong môi trường thay đổi. Mục tiêu không phải giữ plan bất biến mà là đảm bảo change được đưa vào decision system phù hợp.

Predictive context thường cần formal impact analysis và approval khi baseline bị ảnh hưởng. Adaptive context absorb nhiều product change qua backlog reprioritization, nhưng budget, regulatory scope, contract và release commitment vẫn có guardrail.

Không có một change process duy nhất cho mọi level. Typo trong document và thay authentication architecture không cần cùng governance.

## Cost of change và timing của decision

Một change giống nhau có cost khác nhau tùy thời điểm. Đổi requirement trước design rẻ hơn sau procurement, integration test hoặc regulatory submission. Đây là lý do early feedback có economic value.

Tuy nhiên quyết định quá sớm khi information chưa đủ cũng có cost. Integration cần cân bằng hai áp lực: delay decision có thể làm change cost tăng; commit sớm có thể khóa option sai. Reversible decision nên giữ linh hoạt lâu hơn; irreversible/long-lead decision cần evidence sớm hơn.

## Change control: bảo vệ coherence, không bảo vệ status quo

Change control (kiểm soát thay đổi / 변경 통제) tồn tại vì một change có second-order effect. Quy trình hợp lý thường bắt đầu bằng mô tả change và reason, sau đó impact analysis, authority decision, implementation, update artifacts/baselines và communication.

Trong predictive context, Change Control Board có thể phê duyệt change lớn. Trong adaptive context, product owner/backlog prioritization có thể hấp thụ requirement change mà không cần ceremony giống predictive, miễn guardrail về budget, release, compliance và architecture được giữ.

Điểm chung là không làm “silent change”. Decision phải có owner, impact và traceability phù hợp.

## Change authority và threshold

Không phải change nào cũng cần sponsor. Governance nên định nghĩa threshold để reversible/low-impact change được xử lý gần team, còn change vượt tolerance mới escalate.

Nếu mọi change đều lên CCB, queue và delay tăng. Nếu không change nào lên governance, organization mất control. Tailoring đúng là đặt decision đúng level.

Threshold nên gắn với materiality: budget tolerance, regulatory effect, customer commitment, architecture risk hoặc contract impact. “Mọi change trên 3 ngày” có thể quá thô nếu một thay đổi 1 ngày chạm privacy control còn một thay đổi 5 ngày chỉ đổi nội bộ.

## Change latency là một biến quản trị

Change latency là thời gian từ khi nhu cầu thay đổi được nhận diện tới khi decision đủ rõ để execution điều chỉnh. Latency quá cao làm team tiếp tục build theo assumption cũ; latency quá thấp nhưng thiếu analysis tạo quyết định hấp tấp.

Queue ở approval body là một source phổ biến. Nếu CCB họp mỗi tháng trong project có weekly market feedback, governance cadence không phù hợp với uncertainty cadence.

Một control tốt không chỉ hỏi “ai approve?” mà còn “decision phải xảy ra nhanh tới mức nào để còn tạo value?”.

## Impact analysis cần xem second-order effect

Một request “chỉ thêm một field” có thể chạm data model, API contract, migration, privacy classification, report, analytics, test và training.

Impact analysis nên đi qua scope, schedule, cost, quality, risk, resource, procurement, compliance, operation và stakeholder. Không phải mọi dimension đều bị ảnh hưởng, nhưng checklist mental này ngăn local estimate bị coi là total impact.

Second-order effect còn có feedback loop. Thêm feature làm schedule trễ; trễ làm contract milestone bị miss; miss milestone làm cash receipt chậm; cash pressure lại giảm ability thêm resource. Integration reasoning cần nhìn loop, không chỉ one-hop dependency.

## Change propagation và blast radius

Khi change được approve, câu hỏi tiếp theo là “state nào phải đổi?”. Có thể phải update requirement, WBS/backlog, schedule, cost forecast, risk response, vendor SOW, test evidence, training và operational runbook.

Blast radius càng rộng, coordination cost càng cao. Modular architecture, clear interface và decoupled contract boundary làm blast radius nhỏ hơn. Vì thế integration quality chịu ảnh hưởng trực tiếp bởi system design và organizational design.

## Concurrent change và collision risk

Hai change riêng lẻ có thể đều hợp lý nhưng xung đột khi diễn ra đồng thời. Team A đổi schema để hỗ trợ feature mới; Team B tối ưu migration dựa trên schema cũ. Security đổi authentication flow trong khi vendor đang certify integration. Mỗi change có impact analysis local đúng nhưng combined state lại không hợp lệ.

Vì vậy integration cần nhìn **change concurrency**, không chỉ từng ticket độc lập. Khi nhiều change chạm cùng interface, shared resource, baseline hoặc release window, cần sequence, compatibility rule hoặc synchronization point.

Collision risk tăng khi change throughput cao nhưng configuration visibility thấp. Adaptive delivery không loại bỏ vấn đề này; cadence nhanh thậm chí làm collision xảy ra nhanh hơn nếu interface contract và automated integration evidence yếu.

Một useful question là: “Nếu change A và B đều được approve, state cuối có còn coherent không?”. Đây là level reasoning cao hơn “A có approve được không?” và “B có approve được không?”.

## Configuration management và version truth

Khi nhiều version của requirement, design hoặc deliverable tồn tại, team cần biết cái nào là authorized state. Configuration management giải quyết identification, versioning, status accounting và control. Trong software, Git/CI/CD là một phần technical mechanism; ở project level còn có version của contract, scope baseline, test evidence và release package.

Configuration management khác change control nhưng liên quan chặt. Change control quyết định state có được đổi không; configuration control đảm bảo mọi người biết authorized state nào đang có hiệu lực.

Nếu change được approve nhưng vendor vẫn implement specification cũ, failure không nằm ở approval mà ở configuration propagation.

## Compatibility window và migration state

Trong project có nhiều team/vendor, không phải mọi component có thể đổi atomically. Một thời gian có thể phải hỗ trợ old và new state cùng tồn tại: API v1/v2, old/new process, legacy/new data format hoặc hai policy version trong transition.

Đây là **compatibility window**. Nó cần start/end condition, owner và retirement plan. Nếu chỉ thêm backward compatibility mà không có exit criterion, temporary complexity dễ trở thành permanent cost.

Migration state cũng tạo risk riêng: data có thể nằm ở hai source, user được chia cohort, support phải hiểu hai workflow. Integration plan phải quản lý intermediate state chứ không chỉ current state và target state.

## Baseline topology: scope, schedule và cost liên kết nhau

Scope, schedule và cost baseline không nên được xem là ba file rời. Chúng là ba projection của cùng commitment. Scope nói “cái gì”, schedule nói “khi nào”, cost nói “bao nhiêu resource”.

Một approved change có thể chỉ tác động một baseline, nhưng nếu scope tăng mà schedule/cost không đổi, cần giải thích mechanism nào hấp thụ change. Nếu không có mechanism, baseline set đã trở nên internally inconsistent.

Rebaseline chỉ nên xảy ra khi authorized planning basis thay đổi, không phải để xóa lịch sử performance. Original baseline, approved changes và current baseline cần trace được.

## Integrated change control và feedback loop

Sau khi change được approve, work chưa kết thúc. Plan, baseline, risk, requirement, procurement và communication cần được update. Nếu decision được approve nhưng downstream artifact không đổi, project có inconsistent truth.

Một good change loop là proposed → analyzed → decided → implemented → verified → reflected in source-of-truth. Mất một transition tạo hidden debt.

Verification của change cũng quan trọng. “Implemented” không đồng nghĩa intended effect đã đạt. Một new control cần evidence rằng risk giảm; một scope reduction cần evidence rằng dependency cũ thực sự được remove.

## Integration debt

Integration debt là khoảng cách giữa local states đã thay đổi và project-wide state chưa được reconcile. Ví dụ backlog đã bỏ feature nhưng contract chưa sửa; release đã đổi architecture nhưng runbook/training vẫn mô tả flow cũ; sponsor đã đổi benefit target nhưng metric plan chưa đổi.

Debt này thường không visible như defect. Mỗi artifact riêng có thể “đúng theo lần cập nhật cuối của nó”, nhưng chúng không còn đúng **cùng nhau**. Khi project gần gate hoặc handover, debt bùng ra thành reconciliation work, dispute hoặc rework.

Một cách kiểm soát là dùng integration checkpoint dựa trên event: approved material change, release candidate, vendor milestone, regulatory submission hoặc transition gate. Checkpoint không cần review mọi file; nó cần xác nhận những state có coupling cao đã converged về cùng authorized decision.

## Dependency management

Integration cũng là quản lý dependency. Dependency có thể technical, resource, external approval, contract hoặc organizational.

Một dependency tốt cần owner, needed-by date, current confidence và fallback/escalation. “Team B đang làm” không phải đủ information nếu milestone của Team A phụ thuộc output đó.

Dependency nên được giảm khi có thể, không chỉ theo dõi. Architecture decoupling, contract interface rõ hoặc team topology tốt có thể xóa coordination work khỏi project.

## Interface contract và handoff quality

Nhiều failure không xảy ra bên trong team mà ở handoff. Interface contract nên làm rõ input, output, format, acceptance, timing và error handling giữa hai workstream/party.

Nếu Team A “hoàn thành API” nhưng Team B không biết version, rate limit hoặc test environment, local completion không tạo integrated progress. Handoff cần evidence rằng receiving side có thể sử dụng output, không chỉ sender tuyên bố done.

## Decision log và consistency

Nhiều integration failure xuất hiện vì decision được đưa ra riêng lẻ trong các meeting khác nhau. Decision log giữ context và rationale giúp tránh contradiction.

Ví dụ security team approve design A với assumption data không lưu lâu dài, nhưng business sau đó quyết định retention 7 năm. Integration mechanism phải detect assumption conflict và trigger review.

Decision log mạnh hơn khi ghi decision owner, effective date, affected artifacts và assumption expiry. Nó trở thành node trong change graph thay vì meeting minutes.

## Ví dụ impact analysis

Customer yêu cầu thêm biometric fallback trước go-live. Thay vì hỏi “mất bao nhiêu ngày?”, PM cần kiểm tra ít nhất: requirement/security implication, vendor/API dependency, privacy review, test scope, schedule critical path, budget, operations training và business value. Có thể feature chỉ code ba ngày nhưng kéo thêm security approval hai tuần. Integration reasoning tìm total system impact chứ không chỉ coding effort.

Nếu fallback là mandatory regulatory requirement mới, priority khác hoàn toàn một optional UX enhancement. Nếu deadline legal không đổi, project có thể phải de-scope optional feature khác hoặc tăng capacity. Change decision là trade-off system, không phải estimate exercise.

Một scenario khác: sponsor approve scope reduction để giữ deadline nhưng procurement contract vẫn yêu cầu deliverable cũ. Nếu team chỉ update backlog, vendor vẫn có contractual obligation và invoice basis khác. Integration failure xuất hiện vì change chưa propagate qua commercial boundary.

## Failure modes

Local optimization xảy ra khi từng domain tối ưu riêng. Silent scope creep xảy ra khi team làm change trước approval. Baseline theater xảy ra khi baseline liên tục rewrite để không có variance. Requirement dumping xảy ra khi mọi stakeholder request đều được ghi nhưng không resolve conflict. Approval theater xảy ra khi CCB approve nhưng không ai update execution artifact.

Decision latency mismatch xảy ra khi governance cadence chậm hơn cadence của uncertainty. Configuration drift xảy ra khi các party dùng version khác nhau. Acceptance debt xảy ra khi technical completion đi trước formal/business validation. Interface blindness xảy ra khi mỗi team đúng local scope nhưng handoff không usable. Assumption debt làm nhiều commitment phụ thuộc fact chưa được chứng minh. Change collision xảy ra khi các change local hợp lệ tạo combined state không coherent. Integration debt tích khi artifact đúng riêng lẻ nhưng sai với nhau.

Integration maturity được đo bằng consistency giữa decision và actual project state.

## Mental model

> Scope tạo boundary cho commitment; change control giữ các commitment liên quan vẫn nhất quán khi boundary thay đổi. Integration là khả năng làm một decision propagate đúng qua requirement, assumption, baseline, dependency, contract, evidence và stakeholder trước khi các local state tách thành nhiều “sự thật”.

Tiếp theo: [Schedule, estimation, dependency và flow](./05_schedule_estimation_and_flow.md).
