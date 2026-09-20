# Case Study: Hệ thống định tuyến từ góc nhìn đồ thị
**Routing System Case Study / 라우팅 시스템 설계 사례**

Một hệ thống định tuyến không chỉ cần “chạy Dijkstra”. Nó phải mô hình hóa topology, cập nhật thay đổi, tính đường đi, xử lý tie-break, bảo đảm hội tụ, giới hạn state và đôi khi phải phản ứng với lỗi trong vài mili giây. DSA cung cấp các primitive quan trọng, nhưng thiết kế thật là sự kết hợp giữa biểu diễn đồ thị, shortest path, priority queue, incremental update và cache.

## 1. Mô hình đồ thị

Mạng có thể được biểu diễn:

```text
router / switch / location -> đỉnh
link                        -> cạnh
latency / cost / hop        -> trọng số
```

Điều đầu tiên cần xác định là cạnh có hướng hay vô hướng, trọng số có âm không, có nhiều cạnh song song hay không và topology có thay đổi theo thời gian không.

Nếu link hai chiều có chi phí khác nhau theo từng hướng, mô hình đúng là hai cạnh có hướng chứ không phải một cạnh vô hướng.

## 2. Adjacency List hay Matrix?

Mạng thực thường thưa: mỗi router chỉ nối trực tiếp một phần nhỏ tổng số router. Vì vậy danh sách kề thường có bộ nhớ:

\[
O(V+E)
\]

và duyệt cạnh hiệu quả hơn ma trận `O(V^2)`.

Nếu cần kiểm tra adjacency cực thường xuyên trên đồ thị nhỏ/dày, matrix có thể hợp lý. Representation phải theo workload.

## 3. Dijkstra và invariant

Với trọng số không âm, Dijkstra duy trì:

```text
dist[v] = khoảng cách tốt nhất đã biết
```

Khi một đỉnh `u` được lấy ra với khoảng cách nhỏ nhất còn hợp lệ, khoảng cách đó trở thành tối ưu cuối cùng.

Lý do là mọi đường đi khác chưa xét phải đi qua các đỉnh có khoảng cách ít nhất bằng `dist[u]`; với cạnh không âm, chúng không thể tạo đường tới `u` ngắn hơn giá trị hiện tại.

Priority Queue giúp chọn frontier nhỏ nhất nhanh hơn quét toàn bộ đỉnh.

## 4. Lazy Priority Queue

Nhiều heap chuẩn không có decrease-key tiện dụng. Ta có thể chèn trạng thái mới:

```text
(newDist, node)
```

và khi pop:

```text
nếu d != dist[node] -> bỏ qua entry cũ
```

Đây là một ví dụ dùng thêm bộ nhớ để đổi lấy implementation đơn giản và robust.

## 5. Tie-break không chỉ là chi tiết

Hai đường đi có cùng cost có thể cần tie-break theo:

```text
ít hop hơn
đường ổn định hơn
ID nhỏ hơn
policy cụ thể
```

Nếu tie-break là một phần của output contract, comparator/state phải phản ánh nó. Chỉ so `distance` có thể trả lời đúng về cost nhưng sai về semantics của sản phẩm.

## 6. Nếu trọng số có thể âm?

Dijkstra không còn hợp lệ. Khi đó có thể cần Bellman–Ford hoặc mô hình khác.

Trong routing thực, metric thường được thiết kế không âm chính vì muốn giữ các tính chất tốt của shortest-path framework.

Đây là ví dụ domain constraint được chọn để làm thuật toán dễ và đáng tin cậy hơn.

## 7. All-pairs hay single-source?

Nếu một router cần đường tới mọi đích, chạy single-source shortest path từ router đó là tự nhiên. Nếu hệ thống trung tâm cần mọi cặp trên graph nhỏ, Floyd–Warshall có thể hợp lý.

Nếu graph lớn và sparse, chạy Dijkstra từ nhiều nguồn có thể tốt hơn `O(V^3)`.

