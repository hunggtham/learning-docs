# Lý thuyết đồ thị: toán học của mạng lưới và quan hệ

Đồ thị (Graph / 그래프) trong graph theory không phải chart dữ liệu. Nó là structure gồm vertices/nodes và edges nối chúng. Khi problem quan trọng hơn ở “ai liên kết với ai” thay vì coordinates chính xác, graph là abstraction tự nhiên.

## Graph definition

Một graph có thể viết

```math
G=(V,E)
```

trong đó `V` là set vertices, `E` là set edges. Với undirected graph, edge `{u,v}` không có direction. Với directed graph, edge `(u,v)` đi từ `u` sang `v`.

Social friendship có thể model undirected; following trên social network thường directed. Road network có thể directed do one-way streets và weighted do travel time/distance.

## Degree

Degree của vertex trong undirected graph là số incident edges. Directed graph có in-degree và out-degree.

Handshake lemma:

```math
\sum_{v\in V}\deg(v)=2|E|
```

vì mỗi edge đóng góp 1 degree cho hai endpoints. Do đó số vertices có odd degree luôn even.

## Path và connectivity

Path là sequence vertices nối bởi edges. Graph connected nếu mọi pair vertices có path giữa chúng.

Trong network routing, connectivity nói packets theoretically có route. Nhưng performance còn phụ thuộc weights, capacity và failures.

## Trees

Tree là connected undirected graph không cycles. Với `n` vertices, tree có exactly `n-1` edges.

Tại sao? Bắt đầu một vertex; mỗi vertex mới muốn giữ connected nhưng không tạo cycle phải thêm đúng một edge. Sau khi thêm `n-1` vertices cần `n-1` edges.

File systems, DOM trees, ASTs và hierarchical indexes dùng tree structures. Nhưng Git commit history nói chung là DAG, không strict tree, vì merge commit có thể có nhiều parents.

## Directed acyclic graphs

DAG (Directed Acyclic Graph / 방향 비순환 그래프) không có directed cycles. Dependencies trong build systems, package managers, workflows và task scheduling thường là DAG nếu hợp lệ.

Topological ordering sắp vertices sao cho mọi edge `u→v` đặt `u` trước `v`. Nếu directed cycle tồn tại, topological order không thể tồn tại.

## BFS và shortest paths trong unweighted graph

Breadth-first search khám phá theo layers distance edges từ source. Vì nodes distance `d` được khám phá trước `d+1`, BFS tìm shortest number-of-edges path trong unweighted graph.

Complexity với adjacency list:

```math
O(|V|+|E|)
```

vì mỗi vertex/edge được process bounded number times.

## DFS

Depth-first search đi sâu trước khi backtrack. Nó hữu ích cycle detection, connected components, topological sorting variants và traversal.

DFS stack có thể explicit hoặc recursion. Với deep graph, recursion depth có thể thành engineering constraint.

## Weighted shortest path

Dijkstra's algorithm tìm shortest paths khi edge weights nonnegative. Greedy step chọn unsettled vertex có smallest tentative distance. Negative edges phá core assumption rằng settled distance không thể cải thiện sau.

Bellman–Ford handle negative weights và detect negative cycles nhưng cost cao hơn.

## Adjacency matrix vs adjacency list

Adjacency matrix dùng `O(V^2)` memory và edge lookup `O(1)`. Adjacency list dùng roughly `O(V+E)` cho sparse graphs và iteration neighbors efficient.

Representation choice phụ thuộc graph density và operations, giống database indexing tradeoffs.

## Graphs trong software systems

Call graph, dependency graph, state-transition graph, network topology, knowledge graph, database relationship network và recommendation graph đều reuse cùng abstraction. Graph algorithms vì vậy là bridge trực tiếp giữa discrete mathematics và software engineering.

## Mental Model

> Graph bỏ hình dạng vật lý để giữ connectivity. Khi một problem chủ yếu hỏi đường đi, dependency, reachability, neighborhood hay cycles, hãy nghĩ bằng vertices và edges trước khi nghĩ bằng arrays hay business objects.

## Common Misconceptions

Graph theory graph không phải plot. Tree chỉ là một loại graph đặc biệt. Dijkstra không đúng với arbitrary negative edge weights. “Connected” không nói network nhanh hay reliable, chỉ nói có path trong model.
