# Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory

> **Mạch đọc:** Đọc **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Ordinary differential equation** sang **Initial giá trị (value / 값) bài toán (problem / 문제)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Nhiều mô hình khoa học không nói trực tiếp “trạng thái (state / 상태) sẽ bằng bao nhiêu tại thời gian (time / 시간) `t`”. Chúng mô tả **quy luật thay đổi cục bộ**: velocity phụ thuộc position ra sao, population tăng theo kích thước (size / 크기) thế nào, hiện tại (current / 현재) phụ thuộc voltage như thế nào, hay concentration thay đổi theo reaction tỷ lệ (rate / 비율) ra sao.

**Differential equation (미분방정식)** là phương trình chứa một unknown hàm (function / 함수) cùng derivatives của nó. Solution là hàm (function / 함수) có hành vi (behavior / 동작) phù hợp với cục bộ (local / 로컬) law ở mọi điểm (point / 지점) trong lĩnh vực (domain / 도메인).

Ý tưởng cốt lõi là:

```text
local rule of change + initial/boundary information → global behavior
```

## Ordinary differential equation

Một **ordinary differential equation — ODE (상미분방정식)** có một independent variable, thường là thời gian (time / 시간).

First-order ODE có dạng

```math
\frac{dy}{dt}=f(t,y).
```

Second-order ODE có thể có dạng

```math
\frac{d^2y}{dt^2}=f(t,y,y').
```

Thứ tự (order / 순서) của ODE là thứ tự (order / 순서) cao nhất của derivative xuất hiện.

## Initial giá trị (value / 값) bài toán (problem / 문제)

Equation thường cho một family solutions. Initial điều kiện (condition / 조건) chọn trajectory cụ thể.

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

Pair của differential equation và initial điều kiện (condition / 조건) gọi là **initial giá trị (value / 값) bài toán (problem / 문제) — IVP**.

## Existence và uniqueness

Không phải every differential equation với initial điều kiện (condition / 조건) đều có unique solution.

Một important theorem, Picard–Lindelöf, nói roughly rằng nếu `f(t,y)` continuous và sufficiently Lipschitz theo `y` quanh initial điểm (point / 지점), IVP

```math
y'=f(t,y),\qquad y(t_0)=y_0
```

có cục bộ (local / 로컬) unique solution.

Điểm thực dụng là: trước khi “giải” equation, cần biết bài toán (problem / 문제) có well-defined solution hay không.

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

nói **absolute growth tỷ lệ (rate / 비율) proportional to hiện tại (current / 현재) amount**.

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

Exponential không phải arbitrary curve; nó là unique shape có relative tỷ lệ (rate / 비율) constant.

## First-order tuyến tính (linear / 선형) ODE

General form:

```math
y'+p(t)y=q(t).
```

Integrating factor là

```math
\mu(t)=e^{\int p(t)dt}.
```

Nhân equation với `μ` biến left side thành derivative của sản phẩm (product / 제품):

```math
(\mu y)'=\mu q.
```

Do đó

```math
\mu y=\int \mu q\,dt+C.
```

Phương thức (method / 메서드) này xuất hiện trong RC circuits, mixing các mô hình (models / 모델들) và tuyến tính (linear / 선형) phản hồi (response / 응답) các hệ thống (systems / 시스템들).

## Equilibrium points

Với autonomous equation

```math
y'=f(y),
```

equilibrium `y*` thỏa

```math
f(y^*)=0.
```

Nếu hệ thống (system / 시스템) bắt đầu đúng tại equilibrium, derivative bằng 0 nên trạng thái (state / 상태) không đổi.

Nhưng quan trọng hơn là **stability**: nếu perturb nhẹ khỏi equilibrium, trajectory quay lại hay đi xa?

## Phase line

Trong one-dimensional autonomous hệ thống (system / 시스템), sign của `f(y)` cho direction motion.

Nếu `f(y)>0`, trạng thái (state / 상태) tăng. Nếu `f(y)<0`, trạng thái (state / 상태) giảm.

Plot signs trên number line giúp classify equilibria mà không cần closed-form solution.

Stable equilibrium hút nearby trajectories; unstable equilibrium đẩy chúng ra xa.

