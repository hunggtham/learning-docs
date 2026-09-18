# Phương trình vi phân và hệ động lực: từ local law đến global trajectory

Nhiều mô hình khoa học không nói trực tiếp “state sẽ bằng bao nhiêu tại time `t`”. Chúng mô tả **quy luật thay đổi cục bộ**: velocity phụ thuộc position ra sao, population tăng theo size thế nào, current phụ thuộc voltage như thế nào, hay concentration thay đổi theo reaction rate ra sao.

**Differential equation (미분방정식)** là phương trình chứa một unknown function cùng derivatives của nó. Solution là function có behavior phù hợp với local law ở mọi point trong domain.

Ý tưởng cốt lõi là:

```text
local rule of change + initial/boundary information → global behavior
```

## Ordinary differential equation

Một **ordinary differential equation — ODE (상미분방정식)** có một independent variable, thường là time.

First-order ODE có dạng

```math
\frac{dy}{dt}=f(t,y).
```

Second-order ODE có thể có dạng

```math
\frac{d^2y}{dt^2}=f(t,y,y').
```

Order của ODE là order cao nhất của derivative xuất hiện.

## Initial value problem

Equation thường cho một family solutions. Initial condition chọn trajectory cụ thể.

Ví dụ

```math
y'=2y
```

có family

```math
y(t)=Ce^{2t}.
```

Nếu thêm

```math
y(0)=3,
```

thì `C=3`, nên unique candidate solution là

```math
y(t)=3e^{2t}.
```

Pair của differential equation và initial condition gọi là **initial value problem — IVP**.

## Existence và uniqueness

Không phải every differential equation với initial condition đều có unique solution.

Một important theorem, Picard–Lindelöf, nói roughly rằng nếu `f(t,y)` continuous và sufficiently Lipschitz theo `y` quanh initial point, IVP

```math
y'=f(t,y),\qquad y(t_0)=y_0
```

có local unique solution.

Điểm thực dụng là: trước khi “giải” equation, cần biết problem có well-defined solution hay không.

## Separable equations

Nếu equation có dạng

```math
\frac{dy}{dt}=g(t)h(y),
```

và `h(y)≠0`, có thể tách variables:

```math
\frac{dy}{h(y)}=g(t)dt.
```

Sau đó integrate hai vế.

Ví dụ exponential growth:

```math
y'=ky.
```

Ta có

```math
\frac{dy}{y}=kdt,
```

nên

```math
\ln|y|=kt+C,
```

và

```math
y=Ce^{kt}.
```

## Exponential growth và decay

Equation

```math
\frac{dP}{dt}=kP
```

nói **absolute growth rate proportional to current amount**.

Nếu `k>0`, growth exponential.

Nếu `k<0`, decay exponential:

```math
P(t)=P_0e^{-\lambda t}.
```

Half-life `T_{1/2}` thỏa

```math
e^{-\lambda T_{1/2}}=\frac12,
```

nên

```math
T_{1/2}=\frac{\ln2}{\lambda}.
```

Exponential không phải arbitrary curve; nó là unique shape có relative rate constant.

## First-order linear ODE

General form:

```math
y'+p(t)y=q(t).
```

Integrating factor là

```math
\mu(t)=e^{\int p(t)dt}.
```

Nhân equation với `μ` biến left side thành derivative của product:

```math
(\mu y)'=\mu q.
```

Do đó

```math
\mu y=\int \mu q\,dt+C.
```

Method này xuất hiện trong RC circuits, mixing models và linear response systems.

## Equilibrium points

Với autonomous equation

```math
y'=f(y),
```

equilibrium `y*` thỏa

```math
f(y^*)=0.
```

Nếu system bắt đầu đúng tại equilibrium, derivative bằng 0 nên state không đổi.

Nhưng quan trọng hơn là **stability**: nếu perturb nhẹ khỏi equilibrium, trajectory quay lại hay đi xa?

## Phase line

Trong one-dimensional autonomous system, sign của `f(y)` cho direction motion.

Nếu `f(y)>0`, state tăng. Nếu `f(y)<0`, state giảm.

Plot signs trên number line giúp classify equilibria mà không cần closed-form solution.

Stable equilibrium hút nearby trajectories; unstable equilibrium đẩy chúng ra xa.

## Logistic growth

Resource-limited population model:

```math
P'=rP\left(1-\frac PK\right).
```

Equilibria là

```math
P=0,\qquad P=K.
```

Khi `0<P<K`, growth positive. Khi `P>K`, derivative negative.

`K` là carrying capacity và là stable equilibrium cho positive initial populations trong idealized model.

Logistic model giải thích vì sao exponential growth thường chỉ là local approximation ở giai đoạn đầu.

## Second-order equations

Newton's second law

```math
F=ma
```

với

```math
a=x''(t)
```

