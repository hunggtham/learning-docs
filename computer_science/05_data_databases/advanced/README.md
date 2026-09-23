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
9. [Columnar storage, encoding, pruning và vectorized scans](./08_columnar_storage_encoding_pruning_and_vectorized_scans.md)
10. [Adaptive query execution, runtime filters, skew và re-optimization](./09_adaptive_query_execution_runtime_filters_skew_and_reoptimization.md)

Track đi từ transaction/recovery và concurrency control xuống storage engine, buffer management, optimizer/execution rồi lên distributed transaction và analytical storage. Mỗi chapter cần trả lời visibility/durability invariant, internal state machine, contention/I/O pressure, failure recovery và production evidence như plan/wait/lock/I/O/log position.

Replication/failover/read consistency vẫn thuộc Distributed Systems khi trọng tâm là authority/quorum/failover. Columnar storage giờ có canonical chapter riêng vì physical layout, compression/encoding, row-group pruning, projection/predicate pushdown, late materialization và spill tạo một mental model độc lập với OLTP B+Tree/LSM. Adaptive query execution giờ có owner riêng cho runtime feedback, dynamic filtering, skew mitigation, re-optimization và plan-state transitions; execution sâu tiếp tục nối với canonical join/vectorized chapter thay vì duplicate operator internals.

Khi mở rộng tiếp, chỉ tạo file mới nếu storage/query topic thực sự có invariant và mechanism riêng không còn phù hợp với các canonical file hiện tại. Schema evolution vẫn thuộc Software Systems/Engineering khi trọng tâm là compatibility/migration. Database observability phải nằm ngay trong mechanism chapters thay vì tách thành catalog tool riêng.

Cross-layer path bắt buộc: [application transaction → WAL → filesystem → storage → replication](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).
