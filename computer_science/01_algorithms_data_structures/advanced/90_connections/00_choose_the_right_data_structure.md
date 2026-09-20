# Chọn cấu trúc dữ liệu phù hợp
**Data Structure Selection / 자료구조 선택**

Chọn cấu trúc dữ liệu không phải là nhớ một bảng “bài này dùng cấu trúc nào”, mà là quá trình biến yêu cầu của bài toán thành **workload** rồi chọn representation phù hợp với workload đó. Một cấu trúc dữ liệu chỉ “tốt” khi các operation quan trọng của bài toán trở nên đủ rẻ, invariant cần thiết được giữ ổn định, và chi phí bộ nhớ cũng như chi phí triển khai chấp nhận được.

Nói cách khác, thay vì hỏi “Array, HashMap hay Tree cái nào nhanh nhất?”, hãy hỏi chính xác hơn: dữ liệu được đọc theo index hay theo key, có cần thứ tự hay không, insert/delete diễn ra ở đâu, có cần min/max liên tục hay không, query có theo range hay prefix không, dữ liệu có static hay mutate thường xuyên không, kích thước dữ liệu có vừa RAM hay phải chạm disk/network hay không.

## 1. Bắt đầu từ operation chứ không bắt đầu từ tên cấu trúc

Một requirement như “tìm user theo `userId` thật nhanh” thực ra nói rằng operation trọng tâm là **exact lookup by key**. Với workload này, hash table thường là ứng viên tự nhiên vì lookup expected `O(1)`. Nhưng nếu requirement đổi thành “tìm toàn bộ user có `userId` trong khoảng A đến B”, hash table không còn phù hợp bằng ordered tree hoặc database index kiểu B+Tree, vì bài toán cần **order semantics** chứ không chỉ exact equality.

Nếu requirement là “lấy phần tử thứ `i`”, array có lợi thế vì address có thể suy ra trực tiếp từ base address và index. Nếu requirement là “luôn lấy phần tử nhỏ nhất rồi chèn phần tử mới”, heap hợp lý hơn vì nó duy trì partial order đủ cho `min/max` mà không phải sort toàn bộ.

Bảng sau chỉ nên xem như điểm xuất phát:

| Nhu cầu chính | Cấu trúc thường phù hợp |
|---|---|
| random access theo index | array / dynamic array |
| exact lookup theo key | hash map / hash set |
| ordered dynamic keys | balanced BST / tree map |
| min/max lặp lại | heap / priority queue |
| LIFO | stack |
| FIFO | queue |
| thao tác hai đầu | deque |
| prefix string | trie |
| graph reachability | adjacency list + BFS/DFS |
| merge-only connectivity | DSU / Union-Find |
| static prefix/range aggregate | prefix sum |
| point update + prefix/range sum | Fenwick tree |
| general range aggregate/update | segment tree |
| membership approximate rất lớn | Bloom filter |
| approximate frequency | Count-Min Sketch |

Điểm quan trọng là cùng một requirement có thể có nhiều implementation khác nhau. “Queue” là abstract data type; implementation có thể là circular array, linked list hoặc deque library. Cái phải chọn không chỉ là interface mà còn là representation.

## 2. Read pattern và write pattern quyết định cấu trúc

Hai hệ thống có cùng dữ liệu nhưng read/write ratio khác nhau có thể cần cấu trúc khác nhau.

Một dataset gần như static nhưng query rất nhiều thường đáng để preprocessing mạnh. Prefix sum là ví dụ điển hình: ta bỏ `O(n)` upfront để mỗi range-sum query còn `O(1)`. Nếu dữ liệu thay đổi liên tục, prefix sum trở nên đắt vì mỗi update có thể làm hỏng toàn bộ prefix phía sau. Khi đó Fenwick Tree hoặc Segment Tree hy sinh query từ `O(1)` thành `O(log n)` để đổi lấy update `O(log n)`.

Tư duy này xuất hiện ở mọi nơi trong Computer Science: **precompute vs update cost**, **indexing vs write amplification**, **cache vs freshness**. Database index cũng chính là một trade-off tương tự: đọc nhanh hơn nhưng insert/update/delete phải trả thêm chi phí duy trì index.

## 3. Order requirement là một ranh giới lớn

Hash table rất mạnh nếu chỉ cần equality. Nhưng ngay khi bài toán cần một trong các operation như `min`, `max`, predecessor, successor, lower bound, upper bound hoặc range scan, thứ tự trở thành first-class requirement.

