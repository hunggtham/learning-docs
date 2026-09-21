# Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon

Một cục silicon có thể trở thành transistor không phải vì từng nguyên tử silicon riêng lẻ “biết” cách đóng cắt dòng điện. Tính chất điện tử của vật liệu xuất hiện từ **cấu trúc tập thể của rất nhiều nguyên tử và electron** trong một thế tuần hoàn.

Đây là một trong những ví dụ rõ nhất của hiện tượng nổi lên (emergence):

```text
nguyên tử riêng lẻ
→ orbital nguyên tử
→ tinh thể tuần hoàn
→ trạng thái Bloch
→ dải năng lượng
→ carrier dynamics
→ tính chất điện, nhiệt và quang của vật liệu
```

## Tinh thể và mạng Bravais

Một tinh thể lý tưởng có tính tuần hoàn theo không gian. Nếu `\mathbf R` là một vectơ mạng, cấu trúc thỏa

```math
V(\mathbf r+\mathbf R)=V(\mathbf r).
```

Một mạng Bravais (Bravais lattice / 브라베 격자) được sinh bởi ba vectơ cơ sở

```math
\mathbf a_1,\mathbf a_2,\mathbf a_3,
```

sao cho mọi điểm mạng có dạng

```math
\mathbf R=n_1\mathbf a_1+n_2\mathbf a_2+n_3\mathbf a_3,
```

với `n_i` là số nguyên.

Một **ô nguyên thủy (primitive cell)** chứa đúng một điểm mạng về mặt counting. Một **ô quy ước (conventional cell)** có thể lớn hơn nhưng làm symmetry dễ nhìn hơn.

Tinh thể thật luôn có defect, thermal vibration và bề mặt. Periodic lattice là mô hình nền để tách phần cấu trúc lý tưởng khỏi các hiệu ứng đó.

## Basis và crystal structure

Mạng không đồng nghĩa với vị trí nguyên tử thực tế. Ta có thể gắn một nhóm nguyên tử, gọi là basis, vào mỗi lattice point.

```text
crystal structure = Bravais lattice + basis
```

Ví dụ silicon có cấu trúc diamond, có thể xem như FCC lattice cộng basis hai nguyên tử.

Phân biệt lattice và basis giúp tránh nhầm rằng mọi điểm lặp trong mạng đều tương ứng đúng một nguyên tử.

## Mạng đảo (reciprocal lattice)

Nhiều hiện tượng trong tinh thể được mô tả tự nhiên hơn trong không gian vector sóng `\mathbf k`.

Các vectơ reciprocal primitive `\mathbf b_i` được chọn sao cho

```math
\mathbf a_i\cdot\mathbf b_j=2\pi\delta_{ij}.
```

Một reciprocal lattice vector có dạng

```math
\mathbf G=h\mathbf b_1+k\mathbf b_2+l\mathbf b_3.
```

Reciprocal lattice không phải “một tinh thể khác”. Nó là không gian toán học mã hóa periodicity của lattice thật.

Nó đặc biệt hữu ích cho diffraction vì điều kiện giao thoa xây dựng có thể viết bằng reciprocal vectors.

## Diffraction và cấu trúc tinh thể

Với tia X có bước sóng gần khoảng cách nguyên tử, tinh thể hoạt động như một mạng nhiễu xạ ba chiều.

Dạng Bragg quen thuộc là

```math
2d\sin\theta=n\lambda.
```

Trong reciprocal-space language, điều kiện scattering đàn hồi có thể liên hệ với một reciprocal vector `\mathbf G`.

Nhờ diffraction, ta có thể suy ra lattice spacing, symmetry và atomic structure từ dữ liệu intensity trong reciprocal space.

Đây là cầu nối trực tiếp giữa wave physics, Fourier transform và crystallography.

## Định lý Bloch

Electron trong thế tuần hoàn không có wavefunction giống một plane wave tự do đơn giản. Định lý Bloch cho biết eigenstate có thể viết

```math
\psi_{n\mathbf k}(\mathbf r)
=u_{n\mathbf k}(\mathbf r)e^{i\mathbf k\cdot\mathbf r},
```

trong đó

