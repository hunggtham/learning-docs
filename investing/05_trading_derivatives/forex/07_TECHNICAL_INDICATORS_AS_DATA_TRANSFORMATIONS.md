# 07 — Technical indicators như các phép biến đổi dữ liệu

> **Mạch đọc:** [README](./README.md) là owner của **07 — Technical indicators như các phép biến đổi dữ liệu**; giữ chapter trong tuyến FX data, signal và backtest. Từ **1. Indicator trả lời câu hỏi gì?** chuyển sang moving average, momentum, volatility, normalization và feature dependence, rồi nối transformation với rule/statistical test; indicator chỉ là biểu diễn dữ liệu, không tự tạo causal edge.

Indicator không phải lớp thông tin tách biệt khỏi price. Phần lớn technical indicators là **phép biến đổi của price, return, phạm vi (range / 범위) hoặc volume-like dữ liệu (data / 데이터)**. Hiểu điều này giúp tránh hai lỗi phổ biến: coi indicator là tín hiệu tiên tri và chồng nhiều indicator gần như đo cùng một thứ rồi tưởng rằng có nhiều confirmation độc lập.

Mô hình tư duy (mental model / 사고 모델):

```text
Raw market data
→ transformation
→ smoothed / normalized representation
→ rule
→ statistical test
```

## 1. Indicator trả lời câu hỏi gì?

Một indicator có thể được dùng để ước lượng:

- direction/trend;
- momentum;
- volatility;
- relative position trong recent phạm vi (range / 범위);
- distance from a tham chiếu (reference / 참조) mean;
- tỷ lệ (rate / 비율) of thay đổi (change / 변경);
- volume/luồng (flow / 흐름) proxy nếu dữ liệu (data / 데이터) có volume phù hợp.

Indicator hữu ích khi nó biến một câu hỏi định tính thành chỉ số (metric / 지표) có thể định nghĩa và kiểm thử.

> **Nối mạch:** Trong **07 — Technical indicators như các phép biến đổi dữ liệu**, **2. Moving average** nối từ **1. Indicator trả lời câu hỏi gì?** sang **3. EMA**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Moving average

Simple moving average:

```text
SMA_N(t) = (P_t + P_{t-1} + ... + P_{t-N+1}) / N
```

Nó là low-pass smoothing: giảm short-term noise nhưng tạo lag.

Nếu price tăng nhanh, moving average phản ứng chậm vì vẫn chứa historical prices.

Do đó lag không phải bug; nó là sự đánh đổi (trade-off / 트레이드오프) trực tiếp của smoothing.

> **Nối mạch:** Ở chặng này của **07 — Technical indicators như các phép biến đổi dữ liệu**, **3. EMA** nối từ **2. Moving average** sang **4. Moving-average crossover**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. EMA

Exponential moving average đặt trọng số lớn hơn cho observations mới:

```text
EMA_t = αP_t + (1-α)EMA_{t-1}
```

với:

```text
α ≈ 2 / (N + 1)
```

EMA phản ứng nhanh hơn SMA cùng nominal lookback nhưng vẫn là smoothing filter.

Không có lý do toán học cho rằng EMA20 “tốt” hơn EMA21 một cách universal. Parameter phải được hiểu như horizon choice và kiểm tra robustness.

> **Nối mạch:** Đặt trong câu hỏi lớn của **07 — Technical indicators như các phép biến đổi dữ liệu**, **4. Moving-average crossover** nối từ **3. EMA** sang **5. Momentum**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Moving-average crossover

Quy tắc (rule / 규칙):

```text
Fast MA > Slow MA → positive trend state
Fast MA < Slow MA → negative trend state
```

Nó không dự đoán turning điểm (point / 지점) tức thì. Crossover là delayed confirmation rằng recent prices đã thay đổi đủ để fast average vượt slow average.

Chiến lược (strategy / 전략) có thể hoạt động khi trend persistence bù được whipsaw chi phí (cost / 비용), nhưng thường gặp khó trong phạm vi (range / 범위).

> **Nối mạch:** Trong **07 — Technical indicators như các phép biến đổi dữ liệu**, **5. Momentum** nối từ **4. Moving-average crossover** sang **6. Tỷ lệ (rate / 비율) of Thay đổi (change / 변경)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Momentum

