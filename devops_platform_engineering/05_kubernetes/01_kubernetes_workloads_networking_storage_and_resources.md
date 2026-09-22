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

## 16. Scheduling là bài toán feasibility trước, scoring sau

Scheduler không bắt đầu bằng việc “chọn node tốt nhất”. Trước hết nó loại các node không thể chạy Pod theo constraint và resource request. Sau khi có tập node khả thi, scoring mới xếp hạng lựa chọn.

Điều này giải thích một failure hay gặp: cluster nhìn tổng thể còn nhiều CPU nhưng Pod vẫn `Pending`. Capacity có thể bị phân mảnh. Ví dụ còn bốn node, mỗi node rảnh 1 CPU nhưng Pod request 2 CPU; tổng free là 4 CPU nhưng không node nào đủ 2 CPU. Đây là khác biệt giữa **aggregate capacity** và **schedulable capacity**.

Resource request vì vậy vừa là reservation model vừa là input bin-packing. Request thấp quá tạo overcommit runtime; cao quá tạo fragmentation và tăng node count. Tuning phải nhìn distribution theo replica, không chỉ tổng usage.

## 17. PodDisruptionBudget không phải availability guarantee

PodDisruptionBudget (PDB) chủ yếu giới hạn một số **voluntary disruption** như node drain/maintenance theo cơ chế có tôn trọng PDB. Nó không ngăn node crash, kernel panic hay application process chết.

Do đó một PDB `minAvailable: 2` không có nghĩa “luôn luôn có ít nhất hai Pod”. Nếu hai node cùng mất đột ngột, PDB không thể ngăn failure. Ngược lại, PDB quá chặt có thể chặn maintenance/upgrade nếu workload không có đủ replica hoặc cluster thiếu capacity tạo replacement.

Mental model đúng là: PDB bảo vệ budget cho planned eviction, còn high availability cần topology, replica, capacity và dependency redundancy.

## 18. Priority và preemption đổi failure từ “không schedule được” thành “ai bị đẩy ra”

Khi cluster thiếu resource, Pod priority có thể cho phép workload quan trọng giành chỗ bằng cách preempt workload thấp hơn. Đây là cơ chế policy mạnh nhưng có trade-off: critical workload có thể phục hồi nhanh hơn trong khi batch/dev workload bị gián đoạn.

Nếu mọi team tự đánh workload của mình là priority cao nhất, mechanism mất tác dụng. Priority class phải gắn với business criticality và governance. Preemption cũng không tạo thêm capacity; nó chỉ phân bổ lại scarcity.

## 19. Topology spread cần hiểu failure domain thật

Replica “nằm trên ba node khác nhau” chưa chắc độc lập nếu ba node cùng zone, cùng rack hoặc cùng autoscaling group có failure chung. Topology spread/anti-affinity chỉ hữu ích nếu label topology phản ánh failure domain có ý nghĩa.

Ngược lại, yêu cầu spread quá cứng trong cluster nhỏ có thể làm Pod `Pending` trong lúc incident. Platform nên phân biệt invariant bắt buộc — ví dụ replica critical phải trải ít nhất hai zone — với preference có thể nới khi capacity căng.

## 20. Readiness và termination có một race window

Khi một Pod bị terminate, nhiều subsystem cần hội tụ: Pod nhận termination signal, readiness/endpoints thay đổi, proxy/load balancer cập nhật route và connection hiện tại drain. Những bước này không xảy ra atomically.

Nếu application đóng listener ngay lập tức trong khi proxy vẫn còn route tới endpoint vài giây, user có thể thấy burst 502/connection reset trong rollout dù readiness probe trước đó hoàn toàn đúng. Graceful termination vì vậy cần phối hợp application shutdown với endpoint propagation và connection draining.

Một sequence thường an toàn hơn là: đánh dấu workload không còn sẵn sàng nhận traffic, cho data plane đủ thời gian cập nhật, dừng nhận request mới, hoàn tất in-flight request trong deadline, rồi process thoát trước khi grace period kết thúc. Exact mechanism tùy ingress/runtime nhưng causal chain giống nhau.

## 21. HPA metric phải gắn với work, không chỉ resource

