# Tiến hóa và Di truyền quần thể — Evolution and Population Genetics (진화와 집단유전학)

Genetics cho ta allele, mutation, meiosis và inheritance. Nhưng evolution không hỏi chủ yếu “một cá thể mang allele nào?”, mà hỏi: **sau nhiều thế hệ, tần số allele trong quần thể thay đổi vì những lực nào?** Đây là chuyển đổi từ individual-scale sang population-scale.

> **Mental model:** evolution là thay đổi heritable composition của population qua thời gian. Mutation tạo variation mới; recombination shuffle variation; selection, drift và gene flow thay frequency của variation; speciation xuất hiện khi lineage diverge đủ lâu.

## 1. Population là đơn vị tư duy trung tâm

**Quần thể (population / 개체군)** là nhóm cá thể cùng loài có khả năng giao phối/trao đổi gene trong cùng hệ tương đối liên kết.

Individual không “evolve” trong đời theo nghĩa population genetics. Individual có thể acclimate, learn hoặc thay physiology; evolution là change distribution across generations.

Nếu allele A có frequency \(p\) và allele a có frequency \(q\), với hai allele:

\[
p+q=1
\]

Population genetics theo dõi các frequency này.

## 2. Hardy–Weinberg: null model để biết khi nào population không đổi

Nếu một diploid population lý tưởng có random mating, không selection, không mutation, không migration và effectively infinite size, genotype frequency sau mating là:

\[
p^2+2pq+q^2=1
\]

Trong đó \(p^2\) là AA, \(2pq\) là Aa, \(q^2\) là aa.

Hardy–Weinberg không mô tả thế giới “đúng” mà là **null model**. Khi data lệch expectation, ta hỏi assumption nào bị vi phạm.

Đây là cách model giúp reasoning: xây baseline đơn giản rồi đo deviation.

## 3. Mutation: nguồn cuối cùng của allele mới

Mutation rate thường nhỏ mỗi locus mỗi generation nhưng genome/population rất lớn nên variation liên tục xuất hiện.

Mutation không xuất hiện vì organism cần adaptation. Nó tạo raw variation; environment và population process quyết định fate.

Một mutation beneficial có thể mất bởi chance khi còn rare. Một neutral mutation có thể tăng frequency bởi drift. “Có lợi” không đồng nghĩa “chắc chắn lan rộng”.

## 4. Natural selection: differential reproduction, không phải survival đơn thuần

**Chọn lọc tự nhiên (natural selection / 자연선택)** xảy ra khi heritable variation làm cá thể để lại số descendant khác nhau trong environment cụ thể.

**Fitness (적합도)** trong evolutionary biology liên quan reproductive contribution tương đối, không phải “khỏe” theo nghĩa thường.

Một trait tăng survival nhưng làm reproduction giảm có thể không tăng total fitness. Selection luôn context-dependent.

## 5. Selection coefficient và relative fitness

Nếu genotype có relative fitness 1 và genotype khác 0.9, difference có thể biểu diễn selection coefficient \(s=0.1\) trong model đơn giản.

Nhưng real fitness phụ thuộc sex, age, environment và frequency trait. Model giúp định lượng, không nên nhầm với constant universal.

## 6. Directional, stabilizing và disruptive selection

Directional selection favor một phía phenotype distribution. Stabilizing selection favor intermediate, giảm extreme. Disruptive selection favor extreme hơn intermediate trong context nhất định.

Những label này mô tả pattern selection trên phenotype, không phải mechanism genetic cụ thể.

## 7. Frequency-dependent selection

Fitness của phenotype có thể phụ thuộc nó phổ biến đến đâu.

Trong **negative frequency-dependent selection**, rare type có advantage vì predator/parasite chưa thích nghi hoặc competition khác. Điều này có thể duy trì diversity.

Selection vì vậy không luôn “đẩy một allele tốt nhất tới fixation”.

## 8. Sexual selection

Trait tăng mating success có thể được favored dù có cost survival. Peacock tail là ví dụ classic.

Sexual selection gồm competition trong cùng sex và mate choice, nhưng pattern rất đa dạng giữa species.

Nó giải thích một số trait khó hiểu nếu chỉ xét survival efficiency.

## 9. Genetic drift: randomness mạnh khi population nhỏ

**Trôi dạt di truyền (genetic drift / 유전적 부동)** là change allele frequency do sampling randomness.