Một definition đơn giản:

```text
Momentum_N = P_t / P_{t-N} - 1
```

hoặc log return:

```text
m_N = ln(P_t / P_{t-N})
```

Momentum dương chỉ nói price hiện cao hơn N periods trước. Nó không giải thích tại sao và không bảo đảm tiếp tục.

> **Nối mạch:** Ở chặng này của **07 — Technical indicators như các phép biến đổi dữ liệu**, **6. Tỷ lệ (rate / 비율) of Thay đổi (change / 변경)** nối từ **5. Momentum** sang **7. RSI**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Tỷ lệ (rate / 비율) of Thay đổi (change / 변경)

ROC là percentage thay đổi (change / 변경) qua lookback. Nó gần với momentum nhưng cách quy mô (scale / 규모) có thể khác.

Điểm quan trọng:

```text
price change
→ normalized by prior price
```

nên so sánh giữa periods dễ hơn raw pip movement.

> **Nối mạch:** Đặt trong câu hỏi lớn của **07 — Technical indicators như các phép biến đổi dữ liệu**, **7. RSI** nối từ **6. Tỷ lệ (rate / 비율) of Thay đổi (change / 변경)** sang **8. RSI divergence**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. RSI

Relative Strength Chỉ mục (index / 인덱스) không đo “sức mạnh của EUR so với USD” theo macro nghĩa. Nó là oscillator từ average positive và negative price changes.

Dùng chung (common / 공통) form:

```text
RS = Avg Gain / Avg Loss
RSI = 100 - 100 / (1 + RS)
```

RSI gần 70/30 thường được gọi overbought/oversold, nhưng đây không phải natural law.

Trong strong trend, RSI có thể ở vùng cao/thấp lâu. Vì vậy:

```text
RSI high
≠ price must fall
```

Nó chỉ nói recent upward changes lớn tương đối so với downward changes theo calculation cửa sổ (window / 윈도우).

> **Nối mạch:** Trong **07 — Technical indicators như các phép biến đổi dữ liệu**, **8. RSI divergence** nối từ **7. RSI** sang **9. MACD**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. RSI divergence

Divergence thường mô tả:

```text
price makes new high
but RSI does not
```

Vì RSI là transformed momentum, divergence nói momentum của move đang khác prior move. Nó không guarantee reversal.

Để backtest phải formalize pivot detection, tolerance và horizon; nếu không hindsight độ lệch (bias / 편향) rất lớn.

> **Nối mạch:** Ở chặng này của **07 — Technical indicators như các phép biến đổi dữ liệu**, **9. MACD** nối từ **8. RSI divergence** sang **10. Stochastic oscillator**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. MACD

MACD thường dựa trên difference giữa hai EMAs:

```text
MACD = EMA_fast - EMA_slow
Signal = EMA(MACD)
Histogram = MACD - Signal
```

Vì vậy MACD không phải nguồn (source / 소스) dữ liệu mới. Nó là combination của smoothed trend/momentum.

Dùng MACD cùng nhiều moving-average signals có thể tạo **redundant confirmation**.

> **Nối mạch:** Đặt trong câu hỏi lớn của **07 — Technical indicators như các phép biến đổi dữ liệu**, **10. Stochastic oscillator** nối từ **9. MACD** sang **11. Bollinger Bands**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Stochastic oscillator

Stochastic so close hiện tại với recent high-low phạm vi (range / 범위):

```text
%K = (Close - LowestLow_N) / (HighestHigh_N - LowestLow_N) × 100
```

Nó trả lời:

> Close hiện nằm ở đâu trong phạm vi (range / 범위) N periods gần nhất?

Không phải:

> Thị trường (market / 시장) đã quá mua nên chắc chắn đảo chiều.

> **Nối mạch:** Trong **07 — Technical indicators như các phép biến đổi dữ liệu**, **11. Bollinger Bands** nối từ **10. Stochastic oscillator** sang **12. ATR**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Bollinger Bands

Basic construction:

```text
Middle = Moving Average
Upper = MA + kσ
Lower = MA - kσ
```

