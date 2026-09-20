# Di truyền, biến dị và đột biến — Inheritance, Variation and Mutation (유전, 변이와 돌연변이)

Chương trước giải thích cách DNA lưu information và cách cell đọc information đó. Nhưng một organism không chỉ cần giữ information trong một cell; nó phải truyền information sang daughter cell và thế hệ tiếp theo. Khi sexual reproduction xuất hiện, bài toán trở nên khó hơn: mỗi cá thể diploid có hai chromosome set, nhưng gamete chỉ nên nhận một set. Đồng thời offspring không được giống hệt parent, vì meiosis và recombination tạo variation.

Vì vậy inheritance không phải một bảng Punnett độc lập với molecular biology. Nó là hệ quả trực tiếp của cách chromosome được tổ chức và phân chia.

## 1. Chromosome, homolog và allele

Một chromosome là một DNA molecule dài cùng protein liên quan. Ở diploid organism, mỗi chromosome type thường có hai bản homolog: một từ mẹ, một từ cha.

Hai homolog mang cùng nhóm gene nhưng có thể có version khác nhau. Version của một gene gọi là **allele (alen / 대립유전자)**.

Ví dụ một gene có allele A và a. Một cá thể có thể AA, Aa hoặc aa ở locus đó.

Nhưng allele không phải một “trait”. Allele là sequence variant. Trait xuất hiện sau khi sequence ảnh hưởng expression hoặc protein function trong một developmental/environmental context.

## 2. Meiosis giải bài toán giảm chromosome number

Nếu gamete diploid kết hợp với gamete diploid, chromosome number sẽ tăng gấp đôi mỗi generation. Meiosis giải bài toán bằng cách tạo haploid gamete.

Sau một lần DNA replication, cell trải qua hai division.

Trong meiosis I, homologous chromosome pair tách nhau. Trong meiosis II, sister chromatid tách nhau.

Kết quả cuối cùng là gamete có một chromosome từ mỗi homologous pair.

Đây là cơ sở vật lý của Mendel's law of segregation.

## 3. Mendel không chỉ là ratio 3:1

Mendel quan sát trait pattern trước khi chromosome được hiểu rõ. Modern genetics giải thích ratio bằng meiosis.

Nếu parent Aa tạo gamete, homolog mang A và a segregate, nên trong model đơn giản mỗi gamete có probability gần 1/2 mang A và 1/2 mang a.

Cross Aa × Aa:

\[
P(AA)=\frac14,\quad P(Aa)=\frac12,\quad P(aa)=\frac14
\]

Ratio genotype 1:2:1 không phải rule thần bí. Nó đi ra từ independent gamete formation và probability multiplication.

## 4. Dominant không có nghĩa mạnh hơn hoặc phổ biến hơn

Nếu heterozygote Aa có phenotype giống AA, allele A được gọi là **dominant**, a là **recessive** trong context trait đó.

Dominance mô tả relationship phenotype ở heterozygote. Nó không nói allele A có fitness cao hơn, phổ biến hơn hay “tốt hơn”.

Một recessive allele vẫn có thể rất common. Một dominant disease allele vẫn có thể rare.

Đây là misconception quan trọng vì nó nối genetics với evolution: dominance và natural selection là hai concept khác nhau.

## 5. Independent assortment có điều kiện

Mendel's law of independent assortment đúng tốt khi gene nằm trên chromosome khác nhau hoặc đủ xa nhau.

Nếu hai gene nằm gần nhau trên cùng chromosome, chúng có xu hướng được truyền cùng nhau. Đây là **linkage (liên kết gene / 유전자 연관)**.

Meiosis có crossing-over giữa homolog, nên linkage không tuyệt đối.

Recombination frequency tăng theo distance giữa loci trong range nhất định, cho phép genetic mapping.

Ta thấy một pattern đẹp: probability inheritance phản ánh physical geometry trên chromosome.

## 6. Recombination tạo combination mới

Trong prophase I, homologous chromosome pair và có thể exchange segment qua crossing-over.

Điều này không tạo allele hoàn toàn mới như mutation, nhưng tạo **new combinations** của allele.

Sexual reproduction tăng variation qua ít nhất ba cơ chế:

1. independent assortment của chromosome;
2. crossing-over;
3. random fertilization.

Variation này sẽ trở thành nguyên liệu cho evolution ở chapter sau.

## 7. Probability: prediction cho population, không phải lời hứa cho family nhỏ

Nếu một cross cho probability 25% phenotype nào đó, điều đó không có nghĩa bốn offspring chắc chắn có đúng một cá thể như vậy.

Mỗi conception là random event theo model. Với sample nhỏ, observed ratio có thể lệch xa expected ratio.

Khi sample lớn, law of large numbers làm frequency thường gần expectation hơn.

Đây là bridge sang statistics: Mendelian ratio là probability model, dữ liệu thực cần statistical test để xem deviation có hợp lý do chance hay không.

