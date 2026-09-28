# 04 — Forward Kiểm thử (test / 테스트), Monitoring và Kill Switch cho Systematic FX

Một backtest tốt chỉ chứng minh chiến lược (strategy / 전략) **đáng được kiểm tra tiếp**, không chứng minh hệ thống (system / 시스템) đã sẵn sàng nhận capital. Giữa research và live trading còn một lớp lớn gồm market-data độ tin cậy (reliability / 신뢰성), thứ tự (order / 순서) reconciliation, hiện thực (implementation / 구현) shortfall, margin, operational thất bại (failure / 실패) và mô hình (model / 모델) drift.

Mô-đun (module / 모듈) này xây progression:

```text
Backtest
→ Paper / Demo
→ Small Live
→ Controlled Scale
→ Ongoing Monitoring
→ Pause / Kill / Retire when evidence deteriorates
```

Mục tiêu không phải automation tối đa. Mục tiêu là **thất bại (failure / 실패) phải observable, bounded và recoverable**.

## 1. Promotion gate từ backtest sang forward kiểm thử (test / 테스트)

Không forward-test chỉ vì Sharpe đẹp.

Trước khi promotion, cần:

```text
Frozen strategy specification
Untouched out-of-sample evidence
Cost sensitivity
Stress tests
Known data limitations
Risk limits
Execution model
Operational controls
Retirement criteria
```

Nếu chiến lược (strategy / 전략) spec vẫn thay đổi mỗi tuần theo recent P/L, forward kiểm thử (test / 테스트) không còn independent kiểm tra hợp lệ (validation / 검증).

## 2. Paper/demo phase có mục tiêu gì?

Paper/demo không chủ yếu để chứng minh profitability.

Nó kiểm tra:

```text
Signal timing
Session/timezone behavior
Order generation
Position sizing
Broker/API semantics
State transitions
Monitoring
Reconciliation
```

Demo thực thi (execution / 실행) có thể optimistic hơn live, nên không dùng demo slippage làm final chi phí (cost / 비용) estimate.

## 3. Small-live phase

Sau paper, dùng capital nhỏ đủ để observe real thực thi (execution / 실행) nhưng không material nếu thất bại (failure / 실패) xảy ra.

Monitor:

```text
decision-to-fill latency
spread
slippage
rejection rate
partial fills
financing
margin behavior
platform incidents
```

Mục tiêu là calibrate **backtest-to-live gap**.

## 4. Quy mô (scale / 규모) only by bằng chứng (evidence / 증거)

Quy mô (scale / 규모) gate có thể yêu cầu:

```text
minimum live observations
execution cost within tolerance
no unresolved reconciliation errors
risk limits stable
strategy behavior consistent with expected distribution
```

Không quy mô (scale / 규모) chỉ vì vài trade đầu thắng.

## 5. Live trạng thái (state / 상태) must be authoritative

Nội bộ (internal / 내부) hệ thống (system / 시스템) có expected position.

Broker/dealer có actual position.

Need reconcile:

```text
Expected State
vs
External Authoritative State
```

Nếu khác, không assume nội bộ (internal / 내부) hệ thống (system / 시스템) đúng.

## 6. Reconciliation vòng lặp (loop / 루프)

Regularly compare:

```text
open orders
filled orders
positions
cash/balance
equity
fees
financing
margin
```

Mismatch becomes tường minh (explicit / 명시적) sự cố (incident / 인시던트).

## 7. Unknown trạng thái (state / 상태) is a real trạng thái (state / 상태)

Mạng (network / 네트워크) hết thời gian chờ (timeout / 타임아웃) after thứ tự (order / 순서) submission:

```text
Did broker receive order?
Did order fill?
```

Do not immediately resend.

Mark:

```text
ORDER_STATE_UNKNOWN
```

then truy vấn (query / 쿼리) broker/thứ tự (order / 순서) lịch sử (history / 이력) before hành động (action / 동작).

## 8. Idempotency

If API supports máy khách (client / 클라이언트) thứ tự (order / 순서) ID, generate stable unique ID.

Thử lại (retry / 재시도) should not accidentally create duplicate economic thứ tự (order / 순서).

Concept:

```text
same intent
→ same idempotency key
```

where supported.

## 9. Duplicate-order prevention

Nhánh học (track / 트랙):

```text
strategy_id
signal_id
instrument
intended_side
intended_quantity
```

Before new send, check whether same intent already has active/filled thứ tự (order / 순서).

## 10. Heartbeat

Hệ thống (system / 시스템) needs liveness tín hiệu (signal / 신호) for:

```text
market data
broker connection
strategy process
risk service
clock synchronization
```

Missing heartbeat should trigger degraded trạng thái (state / 상태), not silent continuation.

## 11. Stale-data detection

A valid-looking price can still be stale.

Define maximum acceptable age by chiến lược (strategy / 전략)/timeframe:

```text
now - last_market_timestamp <= threshold
```

If stale:

```text
block new risk
```

and decide whether existing positions require manual/automated safe hành động (action / 동작).

## 12. Clock synchronization

Event-driven các hệ thống (systems / 시스템들) need synchronized clocks.

Monitor cục bộ (local / 로컬) clock drift.

Timestamp inconsistency can break:

```text
latency measurement
event sequencing
session filters
reconciliation
```

## 13. Data-quality kill điều kiện (condition / 조건)

Examples:

```text
crossed market unexpectedly
spread impossible
missing conversion rate
price jump inconsistent across sources
macro event feed delayed
```

Do not trade through unknown dữ liệu (data / 데이터) trạng thái (state / 상태) by default.

## 14. Pre-trade kill switch

Kill switch can khối (block / 블록) **new orders** while leaving hệ thống (system / 시스템) able to manage existing positions.

This is often safer than shutting entire tiến trình (process / 프로세스) immediately.

States could be:

```text
NORMAL
NO_NEW_RISK
REDUCE_ONLY
CLOSE_ALL
HALTED
```

## 15. Daily mất mát (loss / 손실) limit

A daily mất mát (loss / 손실) limit is operational guardrail, not proof chiến lược (strategy / 전략) is bad.

When breached:

```text
stop new risk
review state
```

Do not automatically increase kích thước (size / 크기) to recover.

## 16. Drawdown limit

Portfolio drawdown threshold can trigger:

```text
size reduction
strategy pause
full research review
```

Threshold should reflect expected phân phối (distribution / 분포) and bất định (uncertainty / 불확실성).

## 17. Gross leverage limit

Monitor continuously:

```text
Gross Leverage = Σ|notional| / equity
```

Equity drop can cause leverage limit breach without any new thứ tự (order / 순서).

## 18. Currency-factor limit

If USD short exposure exceeds cap because several strategies align:

```text
block additional USD-short risk
```

even if each chiến lược (strategy / 전략) individually remains within position limit.

## 19. Margin utilization limit

Do not operate near broker stop-out threshold.

Define nội bộ (internal / 내부) buffer substantially more conservative than bên ngoài (external / 외부) minimum.

Monitor:

```text
used_margin / equity
free_margin
margin_level
```

## 20. Margin-policy thay đổi (change / 변경)

Broker may thay đổi (change / 변경) requirements.

On notification or detected thay đổi (change / 변경):

```text
recompute all projected margins
stress before accepting new positions
```

## 21. Slippage drift

Compare live slippage with research expectation.

Metrics:

```text
mean
median
95th percentile
by pair
by session
by event flag
```

Persistent deterioration may erase edge before gross P/L reveals it clearly.

## 22. Spread drift

Nhánh học (track / 트랙) live spread phân phối (distribution / 분포) against backtest dữ liệu (data / 데이터).

If live spread materially worse:

```text
estimated net expectancy must be recomputed
```

## 23. Rejection-rate monitoring

High rejection tỷ lệ (rate / 비율) can indicate:

```text
bad order assumptions
API issues
market stress
broker restrictions
```

Do not treat rejected thứ tự (order / 순서) as zero-cost missing observation.

## 24. Fill-rate monitoring for limits

Limit-order chiến lược (strategy / 전략) may look profitable if backtest assumes fills too easily.

Forward kiểm thử (test / 테스트) compares:

```text
modeled fill probability
vs
actual fill rate
```

by thị trường (market / 시장) regime.

## 25. Hiện thực (implementation / 구현) shortfall dashboard

For each trade:

```text
Decision Price
Arrival Price
Fill Price
Exit Fill
Spread
Commission
Slippage
Financing
```

Aggregate to see where edge leaks.

## 26. P/L reconciliation

Daily:

```text
Opening Equity
+ Realized P/L
+ Unrealized Change
+ Financing
- Fees
+ Deposits/Withdrawals
= Closing Equity
```

Differences beyond rounding threshold become sự cố (incident / 인시던트).

## 27. Chiến lược (strategy / 전략) expected phân phối (distribution / 분포)

Before live, freeze expected ranges for:

```text
trade frequency
win rate interval
average holding period
turnover
cost/trade
volatility
max losing streak distribution
```

