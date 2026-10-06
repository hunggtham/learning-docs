# Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Unhedged foreign asset** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Return decomposition** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối global asset manager với currency hedge, để exposure, benchmark, instrument và hedge effectiveness được đo trên cùng dòng tiền.

Một investor Hàn Quốc có thể nắm US equities, European bonds hoặc toàn cục (global / 전역) multi-asset portfolio. Khi reporting currency là KRW, total return không chỉ đến từ cục bộ (local / 로컬) asset. Nó còn đến từ FX.

Mô hình tư duy (mental model / 사고 모델):

```text
Local Asset Return
+ Currency Return
+ Hedge P/L
+ Hedge Carry / Forward Points
- Transaction Cost
= Investor Return in Reporting Currency
```

Currency hedge vì vậy không đơn giản là “xóa FX”. Nó thay đổi phân phối (distribution / 분포), carry, benchmark tracking và liquidity requirements của portfolio.

## 1. Unhedged foreign asset

Giả sử Korean fund đầu tư:

```text
USD asset value = 100m USD
Reporting currency = KRW
USD/KRW spot = 1,360
```

Initial KRW giá trị (value / 값):

```text
136bn KRW
```

Portfolio có hai main exposures:

```text
Underlying US asset
+ USD/KRW
```

> **Nối mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **2. Return decomposition** nối từ **1. Unhedged foreign asset** sang **3. Example unhedged**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Return decomposition

Approximate simple-return decomposition:

```text
KRW Return
≈ Local Asset Return
+ USD/KRW Return
+ interaction term
```

Chính xác (exact / 정확한) multiplicative relationship:

```text
(1 + R_KRW)
= (1 + R_USD_asset) × (1 + R_USD/KRW)
```

So:

```text
R_KRW
= R_asset + R_fx + R_asset × R_fx
```

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **2. Return decomposition** nêu quy tắc; **3. Example unhedged** thử quy tắc trong tình huống, rồi **4. Opposite scenario** mở rộng hệ quả.

## 3. Example unhedged

US asset rises 10% in USD.

KRW strengthens 8% against USD, meaning USD/KRW falls approximately 8%.

Approximate KRW return:

```text
1.10 × 0.92 - 1
≈ +1.2%
```

Cục bộ (local / 로컬) asset gained 10%, but currency nearly erased kết quả (result / 결과) for KRW investor.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **3. Example unhedged** nêu quy tắc; **4. Opposite scenario** thử quy tắc trong tình huống, rồi **5. Full currency hedge concept** mở rộng hệ quả.

## 4. Opposite scenario

US asset falls 5%, but USD strengthens 12% vs KRW:

```text
0.95 × 1.12 - 1
≈ +6.4%
```

Investor can gain in KRW despite cục bộ (local / 로컬) asset mất mát (loss / 손실).

This is why local-market hiệu năng (performance / 성능) is not investor return.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **5. Full currency hedge concept** nối từ **4. Opposite scenario** sang **6. Hedge ratio**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Full currency hedge concept

Fund can approximately hedge USD asset giá trị (value / 값) by:

```text
Sell USD forward
Buy KRW forward
```

notional close to USD exposure.

Goal:

```text
reduce sensitivity of KRW portfolio value to USD/KRW
```

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **6. Hedge ratio** nối từ **5. Full currency hedge concept** sang **7. Asset giá trị (value / 값) drift creates hedge mismatch**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Hedge ratio

Define:

```text
Hedge Ratio
= FX Hedge Notional / Foreign-Currency Asset Exposure
```

Examples:

```text
0%   unhedged
50%  partial hedge
100% fully hedged approximately
```

“100%” is still approximate because asset giá trị (value / 값) changes between rebalances.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **7. Asset giá trị (value / 값) drift creates hedge mismatch** nối từ **6. Hedge ratio** sang **8. Rebalancing hedge**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Asset giá trị (value / 값) drift creates hedge mismatch

At start:

```text
Asset = 100m USD
Hedge = 100m USD
```

Asset rises 20%:

```text
Asset = 120m USD
Hedge remains = 100m USD
```

Now portfolio has residual:

```text
+20m USD unhedged
```

