# Quality Audit — Round 10: geometry, probability, discrete structures and numerical optimization

Round 10 tiếp tục chiến lược **quality over chapter count**. Mathematics Knowledge Library vẫn giữ nguyên **87 topic**; không thêm chapter mới chỉ để tăng coverage.

Mục tiêu của round này là nâng các chapter vẫn còn ngắn đáng kể so với các phần đã rewrite ở Round 5–9, đặc biệt các chapter nằm giữa những dependency chains quan trọng.

## Tiêu chí chọn chapter

Round 10 ưu tiên file có một hoặc nhiều dấu hiệu:

```text
size/depth thấp hơn rõ so với chapter lân cận
nhiều downstream concepts phụ thuộc vào nó
formalism đúng nhưng intuition/proof idea còn ngắn
connections mới chỉ được nhắc tên
assumptions/failure modes chưa đủ
chapter là bridge giữa hai domain lớn
```

Chuẩn viết vẫn theo `EDITORIAL_STANDARD.md`:

```text
intuition
→ problem structure
→ formalism
→ derivation / proof idea
→ worked examples
→ assumptions / failure modes
→ knowledge connections
→ mental model
```

## Batch 1 — Geometry, Harmonics và Vector Calculus

Commit:

```text
c6ccfad65f21af681f89f30fcf8530297e3225f3
```

### `03_geometry_trigonometry/06_circles_conics_and_loci.md`

Bản cũ đã đúng về locus, standard forms và quadratic forms nhưng còn tương đối ngắn.

Bản mới tổ chức learning flow:

```text
distance constraint
→ locus
→ circle / parabola / ellipse / hyperbola
→ eccentricity
→ general quadratic equation
→ symmetric quadratic form
→ eigenbasis / coordinate rotation
→ Hessian / covariance ellipse / optimization
```

Các phần được tăng sâu:

- gradient như normal của implicit curve;
- focus/directrix derivation của parabola;
- eccentricity như unified conic viewpoint;
- `B²-4AC` cùng limitations/degenerate cases;
- conic equation dưới dạng `x^TQx+d^Tx+F=0`;
- diagonalization giải thích việc rotate axes;
- implicit vs parametric representation;
- covariance ellipse, Mahalanobis geometry và quadratic constraints.

### `03_geometry_trigonometry/07_trigonometric_identities_equations_and_harmonics.md`

Bản mới tránh biến identities thành collection formulas.

Learning dependency:

```text
unit circle
→ rotation matrix
→ angle addition
→ derived identities
→ periodic equations
→ amplitude/frequency/phase
→ harmonic oscillator
→ complex exponential
→ orthogonal harmonics
→ Fourier viewpoint
```

Các phần mới quan trọng:

- identities như consequences của rotation composition;
- product-to-sum như frequency mixing;
- inverse trig principal branches;
- phase vs time delay;
- state-space view của oscillator;
- damping/forcing/resonance connection;
- orthogonality của harmonics;
- aliasing/Nyquist intuition;
- Fourier features trong signal/AI.

### `05_calculus/09_vector_calculus.md`

Bản mới chuyển từ glossary của gradient/divergence/curl thành chapter **local-to-global calculus**.

Learning flow:

```text
scalar/vector field
→ gradient
→ divergence
→ curl
→ line/surface integral
→ Green/Stokes/divergence theorem
→ continuity equation
→ conservation law
```

Các phần tăng sâu:

- Cauchy–Schwarz proof idea cho steepest gradient;
- gradient vuông góc level set;
- divergence như flux density;
- curl qua rigid rotation example;
- local curl-free vs global conservative và topology;
- scalar vs vector line integrals;
- continuity equation;
- generalized Fundamental-Theorem pattern;
- coordinate Jacobian;
- Maxwell/fluid/AI connections;
- singularity/domain caveat trong flux theorem.

## Batch 2 — Combinatorics và Multivariate Probability

Commit:

```text
d2235a5a8007b362027ed4cb611227874428c59d
```

### `06_probability_statistics/00_counting_and_combinatorics.md`

Bản mới chuyển từ formula overview sang cấu trúc của finite possibility spaces.

Learning flow:

```text
sum/product rules
→ permutations/combinations
→ symmetry and quotienting order
→ binomial coefficients
→ inclusion-exclusion
→ complement counting
→ bijections
→ recurrence/generating functions
→ asymptotic counting
→ search-space explosion
```

Các phần mới:

- khi product rule không áp dụng trực tiếp;
- combinatorial proofs/Pascal identity;
- stars-and-bars assumptions;
- generalized pigeonhole principle;
- bijection proofs;
- recurrence counting;
- generating-function intuition;
- Stirling/asymptotic growth;
- hypergeometric vs binomial;
- AI/coding search-space connections.

### `06_probability_statistics/08_covariance_multivariate_probability_and_gaussian.md`

Learning flow mới:

```text
joint distribution
→ marginal / conditional
→ covariance / correlation
→ covariance matrix
→ quadratic form
→ PCA geometry
→ Gaussian ellipsoids
→ linear/nonlinear uncertainty propagation
```

Các phần tăng sâu:

- covariance matrix PSD proof idea;
- variance of linear combination;
- whitening;
- Jacobian-based covariance propagation;
- conditional Gaussian intuition;
- zero covariance vs independence;
- singular covariance as lower-dimensional support;
- robustness/heavy-tail caveats;
- portfolio variance worked example.

### `06_probability_statistics/09_common_distributions_and_when_they_arise.md`

Bản mới tổ chức distributions theo **mechanism + support + assumptions**, không theo bảng formula.

Đã làm sâu:

```text
Bernoulli / indicator
Binomial / Hypergeometric
Geometric / Negative Binomial
Poisson / Exponential / Gamma
Uniform
Gaussian / Student t / Chi-square / F
Beta / Dirichlet / Multinomial
Log-normal / heavy-tail caution
```

Các connections mới:

- Poisson rare-event limit;
- hazard rate;
- overdispersion;
- conjugacy;
- approximation relations giữa distributions;
- support-based sanity checking;
- likelihood/loss choices trong AI;
- Gaussian-tail limitations trong Finance.

## Batch 3 — Trees, Orders, Lattices và Information Theory

Commit:

```text
fdcec8f394fd93eb9250bdfc2932dfe3e37d11a8
```

### `07_discrete_cs/05_trees_posets_and_lattices.md`

Bản mới nối ba topics thành một learning chain duy nhất:

```text
tree
→ rooted hierarchy
→ DAG
→ partial order
→ Hasse diagram
→ topological sort
→ lattice
→ fixpoint computation
```

Các phần tăng sâu:

- equivalent characterizations của tree;
- traversal và height reasoning;
- BST vs heap;
- MST cut intuition;
- minimal/maximal vs minimum/maximum;
- chains/antichains;
- lattice meet/join;
- compiler dataflow analysis;
- fixed-point reasoning;
- CRDT/join-semilattice connection.

### `07_discrete_cs/06_information_theory_and_coding.md`

Bản mới mở rộng thành full dependency chain:

```text
probability
→ self-information
→ entropy
→ compression
→ conditional/joint entropy
→ mutual information
→ KL/cross-entropy
→ channel capacity
→ error-correcting coding
```

Các phần tăng sâu:

- why logarithm;
- entropy vs variance;
- Huffman vs arithmetic coding;
- Kraft inequality;
- data-processing inequality;
- entropy rate;
- KL as extra log-loss/code cost;
- cross-entropy/negative log-likelihood connection;
- binary symmetric channel capacity;
- Hamming geometry;
- linear codes over `GF(2)`;
- feature selection/information bottleneck/perplexity caveats.

## Batch 4 — Constrained Optimization và Numerical Solvers

Commit:

```text
36aff1d613c93274730e472c3e1ea312b3427408
```

### `08_optimization_numerical/03_constrained_optimization_lagrange_and_kkt.md`

Learning flow mới:

```text
feasible set
→ feasible/tangent directions
→ equality Lagrange condition
→ inequality active set
→ KKT
→ constraint qualifications
→ convex sufficiency
→ duality
→ penalty/barrier/projected methods
```

Các phần mới:

- Lagrange geometry từ tangent/normal spaces;
- multiplier units/sensitivity;
- active/slack worked example;
- KKT assumptions;
- Slater condition intuition;
- weak/strong duality;
- projection connection;
- projected gradient;
- penalty vs barrier;
- L1 geometry/sparsity;
- portfolio/resource-allocation examples;
- second-order constrained reasoning.

### `08_optimization_numerical/04_root_finding_interpolation_and_numerical_linear_algebra.md`

Bản mới tách rõ ba layers:

```text
root finding
interpolation / approximation
linear-system computation
```

và đặt chúng dưới common framework:

```text
convergence + conditioning + stability + error control
```

Các phần tăng sâu:

- bisection guarantee/failure regime;
- Newton local quadratic convergence + failure modes;
- secant/hybrid methods;
- contraction/fixed-point view;
- stopping criteria;
- interpolation error formula;
- Runge phenomenon + Chebyshev nodes;
- splines;
- LU/QR/Cholesky assumptions;
- sparse/direct/iterative solvers;
- residual vs error;
- condition number;
- backward stability;
- catastrophic cancellation;
- preconditioning;
- numerical eigenvalue methods.

## Depth balance sau Round 10

Sau Round 10, các dependency chains sau đã tương đối đồng đều về depth:

```text
Geometry → Trigonometry → Fourier/vector-field connections
Counting → Probability → Multivariate Gaussian → Statistics
Graph → Tree/Order/Lattice → CS semantics
Probability → Entropy → Coding/ML losses
Optimization → Constraints/KKT → Numerical computation
```

Coverage không có major gap mới. Vì vậy các round tiếp theo vẫn nên **rewrite/chỉnh dependency**, không nên tăng topic count một cách cơ học.

## Priority hợp lý cho Round 11

Các chapter tiếp theo đáng audit theo depth:

```text
03_geometry_trigonometry/08_topology_continuity_connectivity.md
05_calculus/10_partial_differential_equations_and_fields_intro.md
06_probability_statistics/10_likelihood_mle_map_and_model_selection.md
06_probability_statistics/11_stochastic_processes_markov_chains_and_time_series.md
07_discrete_cs/07_automata_formal_languages_and_computability.md
07_discrete_cs/08_groups_rings_fields_and_algebraic_structures.md
08_optimization_numerical/05_linear_programming_duality_and_simplex.md
09_connections/* các chapter còn ngắn hơn standard
```

Nhưng trước khi rewrite cần audit content thực tế: file size không phải criterion duy nhất. Một chapter ngắn nhưng conceptually complete không cần kéo dài chỉ để đồng đều số dòng.

## Kết luận

Round 10 không thêm topic. Nó làm sâu **10 canonical chapters** và giữ learning flow hiện có.

Nguyên tắc tiếp tục giữ nguyên:

> Không tối ưu library theo số file hoặc số dòng. Tối ưu theo khả năng người đọc hiểu bản chất, assumptions, derivations, failure modes và connections mà không phải ghép kiến thức rời rạc từ nơi khác.
