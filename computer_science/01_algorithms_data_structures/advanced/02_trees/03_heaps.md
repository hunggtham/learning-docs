# Heap
**Đống (Heap / 힙)**

Heap được thiết kế cho câu hỏi: trong tập dữ liệu thay đổi liên tục, phần tử nhỏ nhất/lớn nhất hiện tại là gì?

Min-heap giữ invariant `parent <= children`; max-heap giữ chiều ngược lại. Heap không đảm bảo toàn array sorted.

## Binary heap trong array

Complete binary tree có thể lưu trong array. Với zero-based index:

\[
left(i)=2i+1,\quad right(i)=2i+2
\]

\[
parent(i)=\left\lfloor\frac{i-1}{2}\right\rfloor
\]

Không cần pointer nodes.

## Insert và sift-up

Append phần tử cuối để giữ complete-tree shape, sau đó swap lên khi phá heap invariant. Height `O(log n)`, nên insert `O(log n)`.

## Extract-min và sift-down

Root là minimum. Thay root bằng last element, giảm size rồi đẩy xuống child phù hợp. `O(log n)`. Peek root là `O(1)`.

## Build heap O(n)

Bottom-up heapify là `O(n)`, không phải `O(n log n)`, vì phần lớn nodes ở gần leaves và cần rất ít sift work. Đây là ví dụ cho thấy không nên nhân worst cost của một node với mọi nodes nếu work phân bố không đều.

## Java

```java
PriorityQueue<Integer> pq = new PriorityQueue<>();
pq.offer(5);
pq.offer(2);
pq.offer(8);
System.out.println(pq.poll()); // 2
```

## Top-K

Nếu stream có hàng triệu values nhưng chỉ cần 100 lớn nhất, giữ min-heap size `k=100`. Mỗi new value lớn hơn root thì replace. Time `O(n log k)`, memory `O(k)`, tốt hơn sort toàn bộ khi `k << n`.

## Mental Model

> Heap là partial order có chủ đích: không trả chi phí để biết order của mọi cặp, chỉ duy trì đủ để extreme element luôn ở root.

## Heap không hỗ trợ arbitrary search tốt

Trong min-heap, ta chỉ biết parent <= children. Nếu target lớn hơn root, cả hai subtrees đều vẫn có thể chứa target. Vì vậy search một arbitrary value có thể `O(n)`.

Đây là distinction quan trọng giữa heap và BST: cả hai là trees có order invariant, nhưng invariant phục vụ **query khác nhau**.

## Decrease-key và stale-entry pattern

Classical Dijkstra có `decrease-key`: khi distance của node giảm, update priority của entry đang có trong heap. Nhiều standard priority queue APIs không hỗ trợ efficient decrease-key trực tiếp.

Một pattern thực tế là push một entry mới và khi pop thì bỏ entry stale:

```java
if (cur.dist() != dist[cur.node()]) continue;
```

Correctness giữ vì priority queue cuối cùng vẫn pop best non-stale candidate; trade-off là heap có thể chứa duplicates.

## Indexed heap

Nếu workload cần update priority theo item identity thường xuyên, có thể duy trì `position[item]` để biết item đang ở index nào trong heap. Swap phải update cả heap array và position map. Khi đó decrease-key có thể `O(log n)` mà không tạo duplicates.

## K-way merge

Nếu có `k` sorted streams, thay vì concatenate rồi sort lại, ta đưa head của mỗi stream vào min-heap. Mỗi lần lấy nhỏ nhất, ta advance đúng stream đó và push phần tử tiếp.

Nếu tổng có `N` phần tử:

\[
O(N\log k)
\]

Đây là cơ sở của external merge và nhiều pipeline xử lý sorted data.
