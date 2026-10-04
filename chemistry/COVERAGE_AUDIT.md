# Thư viện kiến thức Hóa học — Kiểm tra độ bao phủ

> **Mạch đọc:** [README](./README.md) là owner của **Thư viện kiến thức Hóa học — Kiểm tra độ bao phủ**. Route audit đi từ trạng thái canonical và bản đồ owner → coverage theo domain/chapter → prerequisite, link và ngôn ngữ → chiều sâu, trùng lặp và rủi ro phát hành; kết quả phải quay lại README để cập nhật thứ tự ưu tiên thay vì chỉ ghi nhận số lượng file.

> Tài liệu này theo dõi **độ bao phủ khái niệm, quan hệ phụ thuộc, tính nhất quán ngôn ngữ, mức độ trùng lặp và chất lượng chiều sâu** của Chemistry thư viện kiến thức (knowledge library / 지식 라이브러리). Đây không phải bản tóm tắt để học nhanh. Nội dung Chemistry hiện là chuẩn gốc (canonical / 정본) trên `main`; các tên branch cũ chỉ được giữ trong lịch sử Git.

## Trạng thái chuẩn gốc (canonical / 정본)

Chemistry đã hoàn tất pre-merge kiểm tra (audit / 감사) và được quản lý trực tiếp trên `main`. Mọi kiểm tra (audit / 감사) mới phải cập nhật ngày rà soát (review / 검토), coverage, phụ thuộc (dependency / 의존성) luồng (flow / 흐름) và các link chuẩn gốc (canonical / 정본) tại đây.

> **Chuyển mạch:** **Trạng thái canonical** xác định owner và evidence; **Audit priority** dùng chúng để mở **Atomic structure/Periodic Trends** theo prerequisite thật.

## Thứ tự ưu tiên kiểm tra (audit / 감사)

Audit bắt đầu từ những dependency có thể làm sai nhiều chapter phía sau. Đọc các bước theo thứ tự này để hiểu vì sao một gap về nguyên tử, năng lượng hoặc cân bằng được ưu tiên trước một chủ đề ứng dụng hẹp.

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

Kích thước tệp (file / 파일) chỉ là tín hiệu. Chapter ngắn nhưng phạm vi hẹp và lập luận (reasoning / 추론) đầy đủ không cần kéo dài chỉ để cân số dòng.

# Trạng thái cấu trúc

Các lĩnh vực (domain / 도메인) từ `00` tới `17` đã được quét theo siêu dữ liệu (metadata / 메타데이터) kích thước và mở nội dung các ứng viên bất thường.

Hiện **không phát hiện tệp (file / 파일) chuẩn gốc (canonical / 정본) rỗng hoặc skeleton quan trọng**.

Các tệp (file / 파일) `90_connections` ngắn hơn chapter textbook chính nhưng có phạm vi (scope / 범위) khác: chúng là lớp kết nối kiến thức, không phải textbook độc lập. Không coi chúng là skeleton chỉ vì kích thước nhỏ hơn.

Phụ thuộc (dependency / 의존성) luồng (flow / 흐름) hiện tại:

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

Luồng (flow / 흐름) này đủ để người gần như quên Hóa phổ thông đi từ vật chất/phép đo tới các lĩnh vực (domain / 도메인) chuyên sâu mà không cần một Chemistry thư viện (library / 라이브러리) khác.

# Cốt lõi (core / 핵심) conceptual gaps đã xử lý

> **Chuyển mạch:** **Atomic structure/Periodic Trends** đặt electron và periodicity; **Chemical Bonding** dùng chúng để giải thích liên kết và năng lượng.

## 01 Atomic cấu trúc (structure / 구조) / Periodic Trends

`04_periodic_table_and_periodic_trends.md` nối:

```text
electron configuration
→ Zeff / shielding / penetration
→ radius / ionization / affinity / electronegativity
→ oxide acidity/basicity
→ oxidation-state trends
→ inorganic chemistry / materials
```

