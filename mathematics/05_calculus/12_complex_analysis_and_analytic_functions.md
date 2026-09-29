# Complex phân tích (analysis / 분석): analytic functions, hình học (geometry / 기하학) và vì sao số phức làm calculus mạnh hơn

> **Mạch đọc:** Đọc **Complex phân tích (analysis / 분석): analytic functions, hình học (geometry / 기하학) và vì sao số phức làm calculus mạnh hơn** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Mặt phẳng phức** sang **Complex derivative**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Số phức ban đầu thường xuất hiện như cách mở rộng hệ số để phương trình như `x²+1=0` có nghiệm. Nhưng khi đưa calculus vào mặt phẳng phức, ta nhận được một lý thuyết (theory / 이론) mạnh hơn rất nhiều calculus thực. **Complex phân tích (analysis / 분석)** nghiên cứu functions

```math
f:\mathbb C\to\mathbb C
```

và đặc biệt là các functions complex-differentiable trên một vùng, gọi là **holomorphic** hoặc **analytic functions**.

Điều bất ngờ là yêu cầu differentiable trong complex plane mạnh hơn nhiều so với differentiable trên real line. Một holomorphic hàm (function / 함수) thường tự động infinitely differentiable, có power-series expansion và bị ràng buộc mạnh bởi values trên ranh giới (boundary / 경계).

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

Đây là lý do số phức tự nhiên trong rotation, oscillation, Fourier phân tích (analysis / 분석) và tín hiệu (signal / 신호) processing.

## Complex derivative

Derivative tại `z_0` được định nghĩa

```math
f'(z_0)=\lim_{h\to0}\frac{f(z_0+h)-f(z_0)}{h}.
```

Nhìn giống real derivative, nhưng `h` bây giờ có thể tiến về 0 từ vô số directions trên plane.

Để limit tồn tại, quotient phải hội tụ về cùng giá trị (value / 값) bất kể direction. Đây là ràng buộc (constraint / 제약조건) rất mạnh.

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

Do đó hàm (function / 함수) thỏa cấu trúc (structure / 구조) cần thiết của complex differentiability.

## Vì sao complex differentiability mạnh

Trong `R²`, một differentiable hàm (function / 함수) có Jacobian ma trận (matrix / 행렬) tổng quát. Với holomorphic hàm (function / 함수), Jacobian phải có form

```math
\begin{bmatrix}
a&-b\\b&a
\end{bmatrix}.
```

Ma trận (matrix / 행렬) dạng này chính là cục bộ (local / 로컬) scaling cộng rotation. Vì vậy holomorphic mappings cục bộ (local / 로컬) bảo toàn angles khi derivative khác 0; thuộc tính (property / 속성) này gọi là **conformal**.

## Analytic functions và power series

Một hàm (function / 함수) analytic quanh `z_0` có expansion

```math
f(z)=\sum_{n=0}^{\infty} a_n(z-z_0)^n.
```

Trong complex phân tích (analysis / 분석), holomorphic trên open region kéo theo analytic. Đây là kết quả mạnh và khác calculus thực, nơi một hàm (function / 함수) có thể infinitely differentiable nhưng Taylor series không bằng hàm (function / 함수).

Các familiar functions như

```math
e^z,\quad \sin z,\quad \cos z
```

đều được định nghĩa tự nhiên bằng power series và giữ nhiều identities quen thuộc.

## Contour và complex integral

Thay vì integrate trên real interval, complex phân tích (analysis / 분석) integrate dọc một curve `γ(t)` trong plane:

```math
\int_\gamma f(z)\,dz
=\int_a^b f(\gamma(t))\gamma'(t)dt.
```

Integral phụ thuộc cả hàm (function / 함수) và đường dẫn (path / 경로). Nhưng với holomorphic functions trên suitable regions, đường dẫn (path / 경로) dependence có thể biến mất.

## Cauchy's theorem

Một central kết quả (result / 결과) nói rằng nếu `f` holomorphic trên simply connected region, thì integral quanh closed contour bằng 0:

```math
\oint_\gamma f(z)\,dz=0.
```

Điều này có hệ quả lớn: integral giữa hai điểm không phụ thuộc đường dẫn (path / 경로) và hàm (function / 함수) có antiderivative trên region đó.

## Cauchy integral formula

Nếu `f` holomorphic bên trong và trên một simple closed contour `γ`, và `z_0` nằm bên trong, thì

```math
f(z_0)=\frac{1}{2\pi i}\oint_\gamma
\frac{f(z)}{z-z_0}\,dz.
```

Formula nói giá trị (value / 값) bên trong region được xác định bởi values trên ranh giới (boundary / 경계).

