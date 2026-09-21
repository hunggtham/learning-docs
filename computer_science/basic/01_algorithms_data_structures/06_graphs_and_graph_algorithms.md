# Graph và graph algorithms

Khi relationships không còn hierarchy đơn giản, graph (그래프 / đồ thị) trở thành model tự nhiên. Social network, road map, dependency graph, network topology, build system, call graph và database foreign-key relationships đều có thể model bằng vertices và edges.

## Graph model

Graph `G=(V,E)` gồm vertices/nodes `V` và edges `E`. Directed graph có edge `u→v`; undirected graph coi relation hai chiều. Edge có thể mang weight như distance, cost, latency hoặc capacity.

Degree đếm connections; path là sequence vertices nối qua edges; cycle quay về vertex đã gặp. Connected components phân vùng graph undirected thành vùng reachable. Directed graph có strongly connected components khi mỗi node reach nhau theo hướng.

Xem nền toán tại [Graph Theory](../../../mathematics/07_discrete_cs/00_graph_theory.md).

## Representation: adjacency list vs matrix

Adjacency matrix dùng `|V|×|V|` entries, edge lookup O(1) nhưng space O(V²). Phù hợp dense graph hoặc algebraic operations.

Adjacency list lưu neighbors cho mỗi vertex, space O(V+E), phù hợp sparse graphs phổ biến. Representation quyết định iteration cost và locality.

## BFS: shortest path theo số cạnh

Breadth-First Search dùng queue và khám phá theo layers. Với unweighted graph, lần đầu reach vertex cho shortest number-of-edges distance.

Invariant: trước khi xử lý layer distance d+1, tất cả vertices distance ≤d đã được discovered theo shortest distance. Complexity adjacency-list O(V+E) vì mỗi vertex/edge xử lý bounded times.

BFS dùng trong degrees-of-separation, shortest hops, crawling và level-order traversal.

## DFS: đi sâu để lộ structure

Depth-First Search dùng recursion hoặc explicit stack. Entry/exit times và recursion stack giúp detect cycles, topological sorting, SCC algorithms và articulation analysis.

DFS không bảo đảm shortest path trong unweighted graph, vì nó có thể chọn một nhánh dài trước.

## Topological sort và dependency

Directed acyclic graph — DAG cho phép linear order sao cho mọi dependency đứng trước dependent. Build systems, course prerequisites và workflow dependencies dùng topological sort.

Nếu graph có cycle, topological order không tồn tại. Cycle thường chính là signal thiết kế: package A phụ thuộc B phụ thuộc lại A; migration dependencies loop; tasks deadlock logic.

## Dijkstra và weighted shortest path

Dijkstra giải shortest paths khi edge weights non-negative. Nó repeatedly chọn unsettled vertex có smallest tentative distance, thường bằng priority queue.

Tại sao non-negative quan trọng? Khi chọn distance nhỏ nhất làm final, một edge âm từ node chưa xử lý có thể sau đó tạo đường ngắn hơn, phá invariant. Với negative edges, Bellman–Ford hoặc model khác cần dùng.

## Minimum Spanning Tree

MST kết nối mọi vertices với total edge weight nhỏ nhất, không tạo cycles. Kruskal sort edges rồi thêm nếu không nối hai vertices đã connected, thường dùng Union-Find/Disjoint Set. Prim phát triển một tree từ frontier.

MST khác shortest-path tree: tối ưu tổng network cost, không tối ưu distance từ một source.

## Union-Find

Disjoint Set Union quản lý partition thành components với `find` và `union`. Path compression + union by rank/size cho amortized gần constant, chính xác hơn là inverse-Ackermann.

Nó minh họa data structure được thiết kế quanh một rất nhỏ operation set nhưng cực hiệu quả cho connectivity.

## Graph ở software systems

Package dependencies, services, ownership và data lineage là graphs. “Microservices architecture” không chỉ là list services; interaction graph quyết định coupling, failure propagation và deploy coordination.

Garbage collector tracing object graph từ roots để xác định reachability. Git commit history là DAG. Web pages + links tạo directed graph.

## Mental Model

> Khi entities có **many-to-many relationships**, nghĩ bằng graph. Sau đó hỏi: directed hay undirected, weighted hay unweighted, sparse hay dense, và operation chính là reachability, shortest path, ordering, connectivity hay flow?

## Common Misconceptions

**“Tree và graph là hai thứ tách biệt.”** Tree là graph connected acyclic với structure đặc biệt.

**“BFS luôn nhanh hơn DFS.”** Cả hai O(V+E) trong adjacency-list model; memory và traversal behavior khác.

**“Dijkstra dùng được với negative weight nếu không có negative cycle.”** Invariant greedy của Dijkstra vẫn có thể sai với negative edge; dùng algorithm phù hợp.

## Kết nối

Graph algorithms dùng [linear structures](./03_linear_data_structures.md) và [heap](./05_trees_heaps_and_search_structures.md). Dependency graphs xuất hiện trong [build/package systems](../08_software_systems/01_version_control_build_link_and_packages.md), routing trong [networking](../06_networks_distributed_systems/01_ethernet_ip_subnetting_and_routing.md), wait-for graph trong [deadlock](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md).
