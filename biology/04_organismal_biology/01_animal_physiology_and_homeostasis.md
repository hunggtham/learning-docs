# Sinh lý động vật và cân bằng nội môi — Animal Physiology and Homeostasis (동물생리학과 항상성)

Plant giải bài toán vận chuyển và điều hòa bằng xylem, phloem, stomata và hormone. Animal đối mặt cùng bài toán nhưng thường có metabolic demand cao hơn và movement nhanh hơn. Khi muscle hoạt động, oxygen phải đến nhanh; CO₂ và heat phải được đưa đi; ion, pH, glucose và water phải được giữ trong vùng thích hợp.

Vì vậy animal physiology không nên học như một danh sách “hệ tuần hoàn, hô hấp, tiêu hóa, bài tiết”. Tất cả các hệ này là những module phối hợp để bảo vệ **internal environment** của cell.

## 1. Homeostasis là bài toán trung tâm

Một cell chỉ hoạt động tốt trong range nhất định của temperature, pH, ion, oxygen và nutrient. Nhưng external environment thay đổi liên tục.

**Homeostasis (cân bằng nội môi / 항상성)** là khả năng duy trì variable sinh lý trong range phù hợp nhờ sensing, control và response.

Ta có generic loop:

```text
controlled variable
      ↓
sensor
      ↓
integrating center
      ↓
effector
      ↓
negative feedback
```

Ví dụ blood glucose tăng sau bữa ăn. Pancreatic beta cell sense glucose, insulin tăng, tissue uptake/storage glucose tăng, blood glucose hạ.

Đây không phải một exception. Cùng control logic xuất hiện ở blood pressure, body temperature, osmolality và pH.

## 2. Internal environment là extracellular fluid

Cell trong body đa bào không trực tiếp tiếp xúc external world. Chúng được bathing trong **extracellular fluid**.

Circulatory system, lung, intestine và kidney cùng nhau điều chỉnh composition của fluid này.

Ta có thể xem physiology như logistics system:

```text
external environment
   ↓ intestine / lung
blood and extracellular fluid
   ↓
body cells
   ↓
waste
   ↓ lung / kidney / liver
external environment
```

Điểm này giúp nối các organ system thay vì học tách riêng.

## 3. Circulation: vì diffusion một mình không đủ

Diffusion hiệu quả ở distance ngắn. Khi organism lớn, oxygen từ lung không thể diffusion trực tiếp vài chục centimet tới muscle đủ nhanh.

Circulatory system giải quyết bằng **bulk flow**: heart tạo pressure gradient, blood mang substance đi xa, rồi diffusion chỉ cần xử lý đoạn cuối từ capillary tới cell.

Đây là ví dụ classic cho việc organism kết hợp hai transport mode:

```text
long distance: bulk flow
short distance: diffusion
```

## 4. Heart là pump tạo pressure gradient

Heart không “đẩy oxygen” trực tiếp. Nó tạo pressure difference làm blood flow.

Một relationship đơn giản:

\[
Flow \approx \frac{\Delta P}{R}
\]

Flow tăng khi pressure difference tăng và giảm khi resistance tăng.

Resistance vessel phụ thuộc mạnh radius; vì vậy arteriole nhỏ có thể regulation flow bằng constriction/dilation.

Điều này nối anatomy vessel với physics của fluid flow.

## 5. Cardiac output nối heart rate và stroke volume

Lượng blood heart bơm mỗi phút:

\[
CO = HR \times SV
\]

Trong đó HR là heart rate, SV là stroke volume.

Khi exercise, sympathetic signal tăng heart rate và contractility; muscle vessel dilate; venous return tăng. Whole system điều chỉnh để oxygen delivery match metabolic demand.

Từ metabolism ở muscle, ta đã đi lên cardiovascular response.

## 6. Gas exchange: diffusion qua surface mỏng

Lung alveoli tạo diện tích bề mặt rất lớn với barrier mỏng.

Oxygen diffuse từ alveolar air vào blood theo partial-pressure gradient. CO₂ đi chiều ngược.

Hemoglobin trong red blood cell bind oxygen, làm blood mang lượng O₂ lớn hơn rất nhiều so với chỉ hòa tan trong plasma.

Structure–function lại xuất hiện: thin membrane + huge area + dense capillary network = efficient gas exchange.

## 7. Hemoglobin: binding phải vừa đủ mạnh

Nếu hemoglobin bind O₂ quá yếu, lung không load tốt. Nếu quá mạnh, tissue không nhận O₂.

Oxygen-binding curve có tính cooperative: binding một O₂ làm các site còn lại dễ bind hơn.

Ở tissue có CO₂ cao và pH thấp, hemoglobin affinity với O₂ giảm, hỗ trợ release. Đây là **Bohr effect**.

Một molecule protein vì thế phản ứng với local metabolic condition để cải thiện whole-body delivery.

## 8. CO₂, bicarbonate và pH nối lung với kidney

