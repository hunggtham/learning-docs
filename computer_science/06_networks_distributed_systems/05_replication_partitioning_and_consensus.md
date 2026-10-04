# Replication, partitioning và consensus

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Replication, partitioning và consensus**. Route đi từ replication goals/quorum → partitioning/rebalancing → consensus/Raft → leader election/reconfiguration → replication-versus-backup, để authority và availability được phân biệt rõ.

Scaling and độ tin cậy (reliability / 신뢰성) often require dữ liệu (data / 데이터) across multiple nodes. Two orthogonal moves are **replication** — multiple copies of same logical dữ liệu (data / 데이터) — and **partitioning/sharding** — split different dữ liệu (data / 데이터) across nodes. Once multiple replicas may accept/observe changes, thứ tự (ordering / 순서) and agreement become central.

## Replication goals

Replication (복제) can improve availability, read thông lượng (throughput / 처리량), geographic độ trễ (latency / 지연 시간) and durability. But copies create a new bất biến (invariant / 불변식): how do they converge/agree?

Primary-replica mô hình (model / 모델) routes writes through leader, ships log to followers. Synchronous ack from quorum/replicas increases durability/consistency but adds độ trễ (latency / 지연 시간). Async replication lowers ghi (write / 쓰기) độ trễ (latency / 지연 시간) but allows lag/dữ liệu (data / 데이터) mất mát (loss / 손실) on failover depending chính sách (policy / 정책).

Multi-leader accepts writes in multiple regions, improving locality/offline thao tác (operation / 연산) but creates conflicts. Leaderless/quorum designs use versions/vector-like siêu dữ liệu (metadata / 메타데이터)/read-repair/anti-entropy depending cơ sở dữ liệu (database / 데이터베이스).

> **Nối mạch:** Replication đặt mục tiêu availability và durability; quorum tạo điều kiện giao nhau cho read/write, còn partitioning/sharding phân bố dữ liệu và thay đổi phạm vi consensus.

## Quorum intuition

With N replicas, ghi (write / 쓰기) quorum W and read quorum R, điều kiện (condition / 조건) `R + W > N` creates overlap between read and most recent ghi (write / 쓰기) quorum under simplifying các giả định (assumptions / 가정들). But real tính đúng đắn (correctness / 정확성) needs versioning, thất bại (failure / 실패)/reconfiguration, sloppy quorum details; formula alone is not full proof.

> **Nối mạch:** **Partitioning/sharding** nối từ **Quorum intuition** sang **Rebalancing**, vì cơ chế trước tạo đầu vào cho bước sau.

## Partitioning/sharding

Băm (hash / 해시) partitioning distributes keys evenly but loses natural phạm vi (range / 범위) locality; phạm vi (range / 범위) partitioning supports phạm vi (range / 범위) scans but can hotspot skewed ranges. Consistent hashing reduces remapping when nodes thay đổi (change / 변경).

Skew is central: one celebrity/người dùng (user / 사용자)/tenant key can create hot partition even with many nodes. Splitting by composite/thời gian (time / 시간) buckets or workload-aware routing may be needed.

> **Nối mạch:** **Rebalancing** nối từ **Partitioning/sharding** sang **Consensus bài toán (problem / 문제)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Rebalancing

Adding/removing nodes requires moving dữ liệu (data / 데이터) while serving traffic. Rebalancing consumes mạng (network / 네트워크)/disk and can trigger bộ nhớ đệm (cache / 캐시) coldness. Operationally, “quy mô (scale / 규모) out” is not free instantaneous sức chứa (capacity / 용량).

> **Nối mạch:** **Consensus bài toán (problem / 문제)** nối từ **Rebalancing** sang **Raft intuition**, vì cơ chế trước tạo đầu vào cho bước sau.

## Consensus bài toán (problem / 문제)

