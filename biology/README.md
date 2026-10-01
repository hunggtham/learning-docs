# Biology thư viện kiến thức (knowledge library / 지식 라이브러리) — Thư viện kiến thức Sinh học

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Biology thư viện kiến thức (knowledge library / 지식 라이브러리) — Thư viện kiến thức Sinh học**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Mô hình tư duy (mental model / 사고 모델) trung tâm cho lần kiểm tra (audit / 감사) 2026-09** gom các mảnh thành mental model có thể mang sang nhánh khác; sau đó sang **1. Đồ thị kiến thức (knowledge graph) toàn thư viện** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Sinh học (Biology / 생물학) trong thư viện này được viết như một **hệ thống kiến thức liên tục**, không phải tập hợp ghi chú (tập hợp ghi chú (collection note)) hay cheat sheet. Người đọc được giả định có thể đã quên phần lớn Sinh học phổ thông, vì vậy mỗi chapter phải tự dựng nền cần thiết, giải thích vì sao concept xuất hiện, cơ chế (mechanism / 메커니즘) hoạt động ra sao, mô hình (model / 모델) nào giúp suy luận và khái niệm (concept) đó dẫn tự nhiên sang chapter nào tiếp theo.

Mục tiêu cuối cùng không phải nhớ thật nhiều thuật ngữ. Mục tiêu là nhìn thấy một số mẫu (pattern / 패턴) sâu lặp lại từ phân tử (molecule) đến biosphere: **dòng vật chất (matter flow), dòng năng lượng (energy flow), dòng thông tin (information flow), chênh lệch (gradient), phản hồi (feedback / 피드백), sự đánh đổi (trade-off / 트레이드오프), mạng lưới (network), selection và quy mô (scale / 규모)**.

> **mô hình tư duy (mental model / 사고 모델) trung tâm:** sự sống là một hệ vật chất xa cân bằng nhiệt động, duy trì organization nhờ dòng vật chất và năng lượng, dùng thông tin (information / 정보) để điều phối và truyền heredity, tự điều chỉnh bằng phản hồi (feedback / 피드백), và thay đổi qua evolution dưới ràng buộc (constraint / 제약조건) của Physics, Chemistry và tính ngẫu nhiên lịch sử (historical contingency).

---

<!-- depth-audit-2026:central-chain -->

## Mô hình tư duy (mental model / 사고 모델) trung tâm cho lần kiểm tra (audit / 감사) 2026-09

Toàn bộ thư viện được đọc theo chuỗi:

```text
matter
→ energy
→ information
→ regulation
→ adaptation
→ evolution
→ ecosystem
```

Đây không phải taxonomy chapter mà là nhân quả (causal / 인과적) spine. Vật chất tạo cấu trúc (structure / 구조); năng lượng giữ độ dốc (gradient / 기울기) và reaction; thông tin (information / 정보) làm phản hồi (response / 응답) có chọn lọc; regulation biến phản hồi (response / 응답) thành phản hồi (feedback / 피드백); adaptation đổi trạng thái (state / 상태) hoặc trait dưới ràng buộc (constraint / 제약조건); evolution giữ thay đổi heritable qua generation; ecosystem lại tạo dòng vật chất, năng lượng và selection pressure mới.

Khi kiểm tra (audit / 감사) một chapter, dùng template bắt buộc:

```text
structure
→ mechanism
→ regulation
→ function
→ failure
→ adaptation/evolution
```

Nếu chapter chỉ kể tên cấu trúc (structure / 구조) mà không giải cơ chế (mechanism / 메커니즘), hoặc chỉ mô tả hàm (function / 함수) mà không nói thất bại (failure / 실패)/ranh giới (boundary / 경계) điều kiện (condition / 조건), chapter chưa đạt chuẩn dù có nhiều từ khóa (keyword / 키워드).

> **Chuyển mạch:** Trong **Biology thư viện kiến thức (knowledge library / 지식 라이브러리) — Thư viện kiến thức Sinh học**, **1. Đồ thị kiến thức (knowledge graph) toàn thư viện** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델) trung tâm cho lần kiểm tra (audit / 감사) 2026-09** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **2. Cấu trúc thư viện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 1. Đồ thị kiến thức (knowledge graph) toàn thư viện

