# Coverage & Finalization Audit — Mathematics Knowledge Library

## 1. Mục tiêu và kết luận của audit

`mathematics/` là Mathematics Knowledge Library canonical duy nhất của repository. Audit này là vòng hoàn thiện sau các quality/depth rounds trước đó; mục tiêu không phải tăng số lượng chapter mà xác nhận rằng **87 topic hiện tại đủ coherent để trở thành một canonical library trên `main`**, sau đó các branch Mathematics cũ có thể được đóng mà không làm mất nội dung.

Kết luận của vòng audit 2026-09-22:

- Library giữ nguyên **87 topic files**.
- Không phát hiện conceptual dependency gap nào đủ lớn để biện minh cho việc tạo chapter mới.
- Các major depth bottleneck đã được xử lý qua Round 5–11.
- Các short outliers còn lại đã được đọc lại; phần lớn ngắn vì scope hẹp, không phải vì thiếu conceptual depth.
- Finalization tập trung vào clickable internal links, prerequisite/downstream navigation, terminology/glossary, README/dependency graph và branch canonicalization.
- `main` đã chứa nội dung của mọi Mathematics branch cũ đã review. Hai branch Round 5 báo `diverged` chỉ vì lịch sử commit/rebase khác; blob/content cần thiết đã có trong canonical history.

Mental model cho trạng thái hiện tại:

> Coverage tạo các node. Depth làm mỗi node tự đứng được. Finalization làm các edge giữa node trở nên rõ, click được và không còn competing source of truth.

## 2. Tiêu chí canonical quality

Mỗi chapter được audit theo các câu hỏi sau. Không yêu cầu chapter nào cũng có cùng số section hoặc cùng độ dài; yêu cầu là người đọc không gặp một black box quan trọng trong scope của chapter.

1. Công thức quan trọng đã được giải thích meaning chưa?
2. Ký hiệu mới đã được định nghĩa hoặc đủ ngữ cảnh để suy ra chưa?
3. Assumption, domain và validity condition đã rõ chưa?
4. Người đọc có hiểu vì sao formula/theorem tồn tại hoặc đến từ đâu không?
5. Có intuition hoặc geometric/structural example phù hợp không?
6. Có application example đủ để transfer reasoning không?
7. Worked example có đủ bước ở chỗ dễ nhảy logic không?
8. Có hidden prerequisite khiến người đọc buộc phải đi Google không?
9. Chapter có connection thật tới prerequisite/downstream chapters không?
10. Nội dung có paragraph flow hay chỉ là encyclopedia/list of facts?
11. Failure mode, misconception hoặc boundary có được nói ra khi cần không?
12. Connection cross-domain có dựa trên shared mathematical structure hay chỉ là application list?

Chuẩn biên soạn chi tiết nằm tại [EDITORIAL_STANDARD.md](./EDITORIAL_STANDARD.md).

## 3. Phương pháp audit

Final status không được suy ra chỉ từ file size. Audit dùng bốn lớp evidence:

**Inventory toàn library.** Xác nhận toàn bộ 10 conceptual groups và đúng 87 topic files.

**Cumulative quality review.** Round 5–11 đã rewrite các dependency-central nodes theo từng batch. Các file audit lịch sử được giữ để trace lý do rewrite.

**Deep review ở finalization.** Đọc lại các domain ưu tiên và các outlier ngắn: logic/proof, functions, linear algebra, calculus, probability/Bayes, stochastic processes, numerical methods, Fourier/Laplace, matrix calculus/autodiff, optimization và dynamic programming/control.

**Branch-content review.** So sánh mọi Mathematics branch cũ với `main`; không dùng tên branch như `final`, `ready`, `rebased` làm bằng chứng merge.

## 4. Audit toàn bộ 87 chapter

Status notation:

- **Canonical**: depth và boundary phù hợp với scope hiện tại.
- **Canonical — deepened**: đã qua một hoặc nhiều quality rewrite quan trọng.
- **Canonical — final links**: content đã đủ, finalization chỉ bổ sung navigation/cross-links thay vì kéo dài cơ học.

