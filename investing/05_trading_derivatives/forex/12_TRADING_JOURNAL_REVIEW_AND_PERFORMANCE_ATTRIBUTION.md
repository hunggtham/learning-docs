# 12 — Trading journal, review và performance attribution

Journal không phải nơi ghi cảm xúc rời rạc sau mỗi trade. Nó là **research database của quá trình quyết định**. Mục tiêu là tách signal quality, execution quality, sizing, discipline và market regime để biết P/L đến từ đâu.

Mental model:

```text
Decision context
→ planned trade
→ actual execution
→ market path
→ realized outcome
→ attribution
→ process update
```

## 1. Outcome khác process quality

Một trade lời có thể là bad process nếu:

- vi phạm size limit;
- vào lệnh không có thesis;
- may mắn nhờ news bất ngờ.

Một trade lỗ có thể là good process nếu strategy được thực hiện đúng và loss nằm trong expected distribution.

Review phải tách:

```text
Process quality
from
Outcome
```

## 2. Minimum trade record

Mỗi trade nên lưu:

```text
Trade ID
Timestamp
Instrument
Direction
Base units / notional
Entry decision price
Actual fill
Stop / invalidation
Target / exit rule
Planned risk
Actual exit
Fees / spread / slippage
Financing
P/L
Strategy tag
Regime tag
Event tag
```

## 3. Thesis record

Trước trade, viết ngắn:

```text
Observation
Hypothesis
Expected transmission
Catalyst
Invalidation
Main alternative explanation
```

Nếu thesis chỉ được viết sau trade, hindsight bias tăng mạnh.

## 4. Screenshot chỉ là supplement

Chart screenshot hữu ích để reconstruct context nhưng không thay structured fields.

Screenshot không dễ aggregate thống kê hàng trăm trades.

## 5. Strategy tag

Ví dụ:

```text
trend
carry
mean_reversion
event
macro_relative_value
```

Tag phải stable để attribution meaningful.

## 6. Regime tag

Có thể lưu:

- high/low vol;
- trend/range;
- risk-off/normal;
- event-driven;
- policy divergence.

Nếu tag discretionary, cần definition để tránh relabel sau outcome.

## 7. Event tag

Scheduled events:

```text
CPI
FOMC
ECB
BOK
NFP
GDP
PMI
```

Unscheduled events cần ghi timestamp/source.

## 8. Planned vs actual risk

Lưu cả:

```text
planned loss at stop
actual loss
```

Difference có thể đến từ:

- slippage;
- gap;
- manual override;
- size error;
- spread widening.

## 9. R-multiple

Define:

```text
1R = planned initial risk
```

Then:

```text
Trade R = P/L / Initial Risk
```

R giúp compare trades khác lot/account size.

## 10. MAE

**Maximum Adverse Excursion (MAE)** là adverse move lớn nhất trong trade trước exit.

MAE giúp nghiên cứu:

- stop too tight/loose;
- normal noise;
- regime dependence.

Nhưng đừng optimize stop chỉ bằng historical MAE rồi assume future stable.

## 11. MFE

**Maximum Favorable Excursion (MFE)** là favorable move lớn nhất.

MFE có thể giúp xem:

- exit quá sớm;
- target unrealistic;
- trailing-stop behavior.

## 12. Capture ratio

Một metric conceptual:

```text
Captured Profit / MFE
```

Low ratio không tự động bad; trend strategy có thể intentionally give back profit để capture tails.

## 13. Holding time

Track:

```text
minutes/hours/days
```

Performance có thể degrade khi holding longer than hypothesis horizon.

## 14. Entry slippage

```text
Entry Slippage = Actual Fill - Decision/Reference Price
```

Sign convention phải consistent by direction.

Aggregate by pair/session/event.

## 15. Exit slippage

Stop exits thường có worse distribution than take-profit/normal exits.

Nếu average exit slippage high around news, risk model phải update.

## 16. Cost attribution

Tách:

```text
Gross signal P/L
Spread
Commission
Slippage
Financing
Net P/L
```

Nếu cost ăn 70% gross edge, strategy fragile.

## 17. Spot vs carry attribution

Swing/carry strategy cần tách:

```text
spot movement
carry/financing
```

Nếu strategy được gọi “carry” nhưng profit chủ yếu từ directional spot beta, naming/research thesis cần review.

## 18. Currency-factor attribution

Một trade EUR/USD có thể profit vì broad USD weakness chứ không phải EUR-specific thesis.

Tag/ex-post factor analysis giúp phân biệt.

## 19. Execution error tag

Ví dụ:

```text
late_entry
wrong_size
duplicate_order
missed_stop
manual_override
platform_issue
```

Operational errors nên tách khỏi strategy loss.

## 20. Rule violation

Rule violation là binary/structured field, không chỉ narrative.

Ví dụ:

```text
Size limit violated: yes/no
Event rule violated: yes/no
Stop moved wider: yes/no
Unauthorized re-entry: yes/no
```

