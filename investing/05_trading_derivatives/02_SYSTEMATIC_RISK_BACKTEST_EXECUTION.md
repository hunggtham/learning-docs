# Systematic risk, backtest và execution

> Một trading idea chỉ trở thành system khi rules đủ rõ để test, risk đủ rõ để survive và execution đủ realistic để live result không sụp đổ. Chapter này xây process từ hypothesis → rule → data → backtest → robustness → forward/live → review.

## 1. Setup khác system

Setup mô tả entry context. System hoàn chỉnh cần universe/instrument, timeframe, session, entry, invalidation, stop, target/exit, position sizing, news/event rules, maximum exposure, execution assumptions và conditions tạm dừng.

Nếu hai người đọc rules mà tạo trades rất khác nhau, specification còn quá discretionary để backtest đáng tin.

## 2. Hypothesis trước code

Backtest nên bắt đầu bằng causal/economic hypothesis, ví dụ trend persistence do slow information diffusion hoặc mean reversion after liquidity shock.

Nếu bắt đầu scan hàng nghìn indicator combinations để tìm equity curve đẹp, data-mining risk cực cao.

Write why edge may exist, who pays it and why it might persist.

## 3. Define universe

Universe selection affects results. A stock strategy tested only on current index constituents has survivorship bias. FX system on liquid majors differs exotic pairs.

Define inclusion rules available at each historical date when possible.

## 4. Timeframe và sampling

Signal on daily bars has different microstructure/cost sensitivity than M1/M5. Lower timeframe increases number observations but not necessarily independent information.

Ten thousand 1-minute trades from one regime may contain less regime diversity than 300 daily trades over decades.

## 5. Entry rule

Entry must reference information available at decision time. If using daily close signal and entering same close without realistic auction/latency assumption, you may create look-ahead.

Specify signal timestamp and executable timestamp.

## 6. Exit rule

Exit can be price target, stop, time, opposite signal, trailing rule or event-based. Multiple exits interact.

Avoid tuning exit per past trade. Rule must be known ex ante.

## 7. Stop loss as invalidation vs money amount

Good stop often represents thesis invalidation or volatility-adjusted threshold. Position size then adapts to stop distance.

Choosing fixed lot first and moving stop until dollar risk fits reverses logic.

## 8. Position sizing

If account equity `E`, risk fraction `r`, stop distance in money per unit `L`:

`Position Size = E × r / L`

For leveraged instruments, confirm contract multiplier/pip/tick value.

Sizing is often more important than minor entry optimization.

## 9. R-multiple

Define 1R = initial risk. A +2R trade wins twice initial risk; -1R hits full planned loss.

R normalizes across account size/instruments and enables expectancy comparison.

But gaps/slippage can produce losses worse than -1R; journal actual R.

## 10. Expectancy

`Expectancy = WinRate × AvgWin - LossRate × AvgLoss`

Example 40% win, average +2R, 60% loss -1R:

`0.4×2 - 0.6×1 = +0.2R/trade`

Positive expectancy doesn't guarantee short-run profit due variance.

## 11. Profit factor

`Profit Factor = Gross Profit / Gross Loss`

PF >1 historically positive, but small sample can inflate. Compare across regimes/out-of-sample and costs.

## 12. Payoff distribution

Win rate and PF hide skew. Trend strategy often many small losses/few big wins; short-vol strategy many small wins/rare huge losses.

Inspect distribution, tails, largest winners/losses and dependency on top trades.

If removing top 5 trades destroys system, edge fragile or inherently convex; understand which.

## 13. Drawdown

Drawdown measures decline from equity peak. Max drawdown is one historical path, not future worst case.

Also measure drawdown duration/time underwater. A 15% drawdown lasting 2 years can be harder operationally than 20% recovered in month.

## 14. Risk of ruin

Risk of ruin depends expectancy, variance and bet size. Even positive-edge system can blow up if risk/trade too large.

Compounding losses: at 10% risk/trade, 5 consecutive losses leave `0.9^5 ≈ 59%` capital. At 1%, `0.99^5 ≈ 95%`.

Sizing determines survival.

## 15. Portfolio heat

