# Kubernetes: reconciliation, API objects và control plane

## 1. Kubernetes không phải “Docker chạy nhiều máy”

Kubernetes tồn tại vì khi số workload và node tăng, việc tự quyết định container chạy ở đâu, restart thế nào, route tới instance nào và rollout phiên bản mới trở thành một bài toán orchestration có state. Kubernetes giải bài toán này bằng một kiến trúc rất nhất quán: người dùng khai báo trạng thái mong muốn (desired state), control plane lưu và quan sát state, controller liên tục đối soát (reconciliation) để actual state tiến gần desired state.

Mental model cốt lõi:

```text
user / automation
      ↓
 Kubernetes API
      ↓ desired state
 persistent control-plane state
      ↓ watch
 controllers + scheduler
      ↓ act
 kubelet / networking / storage / runtime
      ↓
 actual workload state
      └──── feedback/status ────→ API
```

Nếu chỉ nhớ YAML field mà không hiểu vòng này, rất dễ nhầm “resource đã tạo” với “application đã chạy đúng”.

## 2. API object là contract state

Một object Kubernetes thường có `metadata`, `spec` và `status`. `spec` chủ yếu mô tả điều người dùng muốn. `status` là quan sát của controller về trạng thái hiện tại. Generation, conditions và observed state cho biết controller đã xử lý spec mới tới đâu.

Vì vậy khi `kubectl apply` thành công, điều chắc chắn nhất chỉ là API server chấp nhận request. Deployment có thể vẫn chưa rollout, pod có thể Pending, image pull có thể fail hoặc readiness có thể chưa đạt.

Đây là khác biệt giữa control-plane acknowledgement và data-plane outcome.

## 3. API server là front door của control plane

API server xác thực request, kiểm tra authorization/admission, validate object rồi lưu state. Các controller và component khác watch API thay vì sửa trực tiếp database control-plane.

Điều này tạo một contract mạnh: API là boundary thống nhất cho người dùng, controller và automation. Nó cũng làm API server trở thành security boundary; RBAC quá rộng nghĩa automation có thể thay nhiều state hơn dự kiến.

## 4. etcd và consistency của cluster state

Kubernetes thường dùng `etcd` làm persistent store cho control-plane state. Không cần trở thành chuyên gia Raft để sử dụng Kubernetes, nhưng phải hiểu rằng cluster state là distributed durable state và backup/restore nó khác backup application data.

Consensus, log replication và snapshot mechanism được đào sâu tại [Computer Science — consensus, log replication và snapshots](../../computer_science/06_networks_distributed_systems/advanced/03_consensus_log_replication_reconfiguration_and_snapshots.md). DevOps cần quan tâm vận hành: control-plane backup, compatibility khi upgrade và recovery procedure đã được test hay chưa.

## 5. Controller là control loop có ownership field

Deployment controller, ReplicaSet controller, node controller và nhiều controller khác đều watch state rồi tạo action. Một controller tốt có tính lặp an toàn (idempotent): chạy lại không được tạo state sai chỉ vì event bị duplicate.

Điểm dễ bỏ qua là nhiều controller có thể tương tác trên cùng object graph. Deployment tạo ReplicaSet; ReplicaSet tạo Pod; scheduler gán Pod vào node; kubelet làm container chạy; CNI cung cấp network; CSI cung cấp volume. Khi Pod không Ready, failure có thể nằm ở bất kỳ stage nào.

Troubleshooting Kubernetes vì vậy nên đọc object graph và event chain, không chỉ restart pod.

## 6. Scheduler quyết định placement, không chạy workload

Scheduler chọn node phù hợp cho Pod dựa trên constraint, resource request, affinity/anti-affinity, taint/toleration và plugin scoring. Sau khi binding, kubelet trên node mới thực hiện việc kéo image, mount volume và gọi runtime.

Nếu Pod `Pending`, trước hết xem scheduler/event. Nếu Pod đã `Scheduled` nhưng container không start, search space chuyển sang kubelet/runtime/image/storage. Tách stage giúp giảm đoán mò.

