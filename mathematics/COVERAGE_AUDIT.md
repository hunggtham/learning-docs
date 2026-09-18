# Coverage Audit — Master Knowledge Book: Toán

## Phạm vi của từ “hoàn thiện”

“Toán học” là lĩnh vực mở nên không có một volume hữu hạn nào bao phủ mọi nhánh nghiên cứu. Trong bộ này, **hoàn thiện** được định nghĩa là: bao phủ mạch toán phổ thông → nền tảng đại học → các structures toán cốt lõi dùng trong Computer Science, Software Engineering, AI/Data, Statistics, Engineering và quantitative reasoning; đồng thời không để một connection quan trọng dựa trên khái niệm chưa hề được giải thích.

Mỗi topic trong scope phải có explanation theo first principles, công thức chính kèm meaning/conditions, ví dụ hoặc application có thật về structure, Mental Model và Common Misconceptions khi phù hợp.

## Kết quả audit 2026-09-18

Bản sau hai vòng audit có **80 topic files**. Vòng đầu phát hiện các khoảng trống quan trọng ở function composition/inverse, rational functions/domain, conics, harmonic trigonometry, orthogonality/projection, rank/null space, infinite series/Taylor, vector calculus, statistical inference, multivariate probability, information theory, computability, constrained optimization, numerical linear algebra và Fourier analysis. Vòng thứ hai tiếp tục bổ sung mathematical modeling & dimensional analysis, topology nhập môn, PDE nền tảng, likelihood/MLE/MAP, abstract algebra nền tảng, linear programming/duality và Laplace/Z-transform. Các phần này đều được tách thành topic độc lập để dependency graph không phải nhảy qua khái niệm chưa được giải thích.

Toàn bộ topic files hiện đều có `Mental Model` và `Common Misconceptions`. Tổng nội dung Markdown của bộ hiện khoảng **63.900 từ**; con số chỉ là sanity check về độ phủ, không dùng như thước đo chất lượng duy nhất.

## Coverage matrix

