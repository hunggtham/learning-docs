# 12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Kết quả (outcome / 결과) khác tiến trình (process / 프로세스) chất lượng (quality / 품질)** cho thấy đối tượng vận hành qua những bước nào và tạo ra hệ quả gì; sau đó sang **2. Minimum trade bản ghi (record / 레코드)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối trading journal với review và performance attribution, để kết quả giao dịch được tách thành chiến lược, thực thi và hành vi.

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

> **Nối mạch:** Trong **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **1. Kết quả (outcome / 결과) khác tiến trình (process / 프로세스) chất lượng (quality / 품질)** đặt đầu vào cho **2. Minimum trade bản ghi (record / 레코드)**, rồi **3. Thesis bản ghi (record / 레코드)** mở rộng hệ quả hoặc giới hạn liên quan.

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

> **Nối mạch:** Ở chặng này của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **3. Thesis bản ghi (record / 레코드)** nối từ **2. Minimum trade bản ghi (record / 레코드)** sang **4. Screenshot chỉ là supplement**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **4. Screenshot chỉ là supplement** nối từ **3. Thesis bản ghi (record / 레코드)** sang **5. Chiến lược (strategy / 전략) tag**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Screenshot chỉ là supplement

Chart screenshot hữu ích để reconstruct ngữ cảnh (context / 맥락) nhưng không thay structured fields.

Screenshot không dễ aggregate thống kê hàng trăm trades.

> **Nối mạch:** Trong **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **5. Chiến lược (strategy / 전략) tag** nối từ **4. Screenshot chỉ là supplement** sang **6. Regime tag**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **6. Regime tag** nối từ **5. Chiến lược (strategy / 전략) tag** sang **7. Sự kiện (event / 이벤트) tag**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Regime tag

Có thể lưu:

- high/low vol;
- trend/phạm vi (range / 범위);
- risk-off/normal;
- event-driven;
- chính sách (policy / 정책) divergence.

Nếu tag discretionary, cần definition để tránh relabel sau kết quả (outcome / 결과).

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **7. Sự kiện (event / 이벤트) tag** nối từ **6. Regime tag** sang **8. Planned vs actual rủi ro (risk / 위험)**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **8. Planned vs actual rủi ro (risk / 위험)** nối từ **7. Sự kiện (event / 이벤트) tag** sang **9. R-multiple**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **9. R-multiple** nối từ **8. Planned vs actual rủi ro (risk / 위험)** sang **10. MAE**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **10. MAE** nối từ **9. R-multiple** sang **11. MFE**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. MAE

**Maximum Adverse Excursion (MAE)** là adverse move lớn nhất trong trade trước exit.

MAE giúp nghiên cứu:

- stop too tight/loose;
- normal noise;
- regime dependence.

Nhưng đừng optimize stop chỉ bằng historical MAE rồi assume future stable.

> **Nối mạch:** Trong **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **11. MFE** nối từ **10. MAE** sang **12. Capture ratio**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. MFE

**Maximum Favorable Excursion (MFE)** là favorable move lớn nhất.

MFE có thể giúp xem:

- exit quá sớm;
- mục tiêu (target / 대상) unrealistic;
- trailing-stop hành vi (behavior / 동작).

> **Nối mạch:** Ở chặng này của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **12. Capture ratio** nối từ **11. MFE** sang **13. Holding thời gian (time / 시간)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Capture ratio

Một chỉ số (metric / 지표) conceptual:

```text
Captured Profit / MFE
```

Low ratio không tự động bad; trend chiến lược (strategy / 전략) có thể intentionally give back profit để capture tails.

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **13. Holding thời gian (time / 시간)** nối từ **12. Capture ratio** sang **14. Entry slippage**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Holding thời gian (time / 시간)

Nhánh học (track / 트랙):

```text
minutes/hours/days
```

Hiệu năng (performance / 성능) có thể degrade khi holding longer than hypothesis horizon.

> **Nối mạch:** Trong **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **14. Entry slippage** nối từ **13. Holding thời gian (time / 시간)** sang **15. Exit slippage**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Entry slippage

```text
Entry Slippage = Actual Fill - Decision/Reference Price
```

Sign convention phải consistent by direction.

Aggregate by pair/session/sự kiện (event / 이벤트).

> **Nối mạch:** Ở chặng này của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **15. Exit slippage** nối từ **14. Entry slippage** sang **16. Chi phí (cost / 비용) attribution**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Exit slippage

Stop exits thường có worse phân phối (distribution / 분포) than take-profit/normal exits.

Nếu average exit slippage high around news, rủi ro (risk / 위험) mô hình (model / 모델) phải cập nhật (update / 업데이트).

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **16. Chi phí (cost / 비용) attribution** nối từ **15. Exit slippage** sang **17. Spot vs carry attribution**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **17. Spot vs carry attribution** nối từ **16. Chi phí (cost / 비용) attribution** sang **18. Currency-factor attribution**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Spot vs carry attribution

Swing/carry chiến lược (strategy / 전략) cần tách:

```text
spot movement
carry/financing
```

Nếu chiến lược (strategy / 전략) được gọi “carry” nhưng profit chủ yếu từ directional spot beta, naming/research thesis cần rà soát (review / 검토).

> **Nối mạch:** Ở chặng này của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **18. Currency-factor attribution** nối từ **17. Spot vs carry attribution** sang **19. Thực thi (execution / 실행) lỗi (error / 오류) tag**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Currency-factor attribution

Một trade EUR/USD có thể profit vì broad USD weakness chứ không phải EUR-specific thesis.

Tag/ex-post factor phân tích (analysis / 분석) giúp phân biệt.

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **19. Thực thi (execution / 실행) lỗi (error / 오류) tag** nối từ **18. Currency-factor attribution** sang **20. Quy tắc (rule / 규칙) violation**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **20. Quy tắc (rule / 규칙) violation** nối từ **19. Thực thi (execution / 실행) lỗi (error / 오류) tag** sang **21. Psychology notes dùng để tìm mẫu (pattern / 패턴) hành vi**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Quy tắc (rule / 규칙) violation

Quy tắc (rule / 규칙) violation là nhị phân (binary / 이진)/structured trường dữ liệu (field / 필드), không chỉ narrative.

Ví dụ:

```text
Size limit violated: yes/no
Event rule violated: yes/no
Stop moved wider: yes/no
Unauthorized re-entry: yes/no
```

> **Nối mạch:** Ở chặng này của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **21. Psychology notes dùng để tìm mẫu (pattern / 패턴) hành vi** nối từ **20. Quy tắc (rule / 규칙) violation** sang **22. Rà soát (review / 검토) cadence**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Psychology notes dùng để tìm mẫu (pattern / 패턴) hành vi

Có thể ghi:

- revenge urge;
- fear of missing out;
- hesitation;
- overconfidence.

Nhưng psychological ghi chú (note / 노트) không nên trở thành explanation thay cho bad chiến lược (strategy / 전략) economics.

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **22. Rà soát (review / 검토) cadence** nối từ **21. Psychology notes dùng để tìm mẫu (pattern / 패턴) hành vi** sang **23. Weekly rà soát (review / 검토)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Rà soát (review / 검토) cadence

Một cấu trúc (structure / 구조):

```text
After trade: factual capture
Weekly: process review
Monthly: statistical attribution
Quarterly: strategy-level research review
```

Không thay chiến lược (strategy / 전략) sau mỗi losing trade.

> **Nối mạch:** Trong **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **23. Weekly rà soát (review / 검토)** nối từ **22. Rà soát (review / 검토) cadence** sang **24. Monthly rà soát (review / 검토)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Weekly rà soát (review / 검토)

Questions:

```text
Did I follow rules?
Where did execution differ from plan?
Any repeated operational errors?
Any unusual event/slippage?
```

Focus tiến trình (process / 프로세스), not parameter tối ưu hóa (optimization / 최적화).

> **Nối mạch:** Ở chặng này của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **24. Monthly rà soát (review / 검토)** nối từ **23. Weekly rà soát (review / 검토)** sang **25. Rolling metrics**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Monthly rà soát (review / 검토)

Aggregate:

- expectancy;
- win/mất mát (loss / 손실) phân phối (distribution / 분포);
- R phân phối (distribution / 분포);
- MAE/MFE;
- chi phí (cost / 비용);
- hiệu năng (performance / 성능) by chiến lược (strategy / 전략)/pair/session/regime.

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **25. Rolling metrics** nối từ **24. Monthly rà soát (review / 검토)** sang **26. Confidence interval**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **26. Confidence interval** nối từ **25. Rolling metrics** sang **27. Losing streak**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Confidence interval

Điểm (point / 지점) estimate như average R không đủ.

Estimate bất định (uncertainty / 불확실성) bằng bootstrap/khối (block / 블록) methods nếu dependence relevant.

> **Nối mạch:** Ở chặng này của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **27. Losing streak** nối từ **26. Confidence interval** sang **28. Drawdown attribution**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Losing streak

Expected losing streak phụ thuộc win xác suất (probability / 확률) và dependence.

Một streak không tự động chứng minh edge gone.

Need compare với backtest/Monte Carlo phân phối (distribution / 분포).

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **28. Drawdown attribution** nối từ **27. Losing streak** sang **29. Chiến lược (strategy / 전략) drift**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **29. Chiến lược (strategy / 전략) drift** nối từ **28. Drawdown attribution** sang **30. Mô hình (model / 모델) drift**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. Chiến lược (strategy / 전략) drift

Nếu discretionary hiện thực (implementation / 구현) dần khác specification, live chiến lược (strategy / 전략) không còn là backtested chiến lược (strategy / 전략).

Journal giúp detect drift.

> **Nối mạch:** Ở chặng này của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **30. Mô hình (model / 모델) drift** nối từ **29. Chiến lược (strategy / 전략) drift** sang **31. Kill criteria**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. Mô hình (model / 모델) drift

