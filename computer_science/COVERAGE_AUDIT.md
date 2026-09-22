# Coverage Audit — Computer Science Canonical Library

Audit này đánh giá `computer_science/` theo **chiều sâu reasoning**, không theo số chapter. Một domain chỉ được xem là có coverage tốt khi người đọc có thể đi theo đường:

```text
foundation
→ internals
→ failure modes
→ performance / concurrency / consistency pressure
→ production evidence
→ cross-layer connections
```

Số file không phải mục tiêu. Trong vòng audit này, chapter trùng mental model đã được hợp nhất; các gap mới chủ yếu được hấp thụ vào canonical file hiện có thay vì tạo thêm chapter.

## 1. Tiêu chí chung

Một concept advanced được xem là đủ sâu khi có thể trả lời phần lớn các câu hỏi sau:

```text
Vấn đề ban đầu là gì?
Invariant nào cần được duy trì?
Internals giữ invariant bằng mechanism nào?
Assumption nào đang được dùng?
Failure xảy ra khi assumption nào mất hiệu lực?
Performance pressure làm behavior thay đổi ra sao?
Evidence nào giúp phân biệt các hypothesis?
Abstraction layer nào bên dưới thực sự quyết định behavior?
Fix nên đặt ở layer nào sở hữu invariant?
```

Một chapter chỉ liệt kê technology, API, annotation hoặc pattern mà không tạo thêm mental model không được tính là chiều sâu mới.

---

## 2. Computer Architecture — coverage: mạnh

Foundation đã có CPU/ISA/instruction cycle, memory hierarchy/cache, I/O/interrupt/DMA, ABI, multicore/SIMD/GPU, storage hardware và performance measurement.

Advanced hiện có đường reasoning rõ từ memory consistency/cache coherence tới OoO execution, speculation, cache hierarchy, NUMA, TLB và SIMD/GPU. Vòng audit đã hợp nhất duplicate OoO chapter và đào sâu hai chuỗi chính:

```text
cache/coherence
→ memory ordering
→ ISA memory model
→ language memory model
```

và:

```text
instruction stream
→ register renaming
→ scheduling window
→ speculative execution
→ ROB
→ precise retirement/exception
```

Invariant đã rõ hơn: internal reordering/speculation được phép để tăng performance, nhưng architectural state, precise exception và ISA memory contract phải được giữ.

Failure/performance coverage đã có false sharing, cache-line bouncing, NUMA locality, dependency chain, branch miss, memory-level parallelism và distinction giữa architectural correctness với microarchitectural side channel.

Production evidence đã có PMU/perf-counter mental model: IPC, branch miss, cache/TLB miss, stalled cycles, cache-to-cache traffic, memory bandwidth và NUMA evidence.

**Gap còn lại:** roofline/benchmark methodology và power/thermal throttling có thể được làm sâu hơn trong performance/canonical Architecture chapter hiện có; chưa cần chapter mới.

---

## 3. Operating Systems — coverage: mạnh

Foundation đã bao phủ kernel/syscall, process/thread/scheduling, synchronization/deadlock, virtual memory, filesystem/I/O, isolation/container, IPC và device/async I/O.

Advanced đã được làm sạch duplicate scheduler và memory-pressure chapters. Canonical scheduler hiện reasoning theo:

```text
runnable work
→ per-CPU run queue
→ fairness / priority / preemption
→ migration / cache / NUMA locality
→ wake-up latency
→ production scheduler evidence
```

Memory-pressure chapter reasoning theo:

```text
working set
→ page fault
→ reclaim
→ dirty/writeback
→ storage pressure
→ direct reclaim / cgroup / OOM
```

Invariant đã rõ: scheduler là allocator CPU time; VM subsystem phải giữ address/mapping/lifetime correctness trong khi tái sử dụng physical memory; dirty state không được mất khi backing protocol yêu cầu persistence.

Production evidence đã nối application symptom với run queue, context switch, throttling, steal time, faults, reclaim, dirty pages, swap, cgroup events và storage correlation.

**Gap còn lại:** RCU/kernel synchronization và eBPF/tracing internals vẫn mỏng. Nếu tiếp tục, nên hấp thụ vào concurrency/syscall/observability chapter hiện tại trước khi cân nhắc chapter mới.

