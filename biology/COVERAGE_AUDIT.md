# Biology Knowledge Library — Coverage & Continuity Audit

File này không phải summary kiến thức. Nó kiểm tra hai việc riêng biệt nhưng quan trọng như nhau:

1. **Coverage:** các idea cốt lõi của Biology đã được cover chưa?
2. **Continuity:** knowledge có được xây theo dependency hay vẫn là các chapter đứng cạnh nhau?

Phiên bản audit này được thêm sau khi toàn bộ library được rewrite theo yêu cầu “người chưa có nền tảng vẫn đọc liền mạch”. Tiêu chuẩn không còn là “file có nhắc tới keyword hay chưa”, mà là **keyword đó có được sinh ra từ câu hỏi trước, được giải thích đủ context và được tái sử dụng ở chapter sau hay không**.

## 1. Continuity backbone

Core flow hiện tại:

```text
scientific thinking
      ↓
what is life
      ↓
chemistry / water / energy
      ↓
biomolecules / enzymes / ATP
      ↓
cell organization / membrane / transport
      ↓
metabolism
      ↓
signaling / cell cycle
      ↓
DNA / gene expression
      ↓
inheritance / variation
      ↓
genomics / regulation
      ↓
evolution / population genetics
      ↓
phylogeny / biodiversity
      ↓
microbiology
      ↓
multicellular organism
      ↓
physiology / control / development
      ↓
population / community
      ↓
ecosystem / Earth cycles
      ↓
biotechnology / computation
      ↓
cross-scale connections
```

Flow này là conceptual dependency, không phải difficulty level.

## 2. Foundation audit

### `00_scientific_thinking_scale_and_models.md`

File này hiện làm đúng vai trò “language of reasoning”. Nó giải thích system thinking, causal chain, model, scale, emergence, structure–function, matter/energy/information flow, feedback, variation, probability, gradient, rate và network.

Quan trọng hơn, các concept này được tái sử dụng sau đó:

- gradient → membrane transport, mitochondria, xylem, gas exchange, morphogen;
- feedback → enzyme regulation, cell cycle, endocrine, population density;
- scale → molecular → cell → organism → population → ecosystem;
- causal reasoning → genomics, microbiome, ecology, ML.

### `00_what_is_life.md`

File này không còn liệt kê “đặc điểm của sự sống”, mà xây chain:

```text
boundary
→ metabolism
→ homeostasis
→ information
→ reproduction
→ variation
→ evolution
```

Chapter kết thúc bằng nhu cầu hiểu chemistry, tạo bridge tự nhiên sang file tiếp theo.

### `01_chemistry_energy_and_water.md`

Chemistry được giới hạn đúng phạm vi Biology nhưng không viết kiểu cheat sheet. Atom/bond → polarity → water → hydrophobic effect → diffusion/ion → pH/buffer → free energy → redox.

Mỗi phần có downstream dependency rõ:

- hydrophobic effect → membrane;
- pH/buffer → protein + physiology;
- redox → respiration/photosynthesis;
- electrochemical gradient → neuron + ATP synthesis.

### `02_biomolecules_enzymes_and_energy.md`

Bốn biomolecule không còn là bốn list. Chúng được tổ chức quanh problem solving:

- carbohydrate → carbon/fuel/structure;
- lipid → energy density + boundary;
- protein → catalysis/structure/signaling;
- nucleic acid → templated information.

Enzyme regulation và ATP tạo bridge trực tiếp sang metabolism/cell biology.

**Foundation continuity: đạt.**

## 3. Cell Biology audit

### `00_cells_membranes_and_transport.md`

Cell được xây từ organization problem. Membrane không được giới thiệu như một object có sẵn, mà xuất hiện vì hệ sống cần giữ internal chemistry khác environment.

Diffusion → facilitated diffusion → active transport → electrochemical gradient → membrane potential tạo một flow logic duy nhất.

Organelle được giải thích như lời giải cho compartmentalization chứ không phải danh sách chức năng.

Surface-area-to-volume nối trực tiếp cell size với nhu cầu circulatory system ở organism lớn.

### `01_metabolism_respiration_photosynthesis.md`

Không tổ chức theo “glycolysis/Krebs/ETC phải nhớ”. Chapter theo electron và energy transformation:

```text
nutrient
→ electron carriers
→ electron transport
→ proton gradient
→ ATP
```

Photosynthesis sau đó reuse cùng chemiosmosis pattern.

Chapter kết thúc bằng câu hỏi regulation, dẫn sang signaling.

### `02_cell_signaling_and_cell_cycle.md`

Signaling được đặt như control layer của metabolism. Receptor → transduction → response → feedback → cell-cycle decision.

Mitosis/meiosis không đứng riêng; meiosis trở thành bridge sang inheritance. Cancer nối mutation + signaling + selection.

**Cell Biology continuity: đạt.**

## 4. Genetics & Molecular Biology audit

### `00_dna_genes_and_gene_expression.md`

Information problem → DNA structure → template copying → transcription → RNA processing → translation → gene regulation.

