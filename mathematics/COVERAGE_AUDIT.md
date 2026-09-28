# Coverage & Finalization kiểm tra (audit / 감사) — Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리)

> **Mạch đọc:** Đặt **Coverage & Finalization kiểm tra (audit / 감사) — Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Kết luận chuẩn gốc (canonical / 정본) — 2026-09-22** sang **Tiêu chí kiểm tra (audit / 감사)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## Kết luận chuẩn gốc (canonical / 정본) — 2026-09-22

`mathematics/` là Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리) chuẩn gốc (canonical / 정본) duy nhất của repository. Finalization đã hoàn tất ở mức **content + merge**: 87 topic được giữ nguyên, không tạo chapter để tăng coverage, README/phụ thuộc (dependency / 의존성) routes/glossary/nội bộ (internal / 내부) links đã được chuẩn hóa và PR #41 đã được squash-merge vào `main`.

Chuẩn gốc (canonical / 정본) merge lần ghi nhận (commit / 커밋):

```text
2714ce4529ef9d62ea2ae8e36ad2c299ae347e83
```

Sau merge, `main` đã được đọc lại từ GitHub và xác nhận đang trỏ đúng lần ghi nhận (commit / 커밋) trên. Finalization branch có cùng cây (tree / 트리) SHA `ffd30e10adaf72e2630cb20c1b6c5d8bbfa51c82` với squash lần ghi nhận (commit / 커밋) tại thời điểm merge, nên toàn bộ nội dung finalization đã được canonicalize vào `main`.

Điểm duy nhất chưa thể thực hiện tự động trong phiên này là **xóa branch ref**: GitHub connector hiện có create/move ref nhưng không expose delete branch/delete ref. Vì vậy các branch cũ được đánh dấu **reviewed + safe-to-delete**, nhưng không được ghi sai rằng chúng đã bị xóa.

> Coverage tạo nút (node / 노드); độ sâu (depth / 깊이) làm nút (node / 노드) tự đứng được; finalization làm phụ thuộc (dependency / 의존성) và điều hướng (navigation / 내비게이션) rõ ràng; canonicalization bảo đảm chỉ `main` là nguồn chuẩn (source of truth / 정본).


> **Chuyển mạch:** Từ **Kết luận chuẩn gốc (canonical / 정본) — 2026-09-22**, ta sang **Tiêu chí kiểm tra (audit / 감사)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tiêu chí kiểm tra (audit / 감사)

Mỗi chapter được rà soát (review / 검토) theo cùng chuẩn gốc (canonical / 정본) tiêu chuẩn (standard / 표준):

1. Công thức quan trọng có meaning và provenance, không chỉ là quy tắc (rule / 규칙) để nhớ.
2. Ký hiệu được định nghĩa đủ để đọc độc lập trong phạm vi (scope / 범위) chapter.
3. giả định (assumption / 가정), lĩnh vực (domain / 도메인) và validity điều kiện (condition / 조건) được nói rõ khi chúng ảnh hưởng kết luận.
4. Người đọc hiểu vấn đề concept tồn tại để giải quyết và vì sao formalism có dạng hiện tại.
5. Có intuition/geometric/structural example khi phù hợp.
6. Có ứng dụng (application / 애플리케이션) example đủ để transfer lập luận (reasoning / 추론).
7. Worked example không bỏ qua bước lập luận (reasoning / 추론) quan trọng.
8. Không có hidden prerequisite lớn buộc người đọc phải tìm nguồn ngoài chỉ để hiểu section hiện tại.
9. Prerequisite/downstream liên kết (connection / 연결) được chỉ ra khi dùng chung (shared / 공유) cấu trúc (structure / 구조) thực sự tồn tại.
10. Chapter không bị biến thành encyclopedia/danh sách (list / 목록) of facts.
11. dạng thất bại (failure mode / 실패 모드), misconception hoặc ranh giới (boundary / 경계) được nêu khi dễ dùng sai.
12. Cross-domain liên kết (connection / 연결) với CS/Algorithms/AI/dữ liệu (data / 데이터)/Physics/Finance/Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) dựa trên cùng mathematical cấu trúc (structure / 구조), không chỉ nhắc tên ứng dụng.

