# Systematic Risk, Backtest, Validation và Execution

> Một trading idea chỉ trở thành system khi rules đủ rõ để test, data đủ sạch để không tự lừa mình, risk đủ nhỏ để survive và execution đủ realistic để live result không sụp đổ. Chapter này xây toàn bộ pipeline từ hypothesis → specification → data → backtest → statistical validation → robustness → execution → production monitoring.

## 1. Setup khác System

Một **setup** chỉ mô tả bối cảnh vào lệnh. Một **system** hoàn chỉnh phải định nghĩa universe/instrument, timeframe, session, signal, executable timestamp, entry, invalidation, exit, position sizing, maximum exposure, cost assumptions, event rules, operational controls và conditions tạm dừng.

Nếu hai người đọc rules mà tạo trades rất khác nhau, specification còn quá discretionary để một backtest có ý nghĩa.

## 2. Hypothesis phải có trước Code

Research nên bắt đầu bằng causal/economic/behavioral hypothesis. Momentum có thể tồn tại vì slow information diffusion; mean reversion có thể tồn tại sau liquidity dislocation; carry có thể là compensation cho crash/liquidity risk.

Nếu chỉ scan hàng nghìn indicator combinations để tìm curve đẹp, xác suất tìm noise rất cao. Hãy viết trước: edge có thể tồn tại vì sao, ai trả premium đó và lý do gì khiến nó chưa bị arbitrage hết.

## 3. Falsification Mindset

Mục tiêu research không phải chứng minh strategy đúng mà cố tìm cách nó sai. Một hypothesis càng sống sót nhiều independent tests, confidence càng tăng.

Nếu mỗi test xấu đều dẫn tới thêm một filter để “sửa”, bạn đang chuyển từ research sang curve fitting.

## 4. Universe Definition

Universe phải được xác định bằng rule có thể biết tại thời điểm lịch sử. Equity system test chỉ trên constituents hiện tại có **survivorship bias**. FX majors và exotics có liquidity/cost regimes rất khác.

Universe selection bản thân cũng là parameter; nếu chọn instrument sau khi nhìn chart đẹp, result đã bị selection bias.

## 5. Point-in-Time Data

Fundamentals, index membership, analyst estimates và macro data có revisions. Backtest phải dùng version thực sự available tại decision time nếu edge phụ thuộc những inputs này.

Dùng final revised GDP hoặc earnings data để quyết định historical trade là look-ahead dù timestamp file có vẻ đúng.

## 6. Corporate Actions

Stocks cần xử lý splits, dividends, rights, mergers, delistings và symbol changes. Adjusted prices tốt cho total-return analysis nhưng có thể sai cho actual execution nếu applied không đúng.

Researcher phải biết dataset đã adjust cái gì và khi nào.

## 7. Time Zones

Market data từ US, Korea, Vietnam và macro calendars có timezone khác. Một signal sử dụng data release sau close nhưng backtest cho entry cùng close tạo fake edge.

Mọi feature và order cần timestamp trong một canonical timezone rồi map về local session.

## 8. Bar Construction

OHLC bars hide intrabar path. Nếu cùng bar chạm stop và target, bar data không cho biết event nào xảy ra trước.

Lower-timeframe data hoặc conservative assumption cần được dùng nếu order sequence ảnh hưởng outcome.

## 9. Sampling Frequency

Nhiều observations không đồng nghĩa nhiều independent information. 100,000 one-minute bars trong một regime có thể ít useful diversity hơn 20 năm daily data qua nhiều regimes.

Effective sample size giảm khi returns/signals autocorrelated.

## 10. Entry Timestamp

Nếu signal tính bằng daily close, entry same close thường cần auction/market-on-close assumption thực tế. Nếu signal chỉ được biết sau close, earliest executable time là phiên sau.

Signal timestamp và fill timestamp phải được tách rõ.

## 11. Exit Specification

Exit có thể là stop, target, time stop, opposite signal, trailing logic hoặc event rule. Multiple exits tương tác, nên priority phải được define.

