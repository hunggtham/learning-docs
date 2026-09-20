# Heap và hàng đợi ưu tiên
**Đống và hàng đợi ưu tiên (Heap & Priority Queue / 힙과 우선순위 큐)**

Heap được thiết kế cho một loại câu hỏi rất cụ thể: trong một tập dữ liệu thay đổi liên tục, phần tử **nhỏ nhất hoặc lớn nhất hiện tại** là gì, và làm sao cập nhật tập đó mà không phải sort lại toàn bộ sau mỗi thay đổi?

Đây là điểm bắt đầu quan trọng. Heap không phải “một cách sort dữ liệu”. Nó là cách biểu diễn (representation) tối thiểu đủ mạnh để giữ một extreme phần tử ở vị trí dễ truy cập.

## Heap tính chất và thứ tự bộ phận

Với **đống nhỏ nhất (최소 힙)**, mỗi nút thỏa:

\[
khóa(parent) \le khóa(child)
\]

Với **đống lớn nhất (최대 힙)** thì ngược lại.

bất biến (invariant) này chỉ tạo **thứ tự bộ phận**. Trong đống nhỏ nhất, nút gốc chắc chắn nhỏ nhất, nhưng hai siblings không cần có thứ tự với nhau; phần tử ở cây con trái cũng không cần nhỏ hơn phần tử ở cây con phải.

Đó chính là lý do heap có thể duy trì extreme nhanh hơn việc giữ toàn bộ collection sorted.

## Mô hình tư duy

> Heap cố tình lưu ít thông tin thứ tự hơn một cấu trúc đã sắp xếp hoàn toàn. Nó chỉ duy trì đủ quan hệ để phần tử cực trị luôn ở nút gốc. Chính việc “không trả chi phí cho thông tin không cần thiết” tạo nên hiệu quả của heap.

Nếu tải công việc cần phần tử liền trước/liền sau hoặc duyệt có thứ tự theo khoảng, heap không phù hợp. Nếu liên tục cần `min`, `max`, `top-k` hoặc “tác vụ có độ ưu tiên cao nhất tiếp theo”, heap là lựa chọn tự nhiên.

## đống nhị phân và complete cây

đống nhị phân thường dùng **complete cây nhị phân (완전 이진 트리)**: mọi tầng được lấp đầy từ trái sang phải, trừ tầng cuối có thể chưa đầy.

Shape bất biến này cho phép bỏ hoàn toàn các con trỏ. Với mảng zero-based:

\[
left(i)=2i+1
\]

\[
right(i)=2i+2
\]

\[
nút cha(i)=\left\lfloor\frac{i-1}{2}\right\rfloor
\]

Nhờ đó heap có tính cục bộ (locality) tốt hơn pointer-based các cây, chỉ cần một contiguous/mảng động.

## Chèn: giữ hình dạng trước, sửa thứ tự sau

Để insert `x`, ta append vào cuối mảng. Việc này tự động giữ complete-tree shape. Sau đó `x` có thể nhỏ hơn nút cha và phá heap tính chất, nên ta **sift up / bubble up (상향 이동)**:

```text
append x
while x violates parent relation:
    swap x with parent
```

Mỗi swap đưa phần tử lên một tầng. chiều cao của complete cây nhị phân là `O(log n)`, nên insert là:

\[
O(\log n)
\]

### JavaScript cách triển khai

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

Comparator phải tạo ordering nhất quán. Nếu comparator không transitive, heap tính chất không còn meaningful.

## Extract-min: sửa nút gốc bằng last phần tử

nút gốc là minimum. Khi remove nút gốc, nếu chỉ xóa `a[0]`, complete-tree cách biểu diễn sẽ bị hỏng. Cách chuẩn là:

1. lưu nút gốc làm answer;
2. chuyển last phần tử lên nút gốc;
3. giảm size;
4. sift-down nút gốc tới khi heap tính chất được phục hồi.

Trong đống nhỏ nhất, nếu nút lớn hơn một nút con, ta phải swap với nút con nhỏ hơn. Chọn nút con nhỏ hơn là cần thiết: swap với nút con lớn hơn có thể vẫn để nút con nhỏ hơn vi phạm ngay lập tức.

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

