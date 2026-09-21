# Heuristic Search: Greedy Best-First và A*

Uninformed search biết trạng thái hiện tại, actions và cost đã đi, nhưng không biết hướng nào có vẻ gần goal hơn. Khi state space lớn, điều đó quá đắt. **Heuristic Search (휴리스틱 탐색)** thêm một estimate `h(n)` nhằm trả lời:

> Từ node `n`, còn khoảng bao nhiêu cost nữa để tới goal?

Heuristic không cần hoàn hảo. Chỉ cần correlate đủ tốt với remaining difficulty, nó có thể giảm số node expanded rất mạnh. Nhưng heuristic cũng đưa knowledge/assumption vào search, nên quality và correctness guarantees phụ thuộc properties của `h`.

Xem trước: [Uninformed Search](./01_uninformed_search.md).

## Heuristic function

Heuristic:

\[
h(n)\approx h^*(n)
\]

trong đó `h*(n)` là true optimal cost từ `n` tới goal.

Route planning example:

```text
h(n) = straight-line distance từ n tới destination
```

Actual road distance thường ≥ straight-line distance, nên đây có thể là lower bound phù hợp trong một số map/cost models.

Puzzle example: Manhattan distance sum của tiles tới goal positions.

Heuristic là domain knowledge được nén thành một scalar estimate.

## Greedy Best-First Search

Greedy Best-First Search chọn node có smallest:

\[
f(n)=h(n)
\]

Nó ignore cost đã bỏ ra `g(n)`.

Mental model:

```text
"state nào trông gần goal nhất thì đi trước"
```

Điều này có thể rất nhanh nếu heuristic tốt, nhưng dễ bị lừa.

## Greedy failure example

Suppose route:

```text
S → A → trap-like expensive region → G
 \ 
  → B → C → G
```

Heuristic đánh giá `A` rất gần goal theo geometric distance nhưng actual road blocked/expensive.

Greedy cứ follow `h` thấp dù path cost tăng mạnh.

Vì ignore `g(n)`, Greedy không guarantee optimality và standard graph formulation may require care for completeness.

## A*: combine past cost và future estimate

A* dùng:

\[
f(n)=g(n)+h(n)
\]

Trong đó:

- `g(n)` = actual cost từ start tới `n`;
- `h(n)` = estimated remaining cost;
- `f(n)` = estimated total solution cost through `n`.

A* cân bằng:

```text
what have I already paid?
        +
what do I expect remains?
```

Nếu `h(n)=0` mọi node, A* trở thành Uniform-Cost Search.

Nếu `g(n)` bị bỏ, behavior gần Greedy Best-First.

## Admissible heuristic

Heuristic **admissible (허용적 휴리스틱)** nếu không overestimate true remaining cost:

\[
0\le h(n)\le h^*(n)
\]

Nó “optimistic”.

Vì lower-bound estimate không exaggerate remaining cost, A* tree search có optimality guarantee dưới standard assumptions.

### Goal heuristic

Usually require:

\[
h(goal)=0
\]

Nếu goal remaining cost thật là 0, admissibility implies điều này cho nonnegative heuristic.

## Consistent heuristic

Heuristic **consistent / monotone (일관적 휴리스틱)** nếu với every transition `n→n'` cost `c`:

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

along path.

Consistency làm `f` nondecreasing và giúp graph-search A* settle nodes cleanly without repeated reopening under common implementation.

Consistent ⇒ admissible under suitable goal assumptions. Admissible không nhất thiết consistent.

## Vì sao A* optimal?

Intuition với admissible heuristic:

Suppose optimal solution cost `C*`.

For any node `n` trên optimal path:

\[
f(n)=g(n)+h(n)\le g(n)+h^*(n)=C^*
\]

Một suboptimal goal `G'` có:

\[
f(G')=g(G')>C^*
\]

vì `h(goal)=0`.

A* luôn expand smallest `f`; còn node optimal-path với `f≤C*` thì suboptimal goal không thể được selected first under assumptions.

