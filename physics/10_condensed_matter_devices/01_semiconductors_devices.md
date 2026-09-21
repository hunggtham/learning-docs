# Bán dẫn và thiết bị: pha tạp, tiếp giáp P–N, diode, MOSFET và CMOS

Bán dẫn là nơi nhiều lớp vật lý gặp nhau trực tiếp: cơ học lượng tử quyết định dải năng lượng; cơ học thống kê quyết định số trạng thái được chiếm; điện từ học quyết định thế và điện trường; khuếch tán quyết định chuyển động do gradient nồng độ; còn hình học thiết bị biến các cơ chế đó thành diode, transistor, LED và pin mặt trời.

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

Gradient concentration tạo diffusion. Với electron, một convention thường dùng là

```math
\mathbf J_{n,diff}=qD_n\nabla n.
```

Tổng dòng:

```math
\mathbf J_n
=qn\mu_n\mathbf E+qD_n\nabla n.
```

Với hole, dấu của diffusion term phụ thuộc cách viết carrier flux/current convention.

Trong miền không suy biến, Einstein relation là

```math
D=\mu\frac{k_BT}{q}.
```

Nó cho thấy drift và diffusion không phải hai cơ chế thống kê hoàn toàn độc lập; cả hai bắt nguồn từ transport của carrier trong môi trường nhiệt.

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

Ở field cao, carrier velocity có thể tiến tới saturation thay vì tiếp tục tăng tuyến tính với `E`.

## Tiếp giáp P–N hình thành như thế nào?

Ngay sau khi ghép P và N, concentration gradient rất lớn.

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

Charge separation tạo electric field hướng từ N sang P. Field này tạo drift chống lại diffusion.

Ở thermal equilibrium:

```text
diffusion current + drift current = 0
```

nhưng từng thành phần riêng không nhất thiết bằng zero.

## Band bending và electrostatic potential

Electron energy thay đổi theo electrostatic potential `\phi` gần như

```math
E_{electron}\sim -q\phi.
```

Vì `\phi(x)` thay đổi trong depletion region, conduction-band edge và valence-band edge cũng thay đổi theo vị trí trên band diagram.

Hiện tượng này được gọi là **uốn cong dải năng lượng (band bending)**.

Band diagram vì vậy là cách biểu diễn electrostatic potential bằng energy coordinates.

Ở equilibrium, Fermi level phải phẳng xuyên qua junction. Nếu `E_F` thay đổi theo vị trí ở một hệ cân bằng, carrier sẽ có xu hướng tái phân bố.

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

Nó không phải “pin ẩn” có thể lấy điện liên tục ra ngoài. Ở equilibrium, electrochemical potentials của toàn cấu trúc đã cân bằng nên không có net DC power output.

## Depletion approximation

Một approximation rất hữu ích giả sử depletion region gần như không có mobile carriers; charge density chủ yếu do ionized dopants cố định.

Poisson equation là

```math
\frac{d^2\phi}{dx^2}
=-\frac{\rho(x)}{\varepsilon_s}.
```

Với abrupt junction, `\rho` gần piecewise constant trong depletion region, nên electric field gần piecewise linear và potential gần quadratic.

Tổng depletion width dưới bias `V` có dạng xấp xỉ

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

Khi reverse bias tăng, `V` âm theo convention forward-bias-positive, nên `W` tăng.

Junction capacitance do đó phụ thuộc điện áp.

## Phân cực thuận và phân cực ngược

### Forward bias

External voltage giảm effective barrier. Minority-carrier injection tăng mạnh, dẫn tới current lớn hơn.

### Reverse bias

Barrier tăng và depletion region rộng hơn. Dòng thường nhỏ cho đến breakdown.

Hai cơ chế breakdown chính là:

```text
Zener tunneling
avalanche multiplication
```

Cơ chế trội phụ thuộc doping và field scale.

## Phương trình diode

Trong mô hình lý tưởng hóa,

```math
I=I_S
\left(
 e^{qV/(nk_BT)}-1
\right).
```

Dạng hàm mũ xuất hiện từ carrier statistics và minority-carrier diffusion, không phải từ một quy tắc mạch tùy ý.

Các assumption thường gồm:

```text
low-level injection
quasi-neutral regions
steady state
uniform temperature
idealized recombination
negligible series resistance
```

Ở current lớn, series resistance; ở voltage thấp hoặc defect-rich junction, recombination; và ở reverse breakdown, các cơ chế khác làm phương trình đơn giản không còn đúng.

## LED: band gap và photon

Trong direct-band-gap material, electron và hole có thể tái hợp radiatively với

```math
E_{photon}\approx E_g.
```

Do

```math
\lambda\approx\frac{hc}{E_g},
```

