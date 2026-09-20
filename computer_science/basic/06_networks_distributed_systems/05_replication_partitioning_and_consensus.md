# Replication, partitioning và consensus

Scaling and reliability often require data across multiple nodes. Two orthogonal moves are **replication** — multiple copies of same logical data — and **partitioning/sharding** — split different data across nodes. Once multiple replicas may accept/observe changes, ordering and agreement become central.

## Replication goals

Replication (복제) can improve availability, read throughput, geographic latency and durability. But copies create a new invariant: how do they converge/agree?

Primary-replica model routes writes through leader, ships log to followers. Synchronous ack from quorum/replicas increases durability/consistency but adds latency. Async replication lowers write latency but allows lag/data loss on failover depending policy.

Multi-leader accepts writes in multiple regions, improving locality/offline operation but creates conflicts. Leaderless/quorum designs use versions/vector-like metadata/read-repair/anti-entropy depending database.

## Quorum intuition

With N replicas, write quorum W and read quorum R, condition `R + W > N` creates overlap between read and most recent write quorum under simplifying assumptions. But real correctness needs versioning, failure/reconfiguration, sloppy quorum details; formula alone is not full proof.

## Partitioning/sharding

Hash partitioning distributes keys evenly but loses natural range locality; range partitioning supports range scans but can hotspot skewed ranges. Consistent hashing reduces remapping when nodes change.

Skew is central: one celebrity/user/tenant key can create hot partition even with many nodes. Splitting by composite/time buckets or workload-aware routing may be needed.

## Rebalancing

Adding/removing nodes requires moving data while serving traffic. Rebalancing consumes network/disk and can trigger cache coldness. Operationally, “scale out” is not free instantaneous capacity.

## Consensus problem

Consensus asks nodes to agree on a value/log despite failures. Raft/Paxos-family protocols operate under defined failure/communication assumptions and ensure safety properties.

Replicated state machine approach: replicas agree on ordered log of commands, then deterministic state machine applies same sequence, producing same state. Consensus is about agreeing order/decisions, not magically replicating arbitrary nondeterministic state.

## Raft intuition

Raft divides time into terms, elects leader, leader replicates log entries, quorum commitment establishes entries. Election timeout randomness helps avoid repeated split votes. Terms/log matching rules preserve safety across leader changes.

A committed entry is not simply “leader wrote it locally”; quorum and term rules matter. Reads also need protocol to ensure leader is current if linearizable semantics required.

## Leader election and split brain

Without quorum/fencing, network partition may let two nodes both believe leader and perform conflicting external actions. Consensus/quorum prevents both sides from making authoritative progress if neither has majority; fencing tokens can protect external resources from stale leaders.

## Reconfiguration

Membership changes are consensus problem too. Naively switching old→new member sets can create disjoint majorities. Safe protocols use joint consensus or staged changes so quorums overlap appropriately.

## Replication vs backup

Replication reduces downtime/node-loss impact but copies corruption/deletes. Backup preserves historical independent recovery points. Both needed for different failure models.

## Mental Model

> **Partitioning decides where data lives; replication decides how many copies; consensus decides who may authoritatively order changes.** Scaling one dimension creates coordination costs in another.

## Common Misconceptions

**“Three replicas means no data loss.”** Ack policy, correlated failures and replication lag matter.

**“Consensus is just majority vote.”** Protocol must handle terms, stale messages, log history, reconfiguration and safety under timing uncertainty.

**“Sharding automatically increases all performance.”** Cross-shard queries/transactions, skew and rebalancing add costs.

## Kết nối

[Hashing](../01_algorithms_data_structures/04_hashing_and_hash_tables.md) influences partitioning. [Database WAL](../05_data_databases/04_storage_logs_recovery_and_durability.md) often becomes replication log. [Distributed time/failure](./04_distributed_systems_time_failure_and_consistency.md) explains why consensus rules are necessary. [Fault tolerance](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md) turns mechanisms into production operations.
