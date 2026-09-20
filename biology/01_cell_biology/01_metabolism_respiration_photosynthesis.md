# Chuyển hóa, hô hấp và quang hợp — Metabolism, Respiration and Photosynthesis (대사, 세포호흡과 광합성)

Chương trước đã xây cell như một system có boundary, compartment và gradient. Nhưng một cell được tổ chức tốt vẫn không thể sống nếu không liên tục cung cấp energy và nguyên liệu. Câu hỏi bây giờ là: **cell lấy energy ở đâu, chuyển nó qua những dạng trung gian nào, và dùng architecture của membrane để biến energy thành ATP ra sao?**

Đây là nơi nhiều người bắt đầu học thuộc pathway. Cách đó rất dễ quên. Thay vào đó, ta sẽ theo một dòng xuyên suốt: **electron đi đâu, proton gradient được tạo như thế nào, và ATP xuất hiện từ đâu**.

## 1. Metabolism là network chứ không phải một reaction

**Metabolism (chuyển hóa / 대사)** là toàn bộ reaction hóa học trong cell. Nhưng nói “toàn bộ reaction” vẫn còn quá trừu tượng. Cách nghĩ hữu ích hơn là xem metabolism như một network gồm nhiều pathway nối với nhau.

Một pathway lấy substrate làm input, qua chuỗi enzyme tạo intermediate, rồi cho product. Product này có thể trở thành input của pathway khác.

```text
glucose
  ↓
glycolysis intermediates
  ├── ATP
  ├── NADH
  ├── biosynthesis precursors
  └── pyruvate
        ↓
   acetyl-CoA
        ↓
 citric-acid cycle
```

Như vậy glucose không chỉ “được đốt để lấy năng lượng”. Carbon skeleton của nó còn có thể được rẽ sang synthesis amino acid, lipid hay nucleotide.

## 2. Catabolism và anabolism phải được coupled

**Catabolism** phá molecule và thường giải phóng free energy. **Anabolism** xây molecule và cần free energy.

Cell giải bài toán này bằng coupling. Catabolic pathway tạo ATP và reduced electron carrier như NADH. Sau đó ATP và reducing power được dùng cho anabolic process.

Ta có thể hình dung như economy:

```text
energy-yielding reactions
       ↓
ATP + reducing power
       ↓
energy-requiring reactions
```

Nếu catabolism và anabolism không được coordinate, cell có thể rơi vào “futile cycle”: vừa xây vừa phá cùng một molecule, waste energy.

Vì vậy metabolism luôn gắn với regulation.

## 3. Redox: theo dõi electron thay vì thuộc pathway

Trong cellular respiration, energy lớn nằm trong electron giàu năng lượng của nutrient.

Khi molecule **bị oxy hóa (oxidized)**, nó mất electron. Khi molecule **bị khử (reduced)**, nó nhận electron.

NAD⁺ nhận electron và proton để thành NADH. FAD thành FADH₂.

Những carrier này giống “xe chở electron” hơn là kho energy lâu dài. Chúng đưa electron tới electron transport chain.

Nếu theo dõi electron, respiration trở nên logic hơn:

```text
nutrient carbon
   ↓ oxidation
NADH / FADH2
   ↓
electron transport chain
   ↓
O2 receives electrons
```

## 4. Glycolysis: tại sao pathway đầu tiên nằm trong cytosol?

**Glycolysis (đường phân / 해당과정)** phân một glucose 6-carbon thành hai pyruvate 3-carbon.

Process diễn ra trong cytosol và không cần mitochondria. Điều này quan trọng về evolutionary history: glycolysis có thể đã xuất hiện rất sớm trước khi eukaryote có mitochondria.

Glycolysis gồm phase đầu tiêu tốn ATP để “activate” glucose, rồi phase sau thu lại nhiều ATP hơn và tạo NADH.

Net per glucose trong model đơn giản:

\[
2 ATP + 2 NADH + 2 pyruvate
\]

Điểm cần hiểu là ATP ở glycolysis được tạo bằng **substrate-level phosphorylation**: phosphate được chuyển trực tiếp từ intermediate sang ADP.

Đây khác cơ chế ATP synthase ở mitochondria.

## 5. Tại sao cần đầu tư ATP trước khi thu ATP?

Việc cell dùng ATP ở đầu glycolysis có vẻ nghịch lý. Nhưng phosphorylation glucose giúp molecule trở nên reactive hơn và giữ nó trong cell vì charged molecule khó qua membrane tự do.

