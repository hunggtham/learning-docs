# Phương trình vi phân: luật của sự thay đổi

Phương trình vi phân (Differential Equation / 미분방정식) không trực tiếp nói state là bao nhiêu; nó nói state phải thay đổi theo rule nào. Đây là language tự nhiên của dynamic systems.

## ODE

Ordinary Differential Equation có independent variable thường là time:

```math
\frac{dy}{dt}=f(t,y)
```

Một initial condition

```math
y(t_0)=y_0
```

chọn trajectory cụ thể trong family solutions.

## Exponential growth

Nếu growth rate proportional amount:

```math
\frac{dP}{dt}=kP
```

separate variables:

```math
\frac{dP}{P}=kdt
```

integrate:

```math
\ln|P|=kt+C
```

exponentiate:

```math
P=Ce^{kt}
```

initial value `P(0)=P_0` cho

```math
P(t)=P_0e^{kt}
```

Exponential xuất hiện từ local law “relative growth rate constant”.

## Decay và half-life

Với `k<0`:

```math
P=P_0e^{-\lambda t}
```

Half-life `T` thỏa

```math
e^{-\lambda T}=\frac12
```

nên

```math
T=\frac{\ln2}{\lambda}.
```

## Logistic equation

Resource-limited growth:

```math
\frac{dP}{dt}=rP\left(1-\frac PK\right)
```

có equilibria `P=0,K`. Factor `(1-P/K)` làm growth slow khi population gần capacity.

## Second-order dynamics

Spring-mass ideal:

```math
mx''+kx=0
```

hay

```math
x''+\omega^2x=0
```

với `ω²=k/m`. Solutions sinusoidal, nối differential equations với trigonometry và eigenmodes.

Thêm damping:

```math
mx''+cx'+kx=0
```

behavior phụ thuộc parameters: underdamped oscillation, critical damping, overdamped return.

## Systems of ODEs

State vector `x`:

```math
\frac{d\mathbf x}{dt}=A\mathbf x
```

solution structure liên quan eigenvalues/eigenvectors của `A`. Eigenvalues quyết định growth/decay/oscillation modes.

Control theory và stability analysis dựa sâu vào connection này.

## Numerical solution

Nhiều ODE không có closed form. Euler method:

```math
x_{n+1}=x_n+h f(t_n,x_n)
```

là repeated local linear step. Smaller `h` thường giảm truncation error nhưng tăng work và floating effects; sophisticated Runge–Kutta methods improve accuracy/stability.

## Mental Model

> Differential equation mô tả local law of motion; solution là global trajectory được sinh ra khi law đó được tuân theo ở mọi instant. Parameters và initial conditions quyết định trajectory cụ thể.

## Common Misconceptions

Có equation chưa đủ chọn unique solution nếu thiếu initial/boundary conditions. Closed-form solution không phải lúc nào tồn tại. Numerical solution là approximation và stability có thể quan trọng hơn chỉ giảm step size.
