# 04 — Macro drivers, interest rates, carry và trading sessions

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **04 — Macro drivers, interest rates, carry và trading sessions**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Forex là bài toán relative macro** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Hiện tại (current / 현재) chính sách (policy / 정책) tỷ lệ (rate / 비율) không đủ** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối macro drivers với rates, carry và sessions, để biến chênh lệch lãi suất và thời điểm thị trường thành giả thuyết FX có thể kiểm tra.

Một currency pair là **giá tương đối giữa hai đồng tiền**. Vì vậy không có một biến đơn lẻ kiểu “lãi suất tăng thì currency tăng” có thể dùng như quy luật cơ học.

Mô hình tư duy (mental model / 사고 모델) phù hợp hơn là:

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

Một nền kinh tế có thể tăng trưởng tốt nhưng currency vẫn giảm nếu phía đối diện cải thiện mạnh hơn hoặc thị trường (market / 시장) đã price in kết quả tốt trước đó.

> **Chuyển mạch:** Trong **04 — Macro drivers, interest rates, carry và trading sessions**, **2. Hiện tại (current / 현재) chính sách (policy / 정책) tỷ lệ (rate / 비율) không đủ** tiếp nhận điểm tựa từ **1. Forex là bài toán relative macro** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Central-bank reaction hàm (function / 함수)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Hiện tại (current / 현재) chính sách (policy / 정책) tỷ lệ (rate / 비율) không đủ

Trader mới thường nhìn:

```text
Fed rate = X
ECB rate = Y
```

rồi suy luận currency có lãi suất cao hơn sẽ mạnh hơn.

Thị trường (market / 시장) lại định giá **expected đường dẫn (path / 경로)**.

Ví dụ central bank đang giữ chính sách (policy / 정책) tỷ lệ (rate / 비율) 5%, nhưng thị trường (market / 시장) trước đó kỳ vọng giữ 5% thêm sáu tháng. Nếu dữ liệu (data / 데이터) mới khiến thị trường (market / 시장) tin tỷ lệ (rate / 비율) cuts sẽ bắt đầu sớm hơn và sâu hơn, short-term yields có thể giảm ngay dù hiện tại (current / 현재) chính sách (policy / 정책) tỷ lệ (rate / 비율) chưa thay đổi.

FX có thể phản ứng trước cuộc họp chính thức vì expectation đã đổi.

Mô hình tư duy (mental model / 사고 모델):

```text
Spot FX today
responds partly to
expected future policy / rates
not only today's policy rate
```

> **Chuyển mạch:** Ở chặng này của **04 — Macro drivers, interest rates, carry và trading sessions**, **3. Central-bank reaction hàm (function / 함수)** tiếp nhận điểm tựa từ **2. Hiện tại (current / 현재) chính sách (policy / 정책) tỷ lệ (rate / 비율) không đủ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Surprise quan trọng hơn headline mức (level / 수준) trong ngắn hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Central-bank reaction hàm (function / 함수)

**Hàm phản ứng của ngân hàng trung ương (central-bank reaction function)** là cách chính sách (policy / 정책) maker có xu hướng phản ứng với inflation, labor thị trường (market / 시장), growth, financial stability và mandate của mình.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **04 — Macro drivers, interest rates, carry và trading sessions**, **4. Surprise quan trọng hơn headline mức (level / 수준) trong ngắn hạn** tiếp nhận điểm tựa từ **3. Central-bank reaction hàm (function / 함수)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Nominal yield và real yield** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Surprise quan trọng hơn headline mức (level / 수준) trong ngắn hạn

Giả sử consensus CPI YoY là 3.0%.

Trường hợp (case / 사례) A:

```text
Actual = 3.4%
```

Trường hợp (case / 사례) B:

```text
Actual = 2.7%
```

Cùng một country, cùng một bản phát hành (release / 릴리스), nhưng tín hiệu (signal / 신호) đối với expected chính sách (policy / 정책) có thể trái ngược.

Trong event-driven phân tích (analysis / 분석), cần ghi:

```text
Previous
Consensus
Actual
Revision
Market pricing before release
Market reaction after release
```

Không chỉ ghi actual number.