Use ranges, not one chính xác (exact / 정확한) forecast.

## 28. Hiệu năng (performance / 성능) drift

A few losses are not drift.

Monitor statistical/tiến trình (process / 프로세스) bằng chứng (evidence / 증거) such as:

```text
rolling expectancy
hit rate
payoff ratio
cost-adjusted edge
feature distribution
regime mix
```

Avoid overreacting to noise.

## 29. Tính năng (feature / 기능) drift

If tín hiệu (signal / 신호) tính năng (feature / 기능) phân phối (distribution / 분포) shifts far from huấn luyện (training / 학습) lịch sử (history / 이력):

```text
strategy may be extrapolating
```

Monitor quantiles/phạm vi (range / 범위)/out-of-distribution flags.

## 30. Regime drift

A chiến lược (strategy / 전략) tested mainly in low-volatility monetary-policy regime may face new trạng thái (state / 상태).

Regime detector should be ngữ cảnh (context / 맥락), not magical switch.

Potential inputs:

```text
realized volatility
rate dispersion
funding stress
trend strength
liquidity/spread state
```

## 31. Data-source drift

Vendor can thay đổi (change / 변경) methodology or symbol ánh xạ (mapping / 매핑).

Detect via:

```text
schema change
sudden spread shift
cross-source divergence
missing fields
```

Mô hình (model / 모델) drift may actually be dữ liệu (data / 데이터) drift.

## 32. Mô hình (model / 모델) versioning

Every live thứ tự (order / 순서) should map to:

```text
strategy_version
config_version
risk_model_version
```

If cấu hình (config / 설정) changes intraday, preserve chính xác (exact / 정확한) effective thời gian (time / 시간).

## 33. Controlled cấu hình (configuration / 구성) changes

Do not edit môi trường vận hành (production / 운영 환경) parameters manually without bản ghi (record / 레코드).

Use thay đổi (change / 변경) log:

```text
who/what changed
when
old value
new value
reason
approval if applicable
```

For personal hệ thống (system / 시스템), “who” may be one person; kiểm tra (audit / 감사) still matters.

## 34. Secret management

API keys must not be committed to repo or logs.

Separate:

```text
research credentials
paper credentials
live credentials
```

Use least privilege if provider supports it.

## 35. Withdrawal permission

Trading API generally should not need withdrawal permission.

If provider offers permission scopes, avoid unnecessary fund-transfer năng lực (capability / 역량).

## 36. Môi trường (environment / 환경) separation

Conceptual environments:

```text
RESEARCH
PAPER
LIVE_SMALL
LIVE_SCALED
```

Do not let research notebook accidentally send live orders.

## 37. Tường minh (explicit / 명시적) live flag is not enough

Prefer separate credentials/endpoints/accounts over one Boolean `LIVE=true` where possible.

Reduce catastrophic operator lỗi (error / 오류).

## 38. Max thứ tự (order / 순서) kích thước (size / 크기)

Hard cap at thực thi (execution / 실행) gateway:

```text
requested quantity <= max_order_size
```

independent of chiến lược (strategy / 전략) calculation.

This catches đơn vị (unit / 단위) bugs such as 10,000 vs 1,000,000.

## 39. Price sanity check

Reject thứ tự (order / 순서) if proposed price/tham chiếu (reference / 참조) deviates excessively from hiện tại (current / 현재) validated thị trường (market / 시장) trạng thái (state / 상태).

Avoid sending nonsensical orders after stale/decimal bug.

## 40. Position sanity check

Before thực thi (execution / 실행):

```text
projected_position
```

must stay within hard an toàn (safety / 안전) bound even if chiến lược (strategy / 전략)/rủi ro (risk / 위험) dịch vụ (service / 서비스) malfunctions.

Defense in độ sâu (depth / 깊이) matters.

## 41. Tỷ lệ (rate / 비율) limiting

Cap:

```text
orders/minute
cancels/minute
retries/order
```

Prevents runaway loops.

## 42. Kill switch trigger categories

### Market-risk

```text
daily loss
drawdown
leverage
margin
stress loss
```

### Thực thi (execution / 실행)

```text
slippage spike
rejection spike
fill anomaly
```

### Dữ liệu (data / 데이터)

```text
stale feed
schema error
cross-source inconsistency
```

### Operational

```text
API outage
reconciliation mismatch
unknown positions
process instability
```

## 43. Kill switch hành động (action / 동작) must be predefined

Trigger without hành động (action / 동작) is incomplete.

Define for each:

```text
block new orders?
cancel open orders?
reduce positions?
close all?
notify human?
require manual resume?
```

