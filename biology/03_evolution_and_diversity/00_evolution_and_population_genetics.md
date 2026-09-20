# Tiến hóa và di truyền quần thể — Evolution and Population Genetics (진화·집단유전학)

Tiến hóa (Evolution / 진화) là sự thay đổi đặc điểm di truyền của quần thể qua các thế hệ. Để hiểu nó đúng bản chất, cần rời khỏi hình ảnh “cá thể tự thay đổi để thích nghi” và chuyển sang một mental model khác: variation đã tồn tại trong population, inheritance truyền variation đó, rồi các process như selection, drift, mutation và migration làm allele frequency thay đổi.

## Evolution xảy ra ở population, không phải vì cá thể cố gắng thay đổi

Một cá thể có thể acclimate với môi trường trong đời sống của nó, nhưng đó không phải evolution theo nghĩa population genetics. Evolution cần thay đổi tần số allele hoặc distribution trait qua nhiều generation.

Natural selection (Chọn lọc tự nhiên / 자연선택) xảy ra khi các phenotype khác nhau dẫn tới khác biệt về survival hoặc reproduction và variation đó có thành phần heritable.

## Fitness là khái niệm tương đối

Fitness (적합도) trong evolutionary biology không có nghĩa “mạnh khỏe” theo ngôn ngữ đời thường. Nó mô tả contribution tương đối của genotype hoặc phenotype vào thế hệ sau trong một environment cụ thể.

Một trait có thể tăng fitness trong environment này nhưng giảm trong environment khác. Vì vậy adaptation luôn có context.

## Hardy–Weinberg như baseline

Nếu một locus có hai allele A và a với tần số `p` và `q`, ta có:

```math
p+q=1
```

Trong ideal population không selection, mutation, migration, drift đáng kể và mating ngẫu nhiên, genotype frequency sau random mating là:

```math
p^2 + 2pq + q^2 = 1
```

Hardy–Weinberg equilibrium không mô tả một population “thực tế hoàn hảo”; nó là null model. Khi dữ liệu lệch khỏi expectation, ta hỏi process nào có thể tạo ra lệch đó.

> Mental model: Hardy–Weinberg giống control condition trong experiment. Nó cho ta biết population sẽ trông như thế nào nếu những evolutionary force chính không làm thay đổi allele frequency.

## Mutation, gene flow, drift và selection

Mutation tạo allele mới. Gene flow (유전자 흐름) đưa allele giữa population thông qua migration và reproduction. Genetic drift (유전적 부동) là thay đổi tần số allele do sampling ngẫu nhiên, đặc biệt mạnh ở population nhỏ. Selection thay đổi tần số vì khác biệt fitness.

Founder effect xảy ra khi population mới bắt đầu từ số ít individual. Bottleneck xảy ra khi population giảm mạnh, làm mất variation ngẫu nhiên. Cả hai đều có thể khiến allele frequency khác xa population ban đầu mà không cần selection.

## Natural selection có nhiều dạng

Directional selection làm distribution dịch về một phía. Stabilizing selection ưu tiên intermediate phenotype. Disruptive selection ưu tiên hai extreme hơn intermediate.

Frequency-dependent selection khiến fitness của phenotype phụ thuộc vào tần số của nó. Sexual selection phát sinh khi trait ảnh hưởng mating success, ngay cả khi có cost cho survival.

## Adaptation không đồng nghĩa perfection

Evolution làm việc với variation sẵn có và lịch sử cấu trúc đã tồn tại. Nó không bắt đầu từ zero và không có foresight. Constraint phát triển, trade-off và genetic correlation khiến organism thường là compromise.

Ví dụ pelvis người phải cân bằng locomotion hai chân với childbirth. Đây không phải “thiết kế lỗi” đơn giản mà là kết quả của nhiều selective pressure và historical constraint.

## Speciation

Loài (Species / 종) có nhiều cách định nghĩa. Biological species concept nhấn mạnh reproductive isolation, nhưng không áp dụng tốt cho asexual organism hay fossil.

Allopatric speciation xảy ra khi geographic separation giảm gene flow. Qua thời gian, mutation, drift và selection làm population diverge. Nếu reproductive isolation đủ mạnh, chúng có thể trở thành species khác.

Sympatric speciation có thể xảy ra không cần geographic barrier, ví dụ thông qua polyploidy ở plant hoặc ecological specialization.

## Phylogenetic thinking

Evolution tạo branching pattern, không phải ladder từ “thấp” lên “cao”. Species hiện đại không phải ancestor trực tiếp của nhau chỉ vì một species có vẻ đơn giản hơn.

Human và chimpanzee chia sẻ common ancestor; human không “tiến hóa từ chimpanzee hiện đại”. Đây là một misconception cực kỳ phổ biến.

## Selection ở gene, individual và group

Phần lớn evolutionary analysis có thể thực hiện ở gene hoặc individual level, nhưng một số phenomenon được nghiên cứu bằng multilevel selection framework. Điều quan trọng là xác định rõ level nào đang thay đổi frequency và mechanism nào tạo differential reproduction.

## Evolutionary medicine

Evolutionary thinking giúp giải thích antibiotic resistance, pathogen virulence, cancer evolution và trade-off của immune response. Antibiotic không “tạo” resistant bacteria theo hướng có mục đích; nó tạo selective environment nơi resistant variant có lợi thế lớn.

## Common misconceptions

“Survival of the fittest” không có nghĩa mạnh nhất sống sót. “Fittest” là reproductive success trong context.

“Evolution chỉ là theory” cũng hiểu sai nghĩa khoa học của theory. Scientific theory là framework giải thích được hỗ trợ bởi nhiều independent evidence, không phải phỏng đoán tùy ý.

## Kết nối

Raw material của evolution đến từ [[../02_genetics_molecular_biology/01_inheritance_variation_and_mutation]]. Genome-level evidence nằm trong [[../02_genetics_molecular_biology/02_genomics_epigenetics_and_regulation]]. Cây tiến hóa và biodiversity được phát triển trong [[01_phylogeny_taxonomy_and_biodiversity]]. Population dynamics nối sang [[../05_ecology/00_population_community_and_behavior]].
