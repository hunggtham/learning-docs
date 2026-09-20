# DAG, Topological Sort và Strongly Connected Components
**DAG, sắp xếp tô-pô và thành phần liên thông mạnh / 방향 비순환 그래프, 위상 정렬, 강한 연결 요소**

Directed graph thường được dùng để biểu diễn dependency: package A cần B, task X phải chạy trước Y, course prerequisite, build target, data pipeline, state transition hoặc workflow. Khi dependency có cycle, câu hỏi “cái nào phải trước cái nào” có thể mất ý nghĩa hoặc cần xử lý đặc biệt.

**Directed Acyclic Graph (DAG / 방향 비순환 그래프)** là directed graph không có directed cycle. DAG quan trọng vì nó biến một quan hệ phụ thuộc phức tạp thành một structure có thể xử lý theo thứ tự.

## Mental Model

> DAG cho ta một **partial order**: không phải mọi cặp node đều so sánh được, nhưng mọi dependency edge đều yêu cầu một hướng trước-sau. Topological sort biến partial order đó thành một linear order hợp lệ.

Nếu graph có cycle, không có topological order đầy đủ vì một cycle tạo contradiction kiểu:

```text
A trước B
B trước C
C trước A
```

## Topological order là gì?

Một ordering `v1, v2, ..., vn` là topological order nếu với mọi edge:

\[
u \to v
\]

thì `u` xuất hiện trước `v`.

Topological order **không nhất thiết duy nhất**. Nếu hai tasks không phụ thuộc nhau, chúng có thể đổi chỗ mà vẫn hợp lệ.

Điều này rất quan trọng trong scheduling: graph chỉ encode constraints bắt buộc, không phải một schedule duy nhất.

## Kahn's Algorithm: reasoning bằng indegree

**Indegree (진입 차수)** của node là số incoming edges. Trong dependency graph, indegree 0 nghĩa node hiện không còn prerequisite chưa xử lý.

Kahn's algorithm:

1. tính indegree mọi node;
2. đưa tất cả node indegree 0 vào frontier;
3. lấy một node ra, append vào order;
4. “xóa logic” các outgoing edges bằng cách giảm indegree neighbors;
5. neighbor nào về 0 thì trở thành eligible;
6. nếu xử lý đủ `V` node, graph là DAG.

### JavaScript implementation

```js
function topoSort(n, g) {
  const indeg = Array(n).fill(0);
  for (let u = 0; u < n; u++) {
    for (const v of g[u]) indeg[v]++;
  }

  const q = [];
  let head = 0;
  for (let v = 0; v < n; v++) {
    if (indeg[v] === 0) q.push(v);
  }

  const order = [];

  while (head < q.length) {
    const u = q[head++];
    order.push(u);

    for (const v of g[u]) {
      if (--indeg[v] === 0) q.push(v);
    }
  }

  return order.length === n ? order : null;
}
```

Complexity:

\[
O(V+E)
\]

vì mỗi vertex vào queue tối đa một lần và mỗi edge giảm indegree đúng một lần.

## Tại sao Kahn phát hiện cycle?

Nếu còn nodes chưa xử lý nhưng không còn indegree-0 node, mỗi node còn lại có ít nhất một incoming edge từ region còn lại. Theo finite graph, follow incoming edges mãi cuối cùng phải lặp lại một vertex, tạo cycle.

Do đó:

```text
processedCount < V
```

là certificate rằng graph có directed cycle.

## Frontier data structure quyết định secondary objective

Nếu chỉ cần một order bất kỳ, queue đủ. Nếu muốn lexicographically smallest order, dùng min-heap thay queue:

```text
frontier = all indegree-0 nodes
always choose smallest eligible node
```

Correctness vẫn giống nhau; data structure chỉ thêm secondary objective.

Nếu muốn maximize parallelism, thay vì lấy một node, có thể lấy toàn bộ current frontier như một execution wave. Đây là basis cho build systems và workflow schedulers.

## DFS Topological Sort

Một cách khác dùng DFS. Node được append sau khi tất cả descendants đã được xử lý, sau đó reverse finish order.

```java
void dfs(int u) {
    state[u] = 1; // visiting

    for (int v : g.get(u)) {
        if (state[v] == 1) throw new CycleDetected();
        if (state[v] == 0) dfs(v);
    }

    state[u] = 2; // done
    order.add(u);
}
```

Ba trạng thái thường là:

```text
0 = unseen
1 = active / gray
2 = finished / black
```

Edge tới node đang `active` là back edge và chứng minh có directed cycle.

DFS topo và Kahn đều `O(V+E)`, nhưng mental model khác nhau:

```text
Kahn -> repeatedly remove prerequisites-free nodes
DFS  -> output node only after all descendants finish
```

## Topological order không phải “sort theo label”

Tên “sort” dễ gây hiểu nhầm. Topological sort không so sánh key như quicksort/mergesort. Nó linearize dependency constraints.

