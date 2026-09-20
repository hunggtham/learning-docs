# Di truyền, Biến dị và Đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)

Chapter trước giải thích DNA lưu information và gene expression biến sequence thành function. Nhưng heredity chỉ thật sự trở thành vấn đề khi organism tạo offspring: **allele nào được truyền, chromosome phân ly ra sao, recombination tạo combination mới thế nào, và vì sao offspring vừa giống vừa khác parent?**

Đây là nơi molecular genetics gặp meiosis, probability và population thinking.

> **Mental model:** inheritance không phải “trait đi nguyên vẹn từ parent sang child”. Cái được truyền là genetic material; phenotype xuất hiện sau khi allele tương tác với nhau, với regulatory network và với environment.

## 1. Allele, genotype và phenotype

Một **allele (alen / 대립유전자)** là một version của locus/gene. **Genotype (kiểu gene / 유전자형)** mô tả allele composition; **phenotype (kiểu hình / 표현형)** là trait quan sát/đo được.

Genotype không đồng nghĩa phenotype. Cùng genotype có thể cho phenotype khác do environment, development và stochastic factor. Ngược lại, phenotype tương tự có thể đến từ nhiều genotype khác nhau.

## 2. Diploid organism và homologous chromosome

Human somatic cell điển hình là diploid: có hai set chromosome, một từ mẹ và một từ cha.

Hai chromosome tương ứng gọi là **homologous chromosomes**. Chúng mang cùng loại locus theo cùng order gần tương ứng nhưng có thể chứa allele khác nhau.

Sister chromatid thì khác: đó là hai copy của cùng chromosome sau DNA replication.

Phân biệt homolog với sister chromatid là điều bắt buộc để hiểu meiosis.

## 3. Meiosis tạo gamete haploid

Meiosis giảm chromosome number từ diploid xuống haploid để khi fertilization kết hợp hai gamete, diploid number được phục hồi.

Meiosis I tách homologous chromosome; meiosis II tách sister chromatid.

Nếu không có reduction division, chromosome number sẽ double mỗi generation.

Meiosis vì vậy là lời giải structural cho sexual reproduction.

## 4. Independent assortment: variation xuất hiện từ cách chromosome xếp ngẫu nhiên

Mỗi homologous pair có orientation tương đối độc lập ở metaphase I. Vì vậy maternal/paternal chromosome combination trong gamete thay đổi.

Nếu có \(n\) chromosome pair và bỏ qua recombination, số combination từ independent assortment là khoảng:

\[
2^n
\]

Ở humans với 23 pair, con số đã hơn tám triệu combination trước khi tính crossing-over.

Sexual reproduction tạo variation khổng lồ từ mechanics của meiosis.

## 5. Crossing-over: homolog không chỉ chia ngẫu nhiên, chúng còn trao đổi đoạn

Trong prophase I, homologous chromosome pair và non-sister chromatid có thể recombine.

**Crossing-over (교차)** tạo chromosome mosaic chứa segment từ maternal/paternal homolog.

Recombination vừa tăng variation vừa có vai trò giúp homolog segregation đúng qua chiasma.

Distance giữa loci ảnh hưởng probability recombination, tạo cơ sở genetic mapping.

## 6. Mendel: từ pattern phenotype suy ra unit inheritance

Mendel nghiên cứu pea trước khi biết DNA/chromosome. Từ ratio offspring, ông suy ra trait được truyền qua discrete factor.

Ngày nay ta nối model Mendel với chromosome behavior.

**Law of segregation** phản ánh hai allele ở diploid individual được phân ly vào gamete qua meiosis.

**Independent assortment** đúng xấp xỉ cho gene trên chromosome khác nhau hoặc đủ xa nhau; linked gene là limitation quan trọng.

## 7. Dominant và recessive không có nghĩa “mạnh” và “yếu”

Nếu heterozygote phenotype giống một homozygote, allele thể hiện được gọi **dominant** trong context trait đó; allele kia **recessive**.

Dominance là relationship phenotype giữa allele, không phải property đạo đức hay evolutionary superiority.

Một recessive allele vẫn có thể phổ biến. Một dominant disease allele vẫn có thể rare.

## 8. Molecular basis của dominance

Nhiều recessive loss-of-function allele xảy ra vì một functional copy tạo đủ protein cho phenotype bình thường; đây là **haplosufficiency**.

Trong trường hợp khác, một copy không đủ (**haploinsufficiency**) hoặc mutant protein interfere với normal protein (**dominant negative**), làm inheritance dominant.

Mendelian label có molecular mechanism phía sau.

## 9. Punnett square là probability tool, không phải machine dự đoán family cụ thể

Cross Aa × Aa cho genotype probability:

\[
P(AA)=1/4,\quad P(Aa)=1/2,\quad P(aa)=1/4
\]

Nếu complete dominance, phenotype ratio expected 3:1.

Nhưng mỗi child là event mới; bốn child không bắt buộc có đúng ba dominant và một recessive phenotype.

