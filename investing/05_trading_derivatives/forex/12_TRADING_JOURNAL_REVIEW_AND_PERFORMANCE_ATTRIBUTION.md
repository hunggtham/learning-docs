# 12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution

Journal không phải nơi ghi cảm xúc rời rạc sau mỗi trade. Nó là **research cơ sở dữ liệu (database / 데이터베이스) của quá trình quyết định**. Mục tiêu là tách tín hiệu (signal / 신호) chất lượng (quality / 품질), thực thi (execution / 실행) chất lượng (quality / 품질), sizing, discipline và thị trường (market / 시장) regime để biết P/L đến từ đâu.

Mô hình tư duy (mental model / 사고 모델):

```text
Decision context
→ planned trade
→ actual execution
→ market path
→ realized outcome
→ attribution
→ process update
```

## 1. Kết quả (outcome / 결과) khác tiến trình (process / 프로세스) chất lượng (quality / 품질)

Một trade lời có thể là bad tiến trình (process / 프로세스) nếu:

- vi phạm kích thước (size / 크기) limit;
- vào lệnh không có thesis;
- may mắn nhờ news bất ngờ.

Một trade lỗ có thể là good tiến trình (process / 프로세스) nếu chiến lược (strategy / 전략) được thực hiện đúng và mất mát (loss / 손실) nằm trong expected phân phối (distribution / 분포).

Rà soát (review / 검토) phải tách:

```text
Process quality
from
Outcome
```

## 2. Minimum trade bản ghi (record / 레코드)

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

## 3. Thesis bản ghi (record / 레코드)

Trước trade, viết ngắn:

```text
Observation
Hypothesis
Expected transmission
Catalyst
Invalidation
Main alternative explanation
```

Nếu thesis chỉ được viết sau trade, hindsight độ lệch (bias / 편향) tăng mạnh.

## 4. Screenshot chỉ là supplement

Chart screenshot hữu ích để reconstruct ngữ cảnh (context / 맥락) nhưng không thay structured fields.

Screenshot không dễ aggregate thống kê hàng trăm trades.

## 5. Chiến lược (strategy / 전략) tag

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
- trend/phạm vi (range / 범위);
- risk-off/normal;
- event-driven;
- chính sách (policy / 정책) divergence.

Nếu tag discretionary, cần definition để tránh relabel sau kết quả (outcome / 결과).

## 7. Sự kiện (event / 이벤트) tag

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

Unscheduled events cần ghi timestamp/nguồn (source / 소스).

## 8. Planned vs actual rủi ro (risk / 위험)

Lưu cả:

```text
planned loss at stop
actual loss
```

Difference có thể đến từ:

- slippage;
- gap;
- manual override;
- kích thước (size / 크기) lỗi (error / 오류);
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

R giúp compare trades khác lot/account kích thước (size / 크기).

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
- mục tiêu (target / 대상) unrealistic;
- trailing-stop hành vi (behavior / 동작).

## 12. Capture ratio

Một chỉ số (metric / 지표) conceptual:

```text
Captured Profit / MFE
```

Low ratio không tự động bad; trend chiến lược (strategy / 전략) có thể intentionally give back profit để capture tails.

## 13. Holding thời gian (time / 시간)

Nhánh học (track / 트랙):

```text
minutes/hours/days
```

Hiệu năng (performance / 성능) có thể degrade khi holding longer than hypothesis horizon.

## 14. Entry slippage

```text
Entry Slippage = Actual Fill - Decision/Reference Price
```

Sign convention phải consistent by direction.

Aggregate by pair/session/sự kiện (event / 이벤트).

## 15. Exit slippage

Stop exits thường có worse phân phối (distribution / 분포) than take-profit/normal exits.

Nếu average exit slippage high around news, rủi ro (risk / 위험) mô hình (model / 모델) phải cập nhật (update / 업데이트).

## 16. Chi phí (cost / 비용) attribution

Tách:

```text
Gross signal P/L
Spread
Commission
Slippage
Financing
Net P/L
```

Nếu chi phí (cost / 비용) ăn 70% gross edge, chiến lược (strategy / 전략) fragile.

## 17. Spot vs carry attribution

Swing/carry chiến lược (strategy / 전략) cần tách:

```text
spot movement
carry/financing
```

Nếu chiến lược (strategy / 전략) được gọi “carry” nhưng profit chủ yếu từ directional spot beta, naming/research thesis cần rà soát (review / 검토).

## 18. Currency-factor attribution

Một trade EUR/USD có thể profit vì broad USD weakness chứ không phải EUR-specific thesis.

Tag/ex-post factor phân tích (analysis / 분석) giúp phân biệt.

## 19. Thực thi (execution / 실행) lỗi (error / 오류) tag

Ví dụ:

```text
late_entry
wrong_size
duplicate_order
missed_stop
manual_override
platform_issue
```

Operational errors nên tách khỏi chiến lược (strategy / 전략) mất mát (loss / 손실).

## 20. Quy tắc (rule / 규칙) violation

Quy tắc (rule / 규칙) violation là nhị phân (binary / 이진)/structured trường dữ liệu (field / 필드), không chỉ narrative.

Ví dụ:

```text
Size limit violated: yes/no
Event rule violated: yes/no
Stop moved wider: yes/no
Unauthorized re-entry: yes/no
```

## 21. Psychology notes dùng để tìm mẫu (pattern / 패턴) hành vi

