# DSA như một bài toán mô hình hóa
**Cấu trúc dữ liệu và thuật toán (Data Structures & Algorithms / 자료구조와 알고리즘)**

DSA thường được học bằng tên cấu trúc và tên thuật toán: array, linked list, hash table, tree, graph, BFS, DFS, Dijkstra, dynamic programming. Cách học đó hữu ích để nhận diện pattern, nhưng chưa đủ để giải quyết bài toán mới. Nền tảng sâu hơn là khả năng biến một vấn đề thực tế thành một **mô hình trạng thái (state model / 상태 모델)** có operations rõ ràng, invariants rõ ràng và cost model đủ chính xác để chọn representation phù hợp.

Một chương trình có thể nhìn như hai thành phần lớn: **state** và **transformation**. State là thông tin hệ thống đang giữ; transformation là cách state thay đổi khi có input, query hoặc event mới. Data structure quyết định shape của state và thông tin nào được giữ sẵn. Algorithm quyết định chuỗi transformations dùng để đi từ input tới output. Performance không đến từ “thuật toán hay” một cách cô lập, mà từ sự phù hợp giữa representation, operations và workload.

## Bắt đầu từ câu hỏi chứ không bắt đầu từ cấu trúc dữ liệu

Giả sử một hệ thống có một triệu tài khoản. Nếu operation chính là “tìm account theo id”, quét list từ đầu tới cuối là representation kém phù hợp. Hash table đổi thêm memory, hashing và collision handling để lấy expected lookup gần `O(1)`. Nếu ngoài lookup còn cần `floor/ceiling`, range query hoặc iteration theo thứ tự id, balanced search tree lại phù hợp hơn vì order là một phần của invariant.

Điểm quan trọng là không nên hỏi trước “dùng HashMap hay TreeMap?”, mà nên hỏi:

```text
Hệ thống cần trả lời câu hỏi nào?
Các operations nào xảy ra thường xuyên nhất?
Latency hay throughput quan trọng hơn?
Có cần ordered output không?
Dữ liệu có update thường xuyên không?
Có giới hạn memory không?
Có cần deterministic worst-case guarantee không?
```

Các câu hỏi đó tạo ra **workload model / 작업 부하 모델**. Data structure chỉ có ý nghĩa trong workload.

## Từ nghiệp vụ sang operations

Một bài toán nghiệp vụ nên được chuyển thành các operations cụ thể. Ví dụ hệ thống chat có thể cần:

```text
append(message)
getRecent(k)
findById(id)
delete(id)
searchByTime(from, to)
```

Nếu 95% traffic là `append` và `getRecent`, việc tối ưu một operation hiếm như arbitrary deletion bằng một representation phức tạp có thể là quyết định sai. Ta có thể hình dung expected cost:

\[
E[C] = \sum_i p_i C_i
\]

trong đó `p_i` là tần suất tương đối của operation và `C_i` là cost của operation đó. Đây không phải công thức bắt buộc phải tính bằng số trong mọi dự án, mà là cách ép mình suy nghĩ về performance theo workload thay vì theo tên thuật toán.

## ADT trước implementation

**Kiểu dữ liệu trừu tượng (Abstract Data Type, ADT / 추상 자료형)** mô tả behavior và contract, chưa khóa representation.

Stack ADT cam kết LIFO với các operations như `push`, `pop`, `peek`. Nó có thể được implement bằng dynamic array, linked list hoặc một vùng stack memory chuyên dụng. Queue ADT cam kết FIFO; implementation có thể là ring buffer, linked list, deque hoặc persistent queue.

Tách ADT và implementation rất quan trọng vì hai implementation có thể có cùng semantics nhưng cost model hoàn toàn khác. Ví dụ `List` là abstraction, nhưng array-backed list và linked list không tương đương về locality, random access, allocation overhead hay iterator invalidation.

Trong Java, `Deque<E>` là abstraction; `ArrayDeque<E>` là implementation. Trong C, ADT thường được thể hiện bằng `struct` + API functions + ownership contract. Trong JavaScript, `Array` có thể cung cấp stack semantics qua `push/pop`, nhưng runtime representation và performance characteristics không giống C array.

## Representation là một quyết định về thông tin nào được lưu sẵn

