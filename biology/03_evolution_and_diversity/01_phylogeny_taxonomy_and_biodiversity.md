# Phylogeny, Taxonomy và Đa dạng sinh học — Phylogeny, Taxonomy and Biodiversity (계통학, 분류학과 생물다양성)

Evolution cho ta một hình ảnh quan trọng: history của life không phải chiếc thang mà là **cây phân nhánh**. Population tách ra, divergence tích lũy, lineage mới hình thành. Chapter này trả lời ba câu hỏi nối tiếp nhau: làm sao reconstruct cây lịch sử đó, làm sao đặt tên/phân loại organism theo ancestry, và biodiversity hiện tại được tổ chức ra sao?

> **Mental model:** phylogeny là hypothesis về lịch sử phân nhánh; taxonomy là hệ thống tên/phân loại cố gắng phản ánh history đó; biodiversity là kết quả hiện tại của hàng tỷ năm branching, extinction và ecological diversification.

## 1. Tree of life không phải “thứ bậc tiến hóa”

Một phylogenetic tree gồm node và branch. Node trong tree thường biểu diễn common ancestor; tip là lineage/species sampled.

Hai tip nằm cạnh nhau trên hình không nhất thiết “giống nhau hơn”; điều quan trọng là **most recent common ancestor**.

Không có tip nào “cao cấp hơn” tip khác. Human và chimpanzee đều là lineage hiện đại, mỗi bên có history riêng từ common ancestor.

## 2. Cách đọc một tree đúng

Nếu node chia thành A và B, A và B là **sister taxa**. Một group gồm ancestor và toàn bộ descendant gọi là **clade (nhánh đơn ngành / 단계통군)**.

Tree có thể rotate quanh node mà relationship không đổi. Vì vậy order trái–phải của tip thường không mang meaning evolutionary progress.

Branch length chỉ có meaning nếu tree được scale theo amount change hoặc time; không phải mọi tree đều như vậy.

## 3. Homology và analogy

**Homologous structure (구조적 상동성)** giống nhau do shared ancestry. Forelimb của human, bat và whale có same basic bone pattern vì thừa hưởng từ tetrapod ancestor.

**Analogous/convergent feature** có function tương tự nhưng evolve độc lập, như wing của bird và insect.

Phân biệt homology với convergence cực kỳ quan trọng khi reconstruct tree.

## 4. Shared derived character

Phylogenetic inference tìm **shared derived characters (synapomorphy / 공유파생형질)** — trait xuất hiện ở common ancestor gần và được descendant chia sẻ.

Một trait ancestral quá rộng thường không giúp phân giải relationship gần.

Ví dụ vertebral column giúp define vertebrate clade nhưng không phân biệt mammal species với nhau.

## 5. Molecular phylogenetics

DNA/protein sequence cung cấp rất nhiều character. Nếu sequence tương đồng do common ancestry, pattern mutation có thể giúp suy tree.

Nhưng gene tree có thể khác species tree do incomplete lineage sorting, introgression hoặc horizontal gene transfer.

Một gene không phải luôn đại diện toàn history của species.

## 6. Sequence alignment là bước reasoning chứ không chỉ thao tác kỹ thuật

Trước khi so difference, ta cần align nucleotide/amino acid sao cho position tương ứng homologous được đặt cạnh nhau.

Insertion/deletion làm alignment không trivial. Algorithm dùng scoring cho match, mismatch, gap.

Bad alignment có thể tạo false phylogenetic signal. Đây là connection trực tiếp với bioinformatics.

## 7. Parsimony, likelihood và Bayesian inference

**Maximum parsimony** chọn tree cần ít evolutionary change nhất theo model đơn giản.

**Maximum likelihood** hỏi tree/model nào làm observed sequence data có probability cao nhất.

**Bayesian phylogenetics** kết hợp prior với likelihood để suy posterior distribution của tree/parameter.

Không có method “nhìn data rồi tree tự xuất hiện”; mỗi inference dựa trên model mutation/evolution.

## 8. Support cho branch

Bootstrap resampling hoặc posterior probability được dùng đánh giá support của clade.

Support cao không có nghĩa tree chắc chắn tuyệt đối; nó phản ánh stability/probability dưới data và model đã dùng.

