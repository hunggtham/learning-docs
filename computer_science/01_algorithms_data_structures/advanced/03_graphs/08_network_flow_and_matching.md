# Network Flow và Bipartite Matching
**Network Flow & Bipartite Matching / 네트워크 플로우와 이분 매칭**

Network flow mô hình hóa một lượng tài nguyên di chuyển qua mạng có giới hạn. “Tài nguyên” ở đây không nhất thiết là nước hay dữ liệu; nó có thể là số job được phân cho worker, số đơn hàng đi qua tuyến vận chuyển, số connection qua network, hay đơn giản là một abstraction toán học dùng để giải matching và cut problems.

Sức mạnh của flow không nằm ở việc mô phỏng chất lỏng, mà ở chỗ rất nhiều bài toán “phân phối dưới constraints” có thể được biến thành một graph với capacities.

## 1. Flow network là gì?

Ta có directed graph với một **source** `s`, một **sink** `t`, và mỗi edge `(u,v)` có capacity `c(u,v) >= 0`.

Một flow `f(u,v)` hợp lệ phải thỏa capacity constraint:

\[
0 \le f(u,v) \le c(u,v)
\]

và flow conservation tại mọi vertex trung gian:

\[
\sum_{u} f(u,v) = \sum_{w} f(v,w)
\]

Nói đơn giản: trừ source và sink, vertex không tự tạo hoặc làm mất flow.

Giá trị của flow là lượng flow rời source, tương đương lượng đi vào sink nếu conservation đúng.

## 2. Max-flow problem

**Maximum flow** hỏi lượng flow lớn nhất có thể gửi từ `s` đến `t` mà vẫn tôn trọng capacities.

Một cách nghĩ naive là liên tục tìm path từ source tới sink rồi đẩy nhiều nhất có thể. Nhưng nếu ta chỉ khóa quyết định cũ và không cho phép sửa, greedy path choice có thể làm kẹt solution dưới optimum.

Điểm đột phá là **residual graph**.

## 3. Residual graph: khả năng sửa quyết định cũ

Giả sử edge `u -> v` có capacity 10 và hiện đã gửi flow 6. Forward residual capacity còn 4.

Nhưng residual graph còn có reverse edge `v -> u` capacity 6. Reverse residual edge không có nghĩa hệ thống vật lý thật có đường ngược; nó biểu diễn khả năng **hủy bớt flow đã gửi trước đó**.

Nếu sau này tìm ra route tốt hơn, algorithm có thể đi qua reverse residual edge để “rút lại” quyết định cũ rồi redirect capacity sang nơi khác.

Đây là mental model quan trọng nhất của network flow:

> residual graph là graph của **những thay đổi còn có thể thực hiện trên solution hiện tại**.

## 4. Augmenting path

Một **augmenting path** là path từ `s` đến `t` trong residual graph mà mọi edge có residual capacity dương.

Ta có thể tăng flow theo path đó một lượng bằng bottleneck nhỏ nhất:

\[
\Delta = \min_{e \in path} c_{residual}(e)
\]

Sau đó giảm residual capacity forward và tăng reverse residual capacity tương ứng.

Quá trình lặp lại cho tới khi không còn augmenting path.

## 5. Ford–Fulkerson là framework, không phải một path strategy duy nhất

Ford–Fulkerson mô tả ý tưởng augmenting-path tổng quát. Nếu capacities nguyên, mỗi augmentation tăng flow ít nhất 1, nên algorithm kết thúc. Nhưng runtime có thể phụ thuộc mạnh vào path được chọn và magnitude của capacities.

Nếu capacities không nguyên hoặc dùng floating-point thiếu kiểm soát, behavior lý thuyết trở nên phức tạp hơn. Vì vậy trong DSA/contest, capacities integer là setting phổ biến.

Ford–Fulkerson giúp hiểu residual graph, nhưng khi cần polynomial bound rõ ràng hoặc performance thực tế, ta thường dùng strategy cụ thể hơn.