Đây là pattern phổ biến: system bỏ một khoản energy nhỏ để tạo intermediate có potential cho downstream process lớn hơn.

## 6. Pyruvate là điểm rẽ

Sau glycolysis, pyruvate có nhiều fate tùy organism, oxygen và tissue.

Trong aerobic respiration ở eukaryote, pyruvate vào mitochondria, được chuyển thành **acetyl-CoA**, giải phóng CO₂ và tạo NADH.

Acetyl-CoA không chỉ từ glucose; fatty acid và một số amino acid cũng có thể converged vào đây. Vì vậy acetyl-CoA là metabolic hub.

## 7. Citric-acid cycle: mục tiêu chính không phải ATP trực tiếp

**Citric acid cycle / Krebs cycle / TCA cycle (시트르산 회로)** xảy ra chủ yếu trong mitochondrial matrix.

Acetyl group 2-carbon được oxidized hoàn toàn thành CO₂. Cycle tạo một ít ATP/GTP nhưng output quan trọng hơn là NADH và FADH₂.

Vì sao? Vì electron carrier này sẽ cung cấp electron cho stage tạo phần lớn ATP.

Nếu chỉ đếm ATP ngay trong TCA, ta sẽ bỏ lỡ mục đích thực của cycle: **thu electron có năng lượng cao vào carrier**.

## 8. Electron transport chain: biến redox energy thành proton gradient

Electron transport chain nằm ở inner mitochondrial membrane.

Electron từ NADH và FADH₂ đi qua nhiều protein complex. Mỗi transfer đi theo hướng giảm free energy. Một phần energy được dùng để pump proton H⁺ từ matrix ra intermembrane space.

Kết quả là proton concentration bên ngoài cao hơn bên trong, đồng thời có charge separation.

Ta đã tạo **proton-motive force**.

Điều kỳ diệu về mặt logic là cell chưa tạo ATP ở bước này. Nó chuyển energy từ electron thành gradient.

```text
electron energy
    ↓
protein complexes
    ↓
proton pumping
    ↓
electrochemical gradient
```

## 9. Chemiosmosis: gradient trở thành ATP

Proton muốn quay về matrix theo electrochemical gradient. Nhưng inner membrane không cho proton tự do đi qua dễ dàng. Route chính là **ATP synthase**.

Proton flow qua enzyme làm phần protein quay và thay đổi conformation, thúc đẩy:

\[
ADP + P_i \rightarrow ATP
\]

Đây là **oxidative phosphorylation**.

Mental model quan trọng:

> Mitochondria không “đốt glucose để phun ATP ra”. Nó dùng oxidation để tạo electron flow, electron flow tạo proton gradient, và proton gradient lái ATP synthase.

## 10. Vì sao oxygen cần thiết?

Oxygen là **terminal electron acceptor** ở cuối electron transport chain trong aerobic respiration.

Nếu không có acceptor cuối, electron chain bị nghẽn. NADH không được oxidized trở lại NAD⁺ đủ nhanh. Nếu NAD⁺ thiếu, glycolysis và TCA không thể tiếp tục bình thường.

Do đó oxygen không phải “nguyên liệu trực tiếp để tạo ATP” theo kiểu ATP chứa oxygen. Vai trò chính là giữ dòng electron tiếp tục.

## 11. Fermentation: giải pháp khi electron chain không chạy

Khi oxygen thiếu hoặc organism không dùng aerobic respiration, cell vẫn cần regenerate NAD⁺ để glycolysis tiếp tục.

**Fermentation (lên men / 발효)** chuyển electron từ NADH sang organic molecule, tái tạo NAD⁺.

Ở muscle trong intense exercise, pyruvate có thể thành lactate. Ở yeast, pyruvate có thể thành ethanol + CO₂.

Fermentation tạo ít ATP hơn respiration vì phần lớn energy của glucose vẫn còn trong product hữu cơ.

## 12. Fat metabolism: tại sao fat giàu energy hơn carbohydrate?

Fatty acid chứa nhiều reduced carbon và hydrogen. **Beta oxidation** cắt fatty acid thành acetyl-CoA đồng thời tạo NADH và FADH₂.

Vì fatty acid rất reduced, oxidation giải phóng nhiều electron, cuối cùng tạo nhiều ATP hơn trên mỗi carbon so với carbohydrate.

Điều này nối chemistry của lipid với physiology: fat là compact long-term energy store.

