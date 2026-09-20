# Sinh sản và phát triển — Reproduction and Development (생식과 발생)

Một fertilized egg chỉ là một cell. Vậy bằng cách nào một cell có thể tạo ra organism gồm hàng nghìn tỷ cell với neuron, muscle, skin, blood và organ nằm đúng vị trí?

Developmental biology trả lời bằng một idea quan trọng: **cell không cần genome khác nhau để trở thành cell khác nhau; chúng cần nhận signal khác nhau và biểu hiện những phần genome khác nhau theo đúng không gian và thời gian**.

## Asexual và sexual reproduction

**Asexual reproduction (sinh sản vô tính / 무성생식)** tạo offspring mà không fusion gamete. Nó có thể nhanh và giữ genotype gần parent, nhưng variation mới chủ yếu đến từ mutation.

**Sexual reproduction (sinh sản hữu tính / 유성생식)** kết hợp genetic material từ gamete, tạo recombination và variation lớn hơn.

Sexual reproduction có cost: phải tạo gamete, tìm mate ở nhiều species và chỉ truyền một phần genome mỗi offspring. Tuy vậy recombination có thể giúp lineage đối phó changing environment, parasite và deleterious mutation theo nhiều evolutionary hypothesis.

## Gametogenesis — tạo sperm và egg

**Gametogenesis (sự tạo giao tử / 배우자형성)** dùng meiosis để tạo haploid gamete.

Ở male mammal, spermatogenesis tạo nhiều small motile sperm từ precursor.

Ở female mammal, oogenesis phân chia cytoplasm bất đối xứng, tạo một large ovum và polar body. Egg cần đủ organelle, RNA và nutrient để support early development.

Sự khác biệt này phản ánh function chứ không phải một meiosis “đúng” và một meiosis “lệch”.

## Fertilization — nhiều hơn việc cộng hai bộ chromosome

**Fertilization (thụ tinh / 수정)** là fusion của gamete và activation developmental program.

Sperm phải nhận biết egg environment, fuse membrane và đưa genetic material vào. Egg có mechanism giảm polyspermy vì nhận nhiều sperm sẽ phá chromosome number.

Kết quả tạo **zygote (hợp tử / 접합자)** diploid.

Zygote có genome mới, nhưng early development còn phụ thuộc molecule maternal đã được nạp trong egg trước fertilization.

## Cleavage — tăng cell number mà chưa tăng size nhiều

Sau fertilization, zygote trải qua rapid mitotic division gọi là **cleavage (분할)**.

Cell nhỏ dần vì overall embryo size ban đầu không tăng tương ứng. Những cell này gọi là blastomere.

Ở mammal, embryo đi qua morula rồi blastocyst. Blastocyst có inner cell mass và outer trophoblast lineage, mở đầu specialization.

## Gastrulation — tạo body plan cơ bản

**Gastrulation (낭배형성)** là process cell move và reorganize thành germ layer.

Ba germ layer ở triploblastic animal:

- ectoderm;
- mesoderm;
- endoderm.

Ectoderm tạo nervous system và epidermis trong broad pattern. Mesoderm góp muscle, bone, blood và nhiều connective tissue. Endoderm góp lining của digestive/respiratory tract và nhiều associated organ.

Danh sách derivative có nhiều detail, nhưng mental model quan trọng là gastrulation chuyển embryo từ ball/sheet cell thành spatial body plan.

## Cell differentiation — cùng DNA, khác identity

**Differentiation (biệt hóa / 분화)** là process cell trở nên specialized.

Neuron và liver cell gần như có cùng DNA sequence, nhưng transcription factor và epigenetic state khác làm expression pattern khác.

Một cell identity được duy trì bởi gene regulatory network: factor A activate B, B reinforce A, đồng thời repress alternative fate.

Vì vậy differentiation giống việc cell đi vào một stable regulatory state hơn là “mất các gene không cần”.

## Determination và competence

Một cell có thể dần bị **determined**, nghĩa fate trở nên constrained dù chưa biểu hiện full morphology.

**Competence** là khả năng phản ứng với một developmental signal. Một signal chỉ có effect nếu cell có receptor và regulatory context phù hợp.

Điều này nối trực tiếp với principle ở cell signaling: signal không tự mang meaning; receiving state matter.

## Morphogen — concentration gradient mang positional information

Một **morphogen (형태형성물질)** là signaling molecule có thể tạo concentration gradient và gây response khác nhau theo concentration.

Giả sử source tiết morphogen ở một edge. Diffusion và degradation tạo gradient:

```text
source  ████████▓▓▓▒▒░░  far away
```

Cell gần source nhận high signal và activate gene set A; cell ở intermediate activate B; cell xa activate C.

Như vậy continuous concentration được convert thành discrete spatial fate.

Đây là một biological use của threshold và gradient.

## Induction — tissue nói chuyện với tissue

**Induction (cảm ứng / 유도)** xảy ra khi một cell group gửi signal làm neighboring group đổi developmental fate.

Eye development, limb formation và organogenesis phụ thuộc nhiều reciprocal induction.

Embryo không được build bởi mỗi cell đọc coordinate cố định trong DNA; pattern emerge từ repeated local signaling interaction.

## Hox gene — positional identity dọc body axis

**Hox genes (혹스 유전자)** mã hóa transcription factor giúp xác định regional identity dọc anterior–posterior axis ở nhiều animal.

