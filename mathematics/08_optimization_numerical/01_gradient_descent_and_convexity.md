# Gradient descent và convexity: geometry, convergence và conditioning

Gradient descent (경사하강법 / gradient descent) là một iterative method để giảm differentiable objective. Công thức update rất ngắn:

```math
x_{k+1}=x_k-\eta_k\nabla f(x_k),
```

nhưng hiểu method cần nhiều hơn việc nhớ “đi ngược gradient”. Ta cần biết:

- vì sao direction đó hợp lý;
- learning rate liên hệ curvature thế nào;
- convexity cung cấp guarantee gì;
- conditioning làm convergence chậm ra sao;
- stochastic gradients thay dynamics như thế nào;
- optimizer không thể cứu objective/model sai.

## 1. Optimization landscape trước algorithm

Ta đang solve

```math
\min_x f(x).
```

Gradient descent chỉ là một strategy dùng local information. Nếu objective poorly specified, non-identifiable hoặc constraints bị bỏ qua, optimizer có thể converge hoàn hảo tới answer không có ý nghĩa.

Do đó luôn tách ba tầng:

```text
problem/model
→ objective geometry
→ optimization algorithm
```

## 2. Gradient là local linear model

Gần `x`:

```math
f(x+\Delta)
\approx
f(x)+\nabla f(x)^T\Delta.
```

Nếu giới hạn step có fixed Euclidean length

```math
\|\Delta\|_2=\epsilon,
```

thì inner product nhỏ nhất khi `\Delta` ngược gradient:

```math
\Delta=-\epsilon\frac{\nabla f}{\|\nabla f\|}.
```

Vì vậy negative gradient là steepest-descent direction **dưới Euclidean metric**.

Điểm này quan trọng: đổi metric/preconditioner có thể đổi notion “steepest”.

## 3. Từ direction tới step size

Update thực tế:

```math
x_{k+1}=x_k-\eta\nabla f(x_k).
```

`\eta` (learning rate / 학습률) quyết định scale step.

Direction đúng nhưng step quá lớn vẫn có thể tăng objective hoặc diverge. Vì local linear approximation chỉ valid trong neighborhood đủ nhỏ, learning rate phải respect curvature.

## 4. Quadratic one-dimensional model cho convergence condition

Xét

```math
f(x)=\frac12ax^2,
\qquad a>0.
```

Gradient:

```math
f'(x)=ax.
```

Update:

```math
x_{k+1}=(1-\eta a)x_k.
```

Do đó

```math
x_k=(1-\eta a)^kx_0.
```

Convergence cần

```math
|1-\eta a|<1,
```

hay

```math
0<\eta<\frac2a.
```

Curvature `a` trực tiếp giới hạn stable learning rate.

## 5. Smoothness: gradient thay đổi nhanh đến đâu?

Một differentiable function có `L`-Lipschitz gradient nếu

```math
\|\nabla f(x)-\nabla f(y)\|
\le
L\|x-y\|.
```

`L` là upper curvature scale.

Smoothness cho descent lemma:

```math
f(y)
\le
f(x)+\nabla f(x)^T(y-x)
+\frac L2\|y-x\|^2.
```

Chọn

```math
y=x-\eta\nabla f(x)
```

với `0<\eta<2/L` cho objective decrease under standard conditions.

Đây là formal version của intuition “learning rate phải nhỏ so với steepest curvature”.

## 6. Convexity: local information trở thành global information

Function convex nếu

```math
f(tx+(1-t)y)
\le
tf(x)+(1-t)f(y),
\qquad 0\le t\le1.
```

Nếu differentiable, equivalent first-order condition:

```math
f(y)
\ge
f(x)+\nabla f(x)^T(y-x).
```

Tangent plane là global under-estimator.

Vì vậy nếu

```math
\nabla f(x^*)=0,
```

thì với mọi `y`:

```math
f(y)\ge f(x^*),
```

nên `x^*` là global minimum.

Đây là lý do convexity có giá trị: nó biến stationary condition từ local candidate thành global guarantee.

## 7. Strict và strong convexity

Strict convexity thường cho unique minimizer nếu minimizer tồn tại.

