# BFS và DFS
**Graph Traversal / 그래프 순회**

Traversal trả lời câu hỏi nền tảng nhất của graph: bắt đầu từ một state, ta có thể reach những state nào và theo thứ tự nào? Hai chiến lược kinh điển là **Breadth-First Search (BFS / 너비 우선 탐색)** và **Depth-First Search (DFS / 깊이 우선 탐색)**.

Cả hai thường có complexity `O(V+E)` trên adjacency list. Khác biệt lớn không nằm ở Big-O mà nằm ở **frontier policy**:

```text
BFS: frontier theo FIFO queue -> mở rộng theo layer/distance
DFS: frontier theo stack      -> đi sâu theo branch rồi quay lại
```

Chính search order này quyết định loại theorem/invariant nào ta có thể khai thác.

## BFS như shortest-path theo số edge

Nếu mọi edge có cùng cost, BFS từ source `s` khám phá vertices theo nondecreasing distance tính bằng số edges.

Java:

```java
int[] dist = new int[n];
int[] parent = new int[n];
Arrays.fill(dist, -1);
Arrays.fill(parent, -1);

ArrayDeque<Integer> q = new ArrayDeque<>();
dist[s] = 0;
q.offer(s);

while (!q.isEmpty()) {
    int u = q.poll();

    for (int v : g.get(u)) {
        if (dist[v] != -1) continue;

        dist[v] = dist[u] + 1;
        parent[v] = u;
        q.offer(v);
    }
}
```

Tại sao lần đầu tới `v` là shortest path? Queue bảo đảm mọi node distance `d` được process trước nodes distance `d+1`. Nếu có một path ngắn hơn tới `v`, predecessor của path đó phải nằm ở layer trước và đã discover `v` sớm hơn. Mâu thuẫn.

Đây là proof dựa trên **layer invariant** chứ không phải vì queue “thường dùng như vậy”.

## BFS layer structure

BFS tạo các lớp:

```text
L0 = {source}
L1 = nodes cách source 1 edge
L2 = nodes cách source 2 edges
...
```

Mọi edge trong undirected unweighted graph chỉ nối vertices có BFS level chênh lệch tối đa 1.

Layer view hữu ích cho bipartite checking, shortest path reconstruction, level aggregation và reasoning về wave propagation.

## Parent tree và path reconstruction

Khi lần đầu discover `v` từ `u`, lưu:

```text
parent[v] = u
```

ta tạo BFS tree.

Reconstruct path:

```java
List<Integer> path = new ArrayList<>();
for (int v = target; v != -1; v = parent[v]) {
    path.add(v);
}
Collections.reverse(path);
```

Nếu target unreachable, cần check `dist[target] == -1` trước.

Parent metadata biến answer từ “distance là 7” thành actual route.

## Multi-source BFS

Nếu có nhiều sources cùng distance 0, enqueue tất cả ngay từ đầu:

```text
for each source s:
    dist[s] = 0
    enqueue(s)
```

BFS sau đó trả distance tới **source gần nhất**.

Applications:

```text
nearest hospital/exit
fire/infection spread từ nhiều origins
distance tới nearest zero trong matrix
Voronoi-like partition trên unweighted graph
```

Không cần thuật toán mới; chỉ thay initial frontier.

## Multi-target / early exit

Nếu chỉ cần path tới một target, BFS có thể dừng khi target được dequeued hoặc ngay khi discovered tùy metadata cần thiết.

Nhưng nếu cần all distances hoặc properties toàn component, early exit sẽ bỏ incomplete information.

Optimization phải khớp required output.

## Bidirectional BFS

Nếu graph unweighted, branching factor lớn và biết cả source lẫn target, có thể BFS từ hai phía cho tới khi frontiers gặp nhau.

Nếu branching factor khoảng `b` và shortest distance `d`, một phía có thể explore cỡ `b^d`, còn bidirectional search gần `2*b^(d/2)` trong idealized tree-like space.

Implementation cần:

```text
dist/visited từ source
dist/visited từ target
expand frontier nhỏ hơn khi có thể
phát hiện node/edge nơi hai search regions giao nhau
```

Không phải graph nào cũng được speedup giống nhau, nhưng mental model là giảm search depth mỗi phía.

## BFS trên grid

Grid 4-direction chỉ là implicit graph:

```text
vertex = cell
edge = move hợp lệ sang neighbor
```

Không cần build adjacency list. Generate neighbors on demand:

```java
int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
```

Visited state có thể encode bằng array 2D. Nếu state còn keys, direction, remaining breaks hoặc mode, visited dimension phải mở rộng tương ứng.

## BFS và 0–1 BFS

BFS đúng cho equal-weight edges. Nếu weights chỉ `0` hoặc `1`, standard BFS không đủ nhưng heap Dijkstra hơi thừa.

