# Sinh lý động vật và Cân bằng nội môi — Animal Physiology and Homeostasis (동물생리학과 항상성)

Plant giải bài toán multicellularity bằng vascular transport và growth modular. Animal cũng phải vận chuyển matter, energy và information giữa cell xa nhau, nhưng thường có thêm constraint: movement nhanh, metabolic demand cao và internal environment phải được giữ ổn định dù activity thay đổi liên tục.

Chapter này không phải atlas anatomy. Mỗi organ system sẽ được xem như một lời giải cho một physical/chemical problem: circulation giải bài toán bulk transport, lung giải gas exchange, kidney giải water/ion/waste control, digestion giải nutrient acquisition, thermoregulation giải heat balance.

> **Mental model:** animal body là một network transport + exchange + control. Blood là moving internal environment; organ là specialized interface; homeostasis là feedback giữ các variable quan trọng trong range phù hợp.

## 1. Tại sao diffusion không đủ cho organism lớn?

Diffusion hiệu quả ở distance ngắn. Khi body dày lên, cell sâu bên trong quá xa external environment.

Vì diffusion time tăng xấp xỉ theo bình phương distance, multicellular animal lớn cần **bulk flow**: fluid được pump qua vessel để đưa material nhanh tới gần cell, rồi diffusion hoàn thành đoạn cuối.

Circulation không thay thế diffusion; nó rút ngắn distance diffusion.

## 2. Homeostasis là dynamic regulation

Variable như temperature, glucose, osmolarity, pH và blood pressure không được giữ một giá trị tuyệt đối. Chúng dao động trong range, có set point/context khác nhau.

Một feedback loop cơ bản:

```text
controlled variable
→ sensor
→ integrating center
→ effector
→ variable changes
```

Negative feedback làm deviation giảm. Positive feedback thường dùng cho process cần completion nhanh như blood clotting hoặc childbirth.

## 3. Circulatory system: pressure tạo flow

Heart tạo pressure difference, blood flow từ nơi pressure cao tới thấp qua vascular resistance.

Một relation gần tương tự Ohm’s law:

\[
Flow=\frac{\Delta P}{R}
\]

Resistance phụ thuộc mạnh radius vessel. Trong idealized laminar flow, Poiseuille relation cho thấy:

\[
R\propto\frac{1}{r^4}
\]

Radius thay nhỏ có thể đổi flow lớn. Đây là lý do arteriole vasoconstriction/vasodilation là tool mạnh điều phối blood flow.

## 4. Heart: pump nối hai circulation

Mammalian heart có right side bơm blood tới lung và left side bơm systemic circulation.

Valve giữ one-way flow. Cardiac muscle co theo electrical conduction system.

Stroke volume × heart rate cho cardiac output:

\[
CO=SV\times HR
\]

Khi exercise, cardiac output tăng để đáp ứng oxygen/nutrient demand và remove CO₂/heat.

## 5. Artery, capillary, vein khác nhau vì function khác

Artery chịu pressure cao nên wall dày/elastin. Capillary có wall rất mỏng để exchange. Vein pressure thấp hơn, lumen lớn và valve hỗ trợ return ở limb.

Total cross-sectional area của capillary network rất lớn, làm flow velocity giảm, tăng time exchange.

Structure–function rõ ràng ở vascular tree.

## 6. Blood: transport medium sống

Blood gồm plasma và formed elements.

Red blood cell mang hemoglobin; white blood cell tham gia immunity; platelet tham gia clotting.

Plasma mang nutrient, hormone, waste, protein và ion.

Blood không chỉ “chở oxygen”; nó là shared internal environment kết nối organ.

## 7. Hemoglobin: binding phải vừa đủ mạnh và vừa đủ yếu

Hemoglobin bind oxygen ở lung nơi partial pressure cao và release ở tissue nơi thấp hơn.

Oxygen-binding curve có sigmoid shape do cooperativity.

Nếu hemoglobin bind O₂ quá chặt, loading tốt nhưng unloading kém. pH, CO₂, temperature có thể shift affinity để phù hợp active tissue.

Đây là molecular allostery trở thành whole-body physiology.

## 8. Gas exchange phụ thuộc partial pressure

O₂ diffuse theo partial-pressure gradient từ alveoli → blood → tissue. CO₂ đi hướng ngược.

Lung có diện tích lớn, barrier mỏng và ventilation liên tục duy trì gradient.

