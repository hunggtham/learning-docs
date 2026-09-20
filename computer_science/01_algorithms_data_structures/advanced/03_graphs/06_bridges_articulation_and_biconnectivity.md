# Bridges, Articulation Points và Biconnectivity
**Bridges, Articulation Points & Biconnectivity / 단절선, 단절점, 이중 연결성**

Một connected graph có thể trông “dày”, nhưng chỉ cần hỏng đúng một edge hoặc một vertex là topology bị tách đôi. **Bridge / 단절선** là edge mà khi xóa làm số connected components tăng. **Articulation Point / 단절점** là vertex mà khi xóa cùng incident edges làm số components tăng.

Đây là cách graph theory diễn tả **single point of failure**. Trong mạng, bridge có thể là đường truyền duy nhất; articulation point có thể là router/hub trung tâm. Nhưng mục tiêu của chapter này không chỉ là học công thức `low[v] > tin[u]`; quan trọng hơn là hiểu **low-link value đang tóm tắt khả năng escape khỏi một DFS subtree như thế nào**.

## 1. Tại sao DFS tree chưa đủ?

Khi chạy DFS trên undirected graph, mỗi vertex lần đầu được discover qua một tree edge. Nếu chỉ nhìn DFS tree, mọi parent-child edge dường như đều “quan trọng”, vì subtree child treo dưới parent.

Nhưng graph gốc có thể có edge khác từ subtree quay lên một ancestor. Edge đó tạo alternate route. Vì vậy câu hỏi thật sự là:

> Subtree của child có thể thoát ra ngoài mà không cần dùng lại parent edge hay không?

`low` chính là summary cho câu hỏi này.

## 2. `tin[u]`: thời điểm discover

Khi DFS vào `u`:

```text
tin[u] = low[u] = timer++
```

`tin` tạo thứ tự discover. Ancestor trong DFS tree luôn có `tin` nhỏ hơn descendant.

`low[u]` ban đầu bằng `tin[u]` vì chắc chắn subtree của `u` reachable tới chính `u`.

## 3. Meaning của `low[u]`

Trong undirected DFS chuẩn, `low[u]` là discovery time nhỏ nhất của vertex có thể reachable từ `u` hoặc descendants bằng cách đi xuống zero/more tree edges rồi dùng tối đa một back edge lên ancestor theo structure relevant.

Update rules:

Khi child `v` xong:

\[
low[u]=\min(low[u],low[v])
\]

Khi gặp visited neighbor `v` qua một edge không phải parent edge:

\[
low[u]=\min(low[u],tin[v])
\]

Điểm quan trọng: với back edge dùng `tin[v]`, không tùy tiện dùng `low[v]`, vì low của một visited vertex có thể encode đường đi không tương ứng với edge classification hiện tại.

## 4. Bridge Condition

Với DFS tree edge `(u,v)`:

\[
low[v] > tin[u]
\]

thì `(u,v)` là bridge.

Nếu subtree `v` không thể reach `u` hoặc ancestor của `u` bằng route khác, parent edge là cửa duy nhất ra ngoài. Xóa nó làm subtree tách khỏi phần còn lại.

## 5. Vì sao là `>` chứ không phải `>=`?

Nếu:

\[
low[v]=tin[u]
\]

nghĩa là subtree có back edge quay lại chính `u`. Khi xóa tree edge `(u,v)`, alternate route đó vẫn nối subtree với `u`. Vì vậy edge không phải bridge.

Equality đủ cứu edge, nhưng không đủ cứu vertex như articulation condition phía dưới.

## 6. Articulation Point cho non-root

Với non-root `u`, nếu tồn tại child `v`:

\[
low[v] \ge tin[u]
\]

thì `u` là articulation point.

Nếu equality xảy ra, subtree `v` có thể quay về `u`, nhưng xóa chính `u` thì route đó cũng biến mất. Subtree không reach được ancestor cao hơn.

Đây là lý do articulation dùng `>=` còn bridge dùng `>`.

## 7. Root là case đặc biệt

DFS root không có ancestor phía trên. Root là articulation point khi có **ít nhất hai DFS tree children**.

Nếu root chỉ có một child, toàn bộ phần reachable nằm trong một subtree; xóa root không làm phần còn lại tách thành nhiều components mới hơn theo definition chuẩn.

Nếu root có hai children, DFS từ child thứ nhất đã không thể reach child thứ hai trước khi return, nên root là điểm nối duy nhất giữa chúng trong DFS structure.

## 8. Edge ID bắt buộc khi có parallel edges

Trong multigraph, check:

```text
if (v == parent) continue
```

có thể sai. Giữa `u` và parent có thể tồn tại hai edge song song: một edge là tree edge, edge còn lại là alternate back connection.

Cách robust là mỗi physical edge có unique ID, và DFS nhận `parentEdgeId`:

```java
if (e.id == parentEdgeId) continue;
```

Representation detail này ảnh hưởng trực tiếp correctness.

## 9. Java core implementation

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

Disconnected graph cần DFS từ mọi unvisited vertex.

