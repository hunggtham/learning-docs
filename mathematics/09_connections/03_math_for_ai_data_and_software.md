# Liên kết kiến thức (knowledge connection / 지식 연결) — Toán trong AI, dữ liệu (data / 데이터) và Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학): từ biểu diễn (representation / 표현) đến reliable các hệ thống (systems / 시스템들)

> **Mạch đọc:** Đọc **liên kết kiến thức (knowledge connection / 지식 연결) — Toán trong AI, dữ liệu (data / 데이터) và Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학): từ biểu diễn (representation / 표현) đến reliable các hệ thống (systems / 시스템들)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. dữ liệu (data / 데이터) biểu diễn (representation / 표현) là quyết định toán học** sang **2. tuyến tính (linear / 선형) tầng (layer / 계층) là affine map**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


“Toán cho AI” thường bị trình bày như một danh sách môn học: tuyến tính (linear / 선형) algebra, calculus, xác suất (probability / 확률), statistics. Cách đó đúng nhưng chưa đủ. Trong thực tế, mỗi tầng (layer / 계층) của một hệ thống (system / 시스템) gọi đến một loại mathematical cấu trúc (structure / 구조) khác nhau.

Mental map hữu ích hơn:

```text
representation → linear algebra / geometry
change → calculus
uncertainty → probability
inference → statistics
search/decision → optimization
structure → discrete mathematics / graphs
computation → algorithms / numerical analysis
reliability → estimation / error / conditioning
```

## 1. dữ liệu (data / 데이터) biểu diễn (representation / 표현) là quyết định toán học

Một mẫu (sample / 표본) với features được map thành véc-tơ (vector / 벡터):

```math
x\in\mathbb R^d.
```

Batch trở thành ma trận (matrix / 행렬):

```math
X\in\mathbb R^{n\times d}.
```

Nhưng vectorization không neutral. Ta đã chọn:

```text
feature nào tồn tại
feature scale nào
missing value biểu diễn ra sao
categorical information encode thế nào
```

Biểu diễn (representation / 표현) quyết định hình học (geometry / 기하학) mà mô hình (model / 모델) nhìn thấy.

## 2. tuyến tính (linear / 선형) tầng (layer / 계층) là affine map

Một tầng (layer / 계층):

```math
z=Wx+b
```

là affine transformation.

Nếu ngăn xếp (stack / 스택) nhiều layers nhưng bỏ activation:

```math
W_3(W_2(W_1x+b_1)+b_2)+b_3
```

vẫn collapse thành một affine map.

Nonlinearity là thứ cho mạng (network / 네트워크) expressive power vượt one tuyến tính (linear / 선형) transformation.

## 3. hàm (function / 함수) composition là backbone của neural mạng (network / 네트워크)

Mô hình (model / 모델):

```math
f=f_L\circ f_{L-1}\circ\cdots\circ f_1.
```

Forward pass là composition.

Backpropagation chỉ là chuỗi (chain / 사슬) quy tắc (rule / 규칙) áp dụng efficiently qua computational đồ thị (graph / 그래프).

Nếu:

```math
y=f(g(x)),
```

thì:

```math
\frac{dy}{dx}=\frac{dy}{dg}\frac{dg}{dx}.
```

Trong véc-tơ (vector / 벡터) setting, Jacobians compose bằng phép nhân ma trận (matrix multiplication / 행렬 곱셈).

## 4. Computational đồ thị (graph / 그래프) nối calculus với software đồ thị (graph / 그래프)

Operations tạo nodes; tensors tạo values; dependencies tạo directed đồ thị (graph / 그래프).

Backward pass traverse đồ thị (graph / 그래프) reverse direction để accumulate gradients.

Đây là nơi:

```text
graph theory
+ chain rule
+ dynamic programming-like reuse
```

gặp nhau.

Automatic differentiation không phải symbolic differentiation cũng không phải finite difference. Nó evaluate chính xác (exact / 정확한) derivatives của program operations tới floating-point precision bằng chuỗi (chain / 사슬) quy tắc (rule / 규칙).

