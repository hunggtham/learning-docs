# đồ thị: mô hình hóa và biểu diễn
**Đồ thị (Graph / 그래프)**

đồ thị là sự trừu tượng (abstraction) cho tình huống mà **mối quan hệ quan trọng ngang entity**. Người dùng và quan hệ bạn bè, thành phố và đường đi, gói phần mềm và quan hệ phụ thuộc, dịch vụ và lời gọi mạng, tài khoản ngân hàng và giao dịch, trang web và siêu liên kết, hay hàm và quan hệ lời gọi đều có thể được mô hình hóa bằng:

\[
G=(V,E)
\]

trong đó `V` là tập các đỉnh/các nút và `E` là tập các cạnh.

Điểm khó nhất của đồ thị problem thường không phải BFS hay Dijkstra. Phần khó là quyết định:

```text
một vertex đại diện cho cái gì?
một edge có nghĩa gì?
state nào cần được phân biệt?
weight/capacity/time có nằm trên edge hay node?
graph là directed, undirected, multigraph hay state graph?
```

Một thuật toán hoàn toàn đúng trên **mô hình sai** vẫn cho answer sai cho problem thật.

## Directed, undirected và weighted

**đồ thị vô hướng (undirected graph) / 무방향 그래프** dùng cạnh `u -- v` khi mối quan hệ đối xứng: road hai chiều, friendship, cable connection.

**đồ thị có hướng / 방향 그래프** dùng cạnh `u -> v` khi mối quan hệ có hướng: dependency, hyperlink, money transfer, call đồ thị.

**đồ thị có trọng số / 가중 그래프** gắn chi phí lên cạnh hoặc nút. trọng số có thể là khoảng cách, độ trễ (latency), price, risk, time, energy, xác suất transform hoặc capacity.

Không phải mọi trọng số đều dùng đường đi ngắn nhất (shortest path). Capacity dẫn tới flow; xác suất có thể cần log transform; exchange rate có thể dẫn tới negative-cycle/arbitrage reasoning.

## đơn giản đồ thị, multigraph và self-loop

Một **đơn giản đồ thị** không có các cạnh song song và thường không có self-loop. Nhưng nhiều domains thực tế cho phép cả hai.

các cạnh song song xuất hiện khi hai cities có nhiều flights khác nhau, hai services có nhiều channels hoặc đồ thị giữ các liên kết lịch sử.

Self-loop xuất hiện khi một trạng thái (state) có transition về chính nó hoặc data chứa explicit relation `(u,u)`.

Nếu thuật toán vô thức giả định đơn giản đồ thị, kết quả có thể sai. Bridge detection là ví dụ: hai các cạnh song song giữa cùng cặp các nút nghĩa là xóa một cạnh chưa chắc disconnect đồ thị. Vì vậy cạnh identity phải được giữ rõ.

## đường đi, walk, trail và chu trình

Một **walk** cho phép lặp các đỉnh/các cạnh. **Trail** thường không lặp cạnh. **đường đi** thường không lặp đỉnh trong định nghĩa graph-theory chuẩn. **chu trình** quay lại điểm bắt đầu.

Trong programming problems, từ “đường đi” đôi khi được dùng lỏng hơn. Khi chứng minh quan trọng, hãy xác định ngữ nghĩa (semantics) chính xác thay vì dựa vào wording.

đường đi ngắn nhất với non-negative các trọng số luôn có thể chọn một đơn giản đường đi optimal vì chu trình không giúp giảm chi phí. Nhưng với negative chu trình, objective có thể không còn finite minimum.

## Connectivity và reachability

Trong đồ thị vô hướng, **thành phần liên thông / 연결 요소** là maximal set các đỉnh nối được với nhau.

Trong đồ thị có hướng, reachability có hướng. thành phần liên thông mạnh yêu cầu reachability hai chiều giữa mọi cặp các nút trong thành phần.

Đây là lý do “thành phần” trong đồ thị có hướng không đơn giản là chạy BFS và gom tất cả các nút có thể tới từ nguồn.

