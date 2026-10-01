# Heuristic tìm kiếm (search / 검색): Greedy Best-First và A*

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Heuristic hàm (function / 함수)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Greedy Best-First tìm kiếm (search / 검색)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Uninformed tìm kiếm (search / 검색) biết trạng thái hiện tại, actions và chi phí (cost / 비용) đã đi, nhưng không biết hướng nào có vẻ gần goal hơn. Khi trạng thái (state / 상태) không gian (space / 공간) lớn, điều đó quá đắt. **Heuristic tìm kiếm (search / 검색)** thêm một estimate `h(n)` nhằm trả lời:

> Từ nút (node / 노드) `n`, còn khoảng bao nhiêu chi phí (cost / 비용) nữa để tới goal?

Heuristic không cần hoàn hảo. Chỉ cần correlate đủ tốt với remaining difficulty, nó có thể giảm số nút (node / 노드) expanded rất mạnh. Nhưng heuristic cũng đưa kiến thức (knowledge / 지식)/giả định (assumption / 가정) vào tìm kiếm (search / 검색), nên chất lượng (quality / 품질) và tính đúng đắn (correctness / 정확성) guarantees phụ thuộc properties của `h`.

Xem trước: [Uninformed Search](./01_uninformed_search.md).

## Heuristic hàm (function / 함수)

Heuristic:

\[
h(n)\approx h^*(n)
\]

trong đó `h*(n)` là true optimal chi phí (cost / 비용) từ `n` tới goal.

Tuyến (route / 경로) planning example:

```text
h(n) = straight-line distance từ n tới destination
```

Actual road distance thường ≥ straight-line distance, nên đây có thể là lower bound phù hợp trong một số map/chi phí (cost / 비용) các mô hình (models / 모델들).

Puzzle example: Manhattan distance sum của tiles tới goal positions.

Heuristic là lĩnh vực (domain / 도메인) kiến thức (knowledge / 지식) được nén thành một scalar estimate.

> **Chuyển mạch:** Trong **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Greedy Best-First tìm kiếm (search / 검색)** tiếp nhận điểm tựa từ **Heuristic hàm (function / 함수)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Greedy thất bại (failure / 실패) example** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Greedy Best-First tìm kiếm (search / 검색)

Greedy Best-First tìm kiếm (search / 검색) chọn nút (node / 노드) có smallest:

\[
f(n)=h(n)
\]

Nó ignore chi phí (cost / 비용) đã bỏ ra `g(n)`.

Mô hình tư duy (mental model / 사고 모델):

```text
"state nào trông gần goal nhất thì đi trước"
```

Điều này có thể rất nhanh nếu heuristic tốt, nhưng dễ bị lừa.

> **Chuyển mạch:** Ở chặng này của **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Greedy Best-First tìm kiếm (search / 검색)** cho ta quy tắc; **Greedy thất bại (failure / 실패) example** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **A: combine past chi phí (cost / 비용) và future estimate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Greedy thất bại (failure / 실패) example

Suppose tuyến (route / 경로):

```text
S → A → trap-like expensive region → G
 \ 
  → B → C → G
```

Heuristic đánh giá `A` rất gần goal theo geometric distance nhưng actual road blocked/expensive.

Greedy cứ follow `h` thấp dù đường dẫn (path / 경로) chi phí (cost / 비용) tăng mạnh.

Vì ignore `g(n)`, Greedy không guarantee optimality và tiêu chuẩn (standard / 표준) đồ thị (graph / 그래프) formulation may require care for completeness.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Greedy thất bại (failure / 실패) example** cho ta quy tắc; **A: combine past chi phí (cost / 비용) và future estimate** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Admissible heuristic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## A*: combine past chi phí (cost / 비용) và future estimate

A* dùng:

\[
f(n)=g(n)+h(n)
\]

Trong đó:

- `g(n)` = actual chi phí (cost / 비용) từ start tới `n`;
- `h(n)` = estimated remaining chi phí (cost / 비용);
- `f(n)` = estimated total solution chi phí (cost / 비용) through `n`.

A* cân bằng:

```text
what have I already paid?
        +
what do I expect remains?
```

Nếu `h(n)=0` mọi nút (node / 노드), A* trở thành Uniform-Cost tìm kiếm (search / 검색).

Nếu `g(n)` bị bỏ, hành vi (behavior / 동작) gần Greedy Best-First.

> **Chuyển mạch:** Trong **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Admissible heuristic** tiếp nhận điểm tựa từ **A: combine past chi phí (cost / 비용) và future estimate** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Consistent heuristic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Admissible heuristic

Heuristic **admissible (허용적 휴리스틱)** nếu không overestimate true remaining chi phí (cost / 비용):

\[
0\le h(n)\le h^*(n)
\]

Nó “optimistic”.

Vì lower-bound estimate không exaggerate remaining chi phí (cost / 비용), A* cây (tree / 트리) tìm kiếm (search / 검색) có optimality guarantee dưới tiêu chuẩn (standard / 표준) các giả định (assumptions / 가정들).

### Goal heuristic

Usually require:

\[
h(goal)=0
\]

Nếu goal remaining chi phí (cost / 비용) thật là 0, admissibility implies điều này cho nonnegative heuristic.

> **Chuyển mạch:** Ở chặng này của **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Consistent heuristic** tiếp nhận điểm tựa từ **Admissible heuristic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao A optimal?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Consistent heuristic

Heuristic **consistent / monotone (일관적 휴리스틱)** nếu với every chuyển tiếp (transition / 전이) `n→n'` chi phí (cost / 비용) `c`:

\[
h(n)\le c(n,n')+h(n')
\]

Đây giống triangle inequality.

Rearrange:

\[
g(n)+h(n)\le g(n)+c(n,n')+h(n')
\]

nên:

\[
f(n)\le f(n')
\]

along đường dẫn (path / 경로).

Consistency làm `f` nondecreasing và giúp graph-search A* settle nodes cleanly without repeated reopening under dùng chung (common / 공통) hiện thực (implementation / 구현).

Consistent ⇒ admissible under suitable goal các giả định (assumptions / 가정들). Admissible không nhất thiết consistent.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Vì sao A optimal?** tiếp nhận điểm tựa từ **Consistent heuristic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Better heuristic means what?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao A* optimal?

Intuition với admissible heuristic:

Suppose optimal solution chi phí (cost / 비용) `C*`.

For any nút (node / 노드) `n` trên optimal đường dẫn (path / 경로):

\[
f(n)=g(n)+h(n)\le g(n)+h^*(n)=C^*
\]

Một suboptimal goal `G'` có:

\[
f(G')=g(G')>C^*
\]

vì `h(goal)=0`.

A* luôn expand smallest `f`; còn nút (node / 노드) optimal-path với `f≤C*` thì suboptimal goal không thể được selected first under các giả định (assumptions / 가정들).

Proof formal phụ thuộc cây (tree / 트리)/đồ thị (graph / 그래프) tìm kiếm (search / 검색) details, nhưng đây là central intuition.

> **Chuyển mạch:** Trong **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Better heuristic means what?** tiếp nhận điểm tựa từ **Vì sao A optimal?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Deriving heuristics bằng relaxed bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Better heuristic means what?

Nếu `h_2(n)≥h_1(n)` mọi `n`, và cả hai admissible, `h_2` **dominates** `h_1`.

Closer lower bound thường làm A* expand fewer nodes.

Extreme cases:

```text
h(n)=0        → UCS, little guidance
h(n)=h*(n)    → perfect heuristic
```

Perfect heuristic biết chính xác (exact / 정확한) remaining optimal chi phí (cost / 비용), essentially solves much of bài toán (problem / 문제) already. Computing heuristic cũng có chi phí (cost / 비용), nên practical sự đánh đổi (trade-off / 트레이드오프) là:

```text
heuristic accuracy vs heuristic computation cost
```

> **Chuyển mạch:** Ở chặng này của **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Deriving heuristics bằng relaxed bài toán (problem / 문제)** tiếp nhận điểm tựa từ **Better heuristic means what?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) databases** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deriving heuristics bằng relaxed bài toán (problem / 문제)

