# Coverage Audit — Computer Science Foundations

Tài liệu này kiểm tra coverage và conceptual boundaries để `computer_science/` không trở thành collection chapter ngẫu nhiên. Sau vòng comprehensive expansion, library có **100 topic chapters** trong **14 nhóm conceptual**, cộng `README.md`, glossary Việt–Anh–Hàn và audit này.

## 1. Computation & Information — 5 chapters

Đã cover computation/state transition, information/encoding, binary/hex/integer/floating point, logic/invariants/abstraction và computability/undecidability. Mathematical proof, Boolean algebra và information theory sâu hơn cross-reference sang `mathematics/`.

## 2. Algorithms & Data Structures — 12 chapters

Đã cover specification/correctness/termination; asymptotic, amortized, worst/average/lower bounds; memory locality/layout; arrays/lists/stacks/queues/deques; hashing; trees/B-tree/heaps/tries; graphs; sorting/search/selection; recursion/divide-and-conquer/greedy/backtracking/DP; string algorithms/KMP/rolling hash/suffix structures; randomized/approximation/online/streaming algorithms; reductions, P/NP/NP-hard/NP-complete và parameterized-complexity intuition.

## 3. Computer Architecture — 8 chapters

Đã cover digital logic/sequential circuits; CPU/ISA/instruction cycle; pipeline/out-of-order; cache/TLB/coherence; I/O/interrupt/DMA; assembly/ABI; multicore/SIMD/GPU/NUMA/Amdahl; SSD/HDD/NVMe/FTL/persistence; performance equations, power, benchmarking và roofline intuition.

## 4. Operating Systems — 8 chapters

Đã cover kernel/user privilege, syscalls, processes/threads/scheduling/context switching, synchronization/atomics/memory ordering/deadlock, virtual memory/TLB/COW/mmap, filesystem/page cache/journaling, containers/VM/namespaces/cgroups, IPC/signals/pipes/shared memory, boot/drivers/MMIO/DMA và blocking/non-blocking/async I/O.

## 5. Programming Languages & Runtime — 9 chapters

Đã cover syntax/semantics/execution models; values/references/aliasing/memory management; scope/closure/control/async; compiler/IR/JIT/runtime; programming paradigms; error/resource safety; type systems/subtyping/generics/variance/ADTs; lexer/parser/AST/semantic analysis/SSA; threads/actors/CSP/structured concurrency/ownership/memory safety.

## 6. Data & Databases — 8 chapters

Đã cover data models; relational model/keys/FD/normalization/NULL; transactions ACID/isolation anomalies/locks/MVCC/serializability; indexes/B+ tree/hash/query execution; pages/buffer pool/WAL/recovery/LSM; relational algebra/SQL logical semantics/window/grouping; cardinality estimation/join ordering/query optimization; NoSQL models, shard keys, replication, OLTP/OLAP, row-vs-column stores, warehouse/lake/lakehouse.

## 7. Networks & Distributed Systems — 9 chapters

Đã cover layering/encapsulation/packets; Ethernet/ARP/IP/subnet/routing/NAT; TCP/UDP/flow/congestion/BDP; DNS/HTTP/TLS; partial failure/time/causality/consistency/CAP; replication/sharding/quorum/consensus/Raft intuition; socket APIs, IPv6, firewall/VPN/MTU; forwarding vs routing, OSPF/BGP/AS/anycast; HTTP/2 framing, HTTP/3/QUIC và modern transport trade-offs.

## 8. Security & Reliability — 9 chapters

Đã cover threat modeling/trust/least privilege; cryptographic primitives/password hashing/AEAD/PKI; identity/authentication/authorization/session/OAuth-OIDC intuition; memory/injection vulnerabilities; testing/static/formal/fuzz/debugging; retry/timeout/circuit breaker/bulkhead/observability/SLI-SLO; SOP/CORS/XSS/CSRF/SSRF/session web security; keys/secrets/certificates/KMS/HSM/rotation; dependency/build provenance/SBOM/CI supply-chain security.

## 9. Software Systems — 8 chapters

Đã cover modularity/API contracts; Git/build/link/package/reproducibility; latency/throughput/queueing/capacity/pools/scaling; state placement/queues/backpressure; clocks/serialization/schema evolution/idempotency; caching/TTL/stampede/load balancing/CDN/consistent hashing; event/command/log/stream delivery/order/event time; monolith/services/data ownership/saga/gateway/mesh/Conway's Law.

## 10. Software Engineering — 5 chapters

