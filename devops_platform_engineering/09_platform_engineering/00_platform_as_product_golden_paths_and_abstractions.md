# Platform Engineering: platform as product, golden path và abstraction

## 1. Vì sao platform xuất hiện sau DevOps

DevOps khuyến khích team sở hữu delivery và production outcome. Khi tổ chức có nhiều team, mỗi team tự giải cùng bài toán CI, container, observability, secrets và cloud thì cognitive load tăng. Platform Engineering tạo một product nội bộ để tái sử dụng capability mà không quay lại mô hình ticket queue cũ.

Mục tiêu không phải lấy việc của developer, mà làm self-service an toàn.

## 2. Platform là product có user

Một platform phải biết user persona: backend developer, data engineer, mobile backend team hay operator. Mỗi persona có job-to-be-done khác nhau.

“Developer cần namespace Kubernetes” có thể chỉ là implementation-level request. Job thật có thể là “cần một HTTP service private có database, metrics và deploy pipeline”. Platform nên thiết kế interface theo capability gần job, không theo resource catalog nội bộ.

## 3. Golden path là đường tối ưu cho common case

Golden path bundle decision đã được tổ chức hiểu rõ. Ví dụ service chuẩn có repository template, build, artifact registry, deployment, identity, secret integration, SLO dashboard và ownership metadata.

Golden path nên opinionated đủ để giảm decision fatigue. Nếu generator hỏi 80 câu cloud/Kubernetes, platform chưa giảm cognitive load.

Nhưng golden path không nên khóa use case đặc biệt. Escape hatch cần có, kèm explicit ownership và risk.

## 4. Abstraction phải che complexity accidental, không che physics

Developer không cần biết CNI implementation để deploy service bình thường. Nhưng họ vẫn cần hiểu timeout, resource request, retry và data durability vì đó là property của system chứ không phải chi tiết platform.

Abstraction tốt ẩn implementation nhưng giữ concept quan trọng. “Database plan: small/medium/large” có thể che IOPS detail cho common case, nhưng phải expose backup class, HA, RPO/RTO và connection constraints nếu chúng ảnh hưởng application.

## 5. Interface của platform có nhiều dạng

Internal Developer Portal (IDP portal) chỉ là một interface. Platform có thể expose CLI, API, Git repository schema, CRD, Terraform module và documentation. Portal đẹp không bù được backend capability yếu.

Interface nên composable và automation-friendly. Nếu portal là con đường duy nhất và không có API/declarative source, bulk operation và GitOps integration khó.

## 6. Service catalog là ownership graph

Catalog có giá trị khi nối service với owner, repository, runtime, dependencies, on-call, SLO và docs. Chỉ liệt kê hàng nghìn service name không giúp incident.

Catalog nên được cập nhật từ source of truth tự động càng nhiều càng tốt. Metadata manual thường stale.

## 7. Platform capability nên có contract/version

Template và module thay đổi theo thời gian. Nếu platform update Terraform module/Kubernetes abstraction phá hàng trăm service, platform là dependency production nên cần semantic/version/evolution strategy.

Deprecation cần timeline, migration tooling và visibility ai đang dùng version cũ. Platform không thể nói “developer tự update” nếu abstraction vốn được tạo để giảm workload đó.

## 8. Paved road và escape hatch

Use case phổ biến đi paved road với support/SLO tốt. Use case khác có thể tự quản nhưng phải đáp ứng minimum governance. Điều này tránh hai cực: central platform kiểm soát mọi thứ, hoặc platform bị bỏ qua vì không fit ai.

Escape hatch nên explicit, không phải undocumented workaround.

## 9. Product discovery cho platform

Platform backlog không nên chỉ đến từ tool team muốn thử. Quan sát developer journey: thời gian tạo service mới, bước phải mở ticket, loại incident lặp lại, pipeline wait, secret rotation pain, local-to-prod gap.

Ưu tiên capability loại bỏ toil/cognitive load có tần suất và impact cao.

## 10. Đo platform outcome

Vanity metric như số cluster, số template hoặc số API endpoint không phản ánh value. Có thể đo time-to-first-deploy, lead time cho platform-supported path, tỷ lệ adoption tự nguyện, support ticket theo workflow, failure rate do configuration và developer satisfaction kết hợp reliability.

Metric cần chống gaming. Adoption cao vì policy bắt buộc chưa chắc user experience tốt.

## 11. Platform team không phải ticket team mới

Nếu mọi self-service form cuối cùng tạo ticket để platform engineer thao tác bằng tay, chỉ thay giao diện. True self-service cần automated provisioning với policy và asynchronous status rõ.

Human support vẫn cần cho exception, education và incident, nhưng common path không nên phụ thuộc queue.

## 12. Team topology và ownership

Platform team quản shared capability; enabling team có thể giúp product team học practice mới; complicated subsystem team sở hữu domain chuyên sâu. Boundary tổ chức nên giảm communication path bắt buộc.

Conway's Law nhắc rằng system architecture phản ánh communication structure. Platform API là cách biến communication lặp lại thành contract kỹ thuật.

## 13. Senior note: platform là dependency có blast radius lớn

Một bug trong shared pipeline template, base image hoặc ingress platform có thể ảnh hưởng toàn công ty. Vì vậy platform cần chính SLO, canary, compatibility test, incident response và staged rollout như bất kỳ product critical nào.

