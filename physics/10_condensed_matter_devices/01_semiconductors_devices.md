# Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Bán dẫn và thiết bị: doping, P–N junction, diode, MOSFET và CMOS**. Route đi từ bands/carriers → doping/Fermi level → junction/diode → MOS field effect → CMOS switching, để vật liệu nối với chức năng mạch.

Bán dẫn là nơi nhiều lớp vật lý gặp nhau trực tiếp: cơ học lượng tử quyết định dải năng lượng; cơ học thống kê quyết định số trạng thái được chiếm; điện từ học quyết định thế và điện trường; khuếch tán quyết định chuyển động do độ dốc (gradient / 기울기) nồng độ; còn hình học thiết bị biến các cơ chế đó thành diode, transistor, LED và pin mặt trời.

Điểm quan trọng là một transistor số cuối cùng vẫn được điều khiển bởi các đại lượng liên tục:

```text
band structure
+ carrier statistics
+ electrostatics
+ drift/diffusion
+ recombination
+ geometry
→ device I–V behavior
```

## Bán dẫn nội tại và nồng độ hạt tải

Trong bán dẫn nội tại (intrinsic semiconductor), electron được kích thích từ dải hóa trị lên dải dẫn tạo đồng thời một electron và một lỗ trống.

Ở cân bằng nhiệt,

```math
n=p=n_i,
```

trong đó `n_i` là nồng độ hạt tải nội tại.

Trong mô hình không suy biến (non-degenerate approximation), nồng độ electron và lỗ trống gần đúng là

```math
n=N_C
\exp\left(-\frac{E_C-E_F}{k_BT}\right),
```

```math
p=N_V
\exp\left(-\frac{E_F-E_V}{k_BT}\right).
```

`N_C`, `N_V` là mật độ trạng thái hiệu dụng của dải dẫn và dải hóa trị.

Nhân hai biểu thức cho

```math
np=n_i^2.
```

Đây là **định luật tác dụng khối lượng (mass-action law)** cho bán dẫn ở cân bằng trong miền xấp xỉ này.

Nó cho thấy nếu doping làm electron tăng mạnh thì hole concentration giảm tương ứng ở equilibrium.

> **Chuyển mạch:** Trong **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Pha tạp và mức Fermi** tiếp nhận điểm tựa từ **Bán dẫn nội tại và nồng độ hạt tải** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Drift và diffusion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pha tạp và mức Fermi

Pha tạp (doping / 도핑) thêm impurity có mức năng lượng gần band edge.

### N-type

Donor dễ cho electron vào conduction band, nên

```text
n tăng
E_F dịch gần E_C hơn
```

### P-type

Acceptor dễ nhận electron từ valence band, tạo hole, nên

```text
p tăng
E_F dịch gần E_V hơn
```

Tên N/P không có nghĩa toàn vật liệu mang net charge lớn. Bulk vẫn gần trung hòa vì mobile carriers được cân bằng bởi ionized dopants cố định.

Ở doping rất mạnh, semiconductor có thể trở thành **suy biến (degenerate semiconductor)** và Maxwell–Boltzmann approximation không còn đủ; cần dùng Fermi–Dirac statistics đầy đủ.

> **Chuyển mạch:** Ở chặng này của **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Drift và diffusion** tiếp nhận điểm tựa từ **Pha tạp và mức Fermi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mobility không phải hằng số tuyệt đối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Drift và diffusion

Điện trường tạo vận tốc trôi trung bình

```math
\mathbf v_d=\mu\mathbf E,
```

với `\mu` là mobility.

Mật độ dòng do drift có dạng

```math
\mathbf J_{n,drift}=qn\mu_n\mathbf E.
```

Độ dốc (gradient / 기울기) concentration tạo diffusion. Với electron, một convention thường dùng là

```math
\mathbf J_{n,diff}=qD_n\nabla n.
```

Tổng dòng:

```math
\mathbf J_n
=qn\mu_n\mathbf E+qD_n\nabla n.
```

Với hole, dấu của diffusion term phụ thuộc cách viết carrier flux/hiện tại (current / 현재) convention.

Trong miền không suy biến, Einstein quan hệ (relation / 관계) là

```math
D=\mu\frac{k_BT}{q}.
```

