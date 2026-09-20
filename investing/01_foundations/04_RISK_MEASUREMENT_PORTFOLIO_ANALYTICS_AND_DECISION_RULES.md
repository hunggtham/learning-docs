# 04 — Đo lường rủi ro, Portfolio Analytics và quy tắc ra quyết định

Tài liệu này xây lớp định lượng giữa “hiểu diversification” và khả năng thực sự đo một portfolio. Mục tiêu không phải biến investing thành bài toán thuần toán học, mà giúp bạn hiểu mỗi metric đang đo điều gì, assumption nào nằm bên dưới, metric bỏ sót risk nào và cuối cùng nó phải thay đổi decision ra sao.

Một dashboard đầy số nhưng không dẫn tới decision rule chỉ là decoration. Analytics chỉ có giá trị khi nó giúp sizing, diversification, rebalancing, stress testing hoặc review tốt hơn.

## 1. Simple return

Nếu asset tăng từ 100 lên 110:

`Return = 110 / 100 - 1 = 10%`

Simple return phù hợp cho một period nhưng không thể cộng trực tiếp qua nhiều periods nếu capital compounding.

## 2. Arithmetic vs geometric return

Hai periods +10% rồi -10% có arithmetic average 0%, nhưng capital từ 100 → 110 → 99. Geometric return phản ánh compounding tốt hơn.

Với `n` periods:

`Geometric Return = [(1+r1)(1+r2)...(1+rn)]^(1/n) - 1`

Volatility càng lớn, gap giữa arithmetic và geometric average thường càng đáng kể.

## 3. CAGR

**Compound Annual Growth Rate (CAGR)** trả lời: nếu capital tăng đều mỗi năm với một rate cố định, rate nào nối beginning value với ending value?

`CAGR = (Ending / Beginning)^(1/Years) - 1`

CAGR tiện so long-term outcomes nhưng bỏ qua path và drawdown.

## 4. Log return

Log return là:

`ln(Pt / Pt-1)`

Nó có tính additive theo thời gian và được dùng nhiều trong quantitative finance. Với returns nhỏ, log return gần simple return. Retail investor không cần dùng log return trong mọi analysis, nhưng nên biết vì nhiều models/statistics dùng nó.

## 5. Nominal và real return

Nominal gain không đảm bảo purchasing power tăng. Gần đúng:

`Real Return ≈ Nominal Return - Inflation`

Công thức chính xác:

`Real Return = (1 + Nominal Return)/(1 + Inflation) - 1`

Long-term goals nên đánh giá bằng real wealth.

## 6. Time-Weighted Return và Money-Weighted Return

**TWR** loại bớt ảnh hưởng timing của deposits/withdrawals và phù hợp đánh giá manager/strategy. **MWR/IRR** phản ánh trải nghiệm tiền thật vì cash flow timing matter.

Một investor có thể dùng fund tốt nhưng personal MWR thấp nếu nạp nhiều tiền đúng peak.

## 7. Volatility

Volatility thường là standard deviation của returns. Nó đo dispersion quanh mean, không phải probability permanent loss.

Daily volatility có thể annualize gần đúng bằng nhân `√252` nếu assumptions tương đối ổn. Nhưng volatility clustering và non-normal returns làm simple scaling không hoàn hảo.

## 8. Volatility clustering

Markets thường có quiet periods nối tiếp quiet periods và turbulent periods nối tiếp turbulent periods. Volatility không constant.

Đây là reason rolling volatility hoặc EWMA/GARCH-style thinking hữu ích hơn một long-run average duy nhất.

## 9. Downside deviation

Downside deviation chỉ penalize returns dưới threshold, thường là zero hoặc minimum acceptable return.

Nó phản ánh investor intuition tốt hơn trong một số cases vì upside surprise không bị coi là risk giống downside.

## 10. Drawdown

Drawdown đo decline từ prior peak:

`Drawdown = Current Value / Previous Peak - 1`

Maximum Drawdown là deepest observed decline. Nhưng historical max drawdown không phải worst possible future drawdown.

## 11. Recovery math

Loss và recovery không đối xứng:

`-10% → +11.1%`

`-25% → +33.3%`

`-50% → +100%`

`-80% → +400%`

Đây là lý do deep drawdown phá compounding và psychology.

## 12. Drawdown duration

Không chỉ depth mà **time under water** cũng quan trọng. Strategy -15% nhưng recover sau 2 tháng khác strategy -15% nhưng mất 5 năm mới lập high mới.

Investor horizon và patience phải match drawdown duration distribution.

## 13. Covariance

Covariance đo hai return series có move cùng nhau không và kết hợp scale volatility. Nó là building block của portfolio variance.

Do units khó intuitive, correlation thường dễ interpret hơn.

## 14. Correlation

Correlation chuẩn hóa covariance vào range -1 tới +1. Nhưng correlation gần zero không nghĩa assets independent; nonlinear/tail dependence vẫn có thể tồn tại.