Derivatives cũng được lấy từ ranh giới (boundary / 경계):

```math
f^{(n)}(z_0)=\frac{n!}{2\pi i}\oint_\gamma
\frac{f(z)}{(z-z_0)^{n+1}}\,dz.
```

Đây là lý do holomorphic hàm (function / 함수) cực kỳ rigid.

## Singularities

Không phải complex hàm (function / 함수) nào holomorphic ở mọi điểm. Một điểm (point / 지점) nơi hàm (function / 함수) không analytic được gọi là singularity.

Ví dụ

```math
f(z)=\frac1z
```

có singularity tại `z=0`.

Một singularity isolated có thể là removable singularity, pole hoặc essential singularity.

Pole bậc `m` có hành vi (behavior / 동작) gần `z_0` kiểu

```math
f(z)\approx\frac{a_{-m}}{(z-z_0)^m}.
```

## Laurent series

Quanh singularity, power series thông thường không đủ. Ta dùng Laurent series:

```math
f(z)=\sum_{n=-\infty}^{\infty}a_n(z-z_0)^n.
```

Các terms negative powers tạo principal part và chứa thông tin (information / 정보) về singularity.

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

Functions thỏa Laplace equation gọi là harmonic. Chúng xuất hiện trong steady-state heat, electrostatics, fluid luồng (flow / 흐름) và potential lý thuyết (theory / 이론).

Vì vậy complex phân tích (analysis / 분석) nối trực tiếp với PDE và physics 2D.

## Conformal ánh xạ (mapping / 매핑)

Holomorphic functions với nonzero derivative cục bộ (local / 로컬) bảo toàn góc. Điều này cho phép map một hình học (geometry / 기하학) phức tạp sang hình học (geometry / 기하학) đơn giản hơn để giải boundary-value problems.

Ví dụ Möbius transformation

```math
f(z)=\frac{az+b}{cz+d}
```

map generalized circles thành generalized circles và đóng vai trò quan trọng trong hình học (geometry / 기하학), điều khiển (control / 제어) và tín hiệu (signal / 신호) lý thuyết (theory / 이론).

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

Do đó sinusoidal phân tích (analysis / 분석), Fourier transform, Laplace transform và tuyến tính (linear / 선형) differential equations đều hưởng lợi từ complex biểu diễn (representation / 표현).

## Poles và hệ thống (system / 시스템) hành vi (behavior / 동작)

Trong điều khiển (control / 제어) và tín hiệu (signal / 신호) processing, transfer hàm (function / 함수) thường là rational hàm (function / 함수) của complex variable `s` hoặc `z`.

Locations của poles quyết định stability và transient hành vi (behavior / 동작). Đây không phải coincidence; exponential modes của tuyến tính (linear / 선형) các hệ thống (systems / 시스템들) được encoded bằng complex roots của characteristic equations.

## Mô hình tư duy (mental model / 사고 모델)

Complex phân tích (analysis / 분석) xem complex hàm (function / 함수) như một ánh xạ (mapping / 매핑) vừa biến đổi magnitude vừa rotation trên plane. Yêu cầu differentiability từ mọi direction khiến ánh xạ (mapping / 매핑) cực kỳ structured. Nhờ đó cục bộ (local / 로컬) derivative dẫn tới toàn cục (global / 전역) theorems mạnh như Cauchy formula và residue theorem.

## Dùng chung (common / 공통) Misconceptions

Số phức không chỉ là “số giả”. Chúng là biểu diễn (representation / 표현) tự nhiên của two-dimensional scaling và rotation. Complex derivative cũng không chỉ là lấy derivative theo `x` rồi thêm `i`; nó đòi hỏi consistency giữa mọi direction approach.

Một misconception khác là nghĩ complex phân tích (analysis / 분석) chỉ phục vụ pure mathematics. Trong kỹ thuật (engineering / 엔지니어링), chính nó nằm sau frequency phản hồi (response / 응답), poles/zeros, Fourier/Laplace transforms, electromagnetics và nhiều numerical methods.

## Liên kết kiến thức

Nên đọc sau [Complex numbers](../01_algebra/05_complex_numbers.md), [Infinite series](./07_infinite_series_power_series_and_convergence.md), [Vector calculus](./09_vector_calculus.md) và [PDE](./10_partial_differential_equations_and_fields_intro.md). Sau đó chapter [Fourier](../09_connections/05_fourier_signals_and_frequency.md) và [Laplace/Z-transform](../09_connections/06_laplace_z_transform_and_dynamic_systems.md) sẽ trở nên tự nhiên hơn nhiều.

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 limits and continuity](./00_limits_and_continuity.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
