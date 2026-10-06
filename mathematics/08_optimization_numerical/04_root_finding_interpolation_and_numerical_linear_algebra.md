# Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**. Route đi từ root finding và f(x)=0 → bisection/Newton convergence → interpolation và approximation → numerical linear algebra, conditioning và rounding → chọn phương pháp theo robustness.

Nhiều equations không có closed-form solution hữu ích. Máy tính vì thế không “biết đáp án rồi in ra”; nó tạo chuỗi (sequence / 시퀀스) approximations, theo dõi convergence và quản lý rounding/conditioning.

Cốt lõi (core / 핵심) chuỗi (chain / 사슬):

```text
problem formulation
→ iterative approximation
→ convergence
→ conditioning
→ algorithm stability
→ stopping / error estimate
```

Numerical mathematics là study của **reliable approximation**, không chỉ của algorithms chạy được.

## 1. gốc (root / 루트) finding: rewrite về `f(x)=0`

Một equation:

```math
g(x)=h(x)
```

có thể rewrite:

```math
f(x)=g(x)-h(x)=0.
```

Gốc (root / 루트) finding tìm `x` sao cho residual `f(x)` gần zero.

Nhưng residual nhỏ không luôn đồng nghĩa gốc (root / 루트) lỗi (error / 오류) nhỏ nếu derivative gần zero hoặc bài toán (problem / 문제) ill-conditioned.

> **Nối mạch:** Trong **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **2. Bisection: theorem-driven robustness** nối từ **1. gốc (root / 루트) finding: rewrite về f(x)=0** sang **3. Bisection strength và limitation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Bisection: theorem-driven robustness

Assume:

```text
f continuous trên [a,b]
f(a)f(b)<0
```

Intermediate giá trị (value / 값) Theorem đảm bảo ít nhất một gốc (root / 루트) trong interval.

Midpoint:

```math
m=\frac{a+b}{2}.
```

Giữ half interval còn sign thay đổi (change / 변경).

After `n` steps:

```math
\text{width}_n=\frac{b-a}{2^n}.
```

Absolute gốc (root / 루트) bất định (uncertainty / 불확실성) ≤ half interval width nếu gốc (root / 루트) bracketed uniquely enough for purpose.

> **Nối mạch:** Ở chặng này của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **2. Bisection: theorem-driven robustness** đặt tiêu chí; **3. Bisection strength và limitation** dùng tiêu chí đó để kiểm tra ranh giới, rồi **4. Newton phương thức (method / 메서드) từ Taylor linearization** mở rộng hệ quả.

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

Example `f(x)=x^2` có gốc (root / 루트) at 0 nhưng sign không đổi.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **3. Bisection strength và limitation** đặt tiêu chí; **4. Newton phương thức (method / 메서드) từ Taylor linearization** dùng tiêu chí đó để kiểm tra ranh giới, rồi **5. Quadratic convergence near simple gốc (root / 루트)** mở rộng hệ quả.

## 4. Newton phương thức (method / 메서드) từ Taylor linearization

Near `x_n`:

```math
f(x)
\approx
f(x_n)+f'(x_n)(x-x_n).
```

Set cục bộ (local / 로컬) mô hình tuyến tính (linear model / 선형 모델) to zero:

```math
x_{n+1}
=x_n-
\frac{f(x_n)}{f'(x_n)}.
```

Newton is not arbitrary formula; it solves the tangent-line approximation exactly each iteration.

> **Nối mạch:** Trong **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **5. Quadratic convergence near simple gốc (root / 루트)** nối từ **4. Newton phương thức (method / 메서드) từ Taylor linearization** sang **6. Newton thất bại (failure / 실패) modes**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Quadratic convergence near simple gốc (root / 루트)

Under suitable smoothness and if gốc (root / 루트) `r` is simple:

```math
f(r)=0,
\qquad f'(r)\ne0,
```

Newton lỗi (error / 오류) often satisfies locally:

```math
|e_{n+1}|
\approx C|e_n|^2.
```

Number of correct digits can roughly double each step once close enough.

But this is cục bộ (local / 로컬) hành vi (behavior / 동작), not toàn cục (global / 전역) guarantee.

> **Nối mạch:** Ở chặng này của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **6. Newton thất bại (failure / 실패) modes** nối từ **5. Quadratic convergence near simple gốc (root / 루트)** sang **7. Secant phương thức (method / 메서드)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Newton thất bại (failure / 실패) modes

Newton may thất bại (fail / 실패) when:

```text
initial guess poor
f' near zero
tangent jumps far away
multiple roots
non-smooth function
cycling/divergence
```