> **Chuyển mạch:** Trong **04 — Macro drivers, interest rates, carry và trading sessions**, **5. Nominal yield và real yield** tiếp nhận điểm tựa từ **4. Surprise quan trọng hơn headline mức (level / 수준) trong ngắn hạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Yield differential** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Nominal yield và real yield

**Lợi suất danh nghĩa (nominal yield)** chưa trừ inflation expectation.

Một approximation:

```text
Real Yield
≈ Nominal Yield - Expected Inflation
```

Nếu nominal yield tăng vì inflation expectation tăng mạnh hơn, real return có thể không cải thiện.

Currency valuation và capital flows có thể nhạy với real yield, nhưng quan hệ (relation / 관계) thay đổi theo regime, rủi ro (risk / 위험) sentiment và hedging chi phí (cost / 비용).

Vì vậy:

```text
higher nominal yield
≠ automatically stronger currency
```

> **Chuyển mạch:** Ở chặng này của **04 — Macro drivers, interest rates, carry và trading sessions**, **6. Yield differential** tiếp nhận điểm tựa từ **5. Nominal yield và real yield** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Forward points và interest-rate differential** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Yield differential

Một **chênh lệch lợi suất (yield differential)** so sánh yields giữa hai currency areas ở maturity phù hợp.

Ví dụ conceptual:

```text
US 2Y yield - Germany 2Y yield
```

có thể cung cấp thông tin (information / 정보) về relative monetary-policy expectations có liên quan EUR/USD.

Nhưng correlation không cố định. Một pair còn chịu:

- rủi ro (risk / 위험) premium;
- capital flows;
- reserve demand;
- bên ngoài (external / 외부) balance;
- fiscal concerns;
- hedging flows;
- positioning;
- geopolitical shocks.

Yield spread là một explanatory variable, không phải universal trading tín hiệu (signal / 신호).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **04 — Macro drivers, interest rates, carry và trading sessions**, **7. Forward points và interest-rate differential** tiếp nhận điểm tựa từ **6. Yield differential** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Carry trade** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Forward points và interest-rate differential

Trong simplified no-arbitrage khung phần mềm (framework / 프레임워크), spot và forward liên hệ với interest rates của hai currencies.

Nếu quote là `A/B`, một biểu diễn (representation / 표현) của covered interest parity có dạng gần:

```text
F = S × (1 + r_B × T) / (1 + r_A × T)
```

với convention chính xác phụ thuộc cách định nghĩa pair/rates/day count.

Ý nghĩa quan trọng hơn công thức: nếu hai currencies có funding return khác nhau, forward tỷ lệ (rate / 비율) phải điều chỉnh để ngăn arbitrage đơn giản.

Do đó forward price **không phải đơn thuần thị trường (market / 시장) forecast của future spot**.

> **Chuyển mạch:** Trong **04 — Macro drivers, interest rates, carry và trading sessions**, **8. Carry trade** tiếp nhận điểm tựa từ **7. Forward points và interest-rate differential** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Uncovered interest parity và carry puzzle** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Carry trade

**Carry** là return liên quan đến chênh lệch financing/yield khi nắm exposure qua thời gian.

Carry trade thường được mô tả đơn giản:

```text
borrow low-yield currency
buy high-yield currency
```

Nếu spot không đi ngược quá mạnh, trader có thể hưởng carry. Nhưng high yield thường không phải “free money”. Nó có thể bù cho:

- inflation rủi ro (risk / 위험);
- devaluation rủi ro (risk / 위험);
- sovereign/political rủi ro (risk / 위험);
- liquidity rủi ro (risk / 위험);
- crash rủi ro (risk / 위험).

Một currency có yield cao có thể mất giá mạnh đúng lúc risk-off, xóa nhiều tháng carry trong vài ngày.

> **Chuyển mạch:** Ở chặng này của **04 — Macro drivers, interest rates, carry và trading sessions**, **9. Uncovered interest parity và carry puzzle** tiếp nhận điểm tựa từ **8. Carry trade** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Growth differential** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Uncovered interest parity và carry puzzle