### 00 — Foundations: 6/6 canonical

| Chapter | Status | Final audit note |
|---|---|---|
| `00_foundations/00_mathematical_thinking.md` | Canonical | Entry point cho abstraction, modeling, invariants, approximation và first-principles reasoning. |
| `00_foundations/01_logic_and_proof.md` | Canonical — deepened | Proposition, implication, quantifiers, proof strategies, induction, invariants, counterexamples và formal-vs-testing reasoning đủ cho downstream CS/Math. |
| `00_foundations/02_sets_relations_and_mappings.md` | Canonical — deepened | Sets, relations, equivalence/order, mappings và information-preservation bridge rõ. |
| `00_foundations/03_numbers_and_number_systems.md` | Canonical — deepened | Number-system expansion, completeness motivation và representation-vs-value boundary rõ. |
| `00_foundations/04_measurement_units_and_estimation.md` | Canonical — deepened | Units/dimensions, precision/accuracy, uncertainty propagation, estimation và sanity checks. |
| `00_foundations/05_mathematical_modeling_dimensional_analysis_and_scaling.md` | Canonical | Đã audit và chủ động giữ nguyên: modeling cycle, assumptions, sensitivity, validation và dimensional analysis đủ sâu. |

### 01 — Algebra: 7/7 canonical

| Chapter | Status | Final audit note |
|---|---|---|
| `01_algebra/00_algebraic_language.md` | Canonical — deepened | Algebra như representation-preserving transformation; domain và reversible operations rõ. |
| `01_algebra/01_equations_and_inequalities.md` | Canonical — deepened | Constraint/solution-set viewpoint, reversible vs one-way implication và domain restrictions. |
| `01_algebra/02_ratio_proportion_percentage.md` | Canonical — deepened | Denominator reasoning, rate, percentage points, weighted aggregation, compounding và finance/life examples. |
| `01_algebra/03_powers_roots_and_logarithms.md` | Canonical — deepened | Laws derive từ multiplicative structure; logarithm như inverse depth, không chỉ calculator rule. |
| `01_algebra/04_polynomials_and_factorization.md` | Canonical — deepened | Multiple representations, factor/remainder theorem, roots, multiplicity, conditioning và applications. |
| `01_algebra/05_complex_numbers.md` | Canonical — final links | Scope hẹp nhưng complete: plane, polar form, Euler, conjugate, roots of unity, rotation/phasor. Finalization thêm links tới trig/eigen/Fourier/Laplace/complex analysis. |
| `01_algebra/06_rational_expressions_domain_and_asymptotes.md` | Canonical — final links | Domain, holes vs poles/asymptotes, partial fractions và saturation model đủ; finalization nối limits/ODE/Laplace/numerics. |

### 02 — Functions: 6/6 canonical

| Chapter | Status | Final audit note |
|---|---|---|
| `02_functions/00_function_concept.md` | Canonical — deepened | Mapping contract, domain/codomain/range, injective/surjective/bijective, invertibility và information loss. |
| `02_functions/01_linear_and_quadratic_models.md` | Canonical — deepened | Constant-rate/curvature models, residuals, extrapolation, Taylor/physics/AI/finance bridges. |
| `02_functions/02_exponential_and_logarithmic_models.md` | Canonical — deepened | Proportional growth, differential equation, log depth, compounding, complexity và model limits. |
| `02_functions/03_sequences_series_and_recurrence.md` | Canonical — deepened | Sequence/state, recurrence/transition, series/accumulation, fixed points, characteristic equations và algorithm connections. |
| `02_functions/04_composition_inverse_and_function_transformations.md` | Canonical — final links | Composition order, inverse/information preservation, graph transforms và software pipeline complete; finalization thêm clickable prerequisite/downstream path. |
| `02_functions/05_parametric_polar_and_implicit_relations.md` | Canonical — final links | Representation choice, implicit derivative, parameterized motion, arc length, polar Jacobian complete; finalization nối calculus/conics/Jacobian. |

