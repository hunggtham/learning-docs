# Định lý Pythagoras và ý tưởng khoảng cách: từ tam giác vuông đến véc-tơ (vector / 벡터) norm

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Định lý Pythagoras và ý tưởng khoảng cách: từ tam giác vuông đến véc-tơ (vector / 벡터) norm**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vì sao bình phương xuất hiện?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Converse: quan hệ (relation / 관계) cũng detect right angle** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối Pythagorean theorem với distance và coordinate geometry, để độ dài được suy ra từ cấu trúc vuông góc.

Định lý Pythagoras (Pythagorean theorem / 피타고라스 정리) thường được nhớ bằng

```math
c^2=a^2+b^2,
```

nhưng giá trị thật của nó không nằm ở một công thức tính cạnh. Nó diễn tả một principle sâu hơn:

> Khi hai components **vuông góc** nhau trong Euclidean hình học (geometry / 기하학), squared magnitude của tổng bằng tổng squared magnitudes.

Idea này đi thẳng từ tam giác vuông sang coordinate distance, véc-tơ (vector / 벡터) norm, projection, least squares, tín hiệu (signal / 신호) năng lượng (energy / 에너지) và high-dimensional hình học (geometry / 기하학).

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

Squares xuất hiện trực tiếp từ area. Ở mức (level / 수준) sâu hơn, inner-product hình học (geometry / 기하학) làm squared norm additive cho orthogonal components.

> **Nối mạch:** Trong **Định lý Pythagoras và ý tưởng khoảng cách: từ tam giác vuông đến véc-tơ (vector / 벡터) norm**, **Converse: quan hệ (relation / 관계) cũng detect right angle** nối từ **Vì sao bình phương xuất hiện?** sang **Coordinate distance được derive như thế nào?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Converse: quan hệ (relation / 관계) cũng detect right angle

Nếu positive side lengths thỏa

```math
a^2+b^2=c^2,
```

thì angle opposite `c` là 90°.

Vì vậy theorem không chỉ nói “right triangle implies equation”; converse nói equation characterizes rightness.

Điều này useful trong hình học (geometry / 기하학), surveying và computational checks.

> **Nối mạch:** Ở chặng này của **Định lý Pythagoras và ý tưởng khoảng cách: từ tam giác vuông đến véc-tơ (vector / 벡터) norm**, **Coordinate distance được derive như thế nào?** nối từ **Converse: quan hệ (relation / 관계) cũng detect right angle** sang **Véc-tơ (vector / 벡터) norm và inner sản phẩm (product / 제품)**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Định lý Pythagoras và ý tưởng khoảng cách: từ tam giác vuông đến véc-tơ (vector / 벡터) norm**, **Véc-tơ (vector / 벡터) norm và inner sản phẩm (product / 제품)** nối từ **Coordinate distance được derive như thế nào?** sang **Projection: tách tín hiệu (signal / 신호) thành perpendicular components**, vì cơ chế trước tạo đầu vào cho bước sau.

## Véc-tơ (vector / 벡터) norm và inner sản phẩm (product / 제품)

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

Đây là generalized Pythagorean theorem. Formula triangle là special trường hợp (case / 사례) của inner-product không gian (space / 공간).

> **Nối mạch:** Trong **Định lý Pythagoras và ý tưởng khoảng cách: từ tam giác vuông đến véc-tơ (vector / 벡터) norm**, **Projection: tách tín hiệu (signal / 신호) thành perpendicular components** nối từ **Véc-tơ (vector / 벡터) norm và inner sản phẩm (product / 제품)** sang **Worked example — nearest điểm (point / 지점) trên một line**, vì cơ chế trước tạo đầu vào cho bước sau.

## Projection: tách tín hiệu (signal / 신호) thành perpendicular components

Cho véc-tơ (vector / 벡터) `v` và subspace `S`. Projection `p` của `v` lên `S` tạo residual

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

This định danh (identity / 식별자) explains why orthogonal projection minimizes Euclidean distance. Nếu chọn điểm (point / 지점) khác `q` trong `S`, then

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

Đây là proof idea của least squares hình học (geometry / 기하학).

> **Nối mạch:** Ở chặng này của **Định lý Pythagoras và ý tưởng khoảng cách: từ tam giác vuông đến véc-tơ (vector / 벡터) norm**, **Projection: tách tín hiệu (signal / 신호) thành perpendicular components** nêu quy tắc; **Worked example — nearest điểm (point / 지점) trên một line** thử quy tắc trong tình huống, rồi **Law of cosines: khi components không orthogonal** mở rộng hệ quả.

## Worked example — nearest điểm (point / 지점) trên một line

Tìm điểm (point / 지점) trên x-axis gần điểm (point / 지점) `(3,4)` nhất.

Projection là `(3,0)`. Residual là `(0,4)`.

Distance:

```math
\sqrt{(3-3)^2+(4-0)^2}=4.
```

