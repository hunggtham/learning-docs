# Véc-tơ (vector / 벡터) calculus: cục bộ (local / 로컬) trường dữ liệu (field / 필드) hành vi (behavior / 동작) và toàn cục (global / 전역) conservation

> **Mạch đọc:** Đọc **véc-tơ (vector / 벡터) calculus: cục bộ (local / 로컬) trường dữ liệu (field / 필드) hành vi (behavior / 동작) và toàn cục (global / 전역) conservation** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Scalar trường dữ liệu (field / 필드) và véc-tơ (vector / 벡터) trường dữ liệu (field / 필드)** sang **2. độ dốc (gradient / 기울기): đầu ra (output / 출력) tăng nhanh nhất về đâu?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Véc-tơ (vector / 벡터) calculus nghiên cứu scalar fields và véc-tơ (vector / 벡터) fields trên không gian (space / 공간). Nó là ngôn ngữ tự nhiên của temperature, fluid luồng (flow / 흐름), force, electric trường dữ liệu (field / 필드), heat flux và nhiều các hệ thống (systems / 시스템들) phân bố liên tục.

Cốt lõi (core / 핵심) mental chuỗi (chain / 사슬):

```text
field
→ local derivative
→ directional behavior
→ circulation / flux
→ integral theorem
→ conservation law
```

Điểm quan trọng không phải học riêng `gradient`, `divergence`, `curl`; mà là hiểu mỗi operator trả lời **một câu hỏi hình học khác nhau**.

## 1. Scalar trường dữ liệu (field / 필드) và véc-tơ (vector / 벡터) trường dữ liệu (field / 필드)

Scalar trường dữ liệu (field / 필드):

```math
f(x,y,z)
```

gán một scalar cho mỗi điểm (point / 지점), ví dụ temperature.

Véc-tơ (vector / 벡터) trường dữ liệu (field / 필드):

```math
F(x,y,z)=(P,Q,R)
```

gán một véc-tơ (vector / 벡터) cho mỗi điểm (point / 지점), ví dụ fluid velocity.

Trường dữ liệu (field / 필드) là hàm (function / 함수) có lĩnh vực (domain / 도메인) là không gian (space / 공간). Vì vậy véc-tơ (vector / 벡터) calculus nối trực tiếp với multivariable functions.

## 2. độ dốc (gradient / 기울기): đầu ra (output / 출력) tăng nhanh nhất về đâu?

Với scalar trường dữ liệu (field / 필드) `f`:

```math
\nabla f=
\begin{bmatrix}
f_x\\f_y\\f_z
\end{bmatrix}.
```

Directional derivative theo đơn vị (unit / 단위) véc-tơ (vector / 벡터) `u`:

```math
D_uf=\nabla f\cdot u.
```

Cauchy–Schwarz cho:

```math
D_uf\le \|\nabla f\|.
```

Maximum xảy ra khi `u` cùng direction với độ dốc (gradient / 기울기). Vì vậy:

```text
direction của gradient → steepest local increase
magnitude của gradient → maximum local rate
```

Độ dốc (gradient / 기울기) không phải “mũi tên hướng lên đồ thị (graph / 그래프)”; nó sống trong đầu vào (input / 입력) không gian (space / 공간).

## 3. Vì sao độ dốc (gradient / 기울기) vuông góc mức (level / 수준) set?

Trên mức (level / 수준) surface:

```math
f(x,y,z)=c.
```

Nếu đi infinitesimally theo tangent direction `v`, first-order thay đổi (change / 변경) bằng 0:

```math
\nabla f\cdot v=0.
```

Do đó độ dốc (gradient / 기울기) orthogonal với mọi tangent direction, tức là normal véc-tơ (vector / 벡터) của mức (level / 수준) surface.

Đây là liên kết (connection / 연결) trực tiếp giữa calculus và hình học (geometry / 기하학) of các ràng buộc (constraints / 제약조건들).

## 4. độ dốc (gradient / 기울기) và tối ưu hóa (optimization / 최적화)

Nếu `f` là mục tiêu (objective / 목표), độ dốc (gradient / 기울기) chỉ direction cục bộ (local / 로컬) increase. Negative độ dốc (gradient / 기울기) cho steepest descent dưới Euclidean chỉ số (metric / 지표).

