# Genomics, epigenetics và điều hòa — Genomics, Epigenetics and Regulation (유전체학, 후성유전학과 조절)

Hai chương trước xây information flow từ DNA đến protein và giải thích cách allele được truyền qua meiosis. Nhưng khi nhìn toàn genome, một câu hỏi lớn xuất hiện: **nếu gần như mọi cell trong cơ thể mang cùng DNA, vì sao neuron, muscle cell và liver cell lại khác nhau?**

Câu trả lời không nằm ở sequence alone. Cell type khác nhau vì chúng sử dụng những phần khác nhau của genome, ở mức độ khác nhau và vào thời điểm khác nhau. Chương này nối molecular genetics với development, physiology và modern genomics bằng cách xem genome như một **regulated information system** chứ không phải một danh sách gene.

## 1. Genome lớn hơn tổng các gene

**Genome (bộ gene / 유전체)** là toàn bộ genetic material của organism.

Ở eukaryote, chỉ một phần genome trực tiếp encode protein. Phần còn lại chứa regulatory region, intron, repetitive sequence, transposable element, noncoding RNA gene và nhiều sequence có function hoặc lịch sử tiến hóa khác nhau.

Do đó câu “98% DNA không mã hóa protein” không đồng nghĩa “98% vô dụng”. Nhưng cũng không nên đi tới extreme ngược lại rằng mọi nucleotide đều có function thiết yếu.

Genomics phải phân biệt **biochemical activity**, **evolutionary constraint** và **organism-level function**.

## 2. Chromatin: accessibility là một layer regulation

DNA eukaryote quấn quanh histone tạo nucleosome. Nucleosome tiếp tục được tổ chức thành chromatin.

Nếu một promoter nằm trong chromatin khó tiếp cận, transcription factor khó bind. Nếu chromatin mở hơn, probability transcription tăng.

Vì vậy gene expression không chỉ phụ thuộc “có promoter hay không” mà còn phụ thuộc physical accessibility.

Ta có một causal chain:

```text
chromatin state
    ↓
DNA accessibility
    ↓
transcription-factor binding
    ↓
transcription probability
```

## 3. Epigenetics: state có thể thay đổi mà sequence không đổi

**Epigenetics (후성유전학)** nghiên cứu stable changes in gene regulation hoặc cellular state không cần thay đổi DNA sequence.

Các mechanism thường được nhắc gồm DNA methylation, histone modification, chromatin remodeling và regulatory RNA.

Nhưng cần tránh cách hiểu “epigenetics là một lớp mã bí ẩn đứng trên gene”. Các mark thường là một phần của regulatory network động và có thể vừa là cause vừa là consequence của gene activity.

## 4. DNA methylation

Ở mammal, methylation thường xảy ra ở cytosine trong CpG context.

Methylation ở promoter-rich CpG island thường liên quan reduced transcription, nhưng relationship phụ thuộc genomic context.

Methylation có thể giúp maintain cell identity qua division vì pattern được copy tương đối ổn định.

Điều này rất quan trọng trong development: một liver cell cần “nhớ” chương trình liver khi divide.

## 5. Histone modification và chromatin remodeling

Histone tail có thể được acetylated, methylated và modified theo nhiều cách.

Histone acetylation thường liên quan chromatin mở hơn vì giảm interaction electrostatic giữa histone và DNA, nhưng biology thật phức tạp hơn một rule tuyệt đối.

Chromatin-remodeling complex có thể dùng ATP để reposition nucleosome.

Một lần nữa ATP từ metabolism trở lại trong gene regulation: information processing không tách khỏi energy.

## 6. Enhancer và 3D genome

Enhancer có thể nằm rất xa gene theo linear sequence nhưng lại gần trong 3D nucleus nhờ DNA folding.

Genome vì thế không chỉ là string 1D. Spatial organization ảnh hưởng regulatory contact.

Topologically associating domains và chromatin loop là ví dụ cho cách 3D architecture constrain interaction.

Điều này nối structure–function principle từ protein lên scale chromosome.

## 7. Alternative splicing và transcriptome

Một gene có thể tạo nhiều RNA isoform bằng alternative splicing.

**Transcriptome (전사체)** là tập RNA được expression trong cell/tissue ở một thời điểm.

Genome tương đối ổn định, nhưng transcriptome thay đổi mạnh theo cell type, development, circadian rhythm, stress và signaling.

Do đó khi hỏi “gene này có hoạt động không?”, thường phải chỉ rõ **ở cell nào, lúc nào và condition nào**.

## 8. Proteome: RNA abundance chưa phải function cuối

mRNA level không luôn tỷ lệ trực tiếp protein level. Translation efficiency và protein degradation cũng quan trọng.

