# Warranty, Lifecycle & Total Cost — Giá mua chỉ là điểm bắt đầu

Một sản phẩm rẻ lúc mua có thể đắt trong suốt vòng đời; một sản phẩm đắt hơn có thể lại rẻ hơn nếu dùng lâu, ít downtime, ít consumable và giữ resale value tốt. Nhưng ngược lại, trả premium lớn chỉ để “hy vọng bền hơn” cũng không tự động rational nếu evidence yếu hoặc use horizon ngắn.

Chapter này nối ba lớp:

```text
warranty
→ ai chịu risk nào trong một khoảng thời gian

lifecycle
→ product thay đổi, được dùng, service và kết thúc như thế nào

TCO / total cost of ownership
→ toàn bộ cost materially gắn với việc sở hữu/sử dụng trong horizon đã chọn
```

Personal Finance giữ budget, debt, affordability và household planning. `life/` chỉ giải thích **object-side cost drivers** để người dùng biết cần đưa gì vào comparison.

## 1. Warranty là contract, không phải durability score

Warranty (bảo hành / 보증) quy định một số failure/condition nào đó được manufacturer/seller chịu trách nhiệm trong khoảng thời gian và điều kiện cụ thể.

Một warranty dài có thể phản ánh confidence, positioning hoặc business model, nhưng không tự động chứng minh failure rate thấp.

Cần tách:

```text
product reliability
≠
warranty coverage
```

Và đọc warranty theo:

```text
what is covered?
for how long?
what is excluded?
parts only or labor too?
who pays transport/downtime?
what maintenance proof is required?
what happens after repair/replacement?
```

Các chi tiết legal/statutory rights phụ thuộc jurisdiction và thời điểm. Khi cần quyết định thật, phải kiểm tra nguồn chính thức hoặc policy hiện hành; không dùng chapter này như legal advice.

## 2. Warranty exclusion thường cho biết boundary của designed responsibility

Các exclusion phổ biến có thể liên quan:

- consumable/wear item;
- misuse;
- accidental damage;
- unauthorized modification;
- environmental exposure ngoài rating;
- cosmetic wear;
- software/service condition.

Không nên diễn giải exclusion như bằng chứng product yếu. Nó cho biết **risk nào được transfer cho vendor và risk nào vẫn nằm ở user**.

Đây là perspective hữu ích hơn việc chỉ so “1 năm vs 3 năm”.

## 3. Lifecycle cần một horizon rõ

Không có “TCO tuyệt đối”; TCO luôn phụ thuộc horizon và use pattern.

Ví dụ:

```text
3-year ownership
vs
10-year ownership
```

có thể cho ranking khác nhau vì depreciation, maintenance và replacement cycle xuất hiện ở thời điểm khác.

Trước comparison, ghi:

```text
ownership horizon
usage intensity
environment
expected resale / disposal path
criticality of downtime
```

Nếu horizon không rõ, total cost calculation rất dễ biến thành spreadsheet precision nhưng decision premise sai.

## 4. Lifecycle của product không chỉ gồm “mua → dùng → bỏ”

Một mental model tốt hơn:

```text
acquisition
→ setup / installation
→ normal use
→ consumables / energy
→ maintenance
→ degradation
→ repair / downtime
→ upgrade / support change
→ resale / disposal / replacement
```

Mỗi phase có cost hoặc risk khác nhau.

Ví dụ appliance cần installation; car có registration/insurance/maintenance; electronics có software support; tools có consumables; furniture có transport/assembly.

Không phải category nào cũng cần mọi dòng. Chỉ giữ cost materially liên quan use case.

## 5. Total cost nên phân loại để tránh double-count

Một khung chung:

### Acquisition cost

```text
purchase price
shipping
installation
accessories required to operate
initial fees
```

### Operating cost

```text
energy / fuel
consumables
subscriptions needed for core use
routine maintenance
```

### Failure / service cost

```text
repair parts
labor
transport/service visit
downtime
temporary replacement
```

### Lifecycle transition cost

```text
upgrade
replacement
disposal
resale loss / depreciation
```

### Risk-adjusted cost

Một số cost không chắc xảy ra. Không cần luôn tính expected value chính xác, nhưng ít nhất phải nói:

```text
possible cost
probability/range
impact if it occurs
```

Handoff reasoning sâu sang [`../../thinking/risk/`](../../thinking/risk/README.md) và [`../../thinking/expected-value/`](../../thinking/expected-value/README.md).

## 6. Purchase price có thể là phần nhỏ của TCO

Một item energy-intensive hoặc consumable-heavy có thể có operating cost lớn hơn purchase premium.

Ví dụ abstract:

```text
Option A
purchase 100
annual operating 40
5-year repair 30
resale 10

Option B
purchase 150
annual operating 20
5-year repair 10
resale 30
```

Không cần conclusion từ numbers giả; lesson là **front-loaded cost và lifecycle cost có timing khác nhau**.

Vì vậy comparison phải bắt đầu bằng use horizon, không bằng sticker price.

## 7. Cost per use chỉ hữu ích khi denominator đúng

Có thể tính:

```text
lifecycle cost / number of useful uses
```

nhưng denominator cần meaning.

Một coat dùng 300 lần khác one-off appliance dùng 20 lần; car “cost per km” không capture convenience/time; laptop “cost per day” không capture productivity.

Cost per use là một lens, không phải universal objective.

Rule:

> denominator phải phản ánh use case, không chỉ là con số dễ đếm.

## 8. Energy efficiency cần đặt trong actual usage

Một product efficient hơn chỉ tạo meaningful savings nếu:

```text
energy difference
× usage volume
× energy price
× ownership horizon
```

Nếu usage rất thấp, premium cho efficiency có thể không recover theo purely monetary terms; nếu usage cao, operating difference có thể dominate.

Ngoài money còn có heat/noise/environment/peak-power constraints tùy use case.

Đừng đọc efficiency rating tách khỏi usage.

## 9. Consumable ecosystem có thể khóa lifecycle cost

Một sản phẩm rẻ nhưng proprietary consumable đắt có thể tạo recurring cost lớn.

Cần hỏi:

```text
consumable frequency
unit cost
third-party compatibility
availability
storage/shelf life
replacement complexity
```

Đây là nơi product architecture và business model gặp nhau.

Tuy nhiên đừng mặc định proprietary luôn xấu: nó có thể đảm bảo compatibility/performance. Cần so trade-off thực tế.

## 10. Maintenance cost và deferred maintenance khác nhau

Không làm maintenance có thể tiết kiệm short-term nhưng tăng risk downstream.

Ví dụ conceptual:

```text
skip cheap maintenance
→ accelerated wear
→ secondary damage
→ larger repair / downtime
```

Nhưng maintenance không có causal link với dominant failure cũng có thể chỉ thêm cost.

Vì vậy TCO phải dựa trên maintenance mechanism từ [`02_reliability_repairability_and_maintenance.md`](02_reliability_repairability_and_maintenance.md), không phải ritual list.

## 11. Downtime phải được định giá theo criticality

Một object fail có thể không tốn nhiều repair money nhưng tạo cost lớn nếu critical cho work/safety.

Có thể phân loại:

```text
low criticality:
replacement/use can wait

medium:
need temporary workaround

high:
work/safety/operation stops
```

Downtime value không nhất thiết phải convert thành tiền chính xác. Chỉ cần explicit để không bỏ qua một cost quan trọng.

## 12. Repairability thay đổi expected lifecycle

Hai sản phẩm có cùng failure probability nhưng lifecycle khác nếu:

```text
A: failed module replaceable for 10
B: same module integrated, replacement product 100
```

Do đó TCO cần nhìn:

- modularity;
- spare parts;
- diagnostics;
- labor;
- vendor support horizon.

Repairability thường không xuất hiện trên headline spec sheet nhưng có thể dominate long-term ownership.

## 13. Depreciation và resale là residual value, không phải “free money”

Nếu product có resale market, net ownership cost có thể giảm bởi residual value.

Conceptual:

```text
net lifecycle cost
≈ acquisition + operation + maintenance + repair + downtime - residual value
```

Nhưng resale value uncertain và phụ thuộc condition/market/time. Không nên dùng optimistic resale để làm một purchase trông rẻ.

Với personal balance-sheet decision, handoff sang Personal Finance.

## 14. Replacement cycle có thể làm cheap product đắt

Nếu option A giá bằng 60% option B nhưng phải thay gấp đôi trong cùng horizon, sticker-price advantage có thể biến mất.

Cần hỏi:

```text
expected useful life
failure distribution
repair path
support horizon
obsolescence risk
```

Obsolescence không chỉ physical wear. Software support, compatibility hoặc ecosystem change có thể làm product functionally obsolete dù hardware còn tốt.

## 15. Planned obsolescence không nên được giả định nếu thiếu evidence

Khi product life ngắn, có nhiều explanations:

- cost-performance trade-off;
- rapid technology change;
- support economics;
- integrated design;
- regulation/security requirement;
- actual deliberate lifecycle strategy.

Không suy motive từ outcome alone. Nếu claim về deliberate obsolescence, cần evidence về design/business decisions, không chỉ anecdote “máy cũ chậm”.

Handoff sang Critical Thinking khi đọc claim này.

## 16. Warranty extension / protection plan là risk-transfer decision

