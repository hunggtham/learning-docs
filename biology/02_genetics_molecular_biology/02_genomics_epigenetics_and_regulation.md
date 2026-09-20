# Genomics, epigenetics và điều hòa gene — Genomics, Epigenetics and Regulation (유전체학·후성유전학·유전자 조절)

Nếu genetics cổ điển thường hỏi “một gene ảnh hưởng trait này như thế nào?”, genomics (Genomics / 유전체학) mở rộng câu hỏi sang toàn bộ genome và interaction giữa hàng nghìn locus. Epigenetics (Epigenetics / 후성유전학) nghiên cứu những thay đổi bền tương đối trong gene activity không đòi hỏi thay đổi DNA sequence, còn gene regulation nghiên cứu cách cell quyết định khi nào và mức độ nào một gene được sử dụng.

## Genome không chỉ là danh sách gene

Genome (Genome / 유전체) bao gồm toàn bộ DNA của một organism. Ở eukaryote, phần lớn genome không trực tiếp mã hóa protein. Nó chứa regulatory sequence, intron, repetitive DNA, transposable element và nhiều vùng có function vẫn đang được nghiên cứu.

Vì vậy việc biết sequence chưa tương đương với việc hiểu system. Cần biết region nào được transcribe, chromatin mở hay đóng, protein nào binding, transcript nào được tạo và cell context nào đang xét.

## Chromatin là lớp organization và regulation

DNA eukaryote quấn quanh histone tạo nucleosome. Chromatin không chỉ để “nén DNA cho vừa nucleus”; mức độ đóng gói ảnh hưởng khả năng transcription machinery tiếp cận sequence.

Histone modification như acetylation, methylation và phosphorylation có thể liên quan đến trạng thái transcription khác nhau. Không nên học shortcut “acetylation = bật, methylation = tắt” như luật tuyệt đối, vì effect phụ thuộc residue, location và protein đọc dấu hiệu đó.

## DNA methylation

DNA methylation thường xảy ra ở cytosine trong CpG context ở vertebrate. Methylation ở promoter có thể liên hệ với gene silencing, nhưng relation phụ thuộc locus và cell type.

Epigenetic mark có thể được duy trì qua cell division, giúp liver cell tiếp tục giữ identity khác neuron dù genome gần như giống nhau.

> Mental model: genome là source code; epigenome không đơn giản là config file, mà giống runtime state và access-control layer quyết định vùng nào của source có thể được dùng trong từng cell.

## Enhancer và regulatory logic

Enhancer có thể nằm xa promoter trên linear DNA nhưng được đưa gần nhau trong 3D chromatin. Nhiều transcription factor phối hợp tạo combinatorial regulation.

Một gene vì vậy hiếm khi có một “công tắc” duy nhất. Expression level thường là output của một regulatory network gồm activator, repressor, chromatin state, RNA stability và signaling pathway.

## Alternative splicing và post-transcriptional regulation

Một pre-mRNA có thể được splice theo nhiều cách, tạo transcript khác nhau. miRNA có thể binding mRNA và làm giảm translation hoặc tăng degradation. RNA-binding protein cũng kiểm soát localization, stability và translation.

Điều này giải thích vì sao gene count của organism không trực tiếp tương ứng với complexity. Information processing nằm nhiều ở regulation và combinatorial reuse.

## Genomics hiện đại đo gì?

Whole-genome sequencing đọc DNA sequence. Exome sequencing tập trung vùng exon. RNA-seq đo transcript abundance và isoform. ChIP-seq khảo sát DNA region gắn với protein hoặc histone mark. ATAC-seq đánh giá chromatin accessibility. Single-cell RNA-seq cho phép đo gene-expression profile ở từng cell thay vì trung bình cả tissue.

Các technique này tạo dataset rất lớn, đưa biology sang vùng giao nhau với statistics và computer science.

## Variant, association và causality

Genome-wide association study (GWAS / 전장유전체연관분석) tìm association giữa genetic variant và trait trong population. Một association mạnh không tự động chứng minh variant đó là causal. Variant có thể chỉ linkage với causal locus hoặc bị confounding bởi population structure.

Khi đọc GWAS cần chú ý effect size, sample size, multiple-testing correction và replication. Vì kiểm tra hàng triệu variant, ngưỡng significance phải nghiêm ngặt hơn so với một hypothesis đơn lẻ.

## Epigenetic inheritance: cần phân biệt các nghĩa

Epigenetic state có thể được truyền qua mitotic cell division khá phổ biến. Transgenerational epigenetic inheritance qua nhiều thế hệ organism phức tạp hơn và bằng chứng phụ thuộc loài, mechanism và trait.

Một lỗi phổ biến là dùng “epigenetics” để nói rằng mọi trải nghiệm của bố mẹ đều được ghi vào gene và truyền ổn định cho con cháu. Claim như vậy thường vượt quá evidence.

## Genome như một dynamic system

Transposable element có thể di chuyển hoặc để lại dấu tích trong genome. Gene duplication tạo raw material để một copy giữ function cũ còn copy khác có thể diverge. Structural variant thay đổi copy number hoặc architecture của chromosome.

Genome vì vậy không phải document bất biến mà là hệ có lịch sử tiến hóa.

## Common misconceptions

“Non-coding DNA = junk DNA” là quá đơn giản. Một phần non-coding DNA có regulatory hoặc structural function, một phần có thể gần như neutral. Ngược lại, việc một sequence được transcribe không tự động chứng minh nó có function quan trọng.

“Epigenetics thay thế genetics” cũng sai. Epigenetic mechanism hoạt động trên substrate là genome và thường phụ thuộc protein do gene mã hóa; genetics và epigenetics là các lớp tương tác.

## Kết nối

Foundation molecular nằm ở [[00_dna_genes_and_gene_expression]]. Inheritance và mutation nằm ở [[01_inheritance_variation_and_mutation]]. Population genomics nối trực tiếp sang [[../03_evolution_and_diversity/00_evolution_and_population_genetics]], còn phương pháp phân tích sequencing được nối với [[../06_biotechnology_computation/00_biotechnology_bioinformatics_and_systems_biology]].
