# Lý thuyết obitan phân tử — nhìn electron như trạng thái của toàn phân tử

> **Mạch đọc:** Đọc **Lý thuyết obitan phân tử — nhìn electron như trạng thái của toàn phân tử** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **“Antibonding electron không thuộc molecule”** sang **“HOMO–LUMO gap luôn bằng optical absorption năng lượng (energy / 에너지)”**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


> **Lý thuyết obitan phân tử (molecular orbital theory, MO / 분자 오비탈 이론)** mô tả electron bằng các obitan có thể trải trên toàn bộ phân tử thay vì mặc định gán mỗi cặp electron cho một liên kết cục bộ. MO lý thuyết (theory / 이론) đặc biệt mạnh khi cần hiểu **sự phi định xứ, bậc liên kết, từ tính, màu, kích thích electron, quang hóa và sự hình thành dải năng lượng trong chất rắn**.

Lewis và valence-bond ngôn ngữ (language / 언어) rất hữu ích cho connectivity và cục bộ (local / 로컬) reactivity. MO lý thuyết (theory / 이론) trả lời một lớp câu hỏi khác: nếu toàn bộ electron chịu trường của nhiều nuclei cùng lúc, các trạng thái lượng tử của cả hệ trông như thế nào?

# Tổ hợp tuyến tính của obitan nguyên tử

Trong cách tiếp cận **LCAO — tổ hợp tuyến tính obitan nguyên tử (Linear Combination of Atomic Orbitals)**, molecular orbital được viết khái niệm:

\[
\psi_{MO}=\sum_i c_i\phi_i
\]

trong đó \(\phi_i\) là atomic basis functions còn \(c_i\) là coefficients.

Các coefficients không chỉ nói orbital “đến từ atom nào”; chúng cho amplitude và phase contribution của từng basis hàm (function / 함수) vào MO.

# Khi nào hai atomic orbitals tương tác mạnh?

Tương tác đáng kể khi ba điều kiện tương đối phù hợp:

```text
1. energies không quá xa nhau
2. symmetry cho phép overlap
3. spatial overlap đủ lớn
```

Hai orbitals rất lệch năng lượng (energy / 에너지) hoặc symmetry không phù hợp có thể gần như không trộn dù atoms ở gần.

Điều này trở thành nguyên tắc quan trọng trong frontier-orbital lập luận (reasoning / 추론) và spectroscopy.

# Bonding và antibonding combinations

Với hai basis functions \(\phi_A\), \(\phi_B\), hai combinations đơn giản:

\[
\psi_+=c(\phi_A+\phi_B)
\]

\[
\psi_-=c(\phi_A-\phi_B)
\]

Combination cùng phase tăng electron density giữa nuclei và thường là **bonding MO**.

Combination opposite phase tạo nút (node / 노드) giữa nuclei và thường là **antibonding MO**, ký hiệu \(^*\).

Không nên hiểu “plus = hút, minus = đẩy” như một quy tắc (rule / 규칙) đại số độc lập; năng lượng (energy / 에너지) difference xuất phát từ kinetic + electron–nuclear + nuclear repulsion terms của Hamiltonian.

# Hai atomic orbitals tạo hai molecular orbitals

Nếu combine two AOs, tổng số one-electron states được bảo toàn: tạo one lower-energy bonding MO và one higher-energy antibonding MO.

Đây là conservation of basis dimension:

```text
2 AO → 2 MO
N AO → N MO
```

MO lý thuyết (theory / 이론) không “mất” orbital khi tạo bond; nó reorganize orbital basis thành states của toàn molecule.

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

Bond thứ tự (order / 순서):

\[
BO=\frac{N_b-N_a}{2}=1
\]

Vì bonding population vượt antibonding population, H₂ được ổn định tương đối so với separated atoms.

# H₂⁺ và He₂ — kiểm tra lô-gic (logic / 논리) bond thứ tự (order / 순서)

H₂⁺ có một electron bonding:

\[
BO=\frac12
\]

và thực sự có bound trạng thái (state / 상태) yếu hơn H₂.

He₂ ground-state simple cấu hình (configuration / 구성):

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

