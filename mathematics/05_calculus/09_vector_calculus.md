# Vector calculus: local field behavior và global conservation

Vector calculus nghiên cứu scalar fields và vector fields trên space. Nó là ngôn ngữ tự nhiên của temperature, fluid flow, force, electric field, heat flux và nhiều systems phân bố liên tục.

Core mental chain:

```text
field
→ local derivative
→ directional behavior
→ circulation / flux
→ integral theorem
→ conservation law
```

Điểm quan trọng không phải học riêng `gradient`, `divergence`, `curl`; mà là hiểu mỗi operator trả lời **một câu hỏi hình học khác nhau**.

## 1. Scalar field và vector field

Scalar field:

```math
f(x,y,z)
```

gán một scalar cho mỗi point, ví dụ temperature.

Vector field:

```math
F(x,y,z)=(P,Q,R)
```

gán một vector cho mỗi point, ví dụ fluid velocity.

Field là function có domain là space. Vì vậy vector calculus nối trực tiếp với multivariable functions.

## 2. Gradient: output tăng nhanh nhất về đâu?

Với scalar field `f`:

```math
\nabla f=
\begin{bmatrix}
f_x\\f_y\\f_z
\end{bmatrix}.
```

Directional derivative theo unit vector `u`:

```math
D_uf=\nabla f\cdot u.
```

Cauchy–Schwarz cho:

```math
D_uf\le \|\nabla f\|.
```

Maximum xảy ra khi `u` cùng direction với gradient. Vì vậy:

```text
direction của gradient → steepest local increase
magnitude của gradient → maximum local rate
```

Gradient không phải “mũi tên hướng lên graph”; nó sống trong input space.

## 3. Vì sao gradient vuông góc level set?

Trên level surface:

```math
f(x,y,z)=c.
```

Nếu đi infinitesimally theo tangent direction `v`, first-order change bằng 0:

```math
\nabla f\cdot v=0.
```

Do đó gradient orthogonal với mọi tangent direction, tức là normal vector của level surface.

Đây là connection trực tiếp giữa calculus và geometry of constraints.

## 4. Gradient và optimization

Nếu `f` là objective, gradient chỉ direction local increase. Negative gradient cho steepest descent dưới Euclidean metric.

Constraint surface `g(x)=0` có normal `\nabla g`. Tại constrained optimum, nếu smooth regularity conditions giữ, `\nabla f` phải align với `\nabla g`, dẫn tới Lagrange multiplier condition.

Vector calculus vì vậy đứng ngay dưới constrained optimization.

## 5. Divergence: local source/sink strength

Với

```math
F=(P,Q,R),
```

divergence:

```math
\nabla\cdot F
=
\frac{\partial P}{\partial x}
+
\frac{\partial Q}{\partial y}
+
\frac{\partial R}{\partial z}.
```

Trực giác: lấy một tiny volume quanh point. Nếu nhiều field “đi ra” hơn “đi vào”, divergence positive; nếu net inflow, negative.

Divergence là **net outward flux per unit volume trong limit**.

## 6. Divergence từ local expansion

Ví dụ:

```math
F(x,y,z)=(x,y,z).
```

Khi đó:

```math
\nabla\cdot F=1+1+1=3.
```

Field hướng ra ngoài và magnitude tăng theo distance, nên mọi tiny region có net outward flow.

Ngược lại constant field:

```math
F=(1,0,0)
```

có divergence 0: field đi xuyên region nhưng không được tạo/huỷ bên trong.

## 7. Curl: local circulation tendency

Curl:

```math
\nabla\times F
=
\begin{bmatrix}
R_y-Q_z\\
P_z-R_x\\
Q_x-P_y
\end{bmatrix}.
```

Paddle-wheel intuition hữu ích: đặt tiny wheel vào flow; curl liên quan axis và tendency quay.

Nhưng curl không đơn giản bằng “field nhìn xoáy”. Nó là differential measure của circulation density.

## 8. Worked example: rigid rotation

Xét 2D rotation field embedded in 3D:

```math
F(x,y,z)=(-y,x,0).
```

Divergence:

```math
\nabla\cdot F=0.
```

Curl:

```math
\nabla\times F=(0,0,2).
```

Field không expand locally nhưng có rotational tendency. Đây là ví dụ rõ để tách divergence khỏi curl.

## 9. Conservative field và potential

Nếu

```math
F=\nabla\phi,
```

thì `F` là gradient field/conservative field.

Line integral từ `A` tới `B`:

```math
\int_C F\cdot dr
=
\phi(B)-\phi(A)
```

trong suitable domain.

Do đó work không phụ thuộc path; chỉ endpoints matter.

Trong mechanics, potential energy cho conservative force là manifestation của structure này.

## 10. Curl zero có đủ để conservative không?

Ta luôn có:

```math
\nabla\times(\nabla\phi)=0.
```

Nhưng reverse implication cần domain assumptions như simply connectedness.

Một field có curl zero trên domain có hole vẫn có thể có nonzero circulation quanh hole. Đây là ví dụ quan trọng: **local condition không luôn imply global structure**.

## 11. Line integral: accumulate field along a path

Curve parameterization:

```math
r(t),\quad a\le t\le b.
```

Vector line integral:

```math
\int_C F\cdot dr
=
\int_a^b F(r(t))\cdot r'(t)\,dt.
```

Dot product chỉ lấy component của field theo tangent direction.

Trong mechanics:

```math
W=\int_C F\cdot dr
```

là work along path.

