# Chỉ mục (index / 인덱스), B-tree, hashing và truy vấn (query / 쿼리) thực thi (execution / 실행)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Chỉ mục (index / 인덱스), B-tree, hashing và truy vấn (query / 쿼리) thực thi (execution / 실행)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **B+ cây (tree / 트리) chỉ mục (index / 인덱스)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Băm (hash / 해시) chỉ mục (index / 인덱스)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Không chỉ mục (index / 인덱스), truy vấn (query / 쿼리) `WHERE user_id = ?` trên bảng (table / 테이블) lớn có thể scan nhiều pages. chỉ mục (index / 인덱스) tạo auxiliary cấu trúc (structure / 구조) để đổi thêm lưu trữ (storage / 저장소)/ghi (write / 쓰기) chi phí (cost / 비용) lấy read truy cập (access / 접근) nhanh hơn. Nhưng chỉ mục (index / 인덱스) chỉ hữu ích khi cấu trúc (structure / 구조) và truy vấn (query / 쿼리) predicate/thứ tự (order / 순서) match.

## B+ cây (tree / 트리) chỉ mục (index / 인덱스)

B+ cây (tree / 트리) có high fan-out và nodes page-sized, giữ keys ordered. Equality lookup đi gốc (root / 루트)→nội bộ (internal / 내부) nodes→leaf, thường độ sâu (depth / 깊이) nhỏ. phạm vi (range / 범위) scan tìm lower bound rồi walk linked leaves sequentially.

Ordered thuộc tính (property / 속성) hỗ trợ `<, >, BETWEEN`, prefix thứ tự (ordering / 순서) và thứ tự (order / 순서) BY trong cases phù hợp. Composite chỉ mục (index / 인덱스) `(a,b,c)` được ordered lexicographically; predicates trên leading prefix thường khai thác tốt hơn skip leading columns.

“Leftmost prefix” là consequence của thứ tự (ordering / 순서), không quy tắc (rule / 규칙) thần bí.

