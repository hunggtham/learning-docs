# NoSQL, distributed và analytical databases

Relational database không phải lựa chọn duy nhất vì workloads khác nhau đặt pressure khác nhau lên data model, scale, latency, consistency và query patterns. “NoSQL” không phải một architecture duy nhất mà là umbrella term cho nhiều systems đánh đổi relational generality để tối ưu một số access pattern hoặc distribution model.

Ở mức systems reasoning, database architecture xoay quanh ba câu hỏi:

```text
state được partition ở đâu?
state được replicate theo authority/order nào?
physical layout nào phù hợp query/update pattern?
```

Các lựa chọn này tạo invariant, failure mode và production evidence khác nhau.

## 1. Chọn data model từ access pattern và invariant

Document database lưu aggregate-like documents; key-value store tối ưu lookup theo key; wide-column store tổ chức sparse rows theo partition/clustering keys; graph database tối ưu traversal qua relationships.

Không model nào “schema-less” theo nghĩa không có structure. Schema vẫn tồn tại trong application, validation rule, serialization format hoặc implicit convention. Chỉ là nơi enforcement và evolution khác relational schema.

Câu hỏi tốt hơn “SQL hay NoSQL?” là:

```text
operation nào là critical path?
invariant nào phải atomic?
query nào cần locality?
state có thể partition theo key nào?
reader chấp nhận stale tới mức nào?
```

## 2. Denormalization là intentional replication ở logical layer

Distributed/document systems thường duplicate data để tránh joins xuyên partitions. Điều này giảm read latency nhưng tạo consistency problem: khi source fact đổi, các copies phải được cập nhật.

Normalization giảm update anomalies bằng cách giảm duplication; denormalization chấp nhận duplication để tối ưu access path.

Invariant phải nói rõ copy nào là source of truth, propagation có synchronous hay asynchronous, stale window chấp nhận bao lâu và conflict/rebuild xử lý thế nào.

## 3. Partitioning và shard key quyết định locality lẫn failure surface

Distributed database chia data thành partitions/shards. Shard key quyết định placement và query locality.

Hash partitioning thường phân bố đều hơn nhưng range query khó hơn. Range partitioning giúp scan theo khoảng nhưng dễ skew. Monotonic timestamp có thể dồn writes vào một partition; tenant ID có thể tạo celebrity tenant hotspot.

Một shard key tốt cần cân:

```text
load distribution
query locality
transaction locality
rebalancing cost
hot-key behavior
future growth
```

Không có shard key “đúng” nếu chưa biết workload distribution.

## 4. Replication cần một authority model

Replication tạo nhiều physical copies nhưng correctness cần trả lời: **copy nào có quyền quyết định write order?**

Leader/follower model thường serialize writes qua leader rồi gửi log/changes tới followers. Multi-leader cho phép writes tại nhiều sites nhưng phải giải conflict/order. Leaderless/quorum model dùng read/write quorum và version/conflict semantics khác.

“Số replicas = 3” chưa cho biết consistency. Phải biết commit/ack rule và failover authority.

## 5. Local append, replicated và committed là các trạng thái khác nhau

Một write có thể đi qua:

```text
received by leader
→ appended to local memory/log
→ durable locally
→ sent to followers
→ durable on followers
→ quorum condition satisfied
→ committed/visible theo protocol
→ applied to materialized state
```

Không phải hệ thống nào cũng expose cùng stages, nhưng mental model này giúp hỏi đúng: acknowledgement được gửi ở stage nào?

Nếu client nhận success trước durable quorum, failover có thể mất acknowledged write tùy contract. Nếu phải chờ remote durable quorum, latency path chứa network + remote storage.

## 6. Replication lag là state distance, không chỉ “milliseconds”

Follower có thể chậm theo log position/LSN/index dù wall-clock lag khó đo chính xác. “Replica lag 2 giây” là shorthand; quantity đáng tin hơn thường là khoảng cách applied/received position so với leader theo protocol.

