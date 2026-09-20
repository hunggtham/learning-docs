# DSA trong cơ sở dữ liệu, mạng và hệ thống
**Data Structures & Algorithms in Real Systems / 실무 시스템 속의 자료구조와 알고리즘**

DSA trong hệ thống thực tế hiếm khi xuất hiện dưới nhãn “bài mảng”, “bài heap” hay “bài đồ thị”. Nó ẩn trong index cơ sở dữ liệu, buffer pool, cache, scheduler, routing table, filesystem, compiler, search engine, telemetry pipeline và runtime.

Điểm quan trọng là hệ thống thật gần như luôn **ghép nhiều cấu trúc dữ liệu**, rồi thêm persistence, concurrency, recovery và hardware-aware optimization lên trên phần lõi DSA.

Vì vậy mục tiêu của chương này không phải liệt kê “cấu trúc nào xuất hiện ở đâu”, mà là chỉ ra cách các bất biến và mô hình chi phí của DSA được chuyển thành quyết định kiến trúc.

## 1. B+Tree trong Database Index

Một database index cần:

```text
exact lookup
ordered lookup
lower/upper bound
range scan
insert/update/delete
```

Balanced BST trong RAM có `O(log n)` nhưng mỗi node thường chứa ít key và liên kết bằng pointer. Storage engine lại làm việc theo page/block, nên mục tiêu thật là giảm **số page I/O**.

B+Tree đặt nhiều key trong một page, tạo fan-out lớn và chiều cao rất nhỏ:

\[
height\approx \log_B n
\]

với `B` là số nhánh trên page.

Leaf còn thường liên kết tuần tự, nên range scan sau khi tìm lower bound có thể đọc nhiều page liền nhau.

Đây là ví dụ kinh điển cho việc cùng Big-O nhưng **mô hình chi phí I/O** làm thay đổi lựa chọn cấu trúc.

## 2. Clustered và Secondary Index

Nếu dữ liệu bản ghi được lưu gần theo thứ tự index, range scan có locality tốt hơn. Secondary index có thể chỉ lưu key + row identifier rồi phải truy cập bảng chính để lấy bản ghi đầy đủ.

Một query trả nhiều row có thể trở nên đắt vì nhiều random lookup tới dữ liệu chính.

Do đó cost model không chỉ có “index lookup `O(log n)`” mà còn gồm:

```text
số page của index
số row lookup
locality của table access
selectivity
covering index hay không
```

## 3. Composite Index và Lexicographic Order

Index `(a,b,c)` thường dùng thứ tự từ điển:

```text
so a trước
nếu a bằng nhau -> so b
nếu b bằng nhau -> so c
```

Điều này giải thích vì sao biết prefix trái của key làm vùng tìm kiếm liên tục hơn.

Không nên học “leftmost prefix rule” như mẹo riêng của SQL; nó xuất phát trực tiếp từ ordering invariant của tuple key.

## 4. Hash Index

Hash index phù hợp exact equality lookup nhưng không tự hỗ trợ range scan hoặc ordered iteration.

```sql
WHERE id = ?
```

là workload tự nhiên cho hashing.

```sql
WHERE price BETWEEN ? AND ?
ORDER BY price
```

cần order semantics, nên B+Tree thường phù hợp hơn.

Một index chỉ có giá trị nếu invariant của nó khớp predicate của query.

## 5. Hash Join

Hash Join thường:

1. build Hash Table trên input nhỏ hơn;
2. probe input còn lại bằng join key.

Expected complexity gần:

\[
O(n+m)
\]

nếu hash tốt và dữ liệu đủ nằm trong memory.

Nếu build side vượt memory, engine có thể partition dữ liệu và thực hiện nhiều pass qua disk. Khi đó external-memory cost trở thành phần quan trọng hơn Big-O RAM model.

## 6. Sort-Merge Join

Nếu hai input đã được sắp theo join key, có thể merge bằng hai con trỏ.

Nếu chưa có thứ tự, cần sorting trước.

Sort-Merge Join phù hợp khi:

```text
input đã ordered
join/range semantics phù hợp
external sorting có thể tận dụng sequential I/O
```

Một index có thứ tự có thể đồng thời phục vụ search, order-by và merge join. Đây là ví dụ một invariant được tái sử dụng cho nhiều operator.

## 7. Nested-Loop Join

Naive nested loop có thể `O(nm)`, nhưng nếu phía ngoài nhỏ và phía trong có index lookup rẻ:

```text
for each outer row:
    index lookup inner
```

thì chi phí thực có thể rất tốt.

Do đó tên “hai vòng lặp” không đủ để suy complexity; phải nhìn cost của inner operation.

## 8. Query Optimizer là bài toán Search

Một SQL query có nhiều:

```text
join order
access path
join algorithm
aggregation strategy
sort placement
```

Không gian plan có thể tăng rất nhanh.

Optimizer dùng dynamic programming, memoization, pruning và cost estimation để tìm plan tốt mà không enumerate toàn bộ không gian.

Database query optimization là DSA/search ở cấp hệ thống, không chỉ là rule-based rewriting.

## 9. Cardinality Estimation

Cost model phụ thuộc ước lượng số row trung gian. Nếu estimate sai lớn, optimizer có thể chọn Hash Join thay vì Nested Loop hoặc ngược lại theo cách rất tệ.

Histogram, samples và sketches là các cấu trúc tóm lược để ước lượng phân phối dữ liệu.

Đây là kết nối giữa probabilistic structures và query planning.

## 10. Buffer Pool

Database giữ page trong RAM để tránh I/O lặp lại.

Buffer manager cần:

```text
pageId -> frame lookup
replacement policy
pin/unpin
Dirty-page tracking
```

Exact lookup thường dùng Hash Table. Replacement có thể dùng Clock, LRU-like hoặc chính sách workload-aware.

Một buffer pool là composition giữa **identity lookup** và **replacement ordering/approximation**.

## 11. LRU, LFU và Admission Policy

LRU chỉ quan tâm recency. LFU quan tâm frequency. Real cache thường cần cả hai và còn phải đối phó với scan pollution.

TinyLFU-style designs có thể dùng frequency sketch để quyết định object mới có đáng được nhận vào cache không.

Một lesson quan trọng:

> eviction và admission là hai quyết định khác nhau.

Không phải mọi object vừa được đọc đều đáng đẩy object đang hot ra khỏi cache.

## 12. TTL và Expiration

Cache có TTL cần biết item nào hết hạn tiếp theo.

Một heap theo expiration time là cách tự nhiên nhưng delete/update tùy ý có thể tạo stale entry. Timer wheel hiệu quả hơn khi có rất nhiều timer và độ phân giải thời gian hữu hạn.

Structure phù hợp phụ thuộc:

```text
số timer
độ chính xác thời gian
update/cancel frequency
latency requirement
```

## 13. Write-Ahead Log

WAL là append-oriented structure: ghi log trước, sau đó cập nhật page/data structure.

Append tuần tự thường rẻ hơn random page update và cung cấp nền tảng recovery.

Ở đây DSA không thể tách khỏi durability: representation phải cho phép replay/redo sau crash.

## 14. LSM Tree

LSM Tree tối ưu write path bằng:

```text
WAL
mutable memtable
immutable sorted files
background compaction
```

Memtable có thể là Skip List hoặc tree có thứ tự. SSTable là immutable sorted run. Compaction là repeated multi-way merge.

Trade-off:

```text
write nhanh và sequential hơn
đổi lại read amplification + compaction cost
```

## 15. Bloom Filter trong LSM

Mỗi SSTable có thể kèm Bloom Filter.

Nếu filter nói “chắc chắn không có”, engine bỏ qua file. False positive chỉ tạo thêm một lần đọc; false negative sẽ phá correctness nên không được phép trong mô hình chuẩn.

Đây là ví dụ rất đẹp của approximate data structure được đặt trước exact storage để tối ưu I/O mà không làm sai kết quả cuối.

## 16. Compaction và Merge

Compaction đọc nhiều sorted runs rồi merge thành run mới.

Đây chính là external merge ở quy mô storage engine, nhưng còn thêm:

```text
tombstone
version
sequence number
snapshot visibility
```

Comparator không chỉ sắp user key mà có thể còn sắp theo version nội bộ.

## 17. MVCC và Versioned State

MVCC giữ nhiều version để reader thấy snapshot nhất quán trong khi writer tiếp tục cập nhật.

Conceptually đây là một dạng versioned/persistent state. Storage engine cần cấu trúc để tìm “version mới nhất nhìn thấy được theo snapshot”.

Bài toán không còn chỉ `key -> value`; key logic có thêm chiều thời gian/version.

## 18. Filesystem Directory và B-Tree/Hash

