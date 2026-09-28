# Lý thuyết đồ thị: toán học của quan hệ, đường đi và cấu trúc mạng

> **Mạch đọc:** Đọc **Lý thuyết đồ thị: toán học của quan hệ, đường đi và cấu trúc mạng** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **đồ thị (graph / 그래프) bắt đầu từ lớp trừu tượng (abstraction / 추상화) nào?** sang **Simple đồ thị (graph / 그래프), multigraph và self-loop**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Lý thuyết đồ thị (Graph Theory / 그래프 이론) nghiên cứu những các hệ thống (systems / 시스템들) mà điều quan trọng không phải tọa độ tuyệt đối của objects, mà là **objects nào được nối với objects nào**. Khi ta quan tâm đến phụ thuộc (dependency / 의존성), reachability, tuyến (route / 경로), hierarchy, cycle, neighborhood hoặc connectivity, đồ thị (graph / 그래프) thường là lớp trừu tượng (abstraction / 추상화) tự nhiên nhất.

Một road mạng (network / 네트워크), xã hội (social / 사회적) mạng (network / 네트워크), gói (package / 패키지) phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), workflow, finite-state machine, cơ sở dữ liệu (database / 데이터베이스) relationship mạng (network / 네트워크) hay kiến thức (knowledge / 지식) đồ thị (graph / 그래프) đều có thể rất khác nhau về lĩnh vực (domain / 도메인), nhưng cùng chia sẻ một cấu trúc (structure / 구조): nodes và relationships.

> đồ thị (graph / 그래프) bỏ bớt hình học (geometry / 기하학) để giữ lại topology của quan hệ: ai nối với ai, đi từ đâu tới đâu, và những paths/cycles nào tồn tại.

## Đồ thị (graph / 그래프) bắt đầu từ lớp trừu tượng (abstraction / 추상화) nào?

Một đồ thị (graph / 그래프) thường được viết

```math
G=(V,E),
```

trong đó `V` là set các vertices/nodes và `E` là set các edges.

Nếu đồ thị (graph / 그래프) vô hướng (Undirected Graph / 무방향 그래프), edge giữa `u` và `v` có thể viết `{u,v}`. quan hệ (relation / 관계) “friendship” thường gần kiểu này: nếu A là bạn của B thì B cũng là bạn của A.

Nếu đồ thị (graph / 그래프) có hướng (Directed Graph / 방향 그래프), edge `(u,v)` đi từ `u` sang `v`. “A follows B” hoặc “mô-đun (module / 모듈) A depends on B” là directed quan hệ (relation / 관계).

Đồ thị (graph / 그래프) mô hình (model / 모델) không tự nói nút (node / 노드) hoặc edge “thật sự là gì”. Ta quyết định ngữ nghĩa (semantics / 의미론) theo bài toán (problem / 문제). Đây là sức mạnh của lớp trừu tượng (abstraction / 추상화) nhưng cũng là nguồn rủi ro: nếu edge definition không đúng nghiệp vụ (business / 비즈니스)/vật lý (physical / 물리적) meaning, thuật toán (algorithm / 알고리즘) đúng trên đồ thị (graph / 그래프) vẫn có thể trả lời sai question thực tế.

## Simple đồ thị (graph / 그래프), multigraph và self-loop

Trong simple undirected đồ thị (graph / 그래프), thường không có multiple edges giữa cùng pair và không có self-loop. Nhưng nhiều các hệ thống (systems / 시스템들) cần richer mô hình (model / 모델).

Một airline mạng (network / 네트워크) có thể có nhiều flights giữa cùng hai airports, nên multigraph hợp lý. máy trạng thái (state machine / 상태 머신) có thể có self-loop khi trạng thái (state / 상태) chuyển về chính nó. mạng (network / 네트워크) luồng (flow / 흐름) có directed edges với capacities.

Trước khi dùng theorem hoặc thuật toán (algorithm / 알고리즘), cần biết đồ thị (graph / 그래프) mô hình (model / 모델) cho phép gì. Một thuộc tính (property / 속성) đúng cho simple đồ thị (graph / 그래프) có thể không translate nguyên xi sang multigraph.

