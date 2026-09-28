# Uninformed tìm kiếm (search / 검색): BFS, DFS, UCS và các chiến lược nền tảng

> **Mạch đọc:** Đặt **Uninformed tìm kiếm (search / 검색): BFS, DFS, UCS và các chiến lược nền tảng** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Một lớp trừu tượng (abstraction / 추상화) chung** sang **Breadth-First tìm kiếm (search / 검색)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**Uninformed tìm kiếm (search / 검색)** giải bài toán chỉ bằng bài toán (problem / 문제) definition: initial trạng thái (state / 상태), actions, chuyển tiếp (transition / 전이), goal và đường dẫn (path / 경로) chi phí (cost / 비용). thuật toán (algorithm / 알고리즘) không có domain-specific estimate cho biết trạng thái (state / 상태) nào “gần goal hơn”.

Điều này không làm uninformed tìm kiếm (search / 검색) trở nên lỗi thời. Nó là baseline giúp ta hiểu rõ sự đánh đổi (trade-off / 트레이드오프) giữa completeness, optimality, thời gian (time / 시간) và bộ nhớ (memory / 메모리). Heuristic tìm kiếm (search / 검색) như A* chỉ thực sự dễ hiểu khi ta thấy điều gì xảy ra nếu không có heuristic.

Xem trước: [State Space and Search](./00_state_space_and_search.md).

## Một lớp trừu tượng (abstraction / 추상화) chung

Mọi chiến lược (strategy / 전략) đều có frontier, nhưng khác cách lấy nút (node / 노드):

```text
BFS → queue FIFO
DFS → stack LIFO
UCS → priority queue by g(n)
Depth-limited → DFS + depth bound
Iterative deepening → repeated depth-limited DFS
Bidirectional → two searches meeting
```

Các properties phụ thuộc các giả định (assumptions / 가정들) về branching, goal độ sâu (depth / 깊이) và edge chi phí (cost / 비용).

## Breadth-First tìm kiếm (search / 검색)

Breadth-First tìm kiếm (search / 검색) expand nodes theo độ sâu (depth / 깊이) tăng dần.

Nếu frontier là FIFO hàng đợi (queue / 큐):

```pseudo
queue ← [start]
visited ← {start}

while queue not empty:
    n ← pop_front(queue)
    if goal(n): return path(n)

    for s in successors(n):
        if s not in visited:
            visited.add(s)
            queue.push_back(s)
```

BFS first explores all states độ sâu (depth / 깊이) 0, rồi độ sâu (depth / 깊이) 1, độ sâu (depth / 깊이) 2...

### Khi nào BFS optimal?

Nếu mọi step có cùng chi phí (cost / 비용), shortest độ sâu (depth / 깊이) cũng là lowest đường dẫn (path / 경로) chi phí (cost / 비용). Khi đó BFS optimal.

Nếu edge costs khác nhau, shallowest đường dẫn (path / 경로) có thể đắt hơn đường dẫn (path / 경로) sâu hơn. Lúc đó BFS không guarantee cost-optimal.

### Độ phức tạp (complexity / 복잡도)

Với branching factor `b` và shallowest goal độ sâu (depth / 깊이) `d`, worst-case thời gian (time / 시간)/bộ nhớ (memory / 메모리) thường exponential:

\[
O(b^d)
\]

Bộ nhớ (memory / 메모리) là weakness lớn: BFS phải giữ frontier của whole mức (level / 수준).

### Ví dụ

Đồ thị (graph / 그래프):

```text
S → A → G
 \  
  → B → C → G
```

Nếu edge chi phí (cost / 비용) equal, BFS tìm `S-A-G` trước vì độ sâu (depth / 깊이) nhỏ hơn.

## Depth-First tìm kiếm (search / 검색)

Depth-First tìm kiếm (search / 검색) đi sâu một branch trước khi backtrack.

Ngăn xếp (stack / 스택)/recursion:

```pseudo
stack ← [start]
visited ← set()

while stack not empty:
    n ← pop(stack)
    if n in visited: continue
    visited.add(n)

    if goal(n): return path(n)

    push successors(n)
```

### Strength

DFS bộ nhớ (memory / 메모리) thấp hơn BFS. Nếu maximum độ sâu (depth / 깊이) `m`, rough không gian (space / 공간) độ phức tạp (complexity / 복잡도):

\[
O(bm)
\]

với tiêu chuẩn (standard / 표준) tree-storage lập luận (reasoning / 추론), thay vì exponential frontier theo shallow goal độ sâu (depth / 깊이).

### Weakness

DFS có thể lao sâu vào branch rất dài hoặc infinite nếu không cycle/độ sâu (depth / 깊이) điều khiển (control / 제어).