## xây dựng heap: vì sao `O(n)` chứ không phải `O(n log n)`?

Một cách ngây thơ là insert từng phần tử, cho `O(n log n)`. Nhưng nếu toàn bộ mảng đã có sẵn, ta có thể gọi sift-down từ nút cha cuối cùng đi ngược lên nút gốc.

Thoạt nhìn có `n` các nút và mỗi sift có thể `O(log n)`, nên dễ đoán `O(n log n)`. Nhưng phần lớn các nút nằm gần các nút lá và hầu như không cần đi xa.

Khoảng một nửa các nút là các nút lá, chi phí 0. Khoảng một phần tư có chiều cao 1, một phần tám có chiều cao 2, v.v. Tổng work gần:

\[
n\left(\frac{1}{4}\cdot1+\frac{1}{8}\cdot2+\frac{1}{16}\cdot3+\cdots\right)=O(n)
\]

Đây là ví dụ quan trọng của **aggregate analysis**: không thể lấy worst chi phí của một nút rồi nhân cho mọi nút nếu phân phối của work rất không đều.

## hàng đợi ưu tiên là sự trừu tượng (abstraction), heap là cách triển khai

**hàng đợi ưu tiên (우선순위 큐)** là ADT mô tả các thao tác như:

```text
insert(item, priority)
peek-best()
extract-best()
```

đống nhị phân chỉ là một cách triển khai rất phổ biến. hàng đợi ưu tiên cũng có thể được implement bằng balanced cây, ngăn băm queues, Fibonacci heap, pairing heap hoặc chuyên biệt monotonic queues tùy khối lượng công việc.

Trong Java:

```java
PriorityQueue<Integer> pq = new PriorityQueue<>();
pq.offer(5);
pq.offer(2);
pq.offer(8);
System.out.println(pq.poll()); // 2
```

Muốn đống lớn nhất:

```java
PriorityQueue<Integer> max =
    new PriorityQueue<>(Comparator.reverseOrder());
```

## Comparator pitfalls trong Java

Không nên viết comparator kiểu:

```java
(a, b) -> a.cost - b.cost
```

nếu integer có thể lớn, vì subtraction có thể tràn số. Dùng:

```java
Comparator.comparingInt(Node::cost)
```

hoặc `Integer.compare(a.cost, b.cost)`.

Nếu độ ưu tiên là `long`, dùng `Comparator.comparingLong`.

## Heap không hỗ trợ tìm kiếm tùy ý tốt

Trong đống nhỏ nhất, biết `parent <= child` không cho biết đích nằm ở nhánh nào. Nếu đích lớn hơn nút gốc, cả hai các cây con đều có thể chứa nó. Vì vậy tìm một arbitrary giá trị vẫn có thể:

\[
O(n)
\]

Đây là khác biệt bản chất với BST. Heap tối ưu **extreme retrieval**, BST tối ưu **ordered search theo khóa**.

## Heap Sort

Heap có thể dùng để sort in-place:

1. xây dựng đống lớn nhất `O(n)`;
2. swap nút gốc lớn nhất với cuối mảng;
3. giảm heap size;
4. sift-down nút gốc;
5. lặp lại.

Time:

\[
O(n\log n)
\]

Heap sort có trường hợp xấu nhất tốt và có thể in-place với `O(1)` extra mảng space, nhưng thường bộ nhớ đệm hành vi và constant factor không tốt bằng các sort thực dụng khác. Nó cũng không ổn định theo cách triển khai chuẩn.

Điểm đáng học là heap sort cho thấy cùng bất biến “nút gốc là extreme” có thể được dùng để xác định phần tử cuối của hậu tố đã sắp xếp từng bước.

## Top-K và bounded bộ nhớ

Nếu luồng có `n` phần tử nhưng chỉ cần `k` phần tử lớn nhất, sắp xếp toàn bộ sẽ tạo nhiều thông tin thứ tự không cần thiết.

Giữ **đống nhỏ nhất size `k`**:

```text
nếu heap chưa đủ k -> push
nếu x <= heap.min -> bỏ
nếu x > heap.min -> pop min rồi push x
```

