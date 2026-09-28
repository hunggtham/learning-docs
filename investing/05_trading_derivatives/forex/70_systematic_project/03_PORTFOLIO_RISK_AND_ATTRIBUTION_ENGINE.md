# 03 — Portfolio Risk và Attribution Engine cho Systematic FX

Một strategy có thể đúng ở từng trade nhưng portfolio vẫn nguy hiểm nếu nhiều position thực chất là cùng một factor bet. Module này xây layer biến **tickets → currency legs → factor exposures → portfolio risk → P/L attribution**.

Mục tiêu là để hệ thống trả lời được hai câu hỏi khác nhau:

```text
What risks are we carrying now?
Why did the portfolio make or lose money?
```

Nếu không answer được cả hai, risk management và research feedback loop đều thiếu.

## 1. Ticket không phải true exposure

Ví dụ:

```text
Long EUR/USD
Long GBP/USD
Short USD/JPY
```

Ba tickets nhưng decomposition:

```text
+EUR -USD
+GBP -USD
-USD +JPY
```

USD short factor xuất hiện ba lần.

Risk engine phải aggregate legs thay vì chỉ đếm positions.

## 2. Canonical currency-leg representation

Mỗi FX position `A/B` có thể biểu diễn:

```text
Long A/B  → +A, -B
Short A/B → -A, +B
```

Scale legs theo notional và current price để có comparable reporting currency exposure.

## 3. Reporting currency

Chọn một reporting currency, ví dụ USD hoặc KRW.

Mọi exposure/P&L phải có:

```text
native currency
reporting currency
conversion timestamp
conversion rate source
```

Không overwrite native amount sau conversion; giữ cả hai để audit.

## 4. Gross và net exposure

Tính:

```text
Gross Exposure = Σ absolute economic exposures
Net Currency Exposure = sum of signed legs by currency
```

Net nhỏ không đồng nghĩa risk nhỏ vì gross exposure vẫn tạo:

```text
liquidity risk
margin usage
basis risk
execution cost
```

## 5. Gross leverage

```text
Gross Leverage = Σ|notional_i| / Equity
```

Track distribution theo thời gian:

```text
median
95th percentile
maximum
```

Một end-of-day snapshot có thể bỏ lỡ intraday leverage spikes.

## 6. Net leverage không đủ

Hai opposing positions có thể giảm net directional exposure nhưng vẫn có:

```text
cross risk
basis risk
financing
spread/slippage
```

Risk dashboard nên show cả gross và net.

## 7. Factor buckets

Ngoài currency legs, map positions vào factors tùy strategy:

```text
Broad USD
Rate differential
Carry
Risk sentiment
Commodity beta
China/global-growth beta
Funding currency
Volatility
```

Factor mapping có thể model-based hoặc heuristic, nhưng phải versioned.

## 8. Factor loading is conditional

EUR/USD sensitivity to yields không cố định.

Do đó factor beta nên có:

```text
estimation window
regime label
confidence / error
```

Không trình bày estimated beta như physical constant.

## 9. Currency exposure table

Output ví dụ:

```text
Currency | Long Equivalent | Short Equivalent | Net | Stress Loss
EUR
USD
JPY
GBP
AUD
KRW
```

Rows phải derive từ positions, không manual spreadsheet nếu system có thể calculate.

## 10. Pair correlation vs currency-factor overlap

Correlation giữa EUR/USD và GBP/USD có thể thay đổi.

Nhưng cả hai structurally contain USD leg.

Factor decomposition cung cấp information mà sample correlation có thể bỏ lỡ.

## 11. Covariance matrix

Với return vector `r` và weights `w`:

```text
Portfolio Variance = w' Σ w
```

Useful nhưng phụ thuộc sample.

Store covariance model version và estimation period.

## 12. Stress correlation

Normal correlation thường underestimate crisis clustering.

Compute separately nếu data đủ:

```text
normal regime correlation
high-volatility correlation
downside correlation
funding-stress correlation
```

Do not assume one covariance matrix describes all states.

## 13. Volatility targeting

Target risk example:

```text
Position Risk Budget
= Target Volatility / Estimated Instrument Volatility
```

Nhưng cap size bằng liquidity/margin constraints.

Vol targeting without leverage cap can increase exposure dramatically in calm regime just before volatility jumps.

## 14. Risk contribution

Approximate marginal/component risk giúp biết position nào đóng góp portfolio volatility.

Mục tiêu:

```text
Portfolio weight
≠ Portfolio risk contribution
```

A small position can dominate risk if volatility/correlation high.

## 15. Planned loss vs statistical risk