Đồ thị này là bản đồ dependency, không phải danh sách cần học thuộc. Hãy đọc theo mũi tên để thấy cấu trúc tế bào, dòng năng lượng và thông tin dần mở rộng thành organism, evolution và ecosystem.

```mermaid
flowchart TD
    A[Scientific thinking, scale, models]
    A --> B[What is life?]
    B --> C[Chemistry, water, energy]
    C --> D[Biomolecules, enzymes, ATP]
    D --> E[Origin of life]

    E --> F[Cells, membranes, transport]
    F --> G[Metabolism, respiration, photosynthesis]
    G --> H[Signaling and cell cycle]
    H --> I[Multicellularity, tissues, ECM]

    H --> J[DNA, genes, gene expression]
    J --> K[Inheritance, variation, mutation]
    K --> L[Genomics, epigenetics, regulation]
    L --> M[DNA repair, recombination, genome stability]

    M --> N[Evolution and population genetics]
    N --> O[Phylogeny, taxonomy, biodiversity]
    O --> P[Microorganisms and viruses]
    O --> Q[History of life and major transitions]

    I --> R[Plant biology]
    I --> S[Animal physiology and homeostasis]
    S --> T[Nervous, endocrine, immune systems]
    T --> U[Reproduction and development]
    T --> V[Sensory, motor, behavioral integration]
    S --> VH[Human body principles and health management]
    T --> VH
    V --> VH
    U --> VH
    VH --> VR[Health risk, prevention and self-monitoring]

    N --> W[Population, community, behavior]
    V --> W
    U --> W
    W --> X[Ecosystems, cycles, conservation]
    X --> Y[Biomes, global change, biosphere]

    J --> Z[Biotechnology overview]
    Y --> AA[Experimental methods and measurement]
    Z --> AA
    VR --> AA
    AA --> AB[Bioinformatics algorithms and omics]
    AB --> AC[Systems biology and synthetic biology]

    AC --> AD[Math, computation and scale]
    AC --> AE[Physics, chemistry and engineering]
```

Đồ thị (graph / 그래프) này biểu diễn **phụ thuộc (dependency / 의존성) khái niệm**, không phải lịch học cứng. Nếu một chapter dùng concept đã được dựng ở chapter trước, nó sẽ link ngược lại thay vì giải thích lại từ đầu một cách rời rạc.

---

> **Chuyển mạch:** Knowledge graph cho biết concept phụ thuộc nhau ra sao; cấu trúc thư mục biến dependency đó thành navigation, rồi chapter standard quy định mỗi node phải giải thích tới mức nào.

## 2. Cấu trúc thư viện

Sau khi thấy quan hệ khái niệm, phần này cho biết mỗi lớp kiến thức nằm ở đâu trong thư mục. Cấu trúc file được sắp theo câu hỏi đang được giải quyết để người mới biết nên quay về prerequisite nào khi gặp thuật ngữ mới.

```text
biology/
├── README.md
├── COVERAGE_AUDIT.md
├── 00_foundations/
│   ├── 00_scientific_thinking_scale_and_models.md
│   ├── 00_what_is_life.md
│   ├── 01_chemistry_energy_and_water.md
│   ├── 02_biomolecules_enzymes_and_energy.md
│   └── 03_origin_of_life_and_early_evolution.md
├── 01_cell_biology/
│   ├── 00_cells_membranes_and_transport.md
│   ├── 01_metabolism_respiration_photosynthesis.md
│   ├── 02_cell_signaling_and_cell_cycle.md
│   └── 03_multicellularity_tissues_and_extracellular_matrix.md
├── 02_genetics_molecular_biology/
│   ├── 00_dna_genes_and_gene_expression.md
│   ├── 01_inheritance_variation_and_mutation.md
│   ├── 02_genomics_epigenetics_and_regulation.md
│   └── 03_dna_repair_recombination_and_genome_stability.md
├── 03_evolution_and_diversity/
│   ├── 00_evolution_and_population_genetics.md
│   ├── 01_phylogeny_taxonomy_and_biodiversity.md
│   ├── 02_microorganisms_and_viruses.md
│   └── 03_history_of_life_and_major_transitions.md
├── 04_organismal_biology/
│   ├── 00_plant_biology.md
│   ├── 01_animal_physiology_and_homeostasis.md
│   ├── 02_nervous_endocrine_and_immune_systems.md
│   ├── 03_reproduction_and_development.md
│   ├── 04_sensory_motor_and_behavioral_integration.md
│   ├── 05_human_body_principles_and_health_management.md
│   └── 06_health_risk_prevention_and_self_monitoring.md
├── 05_ecology/
│   ├── 00_population_community_and_behavior.md
│   ├── 01_ecosystems_biogeochemical_cycles_and_conservation.md
│   └── 02_biomes_global_change_and_biosphere.md
├── 06_biotechnology_computation/
│   ├── 00_biotechnology_bioinformatics_and_systems_biology.md
│   ├── 01_experimental_methods_and_measurement.md
│   ├── 02_bioinformatics_algorithms_and_omics_workflows.md
│   └── 03_systems_biology_modeling_and_synthetic_biology.md
└── 90_connections/
    ├── 00_biology_math_computation_and_scale.md
    └── 01_biology_physics_chemistry_and_engineering.md
```