Signals có thể mất predictive relationship.

Monitor:

- tính năng (feature / 기능) phân phối (distribution / 분포);
- tín hiệu (signal / 신호) frequency;
- conditional returns;
- chi phí (cost / 비용);
- regime mix.

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **31. Kill criteria** nối từ **30. Mô hình (model / 모델) drift** sang **32. Pause vs kill**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **32. Pause vs kill** nối từ **31. Kill criteria** sang **33. Re-entry after pause**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. Pause vs kill

Pause có thể dùng khi:

- dữ liệu (data / 데이터) nguồn (source / 소스) broken;
- broker/API issue;
- abnormal spread;
- uncertain đặc tả hợp đồng (contract / 계약) thay đổi (change / 변경).

Kill nghĩa chiến lược (strategy / 전략) hypothesis/hiện thực (implementation / 구현) không còn acceptable.

> **Nối mạch:** Ở chặng này của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **33. Re-entry after pause** nối từ **32. Pause vs kill** sang **34. Benchmark comparison**, vì cơ chế trước tạo đầu vào cho bước sau.

## 33. Re-entry after pause

Need checklist:

```text
root cause resolved
reconciliation complete
data validated
risk reset
small-size validation if needed
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **34. Benchmark comparison** nối từ **33. Re-entry after pause** sang **35. Quyết định (decision / 결정) journal vs trade journal**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. Benchmark comparison

Compare live results với:

- backtest expected phân phối (distribution / 분포);
- paper/forward kiểm thử (test / 테스트);
- simple baseline.

Không chỉ absolute profit mục tiêu (target / 대상).

> **Nối mạch:** Trong **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **35. Quyết định (decision / 결정) journal vs trade journal** nối từ **34. Benchmark comparison** sang **36. Missed trades**, vì cơ chế trước tạo đầu vào cho bước sau.

## 35. Quyết định (decision / 결정) journal vs trade journal

Quyết định (decision / 결정) journal có thể ghi hypotheses không trade.

Điều này giảm selection độ lệch (bias / 편향) vì nếu chỉ ghi executed ideas, ta không biết những signals bị bỏ qua hoạt động ra sao.

> **Nối mạch:** Ở chặng này của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **36. Missed trades** nối từ **35. Quyết định (decision / 결정) journal vs trade journal** sang **37. Dữ liệu (data / 데이터) lược đồ (schema / 스키마) example**, vì cơ chế trước tạo đầu vào cho bước sau.

## 36. Missed trades

Nhánh học (track / 트랙) legitimate tín hiệu (signal / 신호) missed due to operational/human reason.

Nếu exclude missed losers nhưng nhớ missed winners, bộ nhớ (memory / 메모리) độ lệch (bias / 편향) lớn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **36. Missed trades** nêu quy tắc; **37. Dữ liệu (data / 데이터) lược đồ (schema / 스키마) example** thử quy tắc trong tình huống, rồi **38. Journal không được tự động tối ưu liên tục** mở rộng hệ quả.

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

> **Nối mạch:** Trong **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **37. Dữ liệu (data / 데이터) lược đồ (schema / 스키마) example** nêu quy tắc; **38. Journal không được tự động tối ưu liên tục** thử quy tắc trong tình huống, rồi **39. Hiệu năng (performance / 성능) attribution hierarchy** mở rộng hệ quả.

## 38. Journal không được tự động tối ưu liên tục

Nếu mỗi tháng thay threshold theo recent winners, tiến trình (process / 프로세스) trở thành adaptive overfitting.

Research changes cần versioned experiment riêng.

> **Nối mạch:** Ở chặng này của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **39. Hiệu năng (performance / 성능) attribution hierarchy** nối từ **38. Journal không được tự động tối ưu liên tục** sang **40. Good rà soát (review / 검토) đầu ra (output / 출력)**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **40. Good rà soát (review / 검토) đầu ra (output / 출력)** nối từ **39. Hiệu năng (performance / 성능) attribution hierarchy** sang **41. Checklist**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **41. Checklist** nối từ **40. Good rà soát (review / 검토) đầu ra (output / 출력)** sang **Đọc tiếp**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **Đọc tiếp** nối từ **41. Checklist** sang **Nội bộ (internal / 내부) links**, vì cơ chế trước tạo đầu vào cho bước sau.

## Đọc tiếp

→ [13 — Advanced FX microstructure and order flow](./13_ADVANCED_FX_MICROSTRUCTURE_AND_ORDER_FLOW.md)

> **Nối mạch:** Đặt trong câu hỏi lớn của **12 — Trading journal, rà soát (review / 검토) và hiệu năng (performance / 성능) attribution**, **Nội bộ (internal / 내부) links** nối từ **Đọc tiếp** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Nội bộ (internal / 내부) links

- [05 — Execution, brokers, costs and risk](./05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
- [10 — Backtesting and point-in-time data](./10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)
- [11 — Portfolio FX risk](./11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)

> **Bàn giao:** Sau **Nội bộ (internal / 내부) links**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
