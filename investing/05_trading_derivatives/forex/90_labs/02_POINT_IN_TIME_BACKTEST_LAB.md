# Lab 02 — Point-in-Time FX Backtest

Mục tiêu của lab là biến một ý tưởng trading thành test có thể audit. Không được bắt đầu bằng optimization. Trước tiên phải khóa hypothesis, data availability và execution assumptions.

## Bước 1 — Strategy specification

Chọn một hypothesis đơn giản, ví dụ:

```text
Trend continuation after volatility-adjusted pullback
Range mean reversion
Post-event drift
Carry + momentum filter
Breakout conditional on volatility regime
```

Viết specification đủ chi tiết để hai người có thể code giống nhau:

```text
Universe
Pair selection rule
Timeframe
Timezone
Signal formula
Lookback
Entry rule
Exit rule
Stop / invalidation
Holding period
Position sizing
Max concurrent exposure
Event/session filter
Weekend rule
```

## Bước 2 — Point-in-time data map

Với từng biến, ghi:

```text
Source
Timestamp available to strategy
Revision possible?
Publication delay?
Timezone
Missing-data policy
```

Nếu dùng macro data, không được backfill revised values vào lịch sử như thể trader biết chúng ở thời điểm release.

Nếu dùng daily OHLC, phải nói rõ candle cutoff timezone. Nếu dùng session strategy, xử lý DST.

## Bước 3 — Price and execution model

Tối thiểu phải model:

```text
Bid/ask or conservative spread
Commission
Slippage
Financing / rollover for held positions
Delayed execution assumption
```

Không dùng mid-price close làm cả entry và exit nếu live strategy cần crossing spread.

Tạo ba cost scenarios:

```text
Base
1.5x normal cost
2x normal cost / stress
```

## Bước 4 — Train / validate / test

Không dùng toàn bộ sample để chọn parameters rồi báo kết quả trên chính sample đó.

Có thể dùng:

```text
Chronological train
Validation
Final untouched test
```

hoặc walk-forward nếu phù hợp.

Nếu strategy dùng nhiều parameter combinations, ghi rõ số lần thử. Multiple testing là một phần của risk model.

## Bước 5 — Metrics

Không chỉ báo win rate. Tối thiểu:

```text
Number of trades
Average win / loss
Expectancy
Profit factor
CAGR or annualized return if meaningful
Volatility
Sharpe / Sortino with caveats
Max drawdown
Calmar if meaningful
Exposure / time in market
Turnover
Average cost per trade
MAE / MFE
Longest losing streak
```

## Bước 6 — Robustness

Thử ít nhất:

```text
Parameter ±10–20%
Entry delayed 1 bar
Signal threshold shifted
Cost +50%
Different pair subset
Different years
Different volatility regimes
Different rate regimes
Remove best 5 trades
```

Một strategy chỉ tốt ở đúng một parameter point cần bị nghi ngờ.

## Bước 7 — Regime attribution

Chia P/L theo:

```text
Trend / range proxy
High / low volatility
Risk-on / risk-off proxy
Policy-divergence regime
Session
Pair
Long vs short
Event vs non-event period
```

Mục tiêu là biết edge đến từ đâu và điều kiện nào làm nó biến mất.

## Bước 8 — Leakage audit

Trả lời bằng văn bản:

```text
Could any feature contain future information?
Could revised macro data leak future knowledge?
Could session timestamps be shifted by DST?
Could stop/target ordering inside OHLC bars be ambiguous?
Could pair selection use information unavailable at selection time?
Could spread assumptions be based on future averages?
```

## Bước 9 — Forward-test plan

Backtest đạt không có nghĩa triển khai ngay bằng size lớn.

Viết:

```text
Paper/demo period
Small-live period
Required number of observations
Execution metrics to compare with backtest
Maximum tolerated implementation shortfall
Kill-switch conditions
Conditions to scale
Conditions to retire
```

## Đầu ra bắt buộc

Tạo:

```text
fx_strategy_spec.md
fx_data_manifest.md
fx_bias_audit.md
fx_backtest_report.md
fx_robustness_report.md
fx_forward_test_plan.md
```

## Tự chấm

Bài chưa đạt nếu phần hấp dẫn nhất vẫn là equity curve. Bài đạt khi người review có thể kiểm tra **data available when, rule defined how, filled at what assumption, cost modeled how, tested how many times, failed in which regimes**.

Đọc lại:

- [07 — Indicators as data transformations](../07_TECHNICAL_INDICATORS_AS_DATA_TRANSFORMATIONS.md)
- [09 — Carry, momentum, value and macro strategies](../09_CARRY_MOMENTUM_VALUE_AND_MACRO_FX_STRATEGIES.md)
- [10 — Backtesting and point-in-time FX data](../10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)
