# cây khung nhỏ nhất

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **cây khung nhỏ nhất**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Tại sao lời giải tối ưu phải là cây?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. MST khác đường đi ngắn nhất cây** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối MST với cut, cycle và connectivity, để tối ưu kết nối khác với tối ưu đường đi.

**Cây khung nhỏ nhất / cây khung nhỏ nhất (MST) / 최소 신장 트리**

cây khung nhỏ nhất giải bài toán: **kết nối toàn bộ các đỉnh của một undirected đồ thị có trọng số với tổng cạnh chi phí nhỏ nhất**. Nó không tối ưu đường đi giữa từng cặp các nút như đường đi ngắn nhất (shortest path); nó tối ưu **tổng chi phí của toàn bộ hạ tầng kết nối**.

Nếu đồ thị có `V` các đỉnh và connected, một spanning cây có đúng `V-1` các cạnh. MST chọn spanning cây rẻ nhất trong tất cả các spanning các cây khả dĩ.

## 1. Tại sao lời giải tối ưu phải là cây?

Nếu một connected subgraph chứa chu trình, bỏ một cạnh trên chu trình vẫn giữ connected. Vì vậy khi mục tiêu chỉ là connectivity và ta không cần redundancy, chu trình là dư thừa về số cạnh.

Mọi connected acyclic đồ thị có `V-1` các cạnh. Do đó không gian tìm kiếm tự nhiên của bài toán là tập tất cả spanning các cây.

Nhưng cần nhớ: hệ thống thực tế mạng thường cần redundancy. MST cố tình bỏ redundancy để tối thiểu hóa total chi phí; nó không tối ưu fault tolerance.

> **Chuyển mạch:** Trong **cây khung nhỏ nhất**, **2. MST khác đường đi ngắn nhất cây** tiếp nhận điểm tựa từ **1. Tại sao lời giải tối ưu phải là cây?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Cut tính chất — engine chứng minh của MST** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. MST khác đường đi ngắn nhất cây

Giả sử:

```text
A-B = 2
B-C = 2
A-C = 3
```

MST chọn `A-B` và `B-C`, total 4. Nhưng đường đi ngắn nhất từ A tới C trong đồ thị gốc là cạnh trực tiếp chi phí 3.

MST hỏi:

> “Bộ các cạnh rẻ nhất để mọi đỉnh connected là gì?”

cây đường đi ngắn nhất hỏi:

> “Từ một nguồn, làm sao khoảng cách tới từng đỉnh là nhỏ nhất?”

Hai mục tiêu (objective / 목표) khác nhau nên không thể thay thế thuật toán cho nhau.

> **Chuyển mạch:** Ở chặng này của **cây khung nhỏ nhất**, **3. Cut tính chất — engine chứng minh của MST** tiếp nhận điểm tựa từ **2. MST khác đường đi ngắn nhất cây** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. chu trình tính chất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Cut tính chất — engine chứng minh của MST

Một **cut** chia các đỉnh thành hai tập `S` và `V-S`. cạnh có hai endpoint nằm khác phía gọi là crossing cạnh.

Cut tính chất ở dạng thực dụng:

> Với một cut tôn trọng các cạnh đã chọn, một cạnh nhẹ nhất crossing cut là **an toàn**: tồn tại một MST chứa nó.

trực giác chứng minh dùng exchange argument. Giả sử MST `T` không chứa light cạnh `e`. Thêm `e` vào `T` tạo chu trình. chu trình phải chứa một crossing cạnh `f` khác. Vì `w(e) <= w(f)`, thay `f` bằng `e` không tăng total chi phí. Ta thu được MST khác chứa `e`.

Kruskal và Prim chỉ là hai cách khác nhau để liên tục tìm an toàn cạnh bằng cut tính chất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **cây khung nhỏ nhất**, **4. chu trình tính chất** tiếp nhận điểm tựa từ **3. Cut tính chất — engine chứng minh của MST** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Kruskal: grow một forest** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. chu trình tính chất

Trong một chu trình, nếu cạnh `e` nặng hơn nghiêm ngặt mọi cạnh khác trên chu trình, `e` không thể nằm trong bất kỳ MST nào.

Nếu một MST chứa `e`, thêm một cạnh nhẹ hơn khác của chu trình tạo chu trình rồi bỏ `e`, total giảm — mâu thuẫn tối ưu.