## 10. Complexity

Mỗi vertex visit một lần, mỗi undirected edge xuất hiện hai adjacency entries và được xử lý constant number of times:

\[
O(V+E)
\]

Space gồm graph, arrays và DFS stack. Recursive implementation có depth `O(V)` trên path graph và có thể stack overflow.

## 11. Iterative low-link DFS khó hơn DFS thường

Recursive call tự động tạo postorder event: child hoàn tất rồi mới update `low[parent]`.

Iterative DFS phải explicit frame:

```text
vertex
parentEdge
nextAdjIndex
numberOfChildren
```

Khi frame child pop, parent mới có thể apply:

```text
low[parent] = min(low[parent], low[child])
```

Đây là ví dụ rõ rằng recursion frame lưu continuation state, không chỉ vertex ID.

## 12. Characterization: bridge iff edge không thuộc cycle

Trong undirected graph:

> Edge là bridge khi và chỉ khi nó không thuộc bất kỳ cycle nào.

Nếu thuộc cycle, phần còn lại của cycle tạo alternate route. Nếu không thuộc cycle, edge là link duy nhất giữa hai phía theo topology tương ứng.

Low-link DFS là cách tìm tất cả bridge cùng lúc thay vì kiểm tra từng edge riêng lẻ.

## 13. Naive remove-and-test vì sao đắt?

Với mỗi edge, remove rồi DFS/BFS:

\[
O(E(V+E))
\]

Với articulation:

\[
O(V(V+E))
\]

Low-link nén toàn bộ alternate-connectivity information vào một DFS linear-time. Đây là một ví dụ điển hình của **precompute summary thay recompute toàn problem cho từng candidate**.

## 14. 2-edge-connected components và Bridge Tree

Nếu remove tất cả bridges, graph tách thành components mà bên trong không còn bridge.

Contract mỗi component thành một super-node, original bridges trở thành edges giữa super-nodes. Kết quả là một tree/forest gọi là **bridge tree**.

Tại sao không thể có cycle giữa super-nodes? Nếu có cycle, bridge trên cycle có alternate route, mâu thuẫn nó là bridge.

Bridge tree biến graph vulnerability problem thành tree problem.

## 15. Queries sau khi build Bridge Tree

Sau decomposition, nhiều queries dễ hơn:

```text
bao nhiêu bridge trên path giữa u và v?
edge failure nào tách hai nodes?
components nào nằm hai phía của bridge?
```

Map original vertices sang bridge-component rồi dùng LCA/prefix depth trên tree để trả lời path queries.

Một expensive graph preprocessing có thể đổi nhiều online queries thành tree arithmetic nhanh.

## 16. Vertex-biconnected components

Articulation decomposition tinh tế hơn vì articulation vertex có thể thuộc nhiều blocks.

Một **biconnected component / block** là maximal subgraph không bị tách bởi removal một internal single vertex theo definition tương ứng.

Tarjan-style algorithm giữ stack of edges. Khi child `v` thỏa:

\[
low[v] \ge tin[u]
\]

thì edge stack từ `(u,v)` trở lên tạo một block mới.

## 17. Block-Cut Tree

Ta tạo hai loại nodes:

```text
block nodes
articulation-vertex nodes
```

Nối articulation node với block node nếu articulation thuộc block đó. Kết quả là bipartite tree/forest gọi là **block-cut tree**.

Structure này hỗ trợ reasoning kiểu:

```text
path giữa hai regions phải đi qua articulation nào?
bao nhiêu single-vertex failure points trên route structural?
```

## 18. Edge connectivity vs vertex connectivity

Bridge liên quan **edge redundancy**. Articulation liên quan **vertex redundancy**.

Một graph có thể không có bridge nhưng vẫn có articulation point. Ví dụ hai cycles chia sẻ một vertex: không edge đơn lẻ nào làm graph disconnect, nhưng xóa vertex chung sẽ tách hai cycles.

Vì vậy “network có nhiều alternate edges” chưa đủ chứng minh node-level fault tolerance.

## 19. Menger's Theorem connection

Menger cho một connection sâu giữa:

```text
minimum cut size
number of disjoint paths
```

Bridge nghĩa edge connectivity giữa một số regions bằng 1. Articulation point nghĩa vertex connectivity ở nơi đó bằng 1.

Low-link algorithm là specialized linear-time detector cho những cut size 1 cases.

Nếu cần minimum cut lớn hơn 1/general capacities, ta tiến sang flow/min-cut algorithms.

## 20. Bridge Tree và reliability scoring

Có thể xem mỗi bridge là một failure domain boundary. Size của subtree sau khi root bridge tree cho biết bao nhiêu vertices bị cô lập nếu bridge hỏng.

Nếu muốn rank “impact” của bridge, một metric đơn giản có thể dựa trên số pairs bị disconnect:

\[
size \cdot (N-size)
\]

với `size` là số original vertices ở một phía.

Đây là ví dụ biến structural decomposition thành risk metric, nhưng production model có thể cần weights/traffic/capacity thực tế.

