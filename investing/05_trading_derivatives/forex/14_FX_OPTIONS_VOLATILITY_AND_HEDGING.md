# 14 — FX options, volatility và hedging

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **14 — FX options, volatility và hedging**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Lời gọi (call / 호출) và put** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. FX option có hai currencies** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối FX options với volatility, Greeks và hedging, để định giá rủi ro phi tuyến thay vì chỉ nhìn hướng tỷ giá.

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

> **Nối mạch:** Trong **14 — FX options, volatility và hedging**, **2. FX option có hai currencies** nối từ **1. Lời gọi (call / 호출) và put** sang **3. Spot, forward và option**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. FX option có hai currencies

Trong FX, underlying là tỷ giá giữa hai currencies. Rates của cả hai phía ảnh hưởng forward và option valuation.

Không nên bản sao (copy / 복사) intuition equity option mà bỏ qua domestic/foreign-rate cấu trúc (structure / 구조).

> **Nối mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **3. Spot, forward và option** nối từ **2. FX option có hai currencies** sang **4. Intrinsic và thời gian (time / 시간) giá trị (value / 값)**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **4. Intrinsic và thời gian (time / 시간) giá trị (value / 값)** nối từ **3. Spot, forward và option** sang **5. Implied volatility**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Intrinsic và thời gian (time / 시간) giá trị (value / 값)

Option premium gồm:

```text
intrinsic value
+ time value
```

Out-of-the-money option có intrinsic 0 nhưng vẫn có thời gian (time / 시간) giá trị (value / 값) nếu còn khả năng finish in-the-money.

> **Nối mạch:** Trong **14 — FX options, volatility và hedging**, **5. Implied volatility** nối từ **4. Intrinsic và thời gian (time / 시간) giá trị (value / 값)** sang **6. Realized volatility**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Implied volatility

**Implied volatility (IV)** là volatility parameter khiến pricing mô hình (model / 모델) match thị trường (market / 시장) option price.

Nó không phải trực tiếp “dự báo chính xác volatility tương lai”. Nó phản ánh:

- expected movement;
- rủi ro (risk / 위험) premium;
- supply/demand;
- hedging pressure;
- mô hình (model / 모델) convention.

> **Nối mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **6. Realized volatility** nối từ **5. Implied volatility** sang **7. Delta**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Realized volatility

Realized volatility đo movement đã xảy ra.

Volatility trading thường quan tâm relationship:

```text
Implied Vol
vs
Future Realized Vol
```

Nhưng option P/L còn phụ thuộc đường dẫn (path / 경로), skew, giao dịch (transaction / 트랜잭션) chi phí (cost / 비용) và hedging.

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **7. Delta** nối từ **6. Realized volatility** sang **8. Gamma**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Delta

Delta xấp xỉ sensitivity option giá trị (value / 값) với small spot move.

```text
Delta ≈ ∂V/∂S
```

Lời gọi (call / 호출) delta thường positive, put delta negative theo convention phổ biến.

Delta thay đổi theo spot/thời gian (time / 시간)/volatility.

> **Nối mạch:** Trong **14 — FX options, volatility và hedging**, **8. Gamma** nối từ **7. Delta** sang **9. Theta**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Gamma

Gamma đo thay đổi (change / 변경) của delta theo spot:

```text
Gamma = ∂²V/∂S²
```

Long option thường long gamma: delta thay đổi theo hướng có lợi cho convexity, nhưng buyer trả theta/premium cho đặc tính đó.

> **Nối mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **9. Theta** nối từ **8. Gamma** sang **10. Vega**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Theta

Theta đo thời gian (time / 시간) decay, all else equal.

Long option thường chịu negative theta.

Nhưng realized P/L không chỉ là “mỗi ngày mất theta”; spot/vol/hedging moves có thể offset.

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **10. Vega** nối từ **9. Theta** sang **11. Rho / tỷ lệ (rate / 비율) sensitivity**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Vega

Vega đo sensitivity với implied volatility.

Long option thường positive vega.

