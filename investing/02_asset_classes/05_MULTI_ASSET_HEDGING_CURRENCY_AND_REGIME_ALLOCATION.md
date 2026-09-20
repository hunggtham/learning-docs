# 05 — Multi-Asset, Hedging, Currency và Regime Allocation

> Multi-asset investing không phải mua thật nhiều sản phẩm. Nó là quá trình phân bổ **economic exposures** giữa growth, inflation, duration, credit, liquidity, FX, commodities và volatility sao cho portfolio có thể sống qua nhiều states của thế giới. Chapter này nối asset-class knowledge với portfolio construction, hedging, liability matching, stress testing và regime-aware allocation.

## 1. Multi-Asset khác Multi-Product

Portfolio có 12 ETFs vẫn có thể rất concentrated nếu tất cả cùng long US growth, long duration hoặc long USD.

Diversification thật cần nhìn xuyên product label tới economic driver. Một semiconductor ETF, Nasdaq ETF và growth fund có thể là ba tickers nhưng gần như cùng risk factor.

Vì vậy bước đầu luôn là **look-through exposure**, không phải đếm số positions.

## 2. Portfolio là một hệ thống Sensitivities

Có thể map mỗi sleeve theo các dimensions:

```text
Growth beta
Inflation beta
Real-rate duration
Credit beta
FX exposure
Commodity exposure
Liquidity sensitivity
Volatility / convexity
```

Cùng một asset có thể mang nhiều sensitivities. REIT vừa là equity beta, vừa rate-sensitive, vừa property/funding exposure.

## 3. Growth–Inflation Matrix

Một framework đơn giản là hai trục growth và inflation.

Growth ↑ / Inflation ổn thường thuận cho equities/credit. Growth ↓ / Inflation ↓ thường thuận cho high-quality duration. Growth ↑ / Inflation ↑ có thể thuận cyclicals/commodities nhưng gây pressure discount rate. Growth ↓ / Inflation ↑ là stagflation, thường khó cho cả stocks lẫn long bonds.

Framework này không phải signal cơ học. Starting valuation, policy response và shock source luôn quan trọng.

## 4. Regime là Probability Distribution

Không nên nói “đang ở stagflation” như một certainty. Regime allocation tốt hơn khi dùng probability distribution giữa soft landing, reacceleration, recession, inflation resurgence hoặc liquidity shock.

Allocation vì vậy thường là **tilt quanh strategic policy**, không phải all-in theo một forecast.

## 5. Duration xuyên Asset Classes

Duration không chỉ tồn tại trong bonds. Growth equities, long-lease assets, infrastructure và một số private assets cũng có long-duration economics.

Khi real yields tăng mạnh, long Treasuries và expensive growth stocks có thể giảm cùng lúc. Đây là hidden concentration phổ biến của “60/40-like” portfolios.

## 6. Credit beta không chỉ nằm trong Bonds

High-yield credit, leveraged loans, private credit, REITs và highly leveraged equities đều nhạy với refinancing conditions.

Trong downturn, risky credit thường behave equity-like vì spread widening và default expectations dominate falling risk-free rates.

Một defensive allocation phải phân biệt **sovereign duration** với **corporate credit**.

## 7. Inflation Exposure phải phân loại Shock

Demand-driven inflation và supply-driven inflation cho asset reactions khác nhau.

Commodity producers có thể hưởng demand boom, nhưng supply shock có thể làm economy yếu hơn. TIPS hedge inflation index nhưng vẫn chịu real-yield duration. Gold nhạy real yields/USD. REITs cần rent pass-through nhanh hơn financing cost.

Không có một universal inflation hedge.

## 8. Liquidity là một Asset Class-like Resource

Cash không chỉ là low-return asset. Nó là khả năng thanh toán liabilities, margin calls và rebalance khi others bị forced sellers.

Liquidity có option value: một portfolio không bị buộc bán ở đáy có thể compound tốt hơn portfolio có expected return cao nhưng liquidity thấp.

## 9. Cash Optionality và Opportunity Cost

