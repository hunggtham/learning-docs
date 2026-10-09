# các đường đi ngắn nhất

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **các đường đi ngắn nhất**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Mô hình tư duy** gom các mảnh thành mental model có thể mang sang nhánh khác; sau đó sang **đồ thị không trọng số: BFS là shortest-path thuật toán** để kiểm tra nhận định bằng tiêu chí hoặc phép thử. Mạch này nối shortest paths với BFS, Dijkstra, Bellman-Ford và heuristic, để chọn thuật toán theo trọng số và ràng buộc.

**Đường đi ngắn nhất (Shortest Path / 최단 경로)**

“đường đi ngắn nhất (shortest path)” không phải tên của một thuật toán duy nhất. Nó là một họ bài toán, và lựa chọn thuật toán phụ thuộc trực tiếp vào **mô hình trọng số (weight model / 가중치 모델)** của đồ thị.

Cùng một đồ thị topology nhưng nếu các cạnh đều bằng nhau, chỉ có `0/1`, đều không âm, có số âm, hay đồ thị là DAG thì cấu trúc (structure / 구조) toán học khác nhau. Vì vậy trước khi nghĩ tới Dijkstra, câu hỏi đầu tiên phải là:

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

Đây là thành phần nguyên thủy (primitive / 기본 요소) xuyên suốt BFS, Dijkstra, Bellman-Ford và DAG đường đi ngắn nhất.

> **Mạch nối:** Một mô hình shortest path chỉ có giá trị khi invariant của nó kiểm tra được trên dữ liệu cụ thể. Với đồ thị không trọng số, BFS cung cấp tiêu chí cơ bản; khi cạnh có hai mức chi phí, 0–1 BFS mở rộng cùng ý tưởng bằng deque.

## đồ thị không trọng số: BFS là shortest-path thuật toán

Nếu mọi cạnh có cùng chi phí, ví dụ mỗi bước tính 1, **tìm kiếm theo chiều rộng (BFS / 너비 우선 탐색)** đã đủ.

BFS xử lý đồ thị theo tầng:

```text
distance 0: source
distance 1: neighbors
distance 2: neighbors của layer trước chưa thăm
...
```

Khi một đỉnh lần đầu được khám phá, ta đã tìm được đường đi ít cạnh nhất tới nó, bởi vì hàng đợi (queue / 큐) đảm bảo mọi đường đi ngắn hơn đã được xử lý trước.

Độ phức tạp (complexity / 복잡도) với danh sách kề:

\[
O(V+E)
\]

Đây là một insight quan trọng: Dijkstra trên đồ thị không trọng số vẫn đúng nếu coi mọi cạnh trọng số = 1, nhưng vùng nhớ động (heap / 힙) là overhead không cần thiết.

> **Mạch nối:** 0–1 BFS khai thác miền trọng số rất hẹp để sắp xếp frontier hiệu quả. Khi trọng số mở rộng thành mọi giá trị không âm, Dijkstra thay deque bằng priority queue nhưng vẫn dựa trên relaxation và nhãn khoảng cách tốt nhất hiện tại.

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

Intuition là nút có khoảng cách không tăng phải được xử lý trước các nút làm khoảng cách tăng 1. Deque duy trì đúng thứ tự (ordering / 순서) cần thiết mà không cần general-purpose hàng đợi ưu tiên.

Độ phức tạp (complexity / 복잡도):

\[
O(V+E)
\]

Ví dụ thực tế: chuyển trạng thái miễn phí hoặc trả phí 1 đơn vị; đi qua portal chi phí 0 nhưng bước thường chi phí 1; minimize số lần đổi chế độ (mode / 모드).

> **Mạch nối:** Dijkstra chốt một đỉnh khi khóa của nó là nhỏ nhất nhờ mọi cạnh không âm. Chỉ cần xuất hiện cạnh âm, một đỉnh đã khóa có thể còn đường rẻ hơn về sau; đó là lý do cần phân tích riêng failure này.

## Dijkstra: non-negative các trọng số

**Dijkstra (다익스트라 알고리즘)** áp dụng khi mọi có thể tới cạnh trọng số không âm.

Ta giữ `dist[v]` là best khoảng cách hiện biết. hàng đợi ưu tiên chọn unsettled đỉnh có `dist` nhỏ nhất.

