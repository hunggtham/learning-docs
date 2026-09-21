# Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)

Chapter trước giải thích DNA lưu information và biểu hiện gen (gene expression) biến sequence thành function. Nhưng heredity chỉ thật sự trở thành vấn đề khi organism tạo offspring: **allele nào được truyền, chromosome phân ly ra sao, recombination tạo combination mới thế nào, và vì sao offspring vừa giống vừa khác parent?**

Đây là nơi molecular genetics gặp meiosis, probability và population thinking.

> **Mô hình tư duy (mental model):** inheritance không phải “trait đi nguyên vẹn từ parent sang child”. Cái được truyền là vật chất di truyền (genetic material); phenotype xuất hiện sau khi allele tương tác với nhau, với mạng lưới điều hòa (regulatory network) và với environment.

## 1. Alen (allele), genotype và kiểu hình (phenotype)

Một **alen (alen / 대립유전자)** là một version của locus/gen (gene). **Kiểu gen (genotype) (kiểu gene / 유전자형)** mô tả allele composition; **kiểu hình (kiểu hình / 표현형)** là trait quan sát/đo được.

Genotype không đồng nghĩa phenotype. Cùng genotype có thể cho phenotype khác do môi trường (environment), development và stochastic factor. Ngược lại, phenotype tương tự có thể đến từ nhiều genotype khác nhau.

## 2. Diploid organism và nhiễm sắc thể tương đồng (homologous chromosome)

Human somatic cell điển hình là diploid: có hai set chromosome, một từ mẹ và một từ cha.

Hai chromosome tương ứng gọi là **các nhiễm sắc thể tương đồng (homologous chromosomes)**. Chúng mang cùng loại locus theo cùng order gần tương ứng nhưng có thể chứa allele khác nhau.

Nhiễm sắc tử chị em (sister chromatid) thì khác: đó là hai copy của cùng chromosome sau DNA replication.

Phân biệt homolog với nhiễm sắc tử chị em là điều bắt buộc để hiểu meiosis.

## 3. Meiosis tạo gamete haploid

Meiosis giảm số lượng nhiễm sắc thể (chromosome number) từ diploid xuống haploid để khi fertilization kết hợp hai gamete, diploid number được phục hồi.

Meiosis I tách nhiễm sắc thể tương đồng; meiosis II tách nhiễm sắc tử chị em.

Nếu không có reduction division, số lượng nhiễm sắc thể sẽ double mỗi generation.

Meiosis vì vậy là lời giải structural cho sinh sản hữu tính (sexual reproduction).

## 4. Phân ly độc lập (independent assortment): variation xuất hiện từ cách chromosome xếp ngẫu nhiên

Mỗi homologous pair có orientation tương đối độc lập ở metaphase I. Vì vậy maternal/paternal chromosome combination trong gamete thay đổi.

Nếu có \(n\) chromosome pair và bỏ qua tái tổ hợp (recombination), số combination từ phân ly độc lập là khoảng:

\[
2^n
\]

Ở humans với 23 pair, con số đã hơn tám triệu combination trước khi tính trao đổi chéo (crossing-over).

Sinh sản hữu tính tạo variation khổng lồ từ mechanics của meiosis.

## 5. Trao đổi chéo: homolog không chỉ chia ngẫu nhiên, chúng còn trao đổi đoạn

Trong prophase I, nhiễm sắc thể tương đồng pair và non-nhiễm sắc tử chị em có thể recombine.

**Trao đổi chéo (교차)** tạo chromosome mosaic chứa segment từ maternal/paternal homolog.

Recombination vừa tăng variation vừa có vai trò giúp homolog segregation đúng qua chiasma.

Distance giữa loci ảnh hưởng probability tái tổ hợp, tạo cơ sở genetic mapping.

## 6. Mendel: từ mẫu hình (pattern) phenotype suy ra unit inheritance

Mendel nghiên cứu pea trước khi biết DNA/nhiễm sắc thể (chromosome). Từ ratio offspring, ông suy ra trait được truyền qua discrete factor.