## 44. Avoid blind close-all

In some crisis states, thị trường (market / 시장) orders to close all may create worse mất mát (loss / 손실) than controlled reduction.

Kill hành động (action / 동작) should consider liquidity.

Sometimes safest first trạng thái (state / 상태) is:

```text
NO_NEW_RISK
+ reconcile
+ assess executable liquidity
```

## 45. Manual override

Manual override must itself be logged.

If human resumes hệ thống (system / 시스템):

```text
reason
state checked
time
```

Avoid repeated emotional pause/resume based only on recent P/L.

## 46. Broker outage plan

Know:

```text
alternative access channel
phone dealing/support if applicable
web/mobile backup
position visibility
emergency contact
```

Do not promise tools that provider does not offer; document actual account options.

## 47. Internet/thiết bị (device / 장치) thất bại (failure / 실패)

For cục bộ (local / 로컬) personal hệ thống (system / 시스템), plan:

```text
power/network loss
machine sleep
process crash
```

Use broker-side protective orders where appropriate, but remember stop thực thi (execution / 실행) is not guaranteed price.

## 48. Tiến trình (process / 프로세스) supervision

Trọng yếu (critical / 중요) services need restart/alert chính sách (policy / 정책).

But automatic restart after crash must first reconcile bên ngoài (external / 외부) trạng thái (state / 상태).

Never restart and assume no orders filled during downtime.

## 49. Checkpoint trạng thái (state / 상태)

Persist enough trạng thái (state / 상태) to recover:

```text
last processed event
known orders
known fills
virtual strategy positions
risk snapshot
```

After restart, compare with broker before continuing.

## 50. Alert severity

Example:

```text
INFO
WARNING
CRITICAL
HALT
```

Not every warning should wake operator; trọng yếu (critical / 중요) trạng thái (state / 상태) should be unmistakable.

## 51. Monitoring dashboard

Minimum live dashboard:

```text
Equity
Balance
Open P/L
Gross leverage
Currency exposures
Used/free margin
Open orders
Data freshness
Broker connectivity
Today's P/L
Today's costs
Slippage vs model
Active kill-switch state
```

## 52. Research vs môi trường vận hành (production / 운영 환경) metrics

Research cares about:

```text
Sharpe
expectancy
robustness
```

Môi trường vận hành (production / 운영 환경) also cares about:

```text
latency
rejections
reconciliation
uptime
data freshness
```

A profitable mô hình (model / 모델) with unreliable môi trường vận hành (production / 운영 환경) chuỗi xử lý (pipeline / 파이프라인) is not deployable.

## 53. Promotion from small-live to scaled

Require bằng chứng (evidence / 증거) such as:

```text
N minimum trades/events
No unresolved accounting mismatch
Live cost <= predefined tolerance
Risk process worked during adverse events
No material unexplained P/L
```

Quy mô (scale / 규모) gradually.

## 54. Scaling changes chiến lược (strategy / 전략) hành vi (behavior / 동작)

Larger kích thước (size / 크기) can cause:

```text
more slippage
lower fill rate
higher market impact
capacity limit
```

Do not assume small-live thực thi (execution / 실행) scales linearly.

## 55. Sức chứa (capacity / 용량) monitoring

As kích thước (size / 크기) grows, nhánh học (track / 트랙):

```text
cost per unit notional
fill rate
slippage vs size
```

Stop scaling when marginal hiện thực (implementation / 구현) chi phí (cost / 비용) consumes expected edge.

## 56. Pause quy tắc (rule / 규칙)

Pause can be triggered by uncertain bằng chứng (evidence / 증거) where full retirement is premature.

Examples:

```text
data vendor methodology change
unexplained execution deterioration
feature out-of-distribution
regulatory/product term change
```

Pause is research trạng thái (state / 상태), not punishment.

## 57. Retirement quy tắc (rule / 규칙)

Predefine retirement conditions before chiến lược (strategy / 전략) loses money.

Possible:

```text
causal mechanism no longer exists
net expectancy statistically/economically collapses
cost permanently exceeds edge
market access/product changes
risk exceeds mandate
```

## 58. Do not retire only because drawdown hurts

Drawdown may be within expected phân phối (distribution / 분포).

Compare actual hành vi (behavior / 동작) with pre-defined expectation.

Likewise, do not keep chiến lược (strategy / 전략) just because “it always comes back”.

## 59. Chiến lược (strategy / 전략) post-mortem

When paused/retired:

```text
Original hypothesis
Expected behavior
Observed behavior
Signal P/L
Cost drift
Factor exposure
Regime changes
Operational incidents
Decision errors
Conclusion
```

