# Công nghệ sinh học, bioinformatics và systems biology — Biotechnology, Bioinformatics and Systems Biology (생명공학, 생물정보학, 시스템생물학)

Sau khi hiểu DNA, protein, cell, physiology, evolution và ecology, ta có thể hỏi một loại câu hỏi mới: **làm thế nào để đo, đọc, so sánh và thay đổi biological system một cách có kiểm soát?**

Đó là vùng giao nhau của biotechnology và computational biology. Điều quan trọng là không học các kỹ thuật như danh sách acronym. Mỗi kỹ thuật tồn tại vì nó giải quyết một bottleneck cụ thể: quá ít DNA để đo, sequence quá dài để đọc trực tiếp, genome quá lớn để so bằng mắt, network quá phức tạp để hiểu bằng intuition đơn thuần.

## Biotechnology bắt đầu từ khả năng thao tác molecule

**Biotechnology (công nghệ sinh học / 생명공학)** sử dụng organism, cell hoặc biological molecule để tạo measurement, product hay intervention.

Con người đã dùng fermentation hàng nghìn năm trước khi biết microorganism. Modern biotechnology khác ở mức độ control: ta có thể isolate DNA, amplify sequence, clone gene, express recombinant protein, sequence genome và edit selected locus.

## DNA extraction — tách information carrier khỏi cell

Muốn nghiên cứu DNA, trước tiên phải phá cell, loại protein/lipid và thu nucleic acid đủ sạch.

Nguyên lý chung của **DNA extraction (DNA 추출)** là:

```text
cell/tissue
→ lysis
→ remove protein/lipid/contaminant
→ recover DNA
```

Detergent phá membrane vì membrane chứa lipid. Protease có thể xử lý protein. Salt/alcohol hoặc silica chemistry được dùng để recover nucleic acid tùy protocol.

Điều cần hiểu không phải một recipe cố định mà là chemical problem: DNA là polymer charged, hydrophilic; ta thay condition để tách nó khỏi component khác.

## Gel electrophoresis — tách DNA theo kích thước

DNA backbone mang negative charge nhờ phosphate. Trong electric field, DNA di chuyển về positive electrode.

Agarose gel tạo porous network. Fragment nhỏ đi qua pore dễ hơn và di chuyển xa hơn fragment lớn.

Vì vậy **gel electrophoresis (겔 전기영동)** biến invisible DNA mixture thành band theo size.

Đây là example kết nối Biology với Physics: electric force + molecular sieving.

## PCR — giải quyết bài toán “mẫu DNA quá ít”

**Polymerase chain reaction (PCR / 중합효소연쇄반응)** amplify một target DNA region.

Một cycle có ba idea:

1. denaturation: heat tách DNA strand;
2. annealing: primer bind complementary target;
3. extension: thermostable DNA polymerase kéo dài strand.

Sau mỗi cycle lý tưởng, target gần double. Nếu efficiency hoàn hảo:

\[
N_n=N_0 2^n
\]

Sau 30 cycle, theoretical amplification là hơn một tỷ lần.

Thực tế efficiency không 100%, reagent trở thành limiting và product accumulation plateau.

### Primer quyết định specificity

Primer là short DNA sequence định nghĩa boundary target. Nếu primer bind sai location, nonspecific product xuất hiện.

PCR vì vậy là combination của sequence design + thermodynamics + enzyme kinetics.

## qPCR — từ có/không sang định lượng

**Quantitative PCR (qPCR / 실시간 PCR)** theo dõi fluorescence trong amplification.

Cycle threshold thấp hơn thường nghĩa starting template nhiều hơn, nhưng quantitative interpretation cần efficiency, standard/reference và normalization.

Khi dùng reverse transcription trước PCR để đo RNA, ta có RT-qPCR.

RNA được convert thành cDNA vì standard DNA polymerase PCR cần DNA template.

## Restriction enzyme và cloning

**Restriction enzyme (제한효소)** nhận sequence DNA đặc hiệu và cắt DNA.

**DNA ligase** nối DNA end.

Classical molecular cloning dùng restriction/ligation hoặc modern assembly method để đưa DNA insert vào vector như plasmid.

Plasmid thường có origin of replication, selectable marker và cloning/expression region.

Khi plasmid được đưa vào bacteria, bacteria có thể replicate plasmid; nếu vector expression phù hợp, cell có thể produce recombinant protein.

## Recombinant protein — gene trở thành factory instruction

Human insulin historically từng được lấy từ animal pancreas; recombinant DNA technology cho phép đưa human insulin gene vào microorganism production system.

Nhưng “đưa gene vào là xong” quá đơn giản. Expression cần promoter, codon/context phù hợp, folding, post-translational modification và purification.

E. coli tốt cho nhiều protein nhưng không thực hiện mọi eukaryotic modification, nên mammalian/yeast/insect cell system được dùng tùy protein.

## Sequencing — đọc order nucleotide

### Sanger sequencing

