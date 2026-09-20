# Queue, Deque và Priority Queue
**큐, 덱, 우선순위 큐**

Queue, deque và priority queue đều quản lý một tập phần tử “đang chờ được xử lý”, nhưng khác nhau ở **selection policy / 선택 정책**: phần tử nào sẽ được lấy ra tiếp theo. Sự khác biệt tưởng nhỏ này quyết định trực tiếp correctness của nhiều algorithms. BFS cần FIFO để giữ layer order; Dijkstra cần minimum-priority extraction; sliding-window maximum cần một deque giữ candidates theo cả thời gian và value order.

Vì vậy không nên xem queue chỉ là một container có `enqueue/dequeue`. Nó là một abstraction về **thứ tự phục vụ (service order)**.

## Queue: FIFO và time order

**Queue / 큐** dùng FIFO — First In, First Out / 선입선출. Phần tử vào trước được lấy ra trước.

Java:

```java
Queue<Integer> q = new ArrayDeque<>();
q.offer(10);
q.offer(20);
System.out.println(q.poll()); // 10
```

Cốt lõi của queue không phải syntax mà là invariant:

```text
mọi phần tử còn trong queue xuất hiện theo đúng thứ tự enqueue chưa được dequeue
```

FIFO rất phù hợp cho request processing, event buffering, task scheduling theo arrival order và BFS.

## Tại sao BFS cần queue?

Trong unweighted graph, BFS khám phá nodes theo distance layers. Khi node distance `d` được dequeue, mọi node đã enqueue trước nó có distance `<= d`, và neighbors mới được enqueue với distance `d+1`.

Queue giữ exact ordering cần cho proof shortest path theo số edges. Nếu thay queue bằng stack, algorithm trở thành DFS và mất layer guarantee. Nếu thay bằng min-heap theo một custom score, ta đã đổi search semantics.

Đây là một ví dụ quan trọng: **data structure của frontier là một phần của algorithmic proof**, không chỉ là implementation detail.

## Queue interface và empty/full semantics

Một queue API nên xác định rõ:

```text
enqueue khi full làm gì?
dequeue khi empty trả gì?
queue có bounded capacity không?
null/None có được dùng làm value hợp lệ không?
operation có block hay non-blocking?
```

Trong Java, `Queue.add` và `offer` khác error semantics; `remove/element` có thể throw khi empty, trong khi `poll/peek` trả `null` theo contract. Với `ArrayDeque`, `null` không được phép làm element, giúp `poll()==null` biểu diễn empty rõ ràng.

Trong C, API thường dùng boolean + output pointer:

```c
bool queue_pop(Queue *q, Item *out);
```

để tránh dùng magic sentinel trùng với data domain.

## Array queue và vấn đề shift

Naive array queue có thể enqueue ở cuối và khi dequeue thì shift toàn bộ elements sang trái. Điều này biến dequeue thành `O(n)`.

Cách tốt hơn là giữ `head` index. JavaScript example:

```js
class Queue {
  constructor() {
    this.a = [];
    this.head = 0;
  }

  enqueue(x) {
    this.a.push(x);
  }

  dequeue() {
    if (this.head === this.a.length) return undefined;
    const x = this.a[this.head++];

    if (this.head > 4096 && this.head * 2 > this.a.length) {
      this.a = this.a.slice(this.head);
      this.head = 0;
    }
    return x;
  }
}
```

Head-index tránh shift mỗi lần, nhưng cần compaction định kỳ để backing array không giữ references/space cũ quá lâu.

## Circular buffer / ring buffer

**Circular buffer / 원형 버퍼** dùng fixed array và wrap indices về đầu.

Một representation rõ ràng giữ:

```text
capacity
head
size
```

Tail suy ra:

\[
tail=(head+size)\bmod capacity
\]

C implementation:

```c
typedef struct {
    int *a;
    size_t cap;
    size_t head;
    size_t size;
} RingQueue;

bool enqueue(RingQueue *q, int x) {
    if (q->size == q->cap) return false;

    size_t tail = (q->head + q->size) % q->cap;
    q->a[tail] = x;
    q->size++;
    return true;
}

bool dequeue(RingQueue *q, int *out) {
    if (q->size == 0) return false;

    *out = q->a[q->head];
    q->head = (q->head + 1) % q->cap;
    q->size--;
    return true;
}
```

Dùng `size` giải quyết ambiguity khi `head == tail`, trạng thái này nếu chỉ giữ hai indices có thể biểu diễn cả empty lẫn full tùy convention.

