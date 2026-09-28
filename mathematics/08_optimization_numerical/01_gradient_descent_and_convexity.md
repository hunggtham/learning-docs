# Độ dốc (gradient / 기울기) descent và convexity: hình học (geometry / 기하학), convergence và conditioning

> **Mạch đọc:** Đọc **độ dốc (gradient / 기울기) descent và convexity: hình học (geometry / 기하학), convergence và conditioning** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. tối ưu hóa (optimization / 최적화) landscape trước thuật toán (algorithm / 알고리즘)** sang **2. độ dốc (gradient / 기울기) là cục bộ (local / 로컬) mô hình tuyến tính (linear model / 선형 모델)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Độ dốc (gradient / 기울기) descent (경사하강법 / gradient descent) là một iterative phương thức (method / 메서드) để giảm differentiable mục tiêu (objective / 목표). Công thức cập nhật (update / 업데이트) rất ngắn:

```math
x_{k+1}=x_k-\eta_k\nabla f(x_k),
```

nhưng hiểu phương thức (method / 메서드) cần nhiều hơn việc nhớ “đi ngược độ dốc (gradient / 기울기)”. Ta cần biết:

- vì sao direction đó hợp lý;
- học tập (learning / 학습) tỷ lệ (rate / 비율) liên hệ curvature thế nào;
- convexity cung cấp guarantee gì;
- conditioning làm convergence chậm ra sao;
- stochastic gradients thay dynamics như thế nào;
- optimizer không thể cứu mục tiêu (objective / 목표)/mô hình (model / 모델) sai.

## 1. tối ưu hóa (optimization / 최적화) landscape trước thuật toán (algorithm / 알고리즘)

Ta đang solve

```math
\min_x f(x).
```

Độ dốc (gradient / 기울기) descent chỉ là một chiến lược (strategy / 전략) dùng cục bộ (local / 로컬) thông tin (information / 정보). Nếu mục tiêu (objective / 목표) poorly specified, non-identifiable hoặc các ràng buộc (constraints / 제약조건들) bị bỏ qua, optimizer có thể converge hoàn hảo tới answer không có ý nghĩa.

Do đó luôn tách ba tầng:

```text
problem/model
→ objective geometry
→ optimization algorithm
```

## 2. độ dốc (gradient / 기울기) là cục bộ (local / 로컬) mô hình tuyến tính (linear model / 선형 모델)

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

thì inner sản phẩm (product / 제품) nhỏ nhất khi `\Delta` ngược độ dốc (gradient / 기울기):

```math
\Delta=-\epsilon\frac{\nabla f}{\|\nabla f\|}.
```

Vì vậy negative độ dốc (gradient / 기울기) là steepest-descent direction **dưới Euclidean chỉ số (metric / 지표)**.

Điểm này quan trọng: đổi chỉ số (metric / 지표)/preconditioner có thể đổi notion “steepest”.

## 3. Từ direction tới step kích thước (size / 크기)

Cập nhật (update / 업데이트) thực tế:

```math
x_{k+1}=x_k-\eta\nabla f(x_k).
```

`\eta` (learning rate / 학습률) quyết định quy mô (scale / 규모) step.

Direction đúng nhưng step quá lớn vẫn có thể tăng mục tiêu (objective / 목표) hoặc diverge. Vì cục bộ (local / 로컬) tuyến tính (linear / 선형) approximation chỉ valid trong neighborhood đủ nhỏ, học tập (learning / 학습) tỷ lệ (rate / 비율) phải respect curvature.

## 4. Quadratic one-dimensional mô hình (model / 모델) cho convergence điều kiện (condition / 조건)

Xét

```math
f(x)=\frac12ax^2,
\qquad a>0.
```

Độ dốc (gradient / 기울기):

```math
f'(x)=ax.
```

Cập nhật (update / 업데이트):

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

Curvature `a` trực tiếp giới hạn stable học tập (learning / 학습) tỷ lệ (rate / 비율).

## 5. Smoothness: độ dốc (gradient / 기울기) thay đổi nhanh đến đâu?

Một differentiable hàm (function / 함수) có `L`-Lipschitz độ dốc (gradient / 기울기) nếu

```math
\|\nabla f(x)-\nabla f(y)\|
\le
L\|x-y\|.
```

`L` là upper curvature quy mô (scale / 규모).

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