This is **hedge drift**.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **8. Rebalancing hedge** nối từ **7. Asset giá trị (value / 값) drift creates hedge mismatch** sang **9. Hedge ratio is a strategic allocation quyết định (decision / 결정)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Rebalancing hedge

Chính sách (policy / 정책) might rebalance:

```text
monthly
weekly
when hedge ratio leaves tolerance band
```

More frequent rebalancing reduces drift but increases turnover/chi phí (cost / 비용).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **9. Hedge ratio is a strategic allocation quyết định (decision / 결정)** nối từ **8. Rebalancing hedge** sang **10. Liability currency matters**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Hedge ratio is a strategic allocation quyết định (decision / 결정)

Choosing 0%, 50% or 100% changes portfolio rủi ro (risk / 위험) profile.

It should be based on:

```text
Investor liabilities
Strategic benchmark
Currency volatility
Asset-currency correlation
Carry/funding economics
Liquidity
Risk tolerance
```

not only short-term FX forecast.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **10. Liability currency matters** nối từ **9. Hedge ratio is a strategic allocation quyết định (decision / 결정)** sang **11. Bonds vs equities**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Liability currency matters

A Korean pension with KRW liabilities may giá trị (value / 값) KRW stability more than a toàn cục (global / 전역) investor with USD liabilities.

Same foreign asset can have different optimal hedge chính sách (policy / 정책) depending on liabilities.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **11. Bonds vs equities** nối từ **10. Liability currency matters** sang **12. Hedge carry**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Bonds vs equities

Currency volatility can be large relative to bond volatility.

Example:

```text
Foreign bond expected volatility = low/moderate
FX volatility = comparable or larger
```

Unhedged currency can dominate bond portfolio rủi ro (risk / 위험).

For equities, cục bộ (local / 로컬) asset volatility is larger, so relative contribution differs.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **12. Hedge carry** nối từ **11. Bonds vs equities** sang **13. Hedged return approximation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Hedge carry

Forward hedge return includes forward points.

A Korean investor hedging USD back to KRW may face positive or negative carry depending on relative rates/basis.

Do not treat hedge return as simply `-spot FX return`.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **13. Hedged return approximation** nối từ **12. Hedge carry** sang **14. Forward points vs spot view**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Hedged return approximation

Conceptually:

```text
Hedged Portfolio Return
≈ Local Asset Return
+ Hedge Carry
+ Hedge Slippage/Basis Error
- Transaction Cost
```

Currency spot tác động (effect / 효과) is largely offset, not perfectly eliminated.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **14. Forward points vs spot view** nối từ **13. Hedged return approximation** sang **15. Benchmark consistency**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Forward points vs spot view

A 100% currency hedge can underperform unhedged portfolio when USD rises strongly.

That does not imply hedge failed.

The benchmark/mục tiêu (objective / 목표) determines evaluation.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **15. Benchmark consistency** nối từ **14. Forward points vs spot view** sang **16. Active vs strategic currency position**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Benchmark consistency

If fund benchmark is currency-hedged chỉ mục (index / 인덱스) but manager holds unhedged assets:

```text
manager has active currency risk
```

Even if asset selection matches benchmark.

Conversely, hedging a benchmark that is unhedged creates active FX position.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **16. Active vs strategic currency position** nối từ **15. Benchmark consistency** sang **17. Currency overlay**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Active vs strategic currency position

Separate:

```text
Strategic hedge ratio
from
Tactical currency overlay
```

If manager changes hedge ratio based on FX view, that active quyết định (decision / 결정) should be attributed separately.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **17. Currency overlay** nối từ **16. Active vs strategic currency position** sang **18. Netting across portfolios**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Currency overlay

A centralized overlay desk can manage currency exposure across multiple asset portfolios.

Benefits:

```text
netting
lower duplicate hedges
centralized risk
consistent execution
```

But it introduces quản trị (governance / 거버넌스) and attribution độ phức tạp (complexity / 복잡도).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **18. Netting across portfolios** nối từ **17. Currency overlay** sang **19. Cross hedge**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Netting across portfolios

Portfolio A long USD 100m.

Portfolio B economically short USD 30m.

At firm mức (level / 수준):

```text
net USD exposure = 70m
```