Correlation còn state-dependent, thường tăng giữa risky assets khi crisis.

## 15. Portfolio variance

Với hai assets:

`σp² = wA²σA² + wB²σB² + 2wAwBσAσBρAB`

Term correlation giải thích diversification. Asset volatility cao vẫn có thể giảm portfolio risk nếu correlation sufficiently low.

## 16. Marginal Contribution to Risk

**MCTR** hỏi: tăng weight asset thêm một lượng nhỏ sẽ làm total portfolio risk thay đổi bao nhiêu?

Nó hữu ích hơn nhìn standalone volatility khi portfolio đã có nhiều correlated holdings.

## 17. Component Risk Contribution

Component contribution thường kết hợp weight với marginal risk. Tổng contributions cộng lại total portfolio volatility theo một số formulations.

Điều này giúp biết 10% thematic allocation có đang đóng góp 30% risk hay không.

## 18. Concentration metrics

Weight lớn nhất là simplest concentration metric. Có thể thêm **Herfindahl-Hirschman Index (HHI)**:

`HHI = Σ wi²`

HHI cao nghĩa capital concentrated. Nhưng HHI không capture correlation/factor overlap, nên chỉ là first layer.

## 19. Effective number of positions

Một intuition từ HHI là `1/HHI`. Equal-weight 10 positions cho effective number gần 10; concentrated portfolio thấp hơn.

Tuy nhiên factor concentration có thể làm effective economic diversification thấp hơn nhiều.

## 20. Beta

Beta gần bằng:

`β = Cov(asset, market) / Var(market)`

Beta >1 nghĩa historical sensitivity với benchmark cao hơn. Nhưng beta phụ thuộc sample, benchmark và regime.

## 21. Alpha

Trong simple CAPM framing, alpha là return unexplained by market beta. Nhưng practical alpha attribution cần account for sector, size, value, momentum, quality và currency factors.

Nếu benchmark miss relevant factors, “alpha” có thể chỉ là hidden exposure.

## 22. R-squared

R² cho biết proportion of return variation được regression benchmark/factors giải thích.

Low R² làm beta/alpha estimates less informative vì model explain little of asset behavior.

## 23. Multi-factor exposure

Portfolio equity returns có thể regress lên market, size, value, momentum hoặc quality factors. Bond portfolios thêm duration/credit factors.

Factor decomposition giúp nhìn through ticker wrappers và detect duplicated bets.

## 24. Tracking Error

Tracking error là standard deviation của active return `Portfolio - Benchmark`.

High TE nghĩa result có thể lệch benchmark nhiều, không tự động good/bad. Nó phải phù hợp mandate.

## 25. Information Ratio

`Information Ratio = Active Return / Tracking Error`

IR đo efficiency của active risk. Một manager outperform 2% với tiny tracking error khác manager outperform 2% nhưng huge deviations.

## 26. Active Share

Active Share đo holding weights khác benchmark đến đâu. Nó không capture derivatives perfectly và không nói active bets có skill.

Use Active Share cùng tracking error để hiểu nature of active management.

## 27. Sharpe Ratio

`Sharpe = (Portfolio Return - Risk-free Rate) / Volatility`

Sharpe hữu ích để compare risk-adjusted returns nhưng penalize upside/downside equally và dễ bị fooled bởi negative-skew strategies.

## 28. Sortino Ratio

`Sortino = Excess Return / Downside Deviation`

Sortino useful khi investor chỉ care downside variability. Nhưng threshold choice ảnh hưởng result.

## 29. Calmar Ratio

`Calmar = CAGR / Max Drawdown`

Calmar intuitive cho strategies nơi drawdown là practical constraint. Nhưng max drawdown is sample-specific and unstable.

## 30. Omega Ratio

Omega so probability-weighted gains above threshold với losses below threshold. Nó capture distribution beyond mean/variance nhưng less intuitive.

Không cần dùng mọi metric; mục tiêu là hiểu distribution shape.

## 31. Skewness

Positive skew: many small losses, occasional big wins. Negative skew: many small wins, occasional big crash.

Short-option/carry strategies thường negative skew. Trend following có thể more positive skew.

## 32. Kurtosis và fat tails

Financial returns often show more extreme observations than normal distribution. Normal-model probability can underestimate crises.

Stress tests và Expected Shortfall vì vậy quan trọng.

## 33. Value at Risk

VaR estimate loss threshold tại confidence level/horizon. Ví dụ one-day 95% VaR 2% nghĩa model estimate 95% days loss không vượt 2%.

VaR không nói tail beyond threshold và phụ thuộc distribution assumptions.

## 34. Historical, parametric và Monte Carlo VaR

Historical VaR dùng empirical past moves. Parametric VaR assume distribution/model. Monte Carlo VaR simulate many scenarios.

Mỗi method có model risk khác. Không method nào “truth”.

## 35. Expected Shortfall