## 6. Edmonds–Karp

Edmonds–Karp chọn augmenting path bằng BFS, tức shortest path theo số edges trong residual graph.

Runtime bound:

\[
O(VE^2)
\]

Bound này không đến từ việc mỗi BFS nhanh hơn DFS, mà từ structural property: shortest residual distance từ source không giảm theo thời gian, và mỗi critical saturation event chỉ có thể xảy ra hữu hạn lần ở mỗi distance layer.

Edmonds–Karp rất tốt để học correctness và residual mechanics vì implementation đơn giản, dù thường chậm hơn Dinic cho graph lớn.

## 7. Dinic's algorithm

Dinic chạy theo phases. Mỗi phase dùng BFS tạo **level graph**, trong đó chỉ giữ residual edges đi từ level `d` sang `d+1`. Sau đó DFS gửi một **blocking flow** cho tới khi không còn `s-t` path trong level graph.

Sau một blocking-flow phase, shortest residual path từ `s` đến `t` phải dài hơn. Nhờ đó số phases bị giới hạn.

General bound thường được trình bày là:

\[
O(V^2E)
\]

với nhiều lớp graph đặc biệt có bound tốt hơn. Trong competitive programming và nhiều workload vừa phải, Dinic là lựa chọn thực dụng vì khá nhanh và implementation vẫn manageable.

## 8. Current-arc optimization

Trong DFS của Dinic, nếu một outgoing edge của vertex đã được thử và không còn khả năng gửi flow trong phase hiện tại, không nên scan lại edge đó từ đầu mỗi lần.

Ta giữ một pointer `ptr[v]` tới edge tiếp theo cần thử. Đây gọi là current-arc optimization.

Một optimization nhỏ ở representation này rất quan trọng vì nếu cứ rescan adjacency list, implementation có thể chậm đi đáng kể dù Big-O high-level không đổi nhiều trong cách nhìn đơn giản.

## 9. Max-flow min-cut theorem

Một **cut** chia vertices thành hai tập `S` và `T`, với `s in S`, `t in T`. Capacity của cut là tổng capacity của edges đi từ `S` sang `T`.

Bất kỳ flow nào cũng không thể vượt capacity của bất kỳ cut nào, vì mọi flow từ source sang sink phải “băng qua” cut.

Max-flow min-cut theorem nói:

\[
\max flow = \min cut capacity
\]

Đây là một theorem mạnh vì nối hai góc nhìn khác nhau: một bên cố **đẩy nhiều nhất**, bên kia tìm **bottleneck nhỏ nhất**.

Khi residual graph không còn path từ `s` tới `t`, tập vertices reachable từ `s` trong residual graph tạo phía `S` của một minimum cut. Điều này đồng thời cung cấp certificate rằng flow hiện tại đã optimal.

## 10. Tại sao min-cut hữu ích ngoài flow?

Min-cut có thể mô hình hóa segmentation, partitioning, connectivity robustness và selection với pairwise penalties trong một số formulations.

Điểm quan trọng là theorem cho ta một dual perspective: thay vì hỏi “gửi được bao nhiêu”, có thể hỏi “cần cắt tổng capacity nhỏ nhất bao nhiêu để ngăn mọi route từ s tới t”. Hai bài nhìn khác nhau nhưng có cùng optimum value.

## 11. Bipartite matching

Một graph bipartite chia vertices thành hai phía `L` và `R`, edges chỉ nối từ một phía sang phía kia. Matching là tập edges không chia sẻ endpoint.

Ví dụ: workers ở `L`, jobs ở `R`, edge tồn tại nếu worker có thể làm job. Maximum matching hỏi có thể ghép được nhiều worker-job pairs nhất bao nhiêu.

Ta chuyển sang flow bằng network:

```text
source -> mỗi L node      capacity 1
L node -> R node          capacity 1 nếu edge matching tồn tại
mỗi R node -> sink        capacity 1
```