## Power-of-two capacity và masking

Nếu capacity luôn là power of two, wrap có thể dùng bitmask:

```text
index & (capacity - 1)
```

thay modulo trong một số low-level implementations. Tuy nhiên đây là optimization representation; correctness vẫn dựa trên invariant `capacity` là power of two.

Không nên áp dụng trick này nếu capacity arbitrary.

## Ring buffer trong systems

Ring buffer rất tự nhiên cho audio, networking, telemetry, logging pipeline và producer-consumer systems vì memory bounded và access contiguous.

Một bounded ring buffer buộc system định nghĩa overload policy. Khi full, có thể:

```text
block producer
reject item
return failure
overwrite/drop oldest
drop newest
spill elsewhere
```

Đây không còn là chi tiết DSA; nó trở thành reliability/backpressure policy của application.

## Backpressure

Queue vô hạn không giải quyết overload; nó chỉ biến overload thành memory growth và latency tăng dần.

Nếu producer rate `λ` lâu dài lớn hơn consumer service rate `μ`, queue length có xu hướng tăng. Bounded queue ép system phản ứng sớm: block, shed load hoặc scale capacity/service.

Mental model quan trọng:

> Queue hấp thụ burst ngắn hạn; nó không thể chữa throughput deficit dài hạn.

## Little's Law connection

Trong steady state, queueing systems thường dùng intuition của Little's Law:

\[
L=\lambda W
\]

trong đó `L` là average items trong system, `λ` throughput và `W` average time in system.

Không cần biến DSA chapter thành queueing theory, nhưng connection này cho thấy tăng queue capacity không tự giảm latency; queue dài thường đồng nghĩa wait time dài.

## Deque: thao tác ở cả hai đầu

**Double-Ended Queue (Deque / 덱)** hỗ trợ push/pop ở front và back.

```text
pushFront
pushBack
popFront
popBack
peekFront
peekBack
```

Deque có thể mô phỏng stack hoặc queue, nhưng giá trị lớn nhất của nó xuất hiện khi algorithm thực sự cần **hai-ended policy**, không chỉ để có API tiện.

## Array deque và ring representation

Một array deque thường là ring buffer động. Khi push front, head lùi modulo capacity; push back ghi ở tail. Khi full, grow backing array và copy logical order sang buffer mới.

Invariant quan trọng là logical order độc lập với physical wrap. Iterator/resize code phải hiểu rằng elements có thể nằm ở hai physical segments:

```text
[tail segment ........] [........ head segment]
```

## Monotonic deque

Sliding-window maximum là use case kinh điển.

Deque giữ indices sao cho:

```text
index tăng từ front tới back
value giảm từ front tới back
```

Khi thêm index `i`, pop back mọi index có value `<= a[i]`. Vì `i` mới hơn và không nhỏ hơn, các elements đó sẽ hết hạn sớm hơn `i` và không bao giờ trở thành maximum trong future windows chứa cả hai.

Sau đó pop front nếu index đã ra ngoài window. Front luôn là maximum.

```java
Deque<Integer> dq = new ArrayDeque<>();

for (int i = 0; i < a.length; i++) {
    while (!dq.isEmpty() && dq.peekFirst() <= i - k) {
        dq.pollFirst();
    }

    while (!dq.isEmpty() && a[dq.peekLast()] <= a[i]) {
        dq.pollLast();
    }

    dq.offerLast(i);

    if (i >= k - 1) {
        answer.add(a[dq.peekFirst()]);
    }
}
```

Mỗi index vào deque một lần và ra tối đa một lần, nên total time `O(n)`.

Đây là amortized analysis rất đẹp: inner `while` không làm algorithm `O(n^2)` vì mỗi element bị pop chỉ một lần.

## Monotonic queue như compressed candidate set

Monotonic deque không lưu mọi element trong window. Nó chỉ giữ những element vẫn có khả năng trở thành answer tương lai.

Một element nhỏ hơn một element mới hơn bị **dominated**: nó vừa yếu hơn về value, vừa hết hạn sớm hơn. Vì thế có thể loại vĩnh viễn.

Mental model này xuất hiện ở nhiều algorithms: giữ Pareto-like frontier và xóa states bị dominated.

## Deque và 0–1 BFS

Nếu edge weights chỉ `0` hoặc `1`, Dijkstra với heap đúng nhưng nặng hơn cần thiết.

0–1 BFS dùng deque:

```text
weight 0 -> push front
weight 1 -> push back
```

