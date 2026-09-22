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

## 13. API success không luôn đồng nghĩa resource đã usable

Cloud control plane thường có hành vi bất đồng bộ và nhất quán cuối cùng (eventual consistency). API tạo role, route, DNS record hoặc database có thể trả thành công trước khi mọi subsystem nhìn thấy state mới.

Vì vậy automation không nên giả định `create` thành công là bước sau có thể dùng ngay. Cần waiter/retry có backoff cho condition cụ thể, nhưng retry phải phân biệt trạng thái “chưa hội tụ” với lỗi permission/config không thể tự hết.

Một pipeline tạo IAM role rồi ngay lập tức assume role có thể thỉnh thoảng fail dù code không đổi. Nếu chỉ rerun đến khi pass, ta che mất propagation contract. Platform nên encode stabilization semantics để consumer không phải tự đoán sleep bao nhiêu giây.

## 14. Durability, availability và backup là ba property khác nhau

Một storage service có durability rất cao nghĩa xác suất mất bytes lâu dài thấp, nhưng vẫn có thể tạm unavailable do network, identity, control plane hoặc regional issue. Ngược lại service highly available không thay thế backup nếu dữ liệu bị xóa/corrupt hợp lệ rồi replication lan truyền thay đổi đó.

Do đó “provider quảng cáo nhiều số 9” phải hỏi đang nói về durability hay availability và scope nào. Business RPO/RTO vẫn cần recovery design riêng.

Object versioning, cross-region replication và backup vault có thể cung cấp các failure boundary khác nhau; không nên coi chúng là cùng một control.

## 15. Multi-zone không có nghĩa dependency graph đã multi-zone

Application replica có thể nằm ba zone nhưng NAT gateway, database writer, secret endpoint hoặc external dependency vẫn tạo single failure domain. Availability phải được reasoning theo **đường request và dependency graph**, không theo số zone của riêng compute.

Một review hữu ích là chọn một zone rồi giả định zone đó biến mất: traffic route lại ra sao, workload còn capacity không, storage attach/failover mất bao lâu, DNS/identity/control plane có phụ thuộc resource trong zone đó không.

Nếu hệ thống chỉ sống được khi autoscaler thêm node sau failure nhưng node provisioning mất 15 phút còn SLO không chịu được 15 phút degraded capacity, topology trên giấy chưa đủ.

## 16. Autoscaling bị giới hạn bởi provisioning latency và downstream budget

Cloud API giúp scale nhanh hơn datacenter truyền thống nhưng không tức thời. VM/node có thể mất phút để provision, image pull thêm thời gian, application warm-up thêm thời gian nữa. Serverless có abstraction khác nhưng vẫn có concurrency limit, cold-start hoặc downstream quota.

Capacity planning cần so **time-to-capacity** với tốc độ demand tăng. Nếu traffic có thể tăng gấp bốn trong 30 giây còn thêm capacity cần 8 phút, phải giữ headroom, pre-scale theo event hoặc shed load.

Scale compute cũng không tạo thêm database connection budget, third-party API quota hay NAT capacity. Autoscaling là một actuator, không phải nguồn capacity vô hạn.

## 17. Managed service version lifecycle vẫn là trách nhiệm của consumer

Provider có thể patch OS hoặc vận hành failover, nhưng application vẫn phụ thuộc engine/API version, parameter compatibility và maintenance behavior. Major database/cache/runtime upgrade có thể đổi query plan, protocol default hoặc extension compatibility.

Production cần inventory version, deprecation timeline, test path và staged upgrade. “Managed” không biến version evolution thành zero-work; nó chuyển một phần execution cho provider nhưng compatibility contract vẫn thuộc system owner.

Maintenance window cũng là production event. Nếu provider failover/reboot trong window, application phải có reconnect/retry semantics phù hợp; connection pool giữ connection chết quá lâu có thể làm user impact kéo dài hơn infrastructure event.

## 18. IAM policy phải xét resource, action và context cùng lúc

Permission rộng không chỉ đến từ `Action: *`. Một action hẹp trên mọi resource hoặc trust policy cho phép principal quá rộng cũng có blast radius lớn. Điều kiện theo environment, source identity, audience, network context hoặc tag có thể thu hẹp capability khi semantics đáng tin.

Nhưng policy càng phức tạp càng khó reasoning. Platform nên cung cấp role theo capability đã thiết kế thay vì bắt mỗi team tự viết hàng trăm dòng IAM. Exception cần review theo capability thực sự được mở, không chỉ diff JSON.

## 19. Egress cost và latency có thể phát hiện boundary kiến trúc sai

Giả sử service A ở region Seoul gọi service B ở region Tokyo cho mỗi request chỉ để lấy metadata nhỏ nhưng thường xuyên. Hệ thống trả cả latency xuyên region lẫn egress cost cho một dependency chatty.

Thay vì chỉ mua discount, hãy hỏi data có thể cache/replicate gần consumer, API có quá fine-grained hay service boundary có đặt sai không. Cost ở đây là telemetry về architecture.

Tương tự, log ingestion tăng 5 lần sau một release có thể là debug verbosity bị bật hoặc retry loop; FinOps signal nên có đường quay lại production investigation.

## 20. Senior walkthrough: failover database thành công nhưng application vẫn outage

Giả sử managed DB tự failover trong 45 giây và endpoint DNS trỏ writer mới. Dashboard provider báo healthy nhưng application lỗi thêm 8 phút.

