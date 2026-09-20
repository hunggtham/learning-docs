# Khi Exact Algorithm trở nên khó: Reductions, NP-Complete và Approximation
**환원, NP-완전, 근사 알고리즘**

DSA không chỉ dạy cách làm nhanh. Một phần trưởng thành của algorithmic thinking là nhận ra khi một problem general đã khó tới mức việc tiếp tục “tối ưu data structure” không giải quyết được bản chất search space. Khi đó câu hỏi phải đổi từ:

> “Làm sao giảm `O(n^2)` xuống `O(n log n)`?”

sang:

> “General exact problem có khả năng polynomial-time không? Nếu chưa biết, ta có thể khai thác special structure, parameter nhỏ, approximation, heuristic, SAT/ILP solver hay exponential algorithm thông minh nào?”

Chapter này cung cấp mental model để đọc complexity-theory terms và dùng chúng như công cụ engineering, không phải như vocabulary học thuộc.

## Polynomial và exponential là hai scale rất khác

`O(n^3)` có thể nặng nhưng vẫn polynomial. `O(2^n)` tăng khác hẳn: mỗi khi `n` tăng 1, work có thể gần gấp đôi.

Rough intuition:

```text
2^20  ≈ 1 triệu
2^30  ≈ 1 tỷ
2^40  ≈ 1 nghìn tỷ
```

Trong khi đó `n^3` với `n=1000` cũng khoảng một tỷ operations nhưng growth khác hoàn toàn khi `n` tăng tiếp.

Điều quan trọng không phải một threshold cứng, mà là biết exponential search chỉ phù hợp khi `n`/parameter nhỏ hoặc pruning/structure cực mạnh.

## Decision problem và optimization problem

Complexity theory thường nói về **decision problem / 결정 문제** vì output chỉ yes/no, giúp class definitions rõ ràng.

Ví dụ optimization TSP hỏi:

> Tour ngắn nhất dài bao nhiêu?

Decision version hỏi:

> Có tour đi qua mọi city với total cost `<= B` không?

Nếu giải optimization được thì decision dễ. Ngược lại, nhiều optimization problems có thể solved bằng repeated decision queries/binary search dưới conditions thích hợp.

Phân biệt này giúp hiểu tại sao NP-complete thường được định nghĩa cho decision versions.

## Class P

**P** là lớp decision problems có deterministic polynomial-time algorithm trong standard computational model.

Examples kinh điển:

```text
shortest path với non-negative weights
minimum spanning tree
maximum flow
bipartite matching
sorting-based decisions
```

Polynomial không đồng nghĩa practical cho mọi `n`; `O(n^100)` vẫn polynomial. Nhưng P dùng để phân biệt growth class lý thuyết, không phải performance SLA.

## Class NP

**NP** là lớp decision problems mà nếu answer là “yes”, tồn tại certificate có thể verify trong polynomial time.

Ví dụ Hamiltonian Cycle: certificate là một sequence vertices. Verification chỉ cần check sequence dùng mỗi vertex đúng rule và edges tồn tại.

NP không có nghĩa “non-polynomial”, “not possible” hay “hard by definition”. P là subset của NP vì nếu solve polynomial được thì verify cũng polynomial.

## NP-hard và NP-complete

**NP-hard** nghĩa problem ít nhất khó như mọi problem trong NP theo polynomial-time reduction framework. Nó không bắt buộc là decision problem và không bắt buộc thuộc NP.

**NP-complete** nghĩa:

```text
problem ∈ NP
và
problem là NP-hard
```

Nếu tìm polynomial-time algorithm cho bất kỳ NP-complete problem, thì mọi problem trong NP sẽ có polynomial algorithm và `P=NP`.

Cho tới hiện nay, chưa có proof được cộng đồng chấp nhận rằng `P=NP` hay `P≠NP`.

## “NP-complete” không có nghĩa bỏ cuộc

NP-complete nói về general worst-case problem class. Nó không nói every instance khó.

Real-world instances có thể:

```text
n nhỏ
parameter nhỏ
structure đặc biệt
sparse graph
bounded treewidth
geometric restrictions
nearly feasible solution
strong practical solver heuristics
```

Special cases có thể polynomial dù general problem NP-hard.

Một engineer nên hỏi “instance distribution của tôi là gì?” chứ không dừng ở label complexity.

## Reduction là language để so độ khó

Một polynomial-time reduction từ A sang B biến instance `x` của A thành instance `f(x)` của B sao cho:

\[
x\in A \iff f(x)\in B
\]

và `f` computable polynomial time.

Nếu A đã biết hard và `A <=p B`, thì B ít nhất hard tương đương theo framework này.

Direction rất dễ nhầm.

Muốn chứng minh B hard, ta reduce **known hard problem A to B**, không phải B to A.

## Reduction cũng là algorithm-design tool tích cực

Reduction không chỉ để chứng minh hardness. Trong thực hành, ta liên tục reduce problem mới về known solvable problem:

```text
assignment -> bipartite matching
circulation constraints -> max flow
difference constraints -> shortest path
dependency scheduling -> DAG/topological sort
2-SAT -> implication graph + SCC
```

Đây là “reuse theorem/algorithm” ở mức problem model.

Nếu có thể transform problem thành flow, matching hay shortest path mà giữ semantics, ta tránh re-invent solver.

## Một reduction tốt cần chứng minh hai chiều

Không đủ chỉ nói “solution của A trông giống solution của B”. Cần chứng minh:

1. nếu A có yes-solution thì transformed B có yes-solution;
2. nếu transformed B có yes-solution thì có thể suy ra yes-solution cho A.

Nếu thiếu một direction, transformation có thể thêm false solutions hoặc mất valid solutions.

## Independent Set và Vertex Cover

Trong same undirected graph:

\[
S \text{ independent}
\iff
V\setminus S \text{ vertex cover}
\]

Do đó:

```text
Independent Set size >= k
```

tương đương:

```text
Vertex Cover size <= |V|-k
```

Connection này là structural complement relation, minh họa reduction/dual viewpoint rõ ràng.

## Clique connection

Một set vertices là clique trong graph `G` iff nó là independent set trong complement graph `\bar G`.

Vì vậy Clique, Independent Set và Vertex Cover có các transformations chặt chẽ.

Mental model quan trọng: nhiều “different” combinatorial problems chỉ là cùng constraint nhìn qua complement/duality.

## SAT và CNF intuition

SAT hỏi có assignment boolean làm formula true không. CNF-SAT dùng conjunction của clauses, mỗi clause là disjunction literals.

3-SAT restrict mỗi clause có 3 literals nhưng vẫn NP-complete.

SAT là central vì many problems có thể encode thành logical constraints; modern SAT solvers cực mạnh trên nhiều practical instances dù worst-case exponential.

## 2-SAT là special case polynomial

2-SAT chỉ có clauses 2 literals và solve bằng implication graph + SCC trong linear time.

Clause:

\[
(a\lor b)
\]

tương đương implications:

```text
not a -> b
not b -> a
```

Formula satisfiable iff không variable nào cùng SCC với negation của nó.

Một thay đổi constraint nhỏ — clause length 2 vs 3 — thay đổi complexity landscape mạnh. Đây là lesson lớn: luôn tìm special structure.

## Knapsack: pseudo-polynomial algorithm

0/1 Knapsack general decision form NP-complete, nhưng classic DP `O(nW)` theo capacity `W`.

Đây là **pseudo-polynomial**, vì `W` được encode bằng `log W` bits. Runtime polynomial theo numeric value `W`, không polynomial theo input bit-length.

Nếu `W` nhỏ thực tế, DP rất practical. Complexity theory giúp giải thích tại sao “NP-hard nhưng DP chạy tốt” không mâu thuẫn.

## Weakly vs strongly NP-hard intuition

Một số problems có pseudo-polynomial algorithms và hardness liên quan large numeric values; chúng thường được gọi weakly NP-hard/complete trong appropriate setting.

Strongly NP-hard problems vẫn hard ngay khi numeric magnitudes polynomially bounded, nên pseudo-polynomial rescue không tương tự.

Không cần memorize classifications ngay; mental model là numeric value magnitude có thể là hidden dimension.

## Exact exponential algorithms vẫn rất quan trọng

Khi `n` nhỏ, exact exponential algorithms là lựa chọn đúng.

Toolbox gồm:

```text
backtracking
branch and bound
bitmask DP
meet-in-the-middle
subset convolution/SOS ideas
SAT/SMT/ILP/CP solver
parameterized algorithms
```

“Exponential” không đồng nghĩa “bad” nếu parameter nhỏ và alternative approximation không acceptable.

## Meet-in-the-middle

Nếu brute-force `2^n` quá lớn nhưng `n≈40`, split items thành two halves.

Enumerate mỗi half:

\[
2^{n/2}
\]

