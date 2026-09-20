# Tiến hóa và di truyền quần thể — Evolution and Population Genetics (진화와 집단유전학)

Genetics giải thích variation được tạo và truyền đi. Evolution đặt câu hỏi ở scale lớn hơn: **khi variation đó đi qua hàng trăm, hàng nghìn hay hàng triệu thế hệ, population thay đổi như thế nào?**

**Evolution (tiến hóa / 진화)** theo nghĩa population genetics là sự thay đổi frequency của heritable variant trong population qua thế hệ. Đây là định nghĩa rất khác với cách nói đời thường “tiến hóa thành cao cấp hơn”. Evolution không có hướng bắt buộc tới complexity hay perfection.

## Population là đơn vị quan trọng

Một **population (quần thể / 개체군)** là nhóm individual cùng species sống trong vùng và có khả năng trao đổi gene ở mức nào đó.

Individual có genotype; population có **allele frequency**.

Giả sử locus có allele A và a. Trong 100 diploid individual có 200 allele copy. Nếu 120 copy là A và 80 là a:

\[
p=0.6,\quad q=0.4
\]

với \(p+q=1\).

Evolution có thể được quan sát như việc p và q thay đổi theo thế hệ.

> **Mental model:** genetics hỏi “một offspring nhận allele nào?”; population genetics hỏi “sau nhiều generation, allele nào trở nên phổ biến hơn hoặc hiếm hơn, và vì sao?”.

## Hardy–Weinberg equilibrium — null model trước khi nói evolution

**Hardy–Weinberg equilibrium (하디-바인베르크 평형)** là model tưởng tượng population lý tưởng không có selection, mutation, migration, drift đáng kể và mating ngẫu nhiên tại locus xét.

Nếu allele frequency là p và q, genotype frequency kỳ vọng sau random mating:

\[
p^2 + 2pq + q^2 = 1
\]

Trong đó \(p^2\) là AA, \(2pq\) là Aa, \(q^2\) là aa.

Model không nhằm nói nature thực sự đáp ứng mọi assumption. Nó là **baseline**. Nếu observed genotype khác expectation, ta hỏi process nào đang tác động.

Đây giống null model trong statistics: hiểu trạng thái “không có lực tiến hóa” giúp nhận diện force thật.

## Natural selection — không phải sinh vật tự cố thay đổi

**Natural selection (chọn lọc tự nhiên / 자연선택)** cần ba điều cơ bản:

1. individual khác nhau về trait;
2. variation có phần heritable;
3. variation ảnh hưởng reproductive success trong environment cụ thể.

Nếu genotype nào tạo nhiều surviving offspring hơn trung bình, allele liên quan có thể tăng frequency.

### Fitness

**Fitness (độ thích nghi / 적합도)** trong evolution không đồng nghĩa khỏe, mạnh hay sống lâu. Nó liên quan contribution của genotype/phenotype vào thế hệ tiếp theo trong context cụ thể.

Một trait giúp sống rất lâu nhưng làm reproduction bằng 0 có thể có fitness thấp.

### Selection không “chọn” có ý thức

Natural selection không phải agent. Không có entity xem trait nào tốt rồi quyết định giữ lại. Differential survival/reproduction tạo statistical outcome qua nhiều generation.

## Adaptation — kết quả lịch sử của selection

**Adaptation (thích nghi tiến hóa / 적응)** là heritable trait trở nên phổ biến vì từng tăng fitness trong environment lịch sử.

Cần phân biệt với **acclimation/acclimatization**, thay đổi sinh lý của individual trong đời, ví dụ tăng ventilation khi lên altitude.

Một adaptation luôn có trade-off và constraint. Không có trait nào tốt tuyệt đối ở mọi environment.

## Mutation — nguồn variation mới nhưng không hướng theo nhu cầu

Mutation tạo allele mới. Rate mutation thường nhỏ trên mỗi base mỗi generation, nhưng genome lớn và population lớn nên tổng mutation vẫn đáng kể.

Mutation xảy ra không “biết” environment cần gì. Antibiotic không làm bacteria cố tạo đúng mutation resistance. Resistant mutation có thể đã có hoặc xuất hiện random; antibiotic sau đó tạo strong selection làm resistant lineage tăng.

## Genetic drift — evolution do sampling ngẫu nhiên

**Genetic drift (phiêu bạt di truyền / 유전적 부동)** là thay đổi allele frequency do random sampling giữa generation.

Effect mạnh hơn trong population nhỏ.

Hãy tưởng tượng jar có red và blue bead đại diện allele. Nếu mỗi generation chỉ lấy ngẫu nhiên một số bead để tạo generation tiếp theo, ratio có thể lệch chỉ vì chance.

Qua nhiều generation, allele có thể bị fixed hoặc lost mà không liên quan advantage.

### Bottleneck

**Population bottleneck (병목현상)** xảy ra khi population size giảm mạnh. Những survivor chỉ đại diện một sample genetic diversity cũ.

Khi population phục hồi number, diversity đã mất không tự động quay lại.

### Founder effect

