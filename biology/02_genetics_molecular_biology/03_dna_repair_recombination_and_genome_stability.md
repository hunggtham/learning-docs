# Sửa chữa DNA, tái tổ hợp và ổn định genome — DNA Repair, Recombination and Genome Stability (DNA 복구, 재조합과 유전체 안정성)

Sau khi học DNA replication, biểu hiện gen (gene expression), inheritance và đột biến (mutation), một câu hỏi quan trọng xuất hiện: **nếu DNA luôn bị chemical damage và replication không hoàn hảo, vì sao genome vẫn đủ ổn định để cell sống nhiều năm và lineage tồn tại qua hàng triệu generation?** Câu trả lời là genome không phải một “file read-only”. Nó được proofread, kiểm tra, sửa chữa, tái tổ hợp, đóng gói và đôi khi hy sinh cả tế bào (cell) để bảo vệ sinh vật (organism).

Chapter này nối những chủ đề thường bị học tách rời: độ chính xác sao chép (replication fidelity), Tổn thương DNA (DNA damage), đột biến, tái tổ hợp (recombination), nhiễm sắc thể (chromosome) kiến trúc (architecture), điểm kiểm soát chu kỳ tế bào (cell-cycle checkpoint), lão hóa (aging), cancer và tiến hóa (evolution). Nhìn chung, chúng đều xoay quanh một trade-off: **information phải đủ ổn định để phenotype hoạt động, nhưng variation vẫn phải tồn tại để evolution xảy ra.**

> **Mô hình tư duy (mental model):** độ ổn định hệ gen (genome stability) không có nghĩa genome không thay đổi. Nó có nghĩa cell quản lý change: sửa phần lớn damage, cho phép một số variation tồn tại, và kích hoạt checkpoint hoặc chết tế bào (cell death) khi risk vượt ngưỡng.

## 1. Tổn thương DNA là trạng thái bình thường của một molecule sống trong chemistry hoạt động

DNA bị hỏng không chỉ do radiation hay toxin. Water có thể thúc đẩy hydrolysis; base có thể deaminate; reactive oxygen species từ metabolism có thể oxidize nucleotide; chạc sao chép (replication fork) có thể stall; chromosome có thể bị mechanical stress khi segregation.

Vì vậy mỗi cell sống trong **damage–repair balance** liên tục. Đây là điểm quan trọng: repair system không chỉ là emergency response. Nó là infrastructure thường trực giống hệ thống bảo trì của một mạng máy tính luôn hoạt động.

Cần phân biệt **Tổn thương DNA (tổn thương DNA / DNA 손상)** với **đột biến (đột biến / 돌연변이)**. Damage là trạng thái hóa học hoặc structural abnormality. Nếu được sửa đúng, trình tự (sequence) ban đầu được khôi phục. Mutation là sequence change đã trở thành ổn định qua sao chép (replication). Damage có thể dẫn tới mutation, nhưng hai khái niệm không đồng nghĩa.

## 2. Độ chính xác sao chép bắt đầu ngay tại DNA polymerase

DNA polymerase chọn nucleotide dựa trên complementarity và geometry của trung tâm hoạt động (active site). Nhưng base pairing không hoàn hảo tuyệt đối; misincorporation vẫn xảy ra.

Nhiều polymerase có **đọc sửa (proofreading) (교정 기능)** qua 3'→5' exonuclease activity. Khi nucleotide sai làm geometry bất thường, polymerase có thể lùi lại, cắt nucleotide đó rồi tiếp tục synthesis.

Mô hình tư duy hữu ích là replication có nhiều lớp defense:

```text
base selection
→ polymerase proofreading
→ post-replication mismatch repair
→ checkpoint nếu damage vẫn còn
```

Mỗi layer giảm error thêm một bậc. Đây là redundancy có chủ đích: information quan trọng đến mức evolution đầu tư nhiều mechanism độc lập để bảo vệ nó.

## 3. Tỉ lệ lỗi (error rate) và genome size liên kết toán học

Nếu probability lỗi mỗi base là \(\mu\) và genome segment có chiều dài \(L\), xác suất một copy không có lỗi trong approximation đơn giản là:

\[
Q=(1-\mu)^L
\]

Khi \(L\) tăng, cùng tỉ lệ lỗi sẽ tạo nhiều lỗi tuyệt đối hơn. Điều đó giải thích vì sao organism có genome lớn cần độ chính xác sao chép và repair mạnh hơn. Nó cũng nối trực tiếp với [Nguồn gốc sự sống và tiến hóa sớm](../00_foundations/03_origin_of_life_and_early_evolution.md): muốn information capacity tăng, sao chép accuracy phải tăng tương ứng.

