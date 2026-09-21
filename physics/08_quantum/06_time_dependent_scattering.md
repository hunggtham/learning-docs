# Động lực học lượng tử phụ thuộc thời gian và tán xạ

Các chương lượng tử cơ bản thường bắt đầu bằng trạng thái dừng và phương trình Schrödinger không phụ thuộc thời gian. Cách đó rất hữu ích để hiểu phổ năng lượng, giếng thế và dao động tử. Nhưng nhiều thí nghiệm thật sự là bài toán **động lực học**: bật một trường ngoài, chiếu laser vào nguyên tử, chuẩn bị một gói sóng rồi quan sát nó lan truyền, hoặc bắn hạt vào mục tiêu và đo xác suất tán xạ.

Chương này nối trạng thái dừng với các quá trình lượng tử thay đổi theo thời gian.

## Phương trình Schrödinger phụ thuộc thời gian

Trạng thái lượng tử `|\psi(t)\rangle` của hệ kín tiến hóa theo

```math
i\hbar\frac{d}{dt}|\psi(t)\rangle
=\hat H(t)|\psi(t)\rangle.
```

Nếu Hamiltonian không phụ thuộc thời gian,

```math
\hat H|n\rangle=E_n|n\rangle,
```

thì mỗi trạng thái riêng tiến hóa chỉ bằng một pha:

```math
|n,t\rangle
=e^{-iE_nt/\hbar}|n\rangle.
```

Một chồng chập

```math
|\psi(0)\rangle=\sum_n c_n|n\rangle
```

trở thành

```math
|\psi(t)\rangle
=\sum_n c_ne^{-iE_nt/\hbar}|n\rangle.
```

Các hệ số xác suất `|c_n|^2` không đổi trong cơ sở năng lượng nếu Hamiltonian cố định, nhưng pha tương đối giữa các thành phần thay đổi và có thể ảnh hưởng đại lượng quan sát.

## Toán tử tiến hóa thời gian

Với Hamiltonian không phụ thuộc thời gian,

```math
U(t)=e^{-i\hat Ht/\hbar}
```

và

```math
|\psi(t)\rangle=U(t)|\psi(0)\rangle.
```

`U` là toán tử đơn nhất (unitary), nên

```math
U^\dagger U=I.
```

Điều này bảo toàn chuẩn của trạng thái và do đó bảo toàn tổng xác suất.

Nếu Hamiltonian phụ thuộc thời gian, các Hamiltonian tại hai thời điểm khác nhau có thể không giao hoán. Khi đó biểu thức mũ đơn giản không còn đủ và cần toán tử sắp thứ tự thời gian (time ordering).

## Gói sóng và lan truyền

Một hạt tự do không nhất thiết ở trạng thái sóng phẳng có động lượng xác định. Một trạng thái cục bộ hơn phải là chồng chập nhiều động lượng:

```math
\psi(x,0)
=\int A(k)e^{ikx}\,dk.
```

Mỗi thành phần có năng lượng

```math
E(k)=\frac{\hbar^2k^2}{2m},
```

nên sau thời gian `t`,

```math
\psi(x,t)
=\int A(k)e^{i(kx-\omega(k)t)}dk.
```

Vì `\omega(k)` phụ thuộc phi tuyến vào `k`, các thành phần pha khác nhau dần và gói sóng thường **lan rộng (wave-packet spreading)**.

Đây là hiệu ứng động lực học lượng tử thực, không phải chỉ sai số phép đo.

## Vận tốc nhóm

Tâm của một gói sóng hẹp trong không gian `k` chuyển động gần với vận tốc nhóm

```math
v_g=\frac{d\omega}{dk}.
```

Với hạt tự do không tương đối tính,

```math
\omega=\frac{\hbar k^2}{2m},
```

nên

```math
v_g=\frac{\hbar k}{m}=rac{p}{m}.
```

Kết quả nối ngôn ngữ sóng với vận tốc hạt cổ điển.

## Nhiễu loạn phụ thuộc thời gian

Giả sử Hamiltonian gồm phần không đổi và một nhiễu nhỏ biến thiên theo thời gian:

```math
\hat H(t)=\hat H_0+\hat V(t).
```

Ta dùng các trạng thái riêng của `H_0` làm cơ sở rồi hỏi nhiễu `V(t)` làm biên độ chuyển trạng thái thay đổi ra sao.

