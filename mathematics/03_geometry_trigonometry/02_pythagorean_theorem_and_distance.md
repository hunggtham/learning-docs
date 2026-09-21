# Định lý Pythagoras và ý tưởng khoảng cách: từ tam giác vuông đến vector norm

Định lý Pythagoras (Pythagorean theorem / 피타고라스 정리) thường được nhớ bằng

```math
c^2=a^2+b^2,
```

nhưng giá trị thật của nó không nằm ở một công thức tính cạnh. Nó diễn tả một principle sâu hơn:

> Khi hai components **vuông góc** nhau trong Euclidean geometry, squared magnitude của tổng bằng tổng squared magnitudes.

Idea này đi thẳng từ tam giác vuông sang coordinate distance, vector norm, projection, least squares, signal energy và high-dimensional geometry.

## Vì sao bình phương xuất hiện?

Một proof bằng area làm rõ điều này.

Xét square lớn cạnh `a+b`, chứa bốn right triangles có legs `a,b` và một central square cạnh `c`.

Whole area:

```math
(a+b)^2.
```

Decomposition:

```math
4\left(\frac12ab\right)+c^2
=2ab+c^2.
```

Equate:

```math
a^2+2ab+b^2
=
2ab+c^2,
```

nên

```math
a^2+b^2=c^2.
```

Squares xuất hiện trực tiếp từ area. Ở level sâu hơn, inner-product geometry làm squared norm additive cho orthogonal components.

## Converse: relation cũng detect right angle

Nếu positive side lengths thỏa

```math
a^2+b^2=c^2,
```

thì angle opposite `c` là 90°.

Vì vậy theorem không chỉ nói “right triangle implies equation”; converse nói equation characterizes rightness.

Điều này useful trong geometry, surveying và computational checks.

## Coordinate distance được derive như thế nào?

Hai points

```math
P=(x_1,y_1),
\qquad
Q=(x_2,y_2).
```

Difference components:

```math
\Delta x=x_2-x_1,
```

```math
\Delta y=y_2-y_1.
```

Horizontal và vertical directions orthogonal, nên

```math
d^2=(\Delta x)^2+(\Delta y)^2.
```

Do distance nonnegative:

```math
d
=
\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}.
```

Trong 3D:

```math
d
=
\sqrt{(\Delta x)^2+(\Delta y)^2+(\Delta z)^2}.
```

Trong `n` dimensions:

```math
\|x-y\|_2
=
\sqrt{\sum_{i=1}^n(x_i-y_i)^2}.
```

Euclidean distance chỉ là repeated Pythagoras across orthogonal coordinate axes.

## Vector norm và inner product

L2 norm:

```math
\|v\|_2
=
\sqrt{v\cdot v}.
```

Với vectors `u,v`:

```math
\|u+v\|^2
=
\|u\|^2+2u\cdot v+\|v\|^2.
```

Nếu orthogonal:

```math
u\cdot v=0,
```

thì

```math
\|u+v\|^2
=
\|u\|^2+\|v\|^2.
```

Đây là generalized Pythagorean theorem. Formula triangle là special case của inner-product space.

## Projection: tách signal thành perpendicular components

Cho vector `v` và subspace `S`. Projection `p` của `v` lên `S` tạo residual

```math
r=v-p
```

orthogonal với `S`.

Do `p\perp r`:

```math
\|v\|^2
=
\|p\|^2+\|r\|^2.
```

This identity explains why orthogonal projection minimizes Euclidean distance. Nếu chọn point khác `q` trong `S`, then

```math
v-q=(v-p)+(p-q),
```

và hai components orthogonal, nên

```math
\|v-q\|^2
=
\|v-p\|^2+\|p-q\|^2
\ge
\|v-p\|^2.
```

Đây là proof idea của least squares geometry.

## Worked example — nearest point trên một line

Tìm point trên x-axis gần point `(3,4)` nhất.

Projection là `(3,0)`. Residual là `(0,4)`.

Distance:

```math
\sqrt{(3-3)^2+(4-0)^2}=4.
```

Nếu chọn point `(x,0)` bất kỳ:

```math
d^2=(x-3)^2+16\ge16.
```

Minimum tại `x=3`.

Pythagoras cho cả geometry lẫn optimization argument.

## Law of cosines: khi components không orthogonal

