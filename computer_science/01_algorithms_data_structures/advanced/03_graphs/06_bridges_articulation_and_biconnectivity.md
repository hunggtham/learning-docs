# Bridges, Articulation Points và Biconnectivity
**Bridges, Articulation Points & Biconnectivity / 단절선, 단절점, 이중 연결성**

Một connected graph có thể chứa những edges hoặc vertices đóng vai trò **single point of failure**. Nếu xóa một edge làm số connected components tăng, edge đó là **bridge / 단절선**. Nếu xóa một vertex và các incident edges của nó làm số components tăng, vertex đó là **articulation point / 단절점**.

Các khái niệm này mô hình hóa reliability rất trực tiếp: đường truyền nào bị đứt sẽ tách network? Router nào hỏng sẽ chia hệ thống thành nhiều vùng? Thành phần nào cần redundancy?

## 1. Tại sao DFS tree chưa đủ?

Nếu chạy DFS trên undirected graph, ta tạo một DFS tree. Một tree edge `(u,v)` nhìn bề ngoài có vẻ quan trọng vì nó là đường DFS đã dùng để vào subtree `v`.

Nhưng graph gốc có thể có **back edge** từ subtree của `v` quay lên `u` hoặc một ancestor cao hơn. Khi đó dù xóa `(u,v)`, subtree vẫn có route khác ra ngoài.

Vì vậy để biết edge/vertex nào thật sự là điểm cắt, ta phải biết subtree có thể “leo ngược” lên cao đến đâu ngoài parent edge.

Đó là vai trò của `low` value.

## 2. Discovery Time `tin`

Khi DFS visit vertex `u`, gán:

```text
tin[u] = thời điểm u được discover
```

`tin` tạo thứ tự ancestor-descendant theo DFS tree. Ancestor được discover trước descendant.

Ta dùng một counter tăng dần:

```text
tin[u] = low[u] = timer++
```

ban đầu `low[u]` chính là `tin[u]`, vì chắc chắn u reachable từ chính nó.

## 3. Low-link Value `low[u]`

`low[u]` biểu diễn discovery time nhỏ nhất của một vertex có thể reachable từ `u` hoặc subtree của `u` bằng cách đi xuống các tree edges và dùng một back edge lên ancestor theo formulation chuẩn của undirected DFS.

Khi DFS từ `u` xuống child `v` hoàn tất:

\[
low[u] = \min(low[u], low[v])
\]

Nếu gặp edge `(u,v)` tới một vertex đã visited không phải parent edge:

\[
low[u] = \min(low[u], tin[v])
\]

Điểm rất quan trọng là với back edge, ta dùng `tin[v]`, không dùng `low[v]` tùy tiện. `low[v]` có thể encode paths đi qua tree relationships không phù hợp với edge classification hiện tại.

## 4. Bridge Condition

Xét DFS tree edge từ parent `u` xuống child `v`.

Nếu:

\[
low[v] > tin[u]
\]

thì `(u,v)` là bridge.

Lý do: subtree của `v` không có back edge tới `u` hoặc bất kỳ ancestor của `u`. Đường duy nhất nối subtree đó với phần graph phía trên trong DFS structure là edge `(u,v)`.

Nếu xóa edge, subtree bị tách.

## 5. Vì sao điều kiện Bridge là `>` chứ không phải `>=`?

Nếu `low[v] == tin[u]`, nghĩa là subtree của `v` có một back edge quay lại chính `u`. Khi xóa tree edge `(u,v)`, vẫn còn một route khác từ subtree về `u` qua back edge đó.

Do đó equality không đủ để edge là bridge.

Đây là một chi tiết nhỏ nhưng là nguồn off-by-one-like bug logic rất phổ biến.

## 6. Articulation Point cho non-root

Với non-root vertex `u`, nếu tồn tại DFS child `v` sao cho:

\[
low[v] \ge tin[u]
\]

thì `u` là articulation point.

Tại sao ở đây lại là `>=`?

Nếu `low[v] == tin[u]`, subtree của `v` có thể quay về `u`, nhưng nếu xóa chính `u`, route đó cũng biến mất. Subtree không thể vượt qua u để tới ancestor cao hơn.

Vì vậy equality vẫn khiến u là điểm cắt.

## 7. Root là case đặc biệt

DFS root không có parent/ancestor phía trên. Condition `low[child] >= tin[root]` gần như luôn true theo structure nên không thể dùng trực tiếp.

