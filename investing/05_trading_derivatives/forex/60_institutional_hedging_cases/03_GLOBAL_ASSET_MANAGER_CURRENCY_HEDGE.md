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

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **2. Return decomposition** tiếp nhận điểm tựa từ **1. Unhedged foreign asset** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Example unhedged** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **2. Return decomposition** cho ta quy tắc; **3. Example unhedged** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **4. Opposite scenario** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Example unhedged

US asset rises 10% in USD.

KRW strengthens 8% against USD, meaning USD/KRW falls approximately 8%.

Approximate KRW return:

```text
1.10 × 0.92 - 1
≈ +1.2%
```

Cục bộ (local / 로컬) asset gained 10%, but currency nearly erased kết quả (result / 결과) for KRW investor.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **3. Example unhedged** cho ta quy tắc; **4. Opposite scenario** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **5. Full currency hedge concept** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Opposite scenario

US asset falls 5%, but USD strengthens 12% vs KRW:

```text
0.95 × 1.12 - 1
≈ +6.4%
```

Investor can gain in KRW despite cục bộ (local / 로컬) asset mất mát (loss / 손실).

This is why local-market hiệu năng (performance / 성능) is not investor return.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **5. Full currency hedge concept** tiếp nhận điểm tựa từ **4. Opposite scenario** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Hedge ratio** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **6. Hedge ratio** tiếp nhận điểm tựa từ **5. Full currency hedge concept** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Asset giá trị (value / 값) drift creates hedge mismatch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **7. Asset giá trị (value / 값) drift creates hedge mismatch** tiếp nhận điểm tựa từ **6. Hedge ratio** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Rebalancing hedge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **8. Rebalancing hedge** tiếp nhận điểm tựa từ **7. Asset giá trị (value / 값) drift creates hedge mismatch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Hedge ratio is a strategic allocation quyết định (decision / 결정)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Rebalancing hedge

Chính sách (policy / 정책) might rebalance:

```text
monthly
weekly
when hedge ratio leaves tolerance band
```

More frequent rebalancing reduces drift but increases turnover/chi phí (cost / 비용).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **9. Hedge ratio is a strategic allocation quyết định (decision / 결정)** tiếp nhận điểm tựa từ **8. Rebalancing hedge** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Liability currency matters** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **10. Liability currency matters** tiếp nhận điểm tựa từ **9. Hedge ratio is a strategic allocation quyết định (decision / 결정)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Bonds vs equities** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Liability currency matters

A Korean pension with KRW liabilities may giá trị (value / 값) KRW stability more than a toàn cục (global / 전역) investor with USD liabilities.

Same foreign asset can have different optimal hedge chính sách (policy / 정책) depending on liabilities.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **11. Bonds vs equities** tiếp nhận điểm tựa từ **10. Liability currency matters** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Hedge carry** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Bonds vs equities

Currency volatility can be large relative to bond volatility.

Example:

```text
Foreign bond expected volatility = low/moderate
FX volatility = comparable or larger
```

Unhedged currency can dominate bond portfolio rủi ro (risk / 위험).

For equities, cục bộ (local / 로컬) asset volatility is larger, so relative contribution differs.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **12. Hedge carry** tiếp nhận điểm tựa từ **11. Bonds vs equities** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Hedged return approximation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Hedge carry

Forward hedge return includes forward points.

A Korean investor hedging USD back to KRW may face positive or negative carry depending on relative rates/basis.

Do not treat hedge return as simply `-spot FX return`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **13. Hedged return approximation** tiếp nhận điểm tựa từ **12. Hedge carry** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Forward points vs spot view** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **14. Forward points vs spot view** tiếp nhận điểm tựa từ **13. Hedged return approximation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Benchmark consistency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Forward points vs spot view

A 100% currency hedge can underperform unhedged portfolio when USD rises strongly.

That does not imply hedge failed.

The benchmark/mục tiêu (objective / 목표) determines evaluation.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **15. Benchmark consistency** tiếp nhận điểm tựa từ **14. Forward points vs spot view** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Active vs strategic currency position** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Benchmark consistency

If fund benchmark is currency-hedged chỉ mục (index / 인덱스) but manager holds unhedged assets:

```text
manager has active currency risk
```

Even if asset selection matches benchmark.

Conversely, hedging a benchmark that is unhedged creates active FX position.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **16. Active vs strategic currency position** tiếp nhận điểm tựa từ **15. Benchmark consistency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Currency overlay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Active vs strategic currency position

Separate:

```text
Strategic hedge ratio
from
Tactical currency overlay
```

