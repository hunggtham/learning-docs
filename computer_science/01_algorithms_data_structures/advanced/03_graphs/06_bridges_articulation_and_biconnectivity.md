# Bridges, các điểm khớp và Biconnectivity

> **Mạch đọc:** Đọc **Bridges, các điểm khớp và Biconnectivity** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Tại sao DFS cây chưa đủ?** sang **2. tin[u]: thời điểm khám phá**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

**Bridges, các điểm khớp & Biconnectivity / 단절선, 단절점, 이중 연결성**

Một connected đồ thị có thể trông “dày”, nhưng chỉ cần hỏng đúng một cạnh hoặc một đỉnh là topology bị tách đôi. **cầu nối (bridge / 브리지) / 단절선** là cạnh mà khi xóa làm số connected các thành phần tăng. **điểm khớp / 단절점** là đỉnh mà khi xóa cùng sự cố (incident / 인시던트) các cạnh làm số các thành phần tăng.

Đây là cách đồ thị lý thuyết (theory / 이론) diễn tả **single điểm (point / 지점) of thất bại (failure / 실패)**. Trong mạng, cầu nối (bridge / 브리지) có thể là đường truyền duy nhất; điểm khớp có thể là router/hub trung tâm. Nhưng mục tiêu của chapter này không chỉ là học công thức `low[v] > tin[u]`; quan trọng hơn là hiểu **low-link giá trị đang tóm tắt khả năng escape khỏi một DFS cây con như thế nào**.

## 1. Tại sao DFS cây chưa đủ?

Khi chạy DFS trên đồ thị vô hướng (undirected graph), mỗi đỉnh lần đầu được khám phá qua một cây cạnh. Nếu chỉ nhìn DFS cây, mọi parent-child cạnh dường như đều “quan trọng”, vì cây con nút con treo dưới nút cha.

Nhưng đồ thị gốc có thể có cạnh khác từ cây con quay lên một tổ tiên. cạnh đó tạo alternate tuyến (route / 경로). Vì vậy câu hỏi thật sự là:

> cây con của nút con có thể thoát ra ngoài mà không cần dùng lại nút cha cạnh hay không?

`low` chính là dữ liệu tóm lược cho câu hỏi này.

## 2. `tin[u]`: thời điểm khám phá

Khi DFS vào `u`:

```text
tin[u] = low[u] = timer++
```

`tin` tạo thứ tự khám phá. tổ tiên trong DFS cây luôn có `tin` nhỏ hơn hậu duệ.

`low[u]` ban đầu bằng `tin[u]` vì chắc chắn cây con của `u` có thể tới tới chính `u`.

## 3. Meaning của `low[u]`

Trong undirected DFS chuẩn, `low[u]` là thời điểm khám phá nhỏ nhất của đỉnh có thể có thể tới từ `u` hoặc các hậu duệ bằng cách đi xuống zero/more cây các cạnh rồi dùng tối đa một back cạnh lên tổ tiên theo cấu trúc (structure / 구조) relevant.

cập nhật các quy tắc:

Khi nút con `v` xong:

\[
low[u]=\min(low[u],low[v])
\]

Khi gặp đã thăm đỉnh kề `v` qua một cạnh không phải nút cha cạnh:

\[
low[u]=\min(low[u],tin[v])
\]

Điểm quan trọng: với back cạnh dùng `tin[v]`, không tùy tiện dùng `low[v]`, vì low của một đã thăm đỉnh có thể encode đường đi không tương ứng với cạnh classification hiện tại.

## 4. cầu nối (bridge / 브리지) điều kiện

Với DFS cây cạnh `(u,v)`:

\[
low[v] > tin[u]
\]

thì `(u,v)` là cầu nối (bridge / 브리지).

Nếu cây con `v` không thể reach `u` hoặc tổ tiên của `u` bằng tuyến (route / 경로) khác, nút cha cạnh là cửa duy nhất ra ngoài. Xóa nó làm cây con tách khỏi phần còn lại.

## 5. Vì sao là `>` chứ không phải `>=`?

Nếu:

\[
low[v]=tin[u]
\]

