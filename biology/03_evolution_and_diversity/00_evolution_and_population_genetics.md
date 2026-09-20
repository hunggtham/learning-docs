# Tiến hóa và di truyền quần thể — Evolution and Population Genetics (진화와 집단유전학)

Genetics giải thích allele được tạo và truyền thế nào. Evolution hỏi một câu khác ở scale lớn hơn: **khi hàng nghìn cá thể sinh sản qua nhiều thế hệ, tần số allele trong population thay đổi vì những lực nào?**

Đây là điểm chuyển quan trọng từ “inheritance trong một family” sang “change trong một population”. Evolution không xảy ra vì một cá thể cố thích nghi trong đời mình. Nó là sự thay đổi distribution của heritable variation qua generation.

## 1. Population là đơn vị để theo dõi allele frequency

Một **population (quần thể / 개체군)** là nhóm cá thể cùng species có khả năng giao phối trong một khu vực và thời gian nhất định.

Nếu một locus có allele A và a, ta có thể mô tả population bằng frequency:

\[
p=f(A),\quad q=f(a),\quad p+q=1
\]

Evolution ở mức tối thiểu có thể được định nghĩa là **change in allele frequency over generations**.

Định nghĩa này biến evolution từ ý tưởng mơ hồ thành một quantity có thể đo.

## 2. Hardy–Weinberg: null model để biết khi nào population đang đổi

Nếu không có selection, mutation, migration, drift và mating là random, genotype frequency có thể ổn định theo:

\[
p^2+2pq+q^2=1
\]

Đây là **Hardy–Weinberg equilibrium (하디-바인베르크 평형)**.

Không nên học nó như “quy luật quần thể thật phải tuân theo”. Population thật hiếm khi hoàn toàn đáp ứng assumption.

Nó giống null model trong statistics: nếu observed data lệch mạnh khỏi expectation, ta hỏi force nào đang tác động.

## 3. Mutation: nguồn allele mới

Mutation tạo sequence variant mới. Nhưng mutation rate thường nhỏ, nên mutation một mình hiếm khi thay allele frequency cực nhanh trong short term.

Vai trò sâu hơn của mutation là cung cấp **raw variation** lâu dài.

Selection không tạo mutation phù hợp theo nhu cầu. Selection chỉ làm khác biệt reproductive success giữa variant đã xuất hiện.

## 4. Natural selection: từ phenotype đến reproductive success

**Natural selection (chọn lọc tự nhiên / 자연선택)** cần ba điều:

1. cá thể khác nhau về trait;
2. một phần khác biệt có thể di truyền;
3. trait ảnh hưởng reproductive success trong environment hiện tại.

Nếu đủ ba điều, variant liên quan higher reproductive success có xu hướng tăng frequency.

Selection không “muốn” tạo organism hoàn hảo. Nó là statistical consequence của differential reproduction.

## 5. Fitness: concept tương đối, không phải sức khỏe chung

**Fitness (적합도)** trong evolution liên quan contribution gene vào generation sau.

Một trait tăng survival nhưng giảm reproduction mạnh có thể không tăng fitness tổng.

Fitness cũng phụ thuộc environment. Fur dày có thể beneficial ở lạnh nhưng costly ở nóng.

Do đó không tồn tại “allele tốt tuyệt đối” ngoài context.

## 6. Selection làm việc trên phenotype, inheritance truyền genotype

Environment “thấy” phenotype: tốc độ chạy, color, enzyme activity, immune response.

Nhưng response evolutionary chỉ xảy ra nếu variation phenotype có heritable component.

Ta có chain:

```text
genotype variation
   ↓
phenotype variation
   ↓
differential survival/reproduction
   ↓
different allele contribution
   ↓
allele-frequency change
```

Điều này nối trực tiếp genotype–phenotype model ở genetics với population change.

## 7. Genetic drift: randomness cũng làm population tiến hóa

Không phải mọi allele-frequency change đều do selection.

**Genetic drift (phiêu bạt di truyền / 유전적 부동)** là random change do sampling finite population.

Nếu population nhỏ, chance event có thể làm allele biến mất hoặc fix dù allele neutral.

Ví dụ, vài cá thể tình cờ sinh nhiều offspring hơn không phải vì trait superior mà do chance.

Drift mạnh hơn ở small population.

## 8. Bottleneck và founder effect

Nếu population giảm mạnh đột ngột, survivors chỉ là sample của original gene pool. Đây là **bottleneck**.

Nếu một nhóm nhỏ colonize vùng mới, allele frequency của population mới phản ánh sample nhỏ ban đầu — **founder effect**.

Hai case cho thấy history contingency ảnh hưởng genetic structure.

Population hiện tại không chỉ phản ánh “selection tối ưu”; nó còn mang dấu vết accident quá khứ.

## 9. Gene flow: population không đóng kín