## Degree: cục bộ (local / 로컬) connectivity của một nút (node / 노드)

Trong undirected đồ thị (graph / 그래프), degree `deg(v)` là số sự cố (incident / 인시던트) edges tại vertex `v`.

Một định danh (identity / 식별자) cơ bản là Handshake Lemma:

```math
\sum_{v\in V}\deg(v)=2|E|.
```

Lý do không nằm ở algebra phức tạp: mỗi edge có hai endpoints, nên khi cộng degree của mọi vertices, mỗi edge được count đúng hai lần.

Một consequence là số vertices có odd degree luôn even. Vì tổng degree là số chẵn, tổng của một odd number lượng odd không thể tạo số chẵn.

Trong directed đồ thị (graph / 그래프), ta phân biệt in-degree và out-degree. Tổng in-degree bằng tổng out-degree và đều bằng số directed edges:

```math
\sum_v \deg^-(v)=\sum_v\deg^+(v)=|E|.
```

## Walk, trail, đường dẫn (path / 경로) và cycle

Trong informal discussion, mọi chuỗi (sequence / 시퀀스) nodes connected bởi edges thường được gọi “đường dẫn (path / 경로)”, nhưng đồ thị (graph / 그래프) lý thuyết (theory / 이론) phân biệt kỹ hơn.

Một walk có thể lặp vertices và edges. Trail không lặp edges. Simple đường dẫn (path / 경로) không lặp vertices. Cycle là closed đường dẫn (path / 경로) trở về điểm bắt đầu mà không lặp intermediate vertices theo tiêu chuẩn (standard / 표준) simple definition.

Distinctions này quan trọng khi nói về Euler đường dẫn (path / 경로), Hamiltonian đường dẫn (path / 경로), shortest đường dẫn (path / 경로) hoặc cycle detection.

## Connectivity: có đi tới được không?

Undirected đồ thị (graph / 그래프) connected nếu mọi pair vertices có đường dẫn (path / 경로) nối chúng. Nếu không, đồ thị (graph / 그래프) chia thành connected components.

Trong directed đồ thị (graph / 그래프), có hai notions quan trọng:

- strongly connected: từ mọi vertex đi tới mọi vertex khác theo direction;
- weakly connected: nếu bỏ direction, underlying undirected đồ thị (graph / 그래프) connected.

Trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들) hoặc microservice phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), “có đường dẫn (path / 경로)” không đồng nghĩa “yêu cầu (request / 요청) chắc chắn thành công”. đồ thị (graph / 그래프) connectivity chỉ nói cấu trúc (structure / 구조) cho phép tuyến (route / 경로) tồn tại trong mô hình (model / 모델); độ trễ (latency / 지연 시간), sức chứa (capacity / 용량), authorization và failures là properties khác.

## Trees: connectivity tối thiểu không có cycle

Một cây (tree / 트리) là connected undirected đồ thị (graph / 그래프) không có cycles.

Với `n` vertices, cây (tree / 트리) có

```math
|E|=n-1.
```

Có nhiều cách hiểu thuộc tính (property / 속성) này. Một cây (tree / 트리) connected nhưng “just connected enough”: remove bất kỳ edge nào thì đồ thị (graph / 그래프) disconnect; add một edge mới giữa hai existing vertices thì tạo đúng một cycle.

Đó là lý do cây (tree / 트리) là cấu trúc (structure / 구조) tự nhiên cho hierarchy. Mỗi child có tuyến (route / 경로) unique tới gốc (root / 루트) nếu ta orient edges theo parent-child quan hệ (relation / 관계).

Tệp (file / 파일) các hệ thống (systems / 시스템들), DOM, cú pháp (syntax / 문법) trees và many indexes dùng cây (tree / 트리). Nhưng Git lần ghi nhận (commit / 커밋) lịch sử (history / 이력) nói chung là DAG chứ không strict cây (tree / 트리) vì merge lần ghi nhận (commit / 커밋) có thể có nhiều parents.

## Spanning cây (tree / 트리): giữ connectivity, bỏ redundancy cycles