---

## 4. Programming Languages & Runtime / Concurrency — coverage: mạnh

Foundation đã có semantics, values/references, scope/control flow, compiler/interpreter/JIT, paradigms, resource safety, type systems, parsing/AST và concurrency models.

Advanced đi từ type/effect systems tới ADT/variance/inference, ownership, compiler IR/SSA, JIT/deoptimization, GC và coroutine/structured concurrency.

Vòng audit đã hợp nhất duplicate ownership chapters. Canonical ownership hiện reasoning theo:

```text
resource state machine
→ ownership authority
→ borrow/lifetime relation
→ linear/affine usage discipline
→ typestate
→ unsafe/FFI boundary
```

Foundation concurrency cũng đã được đào sâu để không còn là catalogue `threads / actors / async`. Mental model hiện tách rõ:

```text
ownership
communication
ordering
lifetime
progress
```

và phân biệt:

```text
data race
≠ logical race

atomicity
≠ visibility
≠ ordering

concurrency
≠ parallelism
```

Threads/locks, atomics, actors/mailboxes, CSP/channels, async/await, structured concurrency và ownership đều được giải thích như cách chuyển invariant/failure mode sang boundary khác.

Performance connection đã rõ hơn: lock contention, retry/CAS pressure, cache coherence, event-loop stall, worker saturation và scheduler/NUMA interaction.

Production evidence gồm race detector/sanitizer, stress test, invariant assertion, lock/park waits, thread dump, event-loop/on-CPU evidence, scheduler delay và hardware coherence evidence khi cần.

**Gap còn lại:** FFI/ABI/object layout và memory reclamation trong lock-free structures có thể sâu hơn trong canonical ownership/compiler/runtime chapters; chưa cần root Concurrency library.

---

## 5. Database Internals — coverage: mạnh

Foundation đã có relational model, transaction/isolation, index/query execution, storage/WAL/recovery, SQL semantics, optimizer và distributed/analytical database overview.

Advanced hiện bao phủ MVCC/WAL, lock manager/serializability, B+Tree internals, LSM, buffer pool, optimizer/cardinality, join/vectorized execution và distributed transactions.

Vòng audit đã hợp nhất duplicate B-tree chapter và đào sâu canonical B+Tree theo page-oriented invariant:

```text
ordered search invariant
→ page layout/fan-out
→ buffer residency
→ split/merge
→ latch coupling
→ WAL/structural write
→ hot-key/contention evidence
```

Durability connection đã được mở rộng xuyên:

```text
application transaction
→ MVCC/commit state
→ WAL/LSN
→ buffer/page cache
→ filesystem/block layer
→ device persistence
→ replication/quorum
```

Production evidence hiện có execution plan, cardinality, buffer hit/miss, latch/lock waits, WAL/flush latency, dirty pages, replication positions và storage queueing.

**Gap còn lại:** replication/read consistency, failover behavior và analytical columnar/compression internals còn có thể sâu hơn. Ưu tiên mở rộng distributed database/join/storage canonical chapters trước khi thêm file.

---

## 6. Networks & Distributed Systems — coverage: mạnh

Foundation bao phủ packet/layering, Ethernet/IP/routing, TCP/UDP/congestion, DNS/HTTP/TLS, distributed failure/time/consistency, replication/consensus, sockets/NAT/firewall/VPN, routing protocols và HTTP2/HTTP3/QUIC.

Advanced distributed track có failure detector, lease/fencing, consensus, CRDT, multi-region replication và clocks/causality.

Consensus chapter đã được đào sâu theo invariant:

```text
single authoritative history
→ term/epoch
→ quorum intersection
→ log replication
→ commit/apply
→ membership reconfiguration
→ snapshot
→ linearizable read
```

Network production path không được tách thành root library mới. Cross-layer request path hiện đi xuyên:

```text
DNS
→ TCP/TLS
→ proxy/WAF/load balancer
→ runtime
→ connection pool
→ DB/storage
```

và chứa feedback loop:

```text
slowdown
→ timeout
→ retry
→ queue growth
→ saturation
→ service-time increase
→ cascading failure
```

Production evidence đã nối DNS/connection/retransmission, proxy queue, attempts, trace context với leader epoch, quorum state, replica position và clock uncertainty.

