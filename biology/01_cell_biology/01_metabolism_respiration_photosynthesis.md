# Chuyển hóa, hô hấp tế bào và quang hợp — Metabolism, Cellular Respiration and Photosynthesis (대사, 세포호흡, 광합성)

Một tế bào có membrane, protein và DNA vẫn không thể sống nếu không có dòng năng lượng liên tục. Pump cần energy để duy trì ion gradient, ribosome cần energy để tổng hợp protein, cytoskeleton cần energy để vận động, DNA repair cần energy, và ngay cả việc giữ một cell “đứng yên” cũng tiêu tốn energy.

Vì vậy, **metabolism (chuyển hóa / 대사)** không phải một chapter phụ của Sinh học. Nó là cách tế bào biến matter và energy thành khả năng tiếp tục tồn tại.

## Metabolic pathway — reaction được tổ chức thành chuỗi

Một reaction đơn lẻ thường không đủ để biến nutrient thành dạng cell dùng được. Tế bào tổ chức reaction thành **metabolic pathway (con đường chuyển hóa / 대사 경로)**.

```text
Molecule A --E1--> B --E2--> C --E3--> D
```

Mỗi bước thường do enzyme khác nhau xúc tác. Việc chia thành nhiều step cho phép cell:

- thu energy thành từng phần thay vì giải phóng ồ ạt;
- kiểm soát từng point;
- dùng intermediate cho pathway khác;
- dừng hoặc tăng flux tùy nhu cầu.

**Flux (dòng chuyển hóa / 대사 흐름)** là tốc độ matter đi qua pathway. Đây là một mental model tốt hơn việc coi pathway như danh sách reaction bất biến.

## Catabolism và anabolism hoạt động cùng nhau

**Catabolism (dị hóa / 이화작용)** phá molecule và thường giải phóng free energy. **Anabolism (đồng hóa / 동화작용)** xây molecule và thường cần energy.

Cellular respiration là catabolic process lớn: glucose bị oxidized dần và energy được thu vào ATP/NADH.

Protein synthesis là anabolic: amino acid được nối thành polypeptide và cần energy.

Hai nhóm process được nối bằng ATP và electron carrier. Vì vậy metabolism là network chứ không phải hai hộp độc lập.

## Oxidation và reduction — energy thường đi cùng electron

Một molecule bị **oxidized (oxi hóa / 산화)** khi mất electron; molecule khác bị **reduced (khử / 환원)** khi nhận electron.

Electron thường được chuyển cùng hydrogen atom hoặc proton, nên biochemical equation có thể trông khác textbook chemistry nhưng logic redox vẫn giống nhau.

Trong respiration, carbon trong glucose bị oxidized thành CO₂. Oxygen cuối cùng bị reduced thành water.

NAD⁺ nhận high-energy electron để thành NADH:

\[
NAD^+ + 2e^- + H^+ \rightarrow NADH
\]

NADH giống một carrier tạm thời. Nó không phải “energy” tự thân, nhưng trạng thái reduced của nó có khả năng donate electron cho process khác.

## Cellular respiration không phải “cell thở” theo nghĩa phổi

**Hô hấp tế bào (cellular respiration / 세포호흡)** là process chuyển chemical energy trong nutrient thành ATP thông qua oxidation–reduction.

Phổi đưa O₂ vào body và thải CO₂. Nhưng reaction sử dụng O₂ thực sự xảy ra chủ yếu ở mitochondria của cell. Đây là connection giữa physiology và cellular metabolism.

Phương trình tổng quát thường viết:

\[
C_6H_{12}O_6 + 6O_2 \rightarrow 6CO_2 + 6H_2O + energy
\]

Phương trình này đúng ở mức bookkeeping nhưng che mất điều quan trọng: energy không được release trong một bước. Cell chia process thành nhiều stage.

## Stage 1 — Glycolysis

**Glycolysis (đường phân / 해당과정)** xảy ra trong cytosol.

Một glucose 6-carbon được biến thành hai pyruvate 3-carbon.

Quá trình gồm phase đầu investment ATP và phase sau payoff. Net điển hình mỗi glucose:

- 2 pyruvate;
- 2 ATP net;
- 2 NADH.

Tại sao cell lại “tiêu ATP trước rồi mới kiếm lại”? Vì phosphorylation giúp activate molecule và tạo intermediate dễ xử lý hơn. Đây là ví dụ energy investment để mở một pathway profitable hơn sau đó.

Glycolysis rất cổ và không trực tiếp cần oxygen. Vì vậy cả aerobic và nhiều anaerobic organism đều dùng nó.

