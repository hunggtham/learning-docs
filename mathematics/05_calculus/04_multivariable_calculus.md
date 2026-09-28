# Giải tích nhiều biến: từ nhiều partial derivatives đến cục bộ (local / 로컬) tuyến tính (linear / 선형) maps

> **Mạch đọc:** Đọc **Giải tích nhiều biến: từ nhiều partial derivatives đến cục bộ (local / 로컬) tuyến tính (linear / 선형) maps** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Partial derivative: hỏi từng coordinate một** sang **độ dốc (gradient / 기울기): gói các coordinate sensitivities thành một véc-tơ (vector / 벡터)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Giải tích nhiều biến (multivariable calculus / 다변수 미적분학) bắt đầu khi một đầu ra (output / 출력) phụ thuộc đồng thời vào nhiều inputs. Temperature phụ thuộc vị trí trong không gian, profit phụ thuộc price/chi phí (cost / 비용)/demand, neural-network mất mát (loss / 손실) phụ thuộc hàng triệu parameters. Khi đó một slope duy nhất không đủ; ta cần mô tả **sensitivity theo mọi direction**.

Intuition quan trọng nhất là: derivative trong nhiều biến không chỉ là một danh sách (list / 목록) partial derivatives. Nó là **best cục bộ (local / 로컬) tuyến tính (linear / 선형) transformation** mô tả cách small đầu vào (input / 입력) perturbation biến thành đầu ra (output / 출력) perturbation.

## Partial derivative: hỏi từng coordinate một

Với

```math
f(x,y),
```

partial derivative theo `x` giữ `y` fixed:

```math
\frac{\partial f}{\partial x}.
```

Tương tự cho `y`.

Ví dụ

```math
f(x,y)=x^2y+3y.
```

Ta có

```math
\frac{\partial f}{\partial x}=2xy,
```

```math
\frac{\partial f}{\partial y}=x^2+3.
```

Mỗi partial derivative là sensitivity theo một coordinate axis. Nhưng real perturbation thường không đi đúng theo axis; vì vậy ta cần độ dốc (gradient / 기울기) và directional derivative.

## Độ dốc (gradient / 기울기): gói các coordinate sensitivities thành một véc-tơ (vector / 벡터)

Với scalar-valued hàm (function / 함수)

```math
f:\mathbb R^n\to\mathbb R,
```

Độ dốc (gradient / 기울기) là

```math
\nabla f(x)
=
\begin{bmatrix}
\partial f/\partial x_1\\
\vdots\\
\partial f/\partial x_n
\end{bmatrix}.
```

Nếu perturb đầu vào (input / 입력) bởi small véc-tơ (vector / 벡터) `\Delta x`, first-order thay đổi (change / 변경) là

```math
\Delta f
\approx
\nabla f(x)^T\Delta x.
```

Đây là multivariable phiên bản (version / 버전) của

```math
\Delta y\approx f'(x)\Delta x.
```

## Vì sao độ dốc (gradient / 기울기) chỉ hướng steepest ascent?

Directional derivative theo đơn vị (unit / 단위) véc-tơ (vector / 벡터) `u`:

```math
D_uf(x)=\nabla f(x)\cdot u.
```

Theo Cauchy–Schwarz:

```math
\nabla f\cdot u
\le
\|\nabla f\|\|u\|.
```

Với `\|u\|=1`, maximum đạt khi `u` cùng direction với độ dốc (gradient / 기울기). Vì vậy độ dốc (gradient / 기울기) là direction tăng nhanh nhất theo Euclidean chỉ số (metric / 지표); negative độ dốc (gradient / 기울기) là steepest cục bộ (local / 로컬) decrease.

Đây là proof idea của độ dốc (gradient / 기울기) descent hình học (geometry / 기하학).

## Mức (level / 수준) sets và vì sao độ dốc (gradient / 기울기) vuông góc contour

Mức (level / 수준) set là set points thỏa

```math
f(x)=c.
```

