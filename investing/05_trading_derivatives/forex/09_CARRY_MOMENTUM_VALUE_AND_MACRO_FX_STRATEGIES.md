# 09 — Carry, momentum, giá trị (value / 값) và macro FX strategies

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Chiến lược (strategy / 전략) family khác setup đơn lẻ** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Carry** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối carry, momentum, value và macro FX strategies, để so sánh nguồn premium, regime sensitivity và drawdown.

Sau khi hiểu mechanics, regime, indicator và sự kiện (event / 이벤트) phân tích (analysis / 분석), có thể bắt đầu nghiên cứu **chiến lược (strategy / 전략) families**. Mục tiêu của chương này không phải đưa ra tín hiệu giao dịch mà giải thích các nguồn return hypothesis thường gặp trong FX và cách phân biệt chúng.

Mô hình tư duy (mental model / 사고 모델):

```text
Economic / behavioral hypothesis
→ measurable signal
→ portfolio construction
→ execution and financing
→ realized return
→ attribution
```

Một chiến lược (strategy / 전략) family chỉ đáng tin khi return không phụ thuộc vào một chart example đẹp hoặc một parameter cụ thể.

## 1. Chiến lược (strategy / 전략) family khác setup đơn lẻ

Một setup như “RSI < 30 rồi buy” là quy tắc (rule / 규칙) rất cụ thể.

Một chiến lược (strategy / 전략) family như **trend/momentum** rộng hơn: nó giả định price changes có persistence ở một horizon nào đó.

Family-level thinking giúp hỏi:

- cơ chế (mechanism / 메커니즘) là gì;
- horizon nào phù hợp;
- regimes nào thuận lợi/bất lợi;
- hiện thực (implementation / 구현) nào robust.

> **Chuyển mạch:** Trong **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **2. Carry** tiếp nhận điểm tựa từ **1. Chiến lược (strategy / 전략) family khác setup đơn lẻ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Carry không phải free interest** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Carry

Carry chiến lược (strategy / 전략) trong FX khai thác chênh lệch yield/financing giữa currencies.

Simplified intuition:

```text
Long relatively high-yield currency
Short relatively low-yield currency
```

Return gần:

```text
Total Return
≈ Spot Return
+ Carry
- Transaction Cost
```

Carry chỉ profitable nếu adverse spot move không xóa financing advantage.

> **Chuyển mạch:** Ở chặng này của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **3. Carry không phải free interest** tiếp nhận điểm tựa từ **2. Carry** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Forward discount/premium và carry tín hiệu (signal / 신호)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Carry không phải free interest

High yield có thể phản ánh:

- inflation rủi ro (risk / 위험);
- devaluation rủi ro (risk / 위험);
- sovereign/political rủi ro (risk / 위험);
- liquidity rủi ro (risk / 위험);
- crash rủi ro (risk / 위험).

Do đó carry portfolios có thể kiếm nhỏ đều rồi mất mạnh trong risk-off unwind.

Rủi ro (risk / 위험) chỉ số (metric / 지표) cần chú ý skew/tail, không chỉ Sharpe.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **4. Forward discount/premium và carry tín hiệu (signal / 신호)** tiếp nhận điểm tựa từ **3. Carry không phải free interest** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Momentum / trend following** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Forward discount/premium và carry tín hiệu (signal / 신호)

Institutional research thường dùng forward points hoặc interest differential thay vì retail swap quote thô.

Retail broker financing có markup riêng, nên:

```text
academic carry signal
≠ exact retail realized carry
```

Backtest hiện thực (implementation / 구현) phải dùng instrument-specific financing.

> **Chuyển mạch:** Trong **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **5. Momentum / trend following** tiếp nhận điểm tựa từ **4. Forward discount/premium và carry tín hiệu (signal / 신호)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Time-series vs cross-sectional momentum** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Momentum / trend following

Momentum hypothesis:

```text
Currencies that appreciated over lookback
may continue outperforming over holding horizon
```

Possible mechanisms:

- gradual chính sách (policy / 정책) repricing;
- capital-flow persistence;
- underreaction;
- institutional thực thi (execution / 실행) over thời gian (time / 시간).

Hiện thực (implementation / 구현) có thể dùng:

- time-series momentum;
- cross-sectional momentum;
- breakout;
- moving-average trend.

