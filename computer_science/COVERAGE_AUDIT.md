# Coverage Audit — Computer Science Canonical Library

> Audit cập nhật: 2026-09-23 trên `feat/computer-science-depth-expansion`. Branch này được tạo từ `feat/computer-science` để tiếp tục đào sâu trong khi canonical parent/main đang được audit và merge. Không tạo Computer Science library mới, không đổi conceptual boundary hiện có.

Mục tiêu chất lượng vẫn là:

```text
foundation
→ internals
→ failure modes
→ performance / concurrency / consistency pressure
→ production evidence
→ lower abstraction layer
```

Audit không hỏi “đã có keyword X chưa?”. Một domain được coi là đủ mạnh khi người đọc có thể đi từ **problem → invariant → mechanism → assumption → failure → pressure-induced behavior → evidence → lower layer** mà không phải rời chapter chỉ để hiểu prerequisite ẩn.

## 1. Boundary và cấu trúc tổng thể

`computer_science/basic/` là prerequisite/foundation layer. Các domain ở root đi sâu theo conceptual boundary. `advanced/` chỉ chứa topic có mental model riêng đủ bền. `90_connections/` nối các layer thay vì duplicate nội dung.

Boundary canonical tiếp tục là:

```text
Computation & Information
Algorithms & Data Structures
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

Không tách Network, Distributed Systems, Security, Reliability, Performance Engineering, Concurrency hay System Design thành root library mới. Specialized AI vẫn thuộc library AI chuyên sâu; `10_ai_foundations/` chỉ giữ bridge nền tảng systems/foundations của Computer Science.

## 2. Computation & Information — từ computability tới verification

Track formal trước đây mạnh ở formal models, automata và Rice/static-analysis limits nhưng còn dừng sớm trước information/randomness/resource-bounded computation. Vòng expansion này hoàn thiện canonical path:

```text
formal model
→ computability / undecidability
→ semantic-analysis limits
→ Kolmogorov complexity
→ information theory
→ randomness / pseudorandomness
→ complexity classes beyond P/NP
→ interactive proofs / zero-knowledge / verifiable computation
```

Các chapter mới:

- `03_kolmogorov_complexity_compression_and_incompressibility.md`
- `04_information_theory_coding_bounds_and_noisy_channels.md`
- `05_randomness_entropy_sources_and_computational_unpredictability.md`
- `06_complexity_classes_conp_pspace_exp_and_randomized_classes.md`
- `07_interactive_proofs_zero_knowledge_and_verifiable_computation.md`

Coverage mới buộc người đọc phân biệt undecidable với computationally expensive; Kolmogorov complexity của object với Shannon entropy của distribution; statistical randomness với cryptographic unpredictability; proof semantics với authorization/freshness/availability của production system.

**Status:** strong cho formal reasoning nền tảng. Proof toán thuần dài vẫn nên cross-link sang `mathematics/` thay vì duplicate.

## 3. Algorithms & Data Structures — mature specialized track

DSA advanced đã có foundation về modeling/invariant/complexity/memory, linear structures, trees, graphs, algorithmic paradigms, specialized structures, C/Java/JavaScript implementation và systems case studies.

Boundary hiện tại đủ mạnh; không cần tăng chapter count chỉ để thêm tên thuật toán. Gap mới chỉ nên mở khi representation/invariant/complexity model thực sự khác các canonical owner hiện có.

**Status:** strong.

## 4. Computer Architecture — bổ sung sustained-performance control loop

Coverage đã có memory consistency/coherence, OoO/ROB/register renaming, speculation, cache/prefetch/replacement, NUMA/interconnect, TLB/page walk/virtualization và SIMD/GPU execution.

Vòng này canonical hóa:

- `07_power_thermal_dvfs_and_sustained_performance.md`

Chapter mới thêm reasoning path:

```text
workload activity
→ switching / power / heat
→ voltage-frequency operating point
→ thermal/power controller
→ boost / throttling
→ sustained throughput
```

Điểm mới quan trọng là phân biệt peak benchmark với steady-state capacity. Thermal inertia, leakage feedback, package power budget và cooling path có thể làm behavior đổi theo thời gian dù binary/workload không đổi.

**Status:** strong. Hardware-prefetch pathology tiếp tục thuộc cache hierarchy trừ khi sau này đủ độc lập để thành owner mới.

## 5. Operating Systems — synchronization, resource pressure và observability đều có owner

OS advanced cover kernel execution contexts/syscall, scheduler/run queue, memory pressure, virtual memory/TLB, filesystem crash consistency, async I/O/DMA, container isolation và RCU/seqlock/safe reclamation.

Vòng này canonical hóa thêm:

- `08_ebpf_tracing_kernel_observability_and_safety.md`

Reasoning path mới:

```text
kernel event / hook
→ verifier safety gate
→ bounded program + helper contract
→ map / aggregation / event transport
→ user-space evidence
→ correlation với application symptom
```

Chapter làm rõ hook semantics, verifier reasoning, JIT/overhead, per-CPU state, ring-buffer loss, cardinality pressure, sampling bias và observer effect. Observability không còn được coi là “chọn tool”, mà là thu evidence tại đúng state transition với overhead được hiểu.

Kernel packet semantics được đặt ở Network advanced để tránh duplicate; OS chapter sở hữu execution/safety/instrumentation mechanism.

**Status:** strong.

## 6. Programming Languages & Runtime — strong

Coverage mạnh ở type/effect/runtime contract, ownership, compiler IR/SSA, JIT/deoptimization, GC barriers, coroutine, language memory model và FFI/native boundary.

Cross-layer concurrency hiện có owner rõ:

```text
Architecture → visibility/order cost
OS → scheduling/wait/reclamation
Language → happens-before/ownership
Runtime → task/coroutine execution
```

Không cần mở root Concurrency library. Profile-guided/AOT/JIT details chỉ nên deepen compiler/JIT chapters nếu cùng invariant.

**Status:** strong.

## 7. Concurrency — integrated, không phải isolated library

Concurrency vẫn được phân theo abstraction owner. `90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md` là canonical proof path từ cache/coherence → ordering → language memory model → bug/lifetime.

RCU/seqlock chapter ở OS và memory consistency chapter ở Architecture đã đóng gap lớn về reclamation/order. Distributed causality vẫn thuộc Networks & Distributed Systems.

**Status:** strong và đúng boundary.

## 8. Data & Databases — từ OLTP internals tới adaptive analytical execution

Database advanced hiện có MVCC/WAL/recovery, lock manager/serializable isolation, B+Tree, LSM, buffer pool, cost-based optimizer, join/vectorized execution, distributed transactions và columnar analytical storage.

Vòng này canonical hóa:

- `09_adaptive_query_execution_runtime_filters_skew_and_reoptimization.md`

Reasoning path:

```text
logical query
→ compile-time statistics
→ initial physical plan
→ runtime cardinality/distribution evidence
→ safe adaptation boundary
→ revised physical strategy
→ same logical semantics
```

Chapter đóng gap giữa optimizer hypothesis và runtime reality: stale/correlated statistics, broadcast-vs-partitioned join, runtime filters, skew splitting, memory grant/spill, stage materialization và re-optimization. Invariant cốt lõi là physical strategy được phép đổi nhưng query result semantics không được đổi.

Analytical learning path giờ có thể đọc:

```text
optimizer estimate
→ join/operator execution
→ columnar physical layout/pruning
→ runtime adaptation under skew/pressure
```

**Status:** strong cho OLTP + analytical internals.

## 9. Networks — từ routing control plane xuống host packet queues

Foundation đã cover Ethernet/IP/routing, TCP/UDP/congestion, DNS/HTTP/TLS, sockets/IPv6/NAT/firewall/VPN, BGP và HTTP/2–HTTP/3/QUIC. Advanced có distributed protocols, time/causality, multi-region và BGP/routing policy.

Vòng này canonical hóa:

- `08_kernel_packet_path_qdisc_nic_offload_and_observability.md`

State/queue path:

```text
application write
→ socket buffer / transport state
→ routing/policy
→ qdisc
→ driver/NIC queue
→ wire
→ RX queue / interrupt-polling
→ socket receive buffer
→ application read
```

Chapter phân biệt syscall progress với wire delivery, giải thích qdisc/bufferbloat, driver/NIC rings, RSS/ECMP skew, interrupt/NAPI-style batching, segmentation/coalescing/checksum offload và vì sao host packet capture có thể khác wire reality.

Network diagnosis giờ có thể nối control plane `BGP → RIB/FIB` với data plane `socket → qdisc → NIC → wire` và OS evidence `eBPF/scheduler/DMA`.

**Status:** strong cho transport, routing policy và host packet-path production reasoning.

## 10. Distributed Systems — strong

Failure detectors, membership/gossip, lease/fencing, consensus/reconfiguration, CRDT/causal consistency, clocks/causality, exactly-once ambiguity, distributed transaction semantics và multi-region authority/failover đã có reasoning path rõ.

Gap còn lại chủ yếu là worked proofs/case studies: joint-consensus/reconfiguration và queueing under partition. Các gap này nên deepen chapter hiện có trước, không mặc định mở file mới.

**Status:** strong.

## 11. Security & Reliability — từ preventive controls tới artifact trust và incident evidence

Security advanced đã có security boundaries/attack chains, crypto composition, PKI/mTLS, OAuth/OIDC, memory safety/sandbox, browser isolation, secrets/KMS/HSM và detection/forensics.

Vòng này canonical hóa:

- `08_software_supply_chain_provenance_signing_and_build_trust.md`

Trust path:

```text
source/dependency
→ builder/workflow
→ artifact digest
→ provenance / attestation
→ signing authority
→ registry
→ deployment policy
→ runtime artifact
```

Chapter phân biệt digest, signature, provenance, SBOM và policy; giải thích hermetic vs reproducible build, dependency resolution, runner authority, mutable tag vs digest, build-cache poisoning, short-lived identity, transparency evidence, revocation và incident containment theo provenance graph.

Điểm cốt lõi: signing không chứng minh artifact tốt; nó chứng minh một authority đã ký statement. Security phụ thuộc vào ai được phép tạo statement, verifier policy và khả năng cắt authority sau compromise.

**Status:** strong cho preventive + detective + software supply-chain trust.

## 12. Reliability — failure containment vẫn cross-domain

Retry, timeout, circuit breaker, bulkhead, backpressure, load shedding và error budget tiếp tục được chia giữa Security/Reliability foundation và Software Systems production mechanisms.

Canonical feedback loop:

```text
arrival tăng
→ queue
→ latency
→ timeout
→ retry
→ arrival tăng thêm
→ overload / cascading failure
```

Không tạo Reliability root library mới. Security controls như registry/signing/identity dependency cũng phải được đọc theo fail-open/fail-closed và availability dependency.

**Status:** strong.

## 13. Software Systems & Performance — single host tới fleet economics

Queueing/backpressure, capacity/admission, caching, load balancing/pools, event streams, idempotency, schema evolution và fleet profiling/cost attribution đã có coverage tốt.

Fleet chapter đã mở rộng reasoning từ single request sang cohort/hardware/tenant:

```text
useful demand
→ distributed resource consumption
→ placement/skew/headroom
→ SLO outcome
→ cost attribution
→ capacity/architecture decision
```

DVFS chapter bổ sung lower-layer explanation cho sustained capacity; kernel packet path bổ sung network queue owner; AI inference disaggregation bổ sung accelerator state/queue case study.

**Status:** strong cho Performance Engineering và System Design reasoning mà không tách root library.

## 14. System Design — vẫn thuộc Software Systems

Canonical entry point vẫn là `08_software_systems/07_system_decomposition_services_and_boundaries.md`. Boundary được reasoning bằng invariant/state ownership, failure, capacity, security authority và economics; không bằng checklist technology.

Các expansion mới củng cố System Design theo state ownership:

```text
network packet → queue ownership
supply chain → artifact authority ownership
AI inference → KV state ownership
adaptive DB → execution-state adaptation boundary
```

Đây là mental model bền hơn product architecture diagram.

**Status:** strong.

## 15. Software Engineering — changeability + debt economics

Architecture evolution, modularity economics, API/schema compatibility, migration state machine, testing, deployment safety và technical-debt economics/Goodhart đã mạnh.

Supply-chain chapter cross-link Software Engineering ở change process nhưng không duplicate: Software Engineering sở hữu safe evolution/deployment; Security sở hữu trust/authority/provenance của artifact path.

Gap organizational design hoặc portfolio modernization chỉ nên mở khi có case study đủ lớn và independent invariant.

**Status:** strong.

## 16. AI Foundations — inference state ownership đã sâu hơn

AI Foundations trước đây có model lifecycle, Transformer/KV-cache internals và distributed training. Vòng này canonical hóa:

- `03_inference_disaggregation_prefill_decode_and_kv_cache_placement.md`

Reasoning path:

```text
admission
→ prefill
→ KV state creation
→ placement / transfer / ownership
→ decode scheduling
→ token stream
→ cancellation / cleanup
```

Chapter phân biệt TTFT, inter-token latency và total completion time; prefill compute profile với decode memory/KV profile; colocated vs disaggregated serving; KV handoff; continuous batching; prefix reuse/version identity; retry/cancellation ambiguity; memory headroom và phase transition khi queue/KV pressure tăng.

Điểm quan trọng là disaggregation không chỉ là deployment optimization. Nó đổi state ownership boundary và vì vậy tạo protocol cho publication, transfer, retry, cleanup và failure recovery.

**Status:** strong cho foundational AI systems. Accelerator compiler/kernel scheduling vẫn là gap tiềm năng nhưng chỉ nên mở nếu reasoning vượt khỏi SIMD/GPU + inference/training chapters hiện tại.

## 17. Cross-layer Connections — giữ bốn canonical integration paths

`90_connections/advanced/` tiếp tục giữ bốn path chính:

```text
Debugging:
symptom → invariant → evidence → lower layer → fix/containment

