# Eulerian Paths và Cycles
**Đường đi Euler và chu trình Euler / Eulerian Path & Cycle / 오일러 경로와 회로**

Bài toán Eulerian hỏi một câu rất cụ thể: **có thể đi qua mỗi edge đúng một lần hay không?** Đây là bài toán về edge usage, khác bản chất với Hamiltonian path, nơi mục tiêu là thăm mỗi vertex đúng một lần.

Sự khác biệt này cực kỳ quan trọng. Eulerian path/cycle có characterization bằng degree và có thể xây trong thời gian tuyến tính theo kích thước graph. Hamiltonian path nói chung lại thuộc nhóm bài toán khó hơn rất nhiều. Hai bài nhìn giống nhau ở bề mặt nhưng cấu trúc toán học hoàn toàn khác.

## 1. Từ bài toán Königsberg đến graph model

Nguồn gốc kinh điển của Eulerian reasoning là bài toán các cây cầu ở Königsberg: liệu có thể đi qua mỗi cây cầu đúng một lần hay không. Khi bỏ hình dạng địa lý và chỉ giữ land regions thành vertices, bridges thành edges, bài toán trở thành graph problem.

Insight quan trọng là hình học cụ thể không còn cần thiết. Điều quyết định là mỗi vertex có bao nhiêu edge incident và graph có connected hay không. Đây là một ví dụ lịch sử rất rõ về **abstraction**: loại bỏ chi tiết domain để giữ cấu trúc quyết định bài toán.

## 2. Eulerian path, Eulerian trail và Eulerian cycle

Trong nhiều tài liệu, **Eulerian trail/path** là một walk sử dụng mỗi edge đúng một lần. Nếu điểm bắt đầu và kết thúc giống nhau, đó là **Eulerian circuit/cycle**.

Vertex có thể xuất hiện nhiều lần. Điều bị cấm lặp là edge. Đây là chỗ dễ nhầm với simple path.

Nếu graph có 10 edges, một Eulerian trail phải dùng đúng 10 edges. Số vertex xuất hiện trong route có thể lớn hơn số vertex khác nhau vì cùng vertex có thể được quay lại nhiều lần.

## 3. Điều kiện trong undirected graph

Bỏ qua các isolated vertices có degree 0, phần graph chứa edges phải connected.

Eulerian cycle tồn tại khi **mọi vertex có degree chẵn**.

Eulerian path nhưng không phải cycle tồn tại khi **đúng hai vertices có degree lẻ**. Hai vertex lẻ này bắt buộc là start và end.

Nếu số vertex degree lẻ khác 0 hoặc 2, Eulerian trail không tồn tại.

### Vì sao parity quyết định?

Hãy nhìn một vertex trung gian trên route. Mỗi lần route đi vào vertex qua một unused edge, nó phải đi ra qua một unused edge khác. Hai edge này ghép thành một cặp. Vì vậy mọi edge incident ở intermediate vertex phải ghép cặp được, dẫn tới degree chẵn.

Start của open Euler trail có thể có một edge “đi ra” không được ghép với edge “đi vào”, còn end có một edge “đi vào” không có edge “đi ra”. Vì vậy hai endpoints có degree lẻ.

Đây không chỉ là mẹo nhớ; nó là proof intuition của degree condition.

## 4. Connectivity không được bỏ qua

Có thể mọi vertex đều degree chẵn nhưng graph gồm hai component tách rời, mỗi component có edges. Không có một trail duy nhất đi qua edges của cả hai component vì ta không thể teleport giữa chúng.

Do đó degree condition là cần nhưng chưa đủ. Ta phải kiểm tra connectivity trên subgraph gồm các vertex có degree > 0.

Một graph không có edge thường được xử lý như case đặc biệt tùy API/problem statement. Nếu chỉ hỏi có Eulerian cycle hay không, empty edge set có thể được coi là trivial; nhưng implementation phải xác định semantics rõ ràng.

## 5. Directed graph: cân bằng indegree và outdegree

Trong directed graph, mỗi lần đi vào vertex qua một directed edge, ta cần một outgoing edge để tiếp tục. Vì vậy điều kiện không còn là parity mà là balance.

Eulerian cycle yêu cầu với mọi relevant vertex:

```text
indegree(v) == outdegree(v)
```

