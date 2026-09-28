# Bản đồ tổng quan Trading, Forex và quản trị rủi ro

> Tệp (file / 파일) này là bản đồ học tập cho toàn bộ `05_trading_derivatives/`. Mục tiêu không phải thay thế các chapter chuyên sâu, mà giúp người đọc hiểu trading là một hệ thống gồm **tín hiệu → quy mô vị thế → thực thi → chi phí → quản trị danh mục → rà soát (review / 검토)**.

Trading không phải tập hợp các mẫu (pattern / 패턴) vào lệnh. Một chiến lược chỉ có ý nghĩa khi lợi thế kỳ vọng còn tồn tại sau spread, slippage, financing, drawdown và lỗi vận hành.

## 1. Mô hình tư duy (mental model / 사고 모델) cốt lõi

```text
Hypothesis
→ Signal
→ Entry / Exit Rule
→ Position Size
→ Execution
→ Cost
→ P/L Distribution
→ Portfolio Risk
→ Review
```

Nếu thiếu một mắt xích, hệ thống chưa hoàn chỉnh.

## 2. Chart chỉ là biểu diễn dữ liệu giá

Candlestick, bar hay line chart chỉ là cách hiển thị:

- open;
- high;
- low;
- close;
- volume nếu có.

Chart không tự tạo edge. Edge phải đến từ một quan hệ có khả năng lặp lại và có lý do kinh tế hoặc hành vi hợp lý.

## 3. Timeframe

Timeframe càng nhỏ:

- noise càng lớn;
- spread/slippage chiếm tỷ trọng cao hơn;
- thực thi (execution / 실행) quan trọng hơn;
- số lượng giao dịch nhiều hơn.

Không có timeframe “tốt nhất”; nó phải phù hợp chiến lược (strategy / 전략), chi phí (cost / 비용) và thời gian của trader.

## 4. Trend, phạm vi (range / 범위) và regime

Một thị trường có thể ở:

```text
Trend
Range
High Volatility
Low Volatility
Event-Driven State
```

Một setup tốt trong trend có thể hoạt động kém trong phạm vi (range / 범위).

## 5. Thị trường (market / 시장) cấu trúc (structure / 구조)

Thị trường (market / 시장) cấu trúc (structure / 구조) thường mô tả chuỗi swing high, swing low và cách giá phản ứng quanh vùng có thứ tự (order / 순서) luồng (flow / 흐름) lớn.

Các thuật ngữ như break of cấu trúc (structure / 구조) hoặc thay đổi (change / 변경) of character chỉ nên dùng như cách mô tả dữ liệu, không phải quy luật tất định.

## 6. Hỗ trợ (support / 지원) và resistance

Hỗ trợ (support / 지원)/resistance là vùng giá nơi hành vi mua/bán từng thay đổi đáng kể.

Nên nghĩ theo vùng xác suất, không phải một đường chính xác tuyệt đối.

## 7. Breakout

Breakout chỉ có edge nếu sau chi phí, false break và slippage, kết quả (outcome / 결과) phân phối vẫn có expectancy dương.

## 8. Pullback

Pullback chiến lược (strategy / 전략) thường đánh cược rằng trend chính còn tiếp tục sau điều chỉnh tạm thời.

Điểm quan trọng là định nghĩa trend, vô hiệu hóa (invalidation / 무효화) và rủi ro (risk / 위험)/reward rõ ràng.

## 9. Mean reversion

Mean reversion giả định giá có xu hướng quay về một mức tham chiếu sau khi đi quá xa.

Nó có thể thất bại nặng khi thị trường chuyển từ phạm vi (range / 범위) sang trend.

## 10. Volume và liquidity

Volume cao không luôn đồng nghĩa liquidity tốt. Cần nhìn thêm:

- spread;
- độ sâu (depth / 깊이);
- thị trường (market / 시장) impact;
- thời điểm trong ngày.

## 11. Volatility

Volatility quyết định:

- stop distance hợp lý;
- position kích thước (size / 크기);
- expected move;
- margin rủi ro (risk / 위험);
- option pricing.

Cùng một chiến lược (strategy / 전략) không nên dùng kích thước (size / 크기) giống nhau trong mọi volatility regime.

## 12. Indicator

MA, RSI, MACD, ATR hay Bollinger Bands đều là biến đổi của price/volume.

Indicator hữu ích khi nó phục vụ quy tắc (rule / 규칙) rõ ràng, không phải vì thêm nhiều indicator làm hệ thống “chắc chắn” hơn.

## 13. SMC / ICT

Các khái niệm như liquidity sweep, thứ tự (order / 순서) khối (block / 블록), fair giá trị (value / 값) gap có thể dùng như ngôn ngữ mô tả price hành động (action / 동작).