Pythagoras chỉ clean khi angle 90°. General triangle với angle `\theta` giữa sides `a,b`:

```math
c^2=a^2+b^2-2ab\cos\theta.
```

Cross term biến mất khi

```math
\cos90^\circ=0.
```

Từ vector identity:

```math
\|u-v\|^2
=
\|u\|^2+\|v\|^2-2u\cdot v,
```

và

```math
u\cdot v=\|u\|\|v\|\cos\theta,
```

law of cosines xuất hiện tự nhiên.

Pythagoras là zero-cross-term case.

## Distance không phải một khái niệm duy nhất

Euclidean distance phù hợp khi geometry isotropic và coordinate scales meaningful. Nhưng other metrics may better match problem.

Manhattan distance:

```math
\|x-y\|_1
=
\sum_i|x_i-y_i|.
```

Max distance:

```math
\|x-y\|_\infty
=
\max_i|x_i-y_i|.
```

Mahalanobis distance accounts for covariance/scaling:

```math
d_M(x,y)
=
\sqrt{(x-y)^T\Sigma^{-1}(x-y)}.
```

Choosing metric is a modeling decision.

## Why feature scaling matters in ML

Suppose feature vector is

```text
(age in years, income in KRW)
```

Age range ~100, income range millions. Raw Euclidean distance will be dominated by income coordinate.

If geometry should treat both features comparably, normalization/standardization or learned metric may be needed.

Distance algorithm can be mathematically correct but semantically wrong if representation scale is wrong.

## Pythagoras và variance decomposition

A similar orthogonal-sum structure appears in statistics.

In linear regression, fitted vector and residual are orthogonal under ordinary least squares, leading to sum-of-squares decompositions under proper conditions.

ANOVA and projection-based statistics repeatedly reuse “total squared magnitude = explained + orthogonal residual” logic.

This is not accidental; linear regression lives in Euclidean vector geometry.

## Physics connection — energy in orthogonal modes

If a physical state decomposes into orthogonal modes, squared amplitudes often add. Wave/signal energy, quantum-state amplitudes under orthogonal basis and Fourier coefficients all use related Hilbert-space geometry.

Parseval-type identities generalize Pythagorean energy decomposition to function spaces.

## Computer graphics connection

For collision test between point and circle center:

```math
(\Delta x)^2+(\Delta y)^2\le r^2.
```

No square root needed because square root is monotonic on nonnegative numbers.

This is a simple example where understanding formula structure yields computational improvement.

## Geodesic distance: Euclidean formula can fail on curved spaces

On Earth's surface, straight-line distance through 3D space is not road/geodesic distance along surface. Latitude/longitude differences cannot be fed naively into flat Pythagorean formula over large distances.

On curved manifolds, shortest path follows geometry of the space itself.

Thus Euclidean distance is a model assumption about space.

## High-dimensional geometry surprises

In high dimensions, distances can concentrate: nearest and farthest points become relatively less distinguishable under some distributions. This weakens intuitive nearest-neighbor reasoning and contributes to curse-of-dimensionality phenomena.

Pythagorean formula still holds, but geometry's practical meaning changes with dimension.

## Assumptions và failure modes

Pythagorean additivity requires orthogonality in an inner-product geometry. If axes are not orthogonal, cross terms appear.

Coordinate distance assumes coordinates share meaningful metric scale. Data with categorical features, cyclic angles or correlations may need different representation/metric.

Squared distance exaggerates outliers because deviations are squared.

## Mental Model

> Pythagoras is not mainly about triangles; it is the rule of orthogonal decomposition. When two components do not interfere through an inner product, their squared magnitudes add. Distance, projection, least squares and energy decompositions are all descendants of this same geometry.

## Common Misconceptions

**“`a^2+b^2=c^2` applies to any triangle.”** Only right-angle/orthogonal case; otherwise use law of cosines.

**“Euclidean distance is the natural metric for all data.”** Metric choice depends on representation and domain.

**“Large coordinate difference always means large semantic difference.”** Not if units/scales differ or features encode different structures.

**“Square root is required for every distance comparison.”** Comparing squared distances is equivalent when all quantities nonnegative.

**“Pythagoras is only 2D geometry.”** It generalizes to inner-product spaces and orthogonal projections in arbitrary dimensions.