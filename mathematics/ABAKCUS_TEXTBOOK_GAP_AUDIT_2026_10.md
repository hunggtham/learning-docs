# Abakcus Free Math Textbooks — Coverage Gap Audit (2026-10-04)

## 1. Mục tiêu

Audit này đối chiếu catalog **Free Math Textbooks from University Mathematicians** của Abakcus với canonical library `mathematics/` trong repository.

Mục tiêu **không** phải import hoặc tóm tắt toàn bộ textbook. Catalog được dùng như một external coverage signal để trả lời:

1. domain nào repo đã đủ rộng và không cần thêm;
2. domain nào có conceptual gap rõ ràng;
3. textbook/open resource nào nên được giữ như nguồn học sâu hơn;
4. chapter mới nào thực sự cải thiện dependency graph của library.

Nội dung chapter mới là nội dung giải thích nguyên bản của repository. Không sao chép textbook text.

Nguồn catalog:

- Abakcus — https://abakcus.com/book-lists/free-math-textbooks

Nguồn official/author/university được ưu tiên khi link tài liệu học sâu hơn.

## 2. Kết quả tổng quát

Catalog Abakcus chia free mathematics textbooks thành 13 nhóm lớn. `mathematics/` trước audit đã có 87 topic files và đã bao phủ rất mạnh phần core undergraduate mathematics: foundations/proof, algebra, functions, geometry/trigonometry, linear algebra, calculus, ODE/PDE, probability/statistics, discrete mathematics, numerical methods, optimization và applied connections.

Vì vậy audit **không tạo lại** các chapter đã tồn tại. Gap có giá trị nhất nằm ở các transition từ core undergraduate sang advanced undergraduate:

```text
real analysis intro
→ metric spaces / uniform convergence / measure

inferential statistics
→ experimental design
→ statistical learning / generalization

groups-rings-fields intro
→ quotients / actions / ideals / extensions / Galois

number theory core
→ Diophantine structure / quadratic residues / continued fractions / elliptic curves
```

Kết quả: thêm **5 topic files**, đưa library từ **87 → 92 topic files**.

## 3. Mapping 13 nhóm Abakcus với coverage hiện tại

| Abakcus subject | Coverage trước audit | Quyết định | Lý do |
|---|---|---|---|
| Algebra | Core algebra rất mạnh; abstract algebra mới ở mức nhập môn | **Mở rộng** | Thiếu quotient groups, actions, ideals, field extensions và Galois bridge |
| Linear Algebra | Rất mạnh: vectors, matrices, transformations, basis, eigen, SVD, projection, rank/null space, tensors, matrix calculus | Giữ nguyên | Không có conceptual dependency gap đáng kể |
| Calculus | Rất mạnh: limits → derivatives → integrals → multivariable/vector calculus → series/Taylor | Giữ nguyên | Catalog chủ yếu trùng coverage hiện tại |
| Analysis | Có real-analysis intro + topology + complex analysis | **Mở rộng** | Thiếu bridge riêng về metric spaces, completeness, uniform convergence, measure và `L^p` |
| Differential Equations | Có ODE, PDE intro, Laplace/dynamic systems | Giữ nguyên | Coverage đủ cho scope cross-domain hiện tại |
| Number Theory | Core mạnh: gcd, Bézout, primes, congruence, inverse, Fermat/Euler, CRT, finite fields | **Mở rộng** | Thiếu Diophantine equations, multiplicative order, quadratic residues/reciprocity, continued fractions, Pell, elliptic curves |
| Discrete Mathematics & Combinatorics | Graphs, recurrence, posets/lattices, Boolean algebra, automata, information theory đã có | Giữ nguyên | Không có gap đủ lớn để tạo chapter mới |
| Proofs & Foundations | Mathematical thinking, logic/proof, sets/relations/mappings đã có | Giữ nguyên | Đã là prerequisite layer canonical |
| Geometry & Trigonometry | Euclidean/coordinate geometry, conics, transformations, trigonometry, harmonics, topology intro đã có | Giữ nguyên | Coverage rộng hơn catalog cần thiết cho library hiện tại |
| Probability | Foundations, Bayes, RV/distributions, expectation/limit laws, multivariate, stochastic processes, Bayesian inference đã có | Giữ nguyên | Core probability không thiếu |
| Statistics & Data Science | Descriptive/inferential, regression, testing, MLE/MAP/Bayesian đã có | **Mở rộng** | Thiếu experimental design và statistical learning/generalization layer |
| Applied & Engineering Mathematics | Numerical methods, optimization, Fourier, Laplace/Z, control connections đã có | Giữ nguyên | Đã có strong applied bridge |
| General & Popular Mathematics | Mathematical thinking + cross-domain connection chapters đã phục vụ vai trò này | Giữ nguyên | Không nên tạo một “popular math” silo cạnh canonical concept graph |

## 4. Chapter mới

### 4.1 Advanced analysis bridge

`05_calculus/13_metric_spaces_uniform_convergence_and_measure_intro.md`

Bổ sung:

- metric spaces và open balls;
- sequence convergence trong abstract space;
- Cauchy sequence và completeness;
- pointwise vs uniform convergence;
- sup norm;
- interchange of limits/integrals;
- measure, sigma-algebra, almost everywhere;
- `L^p` / `L^2` intuition;
- dominated-convergence pattern;
- connection sang probability, numerical analysis và statistical learning.