Fick principle: exchange tăng với area và gradient, giảm khi barrier dày.

Disease làm alveolar wall dày hoặc giảm area sẽ giảm gas exchange.

## 9. Ventilation và perfusion phải match

Air tới alveoli gọi ventilation; blood tới alveoli gọi perfusion.

Nếu alveolus có air nhưng không blood, O₂ không được transport đi. Nếu có blood nhưng không air, gas exchange cũng kém.

V/Q matching cho thấy physiology là coordination giữa hệ, không phải sum của organ riêng lẻ.

## 10. CO₂ và acid–base regulation

CO₂ trong blood liên hệ bicarbonate equilibrium:

\[
CO_2+H_2O\rightleftharpoons H_2CO_3\rightleftharpoons H^++HCO_3^-
\]

Ventilation thay CO₂ nhanh; kidney điều chỉnh H⁺/HCO₃⁻ chậm hơn nhưng mạnh lâu dài.

Lung và kidney cùng giữ pH — một ví dụ homeostasis đa cơ quan.

## 11. Digestion: từ food lớn tới molecule có thể absorb

Digestive system thực hiện mechanical breakdown, chemical digestion, absorption và elimination.

Carbohydrate → monosaccharide; protein → amino acid/peptide; lipid → fatty acid/monoglyceride.

Enzyme digest macromolecule vì molecule lớn không qua intestinal epithelium nguyên vẹn dễ dàng.

## 12. Small intestine tối ưu cho absorption

Fold, villi và microvilli tăng surface area. Capillary nhận sugar/amino acid; lymphatic lacteal nhận nhiều lipid package dạng chylomicron.

Epithelial membrane dùng transporter và gradient giống cell chapter.

Whole-organ absorption là repetition của membrane transport ở scale lớn hơn.

## 13. Liver: metabolic hub

Liver nhận nutrient từ gut qua portal circulation. Nó điều chỉnh glucose storage/release, amino-acid metabolism, lipid metabolism, detoxification và bile production.

Liver không “lọc độc” theo nghĩa một filter thụ động; enzyme chuyển hóa compound thành form dễ excrete hoặc ít/đôi khi nhiều reactive hơn.

## 14. Kidney: filter rồi chọn lại, không chỉ “lọc chất thải”

Kidney nhận blood và tạo filtrate ở glomerulus. Nhưng nếu chỉ filtration, body sẽ mất water, glucose và ion.

Nephron sau đó **reabsorb** chất cần, **secrete** thêm một số chất và cuối cùng excrete urine.

```text
filtration
→ selective reabsorption
→ secretion
→ excretion
```

Kidney là control system tinh vi cho volume, osmolarity, electrolyte, pH và blood pressure.

## 15. Nephron và countercurrent mechanism

Loop of Henle tạo osmotic gradient trong renal medulla nhờ countercurrent arrangement và differential permeability.

Gradient này cho phép collecting duct reabsorb water hiệu quả khi ADH làm tăng aquaporin.

Một architecture spatial đặc biệt tạo khả năng concentrate urine.

## 16. ADH và water balance

Khi plasma osmolarity tăng, osmoreceptor góp phần kích thích ADH release. ADH làm collecting duct tăng water permeability → reabsorb water nhiều hơn → urine cô đặc hơn.

Negative feedback kéo osmolarity về range.

Hormone control được xây trên membrane protein/aquaporin.

## 17. RAAS và blood pressure/volume

Renin–angiotensin–aldosterone system được activate khi renal perfusion/salt signal phù hợp. Angiotensin II gây vasoconstriction và stimulate aldosterone; aldosterone tăng Na⁺ reabsorption ở nephron, water follow osmotically.

RAAS nối kidney, vessel và endocrine control.

## 18. Thermoregulation

Body heat balance gồm metabolic heat production và heat loss qua radiation, conduction, convection, evaporation.

Sweating dùng latent heat of vaporization; vasodilation tăng heat transfer tới skin; shivering tăng muscular heat production.

Temperature control không phải “giữ 37.0°C tuyệt đối”; có circadian variation và set-point change trong fever.

## 19. Fever khác hyperthermia

Trong fever, inflammatory signal làm hypothalamic set point tăng; body cảm thấy lạnh relative new set point và gây shivering/vasoconstriction.

Trong hyperthermia, set point không tăng nhưng heat production/input vượt heat loss.

Mechanism khác nên cách reasoning clinical khác.

