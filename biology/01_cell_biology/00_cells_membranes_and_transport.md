# Tế bào, màng và vận chuyển — Cells, Membranes and Transport (세포, 세포막과 물질수송)

Ở chương trước, ta đã có đủ “vật liệu”: lipid có thể tự tạo bilayer, protein có thể làm enzyme hoặc transporter, nucleic acid có thể lưu information, ATP và gradient có thể couple process. Nhưng một câu hỏi lớn vẫn còn: **làm thế nào những molecule này được tổ chức thành một đơn vị có thể sống?**

Câu trả lời không nằm ở một bào quan riêng lẻ. Nó nằm ở cách cell tạo ranh giới, chia không gian, kiểm soát exchange và phối hợp reaction. Vì vậy chương này bắt đầu từ vấn đề organization, sau đó mới dẫn đến membrane, transport và organelle.

## 1. Vì sao cell cần boundary?

Một reaction network muốn tồn tại phải giữ một số molecule ở gần nhau và duy trì composition khác với environment. Nếu mọi molecule khuếch tán tự do ra ngoài, concentration cần cho reaction sẽ biến mất. Nếu ion trong và ngoài hoàn toàn cân bằng, cell mất electrochemical gradient. Nếu enzyme và substrate luôn bị pha loãng vô hạn, metabolism trở nên quá chậm.

Boundary vì thế không phải “vỏ bọc”. Nó là điều kiện để tạo một **inside** có chemistry riêng.

Plasma membrane giải bài toán này bằng phospholipid bilayer. Hydrophobic core làm nhiều ion và polar molecule khó đi trực tiếp qua, trong khi membrane protein tạo những route được kiểm soát.

> **Mental model:** membrane không phải bức tường. Nó là một interface có rule, cho phép cell vừa tách khỏi môi trường vừa giao tiếp với môi trường.

## 2. Fluid mosaic: màng là cấu trúc động

Màng thường được mô tả bằng **fluid mosaic model (모자이크 유동 모델)**. “Fluid” nhắc rằng lipid và nhiều protein có thể di chuyển trong plane của membrane. “Mosaic” nhắc rằng membrane không chỉ gồm lipid mà chứa protein, carbohydrate và cholesterol với composition khác nhau theo cell type và membrane region.

Cholesterol ở animal membrane giúp điều chỉnh fluidity. Ở nhiệt độ thấp, nó cản phospholipid đóng gói quá chặt; ở nhiệt độ cao, nó hạn chế motion quá mức.

Vì membrane dynamic, receptor có thể cluster, vesicle có thể fuse, cytoskeleton có thể kéo membrane thay đổi shape. Đây là nền của endocytosis, synapse và cell migration.

## 3. Diffusion: movement không cần “ý chí” của molecule

Molecule trong liquid luôn chuyển động do thermal motion. Nếu concentration khác nhau giữa hai vùng, random motion tạo net movement từ high concentration sang low concentration.

Đây là **diffusion (khuếch tán / 확산)**.

Điểm quan trọng là diffusion không cần ATP trực tiếp. Driving force là concentration gradient.

Một approximation quan trọng là Fick's law:

\[
J=-D\frac{dC}{dx}
\]

Trong đó \(J\) là flux, \(D\) là diffusion coefficient và \(dC/dx\) là concentration gradient.

Dấu âm nói net flux đi theo chiều concentration giảm.

Từ equation này ta suy ra trực giác: gradient càng dốc, diffusion càng mạnh; distance càng lớn, exchange càng chậm. Đây là lý do alveoli và capillary barrier rất mỏng.

## 4. Simple diffusion, facilitated diffusion và active transport

Không phải substance nào cũng đi qua membrane theo cùng cách.

Small nonpolar molecule như O₂ và CO₂ có thể qua lipid bilayer khá dễ bằng **simple diffusion**.

Ion và nhiều polar molecule cần **channel** hoặc **carrier protein**, tạo **facilitated diffusion (khuếch tán được hỗ trợ / 촉진확산)**. Process vẫn đi theo gradient và không dùng ATP trực tiếp.

Nếu cell cần chuyển substance **ngược gradient**, process cần energy coupling. Đây là **active transport (vận chuyển chủ động / 능동수송)**.

Ví dụ Na⁺/K⁺ ATPase dùng ATP để bơm Na⁺ ra và K⁺ vào, tạo gradient rất quan trọng cho nerve, muscle và secondary transport.

