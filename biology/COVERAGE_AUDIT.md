# Biology Knowledge Library — Coverage Audit

File này kiểm tra phạm vi của thư viện Sinh học theo conceptual boundary, dependency và các connection xuyên lĩnh vực. Nó không phải summary kiến thức.

## 1. Foundations

`00_foundations/00_what_is_life.md` xây mental model về sự sống như một process duy trì tổ chức bằng dòng vật chất, năng lượng và thông tin. File này cover cell theory, emergence, scale và evolution như nguyên lý thống nhất.

`00_foundations/01_chemistry_energy_and_water.md` cover carbon chemistry, functional group, water, hydrogen bond, pH, buffer, macromolecule, enzyme, Gibbs free energy, ATP và thermodynamics.

Hai file này tạo prerequisite cho cell biology và biochemistry mà không biến library thành một giáo trình hóa học riêng.

## 2. Cell Biology

`01_cell_biology/00_cells_membranes_and_transport.md` cover prokaryotic/eukaryotic organization, membrane, diffusion, osmosis, active transport, electrochemical gradient, organelle, cytoskeleton, surface-area-to-volume và endosymbiosis.

`01_cell_biology/01_metabolism_respiration_photosynthesis.md` cover redox, glycolysis, pyruvate oxidation, citric-acid cycle, electron transport chain, chemiosmosis, fermentation, photosynthesis và Calvin cycle.

`01_cell_biology/02_cell_signaling_and_cell_cycle.md` cover receptor, kinase/phosphatase, second messenger, feedback, cell cycle, checkpoint, mitosis/meiosis, apoptosis và cancer as regulatory failure.

Đây là core dependency cho genetics, physiology và biotechnology.

## 3. Genetics and Molecular Biology

`02_genetics_molecular_biology/00_dna_genes_and_gene_expression.md` cover DNA structure, replication, transcription, translation, protein processing, central dogma và gene regulation.

`01_inheritance_variation_and_mutation.md` cover Mendelian inheritance, probability, dominance, linkage, recombination, mutation, chromosome abnormality, quantitative trait và heritability.

`02_genomics_epigenetics_and_regulation.md` cover genome organization, chromatin, DNA methylation, enhancer, alternative splicing, RNA regulation, modern omics assay, GWAS và epigenetic inheritance caveat.

Cụm này đủ nền cho modern genetics nhưng không đi quá sâu vào clinical genetics hoặc từng disease riêng lẻ, vì đó là domain y sinh chuyên biệt.

## 4. Evolution, Diversity and Microbiology

`03_evolution_and_diversity/00_evolution_and_population_genetics.md` cover selection, fitness, Hardy–Weinberg, drift, gene flow, mutation, selection mode, speciation và evolutionary medicine.

`01_phylogeny_taxonomy_and_biodiversity.md` cover phylogenetic tree, clade, homology, molecular phylogenetics, molecular clock, taxonomy, three domains, biodiversity và species concepts.

`02_microorganisms_and_viruses.md` bổ sung conceptual boundary còn thiếu của microbiology: Bacteria, Archaea, metabolic diversity, horizontal gene transfer, antibiotic resistance, microbiome, virus, viral evolution, phage/CRISPR, biofilm và quorum sensing.

## 5. Organismal Biology

`04_organismal_biology/00_plant_biology.md` cover plant structure, xylem, phloem, root, stomata, water transport, hormone, tropism và reproduction.

`01_animal_physiology_and_homeostasis.md` cover homeostasis, circulation, gas exchange, digestion, kidney, thermoregulation, muscle và acid–base balance.

`02_nervous_endocrine_and_immune_systems.md` cover neuron, action potential, synapse, nervous-system organization, hormone, endocrine feedback, innate/adaptive immunity, antibody, inflammation và neuroendocrine–immune interaction.

`03_reproduction_and_development.md` cover sexual/asexual reproduction, meiosis, fertilization, differentiation, morphogen, gene-regulatory network, Hox, stem cell, apoptosis và aging connection.

Human anatomy chi tiết theo từng organ không được tách thành atlas riêng vì mục tiêu hiện tại là biological mechanism và system-level understanding. Nếu sau này cần y sinh/human anatomy library, nên tạo domain riêng thay vì phình biology core.

## 6. Ecology

`05_ecology/00_population_community_and_behavior.md` cover population growth, exponential/logistic models, species interaction, niche, competition, predator–prey, food web, behavior và kin selection.

`01_ecosystems_biogeochemical_cycles_and_conservation.md` cover energy flow, GPP/NPP, carbon/nitrogen/phosphorus cycle, nutrient enrichment, succession, island biogeography, conservation, climate-related range shift và resilience.

## 7. Biotechnology and Computation

`06_biotechnology_computation/00_biotechnology_bioinformatics_and_systems_biology.md` cover PCR, electrophoresis, sequencing, CRISPR, recombinant DNA, synthetic biology, alignment, BLAST, assembly graph, omics, machine learning, systems biology và experimental causality.

`90_connections/00_biology_math_computation_and_scale.md` tổng hợp các connection cần mental model xuyên domain: scaling, exponential/logistic growth, probability, statistics, differential equation, graph theory, information theory, optimization, algorithms, machine learning và dimensional analysis.

## 8. Dependency check

Core dependency được giữ theo flow:

```text
chemistry/energy
      ↓
cell structure & transport
      ↓
metabolism + signaling
      ↓
DNA/gene expression
      ↓
inheritance & variation
      ↓
evolution/population genetics
      ↓
phylogeny + ecology
```

Organismal biology tách nhánh từ cell biology và signaling. Biotechnology tách nhánh từ molecular genetics. Microbiology nối cell biology, evolution, ecology và biotechnology.

## 9. Major concepts intentionally not split into separate files

Protein biochemistry, membrane biophysics, developmental genetics, immunology, neuroscience, virology và microbiology đều đủ lớn để trở thành library riêng ở mức university specialization. Trong Biology Knowledge Library này, chúng được cover đến mức xây được correct mental model và dependency cho toàn lĩnh vực, tránh fragment library thành hàng chục note quá nhỏ.

## 10. Remaining expansion candidates

Nếu mở rộng thành specialized library sau này, các candidate tự nhiên là:

1. `biochemistry/` — enzyme kinetics, structural biology, lipid/carbohydrate metabolism sâu hơn.
2. `neuroscience/` — sensory systems, motor control, learning, memory, cognition.
3. `immunology/` — antigen presentation, T/B-cell development, cytokine network, immunopathology.
4. `microbiology/` — microbial ecology, pathogenesis, industrial microbiology.
5. `human_biology/` — anatomy, reproductive physiology, nutrition, pathology foundations.
6. `bioinformatics/` — algorithms, pipelines, genomics statistics, structural bioinformatics.

Các candidate này không phải “missing fundamentals”; chúng là hướng chuyên ngành hóa sau khi biology core đã hoàn chỉnh.

## 11. Final audit conclusion

Library hiện cover các idea lớn cấu thành modern biology: organization, energy, information, inheritance, evolution, regulation, development, physiology, diversity, ecology và technological/computational manipulation of living systems.

Điểm quan trọng nhất là các chủ đề không đứng độc lập. Energy gradient xuất hiện từ membrane đến mitochondria; information đi từ DNA đến development; variation đi từ mutation đến population evolution; scale chuyển từ molecular interaction sang ecosystem dynamics; computation xuất hiện từ genome sequence đến systems biology.

Theo tiêu chuẩn của library này, coverage đạt mức core-complete cho một Biology Knowledge Library tổng quát và có nền đủ tốt để tách ra các thư viện chuyên sâu sau này.
