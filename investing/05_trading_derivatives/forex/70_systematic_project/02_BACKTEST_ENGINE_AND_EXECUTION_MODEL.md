# 02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Causality trước hiệu năng (performance / 성능)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Bốn timestamp nên tách riêng** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối backtest engine với execution model, để kết quả lịch sử tính cả fill, cost, latency và giới hạn vận hành.

Một backtest engine tốt không phải là hàm `signal → return`. Nó là một **máy trạng thái (state machine / 상태 머신) theo thời gian** mô phỏng những gì chiến lược (strategy / 전략) biết, lệnh nào được tạo, giá nào có thể thực thi, account thay đổi ra sao và chi phí nào phát sinh.

Nếu engine cho phép chiến lược (strategy / 전략) vô tình nhìn future bar, fill tại mid-price không tồn tại, hoặc bỏ qua financing/margin thì kết quả đẹp đến đâu cũng không phải bằng chứng cho edge.

## 1. Causality trước hiệu năng (performance / 성능)

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

Không được cập nhật (update / 업데이트) position trước khi thực thi (execution / 실행) sự kiện (event / 이벤트) xảy ra.

> **Chuyển mạch:** Trong **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **2. Bốn timestamp nên tách riêng** tiếp nhận điểm tựa từ **1. Causality trước hiệu năng (performance / 성능)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Quyết định (decision / 결정) price không phải fill price** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Bốn timestamp nên tách riêng

Một trade có thể có:

```text
signal_timestamp
order_created_timestamp
order_arrival_timestamp
fill_timestamp
```

Với daily chiến lược (strategy / 전략), các timestamp có thể gần nhau. Với event-driven chiến lược (strategy / 전략), chênh lệch milliseconds/seconds có thể material.

Backtest phải define độ trễ (latency / 지연 시간) giả định (assumption / 가정) thay vì implicitly cho `signal_timestamp = fill_timestamp`.

> **Chuyển mạch:** Ở chặng này của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **3. Quyết định (decision / 결정) price không phải fill price** tiếp nhận điểm tựa từ **2. Bốn timestamp nên tách riêng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Executable side** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Quyết định (decision / 결정) price không phải fill price

Lưu ít nhất:

```text
decision_price
arrival_bid
arrival_ask
fill_price
```

Hiện thực (implementation / 구현) shortfall có thể tách:

```text
Decision → Arrival
Arrival → Fill
```

Nếu chỉ lưu final P/L, bạn không biết edge mất ở tín hiệu (signal / 신호) hay thực thi (execution / 실행).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **4. Executable side** tiếp nhận điểm tựa từ **3. Quyết định (decision / 결정) price không phải fill price** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Thứ tự (order / 순서) mô hình (model / 모델) phải tường minh (explicit / 명시적)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Executable side

Long entry bằng thị trường (market / 시장) thứ tự (order / 순서) thường cross ask.

Long exit bằng thị trường (market / 시장) sell thường hit bid.

Short entry thường sell at bid; buy-to-cover thường cross ask.

Do đó:

```text
Buy ≠ mid
Sell ≠ mid
```

Một backtest dùng mid cho cả hai phía đang xóa spread khỏi thị trường (market / 시장).

