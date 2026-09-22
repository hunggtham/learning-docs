# Self-service, multi-tenancy, governance và FinOps

## 1. Self-service là delegated control có boundary

Self-service không nghĩa ai cũng có admin. Nó nghĩa user có thể hoàn thành common task trong một permission envelope đã thiết kế: tạo service, database plan, secret binding hoặc environment mà không chờ operator thao tác.

Platform nhận intent mức cao, validate policy, thực hiện provisioning bằng automation identity và trả status. Đây là delegated control.

## 2. API cần thể hiện intent

Nếu developer muốn “một internal HTTP service” nhưng phải khai VPC ID, subnet, security group, node selector và IAM ARN, platform đang expose implementation.

Intent-level API giảm coupling. Platform có thể đổi underlying implementation mà consumer contract ít thay hơn.

Tuy nhiên intent phải đủ rõ cho reliability/cost. User vẫn có thể cần chọn tier, region, data classification, expected traffic hoặc RPO/RTO.

## 3. Multi-tenancy là shared resource + isolation contract

Nhiều team có thể dùng chung cluster, CI runner, registry hoặc observability backend. Multi-tenancy tiết kiệm và chuẩn hóa nhưng tạo noisy neighbor/security risk.

Isolation có nhiều chiều: identity/RBAC, network, compute quota, storage, secret, observability data và billing attribution. Namespace chỉ giải một phần.

## 4. Quota là product feature

Quota ngăn một tenant tiêu hết shared capacity, nhưng quota quá thấp tạo support ticket. Platform cần default theo workload class và cách request increase có reason/approval tự động phù hợp.

Quota usage phải visible cho tenant trước khi chạm limit. Error “quota exceeded” chỉ khi deploy là feedback quá muộn.

## 5. Resource fairness và noisy neighbor

Shared cluster có thể gặp CPU, memory, I/O, network hoặc API-server contention. Request/limit, priority, rate limit và dedicated pool là các công cụ.

Không phải tenant nào cũng cần isolation vật lý. Chọn boundary dựa trên risk/compliance/performance. Dedicated cluster per team có isolation nhưng tăng cost/operational surface.

## 6. Environment strategy

Dev/staging/prod có thể tách account/project/cluster hoặc chia namespace tùy risk. Production thường cần stronger boundary. Nhưng càng nhiều environment giống hệt production càng tốn cost và drift risk.

Mục tiêu của pre-production là tạo confidence cho change, không phải sao chép mọi thứ vô điều kiện. Ephemeral environment có thể phù hợp feature/integration test; long-lived staging phù hợp shared dependency test.

## 7. Governance bằng metadata

Mọi resource nên có owner, environment, service/product, cost center/team, data classification và lifecycle/expiry khi phù hợp. Metadata cho phép policy, cost allocation và cleanup.

Nếu resource không có owner, incident/security/cost question đều khó. Platform nên inject/require metadata thay vì mong user nhớ tag bằng tay.

## 8. FinOps là feedback loop về cost

Cloud bill chỉ hữu ích khi cost được gắn với owner và driver. “Team A tốn 20 triệu” chưa đủ; cần biết compute idle, data egress, database tier, log ingestion hay storage retention nào gây cost.

FinOps không phải chỉ cắt chi phí. Nó tối ưu trade-off cost–reliability–performance–velocity. Giảm replica làm bill thấp nhưng vi phạm SLO không phải optimization.

## 9. Unit economics kỹ thuật

Metric cost trên request, tenant, build minute, GB processed hoặc active user giúp thấy efficiency khi scale. Tổng bill tăng có thể là hợp lý nếu business volume tăng nhanh hơn.

Platform có thể cung cấp cost estimate trước provisioning và actual cost sau sử dụng để close loop.

## 10. Rightsizing có evidence

CPU request lớn hơn nhiều usage có thể là waste, nhưng p99/peak và failover headroom quan trọng. Rightsizing nên dùng historical distribution, SLO, startup time và autoscaling delay.

Tự động giảm resource ngay theo average có thể tạo incident. Recommendation nên có confidence và staged application.

