# Kubernetes workload, networking, storage, scheduling và resource behavior

## 1. Chọn workload abstraction theo identity và lifecycle

`Deployment` phù hợp phần lớn stateless replica có thể thay thế. `StatefulSet` thêm stable identity/order và thường đi với persistent volume. `DaemonSet` bảo đảm workload chạy trên tập node phù hợp. `Job` mô tả công việc cần hoàn thành; `CronJob` tạo Job theo lịch.

Đừng chọn kind theo tên quen thuộc. Hãy hỏi instance identity có quan trọng không, công việc chạy liên tục hay hoàn thành, cần một bản sao trên mỗi node hay replica tùy ý, storage có gắn với identity không.

## 2. Pod là scheduling unit, không phải durable machine

Pod là đơn vị được scheduler đặt lên node. Container trong cùng Pod chia network namespace và có thể chia volume. Pod có IP riêng nhưng identity của Pod thường ephemeral. Khi Deployment thay Pod, IP mới có thể xuất hiện.

Vì vậy application không nên lưu danh sách Pod IP cứng. Service discovery và stable service abstraction tồn tại để decouple consumer khỏi instance lifecycle.

## 3. Service và endpoint

`Service` cung cấp logical endpoint cho một tập backend được chọn qua selector hoặc endpoint mechanism. Nó không “chứa traffic”; data plane như kube-proxy/eBPF implementation thực hiện forwarding.

Troubleshooting cần tách object đúng với packet path. Service object đúng nhưng endpoint rỗng thì selector/readiness có vấn đề. Endpoint đúng nhưng traffic fail thì xem target port, network policy, data plane hoặc application listener.

Request-path mental model đã có tại [DNS, TLS và request path](../01_runtime_foundations/01_network_dns_tls_and_request_path.md).

## 4. Ingress/Gateway và north-south traffic

Traffic từ ngoài cluster thường qua load balancer rồi ingress/gateway controller. Resource API mô tả routing intent; controller phải biến intent thành data-plane configuration.

Nếu sửa Ingress mà route không đổi, kiểm tra controller đã observe generation mới chưa, config reconcile có lỗi không và external load balancer/DNS đã hội tụ chưa. Đây vẫn là control-loop debugging.

## 5. ConfigMap và Secret không giải quyết toàn bộ config lifecycle

`ConfigMap` và `Secret` đưa configuration vào workload, nhưng cách application nhận update quyết định behavior. Environment variable thường chỉ có giá trị khi process start. Volume-mounted config có thể cập nhật file nhưng application có thể không reload.

Vì vậy “Kubernetes đã update Secret” không đồng nghĩa application đang dùng secret mới. Rotation phải có end-to-end lifecycle: issue → distribute → reload/restart → verify → revoke old.

Secrets ở mức cryptography/key lifecycle xem [canonical secrets, KMS, HSM và rotation](../../computer_science/07_security_reliability/advanced/06_secrets_kms_hsm_rotation_and_envelope_encryption.md).

## 6. Persistent Volume là contract storage

PersistentVolume/PersistentVolumeClaim tách nhu cầu storage khỏi implementation. StorageClass mô tả class/provisioning policy. Nhưng Kubernetes không biến stateful system thành stateless.

Database vẫn cần consistency, backup, replication và recovery semantics. Volume replication không tự động tương đương application-consistent backup. Snapshot lúc database đang ghi có thể cần coordination để khôi phục nhất quán.

## 7. Request và limit có hai vai trò khác nhau

Resource `request` là input quan trọng cho scheduling và capacity accounting. `limit` là boundary runtime tùy resource. Memory limit thường có thể dẫn đến OOM kill khi vượt; CPU limit thường throttle.

Nếu request thấp hơn usage thực quá nhiều, scheduler có thể nhồi quá nhiều workload lên node và tạo contention. Nếu request quá cao, cluster có capacity nhưng scheduler không dùng được hiệu quả. Resource tuning vì vậy là bài toán statistical/capacity, không phải copy template.