Trade stop-based risk:

```text
planned loss if stop executes normally
```

Statistical risk:

```text
distribution-based loss estimate
```

Stress risk:

```text
loss under specified extreme scenario
```

Store all three; none replaces the others.

## 16. Portfolio heat

Define one practical metric:

```text
Portfolio Heat = Σ planned stop losses
```

Then enhance with cluster stress:

```text
Correlated Heat = stressed loss if common factor moves and slippage widens
```

Naive heat ignores shared USD/carry factor.

## 17. Scenario engine

Scenario object:

```text
scenario_id
currency shocks
rate shocks
volatility shock
spread multiplier
slippage multiplier
margin-policy shock
notes
```

Apply same scenarios across historical experiments for comparability.

## 18. Deterministic shock examples

```text
USD +5% broad
JPY +8% funding unwind
Oil +20%
US 2Y +100 bp
Risk-off + spread 3x
KRW -10% vs USD
```

Scenarios are not forecasts. They test survivability.

## 19. Combined scenario

Crisis rarely moves one variable.

Example:

```text
USD +4%
JPY +6%
Gold -5% initially
FX spreads 4x
Margin requirement +50%
```

Combined scenario often reveals hidden fragility.

## 20. Reverse stress test

Instead of choosing shock first, solve:

```text
What combination causes:
-10% equity
margin level < threshold
or forced liquidation?
```

Reverse stress identifies failure boundary.

## 21. VaR

VaR can answer:

```text
Under model assumptions,
what loss threshold corresponds to confidence level X?
```

It cannot answer maximum possible loss.

Store model/method:

```text
historical
parametric
Monte Carlo
```

## 22. Expected Shortfall

Expected Shortfall estimates average loss beyond VaR threshold.

Still depends on data/model and may underestimate regime breaks absent from sample.

Use alongside scenario tests.

## 23. Tail events outside sample

CHF 2015-style discontinuity demonstrates:

```text
Historical distribution
may exclude relevant future regime break
```

Risk engine needs explicit jump scenarios not just empirical quantiles.

## 24. Margin stress

For each scenario compute:

```text
Equity
Used Margin
Free Margin
Margin Level
Gross Leverage
Positions liquidated under policy
```

Price risk and margin risk must be simulated together.

## 25. Dynamic margin policy

Provider may raise margin during stress.

Scenario:

```text
Margin requirement × 2
without price move
```

can still force deleveraging.

## 26. Liquidity stress

Add:

```text
spread multiplier
slippage multiplier
max executable size reduction
```

A position may be small in notional but hard to exit in stressed market.

## 27. Concentration limits

Possible limits:

```text
max instrument notional
max currency net exposure
max factor exposure
max gross leverage
max planned portfolio heat
max stressed loss
max margin utilization
```

Limits should be strategy/account specific, not universal percentages.

## 28. Pre-trade risk check

Before order:

```text
Current portfolio
+ proposed fill
→ projected exposures
→ projected margin
→ projected stress loss
```

Reject if limits breached.

Do not check only position after fill.

## 29. Post-fill check

Actual fill may differ from requested size/price.

Recompute risk using filled quantity immediately.

Partial fill changes hedge ratio.

## 30. Hedge representation

A hedge must have target:

```text
hedged factor
hedge instrument
hedge ratio
expected basis risk
carry cost
liquidity
```

Do not label position “hedged” as boolean only.

## 31. Hedge effectiveness

Measure:

```text
Reduction in targeted exposure
Reduction in stress loss
Cost introduced
Residual basis risk
```

A hedge can reduce variance while increasing negative carry.

## 32. P/L attribution architecture

Portfolio P/L should decompose:

```text
price / spot move
carry / financing
spread
commission
slippage
currency conversion
hedge P/L
other fees
```

Then aggregate by:

```text
strategy
instrument
currency
factor
session
event/regime
```

## 33. Gross vs net alpha

Define:

```text
Gross Signal P/L
- implementation costs
- financing
= Net Strategy P/L
```

Research should not call gross paper return “alpha”.

## 34. Factor attribution

If portfolio gains because broad USD moves, but strategy thesis was pair-specific value:

```text
factor attribution reveals mismatch
```

This is crucial for learning whether edge came from intended mechanism.

## 35. Benchmark attribution

Possible benchmarks:

```text
zero exposure
simple carry basket
broad USD factor
risk-parity FX basket
```

Benchmark depends on strategy objective.

Do not choose benchmark after seeing performance.

## 36. R-multiple attribution

At trade level:

```text
Realized R = Net P/L / Planned Initial Risk
```

Also store:

```text
Gross R
Cost R
Slippage R
```

