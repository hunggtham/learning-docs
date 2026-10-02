# Kiểm tra (audit / 감사) phạm vi, độ sâu và chất lượng của Thư viện Vật lý

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Coverage audit phạm vi, độ sâu và chất lượng thư viện Vật lý**. Route đi từ inventory/owner → link/depth checks → conceptual coverage → language/source checks → remediation priorities, để audit dẫn tới phần cần sửa.

Tệp này theo dõi **coverage, phụ thuộc (dependency / 의존성), độ sâu và chất lượng trình bày** của Physics thư viện kiến thức (knowledge library / 지식 라이브러리). Mục tiêu là giữ cốt lõi (core / 핵심) chắc, cầu nối (bridge / 브리지) có chủ đích và tránh mở rộng specialization vô hạn.

## Trạng thái hiện tại

Thư viện hiện có **88 tệp (file / 파일) Markdown**, gồm các chapter nội dung, điều hướng (navigation / 내비게이션), glossary, problem-solving guide và chất lượng (quality / 품질) kiểm tra (audit / 감사). Nội dung được tổ chức dưới chuẩn gốc (canonical / 정본) đường dẫn (path / 경로):

```text
physics/
```

Không có các bản `_updated`, `_final`, `_version2` hay tệp (file / 파일) duplicate theo naming mẫu (pattern / 패턴) trong chuẩn gốc (canonical / 정본) cây (tree / 트리).

> **Chuyển mạch:** Trong **Kiểm tra (audit / 감사) phạm vi, độ sâu và chất lượng của Thư viện Vật lý**, **Tiêu chuẩn chapter đủ sâu** tiếp nhận điểm tựa từ **Trạng thái hiện tại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **00 — Foundations và đo lường (measurement / 측정): mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tiêu chuẩn chapter đủ sâu

Một chapter cốt lõi (core / 핵심) nên có phần lớn các lớp sau:

1. Hiện tượng hoặc câu hỏi vật lý tạo động cơ.
2. Định nghĩa đại lượng và ý nghĩa vật lý.
3. Hệ, bậc tự do, giả định và quy mô (scale / 규모) đang giữ lại.
4. Công thức cốt lõi cùng derivation hoặc lập luận (reasoning / 추론) khi hợp lý.
5. đơn vị (unit / 단위), sign, limiting trường hợp (case / 사례) và order-of-magnitude checks.
6. Worked lập luận (reasoning / 추론) hoặc ví dụ định lượng.
7. ranh giới (boundary / 경계)/initial conditions nếu relevant.
8. lĩnh vực (domain / 도메인) of validity và dấu hiệu mô hình (model / 모델) thất bại.
9. dùng chung (common / 공통) Misconceptions.
10. liên kết kiến thức (knowledge connection / 지식 연결) tới prerequisite và lớp kiến thức kế tiếp.

Với chapter cầu nối (bridge / 브리지), cần chỉ ra rõ cấu trúc toán học lặp lại như eigenvalue, Fourier, tensor, symmetry, conservation, phản hồi (response / 응답), stochastic tiến trình (process / 프로세스) hoặc inverse bài toán (problem / 문제).

Độ dài chỉ là tín hiệu kiểm tra (audit / 감사), không phải tiêu chí quyết định. tệp (file / 파일) ngắn nhưng giải thích đủ cơ chế có thể tốt hơn tệp (file / 파일) dài chỉ liệt kê công thức.

# Coverage theo lĩnh vực (domain / 도메인)

> **Chuyển mạch:** Ở chặng này của **Kiểm tra (audit / 감사) phạm vi, độ sâu và chất lượng của Thư viện Vật lý**, **Tiêu chuẩn chapter đủ sâu** nêu điều cần giải thích; **00 — Foundations và đo lường (measurement / 측정): mạnh** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **01 — Mechanics: mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 00 — Foundations và đo lường (measurement / 측정): mạnh

Vật lý (physical / 물리적) thinking, đo lường (measurement / 측정)/bất định (uncertainty / 불확실성), véc-tơ (vector / 벡터)/frame, mathematical ngôn ngữ (language / 언어), symmetry/scaling và PDE/Green/tensor tạo prerequisite cho toàn thư viện (library / 라이브러리). First-principles workflow đã bao gồm hệ thống (system / 시스템) ranh giới (boundary / 경계), degrees of freedom, quy mô (scale / 규모) phân tích (analysis / 분석), controlled approximation, dimensional checks, forward/inverse bài toán (problem / 문제), falsifiability và mô hình (model / 모델) discrepancy.