tự nhiên tạo second-order ODE.

Ideal spring:

```math
mx''+kx=0.
```

Chia cho `m`:

```math
x''+\omega^2x=0,
```

với

```math
\omega=\sqrt{k/m}.
```

Solutions là

```math
x(t)=A\cos(\omega t)+B\sin(\omega t).
```

Oscillation xuất hiện vì acceleration luôn kéo state về equilibrium.

## Characteristic equation

Linear constant-coefficient ODE

```math
ay''+by'+cy=0
```

thử solution

```math
y=e^{rt}.
```

Ta thu được

```math
ar^2+br+c=0.
```

Roots của polynomial quyết định shape solution.

Hai real distinct roots tạo combinations của exponentials.

Repeated root tạo term `te^{rt}`.

Complex roots

```math
r=\alpha\pm i\beta
```

cho oscillation với envelope `e^{\alpha t}`.

Đây là connection trực tiếp giữa algebraic roots và dynamic behavior.

## Damped oscillator

Model

```math
mx''+cx'+kx=0
```

có characteristic equation

```math
mr^2+cr+k=0.
```

Discriminant

```math
c^2-4mk
```

phân loại behavior.

Nếu negative, roots complex và system underdamped: oscillation decay dần.

Nếu zero, critical damping: return nhanh mà không oscillate trong ideal model.

Nếu positive, overdamped: two real decay modes.

## Forced systems và resonance

Nếu có external input:

```math
mx''+cx'+kx=F(t).
```

Solution thường gồm transient component và forced/steady-state component.

Nếu forcing frequency gần natural frequency và damping nhỏ, response amplitude có thể lớn: **resonance**.

Resonance là dynamic consequence của frequency matching, không chỉ là “rung mạnh”.

## Systems of ODEs

Nhiều systems cần vector state:

```math
\frac{d\mathbf x}{dt}=F(t,\mathbf x).
```

Linear autonomous system:

```math
\mathbf x'=A\mathbf x.
```

Solution formally là

```math
\mathbf x(t)=e^{At}\mathbf x(0).
```

Nếu `A` diagonalizable,

```math
A=PDP^{-1},
```

thì

```math
e^{At}=Pe^{Dt}P^{-1}.
```

Mỗi eigenvalue tạo một dynamic mode `e^{\lambda t}`.

## Stability và eigenvalues

Với continuous linear system

```math
x'=Ax,
```

nếu mọi eigenvalues có negative real part, origin asymptotically stable.

Nếu có eigenvalue với positive real part, có direction grow exponentially và origin unstable.

Imaginary parts tạo oscillation; real parts tạo growth/decay envelope.

Đây là lý do eigenvalues là language trung tâm của control theory.

## Nonlinear systems và linearization

Cho

```math
x'=F(x).
```

Near equilibrium `x*`, Taylor approximation cho

```math
F(x)\approx F(x^*)+J_F(x^*)(x-x^*).
```

Vì equilibrium thỏa `F(x*)=0`, local dynamics gần đó gần giống

```math
\delta x'=J_F(x^*)\delta x.
```

Eigenvalues của Jacobian giúp classify local stability trong nhiều cases.

Điều này nối nonlinear differential equations với matrix calculus và eigenanalysis.

## Phase plane

Với two-dimensional system, thay vì plot variables theo time, ta plot trajectory trong state space `(x,y)`.

Phase portrait cho thấy equilibria, closed orbits, separatrices và flow geometry.

Hai trajectories của deterministic ODE với unique solutions không thể cross tại cùng state/time-independent vector field, vì crossing sẽ imply hai futures từ cùng state.

## Conservation laws

Một differential equation có thể preserve quantity `E(x)` dọc trajectory:

```math
\frac d{dt}E(x(t))=0.
```

Trong undamped mechanical system, total energy thường conserved.

Conserved quantities constrain trajectories vào level sets và có thể simplify analysis mạnh.

## Boundary value problems

Không phải mọi problem cho conditions tại một single initial time.

Ví dụ

```math
y''+\lambda y=0,
```

với

```math
y(0)=0,\qquad y(L)=0
```

là boundary value problem.

Chỉ một số values của `λ` cho nontrivial solutions. Đây là origin của eigenvalue problems trong PDE và quantum mechanics.

## Numerical solution

Nhiều ODE không có elementary closed form hoặc system quá phức tạp để giải symbolic.

Euler method dùng local tangent:

```math
x_{n+1}=x_n+h f(t_n,x_n).
```

Nó là first-order method: global error thường proportional `h` dưới suitable assumptions.

## Runge–Kutta intuition

Euler chỉ lấy slope đầu interval. Runge–Kutta methods sample multiple slopes trong step để estimate average slope tốt hơn.

Classical RK4:

```math
k_1=f(t_n,x_n),
```