Ràng buộc (constraint / 제약조건) surface `g(x)=0` có normal `\nabla g`. Tại constrained optimum, nếu smooth regularity conditions giữ, `\nabla f` phải align với `\nabla g`, dẫn tới Lagrange multiplier điều kiện (condition / 조건).

Véc-tơ (vector / 벡터) calculus vì vậy đứng ngay dưới constrained tối ưu hóa (optimization / 최적화).

## 5. Divergence: cục bộ (local / 로컬) nguồn (source / 소스)/sink strength

Với

```math
F=(P,Q,R),
```

divergence:

```math
\nabla\cdot F
=
\frac{\partial P}{\partial x}
+
\frac{\partial Q}{\partial y}
+
\frac{\partial R}{\partial z}.
```

Trực giác: lấy một tiny volume quanh điểm (point / 지점). Nếu nhiều trường dữ liệu (field / 필드) “đi ra” hơn “đi vào”, divergence positive; nếu net inflow, negative.

Divergence là **net outward flux per đơn vị (unit / 단위) volume trong limit**.

## 6. Divergence từ cục bộ (local / 로컬) expansion

Ví dụ:

```math
F(x,y,z)=(x,y,z).
```

Khi đó:

```math
\nabla\cdot F=1+1+1=3.
```

Trường dữ liệu (field / 필드) hướng ra ngoài và magnitude tăng theo distance, nên mọi tiny region có net outward luồng (flow / 흐름).

Ngược lại constant trường dữ liệu (field / 필드):

```math
F=(1,0,0)
```

có divergence 0: trường dữ liệu (field / 필드) đi xuyên region nhưng không được tạo/huỷ bên trong.

## 7. Curl: cục bộ (local / 로컬) circulation tendency

Curl:

```math
\nabla\times F
=
\begin{bmatrix}
R_y-Q_z\\
P_z-R_x\\
Q_x-P_y
\end{bmatrix}.
```

Paddle-wheel intuition hữu ích: đặt tiny wheel vào luồng (flow / 흐름); curl liên quan axis và tendency quay.

Nhưng curl không đơn giản bằng “trường dữ liệu (field / 필드) nhìn xoáy”. Nó là differential measure của circulation density.

## 8. Worked example: rigid rotation

Xét 2D rotation trường dữ liệu (field / 필드) embedded in 3D:

```math
F(x,y,z)=(-y,x,0).
```

Divergence:

```math
\nabla\cdot F=0.
```

Curl:

```math
\nabla\times F=(0,0,2).
```

Trường dữ liệu (field / 필드) không expand locally nhưng có rotational tendency. Đây là ví dụ rõ để tách divergence khỏi curl.

## 9. Conservative trường dữ liệu (field / 필드) và potential

Nếu

```math
F=\nabla\phi,
```

thì `F` là độ dốc (gradient / 기울기) trường dữ liệu (field / 필드)/conservative trường dữ liệu (field / 필드).

Line integral từ `A` tới `B`:

```math
\int_C F\cdot dr
=
\phi(B)-\phi(A)
```

trong suitable lĩnh vực (domain / 도메인).

Do đó công việc (work / 작업) không phụ thuộc đường dẫn (path / 경로); chỉ endpoints matter.

Trong mechanics, potential năng lượng (energy / 에너지) cho conservative force là manifestation của cấu trúc (structure / 구조) này.

## 10. Curl zero có đủ để conservative không?

Ta luôn có:

```math
\nabla\times(\nabla\phi)=0.
```

Nhưng reverse implication cần lĩnh vực (domain / 도메인) các giả định (assumptions / 가정들) như simply connectedness.

Một trường dữ liệu (field / 필드) có curl zero trên lĩnh vực (domain / 도메인) có hole vẫn có thể có nonzero circulation quanh hole. Đây là ví dụ quan trọng: **cục bộ (local / 로컬) điều kiện (condition / 조건) không luôn imply toàn cục (global / 전역) cấu trúc (structure / 구조)**.

## 11. Line integral: accumulate trường dữ liệu (field / 필드) along a đường dẫn (path / 경로)

Curve parameterization:

```math
r(t),\quad a\le t\le b.
```

Véc-tơ (vector / 벡터) line integral:

```math
\int_C F\cdot dr
=
\int_a^b F(r(t))\cdot r'(t)\,dt.
```