```math
u_{n\mathbf k}(\mathbf r+\mathbf R)
=u_{n\mathbf k}(\mathbf r).
```

`n` là chỉ số band, còn `\mathbf k` đóng vai trò quantum number liên hệ với crystal momentum.

Bloch theorem là kết quả của translational symmetry rời rạc của crystal lattice.

## Crystal momentum không hoàn toàn là momentum cơ học

Trong lattice, `\hbar\mathbf k` thường được gọi là crystal momentum.

Nó rất hữu ích trong conservation rules của scattering trong tinh thể, nhưng không nên đồng nhất máy móc với mechanical momentum của free particle.

Vì reciprocal lattice có periodicity,

```math
\mathbf k
```

và

```math
\mathbf k+\mathbf G
```

có thể mô tả trạng thái tương đương theo symmetry của lattice.

Điều này dẫn tự nhiên tới Brillouin zone.

## Brillouin zone

Brillouin zone thứ nhất là Wigner–Seitz cell của reciprocal lattice.

Ta có thể giới hạn `\mathbf k` về vùng này mà không mất thông tin độc lập về band structure.

Biên Brillouin zone quan trọng vì tại đó Bragg reflection của electron wave có thể ghép các trạng thái và mở band gap.

Đây là cơ chế toán–vật lý sâu hơn cho câu nói đơn giản “mức nguyên tử tách thành dải”.

## Từ orbital nguyên tử đến dải năng lượng

Xét `N` nguyên tử giống nhau, mỗi nguyên tử có một orbital với năng lượng gần `E_0`.

Khi các nguyên tử ở xa nhau, các trạng thái gần suy biến.

Khi đưa lại gần:

```text
wavefunction chồng lấp
+ interaction
+ Pauli exclusion
→ degeneracy bị tách
```

Một mức nguyên tử có thể tách thành khoảng `N` trạng thái rất gần nhau.

Với `N` vĩ mô, các mức trở thành một dải gần liên tục.

Cách nhìn tight-binding phù hợp khi trạng thái còn mang tính atomic-localized mạnh. Ở phía ngược lại, nearly-free-electron model bắt đầu từ electron gần tự do rồi xét perturbation tuần hoàn của lattice.

Hai mô hình đi từ hai giới hạn khác nhau nhưng cùng dẫn tới band structure.

## Vì sao band gap xuất hiện?

Gần boundary của Brillouin zone, hai plane-wave state có thể bị ghép mạnh bởi periodic potential.

Sự ghép này tách degeneracy thành hai tổ hợp có năng lượng khác nhau, tạo khoảng năng lượng không có eigenstate cho một số `k`.

Đây là nguồn gốc band gap trong picture nearly-free electron.

Vì vậy vùng cấm năng lượng không phải khoảng trống vật lý giữa các nguyên tử. Nó là khoảng trong **phổ năng lượng** không có trạng thái một hạt được phép trong ideal band model.

## Band structure `E_n(k)`

Band structure cho quan hệ

```math
E_n(\mathbf k).
```

Từ độ dốc của band, vận tốc nhóm của wavepacket electron là

```math
\mathbf v_n(\mathbf k)
=\frac{1}{\hbar}\nabla_{\mathbf k}E_n(\mathbf k).
```

Do đó carrier velocity không đơn giản là `p/m` với electron tự do; nó phụ thuộc hình dạng band.

Đây là lý do crystal structure có thể thay đổi carrier dynamics mạnh dù electron vẫn có cùng điện tích cơ bản.

## Khối lượng hiệu dụng

Gần một extremum của band, ta có thể khai triển

```math
E(k)\approx E_0
+\frac{\hbar^2}{2m^*}(k-k_0)^2.
```

Trong một chiều,

```math
\frac{1}{m^*}
=\frac{1}{\hbar^2}
\frac{d^2E}{dk^2}.
```

`m^*` là khối lượng hiệu dụng (effective mass / 유효질량).

Nó không có nghĩa electron cơ bản thay đổi rest mass. Đây là tham số mô tả phản ứng động lực học của wavepacket trong periodic band.

Trong crystal anisotropic, effective mass có thể là tensor.

## Density of states