Nó không optimal. Goal tìm đầu tiên phụ thuộc successor thứ tự (ordering / 순서).

### Khi DFS useful?

- bộ nhớ (memory / 메모리) constrained;
- solution expected deep;
- chỉ cần any solution;
- exhaustive traversal/backtracking;
- topological/cycle-related đồ thị (graph / 그래프) algorithms trong CS broader ngữ cảnh (context / 맥락).

## Depth-Limited tìm kiếm (search / 검색)

Depth-Limited tìm kiếm (search / 검색) (DLS) là DFS với độ sâu (depth / 깊이) limit `ℓ`.

Nếu reached độ sâu (depth / 깊이) `ℓ`, nút (node / 노드) không expand nữa.

Nó tránh infinite descent nhưng có thể miss solution deeper than limit.

Cần phân biệt return states:

```text
SUCCESS
FAILURE    → không có solution trong explored space
CUTOFF     → có thể có solution sâu hơn limit
```

Distinction này quan trọng cho Iterative Deepening.

## Iterative Deepening DFS

Iterative Deepening Depth-First tìm kiếm (search / 검색) (IDDFS) chạy DLS với limits:

```text
0, 1, 2, 3, ...
```

Nó nghe có vẻ wasteful vì expand upper nodes nhiều lần. Nhưng trong exponential cây (tree / 트리), phần lớn nodes nằm ở deepest mức (level / 수준), nên repeated upper-level công việc (work / 작업) relatively small.

Với đơn vị (unit / 단위) costs, IDDFS kết hợp:

- completeness của BFS;
- optimal shallowest-depth hành vi (behavior / 동작) của BFS;
- bộ nhớ (memory / 메모리) profile gần DFS.

Thời gian (time / 시간) vẫn khoảng:

\[
O(b^d)
\]

Không gian (space / 공간) khoảng:

\[
O(bd)
\]

under dùng chung (common / 공통) formulation.

## Uniform-Cost tìm kiếm (search / 검색)

Uniform-Cost tìm kiếm (search / 검색) expand nút (node / 노드) có lowest đường dẫn (path / 경로) chi phí (cost / 비용):

\[
g(n)
\]

Nó là Dijkstra-like tìm kiếm (search / 검색) từ start tới goal trong AI terminology.

Priority hàng đợi (queue / 큐):

```pseudo
frontier ← PQ((0,start))
best[start] ← 0

while frontier:
    g,n ← pop_lowest_cost()

    if g != best[n]: continue
    if goal(n): return path

    for edge(n,s,c):
        new_g ← g + c
        if s unseen OR new_g < best[s]:
            best[s] ← new_g
            push(new_g,s)
```

### Vì sao goal kiểm thử (test / 테스트) thường khi pop, không phải khi generate?

Một goal có thể được generated qua expensive đường dẫn (path / 경로) trước, rồi sau đó có cheaper đường dẫn (path / 경로) chưa explored.

Khi UCS pops goal as lowest-cost frontier nút (node / 노드) under nonnegative costs, ta mới có optimality guarantee.

## BFS là special trường hợp (case / 사례) của UCS

Nếu every edge chi phí (cost / 비용) = 1:

\[
g(n)=độ sâu (depth / 깊이)(n)
\]

UCS thứ tự (ordering / 순서) theo đường dẫn (path / 경로) chi phí (cost / 비용) tương đương BFS thứ tự (ordering / 순서) theo độ sâu (depth / 깊이).

Đây là useful unification:

```text
BFS = UCS khi step cost uniform
```

## Negative edge chi phí (cost / 비용)

UCS/Dijkstra các giả định (assumptions / 가정들) require nonnegative edge chi phí (cost / 비용) for tiêu chuẩn (standard / 표준) optimality lô-gic (logic / 논리).

Nếu negative edges tồn tại, một nút (node / 노드) tưởng cheapest hiện tại có thể later được cải thiện qua negative-cost đường dẫn (path / 경로).

Các algorithms như Bellman–Ford handle negative edges trong đồ thị (graph / 그래프) shortest đường dẫn (path / 경로), và negative cycles làm shortest đường dẫn (path / 경로) undefined (`-∞`).

Trong AI chi phí (cost / 비용) thiết kế (design / 설계), negative rewards/costs cần careful formulation.

## Cycle checking

Trong cây (tree / 트리) tìm kiếm (search / 검색):

```text
A → B → C → A → ...
```

có thể tạo infinite expansion.

Path-based cycle checking ngăn trạng thái (state / 상태) lặp trên hiện tại (current / 현재) đường dẫn (path / 경로).

Toàn cục (global / 전역) explored set mạnh hơn, nhưng với weighted tìm kiếm (search / 검색) cần có best-cost lô-gic (logic / 논리): “đã thấy trạng thái (state / 상태)” không đủ nếu later đường dẫn (path / 경로) rẻ hơn.

