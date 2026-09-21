# Thư viện kiến thức Hóa học — Kiểm tra độ bao phủ

> Tài liệu này theo dõi **độ bao phủ khái niệm, quan hệ phụ thuộc, tính nhất quán ngôn ngữ, mức độ trùng lặp và chất lượng chiều sâu** của Chemistry Knowledge Library. Đây không phải bản tóm tắt để học nhanh. Mục tiêu là xác định những vấn đề còn phải xử lý trước khi branch Chemistry có thể được coi là sẵn sàng hợp nhất vào `main`.

## Branch canonical

Branch Chemistry canonical:

```text
feat/chemistry-knowledge-library
```

`feat/chemistry-depth-pass` là ancestor cũ đã được gom đầy đủ vào canonical branch và đã được xóa sau pre-merge audit.

`main` đang thay đổi liên tục bởi nhiều workstream khác. Vì vậy **không merge, không rebase cưỡng bức và không force-update `main` trong khi Chemistry chưa vượt qua các gate cuối**.

## Thứ tự ưu tiên audit

```text
1. file rỗng / skeleton
2. chapter quá sơ sài so với phạm vi
3. conceptual gap
4. prerequisite bị thiếu
5. giải thích rời rạc / quá nhiều tiếng Anh
6. thiếu example / mechanism / trade-off
7. broken internal links
8. README / coverage metadata
```

Kích thước file chỉ là tín hiệu. Chapter ngắn nhưng phạm vi hẹp và reasoning đầy đủ không cần kéo dài chỉ để cân số dòng.

# Trạng thái cấu trúc

Các domain từ `00` tới `17` đã được quét theo metadata kích thước và mở nội dung các ứng viên bất thường.

Hiện **không phát hiện file canonical rỗng hoặc skeleton quan trọng**.

Các file `90_connections` ngắn hơn chapter textbook chính nhưng có scope khác: chúng là lớp kết nối kiến thức, không phải textbook độc lập. Không coi chúng là skeleton chỉ vì kích thước nhỏ hơn.

Dependency flow hiện tại:

```text
00 Foundations
→ 01 Atomic Structure
→ 02 Chemical Bonding
→ 03 Matter and Phases
→ 04 Chemical Quantities
→ 05 Thermodynamics + 06 Kinetics
→ 07 Equilibrium
→ 08 Acids/Bases + 09 Redox/Electrochemistry
→ 10 Inorganic + 11 Organic
→ 12 Analytical + 13 Biochemistry + 14 Materials
→ 15 Nuclear + 16 Environmental + 17 Laboratory
→ 90 Connections
```

Flow này đủ để người gần như quên Hóa phổ thông đi từ vật chất/phép đo tới các domain chuyên sâu mà không cần một Chemistry library khác.

# Core conceptual gaps đã xử lý

## 01 Atomic Structure / Periodic Trends

`04_periodic_table_and_periodic_trends.md` nối:

```text
electron configuration
→ Zeff / shielding / penetration
→ radius / ionization / affinity / electronegativity
→ oxide acidity/basicity
→ oxidation-state trends
→ inorganic chemistry / materials
```

Đã có second-period anomaly, diagonal relationship, inert-pair effect, transition-metal trends, lanthanide contraction và relativistic effects.

## 02 Chemical Bonding

Chuỗi canonical:

```text
electron bookkeeping
→ Lewis / resonance
→ VSEPR
→ localized VB / hybridization
→ MO / delocalization
→ intermolecular forces
→ bulk properties
```

Lewis, VSEPR, VB, MO và IMF không còn ở mức note nhập môn mỏng.

## 03 Matter and Phases

`gases`, `liquids`, `solids` và `phase_changes_and_phase_diagrams` đã được cân độ sâu.

Chất khí hiện có Maxwell–Boltzmann, collisions/mean free path, ideal-gas reasoning, diffusion/effusion, real-gas deviations, compressibility factor, virial expansion, fugacity và critical behavior.

Chất lỏng, chất rắn và chuyển pha đã có diffusion, viscosity, surface tension, wetting, lattice/defects, phonons/bands, Clapeyron, nucleation và binary phase diagrams.

## 04 Chemical Quantities

Mol được giải thích như cầu nối giữa hạt vi mô và phép đo vĩ mô.

Stoichiometry đã đi xa hơn `gram → mol → gram`, gồm extent of reaction, conversion/yield/selectivity, elemental balance, stoichiometric matrix, null space, flow balance và uncertainty propagation.