Node có candidate distance không tăng được ưu tiên trước. Vì distance increment chỉ có hai mức, deque giữ đủ ordering để đạt `O(V+E)`.

Deque ở đây hoạt động như một priority queue đặc biệt với priority differences bị giới hạn.

## Priority Queue là ADT, heap chỉ là một implementation

**Priority Queue (우선순위 큐)** hỗ trợ operations kiểu:

```text
insert(item, priority)
peek-min / peek-max
extract-min / extract-max
```

Binary heap là implementation phổ biến vì balance giữa memory compact và `O(log n)` update. Nhưng priority queue còn có thể dùng balanced tree, bucket queue, radix heap, pairing heap, Fibonacci heap hoặc specialized structures tùy workload.

Không nên đồng nhất “priority queue” với “heap”.

## Priority không nhất thiết là một số duy nhất

Comparator có thể dùng nhiều fields:

```text
primary: deadline sớm hơn
secondary: priority class cao hơn
tertiary: sequence number nhỏ hơn để FIFO trong cùng priority
```

Tie-breaking là semantics. Nếu scheduler cần stable order trong cùng priority mà comparator bỏ sequence number, behavior có thể nondeterministic hoặc phụ thuộc heap shape.

## Binary heap recap

Binary heap giữ partial order:

```text
min-heap: parent <= children
```

`peek` `O(1)`, insert và extract `O(log n)`, build heap bottom-up `O(n)`.

Heap không sorted toàn bộ; arbitrary search có thể `O(n)`. Đây là intentional trade-off: chỉ maintain đủ order cho extreme extraction.

Chi tiết implementation sâu hơn xem [Heap](../02_trees/03_heaps.md).

## Mutable priority là một correctness trap

Nếu object đã ở Java `PriorityQueue` rồi field dùng trong comparator bị sửa, heap không tự reheapify.

```java
state.priority = 1; // queue không biết cần di chuyển state
```

Do đó Dijkstra thường push entry mới và bỏ stale entry khi poll:

```java
if (cur.dist() != dist[cur.node()]) continue;
```

Hoặc implement indexed heap hỗ trợ decrease-key thật sự.

## Indexed priority queue

Nếu cần update priority theo item identity thường xuyên, giữ mapping:

```text
item -> heap index
```

Mỗi swap phải cập nhật position map. Decrease/increase-key sau đó có thể sift đúng direction trong `O(log n)`.

Đổi lại implementation phức tạp hơn và có thêm cross-invariant:

```text
position[heap[i].item] == i
```

## Lazy deletion / stale-entry pattern

Nhiều standard APIs không hỗ trợ remove/update arbitrary entry hiệu quả. Một pattern phổ biến là không xóa entry cũ ngay; thêm entry mới và khi pop thì kiểm tra entry còn current không.

Pattern này đơn giản hóa code nhưng heap có thể phình lớn. Cost thực tế phụ thuộc số updates/stale entries và memory budget.

## Bucket queue và bounded integer priorities

Nếu priorities là small bounded integers, heap `O(log n)` có thể không cần. Ta có thể giữ array/buckets theo priority và tìm bucket non-empty tiếp theo.

Dial's algorithm cho shortest paths với bounded non-negative integer weights khai thác idea này.

Đây là một pattern chung:

> Constraint trên key/priority domain có thể cho structure đơn giản hơn comparison-based priority queue.

## Radix heap intuition

Radix heap khai thác monotonic extracted keys trong một số shortest-path workloads với integer distances. Nó group keys theo bit-prefix/distance ranges thay vì heap binary comparison.

Không cần dùng thường xuyên, nhưng nó minh họa rằng priority queue design phụ thuộc key structure và monotonicity assumptions.

## Stable priority queue

Heap thường không stable. Nếu two items có equal priority và application cần FIFO tie-break, thêm sequence number tăng dần:

```text
(priority, sequence)
```

Comparator sort theo priority trước, sequence sau.

Đây là ví dụ representation thêm metadata để encode semantics application-level.

## Top-K và bounded priority queue

Nếu stream có `N` items nhưng chỉ cần `k` lớn nhất, giữ min-heap size `k`:

```text
nếu heap size < k -> insert
nếu x > min -> replace min
nếu không -> bỏ x
```

Time:

\[
O(N\log k)
\]

memory `O(k)`. Đây là một cách dùng priority queue như compressed frontier của current best candidates.

## K-way merge

