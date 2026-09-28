# Systematic FX Hiện thực (implementation / 구현) Dự án (project / 프로젝트)

Dự án (project / 프로젝트) này biến phần Forex từ tài liệu phân tích thành một research hệ thống (system / 시스템) có thể kiểm tra (audit / 감사). Mục tiêu không phải tạo bot giao dịch “tự kiếm tiền”, mà là buộc toàn bộ chuỗi **dữ liệu (data / 데이터) → tính năng (feature / 기능) → tín hiệu (signal / 신호) → sizing → thực thi (execution / 실행) giả định (assumption / 가정) → portfolio → rà soát (review / 검토)** phải tường minh (explicit / 명시적) và reproducible.

Dự án (project / 프로젝트) nên được làm sau khi đã đọc ít nhất:

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

Nếu không thể dấu vết (trace / 추적) một P/L observation ngược lại raw dữ liệu (data / 데이터), timestamp, quy tắc (rule / 규칙) và thực thi (execution / 실행) giả định (assumption / 가정), research chưa đủ auditability.

## Các mô-đun (module / 모듈)

1. [01_DATA_PIPELINE_AND_TIME_NORMALIZATION.md](./01_DATA_PIPELINE_AND_TIME_NORMALIZATION.md) — dữ liệu (data / 데이터) lược đồ (schema / 스키마), bid/ask, timezone, DST, macro vintage, chất lượng (quality / 품질) checks và reproducibility.
2. [02_BACKTEST_ENGINE_AND_EXECUTION_MODEL.md](./02_BACKTEST_ENGINE_AND_EXECUTION_MODEL.md) — deterministic vòng lặp sự kiện (event loop / 이벤트 루프), tín hiệu (signal / 신호) timing, fills, spread/slippage, financing, margin và portfolio accounting.
3. [03_PORTFOLIO_RISK_AND_ATTRIBUTION_ENGINE.md](./03_PORTFOLIO_RISK_AND_ATTRIBUTION_ENGINE.md) — currency-leg aggregation, leverage, rủi ro (risk / 위험) limits, stress tests, factor attribution và trade-level decomposition.
4. [04_FORWARD_TEST_MONITORING_AND_KILL_SWITCH.md](./04_FORWARD_TEST_MONITORING_AND_KILL_SWITCH.md) — paper/small-live progression, reconciliation, drift monitoring, operational controls và retirement rules.

## Deliverables

Dự án (project / 프로젝트) hoàn chỉnh nên tạo được:

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

Có thể implement bằng Python, Java, SQL hoặc ngăn xếp (stack / 스택) khác. Ngôn ngữ không quan trọng bằng ngữ nghĩa (semantics / 의미론). Hai hiện thực (implementation / 구현) khác nhau đọc cùng specification phải cho kết quả giống nhau trong tolerance định trước.

## Nguyên tắc thiết kế

Research hệ thống (system / 시스템) không được “sửa kết quả” bằng cách chỉnh dữ liệu (data / 데이터)/parameter sau khi nhìn equity curve mà không ghi lại experiment lịch sử (history / 이력).

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

Nếu một kết quả (result / 결과) không thể reproduce từ các siêu dữ liệu (metadata / 메타데이터) trên, không dùng nó làm bằng chứng cho edge.

## Phạm vi (scope / 범위) ranh giới (boundary / 경계)

Folder này không duplicate kiến thức kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) tổng quát. Nó chỉ giải thích **FX-specific research ngữ nghĩa (semantics / 의미론)**: timezone/session, bid/ask, rollover, macro vintage, currency conversion, margin, portfolio factor exposure và thực thi (execution / 실행) modeling.

Hiện thực (implementation / 구현) sâu về cơ sở dữ liệu (database / 데이터베이스), phân tán (distributed / 분산) processing, CI/CD hay cloud hạ tầng (infrastructure / 인프라) nên tham chiếu các lĩnh vực (domain / 도메인) computing tương ứng trong repository thay vì nhét toàn bộ vào Forex.