## Logistic growth

Resource-limited mô hình quần thể (population model / 개체군 모델):

```math
P'=rP\left(1-\frac PK\right).
```

Equilibria là

```math
P=0,\qquad P=K.
```

Khi `0<P<K`, growth positive. Khi `P>K`, derivative negative.

`K` là carrying sức chứa (capacity / 용량) và là stable equilibrium cho positive initial populations trong idealized mô hình (model / 모델).

Logistic mô hình (model / 모델) giải thích vì sao exponential growth thường chỉ là cục bộ (local / 로컬) approximation ở giai đoạn đầu.

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

Oscillation xuất hiện vì acceleration luôn kéo trạng thái (state / 상태) về equilibrium.

## Characteristic equation

Tuyến tính (linear / 선형) constant-coefficient ODE

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

Repeated gốc (root / 루트) tạo term `te^{rt}`.

Complex roots

```math
r=\alpha\pm i\beta
```

cho oscillation với envelope `e^{\alpha t}`.

Đây là liên kết (connection / 연결) trực tiếp giữa algebraic roots và động (dynamic / 동적) hành vi (behavior / 동작).

## Damped oscillator

Mô hình (model / 모델)

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

phân loại hành vi (behavior / 동작).

Nếu negative, roots complex và hệ thống (system / 시스템) underdamped: oscillation decay dần.

Nếu zero, trọng yếu (critical / 중요) damping: return nhanh mà không oscillate trong ideal mô hình (model / 모델).

Nếu positive, overdamped: two real decay modes.

## Forced các hệ thống (systems / 시스템들) và resonance

Nếu có bên ngoài (external / 외부) đầu vào (input / 입력):

```math
mx''+cx'+kx=F(t).
```

Solution thường gồm transient thành phần (component / 컴포넌트) và forced/steady-state thành phần (component / 컴포넌트).

Nếu forcing frequency gần natural frequency và damping nhỏ, phản hồi (response / 응답) amplitude có thể lớn: **resonance**.

Resonance là động (dynamic / 동적) consequence của frequency matching, không chỉ là “rung mạnh”.

## Các hệ thống (systems / 시스템들) of ODEs

Nhiều các hệ thống (systems / 시스템들) cần véc-tơ (vector / 벡터) trạng thái (state / 상태):

```math
\frac{d\mathbf x}{dt}=F(t,\mathbf x).
```

Tuyến tính (linear / 선형) autonomous hệ thống (system / 시스템):

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

Mỗi eigenvalue tạo một động (dynamic / 동적) chế độ (mode / 모드) `e^{\lambda t}`.

## Stability và eigenvalues

Với continuous hệ tuyến tính (linear system / 선형 시스템)

```math
x'=Ax,
```

nếu mọi eigenvalues có negative real part, origin asymptotically stable.

Nếu có eigenvalue với positive real part, có direction grow exponentially và origin unstable.

Imaginary parts tạo oscillation; real parts tạo growth/decay envelope.

Đây là lý do eigenvalues là ngôn ngữ (language / 언어) trung tâm của điều khiển (control / 제어) lý thuyết (theory / 이론).

## Nonlinear các hệ thống (systems / 시스템들) và linearization

Cho

```math
x'=F(x).
```

Near equilibrium `x*`, Taylor approximation cho

```math
F(x)\approx F(x^*)+J_F(x^*)(x-x^*).
```

Vì equilibrium thỏa `F(x*)=0`, cục bộ (local / 로컬) dynamics gần đó gần giống

```math
\delta x'=J_F(x^*)\delta x.
```

Eigenvalues của Jacobian giúp classify cục bộ (local / 로컬) stability trong nhiều cases.

Điều này nối nonlinear differential equations với ma trận (matrix / 행렬) calculus và eigenanalysis.

## Phase plane

Với two-dimensional hệ thống (system / 시스템), thay vì plot variables theo thời gian (time / 시간), ta plot trajectory trong trạng thái (state / 상태) không gian (space / 공간) `(x,y)`.

Phase portrait cho thấy equilibria, closed orbits, separatrices và luồng (flow / 흐름) hình học (geometry / 기하학).

