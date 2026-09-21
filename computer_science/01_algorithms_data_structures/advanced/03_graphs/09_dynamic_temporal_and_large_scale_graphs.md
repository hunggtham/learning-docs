# Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn
**Dynamic, Temporal & Large-Scale Graphs / 동적·시간·대규모 그래프**

Các chương đồ thị cơ bản thường giả định topology đã biết và tương đối tĩnh trong lúc thuật toán chạy. Hệ thống thực tế lại thường thay đổi liên tục: cạnh được thêm/xóa, trọng số thay đổi, node tạm thời mất kết nối, sự kiện chỉ tồn tại trong một khoảng thời gian, và toàn bộ đồ thị có thể quá lớn để nằm vừa trên một máy.

Chương này tập trung vào câu hỏi: **điều gì thay đổi khi bản thân đồ thị trở thành dữ liệu động?**

## 1. Tĩnh, tăng dần, giảm dần và fully dynamic

Cần phân biệt bốn mô hình cập nhật.

```text
static           -> không thay đổi topology
incremental      -> chỉ thêm cạnh/nút
decremental      -> chỉ xóa cạnh/nút
fully dynamic    -> vừa thêm vừa xóa
```

Sự phân biệt này quan trọng vì tính đơn điệu cho phép thuật toán đơn giản hơn rất nhiều.

Nếu chỉ thêm cạnh và chỉ hỏi connectivity vô hướng, DSU gần như hoàn hảo. Nhưng khi cho phép xóa, DSU chuẩn không biết một thành phần phải tách thành những phần nào vì nó đã nén mất topology chi tiết.

## 2. Tại sao xóa khó hơn thêm?

Khi thêm một cạnh `(u,v)`, ta chỉ cần biết liệu nó nối hai thành phần khác nhau hay tạo thêm đường dư thừa.

Khi xóa một cạnh, phải trả lời câu hỏi khó hơn:

> Cạnh đó có phải là cầu trong topology hiện tại không, hay vẫn còn một đường thay thế khác?

Điều này yêu cầu thông tin về cấu trúc toàn cục, không chỉ component ID.

Đây là một pattern tổng quát: thao tác **hủy một quan hệ** thường khó hơn thao tác **tích lũy quan hệ** vì phải phục hồi thông tin đã từng bị nén.

## 3. Offline Dynamic Connectivity bằng Segment Tree theo thời gian

Nếu biết trước toàn bộ chuỗi thêm/xóa cạnh và truy vấn connectivity, ta có thể xử lý ngoại tuyến.

Mỗi cạnh tồn tại trong một khoảng thời gian:

```text
[timeAdded, timeRemoved)
```

Xây một Segment Tree trên trục thời gian. Gắn mỗi cạnh vào các node của Segment Tree phủ đúng khoảng thời gian nó tồn tại.

DFS cây thời gian:

1. snapshot trạng thái Rollback DSU;
2. union mọi cạnh thuộc node hiện tại;
3. đi xuống con;
4. ở lá, trả lời truy vấn tại thời điểm đó;
5. rollback về snapshot khi quay lên.

Điểm tinh tế là Rollback DSU thường **không dùng path compression**, vì path compression tạo quá nhiều thay đổi khó hoàn tác. Union-by-size vẫn giữ chiều cao `O(log n)`.

Đây là một ví dụ đẹp về composition:

```text
interval over time
+ segment tree
+ rollback DSU
= dynamic connectivity offline
```

## 4. Euler Tour Tree và Link-Cut Tree

Khi đồ thị là rừng động, các cấu trúc cây động cho phép `link`, `cut` và truy vấn trên đường/cây.

**Euler Tour Tree** biểu diễn một cây bằng chuỗi Euler được lưu trong cây tìm kiếm cân bằng; cắt/nối cây trở thành split/merge của chuỗi.

**Link-Cut Tree** dùng Splay Tree để biểu diễn các preferred paths và hỗ trợ các thao tác như:

```text
link(u,v)
cut(u,v)
findRoot(u)
pathAggregate(u,v)
```

với cận khấu hao logarithmic trong mô hình chuẩn.

Đây là ví dụ nơi cây cân bằng không còn chỉ lưu khóa có thứ tự; nó trở thành động cơ cho topology động.