CPU-based HPA hoạt động tốt khi CPU gần tỷ lệ với demand. Nhưng với I/O-bound service, CPU thấp không có nghĩa còn capacity. Queue consumer có thể phù hợp hơn với queue age/depth; request service có thể scale theo concurrency hoặc request rate nếu signal đáng tin.

Metric autoscaling còn có vấn đề cold start. Khi scale out, Pod mới có thể cần load class/JIT/cache/model trước khi thực sự tăng service rate. Nếu HPA nhìn metric thay đổi nhanh hơn workload warm-up, controller có thể overshoot rồi scale down, tạo oscillation.

Do đó autoscaling policy cần biết observation window, stabilization, startup time và minimum headroom. Control loop tốt không chỉ phản ứng đúng hướng mà còn phải ổn định theo thời gian.

## 22. Autoscaling nhiều tầng có thể tạo feedback ngoài ý muốn

Giả sử HPA tăng replica vì latency/CPU. Pod mới không schedule được nên cluster autoscaler tăng node. Khi node xuất hiện, hàng loạt Pod start cùng lúc, mở connection DB và warm cache. Database bị saturation, latency tăng thêm, HPA lại tăng replica. Một loop local hợp lý có thể khuếch đại failure toàn hệ thống.

Cách thiết kế trưởng thành là đặt boundary: max replica theo downstream capacity, connection budget, rate limit, warm-up control và SLO signal. Autoscaler không được coi downstream là vô hạn.

## 23. Senior walkthrough: rollout stuck dù workload mới “không lỗi”

Giả sử Deployment 20 replica dùng `maxSurge: 25%`, nhưng cluster gần đầy. Controller muốn tạo thêm 5 Pod mới trước khi xóa Pod cũ. Scheduler không tìm được node vì request không fit; cluster autoscaler không thể tạo node do cloud quota đã chạm. Pod mới `Pending`, rollout không tiến.

Ứng dụng mới không có bug, readiness chưa có cơ hội chạy. Failure nằm ở interaction giữa rollout policy, resource request, cluster headroom và cloud quota. Fix có thể là tăng capacity/quota, điều chỉnh rollout budget hoặc giảm request sau khi có evidence; restart Pod không giải được causal chain.

Đây là kiểu production reasoning Kubernetes cần: object status là symptom của nhiều control loop lồng nhau, không phải một lỗi đơn lẻ.

## 24. Persistent volume có topology và attach lifecycle riêng

Một PVC tồn tại không có nghĩa volume có thể mount ở mọi node. Nhiều block volume gắn với zone hoặc có giới hạn số volume attach trên node. Scheduler/storage controller phải phối hợp placement với topology của volume.

Vì vậy Pod stateful có thể `Pending` dù CPU/memory còn nhiều nếu volume ở zone không có node phù hợp, attach limit đã chạm hoặc volume vẫn đang detach từ node cũ. Đây là failure path khác hoàn toàn với application startup.

Khi điều tra, nối `PVC/PV → StorageClass/topology → selected node → attach/mount event`. Scale node ở zone khác không giúp nếu volume không di chuyển được. Storage topology phải là input của capacity/recovery design, không phải chi tiết CSI bị phát hiện lần đầu trong incident.

## 25. StatefulSet stable identity không tự tạo data safety

StatefulSet giữ ordinal/network identity và thường gắn mỗi replica với PVC riêng. Nhưng nó không tự hiểu replication/quorum của database. Xóa hoặc restart replica theo thứ tự “đẹp” vẫn có thể mất quorum nếu data system có topology khác Kubernetes topology.

Rolling update của stateful workload cần biết node nào leader, replica nào lag, partition/update order và application-level readiness thật sự có nghĩa gì. Probe chỉ trả lời condition được encode; nó không thay thế consistency invariant của database.

Vì vậy platform không nên biến StatefulSet thành “database button” nếu không sở hữu backup, replication, upgrade và recovery semantics tương ứng.

## 26. Ephemeral storage cũng là resource có pressure và eviction

