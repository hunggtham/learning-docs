# Bản đồ tổng quan Trading, Forex và quản trị rủi ro

> File này là bản đồ học tập cho toàn bộ `05_trading_derivatives/`. Mục tiêu không phải thay thế các chapter chuyên sâu, mà giúp người đọc hiểu trading là một hệ thống gồm **tín hiệu → quy mô vị thế → thực thi → chi phí → quản trị danh mục → review**.

Trading không phải tập hợp các pattern vào lệnh. Một chiến lược chỉ có ý nghĩa khi lợi thế kỳ vọng còn tồn tại sau spread, slippage, financing, drawdown và lỗi vận hành.

## 1. Mental model cốt lõi

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
- execution quan trọng hơn;
- số lượng giao dịch nhiều hơn.

Không có timeframe “tốt nhất”; nó phải phù hợp strategy, cost và thời gian của trader.

## 4. Trend, range và regime

Một thị trường có thể ở:

```text
Trend
Range
High Volatility
Low Volatility
Event-Driven State
```

Một setup tốt trong trend có thể hoạt động kém trong range.

## 5. Market structure

Market structure thường mô tả chuỗi swing high, swing low và cách giá phản ứng quanh vùng có order flow lớn.

Các thuật ngữ như break of structure hoặc change of character chỉ nên dùng như cách mô tả dữ liệu, không phải quy luật tất định.

## 6. Support và resistance

Support/resistance là vùng giá nơi hành vi mua/bán từng thay đổi đáng kể.

Nên nghĩ theo vùng xác suất, không phải một đường chính xác tuyệt đối.

## 7. Breakout

Breakout chỉ có edge nếu sau chi phí, false break và slippage, outcome phân phối vẫn có expectancy dương.

## 8. Pullback

Pullback strategy thường đánh cược rằng trend chính còn tiếp tục sau điều chỉnh tạm thời.

Điểm quan trọng là định nghĩa trend, invalidation và risk/reward rõ ràng.

## 9. Mean reversion

Mean reversion giả định giá có xu hướng quay về một mức tham chiếu sau khi đi quá xa.

Nó có thể thất bại nặng khi thị trường chuyển từ range sang trend.

## 10. Volume và liquidity

Volume cao không luôn đồng nghĩa liquidity tốt. Cần nhìn thêm:

- spread;
- depth;
- market impact;
- thời điểm trong ngày.

## 11. Volatility

Volatility quyết định:

- stop distance hợp lý;
- position size;
- expected move;
- margin risk;
- option pricing.

Cùng một strategy không nên dùng size giống nhau trong mọi volatility regime.

## 12. Indicator

MA, RSI, MACD, ATR hay Bollinger Bands đều là biến đổi của price/volume.

Indicator hữu ích khi nó phục vụ rule rõ ràng, không phải vì thêm nhiều indicator làm hệ thống “chắc chắn” hơn.

## 13. SMC / ICT

Các khái niệm như liquidity sweep, order block, fair value gap có thể dùng như ngôn ngữ mô tả price action.

Nhưng phải chuyển chúng thành rule kiểm chứng được nếu muốn backtest.

## 14. Multi-timeframe

Timeframe lớn có thể cung cấp context; timeframe nhỏ dùng cho timing.

Tuy nhiên thêm quá nhiều timeframe dễ tạo hindsight narrative.

## 15. Forex là thị trường tương đối

Một cặp tiền luôn so hai nền kinh tế.

```text
EUR/USD
= giá EUR theo USD
```

Phân tích cần nhìn relative rates, relative growth, risk sentiment và flow.

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

Margin không phải maximum loss.

## 19. Equity, free margin và margin level

```text
Equity = Balance + Floating P/L
```

```text
Margin Level
= Equity / Used Margin × 100%
```

Nếu equity giảm quá mức, broker có thể margin call hoặc stop-out theo rules riêng.

## 20. Position sizing

Quy mô vị thế phải bắt đầu từ mức lỗ chấp nhận được.

```text
Position Size
≈ Allowed Loss / Loss Per Unit at Invalidation
```

Không nên bắt đầu từ “broker cho leverage bao nhiêu”.

