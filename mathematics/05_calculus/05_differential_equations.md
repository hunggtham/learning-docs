# Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Ordinary differential equation** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Initial giá trị (value / 값) bài toán (problem / 문제)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối phương trình vi phân với điều kiện đầu, nghiệm và ổn định, để phân biệt công thức nghiệm với hành vi của hệ động lực.

Nhiều mô hình khoa học không nói trực tiếp “trạng thái (state / 상태) sẽ bằng bao nhiêu tại thời gian (time / 시간) `t`”. Chúng mô tả **quy luật thay đổi cục bộ**: velocity phụ thuộc position ra sao, population tăng theo kích thước (size / 크기) thế nào, hiện tại (current / 현재) phụ thuộc voltage như thế nào, hay concentration thay đổi theo reaction tỷ lệ (rate / 비율) ra sao.

**Differential equation (미분방정식)** là phương trình chứa một unknown hàm (function / 함수) cùng derivatives của nó. Solution là hàm (function / 함수) có hành vi (behavior / 동작) phù hợp với cục bộ (local / 로컬) law ở mọi điểm (point / 지점) trong lĩnh vực (domain / 도메인).

Ý tưởng cốt lõi là:

```text
local rule of change + initial/boundary information → global behavior
```

## Ordinary differential equation

Một **ordinary differential equation — ODE (상미분방정식)** có một independent variable, thường là thời gian (time / 시간).

First-order ODE có dạng

```math
\frac{dy}{dt}=f(t,y).
```

Second-order ODE có thể có dạng

```math
\frac{d^2y}{dt^2}=f(t,y,y').
```

Thứ tự (order / 순서) của ODE là thứ tự (order / 순서) cao nhất của derivative xuất hiện.

> **Chuyển mạch:** Trong **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Initial giá trị (value / 값) bài toán (problem / 문제)** tiếp nhận điểm tựa từ **Ordinary differential equation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Existence và uniqueness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Initial giá trị (value / 값) bài toán (problem / 문제)

Equation thường cho một family solutions. Initial điều kiện (condition / 조건) chọn trajectory cụ thể.

Ví dụ

```math
y'=2y
```

có family

```math
y(t)=Ce^{2t}.
```

Nếu thêm

```math
y(0)=3,
```

thì `C=3`, nên unique candidate solution là

```math
y(t)=3e^{2t}.
```

Pair của differential equation và initial điều kiện (condition / 조건) gọi là **initial giá trị (value / 값) bài toán (problem / 문제) — IVP**.

> **Chuyển mạch:** Ở chặng này của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Existence và uniqueness** tiếp nhận điểm tựa từ **Initial giá trị (value / 값) bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Separable equations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Existence và uniqueness

Không phải every differential equation với initial điều kiện (condition / 조건) đều có unique solution.

Một important theorem, Picard–Lindelöf, nói roughly rằng nếu `f(t,y)` continuous và sufficiently Lipschitz theo `y` quanh initial điểm (point / 지점), IVP

```math
y'=f(t,y),\qquad y(t_0)=y_0
```

có cục bộ (local / 로컬) unique solution.

Điểm thực dụng là: trước khi “giải” equation, cần biết bài toán (problem / 문제) có well-defined solution hay không.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Separable equations** tiếp nhận điểm tựa từ **Existence và uniqueness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Exponential growth và decay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Separable equations

Nếu equation có dạng

```math
\frac{dy}{dt}=g(t)h(y),
```

và `h(y)≠0`, có thể tách variables:

```math
\frac{dy}{h(y)}=g(t)dt.
```

Sau đó integrate hai vế.

Ví dụ exponential growth:

```math
y'=ky.
```

Ta có

```math
\frac{dy}{y}=kdt,
```

nên

```math
\ln|y|=kt+C,
```

và

```math
y=Ce^{kt}.
```

> **Chuyển mạch:** Trong **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Exponential growth và decay** tiếp nhận điểm tựa từ **Separable equations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **First-order tuyến tính (linear / 선형) ODE** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Exponential growth và decay

Equation

```math
\frac{dP}{dt}=kP
```

nói **absolute growth tỷ lệ (rate / 비율) proportional to hiện tại (current / 현재) amount**.

