# Di truyền, giảm phân, biến dị và đột biến — Inheritance, Meiosis, Variation and Mutation (유전, 감수분열, 변이와 돌연변이)

DNA giải thích cách information được lưu và biểu hiện trong một cell. Nhưng Sinh học còn phải giải thích một câu hỏi lớn hơn: **vì sao con giống cha mẹ nhưng không giống hệt?**

Câu trả lời nằm ở chromosome, meiosis, recombination, fertilization và mutation. Khi những process này kết hợp, genetic information vừa được bảo tồn vừa được xáo trộn đủ để tạo variation.

## Chromosome pair và ploidy

Ở nhiều eukaryote sinh sản hữu tính, cell body là **diploid (lưỡng bội / 이배체)**: mỗi chromosome type có hai bản tương đồng, một thường đến từ mẹ và một từ cha.

Hai chromosome tương đồng gọi là **homologous chromosomes (nhiễm sắc thể tương đồng / 상동염색체)**. Chúng mang các gene ở vị trí tương ứng nhưng có thể chứa version khác nhau của gene.

Một version của gene gọi là **allele (alen / 대립유전자)**.

Ví dụ, một locus có allele A và a. Một diploid individual có thể có AA, Aa hoặc aa tại locus đó.

**Haploid (đơn bội / 반수체)** cell chỉ có một set chromosome. Human sperm và egg là haploid.

## Genotype và phenotype

**Genotype (kiểu gene / 유전자형)** mô tả genetic composition tại locus hoặc rộng hơn.

**Phenotype (kiểu hình / 표현형)** là trait quan sát/đo được phát sinh từ genotype tương tác với environment và development.

Không nên hiểu phenotype = genotype được “in ra” thẳng. Height, body mass, blood pressure và nhiều trait phức tạp chịu ảnh hưởng của nhiều gene và environment.

> **Mental model:** genotype đặt ra một tập khả năng và constraint; phenotype là kết quả của genotype vận hành trong một developmental/environmental context cụ thể.

## Mendel bắt đầu từ pattern chứ không biết DNA

Gregor Mendel nghiên cứu pea plant trước khi chromosome và DNA được hiểu rõ. Ông nhận ra inheritance có pattern có thể mô hình hóa bằng discrete factor.

Ngày nay ta biết các “factor” này tương ứng gần với allele của gene trong nhiều trường hợp đơn giản.

## Segregation — vì sao mỗi gamete chỉ nhận một allele?

Một diploid individual Aa có hai allele ở homologous chromosome. Khi tạo gamete qua meiosis, homologous chromosome tách nhau, nên mỗi gamete nhận một allele.

Đây là molecular basis của **law of segregation (quy luật phân li / 분리의 법칙)**.

Nếu segregation unbiased, một Aa individual tạo gamete A và a với probability gần 1/2 mỗi loại.

Khi Aa × Aa:

```text
       A     a
    +-----+-----+
 A  | AA  | Aa  |
    +-----+-----+
 a  | Aa  | aa  |
    +-----+-----+
```

Probability genotype là 1/4 AA, 1/2 Aa, 1/4 aa.

Điều này không có nghĩa bốn đứa con chắc chắn sẽ theo ratio 1:2:1. Mỗi offspring là một event xác suất; ratio chỉ trở nên gần expectation khi sample lớn.

## Dominant không có nghĩa mạnh hơn hoặc tốt hơn

Nếu heterozygote Aa có phenotype giống AA trong một trait cụ thể, A được gọi là **dominant allele (alen trội / 우성 대립유전자)** và a là recessive.

Dominance mô tả **relationship của phenotype trong heterozygote**, không nói allele phổ biến hơn, tiến hóa hơn hay tốt hơn.

Một allele recessive có thể rất phổ biến. Một allele dominant có thể hiếm.

## Beyond simple dominance

Nhiều trait không theo dominant/recessive đơn giản.

**Incomplete dominance (trội không hoàn toàn / 불완전 우성)**: heterozygote có phenotype trung gian.

**Codominance (đồng trội / 공동우성)**: hai allele cùng được biểu hiện, như A và B trong ABO blood group.

**Multiple alleles**: population có hơn hai allele tại locus, dù mỗi diploid individual thường chỉ mang tối đa hai.

**Pleiotropy (đa hiệu / 다면발현)**: một gene ảnh hưởng nhiều trait.

**Polygenic trait (tính trạng đa gene / 다인자 형질)**: nhiều gene cùng đóng góp.

## Independent assortment và chromosome

Mendel thấy allele của hai gene có thể assort tương đối độc lập. Molecular basis là orientation ngẫu nhiên của homologous chromosome pair trong meiosis I.

Nhưng **independent assortment không luôn đúng** nếu hai gene nằm gần nhau trên cùng chromosome.

Gene gần nhau có xu hướng được di truyền cùng nhau, gọi là **genetic linkage (liên kết gene / 유전자 연관)**.

Crossing over có thể phá linkage, và probability recombination tăng theo physical distance ở một range nhất định. Chính principle này từng được dùng để lập genetic map.

# Meiosis — process tạo gamete và variation

**Meiosis (giảm phân / 감수분열)** gồm một lần DNA replication nhưng hai lần division, tạo haploid cells từ diploid precursor.

## Meiosis I — tách homologous chromosome

Trước meiosis, DNA replicate. Mỗi chromosome có hai sister chromatids.

Trong prophase I, homologous chromosome pair với nhau. Đây là điểm khác rất quan trọng so với mitosis.

### Crossing over

Homologous chromosome có thể trao đổi đoạn DNA tại **crossing over (교차)**.

Result là chromosome recombinant chứa combination allele mới.

Crossing over không phải mutation theo nghĩa tạo base mới; nó reshuffle existing variation giữa homolog.

