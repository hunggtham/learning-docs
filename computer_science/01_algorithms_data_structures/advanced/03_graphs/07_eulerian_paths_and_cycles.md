# Eulerian Paths và Cycles
**Đường đi Euler và chu trình Euler / Eulerian Path & Cycle / 오일러 경로와 회로**

Eulerian problems hỏi một câu rất cụ thể: **có thể đi qua mỗi edge đúng một lần hay không?** Đây là bài toán về edge usage, khác hoàn toàn Hamiltonian path/cycle nơi mỗi **vertex** phải được thăm đúng một lần.

Sự khác biệt này quyết định độ khó. Eulerian path có characterization rất đẹp bằng degree/balance và có thể xây trong `O(V+E)`. Hamiltonian path nói chung không có local criterion đơn giản tương tự và thuộc lớp bài toán khó hơn nhiều.

## 1. Abstraction từ Königsberg

Bài toán các cây cầu Königsberg nổi tiếng vì Euler bỏ hình dạng địa lý cụ thể và chỉ giữ:

```text
land regions -> vertices
bridges      -> edges
```

Question “đi qua mỗi bridge đúng một lần” trở thành graph problem. Đây là một ví dụ lịch sử điển hình của algorithmic modeling: bỏ detail không ảnh hưởng feasibility và giữ structure quyết định bài toán.

## 2. Trail, path, circuit và terminology

Trong nhiều tài liệu:

- **trail**: không lặp edge;
- **path**: thường không lặp vertex theo graph-theory strict terminology;
- **Eulerian trail/path**: đi qua mọi edge đúng một lần, vertex có thể lặp;
- **Eulerian circuit/cycle**: Eulerian trail có start = end.

Competitive-programming material đôi khi dùng “Euler path” cho trail. Khi đọc tài liệu, hãy nhìn semantics thay vì chỉ tên.

## 3. Undirected graph: parity condition

Bỏ qua isolated vertices degree 0, phần graph chứa edges phải connected.

Eulerian cycle tồn tại khi **mọi vertex có degree chẵn**.

Open Eulerian trail tồn tại khi **đúng hai vertices có degree lẻ**; chúng là hai endpoints.

Nếu số odd-degree vertices khác 0 hoặc 2, không tồn tại Eulerian trail.

## 4. Vì sao parity là điều kiện cần?

Ở một vertex trung gian, mỗi lần route đi vào qua một unused edge, nó phải đi ra qua một unused edge khác. Incident edges được consume theo cặp:

```text
in + out
in + out
...
```

nên degree phải chẵn.

Start của open trail có thể có một outgoing edge dư, end có một incoming edge dư, tạo đúng hai odd vertices.

Handshaking lemma cũng nói số odd-degree vertices trong undirected graph luôn chẵn, nên “1 odd vertex” vốn đã bất khả thi.

## 5. Vì sao parity chưa đủ?

Hai cycles tách rời có mọi degree chẵn nhưng không thể có một tour duy nhất dùng edges của cả hai components. Ta không thể teleport.

Vì vậy cần connectivity của **subgraph chứa nonzero-degree vertices**.

Isolated vertices không ảnh hưởng edge-covering trail vì không có edge cần dùng ở đó.

## 6. Directed graph: indegree/outdegree balance

Với directed graph, parity được thay bằng balance.

Eulerian cycle:

```text
indegree(v) == outdegree(v)
```

cho mọi relevant vertex, kèm connectivity condition thích hợp.

Open trail:

```text
start: out = in + 1
end:   in  = out + 1
others: in == out
```

Flow intuition rất rõ: intermediate vertex phải consume incoming/outgoing edges theo cặp.

## 7. Connectivity trong directed graph

Degree balance một mình không đủ. Với Eulerian cycle, các vertices có nonzero degree phải nằm trong một directed connectivity structure đủ mạnh để mọi edges thuộc cùng traversable component.

