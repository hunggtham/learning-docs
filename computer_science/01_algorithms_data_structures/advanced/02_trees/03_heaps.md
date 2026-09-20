# Heap và Priority Queue
**Đống và hàng đợi ưu tiên (Heap & Priority Queue / 힙과 우선순위 큐)**

Heap được thiết kế cho một loại câu hỏi rất cụ thể: trong một tập dữ liệu thay đổi liên tục, phần tử **nhỏ nhất hoặc lớn nhất hiện tại** là gì, và làm sao cập nhật tập đó mà không phải sort lại toàn bộ sau mỗi thay đổi?

Đây là điểm bắt đầu quan trọng. Heap không phải “một cách sort dữ liệu”. Nó là representation tối thiểu đủ mạnh để giữ một extreme element ở vị trí dễ truy cập.

## Heap property và partial order

Với **min-heap (최소 힙)**, mỗi node thỏa:

\[
key(parent) \le key(child)
\]

Với **max-heap (최대 힙)** thì ngược lại.

Invariant này chỉ tạo **partial order**. Trong min-heap, root chắc chắn nhỏ nhất, nhưng hai siblings không cần có thứ tự với nhau; phần tử ở subtree trái cũng không cần nhỏ hơn phần tử ở subtree phải.

Đó chính là lý do heap có thể duy trì extreme nhanh hơn việc giữ toàn bộ collection sorted.

## Mental Model

> Heap cố tình biết ít hơn sorted structure. Nó chỉ duy trì đủ order để extreme luôn ở root. Chính việc “không trả tiền cho thông tin không cần thiết” tạo nên hiệu quả của heap.

Nếu workload cần predecessor/successor/range order, heap không phù hợp. Nếu workload liên tục cần `min`, `max`, `top-k` hoặc “task ưu tiên cao nhất tiếp theo”, heap rất tự nhiên.

## Binary heap và complete tree

Binary heap thường dùng **complete binary tree (완전 이진 트리)**: mọi level được lấp đầy từ trái sang phải, trừ level cuối có thể chưa đầy.

Shape invariant này cho phép bỏ hoàn toàn pointers. Với array zero-based:

\[
left(i)=2i+1
\]

\[
right(i)=2i+2
\]

\[
parent(i)=\left\lfloor\frac{i-1}{2}\right\rfloor
\]

Nhờ đó heap có locality tốt hơn pointer-based trees, chỉ cần một contiguous/dynamic array.

## Insert: giữ shape trước, sửa order sau

Để insert `x`, ta append vào cuối array. Việc này tự động giữ complete-tree shape. Sau đó `x` có thể nhỏ hơn parent và phá heap property, nên ta **sift up / bubble up (상향 이동)**:

```text
append x
while x violates parent relation:
    swap x with parent
```

Mỗi swap đưa element lên một level. Height của complete binary tree là `O(log n)`, nên insert là:

\[
O(\log n)
\]

### JavaScript implementation

```js
class MinHeap {
  constructor(compare = (a, b) => a - b) {
    this.a = [];
    this.compare = compare;
  }

  size() {
    return this.a.length;
  }

  peek() {
    return this.a[0];
  }

  push(x) {
    const a = this.a;
    a.push(x);
    let i = a.length - 1;

    while (i > 0) {
      const p = (i - 1) >> 1;
      if (this.compare(a[p], a[i]) <= 0) break;
      [a[p], a[i]] = [a[i], a[p]];
      i = p;
    }
  }
}
```

Comparator phải tạo ordering nhất quán. Nếu comparator không transitive, heap property không còn meaningful.

## Extract-min: sửa root bằng last element

Root là minimum. Khi remove root, nếu chỉ xóa `a[0]`, complete-tree representation sẽ bị hỏng. Cách chuẩn là:

1. lưu root làm answer;
2. chuyển last element lên root;
3. giảm size;
4. sift-down root tới khi heap property được phục hồi.

Trong min-heap, nếu node lớn hơn một child, ta phải swap với child nhỏ hơn. Chọn child nhỏ hơn là cần thiết: swap với child lớn hơn có thể vẫn để child nhỏ hơn vi phạm ngay lập tức.

```js
pop() {
  const a = this.a;
  if (a.length === 0) return undefined;
  if (a.length === 1) return a.pop();

  const ans = a[0];
  a[0] = a.pop();

  let i = 0;
  while (true) {
    let best = i;
    const l = i * 2 + 1;
    const r = l + 1;

    if (l < a.length && this.compare(a[l], a[best]) < 0) best = l;
    if (r < a.length && this.compare(a[r], a[best]) < 0) best = r;
    if (best === i) break;

    [a[i], a[best]] = [a[best], a[i]];
    i = best;
  }

  return ans;
}
```

`peek()` là `O(1)`, còn `push()` và `pop()` là `O(log n)`.

## Build heap: vì sao `O(n)` chứ không phải `O(n log n)`?

