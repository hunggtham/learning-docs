# Laplace transform, Z-transform và cách nhìn hệ động lực qua domain khác

Fourier analysis đổi representation từ time/space domain sang frequency domain. Hai transforms liên quan rất quan trọng cho systems engineering là **Laplace transform / 라플라스 변환** cho continuous-time systems và **Z-transform / Z변환** cho discrete-time systems.

Mục tiêu của transforms không phải làm signal “khác đi”, mà chọn coordinates nơi differentiation, convolution hoặc recurrence trở nên algebraically đơn giản hơn.

## Laplace transform

Với function `f(t)` cho `t≥0`, Laplace transform được định nghĩa

```math
F(s)=\mathcal L\{f(t)\}
=\int_0^\infty f(t)e^{-st}\,dt,
```

trong đó `s` thường là complex number

```math
s=\sigma+i\omega.
```

Factor `e^{-st}=e^{-\sigma t}e^{-i\omega t}` kết hợp exponential decay/growth weighting với oscillation. Fourier transform có thể xem là special slice `\sigma=0` khi convergence cho phép.

## Vì sao derivative biến thành algebra

Một property trung tâm:

```math
\mathcal L\{f'(t)\}
=sF(s)-f(0).
```

Second derivative:

```math
\mathcal L\{f''(t)\}
=s^2F(s)-sf(0)-f'(0).
```

Do đó differential equation trong time domain biến thành algebraic equation theo `s`.

Ví dụ ODE

```math
y'+ay=u(t),
\qquad y(0)=y_0
```

sau Laplace transform:

```math
sY(s)-y_0+aY(s)=U(s).
```

Suy ra

```math
Y(s)=\frac{U(s)+y_0}{s+a}.
```

Ta có thể inverse transform để recover `y(t)`.

Đây là một change of representation giống diagonalization trong linear algebra: operator differentiation trở nên gần như multiplication by `s`.

## Transfer function

Với linear time-invariant system và zero initial conditions, **transfer function / 전달함수** là ratio

```math
H(s)=\frac{Y(s)}{U(s)}.
```

Nếu system obeys

```math
a_2y''+a_1y'+a_0y
=b_1u'+b_0u,
```

thì

```math
H(s)
=
\frac{b_1s+b_0}{a_2s^2+a_1s+a_0}.
```

Roots của denominator gọi là **poles / 극점**, roots của numerator là **zeros / 영점**. Pole locations encode natural modes và stability properties.

## Stability và poles

Continuous-time LTI system có impulse response terms kiểu `e^{pt}` từ poles `p`. Nếu real part của pole negative, mode decays. Nếu positive, mode grows exponentially. Poles trên imaginary axis cần xét kỹ multiplicity và context.

Do đó left half of complex `s`-plane liên hệ stable decay. Complex numbers ở đây không phải decorative abstraction; chúng encode simultaneous decay rate và oscillation frequency.

## Convolution thành multiplication

Laplace transform biến convolution thành product:

```math
\mathcal L\{f*g\}=F(s)G(s).
```

Time-domain output của LTI system

```math
y=h*u
```

trở thành

```math
Y(s)=H(s)U(s).
```

Đây là cùng principle như Fourier transform: convolution operator được diagonalize bởi exponential basis.

## Z-transform cho discrete time

Với sequence `x[n]`, bilateral Z-transform là

```math
X(z)=\sum_{n=-\infty}^{\infty}x[n]z^{-n}.
```

One-sided version thường dùng cho causal systems và recurrence với initial conditions.

Shift property rất quan trọng. Delay một sample tương ứng multiplication bởi `z^{-1}`. Vì vậy recurrence relations biến thành algebraic equations theo `z`.

Ví dụ difference equation

```math
y[n]-ay[n-1]=x[n]
```

với zero initial state cho

```math
Y(z)-az^{-1}Y(z)=X(z).
```

Do đó transfer function

```math
H(z)=\frac{Y(z)}{X(z)}
=\frac{1}{1-az^{-1}}.
```

## Unit circle và Fourier connection