For multiple gốc (root / 루트), convergence can degrade from quadratic to tuyến tính (linear / 선형).

Modified Newton can use multiplicity thông tin (information / 정보) if known.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **7. Secant phương thức (method / 메서드)** nối từ **6. Newton thất bại (failure / 실패) modes** sang **8. Hybrid methods**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Secant phương thức (method / 메서드)

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

> **Nối mạch:** Trong **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **8. Hybrid methods** nối từ **7. Secant phương thức (method / 메서드)** sang **9. Fixed-point iteration**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Hybrid methods

Practical solvers often combine:

```text
bracketing safety
+ Newton/secant speed
```

For example, stay inside bracket; use fast step when trustworthy, otherwise fall back to bisection.

Kỹ thuật (engineering / 엔지니어링) lesson: robust software rarely uses the pure textbook phương thức (method / 메서드) blindly.

> **Nối mạch:** Ở chặng này của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **9. Fixed-point iteration** nối từ **8. Hybrid methods** sang **10. Contraction ánh xạ (mapping / 매핑) viewpoint**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Fixed-point iteration

Rewrite:

```math
x=g(x).
```

Iterate:

```math
x_{n+1}=g(x_n).
```

Near fixed điểm (point / 지점) `x^*`, if:

```math
|g'(x^*)|<1,
```

Ánh xạ (mapping / 매핑) locally contracts errors:

```math
|e_{n+1}|
\approx |g'(x^*)||e_n|.
```

Same equation can have convergent or divergent fixed-point forms depending on rearrangement.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **10. Contraction ánh xạ (mapping / 매핑) viewpoint** nối từ **9. Fixed-point iteration** sang **11. Stopping criteria**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Contraction ánh xạ (mapping / 매핑) viewpoint

In a complete chỉ số (metric / 지표) không gian (space / 공간), contraction ánh xạ (mapping / 매핑) has unique fixed điểm (point / 지점) and iteration converges from suitable/toàn cục (global / 전역) conditions.

This theorem connects numerical iteration with real phân tích (analysis / 분석) and động (dynamic / 동적) programming.

> **Nối mạch:** Trong **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **11. Stopping criteria** nối từ **10. Contraction ánh xạ (mapping / 매핑) viewpoint** sang **12. Interpolation: chính xác (exact / 정확한) fit tại known nodes**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Stopping criteria

Dùng chung (common / 공통) signals:

```text
|f(x_n)| small
|x_{n+1}-x_n| small
bracket width small
relative change small
iteration limit
```

No single criterion universally sufficient.

Residual tolerance should reflect bài toán (problem / 문제) quy mô (scale / 규모) and conditioning.

> **Nối mạch:** Ở chặng này của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **12. Interpolation: chính xác (exact / 정확한) fit tại known nodes** nối từ **11. Stopping criteria** sang **13. Lagrange interpolation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Interpolation: chính xác (exact / 정확한) fit tại known nodes

Given distinct nodes:

```math
(x_i,y_i),
\qquad i=0,\ldots,n,
```

there is unique polynomial degree ≤ `n` passing through them.

Interpolation assumes values are treated as chính xác (exact / 정확한) enough that matching them exactly is meaningful.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **13. Lagrange interpolation** nối từ **12. Interpolation: chính xác (exact / 정확한) fit tại known nodes** sang **14. Newton divided differences**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Lagrange interpolation

Lagrange interpolation dựng đa thức đi qua các điểm đã biết. Nó hữu ích khi cần giá trị giữa mẫu, nhưng độ ổn định và việc chọn node quyết định sai số ngoài dữ liệu quan sát.

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

Basis thuộc tính (property / 속성):

```math
L_i(x_j)=\delta_{ij}.
```

Each basis polynomial selects one mẫu (sample / 표본) giá trị (value / 값).

> **Nối mạch:** Trong **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **14. Newton divided differences** nối từ **13. Lagrange interpolation** sang **15. Interpolation lỗi (error / 오류)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Newton divided differences

Interpolation polynomial can also be written incrementally:

```math
P_n(x)
=a_0
+a_1(x-x_0)
+a_2(x-x_0)(x-x_1)+\cdots
```

Coefficients come from divided differences.

Advantage: adding a new nút (node / 노드) extends polynomial without rebuilding all basis terms.

> **Nối mạch:** Ở chặng này của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **15. Interpolation lỗi (error / 오류)** nối từ **14. Newton divided differences** sang **16. Runge phenomenon**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Interpolation lỗi (error / 오류)

For sufficiently smooth `f`, degree-`n` interpolation lỗi (error / 오류):