**Gap còn lại:** packet-level congestion/retransmission diagnosis, path MTU và QUIC internals có thể sâu hơn trong foundation/connection chapters. Không tạo Network hoặc Distributed Systems root library mới chỉ vì các phần này còn mỏng.

---

## 7. Security & Reliability — coverage: mạnh

Foundation đã có threat model, cryptography, identity/authentication/authorization, vulnerabilities, testing/debugging, reliability, web security, key/secret operations và supply chain.

Advanced security có trust boundary, crypto misuse, PKI/mTLS, OAuth/OIDC, memory isolation, browser-origin isolation và KMS/HSM lifecycle.

PKI chapter đã được đào sâu theo service-identity invariant, issuance/rotation/revocation, control-plane dependency, authorization separation và production certificate evidence.

Cross-layer security connection hiện được hấp thụ vào debugging path:

```text
identity
→ authorization
→ secret/capability
→ TLS/service identity
→ service boundary
→ KMS/resource access
→ audit
→ incident containment
```

Reliability foundation cũng đã được nâng từ “pattern list” thành reasoning theo:

```text
failure model
→ user-visible invariant
→ redundancy/failure domain
→ timeout/retry/backpressure
→ SLI/SLO
→ error budget/burn rate
→ containment/recovery
→ fault injection evidence
```

Error budget và burn rate hiện đã có định lượng cơ bản; correlated failure và dependency graph được tách khỏi giả định failure độc lập; chaos/fault injection được đặt dưới hypothesis + blast-radius + abort condition + observable recovery expectation.

Production evidence hiện chú trọng principal/certificate/token identity, policy version, key operation, service boundary, retry/timeout, SLI/SLO burn, saturation, failover state và containment timeline.

**Gap còn lại:** incident forensics/detection engineering và abuse/adversarial load có thể sâu hơn. Nên mở rộng security boundary/reliability canonical chapters thay vì tạo SRE root library.

---

## 8. Software Systems / Performance Engineering — coverage: mạnh

Canonical advanced track bao gồm queueing/backpressure, capacity/admission control, cache consistency, load balancing/pools/locality, event streams, idempotency và schema/protocol evolution. Duplicate capacity và cache chapters đã được hợp nhất.

Capacity chapter có invariant vận hành rõ:

> accepted work phải nằm trong vùng mà system còn khả năng hoàn thành theo deadline/SLO đã công bố.

Nó đã cover utilization knee, Little's Law, service-time distribution, concurrency limit, bounded queue, admission control, retry amplification, adaptive control, bulkhead, headroom và graceful degradation.

Performance foundation đã được đào sâu thành reasoning xuyên tầng:

```text
arrival rate
→ service centers/resources
→ service time + waiting time
→ utilization/queueing
→ contention/locality
→ bottleneck attribution
→ production evidence
```

Các điểm đã được bổ sung gồm CPU utilization vs useful work, cache/TLB/NUMA locality, concurrency-vs-contention curve, tail latency/fan-out, batching trade-off, connection-pool queue placement, retry amplification, warm/cold state, coordinated omission và measurement workflow từ SLO xuống resource evidence.

Performance optimization được đặt dưới correctness/reliability invariant: không coi việc bỏ fsync, giảm isolation, bỏ auth hoặc tăng stale window ngoài contract là “optimization”.

Caching chapter đã được đào sâu theo stale-state/invalidation/hot-key/stampede reasoning thay vì chỉ TTL pattern.

**Gap còn lại:** multi-tenant noisy-neighbor, resource fairness và whole-system profiling có thể sâu hơn bằng cách mở rộng capacity/load-balancing/debugging chapters hiện có.

---

## 9. System Design — coverage: mạnh nhưng giữ trong Software Systems

System Design không được tách thành root library riêng. Canonical entry point `system_decomposition_services_and_boundaries.md` đã được đào sâu để design bắt đầu bằng invariant/state ownership thay vì pattern catalogue.

Reasoning hiện đi theo:

```text
business/system invariant
→ state ownership
→ consistency/freshness requirement
→ sync/async communication
→ queue/cache/partition/replication semantics
→ security/failure boundary
→ capacity/overload behavior
→ observability evidence
→ organizational ownership
```