Một textbook intuition nói rằng currency có interest tỷ lệ (rate / 비율) cao hơn có xu hướng depreciate đủ để offset yield advantage trong expectation, nếu không sẽ tồn tại easy excess return.

Thực nghiệm FX historically cho thấy quan hệ (relation / 관계) này không ổn định; carry strategies từng tạo excess returns trong nhiều mẫu (sample / 표본) nhưng đi kèm crash/tail rủi ro (risk / 위험) và regime dependence.

Bài học không phải “UIP sai nên carry luôn thắng”. Bài học là:

```text
interest differential
+ expected depreciation
+ risk premium
+ tail risk
```

phải được xem cùng nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **04 — Macro drivers, interest rates, carry và trading sessions**, **10. Growth differential** tiếp nhận điểm tựa từ **9. Uncovered interest parity và carry puzzle** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Inflation: cùng headline nhưng khác cơ chế (mechanism / 메커니즘)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Không có deterministic ánh xạ (mapping / 매핑).

Điểm cần theo dõi là **growth surprise relative to the other economy and to expectations**.

> **Chuyển mạch:** Trong **04 — Macro drivers, interest rates, carry và trading sessions**, **10. Growth differential** xác định đầu vào; **11. Inflation: cùng headline nhưng khác cơ chế (mechanism / 메커니즘)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **12. Labor-market dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Inflation: cùng headline nhưng khác cơ chế (mechanism / 메커니즘)

Inflation tăng do demand overheating khác inflation tăng do supply shock.

### Demand-driven inflation

Có thể làm central bank hawkish hơn nếu growth vẫn mạnh.

### Supply shock

Ví dụ năng lượng (energy / 에너지) import shock có thể vừa tăng inflation vừa làm household real income giảm, khiến chính sách (policy / 정책) sự đánh đổi (trade-off / 트레이드오프) khó hơn.

Vì vậy currency reaction cần phân tích:

```text
source of inflation
→ policy response
→ growth effect
→ real yield
→ external balance
```

> **Chuyển mạch:** Ở chặng này của **04 — Macro drivers, interest rates, carry và trading sessions**, cơ chế trong **11. Inflation: cùng headline nhưng khác cơ chế (mechanism / 메커니즘)** cần được kiểm chứng bằng dấu vết cụ thể; **12. Labor-market dữ liệu (data / 데이터)** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **13. Balance of payments** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Labor-market dữ liệu (data / 데이터)

Employment, unemployment, wage growth, vacancies và participation có thể ảnh hưởng chính sách (policy / 정책) expectations.

Ví dụ US payroll dữ liệu (data / 데이터) không chỉ là số jobs. Thị trường (market / 시장) có thể chú ý:

- payroll thay đổi (change / 변경);
- revisions;
- unemployment tỷ lệ (rate / 비율);
- labor-force participation;
- average hourly earnings;
- hours worked.

Một headline “strong” nhưng revisions yếu và wage pressure giảm có thể tạo interpretation khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **04 — Macro drivers, interest rates, carry và trading sessions**, **12. Labor-market dữ liệu (data / 데이터)** cho ta quy tắc; **13. Balance of payments** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **14. Hiện tại (current / 현재) account** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Balance of payments

Một country liên hệ với thế giới qua hiện tại (current / 현재) account và financial/capital flows.

Simplified:

```text
Current-account flows
+
Financial-account flows
→ demand/supply for currency
```

Country có trade surplus không tự động có appreciating currency vì residents có thể đầu tư capital ra nước ngoài hoặc central bank có thể can thiệp/reserve accumulation.

Cần nhìn cả hai phía.

> **Chuyển mạch:** Trong **04 — Macro drivers, interest rates, carry và trading sessions**, **14. Hiện tại (current / 현재) account** tiếp nhận điểm tựa từ **13. Balance of payments** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Capital flows** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Hiện tại (current / 현재) account

**Cán cân vãng lai (current account)** gồm trade in goods/services, primary income và transfers.

Persistent deficit nghĩa là country cần counterpart financing từ abroad hoặc asset sales/capital inflows theo accounting định danh (identity / 식별자).

Nếu foreign funding confidence giảm đột ngột, currency có thể chịu pressure mạnh — đặc biệt khi bên ngoài (external / 외부) debt, short-term funding hoặc reserve adequacy yếu.