## 11. Cleanup và ephemeral resource

Preview environment, temporary database và old image tạo cost/leak. Resource tạm nên có TTL/owner mặc định. Cleanup automation phải bảo vệ production bằng classification và explicit retention policy.

“Không ai biết resource này là gì nên không dám xóa” là dấu hiệu metadata/lifecycle design yếu.

## 12. Policy hierarchy

Organization có global policy; platform có default; team có config trong allowed range; workload có runtime state. Conflict resolution phải rõ.

Nếu central policy thay đổi breaking behavior, rollout cần staged/canary. Policy cũng là production code.

## 13. Developer autonomy và guardrail

Autonomy tốt không phải cho mọi người toàn quyền, mà là cho quyền quyết định gần context trong boundary an toàn. Platform encode common constraint; team quyết định business-specific choice.

Khi exception cần nhiều lần, có thể golden path đang thiếu use case chứ không phải user “không tuân thủ”. Platform product discovery phải học từ exception.

## 14. Senior note: shared platform cần economics và reliability cùng lúc

Multi-tenancy tăng utilization nhưng blast radius tăng. Dedicated resource giảm coupling nhưng cost/toil tăng. Quyết định tenancy phải xem workload criticality, compliance, scaling pattern và team maturity.

Không có topology “chuẩn cho mọi công ty”. Có contract rõ và evidence để điều chỉnh mới là maturity.

## 15. Isolation phải được mô tả theo failure và threat model, không theo tên resource

Hai tenant ở hai namespace có thể vẫn chia node kernel, CNI data plane, ingress controller, DNS, API server, registry và observability backend. Vì vậy câu “đã tách namespace” chưa trả lời được tenant A có thể ảnh hưởng tenant B ra sao.

Hãy hỏi theo từng failure class: A có thể ăn hết CPU/memory/I/O không; tạo quá nhiều object có làm API server chậm không; log cardinality có làm observability backend quá tải không; network policy có ngăn data path không; secret/audit/log query có bị đọc chéo tenant không.

Nếu một workload có compliance hoặc hostile-code risk cao, logical isolation có thể không đủ; dedicated node/account/cluster hoặc sandbox boundary mạnh hơn có thể hợp lý dù cost cao hơn.

## 16. Shared control plane là một tài nguyên cần quota riêng

Team thường nhìn CPU/memory workload nhưng quên control-plane resource. Một tenant tạo hàng trăm nghìn object, event, watch hoặc GitOps reconciliation có thể làm API server/controller/etcd pressure tăng dù application request vẫn ít.

Platform nên đặt boundary cho object count, API rate, concurrent reconciliation và automation fan-out khi cần. Multi-tenancy fairness phải bảo vệ cả **control plane** lẫn data plane.

Đây cũng là lý do “mỗi team tự chạy controller tùy ý trong shared cluster” cần governance về permission và load, không chỉ security.

## 17. Quota cần phân biệt hard ceiling và planning signal

Một hard quota bảo vệ shared resource bằng cách từ chối work mới khi chạm giới hạn. Nhưng capacity planning còn cần soft threshold để cảnh báo trước. Nếu tenant chỉ biết vấn đề khi deployment bị reject, feedback đã quá muộn.

Self-service tốt hiển thị current usage, forecast và headroom ngay lúc user chọn tier hoặc scale. Quota increase có thể tự động khi nằm trong policy và capacity còn đủ; chỉ exception lớn mới cần human decision.

Quota cũng phải xét failure mode. Nếu production chạy bình thường ở 80% quota nhưng failover cần gấp đôi replica, quota hiện tại có thể chặn chính recovery path.

## 18. Showback và chargeback tạo incentive khác nhau

Showback cho team thấy chi phí họ tạo nhưng chưa chuyển chi phí đó vào ngân sách trực tiếp. Chargeback phân bổ cost thật về đơn vị sử dụng. Cả hai đều là feedback mechanism; không phải tổ chức nào cũng cần chargeback cứng.