**Founder effect (창시자 효과)** xảy ra khi một population mới được lập bởi số ít individual. Allele frequency của group founder có thể khác population gốc do sampling.

## Gene flow — migration nối các population

**Gene flow (dòng gene / 유전자 흐름)** là movement allele giữa population qua migration và reproduction.

Gene flow thường làm population giống nhau hơn về allele frequency, nhưng cũng có thể đưa adaptive allele mới vào population.

Trong conservation, fragmented habitat giảm gene flow có thể làm small population tăng inbreeding và drift.

## Sexual selection

Một trait có thể giảm survival một chút nhưng tăng mating success mạnh. **Sexual selection (선택)** mô tả selection qua competition for mates hoặc mate choice.

Peacock tail là example kinh điển. Tail tốn energy và có thể tăng visibility, nhưng nếu tăng reproductive success thì vẫn được selection duy trì.

## Different modes of selection

**Directional selection** đẩy trait distribution về một phía.

**Stabilizing selection** favor intermediate range và loại extreme.

**Disruptive selection** có thể favor hai extreme hơn intermediate trong một số environment.

Nhưng real trait thường polygenic và fitness landscape có thể thay đổi, nên ba pattern là model chứ không phải three boxes exhaustive.

## Frequency-dependent selection

Fitness có thể phụ thuộc trait phổ biến hay hiếm.

Trong **negative frequency-dependent selection**, rare phenotype có advantage vì predator/search image hoặc interaction khác. Điều này có thể duy trì polymorphism.

Evolution vì vậy không phải lúc nào cũng kéo population về một “best allele” duy nhất.

## Coevolution

Species tương tác tạo selection pressure lên nhau.

Predator và prey, host và parasite, flower và pollinator có thể trải qua **coevolution (đồng tiến hóa / 공진화)**.

Một adaptation ở species A thay environment của B; response của B lại thay environment của A.

Đây là feedback ở evolutionary scale.

## Speciation — khi gene flow suy giảm đủ lâu

**Speciation (hình thành loài / 종분화)** là process lineage tách thành species khác.

Một cơ chế common là geographic isolation: population bị chia bởi mountain, island hoặc distance; gene flow giảm; mutation, selection và drift làm chúng divergence.

Nếu reproductive isolation phát triển, hai group có thể trở thành species khác.

Nhưng species concept có nhiều loại và không phải organism nào cũng phù hợp biological species concept, đặc biệt asexual organism hoặc fossil.

## Evidence for evolution

Evolution không dựa vào một bằng chứng duy nhất.

### Fossil record

Fossil cho sequence thay đổi và extinct lineage qua geological time, dù record không bao giờ complete.

### Comparative anatomy

**Homologous structure** có common origin nhưng function có thể khác. Forelimb bone pattern của human, whale và bat phản ánh shared ancestry.

### Biogeography

Distribution species trên island và continent phù hợp với history dispersal, isolation và plate tectonics.

### Molecular evidence

DNA/protein sequence cho phép estimate relatedness. Shared mutation và conserved gene tạo evidence rất mạnh cho common descent.

### Direct observation

Antibiotic resistance, pesticide resistance, virus evolution và experimental evolution cho phép quan sát frequency change trong timescale ngắn.

## Phylogenetic thinking

Evolution tạo branching lineage. Vì vậy relatedness nên được nghĩ bằng tree chứ không ladder.

Human không “tiến hóa từ con khỉ hiện đại”. Human và modern ape share common ancestor; các lineage sau đó diverged.

Không có living species nào là “ancestor chưa tiến hóa” của species khác chỉ vì morphology trông simple.

## Evolution và optimization

Natural selection có thể tạo structure rất hiệu quả, nhưng không guarantee global optimum.

Evolution bị constraint bởi:

- ancestral structure;
- available variation;
- developmental pathway;
- trade-off;
- changing environment;
- drift.

Trong computer science, evolutionary algorithm dùng mutation/selection analogy để search solution space. Nhưng biological evolution phức tạp hơn vì genotype–phenotype mapping, ecology và history.

## Common misconceptions

### “Individual tiến hóa vì cần thích nghi”

Individual có thể acclimate; population evolution qua generation.

### “Survival of the fittest nghĩa là mạnh nhất sống”

Fitness là reproductive success trong context, không phải strength.

### “Evolution hoàn toàn ngẫu nhiên”

Mutation và drift có stochastic component; selection thì non-random đối với differential reproductive success trong environment.

### “Evolution luôn làm organism phức tạp hơn”

Không. Simplification có thể adaptive. Parasite thường mất structure không còn cần.

## Mental Model

> Evolution là population-level change tạo bởi mutation, recombination, selection, drift và gene flow. Selection lọc variation theo environment, drift thay frequency do chance, và branching qua thời gian tạo diversity của life.

File [[01_phylogeny_taxonomy_and_biodiversity]] sẽ xây cách đọc evolutionary tree và hệ thống phân loại; [[02_microorganisms_and_viruses]] cho thấy evolution hoạt động đặc biệt nhanh và rõ ở microorganism.