Sanger method dùng chain-terminating nucleotide để tạo fragment kết thúc ở từng base, sau đó phân tách theo size để infer sequence.

Nó đọc tương đối dài và accuracy cao nhưng throughput thấp hơn modern sequencing.

### Next-generation sequencing

**NGS (차세대 염기서열 분석)** tạo rất nhiều short/medium read song song.

Thay vì đọc chromosome từ đầu tới cuối trong một molecule hoàn hảo, ta nhận millions reads rồi computationally reconstruct hoặc align.

Đây là lý do sequencing trở thành data problem.

### Long-read sequencing

Long-read technology đọc molecule dài hơn, giúp resolve repetitive region, structural variant và genome assembly. Error profile và cost trade-off thay đổi theo platform/generation.

Không có “best sequencing” tuyệt đối; choice phụ thuộc question.

# Bioinformatics — khi biological information thành data structure

**Bioinformatics (tin sinh học / 생물정보학)** dùng algorithm, statistics và computation để lưu, so sánh và interpret biological data.

Một DNA sequence có thể được biểu diễn như string trên alphabet `{A,C,G,T}`. Từ góc CS, nhiều bài toán biology trở thành string matching, dynamic programming, graph, probabilistic inference và large-scale data processing.

## Sequence alignment — hai sequence giống nhau đến đâu?

Nếu hai sequence share ancestry, mutation có thể tạo substitution, insertion, deletion.

**Alignment (정렬)** cố đặt character tương ứng sao cho relation hợp lý.

Ví dụ:

```text
ACGTTGCA
ACG-TGGA
```

Gap đại diện insertion/deletion hypothesis.

## Global và local alignment

**Global alignment** cố align toàn sequence, phù hợp sequence cùng chiều dài/relatedness cao.

**Local alignment** tìm region tương đồng tốt nhất, hữu ích khi protein share domain hoặc sequence dài chỉ có một đoạn related.

Needleman–Wunsch và Smith–Waterman dùng **dynamic programming** để tìm optimal alignment theo scoring scheme.

Connection với Computer Science không phải ví dụ trang trí: đây là algorithm thực sự đứng sau molecular comparison.

## Scoring alignment

Match được reward; mismatch và gap bị penalty. Với protein, substitution matrix như BLOSUM encode probability/biological plausibility của amino-acid replacement.

Thay scoring parameter có thể đổi alignment. Vì vậy alignment là model-based inference, không phải một “sự thật duy nhất” không phụ thuộc assumption.

## Genome assembly — reconstruct từ fragment

Nếu không có reference, reads phải được ghép thành genome.

Một approach dùng overlap giữa read; modern short-read assembly thường dùng **de Bruijn graph** từ k-mer.

Node/edge biểu diễn overlap sequence. Repetitive DNA tạo ambiguity giống việc ghép puzzle có nhiều mảnh giống nhau.

Long read giúp bridge repeat region dài hơn.

## Read mapping

Nếu có reference genome, read được align vào reference.

Challenge gồm sequencing error, repetitive region và true biological variant.

Mapper thường dùng index/data structure để tránh so mỗi read với mọi position, vì brute force quá chậm.

## Variant calling

Sau mapping, software tìm position nơi sample khác reference.

Nhưng một mismatch có thể đến từ sequencing error. Vì vậy variant caller dùng read depth, base quality, mapping quality và probabilistic/statistical model.

“Computer thấy chữ khác” chưa đủ để kết luận biological variant.

## Gene expression data

RNA-seq đo abundance RNA transcript bằng sequencing.

Pipeline conceptual:

```text
RNA → library → sequencing reads → QC → alignment/quantification → normalization → statistical comparison
```

Raw read count phụ thuộc sequencing depth và gene length/context, nên comparison cần normalization.

**Differential expression** nói gene có evidence expression khác giữa condition; nó không tự chứng minh gene gây phenotype.

## Multiple testing

Genome-wide analysis có thể test hàng nghìn gene.

Nếu dùng p < 0.05 cho 20,000 test độc lập dưới null, số false positive kỳ vọng có thể rất lớn.

Do đó bioinformatics dùng correction như **false discovery rate (FDR)**.

Đây là connection quan trọng với statistics: dữ liệu lớn không tự động làm inference đúng; multiple comparison làm vấn đề khó hơn.

## Single-cell data

Single-cell RNA-seq tạo matrix cell × gene rất lớn và sparse.

Workflow thường có quality control, normalization, dimensionality reduction, clustering và marker interpretation.

PCA, nearest-neighbor graph, UMAP/t-SNE thường xuất hiện.

Clustering là computational grouping dựa feature; biological cell type cần validation bằng marker, function và context. Algorithm không “phát hiện cell type” một cách tuyệt đối.

# CRISPR — từ immune mechanism của bacteria đến genome editing

**CRISPR–Cas** bắt nguồn từ adaptive defense system ở bacteria/archaea.

