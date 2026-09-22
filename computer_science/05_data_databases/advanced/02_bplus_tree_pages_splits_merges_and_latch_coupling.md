# B+Tree page layout, splits/merges và latch coupling

B+Tree thường được giới thiệu như “balanced tree có O(log n)”. Điều đó đúng nhưng chưa đủ để giải thích database index production. B+Tree tồn tại vì nó giữ một invariant rất thực tế: **mỗi traversal phải đi qua một cấu trúc page-oriented luôn hợp lệ dưới concurrent read/write, trong khi tree vẫn đủ nông để giảm I/O và cache miss.**

Performance thật không được quyết định chỉ bởi `O(log n)`, mà bởi page layout, fan-out, buffer-pool residency, split/merge protocol, latch contention, WAL và key distribution.

## 1. Vì sao database không dùng binary search tree thông thường?

Binary tree có branching factor thấp. Nếu mỗi pointer hop thành một random page access, số I/O rất lớn. B+Tree đóng hàng trăm keys/pointers vào một page để mỗi page access mang về nhiều routing information.

Nếu fan-out là vài trăm, tree hàng triệu hoặc hàng tỷ records vẫn chỉ cần vài levels.

```text
root
  ↓
internal page
  ↓
internal/leaf page
```

Height nhỏ là một invariant performance quan trọng vì mỗi level có thể là buffer lookup hoặc storage access.

## 2. Internal page và leaf page có vai trò khác nhau

Internal page chứa separator keys và child page IDs. Leaf page chứa index entries; tùy clustered/nonclustered design, leaf có thể chứa full row, primary key hoặc row locator.

Leaves thường linked theo key order. Sau khi tìm điểm bắt đầu, range scan có thể đi tuần tự qua sibling leaves thay vì quay lại root cho từng key.

Đây là lý do một cấu trúc vừa phục vụ equality lookup vừa phục vụ ordered range scan tốt.

## 3. Page thực tế không chỉ là array keys

Một page cần header và metadata như page id/type, free-space state, sibling links, LSN/checksum tùy engine. Variable-length records thường dùng **slot directory** để logical slot ổn định hơn dù bytes bên trong page được compact/move.

Điểm này quan trọng vì một update `VARCHAR` dài hơn có thể làm record move trong page mà logical key không đổi. Physical layout vì thế tác động trực tiếp tới write amplification và fragmentation.

## 4. Search đi qua buffer pool trước khi đi tới storage

Logical path root → internal → leaf không đồng nghĩa mỗi level gây disk I/O. Hot root/internal pages thường ở buffer pool. Leaf access hoặc base-table lookup mới có thể là random I/O đáng kể.

Cost model cần tách:

```text
tree height
×
page residency/cache hit
×
storage latency
×
key/record width
```

Hai indexes cùng height có thể có performance rất khác nếu một index lớn hơn và ít fit cache hơn.

## 5. Search trong page cũng có microarchitectural cost

Bên trong page, engine có thể binary-search separator keys, dùng prefix compression hoặc layout tối ưu cache/SIMD tùy implementation.

Khi index nằm phần lớn trong memory, branch prediction, cache-line footprint và key width có thể quan trọng gần như storage I/O.

Đây là connection giữa database internals và Computer Architecture: asymptotic complexity không mô tả toàn bộ behavior khi hierarchy memory chi phối latency.

## 6. Insert và page split

Nếu leaf còn free space, insert tương đối local. Khi page đầy, engine phải split:

```text
[ A B C D E F ]
        ↓
[ A B C ] <-> [ D E F ]
        ↑
parent nhận separator
```

Nếu parent đầy, split có thể propagate lên; root split làm tree cao thêm một level.

Split không chỉ là array operation. Nó cần structural synchronization, WAL/logging, dirty pages và recovery semantics.

Invariant là concurrent readers/writers không được thấy tree ở trạng thái làm mất key, đi sai child hoặc tạo unreachable page.

## 7. Fill factor là trade-off density với future write cost

Page build 100% full tối ưu density hiện tại nhưng random inserts dễ gây split sớm. Fill factor để lại free space để hấp thụ future writes.

Đổi lại:

```text
free space nhiều
→ page count tăng
→ cache footprint tăng
→ range scan đọc nhiều pages hơn
```

Không có fill factor đúng universal. Append-heavy và random-key workloads tạo pressure khác nhau.

## 8. Key distribution quyết định hotspot

Monotonically increasing IDs tập trung insert ở rightmost leaf. Điều này có locality tốt nhưng có thể tạo latch/write hotspot. Random UUID phân tán inserts rộng hơn nhưng làm page locality và fragmentation pattern khác.

Khi scale write concurrency, câu hỏi không chỉ “index có selectivity tốt không?” mà còn “writes tập trung vào bao nhiêu leaves?”.

## 9. Delete và merge trong production không giống textbook tuyệt đối

Textbook B-tree thường redistribute/merge để giữ occupancy bound chặt sau delete. Database engine thực tế có thể trì hoãn cleanup vì merge cũng tạo write amplification và synchronization cost.

