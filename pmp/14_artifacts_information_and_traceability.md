# 14 — Artifacts, information flow và traceability

## Artifact chỉ có giá trị khi nó giữ hoặc truyền information cần cho decision

PMP có nhiều tên artifact nên người học dễ biến chúng thành danh sách cần thuộc. Cách hiểu bền hơn là hỏi mỗi artifact giải quyết information problem nào. Một register giữ tập item cùng loại qua thời gian; một log ghi các event/decision cần theo dõi; một baseline tạo reference để đo variance; một plan định nghĩa cách một loại work/control sẽ được thực hiện; một report nén state thành information cho stakeholder; một agreement tạo commitment giữa các party.

Nếu artifact không có consumer hoặc không thay đổi decision/control nào, nó có nguy cơ trở thành administrative waste. Ngược lại, thiếu artifact ở chỗ failure cost cao làm project mất memory và accountability.

Một artifact tốt cần answer bốn câu: ai dùng, để quyết điều gì, update khi nào, và đâu là source of truth. Nếu không trả lời được, artifact có thể đang tồn tại vì tradition chứ không vì information need.

## Artifact là external memory của temporary organization

Project là tổ chức tạm thời. Con người thay đổi, memory cá nhân mất đi và decision diễn ra ở nhiều thời điểm. Artifact tồn tại để externalize memory, làm coordination không phụ thuộc hoàn toàn vào việc “ai đó còn nhớ”.

Điều này đặc biệt quan trọng ở project dài hoặc có nhiều vendor. Một quyết định không ghi rationale có thể bị tranh luận lại vài tháng sau hoặc bị hiểu sai khi người cũ rời team.

External memory còn giúp accountability công bằng hơn. Khi decision được đánh giá bằng hindsight, artifact cho biết information và assumption có sẵn tại thời điểm quyết định, thay vì dùng knowledge xuất hiện sau đó để phán xét quá khứ.

## Project information architecture có nhiều lớp

Một mental model hữu ích là tách information thành bốn lớp:

```text
source evidence
    ↓
operational state
    ↓
decision / commitment
    ↓
reporting / governance view
```

Source evidence có thể là test result, invoice, system log, signed contract hoặc stakeholder approval. Operational state là risk status, work progress, forecast. Decision layer giữ approval, priority, exception và rationale. Reporting layer nén state cho steering committee hoặc stakeholder.

Nếu report không trace được về source evidence, dispute khó resolve. Nếu source evidence có nhưng decision không được record, project biết “điều gì xảy ra” nhưng không biết “vì sao state đổi”.

## Từ assumption tới decision

Assumption log ghi điều đang được coi là đúng nhưng chưa được chứng minh chắc chắn. Constraint là boundary phải tôn trọng. Risk register quản lý uncertainty có effect lên objective. Issue log quản lý problem đã materialize. Change log theo dõi proposed/approved/rejected change. Decision log giữ quyết định, rationale, owner và thời điểm.

Các artifact này không tách biệt hoàn toàn. Ví dụ assumption “vendor API ổn định trước UAT” bị evidence mới bác bỏ. Assumption chuyển thành risk hoặc issue; risk analysis tạo option; decision đổi integration plan; change có thể cập nhật schedule baseline. Traceability tốt cho phép đi ngược chuỗi để hiểu vì sao plan hiện tại khác plan ban đầu.

Một project information system trưởng thành không chỉ có nhiều document; nó cho phép state transition giữa các loại information mà không mất context.

## Information state transition cần được model explicit

Một signal thường đi qua nhiều state:

```text
observation → assumption/question → risk/issue → analysis → decision → change/action → evidence → closure
```

Không phải mọi signal đi hết chuỗi, nhưng mental model này giúp phát hiện “missing transition”. Nếu issue đã resolved nhưng decision/action evidence không có, status close có thể chỉ là administrative.

Nếu change được approved nhưng requirement/baseline không update, information state bị split. Nếu risk trigger xảy ra mà item vẫn nằm trong risk register như “open risk” nhưng không thành issue/action, tool đang giữ label cũ hơn reality.

## Register, log, plan, baseline, report và agreement khác nhau về purpose

Register thường là tập các item cùng loại cần theo dõi qua thời gian, ví dụ risk register hoặc stakeholder register. Log nhấn mạnh event/action history, ví dụ issue log hoặc decision log. Plan mô tả cách quản lý một domain. Baseline là reference được authorize. Report là view nén cho một audience. Agreement ghi commitment giữa party.

