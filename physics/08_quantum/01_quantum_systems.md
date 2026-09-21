# Các hệ lượng tử mẫu: giếng thế, dao động tử điều hòa và xuyên hầm

Các hệ mẫu trong cơ học lượng tử không chỉ là bài tập kỹ thuật. Chúng đóng vai trò giống như “mẫu thiết kế” của lý thuyết: cùng một cấu trúc toán học xuất hiện lặp lại trong nguyên tử, phân tử, chất rắn, quang học lượng tử và vật lý hạt.

Ba mô hình quan trọng nhất ở mức nền tảng là:

```text
hạt trong giếng thế
→ lượng tử hóa từ điều kiện biên

dao động tử điều hòa
→ lượng tử hóa các mode gần cân bằng

xuyên hầm
→ xác suất khác không trong vùng cổ điển bị cấm
```

## Hạt trong giếng thế vô hạn

Xét một hạt khối lượng `m` bị giữ trong miền

```math
0<x<L
```

với thế

```math
V(x)=0\quad 0<x<L,
```

và thế vô hạn ở ngoài miền.

Vì xác suất tìm thấy hạt ngoài hộp bằng không, hàm sóng phải thỏa điều kiện biên

```math
\psi(0)=\psi(L)=0.
```

Bên trong hộp, phương trình Schrödinger không phụ thuộc thời gian là

```math
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}=E\psi.
```

Đặt

```math
k=\frac{\sqrt{2mE}}{\hbar},
```

ta được nghiệm tổng quát

```math
\psi(x)=A\sin(kx)+B\cos(kx).
```

Điều kiện `\psi(0)=0` buộc

```math
B=0.
```

Điều kiện tại `x=L` yêu cầu

```math
\sin(kL)=0,
```

nên

```math
kL=n\pi,
\qquad n=1,2,3,\ldots
```

Do đó

```math
k_n=\frac{n\pi}{L}
```

và các mức năng lượng là

```math
E_n=\frac{n^2\pi^2\hbar^2}{2mL^2}.
```

Sau khi chuẩn hóa,

```math
\psi_n(x)=\sqrt{\frac{2}{L}}
\sin\left(\frac{n\pi x}{L}\right).
```

## Vì sao năng lượng bị lượng tử hóa?

Các giá trị năng lượng rời rạc không được gắn vào bằng tay. Chúng xuất hiện vì phương trình vi phân và điều kiện biên chỉ cho phép một số mode không gian nhất định.

Cấu trúc này giống sóng dừng trên một sợi dây cố định hai đầu:

```text
phương trình sóng
+ điều kiện biên
→ chỉ một số bước sóng được phép
```

Trong bài lượng tử,

```text
Schrödinger equation
+ boundary conditions
→ chỉ một số eigenstate/eigenvalue được phép
```

Đây là cầu nối trực tiếp giữa Fourier, bài toán trị riêng và lượng tử hóa.

## Vì sao không có trạng thái `n=0`?

Nếu chọn `n=0`, ta có

```math
\psi(x)=0
```

trên toàn miền. Đây không phải một trạng thái lượng tử vì xác suất chuẩn hóa bằng không.

Do đó trạng thái cơ bản là `n=1`, với năng lượng

```math
E_1=\frac{\pi^2\hbar^2}{2mL^2}>0.
```

Ngay cả ở trạng thái năng lượng thấp nhất, hạt vẫn không thể đồng thời bị giam trong hộp và có động lượng bằng chính xác zero. Điều này phù hợp với nguyên lý bất định.

## Ý nghĩa của scale `1/L^2`

Năng lượng trong giếng thế tỉ lệ

```math
E_n\propto\frac{1}{L^2}.
```

Khi hộp nhỏ hơn, gradient không gian của hàm sóng phải lớn hơn để vẫn thỏa điều kiện biên. Gradient lớn tương ứng động lượng lớn hơn và do đó động năng lớn hơn.

Đây là lý do confinement ở nanoscale có thể tạo energy spacing đáng kể, trong khi ở scale vĩ mô các mức nằm rất sát nhau và gần như liên tục.

## Xác suất và giá trị kỳ vọng trong hộp

Mật độ xác suất là

```math
\rho_n(x)=|\psi_n(x)|^2.
```

Nó không đồng đều. Ở các node của hàm sóng, xác suất bằng zero.

Với một trạng thái chuẩn hóa, giá trị kỳ vọng vị trí là

```math
\langle x\rangle
=\int_0^L \psi^*(x)x\psi(x)\,dx.
```

Do đối xứng của giếng thế,

```math
\langle x\rangle=\frac{L}{2}
```

