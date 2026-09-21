# Coverage & Depth Audit — Mathematics Knowledge Library

## Mục tiêu của audit

Mathematics Knowledge Library hiện đã có coverage rộng từ school mathematics tới foundational university mathematics, Computer Science, AI/Data, numerical mathematics, optimization, signal/control và quantitative reasoning. Vì vậy audit hiện tại **không dùng số lượng chapter làm mục tiêu chính**.

Tiêu chí mới là **depth + learning dependency**: người đọc có hiểu vấn đề trước khi gặp formalism không, formula có được giải thích meaning/assumptions không, theorem/rule có proof idea không, examples có đủ để transfer reasoning không, và các chapter có nối với nhau thành knowledge graph hay vẫn giống collection rời rạc.

Library vẫn giữ **87 topic files**; Round 6 không tăng chapter count. Thay đổi chính là rewrite các node có dependency centrality cao nhưng depth thấp hơn đáng kể so với phần còn lại.

## Chuẩn đánh giá depth

Một chapter được xem là đủ sâu trong scope khi phần lớn các câu hỏi sau có câu trả lời ngay trong chapter:

- Concept giải quyết vấn đề gì?
- Intuition nào nên hình thành trước definition?
- Formal definition/theorem xuất hiện sau intuition như thế nào?
- Formula đến từ đâu và từng term có meaning gì?
- Assumptions/domain validity là gì?
- Có proof idea hoặc derivation phù hợp không?
- Có worked example, counterexample hoặc failure mode không?
- Concept liên hệ gì với prerequisite và downstream chapters?
- Có connection thực sự về structure với CS, Physics, AI hoặc Finance không?
- Mental Model có giúp reasoning transfer không?
- Common Misconceptions có giải thích vì sao lỗi tư duy xuất hiện không?

File [`EDITORIAL_STANDARD.md`](./EDITORIAL_STANDARD.md) là chuẩn biên soạn canonical cho các vòng rewrite tiếp theo.

## Domain-depth audit hiện tại

