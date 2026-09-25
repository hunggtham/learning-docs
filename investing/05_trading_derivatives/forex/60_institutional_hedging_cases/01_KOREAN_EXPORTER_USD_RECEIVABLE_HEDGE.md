# Case 01 — Korean Exporter: Hedge USD Receivables về KRW

Một Korean exporter có thể bán hàng bằng USD nhưng trả phần lớn lương, rent, domestic suppliers và reporting cost bằng KRW. Khi đó doanh nghiệp có **economic long USD / short KRW exposure** trên khoản phải thu.

Mục tiêu treasury không phải dự đoán USD/KRW tốt hơn market. Mục tiêu là làm operating cash flow đủ ổn định để planning, pricing, debt service và margin management không phụ thuộc quá mạnh vào một tỷ giá chưa biết.

## 1. Exposure trước hedge

Giả sử exporter dự kiến nhận:

```text
USD receivable = 10,000,000 USD
Expected receipt = 90 days
Functional/reporting currency = KRW
Current USD/KRW spot = 1,360
```

Nếu không hedge, KRW value khi thu tiền là:

```text
KRW cash received
= USD 10m × future USD/KRW
```

Ở spot hiện tại, notional reference:

```text
10,000,000 × 1,360
= 13.6 billion KRW
```

Nhưng đây chưa phải guaranteed cash flow.

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

## 3. Unhedged scenario table

Giả sử sau 90 ngày:

```text
USD/KRW = 1,250 → 12.5bn KRW
USD/KRW = 1,360 → 13.6bn KRW
USD/KRW = 1,450 → 14.5bn KRW
```

FX range tạo difference 2.0bn KRW giữa extreme scenarios dù USD invoice không đổi.

Nếu operating margin vốn mỏng, FX có thể dominate business result.

## 4. Forward hedge

Exporter có thể **sell USD forward / buy KRW forward** cho maturity gần ngày receipt.

Concept:

```text
Future USD receivable
+ Short USD/KRW forward
→ locks approximate KRW conversion rate
```

Forward rate không bằng spot forecast. Nó phản ánh:

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

Approximate locked KRW value:

```text
10,000,000 × 1,355
= 13.55bn KRW
```

Ignoring transaction/credit effects.

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

Combined approximate cash value:

```text
12.5bn + 1.05bn
= 13.55bn KRW
```

The derivative gain offsets weaker KRW value of receivable.

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

Forward “loss” is not hedge failure. It offsets the favorable move in underlying exposure.

## 8. Hedge objective is variance reduction

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

This is **over-hedge risk**.

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

Example policy:

```text
0–3 months: hedge 80–100%
3–6 months: hedge 50–80%
6–12 months: hedge 20–50%
```

Exact ratios depend on firm policy, forecast reliability and risk tolerance.

Concept:

```text
certainty decreases with horizon
→ hedge ratio can decrease with horizon
```

## 12. Layering across time

Instead of hedging entire expected USD 10m on one day:

```text
Month -6: hedge 20%
Month -4: add 20%
Month -2: add 30%
Invoice confirmed: add remaining policy amount
```

This reduces timing concentration in one market quote.

It does not guarantee better average rate.

## 13. Hedge rate vs business budget rate

Corporate planning may use a budget rate:

```text
Budget USD/KRW = 1,330
```

Treasury can compare achieved hedge portfolio rate with budget assumptions.

But budget rate is internal planning input, not fair-value prediction.

## 14. Natural hedge

If exporter also imports USD-denominated components:

```text
USD receivable = 10m
USD payable = 4m
```

Net transaction exposure may be only:

```text
+6m USD
```

Hedging gross 10m while ignoring USD costs can overstate risk.

First step is **net exposure mapping**.

## 15. Debt as natural offset

If company has USD debt service, some USD receivables may naturally fund it.

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

This is **timing/roll risk**, even if amount is correct.

## 17. Amount mismatch

Customer may pay partially.

If hedge maturity is fixed but receivable amount changes, company must resize/close/roll hedge.

This creates transaction cost and potentially realized P/L before underlying cash arrives.

## 18. Forward points are economics, not fee

If 3-month forward is below spot, exporter may feel it is “giving up” spot points.

But forward points primarily encode relative funding/rate economics plus market basis/terms.

Do not interpret:

```text
spot - forward
```

as broker fee automatically.

## 19. NDF possibility

For restricted/non-deliverable currencies, hedge may use NDF rather than deliverable forward.

Settlement is typically net cash based on fixing difference according to contract.

For KRW institutional markets, actual access/product choice depends on entity, jurisdiction, market route and current regulation.

Always verify current legal/operational access.

## 20. Option hedge