cho mọi eigenstate năng lượng.

Nhưng điều này không nghĩa mỗi phép đo vị trí luôn cho `L/2`; đó chỉ là trung bình thống kê của nhiều phép đo trên cùng trạng thái chuẩn bị.

## Giếng thế hữu hạn

Giếng vô hạn là lý tưởng hóa. Với giếng hữu hạn, hàm sóng không dừng đột ngột ở biên mà xuyên một đoạn vào vùng có thế cao hơn.

Điều này dẫn tới hai kết quả quan trọng:

```text
bound state vẫn có thể có năng lượng rời rạc
nhưng wavefunction có tail ngoài vùng “giữ hạt” chính
```

Tail này là tiền đề tự nhiên cho hiện tượng xuyên hầm.

## Dao động tử điều hòa lượng tử

Xét thế

```math
V(x)=\frac12m\omega^2x^2.
```

Đây không chỉ là mô hình lò xo. Bất kỳ thế trơn nào gần một cực tiểu ổn định đều có thể khai triển Taylor:

```math
V(x)\approx V(x_0)
+\frac12V''(x_0)(x-x_0)^2+\cdots
```

vì tại cực tiểu

```math
V'(x_0)=0.
```

Do đó dao động tử điều hòa là mô hình gần đúng phổ quát cho dao động nhỏ quanh cân bằng.

Các mức năng lượng là

```math
E_n=\hbar\omega\left(n+\frac12\right),
\qquad n=0,1,2,\ldots
```

Khoảng cách giữa hai mức liên tiếp luôn bằng

```math
E_{n+1}-E_n=\hbar\omega.
```

## Năng lượng điểm không

Trạng thái cơ bản có

```math
E_0=\frac12\hbar\omega.
```

Nó không thể có cả

```math
x=0
```

và

```math
p=0
```

chính xác vì như vậy

```math
\Delta x=\Delta p=0
```

sẽ vi phạm nguyên lý bất định.

Năng lượng điểm không vì thế không chỉ là một số hạng được thêm vào công thức; nó phản ánh cấu trúc không thể triệt tiêu hoàn toàn cả biến thiên vị trí lẫn động lượng.

## Phương pháp toán tử nâng–hạ

Dao động tử có thể giải bằng phương trình vi phân, nhưng đại số toán tử cho thấy cấu trúc sâu hơn.

Ta định nghĩa toán tử hạ và nâng `a`, `a^\dagger` sao cho

```math
\hat H
=\hbar\omega
\left(a^\dagger a+\frac12\right).
```

Toán tử số

```math
\hat N=a^\dagger a
```

có trị riêng

```math
n=0,1,2,\ldots
```

và

```math
a^\dagger|n\rangle
\propto |n+1\rangle,
```

```math
a|n\rangle
\propto |n-1\rangle.
```

Mỗi lần nâng trạng thái, năng lượng tăng đúng

```math
\hbar\omega.
```

Đại số này trở thành ngôn ngữ cốt lõi của quang học lượng tử và lý thuyết trường: photon, phonon và nhiều quasiparticle mode được mô tả như các kích thích lượng tử của những mode dao động.

## Xuyên hầm lượng tử

Xét một rào thế cao `V_0` có chiều rộng `a`, trong khi năng lượng hạt thỏa

```math
E<V_0.
```

Trong cơ học cổ điển,

```math
K=E-V_0<0
```

là không thể, nên hạt không qua rào.

Trong cơ học lượng tử, phương trình Schrödinger bên trong barrier cho nghiệm dạng mũ

```math
\psi(x)\sim e^{\pm\kappa x},
```

với

```math
\kappa=
\frac{\sqrt{2m(V_0-E)}}{\hbar}.
```

Wavefunction suy giảm trong barrier nhưng không nhất thiết bằng zero. Nếu barrier hữu hạn, biên độ có thể còn khác zero ở phía bên kia.

Trong giới hạn barrier tương đối dày,

```math
T\sim e^{-2\kappa a}.
```

Đây là xác suất truyền qua gần đúng.

## Ý nghĩa của phụ thuộc hàm mũ

Vì

```math
T\propto e^{-2\kappa a},
```

một thay đổi rất nhỏ của chiều rộng `a` có thể tạo thay đổi rất lớn của xác suất xuyên hầm.

Đó là cơ sở vật lý của kính hiển vi xuyên hầm quét (Scanning Tunneling Microscope, STM). Khoảng cách đầu dò–bề mặt thay đổi ở scale nguyên tử làm tunneling current thay đổi mạnh, từ đó có thể suy ra topography và electronic structure.

## Xuyên hầm không phải “mượn năng lượng”