## 7. Kubelet nối desired Pod với node reality

Kubelet là node agent. Nó quan sát Pod được assign cho node, phối hợp runtime/network/storage và báo status về API. Kubelet không phải scheduler và không tự chọn workload từ cluster.

Khi node mất liên lạc với control plane, Pod process có thể còn chạy một thời gian trong khi cluster không còn chắc về state. Đây là ví dụ distributed systems: “không nhận heartbeat” không chứng minh process chết. Failure detector luôn có uncertainty. Nền sâu xem [failure detectors, membership và gossip](../../computer_science/06_networks_distributed_systems/advanced/01_failure_detectors_membership_and_gossip.md).

## 8. Declarative state không có nghĩa mọi thay đổi đều safe

Kubernetes dễ apply config nhưng không hiểu business invariant. Nếu giảm replica từ 10 xuống 1, API vẫn có thể chấp nhận. Nếu readiness probe sai, controller có thể rollout workload không thực sự usable. Declarative engine bảo đảm convergence theo spec; con người/platform phải bảo đảm spec đúng và rollout policy phù hợp.

Admission policy, defaults, quotas và platform abstractions tồn tại để encode những invariant tổ chức muốn giữ trước khi state đi vào cluster.

## 9. Labels và selectors tạo quan hệ động

Kubernetes dùng label/selector để liên kết object như Service→Pod hoặc Deployment→ReplicaSet. Đây là abstraction mạnh nhưng cũng là nguồn failure tinh vi: typo label có thể làm Service không còn endpoint dù Pod healthy.

Selector nên được coi là relational contract. Thay label strategy có thể có blast radius lớn hơn diff YAML thể hiện.

## 10. Namespace là organizational boundary, không phải security boundary tuyệt đối

Namespace giúp scope name, RBAC, quota và policy, nhưng workload ở hai namespace không mặc định bị network-isolated. Security cần nhiều lớp: RBAC, network policy, workload identity, pod security và secret boundary.

Dùng namespace như unit ownership/tenancy là hợp lý khi đi kèm policy rõ; không nên giả định “khác namespace nên không thể ảnh hưởng nhau”.

## 11. Custom Resource và operator

Custom Resource Definition mở rộng API để platform tự định nghĩa desired state mới. Operator/controller đọc resource đó rồi reconcile external/internal resource.

Ví dụ `Database` custom resource có thể đại diện intent “tôi cần PostgreSQL plan X”, còn controller tạo cloud database, secret reference và monitoring. Đây là bridge trực tiếp sang Platform Engineering.

Nhưng CRD chỉ đáng có khi có stable domain model. Nếu mọi cloud field bị expose nguyên xi, platform chỉ đổi YAML shape mà chưa tạo abstraction.

## 12. Evidence khi debug control loop

Thứ tự hữu ích là đọc `spec`, `status.conditions`, `events`, child resources và node/runtime evidence. Hỏi controller nào đang sở hữu bước hiện tại và desired/actual khác nhau ở đâu.

Ví dụ Deployment không Available: xem desired replicas và conditions; ReplicaSet có pod chưa; Pod Pending hay Running; nếu Running thì Ready chưa; nếu không Ready thì probe/application; nếu Pending thì scheduler event; nếu ImagePullBackOff thì registry/auth/image.

## 13. Senior note: Kubernetes là nhiều control loop lồng nhau

Một ứng dụng Kubernetes thường nằm trong nhiều loop: Deployment controller, HPA, GitOps controller, service mesh controller, cloud load balancer controller và autoscaler. Hai controller cùng sửa một field có thể tạo oscillation.

Khi platform tự động hóa nhiều hơn, câu hỏi quan trọng không phải “controller có chạy không?” mà là **ai sở hữu field nào, control loop có stable không, latency của feedback là bao lâu và failure có bị khuếch đại giữa các loop không?**