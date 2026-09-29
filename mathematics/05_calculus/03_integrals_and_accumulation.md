# Tích phân: accumulation, area, expectation và tổng liên tục

> **Mạch đọc:** Đọc **Tích phân: accumulation, area, expectation và tổng liên tục** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Từ tổng hữu hạn đến integral** sang **Integral là signed accumulation**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Đạo hàm trả lời câu hỏi cục bộ (local / 로컬): tại một điểm, quantity đang thay đổi nhanh thế nào? **Tích phân (Integral / 적분)** trả lời câu hỏi toàn cục (global / 전역): nếu có vô số contributions nhỏ dọc theo một interval, surface, thời gian (time / 시간) period hoặc xác suất (probability / 확률) không gian (space / 공간), tổng tác động (effect / 효과) là bao nhiêu?

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

Khi partition fine dần và tổng hội tụ tới một giá trị (value / 값) không phụ thuộc cách chọn mẫu (sample / 표본) points, ta có definite integral

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

không nhất thiết bằng geometric area giữa đồ thị (graph / 그래프) và x-axis.

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

có đơn vị (unit / 단위) meters. Vì vậy

```math
\int_{t_0}^{t_1}v(t)dt
```

là displacement.

Nếu power đo bằng kW và integrate theo hours, kết quả (result / 결과) là kWh.

Nếu density người/km² integrate trên area km², kết quả (result / 결과) là số người.

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

Định nghĩa accumulation hàm (function / 함수)

```math
A(x)=\int_a^x f(t)dt.
```

Nếu `f` continuous, thì

```math
A'(x)=f(x).
```

Điều này nói rằng instantaneous tỷ lệ (rate / 비율) của accumulated total tại endpoint chính là hiện tại (current / 현재) density.

Chiều ngược lại, nếu `F'=f`, thì

```math
\int_a^b f(x)dx=F(b)-F(a).
```

Đây là cầu nối (bridge / 브리지) giữa limit-defined accumulation và antiderivatives.

## Vì sao theorem này sâu?

Differentiation là cục bộ (local / 로컬) thao tác (operation / 연산): zoom vào một điểm. tích hợp (integration / 통합) là toàn cục (global / 전역) thao tác (operation / 연산): cộng contributions trên cả interval.

Fundamental theorem cho biết cục bộ (local / 로컬) tỷ lệ (rate / 비율) và toàn cục (global / 전역) accumulation là inverse views của cùng tiến trình (process / 프로세스) dưới suitable conditions.

Nếu velocity là derivative của position, accumulated velocity khôi phục position thay đổi (change / 변경). Nếu density là derivative của cumulative mass, integrate density khôi phục total mass.

## Substitution: đổi variable để đổi hình học (geometry / 기하학)

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

Substitution không chỉ là trick đổi ký hiệu. Nó là thay đổi (change / 변경) of coordinates trong một dimension.

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

## Tích hợp (integration / 통합) by parts

Từ sản phẩm (product / 제품) quy tắc (rule / 규칙)

```math
(uv)'=u'v+uv',
```

integrate hai vế:

```math
\int u\,dv=uv-\int v\,du.
```

Phương thức (method / 메서드) này hữu ích khi một factor trở nên đơn giản hơn sau differentiation còn factor kia dễ integrate.

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

Infinite lĩnh vực (domain / 도메인) không tự động làm integral infinite; convergence phụ thuộc tốc độ decay.

## Average giá trị (value / 값) của hàm (function / 함수)

Average giá trị (value / 값) trên `[a,b]` là

```math
f_{avg}=\frac1{b-a}\int_a^b f(x)dx.
```

Công thức này là continuous analogue của arithmetic mean.

Integral cho total accumulated giá trị (value / 값); chia total interval length cho average density/tỷ lệ (rate / 비율).

## Xác suất (probability / 확률) density

Nếu continuous random variable có density `p(x)`, xác suất (probability / 확률) interval là

```math
P(a\le X\le b)=\int_a^b p(x)dx.
```

