# 03 — Execution, Market Microstructure và Trading Portfolio

> Chương này tập trung vào phần thường chỉ được học sau khi đã giao dịch một thời gian: giá được khớp như thế nào, vì sao spread và liquidity thay đổi, tại sao một strategy có backtest tốt nhưng live kém, và cách quản trị nhiều vị thế như một portfolio thay vì từng lệnh độc lập.

## 1. Trading không kết thúc ở tín hiệu

Một strategy có thể tạo signal tốt nhưng vẫn fail nếu execution cost lớn hơn edge.

Trading system có ít nhất ba lớp: signal generation, risk sizing và execution. Backtest meaningful chỉ khi mô phỏng tương đối đúng cả ba.

## 2. Limit Order Book

Limit order book chứa resting buy/sell orders ở nhiều mức giá. Best bid là mua cao nhất, best ask là bán thấp nhất, spread là distance giữa hai mức.

Depth cho biết quantity available theo price levels. Spread hẹp nhưng depth mỏng vẫn có thể tạo slippage lớn.

## 3. Price-time priority

Nhiều venues ưu tiên price tốt hơn trước, rồi time priority ở cùng price.

Backtest giả định “price touch = full fill” thường overly optimistic nếu queue lớn. Queue position matters đặc biệt với futures/scalping.

## 4. Maker và taker

Limit order resting thường maker; market/marketable order taker.

Maker có thể pay lower fee nhưng chịu non-fill và adverse-selection risk. Taker chắc execution hơn nhưng trả spread/impact.

Execution quality không thể đánh giá chỉ bằng commission.

## 5. Market order

Market order ưu tiên fill, chấp nhận consume available depth.

Nó hợp lý khi urgency cao nhưng slippage unpredictable trong thin/fast market.

## 6. Marketable limit order

Marketable limit cho phép immediate execution nhưng đặt maximum acceptable price.

Nó giảm extreme-price risk nhưng có thể partially fill hoặc miss nếu market jumps beyond limit.

## 7. Passive limit order

Passive limit kiểm soát price nhưng không guarantee fill. Economic cost gồm opportunity cost và adverse selection.

Nếu bạn thường chỉ được fill trước unfavorable move, “saving spread” không thực sự là free gain.

## 8. Stop order

Stop converts to market/other order after trigger depending order type. Trigger price không guarantee execution price.

Gap qua stop tạo loss lớn hơn planned. Backtest cần model stop slippage.

## 9. Stop-limit

Stop-limit thêm price control sau trigger nhưng đổi lại risk không fill.

Emergency risk exits thường ưu tiên certainty of exit hơn exact price; stop-limit không phải luôn safer.

## 10. Partial fills

Order có thể fill từng phần. Partial fill thay risk profile, especially khi hedge leg hoặc multi-leg strategy involved.

Execution system phải biết remaining quantity và avoid duplicate orders.

## 11. Spread decomposition

Spread compensate market makers cho inventory risk, adverse selection, volatility, operational/venue costs và capital usage.

Khi information risk tăng trước news, spread thường widen vì liquidity provider sợ trading against informed flow.

## 12. Spread seasonality

Spread thay đổi theo session, open/close, rollover, holidays và macro events.

FX Asia session, London/NY overlap và equity auction periods có very different liquidity conditions.

Backtest dùng fixed spread dễ overstate edge.

## 13. Slippage

Slippage = actual execution minus decision/expected price.

Nó phụ thuộc volatility, order type, size/depth, latency và market state. Strategy stop ngắn cực nhạy với vài ticks slippage.

## 14. Implementation shortfall

Implementation shortfall so theoretical decision price với actual realized execution after delays, spread, slippage, commissions và missed fills.

Đây là metric tốt để quantify gap giữa signal edge và live edge.

## 15. Opportunity cost

Limit order không fill cũng có cost nếu signal subsequently moves favorable without you.

Execution analysis phải include both paid costs và missed-trade opportunity cost.

## 16. Market impact

Large order có thể move price against trader. Impact thường tăng nonlinear khi participation rate hoặc order size relative liquidity tăng.

Strategy capacity là maximum capital trước khi impact materially erodes edge.

## 17. Temporary vs permanent impact

Một phần impact may revert after execution; phần khác reflects information perceived by market and persists.

Execution algorithm aims reduce signaling/temporary impact, nhưng cannot eliminate informational impact.

## 18. Adverse selection

Adverse selection xảy ra khi fill probability increases in states that are bad for you.

Passive buy limit may fill mostly when sellers have new negative information. Fill rate high does not equal execution quality high.

## 19. Order-book imbalance

Bid/ask depth imbalance có thể correlate short-term move nhưng very noisy and gameable.

Use as context, not deterministic signal. Canceled orders mean displayed depth can disappear.

## 20. Hidden và iceberg liquidity