Density of states (DOS) cho biết số trạng thái khả dụng trên một khoảng năng lượng.

Trong 3D parabolic band, gần band edge có dạng điển hình

```math
g(E)\propto\sqrt{E-E_c}
```

cho conduction band.

DOS cùng Fermi–Dirac distribution quyết định carrier concentration:

```math
n=\int g_c(E)f(E)\,dE.
```

Do đó chỉ biết band gap chưa đủ để tính carrier density; còn cần DOS và occupancy.

## Mức Fermi và chemical potential

Fermi–Dirac distribution là

```math
f(E)=\frac{1}{e^{(E-\mu)/(k_BT)}+1}.
```

Trong nhiều solid-state context, `\mu` được gọi gần như Fermi level `E_F`.

Ở `T=0`, các trạng thái dưới chemical potential được lấp đầy và các trạng thái trên nó trống cho ideal noninteracting fermions.

Ở nhiệt độ hữu hạn, biên occupancy được làm mờ trên scale khoảng `k_BT`.

Fermi level không nhất thiết phải trùng với một trạng thái energy thực. Trong semiconductor, nó có thể nằm trong band gap.

## Kim loại, bán dẫn và chất cách điện

Cách phân loại sâu hơn dựa trên band filling và band gap.

### Kim loại

Có trạng thái trống khả dụng rất gần Fermi level, nên electric field có thể thay đổi occupancy quanh Fermi surface và tạo current.

### Chất cách điện

Valence band đầy và conduction band cách bởi gap lớn, nên thermal excitation ở điều kiện thường tạo rất ít carriers.

### Bán dẫn

Cũng có band gap, nhưng gap và doping cho phép carrier concentration được điều khiển mạnh bằng nhiệt độ, ánh sáng và impurity.

Sự khác biệt giữa semiconductor và insulator không phải một boundary tuyệt đối chỉ dựa vào một con số gap; material context và operating condition cũng quan trọng.

## Fermi surface

Trong kim loại ở nhiệt độ thấp, các trạng thái occupied trong `k`-space tạo một Fermi sea; boundary của vùng occupied là Fermi surface.

Nhiều tính chất low-energy của kim loại được quyết định bởi states gần Fermi surface hơn là toàn bộ electron sâu bên dưới.

Đây là ví dụ của effective-theory thinking: low-temperature transport thường chỉ cần degrees of freedom gần chemical potential.

## Lỗ trống

Trong một band gần đầy, theo dõi mọi electron có thể rất bất tiện.

Một trạng thái thiếu electron có thể được mô tả như một quasiparticle mang điện tích hiệu dụng dương: lỗ trống (hole / 정공).

Hole không phải proton di chuyển trong lattice. Nó là cách biểu diễn collective response của nhiều electron trong band gần đầy.

## Phonon từ dao động mạng

Nguyên tử trong crystal không đứng yên tại lattice site. Chúng dao động quanh equilibrium position.

Với displacement nhỏ, potential có thể tuyến tính hóa đến bậc hai, dẫn tới một hệ nhiều oscillator ghép.

Ta diagonalize dynamical matrix để tìm normal modes.

Khi lượng tử hóa mode có frequency `\omega`, năng lượng là

```math
E_n=\hbar\omega\left(n+\frac12\right).
```

Mỗi lượng tử excitation được gọi là phonon.

Phonon là quasiparticle, không phải elementary particle trong vacuum.

## Acoustic và optical phonon

Nếu unit cell có nhiều hơn một atom, lattice có thể có nhiều branch phonon.

Acoustic branch có frequency tiến tới zero khi wavelength rất dài và liên hệ với sound wave trong solid.

Optical branch có thể có frequency khác zero gần `k=0` do các atom trong basis dao động tương đối với nhau.

Tên “optical” đến từ khả năng một số mode tương tác mạnh với electromagnetic radiation trong ionic crystals.

## Phonon và nhiệt dung

Mô hình Einstein xem các oscillator có cùng frequency; mô hình Debye xem continuum acoustic modes với cutoff.

Ở nhiệt độ thấp, Debye model dự đoán

```math
C_V\propto T^3.
```

