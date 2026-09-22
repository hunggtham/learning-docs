# CI/CD: biến thay đổi thành flow có bằng chứng

## 1. Continuous Integration là giảm integration risk

Continuous Integration (CI / 지속적 통합) không đồng nghĩa với “có server chạy test”. Bản chất là tích hợp thay đổi nhỏ vào nhánh chính thường xuyên và nhận feedback tự động đủ nhanh để lỗi integration không tích tụ.

Nếu branch sống hai tuần rồi mới merge nhưng có Jenkins chạy mỗi commit, hệ thống có automation nhưng feedback integration vẫn muộn. Nếu test mất sáu giờ và thường flaky, developer có xu hướng bỏ qua signal. Do đó CI là thiết kế feedback loop, không chỉ YAML pipeline.

## 2. Pipeline phải trả lời câu hỏi theo tầng

Một pipeline tốt tổ chức check từ rẻ/nhanh đến đắt/chậm, nhưng không biến pipeline thành một chuỗi tuần tự dài vô lý. Lint/static check cho feedback nhanh. Unit test kiểm tra logic cục bộ. Integration/contract test kiểm tra boundary. Security/supply-chain checks xác minh policy. Build tạo artifact. Một số stage có thể chạy song song nếu dependency cho phép.

Điểm quan trọng là mỗi stage phải có failure semantics rõ. “Pipeline đỏ” nhưng không biết check nào đáng tin, ai sở hữu, có retry được không sẽ tạo alert fatigue giống production monitoring.

## 3. Flaky test là reliability debt

Test lúc pass lúc fail mà source không đổi làm pipeline mất vai trò oracle. Team bắt đầu rerun đến khi xanh và CI trở thành nghi thức. Flaky test cần được đo, quarantine có kiểm soát và sửa có owner. Không nên giữ build đỏ vô hạn, nhưng cũng không được coi rerun là remediation.

Một senior practice là theo dõi false positive/false negative của validation system. Pipeline cũng là production system phục vụ developer; nó có SLO về thời gian, availability và signal quality.

## 4. Continuous Delivery khác Continuous Deployment

Continuous Delivery nghĩa mainline luôn ở trạng thái có thể phát hành thông qua process tự động đáng tin. Continuous Deployment đi thêm một bước: thay đổi đạt policy sẽ tự động vào production mà không cần quyết định thủ công cho từng release.

Tổ chức có thể chọn delivery mà không deployment tự động vì regulation hoặc risk model. Điều quan trọng là approval nếu có phải nằm đúng nơi: xác nhận business/risk decision, không phải bù cho pipeline thiếu test.

## 5. Environment promotion

Một anti-pattern là mỗi môi trường build lại source. Confidence tốt hơn khi build một lần và promote cùng artifact. Environment khác nhau chủ yếu qua config, credential, capacity và external integration.

Promotion cần evidence. Ví dụ artifact A qua integration test, deploy staging, chạy smoke/e2e, rồi mới đủ điều kiện production. Evidence có thể được lưu cùng release metadata. Khi production incident, ta cần biết chính xác artifact, config, migration và deployment event nào vừa xảy ra.

## 6. Deployment không kết thúc khi API trả thành công

Một deployment command thành công chỉ chứng minh control plane chấp nhận desired state. Safe delivery cần xác minh actual behavior sau rollout. Có thể workload chưa ready, traffic error tăng hoặc dependency saturation xuất hiện sau vài phút.

Deployment verification nên dùng production signal liên quan user impact. Canary, blue-green, rolling update và feature flag là các mechanism giảm blast radius. Theory và trade-off đã có canonical chapter [deployment safety, canary, blue-green, flags và rollback](../../computer_science/09_software_engineering/advanced/05_deployment_safety_canary_blue_green_flags_and_rollback.md).

DevOps layer phải nối mechanism đó vào pipeline/controller để promotion dựa trên evidence chứ không dựa vào “deploy command exited 0”.

## 7. Rollback không luôn là inverse

Nếu release chỉ thay stateless code tương thích, rollback image có thể dễ. Nhưng nếu release đã migrate database schema, publish event theo schema mới hoặc gọi external side effect, rollback code có thể làm tình hình tệ hơn.