Nếu ta move tangent theo mức (level / 수준) set, giá trị (value / 값) của `f` không đổi first-order, nên directional derivative bằng zero:

```math
\nabla f\cdot u=0.
```

Do đó độ dốc (gradient / 기울기) perpendicular với tangent directions của mức (level / 수준) set.

Trong 2D, độ dốc (gradient / 기울기) normal với contour line. Trong 3D, độ dốc (gradient / 기울기) normal với mức (level / 수준) surface.

Đây là foundation của Lagrange multipliers: tại constrained optimum, mục tiêu (objective / 목표) độ dốc (gradient / 기울기) phải align với ràng buộc (constraint / 제약조건) normal nếu không còn feasible first-order improvement direction.

## Worked example — độ dốc (gradient / 기울기) của quadratic bowl

Cho

```math
f(x,y)=x^2+4y^2.
```

Độ dốc (gradient / 기울기):

```math
\nabla f=(2x,8y).
```

Tại `(1,1)`:

```math
\nabla f(1,1)=(2,8).
```

Hàm (function / 함수) tăng mạnh hơn theo `y` direction vì curvature/scaling lớn hơn. Negative độ dốc (gradient / 기울기) `(-2,-8)` là steepest Euclidean descent direction cục bộ (local / 로컬).

Nếu features `x,y` có units/scales rất khác nhau, hình học (geometry / 기하학) của “steepest” cũng bị ảnh hưởng. Đây là lý do tính năng (feature / 기능) scaling và preconditioning matter trong tối ưu hóa (optimization / 최적화).

## Jacobian: derivative của vector-valued hàm (function / 함수)

Nếu

```math
F:\mathbb R^n\to\mathbb R^m,
```

thì derivative tại điểm (point / 지점) là ma trận (matrix / 행렬) Jacobian:

```math
J_F(x)
=
\begin{bmatrix}
\partial F_1/\partial x_1&\cdots&\partial F_1/\partial x_n\\
\vdots&\ddots&\vdots\\
\partial F_m/\partial x_1&\cdots&\partial F_m/\partial x_n
\end{bmatrix}.
```

Cục bộ (local / 로컬) linearization:

```math
F(x+\Delta x)
\approx
F(x)+J_F(x)\Delta x.
```

Đây là statement trung tâm: Jacobian là cục bộ (local / 로컬) tuyến tính (linear / 선형) map từ đầu vào (input / 입력) perturbations sang đầu ra (output / 출력) perturbations.

## Chuỗi (chain / 사슬) quy tắc (rule / 규칙) trở thành ma trận (matrix / 행렬) composition

Nếu

```math
F=G\circ H,
```

thì

```math
J_F(x)
=
J_G(H(x))J_H(x).
```

Meaning: cục bộ (local / 로컬) perturbation đi qua `H` trước, rồi qua `G`. phép nhân ma trận (matrix multiplication / 행렬 곱셈) xuất hiện vì cục bộ (local / 로컬) tuyến tính (linear / 선형) maps compose exactly like tuyến tính (linear / 선형) transformations.

Backpropagation là efficient organization của chuỗi (chain / 사슬) quy tắc (rule / 규칙) để tránh forming huge full Jacobians không cần thiết.

## Độ dốc (gradient / 기울기), Jacobian và matrix-calculus conventions

Độ dốc (gradient / 기울기) có thể được viết row hoặc column tùy convention. Trong thư viện (library / 라이브러리) này ưu tiên độ dốc (gradient / 기울기) column véc-tơ (vector / 벡터) khi nói hình học (geometry / 기하학):

```math
\nabla f\in\mathbb R^n.
```

Khi đọc papers/frameworks, phải check convention. Nhiều bugs notation đến từ assume shapes mà không verify.

## Hessian: curvature theo nhiều directions

Với scalar `f`, Hessian là ma trận (matrix / 행렬) second derivatives:

```math
H_f(x)
=
\left[
\frac{\partial^2 f}{\partial x_i\partial x_j}
\right].
```

Second-order cục bộ (local / 로컬) mô hình (model / 모델):

