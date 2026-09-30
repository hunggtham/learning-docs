# 03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX

Một chiến lược (strategy / 전략) có thể đúng ở từng trade nhưng portfolio vẫn nguy hiểm nếu nhiều position thực chất là cùng một factor bet. Mô-đun (module / 모듈) này xây tầng (layer / 계층) biến **tickets → currency legs → factor exposures → portfolio rủi ro (risk / 위험) → P/L attribution**.

Mục tiêu là để hệ thống trả lời được hai câu hỏi khác nhau:

```text
What risks are we carrying now?
Why did the portfolio make or lose money?
```

Nếu không answer được cả hai, rủi ro (risk / 위험) management và research vòng phản hồi (feedback loop / 피드백 루프) đều thiếu.

## 1. Ticket không phải true exposure

Ví dụ:

```text
Long EUR/USD
Long GBP/USD
Short USD/JPY
```

Ba tickets nhưng decomposition:

```text
+EUR -USD
+GBP -USD
-USD +JPY
```

USD short factor xuất hiện ba lần.

Rủi ro (risk / 위험) engine phải aggregate legs thay vì chỉ đếm positions.

## 2. Chuẩn gốc (canonical / 정본) currency-leg biểu diễn (representation / 표현)

Mỗi FX position `A/B` có thể biểu diễn:

```text
Long A/B  → +A, -B
Short A/B → -A, +B
```

Quy mô (scale / 규모) legs theo notional và hiện tại (current / 현재) price để có comparable reporting currency exposure.

## 3. Reporting currency

Chọn một reporting currency, ví dụ USD hoặc KRW.

Mọi exposure/P&L phải có:

```text
native currency
reporting currency
conversion timestamp
conversion rate source
```

Không overwrite bản địa (native / 네이티브) amount sau conversion; giữ cả hai để kiểm tra (audit / 감사).

## 4. Gross và net exposure

Tính:

```text
Gross Exposure = Σ absolute economic exposures
Net Currency Exposure = sum of signed legs by currency
```

Net nhỏ không đồng nghĩa rủi ro (risk / 위험) nhỏ vì gross exposure vẫn tạo:

```text
liquidity risk
margin usage
basis risk
execution cost
```

