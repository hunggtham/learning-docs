# Luồng mạng và ghép cặp hai phía
**Network Flow & Bipartite Matching / 네트워크 플로우와 이분 매칭**

Luồng mạng mô hình hóa việc phân phối một đại lượng qua các tuyến có giới hạn. “Đại lượng” có thể là hàng hóa, lưu lượng mạng, job được gán cho worker, đơn vị hàng hóa đi qua chuỗi cung ứng hoặc chỉ là một đại lượng toán học giúp biến một bài toán tổ hợp thành bài toán luồng.

Sức mạnh của mô hình flow không nằm ở ẩn dụ chất lỏng, mà ở việc nhiều bài toán “phân phối dưới ràng buộc” có thể được biểu diễn thống nhất bằng:

```text
đỉnh
cạnh
sức chứa
nguồn / đích
bảo toàn
```

Một khi mô hình đúng, cùng một bộ định lý và thuật toán có thể giải matching, cut, đường đi rời nhau, phân công, circulation và nhiều bài toán chọn tập có cấu trúc.

## 1. Định nghĩa một flow hợp lệ

Ta có đồ thị có hướng, nguồn `s`, đích `t` và sức chứa `c(u,v) >= 0`.

Flow `f(u,v)` phải thỏa:

\[
0\le f(u,v)\le c(u,v)
\]

và tại mọi đỉnh trung gian:

\[
\sum_x f(x,v)=\sum_y f(v,y)
\]

Điều kiện thứ hai là **bảo toàn luồng (flow conservation)**: đỉnh trung gian không tự sinh hoặc làm mất tài nguyên.

Giá trị luồng bằng tổng luồng rời nguồn, đồng thời bằng tổng luồng đi vào đích nếu bảo toàn đúng.

## 2. Max Flow

Bài toán **luồng cực đại (maximum flow)** tìm giá trị flow lớn nhất có thể gửi từ `s` tới `t` mà không vượt sức chứa.

Một chiến lược tham lam ngây thơ “chọn đường rồi khóa luôn quyết định” có thể thất bại vì đường chọn sớm có thể chiếm capacity cần cho lời giải tốt hơn.

Ý tưởng giải quyết vấn đề này là **đồ thị dư (residual graph)**.

## 3. Đồ thị dư là không gian các thay đổi còn có thể thực hiện

Nếu cạnh `u -> v` có capacity 10 và hiện đang mang flow 6:

```text
forward residual capacity = 4
reverse residual capacity = 6
```

Cạnh ngược không nhất thiết tồn tại trong mạng vật lý. Nó biểu diễn khả năng **rút lại** một phần quyết định cũ để chuyển luồng sang đường khác.

Mô hình tư duy quan trọng nhất:

> Residual graph không mô tả mạng gốc; nó mô tả **không gian những chỉnh sửa khả thi trên lời giải hiện tại**.

Đây là lý do augmenting-path algorithm có thể sửa sai lựa chọn trước đó thay vì bị kẹt bởi quyết định greedy.

## 4. Đường tăng và bottleneck

Một **đường tăng (augmenting path)** là đường từ `s` tới `t` trong residual graph mà mọi cạnh đều còn dung lượng dư dương.

Ta có thể tăng luồng một lượng:

\[
\Delta=\min_{e\in path} c_{residual}(e)
\]

Sau đó cập nhật forward/reverse residual capacities.

Nếu không còn augmenting path, flow hiện tại không thể được cải thiện bằng bất kỳ thay đổi hợp lệ nào trong residual graph.

## 5. Ford–Fulkerson là một khung thuật toán

Ford–Fulkerson chỉ nói:

```text
while còn augmenting path:
    tìm một augmenting path
    đẩy bottleneck flow
```

Cách chọn path quyết định complexity thực tế.

Với capacity nguyên, mỗi augmentation tăng giá trị flow ít nhất 1 nên thuật toán kết thúc. Với capacity lớn, số augmentation có thể phụ thuộc vào magnitude của capacity chứ không chỉ kích thước đồ thị.

Với số thực, các vấn đề hội tụ lý thuyết còn tinh tế hơn. Vì vậy implementation DSA thường dùng capacity nguyên hoặc kiểu số có ngữ nghĩa rõ ràng.

## 6. Edmonds–Karp