## Frontier duplicates

Có hai hiện thực (implementation / 구현) styles:

1. decrease-key/cập nhật (update / 업데이트) entry trong priority hàng đợi (queue / 큐);
2. push new better entry và khi pop bỏ stale entry.

Style 2 thường đơn giản hơn với tiêu chuẩn (standard / 표준) vùng nhớ động (heap / 힙) libraries.

```python
if popped_cost != best[state]:
    continue
```

Mô hình tư duy (mental model / 사고 모델): `best` map là nguồn chuẩn (source of truth / 정본), vùng nhớ động (heap / 힙) có thể chứa stale candidates.

## Bidirectional tìm kiếm (search / 검색)

Nếu start `S` và chính xác (exact / 정확한) goal `G` đều known, tìm kiếm (search / 검색) forward từ `S` và backward từ `G`.

Idealized nút (node / 노드) counts:

\[
O(b^{d/2}) + O(b^{d/2})
\]

so với:

\[
O(b^d)
\]

cho one-direction BFS.

### Conditions thực tế

Bidirectional tìm kiếm (search / 검색) cần:

- generate predecessors hoặc reverse edges;
- efficient intersection kiểm thử (test / 테스트);
- careful stopping criterion với weighted costs;
- manageable frontier from both sides.

Nếu goal là predicate rộng (“bất kỳ schedule hợp lệ”), backward tìm kiếm (search / 검색) có thể không straightforward.

## Tìm kiếm (search / 검색) thứ tự (order / 순서) và tie-breaking

Ngay cả cùng BFS/UCS, thứ tự generate successors ảnh hưởng đường dẫn (path / 경로) returned khi multiple optimal solutions tồn tại.

A* tie-breaking cũng ảnh hưởng nodes expanded.

Reproducibility cần deterministic successor thứ tự (ordering / 순서) khi đầu ra (output / 출력) đường dẫn (path / 경로) matters.

## Cây (tree / 트리) độ phức tạp (complexity / 복잡도) và đồ thị (graph / 그래프) độ phức tạp (complexity / 복잡도)

Textbook often expresses độ phức tạp (complexity / 복잡도) bằng `b,d,m`, nhưng finite đồ thị (graph / 그래프) có `|V|,|E|`.

BFS đồ thị (graph / 그래프) traversal:

\[
O(|V|+|E|)
\]

nếu mỗi nút (node / 노드)/edge processed once.

Priority-queue shortest đường dẫn (path / 경로) có độ phức tạp (complexity / 복잡도) liên quan `|E| log |V|` tùy vùng nhớ động (heap / 힙) hiện thực (implementation / 구현).

Hai notation trả lời two views:

```text
AI search tree view → branching/depth
Graph algorithm view → vertices/edges
```

## Example: weighted routes

Suppose:

```text
S --1--> A --100--> G
 \                    
  --10--> B --10--> C --10--> G
```

BFS thấy `S-A-G` độ sâu (depth / 깊이) 2 và trả đường dẫn (path / 경로) chi phí (cost / 비용) 101.

UCS explores theo accumulated chi phí (cost / 비용) và tìm `S-B-C-G` chi phí (cost / 비용) 30.

Đây là lý do “ít bước hơn” không đồng nghĩa “rẻ hơn”.

## Bộ nhớ (memory / 메모리) as algorithmic tài nguyên (resource / 자원)

BFS thường thất bại (fail / 실패) vì RAM trước CPU.

Suppose frontier 10 million nodes, mỗi nút (node / 노드) siêu dữ liệu (metadata / 메타데이터) 100 bytes:

```text
≈ 1 GB
```

thực tế đối tượng (object / 객체) overhead có thể lớn hơn nhiều.

Compact trạng thái (state / 상태) encoding, parent reconstruction chiến lược (strategy / 전략), external-memory tìm kiếm (search / 검색) hoặc iterative deepening có thể quan trọng hơn micro-optimizing expansion.

## Iterative deepening và hiện đại (modern / 현대적) lập luận (reasoning / 추론) các hệ thống (systems / 시스템들)

Idea allocate progressively larger độ sâu (depth / 깊이) ngân sách (budget / 예산) có analog trong hiện đại (modern / 현대적) các hệ thống (systems / 시스템들):

```text
try shallow/simple reasoning
if insufficient → allow deeper search
```

Không nên gọi mọi “lập luận (reasoning / 추론) độ sâu (depth / 깊이) setting” là literal IDDFS, nhưng resource-bounded iterative expansion là recurring mẫu thiết kế (design pattern / 디자인 패턴).

## Beam tìm kiếm (search / 검색): informed bởi score nhưng incomplete

