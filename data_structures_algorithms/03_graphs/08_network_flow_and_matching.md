# Network Flow và Bipartite Matching  
**네트워크 플로우와 이분 매칭**

Network flow mô hình hóa tài nguyên đi qua một mạng có capacity. Edge `(u,v)` có capacity `c(u,v)`; ta muốn gửi flow từ source `s` tới sink `t` mà không vượt capacity và bảo toàn flow tại intermediate vertices.

## Flow constraints

Capacity:

\[
0 \le f(u,v) \le c(u,v)
\]

Conservation với vertex trung gian:

\[
\sum f(\text{in}) = \sum f(\text{out})
\]

Mục tiêu max-flow là tối đa tổng flow rời source, tương đương tới sink.

## Residual graph

Đây là insight cốt lõi. Nếu đã gửi 5 units qua edge capacity 10, residual forward capacity còn 5. Đồng thời residual graph có reverse edge capacity 5, biểu diễn khả năng **hoàn tác** một phần quyết định cũ.

Residual edge làm flow algorithm khác greedy “khóa quyết định”: algorithm có thể redirect flow nếu path mới tốt hơn.

## Augmenting path

Nếu residual graph còn path từ `s` tới `t`, ta có thể tăng flow bằng bottleneck nhỏ nhất trên path.

Ford–Fulkerson là framework này. Với integer capacities, mỗi augmentation tăng flow ít nhất 1 nhưng runtime phụ thuộc strategy.

Edmonds–Karp dùng BFS chọn shortest augmenting path theo số edges và có polynomial bound `O(VE^2)`.

Dinic xây level graph bằng BFS rồi gửi blocking flow bằng DFS, thường hiệu quả hơn và là lựa chọn thực dụng cho nhiều bài.

## Max-flow min-cut theorem

Giá trị maximum flow bằng capacity của minimum `s-t` cut.

Đây là một theorem sâu vì nó nối một optimization “gửi nhiều nhất” với một certificate “nút cổ chai nhỏ nhất”. Nếu flow đạt cut capacity, ta biết không thể làm tốt hơn.

## Bipartite matching

Bipartite graph chia vertices thành `L` và `R`; edge chỉ nối qua hai phía. Matching chọn edges không chia sẻ endpoint.

Ta biến matching thành flow:

```text
source -> mỗi L node capacity 1
L -> R edges capacity 1
mỗi R node -> sink capacity 1
```

Max flow chính là maximum matching size.

Hopcroft–Karp khai thác bipartite structure để đạt `O(E sqrt(V))`, tốt hơn generic flow cho large matching.

## Assignment và production connections

Matching mô hình hóa job-worker assignment, student-project assignment, resource pairing, ad-slot matching và nhiều scheduling constraints. Khi costs xuất hiện, ta bước sang min-cost flow hoặc Hungarian algorithm tùy structure.

## Mental Model

> Residual graph là “khả năng sửa quá khứ”. Một flow decision không hoàn toàn cố định; reverse residual capacity cho phép algorithm lấy lại capacity và route lại.

Xem thêm: [BFS/DFS](./01_graph_traversal_bfs_dfs.md), [Shortest Paths](./02_shortest_paths.md).
