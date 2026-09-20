# Knowledge Connection — Trade-off xuyên Computer Science

Nhiều câu hỏi kỹ thuật không có answer “cái nào tốt nhất” vì resources và guarantees cạnh tranh. Một cách trưởng thành để reasoning là xác định objective, constraint và trade-off dimension thay vì học rule tuyệt đối.

## Time ↔ Space

Memoization dùng memory để giảm recomputation. Index dùng storage/RAM để giảm query time. Cache dùng duplicated state để giảm latency. Bloom filter dùng bits để tránh expensive lookups nhưng chấp nhận false positives.

Ngược lại, compression dùng CPU để giảm storage/network bandwidth.

Không có “optimize memory” hoặc “optimize speed” độc lập; workload và bottleneck quyết định.

## Latency ↔ Throughput

Batching tăng throughput bằng amortizing fixed cost nhưng item đầu chờ batch fill. Larger queues smooth bursts nhưng tăng queueing latency. Database group commit batches fsync to improve throughput at small latency cost.

Interactive systems ưu tiên tails; batch analytics ưu tiên aggregate throughput.

## Consistency ↔ Availability/Latency

Synchronous quorum write waits more replicas: stronger durability/consistency under failures but higher latency/less availability during partition. Async replication returns earlier but allows lag.

CAP/PACELC are formalized views of some distributed trade-offs; they are not slogans for all design.

## Isolation ↔ Concurrency

Serializable transaction gives strong reasoning but may block/abort more. Weaker isolation permits more overlap but application must tolerate anomalies.

OS coarse lock simpler correctness but reduces parallelism; fine locks increase concurrency and complexity/deadlock surface.

Same mental structure at different layers.

## Abstraction ↔ Control

High-level managed runtime hides memory and offers safety/productivity. Low-level language gives layout/lifetime control but transfers responsibility. ORM hides SQL repetition but can produce N+1/query inefficiency if developer ignores database model.

Abstraction reduces cognitive load until hidden detail affects requirement; then leaky abstraction requires descending a layer.

## Generality ↔ Optimization

Generic algorithm/API works many inputs but cannot exploit specific structure. Counting sort exploits integer range; specialized SIMD kernel exploits alignment; prepared query plan may exploit known parameter distribution.

Specialization improves speed at cost code complexity/portability.

## Safety ↔ Performance/Flexibility

Bounds checks prevent memory corruption but add checks (often optimized). Cryptographic verification adds CPU/latency. Permission boundaries add syscalls/IPC. Removing checks for speed enlarges trusted computing base/risk.

Good systems optimize safety mechanisms rather than silently remove guarantees.

## Redundancy ↔ Cost/Complexity

Replication improves availability/read scale but costs hardware, bandwidth and consistency coordination. Backups cost storage/operations but protect logical corruption. Multiple zones reduce correlated failure but increase network latency/cost.

## Freshness ↔ Cache performance

Long TTL raises hit ratio/lower load but returns stale data longer. Short TTL improves freshness but increases origin traffic and stampede risk. Event invalidation improves freshness but adds delivery/failure complexity.

## Normalize ↔ Denormalize

Normalized DB reduces redundant facts/update anomalies; denormalized read model avoids joins and supports analytics. Derived state demands refresh/invalidation logic.

## Strong typing/static checks ↔ flexibility/build feedback

Static guarantees catch classes bugs earlier but require type modeling and compile checks. Dynamic systems permit rapid structural change but shift detection to runtime/tests/tooling. Modern ecosystems mix gradual typing, inference and runtime contracts.

## Optimize the real constraint

First-principles trade-off process:

1. define property/SLO/invariant;
2. identify bottleneck/resource;
3. list assumptions and failure model;
4. compare options on dimensions, not labels;
5. measure/validate under representative workload;
6. preserve escape path if assumptions change.

## Mental Model

> Most architecture decisions are **moving cost, risk or complexity between dimensions**, not eliminating it. Ask “what became cheaper, and what became more expensive?”

## Cross-references

This chapter connects [complexity](../01_algorithms_data_structures/01_complexity_and_asymptotic_analysis.md), [cache](../02_computer_architecture/02_memory_hierarchy_and_cache.md), [transaction isolation](../05_data_databases/02_transactions_acid_and_concurrency_control.md), [distributed consistency](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md), [reliability](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md) and [performance](../08_software_systems/02_performance_capacity_and_scalability.md).
