# Coverage Audit — Computer Science Canonical Library

> Audit cập nhật: 2026-09-22. Vòng tiếp tục này **không tạo Computer Science library mới, không tạo chapter mới và không tăng chapter count**. Mục tiêu là làm sâu canonical state hiện có theo chuỗi: **foundation → internals → failure modes → performance/concurrency/consistency → production evidence**.

Audit không hỏi “đã có keyword X chưa?”. Một domain chỉ được coi là mạnh khi người đọc có thể đi từ **problem → invariant → internal mechanism → failure → pressure-induced behavior → evidence → lower abstraction layer** mà không phải rời chapter chỉ để hiểu prerequisite ẩn.

## 1. Boundary và cấu trúc tổng thể

`computer_science/basic/` tiếp tục là prerequisite/foundation layer. Các domain canonical ở root đi sâu theo conceptual boundary, còn `advanced/` chỉ chứa những concept có mental model riêng đủ bền. `90_connections/` nối các layers thay vì duplicate nội dung domain.

Boundary hiện tại vẫn hợp lý:

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

## 2. Computer Architecture — strong

Coverage hiện có đã đi qua OoO/ROB/register renaming, speculation, cache/prefetch/replacement, NUMA/interconnect/coherence, TLB/page walk/virtualization, SIMD/GPU execution và memory consistency.

Memory-order path hiện đủ để reasoning từ store buffer/coherence tới ISA ordering, compiler mapping, language happens-before, RMW contention, ABA/reclamation và PMU evidence. Vòng này không rewrite Architecture chỉ để thêm thuật ngữ.

**Gap còn lại:** power/thermal/DVFS behavior và hardware-prefetch pathology có thể được absorb vào các chapter performance/memory hiện hữu nếu cần. Roofline/operational-intensity reasoning đã được nối thêm từ Capacity Engineering ở vòng này, nên không cần chapter mới chỉ để lặp lại model.

## 3. Operating Systems — strong

OS advanced hiện cover syscall/kernel contexts, scheduling/run queues, page faults/reclaim, VM/TLB shootdown, filesystem crash consistency, async I/O/DMA và isolation/container boundaries.

Filesystem và async-I/O chapters đã có crash-state, write ordering, readiness-vs-completion, lifetime/cancellation, queue-depth và evidence đủ sâu cho cross-layer diagnosis.

**Gap còn lại:** RCU/seqlock và tracing/eBPF internals chỉ nên được thêm vào kernel/scheduler/evidence chapter nếu chúng giải một reasoning gap cụ thể; không mở chapter vì công nghệ phổ biến.

## 4. Programming Languages & Runtime — native boundary đã được lấp

Coverage trước đã mạnh ở type/effect/runtime contract, ownership, compiler IR/SSA, JIT/deoptimization, GC barriers, coroutines và language memory model.

Vòng này `04_programming_languages/03_compilers_interpreters_vm_and_jit.md` được mở rộng đúng boundary thay vì tạo FFI library mới. Chapter giờ nối:

```text
source type
→ runtime representation
→ marshalling
→ ABI/calling convention
→ native ownership/lifetime
→ error/thread-state translation
→ result quay lại runtime
```

Đã làm rõ object layout và GC movement, pin/handle semantics, allocator ownership, exception/panic boundary, thread attachment, call granularity, ABI version evolution, opaque-handle idiom, mixed native/managed debugging và việc native code có thể phá safety guarantee của memory-safe language.

**Coverage status:** strong cho compiler/runtime/JIT/GC/async/native interop.

**Gap còn lại:** lock-free reclamation vẫn nên cross-link sâu thêm vào ownership + memory-ordering chapters nếu có production case cụ thể, không cần root Concurrency/FFI library.

## 5. Concurrency — strong và đúng boundary

Concurrency tiếp tục được phân theo owner của invariant:

```text
Architecture   → cache/coherence/ordering cost
OS             → scheduler/threads/waiting
Language       → happens-before/ownership
Runtime        → coroutine/task scheduling
Software Sys   → queue/backpressure/fairness
Distributed    → causality/partial failure
```

`90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md` vẫn là canonical cross-layer proof path nên không rewrite không cần thiết.

## 6. Database internals — LSM gap đã được lấp

MVCC/WAL/recovery, buffer pool, B+Tree, optimizer/execution và distributed transaction coverage đã mạnh từ các vòng trước.

Vòng này `05_data_databases/advanced/03_lsm_tree_compaction_bloom_filters_and_write_amplification.md` được đào sâu từ mô tả mechanism thành storage-engine lifecycle:

```text
WAL
→ memtable
→ immutable memtable
→ SSTable
→ manifest/version-set publication
→ compaction
→ safe reclamation
```

Chapter giờ giải thích rõ read/write/space amplification, leveled-vs-tiered trade-off, Bloom filter memory trade-off, tombstone safety, snapshot/reclamation horizon, range-scan merge cost, skew/hot range, compaction debt, foreground/background I/O competition, corruption/checksum và interaction với SSD FTL write amplification.

Production evidence cũng được nối thành causal chain từ ingest → L0/run growth → compaction debt → storage saturation → read latency → write stall.

