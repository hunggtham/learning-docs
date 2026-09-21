# Numerical calculus: finite differences, quadrature và automatic differentiation

Calculus định nghĩa derivative/integral bằng limits ideal. Máy tính không thực hiện một process vô hạn; nó làm việc với finite precision, finite samples và finite time. Numerical calculus nghiên cứu cách thay những ideal operations đó bằng approximations có error được hiểu và kiểm soát.

Chapter này tập trung riêng vào ba vấn đề:

```text
numerical differentiation
numerical integration
automatic differentiation
```

Các topics rộng hơn như conditioning, floating-point stability, root finding và numerical linear algebra được xử lý sâu ở chapter `08_optimization_numerical/02_numerical_methods_and_error.md`.

## 1. Numerical derivative là inverse problem nhạy cảm

Derivative hỏi local rate. Với sampled/noisy data, ta phải estimate slope từ nearby values.

Forward difference:

```math
f'(x)
\approx
\frac{f(x+h)-f(x)}{h}.
```

Nếu `h` large, approximation không local enough. Nếu `h` too small, subtraction giữa nearly equal floating-point numbers có thể mất significant digits.

Do đó numerical differentiation có một paradox:

> smaller step reduces truncation error only until rounding/noise amplification starts to dominate.

## 2. Derive forward difference từ Taylor expansion

Taylor:

```math
f(x+h)
=
f(x)+hf'(x)+\frac{h^2}{2}f''(x)+O(h^3).
```

Rearrange:

```math
\frac{f(x+h)-f(x)}{h}
=
f'(x)+\frac h2f''(x)+O(h^2).
```

Nên

```math
f'(x)
=
\frac{f(x+h)-f(x)}{h}+O(h).
```

Forward difference có first-order truncation error.

## 3. Backward difference

Tương tự:

```math
f'(x)
\approx
\frac{f(x)-f(x-h)}{h}.
```

Nó cũng first-order.

Forward/backward formulas hữu ích gần boundaries khi samples chỉ available một phía.

## 4. Central difference: symmetry cancels error

Taylor:

```math
f(x+h)=f(x)+hf'(x)+\frac{h^2}{2}f''(x)+\frac{h^3}{6}f'''(x)+\cdots
```

```math
f(x-h)=f(x)-hf'(x)+\frac{h^2}{2}f''(x)-\frac{h^3}{6}f'''(x)+\cdots
```

Subtract:

```math
f(x+h)-f(x-h)
=2hf'(x)+\frac{h^3}{3}f'''(x)+\cdots
```

Do đó

```math
f'(x)
\approx
\frac{f(x+h)-f(x-h)}{2h}
```

với error

```math
O(h^2).
```

Symmetry làm even-order terms cancel.

## 5. Second derivative formula

Cộng Taylor expansions:

```math
f(x+h)-2f(x)+f(x-h)
=h^2f''(x)+O(h^4).
```

Nên

```math
f''(x)
\approx
\frac{f(x+h)-2f(x)+f(x-h)}{h^2}
```

với truncation error `O(h^2)`.

Formula này là building block của finite-difference PDE solvers.

## 6. Step-size trade-off

Một simplified error model cho forward difference:

```math
E(h)
\approx
C_1h+
C_2\frac{\varepsilon_{mach}}{h}.
```

Term đầu là truncation; term sau là rounding/cancellation amplification.

Minimize rough model cho optimal `h` scale around

```math
h\sim\sqrt{\varepsilon_{mach}}
```

times problem scale, under simplified assumptions.

Central difference có different balance because truncation is `O(h^2)`.

Điểm chính: “use smallest possible h” là wrong rule.

## 7. Noise amplification trong measured data

Nếu observed values:

```math
\tilde f(x)=f(x)+\epsilon(x),
```

finite difference divides noise difference by `h`:

```math
\frac{\epsilon(x+h)-\epsilon(x)}{h}.
```

As `h→0`, noise term can explode.

Derivative estimation từ experimental data thường cần smoothing, regularization, local polynomial fit hoặc domain models, không chỉ smaller spacing.

## 8. Higher-order finite differences

Ta có thể combine more sample points để cancel more Taylor terms.

Higher order formulas giảm truncation error với smooth functions, nhưng:

- need wider stencil;
- boundaries khó hơn;
- noise sensitivity có thể tăng;
- floating-point coefficients có trade-offs.

