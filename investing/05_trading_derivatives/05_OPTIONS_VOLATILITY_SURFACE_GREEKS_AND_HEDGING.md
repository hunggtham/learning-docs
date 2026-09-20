# 05 — Options, Volatility Surface, Greeks và Hedging Chuyên Sâu

> Options không chỉ là công cụ “đoán tăng hay giảm”. Chúng là hợp đồng chuyển risk giữa các bên và định giá đồng thời direction, time, volatility, skew, interest rate, dividend, jump risk và liquidity. Chapter này xây từ payoff cơ bản tới volatility surface, Greek interactions, hedging và research workflow để người đọc hiểu vì sao một position có thể đúng direction nhưng vẫn lỗ, và vì sao option premium cao luôn phản ánh risk được chuyển sang ai đó.

## 1. Option là quyền, không phải nghĩa vụ đối với buyer

Buyer của call có quyền mua underlying tại strike trước/đúng expiry tùy exercise style. Buyer của put có quyền bán. Buyer trả premium để mua convexity; seller nhận premium và chấp nhận obligation.

Điều quan trọng là option không tạo return từ hư không. Premium là price của risk transfer. Nếu một investor muốn downside protection, một bên khác phải sẵn sàng bán protection với compensation đủ hấp dẫn.

## 2. Payoff tại expiry khác P/L trước expiry

Payoff chart thường vẽ tại expiry, nhưng live option price trước expiry còn time value và IV. Long call có thể đang lãi dù spot dưới strike nếu IV tăng mạnh và còn nhiều time. Ngược lại call có thể lỗ dù spot tăng nếu IV collapse và theta decay lớn.

Vì vậy trader phải phân biệt **terminal payoff** với **mark-to-market path**.

## 3. Intrinsic Value

Call intrinsic value:

```text
max(S - K, 0)
```

Put intrinsic value:

```text
max(K - S, 0)
```

Premium vượt intrinsic value là **extrinsic/time value**. Extrinsic value giảm về zero khi expiry đến, nhưng tốc độ giảm không tuyến tính.

## 4. Moneyness

ITM, ATM và OTM là mô tả vị trí strike so với spot/forward. Moneyness ảnh hưởng Delta, Gamma, Vega và probability distribution implied by market.

ATM options thường có Gamma cao gần expiry; longer-dated ATM options thường có Vega lớn hơn vì volatility assumption tác động trên horizon dài hơn.

## 5. Forward Price quan trọng hơn Spot trong Pricing

Option pricing thường liên hệ với forward price chứ không chỉ spot. Interest-rate differential, dividends hoặc carry làm forward khác spot.

Với equity index, expected dividends ảnh hưởng fair forward. Với FX, domestic/foreign rates quyết định forward points. Vì vậy cùng spot price nhưng rate/carry khác có thể làm option surface khác.

## 6. Put–Call Parity

Một relationship cơ bản nối call, put, spot/forward và present value của strike. Intuition là nếu hai portfolios tạo cùng terminal payoff thì arbitrage sẽ ép giá gần nhau sau khi tính funding/dividends.

Parity giúp nhìn options như building blocks và phát hiện synthetic positions.

## 7. Synthetic Long và Synthetic Short

Long call + short put cùng strike/expiry tạo exposure gần synthetic long forward. Short call + long put tạo synthetic short.

Điều này cho thấy option strategy names không phải magic; nhiều structures chỉ là cách tái đóng gói direction, carry và convexity.

## 8. Delta

**Delta** là first-order sensitivity của option price với spot/forward. Nó cho biết position behaves approximately như bao nhiêu units underlying cho một small move.

Delta không cố định. Khi spot, IV và time thay đổi, delta cũng đổi. Vì vậy option không thể được quản lý như static stock exposure.

## 9. Delta không phải “xác suất thật”

Delta đôi khi được dùng như rough proxy cho probability kết thúc ITM trong một số model assumptions, nhưng đó không phải objective real-world probability.

Risk-neutral pricing measure, skew và carry khiến interpretation phức tạp hơn. Dùng delta như risk sensitivity trước, probability proxy sau.

## 10. Gamma

**Gamma** đo tốc độ Delta thay đổi khi underlying move. Long option thường long gamma; short option thường short gamma.

