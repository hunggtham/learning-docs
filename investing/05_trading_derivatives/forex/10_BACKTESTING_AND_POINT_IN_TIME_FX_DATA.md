# 10 — Backtesting và point-in-time FX data

Backtest không phải máy chứng minh strategy có edge. Nó là **thí nghiệm lịch sử có giả định**. Nếu dữ liệu, timestamp, execution hoặc selection process sai, kết quả có thể chính xác về code nhưng sai về kinh tế.

Mental model:

```text
Hypothesis
→ point-in-time data
→ signal known at t
→ realistic execution after t
→ costs / financing
→ portfolio accounting
→ out-of-sample validation
→ uncertainty estimate
```

## 1. Câu hỏi đầu tiên: strategy biết gì tại thời điểm t?

Mọi feature phải trả lời:

```text
Was this exact value observable then?
```

Nếu câu trả lời là không, backtest có look-ahead.

Ví dụ:

- revised CPI final value chưa tồn tại lúc release đầu tiên;
- swing high cần future bars để confirm;
- end-of-day high/low chưa biết giữa ngày;
- historical constituent list hôm nay không đại diện past universe.

## 2. Point-in-time data

**Point-in-time** nghĩa là dataset tái tạo thông tin như nó được biết tại thời điểm lịch sử đó.

Đặc biệt quan trọng với:

- macro releases;
- central-bank expectations;
- analyst forecasts;
- index/universe membership;
- financing rates;
- contract specifications.

Final cleaned database thường tốt cho economic history nhưng có thể không hợp live-strategy simulation.

## 3. Vintage data

Macro data thường có revisions.

Research event strategy cần lưu:

```text
release timestamp
first-release value
consensus known before release
later revisions separately
```

Không được dùng final revised number để tính surprise quá khứ nếu trader lúc đó chưa biết.

## 4. Timezone

FX là 24-hour market nên timezone bug cực nguy hiểm.

Pipeline nên dùng:

```text
UTC internally
+
source timezone metadata
+
explicit local-session conversion
```

Daylight-saving phải được xử lý bằng timezone database, không hard-code offset quanh năm.

## 5. Bar timestamp convention

Một bar timestamp có thể đại diện:

- bar open time;
- bar close time;
- exchange/vendor convention.

Nếu không hiểu convention, signal có thể bị shifted một bar.

Ví dụ daily FX bars giữa vendors có thể dùng different session cutoff, tạo OHLC khác nhau.

## 6. Bid, ask hay mid?

Nếu strategy giao dịch thực tế ở bid/ask nhưng backtest dùng mid-price:

```text
entry too good
exit too good
spread cost missing
```

Tối thiểu phải apply spread model. Với short-horizon strategy, historical bid/ask data càng quan trọng.

## 7. OHLC limitation

Một bar chỉ cho:

```text
Open
High
Low
Close
```

Nó không cho intrabar sequence.

Nếu cùng một bar vừa chạm stop vừa chạm target, không biết cái nào xảy ra trước nếu không có finer data.

Conservative rule hoặc lower-resolution data cần được dùng.

## 8. Tick data không tự động hoàn hảo

Tick datasets có thể có:

- bad ticks;
- duplicated timestamps;
- stale quotes;
- different liquidity sources;
- missing periods;
- clock issues.

Higher resolution tăng data-quality burden.

## 9. Broker-specific data

Retail strategy deployed tại broker A nhưng backtest trên feed B có basis mismatch:

- spread khác;
- Sunday candles khác;
- rollover khác;
- high/low khác;
- stop trigger khác.

Không cần feed giống tuyệt đối, nhưng sensitivity cần được hiểu.

## 10. Universe selection

Nếu chỉ backtest các major pairs hiện nay, có thể bỏ qua currencies/instruments từng tồn tại hoặc thay đổi regime.

Với FX majors, survivorship bias ít trực diện hơn equities nhưng vẫn có:

- currency regime changes;
- pegs/breaks;
- capital controls;
- redenomination;
- liquidity changes.

## 11. Structural breaks

Examples conceptual:

```text
fixed/managed regime → float
capital controls change
negative-rate era begins/ends
market microstructure changes
```

Full-history average có thể trộn incompatible states.

## 12. Signal timestamp và fill timestamp

Nếu signal dùng closing price tại `t`:

```text
Signal becomes known after/at close
```

Fill không nên magically xảy ra trước signal.

Reasonable execution:

```text
next executable quote
or
explicit closing-auction/market-on-close mechanism if product supports it
```

Retail OTC FX thường không có centralized closing auction như equities.

## 13. Latency

Intraday systems cần model:

```text
data arrival
→ calculation
→ order transmission
→ broker/venue processing
→ fill
```

