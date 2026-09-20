# 03 — Execution, Market Microstructure và Trading Portfolio

> Signal tốt chưa đủ. Một strategy chỉ tạo được live edge khi order đi qua market với friction thấp, sizing đúng, operational state chính xác và portfolio risk được quản lý ở cấp toàn book. Chapter này đi từ limit order book, spread và market impact tới execution algorithms, TCA, margin stress, factor aggregation và production safety.

## 1. Trading System có ba lớp

Một trading system tối thiểu gồm **signal generation**, **risk sizing** và **execution**.

Nếu signal expectancy là +0,12R nhưng all-in spread/commission/slippage = 0,10R, edge gần như biến mất. Execution vì vậy không phải hậu cần; nó là một phần của strategy economics.

## 2. Decision Price và Execution Price

Decision price là price khi strategy quyết định trade. Execution price là realized fill.

Khoảng cách giữa hai mức gồm latency, spread, impact, missed fills và market movement. Tracking gap này là nền tảng của **implementation shortfall**.

# Phần I — Limit Order Book và Order Types

## 3. Limit Order Book

Order book chứa resting bids/asks theo price level. Best bid là buy cao nhất; best ask là sell thấp nhất; spread là distance giữa chúng.

Depth cho biết quantity available beyond top of book. Spread hẹp với depth mỏng vẫn có thể tạo large slippage.

## 4. Price-Time Priority

Nhiều venues ưu tiên better price trước, rồi earlier time ở same price.

Backtest “touch limit = filled” thường optimistic vì queue position có thể rất xa phía sau.

## 5. Queue Position

Fill probability phụ thuộc volume ahead, cancellations, incoming market orders và venue rules.

For short-horizon passive strategies, queue modeling có thể quan trọng ngang signal.

## 6. Maker và Taker

Maker provides resting liquidity; taker consumes it.

Maker may save spread/fee nhưng faces non-fill/adverse selection. Taker gets immediacy nhưng pays spread/impact. Optimal choice depends urgency and edge decay.

## 7. Market Order

Market order ưu tiên fill certainty, không price certainty.

Appropriate khi urgency/risk exit cao nhưng dangerous trong thin book hoặc news gap.

## 8. Marketable Limit

Marketable limit crosses spread nhưng caps worst acceptable price.

It reduces extreme slippage risk but can partially fill/miss during fast move.

## 9. Passive Limit

Passive limit controls price but exposes opportunity cost and adverse selection.

If order fills mostly when price is about to continue against you, apparent spread saving is illusory.

## 10. Stop Order

Stop triggers order after threshold. Trigger price is not guaranteed fill price.

Gap/limit move can turn planned -1R into much larger realized loss.

## 11. Stop-Limit

Stop-limit controls maximum acceptable execution price but can fail to exit entirely.

Emergency protection often values certainty over exact price; stop-limit is not automatically safer.

## 12. IOC, FOK và Time-in-Force

**Immediate-or-Cancel (IOC)** executes available quantity then cancels remainder. **Fill-or-Kill (FOK)** requires full immediate fill. **Good-Til-Cancelled (GTC)** remains active under broker/venue rules.

Time-in-force is part of execution logic, not UI detail.

## 13. Partial Fills

Partial fills alter actual position risk and can break hedge ratios or multi-leg trades.

Execution engine must track remaining quantity and reconcile actual fills before submitting replacements.

## 14. Multi-Leg Execution

Spread/option pairs may be executed as package or legged separately.

Legging creates **legging risk**: first leg fills, second moves away. Package order reduces this but may sacrifice fill probability/liquidity.

# Phần II — Spread, Liquidity và Price Discovery

## 15. Spread Compensation

Spread compensates liquidity provider for adverse selection, inventory risk, volatility, venue fees and capital use.

Spread widens when information uncertainty rises.

## 16. Quoted Spread vs Effective Spread

Quoted spread is displayed bid-ask. Effective spread measures actual fill relative midpoint/benchmark.

Price improvement or hidden liquidity can make effective spread smaller than quote; fast moves can make it larger.

## 17. Realized Spread

Market maker may earn quoted spread but lose if price moves against fill immediately.

**Realized spread** measured after short horizon helps separate earned spread from adverse selection.