## 5. hàm mất mát (loss function / 손실 함수) chọn hình học (geometry / 기하학) của lỗi (error / 오류)

Regression squared mất mát (loss / 손실):

```math
L=\frac1n\sum_i(y_i-\hat y_i)^2.
```

Absolute mất mát (loss / 손실):

```math
L=\frac1n\sum_i|y_i-\hat y_i|.
```

Classification cross-entropy:

```math
L=-\sum_k y_k\log p_k.
```

Mỗi mất mát (loss / 손실) encode different priorities.

Squared mất mát (loss / 손실) penalize large errors quadratically; absolute mất mát (loss / 손실) robust hơn với outliers theo certain các mô hình (models / 모델들); cross-entropy corresponds to categorical likelihood.

“Chọn mất mát (loss / 손실)” là modeling quyết định (decision / 결정), không chỉ API parameter.

## 6. huấn luyện (training / 학습) là tối ưu hóa (optimization / 최적화) dưới finite dữ liệu (data / 데이터)

Empirical rủi ro (risk / 위험):

```math
\hat R(\theta)
=\frac1n\sum_{i=1}^nL(f_\theta(x_i),y_i).
```

Huấn luyện (training / 학습) solves approximately:

```math
\min_\theta\hat R(\theta).
```

Nhưng real mục tiêu (objective / 목표) là hiệu năng (performance / 성능) trên unknown future dữ liệu (data / 데이터) phân phối (distribution / 분포):

```math
R(\theta)=E[L(f_\theta(X),Y)].
```

Gap giữa empirical rủi ro (risk / 위험) và population rủi ro (risk / 위험) là statistical/generalization question, không chỉ tối ưu hóa (optimization / 최적화) question.

## 7. độ dốc (gradient / 기울기) descent dùng cục bộ (local / 로컬) thông tin (information / 정보)

Cập nhật (update / 업데이트):

```math
\theta_{t+1}=\theta_t-\eta\nabla L(\theta_t).
```

Độ dốc (gradient / 기울기) cho cục bộ (local / 로컬) direction of steepest increase theo Euclidean chỉ số (metric / 지표).

Step kích thước (size / 크기) quá lớn có thể overshoot; quá nhỏ convergence chậm.

Conditioning quyết định directions nào steep/flat và ảnh hưởng tối ưu hóa (optimization / 최적화) speed.

## 8. Hessian và curvature

Second-order approximation:

```math
L(\theta+\Delta)
\approx
L(\theta)+\nabla L^T\Delta
+\frac12\Delta^TH\Delta.
```

Hessian eigenvalues nói cục bộ (local / 로컬) curvature theo principal directions.

Large điều kiện (condition / 조건) number nghĩa landscape elongated; độ dốc (gradient / 기울기) descent zig-zag/slow.

Preconditioning và adaptive methods cố rescale hình học (geometry / 기하학).

## 9. xác suất (probability / 확률) đầu ra (output / 출력) cần interpretation

Softmax:

```math
p_k=\frac{e^{z_k}}{\sum_j e^{z_j}}
```

produce normalized positive numbers.

Nhưng “sum to 1” chưa đủ để guarantee calibrated probabilities.

Calibration là empirical/statistical thuộc tính (property / 속성) của mô hình (model / 모델) + dữ liệu (data / 데이터) phân phối (distribution / 분포).

Predicted `0.9` nên roughly đúng 90% trong relevant calibration population nếu mô hình (model / 모델) calibrated.

## 10. Log-sum-exp là numerical mathematics trong ML

Naive:

```math
\log\sum_i e^{x_i}
```

có thể overflow.

Rewrite với:

```math
m=\max_i x_i
```

thành:

```math
m+\log\sum_i e^{x_i-m}.
```

Mathematics chính xác (exact / 정확한), computation stable hơn.

Đây là important lesson:

> algebraically equivalent expressions có thể rất khác numerical hành vi (behavior / 동작).

## 11. Floating điểm (point / 지점) là finite mô hình (model / 모델) của real arithmetic

