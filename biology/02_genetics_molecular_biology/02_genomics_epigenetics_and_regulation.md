# Genomics, Epigenetics và Điều hòa hệ gene — Genomics, Epigenetics and Regulation (유전체학, 후성유전학과 조절)

Hai chapter trước đi từ DNA sequence tới protein rồi sang inheritance. Bây giờ ta zoom out. Một cell không vận hành bằng một gene riêng lẻ mà bằng **toàn bộ genome và regulatory network**. Hàng nghìn gene có thể thay expression cùng lúc; chromatin quyết định vùng nào accessible; environmental signal đổi transcriptional program; population chứa hàng triệu variant.

Chapter này trả lời câu hỏi: **làm thế nào genome lớn được tổ chức, điều hòa và đo lường ở quy mô toàn hệ?**

> **Mental model:** genomics không phải “genetics nhưng nhiều gene hơn”. Nó thay đổi đơn vị tư duy từ locus riêng lẻ sang pattern toàn genome, network và statistical signal trong dữ liệu lớn.

## 1. Genome không chỉ là danh sách gene

Eukaryotic genome gồm coding gene, noncoding RNA gene, promoter, enhancer, repeat, centromere, telomere và nhiều region có function/regulatory history khác nhau.

Protein-coding sequence chỉ chiếm một phần nhỏ genome human. Nhưng không nên nhảy từ đó tới kết luận “mọi noncoding DNA đều functional”. Một phần có regulatory role, một phần structural/repetitive, một phần có thể gần neutral.

Genomics phải phân biệt **sequence tồn tại** với **sequence có selected biological function**.

## 2. Chromatin tạo layer organization đầu tiên

DNA eukaryote quấn quanh histone tạo nucleosome. Nucleosome tiếp tục organize thành higher-order chromatin.

DNA packaging giải hai bài toán tưởng mâu thuẫn:

- compact genome rất dài vào nucleus;
- vẫn cho replication/transcription/repair machinery truy cập đúng nơi.

Vì vậy chromatin không phải packaging thụ động. Nó là regulatory substrate.

## 3. Euchromatin và heterochromatin là spectrum, không phải hai hộp tuyệt đối

**Euchromatin** thường accessible/transcriptionally active hơn; **heterochromatin** compact hơn và thường ít active.

Nhưng chromatin state phụ thuộc locus, cell type và time. Một region có thể đổi accessibility khi differentiation hoặc signaling.

Genome giống library mà mỗi cell type mở một subset shelf khác nhau.

## 4. Histone modification: “code” nhưng không phải dictionary đơn giản

Histone tail có thể acetylated, methylated, phosphorylated và nhiều modification khác.

Histone acetylation thường liên hệ chromatin accessible hơn vì giảm positive charge/thu hút reader protein, nhưng causal effect phụ thuộc context.

Histone methylation đặc biệt không có nghĩa “methylation = repression”; vị trí residue quyết định association. H3K4me3 thường liên hệ active promoter, H3K27me3 thường repression trong context eukaryote.

Không nên học epigenetics như bảng “mark này bật, mark kia tắt” mà phải hiểu mark nằm trong network writer–reader–eraser.

## 5. DNA methylation

Ở mammals, DNA methylation thường xảy ra tại cytosine trong CpG context. Promoter CpG methylation có thể liên hệ transcriptional repression, nhưng genome-wide interpretation phức tạp hơn.

Methylation pattern có thể được copy tương đối qua cell division, tạo một phần cellular memory.

Nhưng methylation cũng dynamic trong development, germline và disease.

## 6. Epigenetics chính xác là gì?

Thuật ngữ **epigenetics** thường bị dùng quá rộng. Một definition hữu ích là study of heritable/stable change in gene regulation or chromatin state không yêu cầu change DNA sequence.

Trong somatic cell, epigenetic memory giúp daughter cell giữ identity. Trong transgenerational inheritance, claim phải mạnh hơn: mark/effect phải vượt qua germline reprogramming và truyền qua generation.

Ở mammals, nhiều epigenetic mark bị reset mạnh trong gametogenesis/early embryo. Vì vậy câu “stress của bố mẹ chắc chắn truyền epigenetically cho cháu” cần evidence rất cẩn thận.

## 7. X-chromosome inactivation: epigenetic regulation ở chromosome scale

Ở female mammals, một X chromosome phần lớn bị inactivate để balance dosage với male XY.

Long noncoding RNA XIST và chromatin modification tham gia process. Inactivation xảy ra sớm trong development và được duy trì qua nhiều cell division.

Kết quả là female tissue có mosaic cell dùng X maternal hoặc paternal khác nhau.

Đây là ví dụ epigenetic state ổn định tạo phenotype mosaic mà DNA sequence không đổi.

## 8. Genomic imprinting: parent-of-origin effect

Một số gene biểu hiện khác nhau tùy allele đến từ bố hay mẹ do imprint mark được thiết lập trong germline.

