# Lý thuyết đồ thị: toán học của quan hệ, đường đi và cấu trúc mạng

Lý thuyết đồ thị (Graph Theory / 그래프 이론) nghiên cứu những systems mà điều quan trọng không phải tọa độ tuyệt đối của objects, mà là **objects nào được nối với objects nào**. Khi ta quan tâm đến dependency, reachability, route, hierarchy, cycle, neighborhood hoặc connectivity, graph thường là abstraction tự nhiên nhất.

Một road network, social network, package dependency graph, workflow, finite-state machine, database relationship network hay knowledge graph đều có thể rất khác nhau về domain, nhưng cùng chia sẻ một structure: nodes và relationships.

> Graph bỏ bớt geometry để giữ lại topology của quan hệ: ai nối với ai, đi từ đâu tới đâu, và những paths/cycles nào tồn tại.

## Graph bắt đầu từ abstraction nào?

Một graph thường được viết

```math
G=(V,E),
```

trong đó `V` là set các vertices/nodes và `E` là set các edges.

Nếu graph vô hướng (Undirected Graph / 무방향 그래프), edge giữa `u` và `v` có thể viết `{u,v}`. Relation “friendship” thường gần kiểu này: nếu A là bạn của B thì B cũng là bạn của A.

Nếu graph có hướng (Directed Graph / 방향 그래프), edge `(u,v)` đi từ `u` sang `v`. “A follows B” hoặc “module A depends on B” là directed relation.

Graph model không tự nói node hoặc edge “thật sự là gì”. Ta quyết định semantics theo problem. Đây là sức mạnh của abstraction nhưng cũng là nguồn rủi ro: nếu edge definition không đúng business/physical meaning, algorithm đúng trên graph vẫn có thể trả lời sai question thực tế.

## Simple graph, multigraph và self-loop

Trong simple undirected graph, thường không có multiple edges giữa cùng pair và không có self-loop. Nhưng nhiều systems cần richer model.

Một airline network có thể có nhiều flights giữa cùng hai airports, nên multigraph hợp lý. State machine có thể có self-loop khi state chuyển về chính nó. Network flow có directed edges với capacities.

Trước khi dùng theorem hoặc algorithm, cần biết graph model cho phép gì. Một property đúng cho simple graph có thể không translate nguyên xi sang multigraph.

## Degree: local connectivity của một node

Trong undirected graph, degree `deg(v)` là số incident edges tại vertex `v`.

Một identity cơ bản là Handshake Lemma:

```math
\sum_{v\in V}\deg(v)=2|E|.
```

Lý do không nằm ở algebra phức tạp: mỗi edge có hai endpoints, nên khi cộng degree của mọi vertices, mỗi edge được count đúng hai lần.

Một consequence là số vertices có odd degree luôn even. Vì tổng degree là số chẵn, tổng của một odd number lượng odd không thể tạo số chẵn.

Trong directed graph, ta phân biệt in-degree và out-degree. Tổng in-degree bằng tổng out-degree và đều bằng số directed edges:

```math
\sum_v \deg^-(v)=\sum_v\deg^+(v)=|E|.
```

## Walk, trail, path và cycle

Trong informal discussion, mọi sequence nodes connected bởi edges thường được gọi “path”, nhưng graph theory phân biệt kỹ hơn.

Một walk có thể lặp vertices và edges. Trail không lặp edges. Simple path không lặp vertices. Cycle là closed path trở về điểm bắt đầu mà không lặp intermediate vertices theo standard simple definition.

Distinctions này quan trọng khi nói về Euler path, Hamiltonian path, shortest path hoặc cycle detection.

## Connectivity: có đi tới được không?

Undirected graph connected nếu mọi pair vertices có path nối chúng. Nếu không, graph chia thành connected components.

Trong directed graph, có hai notions quan trọng:

- strongly connected: từ mọi vertex đi tới mọi vertex khác theo direction;
- weakly connected: nếu bỏ direction, underlying undirected graph connected.

Trong distributed systems hoặc microservice dependency graph, “có path” không đồng nghĩa “request chắc chắn thành công”. Graph connectivity chỉ nói structure cho phép route tồn tại trong model; latency, capacity, authorization và failures là properties khác.

## Trees: connectivity tối thiểu không có cycle

Một tree (Tree / 트리) là connected undirected graph không có cycles.

