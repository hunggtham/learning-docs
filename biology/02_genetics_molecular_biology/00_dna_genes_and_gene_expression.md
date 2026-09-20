# DNA, gene và biểu hiện gene — DNA, Genes and Gene Expression (DNA·유전자·유전자 발현)

Một hệ sống cần lưu giữ information đủ ổn định để truyền qua thế hệ, nhưng cũng phải có cách đọc và sử dụng information đó trong thời gian thực. DNA giải quyết phần lưu trữ; RNA và protein giúp chuyển information thành structure và function. Molecular biology nghiên cứu chính pipeline này cùng các cơ chế kiểm soát, sửa lỗi và biến đổi của nó.

## DNA là polymer mang information

DNA (Deoxyribonucleic Acid / 디옥시리보핵산) được tạo từ nucleotide gồm deoxyribose, phosphate và nitrogenous base. Bốn base chính là adenine, thymine, guanine và cytosine. Hai strand chạy ngược chiều và bắt cặp bổ sung A–T, G–C.

Điều làm DNA phù hợp để lưu information không chỉ là double helix. Trình tự base tạo một alphabet bốn ký tự có thể copy theo nguyên tắc complementary pairing. Backbone sugar-phosphate tương đối ổn định, còn base sequence có thể thay đổi mà không phá toàn bộ cấu trúc polymer.

> Mental model: DNA giống một storage medium có redundancy và rule sao chép rõ ràng; gene là vùng information có thể được cell sử dụng trong context nhất định, không phải “một hạt vật chất” độc lập.

## Gene không chỉ là đoạn “mã hóa protein”

Gene (Gene / 유전자) là đơn vị genomic information có sản phẩm chức năng. Nhiều gene mã hóa protein thông qua messenger RNA, nhưng nhiều gene tạo functional RNA như rRNA, tRNA, miRNA hoặc lncRNA.

Ở eukaryote, một protein-coding gene thường có promoter, regulatory region, exon và intron. Vì alternative splicing, một gene có thể tạo nhiều transcript và nhiều protein isoform. Do đó quan niệm “một gene = một protein” chỉ là approximation lịch sử.

## DNA replication và vấn đề sao chép

Trước cell division, genome phải được copy. DNA polymerase chỉ tổng hợp strand mới theo hướng 5' → 3'. Vì hai template strand antiparallel, leading strand được tổng hợp tương đối liên tục còn lagging strand hình thành qua Okazaki fragments.

Helicase mở double helix; primase tạo primer; DNA polymerase kéo dài; ligase nối fragment. Proofreading và repair giảm mạnh error rate.

Replication là semiconservative: mỗi daughter DNA molecule giữ một strand cũ và có một strand mới. Cấu trúc complementary của DNA khiến cơ chế này có thể hoạt động.

## Từ DNA sang RNA: transcription

Phiên mã (Transcription / 전사) là quá trình RNA polymerase dùng DNA template để tạo RNA. Polymerase nhận promoter và tổng hợp RNA theo 5' → 3'. Ở eukaryote, primary transcript thường được xử lý bằng 5' cap, poly-A tail và splicing trước khi trở thành mature mRNA.

Regulation có thể xảy ra ngay ở transcription initiation. Transcription factor gắn regulatory DNA, làm tăng hoặc giảm khả năng machinery tiếp cận promoter. Đây là một lý do cell có cùng genome nhưng neuron khác liver cell: chúng bật và tắt các tập gene khác nhau.

## Từ RNA sang protein: translation

Dịch mã (Translation / 번역) diễn ra trên ribosome. mRNA được đọc theo codon, mỗi codon gồm ba nucleotide. tRNA mang amino acid tương ứng nhờ anticodon pairing. Ribosome xúc tác peptide bond để tạo polypeptide.

Genetic code là redundant: nhiều codon có thể mã hóa cùng amino acid. Redundancy này làm một số mutation ở base thứ ba không đổi amino acid.

Start codon thường là AUG; stop codon không mã hóa amino acid mà báo cho release factor kết thúc translation.

## Protein không kết thúc ở translation

Polypeptide phải fold thành cấu trúc phù hợp; nhiều protein còn được phosphorylate, glycosylate, cắt proteolytically hoặc vận chuyển đến compartment cụ thể. Vì vậy phenotype không thể suy ra trực tiếp chỉ từ DNA sequence mà bỏ qua regulation và cell context.

## Central dogma và giới hạn của slogan

Central dogma thường được viết:

```text
DNA → RNA → Protein
```

Sơ đồ này hữu ích nhưng quá ngắn nếu coi nó là toàn bộ biology. RNA có thể là sản phẩm cuối có chức năng. Retrovirus dùng reverse transcription RNA → DNA. Protein và metabolite cũng feedback lên gene expression. Central dogma chủ yếu nói về direction của sequence information, không nói rằng mọi causal influence chỉ đi một chiều.

## Gene regulation ở prokaryote và eukaryote

Bacteria thường tổ chức gene liên quan thành operon. Lac operon là model kinh điển cho việc kết hợp signal về lactose và glucose để điều chỉnh enzyme metabolism.

Eukaryote dùng promoter, enhancer, silencer, chromatin state, transcription factor và RNA processing. Regulation ở nhiều layer giúp multicellular organism tạo hàng trăm cell type từ một genome gần như giống nhau.

## Protein structure và sequence

Primary structure là amino-acid sequence. Secondary structure gồm alpha helix và beta sheet. Tertiary structure là 3D folding của một chain; quaternary structure là assembly của nhiều subunit.

Sequence ảnh hưởng structure qua hydrophobic effect, hydrogen bond, ionic interaction và disulfide bond. Tuy nhiên folding không đơn giản là “mỗi sequence có một hình duy nhất”; protein có dynamics, conformational state và có thể misfold.

## Common misconceptions

“DNA quyết định hoàn toàn số phận” là sai. Genome tạo constraint và potential, nhưng phenotype xuất hiện từ interaction giữa gene, regulation, development và environment.

“Gene trội mạnh hơn gene lặn” cũng là cách nói sai bản chất. Dominance mô tả phenotype của heterozygote, không nói allele nào mạnh hơn về mặt vật lý hay phổ biến hơn trong population.

## Kết nối

Mutation và inheritance được phát triển trong [[01_inheritance_variation_and_mutation]]. Regulation dài hạn và genome-wide analysis nằm ở [[02_genomics_epigenetics_and_regulation]]. Những variation trong DNA trở thành raw material của [[../03_evolution_and_diversity/00_evolution_and_population_genetics]]. Biotechnology khai thác chính các cơ chế này trong [[../06_biotechnology_computation/00_biotechnology_bioinformatics_and_systems_biology]].
