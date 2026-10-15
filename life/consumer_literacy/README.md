# Consumer Literacy — Đọc sản phẩm bằng cơ chế thay vì marketing

Consumer literacy trong `life/` không phải “mẹo săn sale”. Nó là khả năng nhìn một sản phẩm và biết **cần đọc spec nào, label nào chỉ là proxy, trade-off nào đang bị ẩn, tuổi thọ bị chi phối bởi cơ chế nào, failure nào đáng lo và tổng chi phí sở hữu phát sinh từ đâu**.

Backbone này được dùng lại cho Cars, Food & Drink và các vertical tương lai. Nó tránh việc mỗi product domain tự viết lại những ý như `spec ≠ quality`, `feature count ≠ usefulness`, `material name ≠ durability` hay `purchase price ≠ lifecycle cost`.

## Mental model

```text
Use case
→ constraints
→ relevant properties
→ measurement / spec
→ mechanism behind the spec
→ material / construction
→ trade-offs
→ degradation / failure
→ maintenance / repairability
→ warranty / lifecycle cost
→ evidence / reviews / claims
→ comparison / decision
```

Điểm quan trọng là thứ tự. Nếu bắt đầu bằng bảng specification trước khi biết use case, ta rất dễ tối ưu metric không liên quan. Nếu dừng ở material/spec, ta lại bỏ qua phần product thay đổi theo time và failure.

## Learning route

1. [`00_reading_specs_labels_and_units.md`](00_reading_specs_labels_and_units.md) — một spec thực sự đo gì, unit/test condition quan trọng ra sao và vì sao một con số không đại diện cho total quality.
2. [`01_materials_quality_and_durability.md`](01_materials_quality_and_durability.md) — material, processing, construction và degradation cùng tạo ra durability như thế nào.
3. [`02_reliability_repairability_and_maintenance.md`](02_reliability_repairability_and_maintenance.md) — required function, failure mode, consumable, maintenance, diagnostics, parts và repairability liên kết ra sao.
4. [`03_warranty_lifecycle_and_total_cost.md`](03_warranty_lifecycle_and_total_cost.md) — warranty là risk allocation chứ không phải reliability score; acquisition, operating, service, downtime, replacement và residual value tạo lifecycle cost thế nào.

Bốn chapter này tạo backbone đủ để một product-domain chapter không phải lặp lại generic consumer framework. Gap lớn còn lại là marketing/reviews/product claims; chỉ mở chapter riêng khi nó có đủ depth vượt quá các handoff sang Thinking.

## Specification không phải quality score

Một spec thường đo một property dưới điều kiện cụ thể.

Ví dụ:

```text
horsepower
battery capacity
ABV
IBU
screen brightness
water resistance rating
fabric weight
```

Mỗi số đều có value, nhưng không số nào tự trả lời:

> “Sản phẩm này có tốt cho tôi không?”

Câu hỏi đúng hơn:

```text
Spec này đo property nào?
Property đó liên quan thế nào đến use case?
Điều kiện test có giống use thực tế không?
Trade-off nào đi cùng việc đẩy spec lên cao?
```

## Material không tự động quyết định durability

Product behavior xuất hiện từ interaction:

```text
material
× geometry
× process
× joining
× environment
× maintenance
```

Một headline material tốt không cứu được weak joint, poor coating hoặc failure-prone subsystem. Vì vậy material claim chỉ là điểm bắt đầu của quality reasoning.

## Durability không phải reliability

Durability nói về chịu degradation; reliability nói system có thực hiện required function trong condition/time cụ thể không.

Một product có chassis rất durable vẫn có thể kém reliable nếu connector, seal, electronics hoặc control subsystem thường fail.

Đây là lý do Consumer Literacy phải đi tiếp từ “chất liệu gì?” sang:

```text
what fails first?
can failure be detected?
can failed function be restored?
what maintenance changes probability?
```

## Giá không phải total cost

Purchase price dễ thấy nhất nhưng lifecycle còn có:

```text
consumables
energy / fuel
maintenance
repair
downtime
replacement cycle
resale value
```

`life/` giải thích object-side drivers tạo các cost đó; affordability, debt và household planning vẫn thuộc [`../../personal-finance/`](../../personal-finance/README.md).

## Warranty không tự động chứng minh reliability

Warranty là contract xác định một phần risk ai chịu trong một period/condition. Nó cần được đọc cùng:

```text
coverage
exclusions
parts/labor
claim friction
maintenance conditions
support horizon
```

Warranty dài hơn có thể có value, nhưng không được dùng như direct failure-rate statistic nếu không có evidence khác.

## Review không tự động là evidence mạnh

Review hữu ích để tìm failure modes, usability issue và pattern mà spec sheet không thể hiện. Nhưng review score có thể bị selection bias, fake review, expectation effect hoặc khác use case.

Khi claim cần kiểm chứng, dùng:

- [`../../thinking/critical-thinking/`](../../thinking/critical-thinking/README.md)
- [`../../thinking/causal-reasoning/`](../../thinking/causal-reasoning/README.md)

Khi một con số nghe vô lý hoặc quá đẹp, dùng [`../../thinking/statistics-for-life/`](../../thinking/statistics-for-life/README.md) để kiểm tra denominator, baseline và cách đọc quantity. Các practice file mới ở Thinking v2 chỉ nên được link trực tiếp sau khi chúng tồn tại trên canonical `main`.

## Comparison route

Khi compare hai sản phẩm, dùng route:

```text
use case
→ must-have constraints
→ relevant specs
→ mechanism/material
→ dominant failure modes
→ maintenance / repairability
→ lifecycle/TCO
→ evidence quality
→ decision
```

Không cần convert mọi thứ thành một score. Một product có thể tốt hơn theo objective A và kém hơn theo objective B.

## Boundary

Consumer Literacy không thay product-domain mechanism. Muốn hiểu transmission, đọc Cars; muốn hiểu whisky maturation, đọc Whisky. Backbone này chỉ cung cấp **cách đọc, đánh giá và so sánh thông tin về sản phẩm** sau khi mechanism đã đủ rõ.

Nó cũng không thay Personal Finance hoặc Thinking: “product có TCO nào?” là Life; “tôi có afford được không?” là Personal Finance; “với uncertainty này tôi nên chọn option nào?” là Thinking.