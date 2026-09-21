# Root finding, interpolation và numerical linear algebra: approximation dưới finite precision

Nhiều equations không có closed-form solution hữu ích. Máy tính vì thế không “biết đáp án rồi in ra”; nó tạo sequence approximations, theo dõi convergence và quản lý rounding/conditioning.

Core chain:

```text
problem formulation
→ iterative approximation
→ convergence
→ conditioning
→ algorithm stability
→ stopping / error estimate
```

Numerical mathematics là study của **reliable approximation**, không chỉ của algorithms chạy được.

## 1. Root finding: rewrite về `f(x)=0`

Một equation:

```math
g(x)=h(x)
```

có thể rewrite:

```math
f(x)=g(x)-h(x)=0.
```

Root finding tìm `x` sao cho residual `f(x)` gần zero.

Nhưng residual nhỏ không luôn đồng nghĩa root error nhỏ nếu derivative gần zero hoặc problem ill-conditioned.

## 2. Bisection: theorem-driven robustness

Assume:

```text
f continuous trên [a,b]
f(a)f(b)<0
```

Intermediate Value Theorem đảm bảo ít nhất một root trong interval.

Midpoint:

```math
m=\frac{a+b}{2}.
```

Giữ half interval còn sign change.

After `n` steps:

```math
\text{width}_n=\frac{b-a}{2^n}.
```

Absolute root uncertainty ≤ half interval width nếu root bracketed uniquely enough for purpose.

## 3. Bisection strength và limitation

Strength:

```text
guaranteed bracket shrink
no derivative needed
stable logic
```

Limitation:

```text
linear convergence
requires sign-changing bracket
cannot directly detect even-multiplicity root with no sign change
```

Example `f(x)=x^2` có root at 0 nhưng sign không đổi.

## 4. Newton method từ Taylor linearization

Near `x_n`:

```math
f(x)
\approx
f(x_n)+f'(x_n)(x-x_n).
```

Set local linear model to zero:

```math
x_{n+1}
=x_n-
\frac{f(x_n)}{f'(x_n)}.
```

Newton is not arbitrary formula; it solves the tangent-line approximation exactly each iteration.

## 5. Quadratic convergence near simple root

Under suitable smoothness and if root `r` is simple:

```math
f(r)=0,
\qquad f'(r)\ne0,
```

Newton error often satisfies locally:

```math
|e_{n+1}|
\approx C|e_n|^2.
```

Number of correct digits can roughly double each step once close enough.

But this is local behavior, not global guarantee.

## 6. Newton failure modes

Newton may fail when:

```text
initial guess poor
f' near zero
tangent jumps far away
multiple roots
non-smooth function
cycling/divergence
```

For multiple root, convergence can degrade from quadratic to linear.

Modified Newton can use multiplicity information if known.

## 7. Secant method

Approximate derivative using two previous points:

```math
x_{n+1}
=
x_n-
f(x_n)
\frac{x_n-x_{n-1}}
{f(x_n)-f(x_{n-1})}.
```

It avoids analytic derivative and often converges faster than bisection, but lacks same bracketing robustness.

## 8. Hybrid methods

Practical solvers often combine:

```text
bracketing safety
+ Newton/secant speed
```

For example, stay inside bracket; use fast step when trustworthy, otherwise fall back to bisection.

Engineering lesson: robust software rarely uses the pure textbook method blindly.

## 9. Fixed-point iteration

Rewrite:

```math
x=g(x).
```

Iterate:

```math
x_{n+1}=g(x_n).
```

Near fixed point `x^*`, if:

```math
|g'(x^*)|<1,
```

mapping locally contracts errors:

```math
|e_{n+1}|
\approx |g'(x^*)||e_n|.
```

Same equation can have convergent or divergent fixed-point forms depending on rearrangement.

## 10. Contraction mapping viewpoint

In a complete metric space, contraction mapping has unique fixed point and iteration converges from suitable/global conditions.

This theorem connects numerical iteration with real analysis and dynamic programming.

## 11. Stopping criteria

Common signals:

```text
|f(x_n)| small
|x_{n+1}-x_n| small
bracket width small
relative change small
iteration limit
```

No single criterion universally sufficient.

Residual tolerance should reflect problem scale and conditioning.

## 12. Interpolation: exact fit tại known nodes

