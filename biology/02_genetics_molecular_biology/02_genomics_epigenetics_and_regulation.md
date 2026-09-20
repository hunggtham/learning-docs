# Genome, điều hòa gene và epigenetics — Genomics, Gene Regulation and Epigenetics (유전체, 유전자 조절, 후성유전학)

Nếu gần như mọi cell trong cơ thể có cùng DNA, tại sao neuron khác liver cell? Tại sao một cell chỉ tạo insulin còn cell khác tạo antibody? Câu trả lời không nằm chủ yếu ở việc mỗi cell “có gene khác”, mà ở việc **gene nào được dùng, dùng bao nhiêu, vào lúc nào và trong bối cảnh nào**.

Đây là lĩnh vực của gene regulation, epigenetics và genomics.

## Genome lớn hơn rất nhiều so với danh sách gene

**Genome (유전체)** là toàn bộ genetic material của organism/cell.

Trong human genome, protein-coding region chỉ chiếm một phần nhỏ. Phần còn lại gồm intron, regulatory element, noncoding RNA gene, repetitive sequence, transposable element và region có chức năng chưa hoàn toàn rõ.

Vì vậy “đã sequence genome” không có nghĩa “đã hiểu organism”. Sequence giống data layer; biological meaning phụ thuộc organization và context.

## Gene regulation giải quyết bài toán tiết kiệm và specialization

Một cell không cần biểu hiện mọi gene cùng mức. Việc đó vừa lãng phí energy vừa phá identity.

Gene regulation có thể xảy ra ở nhiều tầng:

```text
chromatin accessibility
      ↓
transcription initiation
      ↓
RNA processing
      ↓
RNA stability/localization
      ↓
translation
      ↓
protein modification/degradation
```

Mỗi tầng là một control point.

## Bacterial regulation — operon như một control module

Ở bacteria, các gene liên quan cùng function có thể nằm trong **operon (오페론)**.

Ví dụ kinh điển là **lac operon**, liên quan sử dụng lactose.

Nếu lactose không có, repressor có thể block transcription. Khi lactose/derivative xuất hiện, repression giảm. Đồng thời glucose level ảnh hưởng cAMP signaling, nên cell preferentially dùng glucose khi sẵn có.

Điểm đáng hiểu: operon không chỉ là “on khi có lactose”. Nó integrate nhiều information về nutrient availability.

Đây là một early example của biological logic gate.

## Eukaryotic regulation — nhiều layer và khoảng cách lớn

Eukaryotic genome được đóng gói trong chromatin, nên trước khi RNA polymerase đọc DNA, region phải accessible đủ mức.

### Promoter

Promoter là region gần transcription start site, nơi transcription machinery assemble.

### Enhancer

**Enhancer (인핸서)** là regulatory DNA có thể ở xa gene. Transcription factor bind enhancer; DNA looping đưa complex lại gần promoter.

Một gene có thể chịu ảnh hưởng nhiều enhancer, và một enhancer có thể hoạt động chỉ trong cell type hoặc developmental stage nhất định.

Điều này giúp giải thích cell-specific expression.

## Transcription factor — protein đọc regulatory state

**Transcription factor (yếu tố phiên mã / 전사인자)** là protein bind DNA motif và ảnh hưởng transcription.

Không phải mỗi factor đơn độc quyết định on/off. Nhiều factor kết hợp, interact với coactivator/corepressor và chromatin machinery.

Gene expression vì thế giống computation trên nhiều input hơn là một switch đơn giản.

## Chromatin — DNA packaging cũng là regulation

DNA quấn quanh histone tạo **nucleosome (뉴클레오솜)**. Nucleosome tiếp tục tổ chức thành chromatin.

Nếu DNA region packed chặt, transcription machinery khó access hơn. Nếu chromatin open hơn, transcription thường dễ hơn.

Hai trạng thái textbook thường gọi **euchromatin** (thường accessible hơn) và **heterochromatin** (thường condensed hơn), nhưng real chromatin là continuum động.

## Epigenetics thực sự là gì?

**Epigenetics (biểu sinh / 후성유전학)** thường nói đến stable hoặc heritable change trong gene regulation/state không do thay đổi DNA sequence trực tiếp.

Hai mechanism nổi bật là DNA methylation và histone modification, nhưng epigenetic regulation rộng hơn và context-dependent.

### DNA methylation

Ở vertebrate, methyl group thường được thêm vào cytosine trong CpG context. Methylation ở promoter region thường liên quan transcriptional repression, nhưng interpretation phụ thuộc location và context.

### Histone modification

Histone tail có thể acetylation, methylation và nhiều modification khác.

Acetylation thường liên quan chromatin accessibility tăng trong nhiều context vì làm giảm interaction giữa histone và DNA, nhưng không nên biến thành rule “acetyl = on, methyl = off” quá đơn giản. Histone methylation có thể activate hoặc repress tùy residue.

## Epigenetic không có nghĩa “mọi trải nghiệm được truyền cho con cháu”

Đây là misconception phổ biến.

Environment có thể ảnh hưởng gene expression và epigenetic mark. Một số mark có thể tồn tại qua cell division; một số trường hợp transgenerational inheritance tồn tại ở vài organism/context.

Nhưng ở mammal, nhiều epigenetic mark được reset mạnh trong gametogenesis và early embryo. Vì vậy claim rằng một lifestyle event cụ thể chắc chắn “ghi vào epigenome và truyền nhiều thế hệ” cần evidence rất cẩn thận.

## X-chromosome inactivation — ví dụ epigenetic ở cấp chromosome

