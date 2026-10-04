# Normed, Banach và Hilbert spaces: khi linear algebra chuyển sang không gian hàm

> **Mạch đọc:** Chapter này nối [Vector spaces, basis và dimension](../04_vectors_linear_algebra/03_vector_spaces_basis_dimension.md), [Inner product, orthogonality và projection](../04_vectors_linear_algebra/06_inner_product_orthogonality_and_projection.md), [Metric spaces, uniform convergence và measure](./13_metric_spaces_uniform_convergence_and_measure_intro.md) và [Fourier analysis](../09_connections/05_fourier_signals_and_frequency.md). Mục tiêu là giải thích vì sao linear algebra không dừng ở finite-dimensional vectors: trong analysis, “vectors” thường là functions.

Trong `\mathbb R^n`, ta quen với vector, norm, dot product, basis và linear transformation. Nhưng nhiều problems tự nhiên có unknown không phải một finite vector mà là **một function**:

```text
unknown temperature profile T(x)
unknown signal f(t)
unknown wave ψ(x)
unknown probability density p(x)
unknown solution y(t) của ODE/PDE
```

Nếu functions được xem như vectors, ta có thể hỏi lại các câu linear algebra quen thuộc:

```text
distance giữa hai functions là gì?
orthogonal nghĩa là gì?
projection là gì?
linear transformation trên functions là gì?
sequence of approximate functions có converge không?
```

**Functional analysis (hàm giải tích / 함수해석학)** là nơi linear algebra, topology và analysis gặp nhau để trả lời các câu đó.

---

## 1. Normed vector space

Một **không gian vector có chuẩn (normed vector space / 노름 벡터공간)** là vector space `V` với norm

```math
\|\cdot\|:V\to[0,\infty)
```

thỏa:

```math
\|x\|\ge0,
\qquad
\|x\|=0\iff x=0,
```

```math
\|\alpha x\|=|\alpha|\|x\|,
```

```math
\|x+y\|\le\|x\|+\|y\|.
```

Norm đo magnitude.

Từ norm ta có metric:

```math
d(x,y)=\|x-y\|.
```

Vì vậy normed space tự động là metric space.

Hierarchy:

```text
vector space
    + norm
→ normed vector space
    + completeness
→ Banach space
```

---

## 2. Nhiều norms mô tả nhiều notions of error

Trong `\mathbb R^n`:

```math
\|x\|_1=\sum_i|x_i|,
```

```math
\|x\|_2=\left(\sum_i|x_i|^2\right)^{1/2},
```

```math
\|x\|_\infty=\max_i|x_i|.
```

Trong finite dimension, các norms này tạo cùng notion of convergence, nhưng geometry khác nhau.

Trong infinite-dimensional function spaces, lựa chọn norm còn quan trọng hơn.

Ví dụ với function `f`:

```math
\|f\|_\infty=\sup_x|f(x)|
```

quan tâm worst-case error, còn

```math
\|f\|_2
=
\left(\int |f(x)|^2dx\right)^{1/2}
```

quan tâm mean-square/energy-like error.

Hai approximations có thể rất gần trong `L^2` nhưng không gần trong sup norm nếu error lớn trên một vùng rất nhỏ.

Mental rule:

> “Approximation tốt” không có nghĩa gì cho tới khi ta nói tốt theo norm nào.

---

## 3. Banach space = complete normed space

Một **Banach space (바나흐 공간)** là normed vector space complete dưới metric do norm sinh ra.

Tức mọi Cauchy sequence:

```math
\forall\varepsilon>0,
\exists N:
m,n\ge N
\Rightarrow
\|x_m-x_n\|<\varepsilon
```

phải converge tới một element vẫn nằm trong space.

Completeness quan trọng vì iterative methods thường chỉ cho ta một sequence approximations.

Nếu space không complete, approximations có thể converge “ra ngoài” space.

---

## 4. Ví dụ: C([a,b]) với sup norm

Set các continuous functions trên `[a,b]`:

```math
C([a,b])
```

với norm

```math
\|f\|_\infty
=
\max_{x\in[a,b]}|f(x)|
```

là Banach space.