ML huấn luyện (training / 학습) dùng fp32, fp16, bfloat16.

Finite precision tạo:

```text
roundoff
overflow
underflow
loss of significance
non-associative summation
```

Ví dụ floating-point addition generally không associative:

```text
(a+b)+c ≠ a+(b+c)
```

exactly.

Parallel reduction thứ tự (order / 순서) có thể đổi final low-order bits.

## 12. Mixed precision là sự đánh đổi (trade-off / 트레이드오프)

Lower precision:

```text
faster compute
lower memory/bandwidth
```

nhưng động (dynamic / 동적) phạm vi (range / 범위)/precision khác.

Huấn luyện (training / 학습) frameworks dùng techniques như mất mát (loss / 손실) scaling để mitigate underflow.

Hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링) và numerical stability không thể tách hoàn toàn.

## 13. Embeddings tạo learned hình học (geometry / 기하학)

Embedding map:

```math
x\mapsto z\in\mathbb R^d.
```

Similarity tìm kiếm (search / 검색) dùng cosine/L2/inner sản phẩm (product / 제품).

Nếu learned mục tiêu (objective / 목표) thay đổi, hình học (geometry / 기하학) của embedding không gian (space / 공간) cũng thay đổi.

Véc-tơ (vector / 벡터) “gần” nghĩa gần theo mô hình (model / 모델) biểu diễn (representation / 표현), không universal ngữ nghĩa (semantic / 의미적) truth.

## 14. Curse of dimensionality

Trong high dimensions:

```text
space volume tăng nhanh
samples trở nên sparse
nearest-neighbor intuition yếu đi
```

Distance concentration có thể làm naive similarity methods kém discriminative.

Dimensionality reduction, regularization và biểu diễn (representation / 표현) học tập (learning / 학습) partly address this.

## 15. PCA và SVD như dữ liệu (data / 데이터) compression hình học (geometry / 기하학)

Center dữ liệu (data / 데이터) ma trận (matrix / 행렬) `X`, SVD:

```math
X=U\Sigma V^T.
```

Top singular directions capture maximum variance/reconstruction năng lượng (energy / 에너지) theo L2 criterion.

Low-rank approximation:

```math
X_k=U_k\Sigma_kV_k^T.
```

là best rank-`k` approximation under Frobenius norm.

Nhưng maximum variance không luôn equal maximum tác vụ (task / 작업) relevance.

## 16. Statistics bắt đầu ở train/kiểm thử (test / 테스트) split

Mô hình (model / 모델) evaluation trên finite kiểm thử (test / 테스트) set là estimation bài toán (problem / 문제).

Observed chỉ số (metric / 지표):

```text
accuracy = 84.2%
```

có sampling bất định (uncertainty / 불확실성).

So sánh mô hình (model / 모델) cần hỏi:

```text
difference có lớn hơn statistical noise không?
test set representative không?
multiple experiments đã chạy bao nhiêu?
```

ML benchmark không thoát khỏi statistical suy luận (inference / 추론).

## 17. phân phối (distribution / 분포) shift phá IID giả định (assumption / 가정)

Huấn luyện (training / 학습) thường idealize:

```math
(X_i,Y_i)\sim iid\ P.
```

Môi trường vận hành (production / 운영 환경) có thể gặp phân phối (distribution / 분포) `Q≠P`.

Examples:

```text
user behavior changes
sensor calibration drift
policy changes
market regime shifts
```

High offline score không guarantee môi trường vận hành (production / 운영 환경) độ tin cậy (reliability / 신뢰성) under shift.

## 18. nhân quả (causal / 인과적) question khác predictive question

Prediction asks:

```text
Y sẽ là gì khi observe X?
```

Nhân quả (causal / 인과적) question asks:

```text
Y thay đổi thế nào nếu intervene X?
```

Correlation/mô hình (model / 모델) fit alone không identify nhân quả (causal / 인과적) tác động (effect / 효과).

A/B testing, randomization và nhân quả (causal / 인과적) các giả định (assumptions / 가정들) matter nếu quyết định (decision / 결정) mục tiêu (target / 대상) là intervention.