Female mammal thường có hai X chromosome. Nếu cả hai active hoàn toàn, dosage của X-linked gene sẽ cao hơn nhiều so với male có một X.

Một X chromosome trong mỗi somatic cell thường bị largely inactivated sớm trong development.

Process này liên quan long noncoding RNA XIST và chromatin modification.

Kết quả là body female là mosaic: cell khác nhau có thể active X khác nhau.

## Genomic imprinting

Ở một số gene, expression phụ thuộc allele đến từ mother hay father. Đây gọi là **genomic imprinting (유전체 각인)**.

Một allele có thể bị epigenetically silenced theo parent-of-origin.

Imprinting cho thấy hai allele có sequence tương tự nhưng regulatory history khác nhau có thể hoạt động khác nhau.

## Noncoding RNA — RNA không chỉ là messenger

Ngoài mRNA, cell dùng nhiều RNA regulatory.

**microRNA (miRNA)** có thể bind mRNA và làm giảm translation hoặc tăng degradation.

**long noncoding RNA (lncRNA)** có nhiều role trong chromatin, transcription và organization; function rất đa dạng và không phải mọi lncRNA đều đã hiểu rõ.

RNA vì thế là cả information carrier lẫn regulatory molecule.

## Genome sequencing — từ molecule thành data

**Sequencing (giải trình tự / 염기서열 분석)** xác định order nucleotide.

Early sequencing đọc fragment tương đối ngắn; modern high-throughput sequencing có thể tạo hàng triệu/billion reads.

Nhưng raw read chưa phải genome hoàn chỉnh. Bioinformatics phải quality-control, align hoặc assemble, rồi variant calling và annotation.

Đây là chỗ Biology nối trực tiếp với Computer Science.

## Reference genome và individual genome

Một **reference genome** là coordinate framework đại diện, không phải “genome chuẩn tuyệt đối của loài”.

Individual có hàng triệu variant so với reference, phần lớn không gây disease.

Khi nói “mutation so với reference”, cần phân biệt variant bình thường trong population với pathogenic variant.

## SNP, indel và structural variant

**SNP/SNV** là difference một nucleotide.

**Indel** là insertion/deletion nhỏ.

**Structural variant** có thể là deletion, duplication, inversion, translocation hoặc rearrangement lớn.

Genome variation vì vậy không chỉ là thay một “chữ”.

## Genome-wide association study — liên kết variant với trait

**GWAS (전장유전체 연관분석)** so sánh variant frequency với phenotype trong large population.

Nếu variant gần một locus xuất hiện thường hơn ở group có trait, ta có statistical association.

Nhưng association không tự động chứng minh causation. Variant marker có thể chỉ linked với causal variant; population structure và confounder cũng phải được kiểm soát.

P-value nhỏ không nói effect lớn. Nhiều common variant có effect size rất nhỏ nhưng cộng lại ảnh hưởng polygenic trait.

## Polygenic score — prediction chứ không phải destiny

**Polygenic score (다유전자 점수)** kết hợp effect estimate của nhiều variant để ước lượng genetic propensity cho trait trong population phù hợp.

Score phụ thuộc training population, phenotype definition và statistical model. Transfer giữa ancestry group có thể giảm accuracy.

Vì vậy polygenic score không phải “mã số định mệnh” của cá nhân.

## Single-cell genomics — tại sao bulk average che mất biology?

Nếu nghiền cả tissue và đo average RNA, signal của rare cell type có thể biến mất.

**Single-cell RNA sequencing (scRNA-seq / 단일세포 RNA 시퀀싱)** đo transcriptome của từng cell, giúp cluster cell type và infer cell state.

Nhưng data rất sparse/noisy; clustering và dimensionality reduction là model, không phải ground truth tuyệt đối.

Đây là ví dụ rõ rằng modern biology vừa là wet lab vừa là data science.

## Systems biology — gene không hoạt động một mình

**Systems biology (hệ thống sinh học / 시스템 생물학)** nghiên cứu network interaction giữa gene, protein, metabolite và signal.

Một gene có thể regulate nhiều target; target feedback lại regulator. Vì vậy phenotype có thể xuất hiện từ network dynamics.

Graph theory dùng node–edge để mô tả gene regulatory network hoặc protein interaction network. Differential equation có thể mô tả concentration thay đổi theo time.

## Common misconceptions

### “Epigenetics thay đổi DNA”

Epigenetic regulation thường không thay base sequence trực tiếp. Nó thay accessibility/expression state.

### “Gene bị methyl hóa thì luôn off”

Không. Effect phụ thuộc genomic location và context.

### “Genome sequence cho biết chính xác tương lai sức khỏe”

Không. Phần lớn trait complex là probabilistic và phụ thuộc environment, age, development, interaction giữa nhiều gene.

### “Noncoding DNA là junk”

Một số noncoding region có function quan trọng; một số có thể ít/no known function. Không nên suy từ “không mã hóa protein” thành “vô dụng”.

## Mental Model

> Genome là storage lớn; chromatin quyết định vùng nào accessible; regulatory DNA và transcription factor quyết định khi nào gene được đọc; RNA layer tinh chỉnh message; genome variation tạo khác biệt giữa individual; genomics dùng computation để đọc pattern trên quy mô lớn.

Từ đây genetics đã đủ nền để bước sang [[../03_evolution_and_diversity/00_evolution_and_population_genetics]]: nếu allele frequency thay đổi qua nhiều thế hệ thì population sẽ tiến hóa như thế nào?