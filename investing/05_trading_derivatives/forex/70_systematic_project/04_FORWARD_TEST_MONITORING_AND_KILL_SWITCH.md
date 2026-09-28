# 04 — Forward Test, Monitoring và Kill Switch cho Systematic FX

Một backtest tốt chỉ chứng minh strategy **đáng được kiểm tra tiếp**, không chứng minh system đã sẵn sàng nhận capital. Giữa research và live trading còn một lớp lớn gồm market-data reliability, order reconciliation, implementation shortfall, margin, operational failure và model drift.

Module này xây progression:

```text
Backtest
→ Paper / Demo
→ Small Live
→ Controlled Scale
→ Ongoing Monitoring
→ Pause / Kill / Retire when evidence deteriorates
```

Mục tiêu không phải automation tối đa. Mục tiêu là **failure phải observable, bounded và recoverable**.

## 1. Promotion gate từ backtest sang forward test

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

Nếu strategy spec vẫn thay đổi mỗi tuần theo recent P/L, forward test không còn independent validation.

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

Demo execution có thể optimistic hơn live, nên không dùng demo slippage làm final cost estimate.

## 3. Small-live phase

Sau paper, dùng capital nhỏ đủ để observe real execution nhưng không material nếu failure xảy ra.

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

## 4. Scale only by evidence

Scale gate có thể yêu cầu:

```text
minimum live observations
execution cost within tolerance
no unresolved reconciliation errors
risk limits stable
strategy behavior consistent with expected distribution
```

Không scale chỉ vì vài trade đầu thắng.

## 5. Live state must be authoritative

Internal system có expected position.

Broker/dealer có actual position.

Need reconcile:

```text
Expected State
vs
External Authoritative State
```

Nếu khác, không assume internal system đúng.

## 6. Reconciliation loop

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

Mismatch becomes explicit incident.

## 7. Unknown state is a real state

Network timeout after order submission:

```text
Did broker receive order?
Did order fill?
```

Do not immediately resend.

Mark:

```text
ORDER_STATE_UNKNOWN
```

then query broker/order history before action.

## 8. Idempotency

If API supports client order ID, generate stable unique ID.

Retry should not accidentally create duplicate economic order.

Concept:

```text
same intent
→ same idempotency key
```

where supported.

## 9. Duplicate-order prevention

Track:

```text
strategy_id
signal_id
instrument
intended_side
intended_quantity
```

Before new send, check whether same intent already has active/filled order.

## 10. Heartbeat

System needs liveness signal for:

```text
market data
broker connection
strategy process
risk service
clock synchronization
```

Missing heartbeat should trigger degraded state, not silent continuation.

## 11. Stale-data detection

A valid-looking price can still be stale.

Define maximum acceptable age by strategy/timeframe:

```text
now - last_market_timestamp <= threshold
```

If stale:

```text
block new risk
```

and decide whether existing positions require manual/automated safe action.

## 12. Clock synchronization

Event-driven systems need synchronized clocks.

Monitor local clock drift.

Timestamp inconsistency can break:

```text
latency measurement
event sequencing
session filters
reconciliation
```

## 13. Data-quality kill condition

Examples:

```text
crossed market unexpectedly
spread impossible
missing conversion rate
price jump inconsistent across sources
macro event feed delayed
```

Do not trade through unknown data state by default.

## 14. Pre-trade kill switch

Kill switch can block **new orders** while leaving system able to manage existing positions.

This is often safer than shutting entire process immediately.

States could be:

```text
NORMAL
NO_NEW_RISK
REDUCE_ONLY
CLOSE_ALL
HALTED
```

## 15. Daily loss limit

A daily loss limit is operational guardrail, not proof strategy is bad.

When breached:

```text
stop new risk
review state
```

Do not automatically increase size to recover.

## 16. Drawdown limit

Portfolio drawdown threshold can trigger:

```text
size reduction
strategy pause
full research review
```

Threshold should reflect expected distribution and uncertainty.

