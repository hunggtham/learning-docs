# Advanced Networks & Distributed Systems

Roadmap:

1. [Distributed transactions, exactly-once và failure semantics](./00_distributed_transactions_exactly_once_and_failure_semantics.md)
2. [Failure detectors, membership và gossip protocols](./01_failure_detectors_membership_and_gossip.md)
3. [Leases, fencing tokens và split-brain prevention](./02_leases_fencing_tokens_and_split_brain_prevention.md)
4. Consensus internals: log replication, reconfiguration và snapshots
5. CRDTs, causal consistency và conflict resolution
6. Multi-region replication và geo-distributed trade-offs
7. Message brokers, consumer groups và stream partitioning
8. Backpressure, load shedding và overload collapse
9. Service discovery, proxies, meshes và connection management
10. Network tail latency, retransmission và congestion interactions
11. QUIC internals, multiplexing và migration
12. Distributed observability, tracing context và clock uncertainty

Phần hiện có tập trung vào failure semantics và authority: transaction không hoàn hảo, peer failure không thể biết tuyệt đối, và stale leader phải bị fence tại resource boundary.