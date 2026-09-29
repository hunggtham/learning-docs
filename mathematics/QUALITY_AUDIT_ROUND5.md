# Chất lượng (quality / 품질) kiểm tra (audit / 감사) — Round 5: nâng chất lượng biên soạn

> **Mạch đọc:** Đặt **chất lượng (quality / 품질) kiểm tra (audit / 감사) — Round 5: nâng chất lượng biên soạn** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Mục tiêu** sang **Các chapter đã rewrite**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Round 5 chuyển trọng tâm từ **mở rộng số lượng topic** sang **nâng độ hoàn thiện và chất lượng viết** của những chapter đã tồn tại.

## Mục tiêu

Các vòng trước chủ yếu giải quyết coverage: thêm các topic còn thiếu để kiến thức (knowledge / 지식) đồ thị (graph / 그래프) không bị nhảy cóc. Sau khi coverage đã rộng, vấn đề nổi bật hơn là chất lượng không đồng đều: chapter mới thường có lập luận (reasoning / 추론), derivation và connections tốt hơn, trong khi một số chapter cũ vẫn giống expanded notes.

Round này đặt ra chuẩn mới: một chapter chỉ được xem là mạnh khi người đọc có thể hiểu **bài toán (problem / 문제) → definition → cơ chế (mechanism / 메커니즘) → derivation → example → các giả định (assumptions / 가정들)/thất bại (failure / 실패) modes → liên kết (connection / 연결) → mô hình tư duy (mental model / 사고 모델)**, thay vì chỉ đọc danh sách definitions và formulas.

Chuẩn đó được ghi thành tệp (file / 파일) [`EDITORIAL_STANDARD.md`](./EDITORIAL_STANDARD.md) để dùng cho các vòng rewrite sau.


> **Chuyển mạch:** Từ **Mục tiêu**, ta sang **Các chapter đã rewrite** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Các chapter đã rewrite

### Functions — `02_functions/00_function_concept.md`

Bản mới mở rộng hàm (function / 함수) từ “đầu vào (input / 입력) → đầu ra (output / 출력)” thành một concept structural: quan hệ (relation / 관계) vs hàm (function / 함수), lĩnh vực (domain / 도메인)/codomain/phạm vi (range / 범위), injective/surjective/bijective, invertibility như thông tin (information / 정보) preservation, composition như chuỗi xử lý (pipeline / 파이프라인), piecewise modeling, parameterized hàm (function / 함수) families, equality của functions, liên kết (connection / 연결) tới kiểu (type / 타입)/Đặc tả API (API contract / API 계약) và random variables.

Mục tiêu là để người đọc hiểu hàm (function / 함수) như một ánh xạ (mapping / 매핑) có đặc tả hợp đồng (contract / 계약), không đồng nhất hàm (function / 함수) với một formula.

### Functions — `02_functions/02_exponential_and_logarithmic_models.md`

Bản mới derive exponential từ repeated proportional growth và từ differential equation `dA/dt=kA`; logarithm được giải thích như inverse/multiplicative độ sâu (depth / 깊이) thay vì chỉ bảng rules.

Chapter bổ sung compound interest, quy tắc (rule / 규칙) of 72 derivation, semi-log modeling và noise mô hình (model / 모델), pH/decibel, algorithmic `O(log n)`, logistic limitation, exponential như eigenfunction của differentiation và information-theory liên kết (connection / 연결).

### Tuyến tính (linear / 선형) Algebra — `04_vectors_linear_algebra/03_vector_spaces_basis_dimension.md`

Bản mới xây từ tuyến tính (linear / 선형) combination → span → independence → basis → dimension → subspace → rank-nullity. Basis được giải thích như coordinate vocabulary; thay đổi (change / 변경) of basis được nối với eigenbasis, PCA, Fourier và representations trong ML.

Chapter cũng nói rõ giới hạn của vector-space mô hình (model / 모델) và curse of dimensionality, thay vì chỉ định nghĩa các term.

### Calculus — `05_calculus/00_limits_and_continuity.md`

Bản mới giải thích limit như tolerance đặc tả hợp đồng (contract / 계약), thêm epsilon–delta lập luận (reasoning / 추론) thực sự, indeterminate forms, chuỗi (sequence / 시퀀스) viewpoint, types of discontinuity, uniform continuity, asymptotic growth, derivative/infinite-series liên kết (connection / 연결) và numerical-computing distinction.

Mục tiêu là biến limit từ một “kỹ thuật thay số” thành foundation lập luận (reasoning / 추론) của calculus.

### Hình học (geometry / 기하학) & Trigonometry — `03_geometry_trigonometry/04_trigonometry.md`