Do đó sparse/fragmented pages có thể tồn tại cho tới background maintenance/rebuild/vacuum tùy engine.

Invariant production thường yếu hơn “mọi page luôn >= 50% full”, nhưng mạnh hơn ở correctness: search/range order vẫn đúng và page graph vẫn reachable hợp lệ.

## 10. Latch khác transaction lock

**Lock** bảo vệ logical database state giữa transactions. **Latch** bảo vệ in-memory data structure trong critical section rất ngắn.

Một row lock có thể sống hàng giây theo transaction. Page/tree latch thường chỉ sống micro/milliseconds hoặc ngắn hơn tùy implementation.

Vì vậy `lock wait` và `latch contention` là hai failure families khác nhau:

```text
transaction lock -> isolation/business concurrency
latch             -> internal structure concurrency
```

Chẩn đoán sai loại wait dẫn tới fix sai abstraction layer.

## 11. Latch coupling / crabbing

Trong traversal concurrent, thread có thể giữ latch parent, acquire latch child rồi release parent khi child được xem là safe cho operation.

Insert/delete phức tạp hơn read vì child có thể split/merge. Protocol phải giữ invariant rằng structure không bị thay đổi dưới chân traversal theo cách làm pointer/search path mất validity.

Nếu latch toàn tree để đơn giản correctness, concurrency sẽ collapse. Vì vậy B+Tree design luôn trade proof complexity lấy parallelism.

## 12. Optimistic traversal và B-link style reasoning

Read-heavy indexes có thể dùng version checks, sibling links hoặc optimistic techniques: traverse nhẹ, validate state, retry khi detect concurrent structural change.

Mental model giống optimistic concurrency control:

```text
đọc nhanh dưới assumption
→ validate invariant
→ retry nếu conflict
```

Mục tiêu là tránh exclusive/shared latch ở hot ancestors nhiều hơn mức cần thiết.

## 13. Covering index: ít lookup hơn nhưng page lớn hơn

Nếu index chứa đủ columns để trả query, engine có thể tránh base-table lookup. Nhưng leaf entry lớn hơn làm:

```text
fan-out giảm
page count tăng
cache footprint tăng
write amplification tăng
```

Index design là trade-off read-path reduction với memory/storage/write pressure, không chỉ “query có dùng index hay không”.

## 14. Composite key và leftmost-prefix từ physical ordering

Index `(a, b)` được sắp lexicographically. Query theo `a` hoặc `(a,b)` thường map thành contiguous range tốt; query chỉ theo `b` không có cùng property vì values của `b` bị xen giữa các groups `a`.

“Leftmost prefix” không phải mẹo để học thuộc. Nó xuất phát từ ordering vật lý của leaf keys.

## 15. Failure mode dưới concurrency và pressure

Các symptom điển hình:

```text
hot leaf/root latch contention
page-split burst khi write spike
index bloat/fragmentation
cache miss tăng vì index quá rộng
range scan chậm vì page density thấp
WAL/write pressure tăng do structural changes
```

Một query plan vẫn “dùng đúng index” nhưng latency có thể xấu vì internals above.

## 16. Production evidence

Evidence cần nối logical SQL với physical index behavior:

```text
execution plan + actual rows/pages
buffer/cache hit ratio phù hợp ngữ cảnh
index/page size và depth
page split/maintenance statistics nếu engine expose
latch/internal wait events
WAL/log volume
I/O latency và random-read pressure
key distribution/hot partition evidence
```

Tên view/wait event khác theo PostgreSQL, Oracle, MySQL/InnoDB, SQL Server. Mental model không phụ thuộc vendor: **đo traversal cost, residency, structural write và contention**.

## 17. Lower layer nào quyết định behavior?

Nếu point lookup chậm vì leaf miss, buffer pool/storage quyết định cost. Nếu write concurrency không scale, page/latch hotspot có thể quyết định. Nếu wide covering index làm cache pressure, data layout quyết định. Nếu split burst làm commit latency tăng, WAL/filesystem path có thể trở thành bottleneck bên dưới.

B+Tree là một abstraction giao nhau giữa algorithm, database concurrency, OS I/O và hardware cache.

## 18. Mô hình tư duy

> B+Tree production là **một hierarchy fixed-size pages giữ ordered-search invariant dưới concurrency**. Fan-out giữ tree nông; buffer pool quyết định bao nhiêu hop thành I/O; split/merge là structural writes; latch giữ structure ngắn hạn; transaction lock giữ isolation logic; key/layout quyết định hotspot và cache footprint.

## Kết nối

Đọc tiếp [LSM Tree](./03_lsm_tree_compaction_bloom_filters_and_write_amplification.md), [Buffer pool](./04_buffer_pool_replacement_and_dirty_page_management.md), [Cost-based optimizer](./05_cost_based_optimizer_cardinality_estimation_and_statistics.md), [Memory/cache hierarchy](../../02_computer_architecture/advanced/03_advanced_cache_hierarchy_prefetching_and_replacement.md) và [Durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).