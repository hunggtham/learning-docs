# Reliability, Repairability & Maintenance — Một sản phẩm “bền” chưa chắc là một hệ thống đáng tin

Sau khi biết cách đọc material và durability, câu hỏi tiếp theo là: **sản phẩm có tiếp tục thực hiện đúng chức năng khi dùng thật không, và khi có vấn đề ta có phát hiện/sửa/phục hồi được không?**

Durability chỉ là một phần. Một khung xe có thể rất bền nhưng hệ thống vẫn không reliable nếu seal, bearing, electronics hoặc connector thường xuyên fail. Ngược lại một component có designed life ngắn nhưng rất reliable trong đúng khoảng thời gian nó được thiết kế phục vụ.

Mental model của chapter này:

```text
reliability
= probability/system tendency to perform required function
under stated conditions
for a stated period

repairability
= how feasibly failed function can be restored

maintenance
= actions that preserve, inspect or restore performance
before/after degradation
```

Formal reliability engineering thuộc engineering/statistics domains. `life/` chỉ giữ phần đủ để consumer hiểu failure, maintenance và lifecycle.

## 1. Reliability luôn cần function + condition + time

Nói “sản phẩm này reliable” mà không có context là incomplete.

Cần hỏi:

```text
Required function là gì?
Trong environment nào?
Load/use pattern nào?
Trong bao lâu?
Failure được định nghĩa thế nào?
```

Ví dụ một laptop có thể reliable cho office work nhưng thermal-throttle hoặc battery-degrade nhanh dưới workload nặng. Một outdoor jacket reliable trong mưa nhẹ chưa chắc đạt mục tiêu trong exposure kéo dài.

Vì vậy reliability không phải nhãn tuyệt đối; nó là relationship giữa **function, environment và time**.

## 2. Durability và reliability liên quan nhưng không giống nhau

Durability tập trung vào khả năng chịu wear/degradation. Reliability tập trung vào việc system có thực hiện function khi cần không.

```text
Durable material
≠ reliable system
```

Ví dụ:

- metal chassis bền nhưng charging port fail;
- engine block bền nhưng sensor/wiring gây no-start;
- fabric bền nhưng zipper/seam fail;
- housing bền nhưng seal mất chức năng.

Điều này dẫn tới một rule quan trọng: khi đánh giá reliability, phải tìm **weakest function-critical subsystem**, không chỉ material headline.

## 3. Failure mode phải cụ thể hơn “hỏng”

“Hỏng” có thể là nhiều dạng:

```text
complete loss of function
intermittent failure
performance degradation
out-of-spec behavior
safety failure
cosmetic damage
user-interface failure
```

Một sản phẩm có thể vẫn bật nhưng không còn đạt performance cần thiết. Ví dụ battery vẫn hoạt động nhưng capacity giảm tới mức không còn đáp ứng use case; brake pad chưa “vỡ” nhưng wear vượt mức an toàn.

Vì vậy maintenance và replacement threshold phải dựa trên failure mode, không chỉ binary works/doesn't work.

## 4. Series dependency tạo single-point failure

Trong nhiều system, nhiều subsystem phải cùng hoạt động:

```text
power source
→ controller
→ actuator
→ interface
→ output
```

Nếu một link critical fail, toàn system mất function dù các phần khác còn tốt.

Ví dụ:

```text
battery tốt
+ motor tốt
+ broken connector
→ device không hoạt động
```

Consumer không cần tính reliability equation formal để giữ intuition:

> Hệ thống càng nhiều dependency bắt buộc, càng phải chú ý component yếu và interface giữa chúng.

Đây là lý do complexity/feature count có thể tăng failure surface.

## 5. Redundancy có thể tăng reliability nhưng cũng tăng complexity

Redundancy nghĩa có path/component thay thế khi một phần fail.

Ví dụ:

- dual storage copy;
- spare tire;
- backup power;
- duplicated sensor trong safety-critical system.

Nhưng redundancy không tự động tốt hơn. Nó thêm:

```text
cost
weight
maintenance
coordination logic
new failure modes
```

Câu hỏi đúng là:

> Failure nào cần survive, và redundancy này có độc lập đủ không?

Hai backup dùng cùng nguồn điện hoặc cùng defect có thể fail cùng lúc.

## 6. Early-life, random và wear-out failure cho maintenance insight khác nhau

Consumer thường gặp ba pattern trực giác:

### Early-life defect

Manufacturing/assembly defect xuất hiện sớm.

### Random/intermittent failure

Có thể đến từ electronics, environment, connector, shock hoặc lỗi khó dự đoán.