---

> **Chuyển mạch:** Folder structure chỉ cho biết đi đâu; chapter standard kiểm tra problem, mechanism, evidence và handoff, từ đó lộ trình beginner có thể xếp prerequisite trước ứng dụng.

## 3. Chuẩn hoàn thiện của một chapter

Một chapter không được coi là hoàn chỉnh chỉ vì “đã nhắc tới đủ từ khóa (keyword / 키워드)”. Chuẩn hiện tại của thư viện là:

```text
Problem / Constraint
→ First Principles
→ Components
→ Mechanism
→ Quantitative reasoning khi hữu ích
→ Case study / worked reasoning
→ Assumption & limitation
→ Common misconception
→ Cross-domain connection
→ Bridge sang chapter kế tiếp
```

Các equation không được đặt như formula để học thuộc. Mỗi equation cần giải thích variable là gì, quan hệ (relation / 관계) nào được giả định, mô hình (model / 모델) bỏ qua điều gì và khi nào mô hình (model / 모델) không còn tốt.

Các tình huống phân tích (case study) không dùng chỉ để “trang trí”. Chúng phải ép người đọc nối nhiều concept cùng lúc. Ví dụ vận chuyển oxy (oxygen delivery) nối diffusion, liên kết (binding), circulation và dòng chảy (flow); hạn hán (drought) ở plant nối thế nước (water potential), VPD, stomata và suy thủy lực (hydraulic failure); tumor nối mutation, độ ổn định hệ gen (genome stability), hợp tác đa bào (multicellular cooperation), evolution và immune pressure; fatigue nối sleep, năng lượng (energy / 에너지), dự trữ (reserve), medication và mental-health ngữ cảnh (context / 맥락).

---

> **Chuyển mạch:** Chapter standard xác định mức bằng chứng cần đạt; reading path sắp prerequisite từ nền tảng tới ứng dụng, rồi motifs xuyên thư viện giúp nhận ra cùng một cơ chế ở nhiều quy mô.

## 4. Lộ trình đọc từ số 0

### Chặng A — Học cách suy nghĩ như một nhà Sinh học

Bắt đầu bằng `00_scientific_thinking_scale_and_models.md`. Chapter này thiết lập tư duy hệ thống (systems thinking), suy luận nhân quả (causal reasoning), mô hình (model / 모델), quy mô (scale / 규모), emergence, cấu trúc (structure / 구조)–chức năng (function), phản hồi, vật chất (matter)–năng lượng–thông tin (information / 정보) và độ bất định (uncertainty / 불확실성).

Sau đó `00_what_is_life.md` chuyển từ cách tư duy sang câu hỏi “một hệ vật chất phải làm gì để được xem là sống?”. `01_chemistry_energy_and_water.md` cung cấp chemistry tối thiểu, rồi `02_biomolecules_enzymes_and_energy.md` giải thích polymer, enzym (enzyme), ATP và ghép năng lượng (energy coupling).

`03_origin_of_life_and_early_evolution.md` là cầu nối (bridge / 브리지) đầy đủ từ chemistry sang cell: hóa học tiền sinh học (prebiotic chemistry), tiền tế bào (protocell), độ chính xác sao chép (replication fidelity), ngưỡng lỗi (error threshold), ghép năng lượng, đơn vị chọn lọc (unit of selection), genetic-code lock-in và tiến hóa sơ khai (early evolution).

