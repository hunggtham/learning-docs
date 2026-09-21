# Cơ sở dữ liệu nâng cao

Lộ trình sau [nền tảng cơ sở dữ liệu](../../basic/05_data_databases/README.md):

1. [MVCC, khả năng quan sát phiên bản, WAL và cơ chế phục hồi](./00_mvcc_visibility_wal_and_recovery_internals.md)
2. [Bộ quản lý khóa, predicate locking và mức cô lập tuần tự hóa](./01_lock_manager_predicate_locking_and_serializable_isolation.md)
3. [Bố cục trang B+Tree, split/merge và latch coupling](./02_bplus_tree_pages_splits_merges_and_latch_coupling.md)
4. [LSM Tree, compaction, Bloom filter và khuếch đại ghi](./03_lsm_tree_compaction_bloom_filters_and_write_amplification.md)
5. [Buffer pool, chính sách thay thế và quản lý trang bẩn](./04_buffer_pool_replacement_and_dirty_page_management.md)
6. [Bộ tối ưu dựa trên chi phí, ước lượng cardinality và statistics](./05_cost_based_optimizer_cardinality_estimation_and_statistics.md)
7. [Thuật toán join, thực thi vector hóa và vật chất hóa muộn](./06_join_algorithms_vectorized_execution_and_late_materialization.md)
8. [Giao dịch phân tán: 2PC, consensus, saga và transactional outbox](./07_distributed_transactions_2pc_consensus_sagas_and_outbox.md)
9. Replication, failover, read consistency và phòng tránh split-brain
10. Lưu trữ dạng cột, compression và analytical query engine
11. Tiến hóa schema, online migration và compatibility
12. Khả năng quan sát database: wait, lock, plan, I/O và saturation

Tám chapter hiện có nối đường đi từ transaction/recovery và concurrency control xuống storage engine, buffer management, optimizer, execution engine rồi lên distributed transaction. Các chapter tiếp theo sẽ đào sâu replication, analytical storage, schema evolution và production observability.