```math
f(x)-P_n(x)
=
\frac{f^{(n+1)}(\xi)}{(n+1)!}
\prod_{i=0}^{n}(x-x_i)
```

for some `\xi` in relevant interval.

Lỗi (error / 오류) depends both hàm (function / 함수) derivatives and nút (node / 노드) placement.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **16. Runge phenomenon** nối từ **15. Interpolation lỗi (error / 오류)** sang **17. Chebyshev nodes**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Runge phenomenon

High-degree polynomial interpolation on equally spaced nodes can oscillate severely near interval endpoints.

More degree does not automatically mean better approximation.

This is a major lesson against “fit more exactly = improve mô hình (model / 모델)”.

> **Nối mạch:** Trong **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **17. Chebyshev nodes** nối từ **16. Runge phenomenon** sang **18. Splines**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Chebyshev nodes

Nodes clustered near endpoints can reduce worst-case polynomial interpolation lỗi (error / 오류).

Chebyshev nodes minimize growth related to interpolation sản phẩm (product / 제품) and help điều khiển (control / 제어) Runge hành vi (behavior / 동작).

This shows **where** dữ liệu (data / 데이터) is sampled can matter as much as number of samples.

> **Nối mạch:** Ở chặng này của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **18. Splines** nối từ **17. Chebyshev nodes** sang **19. Interpolation khác regression**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Splines

Instead of one high-degree polynomial, use piecewise low-degree polynomials joined smoothly.

Cubic splines typically impose continuity of hàm (function / 함수), first derivative and second derivative at knots.

Benefits:

```text
local control
less oscillation
stable interpolation
```

CAD, graphics and numerical approximation use splines extensively.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **19. Interpolation khác regression** nối từ **18. Splines** sang **20. Approximation bases**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Interpolation khác regression

Interpolation:

```text
pass through every data point
```

Regression:

```text
allow residuals to model noisy observations
```

If measurements noisy, chính xác (exact / 정확한) interpolation may fit noise.

This is a modeling quyết định (decision / 결정), not merely mathematical preference.

> **Nối mạch:** Trong **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **20. Approximation bases** nối từ **19. Interpolation khác regression** sang **21. tuyến tính (linear / 선형) các hệ thống (systems / 시스템들): chính xác (exact / 정확한) algebra vs numerical solve**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **21. tuyến tính (linear / 선형) các hệ thống (systems / 시스템들): chính xác (exact / 정확한) algebra vs numerical solve** nối từ **20. Approximation bases** sang **22. Gaussian elimination**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. tuyến tính (linear / 선형) các hệ thống (systems / 시스템들): chính xác (exact / 정확한) algebra vs numerical solve

Mathematically:

```math
Ax=b.
```

If `A` invertible:

```math
x=A^{-1}b.
```

Numerically, explicitly forming `A^{-1}` is usually unnecessary and often less stable/efficient than solving via factorization.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **22. Gaussian elimination** nối từ **21. tuyến tính (linear / 선형) các hệ thống (systems / 시스템들): chính xác (exact / 정확한) algebra vs numerical solve** sang **23. Pivoting**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Gaussian elimination

Elimination transforms hệ thống (system / 시스템) into triangular form using row operations.

Dense độ phức tạp (complexity / 복잡도) roughly:

```math
O(n^3).
```

Back substitution then costs `O(n^2)`.

This is practical for moderate dense các hệ thống (systems / 시스템들) but not huge sparse các hệ thống (systems / 시스템들).

> **Nối mạch:** Trong **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **23. Pivoting** nối từ **22. Gaussian elimination** sang **24. LU factorization**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Pivoting

If pivot is zero/tiny, division can thất bại (fail / 실패)/amplify rounding.

Partial pivoting swaps rows to choose larger pivot magnitude.

LU with pivoting:

```math
PA=LU.
```

Pivoting is numerical stability chiến lược (strategy / 전략), not a thay đổi (change / 변경) to mathematical solution.

> **Nối mạch:** Ở chặng này của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **24. LU factorization** nối từ **23. Pivoting** sang **25. QR factorization**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. LU factorization

LU factorization tách ma trận thành lower và upper triangular để giải nhiều hệ với cùng matrix hiệu quả hơn. Pivoting và conditioning quyết định lời giải có ổn định hay không.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **25. QR factorization** nối từ **24. LU factorization** sang **26. Cholesky**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. QR factorization

QR factorization biểu diễn ma trận qua basis trực giao và phần tam giác. Nó thường ổn định hơn normal equations trong least squares, nên là cầu nối giữa hình học chiếu và tính toán số.

```math
A=QR,
```

with `Q` orthogonal and `R` upper triangular.

