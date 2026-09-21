# Quality Audit — Round 7: depth balancing across Mathematics Knowledge Library

Round 7 tiếp tục chiến lược **quality over chapter count**. Không thêm Mathematics Library mới và không tăng số topic chỉ để mở rộng coverage. Library vẫn giữ 87 topic; mục tiêu là làm các chapter nền có dependency centrality cao đạt chất lượng gần với các chapter mới hơn như Real Analysis, Complex Analysis, Bayesian Inference, Tensor/Matrix Calculus và Dynamic Programming.

## Tiêu chí Round 7

Các chapter được chọn khi có ít nhất một trong các dấu hiệu:

- nhiều chapter downstream phụ thuộc vào concept đó;
- nội dung đúng nhưng ngắn/mang dạng expanded note;
- formalism xuất hiện quá sớm so với intuition;
- formula thiếu provenance hoặc assumptions;
- connection với CS, Physics, AI, Finance còn chỉ được nhắc tên;
- chapter overlap với chapter khác nhưng boundary chưa rõ;
- misconception/failure mode chưa đủ để tạo engineering judgment.

Round 7 giữ chuẩn canonical trong [`EDITORIAL_STANDARD.md`](./EDITORIAL_STANDARD.md): intuition trước formalism, formula có meaning, theorem/rule có reason/proof idea, examples tạo reasoning transfer, assumptions được nói rõ và connections dựa trên shared structure.

## Batch 1 — Algebra core

Commit: `6fd6d6eebd8f846c782567d5d07fe035403af867`

### `01_algebra/01_equations_and_inequalities.md`

Bản mới chuyển từ solving rules sang viewpoint **constraint + solution set + equivalence transformation**.

Learning flow mới:

```text
solution set + domain
→ equivalence vs one-way implication
→ inverse operations
→ linear systems as intersection
→ quadratic representations
→ absolute-value distance
→ rational-domain restrictions
→ inequalities as order constraints
→ optimization/software constraints
```

Điểm quan trọng là người đọc hiểu tại sao squaring có thể sinh extraneous solutions và tại sao “chuyển vế” chỉ là shorthand cho reversible operations.

### `01_algebra/03_powers_roots_and_logarithms.md`

Bản mới xây exponent laws từ repeated multiplication và consistency extension thay vì liệt kê rules.

Connections được làm rõ:

```text
multiplicative growth
→ negative/fractional exponents
→ roots
→ logarithm as inverse depth
→ continuous growth / e
→ O(log n)
→ information theory
→ log-likelihood
→ finance compounding
```

### `01_algebra/04_polynomials_and_factorization.md`

Polynomial được viết như object có nhiều representations: expanded, factored, vertex, Taylor.

Bản mới thêm proof idea cho factor/remainder theorem, multiplicity geometry, Fundamental Theorem of Algebra intuition, Vieta, interpolation limitations, Horner evaluation, root conditioning và connection với eigenvalues/control.

## Batch 2 — Coordinate Geometry, Transformations & Vectors

Commit: `92685a0e9de0f4296311c193ca2c75eb84e5e71b`

Ba chapter được rewrite quanh một concept chung:

> coordinates are representations; vectors encode displacement/state; transformations act on those representations; symmetry studies invariants.

### `03_geometry_trigonometry/01_coordinate_geometry.md`

Bản mới phân biệt point/vector, derive line representations bằng direction/normal vectors, derive point-line distance bằng projection, giải thích affine combination, active/passive coordinate changes, frames trong graphics/robotics và metric assumptions trong AI/geospatial data.

### `03_geometry_trigonometry/05_transformations_and_symmetry.md`

Bản mới đi từ map trên space → rigid/affine transforms → homogeneous coordinates → noncommutative composition → symmetry groups → invariance/equivariance → Noether-style physics intuition → graphics/robotics/ML.

### `04_vectors_linear_algebra/00_vectors.md`

Bản mới chuyển từ “arrow/list of components” sang vector như object trong chosen basis. Nội dung làm sâu norm choices, dot product derivation, projection/residual, cross product, basis dependence, matrix-column viewpoint và applications trong Physics, Graphics, AI và Finance.

## Batch 3 — Statistics & Regression

Commit: `f8f4136726abd8bcf50b4516564b87beedb741c6`

### `06_probability_statistics/05_descriptive_and_inferential_statistics.md`

Learning flow mới:

```text
population/sample
→ descriptive statistics
→ estimator bias/variance
→ sampling distribution
→ CLT/standard error
→ confidence procedure
→ hypothesis testing/power
→ multiple testing/bootstrap
→ causality and sampling design
```

Bản mới nhấn mạnh sample size không sửa systematic bias, p-value không phải probability hypothesis sai, effect size khác statistical significance và dataset shift là statistical assumption.

### `06_probability_statistics/06_regression_and_correlation.md`

Bản mới nối covariance/correlation với geometry; derive OLS slope; giải thích regression như projection + conditional model; làm rõ omitted-variable bias, residual diagnostics, heteroskedasticity, serial dependence, prediction interval, regularization, multicollinearity, logistic regression và maximum-likelihood viewpoint.