với `0<\eta<2/L` cho mục tiêu (objective / 목표) decrease under tiêu chuẩn (standard / 표준) conditions.

Đây là formal phiên bản (version / 버전) của intuition “học tập (learning / 학습) tỷ lệ (rate / 비율) phải nhỏ so với steepest curvature”.

## 6. Convexity: cục bộ (local / 로컬) thông tin (information / 정보) trở thành toàn cục (global / 전역) thông tin (information / 정보)

Hàm (function / 함수) convex nếu

```math
f(tx+(1-t)y)
\le
tf(x)+(1-t)f(y),
\qquad 0\le t\le1.
```

Nếu differentiable, equivalent first-order điều kiện (condition / 조건):

```math
f(y)
\ge
f(x)+\nabla f(x)^T(y-x).
```

Tangent plane là toàn cục (global / 전역) under-estimator.

Vì vậy nếu

```math
\nabla f(x^*)=0,
```

thì với mọi `y`:

```math
f(y)\ge f(x^*),
```

nên `x^*` là toàn cục (global / 전역) minimum.

Đây là lý do convexity có giá trị: nó biến stationary điều kiện (condition / 조건) từ cục bộ (local / 로컬) candidate thành toàn cục (global / 전역) guarantee.

## 7. Strict và strong convexity

Strict convexity thường cho unique minimizer nếu minimizer tồn tại.

Strong convexity với parameter `\mu>0` thỏa roughly:

```math
f(y)
\ge
f(x)+\nabla f(x)^T(y-x)
+\frac\mu2\|y-x\|^2.
```

Nó nói hàm (function / 함수) có curvature lower bound; landscape không quá flat.

Nếu hàm (function / 함수) vừa `L`-smooth vừa `\mu`-strongly convex, điều kiện (condition / 조건) number:

```math
\kappa=\frac L\mu.
```

Large `\kappa` nghĩa curvature scales rất khác nhau, làm first-order tối ưu hóa (optimization / 최적화) chậm.

## 8. Conditioning: vì sao narrow valleys gây zig-zag?

Quadratic multidimensional:

```math
f(x)=\frac12x^TAx-b^Tx,
```

với symmetric positive-definite `A`.

Độ dốc (gradient / 기울기):

```math
\nabla f(x)=Ax-b.
```

Eigenvectors của `A` là principal curvature directions; eigenvalues là curvature magnitudes.

Nếu

```math
\lambda_{\max}\gg\lambda_{\min},
```

stable step phải nhỏ enough cho steep direction, nên progress theo flat direction rất chậm.

Contour plot nhìn như narrow ellipse; độ dốc (gradient / 기울기) thường điểm (point / 지점) across valley, tạo zig-zag.

## 9. tính năng (feature / 기능) scaling và preconditioning thay hình học (geometry / 기하학)

Standardizing features có thể làm Hessian/curvature scales cân bằng hơn.

Preconditioned cập nhật (update / 업데이트):

```math
x_{k+1}
=x_k-\eta M^{-1}\nabla f(x_k)
```

với suitable positive-definite `M`.

Thay vì chỉ “đổi optimizer”, ta đang đổi effective hình học (geometry / 기하학) của parameter không gian (space / 공간).

Newton phương thức (method / 메서드) dùng Hessian:

```math
x_{k+1}
=x_k-H(x_k)^{-1}\nabla f(x_k)
```

để rescale directions theo curvature cục bộ (local / 로컬).

## 10. Convergence rates có meaning gì?

Với convex smooth functions, độ dốc (gradient / 기울기) descent thường có sublinear mục tiêu (objective / 목표) convergence kiểu

```math
f(x_k)-f(x^*)=O(1/k)
```

under tiêu chuẩn (standard / 표준) setup.

Với smooth strongly convex functions, fixed proper step có tuyến tính (linear / 선형)/geometric convergence:

```math
\|x_k-x^*\|
\le
C\rho^k,
\qquad 0<\rho<1.
```

“tuyến tính (linear / 선형) convergence” trong numerical tối ưu hóa (optimization / 최적화) không nghĩa mục tiêu (objective / 목표) là tuyến tính (linear / 선형); nó means lỗi (error / 오류) shrinks by roughly constant factor each iteration.

## 11. Line tìm kiếm (search / 검색): học tập (learning / 학습) tỷ lệ (rate / 비율) có thể được chọn adaptively