Cash chịu inflation drag và opportunity cost trong bull markets, nhưng giúp portfolio survive. Tỷ trọng cash hợp lý phụ thuộc near-term liabilities, funding uncertainty và rebalancing policy.

Cash held vì plan khác cash held vì panic. Strategic liquidity phải được định nghĩa trước crisis.

## 10. Currency là một Exposure độc lập

Home-currency return:

```text
(1 + Local Asset Return) × (1 + FX Return) - 1
```

Korean investor mua US equity unhedged đang long US equity + long USD/KRW. Nếu KRW mạnh, FX có thể erase phần lớn USD asset gain.

## 11. Trading, Underlying, Reporting và Liability Currency

Trading currency là currency giao dịch. Underlying currency là currency của economic cash flows. Reporting currency là currency app dùng hiển thị. Liability currency là currency bạn cần để chi tiêu tương lai.

Nhầm bốn khái niệm này là nguồn lỗi lớn trong cross-border allocation.

## 12. Natural Hedge

Nếu future liability bằng USD, USD assets có thể tự nhiên hedge liability. Nếu goal là mua nhà ở Korea, near-term KRW liabilities nên được matched bằng KRW liquid assets nhiều hơn.

Natural hedge thường tốt hơn speculative FX timing vì nó trực tiếp giảm mismatch.

## 13. Hedged vs Unhedged Foreign Assets

Currency hedge giảm một phần FX volatility nhưng tạo forward/carry/basis/transaction costs.

Unhedged exposure có thể diversify domestic currency risk, đặc biệt khi USD mạnh trong global risk-off. Vì vậy “hedged luôn an toàn hơn” là sai.

## 14. Covered Interest Parity và Forward Points

FX forwards phản ánh interest-rate differential theo arbitrage logic, cộng basis/frictions.

Hedge cost không phải simple fee. Khi US rates cao hơn Korea rates, rolling USD hedge back to KRW có economics khác hẳn khi rate differential đảo chiều.

Đây là lý do hedged vs unhedged ETF relative return thay đổi theo rate regime.

## 15. Strategic Hedge Ratio

Hedge ratio có thể 0%, 50%, 100% hoặc dynamic. Strategic ratio nên dựa liability currency, horizon và tolerance với FX volatility.

Near-term known liabilities thường justify higher hedge ratio; long-horizon growth assets có thể để unhedged nhiều hơn nếu currency diversification có giá trị.

## 16. Dynamic FX Hedging

Dynamic hedge thay ratio theo valuation, volatility hoặc macro. Nó có thể giảm risk nhưng cũng tạo turnover/model risk và nguy cơ timing sai.

Nếu process không rõ, static policy + rebalancing bands thường robust hơn discretionary FX forecasting.

## 17. Equity Beta Hedging bằng Futures

Approximate hedge:

```text
Contracts ≈ Portfolio Value × Portfolio Beta / Futures Notional
```

Nhưng beta thay đổi theo regime; sector mismatch tạo basis risk. Hedge broad index cho concentrated sector book không neutralize idiosyncratic/sector risk.

## 18. Options Hedging

Protective put giữ upside nhưng có premium drag. Put spread giảm cost nhưng protection bị capped. Collar tài trợ put bằng bán call và từ bỏ một phần upside.

Hedge design phải trả lời: cần giảm variance, cap max loss hay protect một event cụ thể?

## 19. Tail Hedging

Tail hedge có negative carry trong normal periods nhưng convex payoff trong crash.

Đánh giá tail hedge ở portfolio level: nếu nó giúp tránh forced selling hoặc giữ khả năng rebalance, value của hedge lớn hơn standalone hedge P/L.

## 20. Hedge Budget

Insurance không miễn phí. Có thể định nghĩa annual hedge budget, ví dụ phần trăm NAV tối đa dành cho option premium.

Budget buộc investor so protection quality với bleed cost và tránh mua expensive protection sau volatility spike.

## 21. Hedge Effectiveness

