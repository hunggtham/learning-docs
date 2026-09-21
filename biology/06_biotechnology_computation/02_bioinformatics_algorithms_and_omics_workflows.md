# Bioinformatics, thuật toán và Omics Workflow — Bioinformatics Algorithms and Omics Workflows (생물정보학, 알고리즘과 오믹스 워크플로)

Khi Biology tạo ra hàng triệu sequence, expression value hoặc image feature, data không còn có thể được hiểu bằng cách đọc từng dòng. **Sinh tin học (bioinformatics / 생물정보학)** xuất hiện ở đúng điểm này: dùng thuật toán, thống kê và mô hình dữ liệu (data model) để biến measurement thành suy luận sinh học (biological inference).

Chapter này không dạy một tool cụ thể. Mục tiêu là xây mô hình tư duy (mental model) từ tín hiệu thô (raw signal) → tệp (file) → QC → representation → thuật toán (algorithm) → mô hình thống kê (statistical model) → diễn giải (interpretation). Khi hiểu flow này, FASTQ, BAM, VCF, BLAST, RNA-seq hay single-cell không còn là những tên riêng rời rạc mà là các stage trong một reasoning pipeline.

> **Mô hình tư duy:** bioinformatics không “khám phá truth trực tiếp từ dữ liệu (data)”. Nó liên tục nén và biến đổi data. Mỗi transformation thêm assumption; vì vậy một conclusion tốt phải trace được ngược về raw evidence.

## 1. Từ molecule sang digital object

Sequencer quan sát biochemical event rồi base caller chuyển signal thành sequence text và điểm chất lượng (quality score). Từ thời điểm đó, molecule trở thành digital record.

Một raw read không biết mình thuộc gene nào hay có mutation gì. Nó chỉ là trình tự (sequence) + siêu dữ liệu (metadata) + chất lượng (quality). Ý nghĩa sinh học (biological meaning) xuất hiện dần qua suy luận ở bước sau (downstream inference).

Các format phổ biến phản ánh stage đó. FASTQ giữ read và chất lượng. FASTA giữ trình tự. SAM/BAM/CRAM mô tả căn chỉnh (alignment). VCF mô tả variant candidate. GTF/GFF mô tả genomic feature.

Format không chỉ là syntax IT; nó encode **state của reasoning**.

## 2. Metadata là một phần của data

Sequence không đủ. Sample thuộc tissue nào, treatment gì, batch nào, time point nào, patient nào, replicate nào — tất cả là siêu dữ liệu.

Nếu metadata sai hoặc ambiguous, analysis có thể technically hoàn hảo nhưng kết luận sinh học (biological conclusion) vô nghĩa.

Điều này làm database thiết kế (design), quy ước đặt tên (naming convention) và từ vựng được kiểm soát (controlled vocabulary) trở thành component của chất lượng khoa học (scientific quality).

## 3. QC phải diễn ra trước inference

Adapter contamination, low-quality tail, unusual GC content, overrepresented sequence hoặc duplicated read có thể báo vấn đề kỹ thuật (technical issue).

Nhưng QC metric không có ngưỡng phổ quát (universal threshold). High duplication có thể bình thường trong targeted amplicon sequencing nhưng suspicious trong whole-genome library.

QC vì vậy là **đánh giá theo bối cảnh (contextual diagnosis)**, không phải đạt/không đạt (pass/fail) máy móc.

## 4. Phred score là probabilistic metadata

Phred quality:

\[
Q=-10\log_{10}P(error)
\]

Q30 tương ứng estimated xác suất lỗi (error probability) khoảng 0.001. Log scale giúp biểu diễn uncertainty nhỏ gọn.

Nhưng điểm chất lượng vẫn là model estimate từ machine behavior. “Q30” không nghĩa base chắc chắn đúng; nó nghĩa instrument/mô hình (model) đánh giá độ tin cậy (confidence) ở mức tương ứng.

## 5. Căn chỉnh trình tự (sequence alignment) biến biological similarity thành bài toán tối ưu (optimization problem)

Hai sequence có thể khác do substitution, insertion hoặc deletion. Alignment chèn gap để tìm correspondence.

Ta định nghĩa score cho match, mismatch và gap. Sau đó algorithm tìm alignment tối ưu theo score đó.