Chuẩn biên soạn chi tiết: [EDITORIAL_STANDARD.md](./EDITORIAL_STANDARD.md).


> **Chuyển mạch:** Từ **Tiêu chí kiểm tra (audit / 감사)**, ta sang **Phương pháp final kiểm tra (audit / 감사)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Phương pháp final kiểm tra (audit / 감사)

Kiểm tra (audit / 감사) không dùng tệp (file / 파일) kích thước (size / 크기) làm proxy cho chất lượng. bằng chứng (evidence / 증거) gồm:

- inventory đầy đủ 87 topic trên hiện tại (current / 현재) `main`;
- cumulative rewrite/kiểm tra (audit / 감사) lịch sử (history / 이력) Round 5–11;
- deep rà soát (review / 검토) lại các central domains và các tệp (file / 파일) ngắn bất thường;
- rà soát (review / 검토) README, glossary, phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) và nội bộ (internal / 내부) links;
- compare toàn bộ Mathematics branches với chuẩn gốc (canonical / 정본) `main`;
- content-level rà soát (review / 검토) riêng cho các branch có lịch sử (history / 이력) divergence.

Các tệp (file / 파일) `QUALITY_AUDIT_ROUND*.md` được giữ như historical rationale; chúng không cạnh tranh với README/topic chapters hiện tại.


> **Chuyển mạch:** Từ **Phương pháp final kiểm tra (audit / 감사)**, ta sang **kiểm tra (audit / 감사) 87/87 topic files** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kiểm tra (audit / 감사) 87/87 topic files

Status dùng dưới đây:

- `Canonical`: đủ độ sâu (depth / 깊이)/ranh giới (boundary / 경계) cho phạm vi (scope / 범위) hiện tại.
- `Deepened`: đã qua rewrite quan trọng ở Round 5–11.
- `Final links`: content đã đủ; finalization chỉ bổ sung clickable prerequisite/downstream điều hướng (navigation / 내비게이션) thay vì kéo dài cơ học.

### 00 — Foundations — 6/6

| Chapter | Status |
|---|---|
| `00_foundations/00_mathematical_thinking.md` | chuẩn gốc (canonical / 정본) |
| `00_foundations/01_logic_and_proof.md` | Deepened |
| `00_foundations/02_sets_relations_and_mappings.md` | Deepened |
| `00_foundations/03_numbers_and_number_systems.md` | Deepened |
| `00_foundations/04_measurement_units_and_estimation.md` | Deepened |
| `00_foundations/05_mathematical_modeling_dimensional_analysis_and_scaling.md` | chuẩn gốc (canonical / 정본) — explicitly audited and kept |

Foundation tầng (layer / 계층) hiện đủ cho lớp trừu tượng (abstraction / 추상화), proof, ánh xạ (mapping / 매핑), number biểu diễn (representation / 표현), units/bất định (uncertainty / 불확실성) và mô hình (model / 모델) các giả định (assumptions / 가정들). lô-gic (logic / 논리)/proof không chỉ có truth tables mà có implication, quantifiers, proof chiến lược (strategy / 전략), induction, invariants, counterexample và formal-vs-testing lập luận (reasoning / 추론).

### 01 — Algebra — 7/7

| Chapter | Status |
|---|---|
| `01_algebra/00_algebraic_language.md` | Deepened |
| `01_algebra/01_equations_and_inequalities.md` | Deepened |
| `01_algebra/02_ratio_proportion_percentage.md` | Deepened |
| `01_algebra/03_powers_roots_and_logarithms.md` | Deepened |
| `01_algebra/04_polynomials_and_factorization.md` | Deepened |
| `01_algebra/05_complex_numbers.md` | Final links |
| `01_algebra/06_rational_expressions_domain_and_asymptotes.md` | Final links |