## Degree

Undirected đỉnh có degree bằng số incident các cạnh, với self-loop convention cần chú ý.

đồ thị có hướng có:

```text
indegree  = số edges đi vào
outdegree = số edges đi ra
```

Degree không chỉ là siêu dữ liệu. Eulerian các điều kiện dùng parity/balance của degree; Kahn sắp xếp tô-pô dùng indegree; đồ thị sparsity thường liên quan average degree.

## ma trận kề

ma trận kề dùng `V x V` cells.

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

Nếu đồ thị có 1 triệu các đỉnh nhưng mỗi đỉnh chỉ vài các đỉnh kề, matrix là bất khả thi.

## danh sách kề

danh sách kề lưu các đỉnh kề theo từng đỉnh.

bộ nhớ:

\[
O(V+E)
\]

và iteration các đỉnh kề của `u` là `O(deg(u))`.

Java:

```java
List<List<Edge>> g = new ArrayList<>(n);
for (int i = 0; i < n; i++) g.add(new ArrayList<>());
```

JavaScript:

```js
const g = Array.from({ length: n }, () => []);
```

Undirected cạnh thường được lưu hai adjacency các mục. Nếu thuật toán cần biết hai các mục đó đại diện cùng vật lý cạnh, hãy gắn unique cạnh id.

## danh sách cạnh

danh sách cạnh chỉ lưu:

```text
(u, v, weight)
```

Nó phù hợp khi thuật toán xử lý các cạnh toàn cục hơn là các đỉnh kề từng đỉnh.

Kruskal MST là ví dụ điển hình:

```text
sort toàn bộ edges theo weight
scan edges
DSU quyết định edge có nối hai component khác nhau không
```

Không có cách biểu diễn (representation) “tốt nhất”; thao tác chính quyết định cách biểu diễn.

## CSR — Compressed Sparse Row

Danh sách kề dùng nhiều đối tượng thuận tiện khi lập trình nhưng tốn chi phí tham chiếu và cấp phát. Trong xử lý đồ thị hiệu năng cao, **CSR (Compressed Sparse Row)** lưu đồ thị bằng các mảng liên tiếp trong bộ nhớ.

Conceptually:

```text
offsets[u] .. offsets[u+1]-1
```

là segment trong `edges[]` chứa các đỉnh kề của `u`.

Ví dụ:

```text
offsets = [0, 2, 5, 5]
edges   = [1, 2, 0, 2, 3]
```

các đỉnh kề của nút 1 là `edges[2..4]`.

CSR giảm chi phí đối tượng trên mỗi nút, tăng tính cục bộ (locality) và rất phù hợp với đồ thị thưa tĩnh. Đánh đổi là thao tác chèn/xóa động khó hơn so với danh sách kề động.

## Adjacency map và sparse bên ngoài IDs

Nếu đỉnh IDs là strings hoặc sparse 64-bit IDs, có thể dùng ánh xạ:

```text
external id -> compact integer id
```

sau đó lưu đồ thị bằng các mảng trên gọn IDs.

Điều này thường tốt hơn `Map<String,List<String>>` ở đồ thị rất lớn vì các phép so sánh, hash, đối tượng cấp phát và bộ nhớ tính cục bộ đều cải thiện.

Đây là một mẫu hệ thống thực tế quan trọng: **normalize identity trước, optimize cách biểu diễn sau**.

## mô hình hóa đồ thị không gian trạng thái

Trong nhiều bài, nút không phải entity domain mà là **trạng thái / 상태**.

Ví dụ grid có khóa và door. trạng thái không thể chỉ là `(row,col)`; hai lần đứng cùng cell nhưng giữ key-mask khác nhau có tương lai khác nhau.

trạng thái đúng có thể là:

```text
(row, col, keysMask)
```

Nếu ta đã thăm theo `(row,col)` בלבד, thuật toán có thể loại sai một đường quay lại cell với nhiều các khóa hơn.