Nếu cost allocation thiếu shared-cost model, team có thể tối ưu cục bộ nhưng platform bill vẫn lớn. Shared ingress, observability, cluster control plane và network backbone cần cách phân bổ minh bạch: theo usage driver, tỷ lệ cố định hoặc coi là central investment tùy mục tiêu.

Mục tiêu là tạo quyết định tốt hơn, không phải làm hóa đơn nội bộ đẹp hơn.

## 19. Unit cost chỉ hữu ích khi denominator có nghĩa

`cost/request` giảm có thể vì workload hiệu quả hơn, nhưng cũng có thể vì traffic bot/cache-hit rẻ tăng mạnh. `cost/user` có thể méo nếu user activity rất khác nhau.

Do đó unit economics cần chọn denominator gần value/work thực: completed order, GB processed, successful build, active tenant hoặc business transaction. Phải giữ quality guardrail như SLO/error rate; nếu giảm cost bằng cách reject nhiều request, unit cost của request thành công có thể nhìn đẹp giả tạo.

Senior FinOps luôn hỏi numerator và denominator đã thay đổi vì architecture, price hay traffic mix.

## 20. Commitment/discount không sửa được resource waste

Reserved capacity, savings plan hoặc volume discount có thể giảm đơn giá nhưng không loại bỏ idle architecture. Nếu commit dựa trên peak ngắn hạn rồi demand giảm, tổ chức chỉ chuyển waste thành hợp đồng dài hạn.

Thứ tự reasoning tốt là hiểu baseline/seasonality, rightsizing và architecture trước, sau đó mới quyết định phần usage ổn định nào đáng commit. Discount strategy là financial optimization trên workload đã hiểu, không thay thế engineering optimization.

## 21. Cost anomaly phải nối lại change telemetry

Một bill tăng đột ngột thường có causal event: release bật debug log, retry storm tăng egress, retention policy đổi, preview environment không cleanup hoặc autoscaler stuck.

Cost monitoring có giá trị hơn khi có dimension owner/service/environment và deployment/config event. Khi daily log cost tăng 4 lần sau release R, operator có thể drill từ FinOps signal sang telemetry/release thay vì chờ cuối tháng.

Cost vì vậy cũng là observability signal của platform.

## 22. Self-service deletion cần mạnh như self-service creation

Platform thường tối ưu “Create” nhưng lifecycle thật còn resize, rotate, migrate, suspend và delete. Nếu tạo database mất 5 phút nhưng xóa cần ticket hai tuần, resource leak là hệ quả thiết kế chứ không phải user lười.

Deletion cần safety: dependency discovery, retention/backup policy, grace period hoặc approval theo criticality. Nhưng common ephemeral resource nên có TTL và cleanup path mặc định.

Day-2 operation mới quyết định platform có thật sự self-service hay chỉ là provisioning portal.

## 23. Senior walkthrough: shared cluster rẻ hơn nhưng một team làm toàn platform chậm

Giả sử team analytics tạo hàng chục nghìn short-lived Job mỗi giờ. CPU application vẫn còn headroom nhưng API server latency, scheduler queue và event volume tăng; các team khác thấy deployment chậm và HPA update trễ.

Nếu chỉ nhìn namespace CPU quota, tenant analytics “không vi phạm”. Failure nằm ở shared control-plane resource chưa được accounting.

Mitigation có thể rate-limit creation, batch work, tách workload class sang cluster/pool riêng hoặc tăng control-plane capacity. Long-term contract cần quota theo object/API behavior và SLO platform. Đây là lý do multi-tenancy economics phải tính externality, không chỉ utilization compute.

## 24. Fairness khác với quota: ai được phục vụ khi resource khan hiếm?

Quota trả lời tenant có thể sở hữu tối đa bao nhiêu resource; fairness trả lời khi nhiều tenant cùng tranh resource tại một thời điểm thì scheduler/queue phân phối ra sao. Hai tenant đều ở dưới quota vẫn có thể gây starvation nếu một tenant luôn submit work trước hoặc giữ connection lâu.