Một cách ngây thơ là insert từng element, cho `O(n log n)`. Nhưng nếu toàn bộ array đã có sẵn, ta có thể gọi sift-down từ parent cuối cùng đi ngược lên root.

Thoạt nhìn có `n` nodes và mỗi sift có thể `O(log n)`, nên dễ đoán `O(n log n)`. Nhưng phần lớn nodes nằm gần leaves và hầu như không cần đi xa.

Khoảng một nửa nodes là leaves, cost 0. Khoảng một phần tư có height 1, một phần tám có height 2, v.v. Tổng work gần:

\[
n\left(\frac{1}{4}\cdot1+\frac{1}{8}\cdot2+\frac{1}{16}\cdot3+\cdots\right)=O(n)
\]

Đây là ví dụ quan trọng của **aggregate analysis**: không thể lấy worst cost của một node rồi nhân cho mọi node nếu distribution của work rất không đều.

## Priority Queue là abstraction, heap là implementation

**Priority Queue (우선순위 큐)** là ADT mô tả operations như:

```text
insert(item, priority)
peek-best()
extract-best()
```

Binary heap chỉ là một implementation rất phổ biến. Priority queue cũng có thể được implement bằng balanced tree, bucket queues, Fibonacci heap, pairing heap hoặc specialized monotonic queues tùy workload.

Trong Java:

```java
PriorityQueue<Integer> pq = new PriorityQueue<>();
pq.offer(5);
pq.offer(2);
pq.offer(8);
System.out.println(pq.poll()); // 2
```

Muốn max-heap:

```java
PriorityQueue<Integer> max =
    new PriorityQueue<>(Comparator.reverseOrder());
```

## Comparator pitfalls trong Java

Không nên viết comparator kiểu:

```java
(a, b) -> a.cost - b.cost
```

nếu integer có thể lớn, vì subtraction có thể overflow. Dùng:

```java
Comparator.comparingInt(Node::cost)
```

hoặc `Integer.compare(a.cost, b.cost)`.

Nếu priority là `long`, dùng `Comparator.comparingLong`.

## Heap không hỗ trợ arbitrary search tốt

Trong min-heap, biết `parent <= child` không cho biết target nằm ở nhánh nào. Nếu target lớn hơn root, cả hai subtrees đều có thể chứa nó. Vì vậy tìm một arbitrary value vẫn có thể:

\[
O(n)
\]

Đây là khác biệt bản chất với BST. Heap tối ưu **extreme retrieval**, BST tối ưu **ordered search theo key**.

## Heap Sort

Heap có thể dùng để sort in-place:

1. build max-heap `O(n)`;
2. swap root lớn nhất với cuối array;
3. giảm heap size;
4. sift-down root;
5. lặp lại.

Time:

\[
O(n\log n)
\]

Heap sort có worst-case tốt và có thể in-place với `O(1)` extra array space, nhưng thường cache behavior và constant factor không tốt bằng các sort thực dụng khác. Nó cũng không stable theo implementation chuẩn.

Điểm đáng học là heap sort cho thấy cùng invariant “root là extreme” có thể được dùng để xác định phần tử cuối của sorted suffix từng bước.

## Top-K và bounded memory

Nếu stream có `n` phần tử nhưng chỉ cần `k` lớn nhất, sort toàn bộ tạo nhiều order information không cần thiết.

Giữ **min-heap size `k`**:

```text
nếu heap chưa đủ k -> push
nếu x <= heap.min -> bỏ
nếu x > heap.min -> pop min rồi push x
```

Time:

\[
O(n\log k)
\]

Memory:

\[
O(k)
\]

Khi `k << n`, đây là improvement quan trọng cả về time lẫn memory. Pattern này dùng trong ranking candidates, monitoring, recommendation, search aggregation và distributed top-k stages.

## K-way merge

Giả sử có `k` sorted lists với tổng `N` elements. Ta đưa phần tử đầu mỗi list vào min-heap. Mỗi lần pop smallest, ta advance đúng list đó rồi push phần tử tiếp theo.

Heap chỉ chứa tối đa `k` heads:

\[
O(N\log k)
\]

Đây là core idea của external merge sort, merge SSTables, merge log streams và nhiều pipeline xử lý sorted runs.

## Dijkstra và decrease-key

Classical Dijkstra thường được mô tả với `decrease-key`: nếu distance của vertex giảm, update priority của entry đang trong heap.

Nhiều standard `PriorityQueue` APIs không hỗ trợ update priority trực tiếp. Có hai pattern chính.

### Pattern 1: stale entries

Mỗi khi có distance tốt hơn, push entry mới. Khi pop:

```java
if (cur.dist() != dist[cur.node()]) continue;
```

Entry cũ trở thành stale và được bỏ qua.

Ưu điểm là implementation đơn giản; nhược điểm là heap có duplicates và memory/work tăng.

### Pattern 2: indexed heap

Duy trì:

```text
position[item] -> heap index
```