Có thể ghi:

- revenge urge;
- fear of missing out;
- hesitation;
- overconfidence.

Nhưng psychological ghi chú (note / 노트) không nên trở thành explanation thay cho bad chiến lược (strategy / 전략) economics.

## 22. Rà soát (review / 검토) cadence

Một cấu trúc (structure / 구조):

```text
After trade: factual capture
Weekly: process review
Monthly: statistical attribution
Quarterly: strategy-level research review
```

Không thay chiến lược (strategy / 전략) sau mỗi losing trade.

## 23. Weekly rà soát (review / 검토)

Questions:

```text
Did I follow rules?
Where did execution differ from plan?
Any repeated operational errors?
Any unusual event/slippage?
```

Focus tiến trình (process / 프로세스), not parameter tối ưu hóa (optimization / 최적화).

## 24. Monthly rà soát (review / 검토)

Aggregate:

- expectancy;
- win/mất mát (loss / 손실) phân phối (distribution / 분포);
- R phân phối (distribution / 분포);
- MAE/MFE;
- chi phí (cost / 비용);
- hiệu năng (performance / 성능) by chiến lược (strategy / 전략)/pair/session/regime.

## 25. Rolling metrics

Nhánh học (track / 트랙) rolling:

```text
30-trade expectancy
60-trade hit rate
rolling cost
rolling drawdown
rolling volatility
```

But small windows noisy; avoid overreacting.

## 26. Confidence interval

Điểm (point / 지점) estimate như average R không đủ.

Estimate bất định (uncertainty / 불확실성) bằng bootstrap/khối (block / 블록) methods nếu dependence relevant.

## 27. Losing streak

Expected losing streak phụ thuộc win xác suất (probability / 확률) và dependence.

Một streak không tự động chứng minh edge gone.

Need compare với backtest/Monte Carlo phân phối (distribution / 분포).

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

Different cause → different phản hồi (response / 응답).

## 29. Chiến lược (strategy / 전략) drift

Nếu discretionary hiện thực (implementation / 구현) dần khác specification, live chiến lược (strategy / 전략) không còn là backtested chiến lược (strategy / 전략).

Journal giúp detect drift.

## 30. Mô hình (model / 모델) drift

Signals có thể mất predictive relationship.

Monitor:

- tính năng (feature / 기능) phân phối (distribution / 분포);
- tín hiệu (signal / 신호) frequency;
- conditional returns;
- chi phí (cost / 비용);
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

Kill/rà soát (review / 검토) criteria không nên chỉ là “lost X trades”.

## 32. Pause vs kill

Pause có thể dùng khi:

- dữ liệu (data / 데이터) nguồn (source / 소스) broken;
- broker/API issue;
- abnormal spread;
- uncertain đặc tả hợp đồng (contract / 계약) thay đổi (change / 변경).

Kill nghĩa chiến lược (strategy / 전략) hypothesis/hiện thực (implementation / 구현) không còn acceptable.

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

- backtest expected phân phối (distribution / 분포);
- paper/forward kiểm thử (test / 테스트);
- simple baseline.

Không chỉ absolute profit mục tiêu (target / 대상).

## 35. Quyết định (decision / 결정) journal vs trade journal

Quyết định (decision / 결정) journal có thể ghi hypotheses không trade.

Điều này giảm selection độ lệch (bias / 편향) vì nếu chỉ ghi executed ideas, ta không biết những signals bị bỏ qua hoạt động ra sao.

## 36. Missed trades

Nhánh học (track / 트랙) legitimate tín hiệu (signal / 신호) missed due to operational/human reason.

Nếu exclude missed losers nhưng nhớ missed winners, bộ nhớ (memory / 메모리) độ lệch (bias / 편향) lớn.

## 37. Dữ liệu (data / 데이터) lược đồ (schema / 스키마) example

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

Structured lược đồ (schema / 스키마) giúp export/analyze bằng Python/SQL sau này.

## 38. Journal không được tự động tối ưu liên tục

Nếu mỗi tháng thay threshold theo recent winners, tiến trình (process / 프로세스) trở thành adaptive overfitting.

Research changes cần versioned experiment riêng.

## 39. Hiệu năng (performance / 성능) attribution hierarchy

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

## 40. Good rà soát (review / 검토) đầu ra (output / 출력)

Một rà soát (review / 검토) tốt kết thúc bằng:

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

1. Tách kết quả (outcome / 결과) khỏi tiến trình (process / 프로세스).
2. Tính R, MAE, MFE.
3. Tách gross P/L và thực thi (execution / 실행) costs.
4. Tách spot và carry.
5. Phân loại quy tắc (rule / 규칙) violations.
6. Rà soát (review / 검토) theo cadence thay vì từng trade.
7. Phân biệt chiến lược (strategy / 전략) drift và mô hình (model / 모델) drift.
8. Đặt kill/pause criteria.
9. Reproduce hiệu năng (performance / 성능) attribution từ journal dữ liệu (data / 데이터).

## Đọc tiếp

→ [13 — Advanced FX microstructure and order flow](./13_ADVANCED_FX_MICROSTRUCTURE_AND_ORDER_FLOW.md)

## Nội bộ (internal / 내부) links

- [05 — Execution, brokers, costs and risk](./05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
- [10 — Backtesting and point-in-time data](./10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)
- [11 — Portfolio FX risk](./11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
