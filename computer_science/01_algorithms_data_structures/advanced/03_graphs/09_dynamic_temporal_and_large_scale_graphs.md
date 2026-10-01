# Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Tĩnh, tăng dần, giảm dần và fully động (dynamic / 동적)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Tại sao xóa khó hơn thêm?** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**động (dynamic / 동적), Temporal & Large-Scale Graphs / 동적·시간·대규모 그래프**

Các chương đồ thị cơ bản thường giả định topology đã biết và tương đối tĩnh trong lúc thuật toán chạy. Hệ thống thực tế lại thường thay đổi liên tục: cạnh được thêm/xóa, trọng số thay đổi, nút (node / 노드) tạm thời mất kết nối, sự kiện chỉ tồn tại trong một khoảng thời gian, và toàn bộ đồ thị có thể quá lớn để nằm vừa trên một máy.

Chương này tập trung vào câu hỏi: **điều gì thay đổi khi bản thân đồ thị trở thành dữ liệu động?**

## 1. Tĩnh, tăng dần, giảm dần và fully động (dynamic / 동적)

Cần phân biệt bốn mô hình cập nhật.

```text
static           -> không thay đổi topology
incremental      -> chỉ thêm cạnh/nút
decremental      -> chỉ xóa cạnh/nút
fully dynamic    -> vừa thêm vừa xóa
```

Sự phân biệt này quan trọng vì tính đơn điệu cho phép thuật toán đơn giản hơn rất nhiều.

Nếu chỉ thêm cạnh và chỉ hỏi connectivity vô hướng, DSU gần như hoàn hảo. Nhưng khi cho phép xóa, DSU chuẩn không biết một thành phần phải tách thành những phần nào vì nó đã nén mất topology chi tiết.

> **Chuyển mạch:** Trong **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **2. Tại sao xóa khó hơn thêm?** tiếp nhận điểm tựa từ **1. Tĩnh, tăng dần, giảm dần và fully động (dynamic / 동적)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Offline động (dynamic / 동적) Connectivity bằng Segment cây (tree / 트리) theo thời gian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Tại sao xóa khó hơn thêm?

Khi thêm một cạnh `(u,v)`, ta chỉ cần biết liệu nó nối hai thành phần khác nhau hay tạo thêm đường dư thừa.

Khi xóa một cạnh, phải trả lời câu hỏi khó hơn:

> Cạnh đó có phải là cầu trong topology hiện tại không, hay vẫn còn một đường thay thế khác?

Điều này yêu cầu thông tin về cấu trúc toàn cục, không chỉ thành phần (component / 컴포넌트) ID.

Đây là một mẫu (pattern / 패턴) tổng quát: thao tác **hủy một quan hệ** thường khó hơn thao tác **tích lũy quan hệ** vì phải phục hồi thông tin đã từng bị nén.

