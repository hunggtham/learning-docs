# Audit phạm vi, độ sâu và chất lượng của Thư viện Vật lý

Tệp này theo dõi **coverage, dependency, độ sâu và chất lượng trình bày** của Physics Knowledge Library. Mục tiêu là giữ core chắc, bridge có chủ đích và tránh mở rộng specialization vô hạn.

## Trạng thái hiện tại

Thư viện hiện có **88 file Markdown**, gồm các chapter nội dung, navigation, glossary, problem-solving guide và quality audit. Nội dung được tổ chức dưới canonical path:

```text
physics/
```

Không có các bản `_updated`, `_final`, `_version2` hay file duplicate theo naming pattern trong canonical tree.

## Tiêu chuẩn chapter đủ sâu

Một chapter core nên có phần lớn các lớp sau:

1. Hiện tượng hoặc câu hỏi vật lý tạo động cơ.
2. Định nghĩa đại lượng và ý nghĩa vật lý.
3. Hệ, bậc tự do, giả định và scale đang giữ lại.
4. Công thức cốt lõi cùng derivation hoặc reasoning khi hợp lý.
5. Unit, sign, limiting case và order-of-magnitude checks.
6. Worked reasoning hoặc ví dụ định lượng.
7. Boundary/initial conditions nếu relevant.
8. Domain of validity và dấu hiệu model thất bại.
9. Common Misconceptions.
10. Knowledge Connection tới prerequisite và lớp kiến thức kế tiếp.

Với chapter bridge, cần chỉ ra rõ cấu trúc toán học lặp lại như eigenvalue, Fourier, tensor, symmetry, conservation, response, stochastic process hoặc inverse problem.

Độ dài chỉ là tín hiệu audit, không phải tiêu chí quyết định. File ngắn nhưng giải thích đủ cơ chế có thể tốt hơn file dài chỉ liệt kê công thức.

# Coverage theo domain

## 00 — Foundations và measurement: mạnh

Physical thinking, measurement/uncertainty, vector/frame, mathematical language, symmetry/scaling và PDE/Green/tensor tạo prerequisite cho toàn library. First-principles workflow đã bao gồm system boundary, degrees of freedom, scale analysis, controlled approximation, dimensional checks, forward/inverse problem, falsifiability và model discrepancy.

**Trạng thái:** không còn lỗ core lớn.

## 01 — Mechanics: mạnh

Dependency chính:

```text
kinematics
→ Newton dynamics
→ common forces
→ work/energy + momentum
→ rotation + gravity + statics
→ analytical mechanics
→ nonlinear/canonical/rotating-frame extensions
```

Coverage gồm force modelling, free-body reasoning, work–energy, momentum, rigid-body rotation, gravitation/orbits, elasticity, Lagrange/Hamilton, chaos, Hamilton–Jacobi và non-inertial frames.

**Trạng thái:** strong undergraduate core + advanced bridge.

## 02 — Oscillations và waves: mạnh

SHM, damping, driven response, resonance, wave equation, standing waves, Fourier, sound, dispersion và normal modes đều có. Boundary conditions và dispersion limits đã được làm rõ.

**Trạng thái:** strong core/bridge.

## 03 — Continuum, fluids và transport: mạnh

Hydrostatics, buoyancy, continuity, Bernoulli, viscosity, Reynolds, Poiseuille, boundary layer và Navier–Stokes đã có. Capillarity, transport, turbulence/rheology và continuum stress tensor nối conservation law với constitutive relation.

**Trạng thái:** strong core/bridge.

## 04 — Thermodynamics và Statistical Physics: mạnh

Thermodynamics, entropy, phase transitions, ensembles, Boltzmann equation, stochastic nonequilibrium, critical phenomena/RG và linear response/FDT tạo chuỗi micro ↔ macro ↔ fluctuations ↔ response.

**Trạng thái:** strong undergraduate + selected graduate bridge.

## 05 — Electricity, circuits, magnetism và electromagnetism: mạnh

Electrostatics, capacitance, DC/AC circuits, magnetism/induction, Maxwell, transmission lines, gauge/potentials và fields in matter đều đã có. Boundary-value/multipole, radiation/scattering/antenna và relativistic electrodynamics bổ sung selected depth.

Transmission-line chapter đã có telegrapher derivation, characteristic impedance, reflection/VSWR, lossy line, waveguide modes và signal-integrity reasoning.

**Trạng thái:** strong calculus-based university coverage.

## 06 — Optics: mạnh

Geometric optics, wave optics, photon/laser/coherence, polarization/dispersion/nonlinear optics và Fourier imaging đều có. Wave-optics và laser chapters đã có derivation giao thoa/nhiễu xạ, coherence, PSF/OTF, Einstein coefficients, rate equations, cavity threshold, linewidth/Q và mode locking.

**Trạng thái:** strong core/bridge.