## 19. đồ thị (graph / 그래프) lý thuyết (theory / 이론) trong kỹ nghệ phần mềm (software engineering / 소프트웨어 공학)

Phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프):

```text
package A → package B
```

Bản dựng (build / 빌드) thứ tự (order / 순서) dùng topological sort nếu DAG.

Lời gọi (call / 호출) đồ thị (graph / 그래프), dịch vụ (service / 서비스) đồ thị (graph / 그래프), workflow đồ thị (graph / 그래프), kiến thức (knowledge / 지식) đồ thị (graph / 그래프) và mạng (network / 네트워크) routing đều dùng đồ thị (graph / 그래프) concepts.

Cycle có meaning khác theo lĩnh vực (domain / 도메인):

```text
build dependency cycle → lỗi
state-machine cycle → bình thường
network route cycle → có thể problematic
```

Cấu trúc (structure / 구조) phải interpret theo bài toán (problem / 문제).

## 20. Trees và indexes

B-tree/B+cây (tree / 트리) power cơ sở dữ liệu (database / 데이터베이스) indexes vì balanced hierarchy cho logarithmic tìm kiếm (search / 검색)/cập nhật (update / 업데이트) độ sâu (depth / 깊이).

Băm (hash / 해시) chỉ mục (index / 인덱스) dựa trên different mathematical cấu trúc (structure / 구조).

Cấu trúc dữ liệu (data structure / 자료구조) choice là ánh xạ (mapping / 매핑) giữa thao tác (operation / 연산) profile và độ phức tạp (complexity / 복잡도) mô hình (model / 모델).

## 21. cơ sở dữ liệu (database / 데이터베이스) cardinality estimation là statistics

Truy vấn (query / 쿼리) planner cần estimate rows sau filters/joins.

Nếu estimate sai mạnh, optimizer có thể chọn bad plan.

Statistics như histograms, selectivity các giả định (assumptions / 가정들) và correlations ảnh hưởng hiệu năng (performance / 성능).

Backend hiệu năng (performance / 성능) vì vậy chứa xác suất (probability / 확률)/statistics dù nhà phát triển (developer / 개발자) không viết formula trực tiếp.

## 22. Big-O nói asymptotic growth, không chính xác (exact / 정확한) thời gian chạy (runtime / 런타임)

`O(n log n)` không automatically faster than `O(n^2)` cho all n.

Constants, bộ nhớ (memory / 메모리) locality, parallelism và hardware matter.

Nhưng độ phức tạp (complexity / 복잡도) rất hữu ích để detect quy mô (scale / 규모) disaster:

```text
n → 10n
```

có thể biến exponential thuật toán (algorithm / 알고리즘) thành impossible.

## 23. NP-hardness thay đổi kỹ thuật (engineering / 엔지니어링) chiến lược (strategy / 전략)

Nếu general chính xác (exact / 정확한) bài toán (problem / 문제) NP-hard, practical hệ thống (system / 시스템) có thể dùng:

```text
heuristic
approximation
relaxation
branch-and-bound
special-case structure
```

Mathematical hardness không nói “không làm được”; nó nói cần quản lý sự đánh đổi (trade-off / 트레이드오프) thay vì kỳ vọng one efficient chính xác (exact / 정확한) thuật toán (algorithm / 알고리즘) cho general trường hợp (case / 사례).

## 24. Numerical conditioning khác thuật toán (algorithm / 알고리즘) bug

Bài toán (problem / 문제) ill-conditioned nghĩa đầu ra (output / 출력) intrinsically sensitive với đầu vào (input / 입력) perturbation.

Stable thuật toán (algorithm / 알고리즘) không thể recover thông tin (information / 정보) đầu vào (input / 입력) không có.

Ví dụ nearly singular hệ tuyến tính (linear system / 선형 시스템) có thể đổi solution mạnh khi coefficients thay rất nhỏ.

Phân biệt:

```text
conditioning → property của problem
stability    → property của algorithm
```