Mỗi representation trả chi phí trước để một nhóm queries nào đó rẻ hơn sau này.

Sorted array giữ toàn bộ order. Nhờ đó binary search là `O(log n)`, nhưng middle insertion có thể `O(n)` vì phải dịch elements. Hash table không giữ order nhưng giữ bucket location theo hash để equality lookup expected `O(1)`. Heap không giữ full sorted order; nó chỉ giữ đủ partial order để extreme element luôn ở root. Segment tree lưu aggregates của canonical ranges để range query/update nhanh. Trie lưu prefix structure để prefix queries không phải so sánh toàn string với toàn collection.

Có thể xem data structure như **materialized information**: ta chủ động lưu một số relationship hoặc summary để không phải tính lại từ đầu khi query tới.

## Representation → invariant → operations → cost

Mọi data structure có một hoặc nhiều **bất biến (Invariant / 불변식)**. Min-heap giữ `parent <= children`. BST giữ left keys nhỏ hơn và right keys lớn hơn theo comparator. Disjoint Set Union giữ forest parent structure đại diện components. B+Tree giữ keys sorted trong page, occupancy constraints và leaves cùng depth.

Chuỗi reasoning tốt là:

```text
representation
    ↓
invariant
    ↓
operations được hỗ trợ
    ↓
complexity
    ↓
trade-offs và failure modes
```

Ví dụ binary heap dùng array representation + complete-tree shape + heap-order invariant. Complete-tree shape cho phép parent/children tính bằng index và giữ height `O(log n)`. Heap-order invariant cho `peek-min` `O(1)` và `insert/extract` `O(log n)`, nhưng không đủ để arbitrary search nhanh. Nếu ta đòi heap hỗ trợ mọi query như balanced BST thì ta đang yêu cầu sai abstraction.

## State phải chứa đủ thông tin để tương lai được xác định

Mô hình state sai là một trong những nguyên nhân lớn nhất khiến thuật toán “đúng code nhưng sai bài”.

Ví dụ shortest path trên grid có keys và doors. Nếu state chỉ là `(row, col)`, hai lần đứng ở cùng cell nhưng có bộ keys khác nhau bị coi là giống nhau, trong khi future actions khác nhau. State đúng có thể là `(row, col, keyMask)`.

Ngược lại, state quá chi tiết làm search space phình không cần thiết. Nếu history đầy đủ không ảnh hưởng future ngoài một summary nhỏ, ta nên compress state. Đây chính là tư tưởng đứng sau Dynamic Programming: nhiều histories được gom vào cùng state vì từ điểm đó future của chúng tương đương.

Một câu hỏi mạnh khi thiết kế state là:

> Hai histories khác nhau có thể được xem là cùng một state nếu mọi quyết định tương lai hợp lệ và mọi cost tương lai từ hai histories đó là tương đương hay không?

## Graph modeling: entity graph và state graph

Graph là ví dụ rõ nhất cho sức mạnh của modeling. Trong social network, node có thể là user và edge là friendship. Trong compiler, node có thể là module và edge là dependency. Trong shortest-path puzzle, node không nhất thiết là entity thật; node có thể là **state**.

Nếu một bài flight có giới hạn “tối đa K chặng”, state chỉ là airport có thể không đủ. Một model đúng có thể là `(airport, flightsUsed)`. Nếu cost thay đổi theo time slot, state có thể phải thêm time dimension. Đây gọi là **state-space graph / 상태 공간 그래프**.

Algorithm tốt trên graph model sai vẫn trả lời sai problem thật. Vì vậy modeling luôn đứng trước algorithm selection.

## Constraints là một phần của problem definition

Cùng một câu hỏi nhưng constraint khác có thể đổi hoàn toàn algorithm.

Shortest path với unweighted graph dùng BFS. Edge weights chỉ `0/1` cho phép 0–1 BFS. Non-negative weights phù hợp Dijkstra. DAG cho phép topological relaxation ngay cả khi có negative edges. Có negative cycle reachable thì “shortest path” tới một số nodes không còn finite minimum.

Tương tự, exact subset problem với `n=20` có thể brute-force `2^n`; với `n=60`, meet-in-the-middle có thể hợp; với `n=200000`, phải khai thác structure khác. Constraint không phải phụ lục cuối đề bài; nó là tín hiệu algorithmic quan trọng.