Không được nhìn historical trade rồi chọn “exit hợp lý nhất” cho từng case.

## 12. Invalidation trước Position Size

Stop tốt thường gắn thesis invalidation hoặc volatility structure. Position size sau đó được tính từ distance tới invalidation.

Chọn lot trước rồi kéo stop tới mức vừa dollar risk là logic ngược.

## 13. Position Sizing

Nếu account equity `E`, risk fraction `r`, loss per unit tới stop là `L`:

```text
Position Size = E × r / L
```

Với futures/FX/CFD phải tính multiplier, tick/pip value và currency conversion.

## 14. R-Multiple

**1R** là planned initial risk. +2R nghĩa gain bằng hai lần initial risk; -1R là full planned stop loss.

R giúp normalize trades, nhưng actual gap/slippage có thể tạo -1.5R, -3R hoặc hơn. Journal phải dùng realized R.

## 15. Expectancy

```text
Expectancy = P(win) × AvgWin - P(loss) × AvgLoss
```

Positive expectancy chỉ là estimate. Short-run outcome vẫn có thể âm vì variance và sequencing.

## 16. Profit Factor

```text
Profit Factor = Gross Profit / Gross Loss
```

PF > 1 trong sample chưa chứng minh edge. Sample size, top-trade dependency, costs và regime diversity quan trọng hơn headline PF.

## 17. Payoff Distribution

Trend systems thường right-skewed: many small losses, few large winners. Short-vol systems thường negative-skewed: many small wins, rare huge losses.

Cùng average return nhưng distribution shape có operational/risk implication rất khác.

## 18. Median vs Mean Trade

Mean can be dominated by outliers. So sánh mean, median, percentiles và trimmed results giúp thấy strategy phụ thuộc vài extreme winners/losses đến đâu.

Nếu bỏ top five trades mà expectancy biến mất, cần hiểu đó là flaw hay natural convexity của strategy.

## 19. Maximum Drawdown

Max drawdown là largest peak-to-trough loss trong một realized path. Nó không phải future worst case.

Measure thêm drawdown duration/time underwater; psychological/capital pressure có thể đến từ thời gian dài không tạo new high chứ không chỉ depth.

## 20. Sequence Risk

Same set trades với ordering khác tạo path khác. Leverage/withdrawal/scaling khiến sequencing ảnh hưởng survival.

Đây là lý do Monte Carlo path analysis quan trọng.

## 21. Risk of Ruin

Risk of ruin tăng khi expectancy nhỏ, variance lớn và bet size cao. Even profitable edge can fail before law of large numbers if sizing aggressive.

Survival is prerequisite for compounding.

## 22. Kelly Criterion

Kelly gives growth-optimal fraction under known probabilities/payoffs. Trong markets, inputs are estimated and nonstationary, nên full Kelly thường quá aggressive.

Fractional Kelly hoặc conservative fixed risk thực tế hơn.

## 23. Portfolio Heat

Risk/trade không đủ khi nhiều positions mở. Long EURUSD, GBPUSD và gold có thể cùng short-USD factor.

Define max aggregate planned loss và factor-level exposure, không chỉ sum ticker count.

## 24. Gross và Net Exposure

Long 100 và short 80 có gross exposure 180 nhưng net 20. Gross quyết định leverage/liquidity risk; net quyết định directional bias gần đúng.

Both need monitoring.

## 25. Beta / Factor Exposure

A long-short portfolio net market-neutral may still be long size, momentum, quality or short volatility.

Factor decomposition helps identify hidden bets that become correlated during stress.

## 26. Correlation Instability

Historical correlations often rise during deleveraging. Stress test with higher correlations than sample average.

Diversification should be based on different economic drivers, not only a static matrix.

## 27. Data Cleaning

Bad ticks, duplicated bars, stale quotes, missing sessions and zero prices can create fake fills/signals.

