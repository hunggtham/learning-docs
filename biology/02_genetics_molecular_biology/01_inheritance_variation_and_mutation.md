# Di truyền, biến dị và đột biến — Inheritance, Variation and Mutation (유전·변이·돌연변이)

Di truyền học (Genetics / 유전학) nghiên cứu cách biological information được truyền qua thế hệ và vì sao offspring vừa giống vừa khác nhau. Nếu molecular biology tập trung vào cách DNA được đọc trong cell, genetics mở rộng câu hỏi sang chromosome, meiosis, allele, probability và phenotype.

## Mendel và logic của inheritance

Gregor Mendel cho thấy nhiều trait có thể được giải thích bằng các hereditary factor tồn tại thành cặp và tách nhau khi tạo gamete. Ngày nay ta gọi những version khác nhau của một gene là allele (대립유전자).

Trong organism diploid, mỗi locus thường có hai allele, một từ mỗi parent. Khi meiosis xảy ra, hai allele segregate vào gamete khác nhau. Fertilization ghép hai gamete để tái tạo trạng thái diploid.

Định luật phân ly (Law of Segregation / 분리의 법칙) vì vậy không phải rule trừu tượng; nó xuất phát trực tiếp từ việc homologous chromosomes tách trong meiosis.

## Probability trong di truyền

Nếu hai heterozygous parent `Aa × Aa` tạo offspring, mỗi parent truyền A hoặc a với xác suất khoảng 1/2. Kết hợp hai event độc lập cho genotype ratio:

```text
AA : Aa : aa = 1 : 2 : 1
```

Nếu A hoàn toàn dominant so với a, phenotype ratio trở thành 3:1.

Điều này không có nghĩa cứ bốn con thì chính xác ba con biểu hiện dominant phenotype. Probability mô tả distribution dài hạn của nhiều event độc lập.

## Dominance không đồng nghĩa superiority

Trội (Dominant / 우성) mô tả phenotype của heterozygote. Lặn (Recessive / 열성) mô tả allele có phenotype bị che trong heterozygote. Dominant allele không nhất thiết phổ biến hơn, tốt hơn hay “mạnh” hơn.

Incomplete dominance tạo intermediate phenotype; codominance cho phép cả hai allele cùng biểu hiện rõ, như hệ nhóm máu ABO ở một số genotype.

## Independent assortment có điều kiện

Các gene nằm trên chromosome khác nhau thường assort độc lập trong meiosis. Nhưng gene gần nhau trên cùng chromosome có thể linkage và không tuân theo independent assortment hoàn toàn.

Crossing over trong prophase I tạo recombinant chromosome. Xác suất recombination giữa hai locus tăng theo khoảng cách tương đối giữa chúng, tạo nền cho genetic mapping.

## Mutation là nguồn variation mới

Đột biến (Mutation / 돌연변이) là thay đổi trong DNA sequence hoặc chromosome structure. Mutation có thể là substitution, insertion, deletion, duplication, inversion hoặc translocation.

Point mutation trong coding region có thể silent, missense hoặc nonsense tùy ảnh hưởng lên codon. Insertion/deletion không phải bội số của ba có thể gây frameshift.

Mutation không xảy ra “vì organism cần nó”. Phần lớn mutation xuất hiện từ replication error, DNA damage hoặc transposable element; selection chỉ tác động sau đó lên effect của variation.

> Mental model: mutation tạo candidate; recombination xáo trộn candidate; inheritance truyền chúng; selection và drift thay đổi tần số ở population.

## DNA repair và mutation rate

Cell có base excision repair, nucleotide excision repair, mismatch repair và nhiều pathway khác. Repair không hoàn hảo nên mutation rate không bằng zero.

Một mutation rate bằng zero cũng không hẳn tối ưu về evolutionary perspective: không có variation mới thì khả năng thích nghi lâu dài giảm. Tuy nhiên quá nhiều mutation phá genome stability.

## Chromosome và nondisjunction

Chromosome (염색체) là DNA molecule cùng protein tổ chức nó. Trong meiosis, homologous chromosomes phải phân ly chính xác. Nondisjunction xảy ra khi chromosome không tách đúng, tạo gamete có số chromosome bất thường.

Aneuploidy như trisomy 21 là hệ quả của kiểu error này. Đây là ví dụ cho thấy mutation không chỉ xảy ra ở nucleotide scale mà còn ở chromosome scale.

## Quantitative traits

Nhiều trait như chiều cao, huyết áp hay skin pigmentation không do một gene đơn lẻ quyết định mà là polygenic và chịu ảnh hưởng environment. Vì vậy distribution phenotype thường liên tục thay vì chia thành vài category.

Trong quantitative genetics, phenotype thường được conceptualize như:

```math
P = G + E + G\times E
```

Đây không phải phương trình cơ học tuyệt đối cho từng cá thể, mà là cách phân tách variation thành genetic effect, environmental effect và interaction.

## Heritability không nói trait “do gene bao nhiêu phần trăm”

Heritability (유전력) đo tỷ lệ variation phenotype trong một population và environment cụ thể có thể liên hệ với genetic variation. Nó không phải tỷ lệ phần trăm trait của một cá nhân “được quyết định bởi gene”.

Nếu môi trường đồng nhất, heritability có thể cao dù environment vẫn rất quan trọng cho trait. Đây là một trong những khái niệm dễ bị hiểu sai khi đọc nghiên cứu genetics.

## Common misconceptions

“Mutation luôn có hại” là sai. Phần lớn có thể neutral; một số có hại; số ít có lợi trong context cụ thể.

“Trait phức tạp có một gene gây ra” thường là simplification. Nhiều phenotype xuất hiện từ network gene và environment.

## Kết nối

Cơ chế DNA nằm trong [[00_dna_genes_and_gene_expression]]. Population-level fate của allele được phát triển trong [[../03_evolution_and_diversity/00_evolution_and_population_genetics]]. Genome-wide variation và epigenetic regulation nằm trong [[02_genomics_epigenetics_and_regulation]].
