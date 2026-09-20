# B-Tree, B+Tree và cấu trúc dữ liệu cho External Memory
**B-Tree / B+Tree / B 트리와 외부 메모리 자료구조**

B-Tree xuất hiện khi cost model của BST trong RAM không còn phù hợp. Một binary search tree giả định truy cập child pointer tương đối rẻ; nhưng khi node nằm trên SSD, HDD, database page hoặc storage block, chi phí lớn thường không phải vài phép so sánh mà là **I/O / 입출력**.

Vì vậy mục tiêu đổi từ “giảm số comparison” sang:

```text
mỗi lần đọc storage block phải mang về nhiều information hữu ích
số tầng của tree phải thật thấp
các node nên khớp page/block size của storage system
```

Đây là ví dụ kinh điển cho một nguyên tắc rộng hơn của DSA: cấu trúc dữ liệu tốt phụ thuộc **cost model của hardware và workload**, không chỉ Big-O trên RAM model trừu tượng.

## Vì sao binary tree không lý tưởng cho disk/page storage?

Binary tree có fan-out tối đa 2. Nếu có hàng triệu keys, height vẫn khoảng `log2(n)` dù balanced. Trong RAM, khoảng vài chục pointer dereference có thể chấp nhận được. Nhưng nếu mỗi level tương ứng một random page read, latency trở nên rất đắt.

B-tree tăng **branching factor / 분기 계수**. Một node có thể chứa hàng chục, hàng trăm hoặc hàng nghìn separator keys tùy page size và key width.

Ví dụ:

```text
[ 10 | 20 | 35 | 48 ]
 /     |     |     |     \
<10 10..20 20..35 35..48 >48
```

Một page read đưa về nhiều separators cùng lúc, cho phép chọn trong rất nhiều children. Nếu effective branching factor là `B`, height xấp xỉ:

\[
O(\log_B n)
\]

Sự khác biệt giữa `log2(n)` và `log200(n)` cực lớn khi mỗi level là một I/O.

## Node như một page-sized search structure

Một B-tree node thường chứa:

```text
sorted keys
child pointers/page ids
metadata cần thiết
```

Keys trong node được sorted. Ta có thể dùng linear search, binary search hoặc SIMD-friendly search tùy node size/hardware. Nhưng ngay cả nếu phải làm thêm vài chục comparisons trong memory, điều đó vẫn thường rẻ hơn một storage I/O bổ sung.

Do đó B-tree chủ động “làm nhiều việc trong một node” để giảm height.

## B-tree invariant

Có nhiều cách định nghĩa theo order/minimum degree, nhưng tinh thần giống nhau:

```text
keys trong mỗi node sorted
children partition key space theo separators
mọi leaves ở cùng depth
node không được quá đầy
node không-root không được quá rỗng
```

Nếu minimum degree là `t`, một formulation điển hình cho B-tree là:

```text
mỗi non-root node có ít nhất t-1 keys
mỗi node có nhiều nhất 2t-1 keys
internal node có #children = #keys + 1
```

Exact convention khác nhau giữa sách và implementation. Khi đọc code, đừng học thuộc số trước; hãy xác định rõ “max keys”, “min keys”, “split threshold” mà implementation dùng.

## Search

Search trong B-tree gồm hai lớp:

```text
1. search key position trong node hiện tại
2. nếu chưa thấy, chọn đúng child interval và đi xuống
```

Pseudo-code:

```text
node = root
while node exists:
    i = first position where key <= keys[i]
    if keys[i] == key:
        return found
    if node is leaf:
        return not found
    node = child[i]
```

Số page accesses là `O(height)`, trong khi comparison count trong page có thể lớn hơn nhưng rẻ hơn nhiều.

## Insert: overflow và split

Insert thường đi xuống leaf như search. Vấn đề là leaf có thể đã full.

Một strategy phổ biến là **split full child trước khi descend**. Full node được chia thành hai nodes và median separator được đẩy lên parent.

Ví dụ conceptual:

```text
[ 10 | 20 | 30 | 40 | 50 ]
             ^ median

split ->

[10 | 20]   30   [40 | 50]
```

