# DSA trong Database, Networking và Systems
**Data Structures & Algorithms in Real Systems / 실무 시스템 속의 자료구조와 알고리즘**

DSA trong production hiếm khi xuất hiện với nhãn “bài array”, “bài graph” hay “bài heap”. Nó thường ẩn bên dưới database index, scheduler, cache, routing table, compiler, search engine, filesystem hoặc observability pipeline. Khi nhận ra invariant và workload phía sau những abstraction này, ta thấy các cấu trúc học trong DSA không phải bài tập rời rạc mà là vocabulary để thiết kế hệ thống.

Điểm quan trọng là production systems hiếm khi dùng một cấu trúc duy nhất. Chúng thường **compose nhiều structures**, thêm persistence, concurrency, failure handling và hardware-aware optimization lên trên DSA core.

## 1. Database index: tại sao B+Tree chứ không phải một BST bình thường?

Một database cần exact lookup, ordered lookup, predecessor/successor và range scan. Balanced BST trên lý thuyết có `O(log n)` search, nhưng node-per-object với branching factor nhỏ không phù hợp storage hierarchy.

Disk/SSD và buffer pool làm việc theo pages/blocks. B+Tree tăng branching factor rất lớn: một page có thể chứa hàng trăm keys/pointers. Height vì thế rất thấp, giảm số page reads.

B+Tree còn giữ records hoặc record pointers chủ yếu ở leaves; leaves thường linked với nhau nên range scan sau khi tìm lower bound có thể đi tuần tự qua leaf pages.

Đây là ví dụ điển hình nơi Big-O giống nhau nhưng **I/O model** làm structure khác biệt hoàn toàn.

## 2. Hash index và ordered index phục vụ workload khác nhau

Hash index phù hợp exact equality lookup vì bucket được chọn từ hash. Nhưng hash không giữ global order, nên query kiểu:

```sql
WHERE price BETWEEN 100 AND 200
ORDER BY price
```

không được hỗ trợ tự nhiên như B+Tree.

Nếu workload chủ yếu `WHERE id = ?`, hash structure có thể rất hiệu quả. Nếu cần range, prefix/order hoặc index scan, ordered tree thường hữu ích hơn.

Bài học là index không chỉ là “tăng tốc query”; nó encode loại predicate nào có thể được prune hiệu quả.

## 3. Composite index và lexicographic order

Database composite index `(a,b,c)` thường giữ keys theo lexicographic order. Điều này giải thích left-prefix behavior: order đầu tiên theo `a`, trong cùng `a` mới theo `b`, rồi `c`.

Nếu query bỏ qua `a` nhưng chỉ filter `b`, index không còn cho một contiguous search region đơn giản như khi biết prefix key.

Đây chính là tree ordering invariant được áp dụng vào database design. Hiểu comparator/order giúp hiểu index access path tốt hơn việc học thuộc rule.

## 4. Query execution: hash join, sort-merge join và nested-loop join

Relational database chọn join algorithm theo data size, available indexes và memory.

**Hash Join** build hash table trên một input rồi probe input kia. Nó phù hợp equality join và thường gần `O(n+m)` expected nếu memory đủ.

**Sort-Merge Join** sort hai inputs theo join key rồi merge bằng two pointers. Nếu inputs đã ordered bởi index, sorting cost có thể giảm hoặc biến mất. Nó phù hợp khi ordering có giá trị hoặc range-like behavior.

**Nested Loop Join** có thể tốt nếu outer side nhỏ và inner lookup dùng index rất rẻ. Naive nested loops `O(nm)` không phản ánh đầy đủ case index-assisted.

Đây là data-structure selection ở cấp query engine.

## 5. Query optimizer là search trên plan space

Một SQL query có thể có nhiều join orders, access methods và physical operators. Optimizer phải tìm execution plan tốt trong một space có thể tăng combinatorially.

Dynamic programming, memoization và cost-based pruning được dùng để tránh enumerate mọi plan một cách ngây thơ. Statistics/histograms giúp estimate cardinality, từ đó estimate cost.

Vì vậy database query optimization kết nối DSA với dynamic programming và search, không chỉ với B+Tree.

## 6. Buffer pool và cache eviction

