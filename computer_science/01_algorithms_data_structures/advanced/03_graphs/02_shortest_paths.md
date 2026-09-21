# các đường đi ngắn nhất
**Đường đi ngắn nhất (Shortest Path / 최단 경로)**

“đường đi ngắn nhất (shortest path)” không phải tên của một thuật toán duy nhất. Nó là một họ bài toán, và lựa chọn thuật toán phụ thuộc trực tiếp vào **mô hình trọng số (weight model / 가중치 모델)** của đồ thị.

Cùng một đồ thị topology nhưng nếu các cạnh đều bằng nhau, chỉ có `0/1`, đều không âm, có số âm, hay đồ thị là DAG thì structure toán học khác nhau. Vì vậy trước khi nghĩ tới Dijkstra, câu hỏi đầu tiên phải là:

```text
Edge cost có dạng gì?
Graph directed hay undirected?
Có negative edge không?
Có negative cycle không?
Cần shortest path từ một source hay mọi cặp?
Graph sparse hay dense?
Có cần actual path hay chỉ distance?
```

## Mô hình tư duy

> Mọi shortest-path thuật toán đều cố cải thiện một **ước lượng khoảng cách** bằng relaxation. Khác nhau ở thứ tự relaxation và điều kiện nào cho phép xem một khoảng cách là đã “final”.

Với cạnh `u -> v` có trọng số `w`, relaxation kiểm tra:

\[
dist[v] > dist[u] + w
\]

Nếu đúng:

\[
dist[v] \leftarrow dist[u] + w
\]

Đây là primitive xuyên suốt BFS, Dijkstra, Bellman-Ford và DAG đường đi ngắn nhất.

## đồ thị không trọng số: BFS là shortest-path thuật toán

Nếu mọi cạnh có cùng chi phí, ví dụ mỗi bước tính 1, **tìm kiếm theo chiều rộng (BFS / 너비 우선 탐색)** đã đủ.

BFS xử lý đồ thị theo tầng:

```text
distance 0: source
distance 1: neighbors
distance 2: neighbors của layer trước chưa thăm
...
```

Khi một đỉnh lần đầu được khám phá, ta đã tìm được đường đi ít cạnh nhất tới nó, bởi vì queue đảm bảo mọi đường đi ngắn hơn đã được xử lý trước.

Complexity với danh sách kề:

\[
O(V+E)
\]

Đây là một insight quan trọng: Dijkstra trên đồ thị không trọng số vẫn đúng nếu coi mọi cạnh trọng số = 1, nhưng heap là overhead không cần thiết.

## 0–1 BFS: khi các trọng số chỉ là 0 hoặc 1

Nếu trọng số chỉ thuộc `{0,1}`, ta có thể dùng deque thay vì đống nhị phân.

Relax cạnh trọng số 0:

```text
push_front(v)
```

Relax cạnh trọng số 1:

```text
push_back(v)
```

Intuition là nút có khoảng cách không tăng phải được xử lý trước các nút làm khoảng cách tăng 1. Deque duy trì đúng ordering cần thiết mà không cần general-purpose hàng đợi ưu tiên.

Complexity:

\[
O(V+E)
\]

Ví dụ thực tế: chuyển trạng thái miễn phí hoặc trả phí 1 đơn vị; đi qua portal chi phí 0 nhưng bước thường chi phí 1; minimize số lần đổi mode.

## Dijkstra: non-negative các trọng số

**Dijkstra (다익스트라 알고리즘)** áp dụng khi mọi có thể tới cạnh trọng số không âm.

Ta giữ `dist[v]` là best khoảng cách hiện biết. hàng đợi ưu tiên chọn unsettled đỉnh có `dist` nhỏ nhất.

### bất biến (invariant) cốt lõi

Khi `u` là nút có tentative khoảng cách nhỏ nhất và mọi cạnh trọng số không âm, không thể có một đường đi đi qua một unsettled nút xa hơn rồi quay lại làm `u` rẻ hơn.

