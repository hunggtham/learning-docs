# Eulerian các đường đi và các chu trình
**Đường đi Euler và chu trình Euler / Eulerian đường đi & chu trình / 오일러 경로와 회로**

Eulerian problems hỏi một câu rất cụ thể: **có thể đi qua mỗi cạnh đúng một lần hay không?** Đây là bài toán về cạnh usage, khác hoàn toàn Hamiltonian đường đi/chu trình nơi mỗi **đỉnh** phải được thăm đúng một lần.

Sự khác biệt này quyết định độ khó. Eulerian đường đi có characterization rất đẹp bằng degree/balance và có thể xây trong `O(V+E)`. Hamiltonian đường đi nói chung không có cục bộ criterion đơn giản tương tự và thuộc lớp bài toán khó hơn nhiều.

## 1. sự trừu tượng (abstraction) từ Königsberg

Bài toán các cây cầu Königsberg nổi tiếng vì Euler bỏ hình dạng địa lý cụ thể và chỉ giữ:

```text
land regions -> vertices
bridges      -> edges
```

Question “đi qua mỗi bridge đúng một lần” trở thành đồ thị problem. Đây là một ví dụ lịch sử điển hình của algorithmic mô hình hóa: bỏ detail không ảnh hưởng feasibility và giữ structure quyết định bài toán.

## 2. Trail, đường đi, circuit và terminology

Trong nhiều tài liệu:

- **trail**: không lặp cạnh;
- **đường đi**: thường không lặp đỉnh theo graph-theory strict terminology;
- **Eulerian trail/đường đi**: đi qua mọi cạnh đúng một lần, đỉnh có thể lặp;
- **Eulerian circuit/chu trình**: Eulerian trail có start = end.

Competitive-programming material đôi khi dùng “Euler đường đi” cho trail. Khi đọc tài liệu, hãy nhìn ngữ nghĩa (semantics) thay vì chỉ tên.

## 3. đồ thị vô hướng (undirected graph): parity điều kiện

Bỏ qua isolated các đỉnh degree 0, phần đồ thị chứa các cạnh phải connected.

Eulerian chu trình tồn tại khi **mọi đỉnh có degree chẵn**.

Đường đi Euler mở tồn tại khi **đúng hai đỉnh có bậc lẻ**; hai đỉnh đó là hai đầu mút của đường đi.

Nếu số odd-degree các đỉnh khác 0 hoặc 2, không tồn tại Eulerian trail.

## 4. Vì sao parity là điều kiện cần?

Ở một đỉnh trung gian, mỗi lần route đi vào qua một unused cạnh, nó phải đi ra qua một unused cạnh khác. Incident các cạnh được consume theo cặp:

```text
in + out
in + out
...
```

nên degree phải chẵn.

Start của open trail có thể có một outgoing cạnh dư, end có một incoming cạnh dư, tạo đúng hai odd các đỉnh.

Handshaking lemma cũng nói số odd-degree các đỉnh trong đồ thị vô hướng luôn chẵn, nên “1 odd đỉnh” vốn đã bất khả thi.

## 5. Vì sao parity chưa đủ?

Hai các chu trình tách rời có mọi degree chẵn nhưng không thể có một tour duy nhất dùng các cạnh của cả hai các thành phần. Ta không thể teleport.

Vì vậy cần connectivity của **subgraph chứa nonzero-degree các đỉnh**.

Isolated các đỉnh không ảnh hưởng edge-covering trail vì không có cạnh cần dùng ở đó.

## 6. đồ thị có hướng: cân bằng bậc vào/bậc ra

Với đồ thị có hướng, parity được thay bằng balance.

Eulerian chu trình:

```text
indegree(v) == outdegree(v)
```

cho mọi relevant đỉnh, kèm connectivity điều kiện thích hợp.

Open trail:

```text
start: out = in + 1
end:   in  = out + 1
others: in == out
```

Trực giác theo luồng rất rõ: ở mỗi đỉnh trung gian, các cạnh đi vào và đi ra phải được sử dụng theo cặp.

## 7. Connectivity trong đồ thị có hướng