Nếu sequence continuous functions là Cauchy theo sup norm, nó converge uniformly tới một continuous function.

Điều này nối completeness với theorem:

> uniform limit của continuous functions vẫn continuous.

Vì vậy Banach-space language đóng gói nhiều facts của elementary analysis thành một structural statement.

---

## 5. Lp spaces

Trên measure space phù hợp:

```math
\|f\|_p
=
\left(\int |f|^p d\mu\right)^{1/p},
\qquad 1\le p<\infty.
```

`L^p` gồm equivalence classes of functions với finite `p`-norm, trong đó functions khác nhau chỉ trên measure-zero set được xem là cùng element.

Các `L^p` spaces là Banach spaces.

Một vài interpretations:

```text
L1     → total absolute mass/error
L2     → energy / mean-square geometry
L∞     → worst-case magnitude
```

Không có một norm “đúng nhất”; norm phải match question.

---

## 6. Inner-product space thêm notion of angle

Một **inner product (내적)** trên real vector space là map

```math
\langle x,y\rangle
```

thỏa linearity, symmetry và positive definiteness.

Nó sinh norm:

```math
\|x\|
=
\sqrt{\langle x,x\rangle}.
```

Nhưng không phải mọi norm đến từ inner product.

Ví dụ `L^2` có natural inner product:

```math
\langle f,g\rangle
=
\int f(x)g(x)\,d\mu(x).
```

Do đó ta có geometry cho functions:

```text
angle
orthogonality
projection
Pythagorean theorem
```

---

## 7. Hilbert space = complete inner-product space

Một **Hilbert space (힐베르트 공간)** là inner-product space complete theo norm do inner product sinh ra.

Finite-dimensional Euclidean space `\mathbb R^n` là Hilbert space.

`L^2` cũng là Hilbert space.

Mental model:

> Hilbert space là Euclidean geometry được mở rộng sang infinite dimensions, miễn ta giữ inner product và completeness.

Đây là reason Fourier series, least squares, quantum mechanics và PDE có cùng geometric language.

---

## 8. Orthogonality của functions

Functions `f,g` orthogonal nếu

```math
\langle f,g\rangle=0.
```

Trên interval phù hợp:

```math
\int \sin(nx)\sin(mx)\,dx=0
```

khi `n≠m` dưới standard boundary/normalization conditions.

Sine/cosine modes hoạt động như perpendicular coordinate axes.

Fourier coefficients vì vậy là projection coefficients:

```math
c_k
=
\frac{\langle f,\phi_k\rangle}
{\langle\phi_k,\phi_k\rangle}.
```

Fourier series không chỉ là trig identity machinery; nó là linear algebra trong function space.

---

## 9. Projection theorem

Trong Hilbert space, nếu `M` là suitable closed subspace, mỗi `x` có nearest point `P_Mx` trong `M`.

Residual:

```math
x-P_Mx
```

orthogonal với `M`.

Đây là infinite-dimensional extension của least squares.

Pattern chung:

```text
choose model subspace M
→ project target x onto M
→ residual orthogonal to all allowed directions
```

Regression, Fourier approximation, Galerkin methods và finite-element methods đều dùng variants của pattern này.

---

## 10. Orthonormal basis trong infinite dimensions

Trong `\mathbb R^n`, basis hữu hạn cho unique coordinate vector.

Trong Hilbert space, orthonormal basis có thể countably infinite và expansion thường là limit:

```math
f
=
\sum_{k=1}^{\infty}c_ke_k.
```

Convergence phải được hiểu theo norm phù hợp.

Ví dụ Fourier series có thể converge trong `L^2` ngay cả khi pointwise behavior phức tạp hơn.

Điều này nhắc lại distinction:

```text
pointwise convergence
uniform convergence
L2 convergence
```

không interchangeable.

---

## 11. Parseval identity

Với complete orthonormal system:

```math
\|f\|^2
=
\sum_k|\langle f,e_k\rangle|^2.
```

Đây là infinite-dimensional Pythagorean theorem.

Signal energy trong time domain bằng total squared coordinate magnitudes trong orthonormal frequency basis.

Đó là geometric core đằng sau nhiều energy-conservation identities trong Fourier analysis.