## 18. Depth

Liquidity is multi-dimensional: spread, depth, resilience and market impact.

A market with narrow spread but tiny depth may be poor for large order.

## 19. Order-Book Imbalance

Displayed bid/ask imbalance can contain short-term information but is noisy and manipulable by cancellations.

Use as context, not deterministic predictor.

## 20. Hidden / Iceberg Liquidity

Some orders show only partial size. Visible depth therefore underestimates actual liquidity in some venues.

Conversely displayed liquidity may vanish instantly, so book snapshot is not guarantee.

## 21. Dark Pools và Off-Exchange Venues

Dark venues allow trading without displaying full pre-trade interest, potentially reducing signaling for institutional orders.

They complicate consolidated price discovery and venue analysis.

## 22. Venue Fragmentation

Same security can trade across exchanges/ATSs. Best route depends price, fee, queue, latency and fill probability.

Broker routing policy can materially affect retail execution quality.

## 23. Price Discovery

Price discovery is process by which new information moves quotes/trades. It may occur first in futures, ETF, options, FX or underlying cash depending market hours/liquidity.

Understanding lead market helps avoid treating stale reference price as fair value.

# Phần III — Auctions và Intraday Structure

## 24. Opening Auction

Open consolidates overnight information and queued orders. Price formation differs continuous market.

Backtest entering “at open” must model auction access and gaps realistically.

## 25. Closing Auction

Close attracts benchmark/index/fund flows. Volume may be huge and technically driven.

Official close is not automatically freely executable unless strategy participates correctly.

## 26. Imbalance Information

Some exchanges publish auction imbalance indicators. They can forecast closing pressure but also change as orders enter/cancel.

Use timing rules exactly; data availability matters in backtest.

## 27. Intraday Seasonality

Volume/volatility often U-shaped in equities; FX follows regional sessions; futures react around scheduled macro events.

Execution assumptions should depend time-of-day.

## 28. Rollover / Fixing Windows

FX fixes, futures settlement windows and index rebalances can create temporary flow concentration.

Short-term strategies need separate cost model for these windows.

# Phần IV — Slippage và Market Impact

## 29. Slippage

Slippage is difference between expected and realized execution. It depends volatility, urgency, size/depth, latency and order type.

Do not model slippage as constant if trading across regimes.

## 30. Implementation Shortfall

Implementation shortfall measures difference between hypothetical portfolio at decision price and actual outcome after execution.

It includes explicit cost, spread, delay, market impact and opportunity cost.

## 31. Opportunity Cost

An unfilled passive order can miss a profitable move. Zero commission/slippage does not mean zero execution cost.

Missed opportunity must be included in strategy economics.

## 32. Market Impact

Own order can move market. Impact grows with size relative to available volume and urgency.

Strategy capacity is limited by impact, not account balance alone.

## 33. Temporary vs Permanent Impact

Temporary impact may revert after execution; permanent impact reflects information/signaling incorporated into fair price.

Execution algorithms aim reduce unnecessary temporary/signaling cost.

## 34. Participation Rate

Participation = own traded volume / market volume during execution.

Higher participation increases speed but generally increases impact/signaling risk.

## 35. Square-Root Impact Intuition

Empirically, impact often grows sublinearly/nonlinearly with order size relative volume and volatility; exact model varies.

Main lesson: doubling order size does not necessarily double cost predictably, and large orders can become disproportionately expensive.

## 36. Capacity

Capacity asks how much capital strategy can deploy before execution erodes edge.

Estimate average daily volume, participation rate, turnover, holding period and exit stress.

# Phần V — Execution Algorithms

## 37. TWAP

TWAP slices order roughly evenly through time.

Simple but ignores varying liquidity; may overtrade quiet periods.

## 38. VWAP

VWAP schedules according expected/realized volume profile.

Useful benchmark-following execution, but benchmark beating does not guarantee good investment decision.

## 39. POV

Percentage-of-Volume trades fixed share of market volume.

Adaptive to activity but can trade more exactly when volatility/volume spike.

## 40. Implementation-Shortfall Algorithm

IS algos optimize trade-off between market impact and price-risk from waiting.

High urgency front-loads execution; low urgency waits more for liquidity.