Proof formal phụ thuộc tree/graph search details, nhưng đây là central intuition.

## Better heuristic means what?

Nếu `h_2(n)≥h_1(n)` mọi `n`, và cả hai admissible, `h_2` **dominates** `h_1`.

Closer lower bound thường làm A* expand fewer nodes.

Extreme cases:

```text
h(n)=0        → UCS, little guidance
h(n)=h*(n)    → perfect heuristic
```

Perfect heuristic biết exact remaining optimal cost, essentially solves much of problem already. Computing heuristic cũng có cost, nên practical trade-off là:

```text
heuristic accuracy vs heuristic computation cost
```

## Deriving heuristics bằng relaxed problem

Một powerful method là **relax constraints**.

Nếu solve easier problem whose optimal cost lower-bounds original problem, result becomes admissible heuristic.

8-puzzle example:

- original: tile moves only into blank adjacent position;
- relaxed: tile can move independently → Manhattan distance-like estimate.

General principle:

> Remove constraints → easier problem → optimistic lower bound.

This connects heuristic design with optimization relaxations.

## Pattern databases

Pattern Database (PDB) precompute exact distances for abstracted subset of problem states.

At runtime:

\[
h(n)=distance\_in\_abstract\_space(n)
\]

Nếu abstraction relaxes original problem properly, heuristic admissible.

PDB trades memory/precomputation for faster search.

This is early example of “learn/cache useful value estimates” before neural heuristics.

## Combining heuristics

Nếu `h1` và `h2` admissible, then:

\[
h(n)=\max(h_1(n),h_2(n))
\]

vẫn admissible và dominates each individually.

Sum `h1+h2` không automatically admissible vì có thể double-count cost, trừ khi heuristics additive under partitioned costs.

## Weighted A*

Weighted A*:

\[
f(n)=g(n)+w h(n),\quad w>1
\]

prioritize heuristic more strongly.

Nó thường expand fewer nodes/faster nhưng sacrifice exact optimality. Under certain assumptions one can derive bounded suboptimality.

This is practical example của quality-vs-compute trade-off.

## Anytime search

Anytime variants tìm solution nhanh trước, rồi use more time để improve bound/quality.

Example family: Anytime Repairing A* (ARA*) gradually reduce heuristic weight.

Useful in robotics/planning when system has variable planning time.

## Memory problem của A*

A* có thể be time-efficient nhưng memory-hungry vì store frontier/explored nodes.

Variants:

- Iterative Deepening A* (IDA*);
- Recursive Best-First Search (RBFS);
- Simplified Memory-Bounded A* (SMA*).

They trade repeated computation hoặc weaker behavior for lower memory.

## IDA*

IDA* uses depth-first contours bounded by `f=g+h` rather than depth.

Run DFS with threshold `T`; if no solution, next threshold becomes minimum exceeded `f`.

Memory near DFS, but nodes can be re-expanded many times.

Useful when memory dominates and heuristic reasonably strong.

## Beam Search

Beam Search keeps only best `k` candidates per depth/step according to score.

It is not A* and generally:

- incomplete;
- non-optimal;
- bounded memory roughly by beam width.

Sequence models use beam search because branching vocabulary huge and exact search impossible.

Beam score often uses log probability and length normalization, not classic path cost + admissible heuristic.

## Heuristic accuracy vs calibration

Heuristic need not be probability. It estimates cost/value.

For A* guarantees, *lower-bound property* matters more than statistical calibration.

A learned heuristic from neural network may be accurate average-wise but occasionally overestimate, breaking strict admissibility.

Practical learned search often accepts this to gain speed.

## Learned heuristics

Train model:

\[
h_\theta(s)\approx cost\_to\_goal(s)
\]

using solved examples.

Benefits:

- capture complex domain structure;
- fast inference after training;
- generalize across instances.

Risks:

- distribution shift;
- no admissibility guarantee;
- confident bad estimates;
- inference cost.

One hybrid approach combines safe lower bound + learned guidance separately.

## Policy guidance vs value heuristic