### Wear-out / aging

Probability failure tăng khi wear, fatigue, seal, battery, lubricant hoặc consumable đi gần end-of-life.

Không cần biến thành formal bathtub curve để hiểu consequence:

```text
early defect → warranty/QC matters
random failure → diagnostics/redundancy matters
wear-out → inspection/maintenance/replacement cycle matters
```

## 7. Maintenance có ba mục tiêu khác nhau

### Preventive maintenance

Thực hiện theo interval hoặc usage để giảm probability failure.

Ví dụ:

- thay dầu/lubricant;
- filter;
- cleaning;
- inspection;
- tightening;
- replacing wear item.

### Condition-based maintenance

Thực hiện khi signal cho thấy degradation:

```text
wear indicator
noise/vibration
battery health
pressure
error log
leak
```

### Corrective maintenance

Sửa sau khi failure đã xuất hiện.

Không phải subsystem nào cũng cần preventive maintenance. Thay item quá sớm cũng tạo waste/cost. Vì vậy interval tốt phải liên quan failure mechanism và risk.

## 8. Maintenance không chữa được mọi aging

Maintenance có thể slow degradation nhưng không reset toàn bộ material history.

Ví dụ:

```text
cleaning
lubrication
filter replacement
inspection
```

không đảo ngược hoàn toàn:

```text
fatigue accumulation
polymer aging
battery cycle aging
UV damage
corrosion đã mất material
```

Rule:

> Maintainable ≠ immortal.

Lifecycle planning cần phân biệt item có thể service và item có finite consumption/life.

## 9. Consumable khác component failure

Consumable được thiết kế để bị tiêu hao hoặc thay theo use:

```text
brake pad
filter
ink/toner
blade
battery in some products
seal/lubricant
```

Việc consumable cần thay không tự động nghĩa product unreliable. Reliability question là:

```text
Consumable life predictable không?
Replacement easy không?
Cost reasonable không?
Failure có warning không?
Ignoring replacement gây secondary damage không?
```

Một thiết kế tốt thường làm wear item dễ inspect/replace hơn component core.

## 10. Repairability bắt đầu từ diagnosis

Không thể sửa hiệu quả nếu không biết failure nằm đâu.

Repairability phụ thuộc:

```text
observability / diagnostics
accessibility
fastener / joining method
modularity
spare parts
service documentation
tooling
software pairing / calibration
labor skill
```

Một sản phẩm dùng material tốt nhưng sealed/glued hoàn toàn có thể có lifecycle ngắn nếu một component nhỏ fail mà không thể thay.

## 11. Modular design tạo trade-off chứ không phải free win

Modularity có thể giúp:

- replace component;
- upgrade subsystem;
- isolate failure;
- reduce repair cost.

Nhưng modular connector, housing và interfaces có thể tăng:

- size;
- cost;
- contact failure;
- ingress risk;
- design complexity.

Do đó repairability phải được đánh giá trong context, không biến “modular” thành quality badge tuyệt đối.

## 12. Spare parts và support horizon là một phần của real repairability

Một product theoretically repairable nhưng không có parts sau vài năm thì practical repairability thấp.

Cần hỏi:

```text
Parts có bán riêng không?
Có standard/generic replacement không?
Service documentation tồn tại không?
Software support/calibration có cần vendor không?
Support horizon dự kiến bao lâu?
```

Điều này đặc biệt quan trọng với products kết hợp hardware + software.

## 13. Downtime là một cost riêng

Repair cost không chỉ là giá part + labor.

Nếu object critical cho work/life, failure còn tạo:

```text
lost time
rental/replacement temporary cost
missed work
inconvenience
risk exposure
```

Vì vậy một product rẻ để sửa nhưng thường xuyên downtime có thể có lifecycle value kém hơn product repair cost cao nhưng failure hiếm.

TCO chapter tiếp theo sẽ đưa downtime vào total cost framework.

## 14. Maintenance schedule phải theo mechanism, không chỉ calendar

Một interval cố định dễ nhớ nhưng use intensity khác nhau.

Có ba clock phổ biến:

```text
calendar time
usage amount
condition signal
```

Ví dụ:

```text
12 months
10,000 km
battery cycle count
filter pressure drop
wear indicator
```

Schedule tốt dùng clock gần failure mechanism nhất nếu measurement practical.

## 15. User behavior là một phần của operating condition

Reliability data từ một context không chuyển trực tiếp sang context khác nếu:

- load khác;
- environment khác;
- maintenance khác;
- use frequency khác;
- storage khác.

