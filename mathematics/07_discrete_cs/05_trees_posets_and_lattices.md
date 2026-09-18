# Cây, thứ tự bộ phận và lattice

Discrete mathematics thường nghiên cứu structure thay vì continuous magnitude. Ba structures rất hữu ích trong CS là tree, partial order và lattice. Chúng xuất hiện trong file systems, syntax trees, dependency graphs, version histories, type hierarchies và distributed systems.

## Tree là graph không có cycle và connected

Một tree (Tree / 트리) là undirected graph connected và acyclic.

Với `n` vertices, một tree có đúng

```math
n-1
```

edges.

Tại sao? Bắt đầu từ một vertex. Mỗi khi thêm một new vertex mà vẫn giữ connected và không tạo cycle, ta cần đúng một edge nối nó vào structure hiện tại. Thêm `n-1` vertices cần `n-1` edges.

Nếu connected graph có ít hơn `n-1` edges, không đủ links để nối mọi vertices. Nếu có nhiều hơn mà vẫn connected, ít nhất một edge tạo cycle.

## Rooted tree và hierarchy

Chọn một root tạo orientation parent–child. Mỗi node ngoài root có exactly one parent trong tree.

Depth là số edges từ root tới node. Height liên quan longest downward path.

File system, DOM tree và abstract syntax tree dùng hierarchy này. Nhưng Git history không luôn là tree vì merge commit có thể có nhiều parents; nó là directed acyclic graph.

## Binary tree và search

Trong binary search tree, mỗi node có at most two children và ordering invariant thường là left keys nhỏ hơn node, right keys lớn hơn.

Nếu tree balanced, height khoảng

```math
O(\log n),
```

vì mỗi level có thể roughly double số nodes. Nếu degenerate thành chain, height là `O(n)`.

Do đó complexity không đến từ tên “binary tree” mà từ geometric growth của number of reachable nodes theo depth.

## Spanning tree

Cho connected graph có cycles, spanning tree giữ tất cả vertices nhưng chỉ giữ đủ edges để connected mà không cycle.

Minimum spanning tree chọn spanning tree có total edge weight nhỏ nhất. Applications gồm network design, clustering và approximation.

Algorithms như Kruskal/Prim use cut/cycle properties để chọn edges mà không cần thử mọi trees.

## Partial order

Một quan hệ `\preceq` trên set `P` là partial order nếu reflexive, antisymmetric và transitive.

“Partial” nghĩa không phải mọi pair đều comparable.

Ví dụ subset relation `\subseteq`: với sets `{1}` và `{2}`, neither là subset của other. Nhưng relation vẫn có order structure.

Dependency relation thường partial: task A phải trước B, nhưng task C có thể independent nên không cần so trước/sau với A.

## Hasse diagram

Hasse diagram biểu diễn finite poset bằng cách bỏ self-loops và transitive edges, chỉ giữ cover relations.

Nó làm hierarchy lộ ra mà không làm graph cluttered. Divisibility trên positive integers là classic poset: `a\preceq b` nếu `a` divides `b`.

## Total order và topological sorting

Total order yêu cầu mọi pair comparable. Partial order có thể được mở rộng thành một linear order phù hợp constraints.

Trong DAG, topological sort tạo sequence các vertices sao cho mọi directed edge `u\to v` đặt `u` trước `v`.

Build systems, package dependencies và course prerequisites dùng chính idea này.

## Lattice

Một lattice (격자) là poset trong đó mọi pair có greatest lower bound (meet) và least upper bound (join).

Với subsets dưới inclusion:

```math
A\wedge B=A\cap B,
```

```math
A\vee B=A\cup B.
```

Boolean algebra là một distributive complemented lattice.

Trong type systems, lattice-like structures mô tả subtype joins/meets. Trong dataflow analysis của compilers, fixpoint computation thường diễn ra trên lattices để đảm bảo convergence dưới monotonic transfer functions.

## Knowledge Connection

Trees là special graphs. Posets formalize dependency without forcing arbitrary total order. Lattices nối order theory với logic, set operations và static analysis. Topological sorting biến partial constraints thành executable sequence.

## Mental Model

> Tree encode “một đường cha duy nhất”; partial order encode “một số things phải trước/nhỏ hơn things khác nhưng không cần so mọi pair”; lattice thêm khả năng merge hai states bằng join/meet có nghĩa toán học.

## Common Misconceptions

Mọi hierarchy không nhất thiết là tree; multiple inheritance hoặc merges tạo DAG. Acyclic graph không tự động connected nên chưa chắc là tree. Partial order không có nghĩa relation “thiếu chính xác”; incomparability là feature. Topological order thường không unique.
