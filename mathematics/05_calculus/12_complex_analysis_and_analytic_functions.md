# Complex analysis: analytic functions, geometry và vì sao số phức làm calculus mạnh hơn

Số phức ban đầu thường xuất hiện như cách mở rộng hệ số để phương trình như `x²+1=0` có nghiệm. Nhưng khi đưa calculus vào mặt phẳng phức, ta nhận được một theory mạnh hơn rất nhiều calculus thực. **Complex analysis (복소해석학)** nghiên cứu functions

```math
f:\mathbb C\to\mathbb C
```

và đặc biệt là các functions complex-differentiable trên một vùng, gọi là **holomorphic** hoặc **analytic functions**.

Điều bất ngờ là yêu cầu differentiable trong complex plane mạnh hơn nhiều so với differentiable trên real line. Một holomorphic function thường tự động infinitely differentiable, có power-series expansion và bị ràng buộc mạnh bởi values trên boundary.

## Mặt phẳng phức

Một số phức viết

```math
z=x+iy,
```

với `i²=-1`. Ta có thể xem `z` như điểm `(x,y)` trên plane.

Modulus là

```math
|z|=\sqrt{x^2+y^2},
```

và argument `arg z` là góc so với positive real axis.

Polar form là

```math
z=re^{i\theta},
```

với Euler formula

```math
e^{i\theta}=\cos\theta+i\sin\theta.
```

Phép nhân số phức trở thành nhân độ lớn và cộng góc:

```math
r_1e^{i\theta_1}r_2e^{i\theta_2}
=r_1r_2e^{i(\theta_1+\theta_2)}.
```

Đây là lý do số phức tự nhiên trong rotation, oscillation, Fourier analysis và signal processing.

## Complex derivative

Derivative tại `z_0` được định nghĩa

```math
f'(z_0)=\lim_{h\to0}\frac{f(z_0+h)-f(z_0)}{h}.
```

Nhìn giống real derivative, nhưng `h` bây giờ có thể tiến về 0 từ vô số directions trên plane.

Để limit tồn tại, quotient phải hội tụ về cùng value bất kể direction. Đây là constraint rất mạnh.

## Cauchy–Riemann equations

Viết

```math
f(z)=u(x,y)+iv(x,y).
```

Nếu `f` holomorphic và partial derivatives đủ regular, ta có Cauchy–Riemann equations:

```math
\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y},
```

```math
\frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}.
```

Ví dụ `f(z)=z²` cho

```math
u=x^2-y^2,
```

```math
v=2xy.
```

Ta có

```math
u_x=2x=v_y,
```

và

```math
u_y=-2y=-v_x.
```

Do đó function thỏa structure cần thiết của complex differentiability.

## Vì sao complex differentiability mạnh

Trong `R²`, một differentiable function có Jacobian matrix tổng quát. Với holomorphic function, Jacobian phải có form

```math
\begin{bmatrix}
a&-b\\b&a
\end{bmatrix}.
```

Matrix dạng này chính là local scaling cộng rotation. Vì vậy holomorphic mappings local bảo toàn angles khi derivative khác 0; property này gọi là **conformal**.

## Analytic functions và power series

Một function analytic quanh `z_0` có expansion

```math
f(z)=\sum_{n=0}^{\infty} a_n(z-z_0)^n.
```

Trong complex analysis, holomorphic trên open region kéo theo analytic. Đây là kết quả mạnh và khác calculus thực, nơi một function có thể infinitely differentiable nhưng Taylor series không bằng function.

Các familiar functions như

```math
e^z,\quad \sin z,\quad \cos z
```

đều được định nghĩa tự nhiên bằng power series và giữ nhiều identities quen thuộc.

## Contour và complex integral

Thay vì integrate trên real interval, complex analysis integrate dọc một curve `γ(t)` trong plane:

```math
\int_\gamma f(z)\,dz
=\int_a^b f(\gamma(t))\gamma'(t)dt.
```

Integral phụ thuộc cả function và path. Nhưng với holomorphic functions trên suitable regions, path dependence có thể biến mất.

## Cauchy's theorem

Một central result nói rằng nếu `f` holomorphic trên simply connected region, thì integral quanh closed contour bằng 0:

```math
\oint_\gamma f(z)\,dz=0.
```

Điều này có hệ quả lớn: integral giữa hai điểm không phụ thuộc path và function có antiderivative trên region đó.

## Cauchy integral formula

Nếu `f` holomorphic bên trong và trên một simple closed contour `γ`, và `z_0` nằm bên trong, thì

```math
f(z_0)=\frac{1}{2\pi i}\oint_\gamma
\frac{f(z)}{z-z_0}\,dz.
```

Formula nói value bên trong region được xác định bởi values trên boundary.

Derivatives cũng được lấy từ boundary:

```math
f^{(n)}(z_0)=\frac{n!}{2\pi i}\oint_\gamma
\frac{f(z)}{(z-z_0)^{n+1}}\,dz.
```

Đây là lý do holomorphic function cực kỳ rigid.

## Singularities

Không phải complex function nào holomorphic ở mọi điểm. Một point nơi function không analytic được gọi là singularity.

Ví dụ

```math
f(z)=\frac1z
```

có singularity tại `z=0`.

Một singularity isolated có thể là removable singularity, pole hoặc essential singularity.

Pole bậc `m` có behavior gần `z_0` kiểu

```math
f(z)\approx\frac{a_{-m}}{(z-z_0)^m}.
```

## Laurent series

Quanh singularity, power series thông thường không đủ. Ta dùng Laurent series:

```math
f(z)=\sum_{n=-\infty}^{\infty}a_n(z-z_0)^n.
```

Các terms negative powers tạo principal part và chứa information về singularity.

Coefficient `a_{-1}` đặc biệt quan trọng; nó là **residue**.

## Residue theorem

Nếu contour bao quanh các isolated singularities `z_k`, thì

```math
\oint_\gamma f(z)dz
=2\pi i\sum_k\operatorname{Res}(f,z_k).
```

Theorem này biến complex contour integral thành bài toán algebraic tính residues.

Nó còn giúp evaluate một số real integrals khó, inverse transforms và integrals trong physics.

## Ví dụ residue đơn giản

Với

```math
f(z)=\frac{e^z}{z},
```

residue tại `0` là coefficient của `1/z`. Vì

```math
e^z=1+z+\frac{z^2}{2!}+\cdots,
```

nên

```math
\frac{e^z}{z}=\frac1z+1+\frac z{2!}+\cdots.
```

Do đó residue bằng 1 và integral quanh contour bao `0` là

```math
2\pi i.
```

## Harmonic functions

Nếu `f=u+iv` holomorphic, real và imaginary parts thỏa Laplace equation:

```math
\nabla^2u=0,
```

```math
\nabla^2v=0.
```

Functions thỏa Laplace equation gọi là harmonic. Chúng xuất hiện trong steady-state heat, electrostatics, fluid flow và potential theory.

Vì vậy complex analysis nối trực tiếp với PDE và physics 2D.

## Conformal mapping

Holomorphic functions với nonzero derivative local bảo toàn góc. Điều này cho phép map một geometry phức tạp sang geometry đơn giản hơn để giải boundary-value problems.

Ví dụ Möbius transformation

```math
f(z)=\frac{az+b}{cz+d}
```

map generalized circles thành generalized circles và đóng vai trò quan trọng trong geometry, control và signal theory.

## Complex exponential và oscillation

Một sinusoid

```math
A\cos(\omega t+\phi)
```

có thể được xem là real part của

```math
Ae^{i(\omega t+\phi)}.
```

Differentiation trở nên đơn giản:

```math
\frac d{dt}e^{i\omega t}=i\omega e^{i\omega t}.
```

Do đó sinusoidal analysis, Fourier transform, Laplace transform và linear differential equations đều hưởng lợi từ complex representation.

## Poles và system behavior

Trong control và signal processing, transfer function thường là rational function của complex variable `s` hoặc `z`.

Locations của poles quyết định stability và transient behavior. Đây không phải coincidence; exponential modes của linear systems được encoded bằng complex roots của characteristic equations.

## Mental Model

Complex analysis xem complex function như một mapping vừa biến đổi magnitude vừa rotation trên plane. Yêu cầu differentiability từ mọi direction khiến mapping cực kỳ structured. Nhờ đó local derivative dẫn tới global theorems mạnh như Cauchy formula và residue theorem.

## Common Misconceptions

Số phức không chỉ là “số giả”. Chúng là representation tự nhiên của two-dimensional scaling và rotation. Complex derivative cũng không chỉ là lấy derivative theo `x` rồi thêm `i`; nó đòi hỏi consistency giữa mọi direction approach.

Một misconception khác là nghĩ complex analysis chỉ phục vụ pure mathematics. Trong engineering, chính nó nằm sau frequency response, poles/zeros, Fourier/Laplace transforms, electromagnetics và nhiều numerical methods.

## Liên kết kiến thức

Nên đọc sau [Complex numbers](../01_algebra/05_complex_numbers.md), [Infinite series](./07_infinite_series_power_series_and_convergence.md), [Vector calculus](./09_vector_calculus.md) và [PDE](./10_partial_differential_equations_and_fields_intro.md). Sau đó chapter [Fourier](../09_connections/05_fourier_signals_and_frequency.md) và [Laplace/Z-transform](../09_connections/06_laplace_z_transform_and_dynamic_systems.md) sẽ trở nên tự nhiên hơn nhiều.