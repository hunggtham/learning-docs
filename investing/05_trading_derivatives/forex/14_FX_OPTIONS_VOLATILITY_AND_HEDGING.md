# 14 — FX options, volatility và hedging

FX options thêm một chiều mới vào trading: payoff không còn chỉ phụ thuộc hướng spot mà còn phụ thuộc **implied volatility, time, rates và convexity**. Vì vậy đúng hướng spot vẫn có thể lỗ nếu option premium, timing hoặc volatility view sai.

Mental model:

```text
Spot / forward state
+ strike
+ maturity
+ implied volatility
+ rates / carry
→ option value
→ Greeks
→ hedge behavior
→ P/L path
```

## 1. Call và put

Một call cho quyền mua underlying theo strike `K`.

Một put cho quyền bán.

Payoff tại expiry:

```text
Call = max(S_T - K, 0)
Put  = max(K - S_T, 0)
```

Nhưng trước expiry, option value còn chứa time value.

## 2. FX option có hai currencies

Trong FX, underlying là tỷ giá giữa hai currencies. Rates của cả hai phía ảnh hưởng forward và option valuation.

Không nên copy intuition equity option mà bỏ qua domestic/foreign-rate structure.

## 3. Spot, forward và option

Option thường được định giá relative to forward dynamics.

Simplified:

```text
Spot
+ interest-rate differential
→ forward
+ volatility / strike / time
→ option value
```

## 4. Intrinsic và time value

Option premium gồm:

```text
intrinsic value
+ time value
```

Out-of-the-money option có intrinsic 0 nhưng vẫn có time value nếu còn khả năng finish in-the-money.

## 5. Implied volatility

**Implied volatility (IV)** là volatility parameter khiến pricing model match market option price.

Nó không phải trực tiếp “dự báo chính xác volatility tương lai”. Nó phản ánh:

- expected movement;
- risk premium;
- supply/demand;
- hedging pressure;
- model convention.

## 6. Realized volatility

Realized volatility đo movement đã xảy ra.

Volatility trading thường quan tâm relationship:

```text
Implied Vol
vs
Future Realized Vol
```

Nhưng option P/L còn phụ thuộc path, skew, transaction cost và hedging.

## 7. Delta

Delta xấp xỉ sensitivity option value với small spot move.

```text
Delta ≈ ∂V/∂S
```

Call delta thường positive, put delta negative theo convention phổ biến.

Delta thay đổi theo spot/time/volatility.

## 8. Gamma

Gamma đo change của delta theo spot:

```text
Gamma = ∂²V/∂S²
```

Long option thường long gamma: delta thay đổi theo hướng có lợi cho convexity, nhưng buyer trả theta/premium cho đặc tính đó.

## 9. Theta

Theta đo time decay, all else equal.

Long option thường chịu negative theta.

Nhưng realized P/L không chỉ là “mỗi ngày mất theta”; spot/vol/hedging moves có thể offset.

## 10. Vega

Vega đo sensitivity với implied volatility.

Long option thường positive vega.

Nếu IV giảm mạnh sau event, option buyer có thể lỗ dù spot direction đúng nhẹ.

## 11. Rho / rate sensitivity

FX options phụ thuộc rate differential, nên sensitivity với rates relevant hơn simple equity-option intuition trong một số maturities.

## 12. Delta-neutral không risk-neutral

Một portfolio delta ≈ 0 vẫn có:

- gamma;
- vega;
- theta;
- skew;
- jump risk;
- liquidity risk.

Neutralizing first-order direction không xóa nonlinear risk.

## 13. Gamma scalping intuition

Long gamma trader có thể rebalance delta:

```text
price rises → sell some underlying
price falls → buy some underlying
```

Nếu realized movement đủ lớn relative to option premium/cost, rehedging can monetize convexity.

Nhưng transaction cost và discrete jumps matter.

## 14. Volatility surface

IV không chỉ là một số. Nó thay đổi theo:

```text
maturity
strike / delta
```

Collection này là volatility surface.

## 15. Smile / skew

Different strikes can trade at different IV.

FX market thường quote skew via conventions như risk reversals/butterflies.

Skew phản ánh asymmetric demand/risk perceptions, không chỉ statistical distribution.

## 16. Risk reversal

Conceptually, risk reversal compares IV of out-of-the-money call vs put at matched delta convention.

It gives information about relative demand for upside vs downside protection.

Exact quoting conventions depend on pair/market.

## 17. Butterfly

Butterfly quote captures curvature/smile relative to ATM and wings.

It helps construct surface, not a directional spot signal by itself.

## 18. Delta conventions in FX

FX options have market-specific delta conventions, including spot/forward delta and premium-adjusted variants depending on pair/market.

Never assume a quoted “25-delta option” has one universal formula without checking convention.

## 19. ATM conventions

ATM can mean different things:

- spot ATM;
- forward ATM;
- delta-neutral straddle conventions.

Market documentation matters.

## 20. Straddle

Long straddle:

```text
long call + long put
same strike/maturity
```

It is primarily a long-volatility/large-move structure, not simply “bet price goes up or down”.

Break-even depends on premium and final move.

## 21. Strangle

Long OTM call + OTM put.

Cheaper than comparable straddle but requires larger move to profit at expiry.

## 22. Risk reversal trade

Buy call/sell put or opposite creates directional + skew exposure.

It is not pure direction because option vols and convexity differ.

## 23. Butterfly structures

Can express view on distribution around central region vs tails.

Payoff shape must be understood exactly before using labels.

## 24. Event volatility

Before CPI/FOMC/election-like or major policy event, option IV may rise.

