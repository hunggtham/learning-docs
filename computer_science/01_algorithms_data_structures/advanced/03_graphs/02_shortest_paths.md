# Shortest Paths
**Đường đi ngắn nhất (Shortest Path / 최단 경로)**

“Shortest path” không phải tên của một thuật toán duy nhất. Nó là một họ bài toán, và lựa chọn algorithm phụ thuộc trực tiếp vào **mô hình trọng số (weight model / 가중치 모델)** của graph.

Cùng một graph topology nhưng nếu edges đều bằng nhau, chỉ có `0/1`, đều không âm, có số âm, hay graph là DAG thì structure toán học khác nhau. Vì vậy trước khi nghĩ tới Dijkstra, câu hỏi đầu tiên phải là:

```text
Edge cost có dạng gì?
Graph directed hay undirected?
Có negative edge không?
Có negative cycle không?
Cần shortest path từ một source hay mọi cặp?
Graph sparse hay dense?
Có cần actual path hay chỉ distance?
```

## Mental Model

> Mọi shortest-path algorithm đều cố cải thiện một **ước lượng distance** bằng relaxation. Khác nhau ở thứ tự relaxation và điều kiện nào cho phép xem một distance là đã “final”.

Với edge `u -> v` có weight `w`, relaxation kiểm tra:

\[
dist[v] > dist[u] + w
\]

Nếu đúng:

\[
dist[v] \leftarrow dist[u] + w
\]

Đây là primitive xuyên suốt BFS, Dijkstra, Bellman-Ford và DAG shortest path.

## Unweighted graph: BFS là shortest-path algorithm

Nếu mọi edge có cùng cost, ví dụ mỗi bước tính 1, **Breadth-First Search (BFS / 너비 우선 탐색)** đã đủ.

BFS xử lý graph theo layer:

```text
distance 0: source
distance 1: neighbors
distance 2: neighbors của layer trước chưa thăm
...
```

Khi một vertex lần đầu được discover, ta đã tìm được path ít edge nhất tới nó, bởi vì queue đảm bảo mọi path ngắn hơn đã được xử lý trước.

Complexity với adjacency list:

\[
O(V+E)
\]

Đây là một insight quan trọng: Dijkstra trên unweighted graph vẫn đúng nếu coi mọi edge weight = 1, nhưng heap là overhead không cần thiết.

## 0–1 BFS: khi weights chỉ là 0 hoặc 1

Nếu weight chỉ thuộc `{0,1}`, ta có thể dùng deque thay vì binary heap.

Relax edge weight 0:

```text
push_front(v)
```

Relax edge weight 1:

```text
push_back(v)
```

Intuition là node có distance không tăng phải được xử lý trước các node làm distance tăng 1. Deque duy trì đúng ordering cần thiết mà không cần general-purpose priority queue.

Complexity:

\[
O(V+E)
\]

Ví dụ thực tế: chuyển trạng thái miễn phí hoặc trả phí 1 đơn vị; đi qua portal cost 0 nhưng bước thường cost 1; minimize số lần đổi mode.

## Dijkstra: non-negative weights

**Dijkstra (다익스트라 알고리즘)** áp dụng khi mọi reachable edge weight không âm.

Ta giữ `dist[v]` là best distance hiện biết. Priority queue chọn unsettled vertex có `dist` nhỏ nhất.

### Invariant cốt lõi

Khi `u` là node có tentative distance nhỏ nhất và mọi edge weight không âm, không thể có một path đi qua một unsettled node xa hơn rồi quay lại làm `u` rẻ hơn.

Giả sử có path tốt hơn tới `u` đi qua một unsettled vertex `x`. Vì edge weights không âm, prefix tới `x` không thể lớn hơn toàn path tới `u`. Nhưng `u` đang là tentative nhỏ nhất trong frontier. Điều này dẫn tới contradiction với giả định có path tốt hơn chưa được phát hiện.

Do đó khi pop một state non-stale tốt nhất, distance đó có thể được xem là finalized.

### Java với stale-entry pattern

```java
record Edge(int to, long w) {}
record State(int node, long dist) {}

static long[] dijkstra(List<List<Edge>> g, int s) {
    int n = g.size();
    long INF = Long.MAX_VALUE / 4;
    long[] dist = new long[n];
    Arrays.fill(dist, INF);
    dist[s] = 0;

    PriorityQueue<State> pq =
        new PriorityQueue<>(Comparator.comparingLong(State::dist));
    pq.offer(new State(s, 0));

    while (!pq.isEmpty()) {
        State cur = pq.poll();
        int u = cur.node();

        if (cur.dist() != dist[u]) continue; // stale

        for (Edge e : g.get(u)) {
            long nd = dist[u] + e.w();
            if (nd < dist[e.to()]) {
                dist[e.to()] = nd;
                pq.offer(new State(e.to(), nd));
            }
        }
    }
    return dist;
}
```