Với `n` vertices, tree có

```math
|E|=n-1.
```

Có nhiều cách hiểu property này. Một tree connected nhưng “just connected enough”: remove bất kỳ edge nào thì graph disconnect; add một edge mới giữa hai existing vertices thì tạo đúng một cycle.

Đó là lý do tree là structure tự nhiên cho hierarchy. Mỗi child có route unique tới root nếu ta orient edges theo parent-child relation.

File systems, DOM, syntax trees và many indexes dùng tree. Nhưng Git commit history nói chung là DAG chứ không strict tree vì merge commit có thể có nhiều parents.

## Spanning tree: giữ connectivity, bỏ redundancy cycles

Cho connected graph `G`, spanning tree chứa tất cả vertices nhưng chỉ giữ subset edges đủ để graph vẫn connected và acyclic.

Mọi spanning tree với `n` vertices có `n-1` edges.

Trong network design, nếu goal chỉ là maintain connectivity với minimum number edges, spanning tree là natural object. Nhưng nếu edges có costs, ta cần minimum spanning tree.

## Minimum spanning tree

Cho weighted undirected graph, minimum spanning tree (MST) tìm spanning tree với total edge weight nhỏ nhất.

Kruskal's algorithm sort edges theo weight và thêm edge nếu không tạo cycle. Prim's algorithm grow một connected tree bằng cheapest edge crossing từ visited sang unvisited side.

Điểm cốt lõi là **cut property**: với một cut của vertices thành hai groups, lightest edge crossing cut có thể là safe choice dưới conditions chuẩn. Đây là structural reason greedy algorithms đúng, không chỉ là “chọn edge nhỏ nhất vì nghe hợp lý”.

MST không giải shortest paths giữa một source và mọi nodes. Hai problems khác nhau: MST minimize total tree cost; shortest-path tree minimize source-to-node distances.

## Directed acyclic graph và dependency

DAG (Directed Acyclic Graph / 방향 비순환 그래프) là directed graph không có directed cycles.

Dependencies thường muốn DAG structure vì cycle có thể làm “phải hoàn thành A trước B, B trước C, C trước A” trở thành impossible ordering.

Topological ordering là sequence vertices sao cho mọi edge

```math
u\to v
```

đặt `u` trước `v`.

Topological order tồn tại **iff** directed graph là DAG.

Build systems, package resolution, course prerequisites và workflow scheduling đều dùng idea này. Nhiều valid topological orders có thể tồn tại; algorithm không nhất thiết trả unique ordering.

## Graph representation: adjacency list và adjacency matrix

Mathematical graph là abstract object. Software phải chọn representation.

Adjacency matrix `A` với `n` vertices dùng roughly

```math
O(n^2)
```

space. Edge lookup `A_{ij}` thường `O(1)`.

Adjacency list lưu neighbors cho từng vertex. Với sparse graph, space roughly

```math
O(|V|+|E|).
```

Iteration qua neighbors hiệu quả hơn nhiều.

Choice phụ thuộc graph density và operations. Dense linear-algebra workloads có thể thích matrix representation; large sparse networks thường dùng adjacency lists hoặc compressed sparse formats.

Representation là engineering decision, không phải graph-theory definition.

## BFS: shortest number of edges bằng layer expansion

Breadth-First Search (BFS / 너비 우선 탐색) bắt đầu từ source và khám phá graph theo layers.

Layer 0 là source. Layer 1 gồm neighbors trực tiếp. Layer 2 gồm unvisited nodes reachable qua hai edges, và tiếp tục như vậy.

Vì toàn bộ nodes ở distance `d` được discover trước nodes ở distance `d+1`, BFS tìm shortest path theo **number of edges** trong unweighted graph.

Với adjacency list, complexity là

```math
O(|V|+|E|),
```

vì mỗi vertex được visited bounded number times và adjacency entries được scan bounded number times.

### Vì sao BFS không trực tiếp đúng cho weighted graph?

BFS coi mọi edge có same cost. Nếu một direct edge cost 100 nhưng route qua ba edges cost 1+1+1=3, “fewer edges” không còn đồng nghĩa “shorter cost”. Khi weights khác nhau, cần algorithm phù hợp như Dijkstra hoặc Bellman–Ford.

## DFS: đi sâu để lộ structure

