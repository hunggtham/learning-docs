# Abakcus Mathematics Depth Audit — Round 2 (2026-10-04)

## 1. Vì sao cần vòng audit thứ hai?

Vòng đầu tiên đối chiếu taxonomy 13 nhóm của Abakcus với `mathematics/` và bổ sung các khoảng trống rõ nhất từ core undergraduate sang advanced undergraduate: metric/measure analysis, experimental design, statistical learning, abstract algebra nâng cao và number theory nâng cao.

Round 2 không lặp lại phép so sánh theo tên môn. Thay vào đó, nó đọc sâu hơn các textbook được Abakcus giới thiệu và hỏi:

```text
Một textbook có concept nào tạo node mới
trong dependency graph của library không?
```

Nếu textbook chỉ giải thích lại calculus, linear algebra, probability hoặc proof theo cách khác, nó được giữ như further reading nhưng không tạo chapter mới.

Nếu textbook mở ra một bridge có khả năng tái sử dụng xuyên nhiều domain, bridge đó được thêm vào canonical library.

Kết quả Round 2: thêm **6 topic files**, đưa Mathematics library từ **92 → 98 topic files**.

---

## 2. Những gap được xác nhận

### 2.1 Combinatorics: từ counting basics sang generating functions

Existing coverage đã có:

- permutations/combinations;
- inclusion–exclusion;
- pigeonhole;
- recurrence;
- generating-function intuition ngắn.

Nhưng còn thiếu layer biến generating function thành một phương pháp thực sự:

```text
sequence
→ formal power series
→ algebra/convolution
→ coefficient extraction
```

Ngoài ra còn thiếu probabilistic method và một bridge rõ từ group actions sang Burnside/Pólya enumeration.

Chapter mới:

`07_discrete_cs/11_generating_functions_and_advanced_counting.md`

Bổ sung:

- ordinary/formal generating functions;
- convolution;
- solving recurrences bằng generating functions;
- coin-change/partition models;
- probability generating functions;
- exponential generating functions;
- derangements;
- probabilistic method và first-moment method;
- Burnside/Pólya bridge;
- relation với FFT/algorithmic convolution.

Reference ưu tiên:

- Herbert S. Wilf — **generatingfunctionology**, University of Pennsylvania: https://www2.math.upenn.edu/~wilf/gfologyLinked2.pdf
- Mitchel T. Keller, William T. Trotter — **Applied Combinatorics**: https://appliedcombinatorics.org/

---

### 2.2 Graph theory: từ connectivity sang capacity, flow và matching

Existing graph chapter mạnh ở:

- paths/cycles/connectivity;
- trees/MST;
- DAG/topological ordering;
- graph representation;
- graph algorithms.

Nhưng chưa có một treatment riêng cho network capacity và assignment structure.

Chapter mới:

`07_discrete_cs/12_network_flows_matchings_and_min_cut.md`

Bổ sung:

- capacity/conservation;
- residual networks;
- augmenting paths;
- Ford–Fulkerson/Edmonds–Karp idea;
- cuts và optimality certificates;
- max-flow min-cut theorem;
- integrality;
- bipartite matching;
- Hall's theorem;
- min-cost flow;
- vertex capacity;
- edge-disjoint paths;
- LP duality connection;
- system-capacity/bottleneck reasoning.

Reference ưu tiên:

- Keller & Trotter — **Applied Combinatorics**, Network Flows: https://appliedcombinatorics.org/book/s_flowapplications.html

---

### 2.3 Analysis: từ metric/measure sang Banach/Hilbert/operator viewpoint

Round 1 đã bổ sung metric spaces, completeness, uniform convergence, measure và `L^p` intuition. Nhưng một dependency gap vẫn còn:

```text
finite-dimensional linear algebra
→ function spaces
→ operators
→ Fourier/PDE/inverse problems
```

Chapter mới:

`05_calculus/14_normed_banach_hilbert_spaces_and_operators.md`

Bổ sung:

- normed vector spaces;
- Banach spaces;
- `C([a,b])` và `L^p`;
- Hilbert spaces;
- orthogonality/projection trong function spaces;
- infinite-dimensional bases;
- bounded/unbounded operators;
- operator norm;
- spectrum/compact operators;
- Riesz representation intuition;
- weak convergence;
- function-space optimization và regularization.

Reference ưu tiên:

- Lynn H. Loomis, Shlomo Sternberg — **Advanced Calculus**, Harvard: http://people.math.harvard.edu/~shlomo/docs/Advanced_Calculus.pdf

---

### 2.4 Geometry/advanced calculus: từ multivariable calculus sang manifolds

Existing library đã có topology intro, vector calculus, tensors và Jacobian/Hessian. Nhưng chưa có node giải thích vì sao calculus có thể hoạt động trên curved spaces mà không phụ thuộc global coordinates.

Chapter mới:

`05_calculus/15_manifolds_differential_forms_and_generalized_stokes.md`

Bổ sung:

- manifolds/charts/atlases;
- tangent/cotangent spaces;
- differential như linear map giữa tangent spaces;
- vector fields;
- differential forms;
- wedge product/exterior derivative;
- pullback;
- integration on manifolds;
- generalized Stokes theorem;
- closed vs exact forms;
- de Rham cohomology intuition;
- Lie-group bridge;
- Riemannian metric/geodesic intuition;
- optimization on manifolds.

Reference ưu tiên:

- Loomis & Sternberg — **Advanced Calculus**, phần differentiable manifolds và exterior calculus.

---

### 2.5 Differential equations: từ stability intro sang bifurcation và chaos

