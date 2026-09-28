# FX Funding, NDF, Basis & Forward Curve — nối spot Forex với money market và funding

Chapter bridge này không nằm trong linear route `01–15`. Nó tồn tại để trả lời một câu hỏi mà spot chart không trả lời được: **khi một tổ chức hedge, vay hoặc chuyển funding giữa hai đồng tiền, tỷ giá forward/NDF/basis được hình thành như thế nào và vì sao chúng có thể tách khỏi textbook parity?**

Đây là bridge giữa Forex, derivatives và macro funding. Nếu mục tiêu chỉ là hiểu retail spot mechanics, có thể đọc sau. Nếu muốn hiểu institutional FX, corporate hedging, KRW/VND offshore pricing hoặc USD funding stress, đây là phần bắt buộc.

Mental model:

```text
Spot FX
+ relative interest rates
+ settlement / calendar
+ collateral / counterparty
+ dealer balance sheet
+ convertibility / capital controls
→ forward points / FX swap / NDF / basis
```

## 1. Spot direction và funding economics là hai thứ khác nhau

Một trader có thể đúng hướng spot nhưng vẫn nhận P/L khác kỳ vọng vì financing hoặc hedge roll. Một corporation có thể giao dịch forward lớn dù không có directional view. Một bank có thể mua USD qua FX swap vì funding need chứ không phải vì bullish USD.

Do đó khi nhìn flow, cần hỏi trước:

```text
Directional position?
Hedge?
Funding transformation?
Liquidity management?
Regulatory balance-sheet management?
```

Không được suy `large USD buy = bullish USD view` một cách máy móc.

## 2. Forward price không phải market forecast thuần túy

Trong covered-interest-parity intuition, forward rate liên kết với spot và hai interest rates.

Với quote A/B, một representation đơn giản có dạng:

```text
F = S × (1 + r_B T) / (1 + r_A T)
```

Exact convention phụ thuộc day count, compounding và quote direction. Nhưng ý nghĩa cốt lõi là:

```text
Forward rate
≈ spot rate
adjusted for relative funding return
```

Vì vậy:

```text
Forward ≠ expected future spot
```

Forward có thể cao/thấp hơn spot chỉ vì interest differential, ngay cả khi market expectation về future spot không cùng hướng.

## 3. Forward points

Market thường quote:

```text
Forward = Spot + Forward Points
```

Forward points reflect principalmente:

```text
interest-rate differential
+ tenor
+ basis / funding pressure
+ liquidity / balance-sheet cost
```

Khi phân tích carry, phải tách:

```text
spot return
from
forward / funding component
```

Nếu không, một backtest có thể gọi financing return là directional alpha.

## 4. Covered Interest Parity — CIP

Textbook no-arbitrage logic so sánh hai paths.

Path A:

```text
hold/invest currency A
```

Path B:

```text
borrow A
→ exchange into B at spot
→ invest B
→ lock B back into A with forward
```

Nếu markets frictionless, covered returns phải gần bằng nhau sau conversion. Nếu không, arbitrageur theoretically có thể lock return difference.

## 5. Vì sao CIP có thể không khớp hoàn hảo

Real institutional market có constraints:

```text
counterparty limits
collateral terms
regulatory capital
leverage-ratio cost
balance-sheet scarcity
transaction costs
credit spreads
funding fragmentation
capital controls
```

Do đó actual forward/swap pricing có thể lệch khỏi simple textbook parity.

## 6. Cross-currency basis

**Cross-currency basis** là adjustment cần thêm để actual synthetic funding economics khớp market prices.

Trực giác:

```text
Direct USD funding cost
may differ from
Synthetic USD funding via FX swap
```

Nếu many institutions urgently need USD funding, synthetic USD can become expensive relative to textbook parity.

Basis vì thế là một window vào funding pressure và dealer intermediation capacity.

## 7. Basis không phải simple spot trading signal

Một basis move có thể đến từ:

```text
USD funding demand
hedging demand
quarter-end balance-sheet constraints
collateral scarcity
risk-off deleveraging
regulatory reporting dates
```

Không có mapping universal:

```text
basis wider → spot must go up/down
```

Need identify mechanism first.

## 8. FX swap khác currency swap

FX swap thường gồm:

```text
near leg
+
far leg reversing currency exchange
```

Nó thường phục vụ short-to-medium funding/liquidity transformation.