Hai trajectories của deterministic ODE với unique solutions không thể cross tại cùng trạng thái (state / 상태)/time-independent véc-tơ (vector / 벡터) trường dữ liệu (field / 필드), vì crossing sẽ imply hai futures từ cùng trạng thái (state / 상태).

## Conservation laws

Một differential equation có thể preserve quantity `E(x)` dọc trajectory:

```math
\frac d{dt}E(x(t))=0.
```

Trong undamped mechanical hệ thống (system / 시스템), total năng lượng (energy / 에너지) thường conserved.

Conserved quantities constrain trajectories vào mức (level / 수준) sets và có thể simplify phân tích (analysis / 분석) mạnh.

## Ranh giới (boundary / 경계) giá trị (value / 값) problems

Không phải mọi bài toán (problem / 문제) cho conditions tại một single initial thời gian (time / 시간).

Ví dụ

```math
y''+\lambda y=0,
```

với

```math
y(0)=0,\qquad y(L)=0
```

là ranh giới (boundary / 경계) giá trị (value / 값) bài toán (problem / 문제).

Chỉ một số values của `λ` cho nontrivial solutions. Đây là origin của eigenvalue problems trong PDE và quantum mechanics.

## Numerical solution

Nhiều ODE không có elementary closed form hoặc hệ thống (system / 시스템) quá phức tạp để giải symbolic.

Euler phương thức (method / 메서드) dùng cục bộ (local / 로컬) tangent:

```math
x_{n+1}=x_n+h f(t_n,x_n).
```

Nó là first-order phương thức (method / 메서드): toàn cục (global / 전역) lỗi (error / 오류) thường proportional `h` dưới suitable các giả định (assumptions / 가정들).

## Runge–Kutta intuition

Euler chỉ lấy slope đầu interval. Runge–Kutta methods mẫu (sample / 표본) multiple slopes trong step để estimate average slope tốt hơn.

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

## Cục bộ (local / 로컬) lỗi (error / 오류) và toàn cục (global / 전역) lỗi (error / 오류)

Cục bộ (local / 로컬) truncation lỗi (error / 오류) đo lỗi (error / 오류) tạo trong một step nếu starting giá trị (value / 값) chính xác (exact / 정확한).

Toàn cục (global / 전역) lỗi (error / 오류) là accumulated lỗi (error / 오류) sau nhiều steps.

Một phương thức (method / 메서드) cục bộ (local / 로컬) rất chính xác vẫn cần stability để lỗi (error / 오류) không amplify qua repeated steps.

## Stiff equations

Một ODE gọi là **stiff** khi có nhiều thời gian (time / 시간) scales rất khác nhau làm tường minh (explicit / 명시적) methods cần extremely small step để remain stable, dù solution itself có thể smooth.

Ví dụ chemical kinetics có fast reactions và slow processes cùng tồn tại.

Implicit methods như backward Euler thường stable hơn cho stiff problems.

## Backward Euler

Backward Euler dùng

```math
x_{n+1}=x_n+h f(t_{n+1},x_{n+1}).
```

Unknown `x_{n+1}` xuất hiện cả hai vế, nên mỗi step có thể cần solve nonlinear equation.

Đổi lại, phương thức (method / 메서드) có stronger stability properties.

## Adaptive step kích thước (size / 크기)

Fixed step `h` có thể waste computation ở smooth regions và thiếu accuracy ở rapidly changing regions.

Adaptive solvers estimate cục bộ (local / 로컬) lỗi (error / 오류) rồi tự tăng/giảm step kích thước (size / 크기) để đạt tolerance mục tiêu (target / 대상).

Hiện đại (modern / 현대적) ODE solvers thường ưu tiên tolerance hơn việc người dùng chọn một `h` cứng.

## Sự kiện (event / 이벤트) detection

Trong simulation, ta đôi khi quan tâm thời điểm solution cross threshold, va chạm hoặc switch regime.

Solver cần locate sự kiện (event / 이벤트) thời gian (time / 시간) giữa numerical steps, thường bằng interpolation/gốc (root / 루트) finding, thay vì chỉ kiểm tra discrete sampled times.

## Dimensionless variables

Scaling variables có thể reveal key dimensionless parameters và improve numerical conditioning.

Ví dụ thay