Ngược lại, trạng thái chứa quá nhiều lịch sử không ảnh hưởng tương lai sẽ làm đồ thị phình khổng lồ.

Một trạng thái tốt giữ đúng **future-relevant thông tin** — mental mô hình này giống quy hoạch động (dynamic programming).

## Product đồ thị

Khi problem có nhiều dimensions các ràng buộc, ta có thể tạo **product đồ thị**.

Ví dụ đường đi ngắn nhất với tối đa `K` coupons:

```text
state = (vertex, couponsUsed)
```

cạnh transition có thể:

```text
đi bình thường: (u,k) -> (v,k)
dùng coupon:     (u,k) -> (v,k+1)
```

đồ thị mới có khoảng `V*(K+1)` các trạng thái. Chuẩn shortest-path thuật toán giờ có thể chạy trên expanded không gian trạng thái.

Đây là cách biến “ràng buộc phức tạp” thành topology rõ ràng.

## đồ thị mở rộng theo thời gian

Scheduling, transport và temporal mạng có thể cần time trong trạng thái:

```text
(vertex, time)
```

Ví dụ train chỉ chạy ở departure times cụ thể. cạnh không chỉ nói “A nối B”; nó nói “từ A lúc t có thể tới B lúc t'”.

đồ thị mở rộng theo thời gian có thể lớn, nên đôi khi ta không materialize toàn bộ; generate transitions on demand.

## đồ thị ẩn

đồ thị không nhất thiết phải được xây dựng trước.

Word ladder:

```text
vertex = một word
edge = đổi đúng một ký tự
```

Thay vì tạo mọi pair các cạnh `O(n^2)`, ta có thể generate các đỉnh kề qua wildcard các ngăn băm hoặc dictionary tra cứu khi BFS cần.

Puzzle, game trạng thái và combinatorial search thường dùng implicit các đồ thị.

Mô hình tư duy:

> đồ thị là **relation**, không phải bắt buộc là `List<List<Integer>>`.

## Hypergraph và relation nhiều hơn hai endpoints

Chuẩn đồ thị cạnh nối hai các đỉnh. Nhưng một relation có thể liên quan nhiều entities cùng lúc, ví dụ một cơ sở dữ liệu transaction chạm nhiều accounts hoặc một ràng buộc chứa nhiều variables.

**Hypergraph** cho phép hyperedge nối nhiều các đỉnh. Trong cách triển khai, hyperedge thường được biến đổi thành bipartite incidence đồ thị hoặc phụ trợ nút để dùng các thuật toán chuẩn.

Biết mô hình này giúp tránh ép mọi problem về pairwise cạnh một cách sai nghĩa.

## Bipartite mô hình hóa

Nếu miền bài toán có hai loại thực thể rõ ràng — chẳng hạn công việc/người lao động, sinh viên/dự án hoặc người dùng/mục dữ liệu — đồ thị thường là đồ thị hai phía (bipartite graph).

Tách hai phía giúp nhận ra matching/flow structure thay vì tổng quát đồ thị search.

Ví dụ:

```text
Worker -> Job nếu worker có thể làm job
```

Maximum matching trả assignment tối đa không conflict.

## đồ thị và sparse matrix

ma trận kề chính là matrix cách biểu diễn của relation. Nhiều các thuật toán đồ thị có linear algebra interpretation.

lặp lại matrix multiplication liên quan đường đi counts/reachability. PageRank dùng transition matrix. đồ thị Neural mạng các tầng thường aggregate đỉnh kề features, tương đương sparse-matrix-like các thao tác.

CSR thực chất cũng là cách biểu diễn kinh điển của sparse matrix. đồ thị theory và linear algebra vì thế là hai góc nhìn của cùng structure.

## bộ nhớ chi phí không chỉ là O(V+E)

Hai adjacency lists đều là `O(V+E)` nhưng constants có thể khác hàng lần.

Java:

```text
ArrayList<ArrayList<EdgeObject>>
```

có phần đầu các đối tượng, các tham chiếu và đóng hộp nếu dùng wrapper types.

