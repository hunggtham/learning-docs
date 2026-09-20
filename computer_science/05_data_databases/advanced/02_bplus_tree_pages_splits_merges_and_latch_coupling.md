# B+Tree page layout, splits/merges và latch coupling

B+Tree thường được giới thiệu như “balanced tree có O(log n)”. Điều đó đúng nhưng chưa giải thích vì sao database dùng nó. Điểm cốt lõi là B+Tree được thiết kế quanh **page/block I/O**: mỗi node chứa nhiều keys để một lần đọc page mang về lượng lớn routing information, giữ tree rất nông ngay cả khi có hàng triệu hoặc hàng tỷ rows.

## Node là page-oriented structure

Database page thường có fixed size. Một B+Tree page chứa header, slot metadata, keys và child pointers hoặc record references. Leaf page chứa entries theo key order; internal page chứa separator keys để chọn child.

Fan-out lớn làm height nhỏ. Nếu mỗi internal page trỏ được hàng trăm child, chỉ vài levels đã index được lượng dữ liệu rất lớn. Đây là khác biệt quan trọng so với binary search tree trong RAM.

## B+Tree khác B-Tree ở data placement

Trong B+Tree, internal nodes chủ yếu phục vụ routing; data entries tập trung ở leaves. Leaves thường được liên kết theo thứ tự để range scan đi tuần tự mà không quay lại root cho từng key.

Vì vậy cùng index có thể phục vụ cả point lookup và ordered range scan — một đặc tính rất phù hợp SQL `WHERE`, `ORDER BY`, prefix/range condition.

## Search đi qua buffer pool

Logical traversal root → internal → leaf không nhất thiết tạo disk I/O ở mỗi level. Hot root/internal pages thường nằm trong buffer pool. Leaf access mới có thể là phần random I/O đáng kể.

Do đó cost model phải kết hợp tree height với cache residency, page locality và storage device, không chỉ đếm comparison.

## Insert và page split

Khi leaf còn chỗ, insert đặt entry đúng vị trí. Khi page đầy, engine phải split: tạo page mới, phân phối entries và propagate separator key lên parent. Nếu parent cũng đầy, split có thể lan tới root và làm tree cao thêm một level.

Split không chỉ là thao tác cấu trúc. Nó tạo WAL records, dirty pages, latch coordination và có thể ảnh hưởng concurrent readers/writers.

Sequential insert thường tập trung vào rightmost leaf; random insert phân tán hơn nhưng có thể gây fragmentation. Fill factor là một cách chủ động để chừa headroom cho future inserts, đổi storage density lấy ít split hơn.

## Delete và merge

Textbook tree thường merge/redistribute khi node quá rỗng để giữ occupancy bound. Database engine thực tế có thể trì hoãn hoặc tối ưu cleanup vì merge cũng tốn write amplification và synchronization. “Balanced” trong production không nhất thiết có nghĩa mọi page luôn đạt occupancy lý tưởng sau từng delete.

Vacuum/compaction/rebuild policy tùy engine và storage model.

## Latch khác transaction lock

**Lock** bảo vệ logical database state giữa transactions; **latch** bảo vệ in-memory data structure trong thời gian rất ngắn khi threads cùng sửa page/tree metadata.

Một transaction có thể giữ row lock hàng giây, nhưng latch trên buffer/page thường chỉ giữ trong critical section rất ngắn. Trộn hai khái niệm này dẫn đến hiểu sai database contention.

## Latch coupling

Trong traversal concurrent, thread có thể giữ latch parent, acquire latch child rồi release parent khi đã chắc child ổn định cho operation. Pattern này thường gọi **latch coupling/crabbing**.

Insert/split khó hơn read vì structure có thể thay đổi. Engine hiện đại dùng nhiều optimization để tránh giữ latch từ root xuống leaf quá lâu, nhưng invariant chung là traversal phải không nhìn thấy tree ở trạng thái cấu trúc bất hợp lệ.

## Composite index và physical order

Index `(a, b)` được sắp lexicographically: trước theo `a`, trong cùng `a` theo `b`. Vì vậy query chỉ theo `b` thường không có một contiguous range dễ seek như query theo `a` hoặc `(a,b)`.

“Leftmost prefix” không phải rule để học thuộc; nó xuất phát từ ordering vật lý của key trong leaves.

## Covering index

Nếu index chứa đủ columns để trả query, engine có thể tránh lookup về base table/heap. Điều này giảm random access nhưng index lớn hơn, fan-out giảm, write cost tăng và cache footprint lớn hơn.

Index design vì thế là trade-off read path ↔ write amplification ↔ storage ↔ cache.

## Mental model

> B+Tree là ordered, page-oriented search structure. Sức mạnh của nó đến từ fan-out lớn, shallow height và ordered leaves. Production behavior được quyết định không chỉ bởi O(log n), mà bởi page layout, buffer pool, split/merge, WAL và concurrent latching.