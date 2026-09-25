# 02 — Backtest Engine và Execution Model cho Systematic FX

Một backtest engine tốt không phải là hàm `signal → return`. Nó là một **state machine theo thời gian** mô phỏng những gì strategy biết, lệnh nào được tạo, giá nào có thể thực thi, account thay đổi ra sao và chi phí nào phát sinh.

Nếu engine cho phép strategy vô tình nhìn future bar, fill tại mid-price không tồn tại, hoặc bỏ qua financing/margin thì kết quả đẹp đến đâu cũng không phải bằng chứng cho edge.

## 1. Causality trước performance

Mỗi quyết định phải theo thứ tự:

```text
Market / event data becomes available
→ feature state updates
→ signal is evaluated
→ order is created
→ order reaches execution model
→ fill / rejection / partial fill occurs
→ position and cash ledger update
→ risk is recomputed
```

Không được update position trước khi execution event xảy ra.

## 2. Bốn timestamp nên tách riêng

Một trade có thể có:

```text
signal_timestamp
order_created_timestamp
order_arrival_timestamp
fill_timestamp
```

Với daily strategy, các timestamp có thể gần nhau. Với event-driven strategy, chênh lệch milliseconds/seconds có thể material.

Backtest phải define latency assumption thay vì implicitly cho `signal_timestamp = fill_timestamp`.

## 3. Decision price không phải fill price

Lưu ít nhất:

```text
decision_price
arrival_bid
arrival_ask
fill_price
```

Implementation shortfall có thể tách:

```text
Decision → Arrival
Arrival → Fill
```

Nếu chỉ lưu final P/L, bạn không biết edge mất ở signal hay execution.

## 4. Executable side

Long entry bằng market order thường cross ask.

Long exit bằng market sell thường hit bid.

Short entry thường sell at bid; buy-to-cover thường cross ask.

Do đó:

```text
Buy ≠ mid
Sell ≠ mid
```

Một backtest dùng mid cho cả hai phía đang xóa spread khỏi market.

## 5. Order model phải explicit

Tối thiểu support conceptual states:

```text
CREATED
SENT
ACKNOWLEDGED
PARTIALLY_FILLED
FILLED
CANCELED
REJECTED
EXPIRED
UNKNOWN
```

Không phải mọi strategy cần simulate mọi broker protocol, nhưng state semantics phải rõ để sau này nối live system không phải viết lại mental model.

## 6. Market order

Execution assumption tối thiểu:

```text
Buy market
→ fill at current ask + adverse slippage

Sell market
→ fill at current bid - adverse slippage
```

Slippage có thể stochastic hoặc deterministic theo model, nhưng phải versioned.

## 7. Limit order

Limit order cần hai questions:

```text
Did market become executable at limit?
If yes, was enough liquidity available to fill requested size?
```

Bar-only data không biết queue position.

Vì vậy nếu dùng OHLC:

```text
Low <= buy_limit
```

không đủ để biết full fill chắc chắn.

Có thể dùng conservative rule như:

```text
price must trade through limit by buffer
```

hoặc assign fill probability, nhưng limitation phải ghi rõ.

## 8. Stop order

Stop trigger không đồng nghĩa fill tại stop price.

Simulation:

```text
trigger condition met
→ marketable order created
→ execute against available bid/ask
```

Gap qua stop phải fill tại first modeled executable price, không force fill ở trigger.

## 9. Stop-limit

Stop-limit có hai risk:

```text
Trigger risk
Non-execution risk
```

Nếu price gap beyond limit, position có thể vẫn mở.

Engine phải preserve this rather than silently converting stop-limit into guaranteed stop.

## 10. OHLC intrabar ambiguity

Một bar có:

```text
Open = 100
High = 110
Low = 90
Close = 105
```

Nếu strategy có stop 95 và target 108, OHLC không cho biết cái nào xảy ra trước.

Các lựa chọn:

```text
Use higher-frequency data
Use conservative ordering
Use explicit intrabar path assumption
Reject ambiguous trades from evaluation
```

Không chọn ordering làm equity curve đẹp nhất.

## 11. Same-bar entry and exit

Nếu signal xuất hiện từ close của bar, strategy không thể entry ở chính close rồi cũng dùng high/low cùng bar để stop/target như thể đã ở trong market cả bar.

Define:

```text
Signal computed at close T
→ earliest execution at T+1 open/quote
```

trừ khi data/event timing thực sự cho phép khác.

## 12. Partial fills

Position ledger phải dùng `filled_quantity`, không `requested_quantity`.

Average fill:

```text
VWAP_fill = Σ(price_i × quantity_i) / Σquantity_i
```

Remaining quantity có thể:

```text
stay open
cancel
expire
```

according to order policy.

## 13. Rejection

Order có thể rejected vì:

```text
insufficient margin
invalid size
market closed
price protection
risk limit
instrument unavailable
```