## 8. QoS và eviction dưới pressure

Khi node chịu memory/disk pressure, kubelet có thể evict workload. Priority và resource configuration ảnh hưởng workload nào được giữ. Critical service cần hiểu node failure/eviction behavior thay vì chỉ tăng replicas.

Một deployment ba replica nhưng cả ba nằm cùng node hoặc cùng failure domain vẫn có availability thấp. Anti-affinity/topology spread giúp phân tán, nhưng càng nhiều constraint càng có nguy cơ unschedulable khi capacity nhỏ.

## 9. Probe: startup, readiness, liveness

Startup probe giúp ứng dụng khởi động chậm tránh bị liveness kill sớm. Readiness quyết định traffic eligibility. Liveness quyết định restart khi process được xem là không tự hồi phục.

Một probe tốt phải rẻ, ổn định và phản ánh semantics đúng. Liveness không nên gọi một dependency xa nếu dependency outage không thể được chữa bằng restart local process. Nếu mỗi pod restart vì DB down, restart storm có thể làm recovery tệ hơn.

## 10. HPA và autoscaling là feedback controller

Horizontal Pod Autoscaler quan sát metric rồi thay desired replica count. Đây là một control loop có delay. Metric tăng → scale out → pod schedule/start/warm → traffic phân phối → metric thay đổi.

Nếu loop phản ứng quá nhanh với noisy metric, replica có thể dao động. Nếu phản ứng quá chậm, user chịu latency trước khi capacity đến. Metric chọn cho autoscaling phải liên hệ demand và bottleneck. CPU không phải lúc nào cũng phù hợp; queue depth hoặc concurrency có thể phản ánh workload tốt hơn.

## 11. Cluster autoscaling và interaction giữa control loop

HPA có thể yêu cầu thêm Pod nhưng scheduler không có chỗ. Cluster autoscaler thấy unschedulable Pod rồi tăng node. Cloud provider tạo VM mất thời gian. Nếu traffic spike ngắn hơn node provisioning time, autoscaling không cứu được spike đó.

Đây là lý do cần capacity buffer, rate limiting và load shedding. Autoscaling không thay thế capacity planning.

## 12. Rolling update và availability math

Deployment rollout dùng các tham số như `maxUnavailable` và `maxSurge` để điều khiển bao nhiêu replica cũ có thể mất và bao nhiêu replica mới có thể thêm. Nhưng availability thật còn phụ thuộc readiness time, capacity, PodDisruptionBudget, node drain và downstream.

Nếu cluster không có headroom để surge, rollout có thể stuck dù config hợp lý trên giấy.

## 13. Scheduling constraint như policy

Node selector, affinity, taint/toleration và topology spread là ngôn ngữ mô tả placement. Dùng quá nhiều hard constraint làm scheduling brittle. Ưu tiên soft preference khi business invariant không bắt buộc.

Platform nên expose intent như “GPU workload”, “zone-spread service”, “stateful-high-io” thay vì yêu cầu mọi developer hiểu toàn bộ label topology của cluster.

## 14. Failure walkthrough

Pod `Pending`: đọc events để biết insufficient CPU, taint, PVC hoặc affinity. Pod `Running` nhưng `NotReady`: xem readiness, application và dependency. Pod restart: xem `lastState`, exit code, OOM/event, liveness. Service 503: xem endpoints/readiness trước proxy config. Latency tăng khi CPU graph không cao: kiểm tra throttling, queue, downstream và node pressure.

## 15. Senior note: abstraction phải giữ được causal chain

Kubernetes có nhiều object và controller, nhưng operator giỏi luôn giữ causal chain: desired object → controller decision → child resource → scheduler/node → runtime → network/storage → application signal. Platform tốt có thể che bớt object bình thường nhưng phải cho phép mở causal chain khi incident.