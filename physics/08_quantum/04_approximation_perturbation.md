# Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Các phương pháp xấp xỉ trong cơ học lượng tử**. Route đi từ solvability/scale separation → perturbation theory → variational bounds → semiclassical/WKB → error and validity estimates, để chọn phương pháp theo cấu trúc bài toán.

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

Không có một approximation phương thức (method / 메서드) tốt nhất cho mọi bài toán.

> **Chuyển mạch:** Trong **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Lý thuyết nhiễu loạn không phụ thuộc thời gian** tiếp nhận điểm tựa từ **Phân loại bài toán trước khi chọn phương pháp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Correction trạng thái bậc một** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Ý nghĩa vật lý: ở bậc thấp nhất, năng lượng (energy / 에너지) shift là giá trị kỳ vọng của perturbing tương tác (interaction / 상호작용) trên trạng thái chưa bị perturb.

> **Chuyển mạch:** Ở chặng này của **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Correction trạng thái bậc một** tiếp nhận điểm tựa từ **Lý thuyết nhiễu loạn không phụ thuộc thời gian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Correction năng lượng bậc hai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Do đó “`V` nhỏ” phải luôn được hiểu tương đối với relevant năng lượng (energy / 에너지) gaps.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Correction năng lượng bậc hai** tiếp nhận điểm tựa từ **Correction trạng thái bậc một** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ví dụ: Stark tác động (effect / 효과) bậc một** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Nếu một trạng thái (state / 상태) gần degenerate với `n`, denominator nhỏ và correction có thể lớn dù perturbation coefficient nhỏ.

Một tiêu chí heuristic là

```math
\left|
\frac{\langle m|V|n\rangle}
{E_n-E_m}
\right|\ll1
```

cho các trạng thái (state / 상태) coupling đáng kể.

> **Chuyển mạch:** Trong **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Correction năng lượng bậc hai** cho ta quy tắc; **Ví dụ: Stark tác động (effect / 효과) bậc một** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Nhiễu loạn suy biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ví dụ: Stark tác động (effect / 효과) bậc một

Đặt atom trong electric trường dữ liệu (field / 필드) `\mathbf E`. Perturbation có dạng

```math
V=q\mathbf E\cdot\mathbf r.
```

Nếu symmetry khiến

```math
\langle n|\mathbf r|n\rangle=0,
```

thì first-order shift có thể bằng zero.

Điều này cho thấy symmetry có thể làm correction biến mất trước cả khi cần tính integral chi tiết.

Trong degenerate subspace của hydrogen, electric trường dữ liệu (field / 필드) lại có thể mix mạnh states cùng năng lượng (energy / 에너지) và tạo tuyến tính (linear / 선형) Stark tác động (effect / 효과).

> **Chuyển mạch:** Ở chặng này của **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Ví dụ: Stark tác động (effect / 효과) bậc một** cho ta quy tắc; **Nhiễu loạn suy biến** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mức (level / 수준) repulsion và avoided crossing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhiễu loạn suy biến

Nếu nhiều trạng thái (state / 상태) có cùng unperturbed năng lượng (energy / 에너지), công thức non-degenerate chứa denominator zero và không dùng được.

Ta phải dự án (project / 프로젝트) perturbation vào degenerate subspace và diagonalize ma trận (matrix / 행렬)

```math
V_{ij}=\langle i|V|j\rangle.
```

Eigenvectors mới của ma trận (matrix / 행렬) này là những tuyến tính (linear / 선형) combinations đúng để dùng làm zeroth-order basis.

Đây là bài học tổng quát:

```text
near degeneracy
→ choose a better basis first
```

Thay đổi basis có thể quan trọng hơn việc thêm nhiều bậc perturbation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Mức (level / 수준) repulsion và avoided crossing** tiếp nhận điểm tựa từ **Nhiễu loạn suy biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nhiễu loạn phụ thuộc thời gian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mức (level / 수준) repulsion và avoided crossing

Khi hai mức (level / 수준) có cùng symmetry được coupled, degeneracy thường bị tách và tạo avoided crossing khi parameter thay đổi.

Một mô hình (model / 모델) `2×2` đơn giản là

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

Cấu trúc này xuất hiện trong atomic spectra, coupled oscillators, qubits và band lý thuyết (theory / 이론).