> **Chuyển mạch:** Trong **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **5. Thứ tự (order / 순서) mô hình (model / 모델) phải tường minh (explicit / 명시적)** tiếp nhận điểm tựa từ **4. Executable side** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Thị trường (market / 시장) thứ tự (order / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Thứ tự (order / 순서) mô hình (model / 모델) phải tường minh (explicit / 명시적)

Tối thiểu hỗ trợ (support / 지원) conceptual states:

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

Không phải mọi chiến lược (strategy / 전략) cần simulate mọi broker giao thức (protocol / 프로토콜), nhưng trạng thái (state / 상태) ngữ nghĩa (semantics / 의미론) phải rõ để sau này nối live hệ thống (system / 시스템) không phải viết lại mô hình tư duy (mental model / 사고 모델).

> **Chuyển mạch:** Ở chặng này của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **6. Thị trường (market / 시장) thứ tự (order / 순서)** tiếp nhận điểm tựa từ **5. Thứ tự (order / 순서) mô hình (model / 모델) phải tường minh (explicit / 명시적)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Limit thứ tự (order / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Thị trường (market / 시장) thứ tự (order / 순서)

Thực thi (execution / 실행) giả định (assumption / 가정) tối thiểu:

```text
Buy market
→ fill at current ask + adverse slippage

Sell market
→ fill at current bid - adverse slippage
```

Slippage có thể stochastic hoặc deterministic theo mô hình (model / 모델), nhưng phải versioned.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **6. Thị trường (market / 시장) thứ tự (order / 순서)** đã nêu tiêu chí phân biệt, còn **7. Limit thứ tự (order / 순서)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **8. Stop thứ tự (order / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Limit thứ tự (order / 순서)

Limit thứ tự (order / 순서) cần hai questions:

```text
Did market become executable at limit?
If yes, was enough liquidity available to fill requested size?
```

Bar-only dữ liệu (data / 데이터) không biết hàng đợi (queue / 큐) position.

Vì vậy nếu dùng OHLC:

```text
Low <= buy_limit
```

không đủ để biết full fill chắc chắn.

Có thể dùng conservative quy tắc (rule / 규칙) như:

```text
price must trade through limit by buffer
```

hoặc assign fill xác suất (probability / 확률), nhưng limitation phải ghi rõ.

> **Chuyển mạch:** Trong **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **7. Limit thứ tự (order / 순서)** đã nêu tiêu chí phân biệt, còn **8. Stop thứ tự (order / 순서)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **9. Stop-limit** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Stop thứ tự (order / 순서)

Stop trigger không đồng nghĩa fill tại stop price.

Simulation:

```text
trigger condition met
→ marketable order created
→ execute against available bid/ask
```

Gap qua stop phải fill tại first modeled executable price, không force fill ở trigger.

> **Chuyển mạch:** Ở chặng này của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **8. Stop thứ tự (order / 순서)** đã nêu tiêu chí phân biệt, còn **9. Stop-limit** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **10. OHLC intrabar ambiguity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Stop-limit

Stop-limit có hai rủi ro (risk / 위험):

```text
Trigger risk
Non-execution risk
```

Nếu price gap beyond limit, position có thể vẫn mở.

Engine phải preserve this rather than silently converting stop-limit into guaranteed stop.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **9. Stop-limit** đã nêu tiêu chí phân biệt, còn **10. OHLC intrabar ambiguity** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **11. Same-bar entry and exit** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. OHLC intrabar ambiguity

Một bar có:

```text
Open = 100
High = 110
Low = 90
Close = 105
```

Nếu chiến lược (strategy / 전략) có stop 95 và mục tiêu (target / 대상) 108, OHLC không cho biết cái nào xảy ra trước.

Các lựa chọn:

```text
Use higher-frequency data
Use conservative ordering
Use explicit intrabar path assumption
Reject ambiguous trades from evaluation
```

Không chọn thứ tự (ordering / 순서) làm equity curve đẹp nhất.

> **Chuyển mạch:** Trong **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **11. Same-bar entry and exit** tiếp nhận điểm tựa từ **10. OHLC intrabar ambiguity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Partial fills** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Same-bar entry and exit

Nếu tín hiệu (signal / 신호) xuất hiện từ close của bar, chiến lược (strategy / 전략) không thể entry ở chính close rồi cũng dùng high/low cùng bar để stop/mục tiêu (target / 대상) như thể đã ở trong thị trường (market / 시장) cả bar.

Define:

```text
Signal computed at close T
→ earliest execution at T+1 open/quote
```

trừ khi dữ liệu (data / 데이터)/sự kiện (event / 이벤트) timing thực sự cho phép khác.

> **Chuyển mạch:** Ở chặng này của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **12. Partial fills** tiếp nhận điểm tựa từ **11. Same-bar entry and exit** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Rejection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

according to thứ tự (order / 순서) chính sách (policy / 정책).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **13. Rejection** tiếp nhận điểm tựa từ **12. Partial fills** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Slippage mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Rejection

Thứ tự (order / 순서) có thể rejected vì:

```text
insufficient margin
invalid size
market closed
price protection
risk limit
instrument unavailable
```

Engine nên bản ghi (record / 레코드) rejection as sự kiện (event / 이벤트), không biến thành silent no-trade.

> **Chuyển mạch:** Trong **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **14. Slippage mô hình (model / 모델)** tiếp nhận điểm tựa từ **13. Rejection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Chi phí (cost / 비용) scenario ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Slippage mô hình (model / 모델)

Một hierarchy đơn giản:

### Mức (level / 수준) 1 — fixed

```text
slippage = constant pips
```

### Mức (level / 수준) 2 — volatility/session-aware

```text
slippage = f(pair, session, volatility)
```

### Mức (level / 수준) 3 — sự kiện (event / 이벤트)/liquidity-aware

```text
slippage = f(spread, volatility, event flag, size, depth proxy)
```

Không cần mô hình (model / 모델) phức tạp hơn dữ liệu (data / 데이터) chất lượng (quality / 품질).

> **Chuyển mạch:** Ở chặng này của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **15. Chi phí (cost / 비용) scenario ma trận (matrix / 행렬)** tiếp nhận điểm tựa từ **14. Slippage mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Spread mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Chi phí (cost / 비용) scenario ma trận (matrix / 행렬)

Mọi chiến lược (strategy / 전략) nên chạy ít nhất:

```text
Base cost
1.5x cost
2x cost
Stress-event cost
```

Nếu edge biến mất ngay ở 1.2x normal chi phí (cost / 비용), chiến lược (strategy / 전략) có little hiện thực (implementation / 구현) margin.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **16. Spread mô hình (model / 모델)** tiếp nhận điểm tựa từ **15. Chi phí (cost / 비용) scenario ma trận (matrix / 행렬)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Commission mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Spread mô hình (model / 모델)

Nếu historical bid/ask có sẵn, dùng observed spread.

Nếu không:

```text
spread_by_pair_session_regime
```

nên conservative hơn một toàn cục (global / 전역) constant.

Store:

```text
spread_model_version
```

trong experiment siêu dữ liệu (metadata / 메타데이터).

> **Chuyển mạch:** Trong **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **17. Commission mô hình (model / 모델)** tiếp nhận điểm tựa từ **16. Spread mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Financing / rollover** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Commission mô hình (model / 모델)

Commission có thể theo:

```text
per notional
per lot
per ticket
minimum fee
```

Không hard-code giả định (assumption / 가정) từ một broker nếu chiến lược (strategy / 전략) mục tiêu (target / 대상) instrument khác.

> **Chuyển mạch:** Ở chặng này của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **18. Financing / rollover** tiếp nhận điểm tựa từ **17. Commission mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Carry attribution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **19. Carry attribution** tiếp nhận điểm tựa từ **18. Financing / rollover** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Account currency conversion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Chiến lược (strategy / 전략) carry chỉ có thể được hiểu nếu attribution riêng.

> **Chuyển mạch:** Trong **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **20. Account currency conversion** tiếp nhận điểm tựa từ **19. Carry attribution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Position đối tượng (object / 객체)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

hoặc direct tỷ lệ (rate / 비율) nếu available.

Conversion phải dùng tỷ lệ (rate / 비율) tại relevant accounting timestamp.

> **Chuyển mạch:** Ở chặng này của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **21. Position đối tượng (object / 객체)** tiếp nhận điểm tựa từ **20. Account currency conversion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Balance và equity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Position đối tượng (object / 객체)

Một position trạng thái (state / 상태) có thể gồm:

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

Không chỉ lưu lot kích thước (size / 크기).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **22. Balance và equity** tiếp nhận điểm tựa từ **21. Position đối tượng (object / 객체)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Margin accounting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Balance và equity

Dùng chung (common / 공통) ngữ nghĩa (semantics / 의미론):

```text
Balance = realized account cash/equity base before open P/L
Equity = Balance + Unrealized P/L
```

Define chính xác (exact / 정확한) ngữ nghĩa (semantics / 의미론) của engine và giữ nhất quán.

> **Chuyển mạch:** Trong **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **23. Margin accounting** tiếp nhận điểm tựa từ **22. Balance và equity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Margin quy tắc (rule / 규칙) is product-specific** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Margin accounting

Tối thiểu:

```text
required_margin(position)
used_margin = Σ position margins after netting rules if applicable
free_margin = equity - used_margin
margin_level = equity / used_margin × 100%
```

Actual broker quy tắc (rule / 규칙) có thể phức tạp hơn.

Engine phải phiên bản (version / 버전) margin chính sách (policy / 정책).

> **Chuyển mạch:** Ở chặng này của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **24. Margin quy tắc (rule / 규칙) is product-specific** tiếp nhận điểm tựa từ **23. Margin accounting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Liquidation / stop-out** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Margin quy tắc (rule / 규칙) is product-specific

Retail FX, CFD và exchange futures có margin mechanics khác nhau.

Do not create one universal formula.

Use giao diện (interface / 인터페이스) concept:

```text
MarginModel
    calculate_initial_margin()
    calculate_maintenance_requirement()
    liquidation_condition()
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **25. Liquidation / stop-out** tiếp nhận điểm tựa từ **24. Margin quy tắc (rule / 규칙) is product-specific** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Portfolio thứ tự (ordering / 순서) during liquidation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Liquidation / stop-out

If modeled retail account reaches stop-out threshold:

```text
risk event triggers
→ liquidation order generated
→ fill through current execution model
```

Không close positions at perfect threshold price.

Liquidation itself may incur adverse slippage.

> **Chuyển mạch:** Trong **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **26. Portfolio thứ tự (ordering / 순서) during liquidation** tiếp nhận điểm tựa từ **25. Liquidation / stop-out** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Effective leverage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Portfolio thứ tự (ordering / 순서) during liquidation

Broker có thể liquidate:

```text
largest loss first
largest margin first
all positions proportionally
```

Quy tắc (rule / 규칙) depends on provider.

If unknown, choose conservative tường minh (explicit / 명시적) giả định (assumption / 가정) and sensitivity-test alternatives.

> **Chuyển mạch:** Ở chặng này của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **27. Effective leverage** tiếp nhận điểm tựa từ **26. Portfolio thứ tự (ordering / 순서) during liquidation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Currency-factor exposure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Effective leverage

At each timestamp:

```text
Gross Leverage = Σ|notional_i| / equity
```

Bản ghi (record / 레코드) thời gian (time / 시간) series.

Drawdown can increase effective leverage even without new trade.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **28. Currency-factor exposure** tiếp nhận điểm tựa từ **27. Effective leverage** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Rủi ro (risk / 위험) check before thứ tự (order / 순서) acceptance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Currency-factor exposure

Engine should expose position legs to rủi ro (risk / 위험) tầng (layer / 계층):

```text
Long EUR/USD
→ +EUR -USD
```

Do not wait until reporting stage to discover all positions are short USD.

> **Chuyển mạch:** Trong **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **29. Rủi ro (risk / 위험) check before thứ tự (order / 순서) acceptance** tiếp nhận điểm tựa từ **28. Currency-factor exposure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Sự kiện (event / 이벤트) sourcing / ledger** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Rủi ro (risk / 위험) check before thứ tự (order / 순서) acceptance

Thứ tự (order / 순서) chuỗi xử lý (pipeline / 파이프라인):

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

> **Chuyển mạch:** Ở chặng này của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **30. Sự kiện (event / 이벤트) sourcing / ledger** tiếp nhận điểm tựa từ **29. Rủi ro (risk / 위험) check before thứ tự (order / 순서) acceptance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Trade ledger vs account ledger** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Sự kiện (event / 이벤트) sourcing / ledger

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

Then reconstruct account trạng thái (state / 상태) from events.

This improves auditability.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **31. Trade ledger vs account ledger** tiếp nhận điểm tựa từ **30. Sự kiện (event / 이벤트) sourcing / ledger** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Deterministic sự kiện (event / 이벤트) thứ tự (order / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Trade ledger vs account ledger

### Trade ledger

Tracks chiến lược (strategy / 전략) vòng đời (lifecycle / 생명주기).

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

> **Chuyển mạch:** Trong **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **32. Deterministic sự kiện (event / 이벤트) thứ tự (order / 순서)** tiếp nhận điểm tựa từ **31. Trade ledger vs account ledger** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Random slippage reproducibility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Deterministic sự kiện (event / 이벤트) thứ tự (order / 순서)

When two events share timestamp, define priority.

Example:

```text
1. market data
2. scheduled macro event
3. signal evaluation
4. order processing
5. financing/accounting event
```

Different thứ tự (ordering / 순서) can thay đổi (change / 변경) kết quả (result / 결과).

Document it.

> **Chuyển mạch:** Ở chặng này của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **33. Random slippage reproducibility** tiếp nhận điểm tựa từ **32. Deterministic sự kiện (event / 이벤트) thứ tự (order / 순서)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Chiến lược (strategy / 전략) giao diện (interface / 인터페이스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Random slippage reproducibility

If stochastic simulation used:

```text
random_seed
```

must be stored.

Run multiple seeds and report phân phối (distribution / 분포), not one lucky simulation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **34. Chiến lược (strategy / 전략) giao diện (interface / 인터페이스)** tiếp nhận điểm tựa từ **33. Random slippage reproducibility** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Mô hình thực thi (execution model / 실행 모델) giao diện (interface / 인터페이스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Chiến lược (strategy / 전략) giao diện (interface / 인터페이스)

Conceptual API:

```text
on_market_event(state) -> proposed_orders
on_fill(fill_event) -> state update
on_timer(timer_event) -> proposed_orders
```

Chiến lược (strategy / 전략) should not directly mutate broker/account ledger.

Separation reduces accidental cheating.

> **Chuyển mạch:** Trong **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **35. Mô hình thực thi (execution model / 실행 모델) giao diện (interface / 인터페이스)** tiếp nhận điểm tựa từ **34. Chiến lược (strategy / 전략) giao diện (interface / 인터페이스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. Financing mô hình (model / 모델) giao diện (interface / 인터페이스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Mô hình thực thi (execution model / 실행 모델) giao diện (interface / 인터페이스)

```text
execute(order, market_state) -> fills/rejection
```

Mô hình thực thi (execution model / 실행 모델) must not truy cập (access / 접근) future thị trường (market / 시장) trạng thái (state / 상태).

> **Chuyển mạch:** Ở chặng này của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **36. Financing mô hình (model / 모델) giao diện (interface / 인터페이스)** tiếp nhận điểm tựa từ **35. Mô hình thực thi (execution model / 실행 모델) giao diện (interface / 인터페이스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Đơn vị (unit / 단위) tests — P/L** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Financing mô hình (model / 모델) giao diện (interface / 인터페이스)

```text
accrue(position, timestamp, calendar) -> cashflow
```

Keeps carry lô-gic (logic / 논리) separate from chiến lược (strategy / 전략) tín hiệu (signal / 신호).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **37. Đơn vị (unit / 단위) tests — P/L** tiếp nhận điểm tựa từ **36. Financing mô hình (model / 모델) giao diện (interface / 인터페이스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. Đơn vị (unit / 단위) tests — spread** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Đơn vị (unit / 단위) tests — P/L

Example bất biến (invariant / 불변식):

```text
Long 100,000 EUR/USD
Entry 1.1000
Exit 1.1010
Gross price P/L = 100 USD
```

Kiểm thử (test / 테스트) long and short, JPY pairs, cross pairs and non-USD account currency.

> **Chuyển mạch:** Trong **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **38. Đơn vị (unit / 단위) tests — spread** tiếp nhận điểm tựa từ **37. Đơn vị (unit / 단위) tests — P/L** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Đơn vị (unit / 단위) tests — margin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Đơn vị (unit / 단위) tests — spread

If no thị trường (market / 시장) move and trader:

```text
buy at ask
immediately sell at bid
```

P/L should be negative by spread plus fees.

If engine returns zero, chi phí (cost / 비용) ngữ nghĩa (semantics / 의미론) are wrong.

> **Chuyển mạch:** Ở chặng này của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **39. Đơn vị (unit / 단위) tests — margin** tiếp nhận điểm tựa từ **38. Đơn vị (unit / 단위) tests — spread** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. Property-based invariants** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Đơn vị (unit / 단위) tests — margin

Create position where:

```text
notional
margin rate
equity
```

are known.

Check used/free margin and liquidation threshold.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **40. Property-based invariants** tiếp nhận điểm tựa từ **39. Đơn vị (unit / 단위) tests — margin** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. Stress replay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. Property-based invariants

Useful invariants:

```text
ask >= bid
filled_qty <= requested_qty unless explicit overfill bug
position after full close = 0
cash reconciliation balances
same seed + inputs = same outputs
```

> **Chuyển mạch:** Trong **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **41. Stress replay** tiếp nhận điểm tựa từ **40. Property-based invariants** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. Survivorship of broker terms** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. Stress replay

Run sự kiện (event / 이벤트) windows like:

```text
CHF 2015
March 2020 USD stress
```

not to optimize chiến lược (strategy / 전략), but to kiểm thử (test / 테스트) whether engine handles:

```text
large gaps
wide spreads
margin stress
```

without impossible fills.

> **Chuyển mạch:** Ở chặng này của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **42. Survivorship of broker terms** tiếp nhận điểm tựa từ **41. Stress replay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. Multi-strategy portfolio** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. Survivorship of broker terms

If backtest retail sản phẩm (product / 제품) across years, hiện tại (current / 현재) margin/financing terms may not equal historical terms.

If historical rules unavailable, disclose giả định (assumption / 가정) and sensitivity-test.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **43. Multi-strategy portfolio** tiếp nhận điểm tựa từ **42. Survivorship of broker terms** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. Same tín hiệu (signal / 신호) from multiple strategies** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. Multi-strategy portfolio

Engine should not run each chiến lược (strategy / 전략) in isolated account then add returns naively if real account shares margin/capital.

Need dùng chung (common / 공통) portfolio/account trạng thái (state / 상태) for:

```text
capital
margin
currency exposure
risk limits
```

> **Chuyển mạch:** Trong **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **44. Same tín hiệu (signal / 신호) from multiple strategies** tiếp nhận điểm tựa từ **43. Multi-strategy portfolio** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **45. Netting vs hedging account chế độ (mode / 모드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. Same tín hiệu (signal / 신호) from multiple strategies

Two strategies may both long EUR/USD.

Decide whether ledger keeps:

```text
separate virtual strategy lots
```

while broker/account net position is combined.

Attribution requires virtual lots even if thực thi (execution / 실행) is netted.

> **Chuyển mạch:** Ở chặng này của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **45. Netting vs hedging account chế độ (mode / 모드)** tiếp nhận điểm tựa từ **44. Same tín hiệu (signal / 신호) from multiple strategies** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **46. Position sizing timing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 45. Netting vs hedging account chế độ (mode / 모드)

Some retail accounts net opposing positions; others represent separate tickets.

Hệ thống (system / 시스템) ngữ nghĩa (semantics / 의미론) must match intended sản phẩm (product / 제품).

Do not assume both long and short EUR/USD can coexist economically without understanding account chế độ (mode / 모드).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **46. Position sizing timing** tiếp nhận điểm tựa từ **45. Netting vs hedging account chế độ (mode / 모드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **47. Volatility targeting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 46. Position sizing timing

Kích thước (size / 크기) should use equity/rủi ro (risk / 위험) trạng thái (state / 상태) **at quyết định (decision / 결정) thời gian (time / 시간)**.

Do not kích thước (size / 크기) all historical trades using final/hiện tại (current / 현재) capital.

> **Chuyển mạch:** Trong **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **47. Volatility targeting** tiếp nhận điểm tựa từ **46. Position sizing timing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **48. Backtest outputs** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 47. Volatility targeting

If kích thước (size / 크기) uses estimated volatility:

```text
vol_estimate_t
```

must only use dữ liệu (data / 데이터) available through `t`.

No future full-sample tiêu chuẩn (standard / 표준) deviation.

> **Chuyển mạch:** Ở chặng này của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **48. Backtest outputs** tiếp nhận điểm tựa từ **47. Volatility targeting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **49. Chi phí (cost / 비용) attribution ratio** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **49. Chi phí (cost / 비용) attribution ratio** tiếp nhận điểm tựa từ **48. Backtest outputs** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **50. Paper chiến lược (strategy / 전략) vs executable chiến lược (strategy / 전략)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 49. Chi phí (cost / 비용) attribution ratio

Useful chỉ số (metric / 지표):

```text
Implementation Cost / Gross Strategy Edge
```

If chi phí (cost / 비용) consumes 80–90% of gross edge, live fragility is high.

> **Chuyển mạch:** Trong **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **50. Paper chiến lược (strategy / 전략) vs executable chiến lược (strategy / 전략)** tiếp nhận điểm tựa từ **49. Chi phí (cost / 비용) attribution ratio** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **51. Lỗi (error / 오류) handling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 50. Paper chiến lược (strategy / 전략) vs executable chiến lược (strategy / 전략)

A paper quy tắc (rule / 규칙) can say:

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

> **Chuyển mạch:** Ở chặng này của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **51. Lỗi (error / 오류) handling** tiếp nhận điểm tựa từ **50. Paper chiến lược (strategy / 전략) vs executable chiến lược (strategy / 전략)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **52. Experiment siêu dữ liệu (metadata / 메타데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 51. Lỗi (error / 오류) handling

Engine should thất bại (fail / 실패) loudly on:

```text
NaN executable price
unknown instrument
missing conversion rate
negative margin
impossible order state
```

Do not silently fill with zero/previous price.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **51. Lỗi (error / 오류) handling** nêu điều cần giải thích; **52. Experiment siêu dữ liệu (metadata / 메타데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **53. Completion criteria** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 52. Experiment siêu dữ liệu (metadata / 메타데이터)

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

> **Chuyển mạch:** Trong **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **52. Experiment siêu dữ liệu (metadata / 메타데이터)** nêu điều cần giải thích; **53. Completion criteria** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Deliverables** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 53. Completion criteria

Mô-đun (module / 모듈) complete when reviewer can dấu vết (trace / 추적) any trade:

```text
Why signal existed
→ what data was known
→ what order was created
→ what executable price was used
→ what costs were charged
→ how margin changed
→ how P/L reached account currency
```

> **Chuyển mạch:** Ở chặng này của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **Deliverables** tiếp nhận điểm tựa từ **53. Completion criteria** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đọc tiếp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Backtest Engine và Mô hình thực thi (execution model / 실행 모델) cho Systematic FX**, **Đọc tiếp** tiếp nhận điểm tựa từ **Deliverables** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Đọc tiếp

→ [03 — Portfolio Risk và Attribution Engine](./03_PORTFOLIO_RISK_AND_ATTRIBUTION_ENGINE.md)

Liên quan:

- [05 — Execution, brokers, costs and risk](../05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
- [10 — Backtesting and point-in-time FX data](../10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)
- [11 — Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)

> **Bàn giao:** Sau **Đọc tiếp**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
