# Cây, thứ tự bộ phận và lattice: cấu trúc của hierarchy, dependency và merge

Discrete mathematics không chỉ nghiên cứu “các số rời rạc”. Một phần rất quan trọng là nghiên cứu **structure**: object nào phụ thuộc object nào, hierarchy được tổ chức ra sao, states có thể so sánh hay merge như thế nào.

Ba structures quan trọng trong Computer Science là:

```text
tree → hierarchy không cycle
partial order → dependency/order không cần compare mọi pair
lattice → partial order có operation merge/refine có meaning
```

Chúng xuất hiện trong file systems, syntax trees, dependency graphs, build systems, type systems, version histories, compilers, distributed systems và abstract interpretation.

## 1. Tree: connected + acyclic

Một tree (cây / 트리) là undirected graph vừa:

```text
connected
acyclic
```

Hai properties này together tạo structure rất mạnh.

Với `n` vertices, tree có đúng:

```math
n-1
```

edges.

### Proof idea

Bắt đầu từ một vertex. Mỗi new vertex muốn nối vào existing connected acyclic structure phải dùng exactly one new edge.

Nếu không edge → disconnected.
Nếu ≥2 new edges tới existing tree → tạo cycle.

Thêm `n-1` vertices cần `n-1` edges.

## 2. Các characterization tương đương của tree

Với finite undirected graph, các statements sau equivalent:

```text
connected và acyclic
connected với n-1 edges
acyclic với n-1 edges
between every pair of vertices có unique simple path
```

Unique-path viewpoint cực hữu ích: hierarchy tree đảm bảo giữa hai nodes chỉ có một route đơn giản.

## 3. Rooted tree: hierarchy xuất hiện khi chọn root

Chọn một root biến undirected tree thành hierarchy.

Mỗi non-root node có exactly one parent.

Concepts:

```text
parent / child
ancestor / descendant
depth
height
subtree
leaf
```

File system directory tree, DOM tree và many ASTs dùng rooted structure.

Nhưng Git commit history không phải tree nói chung vì merge commit có thể có multiple parents; nó là DAG.

## 4. Traversal: DFS và BFS trên tree

Tree traversal không chỉ là implementation detail.

Depth-first search đi sâu theo branch trước. Nó tự nhiên cho recursive structure:

```text
preorder
inorder
postorder
```

Breadth-first search đi theo levels, useful cho shortest-depth questions trong unweighted trees.

Traversal order quyết định semantics trong compilers, UI trees và serialization.

## 5. Binary tree không đồng nghĩa binary search tree

Binary tree chỉ yêu cầu mỗi node có at most two children.

Binary search tree thêm ordering invariant:

```text
left subtree keys < node key
right subtree keys > node key
```

Complexity phụ thuộc height.

Balanced BST:

```math
h=O(\log n).
```

Degenerate chain:

```math
h=O(n).
```

Do đó “binary” không tự tạo `O(log n)`.

## 6. Why balanced trees give logarithmic depth

Nếu mỗi level có thể roughly double nodes, total nodes tới height `h` scale như:

```math
1+2+4+\cdots+2^h\approx2^{h+1}.
```

Invert relation:

```math
h\approx\log_2n.
```

Logarithmic lookup đến từ exponential growth of capacity by depth.

## 7. Heap: tree cho priority, không cho sorted traversal

Binary heap là complete binary tree với heap property:

```text
min-heap: parent ≤ children
max-heap: parent ≥ children
```

Heap support efficient min/max extraction nhưng không guarantee left subtree < right subtree như BST.

Different invariants serve different operations.

## 8. Spanning tree: remove cycles nhưng giữ connectivity

Cho connected graph có cycles. Spanning tree giữ all vertices nhưng chỉ enough edges để graph connected và acyclic.

Every spanning tree has:

```math
n-1
```

edges.

Minimum spanning tree (MST) minimizes total edge weight.

Applications:

```text
network design
clustering
road/cable layout
approximation algorithms
```

## 9. Cut property intuition của MST

Chia vertices thành hai groups. Edge nhẹ nhất crossing một cut, dưới suitable tie reasoning, có thể thuộc một MST.

Kruskal/Prim algorithms exploit local safety properties để tránh enumerate all spanning trees.

Đây là example của proof-guided greedy algorithm.

## 10. Partial order: order không bắt buộc mọi pair comparable

Relation `\preceq` là partial order nếu:

```text
reflexive
antisymmetric
transitive
```

Antisymmetric:

```math
a\preceq b\text{ và }b\preceq a
\Rightarrow a=b.
```

Partial nghĩa có thể tồn tại `a,b` incomparable.

Đây không phải thiếu information; incomparability là structure thật.

## 11. Ví dụ partial orders

Subset inclusion:

```math
A\subseteq B.
```

Divisibility:

```math
a\mid b.
```

Task dependency:

```text
A must finish before B
```

Version ancestry trong DAG.

Hai independent tasks có thể incomparable.

## 12. Hasse diagram

Finite poset có thể visualize bằng Hasse diagram.

Ta bỏ:

```text
self-loops
transitive edges
```

và chỉ giữ cover relations.

Nếu `a<b` nhưng không có `c` với `a<c<b`, `b` covers `a`.

Hasse diagram làm structural hierarchy rõ hơn full relation graph.

## 13. Minimal/maximal khác minimum/maximum

Trong poset:

```text
minimal element → không có element strictly below nó
minimum → ≤ mọi element khác
```

Có thể có nhiều minimal elements nhưng at most one minimum.

Tương tự maximal vs maximum.

Đây là distinction thường gây nhầm.

## 14. Chains và antichains

Chain là subset mà mọi pair comparable.

Antichain là subset mà mọi distinct pair incomparable.

Chain represent fully ordered subset; antichain represent maximal parallelism/no dependency relations.

Trong scheduling, antichain size liên hệ degree of potential concurrency.

## 15. Topological sorting: linear extension của partial order

DAG encodes precedence constraints.

Topological sort tạo total order compatible với all directed edges.

Nếu nhiều independent nodes, topological order không unique.

Build systems, package installation, course prerequisites và workflow engines dùng idea này.

## 16. Cycle nghĩa precedence inconsistent

Nếu dependency graph có directed cycle:

```text
A before B
B before C
C before A
```

không có topological order.

Cycle detection vì vậy không chỉ là graph problem; nó phát hiện inconsistent ordering constraints.

## 17. Lattice: mọi pair có meet và join

Một lattice là poset trong đó mỗi pair `a,b` có:

```text
meet a∧b → greatest lower bound
join a∨b → least upper bound
```

Meet là common information/state thấp nhất vẫn above all common lower constraints.
Join là smallest state chứa/bao cả hai.

Meaning cụ thể phụ thuộc poset.

## 18. Power-set lattice

Trên subsets của universe `U`, order là inclusion:

```math
A\preceq B\iff A\subseteq B.
```

Then:

```math
A\wedge B=A\cap B,
```

```math
A\vee B=A\cup B.
```

Bottom:

```math
\varnothing.
```

Top:

```math
U.
```

Đây là canonical lattice example.

## 19. Boolean algebra như distributive complemented lattice

Power-set lattice có complement:

```math
A^c=U\setminus A.
```

và distributive laws.

Boolean logic vì vậy có deep order-theoretic structure; AND/OR tương ứng meet/join.

## 20. Lattice trong type systems

Subtype relation có thể tạo partial order.

Join của two types có thể represent least common supertype; meet có thể represent greatest common subtype nếu tồn tại.

Type inference và flow analysis thường cần operations giống lattice join để merge information từ control-flow branches.

## 21. Dataflow analysis trong compiler

Mỗi program point có abstract state, ví dụ set variables known constant/live/reaching definitions.

Transfer functions propagate states.

At merge point:

```text
state from path A
join
state from path B
```

Lattice cung cấp mathematically well-defined merge.

Monotonicity + finite-height/appropriate completeness giúp iterative fixpoint algorithms converge.

## 22. Fixed points trên lattices

Nếu function `F` monotone trên suitable complete lattice, fixed-point theorems cho conditions existence của least/greatest fixed points.

Compiler analysis, semantics và model checking dùng principle này.

Iteration:

```text
x0
F(x0)
F(F(x0))
...
```

có thể tiến tới stable abstract state.

## 23. Distributed systems và join-semilattice

CRDTs thường dùng join-semilattice structure để merge replicas.

Nếu merge operation associative, commutative, idempotent:

```text
merge(a,b)=merge(b,a)
merge(merge(a,b),c)=merge(a,merge(b,c))
merge(a,a)=a
```

thì repeated/out-of-order merging có thể converge under model assumptions.

Đây là một application rất concrete của order/lattice theory.

## 24. Trees vs DAGs vs posets

Một tree imposes unique-parent/path structure.

A DAG permits multiple parents.

A poset là abstract relation; DAG/Hasse diagram có thể represent finite poset.

Không nên đồng nhất three concepts dù chúng liên quan.

## 25. Worked example: build dependencies

Suppose:

```text
A → C
B → C
C → D
B → E
```

`A` và `B` incomparable. `C` cần both predecessors. Possible topological orders:

```text
A,B,C,E,D
B,A,E,C,D
```

miễn constraints giữ.

Scheduler có thể parallelize `A` và `B`.

## 26. Worked example: set lattice merge

Suppose dataflow state là set variables definitely initialized.

Path 1:

```text
{a,b}
```

Path 2:

```text
{a,c}
```

Nếu muốn “definitely initialized on all paths”, merge natural là intersection:

```text
{a}
```

Nếu muốn “possibly initialized on some path”, merge có thể là union:

```text
{a,b,c}
```

Cùng sets nhưng order/analysis semantics quyết định meet/join nào relevant.

## Knowledge Connection

```text
graph theory
→ trees / DAGs
→ partial order
→ Hasse representation
→ lattices
→ fixed-point computation
→ compiler analysis / distributed merge
```

Trees connect to recursion and algorithm complexity. Posets connect to scheduling and dependency management. Lattices connect logic/set theory với static analysis và semantics.

## Mental Model

> Tree trả lời “mỗi node nằm trong hierarchy nào?”. Poset trả lời “những constraints trước/sau nào tồn tại?”. Lattice thêm capability “merge/refine hai states theo cách có order meaning”.

## Common Misconceptions

Mọi hierarchy không phải tree; multiple inheritance/merge tạo DAG. DAG không nhất thiết connected. Partial order không cần compare mọi pair. Minimal không đồng nghĩa minimum. Topological order thường không unique. Lattice join không luôn là numeric max; meaning phụ thuộc partial order.
