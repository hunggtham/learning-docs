# Vận chuyển trong chất rắn, hiệu ứng Hall, từ tính và siêu dẫn

Tính chất điện, nhiệt và từ của chất rắn không thể hiểu chỉ bằng cách nhìn từng nguyên tử riêng lẻ. Chúng xuất hiện từ cách rất nhiều electron và dao động mạng tinh thể tổ chức thành các trạng thái tập thể, chịu ràng buộc bởi thống kê lượng tử, cấu trúc dải năng lượng, tán xạ và đối xứng.

Chương này nối bốn lớp vật lý: vận chuyển điện, vận chuyển nhiệt, từ tính và siêu dẫn.

## Từ cấu trúc dải đến vận chuyển

Trong tinh thể, electron không chuyển động như hạt tự do hoàn toàn. Trạng thái Bloch tạo quan hệ phân tán

```math
E_n(\mathbf k).
```

Vận tốc nhóm của wave packet là

```math
\mathbf v_n(\mathbf k)
=\frac{1}{\hbar}\nabla_{\mathbf k}E_n(\mathbf k).
```

Điều này cho thấy khả năng dẫn điện phụ thuộc trực tiếp độ cong của band và các trạng thái gần mức Fermi.

Ở nhiệt độ thấp, phần lớn trạng thái sâu dưới mức Fermi đã bị Pauli blocking; đáp ứng điện chủ yếu đến từ các trạng thái trong một cửa sổ năng lượng cỡ `k_BT` quanh `E_F`.

## Mô hình Drude và ý nghĩa vật lý của thời gian hồi phục

Mô hình Drude giả sử hạt tải được điện trường gia tốc giữa các lần tán xạ. Với electron,

```math
m^*\frac{d\mathbf v}{dt}
=-e\mathbf E-\frac{m^*\mathbf v}{\tau}.
```

Ở trạng thái xác lập,

```math
\mathbf v_d
=-\frac{e\tau}{m^*}\mathbf E.
```

Mật độ dòng là

```math
\mathbf J=-ne\mathbf v_d,
```

nên

```math
\mathbf J=\sigma\mathbf E
```

với

```math
\sigma=\frac{ne^2\tau}{m^*}.
```

`\tau` là thời gian hồi phục động lượng hiệu dụng, không nhất thiết bằng thời gian giữa mọi va chạm vi mô. Các quá trình tán xạ theo góc nhỏ có thể làm đổi quỹ đạo nhưng đóng góp khác nhau vào relaxation của dòng.

## Độ linh động và điện trở suất

Độ linh động

```math
\mu=\frac{e\tau}{m^*}
```

cho

```math
\sigma=ne\mu.
```

Điện trở suất

```math
\rho=\frac{1}{\sigma}.
```

Nếu một vật liệu có carrier density cao nhưng scattering mạnh, conductivity vẫn có thể thấp. Vì vậy “nhiều electron tự do” không đủ để quyết định độ dẫn.

## Phương trình Boltzmann và phân bố ngoài cân bằng

Ở mức sâu hơn, vận chuyển được mô tả bằng distribution function

```math
f(\mathbf r,\mathbf k,t).
```

Phương trình Boltzmann có dạng khái quát

```math
\frac{\partial f}{\partial t}
+\dot{\mathbf r}\cdot\nabla_{\mathbf r}f
+\dot{\mathbf k}\cdot\nabla_{\mathbf k}f
=
\left(\frac{\partial f}{\partial t}\right)_{coll}.
```

Trong relaxation-time approximation,

```math
\left(\frac{\partial f}{\partial t}\right)_{coll}
\approx
-\frac{f-f_0}{\tau}.
```

Điện trường tạo một biến dạng nhỏ của phân bố Fermi–Dirac quanh cân bằng. Dòng điện là moment của phần lệch này trong không gian `k`.

Cách nhìn này giải thích tại sao Drude chỉ là giới hạn đơn giản của một lý thuyết vận chuyển tổng quát hơn.

## Quãng đường tự do trung bình

Nếu hạt tải có vận tốc đặc trưng `v`,

```math
\ell\sim v\tau.
```

Trong kim loại suy biến, vận tốc phù hợp thường gần vận tốc Fermi `v_F`, nên

```math
\ell\sim v_F\tau.
```

Nếu kích thước thiết bị

```math
L\gg\ell,
```

