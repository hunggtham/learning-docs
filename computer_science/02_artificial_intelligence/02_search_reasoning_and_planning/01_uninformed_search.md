# Uninformed Search: BFS, DFS, UCS và các chiến lược nền tảng

**Uninformed Search (무정보 탐색 / tìm kiếm không dùng heuristic)** giải bài toán chỉ bằng problem definition: initial state, actions, transition, goal và path cost. Algorithm không có domain-specific estimate cho biết state nào “gần goal hơn”.

Điều này không làm uninformed search trở nên lỗi thời. Nó là baseline giúp ta hiểu rõ trade-off giữa completeness, optimality, time và memory. Heuristic search như A* chỉ thực sự dễ hiểu khi ta thấy điều gì xảy ra nếu không có heuristic.

Xem trước: [State Space and Search](./00_state_space_and_search.md).

## Một abstraction chung

Mọi strategy đều có frontier, nhưng khác cách lấy node:

```text
BFS → queue FIFO
DFS → stack LIFO
UCS → priority queue by g(n)
Depth-limited → DFS + depth bound
Iterative deepening → repeated depth-limited DFS
Bidirectional → two searches meeting
```

Các properties phụ thuộc assumptions về branching, goal depth và edge cost.

## Breadth-First Search

Breadth-First Search (BFS / 너비 우선 탐색) expand nodes theo depth tăng dần.

Nếu frontier là FIFO queue:

```pseudo
queue ← [start]
visited ← {start}

while queue not empty:
    n ← pop_front(queue)
    if goal(n): return path(n)

    for s in successors(n):
        if s not in visited:
            visited.add(s)
            queue.push_back(s)
```

BFS first explores all states depth 0, rồi depth 1, depth 2...

### Khi nào BFS optimal?

Nếu mọi step có cùng cost, shortest depth cũng là lowest path cost. Khi đó BFS optimal.

Nếu edge costs khác nhau, shallowest path có thể đắt hơn path sâu hơn. Lúc đó BFS không guarantee cost-optimal.

### Complexity

Với branching factor `b` và shallowest goal depth `d`, worst-case time/memory thường exponential:

\[
O(b^d)
\]

Memory là weakness lớn: BFS phải giữ frontier của whole level.

### Ví dụ

Graph:

```text
S → A → G
 \  
  → B → C → G
```

Nếu edge cost equal, BFS tìm `S-A-G` trước vì depth nhỏ hơn.

## Depth-First Search

Depth-First Search (DFS / 깊이 우선 탐색) đi sâu một branch trước khi backtrack.

Stack/recursion:

```pseudo
stack ← [start]
visited ← set()

while stack not empty:
    n ← pop(stack)
    if n in visited: continue
    visited.add(n)

    if goal(n): return path(n)

    push successors(n)
```

### Strength

DFS memory thấp hơn BFS. Nếu maximum depth `m`, rough space complexity:

\[
O(bm)
\]

với standard tree-storage reasoning, thay vì exponential frontier theo shallow goal depth.

### Weakness

DFS có thể lao sâu vào branch rất dài hoặc infinite nếu không cycle/depth control.

Nó không optimal. Goal tìm đầu tiên phụ thuộc successor ordering.

### Khi DFS useful?

- memory constrained;
- solution expected deep;
- chỉ cần any solution;
- exhaustive traversal/backtracking;
- topological/cycle-related graph algorithms trong CS broader context.

## Depth-Limited Search

Depth-Limited Search (DLS) là DFS với depth limit `ℓ`.

Nếu reached depth `ℓ`, node không expand nữa.

Nó tránh infinite descent nhưng có thể miss solution deeper than limit.

Cần phân biệt return states:

```text
SUCCESS
FAILURE    → không có solution trong explored space
CUTOFF     → có thể có solution sâu hơn limit
```

Distinction này quan trọng cho Iterative Deepening.

## Iterative Deepening DFS

Iterative Deepening Depth-First Search (IDDFS) chạy DLS với limits:

```text
0, 1, 2, 3, ...
```

Nó nghe có vẻ wasteful vì expand upper nodes nhiều lần. Nhưng trong exponential tree, phần lớn nodes nằm ở deepest level, nên repeated upper-level work relatively small.

Với unit costs, IDDFS kết hợp:

- completeness của BFS;
- optimal shallowest-depth behavior của BFS;
- memory profile gần DFS.

Time vẫn khoảng:

\[
O(b^d)
\]

space khoảng:

\[
O(bd)
\]

under common formulation.

## Uniform-Cost Search

Uniform-Cost Search (UCS / 균일 비용 탐색) expand node có lowest path cost:

\[
g(n)
\]

Nó là Dijkstra-like search từ start tới goal trong AI terminology.

Priority queue:

```pseudo
frontier ← PQ((0,start))
best[start] ← 0

while frontier:
    g,n ← pop_lowest_cost()

    if g != best[n]: continue
    if goal(n): return path

    for edge(n,s,c):
        new_g ← g + c
        if s unseen OR new_g < best[s]:
            best[s] ← new_g
            push(new_g,s)
```

### Vì sao goal test thường khi pop, không phải khi generate?

Một goal có thể được generated qua expensive path trước, rồi sau đó có cheaper path chưa explored.

Khi UCS pops goal as lowest-cost frontier node under nonnegative costs, ta mới có optimality guarantee.

## BFS là special case của UCS

Nếu every edge cost = 1:

\[
g(n)=depth(n)
\]

UCS ordering theo path cost tương đương BFS ordering theo depth.

Đây là useful unification:

```text
BFS = UCS khi step cost uniform
```

## Negative edge cost

UCS/Dijkstra assumptions require nonnegative edge cost for standard optimality logic.

Nếu negative edges tồn tại, một node tưởng cheapest hiện tại có thể later được cải thiện qua negative-cost path.

Các algorithms như Bellman–Ford handle negative edges trong graph shortest path, và negative cycles làm shortest path undefined (`-∞`).

Trong AI cost design, negative rewards/costs cần careful formulation.

## Cycle checking

Trong tree search:

```text
A → B → C → A → ...
```

có thể tạo infinite expansion.

Path-based cycle checking ngăn state lặp trên current path.

Global explored set mạnh hơn, nhưng với weighted search cần có best-cost logic: “đã thấy state” không đủ nếu later path rẻ hơn.

## Frontier duplicates

Có hai implementation styles:

1. decrease-key/update entry trong priority queue;
2. push new better entry và khi pop bỏ stale entry.

Style 2 thường đơn giản hơn với standard heap libraries.

```python
if popped_cost != best[state]:
    continue
```

Mental model: `best` map là source of truth, heap có thể chứa stale candidates.

## Bidirectional Search

Nếu start `S` và exact goal `G` đều known, search forward từ `S` và backward từ `G`.

Idealized node counts:

\[
O(b^{d/2}) + O(b^{d/2})
\]

so với:

\[
O(b^d)
\]

cho one-direction BFS.

### Conditions thực tế

Bidirectional search cần:

- generate predecessors hoặc reverse edges;
- efficient intersection test;
- careful stopping criterion với weighted costs;
- manageable frontier from both sides.

Nếu goal là predicate rộng (“bất kỳ schedule hợp lệ”), backward search có thể không straightforward.

## Search order và tie-breaking

Ngay cả cùng BFS/UCS, thứ tự generate successors ảnh hưởng path returned khi multiple optimal solutions tồn tại.

A* tie-breaking cũng ảnh hưởng nodes expanded.

Reproducibility cần deterministic successor ordering khi output path matters.

## Tree complexity và graph complexity

Textbook often expresses complexity bằng `b,d,m`, nhưng finite graph có `|V|,|E|`.

BFS graph traversal:

\[
O(|V|+|E|)
\]

nếu mỗi node/edge processed once.