### 03 — Geometry & Trigonometry: 9/9 canonical

| Chapter | Status | Final audit note |
|---|---|---|
| `03_geometry_trigonometry/00_euclidean_geometry.md` | Canonical — deepened | Axioms/model assumptions, congruence/similarity, measure và non-Euclidean boundary. |
| `03_geometry_trigonometry/01_coordinate_geometry.md` | Canonical — deepened | Point/vector distinction, line representations, projection distance, frames và metric assumptions. |
| `03_geometry_trigonometry/02_pythagorean_theorem_and_distance.md` | Canonical — deepened | Pythagoras as orthogonal decomposition; norms, projection, least squares và high-dimensional geometry. |
| `03_geometry_trigonometry/03_similarity_area_volume_and_scaling.md` | Canonical — deepened | `k/k²/k³`, square-cube law, determinant scaling, power laws và dimension effects. |
| `03_geometry_trigonometry/04_trigonometry.md` | Canonical — deepened | Unit-circle/rotation/radian/phase/wave viewpoint; Euler/Fourier/sampling links. |
| `03_geometry_trigonometry/05_transformations_and_symmetry.md` | Canonical — deepened | Rigid/affine maps, homogeneous coordinates, noncommutative composition, invariance/equivariance. |
| `03_geometry_trigonometry/06_circles_conics_and_loci.md` | Canonical — deepened | Locus, conics, eccentricity, quadratic forms, eigenbasis rotation và covariance ellipse. |
| `03_geometry_trigonometry/07_trigonometric_identities_equations_and_harmonics.md` | Canonical — deepened | Identities từ rotation composition, harmonics, resonance, orthogonality và aliasing intuition. |
| `03_geometry_trigonometry/08_topology_continuity_connectivity.md` | Canonical | Audited Round 11 and kept: metric/neighborhood/open set/continuity/connectedness/compactness/homeomorphism đủ cho current scope. |

### 04 — Vectors & Linear Algebra: 10/10 canonical

| Chapter | Status | Final audit note |
|---|---|---|
| `04_vectors_linear_algebra/00_vectors.md` | Canonical — deepened | Vector as basis-dependent representation, norm, dot/cross product, projection và domain applications. |
| `04_vectors_linear_algebra/01_matrices_and_linear_systems.md` | Canonical — deepened | `Ax=b`, row equivalence, column space, rank/nullity, invertibility và conditioning. |
| `04_vectors_linear_algebra/02_linear_transformations.md` | Canonical — deepened | Superposition before matrix representation; kernel/image/rank-nullity and local linearization bridge. |
| `04_vectors_linear_algebra/03_vector_spaces_basis_dimension.md` | Canonical — deepened | Linear combination → span → independence → basis → dimension → rank-nullity; change-of-basis connections. |
| `04_vectors_linear_algebra/04_eigenvalues_and_eigenvectors.md` | Canonical — deepened | Natural modes/directions, diagonalization/stability and downstream stochastic/dynamic systems. |
| `04_vectors_linear_algebra/05_least_squares_svd_and_decompositions.md` | Canonical — deepened | Projection derivation, QR/SVD/pseudoinverse/conditioning/regularization/low-rank structure. |
| `04_vectors_linear_algebra/06_inner_product_orthogonality_and_projection.md` | Canonical — deepened | Inner-product geometry, Cauchy–Schwarz, projection theorem, Gram–Schmidt, weighted/function spaces. |
| `04_vectors_linear_algebra/07_determinant_rank_nullspace_and_inverse.md` | Canonical — deepened | Volume, information loss, reversibility, numerical rank/condition number và identifiability. |
| `04_vectors_linear_algebra/08_tensors_and_multilinear_algebra.md` | Canonical | Tensor/multilinear scope đủ làm bridge sang AI/physics/matrix calculus, không cần split thêm. |
| `04_vectors_linear_algebra/09_matrix_calculus_jacobian_hessian_and_autodiff.md` | Canonical — deepened | Derivative as linear map, gradient/Jacobian/Hessian, shape checking, forward/reverse AD, JVP/VJP/HVP và backprop. |