Đã có second-period anomaly, diagonal relationship, inert-pair tác động (effect / 효과), transition-metal trends, lanthanide contraction và relativistic effects.

> **Chuyển mạch:** **Chemical Bonding** nối electron với cấu trúc chất; **Matter and Phases** mở rộng sang bulk properties và phase behavior.

## 02 Chemical Bonding

Chuỗi chuẩn gốc (canonical / 정본):

```text
electron bookkeeping
→ Lewis / resonance
→ VSEPR
→ localized VB / hybridization
→ MO / delocalization
→ intermolecular forces
→ bulk properties
```

Lewis, VSEPR, VB, MO và IMF không còn ở mức ghi chú (note / 노트) nhập môn mỏng.

> **Chuyển mạch:** **Matter and Phases** mô tả state và transition; **Chemical Quantities** biến mô tả đó thành mol, concentration và stoichiometry.

## 03 Matter and Phases

`gases`, `liquids`, `solids` và `phase_changes_and_phase_diagrams` đã được cân độ sâu.

Chất khí hiện có Maxwell–Boltzmann, collisions/mean free đường dẫn (path / 경로), ideal-gas lập luận (reasoning / 추론), diffusion/effusion, real-gas deviations, compressibility factor, virial expansion, fugacity và trọng yếu (critical / 중요) hành vi (behavior / 동작).

Chất lỏng, chất rắn và chuyển pha đã có diffusion, viscosity, surface tension, wetting, lattice/defects, phonons/bands, Clapeyron, nucleation và nhị phân (binary / 이진) phase diagrams.

> **Chuyển mạch:** **Chemical Quantities** khóa accounting của reaction; **Thermodynamics** giải thích energy, entropy và spontaneity của reaction đó.

## 04 Chemical Quantities

Mol được giải thích như cầu nối giữa hạt vi mô và phép đo vĩ mô.

Stoichiometry đã đi xa hơn `gram → mol → gram`, gồm extent of reaction, conversion/yield/selectivity, elemental balance, stoichiometric ma trận (matrix / 행렬), null không gian (space / 공간), luồng (flow / 흐름) balance và bất định (uncertainty / 불확실성) propagation.

`limiting_reagent_and_yield.md` và `solution_concentration.md` ngắn nhưng có ví dụ số, các giả định (assumptions / 가정들) và mô hình tư duy (mental model / 사고 모델) nên **không phải tệp (file / 파일) yếu**.

> **Chuyển mạch:** **Thermodynamics** nói reaction có thể đi đâu; **Kinetics** nói nó đi nhanh thế nào và qua mechanism nào.

## 05 Thermodynamics

Luồng (flow / 흐름):

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

`04_chemical_thermodynamics.md` vừa được ngôn ngữ (language / 언어)/phạm vi (scope / 범위) pass lớn. tệp (file / 파일) này hiện giữ đúng vai trò **định nghĩa và xây công cụ nhiệt động cho hệ nhiều thành phần**:

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

> **Chuyển mạch:** **Kinetics** cung cấp rate và mechanism; **Equilibrium** đặt rate outcome vào trạng thái cân bằng và constraint.

## 06 Kinetics

Cụm kinetics hiện bao phủ:

- initial-rate phương thức (method / 메서드);
- integrated laws;
- nonlinear fitting và residual phân tích (analysis / 분석);
- pseudo-order / fractional / negative thứ tự (order / 순서);
- coupled ODE và stiff các hệ thống (systems / 시스템들);
- parameter identifiability;
- pre-equilibrium và steady-state approximation;
- KIE/isotope labeling;
- Hammett và Curtin–Hammett;
- Eyring / activation entropy / tunneling;
- diffusion điều khiển (control / 제어);
- catalysis và degree of tỷ lệ (rate / 비율) điều khiển (control / 제어).

> **Chuyển mạch:** **Equilibrium** khóa reaction state; **Acid–base** áp dụng equilibrium cho proton transfer, pH và buffer.

## 07 Equilibrium

Luồng (flow / 흐름):

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