Bands kết hợp mean estimate và recent dispersion.

Price chạm upper band có thể nghĩa:

- strong trend;
- temporary extension;
- volatility expansion.

Ngữ cảnh (context / 맥락) quyết định interpretation. Band không tự phát lệnh sell.

> **Nối mạch:** Ở chặng này của **07 — Technical indicators như các phép biến đổi dữ liệu**, **12. ATR** nối từ **11. Bollinger Bands** sang **13. ADX**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. ATR

ATR đo phạm vi (range / 범위) magnitude chứ không hướng.

Ứng dụng hợp lý:

- volatility-normalized stop;
- position sizing;
- regime classification;
- filter periods quá yên hoặc quá biến động.

ATR multiplier như `2×ATR` không có universal optimality. Cần liên hệ với chiến lược (strategy / 전략) horizon và phân phối (distribution / 분포).

> **Nối mạch:** Đặt trong câu hỏi lớn của **07 — Technical indicators như các phép biến đổi dữ liệu**, **13. ADX** nối từ **12. ATR** sang **14. Donchian channel**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. ADX

Average Directional Chỉ mục (index / 인덱스) được thiết kế để đo trend strength từ directional movement, không trực tiếp nói trend direction.

Một ADX cao có thể xảy ra trong downtrend lẫn uptrend.

Nếu dùng ADX như “buy indicator” mà bỏ qua construction, interpretation đã sai từ đầu.

> **Nối mạch:** Trong **07 — Technical indicators như các phép biến đổi dữ liệu**, **14. Donchian channel** nối từ **13. ADX** sang **15. Z-score**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Donchian channel

```text
Upper = highest high over N periods
Lower = lowest low over N periods
```

Đây là transformation rất trực tiếp của recent extremes và thường dùng trong breakout/trend các hệ thống (systems / 시스템들).

Nó cho thấy đôi khi “indicator” chỉ là một cách formalize price-action quy tắc (rule / 규칙).

> **Nối mạch:** Ở chặng này của **07 — Technical indicators như các phép biến đổi dữ liệu**, **15. Z-score** nối từ **14. Donchian channel** sang **16. Indicator normalization**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Z-score

Nếu có tham chiếu (reference / 참조) mean `μ` và tiêu chuẩn (standard / 표준) deviation `σ`:

```text
Z = (X - μ) / σ
```

Z-score nói observation cách mean bao nhiêu tiêu chuẩn (standard / 표준) deviations theo mô hình (model / 모델)/cửa sổ (window / 윈도우).

Nhưng nếu phân phối (distribution / 분포) non-stationary hoặc fat-tailed, `Z=3` không nên được đọc máy móc theo normal phân phối (distribution / 분포) xác suất (probability / 확률).

> **Nối mạch:** Đặt trong câu hỏi lớn của **07 — Technical indicators như các phép biến đổi dữ liệu**, **16. Indicator normalization** nối từ **15. Z-score** sang **17. Volume trong spot FX cần cẩn thận**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Indicator normalization

Raw indicator values có thể khó so giữa pairs. Có thể normalize bằng:

- volatility;
- percentage return;
- z-score;
- percentile rank.

Ví dụ moving-average distance:

```text
(P - MA) / ATR
```

thường comparable hơn raw pip distance.

> **Nối mạch:** Trong **07 — Technical indicators như các phép biến đổi dữ liệu**, **17. Volume trong spot FX cần cẩn thận** nối từ **16. Indicator normalization** sang **18. Tick volume**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Volume trong spot FX cần cẩn thận

OTC FX không có một centralized tape toàn cầu. Retail chart thường có:

- tick volume;
- broker-specific giao dịch (transaction / 트랜잭션) volume;
- venue-specific volume.

Đừng gọi đó là “toàn cục (global / 전역) Forex volume”.

Exchange-traded currency futures có centralized venue volume của exchange đó, nhưng cũng không đại diện toàn bộ OTC thị trường (market / 시장).

> **Nối mạch:** Ở chặng này của **07 — Technical indicators như các phép biến đổi dữ liệu**, **18. Tick volume** nối từ **17. Volume trong spot FX cần cẩn thận** sang **19. VWAP trong Forex**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Tick volume

