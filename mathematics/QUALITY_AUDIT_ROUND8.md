# Quality Audit — Round 8: strengthen mathematical foundations and probability bridges

Round 8 tiếp tục chiến lược **quality over chapter count**. Mathematics Knowledge Library vẫn giữ nguyên 87 topic; không thêm chapter mới chỉ để tăng coverage.

Mục tiêu của round này là nâng các chapter nền mà nhiều nhánh downstream dựa vào nhưng depth chưa đồng đều với các phần đã rewrite ở Round 5–7.

## Phạm vi Round 8

Round này tập trung tám chapter:

```text
00_foundations/01_logic_and_proof.md
00_foundations/02_sets_relations_and_mappings.md
00_foundations/03_numbers_and_number_systems.md
01_algebra/00_algebraic_language.md
03_geometry_trigonometry/00_euclidean_geometry.md
06_probability_statistics/04_expectation_variance_and_limit_laws.md
07_discrete_cs/03_boolean_algebra_and_digital_logic.md
07_discrete_cs/04_number_theory_and_modular_arithmetic.md
```

Tiêu chí vẫn theo [`EDITORIAL_STANDARD.md`](./EDITORIAL_STANDARD.md): intuition trước formalism, formula/theorem có reason và assumptions, proof idea đủ để hiểu structure, examples tạo reasoning transfer, và connections chỉ thêm khi thật sự cùng mathematical structure.

## Batch 1 — Foundations + Algebraic Language

### Logic and Proof

Bản mới được nâng từ overview logic/proof thành chapter reasoning foundation. Nội dung nhấn mạnh:

```text
proposition
→ implication
→ necessary/sufficient
→ quantifiers
→ negation
→ direct/contrapositive/contradiction
→ induction
→ counterexample
→ proof strategy
→ formal reasoning vs testing
```

Mục tiêu không phải học tên proof methods, mà hiểu khi nào một target theorem gợi ý strategy nào và proof đang bảo toàn logic gì.

### Sets, Relations and Mappings

Bản mới làm rõ set như universe/membership model, relation như subset của Cartesian product và function như relation có uniqueness constraint.

Learning path được nối rõ hơn với:

- database relations;
- graph edges;
- equivalence classes;
- partial orders;
- partitions;
- quotient-style reasoning;
- injectivity/information preservation;
- cardinality và power set.

### Numbers and Number Systems

Bản mới giải thích number-system expansion theo closure problem:

```text
N: counting
→ Z: subtraction
→ Q: division
→ R: completeness / limits
→ C: algebraic closure for polynomial roots + rotation
```

Representation layer được tách khỏi abstract number:

```text
mathematical number
≠ numeral representation
≠ machine representation
```

Điều này nối trực tiếp sang binary/hex, floating point, approximation và numerical computing.

### Algebraic Language

Chapter được nâng theo viewpoint:

> Algebra là transformation của representation trong khi giữ semantic relation.

Các phần variable/domain, expression vs equation, distributivity, identities, inverse operations, reversible transformations và domain restrictions được làm rõ để hỗ trợ các chapter equation/function/calculus phía sau.

## Batch 2 — Euclidean Geometry + Expectation/Variance/Limit Laws

### Euclidean Geometry

Bản mới không coi geometry là collection công thức. Learning flow:

```text
ideal objects
→ axioms / model assumptions
→ distance / angle
→ congruence / similarity
→ triangle structure
→ Pythagorean orthogonality
→ area / volume as measure
→ transformations / invariants
→ coordinate representation
```

Theorem assumptions được làm rõ qua contrast với spherical/non-Euclidean geometry.

Connections chính:

- vector norms;
- least squares;
- geometric optimization;
- graphics;
- physics;
- measurement/model validity.

### Expectation, Variance and Limit Laws

Chapter cũ đúng nhưng quá ngắn so với vai trò central bridge từ Probability sang Statistics.

Bản mới tách rõ bốn câu hỏi:

```text
Expectation → center?
Variance → spread?
LLN → averages stabilize?
CLT → normalized fluctuations have what shape?
```