Degree balance một mình không đủ. Với Eulerian chu trình, các đỉnh có nonzero degree phải nằm trong một directed connectivity structure đủ mạnh để mọi các cạnh thuộc cùng traversable thành phần.

Một cách reasoning chuẩn là kiểm tra strongly connected trên relevant các đỉnh sau khi xử lý start/end các điều kiện thích hợp, hoặc dùng theorem tương đương với tính liên thông của đồ thị vô hướng nền cộng degree các ràng buộc cho Eulerian trail trong formulation cụ thể.

Điểm cốt lõi: **balance không nối các thành phần**.

## 8. Start đỉnh selection

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

Start sai có thể làm traversal kết thúc sớm dù đồ thị có Eulerian trail hợp lệ.

## 9. Hierholzer's thuật toán

Hierholzer xây route bằng cách đi qua unused các cạnh cho tới khi hiện tại đỉnh không còn cạnh unused. Khi dead-end, đỉnh được đưa vào đầu ra và ta backtrack.

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

đầu ra được tạo theo reverse finishing order.

## 10. Vì sao Hierholzer không bị “greedy dead-end”?

Trong đồ thị thỏa Euler các điều kiện, balance/parity đảm bảo một route đang đi không thể mắc kẹt ở đỉnh “sai” trừ endpoint hợp lệ. Nếu tour cục bộ đóng lại nhưng vẫn còn unused các cạnh, connectivity đảm bảo unused region gắn vào một đỉnh đã xuất hiện trong tour. Ta có thể bắt đầu sub-tour ở đó và splice vào route cũ.

Đây là khác biệt với arbitrary đường đi search: đồ thị structure bảo đảm cục bộ cạnh consumption có thể ghép thành toàn cục lời giải.

## 11. Splicing view

Kinh điển chứng minh thường hình dung:

1. xây một chu trình;
2. tìm đỉnh trên chu trình còn unused cạnh;
3. xây chu trình khác từ đỉnh đó;
4. splice chu trình mới vào chu trình cũ;
5. lặp tới khi hết các cạnh.

Stack cách triển khai chính là cách thực hiện việc splice này implicit và gọn hơn.

## 12. cách biểu diễn (representation) quyết định complexity thật

Nếu mỗi lần ở `u` ta quét danh sách kề từ đầu để tìm cạnh unused, cùng cạnh có thể bị xem lại nhiều lần.

Một cách triển khai linear nên giữ:

```text
ptr[u] = vị trí adjacency tiếp theo cần xét
```

hoặc destructively pop các cạnh khỏi cuối list.

Mỗi adjacency mục được advance constant number of times, nên total `O(V+E)`.

## 13. đồ thị vô hướng cần cạnh ID

Mỗi undirected logic cạnh thường xuất hiện hai adjacency các mục. Nếu chỉ mark `(u,v)` theo endpoints, các cạnh song song bị nhầm.

Dùng:

```text
edge id
used[id]
```

để đảm bảo mỗi vật lý cạnh consume đúng một lần.

Self-loop cũng cần cạnh ID; trong đồ thị vô hướng nó góp 2 vào degree.

## 14. JavaScript cách triển khai

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

điều kiện sau mạnh:

```text
path.length == E + 1
```

nếu một Eulerian trail hợp lệ đã dùng hết `E` các cạnh.

## 15. Validate đầu ra thay vì chỉ tin thuật toán

Một bộ xác minh có thể kiểm tra:

```text
route có E+1 vertices
mỗi bước route tương ứng một edge thật
mỗi edge id dùng đúng một lần
start/end đúng degree conditions
```

Với các cạnh song song, bộ xác minh cũng phải match cạnh identities, không chỉ endpoint pairs.

## 16. Fleury's thuật toán và vì sao Hierholzer tốt hơn

Fleury chọn cạnh không phải bridge nếu còn lựa chọn khác. Conceptually đẹp vì cố tránh làm phần đồ thị còn lại disconnect.

Nếu ở mỗi bước đều phải tính lại cầu, cách làm đơn giản sẽ có độ phức tạp cao. Hierholzer đạt thời gian tuyến tính mà không cần phát hiện cầu động.

