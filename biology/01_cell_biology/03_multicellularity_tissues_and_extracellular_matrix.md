# Đa bào, mô và chất nền ngoại bào — Multicellularity, Tissues and Extracellular Matrix (다세포성, 조직과 세포외기질)

Các chapter trước chủ yếu nhìn tế bào như một đơn vị sống tương đối độc lập: nó có màng (membrane), tạo ATP, xử lý signal và kiểm soát chu kỳ tế bào (cell cycle). Nhưng một organism đa bào không đơn giản là “nhiều cell đặt cạnh nhau”. Khi hàng triệu hay hàng nghìn tỉ cell cùng tồn tại trong một body, một cấp bài toán mới xuất hiện: cell nào làm việc gì, làm sao giữ đúng vị trí, ai được phép divide, chất dinh dưỡng (nutrient) đi đến nơi xa bằng cách nào, tissue sửa chữa ra sao, và điều gì ngăn một clone cell tối đa hóa lợi ích riêng đến mức phá hủy toàn organism?

**Đa bào (Multicellularity / 다세포성)** vì vậy là một major transition về organization. Tế bào (cell) đánh đổi một phần autonomy để nhận lại specialization, resource sharing, protection và khả năng xây structure lớn hơn nhiều giới hạn của một cell riêng lẻ.

> **Mô hình tư duy (mental model):** sinh vật (organism) đa bào giống một society of cells có phân công chức năng (division of labor), communication, infrastructure và conflict-điều khiển (control). Nếu chỉ có “nhiều cell” mà không có những cơ chế này, ta có colony lỏng lẻo chứ chưa có mô (tissue)–cơ quan (organ) system phức tạp.

## 1. Vì sao một cell không thể chỉ lớn mãi?

Trong [Tế bào, màng và vận chuyển](00_cells_membranes_and_transport.md), ta đã gặp surface-area-to-volume ratio. Nếu kích thước đặc trưng của cell là \(L\), diện tích bề mặt (surface area) tăng gần theo \(L^2\), trong khi volume tăng theo \(L^3\). Do đó:

\[
\frac{Surface\ Area}{Volume}\propto\frac{1}{L}
\]

Cell càng lớn, lượng membrane trên mỗi đơn vị cytoplasm càng ít. Nhưng nutrient, gas và waste chủ yếu phải qua màng. Đồng thời thời gian khuếch tán (diffusion time) tăng gần theo bình phương distance:

\[
t\sim \frac{x^2}{2D}
\]

Khoảng cách tăng 10 lần có thể làm thời gian khuếch tán tăng khoảng 100 lần trong mô hình (model) đơn giản. Vì vậy “phóng to một cell” nhanh chóng gặp bottleneck exchange và internal transport.

Multicellularity giải bài toán bằng cách giữ individual cell tương đối nhỏ nhưng xây **bulk transport system** ở scale lớn hơn. Animal dùng circulation; plant dùng xylem/mạch rây (phloem); tissue tạo folded surface như villi hay alveoli để tăng area. Một constraint vật lý ở quy mô micromet (micron scale) vì vậy dẫn tới anatomy ở centimet–quy mô mét (metre scale).

## 2. Từ colony đến organism: cooperation phải trở thành ổn định

Nhiều cell có thể sống cạnh nhau mà chưa tạo organism thực sự. Multicellularity bền vững cần ít nhất bốn lớp integration: cell phải bám nhau; phải communicate; phải differentiation thành role khác nhau; và reproduction của whole organism phải được tổ chức sao cho tế bào-level conflict không phá hệ.

Đa bào đã tiến hóa độc lập ở animal, plant, fungi và nhiều algae. Điều đó cho thấy không có một blueprint duy nhất. Tuy nhiên các lineage phức tạp thường hội tụ vào cùng loại problem: sự bám dính (adhesion), truyền tín hiệu (signaling), tính phân cực (polarity), tạo mẫu hình phát triển (developmental patterning), resource transport và kiểm soát xung đột (conflict suppression).

Một yếu tố evolutionary quan trọng là **nút thắt một tế bào (single-cell bottleneck)**. Nhiều organism bắt đầu development từ một zygote. Điều này làm các cell trong body có relatedness rất cao, nên cooperation dễ được selection duy trì hơn so với tập hợp cell không liên quan. Bottleneck cũng gắn reproduction với organism-level program thay vì để mỗi somatic cell tự truyền lineage độc lập.