Ngày nay ta nối model Mendel với chromosome hành vi (behavior).

**Law of segregation** phản ánh hai alen ở diploid individual được phân ly vào gamete qua meiosis.

**Phân ly độc lập** đúng xấp xỉ cho gene trên chromosome khác nhau hoặc đủ xa nhau; linked gene là limitation quan trọng.

## 7. Dominant và recessive không có nghĩa “mạnh” và “yếu”

Nếu heterozygote phenotype giống một homozygote, allele thể hiện được gọi **dominant** trong context trait đó; allele kia **recessive**.

Dominance là mối quan hệ (relationship) kiểu hình giữa allele, không phải property đạo đức hay evolutionary superiority.

Một recessive allele vẫn có thể phổ biến. Một dominant disease allele vẫn có thể rare.

## 8. Molecular basis của dominance

Nhiều recessive loss-of-chức năng (function) allele xảy ra vì một functional copy tạo đủ protein (protein) cho phenotype bình thường; đây là **haplosufficiency**.

Trong trường hợp khác, một copy không đủ (**haploinsufficiency**) hoặc mutant protein interfere với normal protein (**dominant negative**), làm inheritance dominant.

Mendelian label có molecular mechanism phía sau.

## 9. Punnett square là probability tool, không phải machine dự đoán family cụ thể

Cross Aa × Aa cho kiểu gen xác suất (probability):

\[
P(AA)=1/4,\quad P(Aa)=1/2,\quad P(aa)=1/4
\]

Nếu complete dominance, phenotype ratio expected 3:1.

Nhưng mỗi child là event mới; bốn child không bắt buộc có đúng ba dominant và một recessive phenotype.

Expected ratio xuất hiện khi mẫu (sample) đủ lớn.

## 10. Product rule và sum rule

Nếu hai independent event cùng xảy ra:

\[
P(A\cap B)=P(A)P(B)
\]

Nếu hỏi một trong các mutually exclusive outcome:

\[
P(A\cup B)=P(A)+P(B)
\]

Xác suất (probability) giúp giải genetic cross phức tạp mà không cần vẽ Punnett square khổng lồ.

Math ở đây mô tả uncertainty của gamete combination.

## 11. Test cross và suy luận (inference) kiểu gen

Nếu individual có dominant phenotype nhưng genotype có thể AA hoặc Aa, crossing với homozygous recessive có thể cung cấp evidence.

Nếu offspring recessive xuất hiện, parent dominant phải mang recessive allele.

Đây là ví dụ scientific inference: phenotype offspring cung cấp data để suy genotype không quan sát trực tiếp.

## 12. Trội không hoàn toàn (incomplete dominance) và đồng trội (codominance)

Không phải mọi locus theo complete dominance.

Trong **trội không hoàn toàn**, heterozygote có phenotype intermediate. Trong **đồng trội**, hai allele product đều thể hiện rõ.

ABO blood group là ví dụ đồng trội giữa IA và IB, đồng thời cả hai dominant so với i theo kiểu hình kháng nguyên (antigen).

Một locus có thể có **multiple alleles** trong population dù mỗi diploid individual chỉ mang tối đa hai alen ở locus đó.

## 13. Pleiotropy và polygenic trait

**Pleiotropy**: một gene ảnh hưởng nhiều trait vì protein tham gia process chung hoặc nhiều tissue.

**Polygenic trait**: nhiều gene đóng góp một trait. Height, skin pigmentation và nhiều tính trạng định lượng (quantitative trait) thuộc kiểu này.

Điều này phá mô hình (model) “một gene — một trait” vốn chỉ hữu ích trong một số case đơn giản.

## 14. Epistasis: gene tương tác gene

Trong **epistasis (상위성)**, effect của allele ở một locus phụ thuộc genotype ở locus khác.

Ví dụ pathway pigment có enzyme A tạo precursor và enzyme B chuyển precursor thành pigment. Nếu A mất function, B có version nào cũng không tạo pigment.

Phenotype là output của pathway, không phải tổng độc lập của từng gene.

## 15. Linkage: gene gần nhau không assort hoàn toàn độc lập

