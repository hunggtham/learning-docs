# Trường hợp (case / 사례) Study: Hệ thống định tuyến từ góc nhìn đồ thị

> **Mạch đọc:** Đọc **trường hợp (case / 사례) Study: Hệ thống định tuyến từ góc nhìn đồ thị** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Mô hình đồ thị** sang **2. Adjacency danh sách (list / 목록) hay ma trận (matrix / 행렬)?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

**Routing hệ thống (system / 시스템) trường hợp (case / 사례) Study / 라우팅 시스템 설계 사례**

Một hệ thống định tuyến không chỉ cần “chạy Dijkstra”. Nó phải mô hình hóa topology, cập nhật thay đổi, tính đường đi, xử lý tie-break, bảo đảm hội tụ, giới hạn trạng thái (state / 상태) và đôi khi phải phản ứng với lỗi trong vài mili giây. DSA cung cấp các thành phần nguyên thủy (primitive / 기본 요소) quan trọng, nhưng thiết kế thật là sự kết hợp giữa biểu diễn đồ thị, shortest đường dẫn (path / 경로), priority hàng đợi (queue / 큐), incremental cập nhật (update / 업데이트) và bộ nhớ đệm (cache / 캐시).

## 1. Mô hình đồ thị

Mạng có thể được biểu diễn:

```text
router / switch / location -> đỉnh
link                        -> cạnh
latency / cost / hop        -> trọng số
```

Điều đầu tiên cần xác định là cạnh có hướng hay vô hướng, trọng số có âm không, có nhiều cạnh song song hay không và topology có thay đổi theo thời gian không.

Nếu link hai chiều có chi phí khác nhau theo từng hướng, mô hình đúng là hai cạnh có hướng chứ không phải một cạnh vô hướng.

## 2. Adjacency danh sách (list / 목록) hay ma trận (matrix / 행렬)?

Mạng thực thường thưa: mỗi router chỉ nối trực tiếp một phần nhỏ tổng số router. Vì vậy danh sách kề thường có bộ nhớ:

\[
O(V+E)
\]

và duyệt cạnh hiệu quả hơn ma trận `O(V^2)`.

Nếu cần kiểm tra adjacency cực thường xuyên trên đồ thị nhỏ/dày, ma trận (matrix / 행렬) có thể hợp lý. biểu diễn (representation / 표현) phải theo tải công việc (workload / 워크로드).

## 3. Dijkstra và bất biến (invariant / 불변식)

Với trọng số không âm, Dijkstra duy trì:

```text
dist[v] = khoảng cách tốt nhất đã biết
```

Khi một đỉnh `u` được lấy ra với khoảng cách nhỏ nhất còn hợp lệ, khoảng cách đó trở thành tối ưu cuối cùng.

Lý do là mọi đường đi khác chưa xét phải đi qua các đỉnh có khoảng cách ít nhất bằng `dist[u]`; với cạnh không âm, chúng không thể tạo đường tới `u` ngắn hơn giá trị hiện tại.

Priority hàng đợi (queue / 큐) giúp chọn frontier nhỏ nhất nhanh hơn quét toàn bộ đỉnh.

## 4. Lazy Priority hàng đợi (queue / 큐)

Nhiều vùng nhớ động (heap / 힙) chuẩn không có decrease-key tiện dụng. Ta có thể chèn trạng thái mới:

```text
(newDist, node)
```

và khi pop:

```text
nếu d != dist[node] -> bỏ qua entry cũ
```

Đây là một ví dụ dùng thêm bộ nhớ để đổi lấy hiện thực (implementation / 구현) đơn giản và robust.

## 5. Tie-break không chỉ là chi tiết

Hai đường đi có cùng chi phí (cost / 비용) có thể cần tie-break theo:

```text
ít hop hơn
đường ổn định hơn
ID nhỏ hơn
policy cụ thể
```

Nếu tie-break là một phần của đầu ra (output / 출력) đặc tả hợp đồng (contract / 계약), comparator/trạng thái (state / 상태) phải phản ánh nó. Chỉ so `distance` có thể trả lời đúng về chi phí (cost / 비용) nhưng sai về ngữ nghĩa (semantics / 의미론) của sản phẩm.