Nếu `k>0`, growth exponential.

Nếu `k<0`, decay exponential:

```math
P(t)=P_0e^{-\lambda t}.
```

Half-life `T_{1/2}` thỏa

```math
e^{-\lambda T_{1/2}}=\frac12,
```

nên

```math
T_{1/2}=\frac{\ln2}{\lambda}.
```

Exponential không phải arbitrary curve; nó là unique shape có relative tỷ lệ (rate / 비율) constant.

> **Chuyển mạch:** Ở chặng này của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **First-order tuyến tính (linear / 선형) ODE** tiếp nhận điểm tựa từ **Exponential growth và decay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Equilibrium points** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## First-order tuyến tính (linear / 선형) ODE

General form:

```math
y'+p(t)y=q(t).
```

Integrating factor là

```math
\mu(t)=e^{\int p(t)dt}.
```

Nhân equation với `μ` biến left side thành derivative của sản phẩm (product / 제품):

```math
(\mu y)'=\mu q.
```

Do đó

```math
\mu y=\int \mu q\,dt+C.
```

Phương thức (method / 메서드) này xuất hiện trong RC circuits, mixing các mô hình (models / 모델들) và tuyến tính (linear / 선형) phản hồi (response / 응답) các hệ thống (systems / 시스템들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Equilibrium points** tiếp nhận điểm tựa từ **First-order tuyến tính (linear / 선형) ODE** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phase line** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Equilibrium points

Với autonomous equation

```math
y'=f(y),
```

equilibrium `y*` thỏa

```math
f(y^*)=0.
```

Nếu hệ thống (system / 시스템) bắt đầu đúng tại equilibrium, derivative bằng 0 nên trạng thái (state / 상태) không đổi.

Nhưng quan trọng hơn là **stability**: nếu perturb nhẹ khỏi equilibrium, trajectory quay lại hay đi xa?

> **Chuyển mạch:** Trong **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Phase line** tiếp nhận điểm tựa từ **Equilibrium points** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Logistic growth** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phase line

Trong one-dimensional autonomous hệ thống (system / 시스템), sign của `f(y)` cho direction motion.

Nếu `f(y)>0`, trạng thái (state / 상태) tăng. Nếu `f(y)<0`, trạng thái (state / 상태) giảm.

Plot signs trên number line giúp classify equilibria mà không cần closed-form solution.

Stable equilibrium hút nearby trajectories; unstable equilibrium đẩy chúng ra xa.

> **Chuyển mạch:** Ở chặng này của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Logistic growth** tiếp nhận điểm tựa từ **Phase line** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Second-order equations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Logistic growth

Resource-limited mô hình quần thể (population model / 개체군 모델):

```math
P'=rP\left(1-\frac PK\right).
```

Equilibria là

```math
P=0,\qquad P=K.
```

Khi `0<P<K`, growth positive. Khi `P>K`, derivative negative.

`K` là carrying sức chứa (capacity / 용량) và là stable equilibrium cho positive initial populations trong idealized mô hình (model / 모델).

Logistic mô hình (model / 모델) giải thích vì sao exponential growth thường chỉ là cục bộ (local / 로컬) approximation ở giai đoạn đầu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Second-order equations** tiếp nhận điểm tựa từ **Logistic growth** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Characteristic equation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Second-order equations

Newton's second law

```math
F=ma
```

với

```math
a=x''(t)
```

tự nhiên tạo second-order ODE.

Ideal spring:

```math
mx''+kx=0.
```

Chia cho `m`:

```math
x''+\omega^2x=0,
```

với

```math
\omega=\sqrt{k/m}.
```

Solutions là

```math
x(t)=A\cos(\omega t)+B\sin(\omega t).
```

Oscillation xuất hiện vì acceleration luôn kéo trạng thái (state / 상태) về equilibrium.

> **Chuyển mạch:** Trong **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Characteristic equation** tiếp nhận điểm tựa từ **Second-order equations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Damped oscillator** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Characteristic equation

Tuyến tính (linear / 선형) constant-coefficient ODE

```math
ay''+by'+cy=0
```

thử solution

```math
y=e^{rt}.
```

Ta thu được

```math
ar^2+br+c=0.
```

Roots của polynomial quyết định shape solution.

Hai real distinct roots tạo combinations của exponentials.

Repeated gốc (root / 루트) tạo term `te^{rt}`.

Complex roots

```math
r=\alpha\pm i\beta
```

cho oscillation với envelope `e^{\alpha t}`.

Đây là liên kết (connection / 연결) trực tiếp giữa algebraic roots và động (dynamic / 동적) hành vi (behavior / 동작).

> **Chuyển mạch:** Ở chặng này của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Damped oscillator** tiếp nhận điểm tựa từ **Characteristic equation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Forced các hệ thống (systems / 시스템들) và resonance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Damped oscillator

Mô hình (model / 모델)

```math
mx''+cx'+kx=0
```

có characteristic equation

```math
mr^2+cr+k=0.
```

Discriminant

```math
c^2-4mk
```

phân loại hành vi (behavior / 동작).

Nếu negative, roots complex và hệ thống (system / 시스템) underdamped: oscillation decay dần.

Nếu zero, trọng yếu (critical / 중요) damping: return nhanh mà không oscillate trong ideal mô hình (model / 모델).

Nếu positive, overdamped: two real decay modes.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Forced các hệ thống (systems / 시스템들) và resonance** tiếp nhận điểm tựa từ **Damped oscillator** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Các hệ thống (systems / 시스템들) of ODEs** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Forced các hệ thống (systems / 시스템들) và resonance

Nếu có bên ngoài (external / 외부) đầu vào (input / 입력):

```math
mx''+cx'+kx=F(t).
```

Solution thường gồm transient thành phần (component / 컴포넌트) và forced/steady-state thành phần (component / 컴포넌트).

Nếu forcing frequency gần natural frequency và damping nhỏ, phản hồi (response / 응답) amplitude có thể lớn: **resonance**.

Resonance là động (dynamic / 동적) consequence của frequency matching, không chỉ là “rung mạnh”.

> **Chuyển mạch:** Trong **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Các hệ thống (systems / 시스템들) of ODEs** tiếp nhận điểm tựa từ **Forced các hệ thống (systems / 시스템들) và resonance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Stability và eigenvalues** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Các hệ thống (systems / 시스템들) of ODEs

Nhiều các hệ thống (systems / 시스템들) cần véc-tơ (vector / 벡터) trạng thái (state / 상태):

```math
\frac{d\mathbf x}{dt}=F(t,\mathbf x).
```

Tuyến tính (linear / 선형) autonomous hệ thống (system / 시스템):

```math
\mathbf x'=A\mathbf x.
```

Solution formally là

```math
\mathbf x(t)=e^{At}\mathbf x(0).
```

Nếu `A` diagonalizable,

```math
A=PDP^{-1},
```

thì

```math
e^{At}=Pe^{Dt}P^{-1}.
```

Mỗi eigenvalue tạo một động (dynamic / 동적) chế độ (mode / 모드) `e^{\lambda t}`.

> **Chuyển mạch:** Ở chặng này của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Stability và eigenvalues** tiếp nhận điểm tựa từ **Các hệ thống (systems / 시스템들) of ODEs** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nonlinear các hệ thống (systems / 시스템들) và linearization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Stability và eigenvalues

Với continuous hệ tuyến tính (linear system / 선형 시스템)

```math
x'=Ax,
```

nếu mọi eigenvalues có negative real part, origin asymptotically stable.

Nếu có eigenvalue với positive real part, có direction grow exponentially và origin unstable.

Imaginary parts tạo oscillation; real parts tạo growth/decay envelope.

Đây là lý do eigenvalues là ngôn ngữ (language / 언어) trung tâm của điều khiển (control / 제어) lý thuyết (theory / 이론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Nonlinear các hệ thống (systems / 시스템들) và linearization** tiếp nhận điểm tựa từ **Stability và eigenvalues** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phase plane** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nonlinear các hệ thống (systems / 시스템들) và linearization

Cho

```math
x'=F(x).
```

Near equilibrium `x*`, Taylor approximation cho

```math
F(x)\approx F(x^*)+J_F(x^*)(x-x^*).
```

Vì equilibrium thỏa `F(x*)=0`, cục bộ (local / 로컬) dynamics gần đó gần giống

```math
\delta x'=J_F(x^*)\delta x.
```

Eigenvalues của Jacobian giúp classify cục bộ (local / 로컬) stability trong nhiều cases.

Điều này nối nonlinear differential equations với ma trận (matrix / 행렬) calculus và eigenanalysis.

> **Chuyển mạch:** Trong **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Phase plane** tiếp nhận điểm tựa từ **Nonlinear các hệ thống (systems / 시스템들) và linearization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Conservation laws** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phase plane

Với two-dimensional hệ thống (system / 시스템), thay vì plot variables theo thời gian (time / 시간), ta plot trajectory trong trạng thái (state / 상태) không gian (space / 공간) `(x,y)`.

Phase portrait cho thấy equilibria, closed orbits, separatrices và luồng (flow / 흐름) hình học (geometry / 기하학).

Hai trajectories của deterministic ODE với unique solutions không thể cross tại cùng trạng thái (state / 상태)/time-independent véc-tơ (vector / 벡터) trường dữ liệu (field / 필드), vì crossing sẽ imply hai futures từ cùng trạng thái (state / 상태).

> **Chuyển mạch:** Ở chặng này của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Conservation laws** tiếp nhận điểm tựa từ **Phase plane** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ranh giới (boundary / 경계) giá trị (value / 값) problems** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Conservation laws

Một differential equation có thể preserve quantity `E(x)` dọc trajectory:

```math
\frac d{dt}E(x(t))=0.
```

Trong undamped mechanical hệ thống (system / 시스템), total năng lượng (energy / 에너지) thường conserved.

Conserved quantities constrain trajectories vào mức (level / 수준) sets và có thể simplify phân tích (analysis / 분석) mạnh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Conservation laws** đã nêu tiêu chí phân biệt, còn **Ranh giới (boundary / 경계) giá trị (value / 값) problems** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Numerical solution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ranh giới (boundary / 경계) giá trị (value / 값) problems

Không phải mọi bài toán (problem / 문제) cho conditions tại một single initial thời gian (time / 시간).

Ví dụ

```math
y''+\lambda y=0,
```

với

```math
y(0)=0,\qquad y(L)=0
```

là ranh giới (boundary / 경계) giá trị (value / 값) bài toán (problem / 문제).

Chỉ một số values của `λ` cho nontrivial solutions. Đây là origin của eigenvalue problems trong PDE và quantum mechanics.

> **Chuyển mạch:** Trong **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Ranh giới (boundary / 경계) giá trị (value / 값) problems** đã nêu tiêu chí phân biệt, còn **Numerical solution** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Runge–Kutta intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Numerical solution

Nhiều ODE không có elementary closed form hoặc hệ thống (system / 시스템) quá phức tạp để giải symbolic.

Euler phương thức (method / 메서드) dùng cục bộ (local / 로컬) tangent:

```math
x_{n+1}=x_n+h f(t_n,x_n).
```

Nó là first-order phương thức (method / 메서드): toàn cục (global / 전역) lỗi (error / 오류) thường proportional `h` dưới suitable các giả định (assumptions / 가정들).

> **Chuyển mạch:** Ở chặng này của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Runge–Kutta intuition** tiếp nhận điểm tựa từ **Numerical solution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cục bộ (local / 로컬) lỗi (error / 오류) và toàn cục (global / 전역) lỗi (error / 오류)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Runge–Kutta intuition

Euler chỉ lấy slope đầu interval. Runge–Kutta methods mẫu (sample / 표본) multiple slopes trong step để estimate average slope tốt hơn.

Classical RK4:

```math
k_1=f(t_n,x_n),
```

```math
k_2=f(t_n+h/2,x_n+hk_1/2),
```

```math
k_3=f(t_n+h/2,x_n+hk_2/2),
```

```math
k_4=f(t_n+h,x_n+hk_3),
```

và

```math
x_{n+1}=x_n+\frac h6(k_1+2k_2+2k_3+k_4).
```

RK4 có high accuracy cho many smooth nonstiff problems.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Cục bộ (local / 로컬) lỗi (error / 오류) và toàn cục (global / 전역) lỗi (error / 오류)** tiếp nhận điểm tựa từ **Runge–Kutta intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Stiff equations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cục bộ (local / 로컬) lỗi (error / 오류) và toàn cục (global / 전역) lỗi (error / 오류)

Cục bộ (local / 로컬) truncation lỗi (error / 오류) đo lỗi (error / 오류) tạo trong một step nếu starting giá trị (value / 값) chính xác (exact / 정확한).

Toàn cục (global / 전역) lỗi (error / 오류) là accumulated lỗi (error / 오류) sau nhiều steps.

Một phương thức (method / 메서드) cục bộ (local / 로컬) rất chính xác vẫn cần stability để lỗi (error / 오류) không amplify qua repeated steps.

> **Chuyển mạch:** Trong **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Stiff equations** tiếp nhận điểm tựa từ **Cục bộ (local / 로컬) lỗi (error / 오류) và toàn cục (global / 전역) lỗi (error / 오류)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Backward Euler** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Stiff equations

Một ODE gọi là **stiff** khi có nhiều thời gian (time / 시간) scales rất khác nhau làm tường minh (explicit / 명시적) methods cần extremely small step để remain stable, dù solution itself có thể smooth.

Ví dụ chemical kinetics có fast reactions và slow processes cùng tồn tại.

Implicit methods như backward Euler thường stable hơn cho stiff problems.

> **Chuyển mạch:** Ở chặng này của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Backward Euler** tiếp nhận điểm tựa từ **Stiff equations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Adaptive step kích thước (size / 크기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Backward Euler

Backward Euler dùng

```math
x_{n+1}=x_n+h f(t_{n+1},x_{n+1}).
```

Unknown `x_{n+1}` xuất hiện cả hai vế, nên mỗi step có thể cần solve nonlinear equation.

Đổi lại, phương thức (method / 메서드) có stronger stability properties.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Adaptive step kích thước (size / 크기)** tiếp nhận điểm tựa từ **Backward Euler** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sự kiện (event / 이벤트) detection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Adaptive step kích thước (size / 크기)

Fixed step `h` có thể waste computation ở smooth regions và thiếu accuracy ở rapidly changing regions.

Adaptive solvers estimate cục bộ (local / 로컬) lỗi (error / 오류) rồi tự tăng/giảm step kích thước (size / 크기) để đạt tolerance mục tiêu (target / 대상).

Hiện đại (modern / 현대적) ODE solvers thường ưu tiên tolerance hơn việc người dùng chọn một `h` cứng.

> **Chuyển mạch:** Trong **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Sự kiện (event / 이벤트) detection** tiếp nhận điểm tựa từ **Adaptive step kích thước (size / 크기)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dimensionless variables** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sự kiện (event / 이벤트) detection

Trong simulation, ta đôi khi quan tâm thời điểm solution cross threshold, va chạm hoặc switch regime.

Solver cần locate sự kiện (event / 이벤트) thời gian (time / 시간) giữa numerical steps, thường bằng interpolation/gốc (root / 루트) finding, thay vì chỉ kiểm tra discrete sampled times.

> **Chuyển mạch:** Ở chặng này của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Dimensionless variables** tiếp nhận điểm tựa từ **Sự kiện (event / 이벤트) detection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Differential equations và Laplace transform** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dimensionless variables

Scaling variables có thể reveal key dimensionless parameters và improve numerical conditioning.

Ví dụ thay

```math
t=\tau T,
```

có thể biến constants thành ratios thể hiện relative thời gian (time / 시간) scales.

Non-dimensionalization giúp so sánh các hệ thống (systems / 시스템들) khác units và nhận ra dominant mechanisms.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Differential equations và Laplace transform** tiếp nhận điểm tựa từ **Dimensionless variables** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Differential equations và xác suất (probability / 확률)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Differential equations và Laplace transform

Tuyến tính (linear / 선형) ODE với initial conditions có thể transform thành algebraic equation trong `s` lĩnh vực (domain / 도메인).

Ví dụ differentiation trở thành multiplication by `s` cộng initial-condition terms.

Điều này hữu ích cho tuyến tính (linear / 선형) time-invariant các hệ thống (systems / 시스템들) và điều khiển (control / 제어), đặc biệt khi đầu vào (input / 입력) có steps/impulses.

> **Chuyển mạch:** Trong **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Differential equations và xác suất (probability / 확률)** tiếp nhận điểm tựa từ **Differential equations và Laplace transform** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Differential equations và machine học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Differential equations và xác suất (probability / 확률)

Stochastic differential equations thêm random forcing, schematic:

```math
dX_t=\mu(X_t,t)dt+\sigma(X_t,t)dW_t.
```

Ordinary calculus không đủ vì Brownian paths không differentiable theo classical sense; stochastic calculus phát triển rules mới.

Đây là cầu nối (bridge / 브리지) từ deterministic dynamics sang stochastic processes.

> **Chuyển mạch:** Ở chặng này của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Differential equations và machine học tập (learning / 학습)** tiếp nhận điểm tựa từ **Differential equations và xác suất (probability / 확률)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Differential equations và machine học tập (learning / 학습)

Continuous-depth neural networks như Neural ODEs xem hidden trạng thái (state / 상태) evolution là

```math
\frac{dh}{dt}=f_\theta(t,h).
```

Huấn luyện (training / 학습) cần differentiate through numerical ODE solution.

Dù hiện thực (implementation / 구현) hiện đại, underlying mathematics vẫn là hệ động (dynamic system / 동적 시스템), numerical tích hợp (integration / 통합) và sensitivity phân tích (analysis / 분석).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Differential equations và machine học tập (learning / 학습)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Differential equation là một **generator của trajectories**. Nó chỉ cục bộ (local / 로컬) velocity của trạng thái (state / 상태) tại mỗi điểm (point / 지점). Initial điều kiện (condition / 조건) đặt hệ thống (system / 시스템) vào một điểm (point / 지점); véc-tơ (vector / 벡터) trường dữ liệu (field / 필드) nói nó phải đi direction nào; tích hợp (integration / 통합) qua thời gian (time / 시간) tạo toàn cục (global / 전역) trajectory.

Tuyến tính (linear / 선형) các hệ thống (systems / 시스템들) có thể tách thành eigenmodes. Nonlinear các hệ thống (systems / 시스템들) thường được hiểu cục bộ (local / 로컬) bằng linearization, toàn cục (global / 전역) bằng phase hình học (geometry / 기하학), invariants và numerical simulation.

> **Chuyển mạch:** Trong **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

Có differential equation chưa chắc có unique solution; conditions về regularity và initial/ranh giới (boundary / 경계) dữ liệu (data / 데이터) matters. Có closed-form expression cũng không có nghĩa mô hình (model / 모델) đúng về vật lý (physical / 물리적) hệ thống (system / 시스템).

Numerical solver không “giải chính xác bằng máy tính”. Nó tạo approximation với truncation, floating-point và modeling errors.

Giảm step kích thước (size / 크기) không luôn chữa mọi vấn đề; stiff các hệ thống (systems / 시스템들) cần stability-aware methods.

Eigenvalue stability criteria của linearization là cục bộ (local / 로컬) statements cho nonlinear các hệ thống (systems / 시스템들) và có edge cases khi eigenvalues nằm trên imaginary axis.

> **Chuyển mạch:** Ở chặng này của **Phương trình vi phân và hệ động lực: từ cục bộ (local / 로컬) law đến toàn cục (global / 전역) trajectory**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Chapter này nối [Integrals](./03_integrals_and_accumulation.md), [Eigenvalues](../04_vectors_linear_algebra/04_eigenvalues_and_eigenvectors.md), [Taylor approximation](./08_taylor_series_and_local_approximation.md), [PDE](./10_partial_differential_equations_and_fields_intro.md), [Laplace/Z-transform](../09_connections/06_laplace_z_transform_and_dynamic_systems.md), [Stochastic processes](../06_probability_statistics/11_stochastic_processes_markov_chains_and_time_series.md) và [Dynamic programming/optimal control](../08_optimization_numerical/06_dynamic_programming_bellman_and_optimal_control.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
