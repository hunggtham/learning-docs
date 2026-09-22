# Sao chép đa vùng và các đánh đổi của hệ thống phân tán theo địa lý

Khi các bản sao nằm ở nhiều vùng địa lý, tốc độ ánh sáng, topology mạng và failure-domain trở thành một phần của consistency model. Không protocol nào biến một round trip Seoul–Virginia thành memory access cục bộ. Architecture phải quyết định **invariant nào xứng đáng trả coordination cost xuyên vùng** và invariant nào có thể giữ cục bộ rồi reconcile sau.

Mental model của chương này là: **multi-region replication phân phối authority và history qua khoảng cách. Correctness phụ thuộc vào ai có quyền accept write, replica nào có history đủ mới để serve/read/promote, và failover có ngăn old authority tiếp tục ghi hay không.**

## 1. Bài toán ban đầu: latency, availability và consistency cùng chịu physics

Một synchronous coordination round qua nhiều regions có latency floor theo network propagation + processing. Nếu write phải chờ remote quorum, user-facing latency chứa ít nhất một phần remote RTT và remote queue/storage cost.

Tối ưu software có thể giảm overhead nhưng không bỏ khoảng cách vật lý. Vì vậy region placement là **semantic/capacity decision**, không chỉ deployment preference.

## 2. Invariant đầu tiên: chỉ một authority hợp lệ được phép quyết định history cần single-writer

Với single-leader system, invariant thường là:

> Tại một epoch/term có thẩm quyền, chỉ leader hợp lệ được phép accept writes tạo authoritative history.

Network partition làm hai nodes đều “không nghe thấy nhau”; nó không chứng minh node bên kia chết. Failover vì vậy phải dựa vào consensus/lease/fencing/epoch mechanism chứ không chỉ health-check timeout.

Nếu primary cũ vẫn ghi sau khi new primary được promoted, split-brain có thể tạo two divergent histories mà async replication không tự hòa giải được.

## 3. Replication state không phải binary “đồng bộ/chưa đồng bộ”

Một log entry/write có thể đi qua:

```text
created at leader
→ appended locally
→ persisted locally
→ sent
→ received by replica
→ persisted remotely
→ acknowledged by quorum/rule
→ applied to replica state
→ visible to replica reads
```

Các systems đặt acknowledgement/read boundary ở vị trí khác nhau. Do đó cần hỏi cụ thể:

```text
ack sau receive hay persist?
quorum nào phải ack?
read replica serve theo received, applied hay committed frontier?
promotion cần frontier nào?
```

Số replicas tự nó không trả lời durability/consistency.

## 4. Synchronous replication đổi failure model và critical path

Nếu client chỉ nhận success sau remote quorum persistence, RPO trước một số node failures có thể nhỏ hơn. Đổi lại remote network/storage nằm trên critical path.

Một follower chậm có thể kéo p99 nếu quorum policy cần nó; protocol có thể chọn quorum subset, nhưng lựa chọn đó phải vẫn giữ intersection/authority invariant.

Câu hỏi không phải “sync có an toàn hơn async” chung chung. Câu hỏi là **acknowledgement này hứa survive failure set nào?**

## 5. Asynchronous replication tạo failure window có chủ đích

Leader có thể ack local durable write rồi ship log sau. Foreground latency thấp hơn nhưng failover trước replication có thể mất acknowledged writes tùy contract.

Window này phải được diễn đạt bằng **mục tiêu điểm khôi phục (Recovery Point Objective, RPO)** và measured replication lag, không bằng câu “thường chỉ vài ms”. Tail lag trong incident mới là thứ quyết định data-loss window.

## 6. Read consistency phải được thiết kế riêng

Read replica giảm latency và offload leader, nhưng có thể stale. Các guarantees có strength khác nhau:

```text
eventual read
monotonic reads
read-your-writes
causal/session consistency
linearizable/leader/quorum-style read
```

Nếu user vừa update profile ở region A rồi request chuyển sang replica B chưa apply write, user có thể thấy old state.

Read-your-writes có thể dùng session/version token, sticky routing, wait-until-replica-frontier, hoặc route tới authority đủ mới. Mechanism khác nhau nhưng invariant là:

> Read phải được serve từ replica có history frontier đáp ứng consistency contract của request.

## 7. Replica lag là một distance trong history, không chỉ seconds

Time-based lag dễ hiểu nhưng có thể gây nhầm khi clocks/skew hoặc write rate biến động. Một replica 2 seconds behind trong burst 100k writes khác 2 seconds behind lúc idle.

