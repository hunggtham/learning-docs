# NoSQL, distributed và analytical databases

Relational database không phải lựa chọn duy nhất vì workloads khác nhau đặt pressure khác nhau lên data model, scale, latency, consistency và query patterns. “NoSQL” không phải một architecture duy nhất mà là umbrella term cho nhiều systems đánh đổi relational generality để tối ưu một số access patterns hoặc distribution models.

## Chọn data model từ access pattern và invariants

Document database lưu aggregate-like JSON/BSON documents; key-value store tối ưu lookup theo key; wide-column store tổ chức sparse rows theo partition/clustering keys; graph database tối ưu traversal qua relationships.

Không model nào “schema-less” theo nghĩa không có structure. Schema vẫn tồn tại trong application, validation rules hoặc implicit conventions. Chỉ là nơi enforcement và evolution khác relational schema.

## Denormalization như intentional duplication

Distributed/document systems thường duplicate data để tránh joins xuyên partitions. Điều này giảm read latency nhưng tạo consistency problem: khi source fact đổi, các copies phải được cập nhật.

Normalization giảm update anomalies bằng cách giảm duplication; denormalization chấp nhận duplication để tối ưu access path. Đây là trade-off, không phải ideology.

## Partitioning và shard key

Distributed database chia data thành partitions/shards. Shard key quyết định placement và query locality.

Bad shard key có thể tạo hotspot: ví dụ timestamp tăng dần dồn writes vào một partition. Hash partitioning phân bố tốt nhưng làm range query khó hơn. Range partitioning hỗ trợ range scan nhưng dễ skew.

Schema design trong distributed DB vì vậy phải xem workload topology.

## Replication và consistency

Replicas tăng availability/read capacity nhưng tạo vấn đề version/order. Strongly consistent systems có thể dùng consensus/quorum rules để serialize updates; eventually consistent systems chấp nhận temporary divergence và dùng conflict resolution.

Consistency model phải được mô tả bằng observable behavior, không chỉ nhãn “strong/eventual”. Cần hỏi read-after-write? monotonic reads? causal order? stale bao lâu?

## LSM tree và write-heavy workloads

Log-Structured Merge Tree buffer writes trong memory rồi flush immutable sorted tables, sau đó compaction merge levels.

Write path biến nhiều random writes thành sequential writes, nhưng reads có thể cần check nhiều levels/tables nếu bloom filter/index không đủ. Compaction tạo write amplification và background I/O.

LSM là ví dụ điển hình của **defer + batch + merge** trade-off.

## OLTP và OLAP

Online Transaction Processing (OLTP / 온라인 트랜잭션 처리) phục vụ nhiều small reads/writes, concurrency cao, low latency và transactional invariants.

Online Analytical Processing (OLAP / 온라인 분석 처리) scan/aggregate lượng dữ liệu lớn để phân tích. Columnar storage hiệu quả vì query thường chỉ cần vài columns và values cùng column compress tốt.

Workload shape khác khiến storage layout khác.

## Row store và column store

Row store đặt fields của một record gần nhau, tốt cho point lookup/update cả row. Column store đặt values cùng column gần nhau, tốt cho scan/aggregate và compression.

Không phải “column database nhanh hơn”; nó nhanh cho workload phù hợp và có trade-offs cho point mutation.

## Data warehouse, lake và lakehouse

Data warehouse quản lý curated analytical data với schema/query engine chặt. Data lake lưu raw/semi-structured data trên object storage. Lakehouse cố kết hợp cheap open storage với table metadata, transaction và query semantics gần warehouse.

Các terms này là architecture patterns hơn là strict scientific categories; vendors dùng terminology khác nhau.

## Materialized view và precomputation

Nếu analytical query đắt nhưng data update ít hơn, có thể precompute aggregates/materialized views. Đây là same time-space trade-off như caching và dynamic programming: dùng storage/update work để giảm query latency.

## Common Misconceptions

**“NoSQL tốt hơn SQL khi dữ liệu lớn.”** Scale phụ thuộc architecture, partitioning, workload và operations; relational systems cũng có distributed implementations.

**“Schema-less nghĩa là khỏi migration.”** Structure vẫn đổi; chỉ chuyển burden sang application/read-time compatibility.

**“Eventual consistency nghĩa là random.”** Nó có formal guarantees tùy system; cần đọc consistency contract cụ thể.

## Mental Model

> Database architecture là kết quả của ba câu hỏi: data được partition/replicate thế nào, query path cần locality nào, và invariants nào phải giữ mạnh tới mức nào.

## Kết nối

Xem [transactions](./02_transactions_acid_and_concurrency_control.md), [storage/WAL/LSM](./04_storage_logs_recovery_and_durability.md), [distributed consistency](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md) và [replication/consensus](../06_networks_distributed_systems/05_replication_partitioning_and_consensus.md).