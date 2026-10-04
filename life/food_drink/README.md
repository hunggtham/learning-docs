# Food & Drink — Đồ ăn, đồ uống và cách hiểu chúng

Đồ uống là một ví dụ tốt cho cách học đời sống theo cơ chế: cùng bắt đầu từ nguyên liệu tương đối đơn giản nhưng thay đổi nguyên liệu, vi sinh vật, nhiệt độ, thời gian, chưng cất, maturation hoặc packaging có thể tạo ra sản phẩm hoàn toàn khác nhau.

Nhánh này không học theo brand list. Câu hỏi xuyên suốt là:

```text
ingredient
→ transformation
→ process variables
→ classification
→ measurable properties
→ sensory result
→ storage / degradation
→ serving / use
```

Khi mechanism cần theory sâu về fermentation, chemistry hoặc perception, chapter chỉ giải thích mức cần thiết rồi handoff sang canonical science domain thay vì duplicate.

## Lộ trình hiện tại

### Whisky

Whisky hiện đã có một chain từ grain tới sensory/application:

1. [`whisky/00_whisky_foundations.md`](whisky/00_whisky_foundations.md) — grain → sugar → fermentation → distillation → maturation.
2. [`whisky/01_classification_and_legal_definitions.md`](whisky/01_classification_and_legal_definitions.md) — geographic/legal system, grain, distillery source, blending, age, ABV; Scotch, American/Bourbon, Irish và Japanese labeling frameworks.
3. [`whisky/02_distillation_stills_reflux_and_cuts.md`](whisky/02_distillation_stills_reflux_and_cuts.md) — vapour/liquid separation, pot vs column, reflux, copper, condenser, cuts và new-make character.
4. [`whisky/03_casks_maturation_and_finishing.md`](whisky/03_casks_maturation_and_finishing.md) — extraction + transformation + subtraction, oak/char/toast, cask history, oxidation, evaporation, finishing và blending.
5. [`whisky/04_tasting_sensory_vocabulary_and_comparison.md`](whisky/04_tasting_sensory_vocabulary_and_comparison.md) — nose/palate/mouthfeel/finish, sensory families, intensity/balance, dilution, blind comparison, production hypotheses, storage/serving và practice drills.

Whisky route giờ là:

```text
grain / fermentation
→ distillation selection
→ new make
→ cask maturation
→ bottling
→ sensory observation
→ calibrated production hypothesis
```

Điểm quan trọng: sensory descriptor là **observation**, không phải proof của một cask/process cụ thể. `vanilla`, `dried fruit`, `smoke`, `spice` chỉ nên tăng/giảm plausibility của hypotheses rồi được kiểm tra bằng producer data hoặc comparison tốt hơn.

Whisky depth tiếp theo chỉ nên mở khi có use-case gap thật, ví dụ region/tradition comparison hoặc purchase/value casebook. Không cần thêm country taxonomy chỉ để tăng breadth.

### Beer

Beer hiện cũng đã có chain từ ingredient tới consumer state:

1. [`beer/00_beer_foundations.md`](beer/00_beer_foundations.md) — map nhập môn Ale/Lager/IPA/Stout và giới hạn của ABV/IBU.
2. [`beer/01_ingredients_mashing_hops_and_fermentation.md`](beer/01_ingredients_mashing_hops_and_fermentation.md) — malting, mash, gravity, boil, hop timing, water, yeast, attenuation, conditioning, carbonation, packaging và off-flavour mechanism.
3. [`beer/02_style_map_specs_freshness_and_serving.md`](beer/02_style_map_specs_freshness_and_serving.md) — style as process space, ABV/IBU/OG/FG/SRM, freshness, storage, packaging, serving temperature, glass/foam và draft-state effects.

Beer depth tiếp theo chỉ cần mở khi có clear learning gap, ví dụ sensory calibration hoặc detailed style families. Không tạo catalog hàng trăm styles.

## Điểm chung và điểm tách giữa Beer và Whisky

Hai nhánh chia sẻ foundation:

```text
grain
→ starch
→ fermentable sugar
→ yeast fermentation
```

Sau đó tách mạnh:

```text
Beer
→ conditioning
→ carbonation
→ packaging
→ freshness-sensitive product state

Whisky
→ distillation
→ new make
→ cask maturation
→ blending / bottling
→ sensory comparison after maturation has stopped
```

Sự khác biệt này quan trọng hơn brand: Beer giữ phần lớn fermentation matrix; Whisky dùng distillation để select volatile fraction rồi để cask biến đổi spirit qua thời gian.

## Legal definition, process và sensory style phải tách nhau

Recurring failure mode:

```text
Scotch
→ legal/origin system
≠ một flavour duy nhất

Single Malt
→ production/source category
≠ quality score

IPA
→ style/process expectation
≠ một recipe duy nhất

vanilla / citrus / smoke
→ sensory language
≠ proof của ingredient/process duy nhất
```

Mỗi label/descriptor trả lời một câu hỏi khác nhau.

## Measurement cũng phải tách khỏi experience

Food & Drink có nhiều con số dễ bị biến thành quality score:

```text
ABV
IBU
OG / FG
age statement
bottling proof
```

Mỗi metric trả lời một câu hỏi cụ thể. Nó không thay sensory context, process history hoặc use case. Đây là nơi [Specs, Labels & Units](../consumer_literacy/00_reading_specs_labels_and_units.md) cung cấp rule chung cho toàn domain.

## Sensory practice cũng cần protocol

Tasting/review không tự nhiên trở thành evidence chỉ vì người viết dùng nhiều descriptor. Comparison tốt hơn khi kiểm soát:

- glass;
- sample order;
- temperature;
- resting time;
- dilution;
- brand/price knowledge khi cần blind comparison;
- external odors/food.

Whisky sensory chapter sử dụng chính discipline này để nối subjective experience với repeatable observation.

## Freshness và maturation đi theo hai hướng khác nhau

```text
many hop-forward beers
→ freshness loss can be central risk

whisky in sealed bottle after maturation
→ cask maturation has stopped; storage priorities differ
```

Do đó “càng lâu càng tốt” hoặc “càng mới càng tốt” đều không phải rule universal. Phải hỏi product đang còn active transformation nào và degradation mechanism nào material.

## Không mở rộng breadth quá sớm

Wine, coffee, tea và các nhánh khác đều có giá trị, nhưng vertical mới chỉ nên mở khi nó tận dụng được structure đã chứng minh:

- nguyên liệu;
- transformation/process;
- classification axes;
- label/spec;
- sensory vocabulary;
- freshness/storage;
- defect/failure mode;
- comparison/application.

Whisky và Beer hiện đã đủ depth để chứng minh framework hoạt động. Pass tiếp theo nên dựa coverage gap thật, không thêm beverage category chỉ để library trông rộng hơn.

## Consumer Literacy handoff

Khi câu hỏi chuyển từ “đồ uống này được tạo ra thế nào?” sang “nhãn này đo gì, marketing claim này đáng tin không, hay hai sản phẩm nên so theo tiêu chí nào?”, dùng [`../consumer_literacy/`](../consumer_literacy/README.md) và [`../CONCEPTUAL_DEPENDENCIES.md`](../CONCEPTUAL_DEPENDENCIES.md) làm layer chung.

Đặc biệt:

- [Specs, Labels & Units](../consumer_literacy/00_reading_specs_labels_and_units.md) → ABV, IBU, age, proof, legal category.
- [Materials, Quality & Durability](../consumer_literacy/01_materials_quality_and_durability.md) → glass/can/cask material, oxygen/light exposure, aging/degradation.
- [Reliability, Repairability & Maintenance](../consumer_literacy/02_reliability_repairability_and_maintenance.md) → process/QC/failure reasoning ở mức generic.

Food & Drink giữ product/process/sensory mechanism; Consumer Literacy giữ cách đọc measurement, evidence và trade-off dùng xuyên nhiều product domains.