> **Chuyển mạch:** Trong **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Nhiễu loạn phụ thuộc thời gian** tiếp nhận điểm tựa từ **Mức (level / 수준) repulsion và avoided crossing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fermi's Golden quy tắc (rule / 규칙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhiễu loạn phụ thuộc thời gian

Nếu Hamiltonian là

```math
H(t)=H_0+V(t),
```

perturbation có thể gây chuyển tiếp (transition / 전이) giữa eigenstates của `H_0`.

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

Integral cho thấy chuyển tiếp (transition / 전이) mạnh khi perturbation có frequency thành phần (component / 컴포넌트) gần năng lượng (energy / 에너지) splitting của hệ.

Đây là nguồn gốc của resonance trong spectroscopy.

> **Chuyển mạch:** Ở chặng này của **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Fermi's Golden quy tắc (rule / 규칙)** tiếp nhận điểm tựa từ **Nhiễu loạn phụ thuộc thời gian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Variational principle** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fermi's Golden quy tắc (rule / 규칙)

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

Golden quy tắc (rule / 규칙) có các giả định (assumptions / 가정들): weak coupling, continuum gần đủ dày, Markov/long-time lập luận (reasoning / 추론) và chuyển tiếp (transition / 전이) xác suất (probability / 확률) chưa phá mạnh trạng thái (state / 상태) ban đầu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Variational principle** tiếp nhận điểm tựa từ **Fermi's Golden quy tắc (rule / 규칙)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao variational bound luôn ở phía trên?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Variational principle

Với ground-state năng lượng (energy / 에너지) chính xác `E_0`, mọi normalized trial trạng thái (state / 상태) `|\psi\rangle` đều thỏa

```math
\frac{\langle\psi|H|\psi\rangle}
{\langle\psi|\psi\rangle}
\ge E_0.
```

Ta chọn một family

```math
|\psi(\alpha_1,\alpha_2,\ldots)\rangle
```

rồi minimize năng lượng (energy / 에너지) expectation theo parameters.

Nếu trial family đủ linh hoạt, kết quả có thể gần ground trạng thái (state / 상태) rất tốt.

> **Chuyển mạch:** Trong **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Vì sao variational bound luôn ở phía trên?** tiếp nhận điểm tựa từ **Variational principle** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ví dụ tư duy variational** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao variational bound luôn ở phía trên?

Khai triển trial trạng thái (state / 상태) theo chính xác (exact / 정확한) eigenbasis:

```math
|\psi\rangle=\sum_n c_n|n\rangle.
```

Khi normalized,

```math
\sum_n|c_n|^2=1.
```

Năng lượng (energy / 에너지) expectation là

```math
\langle H\rangle
=\sum_n|c_n|^2E_n.
```

Vì

```math
E_n\ge E_0,
```

nên weighted average không thể thấp hơn `E_0`.

Đây là derivation đơn giản nhưng làm rõ bản chất của variational phương thức (method / 메서드).

> **Chuyển mạch:** Ở chặng này của **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Vì sao variational bound luôn ở phía trên?** cho ta quy tắc; **Ví dụ tư duy variational** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Adiabatic approximation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ví dụ tư duy variational

Với một bound hệ thống (system / 시스템), ta có thể chọn trial wavefunction có length quy mô (scale / 규모) `a`.

Kinetic năng lượng (energy / 에너지) thường tăng khi trạng thái (state / 상태) bị localize mạnh:

```math
K\sim\frac{\hbar^2}{ma^2}.
```

Potential năng lượng (energy / 에너지) có thể giảm khi localization tăng.

Minimize tổng

```math
E(a)=K(a)+V(a)
```

tạo compromise length quy mô (scale / 규모) tự nhiên.

Đây là first-principles lập luận (reasoning / 추론) rất hữu ích ngay cả trước khi làm integral chính xác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Ví dụ tư duy variational** cho ta quy tắc; **Adiabatic approximation** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Born–Oppenheimer như separation of scales** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Gần degeneracy hoặc mức (level / 수준) crossing, approximation dễ thất bại.

Adiabatic lập luận (reasoning / 추론) là nền cho:

```text
Born–Oppenheimer approximation
adiabatic quantum control
Berry phase
slow parameter cycles
```