## 21. Articulation impact không chỉ boolean

Biết `u` là articulation point mới là bước đầu. Một câu hỏi sâu hơn là xóa `u` tạo bao nhiêu components và sizes ra sao.

Mỗi DFS child với:

\[
low[child] \ge tin[u]
\]

trở thành một separated region khi xóa `u`. Phần ancestors/outside subtree tạo thêm một region nếu `u` không phải DFS root.

Có thể augment DFS với subtree sizes để tính impact.

## 22. Online/dynamic graph khác hẳn static low-link

Nếu edges được add/remove liên tục, chạy Tarjan lại sau mỗi update có thể đắt.

Incremental/dynamic connectivity và dynamic biconnectivity là advanced topics cần data structures phức tạp hơn. Low-link là giải pháp static graph rất mạnh nhưng không tự hỗ trợ arbitrary updates.

Đây là pattern quan trọng: một linear preprocessing algorithm chưa chắc phù hợp online workload.

## 23. Directed graph không dùng cùng công thức

Standard bridge/articulation chapter này là undirected graph. Directed graph có:

```text
strong bridges
strong articulation points
dominators
SCC-based structure
```

và algorithms khác. Copy `low[v] > tin[u]` sang directed graph là sai model.

## 24. Low-link của Bridge algorithm và Tarjan SCC không interchangeable

Cả hai dùng biến tên `low`, nhưng invariant khác.

Bridge low-link nói về escape từ undirected DFS subtree lên ancestor qua back edge.

Tarjan SCC low-link liên quan earliest reachable discovery index trong active DFS stack/SCC context.

Tên biến giống nhau không có nghĩa update rule giống nhau.

## 25. Self-loops và parallel edges

Self-loop không thể là bridge vì bỏ nó không thay connectivity giữa vertices. Nó có thể ảnh hưởng adjacency processing nhưng không làm alternate component connection.

Parallel edges khiến hai endpoints có alternate edge trực tiếp, nên từng edge riêng lẻ không phải bridge nếu có ít nhất hai parallel connections.

Test multigraph là cách rất tốt để phát hiện code dùng `parent vertex` thay vì `parent edge id`.

## 26. Testing bằng graph families

Các cases quan trọng:

```text
path: mọi edge bridge, internal vertex articulation
simple cycle: không bridge/articulation
star: mọi spoke bridge, center articulation
clique: thường không bridge/articulation
hai cycles nối bằng bridge
hai cycles share một vertex
parallel-edge pair
self-loop
single vertex
disconnected graph
```

Random graph nhỏ có thể verify bridge bằng brute-force remove edge + BFS, articulation bằng remove vertex + BFS.

Differential testing kiểu này rất mạnh vì oracle đơn giản dù chậm.

## 27. Invariant testing của `tin/low`

Sau DFS:

```text
low[u] <= tin[u]
```

cho mọi visited vertex.

Với child tree edge, parent update phải làm `low[parent] <= low[child]` không nhất thiết luôn đúng vì parent có back edge riêng, nhưng `low[parent]` phải bằng min của relevant contributions.

Một validator/debug implementation có thể recompute low-like reachability trên graph nhỏ để so result.

## 28. Systems interpretation và limitation

Bridge/articulation model dùng topology binary: connected hay disconnected. Nhưng production reliability còn có:

```text
capacity
latency
traffic volume
failure probability
shared physical conduit
availability zones
```

Hai logical edges có thể đi chung một cable vật lý; graph nhìn redundant nhưng failure domain thực tế không redundant.

Algorithm chỉ đúng với model. Reliability engineering bắt đầu từ graph abstraction chính xác.

## 29. Connection với spanning tree

Mọi bridge phải xuất hiện trong **mọi spanning tree** của connected graph, vì bỏ bridge làm graph disconnect nên không có alternate edge set nối hai phía.

Ngược lại edge không bridge có thể hoặc không xuất hiện trong một spanning tree tùy choices.

Connection này liên kết low-link connectivity với MST/spanning-tree theory.

## 30. Connection với Eulerian graph

Một connected undirected Eulerian graph mà mọi vertex có even degree không thể có bridge nếu có ít nhất một edge trong component Eulerian cycle covering all edges: mọi edge nằm trên cycle của Euler tour.

Đây là một cách thấy các graph properties không độc lập; degree/cycle structure ảnh hưởng cut vulnerability.

## Mental Model

> `low[u]` là một **compressed escape certificate** của DFS subtree: subtree này có alternate route lên ancestor cao đến đâu mà không quay lại parent edge?

Nếu child không escape tới parent, parent edge là bridge. Nếu child chỉ escape tới chính parent nhưng không vượt parent, xóa parent vertex sẽ cô lập child subtree. Từ local summary `low`, ta suy ra global vulnerability trong `O(V+E)`.

Xem thêm: [Graph Traversal](./01_graph_traversal_bfs_dfs.md), [MST](./03_minimum_spanning_trees.md), [SCC](./04_dag_topological_sort_and_scc.md), [Network Flow](./08_network_flow_and_matching.md).