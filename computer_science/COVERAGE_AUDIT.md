# Coverage Audit — Computer Science Canonical Library

> Audit cập nhật: 2026-09-23. Computer Science đã đủ rộng để vòng tiếp theo ưu tiên **deepening các gap trong owner hiện có**, không mở thêm domain lớn. Mục tiêu vẫn là: **foundation → internals → failure modes → pressure behavior → production evidence → lower abstraction layer**.

Audit không hỏi “đã có keyword X chưa?”. Một domain được coi là mạnh khi người đọc có thể đi từ **problem → invariant → mechanism → assumption → failure → pressure-induced behavior → evidence → lower layer** mà không cần rời chapter chỉ để hiểu prerequisite ẩn.

## 1. Boundary và cấu trúc tổng thể

`computer_science/basic/` là prerequisite/foundation layer. Các domain ở root đi sâu theo conceptual boundary. `advanced/` chỉ chứa topic có mental model riêng đủ bền. `90_connections/` nối các layer thay vì duplicate nội dung.

Boundary hiện tại:

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

Không tách Network, Distributed Systems, Security, Reliability, Performance Engineering, Concurrency hay System Design thành root library mới. Specialized AI vẫn thuộc `02_artificial_intelligence/`; `10_ai_foundations/` chỉ giữ bridge CS systems/foundations. Các root mới như `cybersecurity/`, `distributed_systems/` hay `system_design/` chỉ được xem xét sau khi các gap bên dưới đã được deepen và chứng minh không còn owner phù hợp.

## 2. Computer Architecture — strong

Coverage đã có OoO/ROB/register renaming, speculation, cache/prefetch/replacement, NUMA/interconnect/coherence, TLB/page walk/virtualization, SIMD/GPU execution và memory consistency.

Memory-order path đủ để reasoning từ store buffer/coherence tới ISA ordering, compiler mapping, language happens-before, RMW contention, ABA/reclamation và PMU evidence.

Vòng này đã thêm `02_computer_architecture/advanced/07_power_thermal_dvfs_and_sustained_performance.md`, sở hữu reasoning path từ activity → power/heat → DVFS/control → sustained throughput. Hardware-prefetch pathology đã được deepen trong `02_computer_architecture/advanced/03_advanced_cache_hierarchy_prefetching_and_replacement.md`, gồm accuracy/timeliness/coverage, pollution, bandwidth theft, queue pressure và controlled comparison. Bước tiếp theo là lower-layer validation bằng hardware-event evidence, không mở chapter mới.

## 3. Operating Systems — RCU/reclamation đã thành canonical unit

OS advanced cover syscall/kernel contexts, scheduler/run queues, page faults/reclaim, VM/TLB shootdown, filesystem crash consistency, async I/O/DMA và container isolation.

Vòng này thêm:

- `03_operating_systems/advanced/07_rcu_seqlock_and_safe_memory_reclamation.md`

Chapter mới sở hữu reasoning path:

```text
publication
→ reader lifetime
→ logical removal
→ grace/quiescent proof
→ deferred reclamation
→ pressure/backlog
→ safe physical reuse
```

Nó phân biệt mutual exclusion với lifetime safety, grace period với timeout, logical removal với physical reclamation; đào sâu memory ordering, callback debt, seqlock retry, epoch/hazard-pointer comparison, ABA, scheduler interaction, NUMA/cache-coherence cost và production evidence của reclamation backlog.

`00_kernel_execution_contexts_and_syscall_path.md` vẫn giữ overview để người đọc hiểu context/lock/lifetime trước khi chuyển sang chapter chuyên sâu. Đây là cross-link có chủ đích, không phải hai canonical owners cạnh tranh.

Vòng này đã thêm `03_operating_systems/advanced/08_ebpf_tracing_kernel_observability_and_safety.md`, sở hữu verifier/JIT, helper/map/ring-buffer, event loss, overhead và safety boundary. Chapter đã được deepen thêm cho kernel networking path: ingress/egress lifecycle, NAPI/softirq, socket/qdisc boundaries, GRO/GSO, drop-vs-delay-vs-retransmission và flow-correlated evidence. Bước tiếp theo là lower-layer validation theo driver/workload cụ thể, không mở chapter riêng nếu chỉ lặp packet-path overview.

## 4. Programming Languages & Runtime — strong

Coverage mạnh ở type/effect/runtime contract, ownership, compiler IR/SSA, JIT/deoptimization, GC barriers, coroutine, language memory model và FFI/native boundary.

Native path hiện nối:

```text
source type
→ runtime representation
→ marshalling
→ ABI/calling convention
→ native ownership/lifetime
→ error/thread-state translation
→ result
```

RCU/reclamation chapter mới ở OS tạo thêm cross-layer link tới ownership/memory-ordering mà không tạo root Concurrency library.

**Coverage status:** strong cho compiler/runtime/JIT/GC/async/native interop.

## 5. Concurrency — strong và đúng owner boundary

Concurrency vẫn phân theo owner của invariant:

```text
Architecture   → cache/coherence/ordering cost
OS             → scheduler/threads/waiting/reclamation
Language       → happens-before/ownership
Runtime        → coroutine/task scheduling
Software Sys   → queue/backpressure/fairness
Distributed    → causality/partial failure
```

`90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md` là canonical cross-layer proof path.

## 6. Data & Databases — OLTP + analytical physical path đều mạnh

MVCC/WAL/recovery, lock manager, B+Tree, LSM, buffer pool, optimizer, join/vectorized execution và distributed transactions đã có canonical chapters.

Vòng này thêm:

- `05_data_databases/advanced/08_columnar_storage_encoding_pruning_and_vectorized_scans.md`

Columnar storage đủ độc lập để thành chapter vì nó có physical-performance invariant riêng:

```text
logical table
→ row group / column chunk
→ encoding + compression + metadata
→ partition/file/row-group pruning
→ projection/predicate pushdown
→ vectorized scan
→ selection vector
→ late materialization
→ spill / shuffle
```

Chapter làm rõ dictionary/RLE/delta/bit-packing trade-off, min-max/zone map, Bloom negative pruning, clustering, null/nested representation, immutable segment + delta/delete path, reclustering debt, memory-bandwidth bottleneck, spill phase change, distributed skew và runtime counters.

Pruning metadata được giữ theo invariant: false-positive work có thể chấp nhận; false-negative result không được phép nếu semantics là exact.

**Coverage status:** strong cho OLTP storage-engine internals và analytical storage/execution path.

Vòng này đã thêm `05_data_databases/advanced/09_adaptive_query_execution_runtime_filters_skew_and_reoptimization.md`, đóng gap chính về runtime feedback, dynamic filtering, skew và plan adaptation. **Gap còn lại:** analytical cost-model case studies chỉ khi có invariant/production evidence mới, không mở chapter theo technology name.

## 7. Networks — transport và inter-domain routing đều có advanced reasoning

Foundation đã cover Ethernet/IP/routing, TCP/UDP/congestion, DNS/HTTP/TLS, sockets/IPv6/NAT/firewall/VPN, BGP và HTTP/2–HTTP/3/QUIC.

Modern transport đã đủ sâu ở TCP head-of-line, QUIC packet number vs stream offset, loss recovery, congestion/flow control, TLS/0-RTT, Connection ID, PMTU black-hole, fallback và encrypted-transport evidence.

Vòng này thêm:

- `06_networks_distributed_systems/advanced/07_bgp_routing_policy_convergence_and_route_security.md`

BGP chapter sở hữu state path:

```text
prefix reachability
→ advertisement/withdrawal
→ import/export policy
→ path selection
→ RIB
→ FIB
→ observed packet path
```

Đã phân biệt control plane/data plane, eBGP/iBGP/underlay, policy vs shortest path, RIB/FIB, convergence/path exploration, aggregation, more-specific routes, route leak vs hijack, RPKI scope, filtering/max-prefix, communities, anycast, asymmetric routing, ECMP skew và multi-vantage-point incident evidence.

**Coverage status:** strong cho web transport và routing-policy production diagnosis.

**Gap còn lại:** kernel packet path hoặc congestion-control implementation case studies nếu tạo durable mental model.

## 8. Distributed Systems — strong

Failure detectors, membership/gossip, lease/fencing, consensus/reconfiguration, CRDT/causal consistency, clocks/causality, exactly-once ambiguity, distributed transaction semantics và multi-region authority/failover đã có reasoning path rõ.

BGP chapter bổ sung một distributed policy/control-plane case nhưng không thay owner của consensus/replication material.

Joint-consensus/reconfiguration đã có owner trong `06_networks_distributed_systems/advanced/03_consensus_log_replication_reconfiguration_and_snapshots.md`. **Gap còn lại:** queueing under partition và worked proof sâu hơn, ưu tiên deepen chapter consensus/replication hiện có.

## 9. Security & Reliability — detection/forensics đã có canonical evidence path

Security advanced có authority graph từ identity → authorization → credential/capability → TLS/service boundary → containment, cùng crypto composition, PKI/mTLS, OAuth/OIDC, memory safety/sandbox, browser isolation và KMS/HSM.