**0–1 BFS** dùng deque:

```text
weight 0 -> push front
weight 1 -> push back
```

để duy trì distance order, đạt `O(V+E)`.

Đây là example cho việc frontier data structure encode cost model.

## DFS như một structural exploration

DFS đi sâu theo branch trước khi backtrack.

Recursive JavaScript:

```js
function dfs(u, g, seen) {
  seen[u] = true;
  for (const v of g[u]) {
    if (!seen[v]) dfs(v, g, seen);
  }
}
```

DFS đặc biệt mạnh khi answer phụ thuộc **nested structure**:

```text
connected components
cycle detection
topological ordering
SCC
bridges / articulation points
subtree-like reasoning trong DFS forest
backtracking/state search
```

## DFS tree và forest

Trên connected graph, DFS từ source tạo một DFS tree. Trên disconnected graph, loop qua all vertices tạo **DFS forest**.

```java
for (int u = 0; u < n; u++) {
    if (!seen[u]) {
        dfs(u, -1);
        components++;
    }
}
```

Mỗi root tương ứng một connected component trong undirected graph.

## Directed cycle detection bằng color states

Boolean `seen` không đủ để phân biệt edge tới ancestor đang active và edge tới node đã hoàn thành.

Dùng ba states:

```text
0 = unvisited
1 = visiting / active in recursion stack
2 = finished
```

Nếu từ `u` có edge tới `v` với state `1`, đó là back edge vào active ancestor → directed cycle.

```java
boolean dfsCycle(int u) {
    state[u] = 1;

    for (int v : g.get(u)) {
        if (state[v] == 1) return true;
        if (state[v] == 0 && dfsCycle(v)) return true;
    }

    state[u] = 2;
    return false;
}
```

State `finished` quan trọng vì edge tới một node đã hoàn thành không chứng minh cycle qua current recursion chain.

## Undirected cycle detection

Trong undirected graph, edge trở lại parent là representation của chính edge ta vừa đi xuống, không phải cycle.

Basic DFS:

```text
if neighbor not visited:
    dfs(neighbor, u)
else if neighbor != parent:
    cycle exists
```

Nhưng multigraph cần edge id thay vì chỉ `neighbor != parent`, vì parallel edges giữa cùng endpoints có semantics khác.

## Discovery và finish time

DFS có hai thời điểm tự nhiên:

```text
tin[u]  = lúc enter u
tout[u] = lúc finish toàn subtree DFS của u
```

Ancestor relation trong DFS tree có thể kiểm tra qua interval nesting:

```text
u ancestor của v nếu
tin[u] <= tin[v] && tout[v] <= tout[u]
```

Timestamps/low-link values là nền tảng cho bridges, articulation points, SCC và topological reasoning.

## Edge classification trong directed DFS

Edges có thể được nhìn như:

```text
tree edge    -> discover node mới
back edge    -> tới active ancestor
forward edge -> tới descendant đã discover
cross edge   -> giữa branches/subtrees khác
```

Không phải mọi algorithm cần classification đầy đủ, nhưng distinction giúp hiểu tại sao directed cycle detection dùng back edge.

## Topological order từ finish time

Trong DAG, nếu DFS finish `u`, mọi reachable descendants đã finish trước. Push `u` vào list khi exit rồi reverse list sẽ tạo topological order.

Nếu có back edge/cycle, topological order không tồn tại.

Do đó “reverse postorder” không phải trick; nó xuất phát từ dependency finish invariant.

## Iterative DFS và continuation state

Naive iterative DFS:

```java
stack.push(source);
while (!stack.isEmpty()) {
    int u = stack.pop();
    ...
}
```

mô phỏng preorder khá dễ. Nhưng nếu cần postorder/finish event, mỗi stack frame phải nhớ progress trong adjacency list hoặc dùng enter/exit markers.

Ví dụ two-phase:

```text
push (u, ENTER)

on ENTER:
    mark seen
    push (u, EXIT)
    push unvisited children as ENTER in reverse order

on EXIT:
    process postorder logic
```

Điều này cho thấy recursive function frame thật ra chứa `u`, local variables và vị trí loop hiện tại.

## Recursion depth

Graph dạng chain với hàng trăm nghìn nodes có thể overflow call stack.

C, Java và JavaScript đều có practical recursion limits khác nhau. Không nên dựa vào tail-call optimization portable.

Nếu input depth không controlled, iterative DFS là safer engineering choice.

## Visited: mark khi push hay khi pop?

Với BFS, thường mark visited **khi enqueue**, không phải khi dequeue. Nếu đợi tới dequeue, cùng node có thể được enqueue nhiều lần từ nhiều predecessors, làm queue phình lớn.

DFS iterative cũng thường mark khi push/discover tùy semantics.

Rule phải nhất quán với invariant “mỗi state được scheduled bao nhiêu lần?”.