Ở bậc nhất, biên độ chuyển từ `|i\rangle` sang `|f\rangle` có cấu trúc

```math
c_f^{(1)}(t)
\propto
\frac{1}{i\hbar}
\int_0^t
\langle f|\hat V(t')|i\rangle
 e^{i\omega_{fi}t'}dt',
```

với

```math
\omega_{fi}=\frac{E_f-E_i}{\hbar}.
```

Tích phân cho thấy hai yếu tố quyết định chuyển trạng thái:

```text
matrix element: nhiễu có ghép hai trạng thái hay không
frequency matching: tần số kích thích có phù hợp chênh lệch năng lượng hay không
```

## Cộng hưởng lượng tử

Nếu

```math
\hat V(t)\propto\cos\omega t,
```

chuyển trạng thái mạnh khi

```math
\hbar\omega\approx E_f-E_i.
```

Đây là nguồn gốc của phổ hấp thụ và nhiều kỹ thuật cộng hưởng.

Cấu trúc này rất giống dao động cưỡng bức cổ điển: hệ phản ứng mạnh khi kích thích có tần số phù hợp với một chênh lệch tần số tự nhiên. Nhưng trong lượng tử, “mode” tương ứng là các trạng thái năng lượng và quá trình chuyển giữa chúng.

## Quy tắc chọn lọc

Ngay cả khi tần số phù hợp, chuyển trạng thái có thể bị cấm nếu phần tử ma trận

```math
\langle f|\hat V|i\rangle
```

bằng không do đối xứng.

Ví dụ trong chuyển mức lưỡng cực điện, cấu trúc đối xứng của hàm sóng dẫn tới các quy tắc chọn lọc cho mômen động lượng.

Do đó phổ không chỉ đo khoảng cách mức năng lượng; nó còn tiết lộ đối xứng của trạng thái và dạng tương tác với trường ngoài.

## Quy tắc vàng Fermi

Khi trạng thái cuối tạo thành một miền gần liên tục và nhiễu yếu kéo dài đủ lâu, tốc độ chuyển trạng thái thường có dạng

```math
\Gamma_{i\to f}
=\frac{2\pi}{\hbar}
|\langle f|V|i\rangle|^2
\rho(E_f),
```

trong đó `\rho(E_f)` là mật độ trạng thái cuối.

Công thức này cho thấy tốc độ quá trình phụ thuộc cả:

```text
độ mạnh coupling
×
số lượng trạng thái cuối có thể tiếp cận
```

Nó xuất hiện trong phân rã lượng tử, hấp thụ photon, tán xạ và vận chuyển điện tử.

## Bài toán tán xạ

Trong tán xạ, ta chuẩn bị một trạng thái tới, cho nó tương tác với một thế `V(\mathbf r)`, rồi quan sát phân bố trạng thái đi ra.

Ở rất xa vùng tương tác, hàm sóng có cấu trúc gần

```math
\psi(\mathbf r)
\sim
e^{ikz}
+f(\theta,\phi)\frac{e^{ikr}}{r}.
```

Hạng đầu là sóng tới. Hạng thứ hai là sóng cầu đi ra, với `f(\theta,\phi)` là **biên độ tán xạ (scattering amplitude)**.

Tiết diện vi phân là

```math
\frac{d\sigma}{d\Omega}
=|f(\theta,\phi)|^2.
```

Nó cho biết xác suất tương đối để hạt bị tán xạ vào một góc nhất định.

## Vì sao dùng tiết diện?

Trong thí nghiệm chùm hạt, ta không theo dõi trực tiếp “bán kính hình học” của tương tác. Ta đo tốc độ sự kiện theo góc và cường độ chùm tới.

Tiết diện (cross section) có đơn vị diện tích, nhưng nên hiểu như thước đo xác suất tương tác hiệu dụng hơn là diện tích vật thể cơ học thật.

Một hạt điểm vẫn có thể có tiết diện tán xạ khác không vì tương tác trường lượng tử hoặc thế năng.

## Xấp xỉ Born

Nếu thế tán xạ yếu, xấp xỉ Born bậc nhất cho biên độ tán xạ tỉ lệ với biến đổi Fourier của thế:

```math
f(\mathbf q)
\propto
\int e^{-i\mathbf q\cdot\mathbf r}
V(\mathbf r)d^3r.
```

`\mathbf q` là độ truyền động lượng.

Đây là một liên hệ rất sâu: phân bố góc của hạt tán xạ chứa thông tin Fourier về cấu trúc không gian của mục tiêu.