Lag tăng vì network, storage, apply CPU, lock/contention, large transaction hoặc maintenance.

Production evidence nên đo:

```text
leader commit position
follower receive/durable/apply position
apply throughput
network/storage latency
replay/apply errors
```

## 7. Read consistency là observable contract

“Strong” và “eventual” là quá thô nếu không nói reader quan sát gì.

Các property thực dụng gồm:

```text
read-your-writes
monotonic reads
monotonic writes
consistent prefix
causal consistency
linearizable read
bounded staleness
```

Ví dụ sau khi user đổi profile trên leader rồi request tiếp bị route sang lagging follower, họ có thể không thấy update của chính mình. Fix có thể là session stickiness, read from leader, wait-until replica reaches token/LSN, hoặc stronger read protocol.

Chọn strategy theo invariant, không theo nhãn marketing.

## 8. Replica read không miễn phí về correctness

Read replicas tăng read capacity và tách analytical/report workload khỏi leader, nhưng stale read có thể phá check-then-act logic.

Ví dụ:

```text
writer: mark coupon used
reader trên stale replica: coupon still unused
application: cho phép dùng lại
```

Nếu invariant yêu cầu unique redemption, validation phải chạy tại authority/transaction boundary có consistency đủ mạnh. Cache/replica read có thể dùng cho display nhưng không nhất thiết dùng cho authorization/business decision.

## 9. Failover là authority transfer, không chỉ đổi DNS

Khi leader fail, hệ thống cần chọn node mới và ngăn old leader tiếp tục accept authoritative writes nếu nó quay lại trong trạng thái partitioned.

Mechanism thường cần epoch/term/fencing/quorum. Invariant:

> Tại một thời điểm theo protocol, không được có hai authorities độc lập cùng commit histories không thể reconcile nếu contract yêu cầu single history.

Đây là split-brain problem. Health check một mình không đủ vì “không reach được leader” không chứng minh leader đã chết; có thể chỉ là partition.

## 10. RPO và RTO làm failover contract cụ thể hơn

**Recovery Point Objective (RPO)** trả lời có thể mất bao nhiêu committed/accepted data theo disaster model. **Recovery Time Objective (RTO)** trả lời mất bao lâu để khôi phục service.

Async replication thường cho latency tốt nhưng RPO có thể > 0 khi leader mất trước khi follower catch up. Sync/quorum replication có thể giảm RPO nhưng tăng foreground latency và giảm write availability trong một số partition/failure scenario.

Failover design là trade-off consistency/durability/availability/time, không chỉ “có replica”.

## 11. Read-after-failover cần hiểu commit horizon

Replica được promote có thể có log prefix khác trạng thái mà một số clients vừa quan sát nếu acknowledgement contract yếu hoặc failover chọn node chưa đủ current.

Sau failover, application có thể thấy data “đi lùi”. Đây là violation của monotonic/user-observed history nếu product assumption mạnh hơn database guarantee.

Evidence cần biết:

```text
write acknowledged ở commit position nào?
new leader có position nào?
node nào tham gia quorum?
old leader có bị fenced không?
read routing sau failover đi đâu?
```

## 12. Quorum không có nghĩa mọi quorum design đều linearizable

Nếu N replicas, write quorum `W`, read quorum `R` và `R + W > N` cho intersection intuition, nhưng correctness còn phụ thuộc versioning, failure handling, sloppy quorum, clock assumptions và read-repair protocol.

Intersection là một building block, không phải proof hoàn chỉnh.

Distributed database contract phải được đọc theo concrete protocol, không học thuộc công thức quorum rồi suy ra quá mức.

## 13. LSM tree phù hợp write-heavy nhưng chuyển cost sang compaction/read path

Log-Structured Merge Tree buffer writes trong memory rồi flush immutable sorted tables; background compaction merge levels.

Write path biến nhiều random writes thành sequential writes, nhưng reads có thể cần check nhiều tables nếu Bloom filter/index không loại được. Compaction tạo write amplification và background I/O.

Failure/performance pressure:

```text
write burst
→ memtable flush tăng
→ compaction debt tăng
→ storage bandwidth bị background work chiếm
→ read/write tail latency tăng
```

LSM là ví dụ điển hình của defer + batch + merge: cost bị dời, không bị xóa.

## 14. OLTP và OLAP có physical constraints khác nhau

OLTP phục vụ nhiều point read/write, concurrency cao, low latency và transaction invariants. OLAP scan/aggregate lượng lớn data, thường đọc ít columns trên nhiều rows.

Vì workload khác, physical layout cũng khác. Row store tối ưu locality của một record; column store tối ưu locality của một attribute qua nhiều rows.

“Column database nhanh hơn” chỉ đúng cho query shape phù hợp.

## 15. Columnar storage bắt đầu từ projection pushdown

Nếu table có 100 columns nhưng query chỉ cần 4, row store phải đọc bytes của nhiều fields không dùng tùy layout/cache. Columnar layout cho phép đọc các column chunks cần thiết.

```text
SELECT region, SUM(amount)
FROM sales
GROUP BY region
```

Engine có thể đọc chủ yếu `region` và `amount`, giảm I/O và memory bandwidth.

Đây là performance invariant: **bytes processed nên gần bytes relevant hơn là full logical row width**.

## 16. Compression hiệu quả vì values cùng column có distribution giống nhau

Values cùng column thường có type/distribution lặp lại nên encode tốt: dictionary encoding, run-length encoding, delta encoding, bit packing và compression codecs.

Compression không chỉ giảm storage; nó có thể giảm I/O/memory bandwidth đủ nhiều để CPU decompression vẫn có lợi.

Nhưng high-cardinality/random data compress kém hơn. Encoding choice phụ thuộc distribution.

## 17. Zone map / min-max metadata giúp skip data

Columnar segments/row groups có thể giữ metadata như min/max/null count. Query predicate có thể bỏ qua entire chunk nếu range không thể match.

```text
segment amount: min=0, max=100
predicate amount > 1000
→ skip segment
```

Đây là data-skipping index nhẹ. Nếu clustering/order của data phù hợp predicate, skip ratio cao; nếu values random khắp mọi segment, metadata ít hữu ích.

Physical ordering vì vậy ảnh hưởng analytical scan cost.

## 18. Vectorized execution amortize interpreter/function-call overhead

Thay vì xử lý một row mỗi operator call, analytical engine có thể xử lý batches/vectors. Điều này tăng locality, giảm virtual/function-call overhead và tạo cơ hội SIMD.

Pipeline có thể:

```text
scan vector
→ filter vector
→ project/decode needed columns
→ aggregate in batches
```

Nhưng batch quá lớn tăng cache footprint; variable-length data và branchy expressions có thể giảm SIMD efficiency.

Đọc thêm [join algorithms, vectorized execution và late materialization](../../05_data_databases/advanced/06_join_algorithms_vectorized_execution_and_late_materialization.md).

## 19. Late materialization tránh dựng full row quá sớm

Columnar engine thường giữ column vectors/row identifiers qua filter/join rồi chỉ reconstruct output rows khi cần. Đây là **late materialization**.

Lợi ích: tránh copy/decode columns bị filter bỏ. Trade-off: position mapping và gather có thể phức tạp, random access có thể đắt nếu pipeline mất locality.

Optimization phải reasoning cùng query selectivity và data layout.

## 20. Analytical query vẫn có concurrency và spill failure modes

Hash join/group-by cần memory. Nếu cardinality estimate thấp hơn thực tế, operator có thể vượt budget và spill ra disk. Nhiều concurrent analytical queries có thể cùng consume memory/bandwidth rồi làm whole-node throughput giảm.

Evidence cần tách:

```text
bytes scanned
segments skipped
compression ratio
rows/vectors processed
operator memory
spill bytes/time
CPU utilization + memory bandwidth
storage throughput
```

Query “chậm” không nhất thiết vì SQL logic; có thể vì data skipping thất bại hoặc memory spill.

