# 14 — FX options, volatility và hedging

FX options thêm một chiều mới vào trading: payoff không còn chỉ phụ thuộc hướng spot mà còn phụ thuộc **implied volatility, thời gian (time / 시간), rates và convexity**. Vì vậy đúng hướng spot vẫn có thể lỗ nếu option premium, timing hoặc volatility view sai.

Mô hình tư duy (mental model / 사고 모델):

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

## 1. Lời gọi (call / 호출) và put

Một lời gọi (call / 호출) cho quyền mua underlying theo strike `K`.

Một put cho quyền bán.

Payoff tại expiry:

```text
Call = max(S_T - K, 0)
Put  = max(K - S_T, 0)
```

Nhưng trước expiry, option giá trị (value / 값) còn chứa thời gian (time / 시간) giá trị (value / 값).

## 2. FX option có hai currencies

Trong FX, underlying là tỷ giá giữa hai currencies. Rates của cả hai phía ảnh hưởng forward và option valuation.

Không nên bản sao (copy / 복사) intuition equity option mà bỏ qua domestic/foreign-rate cấu trúc (structure / 구조).

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

## 4. Intrinsic và thời gian (time / 시간) giá trị (value / 값)

Option premium gồm:

```text
intrinsic value
+ time value
```

Out-of-the-money option có intrinsic 0 nhưng vẫn có thời gian (time / 시간) giá trị (value / 값) nếu còn khả năng finish in-the-money.

## 5. Implied volatility

**Implied volatility (IV)** là volatility parameter khiến pricing mô hình (model / 모델) match thị trường (market / 시장) option price.

Nó không phải trực tiếp “dự báo chính xác volatility tương lai”. Nó phản ánh:

- expected movement;
- rủi ro (risk / 위험) premium;
- supply/demand;
- hedging pressure;
- mô hình (model / 모델) convention.

## 6. Realized volatility

Realized volatility đo movement đã xảy ra.

Volatility trading thường quan tâm relationship:

```text
Implied Vol
vs
Future Realized Vol
```

Nhưng option P/L còn phụ thuộc đường dẫn (path / 경로), skew, giao dịch (transaction / 트랜잭션) chi phí (cost / 비용) và hedging.

## 7. Delta

Delta xấp xỉ sensitivity option giá trị (value / 값) với small spot move.

```text
Delta ≈ ∂V/∂S
```

Lời gọi (call / 호출) delta thường positive, put delta negative theo convention phổ biến.

Delta thay đổi theo spot/thời gian (time / 시간)/volatility.

## 8. Gamma

Gamma đo thay đổi (change / 변경) của delta theo spot:

```text
Gamma = ∂²V/∂S²
```

Long option thường long gamma: delta thay đổi theo hướng có lợi cho convexity, nhưng buyer trả theta/premium cho đặc tính đó.

## 9. Theta

Theta đo thời gian (time / 시간) decay, all else equal.

Long option thường chịu negative theta.

Nhưng realized P/L không chỉ là “mỗi ngày mất theta”; spot/vol/hedging moves có thể offset.

## 10. Vega

Vega đo sensitivity với implied volatility.

Long option thường positive vega.

Nếu IV giảm mạnh sau sự kiện (event / 이벤트), option buyer có thể lỗ dù spot direction đúng nhẹ.

## 11. Rho / tỷ lệ (rate / 비율) sensitivity

FX options phụ thuộc tỷ lệ (rate / 비율) differential, nên sensitivity với rates relevant hơn simple equity-option intuition trong một số maturities.

## 12. Delta-neutral không risk-neutral

Một portfolio delta ≈ 0 vẫn có:

- gamma;
- vega;
- theta;
- skew;
- jump rủi ro (risk / 위험);
- liquidity rủi ro (risk / 위험).

Neutralizing first-order direction không xóa nonlinear rủi ro (risk / 위험).

## 13. Gamma scalping intuition

Long gamma trader có thể rebalance delta:

```text
price rises → sell some underlying
price falls → buy some underlying
```

Nếu realized movement đủ lớn relative to option premium/chi phí (cost / 비용), rehedging can monetize convexity.

Nhưng giao dịch (transaction / 트랜잭션) chi phí (cost / 비용) và discrete jumps matter.

## 14. Volatility surface

IV không chỉ là một số. Nó thay đổi theo:

```text
maturity
strike / delta
```

Collection này là volatility surface.

## 15. Smile / skew

Different strikes can trade at different IV.

FX thị trường (market / 시장) thường quote skew via conventions như rủi ro (risk / 위험) reversals/butterflies.

Skew phản ánh asymmetric demand/rủi ro (risk / 위험) perceptions, không chỉ statistical phân phối (distribution / 분포).

## 16. Rủi ro (risk / 위험) reversal

Conceptually, rủi ro (risk / 위험) reversal compares IV of out-of-the-money lời gọi (call / 호출) vs put at matched delta convention.

It gives thông tin (information / 정보) about relative demand for upside vs downside protection.

Chính xác (exact / 정확한) quoting conventions depend on pair/thị trường (market / 시장).

## 17. Butterfly

Butterfly quote captures curvature/smile relative to ATM and wings.

It helps construct surface, not a directional spot tín hiệu (signal / 신호) by itself.

## 18. Delta conventions in FX

FX options have market-specific delta conventions, including spot/forward delta and premium-adjusted variants depending on pair/thị trường (market / 시장).

Never assume a quoted “25-delta option” has one universal formula without checking convention.

## 19. ATM conventions

ATM can mean different things:

- spot ATM;
- forward ATM;
- delta-neutral straddle conventions.

Thị trường (market / 시장) documentation matters.

## 20. Straddle

Long straddle:

```text
long call + long put
same strike/maturity
```

It is primarily a long-volatility/large-move cấu trúc (structure / 구조), not simply “bet price goes up or down”.

Break-even depends on premium and final move.

## 21. Strangle

Long OTM lời gọi (call / 호출) + OTM put.

Cheaper than comparable straddle but requires larger move to profit at expiry.

## 22. Rủi ro (risk / 위험) reversal trade

Buy lời gọi (call / 호출)/sell put or opposite creates directional + skew exposure.

It is not pure direction because option vols and convexity differ.

## 23. Butterfly structures

Can express view on phân phối (distribution / 분포) around central region vs tails.

Payoff shape must be understood exactly before using labels.

## 24. Sự kiện (event / 이벤트) volatility

Before CPI/FOMC/election-like or major chính sách (policy / 정책) sự kiện (event / 이벤트), option IV may rise.

After sự kiện (event / 이벤트) bất định (uncertainty / 불확실성) resolves, IV can collapse.

This is **vol crush** intuition.

A trader long options needs spot movement/vol dynamics sufficient to offset premium decay.

## 25. Implied move

Traders sometimes translate short-dated option premium into approximate market-implied move.

This is heuristic/model-dependent, not hard hỗ trợ (support / 지원)/resistance.

## 26. Volatility rủi ro (risk / 위험) premium

Option sellers may earn premium because implied volatility can exceed subsequently realized volatility on average in some samples, but compensation comes with convex tail/jump rủi ro (risk / 위험).

“Short vol earns theta” is incomplete without crash exposure.

## 27. Jump rủi ro (risk / 위험)

Discrete chính sách (policy / 정책)/geopolitical events can move spot beyond continuous-model các giả định (assumptions / 가정들).

Delta hedging cannot eliminate jump rủi ro (risk / 위험).

## 28. Gap and liquidity rủi ro (risk / 위험)

During stress:

- IV spikes;
- spreads widen;
- hedges slip;
- correlations thay đổi (change / 변경).

Option portfolio marks may move even if theoretical mô hình (model / 모델) inputs seem manageable.

## 29. Vol-of-vol

Implied volatility itself moves. Vol-of-vol matters for longer-dated/exotic exposure and surface dynamics.

## 30. Vanna / volga intuition

Higher-order Greeks describe interactions between spot and vol or curvature with vol.

They become important when portfolio is large/complex; beginner should first master delta/gamma/theta/vega.

## 31. Barrier options

Barrier option activates/deactivates when spot touches mức (level / 수준).

Near barrier, hedging hành vi (behavior / 동작) can become nonlinear and path-dependent.

Retail structured products can embed barrier-like risks without obvious “option” label.

## 32. Digital options

Pay fixed amount conditional on threshold sự kiện (event / 이벤트).

Payoff discontinuity creates concentrated rủi ro (risk / 위험) near strike/expiry.

## 33. Exotic FX options

