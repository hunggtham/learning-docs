# Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển

Phương trình Schrödinger xác định động lực học lượng tử, nhưng biết phương trình không đồng nghĩa với việc luôn tìm được nghiệm giải tích chính xác. Phần lớn nguyên tử nhiều electron, phân tử, vật rắn và hệ tương tác nhiều hạt không có nghiệm đóng đơn giản.

Vì vậy **xấp xỉ có kiểm soát (controlled approximation)** không phải phần phụ của cơ học lượng tử; nó là cách làm việc thực tế của lý thuyết.

Câu hỏi cốt lõi luôn là:

```text
mô hình nào đã giải được?
phần còn lại nhỏ theo tham số nào?
sai số tăng theo bậc nào?
khi nào xấp xỉ thất bại?
```

## Phân loại bài toán trước khi chọn phương pháp

Một workflow hữu ích là:

```text
Hamiltonian có gần một bài đã giải chính xác không?
→ perturbation theory

ground state cần tìm nhưng không có small perturbation rõ?
→ variational method

potential thay đổi chậm so với local wavelength?
→ WKB / semiclassical

Hamiltonian thay đổi chậm theo thời gian?
→ adiabatic approximation

hệ nhiều hạt với interaction phức tạp?
→ mean-field / effective theory / numerical methods
```

Không có một approximation method tốt nhất cho mọi bài toán.

## Lý thuyết nhiễu loạn không phụ thuộc thời gian

Giả sử

```math
H=H_0+\lambda V,
```

trong đó `H_0` đã giải được và `\lambda` là tham số dùng để theo dõi độ lớn của perturbation.

Ta khai triển

```math
E_n
=E_n^{(0)}
+\lambda E_n^{(1)}
+\lambda^2E_n^{(2)}+\cdots
```

và

```math
|n\rangle
=|n^{(0)}\rangle
+\lambda|n^{(1)}\rangle+\cdots.
```

Sau khi suy dẫn, correction năng lượng bậc một cho trạng thái không suy biến là

```math
E_n^{(1)}
=\langle n^{(0)}|V|n^{(0)}\rangle.
```

Ý nghĩa vật lý: ở bậc thấp nhất, energy shift là giá trị kỳ vọng của perturbing interaction trên trạng thái chưa bị perturb.

## Correction trạng thái bậc một

Correction trạng thái là

```math
|n^{(1)}\rangle
=
\sum_{m\ne n}
\frac{
\langle m^{(0)}|V|n^{(0)}\rangle
}{
E_n^{(0)}-E_m^{(0)}
}
|m^{(0)}\rangle.
```

Công thức cho thấy perturbation làm eigenstate cũ trộn với các trạng thái khác.

Mức mixing lớn khi:

```text
matrix element lớn
hoặc
energy denominator nhỏ
```

Do đó “`V` nhỏ” phải luôn được hiểu tương đối với relevant energy gaps.

## Correction năng lượng bậc hai

Với trạng thái không suy biến,

```math
E_n^{(2)}
=
\sum_{m\ne n}
\frac{
|\langle m^{(0)}|V|n^{(0)}\rangle|^2
}{
E_n^{(0)}-E_m^{(0)}
}.
```

Đây là một formula rất giàu thông tin.

Nếu một state gần degenerate với `n`, denominator nhỏ và correction có thể lớn dù perturbation coefficient nhỏ.

Một tiêu chí heuristic là

```math
\left|
\frac{\langle m|V|n\rangle}
{E_n-E_m}
\right|\ll1
```

cho các state coupling đáng kể.

## Ví dụ: Stark effect bậc một

Đặt atom trong electric field `\mathbf E`. Perturbation có dạng

```math
V=q\mathbf E\cdot\mathbf r.
```

Nếu symmetry khiến

```math
\langle n|\mathbf r|n\rangle=0,
```

thì first-order shift có thể bằng zero.