---

## 12. Linear operator

Một **linear operator (선형 연산자)** là linear map giữa function/vector spaces:

```math
T:X\to Y.
```

Ví dụ:

```math
(Tf)(x)=\int K(x,y)f(y)dy
```

là integral operator.

Derivative:

```math
Df=f'
```

cũng là linear operator trên domain phù hợp.

Matrix là finite-dimensional representation của linear operator. Functional analysis nghiên cứu operators khi domain/codomain có thể infinite-dimensional.

---

## 13. Bounded linear operator = continuous linear operator

Một linear operator `T:X→Y` giữa normed spaces gọi là bounded nếu tồn tại `C` sao cho

```math
\|Tx\|_Y
\le C\|x\|_X
```

cho mọi `x`.

Operator norm:

```math
\|T\|
=
\sup_{x\ne0}
\frac{\|Tx\|}{\|x\|}.
```

Với linear operators, boundedness tương đương continuity.

Interpretation:

> small input perturbation không thể bị operator amplify vô hạn relative to input norm.

Điều này nối trực tiếp functional analysis với numerical stability.

---

## 14. Derivative operator có thể unbounded

Xét high-frequency functions:

```math
f_n(x)=\frac{\sin(nx)}{n}.
```

Sup magnitude:

```math
\|f_n\|_\infty=\frac1n\to0.
```

nhưng derivative:

```math
f_n'(x)=\cos(nx)
```

có sup norm `1`.

Với different choices of spaces/norms, differentiation không phải bounded operator.

Đây là reason PDE/quantum theory phải cực kỳ cẩn thận về **domain của operator**.

Một formula như `Tf` chưa đủ; cần nói `f` được phép nằm trong space nào.

---

## 15. Kernel, range và invertibility trở lại

Như finite linear algebra:

```math
\ker T=\{x:Tx=0\},
```

```math
\operatorname{Range}(T)=\{Tx:x\in X\}.
```

Nhưng infinite-dimensional setting thêm subtleties:

- range có thể không closed;
- inverse có thể tồn tại algebraically nhưng không continuous;
- compactness không còn automatic trên bounded sets;
- spectrum phức tạp hơn finite eigenvalue list.

Do đó intuition từ matrices rất hữu ích nhưng không được copy blindly.

---

## 16. Spectrum tổng quát hóa eigenvalues

Trong finite dimensions, `λ` là eigenvalue nếu

```math
T-\lambda I
```

không invertible.

Trong functional analysis, **spectrum (스펙트럼)** của operator gồm các `λ` mà

```math
T-\lambda I
```

không có bounded inverse phù hợp.

Spectrum có thể chứa values không có ordinary eigenvector.

Đây là conceptual extension từ matrix eigenanalysis sang differential/integral operators.

Trong PDE và quantum mechanics, spectrum thường encode natural frequencies, energy levels hoặc decay modes.

---

## 17. Compact operators gần finite-dimensional behavior hơn

Một **compact operator (콤팩트 연산자)** maps bounded sets thành sets có compact-like subsequence behavior.

Compact operators trên infinite-dimensional Hilbert spaces có spectral theory gần matrices hơn nhiều general operators.

Integral operators với sufficiently regular kernels thường là important examples.

Mental idea:

> Compactness là một cách lấy lại một phần “finite-dimensional discipline” trong infinite-dimensional world.

---

## 18. Riesz representation: linear functionals như inner products

Một **linear functional (선형 범함수)** là linear map

```math
\ell:H\to\mathbb R
```

hoặc `\mathbb C`.

Trong Hilbert space, every bounded linear functional có form

```math
\ell(x)=\langle x,y\rangle
```

cho unique `y`.

Đây là Riesz representation theorem.

Nó nói dual object tưởng như abstract có thể được represent bằng một vector trong same Hilbert space.

Trong finite-dimensional Euclidean space, đây là familiar fact rằng linear functional `a^Tx` được represent bởi vector `a`.

---

## 19. Fixed-point theorem và Banach spaces

Nếu complete metric space có contraction

```math
d(Tx,Ty)\le qd(x,y),
\qquad 0<q<1,
```