Reference ưu tiên:

- Jiří Lebl, **Basic Analysis** — https://www.jirka.org/ra/

### 4.2 Experimental design

`06_probability_statistics/13_experimental_design_randomization_blocking_and_anova.md`

Bổ sung:

- experimental unit/treatment/response;
- randomization và causal comparability;
- replication;
- blocking/matched pairs;
- factorial designs/interactions;
- confounding;
- ANOVA và degrees of freedom;
- multiple comparisons;
- fractional factorial designs;
- power;
- A/B-testing design complications;
- ANOVA ↔ regression connection.

Reference ưu tiên:

- R. A. Bailey, **Design of Comparative Experiments** — https://webspace.maths.qmul.ac.uk/r.a.bailey/bookbeam.pdf

### 4.3 Statistical learning

`06_probability_statistics/14_statistical_learning_bias_variance_regularization_and_validation.md`

Bổ sung:

- expected risk vs empirical risk;
- train/validation/test;
- data leakage;
- underfitting/overfitting;
- bias–variance decomposition;
- ridge/L2 và lasso/L1;
- regularization ↔ constraints ↔ MAP;
- basis expansion;
- cross-validation/nested CV;
- high-dimensional settings;
- effective complexity;
- classification metrics/calibration;
- distribution shift;
- model misspecification;
- optimization vs statistical generalization.

References ưu tiên:

- Hastie, Tibshirani, Friedman, **The Elements of Statistical Learning** — https://hastie.su.domains/ElemStatLearn/main.html
- Deisenroth, Faisal, Ong, **Mathematics for Machine Learning** — https://mml-book.github.io/

### 4.4 Abstract algebra depth

`07_discrete_cs/09_abstract_algebra_quotients_actions_and_field_extensions.md`

Bổ sung:

- cosets/Lagrange;
- normal subgroups và quotient groups;
- first isomorphism theorem;
- group actions, orbit/stabilizer, Burnside idea;
- Sylow theorem intuition;
- ideals và quotient rings;
- polynomial rings/irreducibility;
- field extensions/minimal polynomials;
- finite fields;
- splitting fields/Galois group;
- solvability by radicals high-level bridge.

Reference ưu tiên:

- Thomas W. Judson, **Abstract Algebra: Theory and Applications** — https://judsonbooks.org/abstract-algebra-theory-and-applications/

### 4.5 Number theory depth

`07_discrete_cs/10_number_theory_diophantine_quadratic_residues_and_crypto.md`

Bổ sung:

- linear Diophantine equations;
- multiplicative order/primitive roots;
- discrete logarithm;
- quadratic residues và Legendre symbol;
- Euler criterion/quadratic reciprocity;
- continued fractions;
- Pell equations;
- primality testing vs factoring;
- RSA mathematical structure;
- CRT as ring decomposition;
- elliptic curves và finite-field group structure;
- local-to-global reasoning.

Reference ưu tiên:

- William Stein, **Elementary Number Theory: Primes, Congruences, and Secrets** — https://github.com/williamstein/ent
- AIM Open Textbook Initiative entry — https://aimath.org/textbooks/approved-textbooks/stein/

## 5. Những gì cố ý không thêm

### Không thêm một chapter calculus khác

Existing library đã có limits, derivatives, applications, integrals, multivariable calculus, vector calculus, infinite series và Taylor. Open calculus books trong catalog useful như alternative explanations/exercises, nhưng không tạo conceptual node mới.

### Không thêm một linear-algebra course khác

Existing library đã đi xa hơn textbook intro thông thường tới SVD/decompositions, projection, determinant/rank/nullspace, tensors và matrix calculus/autodiff.

### Không tạo `popular-math/`

Repository được tổ chức theo dependency graph. General/popular resources nên feed examples, intuition và reading references vào canonical topics, không tạo một silo taxonomy mới.

### Không copy textbook chapters

External books được dùng để audit coverage và làm further-reading sources. Canonical repository tiếp tục giữ cách giải thích riêng theo `EDITORIAL_STANDARD.md`.

## 6. Learning routes sau audit

### Pure / theoretical route

```text
Logic & Proof
→ Sets / Relations / Mappings
→ Number Systems
→ Real Analysis
→ Metric Spaces / Uniform Convergence / Measure
→ Topology / deeper analysis
```

```text
Number Theory Core
→ Groups / Rings / Fields
→ Advanced Abstract Algebra
→ Advanced Number Theory
```

### Data / AI route

```text
Linear Algebra
→ Probability
→ Regression
→ Statistical Inference
→ Statistical Learning
→ Optimization / Matrix Calculus
```

### Experiment / product analytics route

```text
Probability
→ Sampling & Hypothesis Testing
→ Experimental Design
→ Regression / Statistical Learning
```

## 7. Audit rule cho lần sau

Khi gặp một external textbook list khác, không dùng số lượng books làm proxy cho coverage. Quy trình nên là:

```text
external taxonomy
→ map sang canonical concept graph
→ identify missing dependency or missing depth transition
→ inspect current chapter depth
→ add only reusable conceptual node
→ attach official/open reference
```

Điều này giữ library sâu nhưng không phình thành một collection tài liệu trùng lặp.