Time:

\[
O(n\log k)
\]

bộ nhớ:

\[
O(k)
\]

Khi `k << n`, đây là cải thiện quan trọng cả về thời gian lẫn bộ nhớ. Mẫu này xuất hiện trong xếp hạng ứng viên, giám sát, hệ gợi ý, tổng hợp kết quả tìm kiếm và các giai đoạn Top-K phân tán.

## K-way merge

Giả sử có `k` danh sách đã sắp xếp với tổng `N` phần tử. Ta đưa phần tử đầu của mỗi danh sách vào đống nhỏ nhất. Mỗi lần lấy phần tử nhỏ nhất ra, ta chỉ tiến trong đúng danh sách đó rồi đưa phần tử tiếp theo vào heap.

Heap chỉ chứa tối đa `k` heads:

\[
O(N\log k)
\]

Đây là core idea của bên ngoài sắp xếp trộn, merge SSTables, merge log streams và nhiều chuỗi xử lý xử lý sorted runs.

## Dijkstra và decrease-key

Classical Dijkstra thường được mô tả với `decrease-key`: nếu khoảng cách của đỉnh giảm, cập nhật độ ưu tiên của mục đang trong heap.

Nhiều standard `PriorityQueue` APIs không hỗ trợ cập nhật độ ưu tiên trực tiếp. Có hai mẫu chính.

### mẫu 1: stale các mục

Mỗi khi có khoảng cách tốt hơn, push mục mới. Khi pop:

```java
if (cur.dist() != dist[cur.node()]) continue;
```

mục cũ trở thành stale và được bỏ qua.

Ưu điểm là cách triển khai đơn giản; nhược điểm là heap có các phần tử trùng và bộ nhớ/work tăng.

### mẫu 2: indexed heap

Duy trì:

```text
position[item] -> heap index
```

Mỗi swap phải cập nhật `position`. Khi độ ưu tiên thay đổi, tìm item trực tiếp rồi sift-up/sift-down `O(log n)`.

mẫu này hữu ích khi độ ưu tiên cập nhật rất thường xuyên và identity của item quan trọng.

## Scheduler và sự kiện simulation

hàng đợi ưu tiên không chỉ dùng trong các thuật toán đồ thị. Một sự kiện-driven simulator có các sự kiện với timestamp; mỗi bước lấy sự kiện có thời gian sớm nhất. Scheduler có thể lấy task có deadline/độ ưu tiên cao nhất. Timer wheel, calendar queue hoặc heap đều là cách tổ chức “next sự kiện”.

Điểm chung là tải công việc không cần toàn bộ sự kiện được sắp xếp hoàn chỉnh; nó chỉ liên tục cần **phần tử tốt nhất tiếp theo**.

## Median trực tuyến bằng hai heaps

Để theo dõi median của stream:

```text
max-heap lower half
min-heap upper half
```

bất biến:

```text
mọi lower <= mọi upper
size difference <= 1
```

Median là nút gốc của heap lớn hơn hoặc average của hai các nút gốc.

Mỗi insert `O(log n)`, median truy vấn `O(1)`.

Đây là ví dụ composition: hai heaps phối hợp để duy trì một ranh giới thống kê thứ tự.

## D-ary heap và branching-factor sự đánh đổi (trade-off)

đống nhị phân có 2 các nút con. Có thể dùng d-ary heap với `d` các nút con mỗi nút. chiều cao giảm còn khoảng:

\[
\log_d n
\]

nhưng sift-down phải inspect tới `d` các nút con để chọn best. khối lượng công việc nhiều decrease-key/insert so với extract-min có thể hưởng lợi từ hệ số phân nhánh lớn hơn; bộ nhớ đệm hành vi cũng có thể thay đổi.

cấu trúc dữ liệu design không phải chỉ chọn “heap hay không”, mà còn chọn cách biểu diễn phù hợp thao tác mix.

## tính ổn định và quy tắc phân xử khi bằng nhau

hàng đợi ưu tiên thường không đảm bảo ổn định order giữa items có cùng độ ưu tiên. Nếu domain cần FIFO trong cùng độ ưu tiên, comparator nên thêm số thứ tự:

```text
(priority, insertionSequence)
```

Ví dụ job bộ lập lịch có thể cần “độ ưu tiên cao trước; nếu bằng nhau, task đến trước chạy trước”. quy tắc phân xử khi bằng nhau là part của domain ngữ nghĩa (semantics), không phải chi tiết phụ.

## có thể thay đổi độ ưu tiên các đối tượng: một bug phổ biến

Nếu heap chứa đối tượng rồi độ ưu tiên trường của đối tượng bị mutate trực tiếp, heap không tự biết để rearrange. Heap mảng vẫn giữ shape cũ và bất biến có thể sai.

Do đó hoặc:

- các đối tượng bất biến sau khi tạo về độ ưu tiên;
- dùng explicit cập nhật/decrease-key;
- push mục mới và dùng stale-entry/version mẫu.

Trong Java, mutate đối tượng đang ở `PriorityQueue` không khiến queue reheapify tự động.

## Heap với C: quyền sở hữu (ownership) và capacity

Trong C, đống nhị phân thường là mảng động struct:

```c
typedef struct {
    Item *data;
    size_t size;
    size_t cap;
} Heap;
```

Ngoài heap bất biến, cách triển khai phải giữ thêm capacity bất biến và quyền sở hữu của `data`. `realloc` failure, đối tượng vòng đời (lifetime) và comparator callback là concerns mà Java/JavaScript môi trường chạy (runtime) che bớt.

Nếu item lớn, có thể heap các con trỏ thay vì copy structs, nhưng tính cục bộ và quyền sở hữu ngữ nghĩa thay đổi.

## Những hiểu lầm phổ biến

**“Heap là mảng đã sắp xếp dưới dạng cây.”** Sai. Heap chỉ partial-order.

**“Xây dựng heap phải `O(n log n)` vì mỗi lần chèn tốn `O(log n)`.”** Điều này chỉ đúng nếu xây dựng bằng cách chèn lặp lại. Heapify từ dưới lên (**bottom-up heapify**) là `O(n)`.

**“đống nhỏ nhất giúp binary-search một giá trị.”** Không. Heap không có BST ordering giữa left/right các cây con.

**“PriorityQueue hỗ trợ thay độ ưu tiên của đối tượng tự động.”** Thường không. sự thay đổi dữ liệu ngoài heap các thao tác có thể phá bất biến.

**“Heap luôn tốt hơn mảng đã sắp xếp cho min.”** Nếu dataset tĩnh và cần iterate thứ tự đã sắp xếp nhiều lần, sort một lần có thể tốt hơn. Heap hữu ích khi collection mutate và lặp lại cần extreme.

## kiểm thử heap bằng bất biến

Sau ngẫu nhiên sequence push/pop, kiểm:

```text
for every i > 0:
    compare(parent(i), i) <= 0
```

Đồng thời nên so sánh dãy phần tử lấy ra với kết quả tham chiếu từ `sort()` trên các tập dữ liệu nhỏ. Với đống có chỉ mục (indexed heap), cần kiểm tra thêm tính nhất quán hai chiều:

```text
position[item] = i
heap[i] = item
```

Lỗi heap thường xuất hiện ở các trường hợp biên: rỗng, chỉ một phần tử, chỉ có nút con trái, các phần tử có cùng độ ưu tiên, trường hợp bộ so sánh trả hòa và lần đổi chỗ cuối cùng.

## Mô hình tư duy mở rộng

> Heap là một **động frontier structure**. Nó không cố giữ toàn bộ dữ liệu ordered; nó giữ đủ cục bộ bất biến để câu hỏi “ai là ứng viên tốt nhất tiếp theo?” luôn trả lời rẻ.

Khi gặp một thuật toán có loop kiểu “liên tục chọn ứng viên nhỏ nhất/lớn nhất rồi sinh thêm các ứng viên”, hãy nghĩ tới hàng đợi ưu tiên. Sau đó mới hỏi đống nhị phân có đúng mô hình chi phí không, có cần decrease-key không, có bounded độ ưu tiên domain để dùng ngăn băm không, và quy tắc phân xử khi bằng nhau ngữ nghĩa là gì.