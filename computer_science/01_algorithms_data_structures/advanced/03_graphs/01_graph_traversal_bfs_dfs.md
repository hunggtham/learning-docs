# BFS và DFS
**Graph Traversal / 그래프 순회**

Traversal hỏi: từ một node, ta thăm được những node nào và theo thứ tự nào?

## BFS

**Breadth-First Search / 너비 우선 탐색** dùng queue và mở rộng theo layer. Với unweighted graph, lần đầu tới node `v` là qua path có số edges ít nhất.

```java
int[] dist = new int[n];
Arrays.fill(dist, -1);
Queue<Integer> q = new ArrayDeque<>();
dist[s] = 0;
q.offer(s);

while (!q.isEmpty()) {
    int u = q.poll();
    for (int v : g.get(u)) {
        if (dist[v] == -1) {
            dist[v] = dist[u] + 1;
            q.offer(v);
        }
    }
}
```

Với adjacency list, time `O(V+E)`.

## DFS

**Depth-First Search / 깊이 우선 탐색** đi sâu theo branch trước khi backtrack.

```js
function dfs(u, g, seen) {
  seen[u] = true;
  for (const v of g[u]) {
    if (!seen[v]) dfs(v, g, seen);
  }
}
```

DFS thích hợp cho component exploration, cycle detection, topological reasoning, SCC, bridges và nhiều structural problems.

## Visited state

Graph có cycle cần visited tracking. Directed cycle detection thường dùng 3 states: unvisited, visiting, finished. Edge từ node hiện tại tới node `visiting` là back edge cho thấy directed cycle.

## BFS hay DFS?

Nếu cần shortest path theo số edges, BFS. Nếu cần structural exploration/backtracking, DFS thường tự nhiên. Cả hai có thể `O(V+E)`; khác biệt ở **frontier policy**.

## Mental Model

> BFS hỏi “cái gì gần nhất trước?”. DFS hỏi “nếu đi theo nhánh này tới tận cùng thì chuyện gì xảy ra?”. Queue và stack tạo ra search order, không chỉ là implementation detail.

## Discovery tree và parent reconstruction

Traversal không chỉ đánh dấu visited. Nếu lưu:

```text
parent[v] = u
```

khi lần đầu discover `v`, ta tạo một traversal tree. Với BFS trên unweighted graph, parent chain từ target về source chính là một shortest path.

```java
List<Integer> path = new ArrayList<>();
for (int v = target; v != -1; v = parent[v]) {
    path.add(v);
}
Collections.reverse(path);
```

## Multi-source BFS

Nếu có nhiều sources cùng distance 0, enqueue tất cả từ đầu. BFS sau đó tính distance tới **source gần nhất**.

Ví dụ: trong grid có nhiều exits, muốn biết mỗi cell gần exit nào nhất; hoặc lan truyền infection/fire từ nhiều điểm đồng thời.

Đây là cách thay model chứ không phải thuật toán mới.

## BFS trên implicit graph

Nhiều bài không đưa adjacency list. State tự tạo neighbors qua rules.

Ví dụ word ladder: mỗi word là node; edge tồn tại nếu đổi một ký tự. Ta không nhất thiết build toàn bộ graph trước; có thể generate neighbors on demand.

Graph là **mô hình quan hệ**, không bắt buộc phải materialize bằng object Edge.

## DFS timestamps

Trong DFS directed graph, ta có discovery time và finish time. Edge classification và ancestor relation có thể suy ra từ timestamps. SCC algorithms, articulation-point reasoning và topological ordering đều khai thác structure này.

## Recursive hay iterative DFS?

Recursive code ngắn và khớp mathematical structure, nhưng graph chain rất sâu có thể overflow call stack. Iterative DFS dùng explicit stack để kiểm soát memory rõ hơn. Nếu cần đúng postorder, stack entry thường phải mang thêm state/index hoặc dùng hai-phase entry để mô phỏng thời điểm “return” của recursion.
