# Lý thuyết obitan phân tử — nhìn electron như trạng thái của toàn phân tử

> **Lý thuyết obitan phân tử (molecular orbital theory, MO / 분자 오비탈 이론)** mô tả electron bằng các obitan có thể trải trên toàn bộ phân tử thay vì mặc định gán mỗi cặp electron cho một liên kết cục bộ. MO theory đặc biệt mạnh khi cần hiểu **sự phi định xứ, bậc liên kết, từ tính, màu, kích thích electron, quang hóa và sự hình thành dải năng lượng trong chất rắn**.

Lewis và valence-bond language rất hữu ích cho connectivity và local reactivity. MO theory trả lời một lớp câu hỏi khác: nếu toàn bộ electron chịu trường của nhiều nuclei cùng lúc, các trạng thái lượng tử của cả hệ trông như thế nào?

# Tổ hợp tuyến tính của obitan nguyên tử

Trong cách tiếp cận **LCAO — tổ hợp tuyến tính obitan nguyên tử (Linear Combination of Atomic Orbitals)**, molecular orbital được viết khái niệm:

\[
\psi_{MO}=\sum_i c_i\phi_i
\]

trong đó \(\phi_i\) là atomic basis functions còn \(c_i\) là coefficients.

Các coefficients không chỉ nói orbital “đến từ atom nào”; chúng cho amplitude và phase contribution của từng basis function vào MO.

# Khi nào hai atomic orbitals tương tác mạnh?

Tương tác đáng kể khi ba điều kiện tương đối phù hợp:

```text
1. energies không quá xa nhau
2. symmetry cho phép overlap
3. spatial overlap đủ lớn
```

Hai orbitals rất lệch energy hoặc symmetry không phù hợp có thể gần như không trộn dù atoms ở gần.

Điều này trở thành nguyên tắc quan trọng trong frontier-orbital reasoning và spectroscopy.

# Bonding và antibonding combinations

Với hai basis functions \(\phi_A\), \(\phi_B\), hai combinations đơn giản:

\[
\psi_+=c(\phi_A+\phi_B)
\]

\[
\psi_-=c(\phi_A-\phi_B)
\]

Combination cùng phase tăng electron density giữa nuclei và thường là **bonding MO**.

Combination opposite phase tạo node giữa nuclei và thường là **antibonding MO**, ký hiệu \(^*\).

Không nên hiểu “plus = hút, minus = đẩy” như một rule đại số độc lập; energy difference xuất phát từ kinetic + electron–nuclear + nuclear repulsion terms của Hamiltonian.

# Hai atomic orbitals tạo hai molecular orbitals

Nếu combine two AOs, tổng số one-electron states được bảo toàn: tạo one lower-energy bonding MO và one higher-energy antibonding MO.

Đây là conservation of basis dimension:

```text
2 AO → 2 MO
N AO → N MO
```

MO theory không “mất” orbital khi tạo bond; nó reorganize orbital basis thành states của toàn molecule.

# H₂ — ví dụ tối giản

Hai 1s orbitals tạo:

\[
\sigma_{1s}
\]

và:

\[
\sigma^*_{1s}
\]

Hai electrons occupy bonding orbital:

\[
(\sigma_{1s})^2
\]

Bond order:

\[
BO=\frac{N_b-N_a}{2}=1
\]

Vì bonding population vượt antibonding population, H₂ được ổn định tương đối so với separated atoms.

# H₂⁺ và He₂ — kiểm tra logic bond order

H₂⁺ có một electron bonding:

\[
BO=\frac12
\]

và thực sự có bound state yếu hơn H₂.

He₂ ground-state simple configuration:

\[
(\sigma_{1s})^2(\sigma^*_{1s})^2
\]

cho:

\[
BO=0
\]

nên không dự đoán conventional stable He–He bond.

Ví dụ này cho thấy electron đầy shell nguyên tử không tự động nghĩa molecule bền.

# Sigma và pi molecular orbitals

