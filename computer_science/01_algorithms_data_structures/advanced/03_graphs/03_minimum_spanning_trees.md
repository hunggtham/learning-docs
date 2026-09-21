# cây khung nhỏ nhất
**Cây khung nhỏ nhất / cây khung nhỏ nhất (MST) / 최소 신장 트리**

cây khung nhỏ nhất giải bài toán: **kết nối toàn bộ các đỉnh của một undirected đồ thị có trọng số với tổng cạnh chi phí nhỏ nhất**. Nó không tối ưu đường đi giữa từng cặp các nút như đường đi ngắn nhất (shortest path); nó tối ưu **tổng chi phí của toàn bộ hạ tầng kết nối**.

Nếu đồ thị có `V` các đỉnh và connected, một spanning cây có đúng `V-1` các cạnh. MST chọn spanning cây rẻ nhất trong tất cả các spanning các cây khả dĩ.

## 1. Tại sao lời giải tối ưu phải là cây?

Nếu một connected subgraph chứa chu trình, bỏ một cạnh trên chu trình vẫn giữ connected. Vì vậy khi mục tiêu chỉ là connectivity và ta không cần redundancy, chu trình là dư thừa về số cạnh.

Mọi connected acyclic đồ thị có `V-1` các cạnh. Do đó không gian tìm kiếm tự nhiên của bài toán là tập tất cả spanning các cây.

Nhưng cần nhớ: hệ thống thực tế mạng thường cần redundancy. MST cố tình bỏ redundancy để tối thiểu hóa total chi phí; nó không tối ưu fault tolerance.

## 2. MST khác đường đi ngắn nhất cây

Giả sử:

```text
A-B = 2
B-C = 2
A-C = 3
```

MST chọn `A-B` và `B-C`, total 4. Nhưng đường đi ngắn nhất từ A tới C trong đồ thị gốc là cạnh trực tiếp chi phí 3.

MST hỏi:

> “Bộ các cạnh rẻ nhất để mọi đỉnh connected là gì?”

cây đường đi ngắn nhất hỏi:

> “Từ một nguồn, làm sao khoảng cách tới từng đỉnh là nhỏ nhất?”

Hai objective khác nhau nên không thể thay thế thuật toán cho nhau.

## 3. Cut tính chất — engine chứng minh của MST

Một **cut** chia các đỉnh thành hai tập `S` và `V-S`. cạnh có hai endpoint nằm khác phía gọi là crossing cạnh.

Cut tính chất ở dạng thực dụng:

> Với một cut tôn trọng các cạnh đã chọn, một cạnh nhẹ nhất crossing cut là **an toàn**: tồn tại một MST chứa nó.

trực giác chứng minh dùng exchange argument. Giả sử MST `T` không chứa light cạnh `e`. Thêm `e` vào `T` tạo chu trình. chu trình phải chứa một crossing cạnh `f` khác. Vì `w(e) <= w(f)`, thay `f` bằng `e` không tăng total chi phí. Ta thu được MST khác chứa `e`.

Kruskal và Prim chỉ là hai cách khác nhau để liên tục tìm an toàn cạnh bằng cut tính chất.

## 4. chu trình tính chất

Trong một chu trình, nếu cạnh `e` nặng hơn nghiêm ngặt mọi cạnh khác trên chu trình, `e` không thể nằm trong bất kỳ MST nào.

Nếu một MST chứa `e`, thêm một cạnh nhẹ hơn khác của chu trình tạo chu trình rồi bỏ `e`, total giảm — mâu thuẫn tối ưu.

Cut tính chất giúp **thêm** cạnh. chu trình tính chất giúp **loại** cạnh.

## 5. Kruskal: grow một forest

Kruskal sort các cạnh tăng dần theo trọng số. Mỗi lần gặp cạnh `(u,v)`, nếu `u` và `v` ở hai các thành phần khác nhau, ta chọn cạnh và merge các thành phần.

```text
sort edges by weight
for edge in sorted order:
    if find(u) != find(v):
        choose edge
        union(u,v)
```

DSU trả lời connectivity nhanh; chứng minh optimality vẫn đến từ cut tính chất.

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