Boundary được đánh giá bằng nhiều loại coupling: code, schema, temporal, release, semantic và operational. Shared database, event-driven architecture, saga/compensation, idempotency, queues, cache, sharding, replication, service discovery, gateway/mesh và failure domains đều được giải thích theo invariant/failure cost thay vì “best practice” tuyệt đối.

System Design cũng đã nối security containment và graceful degradation: mTLS không thay authorization; nhiều replicas không tạo availability nếu failure domain/authority protocol sai; fallback không được phá correctness/security invariant.

Production evidence cho boundary gồm latency/error/retry, queue/backlog, schema compatibility, authorization decision, resource saturation, deploy independence và failure propagation.

**Gap còn lại:** cost modeling và capacity estimation cho multi-region/multi-tenant system có thể sâu hơn trong canonical performance/capacity chapters; chưa cần chapter System Design mới.

---

## 10. Software Engineering — coverage: mạnh

Foundation có requirements/specification, architecture reasoning, testing strategy, delivery/operations và maintenance/evolution.

Advanced track giữ canonical chapters cho architecture decisions, modularity/service boundary, API/schema compatibility, large-scale migration, test architecture và deployment safety.

Architecture-decision chapter đã được đào sâu theo quality attribute, reversibility, option value, socio-technical constraint và evidence-based review.

Deployment chapter reasoning theo:

```text
old version
→ mixed fleet
→ partial exposure
→ data/protocol transition
→ guardrail evidence
→ rollout / rollback / roll-forward
```

và nhấn mạnh rollback không phải time machine khi có irreversible side effect hoặc destructive data migration.

Boundary giữa Software Systems và Software Engineering được giữ rõ: Software Systems giải runtime behavior; Software Engineering giải cách thay đổi system đó an toàn theo thời gian.

**Gap còn lại:** incident learning, technical-debt economics và engineering-metric measurement traps có thể sâu hơn trong architecture/evolution chapters; chưa cần chapter mới.

---

## 11. AI Foundations — coverage: tốt và đúng boundary

Foundation đã có search/agents, knowledge/probabilistic inference, ML foundations, neural networks/representation learning và evaluation/data/responsibility.

Advanced hiện có model lifecycle, transformer/KV-cache inference cost và distributed training.

Model-lifecycle chapter đã được đào sâu theo systems reasoning:

```text
data/version
→ input pipeline
→ optimization/checkpoint state
→ model artifact
→ serving runtime
→ batching/KV cache/accelerator memory
→ online evaluation/feedback
```

Performance đã phân biệt compute-bound, memory-bound, communication-bound, queue/batching latency và accelerator-memory pressure.

Production evidence bao gồm artifact lineage, utilization, checkpoint state, communication stalls, serving queue, model version/cohort, drift/data-quality và offline-online gap.

AI specialization như retrieval, NLP, CV, robotics hoặc MLOps platform không nên bị nhồi vào Computer Science foundation chỉ vì công nghệ đang phổ biến. Cross-link tới dedicated AI library tốt hơn duplicate.

**Gap còn lại:** evaluation under distribution shift và serving reliability có thể được làm sâu hơn trong AI canonical chapters nếu cần.

---

## 12. Cross-layer Connections — coverage: mạnh

Bốn canonical advanced connection paths hiện bao phủ các causal chains trọng tâm.

### Correctness

```text
CPU cache/coherence
→ ISA memory ordering
→ compiler/runtime mapping
→ language memory model
→ happens-before
→ concurrency bug
```

### Durability

```text
application transaction
→ MVCC/commit state
→ WAL/LSN
→ filesystem/block/device
→ replication/quorum
→ recovery
```

### Request / overload

```text
DNS
→ TCP/TLS
→ proxy/LB
→ runtime/pool
→ database/storage
→ timeout/retry
→ queue/backpressure/load shedding
```

### Security / containment

```text
identity
→ authorization
→ secret/capability
→ TLS/service boundary
→ downstream authority
→ audit
→ containment
```

Các connection không cần tách thành chapter mới cho mỗi arrow. Nếu causal loop mới có thể được giải thích trong path hiện tại, ưu tiên rewrite sâu hơn.

