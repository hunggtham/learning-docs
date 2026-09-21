# Knowledge Connection — Distance, Similarity và Projection: chọn geometry cho problem

“Gần nhau” không phải một fact tuyệt đối. Trong mathematics, statistics và machine learning, ta phải chọn **geometry**: metric nào đo difference, norm nào đo size, inner product nào đo alignment, projection nào giữ information relevant.

Mental flow:

```text
representation
→ scale
→ norm / metric
→ similarity
→ projection
→ downstream behavior
```

Metric choice không phải chi tiết implementation; nó là một phần của model.

## 1. Norm đo size của một vector

Euclidean norm:

```math
\|x\|_2=\sqrt{\sum_i x_i^2}.
```

Manhattan norm:

```math
\|x\|_1=\sum_i|x_i|.
```

Max norm:

```math
\|x\|_\infty=\max_i|x_i|.
```

Các norms khác nhau định nghĩa unit balls khác nhau, nên optimization geometry cũng khác.

`L1` thường gắn với sparse structure; `L2` tạo smooth rotationally symmetric geometry; `L∞` kiểm soát worst coordinate deviation.

## 2. Distance từ norm

Một common construction:

```math
d(x,y)=\|x-y\|.
```

Euclidean distance:

```math
d_2(x,y)=\sqrt{\sum_i(x_i-y_i)^2}.
```

Manhattan distance:

```math
d_1(x,y)=\sum_i|x_i-y_i|.
```

Trong grid movement, `L1` có thể natural hơn `L2`. Trong physical Euclidean space, `L2` thường phù hợp hơn.

## 3. Metric cần properties gì?

Một metric `d` thường thỏa:

```text
d(x,y) ≥ 0
 d(x,y)=0 iff x=y
 d(x,y)=d(y,x)
 d(x,z) ≤ d(x,y)+d(y,z)
```

Triangle inequality không chỉ là formalism; nó encode idea rằng indirect route không thể ngắn hơn arbitrary amount so với direct relation trong metric geometry.

Không phải mọi similarity score là metric.

## 4. Scale quyết định geometry quan sát được

Giả sử features:

```text
age: 20–60
income: 20,000,000–200,000,000 KRW
```

Raw Euclidean distance gần như bị income dominate.

Standardization:

```math
z_j=\frac{x_j-\mu_j}{\sigma_j}
```

rescale axes.

Nhưng standardization cũng encode assumption:

```text
1 standard deviation ở feature A
≈ comparable với
1 standard deviation ở feature B
```

Preprocessing không neutral; nó thay geometry.

## 5. Inner product đo alignment

Trong Euclidean space:

```math
\langle x,y\rangle=x^Ty.
```

Norm sinh từ inner product:

```math
\|x\|=\sqrt{\langle x,x\rangle}.
```

Angle:

```math
\cos\theta=\frac{\langle x,y\rangle}{\|x\|\|y\|}.
```

Inner product không chỉ là multiplication trick. Nó tạo notion angle, orthogonality và projection.

## 6. Cosine similarity bỏ magnitude

```math
\operatorname{cosSim}(x,y)
=\frac{x^Ty}{\|x\|\|y\|}.
```

Nếu embeddings cùng direction nhưng norms khác, cosine có thể vẫn gần 1.

Điều này hữu ích khi semantic direction quan trọng hơn scale, nhưng không universal.

Nếu vector norm chứa meaningful confidence/intensity, normalize có thể bỏ information quan trọng.

## 7. Projection là nearest-point problem

Projection của `v` lên unit direction `u`:

```math
\operatorname{proj}_u(v)=(u^Tv)u.
```

Tổng quát hơn, projection lên subspace `S` tìm:

```math
\hat v=\arg\min_{s\in S}\|v-s\|_2.
```

Residual:

```math
r=v-\hat v
```

vuông góc với subspace.

Projection formula không arbitrary; nó xuất hiện vì ta minimize squared Euclidean distance.

## 8. Least squares là projection

System overdetermined:

```math
Ax\approx b
```

least squares chọn:

```math
\hat x=\arg\min_x\|Ax-b\|_2^2.
```

Predicted vector `A\hat x` là projection của `b` lên column space `C(A)`.

Residual orthogonality:

```math
A^T(b-A\hat x)=0.
```

nên normal equations:

```math
A^TA\hat x=A^Tb.
```

Regression vì vậy là geometry trước khi là statistics.

## 9. PCA là projection nhưng criterion khác task relevance

PCA chọn directions maximize variance.

Projection lên top principal components giữ maximum variance theo squared reconstruction criterion.

Nhưng:

```text
high variance
≠ automatically high predictive importance
```

Một low-variance direction vẫn có thể chứa class signal.

Dimensionality reduction luôn gắn với criterion cụ thể.

## 10. Mahalanobis distance: covariance tạo geometry