Trong engineered genome editing, guide RNA đưa Cas nuclease đến DNA target có sequence phù hợp và PAM requirement.

Cas tạo cut; cell repair DNA bằng pathway như NHEJ hoặc HDR.

NHEJ thường tạo small indel, useful cho gene disruption. HDR có thể đưa template-directed change nhưng efficiency/context khác nhau.

Điểm quan trọng: CRISPR không “viết DNA tùy ý như text editor” hoàn hảo. Off-target, delivery, mosaicism và repair outcome là practical constraint.

## Gene editing khác gene therapy

**Gene editing** thay sequence genome ở target.

**Gene therapy** rộng hơn: có thể đưa functional gene copy mà không edit original locus.

Vector delivery, target tissue, duration expression và immune response là central design issue.

# Omics — đo nhiều layer cùng lúc

**Genomics**: DNA/genome.

**Transcriptomics**: RNA expression.

**Proteomics**: protein abundance/modification.

**Metabolomics**: small metabolite.

Mỗi layer trả lời câu hỏi khác. DNA relatively stable; RNA dynamic; protein gần function hơn nhưng khó đo; metabolite phản ánh state gần phenotype.

Một genome không đủ để suy toàn bộ cell state.

# Systems biology — từ list thành network

Nếu thousands gene/protein interact, ta cần model network.

## Graph model

Node có thể là gene/protein/metabolite; edge là regulation hoặc physical interaction.

Degree, centrality, module và community detection giúp mô tả network.

Nhưng network database có bias: protein được nghiên cứu nhiều có thể có nhiều recorded edge hơn.

## Dynamic model

Concentration một protein \(X\) có thể model đơn giản:

\[
\frac{dX}{dt}=production-degradation
\]

Nếu production bị regulator Y ảnh hưởng:

\[
\frac{dX}{dt}=f(Y)-kX
\]

Differential equation giúp hỏi system có stable state, oscillation hay switch behavior.

Gene regulatory circuit và signaling pathway có thể được nhìn như control system.

## Feedback tạo switch và oscillation

Positive feedback có thể tạo bistability: system ở state OFF hoặc ON.

Negative feedback với delay có thể tạo oscillation.

Circadian clock và developmental switch cho thấy dynamical systems concept rất relevant biology.

# Machine learning trong biology

ML có thể predict protein structure/property, classify cell, estimate regulatory pattern hoặc model medical image/genomic data.

Nhưng biology data thường có high dimension, small effective sample, batch effect và confounding.

Một model accuracy cao trên test set cùng distribution chưa chắc generalize sang hospital/population khác.

Interpretation phải tách **prediction** khỏi **causal explanation**.

## Feature và representation

DNA sequence có thể encode bằng one-hot, k-mer, embedding hoặc pretrained sequence model.

Protein có sequence embedding, structure graph và physicochemical feature.

Representation quyết định pattern model có thể dễ học.

## Data leakage

Nếu highly similar sequence của cùng family nằm cả train/test, performance có thể bị inflated. Split strategy phải phản ánh real deployment question, ví dụ split theo protein family hoặc time.

Đây là software/ML principle có consequence sinh học trực tiếp.

# Synthetic biology — engineering biological circuit

**Synthetic biology (합성생물학)** cố thiết kế biological component/circuit theo engineering principle.

Một genetic circuit có promoter, sensor, regulator và output.

Logic gate có thể được implement approximate bằng gene regulation:

```text
Input A + Input B → regulatory network → reporter output
```

Nhưng biological component noisy, context-dependent và burden host cell. Vì vậy “programming cell” là analogy hữu ích nhưng cell không deterministic như CPU.

# Ethics và interpretation

Khả năng sequence/edit genome tạo vấn đề privacy, consent, equity và long-term consequence.

Genetic data có tính familial: information về một người có thể gợi ý information về relative.

Gene-editing germline còn ảnh hưởng generation chưa thể consent và có uncertainty dài hạn.

Do đó biotechnology không chỉ là technical optimization; governance và ethics là part của responsible science.

## Common misconceptions

### “PCR đọc sequence DNA”

PCR chủ yếu amplify target. Sequencing mới xác định order base.

### “CRISPR thay gene chính xác 100%”

Không. Targeting và repair đều có constraint/error possibility.

### “Bioinformatics chỉ là vẽ biểu đồ”

Bioinformatics gồm algorithm, data structure, statistics, database và biological inference.

### “AI có thể tự tìm causal mechanism từ data lớn”

Không tự động. Prediction, association và causation là ba mục tiêu khác nhau.

## Mental Model

> Biotechnology thao tác biological matter; sequencing biến molecule thành data; bioinformatics biến data thành inference; systems biology biến list thành network/dynamics; synthetic biology thử biến understanding thành controllable circuit. Mỗi bước thêm sức mạnh nhưng cũng thêm assumption và uncertainty.

Để thấy các connection xuyên toàn thư viện giữa scale, mathematics và computation, đọc [[../90_connections/00_biology_math_computation_and_scale]].