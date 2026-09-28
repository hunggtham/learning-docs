# Chất lượng (quality / 품질) kiểm tra (audit / 감사) — Round 11: computation, tối ưu hóa (optimization / 최적화) và cầu nối (bridge / 브리지) chapters

> **Mạch đọc:** Đặt **chất lượng (quality / 품질) kiểm tra (audit / 감사) — Round 11: computation, tối ưu hóa (optimization / 최적화) và cầu nối (bridge / 브리지) chapters** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Tiêu chí kiểm tra (audit / 감사)** sang **Batch 1 — Automata/Computability + tuyến tính (linear / 선형) Programming**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Round 11 tiếp tục chiến lược **chất lượng (quality / 품질) over chapter count**. Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리) vẫn giữ nguyên **87 topic**; không thêm chapter mới chỉ để tăng coverage.

Mục tiêu của round này là kiểm tra (audit / 감사) nhóm advanced/cốt lõi (core / 핵심) cầu nối (bridge / 브리지) còn lại sau Round 10 và chỉ rewrite nơi có độ sâu (depth / 깊이) gap thực sự.

## Tiêu chí kiểm tra (audit / 감사)

Một chapter chỉ được rewrite nếu có một hoặc nhiều dấu hiệu:

```text
learning dependency quan trọng nhưng nội dung còn ngắn
formalism đúng nhưng proof idea / intuition chưa đủ
assumptions hoặc failure modes còn mỏng
connections chỉ được nhắc tên thay vì derive
chapter bridge chưa thực sự nối được các domain
```

Ngược lại, chapter đủ coherent, có các giả định (assumptions / 가정들), mô hình tư duy (mental model / 사고 모델) và downstream connections thì giữ nguyên dù tệp (file / 파일) ngắn hơn chapter khác.


> **Chuyển mạch:** Từ **Tiêu chí kiểm tra (audit / 감사)**, ta sang **Batch 1 — Automata/Computability + tuyến tính (linear / 선형) Programming** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Batch 1 — Automata/Computability + tuyến tính (linear / 선형) Programming

Lần ghi nhận (commit / 커밋):

```text
aecdfa8bbdbb339d84694b11f2dc744021e0c319
```

### `07_discrete_cs/07_automata_formal_languages_and_computability.md`

Bản cũ đúng về DFA, CFG, Turing machine, halting bài toán (problem / 문제) và P/NP nhưng còn giống overview.

Bản mới tổ chức thành phụ thuộc (dependency / 의존성) chuỗi (chain / 사슬):

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

- DFA trạng thái (state / 상태) như compressed relevant lịch sử (history / 이력);
- NFA vs DFA: same expressive power nhưng trạng thái (state / 상태) blow-up;
- regular expression lý thuyết (theory / 이론) vs môi trường vận hành (production / 운영 환경) regex engines;
- pumping/Myhill–Nerode intuition qua thông tin (information / 정보) sức chứa (capacity / 용량);
- CFG/PDA và recursive cú pháp (syntax / 문법);
- Chomsky hierarchy dưới viewpoint bộ nhớ (memory / 메모리) cấu trúc (structure / 구조);
- universal Turing machine và program-as-data;
- Church–Turing thesis vs theorem;
- recognizable vs decidable;
- halting proof qua self-reference/diagonalization;
- reduction direction;
- NP-hard/NP-complete distinction;
- trạng thái (state / 상태) explosion trong mô hình (model / 모델) checking;
- trình biên dịch (compiler / 컴파일러) lexing/parsing/semantic-analysis separation.

### `08_optimization_numerical/05_linear_programming_duality_and_simplex.md`

Bản cũ đã có primal/dual/simplex và integer programming nhưng độ sâu (depth / 깊이) thấp hơn KKT/Numerical chapters mới.

Bản mới có mạch học (learning flow / 학습 흐름):

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
- simplex pivot như basis thay đổi (change / 변경);
- degeneracy/cycling;
- weak duality derivation;
- strong duality như optimality certificate;
- shadow price only locally valid under regime/basis stability;
- interior-point vs simplex trade-offs;
- LP relaxation, branch-and-bound, integrality gap;
- total unimodularity;
- max-flow/min-cut as structured duality;
- numerical scaling/tolerance caveats;
- deterministic LP vs bất định (uncertainty / 불확실성)/robust tối ưu hóa (optimization / 최적화).


> **Chuyển mạch:** Từ **Batch 1 — Automata/Computability + tuyến tính (linear / 선형) Programming**, ta sang **Batch 2 — 09connections cầu nối (bridge / 브리지) chapters** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Batch 2 — `09_connections` cầu nối (bridge / 브리지) chapters

Lần ghi nhận (commit / 커밋):

```text
bb8f70afd1f53e251c00117f90da252b6a34ff52
```

