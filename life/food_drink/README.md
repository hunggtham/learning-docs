# Food & Drinks — Đồ ăn, đồ uống và cách hiểu chúng

> **Mạch đọc:** [Life README](../README.md) là owner cấp domain của **Food & Drinks**. Route đi từ nguyên liệu và biến đổi → lên men/chưng cất/lưu trữ → hệ phân loại → hương vị và nhãn → cách so sánh và thưởng thức, kết nối giữa tầng tổng quan liên ngành và các chuỗi bài học chuyên sâu theo từng dòng đồ uống.

Đồ uống là một ví dụ mẫu mực cho phương pháp tiếp cận kiến trúc đời sống theo cơ chế: cùng xuất phát từ những nguyên liệu tự nhiên tương đối đơn giản (ngũ cốc, nước, vi sinh vật), nhưng sự thay đổi về giống nguyên liệu, chủng men, profile nước, kỹ thuật gia nhiệt, kiểm soát thời gian, phương pháp chưng cất, quá trình ủ thùng gỗ (maturation) hoặc quy cách đóng gói có thể tạo ra những sản phẩm hoàn toàn khác biệt.

Nhánh này kiên quyết không học theo danh mục thương hiệu (brand list) hay ghi nhớ máy móc các mẹo thưởng thức. Câu hỏi xuyên suốt là:

```text
ingredient
→ transformation
→ process variables
→ classification axes
→ measurable properties
→ sensory result
→ storage / degradation
→ serving / use
```

Khi cơ chế chạm đến lý thuyết sâu về hóa sinh lên men, hóa học hữu cơ hay tâm lý học nhận thức cảm quan, tài liệu chỉ giải thích đúng mức cần thiết để giải quyết câu hỏi đời sống rồi bàn giao sang các domain khoa học chuẩn gốc (Biology, Chemistry, Psychology) thay vì viết lặp.

---

## Cấu trúc phân cấp lộ trình học

Nhánh Food & Drinks được tổ chức thành hai tầng rõ ràng: **Tầng 1** bao quát các nguyên lý liên ngành và bài tập đối chiếu so sánh; **Tầng 2** đi sâu vào từng chuỗi sản xuất từ nguyên liệu đến cảm quan của hai dòng đồ uống nền tảng là Whisky và Bia.

```text
Food & Drinks
├── Tầng 1: Tổng quan liên ngành & Đối chiếu
│   ├── 01_style_process_and_tasting.md (Đối chiếu phong cách, quy trình và cảm quan)
│   ├── 02_regulation_comparison_and_serving.md (Pháp lý, nhãn mác, phục vụ và chuẩn mực)
│   └── 03_beer_whisky_comparison_lab.md (Case lab thực hành so sánh beer và whisky)
│
└── Tầng 2: Chuyên sâu theo dòng sản phẩm
    ├── Whisky Track (Ngũ cốc → Lên men → Chưng cất → Thùng gỗ → Cảm quan)
    │   ├── whisky/00_whisky_foundations.md
    │   ├── whisky/01_classification_and_legal_definitions.md
    │   ├── whisky/02_distillation_stills_reflux_and_cuts.md
    │   ├── whisky/03_casks_maturation_and_finishing.md
    │   └── whisky/04_tasting_sensory_vocabulary_and_comparison.md
    │
    └── Beer Track (Malt → Hoa bia → Lên men → Phong cách → Độ tươi & Phục vụ)
        ├── beer/00_beer_foundations.md
        ├── beer/01_ingredients_mashing_hops_and_fermentation.md
        └── beer/02_style_map_specs_freshness_and_serving.md
```

### Tầng 1: Tổng quan liên ngành & So sánh đối chiếu

Ba chapter tổng quan cung cấp khung tư duy so sánh và bài tập tình huống liên ngành:

1. [`01_style_process_and_tasting.md`](01_style_process_and_tasting.md) — đối chiếu mối liên hệ giữa phong cách sản phẩm (style), quy trình công nghệ (process) và cách đánh giá cảm quan (tasting) xuyên suốt các loại đồ uống.
2. [`02_regulation_comparison_and_serving.md`](02_regulation_comparison_and_serving.md) — giải mã hệ thống quản lý nhãn mác theo từng khu vực pháp lý (jurisdiction), nhiệt độ và dụng cụ phục vụ, cùng trách nhiệm đối với sức khỏe và an toàn.
3. [`03_beer_whisky_comparison_lab.md`](03_beer_whisky_comparison_lab.md) — phòng thực hành tình huống (case lab) so sánh trực tiếp giữa bia và whisky xuất phát từ cùng một bài toán phục vụ cụ thể.

> **Chuyển mạch:** Sau khi có khung so sánh liên ngành, người học đi vào từng dòng đồ uống chuyên sâu để thấy rõ cơ chế hóa sinh và vật lý biến đổi nguyên liệu ở từng mắt xích.

---

### Tầng 2: Chuyên sâu theo dòng đồ uống

#### 1. Whisky Track

Chuỗi bài học whisky khép kín từ nguyên liệu hạt đến phân tích cảm quan và suy luận quy trình:

1. [`whisky/00_whisky_foundations.md`](whisky/00_whisky_foundations.md) — hạt ngũ cốc → đường hóa → lên men → chưng cất → trưởng thành trong thùng gỗ: chuỗi biến đổi hình thành whisky.
2. [`whisky/01_classification_and_legal_definitions.md`](whisky/01_classification_and_legal_definitions.md) — hệ thống pháp lý theo vùng lãnh thổ (Scotch, Bourbon/American, Irish, Japanese), phân loại ngũ cốc, nhà chưng cất đơn (single) và phối trộn (blended).
3. [`whisky/02_distillation_stills_reflux_and_cuts.md`](whisky/02_distillation_stills_reflux_and_cuts.md) — nguyên lý tách pha lỏng–hơi, nồi chưng cất tĩnh (pot still) và cột liên tục (column still), độ hồi lưu (reflux), vai trò của đồng (copper) và kỹ thuật cắt rượu (cuts).
4. [`whisky/03_casks_maturation_and_finishing.md`](whisky/03_casks_maturation_and_finishing.md) — ba cơ chế tương tác thùng gỗ (chiết xuất, biến đổi, hấp phụ), gỗ sồi trắng Mỹ vs châu Âu, mức nướng/đốt than (toast/char), lịch sử thùng ủ, oxy hóa, bốc hơi hao hụt (angel's share) và hoàn thiện (finishing).
5. [`whisky/04_tasting_sensory_vocabulary_and_comparison.md`](whisky/04_tasting_sensory_vocabulary_and_comparison.md) — giao thức nếm chuẩn mực (nose, palate, mouthfeel, finish), bánh xe hương vị, pha loãng với nước, nếm mù (blind tasting) và cách lập giả thuyết sản xuất từ quan sát cảm quan.

Mạch suy luận của Whisky:

```text
grain / fermentation
→ distillation selection
→ new-make spirit
→ cask maturation
→ blending / bottling
→ sensory observation
→ calibrated production hypothesis
```

#### 2. Beer Track

Chuỗi bài học bia phân tích sâu mối quan hệ giữa công nghệ nấu bia, phong cách và độ tươi:

1. [`beer/00_beer_foundations.md`](beer/00_beer_foundations.md) — bản đồ nhập môn các họ bia lớn (Ale vs Lager), các phong cách tiêu biểu (Pilsner, Pale Ale, IPA, Stout) và ranh giới của các con số ABV/IBU.
2. [`beer/01_ingredients_mashing_hops_and_fermentation.md`](beer/01_ingredients_mashing_hops_and_fermentation.md) — xử lý mầm malt, kiểm soát enzyme đường hóa mashing, vai trò hoa bia đắng và hoa bia thơm (dry hopping), profile khoáng của nước, động thái men bia và các cơ chế gây lỗi vị (diacetyl, DMS, oxy hóa).
3. [`beer/02_style_map_specs_freshness_and_serving.md`](beer/02_style_map_specs_freshness_and_serving.md) — không gian phong cách đa chiều, bộ thông số kỹ thuật (ABV, IBU, OG, FG, SRM), quản lý độ tươi (freshness) và kiểm soát nhiệt độ, ly rót cùng bọt bia khi phục vụ.

---

## Các nguyên lý nền tảng cần ghi nhớ

### 1. Điểm chung và điểm tách giữa Beer và Whisky

Hai dòng đồ uống chia sẻ cùng một nền tảng chuyển hóa ban đầu:

```text
grain (lúa mạch, ngô, lúa mì, lúa mạch đen)
→ starch (tinh bột)
→ fermentable sugar (đường có thể lên men)
→ yeast fermentation (lên men bằng nấm men)
```

Sau đó, hai con đường phân kỳ triệt để:

```text
Beer
→ conditioning & carbonation
→ packaging (lon/chai/keg)
→ sản phẩm nhạy cảm cao với độ tươi (freshness-sensitive)

Whisky
→ distillation (chưng cất chọn lọc bay hơi)
→ new-make spirit (rượu nền nồng độ cao)
→ cask maturation (trưởng thành nhiều năm trong thùng gỗ sồi)
→ blending & bottling
→ sản phẩm ổn định sau đóng chai, trải nghiệm cảm quan phức hợp
```

Bia giữ lại phần lớn ma trận lên men và hương hoa bia nhạy cảm; Whisky dùng chưng cất để tách phân đoạn bay hơi mong muốn rồi để tương tác gỗ sồi và thời gian tạo nên chiều sâu hương vị.

### 2. Tách bạch Legal definition, Process và Sensory style

Lỗi nhận thức phổ biến nhất khi học đồ uống là gộp chung các trục phân loại khác nhau:

- **Scotch, Bourbon:** Hệ quy định pháp lý và nguồn gốc địa lý (origin & legal system), không phải một hương vị duy nhất.
- **Single Malt:** Quy định về nguyên liệu (100% malt lúa mạch) và nơi sản xuất (một nhà chưng cất duy nhất), không phải thang điểm chất lượng.
- **IPA:** Nhóm phong cách và kỳ vọng quy trình (style & hop profile), không phải một công thức đơn lẻ.
- **Vanilla, Khói, Trái cây:** Từ vựng mô tả cảm quan (sensory language), không phải bằng chứng nhà sản xuất đã thả nguyên liệu đó vào nồi nấu.

### 3. Tách biệt thông số kỹ thuật khỏi chất lượng trải nghiệm

Các con số trên nhãn mác đo lường một đại lượng vật lý hoặc hóa học cụ thể:

- `ABV` đo tỷ lệ thể tích ethanol, không đo độ đậm đà hương vị.
- `IBU` đo hàm lượng iso-alpha acid đắng từ hoa bia, nhưng vị đắng cảm nhận thực tế phụ thuộc lượng đường dư (FG) và cấu trúc malt.
- `Age statement` (số năm ủ) đo thời gian rượu nằm trong thùng gỗ của giọt rượu trẻ nhất, không tương đương với độ ngon tuyệt đối.

Các quy tắc đọc thông số này được chuẩn hóa tại [Specs, Labels & Units](../consumer_literacy/00_reading_specs_labels_and_units.md).

### 4. Freshness và Maturation: Hai chiều hướng trái ngược

- **Bia (nhất là dòng nhiều hoa bia như IPA):** Mất độ tươi do oxy hóa và phân hủy hợp chất thơm hop là rủi ro hàng đầu. Bia ngon nhất khi uống sớm.
- **Whisky trong chai đã niêm phong:** Quá trình trưởng thành trong thùng gỗ đã dừng lại hoàn toàn sau khi đóng chai. Rượu không "chín thêm" trong chai thủy tinh, nhưng có độ bền lưu trữ rất cao nếu tránh ánh sáng trực tiếp và nhiệt độ cao.

Do đó, không có quy luật vạn năng "càng để lâu càng ngon" hay "càng mới càng tốt". Người học phải xác định sản phẩm còn đang trong quá trình chuyển hóa nào và cơ chế suy thoái chính là gì.

---

## Kết nối sang Consumer Literacy và các domain khác

Khi bài toán chuyển từ cơ chế đồ uống sang kỹ năng đọc nhãn, đánh giá bằng chứng hoặc ra quyết định mua sắm tiêu dùng:

- Sử dụng [`../consumer_literacy/`](../consumer_literacy/README.md) và [`../consumer_knowledge/`](../consumer_knowledge/README.md) làm lớp nền tảng:
  - [Specs, Labels & Units](../consumer_literacy/00_reading_specs_labels_and_units.md) → đọc hiểu ABV, IBU, proof, age statement, chứng nhận nguồn gốc.
  - [Materials, Quality & Durability](../consumer_literacy/01_materials_quality_and_durability.md) → vật liệu chai thủy tinh, lon nhôm tráng men, gỗ sồi, nắp bần và bảo quản.
- Sử dụng [`../CONCEPTUAL_DEPENDENCIES.md`](../CONCEPTUAL_DEPENDENCIES.md) để tra cứu các khái niệm dùng chung giữa đồ uống và các lĩnh vực đời sống khác.

---

## Hướng dẫn đọc theo mục tiêu học tập

- Muốn có cái nhìn đối chiếu liên ngành giữa bia và whisky → [`01_style_process_and_tasting.md`](01_style_process_and_tasting.md) và [`03_beer_whisky_comparison_lab.md`](03_beer_whisky_comparison_lab.md).
- Muốn hiểu luật dán nhãn quốc tế và chuẩn mực phục vụ → [`02_regulation_comparison_and_serving.md`](02_regulation_comparison_and_serving.md).
- Muốn hiểu vì sao whisky có các dòng Scotch, Bourbon, Single Malt → [`whisky/01_classification_and_legal_definitions.md`](whisky/01_classification_and_legal_definitions.md).
- Muốn hiểu cơ chế chưng cất và nồi đồng → [`whisky/02_distillation_stills_reflux_and_cuts.md`](whisky/02_distillation_stills_reflux_and_cuts.md).
- Muốn hiểu bí mật của các loại thùng gỗ ủ rượu → [`whisky/03_casks_maturation_and_finishing.md`](whisky/03_casks_maturation_and_finishing.md).
- Muốn học cách nếm và sử dụng từ vựng hương vị whisky → [`whisky/04_tasting_sensory_vocabulary_and_comparison.md`](whisky/04_tasting_sensory_vocabulary_and_comparison.md).
- Muốn hiểu các họ bia Ale, Lager, Stout, IPA từ nền tảng → [`beer/00_beer_foundations.md`](beer/00_beer_foundations.md).
- Muốn nắm công nghệ nấu bia, hoa bia và men bia → [`beer/01_ingredients_mashing_hops_and_fermentation.md`](beer/01_ingredients_mashing_hops_and_fermentation.md).
- Muốn đọc thông số bia, giữ bia tươi và chọn ly rót → [`beer/02_style_map_specs_freshness_and_serving.md`](beer/02_style_map_specs_freshness_and_serving.md).

> **Bàn giao:** Đừng đọc đồ uống qua giá tiền hay lời đồn tiếp thị. Hãy tiếp cận từng ly đồ uống như một tác phẩm của nguyên liệu, hóa sinh lên men, vật lý chưng cất và thời gian trưởng thành; khi đó hương vị bạn cảm nhận được sẽ là kết quả tự nhiên của toàn bộ chuỗi cơ chế phía sau.