## 20. Muscle contraction: ATP + ion + protein

Skeletal muscle contraction dựa actin–myosin sliding filament.

Nerve signal làm Ca²⁺ release từ sarcoplasmic reticulum; Ca²⁺ bind troponin, cho myosin tương tác actin. ATP cần cho cross-bridge cycling và Ca²⁺ pumping.

Cell signaling, ion gradient, ATP và cytoskeleton hội tụ thành movement.

## 21. Bone không phải structure chết

Bone là tissue dynamic, liên tục remodel bởi osteoblast/osteoclast. Nó hỗ trợ body, bảo vệ organ, store mineral và chứa marrow.

Mechanical load ảnh hưởng remodeling; hormone và calcium/phosphate balance liên quan bone physiology.

## 22. Exercise như stress test của toàn system

Khi running:

- muscle ATP demand tăng;
- respiration tăng;
- CO₂/heat tăng;
- cardiac output tăng;
- blood flow redistribute;
- ventilation tăng;
- sweating/skin blood flow điều chỉnh heat.

Không hệ nào “làm việc một mình”. Exercise là example systems physiology lý tưởng.

## 23. Endocrine pancreas và glucose homeostasis

Beta cell release insulin khi glucose signal phù hợp; alpha cell release glucagon trong fasting context.

Insulin thúc đẩy glucose uptake/storage ở tissue thích hợp; glucagon thúc đẩy liver glucose output.

Blood glucose là variable được điều chỉnh bằng multi-organ feedback, không phải chỉ pancreas.

## 24. Acid–base: lung và kidney phối hợp trên timescale khác

Respiratory adjustment đổi CO₂ trong minutes. Kidney excrete H⁺, regenerate/reabsorb bicarbonate trong hours–days.

Nếu một hệ bị rối, hệ kia có thể compensate phần nào nhưng không hoàn toàn.

Physiology thường có redundancy và compensation.

## 25. Allostasis: body đôi khi thay set point để dự đoán demand

Homeostasis thường mô tả correction sau deviation. **Allostasis** nhấn mạnh body có thể anticipatory adjust theo context — circadian hormone, exercise preparation, stress response.

Một system tốt không chỉ sửa lỗi; nó dự đoán demand.

## 26. Case study: dehydration

Mất water làm plasma osmolarity tăng và volume giảm. Thirst, ADH và RAAS được activate; kidney giữ water/Na⁺ tùy signal; heart/vessel response giữ perfusion.

Nếu dehydration nặng, compensation không đủ → blood pressure/perfusion giảm.

Một symptom “khát” phản ánh integrated sensing/control network.

## 27. Case study: high altitude

Ở altitude cao, partial pressure O₂ thấp. Acute response gồm hyperventilation và cardiovascular change. Qua ngày/tuần có acclimatization: kidney điều chỉnh acid–base, erythropoietin tăng red-cell production và tissue adaptation.

Đây là phenotypic plasticity trong đời, khác genetic adaptation population sống lâu ở high altitude.

## 28. Common misconceptions

“Artery luôn mang oxygen-rich blood” sai; pulmonary artery mang deoxygenated blood.

“Kidney chỉ lọc độc” sai; kidney chủ yếu điều chỉnh composition internal environment qua filtration + reabsorption + secretion.

“Sweat làm mát vì nước lạnh” sai; evaporation mang heat đi.

“Digestion tạo energy trực tiếp” sai; digestion tạo absorbable molecule, cellular respiration mới convert chemical energy thành ATP.

“Homeostasis giữ value không đổi” sai; regulation giữ dynamic range.

## 29. Bridge: coordination cần hệ truyền thông nhanh và chậm

Circulation vận chuyển matter, nhưng organism còn cần information. Khi chạm vật nóng, response phải trong milliseconds; khi điều chỉnh growth/metabolism, signal có thể kéo dài hours–days; khi pathogen xâm nhập, immune system phải nhận dạng và ghi memory.

[[02_nervous_endocrine_and_immune_systems]] sẽ so sánh ba control layer: nervous, endocrine và immune.

> **Mental model cuối chapter:** animal physiology là bài toán giữ internal environment usable cho cell. Organ system không độc lập; lung, heart, kidney, gut, liver và muscle liên kết bằng flow và feedback. Mọi mechanism cuối cùng quay về diffusion, pressure, membrane transport, metabolism và signaling đã học ở cell scale.