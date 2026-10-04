# Abakcus Mathematics Depth Audit — Round 2 (2026-10-04)

## 1. Mục tiêu của Round 2

Round 1 đối chiếu 13 nhóm textbook trên Abakcus với `mathematics/` và bổ sung các gap rõ nhất từ core undergraduate sang advanced undergraduate. Round 2 không lặp lại taxonomy theo tên môn; nó đọc sâu hơn các textbook/reference được Abakcus dẫn tới và hỏi:

```text
Một nguồn mới có tạo ra dependency node thực sự còn thiếu không?
```

Nếu nguồn chỉ giải thích lại calculus, linear algebra, probability, proof hoặc ODE bằng exposition khác, nó được giữ làm further reading chứ không tạo chapter mới. Nếu nó mở một bridge có khả năng tái sử dụng xuyên nhiều domain, bridge đó mới được đưa vào canonical library.

### Bookkeeping correction

Audit trước ghi **92 topic files**, nhưng `09_connections/07_probability_calibration_decision_and_risk.md` đã tồn tại và bị bỏ khỏi README/count. Vì vậy baseline đúng sau Round 1 là **93 topics**.

Round 2 thêm **6 topic files**, đưa Mathematics library lên **99 topic files**.

---

## 2. Sáu gap được xác nhận

### 2.1 Generating functions & advanced counting

Existing coverage đã có permutations/combinations, inclusion–exclusion, pigeonhole, recurrence và generating-function intuition ngắn, nhưng chưa có một method hoàn chỉnh từ sequence → formal series → algebra → coefficient extraction.

Chapter mới:

`07_discrete_cs/11_generating_functions_and_advanced_counting.md`

Coverage mới:

- ordinary/formal generating functions;
- convolution và product rule cho combinatorial composition;
- recurrence → rational generating function;
- coin-change và integer partitions;
- probability/exponential generating functions;
- derangements;
- probabilistic method và first-moment method;
- Burnside/Pólya bridge;
- FFT/convolution connection.

References:

- Herbert S. Wilf — *generatingfunctionology*, University of Pennsylvania.
- Mitchel T. Keller, William T. Trotter — *Applied Combinatorics*.

### 2.2 Network flows, matching & min-cut

Existing graph coverage mạnh ở paths, cycles, connectivity, trees, MST, DAG và graph algorithms, nhưng chưa có capacity/conservation/assignment layer.

Chapter mới:

`07_discrete_cs/12_network_flows_matchings_and_min_cut.md`

Coverage mới:

- flow capacity và conservation;
- residual networks và augmenting paths;
- Ford–Fulkerson/Edmonds–Karp idea;
- cuts và optimality certificates;
- max-flow min-cut theorem;
- integrality;
- bipartite matching và Hall's theorem;
- min-cost flow;
- vertex capacity, edge-disjoint paths;
- LP duality và production-capacity reasoning.

Reference chính:

- Keller & Trotter — *Applied Combinatorics*, Network Flows and Combinatorial Applications of Network Flows.

### 2.3 Banach/Hilbert spaces & operators

Round 1 đã thêm metric spaces, completeness, uniform convergence, measure và `L^p` intuition, nhưng vẫn còn gap:

```text
finite-dimensional linear algebra
→ function spaces
→ operators
→ Fourier / PDE / inverse problems
```

Chapter mới:

`05_calculus/14_normed_banach_hilbert_spaces_and_operators.md`

Coverage mới:

- normed/Banach spaces;
- `C([a,b])` và `L^p`;
- Hilbert spaces;
- infinite-dimensional projection/orthogonality;
- orthonormal expansions và Parseval;
- bounded/unbounded operators;
- operator norm, spectrum và compact operators;
- Riesz representation intuition;
- weak convergence;
- function-space optimization/regularization.

Reference chính:

- Lynn H. Loomis, Shlomo Sternberg — *Advanced Calculus*.

### 2.4 Manifolds, differential forms & generalized Stokes

Existing library đã có topology intro, vector calculus, tensor/multilinear algebra và Jacobian/Hessian nhưng chưa có intrinsic calculus trên curved spaces.

Chapter mới:

`05_calculus/15_manifolds_differential_forms_and_generalized_stokes.md`

Coverage mới:

- manifolds, charts, atlases;
- tangent/cotangent spaces;
- differential như linear map giữa tangent spaces;
- vector fields;
- differential forms, wedge product, exterior derivative;
- pullback và integration on manifolds;
- generalized Stokes theorem;
- closed vs exact forms và de Rham intuition;
- Lie-group bridge;
- Riemannian metric/geodesic intuition;
- optimization on manifolds.

