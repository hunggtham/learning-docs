# Shortest Paths
**Đường đi ngắn nhất (Shortest Path / 최단 경로)**

Shortest path là một family, không phải một thuật toán duy nhất. Chọn algorithm dựa trên edge weights.

## Unweighted / equal weight

Nếu mọi edge cost như nhau, BFS đủ để tìm số edges ít nhất.

## Dijkstra với non-negative weights

Dijkstra duy trì tentative distance `dist[v]`. Relaxation:

\[
\text{if } dist[v] > dist[u]+w(u,v),\quad
 dist[v]\leftarrow dist[u]+w(u,v)
\]

Priority queue luôn lấy unsettled node có distance nhỏ nhất.

```java
record Edge(int to, int w) {}
record State(int node, long dist) {}

PriorityQueue<State> pq =
    new PriorityQueue<>(Comparator.comparingLong(State::dist));
```

Non-negative weight là điều kiện cốt lõi. Khi lấy node gần nhất ra khỏi queue, không thể có đường đi qua một node xa hơn rồi dùng negative edge để quay lại làm nó rẻ hơn.

Với binary heap và adjacency list, complexity thường `O((V+E) log V)`.

## Bellman-Ford

Nếu có negative edges, Bellman-Ford relax mọi edges tối đa `V-1` rounds. Một shortest simple path không có cycle có tối đa `V-1` edges. Nếu round tiếp theo vẫn cải thiện distance, tồn tại negative cycle reachable.

Complexity `O(VE)` — chậm hơn nhưng model rộng hơn.

## Floyd-Warshall

All-pairs shortest paths dùng DP:

\[
d_k(i,j)=\min(d_{k-1}(i,j), d_{k-1}(i,k)+d_{k-1}(k,j))
\]

Time `O(V³)`, phù hợp graph nhỏ/dense khi cần mọi cặp.

## Mental Model

> Shortest-path algorithms đều xoay quanh relaxation: mỗi edge đưa ra một candidate tốt hơn cho distance. Khác biệt nằm ở thứ tự relax và khi nào một distance có thể được xem là final.

## 0–1 BFS

Nếu edge weights chỉ là `0` hoặc `1`, Dijkstra dùng heap là đúng nhưng chưa khai thác hết structure. Ta có thể dùng deque:

```text
weight 0 -> push front
weight 1 -> push back
```

Distance order vẫn được giữ, và complexity trở thành:

\[
O(V+E)
\]

Đây là ví dụ quan trọng: constraint hẹp hơn có thể cho data structure đơn giản hơn và algorithm nhanh hơn.

## DAG shortest path

Nếu graph là DAG, topological order cho phép relax each edge đúng một lần theo dependency order, kể cả edge có negative weight miễn không có cycle.

Complexity:

\[
O(V+E)
\]

Không cần Dijkstra hay Bellman-Ford.

## Path reconstruction

Distance thôi thường chưa đủ. Khi relax:

```text
if dist[u] + w < dist[v]:
    dist[v] = dist[u] + w
    parent[v] = u
```

Sau đó backtrack parent từ target. Parent array là một ví dụ “metadata nhỏ biến optimization value thành actual solution”.

## Integer overflow

Trong Java, nếu `dist[u]` dùng `Long.MAX_VALUE` làm infinity rồi tính:

```java
dist[u] + weight
```

có thể overflow. Chỉ relax từ reachable node hoặc dùng guard. C cũng cần chú ý signed overflow; JavaScript Number có precision limit cho integer lớn hơn `2^53-1`, có thể cần `BigInt` nếu domain thật sự lớn.

## Negative cycle semantics

Negative cycle không có nghĩa “algorithm bị lỗi”. Nó có nghĩa objective shortest path không có finite minimum cho những destinations reachable sau cycle: ta có thể đi vòng cycle thêm lần nữa để cost giảm vô hạn.

Hiểu semantics này quan trọng hơn nhớ Bellman-Ford detect cycle ở iteration thứ V.