Phân biệt theo information purpose giúp nhớ artifact tự nhiên hơn học tên riêng lẻ.

## Semantic contract: cùng một field phải có cùng meaning

Một dashboard có thể đúng về arithmetic nhưng sai về semantics. “Completed” ở team A có thể nghĩa code complete; ở team B nghĩa accepted; ở team C nghĩa deployed. Tổng 80% completion khi definitions khác nhau không có meaning ổn định.

Critical metric/artifact cần semantic contract: definition, unit, source, owner, cutoff, inclusion/exclusion và update rule. Khi definition đổi, history có thể không còn comparable.

Semantic drift là failure mode khi cùng tên metric thay meaning theo thời gian nhưng chart vẫn nối thành một line như không có gì đổi.

## Data lineage: con số này đến từ đâu?

Lineage trả lời một reported value được tạo từ source nào, transform ra sao và version/cutoff nào. Ví dụ dashboard cost lấy invoice từ ERP, committed amount từ procurement và forecast từ PM tool.

Nếu steering committee hỏi vì sao EAC tăng 10%, team nên trace được change về vendor quote, scope decision hoặc productivity evidence. “Dashboard tự tính” không phải explanation.

Lineage đặc biệt quan trọng khi automation aggregate nhiều system. Tự động hóa làm calculation nhanh hơn nhưng cũng có thể propagate semantic error nhanh hơn.

## Requirements Traceability Matrix như một graph

Requirements Traceability Matrix (RTM / 요구사항 추적 매트릭스) thường được dạy như một bảng. Mental model tốt hơn là graph:

```text
business need
   ↓
requirement
   ↓
design/deliverable
   ↓
verification / acceptance evidence
   ↓
outcome / benefit metric
```

Không phải mọi project cần một spreadsheet RTM nặng. Nhưng regulated/high-risk project cần khả năng chứng minh requirement nào được thực hiện ở đâu và evidence nào xác nhận nó.

Trong software, traceability kỹ thuật có thể nối ticket → commit → build → test → deployment. PMP quan tâm boundary lớn hơn: requirement đó đến từ stakeholder/policy nào và acceptance/value được xác nhận ra sao.

## Traceability là graph hai chiều

Forward trace trả lời requirement này được implement và verify ở đâu. Backward trace trả lời feature hoặc control này tồn tại vì requirement/business need nào. Hai chiều đều quan trọng.

Nếu một feature không trace được tới need nào, nó có thể là scope creep. Nếu một requirement không trace được tới verification evidence, project chưa chứng minh completion. Nếu một test không trace tới requirement, có thể đang kiểm thứ không cần hoặc requirement chưa rõ.

## Traceability debt

Traceability debt xuất hiện khi work vẫn tiến nhưng link giữa need, change, implementation và evidence không được cập nhật. Debt có thể chưa gây failure ngay, nhưng cost xuất hiện khi audit, incident hoặc change impact analysis cần reconstruct history.

Debt tăng nhanh trong environment nhiều change. Nếu team liên tục sửa requirement nhưng RTM/test mapping chỉ update cuối release, họ đang tích information rework tương tự technical debt.

Không phải mọi project cần zero traceability debt. Low-risk prototype có thể chấp nhận nhẹ; regulated project có tolerance thấp hơn. Mức traceability phải tailor theo consequence.

## Project management plan và subsidiary plans

Project management plan là integrated control model. Các subsidiary plan như scope, schedule, cost, quality, resource, communication, risk, procurement hoặc stakeholder engagement chỉ nên tách khi complexity cần separation. Chúng trả lời “chúng ta sẽ quản lý domain này như thế nào?”, không phải “state hiện tại là gì?”.

Đây là distinction hữu ích: plan mô tả method/control; document/register thường mô tả current information. Risk management plan định nghĩa risk process/scales/roles; risk register chứa risk cụ thể.

Một plan stale nguy hiểm nếu team vẫn tưởng đó là operating rule hiện hành. Plan change cần governance phù hợp với impact.

## Baseline và working document

Baseline là authorized reference. Working forecast/document có thể thay đổi thường xuyên. Nhầm hai lớp tạo confusion: nếu mọi update forecast tự động rewrite baseline thì variance biến mất; nếu baseline không bao giờ được rebaseline dù objective đã formally đổi, metric mất ý nghĩa.