Một cách giải thích phổ biến nhưng sai là hạt “mượn năng lượng trong thời gian ngắn” để vượt barrier.

Trong bài stationary tunneling, năng lượng toàn phần `E` của trạng thái vẫn được bảo toàn. Điều thay đổi là cấu trúc nghiệm của phương trình Schrödinger trong vùng mà động năng cổ điển sẽ âm.

Do đó không cần vi phạm conservation of energy để có tunneling.

## Ứng dụng của tunneling

Tunneling xuất hiện trong nhiều hệ:

```text
alpha decay
STM
Josephson junction
tunnel diode
nuclear fusion ở nhiệt độ sao
field emission
```

Các ví dụ này có chi tiết khác nhau, nhưng cùng chia sẻ cấu trúc: một amplitude lượng tử suy giảm qua vùng classically forbidden nhưng không bằng zero tuyệt đối.

## Dòng xác suất

Trong cơ học lượng tử một chiều, dòng xác suất có thể viết

```math
j=\frac{\hbar}{2mi}
\left(
\psi^*\frac{d\psi}{dx}
-\psi\frac{d\psi^*}{dx}
\right).
```

Nó liên hệ với phương trình liên tục

```math
\frac{\partial |\psi|^2}{\partial t}
+\nabla\cdot\mathbf j=0.
```

Đây là dạng conservation law của xác suất.

Trong bài scattering/tunneling, hệ số phản xạ và truyền qua được xác định từ tỉ số các probability current, chứ không chỉ từ biên độ wavefunction một cách tùy ý.

## Liên hệ với giới hạn cổ điển

Định lý Ehrenfest cho

```math
m\frac{d^2\langle x\rangle}{dt^2}
=-\left\langle\frac{dV}{dx}\right\rangle.
```

Nếu wavepacket đủ hẹp và thế biến thiên chậm trên kích thước wavepacket,

```math
\left\langle\frac{dV}{dx}\right\rangle
\approx
\frac{dV}{dx}\bigg|_{\langle x\rangle},
```

thì tâm wavepacket gần tuân phương trình Newton.

Nhưng classical limit không chỉ đến từ `\hbar` nhỏ theo nghĩa tuyệt đối. Nó còn phụ thuộc scale của action, decoherence và độ phân giải quan sát.

## Assumptions và giới hạn mô hình

### Giếng thế vô hạn

Wall vô hạn không tồn tại theo nghĩa vật lý chính xác. Nó là giới hạn lý tưởng hóa của confinement mạnh.

### Dao động tử điều hòa

Mô hình bậc hai chỉ tốt khi dao động quanh cực tiểu đủ nhỏ để các hạng Taylor bậc cao có thể bỏ qua.

### Công thức tunneling mũ

Biểu thức

```math
T\sim e^{-2\kappa a}
```

chỉ là xấp xỉ trong một số regime. Barrier profile thực, matching conditions và resonance có thể làm transmission phức tạp hơn.

## Mô hình tư duy (Mental Model)

Ba hệ mẫu này cho ba bài học nền tảng:

```text
boundary condition
→ quantization

local quadratic potential
→ harmonic modes

wavefunction tail
→ tunneling
```

Điểm chung là trạng thái lượng tử được xác định không chỉ bởi năng lượng mà bởi phương trình, hình học, potential và điều kiện biên.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Năng lượng lượng tử luôn rời rạc”

Không. Bound states thường cho phổ rời rạc, nhưng free/scattering states có thể có phổ liên tục.

### “Ground state là hạt đứng yên”

Không. Ground state có thể có năng lượng và momentum uncertainty khác zero.

### “Tunneling vi phạm bảo toàn năng lượng”

Không. Stationary state giữ nguyên tổng năng lượng; phần classically forbidden nằm ở cấu trúc của nghiệm, không phải ở việc hạt vay năng lượng.

### “Expectation value là kết quả chắc chắn của phép đo”

Không. Nó là trung bình thống kê của phân bố kết quả trên nhiều lần chuẩn bị giống nhau.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Nền tảng lượng tử](00_quantum_foundations.md), [Sóng và Fourier](../02_oscillations_waves/01_waves_fourier_sound.md).

**Liên hệ tiếp:** [Xấp xỉ lượng tử](04_approximation_perturbation.md), [Vật lý nguyên tử](../09_atomic_nuclear_particle/00_atomic_physics.md), [Bán dẫn và thiết bị](../10_condensed_matter_devices/01_semiconductors_devices.md), [BEC và chất lưu lượng tử](../10_condensed_matter_devices/05_bec_superfluid_quantum_fluids.md).