states, rồi combine bằng sorting/hash/two pointers/binary search.

Total scale roughly:

\[
O(2^{n/2}\operatorname{poly}(n))
\]

thay vì `2^n`.

Subset Sum là classic application.

Meet-in-the-middle là example quan trọng của **time-space/search decomposition**, không phải magic trick.

## Bitmask DP

TSP Held-Karp state:

```text
dp[mask][v] = minimum cost visit exactly mask and end at v
```

Number states `O(n2^n)`, transitions thêm factor `n`, total around:

\[
O(n^2 2^n)
\]

vẫn exponential nhưng tốt hơn `n!` brute-force.

State compression biến many path histories thành same `(mask,v)` state.

## Branch and bound

Backtracking prune khi partial state infeasible. Branch-and-bound còn tính optimistic bound về best objective branch có thể đạt.

Minimization example:

```text
if lowerBound(branch) >= bestKnown:
    prune
```

Bound phải **safe**. Bound yếu chỉ prune ít; bound không valid có thể xóa optimum và phá correctness.

Design good bound thường là phần khó nhất.

## Search order ảnh hưởng practical performance

Branch-and-bound đúng với bất kỳ branch order nếu bound safe, nhưng tìm good incumbent sớm làm pruning mạnh hơn.

Heuristics chọn promising branch first có thể giảm search tree rất lớn dù worst-case unchanged.

Đây là distinction giữa correctness guarantee và practical search engineering.

## Constraint propagation

CSP/SAT-style search giảm domains trước khi branching. Nếu choosing one variable forces consequences, propagate ngay để detect contradiction early.

Sudoku, exact cover và scheduling có thể được speed up mạnh bằng propagation + smart variable ordering.

Backtracking performance phụ thuộc search tree *sau propagation*, không chỉ raw combinatorial size.

## Parameterized complexity

Nếu problem khó chủ yếu vì parameter `k`, runtime:

\[
f(k)n^{O(1)}
\]

được gọi fixed-parameter tractable (FPT) nếu `f` chỉ phụ thuộc `k`.

Ví dụ algorithm exponential theo solution size nhưng polynomial theo graph size có thể excellent khi `k` nhỏ.

Parameterized thinking hỏi:

> Có một dimension nhỏ tự nhiên nào kiểm soát hardness không?

Examples: treewidth, number of edits, solution size, number of special vertices.

## Kernelization intuition

Một parameterized algorithm có thể preprocess instance thành equivalent smaller instance whose size bounded by function of `k`. Đây gọi là kernelization trong appropriate framework.

Engineering analogy: loại forced/irrelevant structure trước expensive search.

## Treewidth intuition

Graph tree-like có thể cho dynamic programming tốt dù general graph problem NP-hard. Tree decomposition biến graph thành bags với limited interaction width.

Runtime thường exponential theo treewidth `k` nhưng linear/polynomial theo `n`:

\[
f(k)n^{O(1)}
\]

Đây là một ví dụ structure parameter thay đổi practical solvability.

## Approximation algorithm

Approximation algorithm trả feasible solution với **provable quality guarantee** so với optimum.

Với minimization, `α`-approximation thường nghĩa:

\[
cost(A(I)) \le \alpha\,OPT(I)
\]

cho mọi instances trong problem class.

Với maximization, ratio convention có thể viết khác; luôn đọc exact definition.

Approximation không đồng nghĩa “answer gần gần”. Guarantee phải formal.

## Vertex Cover 2-approximation

Một classic approach: lấy một maximal matching `M`, đưa cả hai endpoints của mỗi matched edge vào cover.

Result size:

\[
2|M|
\]

Bất kỳ vertex cover phải chứa ít nhất một endpoint của mỗi matching edge, và matching edges disjoint, nên:

\[
OPT \ge |M|
\]

suy ra result `<=2OPT`.

Đây là một proof approximation ratio rất rõ: construct solution + lower bound optimum.

## Metric TSP và triangle inequality

General weighted TSP rất khó approximate mạnh nếu không assumptions. Metric TSP thêm triangle inequality:

\[
d(a,c)\le d(a,b)+d(b,c)
\]

Structure này cho approximation algorithms có guarantees.

Lesson: approximation ratio luôn gắn problem assumptions; không được transfer guarantee sang general variant.

## PTAS và FPTAS intuition

**PTAS**: với mọi fixed `ε>0`, trả `(1+ε)`-approx (minimization convention) trong polynomial time theo input size, nhưng polynomial degree có thể phụ thuộc mạnh vào `1/ε`.

