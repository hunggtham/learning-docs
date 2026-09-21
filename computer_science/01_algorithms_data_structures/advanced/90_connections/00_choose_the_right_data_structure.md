# Chọn cấu trúc dữ liệu phù hợp
**Data Structure Selection / 자료구조 선택**

Chọn cấu trúc dữ liệu không phải là nhớ một bảng “bài này dùng cấu trúc nào”, mà là quá trình biến yêu cầu thành **khối lượng công việc (workload)** rồi chọn cách biểu diễn phù hợp nhất với khối lượng công việc đó.

Một cấu trúc chỉ “tốt” khi:

```text
các thao tác quan trọng đủ rẻ
bất biến cần thiết được duy trì đúng
bộ nhớ nằm trong ngân sách
độ trễ và thông lượng phù hợp SLA
cách triển khai đủ đơn giản để vận hành và kiểm thử
```

Không có cấu trúc “nhanh nhất” theo nghĩa tuyệt đối. Mảng, bảng băm, cây, heap hay trie chỉ tốt trong một mô hình truy cập cụ thể.

## 1. Bắt đầu từ thao tác

Đừng hỏi “HashMap hay TreeMap?”. Hãy viết các thao tác thật:

```text
lookup(key)
insert(key, value)
delete(key)
min()
max()
predecessor(key)
successor(key)
rangeQuery(l, r)
prefixSearch(prefix)
rank(key)
select(k)
connect(a, b)
sameComponent(a, b)
```

Sau đó đánh dấu thao tác nào chiếm phần lớn lưu lượng và thao tác nào nằm trên đường chạy nóng.

Một thao tác khởi tạo chạy một lần không cần được tối ưu giống thao tác chạy hàng triệu lần mỗi giây.

## 2. Exact Lookup hay Ordered Query?

Nếu chỉ cần equality lookup, Hash Table thường là ứng viên tự nhiên:

```text
get / put / contains -> expected O(1)
```

Nếu cần:

```text
min / max
floor / ceiling
predecessor / successor
range scan
ordered iteration
```

thì thứ tự là một phần của bài toán. Balanced BST hoặc B+Tree thường hợp lý hơn.

Nếu dữ liệu tĩnh, sorted array có thể còn tốt hơn cây vì tìm kiếm `O(log n)`, bộ nhớ gọn và locality tốt.

## 3. Static hay Dynamic?

Dữ liệu tĩnh cho phép tiền xử lý mạnh.

Ví dụ:

```text
static range sum       -> prefix sum
dynamic point update   -> Fenwick / Segment Tree
static RMQ             -> Sparse Table
dynamic ordered set    -> balanced BST
```

Một câu hỏi rất mạnh:

> Ta có thể trả một khoản chi phí xây dựng trước để làm hàng nghìn truy vấn sau rẻ hơn không?

Nếu câu trả lời là có, hãy nghĩ tới sorting, indexing, prefix structures hoặc preprocessing graph/string.

## 4. Read/Write Ratio

Hai hệ thống chứa cùng dữ liệu nhưng tỷ lệ đọc/ghi khác nhau có thể cần cấu trúc khác.

Một index làm đọc nhanh hơn nhưng mọi write phải duy trì index. Một cache làm đọc nhanh nhưng phải trả chi phí invalidation/freshness. Một LSM Tree tối ưu đường ghi tuần tự nhưng tăng read/compaction complexity.

Data structure selection luôn là bài toán **đẩy chi phí từ thao tác này sang thao tác khác**.

## 5. Dense hay Sparse Key Space?

Nếu key là số nguyên dày đặc `0..n-1`, mảng thường tốt hơn HashMap:

```text
count[id]
visited[id]
dist[id]
```

Nếu key thưa, lớn hoặc là chuỗi/object, HashMap phù hợp hơn.

Không nên dùng cấu trúc tổng quát khi miền khóa đã cho phép direct addressing rẻ hơn.

## 6. Contiguous Memory hay Node-Based Structure?

Mảng có locality tốt, ít metadata và traversal nhanh. Cấu trúc node-based linh hoạt hơn cho relinking nhưng phải trả giá cho pointer/reference, allocation và cache miss.

Ví dụ Linked List có thể xóa node `O(1)` khi đã có node, nhưng tìm vị trí vẫn `O(n)` và traversal thường chậm hơn mảng.

