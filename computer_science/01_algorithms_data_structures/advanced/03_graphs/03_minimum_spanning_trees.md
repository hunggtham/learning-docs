# Minimum Spanning Tree
**Cây khung nhỏ nhất / Minimum Spanning Tree (MST) / 최소 신장 트리**

Minimum Spanning Tree giải một objective rất khác shortest path. Shortest path cố tối ưu đường đi giữa một source và các destinations. MST cố chọn một tập edges có tổng cost nhỏ nhất nhưng vẫn kết nối toàn bộ vertices.

Một **spanning tree** của connected undirected graph phải chứa mọi vertex, connected, không cycle và vì thế có đúng `V-1` edges. Một **Minimum Spanning Tree** là spanning tree có tổng trọng số nhỏ nhất trong tất cả spanning trees có thể có.

## 1. Tại sao “tree” xuất hiện?

Nếu một connected subgraph chứa cycle, ta có thể bỏ một edge trên cycle mà graph vẫn connected. Nếu mục tiêu chỉ là kết nối và mọi edge có nonnegative/ordinary cost, việc giữ một cycle thường là dư thừa đối với spanning-tree objective.

Một connected acyclic graph trên `V` vertices luôn có `V-1` edges. Vì vậy MST tìm đúng lượng connectivity tối thiểu về edge count, rồi tối ưu tổng weight trong không gian các spanning trees đó.

## 2. MST không phải shortest-path tree

Giả sử ba vertices A, B, C có edges:

```text
A-B = 2
B-C = 2
A-C = 3
```

MST chọn A-B và B-C, total 4. Nhưng shortest path từ A tới C trong graph gốc là direct edge cost 3, còn path trong MST cost 4.

MST tối ưu **tổng infrastructure cost**, không đảm bảo shortest route giữa từng pair.

Đây là distinction quan trọng trong network design: xây network rẻ nhất và routing nhanh nhất là hai objectives khác nhau.

## 3. Cut Property

Một **cut** chia vertices thành hai tập `S` và `V-S`. Edge crossing cut có một endpoint mỗi phía.

Cut property phát biểu theo dạng an toàn: một light edge có weight nhỏ nhất crossing một cut phù hợp với partial MST có thể được chọn như một **safe edge** cho một MST.

Intuition: giả sử một MST khác không chứa edge nhẹ `e`. Vì tree phải kết nối hai phía, nó chứa một crossing edge khác `f`. Thêm `e` tạo cycle; cycle có `f`. Nếu `w(e) <= w(f)`, thay `f` bằng `e` không tăng total cost. Vì vậy tồn tại một MST chứa `e`.

Đây là proof engine chung cho Kruskal và Prim.

## 4. Cycle Property

Góc nhìn đối ngược: trong một cycle, nếu có một edge nặng hơn nghiêm ngặt mọi edge còn lại, edge đó không cần thuộc bất kỳ MST nào.

Nếu spanning tree chứa edge nặng đó, thêm một edge nhẹ hơn từ cùng cycle tạo cycle; bỏ edge nặng giữ connectivity nhưng giảm cost.

Cut property nói edge nào **safe để thêm**. Cycle property nói edge nào **safe để loại**.

Hai properties giúp reasoning MST vượt khỏi việc học thuộc thuật toán.

## 5. Kruskal's Algorithm

Kruskal sort tất cả edges tăng dần theo weight. Sau đó xét từng edge; nếu hai endpoints đang ở hai components khác nhau, edge được chọn và hai components được merge.

```text
sort edges by weight
for each edge (u,v,w):
    if find(u) != find(v):
        take edge
        union(u,v)
```

DSU/Union-Find trả lời nhanh câu hỏi “u và v đã connected bằng những edge đã chọn chưa?”. Nếu đã connected, thêm edge sẽ tạo cycle nên bỏ qua.

## 6. Tại sao Kruskal đúng?

Tại thời điểm xét edge `e=(u,v)` nối hai components khác nhau, các components hiện tại tạo một cut giữa component chứa u và phần còn lại liên quan. Vì edges được xét tăng dần, `e` là một trong những lightest candidates có thể nối các components đó theo argument chuẩn.

Cut property cho phép chọn `e` an toàn.

DSU không chứng minh optimality; DSU chỉ hiện thực kiểm tra connectivity/cycle nhanh. Greedy proof đến từ cut property.

## 7. Complexity của Kruskal

Sorting edges chi phối:

\[
O(E\log E)
\]

DSU operations gần constant amortized với path compression + union by rank/size:

\[
O(E\alpha(V))
\]

nên tổng thường viết `O(E log E)`.

Vì `E` tối đa khoảng `V^2`, `log E = O(log V)`, nên đôi khi thấy `O(E log V)` trong simplified discussion.