Giả sử có đường đi tốt hơn tới `u` đi qua một unsettled đỉnh `x`. Vì cạnh các trọng số không âm, prefix tới `x` không thể lớn hơn toàn đường đi tới `u`. Nhưng `u` đang là tentative nhỏ nhất trong frontier. Điều này dẫn tới contradiction với giả định có đường đi tốt hơn chưa được phát hiện.

Do đó khi pop một trạng thái (state) non-stale tốt nhất, khoảng cách đó có thể được xem là finalized.

### Java với stale-entry mẫu

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

Với danh sách kề + đống nhị phân, complexity thường viết:

\[
O((V+E)\log V)
\]

hoặc gần `O(E log V)` cho connected đồ thị thưa.

## Tại sao negative cạnh phá Dijkstra?

Giả sử:

```text
s -> a : 2
s -> b : 5
b -> a : -10
```

Dijkstra có thể finalize `a = 2` trước vì `2 < 5`. Nhưng đường đi `s -> b -> a` có chi phí `-5`, tốt hơn rất nhiều.

Vấn đề không phải cách triển khai. giả định “một nút tốt nhất hiện tại sẽ không bị cải thiện trong tương lai” đã sai vì negative cạnh có thể giảm chi phí sau khi đi qua một nút đang xa hơn.

Đây là lý do điều kiện “non-negative trọng số” là phần của tính đúng đắn chứng minh, không chỉ là recommendation hiệu năng.

## Bellman-Ford: relaxation theo số các cạnh

**Bellman-Ford (벨만-포드)** cho phép negative các cạnh.

Một shortest đơn giản đường đi không có lặp lại đỉnh có tối đa `V-1` các cạnh. Vì vậy nếu ta relax mọi cạnh `V-1` rounds, mọi đường đi ngắn nhất finite sẽ có đủ cơ hội propagate từ nguồn.

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

Chậm hơn Dijkstra nhưng support mô hình rộng hơn.

## Negative chu trình ngữ nghĩa (semantics)

Nếu round thứ `V` vẫn có relaxation trên đỉnh có thể tới từ nguồn, có một **negative chu trình (음수 사이클)** ảnh hưởng tới region đó.

Điều này không đơn giản nghĩa là “không có đường đi ngắn nhất ở toàn đồ thị”. Nếu chu trình không có thể tới từ nguồn, nó không ảnh hưởng single-source truy vấn. Nếu chu trình có thể tới nhưng đích không có thể tới từ chu trình, đích vẫn có thể có finite đường đi ngắn nhất.

Nếu đích có thể tới sau một negative chu trình, objective không có finite minimum: đi thêm vòng chu trình làm chi phí giảm vô hạn.

Mô hình tư duy đúng là:

```text
negative cycle reachable + can reach target
=> shortest distance tới target không bị chặn dưới
```

## SPFA: vì sao cần thận trọng

đường đi ngắn nhất Faster thuật toán dùng queue để chỉ relax các đỉnh có thay đổi, thường nhanh trên một số data. Nhưng trường hợp xấu nhất vẫn có thể rất tệ, gần `O(VE)` và còn có đối kháng các đầu vào.

Vì vậy không nên coi SPFA là “Bellman-Ford nhanh hơn” với bảo đảm tốt hơn. Dùng khi hiểu khối lượng công việc hoặc trong context mà empirical hành vi được chấp nhận.

## DAG đường đi ngắn nhất

Nếu đồ thị là **Directed Acyclic đồ thị (DAG / 방향 비순환 그래프)**, ta có thứ tự tô-pô. Mỗi cạnh luôn đi từ nút trước sang nút sau trong order.

Do đó chỉ cần relax mỗi cạnh một lần theo thứ tự tô-pô:

\[
O(V+E)
\]

Điểm đặc biệt: DAG đường đi ngắn nhất chấp nhận negative cạnh vì không có chu trình để quay lại phá ordering.