Central dogma được giải thích như map thông tin, không phải dogma “DNA quyết định mọi thứ”.

### `01_inheritance_variation_and_mutation.md`

Mendelian genetics được dựng trên chromosome mechanics. Segregation ratio được giải từ meiosis và probability.

Linkage/recombination được nối physical distance trên chromosome.

Mutation tạo allele mới; recombination tạo combination mới; hai process cùng tạo raw variation cho evolution.

### `02_genomics_epigenetics_and_regulation.md`

Genome → chromatin → transcriptome → proteome → omics → GWAS.

Statistical association được tách khỏi causal mechanism.

Chapter kết thúc bằng allele frequency trong population, đưa thẳng sang population genetics.

**Genetics continuity: đạt.**

## 5. Evolution, Diversity & Microbiology audit

### `00_evolution_and_population_genetics.md`

Evolution được xây trực tiếp từ inheritance: allele frequency trở thành unit đo. Hardy–Weinberg là null model. Mutation, selection, drift và gene flow là force làm frequency đổi.

Adaptation được giải thích bằng differential reproduction, tránh teleology.

Speciation được trình bày như population divergence kéo dài.

### `01_phylogeny_taxonomy_and_biodiversity.md`

Speciation dẫn tới branching lineage, nên phylogenetic tree xuất hiện tự nhiên.

Tree reading, homology, clade, molecular phylogeny và taxonomy được nối vào một lịch sử chung.

### `02_microorganisms_and_viruses.md`

Microbiology đóng vai trò hub:

- cell biology → bacterial cell;
- metabolism → metabolic diversity;
- genetics → horizontal gene transfer;
- evolution → resistance;
- ecology → microbiome/nutrient cycle;
- biotechnology → CRISPR.

**Evolution/diversity continuity: đạt.**

## 6. Organismal Biology audit

### `00_plant_biology.md`

Plant được xây quanh một problem thống nhất: resource nằm ở hai môi trường soil/air.

Root → xylem → stomata → phloem → hormone → reproduction.

Hydrogen bonding của water từ chemistry được tái sử dụng ở cohesion–tension. Osmosis từ cell biology được tái sử dụng ở turgor/phloem.

### `01_animal_physiology_and_homeostasis.md`

Các organ system được gộp quanh việc duy trì extracellular environment.

Diffusion limitation tạo nhu cầu bulk circulation; gas exchange nối partial pressure; acid–base nối lung–kidney; metabolism nối exercise response.

### `02_nervous_endocrine_and_immune_systems.md`

Ba system được thống nhất bởi communication architecture. Membrane gradient → action potential; vesicle transport → synapse; receptor signaling → hormone; selection-like clonal expansion → adaptive immunity.

### `03_reproduction_and_development.md`

Development trả lời genotype → phenotype bằng intermediate layer: gene-regulatory network → cell fate → tissue interaction → organ morphology.

Morphogen gradient reuse diffusion; apoptosis reuse cell-cycle/control; Hox gene nối development với evolution.

**Organismal continuity: đạt.**

## 7. Ecology audit

### `00_population_community_and_behavior.md`

Scale chuyển từ organism sang population bằng demographic accounting. Exponential → logistic growth được xây qua resource limitation và feedback.

Behavior nối energy budget với fitness. Competition/predation tạo community network.

### `01_ecosystems_biogeochemical_cycles_and_conservation.md`

Community được mở rộng bằng abiotic environment.

Photosynthesis từ cell biology trở thành GPP/NPP; microbial metabolism trở thành nitrogen/carbon cycle; food web trở thành energy transfer network; fragmentation quay về population genetics.

Conservation vì thế xuất hiện như application của toàn bộ knowledge trước đó, không phải section đạo đức rời rạc.

**Ecology continuity: đạt.**

## 8. Biotechnology & Computation audit

### `00_biotechnology_bioinformatics_and_systems_biology.md`

Tool được truy về natural mechanism:

- replication → PCR;
- phosphate charge → electrophoresis;
- plasmid biology → cloning;
- base pairing → sequencing/alignment;
- graph theory → assembly;
- microbial immunity → CRISPR;
- regulatory network → synthetic/systems biology.

Phần computation phân biệt measurement, inference, prediction và causality.

**Technology continuity: đạt.**

## 9. Cross-domain connections audit

### `90_connections/00_biology_math_computation_and_scale.md`

File connections hiện không lặp lại nội dung từng chapter. Nó tổ chức theo mathematical/structural pattern:

- gradient;
- feedback;
- exponential growth;
- saturation;
- probability/Bayes;
- rate/differential equation;
- conservation/mass balance;
- graph/network;
- information theory;
- logarithm;
- optimization/control;
- signal processing;
- reproducible computation.

Các pattern được trỏ ngược về nhiều scale, giúp knowledge transfer.

## 10. Continuity matrix — chapter nào truyền gì cho chapter nào?