| Domain | Depth hiện tại | Audit learning dependency |
|---|---|---|
| Mathematical thinking | Mạnh | `00_foundations/00_mathematical_thinking.md` đã đủ vai trò entry point: modeling, abstraction, invariants, dimensions, approximation và first-principles reasoning. |
| Logic | Khá mạnh | Propositions, implication, quantifiers, contrapositive và reasoning structure đã đủ cho discrete mathematics/proof. Có thể mở rộng formal logic sau này nhưng chưa phải bottleneck. |
| Proof | Khá mạnh | Direct proof, contradiction, induction, counterexample và invariant đã có. Proof ideas được dùng downstream trong algorithms/number theory. |
| Sets | Khá mạnh | Membership, subset, operations, Cartesian product và cardinality đủ làm prerequisite. |
| Relations | Khá mạnh | Relations, equivalence relation và relation-as-subset-of-product đã có connection sang databases/discrete structures. |
| Mappings | Mạnh | Functions/mappings đã được rewrite sâu ở Round 5; injective/surjective/bijective, composition, inverse và information-preservation đã rõ. |
| Number systems | Khá mạnh | Natural/integer/rational/real/complex, positional systems và floating-point motivation đã có. |
| Arithmetic | **Đã nâng mạnh Round 6** | Ratio/rate/proportion/percentage trước đây mỏng; hiện đã nối denominator reasoning, percentage points, weighted averages, geometric growth, finance returns, Simpson-style aggregation và units. |
| Algebra | Trung bình-khá | Algebraic language và rational expressions ổn; equations/inequalities, powers/logarithms và polynomials vẫn ngắn hơn các chapter mới và là candidate Round 7. |
| Functions | Mạnh | Function concept và exponential/logarithmic models đã rewrite; composition/inverse, recurrence, parametric/polar/implicit tạo learning flow tốt. |
| Geometry | **Đã nâng một phần Round 6** | Pythagorean/distance và scaling laws đã rewrite sâu. Coordinate geometry và transformations/symmetry vẫn là các file tương đối ngắn cần ưu tiên tiếp. |
| Trigonometry | Mạnh | Round 5 đã chuyển từ SOH-CAH-TOA sang unit-circle/rotation/radian/harmonics/Fourier viewpoint. |
| Linear algebra | **Đã nâng mạnh Round 6** | Matrices, linear transformations và least squares/SVD trước đây là major depth gap. Ba chapter đã rewrite với rank/null-space, basis dependence, projection, conditioning, QR/SVD, pseudoinverse, regularization và applications. |
| Calculus | **Đã nâng mạnh Round 5–6** | Limits đã rewrite Round 5; derivatives, derivative applications và multivariable calculus đã rewrite Round 6; integrals/ODE đã sâu từ Round 4. Calculus core hiện cân bằng hơn với analysis. |
| Real analysis | Mạnh trong scope | Completeness, Cauchy/convergence, compactness, uniform convergence và rigorous calculus bridge đã đủ cho current library. |
| Complex analysis | Mạnh trong scope | Complex derivative, Cauchy–Riemann, contour integration, residues và transform connections đã có. |
| Probability | **Đã nâng mạnh Round 6** | Probability foundations đã rewrite: sample-space modeling, conditional probability, Bayes/base-rate, independence/conditional independence, expectation, calibration và common-cause dependence. |
| Statistics | Khá mạnh | Sampling, estimation, confidence intervals, hypothesis testing, regression, MLE/MAP, Bayesian inference và multivariate probability đã có. Descriptive/inferential overview và regression chapter vẫn có thể polish sau nhưng không phải missing dependency. |
| Discrete mathematics | Khá mạnh | Logic/induction, Boolean algebra, number theory, trees/posets/lattices, automata và algebraic structures đã đủ broad flow. |
| Graph theory | Mạnh | Round 5 đã rewrite thành modeling + traversal + shortest path + SCC + matching + coloring + flow/cut + Laplacian/random walk connections. |
| Information theory | Mạnh trong scope | Entropy, coding, cross-entropy/KL và probability connection đã có; không cần thêm chapter mới hiện tại. |
| Numerical methods | Mạnh sau Round 5 | Numerical error, conditioning, stability, floating point, root finding, interpolation, numerical LA, ODE stability và mixed precision đã được nâng sâu. |
| Optimization | **Đã nâng mạnh Round 6** | General optimization chapter đã rewrite từ modeling → convexity → gradients → constraints/KKT → duality → discrete/robust/multi-objective optimization. |
| Dynamic programming | Mạnh trong scope | Bellman principle, MDP/value/policy iteration, optimal control bridge đã có riêng. |
| Control | Khá mạnh | ODE/eigenvalue stability + Laplace/Z-transform + Bellman/optimal control tạo dependency path tốt. Control chuyên ngành sâu hơn hiện được xem là optional expansion, không phải prerequisite gap. |
| Fourier/Laplace | Mạnh trong scope | Harmonics → Fourier/frequency → Laplace/Z-transform → ODE/control dependency đã rõ. |
| Mathematical connections | Mạnh | Rate/change/accumulation, distance/projection, uncertainty/information, AI/Data/Software, Finance/Life, Fourier và dynamic systems đã có cross-domain chapters. |

## Round 6 — Batch 1: Linear Algebra core

Commit batch tập trung ba files:

- `04_vectors_linear_algebra/01_matrices_and_linear_systems.md`
- `04_vectors_linear_algebra/02_linear_transformations.md`
- `04_vectors_linear_algebra/05_least_squares_svd_and_decompositions.md`

### Matrices and Linear Systems

Bản cũ đúng concept nhưng chủ yếu liệt kê matrix notation, Gaussian elimination, determinant và inverse. Bản mới tổ chức learning flow:

```text
constraints / transformations
→ Ax=b
→ column-space viewpoint
→ row operations as reversible equivalence
→ rank / nullity / consistency
→ invertibility equivalences
→ determinant as volume collapse
→ conditioning
→ least-squares dependency.
```

Thêm worked portfolio-constraint example, explicit distinction giữa exact algebra và numerical solving, cùng connections sang graphics, ML, circuits và sparse simulation.

### Linear Transformations

Bản mới đặt **superposition** trước formalism. Matrix được giải thích như coordinate representation của an operator, không phải operator itself. Kernel được đọc như information-loss subspace, image như reachable outputs, rank-nullity như accounting of degrees of freedom.