Useful evidence gồm log/LSN/offset/commit/applied positions và queue/backlog. Mental model là đo **history distance + application delay + network delay**, không chỉ một wall-clock number.

## 8. Failover là chuyển authority, không chỉ đổi DNS

Một safe failover cần giải nhiều state transitions:

```text
xác định old authority không còn quyền ghi
→ chọn candidate có history đủ hợp lệ
→ assign new epoch/term/fencing token
→ promote
→ redirect clients/control plane
→ invalidate/drain stale connections/routes
→ verify read/write invariants
```

DNS/TTL chỉ là traffic steering. Nó không giải authority. Connection pools và clients có thể giữ old endpoint lâu hơn DNS change.

Đọc [leases, fencing tokens và split-brain prevention](./02_leases_fencing_tokens_and_split_brain_prevention.md).

## 9. Failover candidate mới nhất chưa chắc tự động là candidate an toàn

Một replica có nhiều bytes nhất nhưng bytes đó chưa chắc thuộc committed authoritative history nếu protocol chưa xác nhận. Consensus system cần term/commit-index-like authority rules; primary-replica system cần promotion rule rõ.

Invariant là **new leader không được invent history trái với commit contract đã hứa cho clients**.

Đây là lý do “copy nhiều data nhất rồi promote” không phải generic failover algorithm.

## 10. Failback còn khó hơn failover nếu histories đã đổi

Sau khi region cũ hồi phục, không nên đơn giản bật write lại. Nó có thể chứa stale/divergent state.

Safe failback thường cần:

```text
rejoin as follower/non-authoritative
→ catch up / snapshot / repair
→ prove frontier consistency
→ only then consider authority transfer
```

Operational runbook phải coi failback là protocol transition, không phải reverse DNS edit.

## 11. Multi-leader chuyển problem từ authority sang conflict semantics

Cho phép mỗi region accept local writes giảm write latency và tăng autonomy, nhưng concurrent writes có thể xung đột.

Một last-write-wins rule dựa timestamp có thể làm mất business intent và phụ thuộc clock assumptions. Unique username, inventory decrement, quota và account balance thường có invariants không thể reconcile chỉ bằng chọn “latest value”.

Cần phân loại state:

```text
commutative/mergeable
conflict-tolerant
requires single authority or coordination
```

Global coordination chỉ nên đặt tại invariants thật sự không thể tách/merge an toàn.

## 12. CRDT giải một lớp conflict nhưng không xóa business constraints

CRDT cho phép merge state với algebraic properties cụ thể mà không cần total order cho mọi operation. Nhưng nếu business invariant là “không bán quá 100 vé toàn cầu”, merge-friendly counter không tự tạo capacity reservation global an toàn.

Đọc [CRDT, causal consistency và conflict resolution](./04_crdts_causal_consistency_and_conflict_resolution.md).

## 13. Geo-partitioning giữ coordination gần ownership tự nhiên

Nếu users/data có “home region”, partition by ownership có thể giữ đa số writes local và chỉ coordinate cross-region khi business operation thật sự vượt boundary.

Ví dụ:

```text
customer profile owned by home region
regional inventory owned locally
analytics replicated globally asynchronously
```

Boundary tốt giảm global coordination volume. Boundary xấu tạo cross-region distributed transaction cho mọi request.

## 14. Hotspot và skew phá assumption “traffic phân bố đều”

Geo sharding theo user-id có thể trông cân bằng trên paper nhưng tenant lớn, event viral hoặc region traffic peak tạo skew.

Một shard/leader nóng có thể saturate CPU/network/storage trong khi fleet average thấp. Multi-region capacity planning cần nhìn per-shard/per-tenant frontier, không chỉ aggregate regional utilization.

## 15. Failure domains phải độc lập thật sự

Ba replicas không tương đương ba independent copies nếu cùng rack, power domain, network control plane, credential root, storage backend hoặc deployment bug.

Availability reasoning cần map:

```text
hardware failure domain
network failure domain
region/provider/control-plane dependency
software rollout/config dependency
security/identity dependency
```

Correlated failure thường phá architecture mà “N regions” marketing diagram không thể hiện.

## 16. Active-active không đồng nghĩa zero downtime

Active-active regions vẫn có shared dependencies: global identity issuer, schema registry, KMS root, DNS/control plane, replication channel hoặc common binary/config.