Cho connected đồ thị (graph / 그래프) `G`, spanning cây (tree / 트리) chứa tất cả vertices nhưng chỉ giữ subset edges đủ để đồ thị (graph / 그래프) vẫn connected và acyclic.

Mọi spanning cây (tree / 트리) với `n` vertices có `n-1` edges.

Trong mạng (network / 네트워크) thiết kế (design / 설계), nếu goal chỉ là maintain connectivity với minimum number edges, spanning cây (tree / 트리) là natural đối tượng (object / 객체). Nhưng nếu edges có costs, ta cần minimum spanning cây (tree / 트리).

## Minimum spanning cây (tree / 트리)

Cho weighted undirected đồ thị (graph / 그래프), minimum spanning cây (tree / 트리) (MST) tìm spanning cây (tree / 트리) với total edge weight nhỏ nhất.

Kruskal's thuật toán (algorithm / 알고리즘) sort edges theo weight và thêm edge nếu không tạo cycle. Prim's thuật toán (algorithm / 알고리즘) grow một connected cây (tree / 트리) bằng cheapest edge crossing từ visited sang unvisited side.

Điểm cốt lõi là **cut thuộc tính (property / 속성)**: với một cut của vertices thành hai groups, lightest edge crossing cut có thể là safe choice dưới conditions chuẩn. Đây là structural reason greedy algorithms đúng, không chỉ là “chọn edge nhỏ nhất vì nghe hợp lý”.

MST không giải shortest paths giữa một nguồn (source / 소스) và mọi nodes. Hai problems khác nhau: MST minimize total cây (tree / 트리) chi phí (cost / 비용); shortest-path cây (tree / 트리) minimize source-to-node distances.

## Directed acyclic đồ thị (graph / 그래프) và phụ thuộc (dependency / 의존성)

DAG (Directed Acyclic Graph / 방향 비순환 그래프) là directed đồ thị (graph / 그래프) không có directed cycles.

Dependencies thường muốn DAG cấu trúc (structure / 구조) vì cycle có thể làm “phải hoàn thành A trước B, B trước C, C trước A” trở thành impossible thứ tự (ordering / 순서).

Topological thứ tự (ordering / 순서) là chuỗi (sequence / 시퀀스) vertices sao cho mọi edge

```math
u\to v
```

đặt `u` trước `v`.

Topological thứ tự (order / 순서) tồn tại **iff** directed đồ thị (graph / 그래프) là DAG.

Bản dựng (build / 빌드) các hệ thống (systems / 시스템들), gói (package / 패키지) resolution, course prerequisites và workflow scheduling đều dùng idea này. Nhiều valid topological orders có thể tồn tại; thuật toán (algorithm / 알고리즘) không nhất thiết trả unique thứ tự (ordering / 순서).

## Đồ thị (graph / 그래프) biểu diễn (representation / 표현): adjacency danh sách (list / 목록) và adjacency ma trận (matrix / 행렬)

Mathematical đồ thị (graph / 그래프) là abstract đối tượng (object / 객체). Software phải chọn biểu diễn (representation / 표현).

Adjacency ma trận (matrix / 행렬) `A` với `n` vertices dùng roughly

```math
O(n^2)
```

Không gian (space / 공간). Edge lookup `A_{ij}` thường `O(1)`.

Adjacency danh sách (list / 목록) lưu neighbors cho từng vertex. Với sparse đồ thị (graph / 그래프), không gian (space / 공간) roughly

```math
O(|V|+|E|).
```

Iteration qua neighbors hiệu quả hơn nhiều.

Choice phụ thuộc đồ thị (graph / 그래프) density và operations. Dense linear-algebra workloads có thể thích ma trận (matrix / 행렬) biểu diễn (representation / 표현); large sparse networks thường dùng adjacency lists hoặc compressed sparse formats.

Biểu diễn (representation / 표현) là kỹ thuật (engineering / 엔지니어링) quyết định (decision / 결정), không phải graph-theory definition.

## BFS: shortest number of edges bằng tầng (layer / 계층) expansion