Expected ratio xuất hiện khi sample đủ lớn.

## 10. Product rule và sum rule

Nếu hai independent event cùng xảy ra:

\[
P(A\cap B)=P(A)P(B)
\]

Nếu hỏi một trong các mutually exclusive outcome:

\[
P(A\cup B)=P(A)+P(B)
\]

Probability giúp giải genetic cross phức tạp mà không cần vẽ Punnett square khổng lồ.

Math ở đây mô tả uncertainty của gamete combination.

## 11. Test cross và inference genotype

Nếu individual có dominant phenotype nhưng genotype có thể AA hoặc Aa, crossing với homozygous recessive có thể cung cấp evidence.

Nếu offspring recessive xuất hiện, parent dominant phải mang recessive allele.

Đây là ví dụ scientific inference: phenotype offspring cung cấp data để suy genotype không quan sát trực tiếp.

## 12. Incomplete dominance và codominance

Không phải mọi locus theo complete dominance.

Trong **incomplete dominance**, heterozygote có phenotype intermediate. Trong **codominance**, hai allele product đều thể hiện rõ.

ABO blood group là ví dụ codominance giữa IA và IB, đồng thời cả hai dominant so với i theo phenotype antigen.

Một locus có thể có **multiple alleles** trong population dù mỗi diploid individual chỉ mang tối đa hai allele ở locus đó.

## 13. Pleiotropy và polygenic trait

**Pleiotropy**: một gene ảnh hưởng nhiều trait vì protein tham gia process chung hoặc nhiều tissue.

**Polygenic trait**: nhiều gene đóng góp một trait. Height, skin pigmentation và nhiều quantitative trait thuộc kiểu này.

Điều này phá model “một gene — một trait” vốn chỉ hữu ích trong một số case đơn giản.

## 14. Epistasis: gene tương tác gene

Trong **epistasis (상위성)**, effect của allele ở một locus phụ thuộc genotype ở locus khác.

Ví dụ pathway pigment có enzyme A tạo precursor và enzyme B chuyển precursor thành pigment. Nếu A mất function, B có version nào cũng không tạo pigment.

Phenotype là output của pathway, không phải tổng độc lập của từng gene.

## 15. Linkage: gene gần nhau không assort hoàn toàn độc lập

Gene trên cùng chromosome có tendency đi cùng nhau. Recombination có thể tách chúng.

Recombination frequency tăng theo genetic distance ở khoảng phù hợp. 1% recombination được dùng định nghĩa khoảng 1 centimorgan trong mapping cổ điển.

Nhưng frequency không tăng tuyến tính vô hạn; multiple crossover làm mapping dài cần model correction.

## 16. Sex-linked inheritance

Gene trên sex chromosome tạo pattern inheritance khác autosomal gene.

Ở X-linked recessive trait, male XY chỉ có một X nên allele recessive trên X có thể biểu hiện ngay nếu không có copy tương ứng trên Y.

Nhưng sex determination và sex-linked biology đa dạng giữa species; không nên lấy human XY làm universal model.

## 17. Mutation tạo allele mới

Recombination chỉ shuffle variation sẵn có; **mutation** tạo sequence variation mới.

Point mutation có thể là transition/transversion; insertion/deletion có thể gây frameshift nếu nằm coding region và length không chia hết cho 3.

Large-scale variant gồm duplication, deletion, inversion, translocation và copy-number variation.

Effect phụ thuộc locus, regulatory context và environment.

## 18. Germline và somatic mutation

**Germline mutation** có thể truyền cho offspring nếu nằm lineage tạo gamete.

**Somatic mutation** xảy ra trong body cell và thường không truyền qua reproduction, nhưng có thể ảnh hưởng clone cell — rất quan trọng trong cancer.

Một human body vì vậy không hoàn toàn genetic-uniform; mosaicism có thể xuất hiện.

## 19. Mutation rate và selection không phải cùng thứ

Mutation xuất hiện không vì organism “cần” adaptation. Mutation source có bias nhưng không được tạo ra có định hướng phù hợp future fitness theo cách Lamarck đơn giản.

Selection acts **sau khi variation tồn tại** bằng differential reproduction/survival.

Phân biệt source variation với filter variation là nền của evolution.

## 20. Chromosome nondisjunction

Nếu homolog hoặc sister chromatid không phân ly đúng, gamete có chromosome number bất thường.

Sau fertilization có thể tạo **aneuploidy**.

Effect thường lớn vì dosage của hàng trăm gene thay đổi cùng lúc.

Age-related change trong meiosis có thể ảnh hưởng risk ở một số aneuploidy, nhưng mechanism phức tạp hơn một nguyên nhân đơn.

## 21. Quantitative genetics: trait liên tục được phân tích thế nào?

Nhiều trait tạo distribution liên tục vì nhiều locus + environment.

Ta có thể phân rã phenotypic variance khái niệm:

\[
V_P=V_G+V_E+V_{G\times E}+...
\]