Tuy nhiên “error càng thấp càng tốt” không phải kết luận cuối cùng. Fidelity có energetic và kinetic cost; hơn nữa evolution cần variation. Hệ thống sinh học (biological system) tối ưu trade-off, không tối đa một metric duy nhất.

## 4. Sửa chữa bắt cặp sai (mismatch repair): sửa lỗi còn sót sau sao chép

**Sửa chữa bắt cặp sai, MMR (불일치 복구)** nhận biết base pair sai hoặc small insertion/deletion loop còn sót sau sao chép. System cắt đoạn chứa mismatch rồi resynthesize dựa trên strand đúng.

Ý tưởng sâu ở đây là repair cần biết **template nào đáng tin hơn**. Trong nhiều context, newly synthesized strand được nhận diện nhờ signal liên quan replication trạng thái (state). Sau khi mismatch được excise, DNA polymerase và ligase hoàn thiện patch.

Defect MMR làm tốc độ đột biến (mutation rate) tăng mạnh. Điều này giúp hiểu **mutator phenotype**: cancer có thể không cần mutation đầu tiên trực tiếp kích hoạt proliferation; chỉ cần phá gen (gene) giữ hệ gen (genome) ổn định, toàn clone sau đó tạo mutation nhanh hơn và tăng cơ hội xuất hiện driver mutation.

## 5. Sửa chữa cắt bỏ base (base excision repair): sửa lesion nhỏ ở từng base

**Sửa chữa cắt bỏ base, BER (염기 절제 복구)** xử lý lesion nhỏ như deamination hay oxidation mà không làm helix méo mạnh.

DNA glycosylase nhận biết base bất thường và bỏ base, để lại AP site. Enzyme khác cắt backbone, polymerase điền nucleotide mới và ligase nối lại.

BER cho thấy double-stranded DNA có một lợi thế sâu: **redundancy**. Khi một strand bị damage cục bộ, strand đối diện thường giữ thông tin (information) để phục hồi. DNA vì vậy vừa là storage medium vừa có built-in error-correction logic ở structural level.

## 6. Sửa chữa cắt bỏ nucleotit (nucleotide excision repair): cắt cả đoạn khi helix bị biến dạng

**Sửa chữa cắt bỏ nucleotit, NER (뉴클레오타이드 절제 복구)** xử lý lesion cồng kềnh làm biến dạng helix, như một số UV-induced photoproduct.

Thay vì chỉ bỏ một base, system nhận structural distortion, cắt một đoạn oligonucleotide chứa lesion, rồi polymerase resynthesize và ligase seal.

Một lesson quan trọng là repair pathway được chọn theo **loại damage**, không phải theo một algorithm duy nhất. Biology dùng modular repair architecture vì lesion có physical chemistry khác nhau.

## 7. Direct reversal và tại sao đôi khi “sửa” không cần cắt DNA

Một số damage có thể được đảo trực tiếp về chemical state ban đầu. Concept này được gọi chung là **direct reversal**. Ở nhiều organism, photolyase có thể dùng light energy để sửa một số UV-induced lesion; ở human, pathway cụ thể này không đóng vai trò tương tự như ở nhiều species khác.

Điểm cần nhớ không phải tên enzyme, mà là lôgic (logic): nếu chemical modification có thể reverse trực tiếp, việc cắt backbone là không cần thiết. Repair strategy phản ánh chemistry của lesion.

## 8. Đứt gãy hai mạch (double-strand break): khi cả hai bản template cùng bị đứt

**Đứt gãy hai mạch, DSB (이중가닥 절단)** nguy hiểm vì continuity của cả hai strand bị mất. Nếu repair sai, chromosome có thể deletion, inversion hoặc translocation.

Hai chiến lược chính là **Nối đầu không tương đồng (non-homologous end joining), NHEJ** và **Tái tổ hợp tương đồng (homologous recombination), HR**.

NHEJ nối hai đầu gãy tương đối trực tiếp. Nó nhanh và hoạt động ngay cả khi không có homologous template gần đó, nhưng processing đầu gãy có thể làm mất/thêm vài nucleotide.

HR dùng homologous sequence, thường nhiễm sắc tử chị em (sister chromatid), làm template nên có thể chính xác hơn. Nhưng HR thuận lợi nhất ở phase khi nhiễm sắc tử chị em đã tồn tại.

Trade-off rất rõ: **speed và availability** của NHEJ đối lại **khuôn (template)-based fidelity** của HR.

## 9. Tế bào-cycle phase quyết định repair choice

