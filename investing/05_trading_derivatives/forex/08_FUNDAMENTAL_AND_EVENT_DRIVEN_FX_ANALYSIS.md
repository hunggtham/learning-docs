# 08 — Fundamental và event-driven FX analysis

Fundamental FX analysis không phải danh sách quy tắc kiểu “CPI tăng → currency tăng”. Nó là bài toán **expectation, relative valuation và transmission**: dữ liệu mới thay đổi kỳ vọng về tăng trưởng, lạm phát, chính sách, dòng vốn và risk premium như thế nào so với phía còn lại của currency pair.

Mental model:

```text
Prior expectations
→ new information
→ repricing of policy / growth / risk
→ rates and asset-price reaction
→ flows / hedging
→ FX reaction
→ follow-through or reversal
```

## 1. Event outcome không đủ; surprise mới quan trọng

Một data release có ba lớp:

```text
Previous
Consensus / market expectation
Actual
```

Thêm vào đó còn:

- revisions;
- composition/detail;
- market positioning;
- policy reaction function;
- mức đã được price in trước event.

Ví dụ CPI 3.0% có thể hawkish nếu consensus 2.7%, nhưng dovish nếu market feared 3.4%.

## 2. “Market expectation” phải được ghi lại trước event

Nếu chỉ xem chart sau event rồi giải thích, rất dễ tạo hindsight narrative.

Event notebook nên lưu trước release:

```text
Consensus
Rate-path pricing if available
Recent central-bank guidance
Positioning proxies
Recent trend / volatility
Key alternative scenarios
```

Sau event mới ghi reaction.

## 3. Central-bank reaction function

Mỗi central bank có mandate, framework và constraints khác nhau. Cần hiểu họ phản ứng với:

- inflation outlook;
- labor market;
- growth;
- financial stability;
- exchange-rate pass-through;
- credit/housing conditions;
- fiscal/financial-system stress.

Một decision chỉ có meaning khi đặt trong reaction function.

## 4. Current rate khác expected path

FX thường phản ứng với thay đổi của **expected future rate path**, không chỉ current policy rate.

Ví dụ:

```text
Rate unchanged today
but guidance becomes more hawkish
→ expected future rates rise
→ front-end yields may rise
→ currency may strengthen
```

Ngược lại, hike hiện tại nhưng dovish future guidance có thể tạo reaction trái dấu.

## 5. FOMC/ECB/BOK event nên đọc theo nhiều layer

Một central-bank event có thể gồm:

```text
Policy decision
Statement language
Economic projections
Press conference
Implementation details
Balance-sheet guidance
```

Không nên lấy headline rate decision làm toàn bộ event.

Nguồn canonical nên là website chính thức của central bank. Với Fed, lịch FOMC, statements, minutes và projection materials được công bố theo calendar chính thức; với ECB/BOK cũng nên dùng press release/decision chính thức thay vì chỉ secondary headline.

## 6. CPI

Không chỉ đọc headline CPI. Tùy economy, market có thể chú ý:

- headline;
- core;
- services;
- housing/rent components;
- goods;
- energy;
- month-on-month momentum;
- annualized short-run measures.

Causal chain cần hỏi:

```text
Which component surprised?
Persistent or temporary?
Does it alter policy path?
Does it alter real growth?
```

## 7. Employment data

Employment release có thể chứa:

- payroll/employment change;
- unemployment rate;
- participation;
- wages;
- hours worked;
- revisions.

Nếu headline jobs mạnh nhưng prior months revised sharply down và wage growth weakens, interpretation khác headline alone.

## 8. GDP

GDP là broad activity measure nhưng có lag và revisions. FX có thể phản ứng nhiều hơn với forward-looking components hoặc high-frequency data nếu GDP đã anticipated.

Một strong GDP print không tự động bullish nếu:

- driven by inventories;
- already priced;
- inflation implications are dovish;
- other side of pair is stronger.

## 9. PMI / business surveys

PMI-like surveys có thể cung cấp earlier signal về activity, orders, employment, prices và sentiment.

Nhưng survey diffusion indices không phải GDP growth rate trực tiếp. Cần hiểu construction và historical relationship.

## 10. Retail sales / consumption

Consumption data ảnh hưởng growth outlook và đôi khi inflation pressure.

Nhưng nominal sales có thể tăng vì prices tăng, không phải real volume. Nếu có thể, phân biệt nominal và real.

## 11. Inflation expectations

Market-based hoặc survey inflation expectations ảnh hưởng real yields và policy pricing.

Một nominal yield tăng 30 bps nhưng expected inflation tăng 40 bps có thể làm real yield giảm.