> **Chuyển mạch:** Ở chặng này của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **6. Time-series vs cross-sectional momentum** tiếp nhận điểm tựa từ **5. Momentum / trend following** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Trend chiến lược (strategy / 전략) thường có profile khác carry** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Time-series vs cross-sectional momentum

### Time-series

So một currency pair với chính lịch sử (history / 이력) của nó:

```text
Past return > 0 → long
Past return < 0 → short
```

### Cross-sectional

Rank nhiều currencies theo past hiệu năng (performance / 성능):

```text
Long strongest group
Short weakest group
```

Hai cách có exposure và portfolio dynamics khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **7. Trend chiến lược (strategy / 전략) thường có profile khác carry** tiếp nhận điểm tựa từ **6. Time-series vs cross-sectional momentum** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Giá trị (value / 값) trong FX** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Trend chiến lược (strategy / 전략) thường có profile khác carry

Trend following thường có:

- nhiều small losses/whipsaws;
- một số large winners trong persistent moves.

Carry thường có thể có:

- frequent positive carry;
- occasional sharp reversals.

Kết hợp chiến lược (strategy / 전략) families cần nhìn correlation trong stress, không chỉ full-sample correlation.

> **Chuyển mạch:** Trong **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **8. Giá trị (value / 값) trong FX** tiếp nhận điểm tựa từ **7. Trend chiến lược (strategy / 전략) thường có profile khác carry** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Purchasing Power Parity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Giá trị (value / 값) trong FX

FX giá trị (value / 값) cố ước lượng currency “cheap/expensive” so với fundamental anchor.

Một anchor phổ biến trong academic discussion là purchasing power parity (PPP), nhưng FX giá trị (value / 값) có thể dùng nhiều các mô hình (models / 모델들) khác.

Giá trị (value / 값) thường có horizon dài hơn intraday technical setup.

> **Chuyển mạch:** Ở chặng này của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **9. Purchasing Power Parity** tiếp nhận điểm tựa từ **8. Giá trị (value / 값) trong FX** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Real exchange tỷ lệ (rate / 비율)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Purchasing Power Parity

PPP intuition:

```text
Long-run exchange rate
should relate to relative price levels
```

Nếu prices ở A tăng nhanh hơn B trong thời gian dài, currency A có thể cần adjust để restore relative purchasing power.

Nhưng PPP deviations có thể tồn tại nhiều năm vì:

- non-tradables;
- productivity differences;
- capital flows;
- rủi ro (risk / 위험) premium;
- chính sách (policy / 정책)/regime differences;
- đo lường (measurement / 측정) issues.

Do đó PPP không phải short-term timing mô hình (model / 모델).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **10. Real exchange tỷ lệ (rate / 비율)** tiếp nhận điểm tựa từ **9. Purchasing Power Parity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. BEER / FEER-like thinking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Real exchange tỷ lệ (rate / 비율)

A simplified real exchange-rate concept combines nominal FX với relative price levels.

Giá trị (value / 값) chiến lược (strategy / 전략) có thể rank currencies theo deviation của real exchange tỷ lệ (rate / 비율) khỏi long-run tham chiếu (reference / 참조).

Nhưng “mean” có thể shift structurally. Stationarity phải được tested, không assumed.

> **Chuyển mạch:** Trong **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **11. BEER / FEER-like thinking** tiếp nhận điểm tựa từ **10. Real exchange tỷ lệ (rate / 비율)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Macro directional chiến lược (strategy / 전략)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. BEER / FEER-like thinking

Behavioral/equilibrium exchange-rate frameworks có thể relate FX valuation tới:

- terms of trade;
- productivity;
- net foreign assets;
- real interest differentials;
- fiscal/bên ngoài (external / 외부) balance.

Mô hình (model / 모델) choice tạo mô hình (model / 모델) rủi ro (risk / 위험) lớn. Không nên có một “fair giá trị (value / 값)” với false precision.

> **Chuyển mạch:** Ở chặng này của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **12. Macro directional chiến lược (strategy / 전략)** tiếp nhận điểm tựa từ **11. BEER / FEER-like thinking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Event-driven chiến lược (strategy / 전략)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Macro directional chiến lược (strategy / 전략)

Macro FX chiến lược (strategy / 전략) xây thesis từ:

```text
policy divergence
relative growth/inflation
capital flows
external balance
risk regime
```

Điểm khó là timing. Fundamental mispricing có thể kéo dài.