Vì mỗi left/right node chỉ có capacity 1 qua source/sink, không vertex nào có thể được match hơn một lần. Integral capacities đảm bảo tồn tại maximum integral flow, nên mỗi unit flow qua `L -> R` tương ứng một matched pair.

## 12. Integrality property

Nếu tất cả capacities là integers, Ford–Fulkerson-style augmentations với integer bottlenecks duy trì integer flow. Do đó max-flow có thể đạt một integral optimum.

Property này rất quan trọng cho matching, vì ta không muốn “0.4 worker” match với một job. Flow formulation vẫn cho ra discrete assignment tự nhiên.

Đây là một ví dụ đẹp về cách continuous-looking flow equations vẫn giải bài combinatorial discrete khi capacities integer.

## 13. Hopcroft–Karp

Nếu bài chỉ là unweighted bipartite maximum matching, generic max-flow thường không phải cách tốt nhất.

Hopcroft–Karp khai thác cấu trúc bipartite để tìm nhiều shortest augmenting paths theo batches. Complexity:

\[
O(E\sqrt{V})
\]

Ý tưởng high-level tương tự Dinic ở chỗ BFS tạo layers rồi DFS tìm augmenting paths phù hợp. Nhưng representation và proof được specialize cho matching.

Bài học lớn hơn: general reduction giúp hiểu problem, nhưng structure đặc biệt có thể cho specialized algorithm tốt hơn.

## 14. Matching khác assignment problem có cost

Maximum bipartite matching chỉ tối đa số cặp. Nếu mỗi worker-job pair có cost/profit và cần tối ưu tổng cost, đó là weighted assignment hoặc min-cost matching.

Hungarian algorithm giải assignment matrix cổ điển. **Min-Cost Max-Flow** mở rộng flow bằng cost trên edges và tối ưu cost trong khi gửi flow.

Không nên dùng plain max-flow nếu objective thật sự chứa cost.

## 15. Vertex capacity và node splitting

Flow capacity mặc định nằm trên edges. Nếu một vertex chỉ được phép xử lý tối đa `k` units, ta có thể **split vertex** thành `v_in` và `v_out`, nối edge:

```text
v_in -> v_out capacity k
```

Mọi incoming edge đi vào `v_in`, mọi outgoing edge đi ra từ `v_out`.

Kỹ thuật này biến vertex constraint thành edge capacity constraint. Đây là một reduction pattern rất thường gặp.

Tương tự, nếu muốn vertex-disjoint paths, node splitting với capacity 1 giúp giới hạn mỗi intermediate vertex chỉ dùng một lần.

## 16. Edge-disjoint paths

Nếu mỗi edge có capacity 1, max flow từ `s` tới `t` cho biết số edge-disjoint paths tối đa trong setting phù hợp.

Mỗi unit integral flow có thể decomposed thành paths. Đây là connection giữa flow và connectivity.

Theo Menger-type reasoning, maximum number of disjoint paths có liên hệ sâu với minimum cut size.

## 17. Super source và super sink

Nếu bài có nhiều sources hoặc nhiều sinks, ta có thể tạo **super source** nối tới các sources thật, và **super sink** nhận edges từ các sinks thật.

Capacity của các artificial edges đặt theo supply/demand hoặc đủ lớn tùy model.

Kỹ thuật này cho phép chuẩn hóa nhiều problem phức tạp về single-source single-sink flow.

## 18. Lower bounds và circulation

Một số edges không chỉ có upper capacity mà còn yêu cầu minimum flow `l(u,v)`. Đây là flow with lower bounds/circulation problem.

Ta có thể chuyển bằng cách đặt residual capacity mới `c-l`, đồng thời điều chỉnh demand/balance tại endpoints. Sau đó thêm super source/sink để kiểm tra feasibility.