`04_thermodynamics_of_equilibrium.md` vừa được tách phạm vi (scope / 범위) khỏi `05/04`:

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

> **Chuyển mạch:** **Acid–base** làm rõ charge và potential trong dung dịch; **Redox/Electrochemistry** mở cùng logic sang electron transfer và cell.

## 08 Acid–cơ sở (base / 기반)

Cốt lõi (core / 핵심) hiện có Arrhenius, Brønsted–Lowry, Lewis, activity-based pH, weak/polyprotic các hệ thống (systems / 시스템들), buffer sức chứa (capacity / 용량), titration mechanisms, equivalence vs endpoint, `Ksp/Qsp`, conditional solubility và complexation/protonation effects.

> **Chuyển mạch:** **Redox/Electrochemistry** nối electron flow với energy; **Organic Chemistry** dùng structure và mechanism để mô tả carbon systems.

## 09 Redox / Electrochemistry

Luồng (flow / 흐름):

```text
oxidation state
→ half-reaction bookkeeping
→ galvanic cells
→ Nernst / activity
→ kinetics / overpotential / mass transport
→ electrolysis
→ battery / corrosion / EIS
```

`06_electrochemical_kinetics_and_impedance.md` đã được chuẩn hóa hierarchy và Việt-first, giữ Butler–Volmer, Tafel, RDE/Koutecký–Levich, double tầng (layer / 계층), Nyquist/Bode, Randles/CPE/Warburg, DRT và thất bại (failure / 실패) modes của EIS.

# Ngôn ngữ (language / 언어) consistency pass

> **Chuyển mạch:** **Organic Chemistry** đặt reaction mechanism lên molecular structure; **Analytical Chemistry** đo identity, amount và uncertainty của sản phẩm.

## Organic Chemistry

Các chapter đã pass trực tiếp:

- `01_functional_groups.md`;
- `04_alkanes_alkenes_and_alkynes.md`;
- `06_alcohols_ethers_and_amines.md`.

English được giữ như từ khóa (keyword / 키워드) chuẩn thay vì trở thành ngôn ngữ chính của câu. Không mở thêm reaction danh mục (catalog / 카탈로그) chỉ để tăng độ dài.

> **Chuyển mạch:** **Analytical Chemistry** cung cấp measurement evidence; **Materials/Polymer Chemistry** chuyển evidence đó vào structure–property relationship.

## Analytical Chemistry

Các chapter đã ngôn ngữ (language / 언어)/hierarchy pass:

### `03_spectroscopy.md`

Giữ Beer–Lambert, UV–Vis, IR, Raman, NMR, fluorescence, atomic spectroscopy và X-ray; thêm prerequisite links và lập luận (reasoning / 추론) examples.

### `04_chromatography.md`

Giữ partition, retention, resolution, plate lý thuyết (theory / 이론), Van Deemter, GC/HPLC, ion exchange, SEC, affinity, chiral separation và LC–MS; prose Việt-first hơn.

### `05_mass_spectrometry.md`

Giữ EI/CI/ESI/MALDI, quadrupole/TOF/ion trap/Orbitrap/FT-ICR, isotope patterns, MS/MS, proteomics/metabolomics và quantitation.

> **Chuyển mạch:** **Materials/Polymer Chemistry** nối measurement với bulk performance; **Inorganic Chemistry** bổ sung coordination, solids và elements.

## Materials / Polymer Chemistry

Các tệp (file / 파일) đã pass:

- `02_polymers.md`;
- `03_semiconductors.md`;
- `04_nanomaterials.md`;
- `05_surface_and_interface_chemistry.md`.

Chúng đã được chuẩn hóa Việt-first nhưng giữ từ khóa (keyword / 키워드) quốc tế cần cho tra cứu. phạm vi (scope / 범위) surface chapter cũng được tách khỏi electrochemical kinetics/EIS.

# Prerequisite chuyển tiếp (transition / 전이) pass

> **Chuyển mạch:** **Inorganic Chemistry** giải thích elements và coordination; **Biochemistry** đặt chúng vào molecules, pathways và living systems.