Điều này cho thấy symmetry có thể làm correction biến mất trước cả khi cần tính integral chi tiết.

Trong degenerate subspace của hydrogen, electric field lại có thể mix mạnh states cùng energy và tạo linear Stark effect.

## Nhiễu loạn suy biến

Nếu nhiều state có cùng unperturbed energy, công thức non-degenerate chứa denominator zero và không dùng được.

Ta phải project perturbation vào degenerate subspace và diagonalize matrix

```math
V_{ij}=\langle i|V|j\rangle.
```

Eigenvectors mới của matrix này là những linear combinations đúng để dùng làm zeroth-order basis.

Đây là bài học tổng quát:

```text
near degeneracy
→ choose a better basis first
```

Thay đổi basis có thể quan trọng hơn việc thêm nhiều bậc perturbation.

## Level repulsion và avoided crossing

Khi hai level có cùng symmetry được coupled, degeneracy thường bị tách và tạo avoided crossing khi parameter thay đổi.

Một model `2×2` đơn giản là

```math
H=
\begin{pmatrix}
E_1(\lambda) & g\\
g^* & E_2(\lambda)
\end{pmatrix}.
```

Eigenvalues là

```math
E_\pm
=\frac{E_1+E_2}{2}
\pm
\sqrt{
\left(\frac{E_1-E_2}{2}\right)^2+|g|^2
}.
```

Nếu `g\ne0`, hai branch không cắt nhau tại điểm bare levels trùng nhau.

Cấu trúc này xuất hiện trong atomic spectra, coupled oscillators, qubits và band theory.

## Nhiễu loạn phụ thuộc thời gian

Nếu Hamiltonian là

```math
H(t)=H_0+V(t),
```

perturbation có thể gây transition giữa eigenstates của `H_0`.

Amplitude bậc một từ `|i\rangle` sang `|f\rangle` có dạng

```math
c_f^{(1)}(t)
\propto
-\frac{i}{\hbar}
\int_0^t
\langle f|V(t')|i\rangle
 e^{i\omega_{fi}t'}dt',
```

trong đó

```math
\omega_{fi}=\frac{E_f-E_i}{\hbar}.
```

Integral cho thấy transition mạnh khi perturbation có frequency component gần energy splitting của hệ.

Đây là nguồn gốc của resonance trong spectroscopy.

## Fermi's Golden Rule

Trong weak coupling tới continuum of final states và long-time limit phù hợp,

```math
\Gamma_{i\to f}
\approx
\frac{2\pi}{\hbar}
|\langle f|V|i\rangle|^2
\rho(E_f).
```

Hai thành phần có ý nghĩa khác nhau:

```text
|matrix element|²
→ interaction mạnh tới đâu

ρ(E_f)
→ có bao nhiêu final states khả dụng
```

Mẫu hình

```text
coupling strength × phase space
```

xuất hiện rộng trong atomic transitions, scattering, carrier relaxation, nuclear decay và particle physics.

Golden rule có assumptions: weak coupling, continuum gần đủ dày, Markov/long-time reasoning và transition probability chưa phá mạnh state ban đầu.

## Variational principle

Với ground-state energy chính xác `E_0`, mọi normalized trial state `|\psi\rangle` đều thỏa

```math
\frac{\langle\psi|H|\psi\rangle}
{\langle\psi|\psi\rangle}
\ge E_0.
```

Ta chọn một family

```math
|\psi(\alpha_1,\alpha_2,\ldots)\rangle
```

rồi minimize energy expectation theo parameters.

Nếu trial family đủ linh hoạt, kết quả có thể gần ground state rất tốt.

## Vì sao variational bound luôn ở phía trên?

Khai triển trial state theo exact eigenbasis:

```math
|\psi\rangle=\sum_n c_n|n\rangle.
```

Khi normalized,

```math
\sum_n|c_n|^2=1.
```

Energy expectation là

```math
\langle H\rangle
=\sum_n|c_n|^2E_n.
```

