# Nhập môn phương trình vi phân riêng phần: khi state phụ thuộc vào không gian và thời gian

Ordinary Differential Equation (ODE / 상미분방정식) thường mô tả một state thay đổi theo một biến độc lập, thường là time. Nhưng nhiệt độ trong một căn phòng, áp suất trong chất lỏng, độ cao của sóng hay electric potential không chỉ phụ thuộc time; chúng thay đổi theo vị trí. Khi unknown là một **field / 장** như `u(x,t)` hoặc `u(x,y,z,t)`, laws of change dẫn tự nhiên đến **phương trình vi phân riêng phần (Partial Differential Equation, PDE / 편미분방정식)**.

PDE là một lĩnh vực lớn. Chương này không cố giải toàn bộ PDE theory; mục tiêu là hiểu vì sao PDE xuất hiện, three canonical types, vai trò của boundary/initial conditions và liên hệ với numerical simulation.

## Field: từ một number sang một value tại mỗi point

Một scalar field gán một scalar cho mỗi point. Temperature có thể viết

```math
T=T(x,y,z,t).
```

Một vector field gán vector cho mỗi point, như velocity field của fluid:

```math
\mathbf v=\mathbf v(x,y,z,t).
```

Khi field thay đổi, partial derivatives đo rate theo từng coordinate. `\partial T/\partial t` đo local time change tại fixed position; gradient `\nabla T` mô tả spatial direction mà temperature tăng nhanh nhất.

## Heat equation: diffusion từ local imbalance

Trong một thanh 1D, heat equation điển hình là

```math
\frac{\partial u}{\partial t}
=
\alpha\frac{\partial^2u}{\partial x^2},
```

trong đó `u(x,t)` là temperature và `\alpha` là thermal diffusivity.

Second derivative `u_{xx}` đo curvature của temperature profile. Nếu một point nóng hơn neighbors, profile có curvature theo hướng khiến heat flow làm point đó giảm nhiệt; nếu lạnh hơn neighbors, nó nhận heat. PDE nói local time change proportional với local spatial imbalance.

Đây là **diffusion equation / 확산방정식**. Same mathematical structure mô tả diffusion của particles, smoothing của concentration và một số algorithms làm mờ image.

## Wave equation: propagation thay vì smoothing

Một ideal vibrating string có wave equation

```math
\frac{\partial^2u}{\partial t^2}
=
c^2\frac{\partial^2u}{\partial x^2}.
```

Khác heat equation, time derivative là second order. Nó liên hệ acceleration của displacement với spatial curvature. Kết quả là disturbance có xu hướng propagate như waves thay vì chỉ diffuse away.

Speed `c` xác định propagation speed. Đây là nơi trigonometric functions, complex exponentials và Fourier analysis trở nên tự nhiên: sinusoidal waves là eigenmodes của nhiều linear PDE systems.

## Laplace và Poisson equations: equilibrium fields

Khi system đạt steady state, time derivative có thể biến mất. Heat equation ở equilibrium dẫn đến

```math
\nabla^2u=0,
```

đó là **Laplace equation / 라플라스 방정식**. Nếu có sources,

```math
\nabla^2u=f,
```

ta có **Poisson equation / 푸아송 방정식**.

Các equations này xuất hiện trong electrostatics, gravitation, steady heat flow và potential theory. Operator

```math
\nabla^2
```

là **Laplacian / 라플라시안**, tổng các second partial derivatives theo spatial coordinates.

## Initial conditions và boundary conditions

PDE không được xác định chỉ bởi equation. Ta cần biết state ban đầu và cách domain tương tác với boundary.

Với heat equation, **initial condition / 초기조건** có thể là

```math
u(x,0)=f(x).
```

Một **Dirichlet boundary condition / 디리클레 경계조건** đặt value ở boundary:

```math
u(0,t)=0,
\qquad
u(L,t)=0.
```

Một **Neumann boundary condition / 노이만 경계조건** đặt derivative normal, thường tương ứng với flux:

```math
\frac{\partial u}{\partial n}=0.
```

Điều này có thể biểu diễn insulated boundary — không có heat flow xuyên qua.

Same PDE với boundary conditions khác có thể cho behavior hoàn toàn khác. Vì vậy boundary conditions là một phần của mathematical model, không phải chi tiết phụ sau khi đã “có phương trình”.

## Classification: elliptic, parabolic, hyperbolic

