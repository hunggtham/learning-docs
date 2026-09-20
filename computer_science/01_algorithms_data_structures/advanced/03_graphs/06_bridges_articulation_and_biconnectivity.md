# Bridges, Articulation Points và Biconnectivity  
**단절선, 단절점, 이중 연결성**

Một connected graph có thể có những cạnh hoặc đỉnh đóng vai trò “điểm yếu”. Nếu xóa một cạnh làm số connected components tăng, cạnh đó là **bridge / 단절선**. Nếu xóa một vertex làm graph tách thêm components, vertex đó là **articulation point / 단절점**.

Đây là model trực tiếp cho reliability: một network link hoặc router nào là single point of failure?

## DFS tree chưa đủ — cần biết back edge

Giả sử DFS đi từ parent `u` xuống child `v`. Nếu subtree của `v` có một edge quay về ancestor của `u`, xóa `(u,v)` vẫn có đường thay thế. Nếu không, `(u,v)` là bridge.

Ta định nghĩa:

```text
tin[u] = discovery time của u
low[u] = discovery time nhỏ nhất reachable từ subtree u
         bằng tree edges cộng tối đa một back edge lên ancestor
```

Khi DFS từ `u` sang child `v` xong:

\[
low[u] = \min(low[u], low[v])
\]

Với back edge `(u,v)` tới ancestor đã visited:

\[
low[u] = \min(low[u], tin[v])
\]

## Bridge condition

Tree edge `(u,v)` là bridge nếu:

\[
low[v] > tin[u]
\]

Tại sao là `>`? Nếu `low[v] <= tin[u]`, subtree `v` có đường quay tới `u` hoặc ancestor của `u`, nên có route thay thế khi bỏ edge.

## Articulation point condition

Với non-root `u`, nếu tồn tại child `v` sao cho:

\[
low[v] \ge tin[u]
\]

thì `u` là articulation point: subtree `v` không thể đi lên ancestor của `u` nếu bỏ `u`.

Root là case đặc biệt: root là articulation point nếu DFS tree của nó có từ hai children độc lập trở lên.

## Java implementation core

```java
void dfs(int u, int parentEdge) {
    seen[u] = true;
    tin[u] = low[u] = timer++;
    int children = 0;

    for (Edge e : g.get(u)) {
        if (e.id == parentEdge) continue;
        int v = e.to;

        if (seen[v]) {
            low[u] = Math.min(low[u], tin[v]);
        } else {
            dfs(v, e.id);
            low[u] = Math.min(low[u], low[v]);

            if (low[v] > tin[u]) {
                bridges.add(e.id);
            }

            if (parentEdge != -1 && low[v] >= tin[u]) {
                articulation[u] = true;
            }
            children++;
        }
    }

    if (parentEdge == -1 && children > 1) {
        articulation[u] = true;
    }
}
```

Dùng edge id thay vì chỉ `v == parent` để xử lý multi-edge đúng.

## Biconnected components

Một graph “robust hơn” nếu không bị tách chỉ vì mất một vertex. Biconnected decomposition nhóm edges/vertices theo các blocks không có articulation point nội bộ theo định nghĩa phù hợp.

Concept này dùng trong network reliability, circuit analysis và graph decomposition.

## Mental Model

> `low[u]` trả lời: “subtree này có thể leo ngược lên cao đến đâu mà không phải quay qua parent edge vừa đi xuống?”

Nếu câu trả lời “không vượt được parent”, parent edge/vertex có thể là điểm cắt.

Xem thêm: [DFS](./01_graph_traversal_bfs_dfs.md).