Long gamma hưởng lợi từ large realized movement vì delta tự tăng theo hướng có lợi. Short gamma có profile ngược lại: position trở nên more wrong khi spot chạy xa.

## 11. Gamma Concentration gần Expiry

ATM gamma thường tăng mạnh khi expiry tới. Điều này khiến short-dated options cực nhạy với small spot changes.

Trader thấy option premium nhỏ có thể tưởng risk nhỏ, nhưng gamma near expiry có thể làm P/L biến động nhanh hơn kỳ vọng.

## 12. Theta

**Theta** là sensitivity với passage of time khi các yếu tố khác giữ nguyên. Long options thường negative theta vì optionality mất dần khi time window ngắn lại.

Short-option seller nhận theta nhưng không phải free yield. Theta là compensation cho gamma, gap và volatility risk.

## 13. Theta không giảm tuyến tính

Time decay thường accelerate gần expiry, đặc biệt với ATM options. Deep ITM/OTM profiles khác nhau.

Do đó “mỗi ngày mất cùng một amount theta” là simplification sai.

## 14. Vega

**Vega** đo sensitivity với implied volatility. Long options thường long vega, short options short vega.

Long-dated options thường có vega lớn vì thay đổi volatility assumption tác động lên nhiều time hơn.

## 15. Rho và Carry

**Rho** đo sensitivity với rates. Với short-dated equity options nó có thể nhỏ hơn Delta/Gamma/Vega, nhưng với LEAPS, FX options hoặc rates products có thể material.

Rates còn ảnh hưởng funding và forward price nên không nên coi option pricing tách khỏi macro rates.

## 16. Higher-order Greeks

Vanna đo interaction giữa delta và volatility; Volga/Vomma đo vega sensitivity với volatility; Charm đo delta decay theo time; Speed đo gamma change theo spot.

Retail investor không cần thuộc formula, nhưng cần hiểu first-order Greeks tự thay đổi. Một hedge “delta-neutral” hôm nay không guaranteed neutral ngày mai.

## 17. Greek Profile là vector risk

Một position nên được mô tả bằng profile: long/short Delta, Gamma, Vega, Theta và tail exposure.

Ví dụ long straddle gần ATM thường delta gần zero ban đầu nhưng long gamma, long vega và short theta. Khi spot move lớn, delta không còn zero.

## 18. Implied Volatility

**Implied Volatility (IV)** là volatility input khiến pricing model khớp market premium. Nó là price-implied parameter, không phải forecast chắc chắn.

IV chứa expected movement, insurance demand, risk premium, liquidity và supply/demand của options.

## 19. Realized Volatility

**Realized volatility (RV)** đo volatility thực tế của underlying qua price path. Có nhiều estimator: close-to-close, intraday, Parkinson, Yang-Zhang… nhưng concept quan trọng là realized movement sau khi trade xảy ra.

Core volatility trade thường hỏi: market đang price IV bao nhiêu và underlying có thể realize bao nhiêu sau costs/jumps?

## 20. Implied vs Realized không đủ để kết luận edge

IV cao hơn realized trung bình không có nghĩa short options luôn profitable. Difference có thể là compensation cho tail losses và crash correlation.

Một strategy kiếm small premium 99 ngày nhưng mất rất lớn ngày 100 cần đánh giá full distribution, không chỉ average spread IV-RV.

## 21. Volatility Risk Premium

Equity index downside protection thường được bid cao do institutional hedging demand. Đây là một nguồn **volatility risk premium**.

Nhưng premium tồn tại chính vì seller chịu negative convexity trong crisis. Risk premium và free alpha là hai khái niệm khác nhau.

## 22. Volatility Smile và Skew

Market IV không flat qua strikes. Equity indexes thường có downside put skew: OTM puts có IV cao hơn ATM/calls.

Skew phản ánh asymmetric crash risk, supply/demand và dealer balance sheet. Không nên đọc “skew cao = chắc chắn crash”.

## 23. Risk Reversal

Trong FX/options markets, difference giữa OTM call IV và put IV thường được mô tả bằng **risk reversal**. Nó cho biết market trả premium tương đối cho one-sided tail.

Risk reversal là price of asymmetry, không phải directional forecast độc lập.

## 24. Butterfly / Curvature