## Correctness model trước performance model

Một representation chỉ hữu ích nếu operations giữ invariant và semantics đúng. Không nên tối ưu trước khi xác định rõ precondition/postcondition.

Ví dụ cache LRU thường dùng hash map + doubly linked list. Hash map giúp lookup `O(1)` expected; linked list giữ recency order. Nhưng nếu update recency không được thực hiện khi `get`, cache có thể vẫn chạy nhanh nhưng semantics không còn là LRU.

DSA production thường là composition nhiều structures. Correctness của composition phụ thuộc cross-structure invariant, ví dụ:

```text
mỗi key trong map trỏ đúng node trong list
mỗi node trong list có đúng một map entry
head/tail phản ánh recency order
size map == size list
```

## Time complexity chỉ là một cost model

Big-O thường đếm primitive operations trong mô hình RAM lý tưởng. Nhưng hardware/runtime thực có cache hierarchy, branch prediction, allocation, GC, page I/O, network latency và concurrency coordination.

Array traversal và linked-list traversal đều `O(n)`, nhưng array thường tốt hơn nhiều về cache locality. Hash table expected `O(1)` có thể có constant factor lớn nếu entries object-heavy, hash function tốn kém hoặc load factor cao. B+Tree có thể làm nhiều comparisons hơn binary tree trong mỗi node nhưng giảm số page I/O nhờ fan-out lớn.

Vì vậy nên reasoning ở ít nhất hai tầng:

```text
asymptotic model: growth theo input size
machine/runtime model: data movement, allocation, cache, I/O, GC, contention
```

Trong storage systems, số I/O có thể quan trọng hơn số comparisons. Trong distributed systems, một network round-trip có thể đắt hơn hàng nghìn operations local. Trong managed runtime, allocation/GC pattern có thể quyết định latency tail.

## Space không chỉ là Big-O memory

Hai structures cùng `O(n)` memory nhưng overhead rất khác. Array of primitives có thể compact. Linked nodes cần pointers/references, headers và allocator metadata. Hash table cần spare capacity để giữ load factor. Trie có thể rất tốn pointer slots nếu alphabet lớn. Bitset dùng một bit cho mỗi boolean state và đôi khi giảm memory hàng chục lần so với object set.

Memory footprint ảnh hưởng performance qua cache, GC và paging. Vì vậy “space complexity `O(n)`” chỉ là bước đầu.

## Online, offline, static và dynamic workload

Một distinction mạnh là dữ liệu/query đến theo cách nào.

**Static** nghĩa data gần như không đổi; có thể preprocess mạnh, ví dụ prefix sums hoặc sparse table. **Dynamic** nghĩa update thường xuyên; segment tree, balanced tree hoặc Fenwick tree có thể phù hợp hơn. **Online** nghĩa phải trả lời khi event tới, không biết tương lai. **Offline** nghĩa có thể reorder queries/events để giải hiệu quả hơn, ví dụ DSU với threshold queries hoặc Mo's algorithm trong một số bài range query.

Một algorithm offline có thể nhanh hơn vì được quyền dùng toàn bộ future information. Production systems phải xác định rõ latency requirement trước khi chọn approach.

## Exact, approximate và probabilistic representation

Không phải mọi requirement đều cần exact answer. Bloom Filter chấp nhận false positive nhưng không false negative trong standard insertion-only model. HyperLogLog đổi exact cardinality lấy fixed compact memory và statistical error. Count-Min Sketch đổi exact frequency lấy one-sided estimate.

Điểm thiết kế ở đây là **error budget**. Approximation hợp lệ khi product requirement cho phép và error model được định lượng. Nếu dữ liệu là accounting balance hoặc access-control authorization, approximate membership thường là sai abstraction.

## Deterministic guarantee và expected guarantee

Balanced BST cho deterministic `O(log n)` height. Skip list và randomized quicksort thường được mô tả bằng expected guarantees. Hash table lookup cũng thường expected `O(1)` dưới hashing assumptions.

Expected complexity không đồng nghĩa “luôn nhanh”. Với adversarial input, poor randomness hoặc latency-sensitive system, worst-case behavior có thể quan trọng. Ngược lại, expected algorithms có thể đơn giản và nhanh hơn thực tế. Chọn guarantee là một phần của requirement, không phải chi tiết lý thuyết.

