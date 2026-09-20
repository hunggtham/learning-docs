# Graph: mô hình hóa và biểu diễn
**Đồ thị (Graph / 그래프)**

Graph mô hình hóa **entities + relationships**. User và friendship, city và road, package và dependency, service và network call đều có thể biểu diễn thành:

\[
G=(V,E)
\]

trong đó `V` là vertices/nodes và `E` là edges.

## Directed, undirected và weighted

Undirected edge `A -- B` biểu diễn quan hệ hai chiều. Directed edge `A -> B` có hướng. Dependency graph thường directed.

Weighted graph gắn cost lên edge: distance, latency, price, risk hoặc energy.

## Adjacency matrix

Matrix `V x V` cho edge lookup `O(1)` nhưng memory `O(V²)`. Hợp với graph dense hoặc matrix-based computation.

## Adjacency list

Mỗi node lưu neighbors. Memory `O(V+E)`, phù hợp sparse graph phổ biến.

Java:

```java
List<List<Integer>> g = new ArrayList<>();
for (int i = 0; i < n; i++) g.add(new ArrayList<>());
g.get(u).add(v);
```

JavaScript:

```js
const g = Array.from({length: n}, () => []);
g[u].push(v);
```

## Modeling quan trọng hơn thuật toán

Nếu bài flight routing có constraint theo thời gian, node có thể không chỉ là `airport`; state có thể phải là `(airport, time bucket)` hoặc `(airport, flightsUsed)`. Một algorithm tốt trên state model sai vẫn cho lời giải sai cho problem thật.

## Degree, path, cycle, connectivity

Directed graph có indegree/outdegree. Path là sequence vertices qua edges. Cycle quay về state cũ. Connectivity/reachability là nền cho BFS, DFS, SCC, MST và DSU.

## Mental Model

> Khi relationship quan trọng ngang entity, hãy nghĩ graph. Khi một câu chuyện nói “kết nối, phụ thuộc, chuyển trạng thái, reachable”, khả năng cao có graph model phía sau.

## Edge list, adjacency list và CSR

Edge list:

```text
(u1,v1,w1)
(u2,v2,w2)
...
```

phù hợp Kruskal vì algorithm cần sort edges toàn cục.

Adjacency list phù hợp traversal từ node vì neighbors truy cập trực tiếp.

CSR (Compressed Sparse Row) dùng arrays `offsets` và `edges` để lưu sparse graph compact, contiguous hơn object-heavy adjacency lists. Nó phổ biến trong high-performance graph processing và sparse matrix representation.

Cùng graph semantics nhưng representation khác theo operation chính.

## Graph và sparse matrix

Adjacency matrix chính là matrix representation của relation. Nhiều graph algorithms có linear-algebra interpretation: repeated matrix multiplication liên quan paths; PageRank dùng transition matrix; graph neural networks aggregate neighbor features.

Không phải lúc nào matrix algorithm là implementation tốt nhất, nhưng connection giúp thấy graph theory và linear algebra là hai cách nhìn cùng structure.

## State-space graph

Trong puzzle/search problem, vertices có thể là states chứ không phải entities domain. Ví dụ state `(x,y,keysMask)` trong grid có keys/doors. Hai states ở cùng cell nhưng khác keys không tương đương vì future actions khác nhau.

Model state thiếu information làm algorithm “visited quá sớm” và sai. Model state dư information làm graph phình lớn không cần thiết.

## Multigraph và self-loop

Nhiều implementations vô thức giả định simple graph. Nếu domain cho phép parallel edges hoặc self-loops, bridge detection, degree counting, MST và adjacency dedup cần xử lý đúng semantics. Luôn xác định graph class trước khi code.

## Directed/undirected storage

Undirected edge thường được lưu hai adjacency entries. Khi algorithm cần nhận diện một physical edge — bridge/Euler — nên dùng unique edge id để hai directions được nhận biết là cùng một edge.