Nó cho thấy drift và diffusion không phải hai cơ chế thống kê hoàn toàn độc lập; cả hai bắt nguồn từ vận chuyển (transport / 전송) của carrier trong môi trường nhiệt.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Mobility không phải hằng số tuyệt đối** tiếp nhận điểm tựa từ **Drift và diffusion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tiếp giáp P–N hình thành như thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mobility không phải hằng số tuyệt đối

Mobility bị ảnh hưởng bởi

```text
phonon scattering
ionized impurity scattering
defects
surface/interface roughness
carrier density
electric field
temperature
```

Do đó phương trình drift đơn giản chỉ là mô hình low-field hiệu dụng.

Ở trường dữ liệu (field / 필드) cao, carrier velocity có thể tiến tới saturation thay vì tiếp tục tăng tuyến tính với `E`.

> **Chuyển mạch:** Trong **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Tiếp giáp P–N hình thành như thế nào?** tiếp nhận điểm tựa từ **Mobility không phải hằng số tuyệt đối** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Band bending và electrostatic potential** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tiếp giáp P–N hình thành như thế nào?

Ngay sau khi ghép P và N, concentration độ dốc (gradient / 기울기) rất lớn.

Electron khuếch tán

```text
N side → P side
```

và hole khuếch tán

```text
P side → N side.
```

Khi các carrier này tái hợp, gần junction còn lại các ion donor dương ở phía N và ion acceptor âm ở phía P.

Các ion cố định tạo **vùng nghèo (depletion region / 공핍층)** gần như thiếu mobile carrier.

Charge separation tạo electric trường dữ liệu (field / 필드) hướng từ N sang P. trường dữ liệu (field / 필드) này tạo drift chống lại diffusion.

Ở thermal equilibrium:

```text
diffusion current + drift current = 0
```

nhưng từng thành phần riêng không nhất thiết bằng zero.

> **Chuyển mạch:** Ở chặng này của **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Band bending và electrostatic potential** tiếp nhận điểm tựa từ **Tiếp giáp P–N hình thành như thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Điện thế tiếp xúc nội tại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Band bending và electrostatic potential

Electron năng lượng (energy / 에너지) thay đổi theo electrostatic potential `\phi` gần như

```math
E_{electron}\sim -q\phi.
```

Vì `\phi(x)` thay đổi trong depletion region, conduction-band edge và valence-band edge cũng thay đổi theo vị trí trên band diagram.

Hiện tượng này được gọi là **uốn cong dải năng lượng (band bending)**.

Band diagram vì vậy là cách biểu diễn electrostatic potential bằng năng lượng (energy / 에너지) coordinates.

Ở equilibrium, Fermi mức (level / 수준) phải phẳng xuyên qua junction. Nếu `E_F` thay đổi theo vị trí ở một hệ cân bằng, carrier sẽ có xu hướng tái phân bố.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Điện thế tiếp xúc nội tại** tiếp nhận điểm tựa từ **Band bending và electrostatic potential** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Depletion approximation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Điện thế tiếp xúc nội tại

Với abrupt PN junction không suy biến, built-in potential gần đúng là

```math
V_{bi}
=\frac{k_BT}{q}
\ln\left(
\frac{N_AN_D}{n_i^2}
\right).
```

Biểu thức này nối trực tiếp:

```text
doping concentration
+ thermal statistics
→ electrostatic barrier
```

Nó không phải “pin ẩn” có thể lấy điện liên tục ra ngoài. Ở equilibrium, electrochemical potentials của toàn cấu trúc đã cân bằng nên không có net DC power đầu ra (output / 출력).

> **Chuyển mạch:** Trong **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Depletion approximation** tiếp nhận điểm tựa từ **Điện thế tiếp xúc nội tại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân cực thuận và phân cực ngược** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Depletion approximation

Một approximation rất hữu ích giả sử depletion region gần như không có mobile carriers; charge density chủ yếu do ionized dopants cố định.

Poisson equation là

```math
\frac{d^2\phi}{dx^2}
=-\frac{\rho(x)}{\varepsilon_s}.
```

Với abrupt junction, `\rho` gần piecewise constant trong depletion region, nên electric trường dữ liệu (field / 필드) gần piecewise tuyến tính (linear / 선형) và potential gần quadratic.

Tổng depletion width dưới độ lệch (bias / 편향) `V` có dạng xấp xỉ

```math
W=
\sqrt{
\frac{2\varepsilon_s}{q}
\left(
\frac{1}{N_A}+\frac{1}{N_D}
\right)
(V_{bi}-V)
}.
```

