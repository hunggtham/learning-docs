# Cơ sở dữ liệu nâng cao

Bắt đầu từ [nền tảng cơ sở dữ liệu](../../basic/05_data_databases/00_data_models_and_database_systems.md).

## Chuẩn gốc (canonical / 정본) chapters

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

Nhánh học (track / 트랙) đi từ giao dịch (transaction / 트랜잭션)/khôi phục (recovery / 복구) và tính đồng thời (concurrency / 동시성) điều khiển (control / 제어) xuống lưu trữ (storage / 저장소) engine, buffer management, optimizer/thực thi (execution / 실행) rồi lên phân tán (distributed / 분산) giao dịch (transaction / 트랜잭션) và analytical lưu trữ (storage / 저장소)/thực thi (execution / 실행). Mỗi chapter cần trả lời visibility/durability bất biến (invariant / 불변식), trạng thái nội bộ (internal state / 내부 상태) machine, contention/I/O pressure, thất bại (failure / 실패) khôi phục (recovery / 복구) và bằng chứng vận hành (production evidence / 운영 증거) như plan/wait/khóa (lock / 잠금)/I/O/log position.

Replication/failover/read consistency vẫn thuộc Phân tán (distributed / 분산) Các hệ thống (systems / 시스템들) khi trọng tâm là authority/quorum/failover. Columnar lưu trữ (storage / 저장소) có chuẩn gốc (canonical / 정본) chapter riêng vì vật lý (physical / 물리적) bố cục (layout / 레이아웃), compression/encoding, row-group pruning, projection/predicate pushdown, late materialization và spill tạo mô hình tư duy (mental model / 사고 모델) độc lập với OLTP B+Cây (tree / 트리)/LSM.

Adaptive truy vấn (query / 쿼리) thực thi (execution / 실행) bổ sung tầng (layer / 계층) còn thiếu giữa compile-time optimizer và thời gian chạy (runtime / 런타임) reality. Statistics chỉ là mô hình (model / 모델); cardinality, skew, bộ nhớ (memory / 메모리) pressure và partition kích thước (size / 크기) thật chỉ xuất hiện khi truy vấn (query / 쿼리) chạy. Re-optimization chỉ an toàn tại ranh giới (boundary / 경계) mà engine có thể đổi vật lý (physical / 물리적) chiến lược (strategy / 전략) nhưng vẫn giữ logical truy vấn (query / 쿼리) ngữ nghĩa (semantics / 의미론). Thời gian chạy (runtime / 런타임) filters phải được lập luận (reasoning / 추론) theo bất biến (invariant / 불변식) không loại bỏ row hợp lệ; skew handling phải phân biệt tải (load / 로드) redistribution với việc chỉ di chuyển bottleneck sang mạng (network / 네트워크)/bộ nhớ (memory / 메모리).

Cơ sở dữ liệu (database / 데이터베이스) khả năng quan sát (observability / 관측 가능성) phải nằm ngay trong cơ chế (mechanism / 메커니즘) chapters thay vì tách thành danh mục (catalog / 카탈로그) công cụ (tool / 도구). Thực thi (execution / 실행) plan chỉ là hypothesis ban đầu; actual row counts, spill bytes, partition phân phối (distribution / 분포), runtime-filter selectivity, bộ nhớ (memory / 메모리) grant/usage và stage timing mới giúp kiểm tra optimizer giả định (assumption / 가정).

Cross-layer đường dẫn (path / 경로) bắt buộc: [application transaction → WAL → filesystem → storage → replication](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md). Analytical đường dẫn (path / 경로) nên đọc `05 → 06 → 08 → 09` để đi từ estimate → operator → vật lý (physical / 물리적) bố cục (layout / 레이아웃) → thời gian chạy (runtime / 런타임) adaptation.