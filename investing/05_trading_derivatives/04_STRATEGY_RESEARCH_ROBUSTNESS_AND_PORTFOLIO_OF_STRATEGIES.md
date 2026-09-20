# 04 — Strategy Research, Robustness và Portfolio of Strategies

Tài liệu này nối khoảng cách giữa “biết backtest” và “có một trading research process đáng tin”. Mục tiêu là biến idea thành hypothesis, test nó với statistical discipline, đánh giá uncertainty, model execution/capacity và cuối cùng ghép nhiều strategies thành một portfolio mà không vô tình nhân đôi cùng một risk.

Một strategy đáng tin không phải strategy có equity curve đẹp nhất. Nó là strategy mà bạn hiểu **vì sao edge có thể tồn tại, edge dễ hỏng ở đâu, result nhạy với assumption nào và account có thể sống qua những path xấu nào**.

## 1. Trading idea khác strategy

Một idea có thể là “breakout sau consolidation thường tiếp tục”. Strategy cần biến idea thành rules có thể reproduce: universe, timeframe, consolidation definition, entry timing, stop, exit, position sizing, trading hours, event filters và maximum exposure.

Nếu hai người implement cùng document nhưng tạo signals rất khác nhau, specification chưa đủ rõ.

## 2. Hypothesis phải đứng trước optimization

Một **hypothesis** tốt bắt đầu từ economic, behavioral hoặc market-structure logic. Momentum có thể đến từ underreaction và slow information diffusion. Mean reversion có thể đến từ temporary liquidity shocks. Carry có thể là compensation cho crash risk. Market making kiếm spread nhưng chịu adverse selection.

Nếu chỉ scan hàng nghìn parameter combinations rồi chọn top result, xác suất bạn đang khai thác noise rất cao.

## 3. Edge cần có economic story nhưng story không đủ

Một plausible story không chứng minh edge tồn tại. Research phải có hai chân: causal intuition và empirical evidence.

Nếu story rất đẹp nhưng data không support, không trade. Nếu data đẹp nhưng không thể giải thích edge và parameter cực fragile, confidence cũng phải thấp.

## 4. Define universe trước khi nhìn result

Universe selection có thể tạo hidden bias. Nếu bạn chỉ test assets hiện tại liquid và successful, survivorship bias xuất hiện.

Universe phải phản ánh instruments thực sự tradable ở từng thời điểm, bao gồm delisted names nếu equity backtest dài hạn.

## 5. Timestamp discipline

Mỗi feature phải chỉ dùng data available tại decision time. Economic data revisions, corporate filings, index constituents và closing prices cần timestamp chính xác.

Một signal dùng today's close nhưng giả định fill tại same close có thể look-ahead nếu signal chỉ xác định sau market close.

## 6. Data cleaning không được tạo future knowledge

Adjusting splits/dividends là cần, nhưng cách adjustment có thể vô tình rewrite historical prices theo future corporate actions.

Missing data, bad ticks và stale quotes phải được xử lý với rule documented, không sửa thủ công chỉ khi trade xấu.

## 7. In-sample và out-of-sample

**In-sample (IS)** dùng develop strategy. **Out-of-sample (OOS)** dùng estimate generalization trên data chưa dùng fit.

Nếu OOS repeatedly deteriorates, strategy có thể overfit hoặc regime-specific hơn bạn nghĩ.

## 8. Validation set và test set

Trong research nghiêm túc, có thể tách development data thành train/validation và giữ final test set untouched.

Nếu bạn liên tục xem test result rồi sửa rules, test set đã trở thành training data về mặt hành vi.

## 9. Walk-forward analysis

Walk-forward train trên một window, test trên next window rồi roll forward. Nó mô phỏng process thực tế tốt hơn one-time split.

Nhưng bạn vẫn có thể overfit walk-forward parameters. Không có methodology nào miễn nhiễm data mining nếu researcher thử đủ nhiều variations.

## 10. Purged và embargoed validation

Với overlapping labels hoặc holding periods, adjacent train/test windows có thể leak information. **Purging** loại observations overlap; **embargo** tạo gap giữa train/test.

Khái niệm này quan trọng hơn với ML/quant research, nhưng tư duy leakage prevention hữu ích cho mọi backtest.

## 11. Look-ahead bias

Look-ahead xảy ra khi model dùng data future. Ví dụ dùng final daily high để trigger intraday trade hoặc dùng earnings figure trước timestamp release.

Đây là một trong những bugs nguy hiểm nhất vì backtest thường đẹp bất thường.

## 12. Survivorship bias

