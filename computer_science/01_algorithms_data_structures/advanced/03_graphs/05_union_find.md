# Union-Find / Disjoint Set Union
**Tập hợp rời nhau (Disjoint Set Union / 서로소 집합)**

Union-Find, thường gọi là **Disjoint Set Union (DSU / 서로소 집합 자료구조)**, được thiết kế cho một câu hỏi rất hẹp nhưng xuất hiện rất nhiều:

> Khi các phần tử liên tục được hợp nhất thành các nhóm, làm sao biết nhanh hai phần tử có đang thuộc cùng một nhóm hay không?

DSU không cố lưu toàn bộ topology của graph. Nó không biết path giữa hai vertices, không biết degree, không biết shortest path. Nó chỉ duy trì **component identity**.

## Hai operation cốt lõi

`find(x)` trả representative của component chứa `x`.

`union(a,b)` hợp nhất hai components nếu chúng khác nhau.

Nếu:

```text
find(a) == find(b)
```

thì `a` và `b` đã connected theo quan hệ merge hiện tại.

## Mental Model

> DSU nén một partition của tập phần tử thành một forest. Mỗi tree đại diện một component; root chỉ là **identifier nội bộ**, không phải vertex “quan trọng nhất”.

Điểm mạnh của DSU đến từ việc nó từ chối lưu thông tin không cần thiết. Nếu bài toán chỉ hỏi connectivity dưới operation merge, path chi tiết là overhead.

## Representation bằng parent forest

Ban đầu mỗi element là một set riêng:

```text
parent[x] = x
```

Khi merge hai sets, ta nối root của một tree vào root của tree kia.

Ví dụ:

```text
0   1   2   3
```

sau `union(0,1)` và `union(2,3)`:

```text
0      2
|      |
1      3
```

sau `union(0,2)`:

```text
    0
   / \
  1   2
      |
      3
```

Tất cả nodes trong cùng tree có cùng representative root.

## Naive union có vấn đề gì?

Nếu luôn gắn root mới vào root cũ một cách tùy ý, có thể tạo chain:

```text
0 <- 1 <- 2 <- 3 <- 4 <- ...
```

Khi đó `find(n-1)` là `O(n)`.

DSU hiệu quả nhờ hai optimization phối hợp:

1. **union by size/rank (크기/랭크 기준 합치기)**;
2. **path compression (경로 압축)**.

## Union by size

Khi merge hai components, gắn root của tree nhỏ hơn dưới root của tree lớn hơn.

```java
boolean union(int a, int b) {
    int ra = find(a);
    int rb = find(b);

    if (ra == rb) return false;

    if (size[ra] < size[rb]) {
        int t = ra;
        ra = rb;
        rb = t;
    }

    parent[rb] = ra;
    size[ra] += size[rb];
    return true;
}
```

### Tại sao size heuristic giúp height nhỏ?

Mỗi khi depth của một node tăng 1 do tree của nó bị gắn dưới tree khác, component mới ít nhất gấp đôi component cũ nếu luôn gắn smaller vào larger.

Một node không thể trải qua hơn `log2 n` lần “component size ít nhất gấp đôi”. Vì vậy chỉ union-by-size đã bound tree height ở `O(log n)`.

## Path compression

`find(x)` không chỉ đi lên root; nó còn sửa parent của các nodes trên path để những lần tìm sau ngắn hơn.

Recursive Java:

```java
int find(int x) {
    if (parent[x] != x) {
        parent[x] = find(parent[x]);
    }
    return parent[x];
}
```

Nếu path ban đầu:

```text
7 -> 5 -> 3 -> 0
```

sau `find(7)` có thể thành:

```text
7 -> 0
5 -> 0
3 -> 0
```

Một operation hiện tại trả thêm maintenance cost để future operations rẻ hơn.

## Iterative find trong C

Recursion không bắt buộc:

```c
int dsu_find(DSU *d, int x) {
    int root = x;

    while (d->parent[root] != root) {
        root = d->parent[root];
    }

    while (d->parent[x] != x) {
        int p = d->parent[x];
        d->parent[x] = root;
        x = p;
    }

    return root;
}
```

Pass đầu tìm root; pass sau compress path. Iterative form tránh recursion depth concern và làm mutation flow rõ ràng.

## `O(alpha(n))` thực sự nghĩa là gì?

Kết hợp union-by-size/rank với path compression cho amortized complexity:

\[
O(\alpha(n))
\]

mỗi operation, trong đó `\alpha` là **inverse Ackermann function**.

Không cần học chi tiết Ackermann function để dùng DSU. Điều cần hiểu là `alpha(n)` tăng cực chậm; với mọi `n` thực tế, nó là một hằng số rất nhỏ.

Nhưng nói “DSU là O(1)” về mặt lý thuyết là không chính xác. Cách nói tốt hơn:

> amortized gần constant trong mọi input size thực tế, với bound `O(alpha(n))`.

## Amortized analysis ở đây đến từ đâu?

Một `find` riêng lẻ vẫn có thể đi qua nhiều nodes. Nhưng mỗi lần đi qua path dài, compression làm structure phẳng hơn. Ta không thể liên tục trả cost lớn trên cùng các nodes mà không thay đổi future shape.

Đây là cùng family reasoning với dynamic array resize: một operation đắt được “trả” bởi việc làm nhiều operation tương lai rẻ hơn.

## DSU trong Kruskal MST

Kruskal sort edges theo weight rồi xét từng edge `(u,v)`.

Nếu:

```text
find(u) != find(v)
```

edge nối hai components khác nhau nên không tạo cycle; ta nhận edge và `union(u,v)`.

Nếu representatives giống nhau, edge đóng cycle và bỏ qua.

DSU ở đây không tìm cycle bằng traversal. Nó chỉ trả lời “hai endpoints đã connected bởi các edges trước chưa?”.

## Cycle detection khi add undirected edges

Trong graph ban đầu rỗng, process edges online:

```text
for edge (u,v):
    if find(u) == find(v):
        adding edge creates a cycle
    else:
        union(u,v)
```

Lưu ý đây là reasoning cho **undirected** connectivity. Directed cycle detection không thể dùng DSU theo cách này vì directed reachability không phải equivalence relation đơn giản.

## Connected components dưới merge-only updates

Nếu vertices ban đầu tách rời và edges chỉ được thêm, DSU là structure rất tự nhiên.

Maintain thêm:

```text
componentCount = n
```

mỗi successful union:

```text
componentCount--
```

Ta có thể query số components `O(1)`.

## Component metadata

Root có thể lưu metadata của toàn component:

```text
size
sum
minimum id
maximum value
aggregate statistics
```

Khi merge two roots, combine metadata.

Ví dụ:

```java
size[ra] += size[rb];
sum[ra] += sum[rb];
```

Nguyên tắc là metadata phải thuộc representative hiện tại; không nên đọc `size[x]` cho non-root nếu implementation không giữ nó cập nhật.

## Offline threshold queries

Một pattern cực mạnh là sort events theo threshold.

Ví dụ: có roads `(u,v,w)` và queries:

> Với chỉ roads có cost `<= X`, `a` và `b` có connected không?

Ta sort roads theo `w`, sort queries theo `X`, rồi tăng dần threshold:

```text
while nextRoad.weight <= query.X:
    union(nextRoad.u, nextRoad.v)

answer = find(a) == find(b)
```

Mỗi edge chỉ được add một lần. Đây là ví dụ của **offline algorithm**: biết trước toàn bộ queries cho phép reorder processing để dùng DSU hiệu quả.

## Kruskal Reconstruction Tree

Một extension thú vị: mỗi successful union có thể tạo một internal node mới đại diện thời điểm/weight mà hai components hợp nhất. Leaves là original vertices; internal node weight là edge threshold.