Shared CI runner, deployment queue, API server và database proxy đều cần fairness model. Có thể dùng weighted queue, priority class, per-tenant concurrency hoặc reservation. Không có một thuật toán universal; contract phải phản ánh business criticality mà vẫn tránh tenant priority cao chiếm mọi capacity vô thời hạn.

Fairness metric nên nhìn wait time/service rate theo tenant hoặc workload class, không chỉ aggregate throughput. Aggregate 10.000 job/giờ có thể che việc một team chờ 40 phút còn team khác gần như không chờ.

## 25. Isolation level nên được chọn theo blast-radius budget

Thay vì hỏi “shared hay dedicated?”, hãy hỏi organization chấp nhận một failure ảnh hưởng tối đa bao nhiêu workload/tenant. Từ đó mới chọn cell, account, cluster, node pool, ingress hay observability partition phù hợp.

Ví dụ workload Tier-0 có thể cần cell riêng vì một policy rollout hoặc noisy tenant không được ảnh hưởng nó; workload internal low-criticality có thể share mạnh hơn để tăng utilization. Isolation là một reliability/economic tier, không chỉ security option.

Platform catalog có thể encode `isolationClass` hoặc `criticalityTier` ở mức intent. User không cần chọn raw topology, nhưng contract phải nói blast radius và support expectation tương ứng.

## 26. Tenant-aware SLO ngăn aggregate metric che unfairness

Một shared platform có thể đạt 99.9% aggregate success nhưng một tenant nhỏ bị lỗi 20% nếu traffic tenant lớn thống trị denominator. Vì vậy ngoài global SLO, cần slice theo tenant class, region hoặc critical journey khi đó là boundary product quan trọng.

Không nên tạo SLO riêng cho hàng nghìn tenant nếu operational cost quá lớn; có thể dùng cohort/tier hoặc fairness guardrail. Mục tiêu là phát hiện systematic isolation failure mà aggregate metric che mất.

Đây cũng áp dụng cho provisioning latency: median toàn platform thấp không có ý nghĩa nếu một account/region luôn bị queue starvation.

## 27. Recovery capacity là một shared resource cần reservation

Trong incident, nhiều tenant có thể cùng cần scale, recreate pod, restore database hoặc pull image. Nếu platform chỉ capacity cho steady state, recovery fan-out có thể làm registry, API server, node provisioning hoặc backup service saturation đúng lúc cần nhất.

Capacity planning multi-tenant nên có **recovery concurrency budget**: bao nhiêu workload có thể restart/reconcile/restore đồng thời mà control plane và dependency vẫn giữ SLO. Game day nên test burst recovery, không chỉ normal traffic.

Điều này giải thích vì sao overcommit quá mạnh hoặc quota “vừa đủ ngày thường” có thể biến một failure nhỏ thành recovery storm.

## 28. Cost allocation phải tính externality chứ không chỉ resource sở hữu trực tiếp

Một tenant có thể dùng ít CPU nhưng tạo log cardinality cực cao, egress lớn, API request storm hoặc nhiều short-lived object khiến shared service phải scale. Nếu chargeback chỉ dựa trên CPU/RAM, incentive bị lệch.

Không nhất thiết billing phải chính xác tuyệt đối từng byte. Quan trọng là chọn driver đủ gần causal cost: ingestion GB, retained GB-day, egress, build minute, object/API volume hoặc dedicated capacity reservation.

Khi externality không được visible, team gây cost có ít feedback để tối ưu còn central platform phải hấp thụ bill và toil.

## 29. Idle capacity không luôn là waste nếu nó mua được option value

Capacity chưa dùng có thể là headroom cho failover, rollout, incident recovery hoặc seasonal spike. FinOps nhìn utilization thấp rồi cắt toàn bộ spare capacity có thể phá reliability contract.

Cần phân biệt **unowned idle** — resource thừa do request sai hoặc lifecycle leak — với **intentional reserve** — capacity được giữ vì failure model/SLO. Metadata và capacity model nên làm reserve explicit để cost review không nhầm nó với waste.

Senior discussion về cost nên hỏi “resource này mua capability gì?” thay vì “tại sao utilization không 90%?”.

## 30. Governance tốt cần lifecycle cho chính policy và exception