Khi reverse độ lệch (bias / 편향) tăng, `V` âm theo convention forward-bias-positive, nên `W` tăng.

Junction capacitance do đó phụ thuộc điện áp.

> **Chuyển mạch:** Ở chặng này của **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Phân cực thuận và phân cực ngược** tiếp nhận điểm tựa từ **Depletion approximation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phương trình diode** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân cực thuận và phân cực ngược

### Forward độ lệch (bias / 편향)

Bên ngoài (external / 외부) voltage giảm effective barrier. Minority-carrier injection tăng mạnh, dẫn tới hiện tại (current / 현재) lớn hơn.

### Reverse độ lệch (bias / 편향)

Barrier tăng và depletion region rộng hơn. Dòng thường nhỏ cho đến breakdown.

Hai cơ chế breakdown chính là:

```text
Zener tunneling
avalanche multiplication
```

Cơ chế trội phụ thuộc doping và trường dữ liệu (field / 필드) quy mô (scale / 규모).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Phương trình diode** tiếp nhận điểm tựa từ **Phân cực thuận và phân cực ngược** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LED: band gap và photon** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phương trình diode

Trong mô hình lý tưởng hóa,

```math
I=I_S
\left(
 e^{qV/(nk_BT)}-1
\right).
```

Dạng hàm mũ xuất hiện từ carrier statistics và minority-carrier diffusion, không phải từ một quy tắc mạch tùy ý.

Các giả định (assumption / 가정) thường gồm:

```text
low-level injection
quasi-neutral regions
steady state
uniform temperature
idealized recombination
negligible series resistance
```

Ở hiện tại (current / 현재) lớn, series resistance; ở voltage thấp hoặc defect-rich junction, recombination; và ở reverse breakdown, các cơ chế khác làm phương trình đơn giản không còn đúng.

> **Chuyển mạch:** Trong **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **LED: band gap và photon** tiếp nhận điểm tựa từ **Phương trình diode** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Photodiode và pin mặt trời** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LED: band gap và photon

Trong direct-band-gap material, electron và hole có thể tái hợp radiatively với

```math
E_{photon}\approx E_g.
```

Do

```math
\lambda\approx\frac{hc}{E_g},
```

band gap quyết định quy mô (scale / 규모) của emission wavelength.

Trong indirect-gap material như silicon, chuyển tiếp (transition / 전이) thường cần phonon để hỗ trợ crystal-momentum conservation, nên light emission kém hiệu quả hơn.

> **Chuyển mạch:** Ở chặng này của **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Photodiode và pin mặt trời** tiếp nhận điểm tựa từ **LED: band gap và photon** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Từ tiếp giáp P–N đến MOS capacitor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Photodiode và pin mặt trời

Photon với

```math
hf\gtrsim E_g
```

có thể tạo electron–hole pair.

Built-in trường dữ liệu (field / 필드) trong junction giúp tách carrier trước khi chúng tái hợp.

Photodiode tối ưu tín hiệu (signal / 신호) detection; solar cell tối ưu năng lượng (energy / 에너지) extraction. Hai thiết bị (device / 장치) dùng cùng physics nhưng mục tiêu kỹ thuật (engineering / 엔지니어링) khác nhau.

Mất mát (loss / 손실) channels của solar cell gồm:

```text
sub-gap photons
thermalization của photon dư năng lượng
recombination
optical reflection
series/shunt losses
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Từ tiếp giáp P–N đến MOS capacitor** tiếp nhận điểm tựa từ **Photodiode và pin mặt trời** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Accumulation, depletion và inversion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Từ tiếp giáp P–N đến MOS capacitor

MOSFET được hiểu rõ nhất nếu trước tiên xem cấu trúc **MOS capacitor**:

```text
metal/gate
→ oxide
→ semiconductor
```

Oxide ngăn DC conduction lý tưởng nhưng cho electric trường dữ liệu (field / 필드) xuyên qua.

Gate voltage làm thay đổi surface potential trong semiconductor và do đó làm band edges cong gần giao diện (interface / 인터페이스).

Đây là bản chất electrostatic của field-effect điều khiển (control / 제어).

> **Chuyển mạch:** Trong **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Accumulation, depletion và inversion** tiếp nhận điểm tựa từ **Từ tiếp giáp P–N đến MOS capacitor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Oxide capacitance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Accumulation, depletion và inversion

Xét nền P-type.

### Accumulation

Gate voltage đủ âm hút hole về bề mặt:

```text
hole concentration tại surface tăng
```

### Depletion

Gate voltage dương đẩy hole khỏi giao diện (interface / 인터페이스), để lại ion acceptor cố định:

```text
surface mobile carrier giảm
```

### Inversion

Tăng gate voltage dương thêm làm band bending đủ mạnh để electron trở thành carrier chiếm ưu thế ngay tại bề mặt, dù bulk vẫn P-type.

Ta đã tạo một **inversion tầng (layer / 계층)** N-like ngay dưới oxide.

Đó chính là nền của kênh nMOS.

> **Chuyển mạch:** Ở chặng này của **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Oxide capacitance** tiếp nhận điểm tựa từ **Accumulation, depletion và inversion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Điện áp ngưỡng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Oxide capacitance

Với oxide dày `t_{ox}` và permittivity `\varepsilon_{ox}`, capacitance trên một đơn vị diện tích là

```math
C_{ox}'=\frac{\varepsilon_{ox}}{t_{ox}}.
```

Oxide mỏng hơn tăng gate điều khiển (control / 제어) vì capacitance lớn hơn, nhưng quá mỏng làm tunneling leakage tăng.

High-k dielectric cho phép tăng effective capacitance mà không cần vật lý (physical / 물리적) thickness nhỏ đến mức tunneling quá mạnh.

Đây là ví dụ trực tiếp của sự đánh đổi (trade-off / 트레이드오프) giữa electrostatics và quantum tunneling.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Điện áp ngưỡng** tiếp nhận điểm tựa từ **Oxide capacitance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **MOSFET channel và drain độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Điện áp ngưỡng

Threshold voltage `V_T` không phải một “công tắc kỳ diệu” nơi transistor đột ngột đổi từ zero hiện tại (current / 현재) sang full hiện tại (current / 현재).

Nó là một convention hữu ích đánh dấu regime hình thành strong inversion/channel theo mô hình (model / 모델).

`V_T` phụ thuộc vào:

```text
work-function difference
oxide capacitance
substrate doping
fixed/interface charge
body bias
temperature
```

Vì vậy threshold là thuộc tính (property / 속성) của cả cấu trúc, không chỉ của material bulk.

> **Chuyển mạch:** Trong **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **MOSFET channel và drain độ lệch (bias / 편향)** tiếp nhận điểm tựa từ **Điện áp ngưỡng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Subthreshold conduction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## MOSFET channel và drain độ lệch (bias / 편향)

Khi gate tạo inversion channel, nguồn (source / 소스) và drain nối carrier vào hai đầu channel.

Drain voltage tạo lateral electric trường dữ liệu (field / 필드) làm carrier drift.

Trong long-channel gradual-channel approximation, hiện tại (current / 현재) có thể được suy ra bằng cách tích phân cục bộ (local / 로컬) channel charge và drift velocity.

Ở vùng tuyến tính (linear / 선형), dạng gần đúng quen thuộc là

```math
I_D
\approx
\mu C_{ox}'\frac{W}{L}
\left[
(V_{GS}-V_T)V_{DS}
-\frac{V_{DS}^2}{2}
\right].
```

Khi

```math
V_{DS}\approx V_{GS}-V_T,
```

channel gần drain bị pinch-off trong ideal long-channel picture và hiện tại (current / 현재) đi vào saturation regime.

Dạng textbook saturation gần đúng:

```math
I_{D,sat}
\approx
\frac12
\mu C_{ox}'\frac{W}{L}
(V_{GS}-V_T)^2.
```

Các công thức này không phải law phổ quát; chúng dựa trên long-channel, mobility gần constant và quasi-static các giả định (assumptions / 가정들).

> **Chuyển mạch:** Ở chặng này của **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Subthreshold conduction** tiếp nhận điểm tựa từ **MOSFET channel và drain độ lệch (bias / 편향)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Short-channel effects** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Subthreshold conduction

Ngay dưới threshold, hiện tại (current / 현재) không bằng zero. Carrier concentration tại surface thay đổi gần exponential với gate voltage, tạo subthreshold hiện tại (current / 현재).

Subthreshold swing được đo bằng số millivolt gate voltage cần để hiện tại (current / 현재) thay đổi một decade.

Ở room temperature, MOSFET conventional có thermodynamic lower-bound lý tưởng khoảng

```math
60\;mV/decade
```

trong điều kiện thích hợp.

Kết quả này liên hệ trực tiếp với Boltzmann statistics và là một giới hạn quan trọng của low-voltage lô-gic (logic / 논리).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Short-channel effects** tiếp nhận điểm tựa từ **Subthreshold conduction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **FinFET và gate-all-around** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Short-channel effects

Khi channel length giảm, nguồn (source / 소스)/drain electrostatic fields bắt đầu cạnh tranh với gate trong việc điều khiển potential barrier.

Các hiệu ứng gồm:

```text
threshold-voltage roll-off
DIBL
velocity saturation
hot carriers
increased leakage
source-to-drain tunneling ở scale cực nhỏ
```

DIBL (Drain-Induced Barrier Lowering) nghĩa là tăng drain voltage làm source-channel barrier giảm, khiến gate mất một phần quyền kiểm soát.

Đây là lý do thiết bị (device / 장치) scaling không thể hiểu chỉ bằng việc “thu nhỏ hình học”. Electrostatic length scales phải giảm tương ứng.

> **Chuyển mạch:** Trong **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **FinFET và gate-all-around** tiếp nhận điểm tựa từ **Short-channel effects** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CMOS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## FinFET và gate-all-around

Planar gate chỉ điều khiển channel chủ yếu từ một mặt.

FinFET bao quanh channel nhiều mặt hơn; gate-all-around tiếp tục tăng electrostatic điều khiển (control / 제어).

Các kiến trúc này không thay đổi nguyên lý transistor cơ bản. Chúng thay đổi hình học (geometry / 기하학) để gate trường dữ liệu (field / 필드) kiểm soát channel tốt hơn so với nguồn (source / 소스)/drain fields.

> **Chuyển mạch:** Ở chặng này của **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **CMOS** tiếp nhận điểm tựa từ **FinFET và gate-all-around** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **RC delay và interconnect** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CMOS

CMOS dùng nMOS và pMOS bổ sung.

Trong ideal static trạng thái (state / 상태), một nhánh gần off nên direct DC đường dẫn (path / 경로) từ supply xuống ground rất nhỏ.

Động (dynamic / 동적) năng lượng (energy / 에너지) dùng để nạp/xả capacitance:

```math
E_{switch}\sim CV^2.
```

Với activity factor `\alpha`:

```math
P_{dynamic}\approx\alpha CV^2f.
```

Do phụ thuộc `V^2`, giảm supply voltage tiết kiệm năng lượng (energy / 에너지) rất mạnh. Nhưng voltage thấp làm giảm noise margin và drive hiện tại (current / 현재), nên xuất hiện sự đánh đổi (trade-off / 트레이드오프) power–hiệu năng (performance / 성능)–độ tin cậy (reliability / 신뢰성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **RC delay và interconnect** tiếp nhận điểm tựa từ **CMOS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quantum tunneling và scaling limit** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RC delay và interconnect

Gate và wiring tạo capacitance; conductor có resistance.

Một thời gian (time / 시간) quy mô (scale / 규모) đơn giản là

```math
\tau\sim RC.
```

Khi transistor nhỏ dần, interconnect delay, parasitic capacitance, coupling, inductance và tín hiệu (signal / 신호) integrity có thể chi phối hiệu năng (performance / 성능).

Vì vậy CPU speed không được quyết định chỉ bởi transistor switching thời gian (time / 시간).

> **Chuyển mạch:** Trong **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **RC delay và interconnect** đã nêu tiêu chí phân biệt, còn **Quantum tunneling và scaling limit** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Nhiệt và độ tin cậy (reliability / 신뢰성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quantum tunneling và scaling limit

Oxide quá mỏng cho gate leakage qua tunneling.

Channel cực ngắn có thể xuất hiện source-to-drain tunneling và quantum confinement làm band/thiết bị (device / 장치) parameters thay đổi.

Ngoài ra variability từ discrete dopants, line-edge roughness và atomic-scale giao diện (interface / 인터페이스) trở nên đáng kể.

Ở nanoscale, “thiết bị (device / 장치) parameter” không còn hoàn toàn là giá trị continuum deterministic; statistical variation trở thành vấn đề kỹ thuật (engineering / 엔지니어링) trực tiếp.

> **Chuyển mạch:** Ở chặng này của **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Quantum tunneling và scaling limit** đã nêu tiêu chí phân biệt, còn **Nhiệt và độ tin cậy (reliability / 신뢰성)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Các giả định (assumptions / 가정들) và giới hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhiệt và độ tin cậy (reliability / 신뢰성)

Power density tạo nhiệt.

Temperature cao có thể thay đổi mobility, leakage, threshold voltage và accelerate degradation mechanisms.

Vì vậy semiconductor physics nối trực tiếp với heat vận chuyển (transport / 전송) và độ tin cậy (reliability / 신뢰성) kỹ thuật (engineering / 엔지니어링).

Một chip không thể được tối ưu chỉ ở electrical mô hình (model / 모델); thermal ranh giới (boundary / 경계) conditions và gói (package / 패키지) cooling cũng quan trọng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Nhiệt và độ tin cậy (reliability / 신뢰성)** đã nêu tiêu chí phân biệt, còn **Các giả định (assumptions / 가정들) và giới hạn** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Các giả định (assumptions / 가정들) và giới hạn

### Drift–diffusion

Drift–diffusion hoạt động tốt khi carrier phân phối (distribution / 분포) gần cục bộ (local / 로컬) equilibrium và length quy mô (scale / 규모) đủ lớn. Ballistic hoặc strongly quantum vận chuyển (transport / 전송) cần mô hình sâu hơn.

### Depletion approximation

Rất hữu ích cho junction lập luận (reasoning / 추론) nhưng không mô tả chính xác mọi carrier phân phối (distribution / 분포) ở junction thật.

### Long-channel MOSFET equations

Các square-law equations mất chính xác trong hiện đại (modern / 현대적) short-channel devices do velocity saturation, mobility degradation, DIBL, quantum confinement và parasitic effects.

### Band picture

Basic semiconductor mô hình (model / 모델) thường dùng effective-mass/single-particle approximations. Strong interactions, disorder hoặc nanostructure có thể cần treatment khác.

> **Chuyển mạch:** Trong **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Các giả định (assumptions / 가정들) và giới hạn** đã nêu tiêu chí phân biệt, còn **Mô hình tư duy (mental model / 사고 모델)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Semiconductor thiết bị (device / 장치) physics có thể nhìn như một chuỗi:

```text
band structure
→ DOS + Fermi statistics
→ carrier concentration
→ electrostatic potential / band bending
→ drift + diffusion
→ junction/channel charge
→ I–V behavior
→ circuit abstraction
```

Lô-gic (logic / 논리) digital `0/1` vì vậy nằm ở cuối một chuỗi physics liên tục, không phải ở đầu chuỗi.

> **Chuyển mạch:** Ở chặng này của **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, **Những ngộ nhận thường gặp (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “N-type mang net điện tích âm lớn”

Không. Bulk vẫn gần trung hòa; N/P nói carrier majority.

### “Built-in voltage của PN junction là một pin miễn phí”

Không. Ở equilibrium không có net power extraction vì electrochemical potential đã cân bằng.

### “Threshold voltage nghĩa dưới `V_T` hiện tại (current / 현재) bằng zero”

Không. Subthreshold conduction vẫn tồn tại.

### “MOSFET saturation giống BJT saturation”

Không. Từ “saturation” được dùng cho hai cơ chế thiết bị (device / 장치) khác nhau.

### “Transistor càng nhỏ thì luôn càng nhanh và ít tốn điện”

Không. Leakage, interconnect, electrostatic điều khiển (control / 제어), thermal density và quantum effects tạo nhiều sự đánh đổi (trade-off / 트레이드오프) mới.

### “Lỗ trống là proton chạy trong silicon”

Sai. Hole là quasiparticle description của trạng thái thiếu electron trong band gần đầy.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Tinh thể và dải năng lượng](00_crystals_bands.md), [Điện tĩnh học](../05_electromagnetism/00_electrostatics.md), [Khuếch tán và vận chuyển](../03_continuum/02_transport_diffusion_heat.md), [Thống kê lượng tử](../08_quantum/05_identical_particles_quantum_statistics.md).

**Liên hệ tiếp:** [Vận chuyển, từ tính và siêu dẫn](02_transport_magnetism_superconductivity.md), [Tín hiệu trên đường truyền](../05_electromagnetism/05_transmission_lines_waveguides.md), [Vật lý tính toán](../12_experimental_computational/02_computational_physics.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
