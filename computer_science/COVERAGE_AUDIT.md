# Coverage Audit — Computer Science Canonical Library

> Audit cập nhật: 2026-09-22. Vòng này **không tạo Computer Science library mới và không tăng chapter count**. Các thay đổi tập trung rewrite sâu những canonical chapters hiện có theo chuỗi: **foundation → internals → failure modes → performance/concurrency/consistency → production evidence**.

Audit này không hỏi “đã có keyword X chưa?”. Một domain chỉ được coi là mạnh khi người đọc có thể đi từ **problem → invariant → internal mechanism → failure → pressure-induced behavior → evidence → lower abstraction layer** mà không phải nhảy sang một chapter mới chỉ để có reasoning cơ bản.

## 1. Boundary và cấu trúc tổng thể

`computer_science/basic/` tiếp tục là prerequisite/foundation layer. Các domain canonical ở root đi sâu hơn theo conceptual boundary, và `advanced/` chỉ chứa những concept có mental model riêng đủ sâu. `90_connections/` nối các layer thay vì duplicate nội dung domain.

Các boundaries lớn hiện tại vẫn đúng:

```text
Computer Architecture
Operating Systems
Programming Languages & Runtime
Data & Databases
Networks & Distributed Systems
Security & Reliability
Software Systems / Performance / System Design
Software Engineering
AI Foundations
Cross-layer Connections
```

Không tách Network, Distributed Systems, Security, Reliability, Performance Engineering, Concurrency hay System Design thành root library mới. Specialized AI vẫn nằm trong `02_artificial_intelligence/`; `10_ai_foundations/` giữ vai trò CS systems/foundational bridge.

## 2. Computer Architecture — mạnh, đã tăng depth về memory-order reasoning

Coverage hiện có gồm OoO/ROB/register renaming, branch prediction/speculation, advanced caches/prefetch/replacement, NUMA/interconnect/coherence, TLB/page walk/huge page/virtualization, SIMD/GPU execution và memory consistency.

Vòng này `advanced/00_memory_consistency_cache_coherence_and_ordering.md` được đào sâu theo đúng cross-layer requirement:

```text
cache coherence
→ store buffer/invalidate visibility
→ ISA memory ordering
→ compiler mapping
→ language happens-before
→ publication/RMW/lock-free bug
```

Đã bổ sung litmus-test reasoning, message passing, compiler-vs-ISA distinction, RMW serialization/coherence pressure, ABA + memory reclamation boundary, architecture-sensitive failures và evidence từ runtime → OS → PMU.

**Coverage status:** strong cho concurrency/memory hierarchy reasoning.

**Gap còn lại nên absorb vào chapter hiện có nếu mở rộng:** roofline/operational-intensity benchmark methodology sâu hơn; power/thermal/DVFS throttling; hardware prefetch pathologies và memory-bandwidth saturation case studies. Không cần chapter mới nếu không có mental model mới.

## 3. Operating Systems — mạnh hơn rõ ở crash consistency và async I/O

OS advanced đã cover syscall/kernel contexts, scheduler/run queues, page faults/reclaim, VM/TLB shootdown, filesystem, async I/O/DMA và isolation/container boundaries.

Hai chapter mỏng trước đây đã được rewrite:

### Filesystem crash consistency

Giờ có explicit crash-state model, separation atomicity/visibility/durability, pointer-before-object ordering invariant, journal commit protocol, metadata-vs-data journaling, barriers/flush/FUA, torn writes, COW root publication, file-vs-directory durability, writeback error propagation, dirty-page pressure, background amplification, failure injection và production evidence.

### epoll/io_uring/zero-copy/DMA

Giờ phân biệt readiness vs completion; cover partial I/O, level/edge trigger protocol, fd reuse/stale-event race, submission/completion ownership, cancellation/late completion, registered/pinned buffer lifetime, queue-depth trade-off, DMA/IOMMU, zero-copy lifetime, event-loop starvation, backpressure và evidence xuyên runtime/OS/device.

**Coverage status:** strong cho user/kernel execution + memory + I/O + persistence path.

