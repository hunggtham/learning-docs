# Biology Knowledge Library — Coverage & Learning-Depth Audit

File này kiểm tra hai thứ riêng biệt:

1. thư viện có bỏ sót conceptual boundary quan trọng của Sinh học tổng quát hay không;
2. chapter có đủ nền để một người gần như bắt đầu từ số 0 theo được hay chỉ là skeleton/summary.

Bản audit này được cập nhật sau đợt rewrite toàn thư viện theo hướng textbook, causal flow và first-principles.

---

# 1. Foundations — đã bổ sung lớp nền bị thiếu

## `00_scientific_thinking_scale_and_models.md`

Đây là entry point mới cho người chưa có background.

File xây các mental model trước khi đi vào terminology: systems thinking, causal reasoning, scale, structure–function, matter/energy/information flow, feedback, variation, probability, model và scientific evidence.

Việc thêm file này giải quyết một vấn đề của bản cũ: người đọc trước đây bị đưa trực tiếp vào “life → chemistry → cell” mà chưa có khung suy nghĩ để kết nối các fact.

## `00_what_is_life.md`

Đã rewrite từ định nghĩa ngắn sang một causal chapter về organization, boundary, metabolism, homeostasis, information, reproduction, evolution, cell theory, prokaryote/eukaryote, virus và emergent property.

Người đọc không cần biết trước cell hoặc DNA; terminology được dựng trong context.

## `01_chemistry_energy_and_water.md`

Đã mở rộng Hóa học nền từ atom → bond → polarity → water → hydrophilic/hydrophobic → pH/logarithm → buffer → thermodynamics → free energy → diffusion → electrochemical gradient.

Macromolecule được chuyển sang file riêng để chemistry không bị quá tải.

## `02_biomolecules_enzymes_and_energy.md`

File mới, tách conceptual boundary trước đây bị gom quá sơ sài.

Cover carbohydrate, lipid, phospholipid, protein folding, enzyme, saturation/inhibition, nucleic acid, ATP, redox carrier và connection trực tiếp lên cell.

### Audit kết luận

Foundations hiện không còn giả định người đọc đã nhớ Chemistry/Biology phổ thông. Flow đã thành:

```text
how to reason
→ what life must do
→ what matter does
→ what biomolecules can do
→ cell organization
```

---

# 2. Cell Biology — đã chuyển từ organelle list sang systems model

## `00_cells_membranes_and_transport.md`

Đã rewrite để bắt đầu bằng bốn bài toán của cell: boundary, exchange, compartmentalization và information/energy control.

Cover prokaryote/eukaryote, organelle, cytoskeleton, surface-area-to-volume, membrane self-assembly, diffusion, osmosis, tonicity, facilitated diffusion, primary/secondary active transport, electrochemical gradient, membrane potential, endocytosis và exocytosis.

Các organelle không chỉ được định nghĩa mà được giải thích theo problem chúng giải quyết.

## `01_metabolism_respiration_photosynthesis.md`

Đã rewrite thành dòng energy liên tục:

```text
nutrient
→ redox carriers
→ electron transport
→ proton gradient
→ ATP
```

Cover glycolysis, pyruvate oxidation, TCA, ETC, chemiosmosis, oxygen, fermentation, fatty-acid metabolism, photosynthesis, Calvin cycle, C3/C4/CAM và metabolic regulation.

Đặc biệt đã sửa các misconception phổ biến như oxygen “biến thành CO₂”, plant “không respiration”, ATP yield là một con số cứng.

## `02_cell_signaling_and_cell_cycle.md`

Đã rewrite thành logic information/control: ligand → receptor → transduction → response, amplification, second messenger, GPCR, RTK, signaling distance, cell cycle, checkpoint, cyclin/CDK, p53, apoptosis và cancer như failure của multicellular cooperation.

Mitosis được giải thích theo mechanical problem thay vì chant phase.

### Audit kết luận

Cell biology hiện đủ làm prerequisite trực tiếp cho genetics, physiology và biotechnology.

---

# 3. Genetics & Molecular Biology — đã dựng từ information flow

## `00_dna_genes_and_gene_expression.md`

Cover nucleotide, strand direction, double helix, chromosome/chromatin, semiconservative replication, leading/lagging strand, repair, gene concept, transcription, RNA processing, alternative splicing, translation, genetic code, protein processing và mutation consequence.

Central dogma được dùng như abstraction hữu ích nhưng có giới hạn, tránh kiểu học thuộc `DNA → RNA → protein` mà không hiểu cơ chế.

## `01_inheritance_variation_and_mutation.md`

Mendel được nối trực tiếp với chromosome/meiosis thay vì đặt trước molecular explanation.

Cover ploidy, homolog, allele, genotype/phenotype, segregation, dominance, codominance, polygenic trait, linkage, meiosis I/II, crossing over, independent assortment, mutation class, germline/somatic, penetrance, expressivity, gene–environment interaction và heritability.

Probability được giải thích đúng nghĩa distribution, không phải schedule.

## `02_genomics_epigenetics_and_regulation.md`