## 13. Photosynthesis: đảo chiều câu hỏi về nguồn electron và carbon

Animal lấy carbon và energy từ organic food. Plant có thể lấy carbon từ CO₂ và energy từ light.

**Photosynthesis (quang hợp / 광합성)** không đơn giản là “plant tạo oxygen”. Nó giải hai bài toán:

1. chuyển light energy thành chemical energy;
2. dùng energy đó để reduce carbon từ CO₂ thành organic molecule.

## 14. Light reaction: photon tạo electron flow

Trong chloroplast, light được hấp thụ bởi pigment như chlorophyll.

Photon kích thích electron lên energy state cao hơn. Electron này được truyền qua electron transport chain ở thylakoid membrane.

Flow electron lại được dùng để pump proton và tạo gradient. ATP synthase dùng proton gradient để tạo ATP — cùng motif chemiosmosis đã gặp ở mitochondria.

Nhưng photosynthesis còn tạo NADPH, cung cấp reducing power.

```text
light
 ↓
excited electron
 ↓
electron transport
 ↓
proton gradient
 ↓
ATP
+
NADPH
```

## 15. Water và oxygen trong photosynthesis

Photosystem II lấy electron từ water:

\[
2H_2O \rightarrow O_2 + 4H^+ + 4e^-
\]

Oxygen ta thở phần lớn có nguồn từ water splitting, không trực tiếp từ CO₂.

Đây là một misconception phổ biến.

## 16. Calvin cycle: carbon fixation cần ATP và reducing power

Light reaction tạo ATP và NADPH. **Calvin cycle** dùng chúng để cố định CO₂ thành carbohydrate precursor.

Enzyme Rubisco gắn CO₂ vào molecule acceptor. Qua chuỗi reaction, carbon được chuyển vào organic form.

Điểm quan trọng là photosynthesis tách hai việc:

- light reaction tạo energy currency và reducing power;
- carbon fixation dùng chúng để xây carbon skeleton.

## 17. Respiration và photosynthesis không phải hai “phương trình ngược nhau” đơn giản

Ta thường viết:

\[
6CO_2+6H_2O \rightarrow C_6H_{12}O_6+6O_2
\]

và respiration theo chiều ngược.

Nhưng trong cell, hai process không phải reverse pathway của nhau. Chúng dùng enzyme, compartment và intermediate khác nhau.

Điều giống nhau sâu hơn nằm ở **energy logic**: cả hai đều dùng membrane electron transport và proton gradient.

Đây là một connection quan trọng hơn việc thuộc hai equation tổng quát.

## 18. Metabolism nối với ecology như thế nào?

Photosynthesis đưa energy ánh sáng và carbon vô cơ vào biosphere dưới dạng chemical energy và organic carbon. Respiration trả carbon về CO₂ và giải phóng energy để organism hoạt động.

Ở ecosystem scale:

```text
Sunlight
  ↓
primary producers
  ↓ organic matter
consumers + decomposers
  ↓
respiration
  ↓
CO2 + heat
```

Energy flow một chiều, trong khi matter như carbon được cycle.

Một pathway ở chloroplast vì thế cuối cùng trở thành global carbon cycle.

## 19. Metabolism nối với physiology như thế nào?

Khi chạy, muscle ATP consumption tăng. Phosphocreatine, glycolysis và oxidative phosphorylation đóng góp theo time scale khác nhau. Heart và lung phải tăng oxygen delivery và CO₂ removal. Liver có thể duy trì glucose availability.

Vì vậy metabolic demand ở cell scale gây response ở whole-body scale.

Đây là lý do physiology không thể học tách khỏi cellular metabolism.

## 20. Tại sao metabolism phải được regulation?

Nếu ATP cao, cell thường không cần tiếp tục chạy catabolic pathway tối đa. Nếu substrate thiếu, pathway phải chậm lại. Nếu hormone báo trạng thái fasting, liver metabolism đổi khác trạng thái fed.

Regulation có thể xảy ra qua:

- allosteric enzyme control;
- phosphorylation;
- substrate availability;
- compartment transport;
- gene expression;
- hormone signaling.

Như vậy câu hỏi tiếp theo xuất hiện tự nhiên: **cell biết trạng thái bên ngoài và bên trong bằng cách nào, rồi truyền thông tin đó tới enzyme và gene ra sao?**

Đó là nội dung của [[02_cell_signaling_and_cell_cycle]].