Nếu đồ thị disconnected, không có spanning cây toàn đồ thị. Kruskal vẫn tạo MST riêng cho từng thành phần liên thông, gọi là **minimum spanning forest**.

API cần phân biệt:

```text
result is forest
vs
input required connected graph but was not connected
```

`used == V-1` là điều kiện sau cho connected đồ thị.

## 7. Prim: grow một cây qua frontier

Prim giữ set `S` các đỉnh đã vào MST. Mỗi bước chọn cạnh nhẹ nhất crossing từ `S` ra ngoài.

Đây chính là cut `(S, V-S)`, nên lightest crossing cạnh an toàn.

### Lazy Prim

Push outgoing các cạnh vào heap. Khi pop nếu endpoint ngoài đã đã thăm thì dùng, nếu stale thì skip.

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

đơn giản, dễ implement, chấp nhận các phần tử trùng/stale các mục.

### Eager Prim

Giữ `key[v]` = cheapest cạnh hiện biết nối `v` vào cây. Khi thấy cạnh nhẹ hơn, cập nhật khóa/nút cha. Indexed heap/decrease-key cho cách triển khai gọn về trạng thái (state), nhưng standard hàng đợi ưu tiên không hỗ trợ decrease-key trực tiếp nên có thể dùng lazy các phần tử trùng.

## 8. Prim và Dijkstra giống code nhưng khác bất biến (invariant)

Dijkstra độ ưu tiên:

```text
best path distance từ source tới v
```

Prim độ ưu tiên:

```text
cheapest single edge nối v vào current tree
```

Dijkstra relax:

\[
dist[u]+w(u,v)
\]

Prim chỉ so sánh:

\[
w(u,v)
\]

Nếu copy code mà không hiểu khóa ngữ nghĩa (semantics), bug rất dễ xuất hiện.

## 9. Chọn Kruskal hay Prim theo cách biểu diễn (representation)

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

đồ thị dày có thể dùng Prim `O(V²)` với ma trận kề mà không cần heap; heap overhead không phải lúc nào cũng thắng.

thuật toán selection phải xét đồ thị density và cách biểu diễn, không chỉ một dòng Big-O.

## 10. Negative các trọng số không gây vấn đề như đường đi ngắn nhất

MST cây không có chu trình. Negative cạnh chỉ đơn giản là cạnh rất hấp dẫn về chi phí và sẽ được chọn nếu không phá cây điều kiện.

Không có khái niệm negative chu trình làm objective xuống vô hạn vì spanning cây luôn có đúng `V-1` các cạnh.

## 11. Unique MST và ties

Nếu mọi cạnh các trọng số distinct, MST unique.

Nếu có ties, nhiều MST khác nhau có thể cùng total trọng số. Test không nên bắt chính xác danh sách cạnh trừ khi quy tắc phân xử khi bằng nhau được cố ý cố định.

Một cạnh là **critical** nếu xuất hiện trong mọi MST; **optional/pseudo-critical** nếu có thể xuất hiện trong một số MST; và **never-MST** nếu không thể xuất hiện.

Cut/chu trình các tính chất là nền cho classification này.

## 12. cạnh bắt buộc: unique light cạnh của một cut

Nếu cạnh `e` là **unique** lightest cạnh crossing một cut, mọi MST phải chứa `e`.

Lý do: nếu MST không chứa `e`, exchange bằng `e` giảm chi phí nghiêm ngặt.

Đây là chứng minh mạnh hơn “an toàn”: an toàn nói có một MST chứa cạnh; unique-light nói mọi MST chứa cạnh.

## 13. cạnh bị cấm: unique heaviest trên chu trình

Nếu `e` là unique heaviest trên một chu trình, không MST nào chứa `e`. Nếu chứa, thay nó bằng cạnh nhẹ hơn trên chu trình làm total giảm.

Hai criteria này rất hữu ích trong sensitivity analysis.

## 14. Bottleneck view

MST cũng là một **minimum bottleneck spanning cây**: trọng số lớn nhất trong cây là nhỏ nhất có thể theo bottleneck objective thích hợp.

