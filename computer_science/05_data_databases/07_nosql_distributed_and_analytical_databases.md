# NoSQL, phân tán (distributed / 분산) và analytical databases

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **NoSQL, phân tán (distributed / 분산) và analytical databases**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Chọn mô hình dữ liệu (data model / 데이터 모델) từ truy cập (access / 접근) mẫu (pattern / 패턴) và invariants** xác định điều kiện hoặc ranh giới mà các cơ chế sau phải tôn trọng; sau đó sang **Denormalization như intentional duplication** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Relational cơ sở dữ liệu (database / 데이터베이스) không phải lựa chọn duy nhất vì workloads khác nhau đặt pressure khác nhau lên mô hình dữ liệu (data model / 데이터 모델), quy mô (scale / 규모), độ trễ (latency / 지연 시간), consistency và truy vấn (query / 쿼리) patterns. “NoSQL” không phải một kiến trúc (architecture / 아키텍처) duy nhất mà là umbrella term cho nhiều các hệ thống (systems / 시스템들) đánh đổi relational generality để tối ưu một số truy cập (access / 접근) patterns hoặc phân phối (distribution / 분포) các mô hình (models / 모델들).

## Chọn mô hình dữ liệu (data model / 데이터 모델) từ truy cập (access / 접근) mẫu (pattern / 패턴) và invariants

Document cơ sở dữ liệu (database / 데이터베이스) lưu aggregate-like JSON/BSON documents; key-value store tối ưu lookup theo key; wide-column store tổ chức sparse rows theo partition/clustering keys; đồ thị (graph / 그래프) cơ sở dữ liệu (database / 데이터베이스) tối ưu traversal qua relationships.

Không mô hình (model / 모델) nào “schema-less” theo nghĩa không có cấu trúc (structure / 구조). lược đồ (schema / 스키마) vẫn tồn tại trong ứng dụng (application / 애플리케이션), kiểm tra hợp lệ (validation / 검증) rules hoặc implicit conventions. Chỉ là nơi enforcement và evolution khác relational lược đồ (schema / 스키마).

> **Chuyển mạch:** Trong **NoSQL, phân tán (distributed / 분산) và analytical databases**, **Chọn mô hình dữ liệu (data model / 데이터 모델) từ truy cập (access / 접근) mẫu (pattern / 패턴) và invariants** nêu điều cần giải thích; **Denormalization như intentional duplication** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Partitioning và shard key** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Denormalization như intentional duplication

Phân tán (distributed / 분산)/document các hệ thống (systems / 시스템들) thường duplicate dữ liệu (data / 데이터) để tránh joins xuyên partitions. Điều này giảm read độ trễ (latency / 지연 시간) nhưng tạo consistency bài toán (problem / 문제): khi nguồn (source / 소스) fact đổi, các copies phải được cập nhật.

Normalization giảm cập nhật (update / 업데이트) anomalies bằng cách giảm duplication; denormalization chấp nhận duplication để tối ưu truy cập (access / 접근) đường dẫn (path / 경로). Đây là sự đánh đổi (trade-off / 트레이드오프), không phải ideology.

> **Chuyển mạch:** Ở chặng này của **NoSQL, phân tán (distributed / 분산) và analytical databases**, **Partitioning và shard key** tiếp nhận điểm tựa từ **Denormalization như intentional duplication** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Replication và consistency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Partitioning và shard key

Phân tán (distributed / 분산) cơ sở dữ liệu (database / 데이터베이스) chia dữ liệu (data / 데이터) thành partitions/shards. Shard key quyết định placement và truy vấn (query / 쿼리) locality.

Bad shard key có thể tạo hotspot: ví dụ timestamp tăng dần dồn writes vào một partition. băm (hash / 해시) partitioning phân bố tốt nhưng làm phạm vi (range / 범위) truy vấn (query / 쿼리) khó hơn. phạm vi (range / 범위) partitioning hỗ trợ phạm vi (range / 범위) scan nhưng dễ skew.

Lược đồ (schema / 스키마) thiết kế (design / 설계) trong phân tán (distributed / 분산) DB vì vậy phải xem tải công việc (workload / 워크로드) topology.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **NoSQL, phân tán (distributed / 분산) và analytical databases**, **Replication và consistency** tiếp nhận điểm tựa từ **Partitioning và shard key** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LSM cây (tree / 트리) và write-heavy workloads** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Replication và consistency

Replicas tăng availability/read sức chứa (capacity / 용량) nhưng tạo vấn đề phiên bản (version / 버전)/thứ tự (order / 순서). Strongly consistent các hệ thống (systems / 시스템들) có thể dùng consensus/quorum rules để serialize updates; eventually consistent các hệ thống (systems / 시스템들) chấp nhận temporary divergence và dùng giải quyết xung đột (conflict resolution / 충돌 해결).

Consistency mô hình (model / 모델) phải được mô tả bằng observable hành vi (behavior / 동작), không chỉ nhãn “strong/eventual”. Cần hỏi read-after-write? monotonic reads? nhân quả (causal / 인과적) thứ tự (order / 순서)? stale bao lâu?

> **Chuyển mạch:** Trong **NoSQL, phân tán (distributed / 분산) và analytical databases**, **LSM cây (tree / 트리) và write-heavy workloads** tiếp nhận điểm tựa từ **Replication và consistency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **OLTP và OLAP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LSM cây (tree / 트리) và write-heavy workloads

Log-Structured Merge cây (tree / 트리) buffer writes trong bộ nhớ (memory / 메모리) rồi flush immutable sorted tables, sau đó compaction merge levels.

