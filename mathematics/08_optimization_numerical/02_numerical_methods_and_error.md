# Toán số: approximation, conditioning và stability trên máy tính hữu hạn

Toán số (Numerical Analysis / 수치해석) nghiên cứu cách biến một problem toán học thành computation đáng tin cậy trên máy tính thực. Điểm xuất phát là một sự thật dễ bỏ qua: computer không thao tác với số thực vô hạn chính xác, không thực hiện vô hạn bước, và thường chỉ thấy dữ liệu đã có measurement noise.

Vì vậy một công thức đúng về mặt toán học chưa bảo đảm kết quả tính được đáng tin. Numerical analysis tách ít nhất ba câu hỏi:

1. **Problem có nhạy không?** — conditioning.
2. **Ta đang approximate ideal mathematics bằng scheme nào?** — discretization/truncation.
3. **Algorithm trên finite precision có khuếch đại error không?** — stability.

> Một numerical result chỉ đáng tin khi ta hiểu cả mathematical problem, approximation scheme và machine arithmetic.

## Exact mathematics và computed number là hai tầng khác nhau

Giả sử ta muốn solve

```math
Ax=b.
```

Trong exact arithmetic, nếu `A` invertible thì solution unique:

```math
x=A^{-1}b.
```

Nhưng trong thực tế có ba vấn đề riêng:

- entries của `A,b` có thể đã là measurements có noise;
- machine lưu numbers bằng floating point nên arithmetic bị rounding;
- computing explicit inverse có thể không phải algorithm tốt để solve system.

Do đó statement “equation có unique solution” không trả lời được “computed solution có accurate không?”.

## Error: absolute và relative

Nếu true value là `x` và approximation là `\hat x`, absolute error là

```math
|\hat x-x|.
```

Relative error là

```math
\frac{|\hat x-x|}{|x|},
```

khi `x≠0`.

Absolute error phù hợp khi scale tự thân có ý nghĩa. Relative error quan trọng khi so accuracy giữa quantities khác magnitude.

Ví dụ approximation `1000001` cho true value `1000000` có absolute error `1`, nhưng relative error chỉ

```math
10^{-6}.
```

Ngược lại approximation `0.0011` cho `0.0010` có absolute error rất nhỏ `0.0001`, nhưng relative error 10%.

## Measurement error, model error và numerical error không giống nhau

Một engineering computation có thể sai do:

**Measurement error:** input data không exact.

**Model error:** mathematical model bỏ qua physics/business behavior quan trọng.

**Discretization error:** continuous/infinite object được replace bằng finite approximation.

**Rounding error:** finite-precision arithmetic.

**Algorithmic instability:** small computational perturbations bị amplify.

Không nên gộp tất cả thành “máy tính sai số”. Nếu model assumption sai, tăng floating-point precision không cứu được result.

## Floating point: tại sao `0.1+0.2` không exact?

Binary floating point biểu diễn finite set numbers gần dạng

```math
(-1)^s\times m\times2^e,
```

với finite significand `m` và exponent `e`.

Giống như `1/3=0.3333...` không có finite decimal representation, `0.1` không có finite binary representation. Computer lưu nearby representable number.

Do đó

```text
0.1 + 0.2
```

có thể không equal exactly `0.3` theo bit pattern.

Điểm đúng không phải “floating point tệ”, mà là **finite representation không thể represent mọi real number**.

## Machine epsilon và spacing

Machine epsilon roughly mô tả khoảng cách relative giữa `1` và next representable number lớn hơn `1` cho một floating format.

Floating point có approximately constant **relative** precision trong normal range, không constant absolute spacing. Numbers magnitude lớn có spacing lớn hơn.

Vì vậy adding tiny number vào huge number có thể không thay representation:

```text
large + tiny == large
```

nếu `tiny` nhỏ hơn resolution tại scale đó.

## Associativity có thể mất

Trong exact real arithmetic,

```math
(a+b)+c=a+(b+c).
```

Trong floating point, intermediate rounding làm identity có thể fail numerically.

Ví dụ nếu `a` rất lớn, `b=-a`, `c` nhỏ:

```text
(a + b) + c
```

có thể giữ `c`, trong khi

```text
a + (b + c)
```

có thể round `b+c` về gần `b`, rồi cancel thành 0.

Parallel reductions vì vậy có thể cho last-bit differences tùy order summation.

## Catastrophic cancellation

Nếu subtract hai gần-equal floating numbers, leading digits cancel và relative error có thể tăng mạnh.

Ví dụ quadratic formula

```math
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
```

có thể unstable cho một root khi `b` và square root gần nhau, vì numerator subtract gần-equal quantities.

Algebraically equivalent reformulation có thể numerically tốt hơn.