Cut tính chất giúp **thêm** cạnh. chu trình tính chất giúp **loại** cạnh.

> **Chuyển mạch:** Trong **cây khung nhỏ nhất**, **5. Kruskal: grow một forest** tiếp nhận điểm tựa từ **4. chu trình tính chất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Minimum Spanning Forest** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Kruskal: grow một forest

Kruskal sort các cạnh tăng dần theo trọng số. Mỗi lần gặp cạnh `(u,v)`, nếu `u` và `v` ở hai các thành phần khác nhau, ta chọn cạnh và merge các thành phần.

```text
sort edges by weight
for edge in sorted order:
    if find(u) != find(v):
        choose edge
        union(u,v)
```

DSU trả lời connectivity nhanh; chứng minh optimality vẫn đến từ cut tính chất.

### Java sketch

Trước khi đọc đoạn triển khai, hãy giữ invariant và complexity mà thuật toán phải bảo toàn. Code bên dưới là một cách hiện thực hóa; cần đối chiếu output, ownership và edge case với mô hình vừa học.

```java
record Edge(int u, int v, long w) {}

edges.sort(Comparator.comparingLong(Edge::w));
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

Độ phức tạp (complexity / 복잡도):

\[
O(E\log E)+O(E\alpha(V))=O(E\log E)
\]

Sorting thường chi phối.

> **Chuyển mạch:** Ở chặng này của **cây khung nhỏ nhất**, **6. Minimum Spanning Forest** tiếp nhận điểm tựa từ **5. Kruskal: grow một forest** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Prim: grow một cây qua frontier** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Minimum Spanning Forest

Nếu đồ thị disconnected, không có spanning cây toàn đồ thị. Kruskal vẫn tạo MST riêng cho từng thành phần liên thông, gọi là **minimum spanning forest**.

API cần phân biệt:

```text
result is forest
vs
input required connected graph but was not connected
```

`used == V-1` là điều kiện sau cho connected đồ thị.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **cây khung nhỏ nhất**, **7. Prim: grow một cây qua frontier** tiếp nhận điểm tựa từ **6. Minimum Spanning Forest** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Prim và Dijkstra giống mã (code / 코드) nhưng khác bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Prim: grow một cây qua frontier

Prim giữ set `S` các đỉnh đã vào MST. Mỗi bước chọn cạnh nhẹ nhất crossing từ `S` ra ngoài.

Đây chính là cut `(S, V-S)`, nên lightest crossing cạnh an toàn.

### Lazy Prim

Push outgoing các cạnh vào vùng nhớ động (heap / 힙). Khi pop nếu endpoint ngoài đã đã thăm thì dùng, nếu stale thì skip.

```text
visit start
push outgoing edges
while heap not empty:
    pop cheapest edge
    if destination already in tree: continue
    choose edge
    visit destination
    push its outgoing edges