Nếu chọn điểm (point / 지점) `(x,0)` bất kỳ:

```math
d^2=(x-3)^2+16\ge16.
```

Minimum tại `x=3`.

Pythagoras cho cả hình học (geometry / 기하학) lẫn tối ưu hóa (optimization / 최적화) argument.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Định lý Pythagoras và ý tưởng khoảng cách: từ tam giác vuông đến véc-tơ (vector / 벡터) norm**, **Worked example — nearest điểm (point / 지점) trên một line** nêu quy tắc; **Law of cosines: khi components không orthogonal** thử quy tắc trong tình huống, rồi **Distance không phải một khái niệm duy nhất** mở rộng hệ quả.

## Law of cosines: khi components không orthogonal

Pythagoras chỉ clean khi angle 90°. General triangle với angle `\theta` giữa sides `a,b`:

```math
c^2=a^2+b^2-2ab\cos\theta.
```

Cross term biến mất khi

```math
\cos90^\circ=0.
```

Từ véc-tơ (vector / 벡터) định danh (identity / 식별자):

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

Pythagoras là zero-cross-term trường hợp (case / 사례).

> **Nối mạch:** Trong **Định lý Pythagoras và ý tưởng khoảng cách: từ tam giác vuông đến véc-tơ (vector / 벡터) norm**, **Distance không phải một khái niệm duy nhất** nối từ **Law of cosines: khi components không orthogonal** sang **Why tính năng (feature / 기능) scaling matters in ML**, vì cơ chế trước tạo đầu vào cho bước sau.

## Distance không phải một khái niệm duy nhất

Euclidean distance phù hợp khi hình học (geometry / 기하학) isotropic và coordinate scales meaningful. Nhưng other metrics may better match bài toán (problem / 문제).

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

Choosing chỉ số (metric / 지표) is a modeling quyết định (decision / 결정).

> **Nối mạch:** Ở chặng này của **Định lý Pythagoras và ý tưởng khoảng cách: từ tam giác vuông đến véc-tơ (vector / 벡터) norm**, **Why tính năng (feature / 기능) scaling matters in ML** nối từ **Distance không phải một khái niệm duy nhất** sang **Pythagoras và variance decomposition**, vì cơ chế trước tạo đầu vào cho bước sau.

## Why tính năng (feature / 기능) scaling matters in ML

Suppose tính năng (feature / 기능) véc-tơ (vector / 벡터) is

```text
(age in years, income in KRW)
```

Age phạm vi (range / 범위) ~100, income phạm vi (range / 범위) millions. Raw Euclidean distance will be dominated by income coordinate.

If hình học (geometry / 기하학) should treat both features comparably, normalization/standardization or learned chỉ số (metric / 지표) may be needed.

Distance thuật toán (algorithm / 알고리즘) can be mathematically correct but semantically wrong if biểu diễn (representation / 표현) quy mô (scale / 규모) is wrong.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Định lý Pythagoras và ý tưởng khoảng cách: từ tam giác vuông đến véc-tơ (vector / 벡터) norm**, **Pythagoras và variance decomposition** nối từ **Why tính năng (feature / 기능) scaling matters in ML** sang **Physics liên kết (connection / 연결) — năng lượng (energy / 에너지) in orthogonal modes**, vì cơ chế trước tạo đầu vào cho bước sau.

## Pythagoras và variance decomposition

A similar orthogonal-sum cấu trúc (structure / 구조) appears in statistics.

In tuyến tính (linear / 선형) regression, fitted véc-tơ (vector / 벡터) and residual are orthogonal under ordinary least squares, leading to sum-of-squares decompositions under proper conditions.

ANOVA and projection-based statistics repeatedly reuse “total squared magnitude = explained + orthogonal residual” lô-gic (logic / 논리).

This is not accidental; tuyến tính (linear / 선형) regression lives in Euclidean véc-tơ (vector / 벡터) hình học (geometry / 기하학).

> **Nối mạch:** Trong **Định lý Pythagoras và ý tưởng khoảng cách: từ tam giác vuông đến véc-tơ (vector / 벡터) norm**, sau nội dung của **Pythagoras và variance decomposition**, **Physics liên kết (connection / 연결) — năng lượng (energy / 에너지) in orthogonal modes** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Computer graphics liên kết (connection / 연결)** mở rộng hệ quả hoặc giới hạn liên quan.

## Physics liên kết (connection / 연결) — năng lượng (energy / 에너지) in orthogonal modes

If a vật lý (physical / 물리적) trạng thái (state / 상태) decomposes into orthogonal modes, squared amplitudes often add. Wave/tín hiệu (signal / 신호) năng lượng (energy / 에너지), quantum-state amplitudes under orthogonal basis and Fourier coefficients all use related Hilbert-space hình học (geometry / 기하학).

Parseval-type identities generalize Pythagorean năng lượng (energy / 에너지) decomposition to hàm (function / 함수) spaces.

