# Lab 02 — Point-in-Time FX Backtest

Mục tiêu của lab là biến một ý tưởng trading thành kiểm thử (test / 테스트) có thể kiểm tra (audit / 감사). Không được bắt đầu bằng tối ưu hóa (optimization / 최적화). Trước tiên phải khóa hypothesis, dữ liệu (data / 데이터) availability và thực thi (execution / 실행) các giả định (assumptions / 가정들).

## Bước 1 — Chiến lược (strategy / 전략) specification

Chọn một hypothesis đơn giản, ví dụ:

```text
Trend continuation after volatility-adjusted pullback
Range mean reversion
Post-event drift
Carry + momentum filter
Breakout conditional on volatility regime
```

Viết specification đủ chi tiết để hai người có thể mã (code / 코드) giống nhau:

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

## Bước 2 — Point-in-time dữ liệu (data / 데이터) map

Với từng biến, ghi:

```text
Source
Timestamp available to strategy
Revision possible?
Publication delay?
Timezone
Missing-data policy
```

Nếu dùng macro dữ liệu (data / 데이터), không được backfill revised values vào lịch sử như thể trader biết chúng ở thời điểm bản phát hành (release / 릴리스).

Nếu dùng daily OHLC, phải nói rõ candle cutoff timezone. Nếu dùng session chiến lược (strategy / 전략), xử lý DST.

## Bước 3 — Price and mô hình thực thi (execution model / 실행 모델)

Tối thiểu phải mô hình (model / 모델):

```text
Bid/ask or conservative spread
Commission
Slippage
Financing / rollover for held positions
Delayed execution assumption
```

Không dùng mid-price close làm cả entry và exit nếu live chiến lược (strategy / 전략) cần crossing spread.

Tạo ba chi phí (cost / 비용) scenarios:

```text
Base
1.5x normal cost
2x normal cost / stress
```

## Bước 4 — Train / validate / kiểm thử (test / 테스트)

Không dùng toàn bộ mẫu (sample / 표본) để chọn parameters rồi báo kết quả trên chính mẫu (sample / 표본) đó.

Có thể dùng:

```text
Chronological train
Validation
Final untouched test
```

hoặc walk-forward nếu phù hợp.

Nếu chiến lược (strategy / 전략) dùng nhiều parameter combinations, ghi rõ số lần thử. Multiple testing là một phần của rủi ro (risk / 위험) mô hình (model / 모델).

## Bước 5 — Metrics

Không chỉ báo win tỷ lệ (rate / 비율). Tối thiểu:

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

Một chiến lược (strategy / 전략) chỉ tốt ở đúng một parameter điểm (point / 지점) cần bị nghi ngờ.

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

## Bước 8 — Leakage kiểm tra (audit / 감사)

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

Backtest đạt không có nghĩa triển khai ngay bằng kích thước (size / 크기) lớn.

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

Bài chưa đạt nếu phần hấp dẫn nhất vẫn là equity curve. Bài đạt khi người rà soát (review / 검토) có thể kiểm tra **dữ liệu (data / 데이터) available when, quy tắc (rule / 규칙) defined how, filled at what giả định (assumption / 가정), chi phí (cost / 비용) modeled how, tested how many times, failed in which regimes**.

Đọc lại:

- [07 — Indicators as data transformations](../07_TECHNICAL_INDICATORS_AS_DATA_TRANSFORMATIONS.md)
- [09 — Carry, momentum, value and macro strategies](../09_CARRY_MOMENTUM_VALUE_AND_MACRO_FX_STRATEGIES.md)
- [10 — Backtesting and point-in-time FX data](../10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)