Chapter cũng nối linearity với local Jacobian linearization, eigenbasis, physics superposition và neural-network representations.

### Least Squares, SVD and Decompositions

Bản mới derive normal equations từ orthogonal projection, thêm worked line-fit example, giải thích vì sao normal equations không phải default numerical solver, và nối QR/SVD với conditioning.

Pseudoinverse, regularization, low-rank approximation, PCA, finance factor models và AI low-rank parameterization được thêm như consequences của cùng geometry, không phải application list rời rạc.

## Round 6 — Batch 2: Calculus core

Files:

- `05_calculus/01_derivatives.md`
- `05_calculus/02_derivative_applications.md`
- `05_calculus/04_multivariable_calculus.md`

### Derivatives

Derivative được rewrite quanh idea **local response / local linear model** thay vì symbolic rules. Power rule, product rule và chain rule đều có derivation/proof idea. Units, error propagation, elasticity, implicit differentiation, numerical differentiation và automatic differentiation được nối bằng chung sensitivity structure.

### Derivative Applications

Critical points, first/second derivative tests và inflection được giải thích bằng sign/curvature/Taylor reasoning. Optimization section nhấn mạnh objective + feasible domain + boundaries thay vì “set derivative = 0”.

Newton method được derive từ tangent approximation; Physics equilibrium, AI gradients và Finance Greeks được dùng như structural connections.

### Multivariable Calculus

Partial derivatives chỉ là entry point; chapter hiện lấy Jacobian/local-linear-map làm central idea. Gradient direction được derive bằng Cauchy–Schwarz, Hessian eigenvalues được nối với conditioning, Lagrange multiplier được derive từ normals/tangent space, và Jacobian determinant được giải thích như local volume scaling.

Probability density transforms, backpropagation, physical fields và multi-factor finance sensitivity được nối cùng dependency path.

## Round 6 — Batch 3: Probability, Complexity and Optimization

Files:

- `06_probability_statistics/01_probability_foundations.md`
- `06_probability_statistics/03_random_variables_and_distributions.md`
- `07_discrete_cs/01_algorithms_complexity_and_logarithms.md`
- `08_optimization_numerical/00_optimization.md`

### Probability Foundations

Bản mới đặt event definition + information set + model assumptions trước formulas. Conditional probability được giải thích như renormalization khi universe thu hẹp. Bayes được derive từ hai factorization của joint event; worked medical-test example làm rõ base-rate effect.

Independence/conditional independence, calibration, common-cause failures và expectation/risk được thêm để chapter usable cho AI, engineering và finance.

### Random Variables and Distributions

Random variable được giữ đúng definition là mapping từ outcome space sang numbers. PMF/density/CDF được tổ chức như representations của probabilistic law, không phải các formulas tách rời.

Chapter bổ sung indicator variables, expectation/variance reasoning, distribution assumptions, joint/marginal/conditional distributions, covariance limits, Jacobian transformation, quantiles/tails và links với likelihood losses.

### Algorithmic Complexity

Bản mới bắt đầu từ **cost model**. Big-O/Theta/Omega được giải thích như scaling statements; logarithm được derive từ repeated multiplicative shrinkage.

Binary search, merge sort, lower bound cho comparison sorting, amortized dynamic arrays, representation-sensitive graph complexity, DP và practical hardware caveats được nối vào cùng growth-accounting model.

### Optimization

Bản mới nhấn mạnh objective/feasible set trước algorithms. Convexity có proof idea cho global guarantee, gradient descent được derive từ local linear model, Lagrange/KKT/duality được giải thích bằng geometry và shadow prices.

Discrete optimization, Bellman structure, Pareto trade-offs, robust optimization, AI objective misspecification và finance estimation risk được thêm để tạo engineering judgment.

## Round 6 — Batch 4: Arithmetic and Geometry bridges

Files:

- `01_algebra/02_ratio_proportion_percentage.md`
- `03_geometry_trigonometry/02_pythagorean_theorem_and_distance.md`
- `03_geometry_trigonometry/03_similarity_area_volume_and_scaling.md`

### Ratio, Proportion and Percentage

Chapter hiện phân biệt additive difference, multiplicative ratio, dimensional rate và percentage. Percentage point, repeated percentage compounding, weighted averages, geometric growth, annualized return, Simpson-style aggregation và nominal/real return được nối vào denominator reasoning.