### Bất biến (invariant / 불변식) cốt lõi

Khi `u` là nút có tentative khoảng cách nhỏ nhất và mọi cạnh trọng số không âm, không thể có một đường đi đi qua một unsettled nút xa hơn rồi quay lại làm `u` rẻ hơn.

Giả sử có đường đi tốt hơn tới `u` đi qua một unsettled đỉnh `x`. Vì cạnh các trọng số không âm, prefix tới `x` không thể lớn hơn toàn đường đi tới `u`. Nhưng `u` đang là tentative nhỏ nhất trong frontier. Điều này dẫn tới contradiction với giả định có đường đi tốt hơn chưa được phát hiện.

Do đó khi pop một trạng thái (state / 상태) non-stale tốt nhất, khoảng cách đó có thể được xem là finalized.

### Java với stale-entry mẫu

Trước khi đọc đoạn triển khai, hãy giữ invariant và complexity mà thuật toán phải bảo toàn. Code bên dưới là một cách hiện thực hóa; cần đối chiếu output, ownership và edge case với mô hình vừa học.

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

Với danh sách kề + đống nhị phân, độ phức tạp (complexity / 복잡도) thường viết:

\[
O((V+E)\log V)
\]

hoặc gần `O(E log V)` cho connected đồ thị thưa.

> **Mạch nối:** Cạnh âm phá bất biến “đã chọn là tối ưu” của Dijkstra, nhưng không làm relaxation mất ý nghĩa. Bellman–Ford thay thứ tự ưu tiên bằng các lượt quét theo số cạnh để xử lý được trọng số âm.

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

> **Mạch nối:** Bellman–Ford cho phép một đường đi tốt dần theo số cạnh đã xét. Nếu sau đủ lượt vẫn còn relaxation, cần chuyển từ câu hỏi khoảng cách sang semantics của negative cycle và vùng đích bị ảnh hưởng.

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

Độ phức tạp (complexity / 복잡도):

\[
O(VE)
\]

Chậm hơn Dijkstra nhưng hỗ trợ (support / 지원) mô hình rộng hơn.

> **Mạch nối:** Negative cycle không đồng nghĩa mọi cặp source–target đều mất khoảng cách hữu hạn; chỉ các vùng reachable và chịu ảnh hưởng mới bị phá vỡ minimum. SPFA cố gắng lan truyền relaxation theo frontier, nhưng phải đánh giá thận trọng vì không có bảo đảm thời gian tốt trong trường hợp xấu.

## Negative chu trình ngữ nghĩa (semantics / 의미론)

Nếu round thứ `V` vẫn có relaxation trên đỉnh có thể tới từ nguồn, có một **negative chu trình (음수 사이클)** ảnh hưởng tới region đó.

Điều này không đơn giản nghĩa là “không có đường đi ngắn nhất ở toàn đồ thị”. Nếu chu trình không có thể tới từ nguồn, nó không ảnh hưởng single-source truy vấn. Nếu chu trình có thể tới nhưng đích không có thể tới từ chu trình, đích vẫn có thể có finite đường đi ngắn nhất.

Nếu đích có thể tới sau một negative chu trình, mục tiêu (objective / 목표) không có finite minimum: đi thêm vòng chu trình làm chi phí giảm vô hạn.

Mô hình tư duy đúng là:

```text
negative cycle reachable + can reach target
=> shortest distance tới target không bị chặn dưới
```

> **Mạch nối:** SPFA hữu ích trong một số dữ liệu nhưng không nên được xem là Bellman–Ford luôn nhanh hơn. Nếu topology có dạng DAG, thứ tự tô-pô loại bỏ hoàn toàn nhu cầu lặp relaxation.

## SPFA: vì sao cần thận trọng

đường đi ngắn nhất Faster thuật toán dùng hàng đợi (queue / 큐) để chỉ relax các đỉnh có thay đổi, thường nhanh trên một số dữ liệu (data / 데이터). Nhưng trường hợp xấu nhất vẫn có thể rất tệ, gần `O(VE)` và còn có đối kháng các đầu vào.

Vì vậy không nên coi SPFA là “Bellman-Ford nhanh hơn” với bảo đảm tốt hơn. Dùng khi hiểu khối lượng công việc hoặc trong ngữ cảnh (context / 맥락) mà empirical hành vi được chấp nhận.