Total xác suất (probability / 확률) yêu cầu

```math
\int_{-\infty}^{\infty}p(x)dx=1.
```

Density `p(x)` có thể lớn hơn 1 vì nó không phải xác suất (probability / 확률) tại một điểm (point / 지점). xác suất (probability / 확률) đến từ integrating density trên interval.

## Expectation là integral

Expected giá trị (value / 값) của continuous random variable:

```math
E[X]=\int_{-\infty}^{\infty}x p(x)dx.
```

More generally,

```math
E[g(X)]=\int g(x)p(x)dx.
```

Do đó expectation chính là weighted accumulation, với weights là xác suất (probability / 확률) density.

Cầu nối (bridge / 브리지) này nối calculus trực tiếp với statistics và machine học tập (learning / 학습).

## Thay đổi (change / 변경) of variables và Jacobian

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

Đây là geometric meaning của Jacobian trong multivariable tích hợp (integration / 통합) và xác suất (probability / 확률) density transformations.

## Double và triple integrals

Nếu density trên region `R` là `f(x,y)`, total amount là

```math
\iint_R f(x,y)dA.
```

Trong 3D:

```math
\iiint_V f(x,y,z)dV.
```

Thứ tự (order / 순서) of tích hợp (integration / 통합) có thể được đổi dưới suitable conditions. Fubini's theorem formalize khi multidimensional integral có thể tính như iterated integrals.

## Line integrals

Nếu véc-tơ (vector / 벡터) trường dữ liệu (field / 필드) `F` tác dụng dọc đường dẫn (path / 경로) `C`, công việc (work / 작업) là

```math
\int_C F\cdot dr.
```

Đây là accumulation không theo x-axis mà theo một curve trong không gian (space / 공간).

Nếu `F` là force và `dr` infinitesimal displacement, dot sản phẩm (product / 제품) lấy thành phần (component / 컴포넌트) force theo direction movement.

## Surface integrals

Flux qua surface `S` là

```math
\iint_S F\cdot n\,dS.
```

Nó đo amount của véc-tơ (vector / 벡터) trường dữ liệu (field / 필드) đi xuyên qua surface.

Divergence theorem và Stokes' theorem nối cục bộ (local / 로컬) derivatives với toàn cục (global / 전역) integrals trên boundaries, mở rộng philosophy của Fundamental Theorem of Calculus sang higher dimensions.

## Convolution là integral accumulation

Continuous convolution:

```math
(f*g)(t)=\int_{-\infty}^{\infty}f(\tau)g(t-\tau)d\tau.
```

Mỗi shifted overlap đóng góp một lượng vào đầu ra (output / 출력).

Convolution xuất hiện trong tín hiệu (signal / 신호) processing, xác suất (probability / 확률) phân phối (distribution / 분포) sums, tuyến tính (linear / 선형) các hệ thống (systems / 시스템들) và neural mạng (network / 네트워크) lý thuyết (theory / 이론).

## Integral transforms

Fourier transform:

```math
F(\omega)=\int_{-\infty}^{\infty}f(t)e^{-i\omega t}dt.
```

Laplace transform:

```math
F(s)=\int_0^\infty f(t)e^{-st}dt.
```

Cả hai đều là weighted integrals: chúng dự án (project / 프로젝트) một hàm (function / 함수) lên families của basis-like functions để đổi biểu diễn (representation / 표현).

## Numerical tích hợp (integration / 통합)

Không phải integral nào có elementary antiderivative. Trong dữ liệu (data / 데이터) phân tích (analysis / 분석), ta còn thường chỉ có sampled values.

Rectangle quy tắc (rule / 규칙) approximate bằng piecewise constant.

Trapezoidal quy tắc (rule / 규칙) approximate bằng line segments.

Nếu equally spaced samples với spacing `h`, composite trapezoidal quy tắc (rule / 규칙) là

```math
\int_a^b f(x)dx
\approx h\left[\frac12f(x_0)+\sum_{i=1}^{n-1}f(x_i)+\frac12f(x_n)\right].
```