Build sanity checks for impossible returns, volume spikes and timestamp gaps.

## 28. Look-Ahead Bias

Examples include using final daily high before decision, future constituent list, revised macro data or next-bar information embedded in indicator.

Every feature should have an availability timestamp.

## 29. Survivorship Bias

Using only securities that survived to today removes bankrupt/delisted names, typically overstating returns of many equity strategies.

Point-in-time universes are preferred.

## 30. Selection Bias

If you picked market because you already noticed pattern, instrument choice is data-mined.

Document why universe exists before seeing test result.

## 31. Data Snooping

Testing 1,000 variants makes some high-Sharpe outcomes inevitable by chance. Research log should count failed tests, not only winners.

A final result should be judged in context of total search effort.

## 32. Multiple Hypothesis Adjustment Intuition

You do not need advanced statistics initially, but should understand that 5% significance is less impressive after hundreds tests.

Methods such as Bonferroni, false-discovery-rate or White’s Reality Check formalize this idea; the practical lesson is to keep models simple and use untouched data.

## 33. Train / Validation / Test

Development data builds strategy; validation data selects model/parameters; final test stays untouched until decisions are frozen.

Once you inspect final test and change rules, it is no longer final test.

## 34. Time-Series Split

Random shuffle often leaks future regimes into training. Financial data usually requires chronological splits.

For overlapping labels/signals, even neighboring samples may share information.

## 35. Purging và Embargo Intuition

If training and validation windows overlap through holding periods, leakage can remain. **Purging** removes overlapping observations; **embargo** leaves gap around boundaries.

Concept matters more than implementation detail: prevent future outcome information from contaminating training.

## 36. Walk-Forward Analysis

Repeatedly calibrate on past and test next window. This approximates real operating process and reveals parameter/regime instability.

Do not optimize walk-forward windows themselves until curve perfect.

## 37. Anchored vs Rolling Window

Anchored training grows through time; rolling window keeps recent fixed history. Anchored assumes old data remains informative; rolling adapts faster but throws away history.

Choice should reflect hypothesis, not best backtest.

## 38. Parameter Stability

Good edge often works across a plateau of nearby parameters. Isolated spike at exact 17 days is red flag.

Plot parameter surface and inspect smoothness.

## 39. Sensitivity Analysis

Change stops, lookbacks, cost assumptions and signal thresholds modestly. If performance collapses from tiny perturbation, system is fragile.

Robustness is not same as maximizing return.

## 40. Placebo Tests

Shift signals randomly, trade unrelated universe or invert timing to see whether apparent edge survives where causal logic says it should not.

If placebo performs similarly, original story may be spurious.

## 41. Regime Segmentation

Analyze by volatility, trend/range, rates, sessions, bull/bear and liquidity regime.

If edge lives only one regime, that can be acceptable if causal and filter ex ante. It is dangerous if discovered only after slicing until one bucket looks good.

## 42. Subsample Stability

Split by decades, instruments, regions or market-cap groups. Edge that works only one stock or one year deserves lower confidence.

Generalization across related markets is strong evidence.

## 43. Transaction Costs

Include commission, spread, exchange fees, taxes, funding, borrow and roll costs.

Costs should reflect historical regime, not today’s tight spread applied to crisis years.

## 44. Slippage

Slippage depends volatility, urgency, spread, order type and size vs liquidity.

A strategy with 0.04R expected edge and 0.03R uncertain cost is not robust.

## 45. Market Impact

Impact rises nonlinearly as participation rate increases. Capacity is part of strategy definition.

An edge viable at $10k may disappear at $10m.

## 46. Limit-Order Fill Bias

Bar touching limit does not guarantee fill. Queue position and traded volume matter.

Use conservative assumptions, especially mean-reversion/scalping.

## 47. Stop Fill và Gap

Do not assume exact stop on gap. Use next tradable price or stress gap distribution.

News/weekend gaps can create losses beyond planned R.

## 48. Borrow Constraints

