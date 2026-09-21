# Cơ học giải tích: tọa độ suy rộng, Lagrangian và Hamiltonian

## Vì sao Newton chưa phải ngôn ngữ duy nhất của cơ học?

Cơ học Newton rất trực quan khi hệ có vài vật và ta dễ liệt kê từng lực. Nhưng với con lắc kép, robot nhiều khớp, vật chuyển động trên mặt cong hoặc hệ có nhiều ràng buộc, việc viết từng thành phần lực trở nên cồng kềnh.

Cơ học giải tích (analytical mechanics / 해석역학) đổi điểm nhìn:

> thay vì bắt đầu từ từng lực riêng lẻ, hãy xác định bậc tự do, ràng buộc, năng lượng và đối xứng của hệ.

Ngôn ngữ này không thay thế vật lý Newton bằng một lý thuyết khác; nó tổ chức cùng động lực học theo cách phù hợp hơn với hệ nhiều bậc tự do.

## Bậc tự do và tọa độ suy rộng

Tọa độ suy rộng (generalized coordinate / 일반화 좌표) `q_i` là một tập biến độc lập đủ để mô tả cấu hình hệ.

Một hạt tự do trong không gian 3D cần ba tọa độ. Một con lắc lý tưởng dài `\ell` bị ràng buộc trên đường tròn nên chỉ cần một góc `\theta`.

Nếu cố giữ cả `x,y` cho con lắc, ta phải thêm ràng buộc

```math
x^2+y^2=\ell^2.
```

Dùng `\theta` hấp thụ ràng buộc ngay từ đầu:

```math
x=\ell\sin\theta,
\qquad
y=-\ell\cos\theta.
```

Đây là ưu điểm lớn của tọa độ suy rộng: chọn biến phù hợp có thể loại bỏ nhiều lực ràng buộc khỏi bài toán.

## Lagrangian và tác dụng

Với hệ bảo toàn cơ học thông thường,

```math
L(q,\dot q,t)=T-V,
```

trong đó `T` là động năng và `V` là thế năng.

Tác dụng (action / 작용) là

```math
S[q]=\int_{t_1}^{t_2}L(q,\dot q,t)\,dt.
```

Nguyên lý tác dụng dừng nói quỹ đạo vật lý làm biến phân bậc nhất của `S` bằng 0:

```math
\delta S=0.
```

“Dừng” chính xác hơn “nhỏ nhất”, vì quỹ đạo vật lý không bắt buộc là minimum toàn cục của tác dụng.

## Suy ra phương trình Euler–Lagrange

Xét biến phân

```math
q(t)\to q(t)+\epsilon\eta(t),
```

với

```math
\eta(t_1)=\eta(t_2)=0.
```

Biến phân tác dụng là

```math
\delta S
=\int_{t_1}^{t_2}
\left(
\frac{\partial L}{\partial q}\delta q
+
\frac{\partial L}{\partial\dot q}\delta\dot q
\right)dt.
```

Tích phân từng phần hạng thứ hai:

```math
\int
\frac{\partial L}{\partial\dot q}
\frac{d}{dt}(\delta q)dt
=
\left[
\frac{\partial L}{\partial\dot q}\delta q
\right]_{t_1}^{t_2}
-
\int
\frac{d}{dt}
\left(
\frac{\partial L}{\partial\dot q}
\right)\delta q\,dt.
```

Hạng biên bằng 0 vì endpoint cố định. Vì `\delta q` tùy ý bên trong khoảng thời gian, ta thu được

```math
\frac{d}{dt}
\left(
\frac{\partial L}{\partial\dot q_i}
\right)
-
\frac{\partial L}{\partial q_i}=0.
```

Đây là phương trình Euler–Lagrange.

## Newton xuất hiện trở lại

Với một hạt một chiều,

```math
L=\frac12m\dot x^2-V(x).
```

Ta có

```math
\frac{\partial L}{\partial\dot x}=m\dot x,
```

```math
\frac{\partial L}{\partial x}
=-\frac{dV}{dx}.
```

Euler–Lagrange cho

```math
m\ddot x=-\frac{dV}{dx}=F.
```

Vì vậy Lagrange không mâu thuẫn Newton; nó tái biểu diễn động lực học theo năng lượng và tọa độ thích hợp.

## Ví dụ: con lắc đơn

Với con lắc dài `\ell`, khối lượng `m`, dùng `\theta` làm tọa độ suy rộng:

```math
T=\frac12m\ell^2\dot\theta^2,
```

```math
V=mg\ell(1-\cos\theta).
```

Do đó

```math
L
=\frac12m\ell^2\dot\theta^2
-mg\ell(1-\cos\theta).
```

Euler–Lagrange cho

```math
m\ell^2\ddot\theta
+mg\ell\sin\theta=0,
```

hay

```math
\ddot\theta
+\frac{g}{\ell}\sin\theta=0.
```

Chỉ khi

```math
|\theta|\ll1
```

và đo bằng radian ta mới dùng

```math
\sin\theta\approx\theta
```

để thu dao động điều hòa.

Điều này cho thấy SHM là tuyến tính hóa của hệ phi tuyến thật.

## Động lượng suy rộng

Động lượng chính tắc liên hợp với `q_i` là

```math
p_i
=\frac{\partial L}{\partial\dot q_i}.
```

Nó không phải lúc nào cũng bằng `m\dot q_i`.

Trong trường điện từ, chẳng hạn, động lượng chính tắc chứa thế vectơ. Vì vậy phải phân biệt động lượng cơ học và động lượng chính tắc theo ngữ cảnh.

## Tọa độ cyclic và định luật bảo toàn

Nếu một tọa độ `q_j` không xuất hiện trực tiếp trong Lagrangian,

```math
\frac{\partial L}{\partial q_j}=0,
```

thì Euler–Lagrange cho

```math
\frac{d}{dt}
\left(
\frac{\partial L}{\partial\dot q_j}
\right)=0.
```

Do đó

```math
p_j=\text{constant}.
```

Tọa độ như vậy gọi là cyclic coordinate.

Đây là phiên bản cụ thể của tư duy Noether: đối xứng liên tục tạo đại lượng bảo toàn.

## Ràng buộc và nhân tử Lagrange

Không phải ràng buộc nào cũng dễ hấp thụ bằng cách chọn tọa độ mới.

Với ràng buộc holonomic

```math
f_a(q,t)=0,
```

ta có thể dùng nhân tử Lagrange `\lambda_a` và viết

```math
\frac{d}{dt}
\left(
\frac{\partial L}{\partial\dot q_i}
\right)
-
\frac{\partial L}{\partial q_i}
=
\sum_a
\lambda_a
\frac{\partial f_a}{\partial q_i}.
```

Các `\lambda_a` thường liên hệ với lực ràng buộc.

Phương pháp này đặc biệt hữu ích khi muốn vừa giữ tọa độ thuận tiện vừa tính phản lực constraint.

## Biến đổi Legendre và Hamiltonian

Từ Lagrangian, định nghĩa Hamiltonian bằng biến đổi Legendre:

```math
H(q,p,t)
=\sum_i p_i\dot q_i-L.
```

Nếu phép biến đổi giữa `\dot q` và `p` khả nghịch, ta viết động lực học trong biến `(q,p)`.

Phương trình Hamilton là

```math
\dot q_i
=\frac{\partial H}{\partial p_i},
```

```math
\dot p_i
=-\frac{\partial H}{\partial q_i}.
```

Một hệ phương trình bậc hai theo `q` trở thành hệ bậc nhất trên không gian pha.

## Hamiltonian có luôn bằng tổng năng lượng không?

Với nhiều hệ cơ học chuẩn, không phụ thuộc thời gian và có thế không phụ thuộc vận tốc,

```math
H=T+V.
```

Nhưng đây không phải định nghĩa tổng quát.

Khi có trường điện từ, tọa độ phụ thuộc thời gian hoặc Lagrangian đặc biệt, Hamiltonian cần được tính từ biến đổi Legendre thay vì giả định bằng “động năng + thế năng”.

Vai trò cơ bản của `H` là generator của tiến hóa theo thời gian trong cấu trúc Hamilton.

## Không gian pha

Trong formulation Hamilton, trạng thái của hệ được mô tả bởi

```math
(q_1,\ldots,q_N,p_1,\ldots,p_N).
```

Một trạng thái là một điểm trong không gian pha; động lực học tạo một quỹ đạo trong không gian đó.

Cách nhìn này mở đường tới:

- cơ học thống kê;
- động lực phi tuyến;
- chaos;
- canonical transformations;
- cơ học lượng tử.

## Ví dụ: Hamiltonian của dao động tử điều hòa

Với

```math
L
=\frac12m\dot x^2
-\frac12kx^2,
```

