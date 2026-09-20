# Graph: mô hình hóa và biểu diễn
**Đồ thị (Graph / 그래프)**

Graph là abstraction cho tình huống mà **relationship quan trọng ngang entity**. User và friendship, city và road, package và dependency, service và network call, bank account và transaction, webpage và hyperlink, function và call relation đều có thể được mô hình hóa bằng:

\[
G=(V,E)
\]

trong đó `V` là tập vertices/nodes và `E` là tập edges.

Điểm khó nhất của graph problem thường không phải BFS hay Dijkstra. Phần khó là quyết định:

```text
một vertex đại diện cho cái gì?
một edge có nghĩa gì?
state nào cần được phân biệt?
weight/capacity/time có nằm trên edge hay node?
graph là directed, undirected, multigraph hay state graph?
```

Một thuật toán hoàn toàn đúng trên **model sai** vẫn cho answer sai cho problem thật.

## Directed, undirected và weighted

**Undirected graph / 무방향 그래프** dùng edge `u -- v` khi relationship đối xứng: road hai chiều, friendship, cable connection.

**Directed graph / 방향 그래프** dùng edge `u -> v` khi relationship có hướng: dependency, hyperlink, money transfer, call graph.

**Weighted graph / 가중 그래프** gắn cost lên edge hoặc node. Weight có thể là distance, latency, price, risk, time, energy, probability transform hoặc capacity.

Không phải mọi weight đều dùng shortest path. Capacity dẫn tới flow; probability có thể cần log transform; exchange rate có thể dẫn tới negative-cycle/arbitrage reasoning.

## Simple graph, multigraph và self-loop

Một **simple graph** không có parallel edges và thường không có self-loop. Nhưng nhiều domains thực tế cho phép cả hai.

Parallel edges xuất hiện khi hai cities có nhiều flights khác nhau, hai services có nhiều channels hoặc graph giữ historical links.

Self-loop xuất hiện khi một state có transition về chính nó hoặc data chứa explicit relation `(u,u)`.

Nếu algorithm vô thức giả định simple graph, kết quả có thể sai. Bridge detection là ví dụ: hai parallel edges giữa cùng cặp nodes nghĩa là xóa một edge chưa chắc disconnect graph. Vì vậy edge identity phải được giữ rõ.

## Path, walk, trail và cycle

Một **walk** cho phép lặp vertices/edges. **Trail** thường không lặp edge. **Path** thường không lặp vertex trong định nghĩa graph-theory chuẩn. **Cycle** quay lại điểm bắt đầu.

Trong programming problems, từ “path” đôi khi được dùng lỏng hơn. Khi proof quan trọng, hãy xác định semantics chính xác thay vì dựa vào wording.

Shortest path với non-negative weights luôn có thể chọn một simple path optimal vì cycle không giúp giảm cost. Nhưng với negative cycle, objective có thể không còn finite minimum.

## Connectivity và reachability

Trong undirected graph, **connected component / 연결 요소** là maximal set vertices nối được với nhau.

Trong directed graph, reachability có hướng. Strongly connected component yêu cầu reachability hai chiều giữa mọi cặp nodes trong component.

Đây là lý do “component” trong directed graph không đơn giản là chạy BFS và gom tất cả nodes reachable từ source.

## Degree

Undirected vertex có degree bằng số incident edges, với self-loop convention cần chú ý.

Directed graph có:

```text
indegree  = số edges đi vào
outdegree = số edges đi ra
```

Degree không chỉ là metadata. Eulerian conditions dùng parity/balance của degree; Kahn topological sort dùng indegree; graph sparsity thường liên quan average degree.

## Adjacency matrix

Adjacency matrix dùng `V x V` cells.

```text
matrix[u][v] = có edge hay weight
```

Ưu điểm:

```text
edge existence lookup O(1)
representation đơn giản
tốt cho dense graph hoặc matrix algorithms
```

Nhược điểm:

```text
memory O(V^2)
iterate neighbors của u tốn O(V)
không phù hợp sparse graph lớn
```

Nếu graph có 1 triệu vertices nhưng mỗi vertex chỉ vài neighbors, matrix là bất khả thi.

## Adjacency list

Adjacency list lưu neighbors theo từng vertex.

Memory:

\[
O(V+E)
\]

và iteration neighbors của `u` là `O(deg(u))`.

Java:

```java
List<List<Edge>> g = new ArrayList<>(n);
for (int i = 0; i < n; i++) g.add(new ArrayList<>());
```

JavaScript:

```js
const g = Array.from({ length: n }, () => []);
```

Undirected edge thường được lưu hai adjacency entries. Nếu algorithm cần biết hai entries đó đại diện cùng physical edge, hãy gắn unique edge id.

