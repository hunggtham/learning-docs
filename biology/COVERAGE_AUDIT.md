# Biology Knowledge Library — Coverage & Continuity Audit

File này kiểm tra thư viện Sinh học theo hai tiêu chí đồng thời:

1. **Coverage** — các conceptual boundary cốt lõi của Biology đã được bao phủ chưa?
2. **Continuity** — các chapter có thật sự truyền mental model cho nhau hay chỉ đứng cạnh nhau như note riêng lẻ?

Nó không phải summary và không thay thế nội dung học.

---

## 1. Tiêu chuẩn audit hiện tại

Một chapter chỉ được xem là đạt khi có đủ các lớp sau ở mức phù hợp với chủ đề:

```text
problem / constraint
→ first-principles components
→ mechanism
→ structure/model
→ quantitative relation nếu cần
→ examples/case studies
→ limitations / assumptions
→ common misconceptions
→ cross-domain connection
→ explicit bridge sang chapter tiếp theo
```

Chapter không đạt nếu chỉ có definition + list property + application.

---

## 2. Foundations

### `00_foundations/00_scientific_thinking_scale_and_models.md`

Đã cover:

- systems thinking;
- observation vs mechanism;
- correlation vs causation;
- control/confounder;
- scientific model và assumption;
- biological scales;
- emergent properties;
- surface-area-to-volume ratio;
- structure–function;
- matter/energy/information flow;
- feedback;
- probability/variation;
- rate, gradient, network.

Continuity: chapter tạo vocabulary reasoning được dùng lại xuyên library. Nó dẫn trực tiếp sang câu hỏi “life là gì?”.

### `00_foundations/00_what_is_life.md`

Đã cover:

- boundary;
- metabolism;
- homeostasis;
- information;
- reproduction/lineage;
- evolution;
- cell theory;
- prokaryote/eukaryote;
- multicellularity;
- virus/prion/dormancy boundary case;
- entropy/non-equilibrium;
- origin-of-life framing;
- emergence.

Continuity: từ concept life tạo câu hỏi chemistry nào cho phép boundary, metabolism và information tồn tại.

### `00_foundations/01_chemistry_energy_and_water.md`

Đã cover atom, ion, covalent bond, polarity, water, hydrogen bonding, hydrophobic effect, functional groups, pH, buffer, free energy, thermodynamics vs kinetics, entropy, redox, diffusion, equilibrium và osmosis.

Continuity: chemistry không đứng riêng; mỗi concept được nối tới membrane, enzyme, respiration, physiology hoặc ecology.

### `00_foundations/02_biomolecules_enzymes_and_energy.md`

Đã cover carbohydrate, lipid, protein, protein folding, enzyme, enzyme kinetics, feedback inhibition, ATP, energy coupling, NADH/FADH₂, nucleic acid, molecular recognition và compartmentalization.

Continuity: chapter kết thúc ở vấn đề “có molecule nhưng chưa có architecture”, dẫn sang cell biology.

**Foundation status: COMPLETE for core Biology.**

---

## 3. Cell Biology

### `01_cell_biology/00_cells_membranes_and_transport.md`

Đã cover:

- cell size/SA:V;
- prokaryotic vs eukaryotic organization;
- compartmentalization;
- fluid membrane;
- selective permeability;
- diffusion/Fick intuition;
- facilitated diffusion;
- osmosis/tonicity;
- active/secondary active transport;
- electrochemical gradient;
- membrane potential;
- endocytosis/exocytosis;
- nucleus/ribosome/ER/Golgi/lysosome;
- cytoskeleton/motor protein;
- ECM/junction;
- endosymbiosis;
- clinical mechanism examples.

Continuity: membrane gradient trở thành prerequisite cho respiration và action potential.

### `01_cell_biology/01_metabolism_respiration_photosynthesis.md`

Đã cover metabolic network, glycolysis, fermentation, acetyl-CoA, TCA, electron transport, oxygen role, chemiosmosis, ATP synthase, lipid metabolism, photosystem, water splitting, NADPH, Calvin cycle, photorespiration, C4/CAM connection, metabolic regulation và case studies.

Continuity: energy machinery dẫn sang control/signaling.

### `01_cell_biology/02_cell_signaling_and_cell_cycle.md`

