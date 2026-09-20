# Công nghệ sinh học, Tin sinh học và Systems Biology — Biotechnology, Bioinformatics and Systems Biology (생명공학, 생물정보학과 시스템생물학)

Toàn bộ các chapter trước xây một knowledge graph từ molecule tới ecosystem. Biotechnology bắt đầu khi ta hỏi một câu mới: **nếu đã hiểu mechanism, ta có thể đo, khuếch đại, chỉnh sửa hoặc thiết kế nó như thế nào?** Bioinformatics xuất hiện khi dữ liệu quá lớn để xử lý thủ công; systems biology xuất hiện khi danh sách component không còn đủ để giải thích behavior của network.

> **Mental model:** biotechnology biến biological mechanism thành tool; bioinformatics biến biological data thành representation có thể tính toán; systems biology biến list component thành model về interaction và dynamics.

## 1. Biotechnology không bắt đầu từ CRISPR

Con người đã dùng fermentation, selective breeding và food biotechnology từ lâu trước molecular biology.

Modern biotechnology khác ở mức precision: ta có thể isolate DNA, amplify sequence, sequence genome, edit locus và measure thousands gene cùng lúc.

Nhưng mỗi tool vẫn dựa mechanism tự nhiên: PCR dùng DNA polymerase; restriction enzyme đến từ bacterial defense; CRISPR đến từ microbial immunity.

## 2. PCR: làm một đoạn DNA trở thành hàng triệu copy

**Polymerase chain reaction, PCR (중합효소연쇄반응)** cần template DNA, two primers, thermostable DNA polymerase, nucleotide và buffer.

Một cycle gồm:

1. denaturation: tách DNA strand bằng heat;
2. annealing: primer bind sequence complement;
3. extension: polymerase kéo dài.

Nếu efficiency lý tưởng, amount target tăng gần:

\[
N_n=N_0 2^n
\]

sau \(n\) cycle. Real efficiency thấp hơn 100% và reaction cuối sẽ plateau.

## 3. Primer tạo specificity

PCR không “copy toàn genome”. Primer xác định boundary region được khuếch đại.

Primer design phải cân nhắc melting temperature, GC content, secondary structure và off-target binding.

Một mismatch gần 3′ end có thể ảnh hưởng extension mạnh hơn một mismatch ở vị trí khác.

Specificity là molecular recognition problem.

## 4. qPCR và quantitative thinking

**qPCR** đo fluorescence theo cycle để estimate initial template amount.

Cycle threshold thấp hơn thường gợi ý starting amount cao hơn vì sample đạt detectable fluorescence sớm hơn.

Quantification cần standard/normalization và efficiency assumption; Ct value không nên so trực tiếp vô điều kiện giữa assay khác nhau.

## 5. RT-PCR: RNA phải được chuyển thành DNA trước

RNA không được standard DNA polymerase PCR copy trực tiếp. **Reverse transcriptase** tạo complementary DNA (cDNA), sau đó PCR amplify cDNA.

Technique này dùng đo transcript hoặc detect RNA virus trong nhiều assay.

Tên “RT-PCR” đôi khi bị dùng lẫn với real-time PCR; context phải rõ.

## 6. Gel electrophoresis: molecule được tách nhờ charge và matrix

DNA mang negative charge do phosphate backbone nên chạy về positive electrode trong electric field.

Agarose gel tạo mesh; fragment nhỏ di chuyển nhanh hơn fragment lớn trong condition phù hợp.

Band position được so với DNA ladder để estimate size.

Electrophoresis biến size molecular thành spatial pattern nhìn thấy.

## 7. Restriction enzyme và recombinant DNA

Restriction enzyme nhận sequence đặc hiệu và cắt DNA. DNA ligase nối fragment.

Plasmid vector có origin replication, selectable marker và cloning site. Insert được ligate vào plasmid rồi đưa vào bacteria để propagate/expression.

Recombinant DNA là “assembly” dựa recognition sequence và cellular replication machinery.

## 8. Transformation và selection

Không phải bacterial cell nào cũng nhận plasmid. Selectable marker như antibiotic resistance trong lab giúp giữ cell mang plasmid trên medium có antibiotic tương ứng.

Đây là artificial selection ở microbial culture.

Marker lab cần biosafety và design phù hợp; concept không đồng nghĩa clinical resistance management.

## 9. DNA sequencing: từ molecule thành string data

Sanger sequencing dùng chain-terminating nucleotide để đọc sequence, phù hợp fragment nhỏ/validation.

Next-generation sequencing song song hóa hàng triệu fragment, tạo massive read dataset.

Long-read platform đọc fragment dài hơn, hữu ích cho repeat, structural variant và assembly.

Không platform nào “tốt nhất”; choice phụ thuộc read length, accuracy, throughput, cost và question.

## 10. Sequencing pipeline cơ bản

