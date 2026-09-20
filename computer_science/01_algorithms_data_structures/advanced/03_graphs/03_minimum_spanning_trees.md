# Minimum Spanning Tree
**Cây khung nhỏ nhất / Minimum Spanning Tree (MST) / 최소 신장 트리**

Minimum Spanning Tree giải bài toán: **kết nối toàn bộ vertices của một undirected weighted graph với tổng edge cost nhỏ nhất**. Nó không tối ưu đường đi giữa từng cặp nodes như shortest path; nó tối ưu **tổng chi phí của toàn bộ hạ tầng kết nối**.

Nếu graph có `V` vertices và connected, một spanning tree có đúng `V-1` edges. MST chọn spanning tree rẻ nhất trong tất cả các spanning trees khả dĩ.

## 1. Tại sao lời giải tối ưu phải là tree?

Nếu một connected subgraph chứa cycle, bỏ một edge trên cycle vẫn giữ connected. Vì vậy khi mục tiêu chỉ là connectivity và ta không cần redundancy, cycle là dư thừa về số cạnh.

Mọi connected acyclic graph có `V-1` edges. Do đó search space tự nhiên của bài toán là tập tất cả spanning trees.

Nhưng cần nhớ: production network thường cần redundancy. MST cố tình bỏ redundancy để tối thiểu hóa total cost; nó không tối ưu fault tolerance.

## 2. MST khác Shortest Path Tree

Giả sử:

```text
A-B = 2
B-C = 2
A-C = 3
```

MST chọn `A-B` và `B-C`, total 4. Nhưng shortest path từ A tới C trong graph gốc là edge trực tiếp cost 3.

MST hỏi:

> “Bộ edges rẻ nhất để mọi vertex connected là gì?”

Shortest-path tree hỏi:

> “Từ một source, làm sao distance tới từng vertex là nhỏ nhất?”

Hai objective khác nhau nên không thể thay thế thuật toán cho nhau.

## 3. Cut Property — engine chứng minh của MST

Một **cut** chia vertices thành hai tập `S` và `V-S`. Edge có hai endpoint nằm khác phía gọi là crossing edge.

Cut property ở dạng thực dụng:

> Với một cut tôn trọng các edges đã chọn, một edge nhẹ nhất crossing cut là **safe**: tồn tại một MST chứa nó.

Proof intuition dùng exchange argument. Giả sử MST `T` không chứa light edge `e`. Thêm `e` vào `T` tạo cycle. Cycle phải chứa một crossing edge `f` khác. Vì `w(e) <= w(f)`, thay `f` bằng `e` không tăng total cost. Ta thu được MST khác chứa `e`.

Kruskal và Prim chỉ là hai cách khác nhau để liên tục tìm safe edge bằng cut property.

## 4. Cycle Property

Trong một cycle, nếu edge `e` nặng hơn nghiêm ngặt mọi edge khác trên cycle, `e` không thể nằm trong bất kỳ MST nào.

Nếu một MST chứa `e`, thêm một edge nhẹ hơn khác của cycle tạo cycle rồi bỏ `e`, total giảm — mâu thuẫn tối ưu.

Cut property giúp **thêm** edge. Cycle property giúp **loại** edge.

## 5. Kruskal: grow một forest

Kruskal sort edges tăng dần theo weight. Mỗi lần gặp edge `(u,v)`, nếu `u` và `v` ở hai components khác nhau, ta chọn edge và merge components.

```text
sort edges by weight
for edge in sorted order:
    if find(u) != find(v):
        choose edge
        union(u,v)
```

DSU trả lời connectivity nhanh; proof optimality vẫn đến từ cut property.

### Java sketch

```java
record Edge(int u, int v, long w) {}

edges.sort(Comparator.comparingLong(Edge::w));
DSU dsu = new DSU(n);
long total = 0;
int used = 0;

for (Edge e : edges) {
    if (dsu.union(e.u(), e.v())) {
        total += e.w();
        used++;
        if (used == n - 1) break;
    }
}
```

Complexity:

\[
O(E\log E)+O(E\alpha(V))=O(E\log E)
\]

Sorting thường chi phối.

## 6. Minimum Spanning Forest

Nếu graph disconnected, không có spanning tree toàn graph. Kruskal vẫn tạo MST riêng cho từng connected component, gọi là **minimum spanning forest**.

API cần phân biệt:

```text
result is forest
vs
input required connected graph but was not connected
```

`used == V-1` là postcondition cho connected graph.

## 7. Prim: grow một tree qua frontier

Prim giữ set `S` các vertices đã vào MST. Mỗi bước chọn edge nhẹ nhất crossing từ `S` ra ngoài.

Đây chính là cut `(S, V-S)`, nên lightest crossing edge safe.

### Lazy Prim

Push outgoing edges vào heap. Khi pop nếu endpoint ngoài đã visited thì dùng, nếu stale thì skip.

```text
visit start
push outgoing edges
while heap not empty:
    pop cheapest edge
    if destination already in tree: continue
    choose edge
    visit destination
    push its outgoing edges
```

Simple, dễ implement, chấp nhận duplicates/stale entries.