Đã cover receptor classes, GPCR, RTK, second messenger, Ca²⁺, phosphorylation, amplification, cross-talk, feedback, gene-expression response, cell cycle, cyclin/CDK, checkpoint, p53, mitosis, meiosis, apoptosis và cancer as control failure.

Continuity: signaling → transcription tạo bridge sang DNA/gene expression; meiosis tạo bridge sang inheritance.

**Cell Biology status: COMPLETE for core Biology.**

---

## 4. Genetics and Molecular Biology

### `02_genetics_molecular_biology/00_dna_genes_and_gene_expression.md`

Đã cover genome/chromosome/gene, DNA structure/directionality, replication, repair, mutation, transcription, promoter/enhancer, RNA processing, RNA roles, genetic code, translation, protein targeting, central dogma nuance, bacterial/eukaryotic regulation, chromatin, epigenetic state, gene network, sequencing/CRISPR connection.

Continuity: DNA information → meiosis/inheritance.

### `01_inheritance_variation_and_mutation.md`

Đã cover diploidy, homolog vs chromatid, meiosis, assortment, crossing-over, Mendel, dominance mechanisms, probability, incomplete dominance/codominance, pleiotropy, polygenic trait, epistasis, linkage, sex-linked inheritance, mutation types, germline/somatic mutation, nondisjunction, quantitative genetics, heritability, G×E, penetrance, pedigree, mitochondrial inheritance và population variation.

Continuity: individual/family genetics → genome-wide data → population genetics.

### `02_genomics_epigenetics_and_regulation.md`

Đã cover genome architecture, chromatin state, histone modification, DNA methylation, epigenetics scope/limitations, X inactivation, imprinting, 3D genome, RNA/post-transcription regulation, omics, sequencing/reference/pangenome, GWAS, LD, polygenic score, single-cell, developmental regulatory state, CRISPR screen và systems biology.

Continuity: genome variation → population evolution; regulatory network → development; omics → bioinformatics.

**Genetics status: COMPLETE for general Biology, intentionally below clinical-genetics specialization.**

---

## 5. Evolution, Diversity and Microbiology

### `03_evolution_and_diversity/00_evolution_and_population_genetics.md`

Đã cover population frequency, Hardy–Weinberg, mutation, selection/fitness, selection modes, frequency dependence, sexual selection, drift, effective population size, bottleneck/founder effect, gene flow, recombination, adaptation/trade-off, local adaptation, plasticity, speciation, reproductive isolation, molecular evolution, molecular clock, coevolution và evolutionary medicine.

Continuity: genetics được chuyển thành population dynamics; branching dẫn sang phylogeny.

### `01_phylogeny_taxonomy_and_biodiversity.md`

Đã cover tree reading, clade/sister taxa, homology/convergence, synapomorphy, molecular phylogenetics, alignment, parsimony/likelihood/Bayesian framing, support, molecular clock, taxonomy, three domains, major diversity, extinction, adaptive radiation, HGT, endosymbiosis, biogeography và conservation phylogenetic diversity.

Continuity: phylogenetic history dẫn sang microbial/viral evolution.

### `02_microorganisms_and_viruses.md`

Đã cover bacterial/archaeal architecture, Gram envelope, microbial metabolism, growth curve, biofilm, quorum sensing, HGT, plasmid, antibiotic mechanism/resistance, microbiome, symbiosis, pathogenesis, virus structure/lifecycle/tropism, RNA virus, retrovirus, phage, CRISPR và One Health.

Continuity: microbe nối cell biology, genetics, evolution, ecology và biotechnology.

**Evolution/Diversity/Microbiology status: COMPLETE at general-biology scope.**

---

## 6. Organismal Biology

### `04_organismal_biology/00_plant_biology.md`

Đã cover land-plant constraints, root/shoot, meristem/tissue, xylem cohesion–tension, water potential, root selective uptake, mineral/mycorrhiza, stomata, transpiration trade-off, C3/C4/CAM, phloem pressure flow, hormone/tropism, ABA, circadian/photoperiod, flower/pollination/fertilization, seed/fruit, defense và case studies.

Continuity: cell transport/osmosis → whole-plant hydraulics; photosynthesis → source–sink; hormone → organism coordination.

### `01_animal_physiology_and_homeostasis.md`

Đã cover diffusion limitation, homeostasis, pressure/flow/resistance, heart/vessel/blood, hemoglobin/gas exchange, ventilation-perfusion, acid-base, digestion/absorption, liver, kidney/nephron/countercurrent, ADH/RAAS, thermoregulation, muscle, glucose regulation, allostasis, dehydration và altitude response.