Complex numbers và rational expressions là hai tệp (file / 파일) ngắn tương đối nhưng đã được đọc sâu. Chúng đủ conceptual phạm vi (scope / 범위); finalization chỉ thêm chuẩn gốc (canonical / 정본) links tới trig/eigen/Fourier/Laplace/complex phân tích (analysis / 분석) và limits/ODE/numerics.

### 02 — Functions — 6/6

| Chapter | Status |
|---|---|
| `02_functions/00_function_concept.md` | Deepened |
| `02_functions/01_linear_and_quadratic_models.md` | Deepened |
| `02_functions/02_exponential_and_logarithmic_models.md` | Deepened |
| `02_functions/03_sequences_series_and_recurrence.md` | Deepened |
| `02_functions/04_composition_inverse_and_function_transformations.md` | Final links |
| `02_functions/05_parametric_polar_and_implicit_relations.md` | Final links |

Hàm (function / 함수) tầng (layer / 계층) hiện đi từ ánh xạ (mapping / 매핑)/đặc tả hợp đồng (contract / 계약) tới mô hình (model / 모델) forms, recurrence, composition/invertibility và alternate representations. Composition/inverse được nối trực tiếp sang chuỗi (chain / 사슬) quy tắc (rule / 규칙), tuyến tính (linear / 선형) transformations, computational graphs và software pipelines; parametric/polar/implicit được nối sang calculus, conics và Jacobian/thay đổi (change / 변경) of variables.

### 03 — hình học (geometry / 기하학) & Trigonometry — 9/9

| Chapter | Status |
|---|---|
| `03_geometry_trigonometry/00_euclidean_geometry.md` | Deepened |
| `03_geometry_trigonometry/01_coordinate_geometry.md` | Deepened |
| `03_geometry_trigonometry/02_pythagorean_theorem_and_distance.md` | Deepened |
| `03_geometry_trigonometry/03_similarity_area_volume_and_scaling.md` | Deepened |
| `03_geometry_trigonometry/04_trigonometry.md` | Deepened |
| `03_geometry_trigonometry/05_transformations_and_symmetry.md` | Deepened |
| `03_geometry_trigonometry/06_circles_conics_and_loci.md` | Deepened |
| `03_geometry_trigonometry/07_trigonometric_identities_equations_and_harmonics.md` | Deepened |
| `03_geometry_trigonometry/08_topology_continuity_connectivity.md` | chuẩn gốc (canonical / 정본) — explicitly audited and kept |

Hình học (geometry / 기하학)/trigonometry không còn là collection công thức: coordinates/frames, orthogonality/distance, scaling, rotation/phase, symmetry/invariance, conic quadratic forms và topology ranh giới (boundary / 경계) được tách đúng conceptual role.

### 04 — Vectors & tuyến tính (linear / 선형) Algebra — 10/10

| Chapter | Status |
|---|---|
| `04_vectors_linear_algebra/00_vectors.md` | Deepened |
| `04_vectors_linear_algebra/01_matrices_and_linear_systems.md` | Deepened |
| `04_vectors_linear_algebra/02_linear_transformations.md` | Deepened |
| `04_vectors_linear_algebra/03_vector_spaces_basis_dimension.md` | Deepened |
| `04_vectors_linear_algebra/04_eigenvalues_and_eigenvectors.md` | Deepened |
| `04_vectors_linear_algebra/05_least_squares_svd_and_decompositions.md` | Deepened |
| `04_vectors_linear_algebra/06_inner_product_orthogonality_and_projection.md` | Deepened |
| `04_vectors_linear_algebra/07_determinant_rank_nullspace_and_inverse.md` | Deepened |
| `04_vectors_linear_algebra/08_tensors_and_multilinear_algebra.md` | chuẩn gốc (canonical / 정본) |
| `04_vectors_linear_algebra/09_matrix_calculus_jacobian_hessian_and_autodiff.md` | Deepened |