Tick volume thường đếm số lần price cập nhật (update / 업데이트) trong period. Nó có thể correlate với activity ở một dữ liệu (data / 데이터) nguồn (source / 소스) nhưng không trực tiếp bằng notional traded globally.

Nếu chiến lược (strategy / 전략) dùng tick volume, phải giữ dữ liệu (data / 데이터) nguồn (source / 소스) nhất quán và kiểm thử (test / 테스트) out-of-sample.

> **Nối mạch:** Đặt trong câu hỏi lớn của **07 — Technical indicators như các phép biến đổi dữ liệu**, **19. VWAP trong Forex** nối từ **18. Tick volume** sang **20. Indicator stacking và multicollinearity**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. VWAP trong Forex

VWAP cần price và actual volume của venue/dataset:

```text
VWAP = Σ(P_i × V_i) / ΣV_i
```

Trong decentralized spot FX, “VWAP” trên retail nguồn (source / 소스) có thể không mang cùng meaning như VWAP của centralized exchange equity/futures dữ liệu (data / 데이터).

Phải biết `V_i` thực sự là gì.

> **Nối mạch:** Trong **07 — Technical indicators như các phép biến đổi dữ liệu**, **20. Indicator stacking và multicollinearity** nối từ **19. VWAP trong Forex** sang **21. Parameter sensitivity**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Indicator stacking và multicollinearity

Ví dụ dùng cùng lúc:

```text
MA crossover
MACD
RSI momentum
ROC
```

có thể trông như bốn confirmations nhưng tất cả đều phần lớn xuất phát từ recent price changes.

Trong mô hình (model / 모델), các features có thể highly correlated.

Cần hỏi:

```text
Does each feature add incremental information?
```

không phải:

```text
How many indicators agree?
```

> **Nối mạch:** Ở chặng này của **07 — Technical indicators như các phép biến đổi dữ liệu**, **21. Parameter sensitivity** nối từ **20. Indicator stacking và multicollinearity** sang **22. Overfitting bằng indicator combinations**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Parameter sensitivity

Nếu chiến lược (strategy / 전략) chỉ profitable với:

```text
RSI length = 14
threshold = 31.7
MA = 47
```

nhưng thất bại khi parameters thay đổi nhẹ, đó là dấu hiệu fragility.

Robust edge thường có vùng parameter tương đối ổn định thay vì một spike tối ưu sắc nhọn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **07 — Technical indicators như các phép biến đổi dữ liệu**, **22. Overfitting bằng indicator combinations** nối từ **21. Parameter sensitivity** sang **23. Indicator lag và quyết định (decision / 결정) độ trễ (latency / 지연 시간)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Overfitting bằng indicator combinations

Thử đủ nhiều:

```text
RSI thresholds
MA lengths
MACD settings
ATR filters
sessions
pairs
```

sẽ tìm được một combination lịch sử đẹp dù không có true edge.

Vì vậy indicator research không thể tách khỏi multiple testing và walk-forward kiểm tra hợp lệ (validation / 검증).

> **Nối mạch:** Trong **07 — Technical indicators như các phép biến đổi dữ liệu**, **23. Indicator lag và quyết định (decision / 결정) độ trễ (latency / 지연 시간)** nối từ **22. Overfitting bằng indicator combinations** sang **24. Repainting**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Indicator lag và quyết định (decision / 결정) độ trễ (latency / 지연 시간)

Indicator dùng close của bar chỉ biết chính xác sau bar close.

Nếu backtest entry ở đúng close đó mà không modeling khả năng thực thi, có thể tạo optimistic fill.

Chuỗi xử lý (pipeline / 파이프라인) đúng:

```text
bar closes
→ indicator becomes known
→ signal computed
→ order sent
→ next executable price
```

trừ khi hệ thống (system / 시스템) thật sự có intrabar dữ liệu (data / 데이터)/quy tắc (rule / 규칙).

> **Nối mạch:** Ở chặng này của **07 — Technical indicators như các phép biến đổi dữ liệu**, **24. Repainting** nối từ **23. Indicator lag và quyết định (decision / 결정) độ trễ (latency / 지연 시간)** sang **25. Centered moving averages và look-ahead**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Repainting