Imprinting cho thấy hai allele cùng sequence không nhất thiết function equivalent nếu epigenetic history khác nhau.

Nhưng imprinting chỉ áp dụng subset gene; không phải rule chung của genome.

## 9. Enhancer và 3D genome

Enhancer có thể nằm rất xa promoter theo linear DNA nhưng ở gần trong 3D nucleus do chromatin folding.

Genome được organize thành loop/domain làm regulatory element gặp target gene.

Do đó distance “trên sequence” và distance “trong không gian nucleus” là hai khái niệm khác.

Structural variant phá boundary hoặc đưa enhancer gần gene khác có thể gây misregulation.

## 10. Alternative splicing mở rộng transcriptome

Một gene có thể tạo nhiều mRNA isoform bằng lựa chọn exon khác nhau. Splicing factor và cell state quyết định pattern.

Vì vậy số protein isoform có thể lớn hơn số protein-coding gene.

Tuy nhiên không phải mọi transcript isoform đều stable/functional; omics data cần validation.

## 11. RNA regulation sau transcription

mRNA stability, localization và translation efficiency được regulation bởi RNA-binding protein và miRNA.

**microRNA (miRNA / 마이크로RNA)** có thể base-pair target mRNA và giảm translation hoặc thúc degradation.

Regulation sau transcription cho phép cell phản ứng nhanh mà không cần thay transcription ngay lập tức.

## 12. Protein level cũng là một layer regulation

Transcript abundance không đồng nghĩa protein abundance. Translation rate, protein degradation, modification và localization đều ảnh hưởng function.

Ubiquitin–proteasome system đánh dấu nhiều protein để degradation.

Vì vậy RNA-seq chỉ quan sát một layer. Muốn hiểu phenotype cần tích hợp proteomics/metabolomics/functional assay.

## 13. “Omics” là gì?

Các domain omics đo nhiều component cùng lúc:

- genomics: DNA sequence/variation;
- transcriptomics: RNA;
- epigenomics: chromatin/DNA mark;
- proteomics: protein;
- metabolomics: metabolite.

Không nên nghĩ multi-omics đơn giản là “càng nhiều data càng tốt”. Mỗi layer có noise, batch effect và measurement bias riêng; integration cần model và biological question rõ.

## 14. Sequencing: đọc hàng triệu fragment rồi reconstruct picture

Modern short-read sequencing tạo rất nhiều fragment sequence. Bioinformatics phải quality-control, align vào reference hoặc assemble, rồi count/call variant.

Một read ngắn không tự cho biết nó đến từ gene nào nếu region repetitive. Mapping uncertainty là một limitation thực.

Long-read sequencing giúp resolve structural variant/repeat tốt hơn nhưng có trade-off về cost/error/platform.

Technology choice phụ thuộc question.

## 15. Reference genome không phải “genome chuẩn của loài”

Reference genome là một coordinate framework được xây từ sample/assembly. Nó không đại diện mọi allele trong population.

Pangenome approach cố biểu diễn diversity tốt hơn linear reference duy nhất.

Đây là ví dụ data representation ảnh hưởng biological inference.

## 16. Variant calling: sequence khác reference chưa chắc gây bệnh

Genomic variant có thể common/rare, coding/noncoding, neutral/deleterious/beneficial tùy context.

Classification pathogenicity cần population frequency, functional evidence, segregation, computational prediction và clinical data.

Không thể nhìn “có mutation” rồi kết luận disease. Mọi người đều mang rất nhiều variant.

## 17. GWAS: tìm association ở population scale

**Genome-wide association study (GWAS / 전장유전체 연관분석)** test association giữa variant và trait trên genome.

Vì test hàng triệu variant, multiple-testing correction rất nghiêm ngặt. Population structure cũng có thể gây confounding.

GWAS signal thường chỉ ra region liên quan trait, không tự chứng minh variant nào causal hoặc mechanism gì.

Association phải được follow bằng fine mapping, functional experiment và biological reasoning.

## 18. Linkage disequilibrium: variant đi cùng nhau làm inference khó hơn

Nearby allele có thể correlated trong population do shared ancestry/recombination history. Đây là **linkage disequilibrium, LD**.

Một SNP GWAS significant có thể chỉ là tag đi cùng causal variant.

Vì vậy statistical association và molecular causation là hai bước khác nhau.

## 19. Polygenic score

Nhiều complex trait chịu contribution từ rất nhiều variant effect nhỏ. **Polygenic score** cộng weighted allele effect từ GWAS.

Score có thể có predictive value trong population tương tự training data nhưng transfer giữa ancestry/population có thể giảm vì LD, allele frequency và environment khác.

Đây là limitation quan trọng khi đưa genomics vào medicine.

## 20. Single-cell genomics: trung bình có thể che mất cell type