Vì vậy macro trader thường cần catalyst hoặc price confirmation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **13. Event-driven chiến lược (strategy / 전략)** tiếp nhận điểm tựa từ **12. Macro directional chiến lược (strategy / 전략)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Mean reversion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Event-driven chiến lược (strategy / 전략)

Sự kiện (event / 이벤트) chiến lược (strategy / 전략) tập trung quanh scheduled/unscheduled releases.

Có thể nghiên cứu:

- surprise-following;
- initial overreaction mean reversion;
- post-announcement drift;
- volatility expansion;
- option sự kiện (event / 이벤트) premium.

Mỗi hypothesis cần timestamp resolution phù hợp.

> **Chuyển mạch:** Trong **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **14. Mean reversion** tiếp nhận điểm tựa từ **13. Event-driven chiến lược (strategy / 전략)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Relative-value / cross chiến lược (strategy / 전략)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Mean reversion

Mean-reversion chiến lược (strategy / 전략) giả định displacement hiện tại tạm thời và price sẽ quay về tham chiếu (reference / 참조).

Possible mechanisms:

- liquidity shock;
- temporary inventory imbalance;
- short-term overreaction;
- fixing/rebalancing luồng (flow / 흐름).

Rủi ro chính: temporary move thực ra là beginning của new trend/regime.

> **Chuyển mạch:** Ở chặng này của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **15. Relative-value / cross chiến lược (strategy / 전략)** tiếp nhận điểm tựa từ **14. Mean reversion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Dollar-neutral không đồng nghĩa risk-neutral** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Relative-value / cross chiến lược (strategy / 전략)

Thay vì directional USD exposure, có thể trade relative view:

```text
Long currency A
Short currency B
```

chọn B để isolate factor tốt hơn.

Ví dụ nếu thesis là Europe outperform Japan, EUR/JPY có thể express thesis trực tiếp hơn EUR/USD nếu USD factor không liên quan — nhưng instrument/liquidity/rủi ro (risk / 위험) vẫn phải đánh giá.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **16. Dollar-neutral không đồng nghĩa risk-neutral** tiếp nhận điểm tựa từ **15. Relative-value / cross chiến lược (strategy / 전략)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Statistical relative giá trị (value / 값)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Dollar-neutral không đồng nghĩa risk-neutral

Một basket có net USD exposure gần zero vẫn có:

- EUR/JPY/AUD factor rủi ro (risk / 위험);
- carry rủi ro (risk / 위험);
- toàn cục (global / 전역) rủi ro (risk / 위험) sentiment;
- liquidity rủi ro (risk / 위험).

Neutrality luôn phải nói neutral đối với factor nào.

> **Chuyển mạch:** Trong **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **17. Statistical relative giá trị (value / 값)** tiếp nhận điểm tựa từ **16. Dollar-neutral không đồng nghĩa risk-neutral** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Volatility chiến lược (strategy / 전략)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Statistical relative giá trị (value / 값)

Pairs/spread các mô hình (models / 모델들) có thể tìm mean-reverting relationship giữa FX rates hoặc related markets.

Nhưng correlation cao không đủ. Cần kiểm tra:

- economic linkage;
- stationarity/cointegration if relevant;
- structural breaks;
- thực thi (execution / 실행) chi phí (cost / 비용).

> **Chuyển mạch:** Ở chặng này của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **18. Volatility chiến lược (strategy / 전략)** tiếp nhận điểm tựa từ **17. Statistical relative giá trị (value / 값)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Hedging chiến lược (strategy / 전략) khác alpha chiến lược (strategy / 전략)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Volatility chiến lược (strategy / 전략)

FX options cho phép chiến lược (strategy / 전략) trên volatility thay vì chỉ direction:

- long/short volatility;
- relative vol;
- skew/rủi ro (risk / 위험) reversal;
- sự kiện (event / 이벤트) volatility;
- carry from option premium.

Đây là separate rủi ro (risk / 위험) dimension và được học sâu ở chapter 14.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **19. Hedging chiến lược (strategy / 전략) khác alpha chiến lược (strategy / 전략)** tiếp nhận điểm tựa từ **18. Volatility chiến lược (strategy / 전략)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Tín hiệu (signal / 신호) combination** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Hedging chiến lược (strategy / 전략) khác alpha chiến lược (strategy / 전략)

Một corporate/portfolio FX hedge có mục tiêu giảm variance hoặc protect liabilities, không phải maximize standalone P/L.