Nếu IV giảm mạnh sau sự kiện (event / 이벤트), option buyer có thể lỗ dù spot direction đúng nhẹ.

> **Nối mạch:** Trong **14 — FX options, volatility và hedging**, **11. Rho / tỷ lệ (rate / 비율) sensitivity** nối từ **10. Vega** sang **12. Delta-neutral không risk-neutral**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Rho / tỷ lệ (rate / 비율) sensitivity

FX options phụ thuộc tỷ lệ (rate / 비율) differential, nên sensitivity với rates relevant hơn simple equity-option intuition trong một số maturities.

> **Nối mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **12. Delta-neutral không risk-neutral** nối từ **11. Rho / tỷ lệ (rate / 비율) sensitivity** sang **13. Gamma scalping intuition**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Delta-neutral không risk-neutral

Một portfolio delta ≈ 0 vẫn có:

- gamma;
- vega;
- theta;
- skew;
- jump rủi ro (risk / 위험);
- liquidity rủi ro (risk / 위험).

Neutralizing first-order direction không xóa nonlinear rủi ro (risk / 위험).

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **13. Gamma scalping intuition** nối từ **12. Delta-neutral không risk-neutral** sang **14. Volatility surface**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Gamma scalping intuition

Long gamma trader có thể rebalance delta:

```text
price rises → sell some underlying
price falls → buy some underlying
```

Nếu realized movement đủ lớn relative to option premium/chi phí (cost / 비용), rehedging can monetize convexity.

Nhưng giao dịch (transaction / 트랜잭션) chi phí (cost / 비용) và discrete jumps matter.

> **Nối mạch:** Trong **14 — FX options, volatility và hedging**, **14. Volatility surface** nối từ **13. Gamma scalping intuition** sang **15. Smile / skew**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Volatility surface

IV không chỉ là một số. Nó thay đổi theo:

```text
maturity
strike / delta
```

Collection này là volatility surface.

> **Nối mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **15. Smile / skew** nối từ **14. Volatility surface** sang **16. Rủi ro (risk / 위험) reversal**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Smile / skew

Different strikes can trade at different IV.

FX thị trường (market / 시장) thường quote skew via conventions như rủi ro (risk / 위험) reversals/butterflies.

Skew phản ánh asymmetric demand/rủi ro (risk / 위험) perceptions, không chỉ statistical phân phối (distribution / 분포).

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **16. Rủi ro (risk / 위험) reversal** nối từ **15. Smile / skew** sang **17. Butterfly**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Rủi ro (risk / 위험) reversal

Conceptually, rủi ro (risk / 위험) reversal compares IV of out-of-the-money lời gọi (call / 호출) vs put at matched delta convention.

It gives thông tin (information / 정보) about relative demand for upside vs downside protection.

Chính xác (exact / 정확한) quoting conventions depend on pair/thị trường (market / 시장).

> **Nối mạch:** Trong **14 — FX options, volatility và hedging**, **17. Butterfly** nối từ **16. Rủi ro (risk / 위험) reversal** sang **18. Delta conventions in FX**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Butterfly

Butterfly quote captures curvature/smile relative to ATM and wings.

It helps construct surface, not a directional spot tín hiệu (signal / 신호) by itself.

> **Nối mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **18. Delta conventions in FX** nối từ **17. Butterfly** sang **19. ATM conventions**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Delta conventions in FX

FX options have market-specific delta conventions, including spot/forward delta and premium-adjusted variants depending on pair/thị trường (market / 시장).

Never assume a quoted “25-delta option” has one universal formula without checking convention.

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **19. ATM conventions** nối từ **18. Delta conventions in FX** sang **20. Straddle**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. ATM conventions

ATM can mean different things:

- spot ATM;
- forward ATM;
- delta-neutral straddle conventions.

Thị trường (market / 시장) documentation matters.

> **Nối mạch:** Trong **14 — FX options, volatility và hedging**, **20. Straddle** nối từ **19. ATM conventions** sang **21. Strangle**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Straddle

Long straddle:

```text
long call + long put
same strike/maturity
```