Beam tìm kiếm (search / 검색) thường được học gần chuỗi (sequence / 시퀀스) decoding hơn uninformed tìm kiếm (search / 검색), nhưng useful contrast.

At each độ sâu (depth / 깊이) chỉ giữ top `k` candidates theo score.

```text
all possibilities exponential
       ↓ prune
keep beam width k
```

Beam tìm kiếm (search / 검색) tiết kiệm bộ nhớ (memory / 메모리)/thời gian (time / 시간) nhưng không complete và không guarantee toàn cục (global / 전역) optimum.

Machine translation và chuỗi (sequence / 시퀀스) generation historically use beam tìm kiếm (search / 검색) extensively.

## Tìm kiếm (search / 검색) under tài nguyên (resource / 자원) limits

Real các hệ thống (systems / 시스템들) có:

- thời gian (time / 시간) ngân sách (budget / 예산);
- bộ nhớ (memory / 메모리) ngân sách (budget / 예산);
- API/công cụ (tool / 도구) chi phí (cost / 비용);
- đơn vị từ (token / 토큰) ngân sách (budget / 예산).

Một theoretically optimal tìm kiếm (search / 검색) may be unusable.

Resource-bounded algorithms trade solution chất lượng (quality / 품질) for computation.

This idea later appears in anytime algorithms, beam tìm kiếm (search / 검색), Monte Carlo cây (tree / 트리) tìm kiếm (search / 검색) and LLM tác nhân (agent / 에이전트) planning.

## Anytime algorithms

Anytime thuật toán (algorithm / 알고리즘) có thể return hiện tại (current / 현재) best solution nếu interrupted, và chất lượng (quality / 품질) cải thiện khi có thêm thời gian (time / 시간).

This is valuable when chính xác (exact / 정확한) compute ngân sách (budget / 예산) uncertain.

Weighted A* và iterative improvement methods can have anytime variants.

## Choosing an uninformed chiến lược (strategy / 전략)

| Situation | chiến lược (strategy / 전략) intuition |
|---|---|
| đơn vị (unit / 단위) chi phí (cost / 비용), shallow solution | BFS |
| bộ nhớ (memory / 메모리) tight, any solution | DFS / DLS |
| Unknown goal độ sâu (depth / 깊이), đơn vị (unit / 단위) chi phí (cost / 비용) | IDDFS |
| Different nonnegative costs | UCS |
| chính xác (exact / 정확한) start + goal, reversible đồ thị (graph / 그래프) | Bidirectional tìm kiếm (search / 검색) |

Bảng (table / 테이블) này là starting heuristic, không substitute phân tích (analysis / 분석) of actual đồ thị (graph / 그래프) kích thước (size / 크기), cycles, các ràng buộc (constraints / 제약조건들) và bộ nhớ (memory / 메모리) biểu diễn (representation / 표현).

## Mô hình tư duy (mental model / 사고 모델)

```text
BFS   = optimize depth
DFS   = commit to one branch, save memory
DLS   = DFS with horizon
IDDFS = BFS-like depth guarantee using DFS-like memory
UCS   = optimize accumulated path cost
Bidirectional = reduce effective depth by meeting in middle
```

## Dùng chung (common / 공통) Misconceptions

### “BFS luôn tìm shortest đường dẫn (path / 경로)”

Chỉ shortest number of edges; cost-optimal khi step costs equal/uniform.

### “DFS nhanh hơn BFS”

Không universal. Nó có different exploration thứ tự (order / 순서) và lower bộ nhớ (memory / 메모리), nhưng có thể tìm kiếm (search / 검색) huge wrong branch.

### “Visited set chỉ là tối ưu hóa (optimization / 최적화)”

Trong cyclic graphs, duplicate detection có thể quyết định termination và tính đúng đắn (correctness / 정확성).

### “UCS goal thấy lần đầu là đủ”

Goal cần được settled/popped theo lowest đường dẫn (path / 경로) chi phí (cost / 비용) lô-gic (logic / 논리); generated first chưa guarantee optimal.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Uninformed tìm kiếm (search / 검색) cung cấp baseline để thấy heuristic mang lại gì. [Heuristic Search](./02_heuristic_search.md) sẽ thêm estimate `h(n)` để focus expansion, còn Planning sẽ add richer hành động (action / 동작) preconditions/effects.

Khi chọn tìm kiếm (search / 검색) thuật toán (algorithm / 알고리즘), hãy bắt đầu bằng đồ thị (graph / 그래프) properties: branching factor, độ sâu (depth / 깊이), edge costs, cycles, bộ nhớ (memory / 메모리) ngân sách (budget / 예산) và whether goal/reverse transitions known.

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 state space and search](./00_state_space_and_search.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