## 5. Gross leverage
Phần “5. Gross leverage” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
Gross Leverage = Σ|notional_i| / Equity
```

Nhánh học (track / 트랙) phân phối (distribution / 분포) theo thời gian:

```text
median
95th percentile
maximum
```

Một end-of-day snapshot có thể bỏ lỡ intraday leverage spikes.

## 6. Net leverage không đủ

Hai opposing positions có thể giảm net directional exposure nhưng vẫn có:

```text
cross risk
basis risk
financing
spread/slippage
```

Rủi ro (risk / 위험) dashboard nên show cả gross và net.

## 7. Factor buckets

Ngoài currency legs, map positions vào factors tùy chiến lược (strategy / 전략):

```text
Broad USD
Rate differential
Carry
Risk sentiment
Commodity beta
China/global-growth beta
Funding currency
Volatility
```

Factor ánh xạ (mapping / 매핑) có thể model-based hoặc heuristic, nhưng phải versioned.

## 8. Factor loading is conditional

EUR/USD sensitivity to yields không cố định.

Do đó factor beta nên có:

```text
estimation window
regime label
confidence / error
```

Không trình bày estimated beta như vật lý (physical / 물리적) constant.

## 9. Currency exposure bảng (table / 테이블)

Đầu ra (output / 출력) ví dụ:

```text
Currency | Long Equivalent | Short Equivalent | Net | Stress Loss
EUR
USD
JPY
GBP
AUD
KRW
```

Rows phải derive từ positions, không manual spreadsheet nếu hệ thống (system / 시스템) có thể calculate.

## 10. Pair correlation vs currency-factor overlap

Correlation giữa EUR/USD và GBP/USD có thể thay đổi.

Nhưng cả hai structurally contain USD leg.

Factor decomposition cung cấp thông tin (information / 정보) mà mẫu (sample / 표본) correlation có thể bỏ lỡ.

## 11. Covariance ma trận (matrix / 행렬)

Với return véc-tơ (vector / 벡터) `r` và weights `w`:

```text
Portfolio Variance = w' Σ w
```

Useful nhưng phụ thuộc mẫu (sample / 표본).

Store covariance mô hình (model / 모델) phiên bản (version / 버전) và estimation period.

## 12. Stress correlation

Normal correlation thường underestimate crisis clustering.

Compute separately nếu dữ liệu (data / 데이터) đủ:

```text
normal regime correlation
high-volatility correlation
downside correlation
funding-stress correlation
```

Do not assume one covariance ma trận (matrix / 행렬) describes all states.

## 13. Volatility targeting

Mục tiêu (target / 대상) rủi ro (risk / 위험) example:

```text
Position Risk Budget
= Target Volatility / Estimated Instrument Volatility
```

Nhưng cap kích thước (size / 크기) bằng liquidity/margin các ràng buộc (constraints / 제약조건들).

Vol targeting without leverage cap can increase exposure dramatically in calm regime just before volatility jumps.

## 14. Rủi ro (risk / 위험) contribution

Approximate marginal/thành phần (component / 컴포넌트) rủi ro (risk / 위험) giúp biết position nào đóng góp portfolio volatility.

Mục tiêu:

```text
Portfolio weight
≠ Portfolio risk contribution
```

A small position can dominate rủi ro (risk / 위험) if volatility/correlation high.

## 15. Planned mất mát (loss / 손실) vs statistical rủi ro (risk / 위험)

Trade stop-based rủi ro (risk / 위험):

```text
planned loss if stop executes normally
```

Statistical rủi ro (risk / 위험):

```text
distribution-based loss estimate
```

Stress rủi ro (risk / 위험):

```text
loss under specified extreme scenario
```

Store all three; none replaces the others.

## 16. Portfolio heat

Define one practical chỉ số (metric / 지표):

```text
Portfolio Heat = Σ planned stop losses
```

Then enhance with cluster stress:

```text
Correlated Heat = stressed loss if common factor moves and slippage widens
```

Naive heat ignores dùng chung (shared / 공유) USD/carry factor.

## 17. Scenario engine

Scenario đối tượng (object / 객체):

```text
scenario_id
currency shocks
rate shocks
volatility shock
spread multiplier
slippage multiplier
margin-policy shock
notes
```

Apply same scenarios across historical experiments for comparability.

## 18. Deterministic shock examples
Phần “18. Deterministic shock examples” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
USD +5% broad
JPY +8% funding unwind
Oil +20%
US 2Y +100 bp
Risk-off + spread 3x
KRW -10% vs USD
```

Scenarios are not forecasts. They kiểm thử (test / 테스트) survivability.

## 19. Combined scenario

Crisis rarely moves one variable.

Example:

```text
USD +4%
JPY +6%
Gold -5% initially
FX spreads 4x
Margin requirement +50%
```

Combined scenario often reveals hidden fragility.

## 20. Reverse kiểm thử sức chịu tải (stress test / 스트레스 테스트)

Instead of choosing shock first, solve:

```text
What combination causes:
-10% equity
margin level < threshold
or forced liquidation?
```

Reverse stress identifies thất bại (failure / 실패) ranh giới (boundary / 경계).

## 21. VaR

VaR can answer:

```text
Under model assumptions,
what loss threshold corresponds to confidence level X?
```

It cannot answer maximum possible mất mát (loss / 손실).

Store mô hình (model / 모델)/phương thức (method / 메서드):

```text
historical
parametric
Monte Carlo
```

## 22. Expected Shortfall

Expected Shortfall estimates average mất mát (loss / 손실) beyond VaR threshold.

Still depends on dữ liệu (data / 데이터)/mô hình (model / 모델) and may underestimate regime breaks absent from mẫu (sample / 표본).

Use alongside scenario tests.

## 23. Tail events outside mẫu (sample / 표본)

CHF 2015-style discontinuity demonstrates:

```text
Historical distribution
may exclude relevant future regime break
```

Rủi ro (risk / 위험) engine needs tường minh (explicit / 명시적) jump scenarios not just empirical quantiles.

## 24. Margin stress

For each scenario compute:

```text
Equity
Used Margin
Free Margin
Margin Level
Gross Leverage
Positions liquidated under policy
```

Price rủi ro (risk / 위험) and margin rủi ro (risk / 위험) must be simulated together.

## 25. Động (dynamic / 동적) margin chính sách (policy / 정책)

Provider may raise margin during stress.