## 60. Sự cố (incident / 인시던트) post-mortem

Operational sự cố (incident / 인시던트) template:

```text
Timeline
Impact
Detection
Root cause
Contributing factors
Why safeguards failed
Immediate fix
Permanent control
Test added
```

No blame ngôn ngữ (language / 언어) needed; focus hệ thống (system / 시스템) mechanics.

## 61. Experiment/live linkage

Every live chiến lược (strategy / 전략) phiên bản (version / 버전) should điểm (point / 지점) to research experiment approved for triển khai (deployment / 배포).

```text
live_strategy_version
→ experiment_id
→ data/config/code versions
```

This closes research-to-production lineage.

## 62. Forward-test report

Compare:

```text
Backtest expected
Paper observed
Small-live observed
```

for:

```text
trade frequency
cost
slippage
holding time
P/L distribution
fill rate
```

## 63. Backtest-to-live gap classification

When live differs, categorize:

```text
Data difference
Signal timing
Execution
Cost
Portfolio interaction
Behavior/operator
Regime
Unknown
```

Avoid changing mô hình (model / 모델) until gap is understood.

## 64. Operational rehearsal

Before scaling, intentionally kiểm thử (test / 테스트):

```text
market data disconnect
broker API disconnect
process restart
order timeout
partial fill
reconciliation mismatch
kill switch
```

A điều khiển (control / 제어) not rehearsed may thất bại (fail / 실패) when needed.

## 65. Khôi phục (recovery / 복구) criterion

After HALT, resumption requires checklist:

```text
External positions reconciled
Orders known
Data fresh
Risk within limits
Root cause understood enough
System tests pass
```

## 66. Weekend/reopen plan

If chiến lược (strategy / 전략) holds weekends:

```text
expected open gap risk
protective order behavior
margin buffer
news monitoring responsibilities
```

must be tường minh (explicit / 명시적).

If no weekend holding, verify hệ thống (system / 시스템) actually closes before provider schedule with enough liquidity buffer.

## 67. Scheduled-event chế độ (mode / 모드)

Before CPI/FOMC/BOK-type events, rủi ro (risk / 위험) chính sách (policy / 정책) may:

```text
reduce size
block new entries
widen modeled cost assumptions
```

only if chiến lược (strategy / 전략) spec says so. Do not improvise sự kiện (event / 이벤트) rules live.

## 68. Regulation/product-term monitoring

Retail FX terms and truy cập (access / 접근) can thay đổi (change / 변경).

Maintain rà soát (review / 검토) date for:

```text
leverage limits
margin policy
negative-balance treatment
product eligibility
broker legal entity
```

Especially for Korea/Vietnam-specific ngữ cảnh (context / 맥락), verify hiện tại (current / 현재) official rules.

## 69. Monitoring retention

Store logs long enough to investigate:

```text
signal
order
fill
risk snapshot
data health
incident
```

Avoid sensitive secret/đơn vị từ (token / 토큰) logging.

## 70. Completion criteria

Dự án (project / 프로젝트) is not complete until you can demonstrate:

```text
System detects stale data
System prevents duplicate order
System reconciles after restart
System blocks limit breach
System records live implementation shortfall
System can enter safe state
System has pre-defined promotion/pause/retirement rules
```

## Deliverables

Create:

```text
forward_test_plan.md
promotion_gates.md
monitoring_spec.md
risk_limits.md
kill_switch_matrix.md
reconciliation_spec.md
incident_runbook.md
strategy_retirement_rule.md
forward_test_report.md
```

## Kết thúc dự án (project / 프로젝트)

Sau bốn mô-đun (module / 모듈), một systematic FX dự án (project / 프로젝트) phải nối được:

```text
Point-in-Time Data
→ Deterministic Research
→ Executable Backtest
→ Portfolio Risk
→ Attribution
→ Forward Test
→ Live Monitoring
→ Safe Failure / Retirement
```

Đây mới là cầu nối (bridge / 브리지) từ “chiến lược (strategy / 전략) idea” sang một research/môi trường vận hành (production / 운영 환경) tiến trình (process / 프로세스) có thể kiểm tra.

Liên quan:

- [12 — Trading journal, review and attribution](../12_TRADING_JOURNAL_REVIEW_AND_PERFORMANCE_ATTRIBUTION.md)
- [13 — Advanced FX microstructure](../13_ADVANCED_FX_MICROSTRUCTURE_AND_ORDER_FLOW.md)
- [05 — Execution, brokers, costs and risk](../05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
