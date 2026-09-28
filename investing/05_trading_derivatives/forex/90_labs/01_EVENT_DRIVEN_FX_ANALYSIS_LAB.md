# Lab 01 — Event-Driven FX Phân tích (analysis / 분석)

Mục tiêu của lab là luyện cách phân tích sự kiện vĩ mô mà không kể chuyện ngược từ chart. Bạn phải ghi **kỳ vọng trước sự kiện** trước khi nhìn kết quả.

## Bối cảnh

Chọn một sự kiện có timestamp rõ ràng, ví dụ:

```text
US CPI
FOMC decision / press conference
US payrolls
ECB decision
BOK decision
Korea CPI / exports
Vietnam monetary-policy or FX-management announcement
```

Nếu dùng dữ liệu lịch sử thật, phải lưu nguồn (source / 소스) và timestamp. Nếu dùng trường hợp (case / 사례) giả định, ghi rõ là simulation.

## Bước 1 — Pre-event trạng thái (state / 상태)

Trước bản phát hành (release / 릴리스), ghi:

```text
Event timestamp and timezone
Previous value
Consensus
Range of forecasts if available
Relevant revisions risk
Current policy rate
Expected policy path
Relevant 2Y / front-end yield level
Pair spot level
Recent realized/implied volatility
Positioning proxy if available
Major correlated markets
```

Sau đó viết thị trường (market / 시장) narrative bằng một chuỗi nhân quả (causal chain / 인과 사슬), không quá ba giả thuyết cạnh tranh.

Ví dụ:

```text
If CPI materially > consensus
→ fewer expected Fed cuts
→ front-end US yields rise
→ relative USD carry/rate support increases
→ USD may strengthen
```

Đây chỉ là hypothesis, không phải quy tắc (rule / 규칙).

## Bước 2 — Define surprise before seeing reaction

Đặt threshold trước:

```text
Small surprise
Moderate surprise
Large surprise
```

Nếu có nhiều components, ghi importance hierarchy. Với CPI có thể gồm headline/cốt lõi (core / 핵심)/monthly; với payrolls có thể gồm payroll, unemployment, wages và revisions.

Không được sau sự kiện mới chọn thành phần (component / 컴포넌트) nào “quan trọng nhất” chỉ vì nó khớp với price move.

## Bước 3 — Observe transmission

Sau bản phát hành (release / 릴리스) ghi theo nhiều horizon:

```text
T+1 minute
T+5 minutes
T+30 minutes
T+2 hours
End of day
Next day if relevant
```

Theo dõi:

```text
Front-end yields
Long-end yields
FX spot
Equity index
Gold / oil if relevant
Credit/risk proxy if relevant
Spread/slippage if available
```

Mục tiêu là phân biệt:

```text
Data surprise
→ rates repricing
→ cross-asset confirmation/divergence
→ FX adjustment
```

## Bước 4 — Competing explanations

Nếu FX reaction không theo hypothesis ban đầu, không được kết luận ngay “thị trường (market / 시장) irrational”. Hãy kiểm tra:

```text
Was the surprise already priced?
Did revisions change the interpretation?
Did the other side of the currency pair receive new information?
Did risk-off / funding flow dominate?
Was positioning crowded?
Was the move mostly mechanical flow / fixing / liquidity?
Did guidance dominate the headline decision?
```

## Bước 5 — Thực thi (execution / 실행) reality

Giả sử chiến lược (strategy / 전략) muốn trade ngay sau bản phát hành (release / 릴리스). So sánh:

```text
Signal price
Displayed spread before event
Displayed spread after event
First executable price
Slippage
Stop distance
Position size if volatility doubles
```

Sau đó trả lời liệu edge gross có đủ lớn để tồn tại sau sự kiện (event / 이벤트) thực thi (execution / 실행) chi phí (cost / 비용) hay không.

## Trường hợp (case / 사례) extension — BOK và USD/KRW

Với BOK quyết định (decision / 결정), thêm:

```text
Fed path
Korea growth/inflation
Foreign portfolio flows
Semiconductor/export cycle
Oil/import cost
FX-policy communication
```

Không được dùng một quy tắc (rule / 규칙) kiểu `BOK hike → KRW strong` nếu không phân tích expectation và Fed side.

## Đầu ra bắt buộc

Tạo `fx_event_study.md`:

```text
Event
Pre-event consensus
Pre-event market pricing
Primary hypothesis
Alternative hypotheses
Defined surprise thresholds
Actual release
Rates reaction
FX reaction by horizon
Cross-asset confirmation
Execution conditions
Was hypothesis supported?
What was learned?
What would invalidate the lesson next time?
```

## Tự chấm

Bài đạt khi một người khác có thể đọc phần **pre-event** mà không biết kết quả và thấy rõ bạn đã đặt hypothesis trước, thay vì viết narrative sau khi biết chart.

Đọc lại:

- [04 — Macro drivers, rates, carry and sessions](../04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)
- [08 — Fundamental and event-driven FX analysis](../08_FUNDAMENTAL_AND_EVENT_DRIVEN_FX_ANALYSIS.md)
- [05 — Execution, brokers, costs and risk](../05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