### Pythagorean Theorem and Distance

Pythagoras được nâng từ triangle formula thành **orthogonal decomposition principle**. Inner product, generalized norm identity, projection proof của nearest point, law of cosines, least squares, statistics sum-of-squares, metrics và high-dimensional geometry đều được nối từ same structure.

### Similarity, Area, Volume and Scaling

Chapter hiện derive `k`, `k^2`, `k^3` từ independent dimensions, thêm square-cube law, determinant scaling, log-log power laws, resolution/voxel complexity, curse of dimensionality, Reynolds-style dynamic similarity và fractal/effective dimension intuition.

## Các chapter vẫn thấp hơn depth median và nên ưu tiên Round 7

Coverage hiện rộng và không có missing prerequisite lớn, nhưng các files sau vẫn tương đối ngắn so với dependency centrality:

1. `01_algebra/01_equations_and_inequalities.md`
2. `01_algebra/03_powers_roots_and_logarithms.md`
3. `01_algebra/04_polynomials_and_factorization.md`
4. `03_geometry_trigonometry/01_coordinate_geometry.md`
5. `03_geometry_trigonometry/05_transformations_and_symmetry.md`
6. `04_vectors_linear_algebra/00_vectors.md`
7. `05_calculus/06_numerical_calculus.md` — overlap với numerical methods cần consolidate/reframe hơn là chỉ kéo dài.
8. `06_probability_statistics/05_descriptive_and_inferential_statistics.md`
9. `06_probability_statistics/06_regression_and_correlation.md`
10. `07_discrete_cs/02_recurrence_and_induction_in_algorithms.md`
11. `08_optimization_numerical/01_gradient_descent_and_convexity.md` — cần tránh duplication với rewritten optimization chapter; nên chuyên sâu convergence/conditioning hơn.

Priority nên tiếp tục dựa trên **dependency centrality trước file count**.

## Dependency path sau Round 6

### Path cho AI/Data

```text
ratio / logarithm
→ functions
→ vectors / matrices
→ linear transformations
→ projection / least squares / SVD
→ derivatives
→ multivariable calculus / matrix calculus
→ probability / random variables
→ statistics / likelihood
→ optimization
→ dynamic programming / information theory.
```

### Path cho Physics/Engineering

```text
geometry / trigonometry
→ vectors / linear transformations
→ derivatives / integrals
→ ODE / eigenvalues
→ multivariable / vector calculus
→ PDE
→ Fourier
→ Laplace / Z-transform
→ control.
```

### Path cho Computer Science

```text
logic / proof
→ sets / relations / mappings
→ functions
→ discrete mathematics
→ induction / recurrence
→ graph theory
→ complexity
→ probability
→ numerical/optimization where needed.
```

### Path cho Finance

```text
ratio / percentage / compounding
→ exponential/logarithm
→ probability / random variables
→ expectation / covariance / statistics
→ linear algebra / factor models
→ optimization
→ stochastic processes / Bayesian inference.
```

## Scope boundary

Các topic như measure theory/Lebesgue integration, functional analysis, differential geometry/manifolds, stochastic calculus, advanced PDE, combinatorial optimization chuyên sâu và category theory vẫn là **optional upper-level expansion**, không phải missing prerequisite của current scope.

Không nên thêm chúng chỉ để tăng số chapter. Một chapter mới chỉ nên được thêm khi nó lấp dependency gap thực sự hoặc tạo knowledge connection có giá trị rõ.

## Kết luận

Round 6 giữ nguyên **87 topics** nhưng nâng depth của **13 chapter có dependency centrality cao** qua bốn batches. Thay đổi trọng tâm từ “coverage completeness” sang “conceptual completeness”: intuition trước formalism, formula có provenance, assumptions/failure modes rõ, proof idea khi phù hợp, worked examples đủ reasoning transfer và connections chỉ dùng khi shared mathematical structure thực sự tồn tại.

Ở trạng thái hiện tại, bottleneck chính không còn là thiếu lĩnh vực, mà là tiếp tục làm đồng đều chất lượng của nhóm chapter cũ còn ngắn hơn depth median.