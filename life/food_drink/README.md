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

Whisky hiện đã có một chain từ nguyên liệu đến cask:

1. [`whisky/00_whisky_foundations.md`](whisky/00_whisky_foundations.md) — grain → sugar → fermentation → distillation → maturation.
2. [`whisky/01_classification_and_legal_definitions.md`](whisky/01_classification_and_legal_definitions.md) — geographic/legal system, grain, distillery source, blending, age, ABV; Scotch, American/Bourbon, Irish và Japanese labeling frameworks.
3. [`whisky/02_distillation_stills_reflux_and_cuts.md`](whisky/02_distillation_stills_reflux_and_cuts.md) — vapour/liquid separation, pot vs column, reflux, copper, condenser, cuts và new-make character.
4. [`whisky/03_casks_maturation_and_finishing.md`](whisky/03_casks_maturation_and_finishing.md) — extraction + transformation + subtraction, oak/char/toast, cask history, oxidation, evaporation, finishing và blending.

Nhờ route này, label như `Single Malt`, `12 Years`, `Sherry Cask` và `46% ABV` được tách khỏi mechanism: label cho biết một dimension; process giải thích vì sao liquid có character cụ thể.

Whisky depth tiếp theo nên là:

```text
tasting / sensory vocabulary
→ production traditions as applied comparisons
→ storage / serving
```

Không cần mở thêm country taxonomy trước khi sensory layer đủ sâu.

### Beer

Beer hiện cũng đã có chain từ ingredient tới consumer state:

1. [`beer/00_beer_foundations.md`](beer/00_beer_foundations.md) — map nhập môn Ale/Lager/IPA/Stout và giới hạn của ABV/IBU.
2. [`beer/01_ingredients_mashing_hops_and_fermentation.md`](beer/01_ingredients_mashing_hops_and_fermentation.md) — malting, mash, gravity, boil, hop timing, water, yeast, attenuation, conditioning, carbonation, packaging và off-flavour mechanism.
3. [`beer/02_style_map_specs_freshness_and_serving.md`](beer/02_style_map_specs_freshness_and_serving.md) — style as process space, ABV/IBU/OG/FG/SRM, freshness, storage, packaging, serving temperature, glass/foam và draft-state effects.

Beer depth tiếp theo chỉ cần mở khi có clear learning gap, ví dụ sensory calibration hoặc detailed style families. Không tạo catalog hàng trăm styles.

## Điểm chung và điểm tách giữa Beer và Whisky

Hai nhánh chia sẻ một chemical/biological foundation:

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
```

Sự khác biệt này quan trọng hơn brand: Beer giữ phần lớn fermentation matrix; Whisky dùng distillation để select volatile fraction rồi để cask biến đổi spirit qua thời gian.

## Legal definition và sensory style phải tách nhau

Một recurring failure mode là dùng legal/geographic label như flavour guarantee.

```text
Scotch
→ legal/origin system
≠ một flavour duy nhất

IPA
→ style/process expectation
≠ một recipe duy nhất
```

Ngược lại tasting descriptor như `vanilla`, `citrus`, `coffee`, `pine` là sensory language. Chúng không nhất thiết nghĩa ingredient tương ứng đã được thêm trực tiếp và cũng không tự chứng minh một process cause duy nhất.

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

## Freshness và maturation đi theo hai hướng khác nhau

Beer và Whisky còn cho một contrast hữu ích:

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
- defect/failure mode.

Whisky và Beer hiện đã có đủ depth để chứng minh framework hoạt động, nhưng Cars vẫn đang là vertical mẫu mạnh nhất của `life/`. Vì vậy pass hiện tại vẫn ưu tiên depth/consistency thay vì mở nhiều beverage category cùng lúc.

## Consumer Literacy handoff

Khi câu hỏi chuyển từ “đồ uống này được tạo ra thế nào?” sang “nhãn này đo gì, marketing claim này đáng tin không, hay hai sản phẩm nên so theo tiêu chí nào?”, dùng [`../consumer_literacy/`](../consumer_literacy/README.md) và [`../CONCEPTUAL_DEPENDENCIES.md`](../CONCEPTUAL_DEPENDENCIES.md) làm layer chung.

Đặc biệt:

- [Specs, Labels & Units](../consumer_literacy/00_reading_specs_labels_and_units.md) → ABV, IBU, age, proof, legal category.
- [Materials, Quality & Durability](../consumer_literacy/01_materials_quality_and_durability.md) → glass/can/cask material, oxygen/light exposure, aging/degradation.
- [Reliability, Repairability & Maintenance](../consumer_literacy/02_reliability_repairability_and_maintenance.md) → process/QC/failure reasoning ở mức generic.

Food & Drink giữ product/process mechanism; Consumer Literacy giữ cách đọc measurement, evidence và trade-off dùng xuyên nhiều product domains.
