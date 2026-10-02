# Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**. Route đi từ Bravais lattice/basis → periodic potential → bands/gaps → Fermi level → lattice vibrations/phonons, để cấu trúc vi mô nối với tính dẫn.

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

> **Chuyển mạch:** Trong **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Basis và crystal cấu trúc (structure / 구조)** tiếp nhận điểm tựa từ **Tinh thể và mạng Bravais** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mạng đảo (reciprocal lattice)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Basis và crystal cấu trúc (structure / 구조)

Mạng không đồng nghĩa với vị trí nguyên tử thực tế. Ta có thể gắn một nhóm nguyên tử, gọi là basis, vào mỗi lattice điểm (point / 지점).

```text
crystal structure = Bravais lattice + basis
```

Ví dụ silicon có cấu trúc diamond, có thể xem như FCC lattice cộng basis hai nguyên tử.

Phân biệt lattice và basis giúp tránh nhầm rằng mọi điểm lặp trong mạng đều tương ứng đúng một nguyên tử.

> **Chuyển mạch:** Ở chặng này của **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Mạng đảo (reciprocal lattice)** tiếp nhận điểm tựa từ **Basis và crystal cấu trúc (structure / 구조)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Diffraction và cấu trúc tinh thể** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mạng đảo (reciprocal lattice)

Nhiều hiện tượng trong tinh thể được mô tả tự nhiên hơn trong không gian véc-tơ (vector / 벡터) sóng `\mathbf k`.

Các vectơ reciprocal thành phần nguyên thủy (primitive / 기본 요소) `\mathbf b_i` được chọn sao cho

```math
\mathbf a_i\cdot\mathbf b_j=2\pi\delta_{ij}.
```

Một reciprocal lattice véc-tơ (vector / 벡터) có dạng

```math
\mathbf G=h\mathbf b_1+k\mathbf b_2+l\mathbf b_3.
```

Reciprocal lattice không phải “một tinh thể khác”. Nó là không gian toán học mã hóa periodicity của lattice thật.

Nó đặc biệt hữu ích cho diffraction vì điều kiện giao thoa xây dựng có thể viết bằng reciprocal vectors.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Diffraction và cấu trúc tinh thể** tiếp nhận điểm tựa từ **Mạng đảo (reciprocal lattice)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Định lý Bloch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Diffraction và cấu trúc tinh thể

Với tia X có bước sóng gần khoảng cách nguyên tử, tinh thể hoạt động như một mạng nhiễu xạ ba chiều.

Dạng Bragg quen thuộc là

```math
2d\sin\theta=n\lambda.
```

Trong reciprocal-space ngôn ngữ (language / 언어), điều kiện scattering đàn hồi có thể liên hệ với một reciprocal véc-tơ (vector / 벡터) `\mathbf G`.

Nhờ diffraction, ta có thể suy ra lattice spacing, symmetry và atomic cấu trúc (structure / 구조) từ dữ liệu intensity trong reciprocal không gian (space / 공간).

Đây là cầu nối trực tiếp giữa wave physics, Fourier transform và crystallography.

> **Chuyển mạch:** Trong **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Định lý Bloch** tiếp nhận điểm tựa từ **Diffraction và cấu trúc tinh thể** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Crystal momentum không hoàn toàn là momentum cơ học** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Crystal momentum không hoàn toàn là momentum cơ học** tiếp nhận điểm tựa từ **Định lý Bloch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Brillouin zone** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Brillouin zone** tiếp nhận điểm tựa từ **Crystal momentum không hoàn toàn là momentum cơ học** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Từ orbital nguyên tử đến dải năng lượng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Brillouin zone

Brillouin zone thứ nhất là Wigner–Seitz cell của reciprocal lattice.

Ta có thể giới hạn `\mathbf k` về vùng này mà không mất thông tin độc lập về band cấu trúc (structure / 구조).

Biên Brillouin zone quan trọng vì tại đó Bragg reflection của electron wave có thể ghép các trạng thái và mở band gap.

Đây là cơ chế toán–vật lý sâu hơn cho câu nói đơn giản “mức nguyên tử tách thành dải”.

> **Chuyển mạch:** Trong **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Từ orbital nguyên tử đến dải năng lượng** tiếp nhận điểm tựa từ **Brillouin zone** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao band gap xuất hiện?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Cách nhìn tight-binding phù hợp khi trạng thái còn mang tính atomic-localized mạnh. Ở phía ngược lại, nearly-free-electron mô hình (model / 모델) bắt đầu từ electron gần tự do rồi xét perturbation tuần hoàn của lattice.