Cần chọn thuật toán theo số nguồn truy vấn chứ không chỉ theo `V` và `E`.

## 8. Dynamic topology

Khi một link đổi cost hoặc down/up, chạy lại toàn bộ shortest path là baseline đơn giản và đúng.

Nếu update rất thường xuyên và graph lớn, incremental shortest-path algorithms có thể tái sử dụng state cũ. Nhưng complexity và correctness khó hơn nhiều.

Nguyên tắc thực dụng:

```text
update hiếm -> recompute đơn giản
update dày -> cân nhắc incremental/dynamic algorithm
```

## 9. Link-state model

Trong mô hình link-state, mỗi router có topology tương đối đầy đủ rồi tự chạy shortest-path tree.

Pipeline khái niệm:

```text
link event
  ↓
flood topology update
  ↓
local graph update
  ↓
shortest-path recomputation
  ↓
routing table
```

DSA nằm ở graph storage và shortest path; distributed protocol chịu trách nhiệm dissemination và convergence.

## 10. Distance-vector model

Distance-vector gần với repeated relaxation kiểu Bellman–Ford:

```text
router trao đổi estimate với hàng xóm
router cập nhật khoảng cách tốt hơn
```

Thông tin phân tán nên router không có toàn graph. Đổi lại, hệ thống có các vấn đề hội tụ như count-to-infinity.

Hai kiến trúc dùng các primitive thuật toán khác nhau vì state được phân phối khác nhau.

## 11. Longest Prefix Match trong data plane

Sau khi control plane tính route, data plane phải map địa chỉ đích tới next hop.

Đây không còn là shortest-path query mà là **longest prefix match**.

Trie/Patricia/Radix Tree phù hợp vì các route được định nghĩa theo prefix bit:

```text
10.0.0.0/8
10.10.0.0/16
10.10.5.0/24
```

Đích `10.10.5.7` phải chọn prefix dài nhất `/24`.

Một hệ thống routing vì vậy kết hợp Graph + Trie, chứ không chỉ một cấu trúc.

## 12. ECMP và nhiều đường bằng nhau

Nếu có nhiều đường cùng cost, hệ thống có thể dùng **Equal-Cost Multi-Path (ECMP)** để chia lưu lượng.

Routing table khi đó có thể lưu một tập next-hop thay vì một next-hop duy nhất.

Hash flow key tới next-hop giúp một flow giữ ổn định đường đi trong khi phân phối nhiều flow qua nhiều đường.

Hashing trở thành một phần của routing data plane.

## 13. Failure và rerouting

Nếu link chính hỏng, recompute global route có thể mất thời gian. Một số hệ thống duy trì backup next-hop hoặc fast-reroute state.

Đây là dạng precomputation:

```text
trả thêm bộ nhớ/update cost trước
→ giảm latency khi failure xảy ra
```

Giống nhiều cấu trúc DSA khác, hệ thống materialize thông tin phục vụ một tình huống quan trọng.

## 14. K-shortest paths

Nếu cần nhiều route dự phòng hoặc candidate routes, shortest path duy nhất không đủ.

Các bài toán k-shortest paths như Yen/Eppstein mở rộng không gian kết quả. Complexity tăng đáng kể, vì output bản thân có kích thước `k`.

Không nên kỳ vọng giữ cùng chi phí với single shortest path khi yêu cầu output mạnh hơn.

## 15. Constrained routing

Một route có thể phải thỏa đồng thời:

```text
latency <= L
bandwidth >= B
không đi qua khu vực X
hop <= H
```

Nhiều ràng buộc làm bài toán khó hơn shortest path chuẩn và có thể dẫn tới multi-criteria optimization hoặc NP-hard variants.

Đây là nơi phải nhận ra giới hạn của primitive cổ điển thay vì cố ép mọi requirement vào Dijkstra.

## 16. A* khi có heuristic

Trong không gian địa lý, nếu có heuristic admissible như khoảng cách đường thẳng, A* có thể giảm số state phải mở rộng so với Dijkstra.