## 8. Khi Mendel đơn giản không đủ

Nhiều trait không tuân dominant/recessive đơn giản.

Trong **incomplete dominance**, heterozygote có phenotype trung gian. Trong **codominance**, hai allele cùng biểu hiện rõ, như ABO blood group với allele A và B.

Một gene cũng có thể có nhiều allele trong population.

Ngoài ra **pleiotropy** xảy ra khi một gene ảnh hưởng nhiều trait, vì protein có thể tham gia nhiều tissue/process.

Ngược lại, **polygenic trait** chịu ảnh hưởng của nhiều gene.

## 9. Quantitative trait: từ category sang distribution

Height, blood pressure, skin pigmentation và nhiều trait khác biến thiên liên tục.

Khi nhiều locus có effect nhỏ cộng thêm environment, phenotype thường tạo distribution thay vì vài category discrete.

Ta có model khái niệm:

\[
P = G + E + G\times E + \epsilon
\]

Trong đó phenotype \(P\) chịu ảnh hưởng genetic component \(G\), environment \(E\), interaction và residual variation.

Equation này không nói organism thật đơn giản là phép cộng; nó là statistical decomposition hữu ích.

## 10. Heritability: câu hỏi về variation trong population

**Heritability (hệ số di truyền / 유전력)** mô tả phần variation phenotype trong một population/environment có thể quy cho genetic variation theo model.

Nó không nói “X% trait của một cá nhân do gene”.

Một trait có heritability cao vẫn có thể thay đổi mạnh nếu environment thay đổi. Ví dụ height có genetic contribution lớn trong nhiều population nhưng nutrition vẫn ảnh hưởng rõ.

Đây là ví dụ về việc statistical concept phải được hiểu đúng scale.

## 11. Mutation tạo allele mới

Recombination trộn allele có sẵn; **mutation** tạo sequence variant mới.

Mutation có thể xuất hiện do replication error, chemical damage, radiation hoặc mobile genetic element.

Nhưng mutation không xuất hiện vì organism “cần thích nghi”. Mutation thường random với respect to adaptive need.

Natural selection sau đó có thể làm frequency của variant thay đổi.

## 12. Mutation effect phụ thuộc vị trí và context

Coding mutation có thể:

- không đổi amino acid vì genetic-code redundancy;
- đổi amino acid;
- tạo stop codon;
- gây frameshift.

Regulatory mutation có thể đổi gene expression. Splice-site mutation có thể đổi RNA processing. Large structural change có thể duplicate hoặc delete gene.

Một mutation cũng có thể neutral trong một environment nhưng harmful hoặc beneficial trong environment khác.

Do đó không thể gắn nhãn mutation chỉ bằng “tốt/xấu” ngoài context.

## 13. Chromosome abnormality: khi variation xảy ra ở scale lớn

Nondisjunction trong meiosis có thể làm gamete nhận thừa hoặc thiếu chromosome.

Sau fertilization, offspring có thể có aneuploidy.

Structural chromosome change gồm deletion, duplication, inversion và translocation.

Duplication đặc biệt quan trọng trong evolution vì một gene copy có thể giữ function cũ trong khi copy khác tích lũy change và đôi khi phát triển function mới.

## 14. Penetrance và expressivity: cùng genotype không nhất thiết cùng phenotype

**Penetrance** hỏi bao nhiêu người mang genotype thể hiện phenotype.

**Expressivity** hỏi phenotype mạnh/yếu đến đâu ở người đã thể hiện.

Hai concept này nhắc lại rằng gene hoạt động trong network và environment, không phải switch isolated.

## 15. Gene–environment interaction

Một allele có effect khác nhau trong environment khác nhau.

Ví dụ enzyme variant có thể chỉ gây phenotype rõ khi diet chứa một substrate nhất định. Temperature có thể ảnh hưởng protein folding ở một số organism. Stress hormone có thể đổi expression program.

Vì vậy inheritance truyền potential và molecular machinery; phenotype là kết quả của development trong environment.

## 16. Family genetics nối tới population genetics thế nào?

Ở family scale, ta hỏi probability offspring nhận allele.

Ở population scale, ta hỏi allele frequency thay đổi qua generation thế nào.

Hai scale nối trực tiếp. Meiosis, mating và reproduction tạo sampling process; mutation, selection, drift và migration thay đổi allele frequency.

Nếu không có variation từ mutation/recombination, evolution không có raw material.

## 17. Từ allele sang genome-wide regulation

Mendelian model thường tập trung một hoặc vài locus. Nhưng modern biology có thể đo hàng triệu variant, chromatin state, RNA abundance và protein expression.

Điều này đặt câu hỏi mới: genome không chỉ là list gene; nó được tổ chức và regulation trên quy mô toàn genome như thế nào? Vì sao cùng DNA nhưng cell type khác nhau? Epigenetic mark có vai trò gì? GWAS thực sự nói được gì?

Đó là bridge sang [[02_genomics_epigenetics_and_regulation]].