> **Chuyển mạch:** Ở chặng này của **04 — Macro drivers, interest rates, carry và trading sessions**, **14. Hiện tại (current / 현재) account** xác định đầu vào; **15. Capital flows** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **16. Risk-on / risk-off chỉ là shorthand** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **04 — Macro drivers, interest rates, carry và trading sessions**, **15. Capital flows** xác định đầu vào; **16. Risk-on / risk-off chỉ là shorthand** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **17. Funding currencies** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Risk-on / risk-off chỉ là shorthand

Thị trường (market / 시장) commentary thường gọi một currency “risk-on” hoặc “safe haven”. Những nhãn này hữu ích như shorthand nhưng không nên trở thành law.

Một currency có thể phản ứng khác nhau tùy:

- nguồn (source / 소스) của shock;
- domestic exposure;
- funding role;
- bên ngoài (external / 외부) balance;
- tỷ lệ (rate / 비율) differential;
- positioning;
- intervention expectation.

Nên hỏi cơ chế (mechanism / 메커니즘) thay vì gắn label cố định.

> **Chuyển mạch:** Trong **04 — Macro drivers, interest rates, carry và trading sessions**, **17. Funding currencies** tiếp nhận điểm tựa từ **16. Risk-on / risk-off chỉ là shorthand** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Commodity-linked currencies** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Funding currencies

Currency có low funding chi phí (cost / 비용) đôi khi được dùng để finance positions ở tài sản/currencies có expected return cao hơn.

Khi rủi ro (risk / 위험) sentiment đảo chiều:

```text
leveraged positions unwind
→ funding currency shorts are covered
→ funding currency may strengthen
```

Đây là một cơ chế (mechanism / 메커니즘) giúp giải thích một số safe-haven-like moves mà không cần giả định investor “thích” currency đó về fundamental.

> **Chuyển mạch:** Ở chặng này của **04 — Macro drivers, interest rates, carry và trading sessions**, **18. Commodity-linked currencies** tiếp nhận điểm tựa từ **17. Funding currencies** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Terms of trade** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Commodity-linked currencies

Một economy xuất khẩu nhiều commodity có thể có currency nhạy với terms of trade.

Ví dụ conceptual:

```text
commodity export price rises
→ export income improves
→ trade balance / corporate income may improve
→ currency-supportive flow may increase
```

Nhưng quan hệ (relation / 관계) còn phụ thuộc:

- import side;
- hedging;
- fiscal chính sách (policy / 정책);
- toàn cục (global / 전역) rủi ro (risk / 위험) appetite;
- China/toàn cục (global / 전역) demand;
- domestic chính sách (policy / 정책).

Không nên trade chỉ vì dầu/gold tăng mà bỏ qua ngữ cảnh (context / 맥락).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **04 — Macro drivers, interest rates, carry và trading sessions**, **19. Terms of trade** tiếp nhận điểm tựa từ **18. Commodity-linked currencies** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Fiscal chính sách (policy / 정책) cũng có thể tác động FX theo nhiều hướng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Terms of trade

**Điều kiện thương mại (terms of trade)** so sánh export prices với import prices.

Nếu country xuất khẩu commodity A và nhập khẩu năng lượng (energy / 에너지) B, relative price changes có thể thay đổi national income ngay cả khi export volume không đổi.

FX có thể phản ánh redistribution này thông qua expected trade balance, income và chính sách (policy / 정책).

> **Chuyển mạch:** Trong **04 — Macro drivers, interest rates, carry và trading sessions**, **20. Fiscal chính sách (policy / 정책) cũng có thể tác động FX theo nhiều hướng** tiếp nhận điểm tựa từ **19. Terms of trade** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Political/geopolitical events nên được phân tích qua channels** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Fiscal chính sách (policy / 정책) cũng có thể tác động FX theo nhiều hướng

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

Phản ứng phụ thuộc starting conditions và monetary-policy tương tác (interaction / 상호작용).

Không có quy tắc (rule / 규칙) “deficit tăng = currency giảm” hoạt động mọi thời điểm.