nghĩa là cây con có back cạnh quay lại chính `u`. Khi xóa cây cạnh `(u,v)`, alternate tuyến (route / 경로) đó vẫn nối cây con với `u`. Vì vậy cạnh không phải cầu nối (bridge / 브리지).

Equality đủ cứu cạnh, nhưng không đủ cứu đỉnh như articulation điều kiện phía dưới.

## 6. điểm khớp cho non-root

Với non-root `u`, nếu tồn tại nút con `v`:

\[
low[v] \ge tin[u]
\]

thì `u` là điểm khớp.

Nếu equality xảy ra, cây con `v` có thể quay về `u`, nhưng xóa chính `u` thì tuyến (route / 경로) đó cũng biến mất. cây con không reach được tổ tiên cao hơn.

Đây là lý do articulation dùng `>=` còn cầu nối (bridge / 브리지) dùng `>`.

## 7. nút gốc là trường hợp (case / 사례) đặc biệt

DFS nút gốc không có tổ tiên phía trên. nút gốc là điểm khớp khi có **ít nhất hai DFS cây các nút con**.

Nếu nút gốc chỉ có một nút con, toàn bộ phần có thể tới nằm trong một cây con; xóa nút gốc không làm phần còn lại tách thành nhiều các thành phần mới hơn theo definition chuẩn.

Nếu nút gốc có hai các nút con, DFS từ nút con thứ nhất đã không thể reach nút con thứ hai trước khi return, nên nút gốc là điểm nối duy nhất giữa chúng trong DFS cấu trúc (structure / 구조).

## 8. cạnh ID bắt buộc khi có các cạnh song song

Trong multigraph, check:

```text
if (v == parent) continue
```

có thể sai. Giữa `u` và nút cha có thể tồn tại hai cạnh song song: một cạnh là cây cạnh, cạnh còn lại là alternate back liên kết (connection / 연결).

Cách robust là mỗi vật lý cạnh có unique ID, và DFS nhận `parentEdgeId`:

```java
if (e.id == parentEdgeId) continue;
```

cách biểu diễn (representation / 표현) detail này ảnh hưởng trực tiếp tính đúng đắn.

## 9. Java cốt lõi (core / 핵심) cách triển khai

```java
void dfs(int u, int parentEdge) {
    seen[u] = true;
    tin[u] = low[u] = timer++;
    int children = 0;

    for (Edge e : g.get(u)) {
        if (e.id == parentEdge) continue;
        int v = e.to;

        if (seen[v]) {
            low[u] = Math.min(low[u], tin[v]);
        } else {
            dfs(v, e.id);
            low[u] = Math.min(low[u], low[v]);

            if (low[v] > tin[u]) {
                bridges.add(e.id);
            }

            if (parentEdge != -1 && low[v] >= tin[u]) {
                articulation[u] = true;
            }

            children++;
        }
    }

    if (parentEdge == -1 && children > 1) {
        articulation[u] = true;
    }
}
```

đồ thị không liên thông cần DFS từ mọi chưa thăm đỉnh.

## 10. độ phức tạp (complexity / 복잡도)

Mỗi đỉnh visit một lần, mỗi undirected cạnh xuất hiện hai adjacency các mục và được xử lý constant number of times:

\[
O(V+E)
\]

Không gian (space / 공간) gồm đồ thị, các mảng và DFS ngăn xếp (stack / 스택). Recursive cách triển khai có độ sâu `O(V)` trên đường đi đồ thị và có thể ngăn xếp (stack / 스택) tràn số.

## 11. Iterative low-link DFS khó hơn DFS thường

lời gọi đệ quy tự động tạo postorder sự kiện: nút con hoàn tất rồi mới cập nhật `low[parent]`.

Iterative DFS phải tường minh (explicit / 명시적) frame:

```text
vertex
parentEdge
nextAdjIndex
numberOfChildren
```

Khi frame nút con pop, nút cha mới có thể apply:

```text
low[parent] = min(low[parent], low[child])
```

Đây là ví dụ rõ rằng recursion frame lưu continuation trạng thái (state / 상태), không chỉ đỉnh ID.

## 12. Characterization: cầu nối (bridge / 브리지) iff cạnh không thuộc chu trình

Trong đồ thị vô hướng:

> cạnh là cầu nối (bridge / 브리지) khi và chỉ khi nó không thuộc bất kỳ chu trình nào.

Nếu thuộc chu trình, phần còn lại của chu trình tạo alternate tuyến (route / 경로). Nếu không thuộc chu trình, cạnh là link duy nhất giữa hai phía theo topology tương ứng.

Low-link DFS là cách tìm tất cả cầu nối (bridge / 브리지) cùng lúc thay vì kiểm tra từng cạnh riêng lẻ.

## 13. Cách đơn giản remove-and-test vì sao đắt?

Với mỗi cạnh, remove rồi DFS/BFS:

\[
O(E(V+E))
\]

Với articulation:

\[
O(V(V+E))
\]

Low-link nén toàn bộ alternate-connectivity thông tin vào một DFS linear-time. Đây là một ví dụ điển hình của **precompute dữ liệu tóm lược thay recompute toàn bài toán (problem / 문제) cho từng ứng viên**.

## 14. 2-edge-connected các thành phần và cầu nối (bridge / 브리지) cây

Nếu remove tất cả bridges, đồ thị tách thành các thành phần mà bên trong không còn cầu nối (bridge / 브리지).

Co mỗi thành phần thành một siêu nút; các cầu ban đầu trở thành cạnh giữa các siêu nút. Kết quả là một cây hoặc rừng gọi là **cây cầu (bridge tree)**.

Tại sao không thể có chu trình giữa super-nodes? Nếu có chu trình, cầu nối (bridge / 브리지) trên chu trình có alternate tuyến (route / 경로), mâu thuẫn nó là cầu nối (bridge / 브리지).

Cầu nối (bridge / 브리지) cây biến đồ thị vulnerability bài toán (problem / 문제) thành cây bài toán (problem / 문제).

## 15. các truy vấn sau khi xây dựng cầu nối (bridge / 브리지) cây

Sau decomposition, nhiều các truy vấn dễ hơn:

```text
bao nhiêu bridge trên path giữa u và v?
edge failure nào tách hai nodes?
components nào nằm hai phía của bridge?
```

Map original các đỉnh sang bridge-component rồi dùng LCA/prefix độ sâu trên cây để trả lời đường đi các truy vấn.

Một expensive đồ thị tiền xử lý có thể đổi nhiều trực tuyến các truy vấn thành cây arithmetic nhanh.

## 16. Vertex-biconnected các thành phần

Articulation decomposition tinh tế hơn vì articulation đỉnh có thể thuộc nhiều blocks.

Một **biconnected thành phần / khối (block / 블록)** là maximal subgraph không bị tách bởi removal một nội bộ single đỉnh theo definition tương ứng.

Tarjan-style thuật toán giữ ngăn xếp (stack / 스택) of các cạnh. Khi nút con `v` thỏa:

\[
low[v] \ge tin[u]
\]

thì cạnh ngăn xếp (stack / 스택) từ `(u,v)` trở lên tạo một khối (block / 블록) mới.

## 17. Block-Cut cây

Ta tạo hai loại các nút:

```text
block nodes
articulation-vertex nodes
```

Nối articulation nút với khối (block / 블록) nút nếu articulation thuộc khối (block / 블록) đó. Kết quả là bipartite cây/forest gọi là **block-cut cây**.

Cấu trúc (structure / 구조) này hỗ trợ lập luận (reasoning / 추론) kiểu:

```text
path giữa hai regions phải đi qua articulation nào?
bao nhiêu single-vertex failure points trên route structural?
```

## 18. cạnh connectivity vs đỉnh connectivity

Cầu nối (bridge / 브리지) liên quan **cạnh redundancy**. Articulation liên quan **đỉnh redundancy**.

Một đồ thị có thể không có cầu nối (bridge / 브리지) nhưng vẫn có điểm khớp. Ví dụ hai các chu trình chia sẻ một đỉnh: không cạnh đơn lẻ nào làm đồ thị disconnect, nhưng xóa đỉnh chung sẽ tách hai các chu trình.

Vì vậy “mạng có nhiều alternate các cạnh” chưa đủ chứng minh node-level fault tolerance.

## 19. Menger's Theorem liên kết (connection / 연결)

Menger cho một liên kết (connection / 연결) sâu giữa:

```text
minimum cut size
number of disjoint paths
```

Cầu nối (bridge / 브리지) nghĩa cạnh connectivity giữa một số regions bằng 1. điểm khớp nghĩa đỉnh connectivity ở nơi đó bằng 1.

Low-link thuật toán là chuyên biệt linear-time detector cho những kích thước lát cắt 1 cases.

Nếu cần lát cắt cực tiểu lớn hơn 1/general capacities, ta tiến sang luồng (flow / 흐름)/min-cut các thuật toán.

## 20. cầu nối (bridge / 브리지) cây và độ tin cậy (reliability / 신뢰성) scoring

Có thể xem mỗi cầu nối (bridge / 브리지) là một miền lỗi (failure domain / 장애 도메인) ranh giới. kích thước (size / 크기) của cây con sau khi nút gốc cầu nối (bridge / 브리지) cây cho biết bao nhiêu các đỉnh bị cô lập nếu cầu nối (bridge / 브리지) hỏng.

Nếu muốn rank “impact” của cầu nối (bridge / 브리지), một chỉ số (metric / 지표) đơn giản có thể dựa trên số pairs bị disconnect:

\[
kích thước (size / 크기) \cdot (N-size)
\]

với `size` là số original các đỉnh ở một phía.

Đây là ví dụ biến structural decomposition thành rủi ro (risk / 위험) chỉ số (metric / 지표), nhưng hệ thống thực tế mô hình có thể cần các trọng số/lưu lượng/sức chứa (capacity / 용량) thực tế.

## 21. Articulation impact không chỉ boolean

Biết `u` là điểm khớp mới là bước đầu. Một câu hỏi sâu hơn là xóa `u` tạo bao nhiêu các thành phần và sizes ra sao.

Mỗi DFS nút con với:

\[
low[nút con] \ge tin[u]
\]

trở thành một separated region khi xóa `u`. Phần ancestors/outside cây con tạo thêm một region nếu `u` không phải DFS nút gốc.

Có thể augment DFS với cây con sizes để tính impact.

## 22. trực tuyến/động đồ thị khác hẳn tĩnh low-link

Nếu các cạnh được add/remove liên tục, chạy Tarjan lại sau mỗi cập nhật có thể đắt.

Incremental/động connectivity và động biconnectivity là advanced topics cần các cấu trúc dữ liệu phức tạp hơn. Low-link là giải pháp tĩnh đồ thị rất mạnh nhưng không tự hỗ trợ arbitrary các cập nhật.

Đây là mẫu quan trọng: một tuyến tính (linear / 선형) tiền xử lý thuật toán chưa chắc phù hợp trực tuyến khối lượng công việc.

## 23. đồ thị có hướng không dùng cùng công thức

Chuẩn cầu nối (bridge / 브리지)/articulation chapter này là đồ thị vô hướng. đồ thị có hướng có:

```text
strong bridges
strong articulation points
dominators
SCC-based structure
```

và các thuật toán khác. bản sao (copy / 복사) `low[v] > tin[u]` sang đồ thị có hướng là sai mô hình.

## 24. Low-link của cầu nối (bridge / 브리지) thuật toán và Tarjan SCC không interchangeable

Cả hai dùng biến tên `low`, nhưng bất biến (invariant / 불변식) khác.

Low-link trong bài toán cầu biểu diễn khả năng đi từ cây con DFS vô hướng lên một tổ tiên thông qua cạnh ngược.

Low-link trong Tarjan SCC liên quan tới chỉ số khám phá sớm nhất có thể đi tới trong ngữ cảnh ngăn xếp DFS đang hoạt động của thành phần liên thông mạnh.

Tên biến giống nhau không có nghĩa cập nhật quy tắc giống nhau.

## 25. các khuyên và các cạnh song song

Self-loop không thể là cầu nối (bridge / 브리지) vì bỏ nó không thay connectivity giữa các đỉnh. Nó có thể ảnh hưởng adjacency xử lý nhưng không làm alternate thành phần liên kết (connection / 연결).

các cạnh song song khiến hai endpoints có alternate cạnh trực tiếp, nên từng cạnh riêng lẻ không phải cầu nối (bridge / 브리지) nếu có ít nhất hai parallel connections.