Priority-queue shortest path có complexity liên quan `|E| log |V|` tùy heap implementation.

Hai notation trả lời two views:

```text
AI search tree view → branching/depth
Graph algorithm view → vertices/edges
```

## Example: weighted routes

Suppose:

```text
S --1--> A --100--> G
 \                    
  --10--> B --10--> C --10--> G
```

BFS thấy `S-A-G` depth 2 và trả path cost 101.

UCS explores theo accumulated cost và tìm `S-B-C-G` cost 30.

Đây là lý do “ít bước hơn” không đồng nghĩa “rẻ hơn”.

## Memory as algorithmic resource

BFS thường fail vì RAM trước CPU.

Suppose frontier 10 million nodes, mỗi node metadata 100 bytes:

```text
≈ 1 GB
```

thực tế object overhead có thể lớn hơn nhiều.

Compact state encoding, parent reconstruction strategy, external-memory search hoặc iterative deepening có thể quan trọng hơn micro-optimizing expansion.

## Iterative deepening và modern reasoning systems

Idea allocate progressively larger depth budget có analog trong modern systems:

```text
try shallow/simple reasoning
if insufficient → allow deeper search
```

Không nên gọi mọi “reasoning depth setting” là literal IDDFS, nhưng resource-bounded iterative expansion là recurring design pattern.

## Beam Search: informed bởi score nhưng incomplete

Beam Search thường được học gần sequence decoding hơn uninformed search, nhưng useful contrast.

At each depth chỉ giữ top `k` candidates theo score.

```text
all possibilities exponential
       ↓ prune
keep beam width k
```

Beam search tiết kiệm memory/time nhưng không complete và không guarantee global optimum.

Machine translation và sequence generation historically use beam search extensively.

## Search under resource limits

Real systems có:

- time budget;
- memory budget;
- API/tool cost;
- token budget.

Một theoretically optimal search may be unusable.

Resource-bounded algorithms trade solution quality for computation.

This idea later appears in anytime algorithms, beam search, Monte Carlo Tree Search and LLM agent planning.

## Anytime algorithms

Anytime algorithm có thể return current best solution nếu interrupted, và quality cải thiện khi có thêm time.

This is valuable when exact compute budget uncertain.

Weighted A* và iterative improvement methods can have anytime variants.

## Choosing an uninformed strategy

| Situation | Strategy intuition |
|---|---|
| Unit cost, shallow solution | BFS |
| Memory tight, any solution | DFS / DLS |
| Unknown goal depth, unit cost | IDDFS |
| Different nonnegative costs | UCS |
| Exact start + goal, reversible graph | Bidirectional search |

Table này là starting heuristic, không substitute analysis of actual graph size, cycles, constraints và memory representation.

## Mental Model

```text
BFS   = optimize depth
DFS   = commit to one branch, save memory
DLS   = DFS with horizon
IDDFS = BFS-like depth guarantee using DFS-like memory
UCS   = optimize accumulated path cost
Bidirectional = reduce effective depth by meeting in middle
```

## Common Misconceptions

### “BFS luôn tìm shortest path”

Chỉ shortest number of edges; cost-optimal khi step costs equal/uniform.

### “DFS nhanh hơn BFS”

Không universal. Nó có different exploration order và lower memory, nhưng có thể search huge wrong branch.

### “Visited set chỉ là optimization”

Trong cyclic graphs, duplicate detection có thể quyết định termination và correctness.

### “UCS goal thấy lần đầu là đủ”

Goal cần được settled/popped theo lowest path cost logic; generated first chưa guarantee optimal.

## Knowledge Connection

Uninformed Search cung cấp baseline để thấy heuristic mang lại gì. [Heuristic Search](./02_heuristic_search.md) sẽ thêm estimate `h(n)` để focus expansion, còn Planning sẽ add richer action preconditions/effects.

Khi chọn search algorithm, hãy bắt đầu bằng graph properties: branching factor, depth, edge costs, cycles, memory budget và whether goal/reverse transitions known.