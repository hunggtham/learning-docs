# Nhập môn phương trình vi phân riêng phần: khi trạng thái (state / 상태) phụ thuộc vào không gian và thời gian

> **Mạch đọc:** [README](../README.md) là owner của **Nhập môn phương trình vi phân riêng phần: khi trạng thái (state / 상태) phụ thuộc vào không gian và thời gian**; đặt chapter sau ODE/functions và trước numerical methods. Từ **Trường dữ liệu (field / 필드)** nối qua heat equation, wave/Laplace equations, boundary/initial conditions và canonical classifications, rồi kết thúc ở numerical simulation để thấy PDE biến giả định vật lý thành mô hình tính toán.

Ordinary Differential Equation (ODE / 상미분방정식) thường mô tả một trạng thái (state / 상태) thay đổi theo một biến độc lập, thường là thời gian (time / 시간). Nhưng nhiệt độ trong một căn phòng, áp suất trong chất lỏng, độ cao của sóng hay electric potential không chỉ phụ thuộc thời gian (time / 시간); chúng thay đổi theo vị trí. Khi unknown là một **trường dữ liệu (field / 필드) / 장** như `u(x,t)` hoặc `u(x,y,z,t)`, laws of thay đổi (change / 변경) dẫn tự nhiên đến **phương trình vi phân riêng phần (Partial Differential Equation, PDE / 편미분방정식)**.

PDE là một lĩnh vực lớn. Chương này không cố giải toàn bộ PDE lý thuyết (theory / 이론); mục tiêu là hiểu vì sao PDE xuất hiện, three chuẩn gốc (canonical / 정본) types, vai trò của ranh giới (boundary / 경계)/initial conditions và liên hệ với numerical simulation.

## Trường dữ liệu (field / 필드): từ một number sang một giá trị (value / 값) tại mỗi điểm (point / 지점)

Một scalar trường dữ liệu (field / 필드) gán một scalar cho mỗi điểm (point / 지점). Temperature có thể viết

```math
T=T(x,y,z,t).
```

Một véc-tơ (vector / 벡터) trường dữ liệu (field / 필드) gán véc-tơ (vector / 벡터) cho mỗi điểm (point / 지점), như velocity trường dữ liệu (field / 필드) của fluid:

```math
\mathbf v=\mathbf v(x,y,z,t).
```

Khi trường dữ liệu (field / 필드) thay đổi, partial derivatives đo tỷ lệ (rate / 비율) theo từng coordinate. `\partial T/\partial t` đo cục bộ (local / 로컬) thời gian (time / 시간) thay đổi (change / 변경) tại fixed position; độ dốc (gradient / 기울기) `\nabla T` mô tả spatial direction mà temperature tăng nhanh nhất.

> **Chuyển mạch:** Trong **Nhập môn phương trình vi phân riêng phần: khi trạng thái (state / 상태) phụ thuộc vào không gian và thời gian**, **Trường dữ liệu (field / 필드): từ một number sang một giá trị (value / 값) tại mỗi điểm (point / 지점)** nêu điều cần giải thích; **Heat equation: diffusion từ cục bộ (local / 로컬) imbalance** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Wave equation: propagation thay vì smoothing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Heat equation: diffusion từ cục bộ (local / 로컬) imbalance

Trong một thanh 1D, heat equation điển hình là

```math
\frac{\partial u}{\partial t}
=
\alpha\frac{\partial^2u}{\partial x^2},
```

trong đó `u(x,t)` là temperature và `\alpha` là thermal diffusivity.

Second derivative `u_{xx}` đo curvature của temperature profile. Nếu một điểm (point / 지점) nóng hơn neighbors, profile có curvature theo hướng khiến heat luồng (flow / 흐름) làm điểm (point / 지점) đó giảm nhiệt; nếu lạnh hơn neighbors, nó nhận heat. PDE nói cục bộ (local / 로컬) thời gian (time / 시간) thay đổi (change / 변경) proportional với cục bộ (local / 로컬) spatial imbalance.