Cross-currency swap thường dài hạn hơn và có interest legs, principal exchanges và richer collateral/credit structure.

Không được dùng hai tên thay thế nhau tùy tiện.

## 9. FX swap là financial plumbing

Large FX swap turnover cho thấy Forex không chỉ là directional speculation.

Banks, asset managers và corporations dùng FX swaps để:

```text
obtain currency funding
roll hedges
manage liquidity
transform liability currency
```

Điều này giải thích vì sao institutional FX activity có thể rất lớn ngay cả khi spot directional conviction thấp.

## 10. Tenor curve

Funding không có một maturity duy nhất.

Typical tenors:

```text
ON / TN
1W
1M
3M
6M
1Y
```

Different tenors can show different pressure.

A 1Y point may reflect medium-horizon rate differential while ON/TN can be dominated by settlement/calendar/liquidity effects.

## 11. Settlement calendars matter

FX settlement requires two currency calendars.

Maturity calculation depends on:

```text
spot date
currency holidays
business-day convention
tenor convention
```

A one-day date error can materially change short-dated swap points.

Backtest must not treat every calendar day as tradable/settleable.

## 12. Quarter-end and year-end effects

Dealer balance sheet can become expensive near reporting dates.

Then:

```text
intermediation capacity ↓
→ FX swap / basis pricing can distort
```

If a strategy sees recurring basis moves around calendar dates, do not immediately call it structural alpha. It may be funding/accounting seasonality.

## 13. Collateral currency matters

Two OTC derivatives with same headline payoff can differ in value if collateral terms differ.

Why?

Because collateral determines funding/discounting economics.

Need know:

```text
CSA terms
collateral currency
margin frequency
counterparty credit
clearing status
```

Public market quotes are simplifications relative to bilateral institutional contracts.

## 14. Counterparty and credit limits

Even when an apparent arbitrage exists, institution may be unable to scale it because:

```text
credit line exhausted
counterparty limit reached
balance sheet constrained
collateral unavailable
```

Thus “why doesn't arbitrage close this?” often has a balance-sheet answer.

## 15. NDF — Non-Deliverable Forward

NDF is a forward contract that settles net cash difference instead of delivering full principal currencies.

Typical structure:

```text
Agree notional + forward rate today
→ observe fixing/reference rate at maturity
→ settle net difference in settlement currency
```

It is especially relevant where local currency is not freely deliverable/offshore accessible.

## 16. Why NDF markets exist

NDFs help market participants hedge/speculate when there are constraints such as:

```text
limited convertibility
capital controls
onshore access restrictions
local-currency delivery limits
```

Therefore NDF pricing can contain policy/access information not present in freely deliverable G10 forwards.

## 17. NDF is not retail CFD

Both may settle cash, but economics and legal structure differ.

NDF has defined:

```text
maturity
fixing source
determination date
settlement currency
notional
forward rate
```

Retail CFD/rolling FX often has ongoing financing and broker-specific margin/execution terms.

Do not merge them into one product category.

## 18. Fixing convention is part of the instrument

For an NDF, P/L depends on contractual fixing.

Research must store:

```text
fixing source
fixing timestamp
valuation date
settlement date
quote direction
```

Using arbitrary daily close instead of official fixing can produce a backtest that does not correspond to the contract.

## 19. Onshore vs offshore market

A currency may have:

```text
onshore spot/forward
+
offshore NDF
```

with different participants, hours, regulations and funding conditions.

Price discovery can shift between them by time zone and policy regime.

## 20. Onshore-offshore basis

Difference between onshore and offshore pricing can reflect:

```text
capital-control wedge
convertibility constraints
liquidity differential
hedging demand
intervention expectation
offshore positioning
```

Persistent difference does not automatically mean arbitrage because the arbitrage route itself may be restricted.

## 21. Capital controls change arbitrage space

Textbook parity assumes capital can move freely.

If participant cannot legally/operationally:

```text
borrow local currency
move it offshore
access deliverable forward
bring proceeds back
```

then price gaps can persist without being exploitable.

Constraint is part of the economic model.

## 22. Synthetic funding

Institution can fund currency via direct borrowing or synthetic FX swap.

Compare:

```text
Direct borrowing rate
vs
Synthetic borrowing implied by FX swap
```

The spread between them can reveal funding scarcity or balance-sheet friction.

## 23. USD funding channel

