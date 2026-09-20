# Java Collections nhìn dưới góc DSA
**Java Collections와 자료구조 선택**

Java Collections Framework cung cấp abstractions mạnh, nhưng dùng đúng đòi hỏi hiểu implementation cost.

## Interface trước implementation

`List`, `Set`, `Map`, `Queue`, `Deque`, `NavigableMap` biểu diễn behavioral contracts. `ArrayList`, `HashSet`, `HashMap`, `ArrayDeque`, `PriorityQueue`, `TreeMap` là implementation choices.

Code API-level nên phụ thuộc interface khi hợp lý, nhưng performance-sensitive code vẫn phải biết implementation thật.

## ArrayList vs LinkedList

`ArrayList` thường là default list vì random access, locality và low per-element overhead. `LinkedList` chỉ đáng cân nhắc khi workload thực sự cần node-based operations và đã có iterator/node position phù hợp; index-based repeated access rất đắt.

## ArrayDeque

Cho stack/queue general-purpose, `ArrayDeque` thường phù hợp hơn legacy `Stack` và nhiều use cases của `LinkedList`.

```java
Deque<Integer> dq = new ArrayDeque<>();
dq.push(1);      // stack style
dq.pop();
dq.offerLast(2); // queue style
dq.pollFirst();
```

## HashMap keys

Key nên có `equals/hashCode` consistent và thực tế nên immutable theo fields tham gia equality/hash. Record thường tiện cho compound keys:

```java
record Pair(int x, int y) {}
```

## Primitive boxing

`List<Integer>` lưu boxed values; `int[]` lưu primitives. Trong hot loops hoặc large data, boxing ảnh hưởng memory và GC. Standard Java collections không có primitive-specialized generic collections; có thể dùng arrays hoặc specialized libraries khi cần.

## PriorityQueue comparator

Tránh subtraction comparator nếu overflow có thể xảy ra:

```java
Comparator.comparingInt(Node::priority)
```

hoặc `Integer.compare(a,b)`.

## TreeMap/NavigableMap

Khi cần floor/ceiling/range views, `TreeMap` thể hiện ordered-map semantics tốt hơn cố ép HashMap + sorting liên tục.

## Concurrent collections không phải drop-in performance replacement

`ConcurrentHashMap`, blocking queues và concurrent structures thêm synchronization/coordination semantics. Chọn chúng vì concurrency requirement, không vì tên nghe “mạnh hơn”.

## Mental Model

> Java Collections che implementation syntax, không che **complexity contract**. Dùng framework đúng là map workload tới đúng abstraction và implementation.

## Complexity table thực dụng

| Abstraction | Implementation thường dùng | Operation cần nhớ |
|---|---|---|
| `List` | `ArrayList` | `get` O(1), append amortized O(1), middle insert O(n) |
| `Deque` | `ArrayDeque` | operations hai đầu amortized O(1) |
| `Map` | `HashMap` | expected get/put O(1), không sorted |
| `NavigableMap` | `TreeMap` | O(log n), floor/ceiling/range |
| `Set` | `HashSet` | expected membership O(1) |
| ordered set | `TreeSet` | O(log n), sorted |
| priority queue | `PriorityQueue` | peek O(1), add/poll O(log n) |

Bảng này không thay documentation/version-specific detail, nhưng nó là baseline để tránh chọn collection theo tên quen thuộc.

## `HashMap` và mutable keys

```java
record Key(int userId, int productId) {}
```

Record là lựa chọn tốt khi fields thật sự tạo identity và immutable. Nếu dùng object mutable làm key rồi sửa field tham gia `equals/hashCode`, map có thể không tìm key theo expected bucket/equality semantics.

## `computeIfAbsent` và graph building

Adjacency map:

```java
Map<String, List<String>> g = new HashMap<>();

g.computeIfAbsent(u, k -> new ArrayList<>()).add(v);
```

API này tiện nhưng lambda/allocation vẫn có cost; trong hot code cần profile chứ không đoán.

## Primitive arrays cho algorithms

Dijkstra, DP, DSU thường dùng:

```java
long[] dist;
int[] parent;
boolean[] seen;
```

thay `List<Long>`/`List<Integer>` khi size biết trước. Điều này giảm boxing, object/reference overhead và làm random access rõ hơn.

## `PriorityQueue` không tự update priority

Nếu object đã nằm trong queue và field priority thay đổi, heap không tự reheapify. Dijkstra thường push state mới rồi bỏ stale entry khi pop, hoặc implement indexed heap riêng.

## `equals`, comparator và consistency

Sorted sets/maps xác định uniqueness/order theo comparator hoặc natural ordering, không nhất thiết theo `equals` trong mọi tình huống. Comparator nên tạo ordering nhất quán với semantics key; nếu comparator trả 0 cho hai objects mà domain coi khác nhau, `TreeSet/TreeMap` có thể coi chúng là cùng key-order position.

## Streams không thay complexity reasoning

Java Stream có thể làm code declarative, nhưng `sorted()`, `distinct()`, grouping và repeated terminal operations vẫn có data-structure/algorithm cost. API abstraction không làm Big-O biến mất.

## Mental Model mở rộng

> Học DSA trong Java có hai lớp: hiểu structure abstract, rồi biết collection nào của JDK thực sự cung cấp operation đó với semantics và cost nào.