> **Mạch nối:** Trên DAG, mỗi cạnh được relaxation đúng một lần theo thứ tự topo, kể cả khi trọng số âm. Khi mục tiêu chuyển từ một nguồn sang mọi cặp đỉnh, ta cần một mô hình all-pairs như Floyd–Warshall.

## DAG đường đi ngắn nhất

Nếu đồ thị là **Directed Acyclic đồ thị (DAG / 방향 비순환 그래프)**, ta có thứ tự tô-pô. Mỗi cạnh luôn đi từ nút trước sang nút sau trong thứ tự (order / 순서).

Do đó chỉ cần relax mỗi cạnh một lần theo thứ tự tô-pô:

\[
O(V+E)
\]

Điểm đặc biệt: DAG đường đi ngắn nhất chấp nhận negative cạnh vì không có chu trình để quay lại phá thứ tự (ordering / 순서).

Đây là ví dụ điển hình cho việc topology mạnh hơn trọng số giả định. Khi đồ thị acyclic, phụ thuộc (dependency / 의존성) thứ tự (order / 순서) loại nhu cầu lặp lại relaxation.

> **Mạch nối:** Floyd–Warshall cập nhật đáp án khi cho phép thêm từng đỉnh trung gian, nên không cần giả định DAG. Cùng recurrence đó cũng cung cấp dấu hiệu diagonal âm để nhận diện negative cycle.

## All-pairs các đường đi ngắn nhất và Floyd-Warshall

Nếu cần đường đi ngắn nhất giữa mọi cặp các đỉnh và đồ thị đủ nhỏ/dense, **Floyd-Warshall (플로이드-워셜)** là một quy hoạch động (dynamic programming) rất trực tiếp.

Định nghĩa:

\[
d_k(i,j)
\]

là shortest khoảng cách từ `i` tới `j` khi chỉ được dùng các intermediate các đỉnh trong `{0,...,k}`.

Chuyển tiếp (transition / 전이):

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

Thời gian (time / 시간):

\[
O(V^3)
\]

bộ nhớ:

\[
O(V^2)
\]

Nó rất phù hợp khi `V` nhỏ và cần nhiều pair các truy vấn, đặc biệt đồ thị dày.

> **Mạch nối:** Negative diagonal cho biết có chu trình âm, còn việc lan ảnh hưởng tới cặp nào vẫn cần xét reachability. Với đồ thị thưa, chi phí O(V³) của Floyd–Warshall thường lãng phí; Johnson kết hợp reweighting với Dijkstra để xử lý all-pairs hiệu quả hơn.

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

> **Mạch nối:** Johnson biến trọng số để loại bỏ cạnh âm nhưng bảo toàn thứ tự đường đi, rồi chạy Dijkstra từ nhiều nguồn. Khoảng cách không đủ để trả lời người dùng; ta cần lưu parent hoặc predecessor để tái dựng chính đường đi.

## Johnson's thuật toán: all-pairs trên đồ thị thưa

Khi đồ thị sparse, `O(V^3)` có thể lãng phí. **Johnson's thuật toán** dùng Bellman-Ford để tìm potentials, reweight các cạnh thành non-negative mà bảo toàn shortest-path thứ tự (ordering / 순서), rồi chạy Dijkstra từ từng nguồn.

Ý tưởng reweight:

\[
w'(u,v)=w(u,v)+h(u)-h(v)
\]

Nếu `h` được chọn từ Bellman-Ford potentials, `w' >= 0`.

đường đi chi phí bị shift theo endpoints nhưng relative choice giữa các đường đi cùng nguồn/đích không đổi. Đây là một example đẹp của việc biến bài toán (problem / 문제) sang lĩnh vực (domain / 도메인) mà thuật toán mạnh hơn áp dụng được.

> **Mạch nối:** Reconstruction biến các relaxation thành chuỗi cạnh có thể trình bày và kiểm tra, nhưng parent tree chỉ chọn một đường khi có nhiều đường đồng hạng. Nếu cần số lượng đường tối ưu, ta phải duy trì thêm trạng thái đếm.

## đường đi reconstruction

