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

Số file không phải mục tiêu. Trong vòng audit này, các chapter advanced trùng mental model đã được hợp nhất thay vì giữ hai bản gần giống nhau.

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

Advanced hiện có đường reasoning rõ từ memory consistency/cache coherence tới OoO execution, speculation, cache hierarchy, NUMA, TLB và SIMD/GPU. Vòng audit này đã hợp nhất duplicate OoO chapter và đào sâu hai điểm trọng tâm:

- **cache/coherence → memory ordering → language memory model**;
- **OoO execution → register renaming → scheduling window → ROB → precise exception**.

Invariant đã rõ hơn: speculative/internal reordering được phép, nhưng architectural state, exception semantics và ISA memory contract phải giữ.

Failure/performance coverage đã có false sharing, cache-line bouncing, NUMA locality, dependency chain, branch miss, memory-level parallelism và microarchitectural side-channel distinction.

Production evidence đã có PMU/perf-counter mental model: IPC, branch miss, cache/TLB miss, stalled cycles, cache-to-cache traffic, bandwidth và NUMA evidence.

**Gap còn lại:** measurement methodology có thể đào sâu thêm trong chapter performance foundation/advanced hiện có; chưa cần chapter mới.

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

Invariant và lower-layer dependency đã rõ: scheduler là allocator CPU time; virtual-memory subsystem phải giữ mapping/lifetime correctness trong khi tái sử dụng physical memory.

Production evidence đã nối application symptom với run queue, context switch, throttling, steal time, faults, reclaim, dirty pages, swap, cgroup events và storage correlation.

**Gap còn lại:** RCU/kernel synchronization và eBPF tracing vẫn mỏng, nhưng nên được hấp thụ vào concurrency/syscall/observability chapter hiện tại nếu mở rộng; chưa đủ lý do tạo chapter riêng.

---

## 4. Programming Languages & Runtime — coverage: mạnh

Foundation đã có semantics, values/references, scope/control flow, compiler/interpreter/JIT, paradigms, resource safety, type systems, parsing/AST và concurrency models.

Advanced đi từ type/effect systems tới ADT/variance/inference, ownership, compiler IR/SSA, JIT/deoptimization, GC và coroutine/structured concurrency.

Vòng audit đã hợp nhất hai ownership chapters thành một canonical chapter. Mental model hiện tập trung vào:

```text
resource state machine
→ ownership authority
→ borrow/lifetime relation
→ linear/affine usage discipline
→ typestate
→ unsafe/FFI boundary
```

Connection với runtime/OS đã rõ hơn: allocator, ABI, native boundary, atomic refcount, structured-concurrency lifetime và language memory model.

Failure coverage không dừng ở memory safety mà phân biệt use-after-free/double-free với logical race, deadlock, starvation và resource exhaustion.

**Gap còn lại:** FFI/ABI/object layout có thể được đào sâu thêm trong ownership/compiler/runtime canonical chapters thay vì tạo chapter mới ngay.

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

**Gap còn lại:** replication/read consistency và analytical columnar internals còn có thể sâu hơn; nên mở rộng các chapter distributed database/join/storage hiện có trước khi cân nhắc file mới.

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

**Gap còn lại:** packet-level congestion/retransmission diagnosis và QUIC internals có thể sâu hơn trong foundation/connection chapters; không cần tạo Network library mới.

---

## 7. Security & Reliability — coverage: mạnh

Foundation đã có threat model, cryptography, identity/authentication/authorization, vulnerabilities, testing/debugging, reliability patterns, web security, key/secret operations và supply chain.

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

Reliability không bị tách khỏi security. Retry/backpressure/load shedding nằm ở Software Systems; containment và correlated failure được cross-link lại tại Security & Reliability.

Production evidence hiện chú trọng principal, certificate/token identity, policy version, key operation, service boundary, timeout/retry, SLO burn, saturation và containment timeline.

**Gap còn lại:** error-budget/burn-rate math và chaos/fault-injection methodology còn mỏng; nên mở rộng reliability foundation hoặc canonical software-system chapters thay vì tạo nhiều file SRE rời rạc.

---

## 8. Software Systems / Performance Engineering / Concurrency / System Design — coverage: mạnh

Các chủ đề này cố ý không tách thành nhiều root libraries. Chúng được tổ chức quanh queue/state/resource boundary.

Canonical advanced track bao gồm queueing/backpressure, capacity/admission control, cache consistency, load balancing/pools/locality, event streams, idempotency và schema/protocol evolution.

Duplicate capacity và cache chapters đã được hợp nhất.

Capacity chapter hiện có invariant vận hành rõ:

> accepted work phải nằm trong vùng mà system còn khả năng hoàn thành theo deadline/SLO đã công bố.

Nó đã cover utilization knee, Little's Law, service-time distribution, concurrency limit, bounded queue, admission control, retry amplification, adaptive control, bulkhead, headroom và graceful degradation.

Caching chapter đã được đào sâu theo stale-state/invalidation/hot-key/stampede reasoning thay vì chỉ TTL pattern.

System Design được giữ trong boundary này: design bắt đầu bằng invariant, workload, failure model và evidence; technology chỉ là implementation choice.

