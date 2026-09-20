# Hệ sinh thái, chu trình vật chất và bảo tồn — Ecosystems, Biogeochemical Cycles and Conservation (생태계, 생지화학적 순환과 보전)

Community ecology cho ta biết species tương tác với nhau. Nhưng organism không chỉ tương tác với organism; chúng còn trao đổi vật chất và năng lượng với không khí, nước, đất và ánh sáng. Khi đưa cả yếu tố sinh học lẫn phi sinh học vào cùng một system, ta có **ecosystem (hệ sinh thái / 생태계)**.

Chương này nối metabolism ở cell với carbon cycle ở planet scale. Một electron đi qua photosystem trong chloroplast cuối cùng có thể ảnh hưởng productivity của ecosystem; respiration của hàng tỷ organism trở thành flux CO₂ toàn cầu. Đây là nơi scale nhỏ và scale lớn thực sự nối lại.

## 1. Energy flow và matter cycle không giống nhau

Một distinction nền tảng:

**Matter cycles. Energy flows.**

Carbon atom có thể đi từ atmosphere → plant → animal → decomposer → atmosphere rồi tiếp tục cycle.

Energy từ sunlight được producer capture, truyền qua food web, nhưng ở mỗi conversion một phần lớn phân tán dưới dạng heat. Heat không được ecosystem recycle trở lại thành chemical energy hữu dụng theo cùng cách.

```text
Sunlight
   ↓
Producers
   ↓
Consumers
   ↓
Decomposers
   ↓
Heat dissipated
```

Trong khi carbon có vòng:

```text
CO2 ↔ organic carbon ↔ decomposed carbon ↔ CO2
```

Nếu trộn hai concept này, ecology rất dễ rối.

## 2. Primary production: photosynthesis trở thành quantity ở ecosystem scale

Plant, algae và cyanobacteria biến light + CO₂ thành organic carbon.

**Gross primary productivity (GPP)** là tổng carbon fixation.

Producer cũng respiration, nên một phần carbon được dùng lại để tạo ATP.

**Net primary productivity (NPP)** gần bằng:

\[
NPP = GPP - R_{producer}
\]

NPP là phần organic matter còn lại để growth/reproduction và làm resource cho consumer.

Một process chloroplast-level giờ trở thành nền của food web.

## 3. Trophic transfer và ecological efficiency

Khi herbivore ăn plant, không phải toàn bộ plant biomass trở thành herbivore biomass. Một phần không được ăn, không tiêu hóa, dùng cho respiration hoặc mất dưới dạng waste.

Vì vậy energy/biomass thường giảm qua trophic level.

“10% rule” đôi khi được dùng như approximation giáo khoa, nhưng efficiency thật thay đổi mạnh theo ecosystem và organism.

Mental model đúng là: **mỗi trophic transfer có loss lớn**, không phải chính xác 10% mọi nơi.

## 4. Decomposer hoàn tất vòng vật chất

Nếu dead organic matter không được phân giải, nutrient sẽ bị khóa lại.

Fungi và bacteria phân giải polymer, sử dụng carbon cho metabolism và trả mineral nutrient về soil/water.

Decomposer vì thế không phải “phần cuối ít quan trọng” của food chain. Chúng là module giúp material trở lại vòng tuần hoàn.

## 5. Carbon cycle: nối photosynthesis, respiration, ocean và geology

Atmospheric CO₂ được photosynthesis fixation. Respiration và decomposition trả CO₂ lại.

Ocean dissolve CO₂ và trao đổi với atmosphere. Một phần carbon bị chôn vùi trong sediment hoặc lưu lâu trong biomass/soil.

Human combustion fossil carbon chuyển carbon geological reservoir sang atmosphere rất nhanh so với nhiều natural geological process.

Carbon cycle vì thế có reservoir với residence time rất khác nhau.

## 6. Nitrogen cycle: có N₂ không có nghĩa organism dùng trực tiếp được

Atmosphere chứa rất nhiều N₂ nhưng triple bond rất bền. Hầu hết organism không tự convert N₂ thành usable nitrogen.

**Nitrogen fixation** do một số bacteria/archaea chuyển N₂ thành ammonia-related form.

Nitrification chuyển reduced nitrogen sang nitrite/nitrate. Denitrification có thể trả nitrogen về N₂.

Plant hấp thu inorganic nitrogen để tổng hợp amino acid/nucleotide; consumer nhận nitrogen qua food.

Một lần nữa microbial metabolism ở chapter trước trở thành global cycle.

## 7. Phosphorus cycle khác nitrogen ở điểm nào?

Phosphorus cần cho ATP, DNA, RNA và phospholipid.

Khác nitrogen, phosphorus cycle không có atmospheric gas phase lớn tương đương. Weathering rock, soil, water và sediment đóng role quan trọng.

Vì phosphorus có thể limiting, fertilizer addition có thể đổi productivity mạnh.

## 8. Limiting nutrient và Liebig-style reasoning

Growth không chỉ phụ thuộc tổng resource; nó có thể bị giới hạn bởi resource thiếu nhất relative to demand.