**Trạng thái:** không còn lỗ cốt lõi (core / 핵심) lớn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiểm tra (audit / 감사) phạm vi, độ sâu và chất lượng của Thư viện Vật lý**, **00 — Foundations và đo lường (measurement / 측정): mạnh** nêu điều cần giải thích; **01 — Mechanics: mạnh** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **02 — Oscillations và waves: mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 01 — Mechanics: mạnh

Phụ thuộc (dependency / 의존성) chính:

```text
kinematics
→ Newton dynamics
→ common forces
→ work/energy + momentum
→ rotation + gravity + statics
→ analytical mechanics
→ nonlinear/canonical/rotating-frame extensions
```

Coverage gồm force modelling, free-body lập luận (reasoning / 추론), công việc (work / 작업)–năng lượng (energy / 에너지), momentum, rigid-body rotation, gravitation/orbits, elasticity, Lagrange/Hamilton, chaos, Hamilton–Jacobi và non-inertial frames.

**Trạng thái:** strong undergraduate cốt lõi (core / 핵심) + advanced cầu nối (bridge / 브리지).

> **Chuyển mạch:** Trong **Kiểm tra (audit / 감사) phạm vi, độ sâu và chất lượng của Thư viện Vật lý**, **02 — Oscillations và waves: mạnh** tiếp nhận điểm tựa từ **01 — Mechanics: mạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **03 — Continuum, fluids và vận chuyển (transport / 전송): mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 02 — Oscillations và waves: mạnh

SHM, damping, driven phản hồi (response / 응답), resonance, wave equation, standing waves, Fourier, sound, dispersion và normal modes đều có. ranh giới (boundary / 경계) conditions và dispersion limits đã được làm rõ.

**Trạng thái:** strong cốt lõi (core / 핵심)/cầu nối (bridge / 브리지).

> **Chuyển mạch:** Ở chặng này của **Kiểm tra (audit / 감사) phạm vi, độ sâu và chất lượng của Thư viện Vật lý**, **03 — Continuum, fluids và vận chuyển (transport / 전송): mạnh** tiếp nhận điểm tựa từ **02 — Oscillations và waves: mạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **04 — Thermodynamics và Statistical Physics: mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 03 — Continuum, fluids và vận chuyển (transport / 전송): mạnh

Hydrostatics, buoyancy, continuity, Bernoulli, viscosity, Reynolds, Poiseuille, ranh giới (boundary / 경계) tầng (layer / 계층) và Navier–Stokes đã có. Capillarity, vận chuyển (transport / 전송), turbulence/rheology và continuum stress tensor nối conservation law với constitutive quan hệ (relation / 관계).

**Trạng thái:** strong cốt lõi (core / 핵심)/cầu nối (bridge / 브리지).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiểm tra (audit / 감사) phạm vi, độ sâu và chất lượng của Thư viện Vật lý**, **04 — Thermodynamics và Statistical Physics: mạnh** tiếp nhận điểm tựa từ **03 — Continuum, fluids và vận chuyển (transport / 전송): mạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **05 — Electricity, circuits, magnetism và electromagnetism: mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 04 — Thermodynamics và Statistical Physics: mạnh

Thermodynamics, entropy, phase transitions, ensembles, Boltzmann equation, stochastic nonequilibrium, trọng yếu (critical / 중요) phenomena/RG và tuyến tính (linear / 선형) phản hồi (response / 응답)/FDT tạo chuỗi micro ↔ macro ↔ fluctuations ↔ phản hồi (response / 응답).

**Trạng thái:** strong undergraduate + selected graduate cầu nối (bridge / 브리지).

> **Chuyển mạch:** Trong **Kiểm tra (audit / 감사) phạm vi, độ sâu và chất lượng của Thư viện Vật lý**, **05 — Electricity, circuits, magnetism và electromagnetism: mạnh** tiếp nhận điểm tựa từ **04 — Thermodynamics và Statistical Physics: mạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **06 — Optics: mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 05 — Electricity, circuits, magnetism và electromagnetism: mạnh

Electrostatics, capacitance, DC/AC circuits, magnetism/induction, Maxwell, transmission lines, gauge/potentials và fields in matter đều đã có. Boundary-value/multipole, radiation/scattering/antenna và relativistic electrodynamics bổ sung selected độ sâu (depth / 깊이).

Transmission-line chapter đã có telegrapher derivation, characteristic impedance, reflection/VSWR, lossy line, waveguide modes và signal-integrity lập luận (reasoning / 추론).

**Trạng thái:** strong calculus-based university coverage.