Pod có thể ghi writable layer, `emptyDir`, logs hoặc temporary files. Những bytes này dùng node ephemeral storage. Workload có CPU/memory khỏe nhưng vẫn bị evict hoặc fail khi node disk pressure nếu temporary/log output tăng bất thường.

Resource planning cần nhìn cả byte capacity lẫn I/O rate. Một batch job tạo hàng trăm GiB temporary data có thể ảnh hưởng node khác dù final output được upload object storage. Requests/limits/quota cho ephemeral storage, log rotation và cleanup lifecycle giúp biến resource ẩn thành contract.

Khi `DiskPressure` xuất hiện, chỉ xóa Pod thường giải phóng tạm thời nhưng không sửa producer tạo data không bounded.

## 27. Job retry semantics phải đi cùng idempotency của business work

`Job` có thể chạy lại Pod khi process fail. Điều đó tốt cho transient infrastructure failure nhưng nguy hiểm nếu business operation đã side-effect một phần rồi exit trước khi ghi completion state.

Ví dụ job charge invoice: payment API đã nhận request nhưng process chết trước khi lưu “done”. Pod mới chạy lại và charge lần hai nếu operation không có idempotency key/transaction protocol phù hợp. Kubernetes chỉ biết process completion, không biết business effect.

Batch platform nên expose retry/backoff/dead-letter semantics và khuyến khích work item có durable identity. “At least one successful Pod” không đồng nghĩa “business side effect exactly once”.

## 28. CronJob phải reasoning về missed run và overlapping run

Scheduled job phụ thuộc controller clock, scheduling delay và previous run duration. Nếu job 10 phút nhưng chạy mỗi 5 phút, overlap có thể tạo concurrent work ngoài ý muốn. Nếu control plane down, một số schedule có thể bị trễ/missed theo policy.

Vì vậy batch contract cần quyết định overlap có được phép không, late execution còn giá trị không, deadline là gì và work có deduplicate theo logical schedule ID không. Không nên giả định cron expression tự tạo business correctness.

Một report “mỗi ngày lúc 00:00” thường thực sự có invariant về data window, timezone và exactly-one logical output; đó là application contract cần được encode ngoài scheduler.

## 29. Endpoint scale tạo pressure lên control plane và data plane

Một Service có vài endpoint khác với một Service có hàng chục nghìn endpoint. Endpoint update, watch fan-out và proxy programming đều có cost. Khi workload churn lớn, control plane có thể xử lý liên tục endpoint changes trong khi data plane chưa hội tụ hoàn toàn.

Vì vậy “thêm thật nhiều replica” không miễn phí. Replica count lớn tăng scheduling, image pull, readiness probe, endpoint propagation, connection warming và observability cardinality. Có lúc scale-up làm reliability giảm vì control-plane/data-plane churn lớn hơn lợi ích capacity.

Capacity engineering cần tìm điểm mà thêm replica còn tăng throughput hữu ích, thay vì dùng replica count như actuator không giới hạn.

## 30. Senior walkthrough: Pod stateful failover chậm dù node mới đã sẵn sàng

Giả sử node chứa một database replica chết. Autoscaler tạo node mới trong 2 phút nhưng Pod vẫn `Pending` thêm 8 phút. CPU/memory fit và image đã pull. Event cho thấy volume cũ chưa detach khỏi node mất liên lạc nên attach vào node mới bị block để tránh simultaneous writer.

Causal chain nằm ở storage fencing/attach lifecycle, không ở scheduler capacity. Force-detach có thể rút ngắn recovery nhưng tăng risk nếu node cũ thực ra vẫn ghi được. Đây là trade-off giữa recovery time và split-brain/data corruption.

Bài học là recovery của stateful workload bị giới hạn bởi **data ownership transfer**, không chỉ bởi tốc độ tạo Pod/node.

## 31. Eviction là protocol có nhiều nguyên nhân, không phải mọi Pod biến mất đều giống nhau

Pod có thể rời node vì operator drain, cluster autoscaler scale-down, node pressure, preemption, node failure hoặc controller rollout. Các đường này có semantics khác nhau: có đường tôn trọng PDB, có đường không; có đường cho grace period đầy đủ, có đường process biến mất cùng node.