## Inorganic Chemistry

Các chapter `01`–`04` đã được pass trực tiếp gần nhất.

### `01_main_group_chemistry.md`

Đã thêm cầu nối (bridge / 브리지) từ electron cấu hình (configuration / 구성), periodic trends, covalent/MO bonding và acid–cơ sở (base / 기반) trước khi đi nhóm 1→18.

Giữ diagonal relationship, second-period anomaly, inert-pair tác động (effect / 효과), hypervalency, acid/cơ sở (base / 기반) trends và industrial links. ngôn ngữ (language / 언어) chuyển Việt-first hơn và thêm lập luận (reasoning / 추론) cho amphoteric `Al2O3`.

### `02_transition_metals.md`

Đã nối electron cấu hình (configuration / 구성), MO, redox và catalysis trước khi dùng d-electron count, spin, color, organometallic mechanisms và metal clusters.

Đã làm rõ:

```text
oxidation state ≠ electron density distribution
catalyst ≠ changed equilibrium
18-electron rule ≠ universal law
redox potential depends on ligand environment
```

### `03_coordination_chemistry.md`

Đã nối Lewis acid–cơ sở (base / 기반), Gibbs, equilibrium, MO và redox.

Các điểm được làm rõ gồm chelate tác động (effect / 효과), conditional formation constants, coupled solubility/speciation, labile vs inert, substitution mechanisms và chelation sự đánh đổi (trade-off / 트레이드오프) trong y học.

### `04_crystal_field_and_ligand_field.md`

Đã nối electron cấu hình (configuration / 구성)/MO/coordination với spectroscopy và solid-state chemistry.

Bổ sung rõ giới hạn của CFSE, lập luận (reasoning / 추론) cho Ni(II) tetrahedral vs square-planar và phân biệt CFT với LFT như hai mức mô hình khác nhau.

`00_inorganic_compounds.md` đã được kiểm tra (audit / 감사) trước và giữ nguyên vì prose/prerequisite tốt. `05_solid_state_and_defect_chemistry.md` đã được độ sâu (depth / 깊이) pass lớn từ trước.

> **Chuyển mạch:** **Biochemistry** nối chemistry với biological function; **Nuclear Chemistry** chuyển mechanism sang isotope, decay và radiation.

## Biochemistry

### `05_enzymes.md`

Đã link trực tiếp tới Gibbs, kinetics/cơ chế (mechanism / 메커니즘), acid–cơ sở (base / 기반), coordination chemistry và intermolecular forces.

Đã làm rõ:

```text
steady state ≠ equilibrium
KM ≠ KD nói chung
more enzyme ≠ changed equilibrium
```

### `06_metabolism_and_bioenergetics.md`

Đã nối Gibbs, equilibrium, Nernst/electrochemistry, enzyme kinetics và stoichiometric matrices.

Nhấn mạnh `flux ≠ concentration` và ghép nhiệt động cần ghép hóa học thật.

> **Chuyển mạch:** **Nuclear Chemistry** cung cấp source–decay evidence; **Environmental Chemistry** đánh giá transport, exposure và risk trong môi trường.

## Nuclear Chemistry

### `00_atomic_nucleus.md`

Đã nối atoms/isotopes, quantum states và electromagnetic radiation tới binding, liquid-drop/shell các mô hình (models / 모델들), magic numbers, gamma states và radioactivity.

### `02_nuclear_reactions.md`

Đã nối binding năng lượng (energy / 에너지), radioactivity, kinetics và reaction-network mathematics.

Bổ sung:

- Q-value numerical example;
- `Q > 0` không đồng nghĩa phản ứng nhanh;
- cross section phụ thuộc năng lượng;
- activation build-up và saturation;
- isotope-production trade-offs;
- stiff reaction networks.

### `03_fission_and_fusion.md`

Đã nối binding năng lượng (energy / 에너지), radioactive decay và nuclear-reaction kinetics trước khi đi vào chuỗi (chain / 사슬) reaction và fusion.