Safe change cần backward/forward compatibility. Database migration thường nên theo expand-and-contract: thêm capability tương thích trước, chuyển traffic/code, sau đó mới bỏ cấu trúc cũ khi chắc chắn không còn consumer. Khi state đã biến đổi không thể đảo, roll-forward có thể an toàn hơn rollback.

## 8. Feature flag tách deploy khỏi release

Deploy là đưa code vào environment. Release là làm behavior mới có hiệu lực với user. Feature flag cho phép hai thời điểm khác nhau. Điều này giảm blast radius và cho progressive exposure, nhưng flag tạo state và complexity riêng.

Flag cần owner, expiry và cleanup. Flag tồn tại nhiều tháng có thể tạo combinatorial behavior mà test không bao phủ. Platform nên hỗ trợ lifecycle chứ không chỉ cung cấp SDK.

## 9. Change metadata là telemetry

Mỗi deployment nên phát event có service, artifact version, commit, environment, actor/automation, thời gian và result. Khi dashboard latency tăng lúc 14:03, operator phải dễ overlay deployment event để thấy correlation. Không có change telemetry, investigation thường bắt đầu bằng câu “có ai vừa deploy gì không?”.

## 10. Pipeline security boundary

CI thường có quyền đọc source, token registry, cloud credential hoặc deploy permission. Vì vậy runner và workflow là security boundary. Pull request từ code chưa tin cậy không nên tự động nhận production secret. Dependency action/plugin phải được pin và kiểm soát. Least privilege nên áp dụng cho job identity theo stage.

## 11. Ví dụ reasoning một release

Giả sử `orders-api` thay logic tính phí. CI xác minh unit/contract test rồi build image digest D. D được scan và publish một lần. Staging deploy D với config staging. Smoke test và contract với dependency pass. Production rollout bắt đầu 5% traffic, theo dõi error rate, latency và business invariant. Nếu signal xấu, controller dừng promotion; rollback hoặc disable feature tùy state compatibility.

Điểm cốt lõi không nằm ở Jenkins/GitHub Actions/Argo Rollouts. Nó nằm ở identity của artifact, staged evidence, blast-radius control và recovery path.

## 12. Senior note: tối ưu lead time bằng giảm queue, không bỏ evidence

Khi pipeline chậm, phản xạ nguy hiểm là bỏ test. Trước tiên tìm critical path: setup dependency, duplicate build, serialized job, scarce runner, flaky rerun hay test suite không partition. Tối ưu feedback time bằng cache đúng, parallelism, test selection và architecture tốt hơn.

Delivery performance cao và reliability không phải hai mục tiêu đối nghịch nếu hệ thống được thiết kế để thay đổi nhỏ, feedback nhanh và rollback/risk boundary rõ.

## 13. Pipeline là DAG có critical path, không phải một danh sách stage

Một pipeline có thể có 30 job nhưng lead time chủ yếu do chuỗi dependency dài nhất quyết định. Hai job 20 phút chạy song song chỉ thêm khoảng 20 phút vào critical path, còn chạy tuần tự thành 40 phút.

Vì vậy tối ưu pipeline nên vẽ dependency DAG: job nào thật sự cần output của job trước, job nào có thể chạy song song, job nào rebuild cùng artifact và job nào chỉ chờ scarce runner. Việc đổi tên stage hoặc tăng runner không giúp nếu critical path nằm ở integration environment mất 40 phút provision.

Pipeline design tốt tách **feedback fast path** cho developer khỏi **evidence deep path** nhưng vẫn giữ policy release. Ví dụ lint/unit/security static chạy sớm; integration suite nặng có thể parallel và promotion chỉ chờ đúng evidence cần thiết.

## 14. Validation có thể stale khi base thay đổi

Một pull request pass toàn bộ test trên commit X + base B. Trong lúc chờ merge, base có thêm change C. Nếu merge tạo state X+C nhưng pipeline không revalidate combination đó, “PR xanh” không chứng minh mainline mới xanh.

Đây là integration race. Cách xử lý có thể là merge queue, rebase/merge-latest-base rồi test lại, hoặc post-merge verification nhanh tùy repository risk. Mental model quan trọng: **evidence phải gắn với exact revision/composition được release**, không chỉ với branch từng xanh.