Rebaseline phải là governance decision khi planning basis thay đổi đủ lớn, không phải cách che performance xấu.

Một useful pattern là giữ baseline, actual và forecast tách rõ. Khi một stakeholder hỏi “plan là gì?”, cần biết họ đang hỏi commitment đã approve hay current expected outcome.

## Artifact lifecycle: draft → reviewed → approved → effective → superseded → archived

Không phải file mới nhất luôn là file có hiệu lực. Contract amendment có thể signed nhưng effective từ tháng sau; policy draft mới hơn vẫn chưa replace approved version.

Critical artifact nên có lifecycle state và effective date rõ. “Latest modified” khác “authorized current”.

Superseded artifact vẫn có historical value. Xóa version cũ làm mất audit trail và khiến decision cũ khó hiểu.

## Immutable history và audit trail

Một số evidence cần append-only hoặc immutable history: approval, financial transaction, test result, decision record. Không nhất thiết dùng blockchain; principle là không overwrite history tới mức không biết state trước.

Version-control system, signed document repository hoặc audit log có thể cung cấp mechanism. Mục tiêu là reconstruct được ai thay gì, khi nào, vì sao và authority nào.

Audit trail mạnh đặc biệt quan trọng khi exception/compliance decision có consequence cao.

## Change request như một information packet

Change request không chỉ là câu “hãy đổi scope”. Một request tốt nên đủ context để authority ra decision: reason, affected objective, impact lên schedule/cost/risk/quality, option và urgency.

Nếu governance body phải tự tìm lại toàn bộ impact, decision latency tăng. Artifact tốt giảm transaction cost của governance.

Decision packet càng high-impact càng cần evidence về alternative và recommendation, không chỉ one-option request. Nếu request chỉ trình bày solution mong muốn, governance khó biết trade-off thật.

## Evidence package cho gate

Stage gate, go/no-go hoặc regulatory approval thường cần nhiều evidence: requirement status, test result, unresolved risk, operational readiness, contract status và approval.

Một gate package tốt không phải folder chứa mọi file. Nó là curated proof rằng exit criteria đã được đáp ứng hoặc exception đã được authority accept.

Gate theater xảy ra khi meeting vẫn “approve” dù evidence package incomplete vì deadline pressure. Khi đó artifact tồn tại nhưng control objective đã fail.

## Decision log và assumption expiration

Decision log nên ghi không chỉ decision mà còn key assumption. Nếu assumption thay đổi, decision có thể cần review.

Ví dụ “chọn vendor A vì cost thấp nhất và API đáp ứng throughput 1.000 req/s”. Nếu forecast traffic tăng lên 5.000 req/s, decision cũ không sai tại thời điểm đó nhưng basis đã hết hạn.

Điều này giúp organization tránh hai cực: giữ decision cũ quá lâu hoặc blame người cũ bằng information mới.

Một decision record mạnh nên gồm context, options considered, owner/authority, rationale, effective date, affected artifacts và review trigger.

## Decision provenance

Provenance nối decision với evidence và authority. Nếu một scope exception được approve, cần biết request nào, analysis nào, ai approve và điều kiện nào đi kèm.

Provenance khác mere history. History nói event đã xảy ra; provenance giải thích chain tạo ra state hiện tại.

Trong incident hoặc audit, provenance giúp phân biệt unauthorized drift với explicit accepted exception.

## Information radiator và dashboard

Adaptive team thường dùng visual board, burnup/burndown, cumulative flow hoặc release forecast như information radiator. Predictive project dùng milestone/Gantt/EVM/dashboard. Tool khác nhau nhưng problem giống nhau: làm state và deviation visible đủ nhanh.

Burnup cho thấy completed scope và total scope nên nhìn được scope change tốt hơn burndown chỉ hiển thị remaining work. Cumulative flow cho thấy WIP theo state và bottleneck. Metric nên chọn theo question, không theo template.

Dashboard tốt không thay source system. Nó là projection của source data cho một decision audience. Nếu dashboard có số nhưng không thể truy ngược data source, trust giảm khi có dispute.

## Information compression luôn làm mất detail

Status report nén hàng nghìn event thành vài signal. Compression là cần thiết, nhưng người thiết kế report phải biết detail nào bị mất.

Một green milestone có thể che critical risk nếu chỉ nhìn completion. Vì vậy report cần surface exception và confidence, không chỉ aggregate average.