Một hedge tốt phải được đo bằng change in portfolio risk, không bằng “hedge riêng có lời không”.

Metrics có thể gồm beta reduction, drawdown reduction, Expected Shortfall reduction hoặc liability mismatch reduction.

Nếu hedge gain +5% nhưng underlying loss -20%, câu hỏi là total portfolio có đáp ứng objective không.

## 22. Basis Risk

Hedge hiếm khi match hoàn hảo underlying. Korean semiconductor basket hedge bằng KOSPI futures còn residual sector risk. Jet fuel hedge bằng crude futures còn crack-spread risk.

Basis risk phải được xem như remaining position.

## 23. 60/40 Portfolio

60/40 dựa equity growth + bond duration diversification. Nó hoạt động tốt nhất khi growth shocks dominate và stock-bond correlation thấp/âm.

Trong inflation shock, both can decline. Lesson là correlation regime changes, không phải framework luôn sai.

## 24. Risk Parity

Risk parity phân bổ theo risk contribution thay vì capital. Vì bonds có volatility thấp, portfolio có thể leverage duration để equalize risk.

Weakness xuất hiện khi bond volatility/correlation jump. Leverage biến “low-vol asset” thành major loss contributor.

## 25. Equal Risk Contribution

Nếu portfolio volatility là `σ_p`, risk contribution của asset phụ thuộc weight, covariance và total volatility.

Một 10% commodity allocation có thể đóng góp nhiều risk hơn 30% bonds. Vì vậy capital weight không đủ để hiểu portfolio construction.

## 26. Marginal Risk Contribution

**Marginal Risk Contribution (MRC)** hỏi total risk thay đổi bao nhiêu nếu tăng một chút weight asset đó.

Nó hữu ích để phát hiện asset tưởng nhỏ nhưng covariance với portfolio rất cao.

Portfolio review nên nhìn both weight và risk contribution.

## 27. Diversification Ratio

Một intuition useful:

```text
Diversification Ratio ≈ Weighted Average Asset Vol / Portfolio Vol
```

Ratio cao hơn cho thấy covariance structure đang giúp giảm total risk. Nhưng historical covariance có thể break trong stress, nên ratio chỉ là one diagnostic.

## 28. Correlation Regime

Average correlation che giấu downside correlation. Stocks và bonds có thể correlation âm trong disinflation regime nhưng dương trong inflation tightening.

Stress correlations nên được estimated/assumed riêng cho crisis scenarios.

## 29. Correlation Breakdown do Deleveraging

Trong margin shock, unrelated assets có thể bị bán để raise cash. Correlations tăng không phải vì fundamentals giống nhau mà vì funding constraint chung.

Liquidity/funding factor vì vậy là một hidden common factor trong diversified portfolios.

## 30. Trend Following như Crisis Diversifier

Trend strategies có thể long hoặc short equities, bonds, FX, commodities. Chúng có potential diversify persistent bear moves.

Nhưng sudden reversal/range market gây whipsaw. Trend không phải instant hedge; nó cần time để detect and position.

## 31. Carry như Risk Premium

FX carry, credit carry, commodity roll carry và short-vol premium thường earn small gains in stable regimes nhưng suffer during stress.

Nếu nhiều sleeves đều earn carry, portfolio có thể hidden short-volatility dù asset labels khác nhau.

## 32. Gold

Gold exposure thường liên quan real yields, USD, central-bank demand và monetary/geopolitical confidence.

Nó có thể diversify some crises nhưng không luôn rise immediately; liquidity stress có thể cause temporary selling.

Portfolio role của gold nên được defined as monetary/real-yield diversifier, không là “asset luôn tăng khi stock giảm”.

## 33. Commodities

Commodity futures provide inflation/supply-shock sensitivity nhưng return gồm spot change + roll + collateral yield.

Broad commodity basket có sector weights và methodology riêng. Energy-heavy index khác diversified index rất nhiều.

## 34. REIT và Infrastructure

REITs có real-asset cash flows nhưng listed-equity beta và financing sensitivity. Infrastructure có long contracts nhưng regulatory/capex/rate risk.