Instead of fixing rate with forward, exporter can buy protection against KRW strengthening while retaining upside if USD strengthens.

Conceptual structure:

```text
Buy USD put / KRW call equivalent
```

depending quote convention/product documentation.

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

Choice depends on business objective, not belief that one instrument is universally superior.

## 22. Participating structures

Structured hedges may reduce premium by giving up part of favorable FX move.

These products can introduce:

```text
knock-in/knock-out
leverage
barrier
conditional notional
```

Treasury must model payoff under stress before using them.

“Zero premium” does not mean zero economic cost or zero tail risk.

## 23. Counterparty risk

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

Thus hedge capacity is not unlimited.

During stress, required collateral/limits may tighten.

## 25. Liquidity concentration

If all hedges mature on quarter-end:

```text
large roll at same date
```

creates execution concentration.

Layering maturities can reduce operational/liquidity risk.

## 26. Forecast error attribution

Suppose hedge ratio looks poor because sales forecast was wrong.

Separate:

```text
Hedge execution error
from
Business forecast error
```

Treasury should not be blamed for volume uncertainty it did not control, but policy should account for that uncertainty.

## 27. Hedge effectiveness decomposition

At review:

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

## 28. Pricing feedback to business

If treasury can lock approximate FX rate, sales team can quote foreign customers with more predictable KRW margin.

Hedging therefore interacts with commercial pricing.

## 29. Economic exposure beyond booked receivables

Even if invoices are hedged, long-term competitiveness changes with FX.

Example:

```text
KRW strengthens structurally
→ Korean exporter products become more expensive relative to competitors
```

Forward hedge on 90-day receivable does not eliminate this **economic exposure**.

## 30. Transaction vs economic exposure

```text
Transaction exposure
= contracted/forecast cash flow

Economic exposure
= long-run effect of FX on prices, volume, costs, competitiveness
```

Do not assume treasury derivatives solve strategic currency exposure.

## 31. Scenario matrix

Build table:

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

## 32. Stress case — sales collapse + KRW weakness

This case is counterintuitive.

If KRW weakens strongly but actual USD sales collapse:

```text
forward hedge may lose
while underlying receivable is smaller than expected
```

The firm can suffer over-hedge loss despite favorable currency move for remaining exports.

Business-volume risk and FX risk interact.

## 33. Stress case — customer default

If receivable disappears after hedge is booked:

```text
underlying exposure = 0
hedge remains
```

Treasury must close hedge, realizing market P/L.

Credit risk can therefore create FX position unexpectedly.

## 34. Stress case — bank line reduced

If bank cuts OTC credit line during stress:

```text
company may be unable to roll existing hedge as planned
```

Counterparty diversification can be part of hedge policy.

## 35. Hedge policy metrics

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

## 36. Decision rule should not depend on trader view

A treasury policy might define hedge ratio mechanically from exposure certainty.

This reduces temptation:

```text
"We think USD will rise, so skip hedge"
```

which converts risk management into speculation.

## 37. Tactical discretion

If policy allows tactical range, define bounds:

```text
Strategic hedge target = 70%
Allowed range = 60–80%
```

Then evaluate discretion separately from core hedge policy.

## 38. Governance

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

Policy:

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

As invoices become committed, increase hedge toward policy ratio.

## 41. Why not simply hedge after invoice?

Waiting until invoice eliminates forecast-volume risk but leaves earlier commercial margin exposed.

If pricing/production decisions occur months before invoice:

```text
FX risk begins economically before receivable is booked
```

This is why firms hedge forecast transactions subject to policy/accounting/legal constraints.

## 42. Hedge accounting boundary

Accounting treatment can materially affect reported earnings volatility, documentation and designation requirements.

This case focuses on economic risk mechanics, not jurisdiction-specific hedge-accounting rules.

If used professionally, current accounting standards and company policy must be checked separately.

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

## 44. Case output

Create:

```text
exporter_exposure_map.md
exporter_cashflow_timeline.md
layered_hedge_policy.md
scenario_matrix.md
hedge_attribution_report.md
counterparty_maturity_dashboard.md
```

## 45. Review questions

You should be able to explain:

1. Why exporter is economically long USD.
2. Why forward loss can coincide with successful hedge.
3. Why forecast error creates over-hedge risk.
4. Why natural hedges should be netted before derivatives.
5. Why forward points are not simply a fee.
6. Why options change payoff shape rather than eliminate cost.
7. Why 90-day hedge does not remove long-term competitiveness exposure.

## Internal links

- [Funding, NDF, basis and forward curve](../90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md)
- [Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
- [FX options and hedging](../14_FX_OPTIONS_VOLATILITY_AND_HEDGING.md)