Nhưng phải chuyển chúng thành quy tắc (rule / 규칙) kiểm chứng được nếu muốn backtest.

## 14. Multi-timeframe

Timeframe lớn có thể cung cấp ngữ cảnh (context / 맥락); timeframe nhỏ dùng cho timing.

Tuy nhiên thêm quá nhiều timeframe dễ tạo hindsight narrative.

## 15. Forex là thị trường tương đối

Một cặp tiền luôn so hai nền kinh tế.

```text
EUR/USD
= giá EUR theo USD
```

Phân tích cần nhìn relative rates, relative growth, rủi ro (risk / 위험) sentiment và luồng (flow / 흐름).

## 16. Pip và lot

Pip là đơn vị biến động giá quy ước. Lot là quy mô hợp đồng.

Trước khi giao dịch phải biết:

```text
Contract Size
Pip Value
Quote Currency
Account Currency
```

## 17. Leverage

Đòn bẩy (leverage) cho phép kiểm soát notional lớn bằng capital nhỏ hơn.

Leverage không tạo edge. Nó chỉ phóng đại:

```text
P/L
Drawdown
Margin Risk
Risk of Ruin
```

## 18. Margin

Margin là collateral broker yêu cầu để giữ position.

```text
Required Margin
≈ Notional / Leverage
```

Margin không phải maximum mất mát (loss / 손실).

## 19. Equity, free margin và margin mức (level / 수준)

```text
Equity = Balance + Floating P/L
```

```text
Margin Level
= Equity / Used Margin × 100%
```

Nếu equity giảm quá mức, broker có thể margin lời gọi (call / 호출) hoặc stop-out theo rules riêng.

## 20. Position sizing

Quy mô vị thế phải bắt đầu từ mức lỗ chấp nhận được.

```text
Position Size
≈ Allowed Loss / Loss Per Unit at Invalidation
```

Không nên bắt đầu từ “broker cho leverage bao nhiêu”.

## 21. Stop-loss

Stop là một thực thi (execution / 실행) instruction, không phải guarantee giá thoát.

Trong gap hoặc sự kiện (event / 이벤트) lớn, fill có thể xa trigger.

## 22. R-multiple

`R` là lượng rủi ro ban đầu.

Ví dụ rủi ro (risk / 위험) 100 USD:

```text
-1R = -100 USD
+2R = +200 USD
```

R giúp so trade khác nhau bằng cùng đơn vị rủi ro.

## 23. Expectancy

```text
Expectancy
= Win Rate × Average Win
- Loss Rate × Average Loss
```

Win tỷ lệ (rate / 비율) cao không bảo đảm có edge.

## 24. Rủi ro (risk / 위험) of ruin

Rủi ro (risk / 위험) of ruin tăng khi:

- rủi ro (risk / 위험)/trade lớn;
- edge nhỏ;
- drawdown kéo dài;
- correlation giữa trade cao.

Survival quan trọng hơn tối đa hóa short-term return.

## 25. Sessions

Forex có đặc điểm khác nhau theo Asia, London và New York session.

Liquidity và volatility thường thay đổi quanh overlap và dữ liệu (data / 데이터) bản phát hành (release / 릴리스).

## 26. News sự kiện (event / 이벤트)

CPI, NFP, central-bank quyết định (decision / 결정) hoặc geopolitical shock có thể làm:

- spread widen;
- slippage tăng;
- stop gap;
- margin thay đổi.

Sự kiện (event / 이벤트) trading đòi hỏi thực thi (execution / 실행) plan trước bản phát hành (release / 릴리스).

## 27. XAUUSD

Gold chịu ảnh hưởng của:

- real yield;
- USD;
- central-bank demand;
- geopolitics;
- inflation regime;
- positioning.

Không dùng quy tắc đơn giản “inflation tăng → gold tăng”.

## 28. Futures

Futures là hợp đồng chuẩn hóa trên exchange.

Cần hiểu:

- multiplier;
- tick;
- expiry;
- margin;
- settlement;
- basis;
- roll.

## 29. Options

Option tạo payoff phi tuyến.

```text
Call = max(S-K, 0)
Put  = max(K-S, 0)
```

Trước expiry, giá option còn phụ thuộc volatility, thời gian (time / 시간), rates và Greeks.

## 30. CFD

CFD thường là bilateral đặc tả hợp đồng (contract / 계약) với broker.

Cần kiểm tra:

- legal thực thể (entity / 엔터티);
- financing chi phí (cost / 비용);
- spread;
- mô hình thực thi (execution model / 실행 모델);
- stop-out;
- jurisdiction.

## 31. Backtest

Backtest phải cố tái tạo thông tin và thực thi (execution / 실행) có thể có thật tại thời điểm quá khứ.