A **policy** predicts promising action:

\[
\pi(a\mid s)
\]

A **value/heuristic** estimates state quality or remaining cost:

\[
V(s), h(s)
\]

Search can use both:

```text
policy → order/select actions
value  → evaluate resulting states
```

This pattern is central in neural-guided game search and modern planning.

## A* và Dijkstra relationship

Dijkstra/UCS:

\[
f(n)=g(n)
\]

A*:

\[
f(n)=g(n)+h(n)
\]

Heuristic can be interpreted as a potential that reweights search toward goal.

When `h=0`, A* exactly reduces to UCS under equivalent implementation.

## Geometry heuristic

For 4-direction grid unit moves, Manhattan distance:

\[
h=|x-x_g|+|y-y_g|
\]

is admissible if no cheaper teleport/diagonal action exists.

If diagonal moves allowed with unit cost, Manhattan can overestimate and lose admissibility. Chebyshev-like distance may be appropriate.

Important lesson:

> A heuristic is only valid relative to transition model and cost model.

## Heuristic under dynamic environment

If road traffic changes, static distance heuristic may remain admissible for travel time only if lower-bound speed assumptions hold.

Dynamic path planning may use algorithms like D* / Lifelong Planning A* that reuse prior search when costs change.

This connects heuristic search to robotics/navigation.

## Search errors vs heuristic errors

If search returns bad path, diagnose:

```text
representation wrong?
transition/cost wrong?
heuristic invalid?
algorithm implementation wrong?
resource cutoff pruned optimum?
dynamic environment stale?
```

Do not blame heuristic alone.

## Heuristic search in theorem proving

Proof search state = current obligations/clauses; actions = inference rules; goal = proof complete.

Heuristics rank which clause/subgoal to expand.

Modern neural theorem provers learn rankings while symbolic kernel verifies correctness.

This is strong example of Search + Learning + Formal Verification.

## Heuristic search in LLM agents

Agent state may include task status, observations and tool results. Candidate action sequences branch rapidly.

LLM itself can propose actions; another model/rule can score states. Search may keep multiple candidates rather than single greedy chain.

But LLM scores are not admissible heuristic. Therefore A* theoretical guarantees do not transfer automatically.

Use terminology carefully:

```text
A*-like priority search with learned score
≠
classical A* with admissible h
```

## Search and Retrieval

Information retrieval ranks documents by relevance score. Conceptually it is search over corpus, but indexing/nearest-neighbor algorithms differ from state-space path search.

Approximate Nearest Neighbor systems deliberately sacrifice exactness for speed, analogous to resource-bounded search trade-offs.

Common mental pattern is **avoid exhaustive enumeration by using structure/guidance**.

## Mental Model

```text
g(n) = cost already paid
h(n) = estimate cost still remaining
f(n) = estimated total cost through n

Greedy → trusts h only
UCS    → trusts g only
A*     → balances g + h
```

Admissible heuristic is optimistic. Consistent heuristic also respects local triangle-like constraint.

## Common Misconceptions

### “A* always fastest shortest-path algorithm”

No. Performance depends heuristic quality, graph structure, implementation and memory. Poor `h` degenerates toward UCS.

### “Heuristic must be accurate”

For classical optimality guarantees, admissibility/consistency properties matter. A slightly less accurate admissible heuristic may be preferable to inaccurate overestimating one when exact optimality required.

### “Learned heuristic automatically makes A* optimal”

Not if it can overestimate and assumptions break.

### “Greedy and A* are basically same”

Greedy ignores accumulated cost `g`; A* includes it. This difference is fundamental.

## Knowledge Connection

Heuristic Search turns domain knowledge into computational savings. It connects classical AI to modern neural-guided search: handcrafted `h` can be replaced or complemented by learned value estimates, while search still handles combinatorial structure.

Xem tiếp: [Adversarial Search and Games](./03_adversarial_search_and_games.md), [Constraint Satisfaction](./04_constraint_satisfaction.md) và [Planning](./05_planning.md).