MO symmetry được phân loại theo bond axis.

**σ MO** có symmetry quanh internuclear axis.

**π MO** có nodal plane chứa axis và thường đến từ side-on overlap của p orbitals.

Hai perpendicular p directions có thể tạo pair π orbitals degenerate trong diatomic molecule có symmetry cao.

# Thứ tự MO của diatomic period 2

Một sơ đồ đơn giản gồm:

```text
σ2s
σ*2s
π2p / σ2p
π*2p
σ*2p
```

Nhưng order giữa \(\pi_{2p}\) và \(\sigma_{2p}\) thay đổi dọc chu kỳ do **s–p mixing**.

Trong B₂, C₂, N₂, mixing mạnh hơn; với O₂, F₂ energy separation thay đổi và order khác.

Vì vậy không nên học một MO diagram universal duy nhất. Hãy reasoning từ symmetry + relative AO energies.

# N₂ — bond order cao và bond mạnh

MO occupancy của N₂ cho bond order gần 3.

Điều này phù hợp với:

- bond ngắn;
- dissociation energy cao;
- chemical inertness tương đối ở room conditions.

Nhưng “bond mạnh” không tự động nói reaction không thuận lợi về thermodynamics; nó góp phần làm activation barriers lớn cho processes phải phá N≡N.

Đây là lý do nitrogen fixation cần enzymes/catalysts có chiến lược activation đặc biệt.

# O₂ — bằng chứng kinh điển của MO theory

Lewis O=O cho all electrons paired, nhưng O₂ bị hút vào magnetic field: nó **thuận từ (paramagnetic)**.

MO theory đặt two electrons vào two degenerate \(\pi^*\) orbitals theo Hund:

```text
π*x ↑
π*y ↑
```

hai electron độc thân → paramagnetism.

Đây là một observation mà simple Lewis picture không giải thích tự nhiên.

# O₂⁺, O₂, O₂⁻, O₂²⁻

Các species khác nhau chủ yếu ở occupancy antibonding \(\pi^*\).

Rút electron khỏi antibonding orbital:

```text
bond order tăng
bond thường ngắn/mạnh hơn
```

Thêm electron vào antibonding:

```text
bond order giảm
bond thường dài/yếu hơn
```

Đây là relation hữu ích để hiểu superoxide \(O_2^-\) và peroxide \(O_2^{2-}\) trong bioinorganic chemistry.

# Bond order là model, không phải số thanh bond

MO bond order:

\[
BO=\frac{N_b-N_a}{2}
\]

là measure của net bonding occupancy trong simple diagram.

Trong polyatomic molecules và computational chemistry có nhiều bond-order definitions khác như Wiberg hoặc Mayer. Chúng có thể không cho cùng exact number.

Bond order nên được dùng như descriptor, không phải observable cơ bản duy nhất.

# Heteronuclear molecules — atomic orbitals không cùng năng lượng

Trong CO hoặc HF, orbitals của hai atoms không có energy giống nhau.

AO của atom electronegative hơn thường lower energy. Vì vậy bonding MO có coefficient lớn hơn ở lower-energy atom, còn antibonding MO thường có character nhiều hơn ở higher-energy partner.

Điều này giải thích tại sao MO không nhất thiết “50/50 giữa hai atoms”.

# HF — symmetry chọn orbital nào được bond

H 1s có symmetry phù hợp để overlap với F orbital hướng theo bond axis, thường F 2p_z-like combination.

Các F p orbitals vuông góc axis không overlap với H 1s theo symmetry, nên chúng gần **nonbonding**.

Đây là ví dụ rõ rằng molecular orbital formation bị symmetry selection chi phối.

# Nonbonding orbitals

Không phải mọi MO đều bonding hoặc antibonding mạnh.

Một **nonbonding orbital** có energy gần parent AO và electron density ít ảnh hưởng bond giữa nuclei.

Lone pairs trong many molecules có thể được hiểu như localized version của occupied nonbonding MOs.

