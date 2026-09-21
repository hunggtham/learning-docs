# Công nghệ sinh học, Tin sinh học và Systems Biology — Biotechnology, Bioinformatics and Systems Biology (생명공학, 생물정보학과 시스템생물학)

Toàn bộ các chapter trước xây một đồ thị kiến thức (knowledge graph) từ molecule tới ecosystem. Biotechnology bắt đầu khi ta hỏi một câu mới: **nếu đã hiểu mechanism, ta có thể đo, khuếch đại, chỉnh sửa hoặc thiết kế nó như thế nào?** Bioinformatics xuất hiện khi dữ liệu quá lớn để xử lý thủ công; sinh học hệ thống (systems biology) xuất hiện khi danh sách component không còn đủ để giải thích behavior của network.

> **Mô hình tư duy (mental model):** công nghệ sinh học (biotechnology) biến biological mechanism thành tool; sinh tin học (bioinformatics) biến biological data thành representation có thể tính toán; sinh học hệ thống biến list component thành model về interaction và động lực học (dynamics).

## 1. Biotechnology không bắt đầu từ CRISPR

Con người đã dùng lên men (fermentation), selective breeding và food biotechnology từ lâu trước sinh học phân tử (molecular biology).

Modern biotechnology khác ở mức precision: ta có thể isolate DNA, amplify sequence, trình tự (sequence) hệ gen (genome), edit locus và measure thousands gene cùng lúc.

Nhưng mỗi tool vẫn dựa mechanism tự nhiên: PCR dùng DNA polymerase; restriction enzyme đến từ bacterial defense; CRISPR đến từ microbial immunity.

## 2. PCR: làm một đoạn DNA trở thành hàng triệu copy

**Polymerase chain reaction, PCR (중합효소연쇄반응)** cần template DNA, two primers, thermostable DNA polymerase, nucleotide và buffer.

Một cycle gồm:

1. denaturation: tách Mạch DNA (DNA strand) bằng heat;
2. annealing: primer bind sequence complement;
3. extension: polymerase kéo dài.

Nếu efficiency lý tưởng, amount target tăng gần:

\[
N_n=N_0 2^n
\]

sau \(n\) cycle. Real efficiency thấp hơn 100% và reaction cuối sẽ plateau.

## 3. Primer tạo độ đặc hiệu (specificity)

PCR không “copy toàn genome”. Primer xác định boundary region được khuếch đại.

Primer design phải cân nhắc melting temperature, GC content, secondary structure và off-target binding.

Một mismatch gần 3′ end có thể ảnh hưởng extension mạnh hơn một mismatch ở vị trí khác.

Specificity là nhận dạng phân tử (molecular recognition) vấn đề (problem).

## 4. qPCR và quantitative thinking

**qPCR** đo huỳnh quang (fluorescence) theo cycle để estimate initial template amount.

Cycle threshold thấp hơn thường gợi ý starting amount cao hơn vì mẫu (sample) đạt detectable fluorescence sớm hơn.

Quantification cần standard/normalization và efficiency assumption; Ct value không nên so trực tiếp vô điều kiện giữa assay khác nhau.

## 5. RT-PCR: RNA phải được chuyển thành DNA trước

RNA không được standard DNA polymerase PCR copy trực tiếp. **Reverse transcriptase** tạo complementary DNA (cDNA), sau đó PCR amplify cDNA.

Technique này dùng đo transcript hoặc detect RNA virus trong nhiều assay.

Tên “RT-PCR” đôi khi bị dùng lẫn với real-time PCR; context phải rõ.

## 6. Gel electrophoresis: phân tử (molecule) được tách nhờ charge và matrix

DNA mang negative charge do phosphate backbone nên chạy về positive electrode trong điện trường (electric field).

Agarose gel tạo mesh; fragment nhỏ di chuyển nhanh hơn fragment lớn trong condition phù hợp.

Band position được so với DNA ladder để estimate size.

Electrophoresis biến size molecular thành spatial pattern nhìn thấy.

## 7. Restriction enzyme và recombinant DNA

Restriction enzyme nhận sequence đặc hiệu và cắt DNA. DNA ligase nối fragment.

Plasmid vector có origin replication, selectable marker và cloning site. Insert được ligate vào plasmid rồi đưa vào bacteria để propagate/expression.

Recombinant DNA là “assembly” dựa recognition sequence và cellular bộ máy sao chép (replication machinery).

## 8. Transformation và chọn lọc (selection)

