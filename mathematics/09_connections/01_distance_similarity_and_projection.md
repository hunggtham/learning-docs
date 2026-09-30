# Liên kết kiến thức (knowledge connection / 지식 연결) — Distance, Similarity và Projection: chọn hình học (geometry / 기하학) cho bài toán (problem / 문제)

> **Mạch đọc:** Đọc **liên kết kiến thức (knowledge connection / 지식 연결) — Distance, Similarity và Projection: chọn hình học (geometry / 기하학) cho bài toán (problem / 문제)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Norm đo kích thước (size / 크기) của một véc-tơ (vector / 벡터)** sang **2. Distance từ norm**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


“Gần nhau” không phải một fact tuyệt đối. Trong mathematics, statistics và machine học tập (learning / 학습), ta phải chọn **hình học (geometry / 기하학)**: chỉ số (metric / 지표) nào đo difference, norm nào đo kích thước (size / 크기), inner sản phẩm (product / 제품) nào đo alignment, projection nào giữ thông tin (information / 정보) relevant.

Mental luồng (flow / 흐름):

```text
representation
→ scale
→ norm / metric
→ similarity
→ projection
→ downstream behavior
```

Chỉ số (metric / 지표) choice không phải chi tiết hiện thực (implementation / 구현); nó là một phần của mô hình (model / 모델).

## 1. Norm đo kích thước (size / 크기) của một véc-tơ (vector / 벡터)

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

Các norms khác nhau định nghĩa đơn vị (unit / 단위) balls khác nhau, nên tối ưu hóa (optimization / 최적화) hình học (geometry / 기하학) cũng khác.

`L1` thường gắn với sparse cấu trúc (structure / 구조); `L2` tạo smooth rotationally symmetric hình học (geometry / 기하학); `L∞` kiểm soát worst coordinate deviation.

## 2. Distance từ norm

Một dùng chung (common / 공통) construction:

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

Trong grid movement, `L1` có thể natural hơn `L2`. Trong vật lý (physical / 물리적) Euclidean không gian (space / 공간), `L2` thường phù hợp hơn.

## 3. chỉ số (metric / 지표) cần properties gì?

Một chỉ số (metric / 지표) `d` thường thỏa:

```text
d(x,y) ≥ 0
 d(x,y)=0 iff x=y
 d(x,y)=d(y,x)
 d(x,z) ≤ d(x,y)+d(y,z)
```

Triangle inequality không chỉ là formalism; nó encode idea rằng indirect tuyến (route / 경로) không thể ngắn hơn arbitrary amount so với direct quan hệ (relation / 관계) trong chỉ số (metric / 지표) hình học (geometry / 기하학).

Không phải mọi similarity score là chỉ số (metric / 지표).

## 4. quy mô (scale / 규모) quyết định hình học (geometry / 기하학) quan sát được

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

Nhưng standardization cũng encode giả định (assumption / 가정):

```text
1 standard deviation ở feature A
≈ comparable với
1 standard deviation ở feature B
```

Preprocessing không neutral; nó thay hình học (geometry / 기하학).

## 5. Inner sản phẩm (product / 제품) đo alignment

Trong Euclidean không gian (space / 공간):

```math
\langle x,y\rangle=x^Ty.
```

Norm sinh từ inner sản phẩm (product / 제품):

```math
\|x\|=\sqrt{\langle x,x\rangle}.
```

Angle:

```math
\cos\theta=\frac{\langle x,y\rangle}{\|x\|\|y\|}.
```

Inner sản phẩm (product / 제품) không chỉ là multiplication trick. Nó tạo notion angle, orthogonality và projection.

## 6. Cosine similarity bỏ magnitude

Cosine similarity so sánh hướng của hai vector và bỏ qua độ lớn. Nó phù hợp khi pattern tương đối quan trọng hơn scale, nhưng cần thận trọng khi magnitude mang ý nghĩa thực.

```math
\operatorname{cosSim}(x,y)
=\frac{x^Ty}{\|x\|\|y\|}.
```

Nếu embeddings cùng direction nhưng norms khác, cosine có thể vẫn gần 1.

Điều này hữu ích khi ngữ nghĩa (semantic / 의미적) direction quan trọng hơn quy mô (scale / 규모), nhưng không universal.

Nếu véc-tơ (vector / 벡터) norm chứa meaningful confidence/intensity, normalize có thể bỏ thông tin (information / 정보) quan trọng.

## 7. Projection là nearest-point bài toán (problem / 문제)

Projection của `v` lên đơn vị (unit / 단위) direction `u`:

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

Hệ thống (system / 시스템) overdetermined:

```math
Ax\approx b
```

least squares chọn:

```math
\hat x=\arg\min_x\|Ax-b\|_2^2.
```

Predicted véc-tơ (vector / 벡터) `A\hat x` là projection của `b` lên column không gian (space / 공간) `C(A)`.

Residual orthogonality:

```math
A^T(b-A\hat x)=0.
```

nên normal equations:

```math
A^TA\hat x=A^Tb.
```

Regression vì vậy là hình học (geometry / 기하학) trước khi là statistics.

## 9. PCA là projection nhưng criterion khác tác vụ (task / 작업) relevance

PCA chọn directions maximize variance.

Projection lên top principal components giữ maximum variance theo squared reconstruction criterion.

Nhưng:

```text
high variance
≠ automatically high predictive importance
```

Một low-variance direction vẫn có thể chứa lớp (class / 클래스) tín hiệu (signal / 신호).

Dimensionality reduction luôn gắn với criterion cụ thể.