CO₂ trong blood tham gia equilibrium:

\[
CO_2 + H_2O \leftrightarrow H_2CO_3 \leftrightarrow H^+ + HCO_3^-
\]

Nếu CO₂ tăng, equilibrium có thể tăng H⁺, làm pH giảm.

Lung điều chỉnh CO₂ nhanh bằng ventilation. Kidney điều chỉnh H⁺ và bicarbonate chậm hơn nhưng mạnh trong long-term acid–base balance.

Một equation hóa học ở foundation giờ trở thành phối hợp giữa hai organ system.

## 9. Digestion: biến food thành molecule cell có thể dùng

Food chứa polymer và molecule lớn. Intestine không thể absorb nguyên protein hoặc starch hiệu quả như vậy.

Digestion dùng enzyme để breakdown carbohydrate thành monosaccharide, protein thành amino acid/peptide, lipid thành fatty acid/monoglyceride.

Sau đó transporter đưa nutrient qua intestinal epithelium.

Microvilli tăng surface area — lại là surface-area-to-volume principle.

## 10. Liver là metabolic hub

Nutrient từ intestine thường đi qua liver trước khi phân phối rộng.

Liver store glycogen, regulate blood glucose, process lipid/amino acid, detoxify many compound và produce plasma protein.

Vì vậy liver nối digestion với metabolism và circulation.

Không nên xem organ system như module kín. Liver là điểm giao của nhiều system.

## 11. Kidney: filter không có nghĩa bỏ tất cả

Kidney nhận blood, filter plasma ở glomerulus rồi selective reabsorption và secretion dọc nephron.

Nếu chỉ “lọc rồi thải”, body sẽ mất glucose, amino acid, ion và water. Logic thật là:

```text
filter broadly
   ↓
reabsorb what should be kept
   ↓
secrete additional waste/ions
   ↓
excrete final urine
```

Đây là strategy khác membrane selectivity ở cell nhưng cùng principle control exchange.

## 12. Nephron và gradient

Loop of Henle góp phần tạo osmotic gradient trong kidney medulla. Gradient cho phép collecting duct reabsorb water tùy hormone signal.

ADH tăng water permeability ở collecting duct, giúp conserve water khi body cần.

Ta lại gặp motif: **tạo gradient trước, sau đó regulation permeability để khai thác gradient**.

## 13. Osmoregulation: water và salt phải được điều chỉnh cùng nhau

Water movement phụ thuộc solute concentration. Nếu body mất water nhiều hơn salt, plasma osmolality tăng. Osmoreceptor detect change; thirst và ADH tăng.

Điều này nối osmosis từ cell biology với behavior (“khát”) và endocrine physiology.

## 14. Thermoregulation: balance giữa heat production và heat loss

Metabolism tạo heat. Exercise tăng heat production.

Body trao đổi heat qua radiation, convection, conduction và evaporation.

Khi nóng, skin blood flow tăng và sweating tăng. Khi lạnh, vasoconstriction giảm heat loss, shivering tăng heat production.

Negative feedback giữ core temperature trong range phù hợp enzyme function.

## 15. Muscle: ATP biến thành mechanical work

Muscle contraction dựa trên actin–myosin sliding.

Myosin hydrolyze ATP để cycle giữa binding state. Ca²⁺ signal expose binding site trên actin regulatory system.

Một contraction vì vậy nối:

```text
nerve signal
 ↓
Ca2+ release
 ↓
actin–myosin interaction
 ↓
ATP hydrolysis
 ↓
force
```

Molecular energy conversion trở thành movement ở organism scale.

## 16. Exercise như bài toán tích hợp nhiều hệ

Khi chạy:

Muscle ATP demand tăng → respiration tăng → O₂ consumption và CO₂ production tăng → ventilation tăng → heart output tăng → skin blood flow và sweating thay đổi → liver và hormone điều chỉnh fuel availability.

Không một organ system nào “chịu trách nhiệm” cho exercise response. Đây là integrated physiology.

## 17. Disease thường là failure của regulation, không chỉ hỏng một bộ phận

Hypertension có thể liên quan vessel resistance, kidney salt handling, nervous/endocrine regulation và vascular remodeling.

Diabetes liên quan insulin production/action, glucose metabolism và long-term vessel/tissue damage.

Physiology giúp hiểu disease như network dysregulation thay vì chỉ tên organ.

## 18. Tại sao bước tiếp theo là nervous, endocrine và immune system?

Ta đã mô tả nhiều response: heart rate đổi, vessel constrict, ADH tăng, insulin release, immune defense. Nhưng system nào coordinate những thay đổi này?

Animal cần ít nhất ba mạng control lớn:

- nervous system: nhanh, spatially precise;
- endocrine system: hormone đi xa, thường chậm hơn nhưng kéo dài;
- immune system: nhận diện threat và điều phối defense.

Ba mạng này cross-talk liên tục.

Tiếp tục với [[02_nervous_endocrine_and_immune_systems]].