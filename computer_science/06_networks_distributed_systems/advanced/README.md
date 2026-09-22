# Mạng & Hệ thống phân tán nâng cao

Phần nâng cao không mở thêm chapter chỉ để bao phủ thêm tên công nghệ. Các chapter hiện có được dùng như các điểm neo để reasoning từ failure ambiguity, authority và ordering tới replication, consistency và production behavior.

## Canonical chapters

1. [Giao dịch phân tán, exactly-once và failure semantics](./00_distributed_transactions_exactly_once_and_failure_semantics.md)
2. [Failure detector, membership và gossip protocol](./01_failure_detectors_membership_and_gossip.md)
3. [Lease, fencing token và phòng tránh split-brain](./02_leases_fencing_tokens_and_split_brain_prevention.md)
4. [Consensus internals: log replication, reconfiguration và snapshot](./03_consensus_log_replication_reconfiguration_and_snapshots.md)
5. [CRDT, causal consistency và conflict resolution](./04_crdts_causal_consistency_and_conflict_resolution.md)
6. [Multi-region replication và các đánh đổi geo-distributed](./05_multi_region_replication_and_geo_distributed_tradeoffs.md)
7. [Thời gian, đồng hồ, thứ tự và quan hệ nhân quả](./06_time_clocks_ordering_and_causality.md)

## Mental models cần đạt

Khi đọc hết track này, người đọc cần phân biệt rõ crash với partition, liveness với safety, suspicion với authority, replication với durability, wall-clock order với causal order và retry với exactly-once illusion.

Mỗi protocol phải được đọc theo cùng một khung:

```text
vấn đề ban đầu
→ invariant cần giữ
→ mechanism giữ invariant
→ failure/partition làm assumption nào mất hiệu lực
→ performance pressure đổi behavior ra sao
→ evidence nào chứng minh state hiện tại
```

## Network path không bị tách thành library khác

DNS, TCP/QUIC, TLS, proxy/load balancer, connection pooling và network tail latency vẫn thuộc conceptual boundary của `computer_science/`. Phần foundation nằm tại [`basic/06_networks_distributed_systems`](../../basic/06_networks_distributed_systems/), còn reasoning production end-to-end được nối tại [request path: DNS → TCP/TLS → proxy → runtime → DB](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).

Không tạo chapter riêng cho service mesh, broker hay QUIC chỉ vì technology phổ biến. Chỉ mở rộng canonical chapter khi nội dung mới tạo mental model về authority, ordering, congestion, queueing, failure propagation hoặc consistency mà tài liệu hiện tại chưa có.

## Production evidence

Network/distributed debugging cần phối hợp packet/connection evidence với distributed state: DNS resolution, connection establishment, retransmission/congestion signals, proxy/LB queue, request attempts, leader term/epoch, quorum membership, replica positions, clock uncertainty và trace causality.

Một timeout không tự chứng minh node đã chết; một node `alive` không chứng minh nó còn authority; một replicated entry không tự chứng minh client-visible commit. Đây là các distinction cốt lõi của track.