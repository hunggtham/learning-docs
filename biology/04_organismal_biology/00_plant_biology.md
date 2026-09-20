# Sinh học thực vật — Plant Biology (식물생물학)

Thực vật thường bị học như danh sách “rễ, thân, lá, hoa”, nhưng cách đó bỏ mất câu hỏi lớn: **một organism không thể đi tìm nước hay thức ăn phải giải quyết việc lấy carbon, nước, mineral, vận chuyển hàng mét và sinh sản như thế nào?**

Plant biology là một bài toán engineering sinh học rất đẹp. Root khai thác soil, leaf khai thác light và CO₂, vascular tissue nối hai vùng, hormone điều phối growth, còn stomata phải liên tục cân bằng CO₂ uptake với water loss.

## Plant không “ăn từ đất”

Một cây tăng khối lượng lớn chủ yếu nhờ carbon từ atmospheric CO₂, không phải vì đất biến trực tiếp thành gỗ.

Photosynthesis cố định carbon:

\[
CO_2 \rightarrow organic\ carbon
\]

Soil cung cấp water và mineral nutrient như nitrogen, phosphorus, potassium, magnesium. Những nguyên tố này rất quan trọng nhưng phần lớn dry mass carbon đến từ air.

Đây là một trong những ví dụ first-principles quan trọng nhất của biology: hãy theo dõi **matter flow**, đừng chỉ nhìn hình dạng organism.

## Ba hệ mô lớn

Plant body có thể được nhìn qua ba **tissue system (hệ mô / 조직계)**.

**Dermal tissue** tạo interface với environment. Epidermis bảo vệ, stomata trao đổi khí, root hair tăng surface area hấp thu.

**Ground tissue** thực hiện photosynthesis, storage và support tùy organ.

**Vascular tissue** gồm xylem và phloem, giải quyết transport distance dài.

## Root — interface với soil

**Root (rễ / 뿌리)** không chỉ neo cây. Nó hấp thu water/mineral và tương tác với microorganism.

### Root hair và surface area

Root hair kéo dài từ epidermal cell, tăng rất nhiều surface area tiếp xúc soil water.

Đây là cùng principle surface-area-to-volume ratio đã gặp ở intestine và lung: khi exchange là bottleneck, biology thường tạo fold, branch hoặc projection để tăng area.

### Mineral uptake

Ion mineral không phải lúc nào tự diffuse vào root. Membrane transporter và proton pump tạo electrochemical gradient giúp uptake.

H⁺-ATPase dùng ATP pump proton ra ngoài, tạo proton motive force. Secondary transporter sau đó có thể dùng gradient để đưa nutrient vào.

Plant root vì vậy ứng dụng chính xác logic active transport ở cell biology.

## Mycorrhiza — root thường làm việc cùng fungi

Nhiều plant tạo mutualistic association với fungi gọi là **mycorrhiza (nấm rễ / 균근)**.

Fungal hyphae mở rộng vùng soil khai thác, giúp plant nhận phosphorus/water; plant cung cấp carbohydrate từ photosynthesis.

Đây là reminder rằng organism trong nature hiếm khi hoạt động cô lập.

## Xylem — làm sao water đi từ root lên tree cao?

**Xylem (mạch gỗ / 물관)** vận chuyển water và dissolved mineral chủ yếu từ root lên shoot.

Các conducting cell khi mature thường chết và tạo tube có wall lignified, giảm resistance và chống collapse.

### Transpiration

Water evaporate từ moist cell surface trong leaf rồi thoát qua stomata. Quá trình này gọi là **transpiration (thoát hơi nước / 증산)**.

Evaporation làm water potential ở leaf giảm, tạo tension kéo cột water trong xylem upward.

### Cohesion–tension mechanism

Water molecule cohesion nhờ hydrogen bond giúp cột water liên tục. Adhesion với xylem wall cũng hỗ trợ.

Không cần một “pump” ở top tree đẩy water lên. Driving force lớn đến từ evaporation + water potential gradient.

> **Mental model:** xylem giống một cột water đang bị “kéo” từ leaf hơn là được root “đẩy” toàn bộ lên.

## Water potential — hướng water movement

Plant physiology thường dùng **water potential (thế nước / 수분퍼텐셜)** ký hiệu \(\Psi\).

Water có xu hướng di chuyển từ nơi water potential cao hơn đến thấp hơn.

Một simplification:

\[
\Psi = \Psi_s + \Psi_p
\]

với \(\Psi_s\) là solute potential và \(\Psi_p\) là pressure potential.

Thêm solute làm solute potential âm hơn. Turgor pressure làm pressure potential tăng.

Concept này tổng quát hơn chỉ nói osmosis vì plant phải xét cả solute và pressure.

## Phloem — transport sugar từ source đến sink

**Phloem (mạch rây / 체관)** vận chuyển sugar và nhiều signaling molecule giữa source và sink.

**Source** là region net export sugar, thường mature leaf.

**Sink** là region net import, như root, fruit, young leaf hoặc storage organ.

Trong **pressure-flow model**, sugar loading làm water vào phloem bằng osmosis, tăng hydrostatic pressure; pressure difference drive bulk flow đến sink.

Một organ có thể đổi role theo season/development. Storage root có thể là sink khi tích trữ và source khi mobilize reserve.

## Leaf — architecture cho photosynthesis và gas exchange

Leaf thường broad và thin, giúp capture light và giảm diffusion distance.

**Mesophyll** chứa nhiều chloroplast.

Internal air space giúp CO₂ diffuse đến photosynthetic cell.

