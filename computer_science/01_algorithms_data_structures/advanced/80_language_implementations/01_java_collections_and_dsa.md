# Java Collections nhìn dưới góc DSA
**Java Collections와 자료구조 선택**

Java Collections Framework cung cấp abstractions mạnh và an toàn hơn so với tự quản pointer, nhưng abstraction không làm complexity biến mất. Khi dùng `List`, `Map`, `Set`, `Queue` hay `Deque`, ta vẫn đang chọn data structure với invariant, memory layout và performance profile cụ thể.

Học DSA trong Java nên có hai lớp:

```text
1. hiểu data structure / algorithm abstract
2. biết JDK collection nào hiện thực semantics đó, với cost và caveat nào
```

Nếu chỉ biết interface mà không biết implementation, code vẫn đúng chức năng nhưng có thể chọn sai workload model.

## Interface trước implementation

Các interface mô tả behavioral contract:

```text
List
Set
Map
Queue
Deque
NavigableMap
NavigableSet
```

Implementations phổ biến:

```text
ArrayList
LinkedList
HashMap
HashSet
TreeMap
TreeSet
ArrayDeque
PriorityQueue
```

API-level code nên depend on interface khi hợp lý:

```java
List<Integer> xs = new ArrayList<>();
Map<String, User> users = new HashMap<>();
Deque<Task> q = new ArrayDeque<>();
```

Nhưng performance-sensitive code vẫn phải biết concrete type.

## ArrayList là default list trong đa số trường hợp

`ArrayList` dựa trên resizable array.

Properties quan trọng:

```text
get(index)        O(1)
set(index)        O(1)
append            amortized O(1)
insert/remove mid O(n)
contains          O(n)
```

Nó thường có locality tốt hơn node-based list và ít per-element overhead hơn.

Ngay cả khi bài toán có insert/delete, `ArrayList` vẫn thường thắng nếu operations chủ yếu ở cuối hoặc dataset vừa phải.

## LinkedList không tự động tốt cho insert/delete

`LinkedList` có node links. Insert/delete tại node position đã biết có thể `O(1)`, nhưng nếu API chỉ cho index:

```java
list.add(i, x)
```

phải traverse tới index trước, thường `O(n)`.

Node allocation, pointer chasing và GC overhead còn làm locality kém.

Vì vậy “LinkedList insert O(1)” là statement thiếu context.

## ArrayDeque cho stack và queue

`ArrayDeque` thường là default tốt cho:

```text
stack
queue
double-ended queue
```

```java
Deque<Integer> dq = new ArrayDeque<>();

dq.push(10);
int x = dq.pop();

dq.offerLast(20);
int y = dq.pollFirst();
```

Nó tránh overhead node của `LinkedList` và không có legacy synchronization baggage của `Stack`.

## Không dùng `Stack` làm default

`java.util.Stack` là legacy class dựa trên `Vector`. Modern code thường dùng `Deque`:

```java
Deque<Integer> stack = new ArrayDeque<>();
```

Interface diễn đạt intention tốt hơn.

## HashMap mental model

`HashMap` map key tới bucket/table position bằng hash.

Expected:

```text
get/put/remove ~ O(1)
```

nhưng không giữ sorted order.

Correctness phụ thuộc contract:

```text
if a.equals(b) == true
then a.hashCode() == b.hashCode()
```

Converse không bắt buộc: equal hash không nghĩa equal objects.

## Mutable keys là một lỗi thiết kế phổ biến

Nếu key object thay đổi field tham gia `equals/hashCode` sau khi insert, logical bucket identity có thể thay đổi nhưng HashMap không tự move entry.

Ví dụ bad idea:

```java
class Key {
    int userId;
    int productId;
    // equals/hashCode use both mutable fields
}
```

Sau mutation, `map.get(key)` có thể không tìm như mong đợi.

Prefer immutable key:

```java
record Key(int userId, int productId) {}
```

Record rất tiện cho compound state/key trong DSA.

## Hash collision và worst-case intuition

HashMap expected O(1) không phải magical direct addressing. Collisions vẫn xảy ra.

Modern JDK có implementation details giúp long collision chains trong một số conditions, nhưng code không nên phụ thuộc mù quáng vào internal thresholds/version details.

Important mental model:

```text
hash quality + load factor + equality cost
```

ảnh hưởng performance thật.

## Load factor và resize

HashMap tăng table khi occupancy vượt threshold liên quan load factor.

Resize là operation đắt nhưng amortized across puts.

Nếu biết expected size lớn, pre-sizing có thể giảm repeated resize:

```java
Map<Integer, Integer> map = new HashMap<>(expectedCapacity);
```

Nhưng initial-capacity semantics cần hiểu theo JDK docs/version; đừng hard-code formulas dựa internal implementation nếu không cần.

## HashSet thực chất dùng hashing semantics

`HashSet` cung cấp membership uniqueness. Nó thường dựa trên hash-backed representation.

Use khi cần:

```text
visited
membership
deduplication
```

Không dùng khi cần sorted iteration/floor/ceiling.

## TreeMap và TreeSet

`TreeMap`/`TreeSet` cung cấp ordered semantics, thường với self-balancing tree implementation.

Operations khoảng:

```text
get/put/remove O(log n)
first/last
floor/ceiling
lower/higher
range views
```

Ví dụ:

```java
NavigableMap<Integer, String> map = new TreeMap<>();
map.floorEntry(x);
map.ceilingEntry(x);
map.subMap(l, true, r, false);
```

Đây là ordered-map abstraction mà HashMap không cung cấp tự nhiên.

## Comparator contract

Comparator phải tạo ordering nhất quán.

Tránh:

```java
(a, b) -> a.priority - b.priority
```

vì overflow.

Dùng:

```java
Comparator.comparingInt(Node::priority)
```

hoặc:

```java
Integer.compare(a, b)
```

Nếu comparator trả `0` cho hai objects mà domain coi khác key, `TreeSet/TreeMap` có thể coi chúng cùng ordering position.

Sorted collection uniqueness dựa comparator/natural ordering semantics, không đơn giản là object identity.

## PriorityQueue

Java `PriorityQueue` là heap-based priority queue.

```text
peek O(1)
offer O(log n)
poll O(log n)
```

Nó không cho efficient arbitrary search/remove-by-value guarantee kiểu indexed heap.

Dijkstra pattern thường push duplicate states và bỏ stale entries khi pop.

```java
record State(int node, long dist) {}

PriorityQueue<State> pq =
    new PriorityQueue<>(Comparator.comparingLong(State::dist));
```

## Mutable priority pitfall

Nếu object đang trong `PriorityQueue` và ta sửa field dùng comparator, queue không tự reheapify.

Bad:

```java
node.priority = newValue;
```

khi `node` vẫn nằm trong PQ.

Use immutable state entry + reinsert, hoặc custom indexed heap.

## Primitive arrays thường tốt hơn boxed collections cho algorithms

```java
int[] parent;
long[] dist;
boolean[] seen;
```

thường tốt hơn:

```java
List<Integer>
List<Long>
List<Boolean>
```

khi size biết trước.

Boxing tạo objects/references, tăng memory và GC pressure.

Trong DSA hot loops, primitive arrays là default rất mạnh.

## Boxing và unboxing

`Integer`, `Long`, `Double` là objects.

```java
List<Integer> xs = new ArrayList<>();
```

mỗi element logically boxed.

Autoboxing làm syntax dễ nhưng không miễn phí.

Ngoài performance, null unboxing còn có thể throw `NullPointerException`:

```java
Integer x = null;
int y = x; // NPE
```

## Array of objects vs primitive arrays

Graph edge objects rất readable:

```java
record Edge(int to, int weight) {}
List<List<Edge>> g;
```

Nhưng huge graph có millions edges → object overhead đáng kể.

Alternative compact representation:

```text
int[] to
int[] weight
int[] next / offsets
```

JVM arrays of primitives gần với SoA/CSR thinking trong C.

Readable model first, compact model when workload justifies.

## Record cho immutable algorithm state

Java records rất hợp với:

```text
priority queue states
compound map keys
edges
coordinates
```

Ví dụ:

```java
record Cell(int r, int c, int mask) {}
```

Records generate value-style `equals/hashCode` based components, useful cho hash key nếu components immutable/value-semantic.

## Beware record containing mutable component

Record reference itself immutable, nhưng referenced object có thể mutable:

```java
record Key(List<Integer> xs) {}
```

Nếu list content tham gia equality/hash và bị mutate, vẫn có mutable-key problem.

Immutability phải deep enough cho identity semantics.

## `computeIfAbsent`

Graph building:

```java
Map<String, List<String>> g = new HashMap<>();
g.computeIfAbsent(u, k -> new ArrayList<>()).add(v);
```

Rất tiện cho sparse maps.

Nhưng trong performance-critical loops, lambda/allocation behavior nên profile thay vì assume free.

## `merge` và frequency maps

```java
freq.merge(x, 1, Integer::sum);
```

