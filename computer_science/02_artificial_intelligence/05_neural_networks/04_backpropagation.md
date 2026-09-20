# Backpropagation: Chain Rule trên Computational Graph

Backpropagation (역전파 / lan truyền ngược) thường bị mô tả như “thuật toán giúp neural network học”. Chính xác hơn, backpropagation là một **efficient algorithm để tính gradients của một scalar output, thường là loss, đối với rất nhiều intermediate values và parameters trong computational graph**.

Learning còn cần optimizer dùng gradients để update parameters. Backprop chỉ trả lời:

> Nếu parameter thay đổi rất nhỏ, loss sẽ thay đổi theo hướng và mức nào?

## Bắt đầu từ Chain Rule

Nếu:

\[
y=f(u),\qquad u=g(x)
\]

thì:

\[
\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}
\]

Neural network chỉ là composition lớn hơn:

\[
L=f_L(f_{L-1}(...f_1(x)))
\]

Backprop áp dụng chain rule theo reverse topological order của computation graph.

## Một scalar example

Giả sử:

\[
z=wx+b
\]

\[
\hat y=\sigma(z)
\]

\[
L=\frac12(\hat y-y)^2
\]

Muốn gradient theo `w`:

\[
\frac{\partial L}{\partial w}
=\frac{\partial L}{\partial \hat y}
\frac{\partial \hat y}{\partial z}
\frac{\partial z}{\partial w}
\]

Từng factor:

\[
\frac{\partial L}{\partial \hat y}=\hat y-y
\]

\[
\frac{\partial \hat y}{\partial z}=\sigma(z)(1-\sigma(z))
\]

\[
\frac{\partial z}{\partial w}=x
\]

nên:

\[
\frac{\partial L}{\partial w}=(\hat y-y)\sigma(z)(1-\sigma(z))x
\]

Không có magic. Đây chỉ là chain rule qua các operations đã chạy ở forward pass.

## Reverse-Mode Automatic Differentiation

Nếu có millions parameters nhưng chỉ một scalar loss, ta cần derivatives:

\[
\frac{\partial L}{\partial \theta_1},...,
\frac{\partial L}{\partial \theta_m}
\]

Reverse-mode AD cực hiệu quả vì một backward traversal có thể compute gradient cho tất cả parameters với cost cùng order với forward pass, thường vài lần forward cost chứ không `m` forward passes.

Backpropagation trong neural networks là application đặc biệt của reverse-mode automatic differentiation.

## Local gradients và upstream gradient

Mỗi operation chỉ cần biết:

1. local derivative của output theo inputs;
2. gradient đã truyền từ downstream.

Ví dụ `z=a+b`:

\[
\frac{\partial z}{\partial a}=1,\qquad \frac{\partial z}{\partial b}=1
\]

Nếu upstream gradient là:

\[
\bar z=\frac{\partial L}{\partial z}
\]

thì:

\[
\bar a=\bar z,
\qquad
\bar b=\bar z
\]

Với multiply `z=ab`:

\[
\bar a=\bar z\cdot b,
\qquad
\bar b=\bar z\cdot a
\]

Autograd frameworks compose thousands such local rules.

## Branching graph và gradient accumulation

Nếu một tensor ảnh hưởng loss qua nhiều paths:

\[
L=f(x)+g(x)
\]

thì:

\[
\frac{dL}{dx}=f'(x)+g'(x)
\]

Backward phải **sum gradients từ mọi downstream paths**.

Đây là lý do frameworks accumulate gradients. Trong PyTorch, gọi `.backward()` nhiều lần mà không zero gradients có thể cộng gradient ngoài ý muốn — hoặc intentionally để gradient accumulation across mini-batches.

## Vector/Jacobian perspective

Nếu function:

\[
y=f(x)
\]

với vectors, derivative là Jacobian:

\[
J_{ij}=\frac{\partial y_i}{\partial x_j}
\]

Nhưng backprop không cần materialize full Jacobian khổng lồ. Nó computes **vector-Jacobian products (VJP)** efficiently.

Nếu upstream gradient `v=∂L/∂y`, backward computes:

\[
v^TJ
\]

mà không xây `J` đầy đủ.

Điều này cực quan trọng cho memory/compute feasibility.

## Backprop qua Linear Layer

Batch form:

\[
Z=XW^T+b
\]

Nếu upstream:

\[
G_Z=\frac{\partial L}{\partial Z}
\]

thì:

\[
\frac{\partial L}{\partial W}=G_Z^TX
\]

\[
\frac{\partial L}{\partial X}=G_ZW
\]

\[
\frac{\partial L}{\partial b}=\sum_{batch}G_Z
\]

Đây là matrix multiplications — lý do GPU rất phù hợp cả forward và backward.

## Backprop qua activation

Elementwise activation:

\[
h=\phi(z)
\]

thì:

\[
\frac{\partial L}{\partial z}
=rac{\partial L}{\partial h}\odot\phi'(z)
\]