Không phải bacterial cell nào cũng nhận plasmid. Selectable marker như kháng kháng sinh (antibiotic resistance) trong lab giúp giữ cell mang plasmid trên medium có antibiotic tương ứng.

Đây là artificial selection ở microbial culture.

Marker lab cần biosafety và design phù hợp; concept không đồng nghĩa clinical resistance management.

## 9. DNA sequencing: từ molecule thành string data

Sanger sequencing dùng chain-terminating nucleotide để đọc sequence, phù hợp fragment nhỏ/validation.

Next-generation sequencing song song hóa hàng triệu fragment, tạo massive read dataset.

Long-read platform đọc fragment dài hơn, hữu ích cho repeat, structural variant và assembly.

Không platform nào “tốt nhất”; choice phụ thuộc read length, độ chính xác (accuracy), throughput, cost và câu hỏi (question).

## 10. Sequencing pipeline cơ bản

Một genomics pipeline có dòng chảy (flow):

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

Mỗi arrow có assumption và source error. “Data từ máy” chưa phải kết luận sinh học (biological conclusion).

## 11. FASTA và FASTQ

FASTA lưu sequence với header. FASTQ lưu sequence kèm điểm chất lượng (quality score) cho từng base.

Representation này quan trọng vì bioinformatics làm việc trên file/cấu trúc dữ liệu (data structure), không trực tiếp trên tube DNA.

Biology chuyển thành computer-readable symbols.

## 12. Căn chỉnh (alignment): tìm correspondence giữa sequence

Căn chỉnh trình tự (sequence alignment) có thể global hoặc local.

Dynamic programming algorithm như Needleman–Wunsch/Smith–Waterman tối ưu score theo match, mismatch và gap.

Time complexity của exact alignment làm database-scale search cần heuristic/index strategy.

Đây là nơi computer science giải biological scale problem.

## 13. BLAST: similarity search không phải proof of function

BLAST tìm local sequence similarity nhanh bằng heuristic.

High similarity có thể gợi ý homology/chức năng (function), nhưng function annotation cần context, domain, phylogeny và thí nghiệm (experiment).

“BLAST hit = cùng function” là shortcut nguy hiểm.

## 14. Genome assembly như bài toán reconstruction

Nếu genome bị cắt thành reads, assembly phải reconstruct original sequence.

Short-read assembler thường dùng de Bruijn graph: k-mer là nút (node)/edge tùy formulation và overlap tạo path.

Repeat tạo ambiguity vì cùng sequence xuất hiện nhiều nơi.

Long read giúp bridge repeat nhưng cũng có error/cost trade-off.

Lý thuyết đồ thị (graph theory) trực tiếp trở thành genomics tool.

## 15. Gọi biến thể (variant calling)

Alignment read với reference cho phép detect SNV, indel và structural variant.

Nhưng sequencing error, mapping ambiguity, coverage thấp và sample mixture có thể tạo false call.

Variant caller dùng statistical/probabilistic model để phân biệt signal khỏi noise.

## 16. RNA-seq

RNA được chuyển thành cDNA/library rồi sequencing. Read được map/quantify để estimate mức độ phong phú của bản phiên mã (transcript abundance).

Biểu hiện khác biệt (differential expression) analysis so condition nhưng cần normalization, replicate và model count distribution.

P-value nhỏ không tự có biological importance; effect size và context cần đi cùng.

## 17. Single-tế bào (cell) sequencing

Single-cell RNA-seq gắn barcode theo tế bào, cho phép profile thousands cell.

Pipeline thường gồm filtering, normalization, giảm chiều dữ liệu (dimensionality reduction), clustering, marker analysis và trajectory inference.

Mỗi bước transform data; cluster là computational construct cần biological validation.

## 18. Dimension reduction

Gen (gene)-expression matrix có hàng nghìn dimension. PCA tìm linear direction variance lớn; t-SNE/UMAP tạo low-dimensional visualization nonlinear.

Khoảng cách trên UMAP/t-SNE không nên đọc quá literal như physical distance; parameter và tiền xử lý (preprocessing) ảnh hưởng hình.

Visualization là mô hình (model), không phải raw reality.

## 19. CRISPR-Cas genome editing

Guide RNA đưa Cas nuclease tới target sequence có complementarity và PAM phù hợp. Cas tạo cut; cell repair qua NHEJ hoặc HDR có thể tạo edit.

NHEJ thường gây indel, hữu ích knockout. HDR có thể đưa template-defined change nhưng efficiency/context khác.

CRISPR không “viết DNA tùy ý không giới hạn”; delivery, off-target, repair biology và loại tế bào (cell type) là ràng buộc (constraint).