Filesystem phải ánh xạ tên file tới inode/metadata. Với directory lớn, linear list quá đắt; implementation có thể dùng hashing hoặc tree-indexed structures.

Extent tree biểu diễn các vùng block liên tiếp thay vì một entry cho từng block, nén representation bằng cách khai thác tính liên tục.

Đây là ví dụ của **run-length-like structural compression** trong storage metadata.

## 19. Free-Space Management

Allocator/filesystem cần theo dõi vùng trống.

Có thể dùng:

```text
bitmap
free list
buddy allocator
extent tree
size-segregated lists
```

Lựa chọn phụ thuộc loại query: tìm block bất kỳ, block đủ lớn, contiguous range, alignment, merge khi free.

## 20. Buddy Allocator

Buddy system chia block theo lũy thừa của hai. Khi free hai block “buddy” cùng size, có thể merge thành block lớn hơn.

Tìm buddy thường dùng XOR theo địa chỉ/index.

Trade-off là quản lý nhanh nhưng có internal fragmentation do làm tròn size.

Đây là một ứng dụng rất thực của power-of-two decomposition.

## 21. Networking: Routing là Graph Problem

Topology mạng là graph. Link-state protocol xây bản đồ topology và chạy shortest path kiểu Dijkstra. Distance-vector family có tinh thần Bellman–Ford relaxation giữa hàng xóm.

Nhưng protocol thật còn có:

```text
policy
convergence
hierarchy
failure recovery
loop prevention
```

Shortest-path algorithm chỉ là primitive toán học bên dưới.

## 22. Longest-Prefix Match

Router không chỉ hỏi exact key. Nó chọn route có prefix dài nhất khớp destination address.

Trie, Radix Tree hoặc Patricia Trie mã hóa prefix relationship trực tiếp.

Hardware có thể dùng TCAM hoặc specialized structure, nhưng requirement vẫn là prefix search.

## 23. Packet Classification

Firewall/router có thể phân loại theo nhiều trường:

```text
source/destination prefix
port range
protocol
```

Đây không còn là một trie một chiều đơn giản. Có thể cần decision tree, multi-dimensional indexing hoặc hardware-specific lookup.

Bài toán cho thấy khi key có nhiều chiều, một index đơn chiều có thể không còn đủ.

## 24. Packet Queue và Scheduling

FIFO là baseline. QoS có thể cần priority queue, weighted fair scheduling hoặc nhiều queue theo class.

Nếu luôn phục vụ priority cao nhất, traffic thấp priority có thể starvation. Scheduler phải duy trì thêm fairness state.

Data structure chọn “phần tử tiếp theo” chính là chính sách hệ thống.

## 25. Backpressure

Nếu producer nhanh hơn consumer trong thời gian dài, unbounded queue chỉ trì hoãn sự cố bằng cách tăng memory và latency.

Bounded queue buộc hệ thống chọn:

```text
block
reject
drop
spill
scale consumer
```

Queue capacity là một phần của reliability policy.

## 26. Consistent Hashing

Nếu mapping dùng `hash(key) mod N`, thay đổi `N` remap rất nhiều key.

Consistent hashing đặt node/key trên một vòng hash. Khi node thêm/bớt, chỉ một vùng keyspace gần vị trí thay đổi cần remap.

Virtual nodes giúp phân phối load đều hơn.

## 27. Rendezvous Hashing

Một lựa chọn khác là tính score cho mỗi `(key,node)` rồi chọn node score cao nhất.

Ưu điểm là không cần duy trì vòng; khi node set thay đổi, chỉ key có winner thay đổi mới remap.

Consistent hashing và rendezvous hashing đều giải bài **stable partitioning dưới membership change** nhưng bằng representation khác nhau.

## 28. Load Balancing và Power of Two Choices

Nếu chọn một server hoàn toàn ngẫu nhiên, load có thể lệch. Một kỹ thuật nổi tiếng là lấy hai candidate ngẫu nhiên rồi chọn server nhẹ hơn.

Một thay đổi nhỏ trong selection policy có thể cải thiện mạnh tail load distribution.

Đây là ví dụ randomized algorithm xuất hiện trực tiếp trong hệ thống phân tán.

## 29. Rate Limiter

Token Bucket có thể được xem như state nhỏ gồm số token và timestamp cập nhật cuối. Sliding-window exact limiter có thể cần queue timestamp; approximate limiter có thể dùng fixed buckets.

Cùng requirement “giới hạn request” có nhiều representation với trade-off precision/memory.