```math
f(x+\Delta)
\approx
f(x)
+
\nabla f(x)^T\Delta
+
\frac12\Delta^T H_f(x)\Delta.
```

Độ dốc (gradient / 기울기) cho tilt; Hessian cho cục bộ (local / 로컬) curvature.

Nếu Hessian positive definite tại a trọng yếu (critical / 중요) điểm (point / 지점), quadratic term positive mọi nonzero direction, nên có strict cục bộ (local / 로컬) minimum dưới smoothness phù hợp.

Nếu Hessian indefinite, có directions up và down: saddle điểm (point / 지점).

## Eigenvalues của Hessian và tối ưu hóa (optimization / 최적화) hình học (geometry / 기하학)

Hessian symmetric khi mixed partials behave well. Its eigenvectors give principal curvature directions; eigenvalues give curvature strengths.

Nếu eigenvalues vary by orders of magnitude, mất mát (loss / 손실) landscape elongated. độ dốc (gradient / 기울기) descent phải dùng học tập (learning / 학습) tỷ lệ (rate / 비율) nhỏ enough cho steep direction, nên progress theo flat direction chậm. Đây là condition-number intuition trong tối ưu hóa (optimization / 최적화).

## Constrained tối ưu hóa (optimization / 최적화) và Lagrange multipliers

Muốn optimize `f(x)` dưới equality ràng buộc (constraint / 제약조건)

```math
g(x)=c,
```

tại smooth interior constrained optimum, feasible tangent directions nằm orthogonal với `\nabla g`. Để không còn first-order feasible improvement, `\nabla f` cũng phải normal với tangent không gian (space / 공간):

```math
\nabla f=\lambda\nabla g.
```

Lagrange multiplier không phải trick algebra; nó encode alignment of normals.

## Multiple integrals: accumulation trong nhiều dimensions

Double integral

```math
\iint_R f(x,y)\,dA
```

accumulates density over area. Triple integral accumulates over volume.

Nếu `f` là mass density kg/m², then integral over area gives mass kg. Units tiếp tục là sanity check.

## Thay đổi (change / 변경) of variables và Jacobian determinant

Khi đổi coordinates, infinitesimal area/volume bị quy mô (scale / 규모). Nếu

```math
x=T(u),
```

thì cục bộ (local / 로컬) volume scaling là

```math
|\det J_T(u)|.
```

Do đó

```math
\int f(x)\,dx
=
\int f(T(u))|\det J_T(u)|\,du.
```

Polar coordinates:

```math
x=r\cos\theta,
\qquad
y=r\sin\theta.
```

Jacobian determinant là `r`, nên

```math
dA=r\,dr\,d\theta.
```

Factor `r` không phải formula cần nhớ riêng; nó là cục bộ (local / 로컬) area expansion khi radial coordinate tăng.

## Xác suất (probability / 확률) liên kết (connection / 연결) — transformations của random variables

Nếu random véc-tơ (vector / 벡터) `X` được transform thành `Y=T(X)`, density transformation cũng cần Jacobian determinant. Same hình học (geometry / 기하학) xuất hiện trong xác suất (probability / 확률), normalizing flows và Bayesian computation.

Đây là liên kết (connection / 연결) sâu: change-of-variables theorem trong tích hợp (integration / 통합) và density transformation là cùng mathematical cấu trúc (structure / 구조).

## Physics liên kết (connection / 연결) — scalar và véc-tơ (vector / 벡터) fields

Temperature `T(x,y,z)` là scalar trường dữ liệu (field / 필드); độ dốc (gradient / 기울기) chỉ direction temperature tăng nhanh nhất.

Velocity trường dữ liệu (field / 필드) `v(x,y,z)` là véc-tơ (vector / 벡터) trường dữ liệu (field / 필드); its Jacobian contains cục bộ (local / 로컬) deformation thông tin (information / 정보). Divergence và curl được xây từ derivatives của véc-tơ (vector / 벡터) fields và nối sang fluid dynamics, electromagnetism và véc-tơ (vector / 벡터) calculus.