Một genomics pipeline có flow:

```text
biological sample
→ nucleic-acid extraction
→ library preparation
→ sequencing
→ raw reads
→ quality control
→ alignment/assembly
→ quantification/variant calling
→ statistics
→ biological interpretation
```

Mỗi arrow có assumption và source error. “Data từ máy” chưa phải biological conclusion.

## 11. FASTA và FASTQ

FASTA lưu sequence với header. FASTQ lưu sequence kèm quality score cho từng base.

Representation này quan trọng vì bioinformatics làm việc trên file/data structure, không trực tiếp trên tube DNA.

Biology chuyển thành computer-readable symbols.

## 12. Alignment: tìm correspondence giữa sequence

Sequence alignment có thể global hoặc local.

Dynamic programming algorithm như Needleman–Wunsch/Smith–Waterman tối ưu score theo match, mismatch và gap.

Time complexity của exact alignment làm database-scale search cần heuristic/index strategy.

Đây là nơi computer science giải biological scale problem.

## 13. BLAST: similarity search không phải proof of function

BLAST tìm local sequence similarity nhanh bằng heuristic.

High similarity có thể gợi ý homology/function, nhưng function annotation cần context, domain, phylogeny và experiment.

“BLAST hit = cùng function” là shortcut nguy hiểm.

## 14. Genome assembly như bài toán reconstruction

Nếu genome bị cắt thành reads, assembly phải reconstruct original sequence.

Short-read assembler thường dùng de Bruijn graph: k-mer là node/edge tùy formulation và overlap tạo path.

Repeat tạo ambiguity vì cùng sequence xuất hiện nhiều nơi.

Long read giúp bridge repeat nhưng cũng có error/cost trade-off.

Graph theory trực tiếp trở thành genomics tool.

## 15. Variant calling

Alignment read với reference cho phép detect SNV, indel và structural variant.

Nhưng sequencing error, mapping ambiguity, coverage thấp và sample mixture có thể tạo false call.

Variant caller dùng statistical/probabilistic model để phân biệt signal khỏi noise.

## 16. RNA-seq

RNA được chuyển thành cDNA/library rồi sequencing. Read được map/quantify để estimate transcript abundance.

Differential expression analysis so condition nhưng cần normalization, replicate và model count distribution.

P-value nhỏ không tự có biological importance; effect size và context cần đi cùng.

## 17. Single-cell sequencing

Single-cell RNA-seq gắn barcode theo cell, cho phép profile thousands cell.

Pipeline thường gồm filtering, normalization, dimensionality reduction, clustering, marker analysis và trajectory inference.

Mỗi bước transform data; cluster là computational construct cần biological validation.

## 18. Dimension reduction

Gene-expression matrix có hàng nghìn dimension. PCA tìm linear direction variance lớn; t-SNE/UMAP tạo low-dimensional visualization nonlinear.

Khoảng cách trên UMAP/t-SNE không nên đọc quá literal như physical distance; parameter và preprocessing ảnh hưởng hình.

Visualization là model, không phải raw reality.

## 19. CRISPR-Cas genome editing

Guide RNA đưa Cas nuclease tới target sequence có complementarity và PAM phù hợp. Cas tạo cut; cell repair qua NHEJ hoặc HDR có thể tạo edit.

NHEJ thường gây indel, hữu ích knockout. HDR có thể đưa template-defined change nhưng efficiency/context khác.

CRISPR không “viết DNA tùy ý không giới hạn”; delivery, off-target, repair biology và cell type là constraint.

## 20. Base editing và prime editing

Base editor kết hợp targeting CRISPR với deaminase để đổi base nhất định không cần double-strand break cổ điển trong nhiều design.

Prime editing dùng reverse-transcriptase-based mechanism và pegRNA để viết edit linh hoạt hơn ở một số context.

Mỗi tool có edit window, byproduct và delivery constraint riêng.

## 21. Functional genomics

CRISPR screen, RNAi hoặc overexpression screen perturb thousands gene rồi đo phenotype.

Observation genomics tìm association; functional genomics cố tạo causal evidence bằng perturbation.

Kết hợp screening + sequencing biến cell population thành high-throughput experiment.

## 22. Synthetic biology

Synthetic biology cố thiết kế genetic circuit, metabolic pathway hoặc cell behavior với engineering mindset.

Promoter, ribosome-binding site, regulator và sensor có thể xem như module, nhưng biological component không hoàn toàn orthogonal như electronic part; context và burden gây interaction.

Engineering life cần hiểu noise, evolution và host physiology.

## 23. Genetic circuit

Một toggle switch có thể dùng two repressors ức chế nhau để tạo bistability. Oscillator dùng delayed negative feedback.

Circuit behavior xuất hiện từ network dynamics chứ không chỉ component list.

Đây là systems biology theo hướng design.

