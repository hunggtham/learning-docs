# Support Vector Machines: margin, geometry và kernel

Support Vector Machine (SVM / 서포트 벡터 머신) xây classifier từ một geometric principle: không chỉ tìm hyperplane phân tách classes, mà tìm hyperplane có **margin** lớn. Margin là khoảng cách an toàn giữa decision boundary và những training points gần boundary nhất.

SVM quan trọng không chỉ vì bản thân algorithm; nó giúp hiểu regularization, convex optimization, duality, kernels và representation geometry.

## Từ separating hyperplane tới margin

Binary classifier:

\[
f(x)=\mathbf w^T\mathbf x+b
\]

Decision boundary:

\[
\mathbf w^T\mathbf x+b=0
\]

Với labels `y∈{-1,+1}`, nếu data linearly separable ta muốn:

\[
y_i(\mathbf w^T\mathbf x_i+b)\ge1
\]

Geometric margin tỉ lệ nghịch với norm của weight:

\[
margin=\frac{2}{\|\mathbf w\|}
\]

Maximize margin tương đương minimize:

\[
\frac12\|\mathbf w\|^2
\]

subject to classification constraints.

## Tại sao margin có ý nghĩa?

Nếu có nhiều boundaries đều classify training set hoàn hảo, boundary đi sát data points dễ thay đổi prediction khi input perturb nhẹ. Large margin chọn solution có buffer lớn hơn.

Đây là một inductive bias về robustness/generalization.

## Support Vectors

Chỉ những points nằm trên hoặc trong margin quyết định optimum mạnh nhất. Chúng gọi là **support vectors (서포트 벡터)**.

Points rất xa boundary thường không ảnh hưởng solution nếu constraints đã satisfied.

Đây là reason SVM có tên như vậy: boundary được “đỡ” bởi critical examples.

## Soft Margin

Real data thường không perfectly separable. Introduce slack variables `ξ_i`:

\[
y_i(\mathbf w^T\mathbf x_i+b)\ge1-\xi_i,\qquad \xi_i\ge0
\]

Objective:

\[
\min_{w,b,\xi}\frac12\|w\|^2+C\sum_i\xi_i
\]

`C` control trade-off:

- large `C`: phạt training violations mạnh, fit data hơn;
- small `C`: chấp nhận violations để giữ margin rộng hơn.

Đây là regularization trade-off dưới một form khác.

## Hinge Loss

Soft-margin SVM có thể viết gần với regularized empirical risk:

\[
J(w)=\frac12\|w\|^2+C\sum_i\max(0,1-y_if(x_i))
\]

Hinge loss bằng zero khi example không chỉ đúng mà còn nằm ngoài margin.

## Feature Scaling

SVM phụ thuộc dot products/distances, nên feature scale rất quan trọng. Một feature magnitude lớn có thể dominate geometry.

Standardization thường là preprocessing mặc định cho SVM.

## Kernel Trick

Nếu classes không linearly separable trong original space, ta có thể map input qua nonlinear feature map:

\[
\phi(x)
\]

rồi học linear separator trong transformed space.

Dual form của SVM phụ thuộc vào inner products:

\[
\phi(x_i)^T\phi(x_j)
\]

Nếu có kernel function:

\[
K(x_i,x_j)=\phi(x_i)^T\phi(x_j)
\]

thì không cần compute `φ(x)` explicitly. Đây là **kernel trick**.

RBF kernel:

\[
K(x,z)=\exp(-\gamma\|x-z\|^2)
\]

cho nonlinear boundaries rất linh hoạt.

## Kernel không phải magic similarity bất kỳ

Kernel hợp lệ cần thỏa properties để tương ứng inner product trong một feature space, thường liên quan positive semidefinite Gram matrix.

Không phải mọi similarity function tùy ý đều có thể dùng như kernel mà vẫn giữ theory/optimization properties.

## C và gamma

Với RBF SVM:

- `C` điều khiển penalty cho classification errors/margin violations;
- `γ` điều khiển mức local của kernel.

`γ` quá lớn làm mỗi point influence vùng rất nhỏ → boundary phức tạp/high variance.

`γ` quá nhỏ làm influence quá rộng → model quá smooth/high bias.

Hyperparameter search cần nested/correct validation để tránh optimistic bias.

## Computational scaling

Kernel SVM cần pairwise relationships giữa training points; memory/time có thể tăng rất mạnh với `n`.

Vì vậy kernel SVM phù hợp hơn small/medium datasets. Large-scale problems thường dùng linear SVM, approximate kernels hoặc models khác.

## SVM vs Logistic Regression

Cả hai có linear decision boundary nếu dùng raw linear features.

Logistic Regression optimize probabilistic log-loss và output probability model trực tiếp.

SVM optimize margin/hinge objective; raw decision score không phải calibrated probability.

Nếu cần probability, có thể calibrate SVM bằng Platt scaling hoặc isotonic regression trên held-out data.

## Kernels và Neural Representation Learning

Kernel methods encode nonlinear similarity thông qua fixed/designed kernel. Deep Learning học representation `φ_θ(x)` từ data.

Có thể nhìn một neural network như học feature space rồi dùng simple output head. Difference lớn là feature map trong deep learning được learned jointly, thay vì kernel fixed trước.

## Mental Model

> SVM hỏi: boundary nào không chỉ đúng trên training data mà còn giữ khoảng cách an toàn lớn nhất với critical examples?

Kernel mở rộng câu hỏi này sang một feature space nonlinear mà ta có thể không cần biểu diễn trực tiếp.

## Common Misconceptions

### “Support vectors là mọi points gần boundary”

Theo optimization, support vectors là points có nonzero dual coefficients; chúng là points active trong solution.

### “SVM luôn tốt cho high-dimensional data”

Linear SVM có thể rất mạnh với sparse high-dimensional data như text, nhưng kernel SVM có scaling issue theo sample size.

### “Kernel trick giống neural network hidden layer”

Cả hai tạo effective nonlinear representation, nhưng kernel map thường fixed/implicit còn neural representation learned.

### “SVM score là probability”

Không. Margin score cần calibration nếu muốn probabilistic interpretation.

## Knowledge Connection

SVM nối [Optimization](../01_mathematical_foundations/06_optimization.md), [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md) và [Bias–Variance](./14_bias_variance_and_generalization.md).

Xem tiếp: [Clustering](./11_clustering.md), nơi không còn target labels để định nghĩa boundary.