Trong metaphase I, homolog pair align với orientation ngẫu nhiên. Trong anaphase I, homolog tách nhau.

## Meiosis II — tách sister chromatid

Sau meiosis I, cell đã giảm số homologous set nhưng mỗi chromosome vẫn gồm hai sister chromatid.

Meiosis II tách sister chromatid, tương tự một số aspect của mitosis.

Kết quả cuối thường là bốn haploid product từ một precursor, dù gametogenesis ở egg/sperm có detail khác nhau.

## Ba nguồn variation lớn của sexual reproduction

### Independent assortment

Ở organism có n chromosome pair, chỉ riêng orientation của homolog pair đã tạo khoảng:

\[
2^n
\]

combination chromosome khác nhau trước khi tính crossing over.

Ở người n = 23, con số là hơn 8 triệu combination từ assortment đơn thuần.

### Crossing over

Crossing over tạo chromosome recombinant, làm diversity lớn hơn nhiều.

### Random fertilization

Một sperm bất kỳ kết hợp một egg bất kỳ tạo thêm combination.

Vì vậy sibling cùng cha mẹ vẫn có genome combination khác nhau đáng kể.

## Mutation — nguồn allele mới

Recombination chỉ shuffle allele đang có. **Mutation (đột biến / 돌연변이)** mới tạo sequence variation mới.

### Point mutation

Một nucleotide bị thay đổi. Effect có thể synonymous, missense hoặc nonsense nếu nằm trong coding sequence.

### Insertion và deletion

Nucleotide được thêm hoặc mất. Nếu số base không chia hết cho 3 trong coding region, có thể gây **frameshift**, thay đổi cách codon được đọc downstream.

### Structural variation

Đoạn chromosome có thể duplication, deletion, inversion hoặc translocation.

### Copy-number variation

Một region có số copy khác nhau giữa individual.

Mutation ở regulatory region cũng có thể đổi expression mà protein sequence không thay đổi.

## Mutation xuất hiện do đâu?

Mutation có thể từ replication error, spontaneous chemical change, reactive oxygen species, UV radiation hoặc một số mutagen khác.

Điều quan trọng: mutation không xuất hiện “vì organism cần nó”. Need không hướng mutation đến solution phù hợp.

Selection có thể làm mutation hữu ích lan rộng sau khi nó xuất hiện, nhưng selection không tạo mutation có mục tiêu.

## Germline và somatic mutation

**Germline mutation (đột biến dòng mầm / 생식세포 돌연변이)** có thể truyền cho offspring nếu nằm trong lineage tạo gamete.

**Somatic mutation (đột biến soma / 체세포 돌연변이)** xuất hiện trong body cell và thường không truyền qua reproduction, nhưng có thể góp phần vào cancer hoặc mosaicism.

## Penetrance và expressivity

Một genotype không phải lúc nào cũng tạo phenotype giống nhau 100%.

**Penetrance (độ thâm nhập / 침투도)** nói proportion người mang genotype biểu hiện trait.

**Expressivity (mức độ biểu hiện / 표현도)** nói mức độ/severity phenotype khác nhau giữa individual có cùng genotype.

Hai khái niệm này nhắc ta rằng genetic effect tồn tại trong network và environment.

## Gene–environment interaction

Phenotype thường là function của genotype, environment và interaction:

\[
P \approx G + E + G\times E
\]

Đây không phải equation cơ học tuyệt đối mà là conceptual statistical decomposition.

Ví dụ genetic variant có thể ảnh hưởng cách body phản ứng với diet, temperature hoặc pathogen. Cùng genotype trong environment khác có thể cho phenotype khác.

## Heritability không phải “bao nhiêu phần trăm trait do gene quyết định”

**Heritability (hệ số di truyền / 유전력)** trong quantitative genetics mô tả proportion phenotypic variance trong một population và environment cụ thể liên quan genetic variance.

Nếu height có heritability cao trong một population, không có nghĩa height của một cá nhân “80% do gene”. Heritability là population-level statistic, không chia một người thành phần gene và environment.

Đây là misconception rất phổ biến.

## Pedigree — suy luận inheritance từ family pattern

**Pedigree (phả hệ di truyền / 가계도)** dùng symbol để theo dõi trait qua thế hệ.

Pattern autosomal dominant, autosomal recessive, X-linked có thể được suy luận từ distribution, nhưng real pedigree có sample nhỏ, incomplete penetrance và de novo mutation nên không phải lúc nào cũng textbook-clean.

## Common misconceptions

### “Dominant allele sẽ dần loại recessive allele khỏi population”

Không. Dominance không trực tiếp quyết định frequency change. Selection phụ thuộc fitness effect của genotype.

### “Một trait có genetic component nghĩa là không thay đổi được”

Sai. Genetic influence không đồng nghĩa deterministic. Environment hoặc intervention vẫn có thể thay phenotype.

### “Mutation luôn làm organism yếu đi”

Phần lớn mutation có effect nhỏ/neutral; một số harmful; một số có thể beneficial trong context cụ thể.

### “Meiosis chỉ là mitosis hai lần”

Không. Pairing của homolog, crossing over và separation of homolog trong meiosis I làm meiosis có logic riêng.

## Mental Model

> Inheritance bảo tồn information qua chromosome; meiosis giảm ploidy và reshuffle allele; fertilization khôi phục diploidy; mutation tạo variation mới. Variation này là cầu nối trực tiếp từ genetics sang evolution.

File [[02_genomics_epigenetics_and_regulation]] sẽ chuyển từ inheritance pattern sang câu hỏi: genome lớn được tổ chức và điều hòa như thế nào, tại sao cùng DNA nhưng cell khác nhau, và “epigenetics” thực sự nghĩa là gì.