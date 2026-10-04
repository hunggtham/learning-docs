# Network flows, matching và max-flow min-cut: tối ưu trên mạng có capacity

> **Mạch đọc:** Chapter này đi sau [Graph Theory](./00_graph_theory.md) và [Linear Programming & Duality](../08_optimization_numerical/05_linear_programming_duality_and_simplex.md). Graph theory trả lời “ai nối với ai”; network flow thêm một câu hỏi mới: **mỗi connection có thể chuyên chở bao nhiêu và toàn hệ thống có thể đẩy bao nhiêu từ source tới sink?**

Một graph thông thường chỉ giữ connectivity. Nhưng nhiều hệ thực tế còn có **capacity (dung lượng / 용량)**:

```text
road      → vehicles/hour
pipe      → liters/second
network   → packets/second
warehouse → units/day
API path  → requests/second
```

Vì vậy tồn tại path chưa đủ. Một route có thể tồn tại nhưng bottleneck của nó quá nhỏ để đáp ứng demand.

Network flow biến graph thành optimization problem.

---

## 1. Flow network

Một **mạng luồng (flow network / 유량 네트워크)** thường là directed graph

```math
G=(V,E)
```

với:

- source `s`;
- sink `t`;
- capacity `c(u,v)≥0` trên mỗi edge.

Một **flow (유량)** `f(u,v)` phải thỏa hai loại constraints.

### Capacity constraint

```math
0\le f(u,v)\le c(u,v).
```

Ta không thể gửi nhiều hơn edge chịu được.

### Flow conservation

Với mọi intermediate vertex `v` khác `s,t`:

```math
\sum_u f(u,v)
=
\sum_w f(v,w).
```

Amount đi vào phải bằng amount đi ra nếu node không tạo hoặc tiêu thụ commodity.

---

## 2. Value của flow

Total flow rời source:

```math
|f|
=
\sum_v f(s,v).
```

Nếu conservation đúng, lượng này bằng total flow đi vào sink.

**Maximum-flow problem (최대 유량 문제)** hỏi:

```text
Trong tất cả feasible flows,
flow value lớn nhất là bao nhiêu?
```

Đây là optimization trên graph.

---

## 3. Bottleneck không nhất thiết là edge nhỏ nhất toàn graph

Giả sử có hai parallel routes:

```text
s → A → t     capacities 5, 5
s → B → t     capacities 8, 8
```

Ta có thể gửi total:

```math
5+8=13.
```

Edge capacity nhỏ nhất là 5 nhưng max flow là 13.

Vì vậy “tìm bottleneck edge nhỏ nhất” là sai mental model.

Network throughput phụ thuộc cách capacities tương tác qua **cuts** và alternative routes.

---

## 4. Residual graph: phần capacity còn có thể thay đổi

Giả sử edge `(u,v)` có capacity `10` và đang carry flow `6`.

Forward residual capacity:

```math
c_f(u,v)=10-6=4.
```

Nhưng residual graph còn có reverse edge `(v,u)` capacity `6`.

Tại sao?

Vì algorithm phải có khả năng **undo/reroute** một phần quyết định trước đó.

Nếu ta đã gửi 6 units qua `u→v`, reverse residual edge cho phép “rút lại” tối đa 6 units để dùng capacity theo cách khác.

Đây là insight quan trọng:

> Greedy local flow assignment có thể sai; residual network giữ freedom để sửa quyết định cũ.

---

## 5. Augmenting path

Một **augmenting path (증가 경로)** là path từ `s` tới `t` trong residual graph với positive residual capacity trên mọi edge.

Amount có thể augment bằng minimum residual capacity trên path:

```math
\Delta
=
\min_{e\in P}c_f(e).
```

Đây là bottleneck của **path hiện tại**.

Ta tăng flow theo forward residual edges và giảm flow nếu đi qua reverse residual edges.

Lặp process:

```text
find augmenting path
→ compute path bottleneck
→ augment flow
→ update residual graph
→ repeat
```