**Stomata (khí khổng / 기공)** là pore controlled bởi guard cell.

## Stomata — trade-off giữa carbon và water

Để photosynthesis, plant cần CO₂ vào leaf. Nhưng mở stomata cũng làm water vapor thoát.

Đây là fundamental trade-off:

```text
mở stomata
→ CO₂ vào nhiều hơn
→ photosynthesis có thể tăng
BUT
→ water loss tăng
```

Guard cell điều chỉnh stomatal aperture theo light, CO₂, humidity, water status và hormone.

Khi drought, hormone ABA thường góp phần làm stomata đóng, giảm water loss nhưng cũng hạn chế carbon uptake.

Plant không tối ưu một variable; nó cân bằng nhiều constraint.

## Photosynthesis trong context whole plant

Chloroplast light reaction tạo ATP/NADPH; Calvin cycle cố định CO₂.

Nhưng photosynthesis rate whole plant còn phụ thuộc stomatal conductance, leaf temperature, nitrogen supply, source–sink relationship và water status.

Vì vậy “nhiều ánh sáng hơn = luôn photosynthesis cao hơn” không đúng vô hạn. Light saturation và stress có thể giới hạn.

## Growth — plant lớn lên từ meristem

**Meristem (mô phân sinh / 분열조직)** chứa cell có khả năng division và differentiation.

**Apical meristem** ở root/shoot tip tạo primary growth, kéo dài body.

**Lateral meristem** như vascular cambium tạo secondary growth, làm stem/root dày lên ở woody plant.

Plant growth khác animal vì nhiều organ được tạo liên tục suốt đời từ meristem.

## Plant hormone — signal phối hợp growth

### Auxin

**Auxin (옥신)** ảnh hưởng cell elongation, apical dominance, root development và tropism.

Trong phototropism, asymmetric auxin distribution có thể làm một side stem elongate nhiều hơn, khiến shoot bend toward light.

### Gibberellin

**Gibberellin (지베렐린)** liên quan stem elongation, seed germination và developmental transition.

### Cytokinin

**Cytokinin (사이토키닌)** liên quan cell division và nhiều aspect development; effect phụ thuộc interaction với auxin và tissue context.

### Abscisic acid

**ABA (앱시스산)** quan trọng trong drought response, stomatal closure và seed dormancy.

### Ethylene

**Ethylene (에틸렌)** là gaseous hormone liên quan fruit ripening, senescence và stress response.

Hormone không có một function duy nhất. Meaning phụ thuộc concentration, tissue, developmental state và cross-talk.

## Tropism — growth theo direction stimulus

**Tropism (hướng động / 굴성)** là directional growth response.

Phototropism phản ứng với light; gravitropism phản ứng gravity.

Root thường positive gravitropic, shoot negative gravitropic. Gravity-sensing organelle và auxin redistribution góp phần tạo differential growth.

Tropism cho thấy plant “respond” dù không có nervous system.

## Plant reproduction — flower là structure cho sexual reproduction

Flowering plant tạo pollen chứa male gametophyte và ovule chứa female gametophyte.

**Pollination (thụ phấn / 수분)** là transfer pollen đến compatible reproductive structure, không đồng nghĩa fertilization.

Sau pollen germination, pollen tube đưa sperm cell tới ovule.

Angiosperm có **double fertilization**: một sperm fertilize egg tạo zygote, sperm khác hợp với central cell tạo endosperm tissue nuôi embryo.

Ovule phát triển thành seed; ovary thường phát triển thành fruit.

## Seed — package của embryo

Seed chứa embryo, nutrient reserve tùy species và protective coat.

Dormancy giúp embryo chờ environment phù hợp.

Germination bắt đầu khi water, temperature và signal phù hợp. Metabolism tăng, reserve mobilize, root thường emerge trước để establish water uptake.

## Alternation of generations

Plant life cycle có cả multicellular **sporophyte (2n)** và **gametophyte (n)**.

Meiosis trong sporophyte tạo spore, không trực tiếp tạo gamete như animal. Spore grow thành gametophyte; gametophyte tạo gamete bằng mitosis.

Fertilization tạo zygote 2n, phát triển thành sporophyte.

Đây là điểm dễ nhầm nếu đem animal meiosis model áp thẳng sang plant.

## Plant evolution — từ water lên land

Land plant phải giải quyết dehydration, support, gas exchange và reproduction không phụ thuộc water tự do.

Key innovations qua lineage gồm cuticle, stomata, vascular tissue, seed, pollen và flower.

Mỗi innovation mở một ecological possibility mới nhưng cũng đi kèm constraint.

## Common misconceptions

### “Plant lấy thức ăn từ đất”

Carbon organic chủ yếu đến từ CO₂. Soil cung cấp water và mineral nutrient.

### “Xylem là pump”

Xylem chủ yếu là conduit; transpiration-driven tension là force lớn trong water transport.

### “Plant không hô hấp vì đã photosynthesize”

Plant cell vẫn cellular respire để tạo ATP usable day and night.

### “Hormone thực vật giống hormone người, mỗi loại một chức năng”

Không. Plant hormone có pleiotropic effect và strong cross-talk.

## Mental Model

> Plant là organism nối hai resource space: root khai thác water/mineral trong soil, leaf khai thác light/CO₂ trong air. Xylem nối water upward, phloem phân phối carbon, stomata điều khiển trade-off carbon–water, hormone điều phối growth theo environment.

File tiếp theo [[01_animal_physiology_and_homeostasis]] chuyển sang animal, nơi mobility và high metabolic demand tạo bài toán transport, gas exchange, digestion, excretion và control khác.