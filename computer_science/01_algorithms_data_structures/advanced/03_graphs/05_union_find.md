# Union-Find / Disjoint Set Union
**Tập hợp rời nhau (DSU / 서로소 집합)**

Union-Find tối ưu hai operation: `find(x)` xác định component representative và `union(a,b)` hợp nhất hai components.

Mỗi set được biểu diễn như một parent tree. Root là representative.

## Path compression

Sau `find(x)`, cho các nodes trên path trỏ gần trực tiếp tới root. Tree dần phẳng.

## Union by size/rank

Khi merge, gắn tree nhỏ hơn dưới tree lớn hơn để hạn chế height.

```java
class DSU {
    int[] parent, size;

    DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) { parent[i] = i; size[i] = 1; }
    }

    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    boolean union(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return false;
        if (size[ra] < size[rb]) { int t = ra; ra = rb; rb = t; }
        parent[rb] = ra;
        size[ra] += size[rb];
        return true;
    }
}
```

Kết hợp hai optimization cho amortized complexity gần constant: `O(alpha(n))`, với inverse Ackermann tăng cực chậm.

## Use cases và limitation

Kruskal MST, offline connectivity, equivalence classes, detect cycle khi thêm undirected edges. DSU rất mạnh với merge nhưng không hỗ trợ split/delete component dễ dàng.

## Mental Model

> DSU không lưu toàn bộ đường đi; nó chỉ lưu đủ để trả lời “hai phần tử có cùng component identity không?”.

## Vì sao path compression + union-by-size gần O(1)?

Nếu chỉ path compression hoặc chỉ union-by-size, tree đã khá nông. Kết hợp hai kỹ thuật tạo bound inverse Ackermann `alpha(n)`, nhỏ hơn 5 cho mọi input size thực tế tưởng tượng được.

Điều đáng nhớ không phải function Ackermann. Mental model là: **mỗi find làm cấu trúc tương lai phẳng hơn, còn union tránh tạo cây cao ngay từ đầu**.

## C implementation

```c
typedef struct {
    int *parent;
    int *size;
    int n;
} DSU;

int dsu_find(DSU *d, int x) {
    int root = x;
    while (d->parent[root] != root)
        root = d->parent[root];

    while (d->parent[x] != x) {
        int p = d->parent[x];
        d->parent[x] = root;
        x = p;
    }
    return root;
}
```

Iterative version tránh recursion depth và thực hiện compression ở pass thứ hai.

## Offline connectivity

Nếu edges được thêm dần và có queries “u,v connected chưa?”, DSU cực phù hợp. Nếu queries theo threshold weight, có thể sort edges và queries theo threshold rồi union dần — một pattern offline mạnh.

Ví dụ hỏi “hai thành phố connected nếu chỉ dùng roads cost <= X?”: sort roads theo cost, sort queries theo X, add roads tới threshold rồi query DSU.

## Rollback DSU

Standard path compression làm rollback khó vì sửa nhiều parents. Nếu cần divide-and-conquer over time với edge additions/removals offline, có thể dùng DSU rollback: union-by-size nhưng không path-compress, ghi change stack để undo.

Điều này minh họa trade-off: optimization tốt cho một operation có thể cản một capability khác.
