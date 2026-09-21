# Queue, Deque và hàng đợi ưu tiên
**Queue, Deque & Priority Queue / 큐, 덱, 우선순위 큐**

Queue, deque và priority queue đều quản lý một tập phần tử “đang chờ”, nhưng khác nhau ở **chính sách chọn phần tử tiếp theo (selection policy)**. Khác biệt tưởng nhỏ này lại quyết định trực tiếp tính đúng đắn của nhiều thuật toán.

BFS cần FIFO để bảo toàn thứ tự theo tầng. Dijkstra cần phần tử có tentative distance nhỏ nhất. Sliding-window maximum cần deque duy trì đồng thời thứ tự thời gian và quan hệ ưu thế về giá trị.

Vì vậy queue không chỉ là một container; nó là một abstraction về **thứ tự phục vụ**.

## Queue và nguyên tắc FIFO

Queue dùng nguyên tắc **vào trước, ra trước (First In, First Out – FIFO / 선입선출)**.

```java
Queue<Integer> q = new ArrayDeque<>();
q.offer(10);
q.offer(20);
System.out.println(q.poll()); // 10
```

Bất biến logic:

> Các phần tử còn trong queue xuất hiện theo đúng thứ tự enqueue chưa bị dequeue.

Đây là lý do queue phù hợp với request arrival order, event processing, producer–consumer pipeline và BFS.

## Vì sao BFS cần FIFO?

Trong graph không trọng số, mỗi cạnh tăng độ dài đường đi thêm đúng 1. Khi BFS lấy một node có distance `d`, các node đã được discover trước nó có distance không lớn hơn `d`; các neighbor mới được thêm với distance `d+1`.

FIFO bảo đảm frontier được xử lý theo lớp khoảng cách không giảm.

Nếu thay queue bằng stack, ta có DFS và mất shortest-path guarantee theo số cạnh. Nếu thay bằng min-heap theo weight, ta chuyển sang một policy gần Dijkstra.

Do đó cấu trúc frontier không phải chi tiết implementation; nó là một phần của proof.

## Queue API cũng là một contract

Một queue thực tế phải định nghĩa rõ:

```text
enqueue khi đầy làm gì?
dequeue khi rỗng làm gì?
capacity có cố định không?
operation có block không?
null có phải một giá trị hợp lệ không?
queue có thread-safe không?
iteration có snapshot hay live view?
```

Trong Java, `offer` và `add` có semantics khác khi queue từ chối phần tử; `poll/peek` khác `remove/element` khi queue rỗng.

Trong C, một API rõ thường dùng:

```c
bool queue_pop(Queue *q, Item *out);
```

thay vì dùng magic sentinel có thể trùng dữ liệu thật.

## Vì sao shift mảng là thiết kế queue kém?

Nếu dequeue luôn dịch toàn bộ phần tử còn lại sang trái, mỗi lần dequeue tốn `O(n)`.

Cách tốt hơn là giữ `head` index:

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

Head-index tránh shift mỗi operation, nhưng cần compaction nếu runtime vẫn giữ references cũ trong backing array quá lâu.

## Ring buffer

**Bộ đệm vòng (ring buffer / 원형 버퍼)** dùng một mảng và cho chỉ số quay lại đầu khi chạm cuối.

Một representation dễ reasoning giữ:

```text
capacity
head
size
```

Tail được suy ra:

\[
tail=(head+size)\bmod capacity
\]

```c
typedef struct {
    int *a;
    size_t cap;
    size_t head;
    size_t size;
} RingQueue;
```

Bất biến:

```text
0 <= size <= cap
head < cap khi cap > 0
phần tử logic thứ i nằm tại (head + i) mod cap
```

Dùng `size` giúp phân biệt rõ trạng thái rỗng và đầy khi `head == tail`.

## Nhiều convention của ring buffer

Có ít nhất ba cách phổ biến:

```text
head + size
head/tail và chừa một slot rỗng
head/tail + cờ full
```

Không có convention duy nhất đúng. Sai lầm thường đến từ việc trộn hai convention trong cùng implementation.

Một proof tốt phải xác định chính xác:

```text
head trỏ phần tử đầu hay slot trống kế tiếp?
tail trỏ phần tử cuối hay slot trống kế tiếp?
full được nhận biết bằng gì?
```