```math
t=\tau T,
```

có thể biến constants thành ratios thể hiện relative thời gian (time / 시간) scales.

Non-dimensionalization giúp so sánh các hệ thống (systems / 시스템들) khác units và nhận ra dominant mechanisms.

## Differential equations và Laplace transform

Tuyến tính (linear / 선형) ODE với initial conditions có thể transform thành algebraic equation trong `s` lĩnh vực (domain / 도메인).

Ví dụ differentiation trở thành multiplication by `s` cộng initial-condition terms.

Điều này hữu ích cho tuyến tính (linear / 선형) time-invariant các hệ thống (systems / 시스템들) và điều khiển (control / 제어), đặc biệt khi đầu vào (input / 입력) có steps/impulses.

## Differential equations và xác suất (probability / 확률)

Stochastic differential equations thêm random forcing, schematic:

```math
dX_t=\mu(X_t,t)dt+\sigma(X_t,t)dW_t.
```

Ordinary calculus không đủ vì Brownian paths không differentiable theo classical sense; stochastic calculus phát triển rules mới.

Đây là cầu nối (bridge / 브리지) từ deterministic dynamics sang stochastic processes.

## Differential equations và machine học tập (learning / 학습)

Continuous-depth neural networks như Neural ODEs xem hidden trạng thái (state / 상태) evolution là

```math
\frac{dh}{dt}=f_\theta(t,h).
```

Huấn luyện (training / 학습) cần differentiate through numerical ODE solution.

Dù hiện thực (implementation / 구현) hiện đại, underlying mathematics vẫn là hệ động (dynamic system / 동적 시스템), numerical tích hợp (integration / 통합) và sensitivity phân tích (analysis / 분석).

## Mô hình tư duy (mental model / 사고 모델)

Differential equation là một **generator của trajectories**. Nó chỉ cục bộ (local / 로컬) velocity của trạng thái (state / 상태) tại mỗi điểm (point / 지점). Initial điều kiện (condition / 조건) đặt hệ thống (system / 시스템) vào một điểm (point / 지점); véc-tơ (vector / 벡터) trường dữ liệu (field / 필드) nói nó phải đi direction nào; tích hợp (integration / 통합) qua thời gian (time / 시간) tạo toàn cục (global / 전역) trajectory.

Tuyến tính (linear / 선형) các hệ thống (systems / 시스템들) có thể tách thành eigenmodes. Nonlinear các hệ thống (systems / 시스템들) thường được hiểu cục bộ (local / 로컬) bằng linearization, toàn cục (global / 전역) bằng phase hình học (geometry / 기하학), invariants và numerical simulation.

## Dùng chung (common / 공통) Misconceptions

Có differential equation chưa chắc có unique solution; conditions về regularity và initial/ranh giới (boundary / 경계) dữ liệu (data / 데이터) matters. Có closed-form expression cũng không có nghĩa mô hình (model / 모델) đúng về vật lý (physical / 물리적) hệ thống (system / 시스템).

Numerical solver không “giải chính xác bằng máy tính”. Nó tạo approximation với truncation, floating-point và modeling errors.

Giảm step kích thước (size / 크기) không luôn chữa mọi vấn đề; stiff các hệ thống (systems / 시스템들) cần stability-aware methods.

Eigenvalue stability criteria của linearization là cục bộ (local / 로컬) statements cho nonlinear các hệ thống (systems / 시스템들) và có edge cases khi eigenvalues nằm trên imaginary axis.

## Liên kết kiến thức

Chapter này nối [Integrals](./03_integrals_and_accumulation.md), [Eigenvalues](../04_vectors_linear_algebra/04_eigenvalues_and_eigenvectors.md), [Taylor approximation](./08_taylor_series_and_local_approximation.md), [PDE](./10_partial_differential_equations_and_fields_intro.md), [Laplace/Z-transform](../09_connections/06_laplace_z_transform_and_dynamic_systems.md), [Stochastic processes](../06_probability_statistics/11_stochastic_processes_markov_chains_and_time_series.md) và [Dynamic programming/optimal control](../08_optimization_numerical/06_dynamic_programming_bellman_and_optimal_control.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 limits and continuity](./00_limits_and_continuity.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