Causal interpretation được tách rõ khỏi fit/prediction.

## Batch 4 — Gradient Optimization & Numerical Calculus

Commit: `275ce7792ad68c70ad192e1919a26ed8503a7640`

### `08_optimization_numerical/01_gradient_descent_and_convexity.md`

Bản mới tập trung riêng vào optimization dynamics thay vì duplicate general optimization chapter.

Nội dung trọng tâm:

```text
local linear model
→ learning-rate stability
→ L-smoothness
→ convexity / strong convexity
→ condition number
→ convergence rates
→ preconditioning
→ momentum / stochastic gradients
→ non-convex saddles
→ gradient-flow connection
```

### `05_calculus/06_numerical_calculus.md`

File này được **consolidate boundary** với general Numerical Methods.

Nó chỉ tập trung sâu vào:

- finite differentiation;
- truncation vs roundoff/noise;
- higher-order differences/Richardson;
- quadrature/adaptive quadrature;
- Monte Carlo integration;
- automatic differentiation/JVP/VJP;
- gradient checking;
- complex-step differentiation.

Conditioning/root finding/numerical linear algebra/ODE stability vẫn thuộc canonical numerical-methods chapter, tránh duplicate nội dung.

## Batch 5 — Recurrence, Induction & Recursive Algorithms

Commit: `bbf6a7e35edeb62f0527278b740481935783702c`

### `07_discrete_cs/02_recurrence_and_induction_in_algorithms.md`

Bản mới thống nhất ba concepts:

```text
recursion = computation structure
recurrence = mathematical dependency
induction = proof structure
```

Nội dung làm sâu recursion trees, Master Theorem intuition, substitution proof, memoization vs recurrence semantics, dynamic-programming state design, loop invariants, structural induction, termination/ranking functions, matrix recurrence/eigenvalues và Bellman connection.

## Tác động lên learning dependency

Sau Round 7, các đường học phổ biến cân bằng hơn:

### CS / Algorithms

```text
algebra/logarithm
→ recurrence
→ induction
→ complexity
→ graph/DP
```

### AI / Data

```text
coordinates/vectors
→ linear algebra
→ calculus
→ probability
→ statistics/regression
→ gradient optimization
```

### Physics / Engineering

```text
geometry/vectors
→ transformations
→ calculus
→ differential equations
→ numerical calculus
→ Fourier/Laplace/control
```

### Finance

```text
ratio/percentage
→ exponential/logarithm
→ vectors/matrices
→ probability/statistics
→ regression
→ optimization
```

## Depth status sau Round 7

Các major bottlenecks được xử lý trong Round 5–7 hiện gồm:

- functions/exponential models;
- trigonometry;
- vectors/vector spaces;
- matrices/linear transformations/SVD;
- limits/derivatives/multivariable calculus;
- probability/statistics/regression;
- graph theory/complexity/recurrence;
- numerical methods/numerical calculus;
- general optimization/gradient optimization;
- ratios/scaling/coordinate geometry/transformations.

Các advanced chapters như Real Analysis, Complex Analysis, Information Theory, Bayesian Inference, Dynamic Programming, Fourier/Laplace và Control hiện không phải depth bottleneck tương đối.

## Priority hợp lý cho Round tiếp theo

Không nên mở rộng research-level topics trước khi polish thêm một số foundational nodes còn ngắn hơn median quality:

1. `00_foundations/01_logic_and_proof.md` — tăng proof strategy, quantifier negation và formal-vs-informal reasoning.
2. `00_foundations/02_sets_relations_and_mappings.md` — sâu hơn equivalence/order relations, cardinality và relation composition.
3. `00_foundations/03_numbers_and_number_systems.md` — construction intuition, completeness motivation, representation vs value.
4. `01_algebra/00_algebraic_language.md` — expressions/identities/equivalence/substitution as symbolic semantics.
5. `03_geometry_trigonometry/00_euclidean_geometry.md` — axioms, congruence, parallelism, proof structure và non-Euclidean boundary.
6. `06_probability_statistics/04_expectation_variance_and_limit_laws.md` — unify linearity, covariance, LLN/CLT and risk applications.
7. `07_discrete_cs/03_boolean_algebra_and_digital_logic.md` — strengthen algebra ↔ circuits ↔ predicates ↔ bit operations.
8. `07_discrete_cs/04_number_theory_and_modular_arithmetic.md` — proof ideas, congruence structure, gcd/inverses/CRT.

Những items này đều là **depth upgrades**, không phải yêu cầu thêm chapter mới.

## Kết luận

Round 7 không thay đổi coverage count. Giá trị chính là giảm variance về chất lượng giữa các chapter cũ và mới. Library ngày càng giống một connected textbook/knowledge graph hơn là collection của các notes độc lập.

> Coverage trả lời “concept có tồn tại trong library không?”. Depth trả lời “người đọc có thể tự reasoning từ concept đó sang vấn đề mới không?”. Round 7 tiếp tục tối ưu cho câu hỏi thứ hai.
