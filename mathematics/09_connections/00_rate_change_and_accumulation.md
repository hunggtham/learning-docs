# Knowledge Connection — Rate, Change và Accumulation: từ difference đến conservation

Một pattern xuất hiện xuyên suốt calculus, physics, finance, probability, data systems và optimization là:

```text
state
↔ local change
↔ accumulated change
```

Nếu không nhận ra pattern này, derivative, integral, difference equation, throughput, marginal cost và probability density dễ trông như các khái niệm rời rạc. Thực ra chúng thường là những phiên bản khác nhau của cùng một structure.

## 1. State và change trả lời hai câu hỏi khác nhau

Giả sử quantity `x(t)` thay đổi theo thời gian.

`x(t)` trả lời:

```text
state hiện tại là bao nhiêu?
```

Difference:

```math
\Delta x=x(t_2)-x(t_1)
```

trả lời:

```text
state đã thay đổi bao nhiêu trên interval?
```

Average rate:

```math
\frac{\Delta x}{\Delta t}
```

trả lời:

```text
mỗi unit time, trung bình state thay đổi bao nhiêu?
```

Units giúp phân biệt ba quantities này.

Nếu `x` đo bằng meter:

```text
x           → m
Δx          → m
Δx/Δt       → m/s
```

Rate không phải total.

## 2. Derivative là local linear response

Instantaneous rate được formalize bằng limit:

```math
x'(t)=\lim_{h\to0}\frac{x(t+h)-x(t)}{h}.
```

Nhưng mental model tốt hơn “slope formula” là local approximation:

```math
x(t+h)\approx x(t)+x'(t)h.
```

Derivative nói nếu input đổi một amount rất nhỏ thì output phản ứng first-order ra sao.

Đây là lý do cùng concept xuất hiện dưới nhiều names:

```text
velocity
marginal cost
sensitivity
gradient
Jacobian
growth rate
```

## 3. Accumulation là inverse question

Nếu biết rate `r(t)`, accumulated change trên `[a,b]` là:

```math
\int_a^b r(t)\,dt.
```

Nếu:

```math
x'(t)=r(t),
```

thì:

```math
x(b)-x(a)=\int_a^b r(t)\,dt.
```

Đây là Fundamental Theorem of Calculus nhìn như accounting law:

> cộng tất cả local changes cho ra net global change.

## 4. Vì sao dấu quan trọng?

Integral của rate là **net accumulation**, không luôn là total amount traveled.

Nếu velocity đổi dấu:

```math
\int v(t)dt
```

cho displacement.

Distance traveled cần:

```math
\int |v(t)|dt.
```

Cùng logic trong finance: signed cash flow netting khác gross transaction volume.

## 5. Discrete analogue: difference và summation

Với sequence `a_n`:

```math
\Delta a_n=a_{n+1}-a_n.
```

Summing:

```math
\sum_{n=m}^{N-1}\Delta a_n
=a_N-a_m.
```

Middle terms cancel. Đây là telescoping sum — discrete version của Fundamental Theorem.

Mental mapping:

```text
derivative ↔ finite difference
integral   ↔ summation
ODE        ↔ recurrence relation
```

## 6. Recurrence là rate law cho discrete time

Nếu:

```math
a_{n+1}=a_n+r,
```

mỗi step cộng constant amount, nên:

```math
a_n=a_0+nr.
```

Nếu:

```math
a_{n+1}=qa_n,
```

mỗi step scale theo current state:

```math
a_n=a_0q^n.
```

Additive update sinh linear behavior; multiplicative update sinh exponential behavior.

Đây là discrete counterpart của:

```math
x'=k
```

và:

```math
x'=kx.
```

## 7. Density cũng là rate of accumulation

Probability density `f(x)` không phải probability tại một point.

CDF:

```math
F(x)=P(X\le x)
```

là accumulated probability.

Khi differentiable:

```math
F'(x)=f(x).
```

Và:

```math
P(a\le X\le b)=\int_a^b f(x)dx.
```

Pattern hoàn toàn giống:

```text
local density
→ integrate
→ accumulated mass
```

## 8. Throughput và queue length

Trong system engineering, queue length `Q(t)` là state.

Arrival rate `λ(t)` và service rate `μ(t)` cho local change roughly:

```math
Q'(t)\approx \lambda(t)-\mu(t)
```

khi dùng continuous approximation.

Nếu arrival > service lâu dài, backlog tích lũy.

Một dashboard chỉ nhìn throughput mà không nhìn accumulated queue có thể bỏ lỡ overload đang tích tụ.

## 9. Finance: balance là accumulated cash flow

Nếu `B(t)` là account balance và `c(t)` là net cash-flow rate:

```math
B'(t)=c(t)
```

thì:

```math
B(T)=B(0)+\int_0^T c(t)dt.
```

Nếu balance tự sinh interest proportional với current balance:

```math
B'(t)=rB(t),
```

solution exponential:

```math
B(t)=B_0e^{rt}.
```

Rate law quyết định accumulation shape.

## 10. Marginal vs total trong economics

Nếu total cost là `C(q)`, marginal cost:

```math
C'(q)
```

là local cost của thêm một unit production.

Net total change từ `q_1` tới `q_2`:

```math
C(q_2)-C(q_1)
=\int_{q_1}^{q_2}C'(q)dq.
```

Mistake phổ biến là đọc marginal quantity như average hoặc total quantity.

## 11. Gradient là vector của local rates

Với multivariable function:

```math
L(\theta_1,\ldots,\theta_n),
```

gradient:

```math
\nabla L=
\begin{bmatrix}
\partial L/\partial\theta_1\\
\vdots\\
\partial L/\partial\theta_n
\end{bmatrix}
```

collect local sensitivities.

Directional derivative:

```math
D_uL=\nabla L\cdot u.
```

nói loss thay đổi nhanh thế nào nếu parameters move theo direction `u`.

## 12. Gradient descent là tích lũy các local decisions

Update:

```math
\theta_{k+1}=\theta_k-\eta\nabla L(\theta_k)
```

là discrete trajectory.

Mỗi step dùng local rate information; toàn bộ training path là accumulated result của many local updates.

Trong limit step nhỏ, ta gặp gradient flow:

```math
\frac{d\theta}{dt}=-\nabla L(\theta).
```

Optimization nối recurrence với differential equations.

## 13. Differential equation: biết law của change, reconstruct state

ODE:

```math
x'=F(x,t)
```

không cho state trực tiếp. Nó cho **law of change**.

Solving ODE nghĩa reconstruct trajectory consistent với local law + initial condition.

PDE mở rộng idea này sang field:

```text
local law at every point
→ global field evolution
```

## 14. Conservation law là accounting ở cấp field

Nếu density `ρ(x,t)` và flux `J(x,t)` satisfy:

```math
\frac{\partial \rho}{\partial t}
+\nabla\cdot J=0,
```

thì local density chỉ thay đổi vì flow đi vào/ra.

Integrate over region `V`:

```math
\frac{d}{dt}\int_V\rho\,dV
=-\int_{\partial V}J\cdot n\,dS.
```

Accumulated amount bên trong thay đổi bằng net boundary flow.

Đây là continuous accounting principle nằm dưới mass, charge, probability và fluid conservation.

## 15. Local-to-global là pattern lớn hơn calculus

Nhiều theorem có structure:

```text
local quantity
→ integrate/sum
→ global statement
```

Ví dụ:

```text
derivative → net change
curl → circulation
ndivergence → flux
local loss → empirical risk
per-step cost → total dynamic-programming cost
```

Nhận ra pattern này giúp transfer intuition giữa domains.

## 16. Units như sanity check

Nếu rate có units:

```text
requests / second
```

integrating over seconds phải cho:

```text
requests
```

Nếu derivative:

```math
\frac{dB}{dt}
```

có units KRW/day thì multiplying by a time interval cho KRW.

Dimensional analysis thường bắt được confusion giữa state và rate trước cả algebra.

## 17. Continuous model là approximation của discrete reality

People, packets và database rows là discrete.

Derivative model có thể hữu ích khi scale lớn và changes smooth enough, nhưng exact microscopic process vẫn discrete.

Ví dụ average request rate 1000 req/s không nghĩa mỗi millisecond có đúng 1 request.

Continuous approximation smooths randomness và granularity.

## 18. Common failure modes

### Endpoint-only thinking

Average rate giữa hai endpoints không reveal spikes bên trong interval.

### Confusing signed and absolute accumulation

Net change có cancellation; total activity có thể không.

### Treating derivative as global trend

Local derivative tại một point không đảm bảo same slope far away.

### Ignoring state dependence

Rate có thể depend on state, tạo nonlinear feedback.

### Integrating a wrong model

Precise accumulation của wrong rate law vẫn cho wrong result.

## Knowledge Connection

```text
Algebra      → finite difference
Calculus     → derivative/integral
Probability  → density/CDF
Optimization → gradient/update trajectory
ODE/PDE      → local law → global state
Finance      → cash flow → balance
Systems      → throughput → queue/backlog
Physics      → velocity/flux → conserved quantity
```

## Mental Model

> Mỗi khi gặp một quantity, hỏi: đây là state, local rate hay accumulated total? Nếu biết state, derivative/difference nói nó đang đổi thế nào. Nếu biết rate, sum/integral reconstruct net accumulation. Rất nhiều công thức khác domain chỉ là cùng accounting structure dưới notation khác nhau.