### Chặng B — Cell như một hệ thống (system / 시스템) có ranh giới (boundary / 경계), năng lượng (energy / 에너지) và điều khiển (control / 제어)

`00_cells_membranes_and_transport.md` bắt đầu từ định danh (identity / 식별자) và selective exchange. `01_metabolism_respiration_photosynthesis.md` dùng redox, electron luồng (flow / 흐름) và thẩm thấu hóa học (chemiosmosis) để nối respiration với quang hợp (photosynthesis). `02_cell_signaling_and_cell_cycle.md` thêm sensing, phản hồi (feedback / 피드백) và quyết định (decision / 결정) về sinh trưởng (growth)/phân chia (division)/death.

`03_multicellularity_tissues_and_extracellular_matrix.md` giải thích diffusion limit, tính phân cực (polarity), kiến trúc mô (tissue architecture), ECM, mechanotransduction, vascularization, tạo hình (morphogenesis), regeneration và cancer như breakdown của hợp tác đa bào.

### Chặng C — thông tin (information / 정보): lưu, đọc, truyền và bảo vệ

`00_dna_genes_and_gene_expression.md` xây dòng thông tin DNA → RNA → protein (protein). `01_inheritance_variation_and_mutation.md` chuyển sang chromosome, meiosis và di truyền (inheritance). `02_genomics_epigenetics_and_regulation.md` thay mô hình tư duy “một gene = một trait” bằng mạng lưới điều hòa (regulatory network).

`03_dna_repair_recombination_and_genome_stability.md` làm rõ độ chính xác sao chép, MMR/BER/NER, repair choice NHEJ–HR, căng thẳng sao chép (replication stress), telomere, transposon, mosaicism, p53, synthetic lethality và sự đánh đổi (trade-off / 트레이드오프) stability–evolvability.

### Chặng D — Evolution từ alen (allele) đến lịch sử sự sống

`00_evolution_and_population_genetics.md` theo dõi tần số alen (allele frequency) qua chọn lọc (selection), drift, mutation và dòng gen (gene flow). `01_phylogeny_taxonomy_and_biodiversity.md` đưa population thay đổi (change / 변경) thành branching lịch sử (history / 이력). `02_microorganisms_and_viruses.md` cho thấy evolution chạy nhanh trong microbe/virus.

`03_history_of_life_and_major_transitions.md` mở rộng sang fossil lấy mẫu (sampling), định tuổi phóng xạ (radiometric dating), nội cộng sinh (endosymbiosis), energetic kiến trúc (architecture / 아키텍처), sex, multicellularity, Evo-Devo, gene duplication, convergence, neutral evolution, đồng hồ phân tử (molecular clock), tuyệt chủng hàng loạt (mass extinction) và bức xạ thích nghi (adaptive radiation).

### Chặng E — Organism như một hệ phối hợp nhiều subsystem

`00_plant_biology.md` hiện đọc plant như một **hydraulic–kinh tế carbon (carbon economy)** thay vì chỉ học gốc (root / 루트)/thân (stem)/lá (leaf). Chapter nối thế nước, xylem cohesion–tension, sức cản thủy lực (hydraulic resistance)/cavitation, VPD, stomatal regulation, C3/C4/CAM, nguồn (source / 소스)–sink phloem, tương tác chéo hoóc-môn (hormone crosstalk), circadian/quang chu kỳ (photoperiod) điều khiển, hạt (seed)/hoa (flower) phát triển (development), miễn dịch thực vật (plant immunity), electrical/Ca²⁺ signaling và khí hậu (climate)-response sự đánh đổi (trade-off / 트레이드오프).

`01_animal_physiology_and_homeostasis.md` hiện xây cơ thể động vật (animal body) như một mạng (network / 네트워크) `flow + exchange + control`. Ngoài circulation, hô hấp (respiration), digestion và kidney, chương (chapter) đi sâu hàm lượng oxy (oxygen content)/delivery, hemoglobin affinity, thông khí (ventilation)–perfusion matching, compliance, Frank–Starling, axit–bazơ (acid–base) compensation, GFR, countercurrent concentration, ADH/RAAS/natriuretic counter-điều khiển, điều hòa thân nhiệt (thermoregulation), cơ học cơ (muscle mechanics), Fick principle trong exercise và lô-gic (logic / 논리) physiological compensation/thất bại (failure / 실패).