Breadth-First tìm kiếm (search / 검색) bắt đầu từ nguồn (source / 소스) và khám phá đồ thị (graph / 그래프) theo layers.

Tầng (layer / 계층) 0 là nguồn (source / 소스). tầng (layer / 계층) 1 gồm neighbors trực tiếp. tầng (layer / 계층) 2 gồm unvisited nodes reachable qua hai edges, và tiếp tục như vậy.

Vì toàn bộ nodes ở distance `d` được discover trước nodes ở distance `d+1`, BFS tìm shortest đường dẫn (path / 경로) theo **number of edges** trong unweighted đồ thị (graph / 그래프).

Với adjacency danh sách (list / 목록), độ phức tạp (complexity / 복잡도) là

```math
O(|V|+|E|),
```

vì mỗi vertex được visited bounded number times và adjacency entries được scan bounded number times.

### Vì sao BFS không trực tiếp đúng cho weighted đồ thị (graph / 그래프)?

BFS coi mọi edge có same chi phí (cost / 비용). Nếu một direct edge chi phí (cost / 비용) 100 nhưng tuyến (route / 경로) qua ba edges chi phí (cost / 비용) 1+1+1=3, “fewer edges” không còn đồng nghĩa “shorter chi phí (cost / 비용)”. Khi weights khác nhau, cần thuật toán (algorithm / 알고리즘) phù hợp như Dijkstra hoặc Bellman–Ford.

## DFS: đi sâu để lộ cấu trúc (structure / 구조)

Depth-First tìm kiếm (search / 검색) đi sâu theo một branch cho tới khi không còn unvisited neighbor rồi backtrack.

DFS tạo discovery/finish cấu trúc (structure / 구조) hữu ích cho:

- connected components;
- cycle detection;
- topological sorting;
- articulation-like lập luận (reasoning / 추론);
- strongly connected thành phần (component / 컴포넌트) algorithms.

Recursive hiện thực (implementation / 구현) tự nhiên nhưng deep đồ thị (graph / 그래프) có thể vượt call-stack limit. tường minh (explicit / 명시적) ngăn xếp (stack / 스택) thường an toàn hơn trong môi trường vận hành (production / 운영 환경) các hệ thống (systems / 시스템들).

## Dijkstra: shortest đường dẫn (path / 경로) khi weights nonnegative

Dijkstra's thuật toán (algorithm / 알고리즘) duy trì tentative distance từ nguồn (source / 소스). Mỗi bước chọn unsettled vertex có tentative distance nhỏ nhất và “settle” nó.

Tại sao greedy step đúng? Với nonnegative edge weights, bất kỳ alternate đường dẫn (path / 경로) đi qua một unsettled vertex khác phải có chi phí (cost / 비용) ít nhất bằng hiện tại (current / 현재) smallest tentative distance trước khi cộng thêm nonnegative chi phí (cost / 비용). Vì vậy settled distance không thể được cải thiện sau đó.

Cốt lõi (core / 핵심) relaxation thao tác (operation / 연산) là:

```math
\text{if }d[u]+w(u,v)<d[v],\text{ then update }d[v].
```

Với priority hàng đợi (queue / 큐), dùng chung (common / 공통) độ phức tạp (complexity / 복잡도) là approximately

```math
O((|V|+|E|)\log|V|)
```

cho tiêu chuẩn (standard / 표준) sparse hiện thực (implementation / 구현).

### Tại sao negative weight phá Dijkstra?

Nếu negative edge tồn tại, một vertex đã settle có thể về sau nhận tuyến (route / 경로) rẻ hơn thông qua negative edge. Greedy bất biến (invariant / 불변식) bị phá.

Bellman–Ford relax mọi edges repeatedly và xử lý negative weights, đồng thời detect negative cycles reachable từ nguồn (source / 소스).

Negative cycle nghĩa shortest đường dẫn (path / 경로) có thể không finite: đi vòng cycle mỗi lần làm chi phí (cost / 비용) giảm thêm.

## Floyd–Warshall và all-pairs shortest paths