Scenario:

```text
Margin requirement × 2
without price move
```

can still force deleveraging.

## 26. Liquidity stress

Add:

```text
spread multiplier
slippage multiplier
max executable size reduction
```

A position may be small in notional but hard to exit in stressed thị trường (market / 시장).

## 27. Concentration limits

Possible limits:

```text
max instrument notional
max currency net exposure
max factor exposure
max gross leverage
max planned portfolio heat
max stressed loss
max margin utilization
```

Limits should be chiến lược (strategy / 전략)/account specific, not universal percentages.

## 28. Pre-trade rủi ro (risk / 위험) check

Before thứ tự (order / 순서):

```text
Current portfolio
+ proposed fill
→ projected exposures
→ projected margin
→ projected stress loss
```

Reject if limits breached.

Do not check only position after fill.

## 29. Post-fill check

Actual fill may differ from requested kích thước (size / 크기)/price.

Recompute rủi ro (risk / 위험) using filled quantity immediately.

Partial fill changes hedge ratio.

## 30. Hedge biểu diễn (representation / 표현)

A hedge must have mục tiêu (target / 대상):

```text
hedged factor
hedge instrument
hedge ratio
expected basis risk
carry cost
liquidity
```

Do not label position “hedged” as boolean only.

## 31. Hedge effectiveness

Measure:

```text
Reduction in targeted exposure
Reduction in stress loss
Cost introduced
Residual basis risk
```

A hedge can reduce variance while increasing negative carry.

## 32. P/L attribution kiến trúc (architecture / 아키텍처)

Portfolio P/L should decompose:

```text
price / spot move
carry / financing
spread
commission
slippage
currency conversion
hedge P/L
other fees
```

Then aggregate by:

```text
strategy
instrument
currency
factor
session
event/regime
```

## 33. Gross vs net alpha

Define:

```text
Gross Signal P/L
- implementation costs
- financing
= Net Strategy P/L
```

Research should not lời gọi (call / 호출) gross paper return “alpha”.

## 34. Factor attribution

If portfolio gains because broad USD moves, but chiến lược (strategy / 전략) thesis was pair-specific giá trị (value / 값):

```text
factor attribution reveals mismatch
```

This is crucial for học tập (learning / 학습) whether edge came from intended cơ chế (mechanism / 메커니즘).

## 35. Benchmark attribution

Possible benchmarks:

```text
zero exposure
simple carry basket
broad USD factor
risk-parity FX basket
```

Benchmark depends on chiến lược (strategy / 전략) mục tiêu (objective / 목표).

Do not choose benchmark after seeing hiệu năng (performance / 성능).

## 36. R-multiple attribution

At trade mức (level / 수준):

```text
Realized R = Net P/L / Planned Initial Risk
```

Also store:

```text
Gross R
Cost R
Slippage R
```

This normalizes trades of different sizes.

## 37. MAE/MFE

Store:

```text
Maximum Adverse Excursion
Maximum Favorable Excursion
```

relative to entry and planned R.

Useful for exit research but vulnerable to hindsight overfitting if repeatedly optimized.

## 38. Drawdown attribution

When portfolio hits drawdown, identify:

```text
which strategies
which currencies
which factors
which cost components
```

contributed.

Do not treat drawdown as one number only.

## 39. Correlated losing clusters

Detect periods where multiple strategies lose simultaneously.

This may reveal:

```text
shared hidden factor
regime dependence
liquidity shock
```

Portfolio of strategies is not diversified merely because chiến lược (strategy / 전략) names differ.

## 40. Risk-adjusted metrics

Can report:

```text
Sharpe
Sortino
Calmar
Max Drawdown
Expected Shortfall
```

but always alongside leverage, liquidity and tail scenarios.

## 41. Turnover and sức chứa (capacity / 용량)

Nhánh học (track / 트랙):

```text
turnover
average ticket size
size relative to liquidity proxy
```

A scalable chiến lược (strategy / 전략) should not assume unlimited thực thi (execution / 실행) at top-of-book.

## 42. Exposure by session

Rủi ro (risk / 위험) may cluster around:

```text
Asia
London
New York
rollover
macro-event windows
```

Report exposure before major scheduled events.

## 43. Sự kiện (event / 이벤트) rủi ro (risk / 위험) inventory