`02_nervous_endocrine_and_immune_systems.md` không còn chỉ là ba hệ riêng. Nervous phần đi từ Nernst/điện thế hoạt động (action potential) sang neural coding, trường tiếp nhận (receptive field), thích nghi (adaptation), baroreflex và plasticity. Endocrine phần thêm pulsatile secretion, thụ thể (receptor) adaptation và state-điều khiển lôgic (logic). Immune phần đi từ barrier/innate tới trình diện kháng nguyên (antigen presentation), MHC, chọn lọc dòng tế bào (clonal selection), trưởng thành ái lực (affinity maturation), bộ nhớ (memory / 메모리), tiêm chủng (vaccination), tolerance, allergy, resolution và chronic stimulation. Cuối chapter nối chúng thành một neuro–endocrine–immune mạng (network / 네트워크) có circadian điều khiển (control / 제어).

`03_reproduction_and_development.md` hiện đi từ gametogenesis/fertilization tới maternal–zygotic chuyển tiếp (transition / 전이), cleavage, gastrulation, morphogen/phản ứng–khuếch tán (reaction–diffusion), Hox, segmentation, EMT, cơ học mô (tissue mechanics), sự hình thành cơ quan (organogenesis), placenta, sexual development, puberty, postnatal brain development, giai đoạn tới hạn (critical period), developmental plasticity, tái sinh (regeneration), xơ hóa (fibrosis), aging và Evo-Devo. Phát triển (development) được trình bày như quá trình biến regulatory thông tin (information / 정보) thành hình học (geometry / 기하학) rồi thành physiological hàm (function / 함수).

`04_sensory_motor_and_behavioral_integration.md` nối receptor → coding → ước lượng trạng thái (state estimation) → lựa chọn hành động (action selection) → điều khiển vận động (motor control) → sai số dự đoán (prediction error) → học tập (learning / 학습) → hành vi (behavior / 동작). Chapter dùng Bayesian intuition, reward-sai số dự đoán, huy động đơn vị vận động (motor-unit recruitment), lực–vận tốc (force–velocity), CPG và sinh thái học hành vi (behavioral ecology) để nối physiology với ecology.

`05_human_body_principles_and_health_management.md` chuyển physiology sang quản lý sức khỏe (health management). Chapter bắt đầu từ cân bằng nội môi (homeostasis), khả năng dự trữ (reserve capacity) và gánh nặng thích nghi (allostatic load) rồi nối sang cân bằng năng lượng (energy balance), dinh dưỡng (nutrition), hydration, điều hòa glucose (glucose regulation), muscle, thể lực tim phổi (cardiorespiratory fitness), giấc ngủ (sleep)/nhịp sinh học ngày đêm (circadian rhythm), căng thẳng (stress), miễn dịch (immunity), viêm (inflammation), liver/kidney, hệ vi sinh (microbiome), sức khỏe răng miệng (oral health), tobacco/alcohol, chất bổ sung (supplement), chăm sóc dự phòng (preventive care) và các chỉ số sức khỏe (health metrics). Phần cuối xây một **Health Operating hệ thống (system / 시스템)** theo dòng chảy `Foundation → Observe → Identify bottleneck → Controlled change → Reassess`.

`06_health_risk_prevention_and_self_monitoring.md` đi thêm một bước sang **khoa học ra quyết định về sức khỏe dự phòng (preventive-health decision science)**: triệu chứng (symptom)–sign–nguy cơ (risk)–bệnh (disease), absolute/nguy cơ tương đối (relative risk), cardiometabolic cluster, hội chứng chuyển hóa (metabolic syndrome), musculoskeletal tải (load / 로드), khoa học thần kinh về đau (pain neuroscience), sensory health, giấc ngủ-disorder lập luận (reasoning / 추론), đối chiếu danh sách thuốc (medication reconciliation), supplement cây quyết định (decision tree / 의사결정 트리), wearable/HRV/SpO₂, signal-vs-nhiễu (noise), lab interpretation, sàng lọc (screening) sai lệch (bias), tiêm chủng, lão hóa (aging)/frailty và thử nghiệm N-of-1 an toàn (safe N-of-1 experimentation).