là core của Ford–Fulkerson framework.

---

## 6. Ford–Fulkerson: algorithm từ local improvement

Pseudo-flow:

```text
f = 0
while residual graph contains s→t path:
    P = one augmenting path
    Δ = minimum residual capacity on P
    augment f by Δ along P
return f
```

Nếu capacities là integers, mỗi augmentation tăng flow ít nhất 1, nên process terminate.

Tuy nhiên path-selection strategy ảnh hưởng performance. Edmonds–Karp chọn shortest augmenting path theo number of edges bằng BFS và có polynomial-time guarantee.

Điểm sâu hơn runtime:

> Residual graph biến một optimization problem global thành sequence của local corrections nhưng vẫn giữ khả năng undo.

Pattern này tái xuất hiện trong optimization, matching và min-cost flow.

---

## 7. Cut là certificate của upper bound

Một **s–t cut (컷)** chia vertices thành hai sets:

```math
S\cup T=V,
\qquad
S\cap T=\varnothing,
```

với

```math
s\in S,
\qquad
t\in T.
```

Capacity của cut:

```math
c(S,T)
=
\sum_{u\in S,v\in T}c(u,v).
```

Mọi flow từ source sang sink phải cross từ `S` sang `T`, nên:

```math
|f|\le c(S,T)
```

cho mọi feasible flow.

Cut vì vậy là **upper-bound certificate**.

---

## 8. Max-flow min-cut theorem

Theorem trung tâm:

```math
\max_f |f|
=
\min_{(S,T)} c(S,T).
```

Nói bằng lời:

> throughput lớn nhất có thể gửi qua network bằng đúng capacity của bottleneck cut nhỏ nhất.

Điều này rất mạnh vì nó nối hai object khác nhau:

```text
primal object: actual flow
        ↕ equality
certificate: cut capacity
```

Nếu ta tìm một flow value 23 và một cut capacity 23, không cần search thêm: flow đó optimal.

Đây là discrete version rất đẹp của **duality (đối ngẫu / 쌍대성)**.

---

## 9. Vì sao no augmenting path dẫn tới min cut?

Khi algorithm dừng, residual graph không còn path `s→t`.

Gọi `S` là set vertices reachable từ `s` trong residual graph; `T` là phần còn lại.

Vì `t` không reachable:

```math
s\in S,
\qquad
t\in T.
```

Mọi original edge từ `S` sang `T` phải saturated; nếu còn residual capacity thì endpoint bên `T` sẽ reachable.

Các relevant reverse conditions cũng bảo đảm không có net flow “sai hướng” phá equality.

Từ đó flow value bằng capacity của cut `(S,T)`.

Algorithm không chỉ tìm solution; trạng thái residual cuối cùng tự tạo **proof of optimality**.

---

## 10. Integrality theorem

Nếu mọi capacities là integers, tồn tại maximum flow với integer flows trên mọi edges.

Đây là property rất quan trọng vì nhiều combinatorial problems cần 0/1 decisions chứ không muốn “0.37 người” hay “2.4 jobs”.

Network flow có special polyhedral structure khiến linear optimization cho integer solution trong nhiều cases mà không cần generic integer programming.

Đây là bridge sang linear programming và total unimodularity.

---

## 11. Bipartite matching thành flow problem

Cho bipartite graph với left set `L`, right set `R`.

Muốn tìm maximum matching.

Construct network:

```text
source s
  ↓ capacity 1
left vertices L
  ↓ capacity 1 on original bipartite edges
right vertices R
  ↓ capacity 1
sink t
```

Mỗi integer unit flow correspond với một matched edge.

Capacity `1` bảo đảm mỗi vertex được match tối đa một lần.

Do integrality:

```text
maximum flow value
=
maximum matching size.
```

Đây là example điển hình của modeling:

> Một combinatorial problem có vẻ riêng biệt trở thành network-flow problem sau khi chọn representation đúng.