Order cao không automatic nghĩa practical accuracy cao hơn.

## 9. Richardson extrapolation

Nếu approximation có expansion

```math
D(h)=D+C h^p+O(h^{p+1}),
```

và compute `D(h)` cùng `D(h/2)`, ta combine để cancel leading error term.

Ý tưởng này tạo Richardson extrapolation và là principle phía sau Romberg integration.

Nó dùng knowledge về error structure để improve estimate thay vì chỉ shrink step blindly.

## 10. Numerical integration khác numerical differentiation về stability

Integration averages/accumulates values, nên thường smoothing hơn differentiation.

Ta approximate

```math
\int_a^b f(x)\,dx
```

bằng weighted sum of samples:

```math
\sum_i w_i f(x_i).
```

Choice nodes/weights quyết định quadrature rule.

## 11. Trapezoidal rule từ linear interpolation

Trên one interval `[a,b]`, approximate `f` bằng line nối endpoints.

Area trapezoid:

```math
\int_a^b f(x)dx
\approx
\frac{b-a}{2}[f(a)+f(b)].
```

Composite trapezoidal rule chia interval thành many subintervals.

Với smooth function và uniform step `h`, global error thường `O(h^2)`.

## 12. Simpson's rule từ quadratic interpolation

Trên interval với midpoint `m=(a+b)/2`, fit quadratic qua `a,m,b` rồi integrate exact polynomial đó:

```math
\int_a^b f(x)dx
\approx
\frac{b-a}{6}
\left[
f(a)+4f(m)+f(b)
\right].
```

Composite Simpson thường có high accuracy for smooth functions, with global error `O(h^4)` under standard conditions.

Weights `1,4,1` không arbitrary; chúng đến từ integrating quadratic interpolation basis.

## 13. Gaussian quadrature: choose nodes intelligently

Newton–Cotes rules như trapezoidal/Simpson use equally spaced nodes.

Gaussian quadrature chooses nodes/weights để integrate polynomials tới high degree exactly với fixed number samples.

Nó cho thấy numerical integration không chỉ là “sample dày hơn”; placement của samples có mathematical structure.

## 14. Adaptive quadrature

Function có thể smooth ở most interval nhưng thay đổi nhanh ở small region.

Uniform fine grid wastes work.

Adaptive methods estimate local error và subdivide nơi cần thiết:

```text
coarse estimate
vs
refined estimate
→ if mismatch large, split interval further
```

Đây là general numerical principle: allocate computation where error indicators say it matters.

## 15. Improper integrals cần transformation/truncation strategy

For

```math
\int_0^\infty f(x)dx,
```

computer cannot integrate to literal infinity.

Strategies:

- truncate domain with tail error bound;
- change variables map infinite interval to finite;
- use specialized quadrature.

Mathematical convergence không automatically cho numerical strategy tốt.

## 16. Highly oscillatory integrals

Nếu integrand oscillates rapidly, naive uniform sampling có thể alias/cancel incorrectly.

Methods may need:

- sufficiently high resolution;
- analytic phase information;
- Filon-type/specialized quadrature;
- transform methods.

Connection với sampling theory/Fourier rất trực tiếp.

## 17. Monte Carlo integration

For high-dimensional integral,

```math
I=E[f(X)]
```

under suitable distribution representation.

Estimate:

```math
\hat I
=\frac1N\sum_{i=1}^N f(X_i).
```

Standard error typically scales

```math
O(N^{-1/2}),
```

slow compared with deterministic low-dimensional quadrature nhưng less sensitive to dimension in exponent.

Đây là lý do Monte Carlo mạnh trong finance, Bayesian computation và high-dimensional physics.

## 18. Quasi-Monte Carlo

Thay pseudorandom samples bằng low-discrepancy sequences để fill space more evenly.

Can improve convergence for sufficiently regular integrands, though guarantees/behavior depend dimension and variation.

## 19. Automatic differentiation khác finite differences hoàn toàn

Automatic differentiation (AD / 자동미분) không approximate derivative bằng `h`.

Nó decompose computation thành primitive operations và apply chain rule exactly theo machine arithmetic.

Ví dụ:

```text
x → multiply → sin → add → loss
```

AD propagates derivative information through this computational graph.

No truncation error from finite step exists, though floating-point rounding still exists.