Centralized hedge can reduce gross transactions if mandates allow.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **19. Cross hedge** nối từ **18. Netting across portfolios** sang **20. NDF hedge**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Cross hedge

If direct hedge thị trường (market / 시장) is illiquid, manager may hedge with correlated currency.

Example conceptual:

```text
illiquid EM currency exposure
→ hedge partly with regional/broad USD proxy
```

This creates **basis rủi ro (risk / 위험)** because correlation is imperfect and regime-dependent.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **20. NDF hedge** nối từ **19. Cross hedge** sang **21. Rolling forwards**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. NDF hedge

For non-deliverable/restricted currency exposure, NDF may be used.

Need mô hình (model / 모델):

```text
fixing source
settlement currency
onshore/offshore basis
capital-control/access constraints
```

NDF return can differ from onshore spot move.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **21. Rolling forwards** nối từ **20. NDF hedge** sang **22. Roll rủi ro (risk / 위험)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Rolling forwards

If fund holds asset indefinitely but forward matures every 1–3 months:

```text
asset horizon = long
hedge tenor = short
```

Hedge must roll repeatedly.

Long-run kết quả (result / 결과) depends on chuỗi (sequence / 시퀀스) of forward points and roll thực thi (execution / 실행).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **22. Roll rủi ro (risk / 위험)** nối từ **21. Rolling forwards** sang **23. Collateral and variation margin**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Roll rủi ro (risk / 위험)

At each maturity:

```text
close/mature old forward
open next forward
```

During stress:

```text
spread widens
basis moves
credit line tightens
liquidity declines
```

So hedge that reduced spot FX rủi ro (risk / 위험) can introduce funding/liquidity rủi ro (risk / 위험).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **23. Collateral and variation margin** nối từ **22. Roll rủi ro (risk / 위험)** sang **24. Example collateral mismatch**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Collateral and variation margin

Depending instrument/CSA/clearing cấu trúc (structure / 구조), hedge can require collateral when marked against fund.

Important paradox:

```text
Underlying foreign asset may gain from FX move
while derivative loses and requires cash collateral now
```

Economic hedge can still create short-term liquidity need.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **23. Collateral and variation margin** nêu quy tắc; **24. Example collateral mismatch** thử quy tắc trong tình huống, rồi **25. Hedge ratio and liquidity buffer** mở rộng hệ quả.

## 24. Example collateral mismatch

USD strengthens strongly.

For KRW investor with short USD forward:

```text
foreign asset KRW value rises
forward loses
```

If asset is not immediately liquid but derivative margin is due daily:

```text
liquidity mismatch
```

can matter even though combined net worth is protected.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **24. Example collateral mismatch** nêu quy tắc; **25. Hedge ratio and liquidity buffer** thử quy tắc trong tình huống, rồi **26. Currency-asset correlation** mở rộng hệ quả.

## 25. Hedge ratio and liquidity buffer

A 100% hedge may require larger collateral buffer than 50% hedge.

Rủi ro (risk / 위험) chính sách (policy / 정책) should include:

```text
FX risk reduction
vs
liquidity requirement
```

not just volatility tối ưu hóa (optimization / 최적화).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **26. Currency-asset correlation** nối từ **25. Hedge ratio and liquidity buffer** sang **27. Correlation is not stable**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Currency-asset correlation

If foreign asset tends to fall when USD rises, unhedged USD may provide diversification for KRW investor.

If hedge removes USD exposure, portfolio volatility could increase in some regimes.

Therefore:

```text
currency risk is not always pure uncompensated noise
```

Its tương tác (interaction / 상호작용) with asset return matters.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **27. Correlation is not stable** nối từ **26. Currency-asset correlation** sang **28. Safe-haven currencies**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Correlation is not stable

A currency that hedged equity drawdowns historically may not do so next crisis.

Stress-test multiple correlation regimes.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **28. Safe-haven currencies** nối từ **27. Correlation is not stable** sang **29. Multi-currency portfolio**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. Safe-haven currencies

JPY, CHF, USD can behave differently across crises depending funding and shock nguồn (source / 소스).

Do not hard-code “safe haven” into hedge chính sách (policy / 정책) without scenario phân tích (analysis / 분석).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **29. Multi-currency portfolio** nối từ **28. Safe-haven currencies** sang **30. Trading currency vs economic currency**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. Multi-currency portfolio