> **Chuyển mạch:** Ở chặng này của **04 — Macro drivers, interest rates, carry và trading sessions**, **21. Political/geopolitical events nên được phân tích qua channels** tiếp nhận điểm tựa từ **20. Fiscal chính sách (policy / 정책) cũng có thể tác động FX theo nhiều hướng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Thị trường (market / 시장) expectation là hidden variable quan trọng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

FX reaction đến từ channels cụ thể và positioning, không phải từ tên của sự kiện (event / 이벤트).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **04 — Macro drivers, interest rates, carry và trading sessions**, **22. Thị trường (market / 시장) expectation là hidden variable quan trọng** tiếp nhận điểm tựa từ **21. Political/geopolitical events nên được phân tích qua channels** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Positioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Thị trường (market / 시장) expectation là hidden variable quan trọng

Một central bank hike 25 bps:

- nếu thị trường (market / 시장) expected 50 bps → có thể bị đọc là dovish surprise;
- nếu thị trường (market / 시장) expected 0 bps → có thể là hawkish surprise;
- nếu 25 bps đã fully priced → reaction có thể nhỏ;
- guidance sau cuộc họp có thể quan trọng hơn hike hiện tại.

Do đó sự kiện (event / 이벤트) notebook nên lưu **pre-event pricing**.

> **Chuyển mạch:** Trong **04 — Macro drivers, interest rates, carry và trading sessions**, **23. Positioning** tiếp nhận điểm tựa từ **22. Thị trường (market / 시장) expectation là hidden variable quan trọng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Sessions và participant mix** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Positioning

Hai thị trường (market / 시장) có cùng fundamental news nhưng reaction khác nhau nếu positioning khác.

Nếu thị trường (market / 시장) đã extremely long currency A, thêm positive news có thể chỉ tạo limited buying, trong khi mild disappointment kích hoạt crowded exit.

Positioning không nói intrinsic giá trị (value / 값), nhưng ảnh hưởng **đường dẫn (path / 경로)** của price adjustment.

> **Chuyển mạch:** Ở chặng này của **04 — Macro drivers, interest rates, carry và trading sessions**, **24. Sessions và participant mix** tiếp nhận điểm tựa từ **23. Positioning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Daylight-saving thời gian (time / 시간) là research bài toán (problem / 문제) thật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Sessions và participant mix

FX gần như liên tục trong nghiệp vụ (business / 비즈니스) week, nhưng không có cùng participant mix 24/5.

Một simplified chuỗi (sequence / 시퀀스):

```text
Asia
→ Europe/London
→ New York
→ late US / Asia handoff
```

Các trung tâm overlap làm liquidity và thông tin (information / 정보) processing thay đổi.

Ví dụ:

- Asian hours thường quan trọng với JPY, AUD, NZD, CNH và regional flows;
- London là một trung tâm FX rất lớn;
- New York overlap với London thường có nhiều macro releases và liquidity lớn ở USD pairs.

Đây là tendency, không phải guarantee mỗi ngày.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **04 — Macro drivers, interest rates, carry và trading sessions**, **25. Daylight-saving thời gian (time / 시간) là research bài toán (problem / 문제) thật** tiếp nhận điểm tựa từ **24. Sessions và participant mix** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Fixing flows** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Daylight-saving thời gian (time / 시간) là research bài toán (problem / 문제) thật

Nếu backtest “London open breakout” bằng fixed UTC/cục bộ (local / 로컬) hour mà không xử lý DST, dataset có thể trộn hai thị trường (market / 시장) states khác nhau theo mùa.

Time-series chuỗi xử lý (pipeline / 파이프라인) nên lưu timezone-aware timestamps và map session theo actual financial-centre clock.

> **Chuyển mạch:** Trong **04 — Macro drivers, interest rates, carry và trading sessions**, **25. Daylight-saving thời gian (time / 시간) là research bài toán (problem / 문제) thật** xác định đầu vào; **26. Fixing flows** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **27. Month-end / quarter-end rebalancing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Fixing flows

Institutional benchmark fixing windows có thể tập trung hedging/rebalancing orders vào thời điểm nhất định.

Điều này có thể tạo temporary volume/volatility mà không nhất thiết phản ánh new macro thông tin (information / 정보).