Discrete-time Fourier transform xuất hiện khi evaluate Z-transform trên unit circle

```math
z=e^{i\omega}.
```

Nếu region of convergence chứa unit circle, frequency response là

```math
H(e^{i\omega}).
```

Vì thế Z-transform chứa cả growth/decay information theo radius `|z|` và oscillation theo angle.

## Poles và stability trong discrete systems

Mode kiểu `a^n` decay nếu

```math
|a|<1.
```

Do đó causal discrete LTI system rational thường stable khi poles nằm inside unit circle. Continuous system dùng left half-plane; discrete system dùng unit disk. Mapping giữa hai worlds có thể thực hiện bằng transformations như bilinear transform.

## State-space và eigenvalues

Dynamic system dạng

```math
\dot x=Ax+Bu
```

có natural behavior liên hệ eigenvalues của `A`. Laplace transform cho

```math
(sI-A)X(s)=BU(s)+x(0).
```

Matrix inverse

```math
(sI-A)^{-1}
```

là resolvent; poles liên hệ eigenvalues của `A`. Đây là bridge trực tiếp giữa linear algebra và control theory.

Discrete-time system

```math
x_{n+1}=Ax_n+Bu_n
```

ổn định theo analogous sense khi eigenvalues liên quan nằm inside unit circle.

## Filters trong software và signal processing

Digital filters được implement bằng difference equations. FIR filter có finite impulse response; IIR filter có feedback và theoretically infinite response. Z-domain giúp analyze frequency response và stability trước khi code.

Moving average filter là convolution đơn giản. Exponential moving average

```math
y[n]=\alpha x[n]+(1-\alpha)y[n-1]
```

là first-order IIR filter. Nó xuất hiện không chỉ trong DSP mà cả metrics smoothing, finance và optimizer statistics.

## Knowledge Connection

Laplace/Z-transform nối differential equations, recurrence relations, complex numbers, Fourier analysis, convolution, eigenvalues và control systems. Về mặt mental model, đây là một ví dụ nữa của strategy cực mạnh trong mathematics: đổi basis/representation để operator khó biến thành multiplication dễ.

Fourier hỏi system phản ứng với pure frequencies thế nào. Laplace mở rộng bằng exponential growth/decay. Z-transform làm analogous job cho discrete-time sequences.

## Mental Model

> Transform domain giống như đổi tọa độ cho một bài toán động. Trong time domain ta thấy derivative, convolution và recurrence. Trong Laplace/Z domain, chúng thường biến thành multiplication, rational functions và pole-zero geometry. Ta không né dynamics; ta chọn representation nơi dynamics lộ structure dễ thao tác hơn.

## Common Misconceptions

Laplace transform không chỉ là bảng công thức inverse transforms. Giá trị thật nằm ở operator properties, initial conditions, region of convergence và pole structure.

Pole ở đâu quyết định stability chỉ khi assumptions về system và region of convergence phù hợp. Không nên dùng rule “pole inside/outside” ngoài đúng continuous/discrete setting.

Fourier, Laplace và Z-transform không interchangeable một cách vô điều kiện. Chúng có domains, convergence conditions và purposes khác nhau dù liên hệ chặt chẽ.

## Liên kết kiến thức

Prerequisite trực tiếp gồm [Complex Numbers](../01_algebra/05_complex_numbers.md), [Sequences, Series and Recurrence](../02_functions/03_sequences_series_and_recurrence.md), [Differential Equations](../05_calculus/05_differential_equations.md) và [Eigenvalues/Eigenvectors](../04_vectors_linear_algebra/04_eigenvalues_and_eigenvectors.md).

Để hiểu basis/frequency viewpoint trước khi học pole-zero geometry, đọc [Fourier, Signals and Frequency](./05_fourier_signals_and_frequency.md). Với control/decision dynamics, đọc tiếp [Dynamic Programming, Bellman and Optimal Control](../08_optimization_numerical/06_dynamic_programming_bellman_and_optimal_control.md). Numerical implementation và stability caveats nối với [Numerical Methods and Error](../08_optimization_numerical/02_numerical_methods_and_error.md).