Vòng này thêm:

- `07_security_reliability/advanced/07_detection_engineering_forensics_and_incident_evidence.md`

Chapter mới đi theo:

```text
security invariant
→ trusted telemetry
→ detection hypothesis
→ correlation
→ triage/investigation
→ containment
→ recovery
→ learning
```

Đã bổ sung evidence trust, event identity/causality, base-rate problem, false positive/negative, correlation windows, clock uncertainty, tamper-resistant audit path, provenance/chain of custody, ephemeral infrastructure, memory/process/network evidence, identity graph, effective secret revocation, logging overload, telemetry data quality, privacy/retention và incident containment theo capability graph.

**Coverage status:** strong cho preventive controls + production detection/forensics.

Detection/forensics và detection-quality measurement đã có canonical owner trong `07_security_reliability/advanced/07_detection_engineering_forensics_and_incident_evidence.md`; chapter hiện có measurement protocol cho label provenance, prevalence, precision/recall, analyst capacity, false-negative exposure, calibration và regression gates. **Gap còn lại:** selected software-supply-chain trust mechanism nếu tạo independent reasoning path.

## 10. Software Systems & Performance — từ single host đến fleet economics

Queueing/backpressure, capacity/admission, caching, load balancing/pools, streams, idempotency và schema evolution đã có coverage tốt. Whole-system profiling đã nối SLO symptom với queue/service split, on/off-CPU, scheduler, PMU/cache/memory bandwidth, I/O queue depth và useful-outcome cost.

Vòng này thêm:

- `08_software_systems/advanced/07_fleet_profiling_cost_attribution_and_multi_tenant_efficiency.md`

Chapter mới mở rộng scale:

```text
useful demand
→ distributed critical path
→ fleet resource consumption
→ placement/skew/headroom
→ SLO outcome
→ cost attribution
→ capacity/architecture decision
```

Nó giải thích aggregation bias, hardware cohorts, cost per useful outcome, failure headroom, bin-packing/blast-radius trade-off, rightsizing, noisy neighbors, fairness work-unit, shared-cost allocation, showback/chargeback, tracing-vs-profiling-vs-metrics, sampling bias, rollout cohort comparison, tail cohort drill-down, autoscaling oscillation, cold start và accelerator memory/queue economics.

**Coverage status:** strong cho single-node + fleet-level performance/cost reasoning.

**Gap còn lại:** fleet-wide causal profiling hoặc scheduler-specific implementation chỉ khi có case thật sự cần.

## 11. System Design — vẫn thuộc Software Systems

Canonical entry point vẫn là `08_software_systems/07_system_decomposition_services_and_boundaries.md`. Boundary được reasoning bằng invariant/state ownership, failure, capacity, security authority và economics; không bằng checklist technology.

Fleet chapter làm rõ placement, multi-tenancy, fairness, headroom và cost attribution nhưng không tạo root Performance/System Design library mới.

## 12. Software Engineering — changeability giờ có debt economics riêng

Architecture evolution, modularity economics, API/schema compatibility, migration state machine, testing và deployment safety đã mạnh.

Vòng này thêm:

- `09_software_engineering/advanced/06_technical_debt_economics_metrics_and_goodhart.md`

Chapter mới định nghĩa debt bằng future change cost/risk thay vì code aesthetics; phân biệt deliberate/accidental/obsolescence debt; đào sâu change amplification, coordination/data/test/operational debt, recurring interest evidence, trigger/exit condition, option value, reversibility, compounding coupling và quyết định paydown/contain/accept/retire.

Metric governance đi theo outcome → guardrail → delivery/system signals. Goodhart risk được giải thích qua coverage/deploy/ticket/LOC proxy; DORA-style metrics được dùng như diagnostic signal chứ không team leaderboard.

**Coverage status:** strong cho verification, migration, deployment và economics/governance của changeability.

**Gap còn lại:** deeper organizational design hoặc portfolio-level modernization chỉ khi cần case study lớn.

## 13. AI Foundations — giữ boundary hẹp

Transformer inference và distributed training đã có KV ownership, batching/admission, bandwidth pressure, topology-aware collectives, stragglers, distributed checkpoint, restart storm và evidence.

Fleet cost chapter tạo bridge tốt hơn cho accelerator utilization/cost nhưng không kéo framework/kernel vendor-specific vào CS.

**Gap còn lại:** accelerator compiler/kernel scheduling, inference disaggregation và heterogeneous-memory case study nếu chúng tạo durable mental model.