Policy có owner, version, rollout ring, telemetry, deprecation và rollback giống software. Exception cũng là resource: có requester, reason, scope, expiry, reviewer và evidence cho việc gia hạn.

Nếu exception không bao giờ hết hạn, policy dần trở thành nominal. Nếu policy không có migration path, platform tạo shadow workflow và bypass. Governance trưởng thành tối ưu **risk reduction trên flow**, không tối đa số rule.

Một signal tốt là exception rate theo policy. Nếu một rule liên tục cần exception hợp lệ, rule hoặc golden path có thể đang model sai thực tế và cần product discovery lại.

## 31. Reservation và borrowing cần reclamation semantics

Shared platform thường muốn vừa bảo đảm capacity cho workload critical vừa cho workload khác mượn phần đang rảnh để tăng utilization. Borrowing có ích, nhưng nếu không có reclamation contract thì “capacity dự phòng” chỉ tồn tại trên giấy: khi Tier-0 cần scale, batch job đang mượn resource có thể không nhả đủ nhanh.

Contract cần nói resource nào reserved, ai được borrow, khi nào bị reclaim, workload bị preempt có checkpoint/resume được không và thời gian thu hồi có phù hợp RTO không. Một batch job mất 20 phút để shutdown không phải spare capacity hữu ích cho failover cần 2 phút.

Vì vậy headroom phải đo ở **recoverable capacity**, không chỉ free capacity. Game day nên chứng minh borrowed resource thực sự có thể được reclaim trong deadline.

## 32. Preemption là policy về ai chịu thiệt khi scarcity xảy ra

Priority class chỉ có ý nghĩa khi organization chấp nhận workload thấp hơn bị delay/evict để bảo vệ workload cao hơn. Nếu mọi workload đều gắn priority cao nhất, policy mất tác dụng. Nếu preemption giết stateful/batch work không checkpoint, recovery cost có thể lớn hơn lợi ích.

Thiết kế priority cần nối business criticality với failure semantics: request-serving Tier-0 có thể giữ reserved concurrency; batch low-priority có thể pause; background cleanup có thể shed; security/recovery control work có thể cần lane riêng. Sau preemption phải có retry/backoff để tránh tất cả workload thấp cùng quay lại tạo thundering herd.

Scarcity policy tốt trả lời trước incident: **ai được phục vụ, ai chờ, ai bị hủy, và trạng thái của work bị hủy được phục hồi thế nào**.

## 33. Isolation mạnh hơn làm giảm pooling efficiency và tăng fragmentation

Tách tenant thành nhiều cluster/cell/account giảm blast radius nhưng capacity không còn pooling hoàn toàn. Mỗi cell phải giữ headroom riêng, workload nhỏ có thể không tận dụng hết node/database tier và operator phải duy trì nhiều control plane hơn.

Đây là trade-off cấu trúc, không phải lý do tránh isolation. Quyết định đúng cần so `blast-radius reduction + compliance + predictable performance` với `fragmentation + duplicated reserve + operational surface`. Một Tier-0 có thể đáng trả cost đó; hàng trăm workload dev nhỏ có thể không.

FinOps vì vậy phải hiểu topology. So đơn giá CPU giữa shared và dedicated mà bỏ qua failure budget/support burden sẽ cho kết luận sai.

## 34. Tenant isolation cần kiểm tra cả recovery path và operator path

Hai tenant có thể được tách tốt ở steady state nhưng dùng chung break-glass admin, restore bucket, registry mirror hoặc recovery queue. Khi incident, operator dùng quyền rộng hoặc restore nhiều tenant qua cùng pipeline có thể phá boundary vốn tồn tại lúc bình thường.

Threat/failure model nên hỏi cả Day-2: backup của tenant A có thể restore nhầm sang tenant B không; support engineer có thể query log chéo tenant không; emergency tool có audit/target confirmation không; bulk recovery của A có starve B không.

Isolation trưởng thành là property của toàn lifecycle `create → run → observe → recover → delete`, không chỉ namespace/network policy lúc workload đang khỏe.