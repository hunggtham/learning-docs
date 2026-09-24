# 04 — Macro drivers, interest rates, carry và trading sessions

Một currency pair là **giá tương đối giữa hai đồng tiền**. Vì vậy không có một biến đơn lẻ kiểu “lãi suất tăng thì currency tăng” có thể dùng như quy luật cơ học.

Mental model phù hợp hơn là:

```text
New Information
→ changes expected economic path
→ changes expected central-bank path / risk premium / capital flows
→ changes relative return of holding currencies and assets
→ portfolio hedging / rebalancing / speculation
→ FX price adjustment
```

Price phản ứng với **chênh lệch giữa điều thị trường đã kỳ vọng và thông tin mới**, không chỉ với mức của một chỉ số kinh tế.

## 1. Forex là bài toán relative macro

Phân tích EUR/USD không phải:

```text
Eurozone economy is strong?
```

mà gần hơn với:

```text
Eurozone outlook
relative to
US outlook
```

Các biến quan trọng cũng nên được đặt theo relative terms:

```text
Expected ECB path vs expected Fed path
European growth vs US growth
Euro real yields vs US real yields
European risk premium vs US risk premium
Capital demand for EUR assets vs USD assets
```

Một nền kinh tế có thể tăng trưởng tốt nhưng currency vẫn giảm nếu phía đối diện cải thiện mạnh hơn hoặc market đã price in kết quả tốt trước đó.

## 2. Current policy rate không đủ

Trader mới thường nhìn:

```text
Fed rate = X
ECB rate = Y
```

rồi suy luận currency có lãi suất cao hơn sẽ mạnh hơn.

Market lại định giá **expected path**.

Ví dụ central bank đang giữ policy rate 5%, nhưng market trước đó kỳ vọng giữ 5% thêm sáu tháng. Nếu data mới khiến market tin rate cuts sẽ bắt đầu sớm hơn và sâu hơn, short-term yields có thể giảm ngay dù current policy rate chưa thay đổi.

FX có thể phản ứng trước cuộc họp chính thức vì expectation đã đổi.

Mental model:

```text
Spot FX today
responds partly to
expected future policy / rates
not only today's policy rate
```

## 3. Central-bank reaction function

**Hàm phản ứng của ngân hàng trung ương (central-bank reaction function)** là cách policy maker có xu hướng phản ứng với inflation, labor market, growth, financial stability và mandate của mình.

Không nên học kiểu:

```text
CPI high → hike → currency up
```

Hãy hỏi:

```text
Actual data
vs prior expectation
→ changes inflation/growth assessment by how much?
→ does that change policy reaction function/path?
→ how much was already priced into rates?
→ what is happening on the other currency side?
```

Một CPI cao nhưng thấp hơn fear scenario có thể làm yields và currency giảm. Một CPI giảm nhưng vẫn cao hơn consensus có thể tạo phản ứng ngược lại.

## 4. Surprise quan trọng hơn headline level trong ngắn hạn

Giả sử consensus CPI YoY là 3.0%.

Case A:

```text
Actual = 3.4%
```

Case B:

```text
Actual = 2.7%
```

Cùng một country, cùng một release, nhưng signal đối với expected policy có thể trái ngược.

Trong event-driven analysis, cần ghi:

```text
Previous
Consensus
Actual
Revision
Market pricing before release
Market reaction after release
```

Không chỉ ghi actual number.

## 5. Nominal yield và real yield

**Lợi suất danh nghĩa (nominal yield)** chưa trừ inflation expectation.

Một approximation:

```text
Real Yield
≈ Nominal Yield - Expected Inflation
```

Nếu nominal yield tăng vì inflation expectation tăng mạnh hơn, real return có thể không cải thiện.

Currency valuation và capital flows có thể nhạy với real yield, nhưng relation thay đổi theo regime, risk sentiment và hedging cost.

Vì vậy:

```text
higher nominal yield
≠ automatically stronger currency
```

## 6. Yield differential

Một **chênh lệch lợi suất (yield differential)** so sánh yields giữa hai currency areas ở maturity phù hợp.

Ví dụ conceptual:

```text
US 2Y yield - Germany 2Y yield
```