Thay fixed `\eta`, line tìm kiếm (search / 검색) chọn step dọc direction `p_k`.

Backtracking line tìm kiếm (search / 검색) giảm step cho đến khi sufficient decrease điều kiện (condition / 조건) như Armijo thỏa.

Điều này useful khi curvature quy mô (scale / 규모) chưa biết, dù mỗi iteration cần extra hàm (function / 함수) evaluations.

## 12. Momentum: thêm dynamics vào tối ưu hóa (optimization / 최적화)

Một simple momentum form:

```math
v_{k+1}=\beta v_k+\nabla f(x_k)
```

```math
x_{k+1}=x_k-\eta v_{k+1}.
```

Intuition: consistent độ dốc (gradient / 기울기) directions accumulate velocity; oscillating directions partially cancel.

Momentum có thể accelerate elongated valleys, nhưng introduces additional stability/tuning dynamics.

## 13. Nesterov acceleration

Nesterov-style methods evaluate độ dốc (gradient / 기울기) at a look-ahead điểm (point / 지점) and achieve improved theoretical rates for convex problems.

Điểm học quan trọng không phải memorize cập nhật (update / 업데이트) variants, mà hiểu acceleration exploits predictable tối ưu hóa (optimization / 최적화) dynamics rather than changing mục tiêu (objective / 목표).

## 14. Stochastic độ dốc (gradient / 기울기) descent

Nếu mục tiêu (objective / 목표) là empirical average:

```math
f(\theta)=\frac1N\sum_{i=1}^N\ell_i(\theta),
```

full độ dốc (gradient / 기울기):

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

Noise không chỉ “bad”; nó giảm chi phí (cost / 비용) per step và đôi khi giúp escape narrow/saddle regions trong non-convex landscapes.

## 15. Batch kích thước (size / 크기) là variance-computation sự đánh đổi (trade-off / 트레이드오프)

Larger batch:

- lower độ dốc (gradient / 기울기) variance;
- more compute/bộ nhớ (memory / 메모리) per cập nhật (update / 업데이트);
- fewer updates per dữ liệu (data / 데이터) pass.

Smaller batch:

- noisier direction;
- cheaper updates;
- potentially better hardware/tối ưu hóa (optimization / 최적화) dynamics depending setup.

Không có universal best batch kích thước (size / 크기) tách khỏi mô hình (model / 모델)/hardware/dữ liệu (data / 데이터).

## 16. Learning-rate schedules

Trong stochastic tối ưu hóa (optimization / 최적화), constant học tập (learning / 학습) tỷ lệ (rate / 비율) có thể leave noise floor quanh optimum.

Decay schedules giảm step over thời gian (time / 시간) để stabilize convergence.

Warmup có thể hữu ích với adaptive optimizers/large batches khi early độ dốc (gradient / 기울기) scales unstable.

Schedule là part of tối ưu hóa (optimization / 최적화) dynamics, không chỉ huấn luyện (training / 학습) ritual.

## 17. Adam và adaptive scaling

Adam tracks moving estimates của first và second moments of gradients, rồi quy mô (scale / 규모) parameter-wise updates.

Điều này giúp khi coordinates có different độ dốc (gradient / 기울기) scales và sparse gradients.

Nhưng adaptive phương thức (method / 메서드) không guarantee better generalization hoặc convergence in every bài toán (problem / 문제). Hyperparameters, weight decay hiện thực (implementation / 구현) và mục tiêu (objective / 목표) hình học (geometry / 기하학) vẫn matter.

## 18. Saddles và non-convex objectives

Neural-network mất mát (loss / 손실) surfaces non-convex. điểm (point / 지점) có

```math
\nabla f=0
```

có thể là:

- cục bộ (local / 로컬) minimum;
- cục bộ (local / 로컬) maximum;
- saddle;
- flat plateau.

Hessian eigenvalues help classify cục bộ (local / 로컬) curvature.

In high dimensions, saddle cấu trúc (structure / 구조) often more relevant than simple one-dimensional “many bad cục bộ (local / 로컬) minima” picture.

## 19. độ dốc (gradient / 기울기) clipping và exploding gradients

Trong deep/recurrent các mô hình (models / 모델들), gradients có thể grow very large through repeated Jacobian products.

Độ dốc (gradient / 기울기) clipping modifies effective cập nhật (update / 업데이트), e.g.

```math
\tilde g
=
g\min\left(1,\frac c{\|g\|}\right).
```