## 5. Dynamic MST: tại sao khó?

Nếu thêm một cạnh mới `(u,v,w)` vào MST hiện tại, cạnh này tạo một chu trình với đường duy nhất giữa `u` và `v` trong cây. Nếu `w` nhỏ hơn cạnh nặng nhất trên đường đó, ta có thể thay cạnh nặng nhất bằng cạnh mới.

Nghe đơn giản, nhưng cần trả nhanh:

```text
max edge weight on path(u,v)
```

và hỗ trợ cập nhật cấu trúc cây sau khi thay cạnh. Link-Cut Tree hoặc Heavy-Light Decomposition có thể đóng vai trò.

Khi còn cho phép xóa cạnh bất kỳ khỏi graph, bài toán phức tạp hơn vì nếu xóa cạnh thuộc MST, ta phải tìm cạnh nhẹ nhất nối lại hai thành phần.

Dynamic MST cho thấy rõ sự khác biệt giữa **duy trì một lời giải tối ưu** và **tính lại lời giải từ đầu**.

## 6. Dynamic Shortest Path

Nếu chỉ một vài trọng số thay đổi, chạy lại Dijkstra toàn bộ có thể lãng phí. Các thuật toán incremental/decremental cố tái sử dụng khoảng cách cũ.

Tuy nhiên, shortest path rất nhạy: thay một cạnh gần nguồn có thể thay đổi khoảng cách của cả vùng lớn. Vì vậy không có một incremental update đơn giản luôn rẻ.

Trong routing system thực tế, người ta thường kết hợp:

```text
incremental recomputation
region-local repair
hierarchical graph
cache invalidation
batch updates
```

thay vì kỳ vọng một cấu trúc động tổng quát giải mọi trường hợp tối ưu.

## 7. Temporal Graph

Trong đồ thị thời gian, cạnh không chỉ có tồn tại/không tồn tại mà có timestamp hoặc khoảng hiệu lực.

Ví dụ chuyến tàu:

```text
A -> B departs 10:00 arrives 10:30
```

Một đường đi hợp lệ phải tôn trọng thứ tự thời gian; cạnh tiếp theo không thể khởi hành trước khi ta đến.

Do đó “đường đi ngắn nhất” có thể trở thành:

```text
earliest arrival
minimum waiting time
minimum number of transfers
```

Mỗi objective tạo một mô hình trạng thái khác.

## 8. Time-Expanded Graph và Time-Dependent Graph

Một cách là tạo trạng thái `(vertex,time)` và nối các transition hợp lệ. Đây là **time-expanded graph**. Nó rõ ràng nhưng có thể rất lớn.

Một cách khác giữ mỗi cạnh như một hàm chi phí theo thời gian:

\[
w_e(t)
\]

Đây là **time-dependent graph**. Dijkstra-like reasoning chỉ hoạt động dưới các điều kiện nhất định, chẳng hạn FIFO property: rời sớm hơn không thể đến muộn hơn chỉ vì đi cùng cạnh.

Nếu property này bị phá, greedy finalization của Dijkstra có thể không còn đúng.

## 9. Sliding-Window Graph

Trong fraud detection, observability hoặc telemetry, ta có thể chỉ quan tâm các cạnh trong `W` phút gần nhất.

Khi cửa sổ trượt:

```text
new events enter
after W time, old events expire
```

Topology liên tục thêm và xóa cạnh. Nếu chỉ cần thống kê cục bộ, có thể dùng bucket thời gian và rebuild định kỳ thay vì fully dynamic structure phức tạp.

Đây là bài học thực tế quan trọng:

> Một thuật toán lý thuyết mạnh không phải lúc nào cũng tốt hơn một thiết kế batch + rebuild đơn giản nếu tải công việc cho phép.

## 10. Graph Streaming

Khi số cạnh quá lớn để giữ toàn bộ trong RAM, thuật toán streaming chỉ xem mỗi cạnh một hoặc vài lượt với bộ nhớ nhỏ.

Các câu hỏi có thể là:

```text
ước lượng số tam giác
ước lượng degree distribution
phát hiện heavy hitters
sampling edges/nodes
approximate connectivity
```