Đã làm rõ:

```text
k = 1 ≠ “mất kiểm soát”
energy density ≠ system efficiency
fusion ≠ zero radiation/waste
Lawson criterion = reaction-rate + confinement + materials trade-off
```

`01_radioactivity.md` và `04_radiochemistry_and_applications.md` được mở kiểm tra (audit / 감사) lại và giữ nguyên vì đã có quantitative các mô hình (models / 모델들), cơ chế (mechanism / 메커니즘), sự đánh đổi (trade-off / 트레이드오프) và prose chủ yếu là tiếng Việt.

> **Chuyển mạch:** **Environmental Chemistry** nối mechanism với exposure evidence; **Electrochemistry ↔ Electroanalysis** quay lại đo signal, interface và concentration.

## Environmental Chemistry

Các tệp (file / 파일) `00`–`03` đã có prerequisite pass:

- atmospheric chemistry nối gas/quantum/spectroscopy/kinetics/equilibrium/surface chemistry;
- water chemistry nối acid–cơ sở (base / 기반), `Ksp`, Nernst/Eh, coordination, surface và sampling;
- soil chemistry nối water/surface/CEC/redox/reactive vận chuyển (transport / 전송);
- pollutant/toxic chemistry tổ chức theo hazard → exposure → nội bộ (internal / 내부) dose → cơ chế (mechanism / 메커니즘) → fate → rủi ro (risk / 위험).

`04_green_chemistry.md` được kiểm tra (audit / 감사) lại và giữ nguyên vì đã có metrics, catalysis/solvent/năng lượng (energy / 에너지)/feedstock trade-offs và vòng đời (lifecycle / 생명주기) lập luận (reasoning / 추론).

# Duplicate phạm vi (scope / 범위) rà soát (review / 검토)

> **Chuyển mạch:** **Electrochemistry/Electroanalysis** khóa measurement và potential; **Thermodynamics of Equilibrium** giải thích energy và equilibrium constraint.

## Electrochemistry ↔ Electroanalysis

Đã xử lý:

```text
09/06 electrochemical kinetics + impedance
→ theory / mechanism / EIS model

12/06 electroanalytical methods
→ measurement / calibration / matrix / fouling / uncertainty
```

Butler–Volmer, RDE và EIS không còn được giải thích hai lần với cùng mục tiêu.

> **Chuyển mạch:** **Thermodynamics/Equilibrium** khóa model và assumptions; **Analytical measurement/lab design** kiểm tra model bằng uncertainty và calibration.

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

> **Chuyển mạch:** Ở chặng này của **Thư viện kiến thức Hóa học — Kiểm tra độ bao phủ**, **Chemical Thermodynamics ↔ Thermodynamics of Equilibrium** cho ta quy tắc; **Analytical đo lường (measurement / 측정) ↔ Laboratory thiết kế (design / 설계)/bất định (uncertainty / 불확실성)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Các overlap có chủ ý khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Analytical đo lường (measurement / 측정) ↔ Laboratory thiết kế (design / 설계)/bất định (uncertainty / 불확실성)

Đã mở và so trực tiếp. Hiện **không coi là duplicate lớn** vì phạm vi (scope / 범위) khác nhau:

```text
12/00 measurement_and_sampling
→ analytical evidence chain
→ representative sampling / sample prep / calibration

17/04 experimental_design
→ experimental unit / controls / randomization / blocking / DoE

17/05 error_uncertainty_and_data_analysis
→ metrology / bias / statistics / uncertainty propagation
```

Các khái niệm calibration/bất định (uncertainty / 불확실성) xuất hiện ở nhiều nơi là cross-domain reuse có chủ ý, không phải ba chapter cạnh tranh cùng mục tiêu.

> **Chuyển mạch:** **Analytical measurement/lab design** khép coverage bằng evidence, uncertainty và owner; các overlap còn lại được giữ như link có chủ đích.

## Các overlap có chủ ý khác

