# Manifolds, differential forms và generalized Stokes: calculus không cần global coordinates

> **Mạch đọc:** Chapter này đi sau [Multivariable calculus](./04_multivariable_calculus.md), [Vector calculus](./09_vector_calculus.md), [Topology intro](../03_geometry_trigonometry/08_topology_continuity_connectivity.md) và [Tensor & multilinear algebra](../04_vectors_linear_algebra/08_tensors_and_multilinear_algebra.md). Mục tiêu là giải thích bước abstraction tiếp theo: nhiều spaces curved nhưng locally giống `\mathbb R^n`, nên calculus có thể được xây bằng local coordinates rồi ghép lại một cách coordinate-independent.

Trong multivariable calculus, ta thường làm việc trên open subsets của `\mathbb R^n`. Nhưng nhiều state spaces tự nhiên không phải flat Euclidean space:

```text
surface của sphere
orientation của rigid body
configuration space của robot
constraint surface g(x)=0
space-time geometry
parameter manifold của một model
```

Một sphere nằm trong `\mathbb R^3`, nhưng bản thân sphere là two-dimensional object. Nếu dùng ba coordinates `(x,y,z)` ta mang theo một redundant constraint:

```math
x^2+y^2+z^2=1.
```

**Manifold (đa tạp / 다양체)** formalize idea rằng object có thể curved globally nhưng nhìn Euclidean ở local scale.

---

## 1. Local Euclidean không có nghĩa globally Euclidean

Một smooth `n`-dimensional manifold `M` là space mà quanh mỗi point `p`, ta có neighborhood có thể được coordinatize bằng open subset của `\mathbb R^n`.

Một **chart (좌표계/차트)**:

```math
\varphi:U\subset M\to \mathbb R^n
```

cho local coordinates.

Sphere `S^2` không thể có one global smooth chart giống toàn `\mathbb R^2`, nhưng có thể cover bằng nhiều charts.

Mental model:

```text
Earth is curved globally
but a small city map looks flat locally
```

Manifold calculus là cách làm math mà không nhầm local map với global territory.

---

## 2. Atlas và compatibility

Một collection charts cover manifold gọi là **atlas (아틀라스)**.

Nếu hai charts overlap:

```math
\varphi:U\to\mathbb R^n,
\qquad
\psi:V\to\mathbb R^n,
```

thì transition map

```math
\psi\circ\varphi^{-1}
```

trên overlap phải smooth.

Điều này bảo đảm “smoothness” không phụ thuộc arbitrary coordinate choice.

Ta không muốn một curve smooth trong chart A bỗng trở thành jagged chỉ vì đổi coordinate hợp lệ.

---

## 3. Tangent vector không phải chỉ là arrow nằm trong ambient space

Trên surface embedded trong `\mathbb R^3`, tangent vector có thể hình dung như arrow nằm trong tangent plane.

Nhưng abstract manifold có thể không được embedded sẵn.

Một cách define tangent vector tại `p` là velocity của curve:

```math
\gamma:(-\varepsilon,\varepsilon)\to M,
\qquad
\gamma(0)=p.
```

Two curves represent same tangent vector nếu có same first-order behavior trong local coordinates.

Tangent space:

```math
T_pM
```

là vector space của possible infinitesimal directions tại `p`.

Manifold curved, nhưng mỗi tangent space linear.

Đây là core bridge:

```text
nonlinear global geometry
→ local linear approximation
```

---

## 4. Differential là linear map giữa tangent spaces

Cho smooth map

```math
F:M\to N.
```

Differential tại `p`:

```math
dF_p:T_pM\to T_{F(p)}N
```

là linear map.

Trong Euclidean coordinates, đây chính là Jacobian.

Vì vậy Jacobian không phải chỉ là matrix of partial derivatives; nó là coordinate representation của intrinsic linear map `dF_p`.

Mental model:

> Smooth nonlinear map có first-order shadow là linear map giữa tangent spaces.