Nếu population nhỏ, generation sau chỉ là sample nhỏ của gamete generation trước; random fluctuation có thể lớn.

Drift có thể fix hoặc mất neutral allele mà không cần selection.

> Selection là biased sampling theo fitness; drift là stochastic sampling.

Hai lực hoạt động đồng thời.

## 10. Effective population size

Actual census size và **effective population size \(N_e\)** không giống nhau. Sex ratio lệch, variation reproductive success hay bottleneck làm \(N_e\) thấp hơn census size.

Drift strength liên hệ \(N_e\), vì nó phản ánh số cá thể thực sự góp gene vào generation sau.

## 11. Bottleneck và founder effect

**Bottleneck** xảy ra khi population giảm mạnh, làm diversity mất ngẫu nhiên.

**Founder effect** xảy ra khi một nhóm nhỏ lập population mới; allele frequency của nhóm founder có thể khác source population.

Cả hai là special case drift, không phải selection.

Một allele tăng sau bottleneck không có nghĩa nó adaptive.

## 12. Gene flow: population không phải đảo genetic kín

Migration và mating giữa population tạo **gene flow (유전자 이동)**.

Gene flow thường làm population giống nhau hơn và đưa allele mới vào population. Nhưng nếu local selection mạnh, differentiation vẫn có thể duy trì.

Evolution landscape là kết quả competition giữa gene flow, selection và drift.

## 13. Recombination: không tạo allele mới nhưng tạo genotype mới

Recombination phá association giữa allele và tạo haplotype mới. Nó giúp selection act trên combination khác nhau hiệu quả hơn trong nhiều context.

Linkage làm nearby locus chia sẻ history. Recombination rate ảnh hưởng pattern linkage disequilibrium trong genome.

Genomics và evolution gặp nhau trực tiếp ở đây.

## 14. Adaptation không có foresight

Natural selection không “thiết kế” trait cho future. Variation tồn tại hoặc xuất hiện; current environment tạo differential reproduction.

Evolution cũng bị constraint bởi ancestry. Organism sửa đổi structure sẵn có hơn là thiết kế lại từ zero.

Whale flipper, bat wing và human arm có homologous bone plan vì cùng tetrapod ancestry dù function khác.

## 15. Trade-off và evolutionary compromise

Resource hữu hạn. Investment vào growth, reproduction, immunity và maintenance có trade-off.

Trait tối ưu cho một environment có thể bất lợi trong environment khác. Hemoglobin allele liên quan sickle-cell/malaria là ví dụ context-dependent fitness.

Evolution thường tạo compromise chứ không tạo perfect organism.

## 16. Local adaptation

Population sống ở environment khác nhau có thể evolve khác nhau nếu local selection vượt gene flow.

Plant ở altitude cao, fish ở salinity khác hoặc pathogen trong host khác có thể thích nghi local.

Nhưng để kết luận adaptation cần evidence beyond phenotype difference; common-garden/reciprocal-transplant experiment giúp tách genetic effect khỏi plasticity.

## 17. Phenotypic plasticity và evolution không giống nhau

**Plasticity (표현형 가소성)** là cùng genotype tạo phenotype khác theo environment.

Ví dụ plant leaf shape, acclimation heat hay muscle training có thể thay phenotype trong đời mà không đổi allele frequency.

Plasticity itself có genetic basis và có thể evolve, nhưng response trong một individual không phải evolution.

## 18. Speciation: khi gene flow giảm và lineage diverge

**Hình thành loài (speciation / 종분화)** xảy ra khi population divergence dẫn tới reproductive isolation đủ mạnh.

Allopatric speciation thường bắt đầu bằng geographic separation. Sympatric speciation xảy ra không cần barrier địa lý hoàn toàn, ví dụ polyploidy ở plant hoặc ecological divergence mạnh.

Speciation là process, không nhất thiết có một instant “ngày sinh loài mới”.

## 19. Reproductive isolation

Prezygotic barrier ngăn mating/fertilization: time, behavior, habitat, mechanical/gametic incompatibility.

Postzygotic barrier làm hybrid viability/fertility giảm.

Barrier có thể accumulate khi population diverge.

## 20. Species concept và giới hạn

Biological species concept dựa reproductive isolation hữu ích cho sexual organism, nhưng khó áp dụng bacteria, asexual organism hoặc fossil.

Morphological, ecological và phylogenetic species concept giải quyết câu hỏi khác.

