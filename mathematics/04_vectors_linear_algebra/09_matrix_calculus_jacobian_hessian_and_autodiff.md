# Matrix calculus, Jacobian, Hessian và automatic differentiation

Khi một function nhận scalar và trả scalar, đạo hàm quen thuộc là một số. Nhưng trong optimization, machine learning, robotics, graphics và scientific computing, input thường là vector hoặc matrix và output cũng có thể là vector. Lúc đó câu hỏi “đạo hàm là gì?” cần được mở rộng thành **matrix calculus (행렬 미적분)**.

Mục tiêu của matrix calculus không phải tạo thêm ký hiệu phức tạp. Nó cung cấp ngôn ngữ để mô tả độ nhạy của một hệ nhiều biến: nếu từng input thay đổi rất nhỏ, output thay đổi theo hướng nào và mạnh đến mức nào?

## Từ derivative một biến đến differential nhiều biến

Với function scalar

```math
f:\mathbb R\to\mathbb R,
```

derivative tại `x` là số `f'(x)` sao cho

```math
f(x+\Delta x)\approx f(x)+f'(x)\Delta x
```

khi `Δx` nhỏ.

Tư tưởng này quan trọng hơn công thức derivative. Derivative là **linear approximation tốt nhất ở local neighborhood**.

Với function nhiều biến

```math
f:\mathbb R^n\to\mathbb R,
```

ta muốn một linear map biến perturbation `Δx` thành perturbation của output:

```math
f(x+\Delta x)\approx f(x)+\nabla f(x)^T\Delta x.
```

Gradient xuất hiện vì output là scalar còn input là vector.

## Gradient

Với

```math
x=(x_1,\dots,x_n)^T,
```

gradient là

```math
\nabla f(x)=
\begin{bmatrix}
\partial f/\partial x_1\\
\vdots\\
\partial f/\partial x_n
\end{bmatrix}.
```

Gradient không đơn thuần là list partial derivatives. Trong Euclidean space nó chỉ direction của mức tăng nhanh nhất của function, còn magnitude cho biết local sensitivity theo direction đó.

Ví dụ

```math
f(x)=x^Tx.
```

Vì

```math
f(x)=\sum_i x_i^2,
```

nên

```math
\nabla f(x)=2x.
```

Điều này giải thích vì sao L2 regularization tạo gradient kéo parameter về origin.

## Jacobian

Nếu

```math
f:\mathbb R^n\to\mathbb R^m,
```

thì mỗi output component phụ thuộc vào nhiều input components. **Jacobian (야코비안)** gom tất cả first-order partial derivatives vào một matrix:

```math
J_f(x)=
\begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n}\\
\vdots & \ddots & \vdots\\
\frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n}
\end{bmatrix}.
```

Kích thước của Jacobian là `m × n` nếu input dimension là `n` và output dimension là `m`.

Local approximation trở thành

```math
f(x+\Delta x)\approx f(x)+J_f(x)\Delta x.
```

Đây chính là linear transformation tốt nhất xấp xỉ function nonlinear gần `x`.

## Ví dụ Jacobian

Xét

```math
f(x,y)=
\begin{bmatrix}
x^2y\\
\sin x+y
\end{bmatrix}.
```

Jacobian là

```math
J_f(x,y)=
\begin{bmatrix}
2xy & x^2\\
\cos x & 1
\end{bmatrix}.
```

Nếu input dịch một lượng nhỏ `(Δx,Δy)`, matrix này dự đoán first-order change của cả hai output.

## Chain rule ở dạng matrix

Nếu

```math
x\xrightarrow{g}y\xrightarrow{f}z,
```

thì

```math
J_{f\circ g}(x)=J_f(g(x))J_g(x).
```

Thứ tự nhân matrix phản ánh đúng flow của perturbation: perturbation ở `x` trước hết bị `J_g` biến đổi thành perturbation ở `y`, rồi `J_f` biến đổi tiếp thành perturbation ở `z`.

Đây chính là nền tảng toán học của backpropagation.

## Hessian

Với scalar function `f:R^n→R`, đạo hàm bậc hai được gom vào **Hessian (헤시안)**:

```math
H_f(x)=
\begin{bmatrix}
\frac{\partial^2f}{\partial x_1^2} & \cdots & \frac{\partial^2f}{\partial x_1\partial x_n}\\
\vdots & \ddots & \vdots\\
\frac{\partial^2f}{\partial x_n\partial x_1} & \cdots & \frac{\partial^2f}{\partial x_n^2}
\end{bmatrix}.
```

Gradient nói slope. Hessian nói slope đang thay đổi ra sao, tức local curvature.

Taylor approximation bậc hai là

```math
f(x+\Delta x)\approx f(x)+\nabla f(x)^T\Delta x+
\frac12\Delta x^T H_f(x)\Delta x.
```

Nếu Hessian positive definite tại stationary point, function local cong lên theo mọi direction và điểm đó là strict local minimum. Nếu Hessian có cả positive và negative eigenvalues, stationary point là saddle point.

## Quadratic form

Với

```math
f(x)=\frac12x^TAx+b^Tx+c
```

và `A` symmetric,

```math
\nabla f(x)=Ax+b,
```

```math
H_f(x)=A.
```

Quadratic functions đặc biệt quan trọng vì curvature là constant. Nhiều optimization algorithms local xem nonlinear objective như một quadratic approximation.

## Đạo hàm theo matrix

Giả sử

```math
f(X)=\operatorname{tr}(X^TAX).
```

Nếu `A` symmetric,

```math
\nabla_X f=2AX.
```

Matrix calculus thường dùng trace identities để biến expressions về dạng dễ differentiate. Một identity rất hữu ích là

```math
\operatorname{tr}(ABC)=\operatorname{tr}(BCA)=\operatorname{tr}(CAB).
```