Nếu `φ'(z)` thường gần zero, gradient shrink. Đây là vanishing-gradient connection.

## Sigmoid + Cross-Entropy simplification

Binary sigmoid:

\[
p=\sigma(z)
\]

BCE loss:

\[
L=-[y\log p+(1-y)\log(1-p)]
\]

Derivative simplifies đẹp:

\[
\frac{\partial L}{\partial z}=p-y
\]

Softmax + cross-entropy multiclass cũng có analogous result:

\[
\frac{\partial L}{\partial z_k}=p_k-y_k
\]

Sự cancellation này giúp gradient behavior và numerical implementation tốt hơn việc treat từng block naive.

## Vanishing Gradients

Gradient qua depth là product của many Jacobians:

\[
\frac{\partial L}{\partial h^{(l)}}
=J_{l+1}^TJ_{l+2}^T...J_L^T
\frac{\partial L}{\partial h^{(L)}}
\]

Nếu norms thường <1, product shrink exponentially. Early layers nhận signal rất nhỏ.

Sigmoid/tanh saturation làm problem nặng hơn.

Solutions/history:

- ReLU-family activations;
- Xavier/He initialization;
- normalization;
- residual connections;
- gated architectures.

## Exploding Gradients

Nếu Jacobian products có norms >1 repeatedly, gradients explode. Symptoms:

- loss NaN/Inf;
- huge parameter update;
- unstable training.

Mitigations:

- appropriate initialization;
- normalization;
- smaller learning rate;
- gradient clipping.

Gradient norm clipping:

\[
g\leftarrow g\cdot\min\left(1,\frac{c}{\|g\|}\right)
\]

limits global gradient norm to threshold `c`.

## Residual Connection và gradient highway

Residual block:

\[
y=x+F(x)
\]

Derivative:

\[
\frac{\partial y}{\partial x}=I+\frac{\partial F}{\partial x}
\]

Identity term tạo direct gradient path, giúp very deep networks trainable hơn.

Transformers và ResNets đều phụ thuộc insight này.

## Gradient Checkpointing

Backward cần activations từ forward. Nếu model lớn, memory cao.

Checkpointing chỉ store một số activations; backward recompute missing forward segments.

Trade-off:

```text
less memory
↔
more compute
```

Đây là systems consequence trực tiếp của backprop dependency.

## Stop Gradient / Detach

Đôi khi muốn value participate forward nhưng không receive gradient.

`detach` / stop-gradient tạo boundary trong graph.

Use cases:

- target networks;
- contrastive learning tricks;
- teacher-student setup;
- preventing unwanted parameter updates.

Dùng sai có thể silently break learning.

## Higher-Order Gradients

Backprop thường compute first-order gradients. Một số algorithms cần gradient of gradient, Hessian-vector products hoặc meta-learning derivatives.

Framework có thể build graph of backward computation nếu configured, nhưng memory/compute tăng mạnh.

## Backprop không phải biologically plausible explanation

Backprop là computational optimization algorithm, không phải established model về cách biological brain learns. Research có biologically plausible alternatives, nhưng engineering success của backprop không chứng minh brain dùng same mechanism.

## Gradient không phải explanation của model prediction

Gradient `∂output/∂input` có thể dùng saliency, nhưng gradient chỉ local sensitivity. Nó không automatically là causal explanation hay full reasoning trace.

## Debugging gradients

Useful diagnostics:

- gradient norm per layer;
- parameter norm/update ratio;
- percent zero gradient;
- NaN/Inf;
- exploding/vanishing across depth.

Finite-difference gradient check cho small network:

\[
\frac{\partial L}{\partial \theta}
\approx
\frac{L(\theta+\epsilon)-L(\theta-\epsilon)}{2\epsilon}
\]

có thể verify custom backward implementation. Không dùng cho large-scale training vì expensive/numerically sensitive.

## Mental Model

```text
Forward:
parameters → intermediate values → loss

Backward:
loss sensitivity
← local derivative
← local derivative
← ...
→ gradient for every parameter
```

Backprop không “biết” cách sửa model theo semantic meaning. Nó chỉ propagate quantitative credit/blame defined bởi loss và computation graph.

## Common Misconceptions

### “Backpropagation = Gradient Descent”

Backprop tính gradients. Gradient Descent/Adam dùng gradients để update.

### “Autograd nghĩa không cần hiểu derivatives”

Không hiểu gradient flow khiến khó debug saturation, detach, exploding gradient, custom operations và training instability.

### “Gradient lớn nghĩa feature quan trọng”

Gradient là local sensitivity, phụ thuộc scale/point/model; không tự động là global importance.

### “Backward pass lưu toàn bộ Jacobian”

Reverse-mode AD dùng VJP/local rules để tránh materialize full Jacobians.

## Knowledge Connection

Xem [Calculus for AI](../01_mathematical_foundations/04_calculus_for_ai.md), [Forward Propagation](./03_forward_propagation.md) và tiếp theo [Gradient Descent and Optimizers](./05_gradient_descent_and_optimizers.md).