vận chuyển khuếch tán (diffusive transport) thường hợp lý.

Nếu

```math
L\lesssim\ell,
```

vận chuyển đạn đạo (ballistic transport) trở nên quan trọng.

## Từ Ohm sang Landauer

Trong hệ mesoscopic ngắn, thay vì mô tả điện trở bằng scattering liên tục trong bulk, ta có thể nhìn thiết bị như tập các kênh truyền lượng tử.

Công thức Landauer ở nhiệt độ thấp có dạng

```math
G=\frac{2e^2}{h}\sum_n T_n,
```

trong đó `T_n` là xác suất truyền của channel `n`.

Nếu một channel hoàn toàn truyền,

```math
G_0=\frac{2e^2}{h}
```

là quantum of conductance có spin degeneracy 2.

Landauer cho thấy resistance có thể xuất hiện từ contact và transmission probability ngay cả khi vùng giữa gần ballistic.

## Tán xạ electron–phonon và Matthiessen

Các nguồn tán xạ gồm phonon, impurity, defect, boundary và electron–electron processes.

Trong một xấp xỉ đơn giản, các rate cộng gần như

```math
\frac{1}{\tau_{tot}}
\approx
\frac{1}{\tau_1}
+
\frac{1}{\tau_2}
+\cdots.
```

Đây là dạng Matthiessen. Nó hữu ích nhưng không phải định luật tuyệt đối; nếu các cơ chế scattering không độc lập hoặc band structure phức tạp, phép cộng đơn giản có thể thất bại.

## Vận chuyển nhiệt và định luật Wiedemann–Franz

Trong kim loại, electron dẫn mang cả điện tích và năng lượng. Vì vậy conductivity điện `\sigma` và thermal conductivity điện tử `\kappa_e` có quan hệ gần

```math
\frac{\kappa_e}{\sigma T}\approx L_0,
```

với

```math
L_0\approx2.44\times10^{-8}\,W\Omega K^{-2}.
```

Đây là định luật Wiedemann–Franz.

Quan hệ này hoạt động tốt khi cùng quasiparticles và cùng scattering physics kiểm soát cả hai dòng. Gần phase transition hoặc trong strongly correlated materials, deviations có thể chứa thông tin vật lý quan trọng.

## Hiệu ứng nhiệt điện

Gradient nhiệt có thể tạo điện áp:

```math
\Delta V=-S\Delta T,
```

trong đó `S` là hệ số Seebeck.

Ngược lại, dòng điện có thể vận chuyển nhiệt qua hiệu ứng Peltier.

Chất lượng vật liệu nhiệt điện thường đánh giá bằng

```math
ZT=\frac{S^2\sigma T}{\kappa}.
```

Muốn `ZT` lớn cần `S` lớn, `\sigma` cao và `\kappa` thấp. Nhưng các đại lượng này không độc lập, tạo trade-off vật liệu khó tối ưu.

## Hiệu ứng Hall cổ điển

Xét carrier điện tích `q`, mật độ `n`, chuyển động với drift velocity `v_x` trong từ trường `B_z`.

Lực Lorentz tạo lệch ngang:

```math
qE_y+qv_xB_z=0.
```

Suy ra

```math
E_y=-v_xB_z.
```

Vì

```math
J_x=nqv_x,
```

nên Hall coefficient

```math
R_H=\frac{E_y}{J_xB_z}
=\frac{1}{nq}
```

trong mô hình một loại hạt tải.

Dấu của `R_H` cho biết dấu charge hiệu dụng, còn độ lớn cho ước lượng carrier density.

Trong multiband material, công thức đơn giản này có thể sai mạnh vì nhiều carrier types cùng đóng góp.

## Magnetoresistance

Từ trường bẻ quỹ đạo carrier và thay đổi scattering/trajectories, nên điện trở có thể phụ thuộc `B`.

Trong một số vật liệu nhiều lớp từ, giant magnetoresistance (GMR) xuất hiện do spin-dependent scattering. Hiệu ứng này là nền tảng lịch sử quan trọng của đầu đọc ổ cứng và spintronics.

## Từ tính lượng tử

Mômen từ có hai nguồn chính: orbital motion và spin.

Nghịch từ (diamagnetism) phản ứng theo hướng chống lại trường áp dụng. Thuận từ (paramagnetism) có các moments có xu hướng căn theo trường nhưng bị thermal disorder cạnh tranh.

