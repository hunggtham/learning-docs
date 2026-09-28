# Mạng & Hệ thống phân tán nâng cao

Phần nâng cao không mở chapter chỉ để bao phủ tên công nghệ. Chapter mới chỉ được thêm khi topic có invariant, state machine và failure model độc lập đủ để trở thành dependency cho nhiều phần khác.

## Canonical chapters

1. [Giao dịch phân tán, exactly-once và failure semantics](./00_distributed_transactions_exactly_once_and_failure_semantics.md)
2. [Failure detector, membership và gossip protocol](./01_failure_detectors_membership_and_gossip.md)
3. [Lease, fencing token và phòng tránh split-brain](./02_leases_fencing_tokens_and_split_brain_prevention.md)
4. [Consensus internals: log replication, reconfiguration và snapshot](./03_consensus_log_replication_reconfiguration_and_snapshots.md)
5. [CRDT, causal consistency và conflict resolution](./04_crdts_causal_consistency_and_conflict_resolution.md)
6. [Multi-region replication và các đánh đổi geo-distributed](./05_multi_region_replication_and_geo_distributed_tradeoffs.md)
7. [Thời gian, đồng hồ, thứ tự và quan hệ nhân quả](./06_time_clocks_ordering_and_causality.md)
8. [BGP, routing policy, convergence và route security](./07_bgp_routing_policy_convergence_and_route_security.md)
9. [Kernel packet path, qdisc, NIC offload và observability](./08_kernel_packet_path_qdisc_nic_offload_and_observability.md)

## Mental models cần đạt

Khi đọc hết track này, người đọc cần phân biệt crash với partition, liveness với safety, suspicion với authority, replication với durability, wall-clock order với causal order, retry với exactly-once illusion, control-plane reachability với data-plane forwarding và application socket progress với packet thực sự đã đi qua wire.

Mỗi protocol/path phải được đọc theo cùng một khung:

```text
vấn đề ban đầu
→ invariant cần giữ
→ mechanism giữ invariant
→ failure/partition/pressure làm assumption nào mất hiệu lực
→ queue hoặc state transition nào đổi behavior
→ evidence nào chứng minh state hiện tại
```

## Network path vẫn thuộc Computer Science

DNS, TCP/QUIC, TLS, proxy/load balancer, connection pooling và network tail latency vẫn thuộc conceptual boundary của `computer_science/`. Foundation nằm tại [`basic/06_networks_distributed_systems`](../../basic/06_networks_distributed_systems/), còn reasoning production end-to-end được nối tại [request path: DNS → TCP/TLS → proxy → runtime → DB](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).

BGP có chapter riêng vì nó có control-plane state machine, inter-domain policy, convergence, route leak/hijack và RIB→FIB boundary độc lập. Kernel packet path có chapter riêng vì socket buffers, transport backpressure, qdisc, driver/NIC rings, interrupt/polling, RSS/ECMP skew và offload tạo một queue/evidence model khác với routing control plane.

Chapter packet path cố ý không duplicate kernel tracing internals. Khi cần instrumentation semantics, đọc [eBPF/tracing](../../03_operating_systems/advanced/08_ebpf_tracing_kernel_observability_and_safety.md); khi cần scheduler/NUMA/DMA mechanics, quay về OS/Architecture owner chapters.

## Production evidence

Network/distributed debugging cần phối hợp packet/connection evidence với distributed state: DNS resolution, connection establishment, retransmission/congestion signals, socket wait, qdisc backlog/sojourn, per-NIC-queue drop/utilization, softirq CPU, offload/capture boundary, proxy/LB queue, request attempts, BGP advertisement/withdrawal, RIB/FIB state, leader term/epoch, quorum membership, replica positions, clock uncertainty và trace causality.

Một timeout không tự chứng minh node đã chết; một BGP session `Established` không chứng minh application reachability; một syscall `send` thành công không chứng minh peer đã nhận bytes; một node `alive` không chứng minh nó còn authority; một replicated entry không tự chứng minh client-visible commit. Đây là các distinction cốt lõi của track.