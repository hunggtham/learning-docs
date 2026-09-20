# Minimum Spanning Tree
**Cây khung nhỏ nhất (MST / 최소 신장 트리)**

MST không phải shortest path. Shortest path tối ưu route từ source; MST tối ưu tổng cost để kết nối toàn bộ vertices.

Một spanning tree của connected undirected graph chứa mọi vertex, không cycle và có `V-1` edges. MST là spanning tree có tổng weight nhỏ nhất.

## Kruskal

Sort edges tăng theo weight, thêm edge nếu nó không tạo cycle. Union-Find trả lời nhanh hai endpoints đã connected chưa.

```text
sort edges
for (u,v,w):
    if find(u) != find(v):
        union(u,v)
        take edge
```

Cost bị chi phối bởi sort: `O(E log E)`.

## Prim

Prim bắt đầu từ một node, luôn chọn edge rẻ nhất nối tree hiện tại với node bên ngoài. Priority queue quản lý frontier. Với adjacency list + heap: `O(E log V)`.

## Cut property

Nếu chia vertices thành hai nhóm, một edge nhẹ nhất crossing cut là safe cho một MST. Đây là nền tảng proof cho Kruskal/Prim.

## Mental Model

> MST tối ưu infrastructure toàn cục, không tối ưu từng route. Một path trong MST có thể dài hơn shortest path của graph gốc.

## Cycle property

Một property bổ sung cho cut property: trong một cycle, nếu một edge nặng hơn hẳn các edge khác, edge đó không cần thuộc MST. Nếu thêm edge đó vào một spanning tree tạo cycle, ta có thể bỏ edge nặng nhất để không tăng hoặc giảm total cost.

Cut và cycle properties cung cấp hai hướng reasoning đối xứng: edge nào safe để thêm và edge nào safe để loại.

## Kruskal với DSU — Java

```java
record Edge(int u, int v, int w) {}

edges.sort(Comparator.comparingInt(Edge::w));
DSU dsu = new DSU(n);
long total = 0;
int used = 0;

for (Edge e : edges) {
    if (dsu.union(e.u(), e.v())) {
        total += e.w();
        used++;
        if (used == n - 1) break;
    }
}
```

Nếu `used != n-1`, graph disconnected và không có spanning tree cho toàn graph; kết quả là minimum spanning forest nếu tiếp tục theo components.

## Prim và frontier invariant

Prim giữ một tree `S`. Priority queue chứa candidate edges crossing từ `S` ra ngoài. Mỗi bước chọn cheapest valid crossing edge. Cut property chứng minh edge đó safe.

Lazy Prim có thể giữ stale edges tới nodes đã vào tree; khi pop thì skip. Pattern giống Dijkstra stale-entry handling.

## Unique MST

Nếu mọi edge weights khác nhau, MST là unique. Nếu ties tồn tại, có thể có nhiều MST cùng total weight. Algorithm có thể trả một trong số đó; correctness không yêu cầu cùng tree cụ thể.

## MST không bảo toàn shortest paths

MST tối thiểu tổng infrastructure cost. Một path giữa hai vertices trong MST có thể dài hơn đáng kể shortest route của graph gốc. Network backbone design và route optimization là hai objectives khác nhau.