Cover operon, eukaryotic promoter/enhancer, transcription factor, chromatin, DNA methylation, histone modification, X inactivation, imprinting, noncoding RNA, sequencing, reference genome, variant, GWAS, polygenic score, single-cell genomics và systems biology.

Epigenetics được viết cẩn thận để tránh claim “mọi trải nghiệm đều truyền nhiều thế hệ”.

### Audit kết luận

Genetics hiện đi đủ từ sequence → expression → inheritance → regulation → population variation.

---

# 4. Evolution, Phylogeny, Diversity & Microbiology

## `00_evolution_and_population_genetics.md`

Evolution được định nghĩa bằng allele-frequency change, sau đó mới dựng Hardy–Weinberg, selection, fitness, adaptation, mutation, drift, bottleneck, founder effect, gene flow, sexual selection, frequency dependence, coevolution, speciation và evidence.

Đã loại cách diễn giải evolution như ladder hoặc organism “cố biến đổi vì cần”.

## `01_phylogeny_taxonomy_and_biodiversity.md`

Cover cách đọc tree từ node/branch/tip, sister taxa, clade, homology/convergence, molecular phylogenetics, molecular clock, taxonomy, species concept, three domains, endosymbiosis, horizontal transfer, richness/evenness, Shannon diversity và mass extinction.

Người mới có đủ context để không đọc tree bằng vị trí trái/phải.

## `02_microorganisms_and_viruses.md`

Cover bacteria/archaea, Gram envelope, metabolic diversity, nitrogen fixation, microbiome, symbiosis, horizontal gene transfer, antibiotic resistance, virus architecture/life-cycle abstraction, genome strategy, retrovirus, phage, viral evolution và immune connection.

Microbiology được viết như node nối chemistry, metabolism, evolution và ecology chứ không phải appendix về pathogen.

### Audit kết luận

Evolutionary framework hiện nối trực tiếp variation ở molecular scale với biodiversity ở biosphere scale.

---

# 5. Organismal Biology — mechanism trước anatomy

## `00_plant_biology.md`

Bắt đầu bằng bài toán organism cố định phải lấy CO₂/light từ air và water/mineral từ soil.

Cover tissue, root, mycorrhiza, xylem, cohesion–tension, water potential, phloem pressure flow, leaf/stomata trade-off, meristem, hormone, tropism, flower, seed, alternation of generations và land-plant evolution.

Plant không còn bị mô tả như danh sách organ.

## `01_animal_physiology_and_homeostasis.md`

Bắt đầu từ internal logistics.

Cover tissue, homeostasis, digestion/absorption, circulation và pressure/resistance, gas exchange/partial pressure/hemoglobin, nephron/countercurrent, osmoregulation, acid–base balance, thermoregulation, exercise integration và allostasis.

Các hệ organ được nối bằng flow và feedback.

## `02_nervous_endocrine_and_immune_systems.md`

Ba system được đặt chung vì cùng giải bài toán information/control/recognition nhưng ở timescale và mechanism khác nhau.

Cover resting/action potential, myelin, synapse, CNS/PNS/reflex, hormone/receptor, endocrine axis, glucose/stress regulation, barrier, innate/adaptive immunity, inflammation, phagocytosis, B/T cell, antibody, MHC, memory, tolerance và allergy.

## `03_reproduction_and_development.md`

Cover sexual/asexual reproduction, gametogenesis, fertilization, cleavage, gastrulation, germ layers, differentiation, competence, morphogen, induction, Hox, organogenesis, stem-cell potency, regeneration, reproductive endocrine axis, pregnancy, sex determination, aging và evo-devo.

Development được giải thích như gene regulation + signaling + mechanics trong space/time, không phải “cell divide rồi thành body”.

### Audit kết luận

Organismal biology đủ nền để người đọc hiểu whole-body function mà chưa cần một human anatomy atlas riêng.

---

# 6. Ecology — từ individual decision đến planetary matter cycle

## `00_population_community_and_behavior.md`

Cover behavior mechanism/function, learning, foraging trade-off, kin selection/Hamilton rule, exponential/logistic growth, carrying capacity, life history, survivorship, metapopulation, niche, competition, predator–prey model, mutualism, keystone species, food web, trophic cascade, succession và island biogeography.

Mathematical model được giải thích bằng variable và assumption thay vì chỉ đưa formula.

## `01_ecosystems_biogeochemical_cycles_and_conservation.md`

Cover GPP/NPP, trophic efficiency, energy pyramid, decomposition, carbon/nitrogen/phosphorus/water cycle, eutrophication, biome/aquatic system, disturbance, resistance/resilience, alternative stable state, small-population conservation, fragmentation, ecosystem service, climate forcing và phenology.

Key distinction được giữ xuyên file:

> Matter cycles; energy flows.

### Audit kết luận

Ecology đã nối đầy đủ organism → population → community → ecosystem → Earth system ở mức Biology core.

---

# 7. Biotechnology & Computation

## `00_biotechnology_bioinformatics_and_systems_biology.md`