Linear second-order PDE thường được phân loại thành elliptic, parabolic và hyperbolic. Không cần học classification như taxonomy rời rạc; nó phản ánh qualitative behavior.

**Elliptic** equations như Laplace thường mô tả equilibrium; influence có tính global. **Parabolic** equations như heat mô tả diffusion và smoothing theo time. **Hyperbolic** equations như wave mô tả propagation với finite-speed characteristics.

Classification ảnh hưởng cả mathematical theory lẫn numerical method thích hợp.

## Separation of variables và eigenfunctions

Một classical technique là giả sử solution có product form

```math
u(x,t)=X(x)T(t).
```

Thay vào PDE có thể tách problem thành ODEs. Với heat equation,

```math
X(x)T'(t)=\alpha X''(x)T(t).
```

Chia cho `\alpha XT`:

```math
\frac{T'}{\alpha T}=\frac{X''}{X}.
```

Vế trái chỉ phụ thuộc `t`, vế phải chỉ phụ thuộc `x`; để equality giữ cho mọi `x,t`, cả hai phải bằng cùng constant. Ta thu được hai ODEs.

Boundary conditions thường chỉ cho phép một discrete set các spatial modes `X_n`. Đây chính là bridge tới eigenvalues/eigenvectors và Fourier series: arbitrary initial profile được phân rã thành eigenmodes, mỗi mode tiến hóa theo law riêng.

## Numerical PDE: grid hóa không gian và thời gian

Đa số realistic PDE không có closed-form solution dễ dùng. Ta discretize domain thành grid hoặc mesh. Với finite difference, second derivative có approximation

```math
\frac{\partial^2u}{\partial x^2}(x_i)
\approx
\frac{u_{i+1}-2u_i+u_{i-1}}{\Delta x^2}.
```

Heat equation trở thành update rule trên array values. Đây là điểm PDE gặp numerical linear algebra, sparse matrices, parallel computing và GPU.

Nhưng discretization tạo thêm questions về **stability / 안정성**, **consistency / 일관성** và **convergence / 수렴성**. Một scheme nhìn hợp lý về algebra có thể explode numerically nếu timestep quá lớn. Ví dụ explicit heat scheme thường có stability restriction liên hệ `\Delta t` với `\Delta x^2`.

## PDE trong graphics, ML và engineering

Computer graphics dùng PDE trong fluid simulation, cloth, diffusion và image processing. Computational fluid dynamics giải Navier–Stokes equations trên meshes. Finance dùng PDE như Black–Scholes dưới certain assumptions. Physics-informed neural networks đưa PDE residual vào loss function, biến differential law thành training constraint.

Trong image processing, diffusion-like PDE có thể smooth noise. Nhưng isotropic diffusion cũng làm mờ edges; nonlinear diffusion cố preserve important boundaries. Đây là ví dụ rõ rằng mathematical model quyết định loại information bị giữ hay mất.

## Knowledge Connection

PDE ngồi ở intersection của multivariable calculus, vector calculus, linear algebra, Fourier analysis, differential equations và numerical methods. Gradient/divergence/curl mô tả fields; eigenfunctions cung cấp natural modes; Fourier đổi representation; sparse matrices xuất hiện sau discretization; optimization xuất hiện trong variational formulations.

Một powerful viewpoint là xem PDE như “local law applied everywhere”. ODE nói state tại một point in state-space thay đổi theo law; PDE nói field tại mọi spatial point thay đổi theo local differential relationships và bị coupled qua neighbors.

## Mental Model

> PDE là cách viết một luật local cho một field trải trên không gian. Differential operator đo local shape hoặc flux; boundary/initial conditions xác định environment; solution là global behavior xuất hiện khi cùng local law được thỏa ở mọi point.

## Common Misconceptions

PDE không đơn giản là ODE “có nhiều biến hơn”. Spatial coupling, boundaries và function spaces làm problem qualitatively khác.

Có PDE và boundary conditions chưa chắc luôn có unique smooth solution; existence, uniqueness và regularity là questions riêng. Numerical solution cũng không tự động là solution thật: cần analyze discretization error và stability.

Cuối cùng, Fourier methods không “giải mọi PDE”. Chúng đặc biệt mạnh với linear systems và regular domains/boundaries; nonlinearities, irregular geometry hoặc changing boundaries có thể yêu cầu methods khác.
