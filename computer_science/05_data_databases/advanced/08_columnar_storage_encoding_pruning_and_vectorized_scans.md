# Columnar storage, encoding, pruning và vectorized scans

Đọc trước [NoSQL, distributed và analytical databases](../../basic/05_data_databases/07_nosql_distributed_and_analytical_databases.md) để có khái niệm OLTP/OLAP, và [join algorithms, vectorized execution, late materialization](./06_join_algorithms_vectorized_execution_and_late_materialization.md) để nối storage path với execution engine.

Chapter này tập trung vào một câu hỏi khác B+Tree hay LSM: **khi workload đọc rất nhiều rows nhưng chỉ cần một số columns và thường thực hiện aggregate/filter, physical layout nào giảm bytes phải đọc và tăng work hữu ích trên mỗi CPU cycle?**

Mental model:

```text
logical table
→ row groups / column chunks
→ encoding + compression + metadata
→ pruning / projection
→ decode in vectors
→ predicate / aggregate / join
→ late materialization
→ result
```

## 1. Row store tối ưu locality theo record; column store tối ưu locality theo attribute

Trong row-oriented layout, các fields của một row nằm gần nhau. Điều này rất hợp với point lookup hoặc transaction cần đọc/ghi phần lớn record.

Trong columnar layout, values của cùng một column được đặt gần nhau. Một query như:

```sql
SELECT region, SUM(amount)
FROM sales
WHERE event_date >= ...
GROUP BY region;
```

không cần đọc `customer_name`, `shipping_address`, `comment` hoặc nhiều columns khác. Columnar storage giảm I/O bằng cách chỉ mang các column chunks cần thiết qua storage/memory hierarchy.

Đây là invariant performance đầu tiên:

> Không chuyển bytes qua disk → memory → cache → CPU nếu query không cần chúng.

## 2. Row group tạo compromise giữa locality và parallelism

Column store thường không lưu “một file cho mỗi column toàn table” vô hạn. Dữ liệu được chia thành **row groups**, mỗi row group chứa column chunks tương ứng cho một range rows.

Row group quá nhỏ làm metadata và seek/object-request overhead tăng. Quá lớn làm pruning thô, memory working set lớn và task parallelism kém linh hoạt.

Vì vậy row-group size là trade-off giữa scan efficiency, pruning granularity, compression ratio và scheduling flexibility.

## 3. Encoding và compression không chỉ để tiết kiệm disk

Values cùng column thường có distribution thuận lợi cho encoding. Ví dụ categorical string có thể dictionary encode thành integer IDs; sorted integer có thể delta encode; repeated values có thể run-length encode; small domains có thể bit-pack.

Compression đem lại một hiệu ứng quan trọng: **đọc ít bytes hơn có thể nhanh hơn dù CPU phải decode**. Nếu bottleneck nằm ở storage hoặc memory bandwidth, thêm decode compute để giảm bytes có thể tăng overall throughput.

Ngược lại, nếu data đã ở cache và decoder quá đắt, compression mạnh hơn chưa chắc nhanh hơn. Performance phụ thuộc bottleneck hiện tại.

## 4. Dictionary encoding đổi string comparison thành integer-domain work

Giả sử column `country` chỉ có vài chục values. Thay vì lặp chuỗi dài cho hàng triệu rows, storage lưu dictionary và sequence IDs.

Predicate `country = 'KR'` có thể resolve `'KR'` thành dictionary ID rồi scan integer IDs. Điều này giảm footprint và thường thân thiện hơn với SIMD/cache.

Nhưng dictionary có scope. Dictionary per page/row-group giúp local compression tốt nhưng complicate comparison/merge giữa chunks. Global dictionary dễ reuse ID nhưng khó maintain khi cardinality drift hoặc distributed ingest.

## 5. Zone map/min-max metadata biến scan thành skip

Nếu mỗi chunk lưu min/max, query `event_date BETWEEN A AND B` có thể bỏ qua chunk mà range không overlap.

Đây là **data skipping**: không tăng tốc việc xử lý row; nó loại bỏ cả vùng dữ liệu trước khi đọc/decode.

Hiệu quả phụ thuộc physical clustering. Nếu values ngẫu nhiên, hầu hết row group đều có min/max rất rộng và pruning yếu. Nếu data được sort/cluster theo query dimension, min/max trở nên sắc hơn.

Vì vậy layout và workload query phải được reasoning cùng nhau.