Uncertainty nên được giữ lại thay vì ép mọi branch thành certainty.

## 9. Molecular clock

Nếu substitution tích lũy gần đều theo time ở marker phù hợp, sequence divergence có thể estimate split time.

Nhưng rate thay đổi giữa lineage/gene. Calibration bằng fossil hoặc geological event cần thiết.

Clock là model có error bar, không phải đồng hồ literal.

## 10. Taxonomy: đặt tên để communication ổn định

**Taxonomy (phân loại học / 분류학)** đặt tên và group organism.

Binomial nomenclature dùng genus + species, ví dụ *Homo sapiens*.

Hierarchy truyền thống: Domain → Kingdom → Phylum → Class → Order → Family → Genus → Species.

Nhưng modern classification ngày càng ưu tiên clade và phylogeny hơn rigid rank.

## 11. Three domains

Life cellular hiện đại thường được chia ba domain: **Bacteria, Archaea, Eukarya**.

Archaea từng bị gộp với bacteria vì đều prokaryotic, nhưng molecular data cho thấy Archaea có nhiều feature information-processing gần Eukarya hơn theo một số hệ.

Đây là ví dụ molecular phylogeny thay đổi taxonomy.

## 12. Bacteria: metabolic diversity khổng lồ

Bacteria không phải synonym “germ gây bệnh”. Phần lớn bacteria không pathogenic; nhiều species essential trong nutrient cycle, microbiome và biotechnology.

Bacteria có cell architecture prokaryotic nhưng metabolism rất đa dạng: aerobic/anaerobic respiration, fermentation, photosynthesis, chemolithotrophy.

## 13. Archaea: không chỉ organism sống ở cực hạn

Một số Archaea là extremophile, nhưng rất nhiều sống trong ocean, soil và microbiome bình thường.

Methanogen là group đặc biệt tạo methane trong anaerobic environment.

Archaea cho thấy morphology “nhìn giống bacteria” không đồng nghĩa close evolutionary relationship.

## 14. Eukarya và major lineage

Eukarya gồm animal, plant, fungi và nhiều protist lineage.

“Protist” thường là convenience category hơn clade tự nhiên duy nhất.

Modern phylogeny cho thấy eukaryotic diversity sâu hơn classification schoolbook kingdom đơn giản.

## 15. Plant diversity như history của transition lên land

Green plant ancestry bắt đầu aquatic. Land colonization tạo challenge: tránh mất water, support body, transport, reproduction không phụ thuộc hoàn toàn water.

Bryophyte, vascular plant, seed plant và flowering plant phản ánh các innovation như vascular tissue, seed, pollen, flower/fruit.

Plant biology chapter sẽ xem mechanism của những innovation này.

## 16. Fungi: absorptive heterotroph và network hyphae

Fungi không phải plant. Chúng lấy nutrient bằng secretion enzyme ra môi trường rồi absorb product.

Hypha tạo mycelium với surface area lớn, rất phù hợp decomposition và symbiosis.

Mycorrhiza nối fungi với plant root, ảnh hưởng nutrient acquisition và ecosystem nutrient cycle.

## 17. Animal diversity và body plan

Animal evolution tạo nhiều body plan khác nhau về symmetry, tissue layer, body cavity, segmentation và development.

Không cần học toàn taxonomy trước để hiểu principle: developmental program và gene regulation tạo architecture body; selection và history tạo diversification.

Vertebrate chỉ là một nhánh nhỏ trong animal diversity.

## 18. Biodiversity có nhiều cấp

**Đa dạng sinh học (biodiversity / 생물다양성)** gồm ít nhất:

- genetic diversity trong species;
- species diversity trong community;
- ecosystem diversity trên landscape.

Mất biodiversity không chỉ là “mất số loài”. Loss genetic diversity làm population khó adapt; loss functional group có thể đổi ecosystem process.

## 19. Species richness và evenness

Community có thể có cùng số species nhưng distribution abundance rất khác.

**Richness** là số species; **evenness** phản ánh abundance phân bố đều đến đâu.

Diversity index kết hợp hai dimension, nhưng choice metric phụ thuộc question.

## 20. Extinction là phần tự nhiên của evolution nhưng rate quan trọng

Lineage luôn xuất hiện và biến mất trong history. Mass extinction là period mất diversity rất nhanh ở geological scale.