Nếu graph có nhiều valid orders, algorithm được phép trả bất kỳ order nào trừ khi problem thêm tie-breaking rule.

## DP trên DAG

DAG đặc biệt mạnh vì topological order chính là evaluation order của dynamic programming.

Giả sử `dp[v]` phụ thuộc các predecessor `u -> v`. Sau topological sort, khi tới `v`, mọi predecessor đã được xử lý.

### Longest path trên DAG

Longest path trên general graph rất khó vì cycle cho phép combinatorial explosion. Trên DAG:

\[
dp[v] = \max_{u \to v}(dp[u] + w(u,v))
\]

chỉ cần một pass theo topological order:

\[
O(V+E)
\]

### Path counting

Nếu muốn số paths từ source tới mỗi node:

```text
ways[source] = 1
for u in topo:
    for v in g[u]:
        ways[v] += ways[u]
```

Không cycle nghĩa là contribution chỉ chảy theo một chiều và không cần repeated relaxation.

## Scheduling và Critical Path Method

Trong project scheduling, vertex/edge có thể biểu diễn task và dependency. Earliest completion time có thể được tính bằng longest path trong DAG nếu durations không âm theo model phù hợp.

Ví dụ:

\[
finish[v] = duration[v] + \max_{u \to v} finish[u]
\]

Task trên longest dependency chain tạo **critical path**: delay ở đó trực tiếp kéo dài project finish time nếu không có slack.

Đây là connection trực tiếp giữa DAG algorithm và project/build scheduling.

## Strongly Connected Component là gì?

Trong directed graph, một **Strongly Connected Component (SCC / 강한 연결 요소)** là một maximal set vertices sao cho với mọi `u,v` trong component:

```text
u reaches v
v reaches u
```

Từ “maximal” quan trọng: không thể thêm vertex ngoài vào mà vẫn giữ mutual reachability.

SCC là cách nén những region mà directed reachability đã trở thành “hai chiều”.

## Condensation Graph

Collapse mỗi SCC thành một super-node. Nếu có edge giữa hai SCC khác nhau, tạo edge giữa super-nodes.

Graph kết quả gọi là **condensation DAG (축약 DAG)** và luôn là DAG.

Proof rất trực tiếp: nếu condensation graph có cycle giữa nhiều components, từ component nào cũng có thể đi vòng về component khác và quay lại; như vậy chúng thực ra mutually reachable và phải là cùng một SCC, contradiction.

Mental pipeline rất mạnh:

```text
graph directed phức tạp
        ↓
find SCCs
        ↓
collapse mutually-reachable regions
        ↓
solve easier problem on DAG
```

## Kosaraju's Algorithm

Kosaraju dùng hai DFS passes.

### Pass 1: finish order trên graph gốc

DFS graph và record vertices theo finishing time.

### Pass 2: DFS transpose theo reverse finish order

**Transpose graph** đảo mọi edge `u -> v` thành `v -> u`.

Process vertices theo decreasing finish time. Mỗi DFS trong transpose thu được một SCC.

### Intuition

Trong condensation DAG, finishing order của DFS có property giúp ta chọn một component mà trên transpose không “chảy” sang component chưa nên gom. Đảo edges biến sink/source relation, và reverse finish order cô lập từng component đúng lúc.

Complexity:

\[
O(V+E)
\]

nhưng cần transpose graph hoặc cách iterate reverse edges.

## Tarjan's SCC Algorithm

Tarjan tìm SCC trong một DFS bằng discovery index và stack active.

Mỗi node có:

```text
index[u] = thời điểm discover
low[u]   = smallest discovery index reachable
           trong active DFS region theo rule của SCC
```

Node được push lên stack khi active. Khi:

\[
low[u] = index[u]
\]

`u` là root của một SCC; pop stack cho tới `u`.

### Vì sao cần `onStack`?

Không phải mọi visited neighbor đều được phép kéo `low[u]` xuống. Edge tới node thuộc SCC đã hoàn tất không biểu diễn một cycle nằm trong active region hiện tại.

Vì vậy khi gặp edge tới visited node `v`, chỉ dùng `index[v]` để update low nếu `v` vẫn `onStack`.

Đây là một bug kinh điển khi implement Tarjan.

## Low-link trong Tarjan khác bridge low-link

Cùng tên `low` nhưng semantics không hoàn toàn giống nhau.

Bridge/articulation trong undirected graph hỏi subtree có thể đi ngược tới ancestor nào mà không dùng parent edge.

Tarjan SCC hỏi active directed DFS region có thể reach discovery index nhỏ nhất nào trong current stack semantics.

Không nên copy công thức giữa hai algorithms mà không hiểu invariant.

## Java skeleton cho Tarjan SCC