### Eager Prim

Giữ `key[v]` = cheapest edge hiện biết nối `v` vào tree. Khi thấy edge nhẹ hơn, update key/parent. Indexed heap/decrease-key cho implementation gọn về state, nhưng standard priority queue không hỗ trợ decrease-key trực tiếp nên có thể dùng lazy duplicates.

## 8. Prim và Dijkstra giống code nhưng khác invariant

Dijkstra priority:

```text
best path distance từ source tới v
```

Prim priority:

```text
cheapest single edge nối v vào current tree
```

Dijkstra relax:

\[
dist[u]+w(u,v)
\]

Prim chỉ compare:

\[
w(u,v)
\]

Nếu copy code mà không hiểu key semantics, bug rất dễ xuất hiện.

## 9. Chọn Kruskal hay Prim theo representation

Kruskal tự nhiên khi:

```text
đã có edge list
sparse graph
cần sort/scan edges toàn cục
```

Prim tự nhiên khi:

```text
đã có adjacency list/matrix
muốn grow từ vertex
```

Dense graph có thể dùng Prim `O(V²)` với adjacency matrix mà không cần heap; heap overhead không phải lúc nào cũng thắng.

Algorithm selection phải xét graph density và representation, không chỉ một dòng Big-O.

## 10. Negative weights không gây vấn đề như shortest path

MST tree không có cycle. Negative edge chỉ đơn giản là edge rất hấp dẫn về cost và sẽ được chọn nếu không phá tree condition.

Không có khái niệm negative cycle làm objective xuống vô hạn vì spanning tree luôn có đúng `V-1` edges.

## 11. Unique MST và ties

Nếu mọi edge weights distinct, MST unique.

Nếu có ties, nhiều MST khác nhau có thể cùng total weight. Test không nên bắt exact edge list trừ khi tie-breaking được cố ý cố định.

Một edge là **critical** nếu xuất hiện trong mọi MST; **optional/pseudo-critical** nếu có thể xuất hiện trong một số MST; và **never-MST** nếu không thể xuất hiện.

Cut/cycle properties là nền cho classification này.

## 12. Edge bắt buộc: unique light edge của một cut

Nếu edge `e` là **unique** lightest edge crossing một cut, mọi MST phải chứa `e`.

Lý do: nếu MST không chứa `e`, exchange bằng `e` giảm cost nghiêm ngặt.

Đây là proof mạnh hơn “safe”: safe nói có một MST chứa edge; unique-light nói mọi MST chứa edge.

## 13. Edge bị cấm: unique heaviest trên cycle

Nếu `e` là unique heaviest trên một cycle, không MST nào chứa `e`. Nếu chứa, thay nó bằng edge nhẹ hơn trên cycle làm total giảm.

Hai criteria này rất hữu ích trong sensitivity analysis.

## 14. Bottleneck view

MST cũng là một **minimum bottleneck spanning tree**: weight lớn nhất trong tree là nhỏ nhất có thể theo bottleneck objective thích hợp.

Kruskal cho intuition rõ. Khi tăng threshold `T` và cho phép tất cả edges có weight `<=T`, threshold nhỏ nhất làm graph connected chính là bottleneck optimum.

Connection này biến nhiều bài threshold-connectivity thành Kruskal/DSU problems.

## 15. Maximum Spanning Tree

Đổi objective thành maximize total weight, Kruskal sort giảm dần hoặc đảo comparator. Logic cut/cycle tương tự theo chiều ngược.

Ứng dụng có thể là maximize affinity/reliability score trong một formulation phù hợp.

## 16. Single-Linkage Clustering

Xây MST trên points theo distance, rồi remove `k-1` edges lớn nhất. Ta được `k` connected clusters.

MST giữ các cheapest links cần cho connectivity; các edges lớn trong MST thường đại diện gaps giữa groups.

Đây là connection giữa graph theory và hierarchical clustering.

## 17. Euclidean MST và không materialize complete graph

Với `n` points, complete geometric graph có `Θ(n²)` edges. Chạy Kruskal trên tất cả edges có thể quá lớn.

Trong plane, Euclidean MST là subgraph của Delaunay triangulation, nên geometric structure có thể giảm candidate edges trước khi chạy MST.

Bài học rộng hơn:

> Đôi khi complexity bottleneck là **xây graph**, không phải graph algorithm sau đó.

## 18. Second-Best MST

Lấy MST `T`. Mỗi non-tree edge `(u,v,w)` khi thêm vào `T` tạo đúng một cycle. Để trở lại tree, phải bỏ một edge trên path `u-v` trong `T`.

Candidate tốt nhất cho edge mới thường bỏ edge lớn nhất trên path:

\[
newCost = mstCost + w - maxEdgeOnPath(u,v)
\]

Nếu preprocess binary lifting/LCA để query max edge path `O(log V)`, có thể xét mọi non-tree edge hiệu quả.

Đây là connection giữa MST và tree path queries.

## 19. Replacement Edge và sensitivity

Nếu một MST edge bị xóa hoặc tăng weight, component tree bị split thành hai phía. Edge ngoài MST rẻ nhất crossing cut đó là replacement candidate.