Not all liquidity is visible. Iceberg/hidden orders expose only part of true size depending venue rules.

Visible book therefore underestimates some liquidity, while spoof-like cancellations can overstate reliable liquidity.

## 21. Dark pools và off-exchange trading

Some markets route orders to dark/off-exchange venues to reduce displayed impact. This can improve large-order execution but also complicates price discovery and venue analysis.

Retail trader mainly needs understand consolidated volume may originate across multiple venues.

## 22. Venue fragmentation

Same security may trade across multiple exchanges/ATSs. Best displayed quote may depend routing and latency.

Smart-order routers try find best execution. Broker routing policy matters.

## 23. Opening auction

Equity open concentrates overnight information and large orders into auction price discovery.

Volatility can be high, spreads/order-book behavior differ from continuous trading. Backtest entering exactly at open must use realistic auction assumption.

## 24. Closing auction

Closing auction attracts index funds, benchmarks and institutional rebalancing. Volume can be large and price moves technical.

Strategies using close need understand whether fill assumed at official close is actually obtainable with correct order/auction participation.

## 25. Intraday seasonality

Volume/volatility often high at open/close and lower midday; FX follows global sessions.

A system profitable only in one liquidity window should not be extrapolated all day.

## 26. News execution

CPI, NFP, FOMC, earnings or geopolitics can widen spreads, reduce depth and create jumps.

Stop orders can slip; limit entries can miss or become adversely selected. If strategy not designed for event risk, reducing exposure can be rational.

## 27. Latency

Latency is delay from signal to venue/fill. For swing trading, 100 ms often irrelevant; for arbitrage/scalping, can erase edge.

Choose strategy consistent with infrastructure. Retail should not compete directly with HFT on latency-dependent edge.

## 28. Clock synchronization

Systematic execution requires accurate timestamps across market data, signal engine, broker and fills.

Clock drift can create false backtest/live attribution and order sequencing bugs.

## 29. Broker execution model

In OTC Forex/CFD, broker may internalize, hedge externally or mix models.

Marketing labels ECN/STP/market-maker are less useful than actual execution disclosure, conflicts, price source, slippage rules và legal entity.

## 30. Last look và quote rejection

Some OTC markets permit liquidity provider to reject stale quote under specified rules. This affects fill quality in fast markets.

Trader should understand broker's order handling rather than assume every displayed quote is firm.

## 31. TWAP

Time-Weighted Average Price algorithm slices order across time roughly evenly.

TWAP reduces immediate footprint but ignores actual volume pattern; can trade too much in quiet periods.

## 32. VWAP

Volume-Weighted Average Price algorithm schedules more volume when market historically/actually trades more.

VWAP is execution benchmark, not signal. Chasing VWAP mechanically can still create impact if participation too high.

## 33. POV

Percentage-of-Volume algorithm targets fraction of market volume.

It adapts to activity but can amplify trading during volatility spikes and reveals persistent participation if too mechanical.

## 34. Arrival price benchmark

Arrival price is market price when decision/order begins. Comparing fills against arrival measures implementation cost more directly than daily VWAP for many strategies.

Choose benchmark matching investment decision.

## 35. Liquidity sweep dưới microstructure

Prior highs/lows often cluster stops and breakout orders. Triggering them can generate temporary market-order flow.

If opposite resting liquidity absorbs flow, reversal can occur. This mechanism explains many “liquidity sweep” patterns without assuming intentional stop hunting conspiracy.

## 36. Liquidation cascades

Leveraged markets can experience forced liquidations when prices move through margin thresholds. Forced orders push price further, triggering more liquidations.

Crypto/futures/CFD traders must distinguish fundamental move from leverage cascade.

## 37. Circuit breakers và price limits

Markets may halt trading or impose price bands. These controls reduce disorderly trading but can trap positions and delay exit.

Risk sizing should include possibility stop cannot execute before halt/limit.

## 38. Volatility clustering

High-vol periods tend to persist. Fixed stop/size can therefore create unintended risk changes.

Volatility-normalized sizing helps but can become procyclical if it forces large deleveraging after shock.

## 39. Trading portfolio, không phải collection of trades

Five positions interact through common factors. EURUSD, GBPUSD and gold may all be short-USD exposure. Nasdaq, semis and growth stocks share duration/risk-on factors.

Book risk phải aggregate by factor, not ticket count.

## 40. Portfolio heat

Portfolio heat = planned potential loss if stops hit, often as % equity.

But nominal sum understates correlated tail loss. Heat limit nên include common-factor stress.

## 41. Correlation instability

Historical correlation changes by regime and tends rise in deleveraging.

Stress assumptions should use higher crisis correlation rather than average-only matrix.

## 42. Factor exposure

Map each trade to factors: USD, rates, equity beta, commodity, volatility, country, liquidity.