## 5. Primary và secondary active transport

Trong **primary active transport**, transporter dùng energy source trực tiếp, thường ATP hydrolysis.

Trong **secondary active transport**, transporter không hydrolyze ATP trực tiếp. Nó khai thác gradient đã được tạo bởi transporter khác.

Ví dụ sodium–glucose cotransporter ở intestine dùng Na⁺ gradient để kéo glucose vào cell. Na⁺ gradient này cuối cùng tồn tại nhờ Na⁺/K⁺ ATPase dùng ATP.

Vì vậy “glucose uptake không dùng ATP trực tiếp” không có nghĩa process không phụ thuộc energy. Energy có thể nằm **upstream trong gradient**.

Đây là một pattern rất quan trọng: biological system thường truyền energy qua nhiều dạng trung gian.

## 6. Osmosis: water cũng phản ứng với concentration difference

**Osmosis (thẩm thấu / 삼투)** là net movement của water qua selectively permeable membrane theo water potential difference.

Trong cách học đơn giản, ta thường nói water đi từ nơi “ít solute” sang nơi “nhiều solute”. Mental model này tạm dùng được nếu solute không qua membrane.

Nếu animal cell đặt trong solution hypotonic, water vào nhiều, cell có thể swell và lyse. Trong hypertonic solution, water ra, cell shrink.

Plant cell khác vì có cell wall. Water vào tạo **turgor pressure**, giúp tissue thực vật giữ form.

Cùng một principle membrane + water gradient dẫn đến physiology rất khác tùy structure.

## 7. Electrochemical gradient: concentration và charge gộp lại

Ion mang charge nên movement không chỉ phụ thuộc concentration. Nếu inside cell negative, cation bị hút vào và anion bị đẩy ra về mặt electrical force.

Do đó ion chịu **electrochemical gradient** gồm chemical component và electrical component.

Một ion có thể có concentration gradient đẩy ra nhưng electrical gradient kéo vào. Net direction phụ thuộc tổng free-energy change.

Đây là nền trực tiếp của membrane potential và action potential trong nervous system.

## 8. Membrane potential: cell biến ion distribution thành electrical state

Khi ion distribution hai bên membrane khác nhau và membrane permeability chọn lọc, điện thế hai bên có thể khác nhau. Đây là **membrane potential (điện thế màng / 막전위)**.

Cell không phải một pin đơn giản, nhưng analogy pin hữu ích: chemical separation của charge lưu potential energy.

Nếu channel mở, ion flow thay đổi membrane potential. Vì channel có thể được điều khiển bằng voltage, ligand hoặc mechanical force, membrane trở thành device có khả năng xử lý signal.

Từ transport, ta đã chạm tới signaling.

## 9. Surface-area-to-volume: vì sao cell không thể lớn vô hạn?

Khi kích thước cell tăng, volume tăng nhanh hơn surface area.

Nếu coi cell gần như sphere:

\[
A=4\pi r^2
\]

\[
V=\frac{4}{3}\pi r^3
\]

Do đó:

\[
\frac{A}{V}=\frac{3}{r}
\]

Khi radius tăng, surface-area-to-volume ratio giảm.

Điều này tạo constraint: metabolic demand liên quan volume tăng nhanh nhưng membrane area cho exchange không tăng nhanh bằng.

Biology giải constraint bằng nhiều cách: cell nhỏ, membrane fold, microvilli tăng area, organism đa bào dùng specialized transport system.

Một equation hình học đơn giản giải thích từ size của cell đến sự cần thiết của circulation ở organism lớn.

## 10. Prokaryotic organization: ít compartment nhưng không đơn giản về function

Bacteria và archaea không có nucleus bao membrane như eukaryote, nhưng chúng vẫn tổ chức DNA, ribosome, membrane, enzyme và cytoskeleton-like protein.

Nhiều metabolic reaction xảy ra trực tiếp ở plasma membrane hoặc cytosol. Một số bacteria có internal membrane specialization.

Điểm quan trọng là prokaryote không phải cell “thiếu bộ phận”. Chúng giải bài toán organization bằng architecture khác.

## 11. Eukaryotic compartmentalization: chia không gian để control chemistry

Eukaryotic cell có nhiều membrane-bound organelle. Compartmentalization mang lại ba lợi ích lớn.