> **Chuyển mạch:** Trong **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Born–Oppenheimer như separation of scales** tiếp nhận điểm tựa từ **Adiabatic approximation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **WKB và giới hạn bán cổ điển** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Born–Oppenheimer như separation of scales

Nuclei nặng hơn electron rất nhiều.

Một first approximation là giữ nuclei gần cố định khi giải electronic bài toán (problem / 문제), rồi dùng electronic năng lượng (energy / 에너지) làm effective potential cho nuclear motion.

Chuỗi lập luận (reasoning / 추론) là

```text
mass scale separation
→ time-scale separation
→ fast electron / slow nuclei
→ approximate factorization
```

Approximation thất bại mạnh hơn gần electronic degeneracy hoặc nonadiabatic chuyển tiếp (transition / 전이).

> **Chuyển mạch:** Ở chặng này của **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Born–Oppenheimer như separation of scales** đã nêu tiêu chí phân biệt, còn **WKB và giới hạn bán cổ điển** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **WKB tunneling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## WKB và giới hạn bán cổ điển

Trong 1D,

```math
-\frac{\hbar^2}{2m}\psi''+V(x)\psi=E\psi.
```

Đặt cục bộ (local / 로컬) classical momentum

```math
p(x)=\sqrt{2m(E-V(x))}.
```

Khi potential thay đổi chậm trên cục bộ (local / 로컬) wavelength quy mô (scale / 규모), nghiệm WKB trong classically allowed region có dạng

```math
\psi(x)
\approx
\frac{C}{\sqrt{p(x)}}
\exp\left(
\pm\frac{i}{\hbar}
\int^xp(x')dx'
\right).
```

Pha là classical hành động (action / 동작) chia `\hbar`.

Điều này nối wavefunction với Hamilton–Jacobi/hành động (action / 동작) formulation của mechanics.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **WKB và giới hạn bán cổ điển** đã nêu tiêu chí phân biệt, còn **WKB tunneling** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Turning điểm (point / 지점) là nơi WKB thất bại cục bộ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Alpha decay và fusion penetration có thể được hiểu bằng cùng cấu trúc (structure / 구조).

> **Chuyển mạch:** Trong **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Turning điểm (point / 지점) là nơi WKB thất bại cục bộ** tiếp nhận điểm tựa từ **WKB tunneling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mean-field approximation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Turning điểm (point / 지점) là nơi WKB thất bại cục bộ

Tại

```math
E=V(x),
```

ta có

```math
p(x)=0.
```

WKB amplitude `1/\sqrt{p}` trở nên singular, nên approximation không còn hợp lệ ngay tại turning điểm (point / 지점).

Cần liên kết (connection / 연결) formulas hoặc cục bộ (local / 로컬) Airy-function treatment để nối hai miền.

Đây là ví dụ quan trọng: một approximation có thể rất tốt gần như mọi nơi nhưng vẫn hỏng ở một vùng nhỏ có cấu trúc đặc biệt.

> **Chuyển mạch:** Ở chặng này của **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Mean-field approximation** tiếp nhận điểm tựa từ **Turning điểm (point / 지점) là nơi WKB thất bại cục bộ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Effective lý thuyết (theory / 이론) và tích phân bỏ bậc tự do** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mean-field approximation

Trong many-body hệ thống (system / 시스템), tương tác (interaction / 상호작용) của mỗi particle với mọi particle khác tạo bài toán cực lớn.

Mean-field idea thay fluctuating many-body môi trường (environment / 환경) bằng effective average trường dữ liệu (field / 필드) được xác định self-consistently.

Hartree và Hartree–Fock là ví dụ điển hình.

Workflow thường là

```text
initial guess
→ solve one-particle effective equations
→ recompute density/field
→ iterate to self-consistency
```

Mean trường dữ liệu (field / 필드) thường bỏ qua correlation hoặc fluctuation beyond average phản hồi (response / 응답).

Nó có thể rất tốt ở một số regime nhưng thất bại gần trọng yếu (critical / 중요) điểm (point / 지점), low dimension hoặc strongly correlated trạng thái (state / 상태).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Effective lý thuyết (theory / 이론) và tích phân bỏ bậc tự do** tiếp nhận điểm tựa từ **Mean-field approximation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lỗi (error / 오류) điều khiển (control / 제어) và asymptotic series** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Effective lý thuyết (theory / 이론) và tích phân bỏ bậc tự do