Compression cũng tạo aggregation bias. Average defect rate 2% có thể che một segment high-risk 20%. Report designer cần biết khi nào aggregate cần drill-down.

## Dashboard là view, không phải reality

Dashboard thường dùng cutoff time và transform. Một dashboard 09:00 có thể stale sau incident 10:00. “Green” nghĩa green theo data captured và rule hiện tại, không phải metaphysical truth.

Critical decision nên kiểm tra freshness và underlying evidence, đặc biệt khi state đang thay đổi nhanh.

## Information latency

Information latency là thời gian từ event xảy ra tới khi người có authority nhìn thấy signal usable. Latency dài làm control phản ứng muộn.

Ví dụ defect production xuất hiện hôm nay nhưng quality dashboard update weekly; management có thể tiếp tục rollout sáu ngày dựa trên stale state.

Automation có thể giảm latency, nhưng only if alert threshold và ownership rõ. Alert không ai đọc chỉ chuyển latency từ data layer sang human queue.

## Communication channels formula và giới hạn của nó

Với `n` người nếu mọi cặp có thể giao tiếp trực tiếp, số channel lý thuyết là:

```text
channels = n(n - 1) / 2
```

5 người tạo 10 channel; 10 người tạo 45. Formula giải thích vì sao coordination complexity tăng nhanh khi team lớn. Nhưng nó không có nghĩa mọi channel hoạt động đều như nhau hoặc một project 10 người “phức tạp 4.5 lần” project 5 người. Structure, role và communication design làm giảm interaction cần thiết.

Artifact và protocol chính là cách giảm coordination load. Shared API contract, architecture decision record hoặc acceptance criterion có thể thay hàng chục conversation lặp lại.

## Single source of truth không có nghĩa một tool duy nhất

Một project lớn có thể dùng Jira cho work, Git cho code, CI cho test evidence và ERP cho actual cost. Không cần ép mọi information vào một tool.

“Single source of truth” nên hiểu là mỗi loại fact có authoritative source rõ. Dashboard có thể aggregate nhiều source nhưng không nên tạo competing truth.

Source ownership cũng cần conflict-resolution rule. Nếu ERP và procurement tool khác nhau về committed cost, organization phải biết system nào authoritative cho từng field hoặc cách reconcile.

## Versioning và configuration control

Artifact quan trọng cần biết version nào đang có hiệu lực. Điều này đặc biệt quan trọng với requirement, contract, design, baseline và test evidence.

Nếu team review requirement v3 nhưng vendor implement v2, communication frequency cao cũng không cứu được configuration failure. Configuration management tạo identity và version control cho artifact/deliverable để mọi party làm việc trên cùng state.

Version string chỉ có giá trị nếu mapping tới effective configuration. “v3-final-final2” không phải configuration management.

## Artifact ownership và freshness

Artifact stale nguy hiểm hơn artifact thiếu vì nó tạo confidence giả. Mỗi critical artifact cần source of truth, owner, update trigger và archive/version policy. Nếu risk register chỉ cập nhật trước audit, nó không phải risk-control instrument.

Automation có thể giảm maintenance: CI tạo test evidence, issue tracker sinh status, financial system cập nhật actual cost. Nhưng automation chỉ tốt nếu semantic definition đúng.

Freshness requirement nên phụ thuộc decision cadence. Daily flow board cần cập nhật gần real time; benefits report có thể monthly/quarterly. Không phải artifact nào cũng cần cùng update frequency.

## Freshness SLO cho information

Có thể nghĩ freshness như service level cho information. Critical incident status có thể cần dưới 15 phút; schedule forecast weekly; benefit realization monthly.

Nếu decision cadence nhanh hơn freshness, governance đang lái bằng rear-view mirror. Nếu update cadence quá cao so với decision need, team tạo reporting waste.

Tailoring artifact cadence là matching information half-life với decision cadence.

## Automation boundary và human validation

Automation tốt cho deterministic transform: aggregate actual cost, link build-test evidence, calculate metric. Nhưng semantic exception cần human judgment.

Ví dụ tool có thể auto-close risk khi due date qua là dangerous; due date không chứng minh risk retired. Automation nên reduce clerical work mà không encode false business rule.

Automated artifact cần observable failure. Nếu integration từ ERP sang dashboard fail silently, report có thể stale mà người dùng không biết.