Simpson's quy tắc (rule / 규칙) dùng quadratic interpolation và thường chính xác hơn cho smooth functions.

## Lỗi (error / 오류) và step kích thước (size / 크기)

Giảm step kích thước (size / 크기) thường giảm truncation lỗi (error / 오류), nhưng không vô hạn tốt hơn. Floating-point rounding, noisy dữ liệu (data / 데이터) và computation chi phí (cost / 비용) có thể trở nên dominant.

Numerical tích hợp (integration / 통합) vì vậy là balance giữa approximation thứ tự (order / 순서), smoothness các giả định (assumptions / 가정들), resolution và noise.

Adaptive quadrature tự động refine intervals nơi hàm (function / 함수) thay đổi nhanh hơn.

## Monte Carlo tích hợp (integration / 통합)

Với high-dimensional integral, grid-based quadrature suffer curse of dimensionality.

Nếu `X` sampled từ density `p`, ta có thể rewrite

```math
I=\int f(x)p(x)dx=E[f(X)].
```

Approximate bằng mẫu (sample / 표본) mean:

```math
I\approx\frac1N\sum_{i=1}^N f(X_i).
```

Convergence tỷ lệ (rate / 비율) khoảng `O(N^{-1/2})` không phụ thuộc dimension theo cùng cách grid methods, nên Monte Carlo rất quan trọng trong high-dimensional statistics và physics.

## Integrals và conservation laws

Nếu cục bộ (local / 로컬) density thay đổi nhưng total quantity được bảo toàn, integral over region thường encode conserved quantity.

Mass:

```math
M=\int\rho(x)dV.
```

Năng lượng (energy / 에너지), charge và xác suất (probability / 확률) đều có integral formulations tương tự.

PDE conservation laws thường nói tỷ lệ (rate / 비율) of thay đổi (change / 변경) của integral trong region bằng flux qua ranh giới (boundary / 경계) cộng sources/sinks.

## Mô hình tư duy (mental model / 사고 모델)

Hãy xem integral như operator biến “density/tỷ lệ (rate / 비율)/contribution per đơn vị (unit / 단위)” thành “total amount”. `dx`, `dt`, `dA`, `dV` không phải decorative symbols; chúng cho biết infinitesimal measure mà contribution đang được weighted theo.

Fundamental theorem nói nếu một hàm (function / 함수) mô tả cục bộ (local / 로컬) tỷ lệ (rate / 비율) của cumulative quantity, integrating tỷ lệ (rate / 비율) reconstructs toàn cục (global / 전역) thay đổi (change / 변경) và differentiating cumulative quantity trả lại cục bộ (local / 로컬) tỷ lệ (rate / 비율).

## Dùng chung (common / 공통) Misconceptions

Integral không chỉ là area under curve. Area, displacement, xác suất (probability / 확률), expectation, công việc (work / 작업), mass, flux và transform coefficients đều là cùng accumulation idea trong contexts khác nhau.

Indefinite integral phải có constant `C`. Definite integral không cần `C` vì constants cancel trong `F(b)-F(a)`.

Improper integral có infinite bound không tự động diverge. Ngược lại, finite interval vẫn có thể tạo divergent integral nếu integrand có singularity đủ mạnh.

Numerical integral trả approximation, không phải chính xác (exact / 정확한) giá trị (value / 값) chỉ vì calculator hiển thị nhiều digits.

## Liên kết kiến thức

Chapter này nối trực tiếp với [Derivatives](./01_derivatives.md), [Real analysis](./11_real_analysis_convergence_and_rigor.md), [Probability](../06_probability_statistics/01_probability_foundations.md), [Vector calculus](./09_vector_calculus.md), [Fourier](../09_connections/05_fourier_signals_and_frequency.md) và [Numerical methods](../08_optimization_numerical/02_numerical_methods_and_error.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 limits and continuity](./00_limits_and_continuity.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
