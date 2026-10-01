# Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vùng nhớ vùng nhớ động (heap / 힙) tính chất và thứ tự bộ phận** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Mô hình tư duy** để rút ra mô hình chung và giới hạn. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Đống và hàng đợi ưu tiên (Heap & Priority Queue / 힙과 우선순위 큐)**

Vùng nhớ vùng nhớ động (heap / 힙) được thiết kế cho một loại câu hỏi rất cụ thể: trong một tập dữ liệu thay đổi liên tục, phần tử **nhỏ nhất hoặc lớn nhất hiện tại** là gì, và làm sao cập nhật tập đó mà không phải sort lại toàn bộ sau mỗi thay đổi?

Đây là điểm bắt đầu quan trọng. vùng nhớ động (heap / 힙) không phải “một cách sort dữ liệu”. Nó là cách biểu diễn (representation / 표현) tối thiểu đủ mạnh để giữ một extreme phần tử ở vị trí dễ truy cập.

## Vùng nhớ vùng nhớ động (heap / 힙) tính chất và thứ tự bộ phận

Với **đống nhỏ nhất (최소 힙)**, mỗi nút thỏa:

\[
khóa(parent) \le khóa(child)
\]

Với **đống lớn nhất (최대 힙)** thì ngược lại.

Bất biến (invariant / 불변식) này chỉ tạo **thứ tự bộ phận**. Trong đống nhỏ nhất, nút gốc chắc chắn nhỏ nhất, nhưng hai siblings không cần có thứ tự với nhau; phần tử ở cây con trái cũng không cần nhỏ hơn phần tử ở cây con phải.

Đó chính là lý do vùng nhớ động (heap / 힙) có thể duy trì extreme nhanh hơn việc giữ toàn bộ collection sorted.

> **Chuyển mạch:** Trong **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **Mô hình tư duy** gom các mảnh từ **Vùng nhớ vùng nhớ động (heap / 힙) tính chất và thứ tự bộ phận** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **đống nhị phân và complete cây** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> vùng nhớ động (heap / 힙) cố tình lưu ít thông tin thứ tự hơn một cấu trúc đã sắp xếp hoàn toàn. Nó chỉ duy trì đủ quan hệ để phần tử cực trị luôn ở nút gốc. Chính việc “không trả chi phí cho thông tin không cần thiết” tạo nên hiệu quả của vùng nhớ động (heap / 힙).

Nếu tải công việc cần phần tử liền trước/liền sau hoặc duyệt có thứ tự theo khoảng, vùng nhớ động (heap / 힙) không phù hợp. Nếu liên tục cần `min`, `max`, `top-k` hoặc “tác vụ có độ ưu tiên cao nhất tiếp theo”, vùng nhớ động (heap / 힙) là lựa chọn tự nhiên.

> **Chuyển mạch:** Ở chặng này của **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **đống nhị phân và complete cây** gom các mảnh từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Chèn: giữ hình dạng trước, sửa thứ tự sau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Nhờ đó vùng nhớ động (heap / 힙) có tính cục bộ (locality) tốt hơn pointer-based các cây, chỉ cần một contiguous/mảng động.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **Chèn: giữ hình dạng trước, sửa thứ tự sau** tiếp nhận điểm tựa từ **đống nhị phân và complete cây** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Extract-min: sửa nút gốc bằng last phần tử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chèn: giữ hình dạng trước, sửa thứ tự sau

Để insert `x`, ta append vào cuối mảng. Việc này tự động giữ complete-tree shape. Sau đó `x` có thể nhỏ hơn nút cha và phá vùng nhớ động (heap / 힙) tính chất, nên ta **sift up / bubble up (상향 이동)**:

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

Trước khi đọc đoạn triển khai, hãy giữ invariant và complexity mà thuật toán phải bảo toàn. Code bên dưới là một cách hiện thực hóa; cần đối chiếu output, ownership và edge case với mô hình vừa học.

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

Comparator phải tạo thứ tự (ordering / 순서) nhất quán. Nếu comparator không transitive, vùng nhớ động (heap / 힙) tính chất không còn meaningful.

> **Chuyển mạch:** Trong **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **Extract-min: sửa nút gốc bằng last phần tử** tiếp nhận điểm tựa từ **Chèn: giữ hình dạng trước, sửa thứ tự sau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **xây dựng vùng nhớ động (heap / 힙): vì sao O(n) chứ không phải O(n log n)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Extract-min: sửa nút gốc bằng last phần tử

nút gốc là minimum. Khi remove nút gốc, nếu chỉ xóa `a[0]`, complete-tree cách biểu diễn sẽ bị hỏng. Cách chuẩn là:

1. lưu nút gốc làm answer;
2. chuyển last phần tử lên nút gốc;
3. giảm kích thước (size / 크기);
4. sift-down nút gốc tới khi vùng nhớ động (heap / 힙) tính chất được phục hồi.

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

> **Chuyển mạch:** Ở chặng này của **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **xây dựng vùng nhớ động (heap / 힙): vì sao O(n) chứ không phải O(n log n)?** tiếp nhận điểm tựa từ **Extract-min: sửa nút gốc bằng last phần tử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **hàng đợi ưu tiên là sự trừu tượng (abstraction), vùng nhớ động (heap / 힙) là cách triển khai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## xây dựng vùng nhớ động (heap / 힙): vì sao `O(n)` chứ không phải `O(n log n)`?

Một cách ngây thơ là insert từng phần tử, cho `O(n log n)`. Nhưng nếu toàn bộ mảng đã có sẵn, ta có thể gọi sift-down từ nút cha cuối cùng đi ngược lên nút gốc.

Thoạt nhìn có `n` các nút và mỗi sift có thể `O(log n)`, nên dễ đoán `O(n log n)`. Nhưng phần lớn các nút nằm gần các nút lá và hầu như không cần đi xa.

Khoảng một nửa các nút là các nút lá, chi phí 0. Khoảng một phần tư có chiều cao 1, một phần tám có chiều cao 2, v.v. Tổng công việc (work / 작업) gần:

\[
n\left(\frac{1}{4}\cdot1+\frac{1}{8}\cdot2+\frac{1}{16}\cdot3+\cdots\right)=O(n)
\]

Đây là ví dụ quan trọng của **aggregate phân tích (analysis / 분석)**: không thể lấy worst chi phí của một nút rồi nhân cho mọi nút nếu phân phối của công việc (work / 작업) rất không đều.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **hàng đợi ưu tiên là sự trừu tượng (abstraction), vùng nhớ động (heap / 힙) là cách triển khai** tiếp nhận điểm tựa từ **xây dựng vùng nhớ động (heap / 힙): vì sao O(n) chứ không phải O(n log n)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Comparator pitfalls trong Java** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## hàng đợi ưu tiên là sự trừu tượng (abstraction), vùng nhớ động (heap / 힙) là cách triển khai

**hàng đợi ưu tiên (우선순위 큐)** là ADT mô tả các thao tác như:

```text
insert(item, priority)
peek-best()
extract-best()
```

đống nhị phân chỉ là một cách triển khai rất phổ biến. hàng đợi ưu tiên cũng có thể được implement bằng balanced cây, ngăn băm queues, Fibonacci vùng nhớ động (heap / 힙), pairing vùng nhớ động (heap / 힙) hoặc chuyên biệt monotonic queues tùy khối lượng công việc.

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

> **Chuyển mạch:** Trong **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **Comparator pitfalls trong Java** tiếp nhận điểm tựa từ **hàng đợi ưu tiên là sự trừu tượng (abstraction), vùng nhớ động (heap / 힙) là cách triển khai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vùng nhớ vùng nhớ động (heap / 힙) không hỗ trợ tìm kiếm tùy ý tốt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **Vùng nhớ vùng nhớ động (heap / 힙) không hỗ trợ tìm kiếm tùy ý tốt** tiếp nhận điểm tựa từ **Comparator pitfalls trong Java** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vùng nhớ vùng nhớ động (heap / 힙) Sort** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vùng nhớ vùng nhớ động (heap / 힙) không hỗ trợ tìm kiếm tùy ý tốt

Trong đống nhỏ nhất, biết `parent <= child` không cho biết đích nằm ở nhánh nào. Nếu đích lớn hơn nút gốc, cả hai các cây con đều có thể chứa nó. Vì vậy tìm một arbitrary giá trị vẫn có thể:

\[
O(n)
\]

Đây là khác biệt bản chất với BST. vùng nhớ động (heap / 힙) tối ưu **extreme retrieval**, BST tối ưu **ordered tìm kiếm (search / 검색) theo khóa**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **Vùng nhớ vùng nhớ động (heap / 힙) Sort** tiếp nhận điểm tựa từ **Vùng nhớ vùng nhớ động (heap / 힙) không hỗ trợ tìm kiếm tùy ý tốt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Top-K và bounded bộ nhớ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vùng nhớ vùng nhớ động (heap / 힙) Sort

Vùng nhớ vùng nhớ động (heap / 힙) có thể dùng để sort in-place:

1. xây dựng đống lớn nhất `O(n)`;
2. swap nút gốc lớn nhất với cuối mảng;
3. giảm vùng nhớ động (heap / 힙) kích thước (size / 크기);
4. sift-down nút gốc;
5. lặp lại.

