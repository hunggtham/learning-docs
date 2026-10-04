# Life Knowledge — Conceptual Dependencies

File này mô tả các concept dùng lại giữa nhiều nhánh trong `life/`. Mục tiêu là tránh mỗi product domain tự phát minh lại cách nói về vật liệu, thông số, độ bền, bảo dưỡng, repairability và total cost.

## Core graph

```text
Use case / problem
        ↓
Material / ingredient
        ↓
Construction / production
        ↓
Mechanism
        ↓
Classification axes
        ↓
Specs / labels / measurements
        ↓
Trade-offs
        ↓
Degradation / failure
        ↓
Reliability / maintenance
        ↓
Repairability / support
        ↓
Warranty / lifecycle
        ↓
Total ownership / comparison
```

Đây không phải thứ tự tuyệt đối cho mọi chapter. Whisky bắt đầu mạnh ở ingredient/process; Cars bắt đầu tốt ở energy/mechanism; Consumer Literacy thường bắt đầu từ specs/claims. Nhưng khi một topic bỏ hẳn một layer ở trên, cần biết lý do.

## Shared concepts

### Material / ingredient

Câu hỏi:

- vật liệu/nguyên liệu nào tạo thuộc tính chính?
- property nào đến từ material, property nào đến từ construction/process?
- cùng tên material nhưng grade/process khác có tạo kết quả khác không?

Canonical science sâu vẫn thuộc Chemistry, Physics, Biology hoặc Electrical Engineering.

Handoff generic: [`consumer_literacy/01_materials_quality_and_durability.md`](consumer_literacy/01_materials_quality_and_durability.md).

### Construction / production

Cùng nguyên liệu có thể cho sản phẩm khác vì:

```text
geometry
processing
heat / pressure
fermentation
machining
assembly
surface treatment
quality control
```

Life chỉ giữ phần process cần để hiểu object; manufacturing science chuyên sâu thuộc owner phù hợp.

### Mechanism

Mechanism trả lời “vì sao object tạo được chức năng này?”. Không thay mechanism bằng feature list.

Ví dụ:

```text
Turbocharger
≠ “tăng công suất” như magic feature

Hops
≠ “làm bia đắng” như thuộc tính duy nhất
```

Cần giải thích đường từ structure/process tới observable consequence.

### Classification axes

Một recurring failure mode là đặt các label thuộc trục khác nhau thành một danh sách ngang hàng.

Ví dụ:

```text
SUV        = body/vehicle architecture
AWD        = drivetrain
Hybrid     = powertrain/energy architecture
Luxury     = market positioning, không phải mechanical category
```

Tương tự:

```text
Scotch      = geographic/legal system
Single Malt = production/source category
12 years    = age statement
46% ABV     = alcohol concentration
```

Mỗi chapter cần nói rõ “label này trả lời câu hỏi nào?”.

### Specs / labels / measurements

Một spec chỉ có nghĩa khi biết:

```text
what is measured
how it is measured
unit
conditions
what it predicts well
what it does not predict
```

Rule nền:

> specification ≠ total quality

Handoff: [`consumer_literacy/00_reading_specs_labels_and_units.md`](consumer_literacy/00_reading_specs_labels_and_units.md).

### Trade-offs

Không có “best” ngoài objective. Một design choice thường đổi:

```text
performance
vs
cost
vs
weight
vs
durability
vs
complexity
vs
repairability
vs
energy use
```

Trade-off cụ thể thuộc từng object domain; reasoning framework chung có thể handoff sang [`../thinking/decision-making/`](../thinking/decision-making/README.md).

### Degradation / failure

Object thật thay đổi theo thời gian. Một chapter chỉ mô tả trạng thái “mới xuất xưởng” thường chưa đủ practical.

Cần phân biệt:

```text
wear
aging
corrosion / oxidation
fatigue
thermal cycling
consumables
misuse
random defect
```

Không phải mọi failure đều phòng được bằng maintenance.

Handoff generic: [`consumer_literacy/01_materials_quality_and_durability.md`](consumer_literacy/01_materials_quality_and_durability.md).

### Reliability / maintenance

Reliability cần được hiểu như:

```text
required function
+ operating condition
+ time horizon
+ failure definition
```

Không được suy từ material name alone.

Maintenance cần có causal link với failure mode:

```text
failure mechanism
→ observable signal
→ preventive / condition-based action
→ reduced probability or consequence
```