## AI liên kết (connection / 연결) — mất mát (loss / 손실) landscapes và backpropagation

Mất mát (loss / 손실)

```math
L(\theta_1,\ldots,\theta_n)
```

là scalar hàm (function / 함수) trên parameter không gian (space / 공간). độ dốc (gradient / 기울기) gives cục bộ (local / 로컬) first-order sensitivity. Hessian captures curvature but full Hessian quá lớn cho hiện đại (modern / 현대적) networks, nên algorithms dùng Hessian-vector products, approximations hoặc adaptive first-order methods.

Automatic differentiation computes chính xác (exact / 정확한) chain-rule derivatives của implemented computation đồ thị (graph / 그래프) up to floating-point effects; nó không phải numerical finite differencing.

## Finance liên kết (connection / 연결) — multi-factor sensitivity

Portfolio giá trị (value / 값) có thể depend on rates, FX, volatility, equity levels. độ dốc (gradient / 기울기) véc-tơ (vector / 벡터) captures first-order exposures; Hessian captures cross-effects và convexity-like second-order risks.

Nhưng cục bộ (local / 로컬) Greeks/sensitivities không thay thế scenario phân tích (analysis / 분석) cho large shocks, vì Taylor approximation có validity phạm vi (range / 범위).

## Differentiability không chỉ là “mọi partial derivative tồn tại”

Một hàm (function / 함수) có thể có all partial derivatives tại điểm (point / 지점) nhưng vẫn không differentiable ở đó. Differentiability yêu cầu tồn tại một single tuyến tính (linear / 선형) map approximation cho **mọi small directions đồng thời**.

Đây là lý do Jacobian/local-linear-map viewpoint mạnh hơn việc coi multivariable calculus là “take partials one by one”.

## Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes

Độ dốc (gradient / 기울기) depends on coordinate scaling and chỉ số (metric / 지표). Rescaling a variable changes numerical độ dốc (gradient / 기울기) components dù underlying vật lý (physical / 물리적) bài toán (problem / 문제) same. tối ưu hóa (optimization / 최적화) methods often need normalization/preconditioning.

Hessian-based classification cần smoothness và cục bộ (local / 로컬) ngữ cảnh (context / 맥락); positive semidefinite but not definite can be inconclusive.

Jacobian linearization chỉ accurate locally. Large perturbations require nonlinear terms or repeated re-linearization.

## Mô hình tư duy (mental model / 사고 모델)

> Multivariable calculus asks how a small véc-tơ (vector / 벡터) perturbation flows through a hệ thống (system / 시스템). độ dốc (gradient / 기울기) is the scalar-output sensitivity véc-tơ (vector / 벡터); Jacobian is the cục bộ (local / 로컬) tuyến tính (linear / 선형) transformation for véc-tơ (vector / 벡터) outputs; Hessian is the curvature operator describing how first-order sensitivity itself changes. tích hợp (integration / 통합) and Jacobian determinants describe how small pieces of area/volume transform and accumulate.

## Dùng chung (common / 공통) Misconceptions

**“độ dốc (gradient / 기울기) là chỉ hướng hàm (function / 함수) lớn nhất globally.”** Nó chỉ steepest cục bộ (local / 로컬) direction under the chosen chỉ số (metric / 지표).

**“Có partial derivatives là differentiable.”** Không đủ; cần a coherent cục bộ (local / 로컬) tuyến tính (linear / 선형) approximation.

**“Jacobian determinant chỉ là correction factor để nhớ.”** Nó là cục bộ (local / 로컬) volume scaling của coordinate transformation.

**“Hessian positive semidefinite luôn nghĩa strict minimum.”** Không; semidefinite can be inconclusive without additional cấu trúc (structure / 구조).

**“Backpropagation là một numerical approximation.”** Nó là chuỗi (chain / 사슬) quy tắc (rule / 규칙)/automatic differentiation trên computation đồ thị (graph / 그래프), khác finite differences.

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 limits and continuity](./00_limits_and_continuity.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