có thể cung cấp information về relative monetary-policy expectations có liên quan EUR/USD.

Nhưng correlation không cố định. Một pair còn chịu:

- risk premium;
- capital flows;
- reserve demand;
- external balance;
- fiscal concerns;
- hedging flows;
- positioning;
- geopolitical shocks.

Yield spread là một explanatory variable, không phải universal trading signal.

## 7. Forward points và interest-rate differential

Trong simplified no-arbitrage framework, spot và forward liên hệ với interest rates của hai currencies.

Nếu quote là `A/B`, một representation của covered interest parity có dạng gần:

```text
F = S × (1 + r_B × T) / (1 + r_A × T)
```

với convention chính xác phụ thuộc cách định nghĩa pair/rates/day count.

Ý nghĩa quan trọng hơn công thức: nếu hai currencies có funding return khác nhau, forward rate phải điều chỉnh để ngăn arbitrage đơn giản.

Do đó forward price **không phải đơn thuần market forecast của future spot**.

## 8. Carry trade

**Carry** là return liên quan đến chênh lệch financing/yield khi nắm exposure qua thời gian.

Carry trade thường được mô tả đơn giản:

```text
borrow low-yield currency
buy high-yield currency
```

Nếu spot không đi ngược quá mạnh, trader có thể hưởng carry. Nhưng high yield thường không phải “free money”. Nó có thể bù cho:

- inflation risk;
- devaluation risk;
- sovereign/political risk;
- liquidity risk;
- crash risk.

Một currency có yield cao có thể mất giá mạnh đúng lúc risk-off, xóa nhiều tháng carry trong vài ngày.

## 9. Uncovered interest parity và carry puzzle

Một textbook intuition nói rằng currency có interest rate cao hơn có xu hướng depreciate đủ để offset yield advantage trong expectation, nếu không sẽ tồn tại easy excess return.

Thực nghiệm FX historically cho thấy relation này không ổn định; carry strategies từng tạo excess returns trong nhiều sample nhưng đi kèm crash/tail risk và regime dependence.

Bài học không phải “UIP sai nên carry luôn thắng”. Bài học là:

```text
interest differential
+ expected depreciation
+ risk premium
+ tail risk
```

phải được xem cùng nhau.

## 10. Growth differential

Growth mạnh có thể hỗ trợ currency qua nhiều kênh:

```text
stronger demand
→ higher expected rates
→ stronger asset returns / capital inflows
→ currency demand
```

Nhưng growth mạnh cũng có thể:

```text
widen imports / current-account deficit
or
already be fully priced
```

Không có deterministic mapping.

Điểm cần theo dõi là **growth surprise relative to the other economy and to expectations**.

## 11. Inflation: cùng headline nhưng khác mechanism

Inflation tăng do demand overheating khác inflation tăng do supply shock.

### Demand-driven inflation

Có thể làm central bank hawkish hơn nếu growth vẫn mạnh.

### Supply shock

Ví dụ energy import shock có thể vừa tăng inflation vừa làm household real income giảm, khiến policy trade-off khó hơn.

Vì vậy currency reaction cần phân tích:

```text
source of inflation
→ policy response
→ growth effect
→ real yield
→ external balance
```

## 12. Labor-market data

Employment, unemployment, wage growth, vacancies và participation có thể ảnh hưởng policy expectations.

Ví dụ US payroll data không chỉ là số jobs. Market có thể chú ý:

- payroll change;
- revisions;
- unemployment rate;
- labor-force participation;
- average hourly earnings;
- hours worked.

Một headline “strong” nhưng revisions yếu và wage pressure giảm có thể tạo interpretation khác.

## 13. Balance of payments

Một country liên hệ với thế giới qua current account và financial/capital flows.

Simplified:

```text
Current-account flows
+
Financial-account flows
→ demand/supply for currency
```

Country có trade surplus không tự động có appreciating currency vì residents có thể đầu tư capital ra nước ngoài hoặc central bank có thể can thiệp/reserve accumulation.

Cần nhìn cả hai phía.

## 14. Current account

**Cán cân vãng lai (current account)** gồm trade in goods/services, primary income và transfers.