Edmonds–Karp chọn augmenting path ngắn nhất theo số cạnh bằng BFS.

Complexity cổ điển:

\[
O(VE^2)
\]

Điều đáng học không phải chỉ công thức mà là lý do: khoảng cách BFS trong residual graph từ nguồn tới các đỉnh không giảm qua các augmentation phù hợp, và mỗi cạnh chỉ có thể trở thành bottleneck ở một tầng nhất định hữu hạn lần.

Edmonds–Karp rất tốt để học correctness và residual mechanics, nhưng thường chậm hơn Dinic trên đồ thị lớn.

## 7. Dinic

Dinic chạy theo các pha:

1. BFS xây **level graph**;
2. chỉ giữ residual edge đi từ level `d` sang `d+1`;
3. DFS đẩy **blocking flow** cho đến khi không còn đường `s -> t` trong level graph đó;
4. xây level graph mới.

Sau mỗi blocking-flow phase, độ dài đường residual ngắn nhất từ `s` tới `t` tăng.

Cận tổng quát thường được trình bày là:

\[
O(V^2E)
\]

nhưng nhiều lớp đồ thị đặc biệt có cận tốt hơn.

Trong thực hành, Dinic thường là lựa chọn cân bằng giữa hiệu năng và độ phức tạp implementation.

## 8. Current-Arc Optimization

Trong DFS của Dinic, nếu một cạnh đã được thử hết trong phase hiện tại, không nên quét lại từ đầu.

Ta giữ:

```text
ptr[v] = cạnh tiếp theo cần thử của v
```

Optimization này không thay đổi ý tưởng toán học nhưng giảm đáng kể việc quét lặp adjacency list.

Đây là ví dụ DSA quan trọng: cùng một thuật toán lý thuyết nhưng cách tổ chức trạng thái phụ có thể quyết định hiệu năng implementation.

## 9. Max-Flow Min-Cut

Một cut chia các đỉnh thành `S` và `T`, với `s∈S`, `t∈T`.

Dung lượng cut:

\[
c(S,T)=\sum_{u\in S,v\in T} c(u,v)
\]

Mọi flow từ `s` sang `t` phải đi qua cut, nên:

\[
|f|\le c(S,T)
\]

Định lý max-flow min-cut nói:

\[
\max flow = \min cut
\]

Khi residual graph không còn đường từ `s` tới `t`, tập đỉnh còn reachable từ `s` trong residual graph chính là phía `S` của một min-cut tương ứng.

Flow hiện tại và cut này tạo ra **certificate tối ưu**: cận dưới và cận trên gặp nhau.

## 10. Duality intuition

Max-flow hỏi: “đẩy được bao nhiêu?”. Min-cut hỏi: “cần chặn tổng sức chứa nhỏ nhất bao nhiêu để tách nguồn và đích?”.

Hai bài nhìn khác nhau nhưng có cùng giá trị tối ưu.

Đây là một ví dụ trực quan của **đối ngẫu (duality)** trong tối ưu hóa: lời giải primal và một certificate dual có thể xác nhận tính tối ưu lẫn nhau.

## 11. Bipartite Matching như một bài flow

Với hai phía `L` và `R`:

```text
source -> L        capacity 1
L -> R             capacity 1 nếu có cạnh matching
R -> sink          capacity 1
```

Mỗi unit flow qua một cạnh `L -> R` tương ứng với một cặp được ghép.

Capacity 1 ở nguồn và đích đảm bảo một đỉnh không được dùng trong hai cặp.

## 12. Integrality

Nếu capacity đều nguyên, tồn tại max flow nguyên.

Tính chất này rất quan trọng: flow equations nhìn giống bài liên tục, nhưng với mạng matching capacity nguyên, lời giải tự nhiên cho ra số cặp nguyên thay vì “0.3 worker”.

Tính nguyên của flow là cầu nối giữa tối ưu liên tục kiểu đại số và bài toán tổ hợp rời rạc.

## 13. Augmenting Path trong matching

Trong matching, augmenting path luân phiên giữa:

```text
cạnh chưa nằm trong matching
cạnh đang nằm trong matching
```

và bắt đầu/kết thúc ở hai đỉnh chưa ghép.

Flip trạng thái của các cạnh trên path làm matching tăng thêm đúng 1 cạnh.