Tuyến tính (linear / 선형) algebra hiện tạo một coherent đường dẫn (path / 경로): biểu diễn (representation / 표현) → tuyến tính (linear / 선형) map → véc-tơ (vector / 벡터) không gian (space / 공간)/basis → eigenmodes → projection/least squares/SVD → rank/null-space/reversibility → tensor/multilinear → cục bộ (local / 로컬) nonlinear sensitivity qua Jacobian/Hessian/autodiff. Backprop được phân biệt với optimizer; AD được phân biệt với symbolic differentiation và finite difference.

### 05 — Calculus & phân tích (analysis / 분석) — 13/13

| Chapter | Status |
|---|---|
| `05_calculus/00_limits_and_continuity.md` | Deepened |
| `05_calculus/01_derivatives.md` | Deepened |
| `05_calculus/02_derivative_applications.md` | Deepened |
| `05_calculus/03_integrals_and_accumulation.md` | Deepened |
| `05_calculus/04_multivariable_calculus.md` | Deepened |
| `05_calculus/05_differential_equations.md` | Deepened |
| `05_calculus/06_numerical_calculus.md` | Deepened / consolidated ranh giới (boundary / 경계) |
| `05_calculus/07_infinite_series_power_series_and_convergence.md` | Deepened |
| `05_calculus/08_taylor_series_and_local_approximation.md` | Deepened |
| `05_calculus/09_vector_calculus.md` | Deepened |
| `05_calculus/10_partial_differential_equations_and_fields_intro.md` | chuẩn gốc (canonical / 정본) — explicitly audited and kept |
| `05_calculus/11_real_analysis_convergence_and_rigor.md` | chuẩn gốc (canonical / 정본) |
| `05_calculus/12_complex_analysis_and_analytic_functions.md` | chuẩn gốc (canonical / 정본) |

Calculus cốt lõi (core / 핵심) hiện ưu tiên cục bộ (local / 로컬) linearity, accumulation, lỗi (error / 오류)/remainder, các giả định (assumptions / 가정들) và local-to-global lập luận (reasoning / 추론). Numerical calculus giữ ranh giới (boundary / 경계) riêng với general numerical methods để tránh duplication.

### 06 — xác suất (probability / 확률) & Statistics — 13/13

| Chapter | Status |
|---|---|
| `06_probability_statistics/00_counting_and_combinatorics.md` | Deepened |
| `06_probability_statistics/01_probability_foundations.md` | Deepened |
| `06_probability_statistics/02_conditional_probability_and_bayes.md` | Deepened |
| `06_probability_statistics/03_random_variables_and_distributions.md` | Deepened |
| `06_probability_statistics/04_expectation_variance_and_limit_laws.md` | Deepened |
| `06_probability_statistics/05_descriptive_and_inferential_statistics.md` | Deepened |
| `06_probability_statistics/06_regression_and_correlation.md` | Deepened |
| `06_probability_statistics/07_sampling_estimation_confidence_and_hypothesis_testing.md` | Deepened |
| `06_probability_statistics/08_covariance_multivariate_probability_and_gaussian.md` | Deepened |
| `06_probability_statistics/09_common_distributions_and_when_they_arise.md` | Deepened |
| `06_probability_statistics/10_likelihood_mle_map_and_model_selection.md` | chuẩn gốc (canonical / 정본) — explicitly audited and kept |
| `06_probability_statistics/11_stochastic_processes_markov_chains_and_time_series.md` | chuẩn gốc (canonical / 정본) — explicitly audited and kept |
| `06_probability_statistics/12_bayesian_inference_posterior_predictive_and_hierarchical_models.md` | chuẩn gốc (canonical / 정본) |

Xác suất (probability / 확률)/statistics tầng (layer / 계층) hiện phân biệt rõ xác suất (probability / 확률) mô hình (model / 모델), sampling/suy luận (inference / 추론), likelihood, Bayesian bất định (uncertainty / 불확실성), calibration và nhân quả (causal / 인과적) interpretation. Stochastic-process chapter có tiến trình (process / 프로세스)/mẫu (sample / 표본) đường dẫn (path / 경로), stationarity/autocorrelation, Markov cấu trúc (structure / 구조), stationary phân phối (distribution / 분포), random walk/Poisson/Brownian/martingale/HMM/MCMC đủ cho hiện tại (current / 현재) phụ thuộc (dependency / 의존성) mức (level / 수준).