Ta chấp nhận kết quả xấp xỉ hoặc nhiều pass để đổi lấy bộ nhớ nhỏ hơn.

Probabilistic sketches và reservoir sampling xuất hiện tự nhiên ở đây.

## 11. Reservoir Sampling trên cạnh

Nếu luồng cạnh có độ dài chưa biết và muốn giữ một mẫu đều kích thước `k`, Reservoir Sampling cho mỗi cạnh cùng xác suất cuối cùng `k/n`.

Mẫu này có thể dùng để ước lượng thống kê graph hoặc làm nền cho approximate motif counting.

Nhưng sampling edge đều không đồng nghĩa sampling vertex đều; node có degree cao xuất hiện nhiều hơn trong edge sample. Phải phân biệt đơn vị lấy mẫu.

## 12. Graph Partitioning

Đồ thị lớn trên nhiều máy phải được phân vùng. Mục tiêu thường đồng thời:

```text
cân bằng số node/edge giữa các máy
giảm số cạnh cắt qua partition
giảm communication
```

Đây là bài toán khó. Heuristic và multilevel methods thường được dùng trong thực tế.

Cách partition ảnh hưởng trực tiếp đến distributed BFS/PageRank/GNN vì cạnh cắt partition tạo network traffic.

## 13. Vertex Cut và Edge Cut

**Edge cut** gán node vào partition; cạnh nối node ở hai partition tạo communication.

**Vertex cut** gán cạnh vào partition và có thể sao chép node degree cao trên nhiều partition.

Trong power-law graph, một vài hub có degree cực lớn. Vertex-cut có thể phân tán tải tốt hơn nhưng phải đồng bộ trạng thái bản sao của node.

Đây là một ví dụ representation quyết định scalability.

## 14. Power-Law Graph và skew

Social graph, web graph và interaction graph thường có phân phối degree lệch mạnh: phần lớn node degree nhỏ, vài node degree cực lớn.

Một thuật toán chỉ phân tích theo average degree có thể bỏ qua hot spot ở hub node.

Trong parallel traversal, một hub có thể tạo hàng triệu neighbor expansion trên một worker, gây mất cân bằng. Cần chunk adjacency, work stealing hoặc specialized partitioning.

## 15. Direction-Optimizing BFS

BFS truyền thống đi từ frontier ra neighbor, thường gọi là **top-down**.

Khi frontier trở nên rất lớn, có thể hiệu quả hơn nếu duyệt các node chưa thăm và hỏi “node này có neighbor nào thuộc frontier không?”. Đây là **bottom-up BFS**.

Direction-optimizing BFS chuyển giữa hai chế độ tùy kích thước frontier và số cạnh dự kiến phải quét.

Đây là một ví dụ thuật toán giữ cùng semantics nhưng thay hướng traversal theo shape của workload.

## 16. Bidirectional Search

Nếu cần đường đi giữa một nguồn và một đích cụ thể trong graph không trọng số, BFS từ hai phía có thể giảm mạnh không gian tìm kiếm thực tế.

Thay vì mở rộng khoảng `b^d`, lý tưởng mỗi phía chỉ đi sâu khoảng `d/2`, cho tổng gần `2b^{d/2}`.

Cần cẩn thận khi graph có hướng: backward search phải dùng transpose edges hoặc predecessor relation.

## 17. Landmark và A*

A* dùng heuristic `h(v)` để ưu tiên node có vẻ gần đích. Heuristic phải **admissible** để không đánh giá quá cao chi phí còn lại nếu muốn bảo đảm tối ưu trong mô hình chuẩn.

Landmark-based heuristics có thể tiền xử lý khoảng cách tới một số landmark và dùng bất đẳng thức tam giác để tạo lower bound tốt hơn.

Đây là trade-off giữa preprocessing/memory và query latency.

## 18. Contraction Hierarchies

Route planning đường bộ thực tế có thể có hàng triệu node. Chạy Dijkstra toàn graph cho mỗi truy vấn có thể quá chậm.

**Contraction Hierarchies** lần lượt loại node ít quan trọng và thêm shortcut để bảo toàn khoảng cách. Query sau đó chủ yếu đi qua hierarchy.