Đây là ví dụ điển hình cho việc topology mạnh hơn trọng số giả định. Khi đồ thị acyclic, dependency order loại nhu cầu lặp lại relaxation.

## All-pairs các đường đi ngắn nhất và Floyd-Warshall

Nếu cần đường đi ngắn nhất giữa mọi cặp các đỉnh và đồ thị đủ nhỏ/dense, **Floyd-Warshall (플로이드-워셜)** là một quy hoạch động (dynamic programming) rất trực tiếp.

Định nghĩa:

\[
d_k(i,j)
\]

là shortest khoảng cách từ `i` tới `j` khi chỉ được dùng các intermediate các đỉnh trong `{0,...,k}`.

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

bộ nhớ:

\[
O(V^2)
\]

Nó rất phù hợp khi `V` nhỏ và cần nhiều pair các truy vấn, đặc biệt đồ thị dày.

## Floyd-Warshall và negative các chu trình

Sau thuật toán, nếu:

\[
d[i][i] < 0
\]

thì có negative chu trình có thể tới từ `i` và quay về `i`.

Muốn biết pair `(s,t)` có đường đi ngắn nhất không hữu hạn, phải kiểm có đỉnh `k` sao cho:

```text
s reaches k
k lies on/reaches negative cycle
negative cycle region reaches t
```

Chỉ nhìn một diagonal âm mà tuyên bố mọi cặp không hợp lệ là sai.

## Johnson's thuật toán: all-pairs trên đồ thị thưa

Khi đồ thị sparse, `O(V^3)` có thể lãng phí. **Johnson's thuật toán** dùng Bellman-Ford để tìm potentials, reweight các cạnh thành non-negative mà bảo toàn shortest-path ordering, rồi chạy Dijkstra từ từng nguồn.

Ý tưởng reweight:

\[
w'(u,v)=w(u,v)+h(u)-h(v)
\]

Nếu `h` được chọn từ Bellman-Ford potentials, `w' >= 0`.

đường đi chi phí bị shift theo endpoints nhưng relative choice giữa các đường đi cùng nguồn/đích không đổi. Đây là một example đẹp của việc biến problem sang domain mà thuật toán mạnh hơn áp dụng được.

## đường đi reconstruction

khoảng cách giá trị thường chưa đủ. Muốn actual route, khi relaxation thành công:

```text
parent[v] = u
```

Sau thuật toán, backtrack từ đích tới nguồn.

```java
List<Integer> path = new ArrayList<>();
for (int v = target; v != -1; v = parent[v]) {
    path.add(v);
}
Collections.reverse(path);
```

Cần phân biệt `parent` cho cây đường đi ngắn nhất với đồ thị nút cha tổng quát. Nếu có nhiều các đường đi ngắn nhất cùng chi phí, quy tắc phân xử khi bằng nhau quyết định đường đi nào được lưu.

## Counting các đường đi ngắn nhất

Nếu cần số các đường đi ngắn nhất, có thể maintain `ways[v]` cùng `dist[v]`:

```text
new distance better:
    dist[v] = nd
    ways[v] = ways[u]

new distance equal:
    ways[v] += ways[u]
```

Tính đúng đắn còn phụ thuộc vào thứ tự xử lý và các chu trình trọng số 0. Nếu tồn tại chu trình chi phí 0, số hành trình ngắn nhất có thể là vô hạn. Miền bài toán phải nói rõ đang đếm đường đi đơn, hành trình (walk), hay đường đi trong DAG hoặc đồ thị có trọng số dương.

## Multi-source đường đi ngắn nhất

Nếu có nhiều sources và cần khoảng cách tới nguồn gần nhất, không nhất thiết chạy thuật toán nhiều lần.

Với đồ thị không trọng số, đưa vào hàng đợi tất cả sources với khoảng cách 0 rồi BFS một lần.

Với non-negative đồ thị có trọng số, push tất cả sources vào Dijkstra PQ với khoảng cách 0.

Mô hình tư duy: tạo một virtual super-source nối tới mọi nguồn bằng cạnh trọng số 0.