## 25. Software khả năng quan sát (observability / 관측 가능성) cũng dùng tỷ lệ (rate / 비율)/accumulation/statistics

Metrics như:

```text
latency percentile
error rate
throughput
queue depth
CPU utilization
```

đều có mathematical ngữ nghĩa (semantics / 의미론).

Average độ trễ (latency / 지연 시간) có thể hide tail độ trễ (latency / 지연 시간). lỗi (error / 오류) tỷ lệ (rate / 비율) cần denominator. Percentile cần mẫu (sample / 표본) cửa sổ (window / 윈도우). thông lượng (throughput / 처리량) là tỷ lệ (rate / 비율), hàng đợi (queue / 큐) độ sâu (depth / 깊이) là accumulated trạng thái (state / 상태).

Monitoring đúng cần quantitative literacy.

## 26. AI hệ thống (system / 시스템) là chuỗi xử lý (pipeline / 파이프라인), không chỉ mô hình (model / 모델)

Môi trường vận hành (production / 운영 환경) AI gồm:

```text
data collection
→ preprocessing
→ model
→ calibration/threshold
→ retrieval
→ serving
→ monitoring
→ feedback
```

Math xuất hiện ở mỗi tầng (layer / 계층) khác nhau.

Một mô hình (model / 모델) mathematically tốt vẫn có thể thất bại (fail / 실패) vì dữ liệu (data / 데이터) leakage, unstable tính năng (feature / 기능) chuỗi xử lý (pipeline / 파이프라인), bad threshold, stale phân phối (distribution / 분포) hoặc numerical serving mismatch.

## 27. bảo mật (security / 보안) liên kết (connection / 연결)

Hashing, modular arithmetic, xác suất (probability / 확률) và combinatorics xuất hiện trong bảo mật (security / 보안).

Nhưng “dùng crypto math” không tự động tạo secure hệ thống (system / 시스템). giao thức (protocol / 프로토콜) thiết kế (design / 설계), randomness, key management và hiện thực (implementation / 구현) side channels matter.

Đây là recurring lesson:

```text
correct mathematics
≠ automatically correct system
```

## 28. Một forward pass nhìn bằng nhiều branches của math

Forward pass là ví dụ tốt để gom nhiều nhánh toán: linear algebra tạo biến đổi, calculus mô tả gradient, probability diễn giải output và optimization cập nhật tham số. Đọc theo chuỗi này giúp hiểu model như một hệ tính toán chứ không phải hộp đen.

```math
z=Wx+b,
\qquad
p=\operatorname{softmax}(z).
```

Ta có:

```text
W x          → linear algebra
+b           → affine geometry
softmax      → exponential / normalization
cross-entropy→ probability / information theory
backprop     → calculus / chain rule
optimizer    → numerical optimization
fp16         → numerical analysis
validation   → statistics
serving SLA  → systems metrics
```

Một vài dòng mã (code / 코드) có thể nằm ở intersection của gần toàn bộ Mathematics thư viện (library / 라이브러리).

## Dùng chung (common / 공통) thất bại (failure / 실패) modes

### Học “math for AI” như formula danh sách (list / 목록)

Dễ biết cú pháp (syntax / 문법) nhưng không biết các giả định (assumptions / 가정들).

### Tối ưu huấn luyện (training / 학습) mất mát (loss / 손실) như final goal

Population/generalization mới là mục tiêu (target / 대상) thực.

### Tin xác suất (probability / 확률) đầu ra (output / 출력) không kiểm tra calibration

Normalization không guarantee calibration.

### Dùng exact-real intuition cho floating điểm (point / 지점)

Algebraic equivalence có thể khác stability.

### Đánh đồng correlation với causation

Prediction và intervention là different questions.

## Mô hình tư duy (mental model / 사고 모델)

> AI/Data/Software là nơi nhiều mathematical structures gặp nhau. Representation quyết định geometry; calculus mô tả sensitivity; probability mô tả uncertainty; statistics kiểm tra evidence; optimization chọn decisions; discrete math mô tả structure; numerical analysis quyết định những công thức đó có chạy đáng tin trên machine hay không.