## 21. Stop-loss

Stop là một execution instruction, không phải guarantee giá thoát.

Trong gap hoặc event lớn, fill có thể xa trigger.

## 22. R-multiple

`R` là lượng rủi ro ban đầu.

Ví dụ risk 100 USD:

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

Win rate cao không bảo đảm có edge.

## 24. Risk of ruin

Risk of ruin tăng khi:

- risk/trade lớn;
- edge nhỏ;
- drawdown kéo dài;
- correlation giữa trade cao.

Survival quan trọng hơn tối đa hóa short-term return.

## 25. Sessions

Forex có đặc điểm khác nhau theo Asia, London và New York session.

Liquidity và volatility thường thay đổi quanh overlap và data release.

## 26. News event

CPI, NFP, central-bank decision hoặc geopolitical shock có thể làm:

- spread widen;
- slippage tăng;
- stop gap;
- margin thay đổi.

Event trading đòi hỏi execution plan trước release.

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

Trước expiry, giá option còn phụ thuộc volatility, time, rates và Greeks.

## 30. CFD

CFD thường là bilateral contract với broker.

Cần kiểm tra:

- legal entity;
- financing cost;
- spread;
- execution model;
- stop-out;
- jurisdiction.

## 31. Backtest

Backtest phải cố tái tạo thông tin và execution có thể có thật tại thời điểm quá khứ.

Sai lầm phổ biến:

- look-ahead bias;
- survivorship bias;
- data snooping;
- bỏ transaction cost;
- bỏ slippage.

## 32. Forward test

Sau backtest nên có out-of-sample hoặc forward test trước khi dùng capital đáng kể.

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

Tâm lý không thể sửa một strategy không có edge.

Nhưng một strategy có edge vẫn có thể thất bại nếu trader:

- tăng size sau loss;
- bỏ rule;
- revenge trade;
- stop quá sớm;
- overtrade.

## 35. Portfolio heat

Nhiều trade riêng lẻ có thể cùng chịu một factor.

Ví dụ long EUR/USD, long GBP/USD và long gold có thể cùng là short-USD exposure.

Cần nhìn tổng risk, không chỉ risk/trade.

## 36. Kelly

Kelly criterion cho sizing tối ưu theo growth trong điều kiện giả định hoàn hảo.

Thực tế thường dùng fractional Kelly vì:

- edge estimate không chắc;
- distribution có fat tail;
- drawdown tâm lý lớn.

## 37. Monte Carlo

Monte Carlo giúp kiểm tra nhiều thứ tự trade khác nhau để thấy drawdown distribution và risk of ruin.

Nó không sửa được sample kém chất lượng.

## 38. MAE và MFE

**Maximum Adverse Excursion (MAE)** đo mức đi ngược lớn nhất trước khi trade đóng.

**Maximum Favorable Excursion (MFE)** đo mức có lợi lớn nhất.

Hai metric giúp cải thiện stop và exit rule.

## 39. Profit factor

```text
Profit Factor
= Gross Profit / Gross Loss
```

Cần đọc cùng sample size, drawdown và cost.

## 40. Sharpe / Sortino / Calmar

Các ratio này mô tả return so với risk theo góc khác nhau nhưng không thay thế:

- tail risk;
- liquidity;
- leverage;
- operational risk.

## 41. Regime dependence

Một strategy có thể kiếm tiền chỉ trong một regime.

Cần biết edge phụ thuộc:

- trend;
- volatility;
- carry;
- liquidity;
- macro environment.

## 42. Broker safety

Trước khi quan tâm setup, cần hiểu broker legal entity, custody/margin rules và khả năng rút tiền.

## 43. Từ master map tới chapter chuyên sâu

Nếu mục tiêu chính là **Forex**, đi vào learning path riêng:

- [forex/README.md](./forex/README.md): từ market structure, P/L, leverage, macro và execution tới price action, strategy research, backtesting, portfolio risk, microstructure, FX options và Korea/Vietnam context.

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

Leverage không tạo lợi thế. Pattern không thay thế expectancy. Và một strategy chỉ đáng dùng khi nó sống sót sau chi phí, stress và sai số thực tế.