khoảng cách giá trị thường chưa đủ. Muốn actual tuyến (route / 경로), khi relaxation thành công:

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

> **Mạch nối:** Đếm đường ngắn nhất cần cập nhật count khi gặp khoảng cách tốt hơn hoặc bằng nhau, đồng thời tránh đếm sai trong chu trình zero hoặc cấu trúc không phù hợp. Với nhiều nguồn, ta có thể khởi tạo khoảng cách 0 cho tất cả nguồn trong cùng một lần chạy.

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

> **Mạch nối:** Multi-source shortest path tương đương thêm một super-source với cạnh 0, miễn semantics của nguồn chung là đúng. Khi chỉ cần một nhóm đích, multi-target và early exit cắt bớt phần tính toán nhưng phải giữ invariant của priority queue.

## Multi-source đường đi ngắn nhất

Nếu có nhiều sources và cần khoảng cách tới nguồn gần nhất, không nhất thiết chạy thuật toán nhiều lần.

Với đồ thị không trọng số, đưa vào hàng đợi tất cả sources với khoảng cách 0 rồi BFS một lần.

Với non-negative đồ thị có trọng số, push tất cả sources vào Dijkstra PQ với khoảng cách 0.

Mô hình tư duy: tạo một virtual super-source nối tới mọi nguồn bằng cạnh trọng số 0.

> **Mạch nối:** Early exit chỉ an toàn khi hàng đợi cho biết không còn đường rẻ hơn tới các đích chưa xử lý. Nếu muốn hướng tìm kiếm về đích trước, heuristic đưa thêm ước lượng vào priority nhưng phải thỏa điều kiện phù hợp.

## Multi-target và early exit

Trong Dijkstra, nếu chỉ cần một đích, có thể dừng khi đích được pop với non-stale minimum khoảng cách, vì lúc đó nó đã finalized.

Không nên dừng ngay khi đích lần đầu được được khám phá/relaxed; tentative khoảng cách có thể còn được cải thiện trước khi đích trở thành min frontier.

> **Mạch nối:** Heuristic giúp A* ưu tiên vùng có triển vọng, còn tính tối ưu phụ thuộc admissibility và cách xử lý consistency. Bidirectional search là một hướng giảm không gian khác, dựa trên hai frontier thay vì dự đoán chi phí.

## A*: đường đi ngắn nhất với heuristic

**A\*** ưu tiên:

\[
f(v)=g(v)+h(v)
\]

trong đó `g(v)` là chi phí từ nguồn, `h(v)` ước lượng chi phí còn lại tới đích.

Nếu heuristic **admissible** (`h(v)` không overestimate true remaining chi phí), A* có thể giữ optimality. Nếu heuristic còn consistent, xử lý hành vi gần Dijkstra với reweighted các độ ưu tiên và ít reopen hơn.

Dijkstra chính là A* với `h(v)=0`.

Trong routing/spatial tìm kiếm (search / 검색), heuristic tốt giúp bỏ rất nhiều vùng đồ thị không liên quan.

> **Mạch nối:** Bidirectional search cần quy tắc gặp nhau và điều kiện dừng nhất quán giữa hai phía. Dù thuật toán đúng về mặt lý thuyết, biểu diễn infinity và phép cộng khoảng cách sai có thể làm hỏng chính invariant đó.

## Bidirectional tìm kiếm (search / 검색)

Nếu nguồn và đích đã biết, có thể tìm kiếm từ hai phía và gặp nhau ở giữa. Với đồ thị không trọng số, BFS hai chiều có thể giảm mạnh kích thước biên tìm kiếm hiệu dụng từ khoảng `b^d` xuống gần `2b^{d/2}` trong mô hình phân nhánh lý tưởng.

Weighted bidirectional Dijkstra phức tạp hơn vì stopping điều kiện phải đảm bảo cận dưới hai frontier đã đủ lớn; không thể chỉ dừng ở lần đầu hai searches chạm nhau một cách ngây thơ.

> **Mạch nối:** Infinity phải được chọn sao cho cộng và so sánh không gây overflow hoặc biến trạng thái unreachable thành reachable. Với trọng số số thực, sai số làm nảy sinh một lớp vấn đề khác về so sánh và tie-breaking.