Trong đó genetic variance, environmental variance và gene–environment interaction cùng đóng góp.

Đây là statistical model ở population level, không phải decomposition cố định của một individual.

## 22. Heritability: một khái niệm rất dễ hiểu sai

**Heritability (유전력)** là phần variance phenotype trong một population/environment được liên hệ với genetic variance theo model cụ thể.

Heritability cao không có nghĩa trait “không đổi được bởi environment”. Height có heritability cao trong một population nhưng nutrition vẫn ảnh hưởng growth.

Heritability cũng không nói “X% trait của một người do gene”. Nó là property của population variance, không phải individual causal percentage.

## 23. Gene–environment interaction

Cùng genotype có thể phản ứng khác nhau trong environment khác. **Reaction norm** mô tả phenotype của genotype qua range environment.

Ví dụ nutrient, temperature hoặc stress có thể thay effect allele.

Nature và nurture không phải hai hộp cộng độc lập; chúng tương tác.

## 24. Penetrance và expressivity

**Penetrance** mô tả fraction individual mang genotype và biểu hiện phenotype xác định.

**Expressivity** mô tả mức độ phenotype khác nhau giữa người có cùng genotype.

Incomplete penetrance có thể đến từ modifier gene, environment, age hoặc stochastic factor.

Điều này làm pedigree thực tế phức tạp hơn Punnett square đơn giản.

## 25. Pedigree: suy inheritance từ family pattern

Pedigree dùng symbol để biểu diễn relationship và phenotype qua generation.

Ta suy autosomal dominant/recessive, X-linked hoặc mitochondrial pattern dựa trên transmission, nhưng cần cẩn trọng vì small family, incomplete penetrance và new mutation có thể làm pattern mơ hồ.

Pedigree là inference under uncertainty, không phải nhìn một hình rồi “đoán chắc”.

## 26. Mitochondrial inheritance

Mitochondrial DNA ở human thường được truyền chủ yếu từ mẹ vì mitochondria của egg đóng góp phần lớn organelle cho embryo.

Tuy nhiên phenotype mitochondrial disease còn phụ thuộc heteroplasmy và threshold ở tissue.

Non-Mendelian inheritance nhắc ta rằng Mendel là nền, không phải toàn bộ genetics.

## 27. Genetic variation ở population scale

Ở một individual ta nói genotype. Ở population ta quan tâm **allele frequency** và **genotype frequency**.

Đây là bước chuyển cực kỳ quan trọng. Evolution không phải “một individual đổi gene để thích nghi”; nó là change distribution variation trong population qua generation.

Mọi mutation, meiosis, recombination học trong chapter này trở thành input cho population genetics.

## 28. Case study: lactose persistence

Khả năng tiêu hóa lactose ở adulthood liên quan regulation của lactase gene và population history.

Ở một số population có tradition chăn nuôi/sữa, regulatory variant liên quan lactase persistence tăng frequency qua selection.

Trait cho thấy connection:

```text
regulatory DNA variant
→ gene expression after childhood
→ digestive phenotype
→ cultural/environment context
→ differential fitness historically
→ allele-frequency change
```

Gene–culture coevolution nối molecular genetics, inheritance và evolution.

## 29. Case study: antibiotic resistance không phải bacteria “cố biến đổi”

Trong bacterial population có variation do mutation/horizontal gene transfer. Antibiotic giết susceptible cell mạnh hơn. Resistant variant survive/reproduce, làm resistance allele tăng frequency.

Selection thay composition population; antibiotic không “dạy” từng bacterium cách resistance theo nghĩa có mục tiêu.

Đây là bridge sang evolution và microbiology.

## 30. Common misconceptions

“Dominant allele phổ biến hơn recessive allele” sai.

“Recessive nghĩa yếu” sai.

“50% risk nghĩa hai child chắc chắn một affected” sai.

“Heritability cao nghĩa environment không quan trọng” sai.

“Mutation xảy ra để thích nghi” sai.

“Gene và trait có mapping một-một” hiếm khi đúng cho trait phức tạp.

## 31. Bridge: từ family inheritance sang genome và population

Chapter này đi từ meiosis đến allele transmission và variation. Nhưng modern genetics còn hỏi ở scale lớn hơn: hàng triệu variant trong genome được tổ chức thế nào? Chromatin làm gene accessible ra sao? GWAS tìm association bằng cách nào? Transcriptomics đo expression của hàng nghìn gene ra sao?

[[02_genomics_epigenetics_and_regulation]] sẽ mở rộng sang genome-wide regulation và omics.

Sau đó [[../03_evolution_and_diversity/00_evolution_and_population_genetics]] sẽ lấy chính allele frequency, mutation, recombination và fitness để xây theory evolution.

> **Mental model cuối chapter:** heredity là quá trình chromosome/DNA được phân phối qua meiosis và fertilization; variation phát sinh từ mutation + recombination + assortment; phenotype là outcome của genotype trong context. Khi ta chuyển từ một family sang cả population, chính variation này trở thành dữ liệu cho evolution.