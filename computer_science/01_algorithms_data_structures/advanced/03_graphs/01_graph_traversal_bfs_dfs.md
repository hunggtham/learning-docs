# BFS và DFS
**đồ thị Traversal / 그래프 순회**

Traversal trả lời câu hỏi nền tảng nhất của đồ thị: bắt đầu từ một trạng thái (state), ta có thể reach những trạng thái nào và theo thứ tự nào? Hai chiến lược kinh điển là **tìm kiếm theo chiều rộng (BFS / 너비 우선 탐색)** và **tìm kiếm theo chiều sâu (DFS / 깊이 우선 탐색)**.

Cả hai thường có complexity `O(V+E)` trên danh sách kề. Khác biệt lớn không nằm ở Big-O mà nằm ở **frontier chính sách**:

```text
BFS: frontier theo FIFO queue -> mở rộng theo layer/distance
DFS: frontier theo stack      -> đi sâu theo branch rồi quay lại
```

Chính thứ tự tìm kiếm này quyết định loại theorem/bất biến (invariant) nào ta có thể khai thác.

## BFS như shortest-path theo số cạnh

Nếu mọi cạnh có cùng chi phí, BFS từ nguồn `s` khám phá các đỉnh theo nondecreasing khoảng cách tính bằng số các cạnh.

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

Tại sao lần đầu tới `v` là đường đi ngắn nhất (shortest path)? Queue bảo đảm mọi nút khoảng cách `d` được xử lý trước các nút khoảng cách `d+1`. Nếu có một đường đi ngắn hơn tới `v`, predecessor của đường đi đó phải nằm ở tầng trước và đã khám phá `v` sớm hơn. Mâu thuẫn.

Đây là chứng minh dựa trên **tầng bất biến** chứ không phải vì queue “thường dùng như vậy”.

## BFS tầng structure

BFS tạo các lớp:

```text
L0 = {source}
L1 = nodes cách source 1 edge
L2 = nodes cách source 2 edges
...
```

Mọi cạnh trong undirected đồ thị không trọng số chỉ nối các đỉnh có BFS tầng chênh lệch tối đa 1.

tầng view hữu ích cho kiểm tra hai phía, đường đi ngắn nhất reconstruction, tầng aggregation và reasoning về sự lan truyền theo lớp sóng.

## nút cha cây và đường đi reconstruction

Khi lần đầu khám phá `v` từ `u`, lưu:

```text
parent[v] = u
```

ta tạo BFS cây.

Reconstruct đường đi:

```java
List<Integer> path = new ArrayList<>();
for (int v = target; v != -1; v = parent[v]) {
    path.add(v);
}
Collections.reverse(path);
```

Nếu đích unreachable, cần check `dist[target] == -1` trước.

nút cha siêu dữ liệu biến answer từ “khoảng cách là 7” thành actual route.

## Multi-source BFS

Nếu có nhiều sources cùng khoảng cách 0, đưa vào hàng đợi tất cả ngay từ đầu:

```text
for each source s:
    dist[s] = 0
    enqueue(s)
```

BFS sau đó trả khoảng cách tới **nguồn gần nhất**.

các ứng dụng:

```text
nearest hospital/exit
fire/infection spread từ nhiều origins
distance tới nearest zero trong matrix
Voronoi-like partition trên unweighted graph
```

Không cần thuật toán mới; chỉ thay initial frontier.

## Multi-target / early exit

Nếu chỉ cần đường đi tới một đích, BFS có thể dừng khi đích được dequeued hoặc ngay khi được khám phá tùy siêu dữ liệu cần thiết.

Nhưng nếu cần all các khoảng cách hoặc các tính chất toàn thành phần, early exit sẽ bỏ incomplete thông tin.

Optimization phải khớp required đầu ra.

## Bidirectional BFS

Nếu đồ thị unweighted, hệ số phân nhánh lớn và biết cả nguồn lẫn đích, có thể BFS từ hai phía cho tới khi frontiers gặp nhau.

Nếu hệ số phân nhánh khoảng `b` và shortest khoảng cách `d`, một phía có thể explore cỡ `b^d`, còn bidirectional search gần `2*b^(d/2)` trong idealized tree-like space.

cách triển khai cần:

```text
dist/visited từ source
dist/visited từ target
expand frontier nhỏ hơn khi có thể
phát hiện node/edge nơi hai search regions giao nhau
```

Không phải đồ thị nào cũng được speedup giống nhau, nhưng mental mô hình là giảm search độ sâu mỗi phía.

## BFS trên grid

Grid 4-direction chỉ là đồ thị ẩn:

```text
vertex = cell
edge = move hợp lệ sang neighbor
```

Không cần xây dựng danh sách kề. Generate các đỉnh kề on demand:

```java
int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
```

đã thăm trạng thái có thể encode bằng mảng 2D. Nếu trạng thái còn các khóa, direction, remaining breaks hoặc mode, đã thăm dimension phải mở rộng tương ứng.

## BFS và 0–1 BFS