Hox gene thường nằm thành cluster, và order trên chromosome liên quan pattern expression theo body axis trong nhiều species.

Conservation của Hox gene giữa fly và vertebrate là evidence sâu về common ancestry của developmental toolkit.

## Organogenesis — pattern thành organ

Sau germ layer và body axis, tissue tiếp tục fold, migrate, proliferate và die có chương trình để tạo organ.

Heart tube fold và chamber specialize; neural tube tạo central nervous system; limb bud phát triển qua signaling center và growth gradient.

**Apoptosis** cũng là constructive process. Ví dụ cell death giúp sculpt interdigital region trong nhiều vertebrate limb development.

Development vì vậy là combination của cell proliferation + differentiation + migration + mechanical force + programmed death.

## Stem cell — self-renewal và potency

**Stem cell (tế bào gốc / 줄기세포)** có hai property chính: self-renewal và khả năng tạo differentiated progeny.

### Totipotent

Có thể tạo toàn organism và extraembryonic tissue trong context phù hợp, như zygote/very early blastomere.

### Pluripotent

Có thể tạo gần như mọi body cell type nhưng không toàn bộ extraembryonic structure cần cho organism hoàn chỉnh.

### Multipotent

Tạo nhiều cell type trong một lineage/tissue, như hematopoietic stem cell tạo blood cell lineage.

Potency không giống proliferation rate; một cancer cell divide mạnh không tự động là pluripotent stem cell.

## Regeneration

Một số animal như planarian hoặc salamander regenerate structure đáng kể; mammal có regenerative capacity hạn chế hơn tùy tissue.

Regeneration cần wound response, proliferation, positional information và differentiation.

Liver có khả năng phục hồi mass mạnh nhưng chủ yếu qua proliferation/hypertrophy của existing cell hơn là tái tạo nguyên whole organ architecture từ một fragment theo cách salamander limb.

## Human reproductive endocrine axis

Hypothalamus release GnRH; pituitary release LH/FSH; gonad produce sex steroid và gamete-supporting signal.

Feedback giữa hormone điều khiển cycle và gametogenesis.

Ở menstrual cycle, follicular development, ovulation và luteal phase xuất hiện từ changing interaction giữa FSH, LH, estrogen và progesterone.

Không nên học cycle như bốn hormone tăng giảm độc lập; nó là coupled feedback system.

## Pregnancy — maternal và fetal physiology tương tác

Sau implantation, placenta phát triển như exchange/endocrine organ giữa maternal và fetal circulation.

Hai blood supply thường không trộn trực tiếp hoàn toàn; gas, nutrient, waste và signal trao đổi qua placental interface.

Placenta release hormone làm maternal metabolism/circulation thích nghi pregnancy.

Đây là example organism-level physiology được tái cấu hình để support development.

## Sex determination và differentiation

Sex determination mechanism rất đa dạng giữa species: chromosome, temperature hoặc environmental factor khác có thể tham gia.

Ở human, SRY trên Y chromosome thường trigger testis-development pathway, nhưng sex development là cascade gồm gene, hormone, receptor và tissue response. Biological variation có thể xuất hiện ở nhiều step.

Vì vậy textbook XX/XY là useful baseline cho human genetics nhưng không phải toàn bộ biology của sex determination across life.

## Aging — development không kết thúc ở adulthood

**Aging (lão hóa / 노화)** là progressive change trong function và risk theo time, không có một cause duy nhất.

Mechanism được nghiên cứu gồm genomic instability, telomere attrition, epigenetic alteration, loss of proteostasis, mitochondrial dysfunction, cellular senescence, stem-cell exhaustion và altered intercellular communication.

Các “hallmarks” là framework research, không phải một single pathway đã giải thích hoàn toàn aging.

Evolutionary perspective cũng quan trọng: selection thường yếu hơn với effect chỉ xuất hiện sau reproductive age, và trade-off giữa early-life benefit với late-life cost có thể tồn tại.

## Development và evolution — evo-devo

**Evolutionary developmental biology (evo-devo / 진화발생생물학)** hỏi variation trong developmental program tạo morphological diversity như thế nào.

Evolution không cần tạo mỗi structure từ gene hoàn toàn mới. Change timing, location hoặc level expression của conserved developmental gene có thể tạo phenotype lớn.

Đây là connection mạnh giữa gene regulation, development và evolution.

## Common misconceptions

### “Mỗi cell type có gene riêng”

Đa số somatic cell giữ gần như cùng genome; difference chủ yếu do expression/regulation.

### “Development chỉ là cell division”

Không. Nếu chỉ tăng cell number, embryo sẽ là mass cell. Spatial pattern, migration, differentiation và mechanical remodeling mới tạo body.

### “Stem cell có thể tự động biến thành bất cứ cell nào”

Potency khác nhau, và differentiation cần signal/context phù hợp.

### “Gene quyết định sẵn từng chi tiết anatomy”

Genome mã hóa component và regulatory logic; final structure emerge từ gene expression, signaling, mechanics và environment.

## Mental Model

> Development là computation phân tán bằng cell: gene regulatory network lưu state, signaling truyền information giữa cell, morphogen tạo positional cue, mechanics thay shape, feedback ổn định fate. Từ một genome gần như chung, spatial context tạo nhiều cell type và organ.

Sau organismal biology, [[../05_ecology/00_population_community_and_behavior]] đưa scale lên population và community: individual behavior và interaction giữa species tạo pattern ở environment như thế nào.