Kruskal cho intuition rõ. Khi tăng threshold `T` và cho phép tất cả các cạnh có trọng số `<=T`, threshold nhỏ nhất làm đồ thị connected chính là bottleneck phương án tối ưu.

Connection này biến nhiều bài threshold-connectivity thành Kruskal/DSU problems.

## 15. Maximum Spanning cây

Nếu mục tiêu chuyển thành tối đa hóa tổng trọng số, Kruskal có thể sắp xếp giảm dần hoặc đảo bộ so sánh. Lập luận dựa trên lát cắt và chu trình được áp dụng theo chiều ngược lại.

Ứng dụng có thể là maximize affinity/reliability score trong một formulation phù hợp.

## 16. Single-Linkage Clustering

Xây MST trên points theo khoảng cách, rồi remove `k-1` các cạnh lớn nhất. Ta được `k` connected clusters.

MST giữ các liên kết rẻ nhất cần cho connectivity; các cạnh lớn trong MST thường đại diện gaps giữa groups.

Đây là connection giữa đồ thị theory và hierarchical clustering.

## 17. Euclidean MST và không materialize đồ thị đầy đủ

Với `n` points, complete geometric đồ thị có `Θ(n²)` các cạnh. Chạy Kruskal trên tất cả các cạnh có thể quá lớn.

Trong plane, Euclidean MST là subgraph của Delaunay triangulation, nên cấu trúc hình học có thể giảm ứng viên các cạnh trước khi chạy MST.

Bài học rộng hơn:

> Đôi khi complexity bottleneck là **xây đồ thị**, không phải thuật toán đồ thị sau đó.

## 18. Second-Best MST

Lấy MST `T`. Mỗi non-tree cạnh `(u,v,w)` khi thêm vào `T` tạo đúng một chu trình. Để trở lại cây, phải bỏ một cạnh trên đường đi `u-v` trong `T`.

ứng viên tốt nhất cho cạnh mới thường bỏ cạnh lớn nhất trên đường đi:

\[
newCost = mstCost + w - maxEdgeOnPath(u,v)
\]

Nếu preprocess nhảy nhị phân/LCA để truy vấn max cạnh đường đi `O(log V)`, có thể xét mọi non-tree cạnh hiệu quả.

Đây là connection giữa MST và cây đường đi các truy vấn.

## 19. Replacement cạnh và sensitivity

Nếu một MST cạnh bị xóa hoặc tăng trọng số, thành phần cây bị split thành hai phía. cạnh ngoài MST rẻ nhất crossing cut đó là replacement ứng viên.

Nếu nhiều các cập nhật xảy ra, recompute từ đầu có thể đắt; động MST structures quản lý replacement các cạnh phức tạp hơn.

tĩnh sensitivity analysis vẫn có thể dùng cut/chu trình + tiền xử lý để trả lời “nếu cạnh này đổi chi phí thì MST thay đổi thế nào?”.

## 20. động MST khó vì cục bộ cập nhật có effect toàn cục

Một cạnh insertion có thể tạo chu trình với đường đi trong MST. Nếu cạnh mới nhẹ hơn maximum cạnh trên đường đi, ta swap chúng.

Một tree-edge deletion tạo cut và cần tìm cheapest non-tree cạnh nối lại hai thành phần.

Hai primitives:

```text
max edge on tree path
minimum replacement edge crossing cut
```

là trung tâm của động MST, dẫn tới động các cây như Link-Cut cây trong advanced settings.

## 21. Reverse-Delete thuật toán

Một cách nhìn đối xứng với Kruskal:

1. sort các cạnh giảm dần;
2. thử delete cạnh;
3. nếu đồ thị vẫn connected, giữ cạnh bị xóa;
4. nếu disconnect, phục hồi.

chu trình tính chất giải thích tính đúng đắn. Cách đơn giản kiểm tra liên thông làm cách triển khai chậm, nhưng thuật toán rất hữu ích về mặt conceptual: Kruskal “thêm an toàn các cạnh”, reverse-delete “xóa unnecessary heavy các cạnh”.

## 22. MST và Matroid intuition