## 6. Nếu trọng số có thể âm?

Dijkstra không còn hợp lệ. Khi đó có thể cần Bellman–Ford hoặc mô hình khác.

Trong routing thực, chỉ số (metric / 지표) thường được thiết kế không âm chính vì muốn giữ các tính chất tốt của shortest-path khung phần mềm (framework / 프레임워크).

Đây là ví dụ lĩnh vực (domain / 도메인) ràng buộc (constraint / 제약조건) được chọn để làm thuật toán dễ và đáng tin cậy hơn.

## 7. All-pairs hay single-source?

Nếu một router cần đường tới mọi đích, chạy single-source shortest đường dẫn (path / 경로) từ router đó là tự nhiên. Nếu hệ thống trung tâm cần mọi cặp trên đồ thị (graph / 그래프) nhỏ, Floyd–Warshall có thể hợp lý.

Nếu đồ thị (graph / 그래프) lớn và sparse, chạy Dijkstra từ nhiều nguồn có thể tốt hơn `O(V^3)`.

Cần chọn thuật toán theo số nguồn truy vấn chứ không chỉ theo `V` và `E`.

## 8. động (dynamic / 동적) topology

Khi một link đổi chi phí (cost / 비용) hoặc down/up, chạy lại toàn bộ shortest đường dẫn (path / 경로) là baseline đơn giản và đúng.

Nếu cập nhật (update / 업데이트) rất thường xuyên và đồ thị (graph / 그래프) lớn, incremental shortest-path algorithms có thể tái sử dụng trạng thái (state / 상태) cũ. Nhưng độ phức tạp (complexity / 복잡도) và tính đúng đắn (correctness / 정확성) khó hơn nhiều.

Nguyên tắc thực dụng:

```text
update hiếm -> recompute đơn giản
update dày -> cân nhắc incremental/dynamic algorithm
```

## 9. Link-state mô hình (model / 모델)

Trong mô hình link-state, mỗi router có topology tương đối đầy đủ rồi tự chạy shortest-path cây (tree / 트리).

Chuỗi xử lý (pipeline / 파이프라인) khái niệm:

```text
link event
  ↓
flood topology update
  ↓
local graph update
  ↓
shortest-path recomputation
  ↓
routing table
```

DSA nằm ở đồ thị (graph / 그래프) lưu trữ (storage / 저장소) và shortest đường dẫn (path / 경로); phân tán (distributed / 분산) giao thức (protocol / 프로토콜) chịu trách nhiệm dissemination và convergence.

## 10. Distance-vector mô hình (model / 모델)

Distance-vector gần với repeated relaxation kiểu Bellman–Ford:

```text
router trao đổi estimate với hàng xóm
router cập nhật khoảng cách tốt hơn
```

Thông tin phân tán nên router không có toàn đồ thị (graph / 그래프). Đổi lại, hệ thống có các vấn đề hội tụ như count-to-infinity.

Hai kiến trúc dùng các thành phần nguyên thủy (primitive / 기본 요소) thuật toán khác nhau vì trạng thái (state / 상태) được phân phối khác nhau.

## 11. Longest Prefix Match trong mặt phẳng dữ liệu (data plane / 데이터 플레인)

Sau khi điều khiển (control / 제어) plane tính tuyến (route / 경로), mặt phẳng dữ liệu (data plane / 데이터 플레인) phải map địa chỉ đích tới next hop.

Đây không còn là shortest-path truy vấn (query / 쿼리) mà là **longest prefix match**.

Trie/Patricia/Radix cây (tree / 트리) phù hợp vì các tuyến (route / 경로) được định nghĩa theo prefix bit:

```text
10.0.0.0/8
10.10.0.0/16
10.10.5.0/24
```

Đích `10.10.5.7` phải chọn prefix dài nhất `/24`.

Một hệ thống routing vì vậy kết hợp đồ thị (graph / 그래프) + Trie, chứ không chỉ một cấu trúc.

## 12. ECMP và nhiều đường bằng nhau