Database không đọc page từ disk mỗi query. Buffer pool cache pages trong RAM và cần eviction policy khi memory đầy.

LRU là mental model phổ biến: hash map `pageId -> node/frame` cho exact lookup, và ordered recency structure cho eviction. Nhưng production database có thể dùng Clock, LRU-K hoặc workload-aware policies để tránh scan pollution và giảm metadata overhead.

Underlying design vẫn là composition: **identity lookup + replacement ordering/approximation**.

## 7. Write path: WAL, memtable và LSM-tree

Không phải mọi database dùng B+Tree làm primary write structure. LSM-tree systems thường append write-ahead log, update một in-memory ordered structure như skip list/tree (memtable), rồi flush thành sorted immutable files.

Background compaction merge các sorted runs. Lookup phải kiểm tra multiple levels/files, nên Bloom filters và sparse indexes giúp tránh unnecessary reads.

LSM design thể hiện trade-off rất DSA: tối ưu sequential writes và batching, đổi lại read amplification/compaction complexity.

## 8. Cache: LRU chỉ là một composition pattern

Classic LRU cache dùng HashMap cho `O(1)` key lookup và doubly linked list cho `O(1)` move-to-front/remove-tail.

Nhưng một cache thật còn có TTL, size-based cost, frequency, concurrency và distributed invalidation. LFU cần frequency buckets; TinyLFU có thể dùng frequency sketch để estimate admission; TTL expiration có thể dùng heap hoặc timer wheel tùy scale.

Bài “implement LRU” chỉ là phiên bản tối giản của cache architecture.

## 9. Networking: graph ở cả control plane lẫn data plane

Network topology là graph. Routing protocols phải reason về path cost, reachability và topology changes.

Link-state protocols có thể xây topology map rồi chạy shortest-path algorithm kiểu Dijkstra. Distance-vector family liên quan Bellman-Ford-style relaxation: mỗi router trao đổi distance estimates với neighbors.

Tuy nhiên production routing còn có policy, convergence, hierarchical areas và failure recovery. DSA shortest path là core mathematical primitive, không phải toàn bộ protocol.

## 10. Longest Prefix Match và trie/radix tree

IP forwarding không hỏi exact equality đơn giản. Router cần tìm route có network prefix dài nhất match destination address.

Trie/patricia/radix structures phù hợp vì search đi theo bit prefix. Longest-prefix rule là trực tiếp một prefix-search problem.

Hardware routers có thể dùng TCAM hoặc specialized data structures, nhưng conceptual requirement vẫn là ordered/prefix matching.

## 11. Packet queues và scheduling

Network interface có packets chờ gửi. FIFO queue là baseline, nhưng QoS có thể yêu cầu priority queues, fair queuing hoặc weighted scheduling.

Nếu chỉ luôn gửi packet priority cao nhất, heap là natural abstraction. Nhưng fairness và latency guarantees có thể yêu cầu nhiều queues, virtual finish times hoặc hierarchical schedulers.

Một scheduler là bài toán chọn “item tiếp theo” dưới constraints, vì thế priority structures xuất hiện tự nhiên.

## 12. Message queues và backpressure

Trong distributed systems, queue không chỉ là container FIFO. Nếu producer nhanh hơn consumer, queue length có thể tăng mãi và cuối cùng gây out-of-memory hoặc disk explosion.

Bounded queue/ring buffer biến memory limit thành explicit policy. Khi full, hệ thống phải block producer, reject, drop, spill to disk hoặc scale consumer.

Ở đây capacity của data structure gắn trực tiếp với reliability semantics. DSA operation không thể tách khỏi system policy.

## 13. Consistent hashing và partitioning

Distributed cache/database cần map keys tới nodes. Hash modulo `N` đơn giản nhưng khi `N` đổi, rất nhiều keys remap.

Consistent hashing đặt nodes và keys trên một hash ring; khi thêm/bớt node, chỉ một phần keyspace gần node đó di chuyển. Virtual nodes giúp cân bằng load.

Đây là ví dụ hashing được dùng để giải distribution, không chỉ lookup trong một process.

## 14. Git commit graph

Git commit history là directed acyclic graph theo parent relation. Commit thường có một parent; merge commit có nhiều parents.