Big-O không mô tả đầy đủ memory hierarchy.

## 7. Min/Max liên tục hay Full Order?

Nếu chỉ cần phần tử nhỏ nhất/lớn nhất lặp lại, heap thường đủ:

```text
peek min O(1)
insert O(log n)
extract min O(log n)
```

Không cần trả chi phí duy trì full sorted order của TreeMap.

Nếu cần cả predecessor/range scan, heap không đủ.

Một nguyên tắc quan trọng:

> Chỉ duy trì lượng thứ tự tối thiểu đủ để trả lời query.

## 8. Prefix hay Full-Key Equality?

Nếu workload hỏi prefix:

```text
autocomplete
routing prefix
string dictionary
```

Trie/Radix Tree có thể trực tiếp mã hóa prefix structure.

Nếu chỉ cần exact string lookup, HashMap có thể đơn giản hơn và gọn hơn.

Structure mạnh là structure lưu đúng loại thông tin mà query cần.

## 9. Range Query yêu cầu phép toán gì?

Không phải mọi range structure hỗ trợ mọi aggregate.

Prefix sum dựa trên khả năng “trừ phần trước”. Fenwick Tree phù hợp các phép toán có cấu trúc đại số thích hợp. Segment Tree chỉ cần phép combine có tính kết hợp. Sparse Table đặc biệt mạnh với static idempotent operation như `min/max/gcd`.

Vì vậy trước khi chọn structure hãy hỏi:

```text
operation có associative không?
có identity không?
có inverse không?
có idempotent không?
update là point hay range?
query là prefix hay arbitrary interval?
```

## 10. Mutable hay Persistent?

Nếu chỉ cần trạng thái hiện tại, mutable structure thường đơn giản và tiết kiệm allocation.

Nếu cần:

```text
undo/versioning
snapshot
branching histories
functional semantics
```

persistent structure với structural sharing có thể phù hợp.

Persistent không có nghĩa “lưu xuống disk”; nó có nghĩa phiên bản cũ vẫn dùng được sau update.

## 11. Exact hay Approximate?

Nếu dữ liệu quá lớn, có thể không cần lưu trạng thái chính xác cho mọi key.

```text
membership approximate     -> Bloom/Cuckoo/XOR Filter
cardinality approximate    -> HyperLogLog
frequency approximate      -> Count-Min Sketch
similarity approximate     -> MinHash
```

Nhưng approximation chỉ hợp lệ nếu nghiệp vụ chấp nhận error model.

Một Bloom Filter có false positive nhưng không false negative trong mô hình chuẩn có thể rất tốt làm bộ lọc I/O, nhưng không nên là nguồn sự thật cho authorization.

## 12. Online hay Offline?

Nếu phải trả lời ngay khi dữ liệu đến, chỉ dùng thông tin quá khứ. Nếu có thể giữ toàn bộ input rồi reorder, nhiều thuật toán offline mạnh hơn.

Ví dụ:

```text
sweep line
Kruskal + query sorting
Mo's algorithm
batch processing
```

Offline processing có thể đổi thứ tự event để giảm work. Online system không có quyền đó.

## 13. Ordered Array hay Balanced Tree?

Nếu dữ liệu ít thay đổi:

```text
sorted array
+ binary search
+ sequential range scan
```

có locality và memory footprint rất tốt.

Nếu insert/delete liên tục ở vị trí tùy ý, balanced tree tránh `O(n)` dịch phần tử.

Không nên chọn tree chỉ vì “search O(log n)” nếu workload thực tế gần tĩnh.

## 14. Heap hay Sorted Structure cho Top-K?

Nếu cần Top-K một lần từ batch dữ liệu:

```text
Quickselect
partial sort
heap size k
full sort
```

đều có thể hợp lý tùy `k`, `n` và yêu cầu thứ tự đầu ra.

Nếu dữ liệu đến liên tục, heap size `k` tự nhiên hơn.

Nếu cần truy vấn rank động cho nhiều `k`, order-statistic tree có thể phù hợp hơn.

## 15. Graph Representation

Đồ thị thưa thường dùng adjacency list:

\[
O(V+E)
\]