Trace cho phép đưa differential về dạng

```math
df=\operatorname{tr}(G^T dX),
```

sau đó đọc gradient `G`.

## Differential notation

Thay vì ghi partial derivative trực tiếp, có thể làm việc với differential.

Nếu

```math
y=Ax,
```

thì

```math
dy=A\,dx.
```

Nếu

```math
f=x^TAx,
```

thì

```math
df=d(x^T)Ax+x^TA\,dx.
```

Sau biến đổi,

```math
df=x^T(A^T+A)dx.
```

nên

```math
\nabla f=(A+A^T)x.
```

Nếu `A` symmetric thì gradient trở thành `2Ax`.

Differential notation thường giảm lỗi transpose khi expression phức tạp.

## Shape checking

Trong matrix calculus, kiểm tra shape là phương pháp debugging rất mạnh. Nếu `x∈R^n`, gradient của scalar theo `x` phải có `n` components. Nếu `f:R^n→R^m`, Jacobian phải ánh xạ perturbation dimension `n` sang output perturbation dimension `m`.

Nếu một expression derivative tạo shape không phù hợp với vai trò linear map của nó, nhiều khả năng notation hoặc transpose đang sai.

## Forward-mode automatic differentiation

**Automatic differentiation — AD (자동미분)** không phải symbolic differentiation và cũng không phải numerical finite difference.

Ý tưởng là decomposed computation thành elementary operations và propagate derivative chính xác theo chain rule.

Ví dụ

```math
u=x^2,
```

```math
v=\sin u,
```

```math
y=3v.
```

Forward mode propagate cùng lúc value và derivative:

```math
\dot u=2x\dot x,
```

```math
\dot v=\cos(u)\dot u,
```

```math
\dot y=3\dot v.
```

Nếu input dimension nhỏ và output dimension lớn, forward mode thường phù hợp.

## Reverse-mode automatic differentiation

Reverse mode trước tiên chạy computation forward để lưu intermediate values, sau đó đi ngược graph để propagate sensitivities từ output về inputs.

Với scalar loss `L`, ta propagate các quantities dạng

```math
\bar x=\frac{\partial L}{\partial x}.
```

Mỗi operation local biết cách nhận upstream gradient và tạo downstream gradients.

Nếu

```math
y=f(x),
```

thì reverse mode thực hiện vector-Jacobian product thay vì materialize full Jacobian.

Đây là lý do reverse mode cực kỳ hiệu quả khi output là một scalar loss còn model có hàng triệu parameters.

## Backpropagation là reverse-mode AD trên computational graph

Trong neural network, layers tạo một computational graph. Forward pass tính activations và loss. Backward pass áp dụng chain rule từ loss về từng parameter.

Ví dụ linear layer

```math
y=Wx+b
```

với upstream gradient `g=∂L/∂y` cho

```math
\frac{\partial L}{\partial x}=W^Tg,
```

```math
\frac{\partial L}{\partial W}=gx^T,
```

```math
\frac{\partial L}{\partial b}=g.
```

Ba công thức này không phải mẹo deep learning; chúng là matrix chain rule.

## Finite difference và vì sao không dùng để train network

Derivative có thể xấp xỉ bằng

```math
f'(x)\approx\frac{f(x+h)-f(x)}{h}.
```

Nhưng `h` quá lớn tạo truncation error; `h` quá nhỏ tạo floating-point cancellation. Với hàng triệu parameters, finite difference còn yêu cầu số lần evaluate function rất lớn.

Automatic differentiation tránh hai vấn đề đó bằng cách tính derivative qua algebra của computation graph ở machine precision.

## Jacobian-vector product và vector-Jacobian product

Trong systems lớn ta hiếm khi muốn materialize Jacobian đầy đủ.

Forward mode thường tính

```math
Jv,
```

nghĩa là effect của perturbation direction `v` lên output.

Reverse mode thường tính

```math
v^TJ,
```

nghĩa là propagate sensitivity từ output backward.

Cách nhìn này giải thích performance của modern autodiff frameworks tốt hơn việc tưởng rằng chúng xây một giant Jacobian matrix.

## Hessian-vector product

Second-order optimization đôi khi cần curvature nhưng Hessian `n×n` quá lớn để materialize. Có thể tính trực tiếp

```math
Hv
```

bằng combinations của automatic differentiation mà không lưu toàn bộ Hessian.

Điều này quan trọng trong Newton-CG, curvature analysis và một số meta-learning methods.

## Mental Model

Derivative nhiều chiều nên được hiểu như một **linear map của perturbations**. Gradient, Jacobian và Hessian chỉ là các representations khác nhau của local sensitivity và curvature. Automatic differentiation là kỹ thuật thực thi chain rule trên computational graph mà không cần viết symbolic derivative bằng tay.

## Common Misconceptions

Gradient không phải lúc nào cũng là “derivative duy nhất” của vector function; vector-output function tự nhiên có Jacobian. Backpropagation cũng không phải một algorithm optimization riêng: nó là cách tính gradients. Gradient descent mới là algorithm dùng gradients đó để update parameters.

Autodiff không phải finite difference. Nó không perturb input bằng một `h` nhỏ mà propagate derivatives qua các elementary operations.

## Liên kết kiến thức

Nên đọc sau [Multivariable calculus](../05_calculus/04_multivariable_calculus.md), [Linear transformations](./02_linear_transformations.md) và [Tensor & multilinear algebra](./08_tensors_and_multilinear_algebra.md). Chapter này nối trực tiếp tới [Gradient descent và convexity](../08_optimization_numerical/01_gradient_descent_and_convexity.md), [Taylor approximation](../05_calculus/08_taylor_series_and_local_approximation.md) và toàn bộ machine learning optimization.