**Proteome (단백질체)** là tập protein được expression trong một cell/tissue.

Protein còn có post-translational modification như phosphorylation, glycosylation, ubiquitination.

Vì vậy system có nhiều layer:

```text
genome
 ↓
epigenome / chromatin
 ↓
transcriptome
 ↓
proteome
 ↓
metabolome / phenotype
```

Các layer interaction hai chiều qua signaling và metabolism.

## 9. Omics: đo nhiều thành phần cùng lúc

Modern biology dùng suffix **-omics** cho large-scale measurement.

Genomics đo DNA variation. Transcriptomics đo RNA. Proteomics đo protein. Metabolomics đo small molecule.

Ý tưởng mạnh là thay vì chọn một molecule trước, ta đo hàng nghìn/millions feature rồi tìm pattern.

Nhưng data-rich không tự động causal. Omics thường rất mạnh để discovery correlation, nhưng experiment thêm vẫn cần để test mechanism.

## 10. Sequencing biến biology thành data science

DNA sequencing biến physical molecule thành sequence data.

Ở mức computation, genome trở thành string trên alphabet A/C/G/T. Điều này cho phép alignment, variant calling, phylogenetic inference và assembly.

Nhưng raw read không phải genome hoàn chỉnh. Sequencing machine tạo measurement có error; reads phải được quality-control, mapped hoặc assembled.

Biology hiện đại vì thế nối wet lab với algorithm.

Chương [[../06_biotechnology_computation/00_biotechnology_bioinformatics_and_systems_biology]] sẽ đi sâu hơn.

## 11. Genetic variant: từ single nucleotide đến structural variation

Population genome chứa nhiều loại variation: SNP, small insertion/deletion, copy-number variation và large structural rearrangement.

Không phải variant nào cũng ảnh hưởng phenotype. Nhiều variant neutral hoặc effect cực nhỏ.

Đây là lý do modern genetics thường cần statistical sample rất lớn.

## 12. GWAS: association không phải mechanism

**Genome-wide association study (GWAS / 전장유전체연관분석)** tìm variant có frequency khác nhau liên quan tới trait.

Nếu một SNP associated với disease risk, điều đó không nhất thiết SNP đó là causal. Nó có thể chỉ linked với causal variant gần đó.

GWAS vì thế tạo hypothesis region; functional experiment cần xác định mechanism.

Đây là causal-reasoning principle ở chapter đầu quay lại trong genomics.

## 13. Polygenic architecture

Nhiều complex trait chịu effect của rất nhiều variant nhỏ.

Một **polygenic score** cộng weighted effect của nhiều allele để estimate genetic propensity trong population tương tự training data.

Nhưng score không phải destiny. Predictive performance phụ thuộc ancestry, environment, measurement và population structure.

Điều này nhắc lại distinction giữa statistical prediction và biological mechanism.

## 14. Epigenetic inheritance: cần phân biệt cell memory và transgenerational inheritance

Trong mitosis, epigenetic state có thể được maintain qua daughter cell — đây là cellular memory rất phổ biến.

Nhưng claim rằng acquired epigenetic mark thường xuyên truyền qua nhiều human generation cần thận trọng hơn, vì germline và early embryo trải qua extensive epigenetic reprogramming.

Một số exception tồn tại, nhưng không nên biến epigenetics thành “Lamarckism hiện đại”.

## 15. Development: genome giống nhau, state khác nhau

During development, signal làm transcription factor activate/inhibit gene network. Những network tạo stable cell state.

Một stem cell có thể differentiate vì regulatory network chuyển sang attractor/state mới.

Chromatin change giúp stabilize state đó.

Do đó development là sequence of regulatory transitions, không phải genome thay đổi ở mỗi tissue.

## 16. Cancer như genomic + regulatory evolution

Cancer cell tích lũy mutation, copy-number change và epigenetic alteration. Clone có growth advantage expand.

Tumor vì thế vừa là genomic disorder vừa là evolutionary system trong tissue.

Điều này nối genomics trực tiếp với chapter evolution kế tiếp.

## 17. Từ genome cá thể sang population

Khi sequencing nhiều cá thể, ta không chỉ thấy variant của một người mà có thể đo **allele frequency** trong population.

Tần số này thay đổi qua mutation, selection, drift và migration.

Vì vậy genomics tự nhiên dẫn tới population genetics.

Ta đang chuyển scale:

```text
DNA sequence in one cell
       ↓
variant in one organism
       ↓
allele frequency in population
       ↓
change across generations
       ↓
evolution
```

Tiếp tục với [[../03_evolution_and_diversity/00_evolution_and_population_genetics]].