Đồ thị dày có thể dùng adjacency matrix nếu cần edge lookup cực nhanh và `V²` memory chấp nhận được.

Nếu graph tĩnh rất lớn, CSR giúp giảm overhead object và tăng locality.

Representation graph quyết định cả memory lẫn complexity của traversal.

## 16. DSU chỉ tốt khi bài toán đúng mô hình merge-only

DSU hỗ trợ rất tốt:

```text
union(a,b)
find(a)
sameComponent(a,b)
```

nhưng không hỗ trợ split/delete edge tổng quát.

Nếu graph connectivity thay đổi bằng cả add và remove, cần offline reversal, rollback DSU hoặc dynamic connectivity structure phức tạp hơn.

Structure nhanh thường nhanh vì nó **không hỗ trợ một số thao tác khó**.

## 17. Bounded Memory hay Unbounded Growth?

Queue không giới hạn có thể che giấu overload cho tới khi hệ thống hết memory. Ring buffer bounded bắt hệ thống chọn policy khi đầy:

```text
block
drop
reject
spill
backpressure
```

Data structure capacity là một quyết định reliability, không chỉ implementation detail.

## 18. Worst-Case hay Expected Guarantee?

Hash Table, Skip List và randomized algorithms thường có expected bound tốt. Balanced Tree cho deterministic `O(log n)`.

Nếu workload có thể đối nghịch hoặc tail latency quan trọng, deterministic bound có thể đáng giá hơn constant factor trung bình tốt.

Nếu throughput là mục tiêu chính, expected/amortized design đơn giản hơn có thể thắng.

## 19. Amortized hay Per-Operation Latency?

Dynamic array append `O(1)` amortized nhưng một resize riêng có thể `O(n)`. Hash Table resize tương tự.

Hệ thống real-time có thể cần:

```text
preallocation
incremental resize
deamortized structure
bounded buffer
```

Đừng xóa từ “amortized” khi mô tả SLA.

## 20. External Memory

Khi dữ liệu vượt RAM, số page I/O quan trọng hơn số comparison.

B+Tree có fan-out lớn để giảm chiều cao. External Merge Sort dùng sequential I/O. LSM Tree chuyển random write thành sequential append + background compaction.

Data structure phải khớp tầng lưu trữ thực tế.

## 21. Concurrency

Một structure tốt single-thread chưa chắc tốt multi-thread.

Cần hỏi:

```text
read-heavy hay write-heavy?
contention tập trung ở đâu?
lock granularity thế nào?
cần linearizability không?
iterator/snapshot semantics là gì?
```

ConcurrentHashMap không chỉ là HashMap “nhanh hơn”; nó có contract đồng thời khác.

Lock-free structure thêm vấn đề ABA, memory reclamation và ordering.

## 22. Composition

Hệ thống thực tế thường ghép nhiều structure.

### LRU Cache

```text
HashMap       -> tìm node theo key
Doubly List   -> recency order
```

### Dijkstra

```text
adjacency list
+ distance array/map
+ priority queue
```

### Database Query Engine

```text
B+Tree / Hash Index
+ Buffer Pool
+ Hash Join / Sort-Merge Join
+ Heap cho Top-N
```

### Autocomplete

```text
Trie/Radix index
+ ranking metadata
+ heap/top-k cache
```

Điểm khó không chỉ là từng structure mà là **bất biến liên cấu trúc**.

## 23. Đừng nhân đôi nguồn sự thật nếu không cần

Nếu cùng một dữ liệu được lưu trong map và list, cần bảo đảm hai representation luôn đồng bộ.

Mỗi secondary index, cache hoặc metadata tăng tốc query nhưng đồng thời tạo thêm invariant phải duy trì.

Một structure phụ chỉ đáng có nếu lợi ích query lớn hơn cost update, memory và complexity vận hành.

## 24. Một decision matrix thực dụng

| Câu hỏi | Nếu “có”, hãy nghĩ tới |
|---|---|
| key dày đặc dạng integer? | array / bitset |
| equality lookup là chính? | hash table |
| cần ordered/range query? | sorted array / balanced tree / B+Tree |
| cần min/max liên tục? | heap |
| cần prefix? | trie / radix tree |
| dữ liệu tĩnh, nhiều range query? | prefix / sparse table |
| có update + aggregate? | Fenwick / Segment Tree |
| chỉ merge connectivity? | DSU |
| text cần substring index? | suffix structures / automata |
| dữ liệu vượt RAM? | B+Tree / external sort / LSM concepts |
| memory cực hạn, chấp nhận sai số? | probabilistic structures |