## 3. Cùng genome, khác loại tế bào (cell type): differentiation là regulation chứ không phải đổi DNA

Nơron (neuron), hepatocyte và muscle cell trong cùng body phần lớn chứa genome rất giống nhau. Khác biệt chức năng đến chủ yếu từ **biểu hiện gene khác biệt (Differential Gene Expression / 차등 유전자 발현)**.

Yếu tố phiên mã (transcription factor), enhancer, trạng thái nhiễm sắc chất (chromatin state), con đường truyền tín hiệu (signaling pathway) và RNA regulation làm một tập gene active ở loại tế bào này nhưng inactive ở loại tế bào khác. Vì vậy genome nên được hình dung như một thư viện chung, còn mỗi loại tế bào sử dụng một chương trình truy cập khác nhau.

Điểm quan trọng là differentiation không chỉ là “bật vài gene dấu ấn (marker)”. Một loại tế bào là một **stable regulatory state**: protein màng (membrane protein), bộ xương tế bào (cytoskeleton), chuyển hóa (metabolism), secreted molecule và đáp ứng (response) con đường (pathway) được phối hợp thành whole phenotype. Chương (chapter) [Genomics, Epigenetics và Điều hòa hệ gene](../02_genetics_molecular_biology/02_genomics_epigenetics_and_regulation.md) giải cơ chế molecular của việc này, còn [Sinh sản và Phát triển](../04_organismal_biology/03_reproduction_and_development.md) giải cách pattern này được xây trong embryo.

## 4. Tính phân cực tế bào (cell polarity): một cell trong tissue thường có “phía trên” và “phía dưới”

Trong textbook cơ bản, cell thường được vẽ như hình tròn đồng đều. Nhưng nhiều epithelial cell có **tính phân cực tế bào (tính phân cực tế bào / 세포 극성)** rất rõ. Bề mặt đỉnh (apical surface) hướng về lumen hoặc exterior; bề mặt đáy (basal surface) gắn màng đáy (basement membrane); bề mặt bên (lateral surface) tiếp xúc tế bào lân cận (neighboring cell).

Polarity làm protein transporter được đặt ở đúng side. Ví dụ intestinal epithelial cell có transporter ở apical membrane để lấy nutrient từ lumen và transporter khác ở basolateral membrane để đưa nutrient vào blood. Nếu cùng transporter bị phân bố ngẫu nhiên toàn membrane, vận chuyển có định hướng (directed transport) qua tissue sẽ mất hiệu quả.

Vì vậy, multicellular function đòi hỏi không chỉ biết cell nào ở đâu mà còn biết **orientation của từng cell**.

## 5. Junction tạo kiến trúc (architecture), permeability và communication

Tế bào trong mô được nối bằng nhiều loại junction vì mỗi loại giải bài toán khác nhau.

**Mối nối kín (tight junction) (밀착연접)** hạn chế passage qua khoảng giữa cell, rất quan trọng khi epithelium phải kiểm soát thứ gì đi từ lumen vào body. **Mối nối bám dính (adherens junction)** và **desmosome** nối cytoskeleton giữa cell để truyền mechanical force. **Mối nối khe (gap junction) (간극연접)** tạo channel cho ion và small molecule đi trực tiếp giữa neighboring animal cells, giúp electrical hoặc metabolic coupling. Ở plant, **plasmodesmata (원형질연락사)** tạo communication xuyên thành tế bào (cell wall).

Điểm cần nhìn thấy là tissue barrier không phải một “bức tường”. Nó là một **selective interface**. Mối nối kín quyết định paracellular route; protein vận chuyển màng (membrane transporter) quyết định transcellular route; signaling quyết định barrier được mở, đóng hay remodeled khi condition thay đổi.

## 6. Sự bám dính tế bào (cell adhesion) molecule không chỉ là keo

**Cadherin** giúp cell–sự bám dính tế bào, còn **integrin** nối cell với **chất nền ngoại bào (Extracellular Matrix, ECM / 세포외기질)**. Nhưng adhesion receptor không chỉ giữ cell tại chỗ. Chúng nối với cytoskeleton và truyền tín hiệu (signaling) bộ máy (machinery), vì vậy mechanical force có thể đổi biochemical state.