### 07 — Discrete Mathematics & Theoretical CS — 9/9

| Chapter | Status |
|---|---|
| `07_discrete_cs/00_graph_theory.md` | Deepened |
| `07_discrete_cs/01_algorithms_complexity_and_logarithms.md` | Deepened |
| `07_discrete_cs/02_recurrence_and_induction_in_algorithms.md` | Deepened |
| `07_discrete_cs/03_boolean_algebra_and_digital_logic.md` | Deepened |
| `07_discrete_cs/04_number_theory_and_modular_arithmetic.md` | Deepened |
| `07_discrete_cs/05_trees_posets_and_lattices.md` | Deepened |
| `07_discrete_cs/06_information_theory_and_coding.md` | Deepened |
| `07_discrete_cs/07_automata_formal_languages_and_computability.md` | Deepened |
| `07_discrete_cs/08_groups_rings_fields_and_algebraic_structures.md` | chuẩn gốc (canonical / 정본) — explicitly audited and kept |

Discrete tầng (layer / 계층) tạo cầu nối (bridge / 브리지) trực tiếp sang algorithms/software: proof/bất biến (invariant / 불변식) → recurrence/độ phức tạp (complexity / 복잡도) → graphs/trees/orders → lô-gic (logic / 논리)/circuits → number lý thuyết (theory / 이론) → thông tin (information / 정보)/coding → automata/computability.

### 08 — tối ưu hóa (optimization / 최적화) & Numerical Mathematics — 7/7

| Chapter | Status |
|---|---|
| `08_optimization_numerical/00_optimization.md` | Deepened |
| `08_optimization_numerical/01_gradient_descent_and_convexity.md` | Deepened |
| `08_optimization_numerical/02_numerical_methods_and_error.md` | Deepened |
| `08_optimization_numerical/03_constrained_optimization_lagrange_and_kkt.md` | Deepened |
| `08_optimization_numerical/04_root_finding_interpolation_and_numerical_linear_algebra.md` | Deepened |
| `08_optimization_numerical/05_linear_programming_duality_and_simplex.md` | Deepened |
| `08_optimization_numerical/06_dynamic_programming_bellman_and_optimal_control.md` | chuẩn gốc (canonical / 정본) |

Tối ưu hóa (optimization / 최적화) và numerics được giữ tách biệt về question: tối ưu hóa (optimization / 최적화) chọn quyết định (decision / 결정) dưới mục tiêu (objective / 목표)/các ràng buộc (constraints / 제약조건들); numerical phân tích (analysis / 분석) đánh giá khả năng tính answer đáng tin trên finite-precision machine. Conditioning, stability, convergence, KKT/duality và Bellman lập luận (reasoning / 추론) tạo production-oriented judgment thay vì chỉ thuật toán (algorithm / 알고리즘) recipes.

### 09 — kiến thức (knowledge / 지식) Connections — 7/7

| Chapter | Status |
|---|---|
| `09_connections/00_rate_change_and_accumulation.md` | Deepened |
| `09_connections/01_distance_similarity_and_projection.md` | Deepened |
| `09_connections/02_uncertainty_information_and_entropy.md` | Deepened |
| `09_connections/03_math_for_ai_data_and_software.md` | Deepened |
| `09_connections/04_math_for_finance_work_and_daily_life.md` | chuẩn gốc (canonical / 정본) — explicitly audited and kept |
| `09_connections/05_fourier_signals_and_frequency.md` | Deepened |
| `09_connections/06_laplace_z_transform_and_dynamic_systems.md` | Final links |