Hai mô hình đi từ hai giới hạn khác nhau nhưng cùng dẫn tới band cấu trúc (structure / 구조).

> **Chuyển mạch:** Ở chặng này của **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Vì sao band gap xuất hiện?** tiếp nhận điểm tựa từ **Từ orbital nguyên tử đến dải năng lượng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Band cấu trúc (structure / 구조) En(k)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao band gap xuất hiện?

Gần ranh giới (boundary / 경계) của Brillouin zone, hai plane-wave trạng thái (state / 상태) có thể bị ghép mạnh bởi periodic potential.

Sự ghép này tách degeneracy thành hai tổ hợp có năng lượng khác nhau, tạo khoảng năng lượng không có eigenstate cho một số `k`.

Đây là nguồn gốc band gap trong picture nearly-free electron.

Vì vậy vùng cấm năng lượng không phải khoảng trống vật lý giữa các nguyên tử. Nó là khoảng trong **phổ năng lượng** không có trạng thái một hạt được phép trong ideal band mô hình (model / 모델).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Band cấu trúc (structure / 구조) En(k)** tiếp nhận điểm tựa từ **Vì sao band gap xuất hiện?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khối lượng hiệu dụng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Band cấu trúc (structure / 구조) `E_n(k)`

Band cấu trúc (structure / 구조) cho quan hệ

```math
E_n(\mathbf k).
```

Từ độ dốc của band, vận tốc nhóm của wavepacket electron là

```math
\mathbf v_n(\mathbf k)
=\frac{1}{\hbar}\nabla_{\mathbf k}E_n(\mathbf k).
```

Do đó carrier velocity không đơn giản là `p/m` với electron tự do; nó phụ thuộc hình dạng band.

Đây là lý do crystal cấu trúc (structure / 구조) có thể thay đổi carrier dynamics mạnh dù electron vẫn có cùng điện tích cơ bản.

> **Chuyển mạch:** Trong **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Khối lượng hiệu dụng** tiếp nhận điểm tựa từ **Band cấu trúc (structure / 구조) En(k)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Density of states** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Density of states** tiếp nhận điểm tựa từ **Khối lượng hiệu dụng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mức Fermi và chemical potential** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Density of states

Density of states (DOS) cho biết số trạng thái khả dụng trên một khoảng năng lượng.

Trong 3D parabolic band, gần band edge có dạng điển hình

```math
g(E)\propto\sqrt{E-E_c}
```

cho conduction band.

DOS cùng Fermi–Dirac phân phối (distribution / 분포) quyết định carrier concentration:

```math
n=\int g_c(E)f(E)\,dE.
```

Do đó chỉ biết band gap chưa đủ để tính carrier density; còn cần DOS và occupancy.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Mức Fermi và chemical potential** tiếp nhận điểm tựa từ **Density of states** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kim loại, bán dẫn và chất cách điện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mức Fermi và chemical potential

Fermi–Dirac phân phối (distribution / 분포) là

```math
f(E)=\frac{1}{e^{(E-\mu)/(k_BT)}+1}.
```

Trong nhiều solid-state ngữ cảnh (context / 맥락), `\mu` được gọi gần như Fermi mức (level / 수준) `E_F`.

Ở `T=0`, các trạng thái dưới chemical potential được lấp đầy và các trạng thái trên nó trống cho ideal noninteracting fermions.

Ở nhiệt độ hữu hạn, biên occupancy được làm mờ trên quy mô (scale / 규모) khoảng `k_BT`.

Fermi mức (level / 수준) không nhất thiết phải trùng với một trạng thái năng lượng (energy / 에너지) thực. Trong semiconductor, nó có thể nằm trong band gap.

> **Chuyển mạch:** Trong **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Kim loại, bán dẫn và chất cách điện** tiếp nhận điểm tựa từ **Mức Fermi và chemical potential** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fermi surface** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kim loại, bán dẫn và chất cách điện

Cách phân loại sâu hơn dựa trên band filling và band gap.

### Kim loại

Có trạng thái trống khả dụng rất gần Fermi mức (level / 수준), nên electric trường dữ liệu (field / 필드) có thể thay đổi occupancy quanh Fermi surface và tạo hiện tại (current / 현재).

### Chất cách điện

Valence band đầy và conduction band cách bởi gap lớn, nên thermal excitation ở điều kiện thường tạo rất ít carriers.

