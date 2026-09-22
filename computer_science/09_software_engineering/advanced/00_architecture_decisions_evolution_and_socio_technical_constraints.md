# Architecture decisions, evolution và socio-technical constraints

Advanced software architecture không phải thuộc nhiều pattern hơn. Nó là khả năng chọn boundary và trade-off phù hợp với **workload, invariant, rate of change, failure domain, ownership, data consistency, deployment topology và organizational communication**.

System Design cũng không phải ghép các hộp “load balancer + cache + queue + database”. Một thiết kế tốt bắt đầu từ property hệ thống phải giữ, pressure mà nó phải chịu, failure nào được phép, rồi mới chọn topology và technology.

## 1. Architecture là tập constraints trên thay đổi và failure

Một architecture tốt làm một số thay đổi dễ và một số thay đổi khó có chủ đích. Module boundary tốt cho phép implementation bên trong đổi mà consumer không cần biết chi tiết. Failure boundary tốt ngăn một component bị lỗi kéo cả system sập.

Do đó đánh giá architecture phải hỏi hai loại scenario:

```text
change scenario:
- thêm field/protocol mới
- thay storage engine
- chia team/ownership
- deploy version mới

failure scenario:
- downstream chậm
- region mất
- credential compromise
- DB lag/lock
- cache outage
```

Diagram tĩnh không đủ để trả lời behavior dưới change/failure.

## 2. Bắt đầu từ invariant, không bắt đầu từ component

Ví dụ một payment system có thể có invariant:

```text
một payment intent không bị charge hai lần
successful charge phải có audit trail
caller timeout không được làm mất khả năng xác định outcome
```

Từ đây mới suy ra idempotency key, state machine, durable log/outbox, retry semantics và reconciliation.

Nếu bắt đầu bằng “dùng Kafka hay RabbitMQ?”, ta đang chọn implementation trước khi biết property cần giữ.

## 3. Quality attributes tạo trade-off thật

Latency, availability, consistency, security, operability, modifiability và cost thường xung đột.

Tách service có thể scale/deploy độc lập nhưng thêm:

```text
network partial failure
serialization/schema evolution
cross-service tracing
retry/idempotency
cross-service data consistency
more operational surfaces
```

“Microservices scalable hơn” là statement quá thô. Cần hỏi scale **resource nào**, failure boundary nào và coordination cost nào.

## 4. Workload model là input kiến trúc

Thiết kế cho 100 RPS đều khác 100k RPS bursty; 99% read khác write-heavy; object 1 KB khác 100 MB; global users khác single region.

Workload model nên gồm:

```text
arrival distribution, không chỉ average
read/write ratio
request/service-time distribution
object/data size
hot-key/skew
consistency/durability requirement
retention/growth
failure/recovery target
```

System Design không có meaning nếu assumptions workload không được nói rõ.

## 5. Bottleneck resource quyết định topology hữu ích

Scale-out application nodes không tăng capacity nếu bottleneck là shared database lock, storage IOPS hoặc third-party quota.

Mỗi scale decision nên hỏi:

```text
resource nào đang giới hạn throughput?
request giữ resource đó bao lâu?
resource có partition được không?
partition key có tạo hot spot không?
queue nằm đâu trước resource?
```

Điều này nối trực tiếp system design với [capacity/admission control](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md).

## 6. State placement là decision trung tâm

Stateless compute dễ replicate nhưng application thực tế luôn có state ở đâu đó: database, cache, object store, queue, session, local filesystem hoặc external service.

State placement quyết định:

```text
failure/recovery behavior
consistency boundary
deployment coupling
migration difficulty
latency/locality
backup/retention
```

“Stateless service” chỉ có nghĩa state được đẩy sang boundary khác, không phải state biến mất.

## 7. Data ownership và transaction boundary phải khớp invariant

Hai services có API riêng nhưng cùng sửa tables của nhau chưa có data autonomy. Ngược lại, tách database chỉ để đạt purity có thể tạo saga/eventual-consistency complexity không cần thiết.

Nếu hai facts phải commit atomically rất thường xuyên vì cùng business invariant, việc tách chúng qua network có thể đang cắt sai aggregate boundary.

Boundary nên được chọn từ **ownership + invariant + change rate**, không từ sơ đồ tổ chức mong muốn đơn lẻ.

## 8. Synchronous call tạo temporal coupling

Service A gọi B synchronously nghĩa A's latency/availability phụ thuộc B trong request window.

Async queue/event có thể giảm temporal coupling nhưng tạo semantic complexity mới:

```text
delivery duplicate
ordering
backlog
consumer lag
schema evolution
reconciliation
```

Không có “async = resilient” tự động. Nó đổi failure shape từ request timeout sang backlog/state convergence.

## 9. Queue là state và debt

Queue hấp thụ mismatch tạm thời giữa producer/consumer, nhưng queue dài là outstanding work phải trả sau.

System Design cần định nghĩa:

```text
max backlog?
deadline/TTL của message?
poison message?
retry/DLQ semantics?
consumer recovery rate > arrival rate sau outage không?
```

Nếu recovery throughput chỉ bằng arrival throughput, backlog sau incident không bao giờ được trả.

## 10. Cache là consistency decision

Cache không chỉ “giảm DB load”. Nó tạo replica state và freshness contract.

Khi thiết kế cache, hỏi source of truth, staleness tolerance, invalidation ordering, hot-key behavior và origin capacity khi cache fail.