USD is deeply used in global finance. During stress:

```text
USD funding demand ↑
→ swap/basis pressure
→ hedging cost ↑
→ dealer balance-sheet strain
```

This can coexist with spot USD strength, but the relationship is not an identity.

## 24. Central-bank swap lines

Central-bank swap lines can provide foreign-currency liquidity to alleviate funding stress.

Important distinction:

```text
Funding-liquidity support
≠ spot FX intervention aimed at exchange-rate level
```

Do not label every central-bank FX-related operation “intervention”.

## 25. Corporate hedge flow

Exporter with foreign-currency receivable may sell FX forward. Importer with future payable may buy forward.

These flows are often risk management, not speculation.

Therefore:

```text
hedging flow
≠ directional macro view
```

## 26. Asset-manager hedge ratios

A global bond/equity investor may vary hedge ratio over time.

Changes in hedge ratio can create large forward demand even when underlying asset position is unchanged.

This connects asset allocation to FX forward markets.

## 27. Hedge-return decomposition

For foreign asset investor:

```text
Local asset return
+ spot FX return
+ forward/hedge P&L
+ carry / basis
− transaction cost
```

A “currency-hedged return” without roll/funding cost is incomplete.

## 28. Rolling forwards

Most hedges are not one-shot forever. Short-dated forward hedges must be rolled.

Roll outcome depends on:

```text
forward curve
spot at roll
spread
liquidity
basis
```

This creates path dependency in long-horizon hedged returns.

## 29. Spot, forward and NDF return series are not interchangeable

Before research, define object precisely:

```text
spot return
forward excess return
NDF return
futures return
retail rolling P/L
```

A strategy tested on one instrument cannot be assumed executable identically on another.

## 30. Academic carry vs retail carry

Academic carry research often uses forward rates.

Retail implementation may use broker swap/rollover with:

```text
markup
triple-swap calendar
broker credit terms
instrument-specific financing
```

Bridge from academic return to real execution explicitly.

## 31. Data alignment

Institutional study should align:

```text
spot bid/ask
forward points
money-market/OIS rates
basis
fixing data
holiday calendars
```

Unsynchronized timestamps can create fake arbitrage.

## 32. Bid/ask matters for parity tests

Mid-price parity deviations may disappear after executable spreads.

No-arbitrage research should use bid/ask and realistic funding, not just midpoint algebra.

## 33. Common NDF backtest errors

Typical mistakes:

```text
using spot close instead of fixing
mixing tenors
ignoring holidays
assuming onshore deliverability
ignoring capital controls
stitching different regimes blindly
```

## 34. Common basis research errors

Typical mistakes:

```text
wrong benchmark rate
wrong quote sign
unsynchronized timestamps
ignoring collateral
ignoring quarter-end effects
assuming basis is directional alpha
```

## 35. Good research questions

Examples:

```text
Does offshore NDF lead onshore price during local-market closure?
How does basis behave during USD funding stress?
How stable is carry after realistic forward/roll cost?
Does hedge demand change around large cross-border asset flows?
```

Each needs point-in-time data and explicit identification limits.

## 36. Connection map

Read with:

- [`../01_MARKET_STRUCTURE_AND_INSTRUMENTS.md`](../01_MARKET_STRUCTURE_AND_INSTRUMENTS.md)
- [`../04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md`](../04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)
- [`../10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md`](../10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)
- [`../../03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md`](../../03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md)
- [`../../../04_economics/README.md`](../../../04_economics/README.md)

General monetary/funding theory belongs to Economics; this file owns FX-specific implementation and instrument interpretation.

## 37. Mental checklist

Before interpreting forward/NDF/basis, ask:

1. Deliverable or non-deliverable?
2. Quote direction?
3. Tenor and settlement date?
4. Which rate benchmarks?
5. What basis/funding pressure?
6. Which collateral/counterparty assumptions?
7. Onshore/offshore access constraints?
8. Which fixing?
9. Are timestamps synchronized?
10. Is the flow hedge, funding or directional?

## 38. Kết luận

Spot chart chỉ là một layer của FX. Forward points, FX swaps, NDF và basis cho thấy foreign exchange cũng là **funding infrastructure**.

Nếu không hiểu funding, convertibility và settlement conventions, researcher dễ nhầm hedging flow với signal, capital-control wedge với arbitrage và financing return với directional edge.