Depth-First Search (DFS / 깊이 우선 탐색) đi sâu theo một branch cho tới khi không còn unvisited neighbor rồi backtrack.

DFS tạo discovery/finish structure hữu ích cho:

- connected components;
- cycle detection;
- topological sorting;
- articulation-like reasoning;
- strongly connected component algorithms.

Recursive implementation tự nhiên nhưng deep graph có thể vượt call-stack limit. Explicit stack thường an toàn hơn trong production systems.

## Dijkstra: shortest path khi weights nonnegative

Dijkstra's algorithm duy trì tentative distance từ source. Mỗi bước chọn unsettled vertex có tentative distance nhỏ nhất và “settle” nó.

Tại sao greedy step đúng? Với nonnegative edge weights, bất kỳ alternate path đi qua một unsettled vertex khác phải có cost ít nhất bằng current smallest tentative distance trước khi cộng thêm nonnegative cost. Vì vậy settled distance không thể được cải thiện sau đó.

Core relaxation operation là:

```math
\text{if }d[u]+w(u,v)<d[v],\text{ then update }d[v].
```

Với priority queue, common complexity là approximately

```math
O((|V|+|E|)\log|V|)
```

cho standard sparse implementation.

### Tại sao negative weight phá Dijkstra?

Nếu negative edge tồn tại, một vertex đã settle có thể về sau nhận route rẻ hơn thông qua negative edge. Greedy invariant bị phá.

Bellman–Ford relax mọi edges repeatedly và xử lý negative weights, đồng thời detect negative cycles reachable từ source.

Negative cycle nghĩa shortest path có thể không finite: đi vòng cycle mỗi lần làm cost giảm thêm.

## Floyd–Warshall và all-pairs shortest paths

Nếu cần shortest path giữa mọi pair vertices trong dense graph nhỏ/vừa, Floyd–Warshall dùng dynamic programming:

```math
D_{ij}^{(k)}=
\min\left(D_{ij}^{(k-1)},D_{ik}^{(k-1)}+D_{kj}^{(k-1)}\right).
```

Interpretation: shortest path từ `i` đến `j` khi cho phép intermediate vertices trong set đầu `k` nodes hoặc không dùng `k`, hoặc đi qua `k`.

Complexity

```math
O(|V|^3)
```

không phù hợp huge sparse graphs nhưng rất elegant cho dense all-pairs problems.

## Strongly connected components

Trong directed graph, strongly connected component (SCC) là maximal set vertices mà mọi pair reach each other.

Nếu collapse mỗi SCC thành một super-node, condensation graph luôn là DAG. Đây là deep structural fact: mọi directed graph có thể được nhìn như DAG của strongly connected regions.

Compiler analysis, dependency diagnostics và state-transition systems dùng SCC để tìm mutually recursive/dependent groups.

## Bipartite graph và matching

Graph bipartite nếu vertices chia được thành hai sets `L,R` sao cho edges chỉ nối giữa hai sets.

Equivalent structural property: undirected graph bipartite iff không có odd cycle.

Bipartite matching model assignment problems như workers ↔ tasks, students ↔ projects, applicants ↔ positions.

Maximum matching tìm largest set edges không share endpoints. Weighted versions dẫn tới assignment optimization.

Đây là ví dụ graph theory chuyển trực tiếp thành operations research.

## Graph coloring: conflict dưới dạng adjacency

Vertex coloring gán colors sao cho adjacent vertices khác color.

Nếu edge biểu diễn “hai tasks conflict”, coloring partition tasks thành groups không conflict. Exam scheduling và register allocation có graph-coloring flavor.

Minimum number colors cần gọi chromatic number. General coloring problem computationally hard; graph structure cụ thể có thể cho efficient algorithms.

Graph theory vì thế không chỉ nói “có path không”, mà còn model constraints.

## Euler và Hamilton: hai loại “đi qua tất cả” rất khác

Euler path/trail quan tâm đi qua every edge exactly once. Hamiltonian path quan tâm visit every vertex exactly once.

Euler path có characterization local rất đẹp trong undirected connected graph: number odd-degree vertices phải là 0 hoặc 2 tùy circuit/path case.

Hamiltonian path không có criterion đơn giản tương tự và liên quan computationally difficult problems.

Hai concepts trông giống nhưng structure khác hẳn — một warning tốt rằng wording gần nhau không có nghĩa algorithmic difficulty gần nhau.