### Bán dẫn

Cũng có band gap, nhưng gap và doping cho phép carrier concentration được điều khiển mạnh bằng nhiệt độ, ánh sáng và impurity.

Sự khác biệt giữa semiconductor và insulator không phải một ranh giới (boundary / 경계) tuyệt đối chỉ dựa vào một con số gap; material ngữ cảnh (context / 맥락) và operating điều kiện (condition / 조건) cũng quan trọng.

> **Chuyển mạch:** Ở chặng này của **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Fermi surface** tiếp nhận điểm tựa từ **Kim loại, bán dẫn và chất cách điện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lỗ trống** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fermi surface

Trong kim loại ở nhiệt độ thấp, các trạng thái occupied trong `k`-space tạo một Fermi sea; ranh giới (boundary / 경계) của vùng occupied là Fermi surface.

Nhiều tính chất low-energy của kim loại được quyết định bởi states gần Fermi surface hơn là toàn bộ electron sâu bên dưới.

Đây là ví dụ của effective-theory thinking: low-temperature vận chuyển (transport / 전송) thường chỉ cần degrees of freedom gần chemical potential.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Lỗ trống** tiếp nhận điểm tựa từ **Fermi surface** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phonon từ dao động mạng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lỗ trống

Trong một band gần đầy, theo dõi mọi electron có thể rất bất tiện.

Một trạng thái thiếu electron có thể được mô tả như một quasiparticle mang điện tích hiệu dụng dương: lỗ trống (hole / 정공).

Hole không phải proton di chuyển trong lattice. Nó là cách biểu diễn collective phản hồi (response / 응답) của nhiều electron trong band gần đầy.

> **Chuyển mạch:** Trong **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Phonon từ dao động mạng** tiếp nhận điểm tựa từ **Lỗ trống** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Acoustic và optical phonon** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phonon từ dao động mạng

Nguyên tử trong crystal không đứng yên tại lattice site. Chúng dao động quanh equilibrium position.

Với displacement nhỏ, potential có thể tuyến tính hóa đến bậc hai, dẫn tới một hệ nhiều oscillator ghép.

Ta diagonalize dynamical ma trận (matrix / 행렬) để tìm normal modes.

Khi lượng tử hóa chế độ (mode / 모드) có frequency `\omega`, năng lượng là

```math
E_n=\hbar\omega\left(n+\frac12\right).
```

Mỗi lượng tử excitation được gọi là phonon.

Phonon là quasiparticle, không phải elementary particle trong vacuum.

> **Chuyển mạch:** Ở chặng này của **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Acoustic và optical phonon** tiếp nhận điểm tựa từ **Phonon từ dao động mạng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phonon và nhiệt dung** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Acoustic và optical phonon

Nếu đơn vị (unit / 단위) cell có nhiều hơn một atom, lattice có thể có nhiều branch phonon.

Acoustic branch có frequency tiến tới zero khi wavelength rất dài và liên hệ với sound wave trong solid.

Optical branch có thể có frequency khác zero gần `k=0` do các atom trong basis dao động tương đối với nhau.

Tên “optical” đến từ khả năng một số chế độ (mode / 모드) tương tác mạnh với electromagnetic radiation trong ionic crystals.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Phonon và nhiệt dung** tiếp nhận điểm tựa từ **Acoustic và optical phonon** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Electron–phonon scattering** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phonon và nhiệt dung

Mô hình Einstein xem các oscillator có cùng frequency; mô hình Debye xem continuum acoustic modes với cutoff.

Ở nhiệt độ thấp, Debye mô hình (model / 모델) dự đoán

```math
C_V\propto T^3.
```

Kết quả này là một thành công quan trọng của quantum statistical physics trong solids.

Classical equipartition chỉ được khôi phục ở nhiệt độ đủ cao so với characteristic phonon năng lượng (energy / 에너지) scales.

> **Chuyển mạch:** Trong **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Electron–phonon scattering** tiếp nhận điểm tựa từ **Phonon và nhiệt dung** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Defect và vì sao crystal thật không hoàn hảo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Electron–phonon scattering

Lattice vibration làm potential mà electron cảm nhận thay đổi theo thời gian.

Điều này tạo electron–phonon scattering, ảnh hưởng electrical resistance và thermal vận chuyển (transport / 전송).

Ở một số vật liệu, electron–phonon coupling còn đóng vai trò trung tâm trong conventional superconductivity.