Mỗi swap phải cập nhật `position`. Khi priority thay đổi, tìm item trực tiếp rồi sift-up/sift-down `O(log n)`.

Pattern này hữu ích khi priority update rất thường xuyên và identity của item quan trọng.

## Scheduler và event simulation

Priority queue không chỉ dùng trong graph algorithms. Một event-driven simulator có events với timestamp; mỗi bước lấy event có thời gian sớm nhất. Scheduler có thể lấy task có deadline/priority cao nhất. Timer wheel, calendar queue hoặc heap đều là cách tổ chức “next event”.

Điểm chung là workload không cần toàn bộ events sorted hoàn chỉnh; nó chỉ liên tục cần **next best**.

## Median online bằng hai heaps

Để theo dõi median của stream:

```text
max-heap lower half
min-heap upper half
```

Invariant:

```text
mọi lower <= mọi upper
size difference <= 1
```

Median là root của heap lớn hơn hoặc average của hai roots.

Mỗi insert `O(log n)`, median query `O(1)`.

Đây là ví dụ composition: hai heaps phối hợp để duy trì một boundary order statistic.

## D-ary heap và branching-factor trade-off

Binary heap có 2 children. Có thể dùng d-ary heap với `d` children mỗi node. Height giảm còn khoảng:

\[
\log_d n
\]

nhưng sift-down phải inspect tới `d` children để chọn best. Workload nhiều decrease-key/insert so với extract-min có thể hưởng lợi từ branching factor lớn hơn; cache behavior cũng có thể thay đổi.

Data structure design không phải chỉ chọn “heap hay không”, mà còn chọn representation phù hợp operation mix.

## Stability và tie-breaking

Priority queue thường không đảm bảo stable order giữa items có cùng priority. Nếu domain cần FIFO trong cùng priority, comparator nên thêm sequence number:

```text
(priority, insertionSequence)
```

Ví dụ job scheduler có thể cần “priority cao trước; nếu bằng nhau, task đến trước chạy trước”. Tie-breaking là part của domain semantics, không phải chi tiết phụ.

## Mutable priority objects: một bug phổ biến

Nếu heap chứa object rồi priority field của object bị mutate trực tiếp, heap không tự biết để rearrange. Heap array vẫn giữ shape cũ và invariant có thể sai.

Do đó hoặc:

- objects immutable về priority;
- dùng explicit update/decrease-key;
- push entry mới và dùng stale-entry/version pattern.

Trong Java, mutate object đang ở `PriorityQueue` không khiến queue reheapify tự động.

## Heap với C: ownership và capacity

Trong C, binary heap thường là dynamic array struct:

```c
typedef struct {
    Item *data;
    size_t size;
    size_t cap;
} Heap;
```

Ngoài heap invariant, implementation phải giữ thêm capacity invariant và ownership của `data`. `realloc` failure, object lifetime và comparator callback là concerns mà Java/JavaScript runtime che bớt.

Nếu item lớn, có thể heap pointers thay vì copy structs, nhưng locality và ownership semantics thay đổi.

## Common misconceptions

**“Heap là sorted array dưới dạng tree.”** Sai. Heap chỉ partial-order.

**“Build heap phải `O(n log n)` vì mỗi insert `O(log n)`.”** Chỉ đúng nếu build bằng repeated insert. Bottom-up heapify là `O(n)`.

**“Min-heap giúp binary-search một value.”** Không. Heap không có BST ordering giữa left/right subtrees.

**“PriorityQueue hỗ trợ thay priority của object tự động.”** Thường không. Mutation ngoài heap operations có thể phá invariant.

**“Heap luôn tốt hơn sorted array cho min.”** Nếu dataset static và cần iterate sorted order nhiều lần, sort một lần có thể tốt hơn. Heap hữu ích khi collection mutate và repeatedly cần extreme.

## Testing heap bằng invariant

Sau random sequence push/pop, kiểm:

```text
for every i > 0:
    compare(parent(i), i) <= 0
```

Đồng thời so pop sequence với reference `sort()` trên datasets nhỏ. Với indexed heap, phải kiểm thêm bidirectional consistency:

```text
position[item] = i
heap[i] = item
```

Heap bugs thường xuất hiện ở boundary: empty, one element, only-left-child, duplicate priorities, comparator ties và last swap.

## Mental Model mở rộng

> Heap là một **dynamic frontier structure**. Nó không cố giữ toàn bộ dữ liệu ordered; nó giữ đủ local invariant để câu hỏi “ai là ứng viên tốt nhất tiếp theo?” luôn trả lời rẻ.

Khi gặp một algorithm có loop kiểu “liên tục chọn candidate nhỏ nhất/lớn nhất rồi sinh thêm candidates”, hãy nghĩ tới priority queue. Sau đó mới hỏi binary heap có đúng cost model không, có cần decrease-key không, có bounded priority domain để dùng bucket không, và tie-breaking semantics là gì.