# Coverage Audit — Master Knowledge Book: Toán

## Phạm vi của từ “hoàn thiện”

“Toán học” là một lĩnh vực mở nên không tồn tại một bộ tài liệu hữu hạn có thể bao phủ mọi branch nghiên cứu. Trong Knowledge Library này, **hoàn thiện trong scope** được hiểu là: bao phủ mạch kiến thức từ toán phổ thông đến nền tảng đại học và các mathematical structures cốt lõi dùng trong Computer Science, Software Engineering, AI/Data, Statistics, Engineering, signal/control và quantitative reasoning; đồng thời hạn chế tối đa việc một chapter sử dụng concept chưa từng được giải thích ở đâu trong library.

Một topic đạt yêu cầu khi có explanation theo first principles, giải thích meaning của công thức thay vì chỉ liệt kê formula, chỉ rõ assumptions/conditions quan trọng, có example hoặc application đủ cụ thể, có mental model để hình thành intuition và có phần Common Misconceptions cho các lỗi nhận thức thường gặp.

## Kết quả audit hiện tại — 2026-09-18

Library hiện có **87 topic files**, chưa tính `README.md`, glossary và file audit này.

Các vòng đầu đã bổ sung các khoảng trống lớn ở rational functions/domain, composition/inverse, conics, trigonometric identities/harmonics, orthogonality/projection, determinant/rank/null space, infinite series/Taylor, vector calculus, statistical inference, multivariate probability, information theory, computability, constrained optimization, numerical linear algebra và Fourier analysis.

Vòng tiếp theo bổ sung mathematical modeling & dimensional analysis, topology nhập môn, PDE, likelihood/MLE/MAP, abstract algebra nền tảng, linear programming/duality và Laplace/Z-transform.

**Audit round 4** tiếp tục mở rộng phần nối giữa toán nền tảng và modern computing bằng bảy topic mới: Tensor & Multilinear Algebra; Matrix Calculus/Jacobian/Hessian/Automatic Differentiation; Real Analysis; Complex Analysis; Stochastic Processes/Markov Chains/Time Series; Bayesian Inference/Posterior Predictive/Hierarchical Models; Dynamic Programming/Bellman/Optimal Control.

Round 4 cũng không chỉ tăng số file. Ba chapter cốt lõi từng quá ngắn đã được rewrite đáng kể: `Eigenvalues and Eigenvectors`, `Integrals and Accumulation`, `Differential Equations`. Các bản mới bổ sung multiplicity, defective matrices, spectral radius, PCA/Markov/graph connections; substitution, Jacobian, multidimensional integration, expectation, convolution, Monte Carlo; existence/uniqueness, phase portrait, stability, linearization, numerical ODE, stiffness và connections với stochastic systems/control.

## Phân bố topic hiện tại

| Nhóm | Số topic | Phạm vi chính |
|---|---:|---|
| Foundations | 6 | mathematical thinking, proof, sets/mappings, number systems, units, modeling & dimensional analysis |
| Algebra | 7 | equations, ratios, powers/logarithms, polynomials, complex numbers, rational expressions |
| Functions | 6 | function concept, linear/quadratic, exponential/log, recurrence, composition/inverse, parametric/polar/implicit |
| Geometry & Trigonometry | 9 | Euclidean/coordinate geometry, scaling, trigonometry, transformations, conics, harmonics, topology |
| Vectors & Linear Algebra | 10 | vectors, matrices, transformations, spaces/basis, eigenstructure, SVD, projection, rank/null space, tensors, matrix calculus/autodiff |
| Calculus & Analysis | 13 | limits, derivatives, integrals, multivariable calculus, ODE, numerical calculus, series/Taylor, vector calculus, PDE, real analysis, complex analysis |
| Probability & Statistics | 13 | probability, Bayes, distributions, expectation, inference, regression, sampling/testing, multivariate probability, MLE/MAP, stochastic processes, Bayesian inference |
| Discrete Mathematics & Theoretical CS | 9 | graphs, complexity, recurrence/induction, Boolean algebra, number theory, trees/posets/lattices, information theory, automata/computability, algebraic structures |
| Optimization & Numerical Mathematics | 7 | general optimization, gradient/convexity, numerical error, constrained optimization/KKT, root finding/numerical LA, LP/duality, dynamic programming/control |
| Knowledge Connections | 7 | rate/accumulation, distance/projection, uncertainty/entropy, AI/Data/Software, finance/daily life, Fourier, Laplace/Z-transform |
| **Tổng** | **87** | Không tính README, glossary và audit |

## Audit round 4 — topic mới

### Tensor & Multilinear Algebra

File: `04_vectors_linear_algebra/08_tensors_and_multilinear_algebra.md`

Khoảng trống trước audit là library đi từ vectors/matrices thẳng tới AI connections nhưng chưa giải thích tensor như mathematical object, tensor product, contraction, covariant/contravariant components, Einstein notation và distinction giữa tensor với multidimensional array trong software. Chapter mới lấp bridge này và nối trực tiếp sang ML tensor shapes và matrix calculus.

### Matrix Calculus, Jacobian, Hessian & Automatic Differentiation

File: `04_vectors_linear_algebra/09_matrix_calculus_jacobian_hessian_and_autodiff.md`

Trước đây multivariable calculus đã nhắc gradient/Jacobian nhưng chưa đủ để nối với backpropagation và modern autodiff. Chapter mới giải thích derivative như linear map của perturbations, Jacobian, Hessian, quadratic forms, matrix differentials, shape checking, forward/reverse-mode AD, Jacobian-vector product, vector-Jacobian product và Hessian-vector product.

### Real Analysis