## Graph state và visited key

Visited phải match state identity.

Nếu state là:

```text
(node, fuel)
```

thì `seen[node]` là sai; cần `seen[node][fuel]` hoặc canonical key tương đương.

Nếu hai histories dẫn tới cùng future-equivalent state, visited có thể merge chúng. Đây là cùng concept với DP memoization.

## BFS/DFS trên implicit graph

Puzzle, word transformation, lock combinations, scheduling states có thể không materialize adjacency.

Một function:

```text
neighbors(state)
```

generate transitions khi cần.

Complexity khi đó nên đo theo số reachable states và generated transitions, không nhất thiết theo một pre-existing `V,E` literal.

## Flood fill

Flood fill là BFS/DFS trên grid component. Điểm đáng học không phải thuật toán riêng mà là mapping:

```text
cell = vertex
adjacent same-color/passable cells = edges
```

Once model đúng, connected-component toolkit áp dụng trực tiếp.

## Bipartite check bằng BFS/DFS coloring

Undirected graph bipartite iff có thể 2-color vertices sao cho mọi edge nối khác màu.

BFS:

```text
color source = 0
neighbor = 1 - color[u]
conflict nếu edge nối cùng màu
```

Odd cycle là obstruction cho bipartiteness.

Đây là example traversal + small metadata giải structural property.

## Component metadata

Traversal có thể aggregate nhiều thứ trong cùng pass:

```text
component size
sum/min/max value
hasCycle
bounding box trong grid
edge count
```

Nếu component undirected có `V_c` vertices và `E_c` edges, tree component thỏa `E_c = V_c - 1`; thêm edge có thể tạo cycle.

## Complexity thật sự

Với adjacency list:

\[
O(V+E)
\]

vì mỗi vertex visited một số lần constant và mỗi adjacency entry scanned một lần.

Nhưng constants phụ thuộc representation. Object-heavy graph có cache misses/GC; CSR có sequential locality tốt hơn. DFS recursion còn có call overhead.

Big-O giống nhau không nghĩa runtime giống nhau.

## Memory complexity

BFS frontier có thể chứa cả một layer lớn, worst `O(V)`.

DFS stack depth có thể `O(V)` trên chain, nhưng trên balanced/deep-narrow graph thường nhỏ hơn BFS frontier.

Vì vậy BFS vs DFS đôi khi được chọn vì memory shape chứ không chỉ semantics.

## Common misconceptions

“BFS luôn nhanh hơn DFS vì tìm gần trước” là sai. Cả hai `O(V+E)`; goal quyết định suitable traversal.

“DFS recursive luôn dùng ít memory” sai; deep chain có stack `O(V)` và có thể crash.

“Visited là boolean theo vertex” sai khi state có thêm dimensions.

“Lần đầu thấy node trong weighted graph là shortest” chỉ đúng với BFS equal-weight setting, không với arbitrary positive weights.

“Undirected cycle = gặp visited node” sai vì parent edge luôn quay về visited parent.

## Testing traversal

Ngoài examples, test structural properties:

```text
BFS dist[source] == 0
mọi discovered edge thỏa dist[v] <= dist[u]+1 trong unweighted graph
parent chain của reachable node dẫn về source
DFS visits exactly component vertices
no node scheduled repeatedly ngoài design
component count đúng reference model
```

Random small graphs có thể so BFS distances với Floyd-Warshall reference để differential test.

## Khi chọn BFS, DFS hay priority-based search?

Một useful decision model:

```text
reachable/component only      -> BFS hoặc DFS
minimum number of edges       -> BFS
0/1 weights                   -> 0-1 BFS
nonnegative general weights   -> Dijkstra
structural nesting/postorder  -> DFS
all possible branches         -> DFS/backtracking
near-vs-deep exploration      -> frontier policy quyết định
```

Traversal family thực chất khác nhau ở cách chọn **next frontier state**.

## Mental Model

> BFS và DFS không phải hai code templates để học thuộc. Chúng là hai cách tổ chức frontier. BFS bảo toàn layer/distance order; DFS bảo toàn nested call/branch structure. Khi hiểu invariant của frontier, ta có thể derive multi-source BFS, bidirectional BFS, cycle detection, topo order, SCC, bridge logic và nhiều algorithms khác.

Trước khi code traversal, hãy hỏi:

```text
State identity là gì?
Visited được đánh dấu lúc nào?
Frontier cần FIFO, LIFO hay priority?
Có cần parent/path reconstruction không?
Graph có disconnected không?
Recursive depth có an toàn không?
Need preorder hay postorder semantics?
```

Xem tiếp: [Shortest Paths](./02_shortest_paths.md), [DAG & SCC](./04_dag_topological_sort_and_scc.md), [Bridges & Articulation](./06_bridges_articulation_and_biconnectivity.md).