Vì

```math
E_n\ge E_0,
```

nên weighted average không thể thấp hơn `E_0`.

Đây là derivation đơn giản nhưng làm rõ bản chất của variational method.

## Ví dụ tư duy variational

Với một bound system, ta có thể chọn trial wavefunction có length scale `a`.

Kinetic energy thường tăng khi state bị localize mạnh:

```math
K\sim\frac{\hbar^2}{ma^2}.
```

Potential energy có thể giảm khi localization tăng.

Minimize tổng

```math
E(a)=K(a)+V(a)
```

tạo compromise length scale tự nhiên.

Đây là first-principles reasoning rất hữu ích ngay cả trước khi làm integral chính xác.

## Adiabatic approximation

Giả sử Hamiltonian phụ thuộc parameter thay đổi chậm:

```math
H(\lambda(t)).
```

Nếu hệ bắt đầu ở instantaneous eigenstate và variation đủ chậm so với relevant inverse gaps, hệ có xu hướng tiếp tục theo eigenstate tương ứng, ngoài phase factors.

Điều kiện heuristic liên quan

```math
\frac{
|\langle m|\dot H|n\rangle|
}{
|E_m-E_n|^2/\hbar
}
\ll1.
```

Gần degeneracy hoặc level crossing, approximation dễ thất bại.

Adiabatic reasoning là nền cho:

```text
Born–Oppenheimer approximation
adiabatic quantum control
Berry phase
slow parameter cycles
```

## Born–Oppenheimer như separation of scales

Nuclei nặng hơn electron rất nhiều.

Một first approximation là giữ nuclei gần cố định khi giải electronic problem, rồi dùng electronic energy làm effective potential cho nuclear motion.

Chuỗi reasoning là

```text
mass scale separation
→ time-scale separation
→ fast electron / slow nuclei
→ approximate factorization
```

Approximation thất bại mạnh hơn gần electronic degeneracy hoặc nonadiabatic transition.

## WKB và giới hạn bán cổ điển

Trong 1D,

```math
-\frac{\hbar^2}{2m}\psi''+V(x)\psi=E\psi.
```

Đặt local classical momentum

```math
p(x)=\sqrt{2m(E-V(x))}.
```

Khi potential thay đổi chậm trên local wavelength scale, nghiệm WKB trong classically allowed region có dạng

```math
\psi(x)
\approx
\frac{C}{\sqrt{p(x)}}
\exp\left(
\pm\frac{i}{\hbar}
\int^xp(x')dx'
\right).
```

Pha là classical action chia `\hbar`.

Điều này nối wavefunction với Hamilton–Jacobi/action formulation của mechanics.

## WKB tunneling

Trong forbidden region, đặt

```math
\kappa(x)
=\frac{\sqrt{2m(V-E)}}{\hbar}.
```

Transmission exponent gần

```math
T\sim
\exp\left[
-2\int_{x_1}^{x_2}\kappa(x)dx
\right].
```

Đây là generalization của rectangular-barrier tunneling.

Alpha decay và fusion penetration có thể được hiểu bằng cùng structure.

## Turning point là nơi WKB thất bại cục bộ

Tại

```math
E=V(x),
```

ta có

```math
p(x)=0.
```

WKB amplitude `1/\sqrt{p}` trở nên singular, nên approximation không còn hợp lệ ngay tại turning point.

Cần connection formulas hoặc local Airy-function treatment để nối hai miền.

Đây là ví dụ quan trọng: một approximation có thể rất tốt gần như mọi nơi nhưng vẫn hỏng ở một vùng nhỏ có cấu trúc đặc biệt.

## Mean-field approximation

Trong many-body system, interaction của mỗi particle với mọi particle khác tạo bài toán cực lớn.

Mean-field idea thay fluctuating many-body environment bằng effective average field được xác định self-consistently.

Hartree và Hartree–Fock là ví dụ điển hình.

