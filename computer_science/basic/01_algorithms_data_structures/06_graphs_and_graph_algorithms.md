# Đồ thị (graph / 그래프) và đồ thị (graph / 그래프) algorithms

> **Mạch đọc:** Đọc **đồ thị (graph / 그래프) và đồ thị (graph / 그래프) algorithms** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **đồ thị (graph / 그래프) mô hình (model / 모델)** sang **biểu diễn (representation / 표현): adjacency danh sách (list / 목록) vs ma trận (matrix / 행렬)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi relationships không còn hierarchy đơn giản, đồ thị (graph / 그래프) trở thành mô hình (model / 모델) tự nhiên. xã hội (social / 사회적) mạng (network / 네트워크), road map, phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), mạng (network / 네트워크) topology, hệ thống dựng (build system / 빌드 시스템), lời gọi (call / 호출) đồ thị (graph / 그래프) và cơ sở dữ liệu (database / 데이터베이스) foreign-key relationships đều có thể mô hình (model / 모델) bằng vertices và edges.

## Đồ thị (graph / 그래프) mô hình (model / 모델)

Đồ thị (graph / 그래프) `G=(V,E)` gồm vertices/nodes `V` và edges `E`. Directed đồ thị (graph / 그래프) có edge `u→v`; undirected đồ thị (graph / 그래프) coi quan hệ (relation / 관계) hai chiều. Edge có thể mang weight như distance, chi phí (cost / 비용), độ trễ (latency / 지연 시간) hoặc sức chứa (capacity / 용량).

Degree đếm connections; đường dẫn (path / 경로) là chuỗi (sequence / 시퀀스) vertices nối qua edges; cycle quay về vertex đã gặp. Connected components phân vùng đồ thị (graph / 그래프) undirected thành vùng reachable. Directed đồ thị (graph / 그래프) có strongly connected components khi mỗi nút (node / 노드) reach nhau theo hướng.

Xem nền toán tại [Graph Theory](../../../mathematics/07_discrete_cs/00_graph_theory.md).


> **Chuyển mạch:** Từ **đồ thị (graph / 그래프) mô hình (model / 모델)**, ta sang **biểu diễn (representation / 표현): adjacency danh sách (list / 목록) vs ma trận (matrix / 행렬)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Biểu diễn (representation / 표현): adjacency danh sách (list / 목록) vs ma trận (matrix / 행렬)

Adjacency ma trận (matrix / 행렬) dùng `|V|×|V|` entries, edge lookup O(1) nhưng không gian (space / 공간) O(V²). Phù hợp dense đồ thị (graph / 그래프) hoặc algebraic operations.

Adjacency danh sách (list / 목록) lưu neighbors cho mỗi vertex, không gian (space / 공간) O(V+E), phù hợp sparse graphs phổ biến. biểu diễn (representation / 표현) quyết định iteration chi phí (cost / 비용) và locality.


> **Chuyển mạch:** Từ **biểu diễn (representation / 표현): adjacency danh sách (list / 목록) vs ma trận (matrix / 행렬)**, ta sang **BFS: shortest đường dẫn (path / 경로) theo số cạnh** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## BFS: shortest đường dẫn (path / 경로) theo số cạnh

Breadth-First tìm kiếm (search / 검색) dùng hàng đợi (queue / 큐) và khám phá theo layers. Với unweighted đồ thị (graph / 그래프), lần đầu reach vertex cho shortest number-of-edges distance.

Bất biến (invariant / 불변식): trước khi xử lý tầng (layer / 계층) distance d+1, tất cả vertices distance ≤d đã được discovered theo shortest distance. độ phức tạp (complexity / 복잡도) adjacency-list O(V+E) vì mỗi vertex/edge xử lý bounded times.

BFS dùng trong degrees-of-separation, shortest hops, crawling và level-order traversal.


> **Chuyển mạch:** Từ **BFS: shortest đường dẫn (path / 경로) theo số cạnh**, ta sang **DFS: đi sâu để lộ cấu trúc (structure / 구조)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## DFS: đi sâu để lộ cấu trúc (structure / 구조)

Depth-First tìm kiếm (search / 검색) dùng recursion hoặc tường minh (explicit / 명시적) ngăn xếp (stack / 스택). Entry/exit times và recursion ngăn xếp (stack / 스택) giúp detect cycles, topological sorting, SCC algorithms và articulation phân tích (analysis / 분석).

DFS không bảo đảm shortest đường dẫn (path / 경로) trong unweighted đồ thị (graph / 그래프), vì nó có thể chọn một nhánh dài trước.


> **Chuyển mạch:** Từ **DFS: đi sâu để lộ cấu trúc (structure / 구조)**, ta sang **Topological sort và phụ thuộc (dependency / 의존성)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Topological sort và phụ thuộc (dependency / 의존성)

Directed acyclic đồ thị (graph / 그래프) — DAG cho phép tuyến tính (linear / 선형) thứ tự (order / 순서) sao cho mọi phụ thuộc (dependency / 의존성) đứng trước dependent. bản dựng (build / 빌드) các hệ thống (systems / 시스템들), course prerequisites và workflow dependencies dùng topological sort.