### 05 — Calculus & Analysis: 13/13 canonical

| Chapter | Status | Final audit note |
|---|---|---|
| `05_calculus/00_limits_and_continuity.md` | Canonical — deepened | Limit as precise tolerance reasoning, epsilon-delta intuition, discontinuities và numerical distinction. |
| `05_calculus/01_derivatives.md` | Canonical — deepened | Local linear response, derivations of rules, units/sensitivity/error propagation. |
| `05_calculus/02_derivative_applications.md` | Canonical — deepened | Shape, curvature, boundaries, Newton method, physics/AI/finance sensitivities. |
| `05_calculus/03_integrals_and_accumulation.md` | Canonical — deepened | Accumulation, Riemann structure, FTC, expectation/continuous totals and applications. |
| `05_calculus/04_multivariable_calculus.md` | Canonical — deepened | Jacobian/local map, gradient, Hessian, Lagrange geometry and change-of-variable structure. |
| `05_calculus/05_differential_equations.md` | Canonical — deepened | Local law → trajectory, solution families, initial conditions, stability and systems links. |
| `05_calculus/06_numerical_calculus.md` | Canonical — deepened | Boundary deliberately consolidated: differentiation/quadrature/AD/gradient checking, while general numerics lives elsewhere. |
| `05_calculus/07_infinite_series_power_series_and_convergence.md` | Canonical — deepened | Partial sums/tail control, tests, absolute/conditional convergence, power series, truncation. |
| `05_calculus/08_taylor_series_and_local_approximation.md` | Canonical — deepened | Local polynomial information, remainder, multivariable form, Newton/uncertainty/finance/numerical links. |
| `05_calculus/09_vector_calculus.md` | Canonical — deepened | Local-to-global fields: gradient/divergence/curl/integrals/theorems/conservation. |
| `05_calculus/10_partial_differential_equations_and_fields_intro.md` | Canonical | Audited Round 11; field → PDE → IC/BC → classification → modes → numerical stability is sufficient for intro scope. |
| `05_calculus/11_real_analysis_convergence_and_rigor.md` | Canonical | Completeness, Cauchy/convergence, compactness và rigorous bridge đủ cho library scope. |
| `05_calculus/12_complex_analysis_and_analytic_functions.md` | Canonical | Analyticity, Cauchy–Riemann, contour/residues and transform connections; no need for separate advanced course here. |

### 06 — Probability & Statistics: 13/13 canonical

| Chapter | Status | Final audit note |
|---|---|---|
| `06_probability_statistics/00_counting_and_combinatorics.md` | Canonical — deepened | Finite possibility spaces, bijection, inclusion-exclusion, recurrence, generating-function and asymptotic intuition. |
| `06_probability_statistics/01_probability_foundations.md` | Canonical — deepened | Sample-space/model assumptions, conditional structure, independence/calibration/common causes. |
| `06_probability_statistics/02_conditional_probability_and_bayes.md` | Canonical — deepened | Renormalization, chain rule, conditional independence, Bayes/odds/base rates, calibration and causal caveats. |
| `06_probability_statistics/03_random_variables_and_distributions.md` | Canonical — deepened | Random variable as mapping; PMF/PDF/CDF, joint/marginal/conditional, support/tails and loss links. |
| `06_probability_statistics/04_expectation_variance_and_limit_laws.md` | Canonical — deepened | Linearity, covariance, total expectation/variance, LLN/CLT, dependence/heavy-tail boundaries. |
| `06_probability_statistics/05_descriptive_and_inferential_statistics.md` | Canonical — deepened | Population/sample, bias-variance, sampling distribution, testing/power/bootstrap/design/causality boundaries. |
| `06_probability_statistics/06_regression_and_correlation.md` | Canonical — deepened | OLS derivation/projection, assumptions/diagnostics, multicollinearity, prediction vs causation. |
| `06_probability_statistics/07_sampling_estimation_confidence_and_hypothesis_testing.md` | Canonical — deepened | Sampling design, iid/dependence, CI/testing semantics, power/multiple testing/sequential issues. |
| `06_probability_statistics/08_covariance_multivariate_probability_and_gaussian.md` | Canonical — deepened | Covariance PSD geometry, linear combinations, whitening, uncertainty propagation and Gaussian structure. |
| `06_probability_statistics/09_common_distributions_and_when_they_arise.md` | Canonical — deepened | Distribution by mechanism/support/assumptions, approximation relations, hazards/overdispersion/heavy tails. |
| `06_probability_statistics/10_likelihood_mle_map_and_model_selection.md` | Canonical | Audited Round 11; likelihood/NLL/MLE/MAP/model-family assumptions already strong. |
| `06_probability_statistics/11_stochastic_processes_markov_chains_and_time_series.md` | Canonical | Process/sample path, stationarity/autocorrelation, Markov structure, random walk/Poisson/Brownian/HMM/MCMC adequate. |
| `06_probability_statistics/12_bayesian_inference_posterior_predictive_and_hierarchical_models.md` | Canonical | Prior/likelihood/posterior/predictive, partial pooling, MCMC/VI, sensitivity, checking and decision theory. |