Persistent deficit nghĩa là country cần counterpart financing từ abroad hoặc asset sales/capital inflows theo accounting identity.

Nếu foreign funding confidence giảm đột ngột, currency có thể chịu pressure mạnh — đặc biệt khi external debt, short-term funding hoặc reserve adequacy yếu.

## 15. Capital flows

Flows có thể đến từ:

- foreign direct investment;
- portfolio equity;
- bonds;
- bank lending;
- derivatives hedging;
- reserve management.

Không phải mọi inflow có cùng stability.

FDI thường có horizon dài hơn hot-money portfolio flows. Short-term leveraged flows có thể đảo chiều nhanh khi volatility tăng.

## 16. Risk-on / risk-off chỉ là shorthand

Market commentary thường gọi một currency “risk-on” hoặc “safe haven”. Những nhãn này hữu ích như shorthand nhưng không nên trở thành law.

Một currency có thể phản ứng khác nhau tùy:

- source của shock;
- domestic exposure;
- funding role;
- external balance;
- rate differential;
- positioning;
- intervention expectation.

Nên hỏi mechanism thay vì gắn label cố định.

## 17. Funding currencies

Currency có low funding cost đôi khi được dùng để finance positions ở tài sản/currencies có expected return cao hơn.

Khi risk sentiment đảo chiều:

```text
leveraged positions unwind
→ funding currency shorts are covered
→ funding currency may strengthen
```

Đây là một mechanism giúp giải thích một số safe-haven-like moves mà không cần giả định investor “thích” currency đó về fundamental.

## 18. Commodity-linked currencies

Một economy xuất khẩu nhiều commodity có thể có currency nhạy với terms of trade.

Ví dụ conceptual:

```text
commodity export price rises
→ export income improves
→ trade balance / corporate income may improve
→ currency-supportive flow may increase
```

Nhưng relation còn phụ thuộc:

- import side;
- hedging;
- fiscal policy;
- global risk appetite;
- China/global demand;
- domestic policy.

Không nên trade chỉ vì dầu/gold tăng mà bỏ qua context.

## 19. Terms of trade

**Điều kiện thương mại (terms of trade)** so sánh export prices với import prices.

Nếu country xuất khẩu commodity A và nhập khẩu energy B, relative price changes có thể thay đổi national income ngay cả khi export volume không đổi.

FX có thể phản ánh redistribution này thông qua expected trade balance, income và policy.

## 20. Fiscal policy cũng có thể tác động FX theo nhiều hướng

Fiscal expansion có thể:

```text
support growth
→ push yields higher
→ attract capital
```

nhưng cũng có thể:

```text
raise debt concern / inflation risk
→ increase term/risk premium
→ weaken confidence
```

Phản ứng phụ thuộc starting conditions và monetary-policy interaction.

Không có rule “deficit tăng = currency giảm” hoạt động mọi thời điểm.

## 21. Political/geopolitical events nên được phân tích qua channels

Thay vì viết:

> geopolitical tension → USD up

hãy tách:

```text
Shock
→ energy/commodity prices?
→ trade disruption?
→ growth expectations?
→ inflation expectations?
→ safe-asset demand?
→ funding stress?
→ policy response?
```

FX reaction đến từ channels cụ thể và positioning, không phải từ tên của event.

## 22. Market expectation là hidden variable quan trọng

Một central bank hike 25 bps:

- nếu market expected 50 bps → có thể bị đọc là dovish surprise;
- nếu market expected 0 bps → có thể là hawkish surprise;
- nếu 25 bps đã fully priced → reaction có thể nhỏ;
- guidance sau cuộc họp có thể quan trọng hơn hike hiện tại.

Do đó event notebook nên lưu **pre-event pricing**.

## 23. Positioning

Hai market có cùng fundamental news nhưng reaction khác nhau nếu positioning khác.

Nếu market đã extremely long currency A, thêm positive news có thể chỉ tạo limited buying, trong khi mild disappointment kích hoạt crowded exit.

Positioning không nói intrinsic value, nhưng ảnh hưởng **path** của price adjustment.

## 24. Sessions và participant mix

FX gần như liên tục trong business week, nhưng không có cùng participant mix 24/5.