## Access control và information security

Không phải mọi artifact nên mở cho toàn project. Procurement bid, personal data, legal advice hoặc security finding có thể cần access boundary.

Transparency không có nghĩa phá confidentiality. Project information architecture phải cân bằng need-to-know, auditability và collaboration.

Access model cũng ảnh hưởng continuity. Nếu critical artifact nằm trong private account của một contractor, offboarding có thể làm project mất memory. Ownership nên thuộc organizational system khi appropriate.

## Knowledge transfer: artifact không thay conversation hoàn toàn

Tacit knowledge khó capture hoàn toàn bằng document. Handover tốt thường kết hợp artifact với walkthrough, shadowing hoặc joint operation period.

Runbook có thể ghi step, nhưng operator vẫn cần hiểu failure signal và escalation context. Vì vậy knowledge transfer là combination của explicit knowledge và experience transfer.

Teach-back hoặc simulation giúp verify knowledge transfer thay vì chỉ ghi “training completed”.

## Artifact minimization heuristic

Mỗi artifact có carrying cost: create, update, review, reconcile, archive. Vì vậy “có thêm document cho chắc” không luôn tốt.

Trước khi tạo artifact mới, hỏi: information này đã có authoritative source chưa, consumer/decision nào cần view khác, risk của không ghi là gì, và automation/view có đủ thay document mới không.

Nếu hai artifact luôn phải update cùng nhau và không có audience/control khác nhau, chúng có thể đang duplicate truth.

## Artifact anti-patterns

Document theater là tạo artifact để pass audit nhưng không dùng trong work. Duplicate truth xảy ra khi nhiều spreadsheet chứa cùng fact nhưng update khác nhau. Zombie document là file vẫn được link nhưng không còn owner. Dashboard theater là metric đẹp không nối decision. Traceability theater là RTM đầy đủ về hình thức nhưng link không được verify.

Một anti-pattern khác là over-documentation: information được ghi ở quá nhiều nơi đến mức update cost cao hơn value và freshness giảm.

Semantic drift làm cùng metric đổi meaning nhưng report không nói. Lineage break khiến number không trace về source. Gate theater approve dù evidence thiếu. History overwrite xóa state cũ. Automation blindness tin pipeline dù integration đã fail.

## Ví dụ reasoning

Một change request thêm biometric verification được sponsor nói miệng trong meeting. Team dev bắt đầu làm, procurement chưa biết vendor license thay đổi, privacy review chưa được cập nhật và schedule vẫn dùng baseline cũ. Problem không chỉ là “communication kém”. Project đã thiếu artifact transition từ request → impact analysis → approval → baseline/backlog update → compliance evidence.

Một flow tốt làm decision visible và traceable, nhờ đó mỗi domain nhận đúng information tại đúng thời điểm.

Một scenario khác: steering dashboard báo EAC 1.1 tỷ nhưng finance ERP chỉ có actual 600 triệu. Procurement tool cho biết 400 triệu PO đã committed; PM forecast thêm 200 triệu remaining. Nếu dashboard không có lineage, stakeholder có thể tranh luận vì “số không khớp”. Khi semantic contract rõ, ta hiểu EAC = actual/commitment/remaining forecast theo rule, còn ERP actual chỉ là một component.

## Failure modes theo information system

Failure ở capture: event không được ghi. Failure ở semantics: field có meaning khác nhau. Failure ở propagation: source đổi nhưng downstream view không đổi. Failure ở authority: người không có quyền sửa baseline. Failure ở lineage: report không trace về evidence. Failure ở freshness: data đúng nhưng quá cũ. Failure ở access: đúng người không xem được hoặc sai người xem được. Failure ở retention: history bị xóa trước khi audit/learning cần.

Nhìn artifact theo failure mode giúp project manager thiết kế control thực dụng hơn memorizing template.

## Mental model

> Artifact là external memory và evidence architecture của project. Mục tiêu không phải tạo nhiều document mà là giữ được lineage từ source → state → decision → commitment → evidence, với semantics, version, freshness và authority đủ rõ để project có một reality có thể kiểm chứng.

Tiếp theo nên đọc [Quantitative reasoning](./15_quantitative_reasoning_worked_examples.md) để nối data/artifact với các phép tính PMP, hoặc [Case studies](./16_end_to_end_case_studies.md) để thấy nhiều artifact tương tác trong một project.