## 8. Kruskal — Java sketch

```java
record Edge(int u, int v, long w) {}

edges.sort(Comparator.comparingLong(Edge::w));
DSU dsu = new DSU(n);
long total = 0L;
int used = 0;

for (Edge e : edges) {
    if (dsu.union(e.u(), e.v())) {
        total += e.w();
        used++;
        if (used == n - 1) break;
    }
}

if (used != n - 1) {
    // graph disconnected: không có spanning tree toàn graph
}
```

`long` thường an toàn hơn `int` cho total weight nếu edges/vertex count lớn.

## 9. Minimum Spanning Forest

Nếu graph disconnected, không tồn tại spanning tree cho toàn graph.

Kruskal vẫn chọn MST riêng cho mỗi connected component, tạo **Minimum Spanning Forest**.

Do đó `used == V-1` chỉ đúng nếu graph connected. Production/API nên phân biệt “forest result” và “error/no global MST”.

## 10. Prim's Algorithm

Prim xây một tree tăng dần từ một start vertex. Giữ set `S` các vertices đã vào tree. Mỗi bước chọn edge nhẹ nhất crossing từ `S` sang vertex ngoài `S`.

Priority queue quản frontier candidate edges hoặc best key mỗi vertex.

Cut `(S, V-S)` thay đổi sau mỗi step. Lightest crossing edge là safe theo cut property.

## 11. Lazy Prim

Một implementation đơn giản push mọi outgoing edge từ vertex mới vào heap. Khi pop edge, nếu destination đã visited thì skip stale edge.

Pseudo:

```text
visit start
push outgoing edges
while heap not empty:
    e = pop min
    if target already in tree: continue
    take e
    visit target
    push outgoing edges from target
```

Heap có thể chứa nhiều stale entries nhưng implementation rất straightforward.

Với adjacency list + binary heap, complexity thường:

\[
O(E\log E)
\]

hoặc được diễn đạt gần `O(E log V)` tùy variant/analysis.

## 12. Eager Prim

Eager version giữ cho mỗi outside vertex `v` best known crossing edge weight `key[v]`, tương tự Dijkstra giữ best distance.

Nếu edge `(u,v,w)` có `w < key[v]`, update key và parent.

Với decrease-key heap chuẩn có thể phân tích `O(E log V)`. Nếu standard PriorityQueue không hỗ trợ decrease-key, có thể push duplicate entries và skip stale state giống Dijkstra.

## 13. Prim vs Dijkstra: giống implementation, khác invariant

Cả hai có thể dùng min-heap và adjacency list, nhưng key có nghĩa khác.

Dijkstra key:

```text
best distance từ source tới v
```

Prim key:

```text
cheapest single edge nối v vào current tree
```

Dijkstra relax bằng:

```text
dist[u] + w(u,v)
```

Prim compare trực tiếp:

```text
w(u,v)
```

Nhìn code giống nhau nhưng objective/proof khác nhau.

## 14. Kruskal vs Prim: chọn theo graph representation

Kruskal tự nhiên khi đã có edge list hoặc graph sparse; sort edges rồi DSU.

Prim tự nhiên khi có adjacency lists và muốn grow từ a vertex. Với dense graph và adjacency matrix, simple `O(V^2)` Prim không dùng heap đôi khi rất hợp lý và thậm chí practical hơn heap overhead.

Không nên chọn algorithm chỉ vì một asymptotic expression; representation và density matters.

## 15. Unique MST

Nếu mọi edge weights khác nhau, MST là unique.

Nếu ties tồn tại, có thể có nhiều MST khác nhau cùng total weight.

Algorithm có thể trả bất kỳ MST valid nào. Tests không nên hard-code exact edge set nếu input cho phép multiple MSTs, trừ khi comparator/tie policy cố định và test đúng implementation detail.

## 16. Khi nào một edge bắt buộc hoặc có thể thuộc MST?

Cut/cycle properties giúp reasoning.

Nếu một edge là unique lightest crossing một cut, nó phải thuộc mọi MST.

Nếu một edge là unique heaviest trên một cycle, nó không thuộc bất kỳ MST nào.

Với ties, classification trở nên tinh tế hơn: edge có thể nằm trong một số MST nhưng không tất cả.

Những questions này xuất hiện trong sensitivity analysis và bài “critical/pseudo-critical edges”.

## 17. Negative edge weights có vấn đề không?

MST algorithms vẫn hoạt động với negative weights. Objective chỉ là tổng weight của tree; không có issue kiểu negative cycle của shortest paths vì tree không chứa cycle.

Kruskal sẽ đơn giản chọn negative cheap edges sớm nếu chúng không tạo cycle.

