# FX Funding, NDF, Basis & Forward Curve — nối spot Forex với money thị trường (market / 시장) và funding

> **Mạch đọc:** Đọc **FX Funding, NDF, Basis & Forward Curve — nối spot Forex với money thị trường (market / 시장) và funding** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Spot direction và funding economics là hai thứ khác nhau** sang **2. Forward price không phải thị trường (market / 시장) forecast thuần túy**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Chapter cầu nối (bridge / 브리지) này không nằm trong tuyến tính (linear / 선형) tuyến (route / 경로) `01–15`. Nó tồn tại để trả lời một câu hỏi mà spot chart không trả lời được: **khi một tổ chức hedge, vay hoặc chuyển funding giữa hai đồng tiền, tỷ giá forward/NDF/basis được hình thành như thế nào và vì sao chúng có thể tách khỏi textbook parity?**

Đây là cầu nối (bridge / 브리지) giữa Forex, derivatives và macro funding. Nếu mục tiêu chỉ là hiểu retail spot mechanics, có thể đọc sau. Nếu muốn hiểu institutional FX, corporate hedging, KRW/VND offshore pricing hoặc USD funding stress, đây là phần bắt buộc.

Mô hình tư duy (mental model / 사고 모델):

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

Do đó khi nhìn luồng (flow / 흐름), cần hỏi trước:

```text
Directional position?
Hedge?
Funding transformation?
Liquidity management?
Regulatory balance-sheet management?
```

Không được suy `large USD buy = bullish USD view` một cách máy móc.

## 2. Forward price không phải thị trường (market / 시장) forecast thuần túy

Trong covered-interest-parity intuition, forward tỷ lệ (rate / 비율) liên kết với spot và hai interest rates.

Với quote A/B, một biểu diễn (representation / 표현) đơn giản có dạng:

```text
F = S × (1 + r_B T) / (1 + r_A T)
```

Chính xác (exact / 정확한) convention phụ thuộc day count, compounding và quote direction. Nhưng ý nghĩa cốt lõi là:

```text
Forward rate
≈ spot rate
adjusted for relative funding return
```

Vì vậy:

```text
Forward ≠ expected future spot
```

Forward có thể cao/thấp hơn spot chỉ vì interest differential, ngay cả khi thị trường (market / 시장) expectation về future spot không cùng hướng.

## 3. Forward points

Thị trường (market / 시장) thường quote:

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

Textbook no-arbitrage lô-gic (logic / 논리) so sánh hai paths.

Đường dẫn (path / 경로) A:

```text
hold/invest currency A
```

Đường dẫn (path / 경로) B:

```text
borrow A
→ exchange into B at spot
→ invest B
→ lock B back into A with forward
```

Nếu markets frictionless, covered returns phải gần bằng nhau sau conversion. Nếu không, arbitrageur theoretically có thể khóa (lock / 잠금) return difference.

## 5. Vì sao CIP có thể không khớp hoàn hảo

Real institutional thị trường (market / 시장) có các ràng buộc (constraints / 제약조건들):

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

**Cross-currency basis** là adjustment cần thêm để actual synthetic funding economics khớp thị trường (market / 시장) prices.

Trực giác:

```text
Direct USD funding cost
may differ from
Synthetic USD funding via FX swap
```

Nếu many institutions urgently need USD funding, synthetic USD can become expensive relative to textbook parity.

Basis vì thế là một cửa sổ (window / 윈도우) vào funding pressure và dealer intermediation sức chứa (capacity / 용량).

## 7. Basis không phải simple spot trading tín hiệu (signal / 신호)

Một basis move có thể đến từ:

```text
USD funding demand
hedging demand
quarter-end balance-sheet constraints
collateral scarcity
risk-off deleveraging
regulatory reporting dates
```

Không có ánh xạ (mapping / 매핑) universal:

```text
basis wider → spot must go up/down
```

Need identify cơ chế (mechanism / 메커니즘) first.

## 8. FX swap khác currency swap

FX swap thường gồm:

```text
near leg
+
far leg reversing currency exchange
```

Nó thường phục vụ short-to-medium funding/liquidity transformation.