| Từ chapter | Concept truyền đi | Sang chapter |
|---|---|---|
| Scientific thinking | scale, gradient, feedback, causal reasoning | toàn library |
| What is life | boundary, metabolism, information | chemistry/cell |
| Chemistry | polarity, pH, redox, free energy | biomolecule/metabolism |
| Biomolecules | lipid bilayer, enzyme, ATP, nucleic acid | cell/genetics |
| Cell organization | membrane, compartment, gradient | metabolism/physiology |
| Metabolism | electron flow, ATP, energy demand | signaling/physiology/ecology |
| Signaling | receptor, feedback, state control | gene regulation/physiology |
| DNA expression | sequence → RNA → protein | inheritance/development/biotech |
| Inheritance | meiosis, variation, probability | genomics/evolution |
| Genomics | chromatin, omics, population variant | evolution/biotech |
| Evolution | selection, drift, divergence | phylogeny/ecology |
| Phylogeny | lineage, biodiversity | microbiology/ecology |
| Microbiology | HGT, resistance, nutrient metabolism | ecology/biotech |
| Plant biology | transport, water balance | ecology |
| Animal physiology | homeostasis, transport | control systems |
| Neural/endocrine/immune | communication + feedback | development/behavior |
| Development | genotype → multicellular phenotype | evolution/ecology |
| Population/community | dynamics + interaction network | ecosystem |
| Ecosystem | matter cycle + energy flow | conservation/global biology |
| Biotechnology | measurement/manipulation | computation/systems biology |

## 11. Common concepts intentionally repeated

Một số concept xuất hiện nhiều lần có chủ đích, nhưng mỗi lần ở scale mới.

**Gradient**: chemistry → membrane → mitochondria → neuron → morphogen → xylem/lung.

**Feedback**: enzyme → cell cycle → endocrine → immune → population/ecosystem.

**Selection**: organism evolution → immune clonal selection → tumor evolution → antibiotic resistance.

**Network**: metabolism → signaling → gene regulation → neural circuit → food web → systems biology.

Đây không được coi là duplication xấu. Đây là **spaced conceptual reuse**, giúp người đọc nhận ra pattern.

## 12. Những nội dung không cố nhồi sâu vào core library

Core library không cố biến thành medical school hoặc specialist textbook. Một số domain đủ lớn để tách riêng sau này:

- biochemistry chuyên sâu: enzyme kinetics, structural biology, metabolic regulation chi tiết;
- neuroscience: sensory system, motor control, memory, cognition;
- immunology: antigen presentation, lymphocyte development, cytokine network;
- microbiology/virology: taxonomy, pathogenesis, industrial microbiology;
- human anatomy/pathology;
- bioinformatics chuyên sâu: algorithms, workflow, statistical genetics;
- developmental biology/evo-devo chuyên sâu.

Những phần này **không bị bỏ qua hoàn toàn**; core mechanism cần thiết đã có trong Biology Library. Chúng chỉ không được mở rộng đến specialization depth.

## 13. Readability audit cho người bắt đầu từ số 0

Mỗi chapter hiện phải đáp ứng các rule sau:

**Rule 1 — Không mở chapter bằng definition dump.** Mở bằng vấn đề mà chapter cần giải quyết.

**Rule 2 — Concept mới phải có dependency.** Ví dụ ATP chỉ xuất hiện sau free energy; action potential chỉ xuất hiện sau ion gradient.

**Rule 3 — Công thức phải được đọc bằng lời.** Equation được dùng để formalize relationship đã hiểu trước.

**Rule 4 — Bridge cuối chapter là bắt buộc.** Phần cuối chỉ ra câu hỏi chưa giải được và dẫn sang chapter tiếp.

**Rule 5 — Cross-scale reuse.** Concept nền phải được nhắc lại vừa đủ khi dùng ở scale mới.

**Rule 6 — English/Korean keyword không thay cho giải thích.** Term chỉ được note sau/đồng thời với context.

**Rule 7 — Không ép IT application.** Connection computation chỉ xuất hiện khi mathematical/data structure thật sự tương ứng.

## 14. Final audit conclusion

Library hiện không còn được thiết kế như 19 note độc lập. Nó có một causal backbone thống nhất:

> **chemistry tạo interaction → interaction tạo structure → structure cho phép cell process → process cần energy và regulation → regulation dùng information → information được inherited với variation → variation tạo evolution → evolution tạo diversity → multicellularity tạo coordination problem → organism interaction tạo ecology → con người đo và thao tác các process đó bằng biotechnology/computation.**

Đây là standard cần được giữ khi mở rộng library sau này. Một file mới chỉ nên được thêm nếu nó có conceptual boundary rõ ràng và phải trả lời hai câu hỏi trước khi merge:

**Nó nhận dependency gì từ kiến thức đã có?**

**Sau khi đọc nó, người học có thêm mental model nào để hiểu chapter khác hoặc vấn đề thật?**

Theo audit hiện tại, Biology Knowledge Library đạt mức **core-complete và continuity-oriented** cho mục tiêu học lại từ nền tảng bằng first-principles, đồng thời vẫn giữ đường mở tự nhiên sang các specialized library.