Một simplified sequence:

```text
Asia
→ Europe/London
→ New York
→ late US / Asia handoff
```

Các trung tâm overlap làm liquidity và information processing thay đổi.

Ví dụ:

- Asian hours thường quan trọng với JPY, AUD, NZD, CNH và regional flows;
- London là một trung tâm FX rất lớn;
- New York overlap với London thường có nhiều macro releases và liquidity lớn ở USD pairs.

Đây là tendency, không phải guarantee mỗi ngày.

## 25. Daylight-saving time là research problem thật

Nếu backtest “London open breakout” bằng fixed UTC/local hour mà không xử lý DST, dataset có thể trộn hai market states khác nhau theo mùa.

Time-series pipeline nên lưu timezone-aware timestamps và map session theo actual financial-centre clock.

## 26. Fixing flows

Institutional benchmark fixing windows có thể tập trung hedging/rebalancing orders vào thời điểm nhất định.

Điều này có thể tạo temporary volume/volatility mà không nhất thiết phản ánh new macro information.

Bài học:

```text
price move
≠ always new fundamental information
```

Có thể là mechanical flow.

## 27. Month-end / quarter-end rebalancing

Large portfolios thay đổi FX hedge hoặc rebalance asset weights quanh reporting periods.

Ví dụ equity market A outperform market B có thể làm international portfolio weights drift, dẫn đến hedging flow cuối tháng.

Không nên biến month-end effect thành deterministic signal. Cần xác định:

- expected flow;
- size relative to liquidity;
- whether market already anticipates it;
- historical conditional distribution.

## 28. Central-bank intervention

Một central bank có thể tham gia FX market để giảm disorderly moves, influence exchange-rate conditions hoặc thực hiện policy framework tùy jurisdiction.

Intervention có thể là:

- direct transaction;
- verbal communication;
- liquidity operation;
- coordinated action.

Hiệu quả phụ thuộc credibility, size, monetary-policy consistency và market regime.

Không nên coi một price level là guaranteed defense line nếu authority không cam kết như vậy.

## 29. Managed/fixed exchange-rate regimes khác free float

Không phải mọi currency đều free-float giống EUR/USD.

Có các frameworks như:

```text
free float
managed float
crawling arrangement
peg / band
capital controls
```

Với managed currency, policy objective, reserves, capital controls và offshore/onshore market distinction có thể quan trọng hơn textbook technical analysis.

## 30. CNH và CNY minh họa market segmentation

Một currency có thể có onshore/offshore markets với accessibility, liquidity và policy constraints khác nhau.

Do đó ticker gần giống nhau không có nghĩa instrument fungibility hoàn hảo.

Market structure phải được hiểu trước khi áp dụng model.

## 31. Korea context: USD/KRW

Với USD/KRW:

```text
USD/KRW rises
→ one USD buys more KRW
→ KRW weakens relative to USD
```

Các channels có thể bao gồm:

- Fed/BOK expected-rate differential;
- Korean export cycle;
- semiconductor/global trade conditions;
- energy import cost;
- foreign portfolio flows;
- broad USD move;
- global risk sentiment;
- domestic policy/intervention expectations.

Đây là context để hiểu terminology, không phải trading rule.

Một số thuật ngữ Hàn Quốc:

- tỷ giá: **환율**;
- đồng won mạnh lên: **원화 강세**;
- đồng won yếu đi: **원화 약세**;
- chênh lệch lãi suất: **금리차**;
- dòng vốn: **자본 흐름**;
- can thiệp ngoại hối: **외환시장 개입**.

## 32. Một event-analysis template

Khi có macro event, ghi theo chain:

```text
1. Prior market narrative
2. Consensus expectation
3. Actual data / decision
4. Revision / details
5. Immediate rates reaction
6. Equity / credit / commodity reaction
7. FX reaction
8. Positioning / liquidity context
9. Follow-through after 1h / 1d / 1w
10. Was the original causal hypothesis supported?
```

Template này giúp tránh hindsight story kiểu “giá tăng nên chắc do X”.

## 33. Ví dụ causal chain: inflation surprise

Giả sử US CPI cao hơn consensus đáng kể.