Ngoài slope skew, surface còn có curvature. Butterfly-style measures phản ánh wing IV so ATM.

Curvature quan trọng với strategies dùng multiple strikes như butterflies, condors và ratio spreads.

## 25. Term Structure

IV khác theo expiry. Short-dated IV chịu immediate event risk; long-dated IV phản ánh uncertainty dài hơn.

Normal term structure có thể upward sloping, nhưng event/crisis có thể invert khi front-end IV spike mạnh.

## 26. Event Volatility

Earnings, CPI, FOMC hoặc election có thể tạo discrete event variance. Expiry bao quanh event thường chứa premium cao hơn neighboring maturities.

Trader phải tách normal daily variance và event variance để tránh mua “high IV” mà không hiểu high vì event nào.

## 27. Implied Move

ATM straddle premium thường được dùng để ước lượng approximate implied move tới expiry/event. Nó không phải exact confidence interval.

Điểm quan trọng là market đã price movement nào. “Tôi nghĩ stock sẽ tăng” chưa đủ; cần hỏi expected magnitude có vượt move priced không.

## 28. Volatility Surface

**Volatility surface** là IV theo strike và maturity. Surface có thể shift, steepen, flatten hoặc twist.

Một strategy có thể đúng spot direction nhưng lỗ vì surface move bất lợi. Calendar spreads và ratio structures đặc biệt nhạy surface shape.

## 29. Sticky Strike và Sticky Delta Intuition

Different markets có empirical behavior khác khi spot move. Skew có thể giữ gần strike levels hoặc delta levels hơn tùy regime.

Không cần memorize rule; quan trọng là biết IV không dịch chuyển rigidly. Surface dynamics chính là một risk source.

## 30. Vol-of-Vol

IV itself biến động. **Volatility of volatility** quan trọng với vega-heavy strategies và long-dated options.

Khi crisis, spot vol và vol-of-vol có thể tăng cùng lúc, làm surface move nonlinear.

## 31. Long Call

Long call mua upside convexity với max loss premium. Nhưng expected return phụ thuộc strike/IV/time, không chỉ bullish view.

Deep OTM call rẻ theo dollars có thể rất đắt theo implied volatility và probability.

## 32. Long Put

Long put mua downside convexity. Nó có thể là directional bearish bet hoặc insurance cho existing asset.

Insurance hiệu quả phải xét cost over repeated periods, not one crisis payoff.

## 33. Vertical Spreads

Bull call, bear put, call credit và put credit spreads combine two strikes để reshape payoff.

Defined max loss không có nghĩa low risk nếu size quá lớn. Position size phải tính max loss và probability distribution.

## 34. Straddle và Strangle

Long straddle/strangle chủ yếu long movement/volatility; short structures short movement/convexity.

Long vol cần realized move đủ lớn và đúng timing. Short vol cần survive tails và margin expansion.

## 35. Butterfly và Condor

Butterfly/condor concentrate payoff around ranges/strikes. They can express view about distribution shape rather than simple direction.

But multiple legs add execution/slippage and assignment complexity.

## 36. Calendar và Diagonal Spreads

Calendars use different expiries; diagonals combine different strikes and expiries. They are bets on term structure, theta and relative vega as much as direction.

Backtesting them requires historical option surfaces, not just underlying candles.

## 37. Covered Call

Covered call = long underlying + short call. Premium reduces downside slightly but caps upside.

Economically it is partially short volatility/convexity. Calling it “passive income” hides what is being sold.

## 38. Protective Put

Long stock + long put creates downside floor. Cost is premium plus possible IV overpayment.

Hedge evaluation should compare protection efficiency, carry drag and trigger horizon.

## 39. Collar

Collar buys put and sells call. It finances insurance by giving up upside.

Zero-cost collar is not free; price is paid through foregone participation and strike constraints.

## 40. Ratio Spread

Ratio spreads use unequal option quantities and can create hidden naked exposure beyond certain spot levels.

Never infer risk from initial debit/credit alone. Plot full payoff and stress assignment.

## 41. Dispersion Intuition

Index volatility depends component volatilities and correlations. Dispersion strategies trade relationship between index options and single-stock options.

Conceptually useful because it shows correlation itself can be priced risk.

