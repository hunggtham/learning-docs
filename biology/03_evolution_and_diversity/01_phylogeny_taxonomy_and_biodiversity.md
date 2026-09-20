# Phylogeny, taxonomy và đa dạng sinh học — Phylogeny, Taxonomy and Biodiversity (계통·분류·생물다양성)

Nếu evolution tạo ra branching history của sự sống, phylogeny (Phylogeny / 계통) là nỗ lực tái dựng lịch sử phân nhánh đó. Taxonomy (분류학) đặt tên và phân loại organism, còn biodiversity (생물다양성) mô tả sự đa dạng ở cấp gene, species và ecosystem. Ba lĩnh vực liên hệ chặt nhưng không hoàn toàn đồng nhất.

## Cây tiến hóa là hypothesis về lịch sử chung

Phylogenetic tree không phải sơ đồ “loài nào cao cấp hơn”. Mỗi branch point đại diện một common ancestor giả định; các tip là lineage được sampling. Hai taxon có quan hệ gần hơn nếu chúng chia sẻ common ancestor gần hơn theo thời gian.

Clade (분기군) gồm ancestor và tất cả descendant của nó. Nhóm như vậy gọi là monophyletic. Paraphyletic group bỏ sót một số descendant; polyphyletic group gom organism từ nhiều lineage mà không gồm common ancestor gần nhất.

> Mental model: hãy đọc phylogenetic tree như Git commit graph của lịch sử sống. Vị trí trái–phải trên trang không nói “tiến bộ” hơn; topology của branch mới chứa information chính.

## Character và homology

Để dựng tree, ta so sánh character: morphology, protein sequence, DNA sequence hoặc genomic feature. Homologous trait (상동 형질) giống nhau vì shared ancestry. Analogous trait giống về function nhưng tiến hóa độc lập, thường qua convergent evolution.

Cánh chim và cánh insect đều dùng để bay nhưng không homologous như toàn bộ wing structure. Forelimb của human, whale và bat homologous vì cùng bắt nguồn từ tetrapod limb dù function khác nhau.

## Molecular phylogenetics

DNA sequence cung cấp lượng character lớn. Nếu hai lineage có nhiều nucleotide giống nhau hơn tại homologous region, đó có thể là evidence cho recent common ancestry, nhưng cần model substitution vì mutation rate khác nhau giữa site và lineage.

Maximum likelihood và Bayesian method đánh giá tree dựa trên probability model. Vì số lượng possible tree tăng cực nhanh theo số taxon, phylogenetics là một computational problem quan trọng.

## Molecular clock không phải đồng hồ tuyệt đối

Molecular clock dùng mutation/substitution accumulation để ước lượng divergence time. Nhưng rate không cố định tuyệt đối. Calibration từ fossil hoặc geological event thường cần thiết, và uncertainty phải được thể hiện.

## Taxonomy và naming

Hệ thống Linnaean truyền thống dùng domain, kingdom, phylum, class, order, family, genus, species. Binomial nomenclature đặt species name theo `Genus species`, ví dụ *Homo sapiens*.

Modern taxonomy ngày càng cố phản ánh phylogeny, nhưng naming system và evolutionary history không phải lúc nào khớp hoàn toàn vì classification có lịch sử và convention riêng.

## Ba domain lớn

Sinh vật cellular thường được chia thành Bacteria (세균), Archaea (고세균) và Eukarya (진핵생물). Archaea nhìn ngoài có thể giống bacteria vì đều prokaryotic, nhưng nhiều molecular machinery của chúng khác biệt sâu và một số đặc điểm gần Eukarya hơn.

Endosymbiosis giải thích vì sao mitochondria và chloroplast mang dấu vết bacterial ancestry.

## Biodiversity ở nhiều scale

Genetic diversity phản ánh variation trong một species. Species diversity gồm richness và distribution. Ecosystem diversity nói về variation của habitat, community và ecological process.

Biodiversity không chỉ có giá trị vì “nhiều loài là tốt”. Diversity ảnh hưởng resilience, nutrient cycling, pollination, food-web stability và khả năng ecosystem phản ứng với disturbance.

## Extinction là một phần của evolution, nhưng tốc độ matters

Phần lớn species từng tồn tại đã tuyệt chủng. Extinction có thể xảy ra do environment change, competition, catastrophe hoặc nhiều factor kết hợp.

Mass extinction khác background extinction ở scale và rate. Human-driven habitat loss, overexploitation, invasive species, pollution và climate change hiện tạo pressure lớn lên nhiều lineage.

## Species concept không có một định nghĩa duy nhất

Biological species concept tập trung reproductive isolation. Morphological species concept dựa vào hình thái. Phylogenetic species concept tìm smallest diagnosable lineage.

Không có concept nào hoàn hảo cho mọi organism. Asexual bacteria, hybridizing plants và fossil đều tạo boundary case. Đây là ví dụ quan trọng về cách scientific category phải phục vụ mục đích phân tích chứ không nhất thiết trùng đường biên tuyệt đối trong tự nhiên.

## Common misconceptions

“Human ở trên đỉnh cây tiến hóa” là sai. Tree không có “đỉnh” theo nghĩa giá trị. Mọi species hiện sống đều có lịch sử tiến hóa dài tương đương tính từ common ancestry sâu.

“Loài hiện đại là hóa thạch sống không thay đổi” cũng thường bị dùng quá mức. Một lineage có morphology tương đối ổn định vẫn có thể tích lũy genomic và ecological change đáng kể.

## Kết nối

Cơ chế làm lineage thay đổi nằm trong [[00_evolution_and_population_genetics]]. Cell architecture và endosymbiosis quay lại [[../01_cell_biology/00_cells_membranes_and_transport]]. Biodiversity trở thành đối tượng trực tiếp của [[../05_ecology/01_ecosystems_biogeochemical_cycles_and_conservation]].