Một possible chain:

```text
Higher CPI surprise
→ market prices fewer/ later Fed cuts
→ front-end Treasury yields rise
→ USD rate advantage increases
→ USD strengthens
```

Nhưng chain có thể đứt nếu:

```text
inflation surprise is supply-driven
+ growth fear dominates
+ market already extremely long USD
+ risk-off creates other flows
```

Do đó causal chain là hypothesis phải kiểm tra, không phải guarantee.

## 34. Ví dụ causal chain: weak growth but stronger currency

GDP data yếu nhưng currency vẫn tăng có thể xảy ra nếu:

```text
data was less weak than feared
or
weakness reduces import demand
or
safe-haven/funding unwind dominates
or
other side of pair deteriorates more
or
positioning forces short covering
```

Price không “sai” chỉ vì một textbook rule không hoạt động.

## 35. Macro model tốt phải có invalidation

Một FX thesis nên viết như:

```text
Observation:
Market prices X rate cuts.

Hypothesis:
Inflation/labor data will keep policy tighter than priced.

Transmission:
Higher expected front-end yields
→ relative yield support
→ currency demand.

Risks:
Growth shock, global risk-off, positioning, opposite-side repricing.

Invalidation:
Data/policy path moves materially against hypothesis.
```

Đây là research structure tốt hơn “RSI oversold nên buy”.

## 36. Carry return phải tách khỏi spot return

FX total return của leveraged/carry position có thể conceptualize:

```text
Total Return
≈ Spot Move
+ Carry / Financing
- Transaction Cost
```

Nếu strategy kiếm tiền nhờ spot move nhưng mất carry, hoặc ngược lại, performance attribution phải tách hai nguồn.

Nếu không, trader có thể hiểu sai edge.

## 37. Regime dependence

Một relation như:

```text
yield differential ↑ → currency ↑
```

có thể mạnh trong monetary-policy divergence regime nhưng yếu khi crisis liquidity dominates.

Do đó research cần conditioning variables:

- volatility regime;
- growth regime;
- inflation regime;
- policy divergence;
- risk sentiment;
- liquidity stress.

Correlation full-sample có thể che nhiều sub-regimes trái nhau.

## 38. Checklist trước khi sang execution/broker risk

Bạn cần tự giải thích được:

1. Vì sao FX là relative macro.
2. Vì sao expected rate path quan trọng hơn chỉ current policy rate.
3. Vì sao surprise vs consensus ảnh hưởng event reaction.
4. Nominal và real yield khác nhau thế nào.
5. Forward points liên hệ interest differential nhưng không đơn thuần forecast spot.
6. Carry kiếm return từ đâu và crash risk đến từ đâu.
7. Current account và capital flows liên kết currency demand như thế nào.
8. Vì sao risk-on/safe-haven chỉ là shorthand.
9. Vì sao sessions/DST ảnh hưởng backtest.
10. Vì sao flow-driven move không nhất thiết là fundamental information.

## Nối sang chương tiếp theo

Macro giải thích **vì sao participant muốn thay đổi exposure**. Chương tiếp theo giải thích **lệnh đó được truyền qua broker/dealer như thế nào, chi phí thực tế hình thành ở đâu và vì sao execution/counterparty risk có thể phá một strategy đúng về direction**.

→ [05 — Execution, brokers, costs and operational risk](./05_EXECUTION_BROKERS_COSTS_AND_RISK.md)

## Internal links

- [Macro Data Playbook](../../04_economics/03_MACRO_DATA_PLAYBOOK.md)
- [Global Economy, Capital Flows and Crisis](../../04_economics/02_GLOBAL_ECONOMY_CAPITAL_FLOWS_AND_CRISIS.md)
- [Monetary System, Liquidity and Crisis Transmission](../../04_economics/04_MONETARY_SYSTEM_LIQUIDITY_AND_CRISIS_TRANSMISSION.md)
- [03 — Leverage, margin and position sizing](./03_LEVERAGE_MARGIN_POSITION_SIZING.md)
- [Glossary, formulas and research conventions](../../00_GLOSSARY_FORMULAS_AND_RESEARCH_CONVENTIONS.md)
