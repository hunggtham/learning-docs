# Tích phân: accumulation, area, expectation và tổng liên tục

Đạo hàm trả lời câu hỏi local: tại một điểm, quantity đang thay đổi nhanh thế nào? **Tích phân (Integral / 적분)** trả lời câu hỏi global: nếu có vô số contributions nhỏ dọc theo một interval, surface, time period hoặc probability space, tổng effect là bao nhiêu?

Cách hiểu đúng nhất không phải “tích phân là diện tích”. Diện tích chỉ là một interpretation đặc biệt. Tích phân là **continuous accumulation**.

## Từ tổng hữu hạn đến integral

Giả sử ta biết một density `f(x)` và muốn tính total amount trên `[a,b]`.

Chia interval thành các phần nhỏ

```math
[a,b]=[x_0,x_1]\cup\cdots\cup[x_{n-1},x_n].
```

Trong subinterval thứ `i`, width là

```math
\Delta x_i=x_i-x_{i-1}.
```

Nếu `f` thay đổi ít trên subinterval, contribution xấp xỉ

```math
f(x_i^*)\Delta x_i.
```

Cộng lại:

```math
\sum_{i=1}^n f(x_i^*)\Delta x_i.
```

Khi partition fine dần và tổng hội tụ tới một value không phụ thuộc cách chọn sample points, ta có definite integral

```math
\int_a^b f(x)\,dx.
```

Đây là Riemann-sum intuition.

## Integral là signed accumulation

Nếu `f(x)>0`, contribution positive. Nếu `f(x)<0`, contribution negative.

Do đó

```math
\int_a^b f(x)dx
```

không nhất thiết bằng geometric area giữa graph và x-axis.

Muốn total geometric area, thường cần split theo sign hoặc tính

```math
\int_a^b |f(x)|dx.
```

Signed accumulation rất tự nhiên với velocity. Chuyển động 10 m sang phải rồi 10 m sang trái có displacement bằng 0 dù total distance bằng 20 m.

## Units cho biết integral có nghĩa gì

Nếu

```math
v(t)\quad [m/s],
```

thì

```math
v(t)dt
```

có unit meters. Vì vậy

```math
\int_{t_0}^{t_1}v(t)dt
```

là displacement.

Nếu power đo bằng kW và integrate theo hours, result là kWh.

Nếu density người/km² integrate trên area km², result là số người.

Kiểm tra units là một cách cực mạnh để verify interpretation của integral.

## Indefinite integral và antiderivative

Nếu

```math
F'(x)=f(x),
```

thì `F` là antiderivative của `f`.

Ta viết

```math
\int f(x)dx=F(x)+C.
```

Constant `C` bắt buộc vì

```math
\frac d{dx}(F(x)+C)=F'(x).
```

Indefinite integral là family của antiderivatives, không phải một number như definite integral.

## Fundamental Theorem of Calculus

Định nghĩa accumulation function

```math
A(x)=\int_a^x f(t)dt.
```

Nếu `f` continuous, thì

```math
A'(x)=f(x).
```

Điều này nói rằng instantaneous rate của accumulated total tại endpoint chính là current density.

Chiều ngược lại, nếu `F'=f`, thì

```math
\int_a^b f(x)dx=F(b)-F(a).
```

Đây là bridge giữa limit-defined accumulation và antiderivatives.

## Vì sao theorem này sâu?

Differentiation là local operation: zoom vào một điểm. Integration là global operation: cộng contributions trên cả interval.

Fundamental theorem cho biết local rate và global accumulation là inverse views của cùng process dưới suitable conditions.

Nếu velocity là derivative của position, accumulated velocity khôi phục position change. Nếu density là derivative của cumulative mass, integrate density khôi phục total mass.

## Substitution: đổi variable để đổi geometry

Nếu

```math
u=g(x),
```

và

```math
du=g'(x)dx,
```

thì

```math
\int f(g(x))g'(x)dx
=\int f(u)du.
```

Substitution không chỉ là trick đổi ký hiệu. Nó là change of coordinates trong một dimension.

