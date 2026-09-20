# Sinh lý động vật và cân bằng nội môi — Animal Physiology and Homeostasis (동물생리학·항상성)

Một cơ thể đa bào tồn tại được vì hàng tỷ tế bào chia sẻ một môi trường nội tại tương đối ổn định. Sinh lý học (Physiology / 생리학) nghiên cứu cách các hệ cơ quan phối hợp để duy trì trao đổi vật chất, năng lượng và information. Cân bằng nội môi (Homeostasis / 항상성) là nguyên lý trung tâm: cơ thể giữ các biến như nhiệt độ, glucose, pH, osmolarity và huyết áp trong khoảng hoạt động phù hợp thay vì cố định tuyệt đối ở một con số.

## Homeostasis là regulation động

Một hệ homeostatic thường có sensor, control mechanism và effector. Khi variable lệch khỏi range, negative feedback tạo response đưa hệ trở về vùng phù hợp.

Ví dụ, khi blood glucose tăng sau bữa ăn, pancreatic beta cell tiết insulin. Insulin tăng glucose uptake ở một số tissue và thúc đẩy storage. Khi glucose giảm, glucagon tăng và thúc đẩy mobilization glucose.

> Mental model: homeostasis không phải “giữ mọi thứ không đổi”, mà là giữ system bên trong một vùng ổn định động mặc dù input và demand luôn thay đổi.

## Nội môi và trao đổi qua bề mặt

Single cell có thể trao đổi trực tiếp với môi trường. Animal lớn cần hệ chuyên hóa vì diffusion không đủ nhanh trên khoảng cách lớn. Respiratory surface lấy gas, digestive system hấp thu nutrient, circulatory system phân phối và excretory system loại waste.

Scale giải thích vì sao các surface trao đổi thường rất lớn và mỏng: lung alveoli, intestinal villi, capillary network và kidney tubule đều tối ưu surface area và diffusion distance.

## Hệ tuần hoàn

Tim tạo pressure gradient để blood flow qua vessel. Flow có thể mô tả đơn giản bằng:

```math
Q=\frac{\Delta P}{R}
```

Trong đó `Q` là flow, `ΔP` là pressure difference và `R` là resistance. Với laminar flow trong ống lý tưởng, resistance phụ thuộc rất mạnh vào radius, gần theo `1/r^4`. Điều này giúp giải thích vì sao thay đổi nhỏ đường kính arteriole có thể điều chỉnh blood flow mạnh.

Artery đưa blood rời tim; vein đưa blood về tim. Đây là định nghĩa theo direction, không phải theo oxygen content. Pulmonary artery mang blood ít oxygen, còn pulmonary vein mang blood giàu oxygen.

## Trao đổi khí và hemoglobin

O₂ khuếch tán theo partial-pressure gradient từ alveoli vào blood và từ blood vào tissue. CO₂ đi theo chiều ngược lại.

Hemoglobin binding oxygen theo cooperativity. Khi một O₂ gắn, affinity cho O₂ tiếp theo tăng, tạo sigmoidal dissociation curve. pH thấp và CO₂ cao có thể làm affinity giảm, giúp giải phóng O₂ ở tissue đang hoạt động mạnh.

## Tiêu hóa và hấp thu

Digestive system phá macromolecule thành đơn vị nhỏ có thể hấp thu. Enzyme hydrolyze carbohydrate, protein và lipid. Small intestine có villi và microvilli để tăng surface area.

Lipid absorption khác carbohydrate và amino acid vì lipid kỵ nước. Fatty acid và monoglyceride được đóng gói lại thành chylomicron rồi đi qua lymph trước khi vào blood circulation.

## Kidney và cân bằng nước–ion

Kidney lọc plasma tại glomerulus rồi chọn lọc reabsorption và secretion dọc nephron. Điểm quan trọng là urine không phải chỉ là “phần bị lọc bỏ”; composition cuối cùng là kết quả của filter + selective reclaim + active secretion.

Countercurrent mechanism ở loop of Henle tạo osmotic gradient trong renal medulla. ADH tăng water permeability ở collecting duct, giúp cơ thể giữ nước khi cần.

## Thermoregulation

Endotherm như mammal tạo và giữ heat để duy trì body temperature tương đối ổn định. Heat exchange với environment xảy ra qua conduction, convection, radiation và evaporation.

Sweating làm mát vì evaporation cần latent heat. Trong môi trường humid, evaporation kém hiệu quả nên cảm giác nóng tăng dù air temperature giống nhau.

## Muscle contraction

Skeletal muscle contraction dựa trên sliding-filament mechanism. Ca²⁺ làm lộ binding site trên actin; myosin head dùng ATP để cycle giữa attachment, power stroke và release.

ATP không chỉ “cung cấp năng lượng để co”; nó còn cần cho myosin detach khỏi actin. Điều này giải thích rigor mortis khi ATP cạn sau death.

## Acid–base balance

Blood pH được buffer bởi bicarbonate system và điều chỉnh bởi lung cùng kidney:

```math
CO_2 + H_2O \rightleftharpoons H_2CO_3 \rightleftharpoons H^+ + HCO_3^-
```

Lung thay đổi CO₂ nhanh qua ventilation; kidney điều chỉnh H⁺ và bicarbonate chậm hơn nhưng mạnh về dài hạn.

## Common misconceptions

“Máu xanh trong vein” là sai; blood luôn đỏ, màu thay đổi theo oxygenation. Vein nhìn xanh dưới da do optical properties của tissue và light.

“Homeostasis nghĩa là mọi variable luôn đúng một giá trị” cũng sai. Biological control thường giữ variable trong range và có circadian, activity-dependent hoặc developmental variation.

## Kết nối

Membrane transport trong [[../01_cell_biology/00_cells_membranes_and_transport]] là nền cho ion balance và kidney function. Metabolism trong [[../01_cell_biology/01_metabolism_respiration_photosynthesis]] giải thích ATP demand. Neural, endocrine và immune control được phát triển trong [[02_nervous_endocrine_and_immune_systems]].
