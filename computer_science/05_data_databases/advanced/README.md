# Advanced Data & Databases

Roadmap sau [Database foundation](../../basic/05_data_databases/README.md):

1. [MVCC, visibility, WAL và recovery internals](./00_mvcc_visibility_wal_and_recovery_internals.md)
2. [Lock manager, predicate locking và serializable isolation](./01_lock_manager_predicate_locking_and_serializable_isolation.md)
3. [B+Tree page layout, splits/merges và latch coupling](./02_bplus_tree_pages_splits_merges_and_latch_coupling.md)
4. [LSM tree, compaction, Bloom filters và write amplification](./03_lsm_tree_compaction_bloom_filters_and_write_amplification.md)
5. [Buffer pool, replacement và dirty-page management](./04_buffer_pool_replacement_and_dirty_page_management.md)
6. [Cost-based optimizer, cardinality estimation và statistics](./05_cost_based_optimizer_cardinality_estimation_and_statistics.md)
7. Join algorithms, vectorized execution và late materialization
8. Distributed transactions: 2PC, consensus interaction, sagas/outbox
9. Replication, failover, read consistency và split-brain prevention
10. Columnar storage, compression và analytical query engines
11. Schema evolution, online migration và compatibility
12. Database observability: waits, locks, plans, I/O và saturation

Sáu chapter hiện có đã cover transaction/recovery, concurrency control, B+Tree/LSM storage structures, buffer management và query planning. Phần còn lại sẽ nối execution engine với distributed database và operations.