| Nhóm | Topic | File | Trạng thái |
|---|---|---|---|
| Foundations | Tư duy toán học và First Principles | `00_foundations/00_mathematical_thinking.md` | Đã rà soát — hoàn thiện trong scope |
| Foundations | Logic và chứng minh | `00_foundations/01_logic_and_proof.md` | Đã rà soát — hoàn thiện trong scope |
| Foundations | Tập hợp, quan hệ và ánh xạ | `00_foundations/02_sets_relations_and_mappings.md` | Đã rà soát — hoàn thiện trong scope |
| Foundations | Số và các hệ số | `00_foundations/03_numbers_and_number_systems.md` | Đã rà soát — hoàn thiện trong scope |
| Foundations | Đo lường, đơn vị và ước lượng | `00_foundations/04_measurement_units_and_estimation.md` | Đã rà soát — hoàn thiện trong scope |
| Foundations | Mô hình toán học, phân tích thứ nguyên và scaling | `00_foundations/05_mathematical_modeling_dimensional_analysis_and_scaling.md` | Bổ sung vòng audit 2 — hoàn thiện trong scope |
| Algebra | Ngôn ngữ đại số: biến, biểu thức và phép biến đổi | `01_algebra/00_algebraic_language.md` | Đã rà soát — hoàn thiện trong scope |
| Algebra | Phương trình và bất phương trình | `01_algebra/01_equations_and_inequalities.md` | Đã rà soát — hoàn thiện trong scope |
| Algebra | Tỉ số, tỉ lệ và phần trăm | `01_algebra/02_ratio_proportion_percentage.md` | Đã rà soát — hoàn thiện trong scope |
| Algebra | Lũy thừa, căn và logarithm | `01_algebra/03_powers_roots_and_logarithms.md` | Đã rà soát — hoàn thiện trong scope |
| Algebra | Đa thức và phân tích nhân tử | `01_algebra/04_polynomials_and_factorization.md` | Đã rà soát — hoàn thiện trong scope |
| Algebra | Số phức: từ nghiệm phương trình đến rotation | `01_algebra/05_complex_numbers.md` | Đã rà soát — hoàn thiện trong scope |
| Algebra | Biểu thức hữu tỉ, miền xác định và tiệm cận | `01_algebra/06_rational_expressions_domain_and_asymptotes.md` | Bổ sung sau audit — hoàn thiện trong scope |
| Functions | Hàm số: quy tắc biến input thành output | `02_functions/00_function_concept.md` | Đã rà soát — hoàn thiện trong scope |
| Functions | Mô hình tuyến tính và bậc hai | `02_functions/01_linear_and_quadratic_models.md` | Đã rà soát — hoàn thiện trong scope |
| Functions | Hàm mũ và logarithmic models | `02_functions/02_exponential_and_logarithmic_models.md` | Đã rà soát — hoàn thiện trong scope |
| Functions | Dãy, chuỗi và recurrence | `02_functions/03_sequences_series_and_recurrence.md` | Đã rà soát — hoàn thiện trong scope |
| Functions | Hợp hàm, hàm ngược và phép biến đổi hàm | `02_functions/04_composition_inverse_and_function_transformations.md` | Bổ sung sau audit — hoàn thiện trong scope |
| Functions | Quan hệ ẩn, tham số và tọa độ cực | `02_functions/05_parametric_polar_and_implicit_relations.md` | Bổ sung sau audit — hoàn thiện trong scope |
| Geometry & Trigonometry | Hình học Euclid: điểm, đường, góc và cấu trúc không gian | `03_geometry_trigonometry/00_euclidean_geometry.md` | Đã rà soát — hoàn thiện trong scope |
| Geometry & Trigonometry | Hình học tọa độ: biến không gian thành algebra | `03_geometry_trigonometry/01_coordinate_geometry.md` | Đã rà soát — hoàn thiện trong scope |
| Geometry & Trigonometry | Định lý Pythagoras và ý tưởng khoảng cách | `03_geometry_trigonometry/02_pythagorean_theorem_and_distance.md` | Đã rà soát — hoàn thiện trong scope |
| Geometry & Trigonometry | Đồng dạng, diện tích, thể tích và scaling laws | `03_geometry_trigonometry/03_similarity_area_volume_and_scaling.md` | Đã rà soát — hoàn thiện trong scope |
| Geometry & Trigonometry | Lượng giác: góc, tỷ số và dao động | `03_geometry_trigonometry/04_trigonometry.md` | Đã rà soát — hoàn thiện trong scope |
| Geometry & Trigonometry | Phép biến hình và đối xứng | `03_geometry_trigonometry/05_transformations_and_symmetry.md` | Đã rà soát — hoàn thiện trong scope |
| Geometry & Trigonometry | Đường tròn, conic sections và quỹ tích | `03_geometry_trigonometry/06_circles_conics_and_loci.md` | Bổ sung sau audit — hoàn thiện trong scope |
| Geometry & Trigonometry | Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa | `03_geometry_trigonometry/07_trigonometric_identities_equations_and_harmonics.md` | Bổ sung sau audit — hoàn thiện trong scope |
| Geometry & Trigonometry | Nhập môn topology: continuity, connectivity và shape không phụ thuộc thước đo | `03_geometry_trigonometry/08_topology_continuity_connectivity.md` | Bổ sung vòng audit 2 — hoàn thiện trong scope |
| Vectors & Linear Algebra | Vector: đại lượng có nhiều thành phần và hướng | `04_vectors_linear_algebra/00_vectors.md` | Đã rà soát — hoàn thiện trong scope |
| Vectors & Linear Algebra | Ma trận và hệ phương trình tuyến tính | `04_vectors_linear_algebra/01_matrices_and_linear_systems.md` | Đã rà soát — hoàn thiện trong scope |
| Vectors & Linear Algebra | Phép biến đổi tuyến tính | `04_vectors_linear_algebra/02_linear_transformations.md` | Đã rà soát — hoàn thiện trong scope |
| Vectors & Linear Algebra | Không gian vector, cơ sở và số chiều | `04_vectors_linear_algebra/03_vector_spaces_basis_dimension.md` | Đã rà soát — hoàn thiện trong scope |
| Vectors & Linear Algebra | Eigenvalues và eigenvectors: những hướng không đổi dưới transformation | `04_vectors_linear_algebra/04_eigenvalues_and_eigenvectors.md` | Đã rà soát — hoàn thiện trong scope |
| Vectors & Linear Algebra | Least squares, SVD và matrix decompositions | `04_vectors_linear_algebra/05_least_squares_svd_and_decompositions.md` | Đã rà soát — hoàn thiện trong scope |
| Vectors & Linear Algebra | Inner product, trực giao và phép chiếu | `04_vectors_linear_algebra/06_inner_product_orthogonality_and_projection.md` | Bổ sung sau audit — hoàn thiện trong scope |
| Vectors & Linear Algebra | Determinant, rank, null space và nghịch đảo ma trận | `04_vectors_linear_algebra/07_determinant_rank_nullspace_and_inverse.md` | Bổ sung sau audit — hoàn thiện trong scope |
| Calculus | Giới hạn và tính liên tục | `05_calculus/00_limits_and_continuity.md` | Đã rà soát — hoàn thiện trong scope |
| Calculus | Đạo hàm: tốc độ thay đổi cục bộ | `05_calculus/01_derivatives.md` | Đã rà soát — hoàn thiện trong scope |
| Calculus | Ứng dụng của đạo hàm: shape, approximation và optimization | `05_calculus/02_derivative_applications.md` | Đã rà soát — hoàn thiện trong scope |
| Calculus | Tích phân: tích lũy từ những đóng góp vi phân | `05_calculus/03_integrals_and_accumulation.md` | Đã rà soát — hoàn thiện trong scope |
| Calculus | Giải tích nhiều biến: gradient, Jacobian và tối ưu trong nhiều chiều | `05_calculus/04_multivariable_calculus.md` | Đã rà soát — hoàn thiện trong scope |
| Calculus | Phương trình vi phân và hệ động lực | `05_calculus/05_differential_equations.md` | Đã rà soát — hoàn thiện trong scope |
| Calculus | Giải tích số: khi máy tính phải xấp xỉ calculus | `05_calculus/06_numerical_calculus.md` | Đã rà soát — hoàn thiện trong scope |
| Calculus | Chuỗi vô hạn, power series và sự hội tụ | `05_calculus/07_infinite_series_power_series_and_convergence.md` | Bổ sung sau audit — hoàn thiện trong scope |
| Calculus | Taylor approximation: từ đạo hàm đến mô hình cục bộ nhiều bậc | `05_calculus/08_taylor_series_and_local_approximation.md` | Bổ sung sau audit — hoàn thiện trong scope |
| Calculus | Vector calculus: gradient, divergence, curl và tích phân trên đường/mặt | `05_calculus/09_vector_calculus.md` | Bổ sung sau audit — hoàn thiện trong scope |
| Calculus | Nhập môn phương trình vi phân riêng phần: fields, heat, wave và boundary conditions | `05_calculus/10_partial_differential_equations_and_fields_intro.md` | Bổ sung vòng audit 2 — hoàn thiện trong scope |
| Probability & Statistics | Đếm và tổ hợp | `06_probability_statistics/00_counting_and_combinatorics.md` | Đã rà soát — hoàn thiện trong scope |
| Probability & Statistics | Nền tảng xác suất: mô hình hóa bất định | `06_probability_statistics/01_probability_foundations.md` | Đã rà soát — hoàn thiện trong scope |
| Probability & Statistics | Xác suất có điều kiện và định lý Bayes | `06_probability_statistics/02_conditional_probability_and_bayes.md` | Đã rà soát — hoàn thiện trong scope |
| Probability & Statistics | Biến ngẫu nhiên và phân phối | `06_probability_statistics/03_random_variables_and_distributions.md` | Đã rà soát — hoàn thiện trong scope |
| Probability & Statistics | Kỳ vọng, phương sai và các luật giới hạn | `06_probability_statistics/04_expectation_variance_and_limit_laws.md` | Đã rà soát — hoàn thiện trong scope |
| Probability & Statistics | Thống kê mô tả và suy luận | `06_probability_statistics/05_descriptive_and_inferential_statistics.md` | Đã rà soát — hoàn thiện trong scope |
| Probability & Statistics | Hồi quy và tương quan | `06_probability_statistics/06_regression_and_correlation.md` | Đã rà soát — hoàn thiện trong scope |
| Probability & Statistics | Lấy mẫu, ước lượng, confidence interval và hypothesis testing | `06_probability_statistics/07_sampling_estimation_confidence_and_hypothesis_testing.md` | Bổ sung sau audit — hoàn thiện trong scope |
| Probability & Statistics | Covariance, xác suất nhiều biến và multivariate Gaussian | `06_probability_statistics/08_covariance_multivariate_probability_and_gaussian.md` | Bổ sung sau audit — hoàn thiện trong scope |
| Probability & Statistics | Các phân phối xác suất thường gặp và vì sao chúng xuất hiện | `06_probability_statistics/09_common_distributions_and_when_they_arise.md` | Bổ sung sau audit — hoàn thiện trong scope |
| Probability & Statistics | Likelihood, MLE, MAP và chọn mô hình từ dữ liệu | `06_probability_statistics/10_likelihood_mle_map_and_model_selection.md` | Bổ sung vòng audit 2 — hoàn thiện trong scope |
| Discrete Mathematics & Theoretical CS | Lý thuyết đồ thị: toán học của mạng lưới và quan hệ | `07_discrete_cs/00_graph_theory.md` | Đã rà soát — hoàn thiện trong scope |
| Discrete Mathematics & Theoretical CS | Độ phức tạp thuật toán và ý nghĩa của logarithm | `07_discrete_cs/01_algorithms_complexity_and_logarithms.md` | Đã rà soát — hoàn thiện trong scope |
| Discrete Mathematics & Theoretical CS | Recurrence, induction và đệ quy trong thuật toán | `07_discrete_cs/02_recurrence_and_induction_in_algorithms.md` | Đã rà soát — hoàn thiện trong scope |
| Discrete Mathematics & Theoretical CS | Boolean algebra và logic số | `07_discrete_cs/03_boolean_algebra_and_digital_logic.md` | Đã rà soát — hoàn thiện trong scope |
| Discrete Mathematics & Theoretical CS | Lý thuyết số và số học modulo | `07_discrete_cs/04_number_theory_and_modular_arithmetic.md` | Đã rà soát — hoàn thiện trong scope |
| Discrete Mathematics & Theoretical CS | Cây, thứ tự bộ phận và lattice | `07_discrete_cs/05_trees_posets_and_lattices.md` | Bổ sung sau audit — hoàn thiện trong scope |
| Discrete Mathematics & Theoretical CS | Information theory, entropy và coding | `07_discrete_cs/06_information_theory_and_coding.md` | Bổ sung sau audit — hoàn thiện trong scope |
| Discrete Mathematics & Theoretical CS | Automata, formal languages và computability | `07_discrete_cs/07_automata_formal_languages_and_computability.md` | Bổ sung sau audit — hoàn thiện trong scope |
| Discrete Mathematics & Theoretical CS | Cấu trúc đại số: group, ring và field | `07_discrete_cs/08_groups_rings_fields_and_algebraic_structures.md` | Bổ sung vòng audit 2 — hoàn thiện trong scope |
| Optimization & Numerical Mathematics | Tối ưu hóa: mục tiêu, ràng buộc và trade-off | `08_optimization_numerical/00_optimization.md` | Đã rà soát — hoàn thiện trong scope |
| Optimization & Numerical Mathematics | Gradient descent, learning rate và geometry của optimization | `08_optimization_numerical/01_gradient_descent_and_convexity.md` | Đã rà soát — hoàn thiện trong scope |
| Optimization & Numerical Mathematics | Toán số: approximation, conditioning và stability | `08_optimization_numerical/02_numerical_methods_and_error.md` | Đã rà soát — hoàn thiện trong scope |
| Optimization & Numerical Mathematics | Tối ưu có ràng buộc, Lagrange multipliers và KKT | `08_optimization_numerical/03_constrained_optimization_lagrange_and_kkt.md` | Bổ sung sau audit — hoàn thiện trong scope |
| Optimization & Numerical Mathematics | Root finding, interpolation và numerical linear algebra | `08_optimization_numerical/04_root_finding_interpolation_and_numerical_linear_algebra.md` | Bổ sung sau audit — hoàn thiện trong scope |
| Optimization & Numerical Mathematics | Linear programming, duality và simplex | `08_optimization_numerical/05_linear_programming_duality_and_simplex.md` | Bổ sung vòng audit 2 — hoàn thiện trong scope |
| Knowledge Connections | Knowledge Connection — Rate, Change và Accumulation | `09_connections/00_rate_change_and_accumulation.md` | Đã rà soát — hoàn thiện trong scope |
| Knowledge Connections | Knowledge Connection — Distance, Similarity và Projection | `09_connections/01_distance_similarity_and_projection.md` | Đã rà soát — hoàn thiện trong scope |
| Knowledge Connections | Knowledge Connection — Xác suất, thông tin và entropy | `09_connections/02_uncertainty_information_and_entropy.md` | Đã rà soát — hoàn thiện trong scope |
| Knowledge Connections | Knowledge Connection — Toán trong AI, Data và Software Engineering | `09_connections/03_math_for_ai_data_and_software.md` | Đã rà soát — hoàn thiện trong scope |
| Knowledge Connections | Knowledge Connection — Toán trong tài chính, công việc và đời sống | `09_connections/04_math_for_finance_work_and_daily_life.md` | Đã rà soát — hoàn thiện trong scope |
| Knowledge Connections | Fourier, tín hiệu và miền tần số | `09_connections/05_fourier_signals_and_frequency.md` | Bổ sung sau audit — hoàn thiện trong scope |
| Knowledge Connections | Laplace transform, Z-transform và dynamic systems | `09_connections/06_laplace_z_transform_and_dynamic_systems.md` | Bổ sung vòng audit 2 — hoàn thiện trong scope |