Ý tưởng sâu là chuyển chi phí sang preprocessing để tạo một graph mới cùng metric nhưng dễ search hơn.

## 19. Dynamic Graph Cache và versioning

Nếu query graph đắt, hệ thống có thể cache:

```text
shortest path
reachability
component summary
neighborhood expansion
```

Nhưng topology thay đổi làm cache cũ. Invalidation có thể theo version graph, epoch, region hoặc dependency set.

Không nên dùng kết quả cũ nếu không xác định rõ consistency requirement. “Graph cache” là bài toán correctness, không chỉ performance.

## 20. Graph Snapshot

Một chiến lược phổ biến là xử lý update liên tục nhưng xuất bản snapshot bất biến theo epoch.

Reader dùng snapshot ổn định; writer xây snapshot tiếp theo. Điều này đơn giản hóa thuật toán vì traversal không phải xử lý topology đổi giữa chừng.

Đổi lại, kết quả có độ trễ cập nhật. Đây là trade-off giữa **freshness** và **simplicity/consistency**.

## 21. Concurrency và mutation trong traversal

Nếu một luồng đang BFS trong khi luồng khác xóa cạnh, câu hỏi “BFS đang duyệt graph nào?” phải có câu trả lời.

Các lựa chọn gồm:

```text
khóa graph
snapshot isolation
copy-on-write
versioned adjacency
chấp nhận weak consistency
```

Không có một semantics mặc định đúng cho mọi hệ thống.

## 22. Testing Dynamic Graph

Cách kiểm thử mạnh nhất là differential testing với graph nhỏ.

Với dynamic connectivity:

```text
thực hiện chuỗi add/remove/query ngẫu nhiên
sau mỗi query, chạy BFS/DFS brute force trên graph hiện tại
so kết quả với cấu trúc động
```

Với dynamic shortest path, có thể chạy Dijkstra/Floyd-Warshall từ đầu trên graph nhỏ làm oracle.

Đặc biệt cần sinh:

```text
xóa bridge
thêm cạnh song song
self-loop
remove edge không tồn tại
add/remove lặp lại
batch update cùng timestamp
```

## 23. Benchmark phải phản ánh update/query ratio

Một cấu trúc động chỉ đáng dùng nếu giảm tổng chi phí thực tế.

Cần đo:

```text
updates/second
queries/second
ratio update:query
p95/p99 latency
memory overhead
rebuild cost
staleness nếu dùng snapshot
```

Nếu 99.99% thời gian graph không thay đổi, một cấu trúc static tối ưu + rebuild hiếm có thể đơn giản và nhanh hơn fully dynamic algorithm.

## 24. Decision Framework

| Tình huống | Hướng tiếp cận |
|---|---|
| Chỉ thêm cạnh, hỏi connectivity | DSU |
| Add/remove biết trước | Segment tree over time + Rollback DSU |
| Rừng động | Euler Tour Tree / Link-Cut Tree |
| Nhiều path query trên tree động | Link-Cut Tree hoặc cấu trúc chuyên biệt |
| Graph temporal | time-expanded / time-dependent model |
| Graph cực lớn | CSR + partitioning / streaming |
| Query nhiều, update theo batch | snapshot + preprocessing |
| Route query rất nhiều | hierarchy / landmark / A* |

## Mô hình tư duy

> Đồ thị động không chỉ là “đồ thị thường + cập nhật”. Khi topology thay đổi, ta phải quyết định **thời điểm nào được xem là cùng một trạng thái graph**, thông tin nào được duy trì incremental, và thông tin nào nên tính lại theo batch.

Ba câu hỏi quan trọng nhất là:

```text
Update có đơn điệu không?
Có thể xử lý offline không?
Query cần dữ liệu mới đến mức nào?
```

Nếu trả lời được ba câu đó, không gian thiết kế thường thu hẹp mạnh.

Xem thêm: [Graph Modeling](./00_graph_modeling_and_representation.md), [Union-Find](./05_union_find.md), [Shortest Paths](./02_shortest_paths.md), [MST](./03_minimum_spanning_trees.md), [Rollback/Amortized Thinking](../05_specialized/03_amortized_randomized_and_probabilistic_thinking.md), [Routing Case Study](../90_connections/05_case_study_routing_graph_system.md).