Engine nên record rejection as event, không biến thành silent no-trade.

## 14. Slippage model

Một hierarchy đơn giản:

### Level 1 — fixed

```text
slippage = constant pips
```

### Level 2 — volatility/session-aware

```text
slippage = f(pair, session, volatility)
```

### Level 3 — event/liquidity-aware

```text
slippage = f(spread, volatility, event flag, size, depth proxy)
```

Không cần model phức tạp hơn data quality.

## 15. Cost scenario matrix

Mọi strategy nên chạy ít nhất:

```text
Base cost
1.5x cost
2x cost
Stress-event cost
```

Nếu edge biến mất ngay ở 1.2x normal cost, strategy có little implementation margin.

## 16. Spread model

Nếu historical bid/ask có sẵn, dùng observed spread.

Nếu không:

```text
spread_by_pair_session_regime
```

nên conservative hơn một global constant.

Store:

```text
spread_model_version
```

trong experiment metadata.

## 17. Commission model

Commission có thể theo:

```text
per notional
per lot
per ticket
minimum fee
```

Không hard-code assumption từ một broker nếu strategy target instrument khác.

## 18. Financing / rollover

Position held qua rollover có thể accrue financing.

Engine cần:

```text
financing_rate_long
financing_rate_short
applicable value date
number of days charged
broker/provider markup if modeling retail product
```

Weekends/holidays làm charge nhiều ngày cùng lúc tùy convention.

## 19. Carry attribution

Không trộn financing vào price P/L.

Ledger nên tách:

```text
spot_pnl
financing_pnl
commission
spread_cost
slippage_cost
conversion_pnl
```

Strategy carry chỉ có thể được hiểu nếu attribution riêng.

## 20. Account currency conversion

Trade EUR/GBP tạo P/L bằng GBP.

Nếu account USD:

```text
GBP P/L
→ convert at point-in-time GBP/USD
```

Nếu account KRW:

```text
GBP → USD → KRW
```

hoặc direct rate nếu available.

Conversion phải dùng rate tại relevant accounting timestamp.

## 21. Position object

Một position state có thể gồm:

```text
position_id
instrument
signed_base_units
avg_entry_price
open_time
realized_pnl
unrealized_pnl
financing_accrued
margin_required
strategy_id
```

Không chỉ lưu lot size.

## 22. Balance và equity

Common semantics:

```text
Balance = realized account cash/equity base before open P/L
Equity = Balance + Unrealized P/L
```

Define exact semantics của engine và giữ nhất quán.

## 23. Margin accounting

Tối thiểu:

```text
required_margin(position)
used_margin = Σ position margins after netting rules if applicable
free_margin = equity - used_margin
margin_level = equity / used_margin × 100%
```

Actual broker rule có thể phức tạp hơn.

Engine phải version margin policy.

## 24. Margin rule is product-specific

Retail FX, CFD và exchange futures có margin mechanics khác nhau.

Do not create one universal formula.

Use interface concept:

```text
MarginModel
    calculate_initial_margin()
    calculate_maintenance_requirement()
    liquidation_condition()
```

## 25. Liquidation / stop-out

If modeled retail account reaches stop-out threshold:

```text
risk event triggers
→ liquidation order generated
→ fill through current execution model
```

Không close positions at perfect threshold price.

Liquidation itself may incur adverse slippage.

## 26. Portfolio ordering during liquidation

Broker có thể liquidate:

```text
largest loss first
largest margin first
all positions proportionally
```

Rule depends on provider.

If unknown, choose conservative explicit assumption and sensitivity-test alternatives.

## 27. Effective leverage

At each timestamp:

```text
Gross Leverage = Σ|notional_i| / equity
```

Record time series.

Drawdown can increase effective leverage even without new trade.

## 28. Currency-factor exposure

Engine should expose position legs to risk layer:

```text
Long EUR/USD
→ +EUR -USD
```

Do not wait until reporting stage to discover all positions are short USD.

## 29. Risk check before order acceptance

Order pipeline:

```text
signal
→ proposed order
→ pre-trade risk checks
→ accepted/rejected
→ execution
```

Checks may include:

```text
max position
max currency exposure
max gross leverage
max portfolio heat
margin buffer
max event risk
```

## 30. Event sourcing / ledger

Prefer append-only events conceptually:

```text
QUOTE
SIGNAL
ORDER_CREATED
ORDER_FILLED
FINANCING_CHARGE
MARGIN_UPDATE
ORDER_CANCELED
POSITION_CLOSED
```

Then reconstruct account state from events.

This improves auditability.

## 31. Trade ledger vs account ledger

### Trade ledger

Tracks strategy lifecycle.

### Account ledger

Tracks:

```text
cash
positions
fees
financing
conversion
margin
```

Một trade có thể map nhiều fills và ledger entries.

## 32. Deterministic event order

When two events share timestamp, define priority.

Example:

```text
1. market data
2. scheduled macro event
3. signal evaluation
4. order processing
5. financing/accounting event
```

Different ordering can change result.

Document it.

## 33. Random slippage reproducibility

If stochastic simulation used:

```text
random_seed
```

must be stored.

Run multiple seeds and report distribution, not one lucky simulation.

## 34. Strategy interface

Conceptual API:

```text
on_market_event(state) -> proposed_orders
on_fill(fill_event) -> state update
on_timer(timer_event) -> proposed_orders
```

Strategy should not directly mutate broker/account ledger.

Separation reduces accidental cheating.

## 35. Execution model interface

```text
execute(order, market_state) -> fills/rejection
```

Execution model must not access future market state.

## 36. Financing model interface

```text
accrue(position, timestamp, calendar) -> cashflow
```

Keeps carry logic separate from strategy signal.

## 37. Unit tests — P/L

Example invariant:

```text
Long 100,000 EUR/USD
Entry 1.1000
Exit 1.1010
Gross price P/L = 100 USD
```

Test long and short, JPY pairs, cross pairs and non-USD account currency.

## 38. Unit tests — spread

If no market move and trader:

```text
buy at ask
immediately sell at bid
```

P/L should be negative by spread plus fees.

If engine returns zero, cost semantics are wrong.

## 39. Unit tests — margin

Create position where:

```text
notional
margin rate
equity
```

are known.

Check used/free margin and liquidation threshold.

## 40. Property-based invariants

Useful invariants:

```text
ask >= bid
filled_qty <= requested_qty unless explicit overfill bug
position after full close = 0
cash reconciliation balances
same seed + inputs = same outputs
```

## 41. Stress replay

Run event windows like:

```text
CHF 2015
March 2020 USD stress
```

not to optimize strategy, but to test whether engine handles:

```text
large gaps
wide spreads
margin stress
```

without impossible fills.

## 42. Survivorship of broker terms

If backtest retail product across years, current margin/financing terms may not equal historical terms.

If historical rules unavailable, disclose assumption and sensitivity-test.

## 43. Multi-strategy portfolio

Engine should not run each strategy in isolated account then add returns naively if real account shares margin/capital.

Need common portfolio/account state for:

```text
capital
margin
currency exposure
risk limits
```

## 44. Same signal from multiple strategies

Two strategies may both long EUR/USD.

Decide whether ledger keeps:

```text
separate virtual strategy lots
```

while broker/account net position is combined.

Attribution requires virtual lots even if execution is netted.

## 45. Netting vs hedging account mode

Some retail accounts net opposing positions; others represent separate tickets.

System semantics must match intended product.

Do not assume both long and short EUR/USD can coexist economically without understanding account mode.

## 46. Position sizing timing

Size should use equity/risk state **at decision time**.

Do not size all historical trades using final/current capital.

## 47. Volatility targeting

If size uses estimated volatility:

```text
vol_estimate_t
```

must only use data available through `t`.

No future full-sample standard deviation.

## 48. Backtest outputs

Minimum report:

```text
Experiment metadata
Trade count
Gross P/L
Net P/L
Spread cost
Commission
Slippage
Financing
Conversion effect
Max drawdown
Gross leverage distribution
Margin utilization distribution
Rejected orders
Partial fills
Stress-period performance
```

## 49. Cost attribution ratio

Useful metric:

```text
Implementation Cost / Gross Strategy Edge
```

If cost consumes 80–90% of gross edge, live fragility is high.

## 50. Paper strategy vs executable strategy

A paper rule can say:

```text
buy when x > y
```

Executable spec must also say:

```text
when is x known?
what order is sent?
at which side?
what if no fill?
how much size?
what cost?
what margin?
```

Only latter is deployable research.

## 51. Error handling

Engine should fail loudly on:

```text
NaN executable price
unknown instrument
missing conversion rate
negative margin
impossible order state
```

Do not silently fill with zero/previous price.

## 52. Experiment metadata

Store:

```text
experiment_id
strategy_version
data_version
execution_model_version
cost_model_version
margin_model_version
random_seed
code_commit
config_hash
```

## 53. Completion criteria

Module complete when reviewer can trace any trade:

```text
Why signal existed
→ what data was known
→ what order was created
→ what executable price was used
→ what costs were charged
→ how margin changed
→ how P/L reached account currency
```

## Deliverables

Create:

```text
strategy_spec.md
order_state_machine.md
execution_model.md
cost_model.md
margin_model.md
ledger_schema.md
backtest_report.md
engine_test_cases.md
```

## Đọc tiếp

→ [03 — Portfolio Risk và Attribution Engine](./03_PORTFOLIO_RISK_AND_ATTRIBUTION_ENGINE.md)

Liên quan:

- [05 — Execution, brokers, costs and risk](../05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
- [10 — Backtesting and point-in-time FX data](../10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)
- [11 — Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