> **Chuyển mạch:** Trong **Chỉ mục (index / 인덱스), B-tree, hashing và truy vấn (query / 쿼리) thực thi (execution / 실행)**, **Băm (hash / 해시) chỉ mục (index / 인덱스)** tiếp nhận điểm tựa từ **B+ cây (tree / 트리) chỉ mục (index / 인덱스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Clustered và secondary indexes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Băm (hash / 해시) chỉ mục (index / 인덱스)

Băm (hash / 해시) chỉ mục (index / 인덱스) map key qua băm (hash / 해시) buckets, tốt equality nhưng không giữ thứ tự (order / 순서) cho phạm vi (range / 범위) scan. Engine-specific implementations/limitations khác nhau.

> **Chuyển mạch:** Ở chặng này của **Chỉ mục (index / 인덱스), B-tree, hashing và truy vấn (query / 쿼리) thực thi (execution / 실행)**, **Clustered và secondary indexes** tiếp nhận điểm tựa từ **Băm (hash / 해시) chỉ mục (index / 인덱스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Covering chỉ mục (index / 인덱스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Clustered và secondary indexes

Clustered organization đặt bảng (table / 테이블) rows theo primary/cluster key thứ tự (order / 순서) hoặc leaf itself contains row, tùy engine. Secondary chỉ mục (index / 인덱스) leaf thường chứa row locator/primary key. Lookup secondary có thể cần extra bảng (table / 테이블)/clustered lookup.

Wide primary keys vì vậy có thể làm secondary indexes lớn ở engines store PK in them.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chỉ mục (index / 인덱스), B-tree, hashing và truy vấn (query / 쿼리) thực thi (execution / 실행)**, **Covering chỉ mục (index / 인덱스)** tiếp nhận điểm tựa từ **Clustered và secondary indexes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Selectivity và cardinality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Covering chỉ mục (index / 인덱스)

Nếu chỉ mục (index / 인덱스) chứa đủ columns truy vấn (query / 쿼리) cần, engine có thể answer từ chỉ mục (index / 인덱스) mà không fetch cơ sở (base / 기반) row, giảm I/O. Included columns/visibility map ngữ nghĩa (semantics / 의미론) khác DB, nhưng principle là trade lưu trữ (storage / 저장소)/ghi (write / 쓰기) amplification lấy read locality.

> **Chuyển mạch:** Trong **Chỉ mục (index / 인덱스), B-tree, hashing và truy vấn (query / 쿼리) thực thi (execution / 실행)**, **Selectivity và cardinality** tiếp nhận điểm tựa từ **Covering chỉ mục (index / 인덱스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Truy vấn (query / 쿼리) thực thi (execution / 실행) operators** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Selectivity và cardinality

Chỉ mục (index / 인덱스) trên boolean column thường không lọc nhiều rows nếu phân phối (distribution / 분포) gần 50/50; full scan có thể rẻ hơn random lookups. Optimizer estimate cardinality từ statistics/histograms để chọn plan.

Selectivity không phải thuộc tính (property / 속성) column cố định; predicate giá trị (value / 값) và correlations ảnh hưởng. Parameter-sensitive plans có thể gặp “parameter sniffing”-style issues tùy DB.

> **Chuyển mạch:** Ở chặng này của **Chỉ mục (index / 인덱스), B-tree, hashing và truy vấn (query / 쿼리) thực thi (execution / 실행)**, **Truy vấn (query / 쿼리) thực thi (execution / 실행) operators** tiếp nhận điểm tựa từ **Selectivity và cardinality** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chi phí (cost / 비용) mô hình (model / 모델) và statistics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Truy vấn (query / 쿼리) thực thi (execution / 실행) operators

Vật lý (physical / 물리적) plan gồm operators như sequential/chỉ mục (index / 인덱스) scan, filter, sort, aggregate, nested-loop phép nối (join / 조인), băm (hash / 해시) phép nối (join / 조인), merge phép nối (join / 조인). Mỗi operator có chi phí (cost / 비용) profile.

Nested vòng lặp (loop / 루프) tốt khi outer nhỏ và inner indexed. băm (hash / 해시) phép nối (join / 조인) tốt equality joins với enough bộ nhớ (memory / 메모리); bản dựng (build / 빌드) bảng băm (hash table / 해시 테이블) một side. Merge phép nối (join / 조인) tận dụng sorted inputs và equality/range-like ordered processing.

Không có phép nối (join / 조인) thuật toán (algorithm / 알고리즘) luôn tốt nhất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chỉ mục (index / 인덱스), B-tree, hashing và truy vấn (query / 쿼리) thực thi (execution / 실행)**, **Chi phí (cost / 비용) mô hình (model / 모델) và statistics** tiếp nhận điểm tựa từ **Truy vấn (query / 쿼리) thực thi (execution / 실행) operators** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sorting, spilling và bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí (cost / 비용) mô hình (model / 모델) và statistics

Optimizer tìm kiếm (search / 검색) plan không gian (space / 공간), estimate I/O/CPU/bộ nhớ (memory / 메모리). chính xác (exact / 정확한) optimal plan tìm kiếm (search / 검색) có thể quá lớn với many joins, nên optimizers dùng động (dynamic / 동적) programming/heuristics/pruning.

Bad cardinality estimate cascades: nghĩ intermediate kết quả (result / 결과) 10 rows nhưng thật 1M có thể chọn nested vòng lặp (loop / 루프) tệ. `EXPLAIN`/actual plan giúp so estimate vs actual.

> **Chuyển mạch:** Trong **Chỉ mục (index / 인덱스), B-tree, hashing và truy vấn (query / 쿼리) thực thi (execution / 실행)**, **Sorting, spilling và bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Chi phí (cost / 비용) mô hình (model / 모델) và statistics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chỉ mục (index / 인덱스) maintenance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sorting, spilling và bộ nhớ (memory / 메모리)

Sort/băm (hash / 해시) operators cần working bộ nhớ (memory / 메모리). Nếu vượt ngân sách (budget / 예산), spill disk làm độ trễ (latency / 지연 시간) tăng lớn. truy vấn (query / 쿼리) tuning vì vậy liên quan row width, cardinality, bộ nhớ (memory / 메모리) grant và concurrent workloads—not chỉ chỉ mục (index / 인덱스) presence.

> **Chuyển mạch:** Ở chặng này của **Chỉ mục (index / 인덱스), B-tree, hashing và truy vấn (query / 쿼리) thực thi (execution / 실행)**, **Chỉ mục (index / 인덱스) maintenance** tiếp nhận điểm tựa từ **Sorting, spilling và bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chỉ mục (index / 인덱스) maintenance

Insert/cập nhật (update / 업데이트)/delete phải cập nhật (update / 업데이트) indexes. Nhiều indexes tăng ghi (write / 쓰기) amplification, lưu trữ (storage / 저장소) và vacuum/maintenance. Random insert key có thể cause page splits; monotonically increasing key tạo locality nhưng có hot-page contention ở high tính đồng thời (concurrency / 동시성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chỉ mục (index / 인덱스), B-tree, hashing và truy vấn (query / 쿼리) thực thi (execution / 실행)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Chỉ mục (index / 인덱스) maintenance** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> chỉ mục (index / 인덱스) là **materialized alternate truy cập (access / 접근) đường dẫn (path / 경로)**. Nó đáng giá nếu truy vấn (query / 쿼리) savings vượt ghi (write / 쓰기)/lưu trữ (storage / 저장소)/maintenance chi phí (cost / 비용). Optimizer chọn đường dẫn (path / 경로) dựa estimated cardinality và chi phí (cost / 비용), không theo quy tắc (rule / 규칙) “có chỉ mục (index / 인덱스) thì dùng”.

> **Chuyển mạch:** Trong **Chỉ mục (index / 인덱스), B-tree, hashing và truy vấn (query / 쿼리) thực thi (execution / 실행)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Thêm chỉ mục (index / 인덱스) luôn làm truy vấn (query / 쿼리) nhanh.”** Có thể không được chọn, tăng writes hoặc làm planner choices khác.

**“Composite chỉ mục (index / 인덱스) dùng được như nhau cho mọi column.”** thứ tự (ordering / 순서)/prefix matters.

**“EXPLAIN chi phí (cost / 비용) là milliseconds.”** chi phí (cost / 비용) units thường nội bộ (internal / 내부)/relative, engine-specific; cần actual timings/buffers để validate.

> **Chuyển mạch:** Ở chặng này của **Chỉ mục (index / 인덱스), B-tree, hashing và truy vấn (query / 쿼리) thực thi (execution / 실행)**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[B+ trees](../01_algorithms_data_structures/05_trees_heaps_and_search_structures.md), [hashing](../01_algorithms_data_structures/04_hashing_and_hash_tables.md) và [sorting](../01_algorithms_data_structures/07_sorting_searching_and_selection.md) trở thành cơ sở dữ liệu (database / 데이터베이스) operators ở đây. [Storage engine](./04_storage_logs_recovery_and_durability.md) giải thích pages/WAL bên dưới.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