It is primarily a long-volatility/large-move cấu trúc (structure / 구조), not simply “bet price goes up or down”.

Break-even depends on premium and final move.

> **Nối mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **21. Strangle** nối từ **20. Straddle** sang **22. Rủi ro (risk / 위험) reversal trade**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Strangle

Long OTM lời gọi (call / 호출) + OTM put.

Cheaper than comparable straddle but requires larger move to profit at expiry.

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **22. Rủi ro (risk / 위험) reversal trade** nối từ **21. Strangle** sang **23. Butterfly structures**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Rủi ro (risk / 위험) reversal trade

Buy lời gọi (call / 호출)/sell put or opposite creates directional + skew exposure.

It is not pure direction because option vols and convexity differ.

> **Nối mạch:** Trong **14 — FX options, volatility và hedging**, **23. Butterfly structures** nối từ **22. Rủi ro (risk / 위험) reversal trade** sang **24. Sự kiện (event / 이벤트) volatility**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Butterfly structures

Can express view on phân phối (distribution / 분포) around central region vs tails.

Payoff shape must be understood exactly before using labels.

> **Nối mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **24. Sự kiện (event / 이벤트) volatility** nối từ **23. Butterfly structures** sang **25. Implied move**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Sự kiện (event / 이벤트) volatility

Before CPI/FOMC/election-like or major chính sách (policy / 정책) sự kiện (event / 이벤트), option IV may rise.

After sự kiện (event / 이벤트) bất định (uncertainty / 불확실성) resolves, IV can collapse.

This is **vol crush** intuition.

A trader long options needs spot movement/vol dynamics sufficient to offset premium decay.

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **25. Implied move** nối từ **24. Sự kiện (event / 이벤트) volatility** sang **26. Volatility rủi ro (risk / 위험) premium**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. Implied move

Traders sometimes translate short-dated option premium into approximate market-implied move.

This is heuristic/model-dependent, not hard hỗ trợ (support / 지원)/resistance.

> **Nối mạch:** Trong **14 — FX options, volatility và hedging**, **26. Volatility rủi ro (risk / 위험) premium** nối từ **25. Implied move** sang **27. Jump rủi ro (risk / 위험)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Volatility rủi ro (risk / 위험) premium

Option sellers may earn premium because implied volatility can exceed subsequently realized volatility on average in some samples, but compensation comes with convex tail/jump rủi ro (risk / 위험).

“Short vol earns theta” is incomplete without crash exposure.

> **Nối mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **27. Jump rủi ro (risk / 위험)** nối từ **26. Volatility rủi ro (risk / 위험) premium** sang **28. Gap and liquidity rủi ro (risk / 위험)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Jump rủi ro (risk / 위험)

Discrete chính sách (policy / 정책)/geopolitical events can move spot beyond continuous-model các giả định (assumptions / 가정들).

Delta hedging cannot eliminate jump rủi ro (risk / 위험).

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **28. Gap and liquidity rủi ro (risk / 위험)** nối từ **27. Jump rủi ro (risk / 위험)** sang **29. Vol-of-vol**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. Gap and liquidity rủi ro (risk / 위험)

During stress:

- IV spikes;
- spreads widen;
- hedges slip;
- correlations thay đổi (change / 변경).

Option portfolio marks may move even if theoretical mô hình (model / 모델) inputs seem manageable.

> **Nối mạch:** Trong **14 — FX options, volatility và hedging**, **29. Vol-of-vol** nối từ **28. Gap and liquidity rủi ro (risk / 위험)** sang **30. Vanna / volga intuition**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. Vol-of-vol

Implied volatility itself moves. Vol-of-vol matters for longer-dated/exotic exposure and surface dynamics.

> **Nối mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **30. Vanna / volga intuition** nối từ **29. Vol-of-vol** sang **31. Barrier options**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. Vanna / volga intuition

Higher-order Greeks describe interactions between spot and vol or curvature with vol.

They become important when portfolio is large/complex; beginner should first master delta/gamma/theta/vega.

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **31. Barrier options** nối từ **30. Vanna / volga intuition** sang **32. Digital options**, vì cơ chế trước tạo đầu vào cho bước sau.