**Gene flow (dòng gene / 유전자 이동)** xảy ra khi cá thể hoặc gamete di chuyển giữa population và reproduce.

Gene flow có thể làm population giống nhau hơn về allele frequency và mang allele mới vào local population.

Nó cũng có thể chống lại local adaptation nếu migration liên tục đưa allele không phù hợp local environment.

## 10. Selection mode và distribution trait

Selection có thể làm distribution phenotype thay đổi theo pattern khác nhau.

**Directional selection** ưu tiên một phía của distribution.

**Stabilizing selection** ưu tiên vùng trung tâm.

**Disruptive selection** ưu tiên hai extreme.

Nhưng đây là descriptive pattern, không phải ba “loại lực” hoàn toàn độc lập.

## 11. Frequency-dependent selection

Fitness của phenotype đôi khi phụ thuộc frequency của chính nó.

Một rare strategy có thể có advantage vì competitor chưa adapted, hoặc common phenotype có advantage nhờ cooperation.

Điều này làm evolution trở thành dynamical game thay vì một hướng cố định.

## 12. Sexual selection

Trait có thể tăng mating success dù có survival cost.

Peacock tail là example kinh điển: costly structure nhưng có thể tăng reproductive opportunity.

Sexual selection nhắc rằng fitness phải tính reproduction, không chỉ sống lâu.

## 13. Adaptation là kết quả lịch sử, không phải mục đích

**Adaptation (thích nghi / 적응)** là heritable trait tăng fitness trong environment nhất định và đã được shaped bởi selection.

Không nên nói organism “phát triển trait vì cần nó”. Cách nói đúng causal hơn là variant khác nhau tồn tại, variant phù hợp reproduce nhiều hơn, qua generation frequency thay đổi.

Language mục đích dễ làm evolution bị hiểu như planning process.

## 14. Constraint và trade-off

Selection không bắt đầu từ blank design. Nó sửa trên structure có sẵn.

Evolution bị constrain bởi developmental pathway, genetic architecture, physical law và history.

Một trait có benefit và cost. Hemoglobin phải bind oxygen đủ mạnh ở lung nhưng phải release ở tissue. Bone phải strong nhưng không quá heavy.

Do đó adaptation thường là compromise.

## 15. Speciation: khi gene flow giảm đủ lâu

**Speciation (hình thành loài / 종분화)** xảy ra khi lineage diverge đến mức reproductive isolation duy trì khác biệt.

Geographic separation có thể giảm gene flow. Sau đó mutation, drift và selection làm population diverge.

Nếu reproductive barrier hình thành, ngay cả khi gặp lại, gene flow vẫn thấp.

Speciation vì thế là population genetics kéo dài theo thời gian.

## 16. Species concept có nhiều cách định nghĩa

Biological species concept nhấn mạnh reproductive isolation.

Morphological concept dùng form.

Phylogenetic concept nhấn mạnh lineage riêng trên tree.

Không có một definition tiện cho mọi organism, đặc biệt bacteria, fossil và asexual organism.

Điều này dẫn thẳng tới phylogeny và taxonomy.

## 17. Evolution ở molecular scale

Protein sequence cũng thay đổi qua mutation và selection/drift.

Nếu một amino acid cực kỳ quan trọng cho function, position đó thường conserved. Nếu change ít ảnh hưởng, variation có thể tích lũy nhanh hơn.

Comparative sequence vì thế cho phép suy evolutionary relationship.

Genomics đã biến evolution thành data problem có thể đo trên hàng triệu site.

## 18. Antibiotic resistance: evolution có thể quan sát trực tiếp

Trong bacterial population, mutation hoặc horizontal gene transfer tạo resistance variant.

Antibiotic không “dạy” bacterium kháng thuốc. Nó tạo selection pressure: susceptible cell chết hoặc grow kém, resistant cell có relative advantage.

Sau treatment, resistant allele/gene frequency tăng.

Đây là evolution theo đúng population-genetic logic.

## 19. Evolution và medicine

Pathogen evolution ảnh hưởng vaccine, drug resistance và virulence.

Human allele frequency cũng phản ánh lịch sử selection, drift, migration và demographic bottleneck.

Một variant từng beneficial trong environment cũ có thể neutral hoặc harmful trong environment mới.

Evolutionary reasoning giúp đặt physiology và disease vào historical context.

## 20. Từ population change sang cây sự sống

Nếu population tách ra, divergence tích lũy qua thời gian. Sau hàng triệu năm, lineage tạo branching pattern.

Câu hỏi kế tiếp không còn chỉ là “allele frequency thay đổi thế nào?” mà là:

**làm sao reconstruct quan hệ họ hàng giữa species, đọc một phylogenetic tree thế nào, và taxonomy nên phản ánh history ra sao?**

Tiếp tục với [[01_phylogeny_taxonomy_and_biodiversity]].