```java
int timer = 0;
int[] index, low, comp;
boolean[] onStack;
Deque<Integer> stack = new ArrayDeque<>();

void dfs(int u) {
    index[u] = low[u] = timer++;
    stack.push(u);
    onStack[u] = true;

    for (int v : g.get(u)) {
        if (index[v] == -1) {
            dfs(v);
            low[u] = Math.min(low[u], low[v]);
        } else if (onStack[v]) {
            low[u] = Math.min(low[u], index[v]);
        }
    }

    if (low[u] == index[u]) {
        while (true) {
            int v = stack.pop();
            onStack[v] = false;
            comp[v] = componentCount;
            if (v == u) break;
        }
        componentCount++;
    }
}
```

Recursive DFS có thể stack-overflow trên graph cực sâu. Production implementation có thể cần iterative traversal hoặc tăng stack có chủ đích tùy runtime.

## SCC và cycle detection

Một SCC có nhiều hơn một vertex chắc chắn chứa directed cycle. SCC một vertex cũng có cycle nếu có self-loop.

Do đó SCC decomposition không chỉ nói “có cycle không”, mà còn cho biết **cycle clusters ở đâu** và cách chúng liên hệ với phần acyclic còn lại.

## Application: dependency systems

### Build graph

Nếu modules A, B, C tạo SCC, chúng có circular dependency. Build system có thể reject, bundle chúng thành một unit hoặc yêu cầu refactor boundary.

### Package managers

Dependency SCC có thể biểu diễn nhóm packages phụ thuộc vòng nhau. Condensation DAG cho thứ tự xử lý giữa groups.

### State machines

SCC là region mà các states có thể quay lại lẫn nhau. Một SCC không có outgoing edge trong condensation DAG là terminal recurrent region theo deterministic/nondeterministic model phù hợp.

### Web/link graph

SCC có thể biểu diễn communities với mutual reachability, dù graph analytics production thường dùng thêm metrics khác.

## 2-SAT connection

Trong implication graph của 2-SAT, mỗi boolean literal có node và clause tạo implications. Formula unsatisfiable nếu một variable `x` và `¬x` nằm trong cùng SCC.

Sau SCC decomposition, condensation order còn giúp derive assignment.

Đây là một example mạnh nơi logic problem được biến thành directed reachability structure.

## DAG transitive reduction và transitive closure

Hai concepts thường bị nhầm.

**Transitive closure** thêm thông tin reachability: edge logic `u -> v` tồn tại nếu `v` reachable từ `u`.

**Transitive reduction** cố bỏ các edge dư mà vẫn giữ cùng reachability relation. Với DAG, transitive reduction là unique theo điều kiện chuẩn.

Ví dụ nếu có:

```text
A -> B
B -> C
A -> C
```

edge `A -> C` là redundant về reachability.

Trong dependency visualization, reduction giúp graph dễ đọc hơn; closure giúp query reachability nhanh hơn nhưng có thể tốn `O(V^2)` space.

## Uniqueness của topological order

Topological order unique khi tại mỗi bước Kahn chỉ có đúng một eligible indegree-0 node. Nếu có hai choices, ít nhất hai valid orders có thể tồn tại.

Equivalent view: trong một topological order unique, mỗi cặp consecutive vertices phải có dependency structure buộc thứ tự phù hợp.

Đây là useful property khi problem hỏi “schedule có duy nhất không?”.

## Common misconceptions

**“Có topological sort cho mọi directed graph.”** Sai. Chỉ DAG mới có full topological order.

**“Kahn không output đủ node nghĩa là algorithm bug.”** Có thể graph có cycle; đó chính là detection mechanism.

**“Topological order là unique.”** Thường không.

**“SCC giống connected component của undirected graph.”** Không. Directed reachability phải đúng cả hai chiều.

**“Tarjan low giống bridge low nên dùng cùng formula.”** Không nên; invariants khác nhau.

**“Collapse SCC có thể vẫn còn cycle.”** Không. Nếu còn cycle, các components trên cycle phải là một SCC lớn hơn.

## Testing

Cho topological sort, sau khi có `pos[v]`, kiểm mọi edge:

\[
pos[u] < pos[v]
\]

Nếu algorithm report cycle, có thể differential-test với DFS color-state trên graph nhỏ.

Cho SCC, kiểm:

- vertices cùng component mutually reachable trên small reference graph;
- vertices khác component không mutually reachable cả hai chiều;
- condensation graph acyclic;
- self-loop và isolated vertex;
- parallel edges;
- chain, one big cycle, many small SCCs.

Property-based tests đặc biệt hữu ích với Tarjan vì bug `onStack` và low-link thường chỉ xuất hiện ở graph shape cụ thể.

## Mental Model mở rộng

> Topological sort là cách **tháo một dependency graph từ ngoài vào**. SCC là cách **nén các vùng không thể áp một thứ tự một chiều bên trong**. Sau khi nén mọi mutual-reachability region, phần còn lại bắt buộc trở thành DAG.

Khi gặp directed graph có cycles, thay vì cố áp dụng DAG algorithm trực tiếp, hãy hỏi liệu cycle có semantic meaning gì và liệu SCC condensation có biến problem thành DAG problem dễ hơn không.