End-to-end request:
DNS/TCP-or-QUIC/TLS → routing/proxy/LB → runtime → pools/DB/storage
+ socket/qdisc/NIC queues
+ retry → timeout → overload/backpressure

Correctness:
CPU cache/coherence → ordering → language memory model → concurrency/lifetime bug

Durability:
application commit → MVCC/WAL → filesystem/storage → replication authority
```

Không tăng connection chapter count chỉ để nhắc các chapter mới. Packet path được hấp thụ vào request path; supply-chain authority được hấp thụ vào debugging/security evidence khi incident liên quan artifact; DVFS đi vào performance lower layer; inference state ownership cross-link queue/capacity/distributed-state chapters.

**Status:** strong.

## 18. Repository hygiene và branch strategy

Canonical parent vẫn là `feat/computer-science`. Vòng này làm việc trên child branch `feat/computer-science-depth-expansion` để không can thiệp audit/merge đang diễn ra ở parent/main.

Không tạo root library mới. Không tạo file `_final`, `_updated`, `_version2` trong canonical documentation tree. Các chapter mới đều nằm trong owner domain hiện có và README domain đã được cập nhật để tránh orphan file.

Một branch phụ `feat/computer-science-depth-expansion-v2` đã được tạo từ child branch trong quá trình thao tác nhưng không được dùng làm canonical work branch và không chứa thay đổi riêng của vòng này. Canonical work tiếp tục ở `feat/computer-science-depth-expansion`.

## 19. Coverage còn thiếu sau expansion

Các gap đáng xem tiếp nhưng chưa mặc định cần chapter mới:

```text
Architecture:
- hardware prefetch pathology / bandwidth pollution case studies