Một cách xấp xỉ sâu hơn là không cố mô tả mọi microscopic degree of freedom.

Ta giữ các biến low-energy/relevant và hấp thụ physics của quy mô (scale / 규모) cao vào effective parameters và operators.

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

> **Chuyển mạch:** Trong **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Lỗi (error / 오류) điều khiển (control / 제어) và asymptotic series** tiếp nhận điểm tựa từ **Effective lý thuyết (theory / 이론) và tích phân bỏ bậc tự do** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khi nào nên dùng numerical phương thức (method / 메서드)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lỗi (error / 오류) điều khiển (control / 제어) và asymptotic series

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

> **Chuyển mạch:** Ở chặng này của **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Khi nào nên dùng numerical phương thức (method / 메서드)?** tiếp nhận điểm tựa từ **Lỗi (error / 오류) điều khiển (control / 제어) và asymptotic series** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khi nào nên dùng numerical phương thức (method / 메서드)?

Nếu không có small parameter rõ ràng và variational/semiclassical approximations không đủ, numerical methods có thể phù hợp hơn:

```text
matrix diagonalization
finite difference / finite element
basis expansion
Monte Carlo
DMRG / tensor-network methods
```

Nhưng numerical kết quả (result / 결과) vẫn phải kiểm tra convergence và finite-size/basis truncation errors.

Máy tính không loại bỏ approximation; nó chuyển approximation sang discretization và finite biểu diễn (representation / 표현).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Khi nào nên dùng numerical phương thức (method / 메서드)?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Các phương pháp xấp xỉ có thể nhìn theo ba câu hỏi:

```text
1. có một bài toán gần đó đã giải được không?
2. có parameter hoặc scale separation nào nhỏ không?
3. error được kiểm soát bằng cách nào?
```

Approximation tốt không phải “làm sai cho dễ”. Nó là việc bỏ đúng những phần nhỏ so với câu hỏi đang xét và biết rõ chi phí của việc bỏ chúng.

> **Chuyển mạch:** Trong **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, **Những ngộ nhận thường gặp (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Perturbation nhỏ nghĩa coefficient trước `V` nhỏ là đủ”

Không. Relevant ma trận (matrix / 행렬) elements phải nhỏ so với năng lượng (energy / 에너지) gaps; near degeneracy có thể phá approximation.

### “Variational phương thức (method / 메서드) cho đúng ground trạng thái (state / 상태) nếu minimize đủ tốt”

Không nhất thiết. Nó chỉ tối ưu trong trial family đã chọn. Family nghèo vẫn cho bound kém.

### “Adiabatic nghĩa thay đổi chậm theo clock thời gian (time / 시간)”

Không có một threshold tuyệt đối. “Chậm” phải so với nội bộ (internal / 내부) năng lượng (energy / 에너지) gaps/thời gian (time / 시간) scales của hệ.

### “WKB dùng được tại mọi điểm nếu `\hbar` nhỏ”

Không. Turning điểm (point / 지점) là vùng thất bại điển hình.

### “Numerical solution là chính xác (exact / 정확한)”

Không. Basis cutoff, grid spacing, timestep và finite precision đều tạo approximation mới.

> **Chuyển mạch:** Ở chặng này của **Các phương pháp xấp xỉ trong cơ học lượng tử: nhiễu loạn, biến phân và bán cổ điển**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Nền tảng lượng tử](00_quantum_foundations.md), [Các hệ lượng tử mẫu](01_quantum_systems.md), [Đại số tuyến tính và Taylor](../00_foundations/03_mathematical_language.md).

**Liên hệ tiếp:** [Động lực học phụ thuộc thời gian và tán xạ](06_time_dependent_scattering.md), [Vật lý nguyên tử](../09_atomic_nuclear_particle/00_atomic_physics.md), [Vật lý phân tử](../09_atomic_nuclear_particle/04_molecular_physics.md), [Vật lý tính toán](../12_experimental_computational/02_computational_physics.md), [Berry phase và topology](../10_condensed_matter_devices/06_berry_phase_quantum_hall_topology.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
