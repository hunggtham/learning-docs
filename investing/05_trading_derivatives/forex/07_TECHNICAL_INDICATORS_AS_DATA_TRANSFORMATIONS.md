# 07 — Technical indicators như các phép biến đổi dữ liệu

Indicator không phải lớp thông tin tách biệt khỏi price. Phần lớn technical indicators là **phép biến đổi của price, return, range hoặc volume-like data**. Hiểu điều này giúp tránh hai lỗi phổ biến: coi indicator là tín hiệu tiên tri và chồng nhiều indicator gần như đo cùng một thứ rồi tưởng rằng có nhiều confirmation độc lập.

Mental model:

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
- relative position trong recent range;
- distance from a reference mean;
- rate of change;
- volume/flow proxy nếu data có volume phù hợp.

Indicator hữu ích khi nó biến một câu hỏi định tính thành metric có thể định nghĩa và kiểm thử.

## 2. Moving average

Simple moving average:

```text
SMA_N(t) = (P_t + P_{t-1} + ... + P_{t-N+1}) / N
```

Nó là low-pass smoothing: giảm short-term noise nhưng tạo lag.

Nếu price tăng nhanh, moving average phản ứng chậm vì vẫn chứa historical prices.

Do đó lag không phải bug; nó là trade-off trực tiếp của smoothing.

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

## 4. Moving-average crossover

Rule:

```text
Fast MA > Slow MA → positive trend state
Fast MA < Slow MA → negative trend state
```

Nó không dự đoán turning point tức thì. Crossover là delayed confirmation rằng recent prices đã thay đổi đủ để fast average vượt slow average.

Strategy có thể hoạt động khi trend persistence bù được whipsaw cost, nhưng thường gặp khó trong range.

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

## 6. Rate of Change

ROC là percentage change qua lookback. Nó gần với momentum nhưng cách scale có thể khác.

Điểm quan trọng:

```text
price change
→ normalized by prior price
```

nên so sánh giữa periods dễ hơn raw pip movement.

## 7. RSI

Relative Strength Index không đo “sức mạnh của EUR so với USD” theo macro nghĩa. Nó là oscillator từ average positive và negative price changes.

Common form:

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

Nó chỉ nói recent upward changes lớn tương đối so với downward changes theo calculation window.

## 8. RSI divergence

Divergence thường mô tả:

```text
price makes new high
but RSI does not
```

Vì RSI là transformed momentum, divergence nói momentum của move đang khác prior move. Nó không guarantee reversal.

Để backtest phải formalize pivot detection, tolerance và horizon; nếu không hindsight bias rất lớn.

## 9. MACD

MACD thường dựa trên difference giữa hai EMAs:

```text
MACD = EMA_fast - EMA_slow
Signal = EMA(MACD)
Histogram = MACD - Signal
```

Vì vậy MACD không phải source dữ liệu mới. Nó là combination của smoothed trend/momentum.

Dùng MACD cùng nhiều moving-average signals có thể tạo **redundant confirmation**.

## 10. Stochastic oscillator

Stochastic so close hiện tại với recent high-low range:

```text
%K = (Close - LowestLow_N) / (HighestHigh_N - LowestLow_N) × 100
```

Nó trả lời:

> Close hiện nằm ở đâu trong range N periods gần nhất?

Không phải:

> Market đã quá mua nên chắc chắn đảo chiều.

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

Context quyết định interpretation. Band không tự phát lệnh sell.

## 12. ATR

ATR đo range magnitude chứ không hướng.

Ứng dụng hợp lý:

- volatility-normalized stop;
- position sizing;
- regime classification;
- filter periods quá yên hoặc quá biến động.

ATR multiplier như `2×ATR` không có universal optimality. Cần liên hệ với strategy horizon và distribution.

## 13. ADX

Average Directional Index được thiết kế để đo trend strength từ directional movement, không trực tiếp nói trend direction.

Một ADX cao có thể xảy ra trong downtrend lẫn uptrend.

Nếu dùng ADX như “buy indicator” mà bỏ qua construction, interpretation đã sai từ đầu.

## 14. Donchian channel

```text
Upper = highest high over N periods
Lower = lowest low over N periods
```

Đây là transformation rất trực tiếp của recent extremes và thường dùng trong breakout/trend systems.

Nó cho thấy đôi khi “indicator” chỉ là một cách formalize price-action rule.

## 15. Z-score

Nếu có reference mean `μ` và standard deviation `σ`:

```text
Z = (X - μ) / σ
```

Z-score nói observation cách mean bao nhiêu standard deviations theo model/window.

Nhưng nếu distribution non-stationary hoặc fat-tailed, `Z=3` không nên được đọc máy móc theo normal distribution probability.

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

## 17. Volume trong spot FX cần cẩn thận

OTC FX không có một centralized tape toàn cầu. Retail chart thường có:

- tick volume;
- broker-specific transaction volume;
- venue-specific volume.

Đừng gọi đó là “global Forex volume”.