Đây chính là phiên bản matching của residual-path reasoning.

## 14. Hopcroft–Karp

Với maximum bipartite matching không trọng số, Hopcroft–Karp khai thác cấu trúc đặc biệt tốt hơn generic flow.

Complexity:

\[
O(E\sqrt V)
\]

BFS tìm tầng của các augmenting path ngắn nhất, rồi DFS tìm nhiều augmenting path vertex-disjoint trong cùng phase.

Ý tưởng gần Dinic nhưng chuyên biệt hơn.

Bài học tổng quát:

> Reduction về bài tổng quát giúp hiểu cấu trúc; nếu miền có thêm bất biến đặc biệt, thuật toán chuyên biệt có thể nhanh hơn.

## 15. Hall’s Theorem

Với bipartite graph `G=(L,R,E)`, tồn tại matching phủ mọi đỉnh của `L` khi và chỉ khi với mọi tập con `S⊆L`:

\[
|N(S)|\ge |S|
\]

Trực giác: mọi nhóm `S` bên trái phải có ít nhất đủ số hàng xóm bên phải để ghép riêng cho từng phần tử.

Hall’s theorem là characterization mang tính cấu trúc, còn matching algorithm là thủ tục xây dựng lời giải.

Đây là một ví dụ đẹp cho mối quan hệ giữa **định lý tồn tại** và **thuật toán xây dựng**.

## 16. Vertex Cover và Kőnig’s Theorem

Trong bipartite graph:

\[
|maximum\ matching| = |minimum\ vertex\ cover|
\]

Đây là Kőnig’s theorem.

Sau khi có maximum matching, có thể xây minimum vertex cover bằng traversal trên alternating graph theo quy tắc phù hợp.

Đây là một ví dụ khác của primal/dual certificate trong bài toán rời rạc.

## 17. Node Splitting

Nếu capacity nằm ở đỉnh thay vì cạnh, tách:

```text
v_in -> v_out  capacity = cap(v)
```

Mọi cạnh vào nối tới `v_in`, mọi cạnh ra xuất phát từ `v_out`.

Kỹ thuật này chuyển vertex constraint thành edge constraint.

Ứng dụng:

```text
vertex-disjoint paths
giới hạn số job qua một server
resource capacity tại nút trung gian
```

## 18. Edge-Disjoint và Vertex-Disjoint Paths

Nếu mỗi cạnh có capacity 1, max flow cho số đường `s-t` không dùng chung cạnh lớn nhất trong mô hình phù hợp.

Nếu cần không dùng chung đỉnh, dùng node splitting với capacity 1 cho các đỉnh trung gian.

Điều này liên hệ chặt với Menger’s theorem: số đường rời nhau cực đại và kích thước cut tối thiểu phản ánh cùng một cấu trúc kết nối.

## 19. Nhiều nguồn và nhiều đích

Thêm **super source** nối tới các nguồn thật và **super sink** nối từ các đích thật.

Capacity của cạnh nhân tạo phải đủ lớn hoặc bằng giới hạn cung/cầu tương ứng.

Kỹ thuật này biến nhiều nguồn/đích về đúng dạng single-source single-sink của max-flow chuẩn.

## 20. Circulation

Circulation bỏ yêu cầu nguồn/đích duy nhất và yêu cầu bảo toàn flow tại mọi đỉnh. Cạnh có thể có lower/upper bounds.

Đây là mô hình tự nhiên cho:

```text
phân phối cung-cầu
quota tối thiểu/tối đa
lịch phân công với ràng buộc
```

Circulation feasibility thường được reduce về max-flow bằng cách điều chỉnh lower bounds và tạo super source/sink.

## 21. Lower Bounds trên cạnh

Nếu cạnh yêu cầu:

\[
l(u,v)\le f(u,v)\le c(u,v)
\]

ta có thể gửi trước `l(u,v)`, giảm capacity còn lại thành `c-l`, rồi điều chỉnh balance của hai endpoint.

Sau đó thêm super source/sink để bù các nhu cầu dư/thiếu.

Đây là một kỹ thuật reduction mạnh: biến constraint “ít nhất” thành preflow cố định và bài feasibility còn lại.

## 22. Min-Cost Flow

Nếu mỗi đơn vị flow trên cạnh có cost, ta cần tối ưu tổng chi phí bên cạnh lượng flow.