**Gap còn lại:** kernel synchronization patterns như RCU/seqlock và tracing/eBPF internals có thể được absorb vào scheduler/kernel/evidence chapters nếu thực sự cần production diagnosis; không nên tạo technology-centric chapter chỉ vì eBPF phổ biến.

## 4. Programming Languages & Runtime — strong, JIT internals đã đạt production reasoning

Existing coverage đã có type/effect/runtime contract, ownership/borrowing/linear types, compiler IR/SSA, GC barriers, coroutines/continuations/structured concurrency và concurrency memory safety.

`advanced/05_jit_profiling_speculative_optimization_and_deoptimization.md` được rewrite từ mô tả tier/profile thành full runtime state machine:

```text
profile
→ speculative assumption
→ guard
→ optimized representation
→ invalidation
→ deoptimization/materialization
→ reprofile/recompile
```

Đã cover inline-cache polymorphism, code-size/I-cache trade-off, deopt state reconstruction, safepoint metadata, OSR, escape analysis, optimization cliffs, deopt storms, code cache, warm-up/phase change, benchmark traps và production evidence.

**Coverage status:** strong cho compiler/runtime/JIT/GC/async mental models.

**Gap còn lại:** FFI/ABI/object-layout and native boundary; lock-free memory reclamation có thể cross-link sâu thêm giữa ownership chapter và Architecture memory-ordering chapter thay vì chapter mới.

## 5. Concurrency — strong và có proof path xuyên layers

Concurrency hiện không bị cô lập thành một root library, đúng boundary. Nó được phân bố theo ownership của invariant:

```text
Architecture   → cache/coherence/ordering cost
OS             → threads/scheduler/atomics/waiting
Language       → memory model/happens-before/ownership
Runtime        → coroutine/task scheduling/cancellation
Software Sys   → queues/backpressure/fairness
Distributed    → causality/consensus/partial failure
```

`90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md` đã đủ mạnh và được giữ nguyên để tránh rewrite không cần thiết. Architecture chapter mới làm sâu lower-layer mechanisms mà connection này dựa vào.

**Coverage status:** strong.

**Gap còn lại:** additional case study về reclamation/hazard-pointer/epoch có thể đi vào existing ownership or memory-ordering chapter nếu cần, không cần root concurrency library.

## 6. Database internals — strong hơn ở transaction-history lifecycle và buffer management

Existing advanced coverage có lock/predicate/serializable, B+Tree internals, LSM, optimizer/cardinality, execution/vectorization và distributed transactions.

### MVCC/WAL/recovery

`advanced/00_mvcc_visibility_wal_and_recovery_internals.md` giờ tổ chức theo ba frontiers:

```text
visibility
→ durability
→ reclamation
```

Đã làm rõ transaction authority, snapshot vs serializability, WAL/commit acknowledgement, steal/no-steal + force/no-force, LSN/page state, conceptual recovery state machine, crash scenarios, group commit, torn pages, checkpoint debt, vacuum horizon, replica receive/persist/apply frontier, feedback loops và evidence.

### Buffer pool

`advanced/04_buffer_pool_replacement_and_dirty_page_management.md` giờ cover page table/frame lifecycle, pin-vs-latch-vs-lock, dirty write debt, WAL frontier, foreground/background flush, scan-resistant admission, plan/cache feedback, double buffering, NUMA, memory pressure, multi-tenant noisy neighbor và phase changes từ hit-dominated tới flush/storage saturation.

**Coverage status:** strong cho OLTP storage-engine internals.

**Gap còn lại:** LSM compaction/Bloom/write-amplification chapter vẫn tương đối ngắn; analytical columnar compression/vectorized storage path có thể được tăng trong existing execution/storage chapters. Không cần thêm DB library.

## 7. Networks — strong ở end-to-end request path, còn packet-level diagnosis là gap hợp lệ

Foundation hiện có Ethernet/IP/routing, TCP/UDP/congestion, DNS/HTTP/TLS, sockets/IPv6/NAT/firewall/VPN, BGP và HTTP/2–HTTP/3/QUIC.