Quá trình biến force thành intracellular signal được gọi là **mechanotransduction (기계적 신호전달)**. Nếu ECM cứng hơn, integrin tension và downstream pathway có thể thay đổi, dẫn tới thay đổi proliferation, migration hoặc differentiation.

Một cell do đó đọc environment bằng ít nhất hai “ngôn ngữ”: chemical ligand và mechanical property.

## 7. ECM: scaffold, reservoir và information field

ECM chứa collagen, elastin, proteoglycan, fibronectin, laminin và nhiều molecule khác. Composition, orientation và cross-linking thay đổi giữa tissue.

Tendon có collagen bundle định hướng theo lực kéo. Cartilage có proteoglycan giữ nước giúp chống compression. Bone kết hợp collagen với mineral để vừa chịu tension vừa chịu compression. Màng đáy tạo một sheet mỏng vừa support epithelium vừa ảnh hưởng polarity và filtration.

ECM cũng giữ yếu tố tăng trưởng (growth factor), tạo gradient và kiểm soát diffusion. Vì vậy ECM không phải vật liệu “ngoài cell” thụ động. Cell tiết ECM và enzyme remodeling; ECM quay lại điều khiển cell hành vi (behavior).

```text
cell signaling
→ ECM synthesis/remodeling
→ stiffness + geometry + stored signal thay đổi
→ integrin/mechanosensing thay đổi
→ gene expression thay đổi
```

Đây là vòng phản hồi (feedback loop) giữa mechanics và điều hòa gen (gene regulation).

## 8. Bốn nhóm tissue chính ở animal chỉ là điểm bắt đầu

**Biểu mô (Epithelial Tissue / 상피조직)** tạo ranh giới (boundary), absorption surface và gland. **Mô liên kết (Connective Tissue / 결합조직)** nhấn mạnh ECM và support. **Mô cơ (Muscle Tissue / 근육조직)** chuyển chemical energy thành mechanical force. **Mô thần kinh (Nervous Tissue / 신경조직)** xử lý và truyền information nhanh.

Nhưng một organ thật luôn là integration của nhiều tissue. Ruột non cần epithelium hấp thu, smooth muscle tạo motility, nơron điều khiển local reflex, connective tissue support và mạch máu (blood vessel) mang nutrient đi. “Function của ruột” không nằm riêng trong bất kỳ tissue nào; nó là **đặc tính nổi trội (emergent property) của architecture nhiều tissue**.

## 9. Diffusion limit dẫn tới vascularization

Khi tissue dày lên, tế bào ở xa surface không thể nhận oxygen/nutrient chỉ bằng diffusion đủ nhanh. Đây là lý do animal lớn cần vascular network.

Tumor cũng gặp constraint này. Khối tumor nhỏ có thể sống dựa vào diffusion từ vessel gần đó, nhưng khi lớn hơn nó thường cần kích thích **angiogenesis (tạo mạch / 혈관신생)**. Nếu vascularization không theo kịp, region bên trong dễ hypoxia và necrosis.

Case này cho thấy một nguyên lý vật lý tái xuất trong pathology: growth của tissue bị giới hạn bởi transport infrastructure. Organismal circulation không phải một chapter anatomy tách rời; nó là solution trực tiếp của tissue-scale diffusion vấn đề (problem).

## 10. Tế bào gốc (stem cell), progenitor và tissue turnover

**Tế bào gốc (Stem Cell / 줄기세포)** có hai đặc tính (property): self-renew và khả năng tạo differentiated descendants. Nhưng stemness không chỉ nằm “bên trong” tế bào; nó phụ thuộc **thân (stem)-cell niche (줄기세포 미세환경)** gồm tế bào lân cận, ECM, oxy (oxygen), nutrient và tín hiệu (signal).

Skin, intestinal epithelium và blood có turnover cao nên cần stem/progenitor system hoạt động liên tục. Neuron hoặc cardiomyocyte trưởng thành có turnover thấp hơn nhiều. Điều này tạo trade-off: tissue renew nhanh sửa damage tốt nhưng mỗi cycle proliferation lại là một cơ hội replication error và oncogenic mutation.