Short-equity strategy needs locate availability, borrow fee and recall risk. Hard-to-borrow names often carry the very signal being tested.

Ignoring borrow can create impossible alpha.

## 49. Futures Roll

Futures backtests need realistic contract rolls and basis/roll yield. Continuous adjusted series is useful for signals but may not equal tradable P/L.

Specify roll rule and execution costs.

## 50. Funding Cost

Leveraged/CFD/FX positions incur financing. Strategy holding periods long enough can have large carry effect.

Funding regime changes should be included historically.

## 51. MFE và MAE

MFE/MAE help understand intra-trade path and stop/target design. But optimizing stops directly on same sample overfits.

Use as diagnostic, then validate independently.

## 52. Bootstrap

Bootstrap resamples outcomes to estimate confidence intervals. Block bootstrap can preserve some serial dependency.

Wide expectancy interval crossing zero means point estimate is weak evidence.

## 53. Monte Carlo Paths

Simulate many orderings/return draws to estimate drawdown, losing streak and terminal wealth distributions.

Monte Carlo does not predict future; it quantifies path uncertainty under assumptions.

## 54. Statistical Power

Small samples cannot reliably distinguish small edge from noise. Strategy with 25 trades and high Sharpe is usually less convincing than moderate Sharpe over hundreds independent observations and multiple regimes.

Sample quality matters more than raw count.

## 55. Autocorrelation

Returns/trades may be serially correlated. Assuming independence can overstate effective sample size and understate risk.

Trend/carry strategies often cluster wins/losses by regime.

## 56. Nonstationarity

Market distribution changes as participants, policy, technology and costs evolve. Historical average is not guaranteed stable.

Robust strategy should have causal reason to persist and monitoring for degradation.

## 57. Sharpe Ratio

Sharpe = excess return divided volatility. It is useful but weak for skewed/tail strategies and can be inflated by smoothing.

Use with drawdown, skew and stress metrics.

## 58. Sortino Ratio

Sortino penalizes downside deviation rather than all volatility. Better for some asymmetric profiles but still ignores extreme tail structure.

## 59. Calmar Ratio

Calmar compares annualized return to max drawdown. Because max DD is one sample event, confidence is low in short history.

Use Monte Carlo drawdown distribution too.

## 60. Expected Shortfall

Expected Shortfall estimates average loss beyond a tail percentile. It is more informative than VaR about severity after threshold.

Historical ES needs enough tail data; scenario stress remains necessary.

## 61. Ulcer / Time-Under-Water Thinking

Two systems with same max DD can feel very different if one recovers in weeks and one in years. Time under water affects capital patience and business viability.

Include recovery time in evaluation.

## 62. Strategy Archetypes

Trend, mean reversion, carry, breakout, market making and event strategies earn different premia and fail differently.

Portfolio construction should diversify failure modes, not just names.

## 63. Trend Following

Trend systems often tolerate low hit rate and rely on big winners. Main risks: chop, crowding, gap and delayed response.

Do not judge by win rate.

## 64. Mean Reversion

Mean reversion can produce frequent small gains but suffers when “temporary” move becomes structural trend.

Liquidity, stop discipline and regime detection matter.

## 65. Carry

Carry earns ongoing premium but often embeds short-volatility/liquidity exposure. FX carry can unwind violently when funding currencies strengthen.

Backtest must include crisis episodes.

## 66. Breakout

Breakout seeks transition from compression to expansion. False breaks and slippage around triggers are key failure modes.

Parameter robustness matters more than finding perfect lookback.

## 67. Strategy Correlation

Measure correlations of daily returns and stress periods. Two systems may look low-correlated normally but both be short liquidity in crisis.

Factor decomposition is better than strategy count.

## 68. Risk Allocation Across Strategies

Equal capital ≠ equal risk. Allocate by volatility, drawdown, expected shortfall and factor exposure.

High-vol strategy may need much smaller capital weight.

## 69. Volatility Targeting

