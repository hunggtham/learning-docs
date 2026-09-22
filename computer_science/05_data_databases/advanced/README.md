# Cơ sở dữ liệu nâng cao

Bắt đầu từ [nền tảng cơ sở dữ liệu](../../basic/05_data_databases/00_data_models_and_database_systems.md).

## Canonical chapters

1. [MVCC, khả năng quan sát phiên bản, WAL và cơ chế phục hồi](./00_mvcc_visibility_wal_and_recovery_internals.md)
2. [Bộ quản lý khóa, predicate locking và mức cô lập tuần tự hóa](./01_lock_manager_predicate_locking_and_serializable_isolation.md)
3. [Bố cục trang B+Tree, split/merge và latch coupling](./02_bplus_tree_pages_splits_merges_and_latch_coupling.md)
4. [LSM Tree, compaction, Bloom filter và khuếch đại ghi](./03_lsm_tree_compaction_bloom_filters_and_write_amplification.md)
5. [Buffer pool, chính sách thay thế và quản lý trang bẩn](./04_buffer_pool_replacement_and_dirty_page_management.md)
6. [Bộ tối ưu dựa trên chi phí, ước lượng cardinality và statistics](./05_cost_based_optimizer_cardinality_estimation_and_statistics.md)
7. [Thuật toán join, thực thi vector hóa và vật chất hóa muộn](./06_join_algorithms_vectorized_execution_and_late_materialization.md)
8. [Giao dịch phân tán: 2PC, consensus, saga và transactional outbox](./07_distributed_transactions_2pc_consensus_sagas_and_outbox.md)

Track đi từ transaction/recovery và concurrency control xuống storage engine, buffer management, optimizer/execution rồi lên distributed transaction. Mỗi chapter cần trả lời visibility/durability invariant, internal state machine, contention/I/O pressure, failure recovery và production evidence như plan/wait/lock/I/O/log position.

## Depth priorities

Replication/failover/read consistency nên đào sâu qua distributed transaction + consensus chapters và cross-link sang Networks & Distributed Systems. Analytical columnar execution nên được bổ sung nơi join/vectorized execution và storage layout thực sự quyết định behavior. Schema evolution thuộc Software Systems/Engineering nếu trọng tâm là compatibility/migration. Database observability phải nằm ngay trong các mechanism chapters thay vì tách thành catalog tool riêng.

Cross-layer path bắt buộc: [application transaction → WAL → filesystem → storage → replication](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).