`90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md` đã có full path:

```text
DNS
→ TCP/QUIC connection
→ TLS identity
→ proxy/WAF/load balancer
→ runtime/event loop/thread pool
→ pool/queue
→ DB/storage
```

Nó cũng đã cover deadline propagation, retry amplification, fan-out tail, backoff/jitter, load shedding, utilization knee và evidence waterfall. Vì vậy vòng này không rewrite chỉ để lặp lại nội dung.

**Coverage status:** strong ở systems/network boundary reasoning.

**Gap còn lại:** packet-level congestion/retransmission diagnosis, path-MTU/black-hole behavior và QUIC transport internals vẫn là areas có thể đào sâu. Ưu tiên absorb vào existing transport/modern-HTTP chapters thay vì tạo `Networks` library mới.

## 8. Distributed Systems — strong hơn ở replication authority và multi-region failover

Existing advanced coverage có failure detectors/membership/gossip, lease/fencing/split-brain, consensus log replication/reconfiguration/snapshots, CRDT/causal consistency, time/clocks/causality và distributed transaction semantics.

`advanced/05_multi_region_replication_and_geo_distributed_tradeoffs.md` được rewrite theo authority + history frontiers:

```text
leader authority/epoch
→ local durable frontier
→ replica received/persisted/applied frontier
→ read freshness contract
→ failover promotion/fencing
```

Đã thêm read-your-writes/session consistency, lag as history distance, safe promotion/failback, multi-leader conflict invariants, geo-partitioning, hotspot/skew, failure-domain correlation, active-active caveats, regional retry cascade, global coordination cost, data residency/identity dependency, evidence và partial-failure testing.

**Coverage status:** strong cho consensus/replication/geo-distribution reasoning.

**Gap còn lại:** more concrete reconfiguration/joint-consensus case study và queueing under network partitions nếu muốn tăng depth; không cần chapter công nghệ mới.

## 9. Security & Reliability — authority graph và adversarial-load reasoning đã mạnh hơn

Existing Security advanced có cryptographic protocol composition, PKI/mTLS, OAuth/OIDC token lifecycle, memory safety/sandbox, browser isolation và Secrets/KMS/HSM.

`advanced/00_security_boundaries_attack_chains_and_exploitability.md` giờ đi theo authority graph:

```text
identity
→ authorization
→ credential/secret capability
→ TLS/mTLS channel
→ service/resource boundary
→ delegated/downstream authority
→ detection
→ incident containment
```

Đã bổ sung confused-deputy/delegation, rotation as distributed transition, reliability failure of security control, abuse/cost amplification, multi-tenant fairness, parser differential, containment ordering, time dependency, retry classification, evidence và boundary-failure tests.

Reliability vẫn giữ đúng conceptual boundary: retry/timeout/backpressure/overload nằm ở Software Systems, identity/control-plane failure nằm ở Security, incident diagnosis nằm ở cross-layer connections.

**Coverage status:** strong.

**Gap còn lại:** detection engineering/forensic pipeline có thể tăng thêm trong existing security-boundary/evidence material; chaos/fault-injection methodology có thể deepen existing reliability/testing files.

## 10. Software Systems & Performance Engineering — strong hơn ở feedback loops và fairness

Existing advanced coverage có capacity/utilization knee/admission control, cache invalidation/stampede/hot keys, load balancing/connection pools/locality, streams/watermarks/replay, idempotency/dedup và schema/protocol evolution.

`advanced/00_queueing_tail_latency_and_backpressure.md` được rewrite thành full overload model:

```text
arrival variability
→ queue debt
→ tail latency
→ timeout
→ retry/hedge amplification
→ resource contention
→ service rate decreases
→ overload collapse
```

Đã cover Little's Law boundary, queue-vs-service time, deadline propagation, bounded queues, backpressure reachability, pool as concurrency limiter, admission/load shedding, priority enforcement, multi-tenant fairness, rate-vs-concurrency limiting, circuit breaker behavior, queue placement, recovery storms và evidence by work flow.

**Coverage status:** strong cho performance/reliability interaction.