## Những phần đã được làm rõ sau audit

### Functions không còn dừng ở `f(x)`

Bản cũ có domain/codomain và function concept nhưng chưa đủ cầu nối tới composition, inverse, coordinate transformations và implicit/parametric representations. Bản mới tách riêng các topics này để chain rule, graphics, robotics và coordinate changes có prerequisite rõ ràng.

### Linear algebra không còn thiếu geometry trung tâm

Dot product/projection, determinant/rank/null space trước đây nằm rải rác hoặc quá ngắn. Các phần mới giải thích projection như nearest-point problem, least squares như subspace projection, determinant như volume scaling, rank/nullity như accounting của dimensions và inverse như reversibility.

### Calculus đã nối local approximation với fields

Infinite series, Taylor approximation và vector calculus được thêm để calculus không dừng ở derivative/integral một biến. Gradient–divergence–curl và integral theorems tạo cầu sang physics, optimization, graphics và PDE.

### Probability/Statistics đã tách descriptive knowledge khỏi inference

Sampling distribution, standard error, confidence interval, hypothesis testing, Type I/II errors, power, covariance matrix và multivariate Gaussian nay có chapter riêng. Điều này tránh các cách hiểu sai phổ biến như “p-value là xác suất H0 sai” hoặc “correlation 0 nghĩa independent”.