Nonbonding electrons rất quan trọng cho:

- Lewis basicity;
- nucleophilicity;
- spectroscopy;
- photochemistry.

# HOMO và LUMO

**HOMO (Highest Occupied Molecular Orbital)** là occupied MO có energy cao nhất trong ground-state independent-particle picture.

**LUMO (Lowest Unoccupied Molecular Orbital)** là unoccupied MO thấp nhất.

Khoảng:

\[
\Delta E_{HL}=E_{LUMO}-E_{HOMO}
\]

thường liên hệ qualitatively với electronic excitation và reactivity, nhưng không nên đồng nhất trực tiếp với exact optical band gap vì electron correlation và relaxation matters.

# Frontier molecular orbital reasoning

Trong donor–acceptor interaction, occupied orbital của donor tương tác mạnh với unoccupied orbital của acceptor khi:

- energies tương đối gần;
- symmetry phù hợp;
- spatial overlap tốt.

Trong organic chemistry:

```text
nucleophile HOMO-like orbital
→ electrophile LUMO-like orbital
```

là một model mạnh để giải thích orientation và selectivity.

# Carbonyl — vì sao carbon là electrophilic site?

Trong C=O, oxygen electronegative làm occupied π orbital skew về O, còn \(\pi^*\) LUMO có amplitude đáng kể trên carbon.

Nucleophile donation vào \(\pi^*\) làm C=O bond order giảm và tạo new σ bond với carbon.

MO picture giải thích electron flow mà Lewis curved-arrow notation biểu diễn ở mức bookkeeping.

# Conjugated π systems

Với \(N\) adjacent p orbitals, tạo \(N\) π MOs trải trên framework.

Ví dụ butadiene có four p orbitals → four π MOs.

Four π electrons fill two lowest-energy orbitals.

Delocalization làm energy khác với picture two isolated double bonds và ảnh hưởng:

- bond lengths;
- rotational barriers;
- UV absorption;
- reactivity.

# Benzene và aromaticity bằng MO

Six p orbitals combine thành six π MOs.

Six π electrons fill all bonding MOs theo closed-shell pattern, tạo special stabilization và symmetry.

Hückel rule \(4n+2\) có thể được hiểu từ occupancy pattern của cyclic conjugated MO levels, không chỉ là một công thức đếm electron cần học thuộc.

# Hückel approximation

**Hückel molecular orbital (HMO)** là model đơn giản cho π systems, thường đặt:

\[
H_{ii}=\alpha
\]

\[
H_{ij}=\beta
\]

cho neighboring p orbitals và bỏ qua nhiều interactions khác.

Dù thô, model cho qualitative MO energies, coefficients và aromaticity trends.

Đây là ví dụ đẹp của việc một matrix eigenvalue problem đơn giản hóa chemistry.

# MO theory là bài toán trị riêng

Trong quantum chemistry, orbital coefficients được tìm từ equations dạng:

\[
\mathbf H\mathbf c
=E\mathbf S\mathbf c
\]

với \(\mathbf H\) là matrix Hamiltonian và \(\mathbf S\) là overlap matrix.

Nếu basis orthonormal, bài toán gần dạng eigenvalue quen thuộc:

\[
Hc=Ec
\]

Đây là liên hệ trực tiếp giữa hóa học lượng tử và đại số tuyến tính.

# Electron correlation — giới hạn của orbital đơn hạt

Một Slater determinant Hartree–Fock mô tả mỗi electron chuyển động trong average field của các electron khác.

Nó bỏ sót **electron correlation** tức sự tránh nhau tức thời ngoài average-field picture.

Correlation quan trọng cho:

- bond breaking;
- dispersion;
- near-degenerate states;
- accurate reaction energies.

Vì vậy MO diagrams rất hữu ích nhưng không phải exact many-electron wavefunction.

# Hartree–Fock và DFT

**Hartree–Fock (HF)** tối ưu orbitals trong single-determinant model.