Kiểm thử (test / 테스트) multigraph là cách rất tốt để phát hiện mã (code / 코드) dùng `parent vertex` thay vì `parent edge id`.

## 26. kiểm thử bằng đồ thị families

Các cases quan trọng:

```text
path: mọi edge bridge, internal vertex articulation
simple cycle: không bridge/articulation
star: mọi spoke bridge, center articulation
clique: thường không bridge/articulation
hai cycles nối bằng bridge
hai cycles share một vertex
parallel-edge pair
self-loop
single vertex
disconnected graph
```

ngẫu nhiên đồ thị nhỏ có thể verify cầu nối (bridge / 브리지) bằng brute-force remove cạnh + BFS, articulation bằng remove đỉnh + BFS.

Differential kiểm thử kiểu này rất mạnh vì oracle đơn giản dù chậm.

## 27. bất biến kiểm thử của `tin/low`

Sau DFS:

```text
low[u] <= tin[u]
```

cho mọi đã thăm đỉnh.

Với nút con cây cạnh, nút cha cập nhật phải làm `low[parent] <= low[child]` không nhất thiết luôn đúng vì nút cha có back cạnh riêng, nhưng `low[parent]` phải bằng min của relevant contributions.

Một bộ xác minh/gỡ lỗi cách triển khai có thể recompute low-like reachability trên đồ thị nhỏ để so kết quả.

## 28. các hệ thống interpretation và limitation

Mô hình cầu/đỉnh khớp chủ yếu xét tính liên thông theo kiểu nhị phân: còn liên thông hay bị tách rời. Tuy nhiên độ tin cậy trong hệ thống thực tế còn phụ thuộc nhiều yếu tố khác:

```text
capacity
latency
traffic volume
failure probability
shared physical conduit
availability zones
```

Hai lô-gic (logic / 논리) các cạnh có thể đi chung một cable vật lý; đồ thị nhìn redundant nhưng miền lỗi (failure domain / 장애 도메인) thực tế không redundant.

thuật toán chỉ đúng với mô hình. độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링) bắt đầu từ đồ thị sự trừu tượng (abstraction) chính xác.

## 29. liên kết (connection / 연결) với spanning cây

Mọi cầu nối (bridge / 브리지) phải xuất hiện trong **mọi spanning cây** của connected đồ thị, vì bỏ cầu nối (bridge / 브리지) làm đồ thị disconnect nên không có alternate cạnh set nối hai phía.

Ngược lại cạnh không cầu nối (bridge / 브리지) có thể hoặc không xuất hiện trong một spanning cây tùy choices.

Liên kết (connection / 연결) này liên kết low-link connectivity với MST/spanning-tree lý thuyết (theory / 이론).

## 30. liên kết (connection / 연결) với Eulerian đồ thị

Một connected undirected Eulerian đồ thị mà mọi đỉnh có even degree không thể có cầu nối (bridge / 브리지) nếu có ít nhất một cạnh trong thành phần Eulerian chu trình covering all các cạnh: mọi cạnh nằm trên chu trình của Euler tour.

Đây là một cách thấy các đồ thị các tính chất không độc lập; degree/chu trình cấu trúc (structure / 구조) ảnh hưởng cut vulnerability.

## Mô hình tư duy

> `low[u]` là một **compressed escape certificate** của DFS cây con: cây con này có alternate tuyến (route / 경로) lên tổ tiên cao đến đâu mà không quay lại nút cha cạnh?

Nếu nút con không escape tới nút cha, nút cha cạnh là cầu nối (bridge / 브리지). Nếu nút con chỉ escape tới chính nút cha nhưng không vượt nút cha, xóa nút cha đỉnh sẽ cô lập nút con cây con. Từ cục bộ dữ liệu tóm lược `low`, ta suy ra toàn cục vulnerability trong `O(V+E)`.

Xem thêm: [Graph Traversal](./01_graph_traversal_bfs_dfs.md), [MST](./03_minimum_spanning_trees.md), [SCC](./04_dag_topological_sort_and_scc.md), [Network Flow](./08_network_flow_and_matching.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 graph modeling and representation](./00_graph_modeling_and_representation.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
