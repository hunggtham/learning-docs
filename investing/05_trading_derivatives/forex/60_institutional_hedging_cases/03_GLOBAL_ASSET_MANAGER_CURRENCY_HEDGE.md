# Trường hợp (case / 사례) 03 — toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio

> **Mạch đọc:** Đặt **trường hợp (case / 사례) 03 — toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Unhedged foreign asset** sang **2. Return decomposition**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một investor Hàn Quốc có thể nắm US equities, European bonds hoặc toàn cục (global / 전역) multi-asset portfolio. Khi reporting currency là KRW, total return không chỉ đến từ cục bộ (local / 로컬) asset. Nó còn đến từ FX.

Mô hình tư duy (mental model / 사고 모델):

```text
Local Asset Return
+ Currency Return
+ Hedge P/L
+ Hedge Carry / Forward Points
- Transaction Cost
= Investor Return in Reporting Currency
```

Currency hedge vì vậy không đơn giản là “xóa FX”. Nó thay đổi phân phối (distribution / 분포), carry, benchmark tracking và liquidity requirements của portfolio.

## 1. Unhedged foreign asset

Giả sử Korean fund đầu tư:

```text
USD asset value = 100m USD
Reporting currency = KRW
USD/KRW spot = 1,360
```

Initial KRW giá trị (value / 값):

```text
136bn KRW
```

Portfolio có hai main exposures:

```text
Underlying US asset
+ USD/KRW
```

## 2. Return decomposition

Approximate simple-return decomposition:

```text
KRW Return
≈ Local Asset Return
+ USD/KRW Return
+ interaction term
```

Chính xác (exact / 정확한) multiplicative relationship:

```text
(1 + R_KRW)
= (1 + R_USD_asset) × (1 + R_USD/KRW)
```

So:

```text
R_KRW
= R_asset + R_fx + R_asset × R_fx
```

## 3. Example unhedged

US asset rises 10% in USD.

KRW strengthens 8% against USD, meaning USD/KRW falls approximately 8%.

Approximate KRW return:

```text
1.10 × 0.92 - 1
≈ +1.2%
```

Cục bộ (local / 로컬) asset gained 10%, but currency nearly erased kết quả (result / 결과) for KRW investor.

## 4. Opposite scenario

US asset falls 5%, but USD strengthens 12% vs KRW:

```text
0.95 × 1.12 - 1
≈ +6.4%
```

Investor can gain in KRW despite cục bộ (local / 로컬) asset mất mát (loss / 손실).

This is why local-market hiệu năng (performance / 성능) is not investor return.

## 5. Full currency hedge concept

Fund can approximately hedge USD asset giá trị (value / 값) by:

```text
Sell USD forward
Buy KRW forward
```

notional close to USD exposure.

Goal:

```text
reduce sensitivity of KRW portfolio value to USD/KRW
```

## 6. Hedge ratio

Define:

```text
Hedge Ratio
= FX Hedge Notional / Foreign-Currency Asset Exposure
```

Examples:

```text
0%   unhedged
50%  partial hedge
100% fully hedged approximately
```

“100%” is still approximate because asset giá trị (value / 값) changes between rebalances.

## 7. Asset giá trị (value / 값) drift creates hedge mismatch

At start:

```text
Asset = 100m USD
Hedge = 100m USD
```

Asset rises 20%:

```text
Asset = 120m USD
Hedge remains = 100m USD
```

Now portfolio has residual:

```text
+20m USD unhedged
```

This is **hedge drift**.

## 8. Rebalancing hedge

Chính sách (policy / 정책) might rebalance:

```text
monthly
weekly
when hedge ratio leaves tolerance band
```

More frequent rebalancing reduces drift but increases turnover/chi phí (cost / 비용).

## 9. Hedge ratio is a strategic allocation quyết định (decision / 결정)

Choosing 0%, 50% or 100% changes portfolio rủi ro (risk / 위험) profile.

It should be based on:

```text
Investor liabilities
Strategic benchmark
Currency volatility
Asset-currency correlation
Carry/funding economics
Liquidity
Risk tolerance
```

not only short-term FX forecast.

## 10. Liability currency matters

A Korean pension with KRW liabilities may giá trị (value / 값) KRW stability more than a toàn cục (global / 전역) investor with USD liabilities.

Same foreign asset can have different optimal hedge chính sách (policy / 정책) depending on liabilities.

## 11. Bonds vs equities

Currency volatility can be large relative to bond volatility.

Example:

```text
Foreign bond expected volatility = low/moderate
FX volatility = comparable or larger
```

Unhedged currency can dominate bond portfolio rủi ro (risk / 위험).

For equities, cục bộ (local / 로컬) asset volatility is larger, so relative contribution differs.

## 12. Hedge carry

Forward hedge return includes forward points.

A Korean investor hedging USD back to KRW may face positive or negative carry depending on relative rates/basis.