## Mutability, ownership và concurrency làm thay đổi model

Trong C, structure còn có ownership/lifetime invariant: ai allocate, ai free, pointer nào borrowed. Trong Java, object identity, `equals/hashCode`, boxing và GC ảnh hưởng representation. Trong JavaScript, `Map` object keys dùng identity và `Number` có safe-integer limit.

Concurrency thêm một dimension khác. Một structure đúng single-thread chưa chắc đúng khi nhiều threads update. Khi đó invariant phải được giữ qua synchronization protocol hoặc atomic operations. Lock-free structure còn cần reasoning về linearizability, memory reclamation và memory ordering.

Vì vậy “same abstract structure” có thể cần implementation rất khác tùy runtime và concurrency model.

## Khi nào nên preprocess?

Preprocessing là trả chi phí một lần để query sau rẻ hơn. Sorting trước giúp binary search, merge, two pointers. Building index giúp database lookup. Prefix sums giúp range sum `O(1)`. Suffix array/suffix automaton giúp nhiều string queries.

Một cách reasoning đơn giản là so sánh tổng cost:

\[
C_{total} = C_{build} + Q\cdot C_{query}
\]

Nếu `Q` lớn, preprocessing đắt có thể rất đáng. Nếu chỉ có một query, scan thẳng đôi khi tốt hơn xây index.

## Composition: cấu trúc mạnh thường được ghép từ cấu trúc đơn giản

Nhiều systems không dùng một structure duy nhất.

LRU cache = hash map + doubly linked list.

Dijkstra = adjacency representation + priority queue + distance array/map.

Autocomplete = trie/prefix index + ranking structure.

Database query engine = B+Tree/hash index + buffer manager + sorting/hash join operators.

Streaming Top-K = hash/count sketch + heap tùy requirement.

Điều quan trọng là xác định invariant giữa các components. Composition không xóa complexity; nó chuyển thành multi-structure maintenance problem.

## Một workflow mô hình hóa có thể tái sử dụng

Khi gặp một problem mới, có thể đi theo flow sau:

```text
1. Xác định input/output và semantics chính xác.
2. Xác định constraints và error model.
3. Liệt kê operations/queries/updates.
4. Xác định tần suất và latency/memory priorities.
5. Thiết kế state tối thiểu nhưng đủ future-relevant information.
6. Chọn invariant giúp loại work không cần thiết.
7. Chọn representation thực thi invariant đó hiệu quả.
8. Chứng minh correctness của operations.
9. Phân tích asymptotic cost và runtime/memory cost.
10. Test bằng small oracle, adversarial cases và invariant checks.
```

Đây là workflow tổng quát hơn việc ghi nhớ “pattern A dùng HashMap, pattern B dùng heap”.

## Common misconceptions

“Cấu trúc có Big-O tốt hơn luôn tốt hơn” là sai vì constant factor, memory, locality và operation mix khác nhau.

“Có thể chọn algorithm trước rồi ép model vào” thường dẫn tới state thiếu hoặc dư thông tin.

“`O(1)` nghĩa là một bước” là sai; nó chỉ nói cost không tăng theo `n` trong model đó.

“Data structure chỉ là container” cũng sai. Structure là container + invariant + API semantics + cost contract.

## Mental Model

> Data structure là một hợp đồng về shape và summary của state. Algorithm là một hợp đồng về cách state thay đổi. Modeling quyết định information nào cần giữ, invariant quyết định information nào luôn đúng, và complexity là giá phải trả để duy trì các hợp đồng đó dưới workload thực tế.

Khi gặp một bài DSA mới, đừng bắt đầu bằng tên thuật toán. Hãy bắt đầu bằng câu hỏi: **state thật sự là gì, future cần biết gì, query nào phải rẻ, và invariant nào cho phép loại bỏ phần work không cần thiết?**

Xem tiếp: [Correctness & Invariants](./01_algorithm_correctness_and_invariants.md), [Complexity](./02_complexity_analysis.md), [Memory Model](./03_memory_models_c_java_javascript.md), [Mathematical Toolkit](./04_mathematical_toolkit_for_dsa.md) và [Problem Solving Workflow](../90_connections/02_problem_solving_workflow.md).
