# Case 02 — Korean Importer: Hedge USD Payables và Procurement Margin

Một Korean importer mua nguyên liệu/máy móc bằng USD nhưng bán sản phẩm hoặc thu doanh thu chủ yếu bằng KRW. Công ty có **economic short USD / long KRW exposure** trên khoản phải trả: nếu USD/KRW tăng, cùng một invoice USD cần nhiều KRW hơn để thanh toán.

Hedge objective là ổn định **KRW procurement cost**, không phải đánh cược rằng USD sẽ tăng hay giảm.

## 1. Exposure map

Giả sử:

```text
USD payable = 8,000,000 USD
Expected payment = 120 days
Functional currency = KRW
Current USD/KRW spot = 1,360
```

Unhedged KRW cost:

```text
KRW cost = USD 8m × future USD/KRW
```

Reference at current spot:

```text
8,000,000 × 1,360
= 10.88bn KRW
```

## 2. Directional risk

Importer bất lợi khi:

```text
USD/KRW rises
→ USD strengthens / KRW weakens
→ procurement cost in KRW rises
```

Economic exposure:

```text
Short USD
Long KRW
```

## 3. Unhedged scenarios

```text
USD/KRW 1,250 → 10.0bn KRW
USD/KRW 1,360 → 10.88bn KRW
USD/KRW 1,500 → 12.0bn KRW
```

Difference giữa 1,250 và 1,500 là 2.0bn KRW.

Nếu gross margin dự kiến chỉ vài tỷ KRW, currency move có thể thay đổi profitability của entire contract.

## 4. Forward hedge

Importer có thể:

```text
Buy USD forward
Sell KRW forward
```

Giả sử 4-month forward rate:

```text
USD/KRW forward = 1,370
```

Approximate locked KRW cost:

```text
8,000,000 × 1,370
= 10.96bn KRW
```

Ignoring transaction/credit details.

## 5. USD strengthens to 1,500

Underlying payable costs:

```text
8m × 1,500 = 12.0bn KRW
```

Forward approximate gain:

```text
(1,500 - 1,370) × 8m
= +1.04bn KRW
```

Combined cost:

```text
12.0bn - 1.04bn
≈ 10.96bn KRW
```

## 6. USD weakens to 1,250

Underlying payable costs:

```text
10.0bn KRW
```

Forward approximate loss:

```text
(1,370 - 1,250) × 8m
= 0.96bn KRW
```

Combined:

```text
10.0bn + 0.96bn
≈ 10.96bn KRW
```

Again, derivative loss can indicate hedge is working.

## 7. Procurement pricing connection

Suppose importer signs KRW sales contract today but USD supplier invoice is due in four months.

Without hedge:

```text
Sales price fixed in KRW
Input cost floating in USD/KRW
→ gross margin floats with FX
```

A forward can convert uncertain FX cost into known procurement cost, helping price the final product.

## 8. Natural hedge before derivatives

If importer also receives USD revenue:

```text
USD payable = 8m
USD revenue = 3m
```

Net USD need is approximately:

```text
5m USD
```

Buying 8m forward ignores natural offset.

## 9. Payment certainty

Purchase order may be:

```text
firm and non-cancelable
partially cancelable
volume-dependent
subject to shipping delay
```

Hedge ratio should reflect certainty.

A 100% forward against uncertain purchase can create long USD speculation if order is canceled.

## 10. Timing risk from shipment delay

Expected payment day 120 may move to day 150 because shipment/customs delay.

Forward matures day 120.

Treasury may need:

```text
FX swap / forward roll
```

The hedge direction was right, but tenor mismatched actual cash flow.

## 11. Early payment risk

Supplier may offer discount for payment day 90 instead of 120.

Hedge maturity no longer aligns.

Closing/rolling can create mark-to-market cash flows before operating transaction settles.

## 12. Layered purchase hedge

If yearly raw-material purchases are recurring:

```text
next quarter committed 90%
quarter +2 probable 60%
quarter +3 uncertain 30%
```

A layered hedge can reflect confidence by horizon.

## 13. Rolling hedge program

For continuous imports, treasury may maintain policy such as:

```text
Month 1–3: 80% hedged
Month 4–6: 50%
Month 7–12: 20%
```

Each month:

```text
new forecast enters horizon
existing hedges mature
forecast updates
hedge book is rebalanced
```

This is a process, not one trade.

## 14. Rolling creates path dependence

Weighted-average hedge rate depends on when layers were added.

Two companies with same final exposure can have different hedge portfolio rates because execution dates differ.

Do not judge result from one maturity snapshot only.

## 15. Forward points affect locked cost

Importer comparing spot 1,360 with forward 1,370 may say forward is “10 KRW more expensive”.

But forward points arise from relative rates/funding/basis, not merely broker markup.

Economic comparison is:

```text
Unhedged uncertain future cost
vs
known forward-locked cost
```

not `spot today vs forward` as if cash could be settled today for free.

## 16. Money-market hedge intuition

In simplified covered-interest-parity world, importer could conceptually:

```text
borrow KRW today
buy/invest USD today
use matured USD to pay supplier
```

Forward pricing should relate to this synthetic funding path.

This explains why rates enter forward rate.

## 17. Option hedge

Importer can buy protection against USD appreciation while keeping benefit if USD falls.

Conceptually:

```text
right to buy USD at protected rate
```

This costs option premium.

Useful when amount/timing is uncertain or company values favorable FX participation.

## 18. Why option can match uncertain exposure better

If purchase is canceled, a forward creates offsetting exposure that must be closed.

An option can simply expire unused, limiting downside to premium, depending on structure.

Therefore optionality can have value when underlying transaction itself is uncertain.

## 19. Premium is real budget cost