## Edge list

Edge list chỉ lưu:

```text
(u, v, weight)
```

Nó phù hợp khi algorithm xử lý edges toàn cục hơn là neighbors từng vertex.

Kruskal MST là ví dụ điển hình:

```text
sort toàn bộ edges theo weight
scan edges
DSU quyết định edge có nối hai component khác nhau không
```

Không có representation “tốt nhất”; operation chính quyết định representation.

## CSR — Compressed Sparse Row

Object-heavy adjacency lists tiện code nhưng có overhead references/allocations. Trong high-performance graph processing, **CSR (Compressed Sparse Row)** lưu graph bằng contiguous arrays.

Conceptually:

```text
offsets[u] .. offsets[u+1]-1
```

là segment trong `edges[]` chứa neighbors của `u`.

Ví dụ:

```text
offsets = [0, 2, 5, 5]
edges   = [1, 2, 0, 2, 3]
```

Neighbors của node 1 là `edges[2..4]`.

CSR giảm per-node object overhead, tăng locality và rất hợp static sparse graph. Trade-off là dynamic insert/delete khó hơn adjacency lists động.

## Adjacency map và sparse external IDs

Nếu vertex IDs là strings hoặc sparse 64-bit IDs, có thể dùng mapping:

```text
external id -> compact integer id
```

sau đó lưu graph bằng arrays trên compact IDs.

Điều này thường tốt hơn `Map<String,List<String>>` ở graph rất lớn vì comparisons, hash, object allocation và memory locality đều cải thiện.

Đây là một pattern production quan trọng: **normalize identity trước, optimize representation sau**.

## Modeling state-space graph

Trong nhiều bài, node không phải entity domain mà là **state / 상태**.

Ví dụ grid có key và door. State không thể chỉ là `(row,col)`; hai lần đứng cùng cell nhưng giữ key-mask khác nhau có future khác nhau.

State đúng có thể là:

```text
(row, col, keysMask)
```

Nếu ta visited theo `(row,col)` בלבד, algorithm có thể loại sai một đường quay lại cell với nhiều keys hơn.

Ngược lại, state chứa quá nhiều history không ảnh hưởng future sẽ làm graph phình khổng lồ.

Một state tốt giữ đúng **future-relevant information** — mental model này giống Dynamic Programming.

## Product graph

Khi problem có nhiều dimensions constraints, ta có thể tạo **product graph**.

Ví dụ shortest path với tối đa `K` coupons:

```text
state = (vertex, couponsUsed)
```

Edge transition có thể:

```text
đi bình thường: (u,k) -> (v,k)
dùng coupon:     (u,k) -> (v,k+1)
```

Graph mới có khoảng `V*(K+1)` states. Standard shortest-path algorithm giờ có thể chạy trên expanded state space.

Đây là cách biến “constraint phức tạp” thành topology rõ ràng.

## Time-expanded graph

Scheduling, transport và temporal network có thể cần time trong state:

```text
(vertex, time)
```

Ví dụ train chỉ chạy ở departure times cụ thể. Edge không chỉ nói “A nối B”; nó nói “từ A lúc t có thể tới B lúc t'”.

Time-expanded graph có thể lớn, nên đôi khi ta không materialize toàn bộ; generate transitions on demand.

## Implicit graph

Graph không nhất thiết phải được build trước.

Word ladder:

```text
vertex = một word
edge = đổi đúng một ký tự
```

Thay vì tạo mọi pair edges `O(n^2)`, ta có thể generate neighbors qua wildcard buckets hoặc dictionary lookup khi BFS cần.

Puzzle, game state và combinatorial search thường dùng implicit graphs.

Mental model:

> Graph là **relation**, không phải bắt buộc là `List<List<Integer>>`.

## Hypergraph và relation nhiều hơn hai endpoints

Standard graph edge nối hai vertices. Nhưng một relation có thể liên quan nhiều entities cùng lúc, ví dụ một database transaction chạm nhiều accounts hoặc một constraint chứa nhiều variables.

**Hypergraph** cho phép hyperedge nối nhiều vertices. Trong implementation, hyperedge thường được biến đổi thành bipartite incidence graph hoặc auxiliary node để dùng algorithms chuẩn.

Biết model này giúp tránh ép mọi problem về pairwise edge một cách sai nghĩa.

## Bipartite modeling

Nếu domain có hai loại entities rõ ràng — jobs/workers, students/projects, users/items — graph thường bipartite.

Tách hai phía giúp nhận ra matching/flow structure thay vì generic graph search.

Ví dụ:

```text
Worker -> Job nếu worker có thể làm job
```

Maximum matching trả assignment tối đa không conflict.

## Graph và sparse matrix