Nếu đồ thị (graph / 그래프) có cycle, topological thứ tự (order / 순서) không tồn tại. Cycle thường chính là tín hiệu (signal / 신호) thiết kế: gói (package / 패키지) A phụ thuộc B phụ thuộc lại A; di chuyển (migration / 마이그레이션) dependencies vòng lặp (loop / 루프); tasks deadlock lô-gic (logic / 논리).


> **Chuyển mạch:** Từ **Topological sort và phụ thuộc (dependency / 의존성)**, ta sang **Dijkstra và weighted shortest đường dẫn (path / 경로)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dijkstra và weighted shortest đường dẫn (path / 경로)

Dijkstra giải shortest paths khi edge weights non-negative. Nó repeatedly chọn unsettled vertex có smallest tentative distance, thường bằng priority hàng đợi (queue / 큐).

Tại sao non-negative quan trọng? Khi chọn distance nhỏ nhất làm final, một edge âm từ nút (node / 노드) chưa xử lý có thể sau đó tạo đường ngắn hơn, phá bất biến (invariant / 불변식). Với negative edges, Bellman–Ford hoặc mô hình (model / 모델) khác cần dùng.


> **Chuyển mạch:** Từ **Dijkstra và weighted shortest đường dẫn (path / 경로)**, ta sang **Minimum Spanning cây (tree / 트리)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Minimum Spanning cây (tree / 트리)

MST kết nối mọi vertices với total edge weight nhỏ nhất, không tạo cycles. Kruskal sort edges rồi thêm nếu không nối hai vertices đã connected, thường dùng Union-Find/Disjoint Set. Prim phát triển một cây (tree / 트리) từ frontier.

MST khác shortest-path cây (tree / 트리): tối ưu tổng mạng (network / 네트워크) chi phí (cost / 비용), không tối ưu distance từ một nguồn (source / 소스).


> **Chuyển mạch:** Từ **Minimum Spanning cây (tree / 트리)**, ta sang **Union-Find** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Union-Find

Disjoint Set Union quản lý partition thành components với `find` và `union`. đường dẫn (path / 경로) compression + union by rank/kích thước (size / 크기) cho amortized gần constant, chính xác hơn là inverse-Ackermann.

Nó minh họa cấu trúc dữ liệu (data structure / 자료구조) được thiết kế quanh một rất nhỏ thao tác (operation / 연산) set nhưng cực hiệu quả cho connectivity.


> **Chuyển mạch:** Từ **Union-Find**, ta sang **đồ thị (graph / 그래프) ở software các hệ thống (systems / 시스템들)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Đồ thị (graph / 그래프) ở software các hệ thống (systems / 시스템들)

Gói (package / 패키지) dependencies, services, quyền sở hữu (ownership / 소유권) và dữ liệu (data / 데이터) lineage là graphs. “Microservices kiến trúc (architecture / 아키텍처)” không chỉ là danh sách (list / 목록) services; tương tác (interaction / 상호작용) đồ thị (graph / 그래프) quyết định coupling, thất bại (failure / 실패) propagation và deploy coordination.

Garbage collector tracing đối tượng (object / 객체) đồ thị (graph / 그래프) từ roots để xác định reachability. Git lần ghi nhận (commit / 커밋) lịch sử (history / 이력) là DAG. Web pages + links tạo directed đồ thị (graph / 그래프).


> **Chuyển mạch:** Từ **đồ thị (graph / 그래프) ở software các hệ thống (systems / 시스템들)**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Khi entities có **many-to-many relationships**, nghĩ bằng đồ thị (graph / 그래프). Sau đó hỏi: directed hay undirected, weighted hay unweighted, sparse hay dense, và thao tác (operation / 연산) chính là reachability, shortest đường dẫn (path / 경로), thứ tự (ordering / 순서), connectivity hay luồng (flow / 흐름)?


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“cây (tree / 트리) và đồ thị (graph / 그래프) là hai thứ tách biệt.”** cây (tree / 트리) là đồ thị (graph / 그래프) connected acyclic với cấu trúc (structure / 구조) đặc biệt.

**“BFS luôn nhanh hơn DFS.”** Cả hai O(V+E) trong adjacency-list mô hình (model / 모델); bộ nhớ (memory / 메모리) và traversal hành vi (behavior / 동작) khác.

**“Dijkstra dùng được với negative weight nếu không có negative cycle.”** bất biến (invariant / 불변식) greedy của Dijkstra vẫn có thể sai với negative edge; dùng thuật toán (algorithm / 알고리즘) phù hợp.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Đồ thị (graph / 그래프) algorithms dùng [linear structures](./03_linear_data_structures.md) và [heap](./05_trees_heaps_and_search_structures.md). phụ thuộc (dependency / 의존성) graphs xuất hiện trong [build/package systems](../08_software_systems/01_version_control_build_link_and_packages.md), routing trong [networking](../06_networks_distributed_systems/01_ethernet_ip_subnetting_and_routing.md), wait-for đồ thị (graph / 그래프) trong [deadlock](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 algorithmic thinking and correctness](./00_algorithmic_thinking_and_correctness.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