Đây là **diffusion equation / 확산방정식**. Same mathematical cấu trúc (structure / 구조) mô tả diffusion của particles, smoothing của concentration và một số algorithms làm mờ ảnh (image / 이미지).

> **Chuyển mạch:** Ở chặng này của **Nhập môn phương trình vi phân riêng phần: khi trạng thái (state / 상태) phụ thuộc vào không gian và thời gian**, **Wave equation: propagation thay vì smoothing** tiếp nhận điểm tựa từ **Heat equation: diffusion từ cục bộ (local / 로컬) imbalance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Laplace và Poisson equations: equilibrium fields** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Wave equation: propagation thay vì smoothing

Một ideal vibrating string có wave equation

```math
\frac{\partial^2u}{\partial t^2}
=
c^2\frac{\partial^2u}{\partial x^2}.
```

Khác heat equation, thời gian (time / 시간) derivative là second thứ tự (order / 순서). Nó liên hệ acceleration của displacement với spatial curvature. Kết quả là disturbance có xu hướng propagate như waves thay vì chỉ diffuse away.

Speed `c` xác định propagation speed. Đây là nơi trigonometric functions, complex exponentials và Fourier phân tích (analysis / 분석) trở nên tự nhiên: sinusoidal waves là eigenmodes của nhiều tuyến tính (linear / 선형) PDE các hệ thống (systems / 시스템들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhập môn phương trình vi phân riêng phần: khi trạng thái (state / 상태) phụ thuộc vào không gian và thời gian**, **Laplace và Poisson equations: equilibrium fields** tiếp nhận điểm tựa từ **Wave equation: propagation thay vì smoothing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Initial conditions và ranh giới (boundary / 경계) conditions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Laplace và Poisson equations: equilibrium fields

Khi hệ thống (system / 시스템) đạt steady trạng thái (state / 상태), thời gian (time / 시간) derivative có thể biến mất. Heat equation ở equilibrium dẫn đến

```math
\nabla^2u=0,
```

đó là **Laplace equation / 라플라스 방정식**. Nếu có sources,

```math
\nabla^2u=f,
```

ta có **Poisson equation / 푸아송 방정식**.

Các equations này xuất hiện trong electrostatics, gravitation, steady heat luồng (flow / 흐름) và potential lý thuyết (theory / 이론). Operator

```math
\nabla^2
```

là **Laplacian / 라플라시안**, tổng các second partial derivatives theo spatial coordinates.

> **Chuyển mạch:** Trong **Nhập môn phương trình vi phân riêng phần: khi trạng thái (state / 상태) phụ thuộc vào không gian và thời gian**, **Laplace và Poisson equations: equilibrium fields** đã nêu tiêu chí phân biệt, còn **Initial conditions và ranh giới (boundary / 경계) conditions** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Classification: elliptic, parabolic, hyperbolic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Initial conditions và ranh giới (boundary / 경계) conditions

PDE không được xác định chỉ bởi equation. Ta cần biết trạng thái (state / 상태) ban đầu và cách lĩnh vực (domain / 도메인) tương tác với ranh giới (boundary / 경계).

Với heat equation, **initial điều kiện (condition / 조건) / 초기조건** có thể là

```math
u(x,0)=f(x).
```

Một **Dirichlet ranh giới (boundary / 경계) điều kiện (condition / 조건) / 디리클레 경계조건** đặt giá trị (value / 값) ở ranh giới (boundary / 경계):

```math
u(0,t)=0,
\qquad
u(L,t)=0.
```

Một **Neumann ranh giới (boundary / 경계) điều kiện (condition / 조건) / 노이만 경계조건** đặt derivative normal, thường tương ứng với flux:

```math
\frac{\partial u}{\partial n}=0.
```

Điều này có thể biểu diễn insulated ranh giới (boundary / 경계) — không có heat luồng (flow / 흐름) xuyên qua.

Same PDE với ranh giới (boundary / 경계) conditions khác có thể cho hành vi (behavior / 동작) hoàn toàn khác. Vì vậy ranh giới (boundary / 경계) conditions là một phần của mathematical mô hình (model / 모델), không phải chi tiết phụ sau khi đã “có phương trình”.

> **Chuyển mạch:** Ở chặng này của **Nhập môn phương trình vi phân riêng phần: khi trạng thái (state / 상태) phụ thuộc vào không gian và thời gian**, **Initial conditions và ranh giới (boundary / 경계) conditions** đã nêu tiêu chí phân biệt, còn **Classification: elliptic, parabolic, hyperbolic** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Separation of variables và eigenfunctions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Classification: elliptic, parabolic, hyperbolic

Tuyến tính (linear / 선형) second-order PDE thường được phân loại thành elliptic, parabolic và hyperbolic. Không cần học classification như taxonomy rời rạc; nó phản ánh qualitative hành vi (behavior / 동작).

**Elliptic** equations như Laplace thường mô tả equilibrium; influence có tính toàn cục (global / 전역). **Parabolic** equations như heat mô tả diffusion và smoothing theo thời gian (time / 시간). **Hyperbolic** equations như wave mô tả propagation với finite-speed characteristics.

Classification ảnh hưởng cả mathematical lý thuyết (theory / 이론) lẫn numerical phương thức (method / 메서드) thích hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhập môn phương trình vi phân riêng phần: khi trạng thái (state / 상태) phụ thuộc vào không gian và thời gian**, **Separation of variables và eigenfunctions** tiếp nhận điểm tựa từ **Classification: elliptic, parabolic, hyperbolic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Numerical PDE: grid hóa không gian và thời gian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Separation of variables và eigenfunctions

Một classical technique là giả sử solution có sản phẩm (product / 제품) form

```math
u(x,t)=X(x)T(t).
```

Thay vào PDE có thể tách bài toán (problem / 문제) thành ODEs. Với heat equation,

```math
X(x)T'(t)=\alpha X''(x)T(t).
```

Chia cho `\alpha XT`:

```math
\frac{T'}{\alpha T}=\frac{X''}{X}.
```

Vế trái chỉ phụ thuộc `t`, vế phải chỉ phụ thuộc `x`; để equality giữ cho mọi `x,t`, cả hai phải bằng cùng constant. Ta thu được hai ODEs.

Ranh giới (boundary / 경계) conditions thường chỉ cho phép một discrete set các spatial modes `X_n`. Đây chính là cầu nối (bridge / 브리지) tới eigenvalues/eigenvectors và Fourier series: arbitrary initial profile được phân rã thành eigenmodes, mỗi chế độ (mode / 모드) tiến hóa theo law riêng.

> **Chuyển mạch:** Trong **Nhập môn phương trình vi phân riêng phần: khi trạng thái (state / 상태) phụ thuộc vào không gian và thời gian**, **Numerical PDE: grid hóa không gian và thời gian** tiếp nhận điểm tựa từ **Separation of variables và eigenfunctions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **PDE trong graphics, ML và kỹ thuật (engineering / 엔지니어링)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Numerical PDE: grid hóa không gian và thời gian

Đa số realistic PDE không có closed-form solution dễ dùng. Ta discretize lĩnh vực (domain / 도메인) thành grid hoặc mesh. Với finite difference, second derivative có approximation

```math
\frac{\partial^2u}{\partial x^2}(x_i)
\approx
\frac{u_{i+1}-2u_i+u_{i-1}}{\Delta x^2}.
```

Heat equation trở thành cập nhật (update / 업데이트) quy tắc (rule / 규칙) trên array values. Đây là điểm PDE gặp numerical tuyến tính (linear / 선형) algebra, sparse matrices, parallel computing và GPU.

Nhưng discretization tạo thêm questions về **stability / 안정성**, **consistency / 일관성** và **convergence / 수렴성**. Một scheme nhìn hợp lý về algebra có thể explode numerically nếu timestep quá lớn. Ví dụ tường minh (explicit / 명시적) heat scheme thường có stability restriction liên hệ `\Delta t` với `\Delta x^2`.

> **Chuyển mạch:** Ở chặng này của **Nhập môn phương trình vi phân riêng phần: khi trạng thái (state / 상태) phụ thuộc vào không gian và thời gian**, **PDE trong graphics, ML và kỹ thuật (engineering / 엔지니어링)** tiếp nhận điểm tựa từ **Numerical PDE: grid hóa không gian và thời gian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## PDE trong graphics, ML và kỹ thuật (engineering / 엔지니어링)

Computer graphics dùng PDE trong fluid simulation, cloth, diffusion và xử lý ảnh (image processing / 이미지 처리). Computational fluid dynamics giải Navier–Stokes equations trên meshes. Finance dùng PDE như Black–Scholes dưới certain các giả định (assumptions / 가정들). Physics-informed neural networks đưa PDE residual vào hàm mất mát (loss function / 손실 함수), biến differential law thành huấn luyện (training / 학습) ràng buộc (constraint / 제약조건).

Trong xử lý ảnh (image processing / 이미지 처리), diffusion-like PDE có thể smooth noise. Nhưng isotropic diffusion cũng làm mờ edges; nonlinear diffusion cố preserve important boundaries. Đây là ví dụ rõ rằng mathematical mô hình (model / 모델) quyết định loại thông tin (information / 정보) bị giữ hay mất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhập môn phương trình vi phân riêng phần: khi trạng thái (state / 상태) phụ thuộc vào không gian và thời gian**, sau nội dung của **PDE trong graphics, ML và kỹ thuật (engineering / 엔지니어링)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết kiến thức (knowledge connection / 지식 연결)

PDE ngồi ở intersection của multivariable calculus, véc-tơ (vector / 벡터) calculus, tuyến tính (linear / 선형) algebra, Fourier phân tích (analysis / 분석), differential equations và numerical methods. độ dốc (gradient / 기울기)/divergence/curl mô tả fields; eigenfunctions cung cấp natural modes; Fourier đổi biểu diễn (representation / 표현); sparse matrices xuất hiện sau discretization; tối ưu hóa (optimization / 최적화) xuất hiện trong variational formulations.

Một powerful viewpoint là xem PDE như “cục bộ (local / 로컬) law applied everywhere”. ODE nói trạng thái (state / 상태) tại một điểm (point / 지점) in state-space thay đổi theo law; PDE nói trường dữ liệu (field / 필드) tại mọi spatial điểm (point / 지점) thay đổi theo cục bộ (local / 로컬) differential relationships và bị coupled qua neighbors.

> **Chuyển mạch:** Trong **Nhập môn phương trình vi phân riêng phần: khi trạng thái (state / 상태) phụ thuộc vào không gian và thời gian**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Liên kết kiến thức (knowledge connection / 지식 연결)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> PDE là cách viết một luật cục bộ (local / 로컬) cho một trường dữ liệu (field / 필드) trải trên không gian. Differential operator đo cục bộ (local / 로컬) shape hoặc flux; ranh giới (boundary / 경계)/initial conditions xác định môi trường (environment / 환경); solution là toàn cục (global / 전역) hành vi (behavior / 동작) xuất hiện khi cùng cục bộ (local / 로컬) law được thỏa ở mọi điểm (point / 지점).

> **Chuyển mạch:** Ở chặng này của **Nhập môn phương trình vi phân riêng phần: khi trạng thái (state / 상태) phụ thuộc vào không gian và thời gian**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

PDE không đơn giản là ODE “có nhiều biến hơn”. Spatial coupling, boundaries và hàm (function / 함수) spaces làm bài toán (problem / 문제) qualitatively khác.

Có PDE và ranh giới (boundary / 경계) conditions chưa chắc luôn có unique smooth solution; existence, uniqueness và regularity là questions riêng. Numerical solution cũng không tự động là solution thật: cần analyze discretization lỗi (error / 오류) và stability.

Cuối cùng, Fourier methods không “giải mọi PDE”. Chúng đặc biệt mạnh với tuyến tính (linear / 선형) các hệ thống (systems / 시스템들) và regular domains/boundaries; nonlinearities, irregular hình học (geometry / 기하학) hoặc changing boundaries có thể yêu cầu methods khác.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