**FPTAS** yêu cầu runtime polynomial cả theo input size và `1/ε`.

Knapsack có FPTAS via value scaling ideas.

Các terms này giúp mô tả controllable accuracy-time trade-off.

## Heuristic khác approximation

Heuristic như local search, simulated annealing, tabu search, genetic algorithms, domain-specific greedy có thể excellent thực tế nhưng không có worst-case approximation guarantee tương tự.

Không nên gọi một heuristic “approximation algorithm” chỉ vì output approximate.

Engineering có thể hoàn toàn chọn heuristic — chỉ cần mô tả guarantee trung thực.

## Local Search

Local Search bắt đầu với feasible solution, repeatedly move tới neighbor solution tốt hơn cho tới local optimum.

Performance phụ thuộc neighborhood definition. Local optimum không nhất thiết global optimum.

TSP 2-opt/3-opt là examples practical. Search quality có thể improved bằng random restarts hoặc metaheuristics.

## Randomized algorithms vs heuristics

Một randomized algorithm có thể có provable expected runtime/correctness probability. Heuristic randomness không tự tạo guarantee.

Ví dụ randomized quicksort exact output và expected `O(n log n)`; simulated annealing typically heuristic practical behavior unless specific theorem assumptions.

Phân biệt type of uncertainty quan trọng.

## Relaxation

Một powerful strategy là relax constraint để solve easier problem và dùng result làm bound/guide.

Integer programming relax integrality thành linear programming. Branch-and-bound dùng LP relaxation lower/upper bound.

Combinatorial algorithms cũng có relaxations: MST lower bound cho TSP-like structures under conditions, matching relaxation, etc.

Relaxation connects exact optimization và approximation.

## Linear Programming intuition

LP optimize linear objective với linear constraints trên continuous variables, solvable polynomial-time theoretically.

Many discrete problems become hard vì integrality constraints. LP relaxation cho fractional solution dễ hơn và có thể rounding thành approximate integer solution.

Approximation design thường gồm:

```text
relax -> solve -> round -> prove loss bound
```

## Integrality gap

Nếu relaxation optimum quá optimistic so với integer optimum, ratio giữa chúng là integrality gap. Nó giới hạn quality có thể chứng minh bằng simple rounding từ relaxation đó.

Concept này giải thích tại sao “LP bound rất đẹp” chưa đảm bảo approximation tốt nếu gap lớn.

## SAT/SMT/ILP solver như engineering tool

Nếu problem size vừa và constraints phức tạp, modeling vào industrial solver có thể tốt hơn tự viết specialized exponential search.

Solver dùng decades of optimizations: clause learning, propagation, cutting planes, presolve, branching heuristics.

Algorithmic maturity bao gồm biết khi nào **không** nên reimplement solver.

## Exact Cover và Algorithm X

Một số combinatorial problems reduce về Exact Cover. Knuth's Algorithm X + Dancing Links là classic search representation tối ưu remove/restore constraints.

Sudoku có thể encode exact cover.

Điểm học được: right representation có thể làm exponential search practical rất nhiều dù worst-case vẫn exponential.

## Approximate counting và sampling

Hardness không chỉ optimization. Exact counting version của NP-style problems có thể thuộc classes như #P và còn khó hơn decision intuition.

Trong large probabilistic systems, approximate counting/sampling đôi khi practical alternative.

Không cần đi sâu complexity zoo, nhưng nên biết decision/optimization/counting có thể có complexity khác nhau.

## Online vs offline hardness

Một problem offline có toàn input trước; online phải quyết định khi input arrives. Competitive analysis compare online algorithm với offline optimum.

Ví dụ cache replacement, ski-rental-like decisions và online scheduling có different guarantee framework from NP approximation.

Không nên trộn approximation ratio và competitive ratio dù cả hai compare với optimum/reference.

## Lower bounds và impossibility thinking

Một kỹ năng quan trọng là hỏi “có reason nào chứng minh class algorithm này không thể tốt hơn không?”

Examples:

```text
comparison sorting Ω(n log n)
unsorted search Ω(n) comparisons worst case
NP-hardness under standard assumptions
streaming memory lower bounds in advanced settings
```

Lower bound ngăn ta wasting effort tìm optimization bất khả thi trong model hiện tại; thay vào đó ta đổi assumptions/model.

## Recognizing exponential-state problems

Signals thường gặp:

```text
subset of items
assignment of variables
ordering/permutation
partition into groups
visit all vertices exactly once
choose compatible combination with global constraints
```