## Stage 2 — Pyruvate oxidation

Ở eukaryotic aerobic respiration, pyruvate vào mitochondrion và được chuyển thành **acetyl-CoA**.

Một carbon được release thành CO₂ và NAD⁺ được reduced thành NADH.

Acetyl-CoA là metabolic junction quan trọng, không chỉ đến từ glucose mà còn có thể từ fatty acid và một số amino acid.

## Stage 3 — Citric acid cycle

**Citric acid cycle / Krebs cycle / TCA cycle (회로)** xảy ra trong mitochondrial matrix ở eukaryote.

Acetyl group được oxidized hoàn toàn thành CO₂. Nhưng purpose chính của cycle không phải trực tiếp tạo rất nhiều ATP; nó thu electron vào NADH và FADH₂.

Mỗi glucose tạo hai acetyl-CoA, nên cycle quay hai vòng.

Một output điển hình mỗi glucose từ cycle là nhiều NADH, FADH₂, một ít ATP/GTP và CO₂.

## Stage 4 — Electron transport chain

Đây là phần thường bị học thuộc nhưng có mental model rất đẹp.

NADH và FADH₂ đưa electron vào **electron transport chain (chuỗi chuyền electron / 전자전달계)** nằm ở inner mitochondrial membrane.

Electron đi qua một chuỗi protein theo hướng energy giảm dần. Energy released được dùng để pump H⁺ từ matrix ra intermembrane space.

Kết quả: mitochondrion biến energy của electron thành **proton gradient**.

Đây giống việc dùng energy để bơm nước lên hồ cao. Nước ở cao có potential energy; H⁺ concentration difference cũng lưu potential energy.

## Chemiosmosis và ATP synthase

H⁺ muốn chảy trở lại matrix theo electrochemical gradient. Nhưng inner membrane gần như không cho H⁺ tự do qua.

H⁺ đi qua **ATP synthase (ATP 합성효소)**, một molecular machine sử dụng dòng proton để phosphorylate ADP thành ATP.

Process dùng ion gradient để drive chemical synthesis gọi là **chemiosmosis (hóa thẩm / 화학삼투)**.

> **Mental model:** respiration chuyển energy qua ba dạng chính: chemical bond của nutrient → high-energy electron → proton gradient → ATP.

## Oxygen làm gì?

Oxygen là **final electron acceptor (chất nhận electron cuối / 최종 전자수용체)** trong aerobic respiration.

Nếu không có oxygen, electron transport chain không thể tiếp tục nhận electron bình thường. NADH không được oxidized trở lại NAD⁺ đủ nhanh, và nhiều pathway upstream bị nghẽn.

Oxygen nhận electron và proton để tạo water.

Đây là reason O₂ quan trọng, không phải vì nó “được đốt” trực tiếp cùng glucose trong một reaction đơn lẻ.

## ATP yield — vì sao không nên học một con số cứng

Textbook đôi khi đưa con số 30–32 ATP trên một glucose ở eukaryote. Con số thực có thể thay đổi theo cell type, shuttle system, proton leak và condition.

Điều cần hiểu là phần lớn ATP đến từ oxidative phosphorylation, không phải trực tiếp từ glycolysis hoặc TCA cycle.

Một con số chính xác tuyệt đối ít quan trọng hơn flow of energy.

## Khi thiếu oxygen: fermentation

Nếu oxygen không đủ hoặc organism không dùng oxygen, cell vẫn cần NAD⁺ để glycolysis tiếp tục.

**Fermentation (lên men / 발효)** tái sinh NAD⁺ bằng cách chuyển electron từ NADH sang organic molecule.

Trong lactic acid fermentation, pyruvate nhận electron và thành lactate.

Trong alcohol fermentation của yeast, pyruvate được chuyển thành ethanol và CO₂ qua intermediate.

Fermentation không tạo thêm nhiều ATP ngoài ATP từ glycolysis. Purpose cốt lõi là **regenerate NAD⁺**.

## Fat metabolism — vì sao fat chứa nhiều energy?

Fatty acid có nhiều reduced carbon và hydrogen. Qua **beta-oxidation (β-산화)**, fatty acid bị cắt thành acetyl-CoA và tạo NADH/FADH₂.

Acetyl-CoA vào TCA cycle, electron carrier đi vào electron transport chain.

Vì fatty acid có nhiều C–H bond và carbon ở trạng thái reduced hơn carbohydrate, oxidation có thể yield nhiều energy hơn trên mỗi gram.