Kết quả này là một thành công quan trọng của quantum statistical physics trong solids.

Classical equipartition chỉ được khôi phục ở nhiệt độ đủ cao so với characteristic phonon energy scales.

## Electron–phonon scattering

Lattice vibration làm potential mà electron cảm nhận thay đổi theo thời gian.

Điều này tạo electron–phonon scattering, ảnh hưởng electrical resistance và thermal transport.

Ở một số vật liệu, electron–phonon coupling còn đóng vai trò trung tâm trong conventional superconductivity.

Vì vậy phonon là cầu nối giữa mechanical vibration, thermodynamics và electronic transport.

## Defect và vì sao crystal thật không hoàn hảo

Crystal thật có thể có:

```text
vacancy
interstitial
substitutional impurity
dislocation
grain boundary
surface/interface
```

Defect có thể scattering electron/phonon, pin dislocation, thay đổi diffusion và tạo localized electronic states.

Trong semiconductor, impurity được dùng có chủ đích để doping. Trong structural material, defect lại có thể quyết định strength và failure.

Do đó “không hoàn hảo” không phải chỉ là nuisance; nhiều device function tồn tại nhờ defect được kiểm soát.

## Direct và indirect band gap

Band gap còn phụ thuộc vị trí trong `k`-space.

Nếu valence-band maximum và conduction-band minimum ở cùng `k`, ta có direct band gap.

Nếu chúng nằm ở `k` khác nhau, optical transition thường cần thêm phonon để bảo toàn crystal momentum.

Đây là lý do material như GaAs phát sáng hiệu quả hơn silicon trong nhiều LED applications.

## Assumptions và giới hạn của band picture

Basic band theory thường bắt đầu từ effective one-electron picture.

Nó hoạt động rất tốt cho nhiều semiconductor và weakly correlated materials, nhưng có thể thất bại khi electron–electron interaction mạnh.

Các hệ strongly correlated có thể cần Hubbard model, many-body methods hoặc các quasiparticle description sâu hơn.

Crystal periodicity cũng bị phá tại surface, interface, defect và disorder.

Vì vậy band structure là baseline mạnh, không phải lời giải hoàn chỉnh cho mọi solid.

## Mô hình tư duy (Mental Model)

Solid-state physics có thể nhìn theo chuỗi:

```text
periodic geometry
→ reciprocal space
→ Bloch states
→ E(k)
→ DOS + Fermi occupation
→ carrier dynamics
→ transport/optics/device behavior
```

Đồng thời lattice motion tạo chuỗi khác:

```text
coupled atomic oscillations
→ normal modes
→ phonons
→ heat capacity + thermal transport + scattering
```

Hai chuỗi gặp nhau qua electron–phonon interaction và tạo phần lớn physics của material thật.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Band gap là khoảng trống giữa các nguyên tử”

Sai. Nó là khoảng năng lượng không có single-particle state được phép trong ideal band description.

### “Electron trong kim loại là hoàn toàn tự do”

Không. Free-electron model là xấp xỉ; lattice periodicity và interaction thay đổi dispersion thành band structure.

### “Effective mass nghĩa electron thật nặng hoặc nhẹ đi”

Không. Nó mô tả curvature của band và dynamic response của quasiparticle.

### “Phonon là atom bay qua crystal”

Không. Phonon là lượng tử của collective lattice vibration.

### “Crystal hoàn hảo mới hữu ích cho electronics”

Không. Doping, interface và defect được kiểm soát là nền tảng của semiconductor technology.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Normal modes](../02_oscillations_waves/02_coupled_oscillators_normal_modes.md), [Hạt đồng nhất và thống kê lượng tử](../08_quantum/05_identical_particles_quantum_statistics.md), [Vật lý nguyên tử](../09_atomic_nuclear_particle/00_atomic_physics.md).

**Liên hệ tiếp:** [Bán dẫn và thiết bị](01_semiconductors_devices.md), [Vận chuyển, từ tính và siêu dẫn](02_transport_magnetism_superconductivity.md), [Phonon, defect và vật chất tô pô](04_phonons_defects_topological_matter.md), [Berry phase và Quantum Hall](06_berry_phase_quantum_hall_topology.md).