Sai lầm phổ biến:

- look-ahead độ lệch (bias / 편향);
- survivorship độ lệch (bias / 편향);
- dữ liệu (data / 데이터) snooping;
- bỏ giao dịch (transaction / 트랜잭션) chi phí (cost / 비용);
- bỏ slippage.

## 32. Forward kiểm thử (test / 테스트)

Sau backtest nên có out-of-sample hoặc forward kiểm thử (test / 테스트) trước khi dùng capital đáng kể.

## 33. Trading journal

Journal nên ghi:

```text
Setup
Reason
Risk
Expected Outcome
Actual Execution
MAE / MFE
Result
Rule Violation
Lesson
```

## 34. Psychology

Tâm lý không thể sửa một chiến lược (strategy / 전략) không có edge.

Nhưng một chiến lược (strategy / 전략) có edge vẫn có thể thất bại nếu trader:

- tăng kích thước (size / 크기) sau mất mát (loss / 손실);
- bỏ quy tắc (rule / 규칙);
- revenge trade;
- stop quá sớm;
- overtrade.

## 35. Portfolio heat

Nhiều trade riêng lẻ có thể cùng chịu một factor.

Ví dụ long EUR/USD, long GBP/USD và long gold có thể cùng là short-USD exposure.

Cần nhìn tổng rủi ro (risk / 위험), không chỉ rủi ro (risk / 위험)/trade.

## 36. Kelly

Kelly criterion cho sizing tối ưu theo growth trong điều kiện giả định hoàn hảo.

Thực tế thường dùng fractional Kelly vì:

- edge estimate không chắc;
- phân phối (distribution / 분포) có fat tail;
- drawdown tâm lý lớn.

## 37. Monte Carlo

Monte Carlo giúp kiểm tra nhiều thứ tự trade khác nhau để thấy drawdown phân phối (distribution / 분포) và rủi ro (risk / 위험) of ruin.

Nó không sửa được mẫu (sample / 표본) kém chất lượng.

## 38. MAE và MFE

**Maximum Adverse Excursion (MAE)** đo mức đi ngược lớn nhất trước khi trade đóng.

**Maximum Favorable Excursion (MFE)** đo mức có lợi lớn nhất.

Hai chỉ số (metric / 지표) giúp cải thiện stop và exit quy tắc (rule / 규칙).

## 39. Profit factor

```text
Profit Factor
= Gross Profit / Gross Loss
```

Cần đọc cùng cỡ mẫu (sample size / 표본 크기), drawdown và chi phí (cost / 비용).

## 40. Sharpe / Sortino / Calmar

Các ratio này mô tả return so với rủi ro (risk / 위험) theo góc khác nhau nhưng không thay thế:

- tail rủi ro (risk / 위험);
- liquidity;
- leverage;
- operational rủi ro (risk / 위험).

## 41. Regime dependence

Một chiến lược (strategy / 전략) có thể kiếm tiền chỉ trong một regime.

Cần biết edge phụ thuộc:

- trend;
- volatility;
- carry;
- liquidity;
- macro môi trường (environment / 환경).

## 42. Broker an toàn (safety / 안전)

Trước khi quan tâm setup, cần hiểu broker legal thực thể (entity / 엔터티), custody/margin rules và khả năng rút tiền.

## 43. Từ master map tới chapter chuyên sâu

Nếu mục tiêu chính là **Forex**, đi vào lộ trình học (learning path / 학습 경로) riêng:

- [forex/README.md](./forex/README.md): từ thị trường (market / 시장) cấu trúc (structure / 구조), P/L, leverage, macro và thực thi (execution / 실행) tới price hành động (action / 동작), chiến lược (strategy / 전략) research, backtesting, portfolio rủi ro (risk / 위험), microstructure, FX options và Korea/Vietnam ngữ cảnh (context / 맥락).

Các chapter Trading & Derivatives dùng chung:

- [01_DERIVATIVES_FUTURES_OPTIONS_CFD.md](./01_DERIVATIVES_FUTURES_OPTIONS_CFD.md): hợp đồng phái sinh;
- [02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md](./02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md): nghiên cứu hệ thống;
- [03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md](./03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md): thực thi và microstructure;
- [04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md](./04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md): robustness và portfolio of strategies;
- [05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md](./05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md): options và volatility.

## Kết luận

Trading nên được xem là một hệ thống xác suất:

```text
Edge
× Position Sizing
× Execution Quality
× Risk Control
× Discipline
```

Leverage không tạo lợi thế. Mẫu (pattern / 패턴) không thay thế expectancy. Và một chiến lược (strategy / 전략) chỉ đáng dùng khi nó sống sót sau chi phí, stress và sai số thực tế.