## 21. Psychology notes dùng để tìm pattern hành vi

Có thể ghi:

- revenge urge;
- fear of missing out;
- hesitation;
- overconfidence.

Nhưng psychological note không nên trở thành explanation thay cho bad strategy economics.

## 22. Review cadence

Một structure:

```text
After trade: factual capture
Weekly: process review
Monthly: statistical attribution
Quarterly: strategy-level research review
```

Không thay strategy sau mỗi losing trade.

## 23. Weekly review

Questions:

```text
Did I follow rules?
Where did execution differ from plan?
Any repeated operational errors?
Any unusual event/slippage?
```

Focus process, not parameter optimization.

## 24. Monthly review

Aggregate:

- expectancy;
- win/loss distribution;
- R distribution;
- MAE/MFE;
- cost;
- performance by strategy/pair/session/regime.

## 25. Rolling metrics

Track rolling:

```text
30-trade expectancy
60-trade hit rate
rolling cost
rolling drawdown
rolling volatility
```

But small windows noisy; avoid overreacting.

## 26. Confidence interval

Point estimate như average R không đủ.

Estimate uncertainty bằng bootstrap/block methods nếu dependence relevant.

## 27. Losing streak

Expected losing streak phụ thuộc win probability và dependence.

Một streak không tự động chứng minh edge gone.

Need compare với backtest/Monte Carlo distribution.

## 28. Drawdown attribution

Break drawdown into:

```text
normal strategy losses
cost deterioration
factor shock
rule violations
operational errors
model drift
```

Different cause → different response.

## 29. Strategy drift

Nếu discretionary implementation dần khác specification, live strategy không còn là backtested strategy.

Journal giúp detect drift.

## 30. Model drift

Signals có thể mất predictive relationship.

Monitor:

- feature distribution;
- signal frequency;
- conditional returns;
- cost;
- regime mix.

## 31. Kill criteria

Define before crisis:

```text
hard risk breach
operational integrity failure
execution cost exceeds threshold
statistical degradation beyond review threshold
structural market change
```

Kill/review criteria không nên chỉ là “lost X trades”.

## 32. Pause vs kill

Pause có thể dùng khi:

- data source broken;
- broker/API issue;
- abnormal spread;
- uncertain contract change.

Kill nghĩa strategy hypothesis/implementation không còn acceptable.

## 33. Re-entry after pause

Need checklist:

```text
root cause resolved
reconciliation complete
data validated
risk reset
small-size validation if needed
```

## 34. Benchmark comparison

Compare live results với:

- backtest expected distribution;
- paper/forward test;
- simple baseline.

Không chỉ absolute profit target.

## 35. Decision journal vs trade journal

Decision journal có thể ghi hypotheses không trade.

Điều này giảm selection bias vì nếu chỉ ghi executed ideas, ta không biết những signals bị bỏ qua hoạt động ra sao.

## 36. Missed trades

Track legitimate signal missed due to operational/human reason.

Nếu exclude missed losers nhưng nhớ missed winners, memory bias lớn.

## 37. Data schema example

```text
trade_id
strategy_id
signal_time
order_time
fill_time
pair
direction
units
entry_ref
entry_fill
stop
exit_fill
planned_R
realized_R
spread_cost
slippage
financing
regime
macro_event
rule_violation
notes
```

Structured schema giúp export/analyze bằng Python/SQL sau này.

## 38. Journal không được tự động tối ưu liên tục

Nếu mỗi tháng thay threshold theo recent winners, process trở thành adaptive overfitting.

Research changes cần versioned experiment riêng.

## 39. Performance attribution hierarchy

```text
Portfolio P/L
→ strategy
→ pair/currency factor
→ spot/carry
→ gross signal
→ execution cost
→ operational deviations
```

Hierarchy giúp biết “kiếm tiền vì cái gì”.

## 40. Good review output

Một review tốt kết thúc bằng:

```text
Observed fact
Interpretation
Uncertainty
Action / no action
Evidence required before change
```

Không phải chỉ “tuần sau trade cẩn thận hơn”.

## 41. Checklist

Bạn cần có thể:

1. Tách outcome khỏi process.
2. Tính R, MAE, MFE.
3. Tách gross P/L và execution costs.
4. Tách spot và carry.
5. Phân loại rule violations.
6. Review theo cadence thay vì từng trade.
7. Phân biệt strategy drift và model drift.
8. Đặt kill/pause criteria.
9. Reproduce performance attribution từ journal data.

## Đọc tiếp

→ [13 — Advanced FX microstructure and order flow](./13_ADVANCED_FX_MICROSTRUCTURE_AND_ORDER_FLOW.md)

## Internal links

- [05 — Execution, brokers, costs and risk](./05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
- [10 — Backtesting and point-in-time data](./10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)
- [11 — Portfolio FX risk](./11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