Operations như ancestor check, merge-base, history traversal và reachability đều là graph questions. Git còn dùng generation numbers, commit-graph indexes và Bloom-filter-like techniques trong một số paths để giảm traversal cost.

Mental model DAG giúp hiểu tại sao “history” không phải một linked list đơn giản.

## 15. Build systems và dependency graph

Build target phụ thuộc các target khác tạo DAG nếu configuration hợp lệ. Topological order cho biết thứ tự build hợp lệ.

Parallel build không cần chờ toàn graph theo một sequence duy nhất; bất kỳ node nào có indegree dependencies đã hoàn tất có thể đưa vào ready queue và chạy trên worker.

Nếu phát hiện cycle, đó thường là semantic error vì không thể có topological schedule hữu hạn theo dependency model.

## 16. Compiler: tree, graph, set và worklist

Parser biến source text thành syntax tree hoặc AST. Tree traversal dùng cho semantic analysis và transformation.

Compiler optimization hiện đại thường làm việc trên intermediate representation (IR) với control-flow graph (CFG). Basic blocks là vertices, possible jumps là edges. Dominator trees, liveness analysis và data-flow equations đều dựa trên graph/fixed-point algorithms.

Worklist algorithm dùng queue/deque để repeatedly process nodes whose information changed cho tới khi đạt fixed point.

Vì vậy compiler là một playground DSA rất giàu: stack, tree, graph, hash table, bitset, union-find và priority structures đều có thể xuất hiện.

## 17. Search engine: inverted index

Search engine không scan mọi document khi query một term. Nó dùng **inverted index**:

```text
term -> sorted postings list of document IDs / positions
```

Query `A AND B` có thể intersect hai sorted postings lists bằng two pointers. Nếu một list ngắn hơn nhiều, galloping/exponential search hoặc skip pointers có thể giảm work.

Phrase query còn cần positions trong document. Ranking như BM25 thêm score computation, còn top-K retrieval có thể dùng heap hoặc specialized pruning.

Data structure quyết định retrieval candidates; ranking quyết định thứ tự relevance phía trên.

## 18. Autocomplete và text indexing

Trie/radix tree cho prefix search. Nhưng production autocomplete còn cần ranking theo popularity, freshness, personalization và typo tolerance.

Một trie node có thể cache top suggestions; FST hoặc compressed trie giúp memory efficient hơn. Fuzzy matching có thể kết hợp edit distance automata hoặc search structures khác.

Again, textbook trie là core invariant chứ không phải full product.

## 19. Operating system scheduler

OS scheduler quản runnable tasks. Một basic conceptual scheduler có queue; priority scheduling có priority structure. Linux CFS historically dùng red-black tree để order runnable entities theo virtual runtime trong thiết kế cổ điển/đã phát triển qua thời gian.

Điểm cần học là scheduler cần operation insert task, remove task, choose next according to fairness metric. Data structure được chọn để những operation đó rẻ và invariant scheduling được giữ.

## 20. Timer management

Hệ thống có hàng nghìn/millions timers không thể scan toàn bộ mỗi tick. Min-heap hỗ trợ lấy timer sắp hết hạn nhất `O(log n)` update, nhưng timer wheels có thể phù hợp hơn khi time domain discretized và scale lớn.

Đây là một ví dụ hay cho việc heap không phải luôn “best priority queue”; workload distribution và required precision có thể tạo specialized structure tốt hơn.

## 21. Virtual memory và page tables

Virtual address phải map sang physical frame. Multi-level page table là tree-like indexing structure dựa trên bit fields của address. TLB lại là cache cho recent translations.

Một memory access vì thế đi qua hierarchy của indexing + caching. Hardware architecture và data structure gắn chặt nhau.

## 22. Filesystem trees và metadata indexes

Directory hierarchy nhìn như tree, nhưng filesystem implementation có thể dùng hash trees, B-trees hoặc extent trees cho metadata và file block mapping.

Large directory không thể luôn linear scan tên file. Extent structure compress contiguous block ranges thay vì lưu từng block riêng.

Tree abstraction ở API và physical index bên dưới có thể khác nhau.

## 23. Memory allocators

Allocator quản các free memory blocks. Có thể dùng segregated free lists theo size class, bitmaps, balanced trees hoặc buddy system.