## 6. Bloom filter giúp negative pruning nhưng không chứng minh presence

Một chunk-level Bloom filter có thể nói “giá trị chắc chắn không có” hoặc “có thể có”. Nó hữu ích cho equality predicate trên high-cardinality column khi min/max ít giá trị.

False positive làm query đọc thêm chunk nhưng không gây false negative nếu implementation đúng. Memory dành cho Bloom filters và number of hash probes là trade-off giữa metadata size và I/O tránh được.

## 7. Projection pushdown quyết định columns nào đi vào pipeline

Storage reader cần biết query chỉ yêu cầu columns nào. Nếu execution layer materialize full row quá sớm, lợi thế columnar bị phá.

Projection pushdown đẩy knowledge này xuống scan:

```text
query references A, C, F
→ storage reads only A, C, F chunks
→ unused columns never enter memory pipeline
```

Trong distributed/object storage, tránh tải unused columns còn giảm network egress và request cost.

## 8. Predicate pushdown cần phân biệt metadata filter và row filter

Predicate có thể được dùng ở nhiều mức:

```text
partition pruning
→ file pruning
→ row-group pruning
→ page pruning
→ vector predicate
→ row-level residual filter
```

Không phải predicate nào cũng push xuống được. User-defined function phức tạp, collation semantics hoặc expression phụ thuộc runtime state có thể buộc engine đọc/decode rồi mới đánh giá.

Senior debugging cần biết filter đang loại data ở layer nào, không chỉ thấy SQL có `WHERE`.

## 9. Vectorized scan làm việc trên batch thay vì tuple-at-a-time

Tuple-at-a-time interpreter thường lặp qua row và virtual/function dispatch cho từng operator. Vectorized execution xử lý batch values, giảm branch/dispatch overhead và tạo cơ hội SIMD.

Ví dụ scan một vector 1024 integers, so sánh với threshold rồi sinh selection vector. Aggregate chỉ xử lý positions còn sống thay vì materialize object cho từng row.

Mental model:

```text
encoded column chunk
→ decode batch
→ SIMD/vector predicate
→ selection vector
→ aggregate/join
```

## 10. Selection vector giữ “row identity” mà không materialize cả row

Sau filter, engine có thể giữ danh sách offsets/bitmask của rows hợp lệ. Các operators sau dùng selection vector để chỉ đụng dữ liệu cần thiết.

Điều này giảm copying nhưng có cost khi selectivity cao/thấp khác nhau. Với gần 100% rows survive, maintaining sparse index có thể không lợi. Engine thường có multiple code paths tùy density.

## 11. Late materialization trì hoãn reconstruction của row

Nếu query filter mạnh, ta nên filter bằng columns rẻ trước rồi chỉ fetch/materialize columns output cho surviving rows.

Ví dụ:

```text
scan event_date + status
→ filter 100M rows xuống 200K
→ fetch expensive description column chỉ cho 200K rows
```

Late materialization giảm memory traffic nhưng cần giữ mapping từ logical row position sang column values. Join/reorder có thể làm mapping phức tạp hơn.

## 12. Null representation là một physical design concern

Nullable column thường có validity bitmap riêng. Engine có thể process values và null mask theo vector operations thay vì branch mỗi row.

Nhưng SQL three-valued logic vẫn phải được giữ. Optimization không được đổi semantics của `NULL`, especially trong predicate, join và aggregate.

Physical representation được phép thay; logical invariant không được thay.

## 13. Nested data cần thêm structure ngoài flat column

Array/object nested không thể chỉ “tách mỗi field thành một flat vector” nếu muốn reconstruct hierarchy. Columnar formats thường cần offsets, definition/repetition style metadata hoặc equivalent structure để biểu diễn missing/nesting boundaries.

Điều này tăng complexity của scan và predicate pushdown. Query vào nested data có thể vẫn đọc ít fields, nhưng engine phải giữ structural alignment.

## 14. Updates và deletes là điểm khó của immutable columnar layout

Columnar chunks tối ưu scan thường gần immutable. Random in-place update phá compression, clustering và large sequential layout.

Nhiều analytical systems dùng delta structures, delete vectors, append-new-version hoặc background rewrite/compaction.

Pipeline có thể trở thành:

```text
base immutable segment
+ delta/update/delete metadata
→ query merges visibility
→ background compaction rewrites clean segment
```

Điều này giống một dạng debt: foreground update nhanh hơn nhưng read path và background maintenance phải trả chi phí sau.

