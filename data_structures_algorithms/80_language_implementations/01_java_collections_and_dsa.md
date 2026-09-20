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