## tràn số và infinity cách biểu diễn (representation / 표현)

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

Trong C, signed tràn số nguyên (integer overflow) có thể là undefined hành vi. Cần chọn kiểu (type / 타입) đủ rộng và kiểm ranh giới.

JavaScript `Number` biểu diễn integer chính xác tới:

\[
2^{53}-1
\]

Nếu đường đi sum có thể vượt vùng này, cân nhắc `BigInt` hoặc thay đổi mô hình dữ liệu.

> **Mạch nối:** Với floating-point, cần quy định epsilon, cách cộng dồn và tiêu chí đồng hạng thay vì so sánh tuyệt đối. Sau khi chốt tính đúng số học, lựa chọn cấu trúc chạy còn phụ thuộc đồ thị sparse hay dense.

## Floating-point các trọng số

Nếu các trọng số là `double`, equality kiểm thử (test / 테스트) và stale check cần cẩn thận. Với floating-point, expression `curDist != dist[u]` có thể vẫn hoạt động nếu các giá trị được bản sao (copy / 복사) nguyên từ computed khoảng cách, nhưng các phép so sánh gần ranh giới có thể chịu rounding.

Nếu lĩnh vực (domain / 도메인) là tiền tệ hoặc fixed-scale chi phí, integer minor units thường an toàn hơn dấu phẩy động.

> **Mạch nối:** Sparse graph thường hợp với adjacency list và heap, trong khi dense graph có thể hưởng lợi từ ma trận và thao tác tuyến tính. Dù representation nào được chọn, shortest-path tree vẫn phục vụ một nguồn và không đồng nghĩa với minimum spanning tree.

## Sparse vs đồ thị dày

danh sách kề phù hợp đồ thị thưa và Dijkstra/BFS thường chỉ iterate outgoing các cạnh thực sự tồn tại.

ma trận kề cho cạnh tra cứu `O(1)` nhưng iteration các đỉnh kề `O(V)`. Trên đồ thị dày, matrix-based các thuật toán có thể cạnh tranh vì tính cục bộ (locality) tốt và `E ≈ V^2` anyway.

Big-O phải gắn với cách biểu diễn.

> **Mạch nối:** Shortest-path tree tối ưu khoảng cách từ một nguồn, còn MST tối ưu tổng trọng số của toàn cây; hai mục tiêu có thể chọn các cạnh hoàn toàn khác nhau. Bảng quyết định dưới đây đặt các thuật toán cạnh nhau theo điều kiện đầu vào và mục tiêu.

## đường đi ngắn nhất cây không phải cây khung nhỏ nhất

Dijkstra từ nguồn tạo một cây đường đi ngắn nhất: đường đi từ nguồn tới mỗi đỉnh là shortest.

MST tối thiểu **tổng trọng số của toàn bộ cây**. Nó không đảm bảo đường đi từ nút gốc tới từng đỉnh là shortest.

Hai objectives khác nhau:

```text
Shortest-path tree -> tối ưu route từ source
MST                -> tối ưu total infrastructure cost
```

Đừng chọn thuật toán chỉ vì cả hai “trông như chọn cạnh nhỏ”.

> **Mạch nối:** Decision table biến khác biệt giữa BFS, Dijkstra, Bellman–Ford, DAG và Floyd–Warshall thành tiêu chí chọn có thể kiểm tra. Phần tiếp theo dùng các tiêu chí đó để xử lý những hiểu lầm thường làm chọn sai thuật toán.

## Quyết định (decision / 결정) bảng (table / 테이블)

Phần này kiểm tra ranh giới và failure mode của cơ chế vừa học. Hãy dùng nó để biết khi nào mô hình còn đúng, khi nào cần đổi chiến lược và bằng chứng nào phải thu thập.

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

> **Mạch nối:** Một lựa chọn đúng trên giấy vẫn có thể sai do parent, overflow, negative cycle hoặc điều kiện unreachable. Vì vậy kiểm thử triển khai phải xác nhận cả đáp án, đường đi, trạng thái lỗi và trường hợp biên.

## Những hiểu lầm phổ biến

**“Dijkstra nhanh hơn Bellman-Ford nên cứ dùng Dijkstra.”** Sai nếu có negative cạnh. tính đúng đắn điều kiện quan trọng hơn speed.