> **Nối mạch:** Ở chặng này của **Định lý Pythagoras và ý tưởng khoảng cách: từ tam giác vuông đến véc-tơ (vector / 벡터) norm**, **Computer graphics liên kết (connection / 연결)** nối từ **Physics liên kết (connection / 연결) — năng lượng (energy / 에너지) in orthogonal modes** sang **Geodesic distance: Euclidean formula can thất bại (fail / 실패) on curved spaces**, vì cơ chế trước tạo đầu vào cho bước sau.

## Computer graphics liên kết (connection / 연결)

For collision kiểm thử (test / 테스트) between điểm (point / 지점) and circle center:

```math
(\Delta x)^2+(\Delta y)^2\le r^2.
```

No square gốc (root / 루트) needed because square gốc (root / 루트) is monotonic on nonnegative numbers.

This is a simple example where understanding formula cấu trúc (structure / 구조) yields computational improvement.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Định lý Pythagoras và ý tưởng khoảng cách: từ tam giác vuông đến véc-tơ (vector / 벡터) norm**, **Geodesic distance: Euclidean formula can thất bại (fail / 실패) on curved spaces** nối từ **Computer graphics liên kết (connection / 연결)** sang **High-dimensional hình học (geometry / 기하학) surprises**, vì cơ chế trước tạo đầu vào cho bước sau.

## Geodesic distance: Euclidean formula can thất bại (fail / 실패) on curved spaces

On Earth's surface, straight-line distance through 3D không gian (space / 공간) is not road/geodesic distance along surface. Latitude/longitude differences cannot be fed naively into flat Pythagorean formula over large distances.

On curved manifolds, shortest đường dẫn (path / 경로) follows hình học (geometry / 기하학) of the không gian (space / 공간) itself.

Thus Euclidean distance is a mô hình (model / 모델) giả định (assumption / 가정) about không gian (space / 공간).

> **Nối mạch:** Trong **Định lý Pythagoras và ý tưởng khoảng cách: từ tam giác vuông đến véc-tơ (vector / 벡터) norm**, **High-dimensional hình học (geometry / 기하학) surprises** nối từ **Geodesic distance: Euclidean formula can thất bại (fail / 실패) on curved spaces** sang **Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes**, vì cơ chế trước tạo đầu vào cho bước sau.

## High-dimensional hình học (geometry / 기하학) surprises

In high dimensions, distances can concentrate: nearest and farthest points become relatively less distinguishable under some distributions. This weakens intuitive nearest-neighbor lập luận (reasoning / 추론) and contributes to curse-of-dimensionality phenomena.

Pythagorean formula still holds, but hình học (geometry / 기하학)'s practical meaning changes with dimension.

> **Nối mạch:** Ở chặng này của **Định lý Pythagoras và ý tưởng khoảng cách: từ tam giác vuông đến véc-tơ (vector / 벡터) norm**, **Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes** nối từ **High-dimensional hình học (geometry / 기하학) surprises** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes

Pythagorean additivity requires orthogonality in an inner-product hình học (geometry / 기하학). If axes are not orthogonal, cross terms appear.

Coordinate distance assumes coordinates share meaningful chỉ số (metric / 지표) quy mô (scale / 규모). dữ liệu (data / 데이터) with categorical features, cyclic angles or correlations may need different biểu diễn (representation / 표현)/chỉ số (metric / 지표).

Squared distance exaggerates outliers because deviations are squared.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Định lý Pythagoras và ý tưởng khoảng cách: từ tam giác vuông đến véc-tơ (vector / 벡터) norm**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Pythagoras is not mainly about triangles; it is the quy tắc (rule / 규칙) of orthogonal decomposition. When two components do not interfere through an inner sản phẩm (product / 제품), their squared magnitudes add. Distance, projection, least squares and năng lượng (energy / 에너지) decompositions are all descendants of this same hình học (geometry / 기하학).

> **Nối mạch:** Trong **Định lý Pythagoras và ý tưởng khoảng cách: từ tam giác vuông đến véc-tơ (vector / 벡터) norm**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Dùng chung (common / 공통) Misconceptions

**“`a^2+b^2=c^2` applies to any triangle.”** Only right-angle/orthogonal trường hợp (case / 사례); otherwise use law of cosines.

**“Euclidean distance is the natural chỉ số (metric / 지표) for all dữ liệu (data / 데이터).”** chỉ số (metric / 지표) choice depends on biểu diễn (representation / 표현) and lĩnh vực (domain / 도메인).

**“Large coordinate difference always means large ngữ nghĩa (semantic / 의미적) difference.”** Not if units/scales differ or features encode different structures.

**“Square gốc (root / 루트) is required for every distance comparison.”** Comparing squared distances is equivalent when all quantities nonnegative.

**“Pythagoras is only 2D hình học (geometry / 기하학).”** It generalizes to inner-product spaces and orthogonal projections in arbitrary dimensions.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