> **Chuyển mạch:** Ở chặng này của **Kiểm tra (audit / 감사) phạm vi, độ sâu và chất lượng của Thư viện Vật lý**, **06 — Optics: mạnh** tiếp nhận điểm tựa từ **05 — Electricity, circuits, magnetism và electromagnetism: mạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **07 — Relativity: mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 06 — Optics: mạnh

Geometric optics, wave optics, photon/laser/coherence, polarization/dispersion/nonlinear optics và Fourier imaging đều có. Wave-optics và laser chapters đã có derivation giao thoa/nhiễu xạ, coherence, PSF/OTF, Einstein coefficients, tỷ lệ (rate / 비율) equations, cavity threshold, linewidth/Q và chế độ (mode / 모드) locking.

**Trạng thái:** strong cốt lõi (core / 핵심)/cầu nối (bridge / 브리지).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiểm tra (audit / 감사) phạm vi, độ sâu và chất lượng của Thư viện Vật lý**, **07 — Relativity: mạnh** tiếp nhận điểm tựa từ **06 — Optics: mạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **08 — Quantum Physics: mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 07 — Relativity: mạnh

Special relativity có bất biến (invariant / 불변식) interval, Lorentz transformation, proper thời gian (time / 시간), four-vector, four-momentum và relativistic dynamics. General relativity có equivalence principle, chỉ số (metric / 지표), geodesic, curvature, geodesic deviation, weak-field limit, Einstein equation, Schwarzschild, lensing, Shapiro delay, gravitational waves và Friedmann cầu nối (bridge / 브리지).

**Trạng thái:** strong SR + solid GR cầu nối (bridge / 브리지).

> **Chuyển mạch:** Trong **Kiểm tra (audit / 감사) phạm vi, độ sâu và chất lượng của Thư viện Vật lý**, **08 — Quantum Physics: mạnh** tiếp nhận điểm tựa từ **07 — Relativity: mạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **09 — Atomic, molecular, nuclear và particle: mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 08 — Quantum Physics: mạnh

Foundations → mô hình (model / 모델) các hệ thống (systems / 시스템들) → spin/angular momentum → đo lường (measurement / 측정)/decoherence → approximation → identical particles → time-dependent/scattering → symmetry/path-integral tạo chuỗi (sequence / 시퀀스) đầy đủ.

Mô hình (model / 모델) các hệ thống (systems / 시스템들) và spin chapters đã được nâng với boundary-condition derivation, tunneling hiện tại (current / 현재), ladder operators, SU(2), Bloch sphere, Stern–Gerlach, Larmor precession, Clebsch–Gordan và selection rules. Approximation chapter đã có perturbation, degeneracy, variational, adiabatic/Born–Oppenheimer, WKB, mean-field và EFT lập luận (reasoning / 추론).

**Trạng thái:** strong undergraduate + selected advanced cầu nối (bridge / 브리지).

> **Chuyển mạch:** Ở chặng này của **Kiểm tra (audit / 감사) phạm vi, độ sâu và chất lượng của Thư viện Vật lý**, **09 — Atomic, molecular, nuclear và particle: mạnh** tiếp nhận điểm tựa từ **08 — Quantum Physics: mạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10 — Condensed matter, materials, electronics và plasma: mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 09 — Atomic, molecular, nuclear và particle: mạnh

Atomic cấu trúc (structure / 구조)/spectroscopy, molecular modes, nuclear các mô hình (models / 모델들)/decay/reactions, radiation detection và tiêu chuẩn (standard / 표준) mô hình (model / 모델) đều có. Detector chapter đã có dead thời gian (time / 시간), pile-up, năng lượng (energy / 에너지) resolution, efficiency, phản hồi (response / 응답) hàm (function / 함수), background và calibration.

**Trạng thái:** strong cầu nối (bridge / 브리지); không mở full graduate QFT/nuclear-many-body trong phạm vi (scope / 범위) này.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiểm tra (audit / 감사) phạm vi, độ sâu và chất lượng của Thư viện Vật lý**, **10 — Condensed matter, materials, electronics và plasma: mạnh** tiếp nhận điểm tựa từ **09 — Atomic, molecular, nuclear và particle: mạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11 — Astrophysics và cosmology: mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10 — Condensed matter, materials, electronics và plasma: mạnh

Band lý thuyết (theory / 이론), reciprocal lattice, Brillouin zone, DOS, effective mass, semiconductor electrostatics, P–N junction, MOS capacitor, MOSFET scaling, carrier vận chuyển (transport / 전송), Hall, magnetism, superconductivity và plasma đều có. Các extension về phonons/defects/topological matter, BEC/superfluidity và Berry/Quantum Hall bổ sung selected độ sâu (depth / 깊이).