Do đó FX analysis cần nhìn decomposition khi relevant.

## 12. Yield curve

Different maturities encode different combinations của:

- expected policy rates;
- inflation expectations;
- term premium;
- risk/liquidity premium.

FX short-horizon event reaction thường nhạy với front-end repricing, nhưng medium-term thesis có thể liên quan broader curve.

## 13. OIS / money-market pricing

Overnight-indexed instruments thường được dùng để infer market-implied policy expectations.

Không nên đọc implied path như certainty. Nó là price incorporating expectations và risk premia.

## 14. Surprise index

Một economic surprise index tổng hợp actual-vs-consensus across releases.

Nó có thể giúp đo liệu data flow đang systematically vượt hay hụt expectation, nhưng construction/source khác nhau và không phải direct trading signal.

## 15. Relative data surprise

Với currency pair A/B, có thể nghiên cứu:

```text
Surprise_A - Surprise_B
```

thay vì chỉ surprise của một economy.

Đây phù hợp với bản chất relative của FX.

## 16. Trade balance và current account

Trade surplus/deficit không tự động quyết định currency. Cần xem:

```text
Trade/current-account flow
+
Portfolio/FDI/bank flows
+
Hedging
+
Reserve/intervention activity
```

Balance of payments là system, không phải một dòng headline.

## 17. Terms of trade

Commodity import/export prices có thể thay đổi national income và external balance.

Một energy-importing economy có thể chịu:

```text
energy price shock
→ import bill rises
→ trade balance deteriorates
→ inflation rises
→ growth weakens
```

FX effect phụ thuộc policy response và market pricing.

## 18. Fiscal news

Budget, tax, spending hoặc debt issuance có thể tác động qua:

- growth;
- inflation;
- bond supply;
- term premium;
- sovereign risk;
- central-bank response.

Không dùng rule đơn giản “fiscal expansion bullish/bearish currency”.

## 19. Geopolitical shock

Thay vì gắn label “risk-off”, tách channels:

```text
Energy shock?
Trade disruption?
Safe-asset demand?
Funding stress?
Growth hit?
Inflation hit?
Policy reaction?
```

Cùng một geopolitical event có thể tác động khác nhau tới JPY, EUR, KRW, CHF, USD tùy origin và exposure.

## 20. Intervention risk

Với currencies nơi authority có thể can thiệp, cần theo dõi official communication và policy framework.

Không được biến một level được báo chí nhắc đến thành “guaranteed defense line”.

Intervention thesis phải ghi:

- official statements;
- historical mechanism;
- reserve/liquidity capacity if relevant;
- policy consistency;
- market positioning.

## 21. Fixing và benchmark flows

Một move quanh benchmark fixing có thể đến từ mechanical execution/rebalancing thay vì new macro information.

Event analysis phải phân biệt:

```text
information shock
versus
flow shock
```

vì expected persistence có thể khác nhau.

## 22. Options market như expectation proxy

FX options có thể cung cấp information về:

- implied volatility;
- event premium;
- skew/risk reversal;
- demand for asymmetric protection.

Nhưng implied volatility không phải direct probability forecast không điều chỉnh; nó chứa risk premium và market microstructure.

## 23. Event volatility

Trước major release, implied/realized volatility expectation có thể tăng.

Sau release:

```text
uncertainty resolves
→ implied volatility can fall
```

Vì vậy directional view đúng chưa chắc option trade có profit nếu option premium quá cao. Phần này nối với chapter FX options sau.

## 24. First reaction và second reaction

Event có thể có:

```text
0–5 seconds: algorithmic headline reaction
5 min–1h: detail interpretation / liquidity normalization
1d–1w: broader repricing
```

Strategy horizon phải xác định mình nghiên cứu layer nào.

Không nên backtest daily close rồi suy luận về edge vài giây quanh release.

## 25. Revisions

Macro data có thể được revised. Backtest dùng final revised dataset có nguy cơ **look-ahead / vintage bias** nếu live trader lúc đó chỉ biết first release.

Event research nên dùng point-in-time vintage data khi possible.

## 26. Release timestamp

Timestamp phải đúng timezone và daylight-saving convention.

Nếu một release xảy ra lúc 08:30 New York time, UTC timestamp thay đổi theo DST. Data pipeline phải dùng timezone-aware conversion.

## 27. Information leakage / pre-release moves

Nếu price move trước scheduled release, có nhiều explanations:

- unrelated market flow;
- positioning adjustment;
- correlated information;
- rumor;
- leakage in rare cases.

