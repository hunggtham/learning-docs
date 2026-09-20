# DNA, gene và biểu hiện gene — DNA, Genes and Gene Expression (DNA, 유전자와 유전자 발현)

Tế bào cần protein để làm enzyme, receptor, channel, cytoskeleton và hàng nghìn chức năng khác. Nhưng protein không tự xuất hiện. Cell cần một hệ lưu trữ thông tin đủ bền để truyền qua nhiều lần phân chia, đồng thời phải đọc được thông tin đó khi cần.

Giải pháp trung tâm của sự sống trên Trái Đất là **DNA (deoxyribonucleic acid / 디옥시리보핵산)**.

## Information trong biology nghĩa là gì?

Khi nói DNA “chứa thông tin”, ta không có nghĩa DNA hiểu ý nghĩa như con người. Ta nói **sequence của nucleotide ảnh hưởng đến sequence của RNA và protein**, và sequence đó ảnh hưởng structure/function.

Một alphabet nhỏ có thể tạo lượng combination khổng lồ. DNA dùng bốn base chính: A, T, G, C. Information nằm chủ yếu ở thứ tự của chúng.

> **Mental model:** DNA giống một storage medium có sequence; cellular machinery là hệ đọc, copy và điều khiển việc sử dụng sequence đó.

## Nucleotide và DNA strand

Mỗi **nucleotide (뉴클레오타이드)** trong DNA có deoxyribose sugar, phosphate và nitrogenous base.

Nucleotide nối nhau bằng phosphodiester bond tạo sugar–phosphate backbone. Mỗi strand có direction vì hai đầu hóa học khác nhau, ký hiệu 5' và 3'.

Direction quan trọng vì enzyme polymerase không làm việc đối xứng tùy ý; DNA synthesis diễn ra chủ yếu theo hướng 5' → 3'.

## Double helix và complementary base pairing

DNA thường tồn tại dưới dạng **double helix (xoắn kép / 이중나선)** gồm hai strand antiparallel.

A bắt cặp với T; G bắt cặp với C qua hydrogen bond và geometry phù hợp.

Nếu một strand là:

```text
5' - A T G C C A - 3'
```

strand complementary sẽ là:

```text
3' - T A C G G T - 5'
```

Complementarity tạo một property cực mạnh: **mỗi strand có thể làm template để tái tạo strand còn lại**.

## Gene không đơn giản là “một đoạn DNA tạo một protein”

**Gene (유전자)** là vùng DNA tạo ra functional product, thường là RNA hoặc protein thông qua RNA.

Một số gene mã hóa protein. Một số tạo functional RNA như rRNA, tRNA hoặc regulatory RNA.

Ở eukaryote, gene có thể gồm promoter, exon, intron và regulatory region. Vì vậy boundary của một gene trong molecular biology phức tạp hơn câu định nghĩa ngắn ở trường học.

## Genome, chromosome và chromatin

**Genome (bộ gene / 유전체)** là toàn bộ genetic material của organism/cell theo context.

DNA rất dài. Eukaryotic cell đóng gói DNA với histone protein thành **chromatin (염색질)**.

Chromatin được tổ chức thành **chromosome (nhiễm sắc thể / 염색체)**.

Chromosome không phải chỉ xuất hiện lúc cell division. DNA luôn được tổ chức thành chromosome; trong interphase nó chỉ ít condensed hơn nên hình ảnh textbook không thấy các “chữ X” rõ.

Hình chữ X thường là một replicated chromosome gồm hai sister chromatids đã condensed.

## DNA replication — copy information trước khi cell division

Trước khi cell phân chia, genome phải được copy.

Replication là **semiconservative (bán bảo tồn / 반보존적)**: mỗi DNA double helix mới có một strand cũ và một strand mới.

### Helicase mở helix

**Helicase (헬리케이스)** tách hai strand bằng cách phá interaction giữa base pair.

Khi DNA mở, tension có thể tăng phía trước replication fork; topoisomerase giúp giải quyết torsional stress.

### Primer và DNA polymerase

DNA polymerase không bắt đầu chain từ số 0 hiệu quả trong normal replication; cần primer cung cấp 3'-OH.

Primase tạo RNA primer. **DNA polymerase** kéo dài từ primer bằng cách thêm nucleotide complementary vào template.

Vì polymerase synthesize 5' → 3' nhưng hai template antiparallel, hai strand mới được tạo khác kiểu.

### Leading và lagging strand

**Leading strand** được synthesize tương đối liên tục theo hướng replication fork mở.

**Lagging strand** được synthesize thành các đoạn **Okazaki fragment**, sau đó primer được xử lý và DNA ligase nối các đoạn.

Đây không phải complication ngẫu nhiên; nó xuất phát trực tiếp từ geometry antiparallel + constraint 5' → 3' synthesis.

## Proofreading và DNA repair

Replication rất chính xác nhưng không hoàn hảo. Nhiều DNA polymerase có proofreading. Sau replication còn có repair pathway sửa mismatch hoặc damage.

Sai sót còn lại có thể trở thành **mutation (đột biến / 돌연변이)** nếu được cố định trong genome.

Mutation vừa có thể gây disease vừa là nguồn variation cần cho evolution. Không có mutation, natural selection gần như không có nguyên liệu mới lâu dài.

# Central dogma — từ DNA đến RNA đến protein

Một simplification kinh điển:

```text
DNA --transcription--> RNA --translation--> Protein
```

Đây gọi là **central dogma (중심원리)**. Nó hữu ích nhưng không có nghĩa mọi information flow chỉ đi đúng một line đơn giản. RNA có nhiều role, reverse transcription tồn tại, và gene regulation phức tạp.

Mental model đúng hơn: DNA lưu sequence tương đối bền; RNA là lớp trung gian linh hoạt; protein thực hiện phần lớn chemistry/structure.

## Transcription — tạo RNA từ DNA template

**Transcription (phiên mã / 전사)** là quá trình RNA polymerase dùng DNA làm template để tạo RNA.

### Promoter

**Promoter (프로모터)** là DNA region giúp transcription machinery xác định nơi bắt đầu và direction transcription.

Ở bacteria, promoter recognition thường liên quan sigma factor. Ở eukaryote, nhiều transcription factor và RNA polymerase phối hợp.

### RNA polymerase

RNA polymerase đọc template DNA strand và synthesize RNA theo 5' → 3'. RNA complementary với template, nhưng dùng U thay T.

Nếu coding DNA strand có:

```text
5' - ATG CCA - 3'
```

mRNA tương ứng thường có:

```text
5' - AUG CCA - 3'
```

Coding strand giống mRNA về sequence ngoại trừ T/U.

## RNA processing ở eukaryote

Primary RNA transcript thường chưa sẵn sàng để translation.

Nó được xử lý bằng 5' cap, poly-A tail và **splicing (이어맞추기 / 스플라이싱)**.

**Intron (인트론)** bị loại khỏi mature mRNA; **exon (엑손)** được nối lại.

### Alternative splicing

Một pre-mRNA có thể được splice theo nhiều pattern, tạo các mRNA khác nhau từ cùng gene.

Điều này phá vỡ mental model đơn giản “một gene = một protein”. Một gene có thể tạo nhiều isoform.

## Translation — ribosome đọc mRNA

**Translation (dịch mã / 번역)** chuyển sequence nucleotide thành amino acid sequence.

Ribosome đọc mRNA theo nhóm ba nucleotide gọi là **codon (코돈)**.

Ví dụ AUG thường mã hóa methionine và thường đóng vai trò start codon.

**tRNA (transfer RNA / 운반 RNA)** mang amino acid và có anticodon complementary với codon.

Ribosome phối hợp codon–anticodon rồi xúc tác peptide bond.

## Genetic code — redundancy nhưng có logic

Có 64 codon khả dĩ từ 4 nucleotide theo nhóm 3. Chỉ có 20 amino acid chuẩn chính, nên nhiều amino acid được mã hóa bởi nhiều codon. Đây là **degeneracy/redundancy of genetic code**.

Redundancy giúp một số mutation ở nucleotide thứ ba không đổi amino acid, gọi là synonymous mutation.

Genetic code gần như universal, một bằng chứng mạnh cho common ancestry của life.

## Protein chưa hoàn thành sau translation

Polypeptide mới được tạo phải fold. Nhiều protein còn cần cleavage, phosphorylation, glycosylation hoặc transport tới đúng compartment.

Vì vậy flow thực tế là:

```text
DNA information
→ RNA
→ polypeptide
→ folding/modification/localization
→ functional protein
```

## Gene expression — cell chọn gene nào được dùng

**Gene expression (biểu hiện gene / 유전자 발현)** là process dùng information gene để tạo functional product.

Cell gan và neuron có gần cùng genome nhưng proteome rất khác vì expression pattern khác nhau.

Cell identity do đó không chỉ nằm ở “có gene gì”, mà còn ở **gene nào đang on/off, mức bao nhiêu và trong context nào**.

## Mutation ảnh hưởng protein như thế nào?

Mutation ở coding sequence có thể:

- không đổi amino acid;
- đổi một amino acid;
- tạo stop codon sớm;
- làm frameshift nếu insertion/deletion không theo bội số 3.

Nhưng mutation ngoài coding sequence cũng quan trọng. Mutation promoter hoặc enhancer có thể đổi mức expression mà không đổi protein sequence.

Đây là lý do “mutation = protein bị sai” là quá hẹp.

## Common misconceptions

### “DNA là blueprint chính xác của cơ thể”

Blueprint analogy dễ gây cảm giác mỗi gene tương ứng một bộ phận. Thực tế development xuất hiện từ network gene regulation, signaling, physical interaction và environment.

### “Gene bị bật thì chắc chắn tạo protein”

Expression có nhiều checkpoint: transcription, RNA processing, RNA stability, translation và protein degradation.

### “Tất cả DNA đều là gene mã hóa protein”

Không. Genome chứa regulatory region, noncoding RNA gene, repetitive sequence và nhiều vùng chức năng/nonfunction theo context khác nhau.

### “Mutation luôn xấu”

Mutation có thể harmful, neutral hoặc occasionally beneficial tùy context. Evolution cần variation từ mutation và recombination.

## Mental Model

> DNA là long-term sequence storage; replication copy storage; transcription tạo working RNA copy; translation chuyển một subset information thành protein; regulation quyết định lúc nào và ở đâu flow này xảy ra.

File tiếp theo [[01_inheritance_variation_and_mutation]] đưa information từ molecular scale lên family/population scale: chromosome được truyền qua meiosis như thế nào, vì sao offspring khác nhau, và Mendelian probability xuất hiện từ đâu.