Một extended warranty hoặc protection plan đổi:

```text
upfront known cost
vs
uncertain future repair cost
```

Đánh giá cần:

```text
coverage
exclusions
deductible
claim friction
repair probability
repair cost distribution
ability to self-insure
```

Không thể kết luận universally “nên/không nên”. Expected monetary value chỉ là một layer; risk aversion, liquidity và downside cũng matter. Financial choice thuộc Personal Finance/Thinking.

## 17. TCO nên dùng range thay vì một con số duy nhất

Nhiều input uncertain:

```text
energy price
repair count
resale value
ownership period
usage
replacement timing
```

Thay vì:

> “TCO = 4,372,281”

hãy dùng:

```text
base case
low-use / favorable case
high-use / adverse case
```

Và sensitivity:

> Input nào làm ranking A/B đổi?

Nếu ranking chỉ tồn tại dưới một assumption rất precise, decision không robust.

## 18. Sunk cost không quyết định repair-vs-replace

Khi product đã mua, original purchase price phần lớn là sunk cost. Decision repair-vs-replace nên nhìn forward:

```text
repair cost now
remaining expected life
future maintenance/repair
replacement cost
replacement benefits
residual value
switching cost
```

“Đã bỏ nhiều tiền rồi nên phải sửa tiếp” có thể là sunk-cost trap.

Handoff sang [`../../thinking/opportunity-cost/`](../../thinking/opportunity-cost/README.md) và Decision Making.

## 19. Lifecycle worksheet

```text
Product / option:
Use case:
Ownership horizon:
Usage intensity:

Acquisition:
Purchase:
Setup/accessories:

Operating:
Energy/fuel:
Consumables:
Subscriptions:
Routine maintenance:

Failure/service:
Likely repairs:
Parts/labor:
Downtime/workaround:

Lifecycle:
Expected useful life:
Support horizon:
Replacement cycle:
Residual value:
Disposal/switching:

Uncertainty:
Most sensitive assumptions:
Adverse scenario:
What would change option ranking:
```

Không cần fill mọi row. Worksheet tồn tại để nhắc rằng sticker price chỉ là một phase.

## 20. Drill — so hai sản phẩm theo lifecycle

Chọn hai sản phẩm cùng use case.

### Step 1 — bỏ brand prestige

Chỉ ghi:

```text
use horizon
usage
must-have function
```

### Step 2 — map lifecycle

Tạo 4 bucket:

```text
acquisition
operation
service/failure
exit/replacement
```

### Step 3 — gắn uncertainty

Mỗi item ghi:

```text
known / estimated / unknown
```

### Step 4 — sensitivity

Hỏi:

> Assumption nào nếu đổi 30–50% sẽ đảo ranking?

Nếu answer là resale hoặc repair probability mà evidence yếu, conclusion phải giữ uncertainty tương ứng.

## Common failure modes

### Cheapest purchase = cheapest ownership

Bỏ operating/service/replacement.

### Warranty = reliability

Nhầm contract với failure probability.

### False precision

TCO decimal nhưng inputs rất uncertain.

### Ignoring downtime

Chỉ tính invoice repair.

### Optimistic resale

Dùng residual value như guaranteed.

### Over-maintenance hidden cost

Giả định mọi service recommendation đều tạo proportional reliability benefit.

### Sunk-cost repair

Dùng tiền đã chi để justify future spending.

### Lifetime mismatch

So product 3-year use với assumptions 10-year hoặc ngược lại.

## Connections

- [`00_reading_specs_labels_and_units.md`](00_reading_specs_labels_and_units.md): efficiency/rating/spec cần đúng protocol.
- [`01_materials_quality_and_durability.md`](01_materials_quality_and_durability.md): degradation ảnh hưởng useful life.
- [`02_reliability_repairability_and_maintenance.md`](02_reliability_repairability_and_maintenance.md): failure, serviceability và downtime.
- [`../CONCEPTUAL_DEPENDENCIES.md`](../CONCEPTUAL_DEPENDENCIES.md): lifecycle là layer cuối của object reasoning.
- [`../../personal-finance/`](../../personal-finance/README.md): affordability, debt, emergency liquidity và household planning.
- [`../../thinking/opportunity-cost/`](../../thinking/opportunity-cost/README.md): best forgone alternative và sunk cost.
- [`../../thinking/risk/`](../../thinking/risk/README.md): uncertain downside.
- [`../../thinking/decision-making/`](../../thinking/decision-making/README.md): comparison under uncertainty.

Điểm chốt: **TCO không phải công thức để luôn chọn món đắt hơn hoặc bền hơn; nó là cách buộc decision nhìn toàn lifecycle, đúng horizon và đúng uncertainty thay vì chỉ nhìn price tag**.