Những overlap dưới đây không phải nội dung trùng lặp cần xóa. Chúng là các khái niệm được định nghĩa ở một chapter rồi dùng lại trong domain khác, nên người học cần theo mũi tên để biết phần nào là nền và phần nào là ứng dụng.

- activity: thermodynamics định nghĩa; acid–base/electrochemistry áp dụng;
- diffusion: matter giải thích vật lý; kinetics/electrochemistry/environment dùng như transport limit;
- spectroscopy: atomic structure giải thích quantum origin; analytical chemistry giải thích measurement/inference;
- phase equilibrium: matter giới thiệu; thermodynamics/equilibrium xây framework thế hóa học;
- hydrogen bonding: bonding định nghĩa; biochemistry/materials áp dụng.

# Nội bộ (internal / 내부) links

Toàn cục (global / 전역) internal-link checker đã được chạy trên GitHub Actions sau khi bản dựng (build / 빌드) Study Shelf. Checker đã kiểm tra toàn bộ 119 tệp (file / 파일) Chemistry và bỏ qua fenced mã (code / 코드) blocks khi phân tích link.

```text
Chemistry Markdown files: 119
Published Chemistry documents: 119
empty Markdown files: 0
temporary/versioned filenames: 0
duplicate Markdown content: 0
broken internal links: 0
Study Shelf build: pass
```

Hai đường dẫn giả từng bị bắt trong `COVERAGE_AUDIT.md` chỉ là ví dụ cú pháp nằm trong fenced mã (code / 코드) khối (block / 블록), không phải link kết xuất (render / 렌더링) thật.

# Examples / cơ chế (mechanism / 메커니즘) / sự đánh đổi (trade-off / 트레이드오프)

Cốt lõi (core / 핵심) chapter quan trọng hiện có ít nhất một hoặc nhiều dạng sau:

- ví dụ định lượng;
- ví dụ suy luận cơ chế;
- counterexample/misconception;
- sự đánh đổi (trade-off / 트레이드오프) thực tế;
- giới hạn của mô hình.

Pass mới nhất bổ sung rõ ở main-group chemistry, coordination chemistry, ligand-field lý thuyết (theory / 이론), chuyển tiếp (transition / 전이) metals, nuclear reactions, fission/fusion và equilibrium thermodynamics.

Không kéo dài tệp (file / 파일) đã có lập luận (reasoning / 추론) đầy đủ chỉ để tăng số dòng.

# README

`README.md` đã được kiểm tra sau các pass gần đây.

Hiện cây chuẩn gốc (canonical / 정본), phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), lộ trình học (learning path / 학습 경로) và liên kết tới `COVERAGE_AUDIT.md` vẫn phản ánh đúng cấu trúc. Không chỉnh README chỉ để tạo lần ghi nhận (commit / 커밋).

# Trạng thái pre-merge cuối

Đây là bước chốt trước khi hợp nhất branch: các tiêu chí cấu trúc, ngôn ngữ, prerequisite, ví dụ và liên kết phải được kiểm tra cùng nhau. Bảng dưới đây ghi trạng thái kiểm chứng, không thay thế việc đọc các gap còn lại.

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
canonical content đã ở trên main             ✓
```

Pre-merge kiểm tra (audit / 감사) xác nhận toàn bộ 119 tài liệu Chemistry được đưa vào Study Shelf khi prefix `chemistry` được allow-list.

Chemistry thư viện (library / 라이브러리) hiện **content/link/build-ready trên main**. Các thay đổi sau này chỉ cần cập nhật trực tiếp chuẩn gốc (canonical / 정본) content và kiểm tra (audit / 감사) bản ghi (record / 레코드), không cần duy trì một branch chuẩn gốc (canonical / 정본) riêng.

Chemistry Library hiện **content/link/build-ready cho việc merge**. Blocker manifest nói trên có thể làm workflow Pages toàn repo thất bại độc lập với Chemistry cho tới khi workstream tương ứng sửa nó.

> **Bàn giao:** Sau **Các overlap có chủ ý khác**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