Thời gian (time / 시간):

\[
O(n\log n)
\]

Vùng nhớ vùng nhớ động (heap / 힙) sort có trường hợp xấu nhất tốt và có thể in-place với `O(1)` extra mảng không gian (space / 공간), nhưng thường bộ nhớ đệm hành vi và constant factor không tốt bằng các sort thực dụng khác. Nó cũng không ổn định theo cách triển khai chuẩn.

Điểm đáng học là vùng nhớ động (heap / 힙) sort cho thấy cùng bất biến “nút gốc là extreme” có thể được dùng để xác định phần tử cuối của hậu tố đã sắp xếp từng bước.

> **Chuyển mạch:** Trong **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **Top-K và bounded bộ nhớ** tiếp nhận điểm tựa từ **Vùng nhớ vùng nhớ động (heap / 힙) Sort** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **K-way merge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Top-K và bounded bộ nhớ

Nếu luồng có `n` phần tử nhưng chỉ cần `k` phần tử lớn nhất, sắp xếp toàn bộ sẽ tạo nhiều thông tin thứ tự không cần thiết.

Giữ **đống nhỏ nhất kích thước (size / 크기) `k`**:

```text
nếu heap chưa đủ k -> push
nếu x <= heap.min -> bỏ
nếu x > heap.min -> pop min rồi push x
```

Thời gian (time / 시간):

\[
O(n\log k)
\]

bộ nhớ:

\[
O(k)
\]

Khi `k << n`, đây là cải thiện quan trọng cả về thời gian lẫn bộ nhớ. Mẫu này xuất hiện trong xếp hạng ứng viên, giám sát, hệ gợi ý, tổng hợp kết quả tìm kiếm và các giai đoạn Top-K phân tán.

> **Chuyển mạch:** Ở chặng này của **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **K-way merge** tiếp nhận điểm tựa từ **Top-K và bounded bộ nhớ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dijkstra và decrease-key** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## K-way merge

Giả sử có `k` danh sách đã sắp xếp với tổng `N` phần tử. Ta đưa phần tử đầu của mỗi danh sách vào đống nhỏ nhất. Mỗi lần lấy phần tử nhỏ nhất ra, ta chỉ tiến trong đúng danh sách đó rồi đưa phần tử tiếp theo vào vùng nhớ động (heap / 힙).

Vùng nhớ vùng nhớ động (heap / 힙) chỉ chứa tối đa `k` heads:

\[
O(N\log k)
\]

Đây là cốt lõi (core / 핵심) idea của bên ngoài sắp xếp trộn, merge SSTables, merge log streams và nhiều chuỗi xử lý xử lý sorted runs.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **Dijkstra và decrease-key** tiếp nhận điểm tựa từ **K-way merge** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Scheduler và sự kiện simulation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dijkstra và decrease-key

Classical Dijkstra thường được mô tả với `decrease-key`: nếu khoảng cách của đỉnh giảm, cập nhật độ ưu tiên của mục đang trong vùng nhớ động (heap / 힙).

Nhiều tiêu chuẩn (standard / 표준) `PriorityQueue` APIs không hỗ trợ cập nhật độ ưu tiên trực tiếp. Có hai mẫu chính.

### mẫu 1: stale các mục

Mỗi khi có khoảng cách tốt hơn, push mục mới. Khi pop:

```java
if (cur.dist() != dist[cur.node()]) continue;
```

mục cũ trở thành stale và được bỏ qua.

Ưu điểm là cách triển khai đơn giản; nhược điểm là vùng nhớ động (heap / 힙) có các phần tử trùng và bộ nhớ/công việc (work / 작업) tăng.

### mẫu 2: indexed vùng nhớ động (heap / 힙)

Duy trì:

```text
position[item] -> heap index
```

Mỗi swap phải cập nhật `position`. Khi độ ưu tiên thay đổi, tìm item trực tiếp rồi sift-up/sift-down `O(log n)`.

mẫu này hữu ích khi độ ưu tiên cập nhật rất thường xuyên và định danh (identity / 식별자) của item quan trọng.

> **Chuyển mạch:** Trong **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **Scheduler và sự kiện simulation** tiếp nhận điểm tựa từ **Dijkstra và decrease-key** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Median trực tuyến bằng hai heaps** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Scheduler và sự kiện simulation