## 42. Gamma Scalping

A delta-hedged long-gamma position buys low/sells high mechanically as delta changes. Profitability depends realized volatility relative to implied plus transaction costs.

Continuous frictionless hedging is theoretical; real slippage and jumps matter.

## 43. Dynamic Delta Hedging

Rebalancing hedge frequency is trade-off. Too frequent raises cost; too infrequent leaves directional exposure.

In jump markets no feasible frequency removes gap risk completely.

## 44. Jump Risk

Earnings gaps, central-bank surprises and geopolitical shocks violate smooth-price assumptions. Short gamma can suffer loss before hedge executes.

Model max loss based only continuous diffusion can severely underestimate tail.

## 45. Volatility Clustering

High-volatility periods tend to cluster. IV and realized vol are regime dependent.

Option strategy tested only in calm years may be structurally biased. Stress multiple vol regimes.

## 46. Market Maker Hedging

Dealers hedge aggregate Delta/Gamma/Vega subject to inventory and risk limits. Hedging flows can affect short-term price dynamics.

But public estimates of “dealer gamma” are model-dependent. Treat them as context, not deterministic signal.

## 47. Open Interest

Open interest shows outstanding contracts, not whether participants are net bullish/bearish. Every contract has buyer and seller.

Strike concentration can matter operationally near expiry but should not be interpreted mechanically.

## 48. Volume, Spread và Depth

Option liquidity must be assessed by bid-ask, displayed size, underlying liquidity and ability to execute multi-leg order.

A theoretical edge smaller than spread/commission is not tradeable edge.

## 49. Early Exercise

American options can be exercised early. Deep ITM calls before ex-dividend dates and deep ITM puts under certain rate conditions may have early-exercise economics.

Short seller must understand assignment risk, not just terminal payoff.

## 50. Pin Risk

When spot closes near strike at expiry, assignment may be uncertain across contracts. After-hours moves can leave unexpected stock exposure.

Operational plan before expiry is essential.

## 51. Cash vs Physical Settlement

Index options may cash settle; equity options often settle shares. Settlement style affects capital needs and post-expiry exposure.

Contract specification should be read before trade, not after assignment.

## 52. Contract Multiplier

Quoted option price times multiplier determines cash premium/notional. Small quoted numbers can represent large exposure.

Always compute dollar Delta, dollar Gamma approximation and stress loss at portfolio level.

## 53. Dollar Delta

A practical risk metric:

```text
Dollar Delta ≈ Delta × Contract Multiplier × Underlying Price × Contracts
```

It translates option exposure into approximate underlying-equivalent dollars for small moves.

## 54. Gamma Exposure

Gamma tells how Delta changes. Portfolio with small current Delta but large short Gamma can become highly directional after a fast move.

This is why “delta-neutral” does not mean low risk.

## 55. Vega Exposure

Portfolio may be directionally hedged but heavily short Vega. A volatility spike can create loss even if spot barely moves.

Aggregate Greeks should be monitored across positions, not each trade in isolation.

## 56. Margin Risk

Short options may face margin requirement increase exactly when IV rises and equity drops. This creates liquidity/forced-liquidation risk beyond theoretical expiry max loss for uncovered positions.

Risk budget must include margin path.

## 57. Portfolio Hedging bằng Index Futures vs Options

Futures hedge beta cheaply and linearly but remove upside/downside symmetrically. Put options preserve upside but cost premium.

Choice depends whether goal is reduce beta, cap tail loss or protect a temporary event window.

## 58. Hedge Ratio

Approximation:

```text
Hedge Notional ≈ Portfolio Value × Portfolio Beta × Desired Hedge Fraction
```

But sector/basis mismatch means residual risk remains. A semiconductor portfolio hedged by broad index is not sector-neutral.

## 59. Basis Risk

**Basis risk** appears when hedge instrument does not perfectly match exposure. Cross-hedging Korea sector stock with KOSPI futures, or commodity producer with generic commodity future, leaves residual drivers.

Perfect hedge often does not exist; goal is reduce chosen risk dimension.

## 60. FX Options

FX options price relative rates, spot/forward and currency-specific skew. Corporate/investor hedger can buy downside protection while retaining favorable FX upside, unlike full forward hedge.

But option premium and liquidity must be compared with forward carry.