```

đơn giản, dễ implement, chấp nhận các phần tử trùng/stale các mục.

### Eager Prim

Giữ `key[v]` = cheapest cạnh hiện biết nối `v` vào cây. Khi thấy cạnh nhẹ hơn, cập nhật khóa/nút cha. Indexed vùng nhớ động (heap / 힙)/decrease-key cho cách triển khai gọn về trạng thái (state / 상태), nhưng tiêu chuẩn (standard / 표준) hàng đợi ưu tiên không hỗ trợ decrease-key trực tiếp nên có thể dùng lazy các phần tử trùng.

> **Chuyển mạch:** Trong **cây khung nhỏ nhất**, **8. Prim và Dijkstra giống mã (code / 코드) nhưng khác bất biến (invariant / 불변식)** tiếp nhận điểm tựa từ **7. Prim: grow một cây qua frontier** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Chọn Kruskal hay Prim theo cách biểu diễn (representation / 표현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Prim và Dijkstra giống mã (code / 코드) nhưng khác bất biến (invariant / 불변식)

Dijkstra độ ưu tiên:

```text
best path distance từ source tới v
```

Prim độ ưu tiên:

```text
cheapest single edge nối v vào current tree
```

Dijkstra relax:

\[
dist[u]+w(u,v)
\]

Prim chỉ so sánh:

\[
w(u,v)
\]

Nếu bản sao (copy / 복사) mã (code / 코드) mà không hiểu khóa ngữ nghĩa (semantics / 의미론), bug rất dễ xuất hiện.

> **Chuyển mạch:** Ở chặng này của **cây khung nhỏ nhất**, **9. Chọn Kruskal hay Prim theo cách biểu diễn (representation / 표현)** tiếp nhận điểm tựa từ **8. Prim và Dijkstra giống mã (code / 코드) nhưng khác bất biến (invariant / 불변식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Negative các trọng số không gây vấn đề như đường đi ngắn nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Chọn Kruskal hay Prim theo cách biểu diễn (representation / 표현)

Kruskal tự nhiên khi:

```text
đã có edge list
sparse graph
cần sort/scan edges toàn cục
```

Prim tự nhiên khi:

```text
đã có adjacency list/matrix
muốn grow từ vertex
```

đồ thị dày có thể dùng Prim `O(V²)` với ma trận kề mà không cần vùng nhớ động (heap / 힙); vùng nhớ động (heap / 힙) overhead không phải lúc nào cũng thắng.

thuật toán selection phải xét đồ thị density và cách biểu diễn, không chỉ một dòng Big-O.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **cây khung nhỏ nhất**, **10. Negative các trọng số không gây vấn đề như đường đi ngắn nhất** tiếp nhận điểm tựa từ **9. Chọn Kruskal hay Prim theo cách biểu diễn (representation / 표현)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Unique MST và ties** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Negative các trọng số không gây vấn đề như đường đi ngắn nhất

MST cây không có chu trình. Negative cạnh chỉ đơn giản là cạnh rất hấp dẫn về chi phí và sẽ được chọn nếu không phá cây điều kiện.

Không có khái niệm negative chu trình làm mục tiêu (objective / 목표) xuống vô hạn vì spanning cây luôn có đúng `V-1` các cạnh.

> **Chuyển mạch:** Trong **cây khung nhỏ nhất**, **11. Unique MST và ties** tiếp nhận điểm tựa từ **10. Negative các trọng số không gây vấn đề như đường đi ngắn nhất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. cạnh bắt buộc: unique light cạnh của một cut** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Unique MST và ties

Nếu mọi cạnh các trọng số distinct, MST unique.

Nếu có ties, nhiều MST khác nhau có thể cùng total trọng số. kiểm thử (test / 테스트) không nên bắt chính xác danh sách cạnh trừ khi quy tắc phân xử khi bằng nhau được cố ý cố định.

Một cạnh là **trọng yếu (critical / 중요)** nếu xuất hiện trong mọi MST; **optional/pseudo-critical** nếu có thể xuất hiện trong một số MST; và **never-MST** nếu không thể xuất hiện.

Cut/chu trình các tính chất là nền cho classification này.

> **Chuyển mạch:** Ở chặng này của **cây khung nhỏ nhất**, **12. cạnh bắt buộc: unique light cạnh của một cut** tiếp nhận điểm tựa từ **11. Unique MST và ties** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. cạnh bị cấm: unique heaviest trên chu trình** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. cạnh bắt buộc: unique light cạnh của một cut

Nếu cạnh `e` là **unique** lightest cạnh crossing một cut, mọi MST phải chứa `e`.

Lý do: nếu MST không chứa `e`, exchange bằng `e` giảm chi phí nghiêm ngặt.

Đây là chứng minh mạnh hơn “an toàn”: an toàn nói có một MST chứa cạnh; unique-light nói mọi MST chứa cạnh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **cây khung nhỏ nhất**, **13. cạnh bị cấm: unique heaviest trên chu trình** tiếp nhận điểm tựa từ **12. cạnh bắt buộc: unique light cạnh của một cut** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Bottleneck view** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. cạnh bị cấm: unique heaviest trên chu trình

Nếu `e` là unique heaviest trên một chu trình, không MST nào chứa `e`. Nếu chứa, thay nó bằng cạnh nhẹ hơn trên chu trình làm total giảm.

Hai criteria này rất hữu ích trong sensitivity phân tích (analysis / 분석).

> **Chuyển mạch:** Trong **cây khung nhỏ nhất**, **14. Bottleneck view** tiếp nhận điểm tựa từ **13. cạnh bị cấm: unique heaviest trên chu trình** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Maximum Spanning cây** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Bottleneck view

MST cũng là một **minimum bottleneck spanning cây**: trọng số lớn nhất trong cây là nhỏ nhất có thể theo bottleneck mục tiêu (objective / 목표) thích hợp.

Kruskal cho intuition rõ. Khi tăng threshold `T` và cho phép tất cả các cạnh có trọng số `<=T`, threshold nhỏ nhất làm đồ thị connected chính là bottleneck phương án tối ưu.

Liên kết (connection / 연결) này biến nhiều bài threshold-connectivity thành Kruskal/DSU problems.

> **Chuyển mạch:** Ở chặng này của **cây khung nhỏ nhất**, **15. Maximum Spanning cây** tiếp nhận điểm tựa từ **14. Bottleneck view** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Single-Linkage Clustering** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Maximum Spanning cây

Nếu mục tiêu chuyển thành tối đa hóa tổng trọng số, Kruskal có thể sắp xếp giảm dần hoặc đảo bộ so sánh. Lập luận dựa trên lát cắt và chu trình được áp dụng theo chiều ngược lại.

Ứng dụng có thể là maximize affinity/độ tin cậy (reliability / 신뢰성) score trong một formulation phù hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **cây khung nhỏ nhất**, **16. Single-Linkage Clustering** tiếp nhận điểm tựa từ **15. Maximum Spanning cây** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Euclidean MST và không materialize đồ thị đầy đủ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Single-Linkage Clustering

Xây MST trên points theo khoảng cách, rồi remove `k-1` các cạnh lớn nhất. Ta được `k` connected clusters.

MST giữ các liên kết rẻ nhất cần cho connectivity; các cạnh lớn trong MST thường đại diện gaps giữa groups.

Đây là liên kết (connection / 연결) giữa đồ thị lý thuyết (theory / 이론) và hierarchical clustering.

> **Chuyển mạch:** Trong **cây khung nhỏ nhất**, **17. Euclidean MST và không materialize đồ thị đầy đủ** tiếp nhận điểm tựa từ **16. Single-Linkage Clustering** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Second-Best MST** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Euclidean MST và không materialize đồ thị đầy đủ

Với `n` points, complete geometric đồ thị có `Θ(n²)` các cạnh. Chạy Kruskal trên tất cả các cạnh có thể quá lớn.

Trong plane, Euclidean MST là subgraph của Delaunay triangulation, nên cấu trúc hình học có thể giảm ứng viên các cạnh trước khi chạy MST.

Bài học rộng hơn:

> Đôi khi độ phức tạp (complexity / 복잡도) bottleneck là **xây đồ thị**, không phải thuật toán đồ thị sau đó.

> **Chuyển mạch:** Ở chặng này của **cây khung nhỏ nhất**, **18. Second-Best MST** tiếp nhận điểm tựa từ **17. Euclidean MST và không materialize đồ thị đầy đủ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Replacement cạnh và sensitivity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Second-Best MST

Lấy MST `T`. Mỗi non-tree cạnh `(u,v,w)` khi thêm vào `T` tạo đúng một chu trình. Để trở lại cây, phải bỏ một cạnh trên đường đi `u-v` trong `T`.

ứng viên tốt nhất cho cạnh mới thường bỏ cạnh lớn nhất trên đường đi:

\[
newCost = mstCost + w - maxEdgeOnPath(u,v)
\]

Nếu preprocess nhảy nhị phân/LCA để truy vấn max cạnh đường đi `O(log V)`, có thể xét mọi non-tree cạnh hiệu quả.

Đây là liên kết (connection / 연결) giữa MST và cây đường đi các truy vấn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **cây khung nhỏ nhất**, **19. Replacement cạnh và sensitivity** tiếp nhận điểm tựa từ **18. Second-Best MST** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. động MST khó vì cục bộ cập nhật có tác động (effect / 효과) toàn cục** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Replacement cạnh và sensitivity

Nếu một MST cạnh bị xóa hoặc tăng trọng số, thành phần cây bị split thành hai phía. cạnh ngoài MST rẻ nhất crossing cut đó là replacement ứng viên.

Nếu nhiều các cập nhật xảy ra, recompute từ đầu có thể đắt; động MST structures quản lý replacement các cạnh phức tạp hơn.

tĩnh sensitivity phân tích (analysis / 분석) vẫn có thể dùng cut/chu trình + tiền xử lý để trả lời “nếu cạnh này đổi chi phí thì MST thay đổi thế nào?”.

> **Chuyển mạch:** Trong **cây khung nhỏ nhất**, **20. động MST khó vì cục bộ cập nhật có tác động (effect / 효과) toàn cục** tiếp nhận điểm tựa từ **19. Replacement cạnh và sensitivity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Reverse-Delete thuật toán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. động MST khó vì cục bộ cập nhật có tác động (effect / 효과) toàn cục

Một cạnh insertion có thể tạo chu trình với đường đi trong MST. Nếu cạnh mới nhẹ hơn maximum cạnh trên đường đi, ta swap chúng.

Một tree-edge deletion tạo cut và cần tìm cheapest non-tree cạnh nối lại hai thành phần.

Hai primitives:

```text
max edge on tree path
minimum replacement edge crossing cut
```

là trung tâm của động MST, dẫn tới động các cây như Link-Cut cây trong advanced settings.

> **Chuyển mạch:** Ở chặng này của **cây khung nhỏ nhất**, **21. Reverse-Delete thuật toán** tiếp nhận điểm tựa từ **20. động MST khó vì cục bộ cập nhật có tác động (effect / 효과) toàn cục** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. MST và Matroid intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Reverse-Delete thuật toán

Một cách nhìn đối xứng với Kruskal:

1. sort các cạnh giảm dần;
2. thử delete cạnh;
3. nếu đồ thị vẫn connected, giữ cạnh bị xóa;
4. nếu disconnect, phục hồi.

chu trình tính chất giải thích tính đúng đắn. Cách đơn giản kiểm tra liên thông làm cách triển khai chậm, nhưng thuật toán rất hữu ích về mặt conceptual: Kruskal “thêm an toàn các cạnh”, reverse-delete “xóa unnecessary heavy các cạnh”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **cây khung nhỏ nhất**, **22. MST và Matroid intuition** tiếp nhận điểm tựa từ **21. Reverse-Delete thuật toán** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. đồ thị có hướng là bài toán (problem / 문제) khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. MST và Matroid intuition

Spanning forests của đồ thị tạo một cấu trúc gọi là **graphic matroid**. Greedy chọn các cạnh theo trọng số hoạt động vì independent sets của matroid có exchange tính chất mạnh.

Không cần học matroid lý thuyết (theory / 이론) để mã (code / 코드) Kruskal, nhưng nó giải thích vì sao greedy “sort rồi lấy nếu không tạo chu trình” đúng ở đây trong khi nhiều bài khác greedy tương tự lại sai.

Greedy tính đúng đắn không đến từ sorting; nó đến từ cấu trúc (structure / 구조) của feasible sets.

> **Chuyển mạch:** Trong **cây khung nhỏ nhất**, **23. đồ thị có hướng là bài toán (problem / 문제) khác** tiếp nhận điểm tựa từ **22. MST và Matroid intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Multigraph và các cạnh song song** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. đồ thị có hướng là bài toán (problem / 문제) khác

Chuẩn MST áp dụng đồ thị vô hướng (undirected graph). Directed analogue là **cây phân nhánh có hướng nhỏ nhất** rooted tại một đỉnh, giải bằng Chu–Liu/Edmonds-type các thuật toán.

Không thể chỉ chạy Kruskal trên directed các cạnh rồi bỏ orientation.

> **Chuyển mạch:** Ở chặng này của **cây khung nhỏ nhất**, **24. Multigraph và các cạnh song song** tiếp nhận điểm tựa từ **23. đồ thị có hướng là bài toán (problem / 문제) khác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. tràn số và comparator tính đúng đắn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Multigraph và các cạnh song song

Kruskal xử lý các cạnh song song tự nhiên; cạnh rẻ hơn giữa cùng endpoints thường được xét trước. Self-loop luôn tạo chu trình với chính đỉnh và không thể giúp connect thành phần khác, nên bị bỏ.

cách triển khai nên giữ cạnh IDs nếu cần đầu ra chính xác cạnh định danh (identity / 식별자).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **cây khung nhỏ nhất**, **25. tràn số và comparator tính đúng đắn** tiếp nhận điểm tựa từ **24. Multigraph và các cạnh song song** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. xác minh (verification / 확인) của MST kết quả** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. tràn số và comparator tính đúng đắn

Total trọng số có thể vượt `int`. Dùng `long`/64-bit khi các ràng buộc yêu cầu.

Comparator không nên:

```java
return a.w - b.w;
```

nếu tràn số có thể xảy ra. Dùng `Long.compare`/`Comparator.comparingLong`.

C cũng nên tránh subtraction comparator với signed tràn số.

> **Chuyển mạch:** Trong **cây khung nhỏ nhất**, **26. xác minh (verification / 확인) của MST kết quả** tiếp nhận điểm tựa từ **25. tràn số và comparator tính đúng đắn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Differential kiểm thử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. xác minh (verification / 확인) của MST kết quả

Một đầu ra MST cần:

```text
V-1 edges
connected
acyclic
tổng weight đúng
```

Nhưng ba structural các tính chất đầu chỉ chứng minh spanning cây, chưa chứng minh minimum.

Để verify optimality, có tính chất mạnh:

> Với mọi non-tree cạnh `(u,v,w)`, maximum cạnh trọng số trên đường đi `u-v` trong MST không được lớn hơn `w`.

Nếu có cây cạnh trên đường đi nặng hơn `w`, swap sẽ tạo spanning cây nhẹ hơn.

tính chất này cho phép bộ xác minh độc lập mạnh hơn chỉ so đầu ra cấu trúc (structure / 구조).

> **Chuyển mạch:** Ở chặng này của **cây khung nhỏ nhất**, **27. Differential kiểm thử** tiếp nhận điểm tựa từ **26. xác minh (verification / 확인) của MST kết quả** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. MST trong cơ sở dữ liệu/mạng/hệ thống thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Differential kiểm thử

Trên ngẫu nhiên đồ thị nhỏ:

- chạy Kruskal;
- chạy Prim;
- so total chi phí;
- với đồ thị rất nhỏ, brute-force enumerate spanning các cây làm oracle.

các trường hợp kiểm thử nên có:

```text
1 vertex
2 vertices
path
cycle
complete graph nhỏ
negative weights
equal weights
parallel edges
disconnected graph
very large weights
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **cây khung nhỏ nhất**, **27. Differential kiểm thử** nêu điều cần giải thích; **28. MST trong cơ sở dữ liệu/mạng/hệ thống thiết kế (design / 설계)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. MST trong cơ sở dữ liệu/mạng/hệ thống thiết kế (design / 설계)