IaC/GitOps cũng có stale-plan problem tương tự; đây là pattern chung của concurrent change.

## 15. Deploy concurrency phải có ownership theo environment/service

Hai pipeline cùng deploy một service/environment có thể race. Release A bắt đầu canary, release B tới sau thay desired state; metric của A và B trộn lẫn làm verification không còn nghĩa.

Platform nên có concurrency policy: serialize production rollout theo service, cancel superseded run khi safe, hoặc dùng release controller có state machine rõ. “Pipeline job chạy song song nhanh hơn” không áp dụng cho mutation cùng một ownership boundary.

Nếu release B phụ thuộc A, explicit dependency/version tốt hơn để race ngẫu nhiên quyết định order.

## 16. Migration nên được coi là một release contract riêng

Database/schema/message migration có lifecycle dài hơn process deploy. Expand-and-contract thường gồm ít nhất: thêm schema mới tương thích, deploy producer/consumer hiểu cả hai, migrate/backfill data nếu cần, verify usage, rồi mới remove old path.

Pipeline không nên coi migration thành một shell command chạy trước deploy mà không có idempotency, lock/ownership và resume semantics. Migration failure giữa chừng có thể để state partial; rerun phải an toàn hoặc có recovery plan.

Change metadata nên lưu migration version/trạng thái cùng artifact/config để incident biết code nào tương thích data state nào.

## 17. Canary cần guardrail chống false confidence

Canary 1% traffic chỉ có giá trị nếu sample chạm workload đại diện. Rare tenant, write path, batch job hoặc region nhỏ có thể không xuất hiện. Metric aggregate toàn fleet cũng có thể che canary failure vì 1% signal bị 99% stable traffic pha loãng.

Verification nên dimension theo version/canary cohort và chọn business/technical invariant phù hợp. Một canary healthy 10 phút không chứng minh memory leak xảy ra sau 6 giờ; observation window phải phù hợp failure class.

Canary là cách giảm blast radius và tăng evidence, không phải chứng minh tuyệt đối release an toàn.

## 18. Rollback decision cần compatibility matrix

Trước production release, team nên biết ít nhất bốn lớp có thể rollback độc lập đến đâu: application artifact, configuration, database/schema/data và external protocol/event contract.

Có thể biểu diễn mental model:

```text
code N+1 ↔ config C2 ↔ schema S2 ↔ event/API E2
```

Rollback code về N chỉ an toàn nếu N còn hiểu C2/S2/E2 hoặc các lớp kia cũng có recovery path tương thích. Nếu schema S2 đã drop column N cần, rollback image nhanh sẽ fail ngay.

Senior delivery review không chỉ hỏi “có nút rollback không?” mà hỏi “rollback target có còn compatible với actual state sau release không?”.

## 19. Pipeline SLO và error budget cũng áp dụng cho developer experience

Nếu CI availability thấp hoặc p95 feedback 50 phút, developer batch change lớn hơn và rerun nhiều hơn, làm integration risk tăng. Pipeline là shared production system có downstream impact lên delivery behavior.

Platform team có thể đo queue time, execution time, flaky rerun rate, runner saturation và failure do platform vs source. Mục tiêu không phải pipeline luôn xanh; source bug phải làm đỏ. Mục tiêu là **signal đúng, nhanh và đáng tin** để developer không học thói quen bypass.

## 20. Superseded work nên được hủy khi evidence của nó không còn giá trị

Developer push commit B sau commit A nhưng pipeline A vẫn chiếm runner 40 phút. Nếu kết quả A không còn được dùng để merge/release, tiếp tục chạy chỉ làm tăng queue cho evidence mới hơn. Tuy nhiên không phải job nào cũng cancel an toàn; migration/test environment có side effect cần cleanup.

Pipeline nên phân biệt work **pure verification** có thể cancel với work **mutation** cần state machine/cleanup. Cancel-on-new-commit cho lint/unit thường hợp lý; cancel một production deployment giữa migration cần semantics rõ.

Đây là queue discipline: giảm WIP không phải bằng bỏ test mà bằng ngừng tiêu capacity cho evidence đã stale.

