# Phát sinh chủng loại, phân loại và đa dạng sinh học — Phylogeny, Taxonomy and Biodiversity (계통, 분류와 생물다양성)

Evolutionary change ở population tạo divergence; divergence kéo dài tạo lineage; lineage tách nhánh qua thời gian tạo nên **cây sự sống (tree of life)**. Vì vậy phylogeny không phải một chương “học tên các nhóm sinh vật” đứng riêng. Nó là cách biểu diễn lịch sử phân nhánh được tạo ra từ chính các process của evolution.

## 1. Phylogeny là lịch sử quan hệ, không phải thang tiến bộ

**Phylogeny (phát sinh chủng loại / 계통)** mô tả evolutionary relationship giữa lineage.

Một phylogenetic tree có node biểu diễn common ancestor và branch biểu diễn lineage.

Sai lầm phổ biến là đọc tree như thang từ “thấp” lên “cao”. Nhưng tree không có hướng tiến bộ như vậy. Hai species hiện đại cùng ở đầu branch và đều đã evolution từ common ancestor qua cùng khoảng thời gian lịch sử.

Con người không “tiến hóa từ khỉ hiện đại”; human và các ape hiện đại chia sẻ common ancestor.

## 2. Cách đọc một tree đúng

Điều quan trọng là pattern branching, không phải vị trí trái/phải của species trên trang.

Nếu A và B chia sẻ common ancestor gần hơn so với C, A và B là sister taxa.

Xoay branch quanh node không thay relationship.

```text
      ┌─ A
  ┌───┤
  │   └─ B
──┤
  └───── C
```

Tree này nói A và B có common ancestor gần hơn nhau so với C.

## 3. Homology và analogy

Để reconstruct relationship, ta tìm **homologous character (đặc điểm tương đồng do chung nguồn gốc / 상동형질)**.

Human arm, bat wing và whale flipper có bone pattern tương đồng vì thừa hưởng từ tetrapod ancestor, dù function khác.

Ngược lại, bird wing và insect wing đều dùng để bay nhưng origin khác; similarity này phần lớn là **analogy** do convergent evolution.

Nếu nhầm analogy với homology, ta có thể suy tree sai.

## 4. Shared derived character và clade

Một **clade (분기군)** gồm common ancestor và toàn bộ descendant.

Ta ưu tiên character xuất hiện ở ancestor của clade rồi được truyền xuống descendant — **shared derived character**.

Ví dụ hair là derived trait hữu ích để nhận diện Mammalia trong context vertebrate tree.

Cladistics vì vậy cố group organism theo common ancestry, không chỉ similarity tổng quát.

## 5. Molecular phylogenetics

Morphology rất hữu ích nhưng có limitation. DNA/protein sequence cung cấp hàng nghìn character để so sánh.

Nếu hai sequence khác ít hơn, chúng thường có common ancestor gần hơn — nhưng phải dùng model vì mutation rate khác nhau giữa site và lineage.

Alignment đặt position homolog cạnh nhau. Sau đó algorithm như maximum likelihood hoặc Bayesian inference estimate tree phù hợp data và model.

Điều này nối phylogeny với bioinformatics và statistics.

## 6. Molecular clock: useful nhưng không phải đồng hồ hoàn hảo

Nếu sequence change với rate tương đối ổn định, genetic distance có thể giúp estimate divergence time.

Nhưng rate không hoàn toàn constant. Generation time, selection, gene region và lineage đều ảnh hưởng.

Vì vậy molecular clock cần calibration, thường bằng fossil hoặc geological event.

Model luôn đi kèm assumption — principle từ chapter đầu quay lại.

## 7. Taxonomy: đặt tên để phản ánh relationship

**Taxonomy (phân loại học / 분류학)** đặt tên và group organism.

Traditional ranks gồm domain, kingdom, phylum, class, order, family, genus, species.

Binomial nomenclature dùng genus + species, ví dụ *Homo sapiens*.

Modern taxonomy ngày càng cố phản ánh phylogeny. Nếu một group bỏ sót descendant của common ancestor, classification có thể gây misleading.

## 8. Three domains: Bacteria, Archaea, Eukarya

Ribosomal RNA sequence cho thấy cellular life hiện nay có ba domain lớn: **Bacteria**, **Archaea**, **Eukarya**.

Archaea ban đầu dễ bị nhìn như “bacteria lạ”, nhưng molecular data cho thấy nhiều system processing information của archaea gần eukaryote hơn bacteria.

Điều này là ví dụ khoa học thay đổi classification khi evidence mới xuất hiện.

## 9. Endosymbiosis nối tree với cell biology

Mitochondria có origin từ bacterial lineage được ancestral eukaryotic cell engulfed. Chloroplast có origin từ cyanobacteria-like lineage.

Do đó evolutionary history không phải lúc nào cũng tree đơn giản. Có những event gene transfer và symbiosis tạo network-like history.

Cell biology ở [[../01_cell_biology/00_cells_membranes_and_transport]] vì thế mang dấu vết phylogeny.

## 10. Horizontal gene transfer làm microbial evolution đặc biệt

Bacteria có thể nhận gene qua transformation, transduction hoặc conjugation.

Gene có thể đi ngang giữa lineage thay vì chỉ từ parent xuống offspring.

Điều này làm history của một gene không nhất thiết giống history toàn organism.

Antibiotic-resistance gene có thể lan nhanh giữa species qua plasmid.

## 11. Biodiversity có nhiều tầng

**Biodiversity (đa dạng sinh học / 생물다양성)** không chỉ là số species.

Ta có thể nói genetic diversity trong species, species diversity trong community và ecosystem diversity trên landscape.

Các tầng liên kết: genetic diversity giúp population có raw variation để respond environment; species diversity ảnh hưởng interaction network; ecosystem diversity tạo nhiều habitat.

## 12. Species concept và boundary không phải lúc nào cũng rõ

Biological species concept dùng reproductive isolation nhưng khó dùng với fossil hay asexual organism.

Phylogenetic species concept nhấn lineage riêng biệt.

Morphological concept dùng trait observable.

Hybridization cũng làm boundary mờ ở một số group.

Do đó “species” là model hữu ích nhưng nature không luôn chia thành box sắc nét.

## 13. Extinction là một phần của tree

Hầu hết lineage từng tồn tại đã extinct.

Tree hiện tại chỉ là phần survivor của lịch sử lớn hơn.

Mass extinction thay composition biosphere và mở ecological opportunity cho lineage còn lại.

Diversity hiện nay vì thế phản ánh cả origin lẫn loss.

## 14. Diversity nối với ecology

Một species không chỉ có vị trí trên tree; nó còn có **niche**, interaction, resource use và role trong ecosystem.

Evolutionary history ảnh hưởng ecological trait. Closely related species có thể share physiology và vulnerability.

Ngược lại, ecological interaction tạo selection pressure tiếp tục shape evolution.

Evolution và ecology tạo feedback qua nhiều generation.

## 15. Từ tree đến microorganism: vì sao cần zoom vào microbial world?

Nếu chỉ học plant và animal, ta bỏ qua phần lớn metabolic và genetic diversity của life.

Bacteria và archaea thực hiện nhiều reaction nền của carbon/nitrogen cycle. Microbiome ảnh hưởng host. Virus ảnh hưởng evolution và gene transfer.

Do đó bước tiếp theo là zoom vào microbial scale, nơi cell biology, genetics, evolution và ecology gặp nhau.

Tiếp tục với [[02_microorganisms_and_viruses]].