**“BFS chỉ là traversal, không phải đường đi ngắn nhất.”** Với equal cạnh các chi phí, BFS chính là shortest-path thuật toán tối ưu.

**“Negative chu trình nghĩa là mọi đường đi ngắn nhất trong đồ thị đều không tồn tại.”** Không. Chỉ các source-target regions bị ảnh hưởng mới không có finite minimum.

**“Floyd-Warshall chỉ dùng cho positive các trọng số.”** Nó hỗ trợ negative các cạnh, miễn hiểu ngữ nghĩa negative chu trình.

**“Dijkstra dừng khi đích được nhìn thấy lần đầu.”** Không. Dừng khi đích được extract/finalize đúng điều kiện.

**“PriorityQueue phần tử trùng mục làm Dijkstra sai.”** Không nếu dùng stale-entry check. Nó là cách triển khai sự đánh đổi (trade-off / 트레이드오프) phổ biến.

> **Mạch nối:** Test implementation nên đối chiếu với brute force hoặc Floyd–Warshall trên đồ thị nhỏ, rồi mở rộng sang dữ liệu xấu và tải thực tế. Khi các invariant đã được bảo vệ, ta có thể nối shortest path với routing, dependency và scheduling trong hệ thống.

## kiểm thử shortest-path cách triển khai

Kiểm thử (test / 테스트) nên bao gồm:

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

Nếu nút cha đường đi được lưu, tổng trọng số trên nút cha chuỗi (chain / 사슬) phải bằng reported `dist[target]`.

Trên đồ thị nhỏ, có thể differential-test Dijkstra non-negative với Floyd-Warshall tham chiếu.

> **Mạch nối:** Hệ thống thực tế thường thêm thời gian, năng lực, mode di chuyển, ràng buộc và chi phí thay đổi; vì thế “đỉnh” có thể là một state tuple chứ không chỉ là location. Mô hình tư duy mở rộng giúp nhận ra khi nào shortest path cổ điển không còn đủ.

## Liên kết (connection / 연결) với các hệ thống thực tế

Routing, điều hướng bản đồ, phụ thuộc (dependency / 의존성) chi phí, mạng độ trễ (latency / 지연 시간) planning, tìm đường cho AI trò chơi, logistics, tối ưu luồng công việc và xây dựng phụ thuộc (dependency / 의존성) đều có shortest-path variants.

Nhưng hệ thống thực tế thường thêm các ràng buộc: time-dependent các trọng số, turn penalties, multiple resources, sức chứa (capacity / 용량), stochastic các chi phí hoặc động đồ thị. Khi đó classical đường đi ngắn nhất có thể trở thành trạng thái-space đường đi ngắn nhất: mỗi “đỉnh” thực sự là `(location, time, fuel, mode, ...)`.

Đây là liên kết (connection / 연결) quan trọng với bài toán (problem / 문제) mô hình hóa: thuật toán có thể đúng nhưng trạng thái cách biểu diễn thiếu thông tin thì kết quả vẫn sai.

> **Mạch nối:** Mô hình mở rộng luôn bắt đầu bằng việc xác định state, transition, cost, nguồn–đích và invariant cần giữ. Khi năm yếu tố này rõ ràng, việc chọn thuật toán và cách kiểm thử trở thành hệ quả của mô hình thay vì một lựa chọn cảm tính.

## Mô hình tư duy mở rộng

> đường đi ngắn nhất không bắt đầu từ tên thuật toán; nó bắt đầu từ việc xác định **chi phí algebra và thứ tự (ordering / 순서) nào cho phép một ứng viên trở thành final**.

BFS dựa vào thứ tự theo tầng. 0–1 BFS dùng deque để duy trì hai mức chi phí cục bộ. Dijkstra dựa vào trọng số không âm. Bellman–Ford dựa vào giới hạn số cạnh của đường đi đơn. Thuật toán trên DAG dùng thứ tự phụ thuộc. Floyd–Warshall dùng quy hoạch động theo tập đỉnh trung gian được phép.

Nếu nhớ được điều kiện làm mỗi method đúng, bạn có thể chọn thuật toán từ bản chất bài toán thay vì từ mẫu memorization.

> **Bàn giao:** Sau **Mô hình tư duy mở rộng**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
