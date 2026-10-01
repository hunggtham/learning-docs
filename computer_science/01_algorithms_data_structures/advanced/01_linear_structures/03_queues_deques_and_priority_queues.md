# Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Hàng đợi (queue / 큐) và nguyên tắc FIFO** xác định điều kiện hoặc ranh giới mà các cơ chế sau phải tôn trọng; sau đó sang **Vì sao BFS cần FIFO?** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**hàng đợi (queue / 큐), Deque & Priority hàng đợi (queue / 큐) / 큐, 덱, 우선순위 큐**

Hàng đợi (queue / 큐), deque và priority hàng đợi (queue / 큐) đều quản lý một tập phần tử “đang chờ”, nhưng khác nhau ở **chính sách chọn phần tử tiếp theo (selection policy)**. Khác biệt tưởng nhỏ này lại quyết định trực tiếp tính đúng đắn của nhiều thuật toán.

BFS cần FIFO để bảo toàn thứ tự theo tầng. Dijkstra cần phần tử có tentative distance nhỏ nhất. Sliding-window maximum cần deque duy trì đồng thời thứ tự thời gian và quan hệ ưu thế về giá trị.

Vì vậy hàng đợi (queue / 큐) không chỉ là một bộ chứa (container / 컨테이너); nó là một lớp trừu tượng (abstraction / 추상화) về **thứ tự phục vụ**.

## Hàng đợi (queue / 큐) và nguyên tắc FIFO

Hàng đợi (queue / 큐) dùng nguyên tắc **vào trước, ra trước (First In, First Out – FIFO / 선입선출)**.

```java
Queue<Integer> q = new ArrayDeque<>();
q.offer(10);
q.offer(20);
System.out.println(q.poll()); // 10
```

Bất biến lô-gic (logic / 논리):

> Các phần tử còn trong hàng đợi (queue / 큐) xuất hiện theo đúng thứ tự enqueue chưa bị dequeue.

Đây là lý do hàng đợi (queue / 큐) phù hợp với yêu cầu (request / 요청) arrival thứ tự (order / 순서), sự kiện (event / 이벤트) processing, producer–bên tiêu thụ (consumer / 소비자) chuỗi xử lý (pipeline / 파이프라인) và BFS.

> **Chuyển mạch:** Trong **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Vì sao BFS cần FIFO?** tiếp nhận điểm tựa từ **Hàng đợi (queue / 큐) và nguyên tắc FIFO** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hàng đợi (queue / 큐) API cũng là một đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao BFS cần FIFO?

Trong đồ thị (graph / 그래프) không trọng số, mỗi cạnh tăng độ dài đường đi thêm đúng 1. Khi BFS lấy một nút (node / 노드) có distance `d`, các nút (node / 노드) đã được discover trước nó có distance không lớn hơn `d`; các neighbor mới được thêm với distance `d+1`.

FIFO bảo đảm frontier được xử lý theo lớp khoảng cách không giảm.

Nếu thay hàng đợi (queue / 큐) bằng ngăn xếp (stack / 스택), ta có DFS và mất shortest-path guarantee theo số cạnh. Nếu thay bằng min-heap theo weight, ta chuyển sang một chính sách (policy / 정책) gần Dijkstra.

Do đó cấu trúc frontier không phải chi tiết hiện thực (implementation / 구현); nó là một phần của proof.

> **Chuyển mạch:** Ở chặng này của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Hàng đợi (queue / 큐) API cũng là một đặc tả hợp đồng (contract / 계약)** tiếp nhận điểm tựa từ **Vì sao BFS cần FIFO?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao shift mảng là thiết kế hàng đợi (queue / 큐) kém?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hàng đợi (queue / 큐) API cũng là một đặc tả hợp đồng (contract / 계약)

Một hàng đợi (queue / 큐) thực tế phải định nghĩa rõ:

```text
enqueue khi đầy làm gì?
dequeue khi rỗng làm gì?
capacity có cố định không?
operation có block không?
null có phải một giá trị hợp lệ không?
queue có thread-safe không?
iteration có snapshot hay live view?
```

Trong Java, `offer` và `add` có ngữ nghĩa (semantics / 의미론) khác khi hàng đợi (queue / 큐) từ chối phần tử; `poll/peek` khác `remove/element` khi hàng đợi (queue / 큐) rỗng.

Trong C, một API rõ thường dùng:

```c
bool queue_pop(Queue *q, Item *out);
```