Ví dụ

```math
\int 2x\cos(x^2)dx.
```

Đặt

```math
u=x^2,
```

nên

```math
du=2x\,dx.
```

Ta được

```math
\int\cos u\,du=\sin u+C
=\sin(x^2)+C.
```

## Integration by parts

Từ product rule

```math
(uv)'=u'v+uv',
```

integrate hai vế:

```math
\int u\,dv=uv-\int v\,du.
```

Method này hữu ích khi một factor trở nên đơn giản hơn sau differentiation còn factor kia dễ integrate.

Ví dụ

```math
\int x e^x dx.
```

Chọn

```math
u=x,\qquad dv=e^xdx,
```

nên

```math
du=dx,\qquad v=e^x.
```

Do đó

```math
\int xe^xdx=xe^x-e^x+C.
```

## Improper integrals

Integral có thể involve infinite interval hoặc unbounded integrand.

Ví dụ

```math
\int_1^\infty \frac1{x^2}dx
```

được định nghĩa qua limit

```math
\lim_{b\to\infty}\int_1^b\frac1{x^2}dx.
```

Kết quả bằng 1, nên integral converge.

Nhưng

```math
\int_1^\infty\frac1x dx
```

diverges vì logarithm tăng không bị chặn.

Infinite domain không tự động làm integral infinite; convergence phụ thuộc tốc độ decay.

## Average value của function

Average value trên `[a,b]` là

```math
f_{avg}=\frac1{b-a}\int_a^b f(x)dx.
```

Công thức này là continuous analogue của arithmetic mean.

Integral cho total accumulated value; chia total interval length cho average density/rate.

## Probability density

Nếu continuous random variable có density `p(x)`, probability interval là

```math
P(a\le X\le b)=\int_a^b p(x)dx.
```

Total probability yêu cầu

```math
\int_{-\infty}^{\infty}p(x)dx=1.
```

Density `p(x)` có thể lớn hơn 1 vì nó không phải probability tại một point. Probability đến từ integrating density trên interval.

## Expectation là integral

Expected value của continuous random variable:

```math
E[X]=\int_{-\infty}^{\infty}x p(x)dx.
```

More generally,

```math
E[g(X)]=\int g(x)p(x)dx.
```

Do đó expectation chính là weighted accumulation, với weights là probability density.

Bridge này nối calculus trực tiếp với statistics và machine learning.

## Change of variables và Jacobian

Trong nhiều dimensions, khi đổi coordinates, volume element cũng thay đổi.

Ví dụ từ Cartesian sang polar:

```math
x=r\cos\theta,\qquad y=r\sin\theta.
```

Area element không phải `dr dθ` mà là

```math
dA=r\,dr\,d\theta.
```

Factor `r` là magnitude của Jacobian determinant.

Do circumference của ring radius `r` tăng theo `r`, cùng một `dr dθ` ở radius lớn cover area lớn hơn.

Đây là geometric meaning của Jacobian trong multivariable integration và probability density transformations.

## Double và triple integrals

Nếu density trên region `R` là `f(x,y)`, total amount là

```math
\iint_R f(x,y)dA.
```

Trong 3D:

```math
\iiint_V f(x,y,z)dV.
```

Order of integration có thể được đổi dưới suitable conditions. Fubini's theorem formalize khi multidimensional integral có thể tính như iterated integrals.

## Line integrals

Nếu vector field `F` tác dụng dọc path `C`, work là

```math
\int_C F\cdot dr.
```

Đây là accumulation không theo x-axis mà theo một curve trong space.

Nếu `F` là force và `dr` infinitesimal displacement, dot product lấy component force theo direction movement.

## Surface integrals

Flux qua surface `S` là

```math
\iint_S F\cdot n\,dS.
```

Nó đo amount của vector field đi xuyên qua surface.

Divergence theorem và Stokes' theorem nối local derivatives với global integrals trên boundaries, mở rộng philosophy của Fundamental Theorem of Calculus sang higher dimensions.

