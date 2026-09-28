# Laplace transform, Z-transform và cách nhìn hệ động lực qua lĩnh vực (domain / 도메인) khác

> **Mạch đọc:** Đọc **Laplace transform, Z-transform và cách nhìn hệ động lực qua lĩnh vực (domain / 도메인) khác** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Laplace transform** sang **Vì sao derivative biến thành algebra**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Fourier phân tích (analysis / 분석) đổi biểu diễn (representation / 표현) từ thời gian (time / 시간)/không gian (space / 공간) lĩnh vực (domain / 도메인) sang frequency lĩnh vực (domain / 도메인). Hai transforms liên quan rất quan trọng cho các hệ thống (systems / 시스템들) kỹ thuật (engineering / 엔지니어링) là **Laplace transform / 라플라스 변환** cho continuous-time các hệ thống (systems / 시스템들) và **Z-transform / Z변환** cho discrete-time các hệ thống (systems / 시스템들).

Mục tiêu của transforms không phải làm tín hiệu (signal / 신호) “khác đi”, mà chọn coordinates nơi differentiation, convolution hoặc recurrence trở nên algebraically đơn giản hơn.

## Laplace transform

Với hàm (function / 함수) `f(t)` cho `t≥0`, Laplace transform được định nghĩa

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

Một thuộc tính (property / 속성) trung tâm:

```math
\mathcal L\{f'(t)\}
=sF(s)-f(0).
```

Second derivative:

```math
\mathcal L\{f''(t)\}
=s^2F(s)-sf(0)-f'(0).
```

Do đó differential equation trong thời gian (time / 시간) lĩnh vực (domain / 도메인) biến thành algebraic equation theo `s`.

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

Đây là một thay đổi (change / 변경) of biểu diễn (representation / 표현) giống diagonalization trong tuyến tính (linear / 선형) algebra: operator differentiation trở nên gần như multiplication by `s`.

## Transfer hàm (function / 함수)

Với tuyến tính (linear / 선형) time-invariant hệ thống (system / 시스템) và zero initial conditions, **transfer hàm (function / 함수) / 전달함수** là ratio

```math
H(s)=\frac{Y(s)}{U(s)}.
```

Nếu hệ thống (system / 시스템) obeys

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

Continuous-time LTI hệ thống (system / 시스템) có impulse phản hồi (response / 응답) terms kiểu `e^{pt}` từ poles `p`. Nếu real part của pole negative, chế độ (mode / 모드) decays. Nếu positive, chế độ (mode / 모드) grows exponentially. Poles trên imaginary axis cần xét kỹ multiplicity và ngữ cảnh (context / 맥락).

Do đó left half of complex `s`-plane liên hệ stable decay. Complex numbers ở đây không phải decorative lớp trừu tượng (abstraction / 추상화); chúng encode simultaneous decay tỷ lệ (rate / 비율) và oscillation frequency.

## Convolution thành multiplication

Laplace transform biến convolution thành sản phẩm (product / 제품):

```math
\mathcal L\{f*g\}=F(s)G(s).
```

Time-domain đầu ra (output / 출력) của LTI hệ thống (system / 시스템)

```math
y=h*u
```

trở thành

```math
Y(s)=H(s)U(s).
```

Đây là cùng principle như Fourier transform: convolution operator được diagonalize bởi exponential basis.

## Z-transform cho discrete thời gian (time / 시간)

Với chuỗi (sequence / 시퀀스) `x[n]`, bilateral Z-transform là

```math
X(z)=\sum_{n=-\infty}^{\infty}x[n]z^{-n}.
```

One-sided phiên bản (version / 버전) thường dùng cho nhân quả (causal / 인과적) các hệ thống (systems / 시스템들) và recurrence với initial conditions.

Shift thuộc tính (property / 속성) rất quan trọng. Delay một mẫu (sample / 표본) tương ứng multiplication bởi `z^{-1}`. Vì vậy recurrence relations biến thành algebraic equations theo `z`.

Ví dụ difference equation

```math
y[n]-ay[n-1]=x[n]
```

với zero initial trạng thái (state / 상태) cho

```math
Y(z)-az^{-1}Y(z)=X(z).
```

Do đó transfer hàm (function / 함수)

```math
H(z)=\frac{Y(z)}{X(z)}
=\frac{1}{1-az^{-1}}.
```

## Đơn vị (unit / 단위) circle và Fourier liên kết (connection / 연결)

Discrete-time Fourier transform xuất hiện khi evaluate Z-transform trên đơn vị (unit / 단위) circle

```math
z=e^{i\omega}.
```

Nếu region of convergence chứa đơn vị (unit / 단위) circle, frequency phản hồi (response / 응답) là

```math
H(e^{i\omega}).
```

Vì thế Z-transform chứa cả growth/decay thông tin (information / 정보) theo radius `|z|` và oscillation theo angle.

## Poles và stability trong discrete các hệ thống (systems / 시스템들)

Chế độ (mode / 모드) kiểu `a^n` decay nếu

```math
|a|<1.
```