## Capacity là lũy thừa của hai

Nếu `capacity = 2^k`, phép wrap có thể dùng:

```text
index & (capacity - 1)
```

thay modulo.

Nhưng tối ưu này chỉ đúng nếu invariant “capacity luôn là lũy thừa của hai” được giữ qua mọi resize.

Đây là mẫu chung: optimization bit-level thường tạo thêm một invariant cấu trúc.

## Bounded queue và overload policy

Queue có capacity hữu hạn buộc hệ thống trả lời câu hỏi: chuyện gì xảy ra khi đầy?

```text
block producer
reject item
drop newest
drop oldest
overwrite oldest
spill sang disk
scale consumer
```

Đây không còn là chuyện container thuần túy; nó trở thành policy về reliability và backpressure.

## Queue không chữa được throughput deficit dài hạn

Giả sử tốc độ đến trung bình là `λ` và tốc độ xử lý trung bình là `μ`.

Nếu trong thời gian dài:

\[
\lambda > \mu
\]

thì queue có xu hướng dài ra. Queue lớn chỉ trì hoãn hậu quả bằng cách đổi overload thành memory growth và latency growth.

Mô hình tư duy:

> Queue hấp thụ burst ngắn hạn; nó không tạo thêm năng lực xử lý dài hạn.

## Little's Law

Trong trạng thái ổn định, một trực giác quan trọng của queueing theory là:

\[
L=\lambda W
\]

trong đó:

```text
L = số item trung bình trong hệ thống
λ = throughput
W = thời gian trung bình một item ở trong hệ thống
```

Nếu throughput không đổi mà queue length tăng, thời gian chờ trung bình cũng tăng.

Tăng capacity không tự giảm latency; nó chỉ cho phép nhiều item chờ hơn.

## Queue và batching

Một consumer có thể xử lý từng item hoặc gom batch.

Batching có thể giảm overhead cố định trên mỗi item, ví dụ network syscall, disk write hoặc database transaction. Nhưng batch lớn thường tăng latency vì item đầu phải chờ batch đủ hoặc timeout.

Đây là một trade-off hệ thống:

```text
batch lớn -> throughput tốt hơn, latency thường cao hơn
batch nhỏ -> latency tốt hơn, overhead trên mỗi item cao hơn
```

Queue là nơi policy batching thường được thực hiện.

## Deque

**Double-Ended Queue (Deque / 덱)** hỗ trợ thao tác ở cả hai đầu:

```text
pushFront
pushBack
popFront
popBack
peekFront
peekBack
```

Deque có thể dùng như stack hoặc queue, nhưng sức mạnh thật xuất hiện khi thuật toán cần hai đầu với vai trò khác nhau.

## Deque bằng ring buffer động

Một array deque thường dùng ring buffer có thể resize.

Về logic, sequence là liên tục. Về vật lý, nó có thể bị chia thành hai đoạn:

```text
[tail segment .........] [......... head segment]
```

Resize phải copy theo **thứ tự logic**, không phải đơn giản copy vùng nhớ từ index 0 tới cuối.

Đây là một ví dụ representation vật lý khác với thứ tự abstraction.

## Monotonic deque

Sliding-window maximum là ví dụ kinh điển.

Deque giữ index với hai invariant:

```text
index tăng từ front tới back
giá trị giảm từ front tới back
```

Khi thêm `i`, loại ở back mọi index `j` có:

```text
a[j] <= a[i]
```

vì `i` mới hơn và không nhỏ hơn. `j` sẽ hết hạn trước `i` và không thể thắng `i` trong bất kỳ window tương lai chứa cả hai.

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

Mỗi index vào deque một lần và ra tối đa một lần, nên tổng thời gian `O(n)`.

Inner `while` không làm thuật toán `O(n²)` vì tổng số pop bị chặn tuyến tính.

## Dominance trong monotonic deque

Monotonic deque chỉ giữ các candidate chưa bị **chi phối (dominated)**.

Nếu `j` cũ hơn `i` và:

```text
a[j] <= a[i]
```

thì `j` tệ hơn `i` ở cả hai tiêu chí:

```text
hết hạn sớm hơn
không có giá trị lớn hơn
```

Do đó `j` có thể bị loại vĩnh viễn.

Đây là một ví dụ rất rõ của state pruning bằng dominance.