Một cách reasoning chuẩn là kiểm tra strongly connected trên relevant vertices sau khi xử lý start/end conditions thích hợp, hoặc dùng theorem tương đương với underlying undirected connectivity cộng degree constraints cho Eulerian trail trong formulation cụ thể.

Điểm cốt lõi: **balance không nối các components**.

## 8. Start vertex selection

Undirected:

```text
0 odd vertices -> start bất kỳ vertex degree > 0
2 odd vertices -> start phải là một odd vertex
```

Directed:

```text
open trail -> start có out = in + 1
cycle      -> start bất kỳ vertex có outgoing edge
```

Start sai có thể làm traversal kết thúc sớm dù graph có Eulerian trail hợp lệ.

## 9. Hierholzer's Algorithm

Hierholzer xây route bằng cách đi qua unused edges cho tới khi current vertex không còn edge unused. Khi dead-end, vertex được đưa vào output và ta backtrack.

Stack view:

```text
while stack not empty:
    u = top
    if u còn unused edge:
        consume edge (u,v)
        push v
    else:
        path.push(pop stack)
reverse(path)
```

Output được tạo theo reverse finishing order.

## 10. Vì sao Hierholzer không bị “greedy dead-end”?

Trong graph thỏa Euler conditions, balance/parity đảm bảo một route đang đi không thể mắc kẹt ở vertex “sai” trừ endpoint hợp lệ. Nếu tour cục bộ đóng lại nhưng vẫn còn unused edges, connectivity đảm bảo unused region gắn vào một vertex đã xuất hiện trong tour. Ta có thể bắt đầu sub-tour ở đó và splice vào route cũ.

Đây là khác biệt với arbitrary path search: graph structure bảo đảm local edge consumption có thể ghép thành global solution.

## 11. Splicing view

Classic proof thường hình dung:

1. xây một cycle;
2. tìm vertex trên cycle còn unused edge;
3. xây cycle khác từ vertex đó;
4. splice cycle mới vào cycle cũ;
5. lặp tới khi hết edges.

Stack implementation chính là cách thực hiện việc splice này implicit và gọn hơn.

## 12. Representation quyết định complexity thật

Nếu mỗi lần ở `u` ta scan adjacency list từ đầu để tìm edge unused, cùng edge có thể bị xem lại nhiều lần.

Một implementation linear nên giữ:

```text
ptr[u] = vị trí adjacency tiếp theo cần xét
```

hoặc destructively pop edges khỏi cuối list.

Mỗi adjacency entry được advance constant number of times, nên total `O(V+E)`.

## 13. Undirected graph cần Edge ID

Mỗi undirected logical edge thường xuất hiện hai adjacency entries. Nếu chỉ mark `(u,v)` theo endpoints, parallel edges bị nhầm.

Dùng:

```text
edge id
used[id]
```

để đảm bảo mỗi physical edge consume đúng một lần.

Self-loop cũng cần edge ID; trong undirected graph nó góp 2 vào degree.

## 14. JavaScript implementation

```js
function eulerUndirected(n, edges, start) {
  const g = Array.from({ length: n }, () => []);

  edges.forEach(([u, v], id) => {
    g[u].push([v, id]);
    g[v].push([u, id]);
  });

  const used = Array(edges.length).fill(false);
  const ptr = Array(n).fill(0);
  const stack = [start];
  const path = [];

  while (stack.length) {
    const u = stack[stack.length - 1];

    while (ptr[u] < g[u].length && used[g[u][ptr[u]][1]]) {
      ptr[u]++;
    }

    if (ptr[u] === g[u].length) {
      path.push(stack.pop());
    } else {
      const [v, id] = g[u][ptr[u]++];
      if (used[id]) continue;
      used[id] = true;
      stack.push(v);
    }
  }

  path.reverse();
  return path;
}
```

Postcondition mạnh:

```text
path.length == E + 1
```

nếu một Eulerian trail hợp lệ đã dùng hết `E` edges.

## 15. Validate output thay vì chỉ tin algorithm

Một validator có thể kiểm tra:

```text
route có E+1 vertices
mỗi bước route tương ứng một edge thật
mỗi edge id dùng đúng một lần
start/end đúng degree conditions
```

Với parallel edges, validator cũng phải match edge identities, không chỉ endpoint pairs.

## 16. Fleury's Algorithm và vì sao Hierholzer tốt hơn

Fleury chọn edge không phải bridge nếu còn lựa chọn khác. Conceptually đẹp vì cố tránh làm phần graph còn lại disconnect.

Nhưng nếu mỗi bước phải recompute bridge, naive complexity cao. Hierholzer đạt linear time mà không cần dynamic bridge detection.

Bài học: một greedy rule trực quan chưa chắc là implementation tốt nhất dù correctness dễ hình dung.

## 17. Eulerian graph và Bridges

Trong một connected Eulerian graph có edges, mọi edge nằm trên một cycle của Euler tour, nên không edge nào là bridge.

Nếu graph có bridge, đi qua bridge sang một region rồi muốn quay lại sẽ cần dùng bridge lần hai, trừ open trail endpoint structure rất đặc biệt. Parity/cycle perspective giải thích mối liên hệ này.

Graph properties không tồn tại độc lập; bridge/cycle/degree constraints tương tác với nhau.

## 18. Eulerization

Nếu graph chưa Eulerian nhưng muốn route qua mọi edge, ta có thể thêm/duplicate edges để làm odd-degree vertices trở thành even.

Trong undirected graph, số odd vertices luôn chẵn. Bài toán chọn pairs odd vertices để duplicate shortest paths tối ưu dẫn tới **Chinese Postman Problem**.

Eulerian tour là building block sau khi graph được Eulerize.

## 19. Chinese Postman Problem

Objective:

> Đi qua mọi edge ít nhất một lần với tổng cost nhỏ nhất.

Nếu graph Eulerian, answer là Euler tour trực tiếp.

Nếu không, phải duplicate một số routes sao cho mọi degree trở thành chẵn với extra cost nhỏ nhất. Weighted version liên quan shortest paths + minimum-weight matching trên odd vertices.

Đây là ví dụ rõ về cách một theorem structural trở thành primitive của optimization problem lớn hơn.

## 20. De Bruijn Graph

K-mers/string fragments có thể được model:

```text
vertex = prefix/suffix length k-1
edge   = k-mer
```

Một Eulerian path qua mọi fragment edge reconstruct sequence sử dụng mọi k-mer đúng một lần theo model.

Connection này xuất hiện trong genome assembly intuition và de Bruijn sequence construction.

## 21. De Bruijn Sequence

Muốn sequence chứa mọi string length `k` trên alphabet đúng một lần theo cyclic window, xây graph:

```text
vertices = strings length k-1
edges = strings length k
```

Eulerian cycle đi qua mỗi edge exactly once, và đọc labels tạo de Bruijn sequence.

Một problem string tưởng rất khác lại trở thành edge-covering graph problem.

## 22. Itinerary Reconstruction

Một family bài phổ biến: tickets là directed edges, cần dùng tất cả tickets một lần và đôi khi chọn lexical-smallest valid itinerary.

Graph có thể có parallel edges. Hierholzer vẫn là core, nhưng adjacency cần ordering phù hợp — thường sort reverse rồi pop cuối hoặc dùng priority queue.

Complexity lúc này thêm sorting:

\[
O(E\log E)
\]

hoặc sum per-vertex sort costs.

## 23. Lexicographically smallest Eulerian trail

Nếu nhiều valid trails, muốn lexical-smallest route cần định nghĩa order của outgoing edges.

Một cách là sort adjacency và Hierholzer luôn consume smallest edge. Nhưng phải reasoning cẩn thận về output reversal; implementation thường sort descending và pop smallest-from-end hoặc dùng min-heap.

Tie-breaking là thêm output constraint, nên cost model khác pure Eulerian existence.

## 24. Euler Tour trên tree là khái niệm khác