Một powerful phương thức (method / 메서드) là **relax các ràng buộc (constraints / 제약조건들)**.

Nếu solve easier bài toán (problem / 문제) whose optimal chi phí (cost / 비용) lower-bounds original bài toán (problem / 문제), kết quả (result / 결과) becomes admissible heuristic.

8-puzzle example:

- original: tile moves only into blank adjacent position;
- relaxed: tile can move independently → Manhattan distance-like estimate.

General principle:

> Remove các ràng buộc (constraints / 제약조건들) → easier bài toán (problem / 문제) → optimistic lower bound.

This connects heuristic thiết kế (design / 설계) with tối ưu hóa (optimization / 최적화) relaxations.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Mẫu (pattern / 패턴) databases** tiếp nhận điểm tựa từ **Deriving heuristics bằng relaxed bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Combining heuristics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) databases

Mẫu (pattern / 패턴) cơ sở dữ liệu (database / 데이터베이스) (PDB) precompute chính xác (exact / 정확한) distances for abstracted subset of bài toán (problem / 문제) states.

At thời gian chạy (runtime / 런타임):

\[
h(n)=distance\_in\_abstract\_space(n)
\]

Nếu lớp trừu tượng (abstraction / 추상화) relaxes original bài toán (problem / 문제) properly, heuristic admissible.

PDB trades bộ nhớ (memory / 메모리)/precomputation for faster tìm kiếm (search / 검색).

This is early example of “learn/bộ nhớ đệm (cache / 캐시) useful giá trị (value / 값) estimates” before neural heuristics.

> **Chuyển mạch:** Trong **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Combining heuristics** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) databases** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Weighted A** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Combining heuristics

Nếu `h1` và `h2` admissible, then:

\[
h(n)=\max(h_1(n),h_2(n))
\]

vẫn admissible và dominates each individually.

Sum `h1+h2` không automatically admissible vì có thể double-count chi phí (cost / 비용), trừ khi heuristics additive under partitioned costs.

> **Chuyển mạch:** Ở chặng này của **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Weighted A** tiếp nhận điểm tựa từ **Combining heuristics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Anytime tìm kiếm (search / 검색)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Weighted A*

Weighted A*:

\[
f(n)=g(n)+w h(n),\quad w>1
\]

prioritize heuristic more strongly.

Nó thường expand fewer nodes/faster nhưng sacrifice chính xác (exact / 정확한) optimality. Under certain các giả định (assumptions / 가정들) one can derive bounded suboptimality.

This is practical example của quality-vs-compute sự đánh đổi (trade-off / 트레이드오프).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Anytime tìm kiếm (search / 검색)** tiếp nhận điểm tựa từ **Weighted A** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ (memory / 메모리) bài toán (problem / 문제) của A** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Anytime tìm kiếm (search / 검색)

Anytime variants tìm solution nhanh trước, rồi use more thời gian (time / 시간) để improve bound/chất lượng (quality / 품질).

Example family: Anytime Repairing A* (ARA*) gradually reduce heuristic weight.

Useful in robotics/planning when hệ thống (system / 시스템) has variable planning thời gian (time / 시간).

> **Chuyển mạch:** Trong **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Bộ nhớ (memory / 메모리) bài toán (problem / 문제) của A** tiếp nhận điểm tựa từ **Anytime tìm kiếm (search / 검색)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **IDA** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ (memory / 메모리) bài toán (problem / 문제) của A*

A* có thể be time-efficient nhưng memory-hungry vì store frontier/explored nodes.

Variants:

- Iterative Deepening A* (IDA*);
- Recursive Best-First tìm kiếm (search / 검색) (RBFS);
- Simplified Memory-Bounded A* (SMA*).

They trade repeated computation hoặc weaker hành vi (behavior / 동작) for lower bộ nhớ (memory / 메모리).

> **Chuyển mạch:** Ở chặng này của **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **IDA** tiếp nhận điểm tựa từ **Bộ nhớ (memory / 메모리) bài toán (problem / 문제) của A** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Beam tìm kiếm (search / 검색)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## IDA*

IDA* uses depth-first contours bounded by `f=g+h` rather than độ sâu (depth / 깊이).

Run DFS with threshold `T`; if no solution, next threshold becomes minimum exceeded `f`.

Bộ nhớ (memory / 메모리) near DFS, but nodes can be re-expanded many times.

Useful when bộ nhớ (memory / 메모리) dominates and heuristic reasonably strong.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Beam tìm kiếm (search / 검색)** tiếp nhận điểm tựa từ **IDA** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Heuristic accuracy vs calibration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Beam tìm kiếm (search / 검색)

Beam tìm kiếm (search / 검색) keeps only best `k` candidates per độ sâu (depth / 깊이)/step according to score.

It is not A* and generally:

- incomplete;
- non-optimal;
- bounded bộ nhớ (memory / 메모리) roughly by beam width.

Chuỗi (sequence / 시퀀스) các mô hình (models / 모델들) use beam tìm kiếm (search / 검색) because branching vocabulary huge and chính xác (exact / 정확한) tìm kiếm (search / 검색) impossible.

Beam score often uses log xác suất (probability / 확률) and length normalization, not classic đường dẫn (path / 경로) chi phí (cost / 비용) + admissible heuristic.

> **Chuyển mạch:** Trong **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Heuristic accuracy vs calibration** tiếp nhận điểm tựa từ **Beam tìm kiếm (search / 검색)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Learned heuristics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Heuristic accuracy vs calibration

Heuristic need not be xác suất (probability / 확률). It estimates chi phí (cost / 비용)/giá trị (value / 값).

For A* guarantees, *lower-bound thuộc tính (property / 속성)* matters more than statistical calibration.

A learned heuristic from neural mạng (network / 네트워크) may be accurate average-wise but occasionally overestimate, breaking strict admissibility.

Practical learned tìm kiếm (search / 검색) often accepts this to gain speed.

> **Chuyển mạch:** Ở chặng này của **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Learned heuristics** tiếp nhận điểm tựa từ **Heuristic accuracy vs calibration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chính sách (policy / 정책) guidance vs giá trị (value / 값) heuristic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Learned heuristics

Train mô hình (model / 모델):

\[
h_\theta(s)\approx chi phí (cost / 비용)\_to\_goal(s)
\]

using solved examples.

Benefits:

- capture complex lĩnh vực (domain / 도메인) cấu trúc (structure / 구조);
- fast suy luận (inference / 추론) after huấn luyện (training / 학습);
- generalize across instances.

Risks:

- phân phối (distribution / 분포) shift;
- no admissibility guarantee;
- confident bad estimates;
- suy luận (inference / 추론) chi phí (cost / 비용).

One hybrid approach combines safe lower bound + learned guidance separately.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Chính sách (policy / 정책) guidance vs giá trị (value / 값) heuristic** tiếp nhận điểm tựa từ **Learned heuristics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **A và Dijkstra relationship** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chính sách (policy / 정책) guidance vs giá trị (value / 값) heuristic

A **chính sách (policy / 정책)** predicts promising hành động (action / 동작):

\[
\pi(a\mid s)
\]

A **giá trị (value / 값)/heuristic** estimates trạng thái (state / 상태) chất lượng (quality / 품질) or remaining chi phí (cost / 비용):

\[
V(s), h(s)
\]

Tìm kiếm (search / 검색) can use both:

```text
policy → order/select actions
value  → evaluate resulting states
```