This normalizes trades of different sizes.

## 37. MAE/MFE

Store:

```text
Maximum Adverse Excursion
Maximum Favorable Excursion
```

relative to entry and planned R.

Useful for exit research but vulnerable to hindsight overfitting if repeatedly optimized.

## 38. Drawdown attribution

When portfolio hits drawdown, identify:

```text
which strategies
which currencies
which factors
which cost components
```

contributed.

Do not treat drawdown as one number only.

## 39. Correlated losing clusters

Detect periods where multiple strategies lose simultaneously.

This may reveal:

```text
shared hidden factor
regime dependence
liquidity shock
```

Portfolio of strategies is not diversified merely because strategy names differ.

## 40. Risk-adjusted metrics

Can report:

```text
Sharpe
Sortino
Calmar
Max Drawdown
Expected Shortfall
```

but always alongside leverage, liquidity and tail scenarios.

## 41. Turnover and capacity

Track:

```text
turnover
average ticket size
size relative to liquidity proxy
```

A scalable strategy should not assume unlimited execution at top-of-book.

## 42. Exposure by session

Risk may cluster around:

```text
Asia
London
New York
rollover
macro-event windows
```

Report exposure before major scheduled events.

## 43. Event risk inventory

At any time system can list:

```text
positions
next known central-bank event
next macro release
weekend holding
```

This supports event-specific limits.

## 44. Strategy virtual books

If broker nets positions but multiple strategies share pair, maintain internal virtual books:

```text
strategy_A +50k EUR/USD
strategy_B -20k EUR/USD
broker net +30k
```

Attribution remains possible.

## 45. Allocation of execution cost

When orders are netted, need rule to allocate savings/costs among strategies.

Possible:

```text
pro rata by requested quantity
```

Document consistently.

## 46. Allocation of financing

Financing charged to net broker position may differ from sum of virtual strategy positions.

Define attribution policy; otherwise strategy-level P/L won't reconcile to account P/L.

## 47. Reconciliation invariant

At end of period:

```text
Σ strategy attributed P/L
+ unallocated account adjustments
= account P/L
```

Difference must be zero within rounding tolerance.

## 48. Risk snapshot schema

Example:

```text
snapshot_time
account_equity
gross_leverage
used_margin
free_margin
currency_exposures_json
factor_exposures_json
planned_heat
stress_loss_base
stress_loss_severe
```

Store snapshots for later review.

## 49. Scenario result schema

```text
scenario_id
snapshot_time
projected_pnl
projected_equity
projected_margin_level
largest_loss_factor
liquidation_flag
```

## 50. Attribution record schema

```text
trade_id
strategy_id
instrument
spot_pnl
carry_pnl
spread_cost
commission
slippage_cost
conversion_effect
net_pnl
factor_tags
```

## 51. Unit tests — decomposition

Example:

```text
Long 100k EUR/USD
```

must produce:

```text
+100k EUR economic leg
negative USD leg equal to quote value
```

within defined valuation convention.

## 52. Unit tests — aggregation

Long EUR/USD + long GBP/USD should show larger negative USD aggregate than either trade alone.

## 53. Unit tests — P/L reconciliation

For known fills and costs:

```text
Gross P/L - costs = Net P/L
```

and sum of strategy attribution equals account ledger.

## 54. Stress regression tests

Keep fixed scenarios so code changes don't silently alter risk calculation.

Example expected outputs can use tolerance ranges.

## 55. Model change governance

If risk model changes:

```text
risk_model_version++
```

Do not overwrite historical risk snapshots with new methodology without label.

## 56. Completion criteria

Reviewer should be able to answer:

```text
Which currencies are we truly long/short?
Which common factors dominate risk?
What loss occurs under severe scenario?
Will margin force liquidation first?
Where did yesterday's P/L actually come from?
Did intended edge or unintended beta generate return?
```

## Deliverables

Create:

```text
currency_exposure_spec.md
factor_model_spec.md
risk_limits.md
stress_scenarios.md
portfolio_risk_report.md
pnl_attribution_spec.md
attribution_report.md
reconciliation_tests.md
```

## Đọc tiếp

→ [04 — Forward Test, Monitoring và Kill Switch](./04_FORWARD_TEST_MONITORING_AND_KILL_SWITCH.md)

Liên quan:

- [11 — Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
- [12 — Journal, review and attribution](../12_TRADING_JOURNAL_REVIEW_AND_PERFORMANCE_ATTRIBUTION.md)
- [03 — Leverage, margin and position sizing](../03_LEVERAGE_MARGIN_POSITION_SIZING.md)