Repair pathway không hoạt động trong vacuum. Khi tế bào ở G1 chưa có nhiễm sắc tử chị em, HR bị hạn chế. Sau DNA replication ở S/G2, nhiễm sắc tử chị em cung cấp template tốt hơn.

Vì vậy độ ổn định hệ gen nối trực tiếp với [Truyền tín hiệu và Chu kỳ tế bào](../01_cell_biology/02_cell_signaling_and_cell_cycle.md). Điểm kiểm soát chu kỳ tế bào không chỉ hỏi “đã đủ lớn chưa?” mà còn hỏi genome có đủ an toàn để tiếp tục không.

Nếu Tổn thương DNA quá nhiều, cell có thể pause cycle, repair, senescence hoặc apoptosis. Continuation của chu kỳ tế bào (cell cycle) là một **decision under risk**.

## 10. Tái tổ hợp tương đồng: repair machinery được tái sử dụng để tạo biến dị (variation)

Trong meiosis, cell chủ động tạo programmed DSB rồi dùng tái tổ hợp tương đồng để tạo trao đổi chéo (crossing-over). Nghe có vẻ nghịch lý: vì sao hệ gen-protection machinery lại tạo break?

Trao đổi chéo vừa tạo allele combination mới vừa giúp nhiễm sắc thể tương đồng (homologous chromosome) liên kết vật lý để segregation trong meiosis I chính xác hơn. Tiến hóa đã tái sử dụng repair machinery thành công cụ reproductive.

Do đó recombination là ví dụ đẹp cho một motif sinh học: **cơ chế (mechanism) ban đầu giải một constraint có thể được co-opt cho function mới**.

## 11. Recombination khác mutation ở đâu?

Mutation tạo sequence change mới. Recombination chủ yếu reshuffle sequence/haplotype đã tồn tại.

Nếu chromosome homolog mang `AB` và `ab`, trao đổi chéo có thể tạo `Ab` và `aB` mà không cần nucleotide mới. Vì vậy sinh sản hữu tính (sexual reproduction) có thể tạo combinatorial diversity rất lớn ngay cả khi tốc độ đột biến mỗi generation tương đối thấp.

Mutation tạo “new letters”; recombination tạo “new arrangement of existing paragraphs”. Cả hai đều quan trọng cho evolution nhưng theo cách khác nhau.

## 12. Chạc sao chép stress: genome damage có thể sinh ra ngay trong quá trình copy

DNA bộ máy sao chép (replication machinery) phải đi qua repeat, tightly bound protein, unusual DNA structure và vùng transcription active. Fork có thể slow hoặc stall. Nếu fork collapse, DSB có thể xuất hiện.

**Căng thẳng sao chép (replication stress) (복제 스트레스)** vì vậy là cầu nối (bridge) giữa normal replication và genome instability. Oncogene thúc cell proliferate quá mạnh có thể tăng căng thẳng sao chép, tạo thêm damage và đột biến — một phản hồi dương (positive feedback) nguy hiểm trong tumor evolution.

Điểm này sửa một misconception: mutation không chỉ đến từ “environmental mutagen”; chính việc cell cố copy genome dưới pressure cũng có thể tạo damage.

## 13. Telomere: chromosome linear tạo một problem mới

Linear chromosome gặp **end-sao chép problem** vì conventional polymerase không thể copy hoàn chỉnh phần cuối mạch theo sau (lagging strand) sau khi primer cuối bị bỏ.

**Telomere (텔로미어)** gồm repeated DNA và protein complex bảo vệ chromosome end. **Telomerase (텔로머레이스)** dùng RNA template nội tại để kéo dài telomeric repeat.

Telomere còn giải một problem nhận diện: chromosome end tự nhiên phải không bị nhầm với DSB. Nếu repair machinery coi telomere như break và nối hai nhiễm sắc thể, genome sẽ cực kỳ bất ổn.

Vì vậy telomere vừa là sao chép solution vừa là identity signal cho chromosome end.

## 14. Telomere, senescence và cancer là một trade-off multicellular

Nhiều somatic cell có telomerase thấp. Sau nhiều division, telomere có thể ngắn đến mức kích hoạt DNA-damage response và **senescence (lão hóa tế bào / 세포 노화)**.

Điều này giới hạn proliferation — có lợi để giảm cancer risk — nhưng cũng làm tissue renewal giảm theo tuổi. Nhiều tumor tái kích hoạt telomerase hoặc alternative telomere maintenance để vượt proliferative limit.

Do đó aging và cancer không phải hai chủ đề hoàn toàn tách rời. Cả hai chạm vào cùng trade-off giữa tissue regeneration và suppression của uncontrolled proliferation.

## 15. Transposable Element: genome chứa thành phần có “lợi ích riêng”