Portfolio:

```text
USD assets 50%
EUR assets 20%
JPY assets 10%
Other currencies 20%
```

Need currency exposure by underlying economic currency, not listing venue only.

A US-listed ETF can own non-USD assets.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **30. Trading currency vs economic currency** nối từ **29. Multi-currency portfolio** sang **31. Look-through độ sâu (depth / 깊이)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. Trading currency vs economic currency

Ticker trades in USD does not imply portfolio exposure is USD only.

For international equity ETF:

```text
Trading currency = USD
Underlying company revenues/assets = multiple currencies
```

Direct portfolio FX hedge usually targets fund NAV currency exposure according to fund mechanics, not every corporate revenue exposure inside holdings.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **31. Look-through độ sâu (depth / 깊이)** nối từ **30. Trading currency vs economic currency** sang **32. Share-class hedge**, vì cơ chế trước tạo đầu vào cho bước sau.

## 31. Look-through độ sâu (depth / 깊이)

Decide whether rủi ro (risk / 위험) hệ thống (system / 시스템) uses:

```text
fund share-class currency
fund NAV currency
underlying asset currency
company revenue currency
```

Each mức (level / 수준) answers different question.

Do not mix them.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **32. Share-class hedge** nối từ **31. Look-through độ sâu (depth / 깊이)** sang **33. Hedge effectiveness chỉ số (metric / 지표)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. Share-class hedge

Some funds offer currency-hedged share classes.

Investor must understand hedge typically targets share-class currency exposure, not all economic FX exposure of underlying companies.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **33. Hedge effectiveness chỉ số (metric / 지표)** nối từ **32. Share-class hedge** sang **34. Cash inflow/outflow**, vì cơ chế trước tạo đầu vào cho bước sau.

## 33. Hedge effectiveness chỉ số (metric / 지표)

Measure difference between:

```text
Actual hedged portfolio return
vs
Ideal benchmark hedged return
```

Attribution:

```text
hedge ratio drift
forward points
transaction cost
roll timing
basis
cash flows
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **33. Hedge effectiveness chỉ số (metric / 지표)** đặt đầu vào cho **34. Cash inflow/outflow**, rồi **35. Thị trường (market / 시장) move between NAV and hedge thực thi (execution / 실행)** mở rộng hệ quả hoặc giới hạn liên quan.

## 34. Cash inflow/outflow

Subscriptions/redemptions thay đổi (change / 변경) foreign asset exposure.

If hedge is not adjusted promptly:

```text
fund becomes over/under-hedged
```

Cash-flow forecasting matters.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **34. Cash inflow/outflow** đặt đầu vào cho **35. Thị trường (market / 시장) move between NAV and hedge thực thi (execution / 실행)**, rồi **36. Time-zone challenge** mở rộng hệ quả hoặc giới hạn liên quan.

## 35. Thị trường (market / 시장) move between NAV and hedge thực thi (execution / 실행)

If NAV is measured at one cutoff but hedge rebalances later:

```text
timing basis
```

can create tracking lỗi (error / 오류).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **36. Time-zone challenge** nối từ **35. Thị trường (market / 시장) move between NAV and hedge thực thi (execution / 실행)** sang **37. Weekend gap**, vì cơ chế trước tạo đầu vào cho bước sau.

## 36. Time-zone challenge

Toàn cục (global / 전역) assets close at different cục bộ (local / 로컬) times.

FX trades nearly 24/5.

Define consistent exposure snapshot and hedge-rebalance timestamp.

This is a point-in-time các hệ thống (systems / 시스템들) bài toán (problem / 문제).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **37. Weekend gap** nối từ **36. Time-zone challenge** sang **38. Stress scenario**, vì cơ chế trước tạo đầu vào cho bước sau.

## 37. Weekend gap

Foreign asset thị trường (market / 시장) may close while FX or another thị trường (market / 시장) reprices at different times.

Hedge and asset liquidity are not synchronized perfectly.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **38. Stress scenario** nối từ **37. Weekend gap** sang **39. Partial hedge scenario**, vì cơ chế trước tạo đầu vào cho bước sau.

## 38. Stress scenario

Kiểm thử (test / 테스트):

```text
Global equities -25%
USD/KRW +15%
EUR/USD -10%
JPY strengthens 12%
FX spreads 3x
Forward basis widens
Collateral call increases
```

Calculate:

```text
Local asset P/L
FX P/L
Hedge P/L
Collateral requirement
Net portfolio P/L
Liquidity buffer
```

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **39. Partial hedge scenario** nối từ **38. Stress scenario** sang **40. Strategic hedge quyết định (decision / 결정) khung phần mềm (framework / 프레임워크)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 39. Partial hedge scenario

Compare 0%, 50%, 100% USD hedge across:

```text
USD +15%
USD unchanged
USD -15%
```

with cục bộ (local / 로컬) asset +10%/-10% combinations.

Observe that hedge ratio changes phân phối (distribution / 분포), not absolute “chất lượng (quality / 품질)”.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **40. Strategic hedge quyết định (decision / 결정) khung phần mềm (framework / 프레임워크)** nối từ **39. Partial hedge scenario** sang **41. Attribution report**, vì cơ chế trước tạo đầu vào cho bước sau.

## 40. Strategic hedge quyết định (decision / 결정) khung phần mềm (framework / 프레임워크)

```text
Liability currency
Benchmark
Asset class volatility
Currency volatility
Asset-FX correlation
Carry
Liquidity/collateral
Operational capacity
Regulatory/tax/accounting constraints
```

No universal hedge ratio.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **41. Attribution report** nối từ **40. Strategic hedge quyết định (decision / 결정) khung phần mềm (framework / 프레임워크)** sang **42. What not to learn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 41. Attribution report

```text
Local asset return
FX spot contribution
Forward/carry contribution
Hedge ratio drift
Roll cost
Spread/slippage
Collateral/funding cost
Tactical overlay P/L
Net investor return
```

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **42. What not to learn** nối từ **41. Attribution report** sang **43. Trường hợp (case / 사례) outputs**, vì cơ chế trước tạo đầu vào cho bước sau.

## 42. What not to learn

Wrong:

```text
100% hedge always lowers risk.
```

Wrong:

```text
If USD rises, currency hedge was a mistake.
```

Wrong:

```text
Fund traded in USD means USD is the only FX exposure.
```

Better:

```text
Currency hedge must be evaluated relative to liabilities,
benchmark, asset behavior, carry and liquidity constraints.
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **42. What not to learn** nêu quy tắc; **43. Trường hợp (case / 사례) outputs** thử quy tắc trong tình huống, rồi **44. Rà soát (review / 검토) questions** mở rộng hệ quả.

## 43. Trường hợp (case / 사례) outputs

Create:

```text
asset_currency_exposure_map.md
hedge_ratio_policy.md
forward_roll_schedule.md
hedged_unhedged_scenario_matrix.md
collateral_liquidity_stress.md
currency_attribution_report.md
benchmark_tracking_report.md
```

> **Nối mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **43. Trường hợp (case / 사례) outputs** nêu quy tắc; **44. Rà soát (review / 검토) questions** thử quy tắc trong tình huống, rồi **Nội bộ (internal / 내부) links** mở rộng hệ quả.

## 44. Rà soát (review / 검토) questions

Explain:

1. Why cục bộ (local / 로컬) asset return differs from KRW investor return.
2. Why 100% hedge drifts after asset price changes.
3. Why hedge carry belongs in return attribution.
4. Why a derivative mất mát (loss / 손실) can accompany successful hedge.
5. Why collateral creates liquidity rủi ro (risk / 위험) even for economically hedged portfolio.
6. Why benchmark currency treatment matters.
7. Why listing/trading currency is not always economic exposure.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **Nội bộ (internal / 내부) links** nối từ **44. Rà soát (review / 검토) questions** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Nội bộ (internal / 내부) links

- [Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
- [Funding, NDF, basis and forward curve](../90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md)
- [Systematic risk and attribution engine](../70_systematic_project/03_PORTFOLIO_RISK_AND_ATTRIBUTION_ENGINE.md)

> **Bàn giao:** Sau **Nội bộ (internal / 내부) links**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