và các edges phải nằm trong connectivity structure phù hợp.

Eulerian path mở có thể có đúng một start thỏa:

```text
outdegree = indegree + 1
```

và đúng một end thỏa:

```text
indegree = outdegree + 1
```

các vertex còn lại phải cân bằng.

### Connectivity trong directed graph

Với cycle, một cách phát biểu mạnh là các vertex có nonzero degree phải thuộc cùng strongly connected component khi xét khả năng đi theo directed edges phù hợp. Trong implementation contest phổ biến, người ta cũng có thể kiểm tra connectivity của underlying undirected graph kết hợp degree-balance conditions cho Eulerian trail/cycle theo theorem thích hợp.

Điểm quan trọng là không được chỉ kiểm tra indegree/outdegree rồi kết luận. Degree balance không nối các component lại với nhau.

## 6. Hierholzer's algorithm: ý tưởng cốt lõi

Giả sử graph thỏa điều kiện Euler. Bắt đầu từ một vertex hợp lệ và liên tục đi qua unused edge cho tới khi không còn edge để đi tiếp.

Nếu đang tìm cycle và mọi degree cân bằng đúng, route cục bộ này sẽ quay về nơi bắt đầu. Nhưng có thể vẫn còn unused edges ở một vertex đã xuất hiện trong cycle. Khi đó ta bắt đầu một cycle mới từ vertex đó rồi **splice** cycle mới vào cycle cũ.

Hierholzer cho thấy một Eulerian cycle lớn có thể được xây bằng cách ghép các cycle nhỏ.

Một implementation rất tiện dùng stack. Ta đi sâu bằng unused edges. Khi một vertex không còn edge unused, ta pop nó và append vào output. Vì append diễn ra khi “quay lui”, output cuối phải reverse.

## 7. Vì sao thuật toán đúng?

Khi một vertex được đưa vào output, nghĩa là tất cả edge còn khả dụng từ vertex đó đã được tiêu thụ. Ta không còn cần quay lại để mở rộng route từ nó.

Trong graph thỏa Euler conditions, việc đi theo unused edge không thể “phá hỏng” solution vĩnh viễn theo kiểu greedy dead-end thông thường, vì balance/parity đảm bảo structure cho phép splice các phần route lại.

Residual unused edges nếu tồn tại phải nối với một vertex trên route đã có, nếu phần graph có edges connected. Vì vậy ta có thể tiếp tục tour từ đó và ghép vào.

## 8. Complexity và representation

Nếu mỗi edge được xử lý constant number of times, Hierholzer chạy:

\[
O(V+E)
\]

hoặc thực tế gần `O(E)` sau khi adjacency structure đã được xây.

Nhưng representation quyết định bạn có thực sự đạt bound đó hay không. Nếu mỗi lần tìm unused edge lại scan toàn adjacency list từ đầu, edge có thể bị xem lại nhiều lần. Một kỹ thuật phổ biến là giữ pointer/index hiện tại cho mỗi vertex hoặc pop edges khỏi adjacency list.

Với undirected graph, mỗi logical edge xuất hiện hai lần trong adjacency lists. Vì vậy nên gắn **edge id** và một `used[edgeId]` flag để đảm bảo edge chỉ được tiêu thụ một lần.