Phần này cho thấy flow là framework rộng hơn “max flow từ s tới t”; nó có thể mô hình hóa conservation với supplies, demands và mandatory minimums.

## 19. Min-cost flow

Khi mỗi edge có cost trên mỗi unit flow, objective có thể là gửi required amount với minimum total cost hoặc tìm min-cost max-flow.

Residual graph lúc này có reverse edge với **negative cost** tương ứng, vì hủy một unit flow cũ sẽ hoàn lại cost đã trả.

Các algorithm phổ biến dùng shortest augmenting paths với potentials để tránh negative reduced costs và cho phép Dijkstra. Đây là bước nối network flow với shortest path theory.

## 20. Implementation pattern bằng reverse-edge index

Một representation phổ biến lưu mỗi edge object/struct với:

```text
to
capacity
reverseIndex
```

Khi add edge `u -> v` capacity `c`, ta đồng thời add reverse edge `v -> u` capacity 0. Hai edges giữ index trỏ qua nhau.

Khi gửi `delta`:

```text
forward.cap -= delta
reverse.cap += delta
```

Representation này tránh phải tìm reverse edge bằng search, giúp update `O(1)`.

## 21. Overflow và capacity type

Nếu capacities lớn hoặc tổng flow có thể vượt 32-bit, Java nên dùng `long`, C dùng kiểu integer đủ rộng, JavaScript cần kiểm tra `Number.MAX_SAFE_INTEGER` hoặc dùng `BigInt` nếu thực sự cần exact integer lớn.

Một overflow âm thầm có thể làm residual capacity sai và phá toàn bộ invariant.

## 22. Testing network flow

Ngoài sample, nên kiểm tra các properties. Flow trên mỗi edge phải nằm trong bounds. Conservation phải đúng ở mọi vertex trừ source/sink. Reported flow phải bằng net outgoing source.

Sau max-flow, lấy vertices reachable từ source trong residual graph, tính capacity của cut trong original graph; nó phải bằng max-flow value. Đây là một test cực mạnh vì kiểm tra cả primal và cut certificate.

Với bipartite matching, không left/right vertex nào được xuất hiện trong hai matched edges và matching size phải bằng flow.

## 23. Common mistakes

Lỗi rất phổ biến là quên reverse residual edge hoặc update reverse capacity sai. Khi đó algorithm mất khả năng sửa quyết định cũ và có thể dừng ở flow không tối ưu.

Một lỗi khác là dùng original capacity thay vì residual capacity trong traversal. Cũng cần tránh reuse level graph cũ sau khi residual network thay đổi.

Trong Dinic, BFS phải chỉ đi qua edges residual capacity > 0. DFS cũng phải tôn trọng level condition.

## 24. Production/system connections

Flow abstraction xuất hiện trong bandwidth allocation, traffic engineering, supply chain, scheduling và resource assignment. Tuy nhiên production systems thường thêm latency, stochastic demand, fairness, multi-commodity constraints hoặc dynamic changes, khiến pure single-commodity max-flow chỉ là một layer của model.

Dù vậy, học flow vẫn rất giá trị vì nó dạy cách biến constraints thành capacities và dùng residual state để cho phép optimization “undo” quyết định trước đó.

## Mental Model

> Network flow không phải greedy path filling. Nó là quá trình liên tục cải thiện một feasible solution trong **residual graph**, nơi reverse capacity cho phép sửa quá khứ.

Max-flow min-cut theorem cho biết khi không còn cách cải thiện, ta đồng thời có một certificate tối ưu: một cut có capacity đúng bằng flow. Matching, disjoint paths, vertex capacities và assignment variants đều có thể được hiểu như các reductions xoay quanh cùng conservation/capacity framework.

Xem thêm: [Graph Traversal](./01_graph_traversal_bfs_dfs.md), [Shortest Paths](./02_shortest_paths.md), [Hard Problems & Reductions](../04_algorithmic_paradigms/09_hard_problems_reductions_and_approximation.md).