At any thời gian (time / 시간) hệ thống (system / 시스템) can danh sách (list / 목록):

```text
positions
next known central-bank event
next macro release
weekend holding
```

This supports event-specific limits.

## 44. Chiến lược (strategy / 전략) virtual books

If broker nets positions but multiple strategies share pair, maintain nội bộ (internal / 내부) virtual books:

```text
strategy_A +50k EUR/USD
strategy_B -20k EUR/USD
broker net +30k
```

Attribution remains possible.

## 45. Allocation of thực thi (execution / 실행) chi phí (cost / 비용)

When orders are netted, need quy tắc (rule / 규칙) to allocate savings/costs among strategies.

Possible:

```text
pro rata by requested quantity
```

Document consistently.

## 46. Allocation of financing

Financing charged to net broker position may differ from sum of virtual chiến lược (strategy / 전략) positions.

Define attribution chính sách (policy / 정책); otherwise strategy-level P/L won't reconcile to account P/L.

## 47. Reconciliation bất biến (invariant / 불변식)

At end of period:

```text
Σ strategy attributed P/L
+ unallocated account adjustments
= account P/L
```

Difference must be zero within rounding tolerance.

## 48. Rủi ro (risk / 위험) snapshot lược đồ (schema / 스키마)

Example:

```text
snapshot_time
account_equity
gross_leverage
used_margin
free_margin
currency_exposures_json
factor_exposures_json
planned_heat
stress_loss_base
stress_loss_severe
```

Store snapshots for later rà soát (review / 검토).

## 49. Scenario kết quả (result / 결과) lược đồ (schema / 스키마)
Phần “49. Scenario kết quả (result / 결과) lược đồ (schema / 스키마)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
scenario_id
snapshot_time
projected_pnl
projected_equity
projected_margin_level
largest_loss_factor
liquidation_flag
```

## 50. Attribution bản ghi (record / 레코드) lược đồ (schema / 스키마)
Phần “50. Attribution bản ghi (record / 레코드) lược đồ (schema / 스키마)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
trade_id
strategy_id
instrument
spot_pnl
carry_pnl
spread_cost
commission
slippage_cost
conversion_effect
net_pnl
factor_tags
```

## 51. Đơn vị (unit / 단위) tests — decomposition

Example:

```text
Long 100k EUR/USD
```

must produce:

```text
+100k EUR economic leg
negative USD leg equal to quote value
```

within defined valuation convention.

## 52. Đơn vị (unit / 단위) tests — aggregation

Long EUR/USD + long GBP/USD should show larger negative USD aggregate than either trade alone.

## 53. Đơn vị (unit / 단위) tests — P/L reconciliation

For known fills and costs:

```text
Gross P/L - costs = Net P/L
```

and sum of chiến lược (strategy / 전략) attribution equals account ledger.

## 54. Stress regression tests

Keep fixed scenarios so mã (code / 코드) changes don't silently alter rủi ro (risk / 위험) calculation.

Example expected outputs can use tolerance ranges.

## 55. Mô hình (model / 모델) thay đổi (change / 변경) quản trị (governance / 거버넌스)

If rủi ro (risk / 위험) mô hình (model / 모델) changes:

```text
risk_model_version++
```

Do not overwrite historical rủi ro (risk / 위험) snapshots with new methodology without label.

## 56. Completion criteria

Reviewer should be able to answer:

```text
Which currencies are we truly long/short?
Which common factors dominate risk?
What loss occurs under severe scenario?
Will margin force liquidation first?
Where did yesterday's P/L actually come from?
Did intended edge or unintended beta generate return?
```

## Deliverables

Create:

```text
currency_exposure_spec.md
factor_model_spec.md
risk_limits.md
stress_scenarios.md
portfolio_risk_report.md
pnl_attribution_spec.md
attribution_report.md
reconciliation_tests.md
```

## Đọc tiếp

→ [04 — Forward Test, Monitoring và Kill Switch](./04_FORWARD_TEST_MONITORING_AND_KILL_SWITCH.md)

Liên quan:

- [11 — Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
- [12 — Journal, review and attribution](../12_TRADING_JOURNAL_REVIEW_AND_PERFORMANCE_ATTRIBUTION.md)
- [03 — Leverage, margin and position sizing](../03_LEVERAGE_MARGIN_POSITION_SIZING.md)