Đây là thêm một distinction với Dijkstra.

## 18. Maximum Spanning Tree

Nếu muốn spanning tree có tổng weight lớn nhất, ta có thể sort edges giảm dần trong Kruskal hoặc đảo comparator trong Prim-style approach.

Properties tương tự nhưng “lightest” đổi thành “heaviest” theo objective.

Ứng dụng có thể là maximize reliability/capacity score trong một số formulations.

## 19. Bottleneck Property

Một MST cũng là một **minimum bottleneck spanning tree**: nó minimize weight của heaviest edge theo một sense thích hợp, dù minimum bottleneck tree không nhất thiết unique hay luôn là MST theo total weight.

Kruskal intuition rất rõ: threshold weight nhỏ nhất tại đó graph trở nên connected chính là bottleneck value tối ưu.

Connection này hữu ích trong network threshold/connectivity problems.

## 20. MST và clustering

Single-linkage clustering có thể liên hệ MST. Xây MST trên points với edge weights là distances, rồi remove `k-1` edges lớn nhất để tạo `k` clusters.

Reasoning: MST giữ cheapest connectivity giữa points; cutting largest bridges tách structure theo gaps lớn.

Đây là một connection giữa graph algorithms và unsupervised clustering.

## 21. Euclidean MST

Nếu graph là complete graph của `n` points trong plane với Euclidean distances, explicit `O(n^2)` edges có thể quá lớn.

Geometric structure cho phép giảm candidates; Euclidean MST là subgraph của Delaunay triangulation. Ta có thể compute geometric graph sparse hơn rồi run MST.

Bài học: đôi khi bottleneck không nằm ở MST algorithm mà ở việc materialize graph.

## 22. Second-Best MST

Một bài nâng cao hỏi spanning tree có total weight nhỏ thứ hai.

Một cách: lấy MST `T`. Với mỗi non-tree edge `(u,v,w)`, thêm edge tạo một cycle. Để trở lại tree, phải remove một edge trên path `u-v` trong MST. Best alternative cho edge đó thường remove maximum-weight edge trên path.

Nếu preprocess LCA/binary lifting để query max edge on path nhanh, có thể tìm candidate second-best hiệu quả.

Connection này gắn MST với tree path queries.

## 23. Dynamic MST intuition

Nếu graph thay đổi edges/weights online, recompute MST từ đầu mỗi update có thể đắt. Dynamic MST là advanced topic dùng sophisticated dynamic trees/cut replacement reasoning.

Điều đáng nhớ là MST invariant toàn cục bị ảnh hưởng bởi local edge update thông qua cycles/cuts. Đây là lý do dynamic version khó hơn static Kruskal/Prim rất nhiều.

## 24. MST trong infrastructure design

Classic interpretation là nối cities bằng roads/cables với tổng build cost nhỏ nhất.

Nhưng production network thường còn constraints về redundancy. MST chỉ có one path giữa any two vertices, nên mất một tree edge disconnects network. Một system cần fault tolerance thường không thể chỉ deploy MST; phải thêm redundant links.

MST tối ưu cost dưới connectivity minimal, không tối ưu reliability.

## 25. Testing MST

Với connected graph, result phải có `V-1` edges, connected và acyclic.

Total weight có thể cross-check giữa Kruskal và Prim trên random graphs nhỏ.

Với brute-force rất nhỏ, enumerate spanning trees để verify minimum total.

Tests cần include disconnected graphs, equal weights, negative weights, parallel edges và one-vertex graph.

## 26. Common mistakes

Một lỗi là áp dụng MST cho directed graph mà không nhận ra standard MST là undirected. Directed analogue là minimum spanning arborescence/Edmonds' algorithm, problem khác.

Lỗi khác là nhầm MST với shortest-path tree.

Trong Kruskal, nếu comparator `int` dùng subtraction `a.w - b.w`, overflow có thể làm sort sai; dùng safe compare.

Trong Prim lazy, phải skip vertices/edges đã vào tree để tránh cycle/duplicate count.

## Mental Model

> MST là bài toán **mua connectivity toàn cục với tổng cost nhỏ nhất**. Cut property giải thích edge nào an toàn để thêm; cycle property giải thích edge nào an toàn để loại.

Kruskal nhìn graph từ ngoài vào bằng cách merge components theo edge weight. Prim nhìn từ một connected region và mở rộng frontier. Cả hai đúng vì cùng khai thác một structural theorem, không phải vì greedy luôn đúng nói chung.

Xem thêm: [Union-Find](./05_union_find.md), [Shortest Paths](./02_shortest_paths.md), [Greedy Algorithms](../04_algorithmic_paradigms/04_greedy_algorithms.md).