Nhưng signal không chứng minh NP-hard. Một problem có exponential-looking naive search vẫn có hidden polynomial structure, ví dụ bipartite matching.

Do đó hãy search for flow/matching/matroid/interval/DAG structure trước khi kết luận “phải brute-force”.

## Special cases có thể làm problem dễ

Examples:

```text
general graph -> tree
arbitrary weights -> non-negative
arbitrary clauses -> 2-CNF
arbitrary intervals -> interval graph
general TSP -> metric/geometric special cases
large integer capacity -> small W pseudo-polynomial DP
```

Constraint thường là algorithmic gift.

## Modeling can accidentally create NP-hardness

Một requirement nhỏ như “mỗi task có thể assigned many resources, dependencies, deadlines, setup costs và global budget” có thể biến scheduling thành combinatorial optimization hard.

Product/system design đôi khi nên simplify constraints để allow efficient optimization.

Algorithmic complexity có thể feedback vào requirement design.

## Approximation quality vs system value

Một 2-approx theoretical guarantee có thể không đủ cho business objective; ngược lại heuristic không guarantee nhưng 0.1% gap practical có thể excellent.

Engineering evaluation cần cả:

```text
theoretical guarantee
empirical quality distribution
runtime/tail latency
robustness
explainability
implementation/maintenance cost
```

Theory informs risk; production data informs actual trade-off.

## Anytime algorithms

Một anytime optimizer có thể nhanh chóng tìm feasible solution rồi cải thiện dần, giữ best-so-far và bound gap.

Useful khi latency budget variable: stop ở deadline và trả current solution cùng quality bound nếu available.

Branch-and-bound/modern solvers thường có this behavior.

## Approximation certificate / optimality gap

Nếu có lower bound `LB` và feasible solution cost `UB` cho minimization, gap cho biết distance tới optimum:

\[
LB\le OPT\le UB
\]

Relative gap có thể guide stopping. Đây là stronger engineering signal hơn “solver chạy 10 giây”.

## Common misconceptions

“NP nghĩa non-polynomial” — sai.

“NP-complete nghĩa không solve được” — sai; small/structured instances thường solve exact.

“Reduction direction nào cũng như nhau” — sai; để prove B hard, reduce known-hard A to B.

“Exponential algorithm luôn useless” — sai; parameter nhỏ và meet-in-middle/DP/pruning rất practical.

“Approximation = heuristic” — sai; approximation có formal guarantee.

“Problem NP-hard nên không cần optimize implementation” — sai; exact solver engineering vẫn rất quan trọng khi instances practical.

“P problem luôn fast” — sai; polynomial degree/constants/data scale vẫn có thể quá lớn.

## A reusable decision workflow

Khi một exact problem có vẻ bùng nổ:

```text
1. Viết exact state/search space và constraints.
2. Tìm known polynomial structure: graph, flow, matching, interval, DAG, matroid-like.
3. Kiểm tra constraints có tạo special case dễ hơn không.
4. Ước lượng n/parameter thật.
5. Nếu nhỏ: backtracking, bitmask DP, meet-in-middle, branch-and-bound.
6. Tìm useful parameter k cho FPT approach.
7. Nếu exact quá đắt: xem approximation guarantee nào tồn tại.
8. Nếu guarantee chưa đủ/practical: heuristic hoặc solver + empirical validation.
9. Nếu dùng solver: theo dõi bound/gap, không chỉ runtime.
```

Workflow này tốt hơn reflex “thấy NP-hard -> dùng greedy”.

## Mental Model

> Complexity theory không nói ta phải bỏ cuộc. Nó nói **loại leverage nào còn khả dụng**. Nếu general exact polynomial algorithm chưa biết, ta có thể đổi instance assumptions, exploit small parameter, dùng better exponential decomposition, relax problem, approximate với proof, hoặc dùng heuristic/solver có measured behavior.

Điểm trưởng thành là biết guarantee nào mình đang có và guarantee nào đã chủ động từ bỏ.

Xem tiếp: [Backtracking](./02_recursion_and_backtracking.md), [Dynamic Programming](./05_dynamic_programming.md), [Greedy](./04_greedy_algorithms.md), [Graph Flow & Matching](../03_graphs/08_network_flow_and_matching.md), [Mathematical Toolkit](../00_foundations/04_mathematical_toolkit_for_dsa.md) và [Problem Solving Workflow](../90_connections/02_problem_solving_workflow.md).