Nếu nitrogen đã rất dư nhưng phosphorus thiếu, thêm nitrogen không tăng production nhiều.

Điều này giống bottleneck trong engineering system: throughput bị giới hạn bởi constraint chính, không phải tổng capacity của mọi component.

## 9. Eutrophication: nutrient nhiều không phải lúc nào cũng tốt

Khi nitrogen/phosphorus quá nhiều vào lake/coastal water, algae bloom có thể tăng mạnh.

Sau đó biomass chết và bị decomposer phân giải, respiration tiêu thụ dissolved oxygen. Hypoxia có thể làm fish/invertebrate chết.

Causal chain:

```text
nutrient input ↑
   ↓
primary production ↑
   ↓
organic matter decomposition ↑
   ↓
oxygen consumption ↑
   ↓
hypoxia risk ↑
```

Một intervention tưởng như “thêm nutrient giúp growth” có indirect effect qua food web và decomposition.

## 10. Ecosystem disturbance và resilience

Fire, storm, flood, drought hoặc human activity có thể thay system.

**Resistance** mô tả mức system ít đổi trước disturbance.

**Resilience** mô tả khả năng phục hồi function/state sau disturbance.

Hai concept khác nhau. Grassland có thể thay composition sau fire nhưng productivity hồi nhanh — resilience cao dù resistance không nhất thiết cao.

## 11. Alternative stable states và threshold

Một số ecosystem có feedback làm system ổn định quanh nhiều state khác nhau.

Ví dụ clear-water lake và turbid lake có thể được duy trì bởi feedback khác nhau. Khi crossing threshold, system có thể shift nhanh và khó quay lại ngay khi pressure giảm.

Đây là nonlinear dynamics ở ecology, tương tự switch/positive feedback trong cell signaling nhưng ở scale lớn hơn.

## 12. Biodiversity và ecosystem function

Species diversity có thể tăng functional redundancy và resource complementarity trong một số system, nhưng relationship không universal đơn giản.

Quan trọng hơn, mất species có effect phụ thuộc role trong network. Mất keystone species có thể mạnh hơn mất một species redundant về function.

Vì vậy conservation không thể chỉ đếm số species; cần hiểu interaction network và genetic diversity.

## 13. Island biogeography: area và isolation ảnh hưởng species richness

Theory of island biogeography mô hình hóa balance giữa colonization và extinction.

Island lớn thường có extinction rate thấp hơn vì population lớn/habitat đa dạng. Island gần source có colonization rate cao hơn.

Concept này được áp dụng cẩn thận cho habitat fragment: forest patch cô lập có thể giống “island” trong matrix khác habitat.

## 14. Habitat fragmentation nối ecology với population genetics

Khi habitat bị chia nhỏ, population bị tách.

Gene flow giảm, effective population size có thể giảm, drift/inbreeding tăng.

Do đó landscape change không chỉ giảm area sống; nó còn đổi evolutionary dynamics.

Ecology và population genetics nối trực tiếp.

## 15. Climate change và range shift

Species có physiological tolerance. Khi temperature/precipitation pattern đổi, suitable climate zone có thể dịch chuyển.

Species có thể migrate, adapt hoặc decline tùy dispersal ability, generation time, genetic variation và habitat connectivity.

Không phải species nào cũng phản ứng giống nhau, nên community interaction cũng có thể bị reshuffle.

## 16. Phenology mismatch

Nếu flowering time, insect emergence và bird migration respond khác nhau với warming, timing interaction có thể lệch.

Đây là ví dụ climate effect không cần trực tiếp “giết” organism; nó có thể phá temporal synchronization giữa species.

## 17. Conservation biology là applied systems biology ở scale lớn

Conservation cần kết hợp:

- population size và demography;
- genetic diversity;
- habitat quality/connectivity;
- species interaction;
- disturbance regime;
- socioeconomic constraint.

Chỉ bảo vệ một species mà bỏ habitat/network có thể không đủ.

## 18. Ecosystem service và human system

Ecosystem cung cấp pollination, water purification, soil formation, carbon storage và nhiều function khác.

Nhưng framing “service” là một cách nhìn human-centered. Conservation còn có giá trị vì biodiversity và evolutionary history tự thân, tùy ethical framework.

Điều quan trọng khoa học là hiểu mechanism, trade-off và uncertainty trước khi ra quyết định.

## 19. Từ ecology sang biotechnology: con người bắt đầu can thiệp có chủ đích

Đến đây library đã đi từ molecule tới biosphere. Bước còn lại là nhìn cách con người **đo, chỉnh sửa và mô hình hóa** những system này.

PCR khai thác DNA replication chemistry. CRISPR khai thác bacterial defense. Sequencing chuyển genome thành data. Bioinformatics dùng algorithm để reconstruct information. Systems biology dùng network model để hiểu interaction nhiều tầng.

Biotechnology vì thế không phải “ứng dụng thêm” ở cuối sách. Nó là việc tái sử dụng các mechanism đã học.

Tiếp tục với [[../06_biotechnology_computation/00_biotechnology_bioinformatics_and_systems_biology]].