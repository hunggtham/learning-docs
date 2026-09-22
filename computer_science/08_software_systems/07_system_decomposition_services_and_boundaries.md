# System decomposition, services và boundaries

Một system lớn phải được chia để con người, runtime và organization có thể quản lý complexity. Nhưng mỗi boundary cũng tạo serialization, latency, versioning, authorization, observability và partial-failure cost. Architecture tốt không tối đa số services; nó đặt boundaries nơi **invariants, state ownership và rate of change** có thể được quản lý tương đối độc lập.

Mental model trung tâm là: **mỗi boundary là một contract + ownership boundary + failure boundary + capacity boundary**. Tách một function thành remote service chỉ hợp lý khi lợi ích ownership/independent evolution lớn hơn coordination cost mà distribution tạo ra.

## 1. Bài toán ban đầu: complexity phải được partition, nhưng không thể biến mất

Nếu mọi code/data nằm trong một khối không có internal structure, thay đổi nhỏ có blast radius lớn và team khó reasoning. Nếu tách quá nhỏ, complexity chuyển thành network calls, schemas, retries, deployments và coordination giữa teams.

Ta luôn trả complexity ở đâu đó:

```text
inside module/process
hoặc
across API/network/team boundaries
```

System Design là chọn **nơi complexity rẻ nhất để sở hữu**, không phải xóa complexity.

## 2. Invariant trước boundary

Trước khi vẽ services, hãy viết invariants:

```text
order chỉ được charge một lần
inventory không âm
user chỉ đọc data tenant của mình
after success, write survive failure model X
schema producer/consumer coexist trong deployment window
```

State cần coordination mạnh để giữ cùng invariant thường là signal rằng ownership nên gần nhau. Nếu tách hai services nhưng mọi operation vẫn cần distributed transaction giữa chúng, boundary có thể đang cắt xuyên invariant sai chỗ.

## 3. Module trước microservice

Modularity là principle; microservice là deployment/distribution choice.

Một modular monolith có thể có:

```text
clear package/module boundaries
private state
stable internal contracts
independent ownership at code level
```

mà không trả network/TLS/retry/serialization cost cho mọi call.

Distribution nên được chọn khi cần independent deployment/scaling/failure isolation/organizational autonomy đủ mạnh để bù overhead.

## 4. Cohesion và coupling phải đo bằng change, data và runtime interaction

High cohesion nghĩa responsibilities/invariants thay đổi cùng nhau. Low coupling nghĩa components không cần biết internal details hay coordinate thường xuyên.

Coupling không chỉ imports:

```text
shared database schema
shared release train
chatty synchronous calls
shared cache key semantics
shared config/control plane
shared business transaction
one team blocks another for every change
```

Architecture diagram có thể “microservices” nhưng operationally vẫn là distributed monolith.

## 5. Bounded context là semantic boundary, không phải table boundary

Trong Domain-Driven Design, bounded context xác định nơi model/terms có meaning nhất quán. `Customer` trong Billing có thể khác `Customer` trong Support.

Boundary hữu ích khi semantics + invariants + ownership khác. Tách mỗi entity/table thành service thường mechanical và tạo remote joins/chatty CRUD.

Một capability boundary tốt trả lời:

```text
state nào thuộc authority này?
rule nào chỉ authority này được thay đổi?
contract nào bên ngoài được phép thấy?
```

## 6. State ownership mạnh hơn code ownership

Nếu service A “owns” code nhưng service B trực tiếp update tables của A, ownership không thật.

Shared database trap tạo hidden coupling:

```text
schema migration requires coordinated deployment
service B can violate invariant of A
query load of B impacts latency of A
rollback/versioning intertwined
```

Một service owning data qua contract làm authority rõ hơn, nhưng không nghĩa mọi read phải synchronous RPC. Read models, replicated views, cache hoặc event-fed projections có thể giảm coupling nếu consistency contract phù hợp.

## 7. Remote boundary làm xuất hiện partial failure

Local function call thường có outcome trực tiếp hơn. Remote call có states:

```text
request never sent
sent but server never received
server executed but response lost
server committed side effect then client timed out
response delayed while client retries
```

Do đó distribution thêm requirements:

```text
timeout/deadline
retry classification
idempotency
request identity
cancellation semantics
observability
```

Chia service phải budget cả correctness cost này.

## 8. Synchronous boundary đưa downstream vào critical path

Synchronous call dễ reasoning cho immediate result nhưng caller latency/availability phụ thuộc callee.

Một chain:

```text
A → B → C → D
```

có deadline, queue và retry ở nhiều hops. Fan-out còn khuếch đại tail latency.

Nếu invariant thật sự cần immediate decision, sync có thể đúng. Nếu không, asynchronous boundary có thể giảm temporal coupling.

