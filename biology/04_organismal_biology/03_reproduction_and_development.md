# Sinh sản và Phát triển — Reproduction and Development (생식과 발생)

Genetics đã cho ta meiosis và inheritance; organismal physiology cho ta các tissue chuyên hóa. Chapter này nối hai đầu: **làm thế nào một gamete haploid kết hợp thành zygote, rồi từ một cell tạo ra organism gồm nhiều cell type gần cùng genome nhưng structure và function hoàn toàn khác nhau?**

Đây là nơi cell division, signaling, gene regulation, mechanics và evolution hội tụ.

> **Mental model:** development là quá trình một genome được “đọc khác nhau theo không gian và thời gian”. Cell fate xuất hiện từ signal + regulatory network + history, không phải vì mỗi cell có một bộ gene riêng.

## 1. Asexual và sexual reproduction giải hai bài toán khác nhau

**Asexual reproduction** tạo offspring từ một parent, thường nhanh và giữ genotype gần parent hơn. **Sexual reproduction** kết hợp genetic material từ gamete, tạo recombination/assortment và variation.

Sex có cost: cần mate, chỉ truyền một phần genome và có thể phá combination tốt. Nhưng nó tạo genetic diversity và giúp selection/recombination xử lý variation theo cách khác.

Không có một strategy “tốt nhất” cho mọi environment.

## 2. Gametogenesis

Ở animals, meiosis tạo haploid gamete nhưng sperm và egg có architecture khác.

Sperm tối ưu delivery genome/motility; egg chứa cytoplasm, organelle và molecular factor cho early development.

Hai gamete có cùng chromosome number nhưng contribution cellular không cân xứng.

## 3. Fertilization

**Fertilization (수정)** gồm recognition, membrane fusion và kết hợp genetic material.

Mechanism block polyspermy giúp tránh nhiều sperm fertilize cùng egg ở nhiều species.

Fertilization không chỉ “ghép DNA”; nó activate egg metabolism/cell cycle và tạo zygote developmental program.

## 4. Cleavage: nhiều cell nhưng chưa tăng body size nhiều

Early embryo thường chia mitosis nhanh tạo blastomere; total volume không tăng tương ứng nên cell nhỏ dần.

Mục tiêu ban đầu là partition cytoplasm và tạo cell population cho patterning.

Timing/architecture khác giữa species phụ thuộc yolk và developmental strategy.

## 5. Gastrulation: từ ball cell tới body layers

**Gastrulation (낭배형성)** là cell movement/reorganization tạo germ layer như ectoderm, mesoderm, endoderm ở triploblastic animals.

Đây là transition quan trọng vì position mới tạo signal context khác và đặt nền body plan.

Development không chỉ là division; cell phải move, change adhesion và shape tissue.

## 6. Germ layer và organogenesis

Ectoderm góp phần nervous system/epidermis; mesoderm nhiều muscle, bone, circulation; endoderm epithelium nhiều internal organ.

Nhưng table “layer → organ” chỉ là summary. Mechanism thật là signaling + transcription factor + morphogenesis qua thời gian.

## 7. Cell differentiation: cùng genome, khác expression

Neuron và muscle có DNA gần như giống nhau nhưng expression program khác.

Transcription factor activate/repress network; chromatin state ổn định identity; extracellular signal hướng fate.

Differentiation là **state transition của regulatory network**.

## 8. Stem cell và potency

**Stem cell (줄기세포)** có self-renewal và khả năng tạo differentiated descendant.

Totipotent cell có thể tạo toàn organism + extraembryonic tissue trong context; pluripotent tạo hầu hết cell body; multipotent giới hạn lineage hơn.

Potency không phải “chất lượng” tốt/xấu mà là breadth fate potential.

## 9. Asymmetric division

Một stem/progenitor cell có thể divide tạo hai daughter khác fate do unequal determinant hoặc niche signal khác nhau.

Mechanism này cho phép vừa giữ stem pool vừa tạo differentiated cell.

Spatial organization trở thành information.

## 10. Induction: cell fate phụ thuộc neighbor

Developmental cell thường không tự quyết định fate chỉ từ internal program. Neighbor tissue release signal làm gene expression đổi.

Classic lens induction cho thấy optic tissue signal ảnh hưởng ectoderm tạo lens.

Cell–cell communication từ signaling chapter được dùng để xây anatomy.

## 11. Morphogen và positional information

**Morphogen (형태형성인자)** là signal phân bố gradient; cell ở concentration khác có thể activate gene khác nhau.

Một model đơn giản:

```text
high morphogen → fate A
medium → fate B
low → fate C
```

Nhưng real system có receptor dynamics, feedback và timing. Gradient là input; gene network interpret input.

## 12. Reaction–diffusion và pattern formation

Alan Turing đề xuất reaction–diffusion system có thể tự tạo spatial pattern từ interacting activator/inhibitor.

Một số biological pattern có logic tương tự. Math cho thấy stripe/spot có thể emergent từ local reaction + diffusion chứ không cần blueprint pixel-by-pixel.

Đây là connection sâu giữa developmental biology và differential equation.

## 13. Hox gene và body axis

**Hox genes (혹스 유전자)** encode transcription factor giúp specify regional identity dọc anterior–posterior axis ở nhiều animals.

Order Hox gene trong cluster có relation với spatial expression ở nhiều lineage.

Conservation Hox system cho thấy deep common ancestry của body-patterning toolkit.

## 14. Segmentation

Body segment formation dùng oscillatory gene expression và gradient ở một số vertebrate models.

“Clock and wavefront” là example time signal được convert thành spatial pattern.

Development xử lý cả space lẫn time.

## 15. Cell migration