Nếu có nhiều đường cùng chi phí (cost / 비용), hệ thống có thể dùng **Equal-Cost Multi-Path (ECMP)** để chia lưu lượng.

Routing bảng (table / 테이블) khi đó có thể lưu một tập next-hop thay vì một next-hop duy nhất.

Băm (hash / 해시) luồng (flow / 흐름) key tới next-hop giúp một luồng (flow / 흐름) giữ ổn định đường đi trong khi phân phối nhiều luồng (flow / 흐름) qua nhiều đường.

Hashing trở thành một phần của routing mặt phẳng dữ liệu (data plane / 데이터 플레인).

## 13. thất bại (failure / 실패) và rerouting

Nếu link chính hỏng, recompute toàn cục (global / 전역) tuyến (route / 경로) có thể mất thời gian. Một số hệ thống duy trì backup next-hop hoặc fast-reroute trạng thái (state / 상태).

Đây là dạng precomputation:

```text
trả thêm bộ nhớ/update cost trước
→ giảm latency khi failure xảy ra
```

Giống nhiều cấu trúc DSA khác, hệ thống materialize thông tin phục vụ một tình huống quan trọng.

## 14. K-shortest paths

Nếu cần nhiều tuyến (route / 경로) dự phòng hoặc candidate routes, shortest đường dẫn (path / 경로) duy nhất không đủ.

Các bài toán k-shortest paths như Yen/Eppstein mở rộng không gian kết quả. độ phức tạp (complexity / 복잡도) tăng đáng kể, vì đầu ra (output / 출력) bản thân có kích thước `k`.

Không nên kỳ vọng giữ cùng chi phí với single shortest đường dẫn (path / 경로) khi yêu cầu đầu ra (output / 출력) mạnh hơn.

## 15. Constrained routing

Một tuyến (route / 경로) có thể phải thỏa đồng thời:

```text
latency <= L
bandwidth >= B
không đi qua khu vực X
hop <= H
```

Nhiều ràng buộc làm bài toán khó hơn shortest đường dẫn (path / 경로) chuẩn và có thể dẫn tới multi-criteria tối ưu hóa (optimization / 최적화) hoặc NP-hard variants.

Đây là nơi phải nhận ra giới hạn của thành phần nguyên thủy (primitive / 기본 요소) cổ điển thay vì cố ép mọi yêu cầu (requirement / 요구사항) vào Dijkstra.

## 16. A* khi có heuristic

Trong không gian địa lý, nếu có heuristic admissible như khoảng cách đường thẳng, A* có thể giảm số trạng thái (state / 상태) phải mở rộng so với Dijkstra.

A* dùng:

\[
f(v)=g(v)+h(v)
\]

với `g` là chi phí (cost / 비용) đã biết và `h` là ước lượng phần còn lại.

Nếu heuristic không vượt chi phí (cost / 비용) thật, A* giữ tính tối ưu trong mô hình chuẩn.

Đây là ví dụ thêm lĩnh vực (domain / 도메인) kiến thức (knowledge / 지식) để giảm tìm kiếm (search / 검색) không gian (space / 공간).

## 17. Bidirectional tìm kiếm (search / 검색)

Nếu chỉ cần tuyến (route / 경로) giữa một cặp nguồn–đích trên đồ thị (graph / 그래프) lớn, tìm kiếm hai chiều có thể giảm vùng duyệt:

```text
forward từ source
backward từ target
```

Nhưng điều kiện dừng và cách ghép chi phí (cost / 비용) phải được chứng minh cẩn thận, đặc biệt với Dijkstra hai chiều.

## 18. bộ nhớ đệm (cache / 캐시) tuyến (route / 경로)

Nếu nhiều truy vấn (query / 쿼리) lặp lại cùng nguồn (source / 소스)/destination, có thể bộ nhớ đệm (cache / 캐시) kết quả. Nhưng topology cập nhật (update / 업데이트) làm bộ nhớ đệm (cache / 캐시) stale.

Cần sự đánh đổi (trade-off / 트레이드오프):

```text
cache hit nhanh
vs
invalidation complexity
```

Có thể phiên bản (version / 버전) topology; bộ nhớ đệm (cache / 캐시) entry chỉ hợp lệ nếu phiên bản (version / 버전) phù hợp.