### Chặng F — Từ individual lên population, ecosystem và sinh quyển (biosphere)

`00_population_community_and_behavior.md` bắt đầu từ sinh trưởng mô hình (model / 모델) và tương tác (interaction / 상호작용). `01_ecosystems_biogeochemical_cycles_and_conservation.md` theo dõi năng lượng (energy / 에너지) và vật chất qua bậc dinh dưỡng (trophic level) và chu trình dinh dưỡng (nutrient cycle).

`02_biomes_global_change_and_biosphere.md` mở rộng sang solar forcing, cân bằng nước (water balance), ocean mixing, carbon–khí hậu phản hồi, nitrogen microbial điều khiển (control / 제어), succession, hiện tượng trễ (hysteresis), biến đổi khí hậu (climate change), metapopulation, One Health và multi-stressor tình huống phân tích.

### Chặng G — Biology hiện đại được đo như thế nào?

`00_biotechnology_bioinformatics_and_systems_biology.md` giữ vai trò overview. Sau đó `01_experimental_methods_and_measurement.md` giải độ hợp lệ của cấu trúc đo lường (construct validity), điều khiển, ngẫu nhiên hóa (randomization), lần lặp (replicate), hiệu chuẩn (calibration), tín hiệu trên nhiễu (signal-to-noise), hiển vi (microscopy), PCR, đo tế bào dòng chảy (flow cytometry), giải trình tự (sequencing), quan hệ liều–đáp ứng (dose–response), hiệu ứng lô (batch effect), statistics và suy luận nhân quả.

Điểm quan trọng là **thiết bị đo (instrument) tín hiệu (signal / 신호) không phải biological truth trực tiếp**. Hai chapter Human Health dùng chính principle này để giải thích vì sao wearable, huyết áp (blood pressure), SpO₂, body-composition estimate và laboratory kết quả (result / 결과) phải được đọc theo bối cảnh (context), nhiễu, baseline và xác suất trước xét nghiệm (pre-test probability).

### Chặng H — Từ dữ liệu thô (raw data) đến suy luận (inference / 추론) và mô hình dự đoán (predictive model)

`02_bioinformatics_algorithms_and_omics_workflows.md` đi từ FASTQ/siêu dữ liệu (metadata / 메타데이터)/QC sang alignment, BLAST, ánh xạ (mapping / 매핑) bất định (uncertainty / 불확실성), gọi biến thể (variant calling), assembly, RNA-seq, single-tế bào (cell), epigenomics, multi-omics, mạng (network / 네트워크) và ML.

`03_systems_biology_modeling_and_synthetic_biology.md` tiếp tục bằng ODE, trạng thái ổn định (steady state), phản hồi, tính lưỡng ổn (bistability), hiện tượng trễ, tính ngẫu nhiên (stochasticity), độ nhạy (sensitivity), identifiability, epistasis, FBA, mô hình đa quy mô (multi-scale model), mạch sinh học tổng hợp (synthetic circuit) và mô hình lai cơ chế–học máy (hybrid mechanistic–ML modeling).

### Chặng I — Synthesis xuyên môn

`90_connections/00_biology_math_computation_and_scale.md` nối xác suất (probability / 확률), differential equation, đồ thị (graph / 그래프) và thuật toán (algorithm / 알고리즘) với Biology.

`01_biology_physics_chemistry_and_engineering.md` đi sâu vào phân tích thứ nguyên (dimensional analysis), khuếch tán (diffusion), electrochemistry, membrane capacitance, thermodynamics, thẩm thấu hóa học, liên kết, động lực học chất lưu (fluid dynamics), cơ học mô, lý thuyết điều khiển (control theory), phản ứng–khuếch tán, scaling, lý thuyết thông tin (information theory) và tính bền vững (robustness).

Hai chapter này không dùng để học tắt; chúng được đọc sau khi đã gặp concept trong lĩnh vực (domain / 도메인) để nhận ra những mathematical/vật lý (physical / 물리적) motif tái xuất ở quy mô (scale / 규모) khác.

---

> **Chuyển mạch:** Reading path đưa người học qua prerequisite; motifs như gradient, feedback và scale tạo liên kết ngang, còn self-check kiểm tra người học có thể giải thích cơ chế chứ không chỉ nhớ thuật ngữ.