## 21. Approval cũng có thể stale

Một người approve release khi evidence gắn với artifact D và config C. Sau đó pipeline rerun build tạo D2 hoặc config thay C2 nhưng approval cũ vẫn được reuse. Khi đó approval không còn xác nhận subject thực sự được deploy.

Manual gate chỉ có ý nghĩa nếu nó bind tới exact release subject: artifact digest, config/revision, migration state và risk context liên quan. Nếu subject đổi đáng kể, approval/evidence cần được đánh giá lại theo policy.

Điều này giống cryptographic attestation ở cấp quy trình: statement “tôi chấp nhận risk” phải nói rõ chấp nhận **cái gì**.

## 22. Shared integration environment là nguồn nondeterminism và coupling

Hai pipeline dùng cùng database/test tenant có thể ảnh hưởng nhau: test A xóa data test B, schema migration race, rate limit chung hoặc background job chạy chéo. Kết quả flaky không nhất thiết do test code mà do environment không có isolation contract.

Có ba chiến lược chính: environment per change, shared environment nhưng namespace/data isolation mạnh, hoặc serialize class test có conflict. Mỗi lựa chọn đổi cost, fidelity và feedback time.

Không cần mọi PR có full production clone. Nhưng test signal phải biết dependency nào shared và failure do environment phải được phân biệt với failure của source change.

## 23. Release controller cần trạng thái `paused`, không chỉ pass/fail

Trong progressive delivery, signal có thể chưa đủ rõ để promote cũng chưa đủ xấu để rollback. Nếu state machine chỉ có “continue” hoặc “fail”, operator dễ chọn action vội.

`Paused` cho phép giữ cohort hiện tại, thu thêm evidence hoặc điều tra dependency mà không tăng blast radius. Tuy nhiên pause có cost: hai version cùng tồn tại lâu hơn, schema/config compatibility window kéo dài và capacity surge tiếp tục bị giữ.

Do đó release state cần timeout/owner: ai quyết định tiếp, evidence nào cần thêm và sau bao lâu phải rollback/roll-forward. “Để canary treo” không phải strategy.

## 24. Health verification cần phân biệt release fault với platform/dependency fault

Nếu canary error tăng đúng lúc external payment provider outage toàn fleet, tự động rollback canary có thể không cải thiện gì và còn tạo thêm churn. Ngược lại aggregate fleet error có thể che lỗi chỉ ở canary.

Verification tốt dùng comparative/cohort reasoning: canary vs baseline trong cùng region/tenant/dependency window, kết hợp absolute SLO guardrail. Nếu cả old và new cùng xấu, suspect shared dependency/platform; nếu new xấu riêng, evidence cho release fault mạnh hơn.

Automation vẫn có thể chọn conservative stop, nhưng reason phải observable để operator biết rollback dự kiến tác động gì.

## 25. Merge queue là một controller cho integration concurrency

Khi nhiều PR cùng xanh trên base cũ, merge queue tạo candidate composition gần state sẽ vào main rồi verify theo thứ tự. Nó không “làm test tốt hơn”; nó quản concurrency và freshness của evidence.

Queue cũng có throughput/capacity. Nếu test lâu và arrival rate PR cao hơn merge service rate, wait time tăng. Tối ưu cần giảm critical path, tăng parallelism an toàn hoặc giảm batch size; bypass queue khi đông chỉ chuyển queue từ CI sang broken mainline.

Đây là cùng mental model với production admission control: khi resource verification hữu hạn, cần policy chọn work nào được vào và bằng chứng nào còn fresh.

## 26. Senior walkthrough: release được approve nhưng deploy artifact khác

Giả sử artifact D1 pass staging và được approve. Sau approval, pipeline dùng lệnh build lại trước production, tạo D2 vì base image đã đổi. Production incident xảy ra và audit log chỉ ghi commit giống nhau.

Lỗi cấu trúc là gate bind tới source commit thay vì immutable artifact subject. Correct flow là build/publish D1 một lần, gắn evidence/approval vào D1 rồi promote chính digest đó. Nếu buộc rebuild, D2 phải được coi release subject mới và validation tương ứng phải chạy lại.