After event uncertainty resolves, IV can collapse.

This is **vol crush** intuition.

A trader long options needs spot movement/vol dynamics sufficient to offset premium decay.

## 25. Implied move

Traders sometimes translate short-dated option premium into approximate market-implied move.

This is heuristic/model-dependent, not hard support/resistance.

## 26. Volatility risk premium

Option sellers may earn premium because implied volatility can exceed subsequently realized volatility on average in some samples, but compensation comes with convex tail/jump risk.

“Short vol earns theta” is incomplete without crash exposure.

## 27. Jump risk

Discrete policy/geopolitical events can move spot beyond continuous-model assumptions.

Delta hedging cannot eliminate jump risk.

## 28. Gap and liquidity risk

During stress:

- IV spikes;
- spreads widen;
- hedges slip;
- correlations change.

Option portfolio marks may move even if theoretical model inputs seem manageable.

## 29. Vol-of-vol

Implied volatility itself moves. Vol-of-vol matters for longer-dated/exotic exposure and surface dynamics.

## 30. Vanna / volga intuition

Higher-order Greeks describe interactions between spot and vol or curvature with vol.

They become important when portfolio is large/complex; beginner should first master delta/gamma/theta/vega.

## 31. Barrier options

Barrier option activates/deactivates when spot touches level.

Near barrier, hedging behavior can become nonlinear and path-dependent.

Retail structured products can embed barrier-like risks without obvious “option” label.

## 32. Digital options

Pay fixed amount conditional on threshold event.

Payoff discontinuity creates concentrated risk near strike/expiry.

## 33. Exotic FX options

Examples include:

- barriers;
- digitals;
- Asians;
- lookbacks;
- accumulators/structured variants.

Complexity adds model, liquidity and legal-product risk.

## 34. Hedging corporate FX exposure with options

Options can protect adverse move while preserving upside.

Example conceptual:

```text
Importer needs USD later
→ buy USD call / local-currency put
```

Premium is explicit insurance cost.

## 35. Forward vs option hedge

Forward:

```text
lock rate
low/no upfront premium often
but give up favorable move
```

Option:

```text
pay premium
protect adverse tail
retain favorable move subject to structure
```

Choice depends on objective/cost/accounting/liquidity.

## 36. Collar

Collar can reduce option premium by buying protection and selling upside beyond another level.

But sold option creates obligation/cap on favorable outcome.

## 37. Hedge ratio and delta

Option hedge notional should consider delta, which changes over time.

A static “same notional” hedge may not remain equivalent.

## 38. Dynamic hedging cost

Frequent delta rebalancing incurs:

- spread;
- slippage;
- market impact.

Theoretical continuous hedge is impossible in real market.

## 39. Surface marking risk

P/L attribution should separate:

```text
spot delta
volatility
skew/surface movement
time decay
rates
hedging cost
```

Without attribution, option performance is opaque.

## 40. Options backtest difficulty

Need historical:

- full option chain/surface;
- bid/ask;
- conventions;
- expiries;
- rates/forwards;
- realistic hedging.

Backtesting options from spot OHLC + current IV assumption is usually inadequate.

## 41. Stale/missing quotes

OTC option datasets may be indicative, sparse or interpolation-heavy.

Research must know whether quotes are executable, composite or model-derived.

## 42. Greeks are local approximations

Delta/gamma Taylor approximation works for small moves.

Large jump changes Greeks themselves; full revaluation needed.

## 43. Stress test

Option book should shock:

```text
spot ±X%
IV ±Y vols
skew shift
time passage
rate shift
liquidity spread widening
```

Not just delta move.

## 44. Tail hedge cost

Buying protection repeatedly can drag return.

Evaluate:

```text
premium paid
crisis payoff
carry drag
roll timing
basis to risk being hedged
```

## 45. Selling options and margin

Short option has potentially large nonlinear loss and margin requirements can rise sharply as market moves/volatility rises.

Margin stress must be modeled before premium income.

## 46. Broker OTC option/product risk

If using retail OTC products, legal entity, settlement and pricing transparency are part of risk model just as with spot/CFD.

## 47. Do not infer probability directly from delta

Option delta is sometimes loosely interpreted as probability-like. Under specific models/conventions it relates to risk-neutral measures, but it is not a simple real-world probability of expiring ITM.

## 48. Risk-neutral vs real-world probability

Option prices encode risk-neutral valuation plus risk premia, not pure physical probability forecast.

This distinction matters when using options market as macro expectation indicator.

## 49. Minimal option position sheet

```text
Pair
Structure
Notional
Expiry
Strike(s)
Premium
Delta
Gamma
Theta
Vega
IV / skew context
Spot/forward
Max loss / nonlinear tail
Liquidity
Hedge plan
Event exposure
```

## 50. Checklist

Bạn cần tự giải thích được:

1. Option P/L depends on more than spot direction.
2. IV vs realized volatility.
3. Delta/gamma/theta/vega.
4. Why delta-neutral is not risk-neutral.
5. Surface/skew/risk-reversal concepts.
6. Event vol and vol crush.
7. Forward vs option hedge trade-off.
8. Dynamic hedging costs/jump risk.
9. Why option backtesting needs surface data.
10. Why short-vol premium income carries tail risk.

## Đọc tiếp

→ [15 — Korea / Vietnam FX market context and regulations](./15_KOREA_VIETNAM_FX_MARKET_CONTEXT_AND_REGULATIONS.md)

## Internal links

- [Options, Volatility Surface, Greeks and Hedging](../05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md)
- [04 — Macro drivers](./04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)
- [11 — Portfolio FX risk](./11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