## 21. Warehouse, lake và lakehouse là storage/metadata trade-offs

Warehouse thường quản lý curated analytical data với engine/storage integration chặt. Data lake ưu tiên object storage rẻ/open formats. Lakehouse thêm table metadata, transaction/version semantics và query optimizations trên object storage.

Các terms này là architecture families, không phải scientific categories cứng. Điều quan trọng là invariant:

```text
snapshot nào reader thấy?
concurrent writer commit thế nào?
schema evolution ra sao?
metadata/catalog có authority ở đâu?
object files orphan/compact thế nào?
```

## 22. Materialized view là precomputation với freshness contract

Nếu query đắt nhưng source update ít hơn, materialized view đổi storage/update work lấy query latency.

Câu hỏi cần trả lời:

```text
refresh synchronous hay async?
stale window bao lâu?
refresh failure làm view dừng ở version nào?
reader biết freshness không?
```

Materialization là caching ở database scale; consistency semantics vẫn phải explicit.

## 23. Production evidence cho distributed database

Khi điều tra replication/failover/read anomaly, cần nối:

```text
client request + consistency mode
leader/epoch/term
commit/log position
replica receive/durable/apply position
replication lag/backlog
read routing target
failover/promotion timeline
network/storage errors
```

Nếu chỉ có “replica healthy=true”, không đủ để chứng minh read freshness hoặc failover correctness.

## 24. Production evidence cho analytical engine

Khi query scan/aggregate chậm, cần:

```text
actual execution plan
cardinality estimate vs actual
bytes/segments scanned
pruning/data-skipping effectiveness
compression/decode cost
operator memory and spill
CPU/vectorization efficiency
memory/storage bandwidth
```

Tối ưu chỉ index/schema theo intuition mà không nhìn physical execution dễ sửa sai layer.

## 25. Failure matrix cho replication

Một replication design nên giải thích được ít nhất:

```text
leader process crash
leader host/storage loss
network partition leader↔majority
slow follower
follower storage corruption
old leader returns after failover
cross-region latency spike
control-plane membership change
```

Với mỗi case, hỏi: ai còn authority, write có được accept không, acknowledged write nào survive, read có stale không, recovery evidence nằm đâu?

## 26. Mô hình tư duy

> Database architecture là interaction giữa **data model, partition locality, replication authority, consistency contract và physical storage/execution layout**. Replication không chỉ là nhiều copies; nó là protocol quyết định write nào có authority sau failure. Columnar storage không chỉ là “lưu theo cột”; nó là cách giảm bytes processed và tận dụng compression/vectorized execution cho analytical workload. Cả hai phải được đánh giá bằng observable contract và production evidence.

## Những hiểu nhầm thường gặp

**“NoSQL tốt hơn SQL khi dữ liệu lớn.”** Scale phụ thuộc partitioning, workload, consistency và operations; relational systems cũng có distributed implementations.

**“Replica read luôn an toàn nếu chỉ đọc.”** Stale read vẫn có thể phá business decision nếu reader dùng nó để authorize/check invariant.

**“Failover chỉ là promote node khác.”** Promotion là authority transfer; fencing và commit horizon quyết định correctness.

**“Quorum intersection tự động nghĩa linearizable.”** Không; protocol/version/read semantics vẫn quyết định guarantee.

**“Column store luôn nhanh hơn row store.”** Chỉ khi workload tận dụng column projection, compression, skipping và scan/vectorization.

## Kết nối

Xem [transactions](./02_transactions_acid_and_concurrency_control.md), [storage/WAL](./04_storage_logs_recovery_and_durability.md), [distributed consistency](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md), [replication/consensus](../06_networks_distributed_systems/05_replication_partitioning_and_consensus.md), [Consensus advanced](../../06_networks_distributed_systems/advanced/03_consensus_log_replication_reconfiguration_and_snapshots.md), [Distributed transactions](../../05_data_databases/advanced/07_distributed_transactions_2pc_consensus_sagas_and_outbox.md) và [Durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).