Neural crest cell migrate xa và tạo nhiều structure. Immune precursor cũng migrate tới organ khác.

Migration cần cytoskeleton, adhesion, chemotaxis và ECM remodeling.

Cell-biology machinery được tái sử dụng ở developmental scale.

## 16. Epithelial folding và tissue mechanics

Organ shape không chỉ do gene bật/tắt. Cell proliferation, apical constriction, differential adhesion và mechanical force uốn tissue.

Gene regulation tạo protein; protein tạo force/adhesion; force tạo morphology.

Causal chain đi xuyên scale.

## 17. Apoptosis tạo hình

Programmed cell death loại cell giữa developing digit, sculpt nervous system và loại cell lỗi.

Development cần cả growth lẫn death. “Nhiều cell hơn” không đồng nghĩa development tốt hơn.

## 18. Left–right asymmetry

Body nhìn ngoài gần bilateral nhưng heart, liver và gut có asymmetry. Early embryo tạo left–right signal bias qua cilia/fluid flow và gene network ở vertebrate models.

Small symmetry-breaking event sớm có thể dẫn tới anatomy asymmetry lớn sau này.

## 19. Placenta: interface giữa hai organism

Ở placental mammals, placenta trao đổi gas, nutrient, waste và hormone giữa maternal/fetal circulation mà blood không trộn trực tiếp hoàn toàn.

Placenta vừa transport organ vừa endocrine/immune interface.

Pregnancy physiology là negotiation resource giữa maternal và fetal system.

## 20. Developmental constraint

Evolution không thể tạo bất kỳ phenotype tùy ý; new trait phải đi qua viable developmental pathway.

Shared developmental gene làm change có pleiotropic consequence. Constraint giúp giải thích vì sao evolution dùng lại module cũ.

## 21. Evo-devo

**Evolutionary developmental biology (진화발생생물학)** hỏi evolution body form xảy ra qua change developmental gene/network thế nào.

Nhiều morphological difference không cần protein-coding gene hoàn toàn mới; change enhancer/timing/location expression có thể tạo form mới.

Genomics, development và evolution hội tụ ở regulatory DNA.

## 22. Regeneration

Một số animal như salamander tái tạo limb tốt hơn mammals. Regeneration cần wound response, dedifferentiation/progenitor activation, positional information và growth control.

Mammal cũng regenerate một số tissue như liver/skin/blood nhưng limitation khác.

Understanding regeneration cần so sánh developmental program được reactivated thế nào.

## 23. Aging khác development nhưng dùng nhiều pathway chung

**Aging (lão hóa / 노화)** là decline function/risk change theo thời gian, liên quan DNA damage, proteostasis, mitochondrial function, cellular senescence, stem-cell exhaustion và signaling.

Không có một “gene lão hóa” duy nhất. Aging là system-level process với trade-off evolutionary.

## 24. Cellular senescence

Cell senescent dừng proliferation lâu dài sau stress/damage nhưng vẫn metabolically active và có thể secrete factor ảnh hưởng tissue.

Senescence hữu ích trong tumor suppression/wound context nhưng accumulation có thể góp phần age-related dysfunction.

Một mechanism có benefit/cost tùy time và context.

## 25. Cancer như development bị lệch control

Cancer cell re-use pathway growth, migration, angiogenesis và survival vốn cần trong development/repair.

Oncogenesis không tạo machinery hoàn toàn mới; nó deregulate biological program sẵn có.

Developmental biology giúp hiểu cancer invasion và differentiation state.

## 26. Teratogen và critical period

Environmental factor có thể gây developmental abnormality mạnh nếu exposure đúng critical window, dù cùng dose ở adulthood effect khác.

Timing quyết định vì organ pattern chỉ mở một số window.

Development cho thấy “effect của environment” phải luôn hỏi **khi nào**.

## 27. Case study: thalidomide

Thalidomide exposure trong early pregnancy từng gây limb defect nghiêm trọng, minh họa critical-period sensitivity và importance developmental testing.

Mechanism phức tạp gồm target molecular/developmental pathway, nhưng lesson là adult toxicity data không đủ dự đoán embryonic effect.

## 28. Case study: identical twins

Monozygotic twin bắt đầu từ cùng zygote nên genome rất gần nhau, nhưng phenotype vẫn có thể khác do developmental stochasticity, environment, epigenetic state và somatic mutation.

“Same DNA” không đồng nghĩa “same organism outcome”.

## 29. Common misconceptions

“Embryo chỉ là miniature adult lớn dần” sai; structure xuất hiện qua patterning/morphogenesis.

“Mỗi cell type có gene khác” sai; phần lớn genome giống nhau, expression state khác.

“Stem cell có thể biến thành bất cứ gì trong mọi context” sai; potency và niche giới hạn fate.

“Gene tạo hình trực tiếp” quá đơn giản; gene → protein/network → cell behavior → mechanics → morphology.

“Aging chỉ do cell hết khả năng chia” sai; nhiều system/process đóng góp.

## 30. Bridge: organism không sống một mình

Sau organismal biology, ta đã hiểu một body được xây và điều khiển. Nhưng organism luôn nằm trong population/community, cạnh competitor, predator, mutualist và environment vật lý.

Behavior của organism ảnh hưởng survival/reproduction; population size thay resource; species interaction tạo food web. Đó là bước chuyển sang [[../05_ecology/00_population_community_and_behavior]].

> **Mental model cuối chapter:** development là computation phân bố trong tissue: signal cung cấp positional/time information, gene network chuyển information thành cell state, cytoskeleton/adhesion chuyển state thành force và shape. Organism là kết quả history của những decision cell phối hợp, không phải genome “bung ra” như một blueprint cố định.