Buddy allocator chia memory thành power-of-two blocks và cho phép split/merge buddies hiệu quả. Trade-off là internal fragmentation.

Một allocator cần cân bằng allocation latency, fragmentation, metadata overhead, locality và concurrency. Đây là data-structure design rất trực tiếp.

## 24. Observability và streaming algorithms

Metrics/log pipeline có thể nhận hàng triệu events mỗi giây. Không thể lưu toàn bộ để query mọi thứ chính xác.

Count-Min Sketch estimate frequency với bounded memory. HyperLogLog estimate cardinality. Bloom Filter trả lời approximate membership. Reservoir Sampling giữ representative sample từ stream dài không biết trước kích thước.

Top-K heavy hitters có thể kết hợp counters/sketches và heap.

Đây là nơi probabilistic data structures trở thành engineering tools vì memory và throughput quan trọng hơn exact answer tuyệt đối.

## 25. Rate limiter

Fixed-window counter có thể dùng simple counter keyed by user. Sliding-window exact limiter có thể cần deque/timestamps. Token bucket/leaky bucket dùng mathematical state thay vì giữ mọi request.

Representation khác nhau tạo accuracy, burst behavior và memory trade-off khác nhau.

Một bài “đếm request trong 60 giây” có thể là queue problem, prefix/time-bucket problem hoặc distributed counter problem tùy scale.

## 26. Distributed consensus log và ordered sequence

Consensus systems như Raft/Paxos reason về ordered logs, term/index, prefix agreement và replication state. Core algorithm không phải một DSA textbook đơn giản, nhưng arrays/log segments, maps, queues và prefix invariants là những primitive thực tế.

Điểm kết nối ở đây là invariant discipline: replicated state chỉ đúng khi prefix/order constraints được bảo toàn qua failures và retries.

## 27. Graph trong service dependencies và tracing

Microservice call relationships tạo dependency graph. Cycle có thể gây cascading behavior; critical path analysis trên trace là longest-path-like reasoning trong DAG nếu trace edges theo causal order.

Topological reasoning cũng xuất hiện trong deployment dependencies và workflow engines.

## 28. Geospatial systems

Spatial data không phù hợp một-dimensional BST đơn giản. R-tree family index bounding rectangles; KD-tree phù hợp một số nearest-neighbor workloads; geohash/S2-like hierarchical cell schemes map 2D geography sang hierarchical keys.

Đây là bài học rằng dimensionality và geometry quyết định representation.

## 29. DSA trong concurrency

Concurrent queue, lock-free stack, concurrent hash map hay skip list phải giữ structural invariants đồng thời dưới interleavings của threads.

Big-O đơn luồng không đủ. Memory ordering, contention, false sharing và progress guarantees trở thành một phần cost model.

Một theoretically optimal structure có thể scale kém nếu mọi threads tranh cùng lock/root node.

## 30. Từ textbook operation đến system workload

Khi gặp một subsystem production, hãy dịch requirement về operations.

Database index: exact lookup, lower bound, range scan, insert/delete.

Scheduler: insert task, update priority, extract next.

Cache: lookup, admission, recency/frequency update, eviction.

Router: longest-prefix lookup, route update.

Search: term lookup, postings intersection, top-K ranking.

Allocator: find fitting block, split, merge, free.

Khi operations đã rõ, DSA choices trở nên dễ lý giải hơn.

## Mental Model

> Production systems liên tục duy trì các invariant quen thuộc của DSA: **order, priority, reachability, locality, prefix, connectivity, aggregation và approximate summaries**.

Textbook DSA cung cấp primitive mental models. Systems engineering thêm storage hierarchy, concurrency, failures, persistence và workload distribution. Khi học sâu structure, luôn hỏi “operation này xuất hiện ở subsystem thật nào?”; khi học system, hỏi ngược lại “abstraction này đang dựa trên invariant DSA nào?”.

Xem thêm: [Chọn cấu trúc dữ liệu phù hợp](./00_choose_the_right_data_structure.md), [B-Trees & External Memory](../02_trees/05_b_trees_and_external_memory.md), [Probabilistic Data Structures](../05_specialized/06_probabilistic_data_structures.md), [Graph Algorithms](../03_graphs/00_graph_modeling_and_representation.md).