File: `05_calculus/11_real_analysis_convergence_and_rigor.md`

Calculus trước đây chủ yếu dùng intuition operational. Chapter mới bổ sung completeness của real numbers, epsilon definitions, Cauchy sequences, subsequences, compactness, pointwise/uniform convergence, continuity/differentiability rigor và lý do không thể tùy tiện đổi thứ tự limit/integral/derivative.

### Complex Analysis

File: `05_calculus/12_complex_analysis_and_analytic_functions.md`

Complex numbers trước đây đã có nhưng thiếu bridge sang analytic functions và transform methods. Chapter mới bổ sung complex derivative, Cauchy–Riemann equations, contour integrals, Cauchy theorem/formula, singularities, Laurent series, residues, harmonic functions và connection với Fourier/Laplace/control.

### Stochastic Processes, Markov Chains & Time Series

File: `06_probability_statistics/11_stochastic_processes_markov_chains_and_time_series.md`

Probability trước đây chủ yếu mô tả random variables tĩnh. Chapter mới mở sang random evolution theo time với stationarity, autocorrelation, Markov property, transition matrices, stationary distributions, absorbing states, random walk, Poisson process, Brownian motion, martingales, AR/MA intuition, HMM và MCMC connection.

### Bayesian Inference & Hierarchical Models

File: `06_probability_statistics/12_bayesian_inference_posterior_predictive_and_hierarchical_models.md`

Library đã có Bayes theorem và MAP nhưng chưa có full Bayesian workflow. Chapter mới bổ sung prior/likelihood/posterior, conjugacy, posterior predictive, credible interval, prior/posterior predictive checks, hierarchical models, partial pooling, Bayesian regression, MCMC/variational inference, prior sensitivity và decision-theoretic interpretation.

### Dynamic Programming, Bellman & Optimal Control

File: `08_optimization_numerical/06_dynamic_programming_bellman_and_optimal_control.md`

Trước audit, recurrence trong CS và optimization tồn tại như hai nhánh nhưng chưa có chapter nối chúng thành sequential decision theory. Chapter mới giải thích state/action/transition, optimal substructure, Bellman equation, shortest path/knapsack/edit distance, stochastic DP, MDP, value iteration, policy iteration, curse of dimensionality, optimal control và HJB connection.

## Các chapter được nâng cấp sâu trong round 4

### Eigenvalues and Eigenvectors

File giữ nguyên: `04_vectors_linear_algebra/04_eigenvalues_and_eigenvectors.md`

Bản mới bổ sung eigenspace, algebraic/geometric multiplicity, diagonalization dưới góc đổi basis, defective matrices, Jordan intuition, spectral radius, complex eigenpairs, positive definiteness, Rayleigh quotient, SVD relation, PCA, Markov chains, graph Laplacian, matrix exponential và numerical sensitivity.

### Integrals and Accumulation

File giữ nguyên: `05_calculus/03_integrals_and_accumulation.md`

Bản mới mở rộng integral từ “area under curve” thành continuous accumulation framework: substitution, integration by parts, improper integrals, average value, probability/expectation, multidimensional change of variables/Jacobian, line/surface integrals, convolution, integral transforms, numerical quadrature, Monte Carlo integration và conservation laws.

### Differential Equations

File giữ nguyên: `05_calculus/05_differential_equations.md`

Bản mới bổ sung IVP, existence/uniqueness intuition, first-order linear equations, phase lines, equilibria/stability, characteristic roots, damping/resonance, systems of ODEs, matrix exponential, nonlinear linearization, phase planes, conservation laws, boundary-value problems, Euler/RK4, local/global error, stiffness, backward Euler, adaptive step size, event detection và non-dimensionalization.

## Dependency gaps còn lại sau round 4

Không có gap lớn nào buộc các path phổ biến AI/Data/Software/Engineering phải nhảy qua một concept hoàn toàn chưa được giới thiệu. Tuy vậy, nếu tiếp tục mở rộng từ “broad master foundation” sang “upper-undergraduate / early graduate mathematical library”, các candidate hợp lý tiếp theo là measure theory & Lebesgue integration, functional analysis, differential geometry/manifolds, generating functions nâng cao, stochastic calculus, numerical PDE, graph spectral theory sâu hơn, combinatorial optimization, game theory và category theory nhập môn.

Các topic này hiện được xem là **optional expansion**, không phải missing prerequisite bắt buộc của scope hiện tại. Khi thêm, cần giữ nguyên nguyên tắc: không thêm chapter chỉ để tăng số lượng; chapter mới phải lấp một dependency hoặc một knowledge connection có giá trị rõ ràng.

## Tiêu chí tiếp tục audit

Các vòng tiếp theo nên ưu tiên hai loại vấn đề. Thứ nhất là chapter có file size/nội dung quá ngắn so với importance của concept; đây là lý do round 4 rewrite eigenvalues, integrals và differential equations. Thứ hai là concept được reference nhiều lần trong các ứng dụng nhưng chưa có chapter giải thích first principles.

Mục tiêu không phải biến library thành encyclopedia vô hạn, mà giữ một network kiến thức đủ sâu để người đọc có thể đi từ câu hỏi thực tế ngược về mathematical foundations mà không gặp “black box” quá lớn.

## Kết luận

Ở trạng thái hiện tại, library gồm **87 topic files** và đã có coverage từ school mathematics tới phần nền tảng quan trọng của linear algebra, calculus/analysis, probability/statistics, discrete mathematics, numerical methods, optimization, AI/Data mathematics và dynamic systems. Round 4 đặc biệt cải thiện bridge giữa theory và modern computing thông qua tensors, autodiff, stochastic processes, Bayesian modeling và Bellman-style sequential optimization.