`limiting_reagent_and_yield.md` và `solution_concentration.md` ngắn nhưng có ví dụ số, assumptions và mental model nên **không phải file yếu**.

## 05 Thermodynamics

Flow:

```text
internal energy
→ heat / work
→ first law
→ enthalpy
→ entropy
→ Gibbs
→ chemical potential
→ activity / fugacity
→ phase / reaction equilibrium
```

`04_chemical_thermodynamics.md` vừa được language/scope pass lớn. File này hiện giữ đúng vai trò **định nghĩa và xây công cụ nhiệt động cho hệ nhiều thành phần**:

- chemical potential;
- partial molar quantities;
- activity/activity coefficient;
- ionic strength;
- fugacity;
- Raoult/Henry;
- excess properties;
- Gibbs–Duhem;
- phase equilibrium;
- osmosis;
- electrochemical potential;
- nonideal battery electrolyte;
- CALPHAD.

Prose đã chuyển về Việt-first và lỗi LaTeX trong phương trình Nernst đã được sửa.

## 06 Kinetics

Cụm kinetics hiện bao phủ:

- initial-rate method;
- integrated laws;
- nonlinear fitting và residual analysis;
- pseudo-order / fractional / negative order;
- coupled ODE và stiff systems;
- parameter identifiability;
- pre-equilibrium và steady-state approximation;
- KIE/isotope labeling;
- Hammett và Curtin–Hammett;
- Eyring / activation entropy / tunneling;
- diffusion control;
- catalysis và degree of rate control.

## 07 Equilibrium

Flow:

```text
forward/reverse kinetics
→ dynamic equilibrium
→ Q
→ K
→ ΔrG
→ chemical potential
→ mass / charge balance
→ speciation / Gibbs minimization
```

`04_thermodynamics_of_equilibrium.md` vừa được tách scope khỏi `05/04`:

```text
05/04 Chemical Thermodynamics
→ định nghĩa μ, activity, fugacity, nonideality

07/04 Thermodynamics of Equilibrium
→ reaction coordinate / stability
→ K / Q / van't Hoff
→ phase equilibrium / common tangent / spinodal
→ Gibbs minimization
→ speciation / conditional K
→ numerical stability checks
```

Nhờ đó hai chapter hiện bổ sung cho nhau thay vì định nghĩa lại cùng một nội dung.

## 08 Acid–Base

Core hiện có Arrhenius, Brønsted–Lowry, Lewis, activity-based pH, weak/polyprotic systems, buffer capacity, titration mechanisms, equivalence vs endpoint, `Ksp/Qsp`, conditional solubility và complexation/protonation effects.

## 09 Redox / Electrochemistry

Flow:

```text
oxidation state
→ half-reaction bookkeeping
→ galvanic cells
→ Nernst / activity
→ kinetics / overpotential / mass transport
→ electrolysis
→ battery / corrosion / EIS
```

`06_electrochemical_kinetics_and_impedance.md` đã được chuẩn hóa hierarchy và Việt-first, giữ Butler–Volmer, Tafel, RDE/Koutecký–Levich, double layer, Nyquist/Bode, Randles/CPE/Warburg, DRT và failure modes của EIS.

# Language consistency pass

## Organic Chemistry

Các chapter đã pass trực tiếp:

- `01_functional_groups.md`;
- `04_alkanes_alkenes_and_alkynes.md`;
- `06_alcohols_ethers_and_amines.md`.

English được giữ như keyword chuẩn thay vì trở thành ngôn ngữ chính của câu. Không mở thêm reaction catalog chỉ để tăng độ dài.

## Analytical Chemistry

Các chapter đã language/hierarchy pass:

### `03_spectroscopy.md`

Giữ Beer–Lambert, UV–Vis, IR, Raman, NMR, fluorescence, atomic spectroscopy và X-ray; thêm prerequisite links và reasoning examples.

### `04_chromatography.md`

Giữ partition, retention, resolution, plate theory, Van Deemter, GC/HPLC, ion exchange, SEC, affinity, chiral separation và LC–MS; prose Việt-first hơn.

### `05_mass_spectrometry.md`

Giữ EI/CI/ESI/MALDI, quadrupole/TOF/ion trap/Orbitrap/FT-ICR, isotope patterns, MS/MS, proteomics/metabolomics và quantitation.

## Materials / Polymer Chemistry

Các file đã pass:

- `02_polymers.md`;
- `03_semiconductors.md`;
- `04_nanomaterials.md`;
- `05_surface_and_interface_chemistry.md`.