Testing chỉ current index members bỏ companies failed/delisted. Result thường inflated.

Point-in-time constituent data là gold standard nếu strategy phụ thuộc historical universe membership.

## 13. Selection bias

Nếu bạn chọn market để test vì biết trước market đó trend tốt, selection bias xuất hiện.

Research nên define selection logic trước: liquidity, instrument class hoặc economic criteria.

## 14. Data-snooping bias

Nếu test 1.000 strategies, một số sẽ có Sharpe đẹp chỉ do chance. Statistical significance phải được interpreted cùng number of trials.

Research log giúp biết bạn đã thử bao nhiêu ideas thật sự, thay vì giả vờ final test là hypothesis đầu tiên.

## 15. Multiple-hypothesis problem

Traditional p-value assume limited hypothesis testing. Khi thousands of rules được tested, false discoveries tăng.

Các concepts như False Discovery Rate, Reality Check hoặc Deflated Sharpe Ratio giúp nhắc rằng raw best Sharpe thường optimistic.

Retail trader không cần triển khai academic tests đầy đủ, nhưng phải có mental penalty rất lớn cho extensive optimization.

## 16. Parameter stability

Robust strategy hiếm khi chỉ hoạt động tại một exact parameter. Nếu MA 49 cực tốt còn 48/50 collapse, đó là red flag.

Hãy plot performance surface theo parameter. Broad plateau đáng tin hơn sharp peak.

## 17. Sensitivity analysis

Thay đổi fees, slippage, execution delay, stop size, entry threshold và holding period. Nếu strategy chỉ profitable với assumptions cực favorable, edge yếu.

Robustness nghĩa conclusion sống qua reasonable perturbations.

## 18. Placebo tests

Có thể shift signal timing, randomize entry nhỏ hoặc test related markets để xem performance có thực sự gắn với proposed mechanism không.

Nếu strategy vẫn “tốt” khi signal bị randomized, backtest infrastructure có thể có leakage hoặc market beta đang tạo illusion.

## 19. Simple benchmark trước complex model

Complex ML strategy phải beat simple baselines sau costs. Nếu linear rule hoặc buy-and-hold tạo same risk-adjusted result, complexity không mang economic value.

Complexity còn tăng operational và overfit risk.

## 20. Transaction costs

Backtest cần commission, spread, slippage, exchange fees, funding, borrow costs và taxes nếu applicable.

Cost model nên conservative và state-dependent. Spread during high volatility thường rộng hơn calm periods.

## 21. Market impact

Large order relative ADV hoặc depth tự làm price bất lợi. Impact thường nonlinear.

Strategy profitable với $10k không tự động scalable tới $10m. Capacity là property của edge.

## 22. Participation rate

Một useful metric là order size relative market volume. High participation tăng impact và information leakage.

Execution assumption phải match realistic participation.

## 23. Shorting constraints

Short strategy phải model borrow availability, borrow fees, recalls và hard-to-borrow names.

A backtest assuming unlimited short access ở exact close price thường unrealistic.

## 24. Futures roll và contract construction

Continuous futures series có thể tạo misleading historical prices nếu roll adjustment không phù hợp strategy.

Need distinguish actual tradable contracts, roll dates, basis và transaction cost during roll.

## 25. FX rollover và CFD financing

Forex/CFD long-horizon strategies phải model swaps/financing. Carry có thể là major component of return.

Ignoring funding can turn losing strategy into fake winner.

## 26. Corporate actions

Equity backtest cần dividends, splits, rights issues, mergers và delistings. Price return và total return khác nhau đáng kể ở long horizons.

## 27. Expectancy

Core equation:

`E = P(win) × AvgWin - P(loss) × AvgLoss`

Win rate không có ý nghĩa độc lập. Strategy 35% win có thể excellent nếu payoff large; 85% win có thể dangerous nếu rare loss huge.

## 28. R-multiple

Normalize trade result bằng initial risk `R`. Nếu stop-defined loss là $100, +2R nghĩa +$200.

R giúp compare trades across account sizes và instruments.

## 29. Confidence interval của expectancy

Sample expectancy là estimate, không fact. Với 30 trades uncertainty rất lớn. Confidence interval hoặc bootstrap distribution giúp quantify range.

Nếu lower plausible expectancy near zero, sizing nên conservative.

## 30. Serial correlation

Trades không luôn independent. Trend strategy có thể thắng/lỗ thành clusters theo regime.

Assuming IID trades understates long losing streaks và drawdown risk.

## 31. Skewness và tail risk