> **Chuyển mạch:** Ở chặng này của **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **3. Offline động (dynamic / 동적) Connectivity bằng Segment cây (tree / 트리) theo thời gian** tiếp nhận điểm tựa từ **2. Tại sao xóa khó hơn thêm?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Euler Tour cây (tree / 트리) và Link-Cut cây (tree / 트리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Offline động (dynamic / 동적) Connectivity bằng Segment cây (tree / 트리) theo thời gian

Nếu biết trước toàn bộ chuỗi thêm/xóa cạnh và truy vấn connectivity, ta có thể xử lý ngoại tuyến.

Mỗi cạnh tồn tại trong một khoảng thời gian:

```text
[timeAdded, timeRemoved)
```

Xây một Segment cây (tree / 트리) trên trục thời gian. Gắn mỗi cạnh vào các nút (node / 노드) của Segment cây (tree / 트리) phủ đúng khoảng thời gian nó tồn tại.

DFS cây thời gian:

1. snapshot trạng thái quay lui (rollback / 롤백) DSU;
2. union mọi cạnh thuộc nút (node / 노드) hiện tại;
3. đi xuống con;
4. ở lá, trả lời truy vấn tại thời điểm đó;
5. quay lui (rollback / 롤백) về snapshot khi quay lên.

Điểm tinh tế là quay lui (rollback / 롤백) DSU thường **không dùng đường dẫn (path / 경로) compression**, vì đường dẫn (path / 경로) compression tạo quá nhiều thay đổi khó hoàn tác. Union-by-size vẫn giữ chiều cao `O(log n)`.

Đây là một ví dụ đẹp về composition:

```text
interval over time
+ segment tree
+ rollback DSU
= dynamic connectivity offline
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **4. Euler Tour cây (tree / 트리) và Link-Cut cây (tree / 트리)** tiếp nhận điểm tựa từ **3. Offline động (dynamic / 동적) Connectivity bằng Segment cây (tree / 트리) theo thời gian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. động (dynamic / 동적) MST: tại sao khó?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Euler Tour cây (tree / 트리) và Link-Cut cây (tree / 트리)

Khi đồ thị là rừng động, các cấu trúc cây động cho phép `link`, `cut` và truy vấn trên đường/cây.

**Euler Tour cây (tree / 트리)** biểu diễn một cây bằng chuỗi Euler được lưu trong cây tìm kiếm cân bằng; cắt/nối cây trở thành split/merge của chuỗi.

**Link-Cut cây (tree / 트리)** dùng Splay cây (tree / 트리) để biểu diễn các preferred paths và hỗ trợ các thao tác như:

```text
link(u,v)
cut(u,v)
findRoot(u)
pathAggregate(u,v)
```

với cận khấu hao logarithmic trong mô hình chuẩn.

Đây là ví dụ nơi cây cân bằng không còn chỉ lưu khóa có thứ tự; nó trở thành động cơ cho topology động.

> **Chuyển mạch:** Trong **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **5. động (dynamic / 동적) MST: tại sao khó?** tiếp nhận điểm tựa từ **4. Euler Tour cây (tree / 트리) và Link-Cut cây (tree / 트리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. động (dynamic / 동적) Shortest đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. động (dynamic / 동적) MST: tại sao khó?

Nếu thêm một cạnh mới `(u,v,w)` vào MST hiện tại, cạnh này tạo một chu trình với đường duy nhất giữa `u` và `v` trong cây. Nếu `w` nhỏ hơn cạnh nặng nhất trên đường đó, ta có thể thay cạnh nặng nhất bằng cạnh mới.

Nghe đơn giản, nhưng cần trả nhanh:

```text
max edge weight on path(u,v)
```

và hỗ trợ cập nhật cấu trúc cây sau khi thay cạnh. Link-Cut cây (tree / 트리) hoặc Heavy-Light Decomposition có thể đóng vai trò.

Khi còn cho phép xóa cạnh bất kỳ khỏi đồ thị (graph / 그래프), bài toán phức tạp hơn vì nếu xóa cạnh thuộc MST, ta phải tìm cạnh nhẹ nhất nối lại hai thành phần.

Động (dynamic / 동적) MST cho thấy rõ sự khác biệt giữa **duy trì một lời giải tối ưu** và **tính lại lời giải từ đầu**.

> **Chuyển mạch:** Ở chặng này của **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **5. động (dynamic / 동적) MST: tại sao khó?** xác định đầu vào; **6. động (dynamic / 동적) Shortest đường dẫn (path / 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **7. Temporal đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. động (dynamic / 동적) Shortest đường dẫn (path / 경로)

Nếu chỉ một vài trọng số thay đổi, chạy lại Dijkstra toàn bộ có thể lãng phí. Các thuật toán incremental/decremental cố tái sử dụng khoảng cách cũ.

Tuy nhiên, shortest đường dẫn (path / 경로) rất nhạy: thay một cạnh gần nguồn có thể thay đổi khoảng cách của cả vùng lớn. Vì vậy không có một incremental cập nhật (update / 업데이트) đơn giản luôn rẻ.

Trong routing hệ thống (system / 시스템) thực tế, người ta thường kết hợp:

```text
incremental recomputation
region-local repair
hierarchical graph
cache invalidation
batch updates
```

thay vì kỳ vọng một cấu trúc động tổng quát giải mọi trường hợp tối ưu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **6. động (dynamic / 동적) Shortest đường dẫn (path / 경로)** xác định đầu vào; **7. Temporal đồ thị (graph / 그래프)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **8. Time-Expanded đồ thị (graph / 그래프) và Time-Dependent đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Temporal đồ thị (graph / 그래프)

Trong đồ thị thời gian, cạnh không chỉ có tồn tại/không tồn tại mà có timestamp hoặc khoảng hiệu lực.

Ví dụ chuyến tàu:

```text
A -> B departs 10:00 arrives 10:30
```

Một đường đi hợp lệ phải tôn trọng thứ tự thời gian; cạnh tiếp theo không thể khởi hành trước khi ta đến.

Do đó “đường đi ngắn nhất” có thể trở thành:

```text
earliest arrival
minimum waiting time
minimum number of transfers
```

Mỗi mục tiêu (objective / 목표) tạo một mô hình trạng thái khác.

> **Chuyển mạch:** Trong **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **8. Time-Expanded đồ thị (graph / 그래프) và Time-Dependent đồ thị (graph / 그래프)** tiếp nhận điểm tựa từ **7. Temporal đồ thị (graph / 그래프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Sliding-Window đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Time-Expanded đồ thị (graph / 그래프) và Time-Dependent đồ thị (graph / 그래프)

Một cách là tạo trạng thái `(vertex,time)` và nối các chuyển tiếp (transition / 전이) hợp lệ. Đây là **time-expanded đồ thị (graph / 그래프)**. Nó rõ ràng nhưng có thể rất lớn.

Một cách khác giữ mỗi cạnh như một hàm chi phí theo thời gian:

\[
w_e(t)
\]

Đây là **time-dependent đồ thị (graph / 그래프)**. Dijkstra-like lập luận (reasoning / 추론) chỉ hoạt động dưới các điều kiện nhất định, chẳng hạn FIFO thuộc tính (property / 속성): rời sớm hơn không thể đến muộn hơn chỉ vì đi cùng cạnh.

Nếu thuộc tính (property / 속성) này bị phá, greedy finalization của Dijkstra có thể không còn đúng.

> **Chuyển mạch:** Ở chặng này của **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **9. Sliding-Window đồ thị (graph / 그래프)** tiếp nhận điểm tựa từ **8. Time-Expanded đồ thị (graph / 그래프) và Time-Dependent đồ thị (graph / 그래프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. đồ thị (graph / 그래프) Streaming** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Sliding-Window đồ thị (graph / 그래프)

Trong fraud detection, khả năng quan sát (observability / 관측 가능성) hoặc telemetry, ta có thể chỉ quan tâm các cạnh trong `W` phút gần nhất.

Khi cửa sổ trượt:

```text
new events enter
after W time, old events expire
```

Topology liên tục thêm và xóa cạnh. Nếu chỉ cần thống kê cục bộ, có thể dùng bucket thời gian và rebuild định kỳ thay vì fully động (dynamic / 동적) cấu trúc (structure / 구조) phức tạp.

Đây là bài học thực tế quan trọng:

> Một thuật toán lý thuyết mạnh không phải lúc nào cũng tốt hơn một thiết kế batch + rebuild đơn giản nếu tải công việc cho phép.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **10. đồ thị (graph / 그래프) Streaming** tiếp nhận điểm tựa từ **9. Sliding-Window đồ thị (graph / 그래프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Reservoir Sampling trên cạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. đồ thị (graph / 그래프) Streaming

Khi số cạnh quá lớn để giữ toàn bộ trong RAM, thuật toán streaming chỉ xem mỗi cạnh một hoặc vài lượt với bộ nhớ nhỏ.

Các câu hỏi có thể là:

```text
ước lượng số tam giác
ước lượng degree distribution
phát hiện heavy hitters
sampling edges/nodes
approximate connectivity
```

Ta chấp nhận kết quả xấp xỉ hoặc nhiều pass để đổi lấy bộ nhớ nhỏ hơn.

Probabilistic sketches và reservoir sampling xuất hiện tự nhiên ở đây.

> **Chuyển mạch:** Trong **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **11. Reservoir Sampling trên cạnh** tiếp nhận điểm tựa từ **10. đồ thị (graph / 그래프) Streaming** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. đồ thị (graph / 그래프) Partitioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Reservoir Sampling trên cạnh

Nếu luồng cạnh có độ dài chưa biết và muốn giữ một mẫu đều kích thước `k`, Reservoir Sampling cho mỗi cạnh cùng xác suất cuối cùng `k/n`.

Mẫu này có thể dùng để ước lượng thống kê đồ thị (graph / 그래프) hoặc làm nền cho approximate motif counting.

Nhưng sampling edge đều không đồng nghĩa sampling vertex đều; nút (node / 노드) có degree cao xuất hiện nhiều hơn trong edge mẫu (sample / 표본). Phải phân biệt đơn vị lấy mẫu.

> **Chuyển mạch:** Ở chặng này của **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **12. đồ thị (graph / 그래프) Partitioning** tiếp nhận điểm tựa từ **11. Reservoir Sampling trên cạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Vertex Cut và Edge Cut** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. đồ thị (graph / 그래프) Partitioning

Đồ thị lớn trên nhiều máy phải được phân vùng. Mục tiêu thường đồng thời:

```text
cân bằng số node/edge giữa các máy
giảm số cạnh cắt qua partition
giảm communication
```

Đây là bài toán khó. Heuristic và multilevel methods thường được dùng trong thực tế.

Cách partition ảnh hưởng trực tiếp đến phân tán (distributed / 분산) BFS/PageRank/GNN vì cạnh cắt partition tạo mạng (network / 네트워크) traffic.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **13. Vertex Cut và Edge Cut** tiếp nhận điểm tựa từ **12. đồ thị (graph / 그래프) Partitioning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Power-Law đồ thị (graph / 그래프) và skew** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Vertex Cut và Edge Cut

**Edge cut** gán nút (node / 노드) vào partition; cạnh nối nút (node / 노드) ở hai partition tạo communication.

**Vertex cut** gán cạnh vào partition và có thể sao chép nút (node / 노드) degree cao trên nhiều partition.

Trong power-law đồ thị (graph / 그래프), một vài hub có degree cực lớn. Vertex-cut có thể phân tán tải tốt hơn nhưng phải đồng bộ trạng thái bản sao của nút (node / 노드).

Đây là một ví dụ biểu diễn (representation / 표현) quyết định scalability.

> **Chuyển mạch:** Trong **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **14. Power-Law đồ thị (graph / 그래프) và skew** tiếp nhận điểm tựa từ **13. Vertex Cut và Edge Cut** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Direction-Optimizing BFS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Power-Law đồ thị (graph / 그래프) và skew

Xã hội (social / 사회적) đồ thị (graph / 그래프), web đồ thị (graph / 그래프) và tương tác (interaction / 상호작용) đồ thị (graph / 그래프) thường có phân phối degree lệch mạnh: phần lớn nút (node / 노드) degree nhỏ, vài nút (node / 노드) degree cực lớn.

Một thuật toán chỉ phân tích theo average degree có thể bỏ qua hot spot ở hub nút (node / 노드).

Trong parallel traversal, một hub có thể tạo hàng triệu neighbor expansion trên một worker, gây mất cân bằng. Cần chunk adjacency, công việc (work / 작업) stealing hoặc specialized partitioning.

> **Chuyển mạch:** Ở chặng này của **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **15. Direction-Optimizing BFS** tiếp nhận điểm tựa từ **14. Power-Law đồ thị (graph / 그래프) và skew** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Bidirectional tìm kiếm (search / 검색)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Direction-Optimizing BFS

BFS truyền thống đi từ frontier ra neighbor, thường gọi là **top-down**.

Khi frontier trở nên rất lớn, có thể hiệu quả hơn nếu duyệt các nút (node / 노드) chưa thăm và hỏi “nút (node / 노드) này có neighbor nào thuộc frontier không?”. Đây là **bottom-up BFS**.

Direction-optimizing BFS chuyển giữa hai chế độ tùy kích thước frontier và số cạnh dự kiến phải quét.

Đây là một ví dụ thuật toán giữ cùng ngữ nghĩa (semantics / 의미론) nhưng thay hướng traversal theo shape của tải công việc (workload / 워크로드).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **16. Bidirectional tìm kiếm (search / 검색)** tiếp nhận điểm tựa từ **15. Direction-Optimizing BFS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Landmark và A** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Bidirectional tìm kiếm (search / 검색)

Nếu cần đường đi giữa một nguồn và một đích cụ thể trong đồ thị (graph / 그래프) không trọng số, BFS từ hai phía có thể giảm mạnh không gian tìm kiếm thực tế.

Thay vì mở rộng khoảng `b^d`, lý tưởng mỗi phía chỉ đi sâu khoảng `d/2`, cho tổng gần `2b^{d/2}`.

Cần cẩn thận khi đồ thị (graph / 그래프) có hướng: backward tìm kiếm (search / 검색) phải dùng transpose edges hoặc predecessor quan hệ (relation / 관계).

> **Chuyển mạch:** Trong **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **17. Landmark và A** tiếp nhận điểm tựa từ **16. Bidirectional tìm kiếm (search / 검색)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Contraction Hierarchies** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Landmark và A*

A* dùng heuristic `h(v)` để ưu tiên nút (node / 노드) có vẻ gần đích. Heuristic phải **admissible** để không đánh giá quá cao chi phí còn lại nếu muốn bảo đảm tối ưu trong mô hình chuẩn.

Landmark-based heuristics có thể tiền xử lý khoảng cách tới một số landmark và dùng bất đẳng thức tam giác để tạo lower bound tốt hơn.

Đây là sự đánh đổi (trade-off / 트레이드오프) giữa preprocessing/bộ nhớ (memory / 메모리) và truy vấn (query / 쿼리) độ trễ (latency / 지연 시간).

> **Chuyển mạch:** Ở chặng này của **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **18. Contraction Hierarchies** tiếp nhận điểm tựa từ **17. Landmark và A** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. động (dynamic / 동적) đồ thị (graph / 그래프) bộ nhớ đệm (cache / 캐시) và versioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Contraction Hierarchies

Tuyến (route / 경로) planning đường bộ thực tế có thể có hàng triệu nút (node / 노드). Chạy Dijkstra toàn đồ thị (graph / 그래프) cho mỗi truy vấn có thể quá chậm.

**Contraction Hierarchies** lần lượt loại nút (node / 노드) ít quan trọng và thêm shortcut để bảo toàn khoảng cách. truy vấn (query / 쿼리) sau đó chủ yếu đi qua hierarchy.

Ý tưởng sâu là chuyển chi phí sang preprocessing để tạo một đồ thị (graph / 그래프) mới cùng chỉ số (metric / 지표) nhưng dễ tìm kiếm (search / 검색) hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **19. động (dynamic / 동적) đồ thị (graph / 그래프) bộ nhớ đệm (cache / 캐시) và versioning** tiếp nhận điểm tựa từ **18. Contraction Hierarchies** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. đồ thị (graph / 그래프) Snapshot** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. động (dynamic / 동적) đồ thị (graph / 그래프) bộ nhớ đệm (cache / 캐시) và versioning

Nếu truy vấn (query / 쿼리) đồ thị (graph / 그래프) đắt, hệ thống có thể bộ nhớ đệm (cache / 캐시):

```text
shortest path
reachability
component summary
neighborhood expansion
```

Nhưng topology thay đổi làm bộ nhớ đệm (cache / 캐시) cũ. vô hiệu hóa (invalidation / 무효화) có thể theo phiên bản (version / 버전) đồ thị (graph / 그래프), epoch, region hoặc phụ thuộc (dependency / 의존성) set.

Không nên dùng kết quả cũ nếu không xác định rõ consistency yêu cầu (requirement / 요구사항). “đồ thị (graph / 그래프) bộ nhớ đệm (cache / 캐시)” là bài toán tính đúng đắn (correctness / 정확성), không chỉ hiệu năng (performance / 성능).

> **Chuyển mạch:** Trong **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **20. đồ thị (graph / 그래프) Snapshot** tiếp nhận điểm tựa từ **19. động (dynamic / 동적) đồ thị (graph / 그래프) bộ nhớ đệm (cache / 캐시) và versioning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. tính đồng thời (concurrency / 동시성) và mutation trong traversal** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. đồ thị (graph / 그래프) Snapshot

Một chiến lược phổ biến là xử lý cập nhật (update / 업데이트) liên tục nhưng xuất bản snapshot bất biến theo epoch.

Reader dùng snapshot ổn định; writer xây snapshot tiếp theo. Điều này đơn giản hóa thuật toán vì traversal không phải xử lý topology đổi giữa chừng.

Đổi lại, kết quả có độ trễ cập nhật. Đây là sự đánh đổi (trade-off / 트레이드오프) giữa **freshness** và **simplicity/consistency**.

> **Chuyển mạch:** Ở chặng này của **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **21. tính đồng thời (concurrency / 동시성) và mutation trong traversal** tiếp nhận điểm tựa từ **20. đồ thị (graph / 그래프) Snapshot** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Testing động (dynamic / 동적) đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. tính đồng thời (concurrency / 동시성) và mutation trong traversal

Nếu một luồng đang BFS trong khi luồng khác xóa cạnh, câu hỏi “BFS đang duyệt đồ thị (graph / 그래프) nào?” phải có câu trả lời.

Các lựa chọn gồm:

```text
khóa graph
snapshot isolation
copy-on-write
versioned adjacency
chấp nhận weak consistency
```

Không có một ngữ nghĩa (semantics / 의미론) mặc định đúng cho mọi hệ thống.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **22. Testing động (dynamic / 동적) đồ thị (graph / 그래프)** tiếp nhận điểm tựa từ **21. tính đồng thời (concurrency / 동시성) và mutation trong traversal** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Benchmark phải phản ánh cập nhật (update / 업데이트)/truy vấn (query / 쿼리) ratio** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Testing động (dynamic / 동적) đồ thị (graph / 그래프)

Cách kiểm thử mạnh nhất là differential testing với đồ thị (graph / 그래프) nhỏ.

Với động (dynamic / 동적) connectivity:

```text
thực hiện chuỗi add/remove/query ngẫu nhiên
sau mỗi query, chạy BFS/DFS brute force trên graph hiện tại
so kết quả với cấu trúc động
```

Với động (dynamic / 동적) shortest đường dẫn (path / 경로), có thể chạy Dijkstra/Floyd-Warshall từ đầu trên đồ thị (graph / 그래프) nhỏ làm oracle.

Đặc biệt cần sinh:

```text
xóa bridge
thêm cạnh song song
self-loop
remove edge không tồn tại
add/remove lặp lại
batch update cùng timestamp
```

> **Chuyển mạch:** Trong **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **23. Benchmark phải phản ánh cập nhật (update / 업데이트)/truy vấn (query / 쿼리) ratio** tiếp nhận điểm tựa từ **22. Testing động (dynamic / 동적) đồ thị (graph / 그래프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. quyết định (decision / 결정) khung phần mềm (framework / 프레임워크)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Benchmark phải phản ánh cập nhật (update / 업데이트)/truy vấn (query / 쿼리) ratio

Một cấu trúc động chỉ đáng dùng nếu giảm tổng chi phí thực tế.

Cần đo:

```text
updates/second
queries/second
ratio update:query
p95/p99 latency
memory overhead
rebuild cost
staleness nếu dùng snapshot
```

Nếu 99.99% thời gian đồ thị (graph / 그래프) không thay đổi, một cấu trúc static tối ưu + rebuild hiếm có thể đơn giản và nhanh hơn fully động (dynamic / 동적) thuật toán (algorithm / 알고리즘).

> **Chuyển mạch:** Ở chặng này của **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **24. quyết định (decision / 결정) khung phần mềm (framework / 프레임워크)** tiếp nhận điểm tựa từ **23. Benchmark phải phản ánh cập nhật (update / 업데이트)/truy vấn (query / 쿼리) ratio** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. quyết định (decision / 결정) khung phần mềm (framework / 프레임워크)

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

| Tình huống | Hướng tiếp cận |
|---|---|
| Chỉ thêm cạnh, hỏi connectivity | DSU |
| Add/remove biết trước | Segment cây (tree / 트리) over thời gian (time / 시간) + quay lui (rollback / 롤백) DSU |
| Rừng động | Euler Tour cây (tree / 트리) / Link-Cut cây (tree / 트리) |
| Nhiều đường dẫn (path / 경로) truy vấn (query / 쿼리) trên cây (tree / 트리) động | Link-Cut cây (tree / 트리) hoặc cấu trúc chuyên biệt |
| đồ thị (graph / 그래프) temporal | time-expanded / time-dependent mô hình (model / 모델) |
| đồ thị (graph / 그래프) cực lớn | CSR + partitioning / streaming |
| truy vấn (query / 쿼리) nhiều, cập nhật (update / 업데이트) theo batch | snapshot + preprocessing |
| tuyến (route / 경로) truy vấn (query / 쿼리) rất nhiều | hierarchy / landmark / A* |

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đồ thị động, đồ thị thời gian và đồ thị quy mô lớn**, **Mô hình tư duy** gom các mảnh từ **24. quyết định (decision / 결정) khung phần mềm (framework / 프레임워크)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Đồ thị động không chỉ là “đồ thị thường + cập nhật”. Khi topology thay đổi, ta phải quyết định **thời điểm nào được xem là cùng một trạng thái đồ thị (graph / 그래프)**, thông tin nào được duy trì incremental, và thông tin nào nên tính lại theo batch.

Ba câu hỏi quan trọng nhất là:

```text
Update có đơn điệu không?
Có thể xử lý offline không?
Query cần dữ liệu mới đến mức nào?
```

Nếu trả lời được ba câu đó, không gian thiết kế thường thu hẹp mạnh.

Xem thêm: [Graph Modeling](./00_graph_modeling_and_representation.md), [Union-Find](./05_union_find.md), [Shortest Paths](./02_shortest_paths.md), [MST](./03_minimum_spanning_trees.md), [Rollback/Amortized Thinking](../05_specialized/03_amortized_randomized_and_probabilistic_thinking.md), [Routing Case Study](../90_connections/05_case_study_routing_graph_system.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