Scale exposure down when estimated vol rises and up when falls. It stabilizes risk but can force deleveraging after shocks and add procyclicality.

It is risk control, not guaranteed alpha.

## 70. Capacity

Capacity depends turnover, depth, holding period and edge magnitude. Estimate participation rate, days-to-liquidate and impact.

Scaling is part of research, not postscript.

## 71. Paper Trading

Paper validates signals, timestamps, operational workflow and order logic but underestimates psychology and adverse fills.

Use it to debug implementation, not prove edge.

## 72. Small-Live Validation

Trade minimum meaningful size. Compare live vs modeled spread, slippage, missed fills and behavior.

Scale only after predefined evidence threshold, not few winners.

## 73. Production Monitoring

Track signal frequency, expectancy, hit rate, payoff ratio, slippage, latency, rejected orders, exposure and data health.

A production system needs monitoring like software service plus risk desk.

## 74. Drift Detection

Feature distributions, trade frequency or payoff can drift. A system may degrade before total P/L clearly signals it.

Monitor rolling distributions and compare with research baseline.

## 75. Change-Point Thinking

Not every drawdown means regime change. But abrupt shifts in cost, volatility or signal behavior may indicate structural break.

Use multiple evidence sources instead of one rolling Sharpe threshold.

## 76. Kill Switch

Pause trading on data-feed failure, abnormal spread, broker outage, model malfunction, breached daily loss, duplicated orders or conditions strategy was never designed for.

Kill switch protects operational tail risk.

## 77. Position Reconciliation

Automated strategy must reconcile internal positions with broker positions. Network/API error can create ghost or duplicate exposure.

Reconciliation is non-negotiable in production.

## 78. Order Idempotency

Retrying failed API call must not accidentally duplicate order. Use unique client order IDs and state management.

This is a software-engineering risk with direct financial consequence.

## 79. Versioning

Every rule/code/data change creates strategy version. Record what changed, why and expected impact.

Never silently tweak after losses and continue same performance history.

## 80. Research Log

Log hypothesis, datasets, tests, parameter ranges, failed variants and conclusions. This exposes how much search produced the final winner.

Failed research is valuable evidence.

## 81. Trade Journal

Separate valid win/loss, execution error, rule violation and operational issue.

Winning rule violation is bad process; losing valid trade is normal sample.

## 82. Weekly Review

Check rule adherence, actual vs expected costs, open factor exposure and operational errors. Do not redesign system from one week P/L.

Weekly review is for process health.

## 83. Monthly / Quarterly Review

Aggregate by setup, instrument, session, regime and execution type. Compare live distribution with OOS/backtest assumptions.

Identify whether divergence comes from edge, cost, capacity, implementation or behavior.

## 84. Degradation Rules

Predefine thresholds for review/reduce/pause: persistent expectancy deterioration, cost increase, opportunity collapse or structural market change.

Thresholds should account normal statistical variation.

## 85. Production Checklist

Before live, rules frozen; timestamps audited; point-in-time data verified; costs modeled; OOS/walk-forward done; parameter stability acceptable; Monte Carlo/stress survived; broker specs checked; exposure limits defined; logging/reconciliation/kill switch tested.

## 86. Research Quality Hierarchy

Confidence is stronger when an edge has causal logic, clean data, pre-specified test, independent OOS, parameter plateau, cross-market evidence, realistic costs and live confirmation.

A beautiful in-sample equity curve sits near the bottom of that hierarchy.

## 87. Mental Model cuối cùng

```text
Hypothesis
→ Precise Rules
→ Point-in-Time Data
→ Bias Audit
→ Cost-Aware Backtest
→ OOS / Walk-Forward
→ Robustness / Placebo
→ Bootstrap / Monte Carlo / Stress
→ Paper
→ Small Live
→ Production Controls
→ Scale by Capacity
→ Monitor Drift
→ Versioned Improvement
```

Trading edge is not a chart pattern. It is a research, engineering, execution and risk-management process that must survive uncertainty.