Bài học:

```text
price move
≠ always new fundamental information
```

Có thể là mechanical luồng (flow / 흐름).

> **Chuyển mạch:** Ở chặng này của **04 — Macro drivers, interest rates, carry và trading sessions**, **26. Fixing flows** xác định đầu vào; **27. Month-end / quarter-end rebalancing** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **28. Central-bank intervention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Month-end / quarter-end rebalancing

Large portfolios thay đổi FX hedge hoặc rebalance asset weights quanh reporting periods.

Ví dụ equity thị trường (market / 시장) A outperform thị trường (market / 시장) B có thể làm international portfolio weights drift, dẫn đến hedging luồng (flow / 흐름) cuối tháng.

Không nên biến month-end tác động (effect / 효과) thành deterministic tín hiệu (signal / 신호). Cần xác định:

- expected luồng (flow / 흐름);
- kích thước (size / 크기) relative to liquidity;
- whether thị trường (market / 시장) already anticipates it;
- historical conditional phân phối (distribution / 분포).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **04 — Macro drivers, interest rates, carry và trading sessions**, **28. Central-bank intervention** tiếp nhận điểm tựa từ **27. Month-end / quarter-end rebalancing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Managed/fixed exchange-rate regimes khác free float** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Central-bank intervention

Một central bank có thể tham gia FX thị trường (market / 시장) để giảm disorderly moves, influence exchange-rate conditions hoặc thực hiện chính sách (policy / 정책) khung phần mềm (framework / 프레임워크) tùy jurisdiction.

Intervention có thể là:

- direct giao dịch (transaction / 트랜잭션);
- verbal communication;
- liquidity thao tác (operation / 연산);
- coordinated hành động (action / 동작).

Hiệu quả phụ thuộc credibility, kích thước (size / 크기), monetary-policy consistency và thị trường (market / 시장) regime.

Không nên coi một price mức (level / 수준) là guaranteed defense line nếu authority không cam kết như vậy.

> **Chuyển mạch:** Trong **04 — Macro drivers, interest rates, carry và trading sessions**, **29. Managed/fixed exchange-rate regimes khác free float** tiếp nhận điểm tựa từ **28. Central-bank intervention** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. CNH và CNY minh họa thị trường (market / 시장) segmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Với managed currency, chính sách (policy / 정책) mục tiêu (objective / 목표), reserves, capital controls và offshore/onshore thị trường (market / 시장) distinction có thể quan trọng hơn textbook technical phân tích (analysis / 분석).

> **Chuyển mạch:** Ở chặng này của **04 — Macro drivers, interest rates, carry và trading sessions**, **30. CNH và CNY minh họa thị trường (market / 시장) segmentation** tiếp nhận điểm tựa từ **29. Managed/fixed exchange-rate regimes khác free float** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Korea ngữ cảnh (context / 맥락): USD/KRW** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. CNH và CNY minh họa thị trường (market / 시장) segmentation

Một currency có thể có onshore/offshore markets với khả năng tiếp cận (accessibility / 접근성), liquidity và chính sách (policy / 정책) các ràng buộc (constraints / 제약조건들) khác nhau.

Do đó ticker gần giống nhau không có nghĩa instrument fungibility hoàn hảo.

Thị trường (market / 시장) cấu trúc (structure / 구조) phải được hiểu trước khi áp dụng mô hình (model / 모델).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **04 — Macro drivers, interest rates, carry và trading sessions**, **31. Korea ngữ cảnh (context / 맥락): USD/KRW** tiếp nhận điểm tựa từ **30. CNH và CNY minh họa thị trường (market / 시장) segmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Một event-analysis template** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Korea ngữ cảnh (context / 맥락): USD/KRW

Với USD/KRW:

```text
USD/KRW rises
→ one USD buys more KRW
→ KRW weakens relative to USD
```

Các channels có thể bao gồm:

- Fed/BOK expected-rate differential;
- Korean export cycle;
- semiconductor/toàn cục (global / 전역) trade conditions;
- năng lượng (energy / 에너지) import chi phí (cost / 비용);
- foreign portfolio flows;
- broad USD move;
- toàn cục (global / 전역) rủi ro (risk / 위험) sentiment;
- domestic chính sách (policy / 정책)/intervention expectations.