**Lý thuyết phiếm hàm mật độ (density functional theory, DFT)** dùng electron density làm biến cơ bản và đưa exchange–correlation vào functional gần đúng.

Không có một “DFT answer” duy nhất; result phụ thuộc functional, basis set và numerical settings.

Computational chemistry vì thế cần validation, không chỉ chạy software.

# Basis set

MO calculations expand orbitals trong **bộ hàm cơ sở (basis set)**.

Basis lớn hơn cho wavefunction flexibility hơn nhưng computational cost tăng.

Các features như polarization và diffuse functions quan trọng cho:

- anions;
- weak interactions;
- excited states;
- response properties.

Một calculation không chỉ được định nghĩa bởi method name; basis set là phần của model specification.

# Orbital energies không phải luôn observable

Canonical orbital energies là model quantities. Theo Koopmans approximation, occupied HF orbital energy có thể gần negative ionization energy, nhưng relaxation/correlation làm relation không exact.

Do đó không nên coi HOMO energy trực tiếp như một năng lượng electron có thể đo đơn giản trong mọi method.

# Photoelectron spectroscopy

**Quang phổ quang electron (photoelectron spectroscopy, PES)** đo năng lượng cần để loại electron.

Patterns có thể được so với electronic-structure calculations để suy orbital character.

Đây là cầu nối giữa abstract MO diagram và experimental evidence.

# Electronic excitation

Khi hấp thụ photon:

\[
h\nu=\Delta E
\]

electron population có thể chuyển từ occupied state sang unoccupied state.

Common labels:

```text
π → π*
n → π*
d → d
charge-transfer excitation
```

Excitation thay electron occupancy nên bonding, geometry và reactivity có thể thay đổi mạnh.

# Photochemistry — excited-state surface khác ground state

Một photochemical reaction không đơn giản là ground-state reaction “có thêm năng lượng”. Excited electronic state có potential-energy surface khác.

Bonding orbital ground state có thể trở thành singly occupied/antibonding population, làm bond weakness và preferred geometry thay đổi.

Đây là lý do ánh sáng có thể mở reaction pathways thermally inaccessible.

# Conical intersections

Trong polyatomic molecules, excited và ground-state energy surfaces có thể gặp nhau gần **conical intersection**.

Tại đây nonradiative transition giữa electronic states có thể cực nhanh.

Conical intersections là central concept trong modern photochemistry, vision chemistry và photostability of DNA bases.

# MO và magnetism

Magnetism phụ thuộc unpaired electrons.

MO occupancy cho direct count của unpaired electrons trong simple cases.

Transition-metal complexes cần ligand-field/MO treatment sâu hơn, nhưng cùng nguyên lý electron occupancy vẫn quyết định spin state và magnetic moment.

# MO và coordination chemistry

Ligand orbitals combine theo symmetry thành **SALCs — symmetry-adapted linear combinations**.

SALCs sau đó tương tác với metal s/p/d orbitals có cùng symmetry.

Cách nhìn này mở rộng crystal-field picture thành ligand-field/MO theory và giải thích covalency, π backbonding và spectroscopy.

# CO metal bonding — donation và back-donation

CO ligand donate electron pair từ occupied orbital vào metal acceptor orbital:

```text
CO → M σ donation
```

Metal d electrons có thể donate ngược vào CO \(\pi^*\):

```text
M → CO π back-donation
```

Back-donation làm C–O bond yếu hơn, nên IR stretching frequency giảm.

Đây là example mạnh nối MO → coordination → spectroscopy → catalysis.

# Từ MO tới dải năng lượng

Khi two atoms combine, two levels split.

Khi \(N\) atoms combine, mỗi AO-derived level tạo ~\(N\) closely spaced MOs.

Với crystal macroscopic:

```text
rất nhiều levels gần nhau → energy band
```

Occupied/empty band structure quyết định metal, semiconductor hoặc insulator behavior.