## 0–1 BFS

Nếu edge weight chỉ là `0` hoặc `1`, ta không cần full Priority Queue.

```text
weight 0 -> pushFront
weight 1 -> pushBack
```

Deque giữ đủ ordering để node có tentative distance nhỏ hơn được xử lý trước.

Độ phức tạp:

\[
O(V+E)
\]

trong representation adjacency list.

0–1 BFS cho thấy selection policy có thể được chuyên biệt khi miền priority bị giới hạn.

## Priority Queue là ADT, Heap chỉ là implementation phổ biến

Priority Queue hỗ trợ dạng thao tác:

```text
insert(item, priority)
peekMin / peekMax
extractMin / extractMax
```

Binary Heap phổ biến vì cân bằng tốt giữa locality, memory và `O(log n)` update. Nhưng Priority Queue còn có thể được cài bằng:

```text
balanced tree
bucket queue
radix heap
pairing heap
Fibonacci heap
indexed heap
specialized calendar/event structure
```

Không nên đồng nhất Priority Queue với Binary Heap.

## Binary Heap và shape invariant

Binary Heap thường dùng mảng. Với zero-based index:

```text
parent(i) = (i - 1) / 2
left(i)   = 2i + 1
right(i)  = 2i + 2
```

Hai invariant:

```text
shape là complete binary tree
heap-order đúng trên mọi cạnh cha-con
```

Insert giữ shape bằng cách thêm cuối, rồi sift-up sửa order. Extract root giữ shape bằng cách đưa phần tử cuối lên root, giảm size rồi sift-down.

Một mutation chỉ phá order trên một đường, nên không cần xây lại toàn heap.

## Build Heap là O(n), không phải O(n log n)

Nếu insert từng phần tử một, tổng có thể `O(n log n)`.

Nhưng bottom-up heapify gọi sift-down từ các internal node cho tổng thời gian `O(n)`.

Trực giác: phần lớn node nằm gần lá và chỉ có thể đi xuống rất ít bước. Chỉ rất ít node ở gần root có chiều cao lớn.

Đây là ví dụ cần phân tích tổng cost theo độ cao của node thay vì nhân “n node × log n” một cách thô.

## Priority Queue và tie-breaking

Priority không nhất thiết chỉ là một số.

Ví dụ scheduler:

```text
1. deadline sớm hơn
2. priority class cao hơn
3. sequence number nhỏ hơn
```

Nếu hai item có cùng priority nhưng business semantics yêu cầu FIFO, cần sequence number để làm tie-breaker.

Heap bản thân không cam kết stable order giữa các key bằng nhau.

## Mutable priority là một bẫy

Nếu một object đã nằm trong heap rồi priority field bị sửa trực tiếp, heap không tự biết phải reheapify.

Trong Java:

```text
node.priority = smallerValue
```

không tự di chuyển `node` lên.

Có ba hướng:

```text
xóa và chèn lại
cài decreaseKey/increaseKey với index map
chèn state mới và bỏ stale state khi pop
```

Dijkstra trong thư viện chuẩn thường dùng lựa chọn thứ ba vì `PriorityQueue` không cung cấp decrease-key trực tiếp.

## Lazy deletion trong Dijkstra

Một pattern:

```java
record State(int node, long dist) {}
```

Khi tìm được distance mới tốt hơn, chèn một `State` mới. Khi pop:

```text
nếu state.dist != dist[state.node] -> stale, bỏ qua
```

Heap có thể chứa nhiều version của cùng node, nhưng correctness vẫn được giữ nhờ kiểm tra version logic qua distance hiện tại.

Trade-off:

```text
implementation đơn giản
heap có thể lớn hơn
nhiều stale entry hơn
```

## Indexed Heap

Nếu cần `decreaseKey` thật sự, có thể lưu:

```text
heap[pos] = item
position[item] = pos
```

Mỗi swap trong heap phải cập nhật `position`.

Bất biến liên cấu trúc:

```text
position[heap[i]] == i
```

Indexed Heap giảm duplicate entry nhưng implementation phức tạp hơn đáng kể.

## d-ary Heap

Binary Heap có 2 child mỗi node. **d-ary heap** có `d` child.

Tăng `d` làm chiều cao giảm:

\[
O(\log_d n)
\]