Một review “dùng 5 năm không hỏng” là anecdote hữu ích nhưng không đủ để infer defect rate population. Nó cung cấp một case dưới một use profile.

Khi đọc claim/review, handoff sang [`../../thinking/critical-thinking/`](../../thinking/critical-thinking/README.md).

## 16. Repair vs replace là một lifecycle decision

Khi failure xảy ra, không chỉ hỏi “sửa được không?”. Hỏi:

```text
repair cost
remaining life after repair
probability of adjacent failures
replacement cost
replacement performance/efficiency
parts availability
downtime
safety
```

Nếu repair chỉ phục hồi một component trong system đã gần end-of-life, cheap repair có thể không phải cheapest lifecycle option. Ngược lại replacing cả product vì một wear item nhỏ thường tạo waste và cost không cần thiết.

Financial affordability vẫn thuộc Personal Finance; Life chỉ cung cấp object-side variables.

## 17. Reliability evidence nên đọc theo hierarchy

Các nguồn có thể nói những thứ khác nhau:

```text
spec sheet
→ design intent / ratings

warranty policy
→ risk allocation, not direct proof of reliability

teardown
→ architecture / repairability

long-term test
→ behavior under specified protocol

repair data / recall / failure statistics
→ population pattern if denominator/method valid

owner review
→ failure discovery + usability anecdotes
```

Không source nào tự động đủ. Đặc biệt review volume không có denominator đúng có thể làm rare failure trông phổ biến.

## 18. Drill — Failure & maintenance map

Chọn một object bạn dùng thường xuyên.

```text
Object:
Required function:
Operating conditions:
Critical subsystems:
Single-point failures:
Wear items / consumables:
Likely aging mechanisms:
Early warning signals:
Preventive maintenance:
Condition-based checks:
Failure detection:
Repairable modules:
Parts/support constraints:
Expected downtime if failed:
Most likely end-of-life reason:
```

Sau đó chọn **top 3 maintenance actions có causal link rõ nhất** với failure mode. Không thêm maintenance ritual nếu không biết nó ngăn failure nào.

## 19. Comparison framework

Khi so hai sản phẩm, thêm các câu sau vào spec comparison:

```text
What fails first?
Can failure be detected early?
Does failure disable whole system?
What is consumable vs defect?
Can the failed module be replaced?
Are parts/tools available?
How much downtime?
What maintenance prevents the dominant failure?
```

Những câu này thường có value lớn hơn việc so thêm một feature ít dùng.

## Common failure modes khi đánh giá reliability

### “Nặng = bền = reliable”

Weight/material không nói toàn system reliability.

### Warranty dài = chắc chắn reliable

Warranty là contract/risk allocation, không phải direct failure-rate measurement.

### Maintenance càng nhiều càng tốt

Over-maintenance cũng có cost và có thể gây lỗi do intervention.

### Một anecdote = population reliability

Single case thiếu denominator và selection context.

### Repairable trên lý thuyết = repairable thực tế

Thiếu parts/documentation/tool có thể làm repair không economic.

### No scheduled maintenance = no aging

Sealed/maintenance-free system vẫn degrade.

## Reusable checklist

```text
Required function:
Condition/time horizon:
Critical components:
Likely failure modes:
Consumables:
Warning signals:
Preventive/condition maintenance:
Diagnosis path:
Repairability:
Parts/support horizon:
Downtime:
Residual life after repair:
Evidence quality:
```

## Connections

- [`01_materials_quality_and_durability.md`](01_materials_quality_and_durability.md): material/process/degradation tạo failure mechanisms.
- [`00_reading_specs_labels_and_units.md`](00_reading_specs_labels_and_units.md): ratings chỉ có nghĩa trong test conditions.
- [`03_warranty_lifecycle_and_total_cost.md`](03_warranty_lifecycle_and_total_cost.md): reliability/repairability đi vào lifecycle cost như thế nào.
- [`../CONCEPTUAL_DEPENDENCIES.md`](../CONCEPTUAL_DEPENDENCIES.md): shared Life model từ mechanism đến failure/lifecycle.
- [`../../thinking/risk/`](../../thinking/risk/README.md): downside, redundancy, survivability và failure consequence.
- [`../../personal-finance/`](../../personal-finance/README.md): affordability/budgeting khi lifecycle cost trở thành household decision.

Điểm chốt: **reliability không nằm trong một material hoặc một warranty badge; nó xuất hiện từ architecture, interfaces, operating conditions, degradation, detection và khả năng phục hồi function**.