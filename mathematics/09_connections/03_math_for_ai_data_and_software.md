# Knowledge Connection — Toán trong AI, Data và Software Engineering: từ representation đến reliable systems

“Toán cho AI” thường bị trình bày như một danh sách môn học: linear algebra, calculus, probability, statistics. Cách đó đúng nhưng chưa đủ. Trong thực tế, mỗi layer của một system gọi đến một loại mathematical structure khác nhau.

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

## 1. Data representation là quyết định toán học

Một sample với features được map thành vector:

```math
x\in\mathbb R^d.
```

Batch trở thành matrix:

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

Representation quyết định geometry mà model nhìn thấy.

## 2. Linear layer là affine map

Một layer:

```math
z=Wx+b
```

là affine transformation.

Nếu stack nhiều layers nhưng bỏ activation:

```math
W_3(W_2(W_1x+b_1)+b_2)+b_3
```

vẫn collapse thành một affine map.

Nonlinearity là thứ cho network expressive power vượt one linear transformation.

## 3. Function composition là backbone của neural network

Model:

```math
f=f_L\circ f_{L-1}\circ\cdots\circ f_1.
```

Forward pass là composition.

Backpropagation chỉ là chain rule áp dụng efficiently qua computational graph.

Nếu:

```math
y=f(g(x)),
```

thì:

```math
\frac{dy}{dx}=\frac{dy}{dg}\frac{dg}{dx}.
```

Trong vector setting, Jacobians compose bằng matrix multiplication.

## 4. Computational graph nối calculus với software graph

Operations tạo nodes; tensors tạo values; dependencies tạo directed graph.

Backward pass traverse graph reverse direction để accumulate gradients.

Đây là nơi:

```text
graph theory
+ chain rule
+ dynamic programming-like reuse
```

gặp nhau.

Automatic differentiation không phải symbolic differentiation cũng không phải finite difference. Nó evaluate exact derivatives của program operations tới floating-point precision bằng chain rule.

## 5. Loss function chọn geometry của error

Regression squared loss:

```math
L=\frac1n\sum_i(y_i-\hat y_i)^2.
```

Absolute loss:

```math
L=\frac1n\sum_i|y_i-\hat y_i|.
```

Classification cross-entropy:

```math
L=-\sum_k y_k\log p_k.
```

Mỗi loss encode different priorities.

Squared loss penalize large errors quadratically; absolute loss robust hơn với outliers theo certain models; cross-entropy corresponds to categorical likelihood.

“Chọn loss” là modeling decision, không chỉ API parameter.

## 6. Training là optimization dưới finite data

Empirical risk:

```math
\hat R(\theta)
=\frac1n\sum_{i=1}^nL(f_\theta(x_i),y_i).
```

Training solves approximately:

```math
\min_\theta\hat R(\theta).
```

Nhưng real objective là performance trên unknown future data distribution:

```math
R(\theta)=E[L(f_\theta(X),Y)].
```

Gap giữa empirical risk và population risk là statistical/generalization question, không chỉ optimization question.

## 7. Gradient descent dùng local information

Update:

```math
\theta_{t+1}=\theta_t-\eta\nabla L(\theta_t).
```

Gradient cho local direction of steepest increase theo Euclidean metric.

Step size quá lớn có thể overshoot; quá nhỏ convergence chậm.

Conditioning quyết định directions nào steep/flat và ảnh hưởng optimization speed.

## 8. Hessian và curvature

Second-order approximation:

```math
L(\theta+\Delta)
\approx
L(\theta)+\nabla L^T\Delta
+\frac12\Delta^TH\Delta.
```

Hessian eigenvalues nói local curvature theo principal directions.

Large condition number nghĩa landscape elongated; gradient descent zig-zag/slow.

Preconditioning và adaptive methods cố rescale geometry.

## 9. Probability output cần interpretation

Softmax:

```math
p_k=\frac{e^{z_k}}{\sum_j e^{z_j}}
```

produce normalized positive numbers.

Nhưng “sum to 1” chưa đủ để guarantee calibrated probabilities.

Calibration là empirical/statistical property của model + data distribution.

Predicted `0.9` nên roughly đúng 90% trong relevant calibration population nếu model calibrated.

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

Mathematics exact, computation stable hơn.

Đây là important lesson:

> algebraically equivalent expressions có thể rất khác numerical behavior.

## 11. Floating point là finite model của real arithmetic

ML training dùng fp32, fp16, bfloat16.

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

Parallel reduction order có thể đổi final low-order bits.

## 12. Mixed precision là trade-off

Lower precision:

```text
faster compute
lower memory/bandwidth
```

nhưng dynamic range/precision khác.

Training frameworks dùng techniques như loss scaling để mitigate underflow.

Performance engineering và numerical stability không thể tách hoàn toàn.

## 13. Embeddings tạo learned geometry

Embedding map:

```math
x\mapsto z\in\mathbb R^d.
```

Similarity search dùng cosine/L2/inner product.

Nếu learned objective thay đổi, geometry của embedding space cũng thay đổi.

Vector “gần” nghĩa gần theo model representation, không universal semantic truth.

## 14. Curse of dimensionality

Trong high dimensions:

```text
space volume tăng nhanh
samples trở nên sparse
nearest-neighbor intuition yếu đi
```

Distance concentration có thể làm naive similarity methods kém discriminative.

Dimensionality reduction, regularization và representation learning partly address this.