Existing ODE chapter đã có:

- equilibria;
- phase lines/planes;
- systems;
- eigenvalue stability;
- nonlinear linearization;
- conservation laws.

Nhưng chưa trả lời câu hỏi:

```text
Khi parameter thay đổi,
qualitative behavior của system đổi như thế nào?
```

Chapter mới:

`05_calculus/16_dynamical_systems_bifurcations_and_chaos.md`

Bổ sung:

- discrete dynamical systems;
- logistic map;
- local stability;
- saddle-node/transcritical/pitchfork/Hopf bifurcations;
- limit cycles;
- bifurcation diagrams;
- period doubling;
- deterministic chaos;
- Lyapunov exponents;
- attractors/basins;
- conjugacy;
- symbolic dynamics/topological entropy intuition;
- Poincaré sections;
- Lyapunov functions;
- bridges sang optimization/control.

Reference ưu tiên:

- Shlomo Sternberg — **Dynamical Systems**, Harvard: https://people.math.harvard.edu/~shlomo/docs/dynamical_systems.pdf

---

### 2.6 Applied mathematics: strategic interaction và mechanism design

Optimization hiện tại chủ yếu giả định một decision maker hoặc một centrally defined objective. Catalog Abakcus có open game-theory material làm lộ một gap riêng:

```text
optimization
→ multiple strategic agents
→ mutual best responses
→ equilibrium
→ incentive design
```

Chapter mới:

`09_connections/08_game_theory_strategy_equilibrium_and_incentives.md`

Bổ sung:

- strategy/action/payoff;
- best response/dominance;
- Prisoner's Dilemma;
- Nash equilibrium;
- Pareto efficiency;
- zero-sum games;
- mixed strategies/minimax;
- coordination/congestion;
- price of anarchy;
- repeated/sequential games;
- subgame-perfect equilibrium;
- Bayesian games;
- mechanism design/incentive compatibility;
- auction intuition;
- stable matching distinction;
- evolutionary/security/platform game-theory applications.

Reference ưu tiên:

- Jennifer Firkins Nordstrom — **Introduction to Game Theory: a Discovery Approach**: https://jlmartin.ku.edu/courses/math105-F11/Nordstrom-GameTheory.pdf
- Open textbook metadata: https://textbooks.aimath.org/textbooks/approved-textbooks/nordstrom/

---

## 3. Những gì vẫn cố ý không thêm

### Không tạo thêm một proof course

Existing `00_foundations/01_logic_and_proof.md` đã là canonical prerequisite cho propositions, quantifiers, direct/contradiction/contrapositive proof, induction, invariants và counterexamples. Các proof textbooks trong Abakcus hữu ích cho exercises và alternative exposition, nhưng không tạo node dependency mới.

### Không tạo thêm một calculus sequence

Single-variable/multivariable/vector calculus, series/Taylor và numerical calculus đã có. Advanced Calculus chỉ được dùng để nhận ra **function-space** và **manifold** bridges còn thiếu.

### Không tạo một ODE textbook thứ hai

Các methods cơ bản đã có. Round 2 chỉ thêm nonlinear qualitative layer: bifurcation/chaos.

### Không tạo một graph-theory chapter khác

Graph fundamentals đã đủ mạnh. Chỉ thêm flow/matching vì objective, constraints và duality khác về bản chất so với connectivity/MST/shortest paths.

### Không đưa game theory vào `economics/` như canonical owner

Game theory là bridge toán học chung cho economics, algorithms, distributed systems, security và mechanism design. Canonical chapter nằm ở `mathematics/09_connections/`, còn domain-specific consequences vẫn thuộc library economics/software/security tương ứng.

---

## 4. Dependency graph sau Round 2

Các bridge mới có thể đọc như sau.

### Analysis / geometry route

```text
Linear Algebra
→ Real Analysis
→ Metric / Measure
→ Banach & Hilbert Spaces
→ Operators
→ Fourier / PDE / inverse problems
```

```text
Multivariable Calculus
+ Topology
+ Tensor / Multilinear Algebra
→ Manifolds
→ Differential Forms
→ Generalized Stokes
→ Differential Geometry
```

### Discrete route

```text
Counting
→ Recurrence
→ Generating Functions
→ Probabilistic Method / Pólya
```

```text
Graph Theory
→ Network Flow
→ Matching
→ LP Duality / Assignment / Operations Research
```

### Systems route

```text
Recurrence + ODE
→ Stability
→ Bifurcation
→ Chaos
→ Control / optimization dynamics
```

### Strategic route

```text
Probability + Optimization
→ Best Response
→ Nash / Minimax
→ Repeated & Bayesian Games
→ Mechanism Design
```

---

## 5. Coverage conclusion

Sau two-pass Abakcus audit, Mathematics library có **98 topic files**.

Điểm quan trọng không phải con số 98 mà là dependency graph hiện đã có continuous path qua phần lớn undergraduate mathematics và nhiều advanced bridges:

```text
foundations
→ algebra / functions / geometry
→ linear algebra / calculus / probability
→ analysis / algebra / number theory / discrete math
→ optimization / statistical learning
→ functional analysis / manifolds / dynamical systems
→ systems / AI / finance / strategic interaction
```

Từ thời điểm này, nguồn textbook mới nên được dùng chủ yếu cho ba mục đích:

1. tìm missing exercises/problem-solving patterns;
2. phát hiện một dependency bridge thật sự chưa tồn tại;
3. enrich examples/counterexamples/failure modes trong chapter hiện có.

Không nên tiếp tục tăng số chapter chỉ vì một textbook có chapter title khác.