Adjacency matrix chính là matrix representation của relation. Nhiều graph algorithms có linear algebra interpretation.

Repeated matrix multiplication liên quan path counts/reachability. PageRank dùng transition matrix. Graph Neural Network layers thường aggregate neighbor features, tương đương sparse-matrix-like operations.

CSR thực chất cũng là representation kinh điển của sparse matrix. Graph theory và linear algebra vì thế là hai góc nhìn của cùng structure.

## Memory cost không chỉ là O(V+E)

Hai adjacency lists đều là `O(V+E)` nhưng constants có thể khác hàng lần.

Java:

```text
ArrayList<ArrayList<EdgeObject>>
```

có object headers, references và boxing nếu dùng wrapper types.

C arrays có thể compact hơn nhưng ownership/reallocation phức tạp hơn.

JavaScript arrays/objects có dynamic runtime overhead.

Khi graph có hàng chục triệu edges, representation bytes-per-edge trở thành một first-class design metric.

## Edge direction storage

Directed graph lưu đúng direction.

Undirected graph thường lưu hai entries:

```text
u -> v
v -> u
```

Nhưng algorithms như Euler/bridge cần tránh coi hai entries là hai physical edges khác nhau. Unique edge id hoặc paired reverse-index là pattern tốt.

Flow algorithms cũng thường tạo explicit reverse residual edge, nhưng reverse edge ở đó có semantics khác: nó đại diện khả năng undo flow chứ không phải original undirected relation.

## Graph mutation

Nếu graph static, CSR/sorted neighbor arrays rất tốt.

Nếu graph dynamic với nhiều edge insert/delete, structure cần hỗ trợ mutation: hash sets/maps per node, balanced sets hoặc specialized dynamic graph structures.

Trade-off:

```text
static -> compact, cache-friendly, preprocess mạnh
dynamic -> flexible update, nhiều metadata/overhead hơn
```

Đây là cùng pattern thấy ở sparse table vs segment tree.

## Dense vs sparse

Một graph có thể gọi là sparse khi `E` gần tuyến tính theo `V`, và dense khi `E` gần `V^2`.

Representation và algorithm thường thay đổi theo density.

Dijkstra adjacency matrix có thể `O(V^2)` và đủ tốt cho dense graph nhỏ. Heap + adjacency list tốt hơn với sparse graph lớn.

Floyd-Warshall `O(V^3)` đôi khi hợp graph nhỏ cần all-pairs, dù asymptotic nhìn rất lớn.

## Modeling failures phổ biến

### Gộp state quá mạnh

Visited theo city nhưng problem còn phụ thuộc stops-used, fuel, key-set hoặc time.

### State quá chi tiết

Lưu full path trong state khi future chỉ cần current vertex + small metadata. State explosion không cần thiết.

### Direction sai

Dependency `A depends on B` có thể encode `A->B` hoặc `B->A`; algorithm topological scheduling phụ thuộc convention. Hãy định nghĩa rõ edge nghĩa gì.

### Weight sai meaning

Latency path có thể cộng; bandwidth path bottleneck có thể dùng min; reliability có thể nhân probabilities. Không phải metric nào cũng là additive shortest path.

### Không xác định graph class

Parallel edge, self-loop, disconnected components, negative weights, directed/undirected đều có thể làm assumptions của algorithm sai.

## Modeling checklist

Trước khi chọn algorithm, viết rõ:

```text
Vertex = ?
Edge = ?
Directed hay undirected?
Parallel edges/self-loops có thể có không?
Weight/capacity nghĩa gì?
State tối thiểu cần nhớ để future được xác định là gì?
Graph static hay dynamic?
Sparse hay dense?
Có cần actual path hay chỉ value/reachability?
```

Chỉ sau đó mới hỏi BFS, DFS, Dijkstra, DSU hay flow.

## Mental Model

> Graph algorithm bắt đầu từ **state modeling**, không phải từ việc nhận diện tên thuật toán. Vertex là một equivalence class của situations có cùng future possibilities; edge là một allowed transition/relation. Representation phải tối ưu cho operation chính: neighbor traversal, edge lookup, global edge sort hay compact scan.

Một graph problem tốt thường được giải theo pipeline:

```text
Story/domain
→ xác định state/entity
→ xác định transition/relation
→ xác định graph class
→ chọn representation
→ chọn traversal/optimization algorithm
→ chứng minh algorithm phù hợp assumptions
```

Xem tiếp: [BFS & DFS](./01_graph_traversal_bfs_dfs.md), [Shortest Paths](./02_shortest_paths.md), [DAG/SCC](./04_dag_topological_sort_and_scc.md), [Network Flow](./08_network_flow_and_matching.md).