Nếu không biết maintenance ngăn failure nào, ritual đó chưa có justification rõ.

Handoff generic: [`consumer_literacy/02_reliability_repairability_and_maintenance.md`](consumer_literacy/02_reliability_repairability_and_maintenance.md).

### Repairability / support

Repairability không chỉ là “tháo ra được”. Nó phụ thuộc:

```text
diagnostics
accessibility
modularity
fasteners / joining
spare parts
documentation
tools / calibration
software/vendor support
labor skill
```

Một theoretically repairable product nhưng không còn parts/support có practical repairability thấp.

### Warranty / lifecycle / ownership

Warranty là risk allocation, không phải direct reliability score.

Lifecycle nhìn toàn path:

```text
acquisition
→ operation
→ maintenance
→ degradation
→ repair / downtime
→ replacement / resale / disposal
```

Purchase price chỉ là một phần:

```text
acquisition
+ consumables
+ energy/fuel
+ maintenance
+ repair
+ downtime
+ replacement/switching
- residual value
```

Financial affordability/debt handoff sang [`../personal-finance/`](../personal-finance/README.md); `life/` chỉ giải thích object-side drivers tạo ra các cost đó.

Handoff generic: [`consumer_literacy/03_warranty_lifecycle_and_total_cost.md`](consumer_literacy/03_warranty_lifecycle_and_total_cost.md).

## Cross-domain routes

### Product claim

```text
claim
→ what property is claimed?
→ measurement/spec?
→ mechanism plausible?
→ evidence?
→ boundary?
```

Handoff: [`../thinking/critical-thinking/`](../thinking/critical-thinking/README.md) và [`../thinking/causal-reasoning/`](../thinking/causal-reasoning/README.md).

### Purchase comparison

```text
use case
→ must-have constraints
→ relevant specs
→ mechanism/material
→ dominant failure modes
→ maintenance/repairability
→ lifecycle/TCO
→ reversibility
→ decision
```

Handoff: [`../thinking/decision-making/`](../thinking/decision-making/README.md) và [`../personal-finance/`](../personal-finance/README.md).

### “Thông số này có đáng tin không?”

```text
unit
→ test condition
→ denominator
→ capacity/physical limit
→ real-world relevance
```

Handoff hiện tại: [`../thinking/statistics-for-life/`](../thinking/statistics-for-life/README.md). Estimation practice mới chỉ nên được link trực tiếp khi đã tồn tại trên canonical `main`.

### “Sản phẩm này có đáng tin/bền không?”

```text
required function
→ material/construction
→ failure modes
→ operating environment
→ maintenance
→ repairability
→ evidence quality
```

Không dùng một warranty badge, material name hoặc owner anecdote làm answer duy nhất.

### “Giá cao hơn có đáng không?”

```text
use horizon
→ acquisition premium
→ operating difference
→ failure/service difference
→ downtime
→ useful life
→ residual value
→ uncertainty
```

Life cung cấp lifecycle variables; actual financial decision handoff sang Personal Finance + Thinking.

## Vertical example: Cars

Cars dùng graph chung như sau:

```text
energy storage
→ engine/motor/inverter
→ transmission/reduction
→ drivetrain
→ tires/road
→ degradation/failure
→ maintenance/repair
→ lifecycle/TCO
```

Current chapters:

- [`vehicles/cars/01_ice_engine_fundamentals.md`](vehicles/cars/01_ice_engine_fundamentals.md)
- [`vehicles/cars/02_hybrid_phev_bev_architecture.md`](vehicles/cars/02_hybrid_phev_bev_architecture.md)

Cars không tự viết lại generic reliability/TCO theory; nó chỉ map vehicle-specific subsystems vào backbone Consumer Literacy.

## Editorial rule

Khi thêm một Life chapter, phải trả lời được:

1. object/product problem là gì;
2. mechanism nào bắt buộc để hiểu;
3. classification axes nào dễ bị trộn;
4. specs/labels nào cần giải thích;
5. degradation/failure nào materially ảnh hưởng use;
6. maintenance/repairability nào relevant;
7. lifecycle/TCO driver nào đáng nhắc;
8. phần nào thuộc canonical science/domain khác;
9. reader sau chapter có thể đánh giá một example mới bằng criteria nào.

Nếu chapter chỉ là `definition + types + brands + tips`, chưa đạt scope của Life Knowledge.