**Gap còn lại:** whole-system profiling methodology (on-CPU + off-CPU + queues + PMU + I/O) và cost/performance modeling across heterogeneous hardware có thể tăng trong existing evidence/capacity chapters.

## 11. System Design — giữ đúng boundary trong Software Systems, đã tăng chiều sâu

Không tạo System Design root library. Canonical entry point `08_software_systems/07_system_decomposition_services_and_boundaries.md` đã được rewrite.

Chapter giờ bắt đầu từ invariant/state ownership và coi mỗi boundary là:

```text
contract boundary
+ ownership boundary
+ failure boundary
+ capacity boundary
+ security authority boundary
```

Đã thêm remote-outcome ambiguity, sync-vs-async costs, saga as durable state machine, API behavioral contract, capacity/admission, multi-tenant isolation, principal delegation, gateway/mesh retry layers, data/network locality, multi-region coordination classification, cost modeling/fan-out amplification, failure-domain graph, deployment/data compatibility và production boundary evidence.

**Coverage status:** strong như systems-design reasoning, không phải checklist technology.

**Gap còn lại:** end-to-end numerical capacity/cost case studies cho multi-region/multi-tenant có thể absorb vào capacity/System Design chapter; không cần tạo “System Design library”.

## 12. Software Engineering — migration state-machine depth đã tăng

Existing advanced coverage có architecture decisions/evolution/socio-technical constraints, modular-monolith vs services economics, API/schema compatibility, test architecture và deployment safety.

`advanced/03_large_scale_refactoring_strangler_and_branch_by_abstraction.md` giờ coi migration là:

```text
code state
+ data state
+ protocol versions
+ traffic routing
+ ownership
```

Đã cover phase invariants, source-of-truth authority, expand-contract, naive dual-write atomicity gap, dual-read hidden divergence, backfill concurrency, shadow safety, semantic comparison, cutover gates, rollback-vs-roll-forward, irreversible steps, capacity ramp, observability dimensions, transition fault tests, ownership handoff và deletion criteria cho temporary compatibility.

**Coverage status:** strong cho evolutionary change under production constraints.

**Gap còn lại:** technical-debt economics, incident-learning loops và engineering-metric Goodhart traps có thể deepen existing architecture/maintenance/testing chapters.

## 13. AI Foundations — giữ boundary hẹp, systems depth đã tăng đáng kể

Không kéo RAG, agent frameworks, product-specific LLMOps hay model catalog vào `10_ai_foundations/`. Specialized AI vẫn ở `02_artificial_intelligence/`.

### Transformer inference

`advanced/01_transformer_attention_kv_cache_and_inference_cost.md` giờ cover request/model/KV ownership, prefill-vs-decode, KV lifecycle/paged allocation, bandwidth-bound decode, batching/admission, head-of-line/fairness, context capacity, quantization, tensor parallel communication, prefix-cache semantic identity, model-version rollout, memory-pressure phases, retry amplification và evidence.

### Distributed training

`advanced/02_distributed_training_data_model_and_pipeline_parallelism.md` giờ cover logical step invariant, global-batch semantics, topology-aware collectives, compute/communication overlap, stragglers, tensor/pipeline/sharded-state trade-offs, input pipeline, data-sampling correctness, collective failure, consistent distributed checkpoints, RPO/RTO, restart storms, numerical reduction ordering và rank-level evidence.

**Coverage status:** strong ở systems foundations cho training/inference; specialization vẫn đúng chỗ ở AI library riêng.

**Gap còn lại:** accelerator compiler/kernel scheduling, inference disaggregation and heterogeneous-memory case studies chỉ nên thêm nếu chúng tạo durable mental model; không thêm chapter vì một serving framework đang thịnh hành.

## 14. Cross-layer Connections — hiện là một trong các phần mạnh nhất

`90_connections/advanced/` hiện có bốn canonical reasoning paths và **không cần tăng chapter count**:

```text
00 Debugging across abstraction layers
   symptom → invariant → evidence → lower layer → fix/containment

01 End-to-end request
   DNS/TCP/TLS → proxy/LB → runtime → pools/DB/storage
   + retry → timeout → queue → overload → backpressure/cascading failure

02 Correctness path
   CPU cache/coherence → memory ordering → language memory model
   → happens-before → concurrency bug

03 Durability path
   application commit → MVCC/WAL → buffer/filesystem → storage
   → replication/authority
```

Security connection trong `00` đã có identity → authorization → secret/KMS → TLS/mTLS → service boundary → revocation/incident containment. Vì nội dung đã mạnh, vòng này cố ý giữ nguyên thay vì rewrite để tạo diff không có giá trị.

**Coverage status:** strong.

## 15. Production Evidence — coverage đã chuyển từ “có observability” sang “evidence theo invariant”

Sau vòng này, các domain quan trọng đều có evidence chain rõ hơn:

```text
Concurrency:
race/contention evidence → scheduler/off-CPU → cache/NUMA/PMU

Durability:
transaction/WAL frontier → dirty/checkpoint → filesystem/writeback → device/replica

Request latency:
trace → queue wait → runtime/pool → network/storage saturation

Security:
principal → policy decision → key/credential → service boundary → containment timeline

AI:
request/token distribution → scheduler/KV/collective → accelerator/interconnect evidence
```

Rule tiếp tục là: **evidence không thay proof/invariant; evidence dùng để xác định mechanism nào đang active trong execution thật.**

## 16. Những gap có giá trị cao nhất cho vòng tiếp theo

Không cần tăng breadth bằng chapter mới. Nếu tiếp tục, ưu tiên rewrite sâu các canonical file còn mỏng theo thứ tự conceptual value:

1. LSM compaction/Bloom/write amplification và interaction với cache/checkpoint/storage pressure.
2. Packet-level TCP/QUIC congestion, retransmission và Path-MTU failure diagnosis trong existing network chapters.
3. Whole-system performance profiling: on-CPU/off-CPU/queue/PMU/I/O correlation trong existing capacity/evidence chapters.
4. FFI/ABI/object layout/native-runtime boundary trong Programming Languages.
5. Detection/forensic evidence pipeline và chaos/fault-injection methodology trong existing Security/Reliability chapters.
6. Multi-tenant cost/capacity case studies trong Software Systems/System Design.
7. Technical-debt economics + incident learning + engineering metrics traps trong Software Engineering.
8. AI accelerator/kernel/memory case studies only where they generalize beyond one framework/vendor.

Các mục này là **depth backlog**, không phải lý do tạo root library mới.

## 17. Quality gate cho mọi advanced rewrite tiếp theo

Một advanced concept chỉ coi là hoàn thiện khi người đọc có thể trả lời:

```text
Vấn đề ban đầu là gì?
Invariant nào phải giữ?
Mechanism nội bộ giữ invariant bằng cách nào?
Assumption nào đang được dựa vào?
Failure xảy ra ở transition/boundary nào?
Performance pressure làm behavior đổi phase ra sao?
Evidence nào phân biệt các mechanisms cạnh tranh?
Lower abstraction layer nào thật sự quyết định behavior?
Fix nên đặt ở tầng nào sở hữu invariant?
```

Nếu chapter chỉ thêm API, framework, protocol name hoặc trend mà không thêm mental model/reasoning, không nên tạo file mới.

## 18. Kết luận audit

Canonical `computer_science/` hiện có foundation rộng và một advanced systems spine khá đồng nhất. Sau vòng này, các phần từng mỏng nhất ở crash consistency, async I/O, JIT, MVCC/WAL, buffer pool, multi-region replication, security boundaries, queueing/backpressure, System Design, large-scale migration và AI systems đã được nâng theo cùng một reasoning grammar.

Điểm quan trọng nhất là library giờ ngày càng ít phụ thuộc vào “technology catalog” và nhiều hơn vào các invariants lặp lại xuyên layers:

```text
ownership
ordering
visibility
authority
lifetime
capacity
backpressure
durability
consistency
failure containment
```

Đây là đúng boundary cần giữ cho những vòng update tiếp theo.