Given distinct nodes:

```math
(x_i,y_i),
\qquad i=0,\ldots,n,
```

there is unique polynomial degree ≤ `n` passing through them.

Interpolation assumes values are treated as exact enough that matching them exactly is meaningful.

## 13. Lagrange interpolation

```math
P(x)
=
\sum_{i=0}^{n}y_iL_i(x),
```

where:

```math
L_i(x)
=
\prod_{j\ne i}
\frac{x-x_j}{x_i-x_j}.
```

Basis property:

```math
L_i(x_j)=\delta_{ij}.
```

Each basis polynomial selects one sample value.

## 14. Newton divided differences

Interpolation polynomial can also be written incrementally:

```math
P_n(x)
=a_0
+a_1(x-x_0)
+a_2(x-x_0)(x-x_1)+\cdots
```

Coefficients come from divided differences.

Advantage: adding a new node extends polynomial without rebuilding all basis terms.

## 15. Interpolation error

For sufficiently smooth `f`, degree-`n` interpolation error:

```math
f(x)-P_n(x)
=
\frac{f^{(n+1)}(\xi)}{(n+1)!}
\prod_{i=0}^{n}(x-x_i)
```

for some `\xi` in relevant interval.

Error depends both function derivatives and node placement.

## 16. Runge phenomenon

High-degree polynomial interpolation on equally spaced nodes can oscillate severely near interval endpoints.

More degree does not automatically mean better approximation.

This is a major lesson against “fit more exactly = improve model”.

## 17. Chebyshev nodes

Nodes clustered near endpoints can reduce worst-case polynomial interpolation error.

Chebyshev nodes minimize growth related to interpolation product and help control Runge behavior.

This shows **where** data is sampled can matter as much as number of samples.

## 18. Splines

Instead of one high-degree polynomial, use piecewise low-degree polynomials joined smoothly.

Cubic splines typically impose continuity of function, first derivative and second derivative at knots.

Benefits:

```text
local control
less oscillation
stable interpolation
```

CAD, graphics and numerical approximation use splines extensively.

## 19. Interpolation khác regression

Interpolation:

```text
pass through every data point
```

Regression:

```text
allow residuals to model noisy observations
```

If measurements noisy, exact interpolation may fit noise.

This is a modeling decision, not merely mathematical preference.

## 20. Approximation bases

Polynomial interpolation is one basis choice.

Other representations include:

```text
splines
Fourier basis
wavelets
radial basis functions
orthogonal polynomials
```

Basis choice should reflect smoothness, periodicity, locality and computational needs.

## 21. Linear systems: exact algebra vs numerical solve

Mathematically:

```math
Ax=b.
```

If `A` invertible:

```math
x=A^{-1}b.
```

Numerically, explicitly forming `A^{-1}` is usually unnecessary and often less stable/efficient than solving via factorization.

## 22. Gaussian elimination

Elimination transforms system into triangular form using row operations.

Dense complexity roughly:

```math
O(n^3).
```

Back substitution then costs `O(n^2)`.

This is practical for moderate dense systems but not huge sparse systems.

## 23. Pivoting

If pivot is zero/tiny, division can fail/amplify rounding.

Partial pivoting swaps rows to choose larger pivot magnitude.

LU with pivoting:

```math
PA=LU.
```

Pivoting is numerical stability strategy, not a change to mathematical solution.

## 24. LU factorization

```math
A=LU
```

lets solve:

```math
Ly=b
```

then:

```math
Ux=y.
```

If many right-hand sides share same `A`, factorization reused, making solves cheaper.

## 25. QR factorization

```math
A=QR,
```

with `Q` orthogonal and `R` upper triangular.

QR is especially useful for least squares because orthogonal transforms preserve 2-norm and avoid squaring condition number as normal equations do.

## 26. Cholesky

If `A` symmetric positive definite:

```math
A=LL^T.
```

Cholesky uses structure to reduce computation/storage relative to generic LU.

But applying Cholesky requires checking/knowing SPD assumptions.

## 27. Sparse systems

Real scientific/graph/PDE matrices are often sparse.

Dense algorithms waste memory/time. Sparse direct solvers exploit sparsity pattern, but fill-in can appear during factorization.

Ordering strategies matter.

## 28. Iterative linear solvers