MST có thể mô hình:

```text
minimum cable/road/fiber cost
minimum set of pairwise links để bootstrap connectivity
clustering backbone
minimum connection graph trong layout/design
```

Nhưng thực tế thường thêm các ràng buộc:

```text
capacity
redundancy
hop count
latency
geography
fault domains
```

Khi đó bài toán (problem / 문제) có thể không còn là pure MST. DSA mô hình phải khớp yêu cầu, không ép nghiệp vụ (business / 비즈니스) bài toán (problem / 문제) vào thuật toán quen thuộc.

> **Chuyển mạch:** Trong **cây khung nhỏ nhất**, các dấu vết trong **28. MST trong cơ sở dữ liệu/mạng/hệ thống thiết kế (design / 설계)** được đọc cùng nhau ở **Mô hình tư duy** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> MST là bài toán **mua connectivity với total cạnh chi phí nhỏ nhất**. Cut tính chất nói cạnh nào an toàn để thêm; chu trình tính chất nói cạnh nào an toàn để loại. Kruskal và Prim chỉ là hai operational views của cùng optimality cấu trúc (structure / 구조).

Khi gặp bài liên quan “connect tất cả với chi phí tổng nhỏ nhất”, hãy kiểm tra: đồ thị có undirected không, có cần redundancy không, có thêm các ràng buộc không. Nếu mục tiêu (objective / 목표) đúng là pure connectivity chi phí, MST là sự trừu tượng (abstraction) rất mạnh.

Xem thêm: [Union-Find](./05_union_find.md), [Tree Foundations](../02_trees/00_tree_foundations.md), [Greedy Algorithms](../04_algorithmic_paradigms/04_greedy_algorithms.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