**Coverage status:** strong cho OLTP storage-engine internals.

**Gap còn lại:** analytical columnar compression/encoding và storage path cho vectorized execution có thể tăng trong canonical execution/storage chapters; chưa đủ lý do mở library mới.

## 7. Networks — packet-level QUIC/PMTU gap đã được lấp

Foundation đã có Ethernet/IP/routing, TCP/UDP/congestion, DNS/HTTP/TLS, sockets/IPv6/NAT/firewall/VPN, BGP và HTTP/2–HTTP/3/QUIC. End-to-end request path cũng đã được nối ở `90_connections/advanced/01...`.

Vòng này `basic/06_networks_distributed_systems/08_http2_http3_quic_and_modern_transport.md` được mở rộng nhưng vẫn giữ vai trò foundation-to-internals bridge. Chapter giờ phân biệt:

```text
HTTP semantics
vs stream multiplexing
vs transport ordering
vs flow control
vs congestion control
```

Đã làm rõ HTTP/2 TCP head-of-line blocking, QUIC packet number vs stream offset, loss recovery, shared congestion state, TLS integration, 0-RTT replay assumption, Connection ID/path migration, address-validation/amplification protection, Path MTU/PMTU black hole, UDP fallback, HPACK/QPACK state, encrypted-transport observability và packet-level diagnosis.

**Coverage status:** strong cho modern web transport reasoning.

**Gap còn lại:** routing/BGP incident case study hoặc kernel-networking path chỉ nên được thêm nếu cần production diagnosis cụ thể; không tạo Networks library mới.

## 8. Distributed Systems — strong

Failure detectors, lease/fencing, consensus/reconfiguration, CRDT/causal consistency, clocks/causality, distributed transaction semantics và multi-region authority/failover đã có reasoning path rõ.

**Gap còn lại:** joint-consensus/reconfiguration case study và queueing under partition có thể deepen existing chapters, không cần technology-centric file mới.

## 9. Security & Reliability — strong, testing connection đã sâu hơn

Security advanced đã có authority graph từ identity → authorization → secret/capability → TLS/service boundary → containment, cùng PKI/mTLS, OAuth/OIDC, memory safety/sandbox, browser isolation và KMS/HSM.

Vòng này không duplicate security material. Thay vào đó `Software Engineering/Test architecture` được nối thêm authorization testing, parser/protocol fuzzing, credential-lifecycle failure và forensic evidence, để security controls được kiểm thử theo failure model thay vì chỉ happy-path authentication.

**Gap còn lại:** detection-engineering pipeline sâu hơn vẫn có thể absorb vào security-boundary/evidence material nếu có conceptual value.

## 10. Software Systems & Performance Engineering — whole-system profiling gap đã được lấp

Queueing/backpressure, capacity/admission, cache behavior, load balancing/pools, streams, idempotency và schema evolution đã có coverage tốt.

Vòng này `08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md` được mở rộng theo lower-layer evidence thay vì viết một Performance library mới.

Chapter giờ nối:

```text
SLO symptom
→ queue/service-time split
→ on-CPU vs off-CPU
→ scheduler/run queue
→ PMU/cache/memory-bandwidth evidence
→ I/O queue depth
→ useful-outcome cost model
```

Đã thêm whole-system profiling, on/off-CPU distinction, scheduler delay/context switch/migration, PMU hypothesis-driven use, roofline/operational intensity, I/O queue-depth knee, heterogeneous hardware/NUMA/accelerator placement, cost per useful request/transaction/token và worked examples cho DB-pool wait + memory-bandwidth saturation.

**Coverage status:** strong cho performance/reliability/cost interaction.

**Gap còn lại:** fleet-level cost attribution và distributed profiling có thể thêm khi có production case; không cần root Performance Engineering library.

## 11. System Design — giữ đúng boundary trong Software Systems

Canonical entry point vẫn là `08_software_systems/07_system_decomposition_services_and_boundaries.md`. Boundary được reasoning bằng invariant/state ownership, failure, capacity và security authority chứ không bằng checklist technology.

Capacity/evidence bổ sung ở vòng này làm System Design path mạnh hơn mà không cần thêm chapter: một architecture boundary giờ có thể được theo xuống queue, pool, scheduler, hardware bottleneck và cost outcome.

## 12. Software Engineering — test architecture đã đạt failure-model reasoning

Architecture evolution, modularity economics, API/schema compatibility, migration state machine và deployment safety đã có coverage tốt.

Vòng này `09_software_engineering/advanced/04_test_architecture_contract_mutation_property_and_production_verification.md` được đào sâu đáng kể. Chapter giờ bắt đầu từ **test oracle + invariant + failure model**, sau đó đi qua contract, property/metamorphic/mutation testing, real integration semantics, concurrency testing, failure injection, crash interruption points, network ambiguous outcome, chaos experiment, security testing, differential/shadow testing, runtime invariant và production verification.

Đã bổ sung incident-learning loop, Goodhart risk của test metrics, privacy của test data, saturation/recovery testing và forensic usefulness của artifacts. Worked example payment timeout nối idempotency + durability + retry; schema migration example kiểm tra old/new coexistence thay vì giả định deploy atomic.