Có `k` sorted streams. Đưa head mỗi stream vào min-priority queue. Mỗi lần extract smallest, advance đúng stream đó.

Nếu tổng `N` elements:

\[
O(N\log k)
\]

Đây là nền tảng của external merge sort, log compaction và distributed merge pipelines.

## Scheduling và starvation

Priority scheduler luôn chọn high priority có thể làm low-priority tasks chờ vô hạn nếu high-priority work liên tục tới. Đây gọi là starvation.

Systems thường thêm aging, quotas hoặc multi-level policies để cân bằng priority với fairness.

DSA abstraction không tự giải fairness; scheduler policy phải encode requirement này.

## Multiple queues và work stealing

Concurrent schedulers đôi khi dùng per-worker deques. Worker xử lý local tasks một đầu để giữ locality; idle worker “steal” từ đầu kia của worker khác.

Work-stealing deque là một ví dụ nơi deque semantics kết hợp concurrency protocol và locality. Implementation lock-free thực tế phức tạp hơn deque textbook rất nhiều.

## Blocking queues

Concurrent producer-consumer system cần semantics khi empty/full:

```text
take() block khi empty
put() block khi full
```

Java `BlockingQueue` family cung cấp contracts này. Đây là ADT khác queue non-blocking thường dùng trong algorithms.

Khi chọn API phải phân biệt **data order** và **coordination semantics**.

## Memory visibility và thread safety

Một queue đúng single-thread không tự trở thành thread-safe khi thêm locks tùy tiện. Concurrent queue correctness cần đảm bảo linearization point và visibility giữa producer/consumer.

Low-level ring buffers có thể dùng atomics, sequence numbers và memory ordering. Đây là phần systems/concurrency, nhưng mental model vẫn là giữ queue invariant trong mọi allowed interleaving.

## Queue persistence và functional queues

Trong functional programming, queue persistent có thể được tạo từ hai lists/stacks: một list cho front và một list reversed cho rear. Khi front empty, reverse rear.

Với amortized analysis, operations vẫn có thể constant amortized trong model phù hợp. Đây là ví dụ cùng FIFO ADT nhưng representation hoàn toàn khác imperative ring buffer.

## Choosing the right frontier structure

Một useful map:

| Requirement | Frontier structure tự nhiên |
|---|---|
| arrival order | FIFO queue |
| LIFO exploration | stack |
| thao tác hai đầu | deque |
| max/min theo score | priority queue |
| two-level 0/1 priority | deque |
| small bounded integer priorities | bucket queue |
| sliding-window dominated candidates | monotonic deque |

Điều cần nhớ là **selection policy** chứ không phải table.

## Common failure modes

Dùng `Array.shift()` cho queue JavaScript lớn có thể tạo unnecessary movement/runtime cost.

Ring buffer không phân biệt full/empty đúng sẽ overwrite hoặc underflow.

Priority queue với mutable key có thể silently phá heap ordering.

Comparator không transitive có thể phá priority semantics.

Unbounded queue dưới overload có thể gây memory exhaustion.

Monotonic deque lưu values thay vì indices có thể không biết element nào đã expired khi duplicates xuất hiện.

## Testing strategy

Queue/deque có thể test bằng reference `List` nhỏ với random operation sequences. Ring buffer cần đặc biệt test wrap-around nhiều lần, full/empty transitions và resize nếu dynamic.

Priority queue nên insert random values rồi poll toàn bộ, kiểm tra output nondecreasing. Indexed heap cần validator cho heap-order và position-map consistency.

Monotonic deque có thể differential-test sliding-window results với brute-force `O(nk)` trên arrays nhỏ.

## Mental Model

> Queue family không chủ yếu khác nhau ở nơi insert/delete; chúng khác ở **quy tắc chọn phần tử tiếp theo**. FIFO giữ time order, deque cho điều khiển hai biên, priority queue giữ best score, monotonic deque giữ chỉ các candidates chưa bị dominated.

Khi một algorithm có “frontier”, hãy hỏi: **frontier phải được phục vụ theo thứ tự nào để proof đúng?** Câu trả lời thường cho biết nên dùng queue, stack, deque, heap hay một structure chuyên biệt hơn.

Xem tiếp: [Stacks](./02_stacks.md), [Heap](../02_trees/03_heaps.md), [Graph Traversal](../03_graphs/01_graph_traversal_bfs_dfs.md), [Shortest Paths](../03_graphs/02_shortest_paths.md) và [Selection & Top-K](../04_algorithmic_paradigms/06_selection_and_top_k.md).