**Transposable Element, TE (전이인자)** có thể di chuyển hoặc copy trong hệ gen. DNA transposon và retrotransposon dùng mechanism khác nhau, nhưng cùng có khả năng tạo insertion, rearrangement và regulatory change.

TE có thể gây damage nếu insert vào coding/vùng điều hòa (regulatory region). Nhưng qua evolutionary time, nhiều sequence nguồn gốc TE được host co-opt làm enhancer, promoter hoặc thành phần regulatory.

Đây là ví dụ conflict–sự phối hợp (cooperation) ở quy mô phân tử (molecular scale): element có replication interest riêng nhưng product của nó đôi khi trở thành raw material cho host evolution.

## 16. Biến thể cấu trúc (structural variation): mutation không chỉ là đổi một nucleotide

Genome có thể thay đổi ở scale lớn qua deletion, duplication, inversion, translocation và copy-number variation.

**Gene duplication** đặc biệt quan trọng. Sau duplication, một copy có thể duy trì function cũ trong khi copy kia tích lũy change. Copy mới có thể mất function, chia nhỏ function với copy cũ hoặc phát triển function mới.

Nhiều gene family và molecular innovation có nguồn gốc từ logic duplication–divergence. Genome evolution vì vậy là history của cả base-level change và kiến trúc-level change.

## 17. p53 và Tổn thương DNA Response: repair phải được nối với decision

Cell cần đánh giá damage có sửa được không. Một node quan trọng trong nhiều mammalian cell là p53. Tổn thương DNA có thể làm pathway ổn định p53; p53 kích hoạt gene liên quan cell-cycle arrest, repair, senescence hoặc apoptosis tùy context.

Điểm quan trọng không phải xem p53 như “gene chống ung thư đơn lẻ”, mà như một **decision node** nối information về damage với action của whole cell.

Nếu damage nhẹ, pause và repair có lợi. Nếu damage quá nặng, apoptosis có thể tốt hơn cho organism dù bất lợi cho tế bào đó. Đây là ví dụ sinh vật-level fitness thắng cell-level survival.

## 18. Somatic và Đột biến dòng mầm (germline mutation) có consequence khác nhau

**Đột biến dòng mầm (생식계열 돌연변이)** có thể truyền cho offspring và đi vào quần thể (population) gene pool. **Đột biến soma (somatic mutation) (체세포 돌연변이)** thường chỉ ảnh hưởng lineage tế bào trong body.

```text
Germline mutation
→ inheritance
→ population variation
→ evolution qua generation

Somatic mutation
→ clonal mosaicism
→ tissue dysfunction / tumor evolution
→ consequence trong một organism
```

Cùng molecular event nhưng scale khác tạo ý nghĩa sinh học (biological meaning) khác. Đây là lý do “mutation tốt hay xấu?” là câu hỏi thiếu context.

## 19. Mosaicism: một body không hoàn toàn có một genome duy nhất

Mặc dù textbook thường nói mọi somatic cell có cùng genome, mutation tích lũy trong development và aging tạo **khảm soma (somatic mosaicism) (체세포 모자이크)**. Một clone có variant riêng có thể chiếm một fraction tissue.

Phần lớn mosaic variant không gây phenotype rõ. Một số ảnh hưởng developmental disorder, aging hoặc cancer risk. Điều này bổ sung nuance cho statement “mọi cell có cùng DNA”: đúng như approximation nền tảng, nhưng organism thật là một population dòng dõi (lineage) cell có history mutation riêng.

## 20. Tốc độ đột biến là phenotype có thể tiến hóa

Độ chính xác sao chép và repair machinery bản thân cũng do gene encode. Vì vậy tốc độ đột biến không phải constant tuyệt đối; nó có thể thay đổi qua tiến hóa.

High tốc độ đột biến tạo nhiều beneficial variant hơn khi môi trường (environment) đổi nhanh, nhưng cũng tạo nhiều đột biến có hại (deleterious mutation). Low tốc độ đột biến bảo vệ genome nhưng giảm exploration. Kích thước quần thể (population size), reproduction mode và ecological context ảnh hưởng trade-off này.

RNA virus thường có tốc độ đột biến cao hơn cellular organism; DNA organism đầu tư mạnh hơn vào đọc sửa/repair. Không có một tốc độ đột biến “tối ưu cho mọi life”.

## 21. Tình huống phân tích (case study): BRCA pathway và synthetic lethality như logic sinh học hệ thống (systems biology)

Một số protein BRCA tham gia tái tổ hợp tương đồng repair. Khi tumor mất HR function, nó phụ thuộc mạnh hơn vào repair pathway khác để sống.