Sắt từ (ferromagnetism) không chỉ là “nhiều dipole cùng hướng”. Exchange interaction lượng tử tạo xu hướng sắp xếp spin, còn anisotropy và domain structure quyết định trạng thái vĩ mô.

## Tương tác trao đổi

Một mô hình tối giản là Heisenberg model:

```math
H=-J\sum_{\langle ij\rangle}\mathbf S_i\cdot\mathbf S_j.
```

Nếu

```math
J>0,
```

mô hình ưu tiên spin song song.

Nếu

```math
J<0,
```

nó ưu tiên phản song song, dẫn đến antiferromagnetic order trong nhiều hệ.

`J` không phải lực từ cổ điển giữa hai nam châm nhỏ; nó phát sinh từ wavefunction overlap, Coulomb interaction và Pauli principle.

## Domain và hysteresis

Một ferromagnet lớn thường chia thành nhiều magnetic domains để giảm tổng free energy.

Khi áp từ trường ngoài, domain walls di chuyển và moments quay. Quá trình có thể không thuận nghịch hoàn toàn, tạo hysteresis loop.

Các đại lượng như coercive field và remanent magnetization quan trọng trong thiết kế vật liệu nhớ từ.

## Mức Landau

Trong từ trường đều, chuyển động orbital vuông góc `B` bị lượng tử hóa:

```math
E_n=\hbar\omega_c\left(n+\frac12\right),
```

với cyclotron frequency

```math
\omega_c=\frac{|q|B}{m^*}.
```

Trong hệ hai chiều ở nhiệt độ thấp, Landau levels tạo nền tảng cho quantum Hall effect.

## Hall lượng tử

Trong integer quantum Hall regime,

```math
\sigma_{xy}=\nu\frac{e^2}{h}
```

với integer filling factor `\nu`.

Giá trị lượng tử hóa có độ chính xác cao và bền với disorder yếu vì liên quan invariant tô pô của band trạng thái chiếm.

Do đó Hall lượng tử là ví dụ mạnh cho việc một observable vĩ mô được bảo vệ bởi topology chứ không chỉ bởi chi tiết vật liệu cục bộ.

## Siêu dẫn: hơn cả điện trở bằng không

Một superconductor dưới critical temperature có hai dấu hiệu cốt lõi:

1. DC resistance bằng không trong giới hạn thích hợp;
2. hiệu ứng Meissner: từ trường bị đẩy khỏi bulk.

Meissner effect phân biệt superconductor với một conductor lý tưởng chỉ có `\rho=0`.

## London penetration depth

Trong mô hình London, từ trường bên trong superconductor suy giảm theo

```math
B(x)\propto e^{-x/\lambda_L},
```

trong đó `\lambda_L` là London penetration depth.

Do đó trường không biến mất ngay tại mặt; nó xuyên vào một lớp mỏng hữu hạn.

## Cooper pair và BCS

Trong conventional superconductors, electron–phonon interaction có thể tạo attraction hiệu dụng giữa hai electron gần Fermi surface.

Hai electron có thể tạo Cooper pair với correlation trên khoảng cách coherence length `\xi` lớn hơn lattice spacing nhiều lần.

BCS ground state là condensate kết hợp của rất nhiều Cooper pairs, không phải khí các phân tử electron tách biệt.

Một energy gap `\Delta` mở quanh Fermi level. Ở weak coupling,

```math
2\Delta(0)\approx3.52k_BT_c.
```

Gap làm low-energy single-particle excitations bị suppress, góp phần tạo dòng không tiêu tán.

## Flux quantization

Order parameter siêu dẫn có pha lượng tử vĩ mô. Điều kiện single-valued phase quanh một vòng kín dẫn đến flux quantization:

```math
\Phi_0=\frac{h}{2e}.
```

`2e` phản ánh charge của Cooper pair.

## Type-I và Type-II

Type-I superconductor có một critical field đặc trưng.

Type-II có hai trường

```math
H_{c1}<H_{c2}.
```

Giữa chúng, magnetic flux xuyên vào dưới dạng vortices lượng tử hóa.

Mỗi vortex mang gần một flux quantum. Nếu vortices chuyển động dưới tác dụng dòng điện, dissipation xuất hiện. Vì vậy vortex pinning quan trọng trong magnet công suất cao.

## Josephson effect