OS:
- selected scheduler/NUMA/network interaction case studies

Programming Languages:
- deeper AOT/JIT/profile-guided optimization only if current JIT chapter becomes overloaded

Database:
- adaptive execution worked cases across distributed engines

Distributed:
- joint-consensus/reconfiguration worked proof
- queueing/admission behavior under partition

Security:
- deeper supply-chain incident case studies
- detection-quality measurement without turning into SIEM metrics catalog

Software Systems:
- causal fleet profiling and autoscaling-control-loop case studies

AI systems:
- accelerator compiler/kernel scheduling
- heterogeneous memory and KV migration case study

Cross-layer:
- incident case studies that reuse existing four paths instead of creating generic connection chapters
```

Nguyên tắc tiếp tục vẫn là: **absorb vào canonical file nếu cùng invariant; chỉ tăng chapter count khi topic có mental model riêng, dependency rộng và owner boundary rõ**.

## 20. Quality gate cho vòng tiếp theo

Một advanced chapter chỉ được coi là đủ sâu khi trả lời tự nhiên:

```text
Vấn đề ban đầu là gì?
Invariant nào cần giữ?
Mechanism bên trong giữ invariant bằng cách nào?
Assumption nào đang được dựa vào?
Failure xảy ra ở đâu và biểu hiện thế nào?
Pressure làm behavior đổi phase ra sao?
Security/consistency/concurrency boundary nào liên quan?
Production evidence nào phân biệt các hypotheses?
Tầng abstraction bên dưới nào thực sự quyết định behavior?
Canonical source nào sở hữu kiến thức để tránh duplicate?
```

Prose là phần chính; bullet chỉ dùng cho list tự nhiên. Thuật ngữ English/Korean được giữ khi hữu ích nhưng phần giải thích phải là tiếng Việt tự nhiên. API/product/version chỉ neo mechanism, không thay mechanism.

## Kết luận

Sau vòng depth expansion này, `computer_science/` không chỉ rộng hơn mà có thêm các state/control models còn thiếu: information/randomness/verification ở formal CS; sustained power/thermal control ở Architecture; safe dynamic tracing ở OS; adaptive execution ở Database; host packet queues/offload ở Network; artifact provenance/authority ở Security; và KV-state ownership/disaggregation ở AI inference.

Giá trị của expansion không nằm ở số file. Mỗi chapter mới tồn tại vì nó thêm một invariant hoặc state machine đủ độc lập để cải thiện reasoning xuyên domain, đồng thời vẫn trỏ về canonical owner thay vì tạo library cạnh tranh.