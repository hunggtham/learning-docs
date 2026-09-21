# Mạng & Hệ thống phân tán nâng cao

Roadmap:

1. [Giao dịch phân tán, exactly-once và failure semantics](./00_distributed_transactions_exactly_once_and_failure_semantics.md)
2. [Failure detector, membership và gossip protocol](./01_failure_detectors_membership_and_gossip.md)
3. [Lease, fencing token và phòng tránh split-brain](./02_leases_fencing_tokens_and_split_brain_prevention.md)
4. [Consensus internals: log replication, reconfiguration và snapshot](./03_consensus_log_replication_reconfiguration_and_snapshots.md)
5. [CRDT, causal consistency và conflict resolution](./04_crdts_causal_consistency_and_conflict_resolution.md)
6. [Multi-region replication và các đánh đổi geo-distributed](./05_multi_region_replication_and_geo_distributed_tradeoffs.md)
7. [Thời gian, đồng hồ, thứ tự và quan hệ nhân quả](./06_time_clocks_ordering_and_causality.md)
8. Message broker, consumer group và stream partitioning
9. Backpressure, load shedding và overload collapse
10. Service discovery, proxy, service mesh và connection management
11. Network tail latency, retransmission và congestion interaction
12. QUIC internals, multiplexing và connection migration
13. Distributed observability, tracing context và clock uncertainty

Bảy chapter hiện có đi từ failure ambiguity và authority sang consensus, convergence, geo-replication rồi quay lại nền tảng thời gian/ordering cần để hiểu đúng causality, lease, timestamp và timeout. Phần tiếp theo nên nối messaging, overload và network behavior ở production scale thay vì tạo thêm một root domain mới.