## 12. Scalar line integral

Một scalar field cũng có thể tích phân dọc curve:

```math
\int_C f\,ds.
```

Ví dụ wire có linear density `\rho`; mass:

```math
M=\int_C \rho\,ds.
```

Điều này nhắc rằng “line integral” không chỉ có một form.

## 13. Surface integral và flux

Flux qua oriented surface:

```math
\iint_S F\cdot n\,dS.
```

`n` là unit normal. Dot product chọn normal component: field tangent surface không góp flux xuyên surface.

Đổi orientation của normal thì flux đổi dấu.

## 14. Divergence theorem: local source → global flux

```math
\iiint_V \nabla\cdot F\,dV
=
\iint_{\partial V}F\cdot n\,dS.
```

Interpretation:

> Tổng net source density bên trong volume bằng net outward flow qua boundary.

Đây không chỉ là integration trick. Nó là mathematical form của conservation reasoning.

## 15. Continuity equation

Nếu `\rho(x,t)` là density và `J` là flux, local conservation thường có form:

```math
\frac{\partial \rho}{\partial t}
+
\nabla\cdot J=0.
```

Nếu density giảm tại point, mass/charge/probability phải flow ra; nếu tăng, phải flow vào hoặc source term tồn tại.

Đây là một trong các equations sâu nhất nối divergence với Physics.

## 16. Stokes' theorem: local curl → boundary circulation

```math
\iint_S (\nabla\times F)\cdot n\,dS
=
\oint_{\partial S}F\cdot dr.
```

Left side tích lũy local rotation trên surface; right side đo circulation quanh boundary.

Stokes nói rằng internal rotational tendency account cho boundary circulation.

## 17. Green's theorem trong 2D

Green's theorem là 2D version nối line integral quanh boundary với area integral bên trong.

Một form:

```math
\oint_C P\,dx+Q\,dy
=
\iint_D
\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dA.
```

Nó là bridge dễ thấy trước generalized Stokes theorem.

## 18. Fundamental theorem pattern

Fundamental Theorem of Calculus:

```math
\int_a^b f'(x)\,dx=f(b)-f(a).
```

Divergence theorem:

```text
integral of divergence inside
= flux on boundary
```

Stokes theorem:

```text
integral of curl on surface
= circulation on boundary
```

Unified mental model:

> integrate a derivative over a region → recover original object on the boundary.

Generalized Stokes theorem formalizes toàn bộ pattern này.

## 19. Coordinate systems và Jacobian

Vector calculus thường dễ hơn nếu dùng coordinates phù hợp: Cartesian, cylindrical, spherical.

Nhưng operators `\nabla`, divergence, curl không giữ cùng coordinate formula naïvely; scale factors/Jacobian matter.

Ví dụ spherical volume element:

```math
dV=r^2\sin\theta\,dr\,d\theta\,d\phi.
```

Factor `r^2\sin\theta` đến từ local volume scaling của coordinate transform.

## 20. Maxwell equations connection

Electromagnetism dùng divergence/curl trực tiếp. Ví dụ conceptual forms:

```text
Gauss law → divergence của electric field liên hệ charge density
Faraday law → curl của electric field liên hệ changing magnetic field
```

Điểm quan trọng không phải memorize physics constants ở chapter này, mà thấy vector calculus operators được chọn vì chúng encode local source và circulation structure.

## 21. Fluid dynamics connection

Velocity field `v(x,t)`:

```math
\nabla\cdot v=0
```

thường biểu diễn incompressibility trong appropriate model.

Vorticity:

```math
\omega=\nabla\times v.
```

mô tả rotational structure của flow.

Nhưng zero divergence không nghĩa zero velocity; zero curl không nghĩa no motion.

## 22. AI và scalar fields

Loss function trong machine learning là high-dimensional scalar field trên parameter space.

Gradient:

```math
\nabla L
```

cho local sensitivity; Hessian cho curvature. Dù không visualizable ở millions dimensions, geometry vẫn là same differential structure.

Vector calculus intuition vì vậy vẫn relevant cho optimization/AI.

## Worked example: flux của radial field

Xét:

```math
F(x)=\frac{x}{\|x\|^3}
```

trên `\mathbb R^3\setminus\{0\}`.

Field radial và magnitude scale `1/r^2`. Flux qua sphere radius `R`:

```math
F\cdot n=\frac1{R^2},
```

surface area `4\pi R^2`, nên total flux:

```math
4\pi.
```

Nó independent of `R`. Source behavior concentrated at excluded origin cho thấy vì sao domain/singularity matter khi dùng divergence theorem.

## Knowledge Connection

```text
multivariable derivative
→ gradient / Jacobian
→ field geometry
→ line / surface integrals
→ divergence / curl
→ conservation laws
→ PDE / Physics / control
```

Projection và dot product từ Linear Algebra xuất hiện trong directional derivative, work và flux. Topology xuất hiện trong distinction local curl-free vs global conservative. Differential equations/PDE dùng các operators này để model dynamics.

## Mental Model

> Gradient đo local uphill direction của scalar field. Divergence đo local creation/expansion of flow. Curl đo local circulation tendency. Integral theorems biến local derivatives thành global boundary statements.

## Common Misconceptions

Gradient là vector trong input space, không phải graph slope line. Divergence không phải magnitude. Curl zero không luôn imply global potential nếu domain có holes. Flux phụ thuộc surface orientation. Stokes/divergence theorem cần regularity và domain assumptions; không nên apply qua singularities mà không kiểm tra.