Short-vol/carry strategies thường negative skew: many small wins, rare huge loss. Trend/long-option strategies có thể positive skew.

Mean và standard deviation không capture full payoff shape.

## 32. Kurtosis và fat tails

Financial returns often have more extreme events than normal distribution. VaR based purely normal assumptions có thể underestimate tail risk.

Historical stress và scenario analysis phải complement statistical metrics.

## 33. Profit Factor

`Profit Factor = Gross Profit / Gross Loss`

PF >1 means historical gross wins exceed losses, nhưng high PF with few trades có uncertainty lớn.

## 34. Sharpe Ratio

Sharpe measures excess return per volatility. Useful for comparison nhưng penalizes upside/downside symmetrically và assume distribution properties that may not hold.

High Sharpe short-vol strategy vẫn có catastrophic tail.

## 35. Sortino, Calmar và MAR

Sortino focuses downside deviation. Calmar compares annualized return with max drawdown. MAR uses CAGR / max drawdown.

Metrics should describe different risk dimensions, not compete for one “best score”.

## 36. Maximum drawdown

Historical max drawdown is one observation, not worst possible future drawdown.

Sizing based on exact historical MDD is dangerous. Stress larger-but-plausible drawdowns.

## 37. Time under water

Drawdown duration matters psychologically and economically. Strategy may recover eventually but remain below high-water mark for years.

Capital patience must match expected recovery behavior.

## 38. Monte Carlo

Monte Carlo can reshuffle trades or simulate distributions to generate many equity paths. It helps estimate losing streaks, drawdown and terminal wealth ranges.

It does not magically model regime change; output quality depends assumptions.

## 39. Bootstrap

Bootstrap resamples observed returns/trades. Block bootstrap can preserve some serial dependence by sampling chunks.

This can be more realistic than independent reshuffle for clustered strategies.

## 40. Risk of ruin

Risk of ruin rises with high sizing, weak edge and high variance. Positive expectancy strategy can still bankrupt an account before edge realizes.

Survival is prerequisite for compounding.

## 41. Kelly criterion

Kelly estimates growth-optimal bet size under known edge/odds. In trading, edge estimates are noisy, so full Kelly is usually aggressive.

Fractional Kelly, e.g. quarter/half Kelly, is more robust but still requires conservative estimates.

## 42. Fixed fractional sizing

Risking fixed percentage per trade automatically reduces dollar risk during drawdown and increases as equity grows.

However correlated trades can still make total risk too high.

## 43. Volatility scaling

Scale position inversely to estimated volatility to stabilize risk. But volatility estimates lag and may rise after losses, causing procyclical de-risking.

Use caps/floors and understand estimator behavior.

## 44. Portfolio heat

Portfolio heat sums risk across open positions but should adjust for correlation/common factors.

Three trades each risking 0.5% are not truly 1.5% independent risk if all are same USD or equity-beta bet.

## 45. Drawdown budget

Define thresholds for normal drawdown, caution, size reduction and full review before live trading.

Circuit breaker protects capital and psychology while diagnosis happens.

## 46. Regime dependence

Trend, mean reversion, carry, volatility selling and breakout strategies thrive in different environments.

A strategy can be legitimate and still have long flat periods because source of edge is regime-dependent.

## 47. Regime filter caution

Adding filters after every historical loss is classic overfit. Filter should have causal reason and broad parameter stability.

Simpler robust filter often beats complex perfect-history filter.

## 48. Strategy degradation

Edge can decay due competition, market-structure changes, fees, regulation or participant adaptation.

Monitor rolling expectancy, opportunity count, hit rate, payoff, slippage and factor exposure.

## 49. Distinguish drawdown from degradation

A drawdown can be normal variance. Degradation means distribution itself may have changed.

Use multiple diagnostics; do not kill strategy from few losses, but do not worship historical backtest either.

## 50. Change-point thinking

Statistical change detection can help ask whether mean, variance or execution cost shifted. But small samples make false alarms common.

Combine quantitative evidence with causal market changes.

## 51. Forward test

Paper/demo forward test verifies data timing, signal generation, broker workflow and rule clarity.

It cannot fully test fills or psychology because capital not at risk.

## 52. Small live validation

Small real size checks execution, funding, borrow, latency and emotional response.

Goal is process validation, not profit maximization.

## 53. Scaling plan

Scale gradually only when live fills, cost and behavior match assumptions. Doubling size after short winning streak is not evidence-based scaling.

Capacity and liquidity must be re-evaluated at each scale.

## 54. Research log

Record hypothesis, dataset version, rules, parameters, costs, results and conclusion for every experiment.