Asset label “real asset” không remove duration/refinancing risk.

## 35. Private Markets và Stale Pricing

Private equity/credit/real estate NAVs update slowly. Reported volatility và correlation thường understated.

Portfolio optimization dùng raw private NAV data có thể overallocate illiquid assets vì model mistakenly treats stale marks as stability.

## 36. Liquidity-Adjusted Allocation

Risk budget cần thêm liquidity dimension. Một asset chỉ có 5% volatility nhưng không bán được 3 tháng có thể nguy hiểm hơn liquid asset 12% volatility nếu liability đến trong 2 tuần.

Liquidity buckets nên map time-to-cash under stress.

## 37. Leverage Overlay

Portfolio leverage làm small estimation errors trở nên lớn. Risk parity, futures overlays hoặc margin borrowing cần stress funding rate, margin increase và correlation jump.

Leverage policy nên có hard limits và liquidity buffer trước khi dùng.

## 38. Volatility Targeting

Vol targeting scale exposure inverse với estimated volatility để stabilize total risk.

Weakness: vol estimate lagging. Calm market trước shock có thể imply maximum leverage đúng lúc risk sắp tăng. Sau crash, model de-risk muộn và có thể sell low.

## 39. Strategic Asset Allocation

Strategic allocation phản ánh goals, horizon, liabilities và long-run risk tolerance/capacity.

Nó nên thay đổi chậm. Strategic policy là anchor để investor không chase recent winners.

## 40. Tactical Asset Allocation

Tactical allocation thay weights quanh allowed ranges dựa valuation, macro, positioning hoặc market dislocation.

Tactical decision chỉ hợp lý nếu process, horizon và evidence rõ. Nếu không, nó dễ trở thành disguised market timing.

## 41. Regime Probability Allocation

Thay vì một forecast, assign probabilities cho multiple states. Ví dụ soft landing 45%, recession 30%, inflation resurgence 25%.

Portfolio có thể tilt toward base case nhưng maintain protection for alternatives. Objective là robustness, không phải maximum payoff if one forecast happens.

## 42. Valuation Overlay

Macro regime đúng nhưng valuation quá expensive vẫn có poor expected return.

Allocation cần kết hợp:

```text
Regime Probability
× Expected Cash Flows
× Starting Valuation
× Portfolio Role
```

Valuation là bridge giữa macro view và expected return.

## 43. Expected Return Building Blocks

Equity expected return có thể decompose earnings growth + shareholder yield + multiple change. Bonds: carry + roll + rate/spread move. Commodities: spot + roll + collateral yield. FX: spot + carry.

Building-block forecasts buộc assumptions minh bạch hơn black-box optimization.

## 44. Optimization và Estimation Error

Mean-variance optimization cực nhạy với expected-return assumptions. Small change in input có thể tạo huge weight differences.

Covariance estimates cũng unstable. Optimization output nên được constrained/shrunk và dùng như decision support, không oracle.

## 45. Robust Portfolio Construction

Robust methods có thể dùng weight caps, minimum diversification, shrinkage covariance, scenario stress và qualitative risk limits.

Goal không phải mathematically optimal portfolio trên historical sample mà portfolio survivable khi inputs sai.

## 46. Rebalancing Bands

Threshold/band rebalancing giảm turnover so calendar-only approach. Example target 20% với allowed 17–23%.

Band size nên reflect volatility, transaction cost, tax và liquidity.

New cash flows có thể rebalance mà không cần sell assets.

## 47. Rebalancing Premium và Limits

Rebalancing có thể buy low/sell high trong mean-reverting relative moves, nhưng không guaranteed premium.

Nếu asset structurally impaired, mechanical buy-down can compound loss. Rebalancing rule cần governance: distinguish price move from thesis break.

## 48. Liability-Driven Investing

Portfolio không tồn tại độc lập với obligations. Near-term tuition, housing deposit hay debt repayment nên được matched bằng currency, duration và liquidity phù hợp.