hoặc:

```java
freq.compute(x, (k, v) -> v == null ? 1 : v + 1);
```

Readable cho counts, nhưng primitive specialized array nhanh hơn nếu key domain nhỏ.

## Key domain quyết định structure

Nếu keys là integers `0..n-1`, đừng reflexively dùng HashMap:

```java
int[] count = new int[n];
```

Direct indexing cho constant-time lookup với low overhead.

HashMap phù hợp sparse/unbounded key domain, không phải mọi mapping problem.

## EnumMap và EnumSet

Nếu key domain là enum, `EnumMap`/`EnumSet` có specialized representation efficient hơn generic hash structures.

Đây là lesson: JDK có domain-specialized collections mà complexity semantics tốt hơn generic choice.

## BitSet

`java.util.BitSet` compact boolean flags thành machine words.

Useful cho:

```text
large membership sets
bitset DP
set intersection/union
reachability optimization
```

Operations AND/OR/XOR xử lý many bits per machine word.

## Arrays.sort vs Collections.sort/List.sort

Primitive arrays:

```java
Arrays.sort(int[])
```

khác object-array/list sorting implementation details.

Algorithm guarantees/stability có thể khác theo overload/type/version.

Nếu stability semantics quan trọng, check official JDK docs for exact API/version rather than assume.

Core lesson: library method name không thay algorithmic contract.

## Binary search APIs

`Arrays.binarySearch` trả index nếu found; nếu not found trả encoded insertion point negative.

Nếu cần lower-bound/upper-bound với duplicates, thường phải custom implementation vì standard binarySearch không guarantee first occurrence.

Đừng dùng returned arbitrary matching index để suy ra frequency boundary.

## Collections.binarySearch

Trên random-access lists hợp lý. Trên linked list, abstraction may incur traversal cost details. Better understand collection representation rather than apply binary search blindly to a non-random-access structure.

Sorted order alone không đủ; access cost cũng matter.

## List views và aliasing

`subList` thường là view backed by original list, không necessarily independent copy.

Mutation interactions có semantics/invalidation conditions cần hiểu.

Nếu cần snapshot độc lập:

```java
new ArrayList<>(list.subList(l, r))
```

View vs copy là memory/aliasing choice.

## `Collections.unmodifiable*` không phải deep immutability

Unmodifiable wrapper cấm mutation qua wrapper API, nhưng underlying collection hoặc element objects có thể vẫn mutable.

Algorithm state shared across components cần phân biệt read-only view và immutable data.

## Iterator invalidation và fail-fast behavior

Many standard collections có fail-fast iterators detecting structural modification on best-effort basis.

Đây không phải concurrency guarantee.

Đừng dựa vào `ConcurrentModificationException` như synchronization mechanism.

## ConcurrentHashMap

`ConcurrentHashMap` hỗ trợ concurrent access với semantics khác HashMap.

Chọn vì concurrency requirement, không vì “nhanh hơn HashMap”.

Operations compound như:

```text
check then put
read-modify-write
```

cần atomic methods (`compute`, `putIfAbsent`, etc.) nếu muốn race-safe semantics.

## BlockingQueue

Producer-consumer system có thể dùng `BlockingQueue`.

Queue data structure giờ thêm synchronization và blocking semantics.

Bounded queue còn encode backpressure:

```text
put waits when full
```

DSA abstraction nối trực tiếp với systems behavior.

## CopyOnWrite collections

Copy-on-write phù hợp read-heavy, write-rare workloads. Mỗi write copy underlying storage, nên write-heavy cực tệ.

Tên “thread-safe” không đủ để chọn; mutation pattern là critical.

## IdentityHashMap

`IdentityHashMap` dùng reference identity (`==`) thay vì logical `equals` semantics.

Niche use cases: object graph algorithms, serialization internals, identity-based tracking.

Không dùng thay HashMap chỉ vì key objects.

## WeakHashMap và lifetime

`WeakHashMap` cho keys không giữ strong reachability theo same way; entries có thể disappear khi key GC-eligible.

Đây là lifetime semantics đặc biệt, không phải general cache replacement.

Cần hiểu GC reachability nếu dùng.

## Garbage collection không loại bỏ memory leaks logic

Java tự reclaim unreachable objects, nhưng nếu cache/map/list giữ references mãi, objects vẫn reachable và leak ở application level.

Ví dụ unbounded memoization cache có thể tăng heap vô hạn dù không có `malloc/free` bugs.

Memory ownership trong Java là **reachability management** nhiều hơn manual free.