A* dùng:

\[
f(v)=g(v)+h(v)
\]

với `g` là cost đã biết và `h` là ước lượng phần còn lại.

Nếu heuristic không vượt cost thật, A* giữ tính tối ưu trong mô hình chuẩn.

Đây là ví dụ thêm domain knowledge để giảm search space.

## 17. Bidirectional Search

Nếu chỉ cần route giữa một cặp nguồn–đích trên graph lớn, tìm kiếm hai chiều có thể giảm vùng duyệt:

```text
forward từ source
backward từ target
```

Nhưng điều kiện dừng và cách ghép cost phải được chứng minh cẩn thận, đặc biệt với Dijkstra hai chiều.

## 18. Cache route

Nếu nhiều query lặp lại cùng source/destination, có thể cache kết quả. Nhưng topology update làm cache stale.

Cần trade-off:

```text
cache hit nhanh
vs
invalidation complexity
```

Có thể version topology; cache entry chỉ hợp lệ nếu version phù hợp.

## 19. Incremental invalidation

Khi một cạnh thay đổi, không phải mọi cached route đều bị ảnh hưởng. Nếu lưu dependency route → edge, có thể invalidate có chọn lọc.

Nhưng metadata dependency có thể rất lớn. Đây là ví dụ hệ thống đổi thêm state để giảm phạm vi recomputation.

## 20. Complexity model thực tế

Dijkstra với binary heap:

\[
O((V+E)\log V)
\]

Nhưng latency thực còn phụ thuộc:

```text
cache locality của adjacency
allocation của heap entries
số stale entries
branch prediction
độ dài key/policy comparator
```

Trong graph cực lớn, bố trí CSR có thể nhanh hơn graph object-heavy dù cùng Big-O.

## 21. CSR và graph tĩnh

Nếu topology ít thay đổi, CSR:

```text
offsets[]
edges[]
weights[]
```

cho bộ nhớ gọn và locality tốt.

Nếu edge update nhiều, adjacency list động dễ cập nhật hơn.

Static/dynamic workload lại quyết định representation.

## 22. Testing

Có thể differential-test Dijkstra trên graph nhỏ với Floyd–Warshall.

Các trường hợp cần thử:

```text
đồ thị rời rạc
nhiều shortest paths bằng nhau
zero-weight edge
parallel edge
topology thay đổi
source == target
đỉnh không reachable
```

Invariant cần kiểm tra:

```text
mọi next-hop dẫn tới đường hợp lệ
sum weight đúng dist
dist không vi phạm triangle inequality trên edge đã relax hoàn tất
```

## 23. Benchmark

Phải thay đổi:

```text
V, E
độ thưa/dày
weight distribution
update frequency
query locality
cache hit ratio
source distribution
```

Graph ngẫu nhiên đồng đều không đại diện topology thật, vốn thường có hub và cấu trúc phân cấp.

## 24. Pipeline hệ thống

```text
Topology events
    ↓
Graph state
    ↓
Shortest-path computation
    ↓
Routing Information Base
    ↓
Prefix/radix structure
    ↓
Forwarding table
    ↓
Hash/ECMP next-hop selection
```

Mỗi tầng dùng một cấu trúc khác vì câu hỏi khác nhau.

## Mô hình tư duy

> Một hệ thống routing là sự kết hợp giữa **graph reasoning ở control plane** và **prefix/hash lookup ở data plane**. Dijkstra giải một primitive quan trọng, nhưng thiết kế thật còn cần representation, update strategy, tie-break, failover, cache và consistency.

Xem thêm: [Graph Modeling](../03_graphs/00_graph_modeling_and_representation.md), [Shortest Paths](../03_graphs/02_shortest_paths.md), [Priority Queues](../01_linear_structures/03_queues_deques_and_priority_queues.md), [Trie](../02_trees/04_tries.md), [Hash Tables](../01_linear_structures/04_hash_tables.md).