band gap quyết định scale của emission wavelength.

Trong indirect-gap material như silicon, transition thường cần phonon để hỗ trợ crystal-momentum conservation, nên light emission kém hiệu quả hơn.

## Photodiode và pin mặt trời

Photon với

```math
hf\gtrsim E_g
```

có thể tạo electron–hole pair.

Built-in field trong junction giúp tách carrier trước khi chúng tái hợp.

Photodiode tối ưu signal detection; solar cell tối ưu energy extraction. Hai device dùng cùng physics nhưng mục tiêu engineering khác nhau.

Loss channels của solar cell gồm:

```text
sub-gap photons
thermalization của photon dư năng lượng
recombination
optical reflection
series/shunt losses
```

## Từ tiếp giáp P–N đến MOS capacitor

MOSFET được hiểu rõ nhất nếu trước tiên xem cấu trúc **MOS capacitor**:

```text
metal/gate
→ oxide
→ semiconductor
```

Oxide ngăn DC conduction lý tưởng nhưng cho electric field xuyên qua.

Gate voltage làm thay đổi surface potential trong semiconductor và do đó làm band edges cong gần interface.

Đây là bản chất electrostatic của field-effect control.

## Accumulation, depletion và inversion

Xét nền P-type.

### Accumulation

Gate voltage đủ âm hút hole về bề mặt:

```text
hole concentration tại surface tăng
```

### Depletion

Gate voltage dương đẩy hole khỏi interface, để lại ion acceptor cố định:

```text
surface mobile carrier giảm
```

### Inversion

Tăng gate voltage dương thêm làm band bending đủ mạnh để electron trở thành carrier chiếm ưu thế ngay tại bề mặt, dù bulk vẫn P-type.

Ta đã tạo một **inversion layer** N-like ngay dưới oxide.

Đó chính là nền của kênh nMOS.

## Oxide capacitance

Với oxide dày `t_{ox}` và permittivity `\varepsilon_{ox}`, capacitance trên một đơn vị diện tích là

```math
C_{ox}'=\frac{\varepsilon_{ox}}{t_{ox}}.
```

Oxide mỏng hơn tăng gate control vì capacitance lớn hơn, nhưng quá mỏng làm tunneling leakage tăng.

High-k dielectric cho phép tăng effective capacitance mà không cần physical thickness nhỏ đến mức tunneling quá mạnh.

Đây là ví dụ trực tiếp của trade-off giữa electrostatics và quantum tunneling.

## Điện áp ngưỡng

Threshold voltage `V_T` không phải một “công tắc kỳ diệu” nơi transistor đột ngột đổi từ zero current sang full current.

Nó là một convention hữu ích đánh dấu regime hình thành strong inversion/channel theo model.

`V_T` phụ thuộc vào:

```text
work-function difference
oxide capacitance
substrate doping
fixed/interface charge
body bias
temperature
```

Vì vậy threshold là property của cả cấu trúc, không chỉ của material bulk.

## MOSFET channel và drain bias

Khi gate tạo inversion channel, source và drain nối carrier vào hai đầu channel.

Drain voltage tạo lateral electric field làm carrier drift.

Trong long-channel gradual-channel approximation, current có thể được suy ra bằng cách tích phân local channel charge và drift velocity.

Ở vùng linear, dạng gần đúng quen thuộc là

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

channel gần drain bị pinch-off trong ideal long-channel picture và current đi vào saturation regime.

Dạng textbook saturation gần đúng:

```math
I_{D,sat}
\approx
\frac12
\mu C_{ox}'\frac{W}{L}
(V_{GS}-V_T)^2.
```

Các công thức này không phải law phổ quát; chúng dựa trên long-channel, mobility gần constant và quasi-static assumptions.

## Subthreshold conduction

Ngay dưới threshold, current không bằng zero. Carrier concentration tại surface thay đổi gần exponential với gate voltage, tạo subthreshold current.

Subthreshold swing được đo bằng số millivolt gate voltage cần để current thay đổi một decade.

Ở room temperature, MOSFET conventional có thermodynamic lower-bound lý tưởng khoảng

```math
60\;mV/decade
```

trong điều kiện thích hợp.

Kết quả này liên hệ trực tiếp với Boltzmann statistics và là một giới hạn quan trọng của low-voltage logic.

## Short-channel effects

Khi channel length giảm, source/drain electrostatic fields bắt đầu cạnh tranh với gate trong việc điều khiển potential barrier.

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

Đây là lý do device scaling không thể hiểu chỉ bằng việc “thu nhỏ hình học”. Electrostatic length scales phải giảm tương ứng.

## FinFET và gate-all-around

Planar gate chỉ điều khiển channel chủ yếu từ một mặt.