Căn chỉnh toàn cục (global alignment) thích hợp khi hai sequence tương đồng gần toàn chiều dài; căn chỉnh cục bộ (local alignment) tìm region giống nhau tốt nhất.

Biological question “hai sequence có quan hệ không?” trở thành computational problem “alignment nào có score cao dưới model đã chọn?”.

## 6. Dynamic programming: exact solution có cost

Needleman–Wunsch và Smith–Waterman dùng dynamic programming. Với sequence length \(m\) và \(n\), time/memory thường tăng theo tích của chiều dài trong implementation cơ bản.

Khi database có millions sequence, chạy exact algorithm với mọi pair quá đắt. Đây là nơi heuristic xuất hiện.

Computer Science không chỉ giúp chạy nhanh hơn; nó quyết định loại approximation nào ta chấp nhận để scale biological question.

## 7. BLAST: heuristic đánh đổi completeness lấy speed

BLAST tìm short matching word rồi extend candidate region thay vì exhaustively thử mọi alignment.

Kết quả nhanh và thường biologically useful, nhưng “BLAST hit” không tự chứng minh function. Similarity có thể do shared domain, repetitive region hoặc common ancestry xa.

Chức năng (function) inference nên xem coverage, identity, conserved domain, synteny, phylogeny và ideally experiment.

## 8. E-value và significance của sequence match

BLAST E-value gần biểu diễn số match có score tương tự hoặc tốt hơn kỳ vọng xuất hiện ngẫu nhiên trong cơ sở dữ liệu (database) theo model nhất định.

Database càng lớn, chance match càng nhiều. Vì vậy cùng score có significance khác khi search database khác size.

Đây là lesson statistical quan trọng: evidence strength phụ thuộc search space.

## 9. Hệ gen tham chiếu (reference genome) là coordinate system, không phải “genome chuẩn tuyệt đối”

Reference giúp read có coordinate chung. Nhưng reference là representation cụ thể, không chứa mọi haplotype hoặc structural variant trong quần thể (population).

Read từ region divergent hoặc repeat có thể map khó. **Sai lệch do tham chiếu (reference bias)** xảy ra khi pipeline ưu tiên allele giống reference.

Hệ gen toàn quần thể (pangenome) representation cố mô hình hóa nhiều path/haplotype hơn, thường bằng graph-like structure.

## 10. Chất lượng ánh xạ (mapping quality) là uncertainty về vị trí

Short read ở repeat region có thể align nhiều nơi. Mapper phải chọn best location, đánh multi-mapping hoặc bỏ read.

Chất lượng ánh xạ phản ánh confidence placement. Vì vậy statement “read này thuộc gene X” cũng là inference có độ bất định (uncertainty).

Nếu downstream variant caller bỏ qua uncertainty mapping, dương tính giả (false positive) có thể tăng.

## 11. Coverage là redundancy, nhưng coverage thực không đều

Approximation:

\[
Coverage\approx\frac{N\times L}{G}
\]

với \(N\) số read, \(L\) read length và \(G\) genome size.

Coverage cao tạo redundancy giúp phân biệt sequencing error khỏi variant thật. Nhưng GC bias, capture efficiency và mappability làm depth không đều.

“30× hệ gen (genome)” là average, không nghĩa mọi base đều được đọc 30 lần.

## 12. Gọi biến thể (variant calling) là probabilistic decision

Giả sử tại một locus có 18 read A và 12 read G. Có thể sample heterozygous, nhưng cũng có thể mapping bias, contamination hoặc sequencing error.

Variant caller so likelihood của genotype hypothesis dựa trên base quality, chất lượng ánh xạ, allele balance và model ploidy.

VCF vì vậy không phải list truth. Nó là collection of candidate variant + bằng chứng (evidence) + filter.

## 13. Germline và somatic workflow dùng biological prior khác nhau

Germline diploid variant thường có allele fraction gần 0, 0.5 hoặc 1 trong ideal sample.

Tumor sample có purity <100%, subclone, copy-number alteration và normal-cell admixture. Somatic variant fraction vì vậy có thể thấp hoặc lệch.

Cùng raw read nhưng model biological khác làm inference khác.

## 14. Copy-number và structural variant cần evidence khác SNV

Large deletion, duplication, inversion hoặc translocation không thể luôn detect bằng single-base mismatch.

Ta cần depth change, discordant paired-end orientation, split read hoặc long-read spanning event.