Một nguyên tắc đã được củng cố trong vòng này là: **lower layer giải thích mechanism; fix phải đặt tại abstraction layer sở hữu invariant**, trừ khi contract của lower layer thực sự bị vi phạm.

---

## 13. Các foundation domain khác

Computation & Information, Algorithms & Data Structures, HCI & Graphics, Society/Ethics/Profession vẫn có foundational coverage rộng và không phải trọng tâm của vòng depth audit này.

Không vì thế coi chúng hoàn tất vĩnh viễn. Chúng tiếp tục tuân quality rule:

```text
problem
→ invariant/mechanism
→ assumptions
→ failure/edge case
→ evidence/connection khi phù hợp
```

Mathematical/statistical foundations tiếp tục cross-reference sang `mathematics/` thay vì duplicate.

---

## 14. Duplicate cleanup trong vòng audit này

Các advanced chapters trùng conceptual boundary đã được hợp nhất và bản dư được loại bỏ:

```text
Computer Architecture
- duplicate OoO / register-renaming / ROB

Operating Systems
- duplicate scheduler
- duplicate memory-pressure/reclaim

Programming Languages
- duplicate ownership / linear-affine

Database
- duplicate B-tree/B+Tree page-layout

Software Systems
- duplicate capacity/admission-control
- duplicate caching consistency/invalidation
```

Nguyên tắc canonical là: **một mental model chính có một chapter chính**. Variant wording hoặc tên file khác nhẹ không phải lý do tồn tại chapter thứ hai.

---

## 15. Những thứ cố ý không tách thành root library mới

Không tách Network, Distributed Systems, Security, Reliability, Performance Engineering, Concurrency hoặc System Design thành root library mới chỉ để taxonomy chi tiết hơn.

Các boundary hiện tại đã đủ:

```text
Computer Architecture
Operating Systems
Programming Languages & Runtime
Database
Networks & Distributed Systems
Security & Reliability
Software Systems
Software Engineering
AI Foundations
90_connections
```

Specialization chỉ nên tách khi có dependency graph và body of knowledge đủ độc lập để việc đặt trong canonical domain hiện tại làm mất conceptual clarity.

---

## 16. Priority gaps sau vòng audit

Các gap có giá trị nhất cho vòng tiếp theo, theo thứ tự conceptual chứ không phải “technology mới”, là:

```text
1. OS: RCU/kernel synchronization + tracing evidence
2. Database: replication/failover/read-consistency + columnar internals
3. Network: packet-level retransmission/congestion/path diagnosis
4. Security: forensics/detection + adversarial load/abuse resistance
5. Software Systems: noisy-neighbor/resource fairness + whole-system profiling
6. Software Engineering: incident learning + technical-debt economics
7. AI: evaluation under shift + serving reliability
```

Mỗi gap trước hết phải thử mở rộng canonical chapter hiện tại. Chỉ tạo chapter nếu topic có invariant/mechanism riêng đủ lớn và việc nhét vào file cũ thực sự làm mất conceptual boundary.

---

## 17. Maintenance rules sau audit

Khi tiếp tục đào sâu `computer_science/`:

1. Đọc foundation và canonical advanced chapter trước khi tạo file.
2. Nếu gap cùng invariant/failure model với chapter hiện có, rewrite chapter đó.
3. Mỗi phần advanced phải tạo thêm mental model hoặc reasoning, không chỉ thêm terminology.
4. Production claim nên đi kèm evidence model: metric, trace, wait, log, counter hoặc state cần quan sát.
5. Cross-layer explanation phải chỉ ra abstraction nào thật sự sở hữu invariant và lower layer nào chỉ giải thích mechanism.
6. Không dùng chapter count làm proxy cho completeness.
7. Coverage audit phải ghi cả **gap còn lại**, không chỉ liệt kê những gì đã có.
8. Không thêm chapter chỉ vì một công nghệ đang nổi hoặc vì roadmap còn một mục chưa có file.

Mục tiêu lâu dài của canonical library là trả lời được câu hỏi:

> **Computation và software systems duy trì correctness, performance, consistency, security và reliability như thế nào khi đi từ hardware → OS → runtime → application → network → storage → distributed system, và evidence nào cho phép ta chứng minh nguyên nhân khi abstraction bắt đầu leak?**