Sau khi build, các query như “minimum threshold để u và v connected” có thể biến thành LCA trên reconstruction tree.

Insight này cho thấy DSU không chỉ là endpoint algorithm; nó còn có thể xây một hierarchy từ merge history.

## DSU với parity / bipartite constraints

Ta có thể lưu thêm relation từ node tới parent. Ví dụ `parity[x]` biểu diễn màu của `x` XOR màu parent.

Khi `find(x)` compress path, phải compose parity dọc path.

Structure này có thể support constraints kiểu:

```text
u và v phải khác màu
```

và detect contradiction khi thêm edges trong online bipartiteness variants.

General principle: DSU có thể duy trì **relative potential** giữa node và representative nếu relation compose được.

## Weighted / Potential DSU

Một biến thể lưu:

\[
potential[x] = value(x) - value(parent(x))
\]

hoặc một group-like relation tương tự. Khi union hai components với constraint giữa `a` và `b`, ta tính potential của root mới sao cho relation vẫn đúng.

Ứng dụng gồm difference constraints đơn giản, coordinate relation và parity.

Đây là bước nâng cao: path compression không chỉ đổi parent; mọi metadata relative-to-parent phải được cập nhật tương ứng.

## Tại sao standard DSU không hỗ trợ delete/split tốt?

DSU được tối ưu cho **monotonic merge**. Sau path compression, nhiều nodes có thể trỏ thẳng tới root; original tree structure gần như bị mất.

Nếu xóa một edge đã từng làm components merge, DSU không biết component phải split thành những phần nào vì nó chưa bao giờ lưu đủ graph topology.

Đây không phải thiếu feature nhỏ; đó là consequence trực tiếp của information compression.

> DSU nhanh vì nó quên path structure. Muốn support deletion, bạn cần giữ thêm thông tin hoặc đổi algorithm.

## Rollback DSU

Nếu cần undo unions trong offline algorithm, standard path compression gây khó vì một `find` có thể mutate nhiều parents.

**Rollback DSU (롤백 DSU)** thường:

- dùng union-by-size;
- không path-compress;
- mỗi union ghi thay đổi vào stack;
- rollback pop stack để restore parent/size.

Union/find khi đó thường `O(log n)` worst-case do union-by-size height bound, nhưng undo trở nên đơn giản.

### Change stack idea

```text
union(ra, rb):
    record (rb, oldParent, ra, oldSizeRa)
    parent[rb] = ra
    size[ra] += size[rb]

rollback():
    restore recorded values
```

Optimization không tồn tại trong chân không: path compression tốt cho forward queries nhưng xung đột với reversibility.

## Dynamic connectivity offline

Nếu edges có cả add và remove theo time, có thể xử lý offline bằng segment tree over time + rollback DSU.

Mỗi edge tồn tại trên một interval thời gian `[l,r)`. Ta add edge vào các segment-tree nodes phủ interval đó. DFS segment tree:

```text
enter node -> apply unions
process children / answer queries
exit node -> rollback
```

Mỗi query sees đúng tập edges active tại timestamp của nó.

Đây là một example nâng cao của việc combine data structures: segment tree quản time intervals, rollback DSU quản connectivity state.

## Persistent / Partially Persistent DSU

Một hướng khác là giữ history để query connectivity ở version cũ. Có nhiều designs: union tree với timestamps, persistent arrays, or versioned parent relations. Không phải mọi variant support arbitrary branching updates; cần xác định persistence model.

Điểm conceptual là DSU có thể được mở rộng theo trục **time**, nhưng standard implementation chỉ đại diện state hiện tại.

## Small-to-large merging khác DSU thế nào?

Một technique khác cũng gọi “merge smaller into larger” là small-to-large merging của sets/maps trên tree. Ví dụ merge color-frequency maps của children vào largest map.

Nó dùng cùng doubling argument để bound element moves `O(log n)`, nhưng không phải DSU. DSU duy trì partition identity; small-to-large có thể duy trì rich collections.

