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

## 14. API update là optimistic concurrency, không phải khóa object dài hạn

Kubernetes object thay đổi liên tục bởi nhiều actor. API không giữ một lock dài quanh object để ngăn mọi writer. Thay vào đó, mỗi version state có identity/version metadata; update có thể bị từ chối nếu actor dựa trên state cũ.

Mental model là optimistic concurrency: đọc state, tính thay đổi, cố ghi; nếu object đã đổi, reconcile lại trên state mới. Controller vì vậy phải chấp nhận conflict/retry thay vì giả định event chỉ đến đúng một lần và state đứng yên trong lúc xử lý.

Đối với operator/platform controller tự viết, logic “read-modify-write” cần idempotent và chịu conflict. Nếu retry tạo duplicate external resource, bug nằm ở controller contract chứ không phải API server.

## 15. `resourceVersion`, generation và observedGeneration trả lời câu hỏi khác nhau

`resourceVersion` giúp nhận diện phiên bản object trong API/storage/watch semantics. `metadata.generation` thường tăng khi desired spec thay đổi. Controller có thể ghi `observedGeneration`/condition để nói nó đã xử lý generation nào.

Khi spec vừa đổi nhưng status vẫn xấu, hãy hỏi controller đã observe generation mới chưa. Nếu chưa, lỗi có thể ở controller queue/watch. Nếu đã observe nhưng condition vẫn fail, controller đã xử lý intent và tìm thấy failure downstream.

Điều này tốt hơn nhìn timestamp hoặc chỉ chờ vài giây theo cảm giác.

## 16. Admission nằm trên write path nên policy có thể ảnh hưởng availability của control plane

Một request tạo/sửa object thường đi qua authentication, authorization, defaulting/validation và có thể qua admission policy/webhook trước khi persist. Admission cho phép encode guardrail nhưng cũng thêm dependency vào write path.

Nếu admission webhook timeout/fail theo policy fail-closed, deploy có thể bị chặn diện rộng. Nếu fail-open, availability tốt hơn nhưng security invariant có thể tạm không được enforce. Đây là trade-off phải quyết định theo loại policy, không có default đúng cho mọi rule.

Policy engine cần timeout nhỏ hợp lý, HA, telemetry và staged rollout. Một webhook global chậm có thể làm người dùng nghĩ “Kubernetes API chậm” trong khi read path vẫn bình thường.

## 17. Watch biến polling thành event stream nhưng không xóa nhu cầu resync

Controller thường `list` để có snapshot rồi `watch` thay đổi. Watch có thể bị ngắt; event có thể được coalesced hoặc controller restart. Vì vậy controller không nên dựa vào assumption “tôi sẽ nhận chính xác từng event một lần”.

Reconciliation pattern mạnh vì event chỉ là **hint rằng state có thể cần xử lý**. Controller đọc current desired/actual state và hội tụ. Đây là lý do idempotency quan trọng hơn event-processing chính xác từng message.

Khi controller backlog lớn, event delivery vẫn tiếp tục nhưng reconciliation latency tăng. Metric queue depth/reconcile duration/error rate của controller trở thành evidence quan trọng.

## 18. Work queue và backoff bảo vệ control plane khỏi hot loop

Nếu reconcile failure ngay lập tức được retry không giới hạn, một object lỗi có thể tạo hot loop, làm API/provider bị spam và che workload khác. Controller thường cần rate limit/backoff và phân biệt transient failure với invalid desired state.

Ví dụ external cloud API đang outage: retry có bounded exponential backoff hợp lý hơn hàng nghìn request/giây. Ngược lại spec invalid nên surface condition rõ để user sửa, không retry vô hạn như thể dependency sẽ tự hồi.

Một controller tốt không chỉ “eventually reconcile”; nó phải reconcile theo cách không tự khuếch đại outage.

## 19. API server saturation có thể đến từ client hành xử xấu

Control plane có finite CPU/memory/storage bandwidth và request budget. Client list toàn bộ cluster quá thường xuyên, controller tạo update storm hoặc automation retry không backoff có thể gây pressure.

Khi API latency tăng, cần phân dimension read/write, resource kind, client identity/user-agent, request rate và etcd/storage latency. Scale control plane có thể cần nhưng trước hết tìm noisy client/control loop.

Platform controller nên dùng informer/cache/watch phù hợp thay vì polling full list ngắn chu kỳ nếu không cần.

## 20. Upgrade cluster là compatibility problem nhiều chiều

Control plane, kubelet, API version, admission webhook, CRD và controller/operator đều có lifecycle version. “Cluster upgrade thành công” không chỉ là API server lên version mới; workload/controller cũ có thể dùng API đã deprecated hoặc assumptions cũ.

Production upgrade cần inventory API usage, compatibility của extension/controller, staged node/control-plane rollout theo support matrix và rollback/recovery plan. CRD conversion/admission component đặc biệt nhạy vì chúng nằm trên API path.

Không cần thuộc mọi version rule trong chapter này; invariant là **version skew phải nằm trong compatibility contract được support và được test trước production**.

## 21. Senior walkthrough: deploy toàn cluster bị treo nhưng application traffic vẫn khỏe

Giả sử nhiều team cùng báo `kubectl apply` timeout, GitOps controller backlog tăng, nhưng user traffic application vẫn bình thường. Đây là clue control plane write path lỗi chứ không phải data plane outage.

Kiểm tra API request latency theo verb, admission webhook latency/error, etcd/storage, controller client retry. Nếu một validating webhook mới deploy có latency 8–10 giây và mọi create/update đều đi qua nó, root layer khá rõ.