Điều này cho thấy algorithm phụ thuộc **signature vật lý mà experiment tạo ra**.

## 15. Genome assembly: reconstruction không có reference

Assembly ghép read thành contig/scaffold. Với short read, **de Bruijn graph** thường biểu diễn k-mer overlap.

Repeat tạo branch, sequencing error tạo spur, heterozygosity tạo alternative path. Long read span repeat tốt hơn nhưng có error profile riêng.

Assembly là graph reconstruction dưới incomplete/noisy data.

## 16. k-mer size là trade-off

k nhỏ tăng overlap nhưng làm repeat khó phân biệt. k lớn tăng uniqueness nhưng yêu cầu read dài và đủ coverage.

Không có k “tốt nhất” universal. Parameter phản ánh trade-off giữa connectivity và độ đặc hiệu (specificity).

Đây là example algorithm parameter có biological consequence.

## 17. Annotation: sequence không tự nói “đây là gen (gene)”

Gene annotation kết hợp open reading frame, splice signal, transcript evidence, protein homology và comparative genomics.

Annotation database có version và độ bất định. Một gene model có thể được sửa khi RNA-seq hoặc long-read transcript evidence mới xuất hiện.

Do đó downstream analysis phải ghi hệ gen tham chiếu **và annotation version**.

## 18. RNA-seq: count không phải expression tuyệt đối trực tiếp

RNA-seq workflow thường gồm QC → căn chỉnh/pseudoalignment → counting → normalization → biểu hiện khác biệt (differential expression).

Raw count phụ thuộc library size, mức độ phong phú của bản phiên mã (transcript abundance) và technical bias. Transcript length ảnh hưởng probability read xuất hiện trong within-sample comparison.

Normalization cố tạo comparable scale giữa sample nhưng luôn có giả định (assumption).

## 19. Normalization có thể che global shift

Nhiều method giả định phần lớn gene không đổi extreme hoặc composition không đổi quá mạnh.

Nếu treatment làm global RNA production tăng gần toàn transcriptome, relative normalization có thể làm change trông nhỏ đi.

Đây là reason spike-in control đôi khi hữu ích: external reference giúp nhận biết global scaling.

## 20. Biểu hiện khác biệt và kiểm định nhiều lần (multiple testing)

Nếu test 20,000 gene với p<0.05 mà không correction, dương tính giả xuất hiện nhiều chỉ do chance.

False Discovery Rate giúp kiểm soát expected false discovery proportion trong framework nhất định.

Nhưng adjusted p-value nhỏ vẫn cần effect size. Gene thay 1.03× với huge n có thể significant mà biological relevance thấp.

## 21. PCA: nhìn structure high-dimensional bằng vài trục

Mỗi sample expression là vector hàng nghìn chiều. PCA tìm orthogonal direction capture variance lớn.

PCA plot giúp detect batch, outlier hoặc major biological separation. Nhưng principal component chỉ tối đa variance; nó không tự mang meaning biological.

Loading và metadata cần để interpret axis.

## 22. Clustering là hypothesis generator, không phải truth generator

Clustering nhóm cell/mẫu (sample) theo similarity. Kết quả phụ thuộc feature selection, normalization, distance metric và độ phân giải (resolution).

Một cluster đẹp không tự chứng minh “loại tế bào (cell type) mới”. Cần marker, developmental context và ideally validation.

Algorithm tạo partition; biologist gắn interpretation.

## 23. Single-cell RNA-seq: từ average sang distribution

Bulk RNA-seq trộn nhiều cell. Single-cell phân giải heterogeneity và rare population.

Nhưng capture efficiency thấp, count sparse và nhiều zero. Zero có thể nghĩa gene off hoặc transcript bị missed.

Vì vậy single-cell analysis cần model count noise và tránh đọc heatmap như measurement hoàn hảo.

## 24. UMAP/t-SNE: visualization không bảo toàn mọi khoảng cách

Giảm chiều dữ liệu (dimensionality reduction) nén hàng nghìn dimension xuống 2D/3D. Local neighborhood có thể hữu ích, nhưng global distance và cluster gap trên plot không nên overinterpret.

Một plot đẹp là representation của algorithm, không phải microscope image của “tế bào (cell)-state space”.

## 25. Pseudotime: reconstruct dynamics từ snapshot

Developmental single-cell dataset thường chứa nhiều cell ở state khác nhau. Algorithm có thể order cell thành **pseudotime** dựa trên manifold/graph.