Workflow thường là

```text
initial guess
→ solve one-particle effective equations
→ recompute density/field
→ iterate to self-consistency
```

Mean field thường bỏ qua correlation hoặc fluctuation beyond average response.

Nó có thể rất tốt ở một số regime nhưng thất bại gần critical point, low dimension hoặc strongly correlated state.

## Effective theory và tích phân bỏ bậc tự do

Một cách xấp xỉ sâu hơn là không cố mô tả mọi microscopic degree of freedom.

Ta giữ các biến low-energy/relevant và hấp thụ physics của scale cao vào effective parameters và operators.

Ví dụ:

```text
atomic details
→ elastic constants

microscopic collisions
→ viscosity

band structure
→ effective mass
```

Tư duy này xuất hiện từ condensed matter tới particle physics.

## Error control và asymptotic series

Perturbation series không nhất thiết hội tụ theo nghĩa toán học thông thường.

Nhiều series vật lý là asymptotic: vài term đầu cải thiện approximation, nhưng lấy quá nhiều term có thể làm kết quả tệ hơn.

Do đó kiểm soát approximation cần dựa vào:

```text
small parameter
comparison of successive orders
known limiting cases
numerical benchmark nếu có
symmetry/conservation checks
```

Không nên đồng nhất “có expansion” với “series chắc chắn hội tụ”.

## Khi nào nên dùng numerical method?

Nếu không có small parameter rõ ràng và variational/semiclassical approximations không đủ, numerical methods có thể phù hợp hơn:

```text
matrix diagonalization
finite difference / finite element
basis expansion
Monte Carlo
DMRG / tensor-network methods
```

Nhưng numerical result vẫn phải kiểm tra convergence và finite-size/basis truncation errors.

Máy tính không loại bỏ approximation; nó chuyển approximation sang discretization và finite representation.

## Mô hình tư duy (Mental Model)

Các phương pháp xấp xỉ có thể nhìn theo ba câu hỏi:

```text
1. có một bài toán gần đó đã giải được không?
2. có parameter hoặc scale separation nào nhỏ không?
3. error được kiểm soát bằng cách nào?
```

Approximation tốt không phải “làm sai cho dễ”. Nó là việc bỏ đúng những phần nhỏ so với câu hỏi đang xét và biết rõ chi phí của việc bỏ chúng.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Perturbation nhỏ nghĩa coefficient trước `V` nhỏ là đủ”

Không. Relevant matrix elements phải nhỏ so với energy gaps; near degeneracy có thể phá approximation.

### “Variational method cho đúng ground state nếu minimize đủ tốt”

Không nhất thiết. Nó chỉ tối ưu trong trial family đã chọn. Family nghèo vẫn cho bound kém.

### “Adiabatic nghĩa thay đổi chậm theo clock time”

Không có một threshold tuyệt đối. “Chậm” phải so với internal energy gaps/time scales của hệ.

### “WKB dùng được tại mọi điểm nếu `\hbar` nhỏ”

Không. Turning point là vùng thất bại điển hình.

### “Numerical solution là exact”

Không. Basis cutoff, grid spacing, timestep và finite precision đều tạo approximation mới.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Nền tảng lượng tử](00_quantum_foundations.md), [Các hệ lượng tử mẫu](01_quantum_systems.md), [Đại số tuyến tính và Taylor](../00_foundations/03_mathematical_language.md).

**Liên hệ tiếp:** [Động lực học phụ thuộc thời gian và tán xạ](06_time_dependent_scattering.md), [Vật lý nguyên tử](../09_atomic_nuclear_particle/00_atomic_physics.md), [Vật lý phân tử](../09_atomic_nuclear_particle/04_molecular_physics.md), [Vật lý tính toán](../12_experimental_computational/02_computational_physics.md), [Berry phase và topology](../10_condensed_matter_devices/06_berry_phase_quantum_hall_topology.md).