Một số indicators/visual tools thay đổi historical display khi future dữ liệu (data / 데이터) xuất hiện hoặc hiện tại (current / 현재) bar chưa đóng.

Research phải phân biệt:

```text
value known at time t
versus
final value shown later
```

Nếu indicator repaint, screenshot historical đẹp có thể không phản ánh tín hiệu (signal / 신호) live.

> **Nối mạch:** Đặt trong câu hỏi lớn của **07 — Technical indicators như các phép biến đổi dữ liệu**, **25. Centered moving averages và look-ahead** nối từ **24. Repainting** sang **26. Indicator as tính năng (feature / 기능), not quy tắc (rule / 규칙)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. Centered moving averages và look-ahead

Một filter dùng observations trước và sau `t` có thể tạo smooth line tuyệt đẹp nhưng không usable live vì future dữ liệu (data / 데이터) chưa tồn tại.

Bất kỳ transformation nào dùng future samples đều phải được coi là retrospective phân tích (analysis / 분석), không phải trading tín hiệu (signal / 신호) tại t.

> **Nối mạch:** Trong **07 — Technical indicators như các phép biến đổi dữ liệu**, **26. Indicator as tính năng (feature / 기능), not quy tắc (rule / 규칙)** nối từ **25. Centered moving averages và look-ahead** sang **27. Nhị phân (binary / 이진) threshold làm mất thông tin**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Indicator as tính năng (feature / 기능), not quy tắc (rule / 규칙)

Trong quantitative mô hình (model / 모델), indicator có thể là tính năng (feature / 기능):

```text
trend score
volatility percentile
RSI percentile
carry
rate differential
session
```

Mô hình (model / 모델) sau đó estimate conditional kết quả (outcome / 결과).

Điều này thường tốt hơn việc gán mystical meaning cho một threshold duy nhất.

> **Nối mạch:** Ở chặng này của **07 — Technical indicators như các phép biến đổi dữ liệu**, **27. Nhị phân (binary / 이진) threshold làm mất thông tin** nối từ **26. Indicator as tính năng (feature / 기능), not quy tắc (rule / 규칙)** sang **28. Conditional indicator phân tích (analysis / 분석)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Nhị phân (binary / 이진) threshold làm mất thông tin

Ví dụ:

```text
RSI < 30 = BUY
RSI >= 30 = NO BUY
```

biến continuous variable thành nhị phân (binary / 이진) quy tắc (rule / 규칙).

Có thể nghiên cứu kết quả (outcome / 결과) theo bins:

```text
0–10
10–20
20–30
...
```

để xem quan hệ (relation / 관계) có monotonic hay không.

> **Nối mạch:** Đặt trong câu hỏi lớn của **07 — Technical indicators như các phép biến đổi dữ liệu**, **28. Conditional indicator phân tích (analysis / 분석)** nối từ **27. Nhị phân (binary / 이진) threshold làm mất thông tin** sang **29. Indicator và nhân quả (causal / 인과적) cơ chế (mechanism / 메커니즘)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. Conditional indicator phân tích (analysis / 분석)

Thay vì hỏi:

> RSI oversold có hiệu quả không?

hãy hỏi:

```text
What is future-return distribution conditional on:
RSI percentile
× trend regime
× volatility regime
× session
× event state
× cost
```

Có thể một indicator chỉ hữu ích trong subset cụ thể.

> **Nối mạch:** Trong **07 — Technical indicators như các phép biến đổi dữ liệu**, **28. Conditional indicator phân tích (analysis / 분석)** đặt đầu vào cho **29. Indicator và nhân quả (causal / 인과적) cơ chế (mechanism / 메커니즘)**, rồi **30. Không dùng indicator để che một thesis mơ hồ** mở rộng hệ quả hoặc giới hạn liên quan.

## 29. Indicator và nhân quả (causal / 인과적) cơ chế (mechanism / 메커니즘)

Pure technical tín hiệu (signal / 신호) không nhất thiết cần fundamental causality mạnh để có predictive giá trị (value / 값), nhưng một plausible cơ chế (mechanism / 메커니즘) giúp giảm nguy cơ data-mined coincidence.

