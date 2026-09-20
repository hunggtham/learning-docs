# DNA, gene và biểu hiện gene — DNA, Genes and Gene Expression (DNA, 유전자와 유전자 발현)

Cell signaling cho thấy một response dài hạn thường cần thay đổi protein mà cell sản xuất. Điều đó dẫn tới câu hỏi trung tâm của molecular genetics: **cell lưu thông tin để tạo protein ở đâu, copy thông tin đó ra sao, và đọc nó như thế nào?**

Câu trả lời thường được nén thành “DNA → RNA → protein”, nhưng nếu chỉ thuộc mũi tên này ta sẽ bỏ lỡ gần như toàn bộ reasoning. Chương này xây từng bước: vì sao DNA phù hợp để lưu information, replication giải bài toán copy như thế nào, transcription và translation biến sequence thành function ra sao, và regulation quyết định gene nào được dùng.

## 1. Information trong biology là gì?

Khi nói DNA “chứa thông tin”, ta không có nghĩa DNA hiểu ý nghĩa như con người. Information nằm trong **sequence** các base.

Một DNA molecule có sugar-phosphate backbone tương đối lặp lại, trong khi order của A, T, G, C thay đổi. Chính phần có thể thay đổi này mang information.

Nếu protein sequence cần một order amino acid nhất định để fold và function, cell cần một mapping từ nucleotide sequence sang amino-acid sequence. Genetic system giải bài toán đó bằng genetic code.

## 2. DNA double helix: structure phục vụ copying

DNA gồm hai strand chạy antiparallel. Base pair theo rule A–T và G–C.

Complementarity không chỉ làm helix ổn định; nó tạo **template logic**. Nếu biết sequence một strand, về principle có thể suy ra strand còn lại.

Ví dụ:

```text
5' - A T G C C A - 3'
3' - T A C G G T - 5'
```

Vì vậy double-stranded DNA vừa lưu information vừa có built-in redundancy để copy và repair.

> **Mental model:** DNA không giống một cuộn băng chỉ đọc. Hai strand bổ sung nhau khiến mỗi strand có thể giúp reconstruct strand kia.

## 3. Gene không phải lúc nào cũng là “một đoạn DNA tạo một protein”

**Gene (유전자)** là một unit genomic có sản phẩm functional, thường là RNA hoặc protein thông qua RNA intermediate.

Cách nói “one gene–one protein” quá đơn giản. Một gene có thể tạo nhiều transcript qua alternative splicing; một số gene tạo RNA không được translate; protein có thể được modified sau translation.

Do đó relationship thực tế gần hơn với:

```text
genomic region
   ↓ regulated transcription
RNA transcript(s)
   ↓ processing / translation
protein isoform(s) or functional RNA
   ↓
cellular effect
```

## 4. Chromosome: vấn đề packing và organization

Genome eukaryote dài hơn kích thước nucleus rất nhiều. DNA phải được package.

DNA quấn quanh histone tạo nucleosome; nucleosome tổ chức thành chromatin. Packing không chỉ để tiết kiệm không gian. Mức chromatin accessibility ảnh hưởng transcription.

Do đó physical organization của DNA trở thành một layer regulation.

Ta sẽ quay lại sâu hơn ở [[02_genomics_epigenetics_and_regulation]].

## 5. Replication: copy một polymer dài mà vẫn giữ độ chính xác

Trước cell division, genome phải được copy.

DNA replication là **semiconservative**: mỗi daughter DNA có một old strand và một new strand.

Helicase mở double helix. Single-strand binding protein giữ strand tách. Primase tạo primer. DNA polymerase kéo dài chain mới.

Nhưng có một constraint hóa học: DNA polymerase thêm nucleotide vào đầu 3', nên synthesis luôn 5'→3'. Vì hai template antiparallel, một strand được tổng hợp liên tục, strand kia thành Okazaki fragments rồi được ligase nối.

Đây là ví dụ đẹp cho cách một constraint molecular tạo architecture của cả process.

## 6. Proofreading và repair: fidelity không đến từ một enzyme hoàn hảo

DNA polymerase có proofreading, nhưng error vẫn có thể xảy ra. Cell còn có mismatch repair và nhiều pathway repair damage.

Điểm quan trọng là genomic stability xuất hiện từ **nhiều layer error correction**.

Nếu error rate bằng zero tuyệt đối, evolution mất nguồn mutation. Nếu error rate quá cao, genome mất function. Life tồn tại trong một vùng cân bằng giữa fidelity và variation.

## 7. Từ DNA sang RNA: transcription

**Transcription (phiên mã / 전사)** dùng DNA làm template để tổng hợp RNA.

RNA polymerase bind promoter với sự hỗ trợ của transcription factor, mở local DNA và polymerize RNA.

Chỉ một strand làm template cho một transcript cụ thể.

RNA sequence tương ứng coding strand của DNA ngoại trừ U thay T.

Transcription là điểm control mạnh vì cell không cần produce mọi RNA cùng lúc.