```math
k_2=f(t_n+h/2,x_n+hk_1/2),
```

```math
k_3=f(t_n+h/2,x_n+hk_2/2),
```

```math
k_4=f(t_n+h,x_n+hk_3),
```

và

```math
x_{n+1}=x_n+\frac h6(k_1+2k_2+2k_3+k_4).
```

RK4 có high accuracy cho many smooth nonstiff problems.

## Local error và global error

Local truncation error đo error tạo trong một step nếu starting value exact.

Global error là accumulated error sau nhiều steps.

Một method local rất chính xác vẫn cần stability để error không amplify qua repeated steps.

## Stiff equations

Một ODE gọi là **stiff** khi có nhiều time scales rất khác nhau làm explicit methods cần extremely small step để remain stable, dù solution itself có thể smooth.

Ví dụ chemical kinetics có fast reactions và slow processes cùng tồn tại.

Implicit methods như backward Euler thường stable hơn cho stiff problems.

## Backward Euler

Backward Euler dùng

```math
x_{n+1}=x_n+h f(t_{n+1},x_{n+1}).
```

Unknown `x_{n+1}` xuất hiện cả hai vế, nên mỗi step có thể cần solve nonlinear equation.

Đổi lại, method có stronger stability properties.

## Adaptive step size

Fixed step `h` có thể waste computation ở smooth regions và thiếu accuracy ở rapidly changing regions.

Adaptive solvers estimate local error rồi tự tăng/giảm step size để đạt tolerance target.

Modern ODE solvers thường ưu tiên tolerance hơn việc người dùng chọn một `h` cứng.

## Event detection

Trong simulation, ta đôi khi quan tâm thời điểm solution cross threshold, va chạm hoặc switch regime.

Solver cần locate event time giữa numerical steps, thường bằng interpolation/root finding, thay vì chỉ kiểm tra discrete sampled times.

## Dimensionless variables

Scaling variables có thể reveal key dimensionless parameters và improve numerical conditioning.

Ví dụ thay

```math
t=\tau T,
```

có thể biến constants thành ratios thể hiện relative time scales.

Non-dimensionalization giúp so sánh systems khác units và nhận ra dominant mechanisms.

## Differential equations và Laplace transform

Linear ODE với initial conditions có thể transform thành algebraic equation trong `s` domain.

Ví dụ differentiation trở thành multiplication by `s` cộng initial-condition terms.

Điều này hữu ích cho linear time-invariant systems và control, đặc biệt khi input có steps/impulses.

## Differential equations và probability

Stochastic differential equations thêm random forcing, schematic:

```math
dX_t=\mu(X_t,t)dt+\sigma(X_t,t)dW_t.
```

Ordinary calculus không đủ vì Brownian paths không differentiable theo classical sense; stochastic calculus phát triển rules mới.

Đây là bridge từ deterministic dynamics sang stochastic processes.

## Differential equations và machine learning

Continuous-depth neural networks như Neural ODEs xem hidden state evolution là

```math
\frac{dh}{dt}=f_\theta(t,h).
```

Training cần differentiate through numerical ODE solution.

Dù implementation hiện đại, underlying mathematics vẫn là dynamic system, numerical integration và sensitivity analysis.

## Mental Model

Differential equation là một **generator của trajectories**. Nó chỉ local velocity của state tại mỗi point. Initial condition đặt system vào một point; vector field nói nó phải đi direction nào; integration qua time tạo global trajectory.

Linear systems có thể tách thành eigenmodes. Nonlinear systems thường được hiểu local bằng linearization, global bằng phase geometry, invariants và numerical simulation.

## Common Misconceptions

Có differential equation chưa chắc có unique solution; conditions về regularity và initial/boundary data matters. Có closed-form expression cũng không có nghĩa model đúng về physical system.

Numerical solver không “giải chính xác bằng máy tính”. Nó tạo approximation với truncation, floating-point và modeling errors.

Giảm step size không luôn chữa mọi vấn đề; stiff systems cần stability-aware methods.

Eigenvalue stability criteria của linearization là local statements cho nonlinear systems và có edge cases khi eigenvalues nằm trên imaginary axis.

## Liên kết kiến thức

Chapter này nối [Integrals](./03_integrals_and_accumulation.md), [Eigenvalues](../04_vectors_linear_algebra/04_eigenvalues_and_eigenvectors.md), [Taylor approximation](./08_taylor_series_and_local_approximation.md), [PDE](./10_partial_differential_equations_and_fields_intro.md), [Laplace/Z-transform](../09_connections/06_laplace_z_transform_and_dynamic_systems.md), [Stochastic processes](../06_probability_statistics/11_stochastic_processes_markov_chains_and_time_series.md) và [Dynamic programming/optimal control](../08_optimization_numerical/06_dynamic_programming_bellman_and_optimal_control.md).