Cross-currency swap thường dài hạn hơn và có interest legs, principal exchanges và richer collateral/credit cấu trúc (structure / 구조).

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

A 1Y điểm (point / 지점) may reflect medium-horizon tỷ lệ (rate / 비율) differential while ON/TN can be dominated by settlement/calendar/liquidity effects.

## 11. Settlement calendars matter

FX settlement requires two currency calendars.

Maturity calculation depends on:

```text
spot date
currency holidays
business-day convention
tenor convention
```

A one-day date lỗi (error / 오류) can materially thay đổi (change / 변경) short-dated swap points.

Backtest must not treat every calendar day as tradable/settleable.

## 12. Quarter-end and year-end effects

Dealer balance sheet can become expensive near reporting dates.

Then:

```text
intermediation capacity ↓
→ FX swap / basis pricing can distort
```

If a chiến lược (strategy / 전략) sees recurring basis moves around calendar dates, do not immediately lời gọi (call / 호출) it structural alpha. It may be funding/accounting seasonality.

## 13. Collateral currency matters

Two OTC derivatives with same headline payoff can differ in giá trị (value / 값) if collateral terms differ.

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

Công khai (public / 공개) thị trường (market / 시장) quotes are simplifications relative to bilateral institutional contracts.

## 14. Counterparty and credit limits

Even when an apparent arbitrage exists, institution may be unable to quy mô (scale / 규모) it because:

```text
credit line exhausted
counterparty limit reached
balance sheet constrained
collateral unavailable
```

Thus “why doesn't arbitrage close this?” often has a balance-sheet answer.

## 15. NDF — Non-Deliverable Forward

NDF is a forward đặc tả hợp đồng (contract / 계약) that settles net cash difference instead of delivering full principal currencies.

Typical cấu trúc (structure / 구조):

```text
Agree notional + forward rate today
→ observe fixing/reference rate at maturity
→ settle net difference in settlement currency
```

It is especially relevant where cục bộ (local / 로컬) currency is not freely deliverable/offshore accessible.

## 16. Why NDF markets exist

NDFs help thị trường (market / 시장) participants hedge/speculate when there are các ràng buộc (constraints / 제약조건들) such as:

```text
limited convertibility
capital controls
onshore access restrictions
local-currency delivery limits
```

Therefore NDF pricing can contain chính sách (policy / 정책)/truy cập (access / 접근) thông tin (information / 정보) not present in freely deliverable G10 forwards.

## 17. NDF is not retail CFD

Both may settle cash, but economics and legal cấu trúc (structure / 구조) differ.

NDF has defined:

```text
maturity
fixing source
determination date
settlement currency
notional
forward rate
```

Retail CFD/rolling FX often has ongoing financing and broker-specific margin/thực thi (execution / 실행) terms.

Do not merge them into one sản phẩm (product / 제품) category.

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

Using arbitrary daily close instead of official fixing can produce a backtest that does not correspond to the đặc tả hợp đồng (contract / 계약).

## 19. Onshore vs offshore thị trường (market / 시장)

A currency may have:

```text
onshore spot/forward
+
offshore NDF
```

with different participants, hours, regulations and funding conditions.

Price discovery can shift between them by thời gian (time / 시간) zone and chính sách (policy / 정책) regime.

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

Persistent difference does not automatically mean arbitrage because the arbitrage tuyến (route / 경로) itself may be restricted.

## 21. Capital controls thay đổi (change / 변경) arbitrage không gian (space / 공간)

Textbook parity assumes capital can move freely.

If participant cannot legally/operationally:

```text
borrow local currency
move it offshore
access deliverable forward
bring proceeds back
```

then price gaps can persist without being exploitable.

Ràng buộc (constraint / 제약조건) is part of the economic mô hình (model / 모델).

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

USD is deeply used in toàn cục (global / 전역) finance. During stress:

```text
USD funding demand ↑
→ swap/basis pressure
→ hedging cost ↑
→ dealer balance-sheet strain
```

This can coexist with spot USD strength, but the relationship is not an định danh (identity / 식별자).

## 24. Central-bank swap lines