QR is especially useful for least squares because orthogonal transforms preserve 2-norm and avoid squaring điều kiện (condition / 조건) number as normal equations do.

> **Nối mạch:** Trong **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **26. Cholesky** nối từ **25. QR factorization** sang **27. Sparse các hệ thống (systems / 시스템들)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Cholesky

If `A` symmetric positive definite:

```math
A=LL^T.
```

Cholesky uses cấu trúc (structure / 구조) to reduce computation/lưu trữ (storage / 저장소) relative to generic LU.

But applying Cholesky requires checking/knowing SPD các giả định (assumptions / 가정들).

> **Nối mạch:** Ở chặng này của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **27. Sparse các hệ thống (systems / 시스템들)** nối từ **26. Cholesky** sang **28. Iterative tuyến tính (linear / 선형) solvers**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Sparse các hệ thống (systems / 시스템들)

Real scientific/đồ thị (graph / 그래프)/PDE matrices are often sparse.

Dense algorithms waste bộ nhớ (memory / 메모리)/thời gian (time / 시간). Sparse direct solvers exploit sparsity mẫu (pattern / 패턴), but fill-in can appear during factorization.

Thứ tự (ordering / 순서) strategies matter.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **28. Iterative tuyến tính (linear / 선형) solvers** nối từ **27. Sparse các hệ thống (systems / 시스템들)** sang **29. Residual vs lỗi (error / 오류)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. Iterative tuyến tính (linear / 선형) solvers

For very large các hệ thống (systems / 시스템들), methods like:

```text
Jacobi
Gauss–Seidel
Conjugate Gradient
GMRES
```

Bản dựng (build / 빌드) approximate solution iteratively.

Choice depends ma trận (matrix / 행렬) cấu trúc (structure / 구조).

Conjugate độ dốc (gradient / 기울기) requires symmetric positive definite ma trận (matrix / 행렬) for tiêu chuẩn (standard / 표준) guarantee.

> **Nối mạch:** Trong **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **29. Residual vs lỗi (error / 오류)** nối từ **28. Iterative tuyến tính (linear / 선형) solvers** sang **30. điều kiện (condition / 조건) number**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. Residual vs lỗi (error / 오류)

Approximate solution `\hat x`:

```math
r=b-A\hat x.
```

True lỗi (error / 오류):

```math
e=x-\hat x.
```

Quan hệ (relation / 관계):

```math
Ae=r.
```

so:

```math
e=A^{-1}r.
```

If `A^{-1}` has large norm, tiny residual may correspond to large lỗi (error / 오류).

> **Nối mạch:** Ở chặng này của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **30. điều kiện (condition / 조건) number** nối từ **29. Residual vs lỗi (error / 오류)** sang **31. Conditioning vs stability**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. điều kiện (condition / 조건) number

For invertible ma trận (matrix / 행렬):

```math
\kappa(A)=\|A\|\|A^{-1}\|.
```

Roughly measures worst-case relative sensitivity of solution to perturbations.

Large `\kappa` means bài toán (problem / 문제) intrinsically sensitive.

