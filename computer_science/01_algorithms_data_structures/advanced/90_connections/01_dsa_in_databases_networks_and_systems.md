# DSA trong Database, Networking và Systems
**실무 시스템 속의 자료구조와 알고리즘**

DSA trong production thường ẩn dưới abstraction lớn hơn.

## Database

B+Tree index phù hợp range query vì keys có order và leaves hỗ trợ scan tuần tự. Hash index phù hợp equality hơn range. Query optimizer lại là một search/optimization problem trên plan space.

## Cache

LRU cache dùng hash map `key -> node` để lookup expected `O(1)` và doubly linked list để giữ recency/move-to-front `O(1)`.

## Networking

Routing topology là graph. Dijkstra/Bellman-Ford families xuất hiện trong shortest-path reasoning. IP longest-prefix match liên quan trie/radix structures.

## Git

Commit history thường được reasoning như directed acyclic graph: commit có parent(s), merge commit có nhiều parents, ancestor traversal là graph traversal.

## Compiler

Source code được parse thành Abstract Syntax Tree. Optimization passes traverse/transform AST hoặc graph-like intermediate representation. Parser thường dựa trên stacks/automata.

## Search engines

Inverted index ánh `term -> postings list`. Query AND có thể intersect sorted postings lists bằng two pointers. Ranking thêm scoring layer phía trên structure retrieval.

## Operating systems

Schedulers quản lý ready tasks bằng queues/priority structures. Virtual memory dùng page tables. Filesystem metadata dùng tree/index structures.

## Mental Model

> Production systems liên tục dùng các invariant DSA: order, priority, reachability, indexing, locality, prefix, connectivity và aggregation. Tên implementation có thể khác nhưng idea nền vẫn vậy.

## Message queues và backpressure

Queue trong distributed system không chỉ FIFO container. Capacity hữu hạn tạo backpressure problem: producer nhanh hơn consumer thì queue length tăng không giới hạn. Ring buffer/bounded queue biến memory limit thành explicit policy: block, drop, spill hoặc reject.

DSA operation cost vì thế kết nối trực tiếp với reliability policy.

## Memory allocators

Allocator quản free blocks bằng segregated lists, trees, bitmaps hoặc buddy systems tùy design. Đây là DSA rất “thật”: structure lựa chọn quyết định fragmentation, allocation latency và locality.

## Database buffer pool và eviction

LRU chỉ là một policy; production databases có clock, LRU-K hoặc workload-aware variants. Nhưng primitive idea vẫn là kết hợp fast identity lookup với ordered/approximate recency metadata.

## Dependency resolution

Build systems và package managers tạo directed dependency graph. DAG cho phép topological scheduling; cycle là semantic error hoặc cần special handling. Parallel build còn cần scheduling ready nodes theo available workers/resources.

## Observability

Top-K heavy hitters, approximate counters, sketches và streaming structures xuất hiện trong metrics/logging vì giữ toàn bộ events không khả thi. Đây là nơi probabilistic data structures trở thành engineering tool chứ không chỉ academic topic.