## 07 — Relativity: mạnh

Special relativity có invariant interval, Lorentz transformation, proper time, four-vector, four-momentum và relativistic dynamics. General relativity có equivalence principle, metric, geodesic, curvature, geodesic deviation, weak-field limit, Einstein equation, Schwarzschild, lensing, Shapiro delay, gravitational waves và Friedmann bridge.

**Trạng thái:** strong SR + solid GR bridge.

## 08 — Quantum Physics: mạnh

Foundations → model systems → spin/angular momentum → measurement/decoherence → approximation → identical particles → time-dependent/scattering → symmetry/path-integral tạo sequence đầy đủ.

Model systems và spin chapters đã được nâng với boundary-condition derivation, tunneling current, ladder operators, SU(2), Bloch sphere, Stern–Gerlach, Larmor precession, Clebsch–Gordan và selection rules. Approximation chapter đã có perturbation, degeneracy, variational, adiabatic/Born–Oppenheimer, WKB, mean-field và EFT reasoning.

**Trạng thái:** strong undergraduate + selected advanced bridge.

## 09 — Atomic, molecular, nuclear và particle: mạnh

Atomic structure/spectroscopy, molecular modes, nuclear models/decay/reactions, radiation detection và Standard Model đều có. Detector chapter đã có dead time, pile-up, energy resolution, efficiency, response function, background và calibration.

**Trạng thái:** strong bridge; không mở full graduate QFT/nuclear-many-body trong scope này.

## 10 — Condensed matter, materials, electronics và plasma: mạnh

Band theory, reciprocal lattice, Brillouin zone, DOS, effective mass, semiconductor electrostatics, P–N junction, MOS capacitor, MOSFET scaling, carrier transport, Hall, magnetism, superconductivity và plasma đều có. Các extension về phonons/defects/topological matter, BEC/superfluidity và Berry/Quantum Hall bổ sung selected depth.

**Trạng thái:** strong core/bridge.

## 11 — Astrophysics và cosmology: mạnh

Stellar structure/evolution, compact objects, galaxies/cosmology, observational astrophysics/radiative transfer, early universe/dark components và gravitational structure formation đều có. Cosmology core đã có FLRW/Friedmann, critical density, density parameters, distance measures, CMB/BAO, structure growth, dark-energy parameterization và parameter inference.

**Trạng thái:** strong bridge between theory and observation.

## 12 — Experiment, signals, computation và inference: mạnh

Calibration, uncertainty, sampling, PSD/noise, numerical ODE/PDE, Monte Carlo, inverse problems và statistical inference đã có. Đây là lớp kiểm chứng model bằng dữ liệu, không chỉ là phần phụ của lý thuyết.

**Trạng thái:** strong methodological layer.

# Dependency audit

Dependency tổng thể:

```text
physical thinking + measurement + math
→ mechanics
→ oscillations/waves
→ continuum/thermo
→ electromagnetism
→ optics/relativity
→ quantum
→ atomic/nuclear/condensed matter
→ astrophysics/cosmology
```

Experiment/computation/inference chạy song song và quay lại kiểm chứng mọi domain. Các chapter advanced được đặt sau prerequisite hợp lý và không tạo dependency vòng bắt buộc.

# Prose-quality audit

Nguyên tắc toàn library:

```text
Vietnamese explanation first
+ English keyword khi cần tra cứu
+ không giữ cả câu English song song
+ không đổi equations/derivation nếu physics không sai
```

Các prose debt lớn từng tồn tại ở momentum, waves/Fourier, fluids, thermodynamics, quantum foundations, wave optics, laser/coherence và transmission lines đã được normalize.

# Structural checklist trước merge

Canonical tree đã được cleanup theo các tiêu chí:

- một canonical path `physics/`;
- không có file tạm theo pattern `_updated`, `_final`, `_version2`;
- numbering collision đã được chuẩn hóa;
- README chỉ link tới canonical filenames;
- glossary/navigation trỏ theo cấu trúc canonical;
- hai archive variants từng có malformed control character không được dùng trong canonical tree;
- root README và Study Library config chỉ thêm integration cần thiết cho Physics.

GitHub Actions không có PR-triggered run cho commit canonical tại thời điểm audit, nên build validation cần dựa vào site workflow sau khi mở PR/merge. Nội dung Markdown không phụ thuộc binary/build artifact riêng.

# Nguyên tắc dừng

Core Physics được xem là đủ cho Knowledge Library tổng quát khi domain có:

```text
core concepts
+ first-principles reasoning
+ derivation hoặc mechanism
+ worked reasoning
+ assumptions
+ boundary/initial conditions khi relevant
+ model limits
+ misconceptions
+ knowledge connections
```

Các vòng tiếp theo nên tập trung vào lỗi cụ thể hoặc cập nhật khoa học cần thiết, không tăng số chapter chỉ để tăng coverage.