Milliseconds có thể irrelevant với daily strategy nhưng decisive với news scalping.

## 14. Spread model

Levels:

```text
Level 1: fixed conservative spread
Level 2: pair + session spread
Level 3: historical bid/ask spread
Level 4: regime/event-aware executable quotes
```

Model complexity phải tương xứng data quality.

## 15. Slippage model

Một simple approach:

```text
slippage = fixed fraction of spread/ATR
```

better approach có thể condition on:

- volatility;
- event windows;
- order size;
- liquidity/session.

Nhưng slippage model cũng có thể overfit.

Sensitivity test quan trọng hơn false precision.

## 16. Financing / rollover

Swing/carry strategies phải include financing history.

Không được apply current broker swap rate cho 10 năm lịch sử.

Nếu historical retail financing không có, cần dùng transparent proxy + conservative markup và document limitation.

## 17. Forward-based research

Academic FX carry research thường dùng spot + forward rates. Nếu implementation thực tế dùng CFDs/rolling spot, bridge từ forward return sang retail realized P/L phải được giải thích.

Instrument mismatch là model risk.

## 18. Position sizing trong backtest

Fixed lot làm account risk thay đổi theo volatility/equity.

Nếu live plan dùng volatility scaling hoặc percent risk, backtest phải implement cùng rule.

Không nên backtest signal fixed-notional rồi report result như fixed-risk strategy.

## 19. Margin accounting

Leveraged backtest phải track:

```text
cash/balance
equity
notional
used margin
financing
realized/unrealized P/L
```

Nếu strategy có thể vi phạm margin requirement historically, không thể giả định position vẫn tồn tại đến final exit.

## 20. Stop-loss simulation

Stop backtest cần xác định:

- trigger price side;
- gap behavior;
- spread widening;
- intrabar path assumption.

Một exact stop fill mọi lần là optimistic.

## 21. Limit-order fill bias

Price touching limit không guarantee fill. Queue position và liquidity matter.

Backtest kiểu:

```text
Low <= buy limit → filled
```

có thể overestimate fills, đặc biệt short-horizon.

Conservative assumptions hoặc actual order-book/quote data cần thiết nếu edge phụ thuộc passive fills.

## 22. Look-ahead bias

Common forms:

- using future-confirmed pivots;
- future volatility estimate;
- revised macro data;
- optimization over full sample rồi report same sample;
- normalizing bằng full-sample mean/std.

Preprocessing cũng phải fit only on training history.

## 23. Data snooping

Nếu thử hàng nghìn variations, best result likely upward-biased.

Research log nên ghi:

```text
all hypotheses tested
all parameter variants
all rejected models
```

Không chỉ final winner.

## 24. In-sample, validation, test

Chronological split phù hợp time series hơn random shuffle.

Ví dụ conceptual:

```text
Train → choose broad model
Validation → tune limited parameters
Test → final untouched evaluation
```

Sau khi xem test result và thay model, test không còn untouched nữa.

## 25. Walk-forward

Walk-forward mô phỏng repeated research/deployment:

```text
train window
→ test next period
→ roll forward
→ retrain if allowed
→ repeat
```

Nó giúp đánh giá parameter stability và regime adaptation.

## 26. Purging và embargo

Khi labels overlap in time, train/test samples có thể leak information.

Purging/embargo tách observations quanh boundary để giảm overlap leakage.

Đặc biệt relevant với ML/horizon returns.

## 27. Cross-validation không được random máy móc

Random k-fold phá chronology và có thể train on future relative to test.

Time-series CV phải preserve ordering và overlap structure.

## 28. Parameter surface

Đừng chỉ report best parameter.

Plot/evaluate neighborhood:

```text
lookback 20, 30, 40, 50, 60
threshold range
holding-period range
```

Nếu chỉ một point profitable, edge fragile.

## 29. Multiple testing

Nếu test nhiều hypotheses, threshold “significant” thông thường có thể tạo false discoveries.

Cần hiểu:

- family-wise error;
- false discovery;
- selection bias;
- data-mined Sharpe.

Không nhất thiết phải dùng một test duy nhất, nhưng phải account search process.

## 30. Sample size

100 trades không luôn là 100 independent observations.

Nếu trades cluster cùng regime/day/currency factor, **effective sample size** thấp hơn.

Autocorrelation và overlap làm confidence interval rộng hơn tưởng tượng.

## 31. Bootstrap

Bootstrap có thể estimate uncertainty bằng resampling, nhưng time series cần block/bootstrap methods nếu observations dependent.

Naive iid shuffle có thể phá dependence structure.

## 32. Monte Carlo

Monte Carlo có thể stress:

- trade sequence;
- slippage variation;
- parameter uncertainty;
- regime frequencies.