If manager changes hedge ratio based on FX view, that active quyết định (decision / 결정) should be attributed separately.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **17. Currency overlay** tiếp nhận điểm tựa từ **16. Active vs strategic currency position** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Netting across portfolios** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **18. Netting across portfolios** tiếp nhận điểm tựa từ **17. Currency overlay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Cross hedge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Netting across portfolios

Portfolio A long USD 100m.

Portfolio B economically short USD 30m.

At firm mức (level / 수준):

```text
net USD exposure = 70m
```

Centralized hedge can reduce gross transactions if mandates allow.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **19. Cross hedge** tiếp nhận điểm tựa từ **18. Netting across portfolios** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. NDF hedge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Cross hedge

If direct hedge thị trường (market / 시장) is illiquid, manager may hedge with correlated currency.

Example conceptual:

```text
illiquid EM currency exposure
→ hedge partly with regional/broad USD proxy
```

This creates **basis rủi ro (risk / 위험)** because correlation is imperfect and regime-dependent.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **20. NDF hedge** tiếp nhận điểm tựa từ **19. Cross hedge** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Rolling forwards** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **21. Rolling forwards** tiếp nhận điểm tựa từ **20. NDF hedge** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Roll rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Rolling forwards

If fund holds asset indefinitely but forward matures every 1–3 months:

```text
asset horizon = long
hedge tenor = short
```

Hedge must roll repeatedly.

Long-run kết quả (result / 결과) depends on chuỗi (sequence / 시퀀스) of forward points and roll thực thi (execution / 실행).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **22. Roll rủi ro (risk / 위험)** tiếp nhận điểm tựa từ **21. Rolling forwards** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Collateral and variation margin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **23. Collateral and variation margin** tiếp nhận điểm tựa từ **22. Roll rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Example collateral mismatch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Collateral and variation margin

Depending instrument/CSA/clearing cấu trúc (structure / 구조), hedge can require collateral when marked against fund.

Important paradox:

```text
Underlying foreign asset may gain from FX move
while derivative loses and requires cash collateral now
```

Economic hedge can still create short-term liquidity need.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **23. Collateral and variation margin** cho ta quy tắc; **24. Example collateral mismatch** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **25. Hedge ratio and liquidity buffer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **24. Example collateral mismatch** cho ta quy tắc; **25. Hedge ratio and liquidity buffer** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **26. Currency-asset correlation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Hedge ratio and liquidity buffer

A 100% hedge may require larger collateral buffer than 50% hedge.

Rủi ro (risk / 위험) chính sách (policy / 정책) should include:

```text
FX risk reduction
vs
liquidity requirement
```

not just volatility tối ưu hóa (optimization / 최적화).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **26. Currency-asset correlation** tiếp nhận điểm tựa từ **25. Hedge ratio and liquidity buffer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Correlation is not stable** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Currency-asset correlation

If foreign asset tends to fall when USD rises, unhedged USD may provide diversification for KRW investor.

If hedge removes USD exposure, portfolio volatility could increase in some regimes.

Therefore:

```text
currency risk is not always pure uncompensated noise
```

Its tương tác (interaction / 상호작용) with asset return matters.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **27. Correlation is not stable** tiếp nhận điểm tựa từ **26. Currency-asset correlation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Safe-haven currencies** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Correlation is not stable

A currency that hedged equity drawdowns historically may not do so next crisis.

Stress-test multiple correlation regimes.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **28. Safe-haven currencies** tiếp nhận điểm tựa từ **27. Correlation is not stable** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Multi-currency portfolio** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Safe-haven currencies

JPY, CHF, USD can behave differently across crises depending funding and shock nguồn (source / 소스).

Do not hard-code “safe haven” into hedge chính sách (policy / 정책) without scenario phân tích (analysis / 분석).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **29. Multi-currency portfolio** tiếp nhận điểm tựa từ **28. Safe-haven currencies** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Trading currency vs economic currency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **30. Trading currency vs economic currency** tiếp nhận điểm tựa từ **29. Multi-currency portfolio** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Look-through độ sâu (depth / 깊이)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Trading currency vs economic currency

Ticker trades in USD does not imply portfolio exposure is USD only.

For international equity ETF:

```text
Trading currency = USD
Underlying company revenues/assets = multiple currencies
```

Direct portfolio FX hedge usually targets fund NAV currency exposure according to fund mechanics, not every corporate revenue exposure inside holdings.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **31. Look-through độ sâu (depth / 깊이)** tiếp nhận điểm tựa từ **30. Trading currency vs economic currency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Share-class hedge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **32. Share-class hedge** tiếp nhận điểm tựa từ **31. Look-through độ sâu (depth / 깊이)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Hedge effectiveness chỉ số (metric / 지표)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Share-class hedge

