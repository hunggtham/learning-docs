# Index, B-tree, hashing và query execution

Không index, query `WHERE user_id = ?` trên table lớn có thể scan nhiều pages. Index (인덱스 / chỉ mục) tạo auxiliary structure để đổi thêm storage/write cost lấy read access nhanh hơn. Nhưng index chỉ hữu ích khi structure và query predicate/order match.

## B+ tree index

B+ tree có high fan-out và nodes page-sized, giữ keys ordered. Equality lookup đi root→internal nodes→leaf, thường depth nhỏ. Range scan tìm lower bound rồi walk linked leaves sequentially.

Ordered property hỗ trợ `<, >, BETWEEN`, prefix ordering và ORDER BY trong cases phù hợp. Composite index `(a,b,c)` được ordered lexicographically; predicates trên leading prefix thường khai thác tốt hơn skip leading columns.

“Leftmost prefix” là consequence của ordering, không rule thần bí.

## Hash index

Hash index map key qua hash buckets, tốt equality nhưng không giữ order cho range scan. Engine-specific implementations/limitations khác nhau.

## Clustered và secondary indexes

Clustered organization đặt table rows theo primary/cluster key order hoặc leaf itself contains row, tùy engine. Secondary index leaf thường chứa row locator/primary key. Lookup secondary có thể cần extra table/clustered lookup.

Wide primary keys vì vậy có thể làm secondary indexes lớn ở engines store PK in them.

## Covering index

Nếu index chứa đủ columns query cần, engine có thể answer từ index mà không fetch base row, giảm I/O. Included columns/visibility map semantics khác DB, nhưng principle là trade storage/write amplification lấy read locality.

## Selectivity và cardinality

Index trên boolean column thường không lọc nhiều rows nếu distribution gần 50/50; full scan có thể rẻ hơn random lookups. Optimizer estimate cardinality từ statistics/histograms để chọn plan.

Selectivity không phải property column cố định; predicate value và correlations ảnh hưởng. Parameter-sensitive plans có thể gặp “parameter sniffing”-style issues tùy DB.

## Query execution operators

Physical plan gồm operators như sequential/index scan, filter, sort, aggregate, nested-loop join, hash join, merge join. Mỗi operator có cost profile.

Nested loop tốt khi outer nhỏ và inner indexed. Hash join tốt equality joins với enough memory; build hash table một side. Merge join tận dụng sorted inputs và equality/range-like ordered processing.

Không có join algorithm luôn tốt nhất.

## Cost model và statistics

Optimizer search plan space, estimate I/O/CPU/memory. Exact optimal plan search có thể quá lớn với many joins, nên optimizers dùng dynamic programming/heuristics/pruning.

Bad cardinality estimate cascades: nghĩ intermediate result 10 rows nhưng thật 1M có thể chọn nested loop tệ. `EXPLAIN`/actual plan giúp so estimate vs actual.

## Sorting, spilling và memory

Sort/hash operators cần working memory. Nếu vượt budget, spill disk làm latency tăng lớn. Query tuning vì vậy liên quan row width, cardinality, memory grant và concurrent workloads—not chỉ index presence.

## Index maintenance

Insert/update/delete phải update indexes. Nhiều indexes tăng write amplification, storage và vacuum/maintenance. Random insert key có thể cause page splits; monotonically increasing key tạo locality nhưng có hot-page contention ở high concurrency.

## Mental Model

> Index là **materialized alternate access path**. Nó đáng giá nếu query savings vượt write/storage/maintenance cost. Optimizer chọn path dựa estimated cardinality và cost, không theo rule “có index thì dùng”.

## Common Misconceptions

**“Thêm index luôn làm query nhanh.”** Có thể không được chọn, tăng writes hoặc làm planner choices khác.

**“Composite index dùng được như nhau cho mọi column.”** Ordering/prefix matters.

**“EXPLAIN cost là milliseconds.”** Cost units thường internal/relative, engine-specific; cần actual timings/buffers để validate.

## Kết nối

[B+ trees](../01_algorithms_data_structures/05_trees_heaps_and_search_structures.md), [hashing](../01_algorithms_data_structures/04_hashing_and_hash_tables.md) và [sorting](../01_algorithms_data_structures/07_sorting_searching_and_selection.md) trở thành database operators ở đây. [Storage engine](./04_storage_logs_recovery_and_durability.md) giải thích pages/WAL bên dưới.