This reveals hidden concentration and helps choose redundant trades to cut.

## 43. Net vs gross exposure

Long/short book can have low net exposure but high gross exposure. Gross drives leverage, financing, turnover and gap risk even when beta partly hedged.

Both metrics matter.

## 44. Delta-equivalent exposure

Option portfolio should convert positions to delta-equivalent notional plus Gamma/Vega. Futures/CFD already linear-ish; options are nonlinear.

A seemingly small option premium can create large delta/gamma under moves.

## 45. Volatility targeting

Adjust size inversely with estimated volatility to stabilize risk.

But volatility estimate is backward-looking. Calm market before shock can lead high size exactly before volatility expansion.

## 46. Risk parity intuition

Equal capital ≠ equal risk. Scale positions so each contributes similar risk if strategy design warrants.

Still need gap/liquidity/tail adjustments because equal volatility does not equal equal tail loss.

## 47. VaR và Expected Shortfall

VaR estimates threshold loss at confidence; Expected Shortfall averages losses beyond threshold.

They are useful portfolio metrics but model-dependent and weak for unseen jumps. Scenario stress remains necessary.

## 48. Scenario stress

Create combined shocks: USD +5%, equities -10%, gold -7%, oil +15%, spreads widen, slippage doubles.

Ask book P/L and margin requirement under scenario. Stress should include correlation changes and liquidity deterioration.

## 49. Drawdown control

Predefined drawdown rules can reduce risk after statistical/operational deterioration.

Example normal risk 0.5%, reduce after -8R, pause/review after -12R—but thresholds must reflect strategy distribution.

Drawdown rule is circuit breaker, not emotional revenge control invented mid-loss.

## 50. Recovery math

-10% requires +11.1%; -50% requires +100% to recover.

Protecting against deep drawdown supports geometric compounding.

## 51. Pyramiding

Adding to winning trade can exploit trend while controlling risk. Recalculate total stop loss after every add.

If each add sized independently, pyramid can become hidden leverage.

## 52. Averaging down

Adding to losing position is not automatically wrong, but must be explicit strategy with preplanned total risk and thesis.

Unplanned averaging down to avoid realizing loss is behavioral error.

## 53. Scaling out

Partial exits can reduce variance/psychological burden but may cut right tail of trend-following system.

Backtest actual exit rule; do not assume partial profit-taking improves expectancy.

## 54. MAE/MFE

Maximum Adverse/Favorable Excursion help understand intratrade path and stop/target behavior.

Use distributions and out-of-sample validation; optimizing exact stop from MAE same sample can overfit.

## 55. Execution attribution

Separate P/L difference into signal timing, sizing, spread, commission, slippage, missed fills, market impact and management decisions.

Without attribution, trader may “fix strategy” when actual problem is execution.

## 56. Transaction Cost Analysis

TCA compares fills to benchmarks such as arrival, VWAP, close or model price and segments by order type, venue, session, volatility and size.

Purpose is detect systematic execution leakage.

## 57. Order reject và operational errors

Broker/API may reject due margin, symbol status, price bands or connectivity. System must handle rejects explicitly rather than assume position exists.

Operational risk can exceed market risk in automated trading.

## 58. Idempotency và duplicate orders

Retry logic can accidentally submit same order twice after network timeout.

Use client order IDs/idempotent workflow and reconcile broker positions before retrying.

## 59. Position reconciliation

Internal system state must match broker/exchange state. After restart/disconnect, reconcile open positions, pending orders, fills and cash.

Never trust only local database after outage.

## 60. Kill switch

Define conditions to halt new orders/flatten exposure: market-data failure, spread anomaly, broker outage, order duplication, daily loss limit or model malfunction.

Kill switch is operational safety, not forecast.

## 61. Capacity

As capital grows, order size relative volume rises, impact/slippage increase and opportunity count may become insufficient.

Capacity should be estimated before scaling, not discovered after edge disappears.

## 62. Execution and strategy horizon

Expected edge per trade should be large relative total friction. Very short-horizon strategies require exceptional execution quality.

If expected edge is 2 bps and realistic all-in cost 3 bps, better signal cannot fix negative implementation economics.

## 63. Pre-trade checklist

Before order: thesis/signal valid; position size; factor overlap; liquidity/spread; event risk; order type; max acceptable slippage; stop/exit logic; portfolio heat; margin buffer.

## 64. Post-trade checklist

After trade: decision price, fills, spread/slippage, MAE/MFE, rule adherence, market state, unexpected operational events, realized vs expected transaction cost.

Store data systematically so execution learning compounds.

## 65. Mental model cuối cùng

`Signal edge → Order choice → Venue/liquidity → Fill quality → Position/factor aggregation → Margin/tail stress → TCA → Process improvement`

Trading edge chỉ tồn tại nếu còn dương sau execution, financing, slippage và operational reality.