C các mảng có thể gọn hơn nhưng quyền sở hữu (ownership)/reallocation phức tạp hơn.

JavaScript các mảng/các đối tượng có động môi trường chạy (runtime) overhead.

Khi đồ thị có hàng chục triệu cạnh, số byte cần cho mỗi cạnh trở thành một chỉ số thiết kế quan trọng hàng đầu.

## cạnh direction lưu trữ

đồ thị có hướng lưu đúng direction.

đồ thị vô hướng thường lưu hai các mục:

```text
u -> v
v -> u
```

Nhưng các thuật toán như Euler/bridge cần tránh coi hai các mục là hai vật lý các cạnh khác nhau. Unique cạnh id hoặc paired reverse-index là mẫu tốt.

Flow các thuật toán cũng thường tạo explicit reverse residual cạnh, nhưng reverse cạnh ở đó có ngữ nghĩa khác: nó đại diện khả năng undo flow chứ không phải original undirected relation.

## đồ thị sự thay đổi dữ liệu

Nếu đồ thị tĩnh, CSR/sorted đỉnh kề các mảng rất tốt.

Nếu đồ thị động với nhiều thao tác chèn/xóa cạnh, cấu trúc biểu diễn phải hỗ trợ thay đổi dữ liệu hiệu quả, chẳng hạn tập/map băm theo từng nút, tập cân bằng hoặc cấu trúc đồ thị động chuyên biệt.

sự đánh đổi:

```text
static -> compact, cache-friendly, preprocess mạnh
dynamic -> flexible update, nhiều metadata/overhead hơn
```

Đây là cùng mẫu thấy ở bảng thưa (Sparse Table) vs cây đoạn (Segment Tree).

## Dense vs sparse

Một đồ thị có thể gọi là sparse khi `E` gần tuyến tính theo `V`, và dense khi `E` gần `V^2`.

cách biểu diễn và thuật toán thường thay đổi theo density.

Dijkstra ma trận kề có thể `O(V^2)` và đủ tốt cho đồ thị dày nhỏ. Heap + danh sách kề tốt hơn với đồ thị thưa lớn.

Floyd-Warshall `O(V^3)` đôi khi hợp đồ thị nhỏ cần all-pairs, dù asymptotic nhìn rất lớn.

## mô hình hóa failures phổ biến

### Gộp trạng thái quá mạnh

Việc chỉ đánh dấu đã thăm theo thành phố là chưa đủ nếu bài toán còn phụ thuộc vào số chặng đã dùng, lượng nhiên liệu, tập khóa đang có hoặc thời gian.

### trạng thái quá chi tiết

Lưu full đường đi trong trạng thái khi tương lai chỉ cần hiện tại đỉnh + small siêu dữ liệu. trạng thái explosion không cần thiết.

### Direction sai

Dependency `A depends on B` có thể encode `A->B` hoặc `B->A`; thuật toán topological scheduling phụ thuộc convention. Hãy định nghĩa rõ cạnh nghĩa gì.

### trọng số sai meaning

độ trễ đường đi có thể cộng; bandwidth đường đi bottleneck có thể dùng min; reliability có thể nhân probabilities. Không phải metric nào cũng là additive đường đi ngắn nhất.

### Không xác định đồ thị class

Parallel cạnh, self-loop, disconnected các thành phần, negative các trọng số, directed/undirected đều có thể làm các giả định của thuật toán sai.

## mô hình hóa checklist

Trước khi chọn thuật toán, viết rõ:

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

## Mô hình tư duy

> thuật toán đồ thị bắt đầu từ **trạng thái mô hình hóa**, không phải từ việc nhận diện tên thuật toán. đỉnh là một equivalence class của situations có cùng tương lai possibilities; cạnh là một allowed transition/relation. cách biểu diễn phải tối ưu cho thao tác chính: đỉnh kề traversal, cạnh tra cứu, toàn cục cạnh sort hay gọn quét.

Một đồ thị problem tốt thường được giải theo chuỗi xử lý:

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