Nếu cần shortest đường dẫn (path / 경로) giữa mọi pair vertices trong dense đồ thị (graph / 그래프) nhỏ/vừa, Floyd–Warshall dùng động (dynamic / 동적) programming:

```math
D_{ij}^{(k)}=
\min\left(D_{ij}^{(k-1)},D_{ik}^{(k-1)}+D_{kj}^{(k-1)}\right).
```

Interpretation: shortest đường dẫn (path / 경로) từ `i` đến `j` khi cho phép intermediate vertices trong set đầu `k` nodes hoặc không dùng `k`, hoặc đi qua `k`.

Độ phức tạp (complexity / 복잡도)

```math
O(|V|^3)
```

không phù hợp huge sparse graphs nhưng rất elegant cho dense all-pairs problems.

## Strongly connected components

Trong directed đồ thị (graph / 그래프), strongly connected thành phần (component / 컴포넌트) (SCC) là maximal set vertices mà mọi pair reach each other.

Nếu collapse mỗi SCC thành một super-node, condensation đồ thị (graph / 그래프) luôn là DAG. Đây là deep structural fact: mọi directed đồ thị (graph / 그래프) có thể được nhìn như DAG của strongly connected regions.

Trình biên dịch (compiler / 컴파일러) phân tích (analysis / 분석), phụ thuộc (dependency / 의존성) diagnostics và state-transition các hệ thống (systems / 시스템들) dùng SCC để tìm mutually recursive/dependent groups.

## Bipartite đồ thị (graph / 그래프) và matching

Đồ thị (graph / 그래프) bipartite nếu vertices chia được thành hai sets `L,R` sao cho edges chỉ nối giữa hai sets.

Equivalent structural thuộc tính (property / 속성): undirected đồ thị (graph / 그래프) bipartite iff không có odd cycle.

Bipartite matching mô hình (model / 모델) assignment problems như workers ↔ tasks, students ↔ projects, applicants ↔ positions.

Maximum matching tìm largest set edges không share endpoints. Weighted versions dẫn tới assignment tối ưu hóa (optimization / 최적화).

Đây là ví dụ đồ thị (graph / 그래프) lý thuyết (theory / 이론) chuyển trực tiếp thành operations research.

## Đồ thị (graph / 그래프) coloring: xung đột (conflict / 충돌) dưới dạng adjacency

Vertex coloring gán colors sao cho adjacent vertices khác color.

Nếu edge biểu diễn “hai tasks xung đột (conflict / 충돌)”, coloring partition tasks thành groups không xung đột (conflict / 충돌). Exam scheduling và register allocation có graph-coloring flavor.

Minimum number colors cần gọi chromatic number. General coloring bài toán (problem / 문제) computationally hard; đồ thị (graph / 그래프) cấu trúc (structure / 구조) cụ thể có thể cho efficient algorithms.

Đồ thị (graph / 그래프) lý thuyết (theory / 이론) vì thế không chỉ nói “có đường dẫn (path / 경로) không”, mà còn mô hình (model / 모델) các ràng buộc (constraints / 제약조건들).

## Euler và Hamilton: hai loại “đi qua tất cả” rất khác

Euler đường dẫn (path / 경로)/trail quan tâm đi qua every edge exactly once. Hamiltonian đường dẫn (path / 경로) quan tâm visit every vertex exactly once.

Euler đường dẫn (path / 경로) có characterization cục bộ (local / 로컬) rất đẹp trong undirected connected đồ thị (graph / 그래프): number odd-degree vertices phải là 0 hoặc 2 tùy circuit/đường dẫn (path / 경로) trường hợp (case / 사례).

Hamiltonian đường dẫn (path / 경로) không có criterion đơn giản tương tự và liên quan computationally difficult problems.

Hai concepts trông giống nhưng cấu trúc (structure / 구조) khác hẳn — một warning tốt rằng wording gần nhau không có nghĩa algorithmic difficulty gần nhau.

## Đồ thị (graph / 그래프) matrices và tuyến tính (linear / 선형) algebra

Adjacency ma trận (matrix / 행렬) đưa đồ thị (graph / 그래프) vào tuyến tính (linear / 선형) algebra. Nếu `A` là adjacency ma trận (matrix / 행렬) của unweighted đồ thị (graph / 그래프), entries của