Risk per trade understates risk when multiple positions open. Sum planned losses and factor correlations.

Long EURUSD, GBPUSD and gold can all be short-USD macro bet. Three 0.5% risks may behave near one concentrated exposure.

Set max portfolio heat and factor limits.

## 16. Correlation is unstable

Historical correlation changes in crises. Assets with low normal correlation can converge under deleveraging.

Stress correlation higher than normal rather than trust sample matrix.

## 17. Data quality

Backtest data can contain bad ticks, missing bars, corporate-action errors, timezone shifts and incorrect spreads.

Validate suspicious outliers. For stocks use adjusted/unadjusted data appropriately depending dividends/splits and execution.

## 18. Look-ahead bias

Using information not available at trade time creates fake edge: revised fundamental data, future index membership, high/low of current bar before decision.

Timestamp every feature relative execution.

## 19. Survivorship bias

Testing only companies alive today removes bankrupt/delisted names and overstates many equity strategies.

Use point-in-time universe if possible or explicitly acknowledge bias.

## 20. Selection bias

Testing strategy only on instrument because you saw its historical pattern is selection bias. Universe choice itself can be overfit.

Document selection rule before test.

## 21. Data-snooping/multiple-testing bias

If test 1,000 strategies, some look excellent by chance. Best Sharpe among many is not same evidence as pre-specified hypothesis.

Keep research log counting failed tests. Holdout data becomes contaminated once repeatedly inspected.

## 22. In-sample và out-of-sample

In-sample develops rules/parameters. Out-of-sample evaluates unseen data.

Do not optimize after seeing OOS then still call it OOS. Once used for decisions, it is part of development set.

## 23. Train/validation/test mindset

A practical structure: train/development period; validation for parameter/model choices; final untouched test for confidence.

Financial nonstationarity means split should preserve time order rather than random shuffle for most strategies.

## 24. Walk-forward

Walk-forward repeatedly trains/calibrates on past window then tests next period, simulating real process.

It reveals whether edge persists through regimes and parameter recalibration.

Avoid excessive frequent reoptimization that simply chases noise.

## 25. Parameter stability

Robust system should work across neighborhood of parameter values, not only magic 17-day lookback.

Plot performance vs parameters. Smooth plateau more credible than isolated spike.

## 26. Regime segmentation

Break results by volatility, trend/range, bull/bear, policy regimes, sessions and instrument classes.

If strategy only works in one period, decide whether causal regime filter exists or sample accident.

## 27. Transaction costs

Include commission, spread, slippage, financing/borrow, exchange fees and taxes where relevant.

Cost should reflect historical liquidity/volatility, not today's minimum spread across whole sample.

## 28. Slippage model

Simple model can assume half/full spread plus fixed ticks. Better model scales with volatility, order size vs volume and market order usage.

Strategy edge 0.05R/trade with estimated cost 0.04R is dangerously fragile.

## 29. Market impact

Large order moves market. Retail may ignore for very liquid markets at small size, but illiquid small caps/systematic scale must model.

Capacity is maximum capital before impact erodes edge materially.

## 30. Limit-order fill bias

Backtest often assumes limit fills if bar touches price. In reality queue may be ahead; touch can occur with insufficient volume.

Conservative fill assumptions important for mean-reversion/scalping.

## 31. Stop fill and gaps

Backtest should not assume exact stop price if market gaps beyond. Use next available price or gap model.

Overnight/weekend/news risk can create tail losses exceeding planned 1R.

## 32. MFE và MAE

Maximum Favorable Excursion and Maximum Adverse Excursion show best/worst intratrade move before exit.

They help research stop/target but can overfit if optimized directly on same sample.

Use distributions, then validate changes out-of-sample.

## 33. Monte Carlo

Historical equity curve is one ordering. Resample trade outcomes or block sequences to estimate distribution of drawdowns, losing streaks and terminal equity.

Block/bootstrap methods can preserve some autocorrelation better than simple shuffle.

Monte Carlo does not create future truth; it shows path uncertainty.

## 34. Bootstrap confidence interval

Bootstrap can estimate confidence interval for mean return/expectancy. Wide interval crossing zero means sample evidence weak even if point estimate positive.

