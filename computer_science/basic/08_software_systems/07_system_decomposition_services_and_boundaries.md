# System decomposition, services và boundaries

Một system lớn phải được chia nhỏ vì một team hay một process không thể giữ toàn bộ complexity trong đầu. Nhưng mỗi boundary mới cũng tạo communication, versioning, security, latency và failure cost. **System design** vì vậy không phải chọn pattern hoặc công nghệ theo catalogue; nó là bài toán đặt ownership và failure boundaries sao cho invariant quan trọng vẫn được giữ khi load, failure và organizational change xuất hiện.

Câu hỏi đúng không phải “monolith hay microservices?”. Câu hỏi là: **state/invariant nào thuộc về ai, consistency nào cần giữ, failure nào được phép lan qua boundary, và evidence nào cho biết boundary đang hoạt động đúng?**

## 1. Boundary chỉ có giá trị khi nó gom ownership rõ

Một module/service hữu ích khi nó sở hữu một nhóm state và rules thay đổi cùng nhau. Nếu hai services phải cùng deploy mỗi lần, cùng sửa một schema và cùng debug một transaction, boundary vật lý không tạo autonomy thật.

Mental model:

```text
boundary tốt
= ownership rõ
+ contract rõ
+ failure semantics rõ
+ change có thể tương đối độc lập
```

Chia nhỏ vì “mỗi service khoảng 1.000 dòng” hoặc “mỗi table một service” không tạo mental model tốt.

## 2. Module trước distributed boundary

Modularity là principle; microservice chỉ là một deployment form. Một modular monolith có thể có strong boundaries mà không chịu network, serialization, timeout, retry và partial failure cost.

Khi đổi một function call thành remote call, ta thêm ít nhất:

```text
network latency
connection management
serialization/protocol compatibility
timeout/retry
authentication/authorization
partial failure
observability context propagation
```

Do đó distributed boundary phải “kiếm được quyền tồn tại” bằng independent scaling, ownership, failure isolation hoặc deployment/evolution benefit đủ lớn.

## 3. Cohesion và coupling phải đo bằng change/failure, không chỉ import graph

High cohesion nghĩa responsibilities thực sự thay đổi cùng nhau. Low coupling nghĩa component ít assumptions về internals của nhau.

Coupling có nhiều dạng:

```text
code coupling        -> imports/internal API
schema coupling      -> cùng database/table format
temporal coupling    -> caller phải đợi callee sống ngay lúc đó
release coupling     -> phải deploy cùng nhau
semantic coupling    -> cùng hiểu một event/field theo assumptions ngầm
operational coupling -> cùng quota/control plane/failure domain
```

Một architecture có repository tách biệt vẫn có thể coupled mạnh ở runtime.

## 4. Bounded context là semantic boundary

Trong Domain-Driven Design, bounded context xác định nơi một model và vocabulary có meaning nhất quán. `Customer` trong billing có thể cần credit/payment identity; `Customer` trong support có thể cần contact/history.

Boundary tốt thường đi theo **business invariant** hơn là entity CRUD. Nếu invariant “một order chỉ được settle một lần” thuộc payment/order workflow, cần biết authority nào quyết định transition đó.

System design bắt đầu từ invariant ownership chứ không từ boxes trên diagram.

## 5. State placement quyết định architecture nhiều hơn compute placement

Stateless application replicas dễ scale vì request có thể chạy ở nhiều nodes. Nhưng durable state, cache, session, locks và coordination vẫn phải sống ở đâu đó.

Khi thiết kế, hỏi:

```text
source of truth ở đâu?
ai được ghi?
reader cần freshness mức nào?
state có partition được không?
failover có giữ authority không?
cache có thể stale trong bao lâu?
```

Nhiều architecture failure là state-ownership problem bị che dưới “service topology”.

## 6. Shared database làm ownership mơ hồ

Nếu nhiều services trực tiếp mutate cùng tables, transaction boundary có thể tiện nhưng domain ownership trở nên mơ hồ. Schema change cần coordination; service B có thể phá invariant service A.