## Multi-target và early exit

Trong Dijkstra, nếu chỉ cần một đích, có thể dừng khi đích được pop với non-stale minimum khoảng cách, vì lúc đó nó đã finalized.

Không nên dừng ngay khi đích lần đầu được được khám phá/relaxed; tentative khoảng cách có thể còn được cải thiện trước khi đích trở thành min frontier.

## A*: đường đi ngắn nhất với heuristic

**A\*** ưu tiên:

\[
f(v)=g(v)+h(v)
\]

trong đó `g(v)` là chi phí từ nguồn, `h(v)` ước lượng chi phí còn lại tới đích.

Nếu heuristic **admissible** (`h(v)` không overestimate true remaining chi phí), A* có thể giữ optimality. Nếu heuristic còn consistent, xử lý hành vi gần Dijkstra với reweighted các độ ưu tiên và ít reopen hơn.

Dijkstra chính là A* với `h(v)=0`.

Trong routing/spatial search, heuristic tốt giúp bỏ rất nhiều vùng đồ thị không liên quan.

## Bidirectional search

Nếu nguồn và đích đã biết, có thể tìm kiếm từ hai phía và gặp nhau ở giữa. Với đồ thị không trọng số, BFS hai chiều có thể giảm mạnh kích thước biên tìm kiếm hiệu dụng từ khoảng `b^d` xuống gần `2b^{d/2}` trong mô hình phân nhánh lý tưởng.

Weighted bidirectional Dijkstra phức tạp hơn vì stopping điều kiện phải đảm bảo cận dưới hai frontier đã đủ lớn; không thể chỉ dừng ở lần đầu hai searches chạm nhau một cách ngây thơ.

## tràn số và infinity cách biểu diễn (representation)

Trong Java, nếu dùng:

```java
long INF = Long.MAX_VALUE;
```

rồi tính:

```java
INF + w
```

có thể tràn số thành số âm. Thực tế thường dùng `Long.MAX_VALUE / 4` hoặc guard:

```text
if dist[u] != INF before addition
```

Trong C, signed tràn số nguyên (integer overflow) có thể là undefined hành vi. Cần chọn type đủ rộng và kiểm ranh giới.

JavaScript `Number` biểu diễn integer chính xác tới:

\[
2^{53}-1
\]

Nếu đường đi sum có thể vượt vùng này, cân nhắc `BigInt` hoặc thay đổi mô hình dữ liệu.

## Floating-point các trọng số

Nếu các trọng số là `double`, equality test và stale check cần cẩn thận. Với floating-point, expression `curDist != dist[u]` có thể vẫn hoạt động nếu các giá trị được copy nguyên từ computed khoảng cách, nhưng các phép so sánh gần ranh giới có thể chịu rounding.

Nếu domain là tiền tệ hoặc fixed-scale chi phí, integer minor units thường an toàn hơn dấu phẩy động.

## Sparse vs đồ thị dày

danh sách kề phù hợp đồ thị thưa và Dijkstra/BFS thường chỉ iterate outgoing các cạnh thực sự tồn tại.

ma trận kề cho cạnh tra cứu `O(1)` nhưng iteration các đỉnh kề `O(V)`. Trên đồ thị dày, matrix-based các thuật toán có thể cạnh tranh vì tính cục bộ (locality) tốt và `E ≈ V^2` anyway.

Big-O phải gắn với cách biểu diễn.

## đường đi ngắn nhất cây không phải cây khung nhỏ nhất

Dijkstra từ nguồn tạo một cây đường đi ngắn nhất: đường đi từ nguồn tới mỗi đỉnh là shortest.

MST tối thiểu **tổng trọng số của toàn bộ cây**. Nó không đảm bảo đường đi từ nút gốc tới từng đỉnh là shortest.

Hai objectives khác nhau:

```text
Shortest-path tree -> tối ưu route từ source
MST                -> tối ưu total infrastructure cost
```

Đừng chọn thuật toán chỉ vì cả hai “trông như chọn cạnh nhỏ”.