Bulk RNA-seq đo average của hàng triệu cell. Nếu tissue gồm nhiều cell type, change composition có thể bị nhầm là expression change trong từng cell.

Single-cell RNA-seq tách profile từng cell (với sampling/noise limitation), cho phép identify cell type/state và trajectory.

Nhưng “cluster” trong data không tự động bằng biological cell type; annotation cần marker, context và validation.

## 21. Development như một bài toán regulatory state

Fertilized egg tạo rất nhiều cell type gần cùng genome. Difference đến từ regulatory network, chromatin state và signaling history.

Development có thể hình dung như system đi qua landscape state: signal activate transcription factor, factor mở/đóng regulatory program, cell commitment dần ổn định.

Đây là bridge sang development chapter.

## 22. Gene regulatory network

Một transcription factor có thể regulate nhiều gene; nhiều factor cùng control một gene; feedback tạo stable state.

Network motif như positive feedback có thể khóa cell identity. Negative feedback giới hạn signal. Feedforward loop có thể lọc transient input.

Molecular network và systems thinking gặp nhau trực tiếp ở đây.

## 23. Epigenetic memory và cell identity

Khi cell divide, daughter cell cần không chỉ copy DNA mà còn khôi phục chromatin state và transcriptional program.

Một phần information được duy trì qua histone modification, DNA methylation, transcription-factor network và spatial organization.

Cell identity vì vậy là **state của system**, không nằm trong một gene đơn độc.

## 24. Environmental response và plasticity

Environment có thể thay signaling, hormone và gene expression. Nutrition, stress, temperature hoặc toxin có thể tạo molecular response.

Nhưng “environment thay gene” nên nói chính xác: thường environment đổi **expression/regulatory state**, không đổi DNA sequence trừ khi gây mutation.

Phân biệt genetic variation với regulatory plasticity giúp tránh lẫn lộn.

## 25. CRISPR screen: từ edit một gene sang test hàng nghìn gene

CRISPR có thể dùng để knockout/perturb hàng nghìn gene trong population cell. Sequencing barcode/guide abundance giúp tìm gene ảnh hưởng survival hoặc phenotype.

Đây là genomics theo hướng causal: không chỉ quan sát association mà perturb system.

Kết hợp high-throughput perturbation với single-cell readout đang cho phép map regulatory network sâu hơn.

## 26. Systems biology: từ list component sang model interaction

Khi data quá nhiều, mục tiêu không còn là catalog. **Systems biology (시스템생물학)** xây model network và dynamics.

Ví dụ metabolic network có node là metabolite/reaction, gene regulatory network có node gene/protein, edge biểu diễn interaction.

Graph theory, differential equation và statistical inference trở thành công cụ sinh học.

Xem thêm [[../90_connections/00_biology_math_computation_and_scale]].

## 27. Case study: cùng genome, neuron và liver cell khác nhau thế nào?

Neuron và hepatocyte có gần cùng DNA sequence. Nhưng chromatin accessibility khác, transcription factor khác, enhancer active khác, RNA/protein profile khác.

Liver cell expression enzyme metabolism/detoxification; neuron expression ion channel, synaptic protein.

Difference phenotype không cần genome khác. Nó cần regulatory state khác.

## 28. Case study: variant regulatory có thể mạnh như coding variant

Nếu variant nằm enhancer và làm transcription factor bind yếu hơn, gene target có thể expression thấp trong tissue/time cụ thể.

Protein sequence hoàn toàn bình thường nhưng amount/timing sai vẫn tạo phenotype.

Genetics hiện đại vì vậy phải nhìn cả coding lẫn regulatory genome.

## 29. Common misconceptions

“Epigenetic = bất kỳ thứ gì không phải DNA sequence” quá rộng.

“Methylation luôn tắt gene” sai.

“RNA level nói chính xác protein level” sai.

“GWAS variant là nguyên nhân” chưa chắc.

“Reference genome là genome bình thường duy nhất” sai.

“Single-cell data trực tiếp cho cell type thật” sai; clustering là model cần interpretation.

## 30. Bridge: genome variation trở thành evolution như thế nào?

Genomics cho ta picture variation trên nhiều locus và regulatory state. Nhưng evolution hỏi một level khác: **tần số allele thay đổi qua generation bởi mutation, selection, drift và gene flow như thế nào?**

Đó là nội dung của [[../03_evolution_and_diversity/00_evolution_and_population_genetics]].

Phylogeny sau đó dùng sequence difference để reconstruct history; microbiology dùng horizontal gene transfer và rapid evolution; bioinformatics quay lại dùng computational algorithm để xử lý genomic data.

> **Mental model cuối chapter:** genome là một dynamic information system được tổ chức trong chromatin, đọc qua regulatory network và biểu hiện thành nhiều molecular layer. Genomics đo system ở quy mô lớn; statistics giúp tìm pattern, còn experiment mới giúp nối pattern với causation.