# Queue, Deque và Priority Queue
**큐, 덱, 우선순위 큐**

Ba cấu trúc này đều quản lý “frontier” hoặc các phần tử đang chờ, nhưng khác ở quy tắc chọn phần tử tiếp theo.

## Queue: FIFO

Queue dùng **FIFO — First In, First Out / 선입선출**. Request đến trước được xử lý trước. BFS dùng queue để đảm bảo node ở distance nhỏ hơn được mở rộng trước.

Java:

```java
Queue<Integer> q = new ArrayDeque<>();
q.offer(10);
q.offer(20);
int x = q.poll();
```

Trong JavaScript, dùng `Array.shift()` liên tục có thể gây reindex/shift. Với workload lớn, nên dùng head index hoặc queue implementation riêng:

```js
class Queue {
  constructor() { this.a = []; this.head = 0; }
  enqueue(x) { this.a.push(x); }
  dequeue() {
    if (this.head >= this.a.length) return undefined;
    return this.a[this.head++];
  }
}
```

Production implementation cần compaction định kỳ để tránh giữ backing array quá lớn.

## Circular buffer

Fixed-size queue có thể dùng array + `head` + `tail`. Khi index tới cuối array, quay lại đầu bằng modulo:

\[
next=(i+1)\bmod capacity
\]

Nhờ đó enqueue/dequeue không phải dịch elements.

## Deque

**Double-Ended Queue (Deque / 덱)** cho insert/delete ở cả hai đầu. Nó có thể đóng vai stack hoặc queue. Sliding-window maximum thường dùng **monotonic deque**, giữ candidates theo value giảm dần và loại index đã ra ngoài window.

## Priority Queue

Priority queue không hỏi “ai đến trước?” mà hỏi “ai có priority cao nhất/thấp nhất?”. Implementation phổ biến nhất là binary heap.

Java:

```java
PriorityQueue<Integer> pq = new PriorityQueue<>();
pq.offer(30);
pq.offer(10);
pq.offer(20);
System.out.println(pq.poll()); // 10
```

JavaScript không có general-purpose `PriorityQueue` built-in chuẩn, nên thường tự implement heap hoặc dùng library.

## Mental Model

> Queue chọn theo thời gian đến; deque cho thao tác hai biên; priority queue chọn theo score/priority.

Selection policy không phải chi tiết phụ — nó quyết định property của algorithm. BFS đúng cho shortest path unweighted chính vì queue tạo layer order.

## Ring buffer invariant

Một circular queue fixed-capacity thường có `head`, `size`, `capacity`; tail có thể suy ra:

\[
tail=(head+size)\bmod capacity
\]

Dùng `size` giúp phân biệt empty và full dù `head == tail` có thể xảy ra ở cả hai state nếu chỉ giữ hai indices.

C sketch:

```c
typedef struct {
    int *a;
    size_t cap, head, size;
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

Ring buffer rất tự nhiên cho networking/audio/telemetry buffers vì memory bounded và không cần shift.

## Deque và 0–1 BFS

Deque không chỉ là “queue hai đầu”. 0–1 BFS khai thác nó như priority queue hai mức: edge weight 0 đưa node lên front, weight 1 đưa xuống back. Vì chỉ có hai priority increments, deque đủ để giữ processing order mà không cần heap.

## Priority queue không phải sorted list

Một sorted array có minimum `O(1)` nhưng insert `O(n)`. Heap giữ partial order để insert/extract `O(log n)`. Nếu workload là “insert nhiều, thỉnh thoảng lấy min”, heap có trade-off tốt hơn duy trì full sorted order.

## Bounded queue và backpressure

Trong systems, queue vô hạn chỉ chuyển overload thành memory exhaustion. Bounded queue buộc hệ thống định nghĩa behavior khi full: block producer, reject, drop oldest/newest hoặc spill to disk. Đây là nơi data structure capacity trở thành application-level reliability policy.

## Java API semantics

`Queue.add` có thể throw khi không thêm được; `offer` thường biểu diễn failure bằng boolean. `remove/element` throw khi empty; `poll/peek` trả `null` theo contract. Chọn method pair phù hợp làm error handling rõ hơn.

Với `ArrayDeque`, `null` không được dùng như element, giúp `poll()==null` mang nghĩa empty không mơ hồ.
