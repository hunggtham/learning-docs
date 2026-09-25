# Systematic FX Implementation Project

Project này biến phần Forex từ tài liệu phân tích thành một research system có thể audit. Mục tiêu không phải tạo bot giao dịch “tự kiếm tiền”, mà là buộc toàn bộ chuỗi **data → feature → signal → sizing → execution assumption → portfolio → review** phải explicit và reproducible.

Project nên được làm sau khi đã đọc ít nhất:

```text
01–05  mechanics, leverage, execution
07     indicators as data transformations
09     strategy families
10     point-in-time backtesting
11     portfolio FX risk
12     journal and attribution
13     microstructure
```

## Kiến trúc tổng quát

```text
Raw Data
→ Validation
→ Time Normalization
→ Point-in-Time Dataset
→ Features
→ Signal
→ Position Sizing
→ Portfolio Constraints
→ Execution / Cost Model
→ Backtest Ledger
→ Attribution
→ Robustness Tests
→ Forward Test
→ Production Controls
```

Nếu không thể trace một P/L observation ngược lại raw data, timestamp, rule và execution assumption, research chưa đủ auditability.

## Các module

1. [01_DATA_PIPELINE_AND_TIME_NORMALIZATION.md](./01_DATA_PIPELINE_AND_TIME_NORMALIZATION.md) — data schema, bid/ask, timezone, DST, macro vintage, quality checks và reproducibility.
2. [02_BACKTEST_ENGINE_AND_EXECUTION_MODEL.md](./02_BACKTEST_ENGINE_AND_EXECUTION_MODEL.md) — deterministic event loop, signal timing, fills, spread/slippage, financing, margin và portfolio accounting.
3. [03_PORTFOLIO_RISK_AND_ATTRIBUTION_ENGINE.md](./03_PORTFOLIO_RISK_AND_ATTRIBUTION_ENGINE.md) — currency-leg aggregation, leverage, risk limits, stress tests, factor attribution và trade-level decomposition.
4. [04_FORWARD_TEST_MONITORING_AND_KILL_SWITCH.md](./04_FORWARD_TEST_MONITORING_AND_KILL_SWITCH.md) — paper/small-live progression, reconciliation, drift monitoring, operational controls và retirement rules.

## Deliverables

Project hoàn chỉnh nên tạo được:

```text
data_manifest.md
schema.md
validation_report.md
strategy_spec.md
cost_model.md
backtest_report.md
robustness_report.md
portfolio_risk_report.md
attribution_report.md
forward_test_plan.md
monitoring_spec.md
retirement_rule.md
```

Có thể implement bằng Python, Java, SQL hoặc stack khác. Ngôn ngữ không quan trọng bằng semantics. Hai implementation khác nhau đọc cùng specification phải cho kết quả giống nhau trong tolerance định trước.

## Nguyên tắc thiết kế

Research system không được “sửa kết quả” bằng cách chỉnh data/parameter sau khi nhìn equity curve mà không ghi lại experiment history.

Mỗi experiment cần có:

```text
experiment_id
code_version
config_hash
data_version
run_timestamp
train_period
validation_period
test_period
cost_model_version
result_summary
```

Nếu một result không thể reproduce từ các metadata trên, không dùng nó làm bằng chứng cho edge.

## Scope boundary

Folder này không duplicate kiến thức software engineering tổng quát. Nó chỉ giải thích **FX-specific research semantics**: timezone/session, bid/ask, rollover, macro vintage, currency conversion, margin, portfolio factor exposure và execution modeling.

Implementation sâu về database, distributed processing, CI/CD hay cloud infrastructure nên tham chiếu các domain computing tương ứng trong repository thay vì nhét toàn bộ vào Forex.
