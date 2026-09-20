# Advanced Data & Databases

Roadmap sau [Database foundation](../../basic/05_data_databases/README.md):

1. [MVCC, visibility, WAL và recovery internals](./00_mvcc_visibility_wal_and_recovery_internals.md)
2. [Lock manager, predicate locking và serializable isolation](./01_lock_manager_predicate_locking_and_serializable_isolation.md)
3. [B+Tree page layout, splits/merges và latch coupling](./02_bplus_tree_pages_splits_merges_and_latch_coupling.md)
4. LSM tree, compaction, bloom filters và write amplification
5. Buffer pool, replacement và dirty-page management
6. Cost-based optimizer, cardinality estimation và statistics
7. Join algorithms, vectorized execution và late materialization
8. Distributed transactions: 2PC, consensus interaction, sagas/outbox
9. Replication, failover, read consistency và split-brain prevention
10. Columnar storage, compression và analytical query engines
11. Schema evolution, online migration và compatibility
12. Database observability: waits, locks, plans, I/O và saturation

Các chapter hiện có đi từ transaction/recovery → concurrency control → physical index structure, tạo nền để tiếp tục storage engines, optimizer và distributed database.