Platform Engineering không phải “DevOps team đổi tên”. Nó là product discipline áp dụng cho shared engineering capabilities.

## 14. Platform có control plane và data plane riêng

Một platform trưởng thành thường có thể nhìn thành hai lớp. **Control plane** nhận intent, validate policy, tạo workflow, lưu trạng thái và điều phối controller. **Data plane** là workload/resource thực sự phục vụ traffic hoặc chạy job.

Ví dụ developer yêu cầu “internal HTTP service”. Platform control plane có thể tạo repository metadata, identity, deployment object và observability config. Sau đó Kubernetes/cloud/runtime data plane mới chạy process và traffic.

Phân biệt này quan trọng khi incident. Portal/API platform down có thể làm không tạo service mới được nhưng workload hiện tại vẫn phục vụ user. Ngược lại platform UI xanh không chứng minh data plane application khỏe.

## 15. Self-service operation nên là asynchronous state machine

Provision database, cluster resource hoặc environment thường không hoàn thành trong một HTTP request ngắn. Platform API tốt không giả vờ mọi operation là synchronous. Nó nhận intent, tạo operation/resource identity rồi expose status/condition cho user theo dõi.

Mental model:

```text
request intent
→ accepted + resource/operation ID
→ validation/policy
→ provisioning/reconciliation
→ ready | failed | degraded
```

Điều này cho phép retry, timeout và partial failure có semantics rõ. Nếu user bấm nút lần hai vì trang web timeout mà backend không có idempotency key/resource identity, platform có thể tạo duplicate infrastructure.

## 16. Platform contract phải nói cả happy path lẫn failure semantics

API “CreateDatabase(plan=medium)” chưa đủ. Consumer còn cần biết create mất bao lâu, failure có retry được không, delete có giữ backup không, version upgrade có downtime không, credential rotate thế nào và SLO/support boundary là gì.

Abstraction mạnh không chỉ giảm số field; nó nén nhiều decision vào một contract ổn định. Nếu contract chỉ mô tả provisioning mà bỏ Day 2 operation, developer vẫn phải học implementation khi upgrade/incident.

## 17. Version evolution cần compatibility window

Platform interface thay đổi có thể ảnh hưởng hàng trăm team. Một breaking migration “mọi service đổi manifest trong tuần này” chuyển toil từ platform team sang toàn tổ chức.

Evolution tốt thường cần coexistence window: version cũ tiếp tục được support trong thời gian xác định; version mới có migration tool/preview; platform biết consumer nào còn ở old version; deprecation có telemetry và deadline.

Nếu có thể tự động migrate source/config an toàn, platform nên làm automation thay vì phát documentation dài yêu cầu từng team sửa tay.

## 18. Golden path phải encode escape hatch cost

Escape hatch không chỉ là boolean “được phép custom”. Nó cần ownership model. Team rời paved road có thể mất một phần support/SLO, tự chịu upgrade của custom component hoặc phải đáp ứng policy bổ sung.

Nếu custom path miễn mọi cost nhưng vẫn được platform team support đầy đủ, golden path khó duy trì. Ngược lại nếu escape hatch bị phạt quá nặng, team sẽ giấu workaround. Contract minh bạch giúp lựa chọn trade-off có chủ đích.

## 19. Platform SLO nên theo developer journey

Một platform có nhiều internal component nhưng user quan tâm journey end-to-end: tạo service, merge change, deploy, provision environment, rotate secret, debug incident. SLI chỉ đo API uptime của portal có thể xanh trong khi provisioning queue treo hàng giờ.

Ví dụ SLI platform có thể đo tỷ lệ provisioning hoàn tất trong 15 phút, tỷ lệ deploy pipeline thành công không do platform fault, hoặc time-to-first-production trên paved road. Khi SLO cháy, platform team có evidence để ưu tiên reliability thay vì chỉ nhìn support ticket.

## 20. Product discovery phải phân biệt cognitive load thiết yếu và accidental

Không phải mọi complexity đều nên giấu. Developer cần hiểu consistency, timeout, idempotency, resource demand và data ownership vì đó là physics của distributed application. Nhưng họ không nhất thiết phải biết account ID, subnet naming, ingress annotation hay secret-store wiring của tổ chức.

Platform tốt giảm **accidental complexity** nhưng giữ **essential complexity** đủ visible để user đưa quyết định đúng. Nếu abstraction biến mọi database thành một nút “Create” mà che RPO, connection limit và cost tier, cognitive load giảm ngắn hạn nhưng incident/risk tăng dài hạn.

## 21. Senior walkthrough: platform migration gây blast radius toàn công ty

Giả sử shared base image mới nâng runtime/CA bundle và platform cập nhật template để mọi build dùng ngay version mới. Nếu rollout đồng loạt, một compatibility bug có thể làm hàng trăm service fail cùng lúc.

Platform release nên được xử lý như production release: canary một nhóm consumer, compatibility test trên representative workload, đo failure signal, sau đó staged adoption. Có thể giữ old/new version song song và auto-open migration PR thay vì force-update instant.

Điểm cốt lõi là platform có **fan-out blast radius** lớn. Mức discipline cần cao hơn, không thấp hơn, application team bình thường.