```math
A^k
```

liên quan số walks length `k` giữa vertices.

Đồ thị (graph / 그래프) Laplacian thường định nghĩa

```math
L=D-A,
```

trong đó `D` là degree ma trận (matrix / 행렬).

Eigenvalues/eigenvectors của Laplacian encode connectivity và smooth variation trên đồ thị (graph / 그래프). Spectral clustering, đồ thị (graph / 그래프) tín hiệu (signal / 신호) processing và many mạng (network / 네트워크) methods dựa trên cầu nối (bridge / 브리지) đồ thị (graph / 그래프) lý thuyết (theory / 이론) ↔ tuyến tính (linear / 선형) algebra.

## Random walks và Markov chains trên đồ thị (graph / 그래프)

Nếu từ nút (node / 노드) hiện tại ta chọn next nút (node / 노드) theo chuyển tiếp (transition / 전이) probabilities trên outgoing edges, ta có random walk trên đồ thị (graph / 그래프).

Chuyển tiếp (transition / 전이) ma trận (matrix / 행렬) tạo Markov chuỗi (chain / 사슬). Long-run hành vi (behavior / 동작) liên quan eigenvectors/eigenvalues và stationary distributions.

PageRank có thể nhìn như random walk với teleportation/damping. liên kết (connection / 연결) này cho thấy tìm kiếm (search / 검색) ranking không phải “đồ thị (graph / 그래프) heuristic thuần túy”; nó dựa trên xác suất (probability / 확률) + tuyến tính (linear / 선형) algebra trên đồ thị (graph / 그래프).

## Mạng (network / 네트워크) luồng (flow / 흐름): sức chứa (capacity / 용량) thay đổi question

Trong routing hoặc logistics, việc có đường dẫn (path / 경로) chưa đủ; edges có capacities.

Max-flow bài toán (problem / 문제) hỏi maximum amount có thể gửi từ nguồn (source / 소스) `s` tới sink `t` mà không vượt sức chứa (capacity / 용량) và phải satisfy luồng (flow / 흐름) conservation.

Max-flow min-cut theorem nói maximum luồng (flow / 흐름) giá trị (value / 값) bằng sức chứa (capacity / 용량) của minimum `s-t` cut.

Đây là một theorem mạnh vì nối tối ưu hóa (optimization / 최적화) toàn cục với một structural bottleneck: thông lượng (throughput / 처리량) tối đa bị quyết định bởi weakest separating cut.

## Đồ thị (graph / 그래프) trong kỹ nghệ phần mềm (software engineering / 소프트웨어 공학)

Đồ thị (graph / 그래프) lớp trừu tượng (abstraction / 추상화) xuất hiện ở nhiều tầng (layer / 계층):

Lời gọi (call / 호출) đồ thị (graph / 그래프): nút (node / 노드) là hàm (function / 함수)/phương thức (method / 메서드); edge là lời gọi (call / 호출) quan hệ (relation / 관계).

Phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프): gói (package / 패키지)/mô-đun (module / 모듈) nào phụ thuộc mô-đun (module / 모듈) nào.

Control-flow đồ thị (graph / 그래프): basic blocks và possible thực thi (execution / 실행) transitions.

Trạng thái (state / 상태) đồ thị (graph / 그래프): ứng dụng (application / 애플리케이션)/game/giao thức (protocol / 프로토콜) states và transitions.

Cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마) đồ thị (graph / 그래프): tables/entities và relationships.

Kiến thức (knowledge / 지식) đồ thị (graph / 그래프): entities và typed relations.

Git lần ghi nhận (commit / 커밋) đồ thị (graph / 그래프): commits và parent links tạo DAG trong normal lịch sử (history / 이력).

Cùng algorithms về reachability, cycle detection, topological thứ tự (ordering / 순서), components hoặc shortest paths có thể reuse vì underlying cấu trúc (structure / 구조) giống nhau.

## Modeling matters hơn thuật toán (algorithm / 알고리즘) name