Nó không cứu dataset biased hoặc model misspecified.

## 33. Metrics

Không chỉ Sharpe.

Theo dõi:

```text
CAGR / total return
volatility
max drawdown
Calmar
Sharpe / Sortino
profit factor
expectancy
skew / tail loss
turnover
exposure
average holding period
cost share
```

## 34. Drawdown uncertainty

Observed max drawdown chỉ là một path. Future path có thể worse.

Monte Carlo/bootstrap giúp estimate drawdown distribution nhưng vẫn phụ thuộc assumptions.

## 35. Cost sensitivity

Report ít nhất:

```text
Base cost
1.5× cost
2× cost
stress-event cost
```

Strategy chết ngay khi spread tăng nhẹ là fragile.

## 36. Parameter sensitivity

Tương tự:

```text
Base parameters
nearby values
slower/faster variants
```

Robustness quan trọng hơn optimization peak.

## 37. Regime attribution

Break performance by:

- volatility regime;
- trend/range;
- policy divergence;
- crisis/normal;
- session;
- pair;
- decade/subperiod.

Một aggregate Sharpe có thể che strategy kiếm toàn bộ profit trong một giai đoạn ngắn.

## 38. Pair contribution

Nếu multi-pair strategy, report contribution per pair và per underlying currency factor.

Có thể “diversified 10 pairs” nhưng 80% P/L đến từ USD trend trong một era.

## 39. Carry vs spot attribution

Tách:

```text
Spot P/L
Carry
Costs
```

để biết signal thực sự kiếm tiền từ đâu.

## 40. Backtest-to-live gap

Paper/live differences:

- latency;
- spread;
- rejected orders;
- platform outages;
- financing;
- emotional/manual overrides;
- data revisions;
- broker contract changes.

Forward test là phase bắt buộc trước scaling material capital.

## 41. Paper trading

Paper trading test:

- signal generation;
- operational pipeline;
- position accounting.

Nhưng không reproduce fully:

- real slippage;
- liquidity;
- psychological pressure.

## 42. Small-live forward test

Mục tiêu:

```text
validate execution assumptions
validate statements/financing
measure live slippage
find operational bugs
```

Không phải maximize profit.

## 43. Research reproducibility

Mỗi experiment nên lưu:

```text
code version
config
input dataset version
run timestamp
universe
parameters
metrics
plots/results
```

Nếu không reproduce được backtest cũ, research process chưa đủ đáng tin.

## 44. Data lineage

Biết mỗi field đến từ đâu:

```text
Vendor/source
Timezone
Revision policy
Cleaning steps
Missing-value handling
```

Không có data lineage thì bug khó audit.

## 45. Missing data

Không forward-fill mọi thứ máy móc.

Forward-fill policy rate có thể hợp giữa meetings; forward-fill price qua market outage có thể tạo fake tradability.

Handling phải theo semantic của field.

## 46. Outliers

Bad tick và true market jump có thể giống nhau.

Nếu filter mọi extreme return, có thể xóa chính tail risk strategy phải chịu.

Outlier cleaning cần cross-source/context validation nếu possible.

## 47. Delisting/regime transitions equivalent trong FX

Currency conversion, peg break hoặc capital control event cần explicit handling.

Không silently stitch incompatible price series.

## 48. A minimal backtest audit

Trước khi tin result, hỏi:

```text
1. Was every input known at decision time?
2. Is execution after signal formation?
3. Are bid/ask and costs modeled?
4. Is financing modeled?
5. Are timestamps/timezones correct?
6. Is margin/leverage realistic?
7. Was model selected using future/test data?
8. How many variants were tried?
9. Is result stable across parameters/regimes?
10. Can the run be reproduced?
```

## 49. Khi nào backtest không đủ?

Nếu edge phụ thuộc:

- market depth;
- queue priority;
- ultra-fast event execution;
- discretionary interpretation;

OHLC backtest có thể fundamentally inadequate.

Cần richer data hoặc chấp nhận rằng strategy không thể được validated theo cùng standard.

## 50. Handoff sang portfolio risk

Backtest một strategy đơn lẻ chưa trả lời:

- nhiều strategies tương tác ra sao;
- currency factors overlap thế nào;
- correlation thay đổi trong stress;
- risk budget phân bổ thế nào.

→ [11 — Portfolio FX risk, correlation and factor exposure](./11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)

## Internal links

- [Systematic Risk, Backtest and Execution](../02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md)
- [Strategy Research, Robustness and Portfolio of Strategies](../04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md)
- [05 — Execution, brokers, costs and risk](./05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
- [09 — FX strategy families](./09_CARRY_MOMENTUM_VALUE_AND_MACRO_FX_STRATEGIES.md)