Nhưng thứ tự (order / 순서) giữa \(\pi_{2p}\) và \(\sigma_{2p}\) thay đổi dọc chu kỳ do **s–p mixing**.

Trong B₂, C₂, N₂, mixing mạnh hơn; với O₂, F₂ năng lượng (energy / 에너지) separation thay đổi và thứ tự (order / 순서) khác.

Vì vậy không nên học một MO diagram universal duy nhất. Hãy lập luận (reasoning / 추론) từ symmetry + relative AO energies.

# N₂ — bond thứ tự (order / 순서) cao và bond mạnh

MO occupancy của N₂ cho bond thứ tự (order / 순서) gần 3.

Điều này phù hợp với:

- bond ngắn;
- dissociation năng lượng (energy / 에너지) cao;
- chemical inertness tương đối ở room conditions.

Nhưng “bond mạnh” không tự động nói reaction không thuận lợi về thermodynamics; nó góp phần làm activation barriers lớn cho processes phải phá N≡N.

Đây là lý do nitrogen fixation cần enzymes/catalysts có chiến lược activation đặc biệt.

# O₂ — bằng chứng kinh điển của MO lý thuyết (theory / 이론)

Lewis O=O cho all electrons paired, nhưng O₂ bị hút vào magnetic trường dữ liệu (field / 필드): nó **thuận từ (paramagnetic)**.

MO lý thuyết (theory / 이론) đặt two electrons vào two degenerate \(\pi^*\) orbitals theo Hund:

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

Đây là quan hệ (relation / 관계) hữu ích để hiểu superoxide \(O_2^-\) và peroxide \(O_2^{2-}\) trong bioinorganic chemistry.

# Bond thứ tự (order / 순서) là mô hình (model / 모델), không phải số thanh bond

MO bond thứ tự (order / 순서):

\[
BO=\frac{N_b-N_a}{2}
\]

là measure của net bonding occupancy trong simple diagram.

Trong polyatomic molecules và computational chemistry có nhiều bond-order definitions khác như Wiberg hoặc Mayer. Chúng có thể không cho cùng chính xác (exact / 정확한) number.

Bond thứ tự (order / 순서) nên được dùng như descriptor, không phải observable cơ bản duy nhất.

# Heteronuclear molecules — atomic orbitals không cùng năng lượng

Trong CO hoặc HF, orbitals của hai atoms không có năng lượng (energy / 에너지) giống nhau.

AO của atom electronegative hơn thường lower năng lượng (energy / 에너지). Vì vậy bonding MO có coefficient lớn hơn ở lower-energy atom, còn antibonding MO thường có character nhiều hơn ở higher-energy partner.

Điều này giải thích tại sao MO không nhất thiết “50/50 giữa hai atoms”.

# HF — symmetry chọn orbital nào được bond

H 1s có symmetry phù hợp để overlap với F orbital hướng theo bond axis, thường F 2p_z-like combination.

Các F p orbitals vuông góc axis không overlap với H 1s theo symmetry, nên chúng gần **nonbonding**.

Đây là ví dụ rõ rằng molecular orbital formation bị symmetry selection chi phối.

# Nonbonding orbitals

Không phải mọi MO đều bonding hoặc antibonding mạnh.

Một **nonbonding orbital** có năng lượng (energy / 에너지) gần parent AO và electron density ít ảnh hưởng bond giữa nuclei.

Lone pairs trong many molecules có thể được hiểu như localized phiên bản (version / 버전) của occupied nonbonding MOs.

Nonbonding electrons rất quan trọng cho:

- Lewis basicity;
- nucleophilicity;
- spectroscopy;
- photochemistry.

# HOMO và LUMO

**HOMO (Highest Occupied Molecular Orbital)** là occupied MO có năng lượng (energy / 에너지) cao nhất trong ground-state independent-particle picture.

**LUMO (Lowest Unoccupied Molecular Orbital)** là unoccupied MO thấp nhất.

Khoảng:

\[
\Delta E_{HL}=E_{LUMO}-E_{HOMO}
\]

thường liên hệ qualitatively với electronic excitation và reactivity, nhưng không nên đồng nhất trực tiếp với chính xác (exact / 정확한) optical band gap vì electron correlation và relaxation matters.