## Decision table

| trọng số / structure | thuật toán tự nhiên |
|---|---|
| unweighted / equal trọng số | BFS |
| các trọng số 0 hoặc 1 | 0–1 BFS |
| non-negative các trọng số | Dijkstra |
| negative các cạnh, không biết chu trình | Bellman-Ford |
| DAG | topological relaxation |
| all-pairs, đồ thị nhỏ/dense | Floyd-Warshall |
| all-pairs, sparse, có negative các cạnh nhưng không negative chu trình | Johnson |
| spatial single-target + heuristic tốt | A* |

Bảng này không thay chứng minh. Nó chỉ nhắc điều kiện mô hình.

## Những hiểu lầm phổ biến

**“Dijkstra nhanh hơn Bellman-Ford nên cứ dùng Dijkstra.”** Sai nếu có negative cạnh. tính đúng đắn điều kiện quan trọng hơn speed.

**“BFS chỉ là traversal, không phải đường đi ngắn nhất.”** Với equal cạnh các chi phí, BFS chính là shortest-path thuật toán tối ưu.

**“Negative chu trình nghĩa là mọi đường đi ngắn nhất trong đồ thị đều không tồn tại.”** Không. Chỉ các source-target regions bị ảnh hưởng mới không có finite minimum.

**“Floyd-Warshall chỉ dùng cho positive các trọng số.”** Nó hỗ trợ negative các cạnh, miễn hiểu ngữ nghĩa negative chu trình.

**“Dijkstra dừng khi đích được nhìn thấy lần đầu.”** Không. Dừng khi đích được extract/finalize đúng điều kiện.

**“PriorityQueue phần tử trùng mục làm Dijkstra sai.”** Không nếu dùng stale-entry check. Nó là cách triển khai sự đánh đổi (trade-off) phổ biến.

## kiểm thử shortest-path cách triển khai

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

Một tính chất mạnh sau khi có final các khoảng cách là với mọi có thể tới cạnh `(u,v,w)`:

\[
dist[v] \le dist[u] + w
\]

Nếu nút cha đường đi được lưu, tổng trọng số trên nút cha chain phải bằng reported `dist[target]`.

Trên đồ thị nhỏ, có thể differential-test Dijkstra non-negative với Floyd-Warshall tham chiếu.

## Connection với các hệ thống thực tế

Routing, điều hướng bản đồ, dependency chi phí, mạng độ trễ (latency) planning, tìm đường cho AI trò chơi, logistics, tối ưu luồng công việc và xây dựng dependency đều có shortest-path variants.

Nhưng hệ thống thực tế thường thêm các ràng buộc: time-dependent các trọng số, turn penalties, multiple resources, capacity, stochastic các chi phí hoặc động đồ thị. Khi đó classical đường đi ngắn nhất có thể trở thành trạng thái-space đường đi ngắn nhất: mỗi “đỉnh” thực sự là `(location, time, fuel, mode, ...)`.

Đây là connection quan trọng với problem mô hình hóa: thuật toán có thể đúng nhưng trạng thái cách biểu diễn thiếu thông tin thì kết quả vẫn sai.

## Mô hình tư duy mở rộng

> đường đi ngắn nhất không bắt đầu từ tên thuật toán; nó bắt đầu từ việc xác định **chi phí algebra và ordering nào cho phép một ứng viên trở thành final**.

BFS dựa vào thứ tự theo tầng. 0–1 BFS dùng deque để duy trì hai mức chi phí cục bộ. Dijkstra dựa vào trọng số không âm. Bellman–Ford dựa vào giới hạn số cạnh của đường đi đơn. Thuật toán trên DAG dùng thứ tự phụ thuộc. Floyd–Warshall dùng quy hoạch động theo tập đỉnh trung gian được phép.

Nếu nhớ được điều kiện làm mỗi method đúng, bạn có thể chọn thuật toán từ bản chất bài toán thay vì từ mẫu memorization.