# Time, failure và consistency trong distributed systems

Distributed system (분산 시스템 / hệ phân tán) gồm components trên nhiều machines/processes giao tiếp qua network. Điều làm nó khó không chỉ “nhiều máy” mà là **không có shared memory hoàn hảo, không có global clock hoàn hảo, message delay không bounded chắc chắn, và failure có thể partial**.

## Partial failure

Single process crash thường dễ nhận: nó dừng. Distributed system có thể thấy node A nói B timeout nhưng C vẫn nói chuyện được với B. Network partition, asymmetric routing, GC pause, overload và packet loss có thể giống failure.

Timeout chỉ nói “chưa nhận response trong thời gian chờ”, không chứng minh remote operation chưa chạy. Đây là nguồn duplicate side effects khi retry.

## Không có global time đơn giản

Physical clocks drift. NTP/PTP synchronize tương đối nhưng uncertainty vẫn tồn tại. Timestamp từ machine A 10:00:00.100 và B 10:00:00.090 không chứng minh event B xảy ra trước theo causal order.

Lamport clocks capture happens-before partial order: local events increment counter; send includes clock; receive advances max+1. Vector clocks có thể detect concurrency nhưng metadata grows with participants.

Logical clocks không đo wall time; chúng encode ordering information.

## Causality

Event A causally precedes B nếu B có thể be influenced by A via program/message chain. Concurrent events không có causal relation. Many consistency models preserve causal order even if total order unnecessary.

## Consistency models

Strong consistency là family, không một term duy nhất. Linearizability makes operations appear atomic in real-time-consistent order. Sequential consistency preserves per-process order but not real-time constraint. Causal consistency preserves causality. Eventual consistency promises replicas converge if updates stop and propagation continues, but conflict resolution semantics matter.

Client/session guarantees như read-your-writes và monotonic reads có thể làm weakly consistent systems dễ dùng hơn.

## CAP theorem đúng context

CAP states that in an asynchronous-ish distributed data system under network partition, one cannot simultaneously guarantee both strong consistency (linearizability-like in common formulation) and availability for every request. Partition tolerance is not optional on real network; when partition occurs, design chooses rejecting/delaying some requests vs serving possibly divergent state.

CAP không nói “chọn 2 trong 3” trong normal operation, và availability trong theorem có technical meaning, not general uptime SLA.

PACELC extends intuition: if Partition, trade Availability vs Consistency; Else, often Latency vs Consistency.

## Safety và liveness

Safety property: bad thing never happens, e.g. two leaders commit conflicting entries for same log position. Liveness: good thing eventually happens, e.g. request eventually completes when conditions recover.

Consensus algorithms often sacrifice liveness during certain partitions to preserve safety.

## Exactly-once myth

Network can lose request or response. Client timing out cannot know if server executed. End-to-end “exactly once effect” usually requires idempotency keys/deduplication/transactional state, not transport magic.

Message brokers may advertise exactly-once within scoped semantics, but external side effects still need coordinated protocol.

## Failure detectors

Perfectly distinguishing slow from failed is impossible in fully asynchronous model. Practical systems use heartbeats/timeouts and eventually accurate assumptions. Tuning failure detector too aggressive causes false positives; too slow delays failover.

## Mental Model

> Distributed systems replace certainty with **messages + uncertainty**. Never infer “did not happen” from timeout. Separate ordering, durability, availability and latency guarantees explicitly.

## Common Misconceptions

**“Eventual consistency means random/stale forever.”** It promises convergence under conditions, but conflict and session semantics must be defined.

**“CAP means every distributed DB chooses exactly CA/CP/AP.”** The theorem focuses partition periods and specific guarantees; real systems expose tunable operations/models.

**“Timestamp sorts events correctly globally.”** Clock skew and uncertainty break causal inference unless stronger clock protocol/assumptions exist.

## Kết nối

[Concurrency](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md) has shared-memory ordering; distributed systems remove shared clock/memory and add partial failure. Next [replication/partitioning/consensus](./05_replication_partitioning_and_consensus.md) builds mechanisms for these constraints.