# Frontier molecular orbital lập luận (reasoning / 추론)

Trong donor–acceptor tương tác (interaction / 상호작용), occupied orbital của donor tương tác mạnh với unoccupied orbital của acceptor khi:

- energies tương đối gần;
- symmetry phù hợp;
- spatial overlap tốt.

Trong organic chemistry:

```text
nucleophile HOMO-like orbital
→ electrophile LUMO-like orbital
```

là một mô hình (model / 모델) mạnh để giải thích orientation và selectivity.

# Carbonyl — vì sao carbon là electrophilic site?

Trong C=O, oxygen electronegative làm occupied π orbital skew về O, còn \(\pi^*\) LUMO có amplitude đáng kể trên carbon.

Nucleophile donation vào \(\pi^*\) làm C=O bond thứ tự (order / 순서) giảm và tạo new σ bond với carbon.

MO picture giải thích electron luồng (flow / 흐름) mà Lewis curved-arrow notation biểu diễn ở mức bookkeeping.

# Conjugated π các hệ thống (systems / 시스템들)

Với \(N\) adjacent p orbitals, tạo \(N\) π MOs trải trên khung phần mềm (framework / 프레임워크).

Ví dụ butadiene có four p orbitals → four π MOs.

Four π electrons fill two lowest-energy orbitals.

Delocalization làm năng lượng (energy / 에너지) khác với picture two isolated double bonds và ảnh hưởng:

- bond lengths;
- rotational barriers;
- UV absorption;
- reactivity.

# Benzene và aromaticity bằng MO

Six p orbitals combine thành six π MOs.

Six π electrons fill all bonding MOs theo closed-shell mẫu (pattern / 패턴), tạo special stabilization và symmetry.

Hückel quy tắc (rule / 규칙) \(4n+2\) có thể được hiểu từ occupancy mẫu (pattern / 패턴) của cyclic conjugated MO levels, không chỉ là một công thức đếm electron cần học thuộc.

# Hückel approximation

**Hückel molecular orbital (HMO)** là mô hình (model / 모델) đơn giản cho π các hệ thống (systems / 시스템들), thường đặt:

\[
H_{ii}=\alpha
\]

\[
H_{ij}=\beta
\]

cho neighboring p orbitals và bỏ qua nhiều interactions khác.

Dù thô, mô hình (model / 모델) cho qualitative MO energies, coefficients và aromaticity trends.

Đây là ví dụ đẹp của việc một ma trận (matrix / 행렬) eigenvalue bài toán (problem / 문제) đơn giản hóa chemistry.

# MO lý thuyết (theory / 이론) là bài toán trị riêng

Trong quantum chemistry, orbital coefficients được tìm từ equations dạng:

\[
\mathbf H\mathbf c
=E\mathbf S\mathbf c
\]

với \(\mathbf H\) là ma trận (matrix / 행렬) Hamiltonian và \(\mathbf S\) là overlap ma trận (matrix / 행렬).

Nếu basis orthonormal, bài toán gần dạng eigenvalue quen thuộc:

\[
Hc=Ec
\]

Đây là liên hệ trực tiếp giữa hóa học lượng tử và đại số tuyến tính.

# Electron correlation — giới hạn của orbital đơn hạt

Một Slater determinant Hartree–Fock mô tả mỗi electron chuyển động trong average trường dữ liệu (field / 필드) của các electron khác.

Nó bỏ sót **electron correlation** tức sự tránh nhau tức thời ngoài average-field picture.

Correlation quan trọng cho:

- bond breaking;
- dispersion;
- near-degenerate states;
- accurate reaction energies.

Vì vậy MO diagrams rất hữu ích nhưng không phải chính xác (exact / 정확한) many-electron wavefunction.

# Hartree–Fock và DFT

**Hartree–Fock (HF)** tối ưu orbitals trong single-determinant mô hình (model / 모델).

**Lý thuyết phiếm hàm mật độ (density functional theory, DFT)** dùng electron density làm biến cơ bản và đưa exchange–correlation vào functional gần đúng.

Không có một “DFT answer” duy nhất; kết quả (result / 결과) phụ thuộc functional, basis set và numerical settings.