Đây là lesson quan trọng: **symbolically equivalent formulas không nhất thiết computationally equivalent**.

## Conditioning: problem bản thân nhạy tới mức nào?

Conditioning là property của problem, không phải của algorithm.

Suppose function

```math
y=f(x).
```

Nếu small perturbation `δx` tạo large relative change trong `y`, problem ill-conditioned quanh đó.

First-order sensitivity có thể nhìn qua derivative:

```math
\delta y\approx f'(x)\delta x.
```

Relative condition number một biến thường liên quan

```math
\kappa(x)=\left|\frac{x f'(x)}{f(x)}\right|,
```

khi expression hợp lệ.

Large `κ` nghĩa input relative error có thể bị amplify mạnh trong output.

## Condition number của linear system

Cho invertible matrix `A`, condition number theo chosen norm là

```math
\kappa(A)=\|A\|\,\|A^{-1}\|.
```

Nếu `κ(A)` lớn, system gần singular theo norm đó; small perturbations trong data có thể gây large changes trong solution.

Geometrically, transformation `A` squash một số directions rất mạnh. Inverting phải expand lại những directions đó, đồng thời amplify noise.

Đây là reason near-collinear features làm least squares nhạy và multicollinearity gây unstable coefficients.

## Stability: algorithm có thêm amplification không?

Conditioning hỏi “problem khó nhạy đến đâu”. Stability hỏi “algorithm có làm tình hình tệ hơn bản chất problem không?”.

Một algorithm backward stable trả computed answer đúng chính xác cho một nearby problem:

```text
computed solution = exact solution of slightly perturbed input.
```

Nếu problem well-conditioned, nearby input tạo nearby output, nên backward stability thường dẫn tới forward accuracy tốt.

Numerical linear algebra đánh giá algorithms theo lens này thay vì chỉ count arithmetic operations.

## Forward error và backward error

Forward error đo distance từ computed result tới true result.

Backward error hỏi: input phải thay đổi ít nhất bao nhiêu để computed result trở thành exact answer?

Một result có forward error lớn nhưng backward error nhỏ nếu problem ill-conditioned. Khi đó algorithm có thể hoạt động tốt, nhưng problem bản thân amplify uncertainty.

Distinction này giúp tránh blame algorithm cho sensitivity vốn nằm trong problem.

## Truncation error: finite approximation của infinite process

Derivative được định nghĩa bằng limit:

```math
f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}.
```

Computer phải chọn finite `h`, nên dùng approximation

```math
f'(x)\approx\frac{f(x+h)-f(x)}{h}.
```

Taylor expansion cho thấy forward difference có truncation error order `O(h)` dưới smoothness assumptions.

Central difference

```math
f'(x)\approx\frac{f(x+h)-f(x-h)}{2h}
```

thường có truncation error `O(h^2)`.

Higher order không có nghĩa luôn better: smaller `h` giảm truncation error nhưng có thể tăng rounding/cancellation error.

## Tại sao “step càng nhỏ càng tốt” sai?

Derivative finite difference minh họa trade-off.

Nếu `h` lớn, approximation error do Taylor truncation lớn.

Nếu `h` cực nhỏ, `f(x+h)` và `f(x)` gần nhau; subtraction có cancellation, sau đó division by tiny `h` amplify rounding.

Total error thường có U-shaped behavior theo `h`: giảm trước rồi tăng.

Optimal step size cân bằng truncation và floating-point errors.

## Root finding: bisection từ continuity

Suppose continuous function `f` thỏa

```math
f(a)f(b)<0.
```

Intermediate Value Theorem bảo đảm có ít nhất một root trong `(a,b)`.

Bisection lấy midpoint

```math
m=\frac{a+b}{2}
```

và giữ half interval còn sign change.

Sau `k` iterations, interval width là

```math
\frac{b-a}{2^k}.
```

Muốn width ≤ `ε`, cần

```math
k\ge\log_2\frac{b-a}{\varepsilon}.
```

Bisection chậm hơn Newton nhưng robust vì giữ bracket và dựa trên theorem rõ ràng.

## Newton method: local linear model

Newton iteration là

```math
x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}.
```

Derivation đến từ tangent approximation quanh `x_n`:

```math
f(x)\approx f(x_n)+f'(x_n)(x-x_n).
```

Set approximation bằng zero và solve cho `x`:

```math
0\approx f(x_n)+f'(x_n)(x_{n+1}-x_n),
```

suy ra Newton update.

Near a simple root và dưới smoothness/initialization conditions tốt, convergence có thể quadratic.

Nhưng Newton có failure modes: derivative gần zero, initial guess xấu, oscillation hoặc convergence tới root không mong muốn.