## Object retention trong graph/tree

Một root reference giữ toàn bộ reachable graph alive.

Nếu muốn release structure, remove external roots/listeners/caches. Cycles tự thân không gây leak cho tracing GC nếu unreachable từ GC roots.

Đây là khác biệt quan trọng với reference-count-only systems.

## Recursion depth

Java recursion không guaranteed tail-call optimized. Deep DFS/BST chain có thể `StackOverflowError`.

Iterative stack bằng `ArrayDeque` an toàn hơn cho adversarial depth.

Không catch StackOverflowError như normal algorithm control flow.

## `long` cho accumulated cost

Graph distances, prefix sums, counts có thể vượt `int`.

Use `long` when necessary.

Comparator:

```java
Comparator.comparingLong(State::dist)
```

Avoid casts/subtraction narrowing.

## Overflow vẫn có trong `long`

`Long.MAX_VALUE + w` overflow.

Infinity sentinel nên có margin hoặc guard:

```java
static final long INF = Long.MAX_VALUE / 4;
```

và only add from reachable values.

## BigInteger

Nếu exact integers vượt 64-bit, `BigInteger` cung cấp arbitrary precision nhưng operations/object allocations đắt hơn primitives.

Use khi mathematical correctness thật sự cần, không thay `long` mặc định.

## Generic type erasure

Java generics giúp type safety source-level, nhưng primitive types không dùng trực tiếp làm type argument.

Đây là lý do standard `List<int>` không tồn tại và boxing xuất hiện.

Specialized primitive libraries có thể dùng khi profile chứng minh cần.

## Custom heap/segment tree thường dùng arrays

Even trong Java OO, low-level DSA implementation thường tốt nhất bằng primitive arrays:

```java
long[] tree = new long[4 * n];
int[] heap = new int[n];
int[] position = new int[n];
```

Không cần biến mọi node thành class object.

Representation should serve workload, not OO aesthetics.

## Adjacency list patterns

Readable:

```java
List<List<Edge>> g;
```

Memory-conscious static graph:

```text
int[] head
int[] to
int[] next
long[] weight
```

hoặc CSR offsets.

Know both patterns.

## Streams và complexity

Stream API làm code declarative nhưng không xóa algorithmic work.

```java
stream.sorted()
stream.distinct()
collect(groupingBy(...))
```

vẫn build/use data structures và có complexity.

Repeated streams over same data có thể redo work; materialize/preprocess khi workload cần reuse.

## Streams trong hot DSA loops

Traditional loops thường dễ kiểm soát allocation, boxing và early exit hơn.

Streams có thể readable ở non-hot transformations, nhưng competitive/performance DSA code thường dùng loops.

Không phải vì streams “chậm luôn”, mà vì cost/control model khác và profiling quyết định.

## Parallel streams không tự động làm algorithm scalable

Parallelization có splitting/merge overhead và shared-memory contention.

Graph traversals, DP dependencies hoặc small arrays có thể không parallelize tốt.

Algorithm dependency structure phải cho phép independent work.

## `String` và Unicode

Java `String` indexing/`charAt` làm việc theo UTF-16 code units, không guaranteed Unicode code points/graphemes.

String DSA production phải xác định unit.

For code points:

```java
s.codePoints()
```

nhưng converting/storing code points có memory/performance implications.

## StringBuilder

Repeated string concatenation trong loop có thể tạo nhiều temporary strings.

Use `StringBuilder` khi constructing mutable output sequence.

Đây là data-structure choice: dynamic character buffer vs immutable copy chain.

## Memory footprint và object headers

Một node object không chỉ chứa fields; JVM object header/alignment/reference width thêm overhead.

Millions of tiny `Node` objects có thể consume far more memory than raw field sum.

Arrays/flat representations often reduce overhead significantly.

Exact bytes depend JVM configuration; measure rather than assume fixed header size.

## Escape analysis và JIT

JIT có thể scalar-replace/eliminate some allocations nếu objects don't escape, nhưng không nên design correctness/performance based on assuming a specific optimization will occur.

Use profiler/JFR/JMH to observe.

## JMH cho microbenchmark

Java microbenchmark rất dễ sai do JIT warm-up, dead-code elimination và constant folding.

JMH giúp handle warm-up/forks/blackholes.

Không benchmark collection bằng một `System.nanoTime()` loop rồi kết luận global performance.

## GC pressure

Object-heavy graph/PQ workloads tạo many short-lived objects.

GC may handle them efficiently, nhưng extreme allocation rate still affects latency/throughput.

Alternatives:

```text
primitive arrays
object reuse/pooling carefully
compact immutable records only where readability matters
```

Pooling ordinary short-lived Java objects đôi khi làm GC worse; measure.

## Fail-fast vs thread-safe

Fail-fast iterator phát hiện structural modification best-effort; không làm collection thread-safe.

Synchronized wrapper:

```java
Collections.synchronizedList(...)
```

có coarse semantics, nhưng iteration vẫn cần external synchronization per contract.

Concurrent collection choice cần đọc semantics cụ thể.

## Immutability và persistent data structures

JDK core collections chủ yếu mutable, nhưng immutable/persistent structures có thể hữu ích cho snapshots/versioning/concurrency.

Persistent tree path-copying reuse unchanged subtrees.

Trade-off là allocations + different constants.

## Null semantics

Different collections have different null policies. `ArrayDeque` không cho null elements. Some maps permit null keys/values; concurrent collections often differ.

Nếu algorithm dùng `null` làm sentinel, collection contract có thể conflict.

Prefer explicit state where ambiguity matters.

## Reference equality vs logical equality

`==` trên objects compare references; `.equals` compare logical equality theo class contract.

Graph/state algorithms dùng wrong equality có thể break visited/dedup.

For enums, `==` is appropriate due singleton constants; for value objects, usually `.equals`/records.

## Defensive copying

Nếu API nhận mutable array/list và lưu reference, caller có thể mutate structure unexpectedly.

Options:

```text
borrow and document
copy on input
immutable view/snapshot
```

Choice affects memory and semantics.

## Collection selection checklist

```text
Need random index?          -> ArrayList / array
Need stack/queue/deque?     -> ArrayDeque
Need exact key lookup?      -> HashMap/HashSet
Need sorted/range lookup?   -> TreeMap/TreeSet
Need min/max repeatedly?    -> PriorityQueue
Need dense integer keys?    -> arrays/BitSet
Need thread-safe mapping?   -> ConcurrentHashMap after semantics review
Need blocking producer-consumer? -> BlockingQueue
```

Đây là starting point, không thay workload profiling.

## Testing custom DSA in Java

Use reference JDK structure khi có thể.

Custom heap:

```text
random pushes/pops
compare pop sequence với sorted ArrayList
```

Custom BST:

```text
compare set/order behavior với TreeSet/TreeMap
```

Custom hash map:

```text
compare semantics với HashMap trên random operations
```

Property/invariant tests vẫn quan trọng.

## Assertions và validators

Debug builds/tests có thể call:

```java
assert validateHeap();
assert validateTree();
```

Java `assert` có thể disabled runtime; production validation không nên dựa vào it implicitly.

JUnit/property-testing frameworks phù hợp hơn cho automated tests.

## Profiling

JFR, async-profiler, VisualVM/JMC hoặc profiler khác giúp thấy:

```text
allocation hotspots
CPU hotspots
GC pressure
lock contention
```

Không optimize collection choice chỉ bằng intuition.

## Common misconceptions

“Java Collections tự chọn implementation tối ưu” — sai; caller chọn concrete type.

“LinkedList insert/delete O(1) nên tốt hơn ArrayList” — thiếu traversal/locality context.

“ConcurrentHashMap = HashMap nhanh hơn” — sai; nó cung cấp concurrency semantics với coordination cost.

“PriorityQueue object priority mutate thì heap tự update” — sai.

“GC nghĩa là không có memory leak” — sai nếu references vẫn reachable.

“Streams làm code O(n) thành nhanh hơn” — abstraction không thay asymptotic cost.

“TreeMap key uniqueness dùng equals giống HashMap” — ordered comparator semantics khác.

## Mental Model

> Java Collections là **DSA contracts được đóng gói trong framework**. Chúng giảm lượng code tự viết nhưng không giảm trách nhiệm chọn đúng representation. Hiểu Java DSA nghĩa là biết operation semantics, complexity, equality/comparator contract, boxing, GC reachability và runtime allocation behavior.

Khi chọn collection, hãy hỏi:

```text
Operation nào dominant?
Need order hay chỉ identity?
Key/value có immutable không?
Primitive array có đủ không?
Dataset lớn tới mức object overhead đáng kể không?
Concurrency semantics có thật sự cần không?
Iterator/reference invalidation/view semantics thế nào?
```

Sau đó mới chọn `ArrayList`, `HashMap`, `TreeMap`, `PriorityQueue` hay custom structure.

Xem thêm: [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md), [Cross-language Testing](./03_cross_language_testing_and_benchmarking.md).