Sau Round 5–10, nhiều chuẩn gốc (canonical / 정본) topic chapters đã rất sâu nhưng một số `09_connections` chỉ còn 4–5 KB và giống summary. Round 11 nâng 5 cầu nối (bridge / 브리지) chapters để chúng thực sự giúp transfer mô hình tư duy (mental model / 사고 모델) giữa domains.

### `09_connections/00_rate_change_and_accumulation.md`

Mạch học (learning flow / 학습 흐름) mới:

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

- trạng thái (state / 상태) vs tỷ lệ (rate / 비율) vs accumulated total;
- signed vs absolute accumulation;
- discrete Fundamental-Theorem analogy;
- additive vs multiplicative recurrence;
- hàng đợi (queue / 큐) length vs arrival/dịch vụ (service / 서비스) rates;
- finance balance vs cash-flow tỷ lệ (rate / 비율);
- marginal vs total quantities;
- độ dốc (gradient / 기울기) descent as accumulated cục bộ (local / 로컬) updates;
- continuity/conservation equation;
- dimensional sanity checks.

### `09_connections/01_distance_similarity_and_projection.md`

Mạch học (learning flow / 학습 흐름) mới:

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
- chỉ số (metric / 지표) axioms và triangle inequality;
- preprocessing thay đổi hình học (geometry / 기하학);
- cosine similarity và khi normalization làm mất tín hiệu (signal / 신호);
- projection as nearest-point bài toán (problem / 문제);
- least squares hình học (geometry / 기하학);
- PCA criterion vs tác vụ (task / 작업) relevance;
- Mahalanobis/whitening;
- singular covariance/pseudoinverse;
- kernel viewpoint;
- distance concentration/curse of dimensionality;
- embedding similarity and véc-tơ (vector / 벡터) tìm kiếm (search / 검색);
- covariance hình học (geometry / 기하학) in finance.

### `09_connections/02_uncertainty_information_and_entropy.md`

Mạch học (learning flow / 학습 흐름):

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
- coding/Kraft liên kết (connection / 연결);
- data-processing inequality;
- cross-entropy ↔ negative log-likelihood;
- calibration vs entropy;
- expected mất mát (loss / 손실)/quyết định (decision / 결정);
- proper scoring rules;
- thông tin (information / 정보) gain;
- entropy tỷ lệ (rate / 비율);
- channel sức chứa (capacity / 용량);
- compression vs error-correcting redundancy.

### `09_connections/03_math_for_ai_data_and_software.md`

Bản mới không còn chỉ liệt kê “môn toán dùng trong AI”. Nó tổ chức full hệ thống (system / 시스템) phụ thuộc (dependency / 의존성):

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

- biểu diễn (representation / 표현) is a modeling choice;
- computational đồ thị (graph / 그래프) + chuỗi (chain / 사슬) quy tắc (rule / 규칙);
- losses encode probabilistic/robustness các giả định (assumptions / 가정들);
- empirical vs population rủi ro (risk / 위험);
- conditioning/Hessian;
- log-sum-exp stability;
- floating điểm (point / 지점) and mixed precision;
- embedding hình học (geometry / 기하학);
- train/kiểm thử (test / 테스트) suy luận (inference / 추론) and phân phối (distribution / 분포) shift;
- prediction vs causality;
- đồ thị (graph / 그래프)/cơ sở dữ liệu (database / 데이터베이스)/chỉ mục (index / 인덱스)/cardinality-estimation connections;
- Big-O vs chính xác (exact / 정확한) thời gian chạy (runtime / 런타임);
- khả năng quan sát (observability / 관측 가능성) metrics;
- mô hình (model / 모델) tính đúng đắn (correctness / 정확성) vs hệ thống (system / 시스템) tính đúng đắn (correctness / 정확성).

### `09_connections/05_fourier_signals_and_frequency.md`

Mạch học (learning flow / 학습 흐름) mới:

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

- Parseval/năng lượng (energy / 에너지) preservation;
- differentiation as frequency multiplication;
- LTI impulse/frequency phản hồi (response / 응답);
- time-frequency localization sự đánh đổi (trade-off / 트레이드오프);
- aliasing derivation intuition;
- Nyquist các giả định (assumptions / 가정들);
- DFT as ma trận (matrix / 행렬)/basis thay đổi (change / 변경);
- spectral leakage/windowing;
- frequency resolution vs mẫu (sample / 표본) tỷ lệ (rate / 비율);
- filtering/causality sự đánh đổi (trade-off / 트레이드오프);
- Gibbs phenomenon;
- PDE chế độ (mode / 모드) decomposition;
- Fourier features and AI;
- Fourier vs Laplace vs Z-transform mental map.


> **Chuyển mạch:** Từ **Batch 2 — 09connections cầu nối (bridge / 브리지) chapters**, ta sang **Audited but intentionally not rewritten** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Audited but intentionally not rewritten