Option premium should be allocated into procurement economics.

Do not compare:

```text
Forward = free
Option = expensive
```

Forward has opportunity cost/locked payoff; option pays for asymmetry.

## 20. Collars and structured hedges

A collar can finance protection by giving up benefit beyond another rate.

But structured products may add barriers/leverage/conditional notional.

Treasury must model full payoff, especially under large USD move.

## 21. Supplier currency negotiation

Risk can be changed commercially before derivatives.

Possible contract choices:

```text
Pay supplier in KRW
Price-adjustment clause
Split currency invoice
Shorter price validity
```

Supplier will price its own FX risk into terms, so risk does not disappear—it is redistributed.

## 22. Inventory holding period

Even after supplier is paid, imported inventory may be sold months later.

If final selling price can adjust with FX, economic exposure differs from a fully fixed KRW sales contract.

Treasury needs business process map, not invoice list only.

## 23. Pass-through

If company can raise KRW selling prices after USD appreciation:

```text
FX cost shock
→ partially passed to customers
```

Then long-run economic exposure may be smaller than transaction exposure suggests.

But pass-through timing and competitive constraints matter.

## 24. Working-capital impact

USD appreciation can increase KRW working-capital requirement before customer pricing adjusts.

Even if long-run margins recover, short-term liquidity can tighten.

Hedge can protect liquidity timing as well as accounting margin.

## 25. Credit and FX interaction

If supplier requires margin/prepayment when market stress rises:

```text
USD strengthens
+ payment terms tighten
→ KRW liquidity need rises twice
```

FX hedge alone may not cover supplier-credit shock.

## 26. Counterparty concentration

If all forwards are with one bank:

```text
credit line / operational outage
```

can impair hedge program.

Large corporate treasury often tracks counterparty limits.

## 27. Settlement risk

Deliverable forward requires actual currency settlement.

Treasury must coordinate:

```text
bank account
value date
cutoff time
payment instruction
supplier settlement
```

A correctly priced hedge can fail operationally if payment process fails.

## 28. Cash-flow-at-risk view

Instead of focusing only on P/L, measure:

```text
KRW cash needed at payment date
```

under scenarios.

Hedge policy can target maximum acceptable cash-flow-at-risk.

## 29. Budget rate vs market rate

Business plan may assume:

```text
USD/KRW budget = 1,400
```

Treasury hedges at weighted 1,370.

This may create procurement margin buffer relative to budget, but it is not trading alpha.

Budget rate is internal decision benchmark.

## 30. Over-hedge example

Forecast import USD 8m.

Actual purchase only USD 5m.

Forward buy USD 8m remains.

Net after paying supplier:

```text
+3m USD excess
```

Treasury must sell excess USD, exposing company to closeout P/L.

## 31. Under-hedge example

Actual purchase becomes USD 10m while forward covers USD 8m.

Remaining:

```text
2m USD unhedged
```

If USD spikes, residual cost can still be material.

## 32. Forecast-quality feedback loop

Hedge effectiveness depends on procurement forecast quality.

Track:

```text
forecast vs actual amount
forecast vs actual payment date
```

Improving supply-chain forecast can reduce FX risk as much as changing derivative instrument.

## 33. Scenario matrix

Test:

```text
USD/KRW = 1,200 / 1,350 / 1,500 / 1,650
Purchase amount = 60% / 100% / 130% forecast
Payment delay = -30 / 0 / +30 days
```

Compute:

```text
Underlying KRW cost
Hedge P/L
Option premium if applicable
Roll cost
Over/under hedge
Total procurement cash cost
```

## 34. Stress — USD spike + purchase increase

This is worst combination:

```text
USD/KRW rises
and
actual import amount exceeds forecast
```

Residual unhedged amount faces high spot rate.

Risk management must stress volume and rate jointly.

## 35. Stress — order cancellation + USD spike

If purchase canceled but forward remains, company long USD via hedge.

USD spike may create gain, but that is accidental speculation after business exposure disappeared.

Policy should require prompt exposure/hedge reconciliation.

## 36. Hedge attribution

Review:

```text
Unhedged procurement FX effect
+ Forward/option P/L
+ Premium
+ Roll cost
+ Spread/fees
+ Forecast mismatch
= Hedged procurement result
```

## 37. Procurement hedge dashboard

```text
Supplier
Currency
Committed payable
Forecast payable
Natural offsets
Hedge notional
Hedge ratio
Maturity
Weighted hedge rate
Payment-date mismatch
Counterparty
Residual stress cost
```

## 38. What not to learn

Wrong:

```text
Importer should always buy USD early when USD looks cheap.
```

That is a market view, not hedge policy.

Wrong:

```text
Option is always safer than forward.
```

Options have premium, liquidity, valuation and structure risk.

Better:

```text
Instrument and hedge ratio must fit certainty, horizon,
cash-flow objective and residual-risk tolerance.
```

## 39. Case outputs

Create:

```text
importer_exposure_map.md
payment_timeline.md
layered_import_hedge_policy.md
procurement_scenario_matrix.md
cash_flow_at_risk_report.md
hedge_effectiveness_report.md
```

## 40. Review questions

You should explain:

1. Why importer is short USD economically.
2. Why natural USD revenue reduces derivative need.
3. Why delayed shipment creates roll risk.
4. Why option can be useful when purchase amount is uncertain.
5. Why forward points belong to funding economics.
6. Why procurement forecast accuracy is part of FX risk management.
7. Why combined underlying + hedge result matters more than derivative P/L.

## Internal links

- [Funding, NDF, basis and forward curve](../90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md)
- [Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
- [FX options and hedging](../14_FX_OPTIONS_VOLATILITY_AND_HEDGING.md)
