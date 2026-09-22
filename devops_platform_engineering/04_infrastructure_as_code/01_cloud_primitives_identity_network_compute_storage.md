# Cloud primitives: identity, network, compute, storage và shared responsibility

## 1. Cloud không xóa hạ tầng, nó chuyển boundary điều khiển

Public cloud biến nhiều capability hạ tầng thành API. Thay vì mua server, cắm switch và cấu hình storage bằng ticket, engineer gọi control plane để yêu cầu compute, network, database hoặc queue. Điều thay đổi lớn nhất không chỉ là location của máy chủ mà là **infrastructure trở thành programmable resource có lifecycle nhanh hơn**.

Điều này làm IaC, identity và policy quan trọng hơn. Khi một API call có thể tạo hàng trăm resource hoặc mở network ra Internet, automation cần guardrail tương xứng.

## 2. Shared responsibility là boundary, không phải khẩu hiệu

Cloud provider sở hữu một phần stack; customer sở hữu phần còn lại. Boundary thay đổi theo service model. Với VM, customer thường chịu OS patch, process và nhiều network configuration. Với managed database, provider quản nhiều phần OS/database engine nhưng customer vẫn sở hữu schema, access, backup policy, query load và data classification.

Một lỗi phổ biến là nghe từ “managed” rồi giả định provider chịu luôn availability/data recovery theo business requirement. Managed service chỉ thay responsibility matrix; không loại bỏ responsibility.

## 3. Identity là perimeter mới

Trong cloud, IAM policy thường quyết định resource nào có thể gọi API nào. Network private không đủ nếu credential bị lộ có quyền rộng. Human identity, workload identity và automation identity nên tách nhau.

Least privilege không có nghĩa viết policy nhỏ nhất ngay từ ngày đầu bằng phỏng đoán. Nó là lifecycle: bắt đầu permission theo use case, quan sát action thật, giảm wildcard, review unused privilege và dùng short-lived credential khi có thể.

Workload nên ưu tiên identity federation/role thay vì static access key bake vào file/image. Nếu secret dài hạn bị copy qua nhiều CI runner và laptop, rotation trở thành rất khó.

## 4. Region, zone và failure domain

Region thường gồm nhiều availability zone/failure domain riêng hơn. Triển khai replica ở nhiều zone giảm rủi ro node/zone, nhưng không tự động chịu region outage. Multi-region tăng resilience nhưng thêm consistency, data replication, routing và operational complexity.

Đừng chọn multi-region chỉ vì nghe “enterprise”. Bắt đầu từ SLO, RPO/RTO và business impact rồi mới chọn failure domain cần chịu.

## 5. Virtual network là topology + policy

Cloud virtual network thường có subnet, route table, security group/firewall, NAT, gateway và load balancer. Mental model vẫn là packet path. “Private subnet” thường nghĩa không có direct inbound route từ Internet theo topology hiện tại, không phải resource tự động an toàn trước mọi data exfiltration hoặc credential misuse.

Troubleshooting nên vẽ source → DNS → route → security policy → load balancer → target. Chapter [network request path](../01_runtime_foundations/01_network_dns_tls_and_request_path.md) cung cấp causal chain chung.

## 6. Compute: VM, container và serverless là abstraction khác nhau

VM cho control lớn và boundary kernel riêng. Container tăng density/packaging consistency nhưng chia kernel host. Serverless/function/managed runtime đẩy lifecycle/scheduling xuống provider và tính tiền theo model khác.

Không có abstraction luôn tốt hơn. Workload lâu dài, latency-sensitive, GPU, stateful hoặc cần kernel control có requirement khác event-driven function ngắn. Platform nên offer một số paved road theo workload class thay vì buộc tất cả vào Kubernetes.

## 7. Object, block và file storage có semantics khác

Object storage cung cấp object/key API, phù hợp artifact, backup, static asset và data lake pattern. Block storage giống device/volume cho filesystem/database. File storage cung cấp shared filesystem semantics.

Chọn storage theo consistency, access pattern, latency, durability, sharing và lifecycle. Không chọn chỉ theo “rẻ hơn mỗi GB”. Request cost, egress, IOPS và data retrieval có thể chi phối tổng chi phí.

## 8. Managed database là dependency có quota và maintenance

Managed DB vẫn có connection limit, IOPS, failover behavior, maintenance window và version lifecycle. Application connection pool phải phù hợp capacity. Nếu autoscale application từ 10 lên 100 replica, tổng connection có thể tăng 10 lần và làm database collapse.

Platform cần expose quota/budget và integration pattern chứ không chỉ nút “Create database”.

## 9. Quota là một phần capacity

Cloud account/project có quota theo region/service. Autoscaler không thể tạo node mới nếu quota hết. DR failover cũng có thể thất bại nếu region dự phòng chưa có quota/capacity reservation.

Quota nên được monitor trước khi incident, giống disk space. Đây là dependency control-plane chứ không hiện trên application CPU chart.

## 10. Egress và locality

Data transfer giữa zone/region/Internet vừa ảnh hưởng latency vừa cost. Kiến trúc microservice chatty xuyên zone/region có thể tạo bill lớn. Cost telemetry cần nối topology với traffic volume.

“Cloud cost” thường là architectural signal. High egress có thể cho thấy data/service boundary chưa hợp lý, không chỉ là vấn đề mua discount.

## 11. Control plane failure và cached data plane

Nhiều managed service có control plane riêng với data plane. Control plane tạm lỗi không luôn làm traffic hiện tại dừng; nhưng scale, config change hoặc failover có thể không thực hiện được.

Incident runbook phải phân biệt “service data path down” với “provider control API degraded”. Trong trường hợp control plane lỗi, liên tục retry provisioning có thể làm queue/action storm khi provider hồi phục.

## 12. Senior note: thiết kế cloud theo capability, không theo catalog

Cloud provider có hàng trăm service, nhưng platform không nên expose catalog nguyên xi. Hãy gom theo capability: chạy HTTP service, chạy batch, lưu relational data, publish event, lưu object, expose public endpoint. Sau đó platform chọn implementation/default dựa trên tổ chức.

Cách này giảm vendor-specific cognitive load và cho phép evolution mà không bắt product team học lại toàn bộ provider.