**Coverage status:** strong cho verification dưới production constraints.

**Gap còn lại:** technical-debt economics và engineering-metric governance có thể deepen architecture/maintenance chapter; incident-learning mechanism cơ bản đã được lấp ở testing.

## 13. AI Foundations — giữ boundary hẹp

Transformer inference và distributed training đã được đào sâu ở vòng trước: KV ownership, batching/admission, bandwidth pressure, topology-aware collectives, stragglers, distributed checkpoint, restart storm và evidence.

Vòng này không kéo accelerator framework/kernel cụ thể vào CS chỉ vì chúng đang nổi. Roofline, memory-bandwidth và heterogeneous-hardware reasoning mới ở Capacity chapter đã tạo bridge tốt hơn cho AI systems mà không duplicate AI specialization.

**Gap còn lại:** accelerator compiler/kernel scheduling, inference disaggregation và heterogeneous-memory case study chỉ nên thêm nếu chúng tạo durable mental model.

## 14. Cross-layer Connections — vẫn là canonical integration layer

`90_connections/advanced/` giữ bốn reasoning paths chính và không tăng chapter count:

```text
Debugging:
symptom → invariant → evidence → lower layer → fix/containment

End-to-end request:
DNS/TCP-or-QUIC/TLS → proxy/LB → runtime → pools/DB/storage
+ retry → timeout → queue → overload/backpressure

Correctness:
CPU cache/coherence → ordering → language memory model → concurrency bug

Durability:
application commit → MVCC/WAL → filesystem/storage → replication authority
```

Các thay đổi vòng này làm giàu domain source mà các connection trỏ tới, thay vì tạo thêm connection chapter chỉ để đổi tên cùng reasoning.

## 15. Repository hygiene và canonical-state audit

Branch audit tại thời điểm vòng này bắt đầu cho thấy chỉ có một branch riêng của Computer Science: `feat/computer-science`. Không có nhiều branch CS cần merge hoặc prune.

`main` có thay đổi mới thuộc domain khác, nên không được merge mù vào branch CS. Canonical CS branch được giữ riêng và chỉ fast-forward bằng commit thuộc `computer_science/`.

Tree audit không thấy các naming pattern duplicate/temp thường gặp như `_final`, `_updated` hoặc `_version2`. Không có lý do xóa file chỉ dựa vào tên trong vòng này.

Repo hiện **không có dedicated glossary file cho `computer_science/`** dù wording của một audit cũ từng nhắc glossary. Không tạo glossary mới chỉ để khớp tên. Terminology hiện được kiểm soát bởi `LANGUAGE_STYLE.md` và định nghĩa tại chapter nơi concept xuất hiện; nếu sau này glossary tạo thêm navigation value thật sự thì mới cân nhắc.

## 16. Coverage còn thiếu nhưng chưa đáng mở chapter mới

Các gap còn hợp lệ sau vòng này gồm power/thermal/DVFS và prefetch pathology ở Architecture; RCU/seqlock/eBPF internals ở OS; deeper lock-free reclamation case study ở concurrency; analytical columnar storage/encoding ở Database; selected routing/BGP incident reasoning; detection-engineering depth; fleet-level distributed profiling/cost attribution; technical-debt economics; và accelerator compiler/kernel scheduling trong AI systems.

Nguyên tắc tiếp tục là **absorb vào canonical file trước**. Chỉ tăng chapter count khi topic có mental model riêng, dependency rộng và không thể được giải thích mạch lạc trong boundary hiện hữu.

## 17. Quality gate cho vòng tiếp theo

Một phần advanced chỉ được xem là đủ sâu khi nó trả lời tự nhiên:

```text
Vấn đề ban đầu là gì?
Invariant nào cần giữ?
Mechanism bên trong giữ invariant bằng cách nào?
Assumption nào đang được dựa vào?
Failure xảy ra ở đâu và biểu hiện thế nào?
Performance pressure làm behavior đổi phase ra sao?
Security/consistency/concurrency boundary nào liên quan?
Production evidence nào phân biệt các hypotheses?
Tầng abstraction bên dưới nào thực sự quyết định behavior?
Canonical source nào sở hữu kiến thức để tránh duplicate?
```

Prose phải là phần chính; bullet chỉ dùng cho list tự nhiên. Thuật ngữ giữ English/Korean reference khi hữu ích nhưng giải thích bằng tiếng Việt. API/product/version chỉ được dùng để neo mechanism, không thay mechanism.

## Kết luận

Canonical `computer_science/` hiện đã chuyển từ coverage rộng sang giai đoạn **depth consolidation**. Vòng này không mở thêm library/chapter mà lấp năm reasoning gaps thật sự: LSM compaction lifecycle, QUIC/PMTU packet behavior, FFI/native runtime boundary, whole-system performance profiling/cost model và test/failure-injection architecture.

Hướng tiếp theo không phải tăng file count. Giá trị lớn nhất sẽ đến từ production case studies, lower-layer evidence và việc tiếp tục làm rõ abstraction nào sở hữu invariant trong các chapter đang tồn tại.