## 5. Các motif xuyên toàn thư viện

### Chênh lệch

Chênh lệch nồng độ (concentration gradient) → khuếch tán → plant thế nước → chênh lệch điện hóa (electrochemical gradient) → điện thế màng (membrane potential) → động lực proton (proton motive force) → chênh lệch morphogen (morphogen gradient) → physiological exchange → ecological tài nguyên (resource / 자원) độ dốc (gradient / 기울기).

### Phản hồi

Enzyme inhibition → truyền tín hiệu (signaling) → chu kỳ tế bào (cell cycle) → stomatal/điều khiển nội tiết (endocrine control) → immune regulation → motor correction → human homeostasis → health monitoring/reassessment → mật độ quần thể (population density) dependence → khả năng phục hồi hệ sinh thái (ecosystem resilience) → systems-điều khiển mô hình (model / 모델).

### Thông tin

DNA chuỗi (sequence / 시퀀스) → biểu hiện gen (gene expression) → chương trình phát triển (developmental program) → hoóc-môn (hormone)/thụ thể trạng thái (state / 상태) → neural mã (code / 코드) → hành vi → health đo lường (measurement / 측정) → clinical suy luận (inference / 추론) → tính di truyền (heredity) → population evolution → digital omics biểu diễn (representation / 표현).

### Sự đánh đổi (trade-off / 트레이드오프)

Permeability vs điều khiển (control / 제어); thu nhận carbon (carbon gain) vs mất nước (water loss); hydraulic efficiency vs cavitation; fidelity vs evolvability; immune sensitivity vs autoimmunity; regeneration vs fibrosis/cancer; tập luyện (training) stress vs khôi phục (recovery / 복구); screening benefit vs overdiagnosis; tính bền vững vs energetic chi phí (cost / 비용).

### Noise và độ bất định

Molecular tính ngẫu nhiên → developmental variation → sensory noise → biological variation → wearable/lab lỗi (error / 오류) → statistical bất định (uncertainty / 불확실성) → độ bất định của mô hình (model uncertainty). Chương `06_health_risk_prevention_and_self_monitoring.md` biến motif này thành quyết định (decision / 결정) quy tắc (rule / 규칙) thực tế: verify → bối cảnh → xu hướng (trend) → concordant bằng chứng (evidence / 증거) → hành động (action / 동작).

### Quy mô (scale / 규모)

Atom → phân tử → macromolecule → tế bào → mô (tissue) → cơ quan (organ) → sinh vật (organism) → quỹ đạo sức khỏe (health trajectory) → quần thể (population) → quần xã (community) → hệ sinh thái (ecosystem) → sinh quyển. Mỗi lần tăng quy mô (scale / 규모) tạo đặc tính nổi trội (emergent property) nhưng vẫn chịu ràng buộc (constraint / 제약조건) của quy mô (scale / 규모) dưới.

### Mạng lưới

Chuyển hóa (metabolism), plant hydraulic/carbon allocation, tuần hoàn (circulation), neuroendocrine regulation, miễn dịch, phát triển, cardiometabolic rủi ro (risk / 위험), lưới thức ăn (food web) và omics đều cần tư duy nút (node / 노드)–tương tác (interaction / 상호작용)–phản hồi (feedback / 피드백) thay vì danh sách thành phần (component / 컴포넌트).

---

> **Chuyển mạch:** Cross-library motifs tạo câu hỏi tự kiểm tra theo cơ chế; scope tiếp theo nêu những gì thư viện bao phủ và những gì phải đối chiếu ở domain khác.

## 6. Cách tự kiểm tra sau mỗi chapter

Sau khi đọc, đừng chỉ hỏi “tôi nhớ được bao nhiêu thuật ngữ?”. Hãy thử giải thích bằng lời của mình: chương đang giải ràng buộc (constraint / 제약조건) nào; đầu vào (input / 입력)/đầu ra (output / 출력) của hệ thống (system / 시스템) là gì; vật chất, năng lượng (energy / 에너지) và thông tin đi đâu; phản hồi (feedback / 피드백) hoặc sự đánh đổi (trade-off / 트레이드오프) chính là gì; equation hoặc đo lường (measurement / 측정) nào đại diện cho relationship nào; và vì sao chapter này dẫn tự nhiên sang chapter kế tiếp.