## 8. RNA processing: eukaryote không dùng transcript thô ngay

Pre-mRNA thường được thêm 5' cap, poly-A tail và trải qua splicing.

**Intron** được loại, **exon** được nối.

Alternative splicing có thể nối exon theo pattern khác, cho một gene tạo nhiều RNA isoform.

Điều này làm relationship gene → protein trở thành network nhiều hơn một mũi tên 1:1.

## 9. Genetic code: từ alphabet 4 chữ sang alphabet 20 amino acid

Ribosome đọc mRNA theo nhóm ba nucleotide gọi là **codon (코돈)**.

Với 4 loại base và triplet, có \(4^3=64\) codon. Nhiều codon encode cùng amino acid, nên genetic code có redundancy.

Start codon thường AUG; stop codon báo kết thúc translation.

Điểm cần hiểu: genetic code là mapping convention được evolution giữ lại rất rộng, không phải property bắt buộc duy nhất của chemistry.

## 10. tRNA: adapter nối hai ngôn ngữ

tRNA giải bài toán: nucleotide codon không tự “gắn” amino acid đúng.

Một đầu tRNA có anticodon pair với mRNA codon; đầu khác mang amino acid.

Aminoacyl-tRNA synthetase là enzyme gắn đúng amino acid vào tRNA.

Nhờ vậy system chuyển từ information ở nucleotide space sang sequence ở amino-acid space.

## 11. Ribosome: machine biến information thành polymer

Ribosome gồm rRNA và protein. Nó giữ mRNA và tRNA đúng position, xúc tác peptide bond và di chuyển codon-by-codon.

Flow:

```text
mRNA codon
   ↓ recognized by
tRNA anticodon
   ↓ brings
amino acid
   ↓
ribosome builds
polypeptide
```

Sau translation, polypeptide phải fold và đôi khi được modified hoặc transported tới organelle phù hợp.

Do đó “protein được tạo” chưa phải cuối process; function cần đúng shape và location.

## 12. Central dogma: useful map nhưng không phải mọi luồng information

Central dogma thường viết:

```text
DNA → RNA → Protein
```

Đây là map cực hữu ích cho flow sequence information.

Nhưng có exception về route: retrovirus dùng reverse transcription RNA → DNA; RNA virus có thể copy RNA → RNA. Ngoài ra protein state và environment có thể ảnh hưởng gene expression mà không “viết ngược sequence protein thành DNA”.

Vì vậy central dogma không có nghĩa “DNA đơn phương quyết định mọi thứ”.

## 13. Gene expression regulation: genome giống nhau, cell type khác nhau

Neuron và liver cell có gần như cùng genome. Khác biệt chính nằm ở **gene expression program**.

Regulation có nhiều layer:

```text
chromatin accessibility
      ↓
transcription initiation
      ↓
RNA processing / stability
      ↓
translation
      ↓
protein modification / degradation
```

Mỗi layer cho system một điểm control khác nhau về speed, energy cost và reversibility.

## 14. Promoter, enhancer và transcription factor

Promoter là vùng gần transcription start site cần cho initiation.

**Enhancer** có thể nằm xa và bind transcription factor. DNA looping đưa regulatory protein tới transcription machinery.

Một gene có thể integrate nhiều signal vì enhancer chứa binding site cho nhiều factor.

Đây là nơi cell signaling nối trực tiếp tới gene expression: kinase pathway có thể activate transcription factor, transcription factor bind DNA và đổi RNA production.

## 15. Mutation: khi information thay đổi

**Mutation (đột biến / 돌연변이)** là thay đổi sequence DNA.

Point mutation có thể silent, missense hoặc nonsense tùy codon effect. Insertion/deletion có thể gây frameshift nếu không theo bội số ba.

Nhưng effect của mutation phụ thuộc context. Mutation ở regulatory region có thể đổi amount expression; mutation trong intron có thể không có effect hoặc ảnh hưởng splicing; mutation coding region có thể từ neutral đến severe.

Ta không thể suy phenotype chỉ từ label “mutation”. Cần trace mechanism.

## 16. Genotype → phenotype không phải đường thẳng

Một useful diagram:

```text
genotype
   ↓
gene expression
   ↓
protein / RNA function
   ↓
cellular state
   ↓
tissue / organism phenotype
   ↑
environment + development + stochastic effects
```

Environment có thể tác động ở nhiều điểm. Nutrition đổi metabolism; hormone đổi expression; temperature ảnh hưởng protein function.

Do đó phenotype là product của interaction giữa genotype và context.

## 17. Từ molecular information sang inheritance

Ta đã hiểu một genome được copy và expression. Nhưng sexual reproduction đặt thêm câu hỏi: organism diploid có hai chromosome set; khi tạo gamete phải phân phối thế nào? Vì sao trait có probability pattern như Mendel quan sát? Recombination tạo variation ra sao?

Đây là nơi molecular genetics phải nối sang chromosome behavior và probability.

Tiếp tục với [[01_inheritance_variation_and_mutation]].