FinFET bao quanh channel nhiều mặt hơn; gate-all-around tiếp tục tăng electrostatic control.

Các kiến trúc này không thay đổi nguyên lý transistor cơ bản. Chúng thay đổi geometry để gate field kiểm soát channel tốt hơn so với source/drain fields.

## CMOS

CMOS dùng nMOS và pMOS bổ sung.

Trong ideal static state, một nhánh gần off nên direct DC path từ supply xuống ground rất nhỏ.

Dynamic energy dùng để nạp/xả capacitance:

```math
E_{switch}\sim CV^2.
```

Với activity factor `\alpha`:

```math
P_{dynamic}\approx\alpha CV^2f.
```

Do phụ thuộc `V^2`, giảm supply voltage tiết kiệm energy rất mạnh. Nhưng voltage thấp làm giảm noise margin và drive current, nên xuất hiện trade-off power–performance–reliability.

## RC delay và interconnect

Gate và wiring tạo capacitance; conductor có resistance.

Một time scale đơn giản là

```math
\tau\sim RC.
```

Khi transistor nhỏ dần, interconnect delay, parasitic capacitance, coupling, inductance và signal integrity có thể chi phối performance.

Vì vậy CPU speed không được quyết định chỉ bởi transistor switching time.

## Quantum tunneling và scaling limit

Oxide quá mỏng cho gate leakage qua tunneling.

Channel cực ngắn có thể xuất hiện source-to-drain tunneling và quantum confinement làm band/device parameters thay đổi.

Ngoài ra variability từ discrete dopants, line-edge roughness và atomic-scale interface trở nên đáng kể.

Ở nanoscale, “device parameter” không còn hoàn toàn là giá trị continuum deterministic; statistical variation trở thành vấn đề engineering trực tiếp.

## Nhiệt và reliability

Power density tạo nhiệt.

Temperature cao có thể thay đổi mobility, leakage, threshold voltage và accelerate degradation mechanisms.

Vì vậy semiconductor physics nối trực tiếp với heat transport và reliability engineering.

Một chip không thể được tối ưu chỉ ở electrical model; thermal boundary conditions và package cooling cũng quan trọng.

## Assumptions và giới hạn

### Drift–diffusion

Drift–diffusion hoạt động tốt khi carrier distribution gần local equilibrium và length scale đủ lớn. Ballistic hoặc strongly quantum transport cần mô hình sâu hơn.

### Depletion approximation

Rất hữu ích cho junction reasoning nhưng không mô tả chính xác mọi carrier distribution ở junction thật.

### Long-channel MOSFET equations

Các square-law equations mất chính xác trong modern short-channel devices do velocity saturation, mobility degradation, DIBL, quantum confinement và parasitic effects.

### Band picture

Basic semiconductor model thường dùng effective-mass/single-particle approximations. Strong interactions, disorder hoặc nanostructure có thể cần treatment khác.

## Mô hình tư duy (Mental Model)

Semiconductor device physics có thể nhìn như một chuỗi:

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

Logic digital `0/1` vì vậy nằm ở cuối một chuỗi physics liên tục, không phải ở đầu chuỗi.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “N-type mang net điện tích âm lớn”

Không. Bulk vẫn gần trung hòa; N/P nói carrier majority.

### “Built-in voltage của PN junction là một pin miễn phí”

Không. Ở equilibrium không có net power extraction vì electrochemical potential đã cân bằng.

### “Threshold voltage nghĩa dưới `V_T` current bằng zero”

Không. Subthreshold conduction vẫn tồn tại.

### “MOSFET saturation giống BJT saturation”

Không. Từ “saturation” được dùng cho hai cơ chế device khác nhau.

### “Transistor càng nhỏ thì luôn càng nhanh và ít tốn điện”

Không. Leakage, interconnect, electrostatic control, thermal density và quantum effects tạo nhiều trade-off mới.

### “Lỗ trống là proton chạy trong silicon”

Sai. Hole là quasiparticle description của trạng thái thiếu electron trong band gần đầy.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Tinh thể và dải năng lượng](00_crystals_bands.md), [Điện tĩnh học](../05_electromagnetism/00_electrostatics.md), [Khuếch tán và vận chuyển](../03_continuum/02_transport_diffusion_heat.md), [Thống kê lượng tử](../08_quantum/05_identical_particles_quantum_statistics.md).

**Liên hệ tiếp:** [Vận chuyển, từ tính và siêu dẫn](02_transport_magnetism_superconductivity.md), [Tín hiệu trên đường truyền](../05_electromagnetism/05_transmission_lines_waveguides.md), [Vật lý tính toán](../12_experimental_computational/02_computational_physics.md).