Continuity: cell-level transport/metabolism → organ-level bulk flow/control.

### `02_nervous_endocrine_and_immune_systems.md`

Đã cover neuron/resting potential/action potential/myelin/synapse, sensory/reflex/plasticity, endocrine signaling, hypothalamus–pituitary axes, stress, innate/adaptive immunity, antigen presentation, B/T cell, clonal selection, vaccine, tolerance/autoimmunity/allergy và neuroendocrine–immune integration.

Continuity: membrane gradient + receptor signaling được reuse ở information systems của organism.

### `03_reproduction_and_development.md`

Đã cover sexual/asexual reproduction, gametogenesis/fertilization, cleavage/gastrulation, germ layers, differentiation, stem cell, induction, morphogen, reaction–diffusion, Hox, segmentation, migration, tissue mechanics, apoptosis, asymmetry, placenta, evo-devo, regeneration, aging, senescence và developmental disease concepts.

Continuity: genetics + signaling + mechanics → multicellular form; organism → ecology.

**Organismal Biology status: COMPLETE for mechanistic core, intentionally not anatomy atlas.**

---

## 7. Ecology

### `05_ecology/00_population_community_and_behavior.md`

Đã cover demographic structure, exponential/logistic growth, doubling time, density dependence, life history, survivorship, metapopulation, behavior, foraging, territoriality, kin selection, cooperation/game-theory framing, niche, competition/resource partition, predator–prey equations, functional response, mutualism/parasitism, keystone/trophic cascade, food web, disease ecology, invasion và succession.

Continuity: organism behavior/fitness → population/community network → ecosystem flow.

### `01_ecosystems_biogeochemical_cycles_and_conservation.md`

Đã cover GPP/NPP, trophic transfer, ecological pyramid, detrital web, carbon/nitrogen/phosphorus/water cycles, limiting nutrient/eutrophication, biome/climate, disturbance, resistance/resilience, alternative stable state, island biogeography, fragmentation, ecosystem service, climate effects, ocean acidification, conservation genetics, inbreeding, restoration và adaptive management.

Continuity: energy/matter principles từ cellular metabolism xuất hiện lại ở biosphere scale.

**Ecology status: COMPLETE for core Biology.**

---

## 8. Biotechnology and Computation

### `06_biotechnology_computation/00_biotechnology_bioinformatics_and_systems_biology.md`

Đã cover PCR/qPCR/RT-PCR, electrophoresis, recombinant DNA/plasmid, sequencing, FASTA/FASTQ, alignment/BLAST, genome assembly, variant calling, RNA-seq/single-cell, dimensionality reduction, CRISPR/base/prime editing, functional genomics, synthetic biology, metabolic engineering, ODE/network systems biology, ML, protein structure prediction, reproducibility, causality và ethics.

Continuity: tool được giải thích từ mechanism đã học trước; computation xuất hiện vì scale data/mạng quá lớn.

**Biotechnology/Computation status: COMPLETE as bridge into specialized computational biology.**

---

## 9. Cross-domain connections

### `90_connections/00_biology_math_computation_and_scale.md`

Đã cover recurring motifs:

- scale/SA:V;
- rate/derivative;
- exponential/logistic/saturation;
- logarithm;
- gradient;
- flow/resistance;
- feedback/delay;
- probability/Bayes;
- sampling/multiple testing;
- causality/DAG;
- graph/tree;
- information theory;
- alignment algorithms;
- optimization/trade-off;
- dimensional analysis;
- normalization;
- ML/overfitting;
- dynamical/stochastic systems;
- simulation;
- cross-scale motifs “difference → flow → feedback” và “variation → selection → memory”.

**Connections status: COMPLETE as synthesis chapter, not a summary.**

---

## 10. Continuity audit — các bridge bắt buộc

Dòng chính hiện được giữ như sau:

```text
scientific thinking
→ what is life
→ chemistry/water/energy
→ biomolecules/enzyme/ATP
→ cell architecture/membrane/gradient
→ metabolism/chemiosmosis
→ signaling/cell cycle
→ DNA/gene expression
→ inheritance/variation
→ genomics + population genetics
→ evolution
→ phylogeny/diversity
→ organismal physiology/development
→ population/community
→ ecosystem cycles
→ biotechnology/computation
→ cross-domain synthesis
```