**Expected Shortfall (ES/CVaR)** đo average loss conditional on being beyond VaR threshold.

Nó better captures tail severity nhưng vẫn dependent on model/data.

## 36. Liquidity-adjusted risk

A 5% modeled loss assumes you can exit near price. Illiquid asset may suffer additional spread/market impact.

Risk analytics nên include days-to-liquidate, ADV participation và stressed spreads for large positions.

## 37. Gap risk

Stops không guarantee loss cap because market can gap through stop level. Overnight, earnings, geopolitical events và illiquid markets create gap risk.

Scenario analysis must include discontinuous moves, not only smooth volatility.

## 38. Leverage-adjusted risk

Leverage scales notional and magnifies drawdown. Margin requirements can increase exactly when volatility rises.

A leveraged portfolio needs buffer above minimum margin; otherwise analytics that ignore liquidation path are incomplete.

## 39. Efficient Frontier

Mean-variance optimization identifies portfolios efficient under assumed expected returns/covariance. Conceptually important, practically fragile.

Expected returns are noisy; small input changes can create extreme weight changes.

## 40. Minimum-variance portfolio

Minimum variance avoids expected-return estimates and only uses covariance, reducing one source of error. But covariance itself is unstable and may overweight low-vol assets for structural reasons.

Constraints are necessary.

## 41. Maximum Sharpe portfolio

The tangency portfolio maximizes expected excess return per volatility under model assumptions. In practice output is highly sensitive to estimated returns.

Treat as analytical reference, not automatic allocation.

## 42. Shrinkage

**Shrinkage** blends noisy covariance/return estimates toward more stable target. It reduces estimation error.

You do not need implement advanced math to learn lesson: extreme estimates deserve skepticism.

## 43. Robust optimization

Robust portfolio construction uses weight bounds, turnover limits, uncertainty ranges and simpler priors to avoid optimizer extremes.

The best mathematical optimum on estimated inputs may be worse than a slightly suboptimal but robust allocation.

## 44. Scenario analysis

Scenarios specify coherent shocks: growth recession, inflation resurgence, USD spike, oil supply shock, liquidity crisis.

Map shock → rates/FX/spreads → assets. This preserves economic causality better than arbitrary percentage changes alone.

## 45. Historical stress tests

Replaying 2008, 2020 or a rate shock can reveal sensitivity. But portfolio composition and market structure today differ, so historical replay is not forecast.

Use history as mechanism library.

## 46. Hypothetical stress tests

Create shocks not yet seen together, e.g. stocks -25%, long yields +150 bps, KRW +10% versus USD and credit spreads +300 bps.

The goal is survival assessment, not probability prediction.

## 47. Sensitivity analysis

Sensitivity isolates one variable: what if rates +100 bps, USD/KRW -5%, earnings -15%?

It helps identify dominant drivers before complex scenario combinations.

## 48. Rolling analytics

Use rolling 3m/12m volatility, beta, correlation or Sharpe to see stability. Structural shifts often appear as metric drift.

But rolling metrics are backward-looking and can react late.

## 49. Downside capture và upside capture

Capture ratios compare portfolio performance in benchmark down/up periods. They help understand asymmetric behavior.

A defensive strategy may underperform bull markets but protect more in down markets.

## 50. Breadth and contribution analysis

Portfolio return dominated by one position is less robust than return spread across holdings. Contribution-to-return reports help detect hidden dependency.

Risk contribution and return contribution should be viewed together.

## 51. Forecast error as a risk metric

If thesis depends on revenue/margin forecasts, track forecast error over time. Large systematic optimism is a model/process risk.

Investor calibration belongs in portfolio analytics too.

## 52. Decision thresholds

Analytics become actionable through thresholds: concentration cap, drawdown review level, rebalance band, liquidity minimum, max currency mismatch or leverage cap.

Thresholds should be set ex ante, not after loss.

## 53. Bayesian updating intuition

New information should update belief, not flip thesis from 0 to 100. Start with prior probability and revise based on evidence strength.

This mindset reduces overreaction to single data points.

## 54. Base-rate thinking

Before forecasting a rare event, ask historical/base frequency. Narrative-specific evidence should be weighed against base rates.

This guards against vivid-story bias.

## 55. Dashboard design

A useful dashboard should display only metrics linked to decisions: allocation, contribution, drawdown, liquidity, currency, factor exposure, realized volatility and thesis flags.

More charts do not necessarily improve decisions.

## 56. Portfolio review

A review should answer: what drove return, what drove risk, where concentration changed, what assumptions changed, and which action—if any—is justified.

If analytics cannot answer those questions, redesign analytics rather than add more metrics.

## 57. Kết luận

Risk measurement is model-assisted judgment, not truth extraction. Every metric compresses reality and carries assumptions.

The professional habit is to combine quantitative measures with economic mechanism, liquidity, scenario analysis and predefined decision rules. The objective is not a perfect risk number; it is fewer preventable mistakes.