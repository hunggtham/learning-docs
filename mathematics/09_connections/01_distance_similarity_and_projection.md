# Knowledge Connection — Distance, Similarity và Projection

“Gần nhau” nghe trực giác nhưng trong mathematics phải được định nghĩa. Geometry, statistics và machine learning đều cần một notion distance/similarity, và lựa chọn đó quyết định kết quả.

## Euclidean distance

```math
d(x,y)=\sqrt{\sum_i(x_i-y_i)^2}
```

đến từ Pythagoras và L2 norm. Nó hợp lý khi axes comparable, orthogonal và straight-line geometry phù hợp.

## Manhattan distance

```math
d_1(x,y)=\sum_i|x_i-y_i|
```

phù hợp grid movement hoặc settings nơi coordinate-wise costs add linearly.

## Cosine similarity

```math
\operatorname{cosSim}(x,y)=\frac{x\cdot y}{\|x\|\|y\|}
```

bỏ magnitude và đo angle alignment. Text embedding vectors thường dùng cosine vì direction có thể encode semantic pattern hữu ích hơn raw norm, nhưng điều này model-dependent.

## Projection

Projection tìm component của vector theo subspace/direction. Với unit `u`:

```math
\operatorname{proj}_u v=(u\cdot v)u
```

Least squares regression project observed vector lên column space của model. PCA project data lên principal directions. Camera projection map 3D world onto 2D image plane.

Một concept hình học xuất hiện dưới nhiều names vì question giống nhau: “phần của object nằm theo structure này là bao nhiêu?”.

## Normalization

Nếu features khác units/scales, distance bị dominated bởi large-scale axes. Standardization:

```math
z=\frac{x-\mu}{\sigma}
```

changes geometry bằng cách rescale axes.

Do đó preprocessing không chỉ “format data”; nó thay notion of distance và ảnh hưởng nearest neighbors, clustering, gradients.

## Mahalanobis distance

Khi features correlated, Euclidean distance double-count directions. Mahalanobis:

```math
d_M(x,\mu)=\sqrt{(x-\mu)^T\Sigma^{-1}(x-\mu)}
```

uses covariance geometry, effectively whitening correlated scale under suitable invertibility.

## Similarity không phải truth

Nếu user embeddings gần nhau, điều đó nghĩa representation/model coi họ gần theo learned features, không phải họ “giống nhau” trong mọi real-world sense. Metric choice encode assumptions và objectives.

## Mental Model

> Distance là một model của “khác nhau bao nhiêu”; similarity là một model của “alignment bao nhiêu”; projection là cách giữ component liên quan tới một direction/subspace. Chọn metric là chọn geometry của problem.

## Worked Example: nearest-neighbor thay đổi khi đổi scale

Hai features: age khoảng 20–60, annual income khoảng 20,000,000–200,000,000 KRW. Raw Euclidean distance gần như bị income differences thống trị vì numerical scale lớn hàng triệu lần age. Standardize mỗi feature:

```math
z_j=\frac{x_j-\mu_j}{\sigma_j}
```

làm một standard-deviation difference ở mỗi feature có comparable unitless scale.

Nhưng standardization cũng là assumption rằng one standard deviation ở age đáng so với one standard deviation ở income. Không preprocessing nào hoàn toàn neutral; nó encode geometry.

## Projection as information filtering

Khi project high-dimensional vector lên low-dimensional subspace, component orthogonal bị bỏ. PCA chọn subspace tối đa variance captured theo L2 criterion. Compression tốt nếu discarded directions chứa ít relevant information; nhưng high variance không luôn đồng nghĩa high task relevance.

## Connection với clustering

K-means minimize within-cluster squared Euclidean distance, nên chính metric và squared-loss geometry định nghĩa “cluster tốt”. Nếu data có non-spherical structure, categorical features hoặc outliers mạnh, geometry này có thể không phản ánh semantic groups; cần metric/model khác.

Trong mọi bài toán similarity, metric nên được xem là một phần của model specification, không phải lựa chọn kỹ thuật trung lập.

## Common Misconceptions

“Gần” phụ thuộc metric; Euclidean distance không phải lựa chọn đúng cho mọi data. Cosine similarity đo angle chứ không đo magnitude. Projection giữ component theo subspace, không phải lúc nào cũng giữ object “giống nhất” theo mọi loss function; least squares dùng Euclidean squared distance nên projection mới xuất hiện tự nhiên.