---

## 12. Hall's marriage theorem

Cho bipartite graph `G=(L,R,E)`.

Một matching cover toàn bộ `L` tồn tại iff với mọi subset `X⊆L`:

```math
|N(X)|\ge |X|,
```

trong đó `N(X)` là neighbors của `X` trong `R`.

Interpretation:

> Bất kỳ nhóm `k` left vertices nào cũng phải có ít nhất `k` possible right partners.

Nếu 5 tasks chỉ có 3 eligible workers tổng cộng, perfect assignment impossible trước khi chạy algorithm nào.

Hall condition là structural feasibility theorem; max-flow algorithm là computational mechanism.

---

## 13. Matching applications

Matching xuất hiện trong:

- job ↔ worker assignment;
- student ↔ project allocation;
- organ donor ↔ recipient compatibility;
- request ↔ server matching;
- ad ↔ slot assignment;
- course ↔ classroom scheduling components;
- entity resolution candidates.

Không phải mọi assignment problem là plain bipartite matching. Nếu có costs, preferences, capacities >1 hoặc time constraints, model cần min-cost flow, b-matching, stable matching hoặc integer programming.

---

## 14. Max flow khác shortest path

Shortest path hỏi:

```text
Một unit đi từ s đến t theo route rẻ/ngắn nhất nào?
```

Max flow hỏi:

```text
Tổng bao nhiêu units có thể đi đồng thời qua toàn network?
```

Một shortest path có thể đi qua narrow edge và không phản ánh system throughput.

Trong networking:

```text
latency optimization ≠ throughput optimization
```

Hai objective có thể conflict.

---

## 15. Max flow khác minimum spanning tree

MST minimize total cost để connect mọi vertices.

Max flow maximize transferable quantity giữa designated `s,t`.

MST thường undirected connectivity problem; max flow thường directed-capacity problem.

Không nên dùng “graph algorithm” như một category đồng nhất. Mỗi algorithm giải một optimization objective khác nhau.

---

## 16. Min-cost flow

Nếu edge ngoài capacity còn có per-unit cost `w(u,v)`, ta có thể hỏi:

```text
send required amount of flow
with minimum total cost
```

Objective:

```math
\min
\sum_{(u,v)\in E}
w(u,v)f(u,v).
```

subject to capacity/conservation constraints.

Min-cost flow model transportation, supply chains, assignment, routing và scheduling tốt hơn plain max flow khi quantity alone không đủ.

---

## 17. Multi-source / multi-sink reduction

Nếu có nhiều sources, ta có thể thêm **super-source** nối tới từng source.

Nếu có nhiều sinks, thêm **super-sink**.

Điều này là example của reduction:

```text
richer problem
→ add artificial structure
→ solve canonical problem
```

Reduction là một trong những kỹ năng trung tâm của algorithms/discrete mathematics.

---

## 18. Vertex capacity

Standard max flow đặt capacity trên edges. Nếu vertex `v` chỉ xử lý tối đa `k` units, split node:

```text
v_in → v_out
```

với capacity `k` trên internal edge.

Mọi incoming edges đi vào `v_in`; outgoing edges rời `v_out`.

Một modeling trick đơn giản biến node constraint thành edge constraint.

---

## 19. Edge-disjoint paths

Nếu mỗi edge capacity bằng `1`, max-flow value từ `s` tới `t` tương ứng maximum number of edge-disjoint paths.

Điều này nối flow với network resilience:

```text
nhiều edge-disjoint routes
→ khó disconnect hơn khi một edge fail
```

Menger-type theorems formalize relation giữa disjoint paths và minimum cuts.

Connectivity ở đây không còn chỉ binary “connected/not connected”; ta đo **độ dư thừa (redundancy / 중복성)** của connectivity.

---

## 20. Reliability và capacity planning

Trong production systems, một graph có path từ service A tới database không chứng minh capacity đủ.

Ta cần phân biệt:

```text
reachability
capacity
latency
failure probability
queueing behavior
```

Network flow lý tưởng hóa nhiều yếu tố, nhưng cung cấp baseline:

- bottleneck cuts ở đâu?
- capacity nào cần tăng?
- một edge upgrade có thực sự tăng global throughput không?

Upgrade một edge không nằm trên any minimum cut có thể không thay maximum throughput.

---

## 21. Flow decomposition

Mọi feasible flow có thể decomposed thành:

- flows dọc các `s→t` paths;
- cộng thêm circulations quanh cycles.

Điều này giúp hiểu flow không phải một mysterious global object. Nó là superposition của path movements và cycles.

Cycle flow không tăng source-to-sink value, nên trong many contexts có thể remove mà vẫn giữ same total throughput.

---

## 22. Connection với linear programming

Max flow có thể viết như LP.

Variables:

```math
f_e
```

cho mỗi edge.

Constraints:

```math
0\le f_e\le c_e
```

và linear conservation equations.

Objective:

```math
\max |f|.
```

Min-cut đóng vai trò dual structure.

Vì vậy max-flow min-cut không phải isolated graph trick; nó là một concrete, highly structured instance của optimization duality.

Đọc cùng [Linear programming, duality và simplex](../08_optimization_numerical/05_linear_programming_duality_and_simplex.md).

---

## 23. Connection với database / distributed systems

Flow viewpoint hữu ích như abstraction trong software systems:

```text
API gateway
→ services
→ queues
→ workers
→ databases
```

Mỗi component có capacity. Bottleneck có thể là một cut gồm nhiều resources chứ không phải single machine.

Tuy nhiên real distributed systems có queueing, retries, burst traffic, backpressure và correlated failures. Static max-flow model không tự mô tả time-dependent congestion.

Mental discipline:

> Dùng graph flow để hiểu structural capacity trước; dùng queueing/stochastic/system models để hiểu temporal behavior sau.

---

## 24. Common misconceptions

**“Max flow là sum capacities rời source.”** Không nhất thiết; downstream cut có thể nhỏ hơn.

**“Một augmenting path đã chọn sai thì algorithm hỏng.”** Residual reverse edges cho phép reroute previous flow.

**“Min cut là edge nhỏ nhất.”** Cut là một partition và có thể chứa nhiều edges.

**“Matching chỉ là greedy ghép từng pair.”** Greedy có thể block better global matching.

**“Nếu graph connected thì throughput cao.”** Connectivity không nói capacity.

**“Mọi flow problem cho integer answer.”** Integrality guarantee phụ thuộc structure và integer capacities; general LP không có guarantee integer như vậy.

---

## 25. Mental model

> Network flow là conservation + capacity trên graph. Residual graph giữ khả năng sửa quyết định; augmenting path tăng solution; cut tạo upper bound; max-flow min-cut theorem nói solution và certificate gặp nhau tại cùng một value. Matching, assignment và disjoint-path problems trở nên dễ hiểu khi ta nhìn chúng như flow với carefully chosen capacities.

---

## 26. Mạch học tiếp

```text
Graph theory
→ Network flows
→ Matching
→ Linear programming duality
→ Min-cost flow / assignment
→ Operations research
```

hoặc cho software/system reasoning:

```text
Graph reachability
→ Capacity / cuts
→ Queueing & stochastic processes
→ Distributed-system bottlenecks
```

Đọc tiếp:

- [Generating functions và advanced counting](./11_generating_functions_and_advanced_counting.md)
- [Optimization](../08_optimization_numerical/00_optimization.md)
- [Linear programming và duality](../08_optimization_numerical/05_linear_programming_duality_and_simplex.md)
- [Stochastic processes, Markov chains và time series](../06_probability_statistics/11_stochastic_processes_markov_chains_and_time_series.md)

## Further reading

- Mitchel T. Keller, William T. Trotter — *Applied Combinatorics*, chapters on Network Flows and Combinatorial Applications of Network Flows.