Điều này nối trực tiếp với [Linear transformations](../04_vectors_linear_algebra/02_linear_transformations.md) và [Matrix calculus/Jacobian](../04_vectors_linear_algebra/09_matrix_calculus_jacobian_hessian_and_autodiff.md).

---

## 5. Tangent bundle

Nếu gom tangent spaces của mọi points:

```math
TM=\bigsqcup_{p\in M}T_pM,
```

ta được **tangent bundle (접다발)**.

Một **vector field (벡터장)** chọn một tangent vector tại mỗi point:

```math
X(p)\in T_pM.
```

Trong physics, vector field có thể biểu diễn velocity field hoặc force-like local direction.

Trong dynamical systems:

```math
\dot x=X(x)
```

nói trajectory di chuyển theo vector field.

Vì vậy ODE trên manifold là natural extension của ODE trong `\mathbb R^n`.

---

## 6. Cotangent vector và differential forms

Tangent vector là direction.

Một **cotangent vector (공변벡터)** tại `p` là linear functional:

```math
\omega:T_pM\to\mathbb R.
```

Set của chúng là cotangent space:

```math
T_p^*M.
```

Gradient-like objects, differentials `df` và work forms tự nhiên sống ở dual space.

Nếu `f:M→\mathbb R`, differential:

```math
df_p(v)
```

là directional rate of change của `f` theo tangent vector `v`.

---

## 7. 1-form là field của covectors

Một **1-form (1-형식)** `\omega` assign một covector cho mỗi point.

Trong coordinates:

```math
\omega
=P(x,y)dx+Q(x,y)dy.
```

Khi integrate along curve `\gamma`:

```math
\int_\gamma\omega,
```

ta recover familiar line integral.

Work của force field:

```math
\int_C \mathbf F\cdot d\mathbf r
```

có thể được hiểu như integral của 1-form.

Differential forms generalize line/surface/volume integrands trong coordinate-independent language.

---

## 8. k-forms và oriented k-dimensional measurements

Một **k-form (k-형식)** là alternating multilinear object nhận `k` tangent vectors và trả scalar.

Ví dụ 2-form trong `\mathbb R^3` có thể encode oriented area density.

Alternating nghĩa nếu two arguments equal, output zero; swapping arguments đổi sign.

Đây là reason differential forms naturally encode oriented volume elements.

---

## 9. Wedge product

**Wedge product (외적곱)** kết hợp forms:

```math
\alpha\wedge\beta.
```

Với 1-forms:

```math
dx\wedge dy=-dy\wedge dx.
```

và

```math
dx\wedge dx=0.
```

Antisymmetry encode orientation.

Wedge product là exterior-algebra counterpart của building higher-dimensional oriented elements từ one-dimensional covectors.

---

## 10. Exterior derivative

Exterior derivative:

```math
d:\Omega^k(M)\to\Omega^{k+1}(M)
```

generalize gradient, curl-like và divergence-like derivative structures.

Property quan trọng:

```math
d(d\omega)=0.
```

hay

```math
d^2=0.
```

Trong vector-calculus language, identities như

```math
\nabla\times(\nabla f)=0
```

và

```math
\nabla\cdot(\nabla\times F)=0
```

là shadows của same structural fact `d^2=0`.

Điều này là một ví dụ đẹp của abstraction nén nhiều formulas thành một invariant rule.

---

## 11. Pullback: đưa forms ngược qua maps

Cho smooth map

```math
F:M\to N.
```

Một form `\omega` trên `N` có thể được pull back về `M`:

```math
F^*\omega.
```

Pullback là cách đổi variables intrinsic.

Quan trọng:

```math
F^*(d\omega)=d(F^*\omega).
```

Differentiation và pullback commute.

Trong coordinate integration, Jacobian determinant xuất hiện như part của cách volume form transform dưới pullback.

---

## 12. Integration trên manifolds

