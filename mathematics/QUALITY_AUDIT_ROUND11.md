# Quality Audit — Round 11: computation, optimization và bridge chapters

Round 11 tiếp tục chiến lược **quality over chapter count**. Mathematics Knowledge Library vẫn giữ nguyên **87 topic**; không thêm chapter mới chỉ để tăng coverage.

Mục tiêu của round này là audit nhóm advanced/core bridge còn lại sau Round 10 và chỉ rewrite nơi có depth gap thực sự.

## Tiêu chí audit

Một chapter chỉ được rewrite nếu có một hoặc nhiều dấu hiệu:

```text
learning dependency quan trọng nhưng nội dung còn ngắn
formalism đúng nhưng proof idea / intuition chưa đủ
assumptions hoặc failure modes còn mỏng
connections chỉ được nhắc tên thay vì derive
chapter bridge chưa thực sự nối được các domain
```

Ngược lại, chapter đủ coherent, có assumptions, mental model và downstream connections thì giữ nguyên dù file ngắn hơn chapter khác.

## Batch 1 — Automata/Computability + Linear Programming

Commit:

```text
aecdfa8bbdbb339d84694b11f2dc744021e0c319
```

### `07_discrete_cs/07_automata_formal_languages_and_computability.md`

Bản cũ đúng về DFA, CFG, Turing machine, halting problem và P/NP nhưng còn giống overview.

Bản mới tổ chức thành dependency chain:

```text
alphabet / strings
→ formal language
→ recognizer vs decider
→ DFA / NFA
→ regular language
→ finite-memory limitation
→ CFG / PDA
→ hierarchy of memory
→ Turing machine
→ decidability
→ reduction
→ complexity / NP-completeness
```

Các phần tăng sâu:

- DFA state như compressed relevant history;
- NFA vs DFA: same expressive power nhưng state blow-up;
- regular expression theory vs production regex engines;
- pumping/Myhill–Nerode intuition qua information capacity;
- CFG/PDA và recursive syntax;
- Chomsky hierarchy dưới viewpoint memory structure;
- universal Turing machine và program-as-data;
- Church–Turing thesis vs theorem;
- recognizable vs decidable;
- halting proof qua self-reference/diagonalization;
- reduction direction;
- NP-hard/NP-complete distinction;
- state explosion trong model checking;
- compiler lexing/parsing/semantic-analysis separation.

### `08_optimization_numerical/05_linear_programming_duality_and_simplex.md`

Bản cũ đã có primal/dual/simplex và integer programming nhưng depth thấp hơn KKT/Numerical chapters mới.

Bản mới có learning flow:

```text
modeling
→ feasible polyhedron
→ extreme point
→ basis / basic feasible solution
→ simplex pivot
→ degeneracy
→ duality
→ complementary slackness
→ sensitivity
→ interior-point
→ LP relaxation / integrality
```

Các phần tăng sâu:

- feasible/infeasible/unbounded separation;
- algebraic basis ↔ geometric vertex;
- simplex pivot như basis change;
- degeneracy/cycling;
- weak duality derivation;
- strong duality như optimality certificate;
- shadow price only locally valid under regime/basis stability;
- interior-point vs simplex trade-offs;
- LP relaxation, branch-and-bound, integrality gap;
- total unimodularity;
- max-flow/min-cut as structured duality;
- numerical scaling/tolerance caveats;
- deterministic LP vs uncertainty/robust optimization.

## Batch 2 — `09_connections` bridge chapters

Commit:

```text
bb8f70afd1f53e251c00117f90da252b6a34ff52
```

Sau Round 5–10, nhiều canonical topic chapters đã rất sâu nhưng một số `09_connections` chỉ còn 4–5 KB và giống summary. Round 11 nâng 5 bridge chapters để chúng thực sự giúp transfer mental model giữa domains.

### `09_connections/00_rate_change_and_accumulation.md`

Learning flow mới:

```text
state
→ finite difference
→ local derivative
→ accumulation
→ discrete summation
→ recurrence
→ density/CDF
→ differential equations
→ conservation law
```

Connections tăng sâu:

- state vs rate vs accumulated total;
- signed vs absolute accumulation;
- discrete Fundamental-Theorem analogy;
- additive vs multiplicative recurrence;
- queue length vs arrival/service rates;
- finance balance vs cash-flow rate;
- marginal vs total quantities;
- gradient descent as accumulated local updates;
- continuity/conservation equation;
- dimensional sanity checks.

### `09_connections/01_distance_similarity_and_projection.md`

Learning flow mới:

```text
representation
→ norm
→ metric
→ scaling
→ inner product
→ similarity
→ projection
→ covariance geometry
```

Các phần tăng sâu:

- L1/L2/L∞ geometries;
- metric axioms và triangle inequality;
- preprocessing thay đổi geometry;
- cosine similarity và khi normalization làm mất signal;
- projection as nearest-point problem;
- least squares geometry;
- PCA criterion vs task relevance;
- Mahalanobis/whitening;
- singular covariance/pseudoinverse;
- kernel viewpoint;
- distance concentration/curse of dimensionality;
- embedding similarity and vector search;
- covariance geometry in finance.

### `09_connections/02_uncertainty_information_and_entropy.md`

Learning flow:

```text
probability
→ surprise
→ entropy
→ compression
→ conditional entropy
→ mutual information
→ KL / cross-entropy
→ decision theory
```

Các phần tăng sâu:

- entropy vs variance;
- coding/Kraft connection;
- data-processing inequality;
- cross-entropy ↔ negative log-likelihood;
- calibration vs entropy;
- expected loss/decision;
- proper scoring rules;
- information gain;
- entropy rate;
- channel capacity;
- compression vs error-correcting redundancy.