Đã cover requirements/specification/acceptance criteria/traceability/risk-driven process; architecture quality attributes, coupling/cohesion, ADR, information hiding và patterns-by-context; unit/integration/E2E/contract/property/fuzz/mutation/static verification strategy; CI/CD/config/feature flags/deployment/database migration/IaC/runbooks; maintenance/refactoring/legacy/technical debt/data evolution/knowledge debt/sunsetting.

## 11. AI Foundations — 5 chapters

Đã cover agent/problem formulation/state-space search/A*/minimax/planning; logic/knowledge representation/Bayesian networks/approximate inference/causal distinction; supervised/unsupervised/self-supervised learning, loss/generalization/overfit/leakage/shift; neural networks/backprop/SGD/CNN/attention/transformers/embeddings; evaluation metrics/calibration/subgroups/human-in-loop/data provenance/robustness.

AI specialization như NLP, computer vision, reinforcement learning, robotics, foundation-model systems và MLOps đủ lớn để thành libraries riêng; chapter hiện tại cung cấp prerequisites và vocabulary để đi vào chúng.

## 12. HCI & Computer Graphics — 5 chapters

Đã cover mental models/feedback/human factors/Fitts/Hick/errors; interface information architecture/accessibility/keyboard/focus/color/responsive/user research; graphics coordinate spaces/matrices/projection/raster pipeline/shaders/depth; sampling/color spaces/gamma/alpha/textures/raster-vs-ray-tracing/compression; multimedia frame timing/game loop/audio/video/synchronization/real-time behavior.

## 13. Computing, Society, Ethics & Profession — 4 chapters

Đã cover privacy/data minimization/consent/purpose/professional responsibility/dual use; data provenance/measurement-sampling-label bias/fairness/feedback loops/governance; copyright/open-source licenses/patent/trademark/data licenses/compliance; energy/embodied cost/e-waste/digital divide/accessibility/resilience/platform concentration.

Legal specifics thay đổi theo jurisdiction/time nên chapter law chỉ cung cấp conceptual map, không thay current legal research/advice.

## 14. Cross-domain Connections — 5 chapters

Đã có end-to-end source→compiler/JIT→CPU; browser→DNS/TLS/network→server→DB; data lifecycle register→cache→RAM→disk→network; recurring trade-offs; abstraction/leaky-abstraction model.

Các chapter mới cross-link trực tiếp vào những connection này thay vì duplicate toàn bộ content.

## Coverage đối chiếu với một curriculum CS rộng

Library hiện đã có foundational coverage cho các knowledge areas lớn thường xuất hiện trong chương trình Computer Science: algorithmic foundations, architecture, operating systems, programming languages, data management, networking/distributed computing, security, software development/systems, software engineering, AI, HCI, graphics/interactive systems và social/professional issues. Mathematical/statistical foundations nằm trong dedicated `mathematics/` library và được cross-reference thay vì copy.

## Các domain cố ý không nhồi vào foundation library

Các domain sau đủ lớn để tạo Knowledge Library riêng: advanced compiler construction/backend optimization; kernel internals/device-driver programming chuyên sâu; formal methods/model checking/theorem proving chuyên sâu; cryptographic protocol proofs; robotics; NLP/CV chuyên sâu; MLOps/foundation-model engineering; cloud-provider/platform engineering; computer graphics engine/game engine chuyên sâu; quantum computing; scientific/HPC computing; embedded/real-time hardware chuyên sâu.

Việc không tạo 20–50 files cho mỗi specialization là **conceptual boundary**, không phải missing foundational topic.

## Quality audit criteria

Một chapter chỉ được coi là đạt khi có problem/phenomenon trước definition, giải thích mechanism và assumptions, examples/counterexamples hoặc edge case phù hợp, terminology English + Korean khi hữu ích, mental model, misconceptions và cross-reference. Prose phải là phần chính; bullet chỉ dùng cho list tự nhiên.

Vòng comprehensive expansion tập trung xử lý ba loại gap: concept có mặt nhưng quá implicit; foundational domain hoàn toàn chưa có; và production mechanism thường bị framework/API che khuất. Kết quả là library tăng từ 59 lên **100 topic chapters** mà vẫn giữ boundary theo mental model thay vì chia file theo độ khó.

## Maintenance rule

Khi mở rộng tiếp, không thêm chapter chỉ vì technology phổ biến. Chỉ thêm khi topic có mental model riêng, là dependency quan trọng cho nhiều domains, hoặc một specialization mới được tách thành library riêng. `computer_science/` phải tiếp tục trả lời câu hỏi: **“Computation và software systems hoạt động từ information tới human/societal impact như thế nào, và constraints/trade-offs nào lặp lại xuyên các layers?”**