## 24. Metabolic engineering

Ta có thể redirect flux để microbe tạo drug, enzyme, biofuel hoặc chemical.

Nhưng tăng một enzyme chưa chắc tăng product nếu pathway bottleneck chuyển sang step khác hoặc cofactor thiếu.

Flux balance và systems-level model giúp identify bottleneck.

## 25. Systems biology

Systems biology hỏi: network response theo time thế nào khi component tương tác?

Model có thể dùng ordinary differential equation:

\[
\frac{dx_i}{dt}=f_i(x_1,x_2,...,u)
\]

Mỗi \(x_i\) là concentration/activity; function mô tả production/degradation/interactions.

Parameter fitting và sensitivity analysis giúp tìm control point.

## 26. Network biology

Graph representation:

- node: gene/protein/metabolite/species;
- edge: regulation, binding, reaction, feeding.

Degree, centrality, motif và community structure có thể gợi ý organization.

Nhưng network database có bias; high-degree node đôi khi vì được nghiên cứu nhiều.

## 27. Machine learning trong Biology

ML có thể classify cell type, predict protein structure/property, interpret microscopy, prioritize variant hoặc model sequence.

Nhưng model performance phụ thuộc training distribution. Dataset leakage, class imbalance và population bias có thể làm metric đẹp nhưng generalization kém.

Biological ML cần external validation và causal caution.

## 28. Supervised và unsupervised learning

Supervised learning cần label; unsupervised tìm structure không có label rõ.

Clustering gene expression là unsupervised-ish discovery; disease classifier là supervised.

Không nên gọi mọi statistics trên biological data là “AI”. Tool phải phù hợp question.

## 29. Protein structure prediction

Protein sequence chứa constraint shape nhưng folding chịu physics/context. Modern deep-learning model có thể predict structure rất tốt ở nhiều case.

Tuy nhiên structure prediction không tự cho function, dynamics, interaction hay effect mutation đầy đủ.

Experimental structural biology vẫn quan trọng.

## 30. Database và reproducibility

Bioinformatics workflow dùng reference genome, annotation version, software version và parameter. Kết quả có thể thay khi reference/tool đổi.

Reproducible analysis cần version control, environment/container, metadata và workflow documentation.

Software engineering trở thành một phần scientific rigor.

## 31. Causality: omics correlation không đủ

Nếu gene X expression cao ở disease, có thể X gây disease, disease làm X tăng hoặc third factor làm cả hai.

Perturbation experiment, temporal data, genetic instrument hoặc causal model giúp phân biệt.

High-dimensional data làm false correlation dễ xuất hiện; multiple testing và replication bắt buộc.

## 32. Ethics và governance

Genome data có privacy implication; gene editing germline có intergenerational consequence; synthetic organism có biosafety concern.

Technical ability không tự trả lời “nên làm hay không”. Ethics, regulation, informed consent và equity phải đi cùng technology.

## 33. Case study: từ patient sample tới variant interpretation

Blood/tissue → DNA extraction → sequencing → alignment → variant calling → annotation → population frequency → predicted consequence → clinical correlation/functional evidence.

Mỗi bước giảm uncertainty nhưng không xóa hoàn toàn.

Một report tốt phải phân biệt observation, inference và confidence.

## 34. Case study: engineered insulin

Human insulin gene/cDNA được đưa vào microbial expression system; cell culture sản xuất recombinant protein; purification/quality control tạo therapeutic product.

Technology này kết nối gene expression, plasmid, fermentation, protein folding và industrial process.

## 35. Common misconceptions

“PCR cho biết có gene hoạt động” sai; standard PCR chỉ detect/amplify DNA target, activity cần expression assay.

“Sequencing đọc được genome hoàn hảo” sai; coverage, repeat và error tạo uncertainty.

“CRISPR cắt đúng 100%” sai; targeting/off-target/delivery/repair có limitation.

“More omics data = more understanding” sai nếu question/model yếu.

“AI tìm được correlation thì đó là mechanism” sai.

## 36. Bridge sang connections: Biology đang dùng lại cùng một số idea toán học

Tới đây ta đã thấy exponential amplification, logarithm, probability, graph, dynamic system, optimization và statistics xuất hiện liên tục.

[[../90_connections/00_biology_math_computation_and_scale]] sẽ gom các motif này lại để cho thấy Sinh học, Toán và Computer Science không phải ba domain đứng cạnh nhau mà là ba cách mô tả cùng system.

> **Mental model cuối chapter:** biotechnology là “biology made operational”. Ta không thể edit hay model một system nếu không hiểu mechanism; cũng không thể hiểu dữ liệu hiện đại nếu thiếu probability, algorithms và systems thinking. Công nghệ mạnh nhất xuất hiện khi molecular insight, quantitative model và engineering discipline gặp nhau.