Nếu một second pathway bị inhibit, combination có thể gây **synthetic lethality**: mất A riêng chưa chết, mất B riêng chưa chết, nhưng mất cả A và B làm cell không sống được.

Case này quan trọng vì nó nối độ ổn định hệ gen với sinh học hệ thống và therapy: weakness của network có thể xuất hiện không ở một gene riêng mà ở **dependency tạo bởi network trạng thái**.

## 22. Tình huống phân tích reasoning: tại sao repair “quá tích cực” cũng có thể nguy hiểm?

Nếu DSB xảy ra ở repeat-rich region, nối nhầm hai trình tự giống nhau nhưng ở vị trí khác có thể gây deletion hoặc translocation. Repair nhanh không đồng nghĩa repair đúng.

Điều này minh họa principle chung: hệ thống sinh học không tối ưu speed riêng, mà phải trade-off speed, fidelity và availability của template. NHEJ hữu ích vì nhanh, nhưng khi accuracy cực quan trọng và nhiễm sắc tử chị em có sẵn, HR thường cho route an toàn hơn.

## 23. Giải trình tự (sequencing) measurement cũng có bài toán fidelity giống replication

Khi giải trình tự (sequencing), instrument cũng có tỉ lệ lỗi. Một variant thấy trong read có thể là biological variant thật hoặc technical error. Coverage, base quality, chất lượng ánh xạ (mapping quality) và strand balance giúp phân biệt signal khỏi noise.

Có một symmetry thú vị:

```text
DNA polymerase: molecule → molecule copy
sequencer: molecule → digital copy
```

Cả hai đều cần error model và redundancy. Chương (chapter) [Phương pháp thực nghiệm và đo lường trong Sinh học](../06_biotechnology_computation/01_experimental_methods_and_measurement.md) và [Bioinformatics, thuật toán và Omics Workflow](../06_biotechnology_computation/02_bioinformatics_algorithms_and_omics_workflows.md) phát triển tiếp logic này.

## 24. Các hiểu lầm phổ biến (common misconceptions)

“Mutation xảy ra vì organism cần thích nghi” là sai. Mutation không được tạo có chủ đích theo future need; selection thay đổi frequency của variation sau khi variation xuất hiện.

“DNA repair luôn làm sequence trở lại hoàn hảo” cũng sai. NHEJ và repair ở context khó có thể để lại indel hoặc rearrangement.

“Recombination chỉ gây mutation” không đúng. Recombination là mechanism bình thường và thiết yếu của meiosis, đồng thời là repair pathway.

“Hệ gen ổn định nghĩa mọi cell có DNA giống hệt nhau” quá đơn giản. Khảm soma và biến thể cấu trúc tồn tại, nhưng được giữ trong giới hạn mà organism vẫn function.

## 25. Mô hình tư duy tổng hợp

Độ ổn định hệ gen có thể được đọc như một hierarchy:

```text
replication fidelity
→ proofreading
→ lesion-specific repair
→ DSB repair choice
→ checkpoint / cell-cycle arrest
→ apoptosis hoặc senescence nếu damage quá lớn
→ tissue-level selection và organism protection
```

Ở chiều ngược lại, những error thoát qua hierarchy tạo biến dị:

```text
unrepaired / misrepaired change
→ mutation / recombination / structural variation
→ phenotype
→ somatic selection hoặc germline inheritance
→ evolution
```

Stability và evolution vì vậy không đối lập. Evolution cần một system đủ ổn định để heredity có ý nghĩa, đồng thời đủ không hoàn hảo để variation tồn tại.

## 26. Bridge sang Evolution

Sau chapter này, nguồn variation không còn là một từ chung chung “đột biến”. Ta đã thấy variation xuất phát từ replication error, oxidative damage, repair choice, tái tổ hợp, transposable element, gene duplication và structural rearrangement.

Nhưng một variant xuất hiện trong một genome vẫn chưa phải evolution. Evolution bắt đầu khi ta theo dõi **frequency của variant trong quần thể qua nhiều generation**. Điều gì làm allele tăng? Khi nào drift mạnh hơn selection? Dòng gen (gene flow) thay population ra sao? Bottleneck làm mất diversity thế nào?

Đó chính là điểm xuất phát của [Tiến hóa và Di truyền quần thể](../03_evolution_and_diversity/00_evolution_and_population_genetics.md).

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← Genomics, Epigenetics và Điều hòa hệ gene](02_genomics_epigenetics_and_regulation.md) · [Mục lục Biology](../README.md) · [Tiến hóa và Di truyền quần thể →](../03_evolution_and_diversity/00_evolution_and_population_genetics.md)