### 07 — Discrete Mathematics & Theoretical CS: 9/9 canonical

| Chapter | Status | Final audit note |
|---|---|---|
| `07_discrete_cs/00_graph_theory.md` | Canonical — deepened | Modeling semantics, traversal, paths, SCC, DAG, matching/coloring, Laplacian/random walk and flow/cut. |
| `07_discrete_cs/01_algorithms_complexity_and_logarithms.md` | Canonical — deepened | Cost model, asymptotic notation, log from multiplicative shrinkage, lower/amortized/practical complexity. |
| `07_discrete_cs/02_recurrence_and_induction_in_algorithms.md` | Canonical — deepened | Recursion/computation, recurrence/dependency, induction/proof; recursion tree, DP and termination. |
| `07_discrete_cs/03_boolean_algebra_and_digital_logic.md` | Canonical — deepened | Truth semantics → algebra → implementation; circuits/SAT/SQL 3VL/bit masks. |
| `07_discrete_cs/04_number_theory_and_modular_arithmetic.md` | Canonical — deepened | Divisibility/gcd/Bézout/primes/congruence/inverses/CRT/finite fields with proof ideas. |
| `07_discrete_cs/05_trees_posets_and_lattices.md` | Canonical — deepened | Tree → DAG → order → lattice → fixpoint; compiler/CRDT bridges. |
| `07_discrete_cs/06_information_theory_and_coding.md` | Canonical — deepened | Surprise/entropy/compression/MI/KL/capacity/error-correction and ML loss links. |
| `07_discrete_cs/07_automata_formal_languages_and_computability.md` | Canonical — deepened | Memory hierarchy, DFA/NFA/CFG/PDA/TM, decidability, reduction and complexity boundaries. |
| `07_discrete_cs/08_groups_rings_fields_and_algebraic_structures.md` | Canonical | Audited Round 11; symmetry/homomorphism/kernel/finite fields/quotient intuition sufficient for current scope. |

### 08 — Optimization & Numerical Mathematics: 7/7 canonical

| Chapter | Status | Final audit note |
|---|---|---|
| `08_optimization_numerical/00_optimization.md` | Canonical — deepened | Objective/feasible set before algorithm; convexity, constraints, duality, robust/discrete/multi-objective reasoning. |
| `08_optimization_numerical/01_gradient_descent_and_convexity.md` | Canonical — deepened | Optimization dynamics: smoothness, strong convexity, conditioning, convergence, momentum/SGD/nonconvex saddles. |
| `08_optimization_numerical/02_numerical_methods_and_error.md` | Canonical — deepened | Conditioning vs stability, forward/backward error, floating point, cancellation, root/integration/linear-system judgment. |
| `08_optimization_numerical/03_constrained_optimization_lagrange_and_kkt.md` | Canonical — deepened | Tangent/normal geometry, active constraints, KKT assumptions, constraint qualification, dual/penalty/barrier methods. |
| `08_optimization_numerical/04_root_finding_interpolation_and_numerical_linear_algebra.md` | Canonical — deepened | Convergence/conditioning/stability/error control unify bisection/Newton/interpolation/linear solvers. |
| `08_optimization_numerical/05_linear_programming_duality_and_simplex.md` | Canonical — deepened | Polyhedra/basis/simplex/degeneracy/duality/sensitivity/interior point/integrality. |
| `08_optimization_numerical/06_dynamic_programming_bellman_and_optimal_control.md` | Canonical | Bellman principle, state/value/policy, MDP/control bridge and sequential-decision assumptions sufficient for current scope. |