Thứ nhất, nó **tách reaction không tương thích**. Lysosome chứa enzyme phân giải trong môi trường acidic; nếu enzyme này hoạt động tự do khắp cytosol sẽ nguy hiểm.

Thứ hai, nó **tăng local concentration** của enzyme và substrate, giúp pathway hiệu quả hơn.

Thứ ba, membrane của organelle có thể tạo **gradient riêng**, như inner mitochondrial membrane tạo proton gradient.

Vì vậy organelle không nên học như danh sách “nucleus làm gì, Golgi làm gì”. Mỗi organelle là lời giải cho một organizational problem.

## 12. Nucleus: bảo vệ và điều phối information flow

Nucleus chứa phần lớn DNA ở eukaryote. Nuclear envelope tách transcription khỏi translation.

Điều này tạo cơ hội regulation: pre-mRNA có thể được processed, spliced và quality-checked trước khi ra cytoplasm.

Nuclear pore không phải lỗ trống; nó là regulated gateway cho protein và RNA.

Nucleus vì thế là example rõ của principle đã gặp ở plasma membrane: **boundary + selective transport = control**.

## 13. Endoplasmic reticulum và Golgi: cell có logistics system

**Rough ER** có ribosome gắn ngoài, tham gia synthesis protein đi vào secretory pathway hoặc membrane.

Protein mới vào ER có thể fold, form disulfide bond và được kiểm tra quality.

Sau đó vesicle chuyển protein tới **Golgi apparatus**, nơi molecule được modify, sort và gửi tới destination.

Ta có flow:

```text
DNA in nucleus
   ↓ transcription
mRNA
   ↓ translation
rough ER
   ↓ folding / modification
Golgi
   ↓ sorting
membrane / lysosome / secretion
```

Đây là ví dụ cụ thể về information flow biến thành physical logistics.

## 14. Mitochondria và chloroplast: compartment tạo energy conversion

Mitochondria có outer và inner membrane. Inner membrane tạo nhiều fold gọi là cristae, tăng area cho electron transport chain và ATP synthase.

Chloroplast ở plant và algae cũng có membrane system phức tạp để tổ chức photosynthesis.

Cả hai organelle nhấn mạnh một principle: **energy conversion thường cần membrane để giữ gradient**.

Chương sau sẽ dùng chính architecture này để giải respiration và photosynthesis.

## 15. Cytoskeleton: cell cần cơ học và đường vận chuyển

Cytoskeleton gồm microfilament, intermediate filament và microtubule.

Nó không chỉ “giữ hình dạng”. Cytoskeleton tạo track cho motor protein, tham gia cell division, migration, vesicle transport và mechanical force transmission.

Cell vì thế vừa là chemical system vừa là mechanical system.

## 16. Endocytosis và exocytosis: khi molecule quá lớn cho transporter

Large cargo không thể đơn giản chui qua channel. Cell có thể reshape membrane để tạo vesicle.

**Endocytosis** đưa material vào. **Exocytosis** fuse vesicle với plasma membrane để release content hoặc thêm membrane component.

Neurotransmitter release ở synapse là một form exocytosis được regulate rất chặt.

Again, membrane dynamics nối cell logistics với nervous signaling.

## 17. Endosymbiosis: organelle có lịch sử tiến hóa

Mitochondria và chloroplast mang nhiều dấu hiệu cho thấy tổ tiên của chúng từng là free-living bacteria: có DNA riêng, ribosome giống bacterial type hơn và double membrane.

**Endosymbiotic theory (thuyết nội cộng sinh / 세포내공생설)** nói một ancestral cell engulfed bacteria nhưng thay vì tiêu hóa, hai bên hình thành symbiosis lâu dài.

Điểm này rất quan trọng vì nó nối cell biology với evolution. Structure hiện tại của cell mang dấu vết lịch sử.

## 18. Từ organization sang metabolism: câu hỏi tiếp theo

Ta đã hiểu cell tạo boundary, control transport và compartmentalize reaction. Nhưng organization chỉ hữu ích nếu có process diễn ra bên trong.

Mitochondria có membrane gradient để làm gì? Glucose đi vào cell rồi được biến đổi ra sao? Vì sao oxygen cần thiết cho nhiều organism? Plant lấy light rồi biến thành chemical energy như thế nào?

Đây là bước tiếp theo: không chỉ “cell có mitochondria”, mà **energy flow chạy qua cell theo pathway nào**.

Tiếp tục với [[01_metabolism_respiration_photosynthesis]].