Growth assets phục vụ long horizon; liability-matching assets phục vụ certainty. Mixing hai objectives gây forced selling.

## 49. Human Capital

Career income là implicit asset. Developer trong tech/finance có human capital correlated với tech/financial cycle.

Financial portfolio có thể diversify away from employer/industry risk thay vì double down cùng factor.

## 50. Household Balance Sheet

Real estate, pension, debt, salary và family liabilities đều là portfolio exposures.

Nếu household wealth đã concentrated Korea real estate + KRW income, global assets có diversification value. Nếu future liabilities mostly KRW, foreign allocation vẫn cần FX policy.

## 51. Multi-Country Liabilities

Household có goals ở Korea và Vietnam cần currency buckets riêng. Liability matching có thể giảm FX risk mà không cần forecast VND/KRW.

Policy nên define minimum assets/liquidity theo từng goal currency.

## 52. Stress Testing

Stress ít nhất:

```text
Inflation Shock
Recession / Deflation
USD Spike
Rate +200 bps
Credit Spread Blowout
Commodity Supply Shock
Stock-Bond Correlation +0.7
Liquidity Freeze
FX +15% against Home Currency
```

Stress test phải include margin/collateral and time-to-liquidate, không chỉ price P/L.

## 53. Reverse Stress Test

Reverse stress hỏi: “Portfolio phải gặp combination shock nào để drawdown 25% hoặc violate liquidity requirement?”

Cách này giúp phát hiện hidden risk mà normal scenario set bỏ sót.

## 54. Scenario Probability không phải Precision

Gán probability giúp explicit thinking, nhưng 35% không scientific hơn 30% nếu evidence yếu.

Quan trọng là identify outcomes, transmissions và portfolio sensitivity, không tạo false precision.

## 55. Performance Attribution

Sau period, tách return thành strategic allocation, tactical tilts, security/product selection, FX, hedges, fees và rebalancing.

Nếu portfolio outperform chỉ vì unhedged USD mạnh, đừng nhầm với stock-selection skill.

## 56. Risk Attribution

Return attribution nhìn backward; risk attribution nhìn forward. Asset đóng góp ít return nhưng nhiều Expected Shortfall có thể không đáng giữ.

Review both return contribution và risk contribution theo sleeve/factor.

## 57. Product Implementation

Sau khi quyết định exposure mới chọn ETF, fund, futures hoặc direct securities.

Implementation checklist: tracking, expense, spread, taxes, FX conversion, leverage reset, collateral, securities lending và counterparty.

Economic thesis tốt vẫn có thể bị wrapper tệ làm giảm realized return.

## 58. Governance của Portfolio

IPS nên define strategic weights/ranges, hedge policy, liquidity floor, leverage cap, rebalancing rules và decision authority.

Predefined governance giảm behavior drift khi market volatile.

## 59. Portfolio Construction Workflow

```text
Goals
→ Liabilities
→ Liquidity Floor
→ Strategic Exposures
→ Risk Budgets
→ Currency Policy
→ Stress Tests
→ Product Selection
→ Rebalancing Rules
→ Performance/Risk Attribution
→ Annual Review
```

Bắt đầu từ goals giúp tránh portfolio trở thành collection của market narratives.

## 60. Checklist trước khi thêm Asset

Hỏi: return driver là gì; factor nào duplicate; hedge risk nào; stress loss; liquidity; currency; cost; tax; expected return; rebalancing rule; invalidation condition.

Nếu không thể giải thích portfolio role trong một đoạn ngắn, position có thể không cần thiết.

## 61. Mental Model cuối cùng

```text
Economic Regimes
→ Asset Sensitivities
→ Liabilities
→ Risk Contributions
→ Currency / Liquidity Policy
→ Hedging
→ Strategic + Tactical Allocation
→ Implementation
→ Stress / Attribution
→ Governance
```

Multi-asset investing là quản lý một system of risks, không phải chọn nhiều tickers. Portfolio tốt không cần đúng mọi forecast; nó cần đủ robust để survive khi forecast sai.