### 09 — Knowledge Connections: 7/7 canonical

| Chapter | Status | Final audit note |
|---|---|---|
| `09_connections/00_rate_change_and_accumulation.md` | Canonical — deepened | State/rate/accumulation, discrete/continuous analogy, queues/finance/conservation. |
| `09_connections/01_distance_similarity_and_projection.md` | Canonical — deepened | Norm/metric/inner product/projection/covariance geometry and high-dimensional caveats. |
| `09_connections/02_uncertainty_information_and_entropy.md` | Canonical — deepened | Probability → surprise → entropy → MI/KL/cross-entropy → decision/coding. |
| `09_connections/03_math_for_ai_data_and_software.md` | Canonical — deepened | Representation → composition/autodiff → losses/optimization → probability/statistics → numerical/production evidence. |
| `09_connections/04_math_for_finance_work_and_daily_life.md` | Canonical | Compounding, discounting, NPV/annuity/loan and quantitative judgment already balanced. |
| `09_connections/05_fourier_signals_and_frequency.md` | Canonical — deepened | Basis/projection → Fourier → convolution/LTI → sampling/aliasing → DFT/FFT/PDE/AI. |
| `09_connections/06_laplace_z_transform_and_dynamic_systems.md` | Canonical — final links | Transform/operator viewpoint, transfer functions, poles/zeros, stability, state-space/eigen bridge complete; finalization adds canonical navigation. |

**Total: 87/87 topic files audited and accepted for current canonical scope.**

## 5. Các domain ưu tiên xuyên ngành

### Logic / proof

Không chỉ phục vụ pure mathematics. Quantifiers, implication, counterexample và invariant nối trực tiếp sang specification, algorithm correctness, testing và formal verification.

### Functions / composition

Function là mapping/contract; composition là pipeline; inverse là reversibility/information preservation. Đây là bridge giữa algebra, calculus chain rule, neural networks và software data flow.

### Linear algebra / matrix calculus / autodiff

Vectors/matrices/bases/projections/eigen/SVD tạo representation geometry. Jacobian/Hessian/autodiff mở rộng nó sang local nonlinear sensitivity và ML optimization.

### Probability / statistics / Bayes / stochastic process

Probability model uncertainty, statistics học từ samples, Bayes cập nhật uncertainty, stochastic processes mô hình dependency theo time. Các assumptions về sampling, dependence, calibration và model misspecification được giữ tách biệt.

### Optimization / numerical methods

Optimization hỏi decision nào tốt dưới objective/constraints. Numerical analysis hỏi máy tính hữu hạn có tìm/represent answer đáng tin hay không. Hai domain liên hệ nhưng không được nhập làm một.

### Discrete mathematics / graphs / information theory

Đây là mathematical substrate cho algorithms, data structures, networks, coding, databases, state machines và software architecture.

### Fourier / Laplace / dynamic systems

Cùng mental model change-of-representation: chọn basis/domain nơi convolution, differentiation, recurrence hoặc stability trở nên dễ quan sát và thao tác hơn.

## 6. Cross-domain connections đã xác nhận