## Hybrid root solvers

Production numerical libraries thường không chọn “bisection hoặc Newton” theo kiểu tuyệt đối. Hybrid methods combine robustness của bracketing với speed của interpolation/Newton-like steps.

Đây là recurring engineering pattern: use fast method khi conditions tốt, fallback sang safe method khi invariant bị đe dọa.

## Interpolation và approximation không giống nhau

Interpolation tìm function đi qua data points exactly.

Approximation/regression cho phép residual để đạt stability/generalization tốt hơn.

High-degree polynomial interpolation qua equally spaced points có thể oscillate mạnh gần endpoints — Runge phenomenon.

Piecewise polynomial splines dùng local low-degree pieces, thường smooth và stable hơn global high-degree polynomial.

Điều này minh họa nguyên tắc: **degree cao hơn không tự động là model tốt hơn**.

## Polynomial basis và conditioning

Ngay cả khi polynomial model hợp lý, basis choice ảnh hưởng numerical conditioning.

Monomial basis

```math
1,x,x^2,\ldots,x^n
```

trên wide interval có thể tạo Vandermonde matrix ill-conditioned.

Orthogonal polynomial bases như Chebyshev polynomials thường tốt hơn cho approximation.

Một lần nữa, mathematical space giống nhau nhưng representation/basis khác có numerical behavior rất khác.

## Numerical integration

Definite integral

```math
\int_a^b f(x)\,dx
```

thường được approximate từ finite evaluations.

Trapezoidal rule approximate graph bằng line segments. Simpson's rule dùng local quadratic approximation. Gaussian quadrature chọn nodes/weights thông minh để integrate polynomial degree cao với ít evaluations hơn.

Adaptive quadrature refine interval nơi function khó hơn thay vì dùng uniform tiny step mọi nơi.

Method phù hợp phụ thuộc smoothness, singularities, oscillation và cost của evaluating `f`.

## Monte Carlo integration

Trong high dimensions, deterministic grid-based integration chịu curse of dimensionality. Monte Carlo estimate expectation bằng random samples:

```math
\int f(x)p(x)dx
=\mathbb E[f(X)]
\approx\frac1N\sum_{i=1}^N f(X_i).
```

Typical standard error decrease khoảng

```math
O(N^{-1/2}).
```

Convergence rate không nhanh theo `N`, nhưng không explode trực tiếp với dimension theo grid count, nên Monte Carlo rất quan trọng trong finance, Bayesian inference và physics simulations.

## Solve linear systems: đừng mặc định invert matrix

Mathematically,

```math
x=A^{-1}b.
```

Nhưng computationally, forming explicit inverse thường tốn hơn và có thể less stable so với factorization + solve.

Dense system thường dùng LU decomposition. Symmetric positive definite system có thể dùng Cholesky. Least squares thường dùng QR; SVD robust hơn khi rank-deficient hoặc near-degenerate.

Algorithm choice nên exploit structure.

## Sparsity thay đổi computation

Large matrices trong PDE, graphs và recommendation systems thường sparse: phần lớn entries bằng zero.

Dense `n×n` storage cần `O(n^2)` numbers, nhưng sparse representation chỉ lưu nonzeros.

Sparse direct/iterative solvers có thể giảm memory và computation cực lớn, nhưng fill-in, ordering và conditioning trở thành issues quan trọng.

“Matrix size” một mình không đủ dự đoán difficulty.

## Iterative linear solvers

Khi matrix quá lớn để factorize dense, iterative methods xây sequence approximations.

Conjugate Gradient hiệu quả cho symmetric positive definite systems. GMRES xử lý broader nonsymmetric cases.

Convergence thường phụ thuộc spectrum/condition number. Preconditioning transform system thành equivalent problem có conditioning tốt hơn.

Preconditioner tốt có thể quan trọng hơn micro-optimization code.

## Numerical ODE và stability

Euler method cho

```math
x'(t)=f(t,x)
```

là

```math
x_{n+1}=x_n+h f(t_n,x_n).
```

Nó dùng tangent local để advance one step.

Higher-order Runge–Kutta methods combine multiple slope evaluations để giảm truncation error.

Nhưng differential equations có thể **stiff**: explicit method cần tiny step vì stability, không chỉ accuracy. Implicit methods có thể cho phép larger stable steps dù mỗi step phải solve equation.

Numerical stability của time integration là concept riêng, không thể đánh giá chỉ bằng local truncation order.

## Convergence, consistency và stability

Trong discretized differential equations, ba ideas thường liên kết:

**Consistency:** discrete scheme approximate đúng continuous equation khi step → 0.

**Stability:** errors không grow uncontrolled dưới discretized dynamics.

