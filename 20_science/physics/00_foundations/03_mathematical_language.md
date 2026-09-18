# Ngôn ngữ Toán học tối thiểu để đọc Vật lý

## Hàm số: state phụ thuộc vào cái gì?

Một hàm (Function / 함수) là quan hệ ánh xạ input sang output. Khi viết:

```math
x(t)
```

ta đang nói position là một function của time. Khi viết:

```math
T(x,y,z,t)
```

nhiệt độ là một field phụ thuộc cả không gian và thời gian.

Điều quan trọng không phải dấu ngoặc. Function notation bắt ta khai báo dependency. Nếu `P=P(V,T)` thì pressure có thể thay đổi vì volume hoặc temperature; khi lấy derivative cần nói biến nào thay đổi và biến nào giữ cố định.

## Đạo hàm thường và đạo hàm riêng

Nếu function chỉ phụ thuộc một biến:

```math
v=\frac{dx}{dt}
```

là ordinary derivative.

Nếu field phụ thuộc nhiều biến, ví dụ `T(x,y,z,t)`, đạo hàm riêng (Partial Derivative / 편미분) giữ các variables khác cố định:

```math
\frac{\partial T}{\partial x}
```

hỏi temperature thay đổi theo `x` tại cùng `y,z,t`.

Đây là lý do fluid mechanics, electromagnetism và heat equation dùng `\partial` thay `d`.

## Differential equation: luật nói về rate chứ không trực tiếp nói state

Một phương trình vi phân (Differential Equation / 미분방정식) liên hệ function chưa biết với derivatives của nó.

Newton:

```math
m\frac{d^2x}{dt^2}=F(x,v,t)
```

không trực tiếp cho `x(t)`; nó đặt constraint lên curvature theo time của trajectory. Muốn có trajectory cụ thể còn cần initial conditions như `x(0)` và `v(0)`.

Điều này tương tự một software state machine: transition rule chưa đủ để biết current state nếu không biết initial state và sequence/time evolution.

## Gradient

Cho scalar field `f(x,y,z)`, gradient (Gradient / 그래디언트):

```math
\nabla f=
\left(
\frac{\partial f}{\partial x},
\frac{\partial f}{\partial y},
\frac{\partial f}{\partial z}
\right)
```

Gradient chỉ hướng tăng nhanh nhất của `f`, magnitude cho steepness local.

Vì force trong conservative system:

```math
\vec F=-\nabla U
```

nên particle bị accelerate theo direction potential energy giảm nhanh nhất locally.

## Divergence

Cho vector field `\vec A`, divergence (Divergence / 발산):

```math
\nabla\cdot\vec A
```

đo local “net outflow density”. Nếu divergence positive, một tiny region có nhiều field flux đi ra hơn đi vào; negative giống sink.

Gauss law differential form:

```math
\nabla\cdot\vec E=\frac{\rho}{\varepsilon_0}
```

nói electric charge density là source của electric-field divergence.

Fluid incompressibility có:

```math
\nabla\cdot\vec v=0
```

trong suitable constant-density flow, nghĩa local volume không đang phồng/xẹp do net flow imbalance.

## Curl

Curl (Curl / 회전, 컬) của vector field:

```math
\nabla\times\vec A
```

đo tendency circulation local.

Faraday law:

```math
\nabla\times\vec E=-\frac{\partial\vec B}{\partial t}
```

nói changing magnetic field tạo electric field có local circulation.

Gradient, divergence và curl không phải ba phép toán ngẫu nhiên. Chúng là local differential descriptions của slope, flux source và circulation.

## Fundamental theorem family: local ↔ global

Calculus có một pattern sâu: local derivative information tích phân lại thành global boundary information.

Trong một chiều:

```math
\int_a^b\frac{df}{dx}\,dx=f(b)-f(a)
```

Divergence theorem:

```math
\int_V(\nabla\cdot\vec A)dV
=\oint_{\partial V}\vec A\cdot d\vec S
```

Stokes theorem:

```math
\int_S(\nabla\times\vec A)\cdot d\vec S
=\oint_{\partial S}\vec A\cdot d\vec l
```

Maxwell equations có cả integral và differential forms vì các theorem này nối “điều xảy ra tại từng điểm” với “flux/circulation qua toàn boundary”.

## Số phức và phase

Số phức (Complex Number / 복소수) viết:

```math
z=a+ib
```

với `i^2=-1`.

Euler formula:

```math
e^{i\theta}=\cos\theta+i\sin\theta
```

biến rotation/oscillation thành exponential algebra. Một sinusoid có thể viết:

```math
A\cos(\omega t+\phi)=\Re\left(Ae^{i(\omega t+\phi)}\right)
```

Trong AC circuit, wave, optics và quantum mechanics, complex phase giúp addition và differentiation gọn hơn rất nhiều. Physical observables cuối cùng là real hoặc modulus-squared phù hợp, nhưng intermediate complex representation giữ phase information.

## Matrix và phép biến đổi tuyến tính

Matrix (Matrix / 행렬) nên được hiểu trước hết là biểu diễn của linear transformation sau khi chọn basis.

```math
\vec y=A\vec x
```

không chỉ là phép nhân bảng số; `A` biến vector input thành output theo một linear map.

Rotation, stress transformation, coupled oscillators, polarization optics, quantum operators và computer graphics đều dùng matrix.

## Eigenvector và eigenvalue

Nếu:

```math
A\vec v=\lambda\vec v
```

thì `\vec v` là direction mà transformation không xoay sang direction khác, chỉ scale bởi `\lambda`.

Trong mechanical vibration, eigenvectors là normal modes và eigenvalues liên hệ natural frequencies. Trong quantum mechanics, eigenstates của energy operator có definite energy values. Cùng linear algebra nhưng interpretation vật lý khác.

## Taylor expansion và “nhỏ đến mức nào thì bỏ qua được?”

Một smooth function quanh `x_0`:

```math
f(x_0+\delta)=f(x_0)+f'(x_0)\delta+
\frac12f''(x_0)\delta^2+\cdots
```

Nếu `\delta` đủ nhỏ, higher-order terms giảm nhanh. Đây là basis của linearization.

Ví dụ:

```math
\sin\theta=\theta-\frac{\theta^3}{6}+\cdots
```

Nên khi `|\theta|\ll1` rad:

```math
\sin\theta\approx\theta
```

Approximation tốt hay không phải câu hỏi định tính “góc có vẻ nhỏ”; ta có thể estimate next neglected term `\theta^3/6` để biết error scale.

## Differential versus discrete description

Nature thường được model liên tục, nhưng computer simulation discrete hóa:

```math
\frac{dx}{dt}\approx\frac{x_{n+1}-x_n}{\Delta t}
```

Khi `\Delta t` finite, discretization error xuất hiện. Grid quá thô có thể mất high-frequency modes, vi phạm stability condition hoặc tạo numerical artifacts.

Do đó computational physics luôn có hai câu hỏi khác nhau:

1. Physical model có đúng không?
2. Numerical method có giải model đó đủ chính xác không?

Một simulation có thể tính chính xác một phương trình sai, hoặc tính sai một phương trình đúng.

## Mental Model

Trong Vật lý, toán học không chỉ dùng để tính số. Đạo hàm mô tả local change, tích phân cộng dồn local change thành global effect, differential equation mã hóa luật evolution, còn linear algebra mô tả cách nhiều degree of freedom biến đổi và kết hợp.

## Common Misconceptions

Biết thao tác ký hiệu không đồng nghĩa hiểu mô hình. Mỗi đạo hàm phải có biến đang thay đổi, mỗi tích phân phải có miền tích lũy, mỗi vector phải có không gian mà nó sống trong, và mỗi phương trình vi phân cần điều kiện ban đầu hoặc biên để chọn ra nghiệm vật lý.

## Knowledge Connection

**Liên hệ tiếp:** [Knowledge Connections](../13_connections/00_knowledge_connections.md).