Nhiễu xạ tia X, tán xạ neutron và nhiều kỹ thuật cấu trúc vật chất đều dùng nguyên lý tương tự.

## Partial waves

Với thế đối xứng cầu, ta có thể phân rã sóng tán xạ theo mômen động lượng:

```math
\psi=\sum_{\ell=0}^{\infty}\psi_\ell.
```

Mỗi `\ell` là một kênh tán xạ riêng với độ dịch pha (phase shift) `\delta_\ell`.

Ở năng lượng thấp, chỉ một vài `\ell` nhỏ đóng góp đáng kể; thường mode `s` với `\ell=0` chi phối.

Đây là một ví dụ khác của nguyên lý theo thang: khi bước sóng lớn hơn kích thước nguồn, hệ không “nhìn thấy” các chi tiết góc bậc cao.

## Resonance trong tán xạ

Nếu năng lượng hạt tới gần một trạng thái bán liên kết của hệ tương tác, tiết diện có thể tăng mạnh. Đây là cộng hưởng tán xạ.

Một dạng điển hình gần cộng hưởng là Breit–Wigner:

```math
\sigma(E)
\propto
\frac{1}
{(E-E_0)^2+\Gamma^2/4}.
```

`E_0` là năng lượng cộng hưởng và `\Gamma` liên hệ độ rộng cũng như thời gian sống của trạng thái.

Độ rộng lớn thường tương ứng thời gian sống ngắn, phản ánh quan hệ năng lượng–thời gian ở mức động lực học phổ.

## Ma trận S

Một cách mô tả tổng quát tán xạ là ánh xạ trạng thái tới `|in\rangle` thành trạng thái đi ra `|out\rangle` bằng ma trận tán xạ `S`:

```math
|out\rangle=S|in\rangle.
```

Tính đơn nhất của `S` phản ánh bảo toàn tổng xác suất.

Trong lý thuyết trường lượng tử, phần lớn dự đoán thực nghiệm cho collider cuối cùng được tổ chức dưới ngôn ngữ biên độ và ma trận `S`.

## Khi mô tả trạng thái thuần không đủ?

Nếu hệ tương tác với môi trường, mô tả bằng một vectơ trạng thái của riêng hệ có thể không còn đủ. Ta dùng ma trận mật độ và phương trình động lực học hệ mở.

Mất kết hợp (decoherence) làm các pha tương đối khó quan sát khi thông tin rò vào môi trường. Vì vậy động lực học lượng tử thực nghiệm thường nằm giữa hai giới hạn:

```text
hệ kín → tiến hóa unitary
hệ mở → unitary toàn cục nhưng hệ con có decoherence và dissipation
```

## Mô hình tư duy (Mental Model)

Lượng tử phụ thuộc thời gian không chỉ là “cho `t` vào hàm sóng”. Nó là bài toán về cách **biên độ xác suất và pha** dịch chuyển giữa các trạng thái khi Hamiltonian tiến hóa.

Tán xạ thì đảo hướng tư duy: ta biết trạng thái tới và trạng thái đi ra, rồi suy ngược cấu trúc của tương tác ở giữa.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Nếu Hamiltonian không đổi, trạng thái vật lý không đổi”

Chỉ trạng thái riêng năng lượng thay đổi bằng pha toàn cục. Chồng chập nhiều mức có pha tương đối biến thiên và có thể tạo đại lượng quan sát phụ thuộc thời gian.

### “Tiết diện là diện tích hình học thật của hạt”

Không. Nó là đại lượng xác suất hiệu dụng của quá trình tán xạ.

### “Tần số photon đúng bằng chênh lệch năng lượng thì chuyển mức chắc chắn xảy ra”

Không. Còn phụ thuộc phần tử ma trận, đối xứng, thời gian tương tác, độ rộng phổ và các cơ chế cạnh tranh.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Nền tảng lượng tử](00_quantum_foundations.md), [Các hệ lượng tử mẫu](01_quantum_systems.md), [Lý thuyết nhiễu loạn](04_approximation_perturbation.md).

**Liên hệ tiếp:** [Vật lý nguyên tử](../09_atomic_nuclear_particle/00_atomic_physics.md), [Bức xạ và detector](../09_atomic_nuclear_particle/02_radiation_detection.md), [Mô hình Chuẩn](../09_atomic_nuclear_particle/03_particle_standard_model.md).
