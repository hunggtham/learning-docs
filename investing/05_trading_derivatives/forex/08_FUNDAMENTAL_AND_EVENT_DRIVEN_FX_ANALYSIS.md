# 08 — Fundamental và event-driven FX phân tích (analysis / 분석)

> **Mạch đọc:** [README](./README.md) là owner của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**; quay lại README để định vị file trong track FX. Từ **1. Sự kiện (event / 이벤트) kết quả (outcome / 결과) không đủ; surprise mới quan trọng** chuyển sang expectation, relative valuation, policy/rates, flows và risk premium, rồi kiểm tra follow-through hoặc reversal; phản ứng FX chỉ được hiểu qua toàn bộ chuỗi repricing đó.

Fundamental FX phân tích (analysis / 분석) không phải danh sách quy tắc kiểu “CPI tăng → currency tăng”. Nó là bài toán **expectation, relative valuation và transmission**: dữ liệu mới thay đổi kỳ vọng về tăng trưởng, lạm phát, chính sách, dòng vốn và rủi ro (risk / 위험) premium như thế nào so với phía còn lại của currency pair.

Mô hình tư duy (mental model / 사고 모델):

```text
Prior expectations
→ new information
→ repricing of policy / growth / risk
→ rates and asset-price reaction
→ flows / hedging
→ FX reaction
→ follow-through or reversal
```

## 1. Sự kiện (event / 이벤트) kết quả (outcome / 결과) không đủ; surprise mới quan trọng

Một dữ liệu (data / 데이터) bản phát hành (release / 릴리스) có ba lớp:

```text
Previous
Consensus / market expectation
Actual
```

Thêm vào đó còn:

- revisions;
- composition/detail;
- thị trường (market / 시장) positioning;
- chính sách (policy / 정책) reaction hàm (function / 함수);
- mức đã được price in trước sự kiện (event / 이벤트).

Ví dụ CPI 3.0% có thể hawkish nếu consensus 2.7%, nhưng dovish nếu thị trường (market / 시장) feared 3.4%.

> **Chuyển mạch:** Trong **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **2. “Thị trường (market / 시장) expectation” phải được ghi lại trước sự kiện (event / 이벤트)** tiếp nhận điểm tựa từ **1. Sự kiện (event / 이벤트) kết quả (outcome / 결과) không đủ; surprise mới quan trọng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Central-bank reaction hàm (function / 함수)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. “Thị trường (market / 시장) expectation” phải được ghi lại trước sự kiện (event / 이벤트)

Nếu chỉ xem chart sau sự kiện (event / 이벤트) rồi giải thích, rất dễ tạo hindsight narrative.

Sự kiện (event / 이벤트) notebook nên lưu trước bản phát hành (release / 릴리스):

```text
Consensus
Rate-path pricing if available
Recent central-bank guidance
Positioning proxies
Recent trend / volatility
Key alternative scenarios
```

Sau sự kiện (event / 이벤트) mới ghi reaction.