Sau extinction, ecological niche trống có thể tạo adaptive radiation ở surviving lineage.

Current extinction concern không phải vì “extinction chưa từng xảy ra”, mà vì rate, cause và consequence đối với ecosystem/human society.

## 21. Adaptive radiation

Khi lineage tiếp cận nhiều niche mới, diversification có thể nhanh. Island colonization hoặc key innovation có thể mở ecological opportunity.

Darwin’s finches thường được dùng minh họa beak diversification theo food niche.

Phylogeny + ecology cùng giải thích pattern.

## 22. Convergent evolution

Environment tương tự có thể favor solution tương tự ở lineage xa nhau.

Streamlined body ở shark, ichthyosaur extinct và dolphin là convergence do hydrodynamic constraint, không phải close ancestry.

Convergence nhắc ta không suy tree chỉ từ superficial similarity.

## 23. Horizontal gene transfer làm tree of life thành network ở microbes

Bacteria/Archaea có thể trao đổi gene qua transformation, transduction, conjugation.

Vì vậy một gene như antibiotic resistance có history khác organism lineage.

Ở deep microbial evolution, “tree” đôi khi cần bổ sung network reticulation.

## 24. Endosymbiosis và chimeric history của eukaryote

Mitochondria bắt nguồn từ bacterial endosymbiont; chloroplast từ cyanobacterial lineage.

Eukaryotic cell vì vậy mang genetic/history component từ nhiều lineage.

Evolution không chỉ phân nhánh; đôi khi lineage merge qua symbiosis.

## 25. Biogeography

Distribution species trên Earth chứa evidence history. Island species thường gần relative trên mainland/nearby island nhưng diverge sau isolation.

Continental drift cũng giải thích pattern fossil/living species.

Biogeography nối evolution với geology và ecology.

## 26. Conservation cần phylogeny

Nếu phải ưu tiên conservation, giữ evolutionary distinct lineage có thể bảo tồn nhiều unique history/function hơn chỉ đếm species.

Phylogenetic diversity là một dimension của biodiversity planning.

Nhưng conservation decision còn phụ thuộc ecology, social value và uncertainty; không có một metric duy nhất quyết định mọi thứ.

## 27. Case study: whale vẫn là mammal

Whale sống dưới nước và body streamlined giống fish ở superficial level, nhưng anatomy, development và molecular phylogeny đặt whale trong mammals, gần hippo hơn fish.

Convergent adaptation với aquatic environment làm body shape giống fish.

Tree thinking giúp phân biệt ancestry với function.

## 28. Case study: giant panda taxonomy

Morphology/diet từng gây tranh luận relation của giant panda. Molecular evidence đặt giant panda trong bear family, còn red panda ở lineage riêng gần musteloid group hơn.

DNA data có thể resolve ambiguity mà morphology đơn độc khó giải.

## 29. Common misconceptions

“Tree tip nằm cao hơn là tiến hóa hơn” sai.

“Species hiện đại là ancestor trực tiếp của species hiện đại khác” thường sai; chúng share ancestor đã extinct hoặc ancestral population.

“Taxonomy là hệ thống cố định từ Linnaeus” sai; classification đổi theo evidence phylogeny.

“Bacteria là một nhóm organism primitive ít diversity” sai.

“Giống morphology = gần họ” có thể sai vì convergence.

## 30. Bridge: microbe và virus làm evolutionary rule trở nên rõ nhất

Phylogeny cho ta map diversity, nhưng microbes đặt ra những câu hỏi đặc biệt: generation time ngắn, population cực lớn, horizontal gene transfer mạnh, metabolism đa dạng, virus phụ thuộc host nhưng evolution nhanh.

[[02_microorganisms_and_viruses]] sẽ dùng chính cell biology, genetics và evolution vừa học để hiểu microbial life và virus.

Sau đó organismal biology sẽ chuyển sang câu hỏi khác: multicellular lineage giải bài toán transport, control và development ở whole-organism scale thế nào?

> **Mental model cuối chapter:** biodiversity không phải catalog tĩnh. Nó là snapshot của branching history cộng extinction, convergence, migration và ecological diversification. Phylogenetic tree là model để reconstruct history đó từ evidence, không phải chiếc thang xếp organism từ thấp tới cao.