thay vì dùng magic sentinel có thể trùng dữ liệu thật.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Vì sao shift mảng là thiết kế hàng đợi (queue / 큐) kém?** tiếp nhận điểm tựa từ **Hàng đợi (queue / 큐) API cũng là một đặc tả hợp đồng (contract / 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ring buffer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao shift mảng là thiết kế hàng đợi (queue / 큐) kém?

Nếu dequeue luôn dịch toàn bộ phần tử còn lại sang trái, mỗi lần dequeue tốn `O(n)`.

Cách tốt hơn là giữ `head` chỉ mục (index / 인덱스):

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

Head-index tránh shift mỗi thao tác (operation / 연산), nhưng cần compaction nếu thời gian chạy (runtime / 런타임) vẫn giữ references cũ trong backing array quá lâu.

> **Chuyển mạch:** Trong **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Ring buffer** tiếp nhận điểm tựa từ **Vì sao shift mảng là thiết kế hàng đợi (queue / 큐) kém?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nhiều convention của ring buffer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ring buffer

**Bộ đệm vòng (ring buffer / 원형 버퍼)** dùng một mảng và cho chỉ số quay lại đầu khi chạm cuối.

Một biểu diễn (representation / 표현) dễ lập luận (reasoning / 추론) giữ:

```text
capacity
head
size
```

Tail được suy ra:

\[
tail=(head+size)\bmod sức chứa (capacity / 용량)
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

> **Chuyển mạch:** Ở chặng này của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Nhiều convention của ring buffer** tiếp nhận điểm tựa từ **Ring buffer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sức chứa (capacity / 용량) là lũy thừa của hai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhiều convention của ring buffer

Có ít nhất ba cách phổ biến:

```text
head + size
head/tail và chừa một slot rỗng
head/tail + cờ full
```

Không có convention duy nhất đúng. Sai lầm thường đến từ việc trộn hai convention trong cùng hiện thực (implementation / 구현).

Một proof tốt phải xác định chính xác:

```text
head trỏ phần tử đầu hay slot trống kế tiếp?
tail trỏ phần tử cuối hay slot trống kế tiếp?
full được nhận biết bằng gì?
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Sức chứa (capacity / 용량) là lũy thừa của hai** tiếp nhận điểm tựa từ **Nhiều convention của ring buffer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bounded hàng đợi (queue / 큐) và overload chính sách (policy / 정책)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sức chứa (capacity / 용량) là lũy thừa của hai

Nếu `capacity = 2^k`, phép wrap có thể dùng:

```text
index & (capacity - 1)
```

thay modulo.

Nhưng tối ưu này chỉ đúng nếu bất biến (invariant / 불변식) “sức chứa (capacity / 용량) luôn là lũy thừa của hai” được giữ qua mọi resize.

Đây là mẫu chung: tối ưu hóa (optimization / 최적화) bit-level thường tạo thêm một bất biến (invariant / 불변식) cấu trúc.

> **Chuyển mạch:** Trong **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Bounded hàng đợi (queue / 큐) và overload chính sách (policy / 정책)** tiếp nhận điểm tựa từ **Sức chứa (capacity / 용량) là lũy thừa của hai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hàng đợi (queue / 큐) không chữa được thông lượng (throughput / 처리량) deficit dài hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bounded hàng đợi (queue / 큐) và overload chính sách (policy / 정책)

Hàng đợi (queue / 큐) có sức chứa (capacity / 용량) hữu hạn buộc hệ thống trả lời câu hỏi: chuyện gì xảy ra khi đầy?

```text
block producer
reject item
drop newest
drop oldest
overwrite oldest
spill sang disk
scale consumer
```

Đây không còn là chuyện bộ chứa (container / 컨테이너) thuần túy; nó trở thành chính sách (policy / 정책) về độ tin cậy (reliability / 신뢰성) và backpressure.

> **Chuyển mạch:** Ở chặng này của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Hàng đợi (queue / 큐) không chữa được thông lượng (throughput / 처리량) deficit dài hạn** tiếp nhận điểm tựa từ **Bounded hàng đợi (queue / 큐) và overload chính sách (policy / 정책)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Little's Law** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hàng đợi (queue / 큐) không chữa được thông lượng (throughput / 처리량) deficit dài hạn

Giả sử tốc độ đến trung bình là `λ` và tốc độ xử lý trung bình là `μ`.

Nếu trong thời gian dài:

\[
\lambda > \mu
\]

thì hàng đợi (queue / 큐) có xu hướng dài ra. hàng đợi (queue / 큐) lớn chỉ trì hoãn hậu quả bằng cách đổi overload thành bộ nhớ (memory / 메모리) growth và độ trễ (latency / 지연 시간) growth.

Mô hình tư duy:

> hàng đợi (queue / 큐) hấp thụ burst ngắn hạn; nó không tạo thêm năng lực xử lý dài hạn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Little's Law** tiếp nhận điểm tựa từ **Hàng đợi (queue / 큐) không chữa được thông lượng (throughput / 처리량) deficit dài hạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hàng đợi (queue / 큐) và batching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Little's Law

Trong trạng thái ổn định, một trực giác quan trọng của queueing lý thuyết (theory / 이론) là:

\[
L=\lambda W
\]

trong đó:

```text
L = số item trung bình trong hệ thống
λ = throughput
W = thời gian trung bình một item ở trong hệ thống
```

Nếu thông lượng (throughput / 처리량) không đổi mà hàng đợi (queue / 큐) length tăng, thời gian chờ trung bình cũng tăng.

Tăng sức chứa (capacity / 용량) không tự giảm độ trễ (latency / 지연 시간); nó chỉ cho phép nhiều item chờ hơn.

> **Chuyển mạch:** Trong **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Hàng đợi (queue / 큐) và batching** tiếp nhận điểm tựa từ **Little's Law** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Deque** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hàng đợi (queue / 큐) và batching

Một bên tiêu thụ (consumer / 소비자) có thể xử lý từng item hoặc gom batch.

Batching có thể giảm overhead cố định trên mỗi item, ví dụ mạng (network / 네트워크) syscall, disk ghi (write / 쓰기) hoặc cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션). Nhưng batch lớn thường tăng độ trễ (latency / 지연 시간) vì item đầu phải chờ batch đủ hoặc hết thời gian chờ (timeout / 타임아웃).

Đây là một sự đánh đổi (trade-off / 트레이드오프) hệ thống:

```text
batch lớn -> throughput tốt hơn, latency thường cao hơn
batch nhỏ -> latency tốt hơn, overhead trên mỗi item cao hơn
```

Hàng đợi (queue / 큐) là nơi chính sách (policy / 정책) batching thường được thực hiện.

> **Chuyển mạch:** Ở chặng này của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Deque** tiếp nhận điểm tựa từ **Hàng đợi (queue / 큐) và batching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Deque bằng ring buffer động** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deque

**Double-Ended hàng đợi (queue / 큐)** hỗ trợ thao tác ở cả hai đầu:

```text
pushFront
pushBack
popFront
popBack
peekFront
peekBack
```

Deque có thể dùng như ngăn xếp (stack / 스택) hoặc hàng đợi (queue / 큐), nhưng sức mạnh thật xuất hiện khi thuật toán cần hai đầu với vai trò khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Deque bằng ring buffer động** tiếp nhận điểm tựa từ **Deque** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Monotonic deque** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deque bằng ring buffer động

Một array deque thường dùng ring buffer có thể resize.

Về lô-gic (logic / 논리), chuỗi (sequence / 시퀀스) là liên tục. Về vật lý, nó có thể bị chia thành hai đoạn:

```text
[tail segment .........] [......... head segment]
```

Resize phải bản sao (copy / 복사) theo **thứ tự lô-gic (logic / 논리)**, không phải đơn giản bản sao (copy / 복사) vùng nhớ từ chỉ mục (index / 인덱스) 0 tới cuối.

Đây là một ví dụ biểu diễn (representation / 표현) vật lý khác với thứ tự lớp trừu tượng (abstraction / 추상화).

> **Chuyển mạch:** Trong **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Monotonic deque** tiếp nhận điểm tựa từ **Deque bằng ring buffer động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dominance trong monotonic deque** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Monotonic deque

Sliding-window maximum là ví dụ kinh điển.

Deque giữ chỉ mục (index / 인덱스) với hai bất biến (invariant / 불변식):

```text
index tăng từ front tới back
giá trị giảm từ front tới back
```

Khi thêm `i`, loại ở back mọi chỉ mục (index / 인덱스) `j` có:

```text
a[j] <= a[i]
```

vì `i` mới hơn và không nhỏ hơn. `j` sẽ hết hạn trước `i` và không thể thắng `i` trong bất kỳ cửa sổ (window / 윈도우) tương lai chứa cả hai.

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

Mỗi chỉ mục (index / 인덱스) vào deque một lần và ra tối đa một lần, nên tổng thời gian `O(n)`.

Inner `while` không làm thuật toán `O(n²)` vì tổng số pop bị chặn tuyến tính.

> **Chuyển mạch:** Ở chặng này của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Dominance trong monotonic deque** tiếp nhận điểm tựa từ **Monotonic deque** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **0–1 BFS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Đây là một ví dụ rất rõ của trạng thái (state / 상태) pruning bằng dominance.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **0–1 BFS** tiếp nhận điểm tựa từ **Dominance trong monotonic deque** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Priority hàng đợi (queue / 큐) là ADT, vùng nhớ động (heap / 힙) chỉ là hiện thực (implementation / 구현) phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 0–1 BFS

Nếu edge weight chỉ là `0` hoặc `1`, ta không cần full Priority hàng đợi (queue / 큐).

```text
weight 0 -> pushFront
weight 1 -> pushBack
```

Deque giữ đủ thứ tự (ordering / 순서) để nút (node / 노드) có tentative distance nhỏ hơn được xử lý trước.

Độ phức tạp:

\[
O(V+E)
\]

trong biểu diễn (representation / 표현) adjacency danh sách (list / 목록).

0–1 BFS cho thấy selection chính sách (policy / 정책) có thể được chuyên biệt khi miền priority bị giới hạn.

> **Chuyển mạch:** Trong **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Priority hàng đợi (queue / 큐) là ADT, vùng nhớ động (heap / 힙) chỉ là hiện thực (implementation / 구현) phổ biến** tiếp nhận điểm tựa từ **0–1 BFS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nhị phân (binary / 이진) vùng nhớ động (heap / 힙) và shape bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Priority hàng đợi (queue / 큐) là ADT, vùng nhớ động (heap / 힙) chỉ là hiện thực (implementation / 구현) phổ biến

Priority hàng đợi (queue / 큐) hỗ trợ dạng thao tác:

```text
insert(item, priority)
peekMin / peekMax
extractMin / extractMax
```

Nhị phân (binary / 이진) vùng nhớ động (heap / 힙) phổ biến vì cân bằng tốt giữa locality, bộ nhớ (memory / 메모리) và `O(log n)` cập nhật (update / 업데이트). Nhưng Priority hàng đợi (queue / 큐) còn có thể được cài bằng:

```text
balanced tree
bucket queue
radix heap
pairing heap
Fibonacci heap
indexed heap
specialized calendar/event structure
```

Không nên đồng nhất Priority hàng đợi (queue / 큐) với nhị phân (binary / 이진) vùng nhớ động (heap / 힙).

> **Chuyển mạch:** Ở chặng này của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Nhị phân (binary / 이진) vùng nhớ động (heap / 힙) và shape bất biến (invariant / 불변식)** tiếp nhận điểm tựa từ **Priority hàng đợi (queue / 큐) là ADT, vùng nhớ động (heap / 힙) chỉ là hiện thực (implementation / 구현) phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bản dựng (build / 빌드) vùng nhớ động (heap / 힙) là O(n), không phải O(n log n)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhị phân (binary / 이진) vùng nhớ động (heap / 힙) và shape bất biến (invariant / 불변식)

Nhị phân (binary / 이진) vùng nhớ động (heap / 힙) thường dùng mảng. Với zero-based chỉ mục (index / 인덱스):

```text
parent(i) = (i - 1) / 2
left(i)   = 2i + 1
right(i)  = 2i + 2
```

Hai bất biến (invariant / 불변식):

```text
shape là complete binary tree
heap-order đúng trên mọi cạnh cha-con
```

Insert giữ shape bằng cách thêm cuối, rồi sift-up sửa thứ tự (order / 순서). Extract gốc (root / 루트) giữ shape bằng cách đưa phần tử cuối lên gốc (root / 루트), giảm kích thước (size / 크기) rồi sift-down.

Một mutation chỉ phá thứ tự (order / 순서) trên một đường, nên không cần xây lại toàn vùng nhớ động (heap / 힙).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Bản dựng (build / 빌드) vùng nhớ động (heap / 힙) là O(n), không phải O(n log n)** tiếp nhận điểm tựa từ **Nhị phân (binary / 이진) vùng nhớ động (heap / 힙) và shape bất biến (invariant / 불변식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Priority hàng đợi (queue / 큐) và tie-breaking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bản dựng (build / 빌드) vùng nhớ động (heap / 힙) là O(n), không phải O(n log n)

Nếu insert từng phần tử một, tổng có thể `O(n log n)`.

Nhưng bottom-up heapify gọi sift-down từ các nội bộ (internal / 내부) nút (node / 노드) cho tổng thời gian `O(n)`.

Trực giác: phần lớn nút (node / 노드) nằm gần lá và chỉ có thể đi xuống rất ít bước. Chỉ rất ít nút (node / 노드) ở gần gốc (root / 루트) có chiều cao lớn.

Đây là ví dụ cần phân tích tổng chi phí (cost / 비용) theo độ cao của nút (node / 노드) thay vì nhân “n nút (node / 노드) × log n” một cách thô.

> **Chuyển mạch:** Trong **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Priority hàng đợi (queue / 큐) và tie-breaking** tiếp nhận điểm tựa từ **Bản dựng (build / 빌드) vùng nhớ động (heap / 힙) là O(n), không phải O(n log n)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mutable priority là một bẫy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Priority hàng đợi (queue / 큐) và tie-breaking

Priority không nhất thiết chỉ là một số.

Ví dụ scheduler:

```text
1. deadline sớm hơn
2. priority class cao hơn
3. sequence number nhỏ hơn
```

Nếu hai item có cùng priority nhưng nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론) yêu cầu FIFO, cần chuỗi (sequence / 시퀀스) number để làm tie-breaker.

Vùng nhớ vùng nhớ động (heap / 힙) bản thân không cam kết stable thứ tự (order / 순서) giữa các key bằng nhau.

> **Chuyển mạch:** Ở chặng này của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Priority hàng đợi (queue / 큐) và tie-breaking** đã nêu tiêu chí phân biệt, còn **Mutable priority là một bẫy** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Lazy deletion trong Dijkstra** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mutable priority là một bẫy

Nếu một đối tượng (object / 객체) đã nằm trong vùng nhớ động (heap / 힙) rồi priority trường dữ liệu (field / 필드) bị sửa trực tiếp, vùng nhớ động (heap / 힙) không tự biết phải reheapify.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Mutable priority là một bẫy** đã nêu tiêu chí phân biệt, còn **Lazy deletion trong Dijkstra** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Indexed vùng nhớ động (heap / 힙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lazy deletion trong Dijkstra

Một mẫu (pattern / 패턴):

```java
record State(int node, long dist) {}
```

Khi tìm được distance mới tốt hơn, chèn một `State` mới. Khi pop:

```text
nếu state.dist != dist[state.node] -> stale, bỏ qua
```

Vùng nhớ vùng nhớ động (heap / 힙) có thể chứa nhiều phiên bản (version / 버전) của cùng nút (node / 노드), nhưng tính đúng đắn (correctness / 정확성) vẫn được giữ nhờ kiểm tra phiên bản (version / 버전) lô-gic (logic / 논리) qua distance hiện tại.

Sự đánh đổi (trade-off / 트레이드오프):

```text
implementation đơn giản
heap có thể lớn hơn
nhiều stale entry hơn
```

> **Chuyển mạch:** Trong **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Indexed vùng nhớ động (heap / 힙)** tiếp nhận điểm tựa từ **Lazy deletion trong Dijkstra** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **d-ary vùng nhớ động (heap / 힙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Indexed vùng nhớ động (heap / 힙)

Nếu cần `decreaseKey` thật sự, có thể lưu:

```text
heap[pos] = item
position[item] = pos
```

Mỗi swap trong vùng nhớ động (heap / 힙) phải cập nhật `position`.

Bất biến liên cấu trúc:

```text
position[heap[i]] == i
```

Indexed vùng nhớ động (heap / 힙) giảm duplicate entry nhưng hiện thực (implementation / 구현) phức tạp hơn đáng kể.

> **Chuyển mạch:** Ở chặng này của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **d-ary vùng nhớ động (heap / 힙)** tiếp nhận điểm tựa từ **Indexed vùng nhớ động (heap / 힙)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bucket hàng đợi (queue / 큐)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## d-ary vùng nhớ động (heap / 힙)

Nhị phân (binary / 이진) vùng nhớ động (heap / 힙) có 2 child mỗi nút (node / 노드). **d-ary vùng nhớ động (heap / 힙)** có `d` child.

Tăng `d` làm chiều cao giảm:

\[
O(\log_d n)
\]

nhưng sift-down phải so nhiều child hơn để chọn child tốt nhất.

Sự đánh đổi (trade-off / 트레이드오프) này có thể hữu ích khi tải công việc (workload / 워크로드) có nhiều decrease-key hoặc khi bộ nhớ (memory / 메모리)/bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작) thuận lợi.

Không có `d` tối ưu chung cho mọi hệ thống.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Bucket hàng đợi (queue / 큐)** tiếp nhận điểm tựa từ **d-ary vùng nhớ động (heap / 힙)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dial's thuật toán (algorithm / 알고리즘)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bucket hàng đợi (queue / 큐)

Nếu priority là integer trong miền nhỏ, có thể dùng array các bucket thay vì vùng nhớ động (heap / 힙).

```text
bucket[p] chứa các item có priority p
```

Extract-min tìm bucket không rỗng nhỏ nhất.

Nếu miền priority nhỏ hoặc hiện tại (current / 현재) minimum tăng đơn điệu, bucket hàng đợi (queue / 큐) có thể nhanh hơn vùng nhớ động (heap / 힙).

Đây là tư duy giống Counting Sort: khai thác miền khóa hẹp để bỏ comparison cây (tree / 트리) tổng quát.

> **Chuyển mạch:** Trong **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Dial's thuật toán (algorithm / 알고리즘)** tiếp nhận điểm tựa từ **Bucket hàng đợi (queue / 큐)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Radix vùng nhớ động (heap / 힙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dial's thuật toán (algorithm / 알고리즘)

Với shortest đường dẫn (path / 경로) có non-negative integer weights bị chặn nhỏ, có thể dùng bucket theo distance modulo/phạm vi (range / 범위) thay vì vùng nhớ động (heap / 힙) tổng quát.

Đây là một ví dụ selection chính sách (policy / 정책) chuyên biệt cho cấu trúc trọng số.

Bài học:

> Khi priority có thêm cấu trúc (structure / 구조), Priority hàng đợi (queue / 큐) tổng quát có thể chưa phải lựa chọn tốt nhất.

> **Chuyển mạch:** Ở chặng này của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Radix vùng nhớ động (heap / 힙)** tiếp nhận điểm tựa từ **Dial's thuật toán (algorithm / 알고리즘)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Priority hàng đợi (queue / 큐) trong sự kiện (event / 이벤트) simulation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Radix vùng nhớ động (heap / 힙)

Radix vùng nhớ động (heap / 힙) khai thác priority integer không giảm theo các lần extract-min và nhóm key theo bit-length của khoảng cách tới last extracted key.

Nó là ví dụ nâng cao cho việc dùng biểu diễn (representation / 표현) bit của priority để giảm chi phí so với comparison vùng nhớ động (heap / 힙) trong một số shortest-path tải công việc (workload / 워크로드).

Không cần dùng thường xuyên, nhưng đáng hiểu để thấy “vùng nhớ động (heap / 힙)” không phải giới hạn cuối của Priority hàng đợi (queue / 큐).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Priority hàng đợi (queue / 큐) trong sự kiện (event / 이벤트) simulation** tiếp nhận điểm tựa từ **Radix vùng nhớ động (heap / 힙)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Scheduler và starvation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Priority hàng đợi (queue / 큐) trong sự kiện (event / 이벤트) simulation

Discrete-event simulation thường giữ sự kiện theo timestamp:

```text
(time, sequence, event)
```

Lấy sự kiện (event / 이벤트) sớm nhất, chạy nó, rồi có thể sinh sự kiện (event / 이벤트) mới trong tương lai.

Ở đây Priority hàng đợi (queue / 큐) chính là “đồng hồ lô-gic (logic / 논리)” của hệ thống mô phỏng.

Nếu cùng timestamp, chuỗi (sequence / 시퀀스) number có thể bảo đảm deterministic thứ tự (order / 순서).

> **Chuyển mạch:** Trong **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Scheduler và starvation** tiếp nhận điểm tựa từ **Priority hàng đợi (queue / 큐) trong sự kiện (event / 이벤트) simulation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-level hàng đợi (queue / 큐)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Scheduler và starvation

Nếu luôn ưu tiên tác vụ (task / 작업) priority cao, tác vụ (task / 작업) thấp có thể không bao giờ được chạy nếu dòng tác vụ (task / 작업) cao liên tục tới. Đây là **starvation**.

Một scheduler thực tế có thể dùng **aging**: priority hiệu dụng của tác vụ (task / 작업) tăng theo thời gian chờ.

Điều này cho thấy priority chính sách (policy / 정책) không chỉ ảnh hưởng hiệu năng (performance / 성능) mà còn fairness.

> **Chuyển mạch:** Ở chặng này của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Multi-level hàng đợi (queue / 큐)** tiếp nhận điểm tựa từ **Scheduler và starvation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Work-stealing deque** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-level hàng đợi (queue / 큐)

Hệ điều hành hoặc hệ thống worker có thể dùng nhiều hàng đợi (queue / 큐):

```text
high priority queue
normal queue
background queue
```

Scheduler chọn giữa các hàng đợi (queue / 큐) theo chính sách (policy / 정책) riêng.

Đây là composition: mỗi hàng đợi (queue / 큐) bên trong có FIFO, còn hệ thống tổng thể có selection chính sách (policy / 정책) hai tầng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Work-stealing deque** tiếp nhận điểm tựa từ **Multi-level hàng đợi (queue / 큐)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SPSC, MPSC, MPMC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Work-stealing deque

Trong parallel thời gian chạy (runtime / 런타임), mỗi worker có thể có deque tác vụ (task / 작업) riêng.

Một mẫu (pattern / 패턴) phổ biến:

```text
worker chủ sở hữu push/pop ở một đầu
worker khác steal từ đầu đối diện
```

Mục tiêu là giảm contention ở dùng chung (common / 공통) trường hợp (case / 사례) nhưng vẫn cân bằng công việc khi một worker rảnh.

Tính đúng đắn (correctness / 정확성) concurrent của work-stealing deque phức tạp hơn deque single-thread rất nhiều vì phải xử lý atomicity và bộ nhớ (memory / 메모리) thứ tự (ordering / 순서).

> **Chuyển mạch:** Trong **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **SPSC, MPSC, MPMC** tiếp nhận điểm tựa từ **Work-stealing deque** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lock-free không có nghĩa wait-free** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SPSC, MPSC, MPMC

Concurrent hàng đợi (queue / 큐) thường được phân loại theo số producer/bên tiêu thụ (consumer / 소비자):

```text
SPSC: single producer, single consumer
MPSC: multiple producer, single consumer
SPMC: single producer, multiple consumer
MPMC: multiple producer, multiple consumer
```

SPSC ring buffer có thể rất đơn giản vì producer và bên tiêu thụ (consumer / 소비자) sở hữu các chỉ số khác nhau. MPMC cần coordination mạnh hơn và thường có nhiều trạng thái cạnh tranh.

Không nên dùng độ phức tạp (complexity / 복잡도) của hàng đợi (queue / 큐) single-thread để suy ra chi phí concurrent hàng đợi (queue / 큐).

> **Chuyển mạch:** Ở chặng này của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Lock-free không có nghĩa wait-free** tiếp nhận điểm tựa từ **SPSC, MPSC, MPMC** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ (memory / 메모리) reclamation trong concurrent hàng đợi (queue / 큐)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lock-free không có nghĩa wait-free

**Lock-free** thường bảo đảm toàn hệ thống có tiến triển: trong hữu hạn bước, một luồng thực thi (thread / 스레드) nào đó hoàn thành thao tác (operation / 연산).

**Wait-free** mạnh hơn: mỗi luồng thực thi (thread / 스레드) riêng lẻ hoàn thành thao tác (operation / 연산) trong số bước bị chặn.

Một lock-free hàng đợi (queue / 큐) vẫn có thể khiến một luồng thực thi (thread / 스레드) cụ thể thử lại (retry / 재시도) nhiều lần dưới contention.

Đây là các guarantee về progress, khác với Big-O tuần tự.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Bộ nhớ (memory / 메모리) reclamation trong concurrent hàng đợi (queue / 큐)** tiếp nhận điểm tựa từ **Lock-free không có nghĩa wait-free** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hàng đợi (queue / 큐) và bộ nhớ (memory / 메모리) retention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ (memory / 메모리) reclamation trong concurrent hàng đợi (queue / 큐)

Một linked hàng đợi (queue / 큐) lock-free không thể đơn giản `free` nút (node / 노드) ngay khi dequeue nếu luồng thực thi (thread / 스레드) khác vẫn có thể đang đọc con trỏ tới nút (node / 노드) đó.

Cần các kỹ thuật như:

```text
hazard pointers
epoch-based reclamation
reference counting trong một số thiết kế
```

Điều này cho thấy thời gian tồn tại (lifetime / 수명) management là một phần của tính đúng đắn (correctness / 정확성) concurrent.

> **Chuyển mạch:** Trong **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Hàng đợi (queue / 큐) và bộ nhớ (memory / 메모리) retention** tiếp nhận điểm tựa từ **Bộ nhớ (memory / 메모리) reclamation trong concurrent hàng đợi (queue / 큐)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khi hàng đợi (queue / 큐) quá dài: độ trễ (latency / 지연 시간) phân phối (distribution / 분포)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hàng đợi (queue / 큐) và bộ nhớ (memory / 메모리) retention

Trong Java/JavaScript, hàng đợi (queue / 큐) tự cài đặt bằng array + head chỉ mục (index / 인덱스) có thể giữ tham chiếu (reference / 참조) tới các item đã dequeue nếu không đặt slot cũ về `null`/`undefined` hoặc compact tùy biểu diễn (representation / 표현).

Về lô-gic (logic / 논리) item đã ra khỏi hàng đợi (queue / 큐), nhưng GC vẫn thấy tham chiếu (reference / 참조) từ backing array.

Do đó logical kích thước (size / 크기) và reachable bộ nhớ (memory / 메모리) không luôn giống nhau.

> **Chuyển mạch:** Ở chặng này của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Khi hàng đợi (queue / 큐) quá dài: độ trễ (latency / 지연 시간) phân phối (distribution / 분포)** tiếp nhận điểm tựa từ **Hàng đợi (queue / 큐) và bộ nhớ (memory / 메모리) retention** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chọn cấu trúc theo selection chính sách (policy / 정책)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khi hàng đợi (queue / 큐) quá dài: độ trễ (latency / 지연 시간) phân phối (distribution / 분포)

Average hàng đợi (queue / 큐) length không nói hết tail độ trễ (latency / 지연 시간). Một burst lớn có thể tạo một số yêu cầu (request / 요청) chờ rất lâu dù mean vẫn chấp nhận được.

Trong hệ thống thực tế nên quan sát:

```text
queue depth histogram
p50/p95/p99 waiting time
drop/reject rate
consumer utilization
arrival burstiness
```

Hàng đợi (queue / 큐) là một cấu trúc dữ liệu nhưng cũng là một điểm đo sức khỏe hệ thống.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Chọn cấu trúc theo selection chính sách (policy / 정책)** tiếp nhận điểm tựa từ **Khi hàng đợi (queue / 큐) quá dài: độ trễ (latency / 지연 시간) phân phối (distribution / 분포)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kiểm thử hàng đợi (queue / 큐) và deque** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chọn cấu trúc theo selection chính sách (policy / 정책)

Có thể nhìn nhiều thuật toán dưới một khung:

```text
Stack          -> chọn phần tử mới nhất
Queue          -> chọn phần tử cũ nhất
Deque          -> chọn ở một trong hai đầu
Priority Queue -> chọn phần tử tốt nhất theo comparator
Randomized     -> chọn ngẫu nhiên
Bucket Queue   -> chọn theo lớp priority rời rạc
```

Khi đổi chính sách (policy / 정책) của frontier, ta thường đổi cả ngữ nghĩa (semantics / 의미론) của thuật toán.

> **Chuyển mạch:** Trong **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Kiểm thử hàng đợi (queue / 큐) và deque** tiếp nhận điểm tựa từ **Chọn cấu trúc theo selection chính sách (policy / 정책)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kiểm thử Priority hàng đợi (queue / 큐)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiểm thử hàng đợi (queue / 큐) và deque

Thuộc tính (property / 속성) cơ bản:

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

Random differential kiểm thử (test / 테스트) rất hiệu quả cho ring-buffer bugs.

> **Chuyển mạch:** Ở chặng này của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Kiểm thử Priority hàng đợi (queue / 큐)** tiếp nhận điểm tựa từ **Kiểm thử hàng đợi (queue / 큐) và deque** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiểm thử Priority hàng đợi (queue / 큐)

Có thể push random values rồi pop hết và kiểm tra đầu ra (output / 출력) đã sorted theo comparator.

Với indexed vùng nhớ động (heap / 힙), phải kiểm tra:

```text
heap invariant
position[heap[i]] == i
size và active set nhất quán
```

Với lazy deletion, cần kiểm thử (test / 테스트) nhiều stale entries và bảo đảm stale trạng thái (state / 상태) không được dùng để relax tiếp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Những hiểu lầm phổ biến** tiếp nhận điểm tựa từ **Kiểm thử Priority hàng đợi (queue / 큐)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

“hàng đợi (queue / 큐) chỉ là mảng có push/shift” — `shift` lặp lại có thể rất đắt.

“hàng đợi (queue / 큐) càng lớn càng chống overload tốt” — hàng đợi (queue / 큐) lớn có thể chỉ biến overload thành độ trễ (latency / 지연 시간) lớn.

“Priority hàng đợi (queue / 큐) nghĩa là nhị phân (binary / 이진) vùng nhớ động (heap / 힙)” — vùng nhớ động (heap / 힙) chỉ là một hiện thực (implementation / 구현).

“Thay priority trường dữ liệu (field / 필드) trong đối tượng (object / 객체) là vùng nhớ động (heap / 힙) tự cập nhật” — sai.

“Inner while trong monotonic deque làm O(n²)” — sai vì mỗi chỉ mục (index / 인덱스) bị loại tối đa một lần.

“Concurrent hàng đợi (queue / 큐) chỉ cần thêm khóa (lock / 잠금) vào enqueue/dequeue” — chưa đủ để nói về thông lượng (throughput / 처리량), fairness, blocking ngữ nghĩa (semantics / 의미론) và iteration đặc tả hợp đồng (contract / 계약).

> **Chuyển mạch:** Trong **Hàng đợi (queue / 큐), Deque và hàng đợi ưu tiên**, **Mô hình tư duy** gom các mảnh từ **Những hiểu lầm phổ biến** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> hàng đợi (queue / 큐), Deque và Priority hàng đợi (queue / 큐) khác nhau chủ yếu ở **quy tắc chọn ai được phục vụ tiếp theo**. Chính quy tắc đó tạo ra thứ tự xử lý, proof of tính đúng đắn (correctness / 정확성) và đặc tính hệ thống.

Khi gặp một frontier hoặc danh sách chờ, hãy hỏi: **cần FIFO, LIFO, hai đầu, minimum priority hay một priority lĩnh vực (domain / 도메인) chuyên biệt; hàng đợi (queue / 큐) có bounded không; overload xử lý thế nào; fairness có quan trọng không; và selection chính sách (policy / 정책) nào chính xác là điều proof của thuật toán cần?**

Xem tiếp: [Stacks](./02_stacks.md), [Heaps](../02_trees/03_heaps.md), [BFS/DFS](../03_graphs/01_graph_traversal_bfs_dfs.md), [Shortest Paths](../03_graphs/02_shortest_paths.md), [Amortized Analysis](../05_specialized/03_amortized_randomized_and_probabilistic_thinking.md) và [Java Collections](../80_language_implementations/01_java_collections_and_dsa.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