Examples include:

- barriers;
- digitals;
- Asians;
- lookbacks;
- accumulators/structured variants.

Độ phức tạp (complexity / 복잡도) adds mô hình (model / 모델), liquidity and legal-product rủi ro (risk / 위험).

## 34. Hedging corporate FX exposure with options

Options can protect adverse move while preserving upside.

Example conceptual:

```text
Importer needs USD later
→ buy USD call / local-currency put
```

Premium is tường minh (explicit / 명시적) insurance chi phí (cost / 비용).

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

Choice depends on mục tiêu (objective / 목표)/chi phí (cost / 비용)/accounting/liquidity.

## 36. Collar

Collar can reduce option premium by buying protection and selling upside beyond another mức (level / 수준).

But sold option creates obligation/cap on favorable kết quả (outcome / 결과).

## 37. Hedge ratio and delta

Option hedge notional should consider delta, which changes over thời gian (time / 시간).

A static “same notional” hedge may not remain equivalent.

## 38. Động (dynamic / 동적) hedging chi phí (cost / 비용)

Frequent delta rebalancing incurs:

- spread;
- slippage;
- thị trường (market / 시장) impact.

Theoretical continuous hedge is impossible in real thị trường (market / 시장).

## 39. Surface marking rủi ro (risk / 위험)

P/L attribution should separate:

```text
spot delta
volatility
skew/surface movement
time decay
rates
hedging cost
```

Without attribution, option hiệu năng (performance / 성능) is opaque.

## 40. Options backtest difficulty

Need historical:

- full option chuỗi (chain / 사슬)/surface;
- bid/ask;
- conventions;
- expiries;
- rates/forwards;
- realistic hedging.

Backtesting options from spot OHLC + hiện tại (current / 현재) IV giả định (assumption / 가정) is usually inadequate.

## 41. Stale/missing quotes

OTC option datasets may be indicative, sparse or interpolation-heavy.

Research must know whether quotes are executable, composite or model-derived.

## 42. Greeks are cục bộ (local / 로컬) approximations

Delta/gamma Taylor approximation works for small moves.

Large jump changes Greeks themselves; full revaluation needed.

## 43. Kiểm thử sức chịu tải (stress test / 스트레스 테스트)

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

## 44. Tail hedge chi phí (cost / 비용)

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

Short option has potentially large nonlinear mất mát (loss / 손실) and margin requirements can rise sharply as thị trường (market / 시장) moves/volatility rises.

Margin stress must be modeled before premium income.

## 46. Broker OTC option/sản phẩm (product / 제품) rủi ro (risk / 위험)

If using retail OTC products, legal thực thể (entity / 엔터티), settlement and pricing transparency are part of rủi ro (risk / 위험) mô hình (model / 모델) just as with spot/CFD.

## 47. Do not infer xác suất (probability / 확률) directly from delta

Option delta is sometimes loosely interpreted as probability-like. Under specific các mô hình (models / 모델들)/conventions it relates to risk-neutral measures, but it is not a simple real-world xác suất (probability / 확률) of expiring ITM.

## 48. Risk-neutral vs real-world xác suất (probability / 확률)

Option prices encode risk-neutral valuation plus rủi ro (risk / 위험) premia, not pure vật lý (physical / 물리적) xác suất (probability / 확률) forecast.

This distinction matters when using options thị trường (market / 시장) as macro expectation indicator.

## 49. Minimal option position sheet
Phần “49. Minimal option position sheet” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


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
6. Sự kiện (event / 이벤트) vol and vol crush.
7. Forward vs option hedge sự đánh đổi (trade-off / 트레이드오프).
8. Động (dynamic / 동적) hedging costs/jump rủi ro (risk / 위험).
9. Why option backtesting needs surface dữ liệu (data / 데이터).
10. Why short-vol premium income carries tail rủi ro (risk / 위험).

## Đọc tiếp

→ [15 — Korea / Vietnam FX market context and regulations](./15_KOREA_VIETNAM_FX_MARKET_CONTEXT_AND_REGULATIONS.md)

## Nội bộ (internal / 내부) links
Phần “Nội bộ (internal / 내부) links” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- [Options, Volatility Surface, Greeks and Hedging](../05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md)
- [04 — Macro drivers](./04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)
- [11 — Portfolio FX risk](./11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