Gene trên cùng chromosome có tendency đi cùng nhau. Recombination có thể tách chúng.

Tái tổ hợp frequency tăng theo genetic distance ở khoảng phù hợp. 1% tái tổ hợp được dùng định nghĩa khoảng 1 centimorgan trong mapping cổ điển.

Nhưng frequency không tăng tuyến tính vô hạn; multiple crossover làm mapping dài cần model correction.

## 16. Sex-linked inheritance

Gene trên sex chromosome tạo mẫu hình inheritance khác autosomal gene.

Ở X-linked recessive trait, male XY chỉ có một X nên allele recessive trên X có thể biểu hiện ngay nếu không có copy tương ứng trên Y.

Nhưng sex determination và sex-linked biology đa dạng giữa species; không nên lấy human XY làm universal model.

## 17. Mutation tạo allele mới

Recombination chỉ shuffle variation sẵn có; **đột biến (mutation)** tạo trình tự (sequence) variation mới.

Point mutation có thể là transition/transversion; insertion/deletion có thể gây frameshift nếu nằm coding region và length không chia hết cho 3.

Large-scale variant gồm duplication, deletion, inversion, translocation và copy-number variation.

Effect phụ thuộc locus, regulatory context và môi trường.

## 18. Germline và đột biến soma (somatic mutation)

**Đột biến dòng mầm (germline mutation)** có thể truyền cho offspring nếu nằm lineage tạo gamete.

**Đột biến soma** xảy ra trong body cell và thường không truyền qua reproduction, nhưng có thể ảnh hưởng clone cell — rất quan trọng trong cancer.

Một human body vì vậy không hoàn toàn genetic-uniform; mosaicism có thể xuất hiện.

## 19. Tốc độ đột biến (mutation rate) và selection không phải cùng thứ

Mutation xuất hiện không vì sinh vật (organism) “cần” thích nghi (adaptation). Mutation source có bias nhưng không được tạo ra có định hướng phù hợp future fitness theo cách Lamarck đơn giản.

Selection acts **sau khi variation tồn tại** bằng differential reproduction/survival.

Phân biệt source variation với filter variation là nền của evolution.

## 20. Chromosome không phân ly (nondisjunction)

Nếu homolog hoặc nhiễm sắc tử chị em không phân ly đúng, gamete có số lượng nhiễm sắc thể bất thường.

Sau fertilization có thể tạo **aneuploidy**.

Effect thường lớn vì dosage của hàng trăm gene thay đổi cùng lúc.

Age-related change trong meiosis có thể ảnh hưởng risk ở một số aneuploidy, nhưng mechanism phức tạp hơn một nguyên nhân đơn.

## 21. Quantitative genetics: trait liên tục được phân tích thế nào?

Nhiều trait tạo distribution liên tục vì nhiều locus + môi trường.

Ta có thể phân rã phenotypic variance khái niệm:

\[
V_P=V_G+V_E+V_{G\times E}+...
\]

Trong đó genetic variance, environmental variance và gen–environment interaction cùng đóng góp.

Đây là mô hình thống kê (statistical model) ở population level, không phải decomposition cố định của một individual.

## 22. Heritability: một khái niệm rất dễ hiểu sai

**Heritability (유전력)** là phần variance phenotype trong một population/môi trường được liên hệ với genetic variance theo model cụ thể.

Heritability cao không có nghĩa trait “không đổi được bởi environment”. Height có heritability cao trong một population nhưng nutrition vẫn ảnh hưởng growth.

Heritability cũng không nói “X% trait của một người do gen”. Nó là property của population variance, không phải individual causal percentage.

## 23. Gen–environment interaction

Cùng genotype có thể phản ứng khác nhau trong environment khác. **Reaction norm** mô tả phenotype của genotype qua phạm vi (range) môi trường.

Ví dụ chất dinh dưỡng (nutrient), temperature hoặc stress có thể thay effect allele.

Nature và nurture không phải hai hộp cộng độc lập; chúng tương tác.

## 24. Độ thấm (penetrance) và mức biểu hiện (expressivity)