## 10. Mahalanobis distance: covariance tạo hình học (geometry / 기하학)

Nếu dữ liệu (data / 데이터) covariance là `Σ`, Mahalanobis distance:

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

Nếu whiten dữ liệu (data / 데이터):

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

Chỉ số (metric / 지표) formula luôn mang các giả định (assumptions / 가정들) về rank và conditioning.

## 12. Kernel viewpoint: similarity có thể implicit

Kernel phương thức (method / 메서드) dùng hàm (function / 함수):

```math
k(x,y)=\langle\phi(x),\phi(y)\rangle
```

mà không nhất thiết explicitly construct high-dimensional `φ(x)`.

Kernel trick nói similarity có thể encode inner sản phẩm (product / 제품) trong tính năng (feature / 기능) không gian (space / 공간) khác.

Điều này nối hình học (geometry / 기하학) với nonlinear các mô hình (models / 모델들).

## 13. Distance concentration ở high dimensions

Trong high-dimensional spaces, distances có thể trở nên less discriminative: nearest và farthest distances tương đối gần nhau dưới certain dữ liệu (data / 데이터) distributions.

Đây là một aspect của **curse of dimensionality**.

Consequences:

```text
nearest-neighbor search khó hơn
sampling sparse hơn
local neighborhoods kém intuitive hơn
```

Chỉ số (metric / 지표) choice và biểu diễn (representation / 표현) học tập (learning / 학습) càng quan trọng.

## 14. Clustering phụ thuộc hình học (geometry / 기하학)

K-means minimizes:

```math
\sum_i\|x_i-\mu_{c(i)}\|_2^2.
```

Nó ưu tiên roughly spherical clusters theo Euclidean hình học (geometry / 기하학).

Nếu clusters curved, categorical hoặc strongly different density, K-means hình học (geometry / 기하학) có thể sai.

“Cluster thật” không độc lập với chỉ số (metric / 지표)/mô hình (model / 모델).

## 15. Similarity tìm kiếm (search / 검색) trong embeddings

Véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스) thường dùng:

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

Vì vậy cosine ranking và Euclidean ranking có thể equivalent trên đơn vị (unit / 단위) sphere.

Đây là useful hiện thực (implementation / 구현) liên kết (connection / 연결).

## 16. Camera projection và mất mát (loss / 손실) of thông tin (information / 정보)

3D điểm (point / 지점) projected lên 2D ảnh (image / 이미지) mất độ sâu (depth / 깊이) thông tin (information / 정보).

Projection ở đây là many-to-one ánh xạ (mapping / 매핑).

Nó minh họa broader principle:

> Projection giữ cấu trúc (structure / 구조) theo chosen biểu diễn (representation / 표현) nhưng discard orthogonal/unobserved thông tin (information / 정보).

Inverse reconstruction cần additional các giả định (assumptions / 가정들), multiple views hoặc priors.

## 17. Distance trong graphs khác Euclidean distance

Đồ thị (graph / 그래프) shortest-path distance:

```math
d(u,v)=\text{length shortest path}
```

đo connectivity chi phí (cost / 비용), không geometric straight-line displacement.

Xã hội (social / 사회적) mạng (network / 네트워크) “2 hops apart” và vật lý (physical / 물리적) coordinates dùng different geometries.

Đồ thị (graph / 그래프) embeddings cố map structural distance/similarity vào véc-tơ (vector / 벡터) không gian (space / 공간), luôn có distortion sự đánh đổi (trade-off / 트레이드오프).

## 18. Finance: covariance hình học (geometry / 기하학) của portfolios

Portfolio variance:

```math
\operatorname{Var}(w^TR)=w^T\Sigma w.
```

Contours constant variance là ellipsoids.

Portfolio tối ưu hóa (optimization / 최적화) không dùng Euclidean length của weights; covariance ma trận (matrix / 행렬) định nghĩa rủi ro (risk / 위험) hình học (geometry / 기하학).

Một direction trong weight không gian (space / 공간) có thể “dài” về rủi ro (risk / 위험) dù coefficients numerically nhỏ.

## 19. chỉ số (metric / 지표) choice là modeling giả định (assumption / 가정)

Nếu người dùng (user / 사용자) vectors gần nhau, statement chính xác là:

```text
theo representation + metric hiện tại,
model coi chúng gần nhau
```

Không nên nâng nó thành:

```text
hai người thực sự giống nhau
```

Hình học (geometry / 기하학) inherited from dữ liệu (data / 데이터)/mô hình (model / 모델)/mục tiêu (objective / 목표), không phải truth universal.

## Dùng chung (common / 공통) thất bại (failure / 실패) modes

### Raw features khác units

Distance bị quy mô (scale / 규모) dominate.

### Normalize khi magnitude có meaning

Có thể mất useful tín hiệu (signal / 신호).

### Correlation ignored

Euclidean distance double-count redundant axes.

### High-dimensional intuition borrowed from 2D

Nearest-neighbor hình học (geometry / 기하학) thay đổi mạnh.

### Projection interpreted as lossless

Projection discard components ngoài subspace.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Phần kết nối đưa distance, similarity và projection vào geometry, embeddings, nearest neighbors và anomaly detection. Hãy chọn metric theo invariance mà bài toán thực sự cần.

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

## Mô hình tư duy (mental model / 사고 모델)

> Chọn representation và metric là chọn geometry của problem. Distance nói “khác nhau bao nhiêu” theo geometry đó; similarity nói “align bao nhiêu”; projection giữ component phù hợp với chosen subspace/loss. Không có metric nào trung lập cho mọi domain.