Một dạng:

```text
maximize flow trước
trong các max-flow, minimize total cost
```

hoặc gửi chính xác `K` đơn vị với chi phí nhỏ nhất.

Min-Cost Max-Flow thường dùng residual graph với **chi phí cạnh ngược âm** để biểu diễn khả năng hoàn tác quyết định cũ.

Shortest augmenting path với potential/reduced cost là một cách triển khai phổ biến.

## 23. Negative Cost và Potential

Residual reverse edge của một cạnh cost `w` có cost `-w`, vì hoàn tác một đơn vị flow thu lại chi phí đã trả.

Điều này tạo cạnh âm. Ta có thể dùng Bellman–Ford ban đầu hoặc potential để biến reduced cost thành không âm rồi chạy Dijkstra trong các vòng sau.

Đây là ví dụ flow kết nối trực tiếp với shortest-path theory.

## 24. Assignment Problem

Nếu cần ghép mọi worker với job và mỗi cặp có cost, bài toán assignment có thể giải bằng Hungarian algorithm hoặc min-cost flow tùy cấu trúc.

Maximum matching chỉ tối đa hóa số cặp; nó không tự tối ưu tổng lợi ích.

Phải phân biệt objective:

```text
maximum cardinality
maximum weight
minimum cost perfect matching
```

Các bài nhìn giống nhau nhưng cần mô hình khác.

## 25. B-Matching và Capacity > 1

Nếu một worker có thể nhận nhiều job hoặc một resource có quota `b(v)`, matching chuẩn capacity 1 không đủ.

Có thể tăng capacity trên cạnh nguồn/đích hoặc dùng b-matching formulation phù hợp.

Đây là ví dụ đơn giản cho thấy matching chỉ là một trường hợp đặc biệt của flow với capacity 1.

## 26. Flow Decomposition

Một integral flow có thể phân rã thành tập các đường từ nguồn tới đích và chu trình.

Trong nhiều bài application, giá trị max-flow chưa đủ; ta cần chính các assignment/path cụ thể. Khi đó cần duyệt các cạnh có flow dương để reconstruct.

Nếu API cần route cụ thể, output semantics phải được thiết kế ngay từ đầu.

## 27. Capacity Scaling

Một số thuật toán tăng hiệu năng bằng cách ưu tiên các residual edge có capacity lớn trước, rồi giảm ngưỡng theo lũy thừa của 2.

Ý tưởng **scaling** xuất hiện ở nhiều thuật toán tối ưu hóa: giải bài thô trước ở mức giá trị lớn, sau đó tinh chỉnh.

Không phải implementation max-flow nào cũng cần scaling, nhưng đây là pattern thiết kế đáng nhận diện.

## 28. Push–Relabel

Push–Relabel không tìm augmenting path hoàn chỉnh ở mỗi bước. Nó duy trì một **preflow** cho phép đỉnh trung gian tạm thời có excess, cùng nhãn chiều cao `h(v)`.

Thao tác chính:

```text
push      -> đẩy excess qua admissible edge
relabel   -> tăng height khi không còn admissible edge
```

Mô hình tư duy khác hoàn toàn Ford–Fulkerson nhưng vẫn giải cùng max-flow problem.

Trong một số graph lớn/dày, Push–Relabel rất cạnh tranh.

## 29. Min-Cut trong bài chọn tập

Một số bài có cost chọn/bỏ đỉnh và penalty nếu hai lựa chọn không nhất quán có thể reduce về s-t min-cut.

Mẫu thường gặp:

```text
source edge  -> cost của một lựa chọn
sink edge    -> cost của lựa chọn đối lập
pair edge    -> penalty khi tách hai biến
```

Cut chọn một phía cho mỗi node và tổng capacity bị cắt chính là objective.

Đây là nền tảng của nhiều formulation trong computer vision và energy minimization với điều kiện phù hợp.

## 30. Khi Flow là quá nặng

Không nên dùng max-flow chỉ vì “bài có assignment”.

Nếu chỉ cần matching bipartite, Hopcroft–Karp đơn giản và nhanh hơn. Nếu assignment matrix có trọng số đặc biệt, Hungarian có thể phù hợp. Nếu chỉ cần connectivity, DSU/DFS rẻ hơn rất nhiều.