Để integrate top-degree form trên oriented `n`-manifold, local charts convert problem về integrals trên `\mathbb R^n`, rồi partition of unity/gluing machinery bảo result không phụ thuộc chart.

High-level pattern:

```text
cover manifold by local charts
→ integrate locally
→ glue consistently
→ obtain global integral
```

Đây là local-to-global principle recurring khắp geometry và analysis.

---

## 13. Generalized Stokes theorem

Theorem trung tâm:

```math
\int_M d\omega
=
\int_{\partial M}\omega.
```

Nó generalize nhiều theorems familiar:

```text
Fundamental theorem of calculus
Green's theorem
classical Stokes theorem
Divergence theorem
```

Các theorem này không phải four unrelated tricks. Chúng là manifestations của one structural statement:

> Integral của derivative trong region = integral của original quantity trên boundary.

---

## 14. Fundamental theorem of calculus như Stokes 1D

Cho interval `[a,b]` và function `f`:

```math
\int_a^b df
=f(b)-f(a).
```

Boundary của oriented interval là:

```text
+b endpoint
-a endpoint
```

nên generalized Stokes trở thành exactly FTC.

Điều này giúp nhớ theorem bằng structure chứ không bằng formula list.

---

## 15. Closed và exact forms

Một form `\omega` là **closed (닫힌 형식)** nếu

```math
d\omega=0.
```

Nó là **exact (완전형식)** nếu tồn tại `\eta` sao cho

```math
\omega=d\eta.
```

Vì `d^2=0`:

```text
exact ⇒ closed.
```

Nhưng converse không luôn đúng globally.

Đây là nơi topology xuất hiện trong calculus.

Trên simply connected domains phù hợp, closed 1-forms thường exact. Nhưng trên a domain có hole, có thể có closed form không có global potential.

Local derivative information có thể không glue thành global function vì topology cản trở.

---

## 16. Hole tạo obstruction

Trên punctured plane:

```math
\mathbb R^2\setminus\{0\},
```

form liên quan đến angle có thể locally look like derivative nhưng không có single-valued global angle function.

Integral quanh closed loop encircling origin có thể nonzero.

Đây là conceptual reason circulation có thể detect topology.

Bridge:

```text
local differential equation
+
global topology
→ possibility/impossibility of global potential
```

---

## 17. de Rham cohomology intuition

Cohomology groups measure, roughly, closed forms modulo exact forms:

```math
H^k_{dR}(M)
=
\frac{\ker d:\Omega^k\to\Omega^{k+1}}
{\operatorname{im} d:\Omega^{k-1}\to\Omega^k}.
```

Không cần học computational machinery ngay.

Mental idea:

> Cohomology đo những differential patterns local trông như “không có derivative tiếp theo” nhưng global không thể được viết là derivative của một object lower-degree.

Nó biến holes/topology thành algebraic invariants.

---

## 18. Manifold constraints trong optimization

Nhiều optimization problems có constraint khiến feasible set là manifold.

Ví dụ unit sphere:

```math
\|x\|=1.
```

Ordinary gradient có thể point ra khỏi sphere.

Optimization on manifold dùng tangent-space direction:

```text
compute local gradient-like direction
→ project/retract onto tangent/feasible geometry
→ move along manifold
```

Eigenvector optimization, rotation matrices, low-rank manifolds và robotics orientations đều dẫn tới geometric optimization.

---

## 19. Lie groups: manifold + group

Một **Lie group (리 군)** vừa là smooth manifold vừa là group với smooth multiplication/inverse.

Examples:

```text
SO(2), SO(3) rotations
GL(n) invertible matrices
SE(3) rigid-body poses
```

Lie group kết hợp algebraic symmetry với differential geometry.

Tangent space tại identity tạo Lie algebra, một linearized local model của group.

Trong robotics/control, rotation không nên xử lý như arbitrary 9 matrix entries vì orthogonality constraints phải preserved.

---