Một bad deploy hoặc security policy rollout có thể fail tất cả regions cùng lúc. Geographic redundancy chỉ bảo vệ failure modes thực sự independent với nó.

## 17. Cross-region timeout/retry có thể khuếch đại outage

Remote call có RTT cao và variability lớn hơn. Timeout quá sát normal tail tạo false timeout; client retry sang region khác có thể duplicate work và tăng load đúng lúc failover.

Causal loop:

```text
region latency ↑
→ timeout ↑
→ retry/failover traffic ↑
→ alternate region queue ↑
→ its latency ↑
→ more retries
→ cascading regional failure
```

Failover capacity phải tính **redirected demand**, không chỉ normal local traffic.

Đọc [end-to-end request và retry overload](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).

## 18. Consistency policy cũng là capacity policy

Strong remote read/write yêu cầu coordination/network/storage trên critical path. Stale-local read giảm cost nhưng đổi semantics. Session consistency ở giữa cần token/frontier tracking.

System Design nên phân loại operations theo invariant:

```text
must be globally current
must read own write
can tolerate seconds stale
can reconcile asynchronously
```

Sau đó mới chọn replication/read path. Chọn “strong consistency toàn bộ” hoặc “eventual toàn bộ” trước khi phân loại workload thường tạo cost hoặc correctness problem không cần thiết.

## 19. Data residency và security boundary đi cùng replication topology

Data nào được replicate sang region nào là cả performance, privacy, compliance và blast-radius decision. Logs, backups, caches và search indexes cũng là replicas theo nghĩa governance dù application architecture không gọi chúng như vậy.

Identity/KMS topology cần phù hợp: region có thể autonomous khi network partition hay mọi decrypt/auth operation vẫn phụ thuộc control plane global?

## 20. Production evidence phải reconstruct authority + history timeline

Evidence hữu ích:

```text
Replication:
- leader/term/epoch
- commit/durable/applied frontier per replica
- send/receive/apply lag
- snapshot/catch-up state

Network:
- inter-region RTT/loss/retransmission
- bandwidth/queue saturation

Storage:
- WAL/log flush latency per region
- replica persistence latency

Traffic:
- read/write routing by region
- failover/retry rate
- redirected load and queue wait

Correctness:
- stale-read/session-token violations
- conflict/repair events
- fencing/promotion history
```

Một “replication lag = 0” metric không chứng minh no split-brain; một leader election log không chứng minh replica storage healthy. Cần nối authority và data frontier.

## 21. Failure testing phải bao gồm partial failure, không chỉ kill process

Test đáng giá:

```text
partition leader khỏi subset replicas
inject asymmetric packet loss/latency
slow one replica storage
expire lease/fencing boundary
fail leader với outstanding acknowledged/unacknowledged writes
route reads tới lagging replica
promote rồi rejoin old leader
simulate capacity after full-region traffic shift
```

Sau test, kiểm tra data-loss window đúng contract, no dual authority, session/read consistency đúng policy và old leader không thể mutate state sau fencing.

## 22. Abstraction nào thực sự quyết định behavior?

Nếu user đọc stale data, consistency/read-routing frontier quyết định behavior. Nếu failover mất data, ack/replication/persistence rule mới là trọng tâm. Nếu outage lan sang region khỏe, capacity/retry feedback có thể là root mechanism. Nếu two primaries cùng ghi, authority/fencing protocol là invariant bị phá.

## 23. Mô hình tư duy

> Multi-region replication là bài toán **phân phối authority, history và capacity qua khoảng cách**. Synchronous coordination trả latency để làm commit frontier mạnh hơn; asynchronous replication đổi latency lấy failure window; replica reads đổi freshness lấy locality; failover là chuyển authority được fencing, không phải chỉ đổi route. **Global coordination chỉ nên đặt ở invariant cần nó, còn production evidence phải theo dõi cả authority frontier lẫn data frontier.**

## Kết nối

Ôn [distributed consistency foundation](../../basic/06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md), [replication/consensus foundation](../../basic/06_networks_distributed_systems/05_replication_partitioning_and_consensus.md), đọc [failure detectors](./01_failure_detectors_membership_and_gossip.md), [leases/fencing](./02_leases_fencing_tokens_and_split_brain_prevention.md), [consensus internals](./03_consensus_log_replication_reconfiguration_and_snapshots.md), [time/causality](./06_time_clocks_ordering_and_causality.md), [MVCC/WAL](../../05_data_databases/advanced/00_mvcc_visibility_wal_and_recovery_internals.md) và [durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).