Computational chemistry vì thế cần kiểm tra hợp lệ (validation / 검증), không chỉ chạy software.

# Basis set

MO calculations expand orbitals trong **bộ hàm cơ sở (basis set)**.

Basis lớn hơn cho wavefunction flexibility hơn nhưng computational chi phí (cost / 비용) tăng.

Các features như polarization và diffuse functions quan trọng cho:

- anions;
- weak interactions;
- excited states;
- phản hồi (response / 응답) properties.

Một calculation không chỉ được định nghĩa bởi phương thức (method / 메서드) name; basis set là phần của mô hình (model / 모델) specification.

# Orbital energies không phải luôn observable

Chuẩn gốc (canonical / 정본) orbital energies là mô hình (model / 모델) quantities. Theo Koopmans approximation, occupied HF orbital năng lượng (energy / 에너지) có thể gần negative ionization năng lượng (energy / 에너지), nhưng relaxation/correlation làm quan hệ (relation / 관계) không chính xác (exact / 정확한).

Do đó không nên coi HOMO năng lượng (energy / 에너지) trực tiếp như một năng lượng electron có thể đo đơn giản trong mọi phương thức (method / 메서드).

# Photoelectron spectroscopy

**Quang phổ quang electron (photoelectron spectroscopy, PES)** đo năng lượng cần để loại electron.

Patterns có thể được so với electronic-structure calculations để suy orbital character.

Đây là cầu nối giữa abstract MO diagram và experimental bằng chứng (evidence / 증거).

# Electronic excitation

Khi hấp thụ photon:

\[
h\nu=\Delta E
\]

electron population có thể chuyển từ occupied trạng thái (state / 상태) sang unoccupied trạng thái (state / 상태).

Dùng chung (common / 공통) labels:

```text
π → π*
n → π*
d → d
charge-transfer excitation
```

Excitation thay electron occupancy nên bonding, hình học (geometry / 기하학) và reactivity có thể thay đổi mạnh.

# Photochemistry — excited-state surface khác ground trạng thái (state / 상태)

Một photochemical reaction không đơn giản là ground-state reaction “có thêm năng lượng”. Excited electronic trạng thái (state / 상태) có potential-energy surface khác.

Bonding orbital ground trạng thái (state / 상태) có thể trở thành singly occupied/antibonding population, làm bond weakness và preferred hình học (geometry / 기하학) thay đổi.

Đây là lý do ánh sáng có thể mở reaction pathways thermally inaccessible.

# Conical intersections

Trong polyatomic molecules, excited và ground-state năng lượng (energy / 에너지) surfaces có thể gặp nhau gần **conical intersection**.

Tại đây nonradiative chuyển tiếp (transition / 전이) giữa electronic states có thể cực nhanh.

Conical intersections là central concept trong hiện đại (modern / 현대적) photochemistry, vision chemistry và photostability of DNA bases.

# MO và magnetism

Magnetism phụ thuộc unpaired electrons.

MO occupancy cho direct count của unpaired electrons trong simple cases.

Transition-metal complexes cần ligand-field/MO treatment sâu hơn, nhưng cùng nguyên lý electron occupancy vẫn quyết định spin trạng thái (state / 상태) và magnetic moment.

# MO và coordination chemistry

Ligand orbitals combine theo symmetry thành **SALCs — symmetry-adapted tuyến tính (linear / 선형) combinations**.

SALCs sau đó tương tác với metal s/p/d orbitals có cùng symmetry.

Cách nhìn này mở rộng crystal-field picture thành ligand-field/MO lý thuyết (theory / 이론) và giải thích covalency, π backbonding và spectroscopy.

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

Khi \(N\) atoms combine, mỗi AO-derived mức (level / 수준) tạo ~\(N\) closely spaced MOs.

Với crystal macroscopic:

```text
rất nhiều levels gần nhau → energy band
```

Occupied/empty band cấu trúc (structure / 구조) quyết định metal, semiconductor hoặc insulator hành vi (behavior / 동작).

MO lý thuyết (theory / 이론) vì vậy là prerequisite tự nhiên của semiconductor chemistry.

# Valence band và conduction band

Trong semiconductor:

- **valence band** chứa states occupied gần Fermi mức (level / 수준);
- **conduction band** chứa states cao hơn cho mobile carriers;
- **band gap** là vùng không có allowed bulk states trong simple picture.

Doping thay carrier population và Fermi mức (level / 수준) mà chỉ cần impurity concentration rất nhỏ.

Điều này nối chemical composition với electronics.

# Delocalization và conducting polymers

Polyacetylene, polythiophene và nhiều conjugated polymers có π states trải dọc backbone.

Tăng conjugation thường giảm effective frontier gap. Doping tạo charge carriers/polarons và làm conductivity tăng mạnh.

Đây là lý do organic chemistry, MO lý thuyết (theory / 이론) và materials electronics gặp nhau.

# MO lý thuyết (theory / 이론) và color

Một compound hấp thụ visible light khi có allowed electronic chuyển tiếp (transition / 전이) với năng lượng (energy / 에너지) phù hợp visible photons.

Color không đến từ “bond có màu” mà từ electronic-state năng lượng (energy / 에너지) differences + chuyển tiếp (transition / 전이) probabilities.

Transition-metal complexes, organic dyes và semiconductor nanoparticles đều có màu nhưng cơ chế electronic khác nhau.

# Symmetry và selection rules

Không phải chuyển tiếp (transition / 전이) nào có \(\Delta E=h\nu\) cũng hấp thụ mạnh. chuyển tiếp (transition / 전이) dipole còn phải khác zero theo symmetry.

**Quy tắc chọn lọc (selection rules)** giải thích vì sao một số electronic/vibrational transitions mạnh, yếu hoặc forbidden trong ideal symmetry.

Molecular symmetry vì thế nối hình học (geometry / 기하학) với spectroscopy.

# Localized và delocalized descriptions không loại trừ nhau

Chuẩn gốc (canonical / 정본) MOs thường delocalized. Nhưng occupied orbital không gian (space / 공간) có thể được unitary transform thành localized orbitals mà total wavefunction không đổi trong relevant mô hình (model / 모델).

Vì vậy:

```text
Lewis/VB localized picture
và
MO delocalized picture
```

có thể là hai representations hữu ích của cùng electronic trạng thái (state / 상태) cho hai loại câu hỏi khác nhau.

# Khi nào nên dùng MO lý thuyết (theory / 이론)?

MO đặc biệt có giá trị khi cần:

- magnetism;
- spectroscopy;
- excited states;
- toàn cục (global / 전역) conjugation;
- aromaticity;
- donor–acceptor interactions;
- transition-metal bonding;
- semiconductor bands;
- computational chemistry.

Nếu chỉ cần acid-base arrow pushing hoặc cục bộ (local / 로컬) stereochemistry, Lewis/VB có thể trực quan hơn.

# Những hiểu lầm thường gặp

### “Antibonding electron không thuộc molecule”

Sai. Antibonding MO vẫn là trạng thái (state / 상태) của molecule; occupancy của nó chỉ giảm net bonding.

### “HOMO–LUMO gap luôn bằng optical absorption năng lượng (energy / 에너지)”

Không chính xác (exact / 정확한). Exciton, correlation, relaxation và phương thức (method / 메서드) definitions matter.

### “MO lý thuyết (theory / 이론) nói electron thật chạy quanh toàn molecule như một hạt trên quỹ đạo”

Không. MO là wavefunction/trạng thái (state / 상태) xác suất (probability / 확률) description, không phải classical trajectory.

### “Một orbital diagram đúng cho mọi diatomic period-2 molecules”

Không. s–p mixing làm thứ tự (ordering / 순서) thay đổi.

### “DFT cho kết quả chính xác tuyệt đối”

Không. Functional/basis/numerical mô hình (model / 모델) phải được benchmark phù hợp.

## Mô hình tư duy

MO lý thuyết (theory / 이론) chuyển câu hỏi từ:

> “electron pair này thuộc bond nào?”

sang:

> “toàn hệ nhiều nuclei cho phép những one-electron states nào, chúng có năng lượng (energy / 에너지)/symmetry gì và electron chiếm chúng ra sao?”

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

> **Bàn giao:** Sau **Mô hình tư duy**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 why atoms bond](./00_why_atoms_bond.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