Bài học: một quy tắc tham lam trực quan chưa chắc là cách triển khai tốt nhất dù tính đúng đắn dễ hình dung.

## 17. Eulerian đồ thị và Bridges

Trong một connected Eulerian đồ thị có các cạnh, mọi cạnh nằm trên một chu trình của Euler tour, nên không cạnh nào là bridge.

Nếu đồ thị có bridge, đi qua bridge sang một region rồi muốn quay lại sẽ cần dùng bridge lần hai, trừ open trail endpoint structure rất đặc biệt. Parity/chu trình perspective giải thích mối liên hệ này.

đồ thị các tính chất không tồn tại độc lập; bridge/chu trình/degree các ràng buộc tương tác với nhau.

## 18. Eulerization

Nếu đồ thị chưa Eulerian nhưng muốn route qua mọi cạnh, ta có thể thêm/phần tử trùng các cạnh để làm odd-degree các đỉnh trở thành even.

Trong đồ thị vô hướng, số odd các đỉnh luôn chẵn. Bài toán chọn pairs odd các đỉnh để phần tử trùng các đường đi ngắn nhất tối ưu dẫn tới **Chinese Postman Problem**.

Eulerian tour là building block sau khi đồ thị được Eulerize.

## 19. Chinese Postman Problem

Objective:

> Đi qua mọi cạnh ít nhất một lần với tổng chi phí nhỏ nhất.

Nếu đồ thị Eulerian, answer là Euler tour trực tiếp.

Nếu không, phải phần tử trùng một số routes sao cho mọi degree trở thành chẵn với extra chi phí nhỏ nhất. Weighted version liên quan các đường đi ngắn nhất + minimum-weight matching trên odd các đỉnh.

Đây là ví dụ rõ về cách một theorem structural trở thành primitive của optimization problem lớn hơn.

## 20. De Bruijn đồ thị

K-mers/string fragments có thể được mô hình:

```text
vertex = prefix/suffix length k-1
edge   = k-mer
```

Một Eulerian đường đi qua mọi fragment cạnh reconstruct sequence sử dụng mọi k-mer đúng một lần theo mô hình.

Connection này xuất hiện trong lắp ráp bộ gen intuition và de Bruijn xây dựng chuỗi.

## 21. De Bruijn Sequence

Muốn sequence chứa mọi string length `k` trên alphabet đúng một lần theo cyclic window, xây đồ thị:

```text
vertices = strings length k-1
edges = strings length k
```

Chu trình Euler đi qua mỗi cạnh đúng một lần; nếu đọc nhãn theo đường đi, ta có thể xây dựng dãy de Bruijn.

Một problem string tưởng rất khác lại trở thành edge-covering đồ thị problem.

## 22. Itinerary Reconstruction

Một family bài phổ biến: tickets là directed các cạnh, cần dùng tất cả tickets một lần và đôi khi chọn lexical-smallest hợp lệ itinerary.

đồ thị có thể có các cạnh song song. Hierholzer vẫn là core, nhưng adjacency cần ordering phù hợp — thường sort reverse rồi pop cuối hoặc dùng hàng đợi ưu tiên.

Complexity lúc này thêm sorting:

\[
O(E\log E)
\]

hoặc sum per-vertex sort các chi phí.

## 23. Lexicographically smallest Eulerian trail

Nếu nhiều hợp lệ trails, muốn lexical-smallest route cần định nghĩa order của outgoing các cạnh.

Một cách là sort adjacency và Hierholzer luôn consume smallest cạnh. Nhưng phải reasoning cẩn thận về đầu ra reversal; cách triển khai thường sort descending và pop smallest-from-end hoặc dùng đống nhỏ nhất.

quy tắc phân xử khi bằng nhau là thêm đầu ra ràng buộc, nên mô hình chi phí khác pure Eulerian existence.

## 24. Euler Tour trên cây là khái niệm khác

Trong các thuật toán trên cây, “Euler tour” thường là dãy DFS ghi lại thời điểm vào/ra mỗi nút để làm phẳng cây con hoặc giải bài toán LCA/RMQ.

