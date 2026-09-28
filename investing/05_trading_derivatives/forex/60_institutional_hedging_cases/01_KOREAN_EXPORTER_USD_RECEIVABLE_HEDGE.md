# Trường hợp (case / 사례) 01 — Korean Exporter: Hedge USD Receivables về KRW

Một Korean exporter có thể bán hàng bằng USD nhưng trả phần lớn lương, rent, domestic suppliers và reporting chi phí (cost / 비용) bằng KRW. Khi đó doanh nghiệp có **economic long USD / short KRW exposure** trên khoản phải thu.

Mục tiêu treasury không phải dự đoán USD/KRW tốt hơn thị trường (market / 시장). Mục tiêu là làm operating cash luồng (flow / 흐름) đủ ổn định để planning, pricing, debt dịch vụ (service / 서비스) và margin management không phụ thuộc quá mạnh vào một tỷ giá chưa biết.

## 1. Exposure trước hedge

Giả sử exporter dự kiến nhận:

```text
USD receivable = 10,000,000 USD
Expected receipt = 90 days
Functional/reporting currency = KRW
Current USD/KRW spot = 1,360
```

Nếu không hedge, KRW giá trị (value / 값) khi thu tiền là:

```text
KRW cash received
= USD 10m × future USD/KRW
```

Ở spot hiện tại, notional tham chiếu (reference / 참조):

```text
10,000,000 × 1,360
= 13.6 billion KRW
```

Nhưng đây chưa phải guaranteed cash luồng (flow / 흐름).

## 2. Directional exposure

Exporter sẽ bị bất lợi nếu KRW strengthens:

```text
USD/KRW falls
→ each USD converts into fewer KRW
→ KRW revenue falls
```

Exporter được lợi nếu KRW weakens:

```text
USD/KRW rises
→ more KRW per USD
```

Economic exposure:

```text
Long USD
Short KRW
```

## 3. Unhedged scenario bảng (table / 테이블)

Giả sử sau 90 ngày:

```text
USD/KRW = 1,250 → 12.5bn KRW
USD/KRW = 1,360 → 13.6bn KRW
USD/KRW = 1,450 → 14.5bn KRW
```

FX phạm vi (range / 범위) tạo difference 2.0bn KRW giữa extreme scenarios dù USD invoice không đổi.

Nếu operating margin vốn mỏng, FX có thể dominate nghiệp vụ (business / 비즈니스) kết quả (result / 결과).

## 4. Forward hedge

Exporter có thể **sell USD forward / buy KRW forward** cho maturity gần ngày receipt.

Concept:

```text
Future USD receivable
+ Short USD/KRW forward
→ locks approximate KRW conversion rate
```

Forward tỷ lệ (rate / 비율) không bằng spot forecast. Nó phản ánh:

```text
spot
+ relative interest rates
+ forward points
+ funding/basis/market terms
```

## 5. Example forward

Giả sử 3-month outright forward tương ứng:

```text
USD/KRW forward = 1,355
```

Exporter sells USD 10m forward at 1,355.

Approximate locked KRW giá trị (value / 값):

```text
10,000,000 × 1,355
= 13.55bn KRW
```

Ignoring giao dịch (transaction / 트랜잭션)/credit effects.

## 6. If KRW strengthens

At maturity:

```text
Spot = 1,250
```

Unhedged receivable converts to:

```text
12.5bn KRW
```

Forward hedge roughly contributes:

```text
(1,355 - 1,250) × USD 10m
= +1.05bn KRW
```

Combined approximate cash giá trị (value / 값):

```text
12.5bn + 1.05bn
= 13.55bn KRW
```

The derivative gain offsets weaker KRW giá trị (value / 값) of receivable.

## 7. If KRW weakens

At maturity:

```text
Spot = 1,450
```

Receivable converts to:

```text
14.5bn KRW
```

Forward contribution roughly:

```text
(1,355 - 1,450) × USD 10m
= -0.95bn KRW
```

Combined:

```text
14.5bn - 0.95bn
= 13.55bn KRW
```

Forward “mất mát (loss / 손실)” is not hedge thất bại (failure / 실패). It offsets the favorable move in underlying exposure.

## 8. Hedge mục tiêu (objective / 목표) is variance reduction

Wrong evaluation:

```text
Forward lost 950m KRW
→ hedge was bad
```

Correct evaluation:

```text
How variable was combined KRW cash flow
relative to unhedged exposure?
```

Treasury should evaluate portfolio of exposure + hedge.