Vì vậy phonon là cầu nối giữa mechanical vibration, thermodynamics và electronic vận chuyển (transport / 전송).

> **Chuyển mạch:** Ở chặng này của **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Defect và vì sao crystal thật không hoàn hảo** tiếp nhận điểm tựa từ **Electron–phonon scattering** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Direct và indirect band gap** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Trong semiconductor, impurity được dùng có chủ đích để doping. Trong structural material, defect lại có thể quyết định strength và thất bại (failure / 실패).

Do đó “không hoàn hảo” không phải chỉ là nuisance; nhiều thiết bị (device / 장치) hàm (function / 함수) tồn tại nhờ defect được kiểm soát.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Direct và indirect band gap** tiếp nhận điểm tựa từ **Defect và vì sao crystal thật không hoàn hảo** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Các giả định (assumptions / 가정들) và giới hạn của band picture** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Direct và indirect band gap

Band gap còn phụ thuộc vị trí trong `k`-space.

Nếu valence-band maximum và conduction-band minimum ở cùng `k`, ta có direct band gap.

Nếu chúng nằm ở `k` khác nhau, optical chuyển tiếp (transition / 전이) thường cần thêm phonon để bảo toàn crystal momentum.

Đây là lý do material như GaAs phát sáng hiệu quả hơn silicon trong nhiều LED applications.

> **Chuyển mạch:** Trong **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Direct và indirect band gap** đã nêu tiêu chí phân biệt, còn **Các giả định (assumptions / 가정들) và giới hạn của band picture** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Các giả định (assumptions / 가정들) và giới hạn của band picture

Basic band lý thuyết (theory / 이론) thường bắt đầu từ effective one-electron picture.

Nó hoạt động rất tốt cho nhiều semiconductor và weakly correlated materials, nhưng có thể thất bại khi electron–electron tương tác (interaction / 상호작용) mạnh.

Các hệ strongly correlated có thể cần Hubbard mô hình (model / 모델), many-body methods hoặc các quasiparticle description sâu hơn.

Crystal periodicity cũng bị phá tại surface, giao diện (interface / 인터페이스), defect và disorder.

Vì vậy band cấu trúc (structure / 구조) là baseline mạnh, không phải lời giải hoàn chỉnh cho mọi solid.

> **Chuyển mạch:** Ở chặng này của **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Các giả định (assumptions / 가정들) và giới hạn của band picture** đã nêu tiêu chí phân biệt, còn **Mô hình tư duy (mental model / 사고 모델)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

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

Hai chuỗi gặp nhau qua electron–phonon tương tác (interaction / 상호작용) và tạo phần lớn physics của material thật.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, **Những ngộ nhận thường gặp (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Band gap là khoảng trống giữa các nguyên tử”

Sai. Nó là khoảng năng lượng không có single-particle trạng thái (state / 상태) được phép trong ideal band description.

### “Electron trong kim loại là hoàn toàn tự do”

Không. Free-electron mô hình (model / 모델) là xấp xỉ; lattice periodicity và tương tác (interaction / 상호작용) thay đổi dispersion thành band cấu trúc (structure / 구조).

### “Effective mass nghĩa electron thật nặng hoặc nhẹ đi”

Không. Nó mô tả curvature của band và động (dynamic / 동적) phản hồi (response / 응답) của quasiparticle.

### “Phonon là atom bay qua crystal”

Không. Phonon là lượng tử của collective lattice vibration.

### “Crystal hoàn hảo mới hữu ích cho electronics”

Không. Doping, giao diện (interface / 인터페이스) và defect được kiểm soát là nền tảng của semiconductor technology.

> **Chuyển mạch:** Trong **Vật lý chất rắn: mạng tinh thể, dải năng lượng, mức Fermi và phonon**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Normal modes](../02_oscillations_waves/02_coupled_oscillators_normal_modes.md), [Hạt đồng nhất và thống kê lượng tử](../08_quantum/05_identical_particles_quantum_statistics.md), [Vật lý nguyên tử](../09_atomic_nuclear_particle/00_atomic_physics.md).

**Liên hệ tiếp:** [Bán dẫn và thiết bị](01_semiconductors_devices.md), [Vận chuyển, từ tính và siêu dẫn](02_transport_magnetism_superconductivity.md), [Phonon, defect và vật chất tô pô](04_phonons_defects_topological_matter.md), [Berry phase và Quantum Hall](06_berry_phase_quantum_hall_topology.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