Strong convexity với parameter `\mu>0` thỏa roughly:

```math
f(y)
\ge
f(x)+\nabla f(x)^T(y-x)
+\frac\mu2\|y-x\|^2.
```

Nó nói function có curvature lower bound; landscape không quá flat.

Nếu function vừa `L`-smooth vừa `\mu`-strongly convex, condition number:

```math
\kappa=\frac L\mu.
```

Large `\kappa` nghĩa curvature scales rất khác nhau, làm first-order optimization chậm.

## 8. Conditioning: vì sao narrow valleys gây zig-zag?

Quadratic multidimensional:

```math
f(x)=\frac12x^TAx-b^Tx,
```

với symmetric positive-definite `A`.

Gradient:

```math
\nabla f(x)=Ax-b.
```

Eigenvectors của `A` là principal curvature directions; eigenvalues là curvature magnitudes.

Nếu

```math
\lambda_{\max}\gg\lambda_{\min},
```

stable step phải nhỏ enough cho steep direction, nên progress theo flat direction rất chậm.

Contour plot nhìn như narrow ellipse; gradient thường point across valley, tạo zig-zag.

## 9. Feature scaling và preconditioning thay geometry

Standardizing features có thể làm Hessian/curvature scales cân bằng hơn.

Preconditioned update:

```math
x_{k+1}
=x_k-\eta M^{-1}\nabla f(x_k)
```

với suitable positive-definite `M`.

Thay vì chỉ “đổi optimizer”, ta đang đổi effective geometry của parameter space.

Newton method dùng Hessian:

```math
x_{k+1}
=x_k-H(x_k)^{-1}\nabla f(x_k)
```

để rescale directions theo curvature local.

## 10. Convergence rates có meaning gì?

Với convex smooth functions, gradient descent thường có sublinear objective convergence kiểu

```math
f(x_k)-f(x^*)=O(1/k)
```

under standard setup.

Với smooth strongly convex functions, fixed proper step có linear/geometric convergence:

```math
\|x_k-x^*\|
\le
C\rho^k,
\qquad 0<\rho<1.
```

“Linear convergence” trong numerical optimization không nghĩa objective là linear; nó means error shrinks by roughly constant factor each iteration.

## 11. Line search: learning rate có thể được chọn adaptively

Thay fixed `\eta`, line search chọn step dọc direction `p_k`.

Backtracking line search giảm step cho đến khi sufficient decrease condition như Armijo thỏa.

Điều này useful khi curvature scale chưa biết, dù mỗi iteration cần extra function evaluations.

## 12. Momentum: thêm dynamics vào optimization

Một simple momentum form:

```math
v_{k+1}=\beta v_k+\nabla f(x_k)
```

```math
x_{k+1}=x_k-\eta v_{k+1}.
```

Intuition: consistent gradient directions accumulate velocity; oscillating directions partially cancel.

Momentum có thể accelerate elongated valleys, nhưng introduces additional stability/tuning dynamics.

## 13. Nesterov acceleration

Nesterov-style methods evaluate gradient at a look-ahead point and achieve improved theoretical rates for convex problems.

Điểm học quan trọng không phải memorize update variants, mà hiểu acceleration exploits predictable optimization dynamics rather than changing objective.

## 14. Stochastic gradient descent

Nếu objective là empirical average:

```math
f(\theta)=\frac1N\sum_{i=1}^N\ell_i(\theta),
```

full gradient:

```math
\nabla f
=\frac1N\sum_i\nabla\ell_i.
```

SGD dùng minibatch estimator:

```math
\hat g_k
\approx
\nabla f(\theta_k).
```

Nếu estimator unbiased under sampling:

```math
E[\hat g_k\mid\theta_k]
=\nabla f(\theta_k).
```

Nhưng variance tạo noisy trajectory.

Noise không chỉ “bad”; nó giảm cost per step và đôi khi giúp escape narrow/saddle regions trong non-convex landscapes.

## 15. Batch size là variance-computation trade-off

Larger batch:

- lower gradient variance;
- more compute/memory per update;
- fewer updates per data pass.

Smaller batch:

- noisier direction;
- cheaper updates;
- potentially better hardware/optimization dynamics depending setup.

Không có universal best batch size tách khỏi model/hardware/data.

## 16. Learning-rate schedules

Trong stochastic optimization, constant learning rate có thể leave noise floor quanh optimum.

Decay schedules giảm step over time để stabilize convergence.

Warmup có thể hữu ích với adaptive optimizers/large batches khi early gradient scales unstable.

Schedule là part of optimization dynamics, không chỉ training ritual.

## 17. Adam và adaptive scaling

Adam tracks moving estimates của first và second moments of gradients, rồi scale parameter-wise updates.

Điều này giúp khi coordinates có different gradient scales và sparse gradients.

Nhưng adaptive method không guarantee better generalization hoặc convergence in every problem. Hyperparameters, weight decay implementation và objective geometry vẫn matter.

## 18. Saddles và non-convex objectives

Neural-network loss surfaces non-convex. Point có

```math
\nabla f=0
```

có thể là:

- local minimum;
- local maximum;
- saddle;
- flat plateau.

Hessian eigenvalues help classify local curvature.

In high dimensions, saddle structure often more relevant than simple one-dimensional “many bad local minima” picture.

## 19. Gradient clipping và exploding gradients

Trong deep/recurrent models, gradients có thể grow very large through repeated Jacobian products.

Gradient clipping modifies effective update, e.g.

```math
\tilde g
=
g\min\left(1,\frac c{\|g\|}\right).
```

Nó controls step norm, not underlying cause of instability. Architecture/normalization/initialization may still need fixing.

## 20. Vanishing gradients và products of Jacobians

Backprop multiplies local Jacobians through layers/time.

If singular values mostly <1, gradients can shrink exponentially; >1 can explode.

Thus optimization difficulties connect directly to linear algebra spectral behavior.

## 21. Regularization changes objective

With L2:

```math
F(\theta)
=L(\theta)+\lambda\|\theta\|_2^2.
```

Optimizer is now solving a different mathematical problem.

Regularization is not a post-processing correction; it encodes preference/trade-off in objective.

## 22. Constraints require more than vanilla gradient descent

If

```math
x\in C,
```

projected gradient descent can use

```math
x_{k+1}
=\Pi_C(x_k-\eta\nabla f(x_k)).
```

Other problems use proximal methods, Lagrange/KKT, barrier/interior-point methods or specialized algorithms.

Ignoring constraints and clipping after the fact may solve a different problem.

## 23. Finance connection: portfolio quadratic optimization

Mean-variance style objective may contain

```math
w^T\Sigma w
```

as risk term.

Gradient:

```math
2\Sigma w.
```

Conditioning of covariance matrix affects numerical optimization. Near-collinear assets can create unstable directions, tying portfolio optimization to eigenvalues/regularization.

## 24. Physics connection: gradient flow

Continuous-time analogue:

```math
\frac{dx}{dt}=-\nabla f(x).
```

Then

```math
\frac{d}{dt}f(x(t))
=
\nabla f^T\frac{dx}{dt}
=-\|\nabla f\|^2\le0.
```

Energy decreases monotonically along ideal gradient flow.

Discrete gradient descent approximates this dynamics, with step size controlling discretization stability.

## 25. AI engineering: optimizer cannot repair bad problem definition

Even perfect convergence cannot fix:

- data leakage;
- label noise;
- wrong objective metric;
- distribution shift;
- under/overparameterized model;
- invalid constraints.

Optimization success must be separated from model/product success.

## Mental Model

> Gradient descent is local dynamics on an objective landscape. Gradient gives first-order direction; curvature controls safe step size; conditioning controls speed; stochasticity changes trajectory; convexity determines how much local information can be trusted globally.

## Common Misconceptions

**Negative gradient is universally steepest.** It is steepest under Euclidean metric; other geometries/preconditioners change the notion.

**Large learning rate means faster learning.** Above stability range it oscillates/diverges.

**Convex means easy in every practical sense.** Convexity gives global structure, but conditioning and scale can still make computation slow.

**Adam/SGD determines the objective.** Optimizer changes search dynamics, not what objective fundamentally rewards.