## 31. Barrier options

Barrier option activates/deactivates when spot touches mức (level / 수준).

Near barrier, hedging hành vi (behavior / 동작) can become nonlinear and path-dependent.

Retail structured products can embed barrier-like risks without obvious “option” label.

> **Nối mạch:** Trong **14 — FX options, volatility và hedging**, **32. Digital options** nối từ **31. Barrier options** sang **33. Exotic FX options**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. Digital options

Pay fixed amount conditional on threshold sự kiện (event / 이벤트).

Payoff discontinuity creates concentrated rủi ro (risk / 위험) near strike/expiry.

> **Nối mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **33. Exotic FX options** nối từ **32. Digital options** sang **34. Hedging corporate FX exposure with options**, vì cơ chế trước tạo đầu vào cho bước sau.

## 33. Exotic FX options

Examples include:

- barriers;
- digitals;
- Asians;
- lookbacks;
- accumulators/structured variants.

Độ phức tạp (complexity / 복잡도) adds mô hình (model / 모델), liquidity and legal-product rủi ro (risk / 위험).

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **34. Hedging corporate FX exposure with options** nối từ **33. Exotic FX options** sang **35. Forward vs option hedge**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. Hedging corporate FX exposure with options

Options can protect adverse move while preserving upside.

Example conceptual:

```text
Importer needs USD later
→ buy USD call / local-currency put
```

Premium is tường minh (explicit / 명시적) insurance chi phí (cost / 비용).

> **Nối mạch:** Trong **14 — FX options, volatility và hedging**, **35. Forward vs option hedge** nối từ **34. Hedging corporate FX exposure with options** sang **36. Collar**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **36. Collar** nối từ **35. Forward vs option hedge** sang **37. Hedge ratio and delta**, vì cơ chế trước tạo đầu vào cho bước sau.

## 36. Collar

Collar can reduce option premium by buying protection and selling upside beyond another mức (level / 수준).

But sold option creates obligation/cap on favorable kết quả (outcome / 결과).

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **37. Hedge ratio and delta** nối từ **36. Collar** sang **38. Động (dynamic / 동적) hedging chi phí (cost / 비용)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 37. Hedge ratio and delta

Option hedge notional should consider delta, which changes over thời gian (time / 시간).

A static “same notional” hedge may not remain equivalent.

> **Nối mạch:** Trong **14 — FX options, volatility và hedging**, **38. Động (dynamic / 동적) hedging chi phí (cost / 비용)** nối từ **37. Hedge ratio and delta** sang **39. Surface marking rủi ro (risk / 위험)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 38. Động (dynamic / 동적) hedging chi phí (cost / 비용)

Frequent delta rebalancing incurs:

- spread;
- slippage;
- thị trường (market / 시장) impact.

Theoretical continuous hedge is impossible in real thị trường (market / 시장).

> **Nối mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **39. Surface marking rủi ro (risk / 위험)** nối từ **38. Động (dynamic / 동적) hedging chi phí (cost / 비용)** sang **40. Options backtest difficulty**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **40. Options backtest difficulty** nối từ **39. Surface marking rủi ro (risk / 위험)** sang **41. Stale/missing quotes**, vì cơ chế trước tạo đầu vào cho bước sau.

## 40. Options backtest difficulty

Need historical:

- full option chuỗi (chain / 사슬)/surface;
- bid/ask;
- conventions;
- expiries;
- rates/forwards;
- realistic hedging.

Backtesting options from spot OHLC + hiện tại (current / 현재) IV giả định (assumption / 가정) is usually inadequate.

> **Nối mạch:** Trong **14 — FX options, volatility và hedging**, **41. Stale/missing quotes** nối từ **40. Options backtest difficulty** sang **42. Greeks are cục bộ (local / 로컬) approximations**, vì cơ chế trước tạo đầu vào cho bước sau.

## 41. Stale/missing quotes

OTC option datasets may be indicative, sparse or interpolation-heavy.

Research must know whether quotes are executable, composite or model-derived.