## 9. JavaScript implementation bằng edge IDs

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

  return path.reverse();
}
```

Nếu graph connected theo phần edges và start được chọn đúng, path trả về phải có `edges.length + 1` vertices. Đây là một postcondition rất hữu ích để phát hiện graph không thỏa assumptions hoặc implementation bỏ sót edge.

## 10. Chọn start vertex đúng

Trong undirected graph có Eulerian cycle, có thể bắt đầu tại bất kỳ vertex có degree > 0. Nếu graph có exactly two odd-degree vertices, phải bắt đầu ở một trong hai vertex lẻ.

Trong directed graph có open Euler trail, start phải là vertex có `outdegree = indegree + 1`. Nếu tất cả cân bằng, chọn bất kỳ vertex có outgoing edge.

Start sai có thể khiến traversal kết thúc sớm dù graph có Eulerian trail hợp lệ.

## 11. Multigraph, parallel edges và self-loops

Eulerian algorithms phải xử lý được parallel edges. Vì vậy đánh dấu edge bằng cặp `(u,v)` là không đủ; hai edges khác nhau có thể nối cùng hai vertices. Edge ID là representation an toàn hơn.

Self-loop đóng góp 2 vào degree trong undirected graph vì nó vừa đi ra vừa quay vào cùng vertex. Trong directed graph, self-loop đóng góp 1 indegree và 1 outdegree. Nó không phá balance.

Những chi tiết này là lý do nên reason từ graph definitions thay vì dựa vào trực giác hình vẽ.

## 12. Eulerian vs Hamiltonian

Eulerian problem quan tâm mỗi **edge** đúng một lần và có characterization degree rõ ràng. Hamiltonian problem quan tâm mỗi **vertex** đúng một lần và nói chung không có local degree condition đơn giản để giải quyết toàn bài.

Một graph có thể Eulerian nhưng không Hamiltonian, hoặc ngược lại. Đừng dùng DFS “thử mọi đường” cho Eulerian problem nếu degree theorem + Hierholzer giải được tuyến tính.

## 13. De Bruijn graph và sequence reconstruction

Một connection rất quan trọng là **de Bruijn graph**. Giả sử có nhiều substrings/k-mers và muốn ghép lại một sequence. Có thể biểu diễn prefix/suffix overlap thành vertices và mỗi fragment thành edge. Khi đó reconstruct sequence tương ứng với việc tìm Eulerian path qua mỗi fragment edge đúng một lần.

Ý tưởng này xuất hiện trong bioinformatics và cả các bài tạo shortest string chứa mọi pattern độ dài cố định.

Trong de Bruijn sequence construction, vertices có thể là strings độ dài `k-1`, edges là strings độ dài `k`. Một Eulerian cycle đi qua mọi edge đúng một lần cho ta sequence chứa mọi k-length pattern đúng theo cấu trúc cần thiết.

## 14. Route planning và Chinese Postman connection

Nếu một người giao thư phải đi qua **mỗi edge ít nhất một lần** và muốn tổng cost nhỏ nhất, đó là Chinese Postman Problem. Nếu graph đã Eulerian, answer chính là Eulerian cycle. Nếu không, ta cần duplicate một số edges tối ưu để biến degree conditions thành Eulerian rồi mới traverse.

Connection này cho thấy Eulerian theory là building block của routing, không chỉ một bài graph isolated.

## 15. Euler tour trên tree là khái niệm liên quan nhưng khác

Trong tree algorithms, cụm “Euler tour” đôi khi chỉ traversal sequence ghi lại thời điểm enter/exit node, dùng để flatten tree thành array cho subtree query. Đây không nhất thiết là Eulerian path theo nghĩa “mỗi graph edge đúng một lần”.

Tên gọi gần nhau có thể gây nhầm. Khi đọc tài liệu, phải nhìn semantics cụ thể: edge-covering trail hay DFS traversal encoding.

## 16. Các lỗi implementation phổ biến

Một lỗi phổ biến là xóa phần tử đầu adjacency list bằng operation có cost cao như `shift()` trong JavaScript, khiến complexity thực tế xấu đi. Tốt hơn dùng pointer hoặc pop cuối.

Một lỗi khác là với undirected graph, đánh dấu chỉ một bản sao adjacency entry mà không đánh dấu edge đối diện. Edge IDs giải quyết vấn đề này.

Cũng cần kiểm tra connectivity của vertices có edge, chọn start hợp lệ và xác nhận route cuối sử dụng đủ `E` edges.

## Mental Model

> Eulerian reasoning là reasoning về **flow của edge qua vertex**. Mỗi intermediate visit cần một edge vào và một edge ra, nên undirected graph xuất hiện parity còn directed graph xuất hiện indegree/outdegree balance.

Khi degree/balance và connectivity đúng, Hierholzer không cần thử mọi khả năng. Nó sử dụng structure của graph để xây route trong thời gian tuyến tính, cho thấy một characterization toán học tốt có thể biến bài toán tưởng như combinatorial search thành một traversal đơn giản.

Xem thêm: [Graph Modeling](./00_graph_modeling_and_representation.md), [BFS/DFS](./01_graph_traversal_bfs_dfs.md), [Network Flow](./08_network_flow_and_matching.md).