Nếu parent cũng full, split có thể propagate lên trên. Nếu root full, root split và tree tăng height đúng 1.

Điểm quan trọng là split không phá sorted partition invariant. Median trở thành separator giữa left range và right range.

## Tại sao B-tree luôn balanced theo depth?

Insert chỉ split nodes; nó không thêm một leaf sâu hơn riêng lẻ. Khi root split, toàn bộ tree tăng depth đồng đều vì root mới nằm trên root cũ/sibling mới. Do đó mọi leaves vẫn cùng depth.

Đây là khác biệt lớn với raw BST, nơi insertion order có thể làm một branch dài hơn rất nhiều branch khác.

## Delete khó hơn insert

Delete phải tránh underflow. Sau khi xóa key, node non-root không được ít hơn minimum occupancy.

Các thao tác chính là:

```text
borrow/rotate key từ sibling qua parent
merge với sibling khi cả hai đều quá ít keys
replace internal key bằng predecessor/successor rồi delete ở subtree
```

### Borrow từ sibling

Nếu child cần đi xuống đang ở minimum occupancy nhưng sibling có dư key, parent separator và sibling key có thể rotate để child nhận thêm một key.

### Merge

Nếu cả child và sibling đều minimum, ta kéo separator từ parent xuống và merge hai nodes thành một node lớn hơn. Parent mất một key và một child pointer.

Nếu root cuối cùng không còn key và chỉ có một child, child đó trở thành root, làm height giảm 1.

Mental model của delete là: **trước khi đi xuống, đảm bảo child có đủ “room” để mất một key mà không vi phạm lower occupancy bound**.

## B+Tree khác B-tree ở đâu?

Trong **B+Tree / B+ 트리**, internal nodes chủ yếu giữ separator keys để routing; actual records hoặc row pointers nằm ở leaves. Leaves thường được linked theo sorted order.

Conceptual structure:

```text
            [20 | 50]
           /    |    \
      ...      ...      ...
       |        |        |
 leaf <-> leaf <-> leaf <-> leaf
```

Điều này có nhiều lợi ích.

Internal nodes nhỏ hơn vì không cần chứa full records, nên fan-out lớn hơn và height thấp hơn.

Range scan rất tự nhiên: tìm leaf đầu tiên qua tree search rồi scan leaf links tuần tự.

Đây là lý do B+Tree đặc biệt phù hợp database indexes.

## Equality lookup và range scan có cost khác nhau

Equality query:

```sql
WHERE id = :id
```

có thể đi root → internal → leaf rồi dừng.

Range query:

```sql
WHERE created_at >= :from
  AND created_at < :to
```

thường cần:

```text
1. seek tới leaf đầu bằng tree traversal
2. scan tuần tự các leaf entries tiếp theo
```

Cost vì thế gần:

```text
seek cost + number of leaf pages scanned
```

Đây là lý do range selectivity ảnh hưởng query plan. Index không biến một query trả 80% table thành miễn phí; sau khi seek, vẫn phải đọc rất nhiều records/pages.

## Clustered index và secondary index

Database engine cụ thể có semantics khác nhau, nhưng một mental model hữu ích là:

**Clustered index / 클러스터형 인덱스** ảnh hưởng cách rows/data pages được tổ chức theo key chính hoặc tương đương.

**Secondary index / 보조 인덱스** thường chứa secondary key cộng locator tới record/primary key.

Một secondary lookup có thể cần:

```text
secondary B+Tree lookup
→ lấy row locator / primary key
→ thêm lookup tới clustered data
```

Vì vậy một “index hit” không nhất thiết chỉ có một tree traversal.

## Composite index và lexicographic order

Index trên `(a, b, c)` thường sắp theo lexicographic order:

```text
(a1,b1,c1) < (a2,b2,c2)
```

nếu `a1<a2`, hoặc `a1==a2` và `b1<b2`, v.v.

Điều này giải thích **left-prefix behavior** trong nhiều database indexes. Query có condition mạnh trên leading columns thường tận dụng contiguous range tốt hơn query chỉ filter column phía sau.