Evidence cho thấy connection pool giữ các TCP connection cũ; client driver không refresh DNS/reconnect nhanh; retry timeout dài làm worker bị giữ. Infrastructure failover đã hoàn thành, nhưng application recovery contract chưa hoàn thành.

Fix nằm ở connection validation/reconnect, timeout/backoff và test failover end-to-end. Đây là bài học cốt lõi của managed service: provider chỉ sở hữu một phần causal chain; user-visible recovery phải được kiểm chứng ở consumer.

## 21. API rate limit là capacity của control plane

Cloud API không có throughput vô hạn. Một autoscaler, IaC loop hoặc controller fan-out quá mạnh có thể chạm rate limit/throttle dù data-plane workload vẫn khỏe. Khi đó reconcile chậm, scale-out bị trì hoãn hoặc automation bắt đầu retry và tự tạo thêm áp lực.

Vì vậy control-plane client cần bounded concurrency, exponential backoff với jitter và ưu tiên action quan trọng. Nếu 10.000 resource cùng cần refresh sau outage, “retry càng nhanh càng tốt” có thể biến provider recovery thành thundering herd.

Platform nên quan sát API request rate, throttling, queue/reconcile latency và actor identity. Đây là capacity dimension riêng với CPU/memory của workload.

## 22. Zonal capacity scarcity khác quota

Có quota không đồng nghĩa provider chắc chắn có physical capacity ngay tại zone/instance class mong muốn. Một loại VM/GPU có thể tạm thiếu capacity trong một zone dù account quota còn. Autoscaler lúc đó có thể retry mãi trên một option không thể cấp phát trong thời gian cần thiết.

Thiết kế resilient có thể cần nhiều instance type tương đương, nhiều zone hoặc reserved capacity cho workload critical. Nhưng diversity cũng tăng complexity về architecture/performance. Quyết định phải quay về SLO và workload constraint.

Runbook scale failure nên phân biệt `quota exceeded`, `rate limited`, `capacity unavailable`, `permission denied` và `invalid configuration`; cùng biểu hiện “node không lên” nhưng recovery path khác nhau.

## 23. Recovery cần capacity ở failure state, không chỉ steady state

Hệ thống chạy bình thường với 50% utilization trên hai zone có vẻ có headroom. Nhưng nếu mất một zone chứa 50% capacity, zone còn lại lập tức lên gần 100% trước khi autoscaling kịp tạo resource. Nếu provider không còn capacity hoặc quota cho failover, redundancy trên sơ đồ không chuyển thành user availability.

Capacity planning vì vậy phải tính N-1 hoặc failure scenario phù hợp: sau khi mất failure domain lớn nhất, còn bao nhiêu capacity phục vụ traffic trong suốt `time-to-recover-capacity`? Headroom có thể cố ý “idle” ở steady state nhưng là insurance cho SLO.

FinOps cần hiểu reserve này để không tối ưu nhầm reliability headroom thành waste.

## 24. Cross-zone/region replication có consistency và bandwidth budget

Replication không phải phép nhân bản miễn phí. Synchronous replication thường tăng write latency và availability phụ thuộc quorum/path; asynchronous replication giảm coupling trên write path nhưng có replication lag và RPO khác 0 khi failover.

DevOps/Platform layer không cần viết lại distributed-consistency theory, nhưng phải expose consequence: metric lag nào cần theo dõi, failover ở lag bao nhiêu chấp nhận được, egress/bandwidth có đủ khi backfill/recovery không, và failback có conflict/data divergence semantics gì.

Nếu replication thường ngày chỉ dùng 20% network nhưng recovery/backfill cần gấp 10 lần throughput, đường truyền có thể trở thành bottleneck đúng lúc DR cần nhất. Recovery capacity phải được test ở scale thực tế.

## 25. Private endpoint vẫn cần DNS, IAM và route cùng hội tụ

Dịch vụ dùng private endpoint thường được xem “an toàn và đơn giản hơn Internet”, nhưng request path vẫn phụ thuộc nhiều lớp: private DNS resolve đúng address, route tới subnet/endpoint tồn tại, security policy cho phép flow và IAM/service policy cho phép operation.

Một migration từ public sang private endpoint có thể tạo partial failure nếu một VPC dùng DNS mới còn VPC khác cache record cũ, hoặc identity policy chỉ cho source endpoint mới. Vì vậy network privacy là một composition của name, topology và authorization, không phải một checkbox.

Troubleshooting vẫn theo nguyên tắc cũ: name → route → transport → identity → service response.

## 26. Senior walkthrough: autoscaler muốn thêm node nhưng recovery vẫn không tới

Giả sử sau khi một zone mất, workload Pending tăng và cluster autoscaler yêu cầu 30 node mới ở zone còn lại. Cloud quota đủ, nhưng API trả `capacity unavailable` cho instance type chính; controller retry nhanh và bắt đầu bị rate-limit. Mười phút sau provider capacity mới xuất hiện nhưng retry storm làm provisioning vẫn chậm.

Causal chain có ba boundary: physical capacity scarcity, control-plane rate limit và autoscaler retry policy. Chỉ tăng quota không giải quyết. Mitigation có thể mở thêm instance class/zone đã test, giảm retry concurrency và dùng reserved/warm capacity cho tier critical.

Bài học là “cloud elastic” luôn có **time, quota, API và physical-capacity constraints**. Elasticity là capability có latency và failure semantics, không phải định luật rằng capacity luôn xuất hiện khi gọi API.