Hai superconductors ngăn cách bởi barrier mỏng có thể tạo Josephson junction.

DC Josephson relation:

```math
I=I_c\sin\phi,
```

trong đó `\phi` là phase difference của hai order parameters.

Khi có voltage `V`, phase tiến hóa theo

```math
\frac{d\phi}{dt}=\frac{2eV}{\hbar}.
```

Do đó tần số Josephson là

```math
f=\frac{2e}{h}V.
```

Quan hệ này tạo liên kết chính xác giữa voltage và frequency và được dùng trong voltage standards.

## SQUID

SQUID dùng Josephson junctions trong loop siêu dẫn. Flux quantization và interference của phase làm critical current cực nhạy với magnetic flux.

Đây là lý do SQUID có thể đo từ trường rất nhỏ trong vật lý vật chất ngưng tụ, biomagnetism và các thí nghiệm precision measurement.

## Liên hệ với qubit siêu dẫn

Một LC circuit cổ điển có phổ harmonic gần đều. Josephson junction cung cấp nonlinear inductance, làm các mức năng lượng không còn cách đều hoàn toàn.

Nhờ anharmonicity này, hai mức thấp nhất có thể được điều khiển như qubit trong khi hạn chế transition sang mức cao hơn.

Đây là cầu nối từ condensed-matter superconductivity sang quantum information engineering.

## Nhiệt và giới hạn vật lý của điện toán

Công suất điện tiêu thụ cuối cùng phần lớn trở thành nhiệt. Ở mô hình nhiệt tập trung đơn giản,

```math
\Delta T=PR_{th}.
```

Ở mô hình liên tục,

```math
\mathbf q=-k\nabla T.
```

Do đó performance computing bị ràng buộc bởi power density, thermal conductivity, packaging và cooling.

Không thể tăng clock rate vô hạn chỉ bằng thiết kế logic nếu heat flux vượt khả năng loại nhiệt.

## Ví dụ: mean free path

Giả sử kim loại có

```math
v_F=1.5\times10^6\,m/s
```

và

```math
\tau=20\,fs.
```

Khi đó

```math
\ell=v_F\tau
=1.5\times10^6\times20\times10^{-15}
\approx30\,nm.
```

Một dây rộng hàng micromet ở regime diffusive rõ ràng hơn, nhưng channel vài chục nanomet bắt đầu cảm nhận boundary/ballistic effects.

## Điều kiện áp dụng và giới hạn mô hình

Drude bỏ qua chi tiết Fermi statistics và band anisotropy. Relaxation-time approximation gom collision physics vào một tham số `\tau`. Landauer phù hợp mesoscopic coherent/elastic transport hơn bulk macroscopic transport.

BCS mô tả conventional superconductors rất thành công nhưng không tự giải thích mọi high-`T_c` material. Heisenberg model là effective model và không thay thế full electronic structure.

Vì vậy mỗi công thức nên được đọc kèm regime của nó.

## Mô hình tư duy (Mental Model)

Vận chuyển trong chất rắn là bài toán **trạng thái lượng tử + lực ngoài + tán xạ + geometry**. Từ tính là **cách spin/orbital moments tổ chức tập thể**. Siêu dẫn là **pha lượng tử vĩ mô có phase coherence**, không chỉ là vật liệu có điện trở nhỏ.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Điện trở chỉ do electron đập vào nguyên tử”

Quá đơn giản. Carrier scattering có thể đến từ phonon, impurity, defect, boundary, electron–electron interaction và band structure.

### “Superconductor chỉ là conductor có `R=0`”

Không. Meissner effect, flux quantization và phase coherence là phần cốt lõi của pha siêu dẫn.

### “Hole hoặc quasiparticle là hạt cơ bản mới”

Không. Chúng là effective excitations xuất hiện trong môi trường vật chất.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Tinh thể và dải năng lượng](00_crystals_bands.md), [Thống kê lượng tử](../08_quantum/05_identical_particles_quantum_statistics.md), [Từ trường và cảm ứng](../05_electromagnetism/03_magnetism_induction.md).

**Liên hệ tiếp:** [Phonon, khuyết tật và vật chất tô pô](04_phonons_defects_topological_matter.md), [BEC và siêu lưu](05_bec_superfluid_quantum_fluids.md), [Pha Berry và Hall lượng tử](06_berry_phase_quantum_hall_topology.md).