Không phải shared database luôn sai. Nhưng cần biết contract: tables nào thật sự shared, ai sở hữu migration, write paths nào hợp lệ và isolation/failure semantics ra sao.

Tách database per service cũng không tự động tốt nếu kết quả là hàng chục synchronous remote reads cho một request đơn giản.

## 7. Synchronous boundary thêm availability và latency dependency

Synchronous request/response dễ hiểu khi caller cần kết quả ngay. Nhưng caller latency ít nhất phụ thuộc critical path của callee; availability của caller cũng có thể bị kéo xuống nếu callee fail và fallback không có.

Một chain dài:

```text
A → B → C → D
```

có thể tạo cumulative latency, retry amplification và cascading failure. Timeout budget phải propagate thay vì mỗi hop tự đặt một timeout đầy đủ mới.

Synchronous call không xấu; nó chỉ tạo **temporal coupling** cần được budget rõ.

## 8. Asynchronous boundary đổi coupling chứ không xóa coupling

Event/message giúp producer không cần consumer available tức thời. Nhưng ta thêm queue state, delivery semantics, replay, ordering và eventual consistency.

Questions cần trả lời:

```text
event là fact hay command?
at-least-once có tạo duplicate không?
consumer xử lý idempotent không?
partition/order key là gì?
backlog lớn thì freshness/SLO ra sao?
schema evolve thế nào khi nhiều consumer versions cùng tồn tại?
```

Event-driven architecture không tự decoupled. Nó chuyển coupling từ call-time sang schema/semantic/time-history coupling.

## 9. Consistency requirement phải xuất phát từ invariant business

Không phải mọi data cần strong consistency. Nhưng “eventual consistency” cũng không phải default excuse.

Ví dụ product catalog có thể chấp nhận giá hiển thị stale vài giây trong một context, nhưng payment ledger có thể cần stronger serialization/idempotency guarantees.

Trước khi chọn replication/cache/event architecture, viết:

```text
state nào không được mâu thuẫn?
violation window tối đa bao lâu?
ai có authority quyết định state?
conflict có thể merge hay phải reject/serialize?
```

Consistency là product/domain property trước khi là database feature.

## 10. Saga và compensation không phải rollback phân tán

Workflow qua nhiều services thường dùng local transactions + messaging. **Saga** có thể orchestrate hoặc choreograph steps và compensation.

Compensation là business action mới, không phải time machine. Nếu hàng đã giao, compensation có thể là return/refund; email đã gửi không thể “unsend” một cách transactionally.

Invariant phải được thiết kế cho intermediate states. User có thể thấy `PAYMENT_CAPTURED, SHIPMENT_PENDING`; system cần recovery/reconciliation thay vì giả định atomicity toàn cầu.

## 11. Idempotency là boundary invariant khi retry/duplicate có thể xảy ra

Network timeout tạo ambiguity: request có thể đã được server thực hiện nhưng response bị mất. Retry có thể lặp side effect.

Idempotency key/deduplication giúp cùng logical operation không bị áp dụng nhiều lần theo policy. Nhưng storage/lifetime của dedupe record, key scope và response replay semantics phải được định nghĩa.

“HTTP PUT idempotent” ở protocol level không tự chứng minh business side effects bên dưới idempotent.

## 12. Queue là state và debt

Message broker, thread queue hoặc async job queue không chỉ là transport. Queue chứa work chưa hoàn thành — một dạng debt.

Khi producer rate vượt consumer service rate:

```text
backlog tăng
→ processing lag tăng
→ data freshness giảm
→ deadline có thể hết trước khi xử lý
→ recovery time sau incident kéo dài
```

Backpressure/admission control cần đặt ở nơi producer nhận được capacity signal. Queue vô hạn chỉ trì hoãn failure.

## 13. Cache là một replicated state system nhỏ

Cache làm read path nhanh nhưng tạo copy state ngoài source of truth. Cần định nghĩa freshness, invalidation, stampede behavior và failure fallback.