Balanced BST giữ keys có order với lookup/insert/delete thường `O(log n)`. Đổi lại, nó có overhead pointer/node và locality kém hơn contiguous array. Nếu dữ liệu static, sorted array đôi khi còn tốt hơn tree: binary search `O(log n)`, memory compact, cache locality tốt, và range scan rất hiệu quả.

Vì vậy “dynamic hay static” phải được xét cùng “ordered hay unordered”. Một sorted vector static có thể đánh bại tree map trong thực tế dù cùng có `O(log n)` lookup, bởi constants và cache behavior khác nhau.

## 4. Big-O chưa đủ: memory layout và locality cũng quan trọng

Linked list nổi tiếng với insert/delete `O(1)` khi đã có node pointer. Nhưng mỗi node thường chứa pointer metadata, nằm rải rác trong heap và dễ gây cache miss. Array có thể phải dịch chuyển phần tử khi insert giữa, nhưng traversal tuyến tính trên contiguous memory thường rất nhanh trên CPU hiện đại.

Đây là lý do tại sao một structure có Big-O “đẹp” chưa chắc nhanh hơn trên workload thật. Hardware đọc cache line, không đọc từng biến Java/C riêng lẻ. Trong Java còn có object header và reference indirection; trong JavaScript còn có dynamic representation và JIT behavior. Cost model thực tế chịu ảnh hưởng của runtime.

Khi data lớn đến mức không vừa RAM, locality còn quan trọng hơn. B-Tree/B+Tree giảm số lần truy cập page/disk bằng cách tăng branching factor. Đây là lý do database index không dùng binary search tree đơn giản cho persistent storage.

## 5. Mutation pattern: dữ liệu thay đổi như thế nào?

Không chỉ “có update hay không” mà phải hỏi update theo dạng nào.

Nếu chỉ append cuối, dynamic array rất hiệu quả. Nếu thường xuyên insert đầu, deque/circular buffer hợp lý hơn. Nếu chỉ merge các component và hỏi hai node có cùng component không, DSU tối ưu vì nó deliberately không hỗ trợ arbitrary edge deletion. Nếu graph có edge add/remove động và query connectivity online, DSU thường không đủ và ta bước sang dynamic connectivity phức tạp hơn.

Một cấu trúc dữ liệu mạnh thường mạnh vì nó **giới hạn problem model**. Heap nhanh cho min/max vì nó không cố duy trì full sorted order. DSU nhanh vì không hỗ trợ split component. Fenwick Tree gọn vì operation aggregate phải có algebraic structure phù hợp. Hiểu giới hạn này quan trọng hơn thuộc tên cấu trúc.

## 6. Invariant là thứ structure “mua” bằng update cost

Mỗi data structure duy trì một invariant để query rẻ hơn.

Array duy trì contiguous indexing. Heap duy trì parent không lớn hơn children đối với min-heap. BST duy trì mọi key bên trái nhỏ hơn node và mọi key bên phải lớn hơn theo comparator. Balanced BST thêm height/balance invariant. Hash table duy trì mapping từ hash bucket đến entries. Segment Tree duy trì aggregate của mỗi interval node.

Khi chọn structure, hãy hỏi: **invariant nào trực tiếp giúp trả lời query của tôi?** Nếu invariant không phục vụ query, bạn đang trả update/memory cost vô ích.

Ví dụ, nếu chỉ cần membership, full sorted order của TreeSet có thể là chi phí dư thừa so với HashSet. Ngược lại, nếu cần iterate theo order, HashSet lại thiếu invariant cần thiết.

## 7. Composition mới là cách hệ thống thực tế được xây

Một structure riêng lẻ hiếm khi giải trọn requirement production. Hệ thống thường ghép nhiều structures, mỗi structure đảm nhận một operation khác nhau.

**LRU cache** kết hợp hash map và doubly linked list. Hash map cho lookup `O(1)`; linked list giữ recency order và cho phép move-to-front/remove-tail nhanh.

**Dijkstra** kết hợp adjacency list để biểu diễn graph với priority queue để luôn chọn vertex có distance nhỏ nhất tiếp theo.

**Kruskal** kết hợp edge list, sorting và DSU. Sorting tạo order theo weight; DSU kiểm tra nhanh liệu thêm edge có tạo cycle không.

**Autocomplete** có thể kết hợp trie cho prefix lookup với heap hoặc cached ranking cho top suggestions.

**Database engine** có thể đồng thời dùng buffer pool, B+Tree index, hash table cho hash join, heap/priority queue cho top-N, và Bloom filter để loại candidate trước khi đọc dữ liệu đắt tiền.