Mitigation có thể rollback/scope lại webhook theo policy; không nên restart application pods vì chúng không nằm trên failure path. Đây là giá trị của control-plane/data-plane separation trong reasoning.

## 22. Finalizer biến delete thành protocol, không phải một thao tác tức thời

Khi object có cleanup bên ngoài cluster — cloud database, load balancer, DNS record, volume hoặc secret — xóa API object ngay có thể làm mất dấu resource cần cleanup. Finalizer cho phép object đi vào trạng thái terminating trong khi controller hoàn tất side effect rồi mới cho deletion kết thúc.

Invariant là: **đừng xóa record điều phối trước khi hoàn tất cleanup bắt buộc**. Nhưng finalizer cũng tạo failure mode: controller chết, credential mất hoặc provider outage có thể làm object kẹt `Terminating` vô thời hạn.

Force-remove finalizer chỉ nên làm khi operator hiểu orphan nào có thể còn lại và recovery path là gì. “Xóa được object” không đồng nghĩa external resource đã biến mất.

## 23. Owner reference và garbage collection encode lifecycle graph

Kubernetes có object graph: Deployment sở hữu ReplicaSet, ReplicaSet sở hữu Pod. Owner reference cho garbage collector biết resource con có lifecycle gắn với owner nào.

Đây là khác biệt với label/selector. Label thể hiện quan hệ chọn động; owner reference thể hiện ownership/lifecycle. Dùng nhầm hai khái niệm dẫn tới bug như resource con không được cleanup hoặc bị xóa ngoài ý muốn.

Operator tự viết cần nghĩ ownership graph trước khi create child resource. Nếu một external resource không thể biểu diễn bằng owner reference, controller phải tự giữ mapping/identity đủ bền để reconcile/delete an toàn.

## 24. Leader election giảm duplicate active controller nhưng không tự tạo fencing

Nhiều replica controller thường dùng lease/leader election để chỉ một instance active cho một responsibility nhất định. Nhưng network partition, pause dài hoặc delayed actor có thể tạo thời điểm old leader vẫn tiếp tục side effect dù lease đã mất.

Với action chỉ ghi Kubernetes API, optimistic concurrency có thể giúp reject stale write. Với external system không kiểm tra fencing token, leader election một mình có thể chưa đủ cho operation nguy hiểm.

Đây là boundary nơi DevOps nên chuyển sang [leases, fencing và split-brain](../../computer_science/06_networks_distributed_systems/advanced/02_leases_fencing_tokens_and_split_brain_prevention.md). Operational lesson là: **“có leader election” không tự chứng minh side effect external không thể bị duplicate/stale actor thực hiện**.

## 25. Informer cache tăng scale nhưng tạo staleness cần được chấp nhận có chủ đích

Controller thường đọc từ local cache/informer thay vì gọi API server trực tiếp cho mọi reconcile. Điều này giảm load và latency, nhưng cache có thể chậm hơn authoritative API state một khoảng ngắn.

Controller vì vậy phải được viết theo eventual reconciliation, không dựa vào assumption “vừa ghi xong thì cache chắc chắn đã thấy ngay”. Nếu một invariant cần read-after-write mạnh hơn, có thể phải dùng response của write, direct read có chọn lọc hoặc generation/resourceVersion logic phù hợp.

Nhiều bug controller xuất hiện khi developer vô tình trộn semantics của cache với semantics của database transaction.

## 26. Status condition phải là machine-readable contract, không phải log mini

Một CRD có `status.message = "something failed"` chưa đủ cho automation. Condition tốt nên có type ổn định, boolean/status, reason có taxonomy hữu hạn, observed generation và timestamp hữu ích.

Consumer cần phân biệt failure transient với terminal-invalid-spec; degraded nhưng usable với not-ready; dependency pending với policy denied. Nếu mọi lỗi đều thành `Ready=False`, platform user phải đọc controller log để hiểu abstraction — contract đã rò.

Status nên trả lời “controller đã observe intent nào, invariant nào đang đạt, invariant nào chưa và vì lý do loại nào”. Chi tiết dài vẫn có thể ở event/log.

## 27. CRD schema evolution là API evolution thật sự

CRD không chỉ là YAML tùy ý. Khi nhiều client/controller dùng nó, field rename, default thay đổi, semantic đổi hoặc version conversion sai đều có thể phá production.

Một version mới cần compatibility strategy: field cũ được giữ/deprecate bao lâu, default cũ/new khác nhau thế nào, object stored version nào, conversion có reversible không và controller nào support version nào.

Nếu conversion webhook nằm trên API read/write path, availability của nó cũng trở thành control-plane dependency. Platform CRD vì vậy cần cùng discipline versioning/canary/rollback như public API.

## 28. Control-plane fairness cần bảo vệ request quan trọng khi overload

Không phải API request nào có cùng giá trị. Health/control traffic, scheduler/controller action và bulk automation có thể tranh cùng control-plane capacity. Nếu một client gửi burst list/update lớn, request critical có thể bị queue dài.

Operational reasoning nên phân loại caller/verb/resource và xem queue/rejection theo class khi control plane pressure. Rate limit phía client, bounded concurrency và ưu tiên/fairness ở API path giúp tránh noisy automation làm toàn cluster mất khả năng điều khiển.

Điều này nối Kubernetes với multi-tenancy: fairness của shared control plane là reliability contract, không chỉ tuning performance.