Nếu cache outage khiến toàn traffic đập vào database, cache đã trở thành **load-bearing dependency**. Capacity plan phải xét cache miss storm, không chỉ normal hit ratio.

Cache design vì vậy là system design, consistency và reliability cùng lúc.

## 14. Partitioning tăng capacity nhưng tạo hotspot và cross-partition cost

Sharding chia state/work theo key để tăng horizontal capacity. Nhưng shard key quyết định locality và balance.

Một celebrity tenant/hot key có thể phá assumption uniform distribution. Cross-shard query/transaction thêm coordination. Rebalancing cần move state trong khi traffic vẫn chạy.

Không nên nói “system horizontally scalable” nếu chưa biết unit partition và hotspot strategy.

## 15. Replication tăng availability/read scale nhưng thêm authority problem

Replica chỉ hữu ích nếu protocol xác định ai được write, khi nào write committed và failover tránh split-brain.

Async replica có lag; read-after-write có thể fail nếu reader đi tới follower cũ. Sync quorum tăng consistency/durability nhưng thêm latency và giảm availability dưới partition nhất định.

Replication không phải copy count; nó là consistency protocol dưới failure model.

## 16. Load balancer và service discovery là control loops

Routing layer phải biết backend nào tồn tại, healthy và còn capacity. Health check quá nông có thể gửi traffic tới node sống process nhưng đang overload. Health data stale có thể tạo oscillation/hotspot.

Connection reuse cũng làm load balancing stateful: nhiều long-lived HTTP/2 connections có thể giữ traffic trên old subset nodes dù fleet đã scale.

Topology control là dynamic system, không chỉ round-robin algorithm.

## 17. API gateway/service mesh di chuyển cross-cutting logic xuống infrastructure

Gateway có thể centralize auth, rate limit, routing và observability cho north-south traffic. Service mesh có thể xử lý mTLS, retries, telemetry và routing east-west.

Lợi ích là policy consistency; cost là thêm proxies/control plane/failure modes. Nếu proxy tự retry và application cũng retry, load amplification tăng mà team khó nhìn thấy.

Infrastructure abstraction phải expose evidence đủ để debug, nếu không nó biến failure thành “network mystery”.

## 18. Security boundary phải đi cùng service boundary

Tách service mà mọi service tin cùng credential/root permission thì containment kém. Mỗi boundary nên xác định principal nào được gọi, action nào được phép và secret/key scope nào cần thiết.

mTLS chứng minh service identity không thay authorization. Network segmentation không thay application policy. Least privilege làm service decomposition trở thành incident-containment architecture.

Đọc [PKI/service identity](../../07_security_reliability/advanced/02_pki_certificate_validation_mtls_and_service_identity.md).

## 19. Failure domain phải explicit

Hai replicas cùng zone, cùng database, cùng KMS hoặc cùng deployment artifact có thể cùng fail. Architecture diagram chỉ vẽ nhiều boxes nhưng dependency graph vẫn có shared single point.

Khi thiết kế redundancy, hỏi:

```text
failure nào ta muốn survive?
replicas có độc lập trước failure đó không?
control plane có shared dependency nào?
failover path đã được test chưa?
```

“Multi-instance” không đồng nghĩa multi-failure-domain.

## 20. Graceful degradation cần giữ invariant quan trọng

Khi dependency fail, system có thể serve stale cache, bỏ recommendation, chuyển read-only hoặc reject optional work.

Nhưng không được degrade bằng cách bỏ authorization, double-charge hoặc trả committed success khi durability chưa đạt. Degradation phải phân biệt optional quality với correctness/security invariant.

Thiết kế fallback là product/system decision trước incident, không phải improvisation lúc outage.

## 21. Observability phải được thiết kế tại boundary

Mỗi remote boundary nên giữ causal context đủ để trả lời:

```text
caller nào?
principal nào?
attempt thứ mấy?
deadline còn bao nhiêu?
queue wait bao lâu?
downstream service time bao lâu?
version/schema nào?
```