Nó không nhất thiết là Eulerian trail “mỗi cạnh đúng một lần”. Một cây DFS đi xuống và quay lên thường traverse vật lý cạnh hai lần.

Tên giống nhau nhưng sự trừu tượng khác; hãy nhìn definition.

## 25. Directed cạnh labels và phần tử trùng tickets

Nếu two các cạnh có cùng `(u,v)` nhưng đại diện hai tickets/items khác nhau, dùng endpoint pair làm khóa có thể gộp nhầm. cạnh ID hoặc multiset count là bắt buộc.

Nếu chỉ cần route các đỉnh, count cách biểu diễn có thể gọn hơn explicit cạnh đối tượng khi rất nhiều phần tử trùng các cạnh.

## 26. rỗng đồ thị và degenerate cases

đồ thị không có cạnh có thể được coi là Eulerian một cách trivial tùy definition/API. Route có thể là rỗng hoặc một chosen đỉnh.

Một khuyên đơn tự nó đã tạo thành chu trình Euler. Hai cạnh song song giữa hai đỉnh tạo một chu trình độ dài 2 theo ngữ nghĩa của đa đồ thị.

các trường hợp góc (corner cases) cần được định nghĩa trước, không để cách triển khai vô tình quyết định ngữ nghĩa.

## 27. Complexity theo đầu ra

Euler trail đầu ra có `E+1` các đỉnh/cạnh identifiers, nên riêng việc emit lời giải đã cần `Ω(E)`.

Hierholzer `O(V+E)` vì thế asymptotically optimal theo đầu vào/kích thước đầu ra trong adjacency cách biểu diễn thông thường.

Đây là ví dụ đẹp của nhạy theo kích thước đầu ra cận dưới.

## 28. bộ nhớ bố trí và destructive traversal

Nếu thuật toán được phép phá adjacency lists, có thể `pop()` các cạnh để giảm extra `ptr[]`. Nhưng hàm gọi sẽ mất đồ thị original.

Non-destructive cách triển khai giữ `ptr`/used trạng thái (state). Đây là sự đánh đổi (trade-off) sự thay đổi dữ liệu contract vs extra bộ nhớ.

Trong C/JavaScript, destructive pop cuối thường thân thiện với bộ nhớ đệm và đơn giản; trong shared đồ thị structure, copy toàn đồ thị có thể đắt hơn một con trỏ mảng.

## 29. xử lý luồng/trực tuyến limitation

Eulerian trail là toàn cục tính chất. Nếu các cạnh arrive trực tuyến và ta phải đầu ra route ngay mà không biết tương lai các cạnh, cục bộ choice có thể không đủ vì tương lai degree/connectivity chưa biết.

tĩnh Hierholzer giả định đồ thị đã biết. động Eulerian maintenance là problem khác, thường cần maintain degree parity/connectivity và chưa chắc cho phép emit final route incrementally đơn giản.

## 30. kiểm thử

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

Trên đồ thị nhỏ, brute-force quay lui (backtracking) over cạnh IDs có thể làm oracle để verify existence/đường đi của Hierholzer.

## 31. Phổ biến cách triển khai failures

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

Một cách triển khai trả route ngắn hơn `E+1` thường là dấu hiệu đồ thị không thỏa các giả định hoặc traversal bỏ sót thành phần/cạnh.

## Mô hình tư duy

> Eulerian reasoning là **flow balance của các cạnh qua các đỉnh**. Intermediate đỉnh cần ghép cạnh vào với cạnh ra; đồ thị vô hướng biểu hiện bằng parity, đồ thị có hướng biểu hiện bằng cân bằng bậc vào/bậc ra.

Khi balance + connectivity đúng, Hierholzer biến cục bộ cạnh consumption thành toàn cục route bằng reverse finishing/splicing. Đây là lý do Eulerian problems có linear-time structure đẹp trong khi các bài Hamilton đi qua đỉnh không có cùng tính chất.

Xem thêm: [Graph Modeling](./00_graph_modeling_and_representation.md), [Bridges](./06_bridges_articulation_and_biconnectivity.md), [Network Flow](./08_network_flow_and_matching.md).