Concurrency được nối từ CPU memory ordering → language memory model → runtime/OS scheduler → distributed ordering, thay vì dùng một từ `concurrency` cho mọi tầng.

**Gap còn lại:** multi-tenant noisy-neighbor và whole-system profiling có thể sâu hơn bằng cách mở rộng capacity/load-balancing/debugging chapters hiện có.

---

## 9. Software Engineering — coverage: mạnh

Foundation có requirements/specification, architecture reasoning, testing strategy, delivery/operations và maintenance/evolution.

Advanced track giữ sáu canonical chapters: architecture decisions, modularity/service boundary, API/schema compatibility, large-scale migration, test architecture và deployment safety.

Architecture-decision chapter đã được đào sâu theo quality attribute, reversibility, option value, socio-technical constraint và evidence-based decision review.

Deployment chapter hiện reasoning theo:

```text
old version
→ mixed fleet
→ partial exposure
→ data/protocol transition
→ guardrail evidence
→ rollout / rollback / roll-forward
```

và nhấn mạnh rollback không phải time machine khi có irreversible side effect hoặc destructive data migration.

System Design và Software Engineering được phân ranh rõ: Software Systems sở hữu runtime behavior; Software Engineering sở hữu cách thay đổi system đó an toàn theo thời gian.

**Gap còn lại:** incident learning/technical-debt economics/engineering metrics vẫn có thể sâu hơn trong architecture/evolution chapters; chưa cần chapter mới.

---

## 10. AI Foundations — coverage: tốt và đúng boundary

Foundation đã có search/agents, knowledge/probabilistic inference, ML foundations, neural networks/representation learning và evaluation/data/responsibility.

Advanced hiện có model lifecycle, transformer/KV-cache inference cost và distributed training.

Model-lifecycle chapter đã được đào sâu mạnh theo systems reasoning:

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

**Gap còn lại:** model-specific specialization như retrieval, NLP, CV, robotics hoặc MLOps platform không nên nhồi vào Computer Science foundation nếu đã có/đủ lớn cho dedicated AI library. Cross-link tốt hơn duplicate.

---

## 11. Cross-layer Connections — coverage: mạnh

Bốn canonical advanced connection paths hiện bao phủ các causal chains quan trọng nhất:

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

Các connection này không cần tách thành chapter mới riêng cho mỗi arrow. Nếu causal loop mới có thể được giải thích trong một path hiện tại, ưu tiên rewrite sâu hơn.

---

## 12. Domains foundation khác

Computation & Information, Algorithms & Data Structures, HCI & Graphics, Society/Ethics/Profession vẫn có foundational coverage rộng và không phải trọng tâm của vòng depth audit này.

Không vì thế coi chúng “hoàn tất vĩnh viễn”. Chúng tiếp tục tuân cùng quality rule: problem → invariant/mechanism → assumptions → failure/edge case → evidence/connection khi phù hợp.

Mathematical/statistical foundations tiếp tục cross-reference sang `mathematics/` thay vì duplicate.

---

## 13. Duplicate cleanup trong vòng audit này

Các advanced chapters trùng conceptual boundary đã được hợp nhất và bản dư được loại bỏ, gồm các nhóm:

- Computer Architecture: hai chapter OoO/register-renaming/ROB;
- Operating Systems: hai scheduler chapters;
- Operating Systems: hai memory-pressure/reclaim chapters;
- Programming Languages: hai ownership/linear-affine chapters;
- Database: hai B-tree/B+Tree page-layout chapters;
- Software Systems: hai capacity/admission-control chapters;
- Software Systems: hai caching consistency/invalidation chapters.

Nguyên tắc canonical là một mental model chính có một chapter chính; variant wording không phải lý do tồn tại file thứ hai.

---

## 14. Những thứ cố ý không tách thành root library mới

Không tách Network, Distributed Systems, Security, Reliability, Performance Engineering, Concurrency hoặc System Design thành root library mới chỉ để taxonomy trông chi tiết hơn.

Các boundary hiện tại đã đủ để đặt chúng:

```text
Architecture / OS / Runtime
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

## 15. Maintenance rules sau audit

Khi tiếp tục đào sâu `computer_science/`:

1. Đọc foundation và canonical advanced chapter trước khi tạo file.
2. Nếu gap cùng invariant/failure model với chapter hiện có, rewrite chapter đó.
3. Mỗi phần advanced phải tạo thêm mental model hoặc reasoning, không chỉ thêm terminology.
4. Production claim nên đi kèm evidence model: metric, trace, wait, log, counter hoặc state cần quan sát.
5. Cross-layer explanation phải chỉ ra abstraction nào thật sự sở hữu invariant và lower layer nào chỉ giải thích mechanism.
6. Không dùng chapter count làm proxy cho completeness.
7. Coverage audit phải ghi cả **gap còn lại**, không chỉ liệt kê những gì đã có.

Mục tiêu lâu dài của canonical library là trả lời được câu hỏi:

> **Computation và software systems duy trì correctness, performance, consistency, security và reliability như thế nào khi đi từ hardware → OS → runtime → application → network → storage → distributed system, và evidence nào cho phép ta chứng minh nguyên nhân khi abstraction bắt đầu leak?**