Nội dung mới gồm:

- linearity of expectation without independence;
- indicator-variable method;
- covariance terms in variance of sums;
- law of total expectation;
- law of total variance;
- variance of sample mean;
- square-root law;
- weak/strong LLN intuition;
- CLT vs LLN distinction;
- effective sample size under dependence;
- heavy-tail limitations;
- Chebyshev inequality;
- AI mini-batch and finance-risk connections.

## Batch 3 — Boolean Algebra + Number Theory

### Boolean Algebra and Digital Logic

Bản mới phân biệt ba layers:

```text
truth semantics
→ algebraic transformation
→ runtime / circuit implementation
```

Nội dung được mở sâu sang:

- Boolean identities;
- XOR as addition mod 2;
- functionally complete gates;
- SOP/POS;
- CNF/SAT;
- short-circuit semantics;
- SQL three-valued logic;
- bit masks;
- parity/error detection;
- Boolean matrix/graph connection;
- hardware assumptions.

### Number Theory and Modular Arithmetic

Bản mới tổ chức theo structure thay vì theorem list:

```text
divisibility
→ division algorithm
→ gcd
→ Euclidean algorithm
→ Bézout
→ primes
→ congruence classes
→ modular inverse
→ Fermat/Euler
→ fast modular exponentiation
→ CRT
→ finite fields
```

Proof ideas được thêm cho Euclidean algorithm, infinitude of primes và modular impossibility arguments.

Connections được làm rõ với algorithms, cyclic systems, hashing, checksums, finite algebra và cryptographic mathematics, đồng thời ghi rõ boundary giữa mathematical substrate và practical system guarantees.

## Depth balance sau Round 8

Sau Round 8, các foundation nodes quan trọng đã cân bằng hơn đáng kể với những chapter advanced.

Các nhóm hiện tương đối mạnh trong current scope:

```text
mathematical thinking
logic & proof
sets / relations / mappings
number systems
algebraic language
functions
Euclidean / coordinate / transformation geometry
trigonometry
linear algebra
calculus / analysis
probability foundations
expectation / variance / LLN / CLT
statistics / regression
boolean algebra
number theory
algorithmic complexity / recurrence
numerical methods
optimization
Fourier / Laplace / control
```

## Remaining depth priorities

Round tiếp theo không nên tăng chapter count. Priority hợp lý là các chapter vẫn ngắn hoặc chưa đồng đều về proof/application depth:

```text
00_foundations/04_measurement_units_and_estimation.md
00_foundations/05_mathematical_modeling_dimensional_analysis_and_scaling.md
02_functions/01_linear_and_quadratic_functions.md
02_functions/03_sequences_and_recurrence.md
03_geometry_trigonometry/06_conic_sections.md
03_geometry_trigonometry/07_trigonometric_identities_harmonics_and_phasors.md
04_vectors_linear_algebra/06_orthogonality_projection_and_inner_products.md
04_vectors_linear_algebra/07_determinant_rank_nullspace_and_inverse.md
05_calculus/07_infinite_series_and_taylor.md
06_probability_statistics/02_conditional_probability_and_bayes.md
06_probability_statistics/07_sampling_confidence_hypothesis_testing.md
07_discrete_cs/05_trees_posets_lattices.md
08_optimization_numerical/02_numerical_methods_and_error.md
09_connections/00_rate_change_accumulation.md
```

Selection cho round sau nên tiếp tục theo **dependency centrality + depth gap**, không theo folder order.

## Editorial conclusion

Round 8 củng cố layer nền của knowledge graph. Mục tiêu là để người đọc không gặp tình trạng chapter advanced rất sâu nhưng các concepts như implication, equivalence relation, completeness, invariance, expectation hoặc congruence chỉ được giải thích ở mức note.

Mental model cho library tiếp tục là:

> Coverage tạo nodes; depth rewrite làm rõ edges; assumptions xác định nơi edge còn hợp lệ. Một knowledge library mạnh không chỉ có nhiều concepts, mà cho người đọc biết vì sao chúng nối với nhau và khi nào connection đó không còn đúng.