Dot sản phẩm (product / 제품) chỉ lấy thành phần (component / 컴포넌트) của trường dữ liệu (field / 필드) theo tangent direction.

Trong mechanics:

```math
W=\int_C F\cdot dr
```

là công việc (work / 작업) along đường dẫn (path / 경로).

## 12. Scalar line integral

Một scalar trường dữ liệu (field / 필드) cũng có thể tích phân dọc curve:

```math
\int_C f\,ds.
```

Ví dụ wire có tuyến tính (linear / 선형) density `\rho`; mass:

```math
M=\int_C \rho\,ds.
```

Điều này nhắc rằng “line integral” không chỉ có một form.

## 13. Surface integral và flux

Flux qua oriented surface:

```math
\iint_S F\cdot n\,dS.
```

`n` là đơn vị (unit / 단위) normal. Dot sản phẩm (product / 제품) chọn normal thành phần (component / 컴포넌트): trường dữ liệu (field / 필드) tangent surface không góp flux xuyên surface.

Đổi orientation của normal thì flux đổi dấu.

## 14. Divergence theorem: cục bộ (local / 로컬) nguồn (source / 소스) → toàn cục (global / 전역) flux

```math
\iiint_V \nabla\cdot F\,dV
=
\iint_{\partial V}F\cdot n\,dS.
```

Interpretation:

> Tổng net nguồn (source / 소스) density bên trong volume bằng net outward luồng (flow / 흐름) qua ranh giới (boundary / 경계).

Đây không chỉ là tích hợp (integration / 통합) trick. Nó là mathematical form của conservation lập luận (reasoning / 추론).

## 15. Continuity equation

Nếu `\rho(x,t)` là density và `J` là flux, cục bộ (local / 로컬) conservation thường có form:

```math
\frac{\partial \rho}{\partial t}
+
\nabla\cdot J=0.
```

Nếu density giảm tại điểm (point / 지점), mass/charge/xác suất (probability / 확률) phải luồng (flow / 흐름) ra; nếu tăng, phải luồng (flow / 흐름) vào hoặc nguồn (source / 소스) term tồn tại.

Đây là một trong các equations sâu nhất nối divergence với Physics.

## 16. Stokes' theorem: cục bộ (local / 로컬) curl → ranh giới (boundary / 경계) circulation

```math
\iint_S (\nabla\times F)\cdot n\,dS
=
\oint_{\partial S}F\cdot dr.
```

Left side tích lũy cục bộ (local / 로컬) rotation trên surface; right side đo circulation quanh ranh giới (boundary / 경계).

Stokes nói rằng nội bộ (internal / 내부) rotational tendency account cho ranh giới (boundary / 경계) circulation.

## 17. Green's theorem trong 2D

Green's theorem là 2D phiên bản (version / 버전) nối line integral quanh ranh giới (boundary / 경계) với area integral bên trong.

Một form:

```math
\oint_C P\,dx+Q\,dy
=
\iint_D
\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dA.
```

Nó là cầu nối (bridge / 브리지) dễ thấy trước generalized Stokes theorem.

## 18. Fundamental theorem mẫu (pattern / 패턴)

Fundamental Theorem of Calculus:

```math
\int_a^b f'(x)\,dx=f(b)-f(a).
```

Divergence theorem:

```text
integral of divergence inside
= flux on boundary
```

Stokes theorem:

```text
integral of curl on surface
= circulation on boundary
```

Unified mô hình tư duy (mental model / 사고 모델):

> integrate a derivative over a region → recover original đối tượng (object / 객체) on the ranh giới (boundary / 경계).

Generalized Stokes theorem formalizes toàn bộ mẫu (pattern / 패턴) này.

## 19. Coordinate các hệ thống (systems / 시스템들) và Jacobian

Véc-tơ (vector / 벡터) calculus thường dễ hơn nếu dùng coordinates phù hợp: Cartesian, cylindrical, spherical.

Nhưng operators `\nabla`, divergence, curl không giữ cùng coordinate formula naïvely; quy mô (scale / 규모) factors/Jacobian matter.

Ví dụ spherical volume element:

```math
dV=r^2\sin\theta\,dr\,d\theta\,d\phi.
```