## 20. Base editing và prime editing

Base editor kết hợp targeting CRISPR với deaminase để đổi base nhất định không cần đứt gãy hai mạch (double-strand break) cổ điển trong nhiều design.

Prime editing dùng reverse-transcriptase-based mechanism và pegRNA để viết edit linh hoạt hơn ở một số bối cảnh (context).

Mỗi tool có edit window, byproduct và delivery constraint riêng.

## 21. Functional genomics

CRISPR screen, RNAi hoặc overexpression screen perturb thousands gene rồi đo kiểu hình (phenotype).

Observation genomics tìm association; functional genomics cố tạo causal evidence bằng perturbation.

Kết hợp screening + giải trình tự (sequencing) biến cell population thành high-throughput experiment.

## 22. Sinh học tổng hợp (synthetic biology)

Sinh học tổng hợp cố thiết kế mạch di truyền (genetic circuit), con đường chuyển hóa (metabolic pathway) hoặc cell behavior với engineering mindset.

Promoter, ribosome-binding site, regulator và sensor có thể xem như module, nhưng biological component không hoàn toàn orthogonal như electronic part; context và burden gây interaction.

Engineering life cần hiểu noise, evolution và host physiology.

## 23. Mạch di truyền

Một toggle switch có thể dùng two repressors ức chế nhau để tạo tính lưỡng ổn (bistability). Oscillator dùng delayed phản hồi âm (negative feedback).

Circuit behavior xuất hiện từ mạng lưới (network) dynamics chứ không chỉ component list.

Đây là sinh học hệ thống theo hướng design.

## 24. Kỹ thuật chuyển hóa (metabolic engineering)

Ta có thể redirect flux để microbe tạo drug, enzym (enzyme), biofuel hoặc chemical.

Nhưng tăng một enzyme chưa chắc tăng product nếu pathway bottleneck chuyển sang step khác hoặc cofactor thiếu.

Flux balance và systems-level model giúp identify bottleneck.

## 25. Sinh học hệ thống

Sinh học hệ thống hỏi: mạng lưới đáp ứng (response) theo time thế nào khi component tương tác?

Model có thể dùng ordinary differential equation:

\[
\frac{dx_i}{dt}=f_i(x_1,x_2,...,u)
\]

Mỗi \(x_i\) là concentration/hoạt động (activity); function mô tả sự tạo ra (production)/phân giải (degradation)/interactions.

Parameter fitting và phân tích độ nhạy (sensitivity analysis) giúp tìm control point.

## 26. Mạng lưới sinh học (biology)

Graph representation:

- nút: gen/protein (protein)/metabolite/loài (species);
- edge: điều hòa (regulation), liên kết (binding), reaction, feeding.

Degree, centrality, motif và quần xã (community) structure có thể gợi ý organization.

Nhưng network database có sai lệch (bias); high-degree node đôi khi vì được nghiên cứu nhiều.

## 27. Học máy (machine learning) trong Sinh học

ML có thể classify loại tế bào, predict cấu trúc protein (protein structure)/đặc tính (property), interpret microscopy, prioritize variant hoặc model trình tự.

Nhưng model performance phụ thuộc training distribution. Dataset leakage, class imbalance và quần thể (population) bias có thể làm metric đẹp nhưng generalization kém.

Biological ML cần external validation và causal caution.

## 28. Supervised và unsupervised learning

Supervised learning cần label; unsupervised tìm structure không có label rõ.

Clustering biểu hiện gen (gene expression) là unsupervised-ish discovery; disease classifier là supervised.

Không nên gọi mọi statistics trên biological data là “AI”. Tool phải phù hợp question.

## 29. Cấu trúc protein prediction

Protein sequence chứa constraint shape nhưng folding chịu physics/bối cảnh. Modern deep-learning model có thể predict structure rất tốt ở nhiều case.

Tuy nhiên structure prediction không tự cho chức năng, động lực học, interaction hay effect mutation đầy đủ.

Experimental structural biology vẫn quan trọng.

## 30. Database và reproducibility

Bioinformatics workflow dùng hệ gen tham chiếu (reference genome), annotation version, software version và tham số (parameter). Kết quả có thể thay khi reference/tool đổi.

Reproducible analysis cần version control, môi trường (environment)/container, metadata và workflow documentation.

Software engineering trở thành một phần scientific rigor.

## 31. Causality: omics correlation không đủ

Nếu gene X expression cao ở bệnh (disease), có thể X gây disease, disease làm X tăng hoặc third factor làm cả hai.