## 17. Gross leverage limit

Monitor continuously:

```text
Gross Leverage = Σ|notional| / equity
```

Equity drop can cause leverage limit breach without any new order.

## 18. Currency-factor limit

If USD short exposure exceeds cap because several strategies align:

```text
block additional USD-short risk
```

even if each strategy individually remains within position limit.

## 19. Margin utilization limit

Do not operate near broker stop-out threshold.

Define internal buffer substantially more conservative than external minimum.

Monitor:

```text
used_margin / equity
free_margin
margin_level
```

## 20. Margin-policy change

Broker may change requirements.

On notification or detected change:

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

Track live spread distribution against backtest data.

If live spread materially worse:

```text
estimated net expectancy must be recomputed
```

## 23. Rejection-rate monitoring

High rejection rate can indicate:

```text
bad order assumptions
API issues
market stress
broker restrictions
```

Do not treat rejected order as zero-cost missing observation.

## 24. Fill-rate monitoring for limits

Limit-order strategy may look profitable if backtest assumes fills too easily.

Forward test compares:

```text
modeled fill probability
vs
actual fill rate
```

by market regime.

## 25. Implementation shortfall dashboard

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

Differences beyond rounding threshold become incident.

## 27. Strategy expected distribution

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

Use ranges, not one exact forecast.

## 28. Performance drift

A few losses are not drift.

Monitor statistical/process evidence such as:

```text
rolling expectancy
hit rate
payoff ratio
cost-adjusted edge
feature distribution
regime mix
```

Avoid overreacting to noise.

## 29. Feature drift

If signal feature distribution shifts far from training history:

```text
strategy may be extrapolating
```

Monitor quantiles/range/out-of-distribution flags.

## 30. Regime drift

A strategy tested mainly in low-volatility monetary-policy regime may face new state.

Regime detector should be context, not magical switch.

Potential inputs:

```text
realized volatility
rate dispersion
funding stress
trend strength
liquidity/spread state
```

## 31. Data-source drift

Vendor can change methodology or symbol mapping.

Detect via:

```text
schema change
sudden spread shift
cross-source divergence
missing fields
```

Model drift may actually be data drift.

## 32. Model versioning

Every live order should map to:

```text
strategy_version
config_version
risk_model_version
```

If config changes intraday, preserve exact effective time.

## 33. Controlled configuration changes

Do not edit production parameters manually without record.

Use change log:

```text
who/what changed
when
old value
new value
reason
approval if applicable
```

For personal system, “who” may be one person; audit still matters.

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

If provider offers permission scopes, avoid unnecessary fund-transfer capability.

## 36. Environment separation

Conceptual environments:

```text
RESEARCH
PAPER
LIVE_SMALL
LIVE_SCALED
```

Do not let research notebook accidentally send live orders.

## 37. Explicit live flag is not enough

Prefer separate credentials/endpoints/accounts over one Boolean `LIVE=true` where possible.

Reduce catastrophic operator error.

## 38. Max order size

Hard cap at execution gateway:

```text
requested quantity <= max_order_size
```

independent of strategy calculation.

This catches unit bugs such as 10,000 vs 1,000,000.

## 39. Price sanity check

Reject order if proposed price/reference deviates excessively from current validated market state.

Avoid sending nonsensical orders after stale/decimal bug.

## 40. Position sanity check

Before execution:

```text
projected_position
```

must stay within hard safety bound even if strategy/risk service malfunctions.

Defense in depth matters.

## 41. Rate limiting

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

### Execution

```text
slippage spike
rejection spike
fill anomaly
```

### Data

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

## 43. Kill switch action must be predefined

Trigger without action is incomplete.

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

In some crisis states, market orders to close all may create worse loss than controlled reduction.

Kill action should consider liquidity.

Sometimes safest first state is:

```text
NO_NEW_RISK
+ reconcile
+ assess executable liquidity
```

## 45. Manual override

Manual override must itself be logged.