## 9. Asynchronous boundary đổi coupling chứ không xóa coupling

Event/message giúp producer không chờ consumer availability ngay lúc publish, nhưng consumer phụ thuộc schema/semantics/order/delivery contract.

New failure modes:

```text
duplicate delivery
out-of-order
consumer lag
poison message
schema mismatch
replay side effect
unbounded backlog
```

Event-driven không tự “decoupled”; coupling chuyển từ call-time availability sang **protocol + state evolution + operations**.

## 10. Saga là distributed state machine, không phải rollback nhiều database

Workflow xuyên services có thể dùng local transactions + messages/compensation.

Compensation không quay time. Gửi hàng rồi “undo” có thể là return/refund workflow với real-world state mới.

Một saga cần explicit:

```text
state transitions
idempotency key
retry policy
compensation rule
irreversible step
manual intervention state
observability/correlation
```

System Design phải xem saga như durable state machine, không chỉ pattern name.

## 11. API contract phải bao gồm behavior, không chỉ schema

Contract gồm hơn JSON fields:

```text
meaning/units
idempotency
ordering
error taxonomy
pagination consistency
timeout expectations
rate/cost limits
backward/forward compatibility
security principal semantics
```

Hai services compile với cùng protobuf/OpenAPI nhưng hiểu semantics khác vẫn có contract bug.

Đọc [schema/protocol evolution](./advanced/06_schema_protocol_evolution_and_compatibility_contracts.md).

## 12. Capacity boundary phải nằm gần resource hữu hạn

Mỗi service có pools/queues/CPU/memory/storage/downstream limits. Nếu caller có thể tạo unlimited concurrency vào resource giới hạn, service boundary không bảo vệ dependency.

Useful invariant:

> Accepted work không được vượt capacity khiến useful completion trước deadline collapse.

Mechanism: bounded queues, semaphore, admission control, per-tenant quota, backpressure, load shedding.

System Design không chỉ vẽ boxes; nó phải chỉ ra **queue nằm đâu và ai chịu trách nhiệm reject khi full**.

## 13. Multi-tenant boundary cần fairness semantics

Nếu tenants share pool/cache/database, architecture phải quyết định isolation level:

```text
best effort shared
weighted fair
reserved capacity
hard quota
physical separation
```

Tách service không tự tạo tenant isolation nếu backend resource vẫn shared. Noisy-neighbor behavior thường leak từ lower layer như DB connection pool hoặc storage IOPS.

## 14. Security principal đổi ở boundary nào?

North-south request có end-user identity; east-west service call có workload identity; service có thể act on behalf of user hoặc bằng own authority.

Boundary cần explicit:

```text
caller principal là ai?
user context nào được delegated?
service authority nào được dùng?
authorization ở đâu?
credential/secret nào mở downstream capability?
```

Nếu backend chỉ tin header `role=admin` từ gateway mà direct path tồn tại, architecture security boundary sai dù business code đúng.

Đọc [Security boundaries](../07_security_reliability/advanced/00_security_boundaries_attack_chains_and_exploitability.md).

## 15. API gateway và service mesh là policy/runtime layers, không phải dây dẫn trong suốt

Gateway có thể route, auth, rate-limit, retry, cache, transform headers. Mesh/data plane có thể mTLS, retries, load balancing, telemetry.

Mỗi feature thêm queue, state và failure mode. Nếu proxy retry và application cũng retry, load amplification có thể nhân.

Centralized policy giúp consistency nhưng tạo shared dependency; observability phải cho thấy work đã chờ hoặc bị retry ở proxy chứ không chỉ application.

## 16. Data locality và network locality thuộc cùng design

Tách compute khỏi data làm remote access. Chatty service gọi DB/service khác cho từng field có thể biến local memory call thành nhiều RTT.

Boundary nên cân:

```text
data ownership
read locality
write invariant
cacheability
replication freshness
cross-region traffic
```

Independent deployment không đáng nếu mọi request vẫn phải synchronous round-trip qua nhiều owners để assemble trivial state.

## 17. Multi-region decomposition phải phân loại operation theo coordination need

Không phải mọi write cần global consensus. Hãy phân loại:

```text
must preserve global invariant
region-local authority enough
read-your-writes required
stale read acceptable
asynchronous merge acceptable
```

Sau đó chọn placement/replication. Global strong path cho mọi operation trả latency/capacity cost; eventual-everything lại có thể phá business invariant.

Đọc [multi-region replication](../06_networks_distributed_systems/advanced/05_multi_region_replication_and_geo_distributed_tradeoffs.md).

## 18. Cost model phải gồm coordination cost

System Design interview/production thường hỏi QPS/storage nhưng bỏ coordination overhead.

Capacity estimate nên ít nhất cover:

```text
request rate × fan-out
retry/hedge amplification
payload × replication factor
cache hit/miss path
peak/burst not only average
cross-region egress/RTT
per-tenant skew
background jobs/backfill/replay
```

Một design “10k QPS” có thể tạo 100k downstream attempts nếu mỗi request fan-out 5 và retry 2 tầng.

## 19. Failure domains phải được vẽ, không giả định từ box count

Hai services ở two pods nhưng cùng node/database/KMS/control plane có shared failure. Three regions nhưng same global identity issuer có correlated dependency.

Availability reasoning cần dependency graph:

```text
compute
network
storage
control plane
identity/KMS
schema/config rollout
human/operator workflow
```

Redundancy chỉ có giá trị với failure mode độc lập tương ứng.

## 20. Deployment boundary và data boundary có thể khác

Một code rollout có thể rollback binary, nhưng schema/data mutation có thể irreversible. Feature flag chỉ reversible nếu old path còn hiểu state mới.

System Design cần cùng Software Engineering xác định compatibility window và migration state, không xem deployment là external concern.

Đọc [large-scale migration](../09_software_engineering/advanced/03_large_scale_refactoring_strangler_and_branch_by_abstraction.md).

## 21. Conway's Law và ownership queue

System communication thường phản chiếu organization communication. Nếu một service cần approval từ team khác cho mọi thay đổi, “independent service” không independent về lead time.

Architecture decision cần xem:

```text
who owns on-call?
who owns schema/API?
who can deploy independently?
who resolves incident across boundary?
```

Poor socio-technical boundary tạo coordination queue giống runtime queue: work chờ người khác trước khi flow tiếp.

## 22. Distributed monolith là failure mode có dấu hiệu đo được

Dấu hiệu:

```text
services deploy together
shared DB writes
chatty synchronous chains
cross-team changes bắt buộc
one service outage cascades fleet-wide
contract/version changes lock-step
```

Tách thêm services không chữa; thường cần gom invariant lại hoặc thiết kế ownership/protocol đúng hơn.

## 23. Production evidence phải theo boundary

Evidence cho architecture không chỉ infra dashboard. Cần:

```text
call graph/fan-out
per-boundary latency + queue wait
retry/attempt amplification
error taxonomy
data/replica freshness
schema/version distribution
per-tenant resource use
change/deploy coupling
incident blast radius
```

Một service map đẹp nhưng traces cho thấy 40 synchronous calls/request là evidence boundary cost đang cao.

## 24. Boundary review checklist theo invariant

Trước khi tách/giữ service, hỏi:

```text
Invariant nào nằm trong boundary?
State authority ở đâu?
Remote failure tạo outcome ambiguity nào?
Queue/admission ở đâu?
Security principal đổi thế nào?
Schema/version coexist ra sao?
Data locality/replication ra sao?
Failure domain có thật sự khác?
Team có sở hữu độc lập được không?
Evidence nào chứng minh boundary tốt hơn hiện tại?
```

Nếu không trả lời được, technology choice còn quá sớm.

## Common Misconceptions

**“Microservices scale tốt hơn monolith.”** Một monolith stateless vẫn horizontal scale; microservices chủ yếu cho independent scaling/ownership/failure isolation khi boundary đúng.

**“Mỗi table nên là một service.”** Table là storage representation; service boundary nên theo invariant/capability/ownership.

**“Event-driven nghĩa decoupled.”** Coupling chuyển sang event semantics, lag, replay và schema evolution.

**“Service mesh giải reliability.”** Nó có thể cung cấp mechanism, nhưng retry/timeout/admission policy sai vẫn tạo cascading failure.

**“Nhiều regions nghĩa highly available.”** Chỉ đúng với failure domains/dependencies thật sự independent và failover capacity đủ.

## 25. Mô hình tư duy

> System Design là bài toán **đặt authority, invariants, queues và failure boundaries**. Module/service boundary tốt gom state cần coordination và cho phần còn lại evolve độc lập. Distribution chỉ đáng khi autonomy/scaling/isolation lợi hơn network/protocol cost. **Bắt đầu bằng invariant + workload + failure model + evidence; technology là implementation của những contract đó.**

## Kết nối

Đọc [modularity/API](./00_abstraction_modularity_interfaces_and_apis.md), [performance/capacity](./02_performance_capacity_and_scalability.md), [state/queues/backpressure](./03_state_queues_backpressure_and_boundaries.md), [event-driven](./06_event_driven_and_stream_processing.md), [queueing advanced](./advanced/00_queueing_tail_latency_and_backpressure.md), [distributed consistency](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md), [Security boundaries](../07_security_reliability/advanced/00_security_boundaries_attack_chains_and_exploitability.md), [software architecture](../09_software_engineering/01_software_architecture_and_design_reasoning.md) và [end-to-end request path](../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).