Flow là công cụ tổng quát; sức mạnh tổng quát thường đi cùng implementation và constant factor lớn hơn.

## 31. Độ phức tạp phải gắn với lớp đồ thị

Một complexity formula không nói hết câu chuyện.

Cần xét:

```text
V, E
sparse hay dense
capacity magnitude
unit capacity hay arbitrary capacity
bipartite hay general
integer hay real
số augmentation thực tế
```

Cùng Dinic có thể rất nhanh trên unit network nhưng kém hơn một lựa chọn khác trên graph dày hoặc application đặc biệt.

## 32. Overflow

Tổng flow có thể vượt 32-bit dù từng capacity nhỏ. Cost * flow còn dễ vượt hơn.

Nên chọn kiểu số dựa trên cận toán học, không theo kiểu của input riêng lẻ.

Trong Java thường cần `long`; trong C cần kiểu nguyên đủ rộng và kiểm tra overflow khi nhân/cộng cost.

## 33. Biểu diễn Residual Edge

Một pattern phổ biến là mỗi edge lưu index của reverse edge:

```text
Edge { to, capacity, rev }
```

Khi đẩy `delta`:

```text
forward.cap -= delta
reverse.cap += delta
```

Bất biến cực kỳ quan trọng:

> forward và reverse edge phải luôn tham chiếu đúng cặp của nhau.

Lỗi reverse-index là một trong những bug implementation max-flow phổ biến nhất.

## 34. Validator cho Flow

Sau khi thuật toán chạy, có thể kiểm tra:

```text
0 <= flow <= capacity
flow conservation ở mọi đỉnh trung gian
value out of source == value into sink
không còn augmenting path nếu dùng augmenting algorithm
```

Để xác minh optimality mạnh hơn, xây min-cut từ residual reachability và kiểm tra:

\[
flowValue = cutCapacity
\]

Đây là validator rất mạnh vì dùng theorem độc lập với đường chạy cụ thể của thuật toán.

## 35. Differential Testing

Với graph nhỏ, có thể:

```text
so Dinic với Edmonds–Karp
so matching-flow với brute-force matching
so min-cut với enumerate mọi partition nhỏ
```

Random graph + oracle chậm là cách rất hiệu quả để phát hiện bug reverse edge, level graph, ptr hoặc capacity update.

## 36. Những trường hợp biên

Cần thử:

```text
s == t theo hợp đồng API
không có đường s-t
parallel edges
self-loop
capacity 0
capacity rất lớn
nhiều min-cut khác nhau
nhiều maximum matching khác nhau
graph disconnected
node splitting với source/sink đặc biệt
```

Parallel edge thường hoàn toàn hợp lệ trong flow; implementation adjacency phải giữ từng edge riêng hoặc gộp capacity có chủ đích.

## 37. Mô hình hóa quan trọng hơn chọn thuật toán

Nhiều bug flow không nằm trong Dinic mà nằm trong graph construction:

```text
capacity đặt sai phía
quên capacity 1 trong matching
source/sink nối sai
lower-bound balance sai dấu
node splitting bỏ sót cạnh
```

Một max-flow implementation hoàn hảo trên một network model sai vẫn trả lời sai bài toán.

## Mô hình tư duy

> Network flow là một ngôn ngữ để mô hình hóa **phân phối tài nguyên dưới các ràng buộc**, còn residual graph là ngôn ngữ của **những thay đổi còn có thể thực hiện trên lời giải hiện tại**.

Khi nhận ra một bài có tính chất “mỗi đối tượng có capacity/quota, phải phân phối sao cho bảo toàn và tối ưu tổng lượng/chi phí”, hãy thử nghĩ theo flow. Sau đó hỏi: **bài có cấu trúc đặc biệt để dùng matching/Hungarian/DSU thay vì generic flow không, cần cardinality hay cost, capacity nằm ở cạnh hay đỉnh, và có thể tạo certificate min-cut để kiểm chứng tính tối ưu hay không?**

Xem thêm: [Graph Modeling](./00_graph_modeling_and_representation.md), [Shortest Paths](./02_shortest_paths.md), [Union-Find](./05_union_find.md), [Hard Problems & Reductions](../04_algorithmic_paradigms/09_hard_problems_reductions_and_approximation.md).