This mẫu (pattern / 패턴) is central in neural-guided game tìm kiếm (search / 검색) and hiện đại (modern / 현대적) planning.

> **Chuyển mạch:** Trong **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **A và Dijkstra relationship** tiếp nhận điểm tựa từ **Chính sách (policy / 정책) guidance vs giá trị (value / 값) heuristic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hình học (geometry / 기하학) heuristic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## A* và Dijkstra relationship

Dijkstra/UCS:

\[
f(n)=g(n)
\]

A*:

\[
f(n)=g(n)+h(n)
\]

Heuristic can be interpreted as a potential that reweights tìm kiếm (search / 검색) toward goal.

When `h=0`, A* exactly reduces to UCS under equivalent hiện thực (implementation / 구현).

> **Chuyển mạch:** Ở chặng này của **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Hình học (geometry / 기하학) heuristic** tiếp nhận điểm tựa từ **A và Dijkstra relationship** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Heuristic under động (dynamic / 동적) môi trường (environment / 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hình học (geometry / 기하학) heuristic

For 4-direction grid đơn vị (unit / 단위) moves, Manhattan distance:

\[
h=|x-x_g|+|y-y_g|
\]

is admissible if no cheaper teleport/diagonal hành động (action / 동작) exists.

If diagonal moves allowed with đơn vị (unit / 단위) chi phí (cost / 비용), Manhattan can overestimate and lose admissibility. Chebyshev-like distance may be appropriate.

Important lesson:

> A heuristic is only valid relative to chuyển tiếp (transition / 전이) mô hình (model / 모델) and chi phí (cost / 비용) mô hình (model / 모델).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Heuristic under động (dynamic / 동적) môi trường (environment / 환경)** tiếp nhận điểm tựa từ **Hình học (geometry / 기하학) heuristic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tìm kiếm (search / 검색) errors vs heuristic errors** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Heuristic under động (dynamic / 동적) môi trường (environment / 환경)

If road traffic changes, static distance heuristic may remain admissible for travel thời gian (time / 시간) only if lower-bound speed các giả định (assumptions / 가정들) hold.

Động (dynamic / 동적) đường dẫn (path / 경로) planning may use algorithms like D* / Lifelong Planning A* that reuse prior tìm kiếm (search / 검색) when costs thay đổi (change / 변경).

This connects heuristic tìm kiếm (search / 검색) to robotics/điều hướng (navigation / 내비게이션).

> **Chuyển mạch:** Trong **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Tìm kiếm (search / 검색) errors vs heuristic errors** tiếp nhận điểm tựa từ **Heuristic under động (dynamic / 동적) môi trường (environment / 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Heuristic tìm kiếm (search / 검색) in theorem proving** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tìm kiếm (search / 검색) errors vs heuristic errors

If tìm kiếm (search / 검색) returns bad đường dẫn (path / 경로), diagnose:

```text
representation wrong?
transition/cost wrong?
heuristic invalid?
algorithm implementation wrong?
resource cutoff pruned optimum?
dynamic environment stale?
```

Do not blame heuristic alone.

> **Chuyển mạch:** Ở chặng này của **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Heuristic tìm kiếm (search / 검색) in theorem proving** tiếp nhận điểm tựa từ **Tìm kiếm (search / 검색) errors vs heuristic errors** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Heuristic tìm kiếm (search / 검색) in LLM agents** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Heuristic tìm kiếm (search / 검색) in theorem proving

Proof tìm kiếm (search / 검색) trạng thái (state / 상태) = hiện tại (current / 현재) obligations/clauses; actions = suy luận (inference / 추론) rules; goal = proof complete.

Heuristics rank which clause/subgoal to expand.

Hiện đại (modern / 현대적) neural theorem provers learn rankings while symbolic kernel verifies tính đúng đắn (correctness / 정확성).

This is strong example of tìm kiếm (search / 검색) + học tập (learning / 학습) + Formal xác minh (verification / 확인).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Heuristic tìm kiếm (search / 검색) in LLM agents** tiếp nhận điểm tựa từ **Heuristic tìm kiếm (search / 검색) in theorem proving** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tìm kiếm (search / 검색) and Retrieval** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Heuristic tìm kiếm (search / 검색) in LLM agents

Tác nhân (agent / 에이전트) trạng thái (state / 상태) may include tác vụ (task / 작업) status, observations and công cụ (tool / 도구) results. Candidate hành động (action / 동작) sequences branch rapidly.

LLM itself can propose actions; another mô hình (model / 모델)/quy tắc (rule / 규칙) can score states. tìm kiếm (search / 검색) may keep multiple candidates rather than single greedy chuỗi (chain / 사슬).

But LLM scores are not admissible heuristic. Therefore A* theoretical guarantees do not transfer automatically.

Use terminology carefully:

```text
A*-like priority search with learned score
≠
classical A* with admissible h
```

> **Chuyển mạch:** Trong **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Tìm kiếm (search / 검색) and Retrieval** tiếp nhận điểm tựa từ **Heuristic tìm kiếm (search / 검색) in LLM agents** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tìm kiếm (search / 검색) and Retrieval

Thông tin (information / 정보) retrieval ranks documents by relevance score. Conceptually it is tìm kiếm (search / 검색) over corpus, but indexing/nearest-neighbor algorithms differ from state-space đường dẫn (path / 경로) tìm kiếm (search / 검색).

Approximate Nearest Neighbor các hệ thống (systems / 시스템들) deliberately sacrifice exactness for speed, analogous to resource-bounded tìm kiếm (search / 검색) trade-offs.

Dùng chung (common / 공통) mental mẫu (pattern / 패턴) is **avoid exhaustive enumeration by using cấu trúc (structure / 구조)/guidance**.

> **Chuyển mạch:** Ở chặng này của **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Tìm kiếm (search / 검색) and Retrieval** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
g(n) = cost already paid
h(n) = estimate cost still remaining
f(n) = estimated total cost through n

Greedy → trusts h only
UCS    → trusts g only
A*     → balances g + h
```

Admissible heuristic is optimistic. Consistent heuristic also respects cục bộ (local / 로컬) triangle-like ràng buộc (constraint / 제약조건).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “A* always fastest shortest-path thuật toán (algorithm / 알고리즘)”

No. hiệu năng (performance / 성능) depends heuristic chất lượng (quality / 품질), đồ thị (graph / 그래프) cấu trúc (structure / 구조), hiện thực (implementation / 구현) and bộ nhớ (memory / 메모리). Poor `h` degenerates toward UCS.

### “Heuristic must be accurate”

For classical optimality guarantees, admissibility/consistency properties matter. A slightly less accurate admissible heuristic may be preferable to inaccurate overestimating one when chính xác (exact / 정확한) optimality required.

### “Learned heuristic automatically makes A* optimal”

Not if it can overestimate and các giả định (assumptions / 가정들) break.

### “Greedy and A* are basically same”

Greedy ignores accumulated chi phí (cost / 비용) `g`; A* includes it. This difference is fundamental.

> **Chuyển mạch:** Trong **Heuristic tìm kiếm (search / 검색): Greedy Best-First và A**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Heuristic tìm kiếm (search / 검색) turns lĩnh vực (domain / 도메인) kiến thức (knowledge / 지식) into computational savings. It connects classical AI to hiện đại (modern / 현대적) neural-guided tìm kiếm (search / 검색): handcrafted `h` can be replaced or complemented by learned giá trị (value / 값) estimates, while tìm kiếm (search / 검색) still handles combinatorial cấu trúc (structure / 구조).

Xem tiếp: [Adversarial Search and Games](./03_adversarial_search_and_games.md), [Constraint Satisfaction](./04_constraint_satisfaction.md) và [Planning](./05_planning.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