Nếu bạn chỉ nhớ tên `ATP synthase`, `p53`, `Nernst`, `Hardy–Weinberg`, `HRV` hay `FDR` nhưng không giải thích được **vấn đề mà khái niệm đó giải quyết**, hãy quay lại cơ chế (mechanism / 메커니즘) và tình huống phân tích.

---

> **Chuyển mạch:** Trong **Biology thư viện kiến thức (knowledge library / 지식 라이브러리) — Thư viện kiến thức Sinh học**, **7. Phạm vi của thư viện (library / 라이브러리)** tiếp nhận điểm tựa từ **6. Cách tự kiểm tra sau mỗi chapter** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Trạng thái hiện tại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Phạm vi của thư viện (library / 라이브러리)

Đây là **Biology cốt lõi (core / 핵심) tổng quát**, không cố biến mỗi chuyên ngành thành một giáo trình đại học riêng. Neuroscience, Immunology, Biochemistry, Human Anatomy/Pathology, Microbiology, Bioinformatics chuyên sâu và Sinh học phát triển (developmental biology) vẫn có thể tách thành thư viện (library / 라이브러리) riêng sau này.

Hai chapter Human Health cung cấp nền systems-level và preventive-health lập luận (reasoning / 추론), nhưng không thay Human Anatomy, Pathology, Pharmacology hay guideline lâm sàng chuyên sâu. Chúng dạy cách suy luận an toàn về lifestyle, nguy cơ, phép đo (measurement), prevention và escalation — không dạy tự chẩn đoán (diagnosis)/điều trị (treatment).

---

> **Chuyển mạch:** Ở chặng này của **Biology thư viện kiến thức (knowledge library / 지식 라이브러리) — Thư viện kiến thức Sinh học**, **8. Trạng thái hiện tại** tiếp nhận điểm tựa từ **7. Phạm vi của thư viện (library / 라이브러리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quy ước ngôn ngữ và liên kết nội bộ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Trạng thái hiện tại

Sau các deepening pass, thư viện đã chuyển từ collection chapter sang một **đồ thị kiến thức dạng textbook**. Các cầu nối (bridge / 브리지) quan trọng hiện đã được viết rõ:

```text
chemistry → origin of life → cell
cell → multicellularity → tissue → organism
plant water/carbon economy → organismal physiology
DNA → genome stability → population variation → evolution
evolution → major transitions → organism diversity
physiology → neuroendocrine/immune control → development/behavior
physiology → human health management → risk/prevention/self-monitoring
organism reproduction/behavior → ecology
ecosystem → biosphere → Earth-system feedback
experiment → raw data → bioinformatics → systems model → design
```

Chi tiết kiểm tra coverage và continuity nằm trong [Biology Knowledge Library](COVERAGE_AUDIT.md).

<!-- continuity-2026:language-links -->

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Biology thư viện kiến thức (knowledge library / 지식 라이브러리) — Thư viện kiến thức Sinh học**, sau nội dung của **8. Trạng thái hiện tại**, **Quy ước ngôn ngữ và liên kết nội bộ** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Quy ước ngôn ngữ và liên kết nội bộ

Phần giải thích dùng **tiếng Việt làm ngôn ngữ chính**. Thuật ngữ quốc tế được giữ trong ngoặc ở lần xuất hiện cần thiết, ví dụ `phản hồi âm (negative feedback)` hoặc `điện thế hoạt động (action potential)`. Không dùng từ tiếng Anh như thành phần ngữ pháp chính của câu nếu đã có cách diễn đạt tiếng Việt rõ ràng; các viết tắt chuẩn như DNA, RNA, ATP, PCR, CRISPR vẫn được giữ.

Link giữa chapter dùng Markdown link chuẩn thay cho wikilink riêng của Obsidian để hoạt động trên GitHub và GitHub Pages. Mỗi chapter trong learning path có footer điều hướng tới chapter trước, mục lục Biology và chapter kế tiếp. Vì vậy người đọc có thể đi liên tục từ phân tử → tế bào → cơ thể → quần thể → hệ sinh thái mà không phải quay lại cây thư mục.

> **Bàn giao:** Sau **Quy ước ngôn ngữ và liên kết nội bộ**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