Điều này cho thấy data-structure selection thường là bài toán architecture, không phải một lựa chọn duy nhất.

## 8. Một workflow chọn structure có hệ thống

Khi gặp bài mới, trước tiên hãy viết các operation bằng ngôn ngữ trung lập. Ví dụ: `lookup(key)`, `insert(key)`, `delete(key)`, `min()`, `successor(key)`, `rangeSum(l,r)`, `prefixSearch(s)`, `connect(a,b)`, `sameComponent(a,b)`.

Sau đó đánh dấu operation nào nằm trên hot path và tần suất tương đối của chúng. Một operation chạy một lần lúc startup không cần tối ưu giống operation chạy hàng triệu lần mỗi giây.

Tiếp theo xác định constraints: `n` lớn bao nhiêu, dữ liệu static hay dynamic, có duplicate không, cần deterministic worst-case hay expected complexity đủ, có memory limit không, có concurrency không, dữ liệu ở RAM hay storage ngoài.

Cuối cùng mới so sánh candidate theo tổng cost. Có thể một structure cho lookup nhanh hơn nhưng update chậm hơn; hoặc memory cao hơn nhưng implementation đơn giản và ít bug hơn. Production engineering thường ưu tiên giải pháp đủ nhanh và dễ duy trì thay vì cấu trúc lý thuyết phức tạp nhất.

## 9. Ví dụ reasoning: session store

Giả sử cần lưu session theo `sessionId`, lookup rất nhiều, expiry theo thời gian, và phải xóa session hết hạn.

Hash map giải quyết exact lookup. Nhưng hash map không giúp lấy session sắp hết hạn nhất. Nếu thêm một min-heap keyed by expiry time, ta có thể pop expired sessions theo thứ tự. Tuy nhiên vì session có thể refresh expiry, heap có thể chứa stale entries; khi pop cần kiểm tra version/timestamp với map trước khi xóa thật.

Một requirement tưởng như “lưu session” đã dẫn tới composition `HashMap + MinHeap`, kèm invariant cross-structure. Đây là dạng reasoning quan trọng hơn việc thuộc một bảng Big-O.

## 10. C, Java và JavaScript có cost model khác nhau

Trong C, representation quyết định trực tiếp layout, pointer lifetime và allocation strategy. Một contiguous array of structs có thể khác đáng kể so với array of pointers.

Trong Java, `ArrayList<Integer>` có boxing overhead so với primitive array `int[]`. `HashMap<K,V>` và `TreeMap<K,V>` có semantics và object overhead khác nhau. Comparator phải đúng và nhất quán với ordering cần thiết.

Trong JavaScript, `Array` là general-purpose dynamic collection chứ không phải raw contiguous primitive array theo nghĩa C. `Map` phù hợp hơn plain object khi key là arbitrary object hoặc khi muốn semantics mapping rõ ràng. `TypedArray` hữu ích khi cần numeric fixed-size representation predictable hơn.

Do đó cùng một abstract algorithm có thể dùng structure khác nhau ở mức implementation tùy runtime.

## 11. Những sai lầm chọn cấu trúc thường gặp

Một sai lầm phổ biến là tối ưu một operation nhìn thấy rõ mà bỏ qua operation ẩn. Ví dụ “linked list insert `O(1)`” nhưng application phải tìm vị trí trước, khiến toàn operation vẫn `O(n)`. Một lỗi khác là dùng hash map rồi sau đó liên tục sort keys cho mỗi query; nếu ordering là requirement cốt lõi, tree hoặc sorted representation có thể hợp lý hơn.

Cũng cần tránh chọn structure chỉ vì quen tay. Dùng priority queue khi chỉ cần một lần min có thể là over-engineering. Dùng Segment Tree cho dữ liệu static khi prefix sum đủ dùng cũng vậy.

## Mental Model

> Data structure là một hợp đồng trade-off. Bạn trả bằng memory, update cost, implementation complexity hoặc invariant maintenance để mua những query nhất định rẻ hơn.

Một lựa chọn tốt bắt đầu từ workload: **operation nào cần nhanh, dữ liệu biến đổi ra sao, order nào phải giữ, scale ở đâu, và cost model của runtime/hardware là gì**. Khi các câu đó rõ, tên cấu trúc thường tự xuất hiện như hệ quả thay vì phải đoán.

Xem thêm: [Problem-Solving Workflow](./02_problem_solving_workflow.md), [DSA trong Database, Network và Systems](./01_dsa_in_databases_networks_and_systems.md), [Complexity Analysis](../00_foundations/02_complexity_analysis.md).