Giả sử tìm “đường tốt nhất” trên road mạng (network / 네트워크). Nếu edge weight là distance, shortest đường dẫn (path / 경로) trả tuyến (route / 경로) ngắn nhất về km. Nếu weight là expected travel thời gian (time / 시간), kết quả (result / 결과) khác. Nếu congestion phụ thuộc thời gian, static weight đồ thị (graph / 그래프) có thể không đủ. Nếu toll + thời gian (time / 시간) là multi-objective, một scalar weight đơn giản có thể che sự đánh đổi (trade-off / 트레이드오프).

Thuật toán (algorithm / 알고리즘) chỉ optimize quantity mà mô hình (model / 모델) đưa vào.

> Một đồ thị (graph / 그래프) thuật toán (algorithm / 알고리즘) đúng không cứu được một đồ thị (graph / 그래프) mô hình (model / 모델) sai.

Đây là first-principles lesson quan trọng khi chuyển đồ thị (graph / 그래프) lý thuyết (theory / 이론) sang kỹ thuật (engineering / 엔지니어링).

## Mô hình tư duy (mental model / 사고 모델)

> đồ thị (graph / 그래프) là toán học của **quan hệ và khả năng đi qua quan hệ**. Vertices là states/entities; edges là allowed relationships/transitions. Paths nói reachability, cycles nói phản hồi (feedback / 피드백)/phụ thuộc (dependency / 의존성) vòng lặp (loop / 루프), components nói regions tách rời, weights/capacities thêm chi phí (cost / 비용) và tài nguyên (resource / 자원) các ràng buộc (constraints / 제약조건들). Trước khi chọn BFS, Dijkstra hay luồng (flow / 흐름) thuật toán (algorithm / 알고리즘), hãy hỏi edge thật sự đại diện điều gì.

## Dùng chung (common / 공통) Misconceptions

**“đồ thị (graph / 그래프) lý thuyết (theory / 이론) đồ thị (graph / 그래프) là chart dữ liệu.”** Không. đồ thị (graph / 그래프) ở đây là mạng (network / 네트워크) cấu trúc (structure / 구조) `G=(V,E)`.

**“BFS luôn tìm shortest đường dẫn (path / 경로).”** Chỉ theo số edges hoặc khi mọi edges có equal chi phí (cost / 비용). Weighted đồ thị (graph / 그래프) cần thuật toán (algorithm / 알고리즘) tương ứng với weight ngữ nghĩa (semantics / 의미론).

**“Dijkstra chỉ cần đồ thị (graph / 그래프) connected.”** Điều kiện quan trọng là edge weights nonnegative cho tiêu chuẩn (standard / 표준) tính đúng đắn (correctness / 정확성) argument.

**“cây (tree / 트리) và DAG giống nhau.”** cây (tree / 트리) là cấu trúc (structure / 구조) chặt hơn. DAG có thể có nút (node / 노드) nhiều parents và nhiều alternative paths; cây (tree / 트리) underlying hierarchy có unique simple đường dẫn (path / 경로) giữa vertices trong undirected sense.

**“MST cho shortest tuyến (route / 경로) từ nguồn (source / 소스).”** MST minimize total cây (tree / 트리) weight, không minimize từng source-to-node distance.

**“Nếu đồ thị (graph / 그래프) connected thì hệ thống (system / 시스템) reliable.”** Connectivity chỉ nói có đường dẫn (path / 경로) trong mô hình (model / 모델) hiện tại. độ tin cậy (reliability / 신뢰성) còn phụ thuộc redundancy, thất bại (failure / 실패) xác suất (probability / 확률), sức chứa (capacity / 용량) và time-dependent conditions.

**“Thêm càng nhiều edges càng tốt.”** Extra edges tăng redundancy nhưng cũng có thể tạo cycles, coupling, attack surface hoặc routing độ phức tạp (complexity / 복잡도). đồ thị (graph / 그래프) thiết kế (design / 설계) luôn có sự đánh đổi (trade-off / 트레이드오프).

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 algorithms complexity and logarithms](./01_algorithms_complexity_and_logarithms.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