For very large systems, methods like:

```text
Jacobi
Gauss–Seidel
Conjugate Gradient
GMRES
```

build approximate solution iteratively.

Choice depends matrix structure.

Conjugate Gradient requires symmetric positive definite matrix for standard guarantee.

## 29. Residual vs error

Approximate solution `\hat x`:

```math
r=b-A\hat x.
```

True error:

```math
e=x-\hat x.
```

Relation:

```math
Ae=r.
```

so:

```math
e=A^{-1}r.
```

If `A^{-1}` has large norm, tiny residual may correspond to large error.

## 30. Condition number

For invertible matrix:

```math
\kappa(A)=\|A\|\|A^{-1}\|.
```

Roughly measures worst-case relative sensitivity of solution to perturbations.

Large `\kappa` means problem intrinsically sensitive.

Even perfect algorithm cannot recover information absent from noisy/finite-precision input.

## 31. Conditioning vs stability

Conditioning is property of **problem**.

Stability is property of **algorithm**.

```text
well-conditioned + unstable algorithm → bad
ill-conditioned + stable algorithm → still limited
```

Backward stable algorithm returns exact solution to nearby problem.

This distinction is central to numerical analysis.

## 32. Floating-point model

Floating arithmetic often modeled:

```math
\operatorname{fl}(a\circ b)
=(a\circ b)(1+\delta),
\qquad |\delta|\lesssim u,
```

for operation `\circ` under normal conditions, where `u` is machine precision scale.

Small local errors can accumulate/amplify depending algorithm/problem.

## 33. Catastrophic cancellation

Subtracting nearly equal large numbers can lose significant relative digits.

Example:

```math
\sqrt{x+1}-\sqrt{x}
```

for large `x` suffers cancellation.

Rationalize:

```math
\frac{1}{\sqrt{x+1}+\sqrt{x}}
```

which is algebraically equivalent but numerically more stable.

Representation affects computation.

## 34. Scaling và preconditioning

Badly scaled variables/matrices can slow iterative methods or worsen numerical behavior.

Preconditioner `M` transforms system so effective matrix has more favorable spectrum/conditioning.

For example solve:

```math
M^{-1}Ax=M^{-1}b.
```

Good preconditioner approximates inverse cheaply enough to accelerate convergence.

## 35. Numerical eigenvalue connection

Large-scale eigenproblems rarely compute characteristic polynomial.

Methods like power iteration, Lanczos/Arnoldi exploit matrix-vector products and spectral structure.

This shows numerical linear algebra often uses iterative geometry rather than symbolic formulas.

## 36. Worked example: Newton for square root

Solve:

```math
f(x)=x^2-a=0.
```

Newton:

```math
x_{n+1}
=x_n-
\frac{x_n^2-a}{2x_n}
```

so:

```math
x_{n+1}
=\frac12\left(x_n+\frac a{x_n}\right).
```

This is classical Babylonian square-root iteration.

## 37. Worked example: ill-conditioned 2×2 intuition

If two columns of `A` almost parallel, system nearly loses a direction.

Small perturbation in `b` can demand large coefficient changes in `x` to reproduce output.

This is same geometry seen in rank/nullspace: near dependence ⇒ small singular value ⇒ large condition number.

## 38. AI connection

Training/linear algebra stacks rely heavily on:

```text
matrix factorizations
iterative solvers
preconditioning
low-rank approximation
stable softmax/log-sum-exp
```

Numerical correctness matters because high-dimensional optimization repeatedly amplifies small computational choices.

## 39. Scientific computing workflow

Reliable numerical workflow:

```text
model problem
check units/scales
analyze conditioning
choose structure-aware algorithm
monitor residual/error indicator
validate convergence
compare against independent method when possible
```

A number printed with many decimals is not evidence of accuracy.

## Mental Model

> Numerical mathematics studies what information survives finite precision and finite computation. A good method converges for the right structural reasons, exposes error, respects conditioning and uses problem structure instead of blindly applying formulas.

## Common Misconceptions

Newton is not globally guaranteed. More interpolation degree may worsen approximation. Small residual does not always mean small solution error. Explicit inverse is usually not how production solvers solve `Ax=b`. Ill-conditioning cannot be repaired purely by a “more accurate” algorithm if input information is already insufficient.