Factor `r^2\sin\theta` đến từ cục bộ (local / 로컬) volume scaling của coordinate transform.

## 20. Maxwell equations liên kết (connection / 연결)

Electromagnetism dùng divergence/curl trực tiếp. Ví dụ conceptual forms:

```text
Gauss law → divergence của electric field liên hệ charge density
Faraday law → curl của electric field liên hệ changing magnetic field
```

Điểm quan trọng không phải memorize physics constants ở chapter này, mà thấy véc-tơ (vector / 벡터) calculus operators được chọn vì chúng encode cục bộ (local / 로컬) nguồn (source / 소스) và circulation cấu trúc (structure / 구조).

## 21. Fluid dynamics liên kết (connection / 연결)

Velocity trường dữ liệu (field / 필드) `v(x,t)`:

```math
\nabla\cdot v=0
```

thường biểu diễn incompressibility trong appropriate mô hình (model / 모델).

Vorticity:

```math
\omega=\nabla\times v.
```

mô tả rotational cấu trúc (structure / 구조) của luồng (flow / 흐름).

Nhưng zero divergence không nghĩa zero velocity; zero curl không nghĩa no motion.

## 22. AI và scalar fields

Hàm mất mát (loss function / 손실 함수) trong machine học tập (learning / 학습) là high-dimensional scalar trường dữ liệu (field / 필드) trên parameter không gian (space / 공간).

Độ dốc (gradient / 기울기):

```math
\nabla L
```

cho cục bộ (local / 로컬) sensitivity; Hessian cho curvature. Dù không visualizable ở millions dimensions, hình học (geometry / 기하학) vẫn là same differential cấu trúc (structure / 구조).

Véc-tơ (vector / 벡터) calculus intuition vì vậy vẫn relevant cho tối ưu hóa (optimization / 최적화)/AI.

## Worked example: flux của radial trường dữ liệu (field / 필드)

Xét:

```math
F(x)=\frac{x}{\|x\|^3}
```

trên `\mathbb R^3\setminus\{0\}`.

Trường dữ liệu (field / 필드) radial và magnitude quy mô (scale / 규모) `1/r^2`. Flux qua sphere radius `R`:

```math
F\cdot n=\frac1{R^2},
```

surface area `4\pi R^2`, nên total flux:

```math
4\pi.
```

Nó independent of `R`. nguồn (source / 소스) hành vi (behavior / 동작) concentrated at excluded origin cho thấy vì sao lĩnh vực (domain / 도메인)/singularity matter khi dùng divergence theorem.

## Liên kết kiến thức (knowledge connection / 지식 연결)

```text
multivariable derivative
→ gradient / Jacobian
→ field geometry
→ line / surface integrals
→ divergence / curl
→ conservation laws
→ PDE / Physics / control
```

Projection và dot sản phẩm (product / 제품) từ tuyến tính (linear / 선형) Algebra xuất hiện trong directional derivative, công việc (work / 작업) và flux. Topology xuất hiện trong distinction cục bộ (local / 로컬) curl-free vs toàn cục (global / 전역) conservative. Differential equations/PDE dùng các operators này để mô hình (model / 모델) dynamics.

## Mô hình tư duy (mental model / 사고 모델)

> độ dốc (gradient / 기울기) đo cục bộ (local / 로컬) uphill direction của scalar trường dữ liệu (field / 필드). Divergence đo cục bộ (local / 로컬) creation/expansion of luồng (flow / 흐름). Curl đo cục bộ (local / 로컬) circulation tendency. Integral theorems biến cục bộ (local / 로컬) derivatives thành toàn cục (global / 전역) ranh giới (boundary / 경계) statements.

## Dùng chung (common / 공통) Misconceptions

Độ dốc (gradient / 기울기) là véc-tơ (vector / 벡터) trong đầu vào (input / 입력) không gian (space / 공간), không phải đồ thị (graph / 그래프) slope line. Divergence không phải magnitude. Curl zero không luôn imply toàn cục (global / 전역) potential nếu lĩnh vực (domain / 도메인) có holes. Flux phụ thuộc surface orientation. Stokes/divergence theorem cần regularity và lĩnh vực (domain / 도메인) các giả định (assumptions / 가정들); không nên apply qua singularities mà không kiểm tra.

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 limits and continuity](./00_limits_and_continuity.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