Đánh giá hedge bằng:

```text
risk reduction
cash-flow stability
cost
basis
liquidity
```

Không nên gọi hedge “thất bại” chỉ vì position hedge mất tiền khi underlying exposure tăng giá.

> **Chuyển mạch:** Trong **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **20. Tín hiệu (signal / 신호) combination** tiếp nhận điểm tựa từ **19. Hedging chiến lược (strategy / 전략) khác alpha chiến lược (strategy / 전략)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Composite score** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Tín hiệu (signal / 신호) combination

Có thể combine:

```text
Carry
Momentum
Value
Macro regime
```

Nhưng combination cần tránh double counting.

Ví dụ high-yield currency có thể đồng thời đang trong uptrend; carry và momentum signals correlated trong một regime.

> **Chuyển mạch:** Ở chặng này của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **21. Composite score** tiếp nhận điểm tựa từ **20. Tín hiệu (signal / 신호) combination** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Ranking vs absolute tín hiệu (signal / 신호)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Composite score

Một cách:

```text
Score = w1*Carry_z + w2*Momentum_z + w3*Value_z
```

Nhưng weights tạo estimation rủi ro (risk / 위험).

Nên kiểm thử (test / 테스트):

- equal weights;
- broad stable ranges;
- walk-forward weights;
- sensitivity to normalization.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **22. Ranking vs absolute tín hiệu (signal / 신호)** tiếp nhận điểm tựa từ **21. Composite score** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Volatility scaling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Ranking vs absolute tín hiệu (signal / 신호)

Cross-sectional strategies thường rank currencies:

```text
Top quantile → long
Bottom quantile → short
```

Điều này tạo relative portfolio nhưng có turnover và concentration implications.

> **Chuyển mạch:** Trong **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **23. Volatility scaling** tiếp nhận điểm tựa từ **22. Ranking vs absolute tín hiệu (signal / 신호)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Rủi ro (risk / 위험) parity không tạo alpha** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Volatility scaling

Để rủi ro (risk / 위험) across pairs comparable, position kích thước (size / 크기) có thể quy mô (scale / 규모) inversely với volatility:

```text
Weight_i ∝ Signal_i / Volatility_i
```

Nhưng volatility estimate lags shocks. Stress cap vẫn cần.

> **Chuyển mạch:** Ở chặng này của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **24. Rủi ro (risk / 위험) parity không tạo alpha** tiếp nhận điểm tựa từ **23. Volatility scaling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Currency basket exposure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Rủi ro (risk / 위험) parity không tạo alpha

Equalizing rủi ro (risk / 위험) contribution chỉ là portfolio construction. Nó không làm signals có positive expectancy.

Alpha hypothesis và rủi ro (risk / 위험) allocation phải tách riêng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **25. Currency basket exposure** tiếp nhận điểm tựa từ **24. Rủi ro (risk / 위험) parity không tạo alpha** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Carry + momentum** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Currency basket exposure

Nếu trade nhiều pairs, nên convert sang underlying currency exposures.

Ví dụ:

```text
Long EUR/USD
Long GBP/USD
Short USD/JPY
```

có concentrated short-USD factor.

Portfolio optimizer phải nhìn factor/currency ma trận (matrix / 행렬), không chỉ ticket weights.

> **Chuyển mạch:** Trong **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **26. Carry + momentum** tiếp nhận điểm tựa từ **25. Currency basket exposure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Giá trị (value / 값) + momentum** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Carry + momentum

Một practical research question:

> Carry tín hiệu (signal / 신호) có tốt hơn khi aligned với momentum không?

Kiểm thử (test / 테스트) conditional groups:

```text
High carry + positive momentum
High carry + negative momentum
Low carry + positive momentum
Low carry + negative momentum
```

Sau đó so phân phối (distribution / 분포) net of chi phí (cost / 비용).

Không assume combination better trước kiểm thử (test / 테스트).

> **Chuyển mạch:** Ở chặng này của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **27. Giá trị (value / 값) + momentum** tiếp nhận điểm tựa từ **26. Carry + momentum** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Regime-conditioned chiến lược (strategy / 전략)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Giá trị (value / 값) + momentum

Giá trị (value / 값) có thể bắt falling knife; momentum có thể buy expensive currency.

Combination đôi khi dùng momentum làm timing filter cho long-horizon giá trị (value / 값).