Chúng đã được chuẩn hóa Việt-first nhưng giữ keyword quốc tế cần cho tra cứu. Scope surface chapter cũng được tách khỏi electrochemical kinetics/EIS.

# Prerequisite transition pass

## Inorganic Chemistry

Các chapter `01`–`04` đã được pass trực tiếp gần nhất.

### `01_main_group_chemistry.md`

Đã thêm bridge từ electron configuration, periodic trends, covalent/MO bonding và acid–base trước khi đi nhóm 1→18.

Giữ diagonal relationship, second-period anomaly, inert-pair effect, hypervalency, acid/base trends và industrial links. Language chuyển Việt-first hơn và thêm reasoning cho amphoteric `Al2O3`.

### `02_transition_metals.md`

Đã nối electron configuration, MO, redox và catalysis trước khi dùng d-electron count, spin, color, organometallic mechanisms và metal clusters.

Đã làm rõ:

```text
oxidation state ≠ electron density distribution
catalyst ≠ changed equilibrium
18-electron rule ≠ universal law
redox potential depends on ligand environment
```

### `03_coordination_chemistry.md`

Đã nối Lewis acid–base, Gibbs, equilibrium, MO và redox.

Các điểm được làm rõ gồm chelate effect, conditional formation constants, coupled solubility/speciation, labile vs inert, substitution mechanisms và chelation trade-off trong y học.

### `04_crystal_field_and_ligand_field.md`

Đã nối electron configuration/MO/coordination với spectroscopy và solid-state chemistry.

Bổ sung rõ giới hạn của CFSE, reasoning cho Ni(II) tetrahedral vs square-planar và phân biệt CFT với LFT như hai mức mô hình khác nhau.

`00_inorganic_compounds.md` đã được audit trước và giữ nguyên vì prose/prerequisite tốt. `05_solid_state_and_defect_chemistry.md` đã được depth pass lớn từ trước.

## Biochemistry

### `05_enzymes.md`

Đã link trực tiếp tới Gibbs, kinetics/mechanism, acid–base, coordination chemistry và intermolecular forces.

Đã làm rõ:

```text
steady state ≠ equilibrium
KM ≠ KD nói chung
more enzyme ≠ changed equilibrium
```

### `06_metabolism_and_bioenergetics.md`

Đã nối Gibbs, equilibrium, Nernst/electrochemistry, enzyme kinetics và stoichiometric matrices.

Nhấn mạnh `flux ≠ concentration` và ghép nhiệt động cần ghép hóa học thật.

## Nuclear Chemistry

### `00_atomic_nucleus.md`

Đã nối atoms/isotopes, quantum states và electromagnetic radiation tới binding, liquid-drop/shell models, magic numbers, gamma states và radioactivity.

### `02_nuclear_reactions.md`

Đã nối binding energy, radioactivity, kinetics và reaction-network mathematics.

Bổ sung:

- Q-value numerical example;
- `Q > 0` không đồng nghĩa phản ứng nhanh;
- cross section phụ thuộc năng lượng;
- activation build-up và saturation;
- isotope-production trade-offs;
- stiff reaction networks.

### `03_fission_and_fusion.md`

Đã nối binding energy, radioactive decay và nuclear-reaction kinetics trước khi đi vào chain reaction và fusion.

Đã làm rõ:

```text
k = 1 ≠ “mất kiểm soát”
energy density ≠ system efficiency
fusion ≠ zero radiation/waste
Lawson criterion = reaction-rate + confinement + materials trade-off
```

`01_radioactivity.md` và `04_radiochemistry_and_applications.md` được mở audit lại và giữ nguyên vì đã có quantitative models, mechanism, trade-off và prose chủ yếu là tiếng Việt.

## Environmental Chemistry

Các file `00`–`03` đã có prerequisite pass:

- atmospheric chemistry nối gas/quantum/spectroscopy/kinetics/equilibrium/surface chemistry;
- water chemistry nối acid–base, `Ksp`, Nernst/Eh, coordination, surface và sampling;
- soil chemistry nối water/surface/CEC/redox/reactive transport;
- pollutant/toxic chemistry tổ chức theo hazard → exposure → internal dose → mechanism → fate → risk.

`04_green_chemistry.md` được audit lại và giữ nguyên vì đã có metrics, catalysis/solvent/energy/feedstock trade-offs và lifecycle reasoning.

# Duplicate scope review

## Electrochemistry ↔ Electroanalysis

Đã xử lý:

```text
09/06 electrochemical kinetics + impedance
→ theory / mechanism / EIS model

12/06 electroanalytical methods
→ measurement / calibration / matrix / fouling / uncertainty
```

Butler–Volmer, RDE và EIS không còn được giải thích hai lần với cùng mục tiêu.

## Chemical Thermodynamics ↔ Thermodynamics of Equilibrium

Đã xử lý trong pass mới nhất:

```text
05/04
→ chemical potential / activity / fugacity / nonideality
→ multicomponent thermodynamic tools

07/04
→ use those tools for equilibrium
→ stability / K-Q / phases / speciation / minimization
```

## Analytical Measurement ↔ Laboratory Design/Uncertainty

Đã mở và so trực tiếp. Hiện **không coi là duplicate lớn** vì scope khác nhau:

```text
12/00 measurement_and_sampling
→ analytical evidence chain
→ representative sampling / sample prep / calibration

17/04 experimental_design
→ experimental unit / controls / randomization / blocking / DoE

17/05 error_uncertainty_and_data_analysis
→ metrology / bias / statistics / uncertainty propagation
```

Các khái niệm calibration/uncertainty xuất hiện ở nhiều nơi là cross-domain reuse có chủ ý, không phải ba chapter cạnh tranh cùng mục tiêu.

## Các overlap có chủ ý khác

- activity: thermodynamics định nghĩa; acid–base/electrochemistry áp dụng;
- diffusion: matter giải thích vật lý; kinetics/electrochemistry/environment dùng như transport limit;
- spectroscopy: atomic structure giải thích quantum origin; analytical chemistry giải thích measurement/inference;
- phase equilibrium: matter giới thiệu; thermodynamics/equilibrium xây framework thế hóa học;
- hydrogen bonding: bonding định nghĩa; biochemistry/materials áp dụng.

# Internal links

Global internal-link checker đã được chạy trên GitHub Actions sau khi build Study Shelf. Checker đã kiểm tra toàn bộ 119 file Chemistry và bỏ qua fenced code blocks khi phân tích link.

```text
Chemistry Markdown files: 119
Published Chemistry documents: 119
empty Markdown files: 0
temporary/versioned filenames: 0
duplicate Markdown content: 0
broken internal links: 0
Study Shelf build: pass
```

Hai đường dẫn giả từng bị bắt trong `COVERAGE_AUDIT.md` chỉ là ví dụ cú pháp nằm trong fenced code block, không phải link render thật.

# Examples / mechanism / trade-off

Core chapter quan trọng hiện có ít nhất một hoặc nhiều dạng sau:

- ví dụ định lượng;
- ví dụ suy luận cơ chế;
- counterexample/misconception;
- trade-off thực tế;
- giới hạn của mô hình.

Pass mới nhất bổ sung rõ ở main-group chemistry, coordination chemistry, ligand-field theory, transition metals, nuclear reactions, fission/fusion và equilibrium thermodynamics.

Không kéo dài file đã có reasoning đầy đủ chỉ để tăng số dòng.

# README

`README.md` đã được kiểm tra sau các pass gần đây.

Hiện cây canonical, dependency graph, learning path và liên kết tới `COVERAGE_AUDIT.md` vẫn phản ánh đúng cấu trúc. Không chỉnh README chỉ để tạo commit.

# Trạng thái pre-merge cuối

```text
không có file rỗng/skeleton quan trọng       ✓
không còn core chapter mỏng bất hợp lý       ✓
ngôn ngữ chủ yếu là tiếng Việt               ✓
prerequisite flow tới specialized domains     ✓
không còn duplicate lớn gây nhiễu             ✓
examples/mechanisms đủ cho chapter nền        ✓
README phản ánh đúng cấu trúc                 ✓
global internal links đã được kiểm tra        ✓
Study Shelf build + Chemistry publication     ✓
branch cũ đã gom/xóa                          ✓
```

Pre-merge audit xác nhận toàn bộ 119 tài liệu Chemistry được đưa vào Study Shelf khi prefix `chemistry` được allow-list.

Có một blocker tồn tại sẵn trên `main` không thuộc Chemistry: publication manifest còn hai `allowedDocuments` trỏ tới file Java/CSS đã không tồn tại. Trong pre-merge audit, hai entry stale này chỉ được bỏ qua trong runner; chúng không được đưa vào thay đổi Chemistry.

Chemistry Library hiện **content/link/build-ready cho việc merge**. Blocker manifest nói trên có thể làm workflow Pages toàn repo thất bại độc lập với Chemistry cho tới khi workstream tương ứng sửa nó.