Runbook không nên chỉ nhìn trạng thái cuối `Terminated/Evicted`. Evidence cần giữ reason, initiator, node condition, PDB decision và replacement timing. Nếu 20 Pod cùng biến mất vì autoscaler consolidation, remediation khác hoàn toàn 20 Pod bị OOM hoặc zone mất điện.

Platform nên coi disruption source như change telemetry. Availability budget chỉ có ý nghĩa khi biết ai đang tiêu budget và mechanism đó có thể pause/throttle được không.

## 32. Cluster autoscaler scale-down cũng là một control loop gây disruption

Scale-up thường được chú ý vì thiếu capacity, nhưng scale-down có thể tạo churn khi node vừa trở nên “ít dùng”. Evict Pod để consolidate node làm replacement schedule ở nơi khác, pull image, warm cache và mở lại connection. Nếu traffic tăng lại ngay sau đó, cluster có thể vừa scale down xong đã phải scale up.

Một hệ thống ổn định cần hysteresis/stabilization: không thu hồi capacity quá nhanh chỉ vì một cửa sổ utilization thấp. Với workload có startup lâu hoặc traffic theo burst, một phần idle headroom có thể rẻ hơn latency/recovery cost của việc liên tục tạo-hủy node.

Evidence nên nối `scale-down decision → evictions → rescheduling/warm-up → user latency/SLO → scale-up tiếp theo`. Nếu chỉ nhìn cloud cost giảm, ta có thể bỏ qua oscillation mà autoscaler tạo ra.

## 33. HPA, VPA và rollout có thể tranh quyền trên cùng workload

Horizontal scaling thay replica count; vertical scaling thay request/limit; rollout thay Pod template và tạo replacement. Nếu nhiều controller cùng điều chỉnh resource mà không có ownership contract, một action có thể làm signal của controller khác đổi đột ngột.

Ví dụ VPA tăng CPU request làm Pod cũ cần recreate; scheduler cần node lớn hơn; rollout đang surge; HPA lại scale replica dựa trên utilization tính theo request mới. Từng controller local có thể đúng nhưng composition tạo Pending Pod, churn hoặc capacity spike.

Platform cần xác định controller nào được phép mutate field nào, recommendation nào chỉ advisory và maintenance window nào cho disruptive resize. Mental model là **multi-controller composition**, không phải bật càng nhiều autoscaler càng tốt.

## 34. Sau failure, topology có thể hồi phục capacity nhưng chưa hồi phục redundancy

Giả sử service ba replica trải ba zone. Một zone mất, scheduler tạo replacement ở hai zone còn lại để khôi phục replica count. Dashboard lại thấy `3/3 Ready`, nhưng failure tolerance đã giảm vì hai hoặc ba replica có thể tập trung vào ít failure domain hơn.

Khi zone cũ trở lại, scheduler không nhất thiết tự di chuyển Pod chỉ để tái cân bằng nếu placement hiện tại vẫn hợp lệ. Vì vậy recovery criterion cần kiểm tra **redundancy/topology invariant**, không chỉ desired replica count. Có thể cần controlled rebalance với disruption budget và capacity headroom.

Đây là distinction quan trọng giữa `capacity recovered` và `resilience recovered`.

## 35. Sidecar và init lifecycle có thể giữ Pod chưa thật sự hoàn tất hoặc chưa thật sự sẵn sàng

Một Pod có nhiều container nên lifecycle của business process không luôn trùng lifecycle toàn Pod. Init work có thể block startup; sidecar proxy/agent có thể cần sẵn sàng trước application traffic hoặc cần sống đủ lâu để flush telemetry/drain network khi shutdown.

Nếu readiness chỉ kiểm tra application nhưng sidecar data plane chưa nhận config, Pod có thể được route quá sớm. Nếu Job business container hoàn thành nhưng helper container không có completion semantics đúng, logical work đã xong nhưng Pod vẫn chưa kết thúc như operator kỳ vọng.

Thiết kế cần xác định dependency order giữa containers, readiness của **request path đầy đủ**, và shutdown order để in-flight work/telemetry không mất. “Container chính healthy” chưa chắc đồng nghĩa Pod capability mà user cần đã healthy.