Do đó nhân quả (causal / 인과적) discrete LTI hệ thống (system / 시스템) rational thường stable khi poles nằm inside đơn vị (unit / 단위) circle. Continuous hệ thống (system / 시스템) dùng left half-plane; discrete hệ thống (system / 시스템) dùng đơn vị (unit / 단위) disk. ánh xạ (mapping / 매핑) giữa hai worlds có thể thực hiện bằng transformations như bilinear transform.

## State-space và eigenvalues

Hệ động (dynamic system / 동적 시스템) dạng

```math
\dot x=Ax+Bu
```

có natural hành vi (behavior / 동작) liên hệ eigenvalues của `A`. Laplace transform cho

```math
(sI-A)X(s)=BU(s)+x(0).
```

Ma trận (matrix / 행렬) inverse

```math
(sI-A)^{-1}
```

là resolvent; poles liên hệ eigenvalues của `A`. Đây là cầu nối (bridge / 브리지) trực tiếp giữa tuyến tính (linear / 선형) algebra và điều khiển (control / 제어) lý thuyết (theory / 이론).

Discrete-time hệ thống (system / 시스템)

```math
x_{n+1}=Ax_n+Bu_n
```

ổn định theo analogous sense khi eigenvalues liên quan nằm inside đơn vị (unit / 단위) circle.

## Filters trong software và tín hiệu (signal / 신호) processing

Digital filters được implement bằng difference equations. FIR filter có finite impulse phản hồi (response / 응답); IIR filter có phản hồi (feedback / 피드백) và theoretically infinite phản hồi (response / 응답). Z-domain giúp analyze frequency phản hồi (response / 응답) và stability trước khi mã (code / 코드).

Moving average filter là convolution đơn giản. Exponential moving average

```math
y[n]=\alpha x[n]+(1-\alpha)y[n-1]
```

là first-order IIR filter. Nó xuất hiện không chỉ trong DSP mà cả metrics smoothing, finance và optimizer statistics.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Laplace/Z-transform nối differential equations, recurrence relations, complex numbers, Fourier phân tích (analysis / 분석), convolution, eigenvalues và điều khiển (control / 제어) các hệ thống (systems / 시스템들). Về mặt mô hình tư duy (mental model / 사고 모델), đây là một ví dụ nữa của chiến lược (strategy / 전략) cực mạnh trong mathematics: đổi basis/biểu diễn (representation / 표현) để operator khó biến thành multiplication dễ.

Fourier hỏi hệ thống (system / 시스템) phản ứng với pure frequencies thế nào. Laplace mở rộng bằng exponential growth/decay. Z-transform làm analogous job cho discrete-time sequences.

## Mô hình tư duy (mental model / 사고 모델)

> Transform lĩnh vực (domain / 도메인) giống như đổi tọa độ cho một bài toán động. Trong thời gian (time / 시간) lĩnh vực (domain / 도메인) ta thấy derivative, convolution và recurrence. Trong Laplace/Z lĩnh vực (domain / 도메인), chúng thường biến thành multiplication, rational functions và pole-zero hình học (geometry / 기하학). Ta không né dynamics; ta chọn biểu diễn (representation / 표현) nơi dynamics lộ cấu trúc (structure / 구조) dễ thao tác hơn.

## Dùng chung (common / 공통) Misconceptions

Laplace transform không chỉ là bảng công thức inverse transforms. Giá trị thật nằm ở operator properties, initial conditions, region of convergence và pole cấu trúc (structure / 구조).

Pole ở đâu quyết định stability chỉ khi các giả định (assumptions / 가정들) về hệ thống (system / 시스템) và region of convergence phù hợp. Không nên dùng quy tắc (rule / 규칙) “pole inside/outside” ngoài đúng continuous/discrete setting.

Fourier, Laplace và Z-transform không interchangeable một cách vô điều kiện. Chúng có domains, convergence conditions và purposes khác nhau dù liên hệ chặt chẽ.

## Liên kết kiến thức

Prerequisite trực tiếp gồm [Complex Numbers](../01_algebra/05_complex_numbers.md), [Sequences, Series and Recurrence](../02_functions/03_sequences_series_and_recurrence.md), [Differential Equations](../05_calculus/05_differential_equations.md) và [Eigenvalues/Eigenvectors](../04_vectors_linear_algebra/04_eigenvalues_and_eigenvectors.md).

Để hiểu basis/frequency viewpoint trước khi học pole-zero hình học (geometry / 기하학), đọc [Fourier, Signals and Frequency](./05_fourier_signals_and_frequency.md). Với điều khiển (control / 제어)/quyết định (decision / 결정) dynamics, đọc tiếp [Dynamic Programming, Bellman and Optimal Control](../08_optimization_numerical/06_dynamic_programming_bellman_and_optimal_control.md). Numerical hiện thực (implementation / 구현) và stability caveats nối với [Numerical Methods and Error](../08_optimization_numerical/02_numerical_methods_and_error.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 rate change and accumulation](./00_rate_change_and_accumulation.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