Kỹ thuật được tổ chức theo problem:

```text
too little DNA → PCR
need size separation → electrophoresis
need base order → sequencing
millions reads → bioinformatics
need controlled sequence change → genome editing
thousands interactions → systems biology
```

Cover DNA extraction, gel electrophoresis, PCR/qPCR, restriction/cloning, recombinant protein, Sanger/NGS/long-read, alignment, dynamic programming, assembly/de Bruijn graph, mapping, variant calling, RNA-seq, multiple testing, single-cell, CRISPR, gene therapy distinction, omics, systems/dynamic model, ML, synthetic biology và ethics.

### Audit kết luận

Biotech/CS connection hiện được giải thích ở mechanism level chứ không phải một “IT applications” list.

---

# 8. Cross-domain connections

## `90_connections/00_biology_math_computation_and_scale.md`

Đã rewrite để giải thích trực tiếp các pattern toán học:

- surface/volume scaling;
- diffusion/random walk;
- exponential/logistic growth;
- Michaelis–Menten saturation;
- logarithm/pH;
- binomial probability;
- Bayes và base rate;
- statistics/multiple testing;
- vector/PCA;
- graph/network;
- differential equation/steady state;
- feedback/control theory;
- Shannon information;
- optimization/trade-off;
- string matching/dynamic programming/indexing;
- machine learning và multiscale modeling.

Đây là file giúp người có background IT/Math nhìn thấy Biology không phải một domain tách biệt.

---

# 9. Zero-background readability audit

Mỗi chapter core sau rewrite phải đáp ứng các checkpoint sau:

| Tiêu chí | Trạng thái |
|---|---|
| Không giả định người đọc nhớ Biology phổ thông | Đạt |
| Khái niệm mới có problem/phenomenon trước definition | Đạt |
| Keyword có English/Korean khi xuất hiện quan trọng | Đạt |
| Main explanation dùng paragraph, không biến thành bullet notes | Đạt |
| Formula có intuition/variable/assumption | Đạt |
| Có Mental Model | Đạt |
| Có Common Misconceptions ở chủ đề dễ nhầm | Đạt |
| Cross-link theo dependency | Đạt |
| Không tổ chức Beginner/Intermediate/Advanced | Đạt |
| Connection Math/IT xuất hiện trong context | Đạt |

---

# 10. Dependency audit

Luồng chính hiện là:

```text
scientific thinking
      ↓
what is life
      ↓
chemistry / water / energy
      ↓
biomolecules / enzymes / ATP
      ↓
cell organization / transport
      ↓
metabolism + signaling
      ↓
DNA / gene expression
      ↓
inheritance / variation
      ↓
evolution
      ↓
phylogeny / biodiversity
      ↓
population / ecosystem
```

Các nhánh:

```text
cell + signaling
      ↓
physiology / development

DNA + genomics
      ↓
biotechnology / bioinformatics

microbiology
  ↙    ↓    ↘
cell  evolution  ecology
```

Không có chapter chính nào cần knowledge chỉ được định nghĩa ở một file sau mà không có local context tối thiểu.

---

# 11. Những gì cố ý chưa biến thành library chuyên ngành

Biology core hiện cover breadth và mechanism đủ để mở specialization, nhưng không cố nhét toàn bộ university major vào một folder.

Các domain tự nhiên có thể tách riêng khi cần:

- Biochemistry — enzyme kinetics, structural biology, metabolism sâu;
- Neuroscience — sensory/motor system, learning, memory, cognition;
- Immunology — lymphocyte development, cytokine network, immunopathology;
- Microbiology — microbial genetics/ecology/pathogenesis chi tiết;
- Human Biology/Anatomy — anatomy theo organ, nutrition, pathology foundation;
- Developmental Biology — embryology và gene regulatory network sâu;
- Bioinformatics — algorithms, statistical genomics, structural bioinformatics;
- Molecular Biotechnology — experimental design, assay engineering và industrial biotech.

Đây là **specialization candidates**, không phải khoảng trống prerequisite của Biology core.

---

# 12. Final conclusion

Bản đầu của Biology Library có coverage rộng nhưng nội dung khoảng 5–8 KB/chapter khiến nhiều chủ đề vẫn có cảm giác outline mở rộng. Sau rewrite, thư viện đã được chuyển sang hướng textbook cho zero-background learner: nền Hóa học được tách rõ, biomolecule được thêm thành conceptual bridge, các chapter cell/genetics/evolution/physiology/ecology được viết lại theo causal flow và mỗi formula/model được đặt vào reasoning context.

Mục tiêu hiện tại không còn là:

> “Biết Sinh học có những phần nào.”

Mà là:

> “Khi gặp một biological phenomenon, biết xác định scale, theo dõi matter–energy–information flow, tìm feedback/constraint và nối nó với molecular mechanism hoặc evolutionary/ecological process phù hợp.”

Theo tiêu chuẩn của Knowledge Library, core Biology hiện đạt mức **foundation-complete và conceptually connected** để đọc từ số 0 và làm nền cho các thư viện chuyên sâu.