### Discrete/CS đã mở rộng từ graph/complexity sang limits của computation

Trees/posets/lattices, information theory/coding và automata/computability được thêm. Nhờ đó dependency graphs, compiler/static analysis, compression, cross-entropy và decidability không còn xuất hiện như application không có nền toán.

### Numerical/Optimization đã bổ sung reliability và constraints

KKT/Lagrange, root finding, interpolation, factorization, conditioning và floating-point được tách rõ. Mục tiêu là hiểu không chỉ “tìm nghiệm”, mà còn biết nghiệm số có đáng tin hay không và constraint thay đổi geometry của optimum thế nào.

### Vòng audit thứ hai đã lấp các cầu nối liên ngành còn thiếu

Mathematical modeling và dimensional analysis được thêm để phân biệt rõ “thế giới thật” với model và để kiểm tra consistency của equation trước khi tính. Topology nhập môn giải thích continuity/connectivity ở mức structure thay vì chỉ dựa vào distance. PDE nối vector calculus với heat, wave, diffusion và boundary conditions. Likelihood/MLE/MAP tạo cầu từ probability sang statistical learning. Group/ring/field cho thấy symmetry, modular arithmetic và algebraic structure dùng chung một mental model. Linear programming/duality làm rõ optimization với feasible region tuyến tính và shadow price. Laplace/Z-transform nối differential/difference equations với signal, control và dynamic systems.

## Những lĩnh vực cố ý ngoài scope

Các lĩnh vực sau không bị đánh dấu “thiếu” vì chúng thuộc volume chuyên sâu riêng: measure-theoretic probability, real/complex analysis chứng minh chuyên sâu, abstract algebra chuyên sâu, topology chuyên sâu, differential geometry chuyên sâu, functional analysis, stochastic calculus, advanced PDE, numerical PDE, algebraic geometry, category theory, advanced optimization theory và research-level mathematical logic.

Nếu mở rộng bộ sách sau này, các mảng này nên được thêm thành volume/folder riêng thay vì làm phình các chapter nền tảng hiện tại.

## Kiểm tra chất lượng cấu trúc

Một audit hoàn chỉnh không chỉ kiểm tra có file hay chưa. Bộ hiện được kiểm tra theo các invariant sau: mọi topic file có heading cấp 1; không có file rỗng; code fences cân bằng; mọi topic có Mental Model và Common Misconceptions; README link đúng tới file tồn tại; dependency graph không buộc người đọc học tuyến tính từ “dễ đến khó”, mà chỉ mô tả prerequisite logic.