## 9. Why hedge 100% may still be risky

Suppose USD 10m receivable is **forecast**, not legally fixed.

Actual sales could be only USD 7m.

If company hedged USD 10m:

```text
Receivable = +7m USD
Forward = -10m USD
Net = -3m USD
```

The firm accidentally becomes speculative short USD on USD 3m.

This is **over-hedge rủi ro (risk / 위험)**.

## 10. Forecast certainty matters

Separate:

```text
Committed receivable
Highly probable forecast sale
Uncertain sales forecast
```

Higher certainty supports higher hedge ratio.

Lower certainty may justify layered/partial hedging.

## 11. Layered hedging

Example chính sách (policy / 정책):

```text
0–3 months: hedge 80–100%
3–6 months: hedge 50–80%
6–12 months: hedge 20–50%
```

Chính xác (exact / 정확한) ratios depend on firm chính sách (policy / 정책), forecast độ tin cậy (reliability / 신뢰성) and rủi ro (risk / 위험) tolerance.

Concept:

```text
certainty decreases with horizon
→ hedge ratio can decrease with horizon
```

## 12. Layering across thời gian (time / 시간)

Instead of hedging entire expected USD 10m on one day:

```text
Month -6: hedge 20%
Month -4: add 20%
Month -2: add 30%
Invoice confirmed: add remaining policy amount
```

This reduces timing concentration in one thị trường (market / 시장) quote.

It does not guarantee better average tỷ lệ (rate / 비율).

## 13. Hedge tỷ lệ (rate / 비율) vs nghiệp vụ (business / 비즈니스) ngân sách (budget / 예산) tỷ lệ (rate / 비율)

Corporate planning may use a ngân sách (budget / 예산) tỷ lệ (rate / 비율):

```text
Budget USD/KRW = 1,330
```

Treasury can compare achieved hedge portfolio tỷ lệ (rate / 비율) with ngân sách (budget / 예산) các giả định (assumptions / 가정들).

But ngân sách (budget / 예산) tỷ lệ (rate / 비율) is nội bộ (internal / 내부) planning đầu vào (input / 입력), not fair-value prediction.

## 14. Natural hedge

If exporter also imports USD-denominated components:

```text
USD receivable = 10m
USD payable = 4m
```

Net giao dịch (transaction / 트랜잭션) exposure may be only:

```text
+6m USD
```

Hedging gross 10m while ignoring USD costs can overstate rủi ro (risk / 위험).

First step is **net exposure ánh xạ (mapping / 매핑)**.

## 15. Debt as natural offset

If company has USD debt dịch vụ (service / 서비스), some USD receivables may naturally fund it.

```text
USD revenue
→ USD interest/principal payment
```

Converting all USD into KRW and later buying USD again creates unnecessary turnover.

## 16. Timing mismatch

Receivable expected on day 90 may arrive day 105.

Forward settles on day 90.

Then treasury may need:

```text
short-term USD funding
or
FX swap to bridge timing
```

This is **timing/roll rủi ro (risk / 위험)**, even if amount is correct.

## 17. Amount mismatch

Customer may pay partially.

If hedge maturity is fixed but receivable amount changes, company must resize/close/roll hedge.

This creates giao dịch (transaction / 트랜잭션) chi phí (cost / 비용) and potentially realized P/L before underlying cash arrives.

## 18. Forward points are economics, not fee

If 3-month forward is below spot, exporter may feel it is “giving up” spot points.

But forward points primarily encode relative funding/tỷ lệ (rate / 비율) economics plus thị trường (market / 시장) basis/terms.

Do not interpret:

```text
spot - forward
```

as broker fee automatically.

## 19. NDF possibility

For restricted/non-deliverable currencies, hedge may use NDF rather than deliverable forward.

Settlement is typically net cash based on fixing difference according to đặc tả hợp đồng (contract / 계약).

For KRW institutional markets, actual truy cập (access / 접근)/sản phẩm (product / 제품) choice depends on thực thể (entity / 엔터티), jurisdiction, thị trường (market / 시장) tuyến (route / 경로) and hiện tại (current / 현재) regulation.

Always verify hiện tại (current / 현재) legal/operational truy cập (access / 접근).

## 20. Option hedge

Instead of fixing tỷ lệ (rate / 비율) with forward, exporter can buy protection against KRW strengthening while retaining upside if USD strengthens.

Conceptual cấu trúc (structure / 구조):

```text
Buy USD put / KRW call equivalent
```