Vì vậy regeneration và cancer risk liên kết sâu với nhau.

## 11. Tái sinh (regeneration): repair architecture khó hơn thay cell

Sau injury, chỉ tạo thêm cell chưa đủ. Tissue phải khôi phục spatial organization, ECM, vessel và connection với nerve hoặc neighboring tissue.

Inflammation loại debris và phát signal repair. Fibroblast tạo ECM mới. Vascular cell tái lập blood supply. Thân/progenitor cell proliferate. Sau đó matrix phải được remodeled để force và architecture trở lại phù hợp.

Nếu repair quá yếu, wound không lành. Nếu response quá mạnh hoặc kéo dài, **xơ hóa (fibrosis / 섬유화)** có thể làm quá nhiều matrix tích tụ và giảm function. Đây là ví dụ “more response” không đồng nghĩa “better response”. Biology thường tối ưu một range, không tối đa một variable.

## 12. Tạo hình (morphogenesis): tissue shape xuất hiện từ local force và local rule

Development không có một “bàn tay” kéo tissue thành shape. Shape xuất hiện từ phân chia tế bào (cell division), sinh trưởng (growth), sự bám dính, sự di chuyển (migration), tính phân cực, apoptosis và mechanical force.

Nếu epithelial sheet co ở một phía, nó có thể bend. Nếu một nhóm cell thay adhesion và bộ xương tế bào, chúng có thể invaginate hoặc migrate. Nếu proliferation nhanh hơn ở một region, tissue có thể fold.

Đây là **tạo hình (hình thái phát sinh / 형태형성)**: gen (gene)-regulatory program tạo local cell hành vi; local behavior tạo force; force và geometry quay lại ảnh hưởng signaling. Development vì vậy là coupling giữa information và mechanics.

## 13. Plant multicellularity: cùng problem, khác physical solution

Plant cell có thành tế bào cứng và thường không migrate như animal cell. Vì vậy plant morphology phụ thuộc nhiều vào orientation của phân chia tế bào và differential expansion.

Auxin gradient, tế bào-wall loosening và meristem organization giúp plant tạo rễ (root), shoot và lá (leaf). Vì tế bào giữ position tương đối ổn định, “tế bào dòng dõi (lineage)” và “position information” có logic khác animal development.

Plant cũng có developmental plasticity cao; một số differentiated plant cell có thể dedifferentiate và tái tạo whole organism trong condition phù hợp. Điều này cho thấy multicellularity không có một design bắt buộc, mà là nhiều evolutionary solution dưới constraint khác nhau.

## 14. Cạnh tranh tế bào (cell competition) và kiểm soát chất lượng (quality control) trong mô

Trong mô, cell không chỉ hợp tác; chúng còn có thể được so sánh tương đối. Cell damaged hoặc less fit có thể bị loại qua apoptosis hoặc cell-competition mechanism. Hệ miễn dịch (immune system) cũng giám sát abnormal cell.

Kiểm soát chất lượng giúp tissue không tích lũy defect quá nhanh. Nhưng system không hoàn hảo: clone có đột biến (mutation) giúp tránh apoptosis, ignore growth inhibition hoặc evade immune surveillance có thể mở đầu tumor evolution.

Đây là nơi sinh học tế bào (cell biology), genetics và evolution gặp nhau ngay bên trong một organism.

## 15. Cancer như breakdown của multicellular contract

Một somatic cell bình thường chấp nhận nhiều constraint: chỉ divide khi nhận signal phù hợp, không invade tissue khác, chịu apoptosis khi damage quá lớn và sử dụng resource trong giới hạn của organ.

Cancer xuất hiện khi clone tích lũy change phá dần những constraint này. Từ góc nhìn evolutionary, tumor có biến dị (variation), tính di truyền (heredity), differential proliferation và chọn lọc (selection). Hypoxia, immune pressure và drug treatment tạo environment chọn clone phù hợp hơn.

Vì vậy cancer không chỉ là “cell divide nhanh”. Nó là **somatic evolution trong một ecosystem mô** và là failure của cooperation ở level multicellular.

## 16. Tình huống phân tích (case study): intestinal epithelium như một hệ thống đa tầng