Đây là ngữ cảnh (context / 맥락) để hiểu terminology, không phải trading quy tắc (rule / 규칙).

Một số thuật ngữ Hàn Quốc:

- tỷ giá: **환율**;
- đồng won mạnh lên: **원화 강세**;
- đồng won yếu đi: **원화 약세**;
- chênh lệch lãi suất: **금리차**;
- dòng vốn: **자본 흐름**;
- can thiệp ngoại hối: **외환시장 개입**.

> **Chuyển mạch:** Trong **04 — Macro drivers, interest rates, carry và trading sessions**, **32. Một event-analysis template** tiếp nhận điểm tựa từ **31. Korea ngữ cảnh (context / 맥락): USD/KRW** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Ví dụ chuỗi nhân quả (causal chain / 인과 사슬): inflation surprise** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Một event-analysis template

Khi có macro sự kiện (event / 이벤트), ghi theo chuỗi (chain / 사슬):

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

> **Chuyển mạch:** Ở chặng này của **04 — Macro drivers, interest rates, carry và trading sessions**, **32. Một event-analysis template** cho ta quy tắc; **33. Ví dụ chuỗi nhân quả (causal chain / 인과 사슬): inflation surprise** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **34. Ví dụ chuỗi nhân quả (causal chain / 인과 사슬): weak growth but stronger currency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Ví dụ chuỗi nhân quả (causal chain / 인과 사슬): inflation surprise

Giả sử US CPI cao hơn consensus đáng kể.

Một possible chuỗi (chain / 사슬):

```text
Higher CPI surprise
→ market prices fewer/ later Fed cuts
→ front-end Treasury yields rise
→ USD rate advantage increases
→ USD strengthens
```

Nhưng chuỗi (chain / 사슬) có thể đứt nếu:

```text
inflation surprise is supply-driven
+ growth fear dominates
+ market already extremely long USD
+ risk-off creates other flows
```