depending quote convention/sản phẩm (product / 제품) documentation.

Economic goal:

```text
protect minimum KRW conversion value
while preserving some favorable USD upside
```

## 21. Option premium

Optionality costs premium.

Forward:

```text
low/no upfront premium in common structures
but locks rate
```

Option:

```text
upfront premium
but asymmetric payoff
```

Choice depends on nghiệp vụ (business / 비즈니스) mục tiêu (objective / 목표), not belief that one instrument is universally superior.

## 22. Participating structures

Structured hedges may reduce premium by giving up part of favorable FX move.

These products can introduce:

```text
knock-in/knock-out
leverage
barrier
conditional notional
```

Treasury must mô hình (model / 모델) payoff under stress before using them.

“Zero premium” does not mean zero economic chi phí (cost / 비용) or zero tail rủi ro (risk / 위험).

## 23. Counterparty rủi ro (risk / 위험)

OTC forward creates counterparty exposure.

Need consider:

```text
legal entity
credit line
collateral terms
netting
settlement
```

A hedge that cannot settle when needed fails operationally even if price economics were correct.

## 24. Credit-line usage

Large forward book can consume bank credit lines.

Thus hedge sức chứa (capacity / 용량) is not unlimited.

During stress, required collateral/limits may tighten.

## 25. Liquidity concentration

If all hedges mature on quarter-end:

```text
large roll at same date
```

creates thực thi (execution / 실행) concentration.

Layering maturities can reduce operational/liquidity rủi ro (risk / 위험).

## 26. Forecast lỗi (error / 오류) attribution

Suppose hedge ratio looks poor because sales forecast was wrong.

Separate:

```text
Hedge execution error
from
Business forecast error
```

Treasury should not be blamed for volume bất định (uncertainty / 불확실성) it did not điều khiển (control / 제어), but chính sách (policy / 정책) should account for that bất định (uncertainty / 불확실성).

## 27. Hedge effectiveness decomposition

At rà soát (review / 검토):

```text
Underlying FX effect
+ Hedge instrument P/L
+ Forward/carry effect
+ Transaction cost
+ Timing mismatch
+ Volume mismatch
= Combined economic result
```

This is more informative than derivative P/L alone.

## 28. Pricing phản hồi (feedback / 피드백) to nghiệp vụ (business / 비즈니스)

If treasury can khóa (lock / 잠금) approximate FX tỷ lệ (rate / 비율), sales nhóm (team / 팀) can quote foreign customers with more predictable KRW margin.

Hedging therefore interacts with commercial pricing.

## 29. Economic exposure beyond booked receivables

Even if invoices are hedged, long-term competitiveness changes with FX.

Example:

```text
KRW strengthens structurally
→ Korean exporter products become more expensive relative to competitors
```

Forward hedge on 90-day receivable does not eliminate this **economic exposure**.

## 30. Giao dịch (transaction / 트랜잭션) vs economic exposure

```text
Transaction exposure
= contracted/forecast cash flow

Economic exposure
= long-run effect of FX on prices, volume, costs, competitiveness
```

Do not assume treasury derivatives solve strategic currency exposure.

## 31. Scenario ma trận (matrix / 행렬)

Bản dựng (build / 빌드) bảng (table / 테이블):

```text
USD/KRW: 1,200 / 1,300 / 1,400 / 1,500
Actual sales: 60% / 80% / 100% / 120% forecast
Receipt delay: 0 / 15 / 30 days
```

For each calculate:

```text
Underlying KRW cash
Hedge P/L
Net USD over/under-hedge
Roll cost
Combined KRW cash
```

## 32. Stress trường hợp (case / 사례) — sales collapse + KRW weakness

This trường hợp (case / 사례) is counterintuitive.

If KRW weakens strongly but actual USD sales collapse:

```text
forward hedge may lose
while underlying receivable is smaller than expected
```

The firm can suffer over-hedge mất mát (loss / 손실) despite favorable currency move for remaining exports.

Business-volume rủi ro (risk / 위험) and FX rủi ro (risk / 위험) interact.

## 33. Stress trường hợp (case / 사례) — customer default

If receivable disappears after hedge is booked:

```text
underlying exposure = 0
hedge remains
```

Treasury must close hedge, realizing thị trường (market / 시장) P/L.

Credit rủi ro (risk / 위험) can therefore create FX position unexpectedly.

## 34. Stress trường hợp (case / 사례) — bank line reduced

If bank cuts OTC credit line during stress:

```text
company may be unable to roll existing hedge as planned
```

Counterparty diversification can be part of hedge chính sách (policy / 정책).

## 35. Hedge chính sách (policy / 정책) metrics

Monitor:

```text
Hedge ratio by horizon
Forecast accuracy
Weighted-average hedge rate
Maturity concentration
Counterparty concentration
Over/under-hedge amount
Combined cash-flow variance
Hedge transaction cost
```

## 36. Quyết định (decision / 결정) quy tắc (rule / 규칙) should not depend on trader view

A treasury chính sách (policy / 정책) might define hedge ratio mechanically from exposure certainty.

This reduces temptation:

```text
"We think USD will rise, so skip hedge"
```

which converts rủi ro (risk / 위험) management into speculation.

## 37. Tactical discretion

If chính sách (policy / 정책) allows tactical phạm vi (range / 범위), define bounds:

```text
Strategic hedge target = 70%
Allowed range = 60–80%
```

Then evaluate discretion separately from cốt lõi (core / 핵심) hedge chính sách (policy / 정책).

## 38. Quản trị (governance / 거버넌스)

Separate roles conceptually:

```text
Business forecasts exposure
Treasury executes hedge
Risk/finance reviews limits and reporting
```

Even in smaller company, separating responsibilities mentally reduces incentive problems.

## 39. Hedge report template

```text
Exposure period
Forecast USD revenue
Committed USD receivable
Natural USD offsets
Net exposure
Policy hedge target
Actual hedge
Weighted forward rate
Maturity distribution
Counterparties
Stress over-hedge
Combined scenario cash flow
```

## 40. Worked layered example

Forecast USD revenue over next six months:

```text
Month 1: 2m
Month 2: 2m
Month 3: 2m
Month 4: 2m
Month 5: 1m
Month 6: 1m
```

Chính sách (policy / 정책):

```text
0–3m hedge 80%
4–6m hedge 40%
```

Initial hedge notionals:

```text
Months 1–3: 6m × 80% = 4.8m USD
Months 4–6: 4m × 40% = 1.6m USD
Total = 6.4m USD
```

Not USD 10m.

As invoices become committed, increase hedge toward chính sách (policy / 정책) ratio.

## 41. Why not simply hedge after invoice?

Waiting until invoice eliminates forecast-volume rủi ro (risk / 위험) but leaves earlier commercial margin exposed.

If pricing/môi trường vận hành (production / 운영 환경) decisions occur months before invoice:

```text
FX risk begins economically before receivable is booked
```

This is why firms hedge forecast transactions subject to chính sách (policy / 정책)/accounting/legal các ràng buộc (constraints / 제약조건들).

## 42. Hedge accounting ranh giới (boundary / 경계)

Accounting treatment can materially affect reported earnings volatility, documentation and designation requirements.

This trường hợp (case / 사례) focuses on economic rủi ro (risk / 위험) mechanics, not jurisdiction-specific hedge-accounting rules.

If used professionally, hiện tại (current / 현재) accounting standards and company chính sách (policy / 정책) must be checked separately.

## 43. What not to learn

Wrong:

```text
Exporter should always hedge 100%.
```

Wrong:

```text
Forward loss means treasury made a bad trade.
```

Wrong:

```text
Hedging eliminates all FX risk.
```

Better:

```text
Hedge ratio and instrument should match exposure certainty,
objective, tenor, liquidity and residual-risk tolerance.
```

## 44. Trường hợp (case / 사례) đầu ra (output / 출력)

Create:

```text
exporter_exposure_map.md
exporter_cashflow_timeline.md
layered_hedge_policy.md
scenario_matrix.md
hedge_attribution_report.md
counterparty_maturity_dashboard.md
```

## 45. Rà soát (review / 검토) questions

You should be able to explain:

1. Why exporter is economically long USD.
2. Why forward mất mát (loss / 손실) can coincide with successful hedge.
3. Why forecast lỗi (error / 오류) creates over-hedge rủi ro (risk / 위험).
4. Why natural hedges should be netted before derivatives.
5. Why forward points are not simply a fee.
6. Why options thay đổi (change / 변경) payoff shape rather than eliminate chi phí (cost / 비용).
7. Why 90-day hedge does not remove long-term competitiveness exposure.

## Nội bộ (internal / 내부) links

- [Funding, NDF, basis and forward curve](../90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md)
- [Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
- [FX options and hedging](../14_FX_OPTIONS_VOLATILITY_AND_HEDGING.md)