This encourages humility vs one Sharpe number.

## 35. Sharpe

Sharpe ≈ excess return / return volatility. Useful for symmetric strategies, but assumes volatility captures risk reasonably.

Short-tail strategies can show high Sharpe before crash.

## 36. Sortino

Sortino uses downside deviation, less penalizing upside volatility. Still not tail-loss complete.

## 37. Calmar

Calmar compares annualized return to max drawdown. Sensitive to sample because max DD single event.

Use alongside drawdown duration and Monte Carlo.

## 38. Expected Shortfall

Expected Shortfall estimates average loss beyond tail percentile. It focuses severity after VaR threshold.

Historical estimate needs enough tail observations; scenario stress remains necessary.

## 39. Regime filters

Trend/volatility/macro filters can improve if causal. But every filter reduces sample size and adds degrees of freedom.

Simple rule with stable logic preferable to 12 filters fitted to historical losses.

## 40. Trend vs mean reversion

Trend system suffers chop; mean-reversion suffers persistent trend/gap. Combining uncorrelated strategy archetypes can improve portfolio resilience.

But correlations can rise during stress.

## 41. Carry strategies

Carry earns yield/roll premium but often short volatility/liquidity in disguise. FX carry can unwind when funding currencies strengthen in risk-off.

Backtest must include crisis tails.

## 42. Breakout

Breakout benefits volatility expansion/trend but false breaks common. Execution/slippage around triggers matter.

Do not optimize exact breakout length only.

## 43. Strategy capacity

Capacity depends market depth, turnover and holding period. A profitable small-cap strategy may stop working at large AUM.

Estimate order size as fraction of volume and days to enter/exit.

## 44. Paper trading

Paper verifies logic, signal timing and workflow but understates psychology and fill difficulty.

Use to catch implementation bugs before live money.

## 45. Small-live phase

Trade smallest meaningful size to observe real spread, slippage, broker behavior and psychology.

Do not scale from three wins. Require sample/process criteria defined beforehand.

## 46. Scaling rules

Scale based on evidence and capacity. Increase gradually, monitor execution cost and drawdown.

If performance degrades as size rises, reduce; don't assume edge unchanged.

## 47. Strategy degradation

Edge can decay because competition, structural market change, costs or crowding.

Monitor rolling expectancy, hit rate, payoff, slippage and regime-adjusted performance. Avoid shutting after normal statistical drawdown.

Define degradation threshold before pain.

## 48. Change management

Every rule change creates new strategy version. Document reason, expected effect and test evidence.

Do not silently tweak stop after losses; version and retest.

## 49. Research log

Log hypothesis, datasets, tests, parameters tried, rejected ideas and conclusions.

This reduces hindsight/data-snooping and lets you learn from failed research.

## 50. Trading journal

Trade journal should separate:

- strategy-valid loss;
- strategy-valid win;
- execution error;
- rule violation;
- operational issue.

Winning rule violation is bad process. Losing valid trade is not mistake.

## 51. Weekly review

Review R distribution, errors, slippage, exposures, regime and whether rules followed.

Avoid changing system based one week. Use review to collect evidence.

## 52. Monthly/quarterly review

Aggregate by setup, session, instrument, regime and execution type. Compare live vs backtest assumptions.

If divergence appears, identify whether market edge, costs, implementation or behavior changed.

## 53. Kill switch

Define conditions to pause: data feed failure, abnormal spread, broker issue, model malfunction, daily loss limit or structural event strategy not designed for.

Kill switch protects from operational tail risk, not market prediction.

## 54. Production checklist

Before live: rules frozen; code reviewed; timestamps correct; costs modeled; OOS/walk-forward passed; Monte Carlo stress acceptable; broker contract specs verified; sizing/heat limits; kill switch; logging; backup plan.

A strategy not operationally executable is not a strategy.

## 55. Mental model cuối cùng

`Hypothesis → Rules → Point-in-time data → Cost-aware backtest → Robustness/OOS → Stress/Monte Carlo → Paper → Small live → Scale → Monitor/degrade → Versioned improvement`

Trading advantage is a research and risk-control process, not a chart pattern.