Nếu data covariance là `Σ`, Mahalanobis distance:

```math
d_M(x,\mu)
=\sqrt{(x-\mu)^T\Sigma^{-1}(x-\mu)}.
```

Interpretation:

```text
large-variance direction → deviation ít surprising hơn
small-variance direction → same Euclidean deviation đáng kể hơn
correlated directions → không double-count naive
```

Nếu whiten data:

```math
z=\Sigma^{-1/2}(x-\mu),
```

Mahalanobis distance trở thành Euclidean distance trong whitened coordinates.

## 11. Singular covariance và pseudoinverse

Nếu features linearly dependent, `Σ` singular.

Then `Σ^{-1}` không tồn tại.

Possible approaches:

```text
remove redundant dimensions
regularize covariance
use pseudoinverse
work in lower-dimensional support
```

Metric formula luôn mang assumptions về rank và conditioning.

## 12. Kernel viewpoint: similarity có thể implicit

Kernel method dùng function:

```math
k(x,y)=\langle\phi(x),\phi(y)\rangle
```

mà không nhất thiết explicitly construct high-dimensional `φ(x)`.

Kernel trick nói similarity có thể encode inner product trong feature space khác.

Điều này nối geometry với nonlinear models.

## 13. Distance concentration ở high dimensions

Trong high-dimensional spaces, distances có thể trở nên less discriminative: nearest và farthest distances tương đối gần nhau dưới certain data distributions.

Đây là một aspect của **curse of dimensionality**.

Consequences:

```text
nearest-neighbor search khó hơn
sampling sparse hơn
local neighborhoods kém intuitive hơn
```

Metric choice và representation learning càng quan trọng.

## 14. Clustering phụ thuộc geometry

K-means minimizes:

```math
\sum_i\|x_i-\mu_{c(i)}\|_2^2.
```

Nó ưu tiên roughly spherical clusters theo Euclidean geometry.

Nếu clusters curved, categorical hoặc strongly different density, K-means geometry có thể sai.

“Cluster thật” không độc lập với metric/model.

## 15. Similarity search trong embeddings

Vector database thường dùng:

```text
cosine similarity
inner product
L2 distance
```

Nếu embeddings normalized:

```math
\|x\|=\|y\|=1,
```

then:

```math
\|x-y\|_2^2=2-2x^Ty.
```

Vì vậy cosine ranking và Euclidean ranking có thể equivalent trên unit sphere.

Đây là useful implementation connection.

## 16. Camera projection và loss of information

3D point projected lên 2D image mất depth information.

Projection ở đây là many-to-one mapping.

Nó minh họa broader principle:

> Projection giữ structure theo chosen representation nhưng discard orthogonal/unobserved information.

Inverse reconstruction cần additional assumptions, multiple views hoặc priors.

## 17. Distance trong graphs khác Euclidean distance

Graph shortest-path distance:

```math
d(u,v)=\text{length shortest path}
```

đo connectivity cost, không geometric straight-line displacement.

Social network “2 hops apart” và physical coordinates dùng different geometries.

Graph embeddings cố map structural distance/similarity vào vector space, luôn có distortion trade-off.

## 18. Finance: covariance geometry của portfolios

Portfolio variance:

```math
\operatorname{Var}(w^TR)=w^T\Sigma w.
```

Contours constant variance là ellipsoids.

Portfolio optimization không dùng Euclidean length của weights; covariance matrix định nghĩa risk geometry.

Một direction trong weight space có thể “dài” về risk dù coefficients numerically nhỏ.

## 19. Metric choice là modeling assumption

Nếu user vectors gần nhau, statement chính xác là:

```text
theo representation + metric hiện tại,
model coi chúng gần nhau
```

Không nên nâng nó thành:

```text
hai người thực sự giống nhau
```

Geometry inherited from data/model/objective, không phải truth universal.

## Common failure modes

### Raw features khác units

Distance bị scale dominate.

### Normalize khi magnitude có meaning

Có thể mất useful signal.

### Correlation ignored

Euclidean distance double-count redundant axes.

### High-dimensional intuition borrowed from 2D

Nearest-neighbor geometry thay đổi mạnh.

### Projection interpreted as lossless

Projection discard components ngoài subspace.

## Knowledge Connection

```text
Pythagoras → L2 norm
inner product → angle / cosine
orthogonality → projection
projection → least squares
covariance → Mahalanobis geometry
PCA → low-rank projection
kernel → implicit feature geometry
graph → shortest-path metric
AI search → embedding similarity
Finance → quadratic risk geometry
```

## Mental Model

> Chọn representation và metric là chọn geometry của problem. Distance nói “khác nhau bao nhiêu” theo geometry đó; similarity nói “align bao nhiêu”; projection giữ component phù hợp với chosen subspace/loss. Không có metric nào trung lập cho mọi domain.