## 30. Scheduler của OS

Ready tasks có thể được tổ chức bằng queue, priority queue, tree theo virtual runtime hoặc nhiều queue theo priority.

Một scheduler tốt không chỉ tìm task priority cao nhất; nó còn phải cân bằng fairness, starvation, locality và preemption cost.

Data structure encode policy chọn task tiếp theo.

## 31. Timer Management

Hệ điều hành/runtime có hàng nghìn hoặc hàng triệu timer.

Min-heap cho timer sắp hết hạn nhưng update/cancel có cost `O(log n)`. Hierarchical timing wheel tận dụng time buckets để đạt cost gần hằng số với độ phân giải cố định.

Đây là ví dụ workload đặc biệt cho phép structure chuyên biệt vượt generic priority queue.

## 32. Git là DAG

Commit graph của Git là DAG. Merge commit có nhiều parent.

Các thao tác:

```text
ancestor check
merge-base
history traversal
reachability
```

đều là graph queries.

Generation number và commit-graph index giúp prune traversal. Bloom-filter-like metadata có thể giảm kiểm tra path history trong một số workflow.

## 33. Build System

Dependency graph phải acyclic nếu muốn một topological schedule hợp lệ.

Các target có dependency đã hoàn tất có thể được đưa vào ready queue và chạy song song.

Build system thực tế còn cache artifact theo content hash để tránh rebuild phần không thay đổi.

Ở đây DAG + hashing + memoization kết hợp thành incremental build engine.

## 34. Compiler: AST, Symbol Table và CFG

Parser tạo AST — một tree. Symbol table dùng Hash Map hoặc scope stack. Control Flow Graph là graph. Dominator tree và data-flow analysis dùng các thuật toán graph/bitset/fixpoint.

Compiler là ví dụ nơi gần như toàn bộ DSA core xuất hiện trong cùng một pipeline.

## 35. Garbage Collector

Tracing GC bắt đầu từ roots rồi đánh dấu mọi object reachable — bản chất là graph traversal.

Generational GC khai thác giả thuyết rằng object trẻ thường chết sớm, giảm vùng cần scan thường xuyên.

Remembered set/card table là cấu trúc phụ để không phải scan toàn heap khi tìm reference giữa các thế hệ.

## 36. Search Engine Inverted Index

Thay vì map document -> words, inverted index map term -> posting list document IDs.

Posting list được sắp xếp, cho phép giao nhiều danh sách bằng merge/two pointers hoặc skip data.

Dictionary term có thể dùng trie/FST. Ranking dùng heap cho Top-K. Cache và compression lại thêm các lớp structure khác.

## 37. Full-Text Index và Suffix/FM Structures

Suffix Array, FM-index hoặc inverted index phù hợp các kiểu search khác nhau.

Inverted index mạnh cho token/term queries. Suffix structures phù hợp substring/order-based queries. FM-index hỗ trợ compressed substring search.

Index phải khớp query semantics.

## 38. Observability và Sketches

Telemetry có cardinality cực lớn. Không thể luôn giữ exact set/counter cho mọi key.

HyperLogLog, Count-Min Sketch và heavy-hitter algorithms giúp giữ summary nhỏ.

Sketch có thể merge giữa worker nên rất phù hợp distributed aggregation.

## 39. Top-K trong Streaming

Nếu muốn giữ các metric lớn nhất liên tục, có thể dùng min-heap size `k`. Nếu keyspace quá lớn và muốn heavy hitters approximate, Count-Min Sketch + candidate heap là composition phổ biến.

Exact và approximate structure có thể phối hợp nhiều tầng.

## 40. Memory Allocator và Free List

Allocator có thể dùng size classes, bins, tree hoặc bitmap để tìm block phù hợp.

Một allocator tốt phải cân bằng:

```text
allocation latency
fragmentation
concurrency
cache locality
metadata overhead
```

Đây là data-structure selection dưới ràng buộc cực thấp cấp.

## 41. Lock-Free Structures

Lock-free stack/queue thường dùng atomic CAS. Nhưng correctness không chỉ nằm ở shape của stack/queue mà còn ở:

```text
memory ordering
ABA
safe reclamation
linearization point
```

Hazard pointer hoặc epoch reclamation là cấu trúc/phương thức quản lý lifetime đi kèm.

DSA concurrent là DSA + memory model.

## 42. Crash Consistency

Persistent data structure phải sống qua process crash, không chỉ qua function call.