BFS đúng cho equal-weight các cạnh. Nếu các trọng số chỉ `0` hoặc `1`, standard BFS không đủ nhưng heap Dijkstra hơi thừa.

**0–1 BFS** dùng deque:

```text
weight 0 -> push front
weight 1 -> push back
```

để duy trì khoảng cách order, đạt `O(V+E)`.

Đây là example cho việc frontier cấu trúc dữ liệu encode mô hình chi phí.

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

## DFS cây và forest

Trên connected đồ thị, DFS từ nguồn tạo một DFS cây. Trên đồ thị không liên thông, loop qua all các đỉnh tạo **DFS forest**.

```java
for (int u = 0; u < n; u++) {
    if (!seen[u]) {
        dfs(u, -1);
        components++;
    }
}
```

Mỗi nút gốc tương ứng một thành phần liên thông trong đồ thị vô hướng (undirected graph).

## Directed phát hiện chu trình bằng color các trạng thái

Boolean `seen` không đủ để phân biệt cạnh tới tổ tiên đang active và cạnh tới nút đã hoàn thành.

Dùng ba các trạng thái:

```text
0 = unvisited
1 = visiting / active in recursion stack
2 = finished
```

Nếu từ `u` có cạnh tới `v` với trạng thái `1`, đó là back cạnh vào active tổ tiên → directed chu trình.

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

trạng thái `finished` quan trọng vì cạnh tới một nút đã hoàn thành không chứng minh chu trình qua hiện tại recursion chain.

## Undirected phát hiện chu trình

Trong đồ thị vô hướng, cạnh trở lại nút cha là cách biểu diễn (representation) của chính cạnh ta vừa đi xuống, không phải chu trình.

Basic DFS:

```text
if neighbor not visited:
    dfs(neighbor, u)
else if neighbor != parent:
    cycle exists
```

Nhưng multigraph cần cạnh id thay vì chỉ `neighbor != parent`, vì các cạnh song song giữa cùng endpoints có ngữ nghĩa (semantics) khác.

## Discovery và thời điểm kết thúc

DFS có hai thời điểm tự nhiên:

```text
tin[u]  = lúc enter u
tout[u] = lúc finish toàn subtree DFS của u
```

quan hệ tổ tiên trong DFS cây có thể kiểm tra qua sự lồng nhau của khoảng:

```text
u ancestor của v nếu
tin[u] <= tin[v] && tout[v] <= tout[u]
```

Timestamps/low-link các giá trị là nền tảng cho bridges, các điểm khớp, SCC và topological reasoning.

## cạnh classification trong directed DFS

các cạnh có thể được nhìn như:

```text
tree edge    -> discover node mới
back edge    -> tới active ancestor
forward edge -> tới descendant đã discover
cross edge   -> giữa branches/subtrees khác
```

Không phải mọi thuật toán cần classification đầy đủ, nhưng distinction giúp hiểu tại sao directed phát hiện chu trình dùng back cạnh.

## thứ tự tô-pô từ thời điểm kết thúc

Trong DAG, khi DFS hoàn tất nút `u`, mọi hậu duệ có thể đi tới từ `u` đã được hoàn tất trước. Thêm `u` vào danh sách lúc rời nút rồi đảo danh sách sẽ tạo thứ tự tô-pô.

Nếu có back cạnh/chu trình, thứ tự tô-pô không tồn tại.

Do đó “reverse postorder” không phải trick; nó xuất phát từ dependency finish bất biến.

## Iterative DFS và continuation trạng thái

Cách đơn giản iterative DFS:

```java
stack.push(source);
while (!stack.isEmpty()) {
    int u = stack.pop();
    ...
}
```

mô phỏng preorder khá dễ. Nhưng nếu cần postorder/finish sự kiện, mỗi khung ngăn xếp phải nhớ progress trong danh sách kề hoặc dùng enter/exit markers.

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

Điều này cho thấy hàm đệ quy frame thật ra chứa `u`, cục bộ variables và vị trí loop hiện tại.

## Recursion độ sâu

đồ thị dạng chain với hàng trăm nghìn các nút có thể tràn số ngăn xếp lời gọi.

C, Java và JavaScript đều có practical giới hạn đệ quy khác nhau. Không nên dựa vào tối ưu lời gọi đuôi portable.

Nếu đầu vào độ sâu không controlled, iterative DFS là safer lựa chọn kỹ thuật.

## đã thăm: mark khi push hay khi pop?

Với BFS, thường mark đã thăm **khi đưa vào hàng đợi**, không phải khi lấy khỏi hàng đợi. Nếu đợi tới lấy khỏi hàng đợi, cùng nút có thể được đưa vào hàng đợi nhiều lần từ nhiều predecessors, làm queue phình lớn.

DFS iterative cũng thường mark khi push/khám phá tùy ngữ nghĩa.

quy tắc phải nhất quán với bất biến “mỗi trạng thái được scheduled bao nhiêu lần?”.

## đồ thị trạng thái và đã thăm khóa

đã thăm phải match trạng thái identity.