nhưng sift-down phải so nhiều child hơn để chọn child tốt nhất.

Trade-off này có thể hữu ích khi workload có nhiều decrease-key hoặc khi memory/cache behavior thuận lợi.

Không có `d` tối ưu chung cho mọi hệ thống.

## Bucket Queue

Nếu priority là integer trong miền nhỏ, có thể dùng array các bucket thay vì heap.

```text
bucket[p] chứa các item có priority p
```

Extract-min tìm bucket không rỗng nhỏ nhất.

Nếu miền priority nhỏ hoặc current minimum tăng đơn điệu, bucket queue có thể nhanh hơn heap.

Đây là tư duy giống Counting Sort: khai thác miền khóa hẹp để bỏ comparison tree tổng quát.

## Dial's Algorithm

Với shortest path có non-negative integer weights bị chặn nhỏ, có thể dùng bucket theo distance modulo/range thay vì heap tổng quát.

Đây là một ví dụ selection policy chuyên biệt cho cấu trúc trọng số.

Bài học:

> Khi priority có thêm structure, Priority Queue tổng quát có thể chưa phải lựa chọn tốt nhất.

## Radix Heap

Radix Heap khai thác priority integer không giảm theo các lần extract-min và nhóm key theo bit-length của khoảng cách tới last extracted key.

Nó là ví dụ nâng cao cho việc dùng representation bit của priority để giảm chi phí so với comparison heap trong một số shortest-path workload.

Không cần dùng thường xuyên, nhưng đáng hiểu để thấy “heap” không phải giới hạn cuối của Priority Queue.

## Priority Queue trong event simulation

Discrete-event simulation thường giữ sự kiện theo timestamp:

```text
(time, sequence, event)
```

Lấy event sớm nhất, chạy nó, rồi có thể sinh event mới trong tương lai.

Ở đây Priority Queue chính là “đồng hồ logic” của hệ thống mô phỏng.

Nếu cùng timestamp, sequence number có thể bảo đảm deterministic order.

## Scheduler và starvation

Nếu luôn ưu tiên task priority cao, task thấp có thể không bao giờ được chạy nếu dòng task cao liên tục tới. Đây là **starvation**.

Một scheduler thực tế có thể dùng **aging**: priority hiệu dụng của task tăng theo thời gian chờ.

Điều này cho thấy priority policy không chỉ ảnh hưởng performance mà còn fairness.

## Multi-level queue

Hệ điều hành hoặc hệ thống worker có thể dùng nhiều queue:

```text
high priority queue
normal queue
background queue
```

Scheduler chọn giữa các queue theo policy riêng.

Đây là composition: mỗi queue bên trong có FIFO, còn hệ thống tổng thể có selection policy hai tầng.

## Work-stealing deque

Trong parallel runtime, mỗi worker có thể có deque task riêng.

Một pattern phổ biến:

```text
worker chủ sở hữu push/pop ở một đầu
worker khác steal từ đầu đối diện
```

Mục tiêu là giảm contention ở common case nhưng vẫn cân bằng công việc khi một worker rảnh.

Correctness concurrent của work-stealing deque phức tạp hơn deque single-thread rất nhiều vì phải xử lý atomicity và memory ordering.

## SPSC, MPSC, MPMC

Concurrent queue thường được phân loại theo số producer/consumer:

```text
SPSC: single producer, single consumer
MPSC: multiple producer, single consumer
SPMC: single producer, multiple consumer
MPMC: multiple producer, multiple consumer
```

SPSC ring buffer có thể rất đơn giản vì producer và consumer sở hữu các chỉ số khác nhau. MPMC cần coordination mạnh hơn và thường có nhiều trạng thái cạnh tranh.

Không nên dùng complexity của queue single-thread để suy ra chi phí concurrent queue.

## Lock-free không có nghĩa wait-free

**Lock-free** thường bảo đảm toàn hệ thống có tiến triển: trong hữu hạn bước, một thread nào đó hoàn thành operation.

**Wait-free** mạnh hơn: mỗi thread riêng lẻ hoàn thành operation trong số bước bị chặn.

Một lock-free queue vẫn có thể khiến một thread cụ thể retry nhiều lần dưới contention.

Đây là các guarantee về progress, khác với Big-O tuần tự.

## Memory reclamation trong concurrent queue