Some funds offer currency-hedged share classes.

Investor must understand hedge typically targets share-class currency exposure, not all economic FX exposure of underlying companies.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **33. Hedge effectiveness chỉ số (metric / 지표)** tiếp nhận điểm tựa từ **32. Share-class hedge** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Cash inflow/outflow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **33. Hedge effectiveness chỉ số (metric / 지표)** xác định đầu vào; **34. Cash inflow/outflow** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **35. Thị trường (market / 시장) move between NAV and hedge thực thi (execution / 실행)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Cash inflow/outflow

Subscriptions/redemptions thay đổi (change / 변경) foreign asset exposure.

If hedge is not adjusted promptly:

```text
fund becomes over/under-hedged
```

Cash-flow forecasting matters.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **34. Cash inflow/outflow** xác định đầu vào; **35. Thị trường (market / 시장) move between NAV and hedge thực thi (execution / 실행)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **36. Time-zone challenge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Thị trường (market / 시장) move between NAV and hedge thực thi (execution / 실행)

If NAV is measured at one cutoff but hedge rebalances later:

```text
timing basis
```

can create tracking lỗi (error / 오류).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **36. Time-zone challenge** tiếp nhận điểm tựa từ **35. Thị trường (market / 시장) move between NAV and hedge thực thi (execution / 실행)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Weekend gap** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Time-zone challenge

Toàn cục (global / 전역) assets close at different cục bộ (local / 로컬) times.

FX trades nearly 24/5.

Define consistent exposure snapshot and hedge-rebalance timestamp.

This is a point-in-time các hệ thống (systems / 시스템들) bài toán (problem / 문제).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **37. Weekend gap** tiếp nhận điểm tựa từ **36. Time-zone challenge** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. Stress scenario** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Weekend gap

Foreign asset thị trường (market / 시장) may close while FX or another thị trường (market / 시장) reprices at different times.

Hedge and asset liquidity are not synchronized perfectly.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **38. Stress scenario** tiếp nhận điểm tựa từ **37. Weekend gap** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Partial hedge scenario** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **39. Partial hedge scenario** tiếp nhận điểm tựa từ **38. Stress scenario** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. Strategic hedge quyết định (decision / 결정) khung phần mềm (framework / 프레임워크)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Partial hedge scenario

Compare 0%, 50%, 100% USD hedge across:

```text
USD +15%
USD unchanged
USD -15%
```

with cục bộ (local / 로컬) asset +10%/-10% combinations.

Observe that hedge ratio changes phân phối (distribution / 분포), not absolute “chất lượng (quality / 품질)”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **40. Strategic hedge quyết định (decision / 결정) khung phần mềm (framework / 프레임워크)** tiếp nhận điểm tựa từ **39. Partial hedge scenario** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. Attribution report** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **41. Attribution report** tiếp nhận điểm tựa từ **40. Strategic hedge quyết định (decision / 결정) khung phần mềm (framework / 프레임워크)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. What not to learn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **42. What not to learn** tiếp nhận điểm tựa từ **41. Attribution report** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. Trường hợp (case / 사례) outputs** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **42. What not to learn** cho ta quy tắc; **43. Trường hợp (case / 사례) outputs** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **44. Rà soát (review / 검토) questions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **43. Trường hợp (case / 사례) outputs** cho ta quy tắc; **44. Rà soát (review / 검토) questions** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Nội bộ (internal / 내부) links** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. Rà soát (review / 검토) questions

Explain:

1. Why cục bộ (local / 로컬) asset return differs from KRW investor return.
2. Why 100% hedge drifts after asset price changes.
3. Why hedge carry belongs in return attribution.
4. Why a derivative mất mát (loss / 손실) can accompany successful hedge.
5. Why collateral creates liquidity rủi ro (risk / 위험) even for economically hedged portfolio.
6. Why benchmark currency treatment matters.
7. Why listing/trading currency is not always economic exposure.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Toàn cục (global / 전역) Asset Manager: Currency Hedge cho Foreign-Asset Portfolio**, **Nội bộ (internal / 내부) links** tiếp nhận điểm tựa từ **44. Rà soát (review / 검토) questions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Nội bộ (internal / 내부) links

- [Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
- [Funding, NDF, basis and forward curve](../90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md)
- [Systematic risk and attribution engine](../70_systematic_project/03_PORTFOLIO_RISK_AND_ATTRIBUTION_ENGINE.md)

> **Bàn giao:** Sau **Nội bộ (internal / 내부) links**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