Bài học là CI/CD maturity phụ thuộc **evidence identity + freshness + ownership**, không phụ thuộc số stage hay số nút approval.

## 27. Online schema change phải xét lock, rewrite và runtime cost chứ không chỉ DDL hợp lệ

Một migration có thể đúng về cú pháp nhưng nguy hiểm về vận hành. `ALTER TABLE` tùy database/version có thể lấy lock mạnh, rewrite lượng dữ liệu lớn, tăng WAL/replication lag hoặc giữ transaction lâu. Vì vậy câu hỏi production không phải chỉ là “migration chạy được không?” mà là “nó tranh resource gì, trong bao lâu và failure giữa chừng để lại state nào?”.

Pipeline nên tách validation schema khỏi execution risk. Với bảng lớn, cần estimate row/data volume, lock behavior, replication headroom và maintenance/retry semantics; có thể dùng online migration mechanism hoặc chia thay đổi thành nhiều phase. Database internals cụ thể thuộc canonical Data & Databases, nhưng delivery contract phải nhìn thấy operational consequence.

Một migration chạy tốt trên staging nhỏ không chứng minh production an toàn nếu cost tăng theo data size. Evidence phải đại diện volume và concurrency thực tế hoặc có model đủ bảo thủ.

## 28. Backfill là một workload production cần throttle, checkpoint và invariant

Sau khi thêm field/schema mới, backfill hàng triệu record thường kéo dài lâu hơn deploy application. Nếu chạy tối đa tốc độ, backfill có thể chiếm I/O, connection và lock budget của traffic user. Nếu dừng giữa chừng mà không có checkpoint, rerun có thể làm duplicate side effect hoặc phải quét lại toàn bộ.

Backfill trưởng thành có stable progress identity, chunk/checkpoint, rate/concurrency limit, resume semantics và metric về remaining work/error. Quan trọng hơn, phải định nghĩa invariant trong giai đoạn mixed state: record cũ chưa migrate được đọc thế nào, record mới được ghi theo schema nào, và khi nào có thể tuyên bố old representation không còn cần.

Deployment controller không nhất thiết chạy backfill trực tiếp, nhưng release state phải biết dependency này. Không được contract/drop old field chỉ vì application N+1 đã deploy 100% nếu data migration vẫn chưa converge.

## 29. Dual-write tạo cửa sổ inconsistency cần reconciliation chứ không chỉ test happy path

Một migration có thể tạm thời ghi cả old store và new store. Hai write không atomic qua hai hệ thống nên có thể xảy ra `old success/new fail`, `new success/old fail`, timeout không biết side effect nào đã commit hoặc retry tạo duplicate. Vì vậy dual-write là distributed consistency problem, không phải shortcut miễn phí.

Nếu buộc dùng dual-write, cần xác định source of truth trong từng phase, idempotency key, retry/compensation, discrepancy detector và reconciliation job. Read path cũng cần strategy: đọc old, đọc new, shadow compare hay fallback; mỗi lựa chọn tạo evidence khác nhau.

Cutover chỉ nên xảy ra khi mismatch rate, lag và unresolved discrepancy nằm trong threshold đã định nghĩa. Sau cutover vẫn nên giữ compatibility window trước khi xóa old path để rollback/forensic còn khả thi.

## 30. Contract evolution phải theo consumer lag, không theo producer deploy success

API/event/schema producer có thể deploy version mới trong vài phút nhưng consumer nâng chậm hàng tuần. Nếu producer ngừng phát field/event cũ ngay sau khi chính nó xanh, hidden consumer có thể vỡ mà release dashboard producer vẫn healthy.

Compatibility window cần dựa trên inventory/telemetry của consumer thực: version nào đang đọc, consumer nào offline/batch theo lịch, replay có thể đọc event cũ bao lâu và retention kéo dài thế nào. Với event log, một consumer mới restart từ offset cũ có thể gặp schema lịch sử dù live traffic đã chuyển hết.

Mental model release vì vậy là `producer capability → coexistence → consumer adoption → evidence không còn old dependency → contract removal`. “Deploy xong producer” chỉ là đầu migration, không phải điểm kết thúc.