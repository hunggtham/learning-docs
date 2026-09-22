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