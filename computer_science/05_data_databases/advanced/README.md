# Cơ sở dữ liệu nâng cao

> **Mạch đọc:** Đọc **Cơ sở dữ liệu nâng cao** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Hãy xác định đối tượng và câu hỏi trung tâm trước, rồi dùng phần này để đối chiếu với mục liên quan sau khi đã nắm mô hình tư duy (mental model / 사고 모델) chính.


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

Nhánh học (track / 트랙) đi từ giao dịch (transaction / 트랜잭션)/khôi phục (recovery / 복구) và tính đồng thời (concurrency / 동시성) điều khiển (control / 제어) xuống lưu trữ (storage / 저장소) engine, buffer management, optimizer/thực thi (execution / 실행) rồi lên phân tán (distributed / 분산) giao dịch (transaction / 트랜잭션) và analytical lưu trữ (storage / 저장소). Mỗi chapter cần trả lời visibility/durability bất biến (invariant / 불변식), trạng thái nội bộ (internal state / 내부 상태) machine, contention/I/O pressure, thất bại (failure / 실패) khôi phục (recovery / 복구) và bằng chứng vận hành (production evidence / 운영 증거) như plan/wait/khóa (lock / 잠금)/I/O/log position.

Replication/failover/read consistency vẫn thuộc phân tán (distributed / 분산) các hệ thống (systems / 시스템들) khi trọng tâm là authority/quorum/failover. Columnar lưu trữ (storage / 저장소) giờ có chuẩn gốc (canonical / 정본) chapter riêng vì vật lý (physical / 물리적) bố cục (layout / 레이아웃), compression/encoding, row-group pruning, projection/predicate pushdown, late materialization và spill tạo một mô hình tư duy (mental model / 사고 모델) độc lập với OLTP B+cây (tree / 트리)/LSM. Adaptive truy vấn (query / 쿼리) thực thi (execution / 실행) giờ có đơn vị sở hữu (owner / 오너) riêng cho thời gian chạy (runtime / 런타임) phản hồi (feedback / 피드백), động (dynamic / 동적) filtering, skew mitigation, re-optimization và plan-state transitions; thực thi (execution / 실행) sâu tiếp tục nối với chuẩn gốc (canonical / 정본) phép nối (join / 조인)/vectorized chapter thay vì duplicate operator internals.

Khi mở rộng tiếp, chỉ tạo tệp (file / 파일) mới nếu lưu trữ (storage / 저장소)/truy vấn (query / 쿼리) topic thực sự có bất biến (invariant / 불변식) và cơ chế (mechanism / 메커니즘) riêng không còn phù hợp với các tệp chuẩn gốc (canonical file / 정본 파일) hiện tại. lược đồ (schema / 스키마) evolution vẫn thuộc Software các hệ thống (systems / 시스템들)/kỹ thuật (engineering / 엔지니어링) khi trọng tâm là tính tương thích (compatibility / 호환성)/di chuyển (migration / 마이그레이션). cơ sở dữ liệu (database / 데이터베이스) khả năng quan sát (observability / 관측 가능성) phải nằm ngay trong cơ chế (mechanism / 메커니즘) chapters thay vì tách thành danh mục (catalog / 카탈로그) công cụ (tool / 도구) riêng.

Cross-layer đường dẫn (path / 경로) bắt buộc: [application transaction → WAL → filesystem → storage → replication](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

> **Bàn giao:** Sau **chuẩn gốc (canonical / 정본) chapters**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 mvcc visibility wal and recovery internals](./00_mvcc_visibility_wal_and_recovery_internals.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