## Convolution là integral accumulation

Continuous convolution:

```math
(f*g)(t)=\int_{-\infty}^{\infty}f(\tau)g(t-\tau)d\tau.
```

Mỗi shifted overlap đóng góp một lượng vào output.

Convolution xuất hiện trong signal processing, probability distribution sums, linear systems và neural network theory.

## Integral transforms

Fourier transform:

```math
F(\omega)=\int_{-\infty}^{\infty}f(t)e^{-i\omega t}dt.
```

Laplace transform:

```math
F(s)=\int_0^\infty f(t)e^{-st}dt.
```

Cả hai đều là weighted integrals: chúng project một function lên families của basis-like functions để đổi representation.

## Numerical integration

Không phải integral nào có elementary antiderivative. Trong data analysis, ta còn thường chỉ có sampled values.

Rectangle rule approximate bằng piecewise constant.

Trapezoidal rule approximate bằng line segments.

Nếu equally spaced samples với spacing `h`, composite trapezoidal rule là

```math
\int_a^b f(x)dx
\approx h\left[\frac12f(x_0)+\sum_{i=1}^{n-1}f(x_i)+\frac12f(x_n)\right].
```

Simpson's rule dùng quadratic interpolation và thường chính xác hơn cho smooth functions.

## Error và step size

Giảm step size thường giảm truncation error, nhưng không vô hạn tốt hơn. Floating-point rounding, noisy data và computation cost có thể trở nên dominant.

Numerical integration vì vậy là balance giữa approximation order, smoothness assumptions, resolution và noise.

Adaptive quadrature tự động refine intervals nơi function thay đổi nhanh hơn.

## Monte Carlo integration

Với high-dimensional integral, grid-based quadrature suffer curse of dimensionality.

Nếu `X` sampled từ density `p`, ta có thể rewrite

```math
I=\int f(x)p(x)dx=E[f(X)].
```

Approximate bằng sample mean:

```math
I\approx\frac1N\sum_{i=1}^N f(X_i).
```

Convergence rate khoảng `O(N^{-1/2})` không phụ thuộc dimension theo cùng cách grid methods, nên Monte Carlo rất quan trọng trong high-dimensional statistics và physics.

## Integrals và conservation laws

Nếu local density thay đổi nhưng total quantity được bảo toàn, integral over region thường encode conserved quantity.

Mass:

```math
M=\int\rho(x)dV.
```

Energy, charge và probability đều có integral formulations tương tự.

PDE conservation laws thường nói rate of change của integral trong region bằng flux qua boundary cộng sources/sinks.

## Mental Model

Hãy xem integral như operator biến “density/rate/contribution per unit” thành “total amount”. `dx`, `dt`, `dA`, `dV` không phải decorative symbols; chúng cho biết infinitesimal measure mà contribution đang được weighted theo.

Fundamental theorem nói nếu một function mô tả local rate của cumulative quantity, integrating rate reconstructs global change và differentiating cumulative quantity trả lại local rate.

## Common Misconceptions

Integral không chỉ là area under curve. Area, displacement, probability, expectation, work, mass, flux và transform coefficients đều là cùng accumulation idea trong contexts khác nhau.

Indefinite integral phải có constant `C`. Definite integral không cần `C` vì constants cancel trong `F(b)-F(a)`.

Improper integral có infinite bound không tự động diverge. Ngược lại, finite interval vẫn có thể tạo divergent integral nếu integrand có singularity đủ mạnh.

Numerical integral trả approximation, không phải exact value chỉ vì calculator hiển thị nhiều digits.

## Liên kết kiến thức

Chapter này nối trực tiếp với [Derivatives](./01_derivatives.md), [Real analysis](./11_real_analysis_convergence_and_rigor.md), [Probability](../06_probability_statistics/01_probability_foundations.md), [Vector calculus](./09_vector_calculus.md), [Fourier](../09_connections/05_fourier_signals_and_frequency.md) và [Numerical methods](../08_optimization_numerical/02_numerical_methods_and_error.md).