Nhưng filter có thể làm giảm cỡ mẫu (sample size / 표본 크기) và tăng data-mining rủi ro (risk / 위험).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **28. Regime-conditioned chiến lược (strategy / 전략)** tiếp nhận điểm tựa từ **27. Giá trị (value / 값) + momentum** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Chiến lược (strategy / 전략) turnover** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Regime-conditioned chiến lược (strategy / 전략)

Một chiến lược (strategy / 전략) có thể chỉ active khi:

```text
volatility below threshold
policy divergence high
liquidity normal
```

Conditioning phải có economic reason và được xác định trước, nếu không rất dễ overfit.

> **Chuyển mạch:** Trong **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **29. Chiến lược (strategy / 전략) turnover** tiếp nhận điểm tựa từ **28. Regime-conditioned chiến lược (strategy / 전략)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Sức chứa (capacity / 용량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Chiến lược (strategy / 전략) turnover

Turnover quyết định sensitivity với chi phí (cost / 비용).

```text
Annual turnover
× average all-in cost
```

có thể ăn phần lớn gross alpha.

Tín hiệu (signal / 신호) frequency cao chưa chắc tốt nếu edge per trade nhỏ.

> **Chuyển mạch:** Ở chặng này của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **30. Sức chứa (capacity / 용량)** tiếp nhận điểm tựa từ **29. Chiến lược (strategy / 전략) turnover** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Crowding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Sức chứa (capacity / 용량)

Retail major-FX chiến lược (strategy / 전략) thường có sức chứa (capacity / 용량) lớn so với account nhỏ, nhưng không nên bỏ concept.

Sức chứa (capacity / 용량) giảm khi:

- pair illiquid;
- horizon ngắn;
- thứ tự (order / 순서) kích thước (size / 크기) lớn;
- sự kiện (event / 이벤트) thực thi (execution / 실행);
- exotic/offshore instruments.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **31. Crowding** tiếp nhận điểm tựa từ **30. Sức chứa (capacity / 용량)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Structural break** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Crowding

Một chiến lược (strategy / 전략) widely known như carry/momentum có thể bị crowded.

Crowding có thể:

- compress expected return;
- increase unwind correlation;
- worsen crash rủi ro (risk / 위험).

Không dễ đo trực tiếp, nên positioning/liquidity proxies chỉ là partial thông tin (information / 정보).

> **Chuyển mạch:** Trong **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **32. Structural break** tiếp nhận điểm tựa từ **31. Crowding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Chiến lược (strategy / 전략) decay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Structural break

FX regimes thay đổi vì:

- monetary khung phần mềm (framework / 프레임워크);
- capital controls;
- thị trường (market / 시장) cấu trúc (structure / 구조);
- intervention;
- crisis;
- regulation.

Một chiến lược (strategy / 전략) profitable 1990–2010 không tự động representative 2020s.

Kiểm tra hợp lệ (validation / 검증) phải span multiple regimes và emphasize recent relevance without discarding lịch sử (history / 이력) arbitrarily.

> **Chuyển mạch:** Ở chặng này của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **33. Chiến lược (strategy / 전략) decay** tiếp nhận điểm tựa từ **32. Structural break** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Attribution by return nguồn (source / 소스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Chiến lược (strategy / 전략) decay

Sau triển khai (deployment / 배포), edge có thể giảm vì:

- thị trường (market / 시장) adaptation;
- chi phí (cost / 비용) changes;
- dữ liệu (data / 데이터) relationship breaks;
- crowding;
- hiện thực (implementation / 구현) drift.

Monitoring cần compare live phân phối (distribution / 분포) với research các giả định (assumptions / 가정들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **33. Chiến lược (strategy / 전략) decay** nêu điều cần giải thích; **34. Attribution by return nguồn (source / 소스)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **35. Benchmark** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Attribution by return nguồn (source / 소스)

Một FX chiến lược (strategy / 전략) P/L nên tách nếu có thể:

```text
Spot move
Carry/financing
Transaction cost
Slippage
Hedge effect
Currency conversion
```

Nếu không, trader có thể tưởng tín hiệu (signal / 신호) kiếm tiền trong khi actual return chủ yếu đến từ carry hoặc broad USD beta.

> **Chuyển mạch:** Trong **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **34. Attribution by return nguồn (source / 소스)** nêu điều cần giải thích; **35. Benchmark** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **36. Chiến lược (strategy / 전략) specification template** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Benchmark

Chiến lược (strategy / 전략) cần benchmark phù hợp:

- cash/risk-free;
- passive currency exposure;
- simple carry/momentum quy tắc (rule / 규칙);
- equal-risk baseline.

Một complex mô hình (model / 모델) chỉ có giá trị (value / 값) nếu vượt simple baseline sau chi phí (cost / 비용) và độ phức tạp (complexity / 복잡도) penalty.

> **Chuyển mạch:** Ở chặng này của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **36. Chiến lược (strategy / 전략) specification template** tiếp nhận điểm tựa từ **35. Benchmark** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Không đánh giá bằng win tỷ lệ (rate / 비율)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Chiến lược (strategy / 전략) specification template

```text
Universe:
Eligible currency pairs/instruments.

Hypothesis:
Economic/behavioral mechanism.

Signal:
Exact formula and timestamp.

Rebalance:
Frequency and calendar rule.

Sizing:
Volatility/risk constraints.

Execution:
Order/fill assumption.

Financing:
Instrument-specific carry.

Costs:
Spread, commission, slippage.

Risk:
Gross/net leverage, currency caps, drawdown controls.

Validation:
Out-of-sample / walk-forward.

Kill criteria:
Conditions for research review or shutdown.
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **37. Không đánh giá bằng win tỷ lệ (rate / 비율)** tiếp nhận điểm tựa từ **36. Chiến lược (strategy / 전략) specification template** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. Không chọn chiến lược (strategy / 전략) vì backtest đẹp nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Không đánh giá bằng win tỷ lệ (rate / 비율)

Carry/trend/giá trị (value / 값) có payoff distributions khác nhau.

Cần nhìn:

- expectancy;
- volatility;
- drawdown;
- skew;
- tail mất mát (loss / 손실);
- turnover;
- chi phí (cost / 비용);
- correlation;
- cỡ mẫu (sample size / 표본 크기).

Win tỷ lệ (rate / 비율) alone gần như không đủ.

> **Chuyển mạch:** Trong **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **38. Không chọn chiến lược (strategy / 전략) vì backtest đẹp nhất** tiếp nhận điểm tựa từ **37. Không đánh giá bằng win tỷ lệ (rate / 비율)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Không chọn chiến lược (strategy / 전략) vì backtest đẹp nhất

Nếu thử 100 chiến lược (strategy / 전략) families/settings rồi chọn top Sharpe, estimate bị selection độ lệch (bias / 편향).

Chapter 10 sẽ đi sâu cách backtest point-in-time, multiple testing và robustness.

> **Chuyển mạch:** Ở chặng này của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **39. Checklist** tiếp nhận điểm tựa từ **38. Không chọn chiến lược (strategy / 전략) vì backtest đẹp nhất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đọc tiếp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Checklist

Bạn cần phân biệt được:

1. Carry return và spot return.
2. Time-series và cross-sectional momentum.
3. Giá trị (value / 값) horizon và timing bài toán (problem / 문제).
4. Macro chiến lược (strategy / 전략) với sự kiện (event / 이벤트) chiến lược (strategy / 전략).
5. Mean reversion rủi ro (risk / 위험) khi regime shifts.
6. Alpha tín hiệu (signal / 신호) và portfolio construction.
7. Currency-factor aggregation.
8. Turnover/chi phí (cost / 비용)/sức chứa (capacity / 용량).
9. Chiến lược (strategy / 전략) family và parameterized hiện thực (implementation / 구현).
10. Vì sao attribution quan trọng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **Đọc tiếp** tiếp nhận điểm tựa từ **39. Checklist** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nội bộ (internal / 내부) links** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đọc tiếp

→ [10 — Backtesting and point-in-time FX data](./10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)

> **Chuyển mạch:** Trong **09 — Carry, momentum, giá trị (value / 값) và macro FX strategies**, **Nội bộ (internal / 내부) links** tiếp nhận điểm tựa từ **Đọc tiếp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Nội bộ (internal / 내부) links

- [08 — Fundamental and event-driven FX analysis](./08_FUNDAMENTAL_AND_EVENT_DRIVEN_FX_ANALYSIS.md)
- [07 — Technical indicators](./07_TECHNICAL_INDICATORS_AS_DATA_TRANSFORMATIONS.md)
- [Strategy research and robustness](../04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md)
- [Systematic risk, backtest and execution](../02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md)

> **Bàn giao:** Sau **Nội bộ (internal / 내부) links**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