Một update nhiều bước có thể để storage ở trạng thái nửa cũ nửa mới. WAL, copy-on-write hoặc shadow paging tạo protocol để có một commit point rõ ràng.

Đây là phiên bản persistence của transactional update invariant.

## 43. Merkle Tree

Merkle Tree hash mỗi node từ hash của các con. Root hash cam kết toàn bộ nội dung cây.

Ứng dụng:

```text
content verification
replication comparison
blockchain structures
versioned storage
```

Proof path chỉ cần `O(log n)` hash để chứng minh một leaf thuộc tree cân bằng.

## 44. Bloom Filter, Merkle Tree và Index giải các câu hỏi khác nhau

Bloom Filter: “chắc chắn không có hay có thể có?”.

Merkle Tree: “hai tập dữ liệu có cùng nội dung/nhánh này có thuộc snapshot không?”.

B+Tree: “key này nằm ở đâu, range này gồm gì?”.

Cả ba đều là metadata structures nhưng phục vụ semantic hoàn toàn khác.

## 45. Hệ thống thực tế tối ưu data movement

CPU operation thường rẻ hơn cache miss, page I/O hoặc network round trip nhiều bậc độ lớn.

Vì vậy data structure performance trong production thường bị chi phối bởi:

```text
bytes moved
cache lines touched
pages read
RPCs sent
allocations created
locks contended
```

Không nên dừng phân tích ở số comparison.

## 46. Một case study: Read Path của Key-Value Store

Có thể hình dung:

```text
request
 -> routing hash
 -> in-memory cache
 -> Bloom filters
 -> memtable / index lookup
 -> SSTable page read
 -> decompression
 -> value return
```

Mỗi tầng dùng structure khác để giảm chi phí tầng tiếp theo.

Câu hỏi kiến trúc là: **lọc càng sớm càng tốt bằng metadata rẻ hơn có đáng không?**

## 47. Một case study: Scheduler

Scheduler có:

```text
ready set
priority/fairness metadata
timer queue
CPU affinity state
```

Một heap duy nhất hiếm khi đủ. Có thể cần tree theo virtual runtime, queue theo class, bitmap để tìm priority có task và timer wheel cho wake-up.

Production DSA thường là composition theo nhiều query cùng lúc.

## 48. Từ DSA sang System Design

Khi nhìn một subsystem, hãy hỏi:

```text
state nào được giữ?
query nào hot nhất?
metadata nào đang được materialize?
update phải duy trì invariant nào?
chi phí thật là CPU, memory, I/O hay network?
điều gì xảy ra khi crash/concurrent update?
```

Đây là cùng workflow của DSA nhưng mở rộng sang hệ thống.

## 49. Những hiểu lầm phổ biến

“Database dùng B+Tree chỉ vì `O(log n)`” — bỏ qua page I/O và fan-out.

“Cache chỉ cần HashMap” — còn eviction, admission, TTL và concurrency.

“Routing chỉ là Dijkstra” — protocol còn policy/convergence/failure handling.

“GC tự quản bộ nhớ nên không liên quan DSA” — tracing chính là graph reachability.

“Distributed system không còn liên quan cấu trúc dữ liệu” — partitioning, queues, sketches, logs và indexes đều là DSA ở quy mô khác.

## Mô hình tư duy

> Trong hệ thống thực tế, DSA là cách **materialize đúng metadata để tránh công việc đắt hơn ở tầng dưới**.

B+Tree giữ order để tránh nhiều page I/O. Bloom Filter giữ dấu vết membership để tránh đọc file. Cache giữ dữ liệu hot để tránh backend access. Hash ring giữ partition metadata để hạn chế remapping. Timer wheel giữ bucket thời gian để tránh heap operation cho hàng triệu timer.

Khi gặp một subsystem, đừng chỉ hỏi “nó dùng data structure gì?”. Hãy hỏi: **query nào đang được tăng tốc, invariant nào phải trả giá để duy trì, và tầng tài nguyên đắt nhất đang được tránh là CPU, cache miss, disk I/O hay network round-trip?**

Xem thêm: [Choose the Right Data Structure](./00_choose_the_right_data_structure.md), [B/B+Tree](../02_trees/05_b_trees_and_external_memory.md), [Hash Tables](../01_linear_structures/04_hash_tables.md), [Probabilistic Data Structures](../05_specialized/06_probabilistic_data_structures.md), [Graph Algorithms](../03_graphs/_index.md).