Ví dụ index `(country, city, created_at)` tự nhiên hỗ trợ:

```text
country = 'KR'
country = 'KR' AND city = 'Seoul'
country = 'KR' AND city = 'Seoul' AND created_at range
```

nhưng `city = 'Seoul'` một mình không nhất thiết tạo một contiguous interval nhỏ trong global index order.

## Covering index

Nếu query cần các columns đã có đủ trong index leaf, database có thể tránh fetch full row/page bổ sung. Đây là **covering index** idea.

Trade-off là index rộng hơn:

```text
fan-out giảm
storage tăng
write amplification tăng
cache residency có thể xấu hơn
```

Tối ưu index là balancing giữa read path và write/storage cost.

## Page split và write amplification

Insert vào leaf full có thể gây split. Split tạo page mới, di chuyển entries, update parent và có thể cascade.

Trong database thực, còn có logging, locking/latching, WAL và buffer pool interactions. Vì vậy insert vào B+Tree không chỉ là vài pointer assignments như BST trong RAM.

Random inserts vào clustered key có thể gây split rải rác. Monotonic increasing key thường append vào rightmost leaves, giảm random split pattern nhưng có thể tạo contention hotspot trong concurrent workloads.

## Fill factor và occupancy

Nếu pages luôn được đóng gói 100%, insert tương lai dễ split. Một số systems cho phép **fill factor / 채움 비율** để chủ động để trống space trong leaf pages.

Đây là trade-off:

```text
lower fill factor -> nhiều storage hơn nhưng có room cho future inserts
higher fill factor -> compact hơn nhưng split risk cao hơn
```

Không có một fill factor tối ưu cho mọi workload.

## Buffer pool và effective cost model

Không phải mọi page access đều ra disk. Database buffer pool/cache có thể giữ root và upper internal levels gần như luôn trong RAM.

Do đó thực tế:

```text
root/internal top levels rất hot
leaf/data pages quyết định nhiều cache misses hơn
```

B+Tree vẫn tốt vì shallow structure và page locality giúp cache hierarchy hiệu quả.

## Sequential scan vs index scan

Nếu query cần phần lớn table, sequential scan có thể tốt hơn đi index rồi random-fetch rất nhiều rows.

Đây là một lesson quan trọng: index structure mạnh không có nghĩa optimizer phải luôn dùng index.

Query planner so sánh cost:

```text
index seek + random/page lookups
vs
sequential scan
```

DSA chỉ cung cấp primitive; system-level decision còn phụ thuộc data distribution và I/O pattern.

## Hash index vs B+Tree

Hash structure mạnh với equality lookup:

```text
key = X
```

nhưng không giữ total order tự nhiên. Vì vậy range, prefix-order traversal, predecessor/successor, MIN/MAX hoặc ORDER BY thường hợp hơn với B+Tree.

B+Tree trả thêm `log_B n` navigation cost để đổi lấy ordered semantics.

## External-memory complexity

Trong **external memory model / 외부 메모리 모델**, ta quan tâm số block transfers hơn số primitive operations.

Nếu block chứa `B` keys, một search tree có fan-out lớn có thể đạt số I/O gần logarithmic theo base `B`.

Sorting, scanning, joins và graph processing cũng có external-memory variants tối ưu block transfer. Đây mở rộng Big-O truyền thống sang một model gần phần cứng hơn.

## B-Tree vs LSM Tree

Write-heavy storage engines thường dùng **Log-Structured Merge Tree (LSM Tree / 로그 구조 병합 트리)** hoặc hybrid designs.

B+Tree thường update pages in-place/logically in-place, thích hợp reads/range và balanced mixed workloads.

LSM gom writes thành sequential structures rồi merge/compact theo levels. Nó đổi read amplification/compaction cost để đạt write throughput cao.

So sánh mental model:

```text
B+Tree: giữ sorted structure online, update đúng vị trí
LSM: buffer/append writes, rồi merge sorted runs về sau
```

Không có structure “tốt hơn tuyệt đối”; workload quyết định.

## Cache-aware và cache-oblivious thinking