## 14. Cross-layer Connections — canonical integration layer

`90_connections/advanced/` giữ bốn paths chính:

```text
Debugging:
symptom → invariant → evidence → lower layer → fix/containment

End-to-end request:
DNS/TCP-or-QUIC/TLS → routing/proxy/LB → runtime → pools/DB/storage
+ retry → timeout → queue → overload/backpressure

Correctness:
CPU cache/coherence → ordering → language memory model → concurrency/lifetime bug

Durability:
application commit → MVCC/WAL → filesystem/storage → replication authority
```

Các chapter mới cung cấp source sâu hơn để các connection trỏ tới; không tăng connection chapter chỉ để đổi tên cùng reasoning.

## 15. Repository hygiene và branch strategy

Computer Science vẫn có một canonical feature branch: `feat/computer-science`. Tree không dùng naming pattern duplicate/temp như `_final`, `_updated`, `_version2` cho vòng mới.

Repo không có dedicated glossary cho `computer_science/`; không tạo glossary chỉ để đủ checklist. Terminology được điều phối bởi `LANGUAGE_STYLE.md` và định nghĩa tại owner chapter.

`main` có các thay đổi mới hơn thuộc TypeScript/React/Mathematics, không thuộc Computer Science. Khi đưa Computer Science lên `main`, phải preserve các thay đổi đó và merge/copy đúng `computer_science/` subtree thay vì reset hoặc force-update `main` về feature branch.

## 16. P1 — Computer Science: chỉ deepen gap, không mở thêm domain lớn

Computer Science đã rất rộng: computation, DSA, architecture, OS, runtime, database, networking/distributed, security, software systems, software engineering, AI và HCI. Vì vậy, các gap dưới đây là backlog P1 trước khi cân nhắc mở thêm một domain root:

```text
Architecture
✓ power / thermal / DVFS (canonical chapter đã có)
✓ hardware-prefetch pathology (đã deepen trong canonical cache chapter)

Operating Systems
✓ eBPF / tracing internals (canonical chapter đã có)
✓ kernel networking path (đã deepen trong eBPF chapter; cần validation theo workload)

Database
✓ adaptive analytical execution (canonical chapter đã có)
→ deeper analytical cost-model case studies

Distributed Systems
✓ reconfiguration owner (canonical consensus chapter đã có)
→ reconfiguration worked proofs
→ partition + queueing behavior

Security
→ software supply-chain trust
✓ detection quality measurement (đã deepen trong detection chapter)

AI Systems
→ accelerator compiler / kernel scheduling
→ inference disaggregation

Cross-layer
→ incident → correctness / durability / cost
```

Đây là những việc cần làm trước khi nghĩ tới các root như `cybersecurity/`, `distributed_systems/` hoặc `system_design/`; repository hiện đã có owner phù hợp cho các boundary này.

Một chi tiết naming nên cân nhắc sau: hiện tồn tại cả `02_artificial_intelligence` và `02_computer_architecture`, đồng thời còn `10_ai_foundations`. README đã giải thích boundary, nhưng numbering vẫn dễ gây nhầm khi nhìn tree trực tiếp. Không rename trong vòng P1 này; chỉ chuẩn hóa khi có kế hoạch migration và cập nhật toàn bộ internal links.

Các dấu `✓` là gap đã có canonical owner; mũi tên `→` là phần cần deepen tiếp theo. Nguyên tắc tiếp tục vẫn là **absorb vào canonical file nếu cùng invariant; chỉ tăng chapter count khi topic có mental model riêng, dependency rộng và owner boundary rõ**.

## 17. Quality gate

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

Prose là phần chính; bullet chỉ dùng cho list tự nhiên. Thuật ngữ English/Korean được giữ khi hữu ích nhưng phải giải thích bằng tiếng Việt. API/product/version chỉ neo mechanism, không thay mechanism.

## Kết luận

Canonical `computer_science/` đã chuyển từ chỉ depth consolidation sang **selective chapter expansion**. Sáu gap trước đây được giữ trong chapter lớn giờ đã đủ độc lập để trở thành canonical units: safe memory reclamation, columnar analytical storage, BGP/routing policy, detection/forensics, fleet profiling/cost attribution và technical-debt economics/metric governance.

Giá trị của các chapter mới không nằm ở tăng file count mà ở việc tạo sáu reasoning paths mới có owner rõ, cross-link rõ và production evidence rõ. Vòng tiếp theo nên ưu tiên case study sâu và lower-layer validation hơn là tiếp tục tăng chapter count mặc định.