### `09_connections/03_math_for_ai_data_and_software.md`

Bản mới không còn chỉ liệt kê “môn toán dùng trong AI”. Nó tổ chức full system dependency:

```text
representation
→ affine/function composition
→ computational graph/autodiff
→ loss geometry
→ optimization
→ probability/calibration
→ statistics/generalization
→ numerical computing
→ production systems
```

Các phần tăng sâu:

- representation is a modeling choice;
- computational graph + chain rule;
- losses encode probabilistic/robustness assumptions;
- empirical vs population risk;
- conditioning/Hessian;
- log-sum-exp stability;
- floating point and mixed precision;
- embedding geometry;
- train/test inference and distribution shift;
- prediction vs causality;
- graph/database/index/cardinality-estimation connections;
- Big-O vs exact runtime;
- observability metrics;
- model correctness vs system correctness.

### `09_connections/05_fourier_signals_and_frequency.md`

Learning flow mới:

```text
oscillation
→ orthogonal basis
→ Fourier series
→ complex exponential
→ Fourier transform
→ convolution
→ LTI systems
→ sampling / aliasing
→ DFT / FFT
```

Các phần tăng sâu:

- Parseval/energy preservation;
- differentiation as frequency multiplication;
- LTI impulse/frequency response;
- time-frequency localization trade-off;
- aliasing derivation intuition;
- Nyquist assumptions;
- DFT as matrix/basis change;
- spectral leakage/windowing;
- frequency resolution vs sample rate;
- filtering/causality trade-off;
- Gibbs phenomenon;
- PDE mode decomposition;
- Fourier features and AI;
- Fourier vs Laplace vs Z-transform mental map.

## Audited but intentionally not rewritten

Round 11 cũng audit các files sau nhưng giữ nguyên vì content hiện tại đã tương đối cân bằng với editorial standard.

### `03_geometry_trigonometry/08_topology_continuity_connectivity.md`

Giữ nguyên vì đã có:

```text
metric / neighborhood
open sets
continuity
connectedness
compactness
homeomorphism
boundary/interior/closure
TDA / robotics connections
```

File đã giải thích đúng distinction topology vs metric geometry và có assumptions/misconceptions đủ rõ.

### `05_calculus/10_partial_differential_equations_and_fields_intro.md`

Giữ nguyên vì đã có coherent chain:

```text
field
→ heat/wave/Laplace equations
→ initial/boundary conditions
→ PDE classification
→ separation of variables/eigenmodes
→ numerical discretization/stability
```

Nội dung đủ cho scope “intro”; viết sâu thêm sẽ bắt đầu thành course PDE riêng.

### `06_probability_statistics/10_likelihood_mle_map_and_model_selection.md`

Giữ nguyên vì chapter đã derive Bernoulli MLE, giải thích log-likelihood/NLL, model-family assumptions và bridge sang ML/statistics. Đây không còn là bottleneck về depth.

### `06_probability_statistics/11_stochastic_processes_markov_chains_and_time_series.md`

Giữ nguyên vì chapter đã có process/sample-path, stationarity/autocorrelation, Markov property, transition structure và time-series bridge. Scope hiện phù hợp với dependency level của library.

### `07_discrete_cs/08_groups_rings_fields_and_algebraic_structures.md`

Giữ nguyên vì đã có group/ring/field, symmetry, subgroup/generator, homomorphism/kernel/image, finite fields, zero divisors, quotient idea và connections với linear algebra/cryptography.

### `09_connections/04_math_for_finance_work_and_daily_life.md`

Giữ nguyên vì đã đủ sâu hơn nhóm connection cũ, gồm compounding, effective rates, discounting, NPV, annuity/loan derivation và quantitative business reasoning.

### `09_connections/06_laplace_z_transform_and_dynamic_systems.md`

Giữ nguyên vì chapter đã có transform definitions, derivative/recurrence simplification, transfer functions, poles/zeros, stability, convolution và continuous/discrete systems perspective.

## Depth balance sau Round 11

Sau Round 11, các bridge chains sau đã cân bằng hơn đáng kể:

```text
formal language → machine memory → computability → complexity
convex geometry → simplex → duality → integer optimization
rate → accumulation → conservation
metric → projection → statistical/ML geometry
probability → entropy → decision
AI model math → numerical/statistical production behavior
trigonometry → Fourier → transforms / PDE / signals
```

## Priority hợp lý cho Round 12

Không nên tiếp tục theo một fixed list chỉ dựa trên file size. Nên chuyển sang **library-wide consistency audit**:

```text
1. cross-links giữa canonical chapters;
2. duplicate explanations giữa topic và 09_connections;
3. terminology consistency VI/EN/KR;
4. notation consistency;
5. prerequisite/dependency order trong README;
6. worked-example quality;
7. assumptions/failure-mode sections;
8. internal links có click được trên reader/site hay không;
9. chapter openings có intuition trước formalism hay không;
10. glossary coverage cho recurring terms.
```

Nếu vẫn cần rewrite content, chỉ chọn chapter bị phát hiện qua consistency audit, thay vì tiếp tục “file nhỏ → viết dài”.

## Kết luận

Round 11 rewrite **7 canonical/connection files**, audit thêm 7 files và chủ động giữ nguyên chúng.

Nguyên tắc được siết chặt hơn:

> Độ hoàn thiện không được đo bằng số dòng. Một library mature cần chuyển từ mở rộng content sang consistency, dependency, notation, cross-link và editorial coherence.