Bản mới chuyển trọng tâm từ SOH-CAH-TOA sang unit-circle/rotation viewpoint. Sine/cosine được derive như coordinates của rotation; radian được giải thích bằng arc length và calculus; addition formulas được nối với rotation-matrix composition.

Chapter cũng thêm phase, sinusoidal motion, Euler formula, Fourier viewpoint, sampling/aliasing, véc-tơ (vector / 벡터) cosine similarity, 3D rotations và degree/radian API bugs.

### Discrete Mathematics — `07_discrete_cs/00_graph_theory.md`

Bản mới mở rộng từ basic đồ thị (graph / 그래프)/BFS/DFS sang một chapter modeling đầy đủ hơn: đồ thị (graph / 그래프) ngữ nghĩa (semantics / 의미론), connectivity, trees/spanning trees/MST, DAG/topological thứ tự (order / 순서), shortest paths, SCC, bipartite matching, coloring, Euler/Hamilton distinction, đồ thị (graph / 그래프) matrices/Laplacian, random walks, luồng (flow / 흐름)/cut và software-system modeling.

Điểm nhấn là “thuật toán (algorithm / 알고리즘) đúng không cứu được đồ thị (graph / 그래프) mô hình (model / 모델) sai”.

### Numerical Mathematics — `08_optimization_numerical/02_numerical_methods_and_error.md`

Bản mới tách rõ mô hình (model / 모델) lỗi (error / 오류), sai số đo lường (measurement error / 측정 오차), discretization lỗi (error / 오류), conditioning và stability. Nội dung bổ sung floating-point biểu diễn (representation / 표현), cancellation, forward/backward lỗi (error / 오류), gốc (root / 루트) finding derivation, interpolation/basis conditioning, numerical tích hợp (integration / 통합), Monte Carlo, sparse/iterative tuyến tính (linear / 선형) algebra, ODE stability, scaling, reproducibility và mixed precision.

Chapter được viết để tạo kỹ thuật (engineering / 엔지니어링) judgment thay vì collection numerical methods.


> **Chuyển mạch:** Từ **Các chapter đã rewrite**, ta sang **Chuẩn viết mới** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Chuẩn viết mới

Từ round này trở đi, các chapter được kiểm tra (audit / 감사) theo các tiêu chí chính:

- definition phải đi cùng intuition;
- formula quan trọng phải có provenance và các giả định (assumptions / 가정들);
- giải thích chính phải là paragraph có nhân quả (causal / 인과적) luồng (flow / 흐름);
- example phải giúp transfer lập luận (reasoning / 추론), không chỉ “thay số”;
- mô hình (model / 모델), theorem và computation cần phân biệt rõ;
- thất bại (failure / 실패) modes phải được nói ra;
- liên kết (connection / 연결) giữa domains chỉ dùng khi thực sự có cùng mathematical cấu trúc (structure / 구조);
- mô hình tư duy (mental model / 사고 모델) phải tạo reusable way of thinking;
- dùng chung (common / 공통) Misconceptions phải giải thích vì sao intuition sai xuất hiện.

Chi tiết nằm trong [`EDITORIAL_STANDARD.md`](./EDITORIAL_STANDARD.md).


> **Chuyển mạch:** Từ **Chuẩn viết mới**, ta sang **Nhóm ưu tiên cho round tiếp theo** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Nhóm ưu tiên cho round tiếp theo

Các tệp (file / 파일) còn ngắn so với vai trò phụ thuộc (dependency / 의존성) và nên tiếp tục được rewrite theo tiêu chuẩn (standard / 표준) mới gồm:

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

Round sau nên tiếp tục ưu tiên phụ thuộc (dependency / 의존성) centrality trước tệp (file / 파일) count: rewrite những concept nhiều chapter khác dựa vào trước khi mở rộng thêm research-level topics.


> **Chuyển mạch:** Từ **Nhóm ưu tiên cho round tiếp theo**, ta sang **mô hình tư duy (mental model / 사고 모델) cho quá trình biên soạn** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델) cho quá trình biên soạn

> Coverage xây các nút (node / 노드) của kiến thức (knowledge / 지식) đồ thị (graph / 그래프); chất lượng (quality / 품질) rewrite làm rõ các edge giữa chúng. Một thư viện (library / 라이브러리) có nhiều tệp (file / 파일) nhưng các edge mờ vẫn khiến người đọc phải tự nối kiến thức. Mục tiêu tiếp theo là làm cho lập luận (reasoning / 추론) đường dẫn (path / 경로) trở nên nhìn thấy được ngay trong từng chapter.

> **Bàn giao:** Sau **mô hình tư duy (mental model / 사고 모델) cho quá trình biên soạn**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [10 glossary](./10_glossary.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