> **Chuyển mạch:** Ở chặng này của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **3. Central-bank reaction hàm (function / 함수)** tiếp nhận điểm tựa từ **2. “Thị trường (market / 시장) expectation” phải được ghi lại trước sự kiện (event / 이벤트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Hiện tại (current / 현재) tỷ lệ (rate / 비율) khác expected đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Central-bank reaction hàm (function / 함수)

Mỗi central bank có mandate, khung phần mềm (framework / 프레임워크) và các ràng buộc (constraints / 제약조건들) khác nhau. Cần hiểu họ phản ứng với:

- inflation outlook;
- labor thị trường (market / 시장);
- growth;
- financial stability;
- exchange-rate pass-through;
- credit/housing conditions;
- fiscal/financial-system stress.

Một quyết định (decision / 결정) chỉ có meaning khi đặt trong reaction hàm (function / 함수).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **3. Central-bank reaction hàm (function / 함수)** xác định đầu vào; **4. Hiện tại (current / 현재) tỷ lệ (rate / 비율) khác expected đường dẫn (path / 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **5. FOMC/ECB/BOK sự kiện (event / 이벤트) nên đọc theo nhiều tầng (layer / 계층)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Hiện tại (current / 현재) tỷ lệ (rate / 비율) khác expected đường dẫn (path / 경로)

FX thường phản ứng với thay đổi của **expected future tỷ lệ (rate / 비율) đường dẫn (path / 경로)**, không chỉ hiện tại (current / 현재) chính sách (policy / 정책) tỷ lệ (rate / 비율).

Ví dụ:

```text
Rate unchanged today
but guidance becomes more hawkish
→ expected future rates rise
→ front-end yields may rise
→ currency may strengthen
```

Ngược lại, hike hiện tại nhưng dovish future guidance có thể tạo reaction trái dấu.

> **Chuyển mạch:** Trong **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **4. Hiện tại (current / 현재) tỷ lệ (rate / 비율) khác expected đường dẫn (path / 경로)** xác định đầu vào; **5. FOMC/ECB/BOK sự kiện (event / 이벤트) nên đọc theo nhiều tầng (layer / 계층)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **6. CPI** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. FOMC/ECB/BOK sự kiện (event / 이벤트) nên đọc theo nhiều tầng (layer / 계층)

Một central-bank sự kiện (event / 이벤트) có thể gồm:

```text
Policy decision
Statement language
Economic projections
Press conference
Implementation details
Balance-sheet guidance
```

Không nên lấy headline tỷ lệ (rate / 비율) quyết định (decision / 결정) làm toàn bộ sự kiện (event / 이벤트).

Nguồn chuẩn gốc (canonical / 정본) nên là website chính thức của central bank. Với Fed, lịch FOMC, statements, minutes và projection materials được công bố theo calendar chính thức; với ECB/BOK cũng nên dùng press bản phát hành (release / 릴리스)/quyết định (decision / 결정) chính thức thay vì chỉ secondary headline.

> **Chuyển mạch:** Ở chặng này của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **6. CPI** tiếp nhận điểm tựa từ **5. FOMC/ECB/BOK sự kiện (event / 이벤트) nên đọc theo nhiều tầng (layer / 계층)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Employment dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. CPI

Không chỉ đọc headline CPI. Tùy economy, thị trường (market / 시장) có thể chú ý:

- headline;
- cốt lõi (core / 핵심);
- services;
- housing/rent components;
- goods;
- năng lượng (energy / 에너지);
- month-on-month momentum;
- annualized short-run measures.

Chuỗi nhân quả (causal chain / 인과 사슬) cần hỏi:

```text
Which component surprised?
Persistent or temporary?
Does it alter policy path?
Does it alter real growth?
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **6. CPI** nêu điều cần giải thích; **7. Employment dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **8. GDP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Employment dữ liệu (data / 데이터)

Employment bản phát hành (release / 릴리스) có thể chứa:

- payroll/employment thay đổi (change / 변경);
- unemployment tỷ lệ (rate / 비율);
- participation;
- wages;
- hours worked;
- revisions.

Nếu headline jobs mạnh nhưng prior months revised sharply down và wage growth weakens, interpretation khác headline alone.

> **Chuyển mạch:** Trong **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **7. Employment dữ liệu (data / 데이터)** nêu điều cần giải thích; **8. GDP** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **9. PMI / nghiệp vụ (business / 비즈니스) surveys** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. GDP

GDP là broad activity measure nhưng có lag và revisions. FX có thể phản ứng nhiều hơn với forward-looking components hoặc high-frequency dữ liệu (data / 데이터) nếu GDP đã anticipated.

Một strong GDP print không tự động bullish nếu:

- driven by inventories;
- already priced;
- inflation implications are dovish;
- other side of pair is stronger.

> **Chuyển mạch:** Ở chặng này của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **9. PMI / nghiệp vụ (business / 비즈니스) surveys** tiếp nhận điểm tựa từ **8. GDP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Retail sales / consumption** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. PMI / nghiệp vụ (business / 비즈니스) surveys

PMI-like surveys có thể cung cấp earlier tín hiệu (signal / 신호) về activity, orders, employment, prices và sentiment.

Nhưng survey diffusion indices không phải GDP growth tỷ lệ (rate / 비율) trực tiếp. Cần hiểu construction và historical relationship.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **10. Retail sales / consumption** tiếp nhận điểm tựa từ **9. PMI / nghiệp vụ (business / 비즈니스) surveys** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Inflation expectations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Retail sales / consumption

Consumption dữ liệu (data / 데이터) ảnh hưởng growth outlook và đôi khi inflation pressure.

Nhưng nominal sales có thể tăng vì prices tăng, không phải real volume. Nếu có thể, phân biệt nominal và real.

> **Chuyển mạch:** Trong **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **11. Inflation expectations** tiếp nhận điểm tựa từ **10. Retail sales / consumption** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Yield curve** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Inflation expectations

Market-based hoặc survey inflation expectations ảnh hưởng real yields và chính sách (policy / 정책) pricing.

Một nominal yield tăng 30 bps nhưng expected inflation tăng 40 bps có thể làm real yield giảm.

Do đó FX phân tích (analysis / 분석) cần nhìn decomposition khi relevant.

> **Chuyển mạch:** Ở chặng này của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **12. Yield curve** tiếp nhận điểm tựa từ **11. Inflation expectations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. OIS / money-market pricing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Yield curve

Different maturities encode different combinations của:

- expected chính sách (policy / 정책) rates;
- inflation expectations;
- term premium;
- rủi ro (risk / 위험)/liquidity premium.

FX short-horizon sự kiện (event / 이벤트) reaction thường nhạy với front-end repricing, nhưng medium-term thesis có thể liên quan broader curve.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **13. OIS / money-market pricing** tiếp nhận điểm tựa từ **12. Yield curve** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Surprise chỉ mục (index / 인덱스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. OIS / money-market pricing

Overnight-indexed instruments thường được dùng để infer market-implied chính sách (policy / 정책) expectations.

Không nên đọc implied đường dẫn (path / 경로) như certainty. Nó là price incorporating expectations và rủi ro (risk / 위험) premia.

> **Chuyển mạch:** Trong **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **14. Surprise chỉ mục (index / 인덱스)** tiếp nhận điểm tựa từ **13. OIS / money-market pricing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Relative dữ liệu (data / 데이터) surprise** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Surprise chỉ mục (index / 인덱스)

Một economic surprise chỉ mục (index / 인덱스) tổng hợp actual-vs-consensus across releases.

Nó có thể giúp đo liệu luồng dữ liệu (data flow / 데이터 흐름) đang systematically vượt hay hụt expectation, nhưng construction/nguồn (source / 소스) khác nhau và không phải direct trading tín hiệu (signal / 신호).

> **Chuyển mạch:** Ở chặng này của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **14. Surprise chỉ mục (index / 인덱스)** nêu điều cần giải thích; **15. Relative dữ liệu (data / 데이터) surprise** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. Trade balance và hiện tại (current / 현재) account** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Relative dữ liệu (data / 데이터) surprise

Với currency pair A/B, có thể nghiên cứu:

```text
Surprise_A - Surprise_B
```

thay vì chỉ surprise của một economy.

Đây phù hợp với bản chất relative của FX.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **15. Relative dữ liệu (data / 데이터) surprise** nêu điều cần giải thích; **16. Trade balance và hiện tại (current / 현재) account** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **17. Terms of trade** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Trade balance và hiện tại (current / 현재) account

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

Balance of payments là hệ thống (system / 시스템), không phải một dòng headline.

> **Chuyển mạch:** Trong **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **17. Terms of trade** tiếp nhận điểm tựa từ **16. Trade balance và hiện tại (current / 현재) account** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Fiscal news** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Terms of trade

Commodity import/export prices có thể thay đổi national income và bên ngoài (external / 외부) balance.

Một energy-importing economy có thể chịu:

```text
energy price shock
→ import bill rises
→ trade balance deteriorates
→ inflation rises
→ growth weakens
```

FX tác động (effect / 효과) phụ thuộc chính sách (policy / 정책) phản hồi (response / 응답) và thị trường (market / 시장) pricing.

> **Chuyển mạch:** Ở chặng này của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **18. Fiscal news** tiếp nhận điểm tựa từ **17. Terms of trade** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Geopolitical shock** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Fiscal news

Ngân sách (budget / 예산), tax, spending hoặc debt issuance có thể tác động qua:

- growth;
- inflation;
- bond supply;
- term premium;
- sovereign rủi ro (risk / 위험);
- central-bank phản hồi (response / 응답).

Không dùng quy tắc (rule / 규칙) đơn giản “fiscal expansion bullish/bearish currency”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **19. Geopolitical shock** tiếp nhận điểm tựa từ **18. Fiscal news** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Intervention rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Cùng một geopolitical sự kiện (event / 이벤트) có thể tác động khác nhau tới JPY, EUR, KRW, CHF, USD tùy origin và exposure.

> **Chuyển mạch:** Trong **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **20. Intervention rủi ro (risk / 위험)** tiếp nhận điểm tựa từ **19. Geopolitical shock** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Fixing và benchmark flows** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Intervention rủi ro (risk / 위험)

Với currencies nơi authority có thể can thiệp, cần theo dõi official communication và chính sách (policy / 정책) khung phần mềm (framework / 프레임워크).

Không được biến một mức (level / 수준) được báo chí nhắc đến thành “guaranteed defense line”.

Intervention thesis phải ghi:

- official statements;
- historical cơ chế (mechanism / 메커니즘);
- reserve/liquidity sức chứa (capacity / 용량) if relevant;
- chính sách (policy / 정책) consistency;
- thị trường (market / 시장) positioning.

> **Chuyển mạch:** Ở chặng này của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **20. Intervention rủi ro (risk / 위험)** xác định đầu vào; **21. Fixing và benchmark flows** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **22. Options thị trường (market / 시장) như expectation proxy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Fixing và benchmark flows

Một move quanh benchmark fixing có thể đến từ mechanical thực thi (execution / 실행)/rebalancing thay vì new macro thông tin (information / 정보).

Sự kiện (event / 이벤트) phân tích (analysis / 분석) phải phân biệt:

```text
information shock
versus
flow shock
```

vì expected persistence có thể khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **21. Fixing và benchmark flows** xác định đầu vào; **22. Options thị trường (market / 시장) như expectation proxy** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **23. Sự kiện (event / 이벤트) volatility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Options thị trường (market / 시장) như expectation proxy

FX options có thể cung cấp thông tin (information / 정보) về:

- implied volatility;
- sự kiện (event / 이벤트) premium;
- skew/rủi ro (risk / 위험) reversal;
- demand for asymmetric protection.

Nhưng implied volatility không phải direct xác suất (probability / 확률) forecast không điều chỉnh; nó chứa rủi ro (risk / 위험) premium và thị trường (market / 시장) microstructure.

> **Chuyển mạch:** Trong **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **23. Sự kiện (event / 이벤트) volatility** tiếp nhận điểm tựa từ **22. Options thị trường (market / 시장) như expectation proxy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. First reaction và second reaction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Sự kiện (event / 이벤트) volatility

Trước major bản phát hành (release / 릴리스), implied/realized volatility expectation có thể tăng.

Sau bản phát hành (release / 릴리스):

```text
uncertainty resolves
→ implied volatility can fall
```

Vì vậy directional view đúng chưa chắc option trade có profit nếu option premium quá cao. Phần này nối với chapter FX options sau.

> **Chuyển mạch:** Ở chặng này của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **24. First reaction và second reaction** tiếp nhận điểm tựa từ **23. Sự kiện (event / 이벤트) volatility** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Revisions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. First reaction và second reaction

Sự kiện (event / 이벤트) có thể có:

```text
0–5 seconds: algorithmic headline reaction
5 min–1h: detail interpretation / liquidity normalization
1d–1w: broader repricing
```

Chiến lược (strategy / 전략) horizon phải xác định mình nghiên cứu tầng (layer / 계층) nào.

Không nên backtest daily close rồi suy luận về edge vài giây quanh bản phát hành (release / 릴리스).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **25. Revisions** tiếp nhận điểm tựa từ **24. First reaction và second reaction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Bản phát hành (release / 릴리스) timestamp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Revisions

Macro dữ liệu (data / 데이터) có thể được revised. Backtest dùng final revised dataset có nguy cơ **look-ahead / vintage độ lệch (bias / 편향)** nếu live trader lúc đó chỉ biết first bản phát hành (release / 릴리스).

Sự kiện (event / 이벤트) research nên dùng point-in-time vintage dữ liệu (data / 데이터) khi possible.

> **Chuyển mạch:** Trong **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **26. Bản phát hành (release / 릴리스) timestamp** tiếp nhận điểm tựa từ **25. Revisions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Thông tin (information / 정보) leakage / pre-release moves** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Bản phát hành (release / 릴리스) timestamp

Timestamp phải đúng timezone và daylight-saving convention.

Nếu một bản phát hành (release / 릴리스) xảy ra lúc 08:30 New York thời gian (time / 시간), UTC timestamp thay đổi theo DST. Dữ liệu (data / 데이터) chuỗi xử lý (pipeline / 파이프라인) phải dùng timezone-aware conversion.

> **Chuyển mạch:** Ở chặng này của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **27. Thông tin (information / 정보) leakage / pre-release moves** tiếp nhận điểm tựa từ **26. Bản phát hành (release / 릴리스) timestamp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Sự kiện (event / 이벤트) study khung phần mềm (framework / 프레임워크)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Thông tin (information / 정보) leakage / pre-release moves

Nếu price move trước scheduled bản phát hành (release / 릴리스), có nhiều explanations:

- unrelated thị trường (market / 시장) luồng (flow / 흐름);
- positioning adjustment;
- correlated thông tin (information / 정보);
- rumor;
- leakage in rare cases.

Không nên tự động kết luận cause từ chart.

Research cần sự kiện (event / 이벤트) cửa sổ (window / 윈도우) và điều khiển (control / 제어) windows.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **28. Sự kiện (event / 이벤트) study khung phần mềm (framework / 프레임워크)** tiếp nhận điểm tựa từ **27. Thông tin (information / 정보) leakage / pre-release moves** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Conditional phản hồi (response / 응답)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Sự kiện (event / 이벤트) study khung phần mềm (framework / 프레임워크)

Một basic sự kiện (event / 이벤트) study:

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

Sau đó kiểm tra phân phối (distribution / 분포), không chỉ average.

> **Chuyển mạch:** Trong **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **29. Conditional phản hồi (response / 응답)** tiếp nhận điểm tựa từ **28. Sự kiện (event / 이벤트) study khung phần mềm (framework / 프레임워크)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Narrative phải được falsifiable** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Conditional phản hồi (response / 응답)

Một hawkish surprise có thể tạo USD reaction khác khi:

- USD positioning already extreme;
- rủi ro (risk / 위험) crisis dominates;
- surprise comes from inflation vs growth;
- sự kiện (event / 이벤트) was anticipated.

Do đó regression/sự kiện (event / 이벤트) study có thể include interactions.

> **Chuyển mạch:** Ở chặng này của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **30. Narrative phải được falsifiable** tiếp nhận điểm tựa từ **29. Conditional phản hồi (response / 응답)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Sự kiện (event / 이벤트) journal** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **31. Sự kiện (event / 이벤트) journal** tiếp nhận điểm tựa từ **30. Narrative phải được falsifiable** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Official sources first** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Sự kiện (event / 이벤트) journal

Một bản ghi (record / 레코드) nên có:

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

> **Chuyển mạch:** Trong **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **31. Sự kiện (event / 이벤트) journal** nêu điều cần giải thích; **32. Official sources first** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **33. Không trade headline văn bản (text / 텍스트) bằng cảm giác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **32. Official sources first** nêu điều cần giải thích; **33. Không trade headline văn bản (text / 텍스트) bằng cảm giác** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **34. Scheduled vs unscheduled events** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Không trade headline văn bản (text / 텍스트) bằng cảm giác

Một word như “hawkish” hoặc “dovish” là compressed interpretation. Hai analysts có thể disagree.

Nếu research NLP/sự kiện (event / 이벤트) tín hiệu (signal / 신호), cần formalize văn bản (text / 텍스트) features và train/kiểm thử (test / 테스트) chronologically, không label bằng future thị trường (market / 시장) reaction.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **34. Scheduled vs unscheduled events** tiếp nhận điểm tựa từ **33. Không trade headline văn bản (text / 텍스트) bằng cảm giác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Fundamental phân tích (analysis / 분석) không loại bỏ technical/thực thi (execution / 실행) tầng (layer / 계층)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Scheduled vs unscheduled events

Scheduled:

- CPI;
- labor dữ liệu (data / 데이터);
- central-bank meetings;
- GDP/PMI.

Unscheduled:

- surprise intervention;
- political/geopolitical shock;
- emergency chính sách (policy / 정책) hành động (action / 동작);
- financial accident.

Unscheduled events có tail/thực thi (execution / 실행) rủi ro (risk / 위험) lớn hơn vì thị trường (market / 시장) chưa chuẩn bị liquidity giống scheduled sự kiện (event / 이벤트).

> **Chuyển mạch:** Trong **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **35. Fundamental phân tích (analysis / 분석) không loại bỏ technical/thực thi (execution / 실행) tầng (layer / 계층)** tiếp nhận điểm tựa từ **34. Scheduled vs unscheduled events** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. Current-source examples** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Fundamental phân tích (analysis / 분석) không loại bỏ technical/thực thi (execution / 실행) tầng (layer / 계층)

Một macro thesis có thể đúng trong tuần nhưng entry thực thi (execution / 실행) tệ làm trade thất bại.

Chuỗi xử lý (pipeline / 파이프라인) đầy đủ:

```text
Fundamental hypothesis
→ expected horizon
→ market-price confirmation or timing rule
→ position sizing
→ execution
→ attribution
```

Không nên dùng fundamental story để bỏ stop/vô hiệu hóa (invalidation / 무효화).

> **Chuyển mạch:** Ở chặng này của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **35. Fundamental phân tích (analysis / 분석) không loại bỏ technical/thực thi (execution / 실행) tầng (layer / 계층)** cho ta quy tắc; **36. Current-source examples** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **37. Checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Current-source examples

Khi học bằng dữ liệu hiện hành, luôn lấy ngày cụ thể. Ví dụ calendar FOMC chính thức liệt kê meeting dates, statements, minutes và projection materials theo từng kỳ; ECB và Bank of Korea cũng công bố chính sách (policy / 정책) decisions trực tiếp. Những tài liệu này thích hợp để xây sự kiện (event / 이벤트) dataset hơn bài báo tóm tắt.

Không bản sao (copy / 복사) hiện tại (current / 현재) chính sách (policy / 정책) tỷ lệ (rate / 비율) vào tài liệu như một fact vĩnh viễn; nếu cần ví dụ thời điểm phải ghi rõ ngày.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **36. Current-source examples** cho ta quy tắc; **37. Checklist** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Đọc tiếp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Checklist

Bạn cần tự giải thích được:

1. Actual khác surprise như thế nào.
2. Vì sao expected tỷ lệ (rate / 비율) đường dẫn (path / 경로) quan trọng hơn headline tỷ lệ (rate / 비율).
3. Reaction hàm (function / 함수) là gì.
4. Vì sao revisions gây vintage độ lệch (bias / 편향).
5. Vì sao sự kiện (event / 이벤트) timestamp/DST quan trọng.
6. First reaction và follow-through khác nhau.
7. Luồng (flow / 흐름) shock khác thông tin (information / 정보) shock thế nào.
8. Cách viết một fundamental thesis có vô hiệu hóa (invalidation / 무효화).
9. Vì sao official nguồn (source / 소스) nên là nguồn (source / 소스) of bản ghi (record / 레코드).

> **Chuyển mạch:** Trong **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **Đọc tiếp** tiếp nhận điểm tựa từ **37. Checklist** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nguồn nền** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đọc tiếp

→ [09 — Carry, momentum, value and macro FX strategies](./09_CARRY_MOMENTUM_VALUE_AND_MACRO_FX_STRATEGIES.md)

> **Chuyển mạch:** Ở chặng này của **08 — Fundamental và event-driven FX phân tích (analysis / 분석)**, **Đọc tiếp** nêu điều cần giải thích; **Nguồn nền** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Nguồn nền

- Federal Reserve — FOMC calendars and official monetary-policy releases: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
- ECB — Monetary chính sách (policy / 정책) decisions: https://www.ecb.europa.eu/press/govcdec/mopo/html/chỉ mục (index / 인덱스).en.html
- Bank of Korea — Monetary Chính sách (policy / 정책) Decisions: https://www.bok.or.kr/eng/main/contents.do?menuNo=400015
- [Macro Data Playbook](../../04_economics/03_MACRO_DATA_PLAYBOOK.md)
- [04 — Macro drivers, rates, carry and sessions](./04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)

> **Bàn giao:** Sau **Nguồn nền**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