Một linked queue lock-free không thể đơn giản `free` node ngay khi dequeue nếu thread khác vẫn có thể đang đọc con trỏ tới node đó.

Cần các kỹ thuật như:

```text
hazard pointers
epoch-based reclamation
reference counting trong một số thiết kế
```

Điều này cho thấy lifetime management là một phần của correctness concurrent.

## Queue và memory retention

Trong Java/JavaScript, queue tự cài đặt bằng array + head index có thể giữ reference tới các item đã dequeue nếu không đặt slot cũ về `null`/`undefined` hoặc compact tùy representation.

Về logic item đã ra khỏi queue, nhưng GC vẫn thấy reference từ backing array.

Do đó logical size và reachable memory không luôn giống nhau.

## Khi queue quá dài: latency distribution

Average queue length không nói hết tail latency. Một burst lớn có thể tạo một số request chờ rất lâu dù mean vẫn chấp nhận được.

Trong hệ thống thực tế nên quan sát:

```text
queue depth histogram
p50/p95/p99 waiting time
drop/reject rate
consumer utilization
arrival burstiness
```

Queue là một cấu trúc dữ liệu nhưng cũng là một điểm đo sức khỏe hệ thống.

## Chọn cấu trúc theo selection policy

Có thể nhìn nhiều thuật toán dưới một khung:

```text
Stack          -> chọn phần tử mới nhất
Queue          -> chọn phần tử cũ nhất
Deque          -> chọn ở một trong hai đầu
Priority Queue -> chọn phần tử tốt nhất theo comparator
Randomized     -> chọn ngẫu nhiên
Bucket Queue   -> chọn theo lớp priority rời rạc
```

Khi đổi policy của frontier, ta thường đổi cả semantics của thuật toán.

## Kiểm thử queue và deque

Property cơ bản:

```text
enqueue sequence rồi dequeue hết phải bảo toàn FIFO
size không âm và không vượt capacity
ring wrap nhiều lần vẫn giữ thứ tự
resize không đổi logical order
full/empty transition đúng
```

Với deque:

```text
pushFront/popFront đối xứng
pushBack/popBack đối xứng
mixed operations so với reference deque
```

Random differential test rất hiệu quả cho ring-buffer bugs.

## Kiểm thử Priority Queue

Có thể push random values rồi pop hết và kiểm tra output đã sorted theo comparator.

Với indexed heap, phải kiểm tra:

```text
heap invariant
position[heap[i]] == i
size và active set nhất quán
```

Với lazy deletion, cần test nhiều stale entries và bảo đảm stale state không được dùng để relax tiếp.

## Những hiểu lầm phổ biến

“Queue chỉ là mảng có push/shift” — `shift` lặp lại có thể rất đắt.

“Queue càng lớn càng chống overload tốt” — queue lớn có thể chỉ biến overload thành latency lớn.

“Priority Queue nghĩa là Binary Heap” — Heap chỉ là một implementation.

“Thay priority field trong object là heap tự cập nhật” — sai.

“Inner while trong monotonic deque làm O(n²)” — sai vì mỗi index bị loại tối đa một lần.

“Concurrent queue chỉ cần thêm lock vào enqueue/dequeue” — chưa đủ để nói về throughput, fairness, blocking semantics và iteration contract.

## Mô hình tư duy

> Queue, Deque và Priority Queue khác nhau chủ yếu ở **quy tắc chọn ai được phục vụ tiếp theo**. Chính quy tắc đó tạo ra thứ tự xử lý, proof of correctness và đặc tính hệ thống.

Khi gặp một frontier hoặc danh sách chờ, hãy hỏi: **cần FIFO, LIFO, hai đầu, minimum priority hay một priority domain chuyên biệt; queue có bounded không; overload xử lý thế nào; fairness có quan trọng không; và selection policy nào chính xác là điều proof của thuật toán cần?**

Xem tiếp: [Stacks](./02_stacks.md), [Heaps](../02_trees/03_heaps.md), [BFS/DFS](../03_graphs/01_graph_traversal_bfs_dfs.md), [Shortest Paths](../03_graphs/02_shortest_paths.md), [Amortized Analysis](../05_specialized/03_amortized_randomized_and_probabilistic_thinking.md) và [Java Collections](../80_language_implementations/01_java_collections_and_dsa.md).