Trace, metrics và structured logs cần gắn với contract. Nếu chỉ có CPU graph của từng service mà không có end-to-end context, distributed architecture làm debugging khó hơn rất nhiều.

## 22. Conway's Law và ownership là một phần của runtime architecture

System structure thường phản chiếu communication structure của organization. Nếu một service “owned” bởi ba teams và mọi change cần committee, service boundary không tạo autonomy.

Ngược lại, team boundary không nên ép tạo network service nếu module boundary trong monolith đã đủ.

Architecture là socio-technical: code, data, deploy, on-call và decision authority nên tương đối aligned.

## 23. Distributed monolith là failure mode của decomposition

Dấu hiệu:

```text
services deploy cùng lúc
shared DB writes everywhere
chatty synchronous calls
cross-service transaction assumptions
one failure cascades toàn graph
schema change cần coordinated rollout lớn
```

Ta nhận network/ops cost của distributed system nhưng vẫn giữ coupling của monolith.

Fix thường là làm boundary sâu hơn—ownership/contracts—không phải chia thêm services.

## 24. Performance pressure làm boundary behavior thay đổi

Ở low load, remote call cost có thể nhỏ. Gần saturation, mỗi boundary thêm queue, retry và connection-pool pressure. Fan-out khuếch đại tail latency; cache miss storm tạo load lên source; DB pool chuyển queue xuống storage/locks.

System design phải được load-test ở operating region thật. Architecture đúng về chức năng nhưng collapse dưới overload là architecture thiếu capacity/failure reasoning.

## 25. Evidence để đánh giá một boundary

Một boundary khỏe thường có evidence về:

```text
change/deploy independence
request/event volume và latency
error/timeout/retry rate
queue/backlog
schema compatibility failures
authorization decisions
resource saturation
dependencies/failure propagation
ownership/on-call clarity
```

Không phải mọi metric cần dashboard riêng. Nhưng nếu không thể biết boundary đang chờ gì, fail ở đâu và ai sở hữu state, architecture đang thiếu observability/ownership.

## 26. Decision framework thay vì pattern catalogue

Khi cần tách service hoặc chọn interaction model, reasoning sequence hữu ích là:

```text
1. invariant/state nào cần ownership?
2. change nào cần độc lập?
3. consistency/freshness requirement là gì?
4. expected load và partition key là gì?
5. failure nào phải contain/survive?
6. sync hay async phù hợp deadline và semantics?
7. security principal/trust boundary nằm đâu?
8. observability/evidence nào chứng minh contract?
9. operational complexity có đáng với benefit không?
```

Chỉ sau đó mới chọn queue, cache, database, gateway hay service mesh cụ thể.

## 27. Mô hình tư duy

> System design là **đặt ownership, state, communication và failure boundaries**. Boundary tốt gom invariant và authority rõ, có contract có thể evolve, giới hạn blast radius và có evidence khi behavior xấu. Boundary xấu chỉ chuyển function call thành network call rồi thêm timeout/retry mà không giảm coupling. Technology là implementation; invariant và failure model mới là kiến trúc.

## Những hiểu nhầm thường gặp

**“Microservices scale tốt hơn monolith.”** Chỉ khi bottleneck/workload thật sự partition được và boundary có independent capacity.

**“Event-driven nghĩa decoupled.”** Coupling chuyển sang event semantics, ordering, schema và backlog.

**“Nhiều replicas nghĩa high availability.”** Chỉ khi failure domains và authority/failover protocol phù hợp.

**“System design interview pattern là production architecture.”** Pattern chỉ hữu ích khi assumptions/invariant/failure model khớp system thật.

## Kết nối

Đọc [modularity/API](./00_abstraction_modularity_interfaces_and_apis.md), [state/queues/backpressure](./03_state_queues_backpressure_and_boundaries.md), [event-driven](./06_event_driven_and_stream_processing.md), [distributed consistency](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md), [capacity engineering](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md), [architecture decisions](../../09_software_engineering/advanced/00_architecture_decisions_evolution_and_socio_technical_constraints.md), [end-to-end request path](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md) và [debugging xuyên abstraction layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).