**Convergence:** numerical solution tiến tới exact solution khi refinement.

Một scheme có local approximation đẹp nhưng unstable vẫn có thể diverge globally.

## Stopping criteria

Iterative algorithm không nên dừng chỉ vì “đã chạy 1000 iterations”. Better criteria dựa trên residual, update size hoặc estimated error.

Cho linear system,

```math
r=b-A\hat x
```

là residual. Small residual nói computed `\hat x` gần satisfy equation. Nhưng nếu problem ill-conditioned, small residual không guarantee small forward error.

Stopping criterion phải match quantity ta thật sự quan tâm.

## Scaling và nondimensionalization

Nếu variables khác orders of magnitude rất lớn, numerical solver có thể khó optimize hoặc solve system.

Rescaling variables về comparable ranges giúp conditioning và optimization geometry.

Trong physical models, nondimensionalization còn reveal controlling ratios và reduce parameter count.

Scaling không chỉ là cosmetic normalization; nó có thể thay numerical difficulty.

## Reproducibility trong parallel computing

Floating-point sum phụ thuộc order. Parallel threads/GPUs có thể reduce values theo different trees, tạo last-bit differences.

Deterministic bitwise reproducibility có thể cần fixed reduction order và cost performance.

Trong ML/scientific computing, cần phân biệt:

- bitwise identical result;
- numerically close result;
- statistically equivalent training outcome.

Không phải mọi nondeterminism đều là bug, nhưng requirement phải được định nghĩa rõ.

## Mixed precision

Modern accelerators thường dùng FP16/BF16 cho speed và memory, trong khi giữ một số accumulations/parameters ở FP32.

Mixed-precision training thành công nhờ hiểu dynamic range, scaling và error propagation — không phải vì lower precision “đủ đại khái”.

Loss scaling giúp tránh gradient underflow trong low precision.

Đây là numerical analysis xuất hiện trực tiếp trong deep learning engineering.

## Interval arithmetic và rigorous bounds

Standard floating point trả một approximation. Interval arithmetic represent value bằng interval guaranteed chứa true result under controlled rounding.

Nó hữu ích khi cần verified computation, nhưng intervals có thể widen do dependency effects.

Không phải mọi application cần rigorous bounds, nhưng concept này cho thấy numerical output có thể đi kèm certificate về uncertainty thay vì chỉ một number.

## Knowledge Connection — numerical analysis và optimization

Gradient descent dùng gradients được computed finite precision. Learning rate quá lớn gây dynamical instability; gradients rất nhỏ có underflow; ill-conditioned Hessian tạo narrow valleys và slow convergence.

Preconditioning, normalization, adaptive optimizers và second-order methods đều có numerical-analysis flavor: reshape problem để algorithm thấy geometry dễ hơn.

## Knowledge Connection — numerical analysis và data engineering

Summing billions of values có rounding accumulation. Naive mean/variance formulas có thể cancellation. Stable online algorithms như Welford's method giảm error khi tính variance streaming.

Financial systems thường tránh binary floating point cho exact decimal currency rules, dùng fixed-point/decimal representations phù hợp business semantics.

Representation choice vì thế là mathematical decision, không chỉ programming detail.

## Mental Model

> Numerical analysis là science của **độ tin cậy khi toán học đi qua máy tính hữu hạn**. Trước một number computed, hãy hỏi: input có noise gì, problem nhạy tới đâu, approximation bỏ qua gì, arithmetic round thế nào, algorithm có amplify error không, và output accuracy ta thật sự cần là gì. Một formula đúng chỉ là điểm bắt đầu.

## Common Misconceptions

**“Dùng nhiều chữ số hơn thì answer tự động chính xác hơn.”** Precision cao giảm rounding nhưng không sửa model error, measurement noise hay ill-conditioning.

**“Step size càng nhỏ càng tốt.”** Quá nhỏ có thể tăng cancellation/rounding và computation cost; stiff systems còn có stability constraints riêng.

**“Hai formulas algebraically equivalent sẽ cho cùng computed result.”** Finite precision làm order và cancellation matter.

**“Condition number lớn nghĩa algorithm tệ.”** Conditioning là property của problem. Algorithm stability là question khác.

**“Residual nhỏ nghĩa solution error nhỏ.”** Chỉ chắc hơn khi problem well-conditioned hoặc có additional bounds.

**“Muốn solve `Ax=b` thì cứ tính `A^{-1}`.”** Trong numerical linear algebra, factorization/structured solvers thường nhanh và stable hơn explicit inverse.

**“Floating point bug vì `0.1+0.2≠0.3` exact.”** Đó là consequence bình thường của finite binary representation. Bug chỉ xuất hiện khi software giả định exact semantics mà representation không bảo đảm.