Spanning forests của đồ thị tạo một cấu trúc gọi là **graphic matroid**. Greedy chọn các cạnh theo trọng số hoạt động vì independent sets của matroid có exchange tính chất mạnh.

Không cần học matroid theory để code Kruskal, nhưng nó giải thích vì sao greedy “sort rồi lấy nếu không tạo chu trình” đúng ở đây trong khi nhiều bài khác greedy tương tự lại sai.

Greedy tính đúng đắn không đến từ sorting; nó đến từ structure của feasible sets.

## 23. đồ thị có hướng là problem khác

Chuẩn MST áp dụng đồ thị vô hướng (undirected graph). Directed analogue là **cây phân nhánh có hướng nhỏ nhất** rooted tại một đỉnh, giải bằng Chu–Liu/Edmonds-type các thuật toán.

Không thể chỉ chạy Kruskal trên directed các cạnh rồi bỏ orientation.

## 24. Multigraph và các cạnh song song

Kruskal xử lý các cạnh song song tự nhiên; cạnh rẻ hơn giữa cùng endpoints thường được xét trước. Self-loop luôn tạo chu trình với chính đỉnh và không thể giúp connect thành phần khác, nên bị bỏ.

cách triển khai nên giữ cạnh IDs nếu cần đầu ra chính xác cạnh identity.

## 25. tràn số và comparator tính đúng đắn

Total trọng số có thể vượt `int`. Dùng `long`/64-bit khi các ràng buộc yêu cầu.

Comparator không nên:

```java
return a.w - b.w;
```

nếu tràn số có thể xảy ra. Dùng `Long.compare`/`Comparator.comparingLong`.

C cũng nên tránh subtraction comparator với signed tràn số.

## 26. Verification của MST kết quả

Một đầu ra MST cần:

```text
V-1 edges
connected
acyclic
tổng weight đúng
```

Nhưng ba structural các tính chất đầu chỉ chứng minh spanning cây, chưa chứng minh minimum.

Để verify optimality, có tính chất mạnh:

> Với mọi non-tree cạnh `(u,v,w)`, maximum cạnh trọng số trên đường đi `u-v` trong MST không được lớn hơn `w`.

Nếu có cây cạnh trên đường đi nặng hơn `w`, swap sẽ tạo spanning cây nhẹ hơn.

tính chất này cho phép bộ xác minh độc lập mạnh hơn chỉ so đầu ra structure.

## 27. Differential kiểm thử

Trên ngẫu nhiên đồ thị nhỏ:

- chạy Kruskal;
- chạy Prim;
- so total chi phí;
- với đồ thị rất nhỏ, brute-force enumerate spanning các cây làm oracle.

các trường hợp kiểm thử nên có:

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

## 28. MST trong cơ sở dữ liệu/mạng/hệ thống design

MST có thể mô hình:

```text
minimum cable/road/fiber cost
minimum set of pairwise links để bootstrap connectivity
clustering backbone
minimum connection graph trong layout/design
```

Nhưng thực tế thường thêm các ràng buộc:

```text
capacity
redundancy
hop count
latency
geography
fault domains
```

Khi đó problem có thể không còn là pure MST. DSA mô hình phải khớp yêu cầu, không ép business problem vào thuật toán quen thuộc.

## Mô hình tư duy

> MST là bài toán **mua connectivity với total cạnh chi phí nhỏ nhất**. Cut tính chất nói cạnh nào an toàn để thêm; chu trình tính chất nói cạnh nào an toàn để loại. Kruskal và Prim chỉ là hai operational views của cùng optimality structure.

Khi gặp bài liên quan “connect tất cả với chi phí tổng nhỏ nhất”, hãy kiểm tra: đồ thị có undirected không, có cần redundancy không, có thêm các ràng buộc không. Nếu objective đúng là pure connectivity chi phí, MST là sự trừu tượng (abstraction) rất mạnh.

Xem thêm: [Union-Find](./05_union_find.md), [Tree Foundations](../02_trees/00_tree_foundations.md), [Greedy Algorithms](../04_algorithmic_paradigms/04_greedy_algorithms.md).