Không có một definition loài hoàn hảo cho mọi life form; species là scientific model về lineage boundary.

## 21. Molecular evolution

DNA sequence thay đổi theo mutation, selection và drift. Một số site chịu strong purifying selection nên conserved; site khác evolve nhanh hơn.

Synonymous/nonsynonymous substitution comparison có thể gợi ý selective pressure, nhưng interpretation cần model đúng.

Conservation across species thường giúp identify functionally constrained region.

## 22. Molecular clock

Nếu mutation/substitution accumulate với rate tương đối ổn định ở marker/context, sequence difference có thể dùng estimate divergence time.

Nhưng rate không universal; calibration bằng fossil/geological event và model variation cần thiết.

Molecular clock là model có assumption, không phải đồng hồ tuyệt đối.

## 23. Coevolution

Species tương tác tạo reciprocal selection. Host–pathogen, flower–pollinator, predator–prey có thể coevolve.

“Arms race” là một pattern nhưng không phải mọi interaction. Mutualism cũng có coevolution.

Evolution xảy ra trong network ecological, không trong vacuum.

## 24. Evolution of antibiotic resistance

Bacterial population có variation do mutation và horizontal gene transfer. Antibiotic tạo strong selection: susceptible cell giảm, resistant lineage tăng.

Resistance có thể có cost khi antibiotic absent; compensatory mutation có thể giảm cost.

Misuse antibiotic tăng selection exposure và spread resistance, nhưng mechanism luôn đi qua population variation + differential reproduction.

## 25. Evolutionary medicine

Một số disease vulnerability được hiểu tốt hơn khi hỏi evolutionary history.

Fever có thể là regulated defense response; pathogen virulence chịu trade-off transmission; modern diet/lifestyle có thể tạo mismatch với physiology evolved trong past environment.

Evolutionary explanation không thay proximate mechanism. Hai level bổ sung nhau: “cơ chế gây symptom?” và “vì sao system có vulnerability này?”.

## 26. Phylogenetic thinking bắt đầu từ common ancestry

Nếu species share common ancestor, trait similarity có thể do inherited homology chứ không phải independent adaptation.

Khi so sánh species, sample không statistically independent hoàn toàn vì shared ancestry. Comparative biology cần phylogenetic context.

Điều này dẫn thẳng sang chapter phylogeny.

## 27. Case study: Darwin’s finches

Beak morphology thay đổi liên quan food environment. Drought có thể thay seed distribution, làm individual với beak phù hợp có reproductive success khác.

Qua generation, trait distribution có thể shift.

Điểm lesson không phải “finch biến mỏ vì cần”, mà là pre-existing heritable variation + environmental selection.

## 28. Case study: lactase persistence

Regulatory variant duy trì lactase expression adulthood tăng frequency ở một số population có cultural history dùng dairy.

Example này cho thấy gene–culture coevolution: human behavior thay environment selection, selection lại thay allele frequency.

Biology và culture có causal loop.

## 29. Common misconceptions

“Evolution = tiến bộ từ thấp lên cao” sai; evolution không có mục tiêu universal.

“Survival of the fittest = mạnh nhất sống” sai; fitness là reproductive contribution trong context.

“Selection tạo mutation cần thiết” sai.

“Drift chỉ là error không quan trọng” sai; drift là lực tiến hóa mạnh ở population nhỏ.

“Individual evolve trong đời” sai theo population-genetic sense.

“Loài có boundary tuyệt đối” không luôn đúng, nhất là hybridization/microbes.

## 30. Bridge: nếu lineage phân nhánh, ta reconstruct lịch sử đó như thế nào?

Evolution tạo branching history. Nhưng present-day species chỉ cho ta endpoint; fossil, morphology và sequence là evidence để suy tree.

[[01_phylogeny_taxonomy_and_biodiversity]] sẽ xây cách đọc phylogenetic tree, homology, taxonomy và biodiversity.

Sau đó [[02_microorganisms_and_viruses]] sẽ cho thấy evolution hoạt động đặc biệt nhanh và linh hoạt ở microbe nhờ huge population, short generation và horizontal gene transfer.

> **Mental model cuối chapter:** population genetics là mechanics của evolution. Mutation tạo variation, selection tạo bias, drift tạo stochastic change, gene flow nối population, recombination shuffle genome. Từ các lực đơn giản này, lineage có thể diverge và tạo biodiversity qua thời gian sâu.