Trong tree algorithms, “Euler tour” thường là DFS sequence ghi enter/exit node để flatten subtree hoặc solve LCA/RMQ.

Nó không nhất thiết là Eulerian trail “mỗi edge đúng một lần”. Một tree DFS đi xuống và quay lên thường traverse physical edge hai lần.

Tên giống nhau nhưng abstraction khác; hãy nhìn definition.

## 25. Directed edge labels và duplicate tickets

Nếu two edges có cùng `(u,v)` nhưng đại diện hai tickets/items khác nhau, dùng endpoint pair làm key có thể gộp nhầm. Edge ID hoặc multiset count là bắt buộc.

Nếu chỉ cần route vertices, count representation có thể compact hơn explicit edge object khi rất nhiều duplicate edges.

## 26. Empty Graph và degenerate cases

Graph không có edge có thể được coi là Eulerian một cách trivial tùy definition/API. Route có thể là empty hoặc một chosen vertex.

Single self-loop là Eulerian cycle. Two parallel edges giữa hai vertices tạo cycle length 2 theo multigraph semantics.

Corner cases cần được định nghĩa trước, không để implementation vô tình quyết định semantics.

## 27. Complexity theo output

Euler trail output có `E+1` vertices/edge identifiers, nên riêng việc emit solution đã cần `Ω(E)`.

Hierholzer `O(V+E)` vì thế asymptotically optimal theo input/output size trong adjacency representation thông thường.

Đây là ví dụ đẹp của output-sensitive lower bound.

## 28. Memory layout và destructive traversal

Nếu algorithm được phép phá adjacency lists, có thể `pop()` edges để giảm extra `ptr[]`. Nhưng caller sẽ mất graph original.

Non-destructive implementation giữ `ptr`/used state. Đây là trade-off mutation contract vs extra memory.

Trong C/JavaScript, destructive pop cuối thường cache-friendly và đơn giản; trong shared graph structure, copy toàn graph có thể đắt hơn một pointer array.

## 29. Streaming/online limitation

Eulerian trail là global property. Nếu edges arrive online và ta phải output route ngay mà không biết future edges, local choice có thể không đủ vì future degree/connectivity chưa biết.

Static Hierholzer giả định graph đã biết. Dynamic Eulerian maintenance là problem khác, thường cần maintain degree parity/connectivity và chưa chắc cho phép emit final route incrementally đơn giản.

## 30. Testing

Test families:

```text
simple cycle
path graph with exactly 2 odd vertices
star with >2 odd vertices -> impossible
disconnected even-degree components -> impossible
parallel edges
self-loops
directed balanced cycle
directed open trail
duplicate tickets
empty graph
```

Trên graph nhỏ, brute-force backtracking over edge IDs có thể làm oracle để verify existence/path của Hierholzer.

## 31. Common implementation failures

Các lỗi điển hình:

```text
quên connectivity check
start sai
mark adjacency entry thay vì physical edge
không hỗ trợ parallel edges
shift() đầu JS array gây cost xấu
output không reverse
không verify E edges đã dùng
nhầm Eulerian với Hamiltonian
```

Một implementation trả route ngắn hơn `E+1` thường là dấu hiệu graph không thỏa assumptions hoặc traversal bỏ sót component/edge.

## Mental Model

> Eulerian reasoning là **flow balance của edges qua vertices**. Intermediate vertex cần ghép edge vào với edge ra; undirected graph biểu hiện bằng parity, directed graph biểu hiện bằng indegree/outdegree balance.

Khi balance + connectivity đúng, Hierholzer biến local edge consumption thành global route bằng reverse finishing/splicing. Đây là lý do Eulerian problems có linear-time structure đẹp trong khi vertex-covering Hamiltonian problems không có cùng property.

Xem thêm: [Graph Modeling](./00_graph_modeling_and_representation.md), [Bridges](./06_bridges_articulation_and_biconnectivity.md), [Network Flow](./08_network_flow_and_matching.md).