thì Banach fixed-point theorem bảo đảm unique fixed point và iteration converge.

Trong function spaces, ta có thể biến differential/integral equation thành fixed-point problem:

```math
f=T(f).
```

Sau đó prove `T` contraction.

Đây là một route rất phổ biến để prove existence/uniqueness của solutions.

Functional analysis vì vậy không chỉ abstraction; nó cung cấp theorem-level machinery cho ODE/PDE.

---

## 20. Weak convergence

Strong/norm convergence:

```math
\|x_n-x\|\to0.
```

**Weak convergence (약수렴)** roughly yêu cầu mọi bounded linear functional thấy convergence:

```math
\ell(x_n)\to\ell(x).
```

Weak convergence yếu hơn norm convergence.

Tại sao cần?

Trong optimization/PDE, bounded sequences có thể không có strongly convergent subsequence nhưng có weakly convergent subsequence dưới suitable conditions.

Weak topology cho phép lấy limits khi strong convergence quá nhiều để đòi hỏi.

---

## 21. Optimization trong Hilbert space

Finite-dimensional gradient optimization có geometry:

```math
x_{k+1}=x_k-\eta\nabla f(x_k).
```

Trong function space, decision variable có thể là whole function/control trajectory.

Derivative trở thành functional derivative hoặc Fréchet derivative; gradient phụ thuộc chosen inner product.

Điều này dẫn tới:

- calculus of variations;
- optimal control;
- inverse problems;
- regularization;
- PDE-constrained optimization.

Conceptual bridge:

```text
vector optimization
→ function-space optimization
```

---

## 22. Regularization là geometry + stability

Ill-posed inverse problem có thể amplify small data noise thành huge solution changes.

Regularization thêm preference như smoothness hoặc small norm:

```math
\min_f
\|Af-b\|^2
+\lambda\|f\|^2.
```

Đây là same structure như ridge regression, nhưng `f` có thể là function và `A` là operator.

Functional-analysis viewpoint cho thấy regularization không chỉ là ML trick; nó là stability mechanism cho inverse operators.

---

## 23. Common misconceptions

**“Banach space chỉ là vector space rất lớn.”** Không. Completeness dưới specific norm là essential structure.

**“Hilbert = Banach.”** Mọi Hilbert space là Banach dưới induced norm, nhưng không mọi Banach norm đến từ inner product.

**“L2 convergence nghĩa pointwise convergence.”** Không. Chúng là different modes of convergence.

**“Mọi linear operator continuous.”** Chỉ automatic trong finite-dimensional normed spaces. Infinite dimensions có unbounded operators.

**“Eigenvalue theory của matrices áp nguyên xi.”** Spectrum của infinite-dimensional operators có richer behavior.

**“Function space norm chỉ là technical choice.”** Norm quyết định topology, convergence, stability và meaning của approximation.

---

## 24. Mental model

> Functional analysis là linear algebra sau khi vectors trở thành functions và finite-dimensional guarantees biến mất. Norm cho size/error, completeness bảo limit không rơi khỏi space, inner product tạo geometry, Hilbert space giữ projection/orthogonality, còn operators đóng vai trò của matrices. Câu hỏi trung tâm luôn là: ta đang làm việc trong space nào, với norm nào, và operator có stable/continuous trên space đó không?

---

## 25. Mạch học tiếp

```text
Linear algebra
→ Metric spaces / measure
→ Banach & Hilbert spaces
→ Operators / spectrum
→ Fourier / PDE / inverse problems
```

Đọc tiếp:

- [Fourier, signals và frequency](../09_connections/05_fourier_signals_and_frequency.md)
- [PDE intro](./10_partial_differential_equations_and_fields_intro.md)
- [Numerical methods and error](../08_optimization_numerical/02_numerical_methods_and_error.md)
- [Statistical learning and regularization](../06_probability_statistics/14_statistical_learning_bias_variance_regularization_and_validation.md)
- [Manifolds, differential forms và generalized Stokes](./15_manifolds_differential_forms_and_generalized_stokes.md)

## Further reading

- Lynn Loomis, Shlomo Sternberg — *Advanced Calculus*, especially the development of calculus in normed vector spaces and scalar-product spaces.