## 41. Arrival-Price Benchmark

Arrival price captures market when execution decision starts and is often appropriate for alpha-decay strategies.

Benchmark must match economic decision, not chosen after results.

## 42. Passive / Opportunistic Execution

Some algorithms wait for favorable spread/liquidity conditions while respecting completion target.

They can improve cost but increase non-fill/opportunity risk.

## 43. Smart Order Routing

SOR routes among venues based price, queue, fee/rebate and fill probability.

Best displayed quote is not always best realized execution once fees/latency considered.

# Phần VI — Adverse Selection và Information

## 44. Adverse Selection

Fill quality can be bad because other side trades when information favors them.

Passive orders especially vulnerable around news or informed flow.

## 45. Toxic Flow

Liquidity providers call flow “toxic” when counterparties systematically trade before adverse price moves.

Retail should interpret this as information/timing issue, not conspiracy.

## 46. Liquidity Sweep

Prior highs/lows cluster stops/breakout orders. Triggering them creates market-order burst.

If opposing liquidity absorbs burst, reversal can occur. Order clustering alone can explain much of “stop hunt” behavior.

## 47. Spoofing vs Normal Cancellation

Displayed orders can be canceled for legitimate reasons; spoofing is manipulative conduct under market rules.

Do not infer manipulation merely because visible depth disappears.

# Phần VII — News, Gaps và Market Controls

## 48. News Execution

CPI, NFP, FOMC, earnings and geopolitics can widen spread and reduce depth.

A strategy not designed for event conditions should model avoidance/reduced size rather than normal fills.

## 49. Gap Risk

Cash equities gap across sessions; derivatives can jump through stop levels despite extended hours.

Sizing must account discontinuous moves.

## 50. Circuit Breakers

Halts can stop immediate trading but do not erase risk. Reopen may gap further.

A stop is useless while market closed/halted.

## 51. Price Limits

Daily limits can trap positions with no opposite liquidity. This is particularly relevant in some Asian/commodity markets.

Position sizing must include multi-session exit scenario.

## 52. Liquidation Cascades

Leveraged forced selling can create feedback:

```text
Price ↓ → Margin Breach → Forced Sell → Price ↓ further
```

Crypto/futures/CFD markets can exhibit strong liquidation-driven overshoot.

# Phần VIII — Latency và Systems

## 53. Latency

Latency matters only relative strategy horizon. For swing trader, 200 ms irrelevant; for sub-second arbitrage, fatal.

Choose edge matching infrastructure.

## 54. Clock Synchronization

Market data, signal, order and fill timestamps need synchronized clocks.

Otherwise live-vs-backtest attribution and sequencing become unreliable.

## 55. Market Data Quality

Stale quotes, dropped packets, bad ticks or wrong corporate adjustments can generate false signals/orders.

Production system needs validation and fallback behavior.

## 56. Broker/API State

Order submission acknowledgement is not same as fill. Network timeout can leave unknown state.

Always query broker state before retrying.

## 57. Idempotency

Client order IDs/idempotent workflow prevent duplicate orders after retry.

This is basic production safety, not software luxury.

## 58. Reconciliation

Internal positions/cash/open orders must reconcile with broker after disconnect/restart.

Broker/exchange state is source of truth for actual exposure.

## 59. Order Reject Handling

Reject reasons include margin, symbol status, price band, invalid quantity or market closed.

System must define action for each category instead of assuming order exists.

## 60. Kill Switch

Predefine halt conditions: bad market data, duplicate orders, abnormal spread, broker outage, daily loss or risk-limit breach.

Kill switch protects operational survival.

# Phần IX — Trading Portfolio

## 61. Portfolio Heat

Portfolio heat aggregates planned stop losses but should adjust correlation/common factors.

Five 0.5% trades all short USD are not independent 2.5% heat in economic sense; they may fail together.

## 62. Net vs Gross Exposure

Long-short book may have net beta near zero but gross leverage high.

Gross drives funding, turnover, liquidity and gap risk. Monitor both.

## 63. Factor Exposure

Map trades to USD, rates, equity beta, growth, commodity, volatility, country and liquidity factors.

This reveals hidden concentration better than pairwise correlation alone.

