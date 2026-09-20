# Latency, throughput, capacity và scalability

Performance engineering không phải “làm code nhanh” chung chung. Hệ thống có latency distribution, throughput, resource utilization, queueing và workload shape. Optimization đúng phải xác định bottleneck theo measurements và model.

## Latency và throughput

Latency = time một operation/request hoàn thành. Throughput = operations per unit time. Chúng liên quan nhưng không identical: batching có thể tăng throughput nhưng tăng individual wait; low latency one request không chứng minh high throughput under load.

Report averages alone hides tail. p95/p99 latency matter because distributed request fan-out can be dominated by slowest dependency.

## Utilization, saturation và queueing

Khi arrival rate gần service capacity, queue grows và latency tăng nonlinearly. Simple M/M/1 intuition gives utilization `ρ=λ/μ`; expected queue delay blows up as ρ→1. Real workloads not M/M/1, but principle remains: running permanent 100% capacity leaves no burst headroom.

Saturation signal can be CPU run queue, disk queue, connection pool wait, thread pool queue or GC pressure.

## Little's Law

For stable system:

\[
L = \lambda W
\]

Average in-flight L = throughput/arrival rate λ × average time W. If service handles 1000 req/s and average latency 0.2 s, roughly 200 requests in system on average.

This connects concurrency limits to latency/throughput quantitatively.

## Bottleneck

End-to-end throughput limited by constrained resource/stage. Speeding non-bottleneck gives little system gain. Profiling, tracing and resource metrics identify where time/capacity spent.

Amdahl's Law similarly limits optimization speedup by fraction improved.

## Vertical vs horizontal scaling

Scale up adds CPU/RAM/faster device to one machine. Scale out adds nodes. Horizontal scaling requires partitionable workload/state management, load balancing and distributed coordination; it is not automatic.

Stateless request processing scales easier, but persistent state still lives somewhere and can bottleneck DB/cache/network.

## Caching

Cache stores expensive result/data closer to use. Hit ratio, miss penalty, eviction, freshness và invalidation determine value.

Cache-aside loads on miss; write-through/write-back alter consistency. TTL bounds staleness but doesn't guarantee invalidation exactly when source changes.

Cache stampede occurs many clients miss same hot key and recompute simultaneously; single-flight/locking/jittered expiry mitigate.

## Batching

Batching amortizes fixed overhead: syscall, network RTT, transaction commit, GPU launch. But batch too large increases wait/memory and failure scope. Choose batch by throughput-latency SLO.

## Connection pools

DB/network connection setup costly, so pools reuse connections and bound concurrency. Too small creates waits; too large overwhelms database and raises contention. Pool is admission control, not just optimization.

## Load balancing

Round-robin, least-connections, consistent hashing and weighted strategies distribute work under different assumptions. Health check latency/staleness and sticky sessions affect balance. Locality/caching may favor affinity but risk hotspots.

## Performance measurement

Measure representative production-like workload, warm-up where runtime JIT/cache matters, percentiles, resource counters and saturation. Microbenchmarks isolate operation but don't substitute end-to-end tests.

## Mental Model

> Performance is a **flow through finite resources**. Arrival rate creates work; service centers consume capacity; queues store excess; latency reveals waiting. Optimize bottleneck and protect headroom.

## Common Misconceptions

**“CPU 100% means efficient.”** Under latency workload it may mean saturated with exploding queue.

**“Cache makes data access O(1).”** Miss path, network, eviction and consistency still matter.

**“Horizontal scaling solves database bottleneck.”** State partition/replication and coordination may become new bottlenecks.

## Kết nối

[Complexity](../01_algorithms_data_structures/01_complexity_and_asymptotic_analysis.md) models growth of local algorithms; [memory hierarchy](../02_computer_architecture/02_memory_hierarchy_and_cache.md) hardware performance; [fault tolerance](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md) uses capacity headroom and load shedding.