## 20. Coordinate singularity không nhất thiết là geometric singularity

Spherical coordinates có problems tại poles. Longitude không defined uniquely ở pole.

Nhưng sphere itself smooth.

Đây là crucial distinction:

```text
coordinate system breaks
≠
object breaks
```

General relativity, robotics và geographic models thường gặp apparent singularities do coordinates.

Manifold language giúp tách representation failure khỏi geometric failure.

---

## 21. Riemannian metric

Một **Riemannian metric (리만 계량)** assign inner product trên mỗi tangent space smoothly.

Nó cho notions:

- length of tangent vectors;
- angle;
- curve length;
- distance;
- gradient;
- volume;
- geodesics.

Euclidean dot product là flat special case.

Curved space có metric thay đổi theo point.

Đây là bridge sang differential geometry, general relativity và information geometry.

---

## 22. Geodesic là local straightness

Geodesic generalize straight line.

Trên sphere, great circles là geodesics.

“Straight” không còn nghĩa coordinates linear; nó nghĩa path có zero intrinsic acceleration theo appropriate connection hoặc locally extremizes length dưới conditions phù hợp.

Đây là recurring pattern:

> Intrinsic definition tốt hơn coordinate picture khi geometry curved.

---

## 23. Differential forms trong physics

Forms fit conservation laws naturally:

```text
0-form → scalar potential
1-form → line-integrated quantity
2-form → flux through surfaces
3-form → volume density
```

Maxwell equations có elegant differential-form formulation, trong đó `d^2=0` và Stokes theorem làm conservation/boundary relations transparent.

Không cần dùng forms để làm basic electromagnetism, nhưng forms cho structural view mạnh khi geometry/topology phức tạp.

---

## 24. Common misconceptions

**“Manifold phải được nhúng vào higher-dimensional Euclidean space.”** Không; embedding giúp visualization nhưng manifold có intrinsic definition.

**“Dimension là số coordinates ambient.”** Sphere `S^2` nằm trong `\mathbb R^3` nhưng intrinsic dimension là 2.

**“Tangent vector luôn là physical arrow trong ambient space.”** Abstract tangent vector tồn tại intrinsic.

**“Jacobian chỉ là matrix derivatives.”** Matrix là coordinate representation của differential.

**“Closed luôn exact.”** Chỉ local hoặc dưới topology conditions phù hợp.

**“Coordinate singularity = physical/geometric singularity.”** Không nhất thiết.

**“Stokes theorem chỉ nói curl trên surface.”** Classical vector Stokes chỉ là một case của generalized Stokes.

---

## 25. Mental model

> Manifold là space có thể curved globally nhưng locally giống Euclidean space. Tangent space linearize geometry tại một point; differential linearize smooth maps; differential forms là coordinate-independent objects để đo/integrate oriented directions; exterior derivative thống nhất grad/curl/div-like operations; generalized Stokes thống nhất calculus trên region và boundary. Topology xuất hiện khi local information không thể glue thành global potential.

---

## 26. Mạch học tiếp

```text
Multivariable calculus
→ Topology
→ Tangent spaces / manifolds
→ Differential forms
→ Generalized Stokes
→ Differential / Riemannian geometry
```

Applied route:

```text
Linear algebra
→ Matrix Lie groups
→ Manifold geometry
→ Robotics / control / physics
```

Đọc tiếp:

- [Dynamical systems, bifurcations và chaos](./16_dynamical_systems_bifurcations_and_chaos.md)
- [Functional analysis: Banach/Hilbert/operators](./14_normed_banach_hilbert_spaces_and_operators.md)
- [Vector calculus](./09_vector_calculus.md)
- [Tensor and multilinear algebra](../04_vectors_linear_algebra/08_tensors_and_multilinear_algebra.md)

## Further reading

- Lynn Loomis, Shlomo Sternberg — *Advanced Calculus*, especially the chapters on calculus on differentiable manifolds and exterior calculus.