hàng đợi ưu tiên không chỉ dùng trong các thuật toán đồ thị. Một sự kiện-driven simulator có các sự kiện với timestamp; mỗi bước lấy sự kiện có thời gian sớm nhất. Scheduler có thể lấy tác vụ (task / 작업) có deadline/độ ưu tiên cao nhất. Timer wheel, calendar hàng đợi (queue / 큐) hoặc vùng nhớ động (heap / 힙) đều là cách tổ chức “next sự kiện”.

Điểm chung là tải công việc không cần toàn bộ sự kiện được sắp xếp hoàn chỉnh; nó chỉ liên tục cần **phần tử tốt nhất tiếp theo**.

> **Chuyển mạch:** Ở chặng này của **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **Median trực tuyến bằng hai heaps** tiếp nhận điểm tựa từ **Scheduler và sự kiện simulation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **D-ary vùng nhớ động (heap / 힙) và branching-factor sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Median là nút gốc của vùng nhớ động (heap / 힙) lớn hơn hoặc average của hai các nút gốc.

Mỗi insert `O(log n)`, median truy vấn `O(1)`.

Đây là ví dụ composition: hai heaps phối hợp để duy trì một ranh giới thống kê thứ tự.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **D-ary vùng nhớ động (heap / 힙) và branching-factor sự đánh đổi (trade-off / 트레이드오프)** tiếp nhận điểm tựa từ **Median trực tuyến bằng hai heaps** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **tính ổn định và quy tắc phân xử khi bằng nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## D-ary vùng nhớ động (heap / 힙) và branching-factor sự đánh đổi (trade-off / 트레이드오프)

đống nhị phân có 2 các nút con. Có thể dùng d-ary vùng nhớ động (heap / 힙) với `d` các nút con mỗi nút. chiều cao giảm còn khoảng:

\[
\log_d n
\]

nhưng sift-down phải inspect tới `d` các nút con để chọn best. khối lượng công việc nhiều decrease-key/insert so với extract-min có thể hưởng lợi từ hệ số phân nhánh lớn hơn; bộ nhớ đệm hành vi cũng có thể thay đổi.

cấu trúc dữ liệu thiết kế (design / 설계) không phải chỉ chọn “vùng nhớ động (heap / 힙) hay không”, mà còn chọn cách biểu diễn phù hợp thao tác mix.

