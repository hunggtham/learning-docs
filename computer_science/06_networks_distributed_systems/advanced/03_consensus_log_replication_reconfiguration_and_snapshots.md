# Consensus internals: log replication, reconfiguration và snapshots

Distributed system cần consensus khi nhiều nodes phải thống nhất một sequence quyết định dù message delay, node crash và network partition. Consensus không làm network đáng tin; nó giữ một invariant mạnh hơn trên nền communication không đáng tin: **không có hai histories đã commit mâu thuẫn cùng được coi là authoritative trong cùng protocol history.**

Ở mức advanced, cần tách **safety** khỏi **liveness**. Safety hỏi “điều sai có thể xảy ra không?”; liveness hỏi “hệ thống có tiếp tục tiến triển không?”. Network partition có thể làm liveness dừng có chủ đích để safety còn giữ.

## 1. State machine replication biến consensus thành bài toán ordering

Nếu replicas chạy cùng deterministic state machine và apply cùng commands theo cùng order, state của chúng có thể hội tụ giống nhau.

Do đó vấn đề trở thành thống nhất một ordered log:

```text
command 1
command 2
command 3
...
```

Leader-based protocol như Raft làm model này rõ: leader đề xuất entries, replicas ghi entries, quorum rule quyết định entry nào đủ an toàn để commit, rồi state machine apply committed entries theo order.

Invariant quan trọng không phải “mọi replica luôn giống nhau tức thì”. Replica có thể lag. Invariant là **history đã commit không được bị thay bằng history mâu thuẫn sau election/failover hợp lệ.**

## 2. Term/epoch biến authority thành một thứ có ordering

Leadership không phải quyền vĩnh viễn. Term/epoch tăng qua elections. Message từ leader cũ có epoch thấp bị xem là stale.

Điều này giải quyết một failure phổ biến: process cũ bị pause/network partition, sau đó sống lại và vẫn tin mình là leader.

Term một mình chưa đủ; downstream side effects ngoài consensus log có thể vẫn bị old leader thực hiện. Khi cần bảo vệ external resource, **fencing token** hoặc monotonic epoch phải được resource đó kiểm tra.

Đọc cùng [Leases, fencing tokens và split-brain prevention](./02_leases_fencing_tokens_and_split_brain_prevention.md).

## 3. Quorum intersection là core safety argument

Majority quorums có property mọi hai majorities giao nhau ít nhất một node. Intersection giúp election/commit rules mang thông tin committed history sang future authority set.

Safety không đến từ ý tưởng “đa số luôn đúng”. Nó đến từ **set intersection + protocol rules về node nào được vote/accept history nào**.

Nếu cấu hình membership thay đổi sai làm old/new quorum không còn overlap cần thiết, system có thể tạo split-brain history dù mỗi phía đều thấy mình có “đa số” trong config riêng.

## 4. Append local, replicate, commit và apply là bốn mốc khác nhau

Một log entry có thể ở nhiều trạng thái:

```text
accepted by leader
→ appended locally
→ replicated to followers
→ satisfies commit rule
→ applied to state machine
→ observed by client/read path
```

Trộn các mốc này dẫn tới acknowledgement bug. Nếu API hứa write survive leader loss, leader không được ack chỉ vì local append đã xong.

Commit contract còn phụ thuộc local durability: follower “có entry” nhưng chỉ ở volatile memory có thể không đủ cho failure model mạnh hơn.

## 5. Safety và durability giao nhau tại acknowledgement

Consensus thường được dạy ở network/protocol layer; durability thường được dạy ở storage layer. Production system phải nối cả hai.

Một committed entry theo quorum logic chỉ survive power/process failures như contract hứa nếu replicas giữ log theo persistence rules tương ứng.

Causal chain:

```text
client write
→ leader log append
→ follower replication
→ local durable state theo policy
→ quorum commit
→ client ack
```

Nếu ack xảy ra trước durability/quorum condition cần thiết, consistency protocol có thể đúng trên giấy nhưng product durability guarantee vẫn sai.