**Độ thấm** mô tả fraction individual mang genotype và biểu hiện phenotype xác định.

**Mức biểu hiện** mô tả mức độ phenotype khác nhau giữa người có cùng genotype.

Incomplete độ thấm có thể đến từ modifier gene, môi trường, age hoặc stochastic factor.

Điều này làm pedigree thực tế phức tạp hơn Punnett square đơn giản.

## 25. Pedigree: suy inheritance từ family pattern

Pedigree dùng symbol để biểu diễn relationship và kiểu hình qua generation.

Ta suy autosomal dominant/recessive, X-linked hoặc mitochondrial pattern dựa trên transmission, nhưng cần cẩn trọng vì small family, incomplete độ thấm và new mutation có thể làm pattern mơ hồ.

Pedigree là inference under uncertainty, không phải nhìn một hình rồi “đoán chắc”.

## 26. Di truyền ty thể (mitochondrial inheritance)

Mitochondrial DNA ở human thường được truyền chủ yếu từ mẹ vì mitochondria của egg đóng góp phần lớn organelle cho embryo.

Tuy nhiên phenotype mitochondrial disease còn phụ thuộc heteroplasmy và ngưỡng (threshold) ở mô (tissue).

Non-Mendelian inheritance nhắc ta rằng Mendel là nền, không phải toàn bộ di truyền học (genetics).

## 27. Biến dị di truyền (genetic variation) ở quy mô quần thể (population scale)

Ở một individual ta nói genotype. Ở quần thể (population) ta quan tâm **tần số alen (allele frequency)** và **tần số kiểu gen (genotype frequency)**.

Đây là bước chuyển cực kỳ quan trọng. Evolution không phải “một individual đổi gene để thích nghi”; nó là change distribution variation trong quần thể qua generation.

Mọi mutation, meiosis, recombination học trong chapter này trở thành input cho di truyền học quần thể (population genetics).

## 28. Tình huống phân tích (case study): lactose persistence

Khả năng tiêu hóa lactose ở adulthood liên quan regulation của lactase gene và population history.

Ở một số population có tradition chăn nuôi/sữa, regulatory variant liên quan lactase persistence tăng frequency qua chọn lọc (selection).

Trait cho thấy connection:

```text
regulatory DNA variant
→ gene expression after childhood
→ digestive phenotype
→ cultural/environment context
→ differential fitness historically
→ allele-frequency change
```

Gen–culture đồng tiến hóa (coevolution) nối molecular genetics, inheritance và tiến hóa (evolution).

## 29. Tình huống phân tích: kháng kháng sinh (antibiotic resistance) không phải bacteria “cố biến đổi”

Trong bacterial population có biến dị (variation) do đột biến/chuyển gen ngang (horizontal gene transfer). Antibiotic giết susceptible cell mạnh hơn. Resistant variant survive/reproduce, làm resistance allele tăng frequency.

Selection thay composition population; antibiotic không “dạy” từng bacterium cách resistance theo nghĩa có mục tiêu.

Đây là bridge sang evolution và microbiology.

## 30. Các hiểu lầm phổ biến (common misconceptions)

“Dominant allele phổ biến hơn recessive allele” sai.

“Recessive nghĩa yếu” sai.

“50% risk nghĩa hai child chắc chắn một affected” sai.

“Heritability cao nghĩa environment không quan trọng” sai.

“Mutation xảy ra để thích nghi” sai.

“Gene và trait có mapping một-một” hiếm khi đúng cho trait phức tạp.

<!-- depth-audit-2026:genotype-phenotype-map -->
## Từ genotype đến phenotype: bản đồ không tuyến tính

Một allele không “chứa sẵn” phenotype. Sequence thay đổi trước hết tác động một RNA, protein, mức biểu hiện hoặc regulatory interaction; thay đổi đó đi qua mạng phát triển và physiology rồi mới thành trait đo được. Do đó cùng một mutation có thể có effect khác nhau theo tissue, age, environment hoặc genetic background.