Root là articulation point nếu nó có **ít nhất hai DFS tree children độc lập**.

Nếu root chỉ có một DFS child, toàn bộ reachable graph nằm dưới một subtree; xóa root không nhất thiết làm số components tăng theo articulation definition chuẩn cho connected component đó.

Nếu root có hai hoặc nhiều children, vì DFS từ một child không reach được child khác trước khi quay về root, bỏ root tách các child subtrees.

## 8. Edge IDs rất quan trọng với Multi-edge

Trong undirected graph có parallel edges giữa u và v, chỉ kiểm tra:

```text
if (v == parent) continue;
```

có thể sai. Một edge là tree parent edge, nhưng parallel edge còn lại là một legitimate back connection và phải được xét.

Cách an toàn là gắn unique edge ID, truyền `parentEdgeId`, và skip đúng edge vật lý đã dùng để đi xuống:

```java
if (e.id == parentEdge) continue;
```

Đây là representation detail trực tiếp ảnh hưởng correctness.

## 9. Java implementation core

```java
void dfs(int u, int parentEdge) {
    seen[u] = true;
    tin[u] = low[u] = timer++;
    int children = 0;

    for (Edge e : g.get(u)) {
        if (e.id == parentEdge) continue;
        int v = e.to;

        if (seen[v]) {
            low[u] = Math.min(low[u], tin[v]);
        } else {
            dfs(v, e.id);
            low[u] = Math.min(low[u], low[v]);

            if (low[v] > tin[u]) {
                bridges.add(e.id);
            }

            if (parentEdge != -1 && low[v] >= tin[u]) {
                articulation[u] = true;
            }

            children++;
        }
    }

    if (parentEdge == -1 && children > 1) {
        articulation[u] = true;
    }
}
```

Nếu graph disconnected, phải gọi DFS từ mọi unvisited vertex, không chỉ vertex 0.

## 10. Complexity

Mỗi vertex được visit một lần, mỗi undirected edge xuất hiện hai adjacency entries và được xử lý constant number of times.

Time:

\[
O(V+E)
\]

Space gồm adjacency structure, arrays `tin`, `low`, `seen`, recursion stack hoặc explicit stack:

\[
O(V+E)
\]

Graph rất sâu có thể làm recursive DFS stack overflow; iterative low-link implementation có thể tránh nhưng phức tạp hơn vì phải mô phỏng postorder state.

## 11. Bridge Tree / 2-edge-connected Components

Nếu remove tất cả bridges, graph tách thành các components mà bên trong không có bridge. Đây là **2-edge-connected components** theo nghĩa relevant.

Coalesce mỗi component thành một super-node, rồi nối bằng original bridges. Kết quả tạo một tree/forest thường gọi là **bridge tree**.

Tại sao là tree? Nếu super-nodes connected bằng bridges tạo cycle, một edge trên cycle sẽ không còn là bridge vì có alternate route.

Bridge tree giúp nhiều queries về vulnerability trở thành tree queries.

## 12. Vertex-Biconnected Components

Với articulation points, decomposition tinh tế hơn vì một articulation vertex có thể thuộc nhiều blocks.

Một **biconnected component/block** là maximal subgraph không bị tách bởi xóa một single vertex nội bộ theo định nghĩa chuẩn tương ứng.

Tarjan-style DFS có thể dùng stack của edges. Khi `low[v] >= tin[u]`, ta biết một block boundary và pop edges cho tới edge `(u,v)`.

Kết quả có thể được biểu diễn bằng **block-cut tree**: articulation vertices và biconnected blocks trở thành hai loại nodes trong một bipartite tree/forest.

## 13. Block-Cut Tree

Trong block-cut tree, một articulation point node nối với các block nodes mà nó thuộc.

Structure này biến một graph có articulation complexity thành tree, giúp reason về paths qua cut vertices và connectivity queries.

Đây là pattern rất phổ biến trong graph algorithms: decompose graph thành robust components rồi contract thành simpler tree/DAG.

## 14. Reliability Interpretation

Bridge là link mà failure một mình disconnects một phần system.

Articulation point là router/server/hub mà failure một mình disconnects topology.

2-edge-connectivity nghĩa là giữa relevant vertices có redundancy về edges; 2-vertex-connectivity mạnh hơn vì chịu được mất một vertex.

Menger's theorem cung cấp connection sâu hơn giữa số disjoint paths và minimum cut sets.

## 15. Bridge và Edge-disjoint Paths