Even perfect thuật toán (algorithm / 알고리즘) cannot recover thông tin (information / 정보) absent from noisy/finite-precision đầu vào (input / 입력).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **31. Conditioning vs stability** nối từ **30. điều kiện (condition / 조건) number** sang **32. Floating-point mô hình (model / 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 31. Conditioning vs stability

Conditioning is thuộc tính (property / 속성) of **bài toán (problem / 문제)**.

Stability is thuộc tính (property / 속성) of **thuật toán (algorithm / 알고리즘)**.

```text
well-conditioned + unstable algorithm → bad
ill-conditioned + stable algorithm → still limited
```

Backward stable thuật toán (algorithm / 알고리즘) returns chính xác (exact / 정확한) solution to nearby bài toán (problem / 문제).

This distinction is central to numerical phân tích (analysis / 분석).

> **Nối mạch:** Trong **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **32. Floating-point mô hình (model / 모델)** nối từ **31. Conditioning vs stability** sang **33. Catastrophic cancellation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. Floating-point mô hình (model / 모델)

Floating arithmetic often modeled:

```math
\operatorname{fl}(a\circ b)
=(a\circ b)(1+\delta),
\qquad |\delta|\lesssim u,
```

for thao tác (operation / 연산) `\circ` under normal conditions, where `u` is machine precision quy mô (scale / 규모).

Small cục bộ (local / 로컬) errors can accumulate/amplify depending thuật toán (algorithm / 알고리즘)/bài toán (problem / 문제).

> **Nối mạch:** Ở chặng này của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **33. Catastrophic cancellation** nối từ **32. Floating-point mô hình (model / 모델)** sang **34. Scaling và preconditioning**, vì cơ chế trước tạo đầu vào cho bước sau.

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

Biểu diễn (representation / 표현) affects computation.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **34. Scaling và preconditioning** nối từ **33. Catastrophic cancellation** sang **35. Numerical eigenvalue liên kết (connection / 연결)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. Scaling và preconditioning

Badly scaled variables/matrices can slow iterative methods or worsen numerical hành vi (behavior / 동작).

Preconditioner `M` transforms hệ thống (system / 시스템) so effective ma trận (matrix / 행렬) has more favorable spectrum/conditioning.

For example solve:

```math
M^{-1}Ax=M^{-1}b.
```

Good preconditioner approximates inverse cheaply enough to accelerate convergence.

> **Nối mạch:** Trong **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, sau nội dung của **34. Scaling và preconditioning**, **35. Numerical eigenvalue liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **36. Worked example: Newton for square gốc (root / 루트)** mở rộng hệ quả hoặc giới hạn liên quan.

## 35. Numerical eigenvalue liên kết (connection / 연결)

Large-scale eigenproblems rarely compute characteristic polynomial.

Methods like power iteration, Lanczos/Arnoldi exploit matrix-vector products and spectral cấu trúc (structure / 구조).

This shows numerical tuyến tính (linear / 선형) algebra often uses iterative hình học (geometry / 기하학) rather than symbolic formulas.

> **Nối mạch:** Ở chặng này của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **35. Numerical eigenvalue liên kết (connection / 연결)** nêu quy tắc; **36. Worked example: Newton for square gốc (root / 루트)** thử quy tắc trong tình huống, rồi **37. Worked example: ill-conditioned 2×2 intuition** mở rộng hệ quả.

## 36. Worked example: Newton for square gốc (root / 루트)

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **36. Worked example: Newton for square gốc (root / 루트)** nêu quy tắc; **37. Worked example: ill-conditioned 2×2 intuition** thử quy tắc trong tình huống, rồi **38. AI liên kết (connection / 연결)** mở rộng hệ quả.

## 37. Worked example: ill-conditioned 2×2 intuition

If two columns of `A` almost parallel, hệ thống (system / 시스템) nearly loses a direction.

Small perturbation in `b` can demand large coefficient changes in `x` to reproduce đầu ra (output / 출력).

This is same hình học (geometry / 기하학) seen in rank/nullspace: near dependence ⇒ small singular giá trị (value / 값) ⇒ large điều kiện (condition / 조건) number.

> **Nối mạch:** Trong **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **37. Worked example: ill-conditioned 2×2 intuition** nêu quy tắc; **38. AI liên kết (connection / 연결)** thử quy tắc trong tình huống, rồi **39. Scientific computing workflow** mở rộng hệ quả.

## 38. AI liên kết (connection / 연결)

Huấn luyện (training / 학습)/tuyến tính (linear / 선형) algebra stacks rely heavily on:

```text
matrix factorizations
iterative solvers
preconditioning
low-rank approximation
stable softmax/log-sum-exp
```

Numerical tính đúng đắn (correctness / 정확성) matters because high-dimensional tối ưu hóa (optimization / 최적화) repeatedly amplifies small computational choices.

> **Nối mạch:** Ở chặng này của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **38. AI liên kết (connection / 연결)** đặt đầu vào cho **39. Scientific computing workflow**, rồi **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả hoặc giới hạn liên quan.

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

A number printed with many decimals is not bằng chứng (evidence / 증거) of accuracy.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **39. Scientific computing workflow** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Numerical mathematics studies what thông tin (information / 정보) survives finite precision and finite computation. A good phương thức (method / 메서드) converges for the right structural reasons, exposes lỗi (error / 오류), respects conditioning and uses bài toán (problem / 문제) cấu trúc (structure / 구조) instead of blindly applying formulas.

> **Nối mạch:** Trong **Gốc (root / 루트) finding, interpolation và numerical tuyến tính (linear / 선형) algebra: approximation dưới finite precision**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Dùng chung (common / 공통) Misconceptions

Newton is not globally guaranteed. More interpolation degree may worsen approximation. Small residual does not always mean small solution lỗi (error / 오류). tường minh (explicit / 명시적) inverse is usually not how môi trường vận hành (production / 운영 환경) solvers solve `Ax=b`. Ill-conditioning cannot be repaired purely by a “more accurate” thuật toán (algorithm / 알고리즘) if đầu vào (input / 입력) thông tin (information / 정보) is already insufficient.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