Với adjacency list + binary heap, complexity thường viết:

\[
O((V+E)\log V)
\]

hoặc gần `O(E log V)` cho connected sparse graph.

## Tại sao negative edge phá Dijkstra?

Giả sử:

```text
s -> a : 2
s -> b : 5
b -> a : -10
```

Dijkstra có thể finalize `a = 2` trước vì `2 < 5`. Nhưng path `s -> b -> a` có cost `-5`, tốt hơn rất nhiều.

Vấn đề không phải implementation. Assumption “một node tốt nhất hiện tại sẽ không bị cải thiện trong tương lai” đã sai vì negative edge có thể giảm cost sau khi đi qua một node đang xa hơn.

Đây là lý do condition “non-negative weight” là phần của correctness proof, không chỉ là recommendation performance.

## Bellman-Ford: relaxation theo số edges

**Bellman-Ford (벨만-포드)** cho phép negative edges.

Một shortest simple path không có repeated vertex có tối đa `V-1` edges. Vì vậy nếu ta relax mọi edge `V-1` rounds, mọi shortest path finite sẽ có đủ cơ hội propagate từ source.

Pseudo-flow:

```text
dist[source] = 0
repeat V-1 lần:
    changed = false
    for every edge u -> v with weight w:
        if dist[u] + w < dist[v]:
            update
            changed = true
    if !changed: break
```

Complexity:

\[
O(VE)
\]

Chậm hơn Dijkstra nhưng support model rộng hơn.

## Negative cycle semantics

Nếu round thứ `V` vẫn có relaxation trên vertex reachable từ source, có một **negative cycle (음수 사이클)** ảnh hưởng tới region đó.

Điều này không đơn giản nghĩa là “không có shortest path ở toàn graph”. Nếu cycle không reachable từ source, nó không ảnh hưởng single-source query. Nếu cycle reachable nhưng target không reachable từ cycle, target vẫn có thể có finite shortest path.

Nếu target reachable sau một negative cycle, objective không có finite minimum: đi thêm vòng cycle làm cost giảm vô hạn.

Mental model đúng là:

```text
negative cycle reachable + can reach target
=> shortest distance tới target không bị chặn dưới
```

## SPFA: vì sao cần thận trọng

Shortest Path Faster Algorithm dùng queue để chỉ relax vertices có thay đổi, thường nhanh trên một số data. Nhưng worst-case vẫn có thể rất tệ, gần `O(VE)` và còn có adversarial inputs.

Vì vậy không nên coi SPFA là “Bellman-Ford nhanh hơn” với guarantee tốt hơn. Dùng khi hiểu workload hoặc trong context mà empirical behavior được chấp nhận.

## DAG shortest path

Nếu graph là **Directed Acyclic Graph (DAG / 방향 비순환 그래프)**, ta có topological order. Mỗi edge luôn đi từ node trước sang node sau trong order.

Do đó chỉ cần relax mỗi edge một lần theo topological order:

\[
O(V+E)
\]

Điểm đặc biệt: DAG shortest path chấp nhận negative edge vì không có cycle để quay lại phá ordering.

Đây là ví dụ điển hình cho việc topology mạnh hơn weight assumption. Khi graph acyclic, dependency order loại nhu cầu repeated relaxation.

## All-pairs shortest paths và Floyd-Warshall

Nếu cần shortest path giữa mọi cặp vertices và graph đủ nhỏ/dense, **Floyd-Warshall (플로이드-워셜)** là một dynamic programming rất trực tiếp.

Định nghĩa:

\[
d_k(i,j)
\]

là shortest distance từ `i` tới `j` khi chỉ được dùng các intermediate vertices trong `{0,...,k}`.

Transition:

\[
d_k(i,j)=\min(d_{k-1}(i,j), d_{k-1}(i,k)+d_{k-1}(k,j))
\]

In-place form:

```java
for (int k = 0; k < n; k++)
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            d[i][j] = Math.min(d[i][j], d[i][k] + d[k][j]);
```

Time:

\[
O(V^3)
\]

Memory:

\[
O(V^2)
\]

Nó rất phù hợp khi `V` nhỏ và cần nhiều pair queries, đặc biệt dense graph.

## Floyd-Warshall và negative cycles

Sau algorithm, nếu:

\[
d[i][i] < 0
\]

thì có negative cycle reachable từ `i` và quay về `i`.

Muốn biết pair `(s,t)` có shortest path không hữu hạn, phải kiểm có vertex `k` sao cho:

```text
s reaches k
k lies on/reaches negative cycle
negative cycle region reaches t
```

Chỉ nhìn một diagonal âm mà tuyên bố mọi cặp invalid là sai.

## Johnson's algorithm: all-pairs trên sparse graph

Khi graph sparse, `O(V^3)` có thể lãng phí. **Johnson's algorithm** dùng Bellman-Ford để tìm potentials, reweight edges thành non-negative mà bảo toàn shortest-path ordering, rồi chạy Dijkstra từ từng source.

Ý tưởng reweight:

\[
w'(u,v)=w(u,v)+h(u)-h(v)
\]

Nếu `h` được chọn từ Bellman-Ford potentials, `w' >= 0`.

Path cost bị shift theo endpoints nhưng relative choice giữa paths cùng source/target không đổi. Đây là một example đẹp của việc biến problem sang domain mà algorithm mạnh hơn áp dụng được.

## Path reconstruction

Distance value thường chưa đủ. Muốn actual route, khi relaxation thành công:

```text
parent[v] = u
```

Sau algorithm, backtrack từ target tới source.

```java
List<Integer> path = new ArrayList<>();
for (int v = target; v != -1; v = parent[v]) {
    path.add(v);
}
Collections.reverse(path);
```

Cần phân biệt `parent` cho shortest-path tree với graph parent generic. Nếu có nhiều shortest paths cùng cost, tie-breaking quyết định path nào được lưu.

## Counting shortest paths

Nếu cần số shortest paths, có thể maintain `ways[v]` cùng `dist[v]`:

```text
new distance better:
    dist[v] = nd
    ways[v] = ways[u]

new distance equal:
    ways[v] += ways[u]
```

Nhưng correctness còn phụ thuộc processing order và zero-weight cycles. Nếu có zero-cost cycles, số walk shortest có thể không finite. Domain phải nói đang đếm simple paths, walks hay paths trong DAG/positive-weight setting.

## Multi-source shortest path

Nếu có nhiều sources và cần distance tới source gần nhất, không nhất thiết chạy algorithm nhiều lần.

Với unweighted graph, enqueue tất cả sources với distance 0 rồi BFS một lần.

Với non-negative weighted graph, push tất cả sources vào Dijkstra PQ với distance 0.

Mental model: tạo một virtual super-source nối tới mọi source bằng edge weight 0.

## Multi-target và early exit

Trong Dijkstra, nếu chỉ cần một target, có thể dừng khi target được pop với non-stale minimum distance, vì lúc đó nó đã finalized.

Không nên dừng ngay khi target lần đầu được discovered/relaxed; tentative distance có thể còn được cải thiện trước khi target trở thành min frontier.

## A*: shortest path với heuristic

**A\*** ưu tiên:

\[
f(v)=g(v)+h(v)
\]

trong đó `g(v)` là cost từ source, `h(v)` ước lượng cost còn lại tới target.

Nếu heuristic **admissible** (`h(v)` không overestimate true remaining cost), A* có thể giữ optimality. Nếu heuristic còn consistent, processing behavior gần Dijkstra với reweighted priorities và ít reopen hơn.

Dijkstra chính là A* với `h(v)=0`.

Trong routing/spatial search, heuristic tốt giúp bỏ rất nhiều vùng graph không liên quan.

## Bidirectional search

Nếu source và target rõ ràng, có thể search từ hai phía và gặp nhau ở giữa. Với unweighted graph, bidirectional BFS có thể giảm effective search frontier mạnh từ khoảng `b^d` xuống gần `2b^{d/2}` trong ideal branching model.

Weighted bidirectional Dijkstra phức tạp hơn vì stopping condition phải đảm bảo lower bound hai frontier đã đủ lớn; không thể chỉ dừng ở lần đầu hai searches chạm nhau một cách ngây thơ.

## Overflow và infinity representation

Trong Java, nếu dùng:

```java
long INF = Long.MAX_VALUE;
```

rồi tính:

```java
INF + w
```

có thể overflow thành số âm. Thực tế thường dùng `Long.MAX_VALUE / 4` hoặc guard:

```text
if dist[u] != INF before addition
```

Trong C, signed integer overflow có thể là undefined behavior. Cần chọn type đủ rộng và kiểm boundary.

JavaScript `Number` biểu diễn integer chính xác tới:

\[
2^{53}-1
\]

Nếu path sum có thể vượt vùng này, cân nhắc `BigInt` hoặc thay đổi model dữ liệu.

## Floating-point weights