Nếu trạng thái là:

```text
(node, fuel)
```

thì `seen[node]` là sai; cần `seen[node][fuel]` hoặc canonical khóa tương đương.

Nếu hai histories dẫn tới cùng future-equivalent trạng thái, đã thăm có thể merge chúng. Đây là cùng concept với DP memoization.

## BFS/DFS trên đồ thị ẩn

Puzzle, word phép biến đổi, các tổ hợp khóa, scheduling các trạng thái có thể không hiện thực hóa danh sách kề.

Một hàm:

```text
neighbors(state)
```

generate transitions khi cần.

Complexity khi đó nên đo theo số có thể tới các trạng thái và generated transitions, không nhất thiết theo một pre-existing `V,E` literal.

## Flood fill

Flood fill là BFS/DFS trên grid thành phần. Điểm đáng học không phải thuật toán riêng mà là ánh xạ:

```text
cell = vertex
adjacent same-color/passable cells = edges
```

Once mô hình đúng, connected-component toolkit áp dụng trực tiếp.

## Bipartite check bằng BFS/DFS coloring

đồ thị vô hướng bipartite iff có thể 2-color các đỉnh sao cho mọi cạnh nối khác màu.

BFS:

```text
color source = 0
neighbor = 1 - color[u]
conflict nếu edge nối cùng màu
```

Odd chu trình là obstruction cho bipartiteness.

Đây là example traversal + small siêu dữ liệu giải structural tính chất.

## thành phần siêu dữ liệu

Traversal có thể aggregate nhiều thứ trong cùng pass:

```text
component size
sum/min/max value
hasCycle
bounding box trong grid
edge count
```

Nếu thành phần undirected có `V_c` các đỉnh và `E_c` các cạnh, cây thành phần thỏa `E_c = V_c - 1`; thêm cạnh có thể tạo chu trình.

## Complexity thật sự

Với danh sách kề:

\[
O(V+E)
\]

vì mỗi đỉnh đã thăm một số lần constant và mỗi adjacency mục scanned một lần.

Nhưng constants phụ thuộc cách biểu diễn. Object-heavy đồ thị có các lần trượt bộ nhớ đệm/GC; CSR có sequential tính cục bộ (locality) tốt hơn. DFS recursion còn có call overhead.

Big-O giống nhau không nghĩa môi trường chạy (runtime) giống nhau.

## bộ nhớ complexity

BFS frontier có thể chứa cả một tầng lớn, worst `O(V)`.

DFS stack độ sâu có thể `O(V)` trên chain, nhưng trên balanced/deep-narrow đồ thị thường nhỏ hơn BFS frontier.

Vì vậy BFS vs DFS đôi khi được chọn vì bộ nhớ shape chứ không chỉ ngữ nghĩa.

## Những hiểu lầm phổ biến

“BFS luôn nhanh hơn DFS vì tìm gần trước” là sai. Cả hai `O(V+E)`; goal quyết định phép duyệt phù hợp.

“DFS recursive luôn dùng ít bộ nhớ” sai; chuỗi rất sâu có stack `O(V)` và có thể crash.

“đã thăm là boolean theo đỉnh” sai khi trạng thái có thêm dimensions.

“Lần đầu thấy nút trong đồ thị có trọng số là shortest” chỉ đúng với BFS equal-weight setting, không với arbitrary positive các trọng số.

“Undirected chu trình = gặp đã thăm nút” sai vì nút cha cạnh luôn quay về đã thăm nút cha.

## kiểm thử traversal

Ngoài examples, test structural các tính chất:

```text
BFS dist[source] == 0
mọi discovered edge thỏa dist[v] <= dist[u]+1 trong unweighted graph
parent chain của reachable node dẫn về source
DFS visits exactly component vertices
no node scheduled repeatedly ngoài design
component count đúng reference model
```

ngẫu nhiên small các đồ thị có thể so BFS các khoảng cách với Floyd-Warshall tham chiếu để differential test.

## Khi chọn BFS, DFS hay priority-based search?

Một useful decision mô hình:

```text
reachable/component only      -> BFS hoặc DFS
minimum number of edges       -> BFS
0/1 weights                   -> 0-1 BFS
nonnegative general weights   -> Dijkstra
structural nesting/postorder  -> DFS
all possible branches         -> DFS/backtracking
near-vs-deep exploration      -> frontier policy quyết định
```

Traversal family thực chất khác nhau ở cách chọn **next frontier trạng thái**.

## Mô hình tư duy

> BFS và DFS không phải hai mẫu mã để học thuộc. Chúng là hai cách tổ chức **biên tìm kiếm (frontier)**. BFS bảo toàn thứ tự theo tầng hoặc khoảng cách; DFS bảo toàn cấu trúc lời gọi và nhánh lồng nhau. Khi hiểu bất biến của frontier, ta có thể suy ra BFS đa nguồn, BFS hai chiều, phát hiện chu trình, thứ tự tô-pô, SCC, cầu và nhiều thuật toán khác.

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