Do not treat hedge return as simply `-spot FX return`.

## 13. Hedged return approximation

Conceptually:

```text
Hedged Portfolio Return
≈ Local Asset Return
+ Hedge Carry
+ Hedge Slippage/Basis Error
- Transaction Cost
```

Currency spot tác động (effect / 효과) is largely offset, not perfectly eliminated.

## 14. Forward points vs spot view

A 100% currency hedge can underperform unhedged portfolio when USD rises strongly.

That does not imply hedge failed.

The benchmark/mục tiêu (objective / 목표) determines evaluation.

## 15. Benchmark consistency

If fund benchmark is currency-hedged chỉ mục (index / 인덱스) but manager holds unhedged assets:

```text
manager has active currency risk
```

Even if asset selection matches benchmark.

Conversely, hedging a benchmark that is unhedged creates active FX position.

## 16. Active vs strategic currency position

Separate:

```text
Strategic hedge ratio
from
Tactical currency overlay
```

If manager changes hedge ratio based on FX view, that active quyết định (decision / 결정) should be attributed separately.

## 17. Currency overlay

A centralized overlay desk can manage currency exposure across multiple asset portfolios.

Benefits:

```text
netting
lower duplicate hedges
centralized risk
consistent execution
```

But it introduces quản trị (governance / 거버넌스) and attribution độ phức tạp (complexity / 복잡도).

## 18. Netting across portfolios

Portfolio A long USD 100m.

Portfolio B economically short USD 30m.

At firm mức (level / 수준):

```text
net USD exposure = 70m
```

Centralized hedge can reduce gross transactions if mandates allow.

## 19. Cross hedge

If direct hedge thị trường (market / 시장) is illiquid, manager may hedge with correlated currency.

Example conceptual:

```text
illiquid EM currency exposure
→ hedge partly with regional/broad USD proxy
```

This creates **basis rủi ro (risk / 위험)** because correlation is imperfect and regime-dependent.

## 20. NDF hedge

For non-deliverable/restricted currency exposure, NDF may be used.

Need mô hình (model / 모델):

```text
fixing source
settlement currency
onshore/offshore basis
capital-control/access constraints
```

NDF return can differ from onshore spot move.

## 21. Rolling forwards

If fund holds asset indefinitely but forward matures every 1–3 months:

```text
asset horizon = long
hedge tenor = short
```

Hedge must roll repeatedly.

Long-run kết quả (result / 결과) depends on chuỗi (sequence / 시퀀스) of forward points and roll thực thi (execution / 실행).

## 22. Roll rủi ro (risk / 위험)

At each maturity:

```text
close/mature old forward
open next forward
```

During stress:

```text
spread widens
basis moves
credit line tightens
liquidity declines
```

So hedge that reduced spot FX rủi ro (risk / 위험) can introduce funding/liquidity rủi ro (risk / 위험).

## 23. Collateral and variation margin

Depending instrument/CSA/clearing cấu trúc (structure / 구조), hedge can require collateral when marked against fund.

Important paradox:

```text
Underlying foreign asset may gain from FX move
while derivative loses and requires cash collateral now
```

Economic hedge can still create short-term liquidity need.

## 24. Example collateral mismatch

USD strengthens strongly.

For KRW investor with short USD forward:

```text
foreign asset KRW value rises
forward loses
```

If asset is not immediately liquid but derivative margin is due daily:

```text
liquidity mismatch
```

can matter even though combined net worth is protected.

## 25. Hedge ratio and liquidity buffer

A 100% hedge may require larger collateral buffer than 50% hedge.

Rủi ro (risk / 위험) chính sách (policy / 정책) should include:

```text
FX risk reduction
vs
liquidity requirement
```

not just volatility tối ưu hóa (optimization / 최적화).

## 26. Currency-asset correlation

If foreign asset tends to fall when USD rises, unhedged USD may provide diversification for KRW investor.

If hedge removes USD exposure, portfolio volatility could increase in some regimes.

Therefore:

```text
currency risk is not always pure uncompensated noise
```

Its tương tác (interaction / 상호작용) with asset return matters.

## 27. Correlation is not stable

A currency that hedged equity drawdowns historically may not do so next crisis.

Stress-test multiple correlation regimes.

## 28. Safe-haven currencies

JPY, CHF, USD can behave differently across crises depending funding and shock nguồn (source / 소스).

Do not hard-code “safe haven” into hedge chính sách (policy / 정책) without scenario phân tích (analysis / 분석).

## 29. Multi-currency portfolio

Portfolio:

```text
USD assets 50%
EUR assets 20%
JPY assets 10%
Other currencies 20%
```

Need currency exposure by underlying economic currency, not listing venue only.

A US-listed ETF can own non-USD assets.

## 30. Trading currency vs economic currency

Ticker trades in USD does not imply portfolio exposure is USD only.

For international equity ETF:

```text
Trading currency = USD
Underlying company revenues/assets = multiple currencies
```

Direct portfolio FX hedge usually targets fund NAV currency exposure according to fund mechanics, not every corporate revenue exposure inside holdings.

## 31. Look-through độ sâu (depth / 깊이)

Decide whether rủi ro (risk / 위험) hệ thống (system / 시스템) uses:

```text
fund share-class currency
fund NAV currency
underlying asset currency
company revenue currency
```

Each mức (level / 수준) answers different question.

Do not mix them.

## 32. Share-class hedge

Some funds offer currency-hedged share classes.

Investor must understand hedge typically targets share-class currency exposure, not all economic FX exposure of underlying companies.

## 33. Hedge effectiveness chỉ số (metric / 지표)

Measure difference between:

```text
Actual hedged portfolio return
vs
Ideal benchmark hedged return
```

Attribution:

```text
hedge ratio drift
forward points
transaction cost
roll timing
basis
cash flows
```

## 34. Cash inflow/outflow

Subscriptions/redemptions thay đổi (change / 변경) foreign asset exposure.

If hedge is not adjusted promptly:

```text
fund becomes over/under-hedged
```

Cash-flow forecasting matters.

## 35. thị trường (market / 시장) move between NAV and hedge thực thi (execution / 실행)

If NAV is measured at one cutoff but hedge rebalances later:

```text
timing basis
```

can create tracking lỗi (error / 오류).

## 36. Time-zone challenge

Toàn cục (global / 전역) assets close at different cục bộ (local / 로컬) times.

FX trades nearly 24/5.

Define consistent exposure snapshot and hedge-rebalance timestamp.

This is a point-in-time các hệ thống (systems / 시스템들) bài toán (problem / 문제).

## 37. Weekend gap

Foreign asset thị trường (market / 시장) may close while FX or another thị trường (market / 시장) reprices at different times.

Hedge and asset liquidity are not synchronized perfectly.

## 38. Stress scenario

Kiểm thử (test / 테스트):

```text
Global equities -25%
USD/KRW +15%
EUR/USD -10%
JPY strengthens 12%
FX spreads 3x
Forward basis widens
Collateral call increases
```

Calculate:

```text
Local asset P/L
FX P/L
Hedge P/L
Collateral requirement
Net portfolio P/L
Liquidity buffer
```

## 39. Partial hedge scenario

Compare 0%, 50%, 100% USD hedge across:

```text
USD +15%
USD unchanged
USD -15%
```

with cục bộ (local / 로컬) asset +10%/-10% combinations.

Observe that hedge ratio changes phân phối (distribution / 분포), not absolute “chất lượng (quality / 품질)”.

## 40. Strategic hedge quyết định (decision / 결정) khung phần mềm (framework / 프레임워크)

```text
Liability currency
Benchmark
Asset class volatility
Currency volatility
Asset-FX correlation
Carry
Liquidity/collateral
Operational capacity
Regulatory/tax/accounting constraints
```

No universal hedge ratio.

## 41. Attribution report

```text
Local asset return
FX spot contribution
Forward/carry contribution
Hedge ratio drift
Roll cost
Spread/slippage
Collateral/funding cost
Tactical overlay P/L
Net investor return
```

## 42. What not to learn

Wrong:

```text
100% hedge always lowers risk.
```

Wrong:

```text
If USD rises, currency hedge was a mistake.
```

Wrong:

```text
Fund traded in USD means USD is the only FX exposure.
```

Better:

```text
Currency hedge must be evaluated relative to liabilities,
benchmark, asset behavior, carry and liquidity constraints.
```

## 43. trường hợp (case / 사례) outputs

Create:

```text
asset_currency_exposure_map.md
hedge_ratio_policy.md
forward_roll_schedule.md
hedged_unhedged_scenario_matrix.md
collateral_liquidity_stress.md
currency_attribution_report.md
benchmark_tracking_report.md
```

## 44. rà soát (review / 검토) questions

Explain:

1. Why cục bộ (local / 로컬) asset return differs from KRW investor return.
2. Why 100% hedge drifts after asset price changes.
3. Why hedge carry belongs in return attribution.
4. Why a derivative mất mát (loss / 손실) can accompany successful hedge.
5. Why collateral creates liquidity rủi ro (risk / 위험) even for economically hedged portfolio.
6. Why benchmark currency treatment matters.
7. Why listing/trading currency is not always economic exposure.

## Nội bộ (internal / 내부) links

- [Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
- [Funding, NDF, basis and forward curve](../90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md)
- [Systematic risk and attribution engine](../70_systematic_project/03_PORTFOLIO_RISK_AND_ATTRIBUTION_ENGINE.md)

> **Bàn giao:** Sau **nội bộ (internal / 내부) links**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 KOREAN EXPORTER USD RECEIVABLE HEDGE](./01_KOREAN_EXPORTER_USD_RECEIVABLE_HEDGE.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