Pseudotime không phải actual chronological time. Nó là inferred progression dưới assumption rằng sampled states lie along transition path.

Validation bằng lineage tracing hoặc time-course giúp mạnh hơn.

## 26. Epigenomics: accessibility và binding không đồng nghĩa causality

ATAC-seq đo khả năng tiếp cận nhiễm sắc chất (chromatin accessibility). ChIP-seq đo enrichment DNA fragment associated với protein/histone mark. Methyl hóa DNA (DNA methylation) phép thử (assay) đo methylation state.

Kết hợp epigenomics với RNA-seq giúp xây regulatory hypothesis. Nhưng open enhancer correlated với gene up không tự chứng minh enhancer gây expression.

CRISPR perturb enhancer hoặc reporter assay có thể kiểm tra causal role.

## 27. Proteomics và metabolomics đưa ta gần phenotype hơn nhưng tăng ambiguity khác

Mass spectrometry đo mass-to-charge pattern rồi infer peptide/protein (protein)/metabolite identity.

Mức độ phong phú của protein (protein abundance) chịu translation, phân giải (degradation), modification. Metabolite phản ánh network state gần reaction flux nhưng annotation có thể khó.

Không layer omics nào “cao hơn” tuyệt đối. Mỗi layer có ý nghĩa sinh học và phép đo (measurement) bias riêng.

## 28. Multi-omics integration: nhiều layer không tự động tạo hiểu biết

Kết hợp genome, epigenome, transcriptome, proteome và metabolome tăng context nhưng dimension và missing data cũng tăng.

Một useful strategy là đặt causal question rõ: variant có đổi chromatin không, chromatin có đổi expression không, expression có đổi protein/metabolite không?

Integration tốt đi theo biological mechanism, không chỉ concatenate matrix.

## 29. Mạng lưới (network) sinh học (biology): graph hữu ích nhưng edge cần evidence type

Node có thể là gen/protein/metabolite; edge là interaction/điều hòa (regulation).

Degree, centrality và quần xã (community) cấu trúc (structure) giúp tìm organization. Nhưng database interaction biased về gene nổi tiếng; co-expression edge không giống physical-binding edge.

Mọi network visualization nên hỏi: **edge nghĩa gì và evidence từ đâu?**

## 30. Học máy (machine learning): prediction khác explanation

ML có thể classify image, predict phenotype hoặc infer protein đặc tính (property). Nhưng high test accuracy không tự chứng minh model học biology đúng.

Model có thể học batch, hospital, scanner hoặc ancestry confounder.

Prediction trả lời “có dự đoán được không?”. Causality trả lời “thay X có làm Y đổi không?”. Hai câu hỏi khác nhau.

## 31. Train/validation/test và rò rỉ dữ liệu (data leakage)

Training set fit model. Validation set tune hyperparameter. Test set estimate performance cuối trên unseen data.

**Rò rỉ dữ liệu** xảy ra khi information test lọt vào tập luyện (training). Trong sinh học, common leak là sample từ cùng patient hoặc same clone bị split ngẫu nhiên vào cả train và test.

Mô hình khi đó có thể memorize individual-specific signal thay vì general biological rule.

## 32. Cross-validation phải tôn trọng unit độc lập

Nếu unit biological thật là patient, split nên theo patient, không theo image patch hay cell riêng lẻ từ cùng patient.

Đây là cầu nối (bridge) giữa thiết kế thực nghiệm (experimental design) và ML: independence assumption phải phản ánh sampling quá trình (process).

## 33. Feature importance không phải causal importance

Một gene có predictive power lớn có thể chỉ là downstream marker. SHAP/importance score cho biết model dùng feature, không chứng minh gene driver disease.

Để test driver cần perturbation hoặc causal design.

## 34. Quy trình có thể tái lập (reproducible workflow) là một phần của science

Analysis nên track dữ liệu thô (raw data) checksum, reference version, software version, tham số (parameter), environment và code.

Workflow manager, container và version control giúp rerun pipeline và trace figure về source.

Một result không chỉ là final plot:

```text
raw data
→ QC
→ preprocessing
→ intermediate file
→ model
→ table
→ figure
→ biological interpretation
```

Nếu chain không trace được, reproducibility yếu.

## 35. Tình huống phân tích (case study): germline variant workflow end-to-end