**Trạng thái:** strong cốt lõi (core / 핵심)/cầu nối (bridge / 브리지).

> **Chuyển mạch:** Trong **Kiểm tra (audit / 감사) phạm vi, độ sâu và chất lượng của Thư viện Vật lý**, **11 — Astrophysics và cosmology: mạnh** tiếp nhận điểm tựa từ **10 — Condensed matter, materials, electronics và plasma: mạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12 — Experiment, signals, computation và suy luận (inference / 추론): mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11 — Astrophysics và cosmology: mạnh

Stellar cấu trúc (structure / 구조)/evolution, compact objects, galaxies/cosmology, observational astrophysics/radiative transfer, early universe/dark components và gravitational cấu trúc (structure / 구조) formation đều có. Cosmology cốt lõi (core / 핵심) đã có FLRW/Friedmann, trọng yếu (critical / 중요) density, density parameters, distance measures, CMB/BAO, cấu trúc (structure / 구조) growth, dark-energy parameterization và parameter suy luận (inference / 추론).

**Trạng thái:** strong cầu nối (bridge / 브리지) between lý thuyết (theory / 이론) and observation.

> **Chuyển mạch:** Ở chặng này của **Kiểm tra (audit / 감사) phạm vi, độ sâu và chất lượng của Thư viện Vật lý**, **12 — Experiment, signals, computation và suy luận (inference / 추론): mạnh** tiếp nhận điểm tựa từ **11 — Astrophysics và cosmology: mạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 12 — Experiment, signals, computation và suy luận (inference / 추론): mạnh

Calibration, bất định (uncertainty / 불확실성), sampling, PSD/noise, numerical ODE/PDE, Monte Carlo, inverse problems và statistical suy luận (inference / 추론) đã có. Đây là lớp kiểm chứng mô hình (model / 모델) bằng dữ liệu, không chỉ là phần phụ của lý thuyết.

**Trạng thái:** strong methodological tầng (layer / 계층).

# Phụ thuộc (dependency / 의존성) kiểm tra (audit / 감사)

Phụ thuộc (dependency / 의존성) tổng thể:

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

Experiment/computation/suy luận (inference / 추론) chạy song song và quay lại kiểm chứng mọi lĩnh vực (domain / 도메인). Các chapter advanced được đặt sau prerequisite hợp lý và không tạo phụ thuộc (dependency / 의존성) vòng bắt buộc.

# Prose-quality kiểm tra (audit / 감사)

Nguyên tắc toàn thư viện (library / 라이브러리):

```text
Vietnamese explanation first
+ English keyword khi cần tra cứu
+ không giữ cả câu English song song
+ không đổi equations/derivation nếu physics không sai
```

Các prose debt lớn từng tồn tại ở momentum, waves/Fourier, fluids, thermodynamics, quantum foundations, wave optics, laser/coherence và transmission lines đã được normalize.

# Structural checklist trước merge

Chuẩn gốc (canonical / 정본) cây (tree / 트리) đã được cleanup theo các tiêu chí:

- một chuẩn gốc (canonical / 정본) đường dẫn (path / 경로) `physics/`;
- không có tệp (file / 파일) tạm theo mẫu (pattern / 패턴) `_updated`, `_final`, `_version2`;
- numbering collision đã được chuẩn hóa;
- README chỉ link tới chuẩn gốc (canonical / 정본) filenames;
- glossary/điều hướng (navigation / 내비게이션) trỏ theo cấu trúc chuẩn gốc (canonical / 정본);
- hai archive variants từng có malformed điều khiển (control / 제어) character không được dùng trong chuẩn gốc (canonical / 정본) cây (tree / 트리);
- gốc (root / 루트) README và Study thư viện (library / 라이브러리) cấu hình (config / 설정) chỉ thêm tích hợp (integration / 통합) cần thiết cho Physics.

GitHub Actions không có PR-triggered run cho lần ghi nhận (commit / 커밋) chuẩn gốc (canonical / 정본) tại thời điểm kiểm tra (audit / 감사), nên bản dựng (build / 빌드) kiểm tra hợp lệ (validation / 검증) cần dựa vào site workflow sau khi mở PR/merge. Nội dung Markdown không phụ thuộc nhị phân (binary / 이진)/hiện vật bản dựng (build artifact / 빌드 산출물) riêng.

# Nguyên tắc dừng

Cốt lõi (core / 핵심) Physics được xem là đủ cho thư viện kiến thức (knowledge library / 지식 라이브러리) tổng quát khi lĩnh vực (domain / 도메인) có:

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

> **Bàn giao:** Sau **12 — Experiment, signals, computation và suy luận (inference / 추론): mạnh**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