Round 11 cũng kiểm tra (audit / 감사) các files sau nhưng giữ nguyên vì content hiện tại đã tương đối cân bằng với editorial tiêu chuẩn (standard / 표준).

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

Tệp (file / 파일) đã giải thích đúng distinction topology vs chỉ số (metric / 지표) hình học (geometry / 기하학) và có các giả định (assumptions / 가정들)/misconceptions đủ rõ.

### `05_calculus/10_partial_differential_equations_and_fields_intro.md`

Giữ nguyên vì đã có coherent chuỗi (chain / 사슬):

```text
field
→ heat/wave/Laplace equations
→ initial/boundary conditions
→ PDE classification
→ separation of variables/eigenmodes
→ numerical discretization/stability
```

Nội dung đủ cho phạm vi (scope / 범위) “intro”; viết sâu thêm sẽ bắt đầu thành course PDE riêng.

### `06_probability_statistics/10_likelihood_mle_map_and_model_selection.md`

Giữ nguyên vì chapter đã derive Bernoulli MLE, giải thích log-likelihood/NLL, model-family các giả định (assumptions / 가정들) và cầu nối (bridge / 브리지) sang ML/statistics. Đây không còn là bottleneck về độ sâu (depth / 깊이).

### `06_probability_statistics/11_stochastic_processes_markov_chains_and_time_series.md`

Giữ nguyên vì chapter đã có tiến trình (process / 프로세스)/sample-path, stationarity/autocorrelation, Markov thuộc tính (property / 속성), chuyển tiếp (transition / 전이) cấu trúc (structure / 구조) và time-series cầu nối (bridge / 브리지). phạm vi (scope / 범위) hiện phù hợp với phụ thuộc (dependency / 의존성) mức (level / 수준) của thư viện (library / 라이브러리).

### `07_discrete_cs/08_groups_rings_fields_and_algebraic_structures.md`

Giữ nguyên vì đã có group/ring/trường dữ liệu (field / 필드), symmetry, subgroup/generator, homomorphism/kernel/ảnh (image / 이미지), finite fields, zero divisors, quotient idea và connections với tuyến tính (linear / 선형) algebra/cryptography.

### `09_connections/04_math_for_finance_work_and_daily_life.md`

Giữ nguyên vì đã đủ sâu hơn nhóm liên kết (connection / 연결) cũ, gồm compounding, effective rates, discounting, NPV, annuity/loan derivation và quantitative nghiệp vụ (business / 비즈니스) lập luận (reasoning / 추론).

### `09_connections/06_laplace_z_transform_and_dynamic_systems.md`

Giữ nguyên vì chapter đã có transform definitions, derivative/recurrence simplification, transfer functions, poles/zeros, stability, convolution và continuous/discrete các hệ thống (systems / 시스템들) perspective.


> **Chuyển mạch:** Từ **Audited but intentionally not rewritten**, ta sang **độ sâu (depth / 깊이) balance sau Round 11** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Độ sâu (depth / 깊이) balance sau Round 11

Sau Round 11, các cầu nối (bridge / 브리지) chains sau đã cân bằng hơn đáng kể:

```text
formal language → machine memory → computability → complexity
convex geometry → simplex → duality → integer optimization
rate → accumulation → conservation
metric → projection → statistical/ML geometry
probability → entropy → decision
AI model math → numerical/statistical production behavior
trigonometry → Fourier → transforms / PDE / signals
```


> **Chuyển mạch:** Từ **độ sâu (depth / 깊이) balance sau Round 11**, ta sang **Priority hợp lý cho Round 12** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Priority hợp lý cho Round 12

Không nên tiếp tục theo một fixed danh sách (list / 목록) chỉ dựa trên tệp (file / 파일) kích thước (size / 크기). Nên chuyển sang **library-wide consistency kiểm tra (audit / 감사)**:

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

Nếu vẫn cần rewrite content, chỉ chọn chapter bị phát hiện qua consistency kiểm tra (audit / 감사), thay vì tiếp tục “tệp (file / 파일) nhỏ → viết dài”.


> **Chuyển mạch:** Từ **Priority hợp lý cho Round 12**, ta sang **Kết luận** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết luận

Round 11 rewrite **7 chuẩn gốc (canonical / 정본)/liên kết (connection / 연결) files**, kiểm tra (audit / 감사) thêm 7 files và chủ động giữ nguyên chúng.

Nguyên tắc được siết chặt hơn:

> Độ hoàn thiện không được đo bằng số dòng. Một thư viện (library / 라이브러리) mature cần chuyển từ mở rộng content sang consistency, phụ thuộc (dependency / 의존성), notation, cross-link và editorial coherence.

> **Bàn giao:** Sau **Kết luận**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [10 glossary](./10_glossary.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