## 19. Incremental vô hiệu hóa (invalidation / 무효화)

Khi một cạnh thay đổi, không phải mọi cached tuyến (route / 경로) đều bị ảnh hưởng. Nếu lưu phụ thuộc (dependency / 의존성) tuyến (route / 경로) → edge, có thể invalidate có chọn lọc.

Nhưng siêu dữ liệu (metadata / 메타데이터) phụ thuộc (dependency / 의존성) có thể rất lớn. Đây là ví dụ hệ thống đổi thêm trạng thái (state / 상태) để giảm phạm vi recomputation.

## 20. độ phức tạp (complexity / 복잡도) mô hình (model / 모델) thực tế

Dijkstra với nhị phân (binary / 이진) vùng nhớ động (heap / 힙):

\[
O((V+E)\log V)
\]

Nhưng độ trễ (latency / 지연 시간) thực còn phụ thuộc:

```text
cache locality của adjacency
allocation của heap entries
số stale entries
branch prediction
độ dài key/policy comparator
```

Trong đồ thị (graph / 그래프) cực lớn, bố trí CSR có thể nhanh hơn đồ thị (graph / 그래프) object-heavy dù cùng Big-O.

## 21. CSR và đồ thị (graph / 그래프) tĩnh

Nếu topology ít thay đổi, CSR:

```text
offsets[]
edges[]
weights[]
```

cho bộ nhớ gọn và locality tốt.

Nếu edge cập nhật (update / 업데이트) nhiều, adjacency danh sách (list / 목록) động dễ cập nhật hơn.

Static/động (dynamic / 동적) tải công việc (workload / 워크로드) lại quyết định biểu diễn (representation / 표현).

## 22. Testing

Có thể differential-test Dijkstra trên đồ thị (graph / 그래프) nhỏ với Floyd–Warshall.

Các trường hợp cần thử:

```text
đồ thị rời rạc
nhiều shortest paths bằng nhau
zero-weight edge
parallel edge
topology thay đổi
source == target
đỉnh không reachable
```

Bất biến (invariant / 불변식) cần kiểm tra:

```text
mọi next-hop dẫn tới đường hợp lệ
sum weight đúng dist
dist không vi phạm triangle inequality trên edge đã relax hoàn tất
```

## 23. Benchmark

Phải thay đổi:

```text
V, E
độ thưa/dày
weight distribution
update frequency
query locality
cache hit ratio
source distribution
```

Đồ thị (graph / 그래프) ngẫu nhiên đồng đều không đại diện topology thật, vốn thường có hub và cấu trúc phân cấp.

## 24. chuỗi xử lý (pipeline / 파이프라인) hệ thống

```text
Topology events
    ↓
Graph state
    ↓
Shortest-path computation
    ↓
Routing Information Base
    ↓
Prefix/radix structure
    ↓
Forwarding table
    ↓
Hash/ECMP next-hop selection
```

Mỗi tầng dùng một cấu trúc khác vì câu hỏi khác nhau.

## Mô hình tư duy

> Một hệ thống routing là sự kết hợp giữa **đồ thị (graph / 그래프) lập luận (reasoning / 추론) ở điều khiển (control / 제어) plane** và **prefix/băm (hash / 해시) lookup ở mặt phẳng dữ liệu (data plane / 데이터 플레인)**. Dijkstra giải một thành phần nguyên thủy (primitive / 기본 요소) quan trọng, nhưng thiết kế thật còn cần biểu diễn (representation / 표현), cập nhật (update / 업데이트) chiến lược (strategy / 전략), tie-break, failover, bộ nhớ đệm (cache / 캐시) và consistency.

Xem thêm: [Graph Modeling](../03_graphs/00_graph_modeling_and_representation.md), [Shortest Paths](../03_graphs/02_shortest_paths.md), [Priority Queues](../01_linear_structures/03_queues_deques_and_priority_queues.md), [Trie](../02_trees/04_tries.md), [Hash Tables](../01_linear_structures/04_hash_tables.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 choose the right data structure](./00_choose_the_right_data_structure.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