## Photosynthesis — energy đi theo chiều ngược lại?

Nếu respiration lấy chemical energy từ organic molecule, **photosynthesis (quang hợp / 광합성)** dùng light energy để tạo reduced carbon compound từ CO₂.

Phương trình simplified:

\[
6CO_2 + 6H_2O + light \rightarrow C_6H_{12}O_6 + 6O_2
\]

Nhưng như respiration, equation tổng quát che mất mechanism.

Photosynthesis gồm hai nhóm process lớn: light reactions và Calvin cycle.

## Light reactions — ánh sáng tạo ATP và NADPH

Light reaction xảy ra ở thylakoid membrane của chloroplast.

**Chlorophyll (diệp lục / 엽록소)** hấp thụ photon. Photon nâng electron lên energy state cao hơn.

Electron được truyền qua electron transport chain. Energy dùng để tạo proton gradient qua thylakoid membrane.

ATP synthase sử dụng gradient để tạo ATP, rất giống principle ở mitochondria.

Water bị split để cung cấp electron, và O₂ được release như by-product.

NADP⁺ nhận electron thành NADPH.

## Calvin cycle — carbon fixation

**Calvin cycle (캘빈 회로)** dùng ATP và NADPH từ light reactions để đưa carbon từ CO₂ vào organic molecule.

Enzyme Rubisco giúp attach CO₂ vào carbon acceptor. Qua nhiều step, cycle tạo G3P, precursor để plant tạo glucose và nhiều molecule khác.

Điểm quan trọng: plant không “tạo thức ăn từ đất”. Carbon skeleton chủ yếu đến từ atmospheric CO₂; soil cung cấp water và mineral nutrient.

## Respiration và photosynthesis không phải hai reaction đảo ngược đơn giản

Equation tổng quát trông đối xứng, nhưng pathway, enzyme và compartment khác nhau.

Plant cũng thực hiện cellular respiration cả ngày lẫn đêm. Photosynthesis cung cấp organic carbon và energy storage; respiration giải phóng usable energy từ organic molecule.

## C3, C4 và CAM — khi photosynthesis gặp vấn đề môi trường

Rubisco có thể bind O₂ thay vì CO₂, dẫn đến **photorespiration**, làm giảm efficiency.

C4 plant và CAM plant phát triển mechanism concentrate CO₂ quanh Rubisco, đặc biệt hữu ích trong hot/dry environment.

C4 tách carbon fixation và Calvin cycle theo **không gian** giữa cell type.

CAM tách theo **thời gian**: stomata mở chủ yếu ban đêm để giảm water loss, CO₂ được lưu tạm rồi dùng ban ngày.

Đây là ví dụ evolution giải quyết trade-off giữa carbon uptake và water conservation.

## Metabolism được điều hòa như thế nào?

Cell không chạy mọi pathway tối đa cùng lúc.

Enzyme activity có thể thay đổi bằng phosphorylation, allosteric binding, substrate availability và gene expression.

Hormone ở organism level có thể thay đổi metabolism của nhiều tissue. Insulin và glucagon là ví dụ trong glucose regulation.

Đây là bridge sang cell signaling và physiology.

## Common misconceptions

### “Hô hấp tế bào chỉ xảy ra khi đang thở mạnh”

Sai. Cellular respiration diễn ra liên tục ở living cell. Breathing là organism-level process cung cấp O₂ và loại CO₂.

### “Plant chỉ photosynthesize, animal mới respire”

Sai. Plant cell có mitochondria và respiration. Photosynthesis và respiration cùng tồn tại.

### “Oxygen biến thành CO₂”

Carbon trong CO₂ chủ yếu đến từ carbon của nutrient. Oxygen inhaled chủ yếu cuối cùng nhận electron/proton và tạo water.

### “ATP là energy được tạo ra một lần rồi lưu”

ATP được tái tạo và tiêu thụ liên tục. Long-term energy storage chủ yếu nằm trong molecule như glycogen và fat.

## Mental Model

> Metabolism là mạng chuyển đổi energy. Respiration tháo energy khỏi nutrient từng bước, đóng gói vào electron carrier, gradient và ATP. Photosynthesis dùng photon để tạo ATP/NADPH rồi dùng chúng cố định carbon. Hai process nối biosphere thành một dòng năng lượng lớn.

Tế bào không chỉ cần energy; nó còn phải biết **khi nào** tăng metabolism, phân chia hay dừng lại. File [[02_cell_signaling_and_cell_cycle]] xây cơ chế sensing, signaling và control đó.