## Graph matrices và linear algebra

Adjacency matrix đưa graph vào linear algebra. Nếu `A` là adjacency matrix của unweighted graph, entries của

```math
A^k
```

liên quan số walks length `k` giữa vertices.

Graph Laplacian thường định nghĩa

```math
L=D-A,
```

trong đó `D` là degree matrix.

Eigenvalues/eigenvectors của Laplacian encode connectivity và smooth variation trên graph. Spectral clustering, graph signal processing và many network methods dựa trên bridge graph theory ↔ linear algebra.

## Random walks và Markov chains trên graph

Nếu từ node hiện tại ta chọn next node theo transition probabilities trên outgoing edges, ta có random walk trên graph.

Transition matrix tạo Markov chain. Long-run behavior liên quan eigenvectors/eigenvalues và stationary distributions.

PageRank có thể nhìn như random walk với teleportation/damping. Connection này cho thấy search ranking không phải “graph heuristic thuần túy”; nó dựa trên probability + linear algebra trên graph.

## Network flow: capacity thay đổi question

Trong routing hoặc logistics, việc có path chưa đủ; edges có capacities.

Max-flow problem hỏi maximum amount có thể gửi từ source `s` tới sink `t` mà không vượt capacity và phải satisfy flow conservation.

Max-flow min-cut theorem nói maximum flow value bằng capacity của minimum `s-t` cut.

Đây là một theorem mạnh vì nối optimization toàn cục với một structural bottleneck: throughput tối đa bị quyết định bởi weakest separating cut.

## Graph trong software engineering

Graph abstraction xuất hiện ở nhiều layer:

Call graph: node là function/method; edge là call relation.

Dependency graph: package/module nào phụ thuộc module nào.

Control-flow graph: basic blocks và possible execution transitions.

State graph: application/game/protocol states và transitions.

Database schema graph: tables/entities và relationships.

Knowledge graph: entities và typed relations.

Git commit graph: commits và parent links tạo DAG trong normal history.

Cùng algorithms về reachability, cycle detection, topological ordering, components hoặc shortest paths có thể reuse vì underlying structure giống nhau.

## Modeling matters hơn algorithm name

Giả sử tìm “đường tốt nhất” trên road network. Nếu edge weight là distance, shortest path trả route ngắn nhất về km. Nếu weight là expected travel time, result khác. Nếu congestion phụ thuộc thời gian, static weight graph có thể không đủ. Nếu toll + time là multi-objective, một scalar weight đơn giản có thể che trade-off.

Algorithm chỉ optimize quantity mà model đưa vào.

> Một graph algorithm đúng không cứu được một graph model sai.

Đây là first-principles lesson quan trọng khi chuyển graph theory sang engineering.

## Mental Model

> Graph là toán học của **quan hệ và khả năng đi qua quan hệ**. Vertices là states/entities; edges là allowed relationships/transitions. Paths nói reachability, cycles nói feedback/dependency loop, components nói regions tách rời, weights/capacities thêm cost và resource constraints. Trước khi chọn BFS, Dijkstra hay flow algorithm, hãy hỏi edge thật sự đại diện điều gì.

## Common Misconceptions

**“Graph theory graph là chart dữ liệu.”** Không. Graph ở đây là network structure `G=(V,E)`.

**“BFS luôn tìm shortest path.”** Chỉ theo số edges hoặc khi mọi edges có equal cost. Weighted graph cần algorithm tương ứng với weight semantics.

**“Dijkstra chỉ cần graph connected.”** Điều kiện quan trọng là edge weights nonnegative cho standard correctness argument.

**“Tree và DAG giống nhau.”** Tree là structure chặt hơn. DAG có thể có node nhiều parents và nhiều alternative paths; tree underlying hierarchy có unique simple path giữa vertices trong undirected sense.

**“MST cho shortest route từ source.”** MST minimize total tree weight, không minimize từng source-to-node distance.

**“Nếu graph connected thì system reliable.”** Connectivity chỉ nói có path trong model hiện tại. Reliability còn phụ thuộc redundancy, failure probability, capacity và time-dependent conditions.

**“Thêm càng nhiều edges càng tốt.”** Extra edges tăng redundancy nhưng cũng có thể tạo cycles, coupling, attack surface hoặc routing complexity. Graph design luôn có trade-off.