Nếu nhiều updates xảy ra, recompute từ đầu có thể đắt; dynamic MST structures quản lý replacement edges phức tạp hơn.

Static sensitivity analysis vẫn có thể dùng cut/cycle + preprocessing để trả lời “nếu edge này đổi cost thì MST thay đổi thế nào?”.

## 20. Dynamic MST khó vì local update có effect toàn cục

Một edge insertion có thể tạo cycle với path trong MST. Nếu edge mới nhẹ hơn maximum edge trên path, ta swap chúng.

Một tree-edge deletion tạo cut và cần tìm cheapest non-tree edge nối lại hai component.

Hai primitives:

```text
max edge on tree path
minimum replacement edge crossing cut
```

là trung tâm của dynamic MST, dẫn tới dynamic trees như Link-Cut Tree trong advanced settings.

## 21. Reverse-Delete Algorithm

Một cách nhìn đối xứng với Kruskal:

1. sort edges giảm dần;
2. thử delete edge;
3. nếu graph vẫn connected, giữ edge bị xóa;
4. nếu disconnect, phục hồi.

Cycle property giải thích correctness. Naive connectivity check làm implementation chậm, nhưng algorithm rất hữu ích về mặt conceptual: Kruskal “thêm safe edges”, reverse-delete “xóa unnecessary heavy edges”.

## 22. MST và Matroid intuition

Spanning forests của graph tạo một cấu trúc gọi là **graphic matroid**. Greedy chọn edges theo weight hoạt động vì independent sets của matroid có exchange property mạnh.

Không cần học matroid theory để code Kruskal, nhưng nó giải thích vì sao greedy “sort rồi lấy nếu không tạo cycle” đúng ở đây trong khi nhiều bài khác greedy tương tự lại sai.

Greedy correctness không đến từ sorting; nó đến từ structure của feasible sets.

## 23. Directed Graph là problem khác

Standard MST áp dụng undirected graph. Directed analogue là **minimum spanning arborescence** rooted tại một vertex, giải bằng Chu–Liu/Edmonds-type algorithms.

Không thể chỉ chạy Kruskal trên directed edges rồi bỏ orientation.

## 24. Multigraph và parallel edges

Kruskal xử lý parallel edges tự nhiên; edge rẻ hơn giữa cùng endpoints thường được xét trước. Self-loop luôn tạo cycle với chính vertex và không thể giúp connect component khác, nên bị bỏ.

Implementation nên giữ edge IDs nếu cần output exact edge identity.

## 25. Overflow và comparator correctness

Total weight có thể vượt `int`. Dùng `long`/64-bit khi constraints yêu cầu.

Comparator không nên:

```java
return a.w - b.w;
```

nếu overflow có thể xảy ra. Dùng `Long.compare`/`Comparator.comparingLong`.

C cũng nên tránh subtraction comparator với signed overflow.

## 26. Verification của MST result

Một output MST cần:

```text
V-1 edges
connected
acyclic
tổng weight đúng
```

Nhưng ba structural properties đầu chỉ chứng minh spanning tree, chưa chứng minh minimum.

Để verify optimality, có property mạnh:

> Với mọi non-tree edge `(u,v,w)`, maximum edge weight trên path `u-v` trong MST không được lớn hơn `w`.

Nếu có tree edge trên path nặng hơn `w`, swap sẽ tạo spanning tree nhẹ hơn.

Property này cho phép validator độc lập mạnh hơn chỉ so output structure.

## 27. Differential Testing

Trên random graph nhỏ:

- chạy Kruskal;
- chạy Prim;
- so total cost;
- với graph rất nhỏ, brute-force enumerate spanning trees làm oracle.

Test cases nên có:

```text
1 vertex
2 vertices
path
cycle
complete graph nhỏ
negative weights
equal weights
parallel edges
disconnected graph
very large weights
```

## 28. MST trong database/network/system design

MST có thể model:

```text
minimum cable/road/fiber cost
minimum set of pairwise links để bootstrap connectivity
clustering backbone
minimum connection graph trong layout/design
```

Nhưng thực tế thường thêm constraints:

```text
capacity
redundancy
hop count
latency
geography
fault domains
```

Khi đó problem có thể không còn là pure MST. DSA model phải khớp requirement, không ép business problem vào thuật toán quen thuộc.

## Mental Model

> MST là bài toán **mua connectivity với total edge cost nhỏ nhất**. Cut property nói cạnh nào safe để thêm; cycle property nói cạnh nào safe để loại. Kruskal và Prim chỉ là hai operational views của cùng optimality structure.

Khi gặp bài liên quan “connect tất cả với chi phí tổng nhỏ nhất”, hãy kiểm tra: graph có undirected không, có cần redundancy không, có thêm constraints không. Nếu objective đúng là pure connectivity cost, MST là abstraction rất mạnh.

Xem thêm: [Union-Find](./05_union_find.md), [Tree Foundations](../02_trees/00_tree_foundations.md), [Greedy Algorithms](../04_algorithmic_paradigms/04_greedy_algorithms.md).