## 61. Tail Hedging

Tail hedge aims small recurring carry cost for large crisis payoff. Success depends timing, strike, maturity, roll discipline and whether payoff arrives when portfolio liquidity is needed.

A hedge that pays only after forced selling is less useful.

## 62. Hedge Budget

Protection should have explicit annual/quarterly cost budget. Repeatedly buying very expensive protection can destroy compounding.

Evaluate hedge as insurance program, not single-trade P/L.

## 63. Scenario Grid

A practical option risk grid should vary at least:

```text
Spot: -20%, -10%, -5%, 0%, +5%, +10%, +20%
IV: sharply lower / lower / unchanged / higher / crisis spike
Time: now / halfway / near expiry
```

For short options also include gap beyond modeled range and liquidity widening.

## 64. Probability of Profit vs Expectancy

High probability of profit can coexist with negative expectancy if losses are much larger than wins.

Options especially punish obsession with win rate. Always inspect expected payoff and tail size.

## 65. IV Rank và IV Percentile

These measures contextualize current IV relative to history but do not tell whether option is mispriced. High IV can be justified by real event risk; low IV can stay low.

They are descriptors, not strategies.

## 66. Cheap Premium vs Cheap Volatility

A 0.20 option can be expensive if probability is tiny and implied vol extreme. Absolute premium price says little about value.

Compare implied distribution, realized potential and catalyst horizon.

## 67. Options Backtest Difficulty

Underlying price history is insufficient for many option strategies. You need historical IV surface, spreads, dividends, rates, contract adjustments, early exercise and realistic fills.

Backtests using today’s IV assumptions on old spot data can be misleading.

## 68. Contract Adjustments

Splits, special dividends, mergers and corporate actions can adjust strikes/multipliers. Historical options data requires careful normalization.

Operational knowledge matters as much as model knowledge.

## 69. Volatility Forecasting

Historical volatility, EWMA, GARCH-like models and realized measures can inform forecasts, but options trade relative forecast vs market-implied price.

A forecast of “volatility will be high” is incomplete without saying high relative to what the market already charges.

## 70. Distribution Thinking

Option trader should think in distributions, not single target price. What is probability of mild move, large move, gap, volatility collapse or regime shift?

Payoff should match your distribution view, not just directional opinion.

## 71. Position Sizing

For long options, premium may be max contractual loss but repeated premium loss can still be material. For short options, use stress loss rather than margin requirement as risk size.

Margin is collateral, not economic risk measure.

## 72. Exit và Adjustment Rules

Decide ex ante whether thesis is direction, volatility or event. Exit rules should map to thesis: spot invalidation, IV target, time stop, event completion or Greek exposure limit.

Randomly rolling losing options can hide realized losses and enlarge risk.

## 73. Options Research Workflow

```text
Economic / Event Thesis
→ Distribution View
→ Spot View
→ Volatility / Skew / Term View
→ Horizon
→ Desired Payoff
→ Structure
→ Strike / Expiry
→ Greek Profile
→ Liquidity / Cost
→ Scenario Grid
→ Position Size
→ Hedge / Adjustment Rule
→ Exit / Post-trade Attribution
```

## 74. Post-Trade Attribution

After trade, separate P/L into direction, volatility, time decay, execution and sizing. “Call lost” is not enough.

If direction was right but IV crush caused loss, lesson differs from wrong directional thesis.

## 75. Common Failure Modes

Frequent failures include buying deep OTM lotteries, selling naked premium for high win rate, ignoring earnings/dividend/assignment, over-sizing because defined max loss appears small, using illiquid strikes, assuming IV mean reverts automatically and treating dealer-flow estimates as certain forecasts.

## 76. Mental Model cuối cùng

Options are a language for transferring state-contingent risk. A disciplined investor asks:

```text
Risk nào tôi đang mua hoặc bán?
Market đang price distribution nào?
Tôi khác market ở assumption nào?
Payoff có khớp assumption đó không?
Carry, liquidity và margin path ra sao?
Nếu spot + IV + time cùng đi bất lợi, tôi mất bao nhiêu?
```

Nếu chưa trả lời được các câu này, structure phức tạp hơn không tạo edge; nó chỉ làm risk khó nhìn hơn.