Ví dụ trend persistence có thể liên hệ:

- gradual thông tin (information / 정보) diffusion;
- institutional thực thi (execution / 실행) over thời gian (time / 시간);
- behavioral underreaction;
- chính sách (policy / 정책) divergence.

Mean reversion có thể liên hệ:

- temporary liquidity imbalance;
- inventory correction;
- overreaction.

Cơ chế (mechanism / 메커니즘) là hypothesis, vẫn cần dữ liệu (data / 데이터) kiểm thử (test / 테스트).

> **Nối mạch:** Ở chặng này của **07 — Technical indicators như các phép biến đổi dữ liệu**, **29. Indicator và nhân quả (causal / 인과적) cơ chế (mechanism / 메커니즘)** đặt đầu vào cho **30. Không dùng indicator để che một thesis mơ hồ**, rồi **31. Minimal indicator research template** mở rộng hệ quả hoặc giới hạn liên quan.

## 30. Không dùng indicator để che một thesis mơ hồ

Một trade explanation kiểu:

```text
RSI oversold
MACD turning
price at support
Bollinger lower band
```

có thể chỉ là bốn cách nói rằng price vừa giảm mạnh.

Một specification tốt phải nêu:

```text
What market behavior is expected?
Why should it persist/revert?
What data transformation measures it?
What invalidates it?
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **07 — Technical indicators như các phép biến đổi dữ liệu**, **31. Minimal indicator research template** nối từ **30. Không dùng indicator để che một thesis mơ hồ** sang **32. Checklist**, vì cơ chế trước tạo đầu vào cho bước sau.

## 31. Minimal indicator research template

```text
Question:
Does medium-term trend persist in major FX pairs?

Feature:
20-day log return.

Filter:
Realized volatility percentile.

Signal:
Long if momentum > threshold, short if < -threshold.

Execution:
Next-session executable price.

Sizing:
Volatility target.

Cost:
Spread + slippage + financing.

Validation:
Walk-forward across pairs and decades/regimes.
```

Indicator chỉ là một thành phần (component / 컴포넌트) trong toàn research chuỗi xử lý (pipeline / 파이프라인).

> **Nối mạch:** Trong **07 — Technical indicators như các phép biến đổi dữ liệu**, **32. Checklist** nối từ **31. Minimal indicator research template** sang **Đọc tiếp**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. Checklist

Bạn cần tự giải thích được:

1. SMA/EMA sự đánh đổi (trade-off / 트레이드오프) giữa smoothing và lag.
2. RSI thực sự được tính từ gì.
3. MACD vì sao phần lớn là moving-average transformation.
4. ATR khác directional indicator như thế nào.
5. Vì sao spot FX volume cần ghi rõ nguồn (source / 소스).
6. Vì sao nhiều indicators có thể không phải nhiều independent confirmations.
7. Repainting/look-ahead xảy ra thế nào.
8. Vì sao parameter stability quan trọng hơn single best setting.
9. Indicator phải được đánh giá sau giao dịch (transaction / 트랜잭션) costs.

> **Nối mạch:** Ở chặng này của **07 — Technical indicators như các phép biến đổi dữ liệu**, **Đọc tiếp** nối từ **32. Checklist** sang **Nội bộ (internal / 내부) links**, vì cơ chế trước tạo đầu vào cho bước sau.

## Đọc tiếp

→ [08 — Fundamental and event-driven FX analysis](./08_FUNDAMENTAL_AND_EVENT_DRIVEN_FX_ANALYSIS.md)

> **Nối mạch:** Đặt trong câu hỏi lớn của **07 — Technical indicators như các phép biến đổi dữ liệu**, **Nội bộ (internal / 내부) links** nối từ **Đọc tiếp** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Nội bộ (internal / 내부) links

- [06 — Price action and regimes](./06_PRICE_ACTION_TREND_RANGE_AND_VOLATILITY_REGIMES.md)
- [04 — Macro drivers, rates, carry and sessions](./04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)
- [Systematic risk, backtest and execution](../02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md)
- [Strategy research and robustness](../04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md)

> **Bàn giao:** Sau **Nội bộ (internal / 내부) links**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