Sample DNA được sequence thành FASTQ. QC kiểm quality/adapter. Read map lên reference. Duplicate/technical artifact được xử lý. Variant caller tính genotype likelihood. Biến thể (variant) được filter rồi annotate bằng gene/chức năng/cơ sở dữ liệu tần số (frequency).

Cuối cùng variant “pathogenic hay không” vẫn cần clinical/genetic evidence, di truyền (inheritance) pattern và kiểu hình (phenotype) bối cảnh (context).

Pipeline không biến raw read trực tiếp thành diagnosis; mỗi stage thu hẹp uncertainty một phần.

## 36. Tình huống phân tích: RNA-seq biểu hiện khác biệt không dừng ở volcano plot

Sau QC và count, mô hình thống kê tìm gene khác expression. Volcano plot chỉ là visualization.

Biological reasoning tiếp theo hỏi pathway nào enriched, effect có replicate không, cell composition có thay không, yếu tố phiên mã (transcription factor) nào plausible, và perturbation gene candidate có đổi phenotype không.

Omics là hypothesis engine mạnh, nhưng mechanism cần vòng experiment mới.

## 37. Các hiểu lầm phổ biến (common misconceptions)

“Bioinformatics chỉ là chạy tool” là sai. Tool encode assumption và tham số.

“Dataset càng lớn càng tự động đúng” sai; systematic bias không biến mất khi n tăng.

“AI tìm được feature quan trọng nghĩa đã tìm ra cơ chế (mechanism)” sai.

“Hệ gen tham chiếu là genome chuẩn của species” quá đơn giản; population có diversity và biến thể cấu trúc (structural variation).

## 38. Mô hình tư duy tổng hợp

Bioinformatics có thể nén thành flow:

```text
measurement
→ digital representation
→ QC
→ mapping/reconstruction
→ statistical inference
→ uncertainty
→ biological hypothesis
→ experimental validation
```

Mỗi stage vừa thêm information vừa làm mất một phần detail. Phân tích tốt giữ provenance và độ bất định đủ để biết conclusion mạnh đến đâu.

<!-- depth-audit-2026:ai-data-generating-process -->
## Bioinformatics phải bắt đầu từ data-generating process

FASTQ, count matrix hay embedding đều là output sau nhiều transformation. Sample collection, library preparation, sequencing chemistry, reference alignment và filtering quyết định distribution của data trước khi model nhìn thấy nó. Vì vậy một pattern machine learning tìm được có thể phản ánh batch, ancestry imbalance hoặc reference bias thay vì mechanism sinh học.

**Data leakage** xảy ra khi information từ test set lọt vào training/feature selection; **distribution shift** xảy ra khi population triển khai khác population train. Hai lỗi này đặc biệt nguy hiểm trong biomedical AI vì accuracy nội bộ cao có thể không giữ khi hospital, ancestry, instrument hoặc disease prevalence thay đổi.

Foundation model và protein language model có thể học representation mạnh từ sequence lớn, hỗ trợ structure/function prediction và variant prioritization. Nhưng prediction không đồng nghĩa causal mechanism. Model có thể nội suy statistical regularity mà không biết intervention sẽ làm gì trong cell thật. Validation tốt cần external dataset, perturbation experiment và uncertainty calibration.

AI hữu ích nhất khi đặt trong pipeline `biological question → measurement → representation → model → prediction → experimental test`, không phải khi thay toàn bộ biology bằng score.

## 39. Bridge sang Sinh học hệ thống (systems biology)

Omics cho ta component và trạng thái (state) ở scale lớn, nhưng vẫn chưa trả lời network sẽ phản ứng thế nào khi perturb. Biết gene A và B tăng cùng nhau không nói network động lực học (dynamics), phản hồi (feedback) hay causal direction.

Bước tiếp theo là xây model interaction, tốc độ (rate), feedback và perturbation — tức **Sinh học hệ thống**.

Xem tiếp [Sinh học hệ thống, mô hình hóa và sinh học tổng hợp](03_systems_biology_modeling_and_synthetic_biology.md).

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← Phương pháp thực nghiệm và đo lường trong Sinh học](01_experimental_methods_and_measurement.md) · [Mục lục Biology](../README.md) · [Sinh học hệ thống, mô hình hóa và sinh học tổng hợp →](03_systems_biology_modeling_and_synthetic_biology.md)