Xem [Caching consistency](../../08_software_systems/advanced/02_caching_consistency_invalidation_stampede_and_hot_keys.md).

## 11. Failure domain phải cụ thể

“Highly available” không đủ. Cần nói survive cái gì:

```text
process crash?
node loss?
AZ/rack loss?
region loss?
control-plane outage?
operator error?
credential compromise?
```

Replication trong cùng rack không bảo vệ rack failure. Multi-region replication không bảo vệ bad write đã replicate. Backup không giúp request availability ngay lập tức.

Reliability design phải map mechanism vào failure model cụ thể.

## 12. Retry policy là architecture, không phải client helper

Retry thay đổi load và side-effect semantics toàn call graph. Proxy, SDK và application cùng retry có thể nhân attempts ngoài dự kiến.

Architectural review cần biết tầng nào được retry, budget bao nhiêu, operation có idempotent không, deadline còn bao nhiêu và overload feedback loop được chặn ở đâu.

Xem [end-to-end request + overload](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).

## 13. Security boundary cũng là architecture boundary

Identity đổi khi request đi qua browser → edge → service → database/KMS. TLS termination, token exchange hoặc proxy header đều thay trust model.

Architecture review phải hỏi:

```text
principal ở mỗi hop là ai?
authorization nằm ở đâu?
secret/capability scope là gì?
compromise một service lan được tới đâu?
```

Security không phải checklist thêm sau topology; trust graph là một phần topology.

## 14. Reversibility quyết định mức đầu tư decision

Decision dễ đảo như local cache library nên thử nhanh. Decision khó đảo như partition key, public protocol, identity model hoặc data ownership cần nhiều evidence hơn.

ADR hữu ích khi ghi:

```text
context + invariant
assumptions/workload
alternatives
chosen trade-off
failure consequences
revisit trigger
```

ADR là snapshot reasoning, không phải bằng chứng decision sẽ đúng mãi.

## 15. Migration path quan trọng hơn target diagram

Production architecture hiếm khi rewrite một lần. Safe evolution thường cần:

```text
old system
→ compatibility seam
→ dual-read/replication/backfill có kiểm soát
→ verify equivalence
→ shift traffic
→ retire old path
```

Dual-write nguy hiểm nếu thiếu idempotency/reconciliation. Backfill có thể phá production capacity. Migration design phải có observability và rollback/roll-forward story.

## 16. Compatibility là distributed protocol theo thời gian

Khi old/new binaries cùng chạy, API/schema/data phải hợp lệ trong overlap window.

Deployment topology vì thế biến compatibility thành distributed constraint. “Code mới compile” không chứng minh mixed-version fleet hoạt động đúng.

Expand-contract và tolerant reader/writer strategies nên được reasoning từ coexistence window cụ thể.

## 17. Conway's Law là coupling giữa communication graph và software graph

Nếu hai teams phải thay cùng component liên tục nhưng ownership tách rời, coordination cost trở thành architecture reality. Nếu service boundaries cắt qua capability sai, system có chatty network calls và cross-team transactions.

Socio-technical design nhìn code graph, data graph và communication graph cùng lúc.

Một monolith modular có thể ít coupling hơn một fleet microservices phải release đồng bộ.

## 18. Architecture review nên dùng stress/failure scenarios

Thay vì hỏi “có clean architecture không?”, dùng scenarios:

```text
traffic 10x trong 5 phút
DB p99 tăng 20x
cache mất toàn cluster
region A mất
schema N+1 deploy khi N vẫn chạy
client retry sau timeout
credential service A bị compromise
storage flush latency spike
```

Scenario buộc design reveal hidden assumptions, queues và failure propagation.

## 19. Production evidence phải kiểm chứng assumption

Architecture không chỉ tồn tại trong document. Các assumption cần metrics/traces/logs hoặc tests:

```text
actual traffic/skew
queue wait và saturation
dependency critical path
failure injection result
replication/recovery lag
schema/version compatibility errors
security policy decisions
cost per workload unit
```

Nếu ADR nói “cache outage không ảnh hưởng origin” nhưng chaos test làm DB sập, architecture evidence đã phủ định assumption.

## 20. Lower abstraction nào thực sự quyết định behavior?

Một architecture diagram có thể nói “database durable”, nhưng guarantee cuối phụ thuộc WAL/filesystem/storage. Diagram nói “service isolated”, nhưng cgroup/DB pool/shared KMS có thể là hidden shared fate. Diagram nói “secure mTLS”, nhưng authorization policy có thể vẫn allow-all.

Advanced system design luôn hỏi: abstraction nào bên dưới thực sự giữ property đang hứa?

## 21. Mô hình tư duy

> Architecture là **thiết kế invariant, cost-of-change và failure boundaries dưới workload + organizational constraints**. System Design bắt đầu từ properties và pressure, không từ technology boxes. Pattern là vocabulary; decision quality đến từ explicit assumptions, bottleneck model, failure scenarios, migration path và production evidence.

## Kết nối

Đọc cùng [System decomposition foundation](../../basic/08_software_systems/07_system_decomposition_services_and_boundaries.md), [Distributed consistency](../../06_networks_distributed_systems/advanced/06_time_clocks_ordering_and_causality.md), [Capacity engineering](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md), [Security containment](../../90_connections/advanced/00_debugging_across_abstraction_layers.md) và [Deployment safety](./05_deployment_safety_canary_blue_green_flags_and_rollback.md).