Nó controls step norm, not underlying cause of instability. kiến trúc (architecture / 아키텍처)/normalization/initialization may still need fixing.

## 20. Vanishing gradients và products of Jacobians

Backprop multiplies cục bộ (local / 로컬) Jacobians through layers/thời gian (time / 시간).

If singular values mostly <1, gradients can shrink exponentially; >1 can explode.

Thus tối ưu hóa (optimization / 최적화) difficulties connect directly to tuyến tính (linear / 선형) algebra spectral hành vi (behavior / 동작).

## 21. Regularization changes mục tiêu (objective / 목표)

With L2:

```math
F(\theta)
=L(\theta)+\lambda\|\theta\|_2^2.
```

Optimizer is now solving a different mathematical bài toán (problem / 문제).

Regularization is not a post-processing correction; it encodes preference/sự đánh đổi (trade-off / 트레이드오프) in mục tiêu (objective / 목표).

## 22. các ràng buộc (constraints / 제약조건들) require more than vanilla độ dốc (gradient / 기울기) descent

If

```math
x\in C,
```

projected độ dốc (gradient / 기울기) descent can use

```math
x_{k+1}
=\Pi_C(x_k-\eta\nabla f(x_k)).
```

Other problems use proximal methods, Lagrange/KKT, barrier/interior-point methods or specialized algorithms.

Ignoring các ràng buộc (constraints / 제약조건들) and clipping after the fact may solve a different bài toán (problem / 문제).

## 23. Finance liên kết (connection / 연결): portfolio quadratic tối ưu hóa (optimization / 최적화)

Mean-variance style mục tiêu (objective / 목표) may contain

```math
w^T\Sigma w
```

as rủi ro (risk / 위험) term.

Độ dốc (gradient / 기울기):

```math
2\Sigma w.
```

Conditioning of covariance ma trận (matrix / 행렬) affects numerical tối ưu hóa (optimization / 최적화). Near-collinear assets can create unstable directions, tying portfolio tối ưu hóa (optimization / 최적화) to eigenvalues/regularization.

## 24. Physics liên kết (connection / 연결): độ dốc (gradient / 기울기) luồng (flow / 흐름)

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

Năng lượng (energy / 에너지) decreases monotonically along ideal độ dốc (gradient / 기울기) luồng (flow / 흐름).

Discrete độ dốc (gradient / 기울기) descent approximates this dynamics, with step kích thước (size / 크기) controlling discretization stability.

## 25. AI kỹ thuật (engineering / 엔지니어링): optimizer cannot repair bad bài toán (problem / 문제) definition

Even perfect convergence cannot fix:

- dữ liệu (data / 데이터) leakage;
- label noise;
- wrong mục tiêu (objective / 목표) chỉ số (metric / 지표);
- phân phối (distribution / 분포) shift;
- under/overparameterized mô hình (model / 모델);
- invalid các ràng buộc (constraints / 제약조건들).

Tối ưu hóa (optimization / 최적화) success must be separated from mô hình (model / 모델)/sản phẩm (product / 제품) success.

## Mô hình tư duy (mental model / 사고 모델)

> độ dốc (gradient / 기울기) descent is cục bộ (local / 로컬) dynamics on an mục tiêu (objective / 목표) landscape. độ dốc (gradient / 기울기) gives first-order direction; curvature controls safe step kích thước (size / 크기); conditioning controls speed; stochasticity changes trajectory; convexity determines how much cục bộ (local / 로컬) thông tin (information / 정보) can be trusted globally.

## Dùng chung (common / 공통) Misconceptions

**Negative độ dốc (gradient / 기울기) is universally steepest.** It is steepest under Euclidean chỉ số (metric / 지표); other geometries/preconditioners thay đổi (change / 변경) the notion.

**Large học tập (learning / 학습) tỷ lệ (rate / 비율) means faster học tập (learning / 학습).** Above stability phạm vi (range / 범위) it oscillates/diverges.

**Convex means easy in every practical sense.** Convexity gives toàn cục (global / 전역) cấu trúc (structure / 구조), but conditioning and quy mô (scale / 규모) can still make computation slow.

**Adam/SGD determines the mục tiêu (objective / 목표).** Optimizer changes tìm kiếm (search / 검색) dynamics, not what mục tiêu (objective / 목표) fundamentally rewards.

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 optimization](./00_optimization.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