## 15. Compaction/reclustering đổi write cost để mua pruning quality

Khi ingest làm dữ liệu mất sort order, zone map và compression có thể kém dần. Reclustering/compaction sắp xếp lại data để phục hồi locality.

Nhưng rewrite terabytes dữ liệu cạnh tranh I/O/network/CPU với queries. Hệ thống cần throttle maintenance và chọn lúc lợi ích pruning lớn hơn rewrite cost.

Không có trạng thái “columnar table đã optimize xong vĩnh viễn”. Workload và data distribution thay đổi theo thời gian.

## 16. Memory bandwidth thường là bottleneck trước ALU

Analytical scan có thể thực hiện arithmetic rất đơn giản trên lượng data lớn. CPU utilization cao không có nghĩa ALU là bottleneck; cores có thể chờ memory.

Compression, vectorization, prefetch và data layout cùng mục tiêu tăng **useful work per byte moved**. Đây là connection trực tiếp với operational intensity/roofline reasoning trong [capacity planning](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md).

## 17. Spill là phase change của execution

Hash aggregate/join/sort có thể chạy in-memory tới một threshold. Khi memory budget vượt giới hạn, engine partition và spill ra disk/object storage.

Latency lúc này không tăng tuyến tính; execution mode đổi phase:

```text
in-memory
→ memory pressure
→ spill
→ extra serialization + I/O + merge passes
```

Một query chậm 10× có thể không phải “data tăng 10×” mà vì vừa vượt memory threshold.

## 18. Distributed analytical scan thêm network và skew

Khi row groups phân tán, scheduler cố gắng đẩy scan gần data hoặc phân chia ranges song song. Partition skew làm một số workers xong sớm còn một worker giữ tail latency.

Pruning tốt giảm cả storage I/O lẫn network shuffle. Nhưng join/group-by có thể vẫn tạo shuffle mới sau scan. Vì vậy cần phân biệt **bytes read from storage** và **bytes exchanged between workers**.

## 19. Failure modes và correctness

Corrupt page/chunk cần checksum hoặc integrity evidence. Metadata min/max sai có thể nguy hiểm hơn slow query vì engine có thể prune nhầm data hợp lệ. Dictionary/encoding decoder bug có thể tạo silent corruption nếu validation yếu.

Optimization metadata được phép gây false-positive work, nhưng không được gây false-negative result trừ khi semantics explicitly approximate.

Đây là một invariant đáng nhớ:

> Pruning metadata có thể bỏ lỡ cơ hội skip; không được skip dữ liệu có thể chứa kết quả đúng.

## 20. Production evidence

Khi query chậm, nên tách evidence theo pipeline:

```text
partitions/files considered
→ row groups pruned
→ bytes read
→ compressed vs decoded bytes
→ rows scanned / rows selected
→ vector batch efficiency
→ spill bytes / passes
→ shuffle bytes
→ CPU vs memory-bandwidth vs I/O wait
```

Execution plan chỉ cho biết intended operators; runtime counters mới cho thấy selectivity/cardinality thực tế và phase change.

## 21. Worked example: dashboard aggregate

Một dashboard đọc 2 năm dữ liệu nhưng chỉ hiển thị 7 ngày gần nhất. Nếu table partition/cluster theo date, partition + row-group pruning có thể giảm scan từ terabytes xuống gigabytes trước khi decode.

Sau đó chỉ `region`, `amount` và `date` được project. `date` filter sinh selection vector; `region`/`amount` chỉ được xử lý cho surviving rows. Aggregate chạy vectorized. Nếu group cardinality quá lớn và memory budget thiếu, hash aggregate spill và latency đổi hẳn.

Cùng SQL text có thể rất nhanh hoặc rất chậm tùy physical clustering, stats, pruning rate và memory threshold.

## 22. Kết nối sang các chapter khác

Columnar storage nối với [cost-based optimizer](./05_cost_based_optimizer_cardinality_estimation_and_statistics.md), [join/vectorized execution](./06_join_algorithms_vectorized_execution_and_late_materialization.md), [LSM/compaction](./03_lsm_tree_compaction_bloom_filters_and_write_amplification.md) về maintenance debt, và [capacity/whole-system profiling](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md).

Mental model cuối cùng: **analytical performance đến từ việc loại work càng sớm càng tốt, giữ representation compact càng lâu càng tốt, và chỉ materialize bytes/rows thật sự cần cho kết quả.**