> **Nối mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **42. Greeks are cục bộ (local / 로컬) approximations** nối từ **41. Stale/missing quotes** sang **43. Kiểm thử sức chịu tải (stress test / 스트레스 테스트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 42. Greeks are cục bộ (local / 로컬) approximations

Delta/gamma Taylor approximation works for small moves.

Large jump changes Greeks themselves; full revaluation needed.

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **43. Kiểm thử sức chịu tải (stress test / 스트레스 테스트)** nối từ **42. Greeks are cục bộ (local / 로컬) approximations** sang **44. Tail hedge chi phí (cost / 비용)**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **14 — FX options, volatility và hedging**, **44. Tail hedge chi phí (cost / 비용)** nối từ **43. Kiểm thử sức chịu tải (stress test / 스트레스 테스트)** sang **45. Selling options and margin**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **45. Selling options and margin** nối từ **44. Tail hedge chi phí (cost / 비용)** sang **46. Broker OTC option/sản phẩm (product / 제품) rủi ro (risk / 위험)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 45. Selling options and margin

Short option has potentially large nonlinear mất mát (loss / 손실) and margin requirements can rise sharply as thị trường (market / 시장) moves/volatility rises.

Margin stress must be modeled before premium income.

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **46. Broker OTC option/sản phẩm (product / 제품) rủi ro (risk / 위험)** nối từ **45. Selling options and margin** sang **47. Do not infer xác suất (probability / 확률) directly from delta**, vì cơ chế trước tạo đầu vào cho bước sau.

## 46. Broker OTC option/sản phẩm (product / 제품) rủi ro (risk / 위험)

If using retail OTC products, legal thực thể (entity / 엔터티), settlement and pricing transparency are part of rủi ro (risk / 위험) mô hình (model / 모델) just as with spot/CFD.

> **Nối mạch:** Trong **14 — FX options, volatility và hedging**, **47. Do not infer xác suất (probability / 확률) directly from delta** nối từ **46. Broker OTC option/sản phẩm (product / 제품) rủi ro (risk / 위험)** sang **48. Risk-neutral vs real-world xác suất (probability / 확률)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 47. Do not infer xác suất (probability / 확률) directly from delta

Option delta is sometimes loosely interpreted as probability-like. Under specific các mô hình (models / 모델들)/conventions it relates to risk-neutral measures, but it is not a simple real-world xác suất (probability / 확률) of expiring ITM.

> **Nối mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **48. Risk-neutral vs real-world xác suất (probability / 확률)** nối từ **47. Do not infer xác suất (probability / 확률) directly from delta** sang **49. Minimal option position sheet**, vì cơ chế trước tạo đầu vào cho bước sau.

## 48. Risk-neutral vs real-world xác suất (probability / 확률)

Option prices encode risk-neutral valuation plus rủi ro (risk / 위험) premia, not pure vật lý (physical / 물리적) xác suất (probability / 확률) forecast.

This distinction matters when using options thị trường (market / 시장) as macro expectation indicator.

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **49. Minimal option position sheet** nối từ **48. Risk-neutral vs real-world xác suất (probability / 확률)** sang **50. Checklist**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **14 — FX options, volatility và hedging**, **50. Checklist** nối từ **49. Minimal option position sheet** sang **Đọc tiếp**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **Đọc tiếp** nối từ **50. Checklist** sang **Nội bộ (internal / 내부) links**, vì cơ chế trước tạo đầu vào cho bước sau.

## Đọc tiếp

→ [15 — Korea / Vietnam FX market context and regulations](./15_KOREA_VIETNAM_FX_MARKET_CONTEXT_AND_REGULATIONS.md)

> **Nối mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **Nội bộ (internal / 내부) links** nối từ **Đọc tiếp** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Nội bộ (internal / 내부) links

- [Options, Volatility Surface, Greeks and Hedging](../05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md)
- [04 — Macro drivers](./04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)
- [11 — Portfolio FX risk](./11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)

> **Bàn giao:** Sau **Nội bộ (internal / 내부) links**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