**Độ thâm nhập (penetrance)** hỏi bao nhiêu người mang genotype biểu hiện phenotype; **độ biểu hiện (expressivity)** hỏi mức độ phenotype mạnh đến đâu. Epistasis xuất hiện khi effect của allele ở locus A phụ thuộc allele tại locus B. Đây là lý do Punnett square đúng về segregation nhưng không đủ để mô tả nhiều trait thực.

Mutation cũng có phân bố effect rất lệch. Nhiều mutation gần neutral, một số có hại rõ, số có lợi trong một environment cụ thể thường nhỏ hơn. Structural variant, copy-number change và regulatory variant có thể ảnh hưởng phenotype mạnh dù không đổi coding sequence theo cách “một base → một amino acid”.

Với quantitative trait, phương sai phenotype là kết quả của nhiều locus, environment và tương tác. Heritability cao trong một population không có nghĩa trait “không đổi được”; nó chỉ mô tả nguồn variation dưới environment và population đang xét. Đây là bridge quan trọng từ inheritance sang population genetics và tránh biến statistics thành định mệnh sinh học.

<!-- continuity-2026:meiosis-linkage -->
## Từ cơ chế meiosis tới xác suất di truyền và bản đồ liên kết

Quy luật phân ly của Mendel xuất hiện từ hành vi vật lý của chromosome: hai homolog mang các allele tương ứng bắt cặp rồi phân ly ở meiosis I; sister chromatid phân ly ở meiosis II. Khi hai locus nằm trên chromosome khác nhau, orientation của các cặp homolog tạo cơ sở cho phân ly độc lập. Khi hai locus nằm gần nhau trên cùng chromosome, chúng không còn độc lập vì được truyền cùng một đoạn DNA.

Trao đổi chéo (crossing-over) tạo recombinant chromosome. Tần số recombinant tăng khi hai locus xa nhau hơn, nhưng không thể dùng tuyến tính vô hạn vì nhiều crossover có thể che lẫn nhau; ở khoảng cách lớn, recombination fraction tiến gần 0,5 và hai locus trông gần như không liên kết. Đây là lý do bản đồ di truyền là model xác suất của meiosis, không phải thước đo vật lý hoàn hảo.

Failure ở meiosis cũng cho thấy cấu trúc tạo chức năng như thế nào. Nondisjunction làm chromosome không phân ly đúng, tạo giao tử thừa hoặc thiếu chromosome. Cơ thể có checkpoint và cơ chế cohesion để giảm lỗi, nhưng selection không thể làm lỗi về zero tuyệt đối vì replication, recombination và segregation đều có chi phí và giới hạn vật lý.

## 31. Cầu nối (bridge): từ family inheritance sang genome và quần thể

Chapter này đi từ meiosis đến allele transmission và biến dị. Nhưng modern genetics còn hỏi ở scale lớn hơn: hàng triệu variant trong hệ gen (genome) được tổ chức thế nào? Chromatin làm gene accessible ra sao? GWAS tìm association bằng cách nào? Transcriptomics đo expression của hàng nghìn gene ra sao?

[Genomics, Epigenetics và Điều hòa hệ gene](02_genomics_epigenetics_and_regulation.md) sẽ mở rộng sang genome-wide regulation và omics.

Sau đó [Tiến hóa và Di truyền quần thể](../03_evolution_and_diversity/00_evolution_and_population_genetics.md) sẽ lấy chính tần số alen, đột biến, recombination và mức thích nghi sinh sản (fitness) để xây theory evolution.

> **Mô hình tư duy cuối chapter:** heredity là quá trình chromosome/DNA được phân phối qua meiosis và fertilization; variation phát sinh từ đột biến + tái tổ hợp + assortment; phenotype là outcome của genotype trong bối cảnh (context). Khi ta chuyển từ một family sang cả quần thể, chính variation này trở thành dữ liệu cho tiến hóa.

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← DNA, Gene và Biểu hiện gene](00_dna_genes_and_gene_expression.md) · [Mục lục Biology](../README.md) · [Genomics, Epigenetics và Điều hòa hệ gene →](02_genomics_epigenetics_and_regulation.md)