Các branch quan trọng:

```text
cell membrane → neuron action potential
cell membrane → kidney transport
cell membrane → plant water balance

redox/ETC → mitochondria respiration
redox/ETC → chloroplast photosynthesis

meiosis → Mendel/recombination
mutation → evolution
mutation → cancer

signaling → endocrine
signaling → immune
signaling + gene regulation → development

evolution → phylogeny
microbial evolution → antibiotic resistance
phylogeny + ecology → conservation

genomics → sequencing → bioinformatics
network biology → systems biology → ML
```

Không chapter nào trong core chain còn được coi là độc lập hoàn toàn.

---

## 11. Cross-scale consistency audit

Một số concept được cố ý lặp ở scale mới để reinforce knowledge graph:

### Gradient

water/solute chemistry → membrane diffusion → ion gradient → proton gradient → action potential → water potential plant → morphogen → biofilm/ecosystem gradient.

### Feedback

enzyme inhibition → signaling → cell-cycle checkpoint → endocrine → immune regulation → homeostasis → population density → ecosystem resilience.

### Information

DNA sequence → gene expression → cell signaling → development → heredity → evolution → phylogeny → sequencing data.

### Energy

chemical free energy → ATP → cellular work → organism metabolism → primary production → trophic transfer.

### Variation

mutation/recombination → individual genotype → population allele frequency → natural selection → phylogenetic diversification; clonal variation còn xuất hiện trong immunity/cancer/microbes.

Các repetition này là deliberate connection, không phải duplicate content.

---

## 12. Những gì cố ý chưa tách thành core chapter riêng

Các domain dưới đây đủ lớn để thành library chuyên sâu nhưng không phải “missing fundamental”:

1. **Biochemistry / Structural Biology** — enzyme mechanism sâu, protein structure methods, metabolic pathways chi tiết.
2. **Neuroscience** — sensory systems, motor control, learning, cognition, neuroanatomy.
3. **Immunology** — T/B-cell development, cytokine networks, immunopathology.
4. **Microbiology / Virology** — microbial genetics, pathogenesis, industrial microbiology, virus family.
5. **Human Anatomy / Pathophysiology** — anatomy atlas, organ disease, clinical physiology.
6. **Plant Science** — developmental botany, crop science, plant pathology.
7. **Ecology / Earth Systems** — advanced ecosystem modeling, biogeography, climate feedback.
8. **Bioinformatics / Computational Biology** — algorithms, pipelines, genomics statistics, structural bioinformatics.

Nếu thêm các field này, nên tạo sibling library thay vì làm Biology core phình thành textbook chuyên khoa hàng nghìn trang.

---

## 13. Quality audit đối với người bắt đầu từ số 0

Các chapter hiện đáp ứng các nguyên tắc sau:

- thuật ngữ mới được giải thích trong context;
- không yêu cầu thuộc trước chemistry/genetics phổ thông;
- formula được giải thích variable/relationship/assumption;
- mechanism được ưu tiên trước shortcut;
- ví dụ không chỉ thay số mà giải causal chain;
- misconception giải thích “vì sao dễ hiểu sai”;
- English/Korean keyword được giữ ở concept quan trọng;
- paragraph là format chính, bullet chỉ dùng khi bản chất là list;
- cuối chapter có bridge giải thích tại sao chapter sau xuất hiện.

---

## 14. Final audit conclusion

Biology Knowledge Library hiện không còn ở trạng thái skeleton hoặc collection note. Core chapters đã được deepened theo first-principles flow và liên kết thành một graph từ molecular scale tới biosphere scale.

Coverage hiện bao gồm các idea lớn cấu thành modern general biology:

**organization, chemistry, energy, cell, metabolism, signaling, information, heredity, variation, evolution, diversity, microbial life, physiology, control, development, behavior, ecology, Earth-system cycling, biotechnology và computation.**

Điểm quan trọng hơn coverage là continuity: concept được học ở scale nhỏ được tái sử dụng ở scale lớn hơn thay vì định nghĩa lại rời rạc.

> Tiêu chuẩn cuối cùng của library không phải “đã có bao nhiêu heading”, mà là: khi gặp một phenomenon mới, người đọc có thể lần theo **matter → energy → information → feedback → variation → scale** để tự xây một explanation hợp lý trước khi tra cứu chi tiết chuyên ngành.
