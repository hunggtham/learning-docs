# Coverage Audit — Computer Science Foundations

Tài liệu này ghi lại vòng kiểm tra coverage để thư viện không trở thành tập chapter ngẫu nhiên. Nó là maintenance document, không phải cheat sheet.

## Scope đã cover

Library hiện có **59 topic chapters** trong 10 nhóm conceptual cùng README, glossary và audit này.

### Computation & Information

Đã cover computation/state, information/encoding, binary/hex/integer/floating point, logic/invariants/abstraction, computability/undecidability. Các phần toán chứng minh/Boolean/information theory sâu hơn cross-reference sang `mathematics/` thay vì duplicate.

### Algorithms & Data Structures

Đã cover specification/correctness/termination, asymptotic complexity, amortized/worst/average/lower bound, memory locality/layout, arrays/lists/stacks/queues/deques, hashing, trees/B-tree/heaps/tries, graph BFS/DFS/topological/Dijkstra/MST/DSU, sorting/search/selection và algorithmic strategies recursion/divide-and-conquer/greedy/backtracking/DP.

### Architecture

Đã cover digital gates/combinational/sequential logic, CPU/ISA/instruction cycle, registers/pipeline/out-of-order, memory hierarchy/cache/TLB/coherence, I/O/interrupt/DMA, machine code/assembly/ABI/linking boundary, multicore/SIMD/GPU/NUMA/Amdahl.

### Operating Systems

Đã cover kernel/user privilege, syscalls, process/thread/scheduling/context switching, concurrency/atomics/memory ordering/deadlock/liveness, virtual memory/page table/TLB/COW/mmap, filesystem/page cache/journaling/storage, containers/VM/namespaces/cgroups/isolation.

### Programming Languages

Đã cover syntax/semantics/execution models, types/value/reference/aliasing, memory management/GC/ownership, scope/closure/control/async, compiler pipeline/IR/JIT/runtime, paradigms và error/resource safety.

### Data & Databases

Đã cover data models, relational model/keys/FD/normalization/NULL, transactions ACID/isolation anomalies/locks/MVCC/serializability, indexes/B+ tree/hash/query plans/cardinality, storage pages/buffer pool/WAL/recovery/LSM/backup distinction.

### Networks & Distributed Systems

Đã cover layering/encapsulation/packets, Ethernet/ARP/IP/subnet/routing/NAT, TCP/UDP/flow/congestion/BDP, DNS/HTTP/TLS, distributed partial failure/time/causality/consistency/CAP, replication/sharding/quorum/consensus/Raft intuition/reconfiguration.

### Security & Reliability

Đã cover threat modeling/trust/least privilege, cryptographic primitives/password hashing/AEAD/PKI, identity/authn/authz/session/OAuth-OIDC intuition, memory/web/injection vulnerabilities, testing/static/formal/fuzz/debugging, retry/timeout/circuit breaker/bulkhead/observability/SLI-SLO.

### Software Systems

Đã cover modularity/API contracts, Git/build/link/package/reproducibility, latency/throughput/queueing/capacity/cache/pool/scaling, queues/backpressure/messaging semantics/state placement, wall vs monotonic time/serialization/schema evolution/idempotency.

### Cross-domain connections

Đã thêm source→compiler/JIT→CPU, browser→network→server→DB, data lifecycle memory→disk→network, recurring trade-offs và abstraction/leaky-abstraction model.

## Topics intentionally delegated / cross-referenced

Discrete mathematics, graph proofs, formal logic, probability, information theory và deeper complexity theory đã có dedicated [Mathematics Knowledge Library](../mathematics/README.md). Library này nhắc đủ context để self-contained nhưng không copy dài.

Language/framework-specific APIs như Java Collections, Spring transactions, React rendering, Android/iOS runtimes thuộc các existing programming libraries trong repo; Computer Science library tập trung principles làm nền cho chúng.

AI/ML, computer graphics, compilers chuyên sâu, formal methods chuyên sâu, database product internals, kernel development, cryptographic protocol proofs và cloud-provider-specific architecture là domains đủ lớn để thành libraries riêng, không nên nhồi vào “foundations”. Những cầu nối cần thiết đã được đặt.

## Quality checklist đã áp dụng

Mỗi chapter được kiểm tra theo các tiêu chí sau: mở từ problem/mechanism thay vì definition-only; terminology English + Korean khi hữu ích; prose là chính; formulas đều có interpretation; examples/counterexamples ở concept dễ nhầm; common misconceptions; mental model; cross-reference; distinction giữa abstraction và implementation; assumptions/limitations quan trọng.

## Những ranh giới cần giữ khi mở rộng

Nếu sau này thêm chapter, chỉ thêm khi concept có mental model riêng và không duplicate thư viện khác. Ví dụ `Compiler Construction` có thể thành library riêng thay vì mở thêm 20 compiler-specific files ở đây. `Cloud Computing` cũng nên là domain mới dựa trên networking/distributed/security/reliability chapters hiện tại.

Mục tiêu của `computer_science/` là trả lời: **“Một computer system hoạt động từ information tới production service như thế nào, và những constraints nào lặp lại xuyên các layers?”** Nếu chapter mới không phục vụ câu hỏi này, nên đặt ở domain khác.