Bảng chỉ là điểm khởi đầu. Quyết định cuối phải dựa trên workload.

## 25. Từ yêu cầu tới cost model

Một cách formal hơn là viết:

\[
ExpectedCost = \sum_i p_i C_i
\]

với `p_i` là tỷ lệ thao tác và `C_i` là chi phí tương ứng.

Sau đó cộng thêm memory cost, latency requirement và implementation complexity.

Không cần luôn tính ra con số chính xác; mục tiêu là tránh tối ưu một thao tác hiếm mà bỏ qua thao tác chi phối.

## 26. Migration Signal

Structure đúng hôm nay có thể sai sau khi workload thay đổi.

Dấu hiệu cần xem lại:

```text
n tăng 100 lần
read/write ratio đổi mạnh
range query xuất hiện nhiều hơn
GC/allocation trở thành bottleneck
p99 latency tăng do resize
memory vượt budget
concurrency contention tăng
```

Data structure selection là quyết định có thể cần tái đánh giá, không phải lựa chọn một lần mãi mãi.

## 27. Benchmark đúng workload

Không benchmark HashMap với random integer rồi suy ra performance cho key dài, expensive hash hoặc adversarial distribution.

Không benchmark TreeMap chỉ bằng lookup nếu production workload có range scan lớn.

Benchmark phải phản ánh:

```text
data size
key distribution
operation mix
mutation pattern
concurrency
memory pressure
```

## 28. Chọn structure đơn giản nhất đáp ứng yêu cầu

Structure phức tạp hơn tạo nhiều code, nhiều edge case và nhiều invariant hơn.

Nếu array + sort một lần đủ, không cần custom balanced tree. Nếu `HashMap` chuẩn đủ, không cần tự viết Cuckoo Hashing. Nếu `O(n²)` với `n<=100` đã dư sức, không cần Segment Tree.

Độ phức tạp implementation cũng là một chi phí kỹ thuật.

## 29. Những hiểu lầm phổ biến

“Big-O nhỏ hơn luôn nhanh hơn” — sai do constant factor, locality, allocation và workload mix.

“Linked List chèn O(1) nên tốt hơn ArrayList” — bỏ qua chi phí tìm node và cache behavior.

“HashMap luôn tốt hơn TreeMap vì O(1)” — sai nếu cần thứ tự hoặc worst-case deterministic guarantee.

“Segment Tree tốt hơn prefix sum vì mạnh hơn” — sai nếu dữ liệu tĩnh; sức mạnh dư thừa phải trả bằng memory/code/query cost.

“Chỉ cần chọn một data structure cho cả hệ thống” — hệ thống thật thường là composition.

## 30. Workflow chọn cấu trúc

```text
1. Viết chính xác operation set.
2. Ghi tần suất và đường chạy nóng.
3. Xác định static/dynamic, online/offline.
4. Xác định ordered/equality/range/prefix semantics.
5. Xác định dense/sparse và quy mô n.
6. Xác định memory/cache/I/O model.
7. Chọn invariant tối thiểu hỗ trợ query.
8. So các candidate bằng total cost, không chỉ một operation.
9. Kiểm tra correctness + edge cases.
10. Benchmark workload đại diện.
```

## Mô hình tư duy

> Chọn cấu trúc dữ liệu là chọn **thông tin nào đáng được lưu sẵn** và **chi phí nào đáng trả khi cập nhật** để những query quan trọng trở nên rẻ.

Khi phân vân giữa hai cấu trúc, đừng hỏi “cái nào nhanh hơn?”. Hãy hỏi: **workload của tôi là gì, invariant nào thật sự cần, guarantee nào bắt buộc, memory hierarchy ra sao, và liệu một structure đơn giản hơn đã đủ chưa?**

Xem thêm: [Problem Modeling](../00_foundations/00_dsa_as_problem_modeling.md), [Complexity](../00_foundations/02_complexity_analysis.md), [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md), [Problem-Solving Workflow](./02_problem_solving_workflow.md).