Exchange-traded currency futures có centralized venue volume của exchange đó, nhưng cũng không đại diện toàn bộ OTC market.

## 18. Tick volume

Tick volume thường đếm số lần price update trong period. Nó có thể correlate với activity ở một data source nhưng không trực tiếp bằng notional traded globally.

Nếu strategy dùng tick volume, phải giữ data source nhất quán và test out-of-sample.

## 19. VWAP trong Forex

VWAP cần price và actual volume của venue/dataset:

```text
VWAP = Σ(P_i × V_i) / ΣV_i
```

Trong decentralized spot FX, “VWAP” trên retail source có thể không mang cùng meaning như VWAP của centralized exchange equity/futures data.

Phải biết `V_i` thực sự là gì.

## 20. Indicator stacking và multicollinearity

Ví dụ dùng cùng lúc:

```text
MA crossover
MACD
RSI momentum
ROC
```

có thể trông như bốn confirmations nhưng tất cả đều phần lớn xuất phát từ recent price changes.

Trong model, các features có thể highly correlated.

Cần hỏi:

```text
Does each feature add incremental information?
```

không phải:

```text
How many indicators agree?
```

## 21. Parameter sensitivity

Nếu strategy chỉ profitable với:

```text
RSI length = 14
threshold = 31.7
MA = 47
```

nhưng thất bại khi parameters thay đổi nhẹ, đó là dấu hiệu fragility.

Robust edge thường có vùng parameter tương đối ổn định thay vì một spike tối ưu sắc nhọn.

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

Vì vậy indicator research không thể tách khỏi multiple testing và walk-forward validation.

## 23. Indicator lag và decision latency

Indicator dùng close của bar chỉ biết chính xác sau bar close.

Nếu backtest entry ở đúng close đó mà không modeling khả năng thực thi, có thể tạo optimistic fill.

Pipeline đúng:

```text
bar closes
→ indicator becomes known
→ signal computed
→ order sent
→ next executable price
```

trừ khi system thật sự có intrabar data/rule.

## 24. Repainting

Một số indicators/visual tools thay đổi historical display khi future data xuất hiện hoặc current bar chưa đóng.

Research phải phân biệt:

```text
value known at time t
versus
final value shown later
```

Nếu indicator repaint, screenshot historical đẹp có thể không phản ánh signal live.

## 25. Centered moving averages và look-ahead

Một filter dùng observations trước và sau `t` có thể tạo smooth line tuyệt đẹp nhưng không usable live vì future data chưa tồn tại.

Bất kỳ transformation nào dùng future samples đều phải được coi là retrospective analysis, không phải trading signal tại t.

## 26. Indicator as feature, not rule

Trong quantitative model, indicator có thể là feature:

```text
trend score
volatility percentile
RSI percentile
carry
rate differential
session
```

Model sau đó estimate conditional outcome.

Điều này thường tốt hơn việc gán mystical meaning cho một threshold duy nhất.

## 27. Binary threshold làm mất thông tin

Ví dụ:

```text
RSI < 30 = BUY
RSI >= 30 = NO BUY
```

biến continuous variable thành binary rule.

Có thể nghiên cứu outcome theo bins:

```text
0–10
10–20
20–30
...
```

để xem relation có monotonic hay không.

## 28. Conditional indicator analysis

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

## 29. Indicator và causal mechanism

Pure technical signal không nhất thiết cần fundamental causality mạnh để có predictive value, nhưng một plausible mechanism giúp giảm nguy cơ data-mined coincidence.

Ví dụ trend persistence có thể liên hệ:

- gradual information diffusion;
- institutional execution over time;
- behavioral underreaction;
- policy divergence.

Mean reversion có thể liên hệ:

- temporary liquidity imbalance;
- inventory correction;
- overreaction.

Mechanism là hypothesis, vẫn cần data test.

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

Indicator chỉ là một component trong toàn research pipeline.

## 32. Checklist

Bạn cần tự giải thích được:

1. SMA/EMA trade-off giữa smoothing và lag.
2. RSI thực sự được tính từ gì.
3. MACD vì sao phần lớn là moving-average transformation.
4. ATR khác directional indicator như thế nào.
5. Vì sao spot FX volume cần ghi rõ source.
6. Vì sao nhiều indicators có thể không phải nhiều independent confirmations.
7. Repainting/look-ahead xảy ra thế nào.
8. Vì sao parameter stability quan trọng hơn single best setting.
9. Indicator phải được đánh giá sau transaction costs.

## Đọc tiếp

→ [08 — Fundamental and event-driven FX analysis](./08_FUNDAMENTAL_AND_EVENT_DRIVEN_FX_ANALYSIS.md)

## Internal links

- [06 — Price action and regimes](./06_PRICE_ACTION_TREND_RANGE_AND_VOLATILITY_REGIMES.md)
- [04 — Macro drivers, rates, carry and sessions](./04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)
- [Systematic risk, backtest and execution](../02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md)
- [Strategy research and robustness](../04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md)