Liên kết (connection / 연결) chapters không thay topic chapters. Chúng expose dùng chung (shared / 공유) cấu trúc (structure / 구조): tỷ lệ (rate / 비율)/accumulation, hình học (geometry / 기하학)/projection, xác suất (probability / 확률)/thông tin (information / 정보), biểu diễn (representation / 표현)/autodiff/môi trường vận hành (production / 운영 환경), compounding/rủi ro (risk / 위험), basis/frequency và transform-domain dynamics.

**Final count: 87/87 topic files audited and accepted for hiện tại (current / 현재) chuẩn gốc (canonical / 정본) phạm vi (scope / 범위).**


> **Chuyển mạch:** Từ **kiểm tra (audit / 감사) 87/87 topic files**, ta sang **Cross-domain bridges** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cross-domain bridges

| bên ngoài (external / 외부) lĩnh vực (domain / 도메인) | Mathematics cầu nối (bridge / 브리지) |
|---|---|
| Khoa học máy tính (computer science / 컴퓨터 과학) | lô-gic (logic / 논리)/proof, sets/relations, recurrence, graphs, number lý thuyết (theory / 이론), automata, độ phức tạp (complexity / 복잡도). |
| Algorithms | Induction/invariants, recurrence, asymptotics, đồ thị (graph / 그래프)/đường dẫn (path / 경로) cấu trúc (structure / 구조), động (dynamic / 동적) programming. |
| AI/ML | tuyến tính (linear / 선형) algebra, multivariable/ma trận (matrix / 행렬) calculus, autodiff, xác suất (probability / 확률)/statistics, thông tin (information / 정보) lý thuyết (theory / 이론), tối ưu hóa (optimization / 최적화), numerics. |
| kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) | Relations/mappings, functional pipelines, đồ thị (graph / 그래프) phụ thuộc (dependency / 의존성), xác suất (probability / 확률)/statistics, approximation/numerical lập luận (reasoning / 추론). |
| Physics | đo lường (measurement / 측정)/dimensional phân tích (analysis / 분석), hình học (geometry / 기하학)/vectors, calculus, ODE/PDE, Fourier, symmetry/conservation. |
| Finance/Investing | Rates/compounding, xác suất (probability / 확률), expectation/covariance, regression, stochastic processes, tối ưu hóa (optimization / 최적화), numerical sensitivity. |
| Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) | lô-gic (logic / 논리)/contracts, composition, đồ thị (graph / 그래프) phụ thuộc (dependency / 의존성), độ phức tạp (complexity / 복잡도), độ tin cậy (reliability / 신뢰성) xác suất (probability / 확률), floating-point/numerical stability. |
| Đời sống thực tế | Percentage/rates, estimation, units, bất định (uncertainty / 불확실성), expected giá trị (value / 값), compounding, rủi ro (risk / 위험) và quyết định (decision / 결정) trade-offs. |

Clickable học tập (learning / 학습) routes nằm tại [README.md](./README.md).


> **Chuyển mạch:** Từ **Cross-domain bridges**, ta sang **phạm vi (scope / 범위) ranh giới (boundary / 경계)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Phạm vi (scope / 범위) ranh giới (boundary / 경계)

Không tạo thêm chapter cho measure lý thuyết (theory / 이론)/Lebesgue tích hợp (integration / 통합), functional phân tích (analysis / 분석), differential hình học (geometry / 기하학)/manifolds, stochastic calculus, advanced PDE, advanced điều khiển (control / 제어), advanced combinatorial tối ưu hóa (optimization / 최적화) hoặc category lý thuyết (theory / 이론) chỉ vì chúng là subjects quan trọng.

Quy tắc (rule / 규칙) chuẩn gốc (canonical / 정본):

> Chỉ thêm topic khi xuất hiện một phụ thuộc (dependency / 의존성) gap thực tế mà chapter hiện tại không thể giải quyết trong ranh giới (boundary / 경계) hợp lý.


> **Chuyển mạch:** Từ **phạm vi (scope / 범위) ranh giới (boundary / 경계)**, ta sang **Final consistency changes** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Final consistency changes

Finalization 2026-09-22 đã thực hiện:

- đồng bộ README với hiện tại (current / 현재) 87-topic trạng thái (state / 상태) thay cho mô tả cũ “sau bốn vòng kiểm tra (audit / 감사)”;
- đồng bộ hiện tại (current / 현재) chapter titles trong TOC;
- cập nhật phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) tới Bayes, stochastic processes, ma trận (matrix / 행렬) calculus/autodiff, LP/duality, DP/điều khiển (control / 제어) và Fourier/Laplace;
- thêm clickable Markdown học tập (learning / 학습) routes cho CS/Algorithms, AI/dữ liệu (data / 데이터), Physics, tín hiệu (signal / 신호)/điều khiển (control / 제어), Finance và Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학);
- thêm chuẩn gốc (canonical / 정본) prerequisite/downstream links cho `complex_numbers`, `rational_expressions`, `composition_inverse`, `parametric_polar_implicit` và `laplace_z`;
- bổ sung glossary cho automatic differentiation, computational đồ thị (graph / 그래프), backpropagation, prior/posterior/posterior predictive, calibration, nhân quả (causal / 인과적) intervention, stochastic tiến trình (process / 프로세스), Markov chuỗi (chain / 사슬), stationarity, autocorrelation, martingale, hierarchical mô hình (model / 모델), động (dynamic / 동적) programming, Bellman equation, transfer hàm (function / 함수), pole/zero, ROC, trạng thái (state / 상태) không gian (space / 공간) và LTI;
- không thêm Mathematics topic mới.


> **Chuyển mạch:** Từ **Final consistency changes**, ta sang **kiểm tra (audit / 감사) toàn bộ Mathematics branches cũ** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kiểm tra (audit / 감사) toàn bộ Mathematics branches cũ

Trước finalization có **19 Mathematics branches cũ**.

### 17 branch là ancestor/behind chuẩn gốc (canonical / 정본) lịch sử (history / 이력)

Các branch sau đã được compare với pre-finalization `main` và có `ahead_by = 0`:

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

Không branch nào trong nhóm này cần merge/cherry-pick lại.

### 2 Round 5 branches có lịch sử (history / 이력) divergence nhưng không có content cần cứu

18. `math-quality-round5-20260920`
19. `math-quality-round5-rebased`

Hai branch này báo ahead/diverged vì alternate lần ghi nhận (commit / 커밋) lịch sử (history / 이력)/rebase. Final kiểm tra (audit / 감사) đã đối chiếu actual Round 5 content. chuẩn gốc (canonical / 정본) lịch sử (history / 이력) chứa các rewrites tương ứng cho:

- `02_functions/00_function_concept.md`
- `02_functions/02_exponential_and_logarithmic_models.md`
- `03_geometry_trigonometry/04_trigonometry.md`
- `04_vectors_linear_algebra/03_vector_spaces_basis_dimension.md`
- `05_calculus/00_limits_and_continuity.md`
- `07_discrete_cs/00_graph_theory.md`
- `08_optimization_numerical/02_numerical_methods_and_error.md`
- `EDITORIAL_STANDARD.md`
- `QUALITY_AUDIT_ROUND5.md`

Vì vậy đây là **lịch sử (history / 이력) divergence đã rà soát (review / 검토)**, không phải unmerged Mathematics content.

### Finalization branch

`math-finalization-20260922` được tạo trực tiếp từ `main`, thay đổi đúng 8 Mathematics files, rồi squash-merge qua PR #41. Sau merge, finalization head và squash merge lần ghi nhận (commit / 커밋) có cùng cây (tree / 트리) SHA `ffd30e10adaf72e2630cb20c1b6c5d8bbfa51c82`. Branch này cũng **safe-to-delete**.


> **Chuyển mạch:** Từ **kiểm tra (audit / 감사) toàn bộ Mathematics branches cũ**, ta sang **Canonicalization checklist** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Canonicalization checklist

### Content