B-tree là cache-aware ở mức ta thường thiết kế node phù hợp page/block size cụ thể.

**Cache-oblivious algorithms / 캐시 비인지 알고리즘** cố đạt locality tốt qua layout/recursive decomposition mà không hard-code block size. Ví dụ van Emde Boas layout cho tree có thể cải thiện hierarchy locality.

Ý tưởng tổng quát: data structure performance có thể phụ thuộc cách bytes được bố trí trên memory hierarchy, không chỉ topology logic.

## Concurrency và latch coupling

Database B+Tree concurrent cần bảo vệ node/page trong khi traversal và split/merge. Một technique family là latch coupling/crabbing: giữ latch parent khi acquire child, sau đó release khi safe.

Modern engines có nhiều optimization phức tạp hơn, nhưng key insight là balancing operation như split không còn thuần local khi nhiều threads cùng modify tree.

Concurrency thêm các câu hỏi:

```text
reader thấy state nào trong lúc split?
separator update có atomic không?
lock/latch order có gây deadlock không?
```

Logical tree invariant và concurrency invariant phải cùng đúng.

## Prefix compression và key compression

Internal separator keys có thể dài. Database/index implementations đôi khi compress prefixes hoặc store minimal distinguishing separators để tăng fan-out.

Ví dụ nhiều URLs có common prefix lớn; storing full strings trong mọi internal entry lãng phí page space.

Compression tăng CPU work nhưng giảm page size/I/O — lại là một hardware-cost trade-off.

## Variable-length records

Nếu keys/records variable-length, “node chứa tối đa K keys” không còn fixed đơn giản. Occupancy thường được đo bằng bytes, slot directory hoặc free-space layout.

Do đó textbook B-tree với fixed number keys chỉ là conceptual core; production pages còn có slot arrays, fragmentation và compaction.

## Common misconceptions

“B-tree là binary tree nâng cấp” là sai; chữ B không nghĩa binary và branching factor thường lớn hơn rất nhiều.

“B+Tree leaf linked chỉ để tiện implementation” là sai; leaf chaining trực tiếp hỗ trợ efficient range scan.

“Index luôn làm query nhanh hơn” là sai; low-selectivity query hoặc heavy writes có thể khiến index không đáng dùng.

“B-tree search O(log n) nên giống BST” bỏ qua mục tiêu thực sự: base của logarithm/fan-out và số I/O mới là phần quan trọng.

“Page split chỉ tốn O(1)” đúng ở abstraction local nhưng production cost còn bao gồm logging, cache, locks và possible cascade.

## Testing B-tree implementations

Một validator tốt nên kiểm tra sau random inserts/deletes:

```text
keys trong node sorted
child count đúng quan hệ với key count
non-root occupancy nằm trong bounds
mọi leaves có cùng depth
mọi child key range khớp separators
search tất cả inserted keys đúng
inorder/leaf scan sorted
```

Delete là nơi dễ bug nhất; randomized differential testing với `TreeMap`/sorted reference model rất hữu ích.

## Mental Model

> B-tree/B+Tree không tối ưu chủ yếu cho số comparisons; chúng tối ưu cho **memory hierarchy và I/O**. Một node được làm rộng để một page read phân biệt nhiều ranges, khiến tree rất thấp. B+Tree còn tách routing khỏi records và nối leaves để range scan trở thành sequential access.

Khi đánh giá một index/storage tree, hãy hỏi:

```text
Node/page size là bao nhiêu?
Fan-out thực tế là bao nhiêu?
Workload equality hay range?
Read/write ratio thế nào?
Key có monotonic hay random?
Index có cover query không?
Buffer pool giữ được bao nhiêu level?
Page split/merge và write amplification có đáng kể không?
Concurrency cần latch/lock semantics nào?
```

Từ đó B+Tree trở thành bridge tự nhiên giữa DSA, database internals, storage engines và systems performance.

Xem thêm: [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md), [Balanced Search Trees](./02_balanced_search_trees.md), [DSA trong Database & Systems](../90_connections/01_dsa_in_databases_networks_and_systems.md).