Central-bank swap lines can provide foreign-currency liquidity to alleviate funding stress.

Important distinction:

```text
Funding-liquidity support
≠ spot FX intervention aimed at exchange-rate level
```

Do not label every central-bank FX-related thao tác (operation / 연산) “intervention”.

## 25. Corporate hedge luồng (flow / 흐름)

Exporter with foreign-currency receivable may sell FX forward. Importer with future payable may buy forward.

These flows are often rủi ro (risk / 위험) management, not speculation.

Therefore:

```text
hedging flow
≠ directional macro view
```

## 26. Asset-manager hedge ratios

A toàn cục (global / 전역) bond/equity investor may vary hedge ratio over thời gian (time / 시간).

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

A “currency-hedged return” without roll/funding chi phí (cost / 비용) is incomplete.

## 28. Rolling forwards

Most hedges are not one-shot forever. Short-dated forward hedges must be rolled.

Roll kết quả (outcome / 결과) depends on:

```text
forward curve
spot at roll
spread
liquidity
basis
```

This creates đường dẫn (path / 경로) phụ thuộc (dependency / 의존성) in long-horizon hedged returns.

## 29. Spot, forward and NDF return series are not interchangeable

Before research, define đối tượng (object / 객체) precisely:

```text
spot return
forward excess return
NDF return
futures return
retail rolling P/L
```

A chiến lược (strategy / 전략) tested on one instrument cannot be assumed executable identically on another.

## 30. Academic carry vs retail carry

Academic carry research often uses forward rates.

Retail hiện thực (implementation / 구현) may use broker swap/rollover with:

```text
markup
triple-swap calendar
broker credit terms
instrument-specific financing
```

Cầu nối (bridge / 브리지) from academic return to real thực thi (execution / 실행) explicitly.

## 31. dữ liệu (data / 데이터) alignment

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

## 33. dùng chung (common / 공통) NDF backtest errors

Typical mistakes:

```text
using spot close instead of fixing
mixing tenors
ignoring holidays
assuming onshore deliverability
ignoring capital controls
stitching different regimes blindly
```

## 34. dùng chung (common / 공통) basis research errors

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

Each needs point-in-time dữ liệu (data / 데이터) and tường minh (explicit / 명시적) identification limits.

## 36. liên kết (connection / 연결) map

Read with:

- [`../01_MARKET_STRUCTURE_AND_INSTRUMENTS.md`](../01_MARKET_STRUCTURE_AND_INSTRUMENTS.md)
- [`../04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md`](../04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)
- [`../10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md`](../10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)
- [`../../03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md`](../../03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md)
- [`../../../04_economics/README.md`](../../../04_economics/README.md)

General monetary/funding lý thuyết (theory / 이론) belongs to Economics; this tệp (file / 파일) owns FX-specific hiện thực (implementation / 구현) and instrument interpretation.

## 37. Mental checklist

Before interpreting forward/NDF/basis, ask:

1. Deliverable or non-deliverable?
2. Quote direction?
3. Tenor and settlement date?
4. Which tỷ lệ (rate / 비율) benchmarks?
5. What basis/funding pressure?
6. Which collateral/counterparty các giả định (assumptions / 가정들)?
7. Onshore/offshore truy cập (access / 접근) các ràng buộc (constraints / 제약조건들)?
8. Which fixing?
9. Are timestamps synchronized?
10. Is the luồng (flow / 흐름) hedge, funding or directional?

## 38. Kết luận

Spot chart chỉ là một tầng (layer / 계층) của FX. Forward points, FX swaps, NDF và basis cho thấy foreign exchange cũng là **funding hạ tầng (infrastructure / 인프라)**.

Nếu không hiểu funding, convertibility và settlement conventions, researcher dễ nhầm hedging luồng (flow / 흐름) với tín hiệu (signal / 신호), capital-control wedge với arbitrage và financing return với directional edge.

> **Bàn giao:** Sau **38. Kết luận**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 INTERVENTION RESERVES REER AND CURRENCY VALUATION](./01_INTERVENTION_RESERVES_REER_AND_CURRENCY_VALUATION.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