Ruột là ví dụ tốt để nối nhiều concept. Lumen chứa food và microbe nên epithelium phải tạo barrier. Mối nối kín hạn chế uncontrolled paracellular flow. Apical transporter hấp thu nutrient. Basolateral transporter chuyển nutrient về blood. Tế bào gốc ở crypt tạo cell mới để thay epithelium turnover nhanh. Immune cell bên dưới giám sát pathogen. Smooth muscle tạo movement và enteric neuron điều khiển local reflex.

Nếu chỉ học từng loại tế bào riêng, ta không hiểu intestine. Function xuất hiện khi **tính phân cực + junction + thân-cell renewal + vascular transport + immune defense + neural control** được tích hợp.

Đó chính là cách nên đọc mọi organ sau này.

## 17. Tình huống phân tích định lượng: tại sao tissue phải gần vessel?

Thời gian khuếch tán tăng theo \(x^2\). Nếu oxygen diffusion effective distance tăng từ 20 µm lên 200 µm, distance tăng 10 lần nên thời gian khuếch tán đặc trưng (characteristic diffusion time) tăng khoảng 100 lần trong approximation đơn giản.

Vì cell tiêu thụ oxygen liên tục, chỉ tăng thời gian khuếch tán đã chưa đủ mô tả toàn vấn đề; concentration còn giảm theo consumption. Điều này giải thích tại sao capillary network phải dày đặc trong tissue hoạt động mạnh và vì sao hypoxia xuất hiện khi perfusion giảm.

Math ở đây biến một fact anatomy thành causal explanation.

## 18. Các hiểu lầm phổ biến (common misconceptions)

“Tế bào trong cùng body khác nhau vì có DNA khác nhau” phần lớn là sai; khác biệt chính là regulatory state, dù đột biến soma (somatic mutation) vẫn tích lũy theo thời gian.

“ECM chỉ là chất đệm” cũng sai; ECM truyền force, chứa signal và ảnh hưởng biểu hiện gen (gene expression).

“Tế bào gốc càng nhiều càng tốt” không đúng; proliferation potential phải cân bằng với mutation/cancer risk.

“Multicellularity chỉ giúp organism lớn hơn” quá hẹp. Lợi ích quan trọng hơn là phân công chức năng, buffering, complex sensing, transport và reproduction strategy mới.

## 19. Mô hình tư duy tổng hợp

Có thể nén multicellularity thành flow:

```text
cell nhỏ giải exchange tốt
→ nhiều cell hợp tác
→ adhesion + communication
→ differential gene expression
→ polarity + tissue architecture
→ ECM + mechanics
→ transport infrastructure
→ stem-cell renewal + repair
→ organ integration
→ organism-level homeostasis
```

Mỗi step thêm capability mới nhưng cũng tạo vulnerability mới. Sự bám dính cho tissue nhưng mở đường metastasis khi regulation hỏng. Proliferation giúp repair nhưng tăng cancer risk. Barrier bảo vệ nhưng phải vẫn cho selective exchange. Multicellularity luôn là bài toán trade-off và điều khiển.

## 20. Bridge sang Organismal Biology

Khi tissue và cơ quan đã tồn tại, câu hỏi tiếp theo không còn là “cell này làm gì?” mà là **nhiều organ phối hợp thế nào để giữ môi trường bên trong cơ thể (internal environment) đủ ổn định cho hàng nghìn loại cell cùng sống?** Oxygen phải đi từ lung tới mitochondria; nutrient phải đi từ gut tới tissue; waste phải được kidney loại; temperature và pH phải được giữ trong phạm vi (range); signal phải đi nhanh hoặc đi xa.

Đó là điểm xuất phát của [Sinh lý động vật và Cân bằng nội môi](../04_organismal_biology/01_animal_physiology_and_homeostasis.md). Hãy đọc physiology như continuation của tissue-level constraint, không phải một danh sách hệ cơ quan mới.

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← Truyền tín hiệu và Chu kỳ tế bào](02_cell_signaling_and_cell_cycle.md) · [Mục lục Biology](../README.md) · [DNA, Gene và Biểu hiện gene →](../02_genetics_molecular_biology/00_dna_genes_and_gene_expression.md)