## 20. Forward-mode AD

Forward mode propagates pairs like

```text
(value, derivative wrt chosen input direction)
```

through computation.

Efficient khi number of input directions nhỏ relative to outputs.

Mathematically it computes Jacobian-vector products (JVPs).

## 21. Reverse-mode AD

Reverse mode runs forward to record intermediate values, then propagates adjoints backward.

Efficient khi output scalar and inputs many — exactly neural-network loss setting.

It computes vector-Jacobian products (VJPs).

Backpropagation is reverse-mode AD specialized to layered/computational-graph models.

## 22. Computational graph và chain rule

If

```math
z=f(y),\qquad y=g(x),
```

then

```math
\frac{dz}{dx}
=
\frac{dz}{dy}
\frac{dy}{dx}.
```

For many intermediate variables, reverse mode accumulates all downstream sensitivity contributions.

This is dynamic programming on the graph of local derivatives.

## 23. Memory trade-off của reverse mode

Reverse mode often needs intermediate activations from forward pass.

Large models therefore face memory cost.

Checkpointing trades recomputation for memory: save only selected states, recompute others during backward.

This links AD to time-memory trade-offs in CS.

## 24. Nondifferentiability và subgradients

Primitive like ReLU:

```math
\max(0,x)
```

nondifferentiable at `x=0`.

Frameworks choose a convention/subgradient at such points.

AD differentiates **implemented computation**, not an abstract smooth ideal. Branches, clipping, discrete operations and stop-gradient semantics matter.

## 25. Gradient checking

To debug AD implementation, compare with central finite difference:

```math
g_i^{FD}
=
\frac{f(x+he_i)-f(x-he_i)}{2h}.
```

Use relative error, not bitwise equality:

```math
\frac{\|g^{AD}-g^{FD}\|}
{\|g^{AD}\|+\|g^{FD}\|+\epsilon}.
```

If `h` too small/large, finite-difference reference itself is bad.

## 26. Complex-step differentiation

For analytic real-valued computation that can accept complex perturbation without non-analytic operations, one can use

```math
f'(x)
\approx
\frac{\operatorname{Im}f(x+ih)}{h}.
```

This avoids subtractive cancellation and can achieve very high accuracy.

But it requires implementation compatible with complex arithmetic and analyticity assumptions.

## 27. Physics and engineering

Finite differences approximate spatial/time derivatives in PDE discretization.

Quadrature computes work, energy, mass and flux from sampled fields.

AD increasingly appears in differentiable simulation and inverse problems.

Each method addresses a different computational representation of calculus.

## 28. Finance

Numerical derivatives of option prices produce Greeks when analytic formulas unavailable, but bump size/noise matter.

Monte Carlo integrates expected discounted payoff:

```math
V=e^{-rT}E[\text{payoff}].
```

Pathwise derivatives, likelihood-ratio methods and AD can estimate sensitivities more efficiently than naive finite differences.

## 29. AI

Training neural networks relies on reverse-mode AD.

Gradient checking uses finite differences only as debugging reference on small models.

Numerical integration appears in continuous-time models, diffusion/ODE systems and probabilistic inference.

## 30. Chapter boundary: what belongs elsewhere?

This chapter does **not** repeat all numerical-analysis topics.

For:

- floating-point conditioning/stability;
- root finding;
- interpolation broadly;
- numerical linear algebra;
- ODE solver stability;

see `08_optimization_numerical/02_numerical_methods_and_error.md` and related chapters.

The goal here is to keep numerical calculus conceptually focused rather than duplicate a second numerical-analysis survey.

## Mental Model

> Numerical differentiation probes local change and is inherently sensitive to noise/cancellation. Numerical integration accumulates and is often smoother. Automatic differentiation does neither approximation: it executes the chain rule through a computational graph. Choosing among them depends on what representation of the function you actually possess.

## Common Misconceptions

**Smaller finite-difference step is always better.** No; truncation falls while rounding/noise amplification eventually rises.

**AD is numerical differentiation.** No; AD applies exact chain-rule algebra to program primitives in floating-point arithmetic.

**Higher-order quadrature always wins.** Only when smoothness and sampling assumptions justify it.

**A symbolic derivative guarantees stable numerical evaluation.** No; evaluation can still suffer overflow, cancellation or ill-conditioning.