- [x] Inventory đúng 87 topic files.
- [x] kiểm tra (audit / 감사) cumulative Round 5–11 được đọc và đối chiếu với hiện tại (current / 현재) thư viện (library / 라이브러리).
- [x] Các priority domains của final yêu cầu (request / 요청) đã được deep-review hoặc có prior kiểm tra (audit / 감사) bằng chứng (evidence / 증거) đủ mạnh.
- [x] Formula/notation/giả định (assumption / 가정)/provenance/example/prerequisite/liên kết (connection / 연결)/failure-mode criteria được dùng làm chuẩn gốc (canonical / 정본) tiêu chuẩn (standard / 표준).
- [x] Short outliers được đọc trước khi quyết định; không kéo dài tệp (file / 파일) chỉ để đồng đều kích thước (size / 크기).
- [x] Không tạo chapter để tăng coverage.

### Điều hướng (navigation / 내비게이션) & consistency

- [x] README phản ánh hiện tại (current / 현재) 87-topic trạng thái (state / 상태).
- [x] TOC labels và phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) được cập nhật.
- [x] Có clickable học tập (learning / 학습) routes thay vì phụ thuộc Mermaid để navigate.
- [x] Short central nodes được bổ sung prerequisite/downstream links.
- [x] Glossary bao phủ thêm recurring Bayes/stochastic/autodiff/điều khiển (control / 제어) terms.
- [x] Cross-domain boundaries tới CS, Algorithms, AI/dữ liệu (data / 데이터), Physics, Finance/Investing và Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) được làm rõ.

### Merge & branch an toàn (safety / 안전)

- [x] Inventory toàn bộ 19 Mathematics branches cũ.
- [x] 17/19 branches có `ahead_by = 0` trước finalization.
- [x] 2 Round 5 history-diverged branches đã được content-review.
- [x] Tạo finalization branch từ hiện tại (current / 현재) `main`.
- [x] Diff finalization chỉ chạm 8 files dưới `mathematics/`.
- [x] PR #41 mergeable và không có pending status checks.
- [x] Squash-merge PR #41 vào `main`.
- [x] Re-verify `main` tại lần ghi nhận (commit / 커밋) `2714ce4529ef9d62ea2ae8e36ad2c299ae347e83`.
- [x] Verify finalization head và squash lần ghi nhận (commit / 커밋) có cùng cây (tree / 트리) SHA tại thời điểm merge.
- [x] 19 legacy branches + finalization branch đều đủ điều kiện **safe-to-delete** về mặt content.
- [ ] Branch refs chưa bị xóa vì GitHub connector của phiên này không expose delete branch/delete ref.

Dòng cuối là tooling limitation, không phải content blocker. Không còn divergent Mathematics content nào chưa rà soát (review / 검토).


> **Chuyển mạch:** Từ **Canonicalization checklist**, ta sang **chuẩn gốc (canonical / 정본) nguồn chuẩn (source of truth / 정본)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Chuẩn gốc (canonical / 정본) nguồn chuẩn (source of truth / 정본)

Từ thời điểm này:

1. `mathematics/README.md` — entry điểm (point / 지점), TOC, clickable học tập (learning / 학습) routes và phụ thuộc (dependency / 의존성) topology.
2. 87 chuẩn gốc (canonical / 정본) topic chapters — nội dung học chính.
3. `mathematics/10_glossary.md` — terminology chỉ mục (index / 인덱스) VI/EN/KR.
4. `mathematics/COVERAGE_AUDIT.md` — final phạm vi (scope / 범위)/kiểm tra (audit / 감사)/branch-safety bản ghi (record / 레코드).
5. `QUALITY_AUDIT_ROUND*.md` — historical rationale, không phải competing chuẩn gốc (canonical / 정본) indexes.

Future Mathematics công việc (work / 작업) phải bắt đầu từ `main`; không tiếp tục phát triển trên các Round/merge/staging branches cũ.

> **Bàn giao:** Sau **chuẩn gốc (canonical / 정본) nguồn chuẩn (source of truth / 정본)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [10 glossary](./10_glossary.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