Ghi (write / 쓰기) đường dẫn (path / 경로) biến nhiều random writes thành sequential writes, nhưng reads có thể cần check nhiều levels/tables nếu bloom filter/chỉ mục (index / 인덱스) không đủ. Compaction tạo ghi (write / 쓰기) amplification và background I/O.

LSM là ví dụ điển hình của **defer + batch + merge** sự đánh đổi (trade-off / 트레이드오프).

> **Chuyển mạch:** Ở chặng này của **NoSQL, phân tán (distributed / 분산) và analytical databases**, **OLTP và OLAP** tiếp nhận điểm tựa từ **LSM cây (tree / 트리) và write-heavy workloads** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Row store và column store** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## OLTP và OLAP

Online giao dịch (transaction / 트랜잭션) Processing (OLTP / 온라인 트랜잭션 처리) phục vụ nhiều small reads/writes, tính đồng thời (concurrency / 동시성) cao, low độ trễ (latency / 지연 시간) và transactional invariants.

Online Analytical Processing (OLAP / 온라인 분석 처리) scan/aggregate lượng dữ liệu lớn để phân tích. Columnar lưu trữ (storage / 저장소) hiệu quả vì truy vấn (query / 쿼리) thường chỉ cần vài columns và values cùng column compress tốt.

Tải công việc (workload / 워크로드) shape khác khiến lưu trữ (storage / 저장소) bố cục (layout / 레이아웃) khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **NoSQL, phân tán (distributed / 분산) và analytical databases**, **Row store và column store** tiếp nhận điểm tựa từ **OLTP và OLAP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dữ liệu (data / 데이터) warehouse, lake và lakehouse** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Row store và column store

Row store đặt fields của một bản ghi (record / 레코드) gần nhau, tốt cho điểm (point / 지점) lookup/cập nhật (update / 업데이트) cả row. Column store đặt values cùng column gần nhau, tốt cho scan/aggregate và compression.

Không phải “column cơ sở dữ liệu (database / 데이터베이스) nhanh hơn”; nó nhanh cho tải công việc (workload / 워크로드) phù hợp và có trade-offs cho điểm (point / 지점) mutation.

> **Chuyển mạch:** Trong **NoSQL, phân tán (distributed / 분산) và analytical databases**, **Row store và column store** nêu điều cần giải thích; **Dữ liệu (data / 데이터) warehouse, lake và lakehouse** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Materialized view và precomputation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) warehouse, lake và lakehouse

Dữ liệu (data / 데이터) warehouse quản lý curated analytical dữ liệu (data / 데이터) với lược đồ (schema / 스키마)/truy vấn (query / 쿼리) engine chặt. dữ liệu (data / 데이터) lake lưu raw/semi-structured dữ liệu (data / 데이터) trên đối tượng (object / 객체) lưu trữ (storage / 저장소). Lakehouse cố kết hợp cheap open lưu trữ (storage / 저장소) với bảng (table / 테이블) siêu dữ liệu (metadata / 메타데이터), giao dịch (transaction / 트랜잭션) và truy vấn (query / 쿼리) ngữ nghĩa (semantics / 의미론) gần warehouse.

Các terms này là kiến trúc (architecture / 아키텍처) patterns hơn là strict scientific categories; vendors dùng terminology khác nhau.

> **Chuyển mạch:** Ở chặng này của **NoSQL, phân tán (distributed / 분산) và analytical databases**, **Dữ liệu (data / 데이터) warehouse, lake và lakehouse** nêu điều cần giải thích; **Materialized view và precomputation** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Materialized view và precomputation

Nếu analytical truy vấn (query / 쿼리) đắt nhưng dữ liệu (data / 데이터) cập nhật (update / 업데이트) ít hơn, có thể precompute aggregates/materialized views. Đây là same time-space sự đánh đổi (trade-off / 트레이드오프) như caching và động (dynamic / 동적) programming: dùng lưu trữ (storage / 저장소)/cập nhật (update / 업데이트) công việc (work / 작업) để giảm truy vấn (query / 쿼리) độ trễ (latency / 지연 시간).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **NoSQL, phân tán (distributed / 분산) và analytical databases**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **Materialized view và precomputation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“NoSQL tốt hơn SQL khi dữ liệu lớn.”** quy mô (scale / 규모) phụ thuộc kiến trúc (architecture / 아키텍처), partitioning, tải công việc (workload / 워크로드) và operations; relational các hệ thống (systems / 시스템들) cũng có phân tán (distributed / 분산) implementations.

**“Schema-less nghĩa là khỏi di chuyển (migration / 마이그레이션).”** cấu trúc (structure / 구조) vẫn đổi; chỉ chuyển burden sang ứng dụng (application / 애플리케이션)/read-time tính tương thích (compatibility / 호환성).

**“Eventual consistency nghĩa là random.”** Nó có formal guarantees tùy hệ thống (system / 시스템); cần đọc consistency đặc tả hợp đồng (contract / 계약) cụ thể.

> **Chuyển mạch:** Trong **NoSQL, phân tán (distributed / 분산) và analytical databases**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> cơ sở dữ liệu (database / 데이터베이스) kiến trúc (architecture / 아키텍처) là kết quả của ba câu hỏi: dữ liệu (data / 데이터) được partition/replicate thế nào, truy vấn (query / 쿼리) đường dẫn (path / 경로) cần locality nào, và invariants nào phải giữ mạnh tới mức nào.

> **Chuyển mạch:** Ở chặng này của **NoSQL, phân tán (distributed / 분산) và analytical databases**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Xem [transactions](./02_transactions_acid_and_concurrency_control.md), [storage/WAL/LSM](./04_storage_logs_recovery_and_durability.md), [distributed consistency](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md) và [replication/consensus](../06_networks_distributed_systems/05_replication_partitioning_and_consensus.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