| Domain ngoài Mathematics | Canonical mathematical bridge |
|---|---|
| Computer Science | Logic/proof, sets/relations, recurrence, graph theory, number theory, automata, complexity. |
| Algorithms | Induction/invariants, recurrence, asymptotics, graph/path structure, dynamic programming. |
| AI/ML | Linear algebra, multivariable/matrix calculus, autodiff, probability, statistics, information theory, optimization, numerics. |
| Data Engineering | Sets/relations, functions/pipelines, graph dependency, probability/statistics, cardinality/approximation/numerical reasoning. |
| Physics | Measurement, dimensional analysis, geometry/vectors, calculus, ODE/PDE, Fourier, symmetry/conservation. |
| Finance/Investing | Ratio/compounding, probability, expectation/covariance, regression, stochastic processes, optimization, numerical sensitivity. |
| Software Engineering | Logic/contracts, composition, graph dependency, complexity, probabilistic reliability, floating-point/numerical stability. |
| Đời sống thực tế | Percentage/rates, estimation, units, uncertainty, expected value, compounding, risk and decision trade-offs. |

Clickable routes được giữ tại [README.md](./README.md); connection chapters không thay thế canonical topic chapters mà giúp transfer mental models giữa domains.

## 7. Scope boundary — tại sao không thêm chapter mới

Các topic như measure theory/Lebesgue integration, functional analysis, differential geometry/manifolds, stochastic calculus, advanced PDE, advanced control, advanced combinatorial optimization và category theory vẫn là upper-level expansions hợp lệ, nhưng hiện **không phải missing prerequisite** của 87-topic library.

Rule canonical từ vòng này:

> Không thêm chapter vì topic “quan trọng” hoặc “nổi tiếng”. Chỉ thêm khi repository xuất hiện một dependency gap cụ thể mà chapter hiện tại không thể giải quyết trong boundary hợp lý.

## 8. Consistency changes của finalization 2026-09-22

Finalization branch `math-finalization-20260922` được tạo trực tiếp từ current `main` trước khi sửa.

Các thay đổi có chủ đích:

- README được cập nhật từ trạng thái cũ “sau bốn vòng audit” sang canonical state 87 topics sau Round 5–11 + final audit.
- TOC labels được đồng bộ với current chapter titles.
- Dependency graph được cập nhật tới Bayes, stochastic processes, matrix calculus/autodiff, LP/duality, DP/control và Fourier/Laplace.
- Thêm learning routes Markdown có thể click trực tiếp cho CS/Algorithms, AI/Data, Physics, Signal/Control, Finance và Software Engineering.
- Các short-but-complete nodes `complex_numbers`, `rational_expressions`, `composition_inverse`, `parametric_polar_implicit`, `laplace_z` được thêm canonical prerequisite/downstream links thay vì rewrite dài không cần thiết.
- Glossary được bổ sung recurring terms: automatic differentiation, computational graph, backpropagation, prior/posterior/posterior predictive, calibration, causal intervention, stochastic process, Markov chain, stationarity, autocorrelation, martingale, hierarchical model, dynamic programming, Bellman equation, transfer function, pole/zero, ROC, state space và LTI.
- Không thêm Mathematics topic file mới.

## 9. Audit toàn bộ Mathematics branches cũ

Trước finalization có **19 branch Mathematics cũ**. Kết quả branch-level review:

### 17 branch không còn unique commit so với `main`

Các branch sau đều được compare với `main` và có `ahead_by = 0`; chúng chỉ đứng sau canonical history:

1. `add-mathematics-master-book`
2. `math-audit-round4-20260918`
3. `math-depth-audit-round6-20260921`
4. `math-depth-round7-20260921`
5. `math-depth-round8-20260921`
6. `math-depth-round8-20260921-b2`
7. `math-depth-round8-20260921-copy`
8. `math-depth-round8-20260921-work`
9. `math-depth-round9-20260921`
10. `math-depth-round10-20260921`
11. `math-depth-round11-20260921`
12. `math-merge`
13. `math-merge-active`
14. `math-merge-ready`
15. `math-merge-staging-20260918`
16. `math-merge-staging-20260918-v2`
17. `math-merge-staging-final`

Các branch này không cần merge/cherry-pick lại.