Không nên tự động kết luận cause từ chart.

Research cần event window và control windows.

## 28. Event study framework

Một basic event study:

```text
Define event timestamp
Define surprise variable
Define pre-event state
Measure returns in windows:
[-60m, 0]
[0, +5m]
[0, +60m]
[0, +1d]
Normalize by volatility
Include bid/ask cost
Group by surprise magnitude / regime
```

Sau đó kiểm tra distribution, không chỉ average.

## 29. Conditional response

Một hawkish surprise có thể tạo USD reaction khác khi:

- USD positioning already extreme;
- risk crisis dominates;
- surprise comes from inflation vs growth;
- event was anticipated.

Do đó regression/event study có thể include interactions.

## 30. Narrative phải được falsifiable

Bad thesis:

> USD sẽ tăng vì Fed hawkish.

Better thesis:

```text
Market prices X cuts over horizon H.
Incoming inflation/labor data are likely to keep policy tighter than priced.
If front-end yield differential widens beyond threshold Y while risk regime remains normal, USD should receive relative support.
Invalidation: data and policy pricing move opposite, or USD fails to respond despite widening differential over specified horizon.
```

## 31. Event journal

Một record nên có:

```text
Event
Timestamp
Prior consensus
Actual
Revision
Key detail
Pre-event rates pricing
Pre-event FX level/spread
Immediate rates reaction
Immediate FX reaction
1h / 1d follow-through
Execution cost
Original hypothesis
What was wrong/right
```

## 32. Official sources first

Đối với central-bank decisions và macro releases, hierarchy nên ưu tiên:

```text
Official central bank / statistical agency
→ official release/API
→ high-quality data vendor
→ reputable secondary analysis
→ social media only as discovery, not source of record
```

Tài liệu cần phân biệt fact với analyst interpretation.

## 33. Không trade headline text bằng cảm giác

Một word như “hawkish” hoặc “dovish” là compressed interpretation. Hai analysts có thể disagree.

Nếu research NLP/event signal, cần formalize text features và train/test chronologically, không label bằng future market reaction.

## 34. Scheduled vs unscheduled events

Scheduled:

- CPI;
- labor data;
- central-bank meetings;
- GDP/PMI.

Unscheduled:

- surprise intervention;
- political/geopolitical shock;
- emergency policy action;
- financial accident.

Unscheduled events có tail/execution risk lớn hơn vì market chưa chuẩn bị liquidity giống scheduled event.

## 35. Fundamental analysis không loại bỏ technical/execution layer

Một macro thesis có thể đúng trong tuần nhưng entry execution tệ làm trade thất bại.

Pipeline đầy đủ:

```text
Fundamental hypothesis
→ expected horizon
→ market-price confirmation or timing rule
→ position sizing
→ execution
→ attribution
```

Không nên dùng fundamental story để bỏ stop/invalidation.

## 36. Current-source examples

Khi học bằng dữ liệu hiện hành, luôn lấy ngày cụ thể. Ví dụ calendar FOMC chính thức liệt kê meeting dates, statements, minutes và projection materials theo từng kỳ; ECB và Bank of Korea cũng công bố policy decisions trực tiếp. Những tài liệu này thích hợp để xây event dataset hơn bài báo tóm tắt.

Không copy current policy rate vào tài liệu như một fact vĩnh viễn; nếu cần ví dụ thời điểm phải ghi rõ ngày.

## 37. Checklist

Bạn cần tự giải thích được:

1. Actual khác surprise như thế nào.
2. Vì sao expected rate path quan trọng hơn headline rate.
3. Reaction function là gì.
4. Vì sao revisions gây vintage bias.
5. Vì sao event timestamp/DST quan trọng.
6. First reaction và follow-through khác nhau.
7. Flow shock khác information shock thế nào.
8. Cách viết một fundamental thesis có invalidation.
9. Vì sao official source nên là source of record.

## Đọc tiếp

→ [09 — Carry, momentum, value and macro FX strategies](./09_CARRY_MOMENTUM_VALUE_AND_MACRO_FX_STRATEGIES.md)

## Nguồn nền

- Federal Reserve — FOMC calendars and official monetary-policy releases: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
- ECB — Monetary policy decisions: https://www.ecb.europa.eu/press/govcdec/mopo/html/index.en.html
- Bank of Korea — Monetary Policy Decisions: https://www.bok.or.kr/eng/main/contents.do?menuNo=400015
- [Macro Data Playbook](../../04_economics/03_MACRO_DATA_PLAYBOOK.md)
- [04 — Macro drivers, rates, carry and sessions](./04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)