This prevents unconscious p-hacking and repeated testing until something works.

## 55. Version control

Every strategy rule change should create new version. Keep performance by version so you know which rules produced which outcome.

Mixing versions destroys statistical interpretation.

## 56. Reproducibility

A research result should be reproducible from raw/approved data plus code/config. Manual undocumented overrides are hidden model risk.

For discretionary trading, screenshots and structured journal approximate reproducibility.

## 57. Portfolio of Strategies

Multiple strategies reduce dependency on one edge only when return streams have different drivers.

Five momentum systems across correlated FX pairs are not five independent edges.

## 58. Strategy correlation

Measure return correlation, but also downside/cisis correlation. Average correlation may hide joint failure in stress.

Rolling correlation helps see regime dependency.

## 59. Factor decomposition

Strategies often hide long equity beta, short volatility, carry, duration or USD exposure. Factor regressions or scenario analysis can reveal common sources.

Diversification should occur at factor level, not strategy-name level.

## 60. Convexity mix

Short-vol strategies produce frequent income but negative convexity. Trend following or long options can provide more positive convexity.

Portfolio design can intentionally combine payoff shapes rather than only correlations.

## 61. Equal capital vs equal risk

Equal capital assigns same dollars but not same risk. High-vol strategy dominates portfolio volatility.

Risk allocation should consider standalone vol, correlation and tail behavior.

## 62. Risk parity across strategies

Strategy risk parity scales each to similar volatility/risk contribution, but correlations and non-normal tails still matter.

It is a starting framework, not complete solution.

## 63. Correlation spikes

During stress, many strategies de-lever simultaneously or respond to same volatility shock. Historical diversification may disappear.

Stress portfolio with correlation assumptions worse than average.

## 64. Liquidity across strategies

If several strategies need exit same instrument during stress, capacity is shared. Portfolio-level liquidity matters.

Independent signals can still compete for same execution bandwidth.

## 65. Capital efficiency và margin

Futures/options allow multiple strategies share collateral, but margin requirements can rise together in volatility spikes.

Unused cash buffer is essential; theoretical margin efficiency can become crisis fragility.

## 66. Operational risk

API error, wrong symbol, duplicate order, time-zone bug, stale data or broker outage can destroy a mathematically good strategy.

Need order validation, reconciliation, alerting, max-order limits and kill switch.

## 67. Model risk

Strategy code may implement different logic than research notebook. Unit tests and sample-trade reconciliation reduce model risk.

Manual strategies need checklist for same reason.

## 68. Broker/counterparty risk

Execution quality, stop-out rules, funding, data feed and legal entity matter, especially OTC CFD/FX.

Strategy edge does not protect against broker failure or unsuitable leverage terms.

## 69. Post-trade attribution

Separate signal quality, sizing, entry execution, exit execution and discretionary override.

A loss following rules is statistical outcome; a profit from breaking rules can still be process failure.

## 70. Daily, weekly và monthly review

Daily review checks operational issues and violations. Weekly review looks execution/slippage and setup distribution. Monthly/quarterly review evaluates edge, regime and degradation.

Do not redesign strategy after every losing day.

## 71. Kill criteria

Before launch, define conditions requiring pause: data failure, broker inconsistency, drawdown threshold, structural market change or statistically meaningful deterioration.

Predefined kill criteria reduce emotional denial.

## 72. Research falsification mindset

Research should try to kill the idea. Search for periods, markets and parameter perturbations where it fails.

If hypothesis survives independent tests, confidence increases. Confirmation-only research creates fragile systems.

## 73. Minimum viable evidence

There is no universal number of trades sufficient. Sample requirement depends variance, edge size, holding period and independence.

A small but economically strong edge needs more observations to distinguish from noise.

## 74. Capacity-adjusted expected return

Expected return before costs is not enough. As capital grows, impact and opportunity availability can reduce return.

The best strategy for small account may not be best for institutional scale.

## 75. Research-to-production checklist

Before live capital, confirm data timestamps, universe, execution assumptions, costs, OOS robustness, parameter sensitivity, risk limits, broker behavior, monitoring, failover and version control.

If one layer is undefined, production risk remains.

## 76. Kết luận

Strategy research là engineering dưới uncertainty. Bạn không cố chứng minh system chắc chắn kiếm tiền; bạn cố estimate edge, hiểu uncertainty và xây sizing/process để survive khi estimate sai.

Một system tốt không cần perfect equity curve. Nó cần logic, reproducibility, realistic costs, robust parameters, independent validation, operational controls và portfolio context đủ mạnh để tồn tại qua regime change.