Perturbation experiment, temporal data, genetic instrument hoặc causal model giúp phân biệt.

High-dimensional data làm false correlation dễ xuất hiện; kiểm định nhiều lần (multiple testing) và replication bắt buộc.

## 32. Ethics và governance

Genome data có privacy implication; gene editing germline có intergenerational consequence; synthetic organism có biosafety concern.

Technical ability không tự trả lời “nên làm hay không”. Ethics, điều hòa, informed consent và equity phải đi cùng technology.

## 33. Tình huống phân tích (case study): từ patient sample tới variant diễn giải (interpretation)

Blood/mô (tissue) → DNA extraction → giải trình tự → căn chỉnh → gọi biến thể → annotation → quần thể tần số (frequency) → predicted consequence → clinical correlation/functional evidence.

Mỗi bước giảm uncertainty nhưng không xóa hoàn toàn.

Một report tốt phải phân biệt observation, inference và độ tin cậy (confidence).

## 34. Tình huống phân tích: engineered insulin

Human insulin gene/cDNA được đưa vào microbial expression system; cell culture sản xuất recombinant protein; purification/kiểm soát chất lượng (quality control) tạo therapeutic product.

Technology này kết nối biểu hiện gen, plasmid, lên men, sự gấp cuộn protein (protein folding) và industrial process.

## 35. Các hiểu lầm phổ biến (common misconceptions)

“PCR cho biết có gene hoạt động” sai; standard PCR chỉ detect/amplify DNA target, activity cần expression assay.

“Giải trình tự đọc được genome hoàn hảo” sai; coverage, repeat và error tạo độ bất định (uncertainty).

“CRISPR cắt đúng 100%” sai; targeting/off-target/delivery/repair có giới hạn (limitation).

“More omics data = more understanding” sai nếu question/model yếu.

“AI tìm được correlation thì đó là cơ chế (mechanism)” sai.

<!-- depth-audit-2026:dbtl-causal-engineering -->
## Biotechnology hiện đại là vòng Design–Build–Test–Learn, không phải danh sách tool

Sinh học kỹ thuật (engineering biology) thường chạy theo vòng **thiết kế → xây dựng → kiểm thử → học (Design–Build–Test–Learn, DBTL)**. Design chọn mechanism và target; Build tạo construct/cell line; Test đo phenotype; Learn cập nhật model rồi quay lại design. Nếu measurement không phản ánh đúng mechanism, vòng lặp có thể tối ưu nhầm objective dù kỹ thuật thực hiện hoàn hảo.

CRISPR minh họa rõ structure → mechanism → failure. Guide RNA xác định recognition; Cas tạo hoặc xúc tác biến đổi tại target; DNA repair quyết định outcome cuối. Failure có thể đến từ off-target, on-target rearrangement, delivery không đều hoặc mosaicism. Vì vậy “edit thành công” phải được định nghĩa bằng genotype, expression, phenotype và unintended effect chứ không chỉ thấy một band PCR đúng kích thước.

Perturbation mạnh hơn observation cho causal inference nhưng vẫn cần control. Knockout có thể gây compensation; overexpression có thể tạo mức protein phi sinh lý; cell line khác organism. Biotechnology tốt luôn hỏi intervention đang thay node nào, network có feedback gì và model organism bỏ qua layer nào.

## 36. Bridge sang connections: Sinh học đang dùng lại cùng một số idea toán học

Tới đây ta đã thấy exponential amplification, logarithm, xác suất (probability), graph, dynamic system, optimization và statistics xuất hiện liên tục.

[Biology × Mathematics × Computation × Scale](../90_connections/00_biology_math_computation_and_scale.md) sẽ gom các motif này lại để cho thấy Sinh học, Toán và Computer Science không phải ba domain đứng cạnh nhau mà là ba cách mô tả cùng system.

> **Mô hình tư duy cuối chapter:** biotechnology là “biology made operational”. Ta không thể edit hay model một system nếu không hiểu mechanism; cũng không thể hiểu dữ liệu hiện đại nếu thiếu probability, algorithms và tư duy hệ thống (systems thinking). Công nghệ mạnh nhất xuất hiện khi molecular insight, quantitative model và engineering discipline gặp nhau.

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← Quần xã sinh học, biến đổi toàn cầu và sinh quyển](../05_ecology/02_biomes_global_change_and_biosphere.md) · [Mục lục Biology](../README.md) · [Phương pháp thực nghiệm và đo lường trong Sinh học →](01_experimental_methods_and_measurement.md)