Xem [đường durability xuyên tầng](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

## 6. Network partition: node alive không có nghĩa node có authority

Một minority partition có thể có processes hoàn toàn khỏe, CPU thấp và disk bình thường nhưng không được commit writes nếu protocol cần quorum.

Đây là deliberate availability trade-off để bảo vệ single authoritative history.

Failure detector chỉ nói “tôi nghi node kia không reachable/healthy”. Consensus rules mới quyết định ai có quyền commit.

Không được biến suspicion thành authority bằng timeout đơn giản.

## 7. Election timeout là liveness tuning, không phải correctness proof duy nhất

Timeout quá ngắn có thể gây election churn khi network jitter/GC pause; quá dài làm failover chậm.

Timeout tuning chủ yếu ảnh hưởng liveness và operational behavior. Safety phải đến từ term/voting/log rules, không dựa vào assumption “hai leaders chắc không overlap vì timeout”.

Đây là pattern quan trọng trong distributed systems: **clock/timing có thể giúp progress nhưng safety nên dựa vào invariant protocol khi có thể.**

## 8. Log matching và leader completeness giữ history

Leader-based consensus thường cần rules để đảm bảo candidate thiếu committed history không trở thành authority rồi ghi đè history đó.

Intuition cần giữ:

```text
future leader phải mang đủ committed prefix
followers không được chấp nhận arbitrary conflicting suffix
```

Conflict repair được phép thay speculative/uncommitted suffix, nhưng committed prefix phải được bảo toàn theo protocol.

Đây là nơi “replication là copy log” trở thành state-machine protocol thực sự.

## 9. Commit index và apply index không nên bị trộn

Entry có thể committed nhưng state machine chưa apply kịp. Replica lag có thể đến từ network replication hoặc apply throughput.

Nếu read path trả state tại apply index cũ nhưng caller tưởng đang đọc committed-latest, consistency guarantee bị yếu hơn mong đợi.

Observability nên phân biệt:

```text
match/replication position
commit position
applied position
```

Một replica “caught up log” chưa chắc “caught up application state”.

## 10. Linearizable read cần chứng minh authority hiện tại

Read từ leader tưởng miễn phí vì không append log mới. Nhưng stale leader bị partition có thể chưa biết mình đã mất quorum.

Linearizable read cần mechanism xác nhận leader vẫn có authority/current commit state, ví dụ quorum confirmation/read-index style protocol hoặc lease dưới timing assumptions đủ mạnh.

Nếu product chỉ cần stale/eventual read, có thể chọn path rẻ hơn. Consistency guarantee phải là design input, không phải label gắn sau implementation.

## 11. Reconfiguration là consensus trên chính membership

Thêm/bớt node không chỉ sửa config file. Membership quyết định quorum set, nên thay membership là thay safety boundary.

Protocol thường dùng joint/staged configuration để old và new sets overlap trong transition.

Failure mode nguy hiểm:

```text
old config A có quorum riêng
new config B có quorum riêng
A và B không overlap đủ
→ hai groups đều có thể nghĩ mình authoritative
```

Operational tooling phải coi membership change là state-machine operation có guardrail.

## 12. Snapshot và log compaction phải giữ điểm nối với history

Log tăng vô hạn là không thực tế. Replica có thể snapshot state tại một committed/applied index rồi bỏ prefix log cũ.

Snapshot phải gắn chính xác với index/term hoặc equivalent metadata để node biết suffix nào tiếp tục từ state đó.

Failure mode gồm snapshot quá cũ, partial snapshot install, state không đồng bộ với log suffix hoặc compaction xóa history còn cần cho lagging replica/recovery.

## 13. Lagging replica và backpressure

Replica chậm có thể giữ WAL/log retention lâu, chiếm disk và tăng leader memory/network pressure. Nếu leader chờ mọi replica, một node chậm có thể kéo latency toàn cluster; nếu chỉ chờ quorum, node đó có thể tụt xa rồi cần snapshot.

Đây là trade-off giữa foreground latency và recovery/catch-up cost.

Consensus layer vì thế cần retention policy, snapshot policy và monitoring cho lag distribution, không chỉ “quorum còn đủ”.

## 14. Performance pressure thay đổi behavior ở đâu?

Consensus write latency thường gồm:

```text
leader queue
+ local append/persistence
+ network RTT tới quorum
+ follower queue/persistence
+ commit propagation/apply
```

Khi cluster gần capacity, queueing có thể lớn hơn network RTT. Cross-region quorum làm tail nhạy với slowest required member. Large log entry tăng serialization/network/storage pressure.

Batching/group commit cải thiện throughput nhưng có thể thêm latency nhỏ để gom work. Invariant commit không được yếu đi chỉ vì batching.

## 15. Failure modes cần reasoning riêng

```text
leader churn do timeout/jitter
split-brain authority nếu membership/fencing sai
stale read từ old leader
replica apply lag
log growth vì lagging follower
snapshot install failure
ack quá sớm trước quorum/durability condition
external side effect từ stale leader thiếu fencing
```

Không nên gom mọi symptom thành “consensus unstable”. Mỗi failure vi phạm hoặc làm pressure một invariant khác.

## 16. Production evidence

Evidence tốt phải reconstruct protocol state:

```text
current term/epoch và leader identity
membership/config version
per-replica match/commit/applied positions
replication lag theo bytes/time
quorum health và election frequency
append/fsync latency
network RTT/loss giữa members
snapshot create/install state
rejected stale-term/fencing events
client retry/timeout rate
```

Log statement “became leader” đơn lẻ không đủ. Incident cần timeline election → quorum → commit positions → client acknowledgements.

## 17. Lower abstraction nào quyết định behavior?

Nếu commit p99 tăng, nguyên nhân có thể là storage flush hoặc network queue, không phải election logic. Nếu leader churn khi GC pause, runtime stop-the-world behavior có thể quyết định liveness. Nếu stale leader vẫn làm external write, resource fencing boundary mới là nơi correctness phải được enforce.

Consensus algorithm là abstraction trung tâm nhưng production behavior phụ thuộc OS/runtime/network/storage dưới nó.

## 18. Mô hình tư duy

> Consensus quản lý **một history có authority dưới partial failure**. Quorum intersection + voting/log rules giữ safety; term/epoch phân biệt authority qua thời gian; durability nối committed history với storage; reconfiguration giữ quorum overlap; snapshots nén history mà không được mất điểm nối; production evidence phải chỉ ra term, quorum và log positions chứ không chỉ node health.

## Kết nối

Đọc cùng [Failure detectors và membership](./01_failure_detectors_membership_and_gossip.md), [Leases/fencing](./02_leases_fencing_tokens_and_split_brain_prevention.md), [Time/causality](./06_time_clocks_ordering_and_causality.md), [Distributed transactions](../../05_data_databases/advanced/07_distributed_transactions_2pc_consensus_sagas_and_outbox.md) và [Durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).