> **Chuyển mạch:** Trong **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **tính ổn định và quy tắc phân xử khi bằng nhau** tiếp nhận điểm tựa từ **D-ary vùng nhớ động (heap / 힙) và branching-factor sự đánh đổi (trade-off / 트레이드오프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **có thể thay đổi độ ưu tiên các đối tượng: một bug phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## tính ổn định và quy tắc phân xử khi bằng nhau

hàng đợi ưu tiên thường không đảm bảo ổn định thứ tự (order / 순서) giữa items có cùng độ ưu tiên. Nếu lĩnh vực (domain / 도메인) cần FIFO trong cùng độ ưu tiên, comparator nên thêm số thứ tự:

```text
(priority, insertionSequence)
```

Ví dụ job bộ lập lịch có thể cần “độ ưu tiên cao trước; nếu bằng nhau, tác vụ (task / 작업) đến trước chạy trước”. quy tắc phân xử khi bằng nhau là part của lĩnh vực (domain / 도메인) ngữ nghĩa (semantics / 의미론), không phải chi tiết phụ.

> **Chuyển mạch:** Ở chặng này của **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **có thể thay đổi độ ưu tiên các đối tượng: một bug phổ biến** tiếp nhận điểm tựa từ **tính ổn định và quy tắc phân xử khi bằng nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vùng nhớ vùng nhớ động (heap / 힙) với C: quyền sở hữu (ownership / 소유권) và sức chứa (capacity / 용량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## có thể thay đổi độ ưu tiên các đối tượng: một bug phổ biến

Nếu vùng nhớ động (heap / 힙) chứa đối tượng rồi độ ưu tiên trường của đối tượng bị mutate trực tiếp, vùng nhớ động (heap / 힙) không tự biết để rearrange. vùng nhớ động (heap / 힙) mảng vẫn giữ shape cũ và bất biến có thể sai.

Do đó hoặc:

- các đối tượng bất biến sau khi tạo về độ ưu tiên;
- dùng tường minh (explicit / 명시적) cập nhật/decrease-key;
- push mục mới và dùng stale-entry/phiên bản (version / 버전) mẫu.

Trong Java, mutate đối tượng đang ở `PriorityQueue` không khiến hàng đợi (queue / 큐) reheapify tự động.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, sau nội dung của **có thể thay đổi độ ưu tiên các đối tượng: một bug phổ biến**, **Vùng nhớ vùng nhớ động (heap / 힙) với C: quyền sở hữu (ownership / 소유권) và sức chứa (capacity / 용량)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vùng nhớ vùng nhớ động (heap / 힙) với C: quyền sở hữu (ownership / 소유권) và sức chứa (capacity / 용량)

Trong C, đống nhị phân thường là mảng động struct:

```c
typedef struct {
    Item *data;
    size_t size;
    size_t cap;
} Heap;
```

Ngoài vùng nhớ động (heap / 힙) bất biến, cách triển khai phải giữ thêm sức chứa (capacity / 용량) bất biến và quyền sở hữu của `data`. `realloc` thất bại (failure / 실패), đối tượng vòng đời (lifetime) và comparator callback là concerns mà Java/JavaScript môi trường chạy (runtime) che bớt.

Nếu item lớn, có thể vùng nhớ động (heap / 힙) các con trỏ thay vì bản sao (copy / 복사) structs, nhưng tính cục bộ và quyền sở hữu ngữ nghĩa thay đổi.

> **Chuyển mạch:** Trong **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **Những hiểu lầm phổ biến** tiếp nhận điểm tựa từ **Vùng nhớ vùng nhớ động (heap / 힙) với C: quyền sở hữu (ownership / 소유권) và sức chứa (capacity / 용량)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **kiểm thử vùng nhớ động (heap / 힙) bằng bất biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“vùng nhớ động (heap / 힙) là mảng đã sắp xếp dưới dạng cây.”** Sai. vùng nhớ động (heap / 힙) chỉ partial-order.

**“Xây dựng vùng nhớ động (heap / 힙) phải `O(n log n)` vì mỗi lần chèn tốn `O(log n)`.”** Điều này chỉ đúng nếu xây dựng bằng cách chèn lặp lại. Heapify từ dưới lên (**bottom-up heapify**) là `O(n)`.

**“đống nhỏ nhất giúp binary-search một giá trị.”** Không. vùng nhớ động (heap / 힙) không có BST thứ tự (ordering / 순서) giữa left/right các cây con.

**“PriorityQueue hỗ trợ thay độ ưu tiên của đối tượng tự động.”** Thường không. sự thay đổi dữ liệu ngoài vùng nhớ động (heap / 힙) các thao tác có thể phá bất biến.

**“vùng nhớ động (heap / 힙) luôn tốt hơn mảng đã sắp xếp cho min.”** Nếu dataset tĩnh và cần iterate thứ tự đã sắp xếp nhiều lần, sort một lần có thể tốt hơn. vùng nhớ động (heap / 힙) hữu ích khi collection mutate và lặp lại cần extreme.

> **Chuyển mạch:** Ở chặng này của **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **kiểm thử vùng nhớ động (heap / 힙) bằng bất biến** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy mở rộng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## kiểm thử vùng nhớ động (heap / 힙) bằng bất biến

Sau ngẫu nhiên chuỗi (sequence / 시퀀스) push/pop, kiểm:

```text
for every i > 0:
    compare(parent(i), i) <= 0
```

Đồng thời nên so sánh dãy phần tử lấy ra với kết quả tham chiếu từ `sort()` trên các tập dữ liệu nhỏ. Với đống có chỉ mục (indexed heap), cần kiểm tra thêm tính nhất quán hai chiều:

```text
position[item] = i
heap[i] = item
```

Lỗi vùng nhớ động (heap / 힙) thường xuất hiện ở các trường hợp biên: rỗng, chỉ một phần tử, chỉ có nút con trái, các phần tử có cùng độ ưu tiên, trường hợp bộ so sánh trả hòa và lần đổi chỗ cuối cùng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vùng nhớ vùng nhớ động (heap / 힙) và hàng đợi ưu tiên**, **Mô hình tư duy mở rộng** gom các mảnh từ **kiểm thử vùng nhớ động (heap / 힙) bằng bất biến** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy mở rộng

> vùng nhớ động (heap / 힙) là một **động frontier cấu trúc (structure / 구조)**. Nó không cố giữ toàn bộ dữ liệu ordered; nó giữ đủ cục bộ bất biến để câu hỏi “ai là ứng viên tốt nhất tiếp theo?” luôn trả lời rẻ.

Khi gặp một thuật toán có loop kiểu “liên tục chọn ứng viên nhỏ nhất/lớn nhất rồi sinh thêm các ứng viên”, hãy nghĩ tới hàng đợi ưu tiên. Sau đó mới hỏi đống nhị phân có đúng mô hình chi phí không, có cần decrease-key không, có bounded độ ưu tiên domain để dùng ngăn băm không, và quy tắc phân xử khi bằng nhau ngữ nghĩa là gì.

> **Bàn giao:** Sau **Mô hình tư duy mở rộng**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