## 15. PCA và SVD như data compression geometry

Center data matrix `X`, SVD:

```math
X=U\Sigma V^T.
```

Top singular directions capture maximum variance/reconstruction energy theo L2 criterion.

Low-rank approximation:

```math
X_k=U_k\Sigma_kV_k^T.
```

là best rank-`k` approximation under Frobenius norm.

Nhưng maximum variance không luôn equal maximum task relevance.

## 16. Statistics bắt đầu ở train/test split

Model evaluation trên finite test set là estimation problem.

Observed metric:

```text
accuracy = 84.2%
```

có sampling uncertainty.

So sánh model cần hỏi:

```text
difference có lớn hơn statistical noise không?
test set representative không?
multiple experiments đã chạy bao nhiêu?
```

ML benchmark không thoát khỏi statistical inference.

## 17. Distribution shift phá IID assumption

Training thường idealize:

```math
(X_i,Y_i)\sim iid\ P.
```

Production có thể gặp distribution `Q≠P`.

Examples:

```text
user behavior changes
sensor calibration drift
policy changes
market regime shifts
```

High offline score không guarantee production reliability under shift.

## 18. Causal question khác predictive question

Prediction asks:

```text
Y sẽ là gì khi observe X?
```

Causal question asks:

```text
Y thay đổi thế nào nếu intervene X?
```

Correlation/model fit alone không identify causal effect.

A/B testing, randomization và causal assumptions matter nếu decision target là intervention.

## 19. Graph theory trong software engineering

Dependency graph:

```text
package A → package B
```

Build order dùng topological sort nếu DAG.

Call graph, service graph, workflow graph, knowledge graph và network routing đều dùng graph concepts.

Cycle có meaning khác theo domain:

```text
build dependency cycle → lỗi
state-machine cycle → bình thường
network route cycle → có thể problematic
```

Structure phải interpret theo problem.

## 20. Trees và indexes

B-tree/B+tree power database indexes vì balanced hierarchy cho logarithmic search/update depth.

Hash index dựa trên different mathematical structure.

Data structure choice là mapping giữa operation profile và complexity model.

## 21. Database cardinality estimation là statistics

Query planner cần estimate rows sau filters/joins.

Nếu estimate sai mạnh, optimizer có thể chọn bad plan.

Statistics như histograms, selectivity assumptions và correlations ảnh hưởng performance.

Backend performance vì vậy chứa probability/statistics dù developer không viết formula trực tiếp.

## 22. Big-O nói asymptotic growth, không exact runtime

`O(n log n)` không automatically faster than `O(n^2)` cho all n.

Constants, memory locality, parallelism và hardware matter.

Nhưng complexity rất hữu ích để detect scale disaster:

```text
n → 10n
```

có thể biến exponential algorithm thành impossible.

## 23. NP-hardness thay đổi engineering strategy

Nếu general exact problem NP-hard, practical system có thể dùng:

```text
heuristic
approximation
relaxation
branch-and-bound
special-case structure
```

Mathematical hardness không nói “không làm được”; nó nói cần quản lý trade-off thay vì kỳ vọng one efficient exact algorithm cho general case.

## 24. Numerical conditioning khác algorithm bug

Problem ill-conditioned nghĩa output intrinsically sensitive với input perturbation.

Stable algorithm không thể recover information input không có.

Ví dụ nearly singular linear system có thể đổi solution mạnh khi coefficients thay rất nhỏ.

Phân biệt:

```text
conditioning → property của problem
stability    → property của algorithm
```

## 25. Software observability cũng dùng rate/accumulation/statistics

Metrics như:

```text
latency percentile
error rate
throughput
queue depth
CPU utilization
```

đều có mathematical semantics.

Average latency có thể hide tail latency. Error rate cần denominator. Percentile cần sample window. Throughput là rate, queue depth là accumulated state.

Monitoring đúng cần quantitative literacy.

## 26. AI system là pipeline, không chỉ model

Production AI gồm:

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

Math xuất hiện ở mỗi layer khác nhau.

Một model mathematically tốt vẫn có thể fail vì data leakage, unstable feature pipeline, bad threshold, stale distribution hoặc numerical serving mismatch.

## 27. Security connection

Hashing, modular arithmetic, probability và combinatorics xuất hiện trong security.

Nhưng “dùng crypto math” không tự động tạo secure system. Protocol design, randomness, key management và implementation side channels matter.

Đây là recurring lesson:

```text
correct mathematics
≠ automatically correct system
```

## 28. Một forward pass nhìn bằng nhiều branches của math

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

Một vài dòng code có thể nằm ở intersection của gần toàn bộ Mathematics Library.

## Common failure modes

### Học “math for AI” như formula list

Dễ biết syntax nhưng không biết assumptions.

### Tối ưu training loss như final goal

Population/generalization mới là target thực.

### Tin probability output không kiểm tra calibration

Normalization không guarantee calibration.

### Dùng exact-real intuition cho floating point

Algebraic equivalence có thể khác stability.

### Đánh đồng correlation với causation

Prediction và intervention là different questions.

## Mental Model

> AI/Data/Software là nơi nhiều mathematical structures gặp nhau. Representation quyết định geometry; calculus mô tả sensitivity; probability mô tả uncertainty; statistics kiểm tra evidence; optimization chọn decisions; discrete math mô tả structure; numerical analysis quyết định những công thức đó có chạy đáng tin trên machine hay không.