MO theory vì vậy là prerequisite tự nhiên của semiconductor chemistry.

# Valence band và conduction band

Trong semiconductor:

- **valence band** chứa states occupied gần Fermi level;
- **conduction band** chứa states cao hơn cho mobile carriers;
- **band gap** là vùng không có allowed bulk states trong simple picture.

Doping thay carrier population và Fermi level mà chỉ cần impurity concentration rất nhỏ.

Điều này nối chemical composition với electronics.

# Delocalization và conducting polymers

Polyacetylene, polythiophene và nhiều conjugated polymers có π states trải dọc backbone.

Tăng conjugation thường giảm effective frontier gap. Doping tạo charge carriers/polarons và làm conductivity tăng mạnh.

Đây là lý do organic chemistry, MO theory và materials electronics gặp nhau.

# MO theory và color

Một compound hấp thụ visible light khi có allowed electronic transition với energy phù hợp visible photons.

Color không đến từ “bond có màu” mà từ electronic-state energy differences + transition probabilities.

Transition-metal complexes, organic dyes và semiconductor nanoparticles đều có màu nhưng cơ chế electronic khác nhau.

# Symmetry và selection rules

Không phải transition nào có \(\Delta E=h\nu\) cũng hấp thụ mạnh. Transition dipole còn phải khác zero theo symmetry.

**Quy tắc chọn lọc (selection rules)** giải thích vì sao một số electronic/vibrational transitions mạnh, yếu hoặc forbidden trong ideal symmetry.

Molecular symmetry vì thế nối geometry với spectroscopy.

# Localized và delocalized descriptions không loại trừ nhau

Canonical MOs thường delocalized. Nhưng occupied orbital space có thể được unitary transform thành localized orbitals mà total wavefunction không đổi trong relevant model.

Vì vậy:

```text
Lewis/VB localized picture
và
MO delocalized picture
```

có thể là hai representations hữu ích của cùng electronic state cho hai loại câu hỏi khác nhau.

# Khi nào nên dùng MO theory?

MO đặc biệt có giá trị khi cần:

- magnetism;
- spectroscopy;
- excited states;
- global conjugation;
- aromaticity;
- donor–acceptor interactions;
- transition-metal bonding;
- semiconductor bands;
- computational chemistry.

Nếu chỉ cần acid-base arrow pushing hoặc local stereochemistry, Lewis/VB có thể trực quan hơn.

# Những hiểu lầm thường gặp

### “Antibonding electron không thuộc molecule”

Sai. Antibonding MO vẫn là state của molecule; occupancy của nó chỉ giảm net bonding.

### “HOMO–LUMO gap luôn bằng optical absorption energy”

Không exact. Exciton, correlation, relaxation và method definitions matter.

### “MO theory nói electron thật chạy quanh toàn molecule như một hạt trên quỹ đạo”

Không. MO là wavefunction/state probability description, không phải classical trajectory.

### “Một orbital diagram đúng cho mọi diatomic period-2 molecules”

Không. s–p mixing làm ordering thay đổi.

### “DFT cho kết quả chính xác tuyệt đối”

Không. Functional/basis/numerical model phải được benchmark phù hợp.

## Mô hình tư duy

MO theory chuyển câu hỏi từ:

> “electron pair này thuộc bond nào?”

sang:

> “toàn hệ nhiều nuclei cho phép những one-electron states nào, chúng có energy/symmetry gì và electron chiếm chúng ra sao?”

Chuỗi suy luận:

```text
atomic basis
→ symmetry + energy matching
→ molecular orbitals
→ electron occupancy
→ bond order / magnetism / excitation / reactivity
→ nhiều atoms
→ energy bands và materials
```

Xem tiếp: [Lực liên phân tử](./07_intermolecular_forces.md), [Hóa học trường phối tử](../10_inorganic_chemistry/04_crystal_field_and_ligand_field.md) và [Chất bán dẫn](../14_materials_and_polymer_chemistry/03_semiconductors.md).