Do đó chuỗi nhân quả (causal chain / 인과 사슬) là hypothesis phải kiểm tra, không phải guarantee.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **04 — Macro drivers, interest rates, carry và trading sessions**, **33. Ví dụ chuỗi nhân quả (causal chain / 인과 사슬): inflation surprise** cho ta quy tắc; **34. Ví dụ chuỗi nhân quả (causal chain / 인과 사슬): weak growth but stronger currency** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **35. Macro mô hình (model / 모델) tốt phải có vô hiệu hóa (invalidation / 무효화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Ví dụ chuỗi nhân quả (causal chain / 인과 사슬): weak growth but stronger currency

GDP dữ liệu (data / 데이터) yếu nhưng currency vẫn tăng có thể xảy ra nếu:

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

Price không “sai” chỉ vì một textbook quy tắc (rule / 규칙) không hoạt động.

> **Chuyển mạch:** Trong **04 — Macro drivers, interest rates, carry và trading sessions**, **34. Ví dụ chuỗi nhân quả (causal chain / 인과 사슬): weak growth but stronger currency** cho ta quy tắc; **35. Macro mô hình (model / 모델) tốt phải có vô hiệu hóa (invalidation / 무효화)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **36. Carry return phải tách khỏi spot return** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Macro mô hình (model / 모델) tốt phải có vô hiệu hóa (invalidation / 무효화)

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

Đây là research cấu trúc (structure / 구조) tốt hơn “RSI oversold nên buy”.

> **Chuyển mạch:** Ở chặng này của **04 — Macro drivers, interest rates, carry và trading sessions**, **36. Carry return phải tách khỏi spot return** tiếp nhận điểm tựa từ **35. Macro mô hình (model / 모델) tốt phải có vô hiệu hóa (invalidation / 무효화)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Regime dependence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Carry return phải tách khỏi spot return

FX total return của leveraged/carry position có thể conceptualize:

```text
Total Return
≈ Spot Move
+ Carry / Financing
- Transaction Cost
```

Nếu chiến lược (strategy / 전략) kiếm tiền nhờ spot move nhưng mất carry, hoặc ngược lại, hiệu năng (performance / 성능) attribution phải tách hai nguồn.

Nếu không, trader có thể hiểu sai edge.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **04 — Macro drivers, interest rates, carry và trading sessions**, **37. Regime dependence** tiếp nhận điểm tựa từ **36. Carry return phải tách khỏi spot return** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. Checklist trước khi sang thực thi (execution / 실행)/broker rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Regime dependence

Một quan hệ (relation / 관계) như:

```text
yield differential ↑ → currency ↑
```

có thể mạnh trong monetary-policy divergence regime nhưng yếu khi crisis liquidity dominates.

Do đó research cần conditioning variables:

- volatility regime;
- growth regime;
- inflation regime;
- chính sách (policy / 정책) divergence;
- rủi ro (risk / 위험) sentiment;
- liquidity stress.

Correlation full-sample có thể che nhiều sub-regimes trái nhau.

> **Chuyển mạch:** Trong **04 — Macro drivers, interest rates, carry và trading sessions**, **38. Checklist trước khi sang thực thi (execution / 실행)/broker rủi ro (risk / 위험)** tiếp nhận điểm tựa từ **37. Regime dependence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nối sang chương tiếp theo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Checklist trước khi sang thực thi (execution / 실행)/broker rủi ro (risk / 위험)

Bạn cần tự giải thích được:

1. Vì sao FX là relative macro.
2. Vì sao expected tỷ lệ (rate / 비율) đường dẫn (path / 경로) quan trọng hơn chỉ hiện tại (current / 현재) chính sách (policy / 정책) tỷ lệ (rate / 비율).
3. Vì sao surprise vs consensus ảnh hưởng sự kiện (event / 이벤트) reaction.
4. Nominal và real yield khác nhau thế nào.
5. Forward points liên hệ interest differential nhưng không đơn thuần forecast spot.
6. Carry kiếm return từ đâu và crash rủi ro (risk / 위험) đến từ đâu.
7. Hiện tại (current / 현재) account và capital flows liên kết currency demand như thế nào.
8. Vì sao risk-on/safe-haven chỉ là shorthand.
9. Vì sao sessions/DST ảnh hưởng backtest.
10. Vì sao flow-driven move không nhất thiết là fundamental thông tin (information / 정보).

> **Chuyển mạch:** Ở chặng này của **04 — Macro drivers, interest rates, carry và trading sessions**, **Nối sang chương tiếp theo** tiếp nhận điểm tựa từ **38. Checklist trước khi sang thực thi (execution / 실행)/broker rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nội bộ (internal / 내부) links** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nối sang chương tiếp theo

Macro giải thích **vì sao participant muốn thay đổi exposure**. Chương tiếp theo giải thích **lệnh đó được truyền qua broker/dealer như thế nào, chi phí thực tế hình thành ở đâu và vì sao thực thi (execution / 실행)/counterparty rủi ro (risk / 위험) có thể phá một chiến lược (strategy / 전략) đúng về direction**.

→ [05 — Execution, brokers, costs and operational risk](./05_EXECUTION_BROKERS_COSTS_AND_RISK.md)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **04 — Macro drivers, interest rates, carry và trading sessions**, **Nội bộ (internal / 내부) links** tiếp nhận điểm tựa từ **Nối sang chương tiếp theo** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Nội bộ (internal / 내부) links

- [Macro Data Playbook](../../04_economics/03_MACRO_DATA_PLAYBOOK.md)
- [Global Economy, Capital Flows and Crisis](../../04_economics/02_GLOBAL_ECONOMY_CAPITAL_FLOWS_AND_CRISIS.md)
- [Monetary System, Liquidity and Crisis Transmission](../../04_economics/04_MONETARY_SYSTEM_LIQUIDITY_AND_CRISIS_TRANSMISSION.md)
- [03 — Leverage, margin and position sizing](./03_LEVERAGE_MARGIN_POSITION_SIZING.md)
- [Glossary, formulas and research conventions](../../00_GLOSSARY_FORMULAS_AND_RESEARCH_CONVENTIONS.md)

> **Bàn giao:** Sau **Nội bộ (internal / 내부) links**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
