# Quality Audit — Round 5: nâng chất lượng biên soạn

Round 5 chuyển trọng tâm từ **mở rộng số lượng topic** sang **nâng độ hoàn thiện và chất lượng viết** của những chapter đã tồn tại.

## Mục tiêu

Các vòng trước chủ yếu giải quyết coverage: thêm các topic còn thiếu để knowledge graph không bị nhảy cóc. Sau khi coverage đã rộng, vấn đề nổi bật hơn là chất lượng không đồng đều: chapter mới thường có reasoning, derivation và connections tốt hơn, trong khi một số chapter cũ vẫn giống expanded notes.

Round này đặt ra chuẩn mới: một chapter chỉ được xem là mạnh khi người đọc có thể hiểu **problem → definition → mechanism → derivation → example → assumptions/failure modes → connection → mental model**, thay vì chỉ đọc danh sách definitions và formulas.

Chuẩn đó được ghi thành file [`EDITORIAL_STANDARD.md`](./EDITORIAL_STANDARD.md) để dùng cho các vòng rewrite sau.

## Các chapter đã rewrite

### Functions — `02_functions/00_function_concept.md`

Bản mới mở rộng function từ “input → output” thành một concept structural: relation vs function, domain/codomain/range, injective/surjective/bijective, invertibility như information preservation, composition như pipeline, piecewise modeling, parameterized function families, equality của functions, connection tới type/API contract và random variables.

Mục tiêu là để người đọc hiểu function như một mapping có contract, không đồng nhất function với một formula.

### Functions — `02_functions/02_exponential_and_logarithmic_models.md`

Bản mới derive exponential từ repeated proportional growth và từ differential equation `dA/dt=kA`; logarithm được giải thích như inverse/multiplicative depth thay vì chỉ bảng rules.

Chapter bổ sung compound interest, Rule of 72 derivation, semi-log modeling và noise model, pH/decibel, algorithmic `O(log n)`, logistic limitation, exponential như eigenfunction của differentiation và information-theory connection.

### Linear Algebra — `04_vectors_linear_algebra/03_vector_spaces_basis_dimension.md`

Bản mới xây từ linear combination → span → independence → basis → dimension → subspace → rank-nullity. Basis được giải thích như coordinate vocabulary; change of basis được nối với eigenbasis, PCA, Fourier và representations trong ML.

Chapter cũng nói rõ giới hạn của vector-space model và curse of dimensionality, thay vì chỉ định nghĩa các term.

### Calculus — `05_calculus/00_limits_and_continuity.md`

Bản mới giải thích limit như tolerance contract, thêm epsilon–delta reasoning thực sự, indeterminate forms, sequence viewpoint, types of discontinuity, uniform continuity, asymptotic growth, derivative/infinite-series connection và numerical-computing distinction.

Mục tiêu là biến limit từ một “kỹ thuật thay số” thành foundation reasoning của calculus.

### Geometry & Trigonometry — `03_geometry_trigonometry/04_trigonometry.md`

Bản mới chuyển trọng tâm từ SOH-CAH-TOA sang unit-circle/rotation viewpoint. Sine/cosine được derive như coordinates của rotation; radian được giải thích bằng arc length và calculus; addition formulas được nối với rotation-matrix composition.

Chapter cũng thêm phase, sinusoidal motion, Euler formula, Fourier viewpoint, sampling/aliasing, vector cosine similarity, 3D rotations và degree/radian API bugs.

### Discrete Mathematics — `07_discrete_cs/00_graph_theory.md`

Bản mới mở rộng từ basic graph/BFS/DFS sang một chapter modeling đầy đủ hơn: graph semantics, connectivity, trees/spanning trees/MST, DAG/topological order, shortest paths, SCC, bipartite matching, coloring, Euler/Hamilton distinction, graph matrices/Laplacian, random walks, flow/cut và software-system modeling.

Điểm nhấn là “algorithm đúng không cứu được graph model sai”.

### Numerical Mathematics — `08_optimization_numerical/02_numerical_methods_and_error.md`

Bản mới tách rõ model error, measurement error, discretization error, conditioning và stability. Nội dung bổ sung floating-point representation, cancellation, forward/backward error, root finding derivation, interpolation/basis conditioning, numerical integration, Monte Carlo, sparse/iterative linear algebra, ODE stability, scaling, reproducibility và mixed precision.

Chapter được viết để tạo engineering judgment thay vì collection numerical methods.

## Chuẩn viết mới

Từ round này trở đi, các chapter được audit theo các tiêu chí chính:

- definition phải đi cùng intuition;
- formula quan trọng phải có provenance và assumptions;
- giải thích chính phải là paragraph có causal flow;
- example phải giúp transfer reasoning, không chỉ “thay số”; 
- model, theorem và computation cần phân biệt rõ;
- failure modes phải được nói ra;
- connection giữa domains chỉ dùng khi thực sự có cùng mathematical structure;
- Mental Model phải tạo reusable way of thinking;
- Common Misconceptions phải giải thích vì sao intuition sai xuất hiện.

Chi tiết nằm trong [`EDITORIAL_STANDARD.md`](./EDITORIAL_STANDARD.md).

## Nhóm ưu tiên cho round tiếp theo

Các file còn ngắn so với vai trò dependency và nên tiếp tục được rewrite theo standard mới gồm:

1. `03_geometry_trigonometry/02_pythagorean_theorem_and_distance.md`
2. `03_geometry_trigonometry/03_similarity_area_volume_and_scaling.md`
3. `03_geometry_trigonometry/05_transformations_and_symmetry.md`
4. `04_vectors_linear_algebra/01_matrices_and_linear_systems.md`
5. `04_vectors_linear_algebra/02_linear_transformations.md`
6. `04_vectors_linear_algebra/05_least_squares_svd_and_decompositions.md`
7. `05_calculus/01_derivatives.md`
8. `05_calculus/02_derivative_applications.md`
9. `05_calculus/04_multivariable_calculus.md`
10. `06_probability_statistics/01_probability_foundations.md`
11. `06_probability_statistics/03_random_variables_and_distributions.md`
12. `07_discrete_cs/01_algorithms_complexity_and_logarithms.md`
13. `08_optimization_numerical/00_optimization.md`

Round sau nên tiếp tục ưu tiên dependency centrality trước file count: rewrite những concept nhiều chapter khác dựa vào trước khi mở rộng thêm research-level topics.

## Mental Model cho quá trình biên soạn

> Coverage xây các node của knowledge graph; quality rewrite làm rõ các edge giữa chúng. Một library có nhiều file nhưng các edge mờ vẫn khiến người đọc phải tự nối kiến thức. Mục tiêu tiếp theo là làm cho reasoning path trở nên nhìn thấy được ngay trong từng chapter.