### 2 branch báo diverged do history nhưng content đã được review

18. `math-quality-round5-20260920`
19. `math-quality-round5-rebased`

Git history báo ahead/diverged vì Round 5 đã đi qua rebase/cherry-pick/alternate history. Vì vậy không được kết luận chỉ từ `ahead_by`.

Final review đã đối chiếu actual Round 5 files. Canonical `main` chứa cùng content/blob cho các rewrites quan trọng:

- `02_functions/00_function_concept.md`
- `02_functions/02_exponential_and_logarithmic_models.md`
- `03_geometry_trigonometry/04_trigonometry.md`
- `04_vectors_linear_algebra/03_vector_spaces_basis_dimension.md`
- `05_calculus/00_limits_and_continuity.md`
- `07_discrete_cs/00_graph_theory.md`
- `08_optimization_numerical/02_numerical_methods_and_error.md`
- `EDITORIAL_STANDARD.md`
- `QUALITY_AUDIT_ROUND5.md`

Do đó divergence này là **commit-history divergence đã review**, không phải unmerged content divergence.

## 10. Canonicalization checklist

### Content

- [x] Inventory đúng 87 topic files.
- [x] Audit cumulative Round 5–11 được đọc và đối chiếu với current files.
- [x] Logic/proof, functions, linear algebra, calculus, probability/statistics/Bayes, optimization, discrete/graphs/info theory, numerics, Fourier/Laplace, stochastic process, matrix calculus/autodiff và DP/control đã được review ở depth phù hợp.
- [x] Formula/notation/assumption/provenance/worked-example/failure-mode criteria được dùng làm canonical standard.
- [x] Các short outlier được đọc trước khi quyết định; không kéo dài file chỉ để đồng đều size.
- [x] Không thêm chapter chỉ để tăng coverage.

### Navigation & consistency

- [x] README phản ánh current 87-topic state.
- [x] TOC labels và dependency graph được cập nhật.
- [x] Có clickable learning routes thay vì phụ thuộc Mermaid để navigate.
- [x] Các short central nodes được bổ sung prerequisite/downstream links.
- [x] Glossary có thêm advanced recurring terms của Bayes/stochastic/autodiff/control.
- [x] Cross-domain boundaries tới CS, AI/Data, Physics, Finance/Investing và Software Engineering được làm rõ.

### Branch safety

- [x] Toàn bộ 19 Mathematics branches cũ đã được inventory.
- [x] 17/19 branches xác nhận `ahead_by = 0` so với pre-finalization `main`.
- [x] 2 Round 5 branches có history divergence đã được content-review; không còn nội dung Mathematics cần cứu trước cleanup.
- [x] Tạo một finalization branch duy nhất từ canonical `main` để chứa consistency changes cuối.
- [ ] Merge finalization branch vào `main`.
- [ ] Re-verify canonical `main` sau merge.
- [ ] Chỉ sau hai bước trên mới xóa/đóng 19 Mathematics branches cũ và finalization branch.

Hai checkbox cuối cố ý chưa được đánh dấu tại thời điểm file này được viết trên finalization branch. Đây là safety gate: **không cleanup branch trước khi finalization changes thực sự nằm trên `main`.**

## 11. Canonical source of truth sau finalization

Sau merge, thứ tự ưu tiên tài liệu là:

1. `mathematics/README.md` — entry point, TOC, clickable learning routes và dependency topology.
2. 87 canonical topic chapters — nội dung học chính.
3. `mathematics/10_glossary.md` — terminology index VI/EN/KR.
4. `mathematics/COVERAGE_AUDIT.md` — scope/finalization/branch-safety source of truth.
5. `QUALITY_AUDIT_ROUND*.md` — historical rationale của các rewrite rounds, không phải competing canonical indexes.

Ở trạng thái này, Mathematics không cần một library mới, một `*_final` copy hay một branch depth mới. Future work nên bắt đầu từ canonical `main` và chỉ mở branch mới khi có một change cụ thể, reviewable và có conceptual reason rõ ràng.