Consensus asks nodes to agree on a giá trị (value / 값)/log despite failures. Raft/Paxos-family protocols operate under defined thất bại (failure / 실패)/communication các giả định (assumptions / 가정들) and ensure an toàn (safety / 안전) properties.

Replicated máy trạng thái (state machine / 상태 머신) approach: replicas agree on ordered log of commands, then deterministic máy trạng thái (state machine / 상태 머신) applies same chuỗi (sequence / 시퀀스), producing same trạng thái (state / 상태). Consensus is about agreeing thứ tự (order / 순서)/decisions, not magically replicating arbitrary nondeterministic trạng thái (state / 상태).

> **Nối mạch:** **Raft intuition** nối từ **Consensus bài toán (problem / 문제)** sang **Leader election and split brain**, vì cơ chế trước tạo đầu vào cho bước sau.

## Raft intuition

Raft divides thời gian (time / 시간) into terms, elects leader, leader replicates log entries, quorum commitment establishes entries. Election hết thời gian chờ (timeout / 타임아웃) randomness helps avoid repeated split votes. Terms/log matching rules preserve an toàn (safety / 안전) across leader changes.

A committed entry is not simply “leader wrote it locally”; quorum and term rules matter. Reads also need giao thức (protocol / 프로토콜) to ensure leader is hiện tại (current / 현재) if linearizable ngữ nghĩa (semantics / 의미론) required.

> **Nối mạch:** **Leader election and split brain** nối từ **Raft intuition** sang **Reconfiguration**, vì cơ chế trước tạo đầu vào cho bước sau.

## Leader election and split brain

Without quorum/fencing, mạng (network / 네트워크) partition may let two nodes both believe leader and perform conflicting bên ngoài (external / 외부) actions. Consensus/quorum prevents both sides from making authoritative progress if neither has majority; fencing tokens can protect bên ngoài (external / 외부) resources from stale leaders.

> **Nối mạch:** **Reconfiguration** nối từ **Leader election and split brain** sang **Replication vs backup**, vì cơ chế trước tạo đầu vào cho bước sau.

## Reconfiguration

Membership changes are consensus bài toán (problem / 문제) too. Naively switching old→new member sets can create disjoint majorities. Safe protocols use joint consensus or staged changes so quorums overlap appropriately.

> **Nối mạch:** **Replication vs backup** nối từ **Reconfiguration** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Replication vs backup

Replication reduces downtime/node-loss impact but copies corruption/deletes. Backup preserves historical independent khôi phục (recovery / 복구) points. Both needed for different thất bại (failure / 실패) các mô hình (models / 모델들).

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Replication vs backup**; **Dùng chung (common / 공통) Misconceptions** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> **Partitioning decides where dữ liệu (data / 데이터) lives; replication decides how many copies; consensus decides who may authoritatively thứ tự (order / 순서) changes.** Scaling one dimension creates coordination costs in another.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Dùng chung (common / 공통) Misconceptions

**“Three replicas means no dữ liệu (data / 데이터) mất mát (loss / 손실).”** Ack chính sách (policy / 정책), correlated failures and replication lag matter.

**“Consensus is just majority vote.”** giao thức (protocol / 프로토콜) must handle terms, stale messages, log lịch sử (history / 이력), reconfiguration and an toàn (safety / 안전) under timing bất định (uncertainty / 불확실성).

**“Sharding automatically increases all hiệu năng (performance / 성능).”** Cross-shard queries/transactions, skew and rebalancing add costs.

> **Nối mạch:** **Kết nối** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

[Hashing](../01_algorithms_data_structures/04_hashing_and_hash_tables.md) influences partitioning. [Database WAL](../05_data_databases/04_storage_logs_recovery_and_durability.md) often becomes replication log. [Distributed time/failure](./04_distributed_systems_time_failure_and_consistency.md) explains why consensus rules are necessary. [Fault tolerance](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md) turns mechanisms into môi trường vận hành (production / 운영 환경) operations.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
