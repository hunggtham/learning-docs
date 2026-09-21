# Quality Audit — Round 9: strengthen quantitative bridges and convergence reasoning

Round 9 tiếp tục chiến lược **quality over chapter count**. Mathematics Knowledge Library vẫn giữ **87 topic**; không thêm chapter mới chỉ để tăng coverage.

Mục tiêu của round này là nâng các chapter đang nằm giữa các dependency chains quan trọng nhưng depth thấp hơn đáng kể so với phần đã rewrite ở Round 5–8.

## Phạm vi Round 9

Round này audit các priority đã đánh dấu từ Round 8:

```text
00_foundations/04_measurement_units_and_estimation.md
00_foundations/05_mathematical_modeling_dimensional_analysis_and_scaling.md
02_functions/01_linear_and_quadratic_models.md
02_functions/03_sequences_series_and_recurrence.md
04_vectors_linear_algebra/06_inner_product_orthogonality_and_projection.md
04_vectors_linear_algebra/07_determinant_rank_nullspace_and_inverse.md
05_calculus/07_infinite_series_power_series_and_convergence.md
05_calculus/08_taylor_series_and_local_approximation.md
06_probability_statistics/02_conditional_probability_and_bayes.md
06_probability_statistics/07_sampling_estimation_confidence_and_hypothesis_testing.md
```

Sau audit, `05_mathematical_modeling_dimensional_analysis_and_scaling.md` **không được rewrite** vì nội dung đã đủ sâu và tương đối cân bằng với editorial standard. Round 9 chỉ sửa những file thực sự có depth gap.

## Batch 1 — Measurement + Function Models

Commit: `d809264e153ca701b5b56c298f4db6d7a7fce5aa`

### `00_foundations/04_measurement_units_and_estimation.md`

Bản mới chuyển từ overview units/error thành một chapter quantitative reasoning hoàn chỉnh.

Learning flow:

```text
quantity
→ unit / dimension
→ dimensional consistency
→ precision vs accuracy
→ absolute / relative error
→ uncertainty propagation
→ order of magnitude
→ Fermi estimation
→ sanity bounds
→ logarithmic scale
```

Các phần mới quan trọng gồm:

- unit như type information;
- dimension khác unit;
- dimensional consistency là necessary check chứ không phải proof;
- precision vs accuracy;
- false precision;
- first-order uncertainty propagation bằng derivatives/Jacobian;
- bounding và sanity checking;
- unit bugs trong software;
- relation với Finance, CS và AI metrics.

### `02_functions/01_linear_and_quadratic_models.md`

Bản cũ chỉ khoảng 4 KB và ngắn hơn rất nhiều so với Function Concept/Exponential Models đã rewrite.

Bản mới tổ chức quanh structure của change:

```text
constant first-order rate
→ affine model
→ proportionality
→ interpolation / extrapolation
→ residual diagnostics
→ linearly changing rate
→ quadratic model
→ curvature
→ Taylor second-order model
```

Connections được làm rõ với:

- constant acceleration;
- least-squares regression;
- Hessian/quadratic forms;
- AI affine layers;
- Finance first/second-order sensitivity;
- braking-distance scaling.

### `02_functions/03_sequences_series_and_recurrence.md`

Bản mới tách rõ:

```text
sequence = state by discrete step
recurrence = transition law
series = accumulated state
```

Đã bổ sung:

- arithmetic/geometric sequences dưới finite-difference viewpoint;
- affine recurrences và fixed points;
- matrix representation của recurrences;
- characteristic equations;
- algorithm recurrences;
- memoization/dynamic programming;
- sequence convergence;
- series convergence tests;
- generating-function intuition;
- discrete control/numerical iteration connections.

## Batch 2 — Linear Algebra Geometry and Information

Commit: `fcfeeba77aeee70665f51d52394e664bc1114ee1`

### `04_vectors_linear_algebra/06_inner_product_orthogonality_and_projection.md`

Bản mới xây dependency chain:

```text
inner product
→ norm
→ Cauchy–Schwarz
→ angle
→ orthogonality
→ projection
→ orthogonal decomposition
→ least squares
→ QR / Fourier / PCA
```

Điểm mới:

- proof idea của Cauchy–Schwarz;
- projection theorem;
- orthonormal basis và projection matrices;
- Gram–Schmidt vs numerical stability;
- weighted inner products / Mahalanobis geometry;
- function-space inner product;
- PCA/Fourier/embedding connections;
- metric choice làm thay đổi geometry.

### `04_vectors_linear_algebra/07_determinant_rank_nullspace_and_inverse.md`

Bản mới thống nhất bốn concepts bằng viewpoint information flow:

```text
determinant → volume distortion
rank        → visible dimensions
null space  → lost directions
inverse     → reversibility
conditioning→ reliability of recovery
```

Đã bổ sung:

- row operations và determinant meaning;
- rank as reachable-output dimension;
- full row vs full column rank;
- Invertible Matrix Theorem như một unified structure;
- singular values, condition number và numerical rank;
- pseudoinverse;
- identifiability;
- Jacobian determinant;
- PCA/low-rank compression;
- null-space parameterization of constraints.

## Batch 3 — Infinite Series + Taylor

Commit: `6c8de62c51ce096e3d776f3cc70098693f763611`

### `05_calculus/07_infinite_series_power_series_and_convergence.md`

Bản mới đi từ partial sums tới tail control thay vì collection of tests.

Learning flow:

```text
partial sums
→ convergence
→ tail/remainder
→ benchmark series
→ comparison/integral/ratio/root tests
→ absolute vs conditional convergence
→ power series
→ radius of convergence
→ numerical truncation/error
```

Đã thêm:

- integral test và p-series intuition;
- limit comparison;
- root test;
- Cauchy criterion;
- endpoint behavior;
- term-by-term differentiation/integration;
- ODE power-series connection;
- numerical convergence vs computational efficiency;
- Finance perpetuity và CS amortized/geometric work examples.

### `05_calculus/08_taylor_series_and_local_approximation.md`

Bản mới biến Taylor thành framework **local polynomial information**.

Đã bổ sung:

- uniqueness của Taylor polynomial qua derivative matching;
- Taylor polynomial vs Taylor series;
- smooth vs analytic;
- Lagrange remainder/error bounds;
- multivariable Taylor/Hessian;
- Newton derivation;
- uncertainty propagation;
- perturbation/small-angle physics;
- delta-gamma Finance connection;
- Taylor vs interpolation vs Fourier;
- range reduction và numerical evaluation;
- complex singularity intuition cho radius of convergence.

## Batch 4 — Conditional Probability + Statistical Inference

Commit: `280c5ec0f6f59410544c3056769bd83e555b7049`

### `06_probability_statistics/02_conditional_probability_and_bayes.md`

Bản mới đi từ conditional sample-space restriction tới probabilistic modeling hiện đại:

```text
conditional probability
→ product / chain rule
→ independence
→ conditional independence
→ total probability
→ Bayes
→ odds / likelihood ratio
→ sequential updates
→ posterior predictive
→ calibration / causal caveats
```

Đã thêm:

- conditional independence;
- chain rule;
- natural-frequency representation;
- likelihood ratios và log-odds;
- Naive Bayes;
- continuous Bayes;
- Beta–Bernoulli intuition;
- posterior predictive;
- calibration;
- selection/collider effects;
- Simpson's paradox;
- distinction conditioning vs intervention.

### `06_probability_statistics/07_sampling_estimation_confidence_and_hypothesis_testing.md`

Bản mới làm rõ inference là **uncertainty accounting under a sampling design**.

Đã bổ sung:

- sampling design vs sample size;
- iid assumptions;
- effective sample size;
- estimator bias/variance/consistency;
- derivation confidence intervals;
- Student t intuition;
- bootstrap;
- p-value semantics;
- power/sample-size design;
- practical vs statistical significance;
- multiple testing;
- optional stopping/sequential monitoring;
- cluster/time-series dependence;
- missing data/measurement error;
- Bayesian credible interval comparison;
- confidence sequence;
- A/B testing, AI evaluation và Finance backtest connections.

## Depth result after Round 9

Các dependency chains sau hiện đã cân bằng hơn đáng kể:

```text
Measurement
→ Modeling
→ Functions
→ Calculus / Numerical Methods
```

```text
Vectors
→ Inner Product
→ Projection
→ Least Squares / SVD
```

```text
Matrices
→ Rank / Nullspace
→ Inverse / Conditioning
→ PCA / Optimization / Identifiability
```

```text
Sequences
→ Infinite Series
→ Power Series
→ Taylor
→ Numerical Approximation
```

```text
Probability
→ Conditioning / Bayes
→ Sampling Distributions
→ Estimation / Testing
→ Bayesian / Frequentist Inference
```

## Chapters not rewritten in Round 9

`00_foundations/05_mathematical_modeling_dimensional_analysis_and_scaling.md` đã được audit nhưng giữ nguyên vì:

- chapter đã khoảng 11 KB;
- có modeling cycle, assumptions, dimensional analysis, sensitivity, validation, residuals và applications;
- learning dependency sang calculus/statistics/optimization đã rõ;
- rewrite chỉ để đồng bộ length sẽ tạo churn không cần thiết.

Đây là một nguyên tắc quan trọng của continuing audit: **không sửa chapter chỉ vì nó nằm trong checklist**.

## Priority cho Round 10

Sau Round 9, các depth gaps đáng ưu tiên tiếp theo là:

```text
06_probability_statistics/00_counting_and_combinatorics.md
06_probability_statistics/08_covariance_multivariate_probability_and_gaussian.md
06_probability_statistics/09_common_distributions_and_when_they_arise.md

03_geometry_trigonometry/06_conic_sections_and_loci.md
03_geometry_trigonometry/07_trigonometric_identities_equations_and_harmonics.md

05_calculus/09_vector_calculus.md

07_discrete_cs/05_trees_posets_and_lattices.md
07_discrete_cs/06_information_theory_and_coding.md

08_optimization_numerical/03_constrained_optimization_lagrange_kkt.md
08_optimization_numerical/04_root_finding_interpolation_and_numerical_linear_algebra.md
```

Priority này không có nghĩa các chapter trên thiếu coverage. Chúng là các files còn ngắn hơn rõ rệt so với neighboring chapters hoặc đóng vai trò bridge quan trọng chưa đạt cùng editorial depth.

## Kết luận

Round 9 không thay đổi topology của library và không tăng 87-topic count. Giá trị chính là giảm depth discontinuity ở năm bridge lớn: **measurement**, **discrete function evolution**, **linear-algebra geometry**, **convergence/local approximation**, và **probabilistic/statistical inference**.

Mục tiêu tiếp tục không phải biến library thành encyclopedia vô hạn, mà làm cho người đọc có thể đi từ intuition tới formalism rồi sang application mà không gặp black box lớn ở các chapter trung tâm.