Reference chính:

- Loomis & Sternberg — *Advanced Calculus*, phần differentiable manifolds và exterior calculus.

### 2.5 Dynamical systems, bifurcations & chaos

Existing ODE coverage đã có equilibrium, phase lines/planes, systems, eigenvalue stability, nonlinear linearization và conservation laws. Gap còn lại là qualitative change khi parameter đổi và deterministic unpredictability.

Chapter mới:

`05_calculus/16_dynamical_systems_bifurcations_and_chaos.md`

Coverage mới:

- discrete dynamical systems và logistic map;
- fixed-point stability;
- saddle-node/transcritical/pitchfork/Hopf bifurcations;
- limit cycles;
- bifurcation diagrams và period doubling;
- deterministic chaos;
- Lyapunov exponents;
- attractors/basins;
- conjugacy, symbolic dynamics và entropy intuition;
- Poincaré sections;
- Lyapunov functions;
- bridges sang optimization/control.

Reference chính:

- Shlomo Sternberg — *Dynamical Systems*.

### 2.6 Game theory, equilibrium & incentives

Optimization hiện tại chủ yếu giả định một decision maker hoặc centrally defined objective. Một gap riêng xuất hiện khi multiple agents phản ứng lẫn nhau.

Chapter mới:

`09_connections/08_game_theory_strategy_equilibrium_and_incentives.md`

Coverage mới:

- strategy/action/payoff;
- best response và dominant strategy;
- Prisoner's Dilemma;
- Nash equilibrium và Pareto efficiency;
- zero-sum games, mixed strategies và minimax;
- coordination/congestion và price of anarchy;
- repeated/sequential games;
- subgame-perfect equilibrium;
- Bayesian games;
- mechanism design/incentive compatibility;
- auction intuition;
- stable matching distinction;
- evolutionary/security/platform applications.

Reference chính:

- Jennifer Firkins Nordstrom — *Introduction to Game Theory: a Discovery Approach*.

---

## 3. Những gì cố ý không thêm

### Không tạo thêm một proof course

`00_foundations/01_logic_and_proof.md` đã là canonical prerequisite cho propositions, quantifiers, direct/contradiction/contrapositive proof, induction, invariants và counterexamples. Các proof textbooks mới hữu ích cho exercises và alternative exposition nhưng không tạo dependency node mới.

### Không tạo thêm một calculus sequence

Single-variable, multivariable, vector calculus, series/Taylor và numerical calculus đã có. *Advanced Calculus* chỉ được dùng để nhận ra hai bridge thật sự thiếu: function spaces/operators và manifolds/exterior calculus.

### Không tạo một ODE textbook thứ hai

Methods cơ bản đã có. Round 2 chỉ thêm nonlinear qualitative layer: bifurcation, limit cycles và chaos.

### Không tạo một graph-theory chapter thứ hai

Graph fundamentals đã đủ mạnh. Flow/matching được tách vì objective, constraints, residual structure và duality khác về bản chất với connectivity/MST/shortest paths.

### Không đưa game theory vào `economics/` làm canonical owner

Game theory là mathematical bridge cho economics, algorithms, distributed systems, security và mechanism design. Canonical mathematical chapter nằm ở `mathematics/09_connections/`; domain-specific interpretation vẫn thuộc owner tương ứng.

---

## 4. Dependency routes sau Round 2

### Analysis / geometry

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

### Discrete mathematics

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

### Nonlinear systems

```text
Recurrence + ODE
→ Stability
→ Bifurcation
→ Chaos
→ Control / optimization dynamics
```

### Strategic systems

```text
Probability + Optimization
→ Best Response
→ Nash / Minimax
→ Repeated & Bayesian Games
→ Mechanism Design
```

---

## 5. Kết luận coverage

Sau two-pass Abakcus audit, Mathematics library có **99 canonical topic files**.

Dependency graph hiện có continuous paths qua phần lớn undergraduate mathematics và nhiều advanced bridges:

```text
foundations
→ algebra / functions / geometry
→ linear algebra / calculus / probability
→ analysis / algebra / number theory / discrete math
→ optimization / statistical learning
→ functional analysis / manifolds / dynamical systems
→ systems / AI / finance / strategic interaction
```

Từ đây, các textbook collections mới nên chủ yếu được dùng để:

1. tìm missing exercises/problem-solving patterns;
2. phát hiện dependency bridge thực sự chưa tồn tại;
3. enrich examples, counterexamples, derivations và failure modes trong chapter hiện có.

Không nên tiếp tục tăng số chapter chỉ vì taxonomy của nguồn khác taxonomy canonical của repository.