Cùng proof pattern không đồng nghĩa cùng data structure.

## Java implementation đầy đủ cơ bản

```java
final class DSU {
    private final int[] parent;
    private final int[] size;
    private int components;

    DSU(int n) {
        parent = new int[n];
        size = new int[n];
        components = n;

        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    int find(int x) {
        int root = x;
        while (parent[root] != root) {
            root = parent[root];
        }

        while (parent[x] != x) {
            int p = parent[x];
            parent[x] = root;
            x = p;
        }
        return root;
    }

    boolean union(int a, int b) {
        int ra = find(a);
        int rb = find(b);
        if (ra == rb) return false;

        if (size[ra] < size[rb]) {
            int t = ra;
            ra = rb;
            rb = t;
        }

        parent[rb] = ra;
        size[ra] += size[rb];
        components--;
        return true;
    }

    boolean connected(int a, int b) {
        return find(a) == find(b);
    }

    int componentSize(int x) {
        return size[find(x)];
    }

    int componentCount() {
        return components;
    }
}
```

## JavaScript implementation

```js
class DSU {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.size = Array(n).fill(1);
    this.components = n;
  }

  find(x) {
    let root = x;
    while (this.parent[root] !== root) {
      root = this.parent[root];
    }

    while (this.parent[x] !== x) {
      const p = this.parent[x];
      this.parent[x] = root;
      x = p;
    }
    return root;
  }

  union(a, b) {
    let ra = this.find(a);
    let rb = this.find(b);
    if (ra === rb) return false;

    if (this.size[ra] < this.size[rb]) [ra, rb] = [rb, ra];

    this.parent[rb] = ra;
    this.size[ra] += this.size[rb];
    this.components--;
    return true;
  }
}
```

## Common misconceptions

**“Representative là smallest element.”** Không trừ khi bạn chủ động giữ rule đó. Root chỉ là implementation identity.

**“DSU cho biết đường đi giữa hai vertices.”** Không. Nó chỉ biết cùng component hay không.

**“DSU dùng được cho directed reachability.”** Không theo standard formulation; directed connectivity không phải equivalence relation đơn giản.

**“Path compression luôn nên bật.”** Không nếu cần rollback/undo hoặc một persistence design cụ thể.

**“`size[x]` luôn là component size.”** Thường chỉ đúng ở root. Hãy dùng `size[find(x)]`.

**“Gần O(1) nghĩa là worst-case O(1).”** Không. Bound chuẩn là amortized `O(alpha(n))` với hai optimizations.

## Testing DSU

Một test tốt nên tạo random union/query sequence và compare với reference graph connectivity trên `n` nhỏ.

Invariants nên kiểm:

```text
parent[root] == root
size[root] bằng số elements thực trong component
find(x) idempotent: find(find(x)) == find(x)
components giảm đúng một khi union successful
connected là equivalence relation
```

Equivalence relation nghĩa là reflexive, symmetric và transitive. Đây cũng là lý do DSU hợp với partition problems.

## Connection với equivalence classes

Nếu relation “cùng nhóm” thực sự là equivalence relation, DSU là representation tự nhiên:

```text
x ~ x                     reflexive
x ~ y => y ~ x            symmetric
x ~ y và y ~ z => x ~ z   transitive
```

Connected components của undirected graph, account merging theo shared identity, synonym groups, clustering dưới merge rules đều có thể được nhìn như equivalence classes.

## Mental Model mở rộng

> DSU là một structure tối ưu cho **monotonic equivalence merging**. Nó đổi path/topology detail lấy component identity cực rẻ.

Khi gặp bài toán connectivity, hãy hỏi: edges chỉ được thêm hay còn bị xóa? Query cần path hay chỉ yes/no cùng component? Có threshold offline không? Có metadata per component không? Có cần rollback không?

Nếu câu trả lời là “chỉ merge và hỏi cùng nhóm”, DSU thường là abstraction đúng hơn BFS/DFS lặp lại.