động lượng chính tắc là

```math
p=m\dot x.
```

Hamiltonian:

```math
H
=\frac{p^2}{2m}
+\frac12kx^2.
```

Đường

```math
H=E
```

trong không gian pha là ellipse.

Do đó dao động điều hòa có thể được hiểu như chuyển động tuần hoàn trên một đường năng lượng cố định trong phase space.

## Lagrangian với lực không bảo toàn

Công thức `L=T-V` đơn giản nhất phù hợp với lực bảo toàn.

Với ma sát nhớt, một cách mở rộng hiện tượng luận là dùng hàm tiêu tán Rayleigh

```math
\mathcal R
=\frac12b\dot q^2,
```

và viết

```math
\frac{d}{dt}
\frac{\partial L}{\partial\dot q}
-
\frac{\partial L}{\partial q}
+
\frac{\partial\mathcal R}{\partial\dot q}=0.
```

Tuy nhiên hệ tiêu tán không còn giữ đầy đủ cấu trúc Hamilton kín nếu ta chỉ theo dõi vài bậc tự do. Muốn mô tả vi mô đầy đủ thường phải mở rộng hệ để bao gồm môi trường.

## Liên hệ với Engineering và Computer Science

Robot nhiều khớp thường dùng tọa độ khớp `q` và phương trình dạng

```math
M(q)\ddot q
+C(q,\dot q)\dot q
+g(q)=\tau.
```

Các ma trận này được suy ra tự nhiên từ kinetic energy và potential energy.

Trong mô phỏng, việc giữ cấu trúc vật lý có lợi:

- symplectic integrator giữ geometry của Hamiltonian tốt hơn trong mô phỏng dài;
- differentiable physics cho phép lấy gradient qua simulator;
- Hamiltonian Neural Network cố học một hàm sinh động lực thay vì trực tiếp fit trajectory derivative tùy ý.

Cấu trúc vật lý đóng vai trò inductive bias cho mô hình tính toán.

## Miền áp dụng và giới hạn

Cơ học Lagrange/Hamilton cổ điển vẫn nằm trong miền classical mechanics. Nó không tự xử lý hiệu ứng tương đối tính hoặc lượng tử nếu chưa thay Lagrangian/Hamiltonian bằng lý thuyết phù hợp.

Một số ràng buộc không holonomic cần xử lý tinh tế hơn. Biến đổi Legendre cũng có thể suy biến nếu Hessian theo `\dot q` không khả nghịch, như trong gauge theory và constrained systems.

## Mô hình tư duy (Mental Model)

Ba ngôn ngữ chính có thể nhìn như:

```text
Newton: interactions → forces → acceleration
Lagrange: configuration + constraints → action → equations of motion
Hamilton: state in phase space → generator H → phase-space flow
```

Chúng không cạnh tranh; mỗi ngôn ngữ làm một cấu trúc khác của bài toán trở nên rõ hơn.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Nguyên lý tác dụng dừng nói tự nhiên luôn chọn đường ngắn nhất”

Không. Đại lượng được làm stationary là action, không phải khoảng cách; nghiệm có thể là minimum, maximum hoặc saddle theo ngữ cảnh.

### “Lagrangian luôn bằng `T-V`”

Đó là dạng rất phổ biến nhưng không phải định nghĩa duy nhất. Với trường điện từ hoặc hệ tổng quát hơn có thể có hạng phụ thuộc vận tốc.

### “Hamiltonian luôn là tổng năng lượng”

Không trong mọi formulation. Cần tính từ biến đổi Legendre và xét phụ thuộc thời gian/ràng buộc.

### “Cơ học giải tích chỉ là toán khó hơn để giải cùng bài đơn giản”

Với hệ nhiều bậc tự do, symmetry và constraint, nó thường giảm độ phức tạp và mở ra các định luật bảo toàn khó thấy trong FBD.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Công và năng lượng](03_work_energy_power.md), [Chuyển động quay](05_rotation_rigid_body.md), [Đối xứng và bảo toàn](../00_foundations/04_symmetry_conservation_scale.md).

**Liên hệ tiếp:** [Hamilton–Jacobi và biến đổi chính tắc](10_canonical_transformations_hamilton_jacobi.md), [Động lực phi tuyến và chaos](09_nonlinear_dynamics_chaos.md), [Cơ học lượng tử](../08_quantum/00_quantum_foundations.md).