Nếu weights là `double`, equality test và stale check cần cẩn thận. Với floating-point, expression `curDist != dist[u]` có thể vẫn hoạt động nếu values được copy nguyên từ computed distance, nhưng các comparisons gần boundary có thể chịu rounding.

Nếu domain là tiền tệ hoặc fixed-scale cost, integer minor units thường an toàn hơn floating point.

## Sparse vs dense graph

Adjacency list phù hợp sparse graph và Dijkstra/BFS thường chỉ iterate outgoing edges thực sự tồn tại.

Adjacency matrix cho edge lookup `O(1)` nhưng iteration neighbors `O(V)`. Trên dense graph, matrix-based algorithms có thể cạnh tranh vì locality tốt và `E ≈ V^2` anyway.

Big-O phải gắn với representation.

## Shortest path tree không phải Minimum Spanning Tree

Dijkstra từ source tạo một shortest-path tree: path từ source tới mỗi vertex là shortest.

MST tối thiểu **tổng weight của toàn bộ tree**. Nó không đảm bảo path từ root tới từng vertex là shortest.

Hai objectives khác nhau:

```text
Shortest-path tree -> tối ưu route từ source
MST                -> tối ưu total infrastructure cost
```

Đừng chọn algorithm chỉ vì cả hai “trông như chọn edge nhỏ”.

## Decision table

| Weight / structure | Algorithm tự nhiên |
|---|---|
| unweighted / equal weight | BFS |
| weights 0 hoặc 1 | 0–1 BFS |
| non-negative weights | Dijkstra |
| negative edges, không biết cycle | Bellman-Ford |
| DAG | topological relaxation |
| all-pairs, graph nhỏ/dense | Floyd-Warshall |
| all-pairs, sparse, có negative edges nhưng không negative cycle | Johnson |
| spatial single-target + heuristic tốt | A* |

Bảng này không thay proof. Nó chỉ nhắc điều kiện model.

## Common misconceptions

**“Dijkstra nhanh hơn Bellman-Ford nên cứ dùng Dijkstra.”** Sai nếu có negative edge. Correctness condition quan trọng hơn speed.

**“BFS chỉ là traversal, không phải shortest path.”** Với equal edge costs, BFS chính là shortest-path algorithm tối ưu.

**“Negative cycle nghĩa là mọi shortest path trong graph đều không tồn tại.”** Không. Chỉ các source-target regions bị ảnh hưởng mới không có finite minimum.

**“Floyd-Warshall chỉ dùng cho positive weights.”** Nó hỗ trợ negative edges, miễn hiểu semantics negative cycle.

**“Dijkstra dừng khi target được nhìn thấy lần đầu.”** Không. Dừng khi target được extract/finalize đúng điều kiện.

**“PriorityQueue duplicate entry làm Dijkstra sai.”** Không nếu dùng stale-entry check. Nó là implementation trade-off phổ biến.

## Testing shortest-path implementation

Test nên bao gồm:

```text
single vertex
unreachable vertices
parallel edges
zero-weight edges
duplicate equal shortest paths
very large path sum
disconnected graph
negative edge without negative cycle
reachable negative cycle
negative cycle outside source component
DAG with negative weights
```

Một property mạnh sau khi có final distances là với mọi reachable edge `(u,v,w)`:

\[
dist[v] \le dist[u] + w
\]

Nếu parent path được lưu, tổng weight trên parent chain phải bằng reported `dist[target]`.

Trên graph nhỏ, có thể differential-test Dijkstra non-negative với Floyd-Warshall reference.

## Connection với production systems

Routing, map navigation, dependency cost, network latency planning, game AI pathfinding, logistics, workflow optimization và build dependency đều có shortest-path variants.

Nhưng production thường thêm constraints: time-dependent weights, turn penalties, multiple resources, capacity, stochastic costs hoặc dynamic graph. Khi đó classical shortest path có thể trở thành state-space shortest path: mỗi “vertex” thực sự là `(location, time, fuel, mode, ...)`.

Đây là connection quan trọng với problem modeling: algorithm có thể đúng nhưng state representation thiếu thông tin thì kết quả vẫn sai.

## Mental Model mở rộng

> Shortest path không bắt đầu từ tên algorithm; nó bắt đầu từ việc xác định **cost algebra và ordering nào cho phép một candidate trở thành final**.

BFS dùng layer order. 0–1 BFS dùng deque để giữ hai mức cost cục bộ. Dijkstra dựa vào non-negative weights. Bellman-Ford dựa vào giới hạn số edges của simple path. DAG dùng dependency order. Floyd-Warshall dùng allowed-intermediate-state DP.

Nếu nhớ được điều kiện làm mỗi method đúng, bạn có thể chọn algorithm từ bản chất bài toán thay vì từ pattern memorization.