Một edge `(u,v)` là bridge nếu không có alternate path giữa u và v sau khi bỏ edge đó. Nói cách khác, edge không nằm trong bất kỳ cycle nào.

Đây là một characterization rất trực quan:

> Trong undirected graph, một edge là bridge **iff** nó không thuộc cycle nào.

Nếu edge nằm trong cycle, phần còn lại của cycle tạo route thay thế. Nếu không nằm trong cycle, removal disconnects endpoints trong component.

Low-link DFS là cách tìm tất cả bridges cùng lúc trong linear time thay vì test-remove từng edge.

## 16. Articulation và Vertex-disjoint Paths

Articulation point thể hiện thiếu vertex-level redundancy. Nếu hai regions chỉ nối qua u, mọi path giữa chúng phải đi qua u.

Biconnectivity liên quan việc có multiple internally vertex-disjoint paths giữa pairs theo các theorem chuẩn.

Vì vậy low-link values thực chất đang đo khả năng subtree escape qua alternate connections.

## 17. Why Not Remove Each Edge/Vertex and Re-run DFS?

Naive bridge test: với mỗi edge, remove rồi DFS/BFS kiểm tra connectivity. Nếu có E edges, complexity có thể:

\[
O(E(V+E))
\]

Articulation naive tương tự `O(V(V+E))`.

Low-link algorithm nén toàn bộ information về alternate ancestor reachability vào một DFS pass `O(V+E)`.

Đây là ví dụ tuyệt vời của algorithmic reuse: thay vì recompute connectivity sau từng deletion, ta infer vulnerability từ DFS structure.

## 18. Directed Graph không dùng cùng condition đơn giản

Bridge/articulation formulation ở đây dành cho undirected graph.

Directed graph có strongly connected components, dominators và strong articulation/bridge notions phức tạp hơn. Không thể copy công thức `low[v] > tin[u]` sang directed graph một cách mù quáng.

Graph direction thay đổi connectivity semantics căn bản.

## 19. Low-link và SCC dễ bị nhầm

Tarjan SCC algorithm cũng dùng discovery indices và low-link-like values, nhưng meaning/invariant không giống hoàn toàn bridge DFS trên undirected graph.

Trong SCC, stack membership và reachability trong directed graph đóng vai trò khác. Dùng cùng tên `low` không có nghĩa công thức interchangeable.

Khi học graph algorithms, luôn ghi rõ `low` đang đại diện cho cái gì trong algorithm cụ thể.

## 20. Testing các corner cases

Một path graph:

```text
0 - 1 - 2 - 3
```

mọi edge là bridge; internal vertices 1,2 là articulation points.

Một simple cycle không có bridge/articulation point.

Hai cycles nối bằng một edge: edge nối là bridge, endpoints thường articulation theo topology.

Parallel edges giữa hai vertices: không edge nào riêng lẻ là bridge nếu có alternate parallel edge.

Single vertex và two-vertex graph giúp kiểm tra root logic.

## 21. Recursion và state initialization

`timer` phải tăng global/component-wide đủ để discovery times unique. `tin`/`low` arrays phải reset đúng giữa independent runs.

Nếu graph có many vertices path-like, Java/JavaScript recursion có thể overflow. Production code cần explicit stack hoặc stack-size strategy phù hợp.

## 22. Application beyond literal networks

Dependency graph undirected abstractions, circuit connectivity, road/rail topology, social/communication backbones và game maps đều có thể cần tìm articulation/bridge.

Trong software architecture, service dependency graph thường directed và richer than this model, nhưng articulation intuition vẫn hữu ích để nghĩ về single points of failure trước khi chọn model chính xác hơn.

## Mental Model

> `low[u]` trả lời: **subtree này có thể thoát lên ancestor cao đến đâu mà không cần quay qua parent edge?**

Nếu child subtree không thể đi lên tới parent hoặc cao hơn, parent edge là bridge. Nếu subtree chỉ có thể quay lại chính parent nhưng không vượt qua parent, xóa parent vertex sẽ cắt subtree và parent là articulation point.

Low-link không phải magic formula; nó là compressed summary của alternate connectivity được tính trong postorder DFS.

Xem thêm: [Graph Traversal BFS/DFS](./01_graph_traversal_bfs_dfs.md), [SCC & DAG](./04_dag_topological_sort_and_scc.md), [Network Flow & Disjoint Paths](./08_network_flow_and_matching.md).