If human resumes system:

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

## 47. Internet/device failure

For local personal system, plan:

```text
power/network loss
machine sleep
process crash
```

Use broker-side protective orders where appropriate, but remember stop execution is not guaranteed price.

## 48. Process supervision

Critical services need restart/alert policy.

But automatic restart after crash must first reconcile external state.

Never restart and assume no orders filled during downtime.

## 49. Checkpoint state

Persist enough state to recover:

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

Not every warning should wake operator; critical state should be unmistakable.

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

## 52. Research vs production metrics

Research cares about:

```text
Sharpe
expectancy
robustness
```

Production also cares about:

```text
latency
rejections
reconciliation
uptime
data freshness
```

A profitable model with unreliable production pipeline is not deployable.

## 53. Promotion from small-live to scaled

Require evidence such as:

```text
N minimum trades/events
No unresolved accounting mismatch
Live cost <= predefined tolerance
Risk process worked during adverse events
No material unexplained P/L
```

Scale gradually.

## 54. Scaling changes strategy behavior

Larger size can cause:

```text
more slippage
lower fill rate
higher market impact
capacity limit
```

Do not assume small-live execution scales linearly.

## 55. Capacity monitoring

As size grows, track:

```text
cost per unit notional
fill rate
slippage vs size
```

Stop scaling when marginal implementation cost consumes expected edge.

## 56. Pause rule

Pause can be triggered by uncertain evidence where full retirement is premature.

Examples:

```text
data vendor methodology change
unexplained execution deterioration
feature out-of-distribution
regulatory/product term change
```

Pause is research state, not punishment.

## 57. Retirement rule

Predefine retirement conditions before strategy loses money.

Possible:

```text
causal mechanism no longer exists
net expectancy statistically/economically collapses
cost permanently exceeds edge
market access/product changes
risk exceeds mandate
```

## 58. Do not retire only because drawdown hurts

Drawdown may be within expected distribution.

Compare actual behavior with pre-defined expectation.

Likewise, do not keep strategy just because “it always comes back”.

## 59. Strategy post-mortem

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

## 60. Incident post-mortem

Operational incident template:

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

No blame language needed; focus system mechanics.

## 61. Experiment/live linkage

Every live strategy version should point to research experiment approved for deployment.

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

Avoid changing model until gap is understood.

## 64. Operational rehearsal

Before scaling, intentionally test:

```text
market data disconnect
broker API disconnect
process restart
order timeout
partial fill
reconciliation mismatch
kill switch
```

A control not rehearsed may fail when needed.

## 65. Recovery criterion

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

If strategy holds weekends:

```text
expected open gap risk
protective order behavior
margin buffer
news monitoring responsibilities
```

must be explicit.

If no weekend holding, verify system actually closes before provider schedule with enough liquidity buffer.

## 67. Scheduled-event mode

Before CPI/FOMC/BOK-type events, risk policy may:

```text
reduce size
block new entries
widen modeled cost assumptions
```

only if strategy spec says so. Do not improvise event rules live.

## 68. Regulation/product-term monitoring

Retail FX terms and access can change.

Maintain review date for:

```text
leverage limits
margin policy
negative-balance treatment
product eligibility
broker legal entity
```

Especially for Korea/Vietnam-specific context, verify current official rules.

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

Avoid sensitive secret/token logging.

## 70. Completion criteria

Project is not complete until you can demonstrate:

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

## Kết thúc project

Sau bốn module, một systematic FX project phải nối được:

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

Đây mới là bridge từ “strategy idea” sang một research/production process có thể kiểm tra.

Liên quan:

- [12 — Trading journal, review and attribution](../12_TRADING_JOURNAL_REVIEW_AND_PERFORMANCE_ATTRIBUTION.md)
- [13 — Advanced FX microstructure](../13_ADVANCED_FX_MICROSTRUCTURE_AND_ORDER_FLOW.md)
- [05 — Execution, brokers, costs and risk](../05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