## 64. Delta-Equivalent Exposure

Options positions need delta-equivalent plus Gamma/Vega. Small premium can create large state-dependent exposure.

Do not aggregate option book by premium paid.

## 65. DV01 / Rate Exposure

Rates/fixed-income trades should aggregate DV01 and key-rate DV01.

Notional netting can hide curve bets.

## 66. Volatility Exposure

Short options, carry strategies and certain mean-reversion systems may all be short volatility even if instruments differ.

Vol factor should be explicit portfolio bucket.

## 67. Liquidity Factor

Small caps, high-yield credit, altcoins and crowded futures may all become illiquid simultaneously in stress.

Liquidity correlation often rises when funding tightens.

## 68. Correlation Instability

Historical correlations change by regime and increase during deleveraging.

Use scenario correlations, not only sample covariance.

## 69. Volatility Targeting

Scale positions to stabilize expected risk, but beware procyclicality: low vol can encourage leverage before shock, high vol forces deleverage after selloff.

Apply caps/floors and stress overlays.

## 70. Risk Parity across Trades

Equalizing volatility contribution can prevent one market dominating, but equal vol ≠ equal tail risk.

Adjust for gaps, liquidity and nonlinearity.

## 71. VaR

VaR estimates loss threshold at confidence level under model.

It does not describe losses beyond threshold and is weak for unseen jumps.

## 72. Expected Shortfall

Expected Shortfall averages tail losses beyond VaR threshold.

Better tail metric, but still depends data/model. Scenario stress remains mandatory.

## 73. Drawdown Control

Risk reduction rules should be defined before drawdown and based on strategy distribution.

They are safeguards against model/operational deterioration, not emotional response.

## 74. Recovery Math

-10% needs +11.1%; -50% needs +100%.

Deep drawdown damages geometric compounding nonlinearly.

## 75. Pyramiding

Adding to winners can exploit trends, but total stop risk after each add must stay within budget.

Independent sizing of each add creates hidden leverage.

## 76. Averaging Down

Averaging down can be valid only if pre-specified strategy with total risk cap.

Unplanned adding to avoid realizing loss is behavior, not system.

# Phần X — TCA và Learning Loop

## 77. MAE / MFE

Maximum Adverse/Favorable Excursion helps study intratrade path.

Use for diagnosis, not direct same-sample stop optimization without OOS validation.

## 78. Execution Attribution

Break performance gap into signal timing, size, spread, commissions, slippage, missed fills, market impact and discretionary intervention.

Fix the correct layer.

## 79. Transaction Cost Analysis

TCA segments fills by benchmark, venue, order type, size, time, volatility and liquidity.

Goal is systematic detection of leakage.

## 80. Realized vs Expected Cost

Cost model should produce expected spread/slippage. Live realized distribution should be compared regularly.

Persistent deterioration can signal crowding, capacity problem or broker/market change.

## 81. Fill Probability

For passive strategies, track probability of fill conditional on signal quality.

A strategy can look strong on filled trades while ignoring profitable signals that never filled.

## 82. Adverse-Selection Score

Measure price movement shortly after fill. Persistent negative post-fill move suggests passive execution is being selected adversely.

This can guide urgency/order-type changes.

## 83. Capacity Monitoring

As AUM grows, cost should be analyzed vs participation rate and order size percentile.

Scale slowly and verify realized impact remains within model.

## 84. Pre-Trade Checklist

```text
Signal valid?
Position size?
Factor overlap?
Liquidity / spread?
Event risk?
Order type / urgency?
Max slippage?
Margin buffer?
Exit logic?
Portfolio heat?
```

## 85. Post-Trade Checklist

Record decision price, fills, spread/slippage, benchmark, MAE/MFE, market state, rule adherence and operational anomalies.

Data discipline lets execution skill compound.

## 86. Mental Model cuối cùng

```text
Signal
→ Urgency
→ Order Type
→ Venue / Liquidity
→ Fill / Slippage / Impact
→ Position + Factor Aggregation
→ Margin / Tail Stress
→ TCA / Reconciliation
→ Process Improvement
```

Trading edge only exists after costs and operational reality. Market microstructure is the bridge between a theoretical strategy and actual money.