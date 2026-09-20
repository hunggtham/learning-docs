# DAG, Topological Sort và SCC
**DAG, 위상 정렬, 강한 연결 요소**

Dependency graph thường cần không có directed cycle. **Directed Acyclic Graph (DAG / 방향 비순환 그래프)** là directed graph không có cycle.

## Topological sort

Topological order là linear ordering sao cho với mỗi edge `u -> v`, `u` đứng trước `v`. Chỉ DAG mới có topological ordering.

### Kahn's algorithm

Indegree 0 nghĩa node hiện không còn prerequisite. Ta đưa các node đó vào queue, lấy ra, giảm indegree của neighbors, và enqueue neighbor khi indegree về 0.

Nếu output có ít hơn `V` nodes, phần còn lại bị mắc trong cycle.

```js
function topoSort(n, g) {
  const indeg = Array(n).fill(0);
  for (let u = 0; u < n; u++) for (const v of g[u]) indeg[v]++;
  const q = [];
  let head = 0;
  for (let i = 0; i < n; i++) if (indeg[i] === 0) q.push(i);
  const order = [];
  while (head < q.length) {
    const u = q[head++];
    order.push(u);
    for (const v of g[u]) if (--indeg[v] === 0) q.push(v);
  }
  return order.length === n ? order : null;
}
```

## SCC

Strongly Connected Component là maximal set nodes mà mọi node reachable tới mọi node khác. Nếu collapse mỗi SCC thành một super-node, graph kết quả luôn là DAG.

Kosaraju dùng hai DFS passes; Tarjan dùng discovery/low-link values trong một pass.

## Mental Model

> Topological sort biến partial order của dependencies thành một schedule hợp lệ. SCC nén các vùng “reachability hai chiều” thành units để phần còn lại trở thành DAG.

## Topological order không duy nhất

Nếu tại một thời điểm có nhiều nodes indegree 0, chọn node nào trước đều có thể tạo valid topological order. Nếu muốn lexicographically smallest order, dùng min-heap thay queue; complexity tăng theo heap operations.

Đây là ví dụ data structure của frontier quyết định secondary objective.

## DP trên DAG

Một DAG cho sẵn dependency order. Sau topological sort, ta có thể tính longest path, path count hoặc scheduling earliest time bằng một pass relaxation.

Ví dụ earliest finish:

\[
finish[v]=duration[v]+\max_{u\to v}finish[u]
\]

Topological order đảm bảo predecessors đã được tính.

## Kosaraju SCC

Kosaraju làm DFS để lấy finish order, transpose graph, rồi DFS theo reverse finish order. Intuition: condensation graph của SCCs là DAG; finish order giúp bắt đầu từ component không bị “rò” sang component chưa muốn gom trong transpose.

## Tarjan low-link cho SCC

Tarjan giữ DFS stack của active nodes. `low[u]` phản ánh discovery index nhỏ nhất reachable trong active DFS region. Khi `low[u] == index[u]`, `u` là root của một SCC; pop stack tới `u`.

Low-link ở SCC có quan hệ họ hàng với low value trong bridge/articulation, nhưng semantics không hoàn toàn giống; đừng copy công thức máy móc.

## Condensation DAG

Collapse mỗi SCC thành một node. Result luôn là DAG; nếu còn cycle giữa components, chúng thực ra phải thuộc cùng SCC. Nhiều directed-graph problems vì thế có pipeline:

```text
find SCCs -> compress -> solve easier DAG problem
```

## Application

Circular module dependencies, mutually reachable states, deadlock-like dependency clusters và implication graphs đều có thể cần SCC reasoning.
