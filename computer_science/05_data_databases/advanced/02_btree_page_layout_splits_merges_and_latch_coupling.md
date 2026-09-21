# B+Tree page layout, splits/merges và latch coupling

Biết B+Tree có `O(log n)` search chưa đủ để hiểu database index production. Performance và concurrency phụ thuộc cách nodes map thành **pages**, keys/records được packed ra sao, page split thế nào, và nhiều threads thay tree mà không phá invariants bằng latch protocol nào.

## B+Tree được thiết kế quanh page I/O

Binary search tree mỗi node vài bytes không phù hợp storage vì mỗi pointer hop có thể thành random I/O/cache miss. B+Tree dùng branching factor lớn để mỗi node gần kích thước page/block.

Nếu một page chứa hàng trăm keys, tree hàng triệu rows chỉ cần vài levels.

```text
root
  ↓
internal page
  ↓
leaf page
```

Height nhỏ là lý do B+Tree thống trị OLTP indexes.

## Internal page và leaf page

Internal page chứa separator keys và child pointers/page IDs. Leaf page chứa index entries; tùy clustered/nonclustered design, leaf có thể chứa full row, primary key hoặc row locator.

Leaves thường linked theo key order để range scan đi tuần tự sau khi tìm điểm bắt đầu.

Vì vậy equality lookup và range scan đều hiệu quả trên cùng structure.

## Page header và slot directory

Page thực tế cần header: page ID, type, sibling links, free-space metadata, LSN/checksum tùy engine.

Variable-length records thường không đơn giản packed cứng từ đầu page. **Slot directory** cho phép record data di chuyển trong page mà logical slot ID ổn định hơn.

Mental model page quan trọng vì update một varchar dài hơn có thể cần compact/move record dù key logic không đổi.

## Search trong page

Trong mỗi internal node, engine tìm separator để chọn child. Có thể binary search, SIMD-friendly search hoặc layout tối ưu cache tùy implementation.

Asymptotic `log_B(n)` không cho biết cache behavior; page layout và branch prediction có thể ảnh hưởng mạnh với in-memory indexes.

## Insert và page split

Nếu leaf còn free space, insert tương đối local. Khi page đầy, engine phải split:

```text
[ A B C D E F ]
        ↓ split
[ A B C ] <-> [ D E F ]
        ↑ parent nhận separator
```

Nếu parent cũng đầy, split propagate lên; root split làm tree cao thêm một level.

Split gây write amplification, log records và concurrency complexity lớn hơn một simple array insert.

## Fill factor

Nếu build page 100% full, random inserts sớm gây split. Fill factor để lại free space nhằm hấp thụ future inserts.

Nhưng để quá nhiều free space tăng page count, memory footprint và I/O. Workload append-only và random-key insertion cần tuning khác nhau.

Sequential keys như increasing IDs thường concentrate inserts ở rightmost leaf; random UUID phân tán writes nhưng làm locality/page split pattern khác.

## Merge và underflow

Delete làm page sparse. Textbook B-tree thường merge/redistribute để giữ occupancy bound chặt. Production engines có thể trì hoãn hoặc dùng background cleanup vì merge dưới concurrency tốn kém.

Do đó index có thể fragmented/bloated theo thời gian và maintenance policy phụ thuộc engine.

## Latch khác transaction lock

**Lock** bảo vệ logical database concurrency giữa transactions. **Latch** là synchronization ngắn hạn bảo vệ in-memory data structure như buffer/page/tree pointers trong lúc thread thao tác.

Một query có thể không conflict transaction-level nhưng vẫn tranh latch trên hot index page.

Phân biệt này quan trọng khi chẩn đoán wait events.

## Latch coupling / crabbing

Khi thread traverse tree và có thể modify, nó cần bảo đảm node không bị split/remove dưới chân.

Pattern conceptual: latch parent, latch child, khi child đã an toàn thì release parent. Với insert/delete, engine có protocol phức tạp hơn để biết khi nào cần giữ ancestor.

Mục tiêu là không latch toàn tree, vì như vậy concurrency collapse.

## Optimistic traversal

Read-heavy indexes có thể traverse với lightweight/version checks rồi retry nếu structure thay đổi, giảm exclusive latch contention.

Nhiều modern indexes dùng optimistic techniques, B-link tree sibling pointers hoặc versioned nodes để tăng concurrency.

Ý tưởng chung giống optimistic concurrency: cho phép tiến nhanh nếu không conflict, validate/retry khi phát hiện race.

## Hot root / hot leaf

Root được mọi lookup chạm nhưng thường read-mostly và nằm cache nên manageable. Rightmost leaf của monotonically increasing key có thể thành write hotspot.

Partitioning key, sequence allocation strategy hoặc index design có thể ảnh hưởng latch contention ngoài SQL-level lock contention.

## Covering index và page density

Thêm nhiều included columns giúp query tránh table lookup nhưng làm leaf entry lớn, giảm số entry/page và tăng tree/page footprint.

Đây là trade-off: read path ít hop hơn nhưng write cost/cache pressure cao hơn.

Index design vì vậy không thể chỉ hỏi “query có dùng index không?”. Phải hỏi entry size, write rate, selectivity, range pattern và maintenance.

## Mental Model

> B+Tree production là **một hierarchy của fixed-size pages dưới concurrency**, không phải cây node/pointer textbook. Split/merge là structural write; latch bảo vệ structure ngắn hạn; transaction lock bảo vệ logical isolation.

## Common Misconceptions

**“B+Tree index luôn chỉ 3 levels nên không cần quan tâm.”** Page size, key width và row count quyết định height/footprint.

**“Index càng nhiều columns càng tốt.”** Entry lớn làm write amplification và cache footprint tăng.

**“Lock wait và latch wait giống nhau.”** Chúng bảo vệ hai loại invariant khác nhau và cần cách chẩn đoán khác.

## Kết nối

Chapter tiếp theo trong roadmap là LSM tree để so write-optimized structure với B+Tree. Kết hợp chapter này với query optimizer foundation để hiểu vì sao cùng một logical index có cost khác mạnh tùy layout và workload.